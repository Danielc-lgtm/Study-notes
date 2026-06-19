---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - Monoidal Category"
  - "Def - Abelian Group"
  - "Def - Vector Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Fix a [[Def - Monoidal Category|monoidal category]] $(\mathcal{V}, \otimes, I)$ — the **base of enrichment**. The objects of $\mathcal{V}$ are the "values" the hom-objects take; $\otimes$ is the monoidal product, used to compose; $I$ is the unit object, used for identities. A category $\mathcal{C}$ enriched in $\mathcal{V}$ (a **$\mathcal{V}$-category**) has a class of objects $\mathrm{ob}\,\mathcal{C}$ and, for each ordered pair $A, B$, a **hom-object** $\mathcal{C}(A,B) \in \mathcal{V}$ — an *object of $\mathcal{V}$*, not a set. Composition is a morphism $c_{A,B,C} : \mathcal{C}(B,C) \otimes \mathcal{C}(A,B) \to \mathcal{C}(A,C)$ in $\mathcal{V}$, and the identity on $A$ is a morphism $j_A : I \to \mathcal{C}(A,A)$. We use $a, b, c$ for the associator and unitors of $\mathcal{V}$ when needed. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Axiom Motivation

The discovery of this definition begins with an observation you cannot unsee once you have seen it: in most categories you actually care about, the hom-set carries *more structure than a bare set*, and that structure is compatible with composition. If $\mathcal{C}$ is a category of [[Def - Vector Space|vector spaces]] and linear maps, then $\mathcal{C}(A,B)$ is not just a set of linear maps — it is itself a vector space, with pointwise addition and scaling, and composition $(g, f) \mapsto g \circ f$ is *bilinear*. If $\mathcal{C}$ is a category of chain complexes, $\mathcal{C}(A,B)$ is an [[Def - Abelian Group|abelian group]] and composition is biadditive. If $\mathcal{C}$ is a nice category of topological spaces, $\mathcal{C}(A,B)$ is itself a space and composition is continuous. The data "set of morphisms" is throwing away structure that the mathematics manifestly has.

So we want a definition of "category" in which the hom-sets are replaced by hom-*objects* living in some ambient category $\mathcal{V}$ — vector spaces, abelian groups, spaces — and in which composition and identities are morphisms *of $\mathcal{V}$*. The question is: what minimal structure on $\mathcal{V}$ is needed to even *state* the category axioms?

Look at what the axioms require. Composition takes a morphism $B \to C$ and a morphism $A \to B$ and returns a morphism $A \to C$. In the enriched world the inputs are two separate hom-objects, so composition must be a morphism *out of some combination of $\mathcal{C}(B,C)$ and $\mathcal{C}(A,B)$*. The combination that works is a **tensor product** $\mathcal{C}(B,C) \otimes \mathcal{C}(A,B)$ — a way of forming a single object out of two, with a universal property matching "a pair of inputs". This is the first thing $\mathcal{V}$ must have: a monoidal product $\otimes$. Without it there is no way to write down composition as a single morphism.

Next, identities. In an ordinary category the identity is a *chosen element* $1_A \in \mathcal{C}(A,A)$. But $\mathcal{C}(A,A)$ is now an object of $\mathcal{V}$, not a set, so "an element" must be rephrased categorically as "a morphism from a one-element object". The categorical one-element object is the **monoidal unit** $I$, and an identity becomes a morphism $j_A : I \to \mathcal{C}(A,A)$. This is the second thing $\mathcal{V}$ must have: a unit object $I$.

Finally, associativity and the unit laws. In the ordinary case these say $(h g) f = h (g f)$ and $1 \circ f = f = f \circ 1$. Enriched, they become *commuting diagrams in $\mathcal{V}$* — and to even write them down we need to move parentheses around tensor products and to insert and delete the unit, which requires the associator and unitors of $\mathcal{V}$. This is why $\mathcal{V}$ must be a *[[Def - Monoidal Category|monoidal]]* category, not just a category with a product: monoidality is exactly the package $(\otimes, I, a, l, r)$ needed to state the enriched category axioms.

