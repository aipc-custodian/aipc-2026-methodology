# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [intention](https://plato.stanford.edu/entries/intention/), [speech-acts](https://plato.stanford.edu/entries/speech-acts/), [action](https://plato.stanford.edu/entries/action/)
*The theses concern whether a communicative intention controls output or act at the grain of illocutionary force, so they belong to the entry on intention (Wu's Many-Many Problem, control conceptions), the entry on speech acts (illocutionary force versus string), and the entry on action (the control and selection debate).*


## Attah supplies an act-grained template (Levelt's preverbal force-bearing message) but only output-grained evidence for transformers. No argument yet s…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **ANTICIPATED** | 2 | [Nuhu Osman Attah, "Do language models lack communicative intentions?",…](https://philarchive.org/archive/ATTTMP-2) | Attah's control conception makes a state intentional only if it solves Many-Many Problems, i.e. maps varied situations reliably onto appropriate respo… |
| **ADJACENT** | 3 | [Patrick Butlin & Emanuel Viebahn, "AI Assertion", Ergo 12, 2025](https://philpapers.org/rec/BUTAAJ) | They argue that assertion requires outputs with descriptive functions and being capable of being sanctioned by interacting agents. Pre-trained LLMs fa… |
| **ADJACENT** | 3 | ["Where's the Plan? Locating Latent Planning in Language Models with Li…](https://arxiv.org/pdf/2605.07984) | The workshop paper asks whether models form internal representations of future outputs that causally shape generation without showing in behaviour. Th… |
| **ADJACENT** | 2 | [Nuhu Osman Attah, "Do language models lack communicative intentions?",…](https://www.researchgate.net/publication/391019058_Do_language_models_lack_communicative_intentions) | The text I could reach maps a dialog system's dialog manager, generation module and state representations onto the Conceptualizer, Formalizer (sic) an… |
| **ADJACENT** | 2 | [Nuhu Osman Attah, "Do language models lack communicative intentions?",…](https://www.researchgate.net/publication/391019058_Do_language_models_lack_communicative_intentions) | A fragment suggests Attah considers a worry that 'many illocutionary effects' would remain even if intentions were construed narrowly, and that LMs ap… |
| **ADJACENT** | 2 | [Reto Gubelmann, "Large Language Models, Agency, and Why Speech Acts ar…](https://philpapers.org/rec/GUBLLM) | Gubelmann argues that using language is acting, that LLMs cannot act because they lack intentions, and that this is because agents with intentions mus… |
| **ADJACENT** | 2 | ["Large-scale text pre-training helps with dialogue act recognition", I…](https://aclanthology.org/2021.iwcs-1.16.pdf) | The IWCS paper uses dialogue act recognition to test how well BERT represents utterances, and finds task-specific fine-tuning essential. The arXiv pap… |
| **SUPPORTED** | 1 | [Willem J. M. Levelt, "Producing spoken language: a blueprint of the sp…](https://www.mpi.nl/world/materials/publications/levelt/Levelt_Producing_spoken_language_1999.pdf) | Levelt discusses boundary tones as having illocutionary function. He gives an example where a speaker starting 'what do you need?' switches to a yes/n… |
| **SUPPORTED** | 1 | [Review of Levelt, "Speaking: From Intention to Articulation", MIT Pres…](https://aclanthology.org/J90-1012.pdf) | The reviewer describes three modules, Conceptualizer, Formulator and Articulator, plus a Lexicon, and says the Conceptualizer structures the ideas to … |
| **SUPPORTED** | 1 | ["Extracting Algorithms in Pre-trained LLMs: A Case on Hidden Markov Mo…](https://arxiv.org/pdf/2607.22646) | The first shows that a representation can be decodable without being causally used, so decodability and causal use must be tested separately. The seco… |

**What is left.** Attah gives a functional-role mapping and a control conception that asks for sensitivity of response to situation, but the sources I could reach give no evidence, from him or from the interpretability literature, that any transformer state encodes illocutionary force-type and causally governs it upstream of lexical and syntactic choice, with content held fixed. Whether 'plausibly recapitulate' is warranted therefore turns on an interpretability question that existing latent-planning work has addressed only for lexical targets such as rhyme words. The claim should be narrowed to Attah, and the grouping with Gubelmann and Butlin & Viebahn dropped or heavily qualified, since their arguments do not run on the output/act grain.

**Not found.** I did not find the full text of Attah's transformer-to-Levelt comparison, so I could not confirm that he writes 'plausibly recapitulate' or exactly what he says about transformer internals. That was only a snippet-level check. I found no paper that intervenes on force or speech-act-type representations in an LLM with propositional content held fixed, and none that argues the output-control/act-control distinction in philosophy of AI. I found no existing survey that reconciles control-based accounts of intention with Levelt-style models for LLMs, and no empirical psycholinguistics paper comparing LLM production to Levelt's Conceptualizer at the illocutionary level. My searches did leave philosophy, reaching interpretability, planning probes and dialogue-act NLP. They did not reach psycholinguistic work on illocutionary force in the preverbal message beyond Levelt himself, nor Wu's own work on action and attention. Most of the interpretability literature is recent preprints and workshop papers I could only skim, and my searches would miss anything paywalled or filed under different terms (e.g. 'communicative function', 'pragmatic intent', 'dialogue move'). A clean result here is weak evidence about a large and fast-moving literature.


### From the Stanford Encyclopedia — intention

- **SUPPORTED** (2/5) — Matching an intention's output is not enough for intentional action. The state must bear the right causal relation to what is produced. This is the causal-deviance problem, and it backs the demand for more than output-grained evidence. — *Davidson 1973 (causal deviance); Setiya, Mele, Thalberg, Hyman as respondents*
  > the condition of doing A because one so intends looks insufficient. For it says nothing about the causal path from intention to action.
- **SUPPORTED** (2/5) — Intention is individuated by functional role: a conduct-controlling state that serves as input to further reasoning. A state counts as an intention by what it does, not by the outputs it correlates with. — *Bratman 1987*
  > conduct-controlling pro-attitudes, ones which we are disposed to retain without reconsideration, and which play a significant role as inputs to [means-end] reasoning
- **SUPPORTED** (2/5) — Intention as a representation that guides and controls what it represents. This ties counterfactual and causal sensitivity to the content's being act-shaped. — *Setiya's own gloss, offered on behalf of mental-state theorists*
  > if intention is a representation that is such as to guide and control what it represents, its object must be as such as to be guided
- **ADJACENT** (2/5) — Intention's proper object is an action, something one does, not a proposition. This is an act-grained template of a sort, though about intending rather than speech-act force. — *Thompson 2008; Baier 1970; Moran and Stone 2009. Denied by Davis 1984 and Ferrero 2013.*
  > its proper object—what one is on the way to doing—is not a proposition or state of affairs, but something one might do.
- **ADJACENT** (3/5) — 'Causally upstream' need not mean temporally prior. Intention may be a simultaneous, sustaining cause, and Anscombe denies that the intention–action relation is efficient-causal at all (she takes it to be formal). — *Thalberg 1984; Setiya 2007a (simultaneous sustaining cause); Anscombe 1983 (formal, not efficient cause)*
  > causal theorists may deny that claim about the temporality of causes, conceiving intention as the simultaneous, sustaining cause of what one is doing
- **ADJACENT** (2/5) — Prospective intention versus intention in action. A preverbal message prior to speaking resembles prospective intention, while ongoing formulation resembles intention in action. The entry says intention in action need not be preceded by a prior intention. — *Searle 1983*
  > I can wave my arm intentionally without planning in advance.
- **ADJACENT** (1/5) — A state that merely tracks or predicts behaviour is not thereby an intention. The 'promiscuity' worry is that a mechanism keyed to expectations over-generates, because it would motivate beliefs that are not intentions. — *Bratman 1991, against Velleman*
  > it predicts that we will be just as strongly motivated by beliefs that do not constitute intentions, like the belief that I am going to trip over the step

**Nearest positions.** Causal/functional theory of intention as an action-guiding state — Davidson (primary reason as cause), Davis 1984, Mele 1992; Planning theory of intention as a conduct-controlling, reasoning-input state — Bratman 1987; Non-causal or formal-cause view (Anscombe, Thompson), on which 'causally upstream' is the wrong test

**The entry is silent on.** Everything specific to the thesis: LLMs and transformers, Levelt's speech-production model and the preverbal message, illocutionary or speech-act force, and counterfactual-sensitivity tests for model internals. The entry does not discuss attributing intention to artificial systems or interpreting internal states by their outputs, nor linguistic formulation. Only the general causal-role versus output-fit contrast is available.


### From the Stanford Encyclopedia — speech-acts

- **SUPPORTED** (1/5) — Output (the words, even with mood and punctuation) underdetermines force, so output-grained evidence cannot by itself fix which act was performed. This is the premise for the thesis's burden claim. — *Austin, Davidson (Autonomy Thesis), Green*
  > Mood together with content underdetermine force.
- **SUPPORTED** (1/5) — Producing a performative or force-marked string is not sufficient for performing the act. The somniloquist utters 'I hereby promise…' and promises nothing, and Davidson's joker or actor simulates assertion with any force indicator. — *Green (somniloquist); Davidson 1979*
  > every joker, storyteller, and actor will immediately take advantage of the strengthened mood to simulate assertion.
- **SUPPORTED** (1/5) — Speech acts have structural analogues in mental states: assertion expresses belief and promise expresses intention. This gives a general template for act-typed internal states, which is the kind of 'act-grained' state the thesis wants evidence of. — *Searle 1983; Pendlebury 1986*
  > Searle 1983 delineates structural analogies between speech acts and the mental states they express.
- **ADJACENT** (2/5) — The entry contains a close structural parallel to a burden-of-proof argument. Bertolet holds that positing a further (indirect) speech act is explanatorily unmotivated when a simpler indication of intentional state suffices. This is the same kind of parsimony move the thesis makes against 'plausibly recapitulate'. — *Bertolet 1994, 2017; replied to by McGowan et al. 2009*
  > Postulation of a further speech act beyond what has been (relatively) explicitly performed is, he contends, explanatorily unmotivated.
- **ADJACENT** (3/5) — Force is tied to overt commitment and to intentions that are efficacious and publicly accessible. Force is not fixed by internal states or by manifested intention alone. This bears on whether any internal LLM state could make an output an act of a given type, and on the thesis's 'counterfactually sensitive to act type'. — *Green 2013, 2019; Strawson 1964; Grice*
  > speech acts involve intentional undertaking of a publicly accessible commitment; further, that commitment is not undertaken simply by virtue of my intending to undertake it
- **ADJACENT** (2/5) — Speaker meaning may not require intentions to produce effects on an addressee at all. Davis's cases include uncooperative photocopy machines and speaking to pre-linguistic infants. A referee could use this to ask whether non-human or non-intending producers can perform speech acts. — *Davis 1992; Green 2019 (overt manifestation view)*
  > Davis (1992) provides a range of cases such as speaking to pre-linguistic infants, uncooperative photocopy machines, and photos of deceased loved ones.
- **ADJACENT** (2/5) — Force and content are different categories (functional group versus radical). A representation encoding content does not thereby encode force, and force is not a further component of content. This bears on whether a 'force-bearing' preverbal message is coherent as a single representation. — *Stenius 1967; Searle's F(p) form*
  > the forwarding of a Proposition with a particular illocutionary force is not itself a further component of Propositional content.

**Nearest positions.** Force is underdetermined by content and mood (so surface output is weak evidence of force) — Austin, Davidson, Green; Force as an aspect of speaker meaning, grounded in overt commitment and intention rather than in the produced string — Strawson, Grice, Green; Skepticism about positing extra acts or states beyond what output and context indicate (an explanatory-motivation burden) — Bertolet

**The entry is silent on.** Almost everything specific to the thesis. The entry has no discussion of language production or psycholinguistics (no Levelt, no preverbal message, no formulation stage), no discussion of LLMs, transformers, or interpretability, and no discussion of causal or counterfactual tests for internal states. 'Artificial intelligence' appears only in the introduction's list of influenced fields, and Shoham 1993 appears only in the bibliography. Attah is not mentioned. The entry also gives no criteria for deciding when a computational state counts as act-typed.


### From the Stanford Encyclopedia — action

- **SUPPORTED** (1/5) — Sensitivity/feedback conditions on intentional action. A state counts as an action-producing state only if the behaviour it yields varies with conditions and information. This is the template for a 'counterfactually sensitive to act type' test. — *Peacocke 1979; Bishop 1989; Smith 2012*
  > the climber's bodily movements would not count as an intentional action because they would not be sensitive to variations in conditions and information on what needs to be done
- **SUPPORTED** (1/5) — Davidson's Challenge: matching a rationalizing description is not enough. The state that explains must be the one that actually produces the behaviour. Non-causal rivals meet this with counterfactual tests. — *Davidson 1963; Mele 1992, 2013; Löhrer and Sehon 2016*
  > The only way we can explain the difference between potentially rationalizing, but non-explanatory belief-desire pairs, is that the belief-desire pair that genuinely explains the action, the primary reason, also causes the action.
- **SUPPORTED** (1/5) — Causal-pathway constraints: the right state must be the proximate or guiding cause, not merely a correlated antecedent. Hence the 'causally upstream of formulation' requirement. — *Mele 1992 (proximate cause); Frankfurt 1978 and Setiya 2007 (guidance)*
  > an action is intentional only if, for instance, the formation of an intention to φ is the proximate cause of your φ-ing
- **ADJACENT** (2/5) — Empirically informed responses to deviance that look to the detail of cognitive control mechanisms (attention, motor-level intentions, flexible-agency pathways) rather than to outputs alone. — *Wu 2016; Mylopoulos and Pacherie 2019; Shepherd 2021*
  > attention to the details of control mechanisms implemented at the cognitive level yields a response to the deviance problem
- **ADJACENT** (2/5) — Attributing agency from behaviour versus from internal capacities. The entry's schema (premise 1: agency requires features F; premise 2: the system has them) and its empirical disputes over animals parallel the burden-of-evidence structure. — *Godfrey-Smith 2003; Kaufmann 2015; Davidson 1982/2003; Steward 2009*
  > these folk concepts may be particularly problematic when applied to animals
- **ADJACENT** (1/5) — Act-type grain: actions are intentional only under some descriptions. The entry's discussion of description-relativity and individuation is the nearest thing to 'act-grained' states. — *Davidson 1971; Anscombe 1957; Kim and Goldman (fine-grained); Charles 1984*
  > an event is an intentional action under a certain description, if and only if, there is a true rationalizing explanation of the event under this description

**Nearest positions.** Causalism with a causal-pathway or sensitivity condition on deviance — Davidson; Peacocke, Bishop, Smith; Mele; Frankfurt; Setiya; Teleological/counterfactual answers to Davidson's Challenge — Löhrer and Sehon, Wilson, Schueler; Empirically informed control-mechanism accounts — Wu, Mylopoulos and Pacherie, Shepherd

**The entry is silent on.** Everything specific to the thesis. The entry never mentions LLMs, transformers, speech acts or illocutionary force, Levelt or the preverbal message, linguistic formulation as a stage, interpretability or probing evidence, or a distinction between output-grained and internal-state evidence for artificial systems. Robots are mentioned once and set aside: 'Similar questions arise for children and robots, but our focus shall be on ... animal agency.' The entry also does not discuss 'Attah' or the 'plausibly recapitulate' move.

<details><summary>8 searches</summary>

- `Attah intention large language models Levelt Conceptualizer Formulator Articulator Many-Many Problem`
- `LLM probing illocutionary force speech act representation causal intervention hidden states`
- `Gubelmann LLM speech acts intentions Searle`
- `Butlin Viebahn AI language production intentions`
- `Levelt preverbal message illocutionary force conceptual preparation speech production model`
- `language models plan ahead before generating tokens intent representation interpretability planning`
- `Attah "Do language models lack communicative intentions" transformer attention Conceptualizer plausibly Levelt architecture`
- `language models internal representation of speech act type dialogue act probing steering independent of content`

</details>

