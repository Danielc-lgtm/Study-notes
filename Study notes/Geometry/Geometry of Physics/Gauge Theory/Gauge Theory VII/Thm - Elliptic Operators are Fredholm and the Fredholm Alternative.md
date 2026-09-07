---
type: theorem
subject: gauge-theory
prereqs: ["Thm - Elliptic Estimate and Regularity", "Def - Fredholm Operator and Index"]
tags: [gauge-theory, elliptic-operator, fredholm-alternative]
---

# Prerequisite Concepts

- [[Thm - Elliptic Estimate and Regularity]]
- [[Def - Fredholm Operator and Index]]

# Statement

> [!theorem] Elliptic Fredholm theorem
> On a closed manifold, an elliptic operator of order $\ell$ extends to a Fredholm map
> $$L:W^{k+\ell,2}(E)\to W^{k,2}(F),$$
> and its kernel consists of smooth sections. Moreover,
> $$\operatorname{im}L=(\ker L^*)^\perp.$$
> Hence $Ls=t$ is solvable exactly when $t$ is orthogonal to every element of $\ker L^*$.

# Formal Proof

> [!proof]- Formal Proof
> Elliptic regularity makes every weak kernel element smooth. The elliptic estimate and Rellich compactness imply that the unit ball in $\ker L$ is compact: on the kernel the estimate bounds $W^{k+\ell,2}$ by the weaker norm, and a contradiction argument upgrades convergence in the weaker norm to convergence in the stronger norm. A normed space with compact unit ball is finite dimensional.
>
> The same argument applies to $L^*$. A second contradiction argument using the elliptic estimate on $(\ker L)^\perp$ proves $\|s\|_{W^{k+\ell,2}}\le C\|Ls\|_{W^{k,2}}$ there; this coercive estimate makes $\operatorname{im}L$ closed. Hilbert-space duality gives $(\operatorname{im}L)^\perp=\ker L^*$, so the cokernel is naturally $\ker L^*$ and is finite dimensional. This proves Fredholmness and the image formula. The solvability criterion follows immediately.

# Source Correction

The condition is $t\perp\ker L^*$, not $t\in\ker L^*$. For a self-adjoint Laplacian, for example, Poisson's equation is solvable precisely when the source is orthogonal to constants.

