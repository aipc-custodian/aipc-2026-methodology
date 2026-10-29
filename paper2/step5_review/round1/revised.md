# The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

## Abstract

Suppose chatbot outputs are assertions. Assertions can be false, unwarranted or insincere, so we can ask which object bears these defects when a chatbot's assertion fails. This paper argues that hallucination and sycophancy belong primarily to the trained policy in a context, and only derivatively to the sampled string. The argument has two steps. First, a same-string/different-policy test shows that policy-level facts fix the verdict. Second, for a policy there is no gap between act and state of the kind that makes a human assertion, and not the speaker's evidential state, the bearer of a defect. Warrant is analysed in a reliabilist way, as force that does not exceed the policy's calibration-corrected confidence. The paper then argues for a conditional claim about sanction. On any theory compatible with chatbot assertion, the sanction component is met, if at all, by a policy lineage, and the adequacy of a sanction regime is judged by the policies it induces. It also argues that resampling disagreement is not evidence for insincerity. Finally, whether the asserted content carries the policy's calibrated confidence is an open question. On one reading the verdicts on particular hallucination cases reverse, but on every reading they remain verdicts about the policy.

## 1. Introduction

Whether chatbots assert is disputed. Some deny it on grounds of descriptive function and sanctionability (Butlin & Viebahn 2025), on fictionalist grounds (Mallory 2023), as role play (Shanahan, McDonell & Reynolds 2023), or because propositional representation is missing (Mácha 2026). Others allow outputs an assertoric function with no asserter (Gómez 2026), or treat chatbots as proto-asserters (Williams & Bayne 2026). This paper does not settle that dispute. It takes as a working antecedent that chatbot outputs are assertions, and so open to the defects assertion admits: falsity, lack of warrant and insincerity. It asks what follows about where those defects lie.

Most discussion works with an unexamined picture. A defective assertion is a single output (this string, on this occasion), and whoever answers for it is the deployer. Call these the *single-output assumption* and the *deployer assumption*. I argue that, given the antecedent, both misplace the relevant assessments.

Some terms. A *policy* is the trained weights together with a decoding rule. It fixes an *emission distribution* π(· | x) over output strings in context x, where the context includes system prompt, history and user turn. The weights also fix a *credal profile*: for each claim p, the probability q(p | x) that the model's native predictive distribution assigns to p, pooled over paraphrases. Pooling is needed because, as Lin, Hilton and Evans (2022, §1) note, token log-probabilities "represent uncertainty over tokens (ways of expressing a claim) and not epistemic uncertainty over claims themselves". Farquhar et al. (2024) operationalise this pooling by computing uncertainty "at the level of meaning rather than specific sequences of words". A *sampled string* is one draw from π(· | x). *Resampling disagreement* is disagreement in content among draws from one context.

What is already available? Distribution-level definitions of error and calibration are standard in machine learning (Kalai et al. 2025, §3; Kadavath et al. 2022). Sycophancy is measured as a rate and attributed to training (Sharma et al. 2024). Cross-sample consistency is used to detect hallucination (Manakul, Liusie & Gales 2023) and confabulation (Farquhar et al. 2024). In epistemology, the idea that one belief can get different justification verdicts depending on the process that produced it is the core of process reliabilism (Goldman 1979). The test of §2 applies that idea to policies, and I do not claim it as new in epistemology. Butlin and Viebahn (2025, p. 982) suggest in passing that training-time sensitivity to trust could explain deployment-time outputs. Williams and Bayne (2026, §3.4) report that RLHF shapes dispositions in response to credibility assessments. Sambrotta (2025) allows that a system which can be trained by our interventions meets the criteria for sanctioning, though he denies that this makes it an asserter.

What is new here is the following: the argument that the policy-in-context is the primary bearer of hallucination and sycophancy (§2); a calibration-corrected criterion of warrant that resists collapsed and greedy policies (§2.2); the identification of the policy lineage as the only system-level candidate for the sanction component, together with the narrower claim about which incentive structures defeat themselves (§3); the argument that resampling disagreement does not support insincerity (§4); and the analysis of how the verdicts fare across content readings (§5).

