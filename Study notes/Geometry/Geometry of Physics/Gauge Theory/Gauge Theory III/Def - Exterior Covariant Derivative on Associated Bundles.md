---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Associated Bundle"
  - "Def - Connection 1-Form on a Principal Bundle"
tags: [gauge-theory, covariant-derivative, associated-bundle]
---

# The Definition

Let $E=P\times_\rho V$ and let $\rho_*:\mathfrak g\to\mathfrak{gl}(V)$. In a gauge with potential $A$ define
$$
d_A\alpha=d\alpha+\rho_*(A)\wedge\alpha,qquad \alpha\in\Omega^k(U;V).
$$
Here
$$
(\rho_*(A)\wedge\alpha)(X_0,\ldots,X_k)
=\sum_i(-1)^i\rho_*(A(X_i))\alpha(X_0,\widehat X_i,\ldots,X_k).
$$
These local operators glue to the **exterior covariant derivative**
$$d_\nabla:\Omega^k(M;E)\to\Omega^{k+1}(M;E).$$

# Gauge Covariance

If $s'=sg$, then a section coefficient transforms as $\alpha'=\rho(g^{-1})\alpha$ and
$$d_{A'}\alpha'=\rho(g^{-1})d_A\alpha.$$
This identity follows by differentiating $\rho(g)^{-1}$:
$$d(\rho(g)^{-1})=-\rho(g)^{-1}d(\rho(g))\rho(g)^{-1},$$
and using
$$d(\rho(g))=\rho(g)\rho_*(g^{-1}dg).$$
The inhomogeneous terms cancel exactly.

# Curvature

A direct expansion gives
$$d_\nabla^2\alpha=\rho_*(F_A)\wedge\alpha.$$
For the adjoint representation, $d_A\alpha=d\alpha+[A,\alpha]$ and $d_A^2\alpha=[F_A,\alpha]$.

# Axiom Motivation

Ordinary $d$ differentiates the gauge matrix and is therefore not covariant. The connection term is the unique first-order correction whose inhomogeneous transformation cancels that derivative.
