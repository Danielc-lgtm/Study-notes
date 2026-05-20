---
type: exercise-index
subject: complex-analysis
section: "2.1"
tags: [analysis, complex-analysis]
---

## §2.1 Contour Integration — Exercises

This section drills the three foundational tools of the chapter: direct parametrisation of a contour integral, the [[Thm - ML Estimate|ML estimate]] as a coarse upper bound, and the equivalence between primitive existence and vanishing of closed-loop integrals. The exercises are designed to build the diagnostic instinct for which tool to reach for when an integral around a closed curve must be computed or shown to vanish: parametrisation when an explicit value is wanted on a small specific curve; ML when the question is asymptotic vanishing on a growing or shrinking family of paths; primitive-existence in contrapositive when the question is whether a global antiderivative is even available on the domain. The seed example $\oint dz/z = 2\pi i$ recurs in all three exercises as the canonical case that separates each technique's domain of applicability.

- [[Ex - Computing zn dz on a circle]] (⭐) — direct parametrisation $\gamma(t) = e^{it}$ converts the contour integral to a real integral; the integral vanishes for all $n \neq -1$ via primitive, gives $2\pi i$ only for $n = -1$ ([[Def - Contour Integral]], [[Thm - Fundamental Theorem of Contour Integration]], [[Def - Primitive (Antiderivative)]])
- [[Ex - ML estimate bounds a circular integral]] (⭐) — denominator-degree-gap heuristic for vanishing on large circles via reverse triangle inequality on the denominator and $M \cdot L$ from ML ([[Thm - ML Estimate]], [[Def - Contour Integral]])
- [[Ex - A primitive exists iff integral around closed curves is zero]] (⭐⭐) — concrete two-direction verification of the equivalence theorem on $f(z) = 1/z$: contour-integral computation rules out a primitive on $\mathbb{C}^\times$; the principal branch of $\log z$ exhibits a primitive on the slit plane ([[Def - Primitive (Antiderivative)]], [[Thm - Existence of a Primitive iff Closed Integrals Vanish]], [[Thm - Fundamental Theorem of Contour Integration]], [[Def - Contour Integral]])
