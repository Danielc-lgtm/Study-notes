# Study Notes — Obsidian Vault

This is a polymathic study system: an Obsidian vault of interlinked mathematical study notes covering approximately 130 subjects simultaneously, organized via a prerequisite DAG.

## Owner Background

The user has strong background in: applied math (PDEs, fluids, dynamical systems, math finance, numerical analysis), pure analysis (functional analysis, PDE analysis, SDEs), geometric mechanics, statistical mechanics, quantum mechanics, fluid dynamics, information theory, differential/Riemannian geometry, Bayesian networks/causality, algorithmic information theory (AIT).

Weaker areas: algebra (most neglected), some physics curriculum gaps, computational complexity and lambda calculus (forgotten from undergrad), no formal economics background.

Active research areas: ontology identification (AIT + reusable function pointers), information-theoretic emergence of continuity, Bayesian ontology shifts, meta-learning/metacognition, continuous dynamic Bayesian nets, decision theory (UDT, program equilibrium), Maxwell's demon in algorithmic thermodynamics.

## Vault Structure

```
[repo root]/
  CLAUDE.md                        # this file
  .claude/                         # Claude Code skills
    skills/
      polymath-notes/
        SKILL.md
        references/
          obsidian-patterns.md
          templates.md
  Study notes/                     # the Obsidian vault
    [Subject Area]/                # e.g., Algebra/, Analysis/, Geometry/
      [Subtopic]/                  # e.g., Group Theory/, Functional Analysis/
        [Topic Page].md            # chapter-level topic page
        [Topic Name]/              # subfolder for that topic's subpages
          Def - [Name].md
          Thm - [Name].md
          Ex - [Name].md
          Exercise Index - §X.Y.md
    .obsidian/                     # Obsidian configuration
```

## Conventions

### Formatting
- **LaTeX:** `$...$` for inline math, `$$...$$` for display math. Every variable, symbol, and equation in prose must be in LaTeX — no bare Unicode math symbols.
- **Internal links:** Obsidian wikilinks `[[Def - Group]]` or `[[Def - Group|group]]` with display text. Links work across folders by filename; use full paths only to disambiguate.
- **Transclusion:** `![[Def - Group#The Definition]]` to embed sections from other pages inline. Preferred for Recall sections in exercises.
- **Collapsible sections:** HTML `<details><summary>` tags for progressive disclosure. Always leave blank lines after `<summary>` and before `</details>`.
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

The `.claude/skills/polymath-notes/` skill contains the full specification for creating study notes. **Read the SKILL.md and both reference files before creating any study notes.** The skill defines:
- Core philosophy (6 principles)
- Conceptual insight standards
- Page types and their sections (topic, definition, theorem, exercise, exercise index)
- Templates for each page type
- Obsidian formatting patterns
- A 24-item self-evaluation checklist

## Personal Notes

The user may provide a Notion link to their personal notes for a topic. If the Notion MCP is connected, fetch it directly. Otherwise, ask the user to paste the content. Personal notes contain terse, low-context bulletpoints that should be reverse-engineered into full insights and woven seamlessly into the study notes.
