---
type: definition
subject: probability
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.9"
---

# Statement

> **Definition (weighted potential measure; Belyaev–Huseynli Def. 2.9).** For a [[Def - Bernstein Function, Subordinator, and Subordination|Bernstein function]] $\phi$ with subordinator law $\psi^\phi_t$, the **weighted potential measure** $V_\phi$ is the σ-finite measure on $(0,\infty)$ characterised by
> $$\int_{(0,\infty)}h(s)\,V_\phi(ds) = \int_0^\infty\frac{dt}{t}\int_{(0,\infty)}h(s)\,\psi^\phi_t(ds)$$
> for every non-negative measurable $h$ making the right side finite. When absolutely continuous, $V_\phi(ds)=V_\phi(s)\,ds$ (as for all Bernstein functions used in the paper).

**In one line.** The result of collapsing the loop measure's duration-integral $\int_0^\infty\frac{dt}{t}$ against the subordinator law into a single measure on the subordination variable $s$; it is what turns every loop-mass double integral into a single heat-kernel integral (via [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]). Worked values: $\frac{ds}{s}$ (Brownian), $e^{-\kappa s}\frac{ds}{s}$ (killing), $\frac{\alpha}{2}\frac{ds}{s}$ ($\alpha$-stable).

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4.1]] — Example 2.10 computes all three cases.
