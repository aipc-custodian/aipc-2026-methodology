# Status

| Run     | Paper                                               | What the human contributes                                              | Where it stands (23 Oct)                                                                   |
| ------- | --------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Paper 1 | *Common Ground as Accidental Convergence*           | Content: the thesis was revised and the outline merged by hand          | Finished; eligibility for an essay prize doubtful, to be disclosed                         |
| Run A   | Paper 2, philosophy of AI                           | Judgment: choices at each gate, by number, and flags in phrasebook form | Steps 1–5 done; Step 6 (final checks and submission) next                                  |
| Run B   | Paper 3, a field outside the custodian’s competence | Custody only                                                            | Not run: the custodian decided on 23 October not to start it. Part III is kept as designed |

The custodian may instead take a second thesis from Run A’s Thesis Forge through Steps 3–6 (Part III-A).

The deadline is **31 October 2026, 11:59 PM Anywhere on Earth**. Allow about ten working days for a run.

This version replaces the first recipe. Parts I and II describe the pipeline as it now stands, after the changes made during Run A. Part III-A covers a second thesis from Run A. Part III is the plan for Run B, which was not run. Items marked **\[to build\]** do not exist yet and must be built and tested before Run B reaches them.

# Part I. Principles

## The rule the competition sets

The test in the competition’s FAQ is whether the AI originated and developed *all* the substantive philosophical contributions. Topics, theses to defend, generic methodological instructions, scaffolds, selection among outputs, flags of unclarity, checks of originality and quotation are all permitted. Supplying arguments, premises, distinctions, examples, outlines, or feedback containing philosophical reasons is not.

At every gate the custodian does one of three things: **chooses** among whole machine outputs, **flags** a problem without its reason or fix, or **relays** text verbatim. If nothing on offer is good enough, the step is rerun. No output is repaired by hand.

| When you notice               | Say this                                                 | Never say this               |
| ----------------------------- | -------------------------------------------------------- | ---------------------------- |
| A weak argument               | “Section 4 is unconvincing.”                             | “Section 4 fails because…”   |
| A fix you can see             | “The paper needs a stronger case in section 3.”          | “Use a case where…”          |
| A missing distinction         | “Section 2 is unclear.”                                  | “Distinguish X from Y.”      |
| A wrong attribution           | “Verify the attribution to X against the source.”        | “X actually holds…”          |
| Possible prior work           | “Check whether this has been argued before.”             | “Y argued this in 2019, so…” |
| An incomplete list            | “The list looks incomplete on the X side of the debate.” | Naming the missing items     |
| A thesis that is nearly right | Pick another, or rerun.                                  | Any rewording.               |

## The standard for “anticipated”

Set by the custodian on 13 October, during Run A, Step 3, after the first novelty check was found to treat a passing mention in a prior paper as if it settled priority. Every script that judges priority applies this one text (`ANTICIPATION_STANDARD` in `llm.py`).

A prior work **anticipates** a claim only if it discusses the claim **extensively** and **either** its author asserts or endorses the claim (*endorsed*), **or** its argument conclusively closes the claim off (*foreclosed*).

Anything short of that is a **precedent**: the claim is raised in passing (*passing*), explored without being endorsed or closed off (*entertained*), or implied by a broader view the work holds without drawing the application (*framework*). A precedent is credited, not conceded: developing an idea someone mentioned is an ordinary philosophical contribution. A work that argues against the claim without closing it off is a **rival** to be answered.

Extent and endorsement can only be judged from the text, so every finding records what was actually seen (full text, abstract, snippet, or a second-hand report), and a verdict of anticipation that rests on less than the full text is **provisional**. In practice the search-based novelty check can rarely confirm anticipation; the full-text reading in Step 3 is where it is settled.

## Two levels

**Object level.** Everything that produces or judges philosophy:

  - the scripts, which call the API and so have no memory;
  - the topic chats in ChatGPT, Gemini and Claude, run with memory and chat search off;
  - the outside referee chats.

Object-level material is saved whole: run folders for scripts, exported conversations for chats.

