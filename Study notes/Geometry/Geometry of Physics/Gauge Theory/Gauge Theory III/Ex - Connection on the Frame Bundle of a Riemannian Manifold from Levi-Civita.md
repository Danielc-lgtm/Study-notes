---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Levi-Civita Connection"
  - "Def - Orthonormal Frame Bundle"
tags: [geometry, gauge-theory, riemannian-geometry, principal-bundles]
---

# Prerequisite Concepts

- [[Def - Connection 1-Form on a Principal Bundle]]
- [[Def - Levi-Civita Connection]]
- [[Def - Orthonormal Frame Bundle]]

# Problem Statement

Let $F^O(M)$ be the orthonormal frame bundle of a Riemannian $n$-manifold. Construct from its Levi–Civita connection a principal $O(n)$-connection and identify its local connection form.

# Solution

> [!solution]- Solution
> A point $u\in F^O(M)_x$ is an isometry $u:\mathbb R^n\to T_xM$. For
> $X\in T_uF^O(M)$ choose a curve $u(t)$ with $u(0)=u$, $\dot u(0)=X$, and
> base curve $x(t)=\pi(u(t))$. Define
> $$\omega_u(X)=u^{-1}\bigl(\nabla_{\dot x(0)}u(t)\bigr),$$
> where the derivative is applied columnwise. This is independent of the
> representing curve because covariant differentiation along a curve depends
> only on its first jet at the chosen time.
>
> Metric compatibility implies $\omega_u(X)\in\mathfrak o(n)$: differentiating
> $\langle u(t)v,u(t)w\rangle=\langle v,w\rangle$ gives
> $\langle\omega_u(X)v,w\rangle+\langle v,\omega_u(X)w\rangle=0$.
> For the vertical curve $u(t)=u e^{t\xi}$, one obtains
> $\omega_u(\xi_P)=\xi$. For constant $g\in O(n)$,
> $$\omega_{ug}((R_g)_*X)=(ug)^{-1}\nabla_X(ug)
> =g^{-1}\omega_u(X)g,$$
> proving the required equivariance. Thus $\omega$ is a principal connection;
> its horizontal curves are exactly parallel orthonormal frames.
>
> If $s=(e_1,\ldots,e_n)$ is a local orthonormal frame and
> $A=s^*\omega$, then
> $$A^a{}_b(X)=\langle e_a,\nabla_Xe_b\rangle,
> \qquad \nabla_Xe_b=e_aA^a{}_b(X).$$
> These are Cartan's skew-symmetric connection one-forms. Conversely they
> reconstruct $\omega$ in every frame, proving uniqueness.

# Rederivation Scaffold

Differentiate a moving frame covariantly and express the result in that same frame.
