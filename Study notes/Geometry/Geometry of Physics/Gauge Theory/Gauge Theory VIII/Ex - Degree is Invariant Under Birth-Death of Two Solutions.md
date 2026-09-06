---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs: ["Def - Integer Degree of an Oriented Fredholm Map"]
tags: [gauge-theory, degree, cobordism]
---

# Problem Statement

For $f_t(x)=x^2-t$ on $\mathbb R$, explain why the unsigned number of zeros changes at $t=0$ but the signed degree does not.

# Solution

> [!solution]- Solution
> For $t<0$ there are no zeros. For $t>0$ the zeros are $\pm\sqrt t$, with derivative signs $-1$ and $+1$. Their signed sum is zero, matching the empty fibre. The universal zero set $x^2=t$ is a smooth parabola; the apparent birth is a tangency of a nonregular slice, and the two regular solutions appear with opposite boundary orientations. Modulo two they also cancel.
