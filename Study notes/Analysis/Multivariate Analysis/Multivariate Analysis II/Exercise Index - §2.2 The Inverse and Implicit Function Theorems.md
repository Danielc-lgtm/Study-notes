---
type: exercise-index
subject: multivariate-analysis
section: "2.2"
tags: [analysis, multivariate-analysis]
---

## §2.2 The Inverse and Implicit Function Theorems — Exercises

The exercises of §2.2 drill the inverse and implicit function theorems and their failure modes. Polar coordinates illustrate local invertibility everywhere but global injectivity only on one period; implicit function applications solve an underdetermined system locally by isolating a dependent block; and singular-Jacobian counterexamples ($x^3$, $z^2$, matrix squaring) calibrate exactly where the theorem's hypothesis bites. The unifying observation: a nonzero Jacobian at a point gives *local* diffeomorphism status, and the global picture depends on the topology of the domain.

- [[Ex - Local invertibility of a nonlinear map]] (⭐⭐) — apply the inverse function theorem to the polar-coordinate map, whose Jacobian determinant $r$ is nonzero on its whole domain, then confront the local/global gap: $F$ is a local diffeomorphism everywhere yet $2\pi$-periodic, hence not globally injective, and becomes a global diffeomorphism only after restricting to one period of the angle ([[Thm - The Inverse Function Theorem]], [[Def - Partial Derivatives and the Jacobian Matrix]]).

- [[Ex - Solving an implicit equation locally]] (⭐⭐) — solve a $2\times 4$ system for two variables in terms of the other two by checking that the partial Jacobian in the dependent variables is invertible at a base point, then compute the derivatives of the implicit solution by differentiating the defining identity with the chain rule and inverting the dependent block ([[Thm - The Implicit Function Theorem]], [[Def - Partial Derivatives and the Jacobian Matrix]], [[Thm - The Chain Rule]]).

- [[Ex - Failure of inversion at a singular Jacobian]] (⭐) — probe the boundary of the inverse function theorem by examining maps at points where the Jacobian determinant vanishes: $x^3$ (invertible but with non-smooth inverse), the squaring map $z\mapsto z^2$ (a genuine two-to-one fold), and matrix squaring $X\mapsto X^2$ (a kernel vector exhibited at a bad point), diagnosing in each case which hypothesis fails ([[Thm - The Inverse Function Theorem]], [[Def - Partial Derivatives and the Jacobian Matrix]]).
