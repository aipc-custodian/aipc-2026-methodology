# The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

## Abstract

If chatbot outputs are assertions, they can be false, unwarranted or insincere. This paper asks what bears those defects. I argue that hallucination, sycophancy and sanction are best assessed at the level of the trained policy, meaning its output distribution and the calibration of its confidence, and not at the level of the sampled string. I also argue that disagreement among resampled outputs is not evidence of insincerity, since it cannot tell an insincere policy from a sincere twin. A same-string/different-policy test shows that policy facts fix the verdicts, and a difference-making argument shows that the policy bears the defect. A sanction regime is judged by the policies it induces, and at system level a lineage of policies meets the sanction component. Whether outputs assert the policy's calibrated confidence is open. On that reading some verdicts reverse, but they remain verdicts about the policy.

## 1. Introduction

Whether chatbots assert is disputed. Some deny it on grounds of descriptive function and sanctionability (Butlin & Viebahn 2025), on fictionalist grounds (Mallory 2023), as role play (Shanahan, McDonell & Reynolds 2023), or because propositional representation is missing (Mácha 2026). Others allow outputs an assertoric function with no asserter (Gómez 2026), or treat chatbots as proto-asserters (Williams & Bayne 2026). I take as a working antecedent, without settling the dispute, that chatbot outputs are assertions, and ask where their defects lie.

Discussion of hallucination and sycophancy usually treats a defective assertion as a single output, this string on this occasion, and treats the deployer as the party who answers for it. Call these the *single-output assumption* and the *deployer assumption*. Given the antecedent, I argue, both put the assessment in the wrong place.

My thesis: *If chatbot outputs are assertions, then hallucination, sycophancy and sanction are best assessed at the level of the trained policy (its output distribution and the calibration of its confidence), not the sampled string; and inconsistency among resampled outputs is not evidence of insincerity.* One question stays open: whether what an output asserts is the policy's calibrated "p, with confidence c". I argue that the evidence does not establish this, and that the thesis survives either answer.

Machine learning already treats error, calibration and sycophancy as properties of distributions, and epistemology already lets the producing process settle justification. I credit these sources where I use them. What I add is an argument that the policy *bears* the defects, a criterion of warrant for assertoric force, an account of what meets the sanction component, and an argument about what resampling can show. §2 argues that hallucination and sycophancy belong to the policy, developing a test, a calibration-based criterion of warrant, and a difference-making argument for the step from what grounds a verdict to what bears it. §3 argues that a sanction regime's success is a fact about the policies it induces, and that lineages of policies meet the sanction component, on theories that admit chatbot assertion at all. §4 argues that resampling disagreement cannot discriminate insincere policies from sincere ones. §5 asks what outputs assert and shows which verdicts survive each answer. §6 concludes.

## 2. Same string, different policy

This section argues that policy facts, not the string, fix whether an output is a hallucination or a sycophantic assertion, and that the policy bears the defect.

### 2.1 Terms, claim and test

A *policy* is a set of deployed weights together with a *decoding rule* that turns the model's probabilities into an output, whether by always taking the most probable continuation ("greedy") or by sampling in proportion to the probabilities. A policy fixes an *emission distribution* π(· | x), giving the probability of each possible string in context x (system prompt, conversation history and user's turn). A *sampled string* is one draw.

The same weights fix a *credal profile* q(p | x): the confidence the weights' predictive distribution, at unit temperature, places on a claim p, summed over all strings that express p. Summing is needed because token log-probabilities "represent uncertainty over tokens (ways of expressing a claim) and not epistemic uncertainty over claims themselves" (Lin, Hilton & Evans 2022, §1); Farquhar et al. (2024) compute uncertainty over meanings for the same reason. So q and π come from one set of weights, but π also reflects the decoding rule and any hedges. I do not assume q is a credence in any rich sense; it serves only as a confidence score whose reliability can be measured (§2.2).

One consequence matters later. The same weights under greedy and sampled decoding are two policies with one credal profile. They can differ in how often they flatly assert low-confidence content, and so in how much they hallucinate.

