#!/usr/bin/env python3
"""
style_guide.py — a presentation guide drawn from a sample of recently
published philosophy papers, for the drafter to follow.

Style is not graded, but structure affects how clear an argument is, and the
drafter's habits of presentation (formal argument summaries at the head of
every section, heavy signposting) are its own, not the discipline's. This
replaces them with what a model finds published papers actually do. The
model draws the sample by a fixed rule, reads the papers in full, and writes
the guide. Nobody tells it what good structure is.

    Stage 1  SAMPLE   one call, with search. The model chooses the leading
                      general journals and lists the first research articles
                      of each journal's first 2025 issue, skipping any on
                      the subject of the paper being written. You fetch
                      every work listed, and nothing else.
    Stage 2  READ     one call per paper, the PDF in full: how the paper is
                      built and presented, not what it argues.
    Stage 3  SYNTH    one call: the properties most of the papers share,
                      with counts, written as generic guidance.

    python3 style_guide.py --sample --out style1
    (fetch the papers listed in style1/sample.md into style1/papers/)
    python3 style_guide.py --read style1/papers --out style1

The guide (style1/guide.md) then goes to the drafter with --style:

    python3 review_round.py ... --style style1/guide.md

It is about form only. Every prompt here forbids content, and the sample
excludes papers on the paper's own subject, so that no argument, example or
distinction can travel from a published paper into the essay through it.
"""

import argparse, json, os, sys
from concurrent.futures import ThreadPoolExecutor

from llm import Client, extract_json, pdf_block, read_text, source_files
from runlog import RunLog

MODEL = "claude-sonnet-5-5"

SAMPLE_SYSTEM = """\
You are drawing a sample of recently published philosophy articles. Someone
will read them to learn how papers in leading journals are structured and
presented: how they open, how they lay out an argument, where objections
go, how they end. Their content does not matter. Follow the rule exactly;
do not choose papers you think are good examples.

THE RULE.
  1. Take the {journals} general (not specialist) journals of analytic
     philosophy most widely ranked highest. Name them, and say in a
     sentence which rankings you relied on.
  2. For each journal, find its first issue of 2025 (volume and issue
     number). Use search; do not rely on memory.
  3. From that issue take the first {per} research articles in table-of-
     contents order. Skip discussion notes, replies, symposium pieces,
     critical notices, book reviews, editorials, special-issue
     introductions, and named or endowed lectures and any piece published
     as part of a lecture series (for example the Dewey Lectures).
  4. Also skip any article on these subjects, and take the next one
     instead: {exclude}.
  5. If the issue runs out, continue into the journal's second 2025 issue.
  6. List exactly {per} articles for every journal. If you cannot, say
     which journal and why in "shortfall"; never list fewer silently.
  7. Verify every author and title on the article's own page. Never infer
     them. If you could not verify an entry, set "verified" to false.

For each article give the title, authors, journal, volume and issue, the
DOI, and a link to an open-access copy if you find one (a preprint on
PhilPapers, PhilArchive or an author's page). Verify each by search.

Return ONLY JSON:

{{"journals": [{{"journal": "...", "why": "one sentence"}}],
  "rankings_used": "one sentence",
  "articles": [{{"title": "...", "authors": "...", "journal": "...",
                "issue": "volume(issue), year", "doi": "...",
                "open_access": "url or null",
                "verified": true,
                "skipped_before_it": "titles skipped under rules 3-4, or null"}}],
  "shortfall": "which journals have fewer than {per}, and why, or null"}}
"""

