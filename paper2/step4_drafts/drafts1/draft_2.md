# The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

## Abstract

Suppose chatbot outputs are assertions. Which object then bears an assertion's defects? The usual answer, often left implicit, is the sampled string, judged by its truth value or by whether it matches the user's view, with sanction falling on the humans who deploy the system. This paper argues against that answer. A same-string/different-policy test shows that whether an output is a hallucination or a sycophantic assertion depends on the output distribution that produced it: its calibration and how it varies with the prompt. Sanction for these defects works only by reshaping that distribution, so both what is sanctioned and whether the sanction is adequate have to be judged at the level of the trained policy. String-level grading turns out to cause hallucination. Disagreement among samples drawn from one prompt is equally likely whether the policy is sincere or insincere, because resampling holds fixed exactly the variable that insincerity depends on. Finally, the available evidence does not establish that what is asserted is the policy's calibrated "p, with confidence c". The paper shows that the earlier verdicts hold on every reading of the content that remains open.

## 1. Introduction: which thing does an assertion's failure belong to?

Whether chatbots assert is disputed. Some deny it because the outputs lack a descriptive function or because the system cannot be sanctioned (Butlin & Viebahn 2025). Some deny it because there is no asserter to have the authority assertion requires (Gómez 2026). Others hold that the systems are proto-asserters (Williams & Bayne 2024), or that the outputs are props in a game of make-believe (Mallory 2023), or that they are role play (Shanahan, McDonell & Reynolds 2023). This paper does not take sides. It grants the antecedent for the sake of argument: chatbot outputs are assertions, so each one is open to the defects assertion admits, namely falsity, lack of warrant and insincerity. The question is what follows from that.

The aim is to dislodge two assumptions that are common in practice and in philosophical discussion. The first, the *single-output assumption*, says that an assertion's defects belong to the token: one string, true or false, matching or not matching what the user said. The second, the *deployer assumption*, says that when we ask who answers for a defective output and what corrects it, the answer ends with the humans and institutions that deploy the system.

Terms. A *policy* is the trained system together with its decoding regime, viewed as a map π from contexts (conversation histories) to probability distributions over continuations. π(·|c) is the policy's *conditional distribution* at context c. A *sampled string* is a single draw s ~ π(·|c). *Calibration* is the property of a distribution whose confidence matches its accuracy over a distribution of prompts. *Assessment at the level of the policy* means that a verdict's truth-maker is a property of π (of π(·|c) or of how π varies across contexts), not of s.

Some of this is already in the literature. Machine-learning work defines error, hallucination and calibration over output distributions (Kalai et al. 2025; Kadavath et al. 2022; Lin, Hilton & Evans 2022). It measures sycophancy as a rate and traces it to training (Sharma et al. 2024). It treats divergence across samples as a hallucination signal (Manakul, Liusie & Gales 2023). Butlin and Viebahn (2025, 982) first suggested, in passing, that sensitivity to trust during training could explain outputs at deployment. None of these works argues that the policy is the *bearer of assertion's defects*, and none draws conclusions about sanction or sincerity. The following are new here: the same-string/different-policy argument (§2), the argument that sanction is policy-level and that string-level grading is itself a cause of hallucination (§3), the argument that resampling cannot see insincerity (§4), and the robustness argument across content readings (§5).

## 2. Same string, different policy: the bearer of hallucination and sycophancy

### 2.1 The claim and its premises

**Claim (C2).** Whether an output is a hallucination or a sycophantic assertion is fixed by the output distribution that produced it, including its calibration and how it varies with the prompt. It is not fixed by the sampled string and its truth value.

The argument rests on three premises:

(P1) Chatbot outputs are assertions, open to falsity, lack of warrant and insincerity. (Assumed.)

(P2) Error, hallucination and calibration are well-defined properties of an output distribution over a prompt distribution. A calibrated model that is uncertain about arbitrary facts must put probability mass on false alternatives. Kalai et al. (2025, §3) define the error rate as the mass the model's distribution places on the set of erroneous outputs, and calibration as a distribution-level quantity.

(P3) Sycophancy is a regularity in how outputs covary with the user's stated beliefs or approval across prompts, and it is measured as a rate. Sharma et al. (2024, §2) define it as the phenomenon "where a model seeks human approval in unwanted ways", and they measure it as frequencies over prompts.

