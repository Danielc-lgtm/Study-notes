---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, foundations]
---

# Notation

We write $\mathcal{S} \subseteq \mathcal{C}$ for "$\mathcal{S}$ is a subcategory of $\mathcal{C}$". The associated inclusion [[Def - Functor|functor]] is $\iota : \mathcal{S} \hookrightarrow \mathcal{C}$. A subcategory is **full** or **wide** as defined below. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

A [[Def - Subgroup|subgroup]] is a subset closed under the group operations; a subspace is a subset closed under the linear operations. The analogous notion for a [[Def - Category|category]] is a subcategory: a sub-collection of objects and morphisms that is closed under the categorical operations — composition and identities. The motivation is the same as for any substructure: we constantly want to restrict attention to a part of a category ([[Def - Abelian Group|abelian groups]] among all [[Def - Group|groups]], finite-dimensional vector spaces among all vector spaces, the connected spaces among all spaces) and we need that part to *be a category in its own right*.

What must close? If $\mathcal{S}$ is to be a category under the operations inherited from $\mathcal{C}$, then whenever it contains two composable morphisms it must contain their composite, and whenever it contains an object it must contain that object's identity. **Drop closure under composition** and $\mathcal{S}$ is not a category — there are composable arrows whose composite is missing, the exact failure mode of a "graph with broken composition". **Drop the requirement that identities be present** and again $\mathcal{S}$ fails the [[Def - Category|category]] axioms. These are not arbitrary; they are forced by wanting the inclusion $\iota : \mathcal{S} \to \mathcal{C}$ to be a [[Def - Functor|functor]] that is the identity on the elements it touches.

The interesting subtlety, and the reason this notion needs care, is that there are *two* independent ways a subcategory can be "smaller": it can omit objects, and it can omit morphisms between objects it keeps. A subcategory that keeps **all** the morphisms between the objects it retains is **full** — it is determined entirely by its object-collection, and is the categorical analogue of an "induced subgraph". A subcategory that keeps **all** the objects but possibly omits morphisms is **wide** (or **lluf**). These two notions pull in opposite directions, and most of the confusion about subcategories evaporates once you ask "full or wide?" The inclusion functor is **faithful** always; it is **full** exactly when the subcategory is full.

---

# The Definition

A **subcategory** $\mathcal{S}$ of a [[Def - Category|category]] $\mathcal{C}$ consists of:

- a sub-collection $\mathrm{ob}(\mathcal{S}) \subseteq \mathrm{ob}(\mathcal{C})$ of objects;
- for each pair $A, B \in \mathcal{S}$, a sub-collection $\mathcal{S}(A, B) \subseteq \mathcal{C}(A, B)$ of morphisms;

such that

1. $\mathcal{S}$ is closed under composition: $f \in \mathcal{S}(A, B)$ and $g \in \mathcal{S}(B, C)$ imply $g \circ f \in \mathcal{S}(A, C)$;
2. $\mathcal{S}$ contains all relevant identities: $1_A \in \mathcal{S}(A, A)$ for every $A \in \mathcal{S}$.

The inclusion $\iota : \mathcal{S} \hookrightarrow \mathcal{C}$ is then a faithful [[Def - Functor|functor]].

A subcategory is:

- **full** if $\mathcal{S}(A, B) = \mathcal{C}(A, B)$ for all $A, B \in \mathcal{S}$ — it keeps every morphism between its objects, equivalently the inclusion is a [[Def - Full, Faithful, and Essentially Surjective Functor|full functor]];
- **wide** (or **lluf**) if $\mathrm{ob}(\mathcal{S}) = \mathrm{ob}(\mathcal{C})$ — it keeps every object.

A full subcategory is specified by its objects alone; one writes "the full subcategory of $\mathcal{C}$ on the objects with property $P$".

---

# Relate to Other Fields / Compression

