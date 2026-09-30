# Shared content standard

Applies to all four Codex workflows and future study-note work. Templates are in `exercise-format.md`; topic selection is in `selection.md`. Paths beginning `Study notes/` are repository-relative; Obsidian links are vault-relative.

## Reader and self-containedness

Assume mathematical maturity and basic undergraduate notation, not mastery of an undergraduate syllabus. Do not infer specialist knowledge from a familiar-looking symbol, an anchor in the DAG, an existing note, or an advanced topic request.

For every exercise and solved training/reproduction task, first work out a correct solution and trace its dependencies backward. For an open investigation, trace the prerequisites of the proposed approach and milestones without assuming a known solution. Put each required specialized definition, theorem, allowed operation, convention, and assumption into Context (or the algorithmic Problem, or the appropriate research page). Recursively explain specialized objects occurring inside those tools. Stop at the agreed baseline. No glossary entry should itself contain unexplained specialist language.

A usable supplied theorem has precise hypotheses and conclusion, the meaning of its objects, an explanation of what it lets the reader do, and enough mechanism/intuition to use it. Include a small application or boundary example when otherwise its use would remain mysterious. Prove auxiliary claims made by the explanation. A substantial background theorem may be explicitly supplied as a tool without proving its entire general theory; never hide the exercise's target result inside that allowance or assume a stronger theorem than was stated.

Context supplies primitives and tools; the exercise leaves their composition to the reader. A toolkit with only one relevant theorem can still demand serious reasoning. Avoid lengthy catalogues of unused alternatives. If the route is too large for one exercise, build a coherent sequence of separately self-contained exercises instead of skipping dependencies. For frontier reconstructions, retain a complete route to the specified result and clearly identify any intermediate toy model.

Research roadmaps may use linked prerequisite subpages for depth. Explain the immediate concepts on the roadmap and specify exactly what to read before each milestone. Each subpage stands on its own at the same baseline, with essential prerequisite statements inline or embedded. The full local project must supply the learning path without requiring outside reading; citations remain verification and optional depth.

## Type and meaning discipline

Introduce types next to objects at first use, including inside pseudocode and solutions. Prefer a short local declaration over a detached notation dump.

| Object | Required contract |
| --- | --- |
| Function/operator | Domain, codomain, input parameters, assumptions, result and interpretation. Distinguish a function from its value. |
| Algorithm | Typed input/output, valid instances, failure/no-solution output, computational model where relevant, correctness guarantee. |
| Data structure | Abstract represented state; `build`, `query`, `update`, etc. with argument/result types and state changes; invariants and justified costs in the solution. |
| Space, measure, relation, category, distribution, etc. | What kind of object it is, underlying data and constraints, elements/arguments, and relevant operations. Explain random variables versus their laws, objects versus representations, and analogous distinctions when they occur. |
| Theorem/lemma | Typed parameters + hypotheses imply a precise conclusion. Distinguish existence from an effective construction; specify uniqueness, error, probability, or regularity when claimed. |
| Research method | Given data/assumptions/resources, what artifact or evidence the method produces, and what that evidence establishes or does not establish. |

Explain a problem in ordinary language alongside necessary formal precision. Names such as "duality", "renormalization", or "functoriality" cannot substitute for saying which objects are transformed, which property is preserved, and why that helps. Use conventional notation once defined; avoid artificial technical vocabulary.

## Solutions and provenance

Write a complete solution, not an answer key or a high-level sketch. Justify the nontrivial transitions and each theorem application. For algorithms include unambiguous typed pseudocode, initialization, edge cases, termination where relevant, correctness, and time/space analysis with the appropriate worst-case, amortized, or expected qualifier. Define and explain any nontrivial subroutine; do not conceal the hard part behind a library name.

All solution-specific reasoning for ordinary exercises stays inside the solution callout. A requested named-algorithm exercise may use that name; otherwise use neutral titles, metadata, and index descriptions. Context may state usable background results but must not announce the target algorithm or the trick that solves the problem.