READ_SYSTEM = """\
You are studying how a published philosophy paper is built and presented.
Describe its FORM ONLY. Do not summarise its claims, arguments, examples or
distinctions: the reader of your notes must not learn what the paper argues,
beyond a topic label of a few words.

Report, from the full text:

  opening        how the paper begins (a case, a puzzle, a survey, a
                 statement of thesis…); in which paragraph the thesis is
                 first stated; whether there is a roadmap, and how long
  sections       how many; how long, roughly; what headings look like
                 (numbered, descriptive, both); whether sections open by
                 restating or summarising their own argument, and how
  argument       how arguments are laid out: in prose, as numbered
                 premises and conclusion, or both; where numbered
                 arguments appear (if anywhere) and how often; any formal
                 notation
  cases          how many examples or cases; whether labelled or named;
                 where they come in the paper and how they are introduced
  objections     where objections come (inside sections, in a section of
                 their own, at the end); roughly how many; how they are
                 introduced and answered
  prior_work     how other work is brought in: a survey section, woven
                 through, in notes; how disagreement and credit are phrased
  signposting    how much the paper tells the reader what it is about to
                 do or has just done: little, moderate, heavy
  voice          first person singular, plural, or impersonal; register
  notes          footnotes or endnotes: roughly how many, what they do
  ending         what the conclusion does: summarise, extend, concede,
                 point to further work; how long
  distinctive    anything else about its form a writer could learn from

Return ONLY JSON with those twelve keys (each a short string) plus
"topic_label" (a few words) and "length_words" (an estimate of the body's
length, excluding references).
"""

SYNTH_SYSTEM = """\
Below are notes on the form of {n} philosophy articles published in leading
general journals in 2025. The notes describe how each paper is built and
presented, not what it argues.

Write a guide for a writer of a philosophy journal article: the practices
of structure and presentation these papers share.

  - State a practice only if the notes support it, and say how many of the
    {n} papers follow it ("12 of 15"). Where the papers divide, say so and
    give the split, rather than choosing a side.
  - Include practices that are rare or absent in the sample, if a writer
    might otherwise adopt them, with the counts.
  - Cover at least: the opening and where the thesis is stated; roadmaps;
    how sections open; how arguments are laid out, including numbered
    premises; cases; where objections go; how prior work is credited;
    signposting; voice; notes; the conclusion.
  - The guide is about form only. Say nothing about any subject, argument,
    example or position, and do not refer to particular papers.
  - Write it as guidance a writer can follow, in plain prose or short
    bullets, at most 700 words.

Return only the guide, in Markdown, with a title.
"""