**True name:** *a subcollection of objects and arrows closed under composition and identities — full if it omits only objects, wide if it omits only morphisms.* The compression: a full subcategory is "carve out by a property of objects", a wide subcategory is "restrict to a property of morphisms". The categorical analogue of a subgroup is closest to a wide subcategory (same objects, fewer arrows), while the analogue of an induced substructure (the subspace spanned by chosen basis vectors, the full subgraph on chosen vertices) is a full subcategory.

This distinction recurs whenever one restricts a category. "Spaces and *open* embeddings" is a wide subcategory of $\mathbf{Top}$ (all spaces, fewer maps). "Finite groups" is a full subcategory of $\mathbf{Grp}$ (fewer objects, all homomorphisms between them). Recognizing which kind you are forming tells you immediately whether the inclusion is full and whether the subcategory is determined by its objects.

---

# Examples / Corollaries

**$\mathbf{Ab} \subseteq \mathbf{Grp}$ is full.** The [[Def - Abelian Group|abelian groups]] form a full subcategory of [[Def - Group|groups]]: every group homomorphism between two abelian groups is retained, so $\mathbf{Ab}(A, B) = \mathbf{Grp}(A, B)$ for abelian $A, B$. The inclusion is fully faithful. This is the standard full-subcategory example.

**Finite-dimensional vector spaces $\subseteq \mathbf{Vect}_k$ is full.** $\mathbf{FinVect}_k$ keeps the finite-dimensional [[Def - Vector Space|vector spaces]] and all [[Def - Linear Map|linear maps]] between them — full, determined by its objects. It is [[Def - Equivalence of Categories|equivalent]] to the category $\mathbf{Mat}_k$ of matrices (see the §1.5 exercises).

**A wide, non-full subcategory.** Take all [[Def - Group|groups]] as objects, but as morphisms keep only the **injective** homomorphisms. This is closed under composition (a composite of injections is injective) and contains identities, so it is a subcategory; it is wide (all objects) but not full (it omits the non-injective homomorphisms, e.g. the trivial map $\mathbb{Z} \to \mathbb{Z}$, $n \mapsto 0$). Its inclusion into $\mathbf{Grp}$ is faithful but not full. This is the canonical "restrict the morphisms" example, and it illustrates why wide subcategories cannot be specified by objects alone.

**Is NOT a subcategory.** Take the objects of $\mathbf{Set}$ but keep, as morphisms $A \to B$, only the *surjective* functions — and additionally *omit* the identity on any set with more than one element? No: omitting identities breaks axiom 2. Even keeping identities, the surjections-only collection *is* a wide subcategory (surjections compose to surjections). The genuine non-example: keep two composable functions $f : A \to B$, $g : B \to C$ but omit their composite $g \circ f$. Closure under composition fails, so this is not a subcategory — it is a sub-graph, not a sub-category.

**Calibration check.** Verify that a full subcategory is uniquely determined by which objects it contains, but a wide subcategory is not determined by anything less than its full morphism data. Verify the inclusion functor is always faithful, and full exactly for full subcategories. Confirm you can classify each of "finite groups", "groups and injective homomorphisms", "abelian groups", "all groups and surjective homomorphisms" as full, wide, both, or neither.

---

# Unlocked by This

> [!tip] Reflective and Coreflective Subcategories *(from this subject, Chapter IV)*
> A full subcategory whose inclusion has a left [[Def - Adjunction|adjoint]] is **reflective**; one with a right adjoint is **coreflective**. $\mathbf{Ab} \subseteq \mathbf{Grp}$ is reflective (the reflector is abelianization), and compact-Hausdorff $\subseteq \mathbf{Top}$ is reflective (the reflector is Stone–Čech compactification). Reflective subcategories are the categorical theory of "best nice approximation".

> [!tip] The Skeleton of a Category *(from this subject)*
> A **skeleton** of $\mathcal{C}$ is a full subcategory containing exactly one object from each isomorphism class — it is [[Def - Equivalence of Categories|equivalent]] to $\mathcal{C}$ but has no distinct isomorphic objects. Skeletons make precise the slogan that equivalence "allows iso, not equality" on objects.
