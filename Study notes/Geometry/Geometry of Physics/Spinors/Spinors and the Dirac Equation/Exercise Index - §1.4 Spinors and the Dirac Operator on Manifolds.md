---
type: exercise-index
subject: spinors
section: "1.4"
tags: [geometry, spinors, differential-geometry, riemannian-geometry, index-theory]
---

## §1.4 Spinors and the Dirac Operator on Manifolds — Exercises

This section drills the global aspects of spinor theory on curved manifolds: existence of spin structures, the spin connection, the Dirac operator, and the deep interaction between scalar curvature and the spinor spectrum via the Lichnerowicz formula. The unifying technique is the **Bochner-type identity** $\not D^2 = \nabla^{S*}\nabla^S + R/4$, which encodes the entire geometric content of the Dirac operator on a curved manifold and is the source of all vanishing theorems for harmonic spinors. The signature pattern: combining topological data (Stiefel-Whitney classes, $\hat A$-genus) with geometric data (scalar curvature, spin connection) to derive constraints on either topology or geometry.

- [[Ex - Spin Structure on the Sphere S^n]] (⭐⭐) — proof that $S^n$ admits a (unique for $n \geq 2$) spin structure using the stable parallelisability $TS^n \oplus \mathbb{R} \cong S^n \times \mathbb{R}^{n+1}$, with detour to the two spin structures on $S^1$ (periodic vs antiperiodic boundary conditions for fermion fields) ([[Def - Spin Structure on a Manifold]], [[Def - Smooth Manifold]], [[Def - Vector Bundle]]).
- [[Ex - Lichnerowicz Vanishing for Harmonic Spinors on Positive Scalar Curvature]] (⭐⭐⭐) — flagship application of the Lichnerowicz formula: positive scalar curvature kills harmonic spinors; combined with the Atiyah-Singer index theorem, gives $\hat A(M) = 0$ as a topological obstruction to positive-scalar-curvature metrics; concrete consequence: the K3 surface (with $\hat A = 2$) does not admit a positive-scalar-curvature metric ([[Thm - Lichnerowicz Formula]], [[Def - Spin Connection and the Dirac Operator]], [[Def - Spin Structure on a Manifold]]).
- **Compute the Dirac spectrum on the round sphere $S^n$.** Using the rotational symmetry and the explicit form of the spin connection, derive the eigenvalues of $\not D$ on $S^n$ (Friedrich): the eigenvalues are $\pm(k + n/2)$ for $k = 0, 1, 2, \ldots$, with multiplicities related to spherical harmonics. The smallest eigenvalue squared saturates the Friedrich bound $\lambda^2 \geq R/(4(n-1)) \cdot n/(n-1)$ derived from the Lichnerowicz formula. (⭐⭐⭐) ([[Thm - Lichnerowicz Formula]], [[Def - Spin Connection and the Dirac Operator]], [[Ex - Spin Structure on the Sphere S^n]]).
