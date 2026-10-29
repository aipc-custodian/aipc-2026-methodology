# Status

| Run     | Paper                                               | What the human contributes                                      | Where it stands (20 Oct)                                           |
| ------- | --------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------ |
| Paper 1 | *Common Ground as Accidental Convergence*           | Content: the thesis was revised and the outline merged by hand  | Finished; eligibility for an essay prize doubtful, to be disclosed |
| Run A   | Paper 2, philosophy of AI                           | Judgment: choices at each gate, by number                       | Steps 1–3 done; Step 4 (drafting) next                             |
| Run B   | Paper 3, a field outside the custodian’s competence | Custody only: commands, fetching files, pasting outside reviews | Not started; was due to begin by 18 October                        |

The deadline is **31 October 2026, 11:59 PM Anywhere on Earth**. Allow about ten working days for a run.

This version replaces the first recipe. Parts I and II describe the pipeline as it now stands, after the changes made during Run A. Part III is the plan for Run B. Items marked **\[to build\]** do not exist yet and must be built and tested before Run B reaches them.

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

Only three things cross from meta to object:

  - script changes;
  - command-line settings;
  - index numbers chosen at a gate.

Meta-level recommendations at a gate are AI contributions but come from a non-isolated conversation, so each step’s report discloses them.

Each meta-level conversation covers one or two steps. When the custodian says a step is finished, the meta level writes:

1.  a step report in the format of the Step 2 report: what was run, what changed and why, spending and dates, human involvement at each level;
2.  an update to this recipe;
3.  a hand-off prompt for the next meta-level conversation.

# Part II. The pipeline as it now stands

All scripts are in `Desktop/AI Philosophy Competition/clean_run` and are run from inside that folder. The model for every object-level call is `claude-sonnet-5-5` unless stated. Costs are those measured in Run A.

## Before starting a run

  - [ ] **Object-level chats:** memory paused and chat search off (Settings \> Memory). Do not use incognito chats, which cannot be reopened.
  - [ ] **API key:** set it in Terminal with `export ANTHROPIC_API_KEY=…` in each new window. Keep it out of notes and logs.
  - [ ] **Run folder:** create one for the run, with a subfolder per step.
  - [ ] **Probes:** `python3 llm.py --probe claude-sonnet-5-5` and `python3 lit_check.py --probe`.
  - [ ] **After any script change:** confirm the copy on the Mac matches the one that was tested by comparing checksums, and send each new version from a fresh, uniquely named staging folder. In Run A a delivery arrived one version behind three times; each time the checksum caught it.
  - [ ] **Spending log:** read the API balance before and after each run.
  - [ ] **Time log:** a line per step with the minutes you spent.

## Behaviour of Sonnet 5.5 that the scripts now handle

  - **Temperature:** it accepts only its default. The scripts detect the refusal, run every later call at the default, and log the fact.
  - **Reasoning:** it reasons before answering, and the reasoning is billed as output, typically more than half of all output tokens. Output allowances are three times those used for Sonnet 4.5, in the shared `llm.py` and in every script that keeps its own API code (`thesis_forge.py`, `lit_check.py`, `outline_deviser.py`). Large allowances need streamed calls, which all scripts now use.
  - **Truncation:** a call that still hits its allowance prints a warning. A cut-off generator keeps the theses it finished.

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

Three isolated drafts on Opus 5.5, each told to stay under 5,700 words, with no voice model, an anonymous register, and citations verified. A second model ranks them. Choose one whole. Not yet run live: check the first run before relying on it. A reworked outline is numbered 0 in its own file, so use `--outline 0` with it.

## Step 5. Review and revision

    python3 review_round.py --show-prompt

Paste the printed prompt and the paper to ChatGPT and Gemini, with search on and memory off, and save each reply unedited in `reviews_rN/`. Then:

    python3 review_round.py --paper drafts1/draft_D.md --reviews reviews_r1 \
        --claude-referee claude-fable-5-1 --notes notes_N/notes.md --out round1

