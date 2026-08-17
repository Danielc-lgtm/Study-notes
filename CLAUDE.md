# Study Notes — Obsidian Vault

This is a polymathic study system: an Obsidian vault of interlinked mathematical study notes covering approximately 130 subjects simultaneously, organized via a prerequisite DAG.

## Owner Background

The user has strong background in: applied math (PDEs, fluids, dynamical systems, math finance, numerical analysis), pure analysis (functional analysis, PDE analysis, SDEs), geometric mechanics, statistical mechanics, quantum mechanics, fluid dynamics, information theory, differential/Riemannian geometry, Bayesian networks/causality, algorithmic information theory (AIT).

Weaker areas: algebra (most neglected), some physics curriculum gaps, computational complexity and lambda calculus (forgotten from undergrad), no formal economics background.

Active research areas: ontology identification (AIT + reusable function pointers), information-theoretic emergence of continuity, Bayesian ontology shifts, meta-learning/metacognition, continuous dynamic Bayesian nets, decision theory (UDT, program equilibrium), Maxwell's demon in algorithmic thermodynamics.

## Prerequisite DAG

The study system is organized via a prerequisite DAG maintained in Notion:
- **DAG page:** https://www.notion.so/35bf76ffda148143abcad0be3ca296f4

This DAG tracks ~130 subjects with prerequisite dependencies, synergy clusters, and (familiarity, interest) scores. When creating notes, use the DAG to:
- Identify what the current topic unlocks downstream ("aim just above range")
- Find cross-subject connections for the Bridges section
- Determine what prerequisites the reader can be assumed to know

If the Notion MCP is connected, fetch the DAG page directly. Otherwise, ask the user for relevant DAG context.

## Vault Structure

```
[repo root]/
  CLAUDE.md                        # this file
  .claude/                         # Claude Code skills
    skills/
      polymath-notes/              # chapter-level study notes from textbooks
        SKILL.md
        references/
          obsidian-patterns.md
          templates.md
      exercise-builder/            # practice exercises / drills
      paper-notes/                 # self-contained notes from a single paper
        SKILL.md
        references/
          notation-discipline.md
          companion-page-template.md
          recall-callouts.md
          atomic-note-templates.md
          obsidian-patterns.md     # symlink to polymath-notes' copy
  paper_source/                    # source PDFs for paper-notes (incl. the reference thesis)
  Study notes/                     # the Obsidian vault
    [Subject Area]/                # e.g., Algebra/, Analysis/, Geometry/
      [Subtopic]/                  # e.g., Group Theory/, Functional Analysis/
        [Topic Page].md            # chapter-level topic page
        [Topic Name]/              # subfolder for that topic's subpages
          Def - [Name].md
          Thm - [Name].md
          Lemma - [Name].md        # atomic lemma note (paper-notes; Thm-shaped)
          Ex - [Name].md
          Exercise Index - §X.Y.md
    Papers/                        # paper-notes output
      [Short Title]/
        Paper - [Short Title].md   # companion page (reading surface)
        Def - [Name].md            # paper-result stubs → link back to companion
        Thm - [Name].md
    .obsidian/                     # Obsidian configuration
```

## Conventions

### Formatting
- **LaTeX:** `$...$` for inline math, `$$...$$` for display math. Every variable, symbol, and equation in prose must be in LaTeX — no bare Unicode math symbols.
- **Internal links:** Obsidian wikilinks `[[Def - Group]]` or `[[Def - Group|group]]` with display text. Links work across folders by filename; use full paths only to disambiguate.
- **Transclusion:** `![[Def - Group#The Definition]]` to embed sections from other pages inline. Preferred for Recall sections in exercises.
- **Collapsible sections:** Obsidian collapsible callouts `> [!note]- Title` (collapsed by default) for proofs, lemmas, hints, and worked solutions; foldable parent/child bullets for the concept map. Do not use HTML `<details>` tags — they do not collapse reliably in Reading view, and wikilinks placed inside HTML are not clickable.
- **Callouts:** `> [!note]`, `> [!tip]`, `> [!warning]` for exercise index links, unlocked concepts, and illegal-but-tempting operations.
- **YAML frontmatter:** Required on every page. Fields: `type`, `subject`, `tags`, `prereqs`, and `difficulty` (exercises only).

### File Naming
```
Def - [Concept Name].md
Thm - [Theorem Name].md
Ex - [Short Description].md
Exercise Index - §X.Y [Section Title].md
[Topic Name].md
```

### Writing Style
Two registers: formal for definitions and theorem statements; David Tong lecture-note style (conversational, precise, concrete-before-abstract) for everything else. Prose over bullets. No abbreviations. No hedge stacking. Not inspirational — write the explanation that makes insight visible.

### Git Workflow
After creating or modifying study notes, always commit with a descriptive message summarizing what was added (e.g., "Add Measure Theory I — §2.1–2.3: 8 definitions, 4 theorems, 6 exercises"). Push when the user requests it.

## Skills

Three skills build vault content. Each has its own `SKILL.md` and `references/`; read a skill's spec before invoking it.

**`.claude/skills/polymath-notes/`** — the full specification for creating chapter-level study notes from textbooks and lecture notes. **Read the SKILL.md and both reference files before creating any study notes.** The skill defines:
- Core philosophy (6 principles)
- Conceptual insight standards
- Page types and their sections (topic, definition, theorem, exercise, exercise index)
- Templates for each page type
- Obsidian formatting patterns
- A 24-item self-evaluation checklist

**`.claude/skills/exercise-builder/`** — practice exercises and drills as interlinked vault pages; the practice-generating companion to `polymath-notes`. Six modes (algorithm derivations, competitive programming, calculation drills, physical modelling, approximation methods, exam-level exercises).

**`.claude/skills/paper-notes/`** — turns a single research paper (usually a PDF in `paper_source/`) into a self-contained note-set that a reader competent at undergraduate analysis, linear algebra, and elementary probability — but not a specialist in the paper's field — can follow without looking anything up. **Read the SKILL.md, `notation-discipline.md`, the three template references, and the reference thesis before making paper notes.** The skill backchains everything above the undergraduate floor into atomic `Def -`/`Thm -`/`Lemma -` notes, recalls unfamiliar terms at their point of use, types every symbol, rewrites every proof gap-free, and writes in the prose voice of the reference thesis (`paper_source/Chiang Sung En-Thesis.pdf`), which supersedes the David Tong style for paper notes. Output: a companion page `Study notes/Papers/[Short Title]/Paper - [Short Title].md` plus reusable atomic prerequisite notes (in their subject folders) and paper-result stubs. It does **not** consult the Notion DAG.

## Personal Notes

The user may provide a Notion link to their personal notes for a topic. If the Notion MCP is connected, fetch it directly. Otherwise, ask the user to paste the content. Personal notes contain terse, low-context bulletpoints that should be reverse-engineered into full insights and woven seamlessly into the study notes.
