---
type: exercise-index
subject: differential-geometry
section: "1.1"
tags: [geometry, differential-geometry, topology]
---

## §1.1 Topological Manifolds — Exercises

This section drills the foundational topological structure of a [[Def - Topological Manifold|topological manifold]]: the three axioms (Hausdorff, second-countable, locally Euclidean), how to verify them on concrete spaces, and what goes wrong when one fails. The exercises here exercise pure topology, not smoothness — the smooth structure comes in §1.2. Recurring techniques: inheritance of Hausdorff/second-countability via [[Def - Subspace|subspace]]/product/quotient, construction of explicit chart maps, recognition of pathological non-examples (the line with two origins, uncountable disjoint unions).

- [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]] (⭐⭐) — Construct a 2-chart smooth atlas on $S^n$ using stereographic projection, compute the transition function as inversion $u \mapsto u/|u|^2$, verify smoothness. The foundational worked example for "compact manifold needs at least two charts". ([[Def - Topological Manifold]], [[Def - Coordinate Chart and Atlas]], [[Def - Transition Function]], [[Thm - Smooth Structure from Maximal Atlas]])

- [[Ex - Real Projective Space is a Smooth Manifold]] (⭐⭐) — Construct the standard $(n+1)$-chart affine atlas on $\mathbb{RP}^n$, verify Hausdorff and second-countability via the open-map property of the quotient projection, derive rational transition functions. Drills the quotient-by-[[Def - Group|group]]-action construction. ([[Def - Topological Manifold]], [[Def - Coordinate Chart and Atlas]], [[Def - Smooth Atlas and Smooth Structure]])

- **Ex (web-sourced from Lee Problem 1-1) — The line with two origins is not Hausdorff.** Consider the quotient of $\mathbb{R} \times \{0, 1\}$ by the equivalence $(x, 0) \sim (x, 1)$ for $x \neq 0$. Show this space is locally Euclidean and second-countable but not Hausdorff: the two origins $[0, 0]$ and $[0, 1]$ cannot be separated by disjoint open neighbourhoods. This is the canonical pathology of dropping Hausdorff. The argument requires constructing the quotient topology explicitly and verifying limits do not converge uniquely. ([[Def - Topological Manifold]], [[Def - Separation Axioms]])

- **Ex (web-sourced from Lee Problem 1-2) — Uncountable disjoint union is not second-countable.** Show $\mathbb{R} \times S$ (with $S$ uncountable, discrete topology) is locally Euclidean and Hausdorff but not second-countable: any basis for the topology must include open sets in each of the uncountably many connected components. This is the canonical pathology of dropping second-countability. ([[Def - Topological Manifold]], [[Def - First and Second Countable]])

- **Ex (Lee Problem 1-3) — Locally Euclidean Hausdorff + $\sigma$-compact iff topological manifold.** A locally Euclidean Hausdorff space is a topological manifold iff it is *$\sigma$-compact* (a union of countably many compact [[Def - Subspace|subspaces]]). This characterizes the second-countability axiom intrinsically using compactness. Requires the equivalence between second-countability and $\sigma$-compactness for locally Euclidean Hausdorff spaces. ([[Def - Topological Manifold]], [[Def - First and Second Countable]], [[Def - Compact Space]])
