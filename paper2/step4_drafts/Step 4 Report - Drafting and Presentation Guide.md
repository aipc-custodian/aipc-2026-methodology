# Summary

Step 4 took the chosen outline and reading notes from Step 3 and ended with one draft, chosen whole by number. Three isolated drafts were written on Claude Opus 5.5 from the same thesis, outline and notes. A second model (Sonnet 5.5) ranked them, and the custodian chose Draft 1, against the ranker’s first choice (Draft 2).

Step 4 also added a component to the scaffold. To keep the drafter’s own habits of presentation from standing in for the discipline’s, a model drew a sample of articles from leading general journals by a fixed rule and read them in full for their form only. It then wrote a presentation guide with counts. The guide goes to the drafter whenever it revises in Step 5, and to no referee or adjudicator.

Step 4 cost about **$10.20** in API charges. $2.74 went on drafting, ranking and a probe. $7.46 went on the presentation guide, $3.22 of it a sampling run that returned nothing because of a defect in the shared client (change 19). Four changes were made to the scaffold, numbered 17–20 below.

No philosophical content passed from the custodian, or from the conversation in which the pipeline was managed, to any model that generated or judged philosophy.

# Two levels of activity

As before, the **object level** consisted of scripted calls to the Anthropic API, each with no memory and no access to earlier conversations, recorded in full in each run folder (`calls.jsonl`, `run_log.json`). The **meta level** was a Claude conversation (configured as Claude Opus 5.5) with the custodian’s memory on, in which the rules were interpreted, scripts written and repaired, outputs explained and decisions discussed. Only script changes, command-line settings and index numbers crossed from meta to object.

Two further things crossed in Step 4, both argument-neutral and both disclosed here:

  - **Published papers.** These were ten PDFs that a model listed under a fixed sampling rule. The custodian fetched them and no others, and they were read for form only.
  - **The presentation guide.** A model wrote it from those readings. It is given to the drafter as a generic instruction about presentation.

# Inputs

From Step 3 (11–20 October):

  - **Thesis:** `Step 3 - Novelty/restate_1/raw.json`, index 0.
  - **Outline:** `Step 3 - Novelty/outlines_1b_rework0/raw.json`, outline 0 (“The Unit of Assertion Failure”; six sections).
  - **Notes:** `Step 3 - Novelty/notes_1_all.md`, fourteen works read in full.

# Timeline and spending

Spending is from the custodian’s API balance readings, and token counts are from the run logs. Prices per million tokens:

  - Opus 5.5: $4 in, $20 out.
  - Sonnet 5.5: $2 in, $10 out.
  - Web searches: $10 per thousand.

Costs computed from tokens agree with every balance reading taken.

| When (20 Oct, CDT) | Action                                                       | Calls | Tokens in / out   | Search | Balance | Cost       |
| ------------------ | ------------------------------------------------------------ | ----- | ----------------- | ------ | ------- | ---------- |
| 11:58 AM           | End of Step 3                                                | —     | —                 | —      | $14.17  | —          |
| 12:38 PM           | Top-up                                                       |       |                   |        | $34.17  | \+$20.00   |
| 12:40              | Probe of Opus 5.5 (model, temperature, search)               | 2     | —                 | 1      | $34.10  | $0.07      |
| 12:44–12:48        | **Three drafts** (Opus 5.5) and **ranking** (Sonnet 5.5)     | 4     | 362,511 / 61,893  | 9      | $31.43  | $2.67      |
| 1:28–1:30          | Presentation guide, sample 1 (rule not fully followed)       | 1     | 557,298 / 12,502  | 20     | $29.99  | $1.44      |
| 1:33–1:34          | Sample 2, under the tightened rule (change 18)               | 1     | 396,888 / 11,678  | 20     | $28.88  | $1.11      |
| 1:37–1:39          | Sample 3, larger search budget; returned nothing (change 19) | 1     | 1,425,347 / 8,455 | 28     | $25.66  | $3.22      |
| 2:02–2:04          | **Ten papers read for form**, and the guide written          | 11    | 698,873 / 29,075  | 0      | —       | $1.69      |
|                    | **Total for Step 4**                                         |       |                   |        |         | **$10.20** |

No balance reading was taken after the last run. Its cost is computed from tokens, so the balance should now stand at about $23.97.

