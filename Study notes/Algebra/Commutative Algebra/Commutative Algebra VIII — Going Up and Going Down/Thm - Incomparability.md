---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - The Induced Map on Spectra"
  - "Def - Prime and Maximal Ideal"
  - "Def - Local Ring and Residue Field"
  - "Thm - Integral Extensions and Fields (Domain Criterion)"
  - "Thm - Lying Over"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be an [[Def - Integral Element and Integral Extension|integral extension]], [[Def - The Induced Map on Spectra|$\iota^*$]] the contraction $\mathfrak{q} \mapsto \mathfrak{q} \cap A$. For $\mathfrak{p} \in \operatorname{Spec} A$, $B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$, and the **fibre** over $\mathfrak{p}$ is the set of primes of $B$ lying over $\mathfrak{p}$, identified with $\operatorname{mSpec} B_{\mathfrak{p}}$. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

---

# Statement

> **Theorem (Incomparability).** Let $A \subseteq B$ be an integral extension of rings, and let $\mathfrak{q} \subseteq \mathfrak{q}'$ be primes of $B$ with $\mathfrak{q} \cap A = \mathfrak{q}' \cap A$. Then $\mathfrak{q} = \mathfrak{q}'$.

> **Equivalent forms.** (i) No two distinct comparable primes of $B$ lie over the same prime of $A$ — each fibre $(\iota^*)^{-1}(\mathfrak{p})$ is an *antichain*. (ii) For each $\mathfrak{p}$, the fibre ring $B \otimes_A \kappa(\mathfrak{p})$ has Krull dimension $0$. (iii) If $B$ is module-finite over $A$, each fibre is *finite*.

The name records the conclusion: primes in one fibre are pairwise *incomparable* under inclusion.

---

# Motivation

Lying over and going up describe how the contraction map $\iota^*$ moves *between* fibres. Incomparability describes what happens *within* a single fibre, and the answer is: nothing — the fibre has no internal vertical structure. Two primes of $B$ over the same prime of $A$ can never be nested; the fibre is a flat antichain of points, not a chain. Geometrically this is the statement that the fibres of an integral (finite) map are *zero-dimensional*: above each point of the base sit finitely many isolated points, with no positive-dimensional structure and no specialisation among them.

This is the theorem that bounds dimension from *above*. If you take a strict chain $\mathfrak{q}_0 \subsetneq \mathfrak{q}_1 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ in $B$ and contract it, you get a chain $\mathfrak{q}_0 \cap A \subseteq \cdots \subseteq \mathfrak{q}_n \cap A$ in $A$. For a *general* ring map this contracted chain could collapse — two of the $\mathfrak{q}_i$ might share a contraction, shortening the chain. Incomparability forbids exactly this: $\mathfrak{q}_i \subsetneq \mathfrak{q}_{i+1}$ with the same contraction is impossible, so the contracted chain stays strict and has the same length $n$. Hence $\dim B \leq \dim A$. Without incomparability, the dimension inequality fails — and it does fail for non-integral maps, where $k \hookrightarrow k[X]$ contracts the strict chain $(0) \subsetneq (X)$ to the single prime $(0)$.

