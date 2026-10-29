# Summary

Step 2 took the topic files produced in Step 1 and turned them into a shortlist of sixteen theses for the novelty check in Step 3. The Forge generated 279 candidate theses on the question of whether large language models can perform speech acts, ranked the 48 most promising, and put 35 of them through adversarial objection. Two theses survived with little unanswered damage; most survived only in narrower form.

Step 2 cost **$21.64** in API charges across five runs and four smaller calls: $15.80 for the main generation run, $1.30 for tests and diagnostics, and $4.54 for ranking and further attacks, needed because the main run could not separate its leaders. Most of the work went into problems that only appeared once the pipeline met a newer model. Eleven changes were made to the scaffold along the way. All are recorded below, with the evidence that prompted each one.

No philosophical content passed from the custodian, or from the conversation in which the pipeline was managed, to any model that generated or judged theses.

# Two levels of activity

This report distinguishes two levels, and so will the reports for later steps.

**The object level** is where the philosophy is produced. In Step 2 it consisted entirely of scripted calls to the Anthropic API. A model at the object level sees only the area paragraph and literature list written in Step 1, the script’s own prompts, and the outputs of other object-level calls. It has no memory and no access to earlier conversations. Every object-level call is recorded in full in the run folder (`calls.jsonl`), with a summary in `run_log.json`.

**The meta level** is a conversation between the custodian and Claude (configured as Claude Opus 5.5) in the Claude app, with the custodian’s memory turned on. Here the competition rules were interpreted, the scripts were written and repaired, outputs were read and explained, and decisions were discussed. The meta level never sends text to an object-level model. What crosses from meta to object is limited to three things: changes to the scripts, the settings on a command line (model, number of generators, how many theses to attack), and index numbers chosen at a gate.

The distinction matters for eligibility. The meta-level conversation has access to the custodian’s memory, which includes his research and the first paper. Keeping it out of the object level is what keeps Run A’s philosophy machine-originated.

# Inputs

From Step 1 (6 October):

  - `area.txt`: one paragraph stating the question and the rival positions (denials, relocating views, intermediate views, attributing views, and the dispute about agency behind them). Written by Claude in a memory-off chat session. It states no thesis and sketches no argument.
  - `lit.json`: thirteen verified anchor works, 2018–2026, each with a model-written abstract. Expanded from five to thirteen after the custodian sent the flag “The anchor list looks incomplete on the speech-act side of this debate”, in the phrasebook form.

# Timeline and spending

Spending is taken from the custodian’s API balance readings. Token counts are from the run logs. Costs computed from tokens (Sonnet 4.5: $3 in / $15 out per million; Sonnet 5.5: $2 in / $10 out per million) agree with the balance readings to the cent where both exist.

| When (CDT)          | Action                                                              | Model      | Calls      | Tokens in / out             | Balance after | Cost       |
| ------------------- | ------------------------------------------------------------------- | ---------- | ---------- | --------------------------- | ------------- | ---------- |
| 7 Oct, 3:30 PM      | Start                                                               | —          | —          | —                           | $32.32        | —          |
| 7 Oct, 3:34–3:38    | Model probe; small test run (2 generators × 3 theses, 2 attacked)   | Sonnet 4.5 | 18 + probe | 75,716 / 14,735             | $31.83        | $0.49      |
| 7 Oct, 3:43–3:49    | Probe and diagnostic for Sonnet 5.5; failed test run (0 candidates) | Sonnet 5.5 | 2 + 8      | 11,784 / 6,000 (failed run) | $31.63        | $0.20      |
| 7 Oct, 3:52–3:56    | Second test run, after fixes                                        | Sonnet 5.5 | 18         | 102,209 / 40,399            | —             | $0.61      |
| 7 Oct, 4:00–4:34    | **Full generation run** (70 generators × 4, rotation, 25 attacked)  | Sonnet 5.5 | 361        | 2,848,212 / 1,010,717       | $15.22        | $15.80     |
| 11 Oct, 9:58        | Duplicate check and strict ranking of the 48 leaders                | Sonnet 5.5 | 13         | 134,626 / 3,983             | $14.91        | $0.31      |
| 11 Oct, 10:04–10:14 | Attack on 10 more theses                                            | Sonnet 5.5 | 123        | 990,183 / 224,989           | $10.68        | $4.23      |
|                     | **Total for Step 2**                                                |            |            |                             |               | **$21.64** |

Machine time for the full run was 34 minutes of wall-clock time (about 2.5 hours of API time, run in parallel). Custodian time: about 4 hours, over several days (his estimate, supplied 20 October).