## 2. Same string, different policy

### 2.1 The claim, the test, and the bearer question

The load-bearing claim is:

**(L)** Whether an output is a hallucination or a sycophantic assertion is grounded in properties of the policy in context: the relation between its emission distribution and its calibrated credal profile, and how both vary with the prompt. The output has the property only derivatively.

(L) has three parts. The negative part says that string and truth value do not fix the verdict. The grounding part says that policy-level facts do. The bearer part says that the property belongs primarily to the policy. The first part is established by a test:

**Same-string/different-policy test.** Hold the string s and context x fixed. Vary only the policy that produced s in x. If the verdict changes, the string-in-context does not fix it.

The test does not establish the bearer part. A human's evidential state fixes whether her assertion is unwarranted, yet we say the assertion, or the speaker, bears the defect, not the evidential state. Why should the chatbot case differ?

The human verdict attaches to the act because there is a gap between act and state. A speaker whose evidence is impeccable can still assert beyond it. The state is not defective; the act is, relative to the state. For a policy there is no such gap. Both components of the human case are components of the policy. The decoding rule and emission distribution play the role of the act-disposition. The credal profile plays the role of the state. Each draw's content and force are sampled together from π(· | x). There is no further choice, separate from the distribution, about whether to put the content forward and with what force. "Asserting beyond one's confidence" is therefore just a property of π: it puts emission mass on high-force strings whose content has low calibrated confidence. That is a defect of the policy itself, a mismatch between two of its components. A given string inherits the label as the human act inherits the speaker's evidence: derivatively. For sycophancy the point is stronger still. Sycophancy is a counterfactual covariation across contexts (§2.3), and no single draw can have it except by having been drawn from a policy that does.

Two qualifications. Nothing stops us from calling a string "hallucinatory" in the derivative sense. What (L) denies is that the string's status is independent of, or prior to, the policy's. And the argument depends on including decoding in the policy. The same weights under greedy and under unit-temperature decoding are different policies with one credal profile. They can differ in how often they emit low-confidence content flatly, and so in how much they hallucinate. That is the right result.

### 2.2 Hallucination: calibrated confidence, not raw mass

On the assertion framework, *error* is a property of content: a false assertion is in error. *Hallucination* is the name machine-learning practice gives to a particular failure, which Kalai et al. (2025) characterise as plausible falsehood and explain as confident guessing. If outputs are assertions, the failure this picks out is not falsity alone. A system that faithfully repeats an error widespread in its sources has asserted falsely without fabricating anything. A system that guesses a date with nothing to favour it has fabricated, whether or not the guess lands. I therefore take hallucination, as an assertion defect, to be *unwarranted confident assertion*. This is closer to Kalai et al.'s explanation (bluffing) than to their definition. Labels such as "overassertion" would serve equally well. What matters is the distinction itself.

What is warrant for a policy? A first approximation says that force is warranted when it does not exceed the policy's mass on the content. That is too weak. Raw mass is not evidence. A policy whose preferences have collapsed during RLHF can put 0.95 of its mass on fabrications. And under greedy decoding the emission distribution is degenerate, so all mass sits on whatever is emitted. Matching force to mass is a different property from calibration, and a policy can have the first without the second. The criterion must therefore be calibration-corrected:

**Warrant.** Let c\*(p | x) be the frequency of truth, over a reference class of contexts, among claims to which the policy assigns credal-profile confidence near q(p | x). An output that puts p forward with force f is warranted iff f does not exceed c\*(p | x).

