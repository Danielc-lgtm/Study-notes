---
type: exercise-index
subject: differential-geometry
section: "5.2"
tags: [geometry, differential-geometry]
---

## §5.2 Flows and Completeness — Exercises

These exercises drill the construction of flows from vector fields and the question of when the flow is global (completeness). The first exercise constructs a closed-form flow for a linear vector field via the matrix exponential — the prototype of the exponential map in Lie theory. The second exercise establishes the fundamental criterion for completeness: compact support gives a global flow. The recurring techniques are solving autonomous ODEs in closed form and applying the Uniform Time Lemma to extract global existence from local existence plus a uniform bound.

- [[Ex - Constructing the Flow of a Linear Vector Field]] (⭐⭐) — Show that the linear vector field $X(x) = Ax$ on $\mathbb{R}^n$ has flow $\phi_t(x) = e^{tA} x$ via the matrix exponential, and verify all the flow axioms. Prototype of the exponential map in Lie theory. ([[Def - Smooth Vector Field]], [[Def - Integral Curve of a Vector Field]], [[Def - Flow of a Vector Field]], [[Def - Complete Vector Field]])

- [[Ex - Compactly Supported Vector Fields are Complete]] (⭐⭐) — Show that compact support of a smooth vector field implies completeness, via the Uniform Time Lemma. Corollary: every smooth vector field on a compact manifold is complete. ([[Def - Smooth Vector Field]], [[Def - Complete Vector Field]], [[Def - Flow of a Vector Field]], [[Thm - Fundamental Theorem on Flows]])

- [[Ex - Two Vector Fields with Nonzero Lie Bracket]] (⭐) — Compute the flows of $X = \partial_x$ and $Y = x \partial_y$ on $\mathbb{R}^2$ explicitly, then verify that the flows do not commute. The discrepancy is exactly $st [X, Y]_p$, illustrating the [[Thm - Commuting Flows Theorem|Commuting Flows Theorem]]. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Flow of a Vector Field]], [[Thm - Commuting Flows Theorem]])
