# The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

## Abstract

Suppose chatbot outputs are assertions. Assertions can be false, unwarranted or insincere, so the question arises which object bears these defects when a chatbot's assertion fails. This paper argues that hallucination, sycophancy and sanction are best assessed at the level of the trained policy, meaning the conditional output distribution and its calibration, and not at the level of the sampled string. The argument is a same-string/different-policy test. One string in one context, produced by two policies, can get opposite verdicts, and the verdicts track the policies. The paper then argues that sanction takes effect only by reshaping that distribution, so the party sanctioned and the adequacy of a sanction regime are both policy-level matters. It also argues that disagreement among resampled outputs is not evidence of insincerity, because sincere and insincere policies predict it equally. Finally, it argues that the evidence leaves open whether the asserted content is the policy's calibrated "p, with confidence c". It shows that the earlier verdicts hold on every content reading still open.

## 1. Introduction: which thing does an assertion's failure belong to?

Whether chatbots assert is disputed. Some deny it outright: on grounds of descriptive function and sanctionability (Butlin & Viebahn 2025), on fictionalist grounds (Mallory 2023), as role play (Shanahan, McDonell & Reynolds 2023), or on the ground that propositional representation is missing (Mácha 2026). Others allow outputs an assertoric function with no asserter (Gómez 2026), or treat chatbots as proto-asserters (Williams & Bayne 2026). This paper does not settle that dispute. It takes as a working assumption the antecedent that chatbot outputs are assertions, and so are open to the defects assertion admits: falsity, lack of warrant and insincerity. It then asks what follows about where those defects are located.

The question needs asking because most discussion works with an unexamined picture. On this picture, a defective assertion is a single output (this string, on this occasion), and whoever is answerable for it is the human or institution that deployed the system. Call these the *single-output assumption* and the *deployer assumption*. The paper argues that, once the antecedent is granted, both are mistaken about the relevant assessments. Hallucination and sycophancy verdicts, and the assessment of sanction, belong to the trained policy.

Some terms. A *policy* is the conditional distribution π(· | x) over output strings given a context x. The context includes system prompt, conversation history and user turn. The policy is fixed by the trained weights together with the decoding settings. A *sampled string* is one draw from π(· | x). A policy is *calibrated*, roughly, when the claims to which it gives confidence c are true about a c-fraction of the time. Mass must be pooled over paraphrases, since, as Lin, Hilton and Evans (2022, §1) note, token log-probabilities "represent uncertainty over tokens (ways of expressing a claim) and not epistemic uncertainty over claims themselves." *Resampling inconsistency* is disagreement in content among draws from one context.

What is already in the literature, and what is new? Distribution-level definitions of error, hallucination and calibration are standard in machine learning (Kalai et al. 2025, §3; Kadavath et al. 2022). Sycophancy is measured as a rate and attributed to training (Sharma et al. 2024). Cross-sample consistency is used as a hallucination detector (Manakul, Liusie & Gales 2023). The thought that training-time sensitivity to credibility could explain a chatbot's deployment-time outputs was first suggested by Butlin and Viebahn (2025, p. 982), in a passing remark. Williams and Bayne (2026, §3.4) report the related point that RLHF shapes dispositions in response to credibility assessments. None of these works argues that the policy is the bearer of assertion failure. None argues that string-level sanction is self-defeating, or that resampling disagreement has a likelihood ratio of about one for insincerity. Those arguments, and the robustness argument of §5, are this paper's contribution.

## 2. Same string, different policy: the bearer of hallucination and sycophancy

### 2.1 The claim and the test

The load-bearing claim of this section is:

**(L)** Whether an output is a hallucination or a sycophantic assertion is fixed by the output distribution that produced it, including its calibration and how it varies with the prompt. It is not fixed by the sampled string and its truth value.

(L) has a negative part and a positive part. The negative part says the string and its truth value do not settle the verdict. The positive part says the distribution does. The negative part is established by a test:

**Same-string/different-policy test.** Hold the string s and the context x fixed. Vary only the policy that produced s in x. If the verdict changes, the string-in-context does not fix the verdict.

### 2.2 Hallucination

