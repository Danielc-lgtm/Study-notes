---
type: exercise-index
subject: topology
section: "5"
tags: [analysis, topology, separation-axioms]
---

## §5 Separation Axioms — Exercises

The exercises of §5 drill the hierarchy $T_1 \subsetneq T_2 \subsetneq T_3 \subsetneq T_4$ and the strictness of each inclusion. Each counterexample is the canonical witness for one separation strict step: cofinite topology shows $T_1 \neq T_2$ (the singletons are closed but no two opens are disjoint), a refined plane topology shows $T_2 \neq T_3$, and $T_3 \neq T_4$ is the harder construction. Hausdorff transfers to subspaces; normality does not.

- [[Ex - A T1 space that is not Hausdorff]] (⭐⭐) — The cofinite topology on $\mathbb{N}$ realizes $T_1$ (singletons closed) but not Hausdorff (every two nonempty opens intersect on an infinite ambient); the sequence $x_n = n$ converges to every point, making the failure of unique limits maximal. ([[Def - Separation Axioms]], [[Def - Topological Space]])

- [[Ex - A Hausdorff space that is not regular]] (⭐⭐⭐) — A refined topology on $\mathbb{R}^2$ adding the "punctured disc" neighbourhoods at the origin produces a Hausdorff (inherited from the usual Euclidean topology) but non-regular space — the punctured $x$-axis is closed and disjoint from the origin but cannot be separated by disjoint opens. ([[Def - Separation Axioms]], [[Def - Topological Space]], [[Def - Closure, Interior, and Boundary]])

- [[Ex - Subspace of Hausdorff is Hausdorff]] (⭐) — The hereditary property of Hausdorff: any subspace of a Hausdorff space is Hausdorff via the "intersect with $A$" recipe, prototypical for transferring $T_0, T_1, T_2, T_3$ but not $T_4$ to subspaces. ([[Def - Separation Axioms]], [[Def - Subspace Topology]])