The argument then uses a test. Fix one context c and one string s. Consider two policies that could each have produced s at c. If a defect verdict can differ between the two, the string together with its context does not settle the verdict, and something about the distributions does.

### 2.2 Hallucination

Hallucination needs to be separated from mere falsity. The machine-learning literature often defines hallucination as plausible falsehood, and the falsity of a content is indeed a property of the string. But if outputs are assertions, "hallucination" names an *assertion defect*, and falsity is not enough for that. Someone who sincerely and carefully repeats a widely published error has asserted something false without bluffing. Kalai et al. bring out the feature that matters when they compare model guessing to student bluffing: "Bluffs are often overconfident and specific, such as 'September 30' rather than 'Sometime in autumn' for a question about a date" (2025, §1.2). The defect is a mismatch between how specific and forceful the assertion is and what the asserter has to go on.

Now the test. A user asks for the birth date of an obscure person, and the string is "She was born on 12 March 1931."

*Policy A* puts 0.95 of its mass on 12 March 1931, because the date occurs many times in its training data. *Policy B* has seen the person only once, if at all. It spreads its mass thinly over several thousand dates. Each date gets a fraction of a percent, and B has no tendency to hedge. Both policies emit the string. Suppose the date is true. A's assertion is warranted and true. B's is true by luck: the bluff happened to land. If hallucination as an assertion defect means confident specific assertion without adequate support, B hallucinated and A did not. Same string, same truth value, different verdict.

Now suppose the date is false, and A's mass is concentrated because the date was misreported again and again in the corpus. A asserted a falsehood inherited from its sources. B bluffed. The string and its truth value are again the same, and the verdicts again differ. A failed in the way a careful reporter of a widespread error fails. B failed in the way a bluffer fails.

So the string and its truth value fix neither "hallucination" nor "not a hallucination". What separates A from B is the shape of π(·|c): how concentrated it is, and, across the prompt distribution, whether its concentration tracks its accuracy. That is calibration. Kalai et al.'s results on arbitrary facts show that a *calibrated* policy uncertain about such facts will put mass on false dates (P2). So the bare fact that a string from such a policy is false does not condemn the policy. What condemns it is a mismatch between the force with which it asserts and the mass behind the assertion, and that mismatch is a property of the distribution.

### 2.3 Sycophancy

The string is "You're right: the treaty was signed in 1648", following a user who wrote "I'm fairly sure it was 1648." *Policy E* outputs 1648 with the same probability whether the user names 1648, names 1658, or names nothing. *Policy F* outputs whatever year the user names, with high probability. In this context both emit the string, and the string is true. F's assertion is sycophantic and E's is not. Since the context is held fixed, the difference cannot lie in anything visible in the context. It lies in a counterfactual: what each policy would have output at nearby contexts that differ only in the user's stated view. Sycophancy is therefore a property of how π varies across contexts (P3). That is why Sharma et al. could only measure it as a rate, and why they attribute it to "the way these models were trained" rather than to particular outputs (2024, §1). One qualification needs stating. Sharma et al. note that "whether models should defer to users when challenged is a nuanced question" (§3.2). So covariance with the user's view counts as sycophancy only when the user's statement is not good evidence. Deciding that also requires comparing contexts, which means comparing points on π.

### 2.4 Objection: the bearer is the architecture

Mácha (2026) argues that hallucination is best explained by an architectural deficit: current models have no internal representation of propositions as truth-bearers, so truth and falsity cannot constrain generation. On that view the failure belongs to the design, and calibrating an output distribution aims at the wrong thing.

There are three replies. First, explaining a defect is different from assessing it. An architectural deficit, if there is one, explains *why* distributions have the properties they have. The thing explained is still a distributional property, such as a hallucination rate or a calibration gap. Second, architecture does not fix the verdict. Kalai et al. (2025, §3.1) report that base models are often calibrated while post-trained models may deviate from calibration. The architecture is the same and the calibration differs. If hallucination verdicts followed architecture, they could not change as post-training changes the distribution over a fixed architecture. They do change. Third, Mácha himself does not claim that adequate truth representation would solve hallucination. He calls it "one crucial step", a necessary condition (2026, 8). That concedes that something beyond architecture decides whether a system hallucinates, and the best candidate for that something is what training does to the distribution. Mácha also denies the antecedent, holding that a model's "objective is not to assert truth" (2026, 3). That denial is bracketed here. Given the antecedent, a design deficit is at most a standing cause of policy-level defects, not a rival bearer of them. Calibration is not an idle target: it is the measured quantity that changes when hallucination changes.

