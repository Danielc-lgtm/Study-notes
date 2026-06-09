---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Primary Ideal"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - The Prime Spectrum (Spec)"
  - "Def - Quotient Ring"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring and $I \subsetneq R$ a proper [[Def - Ideal|ideal]] that admits a primary decomposition $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$, with each $\mathfrak{q}_i$ a [[Def - Primary Ideal|primary ideal]] and $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ its [[Def - Radical of an Ideal and the Nilradical|radical]] (a prime). A decomposition is **minimal** when the $\mathfrak{p}_i$ are distinct and no $\mathfrak{q}_i$ contains $\bigcap_{j \neq i} \mathfrak{q}_j$. We write $\operatorname{Spec} R$ for the [[Def - The Prime Spectrum (Spec)|prime spectrum]], $V(I) = \{\mathfrak{p} \in \operatorname{Spec} R : I \subseteq \mathfrak{p}\}$, and $(I : x) = \{r \in R : rx \in I\}$ for the colon ideal. The full registry is on [[Commutative Algebra IX — Primary Decomposition]].

This is a compound page: it defines four interlocking notions — the **associated primes** $\operatorname{Ass}(I)$, the **minimal (isolated) primes**, the **embedded primes**, and a **minimal prime over $I$** — because they are introduced together and none is fully usable without the others. The associated primes are the radicals of the primary components; among them the minimal ones are isolated and the rest are embedded; and "minimal prime over $I$" is the intrinsic, decomposition-free description of the isolated ones.

---

# Axiom Motivation

The goal is to extract, from a primary decomposition $I = \bigcap \mathfrak{q}_i$, the part that is *forced by $I$ alone*. A decomposition is a presentation, and like any presentation it has redundancy and choice baked in — the same $I$ can be written several ways. The motivating question of the whole chapter is: **what survives, unchanged, across every minimal primary decomposition of $I$?** The answer turns out to be a finite set of prime ideals, and the entire point of this page is to name that set and to stratify it.

**Why the radicals, and not the primary components themselves.** Start by asking which data attached to the decomposition could possibly be invariant. The primary components $\mathfrak{q}_i$ are *not* invariant — the running example $(X^2, XY)$ has two different minimal decompositions whose $(X,Y)$-primary components differ. So if anything is canonical, it must be coarser than the components. The natural candidate is the list of *primes* the components are attached to: each $\mathfrak{q}_i$ is $\mathfrak{p}_i$-primary, and $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ is the prime "$\mathfrak{q}_i$ belongs to". Taking radicals is the act of forgetting the multiplicity (the thickening) and keeping only the prime. The First Uniqueness Theorem then makes the bet pay off: the *set* $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$ is the same for every minimal decomposition. We name it $\operatorname{Ass}(I)$, the **associated primes**, and it is the invariant skeleton of $I$. Defining it as "the radicals of the components" is the path of least resistance; that it is intrinsic is the content of the theorem.

**Why minimality is required for the set to be the right size.** If we allowed non-minimal decompositions, the set of radicals could be artificially inflated — repeating a component, or adding a redundant $\mathfrak{q}_i \supseteq \bigcap_{j \neq i} \mathfrak{q}_j$, would introduce extra primes that $I$ does not really "see". Minimality strips exactly this padding: distinct radicals (no repetition) and no redundant component (every $\mathfrak{q}_i$ contributes something the others miss). With minimality imposed, $|\operatorname{Ass}(I)| = n$ is forced, and the set is as small as possible. This is why the definition is phrased relative to a *minimal* decomposition, and why the existence of minimal decompositions (from grouping same-radical primaries and deleting redundancies) is a prerequisite.

**Why stratify into minimal and embedded — the two have completely different behaviour.** Once $\operatorname{Ass}(I)$ is in hand, the deepest fact about it is that its members are *not on equal footing*. Some of the $\mathfrak{p}_i$ are minimal under inclusion within the set; these are the **isolated** (or **minimal**) primes, and they have an intrinsic, decomposition-free description: they are exactly the **minimal primes over $I$** — the primes $\mathfrak{p} \supseteq I$ with no prime strictly between $I$ and $\mathfrak{p}$, equivalently the minimal primes of the ring $R/I$. These are the primes the *radical* $\sqrt I = \bigcap (\text{minimal primes})$ records, hence the ones the geometric figure $V(I)$ can see — its irreducible components. The non-minimal members are the **embedded** primes; they are *not* visible in $\sqrt I$ and not visible in $V(I)$ as a set, yet they are genuine associated primes of $I$. The reason to separate them is that their behaviour under the uniqueness theorems is opposite: the isolated primes have *unique* primary components (Second Uniqueness, proved by localization), while the embedded primes have components that genuinely vary. Lumping them together would obscure the single most important structural fact of the chapter — that the canonical part of a decomposition is precisely the isolated part.

