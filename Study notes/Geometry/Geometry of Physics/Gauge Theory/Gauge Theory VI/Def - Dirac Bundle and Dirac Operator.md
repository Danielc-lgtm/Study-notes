---
type: definition
subject: gauge-theory
prereqs: ["Def - Clifford Algebra and Clifford Module", "Def - Connection on a Vector Bundle"]
tags: [gauge-theory, dirac-operator, clifford-module]
---

# Prerequisite Concepts

- [[Def - Clifford Algebra and Clifford Module]]
- [[Def - Connection on a Vector Bundle]]

# Axiom Motivation

Pointwise Clifford multiplication alone cannot be differentiated coherently. A Dirac bundle requires a metric connection compatible with Clifford multiplication, so differentiating $c(\alpha)s$ differentiates both the cotangent factor and the section. This compatibility is what makes the square of the resulting first-order operator Laplace type.

# The Definition

> [!definition] Dirac bundle and operator
> A Dirac bundle over an oriented Riemannian manifold is a metric vector bundle $E$ with Clifford multiplication $c:T^*M\to\operatorname{End}(E)$ and a metric connection $\nabla$ satisfying
> $$\nabla_X(c(\alpha)s)=c(\nabla_X^{LC}\alpha)s+c(\alpha)\nabla_Xs.$$
> Its Dirac operator is
> $$D=c\circ\nabla,\qquad Ds=\sum_{j=1}^n c(e^j)\nabla_{e_j}s$$
> in any local orthonormal frame.

Frame independence follows because both factors transform orthogonally and the index is contracted. Its principal symbol is $\sigma_D(x,\xi)=c(\xi)$, which is invertible for $\xi\ne0$ since $c(\xi)^2=-|\xi|^2$; hence $D$ is elliptic.

# Examples

On $E=\Lambda^*T^*M$ with $c(\alpha)=\alpha\wedge-\iota_{\alpha^\sharp}$, the Dirac operator is $d+d^*$. Spin and $\operatorname{Spin}^c$ structures produce smaller irreducible Clifford modules. An arbitrary connection on a Clifford module is a non-example if it fails the compatibility identity.

**True name:** a Dirac operator is the metric square root of a connection Laplacian, corrected by curvature.

