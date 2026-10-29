#!/usr/bin/env python3
"""
lit_check.py — the check nothing else in the pipeline performs.

Everything upstream judges theses on their own merits. Nothing looks at what
is already published. That gap cost a thesis: the empirical half had been
established in psychology, and the structural move had been published in
philosophy, and both were findable by ordinary search in minutes.

Two checks, one script. It reads the raw.json and works out which you want.

    NOVELTY      (a Forge raw.json)
                 For each thesis you shortlist: what is already out there,
                 and what does that leave it to contribute. Searches the
                 live web — there is no corpus for you to build.

    ATTRIBUTION  (an Outline Deviser raw.json)
                 Every named position in the addresses table. First
                 mechanically: does the cited work exist at all, checked
                 against OpenAlex. Then, for the ones that do: does that
                 person hold the view ascribed to them.

Neither check can certify novelty. Absence of a search hit is weak evidence
and the reports say so. What this buys is reading time — it turns forty
things you would have to check by eye into three you should read properly.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...

    # confirm the web search tool works on your account before spending
    python3 lit_check.py --probe

    # novelty, on one thesis or on the leaders
    python3 lit_check.py --raw self2/raw.json --match "inverted" --out lit1
    python3 lit_check.py --raw self2/raw.json --top 4 --out lit1

    # attribution, on a Deviser run
    python3 lit_check.py --raw selfo3/raw.json --out lit2

    # rebuild reports, no API calls
    python3 lit_check.py --rerender lit1/raw.json
"""

import argparse, difflib, html, json, os, re, ssl, sys, time
import urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None

MODEL = "claude-sonnet-4-5"
SEARCH_TOOL = "web_search_20250305"


# ---------------------------------------------------------------------------
# Prompts.
# ---------------------------------------------------------------------------

NOVELTY_SYSTEM = """\
You are finding out whether a philosophical thesis has already been argued.

You are NOT evaluating it. Do not say whether it is good, plausible, or
interesting — a separate reader does that and you must not try. One question
only: what is already published that bears on this, and what does that leave
the thesis to contribute?

SEARCH BEFORE YOU ANSWER. Answering from memory is the failure this tool
exists to correct. Every claim you make about the literature must come from
a search result you can cite.

REQUIRED SEARCHES — run at least one for each, and follow trails:

  1. The central claim, in the vocabulary of the field it belongs to.

  2. THE SAME CLAIM IN ADJACENT EMPIRICAL LITERATURE — psychology, cognitive
     science, linguistics, economics, sociology: whatever discipline STUDIES
     the phenomenon rather than theorising about it. Philosophical theses are
     routinely anticipated by empirical researchers who never cite a
     philosopher, and a search that stays inside philosophy will miss them
     completely. A search that never left philosophy is a failed search and
     you should say so rather than report a clean result.

  3. Each named target: does that person actually hold the view ascribed to
     them? Check the actual work, not your memory of it.

  4. The most recent synthesis, survey, or reference-work entry on the topic.
     A paper that maps or reconciles the existing positions is where an
     unnoticed anticipation most often hides, because it names moves nobody
     else bothered to name.

Distinguish four relations, because they call for different responses:

  ANTICIPATED  — someone already argued this, or argued something that
                 entails it. The contribution has to move somewhere else.
  CONTRADICTED — evidence or argument tells against the thesis as stated.
                 It has to narrow, or fight.
  SUPPORTED    — work the thesis can use as its evidence base rather than
                 treat as a rival.
  ADJACENT     — close enough that a referee will raise it, not close enough
                 to do damage.

Then say what is LEFT. If parts are anticipated or contradicted, the useful
output is the narrower claim that survives — write it out as a sentence, the
way a good referee would.

Two rules you must not break:

  Report only what you found and can cite. No source, no claim.

  You CANNOT establish that a thesis is novel. Absence of a search hit is
  weak evidence about a large literature, much of which is paywalled and
  invisible to you. Never present a clean result as originality; say what
  you searched for and did not find, so the reader can judge the silence.
"""

NOVELTY_USER = """\
THESIS:
{thesis}

{extra}

Return ONLY JSON:

{{
  "searched": ["the queries you actually ran, verbatim"],
  "left_philosophy": true | false,
  "findings": [
    {{"relation": "ANTICIPATED" | "CONTRADICTED" | "SUPPORTED" | "ADJACENT",
      "part": "which part of the thesis this touches",
      "source": "Author, \\"Title\\", Venue, Year",
      "url": "the URL you found it at, or null",
      "what_they_say": "one or two sentences, from the source not memory",
      "damage": 1-5,
      "note": "one clause: why this relation and not another"}}
  ],
  "what_is_left": "the narrower claim that survives, written as a sentence a \
referee would accept — or null if nothing was anticipated or contradicted",
  "not_found": "what you searched for and did NOT find. Be specific; this is \
what makes a clean result readable."
}}

"damage" is how much this finding costs the thesis:
  5 the thesis cannot stand as stated   4 a major part must go
  3 a real problem, repairable          2 a referee will mention it
  1 worth a footnote
SUPPORTED findings take damage 1.
"""

ATTRIB_SYSTEM = """\
You are checking one attribution: someone has been said to hold a view, and
you are finding out whether they do.

This is the error class this check exists for. A thesis was once aimed at
"interpretivists like Carruthers who endorse thoroughgoing interpretivism
about all mental states" — but Carruthers' interpretive sensory-access theory
says the opposite: attitudes are interpreted, sensory states are not. The
thesis was aimed at nobody, and nothing in the pipeline noticed.

SEARCH. Do not answer from memory, and do not reason from the plausibility
of the ascription. Find what the person actually wrote.

Return ONLY JSON:

{
  "verdict": "HOLDS" | "DOES NOT HOLD" | "DISTORTED" | "CANNOT TELL",
  "confidence": 1-5,
  "what_they_actually_hold": "one or two sentences, from a source",
  "source": "what you are relying on",
  "url": "URL or null",
  "note": "one clause: if DISTORTED, what specifically is off"
}

DISTORTED is for the common and dangerous case: the person is in the right
neighbourhood, holds something adjacent, but not the view ascribed. That is
worse than a plain error because it survives casual checking.

CANNOT TELL is a real answer. Use it rather than guessing, and say in "note"
what you could not reach.
"""

