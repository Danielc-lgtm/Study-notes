---
type: exercise-index
subject: commutative-algebra
section: "10.1"
tags: [algebra, commutative-algebra]
---

## §10.1 Primary Ideals and Decomposition — Exercises

The exercises of §10.1 drill the foundational layer of the chapter: what a [[Def - Primary Ideal|primary ideal]] is, how to certify or refute primariness, and how to compute an explicit primary decomposition. The recurring techniques are the *quotient criterion* (a question about $\mathfrak{q}$ becomes a question about zero-divisors and nilpotents in $R/\mathfrak{q}$), the *maximal-radical shortcut* (a maximal radical forces primariness for free), and the *guess-and-verify* method for decompositions (read the components off the geometry, then check primariness and the intersection by a generator chase). Together they sever the integer-bred intuition "primary $=$ prime power" in both directions and establish the canonical worked example $I = (X^2, XY)$ that the whole chapter returns to — the line plus an embedded point.

- [[Ex - A primary decomposition in k[X,Y]]] (⭐⭐) — compute two distinct minimal primary decompositions of $(X^2, XY)$ and read off the line $(X)$ (isolated) plus the embedded point $(X,Y)$; the canonical decomposition computation, combining the maximal-radical shortcut with a generator chase ([[Def - Primary Ideal]], [[Def - Associated and Minimal Primes]], [[Def - Prime and Maximal Ideal]], [[Def - Radical of an Ideal and the Nilradical]], [[Thm - Maximal and Prime Ideals via Quotients]], [[Ex - Powers of a maximal ideal are primary]])

- [[Ex - Powers of a maximal ideal are primary]] (⭐⭐) — prove $\sqrt{\mathfrak{q}} = \mathfrak{m}$ maximal $\Rightarrow$ $\mathfrak{q}$ is $\mathfrak{m}$-primary, hence every $\mathfrak{m}^n$ is $\mathfrak{m}$-primary; the maximal-radical shortcut, via "the quotient is local with nilpotent maximal ideal, so non-unit $=$ nilpotent" ([[Def - Primary Ideal]], [[Def - Prime and Maximal Ideal]], [[Def - Radical of an Ideal and the Nilradical]], [[Def - Local Ring and Residue Field]])

- [[Ex - A primary ideal need not be a prime power]] (⭐⭐) — sever "primary $=$ prime power" both ways: $(X, Y^2)$ is primary but not a prime power (it sits between $(X,Y)^2$ and $(X,Y)$), and $\mathfrak{p}^2$ on the cone $XY = Z^2$ is a prime power that is not primary (the defining relation injects a non-nilpotent zero-divisor); the counterexample-construction technique ([[Def - Primary Ideal]], [[Def - Prime and Maximal Ideal]], [[Def - Radical of an Ideal and the Nilradical]], [[Thm - Maximal and Prime Ideals via Quotients]], [[Def - Quotient Ring]])
