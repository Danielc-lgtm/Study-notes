---
type: exercise-index
subject: differential-geometry
section: "1.2"
tags: [geometry, differential-geometry]
---

## §1.2 Smooth Structures — Exercises

This section drills the apparatus of smooth atlases, smooth structures, and the equivalence between different representative atlases. The exercises here focus on computing transition functions, verifying smoothness, and showing that two different atlases on the same topological manifold describe the same smooth structure. Recurring techniques: explicit chart-formula derivation, computation of rational transition functions, verification of smoothness via the chain rule and inspection of denominators, and use of [[Thm - Smooth Structure from Maximal Atlas]] to convert any smooth atlas into a unique smooth structure.

- [[Ex - Compatibility of Two Atlases on the Sphere]] (⭐⭐) — Show that the stereographic atlas and the graph-coordinate atlas on $S^n$ determine the same smooth structure by computing the cross-transition functions $\varphi_i^+ \circ \sigma_N^{-1}$ and verifying smoothness. Drills the practical compatibility test from [[Thm - Smooth Structure from Maximal Atlas]] part (b). ([[Def - Smooth Atlas and Smooth Structure]], [[Def - Transition Function]], [[Thm - Smooth Structure from Maximal Atlas]])

- [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]] (⭐⭐) — The foundational example: construct the smooth atlas on $S^n$ and verify the smoothness of the inversion transition function. Demonstrates the general routine "specify a smooth structure by an atlas". ([[Def - Smooth Atlas and Smooth Structure]], [[Def - Transition Function]])

- **Ex (Lee Example 1.23) — A non-standard smooth structure on $\mathbb{R}$.** Consider the chart $\psi(x) = x^3$ on $\mathbb{R}$. Show $\{(\mathbb{R}, \psi)\}$ is a smooth atlas determining a smooth structure on $\mathbb{R}$ *distinct* from the standard one, because the transition function $\psi \circ \mathrm{id}^{-1}(y) = y^{1/3}$ is not smooth at $0$. However, the two smooth manifolds are *diffeomorphic* via $x \mapsto x^3$. Drills the distinction between "smooth structures on the same topological manifold" (set of) and "diffeomorphism classes of smooth manifolds" (quotient of the set). ([[Def - Smooth Atlas and Smooth Structure]], [[Def - Smooth Manifold]], [[Def - Transition Function]])

- **Ex (web-sourced from Lee Problem 1-6) — Uncountably many smooth structures on $\mathbb{R}$.** Generalize Lee Example 1.23: for each $s > 0$, the homeomorphism $F_s(x) = |x|^{s-1} x$ of $\mathbb{B}^n$ is a diffeomorphism iff $s = 1$. Use this to construct uncountably many smooth structures on any positive-dimensional topological manifold (when it has one to begin with). All are diffeomorphic to the standard structure, but distinct as smooth structures. ([[Def - Smooth Atlas and Smooth Structure]], [[Def - Smooth Manifold]])

- **Ex (Lee Problem 1-8) — Smooth structure on $S^1$ via angle functions.** Identify $S^1 \subseteq \mathbb{R}^2 = \mathbb{C}$ via $(x, y) \mapsto x + iy$. An *angle function* on an open subset $U \subseteq S^1$ is a continuous function $\theta : U \to \mathbb{R}$ with $e^{i\theta(z)} = z$. Show that an angle function exists on $U \subseteq S^1$ iff $U \neq S^1$ (the full circle has no continuous global angle). For such $U$ and $\theta$, show $(U, \theta)$ is a smooth chart for the standard smooth structure on $S^1$. This gives a coordinate-free understanding of $S^1$'s smooth structure. ([[Def - Smooth Atlas and Smooth Structure]], [[Def - Coordinate Chart and Atlas]])
