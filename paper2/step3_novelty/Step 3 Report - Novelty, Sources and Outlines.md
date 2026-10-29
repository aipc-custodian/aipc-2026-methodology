# Summary

Step 3 took the sixteen theses shortlisted in Step 2 and ended with one thesis, a reading of its fourteen most relevant sources in full, and a chosen outline. It ran a novelty check on all sixteen theses, ranked the survivors, chose thesis 1, had a model list the works it needed and read them in full, had a model restate the thesis in light of those readings, generated six independent outlines, checked their attributions, and repaired the chosen outline’s one misattribution.

The most consequential event was a change of standard. After the first novelty check, the custodian judged that the check treated a passing mention in a prior paper as if it settled priority, which would rule out promising theses for no good reason. He set an explicit standard for “anticipated” (below), and every script that judges priority was changed to apply it. The novelty check was then rerun on all sixteen theses under the new standard, and the shortlist was revised once, before any source was read.

Step 3 cost **$36.51** in API charges. About $12.70 of that was the rerun under the new standard, and $1.10 was a failed outline run. Five changes were made to the scaffold. All are recorded below with the evidence that prompted each.

No philosophical content passed from the custodian, or from the conversation in which the pipeline was managed, to any model that generated or judged philosophy.

# Two levels of activity

As in Step 2, the **object level** consisted of scripted calls to the Anthropic API, each with no memory and no access to earlier conversations, recorded in full in each run folder (`calls.jsonl`, `run_log.json`). The **meta level** was a Claude conversation (configured as Claude Opus 5.5) with the custodian’s memory on, in which the rules were interpreted, scripts written and repaired, outputs explained and decisions discussed. Only script changes, command-line settings and index numbers crossed from meta to object.

Two further things crossed in Step 3, both argument-neutral and both disclosed here: the **anticipation standard**, a methodological instruction the custodian wrote and which was built into the prompts (change 13); and **source files**, the PDFs the custodian fetched because a model asked for them, and no others.

# Inputs

From Step 2 (7–11 October): sixteen theses by index in `Step 2 - Forge/run1_final/raw.json`: 1, 3, 6, 7, 8, 9, 12, 13, 15, 20, 21, 22, 27, 31, 37, 46. Each was checked as its post-attack “surviving thesis”, not its headline.

# Timeline and spending

Spending is from the custodian’s API balance readings; token counts are from the run logs. Sonnet 5.5 is billed at $2 in / $10 out per million tokens, plus $10 per thousand web searches. Costs computed from tokens agree with the balance readings to within five cents over the step.

| When (CDT)             | Action                                                          | Calls | Tokens in / out     | Search | Balance | Cost       |
| ---------------------- | --------------------------------------------------------------- | ----- | ------------------- | ------ | ------- | ---------- |
| 11 Oct, 2:20 PM        | Start                                                           | —     | —                   | —      | $10.68  | —          |
| 11 Oct, 2:24           | Novelty check, test on thesis 22 (first live run on Sonnet 5.5) | 5     | 264,731 / 14,449    | 8      | $9.88   | $0.80      |
| 11 Oct, 2:38           | Top-up                                                          |       |                     |        | $29.88  | \+$20.00   |
| 11 Oct, 2:39–3:11      | Novelty check, the other fifteen theses                         | 75    | 4,036,359 / 255,327 | 120    | $18.05  | $11.83     |
| 13 Oct, 10:47–10:53 AM | Novelty check under the new standard, test on theses 12, 15, 27 | 15    | 798,750 / 44,770    | 24     | $15.77  | $2.28      |
| 13 Oct, 11:27–11:57    | Novelty check under the new standard, the other thirteen        | 65    | 3,561,616 / 221,043 | 104    | $5.39   | $10.38     |
| 13 Oct, 12:23 PM       | Source list for thesis 1, from the second novelty check only    | 1     | 177,240 / 6,319     | 10     | $4.88   | $0.51      |
| 13 Oct, 12:28          | Source list for thesis 1, from both novelty checks              | 1     | 176,184 / 4,769     | 10     | $4.38   | $0.50      |
| 19 Oct, before 4:14 PM | Top-up                                                          |       |                     |        | $24.38  | \+$20.00   |
| 19 Oct, 4:14–4:16      | **Full reading of 12 sources**                                  | 12    | 825,897 / 33,887    | 0      | $22.38  | $2.00      |
| 19 Oct, 4:28           | Restatement of thesis 1                                         | 1     | 40,421 / 1,302      | 0      | —       | $0.09      |
| 19 Oct, 5:09–5:13      | Outline run, failed (every call cut off; stopped by hand)       | 6     | 180,330 / 73,728    | 0      | $21.19  | $1.10      |
| 19 Oct, 5:16–5:24      | **Six outlines**, after the fix (change 16)                     | 7     | 186,029 / 173,510   | 0      | $19.09  | $2.10      |
| 19 Oct, 5:43–5:45      | Attribution check on the six outlines                           | 27    | 1,435,137 / 47,155  | 87     | $14.87  | $4.22      |
| 20 Oct, 11:38–11:41 AM | Rework of outlines 0 and 4                                      | 2     | 74,421 / 16,898     | 0      | —       | $0.32      |
| 20 Oct, 11:56          | Full reading of two further sources                             | 2     | 167,922 / 5,261     | 0      | $14.17  | $0.38      |
|                        | **Total for Step 3**                                            |       |                     |        |         | **$36.51** |