ATTRIB_USER = """\
THE ATTRIBUTION, as written:
{address}

{ctx}

Does the named person hold the view ascribed to them here?
"""

SEP_PICK_SYSTEM = """\
You are choosing which Stanford Encyclopedia of Philosophy entries to read
against a set of theses. Choose from the candidate list you are given and
nowhere else — every entry you name must appear in that list verbatim.

Pick the ONE to THREE entries whose subject matter would actually contain
the positions these theses engage. Prefer the entry on the DEBATE over the
entry on a philosopher, and prefer a narrower entry to a broad survey when
both apply. Two entries is usually right: the debate itself, and the
neighbouring debate a referee would say the thesis really belongs to.

Return ONLY JSON: {"slugs": ["slug-one", "slug-two"], "why": "one sentence"}
"""

SEP_SYSTEM = """\
You are reading a Stanford Encyclopedia of Philosophy entry — the full text
is below — and checking a set of theses against it.

Why this source and not a search: the entry is the field's own map. It is
written to name the positions in a debate and say who holds them. So if a
position exists in the literature and has a name, it is probably in here.
That makes the entry's SILENCE informative in a way an empty web search is
not — still not proof, but the strongest negative evidence available to you.

Report only what THIS ENTRY says. Not what you recall, not what you would
expect an entry to say. Quote it.

For each thesis, use the same four relations:
  ANTICIPATED  — the entry describes a position that already makes this move
  CONTRADICTED — the entry reports argument or evidence against it
  SUPPORTED    — the entry supplies something the thesis can build on
  ADJACENT     — a near neighbour a referee would raise

And name the NEAREST POSITIONS: the two or three views in the entry the
thesis will have to be situated against, with who holds them. These are
what a paper cites in its opening pages, and getting them from the entry
rather than from memory is the point of this pass.

Return ONLY JSON:

{
  "per_thesis": [
    {"i": 0,
     "findings": [
       {"relation": "ANTICIPATED" | "CONTRADICTED" | "SUPPORTED" | "ADJACENT",
        "position": "the position, as the entry describes it",
        "who": "who the entry says holds it",
        "quote": "a short quotation from the entry",
        "damage": 1-5,
        "note": "one clause"}
     ],
     "nearest_positions": ["view — who holds it", "..."],
     "entry_silent_on": "what this thesis claims that the entry does NOT \
discuss anywhere — the informative silence, or null if none"}
  ]
}
"""


# ---------------------------------------------------------------------------
# Infrastructure — parallel to thesis_forge.py and outline_deviser.py
# ---------------------------------------------------------------------------

def extract_json(text):
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
    """As in the Forge, plus server-side web search.

    The search tool runs inside the API: Claude decides when to search, the
    API performs the search and loops as needed, and the whole exchange comes
    back in one response. There is no tool-handling loop to write here.
    """

    def __init__(self, model, max_tokens=4096):
        if Anthropic is None:
            sys.exit("the anthropic package is not installed: "
                     "python3 -m pip install --upgrade anthropic")
        self.c = Anthropic()
        self.model = model
        self.max_tokens = max_tokens
        self.calls = 0
        self.searches = 0

    def ask(self, system, messages, temperature=0.2, max_tokens=None,
            search=False, max_uses=8):
        self.calls += 1
        kw = {}
        if search:
            kw["tools"] = [{"type": SEARCH_TOOL, "name": "web_search",
                            "max_uses": max_uses}]
        for attempt in range(3):
            try:
                r = self.c.messages.create(
                    model=self.model,
                    max_tokens=max_tokens or self.max_tokens,
                    temperature=temperature,
                    system=system,
                    messages=messages,
                    **kw
                )
                return self._unpack(r)
            except Exception as e:
                msg = str(e)
                if search and attempt == 0 and _looks_like_tool_unsupported(msg):
                    # Fail loudly rather than silently answering from memory,
                    # which is the exact failure this tool exists to prevent.
                    raise RuntimeError(
                        "the web search tool was rejected by the API (%s).\n"
                        "Try:  python3 -m pip install --upgrade anthropic\n"
                        "then: python3 lit_check.py --probe" % msg[:200])
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)

    def _unpack(self, r):
        """Pull out the text and whatever citations came back with it."""
        parts, cites = [], []
        for b in getattr(r, "content", []) or []:
            btype = getattr(b, "type", None)
            if btype == "text":
                parts.append(getattr(b, "text", "") or "")
                for c in (getattr(b, "citations", None) or []):
                    url = getattr(c, "url", None)
                    if not url:
                        continue
                    cites.append({"url": url,
                                  "title": getattr(c, "title", None),
                                  "cited_text": getattr(c, "cited_text", None)})
            elif btype == "server_tool_use":
                self.searches += 1
        # de-duplicate, keeping order
        seen, uniq = set(), []
        for c in cites:
            if c["url"] in seen:
                continue
            seen.add(c["url"])
            uniq.append(c)
        return "".join(parts), uniq


def _looks_like_tool_unsupported(msg):
    m = msg.lower()
    return any(s in m for s in ("web_search", "unexpected keyword", "tools",
                                "not supported", "unknown tool",
                                "invalid_request"))


# ---------------------------------------------------------------------------
# OpenAlex — the mechanical half of the attribution check.
# ---------------------------------------------------------------------------

_OA = "https://api.openalex.org/works"

# An opening quote must follow the start of the string or a space/bracket, and
# the closing quote must be followed by space, punctuation or the end. Without
# both constraints a possessive apostrophe opens a quotation: "David Chalmers'
# view in 'The Contents of Consciousness'" yields the title "view in".
_TITLE_RE = re.compile(
    r"(?:^|(?<=[\s(\[]))"
    r"['\u2018\u201c\"]"
    r"([^'\u2018\u2019\u201c\u201d\"]{6,120}?)"
    r"['\u2019\u201d\"]"
    r"(?=[\s,.;:)\]]|$)",
    re.M)


