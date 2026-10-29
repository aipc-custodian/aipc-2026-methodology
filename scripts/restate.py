#!/usr/bin/env python3
"""
restate.py — narrow a thesis to what is still new. The model does it.

The novelty check often finds that part of a promising thesis has already
been argued. The tempting response is to narrow the thesis yourself. That is
a contribution of content, and it is exactly what the competition rules out:
the claim the paper defends would then be yours.

This script hands the thesis and the novelty findings to a model and asks it
to restate the thesis so that it claims only what is new — or to report that
nothing new remains. Your part is choosing which thesis to send.

The output is a raw.json in the Forge's own format with one thesis in it, so
everything downstream takes it by number exactly as before:

    python3 restate.py --raw run1/raw.json --index 12 --lit lit_12/raw.json \
        --notes notes_12/notes.md --out restate_12

Run it AFTER the source reading, with --notes, so that whether a thesis is
anticipated is judged from full texts and not from search snippets. The
standard for "anticipated" is ANTICIPATION_STANDARD in llm.py.
    python3 outline_deviser.py --raw restate_12/raw.json --index 0 --out out1

Several independent restatements can be asked for with --versions; pick one
by its index.
"""

import argparse, json, os, sys
from concurrent.futures import ThreadPoolExecutor

from llm import ANTICIPATION_STANDARD, Client, extract_json, load_thesis, read_text
from runlog import RunLog

MODEL = "claude-sonnet-4-5"

RESTATE_SYSTEM = """\
You are deciding what a philosophical thesis can still claim, given what a
literature search found and, where available, what a full reading of the
sources found.

""" + ANTICIPATION_STANDARD + """
How to use what you are given:

  - Narrow the thesis ONLY for prior work that meets the standard above
    (ANTICIPATED, ENDORSED or FORECLOSED), and only for the part it meets
    it on. A thesis is not narrowed because someone mentioned, explored or
    framed the idea: that is a PRECEDENT, and the thesis keeps its claim and
    credits the work.
  - Where READING NOTES are given, they come from the full text and
    override the search findings, which mostly rest on abstracts and
    snippets. A search finding of ANTICIPATED marked provisional, or based
    on less than the full text, is not by itself a reason to narrow; if the
    reading notes do not confirm it, treat it as a PRECEDENT.
  - CONTRADICTED findings may require narrowing if the contrary argument is
    sound, or may simply be rivals the paper must answer. Say which.

Restate the thesis so that it claims only what the standard leaves open. The
restated thesis must still be a claim someone could be wrong about, and it
must still be worth a paper. Do not shrink it into safety: a thesis that
survives only by claiming almost nothing is dead, and you should say so
instead.

If nothing meets the standard, return the thesis unchanged. If the standard
is met for the whole of it, say that nothing new remains.

Work only from what you are given. Do not add claims about the literature
from memory.

Return ONLY JSON:

{
  "status": "UNCHANGED" | "NARROWED" | "NOTHING NEW REMAINS",
  "thesis": "the thesis as it should now be stated, one or two sentences, \
or null if nothing new remains",
  "given_up": "what the original claimed that meets the standard, which \
work meets it, and whether ENDORSED or FORECLOSED — or null",
  "still_new": "what is left that no work meets the standard for",
  "credit": ["precedents the paper develops and must credit: Author Year \
— what they suggested"],
  "target": "whose view or which shared assumption the restated thesis is \
aimed at"
}
"""

RESTATE_USER = """\
THESIS:
{thesis}

WHAT THE LITERATURE SEARCH FOUND:
{findings}
{notes}"""


