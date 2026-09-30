# Codex study and research instructions

This repository supports a mathematically mature reader who knows basic undergraduate notation. Build understanding from precisely typed objects and a small, sufficient set of usable tools. Explain what a problem means before naming machinery.

## Scope and entry points

- The Obsidian vault is `Study notes/`. Its subject map is `Study notes/Prerequisite DAG.md`; scores are **(familiarity, interest)**. Scores guide teaching and selection, never excuse missing context.
- Exercises and research live under `Study notes/exercises/`. Start navigation at `Study notes/exercises/Exercises Index.md`.
- These are independent Codex instructions. Preserve `CLAUDE.md`, `.claude/`, Claude outputs, and all other Claude files. Do not import their old templates, scripts, or operating rules into this setup.
- Read `.codex/standards.md` before substantive content work, `.codex/feedback.md` and relevant user-written exercise feedback before selecting or revising material, and only the skill needed for the request.

| Request | Skill | Output folder within `Study notes/exercises/` |
| --- | --- | --- |
| Reconstruct algorithms/data structures or source contest problems | `.agents/skills/algorithmic-exercises/SKILL.md` | `algorithmic/` or `competitive_programming/` |
| Practice a DAG subject or combine subjects | `.agents/skills/interdisciplinary-exercises/SKILL.md` | `interdisciplinary/` |
| Rediscover a recent established result | `.agents/skills/frontier-rediscovery/SKILL.md` | `cutting edge/` |
| Learn a current research approach and begin an investigation | `.agents/skills/active-research/SKILL.md` | `active research/` |

## Nonnegotiable content requirements

1. **Correctness and self-containedness.** Supply every specialized definition, assumption, tool, and necessary intuition. Links provide optional depth; opening another page must not be necessary to understand an exercise. Derive the solution using only the declared baseline and supplied tools. Long context is acceptable when necessary.
2. **Types at first use.** Declare what each object is. For maps and algorithms give inputs, outputs, preconditions, and guarantees; for structures give stored data and operation signatures; for theorems give hypotheses and conclusions. Explain each symbol and all implicit parameters. Do not force non-functions into function notation.
3. **Minimality.** Keep everything required for reasoning and remove material that serves no role. Difficulty should arise from composing the supplied tools, not guessing terminology or an unmentioned theorem.
4. **Format and user ownership.** Follow `.codex/exercise-format.md`. Solutions start collapsed. Leave `insight:` and `feedback:` blank for the user; preserve their text exactly during revisions. No visible algorithm spoilers, convergent-strategy sections, sources/targets apparatus, bridges, or generated takeaways in ordinary exercises.
5. **Selection.** For interdisciplinary exercises follow `.codex/selection.md`: self-containedness first; favor widely reusable concepts and deep subjects just beyond current range; among similarly suitable candidates, underrepresentation outweighs interest. The second DAG score is interest. Instrumentally convergent topic selection does not reintroduce strategy sections.
6. **Navigation.** Every content folder created or worked on has a corresponding index of its direct pages and child-folder indexes, with parent navigation. Category indexes belong directly in `exercises/`, beside their folders. Research projects and prerequisite subfolders follow the same rule. Maintain indexes with content changes; do not launch an unrelated vault-wide indexing project.
7. **Research honesty.** Verify frontier claims and current research approaches from primary sources. Date status checks; distinguish proved results, conjectures, proposed experiments, and your own inferences. A rediscovery exercise reconstructs an established result; active research has no invented final solution.

## Work, feedback, and completion

Treat short requests as requests to complete the relevant workflow. Use the existing folder structure and index coverage. When a quantity is unspecified, choose a small coherent batch and state its scope; a routine exercise batch defaults to three exercises, while a frontier or active-research request defaults to one complete result or project. Do not expand a request into an indefinite curriculum.

Before each batch, inspect relevant `feedback:` fields and `.codex/feedback.md`. Correct the affected material and apply justified improvements to the narrowest appropriate Codex skill, template, or shared rule. Record the source, scope, and change in the feedback ledger. A one-exercise correction is not automatically a universal preference. Never edit the user's insight or feedback to make it agree with a solution.

For multi-session work, use `.codex/current-task.md` as the single task ledger: goal, scope, completed work, remaining work, sources/status dates, blockers, and a concrete next action. `Continue` resumes that action; it does not invent a new task when none is active. Historical files in `.codex/history/` are records, not instructions or active state.

Work locally by default. Commits, pushes, PRs, and merges follow the user's request; they are not completion prerequisites. Preserve unrelated edits and the user's requested folder moves. Do not configure credentials, change remotes, or install dependencies to write Markdown notes.

Before finishing, perform the content review in `.codex/standards.md`, update affected indexes and feedback/task state, run `pwsh -NoProfile -File .codex/setup.ps1`, and inspect the relevant diff. In Markdown tables, escape link/embed pipes as `\|`; an existing target alone does not make the rendered link valid. The script checks structure, table-link escaping, and file targets, not mathematical truth or rendered anchors; inspect changed anchors and callout nesting separately. Run `.codex/tools/test_validate_setup.ps1` when changing the validator. Report actual changes and remaining limitations accurately.

## Adding future workflows

New user requests may extend this system. Add a focused skill and a route above when a recurring new workflow warrants it; reuse shared standards and navigation, and add only genuinely new requirements. Apply specific feedback locally before enlarging global instructions. General study-note requests still use the shared standards and existing note organization without inheriting an exercise template.
