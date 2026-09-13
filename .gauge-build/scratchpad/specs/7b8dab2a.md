# PAGE SPEC

- **Filename:** `Def - Path-Ordered Exponential.md`
- **Type:** definition
- **Chapter:** Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections  (folder `Gauge Theory V/`)
- **Section:** §5.1 Horizontal Lifts and Parallel Transport

## Spec (from the manifest)

**[anchor]** — type: definition (compound); source items: B-D2.6.4, B-R2.6.2, B-T2.6.5, B-E2.6.2; prereqs: [Def - Parallel Transport in a Principal Bundle, Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]; spec: for continuous $A\colon[0,L]\to\operatorname{Mat}(n\times n;\mathbb K)$, $\mathcal P\exp(-\int_0^tA)$ defined by the Dyson series (2.13) and, equivalently, the ordered product limit (2.14) (equivalence is the theorem below); the ordering problem (R2.6.2); corollary proved on the page (B-T2.6.5): if all $A(t)$ commute, $\mathcal P\exp(-\int A)=\exp(-\int_0^tA)$ (termwise differentiation justified by the Banach-algebra power series); the parallel-transport ODE $\dot v=-A(t)v$ as the matrix-group horizontal-lift equation. Verified examples: constant $A$; commuting diagonal $A(t)$; non-example: $A(t)=\sigma_1$ on $[0,1]$ and $\sigma_3$ on $[1,2]$ gives $e^{-\sigma_3}e^{-\sigma_1}\ne e^{-\sigma_1-\sigma_3}$ (computed). Calibration: $\mathcal P\exp$ is invertible with inverse the reversed-order exponential; the value at $t=0$ is $1$.
