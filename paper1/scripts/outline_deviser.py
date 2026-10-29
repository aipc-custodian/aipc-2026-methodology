#!/usr/bin/env python3
"""
outline_deviser.py — the middle stage.

Takes ONE thesis that survived the Forge and produces several independent
outlines of the paper that would argue for it. You read them and pick.

    Stage 1  DEVISE    N isolated outlines, high temperature, blind to each
                       other. Same argument as the Forge's generate stage:
                       dialogue collapses variance, and variance is the only
                       thing this stage produces.
    Stage 2  AUDIT     pure Python, no API calls. The outlines carry a
                       dependency ledger; the audit reads coherence off it
                       rather than asking a model to judge coherence.
    Stage 3  DIVERGE   one call: which structural moves every outline makes
                       (the thesis forces them) and which they split on
                       (free, and yours).
    Stage 4  REPORT    outlines.html + outlines.md + raw.json.

There is NO attack stage and NO ranking. Six outlines do not exceed one
reader's attention; adjudication here would only interpose a mediocre
reader between you and six documents you are going to read anyway.

The kill transcript is deliberately NOT fed in — not the objections, not
the concessions, not the defence. Only the thesis as it stands after the
kill (`surviving_thesis`), which is the thesis. An outline built around
surviving known objections is a defensive outline, and defensive papers
hedge.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...

    # see what is in a Forge run
    python outline_deviser.py --raw self2/raw.json --list

    # build from one of them
    python outline_deviser.py --raw self2/raw.json --match "inverted" \
        --outlines 6 --out outlines1

    # or from a thesis typed in directly
    python outline_deviser.py --thesis "..." --out outlines1

    # rebuild reports from a previous run, no API calls
    python outline_deviser.py --rerender outlines1/raw.json
"""

import argparse, difflib, html, json, os, re, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from anthropic import Anthropic
except ImportError:                                  # --rerender/--list/--dry-run
    Anthropic = None                                 # still work without it

MODEL = "claude-sonnet-4-5"


# ---------------------------------------------------------------------------
# Prompts. These are the actual intellectual content of the stage — edit
# them more readily than you edit the code.
# ---------------------------------------------------------------------------

DEVISER_SYSTEM = """\
You are a philosopher planning a 6,000-word journal article that argues for
a thesis you have been given. You are NOT writing the paper and NOT
defending the thesis here. You are deciding what the paper's argument is and
what order it goes in.

The thesis is fixed. Do not improve it, soften it, broaden it, or argue
about whether it is true. Your job is the ARCHITECTURE.

Seven requirements. An outline that cannot satisfy all seven is not a
weaker outline, it is not an outline — rework it until it does.

1. COMMITMENT. Every section states the one claim it establishes and what
   would refute that claim. The refutation condition must have an ADDRESS:
   a position someone actually holds, named, with who holds it.

   The test is whether you could put the refuting claim to a living
   philosopher and have them assent to it. So:

     NOT an address — "this fails if the phenomenon turns out not to
     exist", "this fails if the distinction collapses". Nobody holds these.
     They are unfalsifiable in practice and cost you nothing to write.

     An address — "this fails if <NAMED PHILOSOPHER> is right that <the
     specific thing they claim>". A person, a claim they actually make, and
     a reader who can go and check.

   Name real people and state their real views. Do not invent a position to
   have something to name, and do not name someone whose view is adjacent
   to the one you need — an address aimed at nobody is worse than none,
   because it looks like work has been done.

2. LEDGER. Every section states what it takes as given, and from where:
   either an earlier section, or an undefended background assumption.
   When a section takes a claim from an earlier section, it must reproduce
   that section's `establishes` sentence WORD FOR WORD. Not a paraphrase,
   not a summary, not a tightened version — the same characters. This is
   the single most important formal constraint here, because arguments
   drift upward in paraphrase: §3 establishes something modest, §5 quotes
   it back slightly stronger, and the gap is invisible in prose. Copy the
   sentence.

3. WORK. No section exists because papers have such sections. Each must be
   needed by something later, or be the section that arrives at the thesis.
   A section that establishes something nothing downstream consumes is a
   defect even if the section is good.

4. ARRIVAL. The argument must reach the thesis AS GIVEN, not a weaker
   neighbour of it. Say which section arrives. The support may be
   deductive, strong inductive, or abductive — the kind of inference is
   free, the arrival is not.

5. THE GAP. Somewhere the outline is at its greatest distance between what
   has been established and what is being claimed. Find that place, name
   the inference doing the work there, and say what would have to be true
   for it to go through. Every outline has such a place. An outline that
   reports no gap has not looked.

6. WEIGHT. Identify the claim the most sections depend on. That claim is
   where the paper lives, and it must be defended in proportion.

7. FRAME. The paper has an introduction and a conclusion. Mark them as
   such. They are not argumentative sections: an introduction establishes
   nothing and nothing depends on it, a conclusion establishes nothing new,
   and neither carries a refutation condition or a ledger entry. They exist
   because papers have readers.

   Everything between them is the argument, and there is NO TARGET NUMBER
   of those. Three substantive sections is a perfectly good paper; so is
   seven. The count is whatever requirement 3 leaves standing after you
   have cut every section that nothing needs. Do not pad toward a shape.

Then two things about the outline as a whole:

  SURPRISE — what would a specialist in this area find surprising here, and
  why. Not what is interesting about the thesis; what is surprising about
  THIS STRUCTURE for arguing it.

  COMMITMENT — what does this outline commit to that a cautious version of
  the same paper would not? If nothing, the outline is hedged and you
  should rebuild it before answering.

Do not include a section whose purpose is to "address concerns" or "discuss
implications". If an objection is worth answering, it is answered inside
the section whose claim it threatens, and that section says so.
"""

