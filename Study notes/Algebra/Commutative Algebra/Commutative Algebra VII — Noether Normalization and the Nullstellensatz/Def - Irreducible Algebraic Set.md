---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Affine Variety and the Vanishing Set"
  - "Def - The Coordinate Ring and the Ideal of a Set"
  - "Def - Prime and Maximal Ideal"
  - "Def - Integral Domain"
  - "Def - Radical of an Ideal and the Nilradical"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. We keep the chapter's standing data: a field $k$, an algebraically closed $\Omega \supseteq k$, affine space $\Omega^n$, the vanishing operation $V$ and the ideal operation $I$. We write $X = V(\mathfrak a)$ for an algebraic set and $k[X] = k[T_1, \dots, T_n]/I(X)$ for its coordinate ring. For this definition we work with **$\Omega$-algebraic sets** (i.e. $k = \Omega$), so that $I(X) \subseteq \Omega[T_1, \dots, T_n]$. The full registry is on [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

---

# Axiom Motivation

The vanishing-set construction had the property $V(\mathfrak a \mathfrak b) = V(\mathfrak a) \cup V(\mathfrak b)$: algebraic sets can break into unions. The union of the two coordinate axes, $V(T_1 T_2) = V(T_1) \cup V(T_2)$, is visibly two separate lines stuck together at the origin; it is *decomposable*, and studying it as one object is like studying $6 = 2 \times 3$ without noticing it factors. We want to name the **indecomposable** algebraic sets — the geometric atoms out of which everything else is built — and then express every algebraic set as a finite union of them. The indecomposable ones are called **irreducible**, and the punchline of the page is that *irreducibility of the geometry is exactly primality of the ideal*: the geometric atoms correspond to the prime ideals, just as the integer atoms (primes) correspond to the prime numbers.

**Why "not a union of two proper closed subsets" and not "connected".** The naive guess for "indecomposable" is *connected* — cannot be split into two disjoint pieces. But that is the wrong notion here, and seeing why pins down the definition. The two axes $V(T_1 T_2)$ are *connected* (they meet at the origin) yet should certainly count as decomposable — they are two lines. So the right condition is not about disjoint pieces but about *any* covering by two smaller closed sets: $X$ is **irreducible** if it is nonempty and cannot be written as $X = X_1 \cup X_2$ with $X_1, X_2$ proper closed subsets — *even if $X_1$ and $X_2$ overlap*. The axes fail this: $V(T_1 T_2) = V(T_1) \cup V(T_2)$ with each axis a proper closed subset. The strength of "irreducible" over "connected" is exactly what is needed: it forbids decomposition even when the pieces are glued, and it is the condition that translates to primality. In the coarse Zariski topology, where any two nonempty open sets meet, irreducible is the natural and useful notion; connectedness is too weak.

**Why nonemptiness is required.** We demand $X \neq \varnothing$ in the definition, for the same reason a prime ideal must be proper and the number $1$ is not prime: the empty set is vacuously "not a union of two proper subsets" in a useless way, and admitting it would force every theorem ("$X$ irreducible $\iff I(X)$ prime") to carry an exception, since $I(\varnothing) = \Omega[T_1, \dots, T_n]$ is the unit ideal, which is *not* prime. Excluding $\varnothing$ keeps the correspondence "irreducible $\leftrightarrow$ prime" clean, matching "prime ideals are proper".

**Why irreducible matches prime — the mechanism.** Here is the heart, worth seeing before the formal proof. Suppose $I(X)$ is *not* prime: there are $f, g \notin I(X)$ with $fg \in I(X)$. The product $fg$ vanishes on all of $X$, so at every point of $X$, $f = 0$ or $g = 0$ — meaning $X \subseteq V(f) \cup V(g)$, hence $X = (X \cap V(f)) \cup (X \cap V(g))$. Since $f \notin I(X)$, $f$ does *not* vanish on all of $X$, so $X \cap V(f)$ is a *proper* closed subset; likewise $X \cap V(g)$. So $X$ is a union of two proper closed subsets: $X$ is reducible. Run the implication backwards and irreducible forces prime. The dictionary is exact: a *reducible geometry* is a *factorisation of the ideal-membership condition* $fg \in I(X)$ with neither factor in $I(X)$ — which is precisely the failure of primality. "Vanishing of a product = union of two vanishing loci" is the geometric face of "$fg \in \mathfrak p \Rightarrow f \in \mathfrak p$ or $g \in \mathfrak p$".

