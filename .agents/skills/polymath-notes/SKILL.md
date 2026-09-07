---
name: polymath-notes
description: >
  Create structured mathematical study notes as interlinked Obsidian markdown pages from uploaded lecture notes,
  textbooks, and papers (supplemented by web search). Use whenever the user asks to create study notes, write up
  a topic, or study an area of mathematics, physics, or theoretical computer science. Trigger phrases: "create
  notes on X," "study X," "write up X," "add X to my notes," "I want to learn X." Also trigger for specific
  components: "legal operations in X," "sources and targets for theorem Y," "axiom motivation for definition Z,"
  "why is theorem X true," "most reusable properties in X," "relate X to Y." Creates chapter-level topic pages
  with definition, theorem, and exercise subpages — designed for spaced retrieval practice with rapid context
  re-entry across many subjects studied simultaneously. Content follows uploaded source material structure by
  default, enriched with the skill's elements (axiom motivations, sources and targets, legal operations,
  convergent strategies, insight standards, etc.).
---

# polymath-notes (pointer)

The full specification for this skill lives in `.claude/skills/polymath-notes/` and is
shared with Claude Code. The `.claude` directory name is historical; its contents
are authoritative for Codex too. Do not duplicate them here.

Read, in this order, then follow them exactly:

1. `.claude/skills/polymath-notes/SKILL.md`
2. `.claude/skills/polymath-notes/references/templates.md`
3. `.claude/skills/polymath-notes/references/obsidian-patterns.md`
4. `.claude/skills/polymath-notes/references/prose-and-proof-standard.md`, then the thesis it points at, `prose/Chiang Sung En-Thesis.pdf` (extract with `pymupdf`) — the prose register and the minimum proof standard for every note

Also read `.codex/note-quality.md` (review standard) and `.codex/workflow.md`
(branch / commit / PR / merge mechanics) before writing anything to the vault.
Scripts referenced by the spec are under `.claude/skills/polymath-notes/scripts/`; run them with `python3`.