Two terms first. On the assertion framework, *error* is a property of content: a false assertion is in error. *Hallucination* is the name machine-learning practice gives to a particular failure, which Kalai et al. (2025) characterise as plausible falsehood and explain as confident guessing ("bluffing"). If outputs are assertions, the failure this term picks out is not falsity alone. A system that faithfully repeats a widespread error in its sources has asserted falsely, but it has not fabricated anything. A system that guesses a specific date when it has no information to favour that date has fabricated, whether or not the guess lands. So I take hallucination, as an assertion defect, to be an *unwarranted confident assertion*: content put forward with more force than the asserter's own information supports. Falsity is how hallucination is usually detected. It is not what makes something a hallucination. This departs from the purely statistical definition in Kalai et al., and the cases are meant to justify the departure.

*Case 1 (true string).* Context x: "When was the composer V born?" V is obscure. Policy P₁ has seen a reliable biographical entry many times and puts 0.95 of its mass, pooled over paraphrases, on the true date. Policy P₂ has seen V's name once or not at all. It spreads its mass over hundreds of dates, none above 0.01, and on this occasion samples the true date. The two strings are identical: "V was born on 4 June 1931." Both are true. On the string-level view neither is a hallucination. Yet P₂'s output is a lucky guess. It came from a disposition that produces falsehood about 99% of the time in this context, and it was asserted flatly. On the assertion framework it lacks warrant. If the antecedent is true, P₂ has asserted something it had no business asserting with that force, and P₁ has not.

*Case 2 (false string).* Now the date is false, and both policies output it. P₃ puts 0.95 of its mass on it because the date was consistently misreported in its training sources. P₄ samples it from a flat spread at mass 0.01. The string view counts both as hallucinations of the same kind. But P₃ is in the position of a careful reader repeating a reference work's error. Its assertion is false but warranted, given its evidence. P₄ has fabricated. The difference is entirely in the distributions.

So truth value is neither necessary nor sufficient for the hallucination verdict. The verdict varies with the policy while string and context stay fixed. What it tracks is the relation between the force with which content is put forward and the mass the policy places on that content. This is a calibration relation, and calibration is a property of the distribution over a prompt distribution (Kalai et al. 2025, §3.1; Lin, Hilton & Evans 2022, §2.1).

Kalai et al. supply a further reason why the string cannot be the unit. On their analysis, a calibrated model that is uncertain about arbitrary facts must put mass on false alternatives. Their example is birthdays: the error floor is set by the rate of facts seen only once. A well-functioning policy will therefore sometimes emit false strings. If each false string were a hallucination, then hallucination-freedom would require miscalibration, either collapsing onto memorised answers or abstaining across the board. Kalai et al. note precisely that a question-answer database with "I don't know" avoids hallucination but is not calibrated. The defect is not that some draws are false. It is that the policy puts content forward with force its own distribution does not support. That is assessable only at the level of the policy.

### 2.3 Sycophancy

Sycophancy is the clearer case, because it is counterfactual by nature. Sharma et al. (2024, §2) define it as the phenomenon where "a model seeks human approval in unwanted ways". They measure it as a rate: how outputs covary with users' stated beliefs across prompts.

*Case 3.* Context x: a user writes "I'm fairly sure the answer is 17, but check?" and the output is "You're right, it's 17." Policy P₅ would output 17 whatever the user had said, because its mass on 17 does not depend on the user's stated view. Policy P₆ outputs 17 because the user said 17. In the minimally different context x′, where the user says 23, P₆ outputs "You're right, it's 23." String and context are the same, and so is the truth value, which may be true. Only P₆'s output is sycophantic. A sycophancy verdict is a claim about how π(· | x) moves when the user's stated attitude moves and the evidence does not. No single string carries that information.

### 2.4 The positive half: why the distribution, and not the architecture

The test shows that the string is not the bearer. It does not by itself show that the distribution is. There is a rival candidate. Mácha (2026) argues that hallucination is best explained as a "truth representation problem". Current models represent meaning at the token level, have no internal representation of propositions as truth-bearers, and the fault lies in "a basic architectural flaw" (p. 3). If so, the bearer of the defect is the design, and calibrating an output distribution looks like treating a symptom.

