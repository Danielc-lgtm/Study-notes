# Codex feedback ledger

Before selecting or revising content, read relevant user `feedback:` fields in `Study notes/exercises/` and this ledger. For cross-topic selection, include unhandled feedback across the exercise collection. Preserve each user's field verbatim in its source note.

For an actionable item, record the source path, a faithful short quotation or summary, the scope (one exercise, one workflow, or shared preference), the corrective change and files affected, and status/date. Re-read the current source text before acting; a changed field may contain new feedback. Use a stored quotation or content fingerprint to distinguish revisions from already-handled text.

Apply clear corrections and requested preferences within the authorized Codex setup. Resolve ambiguous local feedback by the narrowest supported change; ask only if materially different interpretations remain. Never infer a new global rule from a single local complaint. User insight can inform teaching, but is not permission to rewrite personal notes or establish an unrelated preference.

## Applied preferences

- **2026-09-28 — initial setup, user conversation.** Baseline: mathematical maturity plus basic undergraduate notation. Extreme self-containedness takes precedence over compact length and subject depth. Types and operational meaning are explicit throughout.
- **2026-09-28 — initial setup, user conversation.** Frontier subproblems and motivation are visible; each proposed approach and rationale is collapsed separately. Solutions are collapsed; insight/feedback fields remain user-owned.
- **2026-09-28 — initial setup, user conversation.** Prioritize instrumentally reusable concepts and suitably advanced subjects; underrepresentation weighs more strongly than interest. DAG tuples are (familiarity, interest). Implemented in `selection.md` and the interdisciplinary skill.
- **2026-09-28 — initial setup, user conversation.** Every managed content folder needs navigable indexing. Exercises now live inside the `Study notes/` vault. Implemented in `exercise-format.md`, `standards.md`, and category indexes.

## Exercise feedback

- **2026-09-28 — fixed; user conversation, master exercise index.** Report: "The linking for the master exercise index isn't working, fix, check any similar errors, and make sure it doesn't happen again." Cause: unescaped alias pipes inside a Markdown table split links into separate columns; the original validator resolved target filenames without checking that syntax. Corrected the five master-table links and two matching table links in `Study notes/Geometry/Differential Geometry/Differential Geometry VII/Def - Tensor Bundle.md`. The audit covered 3,231 vault Markdown files. Documented the table-specific escaping rule in `AGENTS.md`, `standards.md`, and `exercise-format.md`, and added vault-wide table checks plus positive/negative regression cases. Scope: Markdown table link/embed formatting; ordinary prose aliases remain unchanged.