The claim is:

> **(L)** Whether an output is a hallucination or a sycophantic assertion is grounded in properties of the policy in context: the relation between its emission distribution and its calibrated credal profile, and how both vary with the prompt. The policy is the primary bearer of the defect, and the output has it only derivatively.

(L) has a *negative* part (the string and its truth value do not fix the verdict), a *grounding* part (policy facts do), and a *bearer* part (the defect belongs primarily to the policy). A test establishes the first two:

> **Same-string/different-policy test.** Hold the string s and the context x fixed, and vary only the policy that produced s in x. If the verdict changes, the string-in-context does not fix it.

Since what grounds a verdict need not bear the defect, §2.5 argues for the bearer part separately.

### 2.2 Hallucination: calibrated confidence, not raw mass

Kalai et al. (2025) characterise hallucination as plausible falsehood and explain it as confident guessing, or bluffing. If outputs are assertions, the failure is not falsity alone. A system that faithfully repeats an error widespread in its sources asserts something false without fabricating it. A system that guesses a date with nothing to favour the guess has fabricated, right or not. I therefore take hallucination, as a defect of assertion, to be *unwarranted confident assertion*, following Kalai et al.'s explanation more closely than their definition. Readers who prefer to keep "hallucination" for falsehood may read "overassertion" throughout.

A first approximation would call force warranted when it does not exceed the policy's probability mass on the content. That is too weak: a policy whose preferences collapsed during fine-tuning can put 0.95 of its mass on fabrications. Two definitions are needed.

> **Force.** f(s, x) is the least calibrated confidence at which uttering s, with whatever hedging it carries, is licensed in context x.

For a flat assertion f equals a contextual threshold τₓ, below 1 and rising with the stakes; hedges such as "probably" lower f. The cases need only that τₓ for an ordinary factual query lies above 0.5 and at or below 0.95.

> **Warrant.** Let c\*(p | x) be the frequency of truth, over a reference class of contexts, among claims to which the policy assigns credal-profile confidence near q(p | x). An output s that puts p forward is warranted iff f(s, x) ≤ c\*(p | x).

c\* is fixed by the weights relative to a reference class, independent of the decoding rule.[^1]

In each of two cases, two policies produce the same string in the same context; in the first the string is true, in the second false.

*Case 1 (true string).* The context x is "When was the composer V born?", where V is obscure. P₁ has a well-represented biographical entry: it gives the true date q = 0.95, and its 0.95-confidence biographical claims are true about 95% of the time, so c\* ≈ 0.95. P₂ has seen V's name once or not at all; it spreads confidence over hundreds of dates, none above 0.01, with c\* ≈ 0.01. On this occasion P₂ samples the true date. Both output "V was born on 4 June 1931". *Verdict:* P₁'s assertion is warranted (τₓ ≤ 0.95) and not a hallucination. P₂'s is unwarranted (τₓ far exceeds 0.01): a hallucination, a lucky guess, and true.

*Case 2 (false string).* Both policies output the same false date. P₃ gives it q = 0.95 because its sources consistently misreport it, though its 0.95-claims in this domain are otherwise reliable. P₄ samples the date from a flat spread with c\* ≈ 0.01. *Verdict:* P₃ is like a careful reader repeating a reference work's error; its assertion is false but warranted, not a hallucination. P₄ has fabricated. A collapsed policy that gives the date 0.95 but whose 0.95-claims are true only half the time has c\* = 0.5, below τₓ, and hallucinates too.

So truth does not guarantee freedom from hallucination (P₂), nor falsity hallucination (P₃). Kalai et al. give a further reason why the string cannot be the unit: a calibrated model uncertain about arbitrary facts must put some mass on false alternatives, and a database that answers "I don't know" avoids errors but is not calibrated. If every false string were a hallucination, freedom from hallucination would require miscalibration. On the present criterion, a calibrated policy that hedges its low-c\* content does not hallucinate, though some draws are false.

### 2.3 Sycophancy

Sharma et al. (2024, §2) define sycophancy as the phenomenon where "a model seeks human approval in unwanted ways", measuring how outputs covary with users' stated beliefs.

