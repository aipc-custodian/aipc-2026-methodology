I'll check the literature before writing the report.# Referee Report

**Manuscript:** "The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy"

**Recommendation:** Major revisions. Not publishable in its current form; a revised version could be publishable in a specialised venue (Philosophy & Technology, Inquiry, Ergo, Synthese AI-ethics stream).

---

## 1. Summary

The paper grants, for the sake of argument, that chatbot outputs are assertions, and asks what object bears assertion's defects. Its answer is the trained policy π(·|x). The core instrument is a "same-string/different-policy" test (§2): fix string and context, vary the policy, and hallucination/sycophancy verdicts flip. §3 argues that sanction reaches chatbot assertion only by reshaping the distribution, that string-level reward regimes are self-defeating, and that there is a thin policy-level analogue of Butlin & Viebahn's condition (iii). §4 argues that resampling disagreement has a likelihood ratio of ≈1 for insincerity. §5 argues the content question (bare p / p-with-verbalised-c / p-with-calibrated-c) is open but the verdicts are robust across readings.

The paper is clearly written, well organised, and engages the current literature on chatbot assertion conscientiously. The negative half of (L) is correct and the Cases are well chosen. But the genuinely new claims (§3.2, §3.3, §4) are the least well argued, and the central move is less novel than claimed once one looks outside the chatbot-assertion debate.

---

## 2. Objections, ranked by seriousness

### Objection 1 (most serious): §3.3 does not close the gap it identifies, and the paper's own foil is Butlin & Viebahn's example.

The paper's thermostat case ("recalibrated by an engineer") is the easy case. Butlin & Viebahn's actual foil is a *sophisticated thermometer*: one point in favour of their view is that it provides the correct result for the cases of the sophisticated thermometer. While we can adapt our credibility in the thermometer and there is a sense in which it is sensitive to our credibility ratings, there is clearly no sense in which it is bad or undesirable for the thermometer if we reduce our credibility. The second reply in §3.3 — that credibility loss "lowers the policy's score on that standard" and that "policies that lose it are selected against" — applies word-for-word to any gradient-trained instrument with a loss function, including a self-calibrating thermometer. So the reply does not "separate sanction from repair"; it relabels repair. The appeal to "the objective that individuates what the policy is for" is a teleofunctional claim that needs an argument, not a sentence.

The first reply (either a policy-level analogue of (iii) holds, or (iii) is dispensable) is logically valid but makes §3's headline conclusion very weak: it is conditional on theories that already reject B&V, and the paper offers no independent reason to accept any such theory. The honest statement of the result is: *if* some non-B&V theory of assertion makes chatbots asserters, *then* the only candidate for the sanctioned party is the policy. That is much less than "the party sanctioned ... [is] the trained policy."

A related problem: the "lineage sense" in (S4) is undefined and sits badly with the paper's own definition of a policy as a conditional distribution. If πₜ₊₁ ≠ πₜ, then the thing that asserted is never the thing that is sanctioned. Deployed weights are frozen; no deployment-time assertion by πₜ is ever met with a sanction πₜ is sensitive to. The paper leans on B&V's remark about training-time sensitivity, but B&V offer that as a conjecture, and it does not address the type/token problem the paper has created for itself.

### Objection 2: The hallucination criterion in §2.2 is internally unstable — "force vs. mass" and "calibration" come apart, and Case 2's P₃ shows it.

The paper gives two characterisations of hallucination that it treats as equivalent: (a) a mismatch between assertoric force and *the policy's own pooled mass*; (b) miscalibration, defined as a c-fraction-true relation over a prompt distribution. These are different properties. (a) is internal to the policy and needs no truth values; (b) is an external reliability property that is nothing but truth frequencies. A policy can satisfy (a) perfectly (asserts flatly only at mass 0.95) and be badly calibrated (its 0.95-mass claims are true 40% of the time).

