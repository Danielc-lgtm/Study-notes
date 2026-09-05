# Current task

**Overall status:** no active large task

<!--
Keep every field below, even when empty. Update this file on every commit that
touches notes and always before a run ends (workflow.md Phase 5.2). Keep it in
sync with progress.json — that file is the machine copy of the same state.
A human reading only this file should understand the state of the project.
-->

## Goal
_none_

## Scope
_none_ — list the units (one topic page + its subfolder each), in order.

## Mode
_none_ — `improve` | `create` | `mixed` (mode per unit in Scope if mixed).

## Working branch
_none_ — `codex/<slug>` while a unit is in progress; `none (merged)` between units (each completed unit is merged into `main` and its branch deleted).

## Pull request
_none_ — the PR of the unit currently in progress, `#<number> <url> (open)`; merged PRs move to Merge history.

## Sources
_none_ — repository files under `sources/` or `paper_source/` used for this task; DAG entry consulted.

## Completed units
_none_

## Current unit
_none_ — unit id, and which workflow phase it is in.

## Remaining units
_none_

## Unresolved issues
_none_ — anything a review left open or that needs a human decision.

## Exact next action
Wait for a user prompt. On `Improve <Topic>`, `Improve all <area> notes`, or `Create notes on <X>`: run workflow.md Phase 0, then Phase 1 to populate this file, commit it as the first commit on a new `codex/<slug>` branch, and proceed.

## Last completed commit
_none_

## Merge policy
`auto` — merge each completed unit into `main` immediately (default). Alternatives set by the prompt: `hold` (one PR, left open), `direct` (no PRs, push to `main`).

## Merge history
One line per merged unit: `#<PR> <unit> → main @ <sha> (<date>)`.
- #2 smoke test → main @ eba050d (2026-09-05)
