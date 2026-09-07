---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature 2-Form on a Principal Bundle"
  - "Def - Exterior Covariant Derivative on Associated Bundles"
tags: [gauge-theory, curvature, Bianchi]
---

# Prerequisite Concepts

- [[Def - Curvature 2-Form on a Principal Bundle]]
- [[Def - Exterior Covariant Derivative on Associated Bundles]]

# Statement

> [!theorem] Bianchi identity
> For $\Omega=d\omega+\tfrac12[\omega,\omega]$,
> $$d_\omega\Omega:=d\Omega+[\omega,\Omega]=0.$$
> Locally, $d_AF_A=dF_A+[A,F_A]=0$.

# Formal Proof

> [!proof]- Formal Proof
> The graded derivation rule and $\deg\omega=1$ give
> $$
> d\Omega=\tfrac12d[\omega,\omega]
> =\tfrac12([d\omega,\omega]-[\omega,d\omega])=[d\omega,\omega],
> $$
> because graded antisymmetry gives $[\omega,d\omega]=-[d\omega,\omega]$. Also
> $$[\omega,\Omega]=[\omega,d\omega]+\tfrac12[\omega,[\omega,\omega]].$$
> The first term is $-[d\omega,\omega]$. The last term vanishes: the graded Jacobi identity for three degree-one copies of $\omega$ gives $-3[\omega,[\omega,\omega]]=0$ over $\mathbb R$ or $\mathbb C$. Hence the sum is zero. Pullback by a local section gives the local identity.

# Rederivation Scaffold

Expand $d(d\omega+\frac12[\omega,omega])+[\omega,d\omega+\frac12[\omega,omega]]$. The derivative terms cancel by graded antisymmetry; the cubic term is Jacobi.
