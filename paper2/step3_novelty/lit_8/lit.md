# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [speech-acts](https://plato.stanford.edu/entries/speech-acts/), [assertion](https://plato.stanford.edu/entries/assertion/), [fiction](https://plato.stanford.edu/entries/fiction/)
*The theses ask whether chatbot outputs are serious assertions or non-serious (Searle/Austin) authorial pretence, which draws on the speech-acts entry, the assertion entry (sincerity and commitment conditions, and the debate over whether the model asserts), and the fiction entry (authorial pretence and make-believe).*


## Chatbot outputs are indexed to a represented speaker (the assistant character), so the make-believe need not sit in users, who can read literally. Whe…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **ANTICIPATED** | 3 | [Butlin & Viebahn, "AI Assertion", Ergo 12, 2025](https://www.researchgate.net/publication/394358591_AI_Assertion) | Assertion requires outputs with descriptive functions and capacity to be sanctioned. Pretrained LLMs that have not been fine-tuned fail the first requ… |
| **ANTICIPATED** | 3 | [Marks et al., "The persona selection model", Anthropic/Alignment Forum…](https://www.alignmentforum.org/posts/dfoty34sT7CSKeJNn/the-persona-selection-model) | LLMs learn to simulate diverse characters in pretraining, and post-training elicits and refines one Assistant persona. Interactions are 'something rou… |
| **CONTRADICTED** | 3 | ["The force of fictional discourse", Synthese, c. 2022; Cyzman on Searl…](https://link.springer.com/article/10.1007/s11229-022-03955-w) | Searle (1975b) is the canonical source of the pretence view, on which fictional statements are pretended illocutionary acts. The paper cites Searle's … |
| **ADJACENT** | 3 | [Williams & Bayne, "Chatting with Bots: AI, Speech Acts, and the Edge o…](https://philpapers.org/rec/WILCWB-3) | They ask whether chatbot output qualifies as assertion. They reject proxy-assertion and Mallory-style fictionalism, and propose a category of proto-as… |
| **ADJACENT** | 3 | ["Talking with Language Models" (arXiv 2610.09064, c. Oct 2026)](https://arxiv.org/html/2610.09064v1) | They say pretence or make-believe is not needed to explain most human–AI interactions, and contrast this with fictionalists (Mallory, Shanahan et al.,… |
| **ADJACENT** | 2 | [Mallory, "Fictionalism about Chatbots", Ergo, 2023 (as reported in Wil…](https://arxiv.org/pdf/2410.16645) | Mallory argues that engagement with chatbots is prop-oriented make-believe: outputs are literally meaningless but fictionally meaningful. Williams & B… |
| **ADJACENT** | 2 | [Chatbot apologies: Beyond bullshit (arXiv 2501.09910), discussing Mall…](https://arxiv.org/pdf/2501.09910) | The account is described as prop-oriented and world-oriented, and 'does not require that a user self-consciously pretend anything.' I could not tell f… |
| **ADJACENT** | 2 | [Gubelmann, "Large Language Models, Agency, and Why Speech Acts are Bey…](https://www.researchgate.net/publication/378425318_Large_Language_Models_Agency_and_Why_Speech_Acts_are_Beyond_Them_For_Now_-A_Kantian-Cum-Pragmatist_Case) | The argument runs: to be a speaker one must illocute, to illocute one needs intentions, LLMs have none, so LLMs are not speakers. He concludes that LL… |
| **ADJACENT** | 1 | Not found | Two searches returned nothing by an author named Attah on chatbot illocution. I cannot confirm what this person holds. |
| **SUPPORTED** | 1 | [Shanahan, McDonell & Reynolds, "Role play with large language models",…](https://arxiv.org/pdf/2305.16367) | A dialogue agent is described as role-playing a single character, or as a superposition of simulacra produced by a simulator. A secondary summary quot… |
| **SUPPORTED** | 1 | [Tracing Persona Vectors Through LLM Pretraining (arXiv 2605.13329); Wh…](https://arxiv.org/html/2605.13329) | Persona vectors from base checkpoints still steer fully post-trained variants, and the pretraining direction is never erased. The second paper reports… |

**What is left.** Mallory and the Williams & Bayne reading of him already give the chatbot a fictional-character index. Persona-selection and role-play work already says the base model is an author or simulator of characters and that post-training refines one. What survives is narrower: the claim that the authorial frame is a feature of the producer's speech act, assessed in Searle/Austin terms (the make-believe need not sit in users, who can consume the output literally), together with the question whether post-training moves the system out of that frame or only stabilises it. The 'literal reader of fiction-on-the-producer-side' structure, and the explanation of why the intention and sanction conditions look unmet, are the parts not found in the sources I retrieved. The Searle identification must be argued rather than assumed, because Searle's pretence is an intentional author's performance.

**Not found.** I did not find any source that applies Searle's or Austin's non-serious or pretended illocution to the model's own output on the producer side. I found none that describes users as literal consumers of producer-side fiction, and none that frames the serious-versus-authorial frame as the object of the realist/denier debate. I did not locate any work by Attah on this. I could not read Mallory (2026), Ruyant (2026) or Shanahan (2026), which 'Talking with Language Models' cites as fictionalist. They could anticipate the thesis more closely than anything above. I only saw abstracts, snippets and secondary summaries, mostly of paywalled work. Empirical coverage is incomplete: the search left philosophy only for ML interpretability and persona work (PSM and follow-ups). I ran no search for psychology, HCI or linguistics studies of how users interpret chatbot output (literal versus pretend uptake, anthropomorphism). The 'users read literally' half of the thesis is therefore untested against the empirical literature. I also did not search Austin on 'etiolations' and 'parasitic' uses, or the literature on fiction and unreliable-narrator assertion, which a referee may raise. This is not a clean result. It reflects a small slice of a large literature.


### From the Stanford Encyclopedia — speech-acts

- **ADJACENT** (2/5) — Davidson's argument that actors, jokers and storytellers can simulate assertion with any force-indicating device. Hare replies that a society could have a convention covering even stage and joking utterances. Green replies that assertion requires intentions that no convention can supply. This is the entry's only discussion of simulated or pretended force, and it bears on whether a chatbot's output counts as assertion. — *Davidson 1979; Hare 1989; Green 1997*
  > every joker, storyteller, and actor will immediately take advantage of the strengthened mood to simulate assertion.
- **SUPPORTED** (1/5) — An utterance is not sufficient for a speech act. A sentence uttered with no speaker-meaning behind it (the somniloquist) performs no speech act, and a speech act requires speaker meaning and intention. This gives the thesis a way to say that text output alone does not fix force and that the force has to be indexed to some speaker or intention. — *Green (entry author); Grice-based speaker-meaning account*
  > while talking in my sleep I might say, "I hereby promise to climb the Eiffel Tower," without thereby making any promise.
- **SUPPORTED** (2/5) — Speaker meaning, and so speech-acthood, need not involve intending cognitive effects in an addressee. Davis's cases include pre-linguistic infants, photocopiers and photographs. The overt-manifestation account of speaker meaning is built to cover them. This supports the thesis's point that the make-believe need not sit in the users. — *Davis 1992; Green 2019*
  > some authors have advocated a construal of speaker meaning as overtly manifesting an aspect of one's commitments or state of mind (Green 2019).
- **SUPPORTED** (1/5) — The entry says that what is manifest to one part of the audience may not be manifest to another, so a single utterance can be speaker-meant differently for different audience subsets. This is a precedent for the same output being taken literally by one party and as indexed to a character by another. — *Saul 2018, as discussed by Green*
  > What is manifest to one addressee may not be manifest to another, and a speaker may exploit this fact.
- **ADJACENT** (2/5) — Austin's felicity conditions and uptake: a speech act can misfire when the addressee does not respond appropriately, and a speaker can be disabled from performing a type of act by systematic denial of uptake. A referee could use this to ask what a user's literal reading does to the force of the output. — *Austin 1962; Langton 1993; Hornsby and Langton 1998; Bird 2002*
  > I cannot bet you $100 on who will win the election unless you accept that bet.
- **ADJACENT** (2/5) — Searle's weaker conventionalism and his view that manifesting an intention to perform an act suffices for performing it. A referee would raise these when the thesis invokes Searle. The entry reports them as accounts of real speech acts, not of pretended ones. — *Searle 1969, 1989; Strawson 1964*
  > Searle also takes it that manifesting an intention to perform a speech act is sufficient for the performance of that act.

**Nearest positions.** Davidson's argument that actors, jokers and storytellers simulate force, so no indicator guarantees it — Davidson 1979, with Hare 1989 and Green 1997 replying; Intention-based and overt-manifestation accounts of speaker meaning and force — Grice 1957, Strawson 1964, Green 2019; Uptake-dependent force and illocutionary silencing — Austin 1962, Langton 1993, Hornsby and Langton 1998, with Bird 2002 and Maitra 2009 dissenting

**The entry is silent on.** Chatbots and LLMs, or AI-generated utterances as speech acts, apart from the bare listing of artificial intelligence among the fields speech act theory has influenced (Shoham 1993 appears only in the bibliography). The entry never mentions fiction, make-believe or pretense as a category of speech act. It never attributes a 'pretended illocution' account to Searle, so that attribution gets no support from the entry. It does not discuss a represented or character speaker to whom an output is indexed, or training that changes an output repertoire.


### From the Stanford Encyclopedia — assertion

- **SUPPORTED** (2/5) — Asserting as representing oneself as believing or knowing. The thesis's 'represented speaker' indexing has an analogue in the representation-of-self view, which already separates the speaker's self-representation from what an audience is invited to believe, in the stage-actor case. — *Max Black (1952) and Davidson (1984); Unger (1975) and Slote (1979) for knowing; Green (2007) via expressive conventions*
  > in asserting that p the speaker represents herself as believing that p
- **SUPPORTED** (2/5) — Actor case. The entry says an actor represents himself as asserting without inviting the audience to believe he has the belief. This is the nearest thing in the entry to make-believe not sitting in the audience. — *the entry's own discussion in §4.1, in the Davidson/Black self-representation tradition*
  > But the audience not invited to believe that the speaker, that is, the actor, has that belief.
- **ADJACENT** (2/5) — Force-indicating conventions fail to be sufficient because they can appear in insincere or theatrical uses, with no corresponding force. This bears on whether chatbot output has assertoric force at all. — *Davidson (1979, 1984); Bach and Harnish (1979)*
  > any conventional sign could be used (and would be used) in insincere utterances, where the corresponding force was missing, including cases of deception, jokes, impersonation and other theatrical performances
- **ADJACENT** (3/5) — Pagin's prima facie informative account. Assertion is characterized by default speaker-side and hearer-side patterns tied to surface features, and the hearer's default uptake is credence updating. This fits the thesis's point that users can read literally, but the entry treats the hearer default as part of the account of assertion. — *Pagin (2011, 2020)*
  > it is the cognitive patterns associated with surface features, on the production and comprehension sides, that characterize assertion
- **ADJACENT** (2/5) — Austin's uptake and Strawson's point on conventional force. Illocution depends on the hearer's understanding, yet the entry notes that the speaker-content structure ('Bill asserted that p') is less dependent on uptake. This is relevant to whether users reading literally fixes the force. — *Austin (1962); the entry's own remark on speaker-content structure*
  > Bill still asserted that it was closed, since Bill believed she was still there
- **ADJACENT** (2/5) — Commitment accounts. If chatbot outputs lack a speaker who can be held accountable, commitment-based accounts (Peirce, Alston, Brandom) would deny assertoric status. The entry gives only the general structure, not the chatbot case. — *Peirce; Alston (2000); Brandom (1994); Green; Searle (1969)*
  > renders [the speaker] liable to the penalties of the social law
- **ADJACENT** (2/5) — Searle's rules, including the sincerity rule and the constitutive rule, together with the claim that an actor merely represents himself as asserting. The entry does not use 'pretended illocution' as a category. It lists Searle's five rules, which the thesis would have to apply. — *Searle (1969)*
  > Counts as an undertaking to the effect that p represents an actual state of affairs.

**Nearest positions.** Self-representation accounts: asserting as representing oneself as believing/knowing — Black, Davidson, Unger, Slote, Green; Pagin's prima facie informative account: surface-feature defaults on speaker and hearer sides — Pagin; Commitment accounts and Searle's constitutive-rule account — Peirce, Alston, Brandom, Searle

**The entry is silent on.** Artificial speakers, chatbots, language models and post-training are not discussed anywhere in the entry. Pretended or make-believe illocution as a category, including Searle's own treatment of fictional speech acts, is also absent. The only theatrical case is the actor example in §4.1 and the passing mention of theatrical performances in §5.2. The entry also says nothing on whether fine-tuning changes the indexing of outputs to a speaker.


### From the Stanford Encyclopedia — fiction

- **SUPPORTED** (1/5) — Searle's pretended-illocution account is not established as a definition of fiction. Pretense is neither necessary nor sufficient, and works at best fragment-level. Kripke and Lewis used pretense without defining fiction by it. — *Currie, and the entry's own assessment. Searle is the target. Kripke and Lewis disclaim the definitional use.*
  > not only is pretense not necessary for something to be (part of) a work of fiction, it is also not sufficient: one can pretend to engage in an illocutionary act for all kinds of reasons other than the fact that one is writing fiction—one might just be engaging in mimicry or verbal irony
- **CONTRADICTED** (3/5) — Walton makes it a requirement on consumers that they make believe the content. The make-believe sits in the audience, and a work is fiction only if it is supposed to be used as a prop. — *Walton 1990*
  > what is crucial to a work of fiction is that this is a requirement on consumers of fiction. (For this reason, day-dreaming out loud does not count as fiction.)
- **ANTICIPATED** (3/5) — The thesis's move of locating the fiction in a represented speaker is close to Currie's 'fictional author', a character constructed in make-believe who tells the story as known fact. Lewis gives a similar treatment of tellers who present as ravers or translators. — *Currie 1990; Lewis 1978 fn. 7; Byrne 1993 (idealism)*
  > that fictional character constructed within our make-believe whom we take to be telling us the story as known fact
- **ADJACENT** (2/5) — Objects that were not produced as fiction can still serve as props and so count as fiction. Critics reject this and say they can only be treated as fiction. — *Walton 1990: 87 for; Currie, Lamarque & Olsen, Davies, Stock against*
  > the fact that cracks in a rock might prompt imaginings just shows that the rock could be treated as a work of fiction, not that it could turn out to be a work of fiction.
- **SUPPORTED** (2/5) — Audiences can engage with a text literally or by default without the fictive attitude making a difference. Readers often fail to scrutinize fiction. Expectations differ by genre. — *Matravers 2014; Prentice & Gerrig 1999 and others; Friend 2012 and forthcoming*
  > The experience of reading de Quincey's "The Revolt of the Tartars" is the same whether we believe it is non-fictional, believe it is fictional, or ... we are ignorant of whether it is non-fictional or fictional.
- **ADJACENT** (2/5) — Dual-model and metarepresentation accounts: a pretend model is quarantined from the reality model. Merely having two models active is insufficient, because dissociated subjects such as Capgras patients and sleepwalkers also have them. Awareness of the pretend/real distinction is what is needed. — *Perner 1991; Nichols & Stich 2003; Leslie 1987; Meini & Voltolini 2010; Lillard*
  > a pretender must be aware of the actual situation and the nonactual, represented one, or else (s)he is mistaken, not pretending.
- **SUPPORTED** (1/5) — Fiction need not be a polished work. A single fictive utterance in a brief conversation with one interlocutor can be a fiction. Fictive utterance may also coexist with assertion in the same text. — *Stock 2017; Currie's 'patchwork'; García-Carpintero 2013 (one utterance under both fiction and assertion norms)*
  > a fiction may be uttered only once, in a brief conversation with a single interlocutor
- **ADJACENT** (2/5) — Intentionalist accounts rest on what the author intends the audience to do, and Friend questions what the content of such intentions could be without circularity. These are the accounts the thesis must answer for outputs with no authorial intention at the moment of production. — *Currie 1990; Lamarque & Olsen 1994; Davies; Stock 2017; Friend 2012*
  > Presumably they can't be understood as intentions to write a certain kind of fiction or non-fiction, on pain of circularity, although it is hard to see how else to construe them.

**Nearest positions.** Make-believe located in consumers, with the work as prop (a prescription, not actual imagining) — Walton 1990; Fiction as the author's pretended illocution, with its defects of insufficiency and fragment-level scope — Searle 1975 (Currie 1990 and Lamarque & Olsen 1994 as the audience-directed fictive-intent variants); Represented or fictional teller and constructed 'fictional author' (Currie 1990; Lewis 1978 fn. 7; Byrne 1993)

**The entry is silent on.** Chatbots, language models, training or post-training, and any empirical question about whether a fictional speaker persists. The entry never treats a text-producing system with no author who pretends or intends at the time of production, or a persona that is 'indexed' to a represented speaker as such. Its only non-authored case is Walton's cracks in a rock. It also has no discussion of users who take the output literally while the output is still fiction-like.

<details><summary>8 searches</summary>

- `Mallory chatbot make-believe users pretend speech acts large language models`
- `Gubelmann large language models speech acts illocutionary assertion`
- `Butlin Viebahn AI assertion chatbots`
- `Shanahan role play with large language models simulacra`
- `Attah LLM assertion speech act illocutionary`
- `language model outputs fictional discourse Searle pretended assertion author character chatbot`
- `persona selection model post-training assistant character base model pretraining simulates characters`
- `Attah chatbots serious illocutions assertion language models philosophy`

</details>