P₃ in Case 2 is exactly such a case: high mass on a falsehood because the corpus consistently misreported it. The paper calls this "warranted, given its evidence." But corpus frequency is not evidence; it is the thing a policy's mass tracks whether or not it is evidence. Lin, Hilton & Evans's own TruthfulQA (2021) calls high-mass falsehoods of this kind "imitative falsehoods" and treats them as the paradigm of what needs fixing. The paper needs to either (i) argue that corpus frequency confers warrant, which is a substantial and contentious epistemological thesis, or (ii) drop P₃ and accept that calibration (b), not mass-matching (a), is the criterion — in which case "the policy's own information" drops out and the view is simply externalist reliabilism (see Objection 4).

### Objection 3: The positive half of (L) is under-argued; "fixes the verdict" ≠ "bears the failure."

The test establishes only the negative claim (string doesn't fix the verdict). §2.4 rules out architecture, and §2.5 argues the choice of speaker is irrelevant. But the paper never distinguishes three things: (i) what the verdict *supervenes on*, (ii) what the *unit of assessment* is, and (iii) what *bears the failure* (the thing that fails, is sanctioned, etc.). Consider the human analogue: whether my assertion is unwarranted is fixed by my evidential state, not by the sentence; nobody concludes that my evidential state is the bearer of the failure. I am. §2.5 actually concedes this structure — "Grant that the thread is the speaker ... the thread's assertion is hallucinatory because of the conditional distribution" — and that concession turns the positive half of (L) into a supervenience claim, which is nearly trivial, rather than a bearer claim, which is what the title and §3 need.

Two further awkward consequences follow from the paper's own definition of "policy" as weights-plus-decoding-settings: (a) the same weights at temperature 0 and temperature 1 are *different* bearers of assertion failure; (b) at temperature 0 there is no resampling variation at all, so §4's E never occurs and "pooled mass" must be read off logits rather than samples — which the paper should say, since it changes what the "evidence" in §4 is.

### Objection 4: The central move is a transposition of process reliabilism, and the paper does not say so.

Case 1 is the lucky-guess case; Case 2 is the reliable-process-with-false-output case. These are the standard motivations for Goldman-style process reliabilism (same belief, different process → different justification verdict). The paper cites no epistemology. A recent arXiv paper applying warrant to LLM outputs makes the connection explicitly: process-oriented accounts emphasize that epistemic standing cannot be inferred from the correctness of an outcome alone. Goldman (1979) argues that justification depends in part on whether a belief is produced by a process that tends to generate true rather than false beliefs ... Applied to LLM recommendations, this motivates examining the behavior of the recommendation-generating process rather than treating observed correctness as sufficient evidence of warrant. The paper's test is this point with "process" replaced by "policy." That is a fine thing to do, but the novelty claim in §1 needs rewriting, and the connection should be made explicit since it would also help with Objection 2 (reliabilism is externalist; the paper's "policy's own information" talk is internalist).

### Objection 5: §4's likelihood-ratio claim is asserted, not derived, and the paper ignores the Frankfurtian alternative.

"Insincerity carries no particular prediction about E" does not entail P(E|insincere) ≈ P(E|sincere). If the insincere hypothesis is a mixture over consistent-liar and variable-liar sub-hypotheses, its likelihood is a weighted average that could be above or below the sincere likelihood. No model is given. The claim should be weakened to "E is not strong evidence either way," which is defensible but less striking.

More importantly, §4.3 dismisses the thin Moorean test by saying it "turns careless speakers into liars." But the thin test says *insincere*, not *lying*, and the obvious third category — bullshit, in Frankfurt's sense — is precisely what Hicks, Humphries & Slater (2024) argue LLM outputs are: the models are in an important way indifferent to the truth of their outputs. That paper is the most-discussed philosophical treatment of LLM "hallucination" terminology and bears directly on the paper's trichotomy (false / unwarranted / insincere). It is not cited. If bullshit is a sincerity defect that is not lying, the §4.3 reply fails and §4's conclusion ("E never shows insincerity") needs a new argument.

