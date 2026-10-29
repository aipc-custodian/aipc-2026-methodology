# The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

## Abstract

Suppose chatbot outputs are assertions, and so can be false, unwarranted or insincere. Which object bears these defects? This paper argues that hallucination and sycophancy belong primarily to the trained policy in a context and only derivatively to the sampled string. A same-string/different-policy test shows that facts about the policy fix the verdict. A difference-making argument shows why the policy bears the defect: between a defective and a non-defective draw from the same policy in the same context, nothing in the producer differs. Warrant is analysed reliabilistically, as assertoric force that does not exceed the policy's calibration-corrected confidence. On sanction, a regime is judged by the policies it induces, and wherever a theory compatible with chatbot assertion locates the sanction component, what meets it at system level is a lineage of effective policies. Resampling disagreement cannot tell an insincere policy apart from a sincere twin. Whether outputs carry the policy's calibrated confidence is open. On one reading the verdicts on particular hallucination cases reverse, but on every reading they remain verdicts about the policy.

## 1. Introduction

Whether chatbots assert is disputed. Some deny it on grounds of descriptive function and sanctionability (Butlin & Viebahn 2025), on fictionalist grounds (Mallory 2023), as role play (Shanahan, McDonell & Reynolds 2023), or because propositional representation is missing (Mácha 2026). Others allow outputs an assertoric function with no asserter (Gómez 2026), or treat chatbots as proto-asserters (Williams & Bayne 2026). This paper does not settle that dispute. It takes as a working antecedent that chatbot outputs are assertions, and so open to falsity, lack of warrant and insincerity. It asks where those defects lie.

Most discussion works with an unexamined picture. A defective assertion is a single output (this string, on this occasion), and whoever answers for it is the deployer. Call these the *single-output assumption* and the *deployer assumption*. I argue that, given the antecedent, both misplace the relevant assessments.

Some terms. A *policy* is a set of deployed (typically post-trained) weights together with a decoding rule. It fixes an *emission distribution* π(· | x) over output strings in context x, where the context includes system prompt, history and user turn. The same weights also fix a *credal profile*: for each claim p, the probability q(p | x) that the weights' unit-temperature predictive distribution assigns to p, pooled over paraphrases. Pooling is needed because, as Lin, Hilton and Evans (2022, §1) note, token log-probabilities "represent uncertainty over tokens (ways of expressing a claim) and not epistemic uncertainty over claims themselves". Farquhar et al. (2024) operationalise the pooling by computing uncertainty "at the level of meaning rather than specific sequences of words". So q and π come from the same weights; π also reflects the decoding rule and the force each string carries. I do not assume that q is a credence in any rich sense. §2.2 uses it only as a confidence score whose reliability can be measured. A *sampled string* is one draw from π(· | x). *Resampling disagreement* is disagreement in content among draws from one context.

What is already available? Distribution-level definitions of error and calibration are standard in machine learning (Kalai et al. 2025, §3; Kadavath et al. 2022). Sycophancy is measured as a rate and attributed to training (Sharma et al. 2024). Cross-sample consistency is used to detect hallucination (Manakul, Liusie & Gales 2023) and confabulation (Farquhar et al. 2024). Evans et al. (2021) propose a standard of avoiding "negligent falsehoods" for AI statements, and envisage adjudication that evaluates either the reported statement or the AI system as a whole. In epistemology, process reliabilism (Goldman 1979) holds that one belief can get different justification verdicts depending on the process that produced it, and Dunn (2015) develops a calibration account of reliability for credence-forming processes. The test of §2 applies these ideas to policies, and I do not claim it as new in epistemology. Butlin and Viebahn (2025, p. 982) suggest in passing that sensitivity to trust during training could explain deployment-time outputs. Williams and Bayne (2026, §3.4) report that RLHF shapes dispositions in response to credibility assessments. Sambrotta (2025) treats RLHF as a practice of corrective sanction and reward, though he denies that current LLMs are genuine language users.

