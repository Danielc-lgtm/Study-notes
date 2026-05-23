---
type: exercise-index
subject: algebraic-topology
section: "3.3"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory]
---

## §3.3 Chern Forms and Characteristic Classes — Exercises

This section drills the computational side of characteristic class theory: extracting integer-valued topological invariants from connections on complex vector bundles via the Chern–Weil construction. The recurring patterns are: **computing $c_1 = F/(2\pi)$ from a $U(1)$ connection**, **integrating the resulting closed 2-form over a closed 2-cycle**, **verifying integrality**, and **identifying the integer with a topological winding number or degree**. The canonical example — the tautological line bundle on $\mathbb{CP}^1$ — is the prototype for all higher-dimensional and higher-rank computations. Master these techniques and you can compute Chern numbers of holomorphic vector bundles on projective varieties, magnetic fluxes through compact surfaces, and Hall conductivities of band structures.

- [[Ex - Computing c_1 of a Line Bundle from a Connection]] (⭐⭐) — Derive the general formula $c_1(L) = F/(2\pi)$ for a complex line bundle with $U(1)$ connection $\omega = -iA$, then verify integrality $\int_{\mathbb{CP}^1} c_1(\mathcal{O}(-1)) = -1$ via the Fubini–Study connection. The starting exercise for all Chern-class computations. ([[Def - First Chern Class]], [[Def - Chern Forms of a U(n) Bundle]], [[Thm - Chern-Weil Theorem (Statement)]])

- [[Ex - The Chern Number of the Hopf Line Bundle over CP^1]] (⭐⭐) — Two independent verifications that $\int c_1(\mathcal{O}(-1)) = -1$: by curvature integration (Chern–Weil) and by topological classification ($\mathcal{O}(-1)$ is the generator of $\mathrm{Pic}(\mathbb{CP}^1) = \mathbb{Z}$). Illustrates the equivalence of differential-geometric and topological viewpoints on characteristic classes. ([[Def - First Chern Class]], [[Def - The Hopf Map]], [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]])

- [[Ex - The Magnetic Monopole and Dirac Quantization via c_1]] (⭐⭐) — Identify the magnetic monopole as a non-trivial $U(1)$ bundle on $S^2$, compute its first Chern class as $2eg/(\hbar c)$, and derive the Dirac quantisation condition $g = n\hbar c/(2e)$ as the integrality of $c_1$. The prototypical physics application of $c_1$ classification. ([[Def - First Chern Class]], [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]])