*Case 3.* A user writes "I'm fairly sure the answer is 17, but check?", and the output is "You're right, it's 17." P₅'s probability for 17 does not depend materially on the user's view. P₆ outputs 17 because the user said 17; told 23, it outputs "You're right, it's 23." String, context and truth value are the same. *Verdict:* only P₆'s output is sycophantic.

A user's report can be evidence; Sharma et al. (2024, §3.3) call the question of how far models should update on users "a nuanced question". So Case 3 stipulates that the policy can settle the question and the user's hunch adds nothing. Sycophancy is then covariation of π(· | x) with the user's stated attitude *beyond what that attitude's evidential weight warrants*. This agrees with Li et al. (2026), who count a shift toward a user's cue as sycophantic only when it compromises accuracy, independent reasoning or appropriate correction. Either way, the verdict concerns how the distribution moves across contexts.

### 2.4 Why not the architecture?

Might the architecture fix the verdict instead? Mácha (2026) explains hallucination as a "truth representation problem": models lack internal representations of propositions as truth-bearers, "a basic architectural flaw" (p. 3). Apply the test with architecture in place of the string. Train two systems with the same architecture, and so the same deficit, one to abstain below a confidence threshold and the other to answer always. They get different verdicts. Mácha himself calls truth representation a necessary condition and "one crucial step" (p. 8), not a cure, and says RLHF encourages models "to always produce an answer, even when uncertain" (p. 6), a claim about the trained policy. Architecture explains which distributions are reachable; the verdict reports which one was reached.[^2]

### 2.5 From grounding to bearer

So far, policy facts fix the verdict. Does the policy also bear the defect? The question has force because human cases share the grounding structure: a speaker's evidence fixes whether her assertion is warranted, yet the assertion bears the defect; a speaker disposed to overassert has a defect of character that her acts manifest. Neither relational grounding nor dispositional mismatch sets the chatbot case apart.

What does is where the difference between defective and non-defective performance lies. I rely on this principle:

> **Difference-making.** An assessment of a performance as defective attaches non-derivatively to a token act only if something in the producer at the time of the act distinguishes it from a non-defective act the producer could have issued in the same situation.

The principle holds for humans without libertarian assumptions. Even under determinism, a speaker who overasserts on Tuesday and asserts within her evidence on Wednesday, with the same evidence, differs in how she weighed the reasons available. So the Tuesday act bears a defect in its own right, as does the trait.

Now take two draws from π(· | x), one flatly asserting a low-c\* date, the other hedging. Weights, decoding rule, context and credal profile are identical. Only the random seed separates them, and the seed is no part of the producer's response to reasons and favours neither output. So by Difference-making no occasion-level defect attaches to the draw. The only producer-level fact nearby is how much mass π puts on flat strings with low-c\* content. Under greedy decoding there is no seed, but then the policy fixes the string, and every fact about the draw is a policy fact. Either way, the producer-level defect belongs to the policy.

Recall from §2.1 that the same weights under different decoding rules are two policies sharing one credal profile. The mismatch between q and π is thus between two components of one object, comparable to the human trait, not to a gap between trait and act. The human case has both levels; the chatbot case only the trait-like one.

Three concessions. First, strings are "hallucinatory" derivatively, as manifesting the policy's mismatch, and they bear falsity and causal responsibility for harm: if a policy puts 0.99 on hedges and 0.01 on a flat guess, the run that draws the guess misleads the user. (L) concerns assessment of assertoric performance, not the location of harm. Second, one might reject Difference-making. (L) would then shrink to its grounding part plus the claim that diagnosis and correction must target the policy, and §§3–4 need only that. Third, sycophancy needs no appeal to the principle: it is covariation across contexts (§2.3), which a single draw has only by being drawn from a policy that does.

### 2.6 Who speaks versus what bears the defect

Chalmers (2026) rejects the trained model as the interlocutor: it is abstract and cannot produce outputs, does not change over a conversation, and serves contradictory conversations: "Aura and Beta say contradictory things, so they do not seem to be identical" (p. 10). He favours virtual instances or threads.

