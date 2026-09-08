# Gauge Theory build — resume playbook

This directory persists the scaffolding for the thirteen-chapter Gauge Theory
series build so it survives container reclamation. The vault pages themselves
are committed under `Study notes/Geometry/Gauge Theory/`. This is temporary
build provenance and is removed in the final cleanup commit.

## State (living summary — update as chapters complete)
- Chapters **I, II**: complete and reviewed.
- Chapters **III, IV, V, VI**: first unit(s) written; remaining units pending.
- Chapters **VII–XIII**: not started.
- All three manifests, `specs/`, `units.json`, and `chapargs/` are final.
- Progress ledger of loose ends: `scratchpad/reconcile-notes.txt`.

## The scratchpad path (hardcoded in the workflow script)
`workflow-write.js` hardcodes
`S = /tmp/claude-0/-home-user-Study-notes/a00e52f1-c9a2-537c-a39b-06f8e3c8a9c6/scratchpad`.
That path is derived from the session UUID and is stable across restarts of THIS
session. On a fresh container, restore the scaffolding to it before launching:

```
S=/tmp/claude-0/-home-user-Study-notes/a00e52f1-c9a2-537c-a39b-06f8e3c8a9c6/scratchpad
mkdir -p "$S" && cp -r /home/user/Study-notes/.gauge-build/scratchpad/* "$S/"
```

## Each usage window: write the remaining pages
1. Regenerate the pending-job args (only jobs whose pages are not yet on disk):
   `python3 "$S/pending-units.py"` → writes `$S/chapargs-pending/<CHAPTER>.json`.
2. Launch a batch of chapter-workflows (about 4–6 at once to stay within the
   window). For each chapter C, `cat "$S/chapargs-pending/C.json"` and pass it as
   the `args` of a `Workflow` call with
   `scriptPath: "$S/workflow-write.js"`. The script accepts `{units:[{unit,jobs}]}`.
3. As each completes, `git add -A && git commit && git push`. Re-run
   `pending-units.py` to refresh what's left; repeat until it reports 0 pending.

## After all 604 subpages exist
4. Assembly: for each chapter run `workflow-assemble.js` with
   `args.chapter` from `chapters.json` and `args.subResults` (unit reports), then
   once with `args.seriesMap` to write `Gauge Theory — Series Map`.
5. Mechanical audits over the new folder: `find-unproved-theorems.py`, the
   math/LaTeX/wikilink scanners + fixers, a vault-wide link audit, the autolinker.
6. Reconcile every item in `scratchpad/reconcile-notes.txt` and the manifests'
   `[NEEDED FROM …]` markers (14 in manifest-2, 25 in manifest-3).
7. Update `.codex/current-task.md` and `.codex/progress.json`; optionally note the
   series in `Study notes/Prerequisite DAG.md`.
8. Remove `.gauge-build/` and commit the cleanup.
