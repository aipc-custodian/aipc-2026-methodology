#!/usr/bin/env python3
"""
draft.py — several isolated drafts of the paper, from one outline.

The pipeline's governing principle is that variance is the product: generate
in isolation, then select. The first paper broke that rule at the drafting
stage — one drafter, one draft, revised serially — so the gate of selection
among finished drafts had a single candidate. This restores it.

    Stage 1  DRAFT   N isolated drafts, blind to each other, each with the
                     outline, the reading notes, and web search to verify
                     what it cites.
    Stage 2  COUNT   pure Python. Words that count toward the limit.
    Stage 3  RANK    optional, one call, a DIFFERENT model: the drafts in
                     order against the competition's published criteria,
                     with reasons. A recommendation only. You pick.

Run through the API, a drafter has no memory of you and no access to earlier
conversations. That is the point of doing this here rather than in the app.

    python3 draft.py --raw out1/raw.json --outline 3 --notes notes_12/notes.md \
        --drafts 3 --out drafts1

The outline is chosen by its number in the Deviser's raw.json. A merged or
reworked outline lives in its own raw.json as outline 0.

There is no voice model and no way to give one. The essay has to be
anonymous, and style is not graded.
"""

import argparse, json, os, sys
from concurrent.futures import ThreadPoolExecutor

from llm import Client, extract_json, read_text, split_refs, tagged, word_count
from runlog import RunLog

MODEL = "claude-opus-5-5"
RANK_MODEL = "claude-sonnet-5-5"

DRAFT_SYSTEM = """\
You are a philosopher writing a journal article. You have an outline that
fixes the thesis and the structure of the argument, and reading notes made
by someone who read the sources in full.

Write the essay the outline describes.

  - Argue for the thesis exactly as stated. Do not soften it.
  - Follow the outline's argument. Where the outline names its widest gap,
    do the work to cross it; do not write around it.
  - Make premises and conclusions explicit. Define your terms.
  - Take up the most serious objections where they arise, and answer them.
  - The cases, examples, distinctions, objections and replies are yours to
    devise. Nobody will supply them.
  - Use a neutral academic register. Write nothing autobiographical and
    nothing that could identify an author: no names, institutions,
    acknowledgements, or references to "my earlier work".

On sources:
  - Cite only works that appear in the reading notes or that you have
    verified by search. Do not cite from memory.
  - Represent each author's view as the reading notes report it. Where you
    quote, quote exactly, and only passages given in the notes or found by
    search in the work itself.
  - Say plainly what in the paper is already in the literature and what is
    new. Acknowledge the works closest to your thesis. Where earlier work
    suggested, explored or framed an idea the paper develops, credit it as
    such ("first suggested by…") without giving up the claim; concede a
    claim only where earlier work argued it at length and endorsed it, or
    conclusively closed it off.
  - Use search to check, not to browse.

Length: at most {words} words, counting everything except the bibliography —
title, abstract, headings and notes included. Stay under it.

Format: Markdown. A title, an abstract, numbered sections, and a final
section headed "References" listing every work cited and no others.

Put the whole essay between <essay> and </essay> tags. After it, between
<unverified> and </unverified> tags, list any claim about the literature in
the essay that you could not confirm from the notes or by search — or write
"none".
"""

STYLE_PREAMBLE = """\
PRESENTATION. The guide below describes how articles recently published in
leading general philosophy journals are structured and presented. A model
drew it from a sample of such articles; it is about form, not content.
Follow it where it does not conflict with the instructions above. Where it
reports that papers divide, either way is acceptable.

"""

DRAFT_USER = """\
THESIS:
{thesis}

OUTLINE:
{outline}

READING NOTES:
{notes}
"""

RANK_SYSTEM = """\
You are ranking several drafts of the same philosophy paper, written
independently from the same outline. A reader will choose one to take
forward and wants your recommendation.

Judge them on philosophical quality only, by these criteria:

  CLARITY           an identifiable thesis, defined terms, a clear structure
                    of reasoning
  ARGUMENTATION     conclusions follow from premises, premises are
                    adequately defended, serious objections are addressed
  SIGNIFICANCE      a worthwhile contribution, a non-trivial conclusion
  ORIGINALITY       something new is contributed
  ENGAGEMENT        the relevant literature is understood
  SCHOLARSHIP       sources fairly represented, citations accurate, prior
                    work acknowledged

Style is not a criterion except where it affects the philosophy. Do not
propose improvements and do not say how any draft should be changed — only
which is best and why.

Return ONLY JSON:

{
  "ranking": [
    {"draft": 1,
     "rank": 1,
     "strongest": "one sentence",
     "weakest": "one sentence",
     "scores": {"clarity": 1-5, "argumentation": 1-5, "significance": 1-5,
                "originality": 1-5, "engagement": 1-5, "scholarship": 1-5}}
  ],
  "recommendation": "which draft, and the deciding consideration, in two \
sentences"
}
"""


def load_outline(raw_path, number):
    with open(raw_path) as f:
        state = json.load(f)
    if not isinstance(state, dict) or "outlines" not in state:
        sys.exit("%s is not an Outline Deviser raw.json" % raw_path)
    for o in state["outlines"]:
        if o.get("outline") == number and not o.get("error"):
            clean = {k: v for k, v in o.items() if k != "audit"}
            return state.get("thesis", "").strip(), clean
    have = [o.get("outline") for o in state["outlines"] if not o.get("error")]
    sys.exit("no usable outline numbered %s; that file has %s" % (number, have))


