# Rulings

The paper's central slide from 'the policy fixes the verdict' to 'the policy bears the failure' is a serious gap, and so are the undefended step from pooled mass to warrant, the unexplained sanction/repair gap with its lineage equivocation, the R3 reversal in §5, and the underived likelihood ratio. The literature objections do not meet the standard for anticipation: Sambrotta, Farquhar, Hicks, Evans, Pacchiardi and the calibration work are uncited precedents or rivals, not prior statements of the paper's claims.

8 must address, 15 optional, 2 mistaken.

## MUST ADDRESS

**Concern** (chatgpt (obj. 1), gemini (obj. 5 and rec. 1), claude (obj. 3)): The same-string test shows that policy-level facts fix or ground the verdict. It does not show that the policy is the bearer of the defect. A human's evidential state fixes whether her assertion is unwarranted, but the assertion or the speaker still bears the failure. The §2.5 concession about threads turns the positive half of (L) into a near-trivial supervenience claim.

**Reason:** The abstract and title pose a bearer question ('which object bears these defects', 'unit of assertion failure'), and §3 uses it ('party sanctioned'). The argument only establishes what fixes the verdict, so the paper slides between 'fixes' and 'bears' without an argument linking them.

## MUST ADDRESS

**Concern** (chatgpt (obj. 2), gemini (obj. 1), claude (obj. 2)): The paper treats the policy's pooled mass on a claim as the asserter's 'own information' or warrant. Case 2's P₃ is called 'warranted' because corpus frequency is treated as evidence. Mass-matching (force vs. mass) and calibration (c-fraction true) are different properties that the paper treats as equivalent. A temperature-0 or RLHF-collapsed policy would always count as warranted.

**Reason:** The hallucination verdicts in Cases 1–2 depend on the step from distributional mass to evidential warrant, and the paper does not defend it. The mass-vs-calibration gap is real: a policy can match force to mass and still be miscalibrated.

## MUST ADDRESS

**Concern** (chatgpt (obj. 8), gemini (obj. 1, second horn)): Two systems could implement the same output distribution but differ in provenance, for example retrieval from an authoritative source versus a lucky heuristic. If warrant depends on provenance or training history, the distribution does not suffice for the verdict. The paper moves between a behavioural account and an epistemic one.

**Reason:** §2.4 rebuts only the architecture rival for the positive half of (L). Case 2 itself appeals to the history of the sources, and the paper defines hallucination in terms of the asserter's 'own information'. Sufficiency of the distribution is therefore an open premise.

## MUST ADDRESS

**Concern** (chatgpt (obj. 4), gemini (obj. 4)): On reading R3 the output asserts 'p with confidence c', where c is the policy's calibrated mass. P₂ in Case 1 and P₄ in Case 2 then assert p with confidence of about 0.01, so their force does not exceed their mass. By the paper's own criterion the hallucination verdict reverses, so 'no open reading reverses a verdict' is false.

**Reason:** The paper defines hallucination as force exceeding mass. On R3 force equals mass by construction, so the Case 1–2 verdict flips. 'Policy-level trivially' preserves the locus of the verdict but not its content, and §5.3 and the abstract claim the verdicts are unchanged.

## MUST ADDRESS

**Concern** (chatgpt (obj. 3), gemini (obj. 2), claude (obj. 1)): Changing the policy in response to credibility loss is corrective intervention, not sanction. A university retrains a professor, but the professor is the party sanctioned. The §3.3 reply ('the update is that optimisation', 'selected against') applies equally to any loss-trained instrument. Butlin and Viebahn's actual foil is the self-calibrating thermometer, not an engineer-recalibrated thermostat. The first reply (condition (iii) is met or dispensable) makes the headline result a conditional about non-B&V theories.

**Reason:** The step from a causal fact to a normative claim is the crux of §3, and the 'thin analogue of (iii)' is asserted rather than argued. The paper's thermostat example does miss the harder case. The searches confirmed that Butlin and Viebahn's thermometer recalibrates in response to feedback and is held not to be sanctionable because nothing can be bad for it.

**Checked:** Sambrotta's summary of Butlin and Viebahn says <cite index="68-5,68-6">even a thermometer capable of recalibrating in response to feedback does not plausibly qualify as sanctionable, since nothing can be good or bad for such systems</cite>. Williams & Bayne also discuss <cite index="69-1">Butlin and Viebahn's case of the self-calibrating thermometer</cite>. Claude's description of the foil is accurate.

## MUST ADDRESS

