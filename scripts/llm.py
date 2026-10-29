#!/usr/bin/env python3
"""
llm.py — the client the later-stage scripts share.

restate.py, source_reader.py, draft.py and review_round.py all need the same
four things the earlier scripts did not: long outputs (so calls are
streamed), web search, PDFs in the prompt, and the run log. They are here
once rather than in four places.

    python3 llm.py --probe claude-opus-5-5

makes one tiny call and reports whether the model id is accepted, whether it
takes a temperature, and whether web search works on your key. Run it once
for each model you plan to use, before anything expensive.
"""

import base64, json, os, re, sys, time

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None

SEARCH_TOOL = "web_search_20250305"


class Client:
    def __init__(self, model, log=None):
        if Anthropic is None:
            sys.exit("the anthropic package is not installed: "
                     "python3 -m pip install --upgrade anthropic")
        self.c = Anthropic()
        self.model = model
        self.log = log
        self.calls = 0
        self.send_temperature = True
        # Later models reason before answering and the reasoning is billed
        # as output, so allowances sized for Sonnet 4.5 cut them off. Same
        # rule as lit_check.py, outline_deviser.py and thesis_forge.py.
        self.scale = 1.0 if model.startswith("claude-sonnet-4-5") else 3.0
        if self.log:
            self.log.set("output_allowance_scale", self.scale)

    MAX_OUTPUT = 64000  # ceiling on any single call's allowance
    MAX_PAUSES = 6      # continuations of a paused turn before giving up

    def log_get(self, key):
        try:
            return self.log.head.get("facts", {}).get(key)
        except Exception:
            return None

    def ask(self, system, messages, temperature=1.0, max_tokens=8000,
            search=False, max_uses=8, label=None, model=None):
        """One call, streamed. Returns the text; search narration included.

        Some models refuse a temperature. When one does, the call is retried
        without it and the fact is written to the log — a silent fallback
        would make the report's account of the sampling settings false.
        """
        self.calls += 1
        label = label or sys._getframe(1).f_code.co_name
        use_model = model or self.model
        max_tokens = min(int(max_tokens * self.scale), self.MAX_OUTPUT)
        last = None
        for attempt in range(4):
            kw = dict(model=use_model, max_tokens=max_tokens,
                      messages=messages)
            if system:
                kw["system"] = system
            sent_t = None
            if self.send_temperature and temperature is not None:
                kw["temperature"] = sent_t = temperature
            if search:
                kw["tools"] = [{"type": SEARCH_TOOL, "name": "web_search",
                                "max_uses": max_uses}]
            try:
                # A turn with many server-side searches can come back with
                # stop_reason "pause_turn": the API has paused it and
                # expects it to be sent back, as is, to continue. Treating
                # the pause as the end returned an empty answer (Run A,
                # Step 4, style guide sample). Continue up to MAX_PAUSES.
                convo, parts, pauses = list(messages), [], 0
                while True:
                    kw["messages"] = convo
                    t0 = time.time()
                    with self.c.messages.stream(**kw) as st:
                        r = st.get_final_message()
                    txt = "".join(getattr(b, "text", "") or ""
                                  for b in r.content
                                  if getattr(b, "type", None) == "text")
                    parts.append(txt)
                    stop = getattr(r, "stop_reason", None)
                    if self.log:
                        self.log.record(label if not pauses else
                                        "%s_cont%d" % (label, pauses),
                                        system, convo, txt, r, sent_t,
                                        max_tokens, time.time() - t0,
                                        extra={"search_enabled": bool(search),
                                               "model_requested": use_model,
                                               "stop_reason": stop})
                    if stop != "pause_turn" or pauses >= self.MAX_PAUSES:
                        break
                    pauses += 1
                    print("      %s paused by the API; continuing (%d)"
                          % (label, pauses), file=sys.stderr)
                    new = [_block(b) for b in r.content]
                    if convo and convo[-1].get("role") == "assistant":
                        convo = convo[:-1] + [{"role": "assistant",
                                               "content": convo[-1]["content"] + new}]
                    else:
                        convo = convo + [{"role": "assistant", "content": new}]
                if stop == "pause_turn":
                    print("      warning: %s was still paused after %d "
                          "continuations; its answer may be incomplete"
                          % (label, pauses), file=sys.stderr)
                if pauses and self.log:
                    self.log.set("pause_continuations",
                                 (self.log_get("pause_continuations") or 0) + pauses)
                if stop == "max_tokens":
                    print("      warning: %s hit the output limit (%d tokens) "
                          "and was cut off" % (label, max_tokens),
                          file=sys.stderr)
                return "".join(parts)
            except Exception as e:
                last = e
                msg = str(e).lower()
                if "temperature" in msg and self.send_temperature:
                    self.send_temperature = False
                    if self.log:
                        self.log.set("temperature_refused_by_model", use_model)
                    print("      %s does not accept a temperature; continuing "
                          "without one" % use_model, file=sys.stderr)
                    continue
                if attempt == 3:
                    raise
                time.sleep(2 ** attempt)
        raise last