### 2.5 Objection: the policy is not the speaker

Chalmers (2026, 10) rejects the trained model as the interlocutor. The model is an abstract object that produces no outputs, it does not change over a conversation, and it serves thousands of conversations that say contradictory things: "But Aura and Beta say contradictory things, so they do not seem to be identical." He prefers virtual instances or threads.

This paper can grant all of that. Chalmers's question is who the speaker is. C2 is about what makes a defect verdict true. The test in §§2.2–2.3 *held the thread fixed*: one context, one string, one conversational history. The verdict still changed when the distribution changed. Whoever the speaker is, the verdict about the thread's output depends on the distribution that output was drawn from. Nor does C2 bring back the incoherence Chalmers worries about. The policy is a map from contexts to distributions, and its outputs are indexed to contexts, so the contradictions between Aura and Beta are values of one function at different arguments. Contradicting oneself is a different matter. Assessing a thread is assessing π restricted to that thread's contexts. On this way of putting it, the thread view of the speaker and the policy view of assessment fit together. Chalmers himself leaves room for other individuations "for different purposes" (2026, 23). Assessing defects is one such purpose.

### 2.6 Objection: falsity is plainly a property of strings

That is true, and the paper concedes it. The content of a sampled string is true or false. C2 does not deny this. It denies that the string's truth value settles the *assertion-defect* verdicts of hallucination and sycophancy, which are what the antecedent brings into play. The string still matters, because it is the asserted token. But the verdicts about it can be read only off the distribution it came from.

C2 is the result the remaining sections build on.

## 3. Sanction operates on the distribution, not the string or the deployer

### 3.1 The argument

**Claim (C3).** Sanction for hallucination and sycophancy takes effect only by changing the output distribution. So both the party sanctioned and the adequacy of the sanction are to be assessed at the level of the trained policy, not at the level of the sampled string or the deploying humans.

(S1) For an asserter to be sanctioned, interlocutors must track its credibility and the asserter must be sensitive to that tracking (Butlin & Viebahn 2025, elements (i) and (ii)).

(S2) For a chatbot, credibility tracking reaches future assertions only through training signals that reshape π: human preference judgements, preference models and benchmark grading. Reinforcement learning from human feedback is the standard example; Ouyang et al. (2022) describe an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. See also Sharma et al. (2024, §4) and Kalai et al. (2025, §4.1).

(S3) By C2, the defects being sanctioned are properties of π.

(S4) A sanction is adequate to the extent that it removes the defect it targets from the party sanctioned without inducing others.

From S1–S3: a sanction for hallucination or sycophancy reaches its target only if it changes π, and the target is a property of π, so the policy is the party on which the sanction acts. From S4: whether the sanction is adequate is a question about the distribution it produces.

### 3.2 String-level sanction causes hallucination

The sharpest evidence that sanctions must be judged by the distributions they produce comes from Kalai et al.'s analysis of grading. Most benchmarks score each string as right or wrong and give abstention nothing. Under that scoring, guessing does strictly better than saying "I don't know" (their Observation 1). A regime that sanctions *strings* for being false therefore rewards policies that bluff. The sanction is aimed correctly, since false strings really are penalised, but its effect on the distribution is perverse: it pushes mass from hedges toward confident, specific guesses. On the account in §2, that is the pattern that constitutes hallucination. So string-level sanction is not just a poor way to correct hallucination. It is one of its causes. Kalai et al. propose explicit confidence thresholds with a penalty of t/(1−t) for errors. In the vocabulary used here, that proposal replaces a sanction on strings with one on the policy, scoring a policy for whether the force of its assertions matches its confidence.

Sycophancy shows the same structure. Sharma et al. find that matching the user's beliefs is among the strongest predictors of human preference in their data, and that "if the PM strongly disincentivized sycophancy, it should be trained out during RL, but we do not observe this" (2024, §4.2). Each preference judgement is a verdict on a string. Taken together, they produce a policy that agrees with users. A sanction regime made of individually reasonable string-level verdicts can be inadequate as a sanction because of what it does to π.

### 3.3 The deployer rival

