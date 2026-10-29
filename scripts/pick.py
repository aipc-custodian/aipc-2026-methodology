#!/usr/bin/env python3
"""
pick.py — the gates, with a model choosing instead of a person.

In the ordinary run a person chooses at three gates: which thesis, which
outline, which draft. Those choices are permitted by the competition — they
are selections, not contributions — but they are still a person's judgment
entering the paper. This script takes the person out. It is for the run in
which the human is custodian only.

    --thesis   after the novelty check. The model sees the shortlisted
               theses with their promise and damage scores and what the
               literature search found for each, and chooses one — or says
               none is worth a paper.

        python3 lit_check.py --raw run1/raw.json --top 4 --out lit_top
        python3 pick.py --thesis --raw run1/raw.json --lit lit_top/raw.json \
            --out pick_thesis

    --outline  after the attribution check. The model sees every outline
               with its audit warnings and the attribution verdicts, and
               chooses one.

        python3 pick.py --outline --raw out1/raw.json --attr attr1/raw.json \
            --out pick_outline

    --draft    no call at all. Reads the ranking draft.py --rank already
               asked a second model for, and reports its first choice.

        python3 pick.py --draft --raw drafts1/raw.json --out pick_draft

The shortlist itself needs no judgment from anyone: lit_check.py --top N
takes the N theses highest on promise and lowest on unanswered damage, by
arithmetic.

Each pick is written to pick.md with the model's reasons, and the script
prints the exact command to run next, so nothing is left for you to decide.
A different model from the one that generated the candidates makes the
choice; a generator choosing among its own outputs is the drafter judging
its own criticism again.
"""

import argparse, json, os, sys

from llm import ANTICIPATION_STANDARD, Client, extract_json
from runlog import RunLog

MODEL = "claude-sonnet-5-5"

CRITERIA = """\
  CLARITY           an identifiable thesis, defined terms, a clear structure
                    of reasoning
  ARGUMENTATION     conclusions follow from premises, premises can be
                    adequately defended, serious objections can be met
  SIGNIFICANCE      a worthwhile contribution, a non-trivial conclusion
  ORIGINALITY       something new is contributed
  ENGAGEMENT        the relevant literature is understood
  SCHOLARSHIP       sources fairly represented, prior work acknowledged"""

THESIS_SYSTEM = """\
You are choosing which philosophical thesis will be developed into a
6,000-word paper. You did not write any of them.

For each candidate you are given the thesis, an editor's promise score
(1-5, higher is better), its residual damage after adversarial objection
(0-5, lower is better — the strength of the strongest objection left
unanswered), and what a literature search found: works that ANTICIPATE,
CONTRADICT, SUPPORT or are merely ADJACENT to it.

Choose the one most likely to yield a paper that does well on these
criteria:

""" + CRITERIA + """

""" + ANTICIPATION_STANDARD + """
Apply that standard to the search findings. A thesis that prior work
ENDORSED or FORECLOSED is not original, however promising it looked. A
PRECEDENT (a passing mention, an exploration, a framework) does not count
against originality: developing it is a contribution. The search mostly saw
abstracts and snippets, so a provisional ANTICIPATED is a question to be
settled by reading the source, not a verdict. A thesis that is partly
anticipated may still be the best choice if what remains is worth a paper —
say so; after the sources are read it will be restated to claim only what
is new. If no candidate is worth a paper, say that instead of choosing the
least bad.

Choose; do not improve. Do not reword any thesis or suggest how one could
be strengthened.

Return ONLY JSON:

{
  "choice": the index number of the chosen thesis, or null if none,
  "partly_anticipated": true | false,
  "reason": "two or three sentences: why this one over the others",
  "runner_up": an index number or null,
  "against": [{"index": n, "why_not": "one clause"}]
}
"""

OUTLINE_SYSTEM = """\
You are choosing which outline a 6,000-word philosophy paper will be written
from. Several outlines of the same paper were written independently. You
did not write any of them.

For each you are given the outline, the warnings a mechanical audit raised
against its dependency ledger, and the verdicts of a check on whether each
person it names actually holds the view ascribed to them.

Choose the one most likely to yield a paper that does well on these
criteria:

""" + CRITERIA + """

Weigh the audit: a "bad" flag means the ledger does not close. Weigh the
attribution verdicts: an outline whose argument depends on a position
nobody holds is aimed at nobody. An outline with a failed attribution can
still be chosen if it is otherwise the strongest — it will then be reworked
to replace the positions that failed.

Choose one outline whole. Do not combine outlines, and do not say how any
of them should be changed.

Return ONLY JSON:

{
  "choice": the number of the chosen outline,
  "reason": "two or three sentences: why this one over the others",
  "runner_up": an outline number or null,
  "against": [{"outline": n, "why_not": "one clause"}]
}
"""


