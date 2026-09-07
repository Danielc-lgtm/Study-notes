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
  prose/                           # the owner's thesis — the prose register AND the minimum
                                   #   proof standard for every note in the vault
                                   #   (spec: .claude/skills/polymath-notes/references/prose-and-proof-standard.md)
  sources/                         # source PDFs for polymath-notes (lecture notes, textbook chapters)
  paper_source/                    # source PDFs for paper-notes, plus example.md (Whole-Paper Story exemplar)
  Study notes/                     # the Obsidian vault
    [Subject Area]/                # e.g., Algebra/, Analysis/, Geometry/
      [Subtopic]/                  # e.g., Group Theory/, Functional Analysis/
                                   #   (Geometry/ holds the standalone peers Differential Geometry/ and
                                   #   Gauge Theory/, plus the Frankel-depth gateways under Geometry of Physics/)
        [Topic Page].md            # chapter-level topic page
        [Topic Name]/              # subfolder for that topic's subpages
          Def - [Name].md
          Thm - [Name].md
          Ex - [Name].md
          Exercise Index - §X.Y.md
    paper/                         # paper-notes output — one folder per paper
      [Short Title]/               # index at the top; everything else in Subpages/
        Paper - [Short Title].md               # INDEX (front door; short scaffolding
                                               #   with prominent link to Whole-Paper Story)
        Subpages/
          Paper - [Short Title] — Whole-Paper Story.md
                                               # single coherent narrative walking the
                                               #   entire paper (voice: paper_source/example.md)
          Paper - [Short Title] — §N [Title].md  # one section page per paper section
                                                 #   (polymath-style concept-map index)
          Def - [Name].md          # atomic subpage per paper Definition
          Thm - [Name].md          # atomic subpage per paper Theorem
          Lemma - [Name].md        # atomic subpage per paper Lemma
          Cor - [Name].md          # atomic subpage per paper Corollary
          Prop - [Name].md         # atomic subpage per paper Proposition
          Remark - [Name].md       # atomic subpage per paper Remark
                                   #   OR per load-bearing paragraph (descriptive name)
          Ex - [Name].md           # atomic subpage per paper Example
          # (also: prerequisite Def/Thm/Lemma notes, same Subpages folder)
          # prerequisites already in the vault are wikilinked, not copied here
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
Lemma - [Lemma Name].md        # atomic lemma note (Thm-shaped; used by paper-notes)
Ex - [Short Description].md
Exercise Index - §X.Y [Section Title].md
Paper - [Short Title].md       # paper-notes companion page
[Topic Name].md
```

### Writing Style
**The baseline for all prose is the owner's thesis, `prose/Chiang Sung En-Thesis.pdf`; read it before writing.** Two registers: formal for definitions and theorem statements; the thesis's measured, expansive, first-person-plural academic register for everything else — orient, motivate, state formally, unpack in the smallest concrete case, re-explain in a purpose-titled remark, close in words. Every claim travels with its reason. Standard terminology only; every symbol typed at first use. Prose over bullets. No abbreviations. No hedge stacking. Not inspirational — write the explanation that makes insight visible. Full specification: `.claude/skills/polymath-notes/references/prose-and-proof-standard.md` Part I.

### Proofs
**Every theorem, lemma, proposition, or corollary the notes mention is proved in full, with self-contained rigour, on its own page; the thesis's fully written proofs are the minimum level of detail.** No statement-only pages, no sketches, no "clearly". A result used anywhere is wikilinked to the page carrying its complete proof and restated at the point of use. The single exception — a genuinely book-length result (Freedman, Donaldson's diagonalisation package, Uhlenbeck compactness, Atiyah–Singer) — may be used only inside an `Imported without proof` callout and is registered on the topic page. Mechanical gate: `.claude/skills/polymath-notes/scripts/find-unproved-theorems.py`. Full specification: `prose-and-proof-standard.md` Part II.

### Git Workflow
After creating or modifying study notes, always commit with a descriptive message summarizing what was added (e.g., "Add Measure Theory I — §2.1–2.3: 8 definitions, 4 theorems, 6 exercises"). Push when the user requests it.

## Skills

Three skills build vault content. Each has its own `SKILL.md` and `references/`; read a skill's spec before invoking it.

**`.claude/skills/polymath-notes/`** — the full specification for creating chapter-level study notes from textbooks and lecture notes. **Read the SKILL.md, all three reference files (`templates.md`, `obsidian-patterns.md`, `prose-and-proof-standard.md`), and the thesis in `prose/` before creating any study notes.** The skill defines:
- Core philosophy (6 principles)
- Conceptual insight standards
- Page types and their sections (topic, definition, theorem, exercise, exercise index)
- Templates for each page type
- Obsidian formatting patterns
- The Proof Standard (every theorem mentioned is proved; thesis floor; imported-result exception)
- A 42-item self-evaluation checklist

**`.claude/skills/exercise-builder/`** — practice exercises and drills as interlinked vault pages; the practice-generating companion to `polymath-notes`. Six modes (algorithm derivations, competitive programming, calculation drills, physical modelling, approximation methods, exam-level exercises).

**`.claude/skills/paper-notes/`** — turns a single research paper (usually a PDF in `paper_source/`) into a modularly self-contained note-set that a reader competent at undergraduate analysis, linear algebra, and elementary probability — but not a specialist in the paper's field — can follow without looking anything up. **Read the SKILL.md, `notation-discipline.md`, the three template references, `prose-and-proof-standard.md`, the reference thesis `prose/Chiang Sung En-Thesis.pdf` (the prose register and the minimum proof standard, for the whole vault), and `paper_source/example.md` (the structural exemplar for the Whole-Paper Story page, whose sentences are nonetheless in the thesis register) before making paper notes.** The skill backchains everything above the undergraduate floor into atomic notes, recalls unfamiliar terms at their point of use, types every symbol, rewrites every proof gap-free (and proves in full every external result the paper cites, under the vault-wide Proof Standard), and writes in the thesis's prose register. Output: **one folder per paper**, `Study notes/paper/[Short Title]/`, laid out with an **index page** at the top and everything else in a `Subpages/` folder beside it — the index carries a prominent link at the top to the **Whole-Paper Story** (a mandatory single coherent narrative that walks the entire paper at `paper_source/example.md`-level detail, with mental pictures at every step). The `Subpages/` folder holds the Whole-Paper Story, one **section page per paper section** (polymath-style concept-map index with foldable-bullet statements), **one atomic subpage per named paper item** (Def/Thm/Lemma/Cor/Prop/Remark/Ex), **one atomic subpage per load-bearing paragraph** (descriptively-named `Remark - ...` for the paragraphs the paper spends real prose *establishing* rather than *stating* — periodisations, coset enumerations, changes of variables, invariance arguments, dictionaries), and the atomic prerequisite notes. Every section page is modularly self-contained — a reader jumping into §5 without reading §2–§4 finds every prerequisite recalled or transcluded there. Every atomic subpage is self-contained too — a reader landing on it cold can read and check it without opening any other file. Prerequisites that already have a note elsewhere in the vault are wikilinked, not duplicated into the folder. It does **not** consult the Notion DAG.

## Personal Notes

The user may provide a Notion link to their personal notes for a topic. If the Notion MCP is connected, fetch it directly. Otherwise, ask the user to paste the content. Personal notes contain terse, low-context bulletpoints that should be reverse-engineered into full insights and woven seamlessly into the study notes.
