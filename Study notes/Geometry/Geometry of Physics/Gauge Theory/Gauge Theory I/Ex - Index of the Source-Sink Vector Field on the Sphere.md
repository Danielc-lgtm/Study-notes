---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Index of a Vector Field at a Zero"
  - "Thm - Poincare-Hopf Theorem"
tags: [geometry, topology, index, sphere]
---

# Problem Statement

On the unit sphere let $z:S^2\to\mathbb R$ be the height function and let $v=\operatorname{grad}z$. Find its zeros, compute their indices, and check Poincaré–Hopf.

> [!warning] Coordinate trap
> The coordinate vector $\partial_\theta$ does **not** extend continuously to either pole: its limiting ambient direction depends on $\varphi$. The smooth field is $\operatorname{grad}z=-\sin\theta\,\partial_\theta$.

# Convergent Strategy

Use tangent-plane coordinates near each pole. A nondegenerate zero has index equal to the sign of the determinant of the derivative matrix.

# Solution

> [!proof]- Solution
> Since $z=\cos\theta$ and the round metric is $d\theta^2+\sin^2\theta,d\varphi^2$,
> $$v=\operatorname{grad}z=-\sin\theta\,\partial_\theta.$$
> It vanishes exactly at the north and south poles.
>
> Near the north pole write the sphere as $(x,y,\sqrt{1-x^2-y^2})$. Then
> $$z=1-\frac{x^2+y^2}{2}+O(\lVert(x,y)\rVert^4),$$
> so the derivative of $\operatorname{grad}z$ at the origin is $-I_2$. Its determinant is positive, hence the north-pole index is $+1$.
>
> Near the south pole use the oriented chart $(x,-y)$ on the graph $(x,y,-\sqrt{1-x^2-y^2})$; equivalently note that $z$ has a nondegenerate minimum there. The Hessian is positive definite, so the derivative of the gradient has positive determinant and the index is again $+1$. Thus
> $$\sum_p\operatorname{ind}_p(v)=1+1=2=\chi(S^2).$$

# Key Takeaways

A coordinate singularity is not automatically a zero of a vector field. Verify smooth extension before computing an index.
