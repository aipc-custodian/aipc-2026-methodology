#!/usr/bin/env python3
"""diag.py MODEL — three tiny calls that show how a model behaves. Prints only."""
import sys
from anthropic import Anthropic
m = sys.argv[1] if len(sys.argv) > 1 else "claude-sonnet-5-5"
c = Anthropic()

def show(tag, **kw):
    try:
        r = c.messages.create(model=m, **kw)
        types = [getattr(b, "type", "?") for b in r.content]
        text = "".join(getattr(b, "text", "") or "" for b in r.content if getattr(b, "type", "") == "text")
        print("%s: OK stop=%s blocks=%s in=%s out=%s text=%r"
              % (tag, r.stop_reason, types, r.usage.input_tokens, r.usage.output_tokens, text[:120]))
    except Exception as e:
        print("%s: ERROR %s" % (tag, str(e)[:400]))

q = [{"role": "user", "content": "Return a JSON list of three colours. JSON only."}]
show("A temp=0.2 ", max_tokens=300, temperature=0.2, messages=q)
show("B temp=0.7 ", max_tokens=300, temperature=0.7, messages=q)
show("C temp=1.0 ", max_tokens=300, temperature=1.0, messages=q)
show("D no temp  ", max_tokens=300, messages=q)
show("E search   ", max_tokens=400, messages=[{"role": "user", "content": "Search the web: in what year did the Stanford Encyclopedia of Philosophy first go online? One sentence."}],
     tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 2}])
show("F search2k ", max_tokens=2000, messages=[{"role": "user", "content": "Search the web: in what year did the Stanford Encyclopedia of Philosophy first go online? One sentence."}],
     tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 2}])
