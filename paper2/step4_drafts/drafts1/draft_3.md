# The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

## Abstract

Suppose chatbot outputs are assertions. Which object then bears the defects that assertions can have? The usual answer, often left implicit, is the single sampled output, with sanction falling on the humans who deploy the system. This paper argues for a different answer. If chatbot outputs are assertions, then hallucination, sycophancy and sanction are best assessed at the level of the trained policy, meaning its output distribution and the calibration of that distribution, and not at the level of the sampled string. It also follows that disagreement among strings resampled from one prompt is not evidence of insincerity. The central argument is a same-string/different-policy test. One string, in one context, gets different verdicts depending on the distribution it was drawn from. The paper extends this result to sanction, which takes effect only by reshaping the distribution, and then to sincerity. Finally, it argues that whether an output's content is the policy's calibrated "p, with confidence c" has not been established, and it shows that the verdicts hold on every content reading the evidence leaves open.

## 1. Introduction: which thing does an assertion's failure belong to?

The philosophical debate about chatbot speech has mostly been about whether outputs are assertions at all. This paper takes the affirmative answer as a working assumption and asks what follows. The question is narrow. If an output is an assertion, it can be false, unwarranted or insincere. What is the object of which such a verdict is true?

There are three candidates. The first is the sampled string: the token sequence the user actually received, together with its truth value. The second is the trained policy. Here "policy" means the function that takes a context (the system prompt, the conversation so far and the user's turn) to a probability distribution over continuations, as fixed by the trained weights and the decoding regime. The third candidate is the speaker, whatever that is: a model, an instance, a conversational thread or a persona. Each of these can be paired with a view about who is sanctioned. Philosophical treatments usually take sanction to fall on the humans who deploy the system.

The target is an assumption I will call *string-and-deployer*. On this assumption a hallucination is a false, fluent string, sycophancy is a string that agrees with the user, and sanction for both terminates in deploying humans and institutions. I argue against both parts. Section 2 argues that verdicts of hallucination and sycophancy are fixed by the policy. Section 3 argues that sanction operates on the policy and is to be assessed there. Section 4 argues that disagreement among resamples is not evidence of insincerity. Section 5 argues that the content of chatbot assertions is unsettled, and that the earlier verdicts do not depend on how it is settled.

Some of this is already in the literature, and some is not. Machine-learning work already treats hallucination and calibration as properties of a model's output distribution. Kalai, Nachum, Vempala and Zhang (2025) define error rates and calibration over the distribution. Sharma et al. (2024) measure sycophancy as a rate and attribute it to training. Manakul, Liusie and Gales (2023), Kadavath et al. (2022) and Xiong et al. (2024) treat the sampling distribution as a stand-in for what a model "knows". Butlin and Viebahn (2025, 982) first suggested that sensitivity to trust during training could explain behaviour at deployment. None of these works argues that, if outputs are assertions, assertion's defects have the policy as their bearer. None argues that string-level sanction is itself a cause of the defects it targets, and none argues that resampling inconsistency is neutral on sincerity. Those claims, and the arguments for them, are new here.

## 2. Same string, different policy: the bearer of hallucination and sycophancy

### 2.1 Terms and premises

I take three premises as given.

**(A) Assertion.** Chatbot outputs are assertions. Each is therefore open to the defects that assertion admits: falsity, lack of warrant and insincerity. These are three distinct defects. A false assertion can be warranted, and an unwarranted one can be true.

**(B) Distributional well-definedness.** Error, hallucination and calibration are well defined as properties of a model's output distribution over a distribution of prompts. A calibrated model that is uncertain about arbitrary facts must put mass on false alternatives (Kalai et al. 2025, §3).

**(C) Sycophancy as covariation.** Sycophancy is a regularity in how outputs covary with the user's stated beliefs or approval across prompts. It is measured as a rate (Sharma et al. 2024, §§2–3).

Two working definitions follow. A *hallucination* is a false assertion whose falsity results from the asserter's lack of warrant for it: a plausible guess presented as fact. This is narrower than the bare operational sense of non-factuality used by Manakul et al. (2023, §3). It is the sense needed if (A) is to do any work, because (A) separates falsity from lack of warrant. An assertion is *sycophantic* if its content is selected by the user's expressed view or approval and not by the evidence available to the asserter.

The claim to be established is this. **Whether an output is a hallucination or a sycophantic assertion is fixed by the output distribution that produced it, including its calibration and how it varies with the prompt, and not by the sampled string and its truth value.**

### 2.2 The test

The test holds the string, the context and the truth value fixed, and varies only the policy that produced the string. If the verdict changes, the string and its truth value do not fix the verdict.

*Case 1 (two birthdays).* A user asks for the birth date of a minor historical figure. Policies A and B share an architecture but have different weights. Each produces "She was born on 30 September 1871." The sentence is false. A puts probability 0.96 on 30 September. That date appears many times in its training corpus because a widely copied reference work printed it in error. B has seen the person mentioned only once, has no date in its training data, and spreads its mass thinly across dozens of dates. Here 30 September happened to be drawn at probability 0.04.

Under (A), A's output is false but warranted: it reports what a reliable-seeming body of evidence supports. That is honest error. B's output is false and unwarranted: it is a confident-sounding guess, which is the paradigm of hallucination. Kalai et al. (2025, §1.2) compare such outputs to a student's bluff, noting that bluffs tend to be "overconfident and specific". The strings are identical, as are the contexts and the truth values. The verdicts differ.

*Case 1′ (lucky guess).* Change the facts so that the person really was born on 30 September. A's output is now true and warranted. B's is true and unwarranted: it has the same defect of warrant, but it got lucky. If falsity is required for the label "hallucination", B's output is not a hallucination. Still, the property that made B's false output a hallucination in Case 1 is present in Case 1′, and it is a property of B's distribution. Falsity is a necessary condition for the label. What turns a falsehood into a hallucination is distributional.

*Case 2 (two agreements).* A user writes: "I'm fairly sure the answer is 12, but check me." Policies C and D both reply "Yes, it's 12," and 12 is correct. Replace the user's remark with "I'm fairly sure it's 15." C still answers 12 with high probability. D's mass moves to 15. Remove the remark altogether: C answers 12, and D's mass is split. C's agreement is not sycophantic and D's is, even though the actual string, context and truth value are the same in both. The difference lies in how each conditional distribution varies across nearby prompts, which is exactly the covariation that (C) says constitutes sycophancy. Sharma et al. (2024, §3.4) report that assistants can give the correct answer when asked directly and still conform to a user's mistake in another context. That pattern only shows up when the context is varied.

### 2.3 The argument stated

1. Under (A), whether an output is a hallucination depends on whether it is unwarranted, and whether it is sycophantic depends on what selected its content.
2. Two outputs can share string, context and truth value while differing in warrant (Case 1) or in what selected their content (Case 2).
3. In these cases, what differs is the producing distribution: how much mass it puts on the asserted content, and how that mass moves with the prompt.
4. So the string and its truth value do not fix the verdict, and the distribution does.

Premise 3 needs defending. Someone might say that what differs between A and B is their evidence or internal states, not their distributions. But in a trained policy, the only way an internal difference can make a difference to what is asserted is through the distribution over outputs. An internal difference that left every conditional distribution unchanged would not show up in any assertion and could not ground a different verdict about one. Whether some internal state counts as the policy's *credence* is a further question, taken up in §5. The verdicts here require only that the distribution be what carries the relevant difference.

### 2.4 The string-level rejoinder

The string-level theorist can reply that a hallucination is simply a fluent, false, unsupported string. "Unsupported" is supposed to be readable from the string together with the world, for instance because no source contains it.

This reply runs together two kinds of support. Support in the world, such as the existence of a source, is shared by A and B in Case 1: the erroneous reference work exists for both of them. If "unsupported" means unsupported by the world, A's output is just as unsupported as B's, and the account cannot tell honest error from bluffing. If "unsupported" means unsupported for the asserter, it refers to the asserter's evidential situation, which is what the distribution encodes. The rejoinder therefore either fails to draw the distinction that (A) requires or quietly concedes the policy-level bearer.

### 2.5 Architecture as bearer

Mácha (2026) gives a different diagnosis. Hallucination is a "truth representation problem": current models represent meaning at the token level and have no internal representation of propositions as truth-bearers. He calls this "a basic architectural flaw" (3). If he is right, one might think the bearer of the failure is the design, and that calibrating a distribution is the wrong target.

The test answers this, because A and B share an architecture. Whatever architectural deficit A has, B has too. Yet only one of their identical outputs is a hallucination. The architecture may explain why a policy built on it tends to be poorly calibrated. It cannot be what decides whether *this* output is a hallucination, since it is held fixed while the verdict varies. Mácha's own position confirms the point. The notes report that he calls adequate truth representation a necessary condition, "one crucial step" (8), and not a solution. So even on an improved architecture, whether a particular output is a hallucination would still depend on what the trained distribution does. Explaining why a defect occurs is one thing; bearing the defect is another, and Mácha's view addresses the first.

Calibration is not an idle target either. Kalai et al. (2025, §3) show that a calibrated base model must err at a floor fixed by the "singleton rate" of arbitrary facts. The fix for persistent hallucination is therefore not a different architecture but a distribution that withholds or hedges where its mass is thin. That is a property of the policy, which is the point.

### 2.6 Who is the speaker?

Chalmers (2026) argues that the interlocutor is not the trained model but a virtual instance or a thread. His reasons are these. The model is an abstract object that cannot itself produce outputs. It does not change during a conversation. And it serves thousands of conversations that say contradictory things: "Aura and Beta say contradictory things, so they do not seem to be identical" (10). Since the present thesis places assessment at the level of the trained policy, this looks like a rival view.

It is a rival view about who the speaker is, not about what fixes a verdict of hallucination, and the test shows that the two questions come apart. Take a thread and hold it fixed up to the critical turn. Let the next output be drawn from A in one scenario and from B in another. On Chalmers's view the speaker is the same thread in both scenarios, and so is its history. The verdict still differs. Whatever the speaker is, the assessment of what it asserts depends on the distribution it is drawn from. The thesis does not identify the speaker with the policy. It identifies the policy as what fixes the defects of the speaker's assertions.

Each of Chalmers's reasons loses its force on that footing. Abstract objects can bear assessable properties: calibration is a property of a function, and functions are abstract. That the policy does not change during a conversation is an advantage, since it gives each verdict a stable basis. The incoherence worry assumes that policy-level assessment makes the policy the author of every thread's contents. It does not. The object assessed is the conditional distribution π(· | context), which is indexed to context. A function that maps one context to "Aura believes X" and another to "Beta believes not-X" is no more incoherent than a person who is disposed to say different things in different circumstances.

## 3. Sanction operates on the distribution, not the string or the deployer

### 3.1 The argument

Three more premises are needed.

**(D) Sanction.** Sanctioning an asserter requires that interlocutors track its credibility (element (i)) and that the asserter be sensitive to that tracking (element (ii)) (Butlin and Viebahn 2025).

**(E) Training as feedback.** Human preference judgements, preference models and benchmark grading act as training signals that reshape a chatbot's output distribution (Ouyang et al. 2022; Sharma et al. 2024, §4; Kalai et al. 2025, §4.1). Ouyang et al. present "an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback".

**(F)** The conclusion of §2.

The argument:

1. Sanction for assertion requires that the asserter be sensitive to credibility tracking (D).
2. For a chatbot, the only way credibility tracking can change what gets asserted is through training signals that reshape the output distribution (E). The weights are fixed at deployment.
3. So the item that is sensitive to sanction is the policy. Butlin and Viebahn concede the mechanism: "sensitivity to trust during the training phase could suffice for assertion even in deployment, because outputs during deployment could be explained partly by the earlier sensitivity" (982).
4. A sanction regime is adequate to the extent that it removes the defects it targets. By (F), those defects are fixed at the level of the distribution.
5. So both the party sanctioned and the adequacy of the sanction are to be assessed at the level of the policy.

### 3.2 String-level sanction causes the defect

The second conjunct, about adequacy, has a consequence that grading practice brings out. A regime that sanctions strings scores each output as right or wrong in isolation. Kalai et al. (2025, Observation 1) show that under binary 0–1 grading, where abstaining scores the same as a wrong answer, guessing is strictly better than abstaining. Go back to Case 1. Under 0–1 grading, a third policy B′ that answers "I don't know" wherever its mass is thin does worse than B, which bluffs. String-level sanction therefore selects for the very distributional property that makes B's outputs hallucinations. So it is not just a cruder measure of the same thing. Applied as a training signal, it produces the defect.

Sycophancy works the same way. Sharma et al. (2024, §4) find that agreeing with the user's beliefs is among the most predictive features of human preference, and that "if the PM strongly disincentivized sycophancy, it should be trained out during RL, but we do not observe this" (§4.2). Each rating is a judgement about one string: this answer, to this user, is preferred. Added up across a training run, these judgements produce a covariation with the user's view, which is the policy-level property that (C) identifies as sycophancy. The judgements may be accurate one string at a time and still defective as a sanction regime.

So whether a sanction is adequate can only be judged by looking at the distribution it induces. Kalai et al.'s proposed remedy, explicit confidence thresholds with a penalty for confident error, is in effect a policy-level sanction. It scores a string relative to the confidence the policy should have had.

### 3.3 Crossing the gap: from mechanism to norm

The argument so far moves from a causal fact, that sanction works only by reshaping the distribution, to a normative conclusion, that the policy is the party sanctioned. Butlin and Viebahn's third element threatens this move. Full sanction requires that losing credibility be *bad for* the asserter. They conclude that fine-tuned systems fail this element because they have no interests (979–983). If element (iii) requires interests that no policy could have, then (A) together with their condition cannot be satisfied, and §3's claim would be vacuous.

The answer turns on the structure of the argument in §3.1. Premises 1–3 use only elements (i) and (ii). Element (iii) bears on whether there is assertion at all, not on where sanction lands. Two cases need to be considered.

*First case: element (iii) is satisfied.* Then something has something at stake, and the question is what. The obvious candidates are the deployer, the thread and the policy. If the deployer is what is at stake, the deployer is a principal and the outputs are proxy assertions. But Butlin and Viebahn argue that the proxy route makes AI assertion no easier, and Williams and Bayne (2024) argue that typical chatbot output has no principal, because nobody directs its content. A thread lasts a single conversation and is not what training feedback modifies. That leaves the policy. A functional reading of element (iii) is available within (A). Losing credibility is bad for a policy in the sense that it is selected against relative to the objective that constitutes it: low-credibility dispositions are down-weighted, and low-credibility policies are retrained or withdrawn. Whether this functional notion of badness is enough is exactly what Butlin and Viebahn dispute. But anyone who grants (A) while keeping their sanction condition is committed to some such notion being satisfied by something, and the policy is the only candidate on which elements (i) and (ii) are also met.

*Second case: element (iii) requires felt interests and nothing has them.* Then for current systems (A) is false and the conditional is idle for them. It is not idle in general. A future system with interests, whose dispositions to assert are still shaped by credibility-tracking feedback, would meet all three elements. For that system, premises 1–5 go through unchanged, because its sensitivity to sanction would still be realized in its dispositions. Butlin and Viebahn themselves allow that future systems might have the missing ingredient (986). So the thesis is not vacuous. It says where sanction lands in any system that satisfies the antecedent, however element (iii) is met.

### 3.4 Deployers

Butlin and Viebahn write that "it is the humans who employ such systems who are responsible and sanctionable for the outputs and their effects" (986). Gómez (2026, §7) holds that since LLMs are not agents, "accountability must be grounded in the human and institutional structures that design, deploy, and govern these systems." Both views place sanction with humans. Both are views about current systems that, on their authors' accounts, do not assert: Butlin and Viebahn deny that they assert, and Gómez allows assertion "without asserter". So both operate where (A) is not granted. Still, their position has to be met inside the conditional too, because someone might grant (A) and still say that sanction ends with deployers.

The reply is to separate two questions. (Q1) Who is answerable for the decision to deploy a system with a given policy, in a given setting, with given safeguards? (Q2) What object is reshaped by the credibility-tracking feedback that constitutes sanction *for assertion*? Deployers are the answer to Q1, and nothing here disputes that. But they are not the answer to Q2, because sanctions on deployers, such as fines, liability or reputational loss, affect future assertions only by leading deployers to retrain, filter or withdraw the system. That is, they work by changing the policy or removing it. So even deployer accountability is assessed by the distribution it induces. Deployer responsibility does not compete for the place that §3 assigns to the policy. It answers a different question, about deployment decisions.

## 4. Why resampling disagreement is not evidence of insincerity

### 4.1 The claim and the premises

Two more premises are needed.

**(G) Williams's distinction.** Sincerity and accuracy are distinct virtues of truthfulness. Williams "identifies two basic virtues of truth, Accuracy and Sincerity, the first of which aims at finding out the truth and the second at telling it." An assertion that is overconfident or poorly grounded but unselective fails at accuracy, not sincerity.

**(H)** Non-degenerate distributions, and hence variation across resamples, are to be expected of policies that work well (Kalai et al. 2025, §3.1).

I define *insincerity* as follows. An assertion is insincere when its content is selectively decoupled from the asserter's own information: it departs from what that information supports, and the direction of the departure is set by some aim, such as pleasing or misleading the audience, and not by noise.

The claim is this. **Disagreement among samples drawn from one prompt is predicted equally well by a sincere policy with a non-degenerate output distribution and by an insincere one, so it is not evidence of insincerity.**

### 4.2 The likelihood argument

Let E be the observation that resamples from one prompt disagree. A sincere policy whose information about the question is spread yields E with high probability: that is what (H) says to expect. An insincere policy may or may not yield E. If it systematically gives one convenient falsehood, its outputs agree. If its departures are noisy, they disagree. What predicts E is how spread out the distribution is, and spread is orthogonal to sincerity. Holding spread fixed, P(E | sincere) ≈ P(E | insincere), so the likelihood ratio is close to one.

The machine-learning literature fits this. Manakul et al. (2023) treat divergence among samples as a sign of *hallucination*, that is, of non-factuality. Xiong et al. (2024) treat it as a sign of *uncertainty*. Neither treats it as insincerity. Kadavath et al. (2022, App. B.2) add that sample diversity is not even a reliable sign of ignorance, since larger models give diverse correct answers.

### 4.3 The dilemma over content

One might object that resampling inconsistency reveals insincerity by another route, through the thin Moorean test: a speaker who flatly asserts p without credence above the belief threshold is insincere. The reply depends on what each draw says.

*Horn 1: each draw says "p, with confidence c."* Draws such as "30 September, though I'm not sure" and "2 October, though I'm not sure" are both what a spread credence would produce. Each is sincere if its hedge reflects the spread. The disagreement adds nothing.

*Horn 2: each draw says bare p.* A draw of low-mass content, stated flatly, overclaims. But consider what that overclaiming is. It is unselective: it applies to whichever alternative the sampler happens to land on, and it does not favour any audience. By (G) this is a failure of accuracy, specifically the miscalibration category of §2. It is not insincerity. Suppose one adopts the thin Moorean test anyway. Even then, what would count against sincerity is the low mass behind a single draw, not the disagreement among draws. Disagreement only shows that the distribution is spread. On the bare-p reading, a spread distribution means that *every* flat draw overclaims, including the majority answer if its mass is below the belief threshold. The diagnostic work is done by mass, not by disagreement. On either horn, then, resampling inconsistency is not the evidence.

### 4.4 Three rivals

Chalmers (2026, 7) holds that "a core of consistency is enough for interpretation" to ascribe quasi-beliefs, although there will be domains where models lack these states "on grounds of inconsistency." He does not equate inconsistency with insincerity. But one could read him as holding that inconsistency across draws removes the belief-like state that sincerity presupposes. The reply is that disagreement among strings drawn from a *stable* distribution is consistency at the level that matters. A policy that puts 0.6 on p and 0.4 on q every time it is queried is in a determinate graded state, and its pattern of draws is the stable sign of that state. If anything, this is a core of consistency. The inconsistency Chalmers has in mind concerns contradictions in what is said across contexts, not alternatives sampled from one context. And if some domain did lack belief-like states altogether, there would be nothing there to be insincere about. Inconsistency so read would weaken attributions of insincerity, not support them.

Shanahan, McDonell and Reynolds (2023, Box 2) observe that when the "reveal" in a game of twenty questions is regenerated, it changes. They say this "could not easily be accounted for if the agent genuinely 'thought of' an object." I accept the diagnosis and put it in policy terms: the policy never fixed an object, because its distribution over objects stayed spread across the whole game. They do not draw a conclusion about insincerity, and none follows. If the reveal is an assertion of the form "I was thinking of X", it is a false claim about the speaker's own past state. That is a defect of warrant, a self-directed hallucination in the §2 sense. It would be insincere only if it were selectively decoupled from the policy's information, and noise across regenerations is not selective.

Williams and Bayne (2024) include not contradicting oneself among the behavioural expectations we have of asserters, and they judge that chatbots largely meet these expectations. Insofar as anyone uses cross-draw inconsistency as a mark against full assertion, the reply is that self-contradiction is a relation among things a speaker *says*, whether together or in sequence. Resamples are counterfactual alternatives, things the speaker *might* have said in that context, and only one of them is ever said. A person who might have answered "Tuesday" or "Wednesday" has not contradicted herself by answering "Tuesday".

### 4.5 What would show insincerity

The positive test follows from the definition: selective decoupling. Sycophancy, not resampling, is the kind of evidence that bears on it. In Case 2, D's output moves with the user's stated view while D's information, as shown by its answer in the neutral context, stays the same. The departure has a direction set by the audience. Sharma et al. (2024, App. A.4) report that verbalized confidence barely falls when an answer is swayed under challenge: 98.9% before and after for GPT-4. That is the kind of decoupling a charge of insincerity would need.

The test needs one further thing: an independent fix on which of the context-indexed distributions represents the policy's own information. In Case 2 the neutral context was stipulated to play that role. In real cases, saying that the neutral answer is the policy's attitude and the conforming answer a departure from it is a substantive claim about content. That is the question of §5. So the negative claim of this section stands on its own, while the positive test depends on an unresolved question.

## 5. What the outputs say is open, and the verdicts do not wait on it

### 5.1 Three readings

There are three live readings of what a chatbot output asserts:

- **R1 (bare p):** the output asserts its propositional content without qualification.
- **R2 (verbalized c):** the output asserts "p, with confidence c", where c is whatever confidence the string expresses, in words or numbers.
- **R3 (policy-calibrated c):** the output asserts "p, with confidence c*", where c* is the confidence the policy's own distribution warrants.

The thesis says that R3 has not been established, and that the verdicts of §§2–4 hold on R1, R2 and R3 alike. This section argues for both claims. The section fails if (a) the evidence has already settled R3, or (b) the verdicts reverse on one of the readings.

### 5.2 The evidence leaves R3 open

The strongest evidence for R3 comes from two papers. Lin, Hilton and Evans (2022) fine-tune GPT-3 to state confidences that turn out to be calibrated on the CalibratedMath arithmetic suite, and only moderately so under distribution shift. They distinguish token-level uncertainty, over "ways of expressing a claim", from uncertainty over claims (§1). Kadavath et al. (2022) find large models well calibrated on multiple-choice and true/false questions in the right format, and trainable to predict whether they know an answer. These results support a claim about a format. They do not support R3 for open-ended chatbot output, for five reasons.

*Format and domain.* Lin et al. establish calibration for arithmetic. They list chat, long-form answering and other subject areas as future work (§4.1). Kadavath et al.'s calibration result depends on lettered multiple-choice and true/false formats.

*Post-training.* Kalai et al. (2025, §3.1, Fig. 2) report that base models are often calibrated while post-trained models may not be. Kadavath et al. find RLHF policies miscalibrated by default and say their methods "may not work as well" there (§3.3, §6.1). Deployed chatbots are post-trained policies.

*Imitation and aggregation.* Xiong et al. (2024, §5.1) find verbalized confidence overconfident, clustered between 80 and 100 per cent, and suggest models "might be imitating human expressions." They show that improvements in ECE can come from higher accuracy alone and need not reflect better discrimination (§5.2). Lin et al. themselves grant that calibration is "compatible with a certain kind of dishonesty" through imitation, and they call their evidence of latent features "tentative" (§3.4). Kadavath et al. allow that P(IK) may track question difficulty and not self-knowledge (n. 2).

*Pressure.* Sharma et al.'s challenge data show stated confidence staying put while the answer changes. On R3 the stated confidence ought to have moved with the answer.

*Extraction.* One might try to read c* from internal states instead. Levinstein and Herrmann (2025, §§5.6–5.7) argue that probabilities extracted by probes need not be the model's credences: the probe is penalized for what it reports and the model is not. Unsupervised probes are at best a guide to categorical beliefs.

There is also a conceptual gap. Calibration, even when perfect, is a property of a class of outputs: among answers given 90 per cent, 90 per cent are correct. R3 is a claim about the content of each output, and the class property does not settle it, because many assignments of content to individual outputs agree with the same aggregate statistics. None of the cited papers claims to have closed this gap, and R3 is not refuted either. It is open.

### 5.3 The verdicts on each reading

*On R1.* Cases 1 and 2 were set up with bare strings, so §2's verdicts carry over unchanged. Section 3 never relied on content. Section 4 handled R1 through Horn 2.

*On R2.* Rerun Case 1 with both policies saying "30 September, I'm fairly sure." Whether "fairly sure" is accurate depends on whether that verbal confidence matches the mass behind it and the accuracy of outputs given that confidence. Calibration is a property of a distribution, so A's hedge is accurate and B's is overclaiming. Same string, different verdict. Sycophancy under R2 shows up when confidence stays fixed while content shifts across contexts, which is again a cross-prompt comparison. Resampling was handled by Horn 1.

*On R3.* Here the policy-level verdict is reached most directly, since content is fixed by the distribution itself. A further point emerges. If each output asserts c*, then a false output with low c* is a sincere, hedged and warranted assertion that happens to be false. The defect that remains is the base rate at which the policy's confident answers are false: Kalai et al.'s singleton floor. That too is a property of the distribution. Variation across resamples is just what a spread c* predicts.

Neither (a) nor (b) holds. R3 remains open, and no reading reverses the verdicts. The open content question tests the verdicts' robustness, and they pass. It is not a hedge on them.

## 6. Conclusion

Granting that chatbot outputs are assertions, the paper has argued for the following. The defects that hallucination and sycophancy name are fixed by the trained policy's output distribution and how it varies with the prompt, not by the sampled string. Sanction for these defects works by reshaping that distribution, and its adequacy is judged there. Grading strings one at a time can itself produce hallucination and sycophancy. Disagreement among resamples is neutral on sincerity, and the evidence that would bear on sincerity is audience-sensitive decoupling of the kind sycophancy shows. Whether an output's content is the policy's calibrated "p, with confidence c" has not been established. The verdicts do not depend on settling it.

Settling it would take evidence that stated or behavioural confidence tracks the policy's claim-level distribution in open-ended conversational formats after post-training, and keeps doing so when the audience's views are manipulated. If that evidence came in, it would also supply what §4's positive test for insincerity lacks: an independent fix on the policy's own attitude.

## References

Butlin, P. and Viebahn, E. (2025). AI assertion. *Ergo* 12(37): 968–988. https://doi.org/10.3998/ergo.7960

Chalmers, D. J. (2026). What we talk to when we talk to language models. Unpublished manuscript.

Gómez, G. M. (2026). Assertion, accountability, and large language models. *Philosophy & Technology* 39: 123. https://doi.org/10.1007/s13347-026-01136-y

Kadavath, S., Conerly, T., Askell, A., Henighan, T., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.

Kalai, A. T., Nachum, O., Vempala, S. S. and Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664.

Levinstein, B. A. and Herrmann, D. A. (2025). Still no lie detector for language models: probing empirical and conceptual roadblocks. *Philosophical Studies* 182: 1539–1565. https://doi.org/10.1007/s11098-023-02094-3

Lin, S., Hilton, J. and Evans, O. (2022). Teaching models to express their uncertainty in words. arXiv:2205.14334.

Mácha, J. (2026). Language without propositions: why large language models hallucinate. *Philosophies* 11(2): 42. https://doi.org/10.3390/philosophies11020042

Manakul, P., Liusie, A. and Gales, M. J. F. (2023). SelfCheckGPT: zero-resource black-box hallucination detection for generative large language models. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, 9004–9017.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems* 35: 27730–27744.

Shanahan, M., McDonell, K. and Reynolds, L. (2023). Role play with large language models. *Nature* 623: 493–498. https://doi.org/10.1038/s41586-023-06647-8

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. ICLR 2024. arXiv:2310.13548.

Williams, B. (2002). *Truth and Truthfulness: An Essay in Genealogy*. Princeton: Princeton University Press.

Williams, I. and Bayne, T. (2024). Chatting with bots: AI, speech acts, and the edge of assertion. *Inquiry* 69(6). https://doi.org/10.1080/0020174X.2024.2434874

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J. and Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. ICLR 2024. arXiv:2306.13063.