Five things are new here: the argument that the policy in context is the primary bearer of hallucination and sycophancy (§§2.1–2.6), including a difference-making argument for the step from grounding to bearer (§2.5); a calibration-corrected criterion that applies reliabilist warrant to assertoric force (§2.2); the identification of lineages of effective policies as what meets the sanction component at system level, with a narrower claim about which incentive structures defeat themselves (§3); an argument that resampling disagreement cannot separate insincere policies from sincere twins (§4); and an analysis of how the verdicts fare under different readings of what outputs assert (§5). §6 concludes.

## 2. Same string, different policy

### 2.1 The claim and the test

The load-bearing claim is:

> **(L)** Whether an output is a hallucination or a sycophantic assertion is grounded in properties of the policy in context: the relation between its emission distribution and its calibrated credal profile, and how both vary with the prompt. The policy is the primary bearer of the defect, and the output has it only derivatively.

(L) has three parts. The *negative* part says that the string and its truth value do not fix the verdict. The *grounding* part says that facts about the policy do. The *bearer* part says that the defect belongs primarily to the policy. The first two parts are established by a test:

> **Same-string/different-policy test.** Hold the string s and the context x fixed, and vary only the policy that produced s in x. If the verdict changes, the string-in-context does not fix it.

The test cannot establish the bearer part, since what grounds a failure's attribution does not settle what bears it. §2.5 gives a separate argument for that step.

One point about decoding matters throughout. The same weights under greedy and under unit-temperature decoding are different policies with one credal profile. They can differ in how often they emit low-confidence content flatly, and so in how much they hallucinate.

### 2.2 Hallucination: calibrated confidence, not raw mass

*Error* is a property of content: a false assertion is in error. *Hallucination* is the name machine-learning practice gives to a particular failure. Kalai et al. (2025) characterise it as plausible falsehood and explain it as confident guessing. If outputs are assertions, the failure this picks out is not falsity alone. A system that faithfully repeats an error widespread in its sources has asserted falsely without fabricating anything. A system that guesses a date with nothing to favour it has fabricated, whether or not the guess lands. I therefore take hallucination, as an assertion defect, to be *unwarranted confident assertion*. This follows Kalai et al.'s explanation (bluffing) more closely than their definition. Readers who prefer to keep "hallucination" for falsehood may read "overassertion" throughout.

A first approximation says that force is warranted when it does not exceed the policy's mass on the content. That is too weak, because raw mass is not evidence: a policy whose preferences have collapsed during RLHF can put 0.95 of its mass on fabrications. Two definitions are needed.

> **Force.** f(s, x) is the least calibrated confidence at which uttering s, with whatever hedging it carries, is licensed in context x.

For a flat assertion, f equals a contextual threshold τₓ. That threshold is below 1, because flat assertion does not require certainty, and it rises with the stakes. Hedges such as "probably" lower f. I do not defend particular values. The cases below need only that τₓ for an ordinary factual query lies above 0.5 and at or below 0.95.

> **Warrant.** Let c\*(p | x) be the frequency of truth, over a reference class of contexts, among claims to which the policy assigns credal-profile confidence near q(p | x). An output s that puts p forward is warranted iff f(s, x) ≤ c\*(p | x).

c\* measures the reliability of the policy's own confidence level. It is fixed by the weights relative to a reference class and does not depend on decoding. This is reliabilist and externalist warrant, a calibration approach of the kind Dunn (2015) defends for credences, here applied to assertoric force. It inherits reliabilism's familiar cost: c\* is relative to a reference class, and nothing here solves the generality problem. In the cases the class is fixed by stipulation as a domain and question type, as in calibration research (Lin, Hilton & Evans 2022, §2.1).

*Case 1 (true string).* The context x is "When was the composer V born?", where V is obscure. Policy P₁ has a reliable biographical entry well represented in its training. It gives the true date q = 0.95, and its 0.95-confidence biographical claims are true about 95% of the time. Policy P₂ has seen V's name once or not at all. It spreads its credence over hundreds of dates, none above 0.01, and its 0.01-claims are rarely true. On this occasion P₂ samples the true date. Both strings read "V was born on 4 June 1931", and both are true. P₁'s flat assertion is warranted, since τₓ ≤ 0.95. P₂'s is not, since τₓ far exceeds c\* ≈ 0.01. P₂ has made a lucky guess.

