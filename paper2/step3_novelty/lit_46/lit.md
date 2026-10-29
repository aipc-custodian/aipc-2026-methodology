# Literature check — novelty

This check can show that something HAS been argued. It cannot show that nothing has. Read `not found` as carefully as the findings — a clean result means only that these searches came back empty, and much of the literature is paywalled and invisible to it.


Stanford Encyclopedia entries read in full: [assertion](https://plato.stanford.edu/entries/assertion/), [identity-personal](https://plato.stanford.edu/entries/identity-personal/), [moral-responsibility](https://plato.stanford.edu/entries/moral-responsibility/)
*The theses concern the sanction condition on assertion (Butlin/Viebahn, Skiba, proxy accounts), so the assertion entry is primary; the argument turns on performer/bearer continuity across instances (personal identity) and on answerability or sanctions for acts, which belongs to moral responsibility.*


## The sanction condition on LLM assertion is best explained by a bearer/performer grain gap, not by an agency deficit. Policy-level sanctions are durabl…

*Checked as the post-kill restatement.*

| Relation | Dmg | Source | What they say |
|---|---|---|---|
| **ANTICIPATED** | 3 | ["Dissociative Identity: Language Model Agents Lack Grounding for Reput…](https://arxiv.org/html/2605.30169) | <cite index="31-1">Sanctioning institutions presuppose a subject whose identity persists, whose memory carries consequences forward, whose reputation … |
| **CONTRADICTED** | 3 | [Butlin & Viebahn, "AI Assertion", Ergo 12, 2025](https://journals.publishing.umich.edu/ergo/article/id/7960/print/) | <cite index="54-7,54-8">They require (i) that interlocutors track credibility, (ii) that asserters are sensitive to this, and (iii) that losing credib… |
| **CONTRADICTED** | 3 | [Williams & Bayne, "Chatting with Bots: AI, Speech Acts, and the Edge o…](https://arxiv.org/pdf/2410.16645) | They argue that <cite index="58-8,58-10">in typical proxy assertion there is a clear principal to trace the act to, but in typical LLM chatbot interac… |
| **ADJACENT** | 2 | [Skiba, "Artificial Speech Acts", Analysis (forthcoming)](https://philpapers.org/rec/SKIASA-2) | <cite index="11-4">Skiba shows how a norm-based argument against LLM assertion can be generalized to a negative answer on speech acts generally.</cite… |
| **ADJACENT** | 2 | ["Who asserts when no one asserts? Functionalism, proxy responsibility,…](https://link.springer.com/article/10.1007/s11229-026-05807-3) | <cite index="51-11,51-12">The paper says proto-assertion must either attribute proto-interests to LLMs or explain sanctionability without anything tha… |
| **ADJACENT** | 2 | ["Assertion, Accountability, and Large Language Models", Philosophy & T…](https://link.springer.com/article/10.1007/s13347-026-01136-y) | <cite index="14-3">The paper advances 'assertion without asserter' as a tool for cases where grounding in an individual speaker fails but assertoric f… |
| **ADJACENT** | 2 | ["Talking with Language Models", arXiv 2610.09064, 2026](https://arxiv.org/html/2610.09064v1) | They argue that <cite index="68-9">even if a virtual instance persists across a session, persistence of a computational object is not agency in a cont… |
| **ADJACENT** | 2 | [de Jong, "The Retribution-Gap and Responsibility-Loci Related to Robot…](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7089880/) | de Jong notes that <cite index="45-7,45-8">automated systems cannot respond to punishment and blame as humans do, which gives rise to retribution gaps… |
| **SUPPORTED** | 1 | [Chalmers, "What We Talk to When We Talk to Language Models" (Selfridge…](https://arxiv.org/pdf/2604.17031) | Chalmers holds that <cite index="71-6">the LLM quasi-agents we interact with are best understood as virtual entities bound to conversation-based memor… |
| **SUPPORTED** | 1 | ["Tempting the Agent: The Economics of Reputation without Persistent Id…](https://arxiv.org/pdf/2609.02992) | The economics paper says <cite index="32-10,32-12">the situation changes when the actor behind a service is not persistently identifiable or economica… |
| **SUPPORTED** | 1 | [Löhr, "LLMs and the Logical Space of Reasons", Minds and Machines, 202…](https://link.springer.com/article/10.1007/s11023-025-09751-y) | Löhr agrees that <cite index="3-9,3-10">being subject to a norm includes being sanctionable for violating it, and that sanctions require the agent to … |

**What is left.** Granting that sanctionability is necessary for assertion, and granting Butlin and Viebahn's (i) credibility-tracking and (ii) sensitivity elements, the part of the failure attributable to the sanction landing on the wrong individual (training-time policy versus session-level instance versus persona) is a deployment-relative identity gap. It can be remedied in principle by architectures with persistent, non-forkable, act-indexed identity. It is separable from, and does not by itself discharge, B&V's element (iii), which requires that the costs be bad for the bearer. The thesis contributes a three-way bearer/performer split applied to assertion, and the prediction that persistent-memory agents with reputational stakes would clear the identity part of the condition. It has to say separately what makes those costs bad for the bearer. The persistence-and-reputation diagnosis itself is already published for LLM agents generally (the 'dissociative identity' paper) and for AI agent markets (the economics paper). The claim that proxy accounts are wrong about why current models fail has no textual basis found yet and runs against Williams and Bayne's no-clear-principal objection.

**Not found.** I found no paper that applies a bearer/performer (or sanction-bearer/act-performer) distinction to the sanction condition on assertion. I found none that separates policy, instance and persona as candidate sanction-bearers in the assertion debate. I found none that argues persistent-memory agents with reputational stakes would satisfy B&V's sanction condition. That silence is weak evidence: the Ergo, Synthese and Philosophy & Technology papers were visible only as snippets, and much of this literature is paywalled. I could not read Skiba's argument beyond the abstract, so whether it rests on sanction is unverified. I did not read Nickel (2013) or Green & Michel (2022), the proxy sources, directly. The 'Dissociative Identity' paper was seen only in snippets, so I do not know whether it addresses assertion or speech acts. The empirical side was thin. I found one economics preprint on reputation without persistent identity, game-theoretic reputation work cited second-hand through the dissociative-identity paper, and the Lima et al. 'punishment gap' papers seen only as reference-list entries. I did not read the psychology of punishing machines or the experimental human-AI reputation literature itself, and I found no linguistics or sociology work on assertion norms and sanctions. A fuller empirical pass is needed. Three of the four required search types were run (central claim, adjacent empirical, named targets). The fourth, a recent survey or reference-work entry, was only partly covered, via the Synthese 2026 piece and Williams and Bayne. I found no Stanford Encyclopedia or similar survey on LLM assertion, and I ran out of searches before trying one.


### From the Stanford Encyclopedia — assertion

- **SUPPORTED** (1/5) — Commitment-as-accountability: asserting makes the speaker liable to sanctions/blame if the content is false. This is the sanction condition the thesis builds on. — *Peirce; Alston (2000)*
  > an act of assertion […] renders [the speaker] liable to the penalties of the social law (or, at any rate, those of the moral law) in case [the asserted proposition] should not be true, unless he has a definite and sufficient excuse.
- **SUPPORTED** (1/5) — Alston's liability formulation is stated in terms of what the speaker knowingly takes on, which presupposes a bearer who is also the performer. — *Alston (2000: 55)*
  > knowingly [takes] on the liability to ([lay] herself open to) blame (censure, reproach, being taken to task, being called to account), in case of not-p.
- **SUPPORTED** (1/5) — Commitment as ongoing responsibility to defend the claim or retract it. This is a durable, act-indexed burden that needs a persisting subject. — *Brandom (1994); MacFarlane (2003)*
  > One can escape this commitment only by withdrawing the assertion.
- **ADJACENT** (2/5) — The sanction/liability component is only one of several components in mixed accounts and is not sufficient on its own. This fits the thesis's 'necessary condition only'. — *Green (fidelity, liability, frankness); Searle; Pagin (2004)*
  > incurring a commitment is not sufficient for asserting.
- **ADJACENT** (2/5) — Rescorla holds that no norm governs the making of assertions, only norms on later reactions such as defending or retracting. This bears on whether sanctions are conditions on asserting or on aftermath. — *Rescorla (2009a)*
  > there is no norm at all for proper making of assertions. There are only norms that govern later reactions.
- **ADJACENT** (2/5) — Non-normative or descriptive accounts of assertion (self-representation of belief or knowledge, cognitive safeguards) can explain the same data without sanctions. Jary's 'social safeguards' are sanctions against misleading assertions but are only one part of the account. — *Pagin 2016b; D. Black; Jary (2010)*
  > Social safeguards consist in sanctions against misleading assertions
- **ADJACENT** (1/5) — Austin's uptake and the distinction between performer and addressee. The entry notes that speaker-content verbs like 'assert' do not need a hearer. — *Austin; entry's own discussion*
  > it is less plausible when the structure is speaker-content (“Bill asserted that p”).

**Nearest positions.** Commitment as accountability (liability to sanction/blame) — Peirce, Alston; Commitment as responsibility to defend or retract — Brandom, MacFarlane, Green (fidelity); Commitment/sanction is not sufficient for assertion; assertion not fully reducible to social effects — Pagin 2004, Marsili & Green 2021; Rescorla's view that norms govern only later reactions

**The entry is silent on.** Artificial or LLM speakers, and anything about sanctions falling on a non-performer (policy or developer level) versus the performer, or the durability, forking, or persistent identity of the bearer. The entry assumes without comment that the asserter and the sanctioned party are the same agent. The bearer/performer grain distinction and the agency-deficit alternative are not discussed anywhere.


### From the Stanford Encyclopedia — identity-personal

- **SUPPORTED** (2/5) — The non-branching view makes 'cannot be forked away' a persistence condition. Survival requires that no other being be continuous with you, so fission ends the original. — *Shoemaker 1984, Parfit 1984/2012, Unger 1990*
  > a past or future being is you only if she is then psychologically continuous with you and no other being then is... Fission is death.
- **ADJACENT** (3/5) — Multiple-occupancy view: before fission there were already two coinciding persons, so 'who bears' depends on the grain of individuation. This resembles a bearer/performer grain gap. — *Lewis 1976, Perry 1972, Noonan 2019b*
  > What we think of as you is really two people, who are now exactly similar and located in the same place, doing the same things and thinking the same thoughts.
- **ADJACENT** (3/5) — Temporal-parts ontology yields many candidate bearers at different grains, with indeterminate reference for 'I' and indeterminate persistence conditions. — *Sider 2001b, Hudson 2001, Lewis 1976, Hirsch 1982*
  > it would be indeterminate what things, and even what sort of things, we are. And insofar as the candidates have different histories and different persistence conditions, it would be indeterminate when we came into being
- **CONTRADICTED** (3/5) — Identity is not what matters practically. Responsibility and concern can attach to someone other than the numerically identical individual, so sanction-bearing need not track identity-persistence. — *Parfit 1971, 1984, 1995; Martin 1998 (opposed by Sosa 1990, Merricks 2022)*
  > Likewise, someone else could be responsible for my actions, and not for his own. Identity itself has no practical importance.
- **SUPPORTED** (1/5) — Persistence conditions may differ by kind of being and cannot be settled a priori, so a language agent may have its own persistence conditions. — *Olson (framing the persistence question)*
  > if there could be immaterial people—gods or angels, say—what it would take for them to persist might differ from what it takes for a human person to persist.
- **ADJACENT** (2/5) — Copying or duplication cases show that persistence and 'which one is you' come apart. These include brain-state transfer, 'copy... from one computer drive to another', and the duplicating machine. — *Shoemaker 1984 (yes to brain-state transfer), Unger 1990 (no), van Inwagen 1997*
  > Could you literally move from one organism to another by 'brain-state transfer'? Psychological-continuity theorists disagree.
- **ADJACENT** (2/5) — Evidence versus constitution: what tracks persistence is not thereby what persistence consists in. Anticriterialism holds that continuity is mere evidence. — *Olson (evidence/persistence distinction); Merricks 1998, Swinburne, Lowe*
  > having your fingerprints is not what it is for a past or future being to be you: it's neither necessary... nor sufficient
- **ADJACENT** (2/5) — The population question: what fixes how many subjects occupy one organism or system, for example split brains or multiple personality, which may count as 'two on one organism'. — *Nagel 1971, Wilkes 1988, Rovane 1998, Olson 2003*
  > a human being with multiple personality could literally be the home of two or more thinking beings

**Nearest positions.** Non-branching psychological-continuity view (fission is death, so a forkable agent lacks identity) — Parfit, Shoemaker, Unger; Multiple-occupancy / temporal-parts view (many coinciding candidates, so the bearer is grain-relative) — Lewis, Perry, Sider; Identity-is-not-what-matters (responsibility follows psychological connectedness, not identity) — Parfit, Martin, against Sosa and Merricks

**The entry is silent on.** Assertion, sanctions, norms of assertion, LLMs or language agents, and agency deficits are never discussed. The entry mentions a computer or robot being a person only in passing. It has nothing on sanctions or costs as a condition on speech acts, on policy-level versus instance-level bearers, or on whether a condition is only necessary. Responsibility appears only briefly under 'what matters in survival'.


### From the Stanford Encyclopedia — moral-responsibility

- **SUPPORTED** (1/5) — Blame is tied to liability to sanction, and sanctions raise a fairness requirement that the sanctioned party be the right party. This gives the thesis a reason why sanctions must fall on the performer. — *Wallace 1994; Watson [1987]2004; Rosen 2015; Fritz and Miller 2018 (as reported by the entry)*
  > blameworthiness, unlike praiseworthiness, is often taken to involve liability to sanction
- **ANTICIPATED** (3/5) — Forward-looking, policy-style sanctions do not target the individual wrongdoer and reach anyone who can be influenced. This is close to the thesis's 'policy-level sanctions fall on a non-performer' point. — *Wallace's criticism of Smart's forward-looking account*
  > is not directed exclusively toward the individual agent who has done something morally wrong, but takes account of anyone else who is susceptible to being influenced by our responses
- **ADJACENT** (3/5) — Exempt agents are treated as objects of policy to be managed, handled or trained, not as targets of sanction-bearing responsibility practices. A referee would say the thesis's 'agency deficit' explanation is just this exemption view. — *P. F. Strawson [1962]1993; Watson [1987]2004; McKenna 2012; Wallace 1994*
  > an object of social policy,” something “to be managed or handled or cured or trained
- **CONTRADICTED** (2/5) — The standard explanation of why sanction and blame are inapt is a deficit in moral competence or reasons-responsiveness, not a structural mismatch. The thesis denies that an agency deficit is the best explanation. — *Wolf 1987; Fischer and Ravizza 1998; Wallace 1994; McKenna 2012*
  > Possession of moral competence—the ability to recognize and respond to moral considerations—is often taken to be a condition on moral responsibility.
- **SUPPORTED** (1/5) — Responsibility can be carried across time, from earlier acts to later outcomes, by tracing and derivative responsibility. The entry also notes personal-identity issues in manipulation cases. Both are resources for the thesis's claim that identity must persist through act-indexed costs. — *Sartorio 2016; Fischer and Ravizza 1998; Khoury 2013; Matheson 2014; Shoemaker 2012*
  > their failure to fulfill certain conditions on responsibility is traceable to earlier actions undertaken by the agent
- **ADJACENT** (2/5) — Whether the right bearer exists when many contributors act collectively. Individual contribution versus group-level intention matters for who is accountable. — *Kutz 2000; Lawson 2013; Petersson 2013*
  > we should refer not to individual causal contributions but rather to the pilots’ overlapping intentions and attitudes
- **ADJACENT** (2/5) — Responsibility practices are justified by forward-looking benefits, and some skeptics keep non-desert sanctions. This bears on whether durable policy-level sanctions suffice. — *Schlick; Smart 1961; Vargas 2013; Pereboom 2014; Caruso and Pereboom 2022*
  > non-desert invoking moral desiderata” such as “protection of potential victims, reconciliation to relationships both personal and with the moral community more generally, and moral formation

**Nearest positions.** Forward-looking/instrumental accounts, where sanctions aim at influencing future behavior and may fall on others — Schlick, J. J. C. Smart, Arneson; criticized by Wallace 1994; Strawsonian reactive-attitudes and conversational accounts, where non-sanctionability follows from exemption or moral-competence deficits — Strawson, Watson, Wallace, McKenna; Fairness-based accounts of who may be sanctioned, tied to blameworthiness — Wallace, Rosen, Fritz and Miller, Watson

**The entry is silent on.** Assertion and norms of assertion; any 'sanction condition' on assertion; LLMs or other artificial agents; copying, forking and shedding of agents; and a distinction between sanction-bearer and act-performer at different grains (policy versus instance). The entry's only nearby material is the general fairness-to-the-sanctioned-party point and the Wallace objection to forward-looking accounts.

<details><summary>8 searches</summary>

- `Butlin Viebahn AI assertion LLM sanction condition`
- `Skiba large language models assertion norm-based argument`
- `LLM assertion proxy account speaker deployer developer`
- `accountability AI agents persistent identity reputation sanctions forking`
- `reputation and sanctions chatbots trust psychology accountability machine punishment responsibility gap`
- `Butlin Viebahn "AI Assertion" sanctions fine-tuning "bad for the system" interests persistence across conversations instance`
- `Williams Bayne chatbot speech acts proxy assertion who is the speaker LLM`
- `Chalmers what we talk to when we talk to language models quasi-subject thread instance model identity`

</details>

