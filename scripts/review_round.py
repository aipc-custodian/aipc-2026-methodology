#!/usr/bin/env python3
"""
review_round.py — one round of review: referee, adjudicate, revise, cut.

In the first paper the drafter judged the criticism of its own work. Nobody
independent ruled on which concerns were legitimate, including the decisions
to decline two reviewers' central proposals. This puts an adjudicator between
the reviews and the drafter.

    Stage 1  REFEREE     optional. A Claude model other than the drafter
                         writes a referee report, with search. Reports from
                         other vendors' models you collect by hand and drop
                         into the reviews folder as plain text, UNEDITED.
    Stage 2  ADJUDICATE  a model that wrote neither the paper nor any review
                         rules on each concern: MUST ADDRESS, OPTIONAL, or
                         MISTAKEN, and verifies claims about the literature
                         by search before ruling on them.
    Stage 3  REVISE      the drafter's model gets the paper, the reviews
                         verbatim and the rulings, and revises.
    Stage 4  CUT         pure Python count; if the revision is over length,
                         the drafter is asked to cut restatement until it
                         is not. Critique is additive — every round of the
                         first paper went over the limit.

    mkdir reviews_r1          # paste each outside review into its own file
    python3 review_round.py --paper drafts1/draft_2.md --reviews reviews_r1 \
        --claude-referee claude-fable-5-1 --notes notes_12/notes.md --out round1

    python3 review_round.py --paper round1/revised.md --reviews reviews_r2 \
        --claude-referee claude-fable-5-1 --notes notes_12/notes.md --out round2

Stop when the adjudicator rules no more concerns MUST ADDRESS than a
published paper carries (--stop-at, default 2), or after three rounds. The
default comes from a calibration run on a 2025 Mind article, which drew 2
MUST ADDRESS from the same referees and adjudicator (22 October 2026).

The referee prompt is printed by --show-prompt, so the same words go to the
outside models:

    python3 review_round.py --show-prompt
"""

import argparse, json, os, re, sys

from llm import ANTICIPATION_STANDARD, Client, extract_json, read_text, tagged, word_count
from runlog import RunLog

DRAFTER_MODEL = "claude-opus-5-5"
ADJUDICATOR_MODEL = "claude-sonnet-5-5"

REFEREE_PROMPT = """\
Referee this paper for a philosophy journal. Rank your objections by
seriousness. Search for prior work that anticipates it, and list what you
checked. Say whether it is good, novel and publishable."""

ADJUDICATOR_SYSTEM = """\
You are ruling on referee reports. You wrote neither the paper nor any of
the reports, and you have no stake in either.

Below are a philosophy paper and several referee reports on it. Go through
the reports and identify each distinct concern. Where two referees raise the
same concern, treat it as one and note who raised it.

For each concern, rule:

  MUST ADDRESS  the concern is correct and the paper is damaged if it is not
                answered — an invalid step, an undefended premise the
                argument depends on, a misrepresented source, prior work
                that anticipates a claim the paper presents as new.
  OPTIONAL      the concern has some force, but the paper stands without
                answering it; or it is a matter of emphasis or taste.
  MISTAKEN      the referee is wrong: about what the paper says, about the
                literature, or about what follows.

A referee's claim that prior work anticipates the paper is judged by this
standard:

""" + ANTICIPATION_STANDARD + """
Prior work that meets the standard for a claim the paper presents as new is
MUST ADDRESS. A PRECEDENT the paper does not credit is a scholarship
concern, normally OPTIONAL unless the omission misleads the reader about
what is new; it is never a reason for the paper to give up its claim.

Referees are often wrong about the literature, and they are wrong
confidently. Before ruling on ANY claim that a work exists, says something,
or anticipates the paper, SEARCH and check it. Say what you found. Never
rule on such a claim from memory.

Rule on the concerns. Do not add concerns of your own, and do not say how
the paper should answer them — that is the author's job, not yours.

Return ONLY JSON:

{
  "rulings": [
    {"concern": "the concern, stated in one or two sentences",
     "raised_by": "which report(s)",
     "ruling": "MUST ADDRESS" | "OPTIONAL" | "MISTAKEN",
     "reason": "why, in one or two sentences",
     "checked": "what you searched for and found, or null if the concern \
makes no claim about the literature"}
  ],
  "summary": "two sentences on the state of the paper"
}
"""