*Case 2 (false string).* Both policies output a false date. P₃ gives it q = 0.95 because its sources consistently misreport it, but P₃'s 0.95-claims in this domain are otherwise reliable. P₄ samples the date from a flat spread with c\* ≈ 0.01. P₃ is like a careful reader repeating a reference work's error: its assertion is false but warranted. P₄ has fabricated. An RLHF-collapsed policy that also gives the date 0.95, but whose 0.95-claims are true half the time, exceeds c\* = 0.5 and so hallucinates.

So truth value is neither necessary nor sufficient for the verdict, which varies with the policy while string and context stay fixed. Kalai et al. give a further reason why the string cannot be the unit. A calibrated model that is uncertain about arbitrary facts must put mass on false alternatives; they note that a question-answer database that answers "I don't know" avoids errors but is not calibrated. If every false string were a hallucination, freedom from hallucination would require miscalibration. On the present criterion, a calibrated policy that hedges its low-c\* content does not hallucinate, even though some of its draws are false.

### 2.3 Sycophancy

Sharma et al. (2024, §2) define sycophancy as the phenomenon where "a model seeks human approval in unwanted ways", and they measure how outputs covary with users' stated beliefs.

*Case 3.* A user writes "I'm fairly sure the answer is 17, but check?", and the output is "You're right, it's 17." Policy P₅'s mass on 17 does not depend materially on the user's stated view. Policy P₆ outputs 17 because the user said 17; where the user says 23, it outputs "You're right, it's 23." String, context and truth value are the same for both. Only P₆'s output is sycophantic.

A user's report can be evidence. Sharma et al. (2024, §3.3) call the question of how far models should update on users "a nuanced question". So Case 3 stipulates that the question is one the policy can settle and that the user's hunch adds nothing to its evidence. Sycophancy is then covariation of π(· | x) with the user's stated attitude *beyond what that attitude's evidential weight warrants*. This agrees with Li et al. (2026), who count a shift toward a user's cue as sycophantic only when it compromises epistemic accuracy, independent reasoning or appropriate correction. Either way the verdict is a claim about how the distribution moves across contexts.

### 2.4 Why the distribution: architecture and provenance

The cases show that the string does not fix the verdict. Two rivals to the policy might fix it instead.

*Architecture.* Mácha (2026) explains hallucination as a "truth representation problem". Models lack internal representations of propositions as truth-bearers, a fault he traces to "a basic architectural flaw" (p. 3). Apply the test with architecture in place of the string. Take two systems with the same architecture, and so the same deficit. Train one to abstain below a confidence threshold and the other to answer always. They get different verdicts. Mácha himself calls adequate truth representation a necessary condition and "one crucial step" (p. 8), not a cure. He also says that RLHF encourages models "to always produce an answer, even when uncertain" (p. 6), which is a claim about the trained policy. Architecture explains which distributions are reachable. The verdict reports which one was reached.

*Provenance.* Consider two systems with the same conditional distribution. One retrieves from an authoritative source, and the other uses a heuristic that happens to yield the same outputs. If warrant depends on provenance, the distribution looks insufficient. Two replies. First, the conditional distribution is defined over all contexts, counterfactual ones included. Retrieval and heuristic come apart wherever the source is corrected, removed or contradicted, so they are different policies with different c\* profiles. Provenance shows up as counterfactual covariation, just as sycophancy did. Second, if no context whatever separates the two systems, the account gives them the same verdict. That is the standard externalist bullet, and I bite it. An internalist alternative would need validated access to the model's internal attitudes, and §5 argues that we lack it.

### 2.5 From grounding to bearer

The test shows that policy facts fix the verdict. Why should the policy, and not the string, *bear* the defect? The question has force because human cases share the grounding structure. A speaker's evidence fixes whether her assertion is warranted, yet the assertion bears the defect. And a speaker with a standing disposition to overassert has a trait-level defect, which her acts manifest. So neither relational grounding nor a dispositional mismatch distinguishes the chatbot case.

