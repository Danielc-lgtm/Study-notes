---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Connection on a Vector Bundle"
tags: [geometry, gauge-theory, curvature, Bianchi]
---

# Prerequisite Concepts

- [[Def - Curvature of a Vector-Bundle Connection]]
- [[Def - Connection on a Vector Bundle]]

# Notation

Let $\nabla$ be a connection on $E\to M$. In a local frame let $A\in\Omega^1(U;\mathfrak{gl}_r)$ and $F_A=dA+A\wedge A$. For matrix-valued forms define
$$
[\alpha,\beta]=\alpha\wedge\beta-(-1)^{pq}\beta\wedge\alpha,\qquad
\deg\alpha=p, \deg\beta=q,
$$
and $d_A\beta=d\beta+[A,\beta]$.

# Statement

> [!theorem] Second Bianchi identity
> The curvature satisfies
> $$d_\nabla F_\nabla=0.$$
> In a local frame this is
> $$d_AF_A=dF_A+A\wedge F_A-F_A\wedge A=0.$$
> Equivalently, for vector fields $X,Y,Z$,
> $$
> \sum_{\mathrm{cyc}}\left((\nabla_XF_\nabla)(Y,Z)-F_\nabla([X,Y],Z)\right)=0,
> $$
> where $\nabla$ on $F_\nabla$ is the induced connection on $\operatorname{End}E$.

# Why Is It True

The identity is the compatibility condition forced by the definition $F_A=dA+A^2$: the $dA$ terms cancel by the graded Leibniz rule, and the cubic terms cancel by associativity. Conceptually, it is the graded Jacobi identity for $d_\nabla$ together with $d_\nabla^2=F_\nabla\wedge(-)$.

# Formal Proof

> [!proof]- Formal Proof
> Work in a local frame. Since $d^2=0$ and $d(A\wedge A)=dA\wedge A-A\wedge dA$,
> $$
> dF_A=dA\wedge A-A\wedge dA.
> $$
> Because $\deg F_A=2$,
> $$
> [A,F_A]=A\wedge(dA+A\wedge A)-(dA+A\wedge A)\wedge A.
> $$
> Expanding and using associativity gives
> $$
> [A,F_A]=A\wedge dA-dA\wedge A
> +(A\wedge A)\wedge A-A\wedge(A\wedge A)
> =A\wedge dA-dA\wedge A.
> $$
> Therefore $d_AF_A=dF_A+[A,F_A]=0$.
>
> Under a frame change $F_A$ transforms by conjugation and $d_AF_A$ also transforms by conjugation, so the local identity is global. Evaluating the exterior covariant derivative of an $\operatorname{End}E$-valued $2$-form on $(X,Y,Z)$ yields the displayed cyclic formula; this is the standard alternating-sum definition of $d_\nabla$.

# Rederivation Scaffold

Remember only $F=dA+A^2$ and the graded rule $d(A^2)=dA\,A-A\,dA$. Then $dF+[A,F]$ cancels term by term.

# Unlocked by This

For a Hermitian line bundle the commutators vanish, so Bianchi reduces to $dF=0$, the homogeneous Maxwell equation. For principal connections it becomes $d_AF_A=0$ in the adjoint bundle.
