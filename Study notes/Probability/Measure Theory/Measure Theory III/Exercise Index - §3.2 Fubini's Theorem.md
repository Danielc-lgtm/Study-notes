---
type: exercise-index
subject: measure-theory
section: "3.2"
tags: [analysis, measure-theory]
---

## §3.2 Fubini's Theorem — Exercises

The exercises of §3.2 drill Fubini's theorem and its boundary cases. The recipe is invariant: Tonelli on $|f|$ first (to check $f \in L^1$), then Fubini on $f$ to interchange. Each exercise illustrates a different facet: an explicit failure when integrability fails (an unbounded sum whose iterated values disagree), the layer-cake identity that converts $\int f$ into $\int \mu(\{f > t\})\,dt$ by integrating the indicator under the graph two ways, and the Gaussian integral computed by squaring to expose a rotational symmetry invisible in one [[Def - Dimension|dimension]].

- [[Ex - Fubini fails without integrability]] (⭐⭐) — iterated integrals can disagree when $f\notin L^1$; check $\iint|f|$ first ([[Thm - Fubini-Tonelli Theorem]])
- [[Ex - The area under a graph]] (⭐⭐) — the layer-cake formula $\int f\,d\mu=\int_0^\infty\mu(f>t)\,dt$ from Tonelli ([[Thm - Fubini-Tonelli Theorem]], [[Thm - Product Measure]])
- [[Ex - The Gaussian integral via Fubini]] (⭐⭐) — $\int e^{-x^2/2}\,dx=\sqrt{2\pi}$ by squaring, Tonelli, and polar coordinates ([[Thm - Fubini-Tonelli Theorem]], [[Def - Lebesgue Measure]])
