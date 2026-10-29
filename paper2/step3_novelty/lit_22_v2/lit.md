# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [intention](https://plato.stanford.edu/entries/intention/), [speech-acts](https://plato.stanford.edu/entries/speech-acts/), [artificial-intelligence](https://plato.stanford.edu/entries/artificial-intelligence/)
*The theses concern whether communicative intention, understood as selecting an illocutionary act (Wu's Many-Many Problem, attention-like control), is realised in LLMs, so the entries on intention and speech acts hold the positions at issue, and the artificial intelligence entry is the closest available match for the LLM side.*


## Attah supplies an act-grained template (Levelt's preverbal force-bearing message) but only output-grained evidence for transformers. No argument yet s…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **PRECEDENT · FRAMEWORK (snippet)** | 2 | [(Author name not visible in the snippet; PhilArchive ID WILIRI-4) "Int…](https://link.springer.com/article/10.1007/s11098-026-02605-y) | The paper surveys five properties associated with intentions and assesses two candidate classes of LLM representations against them. It assumes a view… |
| **ADJACENT (snippet)** | 2 | [Attah, "Do language models lack communicative intentions?", Synthese, …](https://link.springer.com/article/10.1007/s11229-025-05022-6) | For an internal state to count as an intention, it must reliably map the right elicitative situations to the right solutions, i.e. solve Many-Many Pro… |
| **ADJACENT (snippet)** | 2 | [Gubelmann, "Large Language Models, Agency, and Why Speech Acts are Bey…](https://www.alexandria.unisg.ch/bitstreams/53bebe1f-a120-43d4-b4ac-09ec5d0e787c/download) | His argument runs: a speaker must be able to illocute; illocuting requires intentions; LLMs have no intentions. In the snippet his ground is that LLMs… |
| **ADJACENT (abstract)** | 2 | [Butlin & Viebahn, "AI Assertion", Ergo, 2023/2025](https://philpapers.org/rec/BUTAAJ) | They hold that an entity must produce outputs with descriptive functions and be capable of being sanctioned. They add that pre-trained LLMs fail the f… |
| **ADJACENT (snippet)** | 2 | [Secondary descriptions of Levelt, Speaking (1989): the 'Thirty years o…](https://www.tandfonline.com/doi/full/10.1080/23273798.2019.1652763) | The conceptualizer generates a preverbal message, the formulator a phonetic plan, and the articulator overt speech. A review notes an important design… |
| **ADJACENT (abstract)** | 1 | [Williams & Bayne, "Chatting with bots: AI, speech acts, and the edge o…](https://www.tandfonline.com/doi/abs/10.1080/0020174X.2024.2434874) | They argue that we need to make space for a category of proto-assertion, after finding the proxy-assertion and fictionalist responses unsatisfactory. |
| **SUPPORTED (secondhand)** | 1 | [Lindsey et al. 2025 (Anthropic planning features) and Todd et al. 2024…](https://link.springer.com/article/10.1007/s11098-026-02605-y) | As reported there, features for the rhyming end word were already active at the end of the prompt, before the second line began. Function-vector work … |
| **SUPPORTED (abstract)** | 1 | ["Where's the Plan? Locating Latent Planning in Language Models with Li…](https://arxiv.org/html/2605.07984v1) | It separates planning-compatible representations (detectable via probing) from causally active planning sites (established via activation patching). O… |

**Credit (precedents the thesis develops).** Williams 2026 (Philosophical Studies; author inferred from the PhilArchive ID) — applies a causal-representational, intervention-based test for intention-like states to LLMs, at the grain of function vectors and rhyme-planning features; Lindsey et al. 2025, as reported by Williams 2026 — evidence of causal planning features upstream of the written continuation (secondhand only); Todd et al. 2024, as reported by Williams 2026 — injecting task representations triggers task execution (secondhand only); 'Where's the Plan?' 2026 — the distinction between probe-readable and causally active planning sites; Attah 2025 — his own acknowledgment of an explanatory debt about how the control problem is solved; the thesis presses on exactly that debt

**Not found.** No ANTICIPATED or CONTRADICTED finding emerged, but the evidence is thin. I did not find any paper that probes or intervenes on illocutionary force or speech-act type in LLM internals, holding lexical content fixed. My one dialogue-act and steering query returned unrelated steering and probing work and corpus-pragmatics classification. I did not find a source that discusses the output-grain versus act-grain distinction in LLM intention. I did not see the passage where Attah says transformers 'plausibly recapitulate' Levelt: I saw only snippets of the Synthese article and of the dissertation abstract, and none mentioned Levelt. I could not confirm from primary text that Levelt's preverbal message carries force. I did not find any psycholinguistic paper that compares Levelt's blueprint to transformers directly. I saw Gubelmann, Butlin and Viebahn, and Williams and Bayne only as snippets or abstracts, so nothing here excludes a fuller treatment of grain in their texts. The thesis's description of Gubelmann and of Butlin and Viebahn as treating the grain as settled does not match what I saw, so check it before relying on it. I ran no search on the empirical literature in pragmatics or developmental psychology on how speakers represent force before formulating, and no search in philosophy of action on act-individuation. The empirical search therefore left philosophy only into ML interpretability and a little psycholinguistics, and a clean result should not be read as originality.


### From the Stanford Encyclopedia — intention

- **SUPPORTED** (2/5) — Matching an output to an intention is not enough. The state has to produce the output in the right way, and causal-deviance cases show that 'because one so intends' is insufficient without that. This backs the demand that an LLM state be causally upstream of formulation, not merely correlated with output. — *Davidson 1973; the causal-theory literature (Thalberg, Mele, Setiya, Hyman) as reported in the entry*
  > If I intend to be shaking in order to signal my confederate, and this intention makes me nervous, so that I shake, I am shaking because I so intend—though not intentionally. My intention did not cause me to shake ‘in the right way.’
- **SUPPORTED** (2/5) — Intention is individuated by functional role: its role in planning, in guiding conduct, and as input to further reasoning. That sets a state-level standard beyond output fit, close to the thesis's counterfactual-sensitivity requirement. — *Bratman 1987, as reported in the entry*
  > intentions are ‘conduct-controlling pro-attitudes, ones which we are disposed to retain without reconsideration, and which play a significant role as inputs to [means-end] reasoning’
- **ADJACENT** (2/5) — Rival to the 'causally upstream state' framing. Davidson's early view treats 'intention with which' as syncategorematic, a redescription of the action by its reason and not a state or event of the agent. Anscombe and the disjunctivists deny that execution of an intention is efferent causation, reading practical knowledge as formal cause. On these views output-grained facts can partly constitute the intention, so the causal-priority burden looks different. — *Davidson 1963; Anscombe 1963/1983; Thompson 2008; O'Brien, Rödl, McDowell, Marcus*
  > the phrase does not refer to an event or state of the agent, but is a way of redescribing what she is doing in terms of a ‘primary reason’
- **ADJACENT** (1/5) — Causal theorists can allow a simultaneous, sustaining cause, so the intention need not temporally precede action. This bears on what 'causally upstream of formulation' must mean for an incremental process. — *Thalberg 1984; Setiya 2007a*
  > conceiving intention as the simultaneous, sustaining cause of what one is doing

**Nearest positions.** Causal theory of intentional action with a deviance constraint (the state must cause the act in the right way) — Davidson 1973, Mele, Thalberg, Setiya; Functional-role / planning theory of intention (state individuated by its role as input to reasoning and guidance of conduct) — Bratman 1987; Non-causal or non-state views (intention as redescription, as being in progress, or as formal cause) — early Davidson, Anscombe, Thompson, Rödl

**The entry is silent on.** Everything specific to the thesis. The entry says nothing about speech acts, illocutionary force, Levelt's preverbal message, language production, Attah, transformers or LLMs, and nothing on counterfactual sensitivity to act type as a test for attributing intention-like states to machines. It is about human intention, so it has no view on the burden of proof for artificial systems.


### From the Stanford Encyclopedia — speech-acts

- **SUPPORTED** (1/5) — Force is underdetermined by what is said or observably done, and by content plus mood. Output-level evidence therefore cannot settle which act was performed. This backs the thesis's complaint that output-grained evidence for transformers is insufficient. — *Austin (the bow example, the 'You'll be more punctual' example); Davidson's Autonomy Thesis; the entry's own section 4*
  > the communicative significance of an act may be underdetermined by what has been said or observably done
- **SUPPORTED** (1/5) — Content and force are independent: content can stay fixed while force varies. This supplies a natural counterfactual test for whether a state is sensitive to act type (same content, different act). — *Stenius's radical/functional-group analogy; Searle's F(p); the entry's section 2.1*
  > a central tenet in the study of speech acts is that content may remain fixed while force varies
- **ADJACENT** (2/5) — Having an internal state that tracks or correlates with an intended act is not the same as performing or constituting that act. Neural evidence that someone is trying to tell you something does not show an assertion. Merely evincing a psychological state is not a speech act. — *Green 2013, 2020*
  > even if you were to find, on the basis of fMRI analysis of my neural activity, that I was trying to tell you that it's going to rain tomorrow, I still have not asserted anything about tomorrow's weather.
- **ADJACENT** (1/5) — Postulating a further act or force beyond what is explicitly performed is explanatorily unmotivated unless the evidence mandates it. This is a burden-of-proof structure like the thesis's. — *Bertolet 1994, 2017 (against McGowan et al. 2009)*
  > Postulation of a further speech act beyond what has been (relatively) explicitly performed is, he contends, explanatorily unmotivated.
- **ADJACENT** (2/5) — Speaker meaning, and hence force, depends on speaker intentions, which must be efficacious and manifest. A force-bearing internal state in a system would need to meet this condition before it counted as performing an act. — *Strawson 1964; Grice; Green*
  > speech acts involve intentional undertaking of a publicly accessible commitment

**Nearest positions.** Force/content independence, with force underdetermined by content and mood — Austin, Stenius, Searle, Davidson (Autonomy Thesis); Intentionalist account of force via manifest communicative intention — Strawson, Grice, Green; Skepticism about positing hidden acts or forces without mandating evidence — Bertolet

**The entry is silent on.** Everything specific to the thesis: LLMs or transformers, Levelt's model of speech production or its preverbal message, Attah, and the causal order between act-type representation and formulation. The entry does not discuss psycholinguistic production architecture or how to test machine states for sensitivity to act type.


### From the Stanford Encyclopedia — artificial-intelligence

- **ADJACENT** (2/5) — The entry flags that AI systems with impressive output-level performance (Watson, AlphaGo) may not have the understanding or general competence that the outputs suggest. It also says AI is measured by tests and performance rather than by whether the internal information-processing matches the human case. This is the nearest the entry gets to the output-grained versus internal-state distinction. — *The entry's own voice, drawing on Descartes' tests and on Levesque's challenges*
  > AI is first and foremost concerned with engineering computational artifacts that measure up to some test (where, yes, sometimes that test is from the human sphere), not with whether these artifacts process information in ways that match those present in the human case.
- **SUPPORTED** (1/5) — The entry reports that adversarial inputs raise doubts about whether benchmark performance reflects the real-world sensitivity of neural networks. This gives a thesis about missing counterfactual-sensitivity evidence something to build on. — *Szegedy et al. 2014, as reported by the entry*
  > The existence of such adversarial inputs... has raised doubts about how well performance on benchmarks can translate into performance in real-world systems with sensory noise
- **ADJACENT** (2/5) — The Turing Test operationalizes intelligence as linguistic indistinguishability, which is an output-grained criterion. The entry reports Descartes' challenge that machines cannot arrange speech appropriately to everything said, and this is a rival standard. — *Turing 1950; Descartes 1637; Nilsson 1998*
  > Passing in this sense operationalizes linguistic indistinguishability.

**Nearest positions.** Behaviour or test-based definition of AI (Human/Act quadrant): Turing, Nilsson, and Russell & Norvig's acting-rationally view, as reported in the entry; Descartes' language tests, which say outputs alone can reveal a machine's lack of understanding, as reported in the entry; The entry's own caution that machines meeting tests need not match human information-processing, and that benchmark performance may not generalize (Szegedy et al.)

**The entry is silent on.** The entry says nothing about LLMs or transformers, speech act theory, Levelt's model of speech production or preverbal messages, Attah, counterfactual sensitivity to act type, or causal upstreamness in formulation. The thesis's whole subject matter is absent, so nothing in the entry anticipates it.

<details><summary>8 searches</summary>

- `Attah intention large language models Levelt Many-Many Problem Wu`
- `probing LLM hidden states speech act illocutionary force representation`
- `Butlin Viebahn AI assertion language models`
- `Gubelmann pragmatic norms LLM speech acts assertion`
- `Levelt preverbal message transformer language model conceptualizer formulator`
- `Intention-like representations in language models? causal intervention planning representations`
- `Attah "Levelt" language models communicative intentions conceptualizer formulator transformer recapitulate`
- `linear probe dialogue act speech act type representation LLM steering intervention`

</details>