What if we tried to drop the unit and ask only for a "semicategory" enriched in a semigroupal $\mathcal{V}$ (no $I$)? Then there is no way to express identity morphisms, and the entire theory of isomorphisms, adjunctions, and limits collapses — identities are not a technicality but the source of all the structure. What if we asked $\otimes$ to be the cartesian product specifically? That is too strong: it would force $\mathcal{V}$ to have projections and a diagonal, excluding the tensor products of vector spaces and abelian groups (where $V \otimes W$ is *not* the cartesian product $V \times W$) — and those are the examples we are trying to capture. The correct level of generality is precisely a monoidal category: enough structure to state the axioms, not so much that it excludes the tensor-product examples.

---

# The Definition

Let $(\mathcal{V}, \otimes, I)$ be a [[Def - Monoidal Category|monoidal category]]. A **category enriched in $\mathcal{V}$**, or **$\mathcal{V}$-category**, $\mathcal{C}$ consists of:

- a class $\mathrm{ob}\,\mathcal{C}$ of **objects**;
- for each pair $A, B \in \mathrm{ob}\,\mathcal{C}$, a **hom-object** $\mathcal{C}(A,B) \in \mathcal{V}$;
- for each triple $A, B, C$, a **composition** morphism in $\mathcal{V}$
$$c_{A,B,C} : \mathcal{C}(B,C) \otimes \mathcal{C}(A,B) \longrightarrow \mathcal{C}(A,C);$$
- for each object $A$, an **identity** morphism in $\mathcal{V}$
$$j_A : I \longrightarrow \mathcal{C}(A,A);$$

such that the following diagrams commute in $\mathcal{V}$, where $a$, $l$, $r$ are the associator and unitors of $\mathcal{V}$.

**Associativity.** The two ways of composing three hom-objects agree:
$$
c_{A,B,D} \circ (c_{B,C,D} \otimes 1) = c_{A,C,D} \circ (1 \otimes c_{A,B,C}) \circ a,
$$
as morphisms $\big(\mathcal{C}(C,D) \otimes \mathcal{C}(B,C)\big) \otimes \mathcal{C}(A,B) \to \mathcal{C}(A,D)$, where $a$ is the associator of $\mathcal{V}$ rebracketing the triple tensor product.

**Unit.** Composing with an identity does nothing:
$$
c_{A,A,B} \circ (1 \otimes j_A) = r_{\mathcal{C}(A,B)}, \qquad c_{A,B,B} \circ (j_B \otimes 1) = l_{\mathcal{C}(A,B)},
$$
where $l, r$ are the left and right unitors of $\mathcal{V}$ identifying $I \otimes X \cong X \cong X \otimes I$.

A **$\mathcal{V}$-functor** $F : \mathcal{C} \to \mathcal{D}$ assigns objects $F A$ and, for each pair, a morphism $F_{A,B} : \mathcal{C}(A,B) \to \mathcal{D}(FA, FB)$ in $\mathcal{V}$ commuting with composition and identities. These assemble into a category $\mathcal{V}\text{-}\mathbf{Cat}$.

---

# Categorical / Structural Definition

The definition *is* the categorical/structural one — it is "the definition of a category, transcribed so that every instance of 'set', 'element', and 'function' is replaced by 'object of $\mathcal{V}$', 'morphism out of $I$', and 'morphism of $\mathcal{V}$'." The dictionary is exact:

| Ordinary category | $\mathcal{V}$-category |
|---|---|
| hom-set $\mathcal{C}(A,B)$ | hom-object $\mathcal{C}(A,B) \in \mathcal{V}$ |
| pair of morphisms | tensor $\mathcal{C}(B,C) \otimes \mathcal{C}(A,B)$ |
| composition (a function) | composition (a $\mathcal{V}$-morphism $c$) |
| identity (an element of $\mathcal{C}(A,A)$) | identity (a $\mathcal{V}$-morphism $j_A : I \to \mathcal{C}(A,A)$) |
| associativity (an equation) | a commuting diagram in $\mathcal{V}$ |

