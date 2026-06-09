---
type: exercise-index
subject: commutative-algebra
section: "4.1-4.2"
tags: [algebra, commutative-algebra]
---

## §4.1–4.2 The Construction and the Universal Property — Exercises

These exercises drill the foundational layer of localization: the fraction model, the universal property, and the two key special cases $R_f$ and $R_{\mathfrak{p}}$. The unifying technique is **"abandon fractions, use the universal property"** — to build a map out of $S^{-1}R$ or to identify a localization with a known ring, you produce a map out of $R$ inverting $S$ and let the universal property hand you the rest. The exercises practice three things: recognising $R_{\mathfrak{p}}$ as a local ring (the chapter's central object), presenting a localization as a polynomial quotient $R[T]/(uT-1)$ (the universal property's cleanest application), and pushing localization through a quotient via exactness. Each bottoms out in either the universal property or the exactness of $S^{-1}(-)$, the two engines installed in these sections.

- [[Ex - Localizing at a prime gives a local ring]] (⭐) — show $R_{\mathfrak{p}}$ is local with maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$, by two routes: classify the units of the fraction model ($\tfrac rs$ a unit iff $r\notin\mathfrak{p}$, so the non-units form an ideal) and read off the unique maximal survivor from the prime correspondence ([[Def - Multiplicative Set and Localization]], [[Def - Local Ring and Residue Field]], [[Def - Prime and Maximal Ideal]], [[Thm - Prime Ideals of a Localization]]).

- [[Ex - A localization as a quotient R[T] over (uT-1)]] (⭐⭐) — prove $R_u\cong R[T]/(uT-1)$ by matching universal properties rather than constructing the isomorphism by hand: an $R$-algebra map out of the quotient is a choice of image for $T$ inverting $u$, uniquely $f(u)^{-1}$, which is verbatim the universal property of $R_u$ ([[Thm - Universal Property of Localization]], [[Def - Multiplicative Set and Localization]], [[Def - Polynomial Ring]], [[Def - Quotient Ring]]).

- [[Ex - Localization commutes with quotients]] (⭐) — prove $S^{-1}(M/N)\cong S^{-1}M/S^{-1}N$ by localizing the defining short exact sequence and reading off the cokernel, then deduce the residue field $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}\cong\operatorname{Frac}(R/\mathfrak{p})$ ([[Thm - Localization is Exact and the Localization is Flat]], [[Thm - Localization Commutes with Quotients and Finite Operations]], [[Def - Quotient Module]], [[Def - Local Ring and Residue Field]]).
