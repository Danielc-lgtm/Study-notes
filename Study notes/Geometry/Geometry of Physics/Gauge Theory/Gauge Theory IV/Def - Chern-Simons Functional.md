---
type: definition
subject: gauge-theory
prereqs: ["Def - Chern-Simons Transgression Form", "Def - Gauge Group of a Principal Bundle"]
tags: [gauge-theory, chern-simons, flat-connection]
---

# The Definition

> [!definition] Chern–Simons functional
> On a closed oriented three-manifold $Y$ with a trivialized $SU(2)$-bundle, set
> $$\operatorname{CS}(A)=\frac1{8\pi^2}\int_Y\operatorname{tr}\left(A\wedge dA+\frac23A\wedge A\wedge A\right)\in\mathbb R/\mathbb Z.$$

The target is $\mathbb R/\mathbb Z$, not canonically $\mathbb R$: changing the extension or applying a gauge transformation of nonzero degree changes a lift by an integer.

# Four-Dimensional Interpretation

If $(Y,P,A)$ extends over an oriented four-manifold $(X,\widetilde P,\widetilde A)$, Stokes' theorem gives
$$\operatorname{CS}(A)=\frac1{8\pi^2}\int_X\operatorname{tr}(F_{\widetilde A}\wedge F_{\widetilde A})\pmod{\mathbb Z}.$$
Two extensions glue to a closed four-manifold, and the difference is the integral second Chern number, proving extension independence modulo integers.

# First Variation and Critical Points

For $A_t=A+ta$ on closed $Y$, differentiate the transgression formula and integrate by parts:
$$\left.\frac d{dt}\right|_0\operatorname{CS}(A_t)=\frac1{4\pi^2}\int_Y\operatorname{tr}(a\wedge F_A).$$
Because $a$ is arbitrary, the critical-point equation is $F_A=0$. Thus Chern–Simons theory packages the flat-connection moduli space as the critical locus of a gauge-invariant circle-valued functional.

# Gauge Change

For $g:Y\to SU(2)$,
$$\operatorname{CS}(A^g)-\operatorname{CS}(A)=\frac1{24\pi^2}\int_Y\operatorname{tr}(g^{-1}dg)^3\in\mathbb Z$$
up to the orientation/sign convention. Hence $e^{2\pi i\operatorname{CS}(A)}$ is gauge invariant.
