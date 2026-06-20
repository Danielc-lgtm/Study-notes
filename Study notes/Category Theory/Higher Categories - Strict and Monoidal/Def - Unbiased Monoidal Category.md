---
type: definition
subject: higher-categories
prereqs:
  - "Def - Monoidal Category"
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]]. The new ingredient is a tensor product of *every* arity at once. For each integer $n \geq 0$ we have an **$n$-ary tensor functor**
$$\otimes_n : \mathcal{C}^n \longrightarrow \mathcal{C}, \qquad (A_1, \dots, A_n) \longmapsto (A_1 \otimes \cdots \otimes A_n),$$
where $\mathcal{C}^n$ is the $n$-fold product category. The two extreme cases are special and are worth naming: $\otimes_0 : \mathcal{C}^0 = \mathbf{1} \to \mathcal{C}$ picks out a single object, the **unit** $I = \otimes_0()$ (the empty tensor), and $\otimes_1 : \mathcal{C} \to \mathcal{C}$ is required to be the identity functor. The coherence isomorphisms are $\gamma$ (composition/associativity, for nesting tensors) and $\iota$ (unit, comparing $\otimes_1$ with the identity). We use $\langle A_1, \dots, A_n \rangle$ or $(A_1 \otimes \cdots \otimes A_n)$ for the unbracketed $n$-fold tensor. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

> [!warning] Convention: "biased" versus "unbiased"
> The familiar [[Def - Monoidal Category|monoidal category]] (CT V) is **biased**: it takes the binary $\otimes$ and the nullary $I$ as primitive and *derives* all other arities by bracketing. This page defines the **unbiased** version, which takes *all* arities as primitive and equally fundamental. The two are equivalent (see [[Thm - Biased and Unbiased Monoidal Categories Coincide]]), but the unbiased presentation makes coherence transparent, so we keep them strictly separate notationally: $\otimes$ for binary, $\otimes_n$ for the unbiased family.

---

# Axiom Motivation

A [[Def - Monoidal Category|monoidal category]] is built on a *choice*: we single out the **binary** tensor $A \otimes B$ and the **nullary** unit $I$ as primitive, and we manufacture every other tensor by bracketing — $A \otimes B \otimes C$ has to be read as either $(A \otimes B) \otimes C$ or $A \otimes (B \otimes C)$, and these are merely isomorphic, not equal. The whole apparatus of associators, unitors, the pentagon, and the triangle exists to manage the ambiguity created by this choice. The unbiased viewpoint asks the natural question: **why choose at all?** Why privilege the binary operation when the thing we actually want is "tensor together a list of objects of any length"? An unbiased monoidal category answers by taking the $n$-ary tensor $\otimes_n$ as fundamental for *every* $n$ simultaneously, on an equal footing.

Suppose we do this. For each $n$ we have a functor $\otimes_n : \mathcal{C}^n \to \mathcal{C}$, with $\otimes_0$ giving the unit $I$ and $\otimes_1$ the identity. The desideratum is that these fit together coherently: tensoring a list, then tensoring the results, should agree with tensoring the concatenated list. Concretely, if we tensor $n$ separate lists of objects of lengths $k_1, \dots, k_n$ — getting $n$ objects $\otimes_{k_1}(\vec A^1), \dots, \otimes_{k_n}(\vec A^n)$ — and then tensor those $n$ results with $\otimes_n$, we should land at (an object canonically isomorphic to) the tensor of the *single* concatenated list of length $k_1 + \cdots + k_n$. This is the **composition** or **associativity** isomorphism
$$\gamma : \otimes_n\big(\otimes_{k_1}(\vec A^1), \dots, \otimes_{k_n}(\vec A^n)\big) \;\overset{\cong}{\longrightarrow}\; \otimes_{k_1 + \cdots + k_n}(\vec A^1, \dots, \vec A^n).$$
There is one such isomorphism for every way of partitioning a list into sublists. Likewise there is a **unit** isomorphism $\iota$ comparing $\otimes_1(A)$ with $A$ (since $\otimes_1$ is the identity, this can be taken to be the identity, but recording it makes the bookkeeping uniform).