**Concern** (gemini (obj. 2), claude (obj. 1, last paragraph), chatgpt (obj. 3, frozen policy)): The policy is defined as a fixed distribution (weights plus decoding), but (S4) shifts to a 'lineage' sense in which πₜ is updated to πₜ₊₁. A frozen deployed policy is never sanctioned for its own assertions, and the thing sanctioned is a successor. The lineage is never individuated.

**Reason:** (S4) depends on the lineage notion, and the paper's own definition of 'policy' in §1 sits badly with it. The reliance on Butlin and Viebahn's conjecture about training-phase sensitivity does not settle the type/token problem.

## MUST ADDRESS

**Concern** (chatgpt (obj. 6), claude (obj. 6)): 'String-level sanction is self-defeating' overgeneralises. Kalai et al.'s result concerns 0–1 grading. Per-response evaluation can penalise confident errors and reward abstention, and Kalai et al.'s own remedy is applied response by response. So the real contrast is between incentive structures, not between string-level and policy-level sanction. Every actual regime already updates the policy.

**Reason:** §3.2 calls Kalai et al.'s threshold-and-penalty remedy 'policy-level' although it is a rule applied to individual answers. The string/policy contrast that carries 'more than a relabelling' is therefore blurred, and 'the single-output assumption causes the failures' is broader than the evidence.

**Checked:** Kalai et al.'s Nature version says <cite index="87-10">accuracy metrics systematically reward guessing over admitting uncertainty</cite>. It is a result about evaluation metrics, as the referees say. The Nature publication itself is real (Nature 653, May 2026).

## MUST ADDRESS

**Concern** (chatgpt (obj. 5), claude (obj. 5)): The claim P(E|insincere) ≈ P(E|sincere) is not derived. 'Insincerity carries no particular prediction about E' does not entail a likelihood ratio of about one. The ratio depends on how mass is spread and on priors over kinds of insincere policy. At most the argument yields 'E alone is weak evidence'.

**Reason:** The ratio of about one is stated in the abstract and §1 as a contribution. The argument shows only compatibility with both hypotheses and gives no model or priors from which a ratio follows.

## OPTIONAL

**Concern** (chatgpt (obj. 3)): (S2) is too strong in saying credibility assessments reach chatbot assertions only through training signals. Conversational correction, external memory, retrieval, prompt changes and deployment restrictions also carry them.

**Reason:** The premise is overstated. But §3.4 already covers deployer-side channels, and in-context channels still run through a conditional distribution that the paper's definition of policy includes. The main inference is not undermined.

## OPTIONAL

**Concern** (claude (obj. 6)): The §3.2 result is the standard statistical point that 0–1 scoring is an improper rule. It is not a point about the unit of assertion, and the section should be framed accordingly.

**Reason:** This is a matter of framing. The paper credits Kalai et al. and Sharma et al. for the results and claims only their use as premises about sanction.

## OPTIONAL

**Concern** (chatgpt (obj. 7 and lit. 9), gemini (obj. 3), claude (obj. 5)): The paper omits Hicks, Humphries and Slater (2024) on Frankfurtian bullshit. Truth-indifferent, unselective overclaiming may be a sincerity defect, or a third category, so §4.2 horn (b) and §4.3 fail and 'E never shows insincerity' needs a new argument.

**Reason:** The paper is real and relevant, but it is a rival classification of confident falsehood and not an anticipation of any claim the paper presents as new. §4.3 already addresses the closely related bluffing and Moorean move, so gemini's 'completely overlooks' is overstated. Engagement would help but the argument does not depend on it.

**Checked:** Searched and found. Hicks et al. argue that LLM falsehoods are <cite index="15-7">better understood as bullshit in Frankfurt's sense: the models are indifferent to the truth of their outputs</cite>. Their abstract presents this as an alternative to 'hallucination', not as a sincerity-failure account (abstract-level reading only). They do not make a policy-level or resampling claim.

## OPTIONAL

**Concern** (chatgpt (obj. 7)): Defining hallucination as 'unwarranted confident assertion', including true lucky guesses, is a stipulative departure from ordinary usage and needs a stronger defence. 'Bluffing' or 'overassertion' might be better labels.

**Reason:** This is largely terminological. The paper flags the departure and offers Cases 1–2 as its justification. The substantive points are covered in the warrant rulings above.

## OPTIONAL

**Concern** (gemini (obj. 5 and novelty comments), claude (obj. 4)): The same-string/different-policy test is a familiar epistemological point: propositional versus doxastic justification, or Goldman-style process reliabilism. The paper cites no epistemology and the novelty claim needs rewriting.

