# Thesis Forge: Methodology Report

## Overview

The essay *Common Ground as Accidental Convergence* was produced by a three-stage pipeline. Stage one generates and ranks many candidate theses. Stage two turns one thesis into an argument structure and checks it against published work. Stage three drafts the paper and revises it under review from other models.

Stages one and two are scripts. Stage three was run by hand in a single conversation. A human custodian chose the topic area, selected among machine outputs at each gate, and carried reviews between models. At stage two the custodian also made four changes of content. These are set out under Human involvement.

One principle governs the design, and it was learned from transcripts, not planned: variance is the product. Candidates are generated in isolation at high temperature. Dialogue between models is used only to put pressure on a fixed object. Verdicts are reported as fields beside each candidate and never used to discard it.

1.  **Thesis Forge.** Input: a topic area and two anchor readings. Output: candidate theses ranked on promise and on residual damage.

2.  **Retrieval Check and Outline Deviser.** Input: one selected thesis. Output: several independent outlines, each audited, plus novelty and attribution reports.

3.  **Drafting and cross-model revision.** Input: one outline. Output: the submitted essay, 5,958 words excluding bibliography, ten sections, twenty-eight references.

## Stage one: the Thesis Forge

The Forge does not write. It produces theses and ranks them on two independent axes so that a human can choose which to develop.

1.  **Generation.** N model instances produce candidate theses at high temperature, blind to one another. Each is prompted to look for a specific kind of move: an undrawn distinction, a counterexample to a shared premise, a reframing, an instability, or an unnoticed commitment.

2.  **Appraisal.** A separate instance scores each thesis for promise, comparatively and in batches. It has seen no objections.

3.  **Clustering.** Near-duplicates are merged. The highest-scoring member is kept and the others are recorded on it.

4.  **Attack.** The highest-promise theses each face three roles. A Killer is assigned one specific line of objection. A Defender must mount a real defence before conceding. An Adjudicator scores each objection for damage and rules whether it was met or merely absorbed.

5.  **Report.** Theses are ranked by promise and by residual damage, meaning the strength of the strongest unanswered objection.

The Forge was rebuilt about a dozen times against its own output. Three findings shaped it.

  - **Dialogue destroys variance.** The project began from two instances conversing freely. Such loops converge, because identical agents mirror each other. Generation therefore uses no conversation at all.

  - **Survival selects against ambition.** In early runs the surviving theses were the least promising. Modest claims are small targets. Promise and survival are therefore reported separately. A further category collects high-promise theses that failed on one locatable flaw, with the narrower surviving version.

  - **Any permitted escape is taken.** Free to choose its objection, the Killer always chose equivocation. Licensed to decline inapplicable objections, it declined ten of twelve. Given a misattribution check, it found misattribution in nineteen of twenty-one. The design now constrains by assignment and rotation, not instruction. An unattacked thesis counts as untested, not as surviving.

Yield is variable. Three runs on one question produced four, one, and zero theses meeting both criteria.

## Stage two: Retrieval Check and Outline Deviser

Stage two has two components. Neither ranks or eliminates anything.

**The Outline Deviser** writes several outlines of the paper the thesis needs. They are written at high temperature and blind to one another, with no adversarial stage. Six outlines do not exceed one reader's attention, so no adjudicator stands between the reader and the documents. Seven requirements are imposed as conditions on production:

  - every section states the claim it establishes and what would refute it, naming a position someone actually holds;

  - every section states what it takes as given, and from where;

  - no section exists that nothing downstream needs;

  - the argument reaches the thesis, by deduction, strong induction or abduction;

  - the outline locates its own widest inferential gap;

  - the most-depended-upon claim is defended in proportion;

  - an introduction and conclusion are required and exempt from the above.

Each outline then passes a mechanical audit. Each section must reproduce verbatim the claim it takes from an earlier section, so upward drift in paraphrase is detectable by string comparison. A divergence pass reports which structural moves all outlines share and which they split on.

**The Retrieval Check** is the pipeline's only contact with published text. It runs twice.

  - *Novelty*, on shortlisted theses. It searches the live web and must search adjacent empirical literatures. A search that never leaves philosophy is reported as failed. It then selects entries from the Stanford Encyclopedia's own contents index and reads them in full. Findings are classed as anticipating, contradicting, supporting or adjacent. It must state what it searched for and did not find.

  - *Attribution*, on the finished outline. Each cited work is checked for existence against a bibliographic index, with no model involved. A model then judges whether each named person holds the view ascribed to them.

Four findings shaped this stage.

  - **The adversarial architecture does not transfer.** A thesis can be attacked. An outline is a structure, and the stage-one objections are category mistakes against it.

  - **Stated parameters become targets.** Told to write five to nine sections, the system wrote seven in ten of twelve runs. With the range removed, counts ran from four to eight.

  - **Isolation prevents mirroring, not convergence.** Six blind outlines produced one argument with its sections permuted. All had been handed the same generating sketch.

  - **Recall cannot detect priority.** A thesis at maximum promise with no unanswered objection lost its empirical claim to an existing psychological literature and its structural move to a 2015 paper. Ordinary search found both in minutes. On the run reported here, retrieval discarded three theses for prior publication. Three of seven named positions in the outline failed attribution and were replaced.

## Stage three: drafting and cross-model revision

Stage three is a procedure, not a component. One instance of Claude Opus 5.5 drafted the paper from the stage-two outline, one section at a time. Two instructions accompanied the outline: write in the register of a named published article, and vary what paragraphs do. The drafter made one retrieval while drafting. Every other claim about the literature came from recall. The first draft ran to about 5,800 words.

