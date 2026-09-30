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

<<<<<<< HEAD
New user requests may extend this system. Add a focused skill and a route above when a recurring new workflow warrants it; reuse shared standards and navigation, and add only genuinely new requirements. Apply specific feedback locally before enlarging global instructions. General study-note requests still use the shared standards and existing note organization without inheriting an exercise template.
=======
- `Improve Complex Analysis II`
  means: locate that topic and all associated subpages, inspect relevant sources and neighbouring vault pages, perform the full rewrite and quality workflow, validate the resulting note graph, update persistent progress, and commit the completed work.

- `Improve all complex analysis notes`
  means: create or update a persistent multi-topic task plan, then work through every relevant topic sequentially in the same run, committing and merging each completed topic before immediately starting the next. Continue until the entire scope is complete or the platform interrupts the run.

- `Create notes on spectral sequences`
  means: locate supplied or repository sources, determine the correct vault location, inspect related notes and prerequisites, and create a complete topic according to the polymath-notes skill.

- `Continue`
  means: read `.codex/current-task.md`, `.codex/progress.json`, and recent relevant commits, then resume the recorded task from the exact next action.

- `Do the next batch`
  means: continue the current persistent task, complete exactly the next sensible atomic unit, and then stop. This is the explicit one-unit exception to the normal keep-going policy.

Prefer reasonable inference from repository context over asking the user to repeat information already recoverable from the repository.

Ask a question only when a genuinely consequential choice cannot be inferred safely.

---

## 3. Preserve the existing knowledge architecture

The vault's structure is intentional.

A topic normally consists of:

- a chapter or topic page giving the global conceptual map;
- a corresponding subfolder;
- atomic definition pages;
- theorem and lemma pages;
- examples;
- exercises and exercise indexes;
- Obsidian wikilinks and transclusions connecting these pages.

Treat the entire topic graph as the unit of understanding.

When rewriting an existing topic:

- preserve filenames unless renaming materially improves the knowledge architecture;
- preserve every correct and useful piece of existing content and all source coverage, integrating it into the best new structure rather than treating the old structure as fixed;
- preserve YAML frontmatter;
- preserve the topic/subpage architecture unless splitting, merging, adding, or reordering pages materially improves the knowledge architecture;
- preserve and improve cross-topic links;
- inspect associated definition, theorem, example, and exercise pages rather than editing only the topic page;
- make substantial changes only when they improve what the reader learns, the rigour, re-entry speed, or the ability to rederive the mathematics—not merely to produce a larger diff.

A rewrite is a **re-derivation of the whole topic from the sources and the
specification**, using the existing note as material rather than as the frame.
Codex is expected to restructure sections, reorder a concept map when the
source order is pedagogically wrong, split or merge subpages, add missing
definition/theorem/exercise pages, rewrite proofs from scratch when the
architecture is weak, replace explanations wholesale under priority P3, and
add examples, counterexamples, bridges, and exercises that the existing note
lacks. Radical means that the reader learns substantially more, more
rigorously, and can re-enter the topic faster; it never means change for its
own sake.

Before renaming any page, heading, or anchor, search the vault for incoming wikilinks and transclusions. Update every affected reference.

Never knowingly leave broken wikilinks or transclusions.

---

## 4. Quality objective

The standard is substantially higher than "correct summary."

A strong note should make it possible to reconstruct mathematics from a relatively small number of conceptual handles while retaining full technical detail.

Every substantial topic should answer, where relevant:

- What problem motivates this construction?
- Why is the definition shaped this way?
- What is the intuitive picture before the formal statement?
- What is the true name or operational characterization of the concept?
- What are the legal operations available once this object is present?
- What is the input type of the main theorem or technique?
- What other situations can be transformed into that input type?
- What trigger-reaction patterns should become automatic?
- Where do important properties come from or get inherited from?
- Is there a local-to-global mechanism?
- What is the abstract object and what is merely a representation?
- What obstruction or counterexample explains why the hypotheses are needed?
- What is the key step that makes the proof work?
- What neighbouring subjects instantiate the same pattern?

Do not force every category onto every page. These are questions for constructing insight, not a rigid template.

A longer rewrite is not automatically a better rewrite. Added material should increase correctness, understanding, rederivability, useful connections, or self-containedness.

---

## 5. Writing standard

Follow the writing rules in the polymath-notes skill.

In particular:

- formal definitions and theorem statements are precise and conventional;
- explanatory material uses flowing, mathematically mature prose;
- motivate before formalizing;
- use concrete cases before abstraction when appropriate;
- prefer prose over bullets except for genuinely enumerative material;
- no generic LLM filler;
- no inspirational padding;
- no hedge stacking;
- do not merely paraphrase formulas;
- explain why each important construction or proof step has the form it does;
- mathematical notation follows the vault's LaTeX conventions.

Aim for the explanatory quality of excellent mathematical lecture notes: conversational enough to expose the thought process, rigorous enough to rely on later.

---

## 6. Source discipline

For substantive mathematical work:

