---
name: paper-notes
description: >
  Turn a single research paper (usually a PDF in paper_source/ or sources/) into a self-contained set of
  Obsidian notes, so that a reader competent at undergraduate analysis, linear algebra, and elementary
  probability — but NOT a specialist in the paper's field — can follow every definition, theorem, and
  reasoning step without looking anything up. Everything the paper uses above that undergraduate floor
  (measure theory, functional analysis, differential and hyperbolic geometry, stochastic processes, group
  theory beyond the basics, information theory, …) is backchained recursively into atomic Def/Thm/Lemma notes
  and recalled at point of use; every proof is rewritten gap-free; every symbol is typed. Use whenever the
  user points at a paper and asks to make notes on it, understand it, or read it without chasing references.
  Trigger phrases: "turn this paper into notes," "make notes on this paper," "self-contained notes from this
  PDF," "backchain this paper," "break down this paper," "make this paper readable without looking things up,"
  "explain this paper so a non-specialist can follow it," "read this paper for me and write it up," "notes on
  the paper in paper_source." Distinct from polymath-notes (chapter-level study notes with exercises from
  textbooks) and prereq-backchain (plans a subject to study). This skill takes ONE finished paper and produces
  a companion page that walks it section by section in the prose voice of the reference thesis, plus reusable
  atomic prerequisite notes and paper-result stubs, all wikilinked into the vault.
---

# paper-notes (pointer)

The full specification for this skill lives in `.claude/skills/paper-notes/` and is
shared with Claude Code. The `.claude` directory name is historical; its contents
are authoritative for Codex too. Do not duplicate them here.

Read, in this order, then follow them exactly:

1. `.claude/skills/paper-notes/SKILL.md`
2. `.claude/skills/paper-notes/references/notation-discipline.md`
3. `.claude/skills/paper-notes/references/companion-page-template.md`
4. `.claude/skills/paper-notes/references/atomic-note-templates.md`
5. `.claude/skills/paper-notes/references/recall-callouts.md`
6. `.claude/skills/paper-notes/references/obsidian-patterns.md`
7. `.claude/skills/paper-notes/references/prose-and-proof-standard.md` (symlink to the polymath-notes copy), then the thesis `prose/Chiang Sung En-Thesis.pdf` — the prose register and the minimum proof standard

Also read `.codex/note-quality.md` (review standard) and `.codex/workflow.md`
(branch / commit / PR / merge mechanics) before writing anything to the vault.

