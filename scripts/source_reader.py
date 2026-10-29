#!/usr/bin/env python3
"""
source_reader.py — the sources, read in full, for their bearing on the thesis.

Two findings from the first paper are behind this script. Recall cannot
establish what a paper argues; and confirming that a reference exists is not
reading it — the drafter once retrieved a paper to check one quotation and
missed that the paper anticipated its thesis.

Two steps. You fetch the files in between; that is the whole of your part.

    Step 1  NEEDS   the model says which works it needs to read in full to
                    argue the thesis responsibly. It chooses; you do not.

        python3 source_reader.py --raw run1/raw.json --index 12 \
            --lit lit_12/raw.json --needs --out needs_12

    (now put those PDFs — or .txt / .md files — in a folder, e.g. sources/)

    Step 2  READ    one call per source, the whole file in the prompt. For
                    each: what it argues, what bears on the thesis, whether
                    it anticipates it, and quotations with page numbers that
                    a drafter can rely on.

        python3 source_reader.py --raw run1/raw.json --index 12 \
            --sources sources/ --out notes_12

notes.md is what the Deviser (--notes) and the drafter (--notes) are given.

Supplying a work the model asked for is permitted by the competition.
Choosing its reading for it is not — so if you add a file it did not ask
for, the log records that, and you should say so in the methodology report.
A PDF over about 100 pages will be refused by the API: supply the relevant
chapter instead.
"""

import argparse, json, os, sys
from concurrent.futures import ThreadPoolExecutor

from llm import (ANTICIPATION_STANDARD, Client, extract_json, load_thesis, pdf_block, read_text,
                 source_files)
from runlog import RunLog

MODEL = "claude-sonnet-4-5"

NEEDS_SYSTEM = """\
You are preparing to write a philosophy paper defending a thesis. Before
anyone writes, the relevant sources will be read in full. Your job is to say
WHICH sources.

List the works that must be read in full to argue this thesis responsibly:
the works the thesis is aimed at, the works closest to anticipating it, and
the works any referee would expect the paper to have understood. Include
every work the literature search marked ANTICIPATED, and any marked
provisional: whether they really anticipate the thesis can only be settled
from the full text. Prefer primary texts to summaries of them. Be selective — eight works read properly
are worth more than thirty skimmed.

SEARCH to confirm that each work exists and to get its full citation. Do not
list a work from memory alone.

Return ONLY JSON:

{
  "works": [
    {"citation": "full citation",
     "why": "one sentence: what the paper needs from it",
     "priority": "ESSENTIAL" | "USEFUL",
     "url": "a URL where it can be found, or null",
     "open_access": true | false | null}
  ]
}
"""

NEEDS_USER = """\
THESIS:
{thesis}

{extra}
"""

READ_SYSTEM = """\
You are reading one source in full, for a philosopher who is about to argue
a thesis and must not misrepresent this source or miss that it got there
first.

""" + ANTICIPATION_STANDARD + """
You have the full text, so judge extent and endorsement directly. A
sentence, footnote or aside that raises the thesis is a PRECEDENT, however
close its wording; it anticipates the thesis only if it meets the standard.

Read the whole document before you answer. Report what it SAYS, not what a
work of this kind usually says, and not what you remember of it.

Return ONLY JSON:

{
  "citation": "full citation, from the document itself",
  "argues": "three or four sentences: the work's own thesis and how it \
argues for it",
  "bearing": "what in this work bears on the thesis you were given — \
claims, distinctions, cases, arguments — each with a page or section \
reference",
  "relation": "ANTICIPATES" | "PARTLY ANTICIPATES" | "PRECEDENT" | \
"CONTRADICTS" | "SUPPORTS" | "ADJACENT",
  "grade": "for ANTICIPATES or PARTLY ANTICIPATES: ENDORSED | FORECLOSED; \
for PRECEDENT: PASSING | ENTERTAINED | FRAMEWORK; otherwise null",
  "relation_note": "for ANTICIPATES, PARTLY ANTICIPATES or PRECEDENT: \
exactly what it says, where (pages), how extensively, whether the author \
endorses it, and what it leaves unsaid",
  "holds": "the positions this author actually commits to that someone \
arguing the thesis might be tempted to misstate, stated carefully",
  "quotations": [
    {"text": "a passage copied EXACTLY, character for character",
     "where": "page or section",
     "use": "what it could be quoted to show"}
  ],
  "read_in_full": true | false,
  "caveat": "anything that limits this report: a draft rather than the \
published version, missing pages, an unreadable scan — or null"
}

Quotations must be exact. If you cannot copy a passage exactly, do not
offer it as a quotation.
"""

