---
type: exercise-index
subject: commutative-algebra
section: "7.2"
tags: [algebra, commutative-algebra]
---

## §7.2 The Nullstellensatz and the Dictionary — Exercises

The exercises of §7.2 drill the algebra–geometry dictionary that the Nullstellensatz installs: radical ideals correspond to algebraic sets, primes to irreducible varieties, maximal ideals to points. The recurring technique is *translation across $V$ and $I$*: convert a geometric statement to an algebraic one (or vice versa) using the formal properties of $V$ and the strong-Nullstellensatz identity $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$, inserting a radical exactly at each $I \circ V$ step. The exercises also drill the two refinements of the bijection — that maximal ideals are points (computed by passing to a residue field and applying Zariski's lemma) and that prime ideals are irreducible varieties (proved via "vanishing of a product = union of zero loci") — and the lattice arithmetic that turns unions into intersections of ideals and intersections into radicals of sums.

- [[Ex - Maximal ideals of a polynomial ring over an algebraically closed field]] (⭐⭐) — establish the bottom rung of the dictionary, $\Omega^n \xrightarrow{\sim} \operatorname{mSpec}$, $x \mapsto \mathfrak m_x$, by passing a maximal ideal to its residue field, applying Zariski's lemma, and collapsing via algebraic closure; exhibit the $\mathbb{R}$-counterexample where the residue field is $\mathbb{C}$ ([[Thm - The Weak Nullstellensatz]], [[Thm - Zariski's Lemma]], [[Def - Prime and Maximal Ideal]], [[Thm - Maximal and Prime Ideals via Quotients]], [[Def - Polynomial Ring]]).

- [[Ex - The radical as the intersection of maximal ideals containing it]] (⭐⭐) — prove $\sqrt{I} = \bigcap_{I \subseteq \mathfrak m}\mathfrak m$ for a finitely generated $k$-algebra (the Jacobson property), by rewriting the radical as $I(V(I))$ via the strong Nullstellensatz and identifying the maximal ideals above $I$ with the points of $V(I)$; contrast with the general-ring truth that only *primes* suffice ([[Thm - The Strong Nullstellensatz]], [[Thm - The Weak Nullstellensatz]], [[Def - Radical of an Ideal and the Nilradical]], [[Def - Prime and Maximal Ideal]], [[Def - Finitely Generated Algebra]]).

- [[Ex - The ideal-variety correspondence and unions and intersections]] (⭐⭐) — determine that $I(X \cup Y) = I(X) \cap I(Y)$ is the always-true identity while $I(X \cap Y) = \sqrt{I(X) + I(Y)}$ needs the radical, by pushing $V$ through the sum and applying $I(V(\mathfrak b)) = \sqrt{\mathfrak b}$; show via a parabola-tangent-to-line that the radical (recording intersection multiplicity) cannot be dropped ([[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)]], [[Thm - The Strong Nullstellensatz]], [[Def - Affine Variety and the Vanishing Set]], [[Def - The Coordinate Ring and the Ideal of a Set]], [[Def - Radical of an Ideal and the Nilradical]]).

- [[Ex - Irreducible iff the ideal is prime]] (⭐⭐) — prove $X$ irreducible $\iff I(X)$ prime $\iff \Omega[X]$ a domain, the geometric-atoms refinement of the dictionary, by translating "$fg \in I(X)$" into the covering $X \subseteq V(f) \cup V(g)$ and using that a prime equal to a finite intersection equals a factor (ES2 Q2a); contrast the reducible $V(T_1 T_2)$ ([[Def - Irreducible Algebraic Set]], [[Thm - The Strong Nullstellensatz]], [[Thm - The Weak Nullstellensatz]], [[Def - Prime and Maximal Ideal]], [[Def - The Coordinate Ring and the Ideal of a Set]]).