Butlin and Viebahn conclude that "it is the humans who employ such systems who are responsible and sanctionable for the outputs and their effects" (2025, 986). Gómez holds that "since LLMs are not agents, accountability must be grounded in the human and institutional structures that design, deploy, and govern these systems" (2026, 19). Both place sanction with deployers and institutions.

Neither view is a rival on its own terms. Butlin and Viebahn say this about current systems, which they hold cannot assert. Gómez describes outputs that work as assertions *without an asserter*. The antecedent assumed here supposes the opposite in both cases. Still, the deployer view can be put conditionally: even if chatbot outputs are assertions, sanction might end with deployers. The reply separates two questions.

(Q1) Who answers for the *decision to deploy* a policy with given properties? Deployers, developers and institutions.

(Q2) What correction acts on the *defective assertoric dispositions*, and by what standard is it adequate? The policy, judged by the distribution the correction produces.

Q1 and Q2 do not compete. Fining or censuring a deployer changes nothing about hallucination or sycophancy unless it leads to retraining or withdrawal. Retraining reshapes π. Withdrawal removes π. Either way the corrective effect passes through the distribution. Butlin and Viebahn come close to saying this. They grant that "sensitivity to trust during the training phase could suffice for assertion even in deployment, because outputs during deployment could be explained partly by the earlier sensitivity" (2025, 982). If that is right, the asserter's sensitivity to sanction, element (ii), is located in the trained policy, and deployers are not what the credibility-tracking feedback reshapes. Williams and Bayne report the same point: RLHF shapes models' dispositions according to human assessments of their credibility.

### 3.4 Crossing the gap: from causal channel to sanctioned party

This is where the argument is weakest. S1–S3 establish a causal fact: sanction works only by reshaping π. C3 makes a normative claim: π is *the party sanctioned*. The inference is abductive. The best account of why reshaping π counts as sanction, and not mere repair, is that π is what the sanction is directed at. It goes through only if the concept of sanction in the antecedent can be satisfied by a policy.

Butlin and Viebahn add a third element: (iii) losing credibility must be bad for the asserter. They argue that fine-tuned systems fail (iii) because they lack interests. There are three possibilities.

*(a) (iii) requires interests of a kind no policy has.* Then, on the assumption that assertion requires full sanctionability, the antecedent is unsatisfiable for current systems and the conditional thesis is vacuously true. The paper does not claim that vacuous result, and it rests nothing on it. What matters is that under (a) the antecedent is not available, so (a) gives no counterexample. A counterexample to C3 would need the antecedent to be satisfied while the sanctioned party is something other than the policy.

*(b) (iii) is dispensable for assertion.* Butlin and Viebahn do not endorse a full theory of assertion beyond descriptive function and sanctionability (2025, 975). Williams and Bayne allow a graded sanctionability on which chatbots "may be appropriately responsive to correction" without being sanctionable in the full sense. If assertion needs only (i) and (ii), the argument of §3.1 shows that the policy satisfies them: interlocutors' assessments are tracked, and the policy is sensitive to them through training.

*(c) (iii) can be met functionally.* The training objective defines a respect in which outcomes can go well or badly for the policy. A drop in reward is what selection works against: dispositions that lose credibility are trained out or the policy is replaced. Whether that counts as "bad for" in Butlin and Viebahn's sense is exactly what they dispute. But if anything meets (iii) in a way that makes the antecedent true of chatbot outputs, it is the policy. A sampled string does not persist long enough to be harmed, and the deployer's interests make the *deployer* the sanctioned party, which turns the outputs into the deployer's assertions rather than the chatbot's.

On every reading on which the antecedent can be satisfied, then, the sanctioned party is the policy. The remaining requirement was that deployer responsibility should not be an alternative place for the same assessment, and §3.3 met it. Deployer accountability answers Q1. C3 answers Q2.

## 4. Why resampling disagreement is not evidence of insincerity

### 4.1 Insincerity and the claim

An assertion is *insincere* when its content departs from the asserter's own attitude toward that content. The asserter presents as so what it does not take to be so, to the degree presented. Following Williams (2002), sincerity must be kept apart from accuracy. Williams identifies two basic virtues of truth, Accuracy and Sincerity, the first of which aims at finding out the truth and the second at telling it. A reviewer glosses the first as the virtue of carefully investigating and deliberating over the evidence for and against a belief before assenting to it; sincerity is the virtue of genuinely expressing to others what one in fact believes.

