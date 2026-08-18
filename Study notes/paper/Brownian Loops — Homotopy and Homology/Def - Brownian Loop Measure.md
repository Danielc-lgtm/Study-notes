---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Disintegration and the Bridge Measure"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [paper, brownian-loops]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.1"
---

# Statement

> **Definition (Brownian loop measure; Belyaev–Huseynli Def. 2.1).** On a complete orientable [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure|Riemannian surface]] $(X,g)$, the **rooted Brownian loop measure** is the infinite but [[Def - σ-Finite Measure|σ-finite]] measure on the space $C^*_X$ of parametrised oriented rooted loops
> $$\mu^*_X := \int_0^\infty \frac{dt}{t}\int_X \mathbb{W}^t_{x\to x}\,d\operatorname{vol}_g(x),$$
> where $\mathbb{W}^t_{x\to x}$ is the [[Def - Disintegration and the Bridge Measure|Brownian bridge]] from $x$ back to $x$ in time $t$ (total mass $p(t,x,x)$) and $\frac{dt}{t}$ is the scale-invariant weight on durations. The **Brownian loop measure** $\mu_X$ is its pushforward to the quotient $C_X$ of unrooted, unparametrised, oriented loops.

**In one line.** A duration-blind, scale-invariant way to weigh *every* Brownian loop on the surface; total mass is infinite (a small-$t$ effect), but each topological type of loop carries finite mass. It satisfies **restriction** ($\mu_{X'}=\mu_X$ restricted to loops inside $X'$) and, for 2-D Brownian motion, **conformal invariance** (depends only on the conformal class $[g]$).

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.1]] — motivation, the divergence computation, and the two fundamental properties.
