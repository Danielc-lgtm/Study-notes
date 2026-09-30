# Codex setup

Open `C:\Users\Owenh\Documents\Study-notes` as the Codex project and its `Study notes/` folder as the Obsidian vault. Start at `exercises/Exercises Index` in Obsidian. Content is plain Markdown; no plugin or package installation is needed.

## Files

| File or folder | Purpose |
| --- | --- |
| `../AGENTS.md` | Always-on requirements, routing, feedback loop, and extension policy. |
| `config.toml` | Project setting requesting live web search for current sources. |
| `standards.md` | Shared type, self-containedness, correctness, source, and navigation standard. |
| `exercise-format.md` | Exact exercise templates, metadata, user fields, and folder mapping. |
| `selection.md` | Interdisciplinary selection using DAG reuse, readiness, coverage, and interest. |
| `feedback.md` | Traceable record of feedback-driven improvements. |
| `current-task.md` | Single lightweight ledger for work that spans sessions. |
| `../.agents/skills/` | Four independent, automatically discoverable workflow skills. |
| `setup.ps1` and `tools/validate_setup.ps1` | Read-only structure and file-link validation. |
| `tools/test_validate_setup.ps1` | Isolated regression tests for rendered table-link syntax and target checks. |
| `history/` | Preserved earlier research/task records; never loaded as current instructions. |

## Example requests

- "Give me three algorithm reconstruction exercises, including an advanced data structure."
- "Find three competitive programming exercises."
- "Choose the next three interdisciplinary exercises using my DAG and current coverage."
- "Turn a recent result in a subject just beyond my range into a rediscovery exercise."
- "Build an active-research onboarding project around a documented approach to [problem]."
- "Read my exercise feedback and improve the relevant instructions and notes."
- "Continue." Resumes the concrete next action only when a task is active.

Named skills can also be invoked directly: `$algorithmic-exercises`, `$interdisciplinary-exercises`, `$frontier-rediscovery`, `$active-research`. General note work follows shared standards without adopting an exercise template.

## Validation and activation

From the repository root, run:

```powershell
pwsh -NoProfile -File .codex/setup.ps1
```

This checks the required files, skill metadata, exercise section structure, collapsed solutions, index coverage, table-link escaping throughout the vault, and managed-note wikilink file targets. Aliased links in tables require `\|`, for example `[[exercises/Algorithmic Index\|Algorithmic]]`; ordinary prose links use `|`. The validator accepts the escaped form and rejects links that a table would split across columns. It does not install anything, change global configuration or Git state, prove mathematics, or test rendered heading/block anchors. Content and anchor review remain part of the authoring workflow. `-ConfigOnly` limits checking to the configuration when staging a replacement.

When changing the validator, run `pwsh -NoProfile -File .codex/tools/test_validate_setup.ps1`. These tests use isolated fixtures and include the original master-index failure.

Project settings apply when Codex trusts the project; start a new task/session in this repository so its root instructions are loaded. Existing higher-priority environment settings still apply. Model choice and access permissions are inherited. The live-search setting is documented in [OpenAI web-search guidance](https://learn.chatgpt.com/docs/web-search); project configuration precedence is documented in [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic).

## Replacement and extension

The former Claude-pointer skills, cloud Git bootstrap, automatic merge workflow, and duplicate active ledgers have been retired. Claude files remain independent and unchanged. Earlier research/task records are preserved under `history/`; this directory is deliberately excluded from operational loading.

Keep future capabilities modular: add a focused skill, link it from `AGENTS.md`, and reuse shared standards, formats, feedback, and navigation. Add a new template only when the new task actually requires a different output. Do not accumulate duplicated instructions across all skills.