**Meta level.** A Claude conversation with memory on, in which the custodian discusses the rules, the scripts, the outputs and his decisions. The meta level may write and repair code, explain outputs and recommend settings. It never sends text to an object-level model.

Only these things cross from meta to object:

  - script changes;
  - command-line settings;
  - index numbers chosen at a gate;
  - the custodian’s flags in phrasebook form, which the meta level may help word but never adds content to;
  - text a model wrote and the custodian chose at a gate (such as the thesis), quoted verbatim;
  - source files a model asked for, and published papers chosen by a rule fixed in advance.

Meta-level recommendations at a gate are AI contributions but come from a non-isolated conversation, so each step’s report discloses them.

Each meta-level conversation covers one or two steps. When the custodian says a step is finished, the meta level writes:

1.  a step report in the format of the latest step report: what was run, what changed and why, spending and dates, human involvement at each level;
2.  an update to this recipe;
3.  a hand-off prompt for the next meta-level conversation.

# Part II. The pipeline as it now stands

All scripts are in `Desktop/AI Philosophy Competition/clean_run` and are run from inside that folder. The model for every object-level call is `claude-sonnet-5-5` unless stated. Costs are those measured in Run A.

## Before starting a run

  - [ ] **Object-level chats:** memory paused and chat search off (Settings \> Memory). Do not use incognito chats, which cannot be reopened.
  - [ ] **API key:** set it in Terminal with `export ANTHROPIC_API_KEY=…` in each new window. Keep it out of notes and logs.
  - [ ] **Run folder:** create one for the run, with a subfolder per step.
  - [ ] **Probes:** `python3 llm.py --probe claude-sonnet-5-5` and `python3 lit_check.py --probe`; before Step 4, also `python3 llm.py --probe claude-opus-5-5`; before Step 5, also `python3 llm.py --probe claude-fable-5-1` (Fable 5.1 costs $10/M in and $50/M out).
  - [ ] **After any script change:** confirm the copy on the Mac matches the one that was tested by comparing checksums, and send each new version from a fresh, uniquely named staging folder. In Run A a delivery arrived one version behind three times; each time the checksum caught it.
  - [ ] **Spending log:** read the API balance before and after each run.
  - [ ] **Time log:** a line per step with the minutes you spent.

## Behaviour of the 5.5 models that the scripts now handle

  - **Temperature:** Sonnet 5.5 and Opus 5.5 both accept only their default (Opus accepted 1.0 and refused 0.2). The scripts detect the refusal, run every later call at the default, and log the fact.
  - **Reasoning:** it reasons before answering, and the reasoning is billed as output, typically more than half of all output tokens. Output allowances are three times those used for Sonnet 4.5, in the shared `llm.py` and in every script that keeps its own API code (`thesis_forge.py`, `lit_check.py`, `outline_deviser.py`). Large allowances need streamed calls, which all scripts now use.
  - **Truncation:** a call that still hits its allowance prints a warning. A cut-off generator keeps the theses it finished.
  - **Paused turns:** a call that runs many searches can come back paused (`pause_turn`). The shared `llm.py` now sends it back to continue, up to six times, and logs each continuation (change 19). The scripts with their own API code (`thesis_forge.py`, `lit_check.py`, `outline_deviser.py`) do not yet do this; their calls search less, and none has paused so far.
  - **Searches are costly beyond their fee.** Each search’s results are added to the context and billed as input. A turn with 28 searches cost $3.22, almost all of it in input tokens.

## Step 1. Topic

1.  Ask ChatGPT and Gemini, separately, with search on, for ten active debates. Use the prompt in the first recipe, changing the field as Part III specifies.
2.  In a memory-off Claude chat, paste both answers verbatim and ask for a merged, verified list, ranked by room for a new position.
3.  Pick the topic (Run A) or have Claude pick (Run B).
4.  In the same chat, ask Claude to write `area.txt` (one paragraph: the question and the rival positions, no thesis, no sketch) and `lit.json` (verified anchor works with accurate abstracts).
5.  **New:** the seed prompt now also tells Claude that `lit.json` must include at least one anchor work for every position named in `area.txt`, and that every abstract must state the work’s conclusion. In Run A both gaps had to be caught by flags.
6.  Save the conversation whole.