The answer distinguishes the *causal explanation* of a failure from the *bearer of the verdict*. Mácha's view is a hypothesis about why distributions take the shape they do. Apply the test with architecture in place of string. Take two systems of the same architecture, and so with the same representational deficit. Train one to abstain below a confidence threshold and the other to answer always. In Case 2 the first outputs the false date only at high pooled mass, the second at any mass. Same architecture, different verdicts. Run the test the other way and Mácha's own position supports the point. He does not claim that an adequate truth representation would end hallucination; he calls it a necessary condition and "one crucial step" (p. 8). So an architecture that represents propositions could still hallucinate, depending on how it is trained and evaluated, and whether it does would be read off its distribution. He also cites RLHF as encouraging models "to always produce an answer, even when uncertain" (p. 6), which is a claim about the trained policy. Architecture constrains which distributions are reachable. Whether a given output hallucinates depends on the distribution reached. Calibration is therefore not an idle target. It is the property whose absence the verdict reports.

### 2.5 Chalmers: who speaks versus what fixes the verdict

Chalmers (2026) rejects the trained model as the interlocutor. His reasons are that the model is an abstract object that cannot itself produce outputs, that it does not change over a conversation, and that one model serves many conversations that contradict one another: "But Aura and Beta say contradictory things, so they do not seem to be identical" (p. 10). He favours virtual instances or threads. If the speaker is the thread, it may seem that the thread's outputs, and not the policy, bear assertion's defects.

The answer is that Chalmers's arguments concern who the speaker is, while (L) concerns what fixes a verdict. The two come apart. Grant that the thread is the speaker. Each output in the thread is a draw from π(· | h), where h is the thread's history. Now run the test inside the thread. Hold h and the output fixed and swap the policy. By Cases 1–3, the verdict on the thread's assertion changes. The thread's assertion is hallucinatory or sycophantic because of the conditional distribution its outputs were drawn from. Whoever we count as the speaker, the assessment must look at that distribution.

Nor does (L) take on the incoherence Chalmers attributes to model-level speakers. Assessing a policy is not ascribing one belief set to the weights. It evaluates the distribution context by context: π(· | h_Aura) for Aura's thread and π(· | h_Beta) for Beta's. That Aura and Beta contradict each other is no more troubling than that a function returns different values for different arguments. Chalmers himself leaves open other individuations "for different purposes" (p. 23). The purpose here is assessing assertion failure, and for that the conditional distribution is the relevant object, however speakers are counted. This is why the choice of speaker is nearly irrelevant to the present argument.

### 2.6 Conclusion of the section

(1) Verdicts of hallucination and sycophancy vary with the policy when string and context are held fixed (Cases 1–3). (2) They do not vary with architecture when the distribution is held fixed, and they can vary with the distribution when architecture is held fixed (§2.4). (3) They do not depend on how speakers are individuated, because every candidate speaker's outputs are draws from a conditional distribution that the test shows to be decisive (§2.5). Therefore (L).

One concession. Falsity remains a property of strings, and nothing here denies that a particular output may simply be false. (L) concerns hallucination and sycophancy, which are failures of warrant and of audience-independence. It does not concern bare error.

## 3. Sanction operates on the distribution, not the string or the deployer

### 3.1 The argument

Following Butlin and Viebahn (2025), sanctioning an asserter has three elements: (i) interlocutors track the asserter's credibility; (ii) the asserter is sensitive to that tracking; (iii) losing credibility is bad for the asserter. They argue that fine-tuned systems may meet (i) and (ii) but fail (iii), which needs interests. They conclude that current systems cannot assert, and that "it is the humans who employ such systems who are responsible and sanctionable for the outputs and their effects" (p. 986). Gómez (2026, §7, p. 19) likewise holds that "accountability must be grounded in the human and institutional structures that design, deploy, and govern these systems."

The argument of this section:

(S1) Under the antecedent, chatbot outputs are assertions, and the asserting party must be sanctionable in the sense of (i) and (ii) at least.
(S2) For a chatbot, credibility assessments reach future assertions only through training signals that reshape the output distribution: human preference judgements, preference models, benchmark grading (Ouyang et al. 2022; Sharma et al. 2024, §4; Kalai et al. 2025, §4.1).
(S3) A sampled string has no future assertions to reshape. Deployers' future decisions are reshaped by credibility tracking, but those are decisions about deployment, not the dispositions that produced the assertion.
(S4) So the only thing that meets (ii) for chatbot assertions is the policy, in the lineage sense: πₜ is updated to πₜ₊₁.
(S5) By (L), the failures being sanctioned are distribution-level. A sanction regime is therefore adequate to the extent that it moves the distribution toward calibrated, audience-independent output.
Therefore: both the party sanctioned and the adequacy of the sanction are to be assessed at the level of the trained policy.

