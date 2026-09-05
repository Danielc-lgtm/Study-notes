# Operational workflow for Codex

This file turns `AGENTS.md`, `CLAUDE.md`, and the polymath-notes skill into a
step-by-step procedure. It is executable, not philosophical: a fresh Codex task
with no conversational memory follows it from Phase 0 to Phase 7. The content
standard itself is NOT restated here — it lives in
`.claude/skills/polymath-notes/SKILL.md` (+ `references/templates.md`,
`references/obsidian-patterns.md`) and is scored by `.codex/note-quality.md`.

Persistent state: `.codex/current-task.md` (human ledger) and
`.codex/progress.json` (machine ledger). Both are committed. They are the only
memory that survives between Codex runs. Scratch working memory goes in
`.scratch/` (gitignored, may be lost between runs — never put anything there that
a future run needs).

---

## Phase 0 — Preflight (every run, before anything else)

    git remote get-url origin >/dev/null 2>&1 || git remote add origin https://github.com/Danielc-lgtm/Study-notes.git
    gh auth status
    git fetch origin --prune
    git status --porcelain

(The first line is needed because Codex Cloud's checkout has no `origin`
remote; adding it is not a credential workaround, the credential itself comes
from `setup.sh`.)

Expected: `gh` logged in as the repository owner; fetch succeeds; working tree
clean. The environment is pre-authenticated by `.codex/setup.sh`. If `gh auth
status` or the fetch fails, do NOT improvise (no `gh auth login`, no device-code
flow, no tokens pasted into remotes). Stop and tell the user the environment is
misconfigured, pointing at `.codex/README.md` §"Environment setup". Never read or
print `~/.git-credentials` or `~/.config/gh/hosts.yml`.

Then read, in order: `AGENTS.md`, `.codex/current-task.md`,
`.codex/progress.json`, and `git log --oneline -15`.

---

## Phase 1 — Resolve the prompt into a task

### 1.1 Classify the prompt

| Prompt shape | Classification |
|---|---|
| `Continue`, `Do the next batch`, `Keep going`, `Next` | **resume** the active task |
| `Improve <Topic>` where `<Topic>` is inside the active task's scope | **resume**, narrowed to that unit |
| `Improve <Topic>` / `Improve all <area> notes` / `Create notes on <X>` naming something outside the active scope | **new task** |
| `... and merge`, `Merge`, `Merge the PR` | the active task's **merge** instruction (see Phase 6) |
| anything else | interpret expansively per `AGENTS.md` §2; if it cannot be mapped to one of the above, ask one precise question |

If `progress.json` has `"active": true` and the new prompt starts a **different**
task: first checkpoint the old task (Phase 5.2 with status `paused`), commit,
then proceed. Never mix two unrelated tasks on one branch or in one ledger.

### 1.2 Determine mode

- **improve** — the topic page already exists in `Study notes/`.
- **create** — no topic page exists; new-note generation from sources.
- **mixed** (multi-topic requests) — record the mode per unit.

Locate the topic: `find "Study notes" -iname "*<topic words>*"` on both the
topic page (`<Topic Name> — <subtitle>.md`) and its subfolder (`<Topic Name>/`).
Topic pages are chapter-level files named like
`Study notes/Analysis/Complex Analysis/Complex Analysis II — Cauchy's Theorem and its Consequences.md`
with subpages in the sibling folder `Complex Analysis II/`.

### 1.3 Resolve scope to concrete units

The default **unit of work** is one topic page plus every page in its subfolder
(Def / Thm / Ex / Exercise Index). Build the unit list:

- single topic → one unit;
- `all <area> notes` → every topic page under that area, in the order the
  chapters build on each other (I before II before III …);
- `Create notes on X` → one unit per chapter-level topic page you will create,
  decided after the Pass-1 content map (Phase 2.2).

Write the resolved scope into `current-task.md` and `progress.json` (Phase 5.2)
**before** editing any note. That is the first commit of a new task.

### 1.4 Branch and PR

Branch names: `codex/<kebab-slug>` (e.g. `codex/improve-complex-analysis-ii`,
`codex/improve-all-topology`, `codex/create-spectral-sequences`).

New task:

    git checkout -B codex/<slug> origin/main

