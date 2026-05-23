---
type: exercise-index
subject: differential-geometry
section: "4.2"
tags: [geometry, differential-geometry]
---

## §4.2 Submanifolds and the Regular Value Theorem — Exercises

This section's exercises exercise the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] — the standard manufacturing device for embedded submanifolds. The recurring pattern is: identify a candidate submanifold as a level set of a smooth map, compute the differential at every preimage point, check surjectivity (the regularity condition), and then read off the [[Def - Dimension|dimension]] and tangent space. The exercises develop this routine in three settings of increasing subtlety: (a) the sphere as a level set of $|x|^2$, the simplest scalar case; (b) $\mathrm{SL}(n, \mathbb{R})$ as a level set of the determinant, requiring Jacobi's formula and a dimension count $n^2 - 1$; (c) $\mathrm{O}(n)$ as a level set of $A^T A$, requiring the subtle choice of codomain (symmetric matrices, not all matrices) to make the regular value condition hold. The tangent spaces at the identity emerge as the corresponding **Lie algebras** — $\mathfrak{sl}(n)$ (trace-zero matrices) and $\mathfrak{o}(n)$ (antisymmetric matrices) — previewing the general construction of a Lie algebra as the tangent space at the identity of a matrix Lie group, developed in [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]].

- [[Ex - The Sphere as a Level Set]] (⭐) — Apply the regular value theorem to $f(x) = |x|^2$ to show $S^n$ is an embedded $n$-submanifold of $\mathbb{R}^{n+1}$ with tangent space $T_p S^n = p^\perp$. The canonical first example of the theorem. ([[Def - Embedded Submanifold]], [[Def - Regular and Critical Points]], [[Def - Tangent Space of a Submanifold]], [[Thm - Regular Value Theorem on Manifolds]])

- [[Ex - The Special Linear Group is a Submanifold of GL(n)|Ex - The Special Linear Group is a Submanifold of GL(n)]] (⭐⭐) — Apply the regular value theorem to $\det : \mathrm{GL}(n, \mathbb{R}) \to \mathbb{R}$, using Jacobi's formula $d(\det)_A(X) = \det(A) \mathrm{tr}(A^{-1} X)$, to show $\mathrm{SL}(n, \mathbb{R})$ is an embedded submanifold of dimension $n^2 - 1$. Compute $T_I \mathrm{SL}(n) = \mathfrak{sl}(n)$, the trace-zero matrices. ([[Def - Embedded Submanifold]], [[Def - Regular and Critical Points]], [[Def - Tangent Space of a Submanifold]], [[Thm - Regular Value Theorem on Manifolds]])

- [[Ex - The Orthogonal Group as a Regular Level Set]] (⭐⭐⭐) — Apply the regular value theorem to $\Phi(A) = A^T A$ with codomain $\mathrm{Sym}_n$ (the symmetric matrices, not all matrices — this is the subtle codomain choice). Show $\mathrm{O}(n)$ is an embedded submanifold of dimension $n(n-1)/2$ with $T_I \mathrm{O}(n) = \mathfrak{o}(n)$, the antisymmetric matrices. The codomain-choice trick is the recurring technique for matrix Lie [[Def - Group|groups]] defined by an equation with hidden symmetry. ([[Def - Embedded Submanifold]], [[Def - Regular and Critical Points]], [[Def - Tangent Space of a Submanifold]], [[Thm - Regular Value Theorem on Manifolds]])
