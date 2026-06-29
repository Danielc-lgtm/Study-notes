---
type: exercise-index
subject: special-relativity
section: "3.1"
tags: [physics, special-relativity]
---

## §3.1 Spacetime as an Affine Space — Exercises

The exercises of §3.1 drill the two foundational structures of the chapter: the **affine** structure of spacetime (points are events, only their differences are four-vectors) and the **pseudo-orthonormal basis** built from the indefinite metric. The recurring technique is operation 1 — choosing an orthonormal basis adapted to a timelike vector — which is the master computational move of the whole topic, and the recurring conceptual point is that the additive constant of a Poincaré translation is exactly what distinguishes a four-vector (a displacement, which transforms homogeneously) from the coordinates of a single event (which do not). Building an orthonormal basis by indefinite-metric Gram-Schmidt also exposes where the Lorentzian signature departs from the Euclidean: null vectors cannot be pivots, and Sylvester's law forces exactly one timelike basis vector.

- [[Ex - Events form an affine space and displacements form vectors]] (⭐) — show that single-event coordinates pick up the translation constant $a^\mu$ under a Poincaré transformation while differences cancel it, verify Chasles' relation, and conclude the interval is origin-independent ([[Def - Minkowski Space and the Metric]], [[Def - Four-Vector]], [[Def - The Lorentz Transformation]], [[Def - The Spacetime Interval]])
- [[Ex - Constructing an orthonormal basis (Gram-Schmidt with indefinite metric)]] (⭐⭐) — run indefinite-metric Gram-Schmidt from a timelike vector, normalising by √|v·v|, observing the forced signature (1,3), and identifying why a null vector cannot serve as a pivot ([[Def - Minkowski Space and the Metric]], [[Def - Classification of Four-Vectors]], [[Def - Metric Duality and Index Manipulation]])
- [[Ex - Classifying four-vectors by the sign of the norm]] (⭐) — compute one scalar square per vector to classify it, exhibit a boost that flips a spacelike vector's time-sign but none that flips a timelike vector's, and identify the interval as the frame-independent causal criterion ([[Def - Classification of Four-Vectors]], [[Def - Minkowski Space and the Metric]], [[Thm - Invariance of the Spacetime Interval]])
