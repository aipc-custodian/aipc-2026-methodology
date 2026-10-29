# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [assertion](https://plato.stanford.edu/entries/assertion/), [artificial-intelligence](https://plato.stanford.edu/entries/artificial-intelligence/), [lying-definition](https://plato.stanford.edu/entries/lying-definition/)
*The theses concern whether chatbot outputs count as assertions (the assertion entry, including sincerity and commitment), within the AI context, and on the neighbouring debate about lying and insincerity (resampling inconsistency read as insincerity).*


## If chatbot outputs are assertions, hallucination, sycophancy and sanction are best assessed at the level of the trained policy, and resampling inconsi…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **CONTRADICTED** | 3 | ["Language Without Propositions: Why Large Language Models Hallucinate"…](https://doi.org/10.3390/philosophies11020042) | <cite index="67-4">Argues that LLMs hallucinate because they have no inherent account of truth as correspondence to facts.</cite> <cite index="67-15">… |
| **CONTRADICTED** | 2 | ["Evaluating and Calibrating LLM Confidence on Questions with Multiple …](https://arxiv.org/html/2602.07842v1) | In MACE, <cite index="36-2">disagreement among sampled correct answers yields low estimated confidence, indistinguishable from alternation between cor… |
| **ADJACENT** | 3 | [David Chalmers, "What We Talk to When We Talk to Language Models", Phi…](https://philarchive.org/archive/CHAWWT-8) | <cite index="57-4,57-5,57-6">Asks whether the LLM interlocutor is the model, an instance running on a GPU, or a more evanescent system tied to a conve… |
| **ADJACENT** | 3 | [Iwan Williams & Tim Bayne, "Chatting with Bots: AI, Speech-Acts, and t…](https://philpapers.org/rec/WILCWB-3) | <cite index="15-8,15-9">They argue that treating chatbots as proto-assertors resolves the dilemma of chatbot assertion.</cite> A secondary source summ… |
| **ADJACENT** | 3 | [Patrick Butlin & Emanuel Viebahn, "AI Assertion", Ergo 12, 2025](https://philpapers.org/rec/BUTAAJ) | <cite index="3-5">Assertion requires outputs with descriptive functions and capacity to be sanctioned by interacting agents.</cite> <cite index="3-8">… |
| **ADJACENT** | 2 | [Shanahan, McDonell & Reynolds, "Role play with large language models",…](https://www.nature.com/articles/s41586-023-06647-8) | <cite index="40-5">Proposes seeing a dialogue agent as a superposition of simulacra within a multiverse of possible characters.</cite> <cite index="41… |
| **ADJACENT** | 2 | ["Assertion, Accountability, and Large Language Models", Philosophy & T…](https://link.springer.com/article/10.1007/s13347-026-01136-y) | <cite index="18-1,18-3">LLM outputs can function as assertions without the normative standing of human assertions. The normative commitments attach to… |
| **ADJACENT** | 1 | ["Alignment for Honesty", arXiv 2312.07000 (2023)](https://arxiv.org/pdf/2312.07000) | <cite index="69-2">Describes sycophancy as LLMs tailoring responses to the user's view even when this does not reflect the model's actual knowledge an… |
| **ADJACENT** | 1 | ["Cooperative Speech, Semantic Competence, and AI", arXiv 2504.16092](https://arxiv.org/pdf/2504.16092) | <cite index="28-3">Argues that present-day LLMs are incapable of assertion.</cite> The argument runs through cooperative speech and discursive respect… |
| **SUPPORTED** | 1 | [Survey of Confidence Estimation and Calibration in LLMs (Geng et al.),…](https://www.alphaxiv.org/abs/2311.08298) | <cite index="37-9,37-10,37-11">Consistency-based estimation generates multiple responses to one query and measures agreement. The principle is that ha… |

**What is left.** Granting that chatbot outputs may be (proto-)assertions, the surviving claim is this. The unit that is answerable to assertoric norms may be the trained policy, with a single output as an exemplar of it. That would let hallucination and sycophancy be assessed as calibration failures of that policy, and would make resampling variation no evidence of insincerity. This must be argued against Chalmers's thread-level individuation, Shanahan's character-superposition picture and the 'no representation of truth' diagnosis. It must also treat 'p, with confidence c' as an open empirical hypothesis, since sample spread does not reliably track credence. And it must not describe Butlin and Viebahn as assessing chatbots only output by output, because their credibility-tracking condition already uses a track record.

**Not found.** I found no source arguing, in the speech-act literature, that the unit of chatbot assertion is the trained policy or the resample distribution. I also found none that uses resampling inconsistency as the objection from commitment, or that links the descriptive-function condition to policy-level calibration. This is weak evidence given that much of the literature is paywalled and my search budget was small. I could not read the commitment section of Williams and Bayne or the full text of Butlin and Viebahn. Their views on consistency are therefore taken from abstracts and a third-party summary and need checking against the papers. The empirical search was narrow: I covered calibration, consistency-based uncertainty and persona and simulator work. I did not search the empirical sycophancy literature, such as Sharma et al., beyond seeing it cited. I did not search the human-side analogue (settled opinion versus slip of the tongue) in philosophy of speech acts, or work on assertion of graded or probabilistic content (credal or 'p with confidence c' assertion). I found no recent survey or reference-work entry that maps these positions; the nearest are the Williams and Bayne review of objections and Chalmers's ontology paper. Those two gaps are where an unnoticed anticipation could hide.


### From the Stanford Encyclopedia — assertion

- **SUPPORTED** (2/5) — Sincerity and insincerity are defined by the speaker's belief state. A resampling inconsistency is evidence of insincerity only if sincerity requires one stable belief. On commitment accounts, what matters is the speaker's answerability, not a stable inner state. — *Green (frankness); Bach & Harnish; Williams; Black/Davidson*
  > assertion is sincere just in case the speaker believes the content she has asserted
- **SUPPORTED** (2/5) — Assertion is characterised by default, prima facie cognitive patterns tied to surface features such as declarative form. Individual departures from those defaults do not remove assertoric status. — *Pagin (2011, 2020)*
  > an assertion is an utterance that is prima facie informative
- **SUPPORTED** (2/5) — Sanction and accountability are the core of the commitment accounts. These accounts assess liability and the duty to defend or retract. They do not require a particular inner episode at each utterance. — *Peirce; Alston; Brandom; MacFarlane; Rescorla; Green*
  > committing the speaker to defend her claim in response to legitimate challenges
- **SUPPORTED** (2/5) — Assertion can carry graded strength of commitment. Hedges and boosters modulate it, and assertability can be graded. — *Green; Marsili; Carter (2022); Jackson/Lewis*
  > These expressions modulate the degree of the commitment engendered by the assertions in which they occur
- **ADJACENT** (3/5) — A calibrated-confidence reading of content would meet the knowledge-norm objection that probability short of 1 does not license flat assertion (lottery assertions). The reading also invites the view that confidence is carried by mitigators, not by the content. — *Williamson (KNA); Carter (2022); Hawthorne*
  > No probability short of 1 seems to authorize A’s utterance of (27).
- **ADJACENT** (3/5) — Whether an utterance is an assertion at all depends on speaker-side conditions: intention, voluntariness, and being the speaker. The entry flags the question and leaves it open. It also treats the actor's non-sincere, 'represented' assertion as different. — *The entry itself; Davidson; Searle/Bach & Harnish (reflexive communicative intentions)*
  > must he intend it to be an assertion? Must it be made voluntarily?
- **ADJACENT** (2/5) — Hallucination as false-but-reasonable output maps onto the unlucky and lucky assertion debate. The entry reports experimental evidence favouring justification norms, and the primary/secondary propriety defence by KNA/TNA theorists. — *Lackey; Kneer; Reuter & Brössel; Marsili & Wiegmann; Williamson; DeRose*
  > It would therefore seem that the latest studies have tipped the scale in favor of non-factive views like (JNA).
- **ADJACENT** (2/5) — Assertion and commitment in context involve retraction. Stalnaker's common-ground model treats accepting as weaker than believing. This bears on sycophancy, which adjusts content to the hearer. — *MacFarlane (retraction rule); Rescorla; Stalnaker*
  > Retract an (unretracted) assertion if it turns out not to be true.
- **ADJACENT** (2/5) — Some argue there is no assertion-specific norm, and that epistemic norms attach to action or to other general principles. This bears on assessing at the policy level in place of the speech-act level. — *Greenberg (2020); Pagin 2016b; D. Black; Cappelen (in the bibliography)*
  > Greenberg (2020) proposes to reframe the debate in terms of epistemic norms constraining action, rather than assertion.

**Nearest positions.** Commitment/accountability accounts of assertion (liability, challenge-and-retract) — Peirce, Alston, Brandom, MacFarlane, Green; Belief-expression/self-representation and sincerity as frankness — Black, Davidson, Bach & Harnish, Williams, Green; Norms of assertion (knowledge vs justification vs truth/belief) with graded or context-sensitive variants — Williamson, Lackey, Kvanvig, Gerken, Carter (2022)

**The entry is silent on.** Artificial or non-human speakers, chatbots and language models. The entry also says nothing on assessing assertion at the level of a trained policy or system, as opposed to an individual utterance or speaker. It does not discuss stochastic resampling or inconsistency across repeated outputs, or sycophancy and hallucination as such. It does not ask whether content is 'p, with confidence c' for a probabilistic producer, and gives no account of an entity with no stable belief state.


### From the Stanford Encyclopedia — artificial-intelligence

- **SUPPORTED** (1/5) — An agent is identified with a function from percepts to actions. Assessment is made of the whole function or program under a performance measure, not of individual outputs. This gives a policy-level unit of evaluation. — *Russell (1997); Russell & Norvig (AIMA)*
  > intelligent agents, which are functions taking as input tuples of percepts from the external environment, and producing behavior (actions) on the basis of these percepts
- **SUPPORTED** (1/5) — Probabilistic agents attach degrees of belief to propositions. Probability theory is symbolic and declarative, so 'p, with confidence c' has a natural formal home. Machine learning is also analysed by PAC bounds on mismatch between learnt and true function. — *AIMA probabilistic tradition; Pearl 1988; Kolmogorov axioms as presented*
  > in probability theory we are concerned with declarative statements, or propositions, to which degrees of belief are applied
- **CONTRADICTED** (3/5) — Non-logicist (connectionist/neural) systems are described as lacking declarative propositional content. On that account their outputs would not be assertions of a candidate p, and the question of calibrated 'p with confidence c' would not arise. — *The entry's own gloss on non-logicist AI*
  > the agents engineered by non-logicist AI researchers ... cannot be said to know that \(\phi\); – for the simple reason that, by negation, the non-logicist paradigm would have not even a single declarative proposition that is a candidate for \(\phi\)
- **ADJACENT** (2/5) — Whether machine speech expresses knowledge or mere 'disposition of organs'. This is the Cartesian doubt that machine utterances are genuine speech acts. — *Descartes 1637, quoted in the entry; Turing's Test as the Human/Act position*
  > they did not act from knowledge, but only for the disposition of their organs
- **ADJACENT** (2/5) — A machine built to induce false beliefs, using a computational theory of mind. This is the nearest the entry comes to insincerity or deception by an artificial agent. — *Clark (2010); Bello & Bringsjord (2013)*
  > build a lying machine that successfully persuades people into believing falsehoods
- **ADJACENT** (1/5) — Output instability: adversarial inputs near-identical to humans are treated differently by neural networks. This is a robustness worry about input-output behaviour. — *Szegedy et al. 2014, as reported*
  > adversarial inputs, which are indistinguishable from normal inputs to humans but are computed in a special manner that makes a neural network regard them as different
- **ADJACENT** (1/5) — Open-domain question answering has no agreed formal function, and Watson fails on dynamic QA whose answers are not recorded anywhere. This bears on hallucination as answering without grounding. — *Entry's discussion of Watson; Levesque (2013); Govindarajulu et al. 2013*
  > there is no agreement as to what underlying function, formally speaking, question-answering capability computes

**Nearest positions.** Agent-as-function / bounded optimality: assess the program-on-machine, not single outputs — Russell (1997), Russell & Norvig; Probabilistic agents with degrees of belief over propositions — AIMA Part IV, Pearl (1988); Non-symbolic systems hold no declarative propositions, so no 'knowing that p' — the entry's characterization of non-logicist AI; Cartesian doubt that machine speech expresses knowledge — Descartes (1637), Turing Test tradition

**The entry is silent on.** Nearly the whole thesis. The entry (2018, pre-LLM) never discusses assertion or speech-act theory for machine outputs, hallucination, sycophancy, sanction or accountability for outputs, sampling or resampling inconsistency, sincerity as a property of a policy, or calibration of stated confidence. Its treatment of 'Strong AI' and the Chinese Room (Section 8) is cut off in the text given, so nothing can be quoted from it.


### From the Stanford Encyclopedia — lying-definition

- **SUPPORTED** (1/5) — Falsity is neither necessary nor sufficient for lying. What matters is the speaker's attitude to what is said. A false statement made without believing it false is not a lie, which gives the thesis a framework for treating hallucination as an error rather than insincerity. — *L1 defenders (Isenberg, Primoratz); the entry describes the falsity condition as a rival (Coleman and Kay, Carson, Saul)*
  > Statements that are truthful may be false. If George makes the statement to Hillary ... 'The enemy has weapons of mass destruction,' and that statement is false, he is not lying if he does not believe that statement to be false.
- **SUPPORTED** (2/5) — Lying is sometimes defined by lack of belief in truth or by belief that the statement is probably false, rather than by belief in falsity. This is the entry's nearest approach to graded attitudes and bears on whether an output expresses a calibrated 'p, with confidence c'. — *Carson (2006, 2010); Shiffrin (2014)*
  > it is sufficient that the statement is not believed to be true, or is believed to be probably false ... 'Agnostics about the truth of their assertions who nonetheless assert them without qualification tell lies'
- **ADJACENT** (3/5) — Asserting a content is a matter of a warranting context, the speaker's belief that a norm against falsehood is in force, or a proposal to update the common ground. These are speaker-level, context-sensitive accounts. A referee would ask which of them licenses treating chatbot output as assertion, and whether the speaker is the policy. — *Carson (warranting); Fallis (L15/L16, Gricean norm); Stokke (L17, common ground); Chisholm and Feehan (L6); Sorensen*
  > x states p in a context in which x thereby warrants the truth of p to y ... 'you lie when you assert something you believe to be false' (Fallis 2009, 33)
- **ADJACENT** (2/5) — Sycophancy resembles white lies and prosocial lies, which the entry counts as lies on L1. It also resembles polite untruths, which are not lies because they are understood as code or euphemism. Which one sycophantic outputs resemble depends on whether the audience takes them as conventional. — *Green (2001), Sweetser (1987), Hardin (2010) on white lies; Isenberg (1973), Shiffrin (2014), Coleman and Kay (1981) on polite untruths*
  > White lies, prosocial lies, and fibs are all intentionally deceptive, and are all lies according to L1 ... Polite untruths may be said to be examples of 'falsifications but not lies'
- **ADJACENT** (2/5) — Whether untruthful speech under external compulsion counts as assertion. 'Sanction' may be read as imposed or required speech, which is the closest analogue to the thesis's sanction term, and the entry reports the view that it does not. — *Leland (2013/2015), Kenyon (2010); Saul (2012) on totalitarian-state utterances; Donagan (L11) on duress*
  > 'Coerced speech acts are not genuinely assertoric' (Leland 2013, 3)
- **ADJACENT** (2/5) — Inadvertent or mistaken deception. Many hold that deception requires intention, so an unintended false belief is 'misleading', not deceiving. This is relevant to classifying hallucination. Chisholm and Feehan allow unintentional deception. — *Linsky, van Horne, Barnes, Carson, Saul, Faulkner (intentional); Demos, Fuller, Chisholm and Feehan, Adler, Gert (can be inadvertent)*
  > They reserve term 'mislead' to cover cases of causing false beliefs either intentionally or unintentionally (Carson 2010, 47).
- **ADJACENT** (1/5) — The addressee condition concerns whether non-persons such as robots can be lied to, and notes lying via non-person intermediaries. A referee may raise this as a nearby issue, though it concerns the hearer rather than the speaker. — *L1 (addressee condition); Chisholm and Feehan (burglar case); Krishna 1961 and Morris 1976 appear only in the bibliography*
  > It is not possible to lie to those whom you believe to be non-persons (goldfish, dogs, robots, etc.) ... It is possible to lie to other persons via intermediaries which are not persons

**Nearest positions.** Complex Deceptionism: assertion as invoking trust or implicit assurance — Chisholm and Feehan, Fried, Simpson, Faulkner; Complex Non-Deceptionism via warranting: lying requires warranting the truth or believing one is in a warranting context — Carson (L12/L13), Saul (L14); Complex Non-Deceptionism via assertion: Gricean norm or common-ground accounts that make lying a speaker-level, belief-based act — Fallis (L15/L16), Stokke (L17), Sorensen (bald-faced lies)

**The entry is silent on.** The entry says nothing about AI systems, chatbots or language models as speakers, or about any policy-level or collective speaker distinct from a single utterance. It does not discuss hallucination, sycophancy, training or reward, sampling or resampling inconsistency, or calibrated credences and explicit confidence statements ('p, with confidence c'). Belief is treated as binary or near-binary (believed false, not believed true, probably false). It never asks what counts as the speaker's belief for an entity whose outputs vary across resamples, so it gives no test of insincerity from inconsistency.

<details><summary>8 searches</summary>

- `Butlin Viebahn AI assistants assert? chatbot assertion`
- `Williams Bayne chatbot assertion objection from commitment`
- `LLM assertion policy level resampling inconsistency speaker commitment`
- `LLM calibration verbalized confidence consistency across samples hallucination uncertainty`
- `large language models simulators personas superposition of characters role play Shanahan`
- `Williams Bayne "Chatting with bots" commitment objection consistency chatbots do not treat claims as binding resampled`
- `Chalmers "What we talk to when we talk to language models" quasi-agent thread character model`
- `LLM hallucination lying assertion sincerity philosophy model-level versus instance-level speaker`

</details>

