# Rulings

The paper is a careful, well-sourced conditional argument. Two concerns are serious: the undefended Difference-making principle that carries the bearer claim, and an insincerity criterion that cannot separate insincerity from gullibility. The prior-work objections were checked, and none meets the standard for anticipation of what the paper presents as new, so they are scholarship points; I saw only abstracts and snippets, so any stronger verdict would be provisional. The other concerns are matters of emphasis or precision.)

2 must address, 13 optional, 1 mistaken.

## MUST ADDRESS

**Concern** (chatgpt (#1), gemini (#1), claude (#1, #5)): The grounds-to-bearer step (§2.5) rests on the Difference-making principle, which is undefended and arguably false. A human who randomises between a flat assertion and a hedge would still make a defective token assertion. Under determinism the 'Tuesday/Wednesday' contrast changes the producer's state rather than holding it fixed. The policy is defined as weights plus decoding rule, so the sampler is part of the producer. The sample-level Warrant condition f(s,x) ≤ c* makes the verdict depend on the draw. If the policy bears the defect and no assertion-level defect exists, that sits uneasily with the antecedent that outputs are assertions (acts).

**Reason:** The paper's headline claim, that the policy and not the string bears the defect, depends on this one premise. The paper itself concedes that if the premise is rejected, (L) shrinks to a grounding claim plus a claim about where diagnosis should aim. The coin-flip and token-norm-breach cases are live counterexamples that the paper does not answer.

## MUST ADDRESS

**Concern** (gemini (#3)): The definition of insincerity as departure from the neutral-context profile q(·|x₀) cannot separate insincerity from gullibility. A cue that shifts q and π together would count as insincere. This conflicts with §5.3's claim that sycophancy does not yet show insincerity as opposed to audience-sensitive miscalibration.

**Reason:** §4.1 says decoupling must be measured against x₀ because q itself moves under flattery pressure, and treats insincerity as a cross-context property. On that criterion every audience-tracking shift counts, including a genuine but over-deferential update. §5.3's distinction between insincerity and miscalibration then lacks a criterion. §4's twin argument runs on this definition.

## OPTIONAL

**Concern** (gemini (#2), claude (#2, partly), chatgpt (#2, partly)): q and Warrant are not operationally well-defined. It is unclear whether hedged strings ('probably p') are summed into q(p|x), and utterances may express several propositions. Unit temperature is privileged arbitrarily. Warrant f(s,x) ≤ c* makes the emission distribution π idle at the level of the single token, which sits oddly with (L)'s claim that the verdict is grounded in the relation between π and q.

**Reason:** The point is fair as a matter of precision, but Cases 1–4 do not turn on how hedges are partitioned. The paper's policy-level defect (§2.5) is mass on flat low-c* strings, so π does enter at the policy level. The paper stands without a fuller specification.

## OPTIONAL

**Concern** (chatgpt (#3, #7), claude (prior-work section)): The paper understates prior anticipation. Atwell et al.'s BASIL anticipates the §2.3 sycophancy criterion (excess shift over rational updating). Other work anticipates the policy-level, calibration-based force/warrant criterion: Kalai et al. 2026 on incentives, 'The Polite Liar', 'Epistemic Integrity in LLMs', and the generality-problem literature (Lyons 2019).

**Reason:** None of these works argues the claims the paper presents as new: the bearer claim, the warrant criterion for assertoric force, the lineage claim, or the resampling claim. The paper already credits Sharma, Li et al., Kalai et al. and Dunn for the sycophancy, incentive and calibration components, so the omissions are scholarship, not anticipation.

**Checked:** Found and read abstracts or snippets only, so any anticipation verdict would be provisional, and none meets the standard in any case. BASIL (arXiv 2508.16846) <cite index="2-5">introduces a Bayesian framework that separates sycophancy from rational belief updating</cite>. It is a measurement framework with no argument about assertion or its bearer. 'The Polite Liar' argues that RLHF produces confident fabrication, <cite index="23-5">framed through Frankfurt's bullshit as structural indifference</cite>. 'Epistemic Integrity in LLMs' <cite index="19-5">defines internal certainty versus linguistic assertiveness</cite> as a measurement problem. Neither argues for a policy-level bearer. I did not search Lyons 2019 or Wang et al. 2026 separately. Lyons is a resource for the acknowledged generality problem, not an anticipation.

## OPTIONAL

**Concern** (chatgpt (#6), claude (#3)): The resampling result (§4) is overstated. Step 2 concedes that disagreement can be evidence given background assumptions, which is how evidence always works. The headline 'not evidence of insincerity' should be restated as a non-identifiability result. Empirical work shows deceptive outputs flip more under resampling. Steps 1 and 3 are near-tautological.

**Reason:** The body already states the qualified claim: no weight beyond what spread assumptions lend. Only the abstract and thesis sentence read more strongly. The empirical stability finding is a background regularity of the kind the paper allows for, so this is a matter of emphasis and presentation.

**Checked:** Searched the stability claim. 'Think Before You Lie' (arXiv 2603.09957) reports that <cite index="38-6">deceptive answers are more easily destabilised by input paraphrasing, output resampling and activation noise than honest ones</cite>. It conditions on an initial deceptive sample in recommendation scenarios, which is not the paper's disagreement statistic E. It supports the paper's own concession that any evidential value comes from background assumptions.

## OPTIONAL

**Concern** (chatgpt (#6)): The Step 3 existence claim, that every insincere policy has a sincere twin, is stipulated rather than shown to be realisable by weights that fix both q and π.

**Reason:** The paper's policy class places no constraint beyond weights plus decoding rule, so the twin's existence is plausible. A short realisability remark would help, but the argument does not collapse without it.

## OPTIONAL

**Concern** (chatgpt (#5), gemini (#4), claude (#4)): The lineage proposal (§§3.2–3.3) establishes little. It rests on a weakened sanction condition that a self-recalibrating thermometer also meets. It substitutes the object of correction for a subject of sanction. Lineage identity is underspecified, for example when one vendor's model replaces another's. It needs a direct reply to Gómez's assertion-without-asserter view.

**Reason:** The paper states its conclusion conditionally, concedes the thermometer worry, says lineages are not sanctioned in the full sense, and flags borderline cases of identity. Gómez's view does not locate the sanction component at system level, so it falls outside the paper's conditional claim. The paper stands as a modest conditional result.

**Checked:** Checked Gómez's paper. Its abstract <cite index="67-7">argues that assertoric function can persist independently of assertoric authority</cite>, so it does not locate the sanction component at system level.

## OPTIONAL

**Concern** (gemini (#4)): Tension between §2.6 and §3.2. In §2.6 a changed conversation history is just a new argument to the same policy, yet in §3.2 a memory write or history update yields a new member of a lineage. Responsiveness through M then looks like ordinary input-sensitivity.

**Reason:** The paper individuates effective policies relative to (θ, M) for the sanction question and relative to θ for the Chalmers question, and it says clear cases suffice. Weight-update cases such as preference fine-tuning carry the lineage claim on their own, so the paper stands.

## OPTIONAL

**Concern** (claude (#2), chatgpt (#7)): The same-string/different-policy test and the negative part of (L) are close to definitional. They follow from defining hallucination as force exceeding a reference-class frequency c*, so the paper may be changing the subject. The 'overassertion' label should be primary. The warrant threshold and the reference class (generality problem, Lyons 2019) are contentious, and engagement with the norms-of-assertion literature is thin.

**Reason:** The paper flags the 'overassertion' reading itself. It acknowledges the generality problem in a footnote and again in the conclusion as an externalist cost. It fixes the threshold range and reference class by stipulation for the cases. Whether this is the concept that matters is a question of emphasis, and the paper stands without more.

## OPTIONAL

**Concern** (chatgpt (#4), gemini (#5), claude (#6)): R3 (an output asserts p with the policy's calibrated confidence) is philosophically unmotivated. It confuses content, force and a reliability statistic. No unhedged string plausibly contains an implicit probability clause, so §5 could be cut or compressed.

**Reason:** The paper treats R3 as one open reading and argues that its thesis survives each answer. The referees' point that R3 may be a poor reading affects how much of §5 is needed, not whether the argument is valid. I did not verify the claim that no one holds R3, and the ruling does not rest on it.

## OPTIONAL

**Concern** (claude (#7)): The 'single-output assumption' and 'deployer assumption' targets are not named. The single-output assumption is hard to find in the literature: ML work already treats sycophancy and calibration as distributional, and Hicks et al. and Mácha are already dispositional.

**Reason:** The introduction credits ML and epistemology for the distribution-level view and does not claim the single-output assumption is universal. Naming proponents would sharpen the framing but is not needed for the argument.

**Checked:** I did not independently check how Hicks et al. or Mácha treat the unit of assessment. The ruling rests on the paper's own acknowledgements.

## OPTIONAL

**Concern** (claude (prior-work section), gemini (checked list)): The proxy-assertion literature that §3.5's attack on the deployer assumption bears on is missing: Nickel 2013, Freiman & Miller 2020, Arora 2024, Löhr 2026, Massaguer Gómez & Gaitán Torres 2026, Gubelmann 2024, Green & Michel 2022, Saxena 2026.

**Reason:** These are rival or background works on who is answerable. None argues that lineages meet the sanction component or that deployers answer for deployment but not assertion failure. The paper already engages proxy views through Williams & Bayne and Gómez, so this is a scholarship gap.

**Checked:** Confirmed several exist. Löhr, 'Why Proxy Accounts of AI Speech Acts Fail', <cite index="49-5">argues the proxy account neglects the relational nature of speech</cite> (APQ 63(3), 2026). Massaguer Gómez & Gaitán Torres (Synthese 2026) discuss <cite index="58-6">tracing responsibility for LLM outputs back to designers, developers or deployers</cite>. Arora 2024 is a proxy-assertion account (<cite index="54-6">cited as such in Williams & Bayne</cite>). Nickel's proxy view is presented in Williams & Bayne's draft. I did not search Freiman & Miller, Gubelmann, Green & Michel or Saxena. I saw abstracts and snippets only.

## OPTIONAL

**Concern** (claude (prior-work section), chatgpt (#3)): The claim in §5.3 that no output-independent measure of the policy's attitude (R3 or a validated probe) is available is asserted without argument against recent probe-based work. Examples are the Hypocrisy Gap probe and Sarkar et al. on representation versus output. MASK also uses a neutral-context belief method.

**Reason:** The paper argues the point in §5.2 via Levinstein & Herrmann and others, and its claim is only that no validated probe exists. The cited probe work reports modest detection and is not validated in that sense. MASK uses the cross-context method the paper itself says insincerity detection needs, so it supports the paper rather than anticipating it.

**Checked:** The Hypocrisy Gap (arXiv 2602.02496) <cite index="77-3">reports AUROC of 0.55–0.73 for detecting sycophantic runs</cite>, which is modest. Sarkar et al. (2608.03035) is about contextual truth probes. MASK compares <cite index="28-2">a pressure prompt and a neutral belief-elicitation prompt</cite>. That is the paper's x₀ comparison, though it does not discuss resampling disagreement. I saw abstracts and snippets only.

## OPTIONAL

**Concern** (chatgpt (#8)): The account of sycophancy (§2.3) is too narrow. It covers factual-answer contamination and omits social or evaluative sycophancy such as validation, face-preservation and moral flattery (ELEPHANT, ICLR 2026). The paper should extend the account or restrict its scope.

**Reason:** The criterion, covariation with a user's stated attitude beyond its evidential weight, may extend to some of these cases, and the paper's scope is assertion. Whether to restrict or extend is a matter of scope and emphasis.

**Checked:** ELEPHANT exists (ICLR 2026). It <cite index="85-2">characterises sycophancy as excessive preservation of a user's face</cite> and finds LLMs <cite index="85-4">affirm whichever side the user adopts in 48% of cases</cite>. This is a scope point, not an anticipation of any claim the paper makes.

## OPTIONAL

**Concern** (claude (minor points, verified citations), chatgpt (prior-work section), gemini (#6)): Bibliographic and minor-citation points. Gómez 2026 should be cited under the surname Massaguer Gómez. Williams & Bayne should carry a DOI and the 2024 online date. Herrmann & Levinstein's 'Standards for Belief Representations' should be added alongside Levinstein & Herrmann. Other epistemology-of-AI-testimony items (Freiman 2024, Gunkel & Coghlan 2025) are suggested.

**Reason:** These are accuracy and completeness fixes that do not affect any argument.

**Checked:** Confirmed that the author of the P&T paper is <cite index="67-2">Germán Massaguer Gómez</cite>, so the reference's surname form is wrong. Herrmann & Levinstein exists (<cite index="111-3">Minds & Machines 35, 5</cite>) and proposes criteria for belief representations. I did not search Freiman 2024 or Gunkel & Coghlan 2025.

## MISTAKEN

**Concern** (chatgpt (#2)): The credal profile q is not shown to measure an epistemic attitude. Probabilities over strings may reflect convention, formatting or learned preferences, and the cited work on query–probe divergence (Liu et al. 2023; Sarkar et al. 2026) must be confronted. The insincerity argument then compares two ways of eliciting output rather than belief and assertion.

**Reason:** The paper expressly declines to treat q as a credence in any rich sense and uses it only as a score whose reliability c* measures. §§4.4 and 5.3 concede that showing insincerity needs an output-independent measure of attitude, so the referee is attacking a claim the paper does not make.

**Checked:** Searched Liu et al. 2023. <cite index="12-5">It identifies three classes of query–probe disagreement: confabulation, deception and heterogeneity.</cite> It concerns query–probe disagreement, not whether summed string probability is a confidence score. Sarkar et al. 2026 exists (arXiv 2608.03035) and <cite index="96-3">separates two forms of sycophancy that output behaviour alone cannot</cite>. Neither work bears on whether the paper's q is as the paper describes it. I saw abstracts and snippets only.

