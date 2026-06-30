---
type: definition
subject: higher-categories
prereqs:
  - "Def - Simplicial Set"
  - "Def - Kan Complex and the Nerve"
  - "Def - Pullback and Pushout"
  - "Def - Enriched Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A **simplicial space** (equivalently a **bisimplicial set**) is a functor $X : \Delta^{op} \to \mathbf{sSet}$, where $\Delta$ is the **simplex category** (objects the ordinals $[n] = \{0 < 1 < \dots < n\}$, morphisms order-preserving maps) and $\mathbf{sSet}$ is the category of **[[Def - Simplicial Set|simplicial sets]]**. We write $X_n := X([n]) \in \mathbf{sSet}$ for the **space of $n$-simplices**; $X_0$ is the **space of objects** and $X_1$ the **space of morphisms**. The face map $d_1 : X_1 \to X_0$ gives the source, $d_0 : X_1 \to X_0$ the target, and the degeneracy $s_0 : X_0 \to X_1$ the identities. The **spine** of $[n]$ is the chain $0 \to 1 \to \dots \to n$; the **spine inclusion** induces a map $X_n \to X_1 \times_{X_0} X_1 \times_{X_0} \cdots \times_{X_0} X_1$ ($n$ factors, the iterated **[[Def - Pullback and Pushout|fibre product]]** over $X_0$). We write $\simeq$ for a weak equivalence of [[Def - Simplicial Set|simplicial sets]]. This is a compound page: it defines **two** interlocking notions — the Segal category and the complete Segal space — because they are the two bisimplicial models of $(\infty,1)$-categories, introduced together and compared in the comparison theorem, and neither is fully understood without the other. The full registry is on [[Higher Categories — Other Definitions of Weak n-Categories]].

---

# Axiom Motivation

We want a model of an $(\infty,1)$-category — a category whose hom-sets are spaces — that encodes composition as a *property* rather than as chosen structure, so that maps automatically respect it. The cleanest source of such a model is the **nerve**, run one level up. Recall from [[Def - Kan Complex and the Nerve|the nerve construction]] that an ordinary category $\mathcal{C}$ becomes a [[Def - Simplicial Set|simplicial set]] $N\mathcal{C}$ with $N\mathcal{C}_n =$ chains of $n$ composable arrows, and that a simplicial set is a nerve exactly when each $N\mathcal{C}_n$ *is* the set of $n$-chains, i.e. when the canonical map $N\mathcal{C}_n \to N\mathcal{C}_1 \times_{N\mathcal{C}_0} \cdots \times_{N\mathcal{C}_0} N\mathcal{C}_1$ is a *bijection*. That bijection is the **Segal condition** for ordinary categories: "an $n$-simplex is exactly a string of $n$ composable arrows". The whole idea of this page is to take that condition and weaken "bijection" to "weak equivalence" — because in the [[Def - Homotopy|homotopy]]-theoretic world the right notion of "exactly determined" is "determined up to a contractible space of choices".

So suppose we record our $(\infty,1)$-category as a **simplicial space** $X$, with $X_0$ the space of objects, $X_1$ the space of morphisms, $X_n$ the space of $n$-chains, and the simplicial structure giving sources, targets, composition data, and degeneracies. We impose the **Segal condition**: the spine map $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ is a weak equivalence for all $n \ge 2$. Read this slowly. The right-hand side is the space of *strings* of $n$ composable morphisms; the left-hand side is the space of *$n$-simplices*. The condition says these two spaces are the same up to homotopy. The $n = 2$ case is the heart: $X_2 \simeq X_1 \times_{X_0} X_1$ says "a pair of composable morphisms determines, up to a contractible space of choices, a $2$-simplex", and a $2$-simplex has a long edge — the composite. So *composition exists and is homotopy-unique*, and we never had to pick a composition operation. This is exactly "composition as a property".

Why must the Segal map be a *weak equivalence* and not an isomorphism? If we demanded an isomorphism we would be back at the strict nerve of a category enriched in spaces — a simplicial category — which is rigid and forces strictly associative composition. The point of the homotopy-theoretic models is to *avoid* that rigidity; the weak-equivalence version is what lets the composite be defined only up to higher homotopy, which is honest about how composition behaves for spaces. Drop the Segal condition entirely and $X$ is just an arbitrary bisimplicial set with no categorical meaning — $X_2$ would carry no relation to composable pairs, so there would be no composition at all.

