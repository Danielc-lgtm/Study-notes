---
type: definition
subject: gauge-theory
prereqs: ["Def - Sobolev Space of Bundle Sections", "Def - Gauge Action and Seiberg-Witten Moduli Space"]
tags: [gauge-theory, seiberg-witten, sobolev]
---

# Prerequisite Concepts

- [[Def - Sobolev Space of Bundle Sections]]
- [[Def - Gauge Action and Seiberg-Witten Moduli Space]]

# The Definition

> [!definition] Sobolev completion
> Fix a smooth reference connection $A_0$. For $kp>4$, set
> $$\mathcal C_{k+1,p}=W^{k+1,p}(S^+)\times(A_0+W^{k+1,p}(iT^*M)),$$
> $$\mathcal G_{k+2,p}=W^{k+2,p}(M,U(1)).$$
> Then $\mathcal G_{k+2,p}$ is a Banach Lie group acting smoothly on $\mathcal C_{k+1,p}$, and
> $$\operatorname{SW}:\mathcal C_{k+1,p}\to W^{k,p}(S^-)\oplus W^{k,p}(i\Lambda^2_+)$$

is smooth.

The derivative loss matches the first-order Dirac and curvature terms. The extra gauge derivative is needed because the action contains $g^{-1}dg$. The condition $kp>4$ supplies continuous representatives and the multiplication estimates for $a\psi$ and $q(\psi)$.