**Why "minimal prime over $I$" is the load-bearing intrinsic notion.** The phrase "isolated prime" is defined relative to $\operatorname{Ass}(I)$, which is defined relative to a decomposition. To break the circularity and make the isolated primes *manifestly* intrinsic, one identifies them with the minimal primes over $I$ — a notion that mentions no decomposition at all, only the inclusion order on primes containing $I$. That these two descriptions agree (minimal elements of $\operatorname{Ass}(I)$ $=$ minimal primes over $I$) is what lets one compute the irreducible components of $V(I)$ without ever computing a primary decomposition: just find the minimal primes containing $I$. This is the practical payoff of the whole stratification, and it is why "minimal prime over $I$" earns its own definition.

---

# The Definition

Let $I \subsetneq R$ admit a minimal primary decomposition $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ with $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$.

## Associated primes

The **associated primes** of $I$ are
$$\operatorname{Ass}(I) = \{\mathfrak{p}_1, \dots, \mathfrak{p}_n\} = \{\sqrt{\mathfrak{q}_i} : 1 \leq i \leq n\}.$$
By the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]] this set is independent of the chosen minimal decomposition; equivalently $\operatorname{Ass}(I) = \{\sqrt{(I:x)} : x \in R\} \cap \operatorname{Spec} R$.

## Minimal prime over an ideal

A **minimal prime over $I$** is a prime ideal $\mathfrak{p} \supseteq I$ such that there is no prime $\mathfrak{q}$ with $I \subseteq \mathfrak{q} \subsetneq \mathfrak{p}$. Equivalently, it is a prime of $R$ corresponding to a minimal prime ideal of $R/I$.

## Isolated (minimal) and embedded primes

The **isolated** (or **minimal**) primes of $I$ are the minimal elements of $\operatorname{Ass}(I)$ under inclusion. They coincide exactly with the minimal primes over $I$. The remaining associated primes — those that are not minimal in $\operatorname{Ass}(I)$ — are the **embedded** primes of $I$.

Thus $\operatorname{Ass}(I) = \{\text{isolated primes}\} \sqcup \{\text{embedded primes}\}$, with the isolated ones recovered intrinsically as the minimal primes over $I$ and satisfying $\sqrt{I} = \bigcap (\text{isolated primes})$.

---

# Categorical / Structural Definition

The structural home of these notions is the ring $R/I$ and its spectrum. The minimal primes over $I$ are precisely the **generic points of the irreducible components** of $\operatorname{Spec}(R/I) = V(I)$: each irreducible component is the closure $V(\mathfrak{p})$ of a unique generic point $\mathfrak{p}$, and these $\mathfrak{p}$ are the minimal primes. Reading $I = \operatorname{Ann}(R/I)$, the associated primes are the **associated primes of the module** $R/I$: a prime $\mathfrak{p}$ is associated to $I$ exactly when $\mathfrak{p} = \operatorname{Ann}(\bar x)$ for some $\bar x \in R/I$, equivalently when there is an injection of $R$-modules $R/\mathfrak{p} \hookrightarrow R/I$. In this framing the embedded primes are the associated points that are *not* generic points of components — they sit, as the name says, embedded inside a component. The union of all associated primes is the set of zero-divisors of $R/I$, which makes $\operatorname{Ass}$ the precise bookkeeping of where $R/I$ fails to be a domain. This module-theoretic definition, developed in [[Modules II — §3.3–3.4|Modules II]], is the one that generalises and is preferred in modern treatments; the ideal definition above is its restriction to the zero submodule of $R/I$.

---

# Relate to Other Fields / Compression

The cleanest compression: **$\operatorname{Ass}(I)$ is the finite set of primes "where $I$ has structure", split into the irreducible components (isolated primes, seen by the variety) and the embedded subvarieties (embedded primes, invisible to the variety but present in the scheme).** The isolated primes are recoverable from $\sqrt I$ alone; the embedded primes are the extra content of $I$ beyond $\sqrt I$.

**True name:** the true name of an associated prime is **"a prime of the form $\sqrt{(I:x)}$"** — a prime that arises as the radical of a colon ideal. This is the operational characterisation: to *find* the associated primes you compute $\sqrt{(I:x)}$ over varying $x$ and keep the primes; to *test* whether a given prime $\mathfrak{p}$ is associated you look for an $x$ with $\sqrt{(I:x)} = \mathfrak{p}$. The "radical of a component" description is for understanding; the colon description is for computing.

In geometry, the isolated primes are the **irreducible components** of $V(I)$ and the embedded primes are **embedded subvarieties** (most commonly the singular locus, or the intersection of two components, where lower-dimensional non-reduced structure hides). In the module-theoretic and homological setting, $\operatorname{Ass}$ controls depth, the zero-divisors, and the support; the isolated associated primes are the generic points of $\operatorname{Supp}(R/I)$. In number theory and Dedekind domains the embedded primes never appear (every nonzero prime is maximal, so all associated primes are isolated), which is exactly why factorisation there is clean.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}$, all isolated.** For $(90) = (2) \cap (3^2) \cap (5)$, the associated primes are $\operatorname{Ass}((90)) = \{(2), (3), (5)\}$, all radicals of the prime-power components. None contains another, so all three are isolated and there are no embedded primes — as always in a [[Def - Principal Ideal Domain|PID]]. They are the minimal primes over $(90)$, and $\sqrt{(90)} = (2) \cap (3) \cap (5) = (30)$.

