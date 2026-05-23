---
type: exercise-index
subject: differential-geometry
section: "4.1"
tags: [geometry, differential-geometry]
---

## §4.1 Maps of Constant Rank — Exercises

This section's exercises develop the local theory of smooth maps via the rank of their differentials. The central tool is the [[Thm - The Rank Theorem|rank theorem]] and its specialisations to immersions ([[Thm - Local Immersion Theorem]]) and submersions ([[Thm - Local Submersion Theorem]]). The exercises drill three recurring patterns: (a) verifying that a specific smooth map is an immersion or submersion by computing the differential's rank, (b) using the rank theorem's coordinate normal form to convert a local question about $F$ into a question about a coordinate projection or inclusion, and (c) recognising the topological consequences of the rank conditions — submersions are open maps, immersions are locally embeddings, and constant-rank maps factor through coordinate projection-inclusions. The crowning example is the **Hopf map**, which is a smooth submersion exhibiting the simplest nontrivial fibre bundle structure $S^1 \to S^3 \to S^2$.

- [[Ex - An Injective Immersion is Not Always an Embedding]] (⭐⭐) — Construct two canonical counterexamples (figure-eight and irrational line on torus) showing that an injective smooth immersion need not be a smooth embedding. The failure modes are topological: [[Def - Subspace|subspace]] topology vs. domain topology disagree. ([[Def - Immersion, Submersion, and Embedding]], [[Def - Embedded Submanifold]], [[Def - Immersed Submanifold]], [[Def - Subspace Topology]])

- [[Ex - The Figure-Eight Immersion]] (⭐⭐) — Detailed analysis of the figure-eight curve $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi)$. Verify it is an injective immersion, that its image is not an embedded submanifold (two tangent directions at the crossing), and that the immersed-submanifold structure on the image disagrees with the subspace topology. ([[Def - Immersion, Submersion, and Embedding]], [[Def - Embedded Submanifold]], [[Def - Immersed Submanifold]])

- [[Ex - The Hopf Map is a Submersion]] (⭐⭐) — Verify the Hopf map $h : S^3 \to S^2 \cong \mathbb{CP}^1$ is a smooth submersion by identifying the kernel of $dh$ as the vertical tangent direction along the $S^1$-fibres. This is the canonical nontrivial fibre bundle and the prototype for principal bundles, gauge theory, and quantum information geometry. ([[Def - Immersion, Submersion, and Embedding]], [[Def - Rank of a Smooth Map]], [[Def - The Differential of a Smooth Map]], [[Thm - Local Submersion Theorem]])