The custodian did not take a balance reading after the restatement; its cost is from tokens, and the balance reading that follows covers both it and the failed outline run. The same applies to the two reworks and the final reading.

Machine time: about 2 hours of API time across all runs. Custodian time: **about 7 hours**, over several days (his estimate). For comparison, Step 2 took about 4 hours of custodian time.

# What was changed, and why

Numbering continues from the Step 2 report. Each change was made at the meta level in response to something observed in an object-level output.

**12. Output allowances in the shared client (13 October).** The ×3 output allowance for Sonnet 5.5 (Step 2, change 6) had been added to the three scripts that keep their own API code, but not to the shared `llm.py` used by `restate.py`, `source_reader.py`, `draft.py`, `review_round.py` and `pick.py`. Those five had only been tested against a stand-in, so the gap had not shown. On Sonnet 5.5 they would have been cut off mid-reasoning. `llm.py` now applies the same rule, with a ceiling of 64,000 tokens a call, and logs the scale.

**13. The standard for “anticipated” (13 October).** Reading the first novelty reports, the custodian raised a concern: many successful philosophy papers develop ideas first mentioned elsewhere, so a single mention in an article should not count as anticipation. The prompts did not draw that line. They defined anticipation as “someone already argued this, or argued something that entails it”, with no requirement of extent; most verdicts rested on abstracts and search snippets, from which extent cannot be judged; and every stage could only narrow a thesis, never credit a precedent. The custodian set this standard, which is now one shared text in `llm.py` used by every script that judges priority:

> A prior work anticipates a claim only if it discusses the claim **extensively** and **either** its author asserts or endorses it, **or** its argument conclusively closes the claim off.

Anything short of that is a **PRECEDENT**, graded as *passing* (raised without development), *entertained* (explored but neither endorsed nor closed off) or *framework* (a broader view of which the claim would be an application). A precedent is credited, not conceded. A work that argues against the claim without closing it off is a rival to answer. Each finding now records what the checker actually saw (full text, abstract, snippet or a second-hand report), and any verdict of anticipation resting on less than the full text is marked provisional.

The scripts changed were `lit_check.py` (novelty and encyclopedia passes, plus a “credit” list), `restate.py` (narrows only for anticipation in this sense; full-text reading notes, given with a new `--notes` option, override search findings), `source_reader.py` (applies the standard to full texts, and is told to request every work flagged as anticipating so the flag can be settled), `pick.py` (for Run B), `review_round.py` (the adjudicator rules an anticipation MUST ADDRESS only when the standard is met; an uncredited precedent is a scholarship point) and `draft.py` (credits precedents, concedes only when the standard is met). The order of Step 3 also changed: **sources are now read before the restatement**, so that whether a thesis is anticipated is judged from full texts rather than snippets. The same change strips stray citation markup from the novelty reports.