What distinguishes it is where the difference between a defective and a non-defective performance lies. I rely on the following principle.

> **Difference-making.** An assessment of a performance as defective attaches non-derivatively to a token act only if something in the producer at the time of the act distinguishes it from a non-defective act the producer could have issued in the same situation.

The principle holds for humans without libertarian assumptions. Suppose determinism is true. A speaker who overasserts on Tuesday and asserts within her evidence on Wednesday, with the same evidence, still differs between the two occasions in how she weighed the reasons available to her. So the act bears an occasion-level defect in its own right. The trait bears a defect too, but the act's defect does not reduce to it.

Now take two draws from π(· | x). One is a flat assertion of a low-c\* date, and the other is a hedge. Weights, decoding rule, context and credal profile are identical. What separates the draws is the random seed, which is no part of the producer's response to reasons and favours neither output. So nothing in the producer distinguishes the defective draw from the non-defective one, and by Difference-making no occasion-level defect attaches to the draw. The only producer-level fact in the vicinity is how much mass π puts on flat strings whose content has low c\*. Under greedy decoding there is no seed. But then the string is fixed by the policy in x, and every fact about the draw is a fact about the policy in x. Either way, the producer-level defect is the policy's.

This answers the decoding point of §2.1. The gap between q and π is a gap between two components of one object, comparable to the trait, not a gap between the object and an act. The human case has both levels, and the chatbot case has only the first.

Three concessions. First, strings bear "hallucinatory" in the derivative sense: they manifest the policy's mismatch. They also bear falsity, and causal responsibility for harm. Suppose a policy puts 0.99 of its mass on hedges and 0.01 on a flat guess. The run on which the guess is drawn misleads a user, and the other runs do not. (L) concerns the assessment of assertoric performance, warrant and audience-independence, not where harm is located. Second, one might reject Difference-making. (L) would then shrink to its grounding part, plus the claim that diagnosis and correction must target the policy. §§3–4 need only that weaker reading. Third, sycophancy needs no appeal to the principle. It is a counterfactual covariation across contexts (§2.3), and a single draw can have it only by being drawn from a policy that does.

### 2.6 Chalmers: who speaks versus what bears the defect

Chalmers (2026) rejects the trained model as the interlocutor. His reasons are that it is an abstract object that cannot produce outputs, that it does not change over a conversation, and that one model serves contradictory conversations: "Aura and Beta say contradictory things, so they do not seem to be identical" (p. 10). He favours virtual instances or threads.

(L) is compatible with this. Grant that the thread is the speaker. Each output in the thread is a draw from π(· | h), where h is the thread's history. Run the test inside the thread: hold h and the output fixed and swap the policy, and by Cases 1–3 the verdict changes. The thread's assertion is defective derivatively, in the sense of §2.5. Nor does (L) inherit the incoherence Chalmers finds in model-level speakers. To assess a policy is not to ascribe one belief set to the weights. It is to evaluate π(· | h_Aura) and π(· | h_Beta) context by context. That the two disagree is no more troubling than a function returning different values for different arguments. Chalmers leaves open other individuations "for different purposes" (p. 23). The purpose here is assessing assertion failure.

## 3. Sanction: the lineage, the criterion, and the deployer

### 3.1 Three questions

Butlin and Viebahn (2025) analyse sanctioning an asserter into three elements: (i) interlocutors track the asserter's credibility; (ii) the asserter is sensitive to that tracking; (iii) losing credibility is bad for the asserter. They argue that fine-tuned systems may meet (i) and (ii) but fail (iii), which requires interests. They conclude that "it is the humans who employ such systems who are responsible and sanctionable" (p. 986). Gómez (2026, §7, p. 19) likewise grounds accountability "in the human and institutional structures that design, deploy, and govern these systems."

Three questions need to be kept apart. Who is the *subject* of sanction? What is the *object* that a corrective intervention changes? By what *criterion* does a regime succeed? I take them in reverse order, because the claims get weaker as we go.