**Reason:** By the referees' own description this is a broader framework of which the test is an application, which does not meet the standard for anticipation. The paper does not claim the test as new in epistemology, and its novelty list (§1) concerns chatbots.

**Checked:** I did not search Goldman or Moss. These are well-known frameworks, and the ruling rests on the referees' description of them as general views, not on a reading of the texts. The claim that the test is trivial is also an argument, not a literature claim.

## OPTIONAL

**Concern** (chatgpt (lit. 3), gemini (lit. 1), claude (lit.)): Farquhar et al. (2024, Nature) on semantic entropy operationalises paraphrase-pooled mass and treats resampling disagreement as diagnostic of confabulation. It is said to anticipate the §2.2 redefinition of hallucination as low-mass guessing 'regardless of truth value' and to bear on §4.

**Reason:** It is a relevant uncited method paper, and the paper credits Lin et al. and Manakul et al. for pooling and consistency. It does not anticipate the truth-independent redefinition, because its confabulations are defined as incorrect. It also uses disagreement to detect confabulation, not insincerity.

**Checked:** Searched; abstract-level reading. Farquhar et al. detect <cite index="20-12">confabulations, which are arbitrary and incorrect generations</cite> by computing <cite index="20-13">uncertainty at the level of meaning rather than specific sequences of words</cite>. Gemini's claim that it defines hallucination regardless of truth value is wrong on this evidence.

## OPTIONAL

**Concern** (claude (lit.)): Evans et al. (2021), 'Truthful AI', already draws the accuracy/sincerity distinction for AI systems (truthful vs honest).

**Reason:** The paper takes the distinction from Williams (2002) and does not claim it as new. Truthful/honest is a precedent for the distinction, not an anticipation of any of the paper's claims.

**Checked:** Searched; snippets and summaries only. Evans et al. propose focusing on AI that only makes true statements <cite index="30-2">regardless of their beliefs (truthfulness)</cite>, alongside honesty as accurately reporting beliefs. I saw no policy-as-bearer, sanction or resampling argument.

## OPTIONAL

**Concern** (claude (lit.)): Pacchiardi et al. (ICLR 2024) define LLM lying as false output despite 'knowing' the truth, and give a black-box lie detector that generalises to sycophantic lies. This bears on §4.6 and partly answers §5.3's complaint that no independent measure of the policy's attitude exists.

**Reason:** The work is relevant to what could show insincerity, but 'knowing' is operationalised behaviourally, much as the paper treats Sharma et al.'s direct-question comparison. The paper already calls that evidence only suggestive. It anticipates none of the paper's claims.

**Checked:** Searched; abstract-level. They define lies as <cite index="43-3">false statements when incentivised to, despite 'knowing' the truth in a demonstrable sense</cite>. The detector <cite index="40-2">generalises out-of-distribution to sycophantic lies</cite>.

## OPTIONAL

**Concern** (chatgpt (lit. 5)): Sambrotta (2025) engages Butlin and Viebahn on sanctionability, allows that a fine-tunable LLM may be sanctionable without interests, and argues this does not suffice for assertion. It is said to anticipate the §3.3 policy-level analogue of (iii).

**Reason:** Sambrotta's remark is a short passage in a paper about inferentialism and meaning, and it concludes that LLMs do not assert, which the paper brackets. He does not discuss the policy as the sanctioned party, the adequacy of sanction regimes, or distribution-level assessment. That is not anticipation under the standard. It is an uncited, related treatment of (iii) that could be credited.

**Checked:** Searched; snippets of §6 and the abstract, not the full text. Sambrotta holds that <cite index="68-7">a sophisticated thermometer that can be trained by us meets the criteria for sanctioning</cite>, but that this does not make it a follower of inferential norms or a producer of genuine assertions. The paper is real (Minds and Machines 35, 2025).

## OPTIONAL

**Concern** (chatgpt (lit. 10), claude (lit.)): Recent work on proxy responsibility and functionalist accounts of assertion (Löhr 2026; the 2026 Synthese 'Who asserts when no one asserts?') is relevant to the deployer assumption in §3.4 and is uncited.

**Reason:** The work is relevant to the deployer assumption. Neither paper, on what I saw, argues for a policy-level bearer or sanction, so this is a scholarship omission and not a threat to any claim.

**Checked:** The Synthese paper exists; abstract-level. It examines <cite index="58-7">functionalist accounts and proxy-based views that trace accountability for LLM outputs back to human agents or organizations</cite>. Its concern is a tension between the two. I did not search Löhr.

