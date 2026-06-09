---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Primary Ideal"
  - "Def - Irreducible Ideal"
  - "Def - Noetherian Ring"
  - "Def - Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Thm - Irreducible Ideals are Primary"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]] and $I \subsetneq R$ a proper [[Def - Ideal|ideal]]. A [[Def - Primary Ideal|primary decomposition]] of $I$ is an expression $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ with each $\mathfrak{q}_i$ primary; it is **minimal** if the radicals $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ are distinct and no $\mathfrak{q}_i$ contains $\bigcap_{j \neq i}\mathfrak{q}_j$. An [[Def - Irreducible Ideal|irreducible ideal]] is one not equal to an intersection of two strictly larger ideals. The full registry is on [[Commutative Algebra IX — Primary Decomposition]].

---

# Statement

> **Theorem (Lasker–Noether, existence).** Let $R$ be a Noetherian ring. Then every proper ideal $I \subsetneq R$ is a finite intersection of [[Def - Primary Ideal|primary ideals]],
> $$I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n,$$
> and hence admits a **minimal** primary decomposition (one in which the radicals $\sqrt{\mathfrak{q}_i}$ are distinct and no component is redundant).

> **Corollary (existence of irreducible decompositions).** In a Noetherian ring, every proper ideal is a finite intersection of [[Def - Irreducible Ideal|irreducible ideals]].

The corollary is in fact the first half of the proof; the theorem follows by combining it with [[Thm - Irreducible Ideals are Primary|irreducible ⇒ primary]] and then refining to a minimal decomposition.

---

# Motivation

This is the theorem that makes the whole chapter possible: it guarantees that the objects the uniqueness theorems analyse actually exist. Without it, "the primary decomposition of $I$" would be an empty phrase for most ideals. The result is named for Emanuel Lasker (the chess world champion, who proved it for polynomial rings) and Emmy Noether (who recast it in the abstract form here, isolating the ascending chain condition as the one hypothesis that matters).

Its role is to extend integer factorisation to all of commutative algebra. In $\mathbb{Z}$, the fundamental theorem of arithmetic says every integer factors into prime powers; rewritten in ideals, $(n) = \bigcap (p_i^{a_i})$. Lasker–Noether is the assertion that the *intersection-into-primary-pieces* part of this survives in every Noetherian ring — you may always break an ideal into primary components. What does *not* survive is uniqueness of the pieces; that is the subject of the later theorems. So this theorem is the existence half of "primary decomposition is the right generalisation of prime factorisation", and it is deliberately separated from uniqueness because the two halves have completely different proofs and different hypotheses: existence needs Noetherianity (to run an induction on ideals), uniqueness needs only that *a* decomposition exists (a property of the single ideal $I$).

The hypothesis is exactly right and cannot be dropped. In a non-Noetherian ring, existence can fail: the ring $C[0,1]$ of continuous functions on the interval has a zero ideal with infinitely many minimal primes, so $(0)$ is not a finite intersection of primary ideals there. The theorem is precisely the statement that *finiteness of the decomposition* is bought by the ascending chain condition.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$R$ is Noetherian", and the skill is recognising the many guises in which Noetherianity arrives.

The first disguised source is **$R$ is a finitely generated algebra over a field (or over $\mathbb{Z}$)**. The property $B$ is "$R = k[X_1, \dots, X_n]/J$". By [[Thm - Hilbert's Basis Theorem|Hilbert's Basis Theorem]], $k[X_1, \dots, X_n]$ is Noetherian, and quotients of Noetherian rings are Noetherian, so $R$ is Noetherian and every ideal has a primary decomposition. The non-obvious value: the coordinate ring of *any* affine variety satisfies the theorem, so every system of polynomial equations has its solution-ideal decomposable into primary pieces — the algebraic engine behind "every algebraic set has finitely many irreducible components". *Example problem:* decompose the ideal of a reducible plane curve into the ideals of its branches plus embedded structure.

The second disguised source is **$R$ is a localization or completion of a Noetherian ring**. The property $B$ is "$R = S^{-1}A$ or $R = \hat A$ for $A$ Noetherian". Localizations of Noetherian rings are Noetherian, and (a harder theorem) so are completions; hence the local and complete-local rings at a point of a variety also enjoy primary decomposition. The non-obviousness: passing to a neighbourhood of a point preserves the existence of decompositions, which is what lets one study a component "locally". *Example problem:* decompose an ideal in the local ring at the origin of a singular curve.

