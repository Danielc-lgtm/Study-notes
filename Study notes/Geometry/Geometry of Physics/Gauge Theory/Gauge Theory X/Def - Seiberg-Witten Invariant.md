---
type: definition
subject: gauge-theory
prereqs: ["Def - Framed Seiberg-Witten Moduli Space and Mu Class", "Thm - Reducibles and Orientation of Seiberg-Witten Moduli"]
tags: [gauge-theory, seiberg-witten, invariant]
---

# The Definition

Let $X$ be a closed oriented four-manifold with $b_2^+(X)\ge2$, equipped with a homology orientation, and let $\mathfrak s$ be a spin-c structure. For a generic perturbation, write
$$d(\mathfrak s)=\frac14\bigl(c_1(L)^2-2\chi(X)-3\sigma(X)\bigr)$$
for the dimension of the compact oriented moduli space $\mathcal M_\eta(\mathfrak s)$.

> [!definition] Seiberg–Witten invariant
> If $d(\mathfrak s)=2k\ge0$, define
> $$\operatorname{SW}_X(\mathfrak s)=\left\langle\mu^k,[\mathcal M_\eta(\mathfrak s)]\right\rangle\in\mathbb Z.$$
> Set $\operatorname{SW}_X(\mathfrak s)=0$ when $d(\mathfrak s)$ is negative or odd.

For $d=0$, this is the signed count of points. The exponent $k=d/2$ is forced: $\mu$ has degree two, so only $\mu^k$ pairs with the $d$-dimensional fundamental class.

# Dependence data

The integer depends on the orientation of $X$, its homology orientation, and $\mathfrak s$. Reversing the moduli-space orientation reverses the sign. The hypothesis $b_2^+\ge2$ prevents a generic one-parameter comparison from meeting the reducible wall; when $b_2^+=1$, chamber data are required.