Setting $\mathcal{V} = (\mathbf{Set}, \times, \{\ast\})$ recovers an ordinary [[Def - Category|category]] exactly: a hom-object is a set, $\otimes = \times$ packages a pair, and a morphism $\{\ast\} \to \mathcal{C}(A,A)$ picks out an element — the identity. So ordinary category theory is the special case $\mathcal{V} = \mathbf{Set}$, and enrichment is the systematic generalisation obtained by turning the dial on $\mathcal{V}$. The "underlying ordinary category" of a $\mathcal{V}$-category is recovered by applying the functor $\mathcal{V}(I, -) : \mathcal{V} \to \mathbf{Set}$ to each hom-object, which turns the hom-object back into its set of "elements" ($\mathcal{V}$-points).

---

# Relate to Other Fields / Compression

Enrichment is the observation that *the category axioms never mention that hom-sets are sets* — they only ever combine two morphisms and pick out an identity. So the axioms make sense in any [[Def - Monoidal Category|monoidal]] context, and a single definition unifies a long list of structures from algebra, geometry, and analysis that look unrelated.

**True name:** a $\mathcal{V}$-category is "an ordinary category whose hom-sets have been promoted to objects of $\mathcal{V}$, with composition and identity promoted to morphisms of $\mathcal{V}$." When you meet hom-sets carrying compatible extra structure, the trigger is to ask "which $\mathcal{V}$?" and then import all of category theory at once.

The most arresting instance is **Lawvere's metric spaces**. Take $\mathcal{V}$ to be the poset $[0,\infty]$ with the *reversed* order $\geq$ as its morphisms (so there is a unique morphism $x \to y$ exactly when $x \geq y$), monoidal product $\otimes = +$ (addition of distances), and unit $I = 0$. A category enriched in this $\mathcal{V}$ has objects (points), and a hom-object $\mathcal{C}(a,b) \in [0,\infty]$ — a number, the distance $d(a,b)$. The composition morphism $\mathcal{C}(b,c) \otimes \mathcal{C}(a,b) \to \mathcal{C}(a,c)$, since $\otimes = +$ and a morphism in $\mathcal{V}$ is the relation $\geq$, says exactly $d(b,c) + d(a,b) \geq d(a,c)$ — the **triangle inequality**. The identity $I \to \mathcal{C}(a,a)$, i.e. $0 \geq d(a,a)$, forces $d(a,a) = 0$. So a category enriched over $([0,\infty], \geq, +, 0)$ is precisely a (generalised, possibly asymmetric, possibly infinite) **metric space**, composition *is* the triangle inequality, and identities *are* the vanishing of self-distance. That a metric space and a 2-category are two readings of one definition is the high-water mark of the enrichment idea.

---

# Examples / Corollaries

**Is an instance — $\mathbf{Set}$-enrichment is ordinary category theory.** With $\mathcal{V} = (\mathbf{Set}, \times, \{\ast\})$, a $\mathcal{V}$-category is exactly an ordinary [[Def - Category|category]], as the dictionary above shows. This is the calibration point: every theorem about $\mathcal{V}$-categories specialises to a familiar theorem about ordinary categories at $\mathcal{V} = \mathbf{Set}$.