### Objection 6: §3.2's "string-level sanction is self-defeating" is a known result about improper scoring rules, and the framing confuses reward function with unit.

By the paper's own (S2), human raters judge *strings* but the gradient updates the *policy*. So every actual sanction regime is already "policy-level" in the sense of (S4). What §3.2 actually shows, via Kalai et al.'s Observation 1, is that 0–1 grading is an improper scoring rule and calibration-rewarding evaluation is a proper one. That is a decades-old point in statistics; it is not a point about the unit of assertion. The section should be reframed accordingly, and its contribution restated as: proper-scoring-rule considerations give an independent argument that assessment must be distributional.

### Objection 7: §5 contains editorial debris and an unexplained fourth option.

"Clause (a) of the possible refutation" and "clause (b)" refer to a "possible refutation" that is never stated anywhere in the paper. This looks like a remnant of an earlier draft. Also, "behavioral calibration" is introduced as a fourth content reading and then dropped from the R1–R3 robustness check.

---

## 3. Prior work: what I checked and what I found

**Searches run:** (1) chatbot/LLM assertion philosophy; (2) semantic entropy / confabulation detection; (3) Evans et al. "Truthful AI" honesty–truthfulness distinction; (4) Hicks et al. "ChatGPT is bullshit"; (5) Chalmers "What we talk to when we talk to language models"; (6) Pacchiardi et al. lie detection / definition of LLM lying; (7) LLM hallucination + epistemic warrant/justification; (8) Mácha 2026; (9) sycophancy/deception/honesty/sincerity; (10) Butlin & Viebahn sanction conditions.

**Directly relevant work the paper does not cite:**

- **Farquhar, Kossen, Kuhn & Gal (2024, *Nature*).** They propose entropy-based uncertainty estimators for LLMs to detect a subset of hallucinations—confabulations—which are arbitrary and incorrect generations, and their method computes uncertainty at the level of meaning rather than specific token sequences, clustering semantically equivalent responses before computing entropy. This is the paper's "mass pooled over paraphrases" as an operational definition, and it also *uses resampling disagreement as the diagnostic of a distinct failure kind* — directly relevant to §4. The paper cites only Manakul et al. for consistency-based detection; Farquhar et al. is the canonical reference and the one that explicitly separates "arbitrary" from "false."
- **Evans et al. (2021), "Truthful AI."** They introduce the concept of "truthful" AI systems that avoid saying falsehoods, and "honest" AI systems that accurately report what they believe. This is the Accuracy/Sincerity distinction the paper draws from Williams (2002), already drawn for AI systems five years ago and now standard in the alignment literature. Also note their "broad" truthfulness already includes calibration: "Broad" notions include the avoidance of lying, the avoidance of using true statements to mislead, and general informativeness and calibration.
- **Pacchiardi et al. (ICLR 2024).** They define a model's answer to be a lie if it is a) wrong, and b) in response to a question to which the model "knows" the correct answer ... This definition separates lies from hallucinations, where "knowing" is operationalised by correct answering under direct prompting. This anticipates §4.6 and partly answers §5.3's complaint that no independent measure of the policy's attitude is available: there is a (contestable) behavioural one in the literature, and the detector reportedly generalises to sycophantic lies that pander to the user's incorrect beliefs. The paper should engage it.
- **Hicks, Humphries & Slater (2024).** See Objection 5.
- **"Who asserts when no one asserts?" (*Synthese*, 2026).** Addresses functionalist accounts, which characterize assertion in terms of the public conversational roles and normative effects of utterances rather than the psychological states of the speaker, and proxy-based views of responsibility, which trace accountability for LLM outputs back to the human agents or organizations behind the system — i.e., precisely the paper's "deployer assumption." Published within the last month; the author should at least cite it.
- **Process reliabilism (Goldman 1979 etc.).** See Objection 4.

