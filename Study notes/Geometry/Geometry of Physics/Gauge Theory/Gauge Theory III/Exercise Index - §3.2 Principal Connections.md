---
type: exercise-index
subject: gauge-theory
section: "3.2"
tags: [geometry, gauge-theory, principal-bundles, connections]
---

## §3.2 Principal Connections — Exercises

This section introduces the central object of the chapter: a **principal connection** on a principal $G$-bundle $P \to M$, defined as a $\mathfrak{g}$-valued 1-form $\omega$ on the total space satisfying *verticality* (recovers the Lie-algebra element on fundamental vector fields) and *equivariance* (transforms under the adjoint action of $G$). The exercises drill the *correspondence* between this 1-form picture (algebraic) and the horizontal-distribution picture (geometric), the *pullback* to the base via a local section (giving the gauge potential $A$), and the *gauge transformation law* $A' = g^{-1}Ag + g^{-1}dg$ that records change of section. Three exercises probe three different facets of this material: the Levi-Civita connection as a principal connection on the orthonormal frame bundle (bridging Riemannian geometry to principal-bundle gauge theory), the electromagnetic $U(1)$-connection in the abelian special case (the prototype), and the *affine structure* of the space of connections (foundational for moduli theory).

- [[Ex - Connection on the Frame Bundle of a Riemannian Manifold from Levi-Civita]] (⭐⭐) — the Levi-Civita connection on a Riemannian manifold is equivalent to a principal connection on the orthonormal frame bundle $F^O(M)$ (a principal $O(n)$-bundle), with local gauge potential equal to the matrix of Cartan connection 1-forms $\omega^a{}_b$; verification of verticality and equivariance ([[Def - Connection 1-Form on a Principal Bundle]], [[Def - Levi-Civita Connection]], [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]], [[Riemannian Geometry I — Connections and Covariant Differentiation]])

- [[Ex - Local Connection 1-Form of the Electromagnetic Bundle]] (⭐) — explicit principal $U(1)$-connection on the trivial bundle, pullback to electromagnetic 4-potential, and verification of the gauge transformation law $A \mapsto A + id\chi$ in the abelian case ([[Def - Connection 1-Form on a Principal Bundle]], [[Def - Local Connection 1-Form (Gauge Potential)]], [[Thm - Gauge Transformation Law for Local Connection 1-Forms]])

- [[Ex - The Affine Space of Connections on a Principal Bundle]] (⭐⭐⭐) — the difference of two connections is a horizontal equivariant 1-form on $P$, equivalently a 1-form section of $\mathrm{Ad}\,P$; the space $\mathcal{A}(P)$ of connections is therefore an affine space modelled on $\Omega^1(M; \mathrm{Ad}\,P)$; foundational for Yang-Mills moduli theory ([[Def - Connection 1-Form on a Principal Bundle]], [[Def - Adjoint Bundle]], [[Thm - Gauge Transformation Law for Local Connection 1-Forms]], [[Def - Exterior Covariant Derivative on Associated Bundles]])
