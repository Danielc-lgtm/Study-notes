---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Brouwer Degree of a Map"
  - "Def - The Tangent Bundle"
tags: [geometry, topology, sphere]
---

# Prerequisite Concepts

- [[Def - Brouwer Degree of a Map]]
- [[Def - The Tangent Bundle]]

# Statement

> [!theorem] Hairy-ball theorem
> Every continuous tangent vector field on $S^{2k}$ has a zero. Conversely, every odd-dimensional sphere has a smooth nowhere-zero tangent vector field.

# Why Is It True

A hypothetical nonzero tangent field on an even sphere would give a homotopy from the identity map to the antipodal map. Those maps have different degrees. Odd spheres admit an explicit field obtained by multiplication by $i$ on $\mathbb C^{k+1}$.

# Formal Proof

> [!proof]- Formal Proof
> Suppose $v$ is nowhere zero on $S^n$ and set $u(x)=v(x)/\lVert v(x)\rVert$. Since $u(x)\perp x$, the map
> $$H(x,t)=\cos(\pi t)x+\sin(\pi t)u(x)$$
> has norm one for every $(x,t)$. It is a homotopy from $H(x,0)=x$ to $H(x,1)=-x$. Homotopy invariance of degree would therefore give
> $$1=\deg(\operatorname{id}_{S^n})=\deg(-\operatorname{id}_{S^n})=(-1)^{n+1}.$$
> When $n$ is even the right side is $-1$, a contradiction. Thus every tangent field on $S^{2k}$ vanishes somewhere.
>
> If $n=2k+1$, regard $\mathbb R^{2k+2}$ as $\mathbb C^{k+1}$ and define $v(z)=iz$. Then $\langle z,iz\rangle_{\mathbb R}=0$, so $v(z)\in T_zS^{2k+1}$, and $\lVert v(z)\rVert=\lVert z\rVert=1$. Hence $v$ is a smooth nowhere-zero tangent field.

# Bridges

For $S^2$, [[Thm - Poincare-Hopf Theorem]] gives the same obstruction because $\chi(S^2)=2$.