Cost: nothing beyond the chat subscriptions.

## Step 2. Thesis Forge

    python3 thesis_forge.py --area "$(cat area.txt)" --literature lit.json \
        --model claude-sonnet-5-5 --rotate --generators 70 --per-generator 4 \
        --out "<run>/Step 2 - Forge/run1"

What happens:

  - **Generate:** 70 isolated generators, each assigned a kind of move and, after the first five, an anchor work to start from (`--rotate`).
  - **Score:** promise on a 1–5 scale.
  - **Rank:** the leaders (everything scoring 4 or 5) are checked for duplicates and put in a strict order.
  - **Attack:** the top 25 by rank face assigned objections, a defender and an adjudicator.
  - **Report:** `gate.html` (the full report), `ranking.md` (the leaders in order) and `by_index.html` (every attacked thesis by index, with its surviving thesis, fatal flaw and objections).

Cost: about $16–17 and 35 minutes.

To attack further down the ranking without regenerating:

    python3 thesis_forge.py --area "$(cat area.txt)" --literature lit.json \
        --model claude-sonnet-5-5 --attack-more "<run>/Step 2 - Forge/run1/raw.json" \
        --attack-top 10 --out "<run>/Step 2 - Forge/run1_final"

This marks duplicates, reuses the ranking already in the folder, skips theses whose twin has been attacked, and attacks the next ten. It costs about $0.40 a thesis.

**Reading the results.** Promise (1–5) is scored before any attack; higher is better. Residual (0–5) is the strongest objection left unanswered; lower is better. Worst is the strongest objection mounted at all. Read the surviving thesis, not the headline: it is what the paper would argue.

In Run A the ranker favoured ambitious theses and the attack broke them, so take both numbers into account at the gate.

## Step 3. Novelty, sources, outlines

Run A spent $36.51 and about 7 hours of the custodian’s time on this step, including a rerun of the novelty check after the anticipation standard was set. Without the rerun, expect about $20.

**1. Novelty check** on each shortlisted thesis, about $0.78 each (five calls, eight searches, two minutes):

    for i in <indices>; do python3 lit_check.py \
        --raw "<run>/Step 2 - Forge/run1_final/raw.json" --index $i \
        --model claude-sonnet-5-5 --out "<run>/Step 3 - Novelty/lit_$i"; done

Read `lit.html`. Each finding has a relation (anticipated, precedent, contradicted, supported, adjacent), a grade, and what it rests on. “What is left” is advice, not a restatement: no thesis is narrowed at this stage.

**2. Optional: cross-family priority check.** For each shortlisted thesis, `lit_check.py --raw ... --index N --priority-prompt --out priority_N` prints and saves a prompt that includes the anticipation standard. Paste it into ChatGPT (search on, memory off) and save the reply unedited as `reply.md` in the same folder. The reply then goes to the source list with `--external`. Prompts were prepared in Run A, but the custodian decided not to run the step.

**3. Shortlist and rank order** (Run A), or the fixed rule (Run B). Fix the rank order of the keepers **before any source is read**, and fix the rule for elimination: move to the next thesis if a work read in full meets the anticipation standard for the central claim. A later replacement then follows a rule, not a fresh judgment.

**4. Sources** for the top thesis. The model lists what it needs, drawing on every novelty check run on that thesis (repeat `--lit`; add `--external` for a cross-family reply). About $0.50:

    python3 source_reader.py --raw <forge raw.json> --index N \
        --lit lit_N/raw.json --lit lit_N_v2/raw.json --needs \
        --model claude-sonnet-5-5 --out needs_N

Fetch every work listed, into `Sources_N/`, and nothing else. Where a link points to a catalogue record, fetch an open-access copy of the same work. A PDF over about 100 pages must be cut to the relevant chapter. Then the full reading, about $0.17 a work:

    python3 source_reader.py --raw <forge raw.json> --index N \
        --sources Sources_N --model claude-sonnet-5-5 --out notes_N

Check every quotation in `notes.md` against the PDFs (in Run A all 56 matched). If a work read in full meets the standard for the central claim, apply the elimination rule.