1. inspect the source material available in the repository;
2. inspect the current note;
3. inspect relevant prerequisite and neighbouring notes;
4. use additional authoritative sources when the existing sources are insufficient and network access is available.

Do not silently replace a source's claim with a different theorem.

When sources differ in conventions, hypotheses, or level of generality, resolve the distinction explicitly where pedagogically relevant.

The goal is not source imitation. Reconstruct the best explanation consistent with the mathematics and source material.

---

## 7. Existing-note rewrite protocol

Before editing a topic, diagnose it and envision the best version it could
become.

Look specifically for:

1. mathematical errors or imprecision;
2. unexplained notation;
3. definitions without motivation;
4. theorem statements whose significance is unclear;
5. proofs with hidden steps;
6. weak or missing "why should this be true?" explanations;
7. missing operational or true-name interpretations;
8. missing legal operations and trigger-reaction patterns;
9. missing examples or counterexamples;
10. poor ordering of intuition and formalism;
11. weak prerequisite recall;
12. weak connections to neighbouring notes;
13. content that is technically complete but difficult to re-enter after months away.

The diagnosis is a floor, not a ceiling. After finding defects, write a target
description of the ideal topic graph: its structure, unifying frame, true
names, proof architecture, examples, counterexamples, bridges, and exercises.
Compare the existing unit with that target and with the gold-standard vault
subjects. Every gap is work even when the existing note has no visible defect.
The target is the best note Codex can write from the sources and specification
today, subject to preserving correct useful content and complete source
coverage.

Do not preserve weaknesses merely because they occur in the existing note.
Do not declare a clean diagnosis complete without performing the target
comparison. Ambition operates inside the unchanged order P1 rigour, P2
self-containedness, P3 explanation, then P4 conciseness.

### Rewrite priorities

When rewriting existing notes, three dimensions take precedence over every
other improvement and are diagnosed and fixed first, in this order:

1. **Rigour.** Every theorem, lemma, proposition, and corollary page carries a
   complete, fully rigorous proof (in its collapsible `Formal Proof` section,
   with the lemma decomposition feeding it). Every existing proof is audited
   line by line: no "clearly", "it is easy to see", "similarly", or omitted
   case that a careful reader could not expand in under a minute; every
   hypothesis used is named at the point of use; every limit interchange,
   measurability, well-definedness, or convergence step is justified. Claims
   made in definition pages (examples, non-examples, corollaries, calibration
   checks) and in exercise solutions get the same treatment: a stated fact is
   either proved on the page or transcluded from the page that proves it.
   Comprehensive means all cases and all directions of an equivalence, not a
   representative one.

2. **Self-containedness.** Every page links or loads the context needed to
   understand it: every definition and theorem it uses is transcluded
   (`![[Def - X#The Definition]]`, `![[Thm - Y#Statement]]`) or briefly
   restated with a wikilink at the point of first use, every symbol is
   introduced on the page, and the prerequisite chain resolves through
   existing vault pages. The test is a cold read: a reader who opens only this
   page must be able to follow it, clicking links for depth but never for
   necessity.

3. **Explanation quality, with permission to replace.** The polymath-notes
   register (motivation before formalism, concrete before abstract, the prose
   voice of the exemplars in `prose/` — the thesis and *Linear Algebra Done
   Right*) remains the target. But when Codex's own default explanation of a
   construction or proof is clearly superior to the existing note's — clearer
   mechanism, better-chosen example, more honest about what is hard, tighter
   route to the result — Codex replaces the existing explanation rather than
   patching it. "Clearly superior" means a reader would learn more, or more
   correctly, from the new text; it does not mean merely different. Record the
   judgement in the diagnosis in one line. Formal statements stay conventional
   regardless; the freedom is in the explanatory prose, proof architecture,
   and choice of examples.

4. **Conciseness without loss.** After the three above are satisfied, tighten
   the prose: remove repetition, throat-clearing, restated formulas, sentences
   that only announce the next sentence, and explanations of the same point
   made twice in different words. The constraint is strict: a cut is allowed
   only if no mathematical content, no case, no justification, no example, and
   no connection is lost. Comprehensiveness (every source item covered) and
   completeness of proofs are never traded for length; the target is the
   shortest text that still says everything. Structure — collapsible
   callouts, subpages, transclusion — is the preferred way to make a page feel
   short; deletion is the last resort and only for text that carries nothing.

These four are the definition of a successful rewrite. Insight sections,
bridges, unlocks, and exercise supplementation are improved after them, never
instead of them.

---

## 8. Review every completed topic

Before declaring a topic complete, perform separate passes.

### Correctness pass

Check definitions, hypotheses, equations, proof steps, notation, examples, and claims.

### Pedagogy pass

Check whether motivation precedes machinery and whether a reader can recover the conceptual picture.

### Rederivation pass

Identify the minimal high-leverage ideas from which the formal development can be reconstructed. Strengthen the note where these are missing.

### Knowledge-graph pass

Check filenames, YAML, wikilinks, transclusions, prerequisite links, atomic subpages, and topic-page consistency.

### Prose pass

Remove generic AI prose, unnecessary repetition, vague transitions, and explanations that merely restate notation.