# ---------------------------------------------------------------------------
# The standard for "anticipated". Every script that judges priority uses this
# one text, so the novelty check, the restatement, the source reader, the
# picker and the review adjudicator all apply the same bar. Set by the
# custodian on 13 October 2026 (Run A, Step 3), after the novelty check was
# found to treat a passing mention as anticipation.
# ---------------------------------------------------------------------------

ANTICIPATION_STANDARD = """\
THE STANDARD FOR "ANTICIPATED". A prior work anticipates a claim only if
EITHER

  ENDORSED   it discusses the claim extensively, as a main or sustained line
             of argument and not a remark, footnote or passing suggestion,
             AND its author asserts or endorses the claim;
OR
  FORECLOSED it discusses the claim extensively AND its argument
             conclusively closes the claim off, so that defending it again
             would be pointless.

Nothing short of this is anticipation. In particular:

  PASSING    the claim is raised, suggested, entertained or listed as an
             option, without development. Developing an idea that someone
             mentioned is an ordinary and legitimate philosophical
             contribution; the earlier mention is credited, not conceded.
  ENTERTAINED the claim is explored at length but neither endorsed nor
             conclusively closed off.
  FRAMEWORK  the work holds a broader view of which the claim would be an
             application, but does not itself draw that application.

A work that argues against the claim without conclusively closing it off is
a rival to be answered (CONTRADICTED), not an anticipation.

Extent and endorsement can only be judged from the text. Say what you
actually saw: the FULL TEXT, an ABSTRACT, a SNIPPET from a search result, or
a SECONDHAND report by another author. A verdict of ANTICIPATED that rests on
anything less than the full text is PROVISIONAL and must be marked so.
"""

# ---------------------------------------------------------------------------
# Small things every script needs
# ---------------------------------------------------------------------------

def _block(b):
    """A response content block as a dict, to send back in a continuation."""
    if isinstance(b, dict):
        return b
    if hasattr(b, "model_dump"):
        return b.model_dump(exclude_none=True)
    return {"type": "text", "text": getattr(b, "text", "")}


def extract_json(text):
    if not text:
        return None
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.M)
    for opener, closer in (("{", "}"), ("[", "]")):
        i, j = t.find(opener), t.rfind(closer)
        if i != -1 and j > i:
            try:
                return json.loads(t[i:j + 1])
            except Exception:
                continue
    return None


def tagged(text, tag):
    """The content of the LAST <tag>…</tag> in a response, or None.

    The last, because a model that searches narrates as it goes and may
    mention the tag before it writes the thing.
    """
    hits = re.findall(r"<%s>\s*(.*?)\s*</%s>" % (tag, tag), text or "", flags=re.S)
    return hits[-1].strip() if hits else None


_REFS = re.compile(r"^\s*(?:#+\s*)?(?:\*\*)?\s*(references|bibliography|works cited)"
                   r"\s*(?:\*\*)?\s*$", re.I | re.M)