Use primary sources for contest statements/editorials, mathematical results, and research status. Open and inspect the supporting source; search snippets are not verification. Preserve assumptions, restrictions, version dates, and the distinction between an original and an adapted exercise. Give compact attribution inside the collapsed solution where it could spoil discovery. Do not copy lengthy copyrighted problem text; write a faithful self-contained reformulation. If no official solution exists, verify your own solution and identify it as independently derived.

For frontier/current research, verify recency and status at creation or substantive update and record the check date. Distinguish the original result date from the date checked. Do not infer that a question remains open merely from an old paper. When verification is unavailable, label the specific uncertainty and avoid a claim of confirmed current status. Separate evidence of a tractable starting task from confidence in solving the open problem.

## Obsidian and indexes

Use Markdown and `$...$`/`$$...$$` math. Define every variable; use supported MathJax notation. Keep math out of wikilink targets/aliases. Use `[[vault/path/Page|Readable name]]` links and `![[vault/path/Page#Heading]]` only for existing targets, with precise anchors. A link alone never supplies required context. Restating a short result is often clearer than embedding a large page.

Inside Markdown tables, escape every pipe belonging to a wikilink alias or embed argument: `[[vault/path/Page\|Readable name]]` and `![[image.png\|200]]`. An unescaped pipe becomes a column boundary and breaks the link even when its target file exists. Outside tables, keep ordinary `[[Page|Label]]` syntax. Check both Markdown structure and target resolution; a filename-only check cannot establish that a link renders correctly. This follows [Obsidian's table formatting rules](https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax).

Use collapsed Obsidian callouts (`> [!note]- Title`), not HTML details. Every line of a callout, including blank lines, fenced pseudocode, and display equations, carries the proper quote prefix. Nested callouts add another `>`. Use headings outside callouts only as the relevant template permits.

Keep filenames portable on Windows; avoid `< > : " / \\ | ? *` in names. Preserve existing user content and useful links. Before renaming pages or headings, find incoming links and repair them in the same change.

Every managed content folder has one corresponding index, normally in its parent, with `type: index` and `indexed_folder: "vault/relative/folder"`. The top exercise folder uses `exercises/Exercises Index.md` to index itself. An existing suitable topic/roadmap page can serve as the index if it declares the folder and covers its pages. Research roadmap indexes use `type: index` and may additionally use `role: research-roadmap`.

Index direct Markdown pages other than the index itself and link each child folder's index. Include a parent-index link and a short neutral description of each page or group; an empty index states that there are no pages yet. Large indexes may group by topic or stage but must not omit pages. Avoid duplicate index documents for the same folder. Exclude hidden/tool folders and attachments from the content-folder rule; link relevant attachments from their consuming notes. Do not display solutions, method tags, or personal feedback in exercise indexes.

## Review before completion

- **Correctness:** independently check the result, assumptions, examples, proof, pseudocode, and complexity as relevant. Use small computational checks when they resolve an actual uncertainty.
- **Cold read:** starting with the agreed baseline, resolve every symbol and tool without external lookup. Verify the reader has enough intuition to use each tool; a hyperlink or theorem name is not enough.
- **Minimality:** every context item has a role; no omitted prerequisite is disguised as brevity. Preserve the reasoning task.
- **Spoilers and ownership:** collapsed content is properly contained; no hidden-method clues in ordinary titles/index entries; user insight and feedback remain intact.
- **Navigation:** every changed content folder has a current index; links and transcluded headings exist. Run `.codex/setup.ps1` for structure, table-link escaping, and file targets; inspect anchors separately. When changing the validator, run `pwsh -NoProfile -File .codex/tools/test_validate_setup.ps1` to exercise valid and invalid table-link cases.

Mathematical and pedagogical review is judgment, not a regex test. Use an independent reviewer for substantial frontier reconstructions or complex research plans when useful; address actual issues rather than demanding an ornamental review pass.