Apply fixes discovered during review. Do not merely report them.

Use `.codex/note-quality.md` as the detailed review standard.

---

## 9. Long-running tasks and persistence

Never rely on conversational memory for a multi-session project.

Persistent task state lives under `.codex/`.

For any task that may require more than one Codex run:

1. read `.codex/current-task.md`;
2. read `.codex/progress.json`;
3. inspect recent relevant Git commits;
4. resume from the recorded next action.

When beginning a new large task, update the current-task and progress files to describe that task.

Work on one atomic unit at a time.

For vault-wide rewrites, the default atomic unit is one complete topic and its associated subpages.

Never intentionally leave many topics simultaneously half-rewritten.

Completing one unit is not a reason to end a run. After a unit passes review,
is committed, pushed, and merged, immediately begin the next unit from the
updated `main` in the same run. Continue through the ledger until every unit in
scope is complete or the platform interrupts the run. Never end a run
voluntarily while units and working budget remain, and never ask “should I
continue?” when the ledger already supplies the next action. `Do the next
batch` is the explicit user request that limits a run to one unit.

**The continuation check controls whether Codex may answer, not merely what it
should do after a merge.** Before sending any user-facing final or progress
report, reread both ledgers. If an in-scope unit remains and the execution
environment still accepts tool calls, sending that report is prohibited:
perform the recorded next action instead. A clean checkpoint, a merged PR, the
completion of a review pass, or the availability of a useful progress summary
does not count as an interruption. “The platform interrupts the run” means an
actual external cutoff that prevents another tool call, not an anticipated
limit, elapsed effort, or a convenient response boundary.

If the platform explicitly signals an imminent hard cutoff but still permits a
final checkpoint tool call:

- bring the current atomic unit to a coherent state if feasible;
- run the required review;
- update `.codex/progress.json`;
- update `.codex/current-task.md` if the plan or next action changed;
- commit durable progress.

If the current unit genuinely cannot be finished, record precisely:

- what is complete;
- what remains;
- any unresolved issue;
- the exact next action.

A fresh Codex task must be able to continue solely from the repository.

If the same unit remains in progress across three runs, the next run must
split it: finish and merge the pages already at standard as a smaller coherent
unit, and record the remainder as a new unit. Do not let one oversized unit
remain open-ended indefinitely.

---

## 10. Git and PR workflow

Exact commands live in `.codex/workflow.md`. Read it and run its preflight
(`gh auth status`, `git fetch origin`) at the start of every run. The environment
is pre-authenticated by `.codex/setup.sh`; if preflight fails, report the
misconfiguration (see `.codex/README.md`) instead of improvising credentials.

Policy — **auto-merge per completed unit**:

`main -> codex/<slug> branch -> complete one atomic unit -> commit -> push -> PR -> merge into main immediately -> next unit on a fresh branch from main`

- Never commit on `main` directly; never force-push. Every change reaches
  `main` through a pull request, but the user never has to click anything: Codex
  opens the PR and merges it itself (`gh pr merge --merge --delete-branch`) as
  soon as a unit passes the final checklist in `.codex/note-quality.md`.
- One PR per completed unit. Its title is the unit's commit message, for example
  `Improve Complex Analysis II: Cauchy theory and theorem pages`.
- An *unfinished* unit is never merged. If a run ends mid-unit, checkpoint it on
  its branch, push, leave the PR open, and record the branch in
  `.codex/current-task.md`; the next run resumes that branch, finishes the unit,
  and merges.
- Because every completed unit lands on `main`, the persistent task state in
  `.codex/` is always on `main` too; a multi-topic task simply continues from
  `main` with a new branch for each unit. Nothing about the plan is lost between
  merges.
- The user can override for one task with `... without merging` (leave PRs
  open) or `... directly on main` (skip PRs; commit and push to `main`).

When—and only when—the continuation check permits a run to end, tell the user
which units were merged (PR numbers), what remains, the exact next action, and
whether an unfinished unit was left on an open branch.

---

## 11. Definition of done

A topic is complete only when:

- the mathematics has passed correctness review;
- the conceptual explanation has materially improved or already meets the standard;
- associated atomic pages are consistent with the topic page;
- useful existing material has not been accidentally lost;
- links and transclusions remain valid;
- formatting follows vault conventions;
- no temporary planning text has leaked into study notes;
- persistent progress state has been updated;
- the completed unit has been committed.

A large task is complete only when:

- every planned unit is complete;
- a final cross-topic consistency review has been performed where appropriate;
- `.codex/current-task.md` and `.codex/progress.json` record completion;
- all durable work is committed;
- the working branch is ready to merge.

After any individual topic becomes complete, begin the next planned topic in
the same run as soon as its PR is merged. A run is finished only when no work
remains in scope or the platform interrupts it; one completed topic is never a
voluntary stopping condition when units and budget remain.

The objective is not to maximize the amount Codex changes.

The objective is to leave behind study notes that are more correct, more insightful, easier to re-enter, and more useful for reconstructing the mathematics.
>>>>>>> 07178865721f37b92e440e4fcc87a187f95a1021