The drafting run broke down as follows:

| Call    | Model      | Tokens in / out  | Searches |
| ------- | ---------- | ---------------- | -------- |
| Draft 1 | Opus 5.5   | 108,381 / 19,745 | 3        |
| Draft 2 | Opus 5.5   | 108,254 / 19,403 | 3        |
| Draft 3 | Opus 5.5   | 107,954 / 19,857 | 3        |
| Ranking | Sonnet 5.5 | 37,922 / 2,888   | 0        |

Each draft cost about $0.86. The estimate in the recipe, $5–10 for the step, was too high: the drafters used three searches each of the twelve allowed, and none came near its output allowance.

Machine time was about 20 minutes of API time across all runs; the drafting run took 3 minutes 49 seconds of wall time. The custodian estimates his own time at about 2 hours.

# What was changed, and why

Numbering continues from the Step 3 report. Each change was made at the meta level in response to something observed in an object-level output.

**17. A presentation guide, and a way to give it to the drafter (20 October).** The three drafts differed in presentation as well as argument. Draft 3, for instance, opened sections with a semi-formal statement of their argument. The custodian found this jarring, and asked whether the conventions of published papers could be learned rather than assumed. A new script, `style_guide.py`, does this in three stages, each with no memory:

1.  **Sample.** One call with search. The model takes the five general analytic journals most widely ranked highest, and lists the first three research articles of each journal’s first 2025 issue. It skips articles on the paper’s own subject (AI and language models; assertion, testimony, sincerity, lying and speech acts; calibration, credence and confidence), so that no argument, example or distinction can travel from a published paper into the essay. The custodian fetches every article listed, and no others.
2.  **Read.** One call per paper, with the full PDF, describing its form only: how it opens, where the thesis is stated, how sections begin, how arguments are laid out, where objections go, how prior work is credited, signposting, voice, notes and the ending. The prompt forbids summarising content.
3.  **Synthesise.** One call, which writes a guide of the practices the papers share, with counts (“8 of 10”). Where the papers divide, it reports the split rather than choosing a side.

`review_round.py` and `draft.py` gained a `--style` option. It appends the guide to the drafter’s revise and cut prompts, and only those. The drafter is told the guide is about form, not content, that it is subordinate to every other instruction (answering MUST ADDRESS concerns, anonymity, length), and that where papers divide either way is acceptable. Referees and the adjudicator never see it. The full text of the guide is saved in each run log.

**18. A tighter sampling rule (20 October).** The first sample did not follow the rule. It gave one *Philosophical Review* article instead of three, without saying why. It took both of its *Journal of Philosophy* entries from that issue’s Dewey Lectures, which are lectures rather than research articles. And it inferred one lecture’s author instead of checking it. Rather than drop entries by hand, which would have meant the custodian choosing the sample, the rule was tightened and the draw rerun. The new rule excludes named or endowed lectures and lecture series, requires exactly the number of articles asked for from each journal or an explicit “shortfall” saying why not, and forbids inferring authors, marking anything unverified. The second sample followed the rule and said where it failed: it could not retrieve the *Philosophical Review*’s first 2025 table of contents, and its search budget ran out before it reached the *Journal of Philosophy*’s next issue.

**19. Continuing a paused turn (20 October).** A third draw, with a larger search budget (40), was run under a rule fixed in advance that its result would be used, whatever it returned. It returned nothing: the API had paused the turn after 28 searches (stop reason `pause_turn`), which happens when a turn runs many server-side searches. The shared client `llm.py` treated the pause as the end of the turn. It now sends a paused turn back to continue, up to six times, records each continuation in the log, and warns if a turn is still paused at the end. The defect had not shown before because no earlier call searched as much. It could equally have struck the adjudicator or the drafter in Step 5, both of which search. The failed call cost $3.22, most of it the 1.4 million input tokens that 28 searches’ results had added to the context.

*The sample used.* With the third draw void, the custodian proposed the rule actually applied: the union of the first two draws, with the tightened rule applied mechanically to both. This keeps the second draw’s nine articles and adds the first draw’s one *Philosophical Review* article. The Dewey Lectures and Goldstein & Hawthorne (excluded under the second draw’s reading of the assertion exclusion) stay out. The result is ten articles from four journals:

  - *Philosophical Review* 134(1), 1 article;
  - *Noûs* 59(1), 3;
  - *Philosophy and Phenomenological Research* 110(1), 3;
  - *Mind* 134(533), 3.