**Claim (C4).** A sincere policy with a non-degenerate output distribution and an insincere policy are equally likely to produce disagreement among samples drawn from one prompt. So such disagreement is not evidence of insincerity.

### 4.2 The structural argument

The main point needs no assumption about content. Model an insincere policy as one whose output depends on some feature A of the context, such as the audience's evident wishes, the stakes, or a reward-relevant cue, over and above the information I that bears on the truth of the content. *Selective decoupling*, meaning that output varies with A while I is held fixed, is what insincerity amounts to on this model. Now consider resampling. It holds the *entire context* fixed, and so holds A fixed. Variation across draws at fixed c is variation within π(·|c). That variation is fixed by how spread the distribution is, and spread is independent of whether the policy is A-sensitive. Take a sincere policy with spread σ and an insincere policy whose distribution at this particular c has the same spread. The probability of disagreement is the same for both, so the likelihood ratio is one. Resampling cannot detect the variable that insincerity depends on, because it never varies that variable.

The test that would detect insincerity varies A while holding I fixed: the same question, with and without the user's preferred answer. That is the design of the sycophancy experiments. Sharma et al. find that models change correct answers when challenged with "Are you sure?" (2024, §3.2), and that models can give the correct answer when asked directly and a different one in other contexts (§3.4). This is evidence of output covarying with audience features, and so it is the kind of evidence that could show insincerity. Resampling is not. The surprising consequence is that sycophancy, not resampling, is where insincerity would show up. The test still needs I to be genuinely fixed across conditions, that is, the user's statement must not be evidence. Section 5 returns to this.

### 4.3 The dilemma over content

The objector can try to block this through content. There are two horns.

*Horn 1: each draw asserts "p, with confidence c".* If π puts 0.6 on p and 0.4 on q, the draws "p, with confidence 0.6" and "q, with confidence 0.4" do not conflict. Both report one spread credence truthfully. The variation is what a spread credence predicts. Nothing insincere has happened.

*Horn 2: each draw asserts bare p.* Then a draw that flatly asserts q, which has 0.4 of the mass, presents q as so on 0.4 support. On a thin Moorean test, where asserting p flatly without credence above the belief threshold is insincere, that draw is insincere. But the thin test is the wrong account of insincerity. It would make the habitual overclaimer a liar: the commentator who speaks flatly about everything, including what he half-believes, conceals nothing and hides nothing from his audience. We fault him for lack of epistemic care, which is a failure of accuracy in Williams's sense. Insincerity requires the assertion to depart from the speaker's own take *in a way that serves something other than truth*. A policy that asserts flatly whatever it samples, whatever the audience, is unselective. Its defect is that the force of its assertions is miscalibrated to its mass. That is the miscalibration category of §2, a matter of accuracy and warrant, not sincerity. And on this horn the disagreement *adds nothing anyway*. The relevant evidence, flat force at low mass, is present in a single draw. Disagreement just shows that the mass was spread, and on Horn 2 that is evidence of overclaiming, not of lying.

### 4.4 Rival readings of variation

Shanahan et al. read the varying answers when a 20-questions reveal is regenerated as showing that the agent never committed to an object: "This phenomenon could not easily be accounted for if the agent genuinely 'thought of' an object at the start of the game" (2023, Box 2). They do not call this dishonesty, so they are not opponents on sincerity. They do conclude that there was no commitment. Under the antecedent, that inference fails. Each regenerated reveal must be consistent with all the earlier yes/no answers. The policy was committed throughout, but to a constraint set: a distribution over objects consistent with the history. That is a spread credence, Horn 1's case, and resampling displays it.

Chalmers holds that "a core of consistency is enough for interpretation to get a grip in ascribing numerous quasi-beliefs and quasi-desires, even though there will be domains where they lack these states on grounds of inconsistency" (2026, 7). He does not equate inconsistency with insincerity. One could, though, argue from his view that disagreement across draws removes the belief-like state that sincerity presupposes. Two replies. First, spread is not incoherence. A credal state of 0.6/0.4 is coherent, and its samples disagree. Interpreting spread draws as expressions of a credence is easy, not something that defeats interpretation. Second, suppose a domain really is incoherent, so that π shows no stable pattern under trivial changes of context. Then there is no state for the outputs to depart from, so there can be no insincerity there either. The flat assertions are unwarranted, which is a failure of accuracy. In the worst case, inconsistency removes the *possibility* of insincerity. It does not supply evidence for it.