## OPTIONAL

**Concern** (chatgpt, claude): Bibliographic updates: Chalmers (2026) is cited as an unpublished manuscript and has now appeared in Inquiry, Kalai et al. (2025) now has a Nature version, and Williams & Bayne is cited in the text as 'the manuscript'. Page references may need re-keying.

**Reason:** The referees are correct on the facts, but this is housekeeping that does not affect any argument.

**Checked:** Chalmers: <cite index="79-3">published in Inquiry on 16 September 2026</cite>. Kalai et al.: published in Nature 653, May 2026, under the title 'Evaluating large language models for accuracy incentivizes hallucinations' (<cite index="88-6">Nature 2026 May;653(8116):1047-1051</cite>).

## OPTIONAL

**Concern** (gemini (obj. 6), claude (obj. 7)): §5.2–5.3 refer to 'clause (a)' and 'clause (b)' of a 'possible refutation' that the paper never states.

**Reason:** The observation is correct. The text has a dangling reference, apparently left over from an earlier draft. The substance of §5.3 can be followed without it, so this is a presentational defect.

## OPTIONAL

**Concern** (claude (obj. 7)): The 'behavioural calibration' reading is introduced in §5.2 as a fourth possibility and then dropped from the R1–R3 robustness check, although the abstract says the verdicts hold on every content reading still open.

**Reason:** The omission is real, but behavioural calibration concerns where confidence is located and plausibly reduces to R1/R2 for the verdicts. The robustness claim is imprecise here without being clearly damaged.

## OPTIONAL

**Concern** (chatgpt (§3 comments)): The paper's conditional antecedent is not theory-neutral. Different norms of assertion (knowledge, commitment, function) could classify hallucination and insincerity differently, so the minimal theory of assertion needed should be specified.

**Reason:** This is a point of emphasis. The conditional strategy is legitimate, and the paper works through the relevant theories where they matter (Butlin & Viebahn, Gómez, Williams & Bayne).

## OPTIONAL

**Concern** (chatgpt (§3 comments), claude (obj. 3, minor points)): 'Policy' is not individuated consistently. The assessed unit may be the global policy, a policy–context pair or a thread's disposition. Weights plus decoding settings make temperature 0 and temperature 1 different bearers. At temperature 0 there is no resampling variation, so §4's E never arises and pooled mass must be read off logits.

**Reason:** The paper's own definition and §2.5 already assess π(·|h) context by context. The decoding-settings consequences are a clarification, not an invalid step.

## MISTAKEN

**Concern** (chatgpt (lit. 1, 2, 4, 6, 7, 8), gemini (lit. 3–5)): Yona et al. (2024), Mielke et al. (2022), Ghafouri et al. (2024), Keeling & Street (2026), Ward et al., Dung, Moss, Hofweber et al., Ji et al. and Kalai & Vempala (2024) are said to anticipate the paper's analysis of overclaiming, of verbalised versus intrinsic confidence, or of the R1–R3 content question. The novelty claim is said to be overstated.

**Reason:** On what I could check, none discusses the claims the paper presents as new (policy as bearer of assertion failure, policy-level sanction, the resampling/insincerity ratio, robustness across content readings) as a sustained endorsed line. At most they are frameworks or neighbouring empirical results. §1 already concedes that distribution-level definitions and calibration are standard in ML, and chatgpt itself finds no anticipation of the thesis. Citing more of this literature is a separate scholarship matter.

**Checked:** Checked Yona et al. (abstract: they <cite index="51-12">formalize faithful response uncertainty as the gap between intrinsic confidence in assertions and decisiveness</cite>, an empirical ML metric), Keeling & Street (abstract: attribution of credences and doubts about whether current techniques track them) and Hofweber et al. (abstract: a <cite index="105-13,105-14">proposed account of credence based on model-internal next-token probabilities</cite>, about coherence norms; gemini's title is slightly wrong). None addresses assertion failure, sanction or resampling and insincerity. I did not search Mielke, Ghafouri, Ward, Dung, Moss, Ji or Kalai & Vempala individually. No anticipation is established for them, but I did not read them.

## MISTAKEN

**Concern** (gemini (obj. 4, first part)): §5.3 is circular. If the policy's internal attitude cannot be established, hallucination cannot be diagnosed either, since it is defined as force exceeding the asserter's information.

**Reason:** The paper separates the two diagnoses. Hallucination is a relation between output force and the distribution, and is assessed over a prompt distribution. Insincerity needs an independent measure of attitude. The real worry about the 'own information' wording is covered in the warrant rulings above.

