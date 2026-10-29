I'll begin by checking the literature for prior work that anticipates the paper's central claims, then verify the paper's key citations.# Referee Report: "The Unit of Assertion Failure"

## Summary of the submission

Conditional on chatbot outputs being assertions, the paper argues that (i) hallucination and sycophancy are primarily properties of the policy-in-context (weights + decoding rule, conditioned on a prompt), not of the sampled string; (ii) warrant should be analysed reliabilistically as assertoric force not exceeding calibration-corrected confidence c*; (iii) the only system-level candidate for whatever sanction component a chatbot-assertion-friendly theory requires is a "policy lineage"; (iv) resampling disagreement is not evidence of insincerity; and (v) the verdicts survive across three readings of what outputs say, though on one reading (R3) the particular hallucination verdicts reverse.

## Recommendation

**Major revisions.** The paper is careful, unusually honest about its concessions, and asks a question the chatbot-assertion literature has mostly left implicit. But the load-bearing argument for the bearer claim is underdeveloped and arguably in tension with the paper's own treatment of decoding; the novelty claims in §1 are overstated relative to literature the paper does not cite; and the manuscript in its current form reads as a response-to-referees memo rather than a standalone article.

---

## Objections, ranked by seriousness

### 1. The "no gap between act and state" argument (§2.1) is the crux, and it does not go through as written

This is the only step that gets from "policy-level facts fix the verdict" to "the policy is the primary bearer." The paper's claim is that for a policy there is no gap between act and state because "content and force are sampled together from π(· | x)."

But the paper's own setup reintroduces the gap. The credal profile q is fixed by the weights alone; the emission distribution π is fixed by weights plus decoding. The paper explicitly says that "the same weights under greedy and under unit-temperature decoding are different policies with one credal profile" and "can differ in how often they emit low-confidence content flatly." That *is* a gap between a state (q) and an act-disposition (π). The human case the paper contrasts it with — evidence impeccable, assertion exceeds it — is structurally the same: a state and a disposition that outruns it.

The reply available to the author is that in the human case the gap is between a state and a *token act*, while here it is between two *dispositional* components of one object, so the mismatch is a property of the object. But that reply cuts both ways: a human with a standing disposition to overassert relative to her evidence also "has" the mismatch as a property of her, and we would say she (not the act) is the primary bearer of overconfidence, with acts inheriting derivatively. So either the human/policy contrast collapses — in which case (L)'s bearer part is just the generic point that dispositional defects belong to the disposition-bearer, true of humans too — or the paper needs an argument that human assertion has a *non-derivative* act-level defect that policy outputs lack. Nothing in §2.1 supplies this. The argument needs to be rebuilt, probably around the absence of a token-level locus of control (no "further choice") rather than around the absence of a gap.

### 2. The warrant criterion and the "unit" thesis are anticipated more closely than §1 admits

The §1 list of "what is new here" needs substantial revision:

- **Calibrationist reliabilism about credence.** The c* criterion is a direct application of the calibration approach to justified credence. The SEP notes that according to the calibration approach, a credence is justified iff it's produced by a well-calibrated process, and that Dunn (2015) defends the calibration approach, arguing that the relevant question is whether the process that produced A's credal state is reliable. Dunn's notion is that a process is well-calibrated if it produces beliefs in P to degree n and n % of the propositions like P are true — which is the paper's c* almost verbatim. Versions of (Calibration) have been put forward by Lam (2011), Goldman (2012), and Goldman (1986), and Tang (2016, *Mind*) and Pettigrew (2021, *Episteme*) are the standard treatments. The paper cites only Goldman (1979). The genuinely new move — applying a calibrationist standard to *assertoric force* rather than credence — should be stated as such, and the author should engage Dunn's point that the reference-class problem for calibrated processes is unresolved (Dunn construes the reliability of a credence-forming process in terms of hypothetical calibration, but he says little about which (hypothetical) counter-factual circumstances are relevant.) This matters because it bites on the paper's own cases (see objection 3).

- **Evans et al. (2021), "Truthful AI."** This widely cited report proposes a standard of avoiding negligent falsehoods — statements that contemporary AI systems should have been able to recognise as unacceptably likely to be false, and explicitly considers what types of evidence might feed into assessments of the truthfulness of an entire system. That is a system-level, reliability-of-confidence standard for AI assertion, with the deployer/institution as the evaluated party. It also draws the honesty/truthfulness distinction the paper's §4 relies on via Williams: If the AI is truthful then S matches the world. If the AI is honest, then S matches its belief. Not cited.

- **"Epistemic integrity" / epistemic calibration in the ML literature.** There is existing work framing the problem of epistemic calibration for LLMs: ensuring that the confidence expressed in a model's communication aligns with its underlying reliability, which decomposes the problem into internal and external certainty and reports gaps between internal confidence and linguistic assertiveness. This is the R2 version of the paper's hallucination criterion, stated as a normative ideal. Not cited.