**5. Restatement**, always, after the reading. About $0.10:

    python3 restate.py --raw <forge raw.json> --index N --lit lit_N_v2/raw.json \
        --notes notes_N/notes.md --model claude-sonnet-5-5 --out restate_N

The model narrows only for anticipation in the standard’s sense, and lists the works to credit. If the status is NOTHING NEW REMAINS, apply the elimination rule. Otherwise choose between the restated and the original thesis (a selection between machine outputs), and use `--raw restate_N/raw.json --index 0` from then on. Known flaw: the status can say UNCHANGED when a clarifying gloss was added, so read the text.

**6. Outlines.** Six independent outlines, about $2.10 and eight minutes:

    python3 outline_deviser.py --raw restate_N/raw.json --index 0 \
        --notes notes_N/notes.md --outlines 6 \
        --model claude-sonnet-5-5 --out outlines_N

Then the attribution check, about $4.20:

    python3 lit_check.py --raw outlines_N/raw.json \
        --model claude-sonnet-5-5 --out attr_N

Read the verdicts per outline (holds, distorted, cannot tell). Ignore the list of “citations that do not resolve”: its existence test treats quoted phrases as titles. A distortion that states a rival’s view without its conditions is a scholarship error; one in the load-bearing section that aims the argument at a view nobody holds is worse.

**7. Choose an outline**, whole and by number. If its attributions failed, a model rewrites only the passages that name other authors, about $0.16:

    python3 outline_deviser.py --raw outlines_N/raw.json --rework K \
        --attr attr_N/raw.json --model claude-sonnet-5-5 --out outlines_N_reworkK

`--merge A,B` remains for two outlines that are each half right. Never use `--thesis` with your own wording, or `--with-sketch`.

**8. Close the reading gap.** If the chosen outline relies on works that were not read in full, fetch them (the outline named them), read them with `source_reader.py --sources` into a separate folder, and join the notes into one file for drafting:

    cat notes_N/notes.md notes_Nx/notes.md > notes_N_all.md

## Step 4. Drafting

    python3 draft.py --raw outlines_N_reworkK/raw.json --outline K \
        --notes notes_N_all.md --drafts 3 --rank --out drafts1

Three isolated drafts on Opus 5.5 ($4 in / $20 out per million tokens), each told to stay under 5,700 words, with no voice model, an anonymous register, and citations verified. A second model ranks them. Choose one whole. A reworked outline is numbered 0 in its own file, so use `--outline 0` with it. Run a dry run first (`--dry-run`) to check the thesis and outline it has loaded.

In Run A (20 October) this cost $2.67 and took four minutes: about $0.86 a draft, plus $0.10 for the ranking. No call was cut off, and all three drafts came in between 5,561 and 5,620 words.

**Reading the drafts.** Choose on what review cannot repair. A citation slip, drafting residue or an under-defended step can be met by a flag in Step 5. The architecture of a section’s argument cannot be changed without rerunning the drafts. In Run A the drafts differed in where their strength lay, and the ranker and the custodian chose differently.

For Run B, add `--style` with the presentation guide (below), so the drafts start from it.

## The presentation guide (built once; reusable)

A model learns how published papers are built and presented, and the drafter is given what it finds. It is built once and kept in `Style Guide/` for every later run.

    python3 style_guide.py --sample --out "../Style Guide/styleN"
    (fetch every article listed in styleN/sample.md into styleN/papers/, and nothing else)
    python3 style_guide.py --read "../Style Guide/styleN/papers" --out "../Style Guide/styleN"

  - **Sample.** One call with search. It takes the five general analytic journals most widely ranked highest, and the first three research articles of each one’s first 2025 issue. It skips lectures and other non-research pieces, and any article on the paper’s own subject (`--exclude`; the default covers Run A’s subject). It must list exactly three per journal or say why not, and must not infer authors. About $1.10–1.40.
  - **Read.** One call per paper, describing its form only; then one call that writes the guide with counts. About $0.17 a paper.
  - **Using it.** Pass `--style "../Style Guide/style2/guide.md"` to `review_round.py`, and to `draft.py` in a run that has not drafted yet. It goes only to the drafter, beneath every other instruction, and is saved in each run log.
  - **Run A’s guide** is `Style Guide/style2/guide.md`. It was built from ten articles: the union of two draws, with the tightened rule applied to both. Those were one article from *Philosophical Review*, and three each from *Noûs*, *PPR* and *Mind*. The *Journal of Philosophy* was lost to retrieval limits. Do not raise `--max-uses` to recover a journal: a 40-search draw paused, returned nothing, and cost $3.22.
  - **Run B** reuses this guide. If Run B’s field overlaps the default exclusions, nothing needs rebuilding, since the exclusions only keep content out of the sample.