def cited_titles(text):
    """Pull candidate work titles out of an address written in prose.

    Only quoted strings. A conservative rule that misses some real titles is
    the right trade: a missed title costs nothing, while a false one sends
    the reader chasing a work that was never claimed.
    """
    out = []
    for m in _TITLE_RE.finditer(str(text or "")):
        t = m.group(1).strip().rstrip(",;:")
        if len(t.split()) >= 2:
            out.append(t)
    seen, uniq = set(), []
    for t in out:
        k = t.lower()
        if k not in seen:
            seen.add(k)
            uniq.append(t)
    return uniq


def _ssl_context():
    """A CA bundle, because macOS Python does not come with one wired up.

    A stock python.org install does not use the system keychain, so HTTPS to
    anything outside the Anthropic SDK dies with CERTIFICATE_VERIFY_FAILED.
    certifi ships as a dependency of that SDK, so it is already installed;
    using its bundle here avoids making anyone run Install Certificates.command.
    """
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return None


_CTX = _ssl_context()


def openalex_lookup(title, timeout=20):
    """Does a work by this title exist? No API key, no account, free.

    This is the check that catches an invented citation, and it needs no
    model at all: the title either resolves to a bibliographic record or it
    does not.
    """
    q = urllib.parse.urlencode({"search": title, "per-page": "3"})
    req = urllib.request.Request(
        "%s?%s" % (_OA, q),
        headers={"User-Agent": "lit_check.py (philosophy pipeline)",
                 "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as fh:
            data = json.loads(fh.read().decode("utf-8", "replace"))
    except Exception as e:
        return {"title": title, "status": "LOOKUP FAILED", "error": str(e)[:160]}

    best, best_r = None, 0.0
    for w in (data.get("results") or []):
        cand = str(w.get("display_name") or "")
        r = difflib.SequenceMatcher(
            None, _norm(title), _norm(cand)).ratio()
        if r > best_r:
            best, best_r = w, r

    if best is None or best_r < 0.72:
        return {"title": title, "status": "NOT FOUND",
                "nearest": (best or {}).get("display_name"),
                "ratio": round(best_r, 2)}

    auths = [ (a.get("author") or {}).get("display_name")
              for a in (best.get("authorships") or [])[:4] ]
    return {"title": title, "status": "FOUND",
            "matched": best.get("display_name"),
            "year": best.get("publication_year"),
            "authors": [a for a in auths if a],
            "url": best.get("doi") or best.get("id"),
            "ratio": round(best_r, 2)}


def _norm(s):
    s = re.sub(r"\s+", " ", str(s or "")).strip().lower()
    return re.sub(r"[^a-z0-9 ]", "", s)


# ---------------------------------------------------------------------------
# The SEP pass.
#
# The encyclopedia is the highest-recall source available and the only
# authoritative one that is never paywalled. It is also the field's own map:
# an entry is written to name the positions in a debate and say who holds
# them, so an entry that does NOT contain your move is real evidence, in a
# way that an empty web search is not.
#
# Entries are chosen from SEP's own contents index rather than by asking a
# model for a URL. A shortlist is built mechanically and the model picks from
# it, so a hallucinated entry is not a possible output.
# ---------------------------------------------------------------------------

_SEP = "https://plato.stanford.edu"
_ENTRY_RE = re.compile(
    r'href="(?:https?://plato\.stanford\.edu)?/?entries/([a-z0-9][a-z0-9-]*)/?"'
    r'[^>]*>(.*?)</a>', re.I | re.S)


def _detag(h):
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    return re.sub(r"[ \t\xa0]+", " ", re.sub(r"\n\s*\n+", "\n\n", h)).strip()


def _get(url, timeout=45):
    req = urllib.request.Request(
        url, headers={"User-Agent": "lit_check.py (philosophy pipeline)"})
    with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as fh:
        return fh.read().decode("utf-8", "replace")


def sep_index():
    """(title, slug) for every entry, from SEP's own contents page."""
    out, seen = [], set()
    for m in _ENTRY_RE.finditer(_get(_SEP + "/contents.html")):
        slug = m.group(1).lower()
        title = re.sub(r"\s+", " ", _detag(m.group(2))).strip()
        if slug in seen or not title or len(title) > 160:
            continue
        seen.add(slug)
        out.append((title, slug))
    return out


# No keyword shortlist. An obvious one fails on exactly the case that
# matters: a thesis about privileged access to standing attitudes shares no
# vocabulary with the title "Self-Knowledge", so word overlap scores it zero
# and drops the one entry worth reading. The whole index is ~18k tokens —
# about five cents — so the model reads every title and the failure mode
# does not exist.


def sep_entry_text(slug, cap=120000):
    raw = _get("%s/entries/%s/" % (_SEP, slug))
    txt = _detag(raw)
    i = txt.find("Bibliography")
    if i > 4000:            # drop the bibliography; it is not argument
        txt = txt[:i]
    return txt[:cap], len(txt) > cap


def sep_pick(client, targets, index):
    if not index:
        return [], "the SEP contents index came back empty"
    blob = "\n\n".join(
        "\n".join(x for x in (t["thesis"], t.get("target"), t.get("sketch")) if x)
        for t in targets)
    listing = "\n".join("%s  [%s]" % (t, s) for t, s in index)
    txt, _ = client.ask(
        SEP_PICK_SYSTEM,
        [{"role": "user",
          "content": "THESES:\n%s\n\nEVERY SEP ENTRY:\n%s" % (blob, listing)}],
        max_tokens=600)
    got = extract_json(txt) or {}
    valid = {s for _, s in index}
    # The slug is checked against the real index, so a hallucinated entry
    # cannot survive into a fetch.
    slugs = [s for s in (got.get("slugs") or []) if s in valid][:3]
    return slugs, got.get("why")


def sep_check(client, targets, slug):
    text, truncated = sep_entry_text(slug)
    listing = "\n\n".join("THESIS %d:\n%s" % (i, t["thesis"])
                          for i, t in enumerate(targets))
    txt, _ = client.ask(
        SEP_SYSTEM,
        [{"role": "user",
          "content": "SEP ENTRY (%s):\n%s\n\n=== END OF ENTRY ===\n\n%s"
                     % (slug, text, listing)}],
        # One call covers every thesis, so the ceiling has to grow with them
        # or the JSON truncates and the whole entry pass is lost.
        max_tokens=min(12000, 1500 + 500 * len(targets)))
    got = extract_json(txt) or {"error": "unparseable"}
    got["slug"] = slug
    got["url"] = "%s/entries/%s/" % (_SEP, slug)
    got["truncated"] = truncated
    return got


# ---------------------------------------------------------------------------
# Which check? Work it out from the file.
# ---------------------------------------------------------------------------

def load_any(path):
    with open(path) as f:
        data = json.load(f)
    if isinstance(data, list):
        return "forge", data
    if isinstance(data, dict) and "outlines" in data:
        return "deviser", data
    if isinstance(data, dict) and "mode" in data:
        return "lit", data
    sys.exit("%s is neither a Forge nor a Deviser raw.json" % path)


def pick_theses(results, match=None, index=None, top=None):
    def key(x):
        ru = x.get("ruling") or {}
        res = ru.get("residual")
        return (-int(x.get("promise") or 0), 99 if res is None else int(res))

    if index is not None:
        return [results[index]]
    if match:
        needle = match.lower()
        hits = [x for x in results
                if needle in (str(x.get("thesis", "")) + " "
                              + str(x.get("sketch", ""))).lower()]
        if not hits:
            sys.exit("no thesis matching %r" % match)
        return hits[:1]
    n = top or 4
    return sorted(results, key=key)[:n]


def build_target(t):
    """What gets checked is the thesis as it now stands.

    Same choice as the Deviser: the post-kill restatement, not the headline.
    Checking the headline would check a claim nobody is going to defend.
    """
    ru = t.get("ruling") or {}
    surviving = ru.get("surviving_thesis")
    return {
        "thesis": (surviving or t.get("thesis") or "").strip(),
        "headline": (t.get("thesis") or "").strip(),
        "used_surviving": bool(surviving),
        "target": t.get("target"),
        "sketch": t.get("sketch"),
        "promise": t.get("promise"),
        "residual": ru.get("residual"),
    }


# ---------------------------------------------------------------------------
# Check 1 — novelty
# ---------------------------------------------------------------------------

def check_novelty(client, tgt, max_uses):
    extra = []
    if tgt.get("target"):
        extra.append("Named targets (check each of these):\n%s" % tgt["target"])
    if tgt.get("sketch"):
        extra.append("How the argument is meant to go — use this only to work "
                     "out WHERE to search, not as something to evaluate:\n%s"
                     % tgt["sketch"])
    txt, cites = client.ask(
        NOVELTY_SYSTEM,
        [{"role": "user",
          "content": NOVELTY_USER.format(thesis=tgt["thesis"],
                                         extra="\n\n".join(extra))}],
        search=True, max_uses=max_uses, max_tokens=6000)
    out = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:4000]}
    out["citations"] = cites
    return out