def draft_one(client, system, user, i, max_uses):
    txt = client.ask(system, [{"role": "user", "content": user}],
                     temperature=1.0, max_tokens=28000, search=max_uses > 0,
                     max_uses=max_uses, label="draft_%d" % i)
    essay = tagged(txt, "essay")
    return {"draft": i,
            "essay": essay,
            "unverified": tagged(txt, "unverified"),
            "error": None if essay else "no <essay> block came back",
            "raw_text": None if essay else txt[:6000]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", required=True, help="an Outline Deviser raw.json")
    p.add_argument("--outline", type=int, required=True,
                   help="the outline's number in that file")
    p.add_argument("--notes", default=None, help="notes.md from source_reader.py")
    p.add_argument("--drafts", type=int, default=3)
    p.add_argument("--words", type=int, default=5700,
                   help="the length the drafter is told to stay under")
    p.add_argument("--limit", type=int, default=6000,
                   help="the competition's limit, for the report")
    p.add_argument("--max-uses", type=int, default=12,
                   help="web searches allowed per draft; 0 turns search off")
    p.add_argument("--rank", action="store_true",
                   help="also ask a second model to rank the drafts")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--rank-model", default=RANK_MODEL)
    p.add_argument("--out", default="drafts1")
    p.add_argument("--style", default=None, metavar="GUIDE",
                   help="a presentation guide from style_guide.py")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    thesis, outline = load_outline(args.raw, args.outline)
    notes = read_text(args.notes) if args.notes else \
        "(none supplied — verify every claim about the literature by search)"
    style = read_text(args.style).strip() if args.style else None
    if args.dry_run:
        print("style guide: %s" % (args.style or "none"))
        print("thesis:  %s" % thesis[:130])
        print("outline: %s  (%d sections)"
              % (outline.get("title"), len(outline.get("sections") or [])))
        print("%d isolated drafts on %s, up to %d searches each%s."
              % (args.drafts, args.model, args.max_uses,
                 ", then 1 ranking call on %s" % args.rank_model if args.rank else ""))
        if not args.notes:
            print("NO READING NOTES. The drafter will be working from recall "
                  "plus search — the condition the first paper's scholarship "
                  "problems came from.")
        return

    log = RunLog(args.out, __file__, args, globals())
    client = Client(args.model, log)
    log.set("thesis", thesis)
    log.set("outline_title", outline.get("title"))
    system = DRAFT_SYSTEM.format(words=args.words)
    if style:
        system += "\n" + STYLE_PREAMBLE + style + "\n"
        log.set("style_guide_file", args.style)
        log.set("style_guide", style)
    user = DRAFT_USER.format(thesis=thesis,
                             outline=json.dumps(outline, indent=2), notes=notes)

    print("[1/3] drafting — %d isolated drafts…" % args.drafts)
    with ThreadPoolExecutor(max_workers=3) as ex:
        drafts = list(ex.map(
            lambda i: draft_one(client, system, user, i, args.max_uses),
            range(1, args.drafts + 1)))

    print("[2/3] counting…")
    for d in drafts:
        if d["error"]:
            print("      draft %d  FAILED: %s" % (d["draft"], d["error"]))
            continue
        d["words"] = word_count(d["essay"])
        d["references"] = max(0, len([l for l in split_refs(d["essay"])[1].splitlines()
                                      if l.strip()]) - 1)
        with open(os.path.join(args.out, "draft_%d.md" % d["draft"]), "w") as f:
            f.write(d["essay"] + "\n")
        over = "  OVER THE LIMIT" if d["words"] > args.limit else ""
        print("      draft %d  %d words, %d references%s"
              % (d["draft"], d["words"], d["references"], over))
    ok = [d for d in drafts if not d["error"]]

    ranking = None
    if args.rank and len(ok) > 1:
        print("[3/3] ranking on %s…" % args.rank_model)
        blob = "\n\n".join("=== DRAFT %d ===\n%s" % (d["draft"], d["essay"])
                           for d in ok)
        txt = client.ask(RANK_SYSTEM, [{"role": "user", "content": blob}],
                         temperature=0.2, max_tokens=6000, label="rank",
                         model=args.rank_model)
        ranking = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:3000]}
    else:
        print("[3/3] ranking skipped")

    with open(os.path.join(args.out, "raw.json"), "w") as f:
        json.dump({"thesis": thesis, "outline": outline, "drafts": drafts,
                   "ranking": ranking}, f, indent=2)

    lines = ["# Drafts", "", "**Thesis:** %s" % thesis, "",
             "| Draft | Words (limit %d) | References | Could not verify |" % args.limit,
             "| --- | --- | --- | --- |"]
    for d in ok:
        lines.append("| %d | %d | %d | %s |"
                     % (d["draft"], d["words"], d["references"],
                        (d.get("unverified") or "—").replace("\n", " ")[:200]))
    if ranking and not ranking.get("error"):
        lines += ["", "## A second model's ranking (a recommendation, not a decision)", "",
                  ranking.get("recommendation") or "", ""]
        for r in sorted(ranking.get("ranking") or [], key=lambda r: r.get("rank", 9)):
            lines.append("%s. **Draft %s** — strongest: %s Weakest: %s"
                         % (r.get("rank"), r.get("draft"), r.get("strongest"),
                            r.get("weakest")))
    lines += ["", "Pick one draft whole, by number. Do not combine them."]
    with open(os.path.join(args.out, "drafts.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    log.set("drafts_requested", args.drafts)
    log.set("drafts_usable", len(ok))
    log.set("word_counts", {d["draft"]: d["words"] for d in ok})
    print(log.summary())
    print("open %s   <- start here" % os.path.join(args.out, "drafts.md"))


if __name__ == "__main__":
    main()