## Step 5. Review and revision

Run A spent $30.59 on this step over 21–23 October, including a $5.39 calibration run and about $2.70 lost to a round started too early. Without those, expect about $20 for three rounds and a custodian pass. Each round’s largest cost is the Claude referee (Fable 5.1), whose searches are billed as input at $10/M.

**Each round.** Run `python3 review_round.py --show-prompt`. Paste the printed prompt and the full paper into **new** ChatGPT and Gemini chats, with search on and memory off. Save each reply with the chat’s own copy button (`pbpaste > chatgpt.txt`): copying the rendered page can turn spaces into replacement characters and lose subscripts. Save the replies unedited in `reviews_rN/`, with nothing else in the folder. Then run:

    python3 review_round.py --paper <paper.md> --reviews reviews_rN \
        --claude-referee claude-fable-5-1 --notes notes_N_all.md \
        --style "../Style Guide/style2/guide.md" --words 5400 --out roundN

The script refuses to run if the reviews folder is empty (change 28). An independent adjudicator rules each concern MUST ADDRESS, OPTIONAL or MISTAKEN, checking literature claims by search against the anticipation standard. Then the drafter revises.

  - **Revision prompt.** The drafter must answer every MUST ADDRESS concern. It is told that every answer has a cost, and that narrowing a claim, dropping one, or acknowledging an objection and setting it aside are full answers (change 23). The paper must read as written once, with no mention of earlier drafts or referees (change 21). It may use footnotes, which count toward the limit (change 26).
  - **Length.** Aim at `--words 5400`: revisions overshoot their target by about 500 words. If the revision is over, up to three cut passes follow. A cut removes redundancy first, then states replies, examples and minor objections more briefly, but removes none of them (change 25).

**Stopping rule (change 24).** A round with **2 or fewer** concerns ruled MUST ADDRESS stops without revising, and its input paper stands (`--stop-at`, default 2). In any case stop after three rounds. The figure 2 comes from a calibration run in which a 2025 *Mind* article went through the same referee prompt, referees and adjudicator and drew 2 MUST ADDRESS (Draft 1 drew 8). A rule of “nothing ruled MUST ADDRESS” would never stop, since model referees always find something; the adjudicator, unlike the referees’ verdicts, does discriminate. To repeat a calibration run, fix the rule for choosing the paper before reading anything, convert it to Markdown, remove its author’s identifying matter mechanically, and run `--reviews <folder> --claude-referee claude-fable-5-1 --no-revise`.

**Custodian pass (change 27), optional, between rounds.** Read the paper and write flags in phrasebook form, one numbered line each, in `custodian_flags/custodian.txt`. Keep this file out of every reviews folder. Then run:

    python3 review_round.py --paper <paper.md> --flags custodian_flags/custodian.txt \
        --notes notes_N_all.md --style "../Style Guide/style2/guide.md" \
        --words 5400 --out custodian_pass

This skips the referee and the adjudicator, and the drafter must act on every flag. Get the next round’s outside reviews only after the pass, so that they review the restructured paper. Run A’s custodian pass came between rounds 2 and 3. It restated the thesis chosen at Step 3, which the drafts had drifted away from, and it brought the paper from 6,060 words (over the limit) to 5,395. Round 3 then stopped at the baseline. Do not run a second pass with the same flags: once a flag has been acted on, it points at text that has moved, and repeating it produces churn.

**Flags.** A flag names a problem or asks for a rearrangement. It gives no reason, no suggested wording and no hint toward an argument. Naming the thesis chosen for the paper, verbatim, is permitted. Never pass text from an unchosen draft. Refer to passages in words (“the third paragraph of §1”), since the model never sees a reading copy’s paragraph labels.