# ---------------------------------------------------------------------------
# Check 2 — attribution
# ---------------------------------------------------------------------------

def check_attribution(client, addr, max_uses):
    ctx = "Where it appears in the outlines: %s" % ", ".join(addr.get("where") or [])
    txt, cites = client.ask(
        ATTRIB_SYSTEM,
        [{"role": "user",
          "content": ATTRIB_USER.format(address=addr["text"], ctx=ctx)}],
        search=True, max_uses=max_uses, max_tokens=2000)
    out = extract_json(txt) or {"error": "unparseable", "raw_text": txt[:2000]}
    out["citations"] = cites
    return out


def addresses_from(state):
    addrs = state.get("addresses")
    if addrs:
        return addrs
    seen = {}
    for o in (state.get("outlines") or []):
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
# Reports
# ---------------------------------------------------------------------------

RELATION_ORDER = {"ANTICIPATED": 0, "CONTRADICTED": 1, "ADJACENT": 2,
                  "SUPPORTED": 3}

HEADNOTE_NOVELTY = (
    "This check can show that something HAS been argued. It cannot show that "
    "nothing has. Read `not found` as carefully as the findings — a clean "
    "result means only that these searches came back empty, and much of the "
    "literature is paywalled and invisible to it.")

HEADNOTE_ATTRIB = (
    "Existence is checked mechanically against OpenAlex: a title either "
    "resolves to a real record or it does not, and no model is involved. "
    "Whether the named person holds the ascribed view is a search-and-judge "
    "step, and DISTORTED is the verdict worth reading — the person is in the "
    "right neighbourhood but does not hold the view, which is the error that "
    "survives casual checking.")


def _cell(s, n=110):
    s = ("" if s is None else str(s)).replace("|", "\\|").replace("\n", " ")
    return s[:n] + ("…" if len(s) > n else "")


def _sep_by_thesis(state):
    """The SEP pass reads one entry against all theses at once; the reader
    wants it the other way round, per thesis."""
    out = {}
    for e in ((state.get("sep") or {}).get("entries") or []):
        if e.get("error"):
            continue
        for per in (e.get("per_thesis") or []):
            try:
                i = int(per.get("i"))
            except (TypeError, ValueError):
                continue
            out.setdefault(i, []).append(dict(per, slug=e.get("slug"),
                                              url=e.get("url")))
    return out