The third disguised source is **$R$ is Artinian, or finite-dimensional as a vector space**. The property $B$ is "$R$ has the descending chain condition" or "$\dim_k R < \infty$". Artinian rings are Noetherian (indeed they are finite products of Artinian local rings), so primary decomposition exists — and is especially rigid, since every prime is maximal and there are no embedded primes among nonzero structure. *Example problem:* decompose $(0)$ in $k[X]/(f)$ for a polynomial $f$ with repeated roots, recovering the multiplicities.

**Targets (Output Amplification)**

The conclusion is "$I = \bigcap \mathfrak{q}_i$, a finite intersection of primary ideals".

Combine the decomposition with **taking radicals**. Since $\sqrt{\bigcap \mathfrak{q}_i} = \bigcap \sqrt{\mathfrak{q}_i} = \bigcap \mathfrak{p}_i$, the existence of the decomposition immediately gives $\sqrt I = \bigcap \mathfrak{p}_i$, a *finite* intersection of primes. The further result $E$: every radical ideal in a Noetherian ring is a finite intersection of primes, hence $V(I)$ has finitely many irreducible components. This is nonobvious because it converts an existence theorem about primary ideals into a finiteness theorem about the geometry — the components are finite precisely because the decomposition is.

Combine the decomposition with **the First Uniqueness Theorem**. Once a decomposition exists, $\operatorname{Ass}(I) = \{\sqrt{\mathfrak{q}_i}\}$ is well-defined and computable via colon ideals. The further result $E$: $I$ acquires a canonical finite invariant, its associated primes, which control the zero-divisors of $R/I$ and the embedded structure. This is nonobvious because the theorem only produces *a* (non-unique) decomposition, yet that suffices to extract a *unique* invariant.

Combine the decomposition with **localization at an isolated prime**. For a minimal prime $\mathfrak{p}_i$ over $I$, the component $\mathfrak{q}_i$ is the contraction of $IR_{\mathfrak{p}_i}$ and hence canonical. The further result $E$: the *isolated* part of the decomposition is unique (Second Uniqueness), so existence plus localization pins down the multiplicities along each irreducible component. This is nonobvious because existence alone gives no uniqueness; the canonicalisation comes from feeding the decomposition into the localization machinery.

---

# Why Is It True

The theorem is true for a reason that has almost nothing to do with rings and almost everything to do with the ascending chain condition. **The whole proof is "you cannot keep splitting forever in a Noetherian ring, and what you cannot split is already primary."**

Think about what could go wrong. We want to write $I$ as a finite intersection of nice pieces. The natural greedy strategy is: if $I$ is not already a nice piece, it splits as $I = J_1 \cap J_2$ with $J_1, J_2$ both strictly bigger; recurse on each. This produces a tree of ever-larger ideals. The *only* danger is that the recursion never terminates — that you keep finding strictly larger ideals forever, building an infinite ascending chain. But that is exactly what the [[Def - Noetherian Ring|Noetherian]] condition forbids: every ascending chain of ideals stabilises. So the recursion must terminate, and when it terminates, every leaf is a piece that *cannot* be split — an [[Def - Irreducible Ideal|irreducible ideal]]. That is the existence of an irreducible decomposition, and it used nothing but the chain condition.

The second, genuinely ring-theoretic, idea is that the indivisible pieces are good enough: **an irreducible ideal is automatically primary** ([[Thm - Irreducible Ideals are Primary]]). This is where the ring structure finally enters, through an argument about the chain of annihilators $\operatorname{Ann}(\bar y) \subseteq \operatorname{Ann}(\bar y^2) \subseteq \cdots$ in $R/I$ stabilising. So the irreducible pieces are primary pieces, and we have a primary decomposition.

The last step, refinement to a minimal decomposition, is cosmetic and uses one clean fact: a finite intersection of $\mathfrak{p}$-primary ideals (same prime $\mathfrak{p}$) is again $\mathfrak{p}$-primary. So you may merge any components that share a radical, collapsing the list until all radicals are distinct, and then throw away any component that already contains the intersection of the others. Nothing deep happens here; it is bookkeeping to make the decomposition canonical-looking.

The division of labour is the thing to remember: **finiteness comes from the chain condition (a property of the lattice of ideals), and the pieces are good because irreducible implies primary (a property of the ring).** Strip the ring away and you still get a finite meet-irreducible decomposition; that is why the existence half is so robust and the uniqueness half, which needs the prime structure, is so delicate.

---

# What Makes This Hard