DEVISER_USER = """\
THESIS (fixed — argue for exactly this):
{thesis}

{context}

Produce ONE outline. Return ONLY JSON, no prose around it:

{{
  "title": "working title of the paper",
  "shape": "one sentence: the argumentative strategy in the large",
  "structure": "standard" | "deviant",
  "structure_note": "if deviant, how and why; else null",
  "sections": [
    {{
      "n": 1,
      "role": "intro" | "substantive" | "conclusion",
      "heading": "section heading",
      "establishes": "ONE declarative sentence — the claim this section \
establishes. Later sections must quote this sentence verbatim. For an \
intro or conclusion, null.",
      "refuted_by": "what would refute this claim",
      "address": "a position someone actually holds that would refute it, \
with who holds it",
      "takes_as_given": [
        {{"claim": "verbatim `establishes` of an earlier section, OR a \
background assumption stated as a sentence",
          "from": "3" for section 3, or "assumed"}}
      ],
      "work": "one clause: what later part of the argument needs this"
    }}
  ],
  "arrives_at": "the section number that establishes the thesis",
  "load_bearing": "verbatim `establishes` of the claim most sections depend on",
  "gap": {{
    "section": "section number",
    "inference": "deductive" | "inductive" | "abductive",
    "statement": "what would have to be true for the inference to go through"
  }},
  "surprise": "one or two sentences",
  "commitment": "one or two sentences"
}}

Exactly one section with role "intro" (first) and one with role
"conclusion" (last). Both have establishes, refuted_by, address and
takes_as_given set to null or empty — they are frame, not argument.

How many SUBSTANTIVE sections between them? However many distinct claims
the argument needs, and not one more. Work out the claims and their
dependencies FIRST; the sections are whatever falls out of that. Do not aim
at a count, and do not reach for a familiar paper shape and distribute the
argument into it — a section that exists because the shape has a slot there
is the defect requirement 3 rules out. If two sections establish claims that
always travel together, they are one section. If one section establishes two
claims that later sections take up separately, it is two.

An argument with three moves gets three substantive sections. Say so rather
than padding to something that looks like an article. A long paper with
three substantive sections is a normal paper.

The first substantive section may take everything as "assumed"; every later
one should take at least one thing from an earlier one, or you have written
a list rather than an argument. `arrives_at` names a substantive section,
never the conclusion.
"""

DIVERGE_SYSTEM = """\
You are comparing several independent outlines of the SAME paper, written
blind to each other. You are not ranking them and must not try. Nobody
wants a winner here; the reader wants to see the shape of the space.

The question is which structural choices the thesis FORCES and which are
FREE. A move every outline makes is forced — the thesis does not permit the
paper to be built without it. A move only some make is free, and the reader
gets to choose it deliberately rather than by accident.

Report only what is actually there. Do not invent agreement by describing
two different moves in one vague phrase, and do not manufacture
disagreement out of wording.

Return ONLY JSON:

{
  "forced": ["moves every outline makes, one clause each"],
  "free": [
    {"move": "the choice at issue",
     "options": ["how outline A does it", "how outline B does it"],
     "outlines": "which outlines take which option"}
  ],
  "sharpest": "the single structural disagreement that most changes what \
the paper would be, and what turns on it",
  "absent": "anything you would expect an outline of this thesis to \
contain that NONE of them has, or null"
}
"""


# ---------------------------------------------------------------------------
# Infrastructure — kept deliberately parallel to thesis_forge.py
# ---------------------------------------------------------------------------

def extract_json(text):
    """Models wrap JSON in prose and fences. Dig it out."""
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    for opener, closer in (("{", "}"), ("[", "]")):
        i, j = text.find(opener), text.rfind(closer)
        if i != -1 and j > i:
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                continue
    return None


class Client:
    def __init__(self, model, max_tokens=4096):
        if Anthropic is None:
            sys.exit("the anthropic package is not installed: pip install anthropic")
        self.c = Anthropic()
        self.model = model
        self.max_tokens = max_tokens
        self.calls = 0

    def ask(self, system, messages, temperature=1.0, max_tokens=None):
        self.calls += 1
        for attempt in range(3):
            try:
                r = self.c.messages.create(
                    model=self.model,
                    max_tokens=max_tokens or self.max_tokens,
                    temperature=temperature,
                    system=system,
                    messages=messages,
                )
                return "".join(b.text for b in r.content if b.type == "text")
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)


# ---------------------------------------------------------------------------
# Picking the thesis out of a Forge run
# ---------------------------------------------------------------------------

