---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Weighted Potential Measure"
tags: [paper, brownian-loops]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 3.6"
---

# Statement

> **Definition (loop-length integral; Belyaev–Huseynli 3.6).** For a Bernstein $\phi$ with [[Def - Weighted Potential Measure|weighted potential measure]] $V_\phi$ and $L>0$,
> $$I_\phi(L):=\int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds),$$
> so that the mass of a free homotopy class ([[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]]) is $\mu^\phi_X(C_X(\gamma^m))=\dfrac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)$ with $L=m\ell_\gamma$.

**In one line.** The purely one-dimensional integral (over the subordination variable) that carries all the $\phi$-dependence of a class-mass; the geometry enters only through $L=m\ell_\gamma$. Evaluates to $\frac{e^{-L/2}}{L}$ (Brownian), $\frac{e^{-L\sqrt{1/4+\kappa}}}{L}$ (killing), $\frac{\alpha}{2}\frac{e^{-L/2}}{L}$ (α-stable). §4 studies its behaviour to sum the masses into a Selberg zeta function.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.1]].