Now the decisive simplification. In the biased theory, coherence requires the pentagon *and* the triangle, two separate diagrams whose sufficiency is a non-trivial theorem ([[Thm - Mac Lane Coherence Theorem|Mac Lane]]). What replaces them here? Only **two** axioms, and both are of "associativity is associative" type. The first is a single **associativity coherence**: composing the $\gamma$'s in two stages (partition a list into sublists, then partition each sublist further) must agree with composing in one stage (partition into the finest pieces directly). The second is a **unit coherence**: inserting a $\otimes_1$ via $\iota$ and then composing via $\gamma$ must be the identity. That is all. The pentagon — which in the biased world is a *consequence* you must check — becomes, in the unbiased world, a *special case* of the single associativity axiom (the case of re-partitioning a length-three list).

Why is this better, and could a reader invent it? The motivation is exactly the experience of bracketing. Once you notice that the pentagon is just "the two ways of regrouping four things agree," and that the only reason there is a pentagon (and not, say, a hexagon or an infinite tower of polygons) is the binary bias, the unbiased reformulation suggests itself: make the $n$-ary operation primitive, demand only that *re-partitioning is coherent*, and let the pentagon fall out as one instance. The structure is precisely a **(pseudo-)algebra for the free-monoid monad** $M$ on $\mathbf{Cat}$, or equivalently a **lax/pseudo-algebra for the "lists" operad** — the $n$-ary operations are exactly the points of the terminal operad, and "monoidal category" means "category with a coherent action of the lists operad." (The biased pentagon-and-triangle is then revealed as a *presentation* of this operad by binary generators and the associativity relation.)

What goes wrong if we drop each axiom? Drop the associativity coherence and the $\gamma$'s no longer determine a single canonical isomorphism between two ways of tensoring a long list — exactly the failure the pentagon rules out in the biased setting, now visible directly. Drop the unit coherence and the unit object $I = \otimes_0()$ stops behaving like a unit: $\otimes_2(I, A)$ would not be canonically $A$. And if we *strengthen* all the $\gamma$'s and $\iota$'s to identities, we recover a **strict** monoidal category, where $\otimes_n$ literally is iterated binary $\otimes$ with no bracketing ambiguity at all. The unbiased weak notion is the Goldilocks point: every arity is primitive, coherence costs only two axioms, and strictness is the degenerate case.

---

# The Definition

An **unbiased monoidal category** consists of:

- a [[Def - Category|category]] $\mathcal{C}$;
- for each $n \geq 0$, a [[Def - Functor|functor]] $\otimes_n : \mathcal{C}^n \to \mathcal{C}$ (the **$n$-ary tensor**), written $\otimes_n(A_1, \dots, A_n) = (A_1 \otimes \cdots \otimes A_n)$, with $\otimes_0() = I$ the **unit**;
- for each $n \geq 0$ and each tuple of arities $(k_1, \dots, k_n)$, a natural **composition isomorphism**
$$\gamma_{k_1, \dots, k_n} : \otimes_n\big(\otimes_{k_1}(-), \dots, \otimes_{k_n}(-)\big) \;\overset{\cong}{\Longrightarrow}\; \otimes_{k_1 + \cdots + k_n}(-);$$
- a natural **unit isomorphism**
$$\iota : \otimes_1 \;\overset{\cong}{\Longrightarrow}\; \mathrm{id}_{\mathcal{C}};$$

subject to two coherence axioms:

**Associativity coherence.** Re-partitioning a list in two stages agrees with re-partitioning it in one stage. Precisely, for a doubly-indexed family of arities, the two composites of $\gamma$'s from
$$\otimes_n\Big(\otimes_{m_1}\big(\otimes_{k_{1,1}}(-), \dots\big), \dots\Big) \quad\text{to}\quad \otimes_{\sum k_{i,j}}(-)$$
— one contracting the inner $\gamma$'s first, the other the outer — are equal.