The conceptual hurdle is realising the proof is in two completely separate halves — a soft order-theoretic induction (every ideal is a finite intersection of irreducibles) and a hard ring-theoretic lemma (irreducible $\Rightarrow$ primary) — and that *only the first half uses Noetherianity*. The most common error is to try to decompose directly into primary ideals by induction, which does not work because "primary" is not a lattice property and gives no clean inductive step; you must route through irreducibles. The second subtlety is the maximal-counterexample setup: one argues by contradiction on the set of ideals that fail, invoking the ascending chain condition to extract a maximal failing element, and it is easy to mis-state which set is being maximised over.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove existence of an irreducible decomposition by Noetherian induction (maximal counterexample). Invoke "irreducible $\Rightarrow$ primary" to upgrade it to a primary decomposition. Refine to minimal by merging equal-radical components and deleting redundant ones.

**Subgoal decomposition:**

1. **Every ideal is a finite intersection of irreducibles.** Show: the set $\Sigma$ of ideals that are *not* finite intersections of irreducible ideals is empty.
   - *Hint:* If $\Sigma \neq \varnothing$, the ascending chain condition gives a maximal element $I \in \Sigma$. $I$ is not irreducible (else $I = I$ is its own decomposition), so $I = J_1 \cap J_2$ with $J_1, J_2 \supsetneq I$. By maximality $J_1, J_2 \notin \Sigma$, so each is a finite intersection of irreducibles, hence so is $I$ — contradiction.
   - *Why needed:* It is the existence engine and the only step using Noetherianity.

2. **Upgrade to primary.** Replace each irreducible component by the fact that it is primary.
   - *Hint:* Apply [[Thm - Irreducible Ideals are Primary]] to each irreducible component; the intersection is now a primary decomposition.
   - *Why needed:* It is what makes the pieces *primary* rather than merely irreducible.

3. **Refine to minimal.** Make the radicals distinct and delete redundancies.
   - *Hint:* Group components by radical and merge each group using "a finite intersection of $\mathfrak{p}$-primary ideals is $\mathfrak{p}$-primary"; then drop any $\mathfrak{q}_i \supseteq \bigcap_{j\neq i}\mathfrak{q}_j$.
   - *Why needed:* It produces the *minimal* decomposition the uniqueness theorems require.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every ideal in a Noetherian ring is a finite intersection of irreducible ideals
> **Statement:** If $R$ is Noetherian, every proper ideal $I$ is a finite intersection of irreducible ideals.
>
> **Hint:** Maximal counterexample: if the set of ideals lacking such a decomposition is nonempty, the ascending chain condition gives it a maximal element, which must split and contradict maximality.
>
> **Why needed:** It is the existence backbone; everything else upgrades or refines its output.
>
> > [!note]- Full proof
> > Let $\Sigma = \{\text{proper ideals } J : J \text{ is not a finite intersection of irreducible ideals}\}$. Suppose $\Sigma \neq \varnothing$. Since $R$ is [[Def - Noetherian Ring|Noetherian]], every nonempty set of ideals has a maximal element (otherwise one could build a strictly ascending chain), so $\Sigma$ has a maximal element $I$.
> >
> > Now $I$ is not irreducible: if it were, then $I$ would be the (length-one) intersection of irreducibles, so $I \notin \Sigma$. Being reducible, $I = J_1 \cap J_2$ with $J_1, J_2$ ideals strictly containing $I$. By maximality of $I$ in $\Sigma$, neither $J_1$ nor $J_2$ lies in $\Sigma$ (each strictly contains $I$), so each *is* a finite intersection of irreducible ideals, say $J_1 = \bigcap_a \mathfrak{r}_a$ and $J_2 = \bigcap_b \mathfrak{r}_b'$. Then $I = J_1 \cap J_2 = \bigcap_a \mathfrak{r}_a \cap \bigcap_b \mathfrak{r}_b'$ is a finite intersection of irreducibles, so $I \notin \Sigma$ — contradicting $I \in \Sigma$. Hence $\Sigma = \varnothing$.

