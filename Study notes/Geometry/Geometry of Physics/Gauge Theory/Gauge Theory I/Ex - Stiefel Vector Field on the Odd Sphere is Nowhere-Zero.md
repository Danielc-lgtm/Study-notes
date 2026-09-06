---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Thm - Hairy Ball Theorem"
tags: [geometry, topology, sphere]
---

# Problem Statement

Let $J:\mathbb R^{2k+2}\to\mathbb R^{2k+2}$ be
$$J(x_1,x_2,\ldots,x_{2k+1},x_{2k+2})=(-x_2,x_1,\ldots,-x_{2k+2},x_{2k+1}).$$
Show that $v(x)=Jx$ is a smooth unit tangent vector field on $S^{2k+1}$, and independently verify $\chi(S^{2k+1})=0$ from its standard CW decomposition.

# Solution

> [!proof]- Solution
> The matrix $J$ is skew-symmetric and orthogonal: $J^T=-J$ and $J^TJ=I$. Hence, for $x\in S^{2k+1}$,
> $$\langle x,Jx\rangle=\langle J^Tx,x\rangle=-\langle Jx,x\rangle=0.$$
> Thus $Jx\in x^\perp=T_xS^{2k+1}$. Orthogonality gives
> $$\lVert Jx\rVert=\lVert x\rVert=1,$$
> so the field never vanishes. It is smooth because it is the restriction of a linear map.
>
> The standard CW decomposition of $S^{2k+1}$ has one $0$-cell and one
> $(2k+1)$-cell, so its alternating cell count is $1-1=0$. Thus
> $\chi(S^{2k+1})=0$, consistently with the existence of the field.

# Key Takeaways

Under $\mathbb R^{2k+2}\cong\mathbb C^{k+1}$, $J$ is multiplication by $i$. Complex structure automatically supplies a tangent direction perpendicular to the radius.