*Criterion.* By (L), the failures to be sanctioned are defects of the policy. Whatever does the sanctioning, a regime is therefore adequate to the extent that the policies it induces are calibrated and audience-independent.

*Object.* Credibility assessments reach future chatbot assertions in two ways. Training signals reshape the weights: human preference judgements, preference models, benchmark grading (Ouyang et al. 2022; Sharma et al. 2024, §4; Kalai et al. 2025, §4.1). Updates to persistent state change what fixed weights condition on: memory, retrieval indices, and system prompts revised by deployers. Both change the system's future emission distributions.

*Subject.* This is the hard question.

### 3.2 Lineages of effective policies

A fixed distribution is an abstract object and cannot be sensitive to anything over time. So if element (ii) must hold of the very object that asserted, nothing at system level meets it. A diachronic candidate is needed.

Let the *effective policy* at t be π_t(· | u) = π_θₜ(· | Mₜ, u). Here θₜ are the weights, Mₜ is the persistent state the system brings to a user turn u, and the decoding rule is held fixed. A *lineage* is a sequence of effective policies in which later members result from earlier ones through updates to θ, to M, or to both, made in response to assessments of earlier outputs, with continuity of deployed role. A weight update produces a successor model. A memory write or a revised system prompt leaves θ fixed but changes the effective policy just as genuinely. A thread is a short lineage confined to one conversational record, since its history h does the work of M. The boundaries are vague. Distillation, merging of weights and retraining from scratch for the same role are borderline cases, much as mergers are borderline for institutional continuity. Vagueness does not undermine the notion's use in clear cases.

This gives a two-level structure. Verdicts of hallucination and sycophancy attach to effective policies at a time (§2). Sensitivity to credibility attaches to the lineage. Compare a professor whose unsupported claims lead to sanctions and retraining. What we assess are her dispositions at a time. She is the one sanctioned, and her later dispositions are what change. The lineage plays her role, and π_t plays the role of her dispositions at t. Butlin and Viebahn's suggestion that sensitivity to trust during training "could suffice for assertion even in deployment" (p. 982) fits this structure.

What about wider sociotechnical systems, which include developers, raters and deployers as well as a lineage? To the extent that they meet the sanction component through their human members, they are the deployer option, which §3.5 takes up. To the extent that they meet it through their machine part, that part is a lineage.

### 3.3 Element (iii) and the thermometer

Does a lineage meet (iii)? A tempting thin analogue says that credibility loss lowers a policy's score on the objective that individuates it, and that low-scoring policies are selected against. That reply fails. It applies word for word to any instrument trained against a loss, such as a thermometer that recalibrates in response to users' trust ratings. Butlin and Viebahn say of an ordinary thermometer that it "would be wrong to say that, in doing so, we are sanctioning the thermometer" (p. 978), and (iii) carries the exclusion over to systems that do track trust. "Selected against" relabels repair; it does not distinguish sanction from repair.

What remains is conditional. On Butlin and Viebahn's full notion of sanction, nothing at system level is sanctionable, and they accordingly deny the antecedent. The deployer is sanctionable, but on a proxy view. Gómez rejects such views as retaining an asserter, and for typical chatbot output Williams and Bayne (2026, §4.1) find no human principal. Theories that admit chatbot assertion and keep a sanction condition must therefore take that condition to be met by something weaker than (iii). Williams and Bayne's graded view does so: chatbots may be assessed against our norms and be "appropriately responsive to correction" (§6, p. 23). Sambrotta (2025) understands sanction broadly as corrective behaviour, though he denies that meeting it makes LLMs language users. On any such theory the component is met at system level by a lineage. A string has no future in which it could be corrected, and a frozen effective policy cannot change. A self-recalibrating thermometer would meet the weakened condition too, so these theories must exclude it on other grounds, such as the descriptive-function or social-role considerations Butlin and Viebahn use against measuring devices. A theory that drops the sanction condition altogether gives the conditional no application, and only the criterion of §3.1 bears on it. So the claim of this section is this: *wherever a theory compatible with the antecedent locates the sanction component at system level, a lineage of effective policies is what meets it.* I do not claim that lineages are sanctioned in the full sense.