def report(state, path):
    L = []
    w = L.append
    if state["mode"] == "novelty":
        w("# Literature check — novelty\n")
        w(HEADNOTE_NOVELTY + "\n")
        sep_by_thesis = _sep_by_thesis(state)
        sep = state.get("sep") or {}
        if sep.get("picked"):
            w("\nStanford Encyclopedia entries read in full: %s"
              % ", ".join("[%s](%s/entries/%s/)" % (s, _SEP, s)
                          for s in sep["picked"]))
            if sep.get("why"):
                w("*%s*" % sep["why"])
            w("")
        for i, r in enumerate(state["results"]):
            t = r["target"]
            w("\n## %s\n" % _cell(t["thesis"], 150))
            if t.get("used_surviving"):
                w("*Checked as the post-kill restatement.*\n")
            f = r.get("finding") or {}
            if f.get("error"):
                w("`%s`\n" % f["error"])
                continue
            hits = sorted((f.get("findings") or []),
                          key=lambda x: (RELATION_ORDER.get(
                              str(x.get("relation")).upper(), 9),
                              -int(x.get("damage") or 0)))
            if hits:
                w("| Relation | Dmg | Source | What they say |")
                w("|---|---|---|---|")
                for h in hits:
                    src = h.get("source") or "—"
                    if h.get("url"):
                        src = "[%s](%s)" % (_cell(src, 70), h["url"])
                    w("| **%s** | %s | %s | %s |"
                      % (h.get("relation"), h.get("damage"), src,
                         _cell(h.get("what_they_say"), 150)))
                w("")
            else:
                w("*No findings returned.*\n")
            if f.get("what_is_left"):
                w("**What is left.** %s\n" % f["what_is_left"])
            if f.get("not_found"):
                w("**Not found.** %s\n" % f["not_found"])
            if f.get("left_philosophy") is False:
                w("> **The search never left philosophy.** The empirical "
                  "literature was not reached, and that is where "
                  "anticipations hide.\n")
            for e in sep_by_thesis.get(i, []):
                w("\n### From the Stanford Encyclopedia — %s\n" % e["slug"])
                for h in e.get("findings") or []:
                    w("- **%s** (%s/5) — %s — *%s*"
                      % (h.get("relation"), h.get("damage"),
                         h.get("position"), h.get("who")))
                    if h.get("quote"):
                        w("  > %s" % _cell(h["quote"], 300))
                if e.get("nearest_positions"):
                    w("\n**Nearest positions.** %s"
                      % "; ".join(e["nearest_positions"]))
                if e.get("entry_silent_on"):
                    w("\n**The entry is silent on.** %s" % e["entry_silent_on"])
                w("")
            if f.get("searched"):
                w("<details><summary>%d searches</summary>\n"
                  % len(f["searched"]))
                for q in f["searched"]:
                    w("- `%s`" % q)
                w("\n</details>\n")
    else:
        w("# Literature check — attribution\n")
        w(HEADNOTE_ATTRIB + "\n")
        w("\n## Citations that do not resolve\n")
        bad = [c for c in state["citations"] if c["status"] == "NOT FOUND"]
        errs = [c for c in state["citations"] if c["status"] == "LOOKUP FAILED"]
        if bad:
            w("| Where | Title as cited | Nearest record |")
            w("|---|---|---|")
            for c in bad:
                w("| %s | %s | %s |"
                  % (", ".join(c.get("where") or []), _cell(c["title"], 80),
                     _cell(c.get("nearest"), 70)))
        else:
            w("*Every quoted title resolved to a real record.*")
        w("")
        if errs:
            # Kept apart deliberately: a network failure must never be read
            # as a fabricated citation.
            w("%d title(s) could not be looked up at all (network or API "
              "error) — these are unchecked, not suspect: %s\n"
              % (len(errs), _cell("; ".join(c["title"] for c in errs), 200)))
        w("\n## Attributions\n")
        rows = sorted(state["results"], key=lambda r: (
            {"DOES NOT HOLD": 0, "DISTORTED": 1, "CANNOT TELL": 2,
             "HOLDS": 3}.get(str((r.get("finding") or {}).get("verdict")), 9)))
        w("| Where | Verdict | Ascribed | What they actually hold |")
        w("|---|---|---|---|")
        for r in rows:
            f = r.get("finding") or {}
            w("| %s | **%s** | %s | %s |"
              % (", ".join(r["address"].get("where") or []),
                 f.get("verdict", "—"),
                 _cell(r["address"]["text"], 90),
                 _cell(f.get("what_they_actually_hold"), 110)))
        w("")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


CSS = """
:root { --bg:#fbfaf8; --fg:#1c1b19; --mut:#6b6862; --line:#e0ddd6;
        --card:#fff; --warn:#8a5a00; --warnbg:#fdf6e3; --bad:#9b2c2c;
        --badbg:#fdf0ef; --ok:#2f6b4f; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#161513; --fg:#eceae6; --mut:#9a968e; --line:#302e2a;
          --card:#1e1d1a; --warn:#e0b458; --warnbg:#2a2317; --bad:#e08c86;
          --badbg:#2b1a19; --ok:#7fb99a; } }
* { box-sizing:border-box }
body { margin:0; padding:2.5rem 1.25rem 6rem; background:var(--bg);
       color:var(--fg); font:16px/1.65 -apple-system,BlinkMacSystemFont,
       "Segoe UI",Helvetica,sans-serif; }
main { max-width:58rem; margin:0 auto }
h1 { font-size:1.5rem; margin:0 0 .5rem }
h2 { font-size:1.05rem; text-transform:uppercase; letter-spacing:.08em;
     color:var(--mut); margin:3rem 0 1rem;
     border-bottom:1px solid var(--line); padding-bottom:.4rem }
h3 { font-size:1.08rem; line-height:1.45; margin:0 0 .5rem }
.note { color:var(--mut); font-size:.92rem; margin:0 0 2rem }
article { background:var(--card); border:1px solid var(--line);
          border-radius:10px; padding:1.4rem 1.5rem; margin:0 0 1.5rem }
table { width:100%; border-collapse:collapse; margin:0 0 1rem;
        font-size:.88rem; display:block; overflow-x:auto }
th { text-align:left; color:var(--mut); font-size:.72rem; font-weight:600;
     letter-spacing:.07em; text-transform:uppercase;
     border-bottom:1px solid var(--line); padding:.5rem .6rem }
td { padding:.5rem .6rem; border-bottom:1px solid var(--line);
     vertical-align:top }
.rel { font-weight:700; white-space:nowrap }
.ANTICIPATED, .DOESNOTHOLD { color:var(--bad) }
.CONTRADICTED, .DISTORTED { color:var(--warn) }
.SUPPORTED, .HOLDS { color:var(--ok) }
.ADJACENT, .CANNOTTELL { color:var(--mut) }
.left { background:var(--warnbg); padding:.9rem 1.1rem; border-radius:8px;
        margin:1rem 0 }
.nf { color:var(--mut); font-size:.93rem; margin:.75rem 0 0 }
.flag { background:var(--badbg); color:var(--bad); padding:.8rem 1rem;
        border-radius:8px; margin:1rem 0; font-size:.93rem }
details { margin-top:1rem; border-top:1px solid var(--line); padding-top:.8rem }
summary { cursor:pointer; color:var(--mut); font-size:.9rem }
code { font-size:.88em }
"""


