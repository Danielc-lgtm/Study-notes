---
type: exercise-index
subject: differential-geometry
section: "5.3"
tags: [geometry, differential-geometry]
---

## §5.3 The Lie Bracket and Lie Derivative — Exercises

These exercises drill the central object of the chapter — the Lie bracket — and its various interpretations as commutator, Lie derivative, and infinitesimal commutator of flows. The first exercise is a concrete computation displaying nonzero bracket and the corresponding non-commutation of flows. The second exercise verifies the Lie derivative reduces to the directional derivative on functions, hence characterizes conserved quantities. The third exercise establishes the Jacobi identity — the structural axiom that makes $\mathfrak{X}(M)$ a Lie algebra — and reinterprets it as $\mathrm{ad}_X = [X, \cdot]$ being a derivation of the bracket. The recurring technique is to compute brackets as commutators of derivations and exploit the algebraic structure of the resulting expressions.

- [[Ex - Two Vector Fields with Nonzero Lie Bracket]] (⭐) — Compute $[X, Y] = \partial_y$ for $X = \partial_x$, $Y = x \partial_y$ on $\mathbb{R}^2$, compute the flows, and verify their non-commutation. The discrepancy of the flow parallelogram is $st [X, Y]_p$, illustrating the geometric meaning of the bracket. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Flow of a Vector Field]], [[Thm - Commuting Flows Theorem]])

- [[Ex - Lie Derivative Annihilates Constant Functions]] (⭐) — Show $\mathcal{L}_X f = Xf$ for any smooth function $f$, hence $\mathcal{L}_X$ vanishes on constants. Reinterpret as the conservation-law characterization $f$ conserved along the flow $\iff Xf = 0$. ([[Def - Lie Derivative of a Vector Field]], [[Def - Smooth Vector Field]])

- [[Ex - The Jacobi Identity for Vector Fields]] (⭐⭐) — Prove the Jacobi identity $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$ by direct expansion using the commutator definition, and interpret it as the statement that $\mathrm{ad}_X = [X, \cdot]$ is a derivation of the Lie bracket. ([[Def - The Lie Bracket of Vector Fields]], [[Thm - Lie Bracket Properties]])

- [[Ex - The Coordinate Vector Fields Commute]] (⭐) — Bracket of coordinate vector fields vanishes, via two routes (coordinate formula and equality of mixed partials). Establishes the calibration point against which non-trivial brackets are measured. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Smooth Vector Field]])

- [[Ex - Faraday's Law via Reynolds Transport]] (⭐⭐⭐) — Differentiate magnetic flux through a moving surface and derive the motional EMF term using the time-dependent Reynolds theorem, Cartan's formula, and Stokes's theorem. ([[Thm - Reynolds Transport Theorem]], [[Def - Lie Derivative of a Vector Field]])