READ_USER = """\
THESIS (the claim that will be argued — you are not evaluating it):
{thesis}

The source is attached. Read all of it, then report.
"""


def needs(args, client, t):
    extra = []
    if t.get("target"):
        extra.append("What the thesis is aimed at:\n%s" % t["target"])
    # Several novelty checks on the same thesis can be given. Searches are
    # not deterministic, so each finds sources the others miss; the reading
    # list should draw on all of them.
    lits = args.lit or []
    for k, path in enumerate(lits, 1):
        with open(path) as f:
            lit = json.load(f)
        hits = [r for r in lit.get("results") or []
                if ((r.get("target") or {}).get("thesis") or "").strip() == t["thesis"]]
        if hits:
            label = ("What a literature search has already found"
                     if len(lits) == 1 else
                     "What literature search %d of %d found (%s)"
                     % (k, len(lits), os.path.basename(os.path.dirname(path)) or path))
            extra.append("%s:\n%s" % (label, json.dumps(hits[0].get("finding"), indent=2)))
        else:
            print("  note: no findings for this thesis in %s" % path, file=sys.stderr)
    for path in (args.external or []):
        extra.append(
            "An independent literature search by a different AI system, pasted "
            "verbatim (%s). Treat its claims about the literature as leads to "
            "confirm by search, not as facts; it may be wrong about what a "
            "work says or whether it exists:\n%s"
            % (os.path.basename(path), read_text(path)))
    if len(lits) > 1 or (lits and args.external):
        extra.append("These searches were run independently and found "
                     "different sources. Consider every source any of them "
                     "found. Where they label the same work differently, the "
                     "label is not your concern here: list the work if it must "
                     "be read, so the reading can settle it.")
    txt = client.ask(NEEDS_SYSTEM,
                     [{"role": "user",
                       "content": NEEDS_USER.format(thesis=t["thesis"],
                                                    extra="\n\n".join(extra))}],
                     temperature=0.3, max_tokens=8000, search=True,
                     max_uses=args.max_uses, label="needs")
    got = extract_json(txt) or {"works": [], "raw_text": txt[:4000]}
    works = got.get("works") or []
    with open(os.path.join(args.out, "raw.json"), "w") as f:
        json.dump({"mode": "needs", "thesis": t["thesis"], "works": works}, f, indent=2)
    lines = ["# Works to be read in full", "", "**Thesis:** %s" % t["thesis"], "",
             "Fetch these and put the files in one folder. Add nothing the "
             "list does not ask for.", ""]
    for w in sorted(works, key=lambda w: w.get("priority") != "ESSENTIAL"):
        lines.append("- [ ] **%s** — %s  \n  %s%s%s"
                     % (w.get("priority", "?"), w.get("citation"),
                        w.get("why") or "",
                        ("  \n  " + w["url"]) if w.get("url") else "",
                        "  (open access)" if w.get("open_access") else ""))
    with open(os.path.join(args.out, "needs.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    client.log.set("works_requested", len(works))
    print("%d works requested." % len(works))
    print("open %s" % os.path.join(args.out, "needs.md"))


def read_one(client, t, path):
    name = os.path.basename(path)
    if path.lower().endswith(".pdf"):
        blocks = [pdf_block(path)]
    else:
        blocks = [{"type": "text",
                   "text": "SOURCE FILE: %s\n\n%s" % (name, read_text(path))}]
    blocks.append({"type": "text", "text": READ_USER.format(thesis=t["thesis"])})
    try:
        txt = client.ask(READ_SYSTEM, [{"role": "user", "content": blocks}],
                         temperature=0.2, max_tokens=12000, label="read:" + name)
    except Exception as e:
        return {"file": name, "error": str(e)[:400]}
    got = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:4000]}
    got["file"] = name
    return got


