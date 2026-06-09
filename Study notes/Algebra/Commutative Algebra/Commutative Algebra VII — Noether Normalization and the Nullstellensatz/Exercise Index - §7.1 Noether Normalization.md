---
type: exercise-index
subject: commutative-algebra
section: "7.1"
tags: [algebra, commutative-algebra]
---

## §7.1 Noether Normalization — Exercises

The exercises of §7.1 drill the structural theorem that every finitely generated $k$-algebra is a finite module over a polynomial ring, and the two hypotheses it relies on. The central technique is the *linear shear that makes an algebraic relation monic*: read off the defining relation, isolate its top homogeneous form, choose a generic direction so the leading coefficient becomes a unit, and read the resulting integral equation. The supporting technical lemmas — that a nonzero homogeneous polynomial dehomogenises to a nonzero one (ES1 Q1b), and that a nonzero polynomial over an infinite field has a non-root (ES1 Q1c, Schwartz–Zippel) — are exactly what guarantee the good direction exists, and they pin down where *infinitude* of the field (as opposed to algebraic closure) is the operative hypothesis. The payoff is geometric: normalization is a finite surjection of a variety onto affine space, and the number of polynomial coordinates is the dimension = transcendence degree.

- [[Ex - Noether normalization of a plane curve]] (⭐⭐) — carry out the normalization of $k[X, Y]/(f)$ explicitly by shearing coordinates to make $f$ monic in one variable, exhibit the integral equation, and read off $\dim = \operatorname{trdeg} = 1$; work the elliptic curve $y^2 = x^3 + x$ as a $2$-sheeted cover of $\mathbb{A}^1$ ([[Thm - Noether Normalization]], [[Def - Algebraic Independence and Transcendence Degree]], [[Def - Integral Element and Integral Extension]], [[Def - The Coordinate Ring and the Ideal of a Set]], [[Def - Polynomial Ring]]).

- [[Ex - Why algebraic closure is needed in the Nullstellensatz]] (⭐⭐) — separate the hypotheses "infinite" (needed for the linear shear, via the homogeneous-dehomogenisation lemma ES1 Q1b and the zero-avoidance lemma ES1 Q1c) from "algebraically closed" (needed for solution-existence); build the $\mathbb{R}$-counterexample to the Nullstellensatz and the finite-field counterexample to zero-avoidance, and spread inclusions from $\mathbb{C}$ to $\overline{\mathbb{F}_p}$ via reduction mod $p$ (ES3 Q8) ([[Thm - Noether Normalization]], [[Thm - The Weak Nullstellensatz]], [[Thm - The Strong Nullstellensatz]], [[Def - Affine Variety and the Vanishing Set]], [[Def - Polynomial Ring]]).

- [[Ex - Maximal ideals of a polynomial ring over an algebraically closed field]] (⭐⭐) — classify $\operatorname{mSpec} \Omega[T_1, \dots, T_n]$ as the points $\mathfrak m_x$ by passing to the residue field and squeezing it with Zariski's lemma (itself the immediate corollary of normalization), then collapsing the finite extension via algebraic closure; exhibit the $\mathbb{R}$-counterexample $(T^2+1)$ ([[Thm - Zariski's Lemma]], [[Thm - The Weak Nullstellensatz]], [[Def - Prime and Maximal Ideal]], [[Thm - Maximal and Prime Ideals via Quotients]], [[Def - Polynomial Ring]]).
