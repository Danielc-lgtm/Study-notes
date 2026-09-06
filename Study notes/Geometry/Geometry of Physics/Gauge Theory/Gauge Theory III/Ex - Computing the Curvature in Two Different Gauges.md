---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cartan Structural Equation for Principal Connections"
  - "Thm - Gauge Transformation Law for Local Connection 1-Forms"
tags: [geometry, gauge-theory, yang-mills, curvature]
---

# Problem Statement

Let $T_a=-i\sigma_a/2$, so $[T_a,T_b]=\varepsilon_{ab}{}^cT_c$, and write
$A=T_aA^a_\mu dx^\mu$. Compute $F=dA+A\wedge A$. Then prove directly that
$A^g=g^{-1}Ag+g^{-1}dg$ has curvature $F^g=g^{-1}Fg$, and specialize to
$g=e^{\chi T_3}$.

# Solution

> [!solution]- Solution
> Since the symmetric part of $T_aT_b$ multiplies the antisymmetric wedge,
> $$A\wedge A=\frac12[T_a,T_b]A^a_\mu A^b_\nu,dx^\mu\wedge dx^\nu.$$
> Therefore $F=\tfrac12T_aF^a_{\mu\nu}dx^\mu\wedge dx^\nu$, where
> $$F^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu
> +\varepsilon_{bc}{}^aA^b_\mu A^c_\nu.$$
> The last term disappears for an abelian Lie algebra.
>
> Put $\theta=g^{-1}dg$. The product rule gives
> $d(g^{-1})=-g^{-1}(dg)g^{-1}$, while the Maurer–Cartan equation gives
> $d\theta+\theta\wedge\theta=0$. Expanding without suppressing cross terms,
> $$
> \begin{aligned}
> dA^g+A^g\wedge A^g
> &=d(g^{-1}Ag)+d\theta+(g^{-1}Ag+\theta)^2\\
> &=g^{-1}(dA+A\wedge A)g.
> \end{aligned}
> $$
> The terms containing one copy of $\theta$ cancel those arising from
> differentiating $g^{-1}$ and $g$, and the two pure-$\theta$ terms cancel by
> Maurer–Cartan. Hence $F^g=g^{-1}Fg$.
>
> For $g=e^{\chi T_3}$, $g^{-1}dg=T_3d\chi$. Moreover
> $\operatorname{Ad}_{g^{-1}}$ fixes $T_3$ and solves
> $\frac d{d\chi}\operatorname{Ad}_{e^{-\chi T_3}}T_1=-[T_3,operatorname{Ad}_{e^{-\chi T_3}}T_1]$;
> thus
> $$\operatorname{Ad}_{g^{-1}}T_1=\cos\chi,T_1-\sin\chi,T_2,
> \quad \operatorname{Ad}_{g^{-1}}T_2=\sin\chi,T_1+\cos\chi,T_2.$$
> Consequently $A^g=\operatorname{Ad}_{g^{-1}}A+T_3d\chi$ while
> $F^g=\operatorname{Ad}_{g^{-1}}F$: the $1$- and $2$-components rotate by the
> displayed matrix and the $3$-component is fixed.

# Rederivation Scaffold

The inhomogeneous Maurer–Cartan term is exactly what cancels derivatives of the gauge function in curvature.
