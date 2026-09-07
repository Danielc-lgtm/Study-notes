---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Hopf Bundle"
  - "Def - Homogeneous Bundle"
tags: [gauge-theory, hopf-fibration, quaternions]
---

# Prerequisite Concepts

- [[Def - The Hopf Bundle]]
- [[Def - Homogeneous Bundle]]

# Problem Statement

Identify $S^3$ with unit quaternions and $S^2$ with unit imaginary quaternions. For
$$\pi(q)=q\mathbf i q^{-1},$$
prove that $\pi:S^3\to S^2$ is the quotient by the right action of
$U(1)=\{e^{\mathbf i\theta}\}$.

# Solution

> [!proof]- Solution
> Quaternionic norm is multiplicative, so $|q\mathbf iq^{-1}|=1$. Conjugation preserves real part, and $\mathbf i$ has real part zero; hence $\pi(q)\in S^2\subset\operatorname{Im}\mathbb H$.
>
> If $z=e^{\mathbf i\theta}$, then $z$ commutes with $\mathbf i$, and
> $$\pi(qz)=qz\mathbf iz^{-1}q^{-1}=q\mathbf iq^{-1}=\pi(q).$$
> Conversely, if $\pi(q')=\pi(q)$, then $a=q^{-1}q'$ satisfies $a\mathbf ia^{-1}=\mathbf i$, so $a$ commutes with $\mathbf i$. Writing $a=a_0+a_1\mathbf i+a_2\mathbf j+a_3\mathbf k$ and comparing $a\mathbf i$ with $\mathbf ia$ gives $a_2=a_3=0$. Since $|a|=1$, $a=e^{\mathbf i\theta}$. Thus each fibre is exactly one right $U(1)$-orbit.
>
> The action is free, compact, and therefore proper, so its orbit space is a smooth manifold and the quotient map is a principal $U(1)$-bundle. The preceding fibre calculation identifies the induced bijection $S^3/U(1)\to S^2$; local slice charts make it a diffeomorphism.

# Key Takeaways

The Hopf map is conjugation, and its fibres are stabilizer cosets. This is simultaneously a principal bundle and the homogeneous-space description $S^2\cong SU(2)/U(1)$.