# What was changed, and why

Each change below was made at the meta level, to the scripts in the `clean_run` folder, in response to something observed in an object-level output. None changes what a model is asked to argue; all change how candidates are generated, stored, or selected.

## Before Step 2 (built 4 October)

**1. Logging.** Every script now writes `run_log.json` (script and its checksum, the command as typed, every setting, every prompt, the model requested and the model the API reported, times, token totals) and `calls.jsonl` (every call in full). The competition’s methodology report requires this information, and the original scripts recorded none of it.

**2. Neutral prompt examples.** Two prompts contained an example drawn from an error the custodian had caught by hand in an earlier run. Both were replaced with neutral wording.

## During Step 2

**3. Literature truncation (6 October).** The Forge cut each abstract in `lit.json` to its first 400 characters. For one anchor work, those characters describe the view the paper attacks, so generators would have read the author as holding the opposite of his view. The limit was raised to 2,500, then to 4,000 when a revised entry reached 2,412 characters.

**4. Change of model (7 October).** The test run on Sonnet 4.5 worked. The pricing documentation showed that Sonnet 4.5 had been deprecated on 30 September, with retirement scheduled for 30 November; the named replacement is Sonnet 5.5. Since the competition concerns the best current AI performance, the custodian chose to switch on Claude’s recommendation. This means Run A uses a different generator from Paper 1, which used Sonnet 4.5 throughout Stages 1 and 2.

**5. Temperature.** Sonnet 5.5 refuses every temperature setting except its default (a diagnostic showed 0.2 and 0.7 rejected, 1.0 accepted). The scripts now detect the refusal on the first call, stop sending a temperature for the rest of the run, and record this in the log. Generation already ran at 1.0, so nothing changed there. The judging stages (scoring, clustering, adjudication), which had used 0.2 to 0.7 for consistency, now run at the model’s default.

**6. Output allowances.** The first Sonnet 5.5 test produced no candidates: both generators were cut off mid-answer. The output allowances, sized for Sonnet 4.5, are now three times larger for later models. A generator that is still cut off keeps the theses it finished, and any truncated call prints a warning.

*Correction recorded.* At the time this was attributed to the newer model writing at greater length. The full run’s logs show the actual cause: Sonnet 5.5 reasons before it answers, and that reasoning is billed as output. Visible text ran at about 1.4 characters per output token, against 4.5 for Sonnet 4.5. The logs now keep whatever reasoning the API returns.

**7. Rotation of assignments.** In the second test, two isolated generators given the same prompt returned the same three theses, pairwise. Temperature could not be raised to counter this. The Forge now has a `--rotate` option: each generator is assigned one of the five kinds of move (distinction, counterexample, reframing, instability, unnoticed commitment) and, after the first five generators, one of the thirteen anchor works as its starting point. Each is told that its first idea will occur to every other generator with the same assignment. With 70 generators, every move was paired with every work once. In the full run, 265 of 279 theses made the move they were assigned, spread evenly across the works.

**8. Clustering.** In the full run the de-duplication call, asked to compare all 279 theses, spent its whole allowance reasoning and returned nothing. “279 distinct” therefore meant “not checked”. Clustering now asks only for groups of duplicates, not a verdict on every thesis, and runs only on the leaders, where the attack budget is spent.

**9. Strict ranking of the leaders (11 October).** Promise is scored 1 to 5, at most one 5. In the full run the 50 leaders were rescored together and 47 received a 4. The Forge then attacked the top 25 by score, so among the fours the choice of which 24 to attack was decided by the order in which generators finished: in effect, by chance. The leaders are now also put in a strict order. Each is ranked against others in batches of twelve, three times with different shuffles, and its rank is its average standing. This runs automatically in new Forge runs, before the cut.

**10. Extending a finished run.** A new `--attack-more` option continues from an existing run without regenerating: it marks duplicates among the leaders, ranks them, and attacks the best unattacked theses, skipping any whose duplicate has already been attacked. It writes a complete new folder and leaves the earlier one untouched. When given a folder it has already ranked, it reuses that ranking, so the order the custodian reads is the order that gets attacked.

*Deployment error recorded.* The reuse feature did not reach the custodian’s computer before it was needed: the file-transfer step delivered the previous version of the script. The attack therefore drew a fresh ranking and attacked seven of the ten theses expected plus three others. The accident measured the ranking’s stability: across the 48 leaders the two independent rankings correlate at 0.95 (Spearman), with eight of the top ten in common and a median shift of three places. Every script delivery is now checked by comparing checksums on both sides.

