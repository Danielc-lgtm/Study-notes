---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Horizontal Subspace"
tags: [gauge-theory, principal-connection, horizontal-distribution]
---

# Statement

> [!theorem] Two equivalent definitions
> Principal connection forms on $P\to M$ are in bijection with smooth right-invariant horizontal complements $TP=H\oplus VP$. The correspondence is
> $$\omega\longmapsto\ker\omega.$$

# Why Is It True

A connection form is a vertical-coordinate projection. Conversely, a horizontal complement lets one project to the vertical space and then use the canonical isomorphism $V_pP\cong\mathfrak g$.

# Formal Proof

> [!proof]- Formal Proof
> Let $\omega$ be a connection form. Since $\omega|_{V_p}$ is inverse to $\xi\mapsto\xi_P(p)$, it is an isomorphism. Hence $H_p=\ker\omega_p$ is a complement to $V_p$. Constant rank makes $H$ smooth. If $X\in H_p$, equivariance gives
> $$\omega_{pg}(dR_gX)=\operatorname{Ad}_{g^{-1}}\omega_p(X)=0,$$
> so $H$ is right invariant.
>
> Conversely let $H$ be such a complement. Write $X=X^H+X^V$ and let $\omega_p(X)$ be the unique $\xi$ with $X^V=\xi_P(p)$. Smoothness follows from the smooth splitting and the smooth vertical trivialization $P\times\mathfrak g\to VP$. It immediately gives $\omega(\xi_P)=\xi$. For $X^V=\xi_P(p)$, right equivariance of $H$ and the fundamental-field transformation law give
> $$(dR_g)X^V=(\operatorname{Ad}_{g^{-1}}\xi)_P(pg).$$
> Therefore $\omega_{pg}(dR_gX)=\operatorname{Ad}_{g^{-1}}\omega_p(X)$.
>
> Starting from $\omega$, the reconstructed form vanishes on $\ker\omega$ and agrees with $\omega$ on $VP$, hence agrees on their direct sum. Starting from $H$, the kernel of the constructed form is exactly $H$. Thus the constructions are inverse.

# Rederivation Scaffold

Use $V_pP\cong\mathfrak g$. A complement determines a projection onto $V_pP$, and composing with this isomorphism gives $\omega$; taking the kernel reverses the construction.