REVISE_SYSTEM = """\
You are the author of the philosophy paper below. It has been refereed, and
an independent adjudicator has ruled on each concern.

Revise the paper.

  - Address every concern ruled MUST ADDRESS. How you answer is yours to
    decide: a new argument, a new case, a narrower claim, a concession.
  - Every answer has a cost. It lengthens or thickens the paper and pushes
    its main line further from the reader. Weigh that cost. Narrowing a
    claim, dropping one, or acknowledging an objection in a sentence and
    setting it aside are full answers where they serve the paper better
    than new argument. The readability of the paper and the clarity of its
    main line count against an answer as well as for it. A published
    philosophy paper advances a debate; it does not settle every objection.
  - Concerns ruled OPTIONAL are at your discretion.
  - Do not act on concerns ruled MISTAKEN.
  - Verify by search any claim about the literature before you rely on it —
    including claims made by the referees and by the adjudicator. Cite only
    what the reading notes report or what you have verified.
  - If the adjudicator has upheld that part of the thesis is anticipated in
    the sense of the standard below (endorsed or conclusively foreclosed in
    an extended discussion), say so in the paper and claim only what is new.
    Where earlier work only mentioned, explored or framed an idea the paper
    develops, keep the claim and credit the earlier work.
  - Keep the paper anonymous and in a neutral academic register.
  - The paper must read as written once, for a reader who has never seen
    an earlier version. Do not mention earlier drafts, earlier versions,
    referees, reviews, the adjudicator, or what has been withdrawn or
    revised; remove any such mention already in the paper. Where the paper
    answers an objection a referee raised, present it as an objection a
    reader might make. The account of what changed belongs only in the
    <response> section.

Then cut. The revised paper must be under {words} words, counting everything
except the bibliography. Critique makes papers longer; make room by removing
redundancy — a summary that repeats what the reader has just read, a second
example where one is enough, hedges that add nothing — not by removing
argument. Keep the roadmap, the transitions between sections, and
cross-references that tell the reader where a premise was defended.

Format: Markdown, with a final section headed "References" listing every
work cited and no others. Footnotes may be used, in Markdown footnote
syntax ([^1] in the text, "[^1]: ..." for the note). Footnotes count toward
the word limit.

Put the whole revised paper between <essay> and </essay> tags. After it,
between <response> and </response> tags, say for each MUST ADDRESS concern
what you changed, and for each OPTIONAL concern whether you acted on it and
why. After that, between <unverified> and </unverified> tags, list any claim
about the literature you could not confirm, or write "none".

""" + ANTICIPATION_STANDARD + """"""

REVISE_USER = """\
THE PAPER:
{paper}

THE REFEREE REPORTS (verbatim):
{reviews}

THE ADJUDICATOR'S RULINGS:
{rulings}

READING NOTES ON THE SOURCES:
{notes}
"""

STYLE_PREAMBLE = """\
PRESENTATION. The guide below describes how articles recently published in
leading general philosophy journals are structured and presented. A model
drew it from a sample of such articles; it is about form, not content.
Follow it where it does not conflict with the instructions above. Where it
reports that papers divide, either way is acceptable.

"""

CUT_SYSTEM = """\
You are the author of the philosophy paper below. It is over length.

Cut it to under {words} words, counting everything except the bibliography.
Remove redundancy: a summary that repeats what the reader has just read, a
second example where one is enough, hedges that add nothing. Keep the
roadmap, the transitions between sections, and cross-references that tell
the reader where a premise was defended.

If removing redundancy is not enough, shorten. State replies, examples,
qualifications and the handling of minor objections in fewer words. Every
premise, objection, reply and acknowledgement of prior work must still be
there, but each may be stated more briefly. Do not remove any of them, and
do not add anything. The one exception: remove any mention of earlier drafts, earlier
versions, referees, reviews or the review process, since the paper must
read as written once.

Return the whole paper between <essay> and </essay> tags.
"""