Why should the fibres be zero-dimensional? Because the fibre lives in $B_{\mathfrak{p}}$, where the base has been localized to the local ring $A_{\mathfrak{p}}$, and the primes of $B$ over $\mathfrak{p}$ are the *maximal* ideals of $B_{\mathfrak{p}}$. But two distinct maximal ideals are never comparable — one maximal ideal inside another forces equality. So the moment you know "the fibre is $\operatorname{mSpec} B_{\mathfrak{p}}$" (lying over's companion), incomparability is automatic: maximal ideals do not nest. The substance is the domain criterion that promotes "contracts to $\mathfrak{p}A_{\mathfrak{p}}$" to "is maximal", and after that the conclusion is the triviality "comparable maximal ideals coincide".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A \subseteq B$ integral, two primes over a common prime, one inside the other".

The first disguised source is **a chain in $B$ to be contracted**. When you contract a strict chain of $B$ to test $\dim B \leq \dim A$, the worry is collapse: do two consecutive primes share a contraction? Incomparability says no — consecutive distinct primes have distinct contractions. *Example problem:* proving $\dim B \leq \dim A$ for an integral extension.

The second disguised source is **a fibre whose size is in question**. Asking "how many primes lie over $\mathfrak{p}$?" is asking about the structure of the fibre; incomparability says they form an antichain, so (with module-finiteness) the fibre ring is Artinian and the fibre finite. *Example problem:* showing a finite map has finite fibres, or counting primes of $\mathbb{Z}[i]$ over $(p)$.

The third disguised source is **a prime over a maximal ideal**. If $\mathfrak{p}$ is maximal, every prime over it is maximal (domain criterion), and maximal ideals form an antichain trivially. Incomparability is then visible directly: the fibre over a maximal ideal is a set of maximal ideals. *Example problem:* the primes of $B$ over a maximal ideal of $A$ are all maximal and pairwise incomparable.

**Targets (Output Amplification)**

The conclusion is "comparable primes in one fibre coincide / fibres are antichains".

Combine incomparability with **contraction of a chain** to get $\dim B \leq \dim A$. A strict chain in $B$ contracts to a chain in $A$ that stays strict (no collapse), so chains upstairs are no longer than chains downstairs. The result $E$ is the upper bound in dimension preservation.

Combine incomparability with **module-finiteness** to get *finite* fibres. The fibre ring $B \otimes_A \kappa(\mathfrak{p})$ is finite-dimensional over the field $\kappa(\mathfrak{p})$, hence Artinian; an Artinian ring has finitely many primes, all maximal — and incomparability already told you the fibre is zero-dimensional, so "Artinian" upgrades "antichain" to "finite set". The result $E$ is finiteness of fibres of finite maps.

Combine incomparability with **[[Thm - Going Up|going up]]** to preserve chain *length* when lifting. Going up lifts a chain with $\subseteq$; incomparability guarantees the lifts are distinct (distinct contractions), so a strict chain lifts to a strict chain. The result $E$ is that lifting preserves length, the other half of dimension preservation.

---

# Why Is It True

The argument has two moves, and the first is the whole content. **Move one: localize at $\mathfrak{p} = \mathfrak{q} \cap A = \mathfrak{q}' \cap A$, where both $\mathfrak{q}$ and $\mathfrak{q}'$ become maximal ideals of $B_{\mathfrak{p}}$.** Why maximal? Because $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral, and both extended primes $\mathfrak{q}B_{\mathfrak{p}}, \mathfrak{q}'B_{\mathfrak{p}}$ contract to $\mathfrak{p}A_{\mathfrak{p}}$ — the *maximal* ideal of the local ring $A_{\mathfrak{p}}$ — so by the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain criterion]] (a prime of $B_{\mathfrak{p}}$ is maximal iff its contraction to $A_{\mathfrak{p}}$ is maximal), both are maximal in $B_{\mathfrak{p}}$. **Move two: comparable maximal ideals coincide.** Since $\mathfrak{q} \subseteq \mathfrak{q}'$, extension preserves the inclusion: $\mathfrak{q}B_{\mathfrak{p}} \subseteq \mathfrak{q}'B_{\mathfrak{p}}$. But $\mathfrak{q}B_{\mathfrak{p}}$ is maximal, hence not contained in any *strictly larger* proper ideal; and $\mathfrak{q}'B_{\mathfrak{p}}$ is proper. So $\mathfrak{q}B_{\mathfrak{p}} = \mathfrak{q}'B_{\mathfrak{p}}$. Contracting back (the localization correspondence is a bijection on primes disjoint from $A\setminus\mathfrak{p}$) gives $\mathfrak{q} = \mathfrak{q}'$.

**The mechanism in one line: after localizing at the common contraction, both primes are maximal ideals of the same ring, and one maximal ideal inside another are equal.** The reason localization is the right move is that it converts "contracts to $\mathfrak{p}$" into "is maximal" — and maximality is the property that makes nesting impossible. The domain criterion is the only non-trivial input; once you accept "contraction-to-$\mathfrak{p}$ becomes maximality after localizing", incomparability is the observation that maximal ideals form an antichain.

---

# What Makes This Hard

The conceptual hurdle is seeing that "lying over the same prime" should be converted to "maximal in the localization", because maximality is what forbids nesting — the naive approach tries to compare $\mathfrak{q}, \mathfrak{q}'$ directly in $B$, where there is no leverage. The non-obvious step is invoking the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]] to upgrade "contracts to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$" to "is itself maximal". The common error is to forget the localization and try to show $\mathfrak{q}, \mathfrak{q}'$ are maximal *in $B$* — which is false unless $\mathfrak{p}$ is maximal in $A$; the localization is essential precisely because it makes the *common contraction* maximal even when $\mathfrak{p}$ is not.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Localize at $\mathfrak{p} = \mathfrak{q} \cap A$. In $B_{\mathfrak{p}}$, both extended primes contract to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$, hence are maximal by the domain criterion; a maximal ideal contained in a proper ideal equals it, so the extensions coincide, and contracting back gives $\mathfrak{q} = \mathfrak{q}'$.

**Subgoal decomposition:**

1. **Localize: $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral, and $\mathfrak{q}B_{\mathfrak{p}}, \mathfrak{q}'B_{\mathfrak{p}}$ are primes of $B_{\mathfrak{p}}$ contracting to $\mathfrak{p}A_{\mathfrak{p}}$.**
   - *Hint:* Both $\mathfrak{q}, \mathfrak{q}'$ avoid $A \setminus \mathfrak{p}$ (as $\mathfrak{q} \cap A = \mathfrak{p}$), so they survive localization; their contractions to $A_{\mathfrak{p}}$ are $\mathfrak{p}A_{\mathfrak{p}}$.
   - *Why needed:* It moves the problem to a ring where the common contraction is *maximal*.

2. **Both $\mathfrak{q}B_{\mathfrak{p}}$ and $\mathfrak{q}'B_{\mathfrak{p}}$ are maximal in $B_{\mathfrak{p}}$.**
   - *Hint:* Domain criterion: for the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$, a prime is maximal iff its contraction is maximal; $\mathfrak{p}A_{\mathfrak{p}}$ is maximal.
   - *Why needed:* Maximality is what forbids strict containment.

3. **$\mathfrak{q}B_{\mathfrak{p}} = \mathfrak{q}'B_{\mathfrak{p}}$, hence $\mathfrak{q} = \mathfrak{q}'$.**
   - *Hint:* $\mathfrak{q} \subseteq \mathfrak{q}'$ extends to $\mathfrak{q}B_{\mathfrak{p}} \subseteq \mathfrak{q}'B_{\mathfrak{p}}$; a maximal ideal in a proper ideal is equal to it; contract back via the localization bijection.
   - *Why needed:* It delivers the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: After localizing, both primes contract to the maximal ideal of $A_{\mathfrak{p}}$
> **Statement:** With $\mathfrak{p} = \mathfrak{q} \cap A = \mathfrak{q}' \cap A$, the extended ideals $\mathfrak{q}B_{\mathfrak{p}}, \mathfrak{q}'B_{\mathfrak{p}}$ are primes of $B_{\mathfrak{p}}$ whose contractions to $A_{\mathfrak{p}}$ both equal $\mathfrak{p}A_{\mathfrak{p}}$.
>
> **Hint:** $\mathfrak{q} \cap (A \setminus \mathfrak{p}) = \varnothing$, so $\mathfrak{q}$ survives in $B_{\mathfrak{p}}$; localization commutes with contraction.
>
> **Why needed:** It produces the common *maximal* contraction needed for the domain criterion.
>
> > [!note]- Full proof
> > Since $\mathfrak{q} \cap A = \mathfrak{p}$, we have $\mathfrak{q} \cap (A \setminus \mathfrak{p}) = \varnothing$, so by the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]] for $B \to B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$, the extension $\mathfrak{q}B_{\mathfrak{p}}$ is a prime of $B_{\mathfrak{p}}$ contracting to $\mathfrak{q}$; likewise $\mathfrak{q}'B_{\mathfrak{p}}$. By the same theorem applied to $A \to A_{\mathfrak{p}}$, the contraction of $\mathfrak{q}B_{\mathfrak{p}}$ to $A_{\mathfrak{p}}$ is $(\mathfrak{q} \cap A)A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}$, the unique maximal ideal of the local ring $A_{\mathfrak{p}}$; identically for $\mathfrak{q}'B_{\mathfrak{p}}$.