def load_thesis(raw_path, match=None, index=None):
    """Pull one thesis from a Forge raw.json.

    The BUILD TARGET is `ruling.surviving_thesis` when there is one — the
    thesis as it stands after the kill, which is more precise than the
    headline and is the thing the paper actually has to reach. Everything
    else from the kill stage (attacks, transcript, defence, fatal_flaw) is
    deliberately left behind.
    """
    with open(raw_path) as f:
        results = json.load(f)

    if index is not None:
        if not 0 <= index < len(results):
            sys.exit("index %d out of range (0..%d)" % (index, len(results) - 1))
        r = results[index]
    elif match:
        needle = match.lower()
        hits = [(i, x) for i, x in enumerate(results)
                if needle in (str(x.get("thesis", "")) + " "
                              + str(x.get("sketch", ""))).lower()]
        if not hits:
            sys.exit("no thesis matching %r — try --list" % match)
        if len(hits) > 1:
            print("%d theses match %r; using index %d. Others: %s"
                  % (len(hits), match, hits[0][0],
                     ", ".join(str(i) for i, _ in hits[1:])), file=sys.stderr)
        r = hits[0][1]
    else:
        sys.exit("give --match or --index (or --list to look)")

    ruling = r.get("ruling") or {}
    surviving = ruling.get("surviving_thesis")
    return {
        "thesis": (surviving or r.get("thesis") or "").strip(),
        "headline": (r.get("thesis") or "").strip(),
        "used_surviving": bool(surviving),
        "sketch": r.get("sketch"),
        "target": r.get("target"),
        "move_type": r.get("move_type"),
        "promise": r.get("promise"),
        "residual": ruling.get("residual"),
    }


def list_theses(raw_path, limit=40):
    with open(raw_path) as f:
        results = json.load(f)

    def key(x):
        ru = x.get("ruling") or {}
        res = ru.get("residual")
        return (-int(x.get("promise") or 0), 99 if res is None else int(res))

    order = sorted(range(len(results)), key=lambda i: key(results[i]))
    print("%-6s %-8s %-9s %s" % ("index", "promise", "residual", "thesis"))
    for i in order[:limit]:
        r = results[i]
        ru = r.get("ruling") or {}
        res = ru.get("residual")
        print("%-6d %-8s %-9s %s"
              % (i, r.get("promise", "?"), "-" if res is None else res,
                 str(r.get("thesis", ""))[:88]))


# ---------------------------------------------------------------------------
# Stage 1 — devise
# ---------------------------------------------------------------------------

def _context_block(t):
    """What the deviser sees besides the thesis.

    Sketch and target come from the GENERATOR, before any attack, so they
    carry no defensive residue. `risk` is excluded on purpose: it is a
    pre-emptive worry, and seeding the outline with worries is how you get a
    defensive structure by another route.
    """
    bits = []
    if t.get("move_type"):
        bits.append("The move this thesis makes: %s." % t["move_type"])
    if t.get("target"):
        bits.append("Whose view or which shared assumption it is aimed at:\n%s"
                    % t["target"])
    if t.get("sketch"):
        bits.append("A first sketch of how the argument might go (you are "
                    "NOT obliged to follow it — it is one route, and finding "
                    "a better one is part of your job):\n%s" % t["sketch"])
    return "\n\n".join(bits)


def devise_one(client, thesis_obj, i):
    txt = client.ask(
        DEVISER_SYSTEM,
        [{"role": "user",
          "content": DEVISER_USER.format(thesis=thesis_obj["thesis"],
                                         context=_context_block(thesis_obj))}],
        temperature=1.0,
    )
    o = extract_json(txt)
    if not isinstance(o, dict):
        return {"outline": i, "error": "unparseable", "raw_text": txt[:4000]}
    o["outline"] = i
    return o


def devise(client, thesis_obj, n):
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(devise_one, client, thesis_obj, i): i
                for i in range(n)}
        for f in as_completed(futs):
            try:
                out.append(f.result())
            except Exception as e:
                print("      outline failed: %s" % e, file=sys.stderr)
    out.sort(key=lambda o: o.get("outline", 0))
    return out


# ---------------------------------------------------------------------------
# Stage 2 — audit. No API calls; coherence is COMPUTED from the ledger.
# ---------------------------------------------------------------------------

def _norm(s):
    """Normalise for the verbatim check.

    Whitespace, case and a terminal full stop only. Anything more forgiving
    would let paraphrase through, which is the whole thing this catches.

    One exception: a leading "<Section Title> establishes: " prefix is
    stripped. Models sometimes label the quotation instead of altering it,
    and that is a citation habit rather than the claim drifting — flagging
    it as DRIFT buries the real cases.
    """
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    s = re.sub(r"^[^:]{0,120}?\bestablish(?:es|ed)\s*:\s*", "", s,
               flags=re.IGNORECASE)
    return s.strip().lower().rstrip(".").strip()


def _role(s):
    r = str((s or {}).get("role") or "").strip().lower()
    if r.startswith("intro"):
        return "intro"
    if r.startswith("conc"):
        return "conclusion"
    return "substantive"


def _sim(a, b):
    return difflib.SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def _secnum(v):
    m = re.search(r"\d+", str(v or ""))
    return int(m.group()) if m else None


