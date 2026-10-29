#!/usr/bin/env python3
"""
thesis_forge.py — the front end.

Generates candidate philosophical theses, then tries hard to kill them.
What survives goes to you for the first human gate.

    Stage 1  GENERATE   N isolated samples, high temperature, blind to
                        each other. No conversation here — dialogue at
                        this stage collapses variance, and variance is
                        the only thing this stage produces.
    Stage 2  CLUSTER    merge near-duplicates.
    Stage 3  KILL       Killer vs. Defender, then an Adjudicator rules.
                        THIS is where the two-Claude conversation lives:
                        pressure on a fixed object.
    Stage 4  REPORT     ranked survivors + kill transcripts, as markdown.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    pip install anthropic

    python thesis_forge.py --area "the metaphysics of friendship" --dry-run
    python thesis_forge.py --area "the metaphysics of friendship" \
        --generators 6 --per-generator 4 --out run1

Optional literature file (JSON list of objects with any of
title / author / year / abstract). Used ONLY for the "already taken?"
kill criterion, not for topic selection:

    python thesis_forge.py --area "..." --literature lit.json
"""

import argparse, html, json, os, random, re, sys, textwrap, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from anthropic import Anthropic
from runlog import RunLog

MODEL = "claude-sonnet-4-5"

# ---------------------------------------------------------------------------
# Prompts. These are the actual intellectual content of the pipeline —
# edit them more readily than you edit the code.
# ---------------------------------------------------------------------------

GENERATOR_SYSTEM = """\
You are a philosopher generating candidate theses for a journal article.

You are NOT writing a survey and NOT summarizing a debate. You are looking
for a MOVE — something a competent philosopher in this area has not already
made. A move is one of:

  - a distinction nobody in the debate has drawn, which reclassifies the
    positions
  - a counterexample to a premise that both sides currently grant
  - a reframing on which the dispute turns out to be verbal, or turns out
    to be about something other than what the participants think
  - an argument that a position everyone treats as a stable option is
    actually unstable — it collapses into a neighbour
  - an unnoticed commitment: showing that holding X commits you to Y,
    which proponents of X reject

Avoid: taking the unoccupied position on an existing map merely because it
is unoccupied; splitting an existing distinction more finely for its own
sake; "a pluralist/contextualist account of X"; anything whose thesis could
be predicted from the topic alone.

Be willing to propose theses you suspect are false but interesting. Do not
hedge. State each thesis as a claim someone could be wrong about.
"""

GENERATOR_USER = """\
Area: {area}

{literature}

{assignment}Produce {n} candidate theses. Return ONLY a JSON array, no prose around it.
Each element:

{{
  "thesis": "one sentence, a claim that could be false",
  "move_type": "distinction | counterexample | reframing | instability | commitment",
  "sketch": "one paragraph: how the argument would actually go, including \
the key premise the argument turns on",
  "target": "whose view or which shared assumption this is aimed at",
  "risk": "the most likely reason this fails"
}}
"""

# Rotation. Isolated generators given the SAME prompt converge: on a first
# test with a newer model, two blind generators returned the same three
# theses, pairwise. Temperature does not fix that and newer models do not
# let it be raised. So the variance is put into the QUESTION instead of the
# dice — the same design the Killer already uses: constrain by assignment
# and rotation, not by instruction.
MOVES = [
    ("distinction", "a distinction nobody in the debate has drawn, which "
                    "reclassifies the positions"),
    ("counterexample", "a counterexample to a premise that both sides "
                       "currently grant"),
    ("reframing", "a reframing on which the dispute turns out to be verbal, "
                  "or to be about something other than what the participants "
                  "think"),
    ("instability", "an argument that a position everyone treats as a stable "
                    "option is actually unstable and collapses into a "
                    "neighbour"),
    ("commitment", "an unnoticed commitment: holding X commits you to Y, "
                   "which proponents of X reject"),
]

ASSIGN_MOVE = """\
YOUR ASSIGNMENT. Many generators are working on this area in parallel, each
with a different assignment, so that between them the space is covered.
Yours:

  Every thesis you produce must be of this kind of move:
  {move} — {gloss}

"""

ASSIGN_TARGET = """\
  And your starting point is this work:
  {work}
  Look for the move by pressing on what THIS work claims or assumes. The
  thesis need not be only about it, but it must come from engaging it.

"""

ASSIGN_TAIL = """\
The first thesis that occurs to you under this assignment will occur to
everyone given it. Think past it before you answer.

"""

CLUSTER_SYSTEM = """\
You are removing REDUNDANCY, not organising by topic. Err heavily toward
keeping theses separate: a wrongly split pair costs one extra slot, while a
wrongly merged pair destroys an argument that will never be seen again.

Two theses are duplicates ONLY if arguing for one just IS arguing for the
other — same claim, same target, same key premise, differing in wording.

They are NOT duplicates when any of these differ:
  - what is being claimed, even slightly in scope or strength
  - whose view is targeted
  - the premise the argument turns on
  - the kind of move (a distinction is not a counterexample)

Sharing a topic, a vocabulary, or an opponent does NOT make two theses
duplicates. Neither does reaching a similar-sounding conclusion by a
different route — those are the most valuable pairs in the batch and
merging them is the worst thing you can do here.

Expect most batches to contain FEW true duplicates. If you find yourself
merging more than a fifth of a batch, you are grouping by subject matter
and should stop. When in doubt, do not merge.

For every group of two or more you must state the single claim both members
assert. If you cannot write that sentence, they are not duplicates.
"""

CRITERIA = [
    ("ALREADY TAKEN", "this is a known position — name it and who holds it"),
    ("PROVES TOO MUCH", "the argument, if it worked, would license an "
                        "obviously unacceptable conclusion"),
    ("COUNTEREXAMPLE", "a concrete case on which the thesis gives the wrong "
                       "result"),
    ("TRIVIAL", "true but uncontested, or a verbal stipulation dressed as a "
                "discovery"),
    ("EQUIVOCATION", "the thesis is plausible on one reading of a key term "
                     "and interesting on another, and the argument needs both"),
    ("UNFALSIFIABLE", "the thesis is protected from every case by "
                      "redefinition — any apparent counterexample gets ruled "
                      "not to be an instance. Immunity from cases is a "
                      "DEFECT, not a strength"),
]

KILLER_SYSTEM = """\
You are trying to kill a candidate thesis. Not a reviewer offering
suggestions — you are trying to establish it is not worth a paper.

You have been ASSIGNED one line of attack:

    {criterion} — {gloss}

Use that line and no other; do not substitute a different objection.

You must ATTEMPT the attack before you may decline it. Answer in this form:

  ATTEMPT. The best version of this attack, naming ONE premise as the weak
  point, in under 200 words. Make it even if you doubt it works.

  STRENGTH: n/5 — how much damage your own attempt actually does.
    5 the thesis cannot survive this   4 serious, needs a real answer
    3 a genuine problem, answerable    2 weak    1 no force at all

Only if your own attempt scores 1 may you add the line "NOT APPLICABLE".

Declining is expensive: an unattacked thesis is recorded as UNTESTED, not
as surviving, so opting out tells us nothing about it. Note also that
several of these lines of attack apply to structural, conceptual and
metaphysical claims, not only to empirical ones — "this is a conceptual
claim, so cases cannot touch it" is usually a reason to reach for
UNFALSIFIABLE, not a reason to decline.

{equivocation_warning}
"""

# Not part of the rotation. Every thesis faces this one, because the failure
# it catches — a thesis aimed at a view nobody holds — is invisible to the
# other five and fatal when it happens.
MISATTRIBUTION = (
    "MISATTRIBUTION",
    "the thesis ascribes to its named target a view that target does not "
    "actually hold, so the argument is aimed at nobody")

MISATTRIBUTION_WARNING = """\
Check the "target" field against what those philosophers actually hold. The
question is not whether the thesis is true but whether anyone holds the
position it attacks. Watch particularly for a view stated more strongly than
its holder states it — a claim someone makes about ONE class of cases
reported as a claim about all of them, a qualified thesis reported flat. That is the usual shape of this error.

You are working from memory, with no access to any text. That cuts both
ways, and the second way matters more: a confidently invented correction is
worse than no objection at all, because it will be believed. So:

  - Rate 4-5 only when you are genuinely confident the target does not hold
    the ascribed view, and say which work or position you are relying on so
    the claim can be checked.
  - If you are unsure who holds what, SAY SO and rate 1-2. That is a correct
    outcome for this check, not a failure of nerve.
  - Never invent a position, a title, or a date to make the objection land.

If the thesis names no specific target, or names a position rather than a
person, say NOT APPLICABLE.\
"""