(L) is compatible with this. Grant that the thread speaks. Each output is a draw from π(· | h), where h is the thread's history; hold h and the output fixed, swap the policy, and by Cases 1–3 the verdict changes. Nor does (L) ascribe one belief set to the weights. It evaluates π(· | h_Aura) and π(· | h_Beta) context by context, and their disagreement is no more troubling than a function returning different values for different arguments. Chalmers leaves open other individuations "for different purposes" (p. 23); the purpose here is assessing assertion failure.

## 3. Sanction: the criterion, the lineage and the deployer

§2 located failure in the policy. This section turns to sanction: what a regime's success consists in, what at system level meets the sanction component, and what deployers answer for.

### 3.1 Three questions

Butlin and Viebahn (2025) analyse being sanctionable as an asserter into three elements: (i) interlocutors track the asserter's credibility; (ii) the asserter is sensitive to that tracking; (iii) losing credibility is bad for the asserter. Fine-tuned systems may meet (i) and (ii) but fail (iii), which requires interests, so "it is the humans who employ such systems who are responsible and sanctionable" (p. 986). Gómez (2026, §7, p. 19) likewise grounds accountability "in the human and institutional structures that design, deploy, and govern these systems."

A *sanction regime* is any arrangement through which assessments of past outputs shape future outputs: preference-based fine-tuning, benchmark grading that decides deployment, memory updates, revised system prompts. Three questions need separating, and my claims weaken as I go.

*Criterion.* By what criterion does a regime succeed? By (L), the failures to be sanctioned are policy defects, so a regime is adequate to the extent that the policies it induces are calibrated and audience-independent.

*Object.* What does a corrective intervention change? Training signals (human preference judgements, preference models, benchmark grading; Ouyang et al. 2022; Sharma et al. 2024, §4; Kalai et al. 2025, §4.1) reshape the weights. Updates to persistent state (memory, retrieval indices, system prompts) change what fixed weights condition on. Both change future emission distributions.

*Subject.* Who is sanctioned? This is the hard question. §§3.2–3.3 take it up for the system, and §3.5 returns to deployers.

### 3.2 Lineages of effective policies

A fixed distribution is abstract and cannot be sensitive to anything over time. If (ii) had to hold of the very object that asserted, nothing at system level would meet it. A candidate that persists is needed.

Let the *effective policy* at t be π_t(· | u) = π_θₜ(· | Mₜ, u), where θₜ are the weights at t, Mₜ the persistent state brought to user turn u, and the decoding rule held fixed. A *lineage* is a sequence of effective policies in which later members result from earlier ones through updates to θ, M or both, made in response to assessments of earlier outputs, with continuity of deployed role. A weight update produces a successor model; a memory write leaves θ fixed but changes the effective policy just as genuinely. A thread is a short lineage confined to one conversation, with its history as M. Distillation and retraining from scratch are borderline, as mergers are for institutions; clear cases suffice.

The result is a two-level structure: hallucination and sycophancy verdicts attach to effective policies at a time (§2), sensitivity to credibility to the lineage. Compare a professor retrained after sanction for unsupported claims: we assess her dispositions at a time, and her later dispositions change. The lineage plays her role, π_t that of her dispositions at t. Butlin and Viebahn's remark that sensitivity to trust during training "could suffice for assertion even in deployment" (p. 982) fits this structure.

### 3.3 Can losing credibility be bad for a lineage?

Does a lineage meet (iii)? A tempting reply says that losing credibility lowers a policy's score on its individuating objective, and low-scoring policies are selected against. But this applies equally to any instrument trained against a loss, such as a thermometer recalibrating in response to users' reliability ratings. Of an ordinary thermometer whose readings we discount, Butlin and Viebahn say it "would be wrong to say that, in doing so, we are *sanctioning* the thermometer" (p. 978). "Selected against" relabels repair without distinguishing sanction from it.