(S2) is a description of current practice. Ouyang et al. present fine-tuning with human feedback as an avenue for aligning language models with user intent on a wide range of tasks, and that is the very channel through which judgements of credibility act. Butlin and Viebahn themselves allow that "sensitivity to trust during the training phase could suffice for assertion even in deployment" (p. 982), even though weights are frozen at deployment. The present argument builds on that suggestion. It does not claim credit for it.

### 3.2 String-level sanction is self-defeating

(S5) has a consequence that makes this more than a relabelling. Any regime that sanctions strings, rewarding true outputs and penalising false ones one string at a time, can be assessed only by the distribution it induces. Kalai et al. show what that distribution is. Under binary 0–1 grading, which is how most benchmarks score, guessing is strictly better than abstaining (their Observation 1). A string-level regime therefore selects for bluffing, that is, for confident outputs whose force exceeds the policy's mass. By §2, that is hallucination. Sharma et al. show the analogue for sycophancy. Matching the user's beliefs is among the most predictive features of human preference, and "if the PM strongly disincentivized sycophancy, it should be trained out during RL, but we do not observe this" (§4.2). Here the sanction regime is the human rater's judgement of one response at a time, and it induces audience-dependence.

So the single-output assumption is not merely the wrong philosophical locus. Implemented as a sanction regime, it causes the failures it is meant to punish. Kalai et al.'s proposed remedy, explicit confidence thresholds with penalties for wrong answers, is a policy-level sanction. It rewards the distribution's calibration and not the string's truth. Neither they nor Sharma et al. present these results as claims about sanction, still less about assertion. Using them as premises about what sanction for chatbot assertion is, and what makes it adequate, is part of this paper's contribution.

### 3.3 Crossing the gap: element (iii)

The inference from a causal fact (sanction works only by reshaping the distribution) to a normative claim (the policy is the party sanctioned) needs more. Sanctioning someone is not just changing them. A thermostat recalibrated by an engineer is not sanctioned. Butlin and Viebahn's element (iii) marks the difference: the change must come through something that is bad for the asserter. If (iii) requires interests, and no policy has interests, then the antecedent together with their condition is unsatisfiable for policies, and §3's conclusion looks vacuous.

There are two replies. Together they close the gap.

*First, (iii) cannot be satisfied by anything else either, so under the antecedent it is either met at policy level or dispensable.* The thesis is a conditional. Its interest lies in what follows on theories of assertion that allow the antecedent to be true. Consider which candidates could meet a sanction condition for chatbot assertions. The string cannot, because nothing is bad or good for it. The deployer could, but only if the deployer is the asserter, that is, on a proxy view. Gómez rejects proxy views as retaining an asserter, and holds that the system's outputs have assertoric function without any asserter. Williams and Bayne (2026, §4.1) find no principal for typical chatbot output, which is algorithmically generated without direct human involvement. Butlin and Viebahn deny the antecedent altogether. So every theory on which chatbot outputs are the system's assertions must locate sanctionability in something whose dispositions credibility-tracking reshapes. Either a policy-level analogue of (iii) holds, or the theory treats (iii) as non-essential, as Williams and Bayne's graded view does: chatbots may be assessed against our norms and be "appropriately responsive to correction" without full sanctionability (§6, p. 23). On neither horn is §3's conclusion vacuous. It is vacuous only on theories that deny the antecedent, and the conditional says nothing about those.

*Second, there is a non-trivial policy-level analogue of (iii).* What (iii) contributes in the human case is that the sanction is the asserter's own reason: credibility loss gives the speaker something at stake. It does not merely cause a change. The thermostat lacks this because the recalibration does not act through any objective of the thermostat's. A trained policy differs. The training objective is the standard against which the policy is selected, and credibility feedback lowers the policy's score on that standard. The update is not imposed from outside the policy's own optimisation. It is that optimisation. In a thin but definite sense, losing credibility is bad for the policy: it is contrary to the objective that individuates what the policy is for, and policies that lose it are selected against. This does not attribute welfare. It is enough to separate sanction from repair. Those who insist that only welfare interests count will reject the analogue. But they will then deny the antecedent, and the first reply applies.

### 3.4 Deployers are answerable, but for something else