EQUIVOCATION_WARNING = """\
A warning specific to this line of attack: equivocation is the easiest
objection to manufacture, because any compressed thesis has terms admitting
more than one reading. It is a real objection ONLY if you can show that the
argument actually NEEDS both readings — that it is plausible on one and
interesting on the other, and cannot be run on either alone. If you cannot
show that, this is NOT APPLICABLE.\
"""

DEFENDER_SYSTEM = """\
You hold this thesis. Your job is to save it if it can be saved.

Answer in two parts, in this order, and NEVER skip the first:

  BEST DEFENCE. State the strongest available reply to the objection —
  the one a capable proponent would give. Push the case: look for a
  version of the objector's own scenario that defeats their distinction,
  a resource in the literature they have ignored, a reason their case is
  not a case of what they claim. Do this even if you suspect it fails.
  Going straight to concession is a FAILURE of your role.

  VERDICT. Only now say whether the defence holds. If it does not, say so
  plainly and say why the defence fails.

Distinguish two things sharply:

  RESISTING is giving a reason the objection does not apply. Always try
  this first.

  HEDGING is narrowing, qualifying or reinterpreting the thesis so the
  objection no longer touches it. Never do this. A thesis that survives
  only by accumulating qualifications is dead — report it as dead rather
  than shrinking it into safety.

Conceding after a real defence is an honourable outcome. Conceding without
one is not an outcome at all.
"""

ADJUDICATOR_SYSTEM = """\
You are ruling on whether a thesis survived an objection. You did not
write either side and have no stake.

Your central question is NOT "was there a reply?" but:

    Was the objection MET, or merely ABSORBED?

An objection is MET if the defence gives a reason the objection does not
apply, or a case that defeats it. An objection is ABSORBED if the defence
narrows, qualifies, or reinterprets the thesis so the objection no longer
touches it. Absorption is failure. Models are strongly biased toward
producing absorption that reads like meeting; look for it.

Judge the EXCHANGE, not the thesis's prospects — a separate reader scores
those and you must not try to. In particular, do not let a thesis you find
unpromising die from a weak objection.

You will be told how many objections were actually mounted and how many
times the defender spoke. Report ONLY what is in the transcript in front of
you. If the defender never spoke, there was NO defence: say so, and do not
describe the objectors' own words as though the defender had offered them.

Score EACH objection separately. Do not take the objector's own strength
rating on trust — rate the damage yourself.

Return ONLY JSON:

{
  "attacks": [
    {"criterion": "the assigned line, e.g. PROVES TOO MUCH",
     "landed": 1-5,
     "met": true | false,
     "note": "one clause: what it did, or why the defence answered it"}
  ],
  "verdict": "untested" | "survives" | "wounded" | "dead",
  "met_or_absorbed": "met" | "absorbed" | "conceded" | "n/a",
  "defended_first": true | false | null,
  "defence_quality": "the best defence the DEFENDER actually gave, or null",
  "surviving_thesis": "the thesis as it now stands, or null if dead",
  "fatal_flaw": "if dead or wounded, what killed it, one sentence",
  "repairable": true | false,
  "repair": "if repairable, the narrowed thesis that would survive, else null"
}

"landed" is how much damage the objection ACTUALLY does to the thesis:
  5 the thesis cannot survive it   4 serious   3 genuine but answerable
  2 weak   1 no force
"met" is whether the defender answered it — gave a reason it does not
apply. A defence that narrows the thesis until the objection misses has NOT
met it; that is absorption, and met is false.

"repairable" is true when the thesis fails as stated but a NARROWER version
plainly survives the objections in front of you — a scope or framing fix,
not a rescue by qualification. Put that narrower version in "repair".

Rules on the verdict:
  - If no objection was mounted (every attack declined), the verdict is
    "untested" — never "survives". Nothing was shown either way.
  - "survives" requires that a real objection was made AND answered.
  - If the defender conceded without mounting a defence, the verdict is at
    most "wounded": a thesis nobody defended has not been shown to fail.
"""

APPRAISER_SYSTEM = """\
You are an editor deciding which of these theses is worth commissioning as
a 6,000-word paper. You have NOT seen any of them attacked, and you are not
being asked whether they are true — only whether each is worth the argument.

Rate promise 1-5:

  5 — if it worked, it would change how people frame this debate
  4 — a real contribution; a good journal would send it out
  3 — competent and publishable somewhere, unlikely to be discussed
  2 — the argument has been made, or the payoff is too small
  1 — confused, or the thesis is not actually contested

You are seeing them TOGETHER so that you can discriminate between them.
Rank them against each other, not against an absolute standard. They must
NOT all receive the same score: whatever the batch, the weakest gets a
lower number than the strongest. Award at most one 5.

Return ONLY a JSON array, one object per thesis, in the order given:
[{"i": 0, "promise": 1-5, "promise_reason": "one sentence"}, ...]
"""


# ---------------------------------------------------------------------------

def extract_json(text):
    """Models wrap JSON in prose and fences. Dig it out."""
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    for opener, closer in (("[", "]"), ("{", "}")):
        i, j = text.find(opener), text.rfind(closer)
        if i != -1 and j > i:
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                continue
    return None


def salvage_list(text):
    """Complete objects from a JSON array that was cut off part-way.

    A generator that runs out of room leaves the last thesis unfinished and
    the whole array unparseable. The finished ones are still good: cut back
    to the last object that closed, close the array, and keep those.
    """
    i = text.find("[")
    if i == -1:
        return None
    body = text[i:]
    for m in reversed(list(re.finditer(r"\}\s*,", body))):
        try:
            got = json.loads(body[:m.start() + 1] + "]")
            if isinstance(got, list) and got:
                return got
        except json.JSONDecodeError:
            continue
    return None


class Client:
    def __init__(self, model, max_tokens=2048):
        self.c = Anthropic()
        self.model = model
        self.max_tokens = max_tokens
        self.calls = 0
        self.log = None
        self.send_temperature = True
        # Output allowances below were sized for Sonnet 4.5. Later models
        # count the same text as roughly half again as many tokens and
        # write at greater length, so an allowance that was ample cuts
        # them off mid-JSON. Everything else gets three times the room.
        self.scale = 1.0 if model.startswith("claude-sonnet-4-5") else 3.0

    def ask(self, system, messages, temperature=1.0, max_tokens=None):
        self.calls += 1
        label = sys._getframe(1).f_code.co_name
        for attempt in range(3):
            try:
                # Newer models refuse any temperature but their default.
                # Send one only while the model accepts it; the log
                # records what was actually sent.
                sent_t = temperature if self.send_temperature else None
                tkw = {} if sent_t is None else {"temperature": sent_t}
                mt = min(20000, int((max_tokens or self.max_tokens)
                                    * self.scale))
                t0 = time.time()
                r = self.c.messages.create(
                    model=self.model,
                    max_tokens=mt,
                    **tkw,
                    system=system,
                    messages=messages,
                )
                txt = "".join(b.text for b in r.content if b.type == "text")
                if getattr(r, "stop_reason", None) == "max_tokens":
                    print("      warning: a %s call hit its output limit "
                          "(%d tokens) and was cut off" % (label, mt),
                          file=sys.stderr)
                if self.log:
                    self.log.record(label, system, messages, txt, r,
                                    sent_t, mt,
                                    time.time() - t0)
                return txt
            except Exception as e:
                if ("temperature" in str(e).lower()
                        and self.send_temperature):
                    self.send_temperature = False
                    if self.log:
                        self.log.set("temperature_refused_by_model",
                                     self.model)
                    print("      " + self.model + " refuses a temperature "
                          "setting; every call now runs at the model's "
                          "default", file=sys.stderr)
                    continue
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)


def load_literature(path):
    if not path:
        return ""
    with open(path) as f:
        items = json.load(f)
    lines = []
    for it in items[:80]:
        bits = [str(it.get(k, "")) for k in ("author", "year", "title")]
        line = " ".join(b for b in bits if b)
        # 4000, not 400: a model-written abstract often spends its first
        # sentences on the view a paper ATTACKS, so a short cut can hand
        # the generators the opposite of what the paper argues.
        abst = (it.get("abstract") or "")[:4000]
        lines.append(f"- {line}" + (f" — {abst}" if abst else ""))
    return ("Recent work in this area (use ONLY to judge whether a thesis is "
            "already taken; do NOT let it steer you toward popular topics):\n"
            + "\n".join(lines))


def literature_works(path):
    """Short labels for the works in the literature file, for --rotate."""
    if not path:
        return []
    with open(path) as f:
        items = json.load(f)
    out = []
    for it in items[:80]:
        bits = [str(it.get(k, "")) for k in ("author", "year")]
        label = " ".join(b for b in bits if b)
        title = str(it.get("title", ""))
        out.append(("%s, \"%s\"" % (label, title)).strip(", "))
    return out