- **Keeling & Street (2025, *Inquiry* 69(6))** on credence attribution to LLMs. The paper's "credal profile" q(p | x), pooled over paraphrases, presupposes that there is a fact about the model's confidence in a claim. Keeling and Street argue that LLM credence attributions made in the empirical literature on LLM evaluation are subject to non-trivial sceptical concerns. It is a distinct possibility that even if LLMs have credences, LLM credence attributions are generally false because the experimental techniques used to assess LLM credences are not truth-tracking. This is directly relevant to §5.2 and §4.5 and is in the same journal issue as Williams & Bayne. Not cited.

- **Massaguer Gómez & Gaitán Torres (2026, *Synthese*)** on the proxy view: they argue that effectively implementing the proxy component erodes two communicative ideals that are internal to the functionalist framework. This bears directly on the paper's "deployer assumption" and §3.5. Not cited.

None of these makes the paper redundant. But the §1 novelty list currently claims the calibration-corrected criterion as new, and it is not; what is new is its application to assertoric force and the same-string/different-policy test as a dialectical device.

### 3. The generality problem is not a "familiar cost" here; it decides the paper's own cases

In Case 2, P₃ (sources consistently misreport V's date, q = 0.95) is warranted because "P₃'s 0.95-claims in this domain are otherwise reliable, so c* is high." But narrow the reference class to "0.95-confidence claims about V" and c* = 0, so P₃ hallucinates. Widen it to "all 0.95 claims" and the RLHF-collapsed variant may come out warranted. Every verdict in Cases 1–2 is reference-class-sensitive, and the paper does not fix the class beyond "a domain and question type … as it is in calibration research." Since the cases are what establish the negative part of (L), the author must either (a) stipulate the reference class and defend it, or (b) show the verdicts are robust across reasonable classes. Simply inheriting the generality problem is not adequate when the illustrative cases turn on it.

### 4. The sanction section's conditional claim is either false or empty

The abstract says: "On any theory compatible with chatbot assertion, the sanction component is met, if at all, by a policy lineage." But Gómez (2026), which the paper cites as a chatbot-assertion-compatible view, holds that assertoric function can persist independently of assertoric authority, giving rise to a structurally asymmetric case of assertion without asserter, and locates accountability in human and institutional structures. On that theory the sanction component is met by institutions, not by a lineage. So either the universal claim is false, or "if at all" does all the work and the claim reduces to "where something at system level meets it, it's the lineage" — which, after the §3.3 withdrawal of the (iii)-reply, is nearly trivial (what else could it be?). §3 as a whole has been pared back honestly, but what remains needs to be presented at its true weight: a conditional about the *object* of correction, not about sanction.

Secondary: the lineage criterion ("weights of πₜ₊₁ result from training the weights of πₜ … under continuity of deployed role") excludes from-scratch retrains, which are common. The paper treats this as borderline vagueness, but it is a routine case, not an edge one.

### 5. §4's conclusion is close to definitional

Insincerity is defined as "selective decoupling … that tracks something else, such as audience approval." Given that definition, it is nearly analytic that spread in a *fixed* context does not evidence it. The dilemma in §4.2 then classifies the bluffing-from-noise case as hallucination by fiat (horn (b)). The result is correct but the section should be more candid that most of its force comes from the definition, and should explicitly argue for the definition against the thin Moorean test, rather than only replying to it. The claim that insincerity "if anything" predicts *less* spread also needs a stated model of insincere policies; the paper admits the ratio "depends on priors over kinds of insincere policy" and then asserts a direction anyway.

### 6. R3 should be dismissed on speech-act grounds, not left "open"

Under the antecedent, what an output asserts is fixed by the conventional content of the string in context. R3 says the content carries a confidence clause fixed by a hidden property of the weights that the hearer cannot access. That is not a reading of what the *output says*; it is a hypothesis about what the model *represents*. Conflating these is exactly the slide Keeling & Street warn about. §5 would be stronger and shorter if R3 were set aside as not an assertoric-content reading at all, with the credence-attribution literature cited for why.

### 7. The manuscript reads as a revision memo

Phrases such as "The earlier draft of this argument ran these together," "The referees' point … is one the revised view accepts," "I withdraw that reply," and "that claim was false" occur throughout §§3–5. These belong in a response letter, not the paper. A reader coming fresh to the article has no idea what the earlier draft claimed, and the repeated self-corrections make the structure hard to follow. This is easily fixed but must be fixed.

### 8. Smaller points

- "Hallucination" is redefined as unwarranted confident assertion, diverging from Kalai et al.'s "plausible falsehood." The paper notes this. Since the paper's own §2.2 says "overassertion" would serve equally well, consider using it and reserving "hallucination" for the ML sense; otherwise readers will read Cases 1–2 as denying that a true string can be a hallucination in the ordinary sense.
- The greedy-decoding discussion assumes the mode of π is a flat date. For a model trained to hedge, the mode may be a hedge, and greedy decoding could reduce overassertion. The claim that greedy policies "merely match force to mass" should be qualified.
- Page references to Chalmers and Williams & Bayne are to manuscript versions; both are now published in *Inquiry* with pagination and should be updated.
- Ward et al. (2023, "Honesty is the best policy") define deception at the level of an agent's policy in structural causal games; the paper should cite it as a precedent for policy-level definitions of a sincerity-type defect.
- Hila (2025, *AI & Society*) argues that LLMs approximate a type of externalist justification termed reliabilism but do not instantiate internalist standards of justification — relevant to §2.4's choice of behavioural reliabilism, if only in a footnote.

---

## Prior work checked

| Source | Status | Relevance |
|---|---|---|
| Butlin & Viebahn, "AI Assertion," *Ergo* 12 (2025) 968–988 | Verified. To be capable of assertion, an entity must meet two requirements: it must produce outputs with descriptive functions, and it must be capable of being sanctioned by agents with which it interacts. | Correctly represented. |
| Chalmers, "What we talk to…," *Inquiry* (2026), DOI 10.1080/0020174X.2026.2727582 | Verified. LLM quasi-agents … are best understood not as abstract models or even as hardware instances but as virtual entities bound to conversation-based memory threads. | Correctly represented; update page refs. |
| Williams & Bayne, *Inquiry* 69(6): 3059–3082 | Verified. | Correctly represented; update page refs. |
| Gómez, *Phil. & Tech.* 39:123 (2026) | Verified. | See objection 4. |
| Mácha, *Philosophies* 11(2):42 (2026) | Verified; the paper's "basic architectural flaw" quote matches: the hallucinations seen in LLMs stem from a basic architectural flaw in the models' design. | Correctly represented. |
| Hicks, Humphries & Slater, *Ethics & IT* 26:38 (2024) | Verified. | Correctly represented. |
| Sambrotta, *Minds & Machines* 35:46 (2025) | Not verified (search budget exhausted). Author should confirm. | — |
| Kalai et al., *Nature* 653 (2026) | Not independently verified; arXiv version confirmed. Author should confirm final pagination. | — |
| **Not cited — should be:** Dunn (2015), Tang (2016), Pettigrew (2021) on calibrationist justified credence | Verified. | Objection 2. |
| **Not cited — should be:** Evans et al. (2021), "Truthful AI" | Verified. | Objection 2. |
| **Not cited — should be:** Keeling & Street (2025), *Inquiry* 69(6): 2918–2944 | Verified. | Objections 2, 6. |
| **Not cited — should be:** Massaguer Gómez & Gaitán Torres (2026), *Synthese* 208:162 | Verified. | Objection 4. |
| **Not cited — should be:** "Epistemic Integrity in LLMs" (arXiv 2411.06528) | Verified. | Objection 2. |
| **Not cited — consider:** Freiman & Miller (2020), Nickel (2013), Green & Michel (2022), Ward et al. (2023), Hila (2025) | Partially verified. | Minor. |

I did not find any paper that states the same-string/different-policy test or the bearer thesis (L) in the context of the philosophy-of-assertion debate. The closest anticipations are at the level of practice (ML evaluation is policy-level by default), of governance (Evans et al.), and of epistemology (calibrationist reliabilism).

---

## Is it good, novel, publishable?

**Good:** In parts. The question is well posed, the test is a clean device, the Case 1–2 pair is genuinely useful against the single-output assumption, and the paper is admirably willing to retract. The writing is clear. The weakness is that the most important inference (§2.1) is the least argued, and the later sections are heavily hedged after concessions.

**Novel:** Moderately. The framing contribution — making explicit that assertion-defect verdicts in the chatbot-assertion debate are verdicts about policies, and showing what this does to Butlin & Viebahn's sanction condition — is new to that debate. The warrant criterion is not new; it is calibrationist reliabilism (Dunn, Tang, Goldman 1986/2012) redeployed. The lineage notion is new but, after §3.3, does little. §4 is a clarification rather than a result. The §1 "what is new" list must be rewritten.

**Publishable:** Yes, after major revision, in a venue such as *Philosophy & Technology*, *Minds & Machines*, *Synthese*, or *Inquiry*. I would not recommend it for a top general journal in its current form. Required for resubmission: (1) rebuild §2.1; (2) engage the calibrationist-reliabilism and Truthful-AI literatures and correct the novelty claims; (3) fix or defend the reference class for the paper's own cases; (4) restate §3's conclusion at its actual strength and address Gómez and Massaguer Gómez & Gaitán Torres; (5) remove all references to earlier drafts and referees; (6) consider dropping R3 or recasting it via Keeling & Street.