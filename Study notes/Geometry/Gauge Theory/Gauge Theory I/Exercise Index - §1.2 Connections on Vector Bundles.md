---
type: exercise-index
subject: gauge-theory
section: "1.2"
tags: [geometry, gauge-theory, connection, curvature]
---

## §1.2 Connections on Vector Bundles — Exercises

This section drills the basic computational techniques for connections and curvature on vector bundles. The exercises proceed from the simplest case (trivial bundle, trivial connection, zero curvature) to the prototype non-trivial example (tangent bundle of $S^2$ with the round metric, where curvature reproduces Gaussian curvature and integrates to Gauss-Bonnet). The structure-equation method $F = d\omega + \omega \wedge \omega$ and the orthonormal-frame approach are the two main techniques drilled. The supplementary cross-link to the DG XII exercise on the Riemannian metric of $S^2$ provides background on how the round metric arises from restriction of the ambient Euclidean inner product.

- [[Ex - Curvature of a Trivial Bundle with Trivial Connection is Zero]] (⭐) — Verifies that the trivial connection on $M \times \mathbb{R}^K$ has $\omega = 0$ in the global frame, hence $F = 0$. Establishes the contrapositive: non-zero curvature in any frame is an obstruction to a global flat trivialization ([[Def - Connection on a Vector Bundle]], [[Def - Curvature of a Vector-Bundle Connection]], [[Def - Vector Bundle]])
- [[Ex - Connection on the Tangent Bundle of S^2 from the Round Metric]] (⭐⭐) — Computes the Levi-Civita connection 1-form in an orthonormal frame on $S^2$ via the first structure equation, gets $\omega^1{}_2 = -\cos\theta\,d\phi$, and computes the curvature $F^1{}_2 = \sin\theta\,d\theta \wedge d\phi$, integrating to $4\pi = 2\pi\chi(S^2)$ — the Gauss-Bonnet theorem ([[Def - Curvature of a Vector-Bundle Connection]], [[Thm - Poincare-Hopf Theorem]])
- [[Ex - The Round Metric on the Sphere via Restriction]] (⭐) — *Supplementary, from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].* Constructs the round metric $g = d\theta^2 + \sin^2\theta\,d\phi^2$ by restricting the ambient Euclidean inner product to the tangent space of the unit sphere $S^2 \subset \mathbb{R}^3$. This is the geometric prerequisite for the Levi-Civita connection computation in the previous exercise — establishing the metric whose orthonormal frame we use ([[Def - Riemannian Metric]])