# --- Stage 1 ---------------------------------------------------------------

def assignment_for(i, works):
    """Generator i's move and starting work under --rotate.

    Moves cycle fastest, so any five consecutive generators cover all five.
    The first five have no starting work — one free pass per move — and
    after that each block of five takes the next work in the list.
    """
    move, gloss = MOVES[i % len(MOVES)]
    work = None
    if works and i >= len(MOVES):
        work = works[((i // len(MOVES)) - 1) % len(works)]
    text = ASSIGN_MOVE.format(move=move, gloss=gloss)
    if work:
        text += ASSIGN_TARGET.format(work=work)
    return move, work, text + ASSIGN_TAIL


def generate(client, area, literature, n_generators, per_generator,
             rotate=False, works=None):
    """Isolated parallel samples. No generator sees another's output."""

    def one(i):
        move = work = None
        assignment = ""
        if rotate:
            move, work, assignment = assignment_for(i, works or [])
        prompt = GENERATOR_USER.format(area=area, literature=literature,
                                       assignment=assignment, n=per_generator)
        txt = client.ask(GENERATOR_SYSTEM,
                         [{"role": "user", "content": prompt}],
                         temperature=1.0,
                         max_tokens=max(3000, 600 * per_generator))
        got = extract_json(txt)
        if not isinstance(got, list):
            got = salvage_list(txt)
        if not isinstance(got, list):
            return []
        for t in got:
            t["generator"] = i
            if rotate:
                t["assigned_move"] = move
                t["assigned_work"] = work
        return got

    out = []
    with ThreadPoolExecutor(max_workers=min(n_generators, 8)) as ex:
        futs = [ex.submit(one, i) for i in range(n_generators)]
        for f in as_completed(futs):
            try:
                out.extend(f.result())
            except Exception as e:
                print(f"  generator failed: {e}", file=sys.stderr)
    return out


# --- Stage 2 ---------------------------------------------------------------

# Merges are now recorded on the survivor and shown in the report, so the
# protection against over-merging is visibility, not a veto. A hard cutoff
# here is a cliff edge — 34% merged 68 theses, 36% merged none — so it warns
# in the ordinary range and only refuses when the rate is so high the pass
# is plainly grouping by topic rather than removing duplicates.
CLUSTER_WARN = 0.25
CLUSTER_VETO = 0.60


def cluster(client, theses):
    listing = "\n".join(f"{i}. {t.get('thesis','')}\n   target: "
                        f"{t.get('target','')}\n   move: {t.get('move_type','')}"
                        for i, t in enumerate(theses))
    txt = client.ask(
        CLUSTER_SYSTEM,
        [{"role": "user", "content":
          f"{listing}\n\nReturn ONLY a JSON array of the duplicate groups. "
          f'Each element is an object {{"group": [i, j, ...], "same_claim": '
          f'"the one claim all members assert"}}. Leave out every thesis '
          f"that has no duplicate — most should be left out. If there are "
          f"no duplicates at all, return []."}],
        temperature=0.2, max_tokens=6000)
    parsed = extract_json(txt)
    if not isinstance(parsed, list):
        return theses

    groups = []
    for g in parsed:
        if isinstance(g, int):
            groups.append(([g], ""))
        elif isinstance(g, list):
            groups.append((g, ""))
        elif isinstance(g, dict) and isinstance(g.get("group"), list):
            groups.append((g["group"], str(g.get("same_claim", ""))))

    merged_away = sum(max(0, len([i for i in g if isinstance(i, int)]) - 1)
                      for g, _ in groups)
    rate = merged_away / max(len(theses), 1)
    if rate > CLUSTER_VETO:
        print(f"      clustering discarded: it wanted to merge away "
              f"{merged_away} of {len(theses)} ({100 * rate:.0f}%), which is "
              f"topic-grouping rather than de-duplication. Keeping all.",
              file=sys.stderr)
        return theses
    if rate > CLUSTER_WARN:
        print(f"      note: merging {merged_away} of {len(theses)} "
              f"({100 * rate:.0f}%) — higher than expected. The merges are "
              f"applied but listed under each survivor; check a few.",
              file=sys.stderr)

    kept, seen = [], set()
    for g, same_claim in groups:
        if not isinstance(g, list) or not g:
            continue
        idxs = [i for i in g if isinstance(i, int) and 0 <= i < len(theses)]
        if not idxs:
            continue
        # Keep the best-scoring member, not whichever happened to be first.
        # Clustering runs after appraisal precisely so this is a choice
        # rather than an accident of array order.
        pick = max(idxs, key=lambda i: int(theses[i].get("promise") or 0))
        if pick in seen:
            continue
        seen.add(pick)
        t = dict(theses[pick])
        t["merged_from"] = len(idxs)
        # Nothing disappears without a record: the losers of each merge are
        # carried on the survivor so you can check whether they really were
        # the same thesis.
        t["merged"] = [{"thesis": theses[i].get("thesis"),
                        "promise": theses[i].get("promise")}
                       for i in idxs if i != pick]
        t["merge_claim"] = same_claim
        kept.append(t)
    # Anything the clusterer never mentioned is kept. `groups` holds
    # (indices, claim) pairs, so membership has to be tested against the
    # index list, not the pair.
    covered = {i for g, _ in groups for i in g if isinstance(i, int)}
    for i, t in enumerate(theses):
        if i not in seen and i not in covered:
            kept.append(t)
    return kept


# --- Stage 3 ---------------------------------------------------------------

def kill(client, thesis, literature, rounds, offset=0):
    """Killer vs Defender, then adjudication. The two-Claude conversation.

    Each round assigns the Killer a DIFFERENT line of attack. Left to choose,
    it reaches for equivocation every time — that objection can be
    manufactured against any compressed thesis, so it stops discriminating.
    The rotation offset staggers which attack each thesis meets first.

    MISATTRIBUTION sits outside the rotation and every thesis faces it. The
    rotation deals four of six lines at random with respect to what is
    actually wrong with a thesis, so a thesis aimed at a view nobody holds
    can pass untouched — which is exactly what happened once, and the whole
    argument collapses when it does.
    """
    card = json.dumps({k: thesis.get(k) for k in
                       ("thesis", "move_type", "sketch", "target")}, indent=2)
    transcript, used = [], []
    attacks_mounted = 0

    lines = [MISATTRIBUTION] + [CRITERIA[(offset + r) % len(CRITERIA)]
                                for r in range(rounds)]
    WARNINGS = {"EQUIVOCATION": EQUIVOCATION_WARNING,
                "MISATTRIBUTION": MISATTRIBUTION_WARNING}

    for name, gloss in lines:
        used.append(name)
        system = KILLER_SYSTEM.format(
            criterion=name, gloss=gloss,
            equivocation_warning=WARNINGS.get(name, ""))
        prior = "\n\n".join(f"[{s}] {t}" for s, t in transcript)
        obj = client.ask(
            system,
            [{"role": "user", "content":
              f"{literature}\n\nCandidate:\n{card}\n\n"
              + (f"Exchange so far:\n{prior}\n\n" if prior else "")
              + f"Attack on the assigned line: {name}."}],
            temperature=0.7, max_tokens=1500)
        transcript.append((f"KILLER ({name})", obj))

        if "NOT APPLICABLE" in obj.upper():
            continue  # nothing to defend against; try the next line of attack
        attacks_mounted += 1

        dfn = client.ask(
            DEFENDER_SYSTEM,
            [{"role": "user", "content":
              f"Candidate:\n{card}\n\nExchange so far:\n"
              + "\n\n".join(f"[{s}] {t}" for s, t in transcript)
              + "\n\nBEST DEFENCE first, then VERDICT."}],
            temperature=0.7, max_tokens=1800)
        transcript.append(("DEFENDER", dfn))

    n_defences = sum(1 for s, _ in transcript if s == "DEFENDER")
    # Bigger budget than the model needs: truncated final turns were being
    # adjudicated as though the argument had simply stopped there.
    ruling_txt = client.ask(
        ADJUDICATOR_SYSTEM,
        [{"role": "user", "content":
          f"Candidate:\n{card}\n\nLines of attack assigned: {', '.join(used)}\n"
          f"Objections actually mounted: {attacks_mounted} "
          f"(the rest were declined)\n"
          f"Times the defender spoke: {n_defences}\n\n"
          f"Exchange:\n"
          + "\n\n".join(f"[{s}] {t}" for s, t in transcript)}],
        temperature=0.2, max_tokens=1600)
    ruling = extract_json(ruling_txt) or {"verdict": "unparsed"}

    # Guardrails the adjudicator is asked for but may not honour.
    if attacks_mounted == 0:
        ruling["verdict"] = "untested"
        ruling["defence_quality"] = None
        ruling["met_or_absorbed"] = "n/a"
    if n_defences == 0:
        ruling["defence_quality"] = None
    # Whether a defence was mounted is a fact about the transcript, not a
    # judgement call — the adjudicator was returning false for exchanges
    # containing four long defences. Read it off the text instead.
    ruling["defended_first"] = (
        any("BEST DEFENCE" in t.upper() for s, t in transcript
            if s == "DEFENDER") if n_defences else None)
    if ruling.get("defended_first") is False and ruling.get("verdict") == "dead":
        ruling["verdict"] = "wounded"
        ruling["fatal_flaw"] = ("(downgraded: defender conceded without "
                                "mounting a defence) "
                                + str(ruling.get("fatal_flaw", "")))

    ruling["attacks_tried"] = used
    ruling["attacks_mounted"] = attacks_mounted
    ruling.update(derive_scores(ruling))
    return {**thesis, "ruling": ruling,
            "transcript": [{"speaker": s, "text": t} for s, t in transcript]}


def derive_scores(ruling):
    """Survival scores, DERIVED from the per-attack records.

    Kept separate from kill() on purpose: the per-attack records are the
    data, these numbers are one reading of them. If residual damage turns
    out to be the wrong measure, --rerender recomputes from raw.json
    instead of paying to run the exchanges again.

    residual  strength of the strongest objection that went UNANSWERED.
              0 means nothing unmet landed. This is the ranking number:
              low is robust.
    worst     strongest objection mounted at all, met or not. A low
              residual next to a low worst means the thesis was never
              seriously tested, not that it is sturdy — the caveat I
              could not design away.
    """
    atk = [a for a in (ruling.get("attacks") or []) if isinstance(a, dict)]

    def lv(a):
        try:
            return max(1, min(5, int(a.get("landed", 0))))
        except (TypeError, ValueError):
            return 0

    if not atk:
        # No per-attack records: an older run, or the adjudicator returned
        # nothing usable. Score it as UNKNOWN rather than as zero damage —
        # otherwise every un-scored thesis reads as flawless.
        return {"residual": None, "worst": None,
                "n_unmet": None, "n_attacks_scored": 0}

    unmet = [lv(a) for a in atk if not a.get("met")]
    return {"residual": max(unmet) if unmet else 0,
            "worst": max([lv(a) for a in atk], default=0),
            "n_unmet": len(unmet),
            "n_attacks_scored": len(atk)}


def _score_batch(client, batch, literature):
    """One comparative call over a batch; writes promise onto each thesis."""
    listing = "\n\n".join(
        f"[{i}] {t.get('thesis','')}\n    sketch: {t.get('sketch','')}"
        for i, t in enumerate(batch))
    txt = client.ask(
        APPRAISER_SYSTEM,
        [{"role": "user", "content": f"{literature}\n\nTheses:\n{listing}"}],
        temperature=0.4, max_tokens=3000)
    got = extract_json(txt)
    by_i = {}
    if isinstance(got, list):
        for s in got:
            if isinstance(s, dict) and isinstance(s.get("i"), int):
                by_i[s["i"]] = s
    for i, t in enumerate(batch):
        s = by_i.get(i, {})
        t["promise"] = s.get("promise", 0)
        t["promise_reason"] = s.get("promise_reason", "unscored")


BATCH = 20


def appraise(client, theses, literature, renorm_top=0):
    """Score promise comparatively and BLIND — before anything is attacked.

    Scored one at a time the range collapses; every thesis comes back a 4.
    The scorer has to see a batch to discriminate within it. Large runs are
    chunked, then the leaders are re-scored together so that scores from
    different chunks are actually comparable before we spend money on them.
    """
    chunks = [theses[i:i + BATCH] for i in range(0, len(theses), BATCH)]
    with ThreadPoolExecutor(max_workers=min(len(chunks), 6)) as ex:
        futs = [ex.submit(_score_batch, client, c, literature) for c in chunks]
        for f in as_completed(futs):
            try:
                f.result()
            except Exception as e:
                print(f"      scoring batch failed: {e}", file=sys.stderr)

    if len(chunks) > 1 and renorm_top:
        lead = sorted(theses, key=lambda t: -int(t.get("promise") or 0))
        lead = lead[:min(len(lead), max(renorm_top * 2, BATCH))]
        try:
            _score_batch(client, lead, literature)
        except Exception as e:
            print(f"      renormalisation failed: {e}", file=sys.stderr)
    return theses


# --- Ranking the leaders ---------------------------------------------------
#
# Promise is a five-point score with at most one 5. Across a whole run that
# is enough to separate the good from the rest, but among the leaders it is
# all ties: on the first full run, 47 theses scored 4, and which 24 of them
# were attacked was decided by the order the generators happened to finish.
# So the leaders are also put in a strict order. Each is ranked against
# others in several small batches, shuffled differently each round, and its
# rank is its average standing across the batches it appeared in.

RANK_SYSTEM = """\
You are an editor choosing which theses to commission as 6,000-word papers.
You have NOT seen any of them attacked, and you are not asked whether they
are true — only which are most worth the argument.

These are all strong candidates. Put them in a strict order, best first.
Ties are not allowed. Prefer, in this order:

  1. a thesis that would change how people frame the debate if it worked,
     over one that makes a local correction;
  2. a thesis that is not already taken by the literature listed;
  3. a thesis whose argument could actually be made in 6,000 words.

Return ONLY JSON: {"order": [the bracketed numbers, best first]}
Every number must appear exactly once.
"""

RANK_BATCH = 12
RANK_ROUNDS = 3


def leaders(theses, minimum=40):
    """Positions of the theses that compete for the attack budget.

    Everything scored 4 or 5 for promise, topped up by score to `minimum`
    if fewer than that scored 4 or more.
    """
    order = sorted(range(len(theses)),
                   key=lambda i: -int(theses[i].get("promise") or 0))
    top = [i for i in order if int(theses[i].get("promise") or 0) >= 4]
    if len(top) < minimum:
        top = order[:min(minimum, len(order))]
    return top


def _rank_batch(client, batch, literature):
    listing = "\n\n".join(
        f"[{i}] {t.get('thesis','')}\n    sketch: {t.get('sketch','')}"
        for i, t in enumerate(batch))
    txt = client.ask(
        RANK_SYSTEM,
        [{"role": "user", "content": f"{literature}\n\nTheses:\n{listing}"}],
        temperature=0.4, max_tokens=3000)
    got = extract_json(txt)
    order = got.get("order") if isinstance(got, dict) else got
    seen, out = set(), []
    for i in order if isinstance(order, list) else []:
        if isinstance(i, int) and 0 <= i < len(batch) and i not in seen:
            seen.add(i)
            out.append(i)
    out += [i for i in range(len(batch)) if i not in seen]   # unplaced: last
    return out


def rank_leaders(client, theses, positions, literature, seed=0):
    """Write `rank` (1 = best) and `rank_score` onto theses[positions]."""
    if len(positions) < 2:
        for n, i in enumerate(positions, 1):
            theses[i]["rank"] = n
        return list(positions)
    rng = random.Random(seed)
    jobs = []
    for r in range(RANK_ROUNDS):
        pos = list(positions)
        rng.shuffle(pos)
        k = max(1, -(-len(pos) // RANK_BATCH))           # batches this round
        size = -(-len(pos) // k)
        jobs += [pos[j:j + size] for j in range(0, len(pos), size)]
    scores = {i: [] for i in positions}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(_rank_batch, client, [theses[i] for i in b],
                          literature): b for b in jobs}
        for f in as_completed(futs):
            b = futs[f]
            try:
                order = f.result()
            except Exception as e:
                print(f"      a ranking batch failed: {e}", file=sys.stderr)
                continue
            m = len(order)
            for place, local in enumerate(order):
                scores[b[local]].append(1.0 if m == 1 else 1 - place / (m - 1))
    for i in positions:
        v = scores[i]
        theses[i]["rank_score"] = round(sum(v) / len(v), 3) if v else 0.0
        theses[i]["rank_seen"] = len(v)
    ranked = sorted(positions,
                    key=lambda i: (-theses[i]["rank_score"],
                                   -int(theses[i].get("promise") or 0)))
    for n, i in enumerate(ranked, 1):
        theses[i]["rank"] = n
    return ranked


def write_ranking(theses, ranked, path):
    L = ["# The leaders, in rank order", "",
         "Every thesis scored 4 or 5 for promise, put in a strict order by "
         "ranking it against others in small shuffled batches. The index is "
         "its position in raw.json, which is what --index takes downstream.",
         "", "| Rank | Index | Promise | Status | Residual | Thesis |",
         "| --- | --- | --- | --- | --- | --- |"]
    for i in ranked:
        t = theses[i]
        ru = t.get("ruling") or {}
        verdict = ru.get("verdict", "unattacked")
        if t.get("skipped_duplicate_of_attacked"):
            verdict = "duplicate of an attacked thesis"
        res = ru.get("residual")
        thesis = str(t.get("thesis", "")).replace("|", "/").replace("\n", " ")
        L.append(f"| {t.get('rank')} | {i} | {t.get('promise')} | {verdict} | "
                 f"{'' if res is None else res} | {thesis} |")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


# --- Stage 4 ---------------------------------------------------------------

BUCKETS = [
    ("pick", "Look here first",
     "Promise 4+ with nothing above a 2 left unanswered. Ambitious and hard "
     "to break. Expect a short list, and an empty one on some runs."),
    ("repair", "Repair candidates",
     "Promise 4+, failed on ONE locatable flaw — usually scope or framing, "
     "with the narrower version already written out. Often the richest vein."),
    ("other", "Attacked, ranked",
     "Everything else that went through the adversarial stage."),
    ("unattacked", "Below the cut",
     "Scored for promise, never attacked. Raise --attack-top to reach "
     "further down."),
]


def bucket(r):
    ru = r.get("ruling") or {}
    if ru.get("verdict") == "unattacked":
        return "unattacked"
    p = int(r.get("promise") or 0)
    res = ru.get("residual")
    # residual None means the exchange was never scored per-attack — that is
    # an absence of evidence, so it must not qualify as low damage.
    if p >= 4 and res is not None and int(res) <= 2:
        return "pick"
    if p >= 4 and (ru.get("repairable") or ru.get("n_unmet") == 1):
        return "repair"
    return "other"


def _order(results):
    def key(r):
        res = (r.get("ruling") or {}).get("residual")
        return (-int(r.get("promise") or 0),
                99 if res is None else int(res))
    return sorted(results, key=key)


def _num(v):
    return "–" if v is None else str(v)


def _attribution_doubt(ru):
    """A landed, unanswered MISATTRIBUTION — surfaced separately.

    It deserves its own line because it is the one objection the reader can
    settle instantly and the machine cannot settle at all: whether the named
    target actually holds the ascribed view.
    """
    for a in (ru.get("attacks") or []):
        if not isinstance(a, dict):
            continue
        if "MISATTRIB" in str(a.get("criterion", "")).upper():
            try:
                landed = int(a.get("landed") or 0)
            except (TypeError, ValueError):
                landed = 0
            if landed >= 3 and not a.get("met"):
                return a
    return None


def _cell(s, n=70):
    s = str(s or "").replace("|", "\\|").replace("\n", " ")
    return s[:n] + ("…" if len(s) > n else "")


def _demote(text):
    """Transcript turns arrive containing '# ATTEMPT' and '## VERDICT'.

    Pasted into the report as-is, those become real headings and take over
    the document outline — the section structure reads as scrambled. Demote
    them to bold so the outline stays the report's own.
    """
    return re.sub(r"(?m)^\s{0,3}#{1,6}\s*(.+?)\s*$", r"**\1**", str(text or ""))


HEADNOTE = (
    "**Promise** is scored blind, before any attack. **Residual** is the "
    "strongest objection left unanswered — 0 is best, and it is the ranking "
    "number. **Worst** is the strongest objection mounted at all: when Worst "
    "is also low, the thesis was not seriously tested rather than sturdy.")


def report(results, area, path):
    results = _order(results)
    groups = {k: [r for r in results if bucket(r) == k]
              for k, _, _ in BUCKETS}

    L = [f"# Thesis gate — {area}", "",
         f"{len(results)} candidates. "
         f"**{len(groups['pick'])} in the top-right quadrant**, "
         f"{len(groups['repair'])} repairable, "
         f"{len(groups['unattacked'])} not attacked.", "",
         "Ranked by promise, then by unanswered damage. Nothing has been "
         "eliminated — the verdict is a field, not a filter.", ""]
    folded = sum(len(r.get("merged") or []) for r in results)
    if folded:
        L += [f"> {folded} near-duplicates were folded into the theses below "
              f"({100 * folded // max(folded + len(results), 1)}% of what was "
              f"generated). Each survivor lists what went into it — worth "
              f"opening a couple to check they really were the same thesis.",
              ""]
    L += [HEADNOTE, "",
         "| P | Res | Worst | Verdict | Thesis |",
         "|---|---|---|---|---|"]
    for r in results:
        ru = r.get("ruling") or {}
        L.append(f"| {r.get('promise','?')} | {_num(ru.get('residual'))} | "
                 f"{_num(ru.get('worst'))} | {ru.get('verdict','?')} | "
                 f"{_cell(r.get('thesis'))} |")
    L.append("")

    for key, title, blurb in BUCKETS:
        rows = groups[key]
        if not rows:
            continue
        L += ["---", "", f"## {title}", "", f"*{blurb}*", ""]
        for i, r in enumerate(rows, 1):
            ru = r.get("ruling") or {}
            L += [f"### {key[0].upper()}{i}. {r.get('thesis','(none)')}", "",
                  f"- **Promise {r.get('promise','?')}/5** · residual "
                  f"{_num(ru.get('residual'))}/5 · worst "
                  f"{_num(ru.get('worst'))}/5 · {ru.get('verdict','?')}",
                  f"- **Move:** {r.get('move_type','?')} — **Target:** "
                  f"{r.get('target','—')}",
                  f"- **Sketch:** {r.get('sketch','—')}",
                  f"- **Appraiser (blind):** {r.get('promise_reason','—')}"]
            for a in (ru.get("attacks") or []):
                if not isinstance(a, dict):
                    continue
                mark = "answered" if a.get("met") else "**UNANSWERED**"
                L.append(f"  - {a.get('criterion','?')} — landed "
                         f"{a.get('landed','?')}/5, {mark}. "
                         f"{a.get('note','')}")
            doubt = _attribution_doubt(ru)
            if doubt:
                L.append(f"- ⚑ **Target attribution disputed** — "
                         f"{doubt.get('note','')} *Check this yourself: it is "
                         f"a claim about who holds what, made from recall.*")
            if ru.get("defended_first") is False:
                L.append("- ⚠️ **Defender folded without defending** — treat "
                         "this row's scores as unreliable.")
            if ru.get("repair"):
                L.append(f"- 🔧 **Survives as:** {ru['repair']}")
            elif ru.get("surviving_thesis") and \
                    ru["surviving_thesis"] != r.get("thesis"):
                L.append(f"- **Survives as:** {ru['surviving_thesis']}")
            if ru.get("fatal_flaw"):
                L.append(f"- **Flaw:** {ru['fatal_flaw']}")
            if r.get("merged"):
                L += ["", f"<details><summary>{len(r['merged'])} near-"
                          f"duplicates merged into this one — check whether "
                          f"they really were the same thesis</summary>", ""]
                if r.get("merge_claim"):
                    L += [f"Claimed shared content: *{r['merge_claim']}*", ""]
                for m in r["merged"]:
                    L.append(f"- ({m.get('promise','?')}/5) "
                             f"{m.get('thesis','')}")
                L += ["", "</details>"]
            if r.get("transcript"):
                L += ["", "<details><summary>full exchange</summary>", ""]
                for turn in r["transcript"]:
                    L += [f"**{turn['speaker']}** — {_demote(turn['text'])}",
                          ""]
                L += ["</details>"]
            L += ["", "---", ""]

    with open(path, "w") as f:
        f.write("\n".join(L))


# --- the same report, as a page a browser can render -----------------------

CSS = """
:root { --bg:#fbfaf8; --fg:#1c1b19; --mut:#6b6862; --line:#e0ddd6;
        --card:#fff; --warn:#8a5a00; --warnbg:#fdf6e3; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#161513; --fg:#eceae6; --mut:#9a968e; --line:#302e2a;
          --card:#1e1d1a; --warn:#e0b458; --warnbg:#2a2317; } }
* { box-sizing:border-box }
body { margin:0; padding:2.5rem 1.25rem 6rem; background:var(--bg);
       color:var(--fg); font:16px/1.65 -apple-system,BlinkMacSystemFont,
       "Segoe UI",Helvetica,sans-serif; }
main { max-width:52rem; margin:0 auto }
h1 { font-size:1.5rem; line-height:1.3; margin:0 0 .5rem }
h2 { font-size:1.05rem; text-transform:uppercase; letter-spacing:.08em;
     color:var(--mut); margin:3rem 0 1rem;
     border-bottom:1px solid var(--line); padding-bottom:.4rem }
h3 { font-size:1.12rem; line-height:1.4; margin:0 0 .75rem }
.tally { color:var(--mut); margin:0 0 1.5rem }
.warn { background:var(--warnbg); color:var(--warn); padding:.85rem 1.1rem;
        border-radius:8px; margin:0 0 2rem; font-size:.94rem }
article { background:var(--card); border:1px solid var(--line);
          border-radius:10px; padding:1.4rem 1.5rem; margin:0 0 1.25rem }
dl { margin:0 }
dt { color:var(--mut); font-size:.78rem; text-transform:uppercase;
     letter-spacing:.06em; margin-top:.9rem }
dd { margin:.15rem 0 0 }
.flag { color:var(--warn); font-weight:600 }
details { margin-top:1.25rem; border-top:1px solid var(--line);
          padding-top:.9rem }
summary { cursor:pointer; color:var(--mut); font-size:.9rem }
.turn { margin:1.25rem 0 0; padding-left:.9rem;
        border-left:3px solid var(--line) }
.who { font-size:.75rem; letter-spacing:.07em; text-transform:uppercase;
       color:var(--mut); margin:0 0 .35rem }
.turn p { margin:.5rem 0 }
.note { color:var(--mut); font-size:.92rem; margin:0 0 1.5rem }
table { width:100%; border-collapse:collapse; margin:0 0 2.5rem;
        font-size:.9rem; display:block; overflow-x:auto }
th { text-align:left; color:var(--mut); font-size:.72rem; font-weight:600;
     letter-spacing:.07em; text-transform:uppercase;
     border-bottom:1px solid var(--line); padding:.5rem .6rem }
td { padding:.45rem .6rem; border-bottom:1px solid var(--line);
     vertical-align:top }
td:nth-child(-n+3) { text-align:center; font-variant-numeric:tabular-nums;
                     white-space:nowrap }
tr.hit td { background:var(--warnbg) }
tr.hit td:first-child { font-weight:700 }
dd ul { margin:.2rem 0 0; padding-left:1.1rem }
dd li { margin:.25rem 0 }
"""


def _rich(s):
    """Escape, then honour the little markdown the models emit."""
    s = html.escape(str(s or ""))
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s, flags=re.S)
    s = re.sub(r"(?m)^#{1,6}\s*(.+)$", r"<strong>\1</strong>", s)
    paras = [p.strip().replace("\n", "<br>") for p in s.split("\n\n")
             if p.strip()]
    return "".join(f"<p>{p}</p>" for p in paras) or "<p>—</p>"


def html_report(results, area, path):
    results = _order(results)
    groups = {k: [r for r in results if bucket(r) == k] for k, _, _ in BUCKETS}

    P = ["<!doctype html><meta charset=utf-8>",
         "<meta name=viewport content='width=device-width,initial-scale=1'>",
         f"<title>Thesis gate — {html.escape(area[:60])}</title>",
         f"<style>{CSS}</style><main>",
         f"<h1>Thesis gate</h1><p class=tally>{html.escape(area)}</p>",
         f"<p class=tally>{len(results)} candidates · "
         f"<strong>{len(groups['pick'])} in the top-right quadrant</strong> · "
         f"{len(groups['repair'])} repairable · "
         f"{len(groups['unattacked'])} not attacked</p>",
         f"<p class=note>{_rich(HEADNOTE)}</p>",
         "<table><thead><tr><th>P</th><th>Res</th><th>Worst</th>"
         "<th>Verdict</th><th>Thesis</th></tr></thead><tbody>"]
    for r in results:
        ru = r.get("ruling") or {}
        cls = " class=hit" if bucket(r) == "pick" else ""
        P.append(f"<tr{cls}><td>{r.get('promise','?')}</td>"
                 f"<td>{_num(ru.get('residual'))}</td>"
                 f"<td>{_num(ru.get('worst'))}</td>"
                 f"<td>{html.escape(str(ru.get('verdict','?')))}</td>"
                 f"<td>{html.escape(_cell(r.get('thesis'), 110))}</td></tr>")
    P.append("</tbody></table>")

    for key, title, blurb in BUCKETS:
        rows = groups[key]
        if not rows:
            continue
        P.append(f"<h2>{title}</h2><p class=note>{html.escape(blurb)}</p>")
        for i, r in enumerate(rows, 1):
            ru = r.get("ruling") or {}
            P.append("<article>")
            P.append(f"<h3>{key[0].upper()}{i}. "
                     f"{html.escape(str(r.get('thesis','(none)')))}</h3>")
            P.append("<dl>")
            P.append(f"<dt>Scores</dt><dd>promise "
                     f"<strong>{r.get('promise','?')}/5</strong> · residual "
                     f"{_num(ru.get('residual'))}/5 · worst "
                     f"{_num(ru.get('worst'))}/5 · "
                     f"{html.escape(str(ru.get('verdict','?')))}</dd>")
            P.append(f"<dt>Move · Target</dt><dd>"
                     f"{html.escape(str(r.get('move_type','?')))} — "
                     f"{html.escape(str(r.get('target','—')))}</dd>")
            P.append(f"<dt>Sketch</dt><dd>{_rich(r.get('sketch'))}</dd>")
            P.append(f"<dt>Appraiser (blind)</dt><dd>"
                     f"{html.escape(str(r.get('promise_reason','—')))}</dd>")
            atk = [a for a in (ru.get("attacks") or []) if isinstance(a, dict)]
            if atk:
                P.append("<dt>Objections</dt><dd><ul>")
                for a in atk:
                    mark = ("answered" if a.get("met")
                            else "<strong>unanswered</strong>")
                    P.append(f"<li>{html.escape(str(a.get('criterion','?')))} "
                             f"— landed {a.get('landed','?')}/5, {mark}. "
                             f"{html.escape(str(a.get('note','')))}</li>")
                P.append("</ul></dd>")
            doubt = _attribution_doubt(ru)
            if doubt:
                P.append(f"<dd class=flag>⚑ Target attribution disputed — "
                         f"{html.escape(str(doubt.get('note','')))} "
                         f"Check this yourself: it is a claim about who holds "
                         f"what, made from recall.</dd>")
            if ru.get("defended_first") is False:
                P.append("<dd class=flag>⚠ Defender folded without "
                         "defending — treat these scores as unreliable.</dd>")
            if ru.get("repair"):
                P.append(f"<dt>🔧 Survives as</dt><dd>"
                         f"{_rich(ru['repair'])}</dd>")
            elif ru.get("surviving_thesis") and \
                    ru["surviving_thesis"] != r.get("thesis"):
                P.append(f"<dt>Survives as</dt><dd>"
                         f"{_rich(ru['surviving_thesis'])}</dd>")
            if ru.get("fatal_flaw"):
                P.append(f"<dt>Flaw</dt><dd>{_rich(ru['fatal_flaw'])}</dd>")
            if r.get("merged"):
                P.append(f"<dt>Merged in ({len(r['merged'])})</dt><dd>")
                if r.get("merge_claim"):
                    P.append(f"<em>claimed shared content: "
                             f"{html.escape(str(r['merge_claim']))}</em>")
                P.append("<ul>")
                for m in r["merged"]:
                    P.append(f"<li>({m.get('promise','?')}/5) "
                             f"{html.escape(str(m.get('thesis','')))}</li>")
                P.append("</ul></dd>")
            P.append("</dl>")
            if r.get("transcript"):
                P.append(f"<details><summary>full exchange "
                         f"({len(r['transcript'])} turns)</summary>")
                for turn in r["transcript"]:
                    P.append(f"<div class=turn><p class=who>"
                             f"{html.escape(str(turn['speaker']))}</p>"
                             f"{_rich(turn['text'])}</div>")
                P.append("</details>")
            P.append("</article>")

    P.append("</main>")
    with open(path, "w") as f:
        f.write("\n".join(P))


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--area", required=True,
                   help="the debate, described in a sentence or two")
    p.add_argument("--generators", type=int, default=6)
    p.add_argument("--per-generator", type=int, default=4)
    p.add_argument("--kill-rounds", type=int, default=4)
    p.add_argument("--attack-top", type=int, default=25,
                   help="how many of the highest-promise theses get the "
                        "adversarial treatment (the expensive stage)")
    p.add_argument("--no-cluster", action="store_true",
                   help="skip de-duplication entirely; duplicates then "
                        "compete for attack slots on their own merits")
    p.add_argument("--rerender", default=None, metavar="RAW.JSON",
                   help="rebuild the reports from a previous run's raw.json "
                        "with the current scoring; makes no API calls")
    p.add_argument("--attack-more", default=None, metavar="RAW.JSON",
                   help="continue an earlier run instead of generating: "
                        "find duplicates among its leaders, then attack the "
                        "--attack-top best theses that were never attacked. "
                        "Writes a complete new run folder to --out; the "
                        "earlier folder is not touched")
    p.add_argument("--no-rank", action="store_true",
                   help="skip the strict ranking of the leaders and cut by "
                        "promise score alone, as the first runs did")
    p.add_argument("--rotate", action="store_true",
                   help="give each generator a different assignment: one of "
                        "the five move types, and (after the first five) a "
                        "work from --literature to start from. Use when "
                        "isolated generators converge on the same theses")
    p.add_argument("--literature", default=None,
                   help="optional JSON file of recent work")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="run1")
    p.add_argument("--dry-run", action="store_true",
                   help="print the call budget and exit")
    args = p.parse_args()

    if args.rerender:
        rerender(args.rerender)
        return

    if args.attack_more:
        attack_more(args)
        return

    raw = args.generators * args.per_generator
    attacked = min(args.attack_top, raw)
    scoring = -(-raw // BATCH) + (1 if raw > BATCH else 0)
    # +1 attack per thesis: MISATTRIBUTION runs outside the rotation.
    est = (args.generators + 1 + scoring
           + attacked * ((args.kill_rounds + 1) * 2 + 1))
    if args.dry_run:
        print(f"~{raw} raw theses; the top {attacked} get attacked.")
        print(f"~{est} API calls (~${est * 0.006:.2f} at recent rates — "
              f"the attack stage is nearly all of it).")
        print(f"--kill-rounds {args.kill_rounds}: each attacked thesis faces "
              f"{min(args.kill_rounds, len(CRITERIA))} of {len(CRITERIA)} "
              f"rotated lines of attack, plus MISATTRIBUTION every time.")
        print("Generate widely and attack narrowly: raise --generators "
              "freely, raise --attack-top only as far as you'll read.")
        return

    os.makedirs(args.out, exist_ok=True)
    client = Client(args.model)
    client.log = RunLog(args.out, __file__, args, globals())
    client.log.set("output_allowance_scale", client.scale)
    lit = load_literature(args.literature)

    print(f"[1/5] generating — {args.generators} isolated samples…")
    works = literature_works(args.literature) if args.rotate else []
    client.log.set("rotation", bool(args.rotate))
    theses = generate(client, args.area, lit, args.generators,
                      args.per_generator, rotate=args.rotate, works=works)
    print(f"      {len(theses)} raw candidates")
    client.log.set("raw_candidates", len(theses))
    if not theses:
        print("nothing generated; check your key and model id", file=sys.stderr)
        return

    # Promise is cheap and attacking is expensive, so score first and spend
    # the adversarial budget only on the leaders. Scoring also runs BEFORE
    # clustering so that each merge keeps its best member rather than its
    # first — clustering is the one stage that still discards anything.
    print(f"[2/5] scoring promise (blind, comparative) — {len(theses)}…")
    theses = appraise(client, theses, lit, renorm_top=args.attack_top)

    if args.no_cluster:
        print(f"[3/5] clustering skipped — keeping all {len(theses)}")
    else:
        print("[3/5] clustering duplicates…")
        before = len(theses)
        # Only the leaders. Duplicates matter where the attack budget is
        # spent; comparing every pair among hundreds of theses is a task a
        # reasoning model can spend its whole allowance thinking about and
        # then answer nothing — which is what happened on the first run.
        theses.sort(key=lambda t: -int(t.get("promise") or 0))
        n_lead = min(len(theses), max(2 * args.attack_top, 40))
        theses = cluster(client, theses[:n_lead]) + theses[n_lead:]
        dropped = before - len(theses)
        print(f"      {len(theses)} distinct ({dropped} merged away, "
              f"{100 * dropped // max(before, 1)}%)")
    theses.sort(key=lambda t: -int(t.get("promise") or 0))
    if not args.no_rank:
        lead = leaders(theses)
        print(f"[3b] ranking the {len(lead)} leaders in a strict order…")
        ranked = rank_leaders(client, theses, lead, lit)
        in_rank = set(ranked)
        rest = [i for i in range(len(theses)) if i not in in_rank]
        theses = [theses[i] for i in ranked] + [theses[i] for i in rest]
        client.log.set("leaders_ranked", len(ranked))
    for t in theses[:5]:
        print(f"      {t.get('promise','?')}/5  {str(t.get('thesis',''))[:64]}")

    cut = max(1, min(args.attack_top, len(theses)))
    front, rest = theses[:cut], theses[cut:]
    client.log.set("distinct_after_clustering", len(theses))
    client.log.set("attacked", len(front))
    print(f"[4/5] attacking top {len(front)} of {len(theses)} — "
          f"{args.kill_rounds} rounds each…")
    results = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(kill, client, t, lit, args.kill_rounds, i): t
                for i, t in enumerate(front)}
        for n, f in enumerate(as_completed(futs), 1):
            try:
                r = f.result()
                results.append(r)
                ru = r["ruling"]
                print(f"      {n}/{len(front)} promise "
                      f"{r.get('promise','?')}/5  residual "
                      f"{_num(ru.get('residual'))}/5  "
                      f"{str(r.get('thesis',''))[:52]}")
            except Exception as e:
                print(f"      attack failed: {e}", file=sys.stderr)
    for t in rest:
        results.append({**t, "ruling": {"verdict": "unattacked"},
                        "transcript": []})

    print("[5/5] writing report…")
    write_outputs(results, args.area, args.out)
    ranked_pos = sorted([i for i, r in enumerate(results) if r.get("rank")],
                        key=lambda i: results[i]["rank"])
    if ranked_pos:
        write_ranking(results, ranked_pos, os.path.join(args.out, "ranking.md"))
    n_pick = sum(1 for r in results if bucket(r) == "pick")
    print(f"\n{client.calls} API calls. {n_pick} in the top-right quadrant "
          f"(promise 4+, residual 2 or less).")
    client.log.set("top_right_quadrant", n_pick)
    print(client.log.summary())
    print(f"open {os.path.join(args.out,'gate.html')}   <- start here")


def duplicate_groups(client, lead):
    """Groups of duplicates among `lead`, as lists of positions in it."""
    listing = "\n".join(f"{i}. {t.get('thesis','')}\n   target: "
                        f"{t.get('target','')}\n   move: {t.get('move_type','')}"
                        for i, t in enumerate(lead))
    txt = client.ask(
        CLUSTER_SYSTEM,
        [{"role": "user", "content":
          f"{listing}\n\nReturn ONLY a JSON array of the duplicate groups. "
          f'Each element is an object {{"group": [i, j, ...], "same_claim": '
          f'"the one claim all members assert"}}. Leave out every thesis '
          f"that has no duplicate — most should be left out. If there are "
          f"no duplicates at all, return []."}],
        temperature=0.2, max_tokens=6000)
    parsed = extract_json(txt)
    out = []
    for g in parsed if isinstance(parsed, list) else []:
        if isinstance(g, dict) and isinstance(g.get("group"), list):
            idxs = sorted({i for i in g["group"]
                           if isinstance(i, int) and 0 <= i < len(lead)})
            if len(idxs) > 1:
                out.append((idxs, str(g.get("same_claim", ""))))
    return out


def attack_more(args):
    """Extend an earlier run: mark duplicates, attack the next-best theses.

    Nothing is regenerated and nothing already attacked is attacked again.
    Duplicates are MARKED, not merged — some of them have transcripts, and
    a transcript is not something to throw away. An unattacked thesis is
    skipped only if a duplicate of it has already been through the attack.
    """
    with open(args.attack_more) as f:
        results = json.load(f)
    os.makedirs(args.out, exist_ok=True)
    client = Client(args.model)
    client.log = RunLog(args.out, __file__, args, globals())
    client.log.set("output_allowance_scale", client.scale)
    client.log.set("continues", os.path.abspath(args.attack_more))
    lit = load_literature(args.literature)

    def attacked(r):
        return (r.get("ruling") or {}).get("verdict") not in (None, "unattacked")

    n_already = sum(1 for r in results if attacked(r))
    lead_idx = leaders(results)
    n_lead = len(lead_idx)
    # A folder this command already wrote carries its duplicate groups and
    # its ranking. Continuing from it reuses both, so the order you read in
    # ranking.md is the order that gets attacked, not a fresh draw.
    reuse = all(results[i].get("rank") for i in lead_idx)
    if reuse:
        print(f"[1/4] reusing the duplicate groups and ranking already in "
              f"{os.path.basename(os.path.dirname(os.path.abspath(args.attack_more)))}")
        by_g = {}
        for i in lead_idx:
            g = results[i].get("dup_group")
            if g:
                by_g.setdefault(g, []).append(i)
        groups = [([lead_idx.index(i) for i in members],
                   results[members[0]].get("dup_claim", ""))
                  for g, members in sorted(by_g.items())]
    else:
        print(f"[1/4] looking for duplicates among the {n_lead} leaders…")
        groups = duplicate_groups(client, [results[i] for i in lead_idx])
    skip, lines = set(), ["# Duplicate groups among the leaders", ""]
    for gid, (members, claim) in enumerate(groups, 1):
        real = [lead_idx[m] for m in members]
        for i in real:
            results[i]["dup_group"] = gid
            results[i]["dup_claim"] = claim
        done = [i for i in real if attacked(results[i])]
        fresh = [i for i in real if not attacked(results[i])]
        if done:
            skip.update(fresh)            # a twin has already been attacked
        else:
            skip.update(fresh[1:])        # attack one of them, the best
        lines += [f"## Group {gid}", "", f"*Shared claim:* {claim}", ""]
        for i in real:
            ru = results[i].get("ruling") or {}
            lines.append(f"- index {i} · promise {results[i].get('promise')} · "
                         f"{ru.get('verdict', 'unattacked')} — "
                         f"{results[i].get('thesis')}")
        lines.append("")
    with open(os.path.join(args.out, "duplicates.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    in_groups = sum(len(m) for m, _ in groups)
    print(f"      {len(groups)} groups covering {in_groups} theses "
          f"— see duplicates.md")

    for i in skip:
        if any(attacked(results[j]) for j in lead_idx
               if results[j].get("dup_group") == results[i].get("dup_group")):
            results[i]["skipped_duplicate_of_attacked"] = True

    if reuse:
        order = sorted(lead_idx, key=lambda i: results[i]["rank"])
    elif args.no_rank:
        order = sorted(lead_idx,
                       key=lambda i: -int(results[i].get("promise") or 0))
    else:
        print(f"[2/4] ranking the {n_lead} leaders in a strict order…")
        order = rank_leaders(client, results, lead_idx, lit)
        write_ranking(results, order, os.path.join(args.out, "ranking.md"))
        print("      written to ranking.md")
    todo = [i for i in order if not attacked(results[i]) and i not in skip]
    todo = todo[:args.attack_top]
    print(f"[3/4] attacking {len(todo)} more — {args.kill_rounds} rounds each…")
    clean = lambda r: {k: v for k, v in r.items()
                       if k not in ("ruling", "transcript")}
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(kill, client, clean(results[i]), lit,
                          args.kill_rounds, n_already + n): i
                for n, i in enumerate(todo)}
        for n, f in enumerate(as_completed(futs), 1):
            i = futs[f]
            try:
                results[i] = f.result()
                ru = results[i]["ruling"]
                print(f"      {n}/{len(todo)} promise "
                      f"{results[i].get('promise','?')}/5  residual "
                      f"{_num(ru.get('residual'))}/5  "
                      f"{str(results[i].get('thesis',''))[:52]}")
            except Exception as e:
                print(f"      attack failed: {e}", file=sys.stderr)

    print("[4/4] writing report…")
    write_outputs(results, args.area, args.out)
    if reuse or not args.no_rank:
        write_ranking(results, order, os.path.join(args.out, "ranking.md"))
    n_pick = sum(1 for r in results if bucket(r) == "pick")
    client.log.set("duplicate_groups", len(groups))
    client.log.set("skipped_as_duplicates", len(skip))
    client.log.set("leaders_ranked", 0 if (args.no_rank or reuse) else n_lead)
    client.log.set("reused_ranking_from_input", reuse)
    client.log.set("attacked_this_time", len(todo))
    client.log.set("attacked_in_total", sum(1 for r in results if attacked(r)))
    client.log.set("top_right_quadrant", n_pick)
    print(f"\n{n_pick} in the top-right quadrant across the whole run.")
    print(client.log.summary())
    print(f"open {os.path.join(args.out,'gate.html')}   <- start here")


def write_by_index(results, path):
    """Every attacked thesis with its index — the number later steps take.

    gate.html is ordered for reading and never shows the index, so on the
    first run the theses could not be found by the numbers used to discuss
    them. This page lists them by index, in rank order where there is one.
    """
    E = html.escape
    att = [i for i, t in enumerate(results)
           if (t.get("ruling") or {}).get("verdict") not in (None, "unattacked")]
    att.sort(key=lambda i: (results[i].get("rank") or 999,
                            -int(results[i].get("promise") or 0)))
    toc, secs = [], []
    for i in att:
        t, ru = results[i], results[i]["ruling"]
        toc.append(f"<tr><td><a href='#i{i}'>{i}</a></td><td>{t.get('rank','')}</td>"
                   f"<td>{t.get('promise')}</td><td>{ru.get('residual')}</td>"
                   f"<td>{E(str(ru.get('verdict')))}</td>"
                   f"<td>{E(str(t.get('thesis',''))[:140])}…</td></tr>")
        rows = "".join(
            f"<tr><td>{E(str(a.get('criterion')))}</td><td>{E(str(a.get('landed')))}</td>"
            f"<td>{'yes' if a.get('met') else 'no'}</td><td>{E(str(a.get('note') or ''))}</td></tr>"
            for a in ru.get("attacks") or [])
        rep = f"<p><b>Repair.</b> {E(str(ru['repair']))}</p>" if ru.get("repair") else ""
        secs.append(
            f"<section id='i{i}'><h2>Index {i} <span class=m>· rank {t.get('rank','–')} · "
            f"promise {t.get('promise')} · residual {ru.get('residual')} · worst "
            f"{ru.get('worst')} · {E(str(ru.get('verdict')))}</span></h2>"
            f"<p><b>Thesis.</b> {E(str(t.get('thesis','')))}</p>"
            f"<p><b>Surviving thesis.</b> {E(str(ru.get('surviving_thesis') or '— none (dead)'))}</p>"
            f"<p><b>Fatal flaw.</b> {E(str(ru.get('fatal_flaw') or '— none'))}</p>{rep}"
            f"<details><summary>Objections</summary><table><tr><th>Objection</th>"
            f"<th>Landed</th><th>Met</th><th>Note</th></tr>{rows}</table></details>"
            f"<details><summary>Generator's sketch</summary><p>{E(str(t.get('sketch') or ''))}</p>"
            f"</details></section>")
    page = (
        "<!doctype html><meta charset=utf-8><title>Attacked theses by index</title>"
        "<style>body{font:15px/1.5 -apple-system,Helvetica,sans-serif;max-width:900px;"
        "margin:2em auto;padding:0 1em;color:#222}h2{font-size:1.1em;margin-top:2em;"
        "border-top:1px solid #ddd;padding-top:1em}.m{font-weight:normal;color:#666}"
        "table{border-collapse:collapse;width:100%;font-size:.9em}td,th{border-bottom:"
        "1px solid #eee;padding:4px 6px;text-align:left;vertical-align:top}"
        "summary{cursor:pointer;color:#555}</style>"
        f"<h1>The {len(att)} attacked theses, by index</h1><p>In rank order. The index "
        "is the number every later command takes (--index).</p><table><tr><th>Index</th>"
        "<th>Rank</th><th>Promise</th><th>Residual</th><th>Verdict</th><th>Thesis</th></tr>"
        + "".join(toc) + "</table>" + "".join(secs))
    with open(path, "w") as f:
        f.write(page)


def write_outputs(results, area, out):
    os.makedirs(out, exist_ok=True)
    write_by_index(results, os.path.join(out, "by_index.html"))
    with open(os.path.join(out, "raw.json"), "w") as f:
        json.dump(results, f, indent=2)
    report(results, area, os.path.join(out, "gate.md"))
    html_report(results, area, os.path.join(out, "gate.html"))


def rerender(path):
    """Recompute the derived scores and rebuild the reports from raw.json.

    The per-attack records are the data; residual damage is one reading of
    them. Change derive_scores() and re-run this — no API calls, no cost.
    """
    out = os.path.dirname(os.path.abspath(path)) or "."
    with open(path) as f:
        results = json.load(f)
    for r in results:
        ru = r.setdefault("ruling", {})
        # older runs kept promise inside ruling; lift it to the top level
        if "promise" not in r and "promise" in ru:
            r["promise"] = ru.get("promise")
            r["promise_reason"] = ru.get("promise_reason")
        ru.update(derive_scores(ru))
    area = "re-rendered from " + os.path.basename(path)
    write_outputs(results, area, out)
    print(f"rebuilt {len(results)} rows, no API calls")
    print(f"open {os.path.join(out,'gate.html')}")


if __name__ == "__main__":
    main()