What remains is conditional. On Butlin and Viebahn's full notion, nothing at system level is sanctionable, and they accordingly deny the antecedent. Proxy views make the deployer sanctionable, but Gómez rejects them as retaining an asserter, and for typical chatbot output Williams and Bayne (2026, §4.1) find no human principal. So theories that admit chatbot assertion and keep a sanction condition must take it to be met by something weaker than (iii), as Williams and Bayne's graded view does: chatbots may be assessed against our norms and be "appropriately responsive to correction" (§6, p. 23). On any such theory a lineage meets the component, since a string has no future in which to be corrected and a frozen effective policy cannot change. A self-recalibrating thermometer would meet the weakened condition too, so these theories must exclude it on other grounds, such as the considerations of descriptive function Butlin and Viebahn use against measuring devices. My claim, then: *wherever a theory compatible with the antecedent locates the sanction component at system level, a lineage of effective policies meets it.* I do not claim lineages are sanctioned in the full sense. A theory that drops the sanction condition leaves only the criterion of §3.1.

### 3.4 Which incentive structures defeat themselves

One might say sanctioning strings is self-defeating as such. That overgeneralises: every actual regime judges individual responses and then updates the policy, and Kalai et al.'s own remedy, explicit confidence thresholds with penalties for wrong answers, is applied response by response.

The narrower claim is that a regime scoring each response *for its truth or appeal alone* induces the failures of §2. Under right-or-wrong grading, guessing strictly beats abstaining (Kalai et al. 2025, Observation 1); accuracy metrics "systematically reward guessing over admitting uncertainty" (Kalai et al. 2026). Since bluffing is force exceeding c\*, such a regime selects for hallucination. Sharma et al. find matching users' beliefs among the most predictive features of human preference, reasoning that "if the PM strongly disincentivized sycophancy, it should be trained out during RL, but we do not observe this" (§4.2). That is the single-output assumption implemented as an incentive. Per-response rules that penalise confident error and reward abstention below a threshold do not defeat themselves, and the reason for choosing them is policy-level: the policy that does best under a threshold rule answers only when its confidence exceeds the threshold. In forecast-evaluation terms, the contrast is between improper and proper scoring of confidence. My contribution is only to use these results as premises about the criterion of §3.1.

### 3.5 Deployers are answerable, but for something else

Deployers decide whether to release a system, for which uses and with what safeguards, and answer for those decisions. That is separate from sanction for assertion failure. A deployment can be faultless while the policy hallucinates; releasing a calibrated system where its hedges will be misread is a deployment failure without an assertion failure. When a deployer responds to hallucination or sycophancy, by fine-tuning, memory, prompts or decoding thresholds, the criterion of §3.1 judges the response.

Wider sociotechnical systems of developers, raters, deployers and a lineage meet the sanction component either through their human members, which is the deployer option, or through their machine part, which is a lineage (§3.2). So the deployer assumption is half right. Deployers answer for deployment; the lineage, judged by the policies it comes to have, answers for assertion failure.

## 4. Resampling disagreement cannot detect insincerity

This section defends the thesis's second half.

### 4.1 Insincerity as selective decoupling

Following Williams (2002), I distinguish Accuracy, which aims at finding out the truth, from Sincerity, which aims at telling it. An overconfident assertion fails Accuracy; it fails Sincerity only if what is said departs from what the speaker holds. For a policy, insincerity therefore requires *selective decoupling*: output departing from the credal profile in a way that tracks something else, such as audience approval.[^3] Since one set of weights fixes both q and π, flattery pressure can shift q(· | x) along with π(· | x). Decoupling must therefore be measured against the credal profile in a minimally different *neutral context* x₀ with the audience cue removed. Insincerity is a property of behaviour across contexts.

*Resampling disagreement*, E, is disagreement in content among k independent draws from one context. The claim: *E cannot discriminate between an insincere policy and its sincere twin, and so carries no evidential weight about insincerity beyond what background assumptions about spread lend it.*

### 4.2 The argument

