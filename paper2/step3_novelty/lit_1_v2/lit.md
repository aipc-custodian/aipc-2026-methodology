# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [assertion](https://plato.stanford.edu/entries/assertion/), [speech-acts](https://plato.stanford.edu/entries/speech-acts/), [artificial-intelligence](https://plato.stanford.edu/entries/artificial-intelligence/)
*The theses concern whether chatbot outputs count as assertions, which the assertion entry covers directly (sincerity, commitment, norms of assertion), with speech-acts as the broader neighbouring debate over what unit counts as an act, and artificial-intelligence as the closest listed entry on the chatbot side.*


## If chatbot outputs are assertions, hallucination, sycophancy and sanction are best assessed at the level of the trained policy, and resampling inconsi…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **CONTRADICTED (abstract)** | 3 | [Butlin & Viebahn, "AI Assertion", Ergo 12, 2025](https://philpapers.org/rec/BUTAAJ) | They argue that an assertor must produce outputs with descriptive functions and must be capable of being sanctioned by the agents it interacts with. M… |
| **CONTRADICTED (snippet)** | 2 | [Williams & Bayne, "Chatting with Bots: AI, Speech-Acts, and the Edge o…](https://arxiv.org/pdf/2410.16645) | They list the expectations attached to adult human assertion: defending it, explaining reasons, not blatantly contradicting it in the next moment, and… |
| **CONTRADICTED (abstract)** | 2 | [Wang, Zhou et al., "Are LLM Decisions Faithful to Verbal Confidence?",…](https://arxiv.org/html/2601.07767v1) | They report a dissociation: models are neither cost-aware when articulating verbal confidence nor strategically responsive when deciding whether to ab… |
| **CONTRADICTED (snippet)** | 2 | ["Do LLMs have core beliefs?", arXiv 2605.03255, 2026; and "Probing the…](https://arxiv.org/pdf/2605.03255) | Across five domains, none of the tested models showed genuine core commitments, and all eventually abandoned well-established truths under sustained a… |
| **CONTRADICTED (snippet)** | 2 | ["The Outputs of Large Language Models are Meaningless", arXiv 2509.222…](https://arxiv.org/pdf/2509.22206) | The randomness of an LLM's token choice contrasts starkly with the process taking a human speaker from hearing a question to asserting an answer. A hu… |
| **PRECEDENT · FRAMEWORK (snippet)** | 2 | [Shanahan, McDonell & Reynolds, "Role play with large language models",…](https://www.nature.com/articles/s41586-023-06647-8) | The dialogue agent maintains a superposition of simulacra, which is a distribution over all possible simulacra consistent with the preceding context. … |
| **ADJACENT (snippet)** | 2 | ["Where is the Mind? Persona Vectors and LLM Individuation", arXiv 2604…](https://arxiv.org/pdf/2604.17031) | Key objections to the instantiated-model and virtual-instance views concern inconsistent behaviour: these entities do not consistently behave in ways … |
| **ADJACENT (snippet)** | 2 | ["Assertion, Accountability, and Large Language Models", Philosophy & T…](https://link.springer.com/article/10.1007/s13347-026-01136-y) | LLM outputs can function as assertions in the sense that they present content as answerable, actionable and truth-evaluable. The normative commitments… |
| **ADJACENT (abstract)** | 1 | ["Can LLMs Lie? Investigation beyond Hallucination", arXiv 2509.03518, …](https://arxiv.org/html/2509.03518v1) | Hallucinations are unintentional falsehoods, whereas lying is an LLM knowingly generating falsehoods for an ulterior objective. |
| **SUPPORTED (abstract)** | 1 | [Xiong et al., "Can LLMs Express their Uncertainty? An Empirical Evalua…](https://arxiv.org/pdf/2306.13063) | Consistency among multiple responses improves failure prediction and calibration compared with single-response verbalized confidence. LLMs verbalizing… |
| **SUPPORTED (snippet)** | 1 | ["The Illusion of Certainty: Decoupling Capability and Calibration in O…](https://arxiv.org/pdf/2604.16830) | Hallucination detection frameworks such as SelfCheckGPT work on the principle that a hallucinating LLM's sampled responses show high entropy and self-… |
| **SUPPORTED (secondhand)** | 1 | [Zhan et al. 2024 survey, as reported in "Lies, Damned Lies, and Distri…](https://arxiv.org/pdf/2412.17128) | Users' trust in ChatGPT was reported as well calibrated to the model's errors, with verification increasing with exposure to misleading content. |

**What is left.** Nothing I could see meets the ANTICIPATED standard. Granting that chatbot outputs can be assertions, the thesis argues that the unit of the speech act is the trained policy's output distribution (including its calibration) and not the sampled string. On that view resampling inconsistency is not evidence of insincerity, hallucination is policy-level miscalibration, sanction targets retraining, and single outputs are at most exemplars or proto-assertions. The thesis must take as rivals the Williams-Bayne reading of inconsistency, the Butlin-Viebahn verdict that fine-tuned models fail the sanction condition, and the empirical evidence that verbal confidence, behaviour and cross-turn stability can come apart. It must say which level counts as 'the policy' (weights, persona or deployed system). Whether the policy's output is a calibrated 'p with confidence c' stays open, as the thesis already says.

**Credit (precedents the thesis develops).** Shanahan, McDonell & Reynolds 2023 — treats an LLM agent as a distribution over simulacra, which shifts the object of description away from the single output; Butlin & Viebahn 2025 — the descriptive-function and sanctionability conditions, and the practice of tracking a chatbot's reliability at the level of the system; Williams & Bayne 2024/2026 — the proto-assertion verdict, and the list of consistency and defence expectations that the objection from commitment draws on; Xiong et al. 2023/2024 and Manakul et al. 2023 (via secondhand description) — sample-consistency as an empirical proxy for calibrated confidence

**Not found.** I searched for but did not find any philosophical work that distinguishes token-assertion from policy-assertion, or that argues resampling inconsistency is not evidence of insincerity. I found none that reads a chatbot's output spread as the content 'p with confidence c', or that ties sanction to retraining the policy. I never saw the full text of Butlin & Viebahn or Williams & Bayne, so I did not verify their treatment of commitment and consistency, and anything they say about sampling or policy-level readings could be missed. I only have a secondhand report of Williams & Bayne on consistency, and none of Levinstein & Herrmann beyond a secondhand summary. I ran no dedicated search for a recent survey or encyclopedia entry on AI assertion, so the fourth required search is incomplete. The empirical search did leave philosophy (calibration, hallucination detection and belief-stability work in ML). It was a single sweep with no check of the primary papers, and I did not search psychology, linguistics or sociology. Most of the literature is paywalled or preprint and invisible to me, so this silence is not evidence of originality.


### From the Stanford Encyclopedia — assertion

- **SUPPORTED** (1/5) — Norms of assertion (knowledge, justification, truth, belief) are candidate standards for assessing assertions; the thesis can borrow these to say hallucination is assessable as a violation of an epistemic norm. — *Williamson (KNA); Lackey, Douven (JNA); Weiner, Whiting (TNA); Bach (BNA)*
  > Williamson (1996, 2000) initiated this debate by proposing that assertion is governed by a single norm
- **SUPPORTED** (2/5) — Assertions can be mitigated or boosted, so commitment comes in degrees. This bears on whether the content is 'p, with confidence c' rather than flat 'p'. — *Entry's commitment section (Green, Caffi, Holmes cited)*
  > These expressions modulate the degree of the commitment engendered by the assertions in which they occur
- **SUPPORTED** (2/5) — Commitment accounts tie sanction and accountability to the asserter: liability to blame, and a duty to defend or retract when challenged. Sanction is thus a speaker-level, hearer-directed matter. — *Peirce, Alston, Brandom, MacFarlane, Green*
  > an act of assertion […] renders [the speaker] liable to the penalties of the social law
- **PRECEDENT · PASSING** (2/5) — Insincerity is analysed via self-representation or communicative intention, and sincerity is a matter of belief. Resampling inconsistency as non-evidence of insincerity is not discussed, but the notion of insincerity at stake is the relevant one. — *Black, Davidson, Williams, Bach & Harnish, Green (frankness)*
  > in asserting that p the speaker represents herself as believing that p
- **ADJACENT** (2/5) — Pagin's cognitive account treats assertion as prima facie informative, with defaults tied to surface features and the speaker's belief 'with sufficient strength' as a partial reason for utterance. This is a graded, dispositional notion that could ground a policy-level reading. — *Pagin (2011, 2020)*
  > the speaker believes, with a sufficient strength, that the sentence expresses a true proposition, and utters it partly because of that
- **ADJACENT** (2/5) — Lackey-style selfless assertion and the primary/secondary propriety distinction bear on assessing a policy's outputs. The latter separates the rule from reasonably believing one satisfies it, and may let hallucination be blameless yet improper. — *Lackey; DeRose*
  > Unlucky and Gettiered assertions are primarily improper but secondarily proper, and that’s why they don’t deserve blame.
- **ADJACENT** (2/5) — The entry flags that an asserter's intentions, e.g. whether the utterance must be intended as an assertion or be voluntary, are open questions. This bears on the antecedent 'if chatbot outputs are assertions'. — *Entry's section 4.2*
  > must he intend it to be an assertion? Must it be made voluntarily?
- **ADJACENT** (2/5) — Hearer-directed and normative accounts predicate assertion of a speaker who can be held accountable, which pressures whether a trained policy can be the asserter. — *Commitment accounts (Brandom, Alston, Searle)*
  > the assertor is expected to “be able to provide reasons for the original statement […] and can be held publicly responsible if it turns out to be false”

**Nearest positions.** Norm-of-assertion debate (knowledge/justification/truth/belief norms) — Williamson, Lackey, Douven, Weiner, Whiting, Bach; Commitment/accountability accounts of assertion — Peirce, Alston, Brandom, MacFarlane, Green; Self-representation / belief-expression accounts of sincerity — Black, Davidson, Bach & Harnish, Williams; Pagin's graded, dispositional cognitive account of assertion

**The entry is silent on.** The entry says nothing about artificial or machine speakers, chatbots, trained policies, hallucination, sycophancy, or resampling inconsistency. It also does not say whether assertoric content can be a calibrated 'p, with confidence c', nor whether assertion or sincerity can be assessed at the level of a dispositional policy rather than an individual utterance.


### From the Stanford Encyclopedia — speech-acts

- **SUPPORTED** (1/5) — Assertion is characterized by overt commitment with a norm of answering 'How do you know?', being right or wrong depending on P, and a duty to retract. This gives the thesis a normative criterion for asking whether chatbot outputs are assertions, and a way to assess them by the commitment they carry. — *Green (the entry's author), drawing on Williamson 1996*
  > One who asserts P lays herself open to the challenge, "How do you know that?", and she is obliged to retract P if she is unable to respond to that challenge adequately.
- **SUPPORTED** (1/5) — Assertion, conjecture and guess share direction of fit and conditions of satisfaction but differ in strength of commitment. This supports the thesis's open question of whether the content is a calibrated 'p, with confidence c' rather than a flat assertion. — *Green; Williamson 1996*
  > as we move down the list we find a decreasing order of stringency in commitment.
- **ADJACENT** (2/5) — Speech acts require speaker meaning, which on the Gricean account involves intentions and overtness. Whether a trained policy can speaker-mean, so that its outputs are assertions at all, is a conditional the thesis presupposes. The entry offers an overtness account and Davis-style cases (speaking to infants, photocopiers) that loosen the requirement of intentions to affect addressees. — *Grice 1957; Davis 1992; Green 2019*
  > Instead of intentions to produce psychological effects in an addressee, some authors have advocated a construal of speaker meaning as overtly manifesting an aspect of one's commitments or state of mind (Green 2019).
- **CONTRADICTED** (2/5) — The entry says that intending to perform a speech act is insufficient, and that a speech act requires intentionally undertaking a publicly accessible commitment. Sincerity concerns whether the speaker is in the psychological state the act expresses. This sits uneasily with assessing sincerity or its absence at the level of a policy rather than an individual utterance. — *Green 2013; Austin; Searle and Vanderveken*
  > A speech act is sincere only if the speaker is in the psychological state that her speech act expresses.
- **SUPPORTED** (1/5) — The entry reports that a pattern of abuses or conduct can deprive a speaker of the ability to perform a speech act in a community. It also distinguishes a retractable assertion from a non-retractable act. This supports assessing sanction at the level of an ongoing pattern or policy, and treating retraction as a feature of assertion. — *Green; Sbisà 2007*
  > a pattern of abuses of speech act institutions might deprive a person of an ability to perform speech acts: the inveterate promise-breaker will, in time, lead others in his community to be unwilling to accept any promises he tries to make.
- **ADJACENT** (2/5) — Illocutionary logic and commitment relations among speech acts concern what a speaker's commitments entail, including illocutionary validity. These are framed in terms of commitment to content under a mode. Inconsistency across assertions would be assessed through that machinery. — *Searle and Vanderveken 1985; Green 2000*
  > Because it concerns what force/content pairs commit an agent to what others, illocutionary validity is an essentially deontic notion

**Nearest positions.** Assertion as overt commitment to P, with the 'How do you know?' challenge and a duty to retract; graded against conjecture and guess — Green, Williamson; Speaker meaning as overt manifestation of commitment or state of mind, as against Gricean reflexive intentions — Green 2019, Grice 1957, Davis 1992; Sincerity conditions: a speech act is sincere only if the speaker is in the psychological state it expresses — Searle and Vanderveken 1985, Austin

**The entry is silent on.** The entry never discusses AI, chatbots, language models, trained policies, resampling or stochastic outputs, sycophancy, hallucination, or the idea that an assertion's content is a probability or confidence-qualified claim 'p, with confidence c'. It also does not discuss whether sincerity or commitment can attach to a policy rather than a single utterance.


### From the Stanford Encyclopedia — artificial-intelligence

- **ADJACENT** (1/5) — Russell's agent-as-function framework: an intelligent agent is a function from percept sequences to actions, and bounded optimality evaluates the program/policy. This is a framework in which evaluating at the level of the whole trained policy is natural, but the entry does not apply it to assertion, hallucination or sincerity. — *Russell (1997); Russell & Norvig (AIMA)*
  > Russell sees AI as the field devoted to building intelligent agents, which are functions taking as input tuples of percepts from the external environment, and producing behavior (actions) on the basis of these percepts.
- **ADJACENT** (1/5) — Probabilistic AI treats beliefs as degrees of belief over propositions, with conditional probability P(p|q). This is a background for reading a policy's output as a calibrated 'p with confidence c', but the entry does not discuss calibration of chatbot outputs. — *Probabilistic AI tradition (Pearl 1988, Kolmogorov axioms as presented)*
  > in probability theory we are concerned with declarative statements, or propositions, to which degrees of belief are applied
- **ADJACENT** (1/5) — Learned systems are evaluated on benchmarks, and adversarial inputs raise doubts about how benchmark performance transfers. This is a loose neighbour of the thesis's point that assessment should target the trained policy rather than individual outputs. — *Szegedy et al. 2014, as reported*
  > the existence of so-called adversarial inputs ... has raised doubts about how well performance on benchmarks can translate into performance in real-world systems
- **ADJACENT** (2/5) — The entry's treatment of the Turing Test and Strong vs. Weak AI concerns whether linguistic behaviour indicates real mentation. This is the rival/background question of whether machine linguistic output counts as genuine thought, which a paper on assertion would be situated against. — *Turing (1950); Descartes (1637); Haugeland (1985); Searle (via the Chinese Room section heading)*
  > Passing in this sense operationalizes linguistic indistinguishability.

**Nearest positions.** Turing Test: linguistic indistinguishability operationalizes intelligence — Turing (1950), as reported; Intelligent agents as policies/functions from percepts to actions, evaluated for rationality — Russell & Norvig; Russell (1997); Probabilistic degree-of-belief representations of uncertainty — Pearl (1988), Kolmogorov-style probability as presented in the entry

**The entry is silent on.** Everything specific to the thesis: whether chatbot outputs are assertions, hallucination, sycophancy, sanction or norms of assertion, sincerity, resampling inconsistency, and whether a policy's outputs express calibrated 'p, with confidence c'. The entry (a 2018 text, truncated before the philosophy-of-AI sections) does not discuss large language models or speech-act theory.

<details><summary>8 searches</summary>

- `Butlin Viebahn AI assistant assertion chatbot`
- `Williams Bayne chatbot assertion objection from commitment`
- `LLM consistency across resampling calibration verbalized confidence assertion policy-level belief`
- `do large language models make assertions philosophy speech act hallucination lying`
- `LLM beliefs inconsistency across samples not evidence against belief; model as distribution over personas, assertion`
- `Williams Bayne proto-assertion commitment consistency chatbot "do not ensure they are consistent" resampling`
- `Shanahan role play simulacra superposition LLM assertion truthfulness`
- `LLM assertion sampling stochastic policy level "type" vs "token" outputs speech act philosophy`

</details>