**Reading copies.** To print a paper, convert it with `pandoc -f markdown-fancy_lists`. Otherwise “(L)” at the start of a paragraph is read as a list marker.

## Step 6. Final checks and submission

  - [ ] **Citations:** attribution check on the final essay, and every quotation checked against its source. Work through the list carried forward in the Step 5 report (page references, names, DOIs, works to credit).
  - [ ] **Originality:** compare the essay with the closest survey or encyclopedia entries the referees named.
  - [ ] **Length:** at most 6,000 words excluding the bibliography, footnotes included, by two different counters.
  - [ ] **Anonymity:** no name, byline or self-citation in the essay; clear the file’s author field; the methodology report refers to “the custodian”.
  - [ ] **No prompt injection:** no instructions addressed to a reader or screener anywhere in the text.
  - [ ] **Methodology report:** assembled from the step reports and run logs, with chat logs attached.
  - [ ] **Submission:** OpenReview only.
  - [ ] **Memory:** turn it back on afterwards.

# Part III-A. A second thesis from Run A

Instead of Run B, the custodian may take another thesis already generated and attacked in Run A’s Thesis Forge (Step 2) through Steps 3–6. One candidate is index 3 (`run1_final`): Austin’s distinction between abuses and misfires, applied to intention-based denials of LLM speech acts. It already has two novelty checks (`lit_3`, `lit_3_v2`) and a priority prompt (`priority_3`). The pipeline is Part II from Step 3, item 4 (sources), with the custodian’s judgment at each gate as in Run A. The choice of thesis is made by index number and disclosed. If the thesis is in the custodian’s own research area, say so in the methodology report. Budget about $20 for Step 3 without reruns, $3 for Step 4 and $20 for Step 5, and allow about a day per step at the least.

# Part III. Run B: the custodian-only run

Not run. On 23 October the custodian decided not to start Run B: a start after about 23 October left no time for Steps 3–6, and the shortlist rule and `pick.py --thesis` had not been built. The plan below is kept as designed, and the methodology report should describe it as planned but not run.

## What changes

In Run B a model makes every choice the custodian made in Run A. The custodian runs commands, fetches the files the model asks for, and pastes the outside referee reports. His only remaining contribution of judgment is the list of fields excluded at Step 1, which is what puts the run outside his competence. That list is disclosed.

| Gate                      | Run A                                                             | Run B                                                                                |
| ------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Field                     | Philosophy of AI, chosen by the custodian                         | Philosophy outside the excluded fields                                               |
| Topic                     | Custodian picks from Claude’s merged list                         | Claude picks: “choose the debate with the most room for a new position, and say why” |
| Anchor completeness       | Caught by a custodian flag                                        | Built into the seed prompt (Step 1, item 5)                                          |
| Shortlist after the Forge | Custodian reads and chooses                                       | Fixed rule **\[to build\]**                                                          |
| Thesis                    | Custodian chooses after novelty, by a rank order fixed in advance | `pick.py --thesis` **\[to update\]**                                                 |
| Restatement               | `restate.py`, after sources, with the reading notes               | Same                                                                                 |
| Sources                   | Model lists, custodian fetches                                    | Same; every work listed, plus those the chosen outline relies on, and nothing else   |
| Outline                   | Custodian chooses                                                 | `pick.py --outline`                                                                  |
| Merge or rework           | Custodian names outlines                                          | `pick.py` reports a rework when attributions failed; no merges                       |
| Draft                     | Custodian chooses                                                 | `pick.py --draft` (the second model’s first choice); `--style`                       |
| Review                    | Custodian pastes outside reviews                                  | Same                                                                                 |

## Step 1 for Run B

Use the Run A prompt with one change: replace “the philosophy of artificial intelligence” with “philosophy, excluding philosophy of language, philosophy of mind, cognitive science, philosophy of artificial intelligence, and the philosophy of friendship”. The custodian should confirm the exclusion list before starting, since it is his one contribution. In the merge chat, add: “Then choose the debate with the most room for a new position, and say why.” Apply the strengthened seed prompt from Part II.

