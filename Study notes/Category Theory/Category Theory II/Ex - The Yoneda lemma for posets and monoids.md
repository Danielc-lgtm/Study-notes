---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Yoneda Lemma"
  - "Thm - The Yoneda Embedding is Fully Faithful"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Problem Statement

Specialize the [[Thm - The Yoneda Lemma|Yoneda lemma]] and the [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness of the Yoneda embedding]] to two thin/one-object categories, and identify what they become.

1. **Posets.** Let $(P, \leq)$ be a poset, regarded as a category with one arrow $a \to b$ iff $a \leq b$. Work out what the Yoneda embedding and full faithfulness say. Show they reduce to the statement that an element of a poset is determined by the set of elements below it (the principal down-set), i.e. the order-embedding $P \hookrightarrow$ down-sets.
2. **Monoids.** Let $M$ be a monoid, regarded as a one-object category $BM$. Show full faithfulness becomes the regular representation: $M$ embeds into the transformation monoid of its underlying set.

**Recall:**

![[Thm - The Yoneda Embedding is Fully Faithful#Statement]]

A poset is a thin category (at most one morphism between objects); a presheaf $P^{op} \to \mathbf{Set}$ that is representable is a principal down-set. A monoid $M$ is a one-object [[Def - Category|category]] $BM$ with $\mathrm{Hom} = M$ and composition the monoid product; a presheaf on $BM$ is a right $M$-set.

---

# Convergent Strategy

**Problem class:** This is a "degenerate the general theorem" exercise: take Yoneda in its full generality and see what it says in the simplest categories. The routine is to substitute the special category into each piece of the statement and simplify until a familiar order-theoretic or monoid-theoretic fact emerges.

**Assumption pattern:** The decisive feature is *thinness* (posets: at most one arrow between objects) and *one-object-ness* (monoids: a single object). Thinness collapses hom-sets to truth values $\{0, 1\}$, so presheaves become down-closed predicates; one-object-ness collapses presheaves to $M$-sets. These structural assumptions are what make the general theorem degenerate to something recognizable.

**Theorem routing:** For posets, the contravariant Yoneda embedding $P \to [P^{op}, \mathbf{Set}]$ lands in presheaves valued in $\{0,1\}$ — i.e. down-sets — and full faithfulness becomes "$a \leq b$ iff the down-set of $a$ is contained in that of $b$". For monoids, [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]] applied to $BM$ gives $M \cong \mathrm{End}_{M\text{-Set}}(M)$, the regular representation, exactly as in the group case [[Ex - Yoneda generalizes Cayley's theorem]] but without invertibility.

**Key decision point:** The interesting recognition is that in a thin category the Yoneda lemma is *not* trivial but says something sharp: it becomes "$a \leq b$ if and only if every $x \leq a$ has $x \leq b$", i.e. an element is determined by its down-set. One must resist the temptation to dismiss the poset case as content-free; the point is to see which order-theoretic statement it is.

---

# Legal Operations Used

1. **Operation 8 from the topic page (translate between a structure and its category).** We pass between a poset/monoid and its associated category, and between order/monoid data and presheaves.

2. **Operation 9 from the topic page (apply Yoneda to compute morphisms/embeddings).** Full faithfulness becomes an order-embedding (posets) and the regular representation (monoids).

---

# Hints

> [!note]- Hint 1
> In a poset $P$, $\mathrm{Hom}(a, b)$ is a singleton if $a \leq b$ and empty otherwise. So the representable presheaf $\mathbf{y}(a) = P(-, a)$ assigns to each $x$ the truth value of "$x \leq a$" — it is the principal down-set $\mathord{\downarrow}a = \{x : x \leq a\}$.

> [!note]- Hint 2
> Full faithfulness says $P(a, b) \cong \mathrm{Nat}(\mathbf{y}a, \mathbf{y}b)$. A natural transformation between down-set presheaves is exactly an inclusion $\mathord{\downarrow}a \subseteq \mathord{\downarrow}b$. So $a \leq b \iff \mathord{\downarrow}a \subseteq \mathord{\downarrow}b$.

> [!note]- Hint 3
> For a monoid $M$, $BM$ has one object with endomorphism monoid $M$. The representable presheaf is the right regular $M$-set. Full faithfulness gives $M \cong \mathrm{End}_{M\text{-Set}}(M)$.

> [!note]- Hint 4
> By the Yoneda lemma, an $M$-equivariant endomorphism of $M$ is determined by the image of $1$, and equivariance forces it to be left-multiplication $L_a$. Unlike the group case, $L_a$ need not be a bijection — monoid elements need not be invertible — so we get an embedding into the transformation monoid, not the symmetric group.

---

# Solution

The plan is to substitute each special category into Yoneda. For posets the hom-sets degenerate to truth values and the embedding becomes the down-set map; for monoids the construction is the group argument minus invertibility, giving the regular representation by transformations.

**Step 1: Posets — the representable presheaf is a down-set.**

> [!note]- Derivation
> In the poset-category $P$, $\mathrm{Hom}(x, a)$ has one element if $x \leq a$ and none otherwise, so as a presheaf $\mathbf{y}(a) = P(-, a)$ is the indicator of the principal **down-set** $\mathord{\downarrow}a = \{x \in P : x \leq a\}$. A presheaf $P^{op} \to \mathbf{Set}$ that is representable thus corresponds to a down-closed subset of $P$.

**Step 2: Posets — full faithfulness is the order-embedding by down-sets.**

> [!note]- Derivation
> Full faithfulness gives $P(a, b) \cong \mathrm{Nat}(\mathbf{y}a, \mathbf{y}b)$. The left side is a singleton iff $a \leq b$. A natural transformation $\mathbf{y}a \Rightarrow \mathbf{y}b$ between down-set indicators exists (and is unique) iff $\mathord{\downarrow}a \subseteq \mathord{\downarrow}b$ — at each $x$, the component $\{x \leq a\} \to \{x \leq b\}$ is a function of truth values, which exists iff $x \leq a \Rightarrow x \leq b$. So
> $$a \leq b \iff \mathord{\downarrow}a \subseteq \mathord{\downarrow}b,$$
> i.e. **an element of a poset is determined by its principal down-set**, and $a \mapsto \mathord{\downarrow}a$ is an order-embedding $P \hookrightarrow (\text{down-sets}, \subseteq)$. This is the order-theoretic shadow of "an object is determined by maps into it" — and it is the **Dedekind–MacNeille / Yoneda** completion in miniature.

**Step 3: Monoids — full faithfulness is the regular representation.**

> [!note]- Derivation
> For a monoid $M$ as the one-object category $BM$, the representable presheaf is the **right regular $M$-set** $M$ (precomposition = right multiplication). Full faithfulness gives $M = BM(\bullet, \bullet) \cong \mathrm{End}_{M\text{-Set}}(M)$. By the [[Thm - The Yoneda Lemma|Yoneda lemma]], an $M$-equivariant endomorphism is determined by the image $a$ of $1$, and equivariance forces it to be left-multiplication $L_a : m \mapsto am$. The map $a \mapsto L_a$ is an injective monoid homomorphism $M \hookrightarrow \mathrm{End}_{\mathbf{Set}}(M)$ — the monoid of *all* self-maps of the underlying set, under composition. Crucially, $L_a$ need not be a bijection (if $a$ is not invertible), so we embed into the *transformation monoid* $\mathrm{End}_{\mathbf{Set}}(M)$, not the symmetric group. This is the monoid regular representation, the exact analogue of Cayley's theorem ([[Ex - Yoneda generalizes Cayley's theorem]]) with invertibility dropped.

