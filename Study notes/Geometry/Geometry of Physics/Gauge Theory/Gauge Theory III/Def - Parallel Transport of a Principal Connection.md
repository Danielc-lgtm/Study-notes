---
type: definition
subject: gauge-theory
prereqs:
  - "Thm - Horizontal Lift Existence and Uniqueness"
tags: [gauge-theory, parallel-transport]
---

# Prerequisite Concepts

- [[Thm - Horizontal Lift Existence and Uniqueness]]

# The Definition

> [!definition] Principal parallel transport
> For a path $\gamma:[a,b]\to M$, define
> $$\operatorname{PT}_\gamma:P_{\gamma(a)}\to P_{\gamma(b)},\qquad
> p\mapsto\widetilde\gamma_p(b),$$
> where $\widetilde\gamma_p$ is the horizontal lift beginning at $p$.

It is $G$-equivariant: $\operatorname{PT}_\gamma(pg)=\operatorname{PT}_\gamma(p)g$. Hence it is an isomorphism of $G$-torsors.

# Legal Operations

For constant paths, transport is the identity. For orientation-preserving reparametrization it is unchanged. If path concatenation $\gamma_2*\gamma_1$ traverses $\gamma_1$ first, then
$$\operatorname{PT}_{\gamma_2*\gamma_1}=\operatorname{PT}_{\gamma_2}\circ\operatorname{PT}_{\gamma_1}.$$
For the reversed path, $\operatorname{PT}_{\bar\gamma}=\operatorname{PT}_\gamma^{-1}$. Each identity follows by concatenating, reparametrizing, or reversing horizontal lifts and invoking uniqueness.

# Local Formula

In a gauge with potential $A$, transport is the path-ordered exponential
$$U_\gamma=\mathcal P\exp\left(-\int_\gamma A\right),$$
meaning the endpoint of $\dot U=-A(\dot\gamma)U$, $U(a)=e$. Path ordering is unnecessary only when the coefficients commute.