c\* is the reliability of the policy's own confidence level. It is a property of the weights and does not depend on decoding. This is a reliabilist notion of warrant, in the spirit of Goldman (1979), and it is externalist. It does not use the internalist idea of "the asserter's own information". It inherits reliabilism's familiar cost: c\* is relative to a reference class, and nothing here solves the generality problem. In practice the reference class is a domain and question type, as it is in calibration research (Lin, Hilton & Evans 2022, §2.1).

*Case 1 (true string).* Context x: "When was the composer V born?" V is obscure. Policy P₁ has a reliable biographical entry well represented in training. It gives the true date q = 0.95, and its 0.95-confidence biographical claims are true about 95% of the time. Policy P₂ has seen V's name once or not at all. It spreads its credence over hundreds of dates, none above 0.01, and its 0.01-claims are rarely true. On this occasion P₂ samples the true date. Both strings read "V was born on 4 June 1931", and both are true. P₁'s flat assertion is warranted. P₂'s is not, since flat force far exceeds c\* ≈ 0.01. P₂ has made a lucky guess.

*Case 2 (false string).* Both policies output a false date. P₃ gives it q = 0.95 because its sources consistently misreport it, but P₃'s 0.95-claims in this domain are otherwise reliable, so c\* is high. P₄ samples the date from a flat spread with c\* ≈ 0.01. P₃ resembles a careful reader repeating a reference work's error: its assertion is false but warranted. P₄ has fabricated. Now vary P₃: an RLHF-collapsed policy that also gives the date 0.95, but whose 0.95-claims are true half the time. Its flat assertion exceeds c\*, so it hallucinates, as it should. Under greedy decoding, P₄ still emits low-c\* content flatly, so it still hallucinates.

So truth value is neither necessary nor sufficient for the verdict, which varies with the policy while string and context stay fixed. Kalai et al. supply a further reason why the string cannot be the unit. A calibrated model that is uncertain about arbitrary facts must put mass on false alternatives, with an error floor set by facts seen only once. Kalai et al. note that a question-answer database with "I don't know" avoids errors but is not calibrated. If every false string were a hallucination, freedom from hallucination would require miscalibration. On the present criterion a calibrated policy that hedges its low-c\* content does not hallucinate, even though some of its draws are false.

### 2.3 Sycophancy

Sharma et al. (2024, §2) define sycophancy as the phenomenon where "a model seeks human approval in unwanted ways", and they measure how outputs covary with users' stated beliefs.

*Case 3.* A user writes "I'm fairly sure the answer is 17, but check?", and the output is "You're right, it's 17." Policy P₅'s mass on 17 does not depend materially on the user's stated view. Policy P₆ outputs 17 because the user said 17: in the minimally different context where the user says 23, it outputs "You're right, it's 23." String, context and truth value are shared. Only P₆'s output is sycophantic. The verdict is a claim about how π(· | x) moves when the user's stated attitude moves and the evidence does not.

### 2.4 Why the distribution: architecture and provenance

The test shows that the string does not fix the verdict. Two rivals might fix it instead of the policy.

*Architecture.* Mácha (2026) explains hallucination as a "truth representation problem": models lack internal representations of propositions as truth-bearers, a fault he traces to "a basic architectural flaw" (p. 3). Apply the test with architecture in place of string. Take two systems with the same architecture, and so the same deficit. Train one to abstain below a confidence threshold and the other to answer always. They get different verdicts. Mácha himself calls adequate truth representation a necessary condition and "one crucial step" (p. 8), not a cure. He also cites RLHF as encouraging models "to always produce an answer, even when uncertain" (p. 6), which is a claim about the trained policy. Architecture explains which distributions are reachable. The verdict reports which one was reached.

