---
type: exercise-index
subject: multivariate-analysis
section: "2.1"
tags: [analysis, multivariate-analysis]
---

## §2.1 Optimization and Lagrange Multipliers — Exercises

- [[Ex - Classifying critical points with the Hessian]] — drill the full unconstrained-optimization pipeline on a parametrized cubic: solve $\nabla f = 0$ as a polynomial system, classify each critical point by the sign of the $2\times 2$ Hessian determinant, and handle the degenerate case ($\alpha = 0$, zero Hessian) by restricting the function to lines through the critical point ([[Thm - First-Order Optimality Condition]], [[Thm - Second-Order Optimality Conditions]], [[Def - Critical Point, Hessian, and Definiteness]]).

- [[Ex - Constrained optimization via Lagrange multipliers]] — find the global extrema of a linear function on a cusped constraint curve inside a box, assembling the complete candidate list from three sources: the regular Lagrange solutions, the boundary points where the curve meets the box, and — the trap — the non-regular cusp point that the Lagrange equations cannot see ([[Thm - The Method of Lagrange Multipliers]], [[Thm - First-Order Optimality Condition]], [[Def - Directional Derivative and the Gradient]]).

- [[Ex - The spectral theorem via constrained optimization]] — prove the spectral theorem for real symmetric matrices analytically, by extremising the quadratic form $\langle x, Ax\rangle$ on the unit sphere so the Lagrange equation becomes the eigenvector equation $Ax = \mu x$, then inducting on the orthogonal complement and using symmetry of $A$ to kill the parasitic multipliers ([[Thm - The Method of Lagrange Multipliers]], [[Thm - First-Order Optimality Condition]], [[Def - Critical Point, Hessian, and Definiteness]]).
