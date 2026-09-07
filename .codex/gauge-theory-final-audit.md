# Gauge Theory final audit

Date: 2026-09-07

## Scope

The audit covers the eleven Gauge Theory topic pages, their atomic subpages, the series map, the Haydys/Wernli source ledger, and incoming references affected by the chapter reorganization.

## Results

- **Source coverage:** every row in `.codex/gauge-theory-source-map.md` is complete. Haydys §§1–7.2.1 and Wernli's Preface and §§1.1–5.3 have destinations.
- **Graph:** all wikilink basenames originating in the 204 pre-audit Gauge Theory pages resolve. No stale references to the replaced Gauge Theory II, III, or IV topic names remain.
- **Structure:** all Gauge Theory Markdown pages have YAML frontmatter. No control characters were found. The eleven topic pages are joined by `Gauge Theory — Series Map.md`.
- **Conventions:** the series consistently distinguishes vector-bundle and principal-bundle connections, right-action gauge conventions, abelian from nonabelian curvature, Euclidean from Lorentzian Hodge signs, and topological from smooth four-manifold classification.
- **Pedagogy and rederivation:** every chapter exposes a concept map, operational route, or explicit proof mechanism. The final series map provides physical, geometric, analytic, and topological re-entry routes.
- **Proof boundary:** deep external classification results—Freedman, Taubes, connected-sum vanishing, and Donaldson diagonalization—are stated with exact hypotheses and explicit accounts of the additional surgery, gluing, compactification, or pseudoholomorphic-curve machinery their full proofs require. They are not silently represented as consequences of the elementary material.

## Mechanical audit boundary

A vault-wide basename scan reports pre-existing unresolved or false-positive links outside the Gauge Theory subtree, including wiki-like notation inside formulas. No unresolved basename link originates in Gauge Theory. Those unrelated findings are outside this campaign and were not modified.
