---
name: algorithmic-exercises
description: Create or revise Obsidian exercises that reconstruct conventional algorithms and advanced data structures, or adapt real competitive programming problems into precise self-contained specifications with collapsed solutions.
---

# Algorithmic and competitive programming exercises

All paths below are relative to the repository root. Read `.codex/standards.md`, `.codex/exercise-format.md`, and `.codex/selection.md` before creating or revising exercises. Read relevant existing `feedback:` fields and preserve user-written `insight:` and `feedback:` text.

Use this skill for two distinct outputs:

- **Algorithmic:** reconstruct a conventional algorithm or advanced data structure from the behavior and efficiency it must provide. Save under `Study notes/exercises/algorithmic/`.
- **Competitive programming:** solve an actual problem obtained from a competitive programming source. Save under `Study notes/exercises/competitive_programming/`.

Use the shared format and metadata. Each note has exactly the two top-level sections `Problem` and `Solution`, an empty editable `insight:` field immediately before `Solution` on creation, and the shared editable `feedback:` field. Everything needed to attempt the task belongs in `Problem`; the complete answer belongs inside its single collapsed solution callout. Do not add hints, visible decompositions, strategy classifications, takeaways, or bridges.

## Algorithm reconstruction

Translate the target technique into an operational task. State the input and output types, legal inputs, required behavior, and any time/space target that defines the challenge. For a data structure, specify the state it represents and the signature, preconditions, effect, and return value of every required operation. Distinguish construction cost from operation cost and worst-case from amortized or expected guarantees. Define the computational model when it affects the answer.

Keep the representation, invariant, and target algorithm's identity out of the unsolved problem unless the user explicitly asks to reconstruct a named algorithm. Neutral titles and index labels should identify the task without revealing the method. Supply definitions and prerequisite tools needed to understand the task; do not assume that naming a sophisticated subroutine explains it.

Cover both conventional algorithms and advanced data structures as requested. Prefer an exercise with a reusable mechanism and a clear reconstruction task over a catalogue entry that merely asks the reader to reproduce familiar code. Avoid making a large data structure artificially easy by disclosing its internal design in the problem statement.

## Competitive programming adaptation

Open the actual original problem on its official contest, judge, or archive page and verify its constraints and semantics. Consult an official editorial when useful, but independently check the solution. Never invent a contest attribution or claim to have retrieved an inaccessible problem; use another accessible primary source or user-supplied problem text.

Remove fictional story details while preserving every mathematical condition. Give a precise typed input/output specification, all bounds that affect feasibility, indexing and tie rules where relevant, and small checked examples when they clarify an ambiguity. Preserve the original task's computational difficulty; record any intentional variation accurately. Judge-specific text parsing is needed only when it affects the task or the user requests submission-ready code.

Keep a minimal original-source citation in the location specified by the shared format, without adding a source/bridge section or exposing editorial spoilers. Check existing exercises by source problem identifier and mathematical specification before adding another.

## Solution and completion

Inside the one collapsed solution, give executable-in-principle pseudocode and a complete self-contained explanation: why the construction is natural, what state and invariants it maintains, why every step is correct, why it terminates, and justified time and space bounds. Define all pseudocode inputs, outputs, helpers, and operations; a black-box call must either be an explicitly supplied primitive or be explained sufficiently to implement. Explain amortization or randomization when used, including its assumptions.

Check the solution against the stated bounds, edge cases, and examples. For a subtle implementation claim, use a small independent brute-force comparison or worked trace when it materially tests correctness. Do not treat successful examples as a proof.

Update the corresponding category index directly in `Study notes/exercises/` and ensure every newly created content folder has a navigable index. Follow shared deduplication, metadata, and feedback rules. Do not create exercises merely because the skill or setup was installed.