def audit(o):
    """Read coherence off the dependency ledger.

    Everything here is mechanical. Nothing asks a model whether the outline
    hangs together; the ledger either closes or it does not.
    """
    flags = []
    def flag(level, code, text):
        flags.append({"level": level, "code": code, "text": text})

    if o.get("error"):
        flag("bad", "UNPARSEABLE", "the model did not return usable JSON")
        return {"flags": flags, "edges": [], "inbound": {}}

    secs = [s for s in (o.get("sections") or []) if isinstance(s, dict)]
    by_n = {}
    for idx, s in enumerate(secs):
        n = _secnum(s.get("n"))
        by_n[n if n is not None else idx + 1] = s

    edges = []            # (from_section, to_section)
    inbound = {}          # section number -> how many later sections use it
    assumed = []

    roles = {n: _role(s) for n, s in by_n.items()}
    arg = [n for n in by_n if roles[n] == "substantive"]
    # Roles are a newer field; on a run that predates them every section
    # reads as substantive and the frame checks stay quiet rather than
    # flagging every old outline.
    has_roles = any(str(s.get("role") or "").strip() for s in by_n.values())
    if has_roles:
        for want, label in (("intro", "NO INTRO"),
                            ("conclusion", "NO CONCLUSION")):
            if sum(1 for r in roles.values() if r == want) != 1:
                flag("bad", label,
                     "expected exactly one section with role %r" % want)

    for n, s in sorted(by_n.items()):
        if roles[n] != "substantive":
            continue
        if not str(s.get("address") or "").strip():
            flag("bad", "NO ADDRESS",
                 "§%s names no position that would refute it" % n)
        for dep in (s.get("takes_as_given") or []):
            if not isinstance(dep, dict):
                continue
            src = str(dep.get("from") or "").strip()
            claim = dep.get("claim") or ""
            if src.lower().startswith("assum") or not _secnum(src):
                assumed.append((n, claim))
                continue
            m = _secnum(src)
            if m not in by_n:
                flag("bad", "BROKEN REF",
                     "§%s takes a claim from §%s, which does not exist" % (n, m))
                continue
            if m >= n:
                flag("bad", "FORWARD REF",
                     "§%s takes a claim from §%s, which comes later" % (n, m))
                continue
            edges.append((m, n))
            inbound[m] = inbound.get(m, 0) + 1
            src_claim = by_n[m].get("establishes") or ""
            if _norm(claim) != _norm(src_claim):
                r = _sim(claim, src_claim)
                if r >= 0.55:
                    flag("bad", "DRIFT",
                         "§%s quotes §%s inexactly (%.0f%% match) — the claim "
                         "moved in transit.\n  §%s establishes: %s\n  §%s "
                         "receives: %s" % (n, m, 100 * r, m, src_claim, n, claim))
                else:
                    flag("bad", "MISMATCH",
                         "§%s cites §%s but the claim is a different one "
                         "(%.0f%% match)" % (n, m, 100 * r))

    arrives = _secnum(o.get("arrives_at"))
    if arrives is not None and roles.get(arrives) in ("intro", "conclusion"):
        flag("bad", "ARRIVES IN FRAME",
             "arrives_at names §%s, which is the %s — the argument has to "
             "land in a substantive section" % (arrives, roles[arrives]))

    # orphans: established but never consumed, and not the arrival section
    for n in sorted(arg):
        if inbound.get(n, 0) == 0 and n != arrives:
            flag("warn", "ORPHAN",
                 "§%s establishes something no later section takes up" % n)

    if not edges:
        flag("bad", "NO EDGES",
             "no section takes anything from any other — this is a list, "
             "not an argument")

    # arrival: reachable, and actually downstream of something
    if arrives is None:
        flag("bad", "NO ARRIVAL", "the outline does not say where it arrives")
    elif arrives not in by_n:
        flag("bad", "NO ARRIVAL", "arrives_at names §%s, which does not exist"
             % arrives)
    else:
        feeders = [a for a, b in edges if b == arrives]
        if not feeders:
            flag("bad", "UNSUPPORTED ARRIVAL",
                 "§%s is said to arrive at the thesis but takes nothing from "
                 "any earlier section" % arrives)
        else:
            # walk back to see how much of the paper actually feeds it
            seen, stack = set(), list(feeders)
            while stack:
                x = stack.pop()
                if x in seen:
                    continue
                seen.add(x)
                stack.extend(a for a, b in edges if b == x)
            if len(seen) < max(1, len(arg) - 2):
                flag("warn", "THIN PATH",
                     "only %d of %d substantive sections feed the arrival "
                     "at §%s" % (len(seen), len(arg), arrives))

    # weight: declared load-bearing claim vs. the one most sections depend on.
    # Only meaningful once something is depended on TWICE — with every
    # section feeding exactly one successor there is no heaviest, just a
    # chain, and max() would pick a winner out of a tie.
    heaviest = max(inbound, key=lambda k: inbound[k]) if inbound else None
    if heaviest is not None and inbound[heaviest] >= 2:
        declared = o.get("load_bearing") or ""
        best_n, best_r = None, 0.0
        for n in arg:
            r = _sim(declared, by_n[n].get("establishes"))
            if r > best_r:
                best_n, best_r = n, r
        if (best_n is not None and best_r > 0.55
                and inbound.get(best_n, 0) < inbound[heaviest]):
            flag("warn", "WEIGHT MISMATCH",
                 "declared load-bearing claim is §%s (%d sections depend on "
                 "it), but §%s is what the most sections (%d) depend on"
                 % (best_n, inbound.get(best_n, 0), heaviest,
                    inbound[heaviest]))
        h = by_n[heaviest]
        lens = sorted(len(str(by_n[n].get("establishes", "")) +
                          str(by_n[n].get("refuted_by", ""))) for n in arg)
        if len(str(h.get("establishes", "")) +
               str(h.get("refuted_by", ""))) <= lens[max(0, len(lens) // 4)]:
            flag("warn", "THIN LOAD BEARER",
                 "§%s carries the most weight and is among the least "
                 "developed sections" % heaviest)

    if not (o.get("gap") or {}).get("statement"):
        flag("bad", "NO GAP", "the outline reports no gap — it has not looked")

    for n, claim in assumed:
        flag("info", "ASSUMED",
             "§%s takes as given, defended nowhere: %s" % (n, claim))

    if str(o.get("structure", "")).lower() == "deviant":
        flag("info", "DEVIANT STRUCTURE",
             o.get("structure_note") or "departs from standard shape")

    return {"flags": flags, "edges": edges, "inbound": inbound,
            "n_substantive": len(arg), "n_sections": len(by_n)}


def audit_all(outlines):
    for o in outlines:
        o["audit"] = audit(o)
    return outlines


def addresses(outlines):
    """Every named position, in one list, deduplicated.

    Requirement 1 asks the model to name real positions held by real people.
    That is exactly the operation that produced the Carruthers error in the
    Forge — confidently, and with nothing downstream able to catch it. No
    machine here can check these. Collecting them into one short list makes
    them checkable by the one reader who can settle them in seconds.
    """
    seen = {}
    for o in outlines:
        for s in (o.get("sections") or []):
            if not isinstance(s, dict):
                continue
            a = str(s.get("address") or "").strip()
            if not a:
                continue
            k = _norm(a)[:120]
            seen.setdefault(k, {"text": a, "where": []})
            seen[k]["where"].append("O%s§%s" % (o.get("outline"), s.get("n")))
    return sorted(seen.values(), key=lambda x: x["text"].lower())


# ---------------------------------------------------------------------------
# Stage 3 — diverge
# ---------------------------------------------------------------------------

def diverge(client, outlines, thesis):
    payload = []
    for o in outlines:
        if o.get("error"):
            continue
        payload.append({
            "outline": o.get("outline"),
            "title": o.get("title"),
            "shape": o.get("shape"),
            "sections": [{"n": s.get("n"), "establishes": s.get("establishes")}
                         for s in (o.get("sections") or [])
                         if isinstance(s, dict)],
            "arrives_at": o.get("arrives_at"),
            "load_bearing": o.get("load_bearing"),
        })
    if len(payload) < 2:
        return None
    txt = client.ask(
        DIVERGE_SYSTEM,
        [{"role": "user",
          "content": "THESIS:\n%s\n\nOUTLINES:\n%s"
                     % (thesis, json.dumps(payload, indent=2))}],
        temperature=0.3,
        max_tokens=3000,
    )
    d = extract_json(txt)
    return d if isinstance(d, dict) else None


# ---------------------------------------------------------------------------
# Stage 4 — report
# ---------------------------------------------------------------------------

HEADNOTE = (
    "Nothing here is ranked and nothing is scored. The outlines were written "
    "blind to each other, and the flags below each one are computed from its "
    "own dependency ledger — no model judged coherence. Read the outlines "
    "first; the divergence section at the end is only useful once you have.")


def _cell(s, n=90):
    s = ("" if s is None else str(s)).replace("|", "\\|").replace("\n", " ")
    return s[:n] + ("…" if len(s) > n else "")


def report(state, path):
    o_all = state["outlines"]
    L = []
    w = L.append
    w("# Outlines — %s\n" % state.get("title_line", ""))
    w("**Thesis (fixed):** %s\n" % state["thesis"])
    if state.get("headline") and state.get("used_surviving"):
        w("*Built on the post-kill restatement. The headline thesis was:* %s\n"
          % state["headline"])
    w(HEADNOTE + "\n")

    addr = state.get("addresses") or []
    if addr:
        w("\n## Addresses to check\n")
        w("Every position the outlines name as a refuter. Nothing in this "
          "pipeline can verify that these people hold these views; this is "
          "the list to run your eye down first.\n")
        w("| Where | Position |")
        w("|---|---|")
        for a in addr:
            w("| %s | %s |" % (", ".join(a["where"]), _cell(a["text"], 200)))
        w("")

    for o in o_all:
        n = o.get("outline")
        if o.get("error"):
            w("\n## Outline %s — FAILED\n" % n)
            w("`%s`\n" % o.get("error"))
            continue
        w("\n## Outline %s — %s\n" % (n, o.get("title") or "untitled"))
        w("*%s*\n" % (o.get("shape") or ""))
        w("- **Surprise.** %s" % (o.get("surprise") or "—"))
        w("- **Commitment.** %s" % (o.get("commitment") or "—"))
        g = o.get("gap") or {}
        w("- **Gap.** §%s, %s: %s"
          % (g.get("section"), g.get("inference"), g.get("statement")))
        w("- **Arrives at.** §%s" % o.get("arrives_at"))
        w("- **Load-bearing.** %s" % (o.get("load_bearing") or "—"))
        au = o.get("audit") or {}
        if au.get("n_substantive") is not None:
            w("- **Shape.** %s substantive sections, plus frame\n"
              % au["n_substantive"])
        else:
            w("")

        w("| § | Establishes | Refuted by / address | Takes as given |")
        w("|---|---|---|---|")
        for s in (o.get("sections") or []):
            if not isinstance(s, dict):
                continue
            if _role(s) != "substantive":
                # Frame sections establish nothing and carry no ledger; render
                # them as the frame rather than as empty argument rows.
                w("| %s | *%s* | — | — |"
                  % (s.get("n"), s.get("heading") or _role(s)))
                continue
            deps = "; ".join(
                "§%s" % d.get("from") if _secnum(d.get("from"))
                else "assumed: %s" % _cell(d.get("claim"), 60)
                for d in (s.get("takes_as_given") or [])
                if isinstance(d, dict)) or "—"
            w("| %s | %s | %s<br>*%s* | %s |"
              % (s.get("n"), _cell(s.get("establishes"), 160),
                 _cell(s.get("refuted_by"), 110), _cell(s.get("address"), 110),
                 deps))
        w("")

        fl = (o.get("audit") or {}).get("flags") or []
        if fl:
            w("**Audit**\n")
            for f in fl:
                mark = {"bad": "✗", "warn": "!", "info": "·"}.get(f["level"], "·")
                w("- %s **%s** — %s" % (mark, f["code"], f["text"]))
            w("")

    d = state.get("divergence")
    if d:
        w("\n## Divergence\n")
        w("**Forced** — every outline does this, so the thesis requires it:\n")
        for x in (d.get("forced") or []):
            w("- %s" % x)
        w("\n**Free** — the outlines split, so this is yours to choose:\n")
        for x in (d.get("free") or []):
            if isinstance(x, dict):
                w("- **%s** — %s *(%s)*"
                  % (x.get("move"), "; ".join(x.get("options") or []),
                     x.get("outlines")))
        if d.get("sharpest"):
            w("\n**Sharpest disagreement.** %s" % d["sharpest"])
        if d.get("absent"):
            w("\n**Absent from all of them.** %s" % d["absent"])

    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


CSS = """
:root { --bg:#fbfaf8; --fg:#1c1b19; --mut:#6b6862; --line:#e0ddd6;
        --card:#fff; --warn:#8a5a00; --warnbg:#fdf6e3; --bad:#9b2c2c;
        --badbg:#fdf0ef; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#161513; --fg:#eceae6; --mut:#9a968e; --line:#302e2a;
          --card:#1e1d1a; --warn:#e0b458; --warnbg:#2a2317; --bad:#e08c86;
          --badbg:#2b1a19; } }
* { box-sizing:border-box }
body { margin:0; padding:2.5rem 1.25rem 6rem; background:var(--bg);
       color:var(--fg); font:16px/1.65 -apple-system,BlinkMacSystemFont,
       "Segoe UI",Helvetica,sans-serif; }
main { max-width:58rem; margin:0 auto }
h1 { font-size:1.5rem; line-height:1.3; margin:0 0 .5rem }
h2 { font-size:1.05rem; text-transform:uppercase; letter-spacing:.08em;
     color:var(--mut); margin:3rem 0 1rem;
     border-bottom:1px solid var(--line); padding-bottom:.4rem }
h3 { font-size:1.12rem; line-height:1.4; margin:0 0 .35rem }
.thesis { background:var(--card); border:1px solid var(--line);
          border-radius:10px; padding:1.1rem 1.3rem; margin:0 0 1.25rem }
.note { color:var(--mut); font-size:.92rem; margin:0 0 2rem }
article { background:var(--card); border:1px solid var(--line);
          border-radius:10px; padding:1.4rem 1.5rem; margin:0 0 1.5rem }
.shape { color:var(--mut); margin:0 0 1rem }
dl { margin:0 0 1.2rem }
dt { color:var(--mut); font-size:.78rem; text-transform:uppercase;
     letter-spacing:.06em; margin-top:.9rem }
dd { margin:.15rem 0 0 }
table { width:100%; border-collapse:collapse; margin:0 0 1rem;
        font-size:.88rem; display:block; overflow-x:auto }
th { text-align:left; color:var(--mut); font-size:.72rem; font-weight:600;
     letter-spacing:.07em; text-transform:uppercase;
     border-bottom:1px solid var(--line); padding:.5rem .6rem }
td { padding:.5rem .6rem; border-bottom:1px solid var(--line);
     vertical-align:top }
td.n { text-align:center; font-variant-numeric:tabular-nums;
       white-space:nowrap; color:var(--mut) }
td .addr { color:var(--mut); font-size:.92em; display:block; margin-top:.25rem }
.flags { margin:0; padding:0; list-style:none; font-size:.92rem }
.flags li { padding:.5rem .8rem; border-radius:6px; margin:.35rem 0;
            white-space:pre-wrap }
.flags li.bad { background:var(--badbg); color:var(--bad) }
.flags li.warn { background:var(--warnbg); color:var(--warn) }
.flags li.info { color:var(--mut) }
.flags code { font-weight:700; letter-spacing:.04em }
.fail { color:var(--bad) }
"""


def _esc(s):
    # `str(s or "")` would swallow 0 — outline 0 rendered as "Outline —".
    return html.escape("" if s is None else str(s))


def html_report(state, path):
    P = []
    w = P.append
    w("<!doctype html><meta charset=utf-8>")
    w("<meta name=viewport content='width=device-width,initial-scale=1'>")
    w("<title>Outlines — %s</title>" % _esc(state.get("title_line", "")))
    w("<style>%s</style><main>" % CSS)
    w("<h1>Outlines</h1>")
    w("<div class=thesis><strong>Thesis (fixed)</strong><br>%s</div>"
      % _esc(state["thesis"]))
    if state.get("headline") and state.get("used_surviving"):
        w("<p class=note>Built on the post-kill restatement. The headline "
          "thesis was: %s</p>" % _esc(state["headline"]))
    w("<p class=note>%s</p>" % _esc(HEADNOTE))

    addr = state.get("addresses") or []
    if addr:
        w("<h2>Addresses to check</h2>")
        w("<p class=note>Every position the outlines name as a refuter. "
          "Nothing in this pipeline can verify that these people hold these "
          "views.</p>")
        w("<table><tr><th>Where</th><th>Position</th></tr>")
        for a in addr:
            w("<tr><td class=n>%s</td><td>%s</td></tr>"
              % (_esc(", ".join(a["where"])), _esc(a["text"])))
        w("</table>")

    for o in state["outlines"]:
        n = o.get("outline")
        if o.get("error"):
            w("<article><h3 class=fail>Outline %s — failed</h3>"
              "<p class=note>%s</p></article>" % (_esc(n), _esc(o.get("error"))))
            continue
        w("<article>")
        w("<h3>Outline %s — %s</h3>" % (_esc(n), _esc(o.get("title"))))
        w("<p class=shape>%s</p>" % _esc(o.get("shape")))
        g = o.get("gap") or {}
        w("<dl>")
        w("<dt>Surprise</dt><dd>%s</dd>" % _esc(o.get("surprise")))
        w("<dt>Commitment</dt><dd>%s</dd>" % _esc(o.get("commitment")))
        w("<dt>Gap</dt><dd>§%s, %s — %s</dd>"
          % (_esc(g.get("section")), _esc(g.get("inference")),
             _esc(g.get("statement"))))
        w("<dt>Arrives at</dt><dd>§%s</dd>" % _esc(o.get("arrives_at")))
        w("<dt>Load-bearing</dt><dd>%s</dd>" % _esc(o.get("load_bearing")))
        au = o.get("audit") or {}
        if au.get("n_substantive") is not None:
            w("<dt>Shape</dt><dd>%s substantive sections, plus frame</dd>"
              % _esc(au["n_substantive"]))
        w("</dl>")

        w("<table><tr><th>§</th><th>Establishes</th>"
          "<th>Refuted by / address</th><th>Takes as given</th></tr>")
        for s in (o.get("sections") or []):
            if not isinstance(s, dict):
                continue
            if _role(s) != "substantive":
                w("<tr><td class=n>%s</td><td colspan=3><em>%s</em></td></tr>"
                  % (_esc(s.get("n")), _esc(s.get("heading") or _role(s))))
                continue
            deps = []
            for d in (s.get("takes_as_given") or []):
                if not isinstance(d, dict):
                    continue
                if _secnum(d.get("from")):
                    deps.append("§%s" % _esc(d.get("from")))
                else:
                    deps.append("<em>assumed:</em> %s" % _esc(d.get("claim")))
            w("<tr><td class=n>%s</td><td><strong>%s</strong><br>"
              "<span class=addr>%s</span></td>"
              "<td>%s<span class=addr>%s</span></td><td>%s</td></tr>"
              % (_esc(s.get("n")), _esc(s.get("establishes")),
                 _esc(s.get("work")), _esc(s.get("refuted_by")),
                 _esc(s.get("address")), "<br>".join(deps) or "—"))
        w("</table>")

        fl = (o.get("audit") or {}).get("flags") or []
        if fl:
            w("<ul class=flags>")
            for f in fl:
                w("<li class=%s><code>%s</code> — %s</li>"
                  % (f["level"], _esc(f["code"]), _esc(f["text"])))
            w("</ul>")
        w("</article>")

    d = state.get("divergence")
    if d:
        w("<h2>Divergence</h2>")
        w("<article>")
        w("<dl><dt>Forced — the thesis requires these</dt><dd><ul>")
        for x in (d.get("forced") or []):
            w("<li>%s</li>" % _esc(x))
        w("</ul></dd>")
        w("<dt>Free — yours to choose</dt><dd><ul>")
        for x in (d.get("free") or []):
            if isinstance(x, dict):
                w("<li><strong>%s</strong> — %s <em>(%s)</em></li>"
                  % (_esc(x.get("move")),
                     _esc("; ".join(x.get("options") or [])),
                     _esc(x.get("outlines"))))
        w("</ul></dd>")
        if d.get("sharpest"):
            w("<dt>Sharpest disagreement</dt><dd>%s</dd>" % _esc(d["sharpest"]))
        if d.get("absent"):
            w("<dt>Absent from all of them</dt><dd>%s</dd>" % _esc(d["absent"]))
        w("</dl></article>")

    w("</main>")
    with open(path, "w") as f:
        f.write("\n".join(P) + "\n")


def write_outputs(state, out):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "raw.json"), "w") as f:
        json.dump(state, f, indent=2)
    report(state, os.path.join(out, "outlines.md"))
    html_report(state, os.path.join(out, "outlines.html"))