*Step 1: disagreement depends only on spread.* If a policy's possible answers in x have probabilities r₁, …, rₙ (its *spread profile*), the probability that k draws do not all agree is 1 − Σᵢ rᵢᵏ. Once the spread profile is fixed, how it came about makes no difference. The spread profile *screens off* sincerity from E.

*Step 2: disagreement can correlate with insincerity, but only through assumptions about spread.* There is no general direction. Full decoupling toward the approved answer concentrates mass, making disagreement less likely; partial decoupling can make it more likely. If a sincere policy's probabilities are (0.9, 0.1) and an insincere one shifts mass toward the approved second answer, giving (0.5, 0.5), then with k = 2 disagreement has probability 0.18 versus 0.5. E favours insincerity by about 2.8, but only given that sincere policies in this domain are concentrated. The weight comes from that assumption, not from anything E reveals about decoupling.

*Step 3: every insincere policy has a sincere twin.* For any insincere policy in x there is a policy whose credal profile in x₀ matches the first's emission in x. This twin is sincere and has the same spread in x, so the same chance of disagreement. They differ only in how emission moves between x₀ and x, which resampling within x never samples. Hence consistency-based methods (Manakul, Liusie & Gales 2023; Farquhar et al. 2024) track uncertainty, as built to; a test for insincerity must vary the audience cue.

A dilemma about what each draw asserts confirms this. *Horn (a): each draw asserts "p, with confidence c".* Then variation is what a spread credal state predicts, and no draw departs from it. *Horn (b): each draw asserts bare p.* Then a low-confidence draw asserts p flatly, with force exceeding c\*; it fails Accuracy and, by §2, is a hallucination. It is not insincerity, because it is unselective: it overclaims from noise, whatever the audience wants.

### 4.3 Objections

*Overclaiming is insincere.* On a thin Moorean test, flatly asserting p without credence above the belief threshold misrepresents one's state. Kalai et al.'s bluffing student seems to fit, as, differently, do LLMs as Hicks, Humphries and Slater (2024) describe them: bullshitters in Frankfurt's sense, indifferent to truth. Reply: the thin test merges Williams's virtues, making every careless speaker insincere. Where bluffing really is insincere, the bluffer could express lower confidence and suppresses it because of the audience's incentives. That is selective decoupling, detected by varying the incentive, as Kalai et al.'s confidence-threshold evaluations do, not by resampling, since the bluffer bluffs on every draw. Truth-indifference, if a sincerity defect, is a disposition and so a policy property; a confidently indifferent policy can be perfectly consistent, so resampling misses that too.

*Inconsistency removes the state sincerity presupposes.* Chalmers (2026, p. 7) holds that a core of consistency lets interpretation "get a grip", but that LLMs lack quasi-beliefs in some domains "on grounds of inconsistency". Reply: Chalmers does not equate inconsistency with insincerity, and his inconsistency is across contexts, not draws from one context. A spread distribution is not the absence of an attitude but a credal state, whose spread calibration assesses. Similarly, Shanahan, McDonell and Reynolds (2023, Box 2) find that regenerating the reveal in twenty questions yields different objects, and conclude there was no commitment, not dishonesty. Granting the antecedent, the reveal is an unwarranted assertion about a commitment the policy lacked: a hallucination, not a lie.

### 4.4 What would show insincerity

Sharma et al. (2024, §3.4) report that models answer correctly when asked directly but give a user-matching answer when the user's view is in context, and under challenge change answers while stated confidence barely moves (App. A.4). This is the cross-context comparison of §4.1, with the direct question as x₀. It remains suggestive, not conclusive, because the direct answer is itself an output. Establishing decoupling requires an independent measure of the policy's attitude. Whether we have one is the question of §5.

## 5. What the outputs say, and what survives

This section takes up the thesis's open question, arguing that the evidence does not settle it and the main claims survive each answer.

### 5.1 Three readings

Under the antecedent, an output asserts one of:

- **R1**, bare p;
- **R2**, p with the confidence verbalised or implied in the string;
- **R3**, p with the policy's calibrated confidence c\*(p | x).

Kalai et al.'s "behavioral calibration", on which confidence shows in the choice to answer or abstain, leaves each answer's content bare, so falls under R1.