def _esc(s):
    # `str(s or "")` would swallow 0 — a damage-0 finding printed as "(/5)".
    return html.escape("" if s is None else str(s))


def _cls(s):
    return re.sub(r"[^A-Z]", "", str(s or "").upper())


def html_report(state, path):
    P = []
    w = P.append
    mode = state["mode"]
    w("<!doctype html><meta charset=utf-8>")
    w("<meta name=viewport content='width=device-width,initial-scale=1'>")
    w("<title>Literature check — %s</title>" % _esc(mode))
    w("<style>%s</style><main>" % CSS)
    w("<h1>Literature check — %s</h1>" % _esc(mode))
    w("<p class=note>%s</p>"
      % _esc(HEADNOTE_NOVELTY if mode == "novelty" else HEADNOTE_ATTRIB))

    if mode == "novelty":
        sep_by_thesis = _sep_by_thesis(state)
        sep = state.get("sep") or {}
        if sep.get("picked"):
            w("<p class=note>Stanford Encyclopedia entries read in full: %s"
              % ", ".join("<a href='%s/entries/%s/'>%s</a>" % (_SEP, s, _esc(s))
                          for s in sep["picked"]))
            if sep.get("why"):
                w(" — %s" % _esc(sep["why"]))
            w("</p>")
        for i, r in enumerate(state["results"]):
            t = r["target"]
            f = r.get("finding") or {}
            w("<article>")
            w("<h3>%s</h3>" % _esc(t["thesis"]))
            if t.get("used_surviving"):
                w("<p class=note>Checked as the post-kill restatement.</p>")
            if f.get("error"):
                w("<p class=flag>%s</p></article>" % _esc(f["error"]))
                continue
            if f.get("left_philosophy") is False:
                w("<p class=flag>The search never left philosophy — the "
                  "empirical literature was not reached, and that is where "
                  "anticipations hide.</p>")
            hits = sorted((f.get("findings") or []),
                          key=lambda x: (RELATION_ORDER.get(
                              str(x.get("relation")).upper(), 9),
                              -int(x.get("damage") or 0)))
            if hits:
                w("<table><tr><th>Relation</th><th>Dmg</th><th>Part</th>"
                  "<th>Source</th><th>What they say</th></tr>")
                for h in hits:
                    src = _esc(h.get("source"))
                    if h.get("url"):
                        src = "<a href='%s'>%s</a>" % (_esc(h["url"]), src)
                    w("<tr><td class='rel %s'>%s</td><td>%s</td><td>%s</td>"
                      "<td>%s</td><td>%s</td></tr>"
                      % (_cls(h.get("relation")), _esc(h.get("relation")),
                         _esc(h.get("damage")), _esc(h.get("part")), src,
                         _esc(h.get("what_they_say"))))
                w("</table>")
            if f.get("what_is_left"):
                w("<div class=left><strong>What is left.</strong> %s</div>"
                  % _esc(f["what_is_left"]))
            if f.get("not_found"):
                w("<p class=nf><strong>Not found.</strong> %s</p>"
                  % _esc(f["not_found"]))
            for e in sep_by_thesis.get(i, []):
                w("<h4 style='margin:1.4rem 0 .4rem'>From the Stanford "
                  "Encyclopedia — <a href='%s'>%s</a></h4>"
                  % (_esc(e.get("url")), _esc(e.get("slug"))))
                for h in (e.get("findings") or []):
                    w("<p style='margin:.5rem 0'><span class='rel %s'>%s</span> "
                      "(%s/5) — %s — <em>%s</em></p>"
                      % (_cls(h.get("relation")), _esc(h.get("relation")),
                         _esc(h.get("damage")), _esc(h.get("position")),
                         _esc(h.get("who"))))
                    if h.get("quote"):
                        w("<blockquote class=note style='margin:.2rem 0 .6rem "
                          "1rem'>%s</blockquote>" % _esc(h["quote"]))
                if e.get("nearest_positions"):
                    w("<p class=nf><strong>Nearest positions.</strong> %s</p>"
                      % _esc("; ".join(e["nearest_positions"])))
                if e.get("entry_silent_on"):
                    w("<div class=left><strong>The entry is silent on.</strong> "
                      "%s</div>" % _esc(e["entry_silent_on"]))
            if f.get("searched"):
                w("<details><summary>%d searches</summary><ul>"
                  % len(f["searched"]))
                for q in f["searched"]:
                    w("<li><code>%s</code></li>" % _esc(q))
                w("</ul></details>")
            w("</article>")
    else:
        bad = [c for c in state["citations"] if c["status"] == "NOT FOUND"]
        errs = [c for c in state["citations"] if c["status"] == "LOOKUP FAILED"]
        w("<h2>Citations that do not resolve</h2>")
        w("<article>")
        if bad:
            w("<table><tr><th>Where</th><th>Title as cited</th>"
              "<th>Nearest record</th></tr>")
            for c in bad:
                w("<tr><td>%s</td><td class='rel DOESNOTHOLD'>%s</td>"
                  "<td>%s</td></tr>"
                  % (_esc(", ".join(c.get("where") or [])),
                     _esc(c["title"]), _esc(c.get("nearest"))))
            w("</table>")
        else:
            w("<p class=note>Every quoted title resolved to a real record.</p>")
        if errs:
            w("<p class=nf>%d title(s) could not be looked up at all "
              "(network or API error). These are <em>unchecked, not "
              "suspect</em>: %s</p>"
              % (len(errs), _esc("; ".join(c["title"] for c in errs))))
        w("</article>")

        w("<h2>Attributions</h2><article>")
        rows = sorted(state["results"], key=lambda r: (
            {"DOES NOT HOLD": 0, "DISTORTED": 1, "CANNOT TELL": 2,
             "HOLDS": 3}.get(str((r.get("finding") or {}).get("verdict")), 9)))
        w("<table><tr><th>Where</th><th>Verdict</th><th>Ascribed</th>"
          "<th>What they actually hold</th></tr>")
        for r in rows:
            f = r.get("finding") or {}
            src = _esc(f.get("what_they_actually_hold"))
            if f.get("url"):
                src += " <a href='%s'>(source)</a>" % _esc(f["url"])
            w("<tr><td>%s</td><td class='rel %s'>%s</td><td>%s</td>"
              "<td>%s</td></tr>"
              % (_esc(", ".join(r["address"].get("where") or [])),
                 _cls(f.get("verdict")), _esc(f.get("verdict")),
                 _esc(r["address"]["text"]), src))
        w("</table></article>")

    w("</main>")
    with open(path, "w") as f:
        f.write("\n".join(P) + "\n")


