# Outlines — outlines_1b_rework4

**Thesis (fixed):** If chatbot outputs are assertions, then hallucination, sycophancy and sanction are best assessed at the level of the trained policy (the output distribution and its calibration), not the sampled string, and resampling inconsistency is not evidence of insincerity. Whether the asserted content is the policy's calibrated 'p, with confidence c' is not established.

Nothing here is ranked and nothing is scored. The outlines were written blind to each other, and the flags below each one are computed from its own dependency ledger — no model judged coherence. Read the outlines first; the divergence section at the end is only useful once you have.


## Addresses to check

Every position the outlines name as a refuter. Nothing in this pipeline can verify that these people hold these views; this is the list to run your eye down first.

| Where | Position |
|---|---|
| O0§3 | David Chalmers ('What We Talk to When We Talk to Language Models', 2026, pp. 10-16) argues that one model serves thousands of conversations that say contradictory things, so a model-level speaker woul… |
| O0§6 | Germán Massaguer Gómez (Philosophy & Technology 39:123, 2026, §7, p. 19) holds that, since LLMs are not agents, accountability must rest with the human and institutional structures that design, deploy… |
| O0§5 | Iwan Williams & Tim Bayne (2026): the thesis targets their use of inconsistency and non-binding behaviour as a mark against full assertion. The reading notes record only that they list not contradicti… |
| O0§4 | Saurav Kadavath et al. (2022, 'Language Models (Mostly) Know What They Know'; attribution here rests on the abstract and the RLHF calibration figure caption, to be checked against the body before subm… |
| O0§2 | Timothy Williamson (Knowledge and its Limits, 2000, ch. 11) holds that assertion is governed by the knowledge rule, which is violated by each assertion made without knowledge whatever the asserter's d… |


## Outline 0 — Judge the Policy, Not the String: Assertion, Hallucination, Sycophancy and Resampling in Chatbots

*Supposing chatbot outputs are assertions, show that the three failures named in the thesis are constituted at the level of the output distribution; that this holds whoever the speaker is; that what the policy asserts is left open; that resampling divergence then fails to indicate insincerity; and that the policy beats the string and the deployer as the unit of assessment.*

- **Surprise.** The structure separates the locus of assessment from the identity of the speaker. This lets the paper grant Chalmers's case against the model-as-speaker in full and still reach a policy-level verdict. It also makes the open-content claim a constraint that §5's argument has to survive on every candidate content, not a closing caveat.
- **Commitment.** The paper commits to inconsistency being no evidence of insincerity, not weak evidence, and to the string being the wrong unit for these three assessments even while conceding that per-assertion norm violation is string-level. It refuses to rest on the credence reading of content, leaving the content claim open at the thesis's own strength. It also stakes the sanction claim against Gómez and Butlin & Viebahn on the ground that deployer assessment is downstream of the policy.
- **Gap.** §5, abductive: From 'sample divergence is fixed by the distribution and the decoding setting' (with §4 leaving the content open) the paper infers 'divergence is not evidence of insincerity'. This goes through only if, for every live candidate content, sincerity and insincerity predict the same divergence once the policy's distribution is given. The candidates are bare p at the mode and p-with-c. It also requires that sampled departures from the mode, on the bare-p reading, be classed as overassertion (a calibration fault already assessed under hallucination) and not as assertions the policy does not believe. That in turn needs a notion of the policy's attitude on which a wide distribution is not itself disbelief in the sampled string, and no independent probe of that attitude (Levinstein & Herrmann) is available to overturn it. If a threshold view of belief is right, on which asserting a non-modal sample is asserting what one disbelieves, the step fails. This is the point of greatest distance between what §§2-4 establish and what is claimed.
- **Arrives at.** §6
- **Load-bearing.** Hallucination as a failing to be assessed and remedied, sycophancy, sanction-sensitivity and calibration are each constituted by how a system's outputs vary across prompts and samples, so no single sampled string settles whether they are present.
- **Shape.** 5 substantive sections, plus frame

| § | Establishes | Refuted by / address | Takes as given |
|---|---|---|---|
| 1 | *Introduction* | — | — |
| 2 | Hallucination as a failing to be assessed and remedied, sycophancy, sanction-sensitivity and calibration are each constituted by how a system's outputs vary acr… | A single-output criterion that settles each of these. Per-act violation of the assertion norm is conceded to b…<br>*Timothy Williamson (Knowledge and its Limits, 2000, ch. 11) holds that assertion is governed by the knowledge …* | assumed: Chatbot outputs are assertions (supposed for the sake of arg…; assumed: Working definitions: hallucination is plausible falsehood ar… |
| 3 | Locating the assessment of hallucination, sycophancy and sanction at the trained policy does not require the policy to be the speaker, because a virtual instanc… | A showing that the policy's dispositions are either too incoherent or too thin to be those of whoever speaks, …<br>*David Chalmers ('What We Talk to When We Talk to Language Models', 2026, pp. 10-16) argues that one model serv…* | §2; assumed: Chatbot outputs are assertions (supposed for the sake of arg… |
| 4 | The evidence on calibration does not establish that what a chatbot asserts is the policy's calibrated 'p, with confidence c', because verbalized confidence is p… | Evidence that deployed, post-trained policies are well calibrated and that their outputs reliably carry that c…<br>*Saurav Kadavath et al. (2022, 'Language Models (Mostly) Know What They Know'; attribution here rests on the ab…* | §2; assumed: Elicited verbalized confidence, sampling consistency and pro… |
| 5 | Divergence among samples drawn from one prompt is fixed by the policy's output distribution and the decoding setting, so it is evidence of how wide the distribu… | A showing that, on some live candidate content for the policy's assertions, samples that depart from the polic…<br>*Iwan Williams & Tim Bayne (2026): the thesis targets their use of inconsistency and non-binding behaviour as a…* | §2; §3; §4; assumed: Insincerity is asserting what one does not believe, that is,… |
| 6 | If chatbot outputs are assertions, then hallucination, sycophancy and sanction are best assessed at the level of the trained policy (the output distribution and… | A showing that the deploying humans or institutions, and not the policy, are the best unit for assessing sanct…<br>*Germán Massaguer Gómez (Philosophy & Technology 39:123, 2026, §7, p. 19) holds that, since LLMs are not agents…* | §2; §3; §4; §5; assumed: A deployer's answerability for a chatbot's outputs is answer… |
| 7 | *Conclusion* | — | — |

**Audit**

- · **ASSUMED** — §2 takes as given, defended nowhere: Chatbot outputs are assertions (supposed for the sake of argument throughout; not defended in this paper).
- · **ASSUMED** — §2 takes as given, defended nowhere: Working definitions: hallucination is plausible falsehood arising as generative error (Kalai et al.); sycophancy is a model seeking human approval in unwanted ways (Sharma et al.); sanction requires that interlocutors track credibility, that the asserter is sensitive to this, and that losing credibility is bad for the asserter (Butlin & Viebahn).
- · **ASSUMED** — §3 takes as given, defended nowhere: Chatbot outputs are assertions (supposed for the sake of argument).
- · **ASSUMED** — §4 takes as given, defended nowhere: Elicited verbalized confidence, sampling consistency and probe-extracted probabilities are the available evidence of a system's confidence.
- · **ASSUMED** — §5 takes as given, defended nowhere: Insincerity is asserting what one does not believe, that is, a mismatch between what is asserted and the asserter's attitude; and decoding temperature is set outside the trained policy.
- · **ASSUMED** — §6 takes as given, defended nowhere: A deployer's answerability for a chatbot's outputs is answerability for deploying a system with a given behavioural profile.
- · **DEVIANT STRUCTURE** — There is no motivation-objection-reply shape and no objections section. Each rival (Williamson, Chalmers and Shanahan et al., Kadavath et al., Williams & Bayne, Gómez and Butlin & Viebahn) is answered inside the section its view threatens. The open-content claim ('not established') gets its own section. It is an argued negative that §5 consumes: §5 must hold on every candidate content, and without §4 it could not be stated at thesis strength. The last substantive section arrives at the thesis by a comparative step (policy over string, policy over deployer), not by summarising.