## Steps 2 to 6 for Run B

  - **Step 2.** As in Part II. A second `--attack-more` round of 10 is part of the plan, not a judgment call.
  - **Shortlist \[to build\].** A rule replacing the custodian’s reading. The proposal, to be settled at the meta level before Run B reaches Step 3: from the attacked theses that are not dead, take the six with the lowest residual (rank breaking ties), plus the two highest-ranked theses with residual 4. This is an “ambition quota” in response to Run A’s finding that the ranker and the attack pull in opposite directions. Run the novelty check on all eight.
  - **Thesis \[to update\].** `pick.py --thesis` currently reads a novelty file covering several theses from `lit_check.py --top`, which sorts by promise alone and so inherits the ties problem. It needs to read the shortlist instead. It already applies the anticipation standard and prints the commands in the new order (sources, then restatement).
  - **Steps 3–6.** As in Part II, with `pick.py` at each gate. It prints the exact command to run next.

## Budget and schedule

| Item                                                       | Run A actual                                                                                           |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Step 2 (Forge, ranking, extra attacks)                     | $21.64 (including about $1.30 of tests)                                                                |
| Step 3 (novelty, sources, outlines, attribution)           | $36.51, including a $12.66 rerun under the new standard; about $20 without it                          |
| Step 4 (three drafts and ranking)                          | $2.74, with the Opus probe                                                                             |
| Presentation guide (once, reusable)                        | $7.46, with a void $3.22 draw                                                                          |
| Step 5 (three rounds, a custodian pass, a calibration run) | $30.59, including the $5.39 calibration and about $2.70 lost to an early start; about $22 without them |
| Total, Steps 2–5                                           | $98.94                                                                                                 |

Run B was not run (see the note at the head of Part III).

# Part IV. What Run A has taught so far

1.  **Isolation does not prevent convergence.** Give the generators different questions, not just different dice.
2.  **Survival selects against ambition.** Do not let either promise or survival decide alone.
3.  **Coarse scores make arbitrary cuts.** Rank the leaders.
4.  **Whole-population comparisons fail at scale** with a reasoning model.
5.  **Newer models change the costs and the failure modes.** Test every stage on the model before the full run.
6.  **The scaffold changed more than expected.** Eleven changes in Step 2, five in Step 3, four in Step 4 and seven in Step 5. Every change is recorded with the evidence that prompted it, for the methodology prize.
7.  **Say what “anticipated” means before checking for it.** Under an explicit standard, the same searches gave different verdicts.
8.  **Read before narrowing.** A search sees abstracts and snippets and can rarely confirm anticipation; the full-text reading is the real filter.
9.  **Independent searches find different literatures.** Feed every check into the reading list.
10. **Every copy of model-handling code must change when the model does.** The Step 2 fix missed two code paths.
11. **Choose drafts on what review cannot repair.** Fixable faults are poor grounds for choosing; the architecture of the argument is what a choice fixes.
12. **Learn the discipline’s conventions from the discipline.** A guide drawn from published papers corrected an assumption built into the scaffold (that signposting is padding).
13. **Search-heavy calls are expensive and can pause.** Keep search budgets modest; the shared client now continues paused turns.
14. **Model referees are never satisfied; the adjudicator is the gate.** ChatGPT recommended major revisions for a published *Mind* article it recognised. Calibrate the stopping rule against a published paper, not against perfection.
15. **Answering every objection thickens a paper.** Under a word limit each answer is paid for in density. Tell the reviser that answers have a cost, and let the cut shorten as well as remove.
16. **Theses drift.** The drafts and early revisions argued for something stronger than the thesis chosen at Step 3, and that stronger claim drew the referees’ fire. Check the paper against the chosen thesis after drafting, and restate the thesis to the reviser if needed.
17. **Keep structural flags apart from refereeing.** A custodian pass with binding flags did more for the paper’s shape than any review round, and the referees then judged the paper the custodian meant to send.
18. **Guard the expensive steps against human slips.** A round started before its reviews were saved cost about $2.70. Scripts should refuse to run with missing inputs.