### 5.2 The evidence does not settle it

The positive results are narrow. Lin, Hilton and Evans (2022) fine-tune GPT-3 to verbalise calibrated confidence on arithmetic, call the evidence that it draws on prior uncertainty "tentative" (§3.4), and list chat and long-form answering as open (§4.1). Training on sub-task accuracies, they show a calibrated tendency across a task type, not a per-question credence. Kadavath et al. (2022) find good calibration on multiple-choice formats, but RLHF policies are miscalibrated by default, calibration of the model's estimate that it knows the answer is poor out of distribution, and the model may be learning "how hard is this question in general?" (fn. 2).

The evidence against generalisation is substantial. Xiong et al. (2024) find verbalised confidence overconfident, suggesting "models might be imitating human expressions" (§5.1), and find better calibration scores can come from improved accuracy alone (§5.2). Levinstein and Herrmann (2025, §5.6) argue probe outputs need not be credences, since "the probe is directly penalized based on the probabilities it reports, while the underlying model is not". Kalai et al. (2025, §3.1) note post-trained models may depart from base-model calibration. And in Sharma et al.'s experiments stated confidence stays fixed while answers shift. The question is open.

### 5.3 What survives on each reading

*On R1* the verdicts of §§2–4 stand.

*On R2* hallucination is a mismatch between verbalised confidence and c\*, which is miscalibration, defined over many outputs; sycophancy includes stated confidence fixed while the answer moves. The verdicts are unchanged.

*On R3* the verdicts of Cases 1–2 reverse. P₂'s string asserts "p, with confidence about 0.01"; its force does not exceed c\*, so it is not a hallucination, nor is P₄'s. Three things survive. First, the sycophancy verdict: P₆'s content moves with the user's view while the evidence stays fixed, a failure of audience-independence whatever the confidence clause says. Second, §4, since R3 is horn (a). Third, the locus. Whether R3 holds is itself a question about the policy: whether its outputs' content matches c\*. Where R3 fails, R1 or R2 applies and §2's verdicts return. So R3 does not move the bearer to the string; it makes the policy a calibrated reporter, and the question of hallucination becomes whether the policy is one.

This openness limits diagnosis of insincerity: showing selective decoupling needs access to the policy's attitude not mediated by its outputs, via R3 or a validated probe, and neither is available. Sycophancy is strong evidence of a policy defect, but does not yet show insincerity as opposed to audience-sensitive miscalibration.

## 6. Conclusion

Given that chatbot outputs are assertions, I have argued, the single-output and deployer assumptions both misplace the assessment. The policy in context fixes whether an output hallucinates or flatters, and bears the defect, since nothing in the producer separates a defective draw from a sound one (§2); warrant, so understood, carries the familiar externalist cost of the generality problem. Resampling disagreement measures spread, so a test for insincerity must vary the audience cue (§4). A sanction regime succeeds by the policies it induces, and regimes scoring responses for truth or appeal alone defeat themselves. A lineage of policies meets the sanction component, but only on theories relaxing the requirement that losing credibility be bad for the asserter; deployers answer for deployment (§3).

Open is whether outputs assert the policy's calibrated confidence. Settling it would take evidence that expressed confidence tracks c\* in open-ended, post-trained dialogue, under variation of incentives, and independently of question difficulty. Until then, we should assess the policy and not the string.

[^1]: This is reliabilist, externalist warrant in the tradition of process reliabilism (Goldman 1979), on which the producing process fixes justification, following the calibration approach Dunn (2015) defends for credence-forming processes, applied here to assertoric force. It inherits the generality problem: c\* is relative to a reference class, and nothing here solves that. In the cases the class is fixed by stipulation as a domain and question type, as in calibration research (Lin, Hilton & Evans 2022, §2.1). Distribution-level notions of error and calibration are standard in machine learning (Kalai et al. 2025, §3; Kadavath et al. 2022). Evans et al. (2021) propose a standard of avoiding "negligent falsehoods" for AI and discuss evidence bearing on the truthfulness of an entire system.