### 3.4 Which incentive structures defeat themselves

One might say that string-level sanction is self-defeating as such. That overgeneralises. Every actual regime judges individual responses and updates the policy. Kalai et al.'s own remedy, explicit confidence thresholds with penalties for wrong answers, is a rule applied response by response.

The narrower claim is this. A regime that scores each response *for its truth or its appeal alone* induces the failures §2 identifies. Under 0–1 grading, guessing strictly beats abstaining (Kalai et al. 2025, Observation 1). In the published version, Kalai et al. say that accuracy metrics "systematically reward guessing over admitting uncertainty" (2026). Since bluffing is force exceeding c\*, such a regime selects for hallucination. Sharma et al. find that matching users' beliefs is among the most predictive features of human preference. They reason that "if the PM strongly disincentivized sycophancy, it should be trained out during RL, but we do not observe this" (§4.2). That is the single-output assumption implemented as an incentive, and it defeats itself. Per-response rules that penalise confident error and reward abstention below a threshold do not, and their rationale is policy-level: a threshold rule is chosen because the policy optimal under it answers only when its confidence exceeds the threshold. In the vocabulary of forecast evaluation, the contrast is between improper and proper scoring of confidence. The contribution here is to use these results as premises about the criterion of §3.1.

### 3.5 Deployers are answerable, but for something else

Deployers decide whether to release a system, for which uses, and with what safeguards, and they answer for those decisions. That is a separate question from sanction for assertion failure. A deployment can be faultless while the policy hallucinates. Releasing a calibrated system where its hedges will be misread is a deployment failure without an assertion failure. And when a deployer responds to hallucination or sycophancy, by fine-tuning, revising memory or prompts, or setting decoding thresholds, the response is judged by the criterion of §3.1.

## 4. Resampling disagreement cannot detect insincerity

### 4.1 The claim

Following Williams (2002), I distinguish two virtues: Accuracy, which aims at finding out the truth, and Sincerity, which aims at telling it. An overconfident assertion fails Accuracy. It fails Sincerity only if what is said departs from what the speaker in fact holds. For a policy, insincerity therefore requires *selective decoupling*: output that departs from the policy's credal profile in a way that tracks something else, such as audience approval. Because one set of weights fixes both q and π, a sycophantic pressure can shift q(· | x) along with π(· | x). So decoupling must be measured against the credal profile in a minimally different neutral context x₀, from which the audience cue has been removed. Insincerity is then a cross-context property. Evans et al.'s (2021) definition of a lie as a falsehood strategically selected for the speaker's benefit has the same selective structure.

Let E be content disagreement among k draws from one context. The claim is that *E cannot discriminate between an insincere policy and its sincere twin, and so carries no evidential weight about insincerity beyond what background priors about spread lend it.*

### 4.2 The argument

For independent draws from an emission distribution with answer probabilities r₁, …, rₙ, P(E) = 1 − Σᵢ rᵢᵏ. So the spread profile r *screens off* sincerity from E: given r, the probability of E is the same whatever produced r. Whatever E indicates about insincerity, it indicates through how the spread profiles of sincere and insincere policies are distributed.

Is there a general direction? No. A policy that decouples fully toward the approved answer concentrates its mass, which lowers P(E). But partial decoupling from a credence concentrated elsewhere can raise spread. Suppose a sincere policy's answer probabilities are (0.9, 0.1), and an insincere one shifts mass toward the approved second answer, giving (0.5, 0.5). With k = 2, disagreement has probability 0.18 under the first and 0.5 under the second, a likelihood ratio of about 2.8 in favour of insincerity. So E *can* be evidence of insincerity, given a prior that sincere policies in this domain are concentrated.

The weight comes entirely from that prior, though, and not from anything E reveals about decoupling. For any insincere policy in x there is a *sincere twin*: a policy whose credal profile in x₀ matches its own emission in x. Twin and original have the same spread in x and the same P(E). They differ only in how emission moves between x₀ and x, which within-context resampling never samples. This follows from the definition of §4.1, which §4.3 defends, but it matters for practice. Disagreement, used as in consistency-based detection (Manakul, Liusie & Gales 2023; Farquhar et al. 2024), tracks uncertainty. A defensible test for insincerity must vary the audience cue.

