---
type: definition
subject: probability-geometry
prereqs:
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Section 6.1"
---

# Statement

> **Definition (probability measure on homotopy classes; Belyaev–Huseynli §6.1).** For $\kappa>0$, $s=\frac12+\sqrt{\frac14+\kappa}$,
> $$\mathbb P_s\big(C_X(\gamma^m)\big):=\frac{\mu^\kappa_X(C_X(\gamma^m))}{-\log Z_X(s)}.$$

**In one line.** The killed loop mass normalised by its finite total $-\log Z_X(s)$ ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Cor 4.3]]) — an honest probability distribution over free homotopy classes. The geodesic length $L=m\ell_\gamma$ is its natural random variable: $\mathbb E_s[e^{-rL}]=\log Z_X(s+r)/\log Z_X(s)$ gives all moments as derivatives of $-\log Z_X$, and as $s\to\infty$ the measure concentrates on the systolic classes with $\mathbb E_s[L]\to\ell_{\mathrm{sys}}$.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.1]].