Resume:

    git checkout <branch from current-task.md>
    git pull --ff-only origin <that branch>

Never commit on `main`. Never force-push. One task ↔ one branch ↔ one PR.

---

## Phase 2 — Gather context for the current unit

### 2.1 Discover the page graph

    ls "Study notes/<area>/<subject>/<Topic>/"
    grep -rl "\[\[<Topic page name>" "Study notes" | head          # incoming links
    grep -o "\[\[[^]|#]*" "<topic page>" | sort -u                  # outgoing links

Record every file in the unit in `progress.json` → `units[<id>].paths`.

### 2.2 Read sources

Repository sources live in `sources/` (and `paper_source/` for paper notes).
Match by filename/topic; for long PDFs extract only the relevant chapters
(`pdftotext`, `qpdf --pages` — see SKILL.md "Source Material"). In **create**
mode do the two-pass procedure from SKILL.md Step 4: Pass 1 skim → content map in
`.scratch/<slug>/content-map.md`; Pass 2 write chapter by chapter. Web search is
allowed when the environment permits it and the sources are thin (SKILL.md
Step 3); it is never required to finish a unit.

### 2.3 Read prerequisite and neighbouring notes

Open every page the topic page links to outside its own folder, the preceding
and following topic pages in the same subject, and the DAG entry for the subject
in `Study notes/Prerequisite DAG.md`. Note conventions (signs, normalisations,
standing assumptions) so the unit agrees with its neighbours.

---

## Phase 3 — Diagnose (improve mode) or plan (create mode)

### 3.1 Improve mode: diagnosis before edits

For the topic page and each subpage, write a short diagnosis in
`.scratch/<slug>/diagnosis-<unit>.md` against the thirteen defects in
`AGENTS.md` §7 and the applicable criteria in `.codex/note-quality.md`. Mark
each criterion **applicable / not applicable / pass / fail**. Only failing,
applicable criteria drive edits. This is what prevents gratuitous regeneration:
if the diagnosis is clean, the unit is already done — record it and move on.

Also run the mechanical audits (Phase 4.2) now to see the baseline.

### 3.2 Create mode: page plan

From the content map, list every page to be created with its exact filename
(the filename manifest, `.scratch/<slug>/manifest.md`), then check for existing
pages covering the same concepts (`grep -ril "<concept>" "Study notes"`) — link,
do not duplicate (SKILL.md Step 2, including the Geometry-of-Physics rule).

---

## Phase 4 — Edit and review the unit

### 4.1 Edit

Apply the polymath-notes templates section by section. Preserve filenames,
frontmatter, and existing correct content (`AGENTS.md` §3). Before renaming any
page or heading, grep for incoming `[[...]]` and `![[...#...]]` references and
update all of them in the same edit.

### 4.2 Mechanical audits (must be clean before review sign-off)

    python3 .claude/skills/polymath-notes/scripts/find-math-bugs.py
    python3 .claude/skills/polymath-notes/scripts/find-latex-bugs.py
    python3 .claude/skills/polymath-notes/scripts/find-wikilink-bugs.py
    python3 .claude/skills/polymath-notes/scripts/find-notation-gaps.py     # triage list, not a bug list
    python3 .claude/skills/polymath-notes/scripts/autolinker.py --apply --max-per-file 10   # create mode, or after adding pages

Fix with the matching `fix-*.py --apply` scripts where mechanical, by hand
otherwise. Then the link audit: every `[[target]]` (outside math/code) must
resolve to an existing `.md` file and every `![[page#section]]` to a real
heading. Unresolved forward references become **bold plain text**.

### 4.3 Five review passes (`AGENTS.md` §8, scored by `note-quality.md`)

Run them as separate passes, in this order, and *fix* what they find:

1. **Correctness** — statements, hypotheses, proofs, examples, conventions.
2. **Pedagogy** — motivation precedes machinery; concrete before abstract.
3. **Rederivation** — scaffolds, "why is it true", true names, legal operations
   are enough to reconstruct the development from a few handles.
4. **Knowledge graph** — filenames, YAML, links, transclusions, prerequisite
   recall, concept-map ↔ subpage consistency.
5. **Prose** — two registers, no filler, no restated formulas, no abbreviations.