**Why this gives decomposition into components.** Once irreducible sets are identified with primes, the structure theory follows from the algebra. The polynomial ring is [[Def - Noetherian Ring|Noetherian]] (Hilbert basis theorem), so it has no infinite ascending chains of ideals, hence the radical ideals have only finitely many minimal primes, hence every algebraic set is a *finite* union of irreducible ones — its **irreducible components** — uniquely once you discard redundant pieces. This is the geometric analogue of unique factorisation: every algebraic set factors into irreducible components as every integer factors into primes, and the components are the minimal primes of $I(X)$. The whole apparatus — atoms, factorisation, uniqueness — is imported wholesale from the algebra by the irreducible-equals-prime dictionary.

---

# The Definition

Fix an algebraically closed field $\Omega$ and $n \geq 0$.

## Irreducible algebraic set

An algebraic set $X \subseteq \Omega^n$ is **irreducible** if $X \neq \varnothing$ and $X$ is **not** the union of two proper algebraic subsets: whenever
$$X = X_1 \cup X_2 \quad \text{with } X_1, X_2 \text{ algebraic subsets of } X,$$
then $X_1 = X$ or $X_2 = X$. An irreducible algebraic set is also called an **affine variety**. A non-irreducible algebraic set is **reducible**.

## Equivalent characterisations

For a nonempty algebraic set $X \subseteq \Omega^n$, the following are equivalent (the second is [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|proved via the Nullstellensatz]]):

1. $X$ is irreducible.
2. The ideal $I(X) \subseteq \Omega[T_1, \dots, T_n]$ is a [[Def - Prime and Maximal Ideal|prime ideal]].
3. The coordinate ring $\Omega[X] = \Omega[T_1, \dots, T_n]/I(X)$ is an [[Def - Integral Domain|integral domain]].
4. Every nonempty (Zariski-)open subset of $X$ is dense in $X$; equivalently, any two nonempty open subsets of $X$ intersect.

## Irreducible components

Every algebraic set $X$ is a finite union $X = X_1 \cup \dots \cup X_r$ of irreducible algebraic sets, and this is unique up to order once no $X_i$ contains another. The $X_i$ are the **irreducible components** of $X$, and they correspond bijectively to the **minimal primes** of the radical ideal $I(X)$.

---

# Categorical / Structural Definition

Structurally, irreducibility is a property of the topological space $X$ alone, transported to algebra by the coordinate ring. A topological space is **irreducible** if it is nonempty and not the union of two proper closed subsets; equivalently every nonempty open is dense; equivalently any two nonempty opens meet. The translation to algebra runs through the [[Def - The Coordinate Ring and the Ideal of a Set|coordinate ring]]: $X$ is irreducible iff $\Omega[X]$ is an integral domain, because zero-divisors in $\Omega[X]$ are exactly pairs of functions whose vanishing loci cover $X$. So "geometric atom" = "irreducible space" = "domain coordinate ring" = "prime defining ideal". The structure theorem — finitely many components — is the topological statement that a **Noetherian** space (one with the descending chain condition on closed sets) is a finite union of irreducible closed subsets, which is the geometric shadow of the [[Def - Noetherian Ring|Noetherian]] ascending chain condition on the ring (Hilbert basis theorem). The components are the maximal irreducible closed subsets, dual to the minimal primes.

---

# Relate to Other Fields / Compression

The cleanest compression: **irreducible is to algebraic sets what prime is to ideals and what prime number is to integers — the indecomposable atom**, with the dictionary $X$ irreducible $\iff I(X)$ prime $\iff \Omega[X]$ a domain.

**True name:** the true name of "$X$ is irreducible" is "**$\Omega[X]$ is an integral domain**" — the form you actually use. To prove a variety irreducible, show its coordinate ring has no zero divisors (often by exhibiting it as a subring of a field, e.g. a polynomial ring); to use irreducibility, treat $\Omega[X]$ as a domain with a [[Def - Field of Fractions|field of fractions]] — the **function field** $\Omega(X) = \operatorname{Frac}(\Omega[X])$, whose [[Def - Algebraic Independence and Transcendence Degree|transcendence degree]] is the dimension of $X$.

The same indecomposability pattern appears throughout: a **connected** space is one not split by disjoint opens (weaker than irreducible); a [[Def - Irreducible and Prime Elements|prime element]] of a ring is one that does not factor nontrivially; a [[Def - Composition Series and Length|simple module]] is one with no proper nonzero submodule. Irreducibility is the version of "atom" appropriate to the Zariski topology, and it is strictly stronger than connectedness precisely because the Zariski topology is so coarse that "indecomposable" must forbid even overlapping decompositions.

