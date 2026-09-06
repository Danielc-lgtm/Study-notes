---
type: definition
subject: gauge-theory
prereqs: ["Def - Representation of a Lie Group"]
tags: [gauge-theory, clifford-algebra, spin-geometry]
---

# Motivation

A Dirac operator should square to a Laplace-type operator. If its principal symbol is multiplication by a cotangent vector $\xi$, this demands $c(\xi)^2=-|\xi|^2$. The Clifford algebra is the universal associative algebra imposing exactly this quadratic relation.

# The Definition

> [!definition] Clifford algebra and module
> For a Euclidean vector space $(V,\langle\ ,\ \rangle)$,
> $$\operatorname{Cl}(V)=T(V)/\langle v\otimes v+|v|^2 1:v\in V\rangle.$$
> A Clifford module is a vector space $S$ with an action $c:\operatorname{Cl}(V)\to\operatorname{End}(S)$; equivalently $c(v)^2=-|v|^2\operatorname{id}$.

Polarization gives
$$c(v)c(w)+c(w)c(v)=-2\langle v,w\rangle.$$
Thus orthogonal unit vectors anticommute and square to $-1$.

# Canonical Example

On $\Lambda^*V^*$ define $c(v)=\iota_v-v^\flat\wedge$. Since
$\iota_v(v^\flat\wedge\alpha)+v^\flat\wedge\iota_v\alpha=|v|^2\alpha$, one obtains $c(v)^2=-|v|^2$. This module later gives the de Rham Dirac operator $d+d^*$.

# Calibration

$\operatorname{Cl}(\mathbb R)\cong\mathbb C$ and $\operatorname{Cl}(\mathbb R^2)\cong\mathbb H$ under the negative-square convention. A representation by commuting self-adjoint matrices is a non-example unless $V=0$, because orthogonal Clifford generators must anticommute and be skew-adjoint.
**True name:** a Clifford module is a linearization of the metric quadratic form.