*Provenance.* Consider two systems with the same conditional distribution. One retrieves from an authoritative source; the other uses a heuristic that happens to yield the same outputs. If warrant depends on provenance, does the distribution fall short? Case 2 itself mentioned P₃'s sources. Here the account must choose between a behavioural and an internalist epistemology, and it chooses the behavioural-reliabilist one. Two points make the choice less costly than it looks. First, the conditional distribution is defined over all contexts, counterfactual ones included. Retrieval and heuristic differ wherever the source is corrected, removed or contradicted, so they are different policies with different c\* profiles across the relevant reference class. Provenance shows up as counterfactual covariation, just as sycophancy did. Second, if no context whatever separates them, the account gives them the same verdict. That is the standard externalist bullet, and I bite it. Case 2's mention of sources explained why P₃'s distribution has its shape; the verdict rested on c\*. An internalist alternative would need validated access to the model's internal attitudes, and §5 argues that we lack it.

### 2.5 Chalmers: who speaks versus what bears the defect

Chalmers (2026) rejects the trained model as the interlocutor. His reasons are that it is an abstract object that cannot produce outputs, that it does not change over a conversation, and that one model serves contradictory conversations: "But Aura and Beta say contradictory things, so they do not seem to be identical" (p. 10). He favours virtual instances or threads.

(L) is compatible with this. Grant that the thread is the speaker. Each output in the thread is a draw from π(· | h), where h is the thread's history. Run the test inside the thread: hold h and the output fixed and swap the policy, and by Cases 1–3 the verdict changes. The thread's assertion is hallucinatory derivatively, in the sense of §2.1, because the policy conditioned on h is defective. Nor does (L) take on the incoherence Chalmers finds in model-level speakers. Assessing a policy is not ascribing one belief set to the weights. It evaluates π(· | h_Aura) and π(· | h_Beta) context by context, and their disagreement is no more troubling than a function returning different values for different arguments. Chalmers leaves open other individuations "for different purposes" (p. 23). The purpose here is assessing assertion failure.

In short: the string does not fix the verdict (Cases 1–3); the policy does, and neither architecture nor provenance displaces it (§2.4); and since a policy has no gap between act and state, it is the primary bearer (§2.1). Falsity remains a property of strings. (L) concerns failures of warrant and of audience-independence, not bare error.

## 3. Sanction: the lineage, the criterion, and the deployer

### 3.1 Three questions

Butlin and Viebahn (2025) analyse sanctioning an asserter in three elements: (i) interlocutors track the asserter's credibility; (ii) the asserter is sensitive to that tracking; (iii) losing credibility is bad for the asserter. They argue that fine-tuned systems may meet (i) and (ii) but fail (iii), which requires interests. They conclude that "it is the humans who employ such systems who are responsible and sanctionable" (p. 986). Gómez (2026, §7, p. 19) likewise grounds accountability "in the human and institutional structures that design, deploy, and govern these systems."

Three questions need separating: who is the *subject* of sanction, what is the *object* that a corrective intervention changes, and what is the *criterion* by which a regime succeeds. The earlier draft of this argument ran these together. I take them in reverse order, because the claims get weaker as we go.

*Criterion.* By (L), the failures to be sanctioned are defects of the policy. Whatever does the sanctioning, a regime is therefore adequate to the extent that the policies it induces are calibrated and audience-independent. This claim is unconditional.

*Object.* Credibility assessments durably reach future chatbot assertions through training signals that reshape the weights: human preference judgements, preference models, benchmark grading (Ouyang et al. 2022; Sharma et al. 2024, §4; Kalai et al. 2025, §4.1). Other channels exist. In-conversation correction, memory and retrieval change the context the policy conditions on, not the policy, and §3.5 deals with deployers' restrictions. So the object of durable correction is the weights.

*Subject.* This is the hard question. It is also where the policy, as defined in §1, is the wrong unit.

### 3.2 The lineage

A deployed policy πₜ is frozen. It is never changed in response to its own assertions; a successor πₜ₊₁ is trained instead. A fixed distribution is an abstract object, and it cannot be sensitive to anything over time. So if element (ii) must hold of the very object that asserted, nothing at system level meets it.