The *Journal of Philosophy* is not represented. The *Philosophical Review* article was read in its accepted-manuscript version.

**20. Cutting redundancy, not signposting (20 October).** The guide found signposting in all ten papers, heavy or moderate-to-heavy in nine. But the revise and cut prompts in `review_round.py` told the drafter to make room by removing “summaries of earlier sections, signposting…”, so every revision that ran over length would have cut first what published papers keep. Both prompts now say to remove *redundancy* (a summary that repeats what the reader has just read, a second example where one is enough, hedges that add nothing) and to keep the roadmap, the transitions between sections, and cross-references that tell the reader where a premise was defended.

**First live run of** `draft.py`**.** It ran as designed, with no change needed: no call was cut off, all three drafts came in under the 5,700 words they were told to stay under, and every call’s tokens were logged. The probe showed that Opus 5.5, like Sonnet 5.5, accepts only its default temperature; this does not affect the drafts, which ask for the default, and the ranking call’s refusal was handled and logged.

**Deployment.** Each script change was delivered from a fresh, uniquely named staging folder and checked by checksum on both sides. No delivery arrived stale in Step 4.

# Results

## The drafts

Words count toward the 6,000-word limit. Rank is the ranker’s place. The six scores (1–5) are the ranker’s, on clarity, argumentation, significance, originality, engagement and scholarship.

| Draft | Words | Refs | Rank | Clar. | Arg. | Sig. | Orig. | Eng. | Schol. |
| ----- | ----- | ---- | ---- | ----- | ---- | ---- | ----- | ---- | ------ |
| 1     | 5,561 | 16   | 2    | 5     | 4    | 4    | 4     | 5    | 5      |
| 2     | 5,598 | 16   | 1    | 4     | 5    | 4    | 4     | 5    | 4      |
| 3     | 5,620 | 15   | 3    | 4     | 4    | 4    | 4     | 5    | 4      |

All three follow the outline’s six sections and grant the antecedent. All three state the thesis’s “p, with confidence c” clause once in the abstract and hold it back for §5 and the conclusion, so the custodian’s concern that a scope caveat might come too early did not separate them.

All three listed their claims about Williams & Bayne among those they could not verify. These are that Williams & Bayne count not blatantly contradicting oneself among the behavioural expectations of asserters, and that chatbots meet these expectations “to an impressive degree”. Whichever draft was chosen, these claims had to be checked against the source before submission, so they did not separate the drafts either.

The ranker recommended Draft 2. In its words, Draft 2’s “argument that resampling holds fixed the very variable insincerity depends on, together with a rigorous check of all content readings including the hard R2 case, gives it the deepest and most defensible argumentation”. Draft 1 was “a close second with cleaner scholarship and a better-defined hallucination notion”. For Draft 3, the ranker noted that its definition of hallucination “wobbles” and that the text “leaks drafting residue (‘the notes report’)”.

## The choice

The custodian chose **Draft 1**, whole and by number. His reasons were given at the meta level and did not cross.

## The presentation guide

The guide (`Style Guide/style2/guide.md`, 745 words) reports, among other things:

  - **Arguments:** prose carries the reasoning in most papers. Half display a numbered premise–conclusion argument, typically once, then defend it premise by premise.
  - **Objections:** only one paper has a separate objections section; the rest answer objections where they arise.
  - **Prior work:** no paper has a stand-alone literature review.
  - **Roadmap and signposting:** eight of ten give a roadmap, and all use signposting.
  - **Conclusions:** short, and they open no new line of argument.

The guide records two practices that the drafter’s other instructions override: four papers cite the author’s earlier work, which the anonymity requirement rules out, and acknowledgements are usual.

# Findings about the method

