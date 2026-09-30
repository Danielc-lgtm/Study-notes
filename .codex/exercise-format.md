# Exercise formats and navigation

Use these skeletons as authoring templates, replacing instructional placeholders. They are not exercises to publish. Folder paths here are repository-relative. Wikilinks in notes start within the `Study notes/` vault.

## Locations

| Mode | Content folder | Corresponding index in `Study notes/exercises/` |
| --- | --- | --- |
| `algorithmic` | `Study notes/exercises/algorithmic/` | `Algorithmic Index.md` |
| `competitive-programming` | `Study notes/exercises/competitive_programming/` | `Competitive Programming Index.md` |
| `interdisciplinary` | `Study notes/exercises/interdisciplinary/` | `Interdisciplinary Index.md` |
| `frontier-rediscovery` | `Study notes/exercises/cutting edge/` | `Cutting Edge Index.md` |
| Active research | `Study notes/exercises/active research/` | `Active Research Index.md` |

`Exercises Index.md` links all five category indexes. Every new subfolder receives an index under the same navigation rule in `standards.md`; an existing complete roadmap may act as its index. Keep filenames and titles neutral unless a named result/algorithm is explicitly requested.

When an index uses a Markdown table, write aliased links with an escaped pipe, for example `[[exercises/Algorithmic Index\|Algorithmic]]`. Ordinary `[[exercises/Exercises Index|Exercises]]` syntax remains correct in a prose parent link. Do not let table formatting split a link across columns.

## Metadata

Exercises use `type: exercise`, a `mode` from the first four rows, and `dag_nodes` listing exact DAG node titles stripped of display icons, score tuples, and status labels. Include only subjects actually exercised; metadata is for coverage, not speculative connections. `dag_nodes: []` is valid for algorithmic/contest problems without a meaningful DAG match. It is not valid for interdisciplinary/frontier exercises. Do not invent DAG nodes or link missing pages.

Optional metadata may include `created`, `updated`, and non-spoiling difficulty. Keep source/result/algorithm names that disclose the solution inside the collapsed solution rather than visible metadata. Do not add required tracking fields without a concrete use.

User-requested blank format previews use `type: format-preview` with the intended `mode` and `dag_nodes: []`. Clearly label them as placeholders, keep them indexed, and preserve the real format's headings, fields, and collapsed callouts. They are not exercises and must not count toward subject coverage. Actual exercises continue to use `type: exercise` and the DAG requirements above.

## Algorithmic and contest template

````markdown
---
type: exercise
mode: algorithmic
dag_nodes: []
---

# Neutral task title

## Problem

[Precisely defined objects, input and output types, all needed definitions,
constraints and edge cases, and any required performance target. For a data
structure give the operations and abstract behavior to implement.]

**insight:**

## Solution

> [!note]- Full solution
> [Self-contained explanation of the construction and why it works.]
>
> ```text
> [Typed pseudocode, including nontrivial subroutines.]
> ```
>
> [Correctness and justified time/space bounds. Compact attribution if sourced.]

**feedback:**
````

For contest exercises set `mode: competitive-programming`. No separate Context section, generated insight, hint, classification, strategy, bridge, or takeaway. Necessary context belongs in Problem. `feedback:` is supported for all exercise types so the same improvement loop applies.

## Interdisciplinary template

````markdown
---
type: exercise
mode: interdisciplinary
dag_nodes:
  - "Exact DAG node title"
---

# Neutral task title

## Context

[Minimal sufficient definitions, typed objects, assumptions, tools, and
intuition. Include physical meaning or units when relevant.]

## Problem

[A precise task solvable by composing the supplied tools.]

**insight:**

## Solution

> [!note]- Full solution
> [Complete derivation with hypotheses checked at their use.]
>
> [Compact source attribution or an accurate description as an original exercise.]

**feedback:**
````

The three unquoted `##` headings are exactly Context, Problem, Solution. Use prose, numbered subproblems, and local bold labels within them, not extra sections. The solution may contain internal structure within its callout. Pseudocode is included where the task calls for an algorithm, not artificially attached to a proof problem.

## Frontier additions

Use the interdisciplinary template with `mode: frontier-rediscovery`. The visible question is framed before the result's discovery. Context includes why the question is worth asking. In Problem, show each subproblem and why it is a natural next question. Follow each with its own collapsed approach and rationale:

```markdown
1. [Typed subproblem.] [Why this is a natural question.]

> [!note]- Approach to subproblem 1
> [Suggested method, why it is natural, and what it is expected to produce.]
```

Put these foldouts before `insight:`. They are the one deliberate exception to ordinary exercises having no advance hints. Do not require the reader to reveal the final solution to access them. The Full solution callout contains the complete chain to the actual result, its source/version/date, and a note identifying the route as a pedagogical reconstruction rather than a documented account of discovery. Reveal auxiliary guidance incrementally without inventing a historical narrative.

## Research pages

Active research is not bound to an exercise's three headings. Use a navigable main roadmap and focused concept/prerequisite subpages as specified by its skill. A project roadmap serving as a folder index has `type: index`, `role: research-roadmap`, and `indexed_folder`; supporting notes use `type: concept` as appropriate. Include a user `feedback:` field on the roadmap and preserve it. Actual exercises embedded in the project use the corresponding exercise template and remain separately self-contained.

## User fields and revision

Both fields belong to the user. They may contain several paragraphs or lists. Preserve their full contents and relative placement, not just the first line. Do not convert observations into generated takeaways or mark feedback processed by editing the feedback itself. Record handling in `.codex/feedback.md`. After a correctness fix, make the solution correction explicit without silently rewriting the user's historical reasoning.
