---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ideal"
  - "Def - Primary Ideal"
  - "Def - Noetherian Ring"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring and $I \subsetneq R$ a proper [[Def - Ideal|ideal]]. We write $J_1 \cap J_2$ for the intersection of two ideals (itself an ideal), and "$J$ strictly larger than $I$" means $I \subsetneq J$. A [[Def - Noetherian Ring|Noetherian ring]] is one in which every ascending chain of ideals stabilises. The full symbol registry is on [[Commutative Algebra IX — Primary Decomposition]].

A warning on a clash of names: an **irreducible *element*** of a ring (one that does not factor into two non-units) is a different notion from an **irreducible *ideal*** defined here (one that is not an intersection of two strictly larger ideals). This page is about ideals.

---

# Axiom Motivation

The goal is to find the **building blocks for an existence proof**. We want to show that every ideal of a [[Def - Noetherian Ring|Noetherian ring]] has a [[Def - Primary Ideal|primary decomposition]], and the cleanest existence arguments proceed by breaking an object into indivisible pieces and then identifying those pieces. The notion of "indivisible" appropriate to a decomposition by *intersection* is exactly what this page defines — an ideal that cannot be written as an intersection of two strictly larger ideals. The strategy of the whole existence theorem is then two moves: first, decompose any ideal into these indivisible pieces (a purely order-theoretic fact, true in any Noetherian ring); second, prove that each indivisible piece is already primary (a ring-theoretic fact). Irreducible ideals are the hinge between the two.

**Why "intersection" is the right operation to be indivisible against.** A primary decomposition writes $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ — an *intersection*. So the relevant notion of an atom is one that resists being split as an intersection. An ideal $I$ is **irreducible** if whenever $I = J_1 \cap J_2$ then $I = J_1$ or $I = J_2$; equivalently, $I$ is not the intersection of two ideals strictly larger than itself. (Strictly larger is the right phrasing: $I = I \cap R$ always, so without "strictly" every ideal would be reducible trivially.) This is precisely "meet-irreducible" in the lattice of ideals. The reason to use *this* operation rather than, say, products is that intersection is what appears in the target theorem, and intersection of ideals is well-behaved (always an ideal, order-reversing in a controlled way) in a manner that products are not.

**Why irreducibility, not primariness, is the easy thing to prove exists.** One might ask: why not decompose directly into primary ideals and skip irreducible ideals entirely? Because *existence* of a decomposition into irreducibles is nearly free — it is a consequence of the ascending chain condition alone, by a maximal-counterexample argument that uses no ring structure beyond the lattice of ideals. The argument: if some ideal failed to be a finite intersection of irreducibles, the [[Def - Noetherian Ring|Noetherian]] condition would give a *maximal* such failing ideal $I$; this $I$ cannot itself be irreducible (or it would be its own trivial decomposition), so $I = J_1 \cap J_2$ with both strictly larger; but then $J_1, J_2$ are not failing (by maximality of $I$), so each *is* a finite intersection of irreducibles, and so is $I = J_1 \cap J_2$ — contradiction. This argument is robust precisely because it asks nothing of the pieces except that they be irreducible. Asking directly for primary pieces would not give such a clean induction, because "primary" is not a lattice property. So irreducibility is the order-theoretic stepping stone, and the genuine ring theory is quarantined into the single lemma "irreducible $\Rightarrow$ primary".

**Why irreducible must be strictly stronger than primary, and why that is acceptable.** The bridge lemma [[Thm - Irreducible Ideals are Primary|irreducible $\Rightarrow$ primary]] goes only one way, and it must: there are primary ideals that are reducible. The standard witness is $(X,Y)^2 = (X^2, XY, Y^2) \subseteq k[X,Y]$, which is $(X,Y)$-primary yet splits as $(X^2, Y) \cap (X, Y^2)$ — an intersection of two strictly larger ideals. This is not a defect. For the existence proof we only need *irreducible $\Rightarrow$ primary*; the reverse would say irreducible pieces are the finest possible, which is false and unnecessary. The takeaway is that irreducible ideals are a *sufficient* supply of primary ideals — every ideal is a finite intersection of irreducibles, and irreducibles are primary, so every ideal is a finite intersection of primaries — without irreducibles being the *only* primary ideals. Decompositions into irreducibles are typically finer than minimal primary decompositions, which is exactly why one passes from "intersection of irreducibles" to "minimal primary decomposition" by grouping same-radical components afterward.

