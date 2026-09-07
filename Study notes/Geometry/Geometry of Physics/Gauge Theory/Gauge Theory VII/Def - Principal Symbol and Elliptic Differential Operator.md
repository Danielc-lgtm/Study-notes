---
type: definition
subject: gauge-theory
prereqs: ["Def - Sobolev Space of Bundle Sections"]
tags: [gauge-theory, elliptic-operator, principal-symbol]
---

# Prerequisite Concepts

- [[Def - Sobolev Space of Bundle Sections]]

# Motivation

Lower-order terms affect solutions but not the high-frequency obstruction to inversion. The principal symbol retains exactly the top derivative terms and tests whether every nonzero cotangent direction can be inverted.

# The Definition

> [!definition] Principal symbol and ellipticity
> If $L:\Gamma(E)\to\Gamma(F)$ has order $\ell$, locally
> $$L=\sum_{|\alpha|\le\ell}A_\alpha(x)\partial^\alpha.$$
> Its principal symbol is
> $$\sigma_L(x,\xi)=\sum_{|\alpha|=\ell}A_\alpha(x)\xi^\alpha:\ E_x\to F_x.$$
> The operator is elliptic when this map is invertible for every $\xi\ne0$.

Coordinate-change terms involving derivatives of the transition functions have lower order, so the top expression transforms as a bundle map on $\pi^*E\to\pi^*F$ over $T^*M$. Thus the definition is intrinsic.

# Examples

The positive Laplacian has symbol $|\xi|^2$. A Dirac operator has symbol $c(\xi)$ and inverse $-c(\xi)/|\xi|^2$. The exterior derivative alone is not elliptic because wedge multiplication by $\xi$ has a kernel; the full de Rham complex is elliptic because its symbol sequence is exact.

**True name:** ellipticity is invertibility after discarding space and retaining only a nonzero frequency direction.

