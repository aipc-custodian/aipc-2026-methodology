# Supporting materials for two essays submitted to the AI Philosophy Competition 2026

The essays:

- **Paper 1:** *Common Ground as Accidental Convergence* (`paper1/essay.md`)
- **Paper 2:** *The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy* (`paper2/essay.md`)

The methodology report, which accompanies each submission, cites the files here. The person who ran the process is called **the custodian** throughout.

## Where to start

Each step of Paper 2 has its own report, giving what was run, every change to the scaffold and why, spending and dates, and the human involvement at each level:

| Step | Report |
|------|--------|
| 1 Topic | `paper2/step1_topic/Step 1 Report - Topic.md` |
| 2 Thesis Forge | `paper2/step2_forge/Step 2 Report - Thesis Forge.md` |
| 3 Novelty, sources, outlines | `paper2/step3_novelty/Step 3 Report - Novelty, Sources and Outlines.md` |
| 4 Drafting and presentation guide | `paper2/step4_drafts/Step 4 Report - Drafting and Presentation Guide.md` |
| 5 Review and revision | `paper2/step5_review/Step 5 Report - Review and Revision.md` |
| 6 Final checks | `paper2/step6_final/Step 6 Report - Final Checks and Submission.md` |

Paper 1 was the design run, in which the pipeline was built. Its report is `paper1/methodology_report_paper1.md`, and there are design reports for each stage in `paper1/design/`.

## Layout

```
paper1/            essay, change log, methodology report, design reports, run outputs, scripts as then used
paper2/
  essay.md         the submitted text
  step1_topic/     topic chats (ChatGPT, Gemini, Claude) and the Forge's input files
  step2_forge/     Thesis Forge runs: every call in calls.jsonl, settings in run_log.json
  step3_novelty/   novelty checks, source lists, reading notes, restatement, outlines, attribution checks
  step4_drafts/    three drafts and their ranking
  step5_review/    outside referee reports (verbatim), Claude referee reports, rulings, revisions,
                   the calibration run, the custodian's flags and pass
  step6_final/     mechanical changes, quotation check, typesetting and repository scripts
  style_guide/     the presentation guide and how it was built
scripts/           the pipeline (clean_run) as it stood at submission
recipe/            the recipe for the runs, with dated earlier versions
```

Every object-level API call is recorded in full in the `calls.jsonl` of its run folder. `run_log.json` gives the script's checksum, the command line, every setting and prompt, and token counts.

## What is not here, and why

- **The published works the models read** (Step 3 sources, the presentation-guide sample, the calibration article). They are copyrighted; the step reports cite each one. The files that contain the calibration article's full text are left out for the same reason.
- **The custodian's private notes**, and a file of personal details.
- **The meta-level conversation** in which the pipeline was managed. It ran with the custodian's personal memory on. Its recommendations are disclosed in every step report.

Local file paths in logs have been replaced with `<project>` and `<user>`.
