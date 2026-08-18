---
type: theorem
subject: probability-geometry
prereqs:
  - "Thm - Mass of a Free Homotopy Class"
  - "Def - The Loop-Length Integral"
  - "Lemma - Collapsing the Time Integral of the Subordinate Kernel"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 3.5"
---

# Statement

> **Theorem (mass of a subordinate loop class; Belyaev–Huseynli 3.5).** For a Bernstein function $\phi$ (Assumption 2.3), $\gamma\in\mathcal P_X$, and $m\ge1$ (with $L=m\ell_\gamma$),
> $$\mu^\phi_X\big(C_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)=\frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L),$$
> where $V_\phi$ is the [[Def - Weighted Potential Measure|weighted potential measure]] and $I_\phi$ the [[Def - The Loop-Length Integral|loop-length integral]].

**In one line.** [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] specialised to a [[Def - Subordinate Brownian Loop Measure|subordinate]] process, with the duration-integral collapsed by [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] and the strip-integral evaluated by the Wang–Xue identity — reducing every class-mass to a single 1-D integral in $L$. Closed forms: $\frac1m\frac{1}{e^L-1}$ (Brownian), $\frac1m\frac{e^{(\frac12-\sqrt{1/4+\kappa})L}}{e^L-1}$ (killing), $\frac\alpha2$× Brownian (α-stable).

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.1]].