def write_outputs(state, out):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "raw.json"), "w") as f:
        json.dump(state, f, indent=2)
    report(state, os.path.join(out, "lit.md"))
    html_report(state, os.path.join(out, "lit.html"))


def rerender(path):
    out = os.path.dirname(os.path.abspath(path)) or "."
    _, state = load_any(path)
    write_outputs(state, out)
    print("rebuilt, no API calls")
    print("open %s" % os.path.join(out, "lit.html"))


def probe(model):
    """One search, to prove the tool works before anything expensive runs."""
    try:
        import anthropic
        print("anthropic %s" % getattr(anthropic, "__version__", "?"))
    except ImportError:
        sys.exit("the anthropic package is not installed")
    c = Client(model)
    txt, cites = c.ask(
        "Answer in one sentence, from a search result.",
        [{"role": "user",
          "content": "Search the web: what is the title of Dorit Bar-On's "
                     "2004 book on avowals and self-knowledge?"}],
        search=True, max_uses=2, max_tokens=600)
    print("\n%s\n" % txt.strip()[:600])
    print("searches run: %d" % c.searches)
    for x in cites[:5]:
        print("  - %s" % x["url"])
    if c.searches == 0:
        print("\nNo search was performed. The tool may not be enabled for "
              "this key — the answer above came from memory, which is exactly "
              "what this script must not do.", file=sys.stderr)
    else:
        print("\nweb search is working.")

    # The other dependency, and the one with no API key behind it.
    print("\nOpenAlex (used to check that cited works exist):")
    r = openalex_lookup("Authority and Estrangement")
    if r["status"] == "FOUND":
        print("  reachable — matched %r (%s)"
              % (r.get("matched"), r.get("year")))
    elif r["status"] == "LOOKUP FAILED":
        err = str(r.get("error") or "")
        print("  NOT REACHABLE from this machine: %s" % err)
        try:
            import certifi
            print("  (certifi is installed at %s)" % certifi.where())
        except ImportError:
            print("  certifi is NOT installed. Fix:")
            print("      python3 -m pip install --upgrade certifi")
        if "CERTIFICATE_VERIFY" in err.upper():
            print("  This is the macOS certificate-store problem. If the "
                  "above did not fix it, run once:")
            print("      /Applications/Python*/Install\\ Certificates.command")
        print("  Attribution runs will still check whether views are held, "
              "but cannot verify that cited works exist.")
    else:
        print("  reachable, but the control lookup did not match — "
              "%s" % r.get("nearest"))


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", default=None,
                   help="a Thesis Forge raw.json (novelty check) or an "
                        "Outline Deviser raw.json (attribution check) — "
                        "it works out which from the file")
    p.add_argument("--match", default=None, help="pick one thesis by substring")
    p.add_argument("--index", type=int, default=None, help="pick one by index")
    p.add_argument("--top", type=int, default=None,
                   help="check the top N theses instead (default 4)")
    p.add_argument("--max-uses", type=int, default=8,
                   help="cap on searches per thesis or attribution")
    p.add_argument("--no-sep", action="store_true",
                   help="skip the Stanford Encyclopedia pass on novelty runs")
    p.add_argument("--no-attrib", action="store_true",
                   help="attribution runs: check that cited works EXIST "
                        "(free, mechanical) but skip the model check on "
                        "whether the ascribed views are held")
    p.add_argument("--rerender", default=None, metavar="RAW.JSON")
    p.add_argument("--probe", action="store_true",
                   help="run one search and exit; confirms the web search "
                        "tool is available before spending anything")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--out", default="lit1")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if args.rerender:
        rerender(args.rerender)
        return
    if args.probe:
        probe(args.model)
        return
    if not args.raw:
        sys.exit("give --raw (a Forge or Deviser raw.json), or --probe")

    kind, data = load_any(args.raw)

    if kind == "forge":
        picks = pick_theses(data, args.match, args.index, args.top)
        targets = [build_target(t) for t in picks]
        if args.dry_run:
            print("NOVELTY check on %d thesis/theses:" % len(targets))
            for t in targets:
                print("  - %s" % t["thesis"][:100])
            cost = len(targets) * args.max_uses * 0.01 + len(targets) * 0.03
            print("~%d API calls, up to %d searches "
                  "(~$%.2f at $10/1000 searches plus tokens)."
                  % (len(targets), len(targets) * args.max_uses, cost))
            if not args.no_sep:
                print("Plus the SEP pass: 1 call to choose entries, then one "
                      "per entry with the full text in context (~$0.10 each, "
                      "all theses covered per call). No searches — the "
                      "entries are fetched directly.")
            return
        client = Client(args.model)
        print("[1/3] novelty — %d thesis/theses, live search…" % len(targets))
        results = []
        with ThreadPoolExecutor(max_workers=3) as ex:
            futs = {ex.submit(check_novelty, client, t, args.max_uses): t
                    for t in targets}
            for f in as_completed(futs):
                t = futs[f]
                try:
                    results.append({"target": t, "finding": f.result()})
                except Exception as e:
                    print("      failed: %s" % e, file=sys.stderr)
                    results.append({"target": t,
                                    "finding": {"error": str(e)[:300]}})
        results.sort(key=lambda r: targets.index(r["target"]))
        for r in results:
            fnd = r["finding"].get("findings") or []
            hard = [x for x in fnd if str(x.get("relation")).upper()
                    in ("ANTICIPATED", "CONTRADICTED")]
            print("      %-58s %d findings, %d damaging"
                  % (r["target"]["thesis"][:58], len(fnd), len(hard)))

        sep = None
        if args.no_sep:
            print("[2/3] SEP pass skipped (--no-sep)")
        else:
            print("[2/3] SEP — reading the entries themselves…")
            try:
                idx = sep_index()
                slugs, why = sep_pick(client, targets, idx)
                print("      %d entries indexed; reading %s"
                      % (len(idx), ", ".join(slugs) or "none"))
                if why:
                    print("      %s" % why)
                entries = []
                for s in slugs:
                    try:
                        entries.append(sep_check(client, targets, s))
                    except Exception as e:
                        entries.append({"slug": s, "error": str(e)[:200]})
                        print("      %s failed: %s" % (s, e), file=sys.stderr)
                sep = {"picked": slugs, "why": why, "entries": entries,
                       "indexed": len(idx)}
            except Exception as e:
                print("      SEP pass failed: %s" % e, file=sys.stderr)
                sep = {"error": str(e)[:300]}

        state = {"mode": "novelty", "source": args.raw,
                 "results": results, "sep": sep,
                 "theses": [t["thesis"] for t in targets]}
        print("[3/3] writing report…")
        write_outputs(state, args.out)
        print("\n%d API calls, %d searches." % (client.calls, client.searches))

    else:
        addrs = addresses_from(data)
        if args.dry_run:
            titles = sum(len(cited_titles(a["text"])) for a in addrs)
            print("ATTRIBUTION check: %d addresses, %d quoted titles."
                  % (len(addrs), titles))
            print("Title existence via OpenAlex is free.")
            if not args.no_attrib:
                print("~%d API calls (~$%.2f)."
                      % (len(addrs), len(addrs) * 0.03))
            return

        print("[1/3] resolving cited titles against OpenAlex (free)…")
        cites = []
        pairs = [(a, t) for a in addrs for t in cited_titles(a["text"])]
        # OpenAlex indexes journal articles and books, not encyclopedia
        # entries. Without this, a real SEP entry — one this tool may have
        # read in full on a novelty run — is reported as NOT FOUND, which
        # reads as a fabricated citation. Worse than useless.
        try:
            sep_titles = sep_index()
        except Exception:
            sep_titles = []
        with ThreadPoolExecutor(max_workers=6) as ex:
            futs = {ex.submit(openalex_lookup, t): (a, t) for a, t in pairs}
            for f in as_completed(futs):
                a, t = futs[f]
                try:
                    rec = f.result()
                except Exception as e:
                    rec = {"title": t, "status": "LOOKUP FAILED",
                           "error": str(e)[:160]}
                rec["where"] = a.get("where")
                if rec["status"] == "NOT FOUND" and sep_titles:
                    best, best_r = None, 0.0
                    for title, slug in sep_titles:
                        r = difflib.SequenceMatcher(
                            None, _norm(rec["title"]), _norm(title)).ratio()
                        if r > best_r:
                            best, best_r = (title, slug), r
                    if best and best_r >= 0.82:
                        rec.update({"status": "FOUND", "matched": best[0],
                                    "source": "SEP",
                                    "url": "%s/entries/%s/" % (_SEP, best[1]),
                                    "ratio": round(best_r, 2)})
                cites.append(rec)
        missing = [c for c in cites if c["status"] != "FOUND"]
        print("      %d titles, %d did not resolve" % (len(cites), len(missing)))
        for c in missing:
            print("      ✗ %s" % c["title"][:70])

        results = []
        if args.no_attrib:
            print("[2/3] view check skipped (--no-attrib)")
            client = None
        else:
            client = Client(args.model)
            print("[2/3] checking %d attributions, live search…" % len(addrs))
            with ThreadPoolExecutor(max_workers=4) as ex:
                futs = {ex.submit(check_attribution, client, a, 4): a
                        for a in addrs}
                for n, f in enumerate(as_completed(futs), 1):
                    a = futs[f]
                    try:
                        results.append({"address": a, "finding": f.result()})
                    except Exception as e:
                        results.append({"address": a,
                                        "finding": {"error": str(e)[:300]}})
            for verdict in ("DOES NOT HOLD", "DISTORTED", "CANNOT TELL"):
                n = sum(1 for r in results
                        if (r["finding"] or {}).get("verdict") == verdict)
                print("      %-14s %d" % (verdict, n))

        state = {"mode": "attribution", "source": args.raw,
                 "citations": cites, "results": results}
        print("[3/3] writing report…")
        write_outputs(state, args.out)
        if client:
            print("\n%d API calls, %d searches."
                  % (client.calls, client.searches))

    print("open %s   <- start here" % os.path.join(args.out, "lit.html"))


if __name__ == "__main__":
    main()