*Evidence that it mattered.* The novelty check was rerun on theses 12, 15 and 27, which had been dropped mainly for anticipation. The searches found largely the same sources; only the classification changed. Butlin & Viebahn and Williams & Bayne against thesis 12 moved from anticipated (damage 4) to entertained precedents, both provisional; Arora against 15 from anticipated (4) to a rival (2); Barandiaran & Almendros and Attah against 27 from anticipated (4) to supporting and adjacent. Across all sixteen theses, only two findings still met the standard, both provisional: Williams & Bayne on one half of thesis 21, and McDonald on thesis 31.

**14. Several novelty checks feeding one source list (13 October).** The first source list for thesis 1 was built from the second novelty check alone and omitted Chalmers, whom the first check had named as a rival the thesis must answer. Searches are not deterministic, so each check had found sources the other missed. `source_reader.py --needs` now takes `--lit` more than once and tells the model to consider every source any check found. The rerun list added Chalmers and Mácha and dropped several narrower empirical papers.

**15. Tools for a cross-family priority check (13 October).** The first recipe had a step that version 2 omitted: giving each shortlisted thesis to a model from a different family (ChatGPT) to ask whether it had been argued before. Two options were built: `lit_check.py --priority-prompt` prints and saves the exact prompt for a thesis, including the anticipation standard, so that the text pasted into ChatGPT comes from a script and is recorded; and `source_reader.py --external` adds a saved reply to the source-list request, as leads to confirm rather than facts. Prompts were generated for the six theses then ranked highest. **The custodian then decided to skip this step for Run A** (19 October). The prompts remain in `priority_N/` as a record that the step was prepared and not run.

**16. Output allowance and streaming in the outline deviser (19 October).** `outline_deviser.py` keeps its own API code, and its default allowance (4,096 × 3 = 12,288 tokens) was too small: on Sonnet 5.5 all six outline calls spent the whole allowance reasoning and returned no text. Each outline now has 48,000 tokens and the comparison of outlines 24,000, with a ceiling of 64,000; calls are streamed, which the larger allowances require.

**Deployment errors recorded.** The file-transfer step twice more delivered an intermediate version of a script: `source_reader.py` on 13 October and `outline_deviser.py` on 19 October. Both times the checksum comparison caught it before the script was used, and a fresh copy from a new staging folder arrived intact. This has now happened three times in Run A.

**Defects found and not yet fixed.** None affected a result. (a) `restate.py` reported its result as UNCHANGED although it had added a clarifying gloss to the thesis. (b) The attribution check’s existence test treats every quoted phrase in an outline as a work’s title, so its list of “citations that do not resolve” is mostly quotations; all quotations had already been checked against the PDFs. (c) Three of the thirty attribution checks failed with a temperature refusal that the script misreported as a search-tool failure. Each attribution they covered was either checked elsewhere in the same run or lies in an outline not chosen.

# Results

## Novelty and the shortlist

The first check (11 October) rested almost entirely on abstracts and snippets. Reading its reports, the custodian kept or dropped each thesis, with meta-level advice, and fixed a rank order for the keepers before any source reading, so that a thesis eliminated later would be replaced by rule rather than fresh judgment.

| Thesis | After the first check (11–13 Oct) | After the rerun under the new standard (13 Oct)                 |
| ------ | --------------------------------- | --------------------------------------------------------------- |
| 1      | Keep, ranked 1st                  | Keep, 1st. **Chosen**                                           |
| 21     | Keep, 2nd                         | Keep, 2nd                                                       |
| 12     | Dropped (anticipated)             | Keep, 3rd                                                       |
| 3      | Keep, 3rd                         | Keep, 4th                                                       |
| 13     | Keep, 4th                         | Keep, 5th                                                       |
| 37     | Keep, 6th                         | Keep, 6th                                                       |
| 31     | Keep, 5th                         | Reserve, 1st (McDonald still meets the standard, provisionally) |
| 20     | Reserve                           | Reserve, 2nd                                                    |
| 6      | Reserve                           | Reserve, 3rd                                                    |
| 9      | Reserve                           | Reserve, 4th                                                    |
| 46     | Reserve (close relative of 1)     | Reserve, 5th                                                    |
| 15     | Dropped (anticipated)             | Reserve, 6th                                                    |
| 27     | Dropped (anticipated)             | Reserve, 7th                                                    |
| 8      | Dropped                           | Reserve, 8th                                                    |
| 7      | Dropped (narrowed to one case)    | Dropped                                                         |
| 22     | Dropped (narrowed to one author)  | Dropped                                                         |

