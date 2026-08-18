---
type: definition
subject: geometry
prereqs:
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
tags: [paper, hyperbolic-geometry, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 3.10"
---

# Statement

> **Definition (marked length spectrum; Belyaev–Huseynli 3.10).** The **marked length spectrum** of $(X,g)$ is the function on non-trivial free homotopy classes of closed curves
> $$\mathrm{MLS}:C_X(\gamma^m)\longmapsto\inf_{\eta\in C_X(\gamma^m)}\ell_g(\eta),$$
> the shortest length in each class. On a hyperbolic surface the infimum is attained by the unique closed [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length|geodesic]], so $\mathrm{MLS}(C_X(\gamma^m))=m\ell_\gamma$.

**In one line.** The lengths of closed geodesics *together with which class realises each* — the "marking." Unmarked lengths do not determine the surface (isospectral non-isometric examples exist, Vignéras), but the marked spectrum does in 2D (Otal, Croke), which is why the loop masses (which recover the MLS, [[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]]) pin down the surface.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.4]].