---

# Examples / Corollaries

**Is an instance — affine space and any hypersurface of an irreducible polynomial.** $\Omega^n$ itself is irreducible: $I(\Omega^n) = (0)$, which is prime because $\Omega[T_1, \dots, T_n]$ is a domain. A hypersurface $V(f)$ for *irreducible* $f$ is irreducible: $I(V(f)) = (f)$ (by the Nullstellensatz, since $(f)$ is radical when $f$ is irreducible — the polynomial ring is a [[Def - Unique Factorization Domain|UFD]]), and $(f)$ is prime because an irreducible element generates a prime ideal in a UFD. So the parabola $V(T_2 - T_1^2)$ and the nodal cubic $V(T_2^2 - T_1^3 - T_1^2)$ are irreducible varieties.

**Is an instance — a single point.** $\{x\}$ is irreducible: $I(\{x\}) = \mathfrak m_x$ is maximal, hence prime; its coordinate ring is the field $\Omega$, a domain. Points are the zero-dimensional irreducible sets.

**Is NOT an instance — the union of two axes.** $X = V(T_1 T_2) = V(T_1) \cup V(T_2)$ is reducible: it is the union of two proper algebraic subsets (the axes). Correspondingly $I(X) = (T_1 T_2) = (T_1) \cap (T_2)$ is *not* prime — $T_1 \cdot T_2 \in I(X)$ but neither $T_1$ nor $T_2$ is — and $\Omega[X] = \Omega[T_1, T_2]/(T_1 T_2)$ has zero divisors $\bar T_1 \bar T_2 = 0$. Its components are the two axes, the minimal primes $(T_1)$ and $(T_2)$.

**Is NOT an instance — a reducible conic.** $V(T_1^2 - T_2^2) = V(T_1 - T_2) \cup V(T_1 + T_2)$ is a pair of crossing lines, reducible because $T_1^2 - T_2^2 = (T_1 - T_2)(T_1 + T_2)$ factors; the ideal $(T_1^2 - T_2^2)$ is not prime. Contrast $V(T_1^2 + T_2^2 - 1)$ (a smooth conic), which *is* irreducible over $\mathbb{C}$ because $T_1^2 + T_2^2 - 1$ is irreducible.

**Corollary — irreducible plus closed determines the components.** Because $\Omega[T_1, \dots, T_n]$ is Noetherian, every algebraic set has finitely many irreducible components, recoverable as $V(\mathfrak p_i)$ for the minimal primes $\mathfrak p_i$ of $I(X)$. This is the geometric form of "a radical ideal in a Noetherian ring is a finite intersection of primes" (an exercise from [[Commutative Algebra IV — Localization|the localization chapter's]] orbit), and the precise analogue of prime factorisation.

**Calibration check.** Confirm $\Omega^n$ and $\{x\}$ are irreducible by naming the prime ideal in each case. Show $V(T_1 T_2)$ is reducible by exhibiting the two proper closed subsets *and* the zero-divisors in its coordinate ring. Verify that $V(f)$ is irreducible iff $f$ is (a power of) an irreducible polynomial. If you can also state why "any two nonempty opens meet" is equivalent to irreducibility — using that open sets are complements of proper closed subsets — you have connected the topological and algebraic faces.

---

# Unlocked by This

> [!tip] Irreducible components and the function field *(from Algebraic Geometry)*
> The decomposition of an algebraic set into **irreducible components** is the geometric form of the primary/minimal-prime decomposition of its ideal, and it is the first structural theorem of variety theory. Each component, being irreducible, has a domain coordinate ring with a **function field** $\Omega(X) = \operatorname{Frac}(\Omega[X])$; the **dimension** of the component is the transcendence degree of its function field. The study of how components meet, and of generic versus special behaviour, is organised by the **generic point** of each component — the non-closed point of $\operatorname{Spec} \Omega[X]$ corresponding to the minimal prime.

> [!tip] Irreducible = prime, and Spec of a domain *(from Algebraic Geometry)*
> The equivalence "irreducible $\iff$ prime ideal $\iff$ domain coordinate ring" generalises verbatim to schemes: a scheme $\operatorname{Spec} A$ is irreducible iff $A$ has a unique minimal prime, and **integral** (reduced and irreducible) iff $A$ is a domain. The points of $\operatorname{Spec} A$ are themselves organised by irreducibility — each point $\mathfrak p$ has an irreducible closure $V(\mathfrak p)$, of which $\mathfrak p$ is the **generic point**. The classical "irreducible variety" is the closed-point-set of an integral affine scheme.
