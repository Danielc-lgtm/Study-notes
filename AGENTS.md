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
5. `.codex/note-quality.md`
6. `.codex/workflow.md`

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
  means: create or update a persistent multi-topic task plan, then work through the relevant topics sequentially. Finish complete topics rather than leaving many half-edited.

- `Create notes on spectral sequences`
  means: locate supplied or repository sources, determine the correct vault location, inspect related notes and prerequisites, and create a complete topic according to the polymath-notes skill.

- `Continue`
  means: read `.codex/current-task.md`, `.codex/progress.json`, and recent relevant commits, then resume the recorded task from the exact next action.

- `Do the next batch`
  means: continue the current persistent task and complete the next sensible atomic unit.

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
- preserve useful existing content;
- preserve YAML frontmatter;
- preserve the topic/subpage architecture unless there is a substantive reason to change it;
- preserve and improve cross-topic links;
- inspect associated definition, theorem, example, and exercise pages rather than editing only the topic page;
- do not regenerate content merely to make it stylistically different.

A rewrite should be semantic refactoring, not gratuitous regeneration.

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

Before editing a topic, diagnose it.

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

Then improve the topic based on that diagnosis.

Do not preserve weaknesses merely because they occur in the existing note.

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

Before a run ends:

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

---

## 10. Git and PR workflow

Exact commands live in `.codex/workflow.md`. Read it and run its preflight
(`gh auth status`, `git fetch origin`) at the start of every run. The environment
is pre-authenticated by `.codex/setup.sh`; if preflight fails, report the
misconfiguration (see `.codex/README.md`) instead of improvising credentials.

Policy:

`main -> codex/<slug> task branch -> one commit per completed atomic unit -> one PR -> merge when the overall task is complete`

- Never commit on `main` directly; never force-push.
- Each completed atomic unit gets its own descriptive commit, for example
  `Improve Complex Analysis II: Cauchy theory and theorem pages`.
- Push after every unit and keep exactly one open PR per task; subsequent runs
  continue the same branch and PR (recorded in `.codex/current-task.md`).
- Merge into `main` (`gh pr merge --merge --delete-branch`) only when the
  overall task is complete per §11, or when the user explicitly asks to merge.
  A plain instruction such as "do X" without "merge" means: finish X, open or
  update the PR, and report the link. "Do X and merge" means: do X, then merge
  it yourself; the user does not want to click anything on GitHub.

If the user explicitly asks to merge before the overall task is complete:

1. make sure all current durable progress and `.codex` state are committed;
2. merge the PR into `main`;
3. preserve the unfinished task state in `.codex`;
4. for subsequent continuation, start from the updated `main` branch;
5. create a new working branch and PR for the remaining work;
6. resume from the recorded next action.

Because `.codex/current-task.md` and `.codex/progress.json` are committed, merging
an intermediate PR must not lose project state. Never assume conversational
memory will bridge a merge.

Always end a run by telling the user the PR URL, what was completed, what
remains, and whether the PR was merged.

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

The objective is not to maximize the amount Codex changes.

The objective is to leave behind study notes that are more correct, more insightful, easier to re-enter, and more useful for reconstructing the mathematics.