# Study Notes Codex Instructions

This repository is an Obsidian vault for long-term mathematical study. The goal is not merely to summarize source material, but to create notes from which a mathematically mature reader can rapidly recover context, understand why constructions are natural, and rederive results after months away from the subject.

These instructions are the permanent entry point for Codex. User prompts may therefore be very short. Infer the full workflow from this file and the repository documentation rather than requiring the user to restate it.

---

## 1. Read the repository specification first

Before creating or substantially rewriting study notes, read:

1. `CLAUDE.md`
2. `.claude/skills/polymath-notes/SKILL.md`
3. `.claude/skills/polymath-notes/references/templates.md`
4. `.claude/skills/polymath-notes/references/obsidian-patterns.md`
5. `.claude/skills/polymath-notes/references/prose-and-proof-standard.md`, and the thesis it points at, `prose/Chiang Sung En-Thesis.pdf` (extract with `pymupdf`) — the prose register and the minimum proof standard for every note
6. `.codex/note-quality.md`
7. `.codex/workflow.md`

The directory name `.claude` is historical. Its specifications are authoritative for Codex as well. The `.agents/skills/` directory contains pointer skills only, so that Codex's skill loader sees the same three skills; the content is in `.claude/skills/`.

For paper-specific notes, exercises, or other work covered by another skill in `.claude/skills/`, read that skill and its referenced files before working.

Do not copy these specifications into generated notes.

---

## 2. Interpret short user requests expansively

The user should not need to specify the mechanical workflow.

Examples:

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

Follow the writing rules in the polymath-notes skill. **The prose baseline is the owner's thesis, `prose/Chiang Sung En-Thesis.pdf`**, specified in `.claude/skills/polymath-notes/references/prose-and-proof-standard.md` Part I; read both before writing.

In particular:

- formal definitions and theorem statements are precise and conventional;
- explanatory material uses the thesis register: orient, motivate, state formally, unpack in the smallest concrete case, re-explain in a purpose-titled remark, close in words — in a measured first-person-plural academic voice, with every claim carrying its reason;
- motivate before formalizing;
- use concrete cases before abstraction when appropriate;
- prefer prose over bullets except for genuinely enumerative material;
- no generic LLM filler;
- no inspirational padding;
- no hedge stacking;
- do not merely paraphrase formulas;
- explain why each important construction or proof step has the form it does;
- mathematical notation follows the vault's LaTeX conventions.

Aim for the explanatory quality of the thesis's background and results chapters: expansive enough to re-explain every object in its smallest concrete case, rigorous enough to rely on later.

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

1. **Rigour.** Every theorem, lemma, proposition, and corollary that the unit
   *mentions* — on a concept map, on its own page, inside a proof, in a
   solution, in a definition's examples, in a bridge — carries a complete,
   fully rigorous proof on its own page (in its collapsible `Formal Proof`
   section, with the lemma decomposition feeding it), and every use of it
   elsewhere wikilinks that page and restates the statement at the point of
   use. **The thesis's fully written proofs are the minimum level of
   detail** (`prose-and-proof-standard.md` §6): named assumptions and goal,
   labelled blocks with bold lead-ins, a justification on every displayed
   line, every hypothesis invoked by name, clause-by-clause well-definedness,
   all directions and cases, a closing sentence in words. Every existing
   proof is audited line by line: no "clearly", "it is easy to see",
   "similarly", "sketch", or omitted case; every limit interchange,
   measurability, well-definedness, or convergence step is justified. A
   `Thm - X (Statement)` page, or a Formal Proof that is a sketch or a
   citation, is a defect to repair by writing the proof — never to
   preserve. The only result that may be used without proof is a genuinely
   book-length one, inside the `Imported without proof` callout and listed
   in the topic page's `# Imported Results`. Claims made in definition pages
   (examples, non-examples, corollaries, calibration checks) and in exercise
   solutions get the same treatment: a stated fact is either proved on the
   page or transcluded from the page that proves it. Comprehensive means all
   cases and all directions of an equivalence, not a representative one.
   `find-unproved-theorems.py` is the mechanical gate.

2. **Self-containedness.** Every page links or loads the context needed to
   understand it: every definition and theorem it uses is transcluded
   (`![[Def - X#The Definition]]`, `![[Thm - Y#Statement]]`) or briefly
   restated with a wikilink at the point of first use, every symbol is
   introduced on the page, and the prerequisite chain resolves through
   existing vault pages. The test is a cold read: a reader who opens only this
   page must be able to follow it, clicking links for depth but never for
   necessity.

3. **Explanation quality, with permission to replace.** The polymath-notes
   register (the thesis register: orient, motivate, state formally, unpack in
   the smallest concrete case, re-explain, close in words) remains the target. But when Codex's own default explanation of a
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