> [!note]- Lemma 2: A finite intersection of $\mathfrak{p}$-primary ideals is $\mathfrak{p}$-primary
> **Statement:** If $\mathfrak{q}_1, \dots, \mathfrak{q}_m$ are all $\mathfrak{p}$-primary (same prime $\mathfrak{p}$), then $\mathfrak{q} = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_m$ is $\mathfrak{p}$-primary.
>
> **Hint:** Compute $\sqrt{\mathfrak{q}} = \bigcap \sqrt{\mathfrak{q}_i} = \mathfrak{p}$, then check the primary condition directly using that each $\mathfrak{q}_i$ is primary.
>
> **Why needed:** It lets you merge components sharing a radical, which is the refinement to distinct radicals.
>
> > [!note]- Full proof
> > First, $\sqrt{\mathfrak{q}} = \sqrt{\bigcap_i \mathfrak{q}_i} = \bigcap_i \sqrt{\mathfrak{q}_i} = \bigcap_i \mathfrak{p} = \mathfrak{p}$. Also $\mathfrak{q} \neq R$ (each $\mathfrak{q}_i \neq R$). For the primary condition, suppose $xy \in \mathfrak{q}$ and $y \notin \sqrt{\mathfrak{q}} = \mathfrak{p}$. Then for each $i$, $xy \in \mathfrak{q}_i$ and $y \notin \mathfrak{p} = \sqrt{\mathfrak{q}_i}$; since $\mathfrak{q}_i$ is primary, $x \in \mathfrak{q}_i$. As this holds for all $i$, $x \in \bigcap_i \mathfrak{q}_i = \mathfrak{q}$. Hence $\mathfrak{q}$ is primary, and with $\sqrt{\mathfrak{q}} = \mathfrak{p}$ it is $\mathfrak{p}$-primary.