**Why properness is required.** We insist $I \subsetneq R$. The whole ring $R$ is the empty intersection and behaves as a unit for $\cap$; declaring it irreducible or not is a convention, and excluding it (as we do for primary ideals too) keeps the statements clean — "every *proper* ideal is a finite intersection of irreducible *proper* ideals". This matches the convention that $R$ is neither prime nor primary.

---

# The Definition

Let $R$ be a commutative ring and $I \subsetneq R$ a proper ideal.

$I$ is **irreducible** if it is not the intersection of two strictly larger ideals: whenever
$$I = J_1 \cap J_2 \quad\text{with } J_1, J_2 \text{ ideals of } R, \qquad\text{then}\qquad I = J_1 \ \text{ or }\ I = J_2.$$
Equivalently, $I \neq J_1 \cap J_2$ for any pair of ideals $J_1, J_2$ both strictly containing $I$.

This is the **meet-irreducible** condition in the lattice of ideals of $R$ (ordered by inclusion, with meet $=$ intersection).

---

# Categorical / Structural Definition

The structural reading is purely **lattice-theoretic**, and this is what makes the existence half of primary decomposition so general. In the lattice $(\mathcal{I}(R), \subseteq)$ of ideals of $R$, with meet $\wedge = \cap$ and join $\vee = +$, an element $I$ is **meet-irreducible** if $I = a \wedge b \Rightarrow I = a$ or $I = b$. The statement "every element of a lattice with the ascending chain condition is a finite meet of meet-irreducible elements" is a theorem about lattices, proved by the maximal-counterexample induction described above, and it specialises to "every ideal of a Noetherian ring is a finite intersection of irreducible ideals". What the ring structure adds, on top of the lattice, is the identification of these abstract meet-irreducibles with the arithmetically meaningful primary ideals (via [[Thm - Irreducible Ideals are Primary]]). So the definition lives at the lattice level, and the ring is needed only to give the irreducible pieces their prime-and-multiplicity interpretation. This is the precise sense in which Lasker–Noether existence is "really" a fact about Noetherian lattices wearing a ring-theoretic costume.

---

# Relate to Other Fields / Compression

The cleanest compression: **an irreducible ideal is a meet-atom — an ideal you cannot split as an intersection of two bigger ideals — and irreducibility is strictly stronger than primariness, finer than what the final decomposition needs.**

**True name:** the true name of "irreducible" is **"meet-irreducible in the ideal lattice"** — the operational test is "can I write $I$ as $J_1 \cap J_2$ with both $J_i \supsetneq I$? If not, it is irreducible." This is the form used in the existence proof: you never check irreducibility positively; you use it negatively, in the contrapositive — *if $I$ is not irreducible, split it* — which is exactly the inductive step. The role of the concept is entirely as the engine of a maximal-counterexample induction.

The notion is the order-dual of **join-irreducible** (an element not expressible as a join of two smaller elements), and the decomposition theorem is the meet-version of the more familiar "every element is a join of join-irreducibles" from the theory of distributive and modular lattices. In a Boolean algebra the meet-irreducibles are the co-atoms; in the divisor lattice of an integer the meet-irreducibles are the prime powers — which is the lattice-theoretic shadow of "primary ideals are the pieces of $(n)$". Beware the unrelated clash with **irreducible element** of a ring (the factorisation notion) and with **irreducible topological space / variety** (a space not a union of two proper closed subsets) — though the last is genuinely related, since $V(\mathfrak{p})$ is an irreducible *space* exactly when $\mathfrak{p}$ is prime.

---

# Examples / Corollaries