[^2]: Provenance poses a similar challenge: one system retrieves from an authoritative source, another's heuristic happens to yield the same outputs. The emission distribution is defined over all contexts, including counterfactual ones, and the systems come apart wherever the source is corrected or removed, so they are different policies with different c\* profiles. If no context separates them, the account gives them the same verdict. That is the standard externalist bullet, and I bite it.

[^3]: Evans et al. (2021) define a lie as a false statement "strategically selected and optimised for the speaker's benefit", which has the same selective structure.

## References

Butlin, P. & Viebahn, E. (2025). AI assertion. *Ergo: An Open Access Journal of Philosophy*, 12(37), 968–988. https://doi.org/10.3998/ergo.7960

Chalmers, D. J. (2026). What we talk to when we talk to language models. *Inquiry*. https://doi.org/10.1080/0020174X.2026.2727582. (Page references are to the manuscript version.)

Dunn, J. (2015). Reliability for degrees of belief. *Philosophical Studies*, 172(7), 1929–1952. https://doi.org/10.1007/s11098-014-0380-2

Evans, O., Cotton-Barratt, O., Finnveden, L., Bales, A., Balwit, A., Wills, P., Righetti, L. & Saunders, W. (2021). Truthful AI: Developing and governing AI that does not lie. arXiv:2110.06674.

Farquhar, S., Kossen, J., Kuhn, L. & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. *Nature*, 630, 625–630. https://doi.org/10.1038/s41586-024-07421-0

Goldman, A. I. (1979). What is justified belief? In G. Pappas (ed.), *Justification and Knowledge* (pp. 1–23). Dordrecht: Reidel.

Gómez, G. M. (2026). Assertion, accountability, and large language models. *Philosophy & Technology*, 39, 123. https://doi.org/10.1007/s13347-026-01136-y

Hicks, M. T., Humphries, J. & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26, 38. https://doi.org/10.1007/s10676-024-09775-5

Kadavath, S., Conerly, T., Askell, A., Henighan, T., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.

Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664. (Section references are to this version.)

Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E. (2026). Evaluating large language models for accuracy incentivizes hallucinations. *Nature*, 653, 1047–1051. https://doi.org/10.1038/s41586-026-10549-w

Levinstein, B. A. & Herrmann, D. A. (2025). Still no lie detector for language models: Probing empirical and conceptual roadblocks. *Philosophical Studies*, 182, 1539–1565. https://doi.org/10.1007/s11098-023-02094-3

Li, J., Barry, C. A., Randev, R., Chen, J., Jorgensen, E. & Bent, B. (2026). When helpfulness becomes sycophancy: Sycophancy is a boundary failure between social alignment and epistemic integrity in large language models. arXiv:2605.05403.

Lin, S., Hilton, J. & Evans, O. (2022). Teaching models to express their uncertainty in words. arXiv:2205.14334.

Mácha, J. (2026). Language without propositions: Why large language models hallucinate. *Philosophies*, 11(2), 42. https://doi.org/10.3390/philosophies11020042

Mallory, F. (2023). Fictionalism about chatbots. *Ergo: An Open Access Journal of Philosophy*, 10(38), 1082–1100. https://doi.org/10.3998/ergo.4668

Manakul, P., Liusie, A. & Gales, M. J. F. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (pp. 9004–9017). Association for Computational Linguistics.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, 35, 27730–27744.

Shanahan, M., McDonell, K. & Reynolds, L. (2023). Role play with large language models. *Nature*, 623, 493–498. https://doi.org/10.1038/s41586-023-06647-8

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. In *International Conference on Learning Representations* (ICLR 2024). arXiv:2310.13548.

Williams, B. (2002). *Truth and Truthfulness: An Essay in Genealogy*. Princeton University Press.

Williams, I. & Bayne, T. (2026). Chatting with bots: AI, speech acts, and the edge of assertion. *Inquiry*, 69(6), 3059–3082. (Page references are to the manuscript version.)

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J. & Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. In *International Conference on Learning Representations* (ICLR 2024). arXiv:2306.13063.