> [!note]- Lemma 2: A prime of $B_{\mathfrak{p}}$ contracting to $\mathfrak{p}A_{\mathfrak{p}}$ is maximal
> **Statement:** For the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$, a prime $\mathfrak{n} \trianglelefteq B_{\mathfrak{p}}$ with $\mathfrak{n} \cap A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}$ is maximal.
>
> **Hint:** Domain criterion: $\mathfrak{n}$ maximal $\iff \mathfrak{n} \cap A_{\mathfrak{p}}$ maximal; $\mathfrak{p}A_{\mathfrak{p}}$ is maximal.
>
> **Why needed:** Maximality is the engine of the antichain conclusion.
>
> > [!note]- Full proof
> > The localized extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral (integrality passes to localizations). By the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]], for an integral extension a prime $\mathfrak{n}$ of $B_{\mathfrak{p}}$ is maximal if and only if its contraction $\mathfrak{n} \cap A_{\mathfrak{p}}$ is maximal in $A_{\mathfrak{p}}$. (This is because $A_{\mathfrak{p}}/(\mathfrak{n}\cap A_{\mathfrak{p}}) \hookrightarrow B_{\mathfrak{p}}/\mathfrak{n}$ is an integral extension of domains, and there one is a field iff the other is.) Since $\mathfrak{p}A_{\mathfrak{p}}$ is the maximal ideal of the local ring $A_{\mathfrak{p}}$, any $\mathfrak{n}$ contracting to it is maximal.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq B$ be integral and $\mathfrak{q} \subseteq \mathfrak{q}'$ primes of $B$ with $\mathfrak{q} \cap A = \mathfrak{q}' \cap A =: \mathfrak{p}$.
>
> **Step 1 — localize at $\mathfrak{p}$.** Set $B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$, $A_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}A$. By Lemma 1, $\mathfrak{q}B_{\mathfrak{p}}$ and $\mathfrak{q}'B_{\mathfrak{p}}$ are primes of $B_{\mathfrak{p}}$, both contracting to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$.
>
> **Step 2 — both extensions are maximal.** By Lemma 2, $\mathfrak{q}B_{\mathfrak{p}}$ and $\mathfrak{q}'B_{\mathfrak{p}}$ are maximal ideals of $B_{\mathfrak{p}}$.
>
> **Step 3 — comparable maximal ideals coincide.** From $\mathfrak{q} \subseteq \mathfrak{q}'$, extension gives $\mathfrak{q}B_{\mathfrak{p}} \subseteq \mathfrak{q}'B_{\mathfrak{p}}$. Now $\mathfrak{q}B_{\mathfrak{p}}$ is a maximal ideal contained in the proper ideal $\mathfrak{q}'B_{\mathfrak{p}}$ (proper because it is a prime, hence $\neq B_{\mathfrak{p}}$); maximality forces $\mathfrak{q}B_{\mathfrak{p}} = \mathfrak{q}'B_{\mathfrak{p}}$.
>
> **Step 4 — contract back.** The prime-correspondence bijection for $B \to B_{\mathfrak{p}}$ (restricted to primes disjoint from $A \setminus \mathfrak{p}$, which includes $\mathfrak{q}, \mathfrak{q}'$) is injective; since $\mathfrak{q}, \mathfrak{q}'$ have equal extensions, $\mathfrak{q} = \mathfrak{q}'$. $\blacksquare$
>
> ---
> **Corollary ($\dim B \leq \dim A$).** Let $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ be a strict chain in $\operatorname{Spec} B$. Contraction gives $\mathfrak{q}_0 \cap A \subseteq \cdots \subseteq \mathfrak{q}_n \cap A$ in $\operatorname{Spec} A$. If two consecutive contractions were equal, say $\mathfrak{q}_i \cap A = \mathfrak{q}_{i+1} \cap A$ with $\mathfrak{q}_i \subsetneq \mathfrak{q}_{i+1}$, incomparability would force $\mathfrak{q}_i = \mathfrak{q}_{i+1}$, a contradiction. So the contracted chain is strict of length $n$, whence $\dim A \geq n$. Taking the supremum over chains in $B$, $\dim B \leq \dim A$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fibres of a finite map of varieties are finite sets of points.** For a module-finite map of affine coordinate rings $A \hookrightarrow B$, incomparability says the fibre over a point is zero-dimensional, and finiteness of $B$ as an $A$-module makes the fibre ring Artinian, so the fibre is a finite set. This is the algebraic core of "a finite morphism is finite-to-one", and it is non-obvious that *no* metric or topological compactness is used — purely the antichain property plus Artinian-ness.

**Primes over a rational prime in a number ring are pairwise incomparable.** For $\mathbb{Z} \subseteq \mathcal{O}_K$, the primes over $(p)$ are all maximal (they lie over the maximal ideal $(p)$) and pairwise incomparable by incomparability — so the factorisation $p\mathcal{O}_K = \mathfrak{P}_1^{e_1}\cdots\mathfrak{P}_g^{e_g}$ involves distinct, incomparable primes. The application is non-obvious because incomparability is what guarantees the $\mathfrak{P}_i$ are genuinely distinct maximal ideals, not nested, underwriting the well-definedness of the splitting type.

**A finite extension of a field is zero-dimensional.** Specialising to $A = k$ a field, any integral $k$-algebra $B$ has $\dim B \leq \dim k = 0$, recovering that a ring integral over a field has Krull dimension $0$ — every prime is maximal. The application is non-obvious because it derives the zero-dimensionality of finite extensions from the *same* incomparability that governs number rings and varieties — one theorem, three scales.

---

# Bridges

- **[[Thm - Lying Over|Lying Over]]** — lying over makes the fibre non-empty; incomparability makes it an antichain. The two are complementary: one says the fibre exists, the other says it has no vertical structure. Together with module-finiteness they yield "non-empty finite fibre".

- **[[Thm - Going Up|Going Up]]** — incomparability is the strictness partner of going up. Going up lifts an ascending chain with $\subseteq$; incomparability promotes each $\subseteq$ to $\subsetneq$, so chain length is preserved exactly. This pairing is what makes $\dim A \leq \dim B$ an *equality* of lengths along the lifted chain.

- **[[Thm - Integral Extensions Preserve Dimension|Integral Extensions Preserve Dimension]]** — incomparability supplies the upper bound $\dim B \leq \dim A$ (contract a chain, no collapse), while lying over and going up supply $\dim A \leq \dim B$. Incomparability is one of the two girders, and notably the one that needs no normality.

- **[[Thm - Integral Extensions and Fields (Domain Criterion)|Domain/Field Criterion]]** — the criterion "contraction of maximal is maximal" is the engine: it is what makes both primes maximal after localizing, and maximality is what forbids nesting. Incomparability is, in a sense, the domain criterion plus "maximal ideals form an antichain".

---

# Unlocked by This

> [!tip] Finite morphisms have zero-dimensional (finite) fibres *(from Algebraic Geometry)*
> Incomparability is the algebra of "the fibres of a **finite morphism of varieties** are zero-dimensional", and with module-finiteness, *finite*. A finite map is therefore a finite-to-one covering with isolated fibre points — the prototype being $\operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$, where each fibre has one or two points. The general principle that finite morphisms have finite fibres, central to the theory of **schemes** and ramification, is the geometric upgrade.