**Unit coherence.** Composing along the unit is trivial: $\gamma_{1,\dots,1}$ followed by nothing, and the insertion of $\otimes_1$ via $\iota$, satisfy
$$\gamma_{n} \circ (\otimes_n \text{ of } \iota\text{'s}) = \mathrm{id}, \qquad \gamma_{k} \circ \iota_{\otimes_k} = \mathrm{id},$$
so that $\otimes_1$ inserted anywhere via $\iota$ and then composed away leaves the tensor unchanged.

An unbiased monoidal category is **strict** if all $\gamma$ and $\iota$ are identity natural transformations; then $\otimes_{m+n} = \otimes_m \circ (\text{things}) = \otimes_n$ composites literally coincide and $\otimes_n$ is genuine iterated tensoring with no bracketing.

A **braided** (resp. **symmetric**) unbiased monoidal category additionally carries a coherent action of the symmetric groups: an isomorphism $\otimes_n(A_{\sigma(1)}, \dots, A_{\sigma(n)}) \cong \otimes_n(A_1, \dots, A_n)$ for each permutation $\sigma$, compatible with $\gamma$. (Compare the binary [[Def - Monoidal Category|braiding and symmetry]]; symmetry is the case where the $S_n$-action is honest, braided where it is an action of the braid groups.)

---

# Categorical / Structural Definition

The unbiased monoidal category *is* the categorical definition: it is the structure you get by spelling out "a category with a coherent action of the operad of lists." Two equivalent high-level descriptions make this precise.

**As a pseudo-algebra for a $2$-monad.** Let $M : \mathbf{Cat} \to \mathbf{Cat}$ be the free-strict-monoidal-category $2$-monad — informally, $M\mathcal{C}$ is the category of finite *lists* of objects of $\mathcal{C}$, with $M$'s monad structure given by concatenation. A **strict** monoidal category is a strict algebra $M\mathcal{C} \to \mathcal{C}$; an **unbiased (weak) monoidal category is a pseudo-algebra** for $M$: a functor $\otimes : M\mathcal{C} \to \mathcal{C}$ together with the invertible coherence cells $\gamma, \iota$ witnessing the algebra laws up to isomorphism, satisfying exactly the two coherence axioms above. The $n$-ary tensor $\otimes_n$ is the restriction of $\otimes$ to length-$n$ lists.

**As an algebra for the terminal operad.** The two-stage/one-stage associativity axiom is precisely the associativity of operadic composition, and the $\gamma$'s are the structure maps of an algebra. The relevant operad is the **terminal (non-symmetric) operad** $\mathrm{As}$ with one operation in each arity — the operad whose algebras in $\mathbf{Set}$ are [[Def - Monoid in a Monoidal Category|monoids]]. An unbiased monoidal category is a (pseudo-)algebra for $\mathrm{As}$ in $\mathbf{Cat}$: "a categorified monoid, with the monoid law holding up to coherent isomorphism." This is the cleanest possible statement of what a monoidal category is, and it is the one that generalises directly to **higher operads** (see [[Higher Categories — Operads and Multicategories]]).

The point of both descriptions is the same: by taking the *whole operad of arities* as primitive rather than presenting it by binary generators, the coherence data and axioms become exactly the operad's structure and associativity — no pentagon to discover, because the pentagon is just associativity of the operad evaluated on a length-three input.

---

# Relate to Other Fields / Compression

The unbiased monoidal category is the answer to "what is a monoidal category, *really*, with the arbitrary binary choice removed." It compresses to: **a category on which you can tensor lists of objects of any length, coherently.** The binary tensor is then a generator, the pentagon a relation, and the whole biased apparatus a *presentation* of this cleaner object — just as a group given by generators and relations is a presentation of the underlying group.

**True name:** an unbiased monoidal category is "a pseudo-algebra for the lists/As operad in $\mathbf{Cat}$" — a categorified monoid. Operationally, when a coherence question arises ("do these two ways of bracketing-and-swapping agree?"), the unbiased frame answers it instantly: both sides are operad operations on the same input, and the operad has a *unique* operation of each arity, so they are equal. This is why the [[Thm - Coherence for Unbiased Monoidal Categories|coherence theorem]] is almost a tautology in the unbiased language and a real theorem in the biased one.

The deep compression, carried forward into the rest of higher category theory: **structures-up-to-coherent-isomorphism are pseudo-algebras for operads (or $2$-monads).** Monoidal categories are pseudo-algebras for the lists operad; braided ones for the braid operad; symmetric ones for the symmetric/$E_\infty$ operad; and weak $n$-categories for globular operads. The unbiased monoidal category is the first and simplest instance of this organising principle, which is exactly why Leinster develops it before the general operadic machinery.

---

# Examples / Corollaries

**Is an instance — any biased [[Def - Monoidal Category|monoidal category]], made unbiased.** Given $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$, define $\otimes_n$ by *left-bracketing*: $\otimes_0() = I$, $\otimes_1(A) = A$, $\otimes_2 = \otimes$, $\otimes_3(A,B,C) = (A \otimes B)\otimes C$, and in general nest to the left. The $\gamma$'s are built from associators and unitors; [[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]] makes them well-defined and the two unbiased axioms hold. This is the forward direction of [[Thm - Biased and Unbiased Monoidal Categories Coincide]].

**Is an instance — $(\mathbf{Vect}_k, \otimes_n, k)$ unbiasedly.** Take $\otimes_n(V_1, \dots, V_n) = V_1 \otimes_k \cdots \otimes_k V_n$ defined by the universal property of the $n$-fold tensor product directly (the object representing $n$-linear maps), with $\otimes_0() = k$. Because the $n$-fold tensor product has its own universal property, the $\gamma$'s — comparing "tensor the sublists then tensor the results" with "tensor the whole list" — are the canonical isomorphisms between representing objects of the *same* multilinear functor, hence honestly canonical. This example shows the unbiased structure is often the *natural* one: nobody computes $V \otimes W \otimes U$ by choosing a bracketing.

**Is an instance — $(\mathbf{Set}, \times_n, 1)$ unbiasedly.** The $n$-fold cartesian product $\times_n(A_1, \dots, A_n) = A_1 \times \cdots \times A_n$ (tuples of length $n$), with the one-point set as $\otimes_0$. The $\gamma$'s reassociate tuples-of-tuples into flat tuples; they are canonical because the $n$-fold product is a [[Def - Limit and Colimit|limit]], determined up to unique isomorphism. The biased associator $((a,b),c) \mapsto (a,(b,c))$ is one instance of $\gamma$.

**Is an instance — every strict monoidal category, unbiasedly with $\gamma = \iota = \mathrm{id}$.** In $([\mathcal{C},\mathcal{C}], \circ, 1)$, the [[Def - Functor Category|endofunctor category]] under composition, $\otimes_n(F_1, \dots, F_n) = F_1 \circ \cdots \circ F_n$ is *strictly* associative, so all $\gamma$ are identities. The unbiased structure is strict.

**Is NOT an instance — a family of functors $\otimes_n$ with no coherent $\gamma$.** Suppose on $\mathbf{Set}$ we set $\otimes_2(A,B) = A \times B$ but $\otimes_3(A,B,C) = A \times B$ (forgetting $C$). There is no natural isomorphism $\gamma_{2,1} : \otimes_2(\otimes_2(A,B), C) \to \otimes_3(A,B,C)$, because the left side depends on $C$ and the right side does not. The arities are present but incoherent, so this is not an unbiased monoidal category — it shows the $\gamma$'s carry real content and are not free.

**Calibration check.** Verify that in any unbiased monoidal category the binary $\otimes_2$ together with the unit $\otimes_0()$ and the $\gamma$'s recover an associator $\alpha_{A,B,C} : (A\otimes_2 B)\otimes_2 C \to A \otimes_2 (B \otimes_2 C)$ via $\gamma_{2,1}^{-1}$ followed by $\gamma_{1,2}$, and that the pentagon for this $\alpha$ is the associativity axiom applied to a length-four list. Confirm that $\otimes_1 = \mathrm{id}$ forces the unitors to be canonical. And check that a strict unbiased monoidal category ($\gamma = \iota = \mathrm{id}$) is the same as a strict [[Def - Monoidal Category|monoidal category]] in the biased sense.

---

# Unlocked by This

> [!tip] Coherence as a Triviality *(from this chapter)*
> In the unbiased frame, [[Thm - Coherence for Unbiased Monoidal Categories|coherence]] says every diagram of $\gamma$'s and $\iota$'s commutes — almost immediate, because they are operad operations and the operad has one operation per arity. This is the conceptual upgrade of [[Thm - Mac Lane Coherence Theorem|Mac Lane's biased coherence theorem]].

> [!tip] Operads and Higher Algebra *(from Algebra and Topology)*
> An unbiased monoidal category is an algebra for the **lists/As operad** in $\mathbf{Cat}$. Swapping that operad for $E_n$, the **little $n$-disks operad**, gives $E_n$-monoidal categories, the categorical home of $n$-fold loop spaces and the input to **derived** and **factorization** algebra.

> [!tip] Pseudo-Algebras and 2-Monad Theory *(from Higher Category Theory)*
> "Structure up to coherent isomorphism" is uniformly a **pseudo-algebra for a 2-monad**. Unbiased monoidal categories (pseudo-algebras for the free-monoidal-category 2-monad) are the first example; the same machine produces unbiased bicategories, **lax-monoidal functors**, and the coherence theorems for all of them.
