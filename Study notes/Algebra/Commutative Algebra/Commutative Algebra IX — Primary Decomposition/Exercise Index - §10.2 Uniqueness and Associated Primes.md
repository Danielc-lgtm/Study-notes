---
type: exercise-index
subject: commutative-algebra
section: "10.2"
tags: [algebra, commutative-algebra]
---

## §10.2 Uniqueness and Associated Primes — Exercises

The exercises of §10.2 drill the invariants of a primary decomposition: which data are forced by the ideal $I$ and which are merely chosen. The recurring techniques are the *colon-ideal probe* (compute $\sqrt{(I:x)}$ to extract associated primes, choosing $x$ to isolate one prime at a time), *localization at an isolated prime* (to canonicalise the isolated component, exploiting that the operation is blind to embedded primes), and *prime avoidance plus Noetherian induction* (to identify the minimal primes as the irreducible components and prove there are finitely many). Together they establish the chapter's central structural fact — the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]] fixes the associated primes, the Second fixes the isolated components, and nothing fixes the embedded components — and translate it into the finiteness and uniqueness of irreducible components of a variety.

- [[Ex - The associated primes via colon ideals]] (⭐⭐) — build the colon-ideal toolkit: $(I:x)$ is an ideal $\supseteq I$ (equal to $R$ when $x \in I$), $(\mathfrak{q}:x)$ stays $\mathfrak{p}$-primary for $x \notin \mathfrak{q}$, and $\sqrt{(I:x)} = \bigcap_{x \notin \mathfrak{q}_i}\mathfrak{p}_i$ recovers $\operatorname{Ass}(I)$; the colon-probe technique behind the First Uniqueness Theorem ([[Def - Primary Ideal]], [[Def - Associated and Minimal Primes]], [[Def - Radical of an Ideal and the Nilradical]], [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)]])

- [[Ex - Embedded primes are not unique]] (⭐⭐⭐) — using $(X^2, XY)$, prove the isolated component $(X)$ is canonical (it equals $I^{ec}$ at $(X)$, since localizing kills the embedded component) while the embedded $(X,Y)$-primary component ranges over the infinite family $(X^2, XY, Y^n)$; the localization-canonicalisation technique and the sharp isolated-versus-embedded dichotomy ([[Def - Associated and Minimal Primes]], [[Def - Primary Ideal]], [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)]], [[Ex - A primary decomposition in k[X,Y]]], [[Ex - The associated primes via colon ideals]])

- [[Ex - Minimal primes and irreducible components]] (⭐⭐) — prove prime avoidance ($\bigcap \mathfrak{a}_i \subseteq \mathfrak{p} \Rightarrow$ some $\mathfrak{a}_i \subseteq \mathfrak{p}$) and that a radical ideal in a Noetherian ring is a finite intersection of its incomparable minimal primes, then identify these as the irreducible components of $V(I)$; the product-of-escapees and maximal-counterexample techniques ([[Def - Prime and Maximal Ideal]], [[Def - Associated and Minimal Primes]], [[Def - Noetherian Ring]], [[Thm - Minimal Primes are Finite in a Noetherian Ring]], [[Def - Irreducible Algebraic Set]])