The rule for elimination at the source stage, fixed in advance: move to the next thesis if a work read in full meets the anticipation standard for the central claim.

## Thesis 1

The thesis as checked (Step 2’s surviving version):

> If chatbot outputs are assertions, hallucination, sycophancy and sanction are best assessed at the level of the trained policy, and resampling inconsistency is not evidence of insincerity. Whether the asserted content is the policy’s calibrated ‘p, with confidence c’ is not established.

**Sources.** The model listed twelve works (seven essential, five useful); the custodian fetched all twelve and nothing else. Read in full, **none met the anticipation standard and none was even a precedent.** Butlin & Viebahn, the source most feared, is adjacent: they deny that current chatbot outputs are assertions but never discuss assessment at the level of the policy. Three works are rivals to answer: Chalmers (the interlocutor is a thread or virtual instance, not the model), Massaguer Gómez (assertion without an asserter) and Shanahan, McDonell & Reynolds (variation across regenerations shows that nothing was committed to). Four empirical papers (Kalai et al.; Sharma et al.; Manakul, Liusie & Gales; Xiong et al.) support the thesis’s framing. The meta level checked all 56 quotations in the notes against the PDFs; every one appears verbatim.

**Restatement.** Given the readings, the model returned the thesis UNCHANGED in substance, adding a gloss on “the trained policy”: “(the output distribution and its calibration), not the sampled string”. It also named the thesis’s target (the shared assumption that the unit of assertion and sanction is the single output or the deploying humans) and listed the works to credit. The custodian chose this restated version over the original.

**Outlines.** Six outlines were generated in isolation. All six grant the antecedent and separate the level of assessment from the identity of the speaker; they differ in what carries the main load, in how rival units of assessment are handled, and in where the “p, with confidence c” clause goes. The free audit flagged a thin load-bearing section in outlines 1, 2 and 3. The attribution check found one distortion each in outlines 0, 2, 3, 4 and 5 and three in outline 1. In outlines 0 and 4 the distortion stated a rival’s results without their conditions (Lin, Hilton & Evans; Kadavath et al.); in outline 5 it attributed a view to Williams & Bayne and Mácha that they do not hold, in the outline’s load-bearing section.

The custodian chose **outline 0**, “The Unit of Assertion Failure”, after reworking both 0 and 4 to compare them. The rework replaced only the passages that name other authors. Its sections: §1 Introduction; §2 Same string, different policy: the bearer of hallucination and sycophancy; §3 Sanction operates on the distribution, not the string or the deployer; §4 Why resampling disagreement is not evidence of insincerity; §5 What the outputs say is open, and the verdicts do not wait on it; §6 Conclusion.

Outline 0’s final section relies on Lin, Hilton & Evans and Kadavath et al., which had not been on the reading list. The custodian fetched both, and the model read them in full: both are adjacent, supplying empirical groundwork. The two sets of notes were joined into one file for drafting.

# Findings about the method

1.  **The standard decided more than the search did.** Rerunning the novelty check under an explicit standard left the sources largely the same and changed the verdicts. Before any argument about priority, a pipeline needs to say what anticipation is.
2.  **A search cannot usually establish anticipation.** Under a standard that requires extent and endorsement, a check that sees abstracts and snippets can rarely confirm anticipation; after the rerun, only two of sixteen theses had any finding that met it, both provisional. The real filter is full-text reading, so it must come before any narrowing.
3.  **Independent searches find different literatures.** Two runs of the same check on the same thesis named different sources. A reading list should draw on all of them.
4.  **Every stage that keeps its own model-handling code must be updated when the model changes.** The Step 2 fixes reached three scripts and missed two code paths, one of which failed in its first live run.
5.  **Checksums on delivery are not optional.** They caught two more stale deliveries.
6.  **The attribution check earns its cost.** It separated outlines that misstated a rival’s results (a scholarship error that leaves the paper answering a stronger opponent) from one that aimed its main argument at a view nobody holds.
7.  **Survival still selects against ambition, at a new stage.** Under the first standard the novelty check pushed theses toward replies to a single author. Theses 7 and 22, dropped for that reason, are the two that remain dropped.

