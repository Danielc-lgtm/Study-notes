---
type: exercise-index
subject: linear-algebra
section: "6C"
tags: [algebra, linear-algebra]
---

## §6C Orthogonal Complements and Projections — Exercises

The exercises of §6C drill the geometric heart of the chapter: the orthogonal decomposition $V = U \oplus U^\perp$, the [[Def - Orthogonal Projection|orthogonal projection]] $P_U$, and its identification with the closest-point map via the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]]. The recurring techniques are **projecting orthogonally** (operation 3) and **using Pythagoras to break a norm into orthogonal pieces** (operation 4). Exercises here include the canonical distance-to-a-[[Def - Subspace|subspace]] problem, the polynomial-approximation problem from §6B re-read as a projection, and the connection to Cauchy-Schwarz via the projection-onto-a-line construction.

- [[Ex - Distance to a subspace via orthogonal projection]] (⭐⭐) — compute the distance from $(1, 2, 3, 4)$ to a $2$-dimensional [[Def - Subspace|subspace]] of $\mathbb{R}^4$, by Gram-Schmidting the spanning vectors and projecting; verify via Pythagoras ([[Def - Inner Product Space]], [[Def - Orthogonal Projection]], [[Thm - Best Approximation by Orthogonal Projection]], [[Thm - Gram-Schmidt Procedure]], [[Thm - Pythagorean Theorem]])
- [[Ex - Cauchy-Schwarz attained iff one vector is a scalar multiple of the other]] (⭐⭐) — re-read in the §6C light, this is the equality case of the projection-onto-a-line construction; $u$ has zero orthogonal component iff $u$ lies on the line through $v$ ([[Def - Inner Product Space]], [[Thm - Cauchy-Schwarz Inequality]], [[Def - Orthogonal Projection]], [[Thm - Pythagorean Theorem]])
- [[Ex - Best polynomial approximation to sine]] (⭐⭐) — the polynomial-approximation problem is most naturally framed in §6C as orthogonal projection onto $\mathcal{P}_5(\mathbb{R}) \subseteq L^2[-\pi, \pi]$, with the answer $P_{\mathcal{P}_5}(\sin x)$ from the best-approximation theorem ([[Def - Inner Product Space]], [[Def - Orthogonal Projection]], [[Thm - Best Approximation by Orthogonal Projection]], [[Thm - Gram-Schmidt Procedure]])
