---
type: theorem
subject: gauge-theory
prereqs: ["Def - Sobolev Seiberg-Witten Configuration Space", "Thm - Weitzenbock Formula for a Dirac Bundle"]
tags: [gauge-theory, seiberg-witten, compactness]
---

# Statement

> [!theorem] Seiberg–Witten compactness
> On a closed oriented Riemannian four-manifold, the moduli space of solutions to a fixed Seiberg–Witten perturbation is compact. Every Sobolev solution is gauge-equivalent to a smooth solution, and compactness holds in the smooth topology modulo gauge.

# Proof Architecture

> [!proof]- Formal Proof
> Apply the spin-c Weitzenböck formula to $D_A^+\psi=0$ and substitute $F_A^+=q(\psi)+\eta$. At a maximum of $|\psi|^2$, the scalar Laplacian inequality and $\langle q(\psi)\psi,\psi\rangle=\frac12|\psi|^4$ bound $\|\psi\|_{L^\infty}$ by the negative part of scalar curvature and $\|\eta\|_\infty$.
>
> The curvature equation then bounds $F_A^+$ in $L^p$. The identity
> $$\int_MF_A\wedge F_A=\|F_A^+\|_2^2-\|F_A^-\|_2^2$$
> is fixed by $c_1(L)^2$, so it bounds the full $L^2$ curvature. Abelian Coulomb gauge writes $A=A_0+a$ with $d^*a=0$ and bounded harmonic component; the elliptic estimate for $d^+\oplus d^*$ bounds $a$.
>
> The Dirac and curvature equations, Sobolev multiplication, and elliptic estimates bootstrap uniform $W^{m,2}$ bounds for every $m$. Rellich gives a convergent subsequence at each stage; a diagonal argument gives smooth convergence modulo gauge. The same bootstrap applied to a weak solution proves smoothness.

# Why Abelian Matters

No curvature concentration or bubbling term occurs: Coulomb control is linear and the spinor maximum principle bounds the nonlinear source. This is the analytic simplification behind Seiberg–Witten compactness.