**Is an instance — $\mathbf{Ab}$-enrichment is a preadditive category.** With $\mathcal{V} = (\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$, the hom-objects $\mathcal{C}(A,B)$ are [[Def - Abelian Group|abelian groups]], and composition $\mathcal{C}(B,C) \otimes_{\mathbb{Z}} \mathcal{C}(A,B) \to \mathcal{C}(A,C)$, being a morphism out of a tensor product, is exactly a *bilinear* (biadditive) map — composition distributes over addition on both sides. This is the definition of a **preadditive** (or $\mathbf{Ab}$-) category, the starting point of homological algebra; adding biproducts gives an additive category, and adding kernels and cokernels gives an **abelian category**.

**Is an instance — $\mathbf{Vect}_k$-enrichment is a $k$-linear category.** With $\mathcal{V} = (\mathbf{Vect}_k, \otimes_k, k)$, the hom-objects are [[Def - Vector Space|k-vector spaces]] and composition is $k$-bilinear. A one-object $\mathbf{Vect}_k$-category is precisely a $k$-algebra: the single hom-object is the underlying vector space, composition is the multiplication, and the identity $k \to \mathcal{C}(\star,\star)$ is the unit of the algebra. So "$k$-algebra = one-object $k$-linear category" is the linear analogue of "monoid = one-object category".

**Is an instance — $\mathbf{Cat}$-enrichment is a 2-category.** With $\mathcal{V} = (\mathbf{Cat}, \times, \mathbf{1})$, the hom-objects $\mathcal{C}(A,B)$ are *categories*, composition is a functor, and the axioms are strict equalities of functors — this is exactly a strict [[Def - 2-Category and Bicategory|2-category]]. The hom-category's objects are 1-cells and its morphisms are 2-cells. This is the link between this page and §H.1.

**Is an instance — $\mathbf{sSet}$-enrichment is a simplicial category.** With $\mathcal{V} = (\mathbf{sSet}, \times, \Delta^0)$, the hom-objects are [[Def - Simplicial Set|simplicial sets]] — combinatorial spaces. A category enriched in $\mathbf{sSet}$ is a **simplicial category**, and it is one of the oldest models of an $\infty$-category: the hom-spaces record the higher morphisms, and composition is strictly associative but the hom-objects are spaces. This is the forward link to quasi-categories.

**Is NOT an instance — a non-bilinear "composition".** Suppose you take abelian groups as hom-objects but define composition by a map $\mathcal{C}(B,C) \times \mathcal{C}(A,B) \to \mathcal{C}(A,C)$ that is additive in the first variable but *not* the second. This is *not* an $\mathbf{Ab}$-enriched category, because enriched composition must be a morphism out of the *tensor product* $\otimes_{\mathbb{Z}}$, which by the universal property of $\otimes$ forces bilinearity in *both* variables. The failure of bilinearity in one slot is exactly the failure to factor through the tensor product, hence the failure to be a $\mathcal{V}$-morphism.

**Calibration check.** Verify that with $\mathcal{V} = \mathbf{Set}$ the enriched unit law $c \circ (1 \otimes j_A) = r$ reduces to the ordinary statement $f \circ 1_A = f$. Check that for Lawvere's $\mathcal{V} = ([0,\infty], \geq, +)$ the associativity axiom is automatic (any inequality between numbers commutes trivially, since $\mathcal{V}$ is a poset and all diagrams in a poset commute). And confirm that a one-object $\mathbf{Vect}_k$-category is a $k$-algebra by writing out what composition and the identity become.

---

# Unlocked by This

> [!tip] Stable ∞-Categories and Spectra *(from Higher Algebra)*
> Enriching in **spectra** — the homotopy-theoretic refinement of [[Def - Abelian Group|abelian groups]], where a "hom" is not a group but a whole spectrum of higher homotopies — produces **stable ∞-categories**. These are the natural home of the **derived category**, of **Tor** and **Ext**, and of homological algebra done coherently; see §H.5.

> [!tip] Weighted Limits and Enriched Yoneda *(from Enriched Category Theory)*
> When $\mathcal{V}$ is monoidal closed, complete, and cocomplete, almost all of ordinary category theory — the [[Thm - The Yoneda Lemma|Yoneda lemma]], [[Def - Adjunction|adjunctions]], (co)limits — lifts to the $\mathcal{V}$-enriched setting, with ordinary limits replaced by **weighted limits**. This is the machinery (Kelly) behind enriched and $\infty$-categorical mathematics.
