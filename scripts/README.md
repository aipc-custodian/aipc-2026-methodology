# clean_run

The pipeline as used for the clean runs. The originals one folder down are
untouched and remain the record of how the first paper was made.

Run everything from inside this folder:

    cd "clean_run"
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 -m pip install --upgrade anthropic

## What is here

| File | Stage | What changed or what it does |
| --- | --- | --- |
| `thesis_forge.py` | 1 | Logging added. One prompt example made neutral. Otherwise as before. |
| `lit_check.py` | 2 | Logging added. One prompt example and the probe question made neutral. |
| `outline_deviser.py` | 2 | Logging added. New: `--notes`, `--merge A,B`, `--rework N --attr`. |
| `restate.py` | 2 | New. A model narrows a partly anticipated thesis to what is still new. |
| `source_reader.py` | 2 | New. A model names the works to read, then reads each in full. |
| `draft.py` | 3 | New. Several isolated drafts from one outline; optional ranking. |
| `review_round.py` | 3 | New. Referee, independent adjudicator, revision, cut to length. |
| `pick.py` | gates | New. A model chooses the thesis, the outline and the draft. For the custodian-only run. |
| `runlog.py` | all | New. Writes `run_log.json` and `calls.jsonl` into every run folder. |
| `llm.py` | all | New. Shared client for the new scripts; `--probe` tests a model id. |

## Before the first real run

    python3 llm.py --probe claude-sonnet-4-5
    python3 llm.py --probe claude-opus-5-5
    python3 llm.py --probe claude-sonnet-5-5
    python3 lit_check.py --probe

Each makes one or two tiny calls. They tell you whether the model id is
accepted on your key, whether the model takes a temperature, and whether web
search works. The new scripts have been run end to end against a stand-in for
the API, so the plumbing is tested; they have NOT yet made a live call.

## The run, in order

    # 1. theses
    python3 thesis_forge.py --area "$(cat seed/area.txt)" --literature seed/lit.json \
        --generators G --per-generator P --out run1
    python3 outline_deviser.py --raw run1/raw.json --list

    # 2. novelty on each shortlisted thesis (N = its index)
    python3 lit_check.py --raw run1/raw.json --index N --out lit_N

    # 2a. only if the one you want is partly anticipated
    python3 restate.py --raw run1/raw.json --index N --lit lit_N/raw.json --out restate_N
    #     ...then use  --raw restate_N/raw.json --index 0  below

    # 3. sources: the model says what to read, you fetch, the model reads
    python3 source_reader.py --raw run1/raw.json --index N --lit lit_N/raw.json \
        --needs --out needs_N
    python3 source_reader.py --raw run1/raw.json --index N --sources sources/ --out notes_N

    # 4. outlines, then attribution
    python3 outline_deviser.py --raw run1/raw.json --index N --notes notes_N/notes.md \
        --outlines 6 --out out1
    python3 lit_check.py --raw out1/raw.json --out attr1

    # 4a. only if needed (K, A, B are outline numbers)
    python3 outline_deviser.py --raw out1/raw.json --rework K --attr attr1/raw.json --out out1_rework
    python3 outline_deviser.py --raw out1/raw.json --merge A,B --out out1_merge
    #     ...the result is outline 0 in the new folder

    # 5. drafts
    python3 draft.py --raw out1/raw.json --outline K --notes notes_N/notes.md \
        --drafts 3 --rank --out drafts1

    # 6. review rounds (D = the draft you picked)
    python3 review_round.py --show-prompt        # paste to ChatGPT and Gemini
    mkdir reviews_r1                             # save each reply there, unedited
    python3 review_round.py --paper drafts1/draft_D.md --reviews reviews_r1 \
        --claude-referee claude-fable-5-1 --notes notes_N/notes.md --out round1
    python3 review_round.py --paper round1/revised.md --reviews reviews_r2 \
        --claude-referee claude-fable-5-1 --notes notes_N/notes.md --out round2

## The custodian-only run (Run B)

A model makes every choice. You run commands and fetch files; `pick.py`
prints the exact command to run next after each gate.

    python3 lit_check.py --raw run1/raw.json --top 4 --out lit_top     # shortlist by arithmetic
    python3 pick.py --thesis --raw run1/raw.json --lit lit_top/raw.json --out pick_thesis
    #   ...run what it prints (restate if needed, sources, outlines, attribution)
    python3 pick.py --outline --raw out1/raw.json --attr attr1/raw.json \
        --notes notes_N/notes.md --out pick_outline
    #   ...run what it prints (rework if needed, drafts with --rank)
    python3 pick.py --draft --raw drafts1/raw.json --notes notes_N/notes.md --out pick_draft
    #   ...run what it prints (review rounds)

If the thesis pick comes back with no choice, run the Forge again.

Every script except `pick.py` takes `--dry-run`, which prints what it would do and spends
nothing.

## What the logs give you

Every run folder now holds `run_log.json` (script and its hash, the command
as typed, every argument, model asked for and model reported, every prompt,
times, token totals, candidate counts) and `calls.jsonl` (every call in full).
The methodology report can be written from these alone. Because you pass
numbers and file paths, the command lines in the logs are also the complete
record of what you contributed.

Cost is not computed: token counts are exact, prices change. Read the cost
from the billing console for the dates of the run.

## Two flags to leave alone

`outline_deviser.py --thesis "..."` takes a thesis typed by hand. The log
records when it is used. `--with-sketch` hands every outline the same prior.