**Is an instance — an embedded prime appears.** For $I = (X^2, XY) \subseteq k[X,Y]$ with minimal decomposition $(X) \cap (X,Y)^2$, the associated primes are $\operatorname{Ass}(I) = \{(X), (X,Y)\}$. Here $(X) \subsetneq (X,Y)$, so $(X)$ is the unique isolated prime (the line $X = 0$, the one irreducible component) and $(X,Y)$ is **embedded** (the fat point at the origin). The radical is $\sqrt I = (X)$, which sees only the isolated prime — the embedded $(X,Y)$ is invisible in $V(I)$.

**Is an instance — recovering isolated primes intrinsically.** For the same $I$, the minimal primes over $I$ are exactly the primes $\mathfrak{p} \supseteq (X^2, XY)$ minimal under inclusion; since $X^2 \in \mathfrak{p}$ forces $X \in \mathfrak{p}$, every prime over $I$ contains $(X)$, and $(X)$ is itself prime and contains $I$. So $(X)$ is the *unique* minimal prime over $I$ — matching the isolated prime found from the decomposition, and confirming $\sqrt I = (X)$ without any decomposition.

**Is NOT an instance — a non-minimal prime that is not associated.** Not every prime containing $I$ is an associated prime. For $I = (X^2, XY)$, the prime $(X, Y - 1)$ contains $X^2, XY$? Check: $X \in (X, Y-1)$ so $X^2, XY \in (X, Y-1)$, yes $I \subseteq (X, Y-1)$. But $(X, Y-1)$ is *not* associated: it is not minimal over $I$ (it strictly contains the minimal prime $(X)$) and it is not an embedded prime either ($\sqrt{(I:x)}$ never equals it). So "$\mathfrak{p} \supseteq I$ and $\mathfrak{p}$ prime" is strictly weaker than "$\mathfrak{p}$ associated" — being associated is special.

**Is NOT an instance — a component is not its prime.** It is a common slip to call the primary component $\mathfrak{q}_i$ itself "an associated prime". The associated prime is $\sqrt{\mathfrak{q}_i} = \mathfrak{p}_i$, not $\mathfrak{q}_i$. For $(X,Y)^2$, the associated prime is $(X,Y)$, while the component $(X,Y)^2$ is merely $(X,Y)$-primary; they are equal only when $\mathfrak{q}_i$ happens to be prime.

**Calibration check.** For $I = (X^2, XY)$, verify directly that $\operatorname{Ass}(I) = \{(X), (X,Y)\}$ by exhibiting an $x$ with $\sqrt{(I:x)} = (X)$ and an $x$ with $\sqrt{(I:x)} = (X,Y)$ (try $x = Y$ and $x = X$ respectively). Confirm that $(X)$ is the unique minimal prime over $I$, hence the unique isolated prime, and that $(X,Y)$ is embedded because it strictly contains $(X)$. Finally check that $\sqrt I = \bigcap(\text{isolated primes}) = (X)$, so the variety $V(I)$ is just the line — losing the embedded point.

---

# Unlocked by This

> [!tip] Irreducible components and the reduced subscheme *(from Algebraic Geometry)*
> The isolated (minimal) primes of $I$ are the generic points of the **irreducible components** of $V(I)$, and $\sqrt I = \bigcap(\text{isolated primes})$ is the ideal of the **reduced subscheme** $V(I)_{\mathrm{red}}$. The embedded primes are **embedded components** — subvarieties glued inside a bigger component, carrying non-reduced infinitesimal structure that the reduced subscheme erases. This stratification of $\operatorname{Ass}(I)$ is exactly the decomposition of a scheme into its components together with the record of where it is non-reduced.

> [!tip] Associated primes of a module and the support *(from Commutative Algebra / Homological Algebra)*
> Reading $I = \operatorname{Ann}(R/I)$, $\operatorname{Ass}(I)$ becomes the set of **associated primes of the module** $R/I$ — the primes $\mathfrak{p}$ with $R/\mathfrak{p} \hookrightarrow R/I$. Their union is the set of zero-divisors of $R/I$; their minimal elements are the generic points of the **support** $\operatorname{Supp}(R/I) = V(I)$. This is the gateway to the homological theory: $\operatorname{Ass}$ controls depth, the grade of an ideal, and the behaviour of $\operatorname{Ext}^i_R(R/I, R)$, and the embedded primes are precisely the obstruction to $R/I$ being Cohen–Macaulay.