**Is an instance — every prime ideal is irreducible.** If $\mathfrak{p}$ is prime and $\mathfrak{p} = J_1 \cap J_2$ with $J_1, J_2 \supsetneq \mathfrak{p}$, pick $a \in J_1 \setminus \mathfrak{p}$ and $b \in J_2 \setminus \mathfrak{p}$; then $ab \in J_1 \cap J_2 = \mathfrak{p}$, contradicting primality. So primes are irreducible — consistent with the chain "prime $\Rightarrow$ irreducible $\Rightarrow$ primary".

**Is an instance — $(X, Y^2)$ in $k[X,Y]$.** This $(X,Y)$-primary ideal is irreducible: $R/(X,Y^2) \cong k[Y]/(Y^2)$ has a unique minimal nonzero ideal $(\bar Y)$, so $(0)$ is irreducible in the quotient, hence $(X,Y^2)$ is irreducible in $R$. (The general principle: $I$ is irreducible iff $(0)$ is irreducible in $R/I$ iff the socle of $R/I$ is "one-dimensional" at the relevant prime.)

**Is an instance — $\mathfrak{m}^n$ in a discrete valuation ring.** In a [[Def - Principal Ideal Domain|PID]] localized at a prime, every ideal is $\mathfrak{m}^n = (\pi^n)$, and these are totally ordered by inclusion. A totally ordered set has *no* nontrivial meets ($J_1 \cap J_2$ is just the smaller of the two), so every $\mathfrak{m}^n$ is irreducible. This is why in dimension one (and more generally in Dedekind domains) irreducible, primary, and prime-power all coincide.

**Is NOT an instance — $(X,Y)^2$ in $k[X,Y]$.** The ideal $(X,Y)^2 = (X^2, XY, Y^2)$ is $(X,Y)$-primary but **reducible**: $(X,Y)^2 = (X^2, Y) \cap (X, Y^2)$, and both $(X^2, Y)$ and $(X, Y^2)$ strictly contain $(X,Y)^2$ (e.g. $Y \in (X^2, Y) \setminus (X,Y)^2$ and $X \in (X, Y^2) \setminus (X,Y)^2$). One checks the intersection equals $(X,Y)^2$ directly. This is the standard witness that primary does *not* imply irreducible.

**Is NOT an instance — a radical ideal with two minimal primes.** $(XY) \subseteq k[X,Y]$ equals $(X) \cap (Y)$, an intersection of two strictly larger ideals, so it is reducible. (It is also not primary: $X \cdot Y \in (XY)$ with $X \notin (XY)$ and $Y \notin \sqrt{(XY)} = (XY)$.) Any ideal with two distinct minimal primes is reducible, since it splits along them.

**Calibration check.** Verify that $(X,Y)^2 = (X^2, Y) \cap (X, Y^2)$ by a generator chase (an element of the right side is a polynomial divisible by $Y$ modulo $X^2$ and by $X$ modulo $Y^2$; deduce it lies in $(X,Y)^2$). Confirm that every prime ideal is irreducible directly from the prime condition. Finally, convince yourself of the master principle: $I$ is irreducible in $R$ if and only if the zero ideal is irreducible in $R/I$ — so irreducibility, like primariness, is a property of the quotient ring.

---

# Unlocked by This

> [!tip] Existence of primary decomposition *(within this chapter)*
> Irreducible ideals are the engine of the [[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether existence theorem]]. The two-step proof — every ideal is a finite intersection of irreducibles (Noetherian induction), every irreducible ideal is primary ([[Thm - Irreducible Ideals are Primary]]) — delivers existence of primary decompositions in every Noetherian ring. The notion exists almost entirely to make this proof work.

> [!tip] Meet-irreducible elements and lattice decomposition *(from Lattice Theory / Order Theory)*
> The decomposition "every ideal is a finite intersection of irreducibles" is the ring-theoretic face of a general theorem: in any lattice satisfying the ascending chain condition, every element is a finite meet of **meet-irreducible** elements. This is the dual of the join-irreducible decompositions central to the structure theory of distributive and modular lattices, and it is the reason the *existence* half of primary decomposition needs only the chain condition while the *uniqueness* half needs the full prime structure of the ring.
