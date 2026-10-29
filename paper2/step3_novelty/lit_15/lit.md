# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [assertion](https://plato.stanford.edu/entries/assertion/), [ethics-ai](https://plato.stanford.edu/entries/ethics-ai/), [speech-acts](https://plato.stanford.edu/entries/speech-acts/)
*The thesis is about the norms of assertion and whether proxy or delegated speech by LLM deployers counts as assertion (assertion), it belongs to the debate over AI systems' outputs and responsibility (ethics-ai), and it relies on speech-act theory's account of commitment and illocutionary acts (speech-acts).*


## If assertion is governed by an epistemic-position norm, then deployers of unreviewed generative systems do not assert the outputs. What they do is end…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **ANTICIPATED** | 4 | [Arora, "Proxy Assertions and Agency: The Case of Machine-Assertions", …](https://link.springer.com/article/10.1007/s13347-024-00703-5) | <cite index="10-3">Arora proposes that only machine utterances count as proxy assertions where the designers' epistemic responsibility or requisite ep… |
| **ANTICIPATED** | 3 | [Williams & Bayne, "Chatting with Bots: AI, Speech Acts, and the Edge o…](https://arxiv.org/pdf/2410.16645) | <cite index="1-8,1-9">They treat the proxy-assertion move as potentially fatally flawed because typical proxy cases have a clear principal.</cite> <ci… |
| **ANTICIPATED** | 3 | [Butlin & Viebahn, "AI Assertion", Ergo, 2025](https://journals.publishing.umich.edu/ergo/article/id/7960/print/) | <cite index="14-8">They argue that if assertion requires sanctionability, proxy assertion does not offer a road to AI assertion.</cite> <cite index="1… |
| **CONTRADICTED** | 3 | [Green & Michel, "What Might Machines Mean?", Minds and Machines, 2022 …](https://journals.publishing.umich.edu/ergo/article/id/7960/print/) | <cite index="15-10">Their RobotCops use a flexible, perhaps reason-responsive method to decide whether to fine or warn drivers, and can send drivers m… |
| **CONTRADICTED** | 3 | [Pagin & Marsili, "Assertion", Stanford Encyclopedia of Philosophy (spr…](https://plato.stanford.edu/archIves/spr2024/entries/assertion/) | <cite index="40-10,40-11">The entry stresses that being subject to the norm, not conforming to it, characterises assertion, and that an assertion viol… |
| **CONTRADICTED** | 3 | [Lackey, "Group Assertion", Erkenntnis, 2018; The Epistemology of Group…](https://philarchive.org/archive/HYSOGL) | <cite index="55-9,55-12">In Lackey's uninformed-spokesperson case, a spokesperson who does not know the company's beliefs speaks on a matter she is au… |
| **ADJACENT** | 2 | [Nickel, "Artificial Speech and Its Authors", Minds and Machines, 2013](https://link.springer.com/10.1007/s11023-013-9303-9) | <cite index="50-7">Nickel's proxy speech is a notion in which responsibility for artificial speech acts is assigned legally or conventionally to an en… |
| **ADJACENT** | 2 | ["Who asserts when no one asserts? Functionalism, proxy responsibility,…](https://link.springer.com/article/10.1007/s11229-026-05807-3) | <cite index="24-4">The Synthese paper sets functionalist accounts against proxy-based views that trace accountability back to the humans or organisati… |
| **ADJACENT** | 2 | [Air Canada chatbot case (Moffatt), as reported in "AI Governance for I…](https://arxiv.org/pdf/2608.02311) | <cite index="5-1">The tribunal held that Air Canada did not take reasonable care to ensure its chatbot was accurate, and that the airline was responsi… |
| **ADJACENT** | 2 | [Kneer, "Can a Robot Lie? Exploring the Folk Concept of Lying as Applie…](https://onlinelibrary.wiley.com/doi/10.1111/cogs.13032) | <cite index="64-7">Kneer found that ordinary people attribute deceptive intentions to artificial agents, judge a robot lie to be a lie, and blame robo… |
| **SUPPORTED** | 1 | ["Mitigating Automation Bias in Generative AI Through Nudges: A Cogniti…](https://www.sciencedirect.com/science/article/pii/S1877050925030042) | <cite index="30-3">Automation bias is described as users over-relying on AI outputs without sufficiently questioning or verifying them.</cite> <cite i… |

**What is left.** Granting that proxy accounts (Nickel, Green & Michel, Arora) already tie assertion to the principal's responsibility, and that Arora already limits proxy assertion to utterances whose designers' epistemic states can be linked to them, what survives is this: on a view where assertion is individuated by its content and its epistemic norm, a deployer who authorises a generator to produce outputs she has no means of identifying in advance does not thereby assert each output. She is better described as giving a reliability guarantee. This has to be argued from a premise that commitment to a content requires a means of identifying it, not from norm-violation alone, and it has to explain why authorising a Lackey-style spokesperson differs from authorising an LLM.

**Not found.** I found no source stating the thesis's specific premise (commitment to a content requires a way of identifying that content at or before the act) as the ground for denying deployer assertion. I also found no source that explicitly recasts the proxy relation as endorsing a reliability level. I could not read the primary texts of Green & Michel, Arora, or Butlin & Viebahn, only abstracts, snippets and secondary reports. The 'whatever the system says under C, I say' conditional speech-act formulation did not turn up in anything I read, so my check of that part of the Green & Michel ascription is incomplete. The empirical search left philosophy but did not reach the phenomenon itself: I found automation-bias studies, folk-lying experiments and a legal case, and nothing from linguistics or sociology on institutional or corporate speech, spokesperson practice, or what recipients take a deployer to be committed to. I did not search the assurance or guarantee view of testimony or assertion (Moran, Hinchman, Goldberg), or other work on whether recorded or read-aloud messages are assertions, which are the closest natural homes for the 'guarantee' reading. I did not run searches on the Wachter/Mittelstadt 'careless speech' line or on Ludwig's work on proxy and group speech, so possible anticipations there are unchecked. Most of this literature is paywalled, so these silences are weak evidence.


### From the Stanford Encyclopedia — assertion

- **CONTRADICTED** (5/5) — Being subject to the norm is what makes something an assertion. Failing to meet the epistemic condition does not remove the act's status as an assertion. This blocks the thesis's inference from 'the deployer lacks the epistemic position' to 'the deployer does not assert'. — *Williamson 2000; Goldberg 2015; Montminy 2013a (Individuation, A3)*
  > It should be emphasized here that it is being subject to the norm that characterizes assertion, not conforming to the norm. An assertion that violates the norm is still an assertion.
- **ANTICIPATED** (4/5) — Taking on a guarantee or accepting responsibility for truth is not an alternative to asserting. Commitment accounts treat it as what asserting consists in, so 'takes on a guarantee' collapses back into assertion. — *Peirce; Alston 2000; Watson 2004; Moran 2005; Hinchman 2013; Carson 2006; Brandom 1994*
  > some authors write that assertions guarantee (Peirce [CP]: 5.543; Watson 2004: 66), assure (Moran 2005, Hinchman 2013) or warrant (Carson 2006) that their content is true.
- **ANTICIPATED** (3/5) — Deferral of responsibility to another source is already part of assertion. A speaker may pass the burden of grounds to an upstream source, so reliance on a process one does not oneself know to be right is not obviously non-assertoric. — *MacFarlane 2003; Goldberg 2015*
  > to defer this responsibility to another asserter on whose testimony one is relying.
- **ANTICIPATED** (4/5) — Proper assertion without the speaker's own belief or knowledge: teacher-style 'selfless' assertions relay content the speaker does not hold. This is the nearest model for institutional telling, and it is used against KNA and in favour of JNA. — *Lackey 2007, 2008; replies by Montminy 2013a, Turri 2015, Milić 2017*
  > Intuitively, it would be appropriate for Stella, as a teacher, to assert (31). However, (KNA) predicts that (31) is incorrect
- **SUPPORTED** (2/5) — Assertion as the outward sign of a judgment, and assertion as the expression of, or representation of oneself as having, belief or knowledge. Where no state of the principal's is expressed, these accounts give a route to denying assertion. — *Frege 1918a; Black 1952; Davidson 1984; Unger 1975; Slote 1979; Pagin 2011, 2020*
  > For the speaker, part of the reason for using a particular sentence is that it is true (in context); that is, the speaker believes, with a sufficient strength, that the sentence expresses a true proposition, and utters it partly because of that.
- **ADJACENT** (3/5) — The justification-type norms, including the reliability-friendly variant requiring justification to believe one is in a position to know, would let a deployer with good grounds for trusting the process meet the norm. The thesis's antecedent 'epistemic-position norm' is therefore underspecified, and the entry reports experimental evidence tipping toward JNA over KNA. — *Smithies 2012; Lackey 2007; Kneer 2017; Reuter & Brössel 2019; Marsili & Wiegmann 2021*
  > p is assertable only if you have a justification to believe that you are in a position to know that p
- **ADJACENT** (2/5) — Norm-sceptics who deny any assertion-specific norm, or place norms only on later reactions such as defending or retracting. This undermines the conditional's antecedent. — *Rescorla 2009a; Greenberg 2020; Cappelen 2011, 2020 (bibliography only)*
  > argues there is no norm at all for proper making of assertions. There are only norms that govern later reactions.
- **ADJACENT** (2/5) — Open questions about what intentions an asserter needs: must the speaker intend the utterance to be an assertion, and must it be voluntary? Also Austin's speaker-content assertion verbs. These bear on whether automated output can be the principal's assertion at all. — *Entry's own open question; Austin 1962; Searle 1969; Bach & Harnish 1979*
  > must he intend it to be an assertion? Must it be made voluntarily?

**Nearest positions.** Knowledge norm as constitutive and individuating, with violators still asserting — Williamson 2000 (with Goldberg 2015, Montminy 2013a); Commitment / accountability accounts, on which guaranteeing or taking responsibility is what asserting is — Peirce, Alston 2000, Brandom 1994, Watson 2004, Green; Selfless and relayed assertion as proper assertion without the speaker's own belief — Lackey 2007 (JNA) against KNA defenders such as Turri 2015 and Montminy 2013a; Belief- or knowledge-expression and self-representation accounts — Davidson, Unger, Slote, Bach & Harnish 1979, Pagin

**The entry is silent on.** Any non-agent or automated source of the content, including generative systems, transducers and machine-generated text. It also says nothing about institutional, corporate or delegated speakers, principals and agents, or authorship and responsibility gaps. It never asks whether a speaker whose utterance content is fixed by something other than their own mental state asserts at all. The nearest it comes is the relaying teacher (Lackey's Stella) and MacFarlane's deferral to another asserter, both of which assume a human source.


### From the Stanford Encyclopedia — ethics-ai

- **ANTICIPATED** (4/5) — LLM outputs create a 'testimony gap'. Testimony, and so the epistemic standing of what is said, cannot be straightforwardly transferred from a system to its users. The entry cites this in the opacity section and again in the politics section. — *Robert Sparrow and Flenady 2025*
  > we need to avoid a “testimony gap” (Robert Sparrow and Flenady 2025)
- **ANTICIPATED** (3/5) — LLM 'hallucinations' are bullshit in Frankfurt's sense, i.e. output indifferent to truth. This is a speech-act-adjacent diagnosis of unreviewed generative output. — *Hicks, Humphries and Slater 2024; Frankfurt 2005*
  > Others have argued that the “hallucinations” that plague LLMs are a form of this “bullshit” (Hicks, Humphries, and Slater 2024)
- **SUPPORTED** (2/5) — Responsibility for AI-mediated outcomes is distributed across many actors, and some views drop the assumption that every outcome has an answerable party. The thesis can build on this by recasting the deployer's relation to output as taking on a guarantee or process-responsibility. — *Taddeo and Floridi 2018; Simpson and Müller 2016; Tigard 2021; Königs 2022*
  > “The effects of decisions or actions based on AI are often the result of countless interactions among many actors, including designers, developers, users, software, and hardware. … With distributed agency comes distributed responsibility.”
- **SUPPORTED** (2/5) — LLMs and generative systems are not agents in the thick sense, since they lack an individual agent, their own norms, and the ability to reflect on values. Floridi allows only a thin, reactive 'agency without intelligence'. This helps the claim that the content comes from a transducer, not from a speaker's epistemic state. — *Barandiaran and Almendros 2024; Floridi 2023a; Dung 2025*
  > There is no individual agent, the agent does not generate its own norms, and the agent is not shaped by its interaction
- **SUPPORTED** (1/5) — The entry separates causes from reasons. Explanation in terms of reasons a rational agent would give is what counts for responsibility, and an opaque system supplies only causes. This parallels content fixed by a transducer rather than by the principal's epistemic state. — *Zednik 2021; Sullivan 2022; Zerilli 2022*
  > the typical distinction is between the causes that lead to a decision and the reasons that a rational agent would provide, where the latter is what counts for responsibility
- **ADJACENT** (2/5) — Guarantee-style and process-based standards for machine output are already proposed as alternatives to human justification. These include a right to a 'well-calibrated machine decision', and existing product liability and non-deception rules that cover deployers. — *Huq 2020; the entry on HRI/business ethics*
  > some authors have argued that instead we have a right to right to a “well-calibrated machine decision” (Huq 2020)
- **ADJACENT** (2/5) — Caution about whether traditional epistemology fits AI-mediated knowledge. The entry doubts that notions such as true justified belief are suitable, which could be turned against importing an epistemic-position norm of assertion. — *Alvarado 2023 (epistemic technology); the entry's own remark*
  > it remains to be seen whether notions and questions from traditional epistemology (about the conditions for true justified belief) are suitable for the many ways in which human perception and knowledge are impacted by AI technologies
- **ADJACENT** (1/5) — AI-generated content threatens the epistemic practices of belief and knowledge formation, and fake content erodes the reliability of digital evidence. This supports the stakes of the thesis, but the entry does not say who is the speaker. — *Rini 2020; Sparrow and Flenady 2025*
  > the basis of our epistemic practices ... for establishing belief and knowledge is threatened by this development (Rini 2020; Robert Sparrow and Flenady 2025)

**Nearest positions.** Testimony gap for LLM output — Robert Sparrow and Flenady 2025; LLM hallucination as Frankfurtian 'bullshit' — Hicks, Humphries and Slater 2024 (after Frankfurt 2005); Distributed agency and responsibility, including scepticism about responsibility gaps — Taddeo and Floridi 2018; Simpson and Müller 2016; Tigard 2021; Königs 2022

**The entry is silent on.** The entry says nothing about assertion, norms of assertion (knowledge, justification or epistemic-position norms), or speech-act theory. It also does not discuss whether deployers, institutions or corporations assert what their systems output, or the 'endorsing a process / taking on a guarantee' distinction. Nor does it cover the generalisation to all unreviewed automated output, or the claim that much institutional 'telling' is not assertion. The testimony-gap and bullshit citations are bare references with no argument.


### From the Stanford Encyclopedia — speech-acts

- **SUPPORTED** (1/5) — Assertion carries an epistemic norm, distinguished from conjecture or guessing by the 'How do you know?' challenge and a retraction obligation. The thesis can build on this. — *Williamson 1996 (knowledge-manifestation norm); Green 2017; Green's own commitment-based account*
  > the former purports to be a manifestation of knowledge, while the latter does not. This is suggested by the fact that it is appropriate to reply to the assertion with, “How do you know?”
- **SUPPORTED** (2/5) — Speech acts are overt commitments to a content, individuated by norms. This lets the thesis say that a deployer who undertakes only a different commitment (a guarantee, an endorsement of a process) performs a different act. — *Green (Section 5.3); the scorekeeping view*
  > When you overtly display a commitment characteristic of that speech act, you have performed that speech act.
- **SUPPORTED** (2/5) — Speech acts require speaker meaning and intention. Merely uttering a sentence, or a sentence being produced, does not suffice. This favours the claim that machine-generated sentences are not the deployer's assertions. — *Green; Strawson 1964*
  > neither a sentence, nor even the utterance of a sentence, is sufficient on its own for the performance of a speech act
- **ADJACENT** (3/5) — Illocutionary commitment can arise by entailment without the speaker intending the act. A deployer may be committed to the outputs, or to related contents, even without asserting them. — *Searle & Vanderveken 1985; Green*
  > it is difficult to see how one can perform S n while having no intention of performing a speech act at all.
- **ADJACENT** (3/5) — Speech act theorists allow speech acts to be performed by uttering performative-like frames or by invoking conventions. Institutional 'telling' could be assertion by convention or standardized practice. — *Bach & Harnish (standardization); Reimer (illocutionary conventions); Searle (constitutive rules)*
  > a sufficiently common practice of issuing assertions with performative effect enables speakers and hearers to bypass complex inferential reasoning
- **ADJACENT** (2/5) — Intentional undertaking of a publicly accessible commitment is required. Mere trying or common knowledge of intent is not enough. This bears on whether the deployer undertakes any commitment to the specific content. — *Green 2013*
  > speech acts involve intentional undertaking of a publicly accessible commitment
- **ADJACENT** (2/5) — Assertion by proxy or delegated speech. The entry notes that indirect or delegated acts depend on intentions and manifestness, and treats conversation as a scorekeeping practice where assertion updates common ground. — *MacFarlane 2011; Stalnaker; Lewis; Roberts*
  > Such an approach will, however, face a difficulty in explaining how two speech acts with the same content... will make different conversational contributions.

**Nearest positions.** Knowledge/epistemic norm of assertion, distinguishing assertion from conjecture by the 'How do you know?' challenge — Williamson 1996, Green 2017; Speech acts as overt undertaking of commitments individuated by norms, with commitment spreading by illocutionary entailment — Green; Searle & Vanderveken 1985; Conventionalist and standardization accounts, on which assertion or performative force can be secured by practice rather than the speaker's epistemic state — Searle, Austin, Bach & Harnish, Reimer

**The entry is silent on.** The entry does not discuss automated, machine-generated or transducer-fixed outputs, or whether deployers or institutions (as opposed to individual speakers) assert. It does not discuss corporate or institutional speakers, delegated speech, or the distinction between endorsing a process and asserting its output. Its only nearby cases are the somniloquist, jokers and actors, and photocopy machines (as an addressee under Davis 1992). It also does not say that assertion is governed by an 'epistemic-position' norm specifically; it gives only the knowledge-based 'How do you know?' challenge and a commitment-to-defend account.

<details><summary>8 searches</summary>

- `Arora assertion proxy LLM chatbot output who is responsible`
- `Green and Michel "Assertion, machine speech" proxy assertion`
- `can large language models assert? knowledge norm of assertion chatbot`
- `automation bias deploying generative AI outputs unreviewed responsibility psychology experiment`
- `Stanford Encyclopedia of Philosophy assertion norms proxy assertion`
- `Nickel "Artificial Speech and Its Authors" proxy speech responsibility`
- `Lackey group assertion spokesperson institution speaks without believing`
- `Kneer Auer AI lies deceive attribution laypeople experiment chatbot deployer blame`

</details>

