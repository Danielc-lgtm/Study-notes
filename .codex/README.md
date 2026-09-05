# `.codex/` — persistent Codex workflow for this vault

Codex Cloud tasks have no memory of each other. This directory is the memory:
it holds the operating procedure, the quality bar, and the state of whatever
task is in flight, all committed to Git so that any fresh run can pick up
exactly where the last one stopped. The content specification itself is *not*
here — it lives in `AGENTS.md`, `CLAUDE.md`, and `.claude/skills/` (shared with
Claude Code; the `.claude` name is historical). `.codex/` adds operational
state, workflow, and quality control on top of that.

| File | Role |
|---|---|
| `workflow.md` | Step-by-step procedure (Phases 0–7): preflight, resolving a short prompt into units, branch/PR, context gathering, diagnosis, edit, review passes, commit, checkpoint, merge, end-of-run report, and resuming in a fresh session. |
| `note-quality.md` | Rubric distilled from the polymath-notes skill, organised by page type with applicability rules, plus the executable final checklist a unit must pass before it is `complete`. |
| `current-task.md` | Human-readable task ledger: goal, scope, mode, branch, PR, sources, completed/current/remaining units, unresolved issues, exact next action, last commit, merge history. |
| `progress.json` | Machine copy of the same state with a documented schema (`_schema` key). Codex updates both files on every commit. |
| `setup.sh` | Environment setup script run by Codex Cloud before each fresh container's agent phase; persists the GitHub credential and installs `gh`. |
| `README.md` | This file: the short-prompt interface, the PR lifecycle, and the one-time environment setup. |

Scratch working memory (content maps, diagnoses, manifests) goes in `.scratch/`,
which is gitignored and may vanish between runs; anything a future run needs
goes in the two ledgers instead.

---

## The short-prompt interface

Prompts can be one line. Codex expands them using `AGENTS.md` §2 and
`workflow.md` Phase 1.

`Improve Complex Analysis II`
→ Start a task for that topic (the topic page plus every page in its
subfolder). Run the full workflow: read sources and neighbours, diagnose, edit,
five review passes, mechanical audits, final checklist; update both ledgers;
commit the completed topic; push to the task branch `codex/improve-complex-analysis-ii`
and open (or update) its PR. Report the PR link. Not merged unless asked.

`Improve all complex analysis notes`
→ Inventory every topic page under that subject (I, II, III, IV …), write a
persistent multi-topic plan into the ledgers, then complete the topics one at a
time in dependency order on one branch and one PR. Each finished topic is its
own commit. A run that cannot finish the next topic checkpoints it coherently
rather than starting another.

`Create notes on spectral sequences`
→ Locate sources in `sources/`, build the content map (two-pass procedure),
decide vault placement and unit split, then create the topic page(s) and all
Def/Thm/Ex/Exercise-Index subpages per the polymath-notes specification,
auto-link, audit, review, commit, PR.

`Continue`
→ Resume the active task from `current-task.md`, `progress.json`, and recent
commits, on the existing branch and PR, starting at the recorded exact next
action.

`Do the next batch`
→ Same as `Continue`, but stop after completing the next atomic unit.

`Improve Complex Analysis II and merge` / `Merge`
→ As above, then merge the PR into `main` (see lifecycle). Only a prompt that
says "merge" merges.

### When another task is already active

- If the new prompt clearly continues or narrows the active task (`Continue`,
  `Do the next batch`, `Improve <unit inside the active scope>`), it updates
  that task.
- If it clearly starts a different task (`Create notes on X` while a
  topology rewrite is active), Codex first checkpoints the active task to a
  coherent state, sets its status to `paused` in both ledgers, commits and
  pushes, and only then replaces the active task with the new one on a new
  branch. The paused task's plan stays in the ledgers' merge/pause history so
  it can be resumed by name later.
- Unrelated tasks are never mixed on one branch, in one PR, or in one ledger
  entry. If a prompt is ambiguous between the two cases, Codex asks one
  question rather than guessing.

---

## PR lifecycle

    main ──► codex/<slug> ──► commit per completed unit ──► one PR ──► merge when the task is complete

- One large task uses one working branch and one pull request.
- Intermediate batches are committed and pushed to that branch and update the
  same PR; they are **not** merged by default.
- Merge happens when every unit is complete and `progress.json` says
  `ready_to_merge: true`, or when the user explicitly requests it.
- Mid-project merge on request: Codex commits the `.codex` state first, merges
  the PR (`gh pr merge --merge --delete-branch`), records the merge in the
  ledgers, and leaves the task active with `branch: null`. The next run starts
  from the updated `main`, creates a successor branch (`codex/<slug>-2`) and a
  new PR, and resumes from the recorded next action. Because the ledgers are in
  `main`, no state is lost across the merge.
- Codex never commits on `main` directly and never force-pushes.

---

## Environment setup (one-time, done by a human)

Codex Cloud separates a *setup phase* (internet on, secrets present) from the
*agent phase* (internet off by default, secrets wiped). For the agent to push,
open PRs, and merge on its own, three things have to be configured once in
ChatGPT → Codex → Environments → this repository. Nothing in the repo can do
these for you.

### 1. GitHub App

Settings → GitHub: the Codex app is installed and granted
`Danielc-lgtm/Study-notes`. (Already true if Codex has ever opened this repo.)

### 2. Fine-grained personal access token

GitHub → Settings → Developer settings → Fine-grained tokens → Generate:

- Repository access: **Only select repositories** → `Danielc-lgtm/Study-notes`
- Permissions: **Contents: Read and write**, **Pull requests: Read and write**
  (Metadata: Read is added automatically). Nothing else.

Scope is your main protection: the token lives in a container with internet.

### 3. Environment settings

| Setting | Value |
|---|---|
| Setup script | `bash .codex/setup.sh` |
| Secrets | `GH_TOKEN` = the token from step 2 |
| Environment variables (optional) | `GIT_USER_NAME`, `GIT_USER_EMAIL` for commit attribution; `GH_USER` if the GitHub login is not `Danielc-lgtm` |
| Agent internet access | **On (limited)** |
| Domain allowlist | `github.com`, `api.github.com`, `githubusercontent.com` (add `pypi.org`, `files.pythonhosted.org` only if you want pip installs) |
| Allowed HTTP methods | **All** — PR creation is POST and merge is PUT; a GET-only setting breaks both silently |

Why a Secret: it is wiped before the agent phase, so the raw token is never in
the agent's environment. `setup.sh` converts it into a stored git credential and
a `gh` login on disk, which do survive. Why internet on: the "Create PR" button
in the Codex UI uses the GitHub App from outside the container and needs no
network, but it is a human click and there is no merge button; an agent that
opens and merges PRs itself must reach `api.github.com` from inside the
container. Codex caches the container for up to 12 hours and reruns
`setup.sh` whenever the script, variables, or secrets change.

### 4. Smoke test

Task 1: `Run the preflight in .codex/workflow.md Phase 0 and report the output. Do not change any notes.`
Expected: logged in to github.com, fetch clean.

Task 2: `Create branch codex/smoke-test, add the line "smoke test <date>" under Merge history in .codex/current-task.md, push, open a PR, merge it, delete the branch.`
If that round-trips, short prompts work end to end.

### 5. Rotating the token

Generate a new token, replace the `GH_TOKEN` secret, save. Nothing in the repo
changes.
