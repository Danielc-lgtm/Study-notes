---
type: exercise-index
subject: special-relativity
section: "19.3"
tags: [physics, special-relativity]
---

## §19.3 Differential Forms and the Exterior Derivative — Exercises

The exercises of §19.3 drill the exterior derivative and its algebraic laws, the metric-free half of the chapter's calculus. The recurring technique is to compute $\mathbf{d}$ of a form as the alternating sum of partial derivatives of its components — the Christoffel symbols cancelling by symmetry, which is why $\mathbf{d}$ needs no connection — and the recurring structural facts are nilpotency $\mathbf{d}^2 = 0$ (the equality of mixed partials in disguise) and the graded Leibniz rule $\mathbf{d}(A\wedge B) = \mathbf{d}A\wedge B + (-1)^{\deg A}A\wedge\mathbf{d}B$ (with the sign a transposition count). The exercises make these laws do real work: they show the classical curl is the Hodge dual of $\mathbf{d}$ of a $1$-form, that the two classical identities $\mathrm{curl}\,\mathrm{grad} = 0$ and $\mathrm{div}\,\mathrm{curl} = 0$ are both $\mathbf{d}^2 = 0$, and — the capstone — that writing the electromagnetic field as $F = \mathbf{d}A$ makes the homogeneous Maxwell equations and gauge invariance automatic consequences of nilpotency, while the inhomogeneous equation forces charge conservation as a consistency condition. The unifying observation is that $\mathbf{d}$ carries the topological content of physics, clean and connection-free, and is the language in which electromagnetism is cleanest.

- [[Ex - The exterior derivative of a 1-form is the curl]] (⭐⭐) — compute $(\mathbf{d}\underline{v})_{\alpha\beta} = \partial_\alpha v_\beta - \partial_\beta v_\alpha$ (Christoffels cancelling), show its Hodge dual is the Cartesian curl $\epsilon^{ijk}\partial_j v_k$, and deduce that $\mathrm{curl}\,\mathrm{grad} = 0$ and $\mathrm{div}\,\mathrm{curl} = 0$ are both instances of $\mathbf{d}^2 = 0$ ([[Def - The Exterior Derivative]], [[Def - The Hodge Star]]).

- [[Ex - The exterior derivative is nilpotent]] (⭐) — prove $\mathbf{d}\mathbf{d}f = 0$ and $\mathbf{d}\mathbf{d}A = 0$ directly, showing the second-derivative terms cancel in pairs by the equality of mixed partials, explain why this is connection-independent, and deduce that exact implies closed with the converse requiring the Poincaré lemma ([[Def - The Exterior Derivative]], [[Thm - Properties of the Exterior Derivative]]).

- [[Ex - The graded Leibniz rule for the exterior derivative]] (⭐⭐) — prove $\mathbf{d}(A\wedge B) = \mathbf{d}A\wedge B + (-1)^p A\wedge\mathbf{d}B$ by expanding in a coordinate basis and applying the product rule, and identify the sign $(-1)^p$ as the cost of sliding the degree-$1$ operator past the $p$ factors of $A$, making $\mathbf{d}$ a graded derivation ([[Def - The Exterior Derivative]], [[Def - Alternate Forms and the Exterior Product]]).

- [[Ex - The field strength as an exterior derivative and the homogeneous Maxwell equations]] (⭐⭐⭐) — define $F = \mathbf{d}A$, derive the homogeneous Maxwell equations $\mathbf{d}F = 0$ and gauge invariance $A\to A+\mathbf{d}\chi$ from nilpotency alone, and show the inhomogeneous equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ forces charge conservation $\nabla_\nu J^\nu = 0$ via the determinant divergence formula ([[Def - The Exterior Derivative]], [[Thm - Properties of the Exterior Derivative]], [[Thm - Divergence of a Vector and Tensor Field]]).
