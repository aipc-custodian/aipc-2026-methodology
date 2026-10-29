# Run A (Paper 2), Step 6: Final Checks and Submission

## Summary

Step 6 prepared both essays for submission. It made only mechanical changes and ran checks. No model generated or judged philosophy in this step, and no API calls were made.

For Paper 2 the step:

- corrected one author’s name and one page reference, and added a DOI;
- matched every quotation from a source held to that source, and verified the rest online or by the custodian;
- checked every page reference to a source held;
- checked length, anonymity and the absence of prompt injection;
- typeset the essay as a PDF.

For Paper 1 it removed a byline, checked length and anonymity, and typeset the essay. Paper 1’s quotations were not checked.

The step also assembled the public repository of supporting materials and drafted the methodology report, which the custodian then edited.

Dates: 27–29 October 2026. API cost: none. Custodian time: about 3 hours (his estimate).

## Paper 2

## Mechanical changes

Each change is logged in `step6_final/changes.md`, from a starting text identical to `step5_review/custodian_pass/revised.md`.

1.  **An author’s name.** Gómez (2026) became Massaguer Gómez (2026), in three citations and the reference list, which was re-sorted. This was verified from the article’s first page.
2.  **A page reference.** The thermometer quotation from Butlin & Viebahn was cited to p. 978. It is on p. 979 of the source, and the citation was corrected.
3.  **A DOI.** The DOI and the 2024 online date were added to Williams & Bayne (2026), verified by the custodian from the arXiv record.

## Checks

- **Quotations.** A script (`step6_final/quotecheck.py`) extracted every quotation and searched for it in the text of the fourteen sources read in Step 3. All 23 quotations from those sources match exactly. The others were checked as follows:
  - two from Evans et al. (2021) were verified against the arXiv text;
  - one from Kalai et al. (2026) was verified by the custodian against the published abstract;
  - one italicisation in Butlin & Viebahn was confirmed by the custodian against the source.

  The remaining unmatched strings are the paper’s own examples and terms. See `step6_final/quotecheck_report.md`.
- **Page references.** Every page reference to Butlin & Viebahn, Chalmers, Williams & Bayne, Massaguer Gómez and Mácha was checked against the source PDF.
- **Attributions.** The claims about Williams & Bayne that all three drafters had flagged as unverified at Step 4 are no longer in the paper. The one remaining attribution to them, that for typical chatbot output there is no clear candidate for the principal, matches their §4.1. The model-based attribution check was therefore not run.
- **Originality.** One referee had twice noted an overlap with the *Encyclopedia of the Philosophy of AI* entry “AI and Assertion”. The custodian compared the two and judged them substantially different.
- **Length:**
  - 5,398 words excluding references, footnotes included, by the pipeline’s counter;
  - 5,410 by a plain whitespace count;
  - 5,112 without the footnotes.
- **Anonymity and injection.** There is no name, affiliation, acknowledgement or self-citation, and nothing addressed to a reader or screener.

## Paper 1

- **Version.** The final version (v4, 2 October) was converted to Markdown.
- **One change.** The byline under the title (date and author name) was removed. See `paper1/changes.md`.
- **Length:** 5,975 words excluding references by the pipeline’s counter, and 5,962 by pandoc.
- **Not checked.** Paper 1’s quotations and page references were not verified against their sources. The custodian decided not to do this, and the methodology report says so.

## Typesetting

Both essays were typeset with pandoc and XeLaTeX:

- TeX Gyre Pagella at 11 point, with real footnotes and hanging-indent references;
- no author line, and an empty author field in the PDF metadata.

A preparation script (`step6_final/pdf_build/prep.py`) does only what typesetting needs. It turns Unicode subscript characters into subscript markup, moves the abstract into the title block and formats the references. It changes no words.

## The repository

The supporting materials were assembled by a script (`step6_final/build_repo.py`) that:

- copies the files on an allowlist and converts Word reports to Markdown;
- replaces local file paths;
- scans every file for names, e-mail addresses and API keys.

It left out:

- the copyrighted sources the models read, and their extracted texts;
- the published article used in the calibration run, and the run files that contain its full text;
- a notes file containing an API key;
- reading copies.

The scan found the author’s name in a byline in one Paper 1 design report and in the wording of Paper 1’s change log. Both were removed. A file of memory-off instructions that contained personal details was left out entirely. The repository is published from an account with no name attached, so that a search for an essay’s title does not identify its author. For the same reason, the methodology report, which names the custodian, is submitted through OpenReview and is not in the repository.

## The methodology report

The meta-level Claude drafted the methodology report from the step reports and run logs. The custodian then read it and revised it: he added detail, corrected emphasis and supplied the facts only he had, including Paper 1’s register model, its cost and time, and his time for each step. Paper 1 is entered under the competition’s “AI-led with human guidance” category and Paper 2 under “AI-driven”.

## Human involvement in Step 6

**The custodian:**

- confirmed the Kalai et al. quotation and the Butlin & Viebahn italicisation;
- found the Williams & Bayne DOI;
- compared the essay with the encyclopedia entry;
- chose the final version of Paper 1;
- decided not to check Paper 1’s quotations;
- chose the competition categories for both papers;
- edited the methodology report;
- published the repository.

**The meta-level Claude:**

- made the mechanical changes;
- wrote and ran the quotation, page-reference and length checks;
- typeset the essays;
- assembled and scanned the repository;
- drafted the methodology report and this report.

No text of either essay was changed except as listed above.