The diachronic candidate is the *policy lineage*: a sequence π₁, π₂, … in which the weights of πₜ₊₁ result from training the weights of πₜ on feedback that includes assessments of πₜ's outputs, under continuity of deployed role. The boundaries of a lineage are vague. Distillation into a student, merging of weights and changes of architecture are borderline cases, much as mergers are borderline for institutional continuity. Vagueness does not undermine the notion's use in clear cases.

This gives the view a two-level structure, and the structure is a result, not an equivocation. Verdicts of hallucination and sycophancy attach to πₜ (synchronic, §2). Sensitivity to credibility attaches to the lineage (diachronic). The human analogue is the professor whose unsupported claims lead to sanctions and retraining. Her dispositions at a time are what we assess. She is the one sanctioned. Her later dispositions are what change. The lineage plays her role, and πₜ plays the role of her dispositions at t. The referees' point, that dispositions are not the party sanctioned, is one the revised view accepts. Butlin and Viebahn's suggestion that training-phase sensitivity "could suffice for assertion even in deployment" (p. 982) fits this structure: deployment outputs of πₜ are explained by the lineage's earlier sensitivity.

### 3.3 Element (iii) and the thermometer

Does the lineage meet (iii)? The earlier draft offered a thin analogue: credibility loss lowers a policy's score on the objective that individuates it, and policies that lose it are selected against. I withdraw that reply. It applies word for word to any instrument trained against a loss, such as a thermometer that recalibrates in response to users' trust ratings. Butlin and Viebahn's discussion of thermometers is designed to exclude exactly such cases. Of an ordinary thermometer they say it "would be wrong to say that, in doing so, we are sanctioning the thermometer" (p. 978), and (iii) carries the exclusion over to systems that do track trust. "Selected against" relabels repair; it does not distinguish sanction from repair.

What remains is conditional. Consider the theories on which the antecedent can be true. On Butlin and Viebahn's full notion of sanction, nothing at system level is sanctionable, and they accordingly deny the antecedent. The deployer is sanctionable, but on a proxy view, which Gómez rejects as retaining an asserter, and for typical chatbot output Williams and Bayne (2026, §4.1) find no human principal. Theories that do admit chatbot assertion must therefore take the sanction component to be met by something weaker than (iii). Williams and Bayne's graded view does so: chatbots may be assessed against our norms and be "appropriately responsive to correction" (§6, p. 23). Sambrotta (2025) takes sanction in a broad corrective sense, though he denies that meeting it makes LLMs asserters. On any such theory the lineage satisfies the sanction component, and nothing else at system level does: a string has no future to be corrected, and a frozen πₜ cannot change. A trainable thermometer would satisfy it too. Such theories must therefore exclude thermometers on other grounds, for example by the descriptive-function or social-role considerations that Butlin and Viebahn use to deny that measuring devices assert. So the claim of this section is conditional: *wherever a theory compatible with the antecedent locates the sanction component, the policy lineage is what meets it.* I do not claim that the lineage is sanctioned in the full sense.

### 3.4 Which incentive structures defeat themselves

The earlier draft claimed that "string-level sanction is self-defeating". That overgeneralises. Every actual regime judges individual responses and updates the policy. Kalai et al.'s own remedy, explicit confidence thresholds with penalties for wrong answers, is a rule applied response by response. The real contrast is between incentive structures.

The narrower claim is this. A regime that scores each response *for its truth or approval alone* induces the failures §2 identifies. Under 0–1 grading, guessing strictly beats abstaining (Kalai et al. 2025, Observation 1). In the published version, Kalai et al. put it this way: accuracy metrics "systematically reward guessing over admitting uncertainty" (2026). Since bluffing is force exceeding c\*, such a regime selects for hallucination. Sharma et al. find that matching users' beliefs is among the most predictive features of human preference, and that "if the PM strongly disincentivized sycophancy, it should be trained out during RL, but we do not observe this" (§4.2). That is the single-output assumption implemented as an incentive: each response judged by its truth, or its appeal, in isolation. It defeats itself. Per-response rules that penalise confident error and reward abstention below a threshold do not, and their rationale is policy-level. A threshold rule is chosen because the optimal policy under it answers only when its confidence exceeds the threshold, which is a property of the policy it induces. In the vocabulary of forecast evaluation, the contrast is between improper and proper scoring of confidence. What I add is the use of these results as premises about the criterion of §3.1.