def _surviving(r):
    return ((r.get("ruling") or {}).get("surviving_thesis")
            or r.get("thesis") or "").strip()


def pick_thesis(args, client):
    with open(args.raw) as f:
        forge = json.load(f)
    with open(args.lit) as f:
        lit = json.load(f)
    if not isinstance(forge, list) or lit.get("mode") != "novelty":
        sys.exit("--thesis needs --raw (a Forge raw.json) and --lit (a "
                 "lit_check novelty raw.json)")
    by_text = {_surviving(r): i for i, r in enumerate(forge)}
    cands = []
    for res in lit.get("results") or []:
        text = ((res.get("target") or {}).get("thesis") or "").strip()
        if text not in by_text:
            continue
        i = by_text[text]
        ru = forge[i].get("ruling") or {}
        fnd = res.get("finding") or {}
        fnd = {k: v for k, v in fnd.items() if k != "citations"}
        cands.append({"index": i, "thesis": text,
                      "promise": forge[i].get("promise"),
                      "residual_damage": ru.get("residual"),
                      "verdict_after_objection": ru.get("verdict"),
                      "literature_search": fnd})
    if not cands:
        sys.exit("none of the theses in %s could be matched to %s — were "
                 "they run on the same Forge file?" % (args.lit, args.raw))
    txt = client.ask(THESIS_SYSTEM,
                     [{"role": "user", "content": json.dumps(cands, indent=2)}],
                     temperature=0.2, max_tokens=5000, label="pick_thesis")
    got = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:3000]}
    choice = got.get("choice")
    valid = [c["index"] for c in cands]
    nxt = []
    if got.get("error"):
        nxt = ["# the model's answer could not be read — see calls.jsonl"]
    elif choice is None:
        nxt = ["# no thesis chosen. Run the Forge again; do not rescue one."]
    elif choice not in valid:
        nxt = ["# the model named index %r, which was not on the shortlist %s"
               % (choice, valid)]
        got["error"] = "choice not on shortlist"
    else:
        # Sources are read BEFORE restating, so that whether the thesis is
        # anticipated is judged from full texts, not search snippets.
        nxt += ["python3 source_reader.py --raw %s --index %d --lit %s --needs --out needs_%d"
                % (args.raw, choice, args.lit, choice),
                "# fetch the works it lists into sources/, then:",
                "python3 source_reader.py --raw %s --index %d --sources sources/ --out notes_%d"
                % (args.raw, choice, choice),
                "python3 restate.py --raw %s --index %d --lit %s --notes notes_%d/notes.md "
                "--out restate_%d" % (args.raw, choice, args.lit, choice, choice),
                "# if NOTHING NEW REMAINS, pick again; otherwise go on with "
                "--raw restate_%d/raw.json --index 0" % choice]
        src, idx = "restate_%d/raw.json" % choice, 0
        nxt += [
                "python3 outline_deviser.py --raw %s --index %d --notes notes_%d/notes.md "
                "--outlines 6 --out out1" % (src, idx, choice),
                "python3 lit_check.py --raw out1/raw.json --out attr1"]
    return {"gate": "thesis", "candidates": valid, "pick": got,
            "chosen_text": next((c["thesis"] for c in cands
                                 if c["index"] == choice), None)}, nxt