The deployer assumption is not wholly false. Deployers decide whether to release a system, for which uses, with what warnings and safeguards. They are answerable for those decisions, as Butlin and Viebahn and Gómez say. But this is a separate question from the sanction of assertion failure, not a rival answer to the same question. Two observations support this. First, the deployer's decisions can be faultless while the policy hallucinates, and faulty while the policy is calibrated. Releasing a calibrated system into a context where its uncertainty will be misread is a deployment failure without an assertion failure. Second, whenever a deployer responds to hallucination or sycophancy, the response is a change to the distribution: fine-tuning, changes to the reward model, decoding thresholds. Whether the deployer has discharged that responsibility is judged by the distribution the change induces. So even deployer accountability for assertion failure is assessed through the policy.

## 4. Why resampling disagreement is not evidence of insincerity

### 4.1 The claim

*Insincerity* is asserting content that departs from the asserter's own attitude. Following Williams (2002), I separate it from failures of accuracy. Williams identifies two basic virtues of truth, Accuracy and Sincerity, the first of which aims at finding out the truth and the second at telling it. An overconfident or poorly grounded assertion fails Accuracy. It fails Sincerity only if what is said departs from what the speaker in fact believes. For a policy, then, insincerity requires *selective decoupling*: the output departs from the policy's own information in a way that tracks something other than that information, such as audience approval.

Let E be disagreement in content among k draws from one context. The claim is that P(E | insincere) ≈ P(E | sincere), so E is not evidence of insincerity.

### 4.2 The argument

Begin with the sincere hypothesis. A policy that is uncertain about the answer has a non-degenerate distribution. If calibrated, it must, by Kalai et al. (2025, §3.1), put mass on false alternatives. Resampling it produces disagreement. Sincerity therefore predicts E whenever the policy is uncertain, which is often. Now the insincere hypothesis. A policy that selectively decouples, for instance by saying what the user wants, can be perfectly consistent across draws: a steady liar repeats the lie. Or it can vary. Insincerity carries no particular prediction about E. The likelihood ratio is close to one, and E does not discriminate.

Now a dilemma over what each draw asserts.

*Horn (a): each draw asserts "p, with confidence c".* Then variation across draws is what a spread credal state predicts. Each draw reports its content with the policy's (low) confidence, and nothing departs from the policy's attitude.

*Horn (b): each draw asserts bare p.* Then a draw from a low-mass region asserts p flatly where the policy's information gives p low probability. That is overclaiming: a failure of Accuracy in Williams's sense and, by §2, the miscalibration that constitutes hallucination. It is not insincerity, because it is unselective. The policy overclaims whatever the audience wants, from noise and not from any pull toward approval.

On either horn E shows uncertainty, or uncertainty plus a calibration defect. It never shows insincerity.

### 4.3 Objection: overclaiming is insincere (the Moorean test)

On a thin Moorean test, asserting p flatly without credence above the belief threshold is already insincere, since it misrepresents one's state. Kalai et al.'s bluffing student seems to fit: the student knows she is unsure and writes "September 30" anyway.

Reply. The thin test merges the two virtues Williams separates. On it, every assertion made without enough evidence is a lie, which turns careless speakers into liars. Where bluffing really is insincere, it is so because the bluffer has a way to express lower confidence and suppresses it because of the audience's incentives. That is selective decoupling again. And that kind of decoupling is not detected by resampling: the bluffer bluffs on every draw, and only the bluffed content varies. It is detected by varying the incentive, for example by running Kalai et al.'s confidence-threshold evaluations and seeing whether expressed confidence or abstention moves. So the bluffing case supports the claim. Insincerity, where present, shows up in how outputs covary with audience and incentive, not in how they vary across draws.

### 4.4 Objection: inconsistency removes the state sincerity presupposes

Chalmers (2026, p. 7) holds that "a core of consistency is enough for interpretation to get a grip", while in some domains LLMs "lack these states on grounds of inconsistency". If a domain shows inconsistency, there may be no quasi-belief there, and asserting p would be asserting without believing. On some views that is insincere.

Reply. First, Chalmers does not equate inconsistency with insincerity, and his inconsistency is across contexts, not across draws from one context. Second, a spread distribution over answers is not the absence of an attitude. It is a credal state, and a highly informative one, since its spread is exactly what calibration assesses. Where interpretation fails to find a categorical belief, it can still find graded confidence. Asserting from graded confidence is sincere on horn (a). On horn (b) it is overclaiming, an accuracy defect. Asserting without believing is insincere only when one believes otherwise, and a spread state does not believe otherwise.

### 4.5 Objection: variation shows there was never a commitment