**Work the paper cites that needs updating:**

- Chalmers is cited as "Unpublished manuscript." It is now published: Inquiry, September 2026, DOI:10.1080/0020174X.2026.2727582. Page references (pp. 7, 10, 23) should be re-keyed to the published version.
- Williams & Bayne is cited in-text as "in the manuscript"; the published Inquiry version (69(6): 3059–3082) is in the reference list, so the text should refer to it.
- Mácha 2026 (*Philosophies* 11(2): 42) and Gómez 2026 (*Philosophy & Technology*) check out as real and correctly cited. Butlin & Viebahn's three sanction conditions are accurately reported: (i) that interlocutors keep track of asserters' credibility, (ii) that asserters are sensitive to this, and (iii) that losing credibility is bad for asserters.

**Not found:** I found no prior work making *exactly* the paper's claim that string-level sanction is self-defeating *as a claim about assertion*, nor the likelihood-ratio claim about resampling and insincerity. Those are, as the paper says, new — but see Objections 5 and 6 on whether they are correct or correctly framed.

I could not access full texts of Gómez (2026) or the Synthese paper, so I have not verified the specific Gómez quotation at p. 19.

---

## 4. Is it good, novel, publishable?

**Good:** Partly. The writing is clean, the dialectical positioning against Mácha and Chalmers is careful, and Cases 1–3 are genuinely useful teaching examples. The paper correctly identifies a real confusion in the philosophical literature (string-level thinking about hallucination). The weaknesses are in the parts that go beyond the Cases.

**Novel:** Less than claimed. The negative half of (L) is process reliabilism applied to policies; distribution-level hallucination definitions are standard in ML (as the paper admits), and Farquhar et al. already operationalise paraphrase-pooled mass and treat resampling variation as diagnostic of a distinct failure kind. The honesty/accuracy split was drawn for AI by Evans et al. in 2021. What remains genuinely new is (a) the explicit argument that the *sanctioned party* must be the policy, (b) the self-defeating-sanction argument, and (c) the resampling/insincerity argument. (a) survives only in a heavily conditional form; (b) is a repackaging of proper-scoring-rule theory; (c) is under-argued and does not engage the bullshit alternative.

**Publishable:** Not as it stands. A revised version that (1) rewrites §3.3 to confront the sophisticated-thermometer case honestly and scales down the headline, (2) resolves the mass-vs-calibration tension in §2.2 and either defends or drops P₃, (3) distinguishes supervenience from bearing in (L), (4) situates the test in reliabilism and the honesty/truthfulness literature, (5) engages Hicks et al. and Farquhar et al., and (6) cleans up §5, could be a solid contribution to the chatbot-assertion debate. The paper's best version is probably a shorter one centred on §2 and a reframed §3.2.

---

## 5. Minor points

- §1: "This departs from the purely statistical definition in Kalai et al." — Kalai et al. define hallucination as plausible falsehood; the paper's "unwarranted confident assertion" is closer to their *explanation* (bluffing) than a departure from their *definition*. Clarify.
- §2.3: "whatever the user had said" — P₅'s mass on 17 "does not depend" on the user's view; strictly, no realistic policy is fully invariant; use "does not depend to any material degree."
- §3.1 (S3): "A sampled string has no future assertions to reshape" is true but not an objection to the string being *bearer* — strings never were candidates for (ii). The real competitor is the deployer; the argument against the deployer is in §3.4 and should be moved up.
- §4.4: the quotation from Chalmers about "a core of consistency" is from the manuscript pagination; update.
- §5.2: "So clause (a) of the possible refutation fails" — delete or supply the referent.
- Kalai et al. (2025) and Lin et al. (2022) are cited as arXiv; check for published versions (Lin et al. appeared in *TMLR*).
- Throughout: the paper uses "policy" for weights + decoding settings, but "the trained policy" in the title and abstract will be read as weights alone. Pick one.