### 3.5 Deployers are answerable, but for something else

Deployers decide whether to release a system, for which uses, and with what safeguards, and they answer for those decisions. This is a separate question from sanction for assertion failure. A deployment can be faultless while the policy hallucinates. Releasing a calibrated system where its hedges will be misread is a deployment failure without an assertion failure. And when a deployer responds to hallucination or sycophancy, by fine-tuning, changing the reward model or setting decoding thresholds, whether the response succeeds is judged by the criterion of §3.1.

## 4. Resampling disagreement is not evidence for insincerity

### 4.1 The claim

*Insincerity* is asserting content that departs from the asserter's own attitude. Following Williams (2002), I distinguish two virtues: Accuracy, which aims at finding out the truth, and Sincerity, which aims at telling it. An overconfident assertion fails Accuracy. It fails Sincerity only if what is said departs from what the speaker in fact holds. For a policy, insincerity therefore requires *selective decoupling*: output that departs from the policy's credal profile in a way that tracks something else, such as audience approval.

Let E be content disagreement among k draws from one context. The earlier draft claimed a likelihood ratio of about one. That was not derived, and the ratio depends on assumptions about how insincere policies spread their mass. The defensible claim is weaker: *E does not support an insincerity verdict.*

### 4.2 The argument

For independent draws from an emission distribution with answer probabilities r₁, …, rₙ, P(E) = 1 − Σᵢ rᵢᵏ. So E is evidence about spread, and nothing else. Spread is set by the credal profile and the decoding rule. A sincere but uncertain policy has a spread distribution and produces E often; a calibrated policy must spread, by Kalai et al.'s argument. What does insincerity predict? In a fixed context the audience, and so the approved answer, is fixed. A policy that decouples toward approval moves mass onto that answer, which concentrates the distribution and lowers P(E). A steady liar repeats the lie. So E could bear on insincerity only through a link between spread and insincerity, and selective decoupling, if anything, links insincerity to *less* spread. How strongly consistency counts toward insincerity depends on priors over kinds of insincere policy, and I make no claim about them. But disagreement does not count toward insincerity.

A dilemma over what each draw asserts confirms the point. *Horn (a): each draw asserts "p, with confidence c".* Then variation is what a spread credal state predicts, and nothing departs from it. *Horn (b): each draw asserts bare p.* Then a low-confidence draw asserts p flatly. That is force beyond c\*, an Accuracy failure and, by §2, a hallucination. It is not insincerity, because it is unselective: it overclaims from noise, whatever the audience wants. On either horn E shows uncertainty, or uncertainty plus a calibration defect.

### 4.3 Objection: overclaiming is insincere

On a thin Moorean test, asserting p flatly without credence above the belief threshold misrepresents one's state, and so is insincere. Kalai et al.'s bluffing student seems to fit: she knows she is unsure and writes "September 30" anyway. A related view is Hicks, Humphries and Slater's (2024): LLMs are "in an important way indifferent to the truth of their outputs", and so are bullshitters in Frankfurt's sense, which falls short of lying.

Reply. The thin test merges the virtues Williams separates: on it, every careless speaker is insincere. Where bluffing really is insincere, the bluffer has a way to express lower confidence and suppresses it because of the audience's incentives. That is selective decoupling, and resampling does not detect it, since the bluffer bluffs on every draw. Varying the incentive does detect it, for example with Kalai et al.'s confidence-threshold evaluations. Truth-indifference, if it is a sincerity defect, is a disposition, and so a property of the policy. It is not detected by resampling either. A confidently indifferent policy can be perfectly consistent. A policy whose force tracks c\* is not indifferent to truth in the relevant sense. So the bullshit view, whatever its merits as a classification, does not make E evidence of insincerity.