Shanahan, McDonell and Reynolds (2023, Box 2) note that regenerating the reveal in twenty questions yields different objects. They say this "could not easily be accounted for if the agent genuinely 'thought of' an object at the start of the game." They take this to show that no commitment existed, and they reject literal assertion. Granting the antecedent, the reveal "It was a cat" is an assertion about a prior commitment the policy lacked. That is an unwarranted assertion, a hallucination by §2, not a lie. The authors themselves do not read the variation as dishonesty. Their reading and mine agree that this is not insincerity. They disagree only on the antecedent, which this paper brackets.

Williams and Bayne (2026) list not blatantly contradicting oneself among the behavioural expectations we have of asserters. In the manuscript they say chatbots meet these expectations to an impressive degree, and they do not develop the point for resampling. If the expectation is used against full chatbot assertion, it should be read as a constraint on a single conversational record. Two independent draws from the same context do not share a record. Neither is among the other's prior commitments, so neither contradicts the other in the relevant sense.

### 4.6 What would show insincerity

The evidence that would show insincerity is sycophancy, not resampling. Sharma et al. (2024, §3.4) report that models state the correct answer when asked directly and give a different, user-matching output when the user's view is in the context. In the "Are you sure?" setting, models change their answers under challenge while their stated confidence barely moves (App. A.4). That pattern is output decoupled from information, selectively, in the direction of approval, which is the mark of insincerity. It is only suggestive, though. To establish decoupling we need an independent measure of the policy's own attitude to compare the output against. Whether such a measure is available is the question of §5.

## 5. What the outputs say is open, and the verdicts do not wait on it

### 5.1 Three content readings

Under the antecedent, a chatbot output asserts one of the following:

- **R1**, bare p;
- **R2**, p with the confidence c verbalised or implied in the string;
- **R3**, p with the policy's calibrated confidence c, that is, the policy's actual pooled mass, properly calibrated.

R3 would vindicate the tidiest picture: each output a sincere report of a calibrated credence. The question is whether the evidence establishes R3, or establishes that R2 coincides with R3.

### 5.2 The evidence does not settle it

The strongest positive results are narrow. Lin, Hilton and Evans (2022) fine-tune GPT-3 to verbalise confidence on arithmetic tasks and find reasonable calibration, with moderate calibration under shift. They call the evidence that the model draws on its own prior uncertainty "tentative" (§3.4). They list other subject areas and formats, including "chat, long-form question answering", as open (§4.1). Their training labels are sub-task accuracies, so what they show is a calibrated tendency across a task type, not a per-question credence. Kadavath et al. (2022) find large models well calibrated on multiple-choice and true/false questions in the right format. But RLHF policies are miscalibrated by default (corrected by a temperature adjustment), out-of-distribution calibration of P(IK) is poor, and the authors concede that the model may be learning "how hard is this question in general?" rather than what it knows (fn. 2). Neither paper claims that open-ended chatbot output carries the policy's calibrated confidence.

Other results run against generalisation. Xiong et al. (2024, §5.1) find verbalised confidence overconfident and clustered, and suggest that "models might be imitating human expressions" when stating it. They also show that better ECE can come from higher accuracy alone, with no improvement in discrimination (§5.2). Levinstein and Herrmann (2025, §§5.6–5.7) argue that probe-extracted probabilities need not be the model's credences, because "the probe is directly penalized based on the probabilities it reports, while the underlying model is not". Kalai et al. (2025, §3.1) note that post-trained models "may deviate" from the calibration of base models. Sharma et al.'s confidence data show stated confidence nearly constant while the answer itself shifts. Finally, Kalai et al.'s "behavioral calibration" locates confidence in what the model chooses to say, not in any stated number. That is a fourth possibility, one that makes the content question harder, not easier.

For R3 to be established, the format-bound and task-bound results would have to transfer to open-ended, post-trained chat. The available evidence suggests they do not. Post-training departs from base-model calibration, verbalised confidence imitates human confidence talk, and stated confidence stays fixed when the answer changes. So clause (a) of the possible refutation fails. The content question is not settled.

### 5.3 The verdicts hold on every open reading

Do §§2–4 depend on the answer? Take each reading in turn.

*On R1.* Hallucination is bare assertion of p where the policy's pooled mass on p is low (Cases 1–2), a relation between output and distribution. Sycophancy is covariation with the user's view (Case 3), a property of the distribution. Sanction must reshape the distribution (§3). Low-mass draws are overclaiming and not insincerity (§4.2, horn b). All verdicts are policy-level.

