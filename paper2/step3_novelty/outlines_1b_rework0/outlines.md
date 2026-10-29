# Outlines — outlines_1b_rework0

**Thesis (fixed):** If chatbot outputs are assertions, then hallucination, sycophancy and sanction are best assessed at the level of the trained policy (the output distribution and its calibration), not the sampled string, and resampling inconsistency is not evidence of insincerity. Whether the asserted content is the policy's calibrated 'p, with confidence c' is not established.

Nothing here is ranked and nothing is scored. The outlines were written blind to each other, and the flags below each one are computed from its own dependency ledger — no model judged coherence. Read the outlines first; the divergence section at the end is only useful once you have.


## Addresses to check

Every position the outlines name as a refuter. Nothing in this pipeline can verify that these people hold these views; this is the list to run your eye down first.

| Where | Position |
|---|---|
| O0§3 | Butlin & Viebahn 2025 (Ergo 12, conclusion) write that it is the humans who employ such systems who are responsible and sanctionable for the outputs and their effects. They say this of current systems… |
| O0§4 | Chalmers 2026 holds that a core of consistency is what lets interpretation ascribe quasi-beliefs, and that in domains where a model is inconsistent it lacks those states. This is a rival on what incon… |
| O0§5 | Lin, Hilton & Evans 2022 (Teaching models to express uncertainty in words) report that a fine-tuned GPT-3's verbalized confidence maps to well-calibrated probabilities on CalibratedMath arithmetic tas… |
| O0§2 | Mácha 2026 (Philosophies 11(2)) holds that hallucination is best explained by an architectural deficit, namely that current models have no internal representation of propositions as truth-bearers. On … |


## Outline 0 — The Unit of Assertion Failure: Assessing Chatbot Hallucination, Sycophancy and Sanction at the Level of the Policy

*Grant the antecedent that chatbot outputs are assertions and ask which object bears assertion's defects; use a same-string/different-policy test to show the policy does (about a third of the words go to this load-bearing step), extend it to sanction and then to sincerity, and finish by showing these verdicts survive every content reading the evidence leaves open, including the unsettled 'p, with confidence c' reading.*