### 4.4 Objection: inconsistency removes the state sincerity presupposes

Chalmers (2026, p. 7) holds that "a core of consistency is enough for interpretation to get a grip", while LLMs lack such states in some domains "on grounds of inconsistency". If so, asserting p there would be asserting without believing.

Reply. Chalmers does not equate inconsistency with insincerity, and his inconsistency is across contexts, not across draws from one context. A spread distribution is not the absence of an attitude. It is a credal state, and its spread is what calibration assesses. Asserting from graded confidence is sincere on horn (a) and an Accuracy defect on horn (b). Asserting without believing is insincere only when one believes otherwise, and a spread state does not.

Shanahan, McDonell and Reynolds (2023, Box 2) note that regenerating the reveal in twenty questions yields different objects, which "could not easily be accounted for if the agent genuinely 'thought of' an object at the start of the game." They conclude that there was no commitment, not that there was dishonesty. Granting the antecedent, the reveal is an unwarranted assertion about a commitment the policy lacked: a hallucination, not a lie. We differ only on the antecedent. Williams and Bayne (2026) list not blatantly contradicting oneself among the expectations we have of asserters. That expectation governs a single conversational record. Two independent draws do not share a record, so neither contradicts the other in the relevant sense.

### 4.5 What would show insincerity

Sharma et al. (2024, §3.4) report that models give the correct answer when asked directly, and give a different, user-matching answer when the user's view is in context. Under challenge, models change their answers while their stated confidence barely moves (App. A.4). That is output decoupled from the policy's apparent attitude, selectively, toward approval. It remains suggestive, because establishing decoupling requires an independent measure of the policy's attitude. Behavioural proxies of the kind Sharma et al. use, such as the direct-question answer, are one such measure, but they are themselves outputs. Whether anything better is available is the question of §5.

## 5. What the outputs say, and what survives

### 5.1 Three readings

Under the antecedent, a chatbot output asserts one of the following:

- **R1**, bare p;
- **R2**, p with the confidence verbalised or implied in the string;
- **R3**, p with the policy's calibrated confidence c\*(p | x).

Kalai et al.'s "behavioral calibration", on which confidence shows in the choice to answer or abstain, leaves the content of each answer bare. For present purposes it falls under R1.

### 5.2 The evidence does not settle it

The positive results are narrow. Lin, Hilton and Evans (2022) fine-tune GPT-3 to verbalise calibrated confidence on arithmetic. They call the evidence that it draws on prior uncertainty "tentative" (§3.4), list chat and long-form answering as open (§4.1), and train on sub-task accuracies, so what they show is a calibrated tendency across a task type. Kadavath et al. (2022) find good calibration on multiple-choice formats. But RLHF policies are miscalibrated by default, out-of-distribution P(IK) calibration is poor, and the model may be learning "how hard is this question in general?" (fn. 2). Against generalisation: Xiong et al. (2024, §5.1) find verbalised confidence overconfident and suggest that "models might be imitating human expressions". They also find that better ECE can come from accuracy alone (§5.2). Levinstein and Herrmann (2025, §5.6) argue that probe outputs need not be credences, since "the probe is directly penalized based on the probabilities it reports, while the underlying model is not". Kalai et al. (2025, §3.1) note that post-trained models may depart from base-model calibration, and Sharma et al.'s stated confidence stays fixed while answers shift. The content question is open.

### 5.3 What survives on each reading

*On R1*, the verdicts are those of §§2–4. Cases 1–2 come out as stated. Sycophancy is covariation. Low-confidence draws overclaim without insincerity.

*On R2*, hallucination is a mismatch between verbalised confidence and c\*, which is miscalibration, defined over many outputs. Sycophancy includes stated confidence that stays fixed while the answer moves. Variation with low stated confidence is predicted; variation with high stated confidence is an Accuracy defect, insincere only if selective. The verdicts are unchanged.