> [!note]- Lemma 3: Redundant components can be deleted to reach minimality
> **Statement:** From any primary decomposition with distinct radicals one obtains a minimal one by deleting components that contain the intersection of the others.
>
> **Hint:** If $\mathfrak{q}_i \supseteq \bigcap_{j \neq i}\mathfrak{q}_j$ then $\bigcap_j \mathfrak{q}_j = \bigcap_{j \neq i}\mathfrak{q}_j$, so $\mathfrak{q}_i$ may be dropped without changing the intersection.
>
> **Why needed:** It enforces the "no redundant component" half of minimality.
>
> > [!note]- Full proof
> > Suppose, after merging same-radical components via Lemma 2, the radicals $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ are distinct. If some $\mathfrak{q}_i \supseteq \bigcap_{j \neq i}\mathfrak{q}_j$, then $\bigcap_j \mathfrak{q}_j = \mathfrak{q}_i \cap \bigcap_{j\neq i}\mathfrak{q}_j = \bigcap_{j\neq i}\mathfrak{q}_j$, so deleting $\mathfrak{q}_i$ leaves the intersection (and hence $I$) unchanged, and the radicals remain distinct. Repeat until no component contains the intersection of the rest; since there are finitely many components the process terminates, yielding a minimal primary decomposition.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian and $I \subsetneq R$.
>
> ---
> **Step 1 — irreducible decomposition.** By Lemma 1, $I = \mathfrak{r}_1 \cap \cdots \cap \mathfrak{r}_n$ for finitely many [[Def - Irreducible Ideal|irreducible ideals]] $\mathfrak{r}_k$ (each proper, since $I$ is proper and a proper ideal is an intersection of proper ones).
>
> ---
> **Step 2 — primary decomposition.** By [[Thm - Irreducible Ideals are Primary|the theorem that irreducible ideals are primary]] (valid in any Noetherian ring), each $\mathfrak{r}_k$ is a [[Def - Primary Ideal|primary ideal]]. Hence $I = \mathfrak{r}_1 \cap \cdots \cap \mathfrak{r}_n$ is a primary decomposition of $I$.
>
> ---
> **Step 3 — minimality.** Group the components $\mathfrak{r}_k$ by their radicals. For each distinct prime $\mathfrak{p}$ appearing among $\{\sqrt{\mathfrak{r}_k}\}$, intersect all the $\mathfrak{r}_k$ with $\sqrt{\mathfrak{r}_k} = \mathfrak{p}$ into a single ideal $\mathfrak{q}_{\mathfrak{p}}$; by Lemma 2 this $\mathfrak{q}_{\mathfrak{p}}$ is $\mathfrak{p}$-primary. Now $I = \bigcap_{\mathfrak{p}} \mathfrak{q}_{\mathfrak{p}}$ has distinct radicals. Finally apply Lemma 3 to delete any component containing the intersection of the others. The result is a minimal primary decomposition of $I$. $\blacksquare$
>
> ---
> **Remark on the hypothesis.** Noetherianity is used only in Step 1 (and inside Step 2's lemma). Without it, existence can fail: in $C[0,1]$ the ideal $(0)$ has infinitely many minimal primes and is not a finite intersection of primary ideals.

---

# Cross-Field Exercise Suggestions

**Solving polynomial systems and counting components.** Given a system of polynomial equations over an algebraically closed field, the solution set is $V(I)$ for $I = (f_1, \dots, f_r)$, and Lasker–Noether (via Hilbert's Basis Theorem making $k[X_1, \dots, X_n]$ Noetherian) guarantees $I = \bigcap \mathfrak{q}_i$ with finitely many components. The irreducible components of the solution set are the $V(\mathfrak{p}_i)$ for isolated $\mathfrak{p}_i$. The nonobvious recognition: a finiteness theorem about *solutions of equations* is an existence theorem about *primary decomposition* — there are only finitely many "kinds" of solution because the decomposition is finite.

**Module decomposition over a PID and the structure theorem.** For a finitely generated module $M$ over a [[Def - Principal Ideal Domain|PID]], the primary decomposition of the zero submodule recovers the primary cyclic factors $R/(p_i^{a_i})$ of the structure theorem. Each $(p_i^{a_i})$ is a $\mathfrak{p}_i$-primary ideal, and the decomposition $(0) = \bigcap \ker(M \to M/p_i^{a_i}M)$ is the module-level Lasker–Noether. The nonobvious link: the elementary-divisor form of the structure theorem *is* a primary decomposition, with no embedded primes because a PID is one-dimensional.

**Intersection multiplicities in Bézout's theorem.** When two plane curves $f = 0$ and $g = 0$ meet, the intersection ideal $(f, g) \subseteq k[X,Y]$ has a primary decomposition whose components, localized at each intersection point, encode the *intersection multiplicity* there. Lasker–Noether guarantees finitely many such points-with-multiplicity, and Bézout's theorem counts them as $\deg f \cdot \deg g$. The nonobvious application: the multiplicities that make Bézout's count exact live in the primary components, and their existence is the existence of the decomposition.

---

# Bridges

- **[[Thm - Irreducible Ideals are Primary|Irreducible Ideals are Primary]]** — the ring-theoretic half of this theorem's proof. The existence theorem is *exactly* "finite intersection of irreducibles (chain condition) $+$ irreducible is primary (ring structure)". The irreducible-decomposition step is soft and order-theoretic; this companion theorem supplies the only genuinely ring-theoretic input, converting indivisible pieces into arithmetically meaningful primary ones. Read the two together: this one provides the *finiteness*, that one provides the *quality* of the pieces.

- **[[Thm - Minimal Primes are Finite in a Noetherian Ring|Minimal Primes are Finite]]** — the radical-ideal specialisation. Taking radicals of a primary decomposition, $\sqrt I = \bigcap \mathfrak{p}_i$, shows a radical ideal is a finite intersection of primes; the minimal-primes theorem proves this directly by the same maximal-counterexample induction, without needing the full primary decomposition. The two are different routes to the same finiteness — one via the whole decomposition, one via a leaner argument tailored to radical ideals.

- **[[Thm - Hilbert's Basis Theorem|Hilbert's Basis Theorem]]** — the source of the hypothesis in practice. It is what makes $k[X_1, \dots, X_n]$ (and every finitely generated algebra, and every coordinate ring) Noetherian, so it is the theorem that delivers Lasker–Noether to algebraic geometry. Without Hilbert's Basis Theorem the existence theorem would have almost no geometric applications, since the rings of interest are exactly the finitely generated algebras.

- **[[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]]** — the natural sequel. Existence produces a (non-unique) decomposition; the First Uniqueness Theorem extracts from it the canonical invariant $\operatorname{Ass}(I)$. Existence and uniqueness are deliberately separated because they need different hypotheses — existence needs Noetherianity, uniqueness needs only that a decomposition exists.

---

# Unlocked by This

> [!tip] Finiteness of irreducible components *(from Algebraic Geometry)*
> Over a field, Lasker–Noether (through Hilbert's Basis Theorem) is the statement that **every algebraic set has finitely many irreducible components**. Taking radicals of $I = \bigcap \mathfrak{q}_i$ gives $\sqrt I = \bigcap \mathfrak{p}_i$, and $V(I) = \bigcup V(\mathfrak{p}_i)$ exhibits the finitely many components $V(\mathfrak{p}_i)$. This is the foundational finiteness theorem of the subject: the very notion of "the components of a variety" depends on this decomposition existing and being finite.

> [!tip] Noetherian schemes and the decomposition of a scheme *(from Algebraic Geometry)*
> Globalised, the theorem says a **Noetherian scheme has finitely many irreducible components**, and primary decomposition becomes the decomposition of a closed subscheme into its components-with-multiplicity together with its embedded points. The Noetherian hypothesis is the scheme-theoretic finiteness condition that guarantees this, and it is exactly the condition under which the local rings $\mathcal{O}_{X,x}$ are Noetherian so that primary decomposition is available at every point.
