---
type: exercise-index
subject: linear-algebra
section: "6B"
tags: [algebra, linear-algebra]
---

## §6B Orthonormal Bases — Exercises

The exercises of §6B drill the workhorse algorithm of the chapter: [[Thm - Gram-Schmidt Procedure|Gram-Schmidt orthogonalization]], and its applications to constructing orthonormal bases, projecting onto subspaces, and approximating functions. The recurring techniques are **applying Gram-Schmidt** (operation 2) and **taking inner products with basis vectors** (operation 6). Exercises here range from the direct application to classical inner products (producing Legendre polynomials) to the projection-based best-approximation of $\sin x$ by a degree-$\leq 5$ polynomial.

- [[Ex - Best polynomial approximation to sine]] (⭐⭐) — find the best polynomial of degree $\leq 5$ approximating $\sin x$ on $[-\pi, \pi]$ in $L^2$ norm, by Gram-Schmidting the monomial basis and projecting; exploit parity to halve the computation ([[Def - Inner Product Space]], [[Def - Orthonormal Basis]], [[Thm - Gram-Schmidt Procedure]], [[Thm - Best Approximation by Orthogonal Projection]], [[Def - Orthogonal Projection]])
- [[Ex - Legendre polynomials from Gram-Schmidt]] (⭐⭐) — apply Gram-Schmidt to monomials $1, x, x^2, x^3$ in $L^2[-1, 1]$ and recognize the result as scalar multiples of the Legendre polynomials; parity simplifies the projection coefficients ([[Def - Inner Product Space]], [[Def - Orthonormal Basis]], [[Thm - Gram-Schmidt Procedure]])
- [[Ex - Inner product determined by norm via the polarization identity]] (⭐⭐) — also relevant to §6B for understanding how the norm in a Gram-Schmidt-produced orthonormal basis encodes the full inner product ([[Def - Inner Product Space]], [[Def - Norm Induced by an Inner Product]], [[Thm - Parallelogram Law]])