def read(args, client, t):
    files = source_files(args.sources)
    if not files:
        sys.exit("no .pdf, .txt or .md files in %s" % args.sources)
    print("reading %d sources in full, one call each…" % len(files))
    with ThreadPoolExecutor(max_workers=3) as ex:
        notes = list(ex.map(lambda p: read_one(client, t, p), files))
    for n in notes:
        print("  %-44s %s" % (n["file"][:44],
                              n.get("relation") or ("FAILED: " + str(n.get("error"))[:60])))
    with open(os.path.join(args.out, "raw.json"), "w") as f:
        json.dump({"mode": "read", "thesis": t["thesis"], "notes": notes}, f, indent=2)

    lines = ["# Reading notes", "", "**Thesis:** %s" % t["thesis"], "",
             "Each source below was read in full by a model with the whole "
             "file in its prompt. Quotations were copied by that reader and "
             "should still be checked against the source before submission.", ""]
    order = {"ANTICIPATES": 0, "PARTLY ANTICIPATES": 1, "CONTRADICTS": 2,
             "PRECEDENT": 3, "SUPPORTS": 4, "ADJACENT": 5}
    for n in sorted(notes, key=lambda n: order.get(n.get("relation"), 9)):
        if n.get("error"):
            lines += ["## %s" % n["file"], "", "NOT READ: %s" % n["error"], ""]
            continue
        lines += ["## %s" % (n.get("citation") or n["file"]), "",
                  "*File: %s — relation to the thesis: %s%s*"
                  % (n["file"], n.get("relation"),
                     (" · %s" % n["grade"]) if n.get("grade") else ""), "",
                  "**Argues.** %s" % n.get("argues"), "",
                  "**Bearing on the thesis.** %s" % n.get("bearing"), ""]
        if n.get("relation_note"):
            lines += ["**What it says on the thesis.** %s" % n["relation_note"], ""]
        lines += ["**Actually holds.** %s" % n.get("holds"), ""]
        for q in n.get("quotations") or []:
            lines.append("> \"%s\" (%s) — %s" % (q.get("text"), q.get("where"),
                                                  q.get("use")))
            lines.append("")
        if n.get("caveat"):
            lines += ["**Caveat.** %s" % n["caveat"], ""]
    with open(os.path.join(args.out, "notes.md"), "w") as f:
        f.write("\n".join(lines))

    damaging = [n for n in notes
                if n.get("relation") in ("ANTICIPATES", "PARTLY ANTICIPATES")]
    client.log.set("sources_read", len([n for n in notes if not n.get("error")]))
    client.log.set("source_files", [os.path.basename(p) for p in files])
    client.log.set("anticipating_sources", [n.get("file") for n in damaging])
    client.log.set("precedent_sources",
                   [n.get("file") for n in notes if n.get("relation") == "PRECEDENT"])
    if damaging:
        print("\n%d source(s) meet the anticipation standard at least in part."
              % len(damaging))
    print("Next: restate.py with --notes %s, which decides from these "
          "readings whether the thesis must narrow. Do not narrow it yourself."
          % os.path.join(args.out, "notes.md"))
    print("open %s" % os.path.join(args.out, "notes.md"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", required=True,
                   help="a Forge, restate.py or Deviser raw.json")
    p.add_argument("--index", type=int, default=None)
    p.add_argument("--needs", action="store_true",
                   help="step 1: ask which works must be read")
    p.add_argument("--lit", action="append", default=None,
                   help="with --needs: a novelty raw.json; repeat --lit to give several "
                        "checks of the same thesis. The list can "
                        "include what the search already turned up")
    p.add_argument("--external", action="append", default=None,
                   help="with --needs: a reply from another model's priority "
                        "check (e.g. ChatGPT), saved unedited; repeatable")
    p.add_argument("--sources", default=None,
                   help="step 2: a folder of .pdf / .txt / .md files to read")
    p.add_argument("--max-uses", type=int, default=10)
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="notes1")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if not args.needs and not args.sources:
        sys.exit("give --needs (step 1) or --sources FOLDER (step 2)")
    t = load_thesis(args.raw, args.index)
    if args.dry_run:
        print("thesis: %s" % t["thesis"][:140])
        if args.needs:
            print("1 API call with search.")
        else:
            fs = source_files(args.sources)
            print("%d sources, one call each, the whole file in the prompt. "
                  "PDFs cost roughly 1,500-3,000 tokens a page." % len(fs))
            for f in fs:
                print("  - %s (%.1f MB)" % (os.path.basename(f),
                                            os.path.getsize(f) / 1e6))
        return

    log = RunLog(args.out, __file__, args, globals())
    client = Client(args.model, log)
    log.set("thesis", t["thesis"])
    if args.needs:
        needs(args, client, t)
    else:
        read(args, client, t)
    print(log.summary())


if __name__ == "__main__":
    main()
