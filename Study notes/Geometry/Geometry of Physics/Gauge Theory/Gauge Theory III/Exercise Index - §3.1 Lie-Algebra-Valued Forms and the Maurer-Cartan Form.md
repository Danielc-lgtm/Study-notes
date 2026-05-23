---
type: exercise-index
subject: gauge-theory
section: "3.1"
tags: [geometry, gauge-theory, lie-groups, differential-forms]
---

## §3.1 Lie-Algebra-Valued Forms and the Maurer-Cartan Form — Exercises

This section introduces the universal language of gauge theory: $\mathfrak{g}$-valued differential forms on a manifold, equipped with an exterior derivative and a graded Lie bracket. The exercises drill the *canonical example* of such a form — the **Maurer-Cartan form** on a Lie group $G$, which left-translates each tangent vector back to the identity. The Maurer-Cartan form satisfies the **Maurer-Cartan equation** $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$, the universal template against which the curvature of every connection is measured. Computing $\theta_G$ explicitly for matrix Lie groups (especially $SU(2)$) and verifying the Maurer-Cartan equation is the foundational calculation that establishes the structural equation pattern used throughout the rest of the chapter.

- [[Ex - The Maurer-Cartan Form on SU(2)]] (⭐⭐) — explicit matrix-group computation of $\theta_G = g^{-1}dg$ on $SU(2)$, identification of three left-invariant 1-forms $\tilde\sigma^a$ on $SU(2) \cong S^3$, and verification of the Maurer-Cartan equation $d\tilde\sigma^a + \tfrac{1}{2}\varepsilon^a{}_{bc}\tilde\sigma^b \wedge \tilde\sigma^c = 0$ ([[Def - The Maurer-Cartan Form]], [[Thm - Maurer-Cartan Equation]], [[Def - Bracket of g-Valued Forms]], [[Def - The Lie Algebra of a Lie Group]])

- [[Ex - Local Connection 1-Form of the Electromagnetic Bundle]] (⭐) — explicit $U(1)$-connection $\omega = id\theta + iA_\mu dx^\mu$ on the trivial $U(1)$-bundle over Minkowski space, the canonical section's pullback giving the electromagnetic 4-potential, and the abelian gauge transformation $A \mapsto A + id\chi$ as the special case of $A \mapsto g^{-1}Ag + g^{-1}dg$ for $g = e^{i\chi}$ ([[Def - Local Connection 1-Form (Gauge Potential)]], [[Def - Connection 1-Form on a Principal Bundle]], [[Def - The Maurer-Cartan Form]])

- [[Ex - The Affine Space of Connections on a Principal Bundle]] (⭐⭐⭐) — the difference of two connections is a horizontal equivariant 1-form on $P$, equivalently a 1-form section of the adjoint bundle, hence $\mathcal{A}(P)$ is an affine space modelled on $\Omega^1(M; \mathrm{Ad}\,P)$; plus the curvature expansion $F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta]$ — touches the Maurer-Cartan template through the affine perturbation analysis ([[Def - Connection 1-Form on a Principal Bundle]], [[Def - Adjoint Bundle]], [[Thm - Gauge Transformation Law for Local Connection 1-Forms]])
