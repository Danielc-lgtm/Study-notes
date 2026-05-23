---
type: exercise-index
subject: differential-geometry
section: "5.1"
tags: [geometry, differential-geometry]
---

## §5.1 Vector Fields and Integral Curves — Exercises

These exercises drill the foundational manipulations of vector fields and integral curves: the chart-based definition, the smoothness criteria, and the coordinate formula for the Lie bracket. The first exercise is a direct computational exercise with the bracket; later exercises in this section's wider context probe smoothness and chart-independence. The recurring technique is to write a vector field as $X = X^i \partial_i$ in a chart and reduce manifold-level questions to standard calculus.

- [[Ex - The Lie Bracket in Coordinates]] (⭐) — Direct application of the coordinate formula $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ to two explicit vector fields on $\mathbb{R}^3$; verifies that bracket of coordinate vector fields vanishes. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Smooth Vector Field]], [[Thm - Lie Bracket Properties]])

- [[Ex - The Coordinate Vector Fields Commute]] (⭐) — Show $[\partial_i, \partial_j] = 0$ in any chart, both via the coordinate formula and via equality of mixed partial derivatives. The two routes illuminate complementary aspects of the bracket — components-perspective vs operator-perspective. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Smooth Vector Field]])

- [[Ex - Lie Derivative Annihilates Constant Functions]] (⭐) — Show $\mathcal{L}_X f = Xf$ for any vector field $X$ and function $f$, hence $\mathcal{L}_X$ vanishes on constants. Reinterpret as a characterization of conservation laws: $f$ is constant along the flow iff $Xf = 0$. ([[Def - Lie Derivative of a Vector Field]], [[Def - Smooth Vector Field]])