Now the two definitions diverge on the treatment of *objects*, and this is the crux. There are two defects a bare Segal space can have. First, $X_0$ might not be discrete even when we want a model whose objects form a set — the **Segal category** fixes this by *requiring $X_0$ to be a discrete set*. This is the more rigid choice and is the natural target when comparing with simplicial categories, whose objects form a set. Second, and more importantly, even with $X_0$ a space, $X_0$ might carry *too few* paths: two objects can be **equivalent** (connected by a morphism that is invertible up to homotopy) without being connected by a path in $X_0$. Then the homotopy theory is wrong — the localisation that should identify equivalent objects actually changes $X$. Rezk's **completeness** condition repairs this by demanding that $X_0$ (objects) match $X^{\mathrm{heq}}_1$ (the space of self-equivalences) via the degeneracy: *every equivalence is, up to homotopy, an identity*, so equivalent objects are connected by a path. A **complete Segal space** is a Segal space satisfying completeness. Without completeness the model has redundant, non-invariant data; this is precisely the "drop completeness and still call equivalences invertible" illegal operation on the parent page.

The two definitions are thus two ways to cure the object-redundancy of a Segal space — *discretise* the objects (Segal category) or *complete* them (complete Segal space) — and the comparison theorem says both cures yield the same homotopy theory.

---

# The Definition

Let $X : \Delta^{op} \to \mathbf{sSet}$ be a simplicial space.

**Segal space.** $X$ is a **Segal space** if for every $n \ge 2$ the **Segal map** (the spine inclusion)
$$
\xi_n : X_n \longrightarrow \underbrace{X_1 \times_{X_0} X_1 \times_{X_0} \cdots \times_{X_0} X_1}_{n \text{ factors}}
$$
is a weak equivalence of [[Def - Simplicial Set|simplicial sets]], where the fibre product is the homotopy [[Def - Pullback and Pushout|pullback]] (one assumes $X$ Reedy fibrant so that the strict and homotopy fibre products agree). Equivalently $\xi_2$ a weak equivalence suffices, by induction. Source, target, identity, and "a $2$-simplex exhibits a composite of its two short edges as its long edge" are read off from the simplicial structure as in the nerve.

**Segal category.** $X$ is a **Segal category** if it is a Segal space and the space of objects $X_0$ is **discrete** (a set, i.e. a constant simplicial set). Equivalently: a bisimplicial set with $X_0$ discrete such that each Segal map $\xi_n$ is a weak equivalence onto its image (one weakens "weak equivalence" to "the map is a weak equivalence to the homotopy fibre product", since with $X_0$ discrete the fibre product is strict).

**Complete Segal space.** $X$ is a **complete Segal space** (Rezk) if it is a Segal space satisfying the **completeness condition**: the degeneracy map
$$
s_0 : X_0 \longrightarrow X^{\mathrm{heq}}_1
$$
is a weak equivalence, where $X^{\mathrm{heq}}_1 \subseteq X_1$ is the union of those path-components of $X_1$ consisting of **homotopy equivalences** — morphisms invertible in the homotopy category of $X$. Equivalently: the map $X_0 \to X_{\bullet}$ induced by including objects as identities exhibits $X_0$ as the space of "constant" simplices, so that equivalent objects are connected by a path in $X_0$.

In all three, a **functor** is a map of simplicial spaces, and the **homotopy category** $\mathrm{ho}(X)$ has objects $\pi_0 X_0$ and morphisms $\pi_0$ of the relevant mapping space, with composition supplied by the (homotopy-unique) Segal composites.

---

# Categorical / Structural Definition

The structural unifier is **enrichment over spaces**, viewed homotopically. A category **[[Def - Enriched Category|enriched]]** in [[Def - Simplicial Set|simplicial sets]] (a *simplicial category*) has, for each pair of objects, a hom-*space* and a strictly associative composition. Its nerve-like construction produces a simplicial space, and the Segal condition is exactly the homotopical relaxation of "this simplicial space comes from a strictly-composing enriched category". So all three notions on this page are *up-to-homotopy enriched categories over spaces*: the data is the same (objects, mapping spaces, composition), but composition is required to exist and be unique only up to weak equivalence rather than chosen on the nose.

The cleanest way to see the **completeness** condition categorically is through the analogy with the nerve of a *groupoid versus a category*. For an ordinary category, the nerve recovers the category; but a category and its idempotent-completion-or-skeleton can have non-isomorphic nerves while being equivalent. Completeness is the simplicial-space condition that pins down the *correct* equivalence-invariant: it forces the simplicial space to be a fixed point of the localisation that inverts equivalences, so that "equivalent objects" and "objects connected by a path" coincide. This is the homotopical analogue of working with a *skeletal* or *univalent* category, and indeed completeness is the direct categorical ancestor of the **univalence axiom** in homotopy type theory.

---

# Relate to Other Fields / Compression

The Segal condition is the same device that defines a **Segal space** in the original work of Graeme Segal on **infinite loop spaces** and **Γ-spaces**: there, a simplicial space satisfying a Segal-type condition encodes a homotopy-coherent monoid (a single object with a space of endomorphisms), and the special case is exactly the one-object version of a Segal category. So a Segal category is "a many-object homotopy-coherent monoid", precisely as an ordinary category is a many-object monoid. The compression is therefore: *Segal category $=$ category, with sets replaced by spaces and equations replaced by weak equivalences, encoded so that composition is a property*.