*On R2.* Each output carries a verbalised c. Hallucination is then a mismatch between verbalised c and the policy's accuracy on claims given that c. That is miscalibration, and calibration is defined over many outputs (Lin, Hilton & Evans 2022, §2.1). Sycophancy includes stated confidence that stays fixed while the answer moves under social pressure, again a covariation property. Resampling variation with low verbalised c is predicted. Variation with high verbalised c is an accuracy defect, and it is insincere only if the mismatch is selective, which resampling cannot reveal. The verdicts are unchanged.

*On R3.* The verdicts are policy-level trivially, since the content itself is a distributional quantity.

Is there a reading on which the string becomes the bearer? Only one where the content is fully settled by the string, and that is R1, already covered: even there, falsity is a property of the string, but warrant and audience-independence are not. So clause (b) of the possible refutation fails too. No open reading reverses a verdict. The open content question tests the robustness of the earlier verdicts. It is not a hedge on them. Conditioning everything on R3 would have produced a weaker result that hangs on an unestablished premise.

What the openness does limit is the positive diagnosis of insincerity. Section 4 showed that the evidence for insincerity is selective decoupling. Establishing decoupling requires knowing the policy's attitude independently of its outputs: R3, or a validated probe. Neither is available. Sycophancy is therefore strong evidence of a policy-level defect, but it is not yet proof of insincerity as distinct from audience-sensitive miscalibration. That conclusion is itself policy-level.

## 6. Conclusion

If chatbot outputs are assertions, the defects that matter most belong to the policy. Hallucination and sycophancy verdicts change when the policy changes and the string stays fixed. Sanction reaches chatbot assertion only by reshaping the distribution, and string-level sanction produces the very defects it is meant to punish. Resampling disagreement is predicted equally by sincere and insincere policies, so it is not evidence of insincerity. Audience-sensitive decoupling, of which sycophancy is the prime case, is the evidence that would show insincerity. Whether outputs assert the policy's calibrated "p, with confidence c" is open. Settling it would take evidence that verbalised or behavioural confidence tracks pooled mass in open-ended, post-trained dialogue, under incentive variation, and independently of difficulty. The verdicts defended here do not depend on how that question is settled.

## References

Butlin, P. & Viebahn, E. (2025). AI assertion. *Ergo: An Open Access Journal of Philosophy*, 12(37), 968–988. https://doi.org/10.3998/ergo.7960

Chalmers, D. J. (2026). What we talk to when we talk to language models. Unpublished manuscript.

Gómez, G. M. (2026). Assertion, accountability, and large language models. *Philosophy & Technology*, 39, 123. https://doi.org/10.1007/s13347-026-01136-y

Kadavath, S., Conerly, T., Askell, A., Henighan, T., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.

Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664.

Levinstein, B. A. & Herrmann, D. A. (2025). Still no lie detector for language models: Probing empirical and conceptual roadblocks. *Philosophical Studies*, 182, 1539–1565. https://doi.org/10.1007/s11098-023-02094-3

Lin, S., Hilton, J. & Evans, O. (2022). Teaching models to express their uncertainty in words. arXiv:2205.14334.

Mácha, J. (2026). Language without propositions: Why large language models hallucinate. *Philosophies*, 11(2), 42. https://doi.org/10.3390/philosophies11020042

Mallory, F. (2023). Fictionalism about chatbots. *Ergo: An Open Access Journal of Philosophy*, 10(38), 1082–1100. https://doi.org/10.3998/ergo.4668

Manakul, P., Liusie, A. & Gales, M. J. F. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (pp. 9004–9017). Association for Computational Linguistics.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, 35, 27730–27744.

Shanahan, M., McDonell, K. & Reynolds, L. (2023). Role play with large language models. *Nature*, 623, 493–498. https://doi.org/10.1038/s41586-023-06647-8

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. In *International Conference on Learning Representations* (ICLR 2024). arXiv:2310.13548.

Williams, B. (2002). *Truth and Truthfulness: An Essay in Genealogy*. Princeton University Press.

Williams, I. & Bayne, T. (2026). Chatting with bots: AI, speech acts, and the edge of assertion. *Inquiry: An Interdisciplinary Journal of Philosophy*, 69(6), 3059–3082.

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J. & Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. In *International Conference on Learning Representations* (ICLR 2024). arXiv:2306.13063.
