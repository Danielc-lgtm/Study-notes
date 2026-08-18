---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 4.6"
---

# Statement

> **Corollary (twisted Ruelle zeta identity; Belyaev–Huseynli 4.6).** With $\kappa_\pm(s)=s(s\pm1)$, for $\operatorname{Re}s>\max(c_\rho,\frac12)$ and a finite-dimensional representation $\rho:\Gamma\to\mathrm{GL}(V_\rho)$,
> $$-\log R_X(s,\rho)=\sum_{\gamma}\sum_{m\ge1}\operatorname{tr}\rho(\tau^m)\big[\mu^{\kappa_-(s)}_X(C_X(\gamma^m))-\mu^{\kappa_+(s)}_X(C_X(\gamma^m))\big]=\sum_\gamma\sum_{m\ge1}\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.$$

**In one line.** The [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|twisted Ruelle zeta]] is $-\exp$ of a *representation-weighted* difference of killed loop masses; the difference between killing rates $\kappa_-$ and $\kappa_+$ telescopes each class to $e^{-sm\ell_\gamma}/m$. Setting $\rho$ a unitary character specialises this to the homology decomposition of §6. Proof: expand $-\log\det(I-M)=\sum\operatorname{tr}(M^m)/m$ and factor $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$.

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1.2]].