def pick_outline(args, client):
    with open(args.raw) as f:
        state = json.load(f)
    if not isinstance(state, dict) or "outlines" not in state:
        sys.exit("--outline needs --raw to be an Outline Deviser raw.json")
    attr = {}
    if args.attr:
        with open(args.attr) as f:
            attr = json.load(f)
    cands, failed_by = [], {}
    for o in state["outlines"]:
        if o.get("error"):
            continue
        n = o.get("outline")
        tag = "O%s§" % n
        verdicts = []
        for r in attr.get("results") or []:
            a, fd = r.get("address") or {}, r.get("finding") or {}
            where = [w for w in (a.get("where") or []) if w.startswith(tag)]
            if where:
                verdicts.append({"position": a.get("text"), "where": where,
                                 "verdict": fd.get("verdict"),
                                 "what_they_actually_hold":
                                     fd.get("what_they_actually_hold")})
        failed_by[n] = sum(1 for v in verdicts if v["verdict"] in
                           ("DOES NOT HOLD", "DISTORTED", "CANNOT TELL"))
        flags = [{"level": fl.get("level"), "code": fl.get("code"),
                  "text": fl.get("text")}
                 for fl in (o.get("audit") or {}).get("flags") or []
                 if fl.get("level") in ("bad", "warn")]
        cands.append({"outline": n,
                      "content": {k: v for k, v in o.items()
                                  if k not in ("audit", "outline")},
                      "audit_warnings": flags,
                      "attribution_verdicts": verdicts})
    if not cands:
        sys.exit("no usable outlines in %s" % args.raw)
    txt = client.ask(OUTLINE_SYSTEM,
                     [{"role": "user",
                       "content": "THESIS:\n%s\n\nTHE OUTLINES:\n%s"
                                  % (state.get("thesis"), json.dumps(cands, indent=2))}],
                     temperature=0.2, max_tokens=5000, label="pick_outline")
    got = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:3000]}
    choice = got.get("choice")
    valid = [c["outline"] for c in cands]
    notes = (" --notes %s" % args.notes) if args.notes else ""
    if got.get("error"):
        nxt = ["# the model's answer could not be read — see calls.jsonl"]
    elif choice not in valid:
        nxt = ["# the model named outline %r, which is not one of %s" % (choice, valid)]
        got["error"] = "choice not among the outlines"
    elif failed_by.get(choice) and args.attr:
        nxt = ["# the chosen outline has %d failed attribution(s): rework it first"
               % failed_by[choice],
               "python3 outline_deviser.py --raw %s --rework %s --attr %s --out out_rework"
               % (args.raw, choice, args.attr),
               "python3 draft.py --raw out_rework/raw.json --outline 0%s --drafts 3 "
               "--rank --out drafts1" % notes]
    else:
        nxt = ["python3 draft.py --raw %s --outline %s%s --drafts 3 --rank --out drafts1"
               % (args.raw, choice, notes)]
    return {"gate": "outline", "candidates": valid, "pick": got,
            "failed_attributions": failed_by}, nxt


def pick_draft(args):
    with open(args.raw) as f:
        state = json.load(f)
    rk = state.get("ranking") or {}
    order = sorted(rk.get("ranking") or [], key=lambda r: r.get("rank", 99))
    if not order:
        sys.exit("no ranking in %s — run draft.py with --rank" % args.raw)
    choice = order[0].get("draft")
    folder = os.path.dirname(args.raw) or "."
    got = {"choice": choice, "reason": rk.get("recommendation"),
           "runner_up": order[1].get("draft") if len(order) > 1 else None}
    nxt = ["python3 review_round.py --show-prompt   # for the two outside reviewers",
           "python3 review_round.py --paper %s/draft_%s.md --reviews reviews_r1 "
           "--claude-referee claude-fable-5-1%s --out round1"
           % (folder, choice, (" --notes %s" % args.notes) if args.notes else "")]
    return {"gate": "draft", "pick": got,
            "candidates": [r.get("draft") for r in order]}, nxt


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--thesis", action="store_true")
    g.add_argument("--outline", action="store_true")
    g.add_argument("--draft", action="store_true")
    p.add_argument("--raw", required=True)
    p.add_argument("--lit", default=None, help="with --thesis: novelty raw.json")
    p.add_argument("--attr", default=None, help="with --outline: attribution raw.json")
    p.add_argument("--notes", default=None,
                   help="the notes.md path, only so the printed next "
                        "command includes it")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="pick1")
    args = p.parse_args()
    if args.thesis and not args.lit:
        sys.exit("--thesis needs --lit")

    log = RunLog(args.out, __file__, args, globals())
    if args.draft:
        result, nxt = pick_draft(args)
    else:
        client = Client(args.model, log)
        result, nxt = (pick_thesis if args.thesis else pick_outline)(args, client)
    pk = result["pick"]
    log.set("gate", result["gate"])
    log.set("candidates", result["candidates"])
    log.set("choice", pk.get("choice"))
    log.set("chosen_by", "ranking in drafts raw.json" if args.draft else args.model)

    with open(os.path.join(args.out, "raw.json"), "w") as f:
        json.dump(result, f, indent=2)
    lines = ["# Pick: %s" % result["gate"], "",
             "**Chosen:** %s" % pk.get("choice"),
             "**Runner-up:** %s" % pk.get("runner_up"), "",
             "**Reason:** %s" % pk.get("reason"), ""]
    if result.get("chosen_text"):
        lines += ["**Thesis:** %s" % result["chosen_text"], ""]
    for a in pk.get("against") or []:
        lines.append("- not %s: %s" % (a.get("index", a.get("outline")),
                                       a.get("why_not")))
    lines += ["", "## Next", "", "```"] + nxt + ["```"]
    with open(os.path.join(args.out, "pick.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    print("%s gate — chosen: %s   (runner-up: %s)"
          % (result["gate"], pk.get("choice"), pk.get("runner_up")))
    print("reason: %s" % pk.get("reason"))
    print("\nnext:")
    for n in nxt:
        print("  " + n)
    print("\n" + log.summary())


if __name__ == "__main__":
    main()
