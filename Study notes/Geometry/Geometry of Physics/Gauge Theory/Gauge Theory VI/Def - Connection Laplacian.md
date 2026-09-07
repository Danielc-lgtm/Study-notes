---
type: definition
subject: gauge-theory
prereqs: ["Def - Connection on a Vector Bundle"]
tags: [gauge-theory, connection-laplacian]
---

# Prerequisite Concepts

- [[Def - Connection on a Vector Bundle]]

# The Definition

> [!definition] Connection Laplacian
> For a metric connection $\nabla$ on $E\to M$, the connection Laplacian is
> $$\nabla^*\nabla:\Gamma(E)\to\Gamma(E).$$
> In a local orthonormal frame,
> $$\nabla^*\nabla s=-\sum_j\left(\nabla_{e_j}\nabla_{e_j}s-\nabla_{\nabla^{LC}_{e_j}e_j}s\right).$$

The correction term makes the formula tensorial away from a normal frame. On a closed manifold,
$$\langle\nabla^*\nabla s,s\rangle_{L^2}=\|\nabla s\|_{L^2}^2,$$
by the definition of the formal adjoint. Hence the operator is nonnegative and its kernel consists exactly of parallel sections.

# Calibration

On a trivial Euclidean bundle over flat space with the product connection, it is the componentwise positive Laplacian $-\sum_j\partial_j^2$. It is not the Hodge Laplacian on bundle-valued forms; a curvature correction relates the two.