FLAGS_NOTE = """

THIS PASS. There are no referees and no adjudicator in this pass. The
concerns below are flags from the custodian, the person running this
process. They concern presentation and structure, and say nothing about how
to answer them. Act on every one; how is yours to decide. Where a flag names
the thesis chosen for the paper, organise the paper around that thesis.
"""


def load_flags(path):
    """The numbered lines of a custodian's flag file, as (number, text)."""
    out = []
    for line in read_text(path).splitlines():
        m = re.match(r"\s*(\d+)\.\s+(\S.*)", line)
        if m:
            out.append((m.group(1), m.group(2).strip()))
    return out


def load_reviews(folder):
    out = []
    if folder and os.path.isdir(folder):
        for f in sorted(os.listdir(folder)):
            if f.startswith(".") or not f.lower().endswith((".txt", ".md")):
                continue
            out.append((os.path.splitext(f)[0], read_text(os.path.join(folder, f))))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--paper", help="the draft to review, a .md file")
    p.add_argument("--reviews", default=None,
                   help="a folder of referee reports, one .txt or .md each, "
                        "pasted unedited")
    p.add_argument("--claude-referee", default=None, metavar="MODEL",
                   help="also get a referee report from this Claude model "
                        "(not the drafter's)")
    p.add_argument("--notes", default=None, help="notes.md from source_reader.py")
    p.add_argument("--words", type=int, default=5800,
                   help="the length the revision must come in under")
    p.add_argument("--limit", type=int, default=6000)
    p.add_argument("--max-uses", type=int, default=12)
    p.add_argument("--stop-at", type=int, default=2, metavar="N",
                   help="stop without revising when N or fewer concerns are "
                        "ruled MUST ADDRESS (default 2, the published baseline)")
    p.add_argument("--no-revise", action="store_true",
                   help="stop after the rulings")
    p.add_argument("--drafter-model", default=DRAFTER_MODEL)
    p.add_argument("--adjudicator-model", default=ADJUDICATOR_MODEL)
    p.add_argument("--out", default="round1")
    p.add_argument("--show-prompt", action="store_true",
                   help="print the referee prompt, to paste to other models")
    p.add_argument("--style", default=None, metavar="GUIDE",
                   help="a presentation guide from style_guide.py, given to "
                        "the drafter when it revises and cuts")
    p.add_argument("--flags", default=None, metavar="FILE",
                   help="a custodian pass: skip the referee and the "
                        "adjudicator, and give the drafter each numbered flag "
                        "in FILE as a concern it must act on (change 27)")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if args.show_prompt:
        print(REFEREE_PROMPT)
        print("\n(Paste this, then the paper. Turn search on. Save the reply "
              "unedited as a .txt file in the reviews folder.)")
        return
    if not args.paper:
        sys.exit("give --paper")

    paper = read_text(args.paper)
    flags = load_flags(args.flags) if args.flags else None
    if flags is not None:
        if args.reviews or args.claude_referee:
            sys.exit("--flags is a pass of its own: give it without --reviews "
                     "or --claude-referee")
        if not flags:
            sys.exit("no numbered flags found in %s" % args.flags)
    reviews = load_reviews(args.reviews)
    if args.reviews and not reviews and not args.dry_run:
        sys.exit("the reviews folder %s has no .txt or .md reports in it. "
                 "Save the outside reviews there first (change 28)."
                 % args.reviews)
    style = read_text(args.style).strip() if args.style else None
    style_add = "\n\n" + STYLE_PREAMBLE + style + "\n" if style else ""
    if args.dry_run:
        print("paper: %s (%d words that count)" % (args.paper, word_count(paper)))
        print("%d outside review(s): %s" % (len(reviews),
                                            ", ".join(n for n, _ in reviews) or "none"))
        if args.claude_referee:
            print("+ 1 referee report from %s" % args.claude_referee)
        if flags is not None:
            print("CUSTODIAN PASS: %d flags from %s, all to be acted on; "
                  "no referee, no adjudicator" % (len(flags), args.flags))
        print("adjudicator: %s    drafter: %s"
              % (args.adjudicator_model, args.drafter_model))
        print("style guide: %s" % ("%s (%d words)" % (args.style, len(style.split()))
                                   if style else "none"))
        if args.adjudicator_model == args.drafter_model:
            print("WARNING: the adjudicator and the drafter are the same "
                  "model. The point of this stage is that they are not.")
        return
    if flags is None and not reviews and not args.claude_referee:
        sys.exit("no reviews: put reports in --reviews FOLDER, or give "
                 "--claude-referee MODEL")

    log = RunLog(args.out, __file__, args, globals())
    client = Client(args.drafter_model, log)
    log.set("paper_in", args.paper)
    if style:
        log.set("style_guide_file", args.style)
        log.set("style_guide", style)
    log.set("words_in", word_count(paper))

    if flags is not None:
        print("[1-2/4] custodian pass: %d flags, no referee, no adjudicator"
              % len(flags))
        flag_text = read_text(args.flags)
        reviews = [("custodian", flag_text)]
        log.set("reviews", ["custodian"])
        log.set("custodian_flags", flag_text)
        review_blob = "=== FLAGS FROM THE CUSTODIAN ===\n" + flag_text
        rulings = [{"concern": t, "raised_by": "custodian (flag %s)" % n,
                    "ruling": "MUST ADDRESS",
                    "reason": "A flag from the custodian. Act on it; how is "
                              "yours to decide.",
                    "checked": None} for n, t in flags]
        ruled = {"rulings": rulings,
                 "summary": "Custodian pass: every flag is to be acted on."}
        count = {"MUST ADDRESS": len(rulings), "OPTIONAL": 0, "MISTAKEN": 0}
        lines = ["# Flags (custodian pass)", "",
                 "%d flags, each to be acted on." % len(rulings), ""]
        lines += ["%s. %s" % (n, t) for n, t in flags]
        with open(os.path.join(args.out, "rulings.md"), "w") as f:
            f.write("\n".join(lines) + "\n")
        log.set("rulings", count)
    else:
        if args.claude_referee:
            print("[1/4] referee report from %s…" % args.claude_referee)
            txt = client.ask("", [{"role": "user",
                                   "content": REFEREE_PROMPT + "\n\n" + paper}],
                             temperature=1.0, max_tokens=12000, search=True,
                             max_uses=args.max_uses, label="referee",
                             model=args.claude_referee)
            name = "referee_" + args.claude_referee
            with open(os.path.join(args.out, name + ".md"), "w") as f:
                f.write(txt)
            reviews.append((name, txt))
        else:
            print("[1/4] no Claude referee asked for")
        log.set("reviews", [n for n, _ in reviews])
        review_blob = "\n\n".join("=== REPORT: %s ===\n%s" % (n, t) for n, t in reviews)

        print("[2/4] adjudicating %d report(s) on %s…"
              % (len(reviews), args.adjudicator_model))
        txt = client.ask(ADJUDICATOR_SYSTEM,
                         [{"role": "user",
                           "content": "THE PAPER:\n%s\n\nTHE REFEREE REPORTS:\n%s"
                                      % (paper, review_blob)}],
                         temperature=0.2, max_tokens=16000, search=True,
                         max_uses=args.max_uses, label="adjudicate",
                         model=args.adjudicator_model)
        ruled = extract_json(txt) or {"rulings": [], "error": "unparseable",
                                      "raw_text": txt[:6000]}
        rulings = ruled.get("rulings") or []
        order = {"MUST ADDRESS": 0, "OPTIONAL": 1, "MISTAKEN": 2}
        rulings.sort(key=lambda r: order.get(r.get("ruling"), 9))
        count = {k: sum(1 for r in rulings if r.get("ruling") == k) for k in order}
        lines = ["# Rulings", "", ruled.get("summary") or "", "",
                 "%d must address, %d optional, %d mistaken."
                 % (count["MUST ADDRESS"], count["OPTIONAL"], count["MISTAKEN"]), ""]
        for r in rulings:
            lines += ["## %s" % r.get("ruling"), "",
                      "**Concern** (%s): %s" % (r.get("raised_by"), r.get("concern")), "",
                      "**Reason:** %s" % r.get("reason"), ""]
            if r.get("checked"):
                lines += ["**Checked:** %s" % r["checked"], ""]
        rulings_md = "\n".join(lines)
        with open(os.path.join(args.out, "rulings.md"), "w") as f:
            f.write(rulings_md + "\n")
        print("      %d must address, %d optional, %d mistaken"
              % (count["MUST ADDRESS"], count["OPTIONAL"], count["MISTAKEN"]))
        log.set("rulings", count)

    state = {"paper_in": args.paper, "reviews": dict(reviews), "ruled": ruled}
    stop = (flags is None and bool(rulings)
            and count["MUST ADDRESS"] <= args.stop_at)

    if ruled.get("error"):
        print("      the adjudicator's answer could not be read; see calls.jsonl. "
              "Not revising.", file=sys.stderr)
    elif args.no_revise:
        print("[3/4] revision skipped (--no-revise)")
    elif stop:
        print("[3/4] %d must address, at or below the published baseline (%d) — "
              "the paper stands. Stop here." % (count["MUST ADDRESS"], args.stop_at))
    else:
        print("[3/4] revising on %s…" % args.drafter_model)
        notes = read_text(args.notes) if args.notes else "(none supplied)"
        txt = client.ask(REVISE_SYSTEM.format(words=args.words) + style_add
                         + (FLAGS_NOTE if flags is not None else ""),
                         [{"role": "user",
                           "content": REVISE_USER.format(
                               paper=paper, reviews=review_blob,
                               rulings=json.dumps(rulings, indent=2), notes=notes)}],
                         temperature=1.0, max_tokens=28000, search=True,
                         max_uses=args.max_uses, label="revise")
        essay = tagged(txt, "essay")
        state["response"] = tagged(txt, "response")
        state["unverified"] = tagged(txt, "unverified")
        if not essay:
            print("      no <essay> block came back; see calls.jsonl", file=sys.stderr)
        else:
            n = word_count(essay)
            log.set("words_after_revision", n)
            print("      revised: %d words" % n)
            cuts = 0
            print("[4/4] length…")
            while n > args.words and cuts < 3:
                cuts += 1
                print("      over %d — cut %d…" % (args.words, cuts))
                txt = client.ask(CUT_SYSTEM.format(words=args.words) + style_add,
                                 [{"role": "user",
                                   "content": "The paper is %d words by the "
                                              "counter that will be used.\n\n%s"
                                              % (n, essay)}],
                                 temperature=0.3, max_tokens=24000,
                                 label="cut_%d" % cuts)
                shorter = tagged(txt, "essay")
                if not shorter:
                    break
                essay, n = shorter, word_count(shorter)
                print("      now %d words" % n)
            log.set("cut_passes", cuts)
            log.set("words_out", n)
            with open(os.path.join(args.out, "revised.md"), "w") as f:
                f.write(essay + "\n")
            with open(os.path.join(args.out, "response.md"), "w") as f:
                f.write("# The drafter's response to the rulings\n\n%s\n\n"
                        "## Could not verify\n\n%s\n"
                        % (state.get("response") or "—",
                           state.get("unverified") or "—"))
            state["revised"] = essay
            state["words_out"] = n
            if n > args.limit:
                print("      STILL OVER THE %d-WORD LIMIT. Run another round "
                      "with --words lower, or say so and rerun." % args.limit)

    with open(os.path.join(args.out, "raw.json"), "w") as f:
        json.dump(state, f, indent=2)
    print(log.summary())
    print("open %s" % os.path.join(args.out, "rulings.md"))
    if state.get("revised"):
        print("next round reviews: %s" % os.path.join(args.out, "revised.md"))


if __name__ == "__main__":
    main()