> [!note]- Complete formal solution
> *Posets.* The representable presheaf $\mathbf{y}(a) = P(-, a)$ is the indicator of the down-set $\mathord{\downarrow}a$. Full faithfulness $P(a,b) \cong \mathrm{Nat}(\mathbf{y}a, \mathbf{y}b)$ becomes $a \leq b \iff \mathord{\downarrow}a \subseteq \mathord{\downarrow}b$, so $a \mapsto \mathord{\downarrow}a$ is an order-embedding of $P$ into its down-sets. *Monoids.* The representable presheaf on $BM$ is the right regular $M$-set; full faithfulness gives $M \cong \mathrm{End}_{M\text{-Set}}(M)$, and by Yoneda each equivariant endomorphism is left-multiplication $L_a$, yielding an injective monoid homomorphism $M \hookrightarrow \mathrm{End}_{\mathbf{Set}}(M)$ — the regular representation by transformations (not necessarily bijections). $\blacksquare$

---

# Key Takeaways

**Yoneda in a thin category is the statement "an element is determined by what lies below it".** The poset case strips Yoneda to its order-theoretic skeleton: because hom-sets are truth values, the representable presheaf is a down-set, and full faithfulness is exactly the antisymmetry-flavored fact that $a \leq b$ iff $\mathord{\downarrow}a \subseteq \mathord{\downarrow}b$. This is not content-free — it is the embedding of a poset into its lattice of down-sets, the starting point of the Dedekind–MacNeille completion. The transferable insight is that Yoneda always says "an object is determined by its lower set of probes", and in a poset "probes" are just smaller elements, so the abstract slogan becomes a concrete order-embedding.

**The monoid case shows Cayley's theorem never needed invertibility — only the regular representation.** Comparing posets, monoids, and groups reveals a hierarchy of degenerations of the same theorem. For groups, left-multiplications are bijections, so you land in the symmetric group (Cayley). For monoids, they are merely self-maps, so you land in the transformation monoid. The invertibility used in [[Ex - Yoneda generalizes Cayley's theorem]] is an *extra* fact about groups, not part of the Yoneda mechanism; the embedding into transformations is the genuinely general statement. Recognizing this tells you the regular representation exists for any monoid, semigroup-with-identity, or category — wherever there is composition.

**One theorem, many faces: thinness and object-count are the dials.** The unifying lesson is that the Yoneda embedding is a single construction whose specializations are named theorems across mathematics — order-embeddings for posets, regular representations for monoids and groups, Spec for rings ([[Ex - A scheme is determined by its functor of points]]). The two structural dials are "how many objects" and "how thin the hom-sets". Turning them produces the zoo of concrete embeddings, and seeing them as one phenomenon is exactly the kind of unifying frame the subject is built to provide. When you meet a new "X is determined by its Y" or "X embeds in transformations of Y" theorem, suspect it is Yoneda in disguise.
