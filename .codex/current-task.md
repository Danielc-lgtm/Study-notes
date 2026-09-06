# Current task

**Overall status:** in progress — Gauge Theory I–VI merged; Gauge Theory VII complete and ready to merge

## Goal
Create a complete, self-contained Obsidian lecture-note series covering both `sources/IntroGaugeTheory_LectNotes.pdf` (Haydys) and `sources/mathematical_gauge_theory.pdf` (Wernli), rebuilding the existing Gauge Theory graph without using existing vault prose or proof architecture as a stylistic anchor.

## Scope
1. Gauge Theory I — Vector-bundle connections and the electromagnetic prototype — complete (PR #19)
2. Gauge Theory II — Principal bundles, representations, and bundle classification — complete (PR #20)
3. Gauge Theory III — Principal connections, curvature, holonomy, and gauge symmetry — complete (PR #21; merged)
4. Gauge Theory IV — Chern–Weil theory, characteristic classes, Chern–Simons, and flat moduli — complete (PR #23; merged)
5. Gauge Theory V — Hodge theory, Maxwell, Yang–Mills, and instantons — complete (PR #24; merged)
6. Gauge Theory VI — Clifford algebras, spin geometry, and Dirac operators — complete (PR #25; merged)
7. Gauge Theory VII — Sobolev spaces, elliptic operators, and elliptic complexes — complete (PR #26; ready to merge)
8. Gauge Theory VIII — Fredholm maps, transversality, determinant lines, and degree — pending
9. Gauge Theory IX — Seiberg–Witten equations and moduli-space analysis — pending
10. Gauge Theory X — Seiberg–Witten invariants and four-manifold applications — pending
11. Gauge Theory XI — Algebraic topology, intersection forms, classification, and Donaldson theory — pending
12. Final source-coverage and cross-topic consistency audit — pending

The persistent section-by-section coverage matrix is `.codex/gauge-theory-source-map.md`.

## Mode
`mixed` — rebuild four existing topics and create the remaining chapters and atomic pages.

## Working branch
`codex/create-complete-gauge-theory-gt-vii`

## Pull request
PR #26 — Gauge Theory VII complete and ready to merge.

## Sources
- `sources/IntroGaugeTheory_LectNotes.pdf` — Andriy Haydys, 73 pages
- `sources/mathematical_gauge_theory.pdf` — Konstantin Wernli, 155 pages
- Existing Gauge Theory I–IV graph, used only as mathematical/structural material under the user's style override
- Relevant prerequisite pages in Differential Geometry, Functional Analysis, Algebraic Topology, and Special Relativity

## Completed units
- Gauge Theory I — Vector-bundle connections and the electromagnetic prototype — complete, merged in PR #19.
- Gauge Theory II — Principal bundles, representations, and classification — complete, merged in PR #20.

## Current unit
Gauge Theory VIII — Fredholm maps, transversality, determinant lines, and degree.

## Remaining units
Gauge Theory VIII–XI and the final audit.

## Unresolved issues
_none_. Source convention conflicts will be made explicit rather than silently normalized.

## Exact next action
Merge PR #26, then create Gauge Theory VIII from Haydys §6.

## Last completed commit
`0c79aa2` — corrected the Gauge Theory V curvature-variation and stress-energy formulas while initializing Gauge Theory VI.

## Merge policy
`auto` — one completed unit per PR, merged immediately, then continue from fresh `main`.

## Merge history
- #19 Gauge Theory I → `main` (`961b960`, 2026-09-06).
- #20 Gauge Theory II → `main` (`40e54fd`, 2026-09-06).
- #21 Gauge Theory III → `main` (`ce4a900`, 2026-09-06).
- #23 Gauge Theory IV → `main` (`6173fb5`, 2026-09-06).
- #24 Gauge Theory V → `main` (`6f77dba`, 2026-09-06).
- #25 Gauge Theory VI → `main` (`c296516`, 2026-09-06).