**True name:** A complete Segal space is *a homotopy-coherent category whose objects, morphisms, and composition all live in spaces, recorded so that (i) an $n$-chain of composable morphisms is the same datum as an $n$-simplex (Segal), and (ii) equivalent objects are connected by a path (completeness)*. Operationally: "$X_2 \simeq X_1 \times_{X_0} X_1$, plus $X_0 \simeq X^{\mathrm{heq}}_1$". The first equation is composition; the second is invariance.

---

# Examples / Corollaries

**Is an instance — the nerve of an ordinary category, as a discrete simplicial space.** Take an ordinary [[Def - Category|category]] $\mathcal{C}$, form its [[Def - Kan Complex and the Nerve|nerve]] $N\mathcal{C}$ (a [[Def - Simplicial Set|simplicial set]]), and regard it as a simplicial space with each $X_n = N\mathcal{C}_n$ discrete. The Segal maps are *bijections* (the classical Segal condition for categories), hence weak equivalences, so this is a Segal space and a Segal category. It is *not* complete in general: $X_0 = \mathrm{ob}\,\mathcal{C}$ is discrete, but $X^{\mathrm{heq}}_1$ is the set of [[Def - Isomorphism|isomorphisms]], and $s_0$ is an equivalence only if $\mathcal{C}$ has no non-identity isomorphisms. The *classifying-space* / Rezk-completion of $N\mathcal{C}$ is the complete Segal space modelling $\mathcal{C}$ — illustrating that completeness genuinely changes the model.

**Is an instance — the complete Segal space of a simplicial category.** Any category enriched in [[Def - Simplicial Set|simplicial sets]] (mapping spaces, strict composition) yields, by Rezk's classification diagram construction, a complete Segal space with the same homotopy theory. This is one leg of the [[Thm - Comparison of Models for (∞,1)-Categories|comparison theorem]]: simplicial categories map to complete Segal spaces, and the map is part of a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]].

**Is an instance (groupoidal case) — a Kan complex as a constant complete Segal space.** A [[Def - Kan Complex and the Nerve|Kan complex]] $K$, viewed as a simplicial space constant in the new direction (or via its associated complete Segal space), models an $(\infty,1)$-category all of whose morphisms are equivalences — an $\infty$-groupoid, i.e. a space. The Segal condition holds because every horn fills; completeness holds because every morphism is an equivalence so $X^{\mathrm{heq}}_1 = X_1$. This is the homotopy hypothesis seen inside the Segal-space model.

**Is NOT an instance — an arbitrary bisimplicial set.** A general functor $\Delta^{op} \to \mathbf{sSet}$ is *not* a Segal space: with no Segal condition, $X_2$ bears no relation to $X_1 \times_{X_0} X_1$, so there is no composition. It is the bare data with none of the categorical content.

**Is NOT an instance — a Segal space that is not complete.** Take the Segal space whose objects are two points $a, b$ with a single morphism $a \to b$ that is an equivalence, but with $a$ and $b$ in *different* path components of $X_0$. This is a Segal space (composition is fine) but not complete: the equivalence $a \to b$ is not witnessed by a path $a \rightsquigarrow b$ in $X_0$, so $s_0 : X_0 \to X^{\mathrm{heq}}_1$ is not surjective on path components. As an $(\infty,1)$-category it should be equivalent to a point (one object up to equivalence), but the bare Segal space "remembers" two objects — the model is not equivalence-invariant. This is the canonical witness for why completeness is required.

**Calibration check.** Verify that for a Segal space the $n=2$ Segal equivalence $X_2 \simeq X_1 \times_{X_0} X_1$ supplies, on taking $\pi_0$ and a section, a composition on the homotopy category $\mathrm{ho}(X)$. Check that a Segal *category* (discrete $X_0$) has a genuine *set* of objects, whereas a complete Segal *space* has a *space* of objects with the property that its $\pi_0$ classifies objects up to equivalence. If you can explain why the two-object example above fails completeness but the *complete* Segal space modelling the same $(\infty,1)$-category has one path-component of objects, you have understood the completeness condition.

---

# Unlocked by This

> [!tip] $\Theta_n$-Spaces and $(\infty,n)$-Categories *(from Higher Algebra)*
> Iterating the complete-Segal-space construction over Joyal's categories $\Theta_n$ gives Rezk's **$\Theta_n$-spaces**, a model of **$(\infty,n)$-categories**, and the iterated-Segal descendant of the [[Def - Tamsamani-Simpson n-Category|Tamsamani–Simpson]] definition. These are the natural setting for the **cobordism hypothesis**.

> [!tip] The Univalence Axiom *(from Homotopy Type Theory)*
> Rezk's completeness condition — "equivalent objects are connected by a path" — is the categorical prototype of the **univalence axiom** of homotopy type theory, which asserts that equivalent types are equal (connected by a path in the universe). The complete-Segal-space model of $(\infty,1)$-categories is one of the standard semantics in which univalence is interpreted.