An independent adjudicator rules each concern MUST ADDRESS, OPTIONAL or MISTAKEN, after checking literature claims by search. The drafter revises and cuts to under 5,800 words. Repeat until nothing is ruled MUST ADDRESS, or for three rounds at most.

## Step 6. Final checks and submission

  - [ ] **Citations:** attribution check on the final essay, and every quotation checked against its source.
  - [ ] **Length:** at most 6,000 words excluding the bibliography, by two different counters.
  - [ ] **Anonymity:** no name, byline or self-citation in the essay; clear the file’s author field; the methodology report refers to “the custodian”.
  - [ ] **No prompt injection:** no instructions addressed to a reader or screener anywhere in the text.
  - [ ] **Methodology report:** assembled from the step reports and run logs, with chat logs attached.
  - [ ] **Submission:** OpenReview only.
  - [ ] **Memory:** turn it back on afterwards.

# Part III. Run B: the custodian-only run

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
| Draft                     | Custodian chooses                                                 | `pick.py --draft` (the second model’s first choice)                                  |
| Review                    | Custodian pastes outside reviews                                  | Same                                                                                 |

## Step 1 for Run B

Use the Run A prompt with one change: replace “the philosophy of artificial intelligence” with “philosophy, excluding philosophy of language, philosophy of mind, cognitive science, philosophy of artificial intelligence, and the philosophy of friendship”. The custodian should confirm the exclusion list before starting, since it is his one contribution. In the merge chat, add: “Then choose the debate with the most room for a new position, and say why.” Apply the strengthened seed prompt from Part II.

## Steps 2 to 6 for Run B

  - **Step 2.** As in Part II. A second `--attack-more` round of 10 is part of the plan, not a judgment call.
  - **Shortlist \[to build\].** A rule replacing the custodian’s reading. The proposal, to be settled at the meta level before Run B reaches Step 3: from the attacked theses that are not dead, take the six with the lowest residual (rank breaking ties), plus the two highest-ranked theses with residual 4. This is an “ambition quota” in response to Run A’s finding that the ranker and the attack pull in opposite directions. Run the novelty check on all eight.
  - **Thesis \[to update\].** `pick.py --thesis` currently reads a novelty file covering several theses from `lit_check.py --top`, which sorts by promise alone and so inherits the ties problem. It needs to read the shortlist instead. It already applies the anticipation standard and prints the commands in the new order (sources, then restatement).
  - **Steps 3–6.** As in Part II, with `pick.py` at each gate. It prints the exact command to run next.

## Budget and schedule

| Item                                             | Run A actual or estimate                                                             |
| ------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Step 2 (Forge, ranking, extra attacks)           | $21.64 actual (including about $1.30 of tests)                                       |
| Step 3 (novelty, sources, outlines, attribution) | $36.51 actual, including a $12.66 rerun under the new standard; about $20 without it |
| Step 4 (three drafts and ranking)                | about $5–10                                                                          |
| Step 5 (three review rounds)                     | about $5–10, plus the outside chats                                                  |
| Total per run                                    | about $55–75                                                                         |

Run B was to start Step 1 no later than 18 October to leave room for one rerun. As of 20 October it has not started; whether it goes ahead before 31 October is the custodian’s decision.

# Part IV. What Run A has taught so far

1.  **Isolation does not prevent convergence.** Give the generators different questions, not just different dice.
2.  **Survival selects against ambition.** Do not let either promise or survival decide alone.
3.  **Coarse scores make arbitrary cuts.** Rank the leaders.
4.  **Whole-population comparisons fail at scale** with a reasoning model.
5.  **Newer models change the costs and the failure modes.** Test every stage on the model before the full run.
6.  **The scaffold changed more than expected.** Eleven changes in Step 2 and five in Step 3. Every change is recorded with the evidence that prompted it, for the methodology prize.
7.  **Say what “anticipated” means before checking for it.** Under an explicit standard, the same searches gave different verdicts.
8.  **Read before narrowing.** A search sees abstracts and snippets and can rarely confirm anticipation; the full-text reading is the real filter.
9.  **Independent searches find different literatures.** Feed every check into the reading list.
10. **Every copy of model-handling code must change when the model does.** The Step 2 fix missed two code paths.
