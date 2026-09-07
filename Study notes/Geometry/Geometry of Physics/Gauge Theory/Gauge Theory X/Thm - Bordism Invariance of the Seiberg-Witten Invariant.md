---
type: theorem
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Invariant", "Thm - Sard-Smale and Parametric Transversality"]
tags: [gauge-theory, seiberg-witten, bordism]
---

# Prerequisite Concepts

- [[Def - Seiberg-Witten Invariant]]
- [[Thm - Sard-Smale and Parametric Transversality]]

# Statement

> [!theorem] Perturbation independence
> If $b_2^+(X)\ge2$, the integer $\operatorname{SW}_X(\mathfrak s)$ is independent of the generic metric and perturbation used to define it.

# Why this should be true

A generic path of auxiliary data produces a compact oriented bordism between the endpoint moduli spaces. Characteristic numbers do not change across an oriented bordism when the cohomology class extends over it.

> [!proof]- Formal Proof
> Join the two regular choices by a smooth path. Parametric transversality permits an arbitrarily small generic adjustment for which the universal moduli space $\mathcal W$ is smooth of dimension $d+1$. The reducible locus has codimension $b_2^+$ in the perturbation space. Because $b_2^+\ge2$, a generic one-dimensional path avoids it. The parameterized a priori estimates are uniform on the compact parameter interval, so $\mathcal W$ is compact modulo gauge. Its boundary, with the outward-normal-first convention, is
> $$\partial\mathcal W=\mathcal M_1\sqcup(-\mathcal M_0).$$
> The based-gauge construction over $\mathcal W$ gives a principal circle bundle whose Chern class $\widetilde\mu$ restricts to the endpoint classes $\mu_i$. If $d=2k$, the cap product $\widetilde\mu^k\frown[\mathcal W,\partial\mathcal W]$ is a relative one-cycle. The algebraic boundary of a relative cycle is zero, hence
> $$0=\langle\mu_1^k,[\mathcal M_1]\rangle-\langle\mu_0^k,[\mathcal M_0]\rangle.$$
> If $d<0$ or $d$ is odd, both invariants are zero by definition. Thus the invariant is independent of the choices.

# Boundary of the argument

For $b_2^+=1$, a generic path can cross the codimension-one reducible wall. The resulting jump is wall crossing, not a contradiction to the proof: its avoidance step has failed.
