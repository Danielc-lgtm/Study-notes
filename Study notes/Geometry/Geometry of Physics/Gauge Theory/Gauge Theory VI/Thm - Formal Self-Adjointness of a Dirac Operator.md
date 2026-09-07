---
type: theorem
subject: gauge-theory
prereqs: ["Def - Dirac Bundle and Dirac Operator"]
tags: [gauge-theory, dirac-operator, formal-adjoint]
---

# Prerequisite Concepts

- [[Def - Dirac Bundle and Dirac Operator]]

# Statement

> [!theorem] Formal self-adjointness
> On a closed Riemannian manifold, a Dirac operator associated to a metric Clifford connection satisfies
> $$\int_M\langle Ds,t\rangle\,dV=\int_M\langle s,Dt\rangle\,dV.$$

# Formal Proof

> [!proof]- Formal Proof
> Clifford multiplication by a real one-form is skew-adjoint. In a local orthonormal frame normal at a chosen point,
> $$\operatorname{div}\bigl(\langle s,c(e^j)t\rangle e_j\bigr)
> =\langle\nabla_{e_j}s,c(e^j)t\rangle+\langle s,c(e^j)\nabla_{e_j}t\rangle.$$
> Skew-adjointness changes the first term to $-\langle c(e^j)\nabla_{e_j}s,t\rangle=-\langle Ds,t\rangle$. Therefore the divergence equals $-\langle Ds,t\rangle+\langle s,Dt\rangle$. Integrating and applying the divergence theorem on a closed manifold proves the identity.

# Boundary Warning

With boundary, the omitted term is the boundary pairing involving Clifford multiplication by the outward conormal. Self-adjointness then requires a boundary condition; it is not automatic.

