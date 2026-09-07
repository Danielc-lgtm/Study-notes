---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Holonomy Group of a Principal Connection"
  - "Def - Gauge Group of a Principal Bundle"
  - "Def - Universal Cover"
tags: [gauge-theory, flat-connection, monodromy]
---

# Prerequisite Concepts

- [[Def - Holonomy Group of a Principal Connection]]
- [[Def - Gauge Group of a Principal Bundle]]
- [[Def - Universal Cover]]

# Statement

> [!theorem] Flat monodromy correspondence
> Let $M$ be connected with base point $x_0$ and let $G$ be a Lie group. Isomorphism classes of flat principal $G$-bundles with connection correspond naturally to conjugacy classes
> $$
> \operatorname{Hom}(\pi_1(M,x_0),G)/G.
> $$
> A based framing removes conjugation.

# Formal Proof

> [!proof]- Formal Proof
> Let $(P,\omega)$ be flat and choose $p_0\in P_{x_0}$. Flatness implies transport is invariant under endpoint-fixed homotopy: for a smooth homotopy of paths, the variation formula for parallel transport is the integral of the curvature conjugated by partial transports, so it vanishes; piecewise-smooth approximation handles arbitrary homotopies. Write $\operatorname{PT}_\gamma(p_0)=p_0h_\gamma$ and define
> $$
> \rho([\gamma])=h_\gamma^{-1}.
> $$
> This inverse is forced by the right principal action. We use the convention
> that $[\gamma_1][\gamma_2]$ means “first traverse $\gamma_1$, then traverse
> $\gamma_2$.” Equivariance of transport gives
> $$
> \operatorname{PT}_{\gamma_1*\gamma_2}(p_0)
> =\operatorname{PT}_{\gamma_2}(p_0h_{\gamma_1})
> =p_0h_{\gamma_2}h_{\gamma_1},
> $$
> and hence
> $$
> \rho([\gamma_1][\gamma_2])
> =(h_{\gamma_2}h_{\gamma_1})^{-1}
> =\rho([\gamma_1])\rho([\gamma_2]).
> $$
> Thus $\rho$ is a homomorphism. Replacing $p_0$ by $p_0g$ replaces
> $h_\gamma$ by $g^{-1}h_\gamma g$ and therefore conjugates $\rho$ by $g^{-1}$.
>
> Conversely let $\rho:\pi_1(M,x_0)\to G$. Let $\widetilde M$ be the universal cover with deck action written on the left. Define
> $$
> P_\rho=(\widetilde M\times G)/\pi_1(M),\qquad
> \gamma\cdot(\widetilde x,h)=(\gamma\widetilde x,\rho(\gamma)h).
> $$
> The action is free and properly discontinuous and commutes with right multiplication on $G$, so $P_\rho\to M$ is principal. The product horizontal distribution $T\widetilde M\oplus0$ is invariant under the action and descends to a flat connection. Lifting a loop to $\widetilde M$ shows its endpoint differs by the deck transformation $\gamma$. Since
> $[\gamma\widetilde x_0,e]=[\widetilde x_0,\rho(\gamma)^{-1}]$, its descended
> transport has right holonomy $h_\gamma=\rho(\gamma)^{-1}$; the preceding
> extraction $h_\gamma^{-1}$ therefore recovers $\rho(\gamma)$ exactly.
>
> Applying the two constructions successively recovers the original framed flat bundle: send $[\widetilde x,h]$ to the endpoint of parallel transport of $p_0h$ along the projected path represented by $\widetilde x$. Homotopy invariance makes this well defined, and it is an equivariant connection-preserving isomorphism. Changing the framing conjugates $\rho$, completing the correspondence.

# What Makes This Hard

With right principal actions, path concatenation and group multiplication can appear in reverse order. One must declare both conventions rather than silently calling an antihomomorphism a representation.

# Rederivation Scaffold

Flatness makes transport depend only on homotopy class. In the reverse direction, quotient the product connection on the universal cover by the prescribed deck action.