Finish with the **final checklist** at the end of `.codex/note-quality.md`.
Record the per-pass verdicts in `progress.json` → `units[<id>].review`.

---

## Phase 5 — Commit and checkpoint

### 5.1 Commit the completed unit

    git add -A "Study notes" .codex
    git commit -m "<Topic>: <what changed>"
    git push -u origin HEAD

Commit message examples: `Improve Complex Analysis II: Cauchy theory and
theorem pages`, `Create Spectral Sequences I — §1.1–1.3: 9 definitions, 5
theorems, 7 exercises`. Never commit `.scratch/`. Do not commit changes to the
specifications (`AGENTS.md`, `CLAUDE.md`, `.claude/`, `.agents/`,
`.codex/workflow.md`, `.codex/note-quality.md`, `.codex/setup.sh`,
`.codex/README.md`) unless the user asked for that.

### 5.2 Update the ledgers (every commit, and always before a run ends)

Update `.codex/current-task.md` (all fields) and `.codex/progress.json`
(schema in that file's `_schema` key). Non-negotiable fields: current unit,
**exact next action**, unresolved issues, last completed commit SHA, branch, PR.
The test: a fresh run reading only these two files and `git log` must know
precisely what to do next. Commit ledger updates together with the unit, or as
their own `Checkpoint: <unit> — <state>` commit if the unit is unfinished.

### 5.3 If a unit cannot be finished in this run

Bring it to a coherent state (no half-rewritten page that contradicts its
neighbours; audits clean), set the unit's status to `in_progress` with an
explicit `next_action`, checkpoint-commit, push. Prefer finishing one unit over
starting a second.

---

## Phase 6 — Pull request and merge

### 6.1 Open the PR (once per task, after the first pushed commit)

    gh pr view --json number,url,state 2>/dev/null   # if it exists, just push; never open a second
    gh pr create --base main --head "$(git branch --show-current)" \
      --title "<Task goal>" --body-file .scratch/<slug>/pr-body.md

PR body: goal and scope; units completed (bullet per unit, one line each);
review passes performed; remaining units / next action; whether ready to merge.
Record the PR number and URL in both ledgers and commit. On later runs, refresh
the body with `gh pr edit --body-file ...` when the unit list changes.

### 6.2 When to merge

Merge only if **(a)** every unit is `complete`, the final cross-topic
consistency check is done, and `progress.json` has `ready_to_merge: true`; or
**(b)** the user explicitly asked to merge (`... and merge`, `Merge`).
Otherwise end the run with the PR open and report its URL.

### 6.3 How to merge

    git status --porcelain            # must be empty apart from .scratch/
    gh pr merge --merge --delete-branch
    git checkout main && git pull --ff-only origin main

`--merge` keeps the per-unit commits in history. If the merge is refused
(conflicts, protection), merge `origin/main` into the task branch, resolve, re-run
the audits on touched pages, push, retry once; otherwise report — never bypass.

### 6.4 Mid-project merge (user asked to merge before the task is complete)

1. Checkpoint per 5.2/5.3 and commit — the ledgers must say the task is
   *incomplete* and name the next unit.
2. Merge per 6.3.
3. Do NOT reset the ledgers. In `progress.json` set `"branch": null`,
   `"pr": null`, append the merged PR to `"merged_prs"`; in `current-task.md`
   record "merged into main at <sha>; continuation needs a new branch".
4. The next run (Phase 1.4) sees an active task with no branch → creates
   `codex/<slug>-2` from the updated `origin/main`, opens a new PR, and resumes
   from `next_action`. Nothing about the plan is lost because the plan lives in
   `main` now.

---

## Phase 7 — End of run

1. Working tree clean; ledgers updated; branch pushed; PR exists (or task done and merged).
2. Report to the user, in this order: PR URL and state (open / merged); units
   completed this run; units remaining; exact next action; any unresolved
   issue that needs a human decision.

---

## Resuming in a completely fresh session (the `Continue` path, end to end)

Phase 0 → read ledgers → Phase 1.4 resume branch → confirm `git log -1` matches
`last_commit` in `progress.json` (if the branch is ahead, the previous run
committed but did not update the ledger: reconcile from the diff before doing
anything else) → go straight to the unit and step named in `next_action` →
Phases 2–7 for that unit only → checkpoint → next unit if budget remains.
