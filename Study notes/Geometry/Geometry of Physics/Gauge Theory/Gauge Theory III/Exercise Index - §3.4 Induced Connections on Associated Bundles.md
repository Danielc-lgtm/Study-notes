---
type: exercise-index
subject: gauge-theory
section: "3.4"
tags: [geometry, gauge-theory, associated-bundles, connections]
---

## §3.4 Induced Connections on Associated Bundles — Exercises

This section delivers the *unifying power* of the principal-bundle formalism: a *single* principal connection induces connections on *every* associated vector bundle via every representation $\rho : G \to \mathrm{GL}(V)$. The induced covariant derivative is $\nabla^\rho = d + d\rho(A)$ in any local trivialisation, where $d\rho : \mathfrak{g} \to \mathfrak{gl}(V)$ is the Lie-algebra differential of $\rho$. The exercises probe the two most important special cases: the **adjoint bundle** $\mathrm{Ad}\,P$ (with $\rho = \mathrm{Ad}$, the home of the curvature and infinitesimal gauge transformations), and the bridge to **classical Riemannian geometry** via the orthonormal frame bundle (where the Levi-Civita connection is the principal connection and the defining rep of $O(n)$ on $\mathbb{R}^n$ gives the tangent bundle $TM$).

- [[Ex - Connection on the Frame Bundle of a Riemannian Manifold from Levi-Civita]] (⭐⭐) — the Levi-Civita connection on $TM$ is exactly the induced connection on the associated bundle $F^O(M) \times_\rho \mathbb{R}^n = TM$ (with $\rho : O(n) \hookrightarrow \mathrm{GL}(n)$ the defining rep), with local gauge potential equal to the Cartan connection 1-forms $\omega^a{}_b$ of Riemannian geometry ([[Thm - Principal Connection Induces a Connection on Every Associated Bundle]], [[Def - Levi-Civita Connection]], [[Def - Connection 1-Form on a Principal Bundle]], [[Riemannian Geometry I — Connections and Covariant Differentiation]])

- [[Ex - Adjoint Bundle of a U(1)-Bundle is Trivial]] (⭐) — for $G = U(1)$ abelian, the adjoint action is trivial, $\mathrm{Ad}\,P = M \times \mathfrak{u}(1)$ is the trivial line bundle, and the induced connection on $\mathrm{Ad}\,P$ is just the exterior derivative $d$ (no twisting) — consequence: the electromagnetic field strength is a globally defined 2-form on $M$, gauge-invariant in the strong sense ([[Def - Adjoint Bundle]], [[Def - Adjoint Representation]], [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]])

- [[Ex - The Affine Space of Connections on a Principal Bundle]] (⭐⭐⭐) — the affine space $\mathcal{A}(P)$ modelled on $\Omega^1(M; \mathrm{Ad}\,P)$ relies on the *induced connection on $\mathrm{Ad}\,P$* (via $\rho = \mathrm{Ad}$, giving $\nabla\psi = d\psi + [A, \psi]$); the curvature expansion $F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta]$ explicitly uses the exterior covariant derivative on $\mathrm{Ad}\,P$-valued forms ([[Def - Adjoint Bundle]], [[Def - Exterior Covariant Derivative on Associated Bundles]], [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]], [[Def - Connection 1-Form on a Principal Bundle]])