- **Surprise.** A specialist would expect the policy-level move to be argued from the metaphysics of the speaker (against Chalmers's thread or instance view). Here it is argued from a same-string/different-policy test that makes the choice of speaker nearly irrelevant, and the ML results (Kalai on grading, Sharma on preference training) are used as premises about what sanction is, so that string-level grading is shown to cause hallucination. A second surprise is that sycophancy, not resampling, is the evidence that would show insincerity.
- **Commitment.** The outline commits to the string not being the unit of assessment even granting that every output is an assertion. It commits to sanction being a policy-level matter that deployer responsibility cannot replace, and to resampling disagreement having a likelihood ratio of about one for insincerity. It also commits to the open content question being a robustness test of these verdicts, not a hedge on them, so a cautious version that conditioned everything on calibrated 'p, with confidence c' would be the weaker paper.
- **Gap.** §3, abductive: §3 moves from a causal fact (sanction works only by reshaping the output distribution) to a normative claim (the policy is the party sanctioned, and the sanction's adequacy is assessable there). This goes through only if the antecedent 'outputs are assertions' is read with a sanction concept on which credibility-tracking feedback onto the asserter's dispositions suffices, or on which the training objective gives the policy something at stake. Butlin & Viebahn's third element, that losing credibility be bad for the asserter, must then be met at policy level or be dispensable. If it requires interests that no policy has, the antecedent plus their condition is unsatisfiable and §3's claim is vacuous. A further requirement is that deployer responsibility is not an alternative locus for the same assessment, but a separate question about deployment decisions.
- **Arrives at.** §5
- **Load-bearing.** Whether an output is a hallucination or a sycophantic assertion is fixed by the output distribution that produced it, including its calibration and how it varies with the prompt, not by the sampled string and its truth value.
- **Shape.** 4 substantive sections, plus frame

| § | Establishes | Refuted by / address | Takes as given |
|---|---|---|---|
| 1 | *Introduction: which thing does an assertion's failure belong to?* | — | — |
| 2 | Whether an output is a hallucination or a sycophantic assertion is fixed by the output distribution that produced it, including its calibration and how it varie… | Fails if a hallucination or sycophancy verdict is settled by the sampled string alone (its match to the facts …<br>*Mácha 2026 (Philosophies 11(2)) holds that hallucination is best explained by an architectural deficit, namely…* | assumed: Chatbot outputs are assertions, so each is open to the defec…; assumed: Error, hallucination and calibration are well defined as pro…; assumed: Sycophancy is a regularity in how outputs covary with the us… |
| 3 | Sanction for hallucination and sycophancy takes effect only by changing the output distribution, so both the party sanctioned and the adequacy of the sanction a… | Fails if sanction for chatbot outputs terminates in the deploying humans and institutions rather than in anyth…<br>*Butlin & Viebahn 2025 (Ergo 12, conclusion) write that it is the humans who employ such systems who are respon…* | §2; assumed: Chatbot outputs are assertions, so each is open to the defec…; assumed: Sanction of an asserter requires that interlocutors track it…; assumed: Human preference judgements, preference models and benchmark… |
| 4 | Disagreement among samples drawn from one prompt is predicted equally by a sincere policy with a non-degenerate output distribution and by an insincere one, so … | Fails if cross-draw inconsistency removes the belief-like state that sincerity presupposes, so that asserting …<br>*Chalmers 2026 holds that a core of consistency is what lets interpretation ascribe quasi-beliefs, and that in …* | §2; assumed: Chatbot outputs are assertions, so each is open to the defec…; assumed: Sincerity (saying what one believes) and accuracy (taking ca…; assumed: A calibrated model that is uncertain about arbitrary facts m… |
| 5 | If chatbot outputs are assertions, then hallucination, sycophancy and sanction are best assessed at the level of the trained policy (the output distribution and… | Fails in two ways. (a) The content question is already settled: verbalized or behavioural confidence has been …<br>*Lin, Hilton & Evans 2022 (Teaching models to express uncertainty in words) report that a fine-tuned GPT-3's ve…* | §2; §3; §4; assumed: Verbalized confidence is overconfident and may imitate human… |
| 6 | *Conclusion* | — | — |

**Audit**

- · **ASSUMED** — §2 takes as given, defended nowhere: Chatbot outputs are assertions, so each is open to the defects assertion admits (falsity, lack of warrant, insincerity).
- · **ASSUMED** — §2 takes as given, defended nowhere: Error, hallucination and calibration are well defined as properties of a model's output distribution over a prompt distribution, and a calibrated model that is uncertain about arbitrary facts must put mass on false alternatives (Kalai, Nachum, Vempala & Zhang 2025, §3).
- · **ASSUMED** — §2 takes as given, defended nowhere: Sycophancy is a regularity in how outputs covary with the user's stated beliefs or approval across prompts, and is measured as a rate (Sharma et al. 2024, §2–3).
- · **ASSUMED** — §3 takes as given, defended nowhere: Chatbot outputs are assertions, so each is open to the defects assertion admits (falsity, lack of warrant, insincerity).
- · **ASSUMED** — §3 takes as given, defended nowhere: Sanction of an asserter requires that interlocutors track its credibility and that the asserter be sensitive to that tracking (Butlin & Viebahn 2025, elements (i) and (ii)).
- · **ASSUMED** — §3 takes as given, defended nowhere: Human preference judgements, preference models and benchmark grading act as training signals that reshape a chatbot's output distribution (Ouyang et al. 2022; Sharma et al. 2024, §4; Kalai et al. 2025, §4.1).
- · **ASSUMED** — §4 takes as given, defended nowhere: Chatbot outputs are assertions, so each is open to the defects assertion admits (falsity, lack of warrant, insincerity).
- · **ASSUMED** — §4 takes as given, defended nowhere: Sincerity (saying what one believes) and accuracy (taking care to believe truly) are distinct virtues of truthfulness, so an overconfident or poorly grounded but unselective assertion is an accuracy failure, not an insincere one (Bernard Williams, Truth and Truthfulness, 2002).
- · **ASSUMED** — §4 takes as given, defended nowhere: A calibrated model that is uncertain about arbitrary facts must put mass on false alternatives, so non-degenerate distributions and resampling variation are expected of well-functioning policies (Kalai et al. 2025, §3.1).
- · **ASSUMED** — §5 takes as given, defended nowhere: Verbalized confidence is overconfident and may imitate human confidence talk; better ECE can come from higher accuracy alone (Xiong et al. 2024, §5.1–5.2); probe-extracted probabilities need not be the model's credences (Levinstein & Herrmann 2025, §5.6–5.7); RL post-training can depart from the calibration of base models (Kalai et al. 2025, §3.1); stated confidence barely moves when the answer is swayed under challenge (Sharma et al. 2024, App. A.4).
- · **DEVIANT STRUCTURE** — There is no literature-review section and no objections section. Rivals (Chalmers, Shanahan et al., Mácha, Gómez, Butlin & Viebahn) are answered inside the sections they threaten. The load-bearing claim comes first and carries most of the length. The last substantive section argues for an absence (the content question is unsettled) and shows the earlier verdicts do not wait on it.