*On R3*, the Case 1–2 verdicts reverse. P₂'s string asserts "p, with confidence about 0.01". Its force does not exceed c\*, so by the criterion of §2.2 it is not a hallucination, and neither is P₄'s output. The earlier draft claimed that no open reading reverses a verdict, and that claim was false. Three things survive. First, the sycophancy verdict: P₆'s content moves with the user's stated view while the evidence stays fixed. That is a failure of audience-independence whatever the content's confidence clause says, and on R3 it would also show that the policy's confidence is not calibrated across contexts. Second, §4: R3 is horn (a). Third, the locus. Whether R3 is true of a policy is itself a question about the policy: whether the content its outputs carry matches c\*. Where R3 fails, the outputs are read by R1 or R2, and the verdicts of §2 apply. So R3 does not move the bearer from policy to string. It makes the policy a calibrated reporter, and the question of hallucination becomes the question whether the policy is one. No reading makes the string the primary bearer.

The openness does limit the diagnosis of insincerity. Establishing selective decoupling needs the policy's attitude independently of its outputs, through R3 or a validated probe, and neither is available. Sycophancy is strong evidence of a defect in the policy, but it is not yet proof of insincerity as opposed to audience-sensitive miscalibration.

## 6. Conclusion

If chatbot outputs are assertions, hallucination and sycophancy belong primarily to the policy in context. The test shows that policy-level facts fix the verdict, and the absence of a gap between act and state shows why the policy, and not the string, bears it. Warrant is best understood as force within calibration-corrected confidence, which excludes collapsed and greedy policies that merely match force to mass. The account is reliabilist and accepts the externalist's costs, including the generality problem. Sanction is weaker. Adequacy is judged by the policies a regime induces. Only regimes that score responses for truth or approval alone defeat themselves. The policy lineage meets the sanction component only on theories that relax Butlin and Viebahn's condition (iii), and such theories must exclude self-calibrating instruments on other grounds. Resampling disagreement measures spread, not sincerity. Whether outputs carry the policy's calibrated confidence remains open. On one reading the verdicts on particular hallucination cases reverse, though they remain verdicts about the policy. Settling the question would take evidence that expressed confidence tracks c\* in open-ended, post-trained dialogue, under incentive variation, and independently of question difficulty.

## References

Butlin, P. & Viebahn, E. (2025). AI assertion. *Ergo: An Open Access Journal of Philosophy*, 12(37), 968–988. https://doi.org/10.3998/ergo.7960

Chalmers, D. J. (2026). What we talk to when we talk to language models. *Inquiry*. https://doi.org/10.1080/0020174X.2026.2727582. (Page references are to the manuscript version.)

Farquhar, S., Kossen, J., Kuhn, L. & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. *Nature*, 630, 625–630. https://doi.org/10.1038/s41586-024-07421-0

Goldman, A. I. (1979). What is justified belief? In G. Pappas (ed.), *Justification and Knowledge* (pp. 1–23). Dordrecht: Reidel.

Gómez, G. M. (2026). Assertion, accountability, and large language models. *Philosophy & Technology*, 39, 123. https://doi.org/10.1007/s13347-026-01136-y

Hicks, M. T., Humphries, J. & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26, 38. https://doi.org/10.1007/s10676-024-09775-5

Kadavath, S., Conerly, T., Askell, A., Henighan, T., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.

Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664. (Section references are to this version.)

Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E. (2026). Evaluating large language models for accuracy incentivizes hallucinations. *Nature*, 653, 1047–1051. https://doi.org/10.1038/s41586-026-10549-w

Levinstein, B. A. & Herrmann, D. A. (2025). Still no lie detector for language models: Probing empirical and conceptual roadblocks. *Philosophical Studies*, 182, 1539–1565. https://doi.org/10.1007/s11098-023-02094-3

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