def sample(args, client):
    system = SAMPLE_SYSTEM.format(journals=args.journals, per=args.per,
                                  exclude=args.exclude)
    print("[1/1] drawing the sample on %s (with search)…" % args.model)
    txt = client.ask(system, [{"role": "user", "content": "Draw the sample."}],
                     temperature=None, max_tokens=12000, search=True,
                     max_uses=args.max_uses, label="sample")
    data = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:6000]}
    with open(os.path.join(args.out, "sample.json"), "w") as f:
        json.dump(data, f, indent=2)
    arts = data.get("articles") or []
    lines = ["# The sample", "",
             "Fetch every article listed into `%s/papers/`, as PDFs, and "
             "nothing else. Where there is no open-access copy, fetch the "
             "published version through the library." % args.out, ""]
    for j in data.get("journals") or []:
        lines.append("- **%s** — %s" % (j.get("journal"), j.get("why")))
    if data.get("rankings_used"):
        lines += ["", "Rankings used: %s" % data["rankings_used"]]
    lines += ["", "| # | Article | Journal | DOI | Open access |",
              "| --- | --- | --- | --- | --- |"]
    for i, a in enumerate(arts, 1):
        lines.append("| %d | %s — %s | %s %s | %s | %s |"
                     % (i, a.get("authors"), a.get("title"), a.get("journal"),
                        a.get("issue"), a.get("doi"), a.get("open_access") or "—"))
    if data.get("shortfall"):
        lines += ["", "**Shortfall:** %s" % data["shortfall"]]
    unver = [a.get("title") for a in arts if a.get("verified") is False]
    if unver:
        lines += ["", "**Not verified:** %s" % "; ".join(unver)]
    skipped = [(a.get("title"), a.get("skipped_before_it")) for a in arts
               if a.get("skipped_before_it")]
    if skipped:
        lines += ["", "## Skipped under the rule", ""]
        lines += ["- before *%s*: %s" % s for s in skipped]
    with open(os.path.join(args.out, "sample.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    client.log.set("articles_listed", len(arts))
    if data.get("error"):
        print("      the answer could not be read; see calls.jsonl", file=sys.stderr)
    print("      %d articles listed" % len(arts))
    print("open %s   <- fetch these" % os.path.join(args.out, "sample.md"))


def read_one(client, path):
    if path.lower().endswith(".pdf"):
        blocks = [pdf_block(path)]
    else:
        blocks = [{"type": "text", "text": read_text(path)}]
    blocks.append({"type": "text", "text": "Describe this paper's form."})
    txt = client.ask(READ_SYSTEM, [{"role": "user", "content": blocks}],
                     temperature=None, max_tokens=4000,
                     label="read_" + os.path.basename(path))
    data = extract_json(txt)
    return {"file": os.path.basename(path), "form": data,
            "error": None if data else "unparseable",
            "raw_text": None if data else (txt or "")[:3000]}


def read(args, client):
    files = source_files(args.read)
    if not files:
        sys.exit("no .pdf, .txt or .md files in %s" % args.read)
    print("[1/2] reading %d papers on %s…" % (len(files), args.model))
    with ThreadPoolExecutor(max_workers=3) as ex:
        forms = list(ex.map(lambda p: read_one(client, p), files))
    ok = [f for f in forms if not f["error"]]
    for f in forms:
        print("      %s  %s" % ("ok    " if not f["error"] else "FAILED", f["file"]))
    if len(ok) < 2:
        sys.exit("fewer than two papers read; nothing to synthesise")
    print("[2/2] writing the guide from %d papers…" % len(ok))
    blob = "\n\n".join("=== PAPER %d ===\n%s" % (i, json.dumps(f["form"], indent=1))
                       for i, f in enumerate(ok, 1))
    guide = client.ask(SYNTH_SYSTEM.format(n=len(ok)),
                       [{"role": "user", "content": blob}],
                       temperature=None, max_tokens=8000, label="synth")
    guide = (guide or "").strip()
    with open(os.path.join(args.out, "forms.json"), "w") as f:
        json.dump(forms, f, indent=2)
    with open(os.path.join(args.out, "guide.md"), "w") as f:
        f.write(guide + "\n")
    client.log.set("papers_read", len(ok))
    client.log.set("papers_failed", [f["file"] for f in forms if f["error"]])
    client.log.set("guide_words", len(guide.split()))
    print("open %s   <- the guide" % os.path.join(args.out, "guide.md"))


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--sample", action="store_true",
                   help="stage 1: list the articles to fetch")
    g.add_argument("--read", metavar="FOLDER",
                   help="stages 2-3: read the fetched papers and write the guide")
    p.add_argument("--journals", type=int, default=5)
    p.add_argument("--per", type=int, default=3, help="articles per journal")
    p.add_argument("--exclude", default="artificial intelligence, language "
                   "models or chatbots; assertion, testimony, sincerity, lying "
                   "or speech acts; calibration, credence or confidence",
                   help="subjects the sample skips, so that no content can "
                        "travel from a sampled paper into the essay")
    p.add_argument("--max-uses", type=int, default=20)
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="style1")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if args.dry_run:
        if args.sample:
            print("sample: %d journals x %d articles, on %s, up to %d searches"
                  % (args.journals, args.per, args.model, args.max_uses))
            print("skipping articles on: %s" % args.exclude)
        else:
            files = source_files(args.read) if os.path.isdir(args.read) else []
            print("read: %d files in %s, then 1 synthesis call, on %s"
                  % (len(files), args.read, args.model))
        return

    # Each stage keeps its own log, so the second does not overwrite the first.
    stage = "sample" if args.sample else "read"
    log = RunLog(os.path.join(args.out, "log_" + stage), __file__, args, globals())
    client = Client(args.model, log)
    if args.sample:
        log.set("stage", "sample")
        log.set("exclude", args.exclude)
        sample(args, client)
    else:
        log.set("stage", "read")
        read(args, client)
    print(log.summary())


if __name__ == "__main__":
    main()
