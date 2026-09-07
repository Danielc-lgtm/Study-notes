---
type: definition
subject: gauge-theory
prereqs: ["Thm - Chern-Weil Theorem"]
tags: [gauge-theory, chern-simons, transgression]
---

# Prerequisite Concepts

- [[Thm - Chern-Weil Theorem]]

# The Definition

> [!definition] Transgression
> For an invariant degree-$k$ polynomial $f$ and connections $A_0,A_1$, put $a=A_1-A_0$, $A_t=A_0+ta$, and
> $$T_f(A_1,A_0)=k\int_0^1f(a,F_{A_t}^{k-1})dt.$$
> Then
> $$dT_f(A_1,A_0)=f(F_{A_1}^k)-f(F_{A_0}^k).$$

This is not an extra theorem hidden in the definition: the identity is exactly the connection-independence calculation in [[Thm - Chern-Weil Theorem#Formal Proof]]. The form has degree $2k-1$.

# The Three-Dimensional Formula

For $f(X,Y)=\frac1{8\pi^2}\operatorname{tr}(XY)$, choose the zero connection in a trivialization. Since $F_{tA}=t,dA+t^2A\wedge A$,
$$T_f(A,0)=\frac1{8\pi^2}\operatorname{tr}\left(A\wedge dA+\frac23A\wedge A\wedge A\right),$$
and its derivative is $\frac1{8\pi^2}\operatorname{tr}(F_A\wedge F_A)$.

# Dependence

Unlike the characteristic form, a transgression form depends on the endpoints and on a trivialization when one endpoint is written as zero. Its exterior derivative is intrinsic. Under a large gauge transformation, its integral on a closed three-manifold can change by an integer, which is why the exponentiated Chern–Simons action is well defined.

**True name:** transgression is the boundary primitive of the difference between two characteristic forms.
