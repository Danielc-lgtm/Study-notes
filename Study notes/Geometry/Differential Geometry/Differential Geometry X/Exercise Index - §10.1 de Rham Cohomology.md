---
type: exercise-index
subject: differential-geometry
section: "10.1"
tags: [geometry, differential-geometry, cohomology]
---

## §10.1 de Rham Cohomology — Exercises

This section's exercises drill the basic computational techniques for de Rham cohomology: identifying contractible domains (where the Poincaré lemma trivializes cohomology in positive degrees), using $H^0_{dR}$ as a connected-components count, and recognizing closed-but-not-exact forms via integration over cycles. The unifying theme is the dichotomy between contractible (trivial cohomology) and topologically interesting (non-trivial cohomology), with detection of non-triviality always reducing to integration against a generating cycle.

- [[Ex - The de Rham Cohomology of R^n is Trivial in Positive Degrees]] (⭐) — direct application of the Poincaré lemma plus the connected-components count to get $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}$, $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$ ([[Def - de Rham Cohomology]], [[Thm - The Poincaré Lemma on a Star-Shaped Region]])
- [[Ex - Computing H^1 of S^1 via Mayer-Vietoris]] (⭐⭐) — sets up the standard two-arc cover, runs the Mayer–Vietoris computation, identifies $[d\theta]$ as the explicit generator. The base case for higher-dimensional sphere computations ([[Def - de Rham Cohomology]], [[Thm - The Mayer-Vietoris Sequence]], [[Thm - The Poincaré Lemma on a Star-Shaped Region]])
- [[Ex - The de Rham Cohomology of the Torus]] (⭐⭐⭐) — uses Künneth (stated as a forward result, derived inductively from Mayer–Vietoris) to compute $H^k_{dR}(T^n) = \mathbb{R}^{\binom{n}{k}}$, with explicit basis the wedges $d\theta^{i_1} \wedge \cdots \wedge d\theta^{i_k}$. Cross-check by integration over sub-tori ([[Def - de Rham Cohomology]], [[Thm - The Mayer-Vietoris Sequence]], [[Thm - Homotopy Invariance of de Rham Cohomology]])
