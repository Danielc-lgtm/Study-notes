---
name: active-research
description: Create or revise Obsidian research onboarding roadmaps using specific current approaches by named researchers, with self-contained prerequisite pages, feasible reproduction milestones, and bounded new investigations.
---

# Active research

Read the repository-relative `AGENTS.md`, `.codex/standards.md`, and `.codex/selection.md`. Use `Study notes/Prerequisite DAG.md` for subjects, interests, and explanation depth, with mathematical maturity and basic undergraduate notation as the baseline. Read the relevant existing research notes and user feedback before choosing or revising a direction; do not assume earlier conversations are accessible unless their content is present.

Write under the repository-relative `Study notes/exercises/active research/`, using a project folder when the topic needs multiple pages. Follow the shared index rules for every content folder created or modified. A project's navigable index may be its main roadmap; concept and prerequisite subfolders also need their own indexes. This skill governs research work when requested; installing it does not request new research content.

## Find a concrete way into the problem

Research current primary papers, authors' lectures, project pages, and repositories. Identify named researchers or groups and the specific mechanism of each relevant approach: what objects it acts on, what obstacle it addresses, what has worked, and what remains unresolved. Cite the evidence next to the associated claims and record an as-of date. Distinguish established results, conjectures, empirical findings, authors' stated plans, and your own inferences about promising next steps. Do not attribute an inferred proposal to a professor.

Select an approach with evidence that useful first steps are tractable for this reader: a reproducible calculation, proof, implementation, or experiment; accessible prerequisites and artifacts; realistic resource demands; and a bounded extension. Explain the evidence and remaining uncertainty. Confidence in an onboarding path is not evidence that its open endpoint will be solved. Where data, code, hardware, access, or background is missing, make the dependency explicit and adapt the first investigation to available resources.

Avoid a broad literature survey followed by a generic reading list. Choose a concrete research question, a justified approach, and the shortest sufficient route to doing meaningful work. A comparison of alternatives is useful when it explains that choice.

## Build the roadmap

The main page should make the following understandable without outside reading:

- The big-picture question, why it matters, and its typed mathematical or computational formulation.
- What is known, what precise obstacle remains, and how the chosen researchers' approach addresses that obstacle.
- The route from current understanding through required capabilities to reproducing a result and attempting a bounded new investigation.
- How the supporting pages fit together and which milestone each enables.

Organize the roadmap around concrete deliverables rather than lists of subjects to study. For each milestone specify:

| Item | Required meaning |
| --- | --- |
| Inputs | Objects, assumptions, data, code, and already completed milestones it consumes. |
| Output | A concrete proof, derivation, calculation, implementation, experiment, or counterexample, with its type and expected form. |
| Prerequisites | The exact concepts and tools needed, linked to the supporting pages that teach them. |
| Approach and reason | What to try and why it naturally addresses this obstacle. |
| Completion evidence | What checks show the deliverable is correct or the existing result has been reproduced; include resource needs when relevant. |
| Failure information | What a failed attempt would reveal, how to diagnose it, and a useful narrower next step. |
| Next milestone | What completing this one enables and how its output is used. |

Give an actionable first task. Connect at least one reproduction milestone to a bounded research question when the requested scope is research onboarding. Separate solved training/reproduction tasks from genuinely open investigations. Provide complete explanations for the former; for the latter provide hypotheses, experiments or proof plans, and evaluation criteria without fabricating a solution or promising success. If including exercise pages, also read and follow `.codex/exercise-format.md`.

## Teach the necessary details

Create linked concept and prerequisite pages only where their detail is needed. Each should explain its role in the roadmap, the objects and their types, the exact tools required, and how to use them in the research approach. For a theorem, provide hypotheses, conclusion, applicability checks, and the intuition needed to recognize its use. For a computational method, state input/output types, assumptions, guarantees, and concrete steps or pseudocode. For a physical or empirical model, explain measurable quantities, units where applicable, assumptions, and what would count as evidence against it.

Use small worked instances to make an abstract tool usable. Derive or explain the specialized steps on which the approach depends. Replace impressive-sounding terminology with the operation or claim it denotes. Keep only material that teaches a required capability or explains the research question; minimality concerns relevance, not page length.

Supporting pages may hold depth, but they must form a closed, navigable prerequisite path from the agreed baseline. No crucial explanation may end with an unexplained term, circular link, citation standing in for teaching, or an instruction to consult a textbook. At the point of use, summarize the tool's applicable inputs, assumptions, and output, then link to its complete explanation.

## Check before delivery

Audit backward from each milestone: can the reader understand the requested output, learn every necessary specialized tool from these notes, carry out the step with the stated resources, and recognize completion? Verify current research claims against the primary sources. Check that the open step is distinguished from established knowledge, the proposed extension follows from the reproduction work, links and folder indexes are navigable, and relevant feedback has informed the notes and applicable Codex instructions. Preserve the user's annotations.