1.  **Drafting was cheap and the ranker was close.** Three isolated Opus drafts cost $2.57 and took four minutes. The ranker put Drafts 1 and 2 within a point of each other on every criterion. At this stage the expensive input is the reader’s judgment, not the drafts.
2.  **The drafts differed in where their strength lay, not in how strong they were.** One draft had the strongest argument about resampling, another the strongest arguments about hallucination and sanction. No draft was best throughout, and the rule against combining drafts means choosing which argument the paper is built on.
3.  **Choose on what review cannot repair.** Citation slips and drafting residue can be met by a flag in Step 5. The architecture of a section’s argument cannot be changed without a rerun. The choice was framed this way at the meta level.
4.  **A model can learn the discipline’s presentation from the discipline.** The guide corrected an assumption built into the scaffold itself (change 20). It also showed that a habit the custodian found jarring is not, in its milder form, out of the norm: half the sample displays a numbered argument.
5.  **Search-heavy calls are expensive in a way that is easy to miss.** Every search adds its results to the context, which is billed as input on each continuation. Twenty-eight searches in one turn cost almost twice as much as reading ten full papers.
6.  **Models report retrieval failures honestly when told to.** Under the tightened rule, the sampler said what it could not retrieve and did not guess. Under the loose rule it had silently listed fewer articles, and inferred an author.
7.  **Every new stage finds a defect in old code.** The paused-turn defect sat in the shared client through three steps, and only a call that searched more than any before it exposed it.

# Human involvement in Step 4

## At the object level, the custodian

  - typed commands and chose their settings;
  - read the three drafts and the ranking, and chose Draft 1 by number;
  - decided that a presentation guide should be built, as a generic method instruction;
  - proposed the rule for the sample actually used: the union of the first two draws, under the tightened rule;
  - fetched exactly the ten papers the sampling rule listed, and no others, preferring published versions;
  - agreed to change 20, after asking whether the guide and the cutting instruction were consistent.

He sent no text to any object-level model in Step 4.

## At the meta level

  - Claude advised the custodian to choose on what revision cannot repair, the architecture of the arguments, rather than on fixable faults.
  - On the custodian’s request, Claude gave short summaries of Draft 2’s resampling argument and Draft 1’s hallucination and sanction arguments, with the weak point of each. The custodian reports that he had been leaning toward Draft 1 beforehand, and that the summaries settled it. Claude offered a full ranking of its own, which was not taken up.
  - Claude proposed a presentation guide built from the literature. It then designed `style_guide.py`, including the sampling rule and the exclusions.
  - Claude recommended rejecting the first sample and rerunning under a tighter rule rather than editing it by hand. It also recommended the third draw, under a rule fixed in advance that its result would be used. When that draw failed, it recommended falling back to the second, and the custodian proposed the union instead.
  - Claude identified the conflict between the guide’s findings and the cutting instruction, and proposed change 20.

*Disclosure.* As in earlier steps, the meta-level Claude has memory of the custodian’s research and of the first paper. Its summaries and recommendations are AI contributions from a conversation not isolated as object-level calls are, so they are reported here as part of the selection process.

*Run B.* The decision whether Run B goes ahead was deferred again at the custodian’s request.

# Carried into Step 5

  - **Paper:** `Step 4 - Drafts/drafts1/draft_1.md` (5,561 words).
  - **Notes:** `Step 3 - Novelty/notes_1_all.md`.
  - **Guide:** `Style Guide/style2/guide.md`, given with `--style` in every round.
  - **To verify before submission:** the claims about Williams & Bayne that all three drafters flagged as unverified; the page references in the notes.
  - **Known in Draft 1** (for the referees to find, not for the custodian to flag with reasons):
      - the ranker found its likelihood-ratio claim about resampling “somewhat asserted”, and its policy-level analogue of the sanction condition “stretched”;
      - the revise prompt now keeps cross-references, which Draft 1 uses heavily.
  - **Untested live:** `review_round.py`, and the continuation of paused turns in `llm.py`.

# Files

| Folder                                                  | Contents                                                                                                                              |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `Second Run - Philosophy of AI/Step 4 - Drafts/drafts1` | The three drafts, the ranking (`drafts.md`, `raw.json`) and the run log                                                               |
| `Style Guide/style1`                                    | Sample 1 (rule not fully followed)                                                                                                    |
| `Style Guide/style2`                                    | Sample 2, the ten papers read (`papers/`), the notes on their form (`forms.json`), the guide (`guide.md`) and the logs of both stages |
| `Style Guide/style3`                                    | Sample 3 (paused turn; empty)                                                                                                         |
| `clean_run`                                             | `style_guide.py` (new, sha256 76288141); `llm.py` (5e9d69ee), `draft.py` (ec04013c) and `review_round.py` (01e276db), changed         |
