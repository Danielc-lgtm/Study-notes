---
type: definition
subject: gauge-theory
prereqs: ["Def - Principal Symbol and Elliptic Differential Operator"]
tags: [gauge-theory, elliptic-complex, deformation-complex]
---

# Prerequisite Concepts

- [[Def - Principal Symbol and Elliptic Differential Operator]]

# The Definition

> [!definition] Elliptic complex
> A differential complex
> $$0\to\Gamma(E_0)\xrightarrow{L_0}\Gamma(E_1)\xrightarrow{L_1}\cdots\xrightarrow{L_{r-1}}\Gamma(E_r)\to0$$
> is elliptic when, for every nonzero $\xi\in T_x^*M$, its symbol sequence is exact. Its degree-$j$ Laplacian is
> $$\Delta_j=L_j^*L_j+L_{j-1}L_{j-1}^*.$$

The complex condition gives $L_jL_{j-1}=0$, hence cohomology $H^j=\ker L_j/\operatorname{im}L_{j-1}$. Symbol exactness implies $\Delta_j$ is elliptic: if $v$ lies in the kernel of its symbol, positivity gives both $\sigma(L_j)v=0$ and $\sigma(L_{j-1})^*v=0$; exactness puts $v$ in the image of $\sigma(L_{j-1})$, orthogonal to that same image, so $v=0$.

# Gauge Interpretation

At degree one, $L_0$ is the infinitesimal gauge action and $L_1$ the linearized equation. The condition $L_0^*a=0$ is a gauge slice. Ellipticity says the equation plus gauge fixing controls all derivatives transverse to gauge.

**True name:** an elliptic complex is a gauge-degenerate operator whose degeneracy becomes invertible after taking the quotient direction and its adjoint together.