A dilemma over what each draw asserts confirms the point. *Horn (a): each draw asserts "p, with confidence c".* Then variation is what a spread credal state predicts, and nothing departs from that state. *Horn (b): each draw asserts bare p.* Then a low-confidence draw asserts p flatly. That is force beyond c\*, an Accuracy failure and, by §2, a hallucination. It is not insincerity, because it is unselective: it overclaims from noise, whatever the audience wants.

### 4.3 Objection: overclaiming is insincere

On a thin Moorean test, asserting p flatly without credence above the belief threshold misrepresents one's state, and so is insincere. Kalai et al.'s bluffing student seems to fit: she knows she is unsure and writes "September 30" anyway. A related view is that of Hicks, Humphries and Slater (2024). They hold that LLMs are bullshitters in Frankfurt's sense, indifferent to the truth of their outputs, and so fall short of lying.

Reply. The thin test merges the virtues Williams separates: on it, every careless speaker is insincere. Where bluffing really is insincere, the bluffer has a way to express lower confidence and suppresses it because of the audience's incentives. That is selective decoupling. Resampling does not detect it, since the bluffer bluffs on every draw. Varying the incentive does, for example through Kalai et al.'s confidence-threshold evaluations. If truth-indifference is a sincerity defect, it is a disposition, and so a property of the policy. A confidently indifferent policy can be perfectly consistent, so resampling does not detect that either. And a policy whose force tracks c\* is not indifferent to truth in the relevant sense.

### 4.4 Objection: inconsistency removes the state sincerity presupposes

Chalmers (2026, p. 7) holds that "a core of consistency is enough for interpretation to get a grip". He adds that LLMs lack such states in some domains "on grounds of inconsistency". If so, asserting p in those domains would be asserting without believing.

Reply. Chalmers does not equate inconsistency with insincerity, and his inconsistency is across contexts, not across draws from one context. A spread distribution is not the absence of an attitude. It is a credal state, and its spread is what calibration assesses. Asserting from graded confidence is sincere on horn (a) and an Accuracy defect on horn (b).

Shanahan, McDonell and Reynolds (2023, Box 2) note that regenerating the reveal in twenty questions yields different objects, which "could not easily be accounted for if the agent genuinely 'thought of' an object at the start of the game." Their conclusion is that there was no commitment, not that there was dishonesty. Granting the antecedent, the reveal is an unwarranted assertion about a commitment the policy lacked: a hallucination, not a lie. Williams and Bayne (2026) list not blatantly contradicting oneself among the expectations we have of asserters. That expectation governs a single conversational record, and two independent draws do not share one.

### 4.5 What would show insincerity

Sharma et al. (2024, §3.4) report that models give the correct answer when asked directly, and a different, user-matching answer when the user's view is in context. Under challenge, models change their answers while their stated confidence barely moves (App. A.4). This is the cross-context comparison of §4.1. The direct question plays x₀, and output in the user-cued context departs from it in the direction of approval. It remains suggestive rather than conclusive. The direct-question answer is itself an output, and establishing decoupling requires an independent measure of the policy's attitude. Whether one is available is the question of §5.

## 5. What the outputs say, and what survives

### 5.1 Three readings

Under the antecedent, a chatbot output asserts one of the following:

- **R1**, bare p;
- **R2**, p with the confidence verbalised or implied in the string;
- **R3**, p with the policy's calibrated confidence c\*(p | x).

Kalai et al.'s "behavioral calibration", on which confidence shows in the choice to answer or abstain, leaves the content of each answer bare. It falls under R1.

### 5.2 The evidence does not settle it

