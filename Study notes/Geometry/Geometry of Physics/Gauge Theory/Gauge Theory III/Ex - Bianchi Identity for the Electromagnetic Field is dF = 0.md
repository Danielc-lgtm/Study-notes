---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Bianchi Identity for Principal Connections"
  - "Def - Curvature 2-Form on a Principal Bundle"
  - "Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection"
tags: [geometry, gauge-theory, electromagnetism, maxwell, bianchi]
---

# Prerequisite Concepts

- [[Thm - Bianchi Identity for Principal Connections]]
- [[Def - Curvature 2-Form on a Principal Bundle]]
- [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]]

# Problem Statement

Let $F\in\Omega^2(M;i\mathbb R)$ be the curvature of a principal $U(1)$-connection.

1. Derive $dF=0$ from the principal Bianchi identity.
2. On Minkowski space with coordinates $(t,x^1,x^2,x^3)$, use
   $$F=E_i\,dt\wedge dx^i-\frac12\varepsilon_{ijk}B^k\,dx^i\wedge dx^j$$
   and show that $dF=0$ is equivalent to
   $$\nabla\cdot B=0,\qquad \partial_tB+\nabla\times E=0.$$
3. Explain why $dF=0$ implies local, but not necessarily global, existence of a potential.

# Solution

> [!solution]- Solution
> For $U(1)$ the Lie algebra is abelian, so the bracket of any two $i\mathbb R$-valued forms vanishes. The Bianchi identity
> $$d_AF=dF+[A,F]=0$$
> therefore reduces to $dF=0$.
>
> Differentiate the displayed decomposition. Since $d(dt)=d(dx^i)=0$,
> $$
> dF=(\partial_jE_i)\,dx^j\wedge dt\wedge dx^i
> -\frac12(\partial_tB^k)\varepsilon_{ijk}\,dt\wedge dx^i\wedge dx^j
> -\frac12(\partial_\ell B^k)\varepsilon_{ijk}\,dx^\ell\wedge dx^i\wedge dx^j.
> $$
> The coefficient of $dt\wedge dx^i\wedge dx^j$ is
> $-\partial_iE_j+\partial_jE_i-\varepsilon_{ijk}\partial_tB^k$.
> Contracting it with $-\tfrac12\varepsilon^{mij}$ gives
> $(\nabla\times E)^m+\partial_tB^m$. The coefficient of
> $dx^1\wedge dx^2\wedge dx^3$ is $-\partial_kB^k$. Hence $dF=0$
> gives exactly the two stated equations, and the converse follows because these
> are all independent coefficients of the three-form $dF$.
>
> On every contractible coordinate ball, the Poincaré lemma turns $dF=0$ into
> $F=dA$. Globally, closedness need not imply exactness: the obstruction is the
> de Rham class $[F]$, whose normalized periods encode the first Chern class.
> Thus the local Bianchi identity does **not** by itself exclude a topologically
> nontrivial monopole bundle; it excludes a magnetic-current term $dF\ne0$ on
> the region where the smooth bundle connection is defined.

# Why This Matters

The homogeneous Maxwell equations are kinematic: they follow from curvature and the abelian Bianchi identity. The sourced equations are dynamical and require an action or constitutive law.

# Rederivation Scaffold

Set the Lie bracket to zero, then read the temporal and spatial coefficients of the three-form $dF$ separately.