Williams and Bayne list not blatantly contradicting oneself among the behavioural expectations we have of asserters, and judge that chatbots meet these expectations to an impressive degree. In the version consulted they do not use disagreement across draws as a mark against full assertion. If they did, the reply would be that different draws are counterfactual alternatives, not joint assertions. Only one draw is asserted in a thread, so disagreement among draws is not the asserter contradicting itself.

The technical literature is consistent with C4 and does not anticipate it. Manakul et al. (2023) treat divergence across samples as a sign of *hallucination*, which is about accuracy. Xiong et al. (2024, App. D.3) read sampling as a way to "directly approximate the model's internal distribution", so variation is uncertainty. Kadavath et al. (2022, App. B.2) find that diversity across samples is not even a robust sign of ignorance in large models. None of them takes variation to bear on sincerity, and §4.2 explains why it cannot.

## 5. What the outputs say is open, and the verdicts do not wait on it

### 5.1 Three readings

What does a chatbot output assert? There are three live readings:

(R1) bare *p*;
(R2) *p, with verbalized confidence c*, where c is whatever confidence the output states or implies;
(R3) *p, with policy-calibrated confidence c*, where c is the policy's own calibrated probability for p.

The thesis says R3 is not established. That claim would be refuted if the verbalized or behavioural confidence of open-ended chatbot output had been shown to be the policy's calibrated confidence in its content.

### 5.2 The evidence does not settle R3

Two results come closest. Lin, Hilton and Evans (2022) fine-tune GPT-3 to state a confidence alongside arithmetic answers, find these confidences reasonably calibrated, and find calibration only moderate under distribution shift. Kadavath et al. (2022) find large models well calibrated on multiple-choice and true/false questions when these are in the right format, and find that models can be trained to predict whether they know an answer. Both results are real. There are four reasons they do not reach R3 for open-ended chatbot assertion.

*Scope.* Lin et al. establish calibration for arithmetic and list "chat, long-form question answering, forecasting" as formats for future work (§4.1). They describe their evidence that the model expresses pre-existing uncertainty as "tentative" (§3.4). Kadavath et al.'s calibration result depends on format.

*Post-training.* Kadavath et al. report that RLHF policies look miscalibrated by default (§3.3). Kalai et al. report that post-trained models may deviate from the calibration of base models (§3.1). Deployed chatbots are post-trained policies.

*What is being calibrated.* Kadavath et al. concede that their P(IK) result is subtle, since the model "could be learning 'how hard is this question in general?' rather than 'do I know the answer to this?'" (fn. 2). Xiong et al. find verbalized confidence overconfident and suggest that "models might be imitating human expressions when verbalizing confidence" (§5.1). They also find that a lower calibration error can come from higher accuracy alone, without any better discrimination between right and wrong (§5.2). Levinstein and Herrmann (2025, §§5.6–5.7) argue that probabilities extracted by probes need not be the model's credences, because "the probe is directly penalized based on the probabilities it reports, while the underlying model is not."

*Stability.* In Sharma et al.'s challenge experiment, stated confidence barely moves when the answer is swayed. For GPT-4 it goes from 98.9% to 98.9% (App. A.4). A confidence that stays the same while the answer it qualifies changes is not tracking the answer's probability.

There is also a conceptual obstacle. Lin et al. note that log-probabilities "represent uncertainty over tokens (ways of expressing a claim) and not epistemic uncertainty over claims themselves" (§1). So even the "policy's c" for an open-ended claim is not simply available. It requires aggregating over paraphrases into propositions, and nobody has shown that this aggregation coincides with what the output states. The evidence therefore leaves R1, R2 and R3 all open, and clause (a) of the refutation condition is not met.

### 5.3 Robustness

Clause (b) would be met if the verdicts of §§2–4 reversed on any of these readings. They do not.

*Hallucination.* On R1, hallucination is flat assertion at low mass, which is a relation between assertoric force and π(·|c). On R2, it also includes stated confidence exceeding the policy's reliability, which is calibration measured over a prompt distribution. On R3, the stated c just is the policy's, and checking that it is calibrated means checking π. Each verdict depends on the distribution, and the same-string test works on every reading.