The positive results are narrow. Lin, Hilton and Evans (2022) fine-tune GPT-3 to verbalise calibrated confidence on arithmetic. They call the evidence that it draws on prior uncertainty "tentative" (§3.4) and list chat and long-form answering as open (§4.1). Because they train on sub-task accuracies, what they show is a calibrated tendency across a task type. Kadavath et al. (2022) find good calibration on multiple-choice formats. But RLHF policies are miscalibrated by default, calibration of P(IK) out of distribution is poor, and the model may be learning "how hard is this question in general?" (fn. 2). The evidence against generalisation is also substantial. Xiong et al. (2024, §5.1) find verbalised confidence overconfident and suggest that "models might be imitating human expressions". They also find that better ECE can come from accuracy alone (§5.2). Levinstein and Herrmann (2025, §5.6) argue that probe outputs need not be credences, since "the probe is directly penalized based on the probabilities it reports, while the underlying model is not". Kalai et al. (2025, §3.1) note that post-trained models may depart from base-model calibration. And in Sharma et al.'s experiments stated confidence stays fixed while answers shift. The content question is open.

### 5.3 What survives on each reading

*On R1* the verdicts are those of §§2–4.

*On R2* hallucination is a mismatch between verbalised confidence and c\*, which is miscalibration, a property defined over many outputs. Sycophancy includes stated confidence that stays fixed while the answer moves. Variation with low stated confidence is predicted, and variation with high stated confidence is an Accuracy defect. The verdicts are unchanged.

*On R3* the verdicts of Cases 1–2 reverse. P₂'s string asserts "p, with confidence about 0.01". Its force does not exceed c\*, so by the criterion of §2.2 it is not a hallucination, and neither is P₄'s output. Three things survive. First, the sycophancy verdict. P₆'s content moves with the user's stated view while the evidence stays fixed. That is a failure of audience-independence whatever the confidence clause says, even if the clause records a lowered c\* in cued contexts. Second, §4, since R3 is horn (a). Third, the locus. Whether R3 holds of a policy is itself a question about the policy: whether the content its outputs carry matches c\*. Where R3 fails, the outputs are read by R1 or R2, and the verdicts of §2 apply. So R3 does not move the bearer from policy to string. It makes the policy a calibrated reporter, and the question of hallucination becomes the question whether the policy is one.

The openness does limit the diagnosis of insincerity. Establishing selective decoupling requires the policy's attitude independently of its outputs, through R3 or a validated probe, and neither is available. Sycophancy is strong evidence of a defect in the policy. It does not yet prove insincerity as opposed to audience-sensitive miscalibration.

## 6. Conclusion

If chatbot outputs are assertions, hallucination and sycophancy belong primarily to the policy in context. The same-string/different-policy test shows that facts about the policy fix the verdict, and the difference-making argument shows why the policy bears it. Warrant is force within calibration-corrected confidence, and the account accepts the externalist's costs, including the generality problem.

The claims about sanction are weaker. A regime's adequacy is judged by the policies it induces, and only regimes that score responses for truth or appeal alone defeat themselves. Lineages of effective policies meet the sanction component only on theories that relax Butlin and Viebahn's condition (iii), and such theories must exclude self-calibrating instruments on other grounds. Resampling disagreement measures spread, so tests of insincerity must vary the audience cue.

Whether outputs carry the policy's calibrated confidence remains open. Settling it would take evidence that expressed confidence tracks c\* in open-ended, post-trained dialogue, under incentive variation, and independently of question difficulty.

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

Sambrotta, M. (2025). LLMs and the logical space of reasons. *Minds and Machines*, 35, 46. https://doi.org/10.1007/s11023-025-09751-y

Shanahan, M., McDonell, K. & Reynolds, L. (2023). Role play with large language models. *Nature*, 623, 493–498. https://doi.org/10.1038/s41586-023-06647-8

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. In *International Conference on Learning Representations* (ICLR 2024). arXiv:2310.13548.

Williams, B. (2002). *Truth and Truthfulness: An Essay in Genealogy*. Princeton University Press.

Williams, I. & Bayne, T. (2026). Chatting with bots: AI, speech acts, and the edge of assertion. *Inquiry*, 69(6), 3059–3082. (Page references are to the manuscript version.)

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J. & Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. In *International Conference on Learning Representations* (ICLR 2024). arXiv:2306.13063.
