#!/usr/bin/env python3
"""Assemble an anonymised, copyright-safe submission repository.

Run from inside "AI Philosophy Competition". Writes ./submission_repo.
Copies an allowlist; converts .docx to .md with pandoc; scrubs identifying
paths; then scans everything for names, keys and e-mail addresses.
"""
import os, re, shutil, subprocess, sys, json

ROOT = os.getcwd()
OUT = os.path.join(ROOT, "submission_repo")
P2 = "Second Run - Philosophy of AI"
P1 = "First Run-Process Design"

# (source, destination) — directories copied recursively, minus EXCLUDE
PLAN = [
    # Paper 2
    (f"{P2}/Step 6 - Final/final.md", "paper2/essay.md"),
    (f"{P2}/Step 6 - Final/changes.md", "paper2/step6_final/changes.md"),
    (f"{P2}/Step 6 - Final/quotecheck/report.md", "paper2/step6_final/quotecheck_report.md"),
    (f"{P2}/Step 6 - Final/quotecheck/check.py", "paper2/step6_final/quotecheck.py"),
    (f"{P2}/Step 1 - Topic", "paper2/step1_topic"),
    (f"{P2}/Step 2 - Forge", "paper2/step2_forge"),
    (f"{P2}/Step 3 - Novelty", "paper2/step3_novelty"),
    (f"{P2}/Step 4 - Drafts", "paper2/step4_drafts"),
    (f"{P2}/Step 5 - Review", "paper2/step5_review"),
    ("Style Guide", "paper2/style_guide"),
    ("Third Run", "recipe"),
    ("clean_run", "scripts"),
    ("Instructions for Blinding Bots.docx", "recipe/instructions_memory_off.docx"),
    ("Current Debates in AI Philosophy (Gemini).pdf", "paper1/design/current_debates_gemini.pdf"),
    # Paper 1
    (f"{P1}/Final/final.md", "paper1/essay.md"),
    (f"{P1}/Final/changes.md", "paper1/changes.md"),
    (f"{P1}/Methodology Report-Common Ground as Accidental Convergence .docx", "paper1/methodology_report_paper1.docx"),
    (f"{P1}/Stage 1 Methodology Report - Thesis Forge.docx", "paper1/design/stage1_thesis_forge.docx"),
    (f"{P1}/Stage 2 Methodology Report - Lit Check and Outline Deviser.docx", "paper1/design/stage2_lit_check_outline_deviser.docx"),
    (f"{P1}/Stage 3 Methodology Report - Drafting and Cross-Model Revision.docx", "paper1/design/stage3_drafting_revision.docx"),
    ("Claude outputs/Stage Two - Methodology Report.docx", "paper1/design/stage2_report_draft.docx"),
    (f"{P1}/Outputs", "paper1/outputs"),
    (f"{P1}/Python Scripts", "paper1/scripts"),
]

ALLOWED_PDF = {"Gemini Suggestions (3.1 Pro Extended Thinking).pdf",
               "current_debates_gemini.pdf",
               "Current Debates in AI Philosophy (Gemini).pdf"}
EXCLUDE_DIRS = {"Sources_1", "Sources_1x", "papers", "__pycache__", "_to_delete"}
EXCLUDE_FILES = {".DS_Store", "notes.docx", "API Info.docx"}
EXCLUDE_PATHS = {  # relative to ROOT
    f"{P2}/Step 5 - Review/calibration/lampert.md",          # full text of a published article
    f"{P2}/Step 5 - Review/calibration/run1/calls.jsonl",     # contains that full text
    f"{P2}/Step 5 - Review/calibration/run1/raw.json",        # likewise
}

SCRUB = [
    (re.compile(r"/Users/[^/\s\"']+/Library/CloudStorage/[^/\s\"']+/Desktop/AI Philosophy Competition"), "<project>"),
    (re.compile(r"/Users/[^/\s\"']+"), "/Users/<user>"),
    (re.compile(r"OneDrive-[A-Za-z]+"), "<cloud>"),
    (re.compile(r"maclap[0-9-]+"), "<host>"),
    (re.compile(r"rcw-[0-9a-z]+"), "<user>"),
]
TEXT_EXT = {".md", ".txt", ".json", ".jsonl", ".py", ".html", ".csv"}
FLAG = re.compile(r"<identifying names and addresses: removed from the published copy>|"
                  r"sk-ant-(?!\.\.\.)[A-Za-z0-9_-]{6,}", re.I)

copied, excluded = [], []

def keep(src_rel):
    parts = src_rel.split(os.sep)
    name = parts[-1]
    if name in EXCLUDE_FILES or any(p in EXCLUDE_DIRS for p in parts):
        return False
    if src_rel in EXCLUDE_PATHS:
        return False
    if name.lower().endswith(".pdf") and name not in ALLOWED_PDF:
        return False
    if name.endswith(".pyc"):
        return False
    return True

def copy_one(src, dst):
    rel = os.path.relpath(src, ROOT)
    if not keep(rel):
        excluded.append(rel); return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if src.endswith(".docx"):
        dst = dst[:-5] + ".md"
        r = subprocess.run(["pandoc", src, "-t", "gfm", "--wrap=none", "-o", dst])
        if r.returncode:
            excluded.append(rel + " (pandoc failed)"); return
    else:
        shutil.copy2(src, dst)
    if os.path.splitext(dst)[1] in TEXT_EXT:
        t = open(dst, encoding="utf-8", errors="surrogateescape").read()
        for pat, rep in SCRUB:
            t = pat.sub(rep, t)
        open(dst, "w", encoding="utf-8", errors="surrogateescape").write(t)
    copied.append(os.path.relpath(dst, OUT))

if os.path.exists(OUT):
    sys.exit("submission_repo already exists; move it aside first")
for src_rel, dst_rel in PLAN:
    src = os.path.join(ROOT, src_rel)
    dst = os.path.join(OUT, dst_rel)
    if not os.path.exists(src):
        print("MISSING:", src_rel); continue
    if os.path.isdir(src):
        for dp, dns, fns in os.walk(src):
            dns[:] = [d for d in dns if d not in EXCLUDE_DIRS]
            for fn in fns:
                s = os.path.join(dp, fn)
                copy_one(s, os.path.join(dst, os.path.relpath(s, src)))
    else:
        copy_one(src, dst)

# scan
hits = []
for dp, dns, fns in os.walk(OUT):
    for fn in fns:
        p = os.path.join(dp, fn)
        if os.path.splitext(fn)[1] in TEXT_EXT:
            t = open(p, encoding="utf-8", errors="ignore").read()
        elif fn.endswith(".pdf"):
            t = subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True).stdout
        else:
            continue
        for m in FLAG.finditer(t):
            hits.append(f"{os.path.relpath(p, OUT)}: …{t[max(0,m.start()-40):m.end()+40]!r}…")

with open(os.path.join(ROOT, "submission_repo_build_log.txt"), "w") as f:
    f.write(f"copied {len(copied)} files\n\nEXCLUDED:\n" + "\n".join(excluded) +
            "\n\nSCAN HITS:\n" + ("\n".join(hits) or "none") + "\n")
size = sum(os.path.getsize(os.path.join(dp, fn)) for dp, _, fns in os.walk(OUT) for fn in fns)
print(f"copied {len(copied)} files, {size/1e6:.1f} MB; excluded {len(excluded)}; scan hits {len(hits)}")
