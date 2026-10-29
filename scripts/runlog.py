#!/usr/bin/env python3
"""
runlog.py — the record every script in this folder keeps of itself.

The competition's methodology report has to state the models and versions
used, the prompts, how many candidates were generated, and the machine time
and token usage. None of that was being written down. This module writes it
down, for every run, without anyone having to remember to.

Two files appear in each run's output folder:

    run_log.json   one record for the run: which script (and a hash of the
                   exact file), the command line as typed, every argument,
                   the model asked for and the model the API reported back,
                   every prompt constant in the script, start and finish
                   times, and token totals.

    calls.jsonl    one line per API call, in full: system prompt, messages
                   sent, text returned, temperature, tokens in and out,
                   searches run, seconds taken. This is the transcript — the
                   scripted equivalent of a chat log.

Nothing here makes an API call or changes what a script sends. It only
records. Cost is deliberately NOT computed: prices change, and a stale
price baked into a log is worse than none. Token counts are exact; read the
cost off them, or off the billing console.
"""

import atexit, datetime, hashlib, json, os, platform, sys, threading, time


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def _sha(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return None


def _plain(v):
    """Make a value JSON-safe without losing what it said."""
    try:
        json.dumps(v)
        return v
    except Exception:
        return repr(v)


def prompts_from(module_globals):
    """Every UPPERCASE constant in a script that holds prompt text.

    The scripts keep their prompts as module-level constants. Collecting
    them by convention means a prompt added later is logged without anyone
    updating a list.
    """
    out = {}
    for k, v in module_globals.items():
        if not k.isupper() or k.startswith("_"):
            continue
        if isinstance(v, (str, list, tuple, dict, int, float)):
            out[k] = _plain(v)
    return out


class RunLog:
    def __init__(self, out_dir, script_path, args=None, module_globals=None,
                 note=None):
        os.makedirs(out_dir, exist_ok=True)
        self.out_dir = out_dir
        self.path = os.path.join(out_dir, "run_log.json")
        self.calls_path = os.path.join(out_dir, "calls.jsonl")
        self._lock = threading.Lock()
        self._t0 = time.time()
        self._closed = False
        self.tot = {"calls": 0, "input_tokens": 0, "output_tokens": 0,
                    "cache_read_input_tokens": 0,
                    "cache_creation_input_tokens": 0,
                    "web_searches": 0, "api_seconds": 0.0}
        self.models_reported = {}
        try:
            import anthropic
            sdk = getattr(anthropic, "__version__", None)
        except Exception:
            sdk = None
        a = vars(args) if args is not None and hasattr(args, "__dict__") else (args or {})
        self.head = {
            "script": os.path.basename(script_path),
            "script_sha256": _sha(script_path),
            "command_line": sys.argv,
            "args": {k: _plain(v) for k, v in a.items()},
            "model_requested": a.get("model"),
            "started_utc": _now(),
            "python": platform.python_version(),
            "anthropic_sdk": sdk,
            "note": note,
            "prompts": prompts_from(module_globals or {}),
        }
        # A fresh run starts a fresh transcript; an old one in the same
        # folder is kept under another name rather than appended to.
        if os.path.exists(self.calls_path):
            os.replace(self.calls_path, self.calls_path + "." +
                       time.strftime("%Y%m%d-%H%M%S") + ".bak")
        self._write(finished=False)
        atexit.register(self.close)

    # -- recording ---------------------------------------------------------

    def record(self, label, system, messages, response_text, response=None,
               temperature=None, max_tokens=None, seconds=None, extra=None):
        u = getattr(response, "usage", None)
        tin = getattr(u, "input_tokens", None) or 0
        tout = getattr(u, "output_tokens", None) or 0
        cr = getattr(u, "cache_read_input_tokens", None) or 0
        cc = getattr(u, "cache_creation_input_tokens", None) or 0
        stu = getattr(u, "server_tool_use", None)
        ws = getattr(stu, "web_search_requests", None)
        if ws is None:
            ws = sum(1 for b in (getattr(response, "content", None) or [])
                     if getattr(b, "type", None) == "server_tool_use")
        model = getattr(response, "model", None)
        # Newer models reason before they answer, and that reasoning is
        # billed as output. Keep whatever of it the API hands back, and the
        # sequence of block types, so the transcript shows it happened.
        blocks = [getattr(b, "type", "?")
                  for b in (getattr(response, "content", None) or [])]
        thinking = "\n\n".join(
            str(getattr(b, "thinking", "") or "")
            for b in (getattr(response, "content", None) or [])
            if getattr(b, "type", None) == "thinking")
        rec = {
            "t_utc": _now(),
            "label": label,
            "model_reported": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stop_reason": getattr(response, "stop_reason", None),
            "input_tokens": tin,
            "output_tokens": tout,
            "cache_read_input_tokens": cr,
            "cache_creation_input_tokens": cc,
            "web_searches": ws or 0,
            "seconds": None if seconds is None else round(seconds, 2),
            "system": system,
            "messages": _scrub(messages),
            "response_text": response_text,
            "block_types": blocks,
            "thinking": thinking or None,
        }
        if extra:
            rec["extra"] = _plain(extra)
        with self._lock:
            with open(self.calls_path, "a") as f:
                f.write(json.dumps(rec) + "\n")
            t = self.tot
            t["calls"] += 1
            t["input_tokens"] += tin
            t["output_tokens"] += tout
            t["cache_read_input_tokens"] += cr
            t["cache_creation_input_tokens"] += cc
            t["web_searches"] += ws or 0
            t["api_seconds"] += seconds or 0.0
            if model:
                self.models_reported[model] = self.models_reported.get(model, 0) + 1

    def set(self, key, value):
        """Attach a fact about the run — a candidate count, a file chosen."""
        with self._lock:
            self.head.setdefault("facts", {})[key] = _plain(value)

    # -- writing -----------------------------------------------------------

    def _write(self, finished):
        d = dict(self.head)
        d["finished_utc"] = _now() if finished else None
        d["wall_seconds"] = round(time.time() - self._t0, 1)
        d["models_reported"] = self.models_reported
        t = dict(self.tot)
        t["api_seconds"] = round(t["api_seconds"], 1)
        d["totals"] = t
        tmp = self.path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(d, f, indent=2)
        os.replace(tmp, self.path)

    def close(self):
        if self._closed:
            return
        self._closed = True
        with self._lock:
            self._write(finished=True)

    def summary(self):
        t = self.tot
        return ("%d calls, %s tokens in, %s out, %d searches, %.0fs — "
                "logged to %s" % (t["calls"], f"{t['input_tokens']:,}",
                                  f"{t['output_tokens']:,}", t["web_searches"],
                                  time.time() - self._t0, self.path))


def _scrub(messages):
    """Messages as sent, except that file payloads are replaced by a stub.

    A base64 PDF in the transcript would make the log hundreds of megabytes
    and add nothing: the file is named, hashed and sized instead.
    """
    out = []
    for m in messages or []:
        c = m.get("content")
        if isinstance(c, str):
            out.append(m)
            continue
        blocks = []
        for b in c or []:
            if isinstance(b, dict) and b.get("type") == "document":
                src = b.get("source") or {}
                data = src.get("data") or ""
                blocks.append({"type": "document",
                               "title": b.get("title"),
                               "media_type": src.get("media_type"),
                               "sha256_of_base64": hashlib.sha256(
                                   data.encode()).hexdigest() if data else None,
                               "base64_chars": len(data)})
            else:
                blocks.append(_plain(b))
        out.append({"role": m.get("role"), "content": blocks})
    return out
