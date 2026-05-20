---
type: exercise-index
subject: topology
section: "6"
tags: [analysis, topology, nets]
---

## §6 Nets — Exercises

The exercises of §6 drill the net formalism and its necessity beyond sequences. Each exercise shows why sequences are *not* enough in general topology: the universal-net property collapses to "eventually constant" for sequences (so the truly useful universal subnets need genuine nets); non-Hausdorff spaces admit nets with multiple limits; and in non-first-countable spaces, closure points need not be sequential limits. The unifying observation: nets are the right generalisation of sequences for general topology, characterising closure, continuity, and compactness uniformly.

- [[Ex - A sequence is universal iff eventually constant]] (⭐⭐) — Shows that the universal-net property is vacuous for sequences (forces eventual constancy), motivating the need for nets indexed by general directed sets; the analogous universal subnet machinery is genuinely useful and gives the convergent-subnet characterization of compactness. ([[Def - Directed Set and Net]], [[Def - Subnet and Universal Net]])

- [[Ex - A net that converges to two points]] (⭐⭐) — Construct a net in the cofinite topology on $\mathbb{N}$ converging to both $0$ and $1$, using the canonical "directed set of pairs of shrinking neighbourhoods" trick — the reverse direction of the Hausdorff iff unique-net-limits theorem. ([[Def - Separation Axioms]], [[Def - Directed Set and Net]], [[Def - Net Convergence]], [[Thm - Hausdorff Iff Unique Net Limits]])

- [[Ex - A closure point not reached by any sequence]] (⭐⭐⭐) — In $ω_1 + 1$ with the order topology, the maximum $ω_1$ is a limit point of $[0, ω_1)$ but no sequence in $[0, ω_1)$ converges to it (a countable sup of countable ordinals is countable); demonstrates non-first-countability and the necessity of nets over sequences for closure characterizations. ([[Def - Topological Space]], [[Def - Closure, Interior, and Boundary]], [[Def - Directed Set and Net]], [[Def - Net Convergence]], [[Thm - Closure via Nets]])
