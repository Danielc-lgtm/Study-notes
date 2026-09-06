---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Fundamental Vector Field of a Principal Bundle"
  - "Def - Lie-Algebra-Valued Differential Form"
tags: [gauge-theory, principal-connection, connection-form]
---

# The Definition

> [!definition] Principal connection form
> A **principal connection** on a right principal $G$-bundle $P\to M$ is a form $\omega\in\Omega^1(P;\mathfrak g)$ such that
> $$
> \omega_p(\xi_P(p))=\xi,qquad
> R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega.
> $$

The first axiom says that $\omega$ reads the infinitesimal group generator of a vertical vector. The second says that changing the point in the torsor changes this generator by the adjoint representation.

# Horizontal Projection

The horizontal space is $H_p=\ker\omega_p$. Every $X\in T_pP$ decomposes uniquely as
$$X=X^H+(\omega_pX)_P(p).$$
Consequently the vertical projection is $X\mapsto(\omega X)_P$ and the horizontal projection is $X\mapsto X-(\omega X)_P$.

# Trivial Bundle

On $P=M\times G$ let $\theta=g^{-1}dg$ be the left Maurer–Cartan form. Every principal connection is uniquely
$$
\omega_{(x,g)}=\operatorname{Ad}_{g^{-1}}A_x+\theta_g
$$
for some $A\in\Omega^1(M;\mathfrak g)$. Pullback by the canonical section $s(x)=(x,e)$ gives $s^*\omega=A$. The connection is the product flat connection exactly when $A=0$.

# Affine Structure

If $\omega'$ and $\omega$ are connections, their difference is horizontal and $\operatorname{Ad}$-equivariant, so it descends to an element of $\Omega^1(M;\operatorname{Ad}P)$. Conversely every such form added upstairs produces another connection. Therefore the space of principal connections is affine over $\Omega^1(M;\operatorname{Ad}P)$.
