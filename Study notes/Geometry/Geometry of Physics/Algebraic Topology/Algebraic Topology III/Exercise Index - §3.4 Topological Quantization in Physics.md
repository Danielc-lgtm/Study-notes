---
type: exercise-index
subject: algebraic-topology
section: "3.4"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory, physics]
---

## §3.4 Topological Quantisation in Physics — Exercises

This section drills the *physical* applications of characteristic class theory: every integer-valued conserved quantity in gauge theory and condensed matter is a Chern number, and its integrality is a consequence of the obstruction-cocycle picture. The two canonical examples are the **magnetic monopole** (a $U(1)$ bundle on $S^2$ surrounding the singularity, with $c_1 = $ monopole charge) and the **Yang–Mills instanton** (an $SU(n)$ bundle on $\mathbb{R}^4$ extended to $S^4$, with $c_2 = $ instanton number). The recurring patterns are: **identifying the bundle structure of a physical configuration**, **computing the relevant Chern number via Chern–Simons reduction or direct integration**, and **interpreting the integer as a topological quantum number** (charge, winding, vorticity). Master these and you can analyse topological phases of matter, instanton physics, vortex configurations, and the topological terms in QFT actions.

- [[Ex - The Magnetic Monopole and Dirac Quantization via c_1]] (⭐⭐) — Identify the magnetic monopole bundle, compute $\int_{S^2} c_1 = 2eg/(\hbar c)$, derive Dirac quantisation $g = n\hbar c/(2e)$. The prototype of topological quantisation in physics. ([[Def - First Chern Class]], [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]])

- [[Ex - Winding Number of the BPST Instanton is 1]] (⭐⭐⭐) — Use Frankel's identity (22.5) and the Chern–Simons reduction to compute $\int_{\mathbb{R}^4} c_2 = 1$ for the BPST instanton, identifying the integer with the degree of the gauge transformation $g : S^3_\infty \to SU(2)$. The cornerstone of Yang–Mills topology and the foundation of Donaldson theory. ([[Def - Second Chern Class]], [[Thm - Chern-Weil Theorem (Statement)]], [[Thm - Chern Forms are Closed and Their Cohomology Class is Independent of Connection]])

- [[Ex - The Chern Number of the Hopf Line Bundle over CP^1]] (⭐⭐) — Although filed under §3.3, the Hopf line bundle is the *exact* analogue of the unit-charge magnetic monopole: it is a $U(1)$ bundle on $S^2$ with $|c_1| = 1$, demonstrating the topological quantisation principle in the simplest non-trivial example. ([[Def - First Chern Class]], [[Def - The Hopf Map]], [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]])
