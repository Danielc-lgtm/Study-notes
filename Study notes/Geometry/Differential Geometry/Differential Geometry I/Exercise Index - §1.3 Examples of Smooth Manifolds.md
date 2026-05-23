---
type: exercise-index
subject: differential-geometry
section: "1.3"
tags: [geometry, differential-geometry]
---

## §1.3 Examples of Smooth Manifolds — Exercises

This section drills the explicit construction of smooth manifold structures on the standard examples: spheres, projective spaces, tori, matrix Lie [[Def - Group|groups]], and Grassmannians. Each exercise drills a different recipe: stereographic charts (sphere), affine charts (projective space), lifting from a fundamental domain (torus), open-subset inheritance (general linear group), the smooth manifold chart lemma (Grassmannian). Recurring techniques: chart construction, transition function computation, verification of Hausdorff and second-countability for quotient spaces. By the end, the reader should be able to construct a smooth atlas on any reasonable space encountered in differential geometry.

- [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]] (⭐⭐) — Construct the standard smooth structure on $S^n$ via the 2-chart stereographic atlas. The foundational compact-manifold example; everything from the round metric to Maxwell's equations on $S^n$ builds on this. ([[Def - Smooth Manifold]], [[Def - Smooth Atlas and Smooth Structure]], [[Def - Transition Function]], [[Thm - Smooth Structure from Maximal Atlas]])

- [[Ex - Real Projective Space is a Smooth Manifold]] (⭐⭐) — Construct the standard smooth structure on $\mathbb{RP}^n$ via $(n+1)$ affine charts with rational transition functions; verify Hausdorff and second-countability via the open-map property of the quotient projection. The prototype quotient-manifold construction. ([[Def - Smooth Manifold]], [[Def - Smooth Atlas and Smooth Structure]], [[Def - Transition Function]], [[Thm - Smooth Structure from Maximal Atlas]])

- [[Ex - The Torus is a Smooth Manifold via Quotient]] (⭐⭐) — Construct the smooth structure on $T^n = \mathbb{R}^n / \mathbb{Z}^n$ via lifting from small open balls in $\mathbb{R}^n$, verify the action is free and properly discontinuous, identify with the product structure. The prototype properly-discontinuous-action quotient. ([[Def - Smooth Manifold]], [[Def - Smooth Atlas and Smooth Structure]], [[Def - Transition Function]], [[Thm - Product of Smooth Manifolds is a Smooth Manifold]])

- [[Ex - The General Linear Group is a Smooth Manifold]] (⭐) — Show that $\mathrm{GL}(n, \mathbb{R})$ inherits a smooth $n^2$-manifold structure as an open subset of $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$. The prototype open-submanifold construction; the source of matrix Lie [[Def - Group|groups]]. ([[Def - Smooth Manifold]], [[Thm - Open Subset of a Smooth Manifold]])

- [[Ex - Compatibility of Two Atlases on the Sphere]] (⭐⭐) — Verify that the stereographic and graph-coordinate atlases on $S^n$ determine the same smooth structure. Drills the practical compatibility test of [[Thm - Smooth Structure from Maximal Atlas]] part (b). ([[Def - Smooth Atlas and Smooth Structure]], [[Def - Transition Function]], [[Thm - Smooth Structure from Maximal Atlas]])

- [[Ex - The Grassmannian is a Smooth Manifold]] (⭐⭐⭐) — Construct the smooth structure on the Grassmannian $G_k(V)$ of $k$-dimensional [[Def - Subspace|subspaces]] of an $n$-dimensional vector space $V$, with charts via graphs of linear maps and transition functions of matrix-Möbius form $X' = (B + DX)(A + CX)^{-1}$. The deepest example of the chapter, and the prototype for classifying spaces in topology. ([[Def - Smooth Manifold]], [[Def - Smooth Atlas and Smooth Structure]], [[Def - Vector Space]], [[Def - Linear Map]], [[Thm - Smooth Structure from Maximal Atlas]])

- **Ex (Lee Problem 1-9) — Complex projective space $\mathbb{CP}^n$.** Show $\mathbb{CP}^n$ — the set of complex one-dimensional linear [[Def - Subspace|subspaces]] of $\mathbb{C}^{n+1}$ — is a compact $2n$-dimensional smooth manifold. Construct $(n+1)$ affine charts with image $\mathbb{C}^n \cong \mathbb{R}^{2n}$ and holomorphic transition functions. The complex case of the projective-space construction; the prototype complex manifold. Identifying $\mathbb{C}^{n+1} \cong \mathbb{R}^{2n+2}$ gives the smooth structure; the *complex* structure is a refinement requiring holomorphic transitions. ([[Def - Smooth Manifold]], [[Def - Smooth Atlas and Smooth Structure]])