**11. An index page.** The Forge’s report never showed the index numbers used to refer to theses downstream. A page listing every attacked thesis by index (`by_index.html`), with its surviving thesis, fatal flaw and objections, was produced for this run and is now written automatically.

# Results

**Generation.** 279 candidates from 70 generators, against 280 requested. Two generators were cut off; the salvage step kept the theses they had finished. Promise scores: 1 at 5, 47 at 4, 162 at 3, 69 at 2.

**Attack.** 35 theses attacked, each by several assigned objections plus a misattribution check, with a defender and an adjudicator. Verdicts: 1 survived, 31 wounded, 3 dead. Two reached the top-right quadrant (promise 4 or more, unanswered damage 2 or less): index 22 (the control conception of intention works at the grain of output, not of the act) and index 37 (proxy accounts conflate endorsing a content with endorsing a generating policy).

**Duplicates.** The checker marks only close restatements. Reading the leaders showed larger families of related theses: one locating the speaker at the wrong level (model, policy, persona or deployment), one about proxy relations, one about status settled after the act, one about the sanction condition on assertion, and one about Barandiaran and Almendros’s “purpose-structured” category.

# Findings about the method

1.  **Isolation does not prevent convergence.** Without rotation, two blind generators produced identical theses. With rotation, the 279 theses spread across all moves and works, though families of related ideas still formed at the top.
2.  **Survival still selects against ambition.** This repeats the Stage 1 finding from Paper 1. In the first ranking, the four theses placed highest were all heavily damaged (one dead, three with unanswered damage of 4), and the one thesis that survived outright ranked 41st of 48 (44th in the second ranking). Neither number should decide on its own.
3.  **A five-point scale cannot select among many good candidates.** Among 48 leaders it produced 47 ties. Ordinal ranking in small batches separated them reliably.
4.  **Newer models reason by default, and this changes the economics.** More than half of Sonnet 5.5’s output tokens were reasoning. The attack phase accounted for about two thirds of the full run’s cost.
5.  **A whole-population comparison fails at scale.** Asking a reasoning model to compare 279 items in one call produced nothing usable.

# Human involvement in Step 2

**At the object level, the custodian:**

  - typed commands, choosing the settings for each run (model, number of generators, how many theses to attack);
  - read the reports;
  - chose the theses to take forward, as index numbers.

He sent no text to any object-level model in Step 2.

**At the meta level:**

  - Claude recommended the model change, rotation, the ranking step and the extension run. The custodian approved each.
  - Claude offered a list of ten candidates, combining rank and unanswered damage. The custodian read all 35 attacked theses and chose twelve: 1, 3, 6, 8, 9, 12, 13, 15, 20, 22, 31 and 46. Five of these overlap with Claude’s list.
  - The custodian then asked that the strongest member of each family of related theses be added where his list had none. “Strongest” was defined as lowest unanswered damage, with rank breaking ties. This added indexes 7, 21, 27 and 37.

All sixteen were selected from machine output. None was edited.

**Disclosure.** The meta-level Claude has memory of the custodian’s research and of the first paper. Its recommendations at the selection gate are AI contributions, not the custodian’s. But they come from a conversation that is not isolated in the way object-level calls are, so they are reported here as part of the selection process.

# Carried into Step 3

  - **Shortlist:** indexes 1, 3, 6, 7, 8, 9, 12, 13, 15, 20, 21, 22, 27, 31, 37, 46 in `Step 2 - Forge/run1_final/raw.json`.
  - **Next action:** the novelty check (`lit_check.py`) on each shortlisted thesis, on Sonnet 5.5, output to `Step 3 - Novelty/lit_N`.
  - **Untested live:** the novelty check on Sonnet 5.5, and every later-stage script (`restate.py`, `source_reader.py`, `draft.py`, `review_round.py`, `pick.py`). These were tested against a stand-in for the API only.
  - **Housekeeping:** the custodian’s `notes.docx` contains an API key in plain text. It should be removed from that file before any notes are shared or included in the methodology report.

# Files

| File                            | Contents                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------- |
| `Step 2 - Forge/test`, `test55` | The two test runs                                                                     |
| `Step 2 - Forge/run1`           | The full generation run: 279 theses, 25 attacked                                      |
| `Step 2 - Forge/run1_ranked`    | Duplicates and the strict ranking of the 48 leaders                                   |
| `Step 2 - Forge/run1_final`     | Final state: 35 attacked; `gate.html`, `ranking.md`, `by_index.html`, `duplicates.md` |
| `clean_run/`                    | The scripts as used, with every change described above                                |
