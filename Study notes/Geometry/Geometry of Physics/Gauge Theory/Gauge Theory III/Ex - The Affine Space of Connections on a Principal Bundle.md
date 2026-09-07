---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Adjoint Bundle"
  - "Def - Exterior Covariant Derivative on Associated Bundles"
tags: [geometry, gauge-theory, principal-bundles, affine-spaces, moduli]
---

# Prerequisite Concepts

- [[Def - Connection 1-Form on a Principal Bundle]]
- [[Def - Adjoint Bundle]]
- [[Def - Exterior Covariant Derivative on Associated Bundles]]

# Problem Statement

Prove that the space $\mathcal A(P)$ of principal connections on $P\to M$ is an affine space modeled on $\Omega^1(M;\operatorname{Ad}P)$. If $A_0$ is a reference connection and $a$ an adjoint-valued one-form, prove
$$F_{A_0+a}=F_{A_0}+d_{A_0}a+\frac12[a,a].$$

# Solution

> [!solution]- Solution
> If $\omega_1,\omega_0$ are connection forms, then
> $(\omega_1-\omega_0)(\xi_P)=\xi-\xi=0$, so their difference is horizontal.
> Their equivariance laws subtract to give
> $R_g^*(\omega_1-\omega_0)=\operatorname{Ad}_{g^{-1}}(\omega_1-\omega_0)$.
> Horizontal equivariant $\mathfrak g$-valued forms on $P$ correspond exactly
> to $\operatorname{Ad}P$-valued forms on $M$: at $x$, evaluate on any lift of
> each tangent vector at any $p\in P_x$ and take the associated class
> $[p,\xi]$. Horizontality makes the lift irrelevant and equivariance makes
> $p$ irrelevant.
>
> Conversely, adding the horizontal equivariant representative of any
> $a\in\Omega^1(M;\operatorname{Ad}P)$ to $\omega_0$ preserves reproduction
> and equivariance. This action is free and transitive, which is precisely the
> assertion that $\mathcal A(P)$ is affine rather than canonically a vector space.
>
> In a gauge, expand the structural equation:
> $$
> \begin{aligned}
> F_{A_0+a}
> &=d(A_0+a)+\tfrac12[A_0+a,A_0+a]\\
> &=F_{A_0}+da+[A_0,a]+\tfrac12[a,a].
> \end{aligned}
> $$
> Graded skew-symmetry gives $[a,A_0]=[A_0,a]$ because both forms have degree
> one, and $d_{A_0}a=da+[A_0,a]$. Every term transforms adjointly, so the local
> identity is the claimed global identity.

# Rederivation Scaffold

Subtract the inhomogeneous objects: the reproduction terms cancel, leaving a tensor.
