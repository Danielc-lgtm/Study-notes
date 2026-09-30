---
name: interdisciplinary-exercises
description: Create or revise self-contained Obsidian exercises from any node of the prerequisite DAG, including problems that meaningfully combine fields, with minimal sufficient context and a collapsed complete solution.
---

# Interdisciplinary exercises

All paths below are relative to the repository root. Read `.codex/standards.md`, `.codex/exercise-format.md`, `.codex/selection.md`, and the relevant parts of `Study notes/Prerequisite DAG.md`. Read relevant exercise feedback before choosing and designing the next exercise.

Create exercises in `Study notes/exercises/interdisciplinary/`. A single DAG node is sufficient; combine fields only when their interaction helps solve a real mathematical task. A change of vocabulary or an incidental example from a second field does not make an exercise interdisciplinary. Use the actual DAG node names in `dag_nodes` metadata and mark only fields meaningfully exercised.

Assume mathematical maturity and basic undergraduate notation, not mastery of a specialized subject. Select reusable definitions, lemmas, theorems, and concepts according to the shared selection policy. The existence of a vault note is not evidence that the user remembers its content.

## Construct the exercise

Start from a definite task with a checkable answer or rigorous solution, then identify precisely the ingredients needed to solve it. Work backward through their dependencies until the stated baseline suffices. Include only those ingredients in `Context`, but include them fully enough that no external lookup or missing intuition blocks the reader.

Give every object its kind and type; state what each operation takes and returns, and what each theorem assumes and permits the reader to conclude. Present unfamiliar tools with their legal uses, relevant intuition, and a small example when needed to understand how to apply them. Explain distinctions that could cause an otherwise reasonable reader to pursue an invalid interpretation. If a theorem is supplied for use, it may be stated as a given tool with its exact assumptions, conclusion, and mechanism; if proving it is the exercise, do not supply the proof as context.

The context supplies the ingredients; the problem leaves their useful composition for the reader to discover. Avoid irrelevant surveys, lists of possible techniques, and solution-shaped introductions. Deep topics are welcome when the context genuinely supports them. If the complete task would require too much new machinery to remain coherent, choose a bounded subproblem and label its scope honestly.

## Format and solution

Follow the shared template with exactly three top-level sections: `Context`, `Problem`, `Solution`. Preserve the editable `insight:` field immediately before `Solution` and the editable `feedback:` field; leave both empty on first creation. They are fields, not additional sections. Do not add hints, strategy classifications, takeaways, or bridge/source sections.

Place the entire solution inside one collapsed callout. Explain the composition of the supplied ingredients, justify every substantive step, and show why the result answers the precise problem. Restate necessary facts at their point of use when this prevents a gap. Include typed pseudocode when the task has an algorithmic component; otherwise use the mathematical derivation appropriate to the problem. The answer must not depend on looking up a linked page.

Perform a cold read of the context and problem without opening the solution: all symbols, objects, hypotheses, tools, and requested outputs must be understandable, while a meaningful task remains. Then verify the full solution against those exact supplies and assumptions. Correct any prerequisite or interpretation gap in the context rather than concealing it in the answer.

Update the interdisciplinary category index directly in `Study notes/exercises/`, and give each new content folder a corresponding navigable index. Preserve user insight and feedback during all revisions. Create only the requested exercises; installing this skill does not request an initial batch.