# Human involvement in Step 3

## At the object level, the custodian

  - typed commands and chose their settings;
  - read the novelty reports, source notes, restatement, outlines and attribution reports;
  - kept, dropped and ranked theses by index (11–13 October), and revised the order once after the standard changed (13 October);
  - chose the restated version of thesis 1 over the original;
  - fetched exactly the fourteen works the models listed (twelve from the source list, two named by the chosen outline), and no others; where a listed link pointed to a catalogue record, he fetched an open-access copy of the same work;
  - ran the rework on outlines 0 and 4, and chose outline 0 by number;
  - set the anticipation standard (change 13), a methodological instruction that says what counts as prior work and contains no claim about the thesis’s subject;
  - decided to skip the cross-family priority check.

He sent no text to any object-level model in Step 3.

## At the meta level

  - Claude recommended, for each thesis, whether to keep, reserve or drop it, and proposed rank orders. The custodian’s decisions differed in places: he initially favoured keeping 9 and dropping 13 and 21, and adopted Claude’s view on those three; he dropped 8 before Claude had read its report; Claude then agreed, ranking it below 6.
  - After the rerun, Claude proposed the revised order; on the custodian’s question, it moved 12 from fifth to third. The custodian adopted that order.
  - Claude recommended the restated version, and ranked the outlines 5, 0, 4. The custodian preferred 0 and 4. After the attribution check Claude withdrew its preference for 5, and the custodian chose 0, for what he judged the more elegant argument. His reasons for choosing were given at the meta level and did not cross.
  - Claude recommended fetching Lin, Hilton & Evans and Kadavath et al., as works the chosen outline relied on, and joined the two notes files into one (a mechanical step).

*Disclosure.* As in Step 2, the meta-level Claude has memory of the custodian’s research and of the first paper. Its recommendations are AI contributions from a conversation not isolated as object-level calls are, so they are reported here as part of the selection process.

# Carried into Step 4

  - **Thesis:** `Step 3 - Novelty/restate_1/raw.json`, index 0.
  - **Outline:** `Step 3 - Novelty/outlines_1b_rework0/raw.json`, outline 0.
  - **Notes:** `Step 3 - Novelty/notes_1_all.md`, fourteen works read in full.
  - **To verify before submission:** that Williams & Bayne use inconsistency across outputs as a mark against full assertion, which the outline targets but their manuscript does not develop; and the page references in the notes.
  - **To watch at the drafting gate:** where the “p, with confidence c” clause appears; the custodian’s preference is that a scope limit sits near the end of a paper. A misplaced clause may be met by choosing another draft or with the flag “The scope caveat comes too early in the paper.”
  - **Untested live:** `draft.py`, `review_round.py`.

# Files

| Folder (in `Step 3 - Novelty`)               | Contents                                                      |
| -------------------------------------------- | ------------------------------------------------------------- |
| `lit_N`                                      | Novelty check, first standard, for each of the sixteen theses |
| `lit_N_v2`                                   | Novelty check under the anticipation standard                 |
| `priority_N`                                 | Prompts for the cross-family check (not run)                  |
| `needs_1`, `needs_1b`                        | Source lists for thesis 1; `needs_1b` was used                |
| `Sources_1`, `Sources_1x`                    | The fourteen PDFs fetched                                     |
| `notes_1`, `notes_1x`, `notes_1_all.md`      | Full-text reading notes, and the joined file                  |
| `restate_1`                                  | The restatement                                               |
| `outlines_1`                                 | The failed outline run                                        |
| `outlines_1b`                                | The six outlines                                              |
| `attr_1`                                     | The attribution check                                         |
| `outlines_1b_rework0`, `outlines_1b_rework4` | The reworked outlines; 0 was chosen                           |
