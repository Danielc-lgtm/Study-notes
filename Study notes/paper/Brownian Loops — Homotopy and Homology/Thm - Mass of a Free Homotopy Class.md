---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
  - "Def - Dirichlet Form Loop Measure"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 3.2"
---

# Statement

> **Theorem (mass of a free homotopy class; Belyaev–Huseynli 3.2).** Let $X=\Gamma\backslash\mathbb{H}^2$ be a geometrically finite hyperbolic surface, $\gamma\in\mathcal P_X$ a primitive closed geodesic with hyperbolic representative $\tau:z\mapsto e^{\ell_\gamma}z$, and $m\ge1$. For a $\Gamma$-invariant [[Def - Dirichlet Form and its Operator and Semigroup|Dirichlet form]] with kernel $p^E_{\mathbb{H}^2}$, the loop-measure mass of the free homotopy class $C_X(\gamma^m)$ is
> $$\mu^E_X\big(C_X(\gamma^m)\big)=\int_0^\infty\frac{dt}{t}\int_{\mathcal F_\tau}p^E_{\mathbb{H}^2}\big(t,z,\tau^m z\big)\,d\rho_{\mathbb{H}^2}(z),$$
> where $\mathcal F_\tau=\{1\le\operatorname{Im}z<e^{\ell_\gamma}\}$ is the fundamental strip for $\langle\tau\rangle$.

**In one line.** The class-mass collapses the group-sum heat kernel to a *single* term $p^E_{\mathbb{H}^2}(t,z,\tau^m z)$ integrated over one geodesic period — the identity that makes each topological type's mass finite and computable. Proof: isolate the conjugacy class, unfold over cosets $\Gamma/\langle\tau\rangle$, reassemble onto the strip.

**Full treatment and gap-free proof:** [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]].
