---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Hopf Bundle"
  - "Def - Universal Bundle and Classifying Space"
tags: [gauge-theory, hopf-fibration, su2, quaternionic]
---

# Prerequisite Concepts

- [[Def - The Hopf Bundle]]
- [[Def - Universal Bundle and Classifying Space]]

# Problem Statement

Let $Sp(1)=\{q\in\mathbb H:|q|=1\}\cong SU(2)$ act on
$S^7\subset\mathbb H^2$ on the right by $(u,v)q=(uq,vq)$. Prove that the action is free, identify the orbit space with $\mathbb{HP}^1\cong S^4$, and explain why this bundle is the restriction of $ESU(2)\to BSU(2)$ to the four-skeleton.

# Solution

> [!proof]- Solution
> If $(u,v)q=(u,v)$, then at least one of $u,v$ is nonzero. Since $\mathbb H$ is a division algebra, $uq=u$ or $vq=v$ implies $q=1$; the action is free. Its orbits are precisely the nonzero quaternionic scalar multiples of $(u,v)$ after normalization, hence the quotient is the quaternionic projective line $\mathbb{HP}^1$.
>
> The charts $u\ne0$ and $v\ne0$ identify $\mathbb{HP}^1$ with $\mathbb H\cup\{\infty\}$ by $[u:v]\mapsto vu^{-1}$ and the complementary coordinate. One-point compactification identifies $\mathbb H\cup\{\infty\}\cong S^4$. Thus
> $$Sp(1)\longrightarrow S^7\longrightarrow S^4$$
> is a principal $SU(2)$-bundle.
>
> In the infinite-dimensional model, $ESU(2)=S^\infty\subset\mathbb H^\infty$ and $BSU(2)=\mathbb{HP}^\infty$. Its first two cells are in dimensions $0$ and $4$, so the four-skeleton is $\mathbb{HP}^1$. Restricting the universal sphere bundle to it gives exactly $S^7\to S^4$.

# Key Takeaways

The complex Hopf bundle detects $H^2$ and $U(1)$ charge; the quaternionic Hopf bundle detects $H^4$ and the basic $SU(2)$ instanton sector.