def split_refs(essay):
    """(body, bibliography). The competition counts everything but the latter."""
    m = None
    for m in _REFS.finditer(essay or ""):
        pass                                   # the last such heading
    if not m:
        return essay or "", ""
    return essay[:m.start()], essay[m.start():]


def word_count(essay):
    """Words that count toward the limit: everything except the bibliography.

    Markdown marks are stripped first so that '##' is not counted as a word.
    Counters differ at the margin — leave room rather than trusting this to
    the last word.
    """
    # Footnotes count wherever their text sits, including below the
    # bibliography, where Markdown lets a writer put it (change 26).
    notes = []
    def _keep(m):
        notes.append(m.group(1))
        return ""
    essay = _FOOTNOTE_DEF.sub(_keep, essay or "")
    body, _ = split_refs(essay)
    body = body + "\n" + "\n".join(notes)
    body = re.sub(r"\[\^[^\]]+\]", " ", body)            # note markers
    body = re.sub(r"^\s*#+\s*", "", body, flags=re.M)
    body = re.sub(r"[*_`>]+", " ", body)
    return len(re.findall(r"\S+", body))


# A Markdown footnote definition: "[^id]: text", with indented continuation
# lines.
_FOOTNOTE_DEF = re.compile(r"^\[\^[^\]]+\]:[ \t]*((?:.*)(?:\n(?:[ \t]+.*|[ \t]*(?=\n[ \t]+\S)))*)", re.M)


def load_thesis(raw_path, index=None):
    """The thesis to work on, from whichever kind of raw.json this is.

    A Forge or restate.py file is a list: pick by --index, and take the
    post-kill restatement where there is one, as the Deviser does. A Deviser
    file is a dict that already carries its thesis.
    """
    with open(raw_path) as f:
        data = json.load(f)
    if isinstance(data, dict):
        return {"thesis": (data.get("thesis") or "").strip(),
                "target": data.get("target"), "source": raw_path,
                "index": None}
    if index is None:
        sys.exit("that is a Forge raw.json — say which thesis with --index "
                 "(python3 outline_deviser.py --raw %s --list)" % raw_path)
    if not 0 <= index < len(data):
        sys.exit("index %d out of range (0..%d)" % (index, len(data) - 1))
    r = data[index]
    surviving = (r.get("ruling") or {}).get("surviving_thesis")
    return {"thesis": (surviving or r.get("thesis") or "").strip(),
            "target": r.get("target"), "source": raw_path, "index": index}


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def pdf_block(path):
    with open(path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode()
    return {"type": "document", "title": os.path.basename(path),
            "source": {"type": "base64", "media_type": "application/pdf",
                       "data": data}}


def source_files(folder):
    ok = (".pdf", ".txt", ".md")
    return sorted(os.path.join(folder, f) for f in os.listdir(folder)
                  if f.lower().endswith(ok) and not f.startswith("."))


# ---------------------------------------------------------------------------

def probe(model):
    try:
        import anthropic
        print("anthropic %s" % getattr(anthropic, "__version__", "?"))
    except ImportError:
        sys.exit("the anthropic package is not installed")
    c = Client(model)
    try:
        txt = c.ask("Answer in five words or fewer.",
                    [{"role": "user", "content": "Say that you are working."}],
                    temperature=1.0, max_tokens=50)
    except Exception as e:
        sys.exit("model %r was refused: %s" % (model, str(e)[:300]))
    print("model accepted: %s  ->  %s" % (model, txt.strip()[:80]))
    print("temperature:    %s" % ("accepted" if c.send_temperature
                                  else "REFUSED — runs will go without one"))
    try:
        txt = c.ask("Answer in one sentence, from a search result.",
                    [{"role": "user",
                      "content": "Search the web: in what year did the "
                                 "Stanford Encyclopedia of Philosophy first "
                                 "go online?"}],
                    temperature=0.2, max_tokens=400, search=True, max_uses=2)
        print("web search:     ok  ->  %s" % txt.strip()[-160:])
    except Exception as e:
        print("web search:     FAILED — %s" % str(e)[:200])


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--probe":
        probe(sys.argv[2])
    else:
        print(__doc__)
