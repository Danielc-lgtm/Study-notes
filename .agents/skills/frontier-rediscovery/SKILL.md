---
name: frontier-rediscovery
description: Create or revise Obsidian exercises that reconstruct a verified cutting-edge result as a problem posed before its discovery, with complete context, motivated subproblems, separately hidden approaches, and a hidden solution.
---

# Frontier rediscovery

Read the repository-relative `AGENTS.md`, `.codex/standards.md`, `.codex/exercise-format.md`, and `.codex/selection.md` before writing. Use `Study notes/Prerequisite DAG.md` to identify subjects and familiarity; familiarity is not permission to omit necessary context. Read relevant exercise feedback and preserve the user's `insight:` and `feedback:` text.

Write under the repository-relative `Study notes/exercises/cutting edge/`. Maintain the folder's navigable index and relevant parent indexes under the shared index rules. This skill produces exercises when requested; installing or revising the skill does not itself request exercise generation.

## Select and verify the result

- Choose a specific actual result in a field represented in the DAG. Check current primary papers and, when useful, the authors' lectures, proofs, and code. Read enough of the actual work to verify the claim, hypotheses, limitations, and proof or method; an abstract alone is insufficient for a complete reconstruction.
- Establish what is cutting-edge as of the research date. Distinguish a proved theorem, empirical result, conjecture, and unresolved question. Record exact attribution and the source's publication or revision date in the hidden solution.
- Prefer a result whose complete reasoning can be made accessible through a finite, explicit dependency chain. Do not silently replace the selected result with a toy example or a weaker theorem. A simplified case may be a labeled subproblem; show how it relates to the full result and what remains to be established.
- If evidence or understanding is insufficient for a correct complete exercise, continue investigating or select a result that can be supported. Do not invent a proof or present a speculative argument as the solution.

## Construct the exercise

Use exactly the three substantive parts `Context`, `Problem`, and `Solution`, following `.codex/exercise-format.md`. The blank `insight:` field goes immediately before the solution; `feedback:` is an editable field, not a fourth part. Use a behavior- or question-based title that does not reveal the winning method.

**Context:** Recreate the question before discovery. Explain what the objects mean, why the question is worth asking, what obstacle makes it nontrivial, and the minimal relevant tools. Give clear types, assumptions, and guarantees for every mathematical or computational object. The baseline is mathematical maturity and basic undergraduate notation. Define specialized notation locally. Explain how supplied theorems can be applied: their inputs, hypotheses, outputs, and usable intuition, with small worked examples where necessary. Context may be long when completeness requires it. Links supply provenance or optional depth; reading them must not be necessary to solve the exercise.

**Problem:** State the target precisely without disclosing the achieved result as known history. Give the subproblems needed to reach it, in dependency order. For each subproblem:

1. State its objects, assumptions, and requested output.
2. Explain visibly why it is a natural question at this stage, using only the context and earlier subproblems.
3. Put the proposed approach and the reason that approach is natural inside its own initially collapsed Obsidian callout. Keep this separate from the final solution, so the reader can reflect before revealing guidance. State the method and its rationale here; keep the worked resolution in the solution.

The path should explain how a reader could discover the result, not merely split a finished proof into arbitrary fragments. Do not add the old convergent-strategy, sources-and-bridges, or generated-insight apparatus.

**Solution:** Put the complete reconstruction inside the initially collapsed solution callout specified in the shared format. Resolve every subproblem, justify each transition, and assemble the result with its full scope and limitations. Include typed pseudocode when the method is algorithmic; otherwise give the appropriate mathematical or experimental derivation. Reveal the actual result, researchers, and compact primary citations here. Label the path as a pedagogical reconstruction unless historical evidence documents it; do not claim to know how the researchers actually discovered the result.

## Check before delivery

Work backward from the completed solution. Every specialized fact or tool required to find it must be available in Context or derived by an earlier subproblem, with an understandable way to use it. Remove unused material. Check that a missing definition, unstated assumption, hidden prerequisite, or obligatory external lookup cannot block the reader. Keep discovery and composition as the source of difficulty. Check the full claim against its primary source, the collapsed callouts, editable fields, and index links. Apply relevant feedback through the shared feedback workflow.