def rerender(path):
    """Re-run the audit and rebuild the reports. No API calls.

    Same bargain as the Forge's --rerender: the outlines are the data, the
    audit is one reading of them. Change audit() and re-run this.
    """
    out = os.path.dirname(os.path.abspath(path)) or "."
    with open(path) as f:
        state = json.load(f)
    audit_all(state.get("outlines") or [])
    state["addresses"] = addresses(state.get("outlines") or [])
    write_outputs(state, out)
    print("re-audited %d outlines, no API calls" % len(state.get("outlines") or []))
    print("open %s" % os.path.join(out, "outlines.html"))


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", default=None,
                   help="a Forge run's raw.json to take the thesis from")
    p.add_argument("--match", default=None,
                   help="substring of the thesis or sketch to pick it")
    p.add_argument("--index", type=int, default=None,
                   help="pick by index instead (see --list)")
    p.add_argument("--list", action="store_true",
                   help="list the theses in --raw and exit")
    p.add_argument("--thesis", default=None,
                   help="a thesis typed in directly, instead of --raw")
    p.add_argument("--outlines", type=int, default=6)
    p.add_argument("--with-sketch", action="store_true",
                   help="also pass the Forge generator's sketch. OFF by "
                        "default: the sketch carries most of the argument "
                        "already, and outlines built from it converge on it "
                        "— they end up disagreeing about section order "
                        "rather than about the argument.")
    p.add_argument("--no-sketch", action="store_true",
                   help=argparse.SUPPRESS)   # now the default; kept so old
                                             # commands still run
    p.add_argument("--no-diverge", action="store_true",
                   help="skip the divergence pass")
    p.add_argument("--rerender", default=None, metavar="RAW.JSON",
                   help="re-audit and rebuild reports from a previous run; "
                        "makes no API calls")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="outlines1")
    p.add_argument("--dry-run", action="store_true",
                   help="print the call budget and exit")
    args = p.parse_args()

    if args.rerender:
        rerender(args.rerender)
        return

    if args.list:
        if not args.raw:
            sys.exit("--list needs --raw")
        list_theses(args.raw)
        return

    if args.thesis:
        t = {"thesis": args.thesis.strip(), "headline": None,
             "used_surviving": False, "sketch": None, "target": None,
             "move_type": None, "promise": None, "residual": None}
    elif args.raw:
        t = load_thesis(args.raw, args.match, args.index)
    else:
        sys.exit("give --raw (with --match or --index) or --thesis")

    if not args.with_sketch:
        t["sketch"] = None

    if not t["thesis"] or t["thesis"].strip().upper() in (
            "PASTE THE RESTATEMENT", "PASTE YOUR THESIS HERE",
            "PASTE THESIS HERE"):
        sys.exit("that is the placeholder, not a thesis — paste the real one, "
                 "or use --raw with --match to pull it from a Forge run")

    est = args.outlines + (0 if args.no_diverge else 1)
    if args.dry_run:
        print("thesis: %s" % t["thesis"][:120])
        if t["used_surviving"]:
            print("  (post-kill restatement; headline was: %s…)"
                  % (t["headline"] or "")[:80])
        print("%d outlines, isolated, blind to each other." % args.outlines)
        # Costed for THIS stage rather than borrowed from the Forge, whose
        # calls are short exchanges. These are output-heavy: the verbatim
        # ledger makes sections reproduce whole sentences, so output runs
        # about 5x input in spend.
        cost = args.outlines * 0.031 + (0.0 if args.no_diverge else 0.02)
        print("~%d API calls (~$%.2f at Sonnet rates — mostly output "
              "tokens, because the ledger repeats claims verbatim)."
              % (est, cost))
        print("No attack stage, no ranking, no scores. The audit is free.")
        print("Cost is not the constraint here; your reading time is. "
              "Section counts are set by each argument, not by a target.")
        if args.with_sketch:
            print("--with-sketch: outlines will see the Forge sketch and "
                  "will converge toward it.")
        return

    os.makedirs(args.out, exist_ok=True)
    client = Client(args.model)

    print("[1/4] devising — %d isolated outlines…" % args.outlines)
    outlines = devise(client, t, args.outlines)
    ok = [o for o in outlines if not o.get("error")]
    print("      %d of %d usable" % (len(ok), len(outlines)))
    if not ok:
        print("nothing usable; check your key and model id", file=sys.stderr)
        return

    print("[2/4] auditing ledgers (no API calls)…")
    audit_all(outlines)
    for o in ok:
        fl = (o.get("audit") or {}).get("flags") or []
        bad = sum(1 for f in fl if f["level"] == "bad")
        warn = sum(1 for f in fl if f["level"] == "warn")
        print("      O%s  %-46s  %d bad, %d warn"
              % (o.get("outline"), str(o.get("title", ""))[:46], bad, warn))

    d = None
    if args.no_diverge:
        print("[3/4] divergence skipped")
    else:
        print("[3/4] divergence pass…")
        try:
            d = diverge(client, ok, t["thesis"])
        except Exception as e:
            print("      divergence failed: %s" % e, file=sys.stderr)

    print("[4/4] writing report…")
    state = dict(t)
    state["outlines"] = outlines
    state["divergence"] = d
    state["addresses"] = addresses(outlines)
    state["title_line"] = os.path.basename(os.path.abspath(args.out))
    write_outputs(state, args.out)

    print("\n%d API calls. %d addresses to check by eye."
          % (client.calls, len(state["addresses"])))
    print("open %s   <- start here" % os.path.join(args.out, "outlines.html"))


if __name__ == "__main__":
    main()
