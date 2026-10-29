# Rulings

The paper is careful and candid, and its same-string/different-policy device and its calibration-corrected warrant criterion are sound. But the step from 'the policy fixes the verdict' to 'the policy is the primary bearer' (§2.1), the unscaled force term in the warrant criterion, the claim that the lineage is the only system-level locus of sanction, and the direction of the spread/insincerity link in §4 all need answers. The novelty claims are largely fair, since most of the cited omissions are rivals or uncredited precedents, and no referee identified prior work that meets the standard for anticipation.

4 must address, 15 optional, 1 mistaken.

## MUST ADDRESS

**Concern** (chatgpt (#1), gemini (#1), referee_claude-fable-5-1 (#1)): The same-string/different-policy test shows only that policy facts ground the verdict. The 'no gap between act and state' argument (§2.1) is meant to move from grounding to the claim that the policy is the primary bearer, and it does not do so. A distribution and a draw are still distinct. The paper's own decoding point (one credal profile, different decoding rules) reintroduces a state/disposition gap. A standing disposition to overassert makes the person, not the act, the primary bearer, which holds for humans too. Deterministic humans would be a counterexample.

**Reason:** The paper itself says the test does not establish the bearer part, so the no-gap argument is the only bridge to the title thesis. The three reports find the same weak points in it: the distribution/draw distinction, the disposition-bearer analogy with humans, and the decoding point. Without an answer the central claim is only grounding.

## MUST ADDRESS

**Concern** (chatgpt (#2, third point), gemini (#4)): The warrant criterion (f ≤ c*) never says what numerical force f a flat or bare assertion has. If a flat assertion has force 1, then P₁ (c* = 0.95) is unwarranted. If it has some threshold, the threshold is unspecified.

**Reason:** The verdicts in Cases 1–2 (P₁ warranted, P₂ not) depend on a scale for f that the paper never gives. The criterion is the paper's main technical proposal, so this is an undefended premise the argument needs.

## MUST ADDRESS

**Concern** (chatgpt (#4), gemini (#5)): The claim that the policy lineage is the only system-level candidate for the sanction component is unsupported. Persistent memory, retrieval, deployer-updated instructions or a (weights + memory) composite can durably change behaviour after criticism without a weight update. Threads or sociotechnical systems are also rivals. The paper excludes these in one sentence by defining them as 'context, not policy'. The assertion that credibility assessments durably reach chatbot assertions only through the weights is overstated.

**Reason:** The abstract and §3.3 rest on the lineage being the only system-level candidate. A frozen-weights-plus-updatable-memory system is an obvious alternative locus of durable corrective responsiveness. The paper's dismissal of it depends on a definitional choice of what counts as the policy.

## MUST ADDRESS

**Concern** (chatgpt (#5), referee_claude-fable-5-1 (#5)): §4's categorical conclusion, that resampling disagreement counts as no evidence of insincerity, does not follow from P(E)=1−Σrᵢᵏ. Disagreement can be indirect evidence for insincerity if insincere policies are more spread out; a toy case gives a likelihood ratio of about 2.8. The claim that insincerity predicts less spread needs a stated model of insincere policies, and the paper admits it depends on priors. Much of the result also comes from the definition of insincerity as selective decoupling.

**Reason:** The paper says the strength of any link depends on priors over kinds of insincere policy, and it makes no claim about them. It nonetheless asserts that disagreement does not count toward insincerity, and it says insincerity 'if anything' predicts less spread. The direction of that link is the premise the conclusion needs, and it is asserted without a model. The claim that the paper merely replies to the thin Moorean test rather than arguing for its definition is overstated, since §4.3 does argue the point.

## OPTIONAL

**Concern** (chatgpt (#2, first point), gemini (#2), referee_claude-fable-5-1 (#2, #6)): The credal profile q(p|x) is under-specified. Pooled token probabilities may measure how likely the model is to express p, not an epistemic attitude. It is also unclear how q relates to the post-RLHF weights and to π, which come from the same weights. Keeling & Street's scepticism about credence attribution to LLMs is relevant.

**Reason:** §5.2 and §4.5 already treat the credal reading as open and say an independent measure of the policy's attitude is unavailable. A reliabilist c* indexed by a confidence score does not strictly need q to be a credence. Sycophancy in §2.3 is defined as covariation, not as a q/π mismatch, so the sycophancy verdicts do not rest on q.

**Checked:** Searched Keeling & Street. Found Inquiry 69(6): 2918–2944. The abstract says LLM credence attributions face non-trivial sceptical concerns and that the existence of LLM credences is plausible but inconclusive. It is relevant background and does not anticipate or refute the paper.

## OPTIONAL

**Concern** (chatgpt (#2, second point), referee_claude-fable-5-1 (#3)): c* depends on a reference class, so it is not simply a property of the weights. Verdicts in Cases 1–2 flip with the choice of class (e.g. 'all 0.95-claims about V' versus the whole domain). The generality problem therefore decides the paper's own cases, so it is more than a 'familiar cost'.

**Reason:** The paper says c* is relative to a reference class, takes it to be domain and question type, and states 'in this domain' in Case 2. The cases fix the class by stipulation. The verdict-sensitivity is real, but the paper's position is stated and consistent. The line calling c* 'a property of the weights' is loose.

## OPTIONAL

**Concern** (chatgpt (#3)): On R3 the Case 1–2 hallucination verdicts reverse. The same-string test then no longer yields hallucination verdicts, and what survives is only that the policy fixes the confidence clause. The paper should separate what survives R3 on substance from what survives because policy confidence was built into the reading. R3 is also a contested pragmatic claim about what utterances communicate.

**Reason:** The paper concedes the reversal openly and argues that whether R3 holds is itself a fact about the policy. That reply is a contestable but real answer. The abstract flags the reading as open, so the paper stands.

## OPTIONAL

**Concern** (referee_claude-fable-5-1 (#6)): R3 should be set aside altogether. It is a hypothesis about what the model represents, not a reading of what the output says, because the confidence clause is fixed by a property of the weights that the hearer cannot access.

**Reason:** This is a contestable view about assertoric content that the paper's working antecedent leaves open. Keeping R3 as an open reading is a choice, not an error.

## OPTIONAL

**Concern** (gemini (#6)): Under R3 a sycophantic P₆ would assert 'the answer is 23, with calibrated confidence ≈0.5'. The epistemic import is diluted, and §5.3's claim that the sycophancy verdict survives needs a clarification.

**Reason:** The reporter calls it minor. The paper's point is that content tracking the user's view with the evidence fixed is an audience-independence failure whatever the confidence clause says. Dilution of the epistemic import does not remove that failure.

## OPTIONAL

**Concern** (referee_claude-fable-5-1 (#4)): The sanction conditional is either false or nearly empty. Gómez locates accountability in human and institutional structures, which seems to refute the universal claim. If instead 'if at all' carries the weight, the claim after the §3.3 withdrawal reduces to a near-triviality. The lineage definition also excludes routine from-scratch retrains.

**Reason:** The paper discusses Gómez directly. It treats his view as assertion without an asserter, so it is not clearly a theory on which the chatbot asserts. The conditional's modest strength is stated openly by the paper. The retrain gap is a boundary issue the paper flags as vague.

**Checked:** Searched Gómez (2026), Phil & Tech 39:123. The abstract snippet says accountability and responsiveness attach to human and institutional structures, not the machine, with assertoric function present without authority. This matches how the paper represents it.

## OPTIONAL

**Concern** (chatgpt (#6)): The sycophancy test is incomplete. Differential responsiveness to a user's stated view is not yet sycophancy, because a user's testimony can be evidence and some accommodation is legitimate. An independent criterion of epistemically inappropriate accommodation is needed. Li et al. (2026) offer a three-condition account that the paper omits.

**Reason:** Case 3 stipulates that the evidence is fixed and defines the verdict as covariation with the user's attitude while the evidence stays fixed. The point has some force because the user's statement is itself testimony. But the paper stands as a conditional analysis.

**Checked:** Searched Li et al. 2026. Found arXiv 2605.05403, a position paper that defines sycophancy as a boundary failure between social alignment and epistemic integrity, with three conditions: a user cue, a shift toward it, and compromised epistemic integrity. It is a related definition of sycophancy, not an anticipation of the bearer thesis (abstract and body snippets).

## OPTIONAL

**Concern** (chatgpt (#7), referee_claude-fable-5-1 (#8, first bullet)): Redefining hallucination as unwarranted confident assertion yields odd classifications: a lucky true guess is a hallucination and a false but warranted report is not. The paper concedes 'overassertion' would do equally well. It should defend the terminology or retitle.

**Reason:** The paper states and motivates the stipulation and says the substance is the distinction itself. This is a matter of terminology and emphasis.

## OPTIONAL

**Concern** (chatgpt (prior work)): Wu (2026) is a rival account on which assertability is a relational status of an output-in-practice, with regulation distributed across models, retrieval systems, interfaces and institutions. This challenges the move from policy properties to policy as the bearer.

**Reason:** It is a rival to answer, not an anticipation. I did not see it assert the policy-bearer thesis or conclusively close it off. Omitting it is a scholarship gap, not damage to the argument.

**Checked:** Searched the title. Found Qian Wu, Ethics and Information Technology, article 46, 25 Sept 2026. I saw the ABSTRACT only, via a citing page. It develops assertability as a relational status of an output-in-practice and organises regulation across four loci (assertoric force, evidential grounding, evidential candor, response selection). The abstract does not say the paper rejects a single machine-level warrant state, as the report says. I could not confirm that part.

## OPTIONAL

**Concern** (chatgpt (prior work)): Related work is omitted that 'anticipates aspects' of the thesis: Arora (2024) on proxy assertions, Band et al. (2024) on linguistic calibration, Orgad et al. (2025) on internal/external discrepancy, Zhang et al. (2023, SAC³) on question-level and model-level hallucination, and Ravichandran (2026) on norms of assertion applied to hallucination and sycophancy.

**Reason:** None of these discusses the claim that the policy is the primary bearer of assertion defects as a sustained line of argument that it endorses. Each is at most a framework neighbour or a passing overlap. They are uncredited precedents, not anticipations.

**Checked:** All five exist. Arora (Phil & Tech 37:15, 2024) defends proxy assertions with responsibility lying with designers, which is the deployer view the paper opposes. Band et al. (ICML 2024) define linguistic calibration by whether users can make calibrated predictions. Orgad et al. (ICLR 2025) report that models can encode a correct answer yet generate an incorrect one. SAC³ (EMNLP Findings 2023) distinguishes question-level and model-level hallucination and shows self-consistency alone is insufficient. Ravichandran is a Harvard thesis whose abstract argues that LLM outputs function as assertions, defines an 'Epistemic Governance Norm of Assertion', and says training decouples epistemic registration from assertoric output, producing hallucination and sycophancy. I saw abstracts or snippets only. None discusses the policy-bearer claim.

## OPTIONAL

**Concern** (referee_claude-fable-5-1 (#2)): The calibration-corrected criterion is anticipated by calibrationist reliabilism about justified credence (Dunn 2015; Tang 2016; Pettigrew 2021; Goldman). The paper cites only Goldman 1979 and should state that its new move is applying the standard to assertoric force.

**Reason:** Dunn-style calibration accounts apply to credence-forming processes, not to assertoric force or chatbot policies. At most the paper is an application of a broader framework that those works do not draw. The paper already says its reliabilism is 'in the spirit of Goldman' and calls the generality problem a cost, so the omission does not mislead about what is new.

**Checked:** Searched for Dunn's calibration approach. SEP and a Springer/Episteme footnote (SECONDHAND) say Dunn defends a calibration account of reliable credence-forming processes, and note he says little about which counterfactual circumstances matter. I did not see Dunn's full text. The accounts concern credence justification, not assertion.

## OPTIONAL

**Concern** (referee_claude-fable-5-1 (#2, #8), gemini (prior-work section)): Other uncited works bear on the paper's claims: Evans et al. (2021) 'Truthful AI', Ward et al. (2023) on deception in structural causal games, Massaguer Gómez & Gaitán Torres (2026), 'Epistemic Integrity in LLMs' (arXiv 2411.06528), Hila (2025), Freiman, Ye et al. (2026), and Brandom-style scorekeeping.

**Reason:** These are suggested citations or distinctions. None is shown to discuss and endorse the bearer, warrant or sanction-lineage claims at length. They are uncredited precedents and do not affect the validity of the argument.

**Checked:** Evans et al. exists (arXiv 2110.06674). Its abstract proposes a negligent-falsehood standard and institutions to evaluate AI systems before and after deployment, and a honesty/truthfulness distinction. Ward et al. (NeurIPS 2023) exists and defines deception in structural causal games. Massaguer Gómez & Gaitán Torres, Synthese 208:162 (2026), exists, on functionalism and proxy responsibility. I saw its title and authors only and could not confirm the report's quoted content. I did not verify arXiv 2411.06528, Hila (2025), Freiman, Ye et al. (2026) or the encyclopedia entry gemini mentions.

## OPTIONAL

**Concern** (chatgpt (#2, closing paragraph)): The warrant criterion should engage the possibility that warrant is contextually evidential rather than reducible to calibration, including discursive-responsibility traditions such as Brandom.

**Reason:** §2.4 considers the internalist and provenance-sensitive alternative and chooses the behavioural-reliabilist account with its costs stated. Engaging Brandom-style accounts would be fuller, but their absence does not damage the argument.

## OPTIONAL

**Concern** (referee_claude-fable-5-1 (#8)): The claim that greedy policies 'merely match force to mass' assumes the mode of π is a flat guess. For a model trained to hedge, the mode may be a hedge, and greedy decoding could reduce overassertion.

**Reason:** The paper's greedy case (P₄) is conditional on a policy that emits a low-c* flat claim. The general line about greedy policies could be qualified, but the point is minor and does not touch the argument.

## OPTIONAL

**Concern** (gemini (#3), referee_claude-fable-5-1 (#7, #8)): The text contains revision-memo artifacts ('the earlier draft', 'the referees' point', 'I withdraw that reply', 'that claim was false') in §§3.1–3.4, 4.1 and 5.3. These belong in a response letter. Page references to Chalmers and Williams & Bayne should also use the published pagination.

**Reason:** The artifacts are present in the text, so the observation is accurate. It is a matter of presentation and does not affect the soundness of any argument.

## MISTAKEN

**Concern** (chatgpt (novelty assessment)): The paper's constituent ideas (process-relative warrant, distributional calibration, policy-dependent sycophancy, consistency-based detection, training incentives) are extensively anticipated. The paper should present only the inference to primary bearership as new.

**Reason:** §1 already credits Goldman, Kalai et al., Kadavath et al., Sharma et al. and Manakul et al. for these ideas. It says outright that applying the process-relative test to policies is not new in epistemology. Its novelty list claims the bearer argument, the lineage claim, the resampling argument and the content-reading analysis. The report itself found no prior work that combines them.

**Checked:** Compared the report's novelty claim with the text of §1, which already makes these credits. Separately checked the listed prior works above.