def findings_for(lit_path, thesis):
    with open(lit_path) as f:
        lit = json.load(f)
    if lit.get("mode") != "novelty":
        sys.exit("%s is not a novelty run of lit_check.py" % lit_path)
    hits = [r for r in lit.get("results") or []
            if ((r.get("target") or {}).get("thesis") or "").strip() == thesis]
    if not hits:
        sys.exit("no novelty findings for that thesis in %s — run\n"
                 "  python3 lit_check.py --raw <forge raw.json> --index N\n"
                 "on the same thesis first" % lit_path)
    keep = {"findings": hits[0].get("finding")}
    sep = lit.get("sep")
    if sep:
        keep["encyclopedia_entries_read_in_full"] = sep
    return json.dumps(keep, indent=2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", required=True, help="a Forge raw.json")
    p.add_argument("--index", type=int, required=True)
    p.add_argument("--lit", required=True,
                   help="the lit_check novelty raw.json for that thesis")
    p.add_argument("--notes", default=None,
                   help="source_reader.py notes.md for this thesis; full-text "
                        "readings override the search findings")
    p.add_argument("--versions", type=int, default=1,
                   help="independent restatements to ask for")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="restate1")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    t = load_thesis(args.raw, args.index)
    findings = findings_for(args.lit, t["thesis"])
    notes = ""
    if args.notes:
        notes = ("\nREADING NOTES (from the full texts; these override the "
                 "search findings):\n%s\n" % read_text(args.notes))
    if args.dry_run:
        print("thesis: %s" % t["thesis"][:140])
        print("reading notes: %s" % (args.notes or "none — search findings only"))
        print("%d API call(s), no search — the findings are already in hand."
              % args.versions)
        return

    log = RunLog(args.out, __file__, args, globals())
    client = Client(args.model, log)
    log.set("original_thesis", t["thesis"])
    log.set("reading_notes", args.notes)

    def one(i):
        txt = client.ask(RESTATE_SYSTEM,
                         [{"role": "user",
                           "content": RESTATE_USER.format(thesis=t["thesis"],
                                                          findings=findings,
                                                          notes=notes)}],
                         temperature=0.7 if args.versions > 1 else 0.3,
                         max_tokens=4000, label="restate")
        return extract_json(txt) or {"status": "UNPARSEABLE", "raw_text": txt[:2000]}

    with ThreadPoolExecutor(max_workers=4) as ex:
        got = list(ex.map(one, range(args.versions)))

    # Forge-shaped, so --raw/--index work downstream unchanged.
    forge_like = []
    for g in got:
        forge_like.append({
            "thesis": g.get("thesis") or "",
            "target": g.get("target"),
            "sketch": None, "move_type": None, "risk": None,
            "promise": None,
            "ruling": {"verdict": "restated", "surviving_thesis": None},
            "transcript": [],
            "restated_from": t["thesis"],
            "restate_status": g.get("status"),
            "given_up": g.get("given_up"),
            "still_new": g.get("still_new"),
            "credit": g.get("credit"),
        })
    with open(os.path.join(args.out, "raw.json"), "w") as f:
        json.dump(forge_like, f, indent=2)

    lines = ["# Restatement", "", "**Original thesis:** %s" % t["thesis"], ""]
    for i, g in enumerate(got):
        lines += ["## Index %d — %s" % (i, g.get("status")), "",
                  "**Thesis now:** %s" % (g.get("thesis") or "—"), "",
                  "**Given up (meets the anticipation standard):** %s" % (g.get("given_up") or "—"), "",
                  "**Still new:** %s" % (g.get("still_new") or "—"), "",
                  "**Credit (precedents developed):** %s"
                  % ("; ".join(g.get("credit") or []) or "—"), ""]
    with open(os.path.join(args.out, "restated.md"), "w") as f:
        f.write("\n".join(lines))

    for i, g in enumerate(got):
        print("  [%d] %-20s %s" % (i, g.get("status"), (g.get("thesis") or "")[:90]))
    log.set("statuses", [g.get("status") for g in got])
    print(log.summary())
    print("open %s" % os.path.join(args.out, "restated.md"))
    print("If the status is NOTHING NEW REMAINS, pick another thesis. "
          "Do not rescue this one.")


if __name__ == "__main__":
    main()
