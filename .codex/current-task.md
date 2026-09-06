# Current task

**Overall status:** in progress — Gauge Theory I–III merged; Gauge Theory IV complete and ready to merge

## Goal
Create a complete, self-contained Obsidian lecture-note series covering both `sources/IntroGaugeTheory_LectNotes.pdf` (Haydys) and `sources/mathematical_gauge_theory.pdf` (Wernli), rebuilding the existing Gauge Theory graph without using existing vault prose or proof architecture as a stylistic anchor.

## Scope
1. Gauge Theory I — Vector-bundle connections and the electromagnetic prototype — complete (PR #19)
2. Gauge Theory II — Principal bundles, representations, and bundle classification — complete (PR #20)
3. Gauge Theory III — Principal connections, curvature, holonomy, and gauge symmetry — complete (PR #21; ready to merge)
4. Gauge Theory IV — Chern–Weil theory, characteristic classes, Chern–Simons, and flat moduli — complete (PR #23; ready to merge)
5. Gauge Theory V — Hodge theory, Maxwell, Yang–Mills, and instantons — pending
6. Gauge Theory VI — Clifford algebras, spin geometry, and Dirac operators — pending
7. Gauge Theory VII — Sobolev spaces, elliptic operators, and elliptic complexes — pending
8. Gauge Theory VIII — Fredholm maps, transversality, determinant lines, and degree — pending
9. Gauge Theory IX — Seiberg–Witten equations and moduli-space analysis — pending
10. Gauge Theory X — Seiberg–Witten invariants and four-manifold applications — pending
11. Gauge Theory XI — Algebraic topology, intersection forms, classification, and Donaldson theory — pending
12. Final source-coverage and cross-topic consistency audit — pending

The persistent section-by-section coverage matrix is `.codex/gauge-theory-source-map.md`.

## Mode
`mixed` — rebuild four existing topics and create the remaining chapters and atomic pages.

## Working branch
`codex/create-complete-gauge-theory-gt-v`

## Pull request
Gauge Theory V PR pending creation.

## Sources
- `sources/IntroGaugeTheory_LectNotes.pdf` — Andriy Haydys, 73 pages
- `sources/mathematical_gauge_theory.pdf` — Konstantin Wernli, 155 pages
- Existing Gauge Theory I–IV graph, used only as mathematical/structural material under the user's style override
- Relevant prerequisite pages in Differential Geometry, Functional Analysis, Algebraic Topology, and Special Relativity

## Completed units
- Gauge Theory I — Vector-bundle connections and the electromagnetic prototype — complete, merged in PR #19.
- Gauge Theory II — Principal bundles, representations, and classification — complete, merged in PR #20.

## Current unit
Gauge Theory V — Hodge theory, Maxwell, Yang–Mills, and instantons.

## Remaining units
Gauge Theory V–XI and the final audit.

## Unresolved issues
_none_. Source convention conflicts will be made explicit rather than silently normalized.

## Exact next action
Merge PR #23, then audit and expand Gauge Theory V against Wernli §§3.1–3.3 on a fresh branch.

## Last completed commit
`978d5c8` — deepened the principal-connection definition with axiom-failure analysis, examples, calibration, and operational interpretation.

## Merge policy
`auto` — one completed unit per PR, merged immediately, then continue from fresh `main`.

## Merge history
- #19 Gauge Theory I → `main` (`961b960`, 2026-09-06).
- #20 Gauge Theory II → `main` (`40e54fd`, 2026-09-06).