Three review rounds followed. Each used the same loop.

1.  The custodian gave the full draft to a reviewer model with one generic prompt: is the paper good, novel and publishable, and where?

2.  The custodian passed the review to the drafter verbatim, with a generic instruction to address the concerns it judged legitimate.

3.  The drafter sorted concerns into accepted and resisted, verified every bibliographic claim at issue by web search, and proposed a plan.

4.  The custodian approved the plan without modification.

5.  The drafter revised, then cut the text back under 6,000 words.

Rounds one and two used Claude Fable. Round three used ChatGPT at medium reasoning effort, added on the drafter's advice that a shared model family was a limitation.

Six findings came out of the run.

  - **An outside reviewer sees what the drafter built around.** The first central case turned on the word "officially", which appealed to an institution and not to the record between speakers. The drafter had argued from it for two pages. The reviewer proposed the minimal pair that replaced it.

  - **A reviewer is a second recall, not a check.** The first reviewer misdated a canonical example, failed to confirm a real 2024 article, and miscounted the word limit. Each error was caught only because the drafter verified before acting.

  - **Fixes relocate problems.** Each repair answered the objection in front of it and opened the place where the next one landed.

  - **Questions did more than objections.** The first reviewer's two closing questions produced the paper's two largest structural changes. Its concrete reframing was declined.

  - **Confirming a reference is not reading it.** The cross-family reviewer, working with search, found two 2025 papers that anticipate part of the thesis. Neither Claude model had raised them. The drafter had retrieved one of them the day before, to check a quotation, and used it for nothing else. The find narrowed what the paper claims as new.

  - **Critique is additive.** Every round pushed the paper over the limit: to 6,520, 6,294 and about 6,180 words. Cutting restatement was the only point at which anything was removed.

## Human involvement

The custodian wrote no passage of the essay and supplied no case, objection or reply. The custodian did change the thesis and the outline at stage two. Those four changes are contributions of content, and the essay inherits them.

| Stage | What the custodian did                                                                                     | Kind                |
| ----- | ---------------------------------------------------------------------------------------------------------- | ------------------- |
| 1     | Chose the topic area, within the custodian's own specialism, and two anchor readings                       | Task specification  |
| 1     | Selected one thesis from the ranked report                                                                 | Selection           |
| 1     | On an earlier run, caught a factual error about a named theorist's position that no component could detect | Scholarship check   |
| 2     | Discarded three theses after findings of prior publication                                                 | Selection           |
| 2     | Replaced three named positions after attribution verdicts                                                  | Scholarship check   |
| 2     | Merged two of the six outlines by hand after a thin-load-bearer warning                                    | Content (structure) |
| 2     | Observed that one of the two mechanisms had no conversational role and would read as trivial               | Content             |
| 2     | Promoted an aside about content moving between mechanisms into a section                                   | Content             |
| 2     | Broadened that mechanism's remit beyond the single case used to isolate it                                 | Content             |
| 2     | Rewrote the thesis to match                                                                                | Content             |
| 3     | Supplied the outline, named a model for register, asked for varied paragraph function                      | Generic instruction |
| 3     | Chose three reviewers and gave each the same generic prompt                                                | Scaffold            |
| 3     | Relayed each review verbatim and approved the drafter's plan unmodified                                    | Scaffold            |
| 3     | Ruled out running the experiment the paper proposes                                                        | Resource decision   |

Origination within stage three is as follows. Every case in the final text is the drafter's, except the minimal-pair design of the report card, which is the first reviewer's. Every reply, every cut, the declined reframings, the interventionist criterion for "mechanism", and the disagreements with Bary are the drafter's. The objections and the pointers to missed literature are the reviewers'. The cross-family reviewer also contributed the "projection of correlated variables" framing and the proposed experimental measure.

The main choice the custodian made at stage three was to leave to the drafter the judgment of which criticisms were legitimate.

## Known limitations

  - **Recall stands in for reading.** Novelty and attribution judgments are hypotheses until retrieved. Retrieval shows that something has been argued; it cannot show that nothing has. Much of the literature is paywalled.

  - **Partial reading of key sources.** Simons was read only in a 2022 draft. The reading of Camp as nesting the record within common ground rests on her abstract and secondary summaries. The claim about demonstratives goes beyond the evidence in Tonhauser and colleagues.

  - **Variance was not applied at stage three.** One drafter wrote one draft and revised it serially. The planned gate of selection among finished drafts had a single candidate.

  - **The drafter judged criticism of its own work.** No independent adjudicator ruled on which concerns were legitimate, including the decisions to decline two reviewers' central reframings.

  - **Two of three reviewers shared the drafter's model family.** The one outside reviewer found two directly relevant papers the others missed, so the concern is real.

  - **The Deviser yields candidates, not a structure.** The outline that went forward was assembled by hand and would not otherwise have existed.

  - **Residual damage is ambiguous.** It cannot tell a thesis that withstood heavy objection from one that drew only weak objection.

  - **Stage three is reproducible as a procedure, not as code.** The proposed experiment is untested.

## To supply before submission

  - [ ] Models and versions used in stages one and two, and the role of each

  - [ ] Values of N, temperatures, and counts of theses and outlines generated on the reported run

  - [ ] Prompts, system instructions and scripts for all three components, as appendices

  - [ ] The Forge's original thesis text beside the custodian's revised thesis

  - [ ] Chat logs for the stage-two review conversation and the stage-three run

  - [ ] Approximate human time, machine time, token usage and cost

  - [ ] Whether memory or earlier conversations were available to the drafter and reviewers