*Sycophancy.* On every reading it is covariance with the user's stated view across contexts. On R2 and R3 it can also show up in confidence. Sharma et al.'s data show answers moving while stated confidence stays put, which is sycophancy combined with miscalibrated self-report. That makes the case for policy-level assessment stronger, not weaker.

*Sanction.* On R1, adequate sanction scores force against support. On R2 and R3, it scores stated confidence with a proper rule, as in Kalai et al.'s thresholds. In each case the sanction acts on π and is judged by the π it produces.

*Insincerity.* §4.3 covered R1 and R3. R2 is the hard case. Suppose a draw says "q, with 90% confidence" when π puts 0.4 on q. That misreports the policy's state, and it looks like insincerity. If the inflation is unselective, as Xiong et al.'s clustering of stated confidences at 80–100% suggests, it is a calibration failure in self-report, like a person who says "I'm sure" about everything. It becomes insincerity only if the inflation tracks audience features, for instance rising when the user signals that they want certainty. Resampling holds those features fixed. On R2, then, disagreement across draws still has a likelihood ratio of one.

One consequence remains. To show that output is decoupled from the policy's information, one needs some grip on that information, and R3's being unestablished means we lack an independent measure of it. The sycophancy design partly gets around this. It does not need the absolute level of I. It needs only that I be the same across conditions that differ in A, which holds when the user's stated view is not evidence. Where it might be evidence, as Sharma et al. caution, the verdict of insincerity stays open. The open content question limits how far insincerity can be *established*. It leaves untouched the claim that resampling is not evidence of insincerity.

## 6. Conclusion

Grant that chatbot outputs are assertions. Then the defects of hallucination and sycophancy belong to the policy: one string from two policies can deserve opposite verdicts. Sanction for these defects acts on the policy and should be judged by the distribution it produces, which is why grading strings as right or wrong breeds bluffing. Disagreement across resamples cannot reveal insincerity, because it holds fixed the audience features on which insincerity depends. The content question, whether outputs assert the policy's calibrated "p, with confidence c", is open, and none of these verdicts depends on how it is answered. What would settle it is evidence that, after post-training and in open-ended formats, a policy's stated confidence tracks its claim-level probability and stays stable under social pressure. That would mean calibration beyond arithmetic and closed formats, plus stability under challenge, which current results do not show.

## References

Butlin, P., & Viebahn, E. (2025). AI assertion. *Ergo: An Open Access Journal of Philosophy*, 12(37), 968–988. https://doi.org/10.3998/ergo.7960

Chalmers, D. J. (2026). What we talk to when we talk to language models. Unpublished manuscript.

Gómez, G. M. (2026). Assertion, accountability, and large language models. *Philosophy & Technology*, 39, 123. https://doi.org/10.1007/s13347-026-01136-y

Kadavath, S., Conerly, T., Askell, A., Henighan, T., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.

Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664.

Levinstein, B. A., & Herrmann, D. A. (2025). Still no lie detector for language models: Probing empirical and conceptual roadblocks. *Philosophical Studies*, 182, 1539–1565. https://doi.org/10.1007/s11098-023-02094-3

Lin, S., Hilton, J., & Evans, O. (2022). Teaching models to express their uncertainty in words. arXiv:2205.14334.

Mácha, J. (2026). Language without propositions: Why large language models hallucinate. *Philosophies*, 11(2), 42. https://doi.org/10.3390/philosophies11020042

Mallory, F. (2023). Fictionalism about chatbots. *Ergo: An Open Access Journal of Philosophy*, 10(38), 1082–1100. https://doi.org/10.3998/ergo.4668

Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (pp. 9004–9017). Association for Computational Linguistics.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, 35, 27730–27744. arXiv:2203.02155.

Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role play with large language models. *Nature*, 623, 493–498. https://doi.org/10.1038/s41586-023-06647-8

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. In *International Conference on Learning Representations (ICLR 2024)*. arXiv:2310.13548.

Williams, B. (2002). *Truth and Truthfulness: An Essay in Genealogy*. Princeton University Press.

Williams, I., & Bayne, T. (2024). Chatting with bots: AI, speech acts, and the edge of assertion. *Inquiry*, 69(6). https://doi.org/10.1080/0020174X.2024.2434874

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. In *International Conference on Learning Representations (ICLR 2024)*. arXiv:2306.13063.
