---
type: topic
subject: higher-categories
chapter: "H.1-H.5"
title: "Higher Categories — 2-Categories, Enrichment, and Quasi-Categories"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

Throughout this chapter we work one dimension above ordinary category theory, so two conventions are worth stating before the symbols. First, **composition is read right-to-left** in the strict settings ($g \circ f$ means "first $f$, then $g$") but the diagrams of cells are drawn left-to-right; when a 2-cell sits between two 1-cells we name the 1-cells $f$ (source) and $g$ (target). Second, the word "category" silently acquires an adjective as we ascend: a 2-category is *strictly* associative, a bicategory is associative *only up to coherent isomorphism*, and a quasi-category is associative *only up to coherent homotopy*. Each weakening is the price of admitting more examples, and the chapter is organised around exactly that trade.

- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ — ordinary categories; $A, B, C, X, Y$ — objects; $f, g, h$ — morphisms (1-cells)
- $\mathcal{C}(A,B)$ or $\mathrm{Hom}_{\mathcal{C}}(A,B)$ — the hom-set, or in the enriched setting the **hom-object**
- $\mathbf{Cat}$ — the (strict 2-)category of small categories, functors, and natural transformations
- $\mathbf{Set}, \mathbf{Ab}, \mathbf{Vect}_k, \mathbf{Top}, \mathbf{sSet}$ — sets, abelian groups, $k$-vector spaces, topological spaces, simplicial sets
- $\mathcal{B}$ — a bicategory; **0-cells** are objects, **1-cells** are morphisms, **2-cells** are morphisms between parallel 1-cells
- $\alpha, \beta, \gamma$ — 2-cells; $\circ$ — **vertical** composition of 2-cells; $\ast$ — **horizontal** composition of 2-cells (and of 1-cells)
- $a_{f,g,h}$ — the **associator** 2-isomorphism $(h \ast g) \ast f \cong h \ast (g \ast f)$; $l_f, r_f$ — left and right **unitors**
- $(\mathcal{V}, \otimes, I)$ — a monoidal category: the base of enrichment, with tensor $\otimes$ and unit object $I$
- $\mathcal{C}(A,B) \in \mathcal{V}$ — the hom-object of a $\mathcal{V}$-enriched category
- $\Delta$ — the **simplex category**: objects the nonempty finite ordinals $[n] = \{0 < 1 < \dots < n\}$, morphisms order-preserving maps
- $d^i, s^i$ — cofaces and codegeneracies in $\Delta$; $d_i, s_i$ — the induced **face** and **degeneracy** maps in a simplicial set
- $X : \Delta^{op} \to \mathbf{Set}$ — a simplicial set; $X_n = X([n])$ — the set of **$n$-simplices**
- $\Delta^n = \Delta(-, [n])$ — the standard $n$-simplex (the representable simplicial set); $|\Delta^n|$ — its topological realisation
- $\Lambda^n_i \subseteq \Delta^n$ — the **$i$th horn**, the union of all faces of $\Delta^n$ except the $i$th; **inner** if $0 < i < n$, **outer** if $i = 0$ or $i = n$
- $N(\mathcal{C})$ — the **nerve** of a category $\mathcal{C}$; $|{-}|$ — geometric realisation; $\mathrm{Sing}$ — the singular nerve
- $\mathrm{ho}(\mathcal{D})$ — the **homotopy category** of a quasi-category $\mathcal{D}$
- $\dashv$ — "is left adjoint to"; $\simeq$ — equivalence / weak equivalence; $\cong$ — isomorphism

---

# Motivation

Here is the entire chapter in one sentence: a higher category is what you get when "the morphisms between two objects" stop being a set and start being a structured object — a category, an abelian group, a space — so that there are morphisms between morphisms, and composition holds only up to those higher morphisms. Ordinary category theory packages mathematical structure by recording objects and the maps between them. But over and over the maps between maps are themselves interesting: between two functors sit natural transformations, between two continuous maps sit homotopies, between two chain maps sit chain homotopies. The moment you take those seriously, a category is no longer the right home, because a category only knows how to compose along one dimension. You need a place where you can compose 1-cells end-to-end *and* compose 2-cells, both vertically (stacking homotopies) and horizontally (whiskering them along maps). That place is a **2-category**, and the most important example is $\mathbf{Cat}$ itself.

There is a second, deeper pressure, and it is the real reason this chapter exists. In a 2-category we still demand that 1-cells compose *strictly* associatively. For algebra that is fine — functor composition is associative on the nose. But for geometry it is a lie. Concatenate three paths $\alpha, \beta, \gamma$ in a space: $(\alpha \cdot \beta) \cdot \gamma$ and $\alpha \cdot (\beta \cdot \gamma)$ are *different parametrised paths*, equal only after a reparametrisation — that is, after a homotopy. The composite of two paths is not a single path at all; it is a *contractible space of choices*. Insisting on a single strict composite throws this structure away, and with it the homotopy type of the space. The fix is to let composition be defined only up to coherent higher cells, and to keep track of all the coherences at once. This chapter builds the two great formalisms for doing so: at level two, **bicategories**, where associativity is weakened to a natural isomorphism (the associator) satisfying a pentagon; and at level infinity, **quasi-categories**, where composition is encoded not by an operation at all but by the *fillability* of certain horns in a simplicial set.

The conceptual backbone, which the whole chapter circles back to, is a single dial turned in three positions:

$$
\underbrace{\text{composition is a unique value}}_{\text{ordinary category}}
\;\;\longrightarrow\;\;
\underbrace{\text{composition is unique up to coherent isomorphism}}_{\text{bicategory}}
\;\;\longrightarrow\;\;
\underbrace{\text{composition exists, unique up to coherent homotopy}}_{\infty\text{-category}}.
$$

The cleanest statement of where ordinary categories sit on this dial is the punchline of §H.3–H.4: a simplicial set is the nerve of a category exactly when every inner horn has a *unique* filler, and it is a quasi-category exactly when every inner horn has *some* filler. Categories are the "unique" case; $\infty$-categories are the "exists" case. That one swap — from "the composite" to "a composite, well-defined up to a contractible space of choices" — is the entire content of the homotopy-theoretic revolution in category theory, and §H.5 explains why it is forced on you the moment you take spaces seriously.

Tying the two halves together is **enrichment** (§H.2), the abstraction of "hom-sets are richer than sets". A 2-category is precisely a category enriched in $\mathbf{Cat}$; a category whose hom-objects are spaces (a simplicial category) is one of the oldest models of an $\infty$-category; and the same definition, run over the monoidal category $([0,\infty], \geq, +)$, makes a metric space into a category. Enrichment is the hinge: it is how "the homs are categories" (giving 2-categories) and "the homs are spaces" (giving $\infty$-categories) become two instances of one idea.

This chapter assumes you are fluent in ordinary category theory: categories, functors, natural transformations and the functor category (Chapter I), the Yoneda embedding and presheaves (Chapter II), limits and colimits (Chapter III), adjunctions (Chapter IV), and monoidal categories (Chapter V). From outside category theory it leans on the fundamental group and homotopy of paths, and on the singular simplices of a space; both are recalled at point of use. No prior exposure to simplicial sets or $\infty$-categories is assumed — that is what we are building.

---

# Concept Map

## §H.1 2-Categories and Bicategories

- **[[Def - 2-Category and Bicategory]]**
	- A **2-category** is a category enriched in $\mathbf{Cat}$: it has 0-cells (objects), 1-cells (morphisms), and 2-cells (morphisms between parallel 1-cells), with vertical composition $\circ$ and horizontal composition $\ast$ of 2-cells, all *strictly* associative and unital. A **bicategory** weakens the associativity and unit laws *of 1-cells* to coherent invertible 2-cells — the associator $a$ and unitors $l, r$ — subject to a pentagon and a triangle axiom. The motivating 2-category is $\mathbf{Cat}$, with categories as 0-cells, [[Def - Functor|functors]] as 1-cells, and [[Def - Natural Transformation|natural transformations]] as 2-cells. A bicategory with one object is exactly a [[Def - Monoidal Category|monoidal category]].

- **[[Thm - The Interchange Law]]**
	- In any 2-category or bicategory the two ways of composing a $2\times 2$ grid of 2-cells agree: $(\beta' \ast \beta) \circ (\alpha' \ast \alpha) = (\beta' \circ \alpha') \ast (\beta \circ \alpha)$. This is just functoriality of horizontal composition, but it has a startling consequence — the **Eckmann–Hilton argument**: two unital operations satisfying interchange on a shared unit must coincide and be commutative. Hence the 2-cells of a one-object, one-1-cell bicategory form a commutative monoid, and $\pi_2$ of a space is abelian.

> [!tip] Unlocked: (∞,n)-Categories *(from Higher Category Theory)*
> Iterating "morphisms between morphisms" past dimension two gives **(∞,n)-categories**: $\infty$-categories in which all cells above dimension $n$ are invertible. The cases $n = 0$ (spaces / **∞-groupoids**), $n = 1$ (the [[Def - Quasi-Category|quasi-categories]] of §H.4), and the symmetric monoidal $(\infty, n)$-categories that appear in **the cobordism hypothesis** are the load-bearing ones for modern topology and **TQFT**.

> [!note] Exercise Index — §H.1
> [[Exercise Index - §H.1 2-Categories and Bicategories]]

- **[[Ex - Cat is a 2-category]]** (⭐⭐)
	- Verify in full that small categories, functors, and natural transformations form a strict 2-category: identify vertical and horizontal composition of natural transformations and check the interchange law.

- **[[Ex - A monoidal category is a one-object bicategory]]** (⭐⭐⭐)
	- Show that a one-object bicategory $\mathcal{B}$ with unique object $\star$ is the same data as a [[Def - Monoidal Category|monoidal category]]: 1-cells become objects, horizontal composition becomes $\otimes$, the associator and unitors transport directly, and pentagon/triangle match.

- **[[Ex - Pasting and the interchange law]]** (⭐⭐)
	- Compute a pasting diagram of 2-cells two different ways and confirm the answers agree, isolating exactly where the interchange law is used.

## §H.2 Enriched Categories

- **[[Def - Enriched Category]]**
	- For a [[Def - Monoidal Category|monoidal category]] $(\mathcal{V}, \otimes, I)$, a **$\mathcal{V}$-category** $\mathcal{C}$ has objects, a **hom-object** $\mathcal{C}(A,B) \in \mathcal{V}$ for each pair, composition morphisms $\mathcal{C}(B,C) \otimes \mathcal{C}(A,B) \to \mathcal{C}(A,C)$ in $\mathcal{V}$, and identities $I \to \mathcal{C}(A,A)$, satisfying associativity and unit laws drawn as commuting diagrams in $\mathcal{V}$. Specialising $\mathcal{V}$ recovers a zoo: $\mathbf{Set}$-enrichment is ordinary category theory, $\mathbf{Ab}$-enrichment is preadditive categories, $\mathbf{Vect}_k$-enrichment is $k$-linear categories, $\mathbf{Cat}$-enrichment is 2-categories, and enrichment over $([0,\infty], \geq, +)$ is — astonishingly — a metric space.

> [!tip] Unlocked: Stable ∞-Categories and Spectra *(from Higher Algebra)*
> Enriching in a category of **spectra** (the homotopy-theoretic analogue of abelian groups) produces **stable ∞-categories**, where every object has a loop/suspension and mapping objects are themselves spectra. This is the natural home of **derived categories**, **Tor** and **Ext**, and the entire apparatus of homological algebra done $\infty$-categorically — see §H.5.

> [!note] Exercise Index — §H.2
> [[Exercise Index - §H.2 Enriched Categories]]

- **[[Ex - An Ab-enriched category is a preadditive category]]** (⭐⭐)
	- Unwind the definition of an $\mathbf{Ab}$-enriched category and show it is exactly a category in which each hom-set is an [[Def - Abelian Group|abelian group]] and composition is bilinear.

- **[[Ex - A metric space is a Lawvere-enriched category]]** (⭐⭐⭐)
	- Take $\mathcal{V} = ([0,\infty], \geq, +, 0)$ as a monoidal poset and show a $\mathcal{V}$-category with $\mathcal{C}(a,b) = d(a,b)$ is a (generalised) metric space: composition is the triangle inequality, identities are $d(a,a) = 0$.

- **[[Ex - Vect-enriched categories]]** (⭐⭐)
	- Show that a $\mathbf{Vect}_k$-enriched category is a $k$-linear category, and identify the one-object case as a $k$-algebra; recall hom-objects are [[Def - Vector Space|vector spaces]] and composition is bilinear.

## §H.3 Simplicial Sets and Kan Complexes

- **[[Def - Simplicial Set]]**
	- The **simplex category** $\Delta$ has the nonempty finite ordinals $[n] = \{0 < 1 < \dots < n\}$ as objects and order-preserving maps as morphisms, generated by cofaces $d^i$ and codegeneracies $s^i$. A **simplicial set** is a [[Def - Presheaf|presheaf]] $X : \Delta^{op} \to \mathbf{Set}$; one writes $X_n = X([n])$ for the $n$-simplices, with face maps $d_i$ and degeneracy maps $s_i$. The representable $\Delta^n = \Delta(-,[n])$ is the standard $n$-simplex, and the **horn** $\Lambda^n_i \subseteq \Delta^n$ is the union of all faces but the $i$th.

- **[[Def - Kan Complex and the Nerve]]**
	- A **Kan complex** is a simplicial set with the right lifting property against *all* horn inclusions $\Lambda^n_i \hookrightarrow \Delta^n$, $0 \le i \le n$: every horn has a (not necessarily unique) filler. The **nerve** $N(\mathcal{C})$ of a [[Def - Category|category]] has $N(\mathcal{C})_n = \mathrm{Fun}([n], \mathcal{C})$, the strings of $n$ composable arrows; faces compose or drop, degeneracies insert identities. The **inner horns** are the $\Lambda^n_i$ with $0 < i < n$, exactly the horns whose filling encodes composition. (Compound page: defines Kan complex, nerve, and inner horn.)

> [!tip] Unlocked: Model Categories *(from Quillen's Homotopy Theory — Chapter M)*
> The right lifting property packaged in the Kan condition is the local face of a global structure: **model categories** axiomatise homotopy theory through interacting classes of cofibrations, fibrations, and weak equivalences defined by exactly such lifting properties. Simplicial sets carry the **Kan–Quillen model structure** whose fibrant objects are precisely the Kan complexes — see the Model Categories chapter.

> [!note] Exercise Index — §H.3
> [[Exercise Index - §H.3 Simplicial Sets and Kan Complexes]]

- **[[Ex - The simplex category and the standard simplices]]** (⭐⭐)
	- Work out the cosimplicial identities for $d^i, s^i$, and describe $\Delta^n$ and the horn $\Lambda^n_i$ explicitly by their non-degenerate simplices.

- **[[Ex - The nerve of a linear order]]** (⭐⭐)
	- Show that the nerve of the poset $[n]$ (as a category) is $\Delta^n$, so the standard simplices are nerves of the finite ordinals, and identify the simplices of $N([n])$ with order-preserving tuples.

- **[[Ex - Simplicial sets form a presheaf category]]** (⭐⭐)
	- Observe $\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ is a [[Def - Presheaf|presheaf]] category, hence complete and cocomplete with limits and colimits computed pointwise ([[Thm - Limits in Set and in Functor Categories]]).

## §H.4 Quasi-Categories as a Model for ∞-Categories

- **[[Def - Quasi-Category]]**
	- A **quasi-category** (synonyms: weak Kan complex, $\infty$-category in Lurie's sense) is a simplicial set in which every *inner* horn $\Lambda^n_i$, $0 < i < n$, has a filler — not necessarily unique. Its 0-simplices are objects, 1-simplices are morphisms, and a 2-simplex with edges $f, g, h$ exhibits $h$ as *a* composite $g \circ f$. A functor of $\infty$-categories is just a map of simplicial sets. This is the Boardman–Vogt / Joyal / Lurie definition; relaxing "unique filler" to "some filler" is the entire step from categories to $\infty$-categories.

- **[[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers]]**
	- The nerve $N : \mathbf{Cat} \to \mathbf{sSet}$ is fully faithful, and a simplicial set is isomorphic to a nerve $N(\mathcal{C})$ if and only if every inner horn has a *unique* filler. So ordinary categories are precisely the simplicial sets with unique inner-horn fillers; [[Def - Quasi-Category|quasi-categories]] relax "unique" to "exists". This is the conceptual heart of the chapter: $\infty$-categories generalise categories by making composition exist but not be unique — defined only up to coherent homotopy.

- **[[Thm - The Homotopy Category of a Quasi-Category]]**
	- The **homotopy category** $\mathrm{ho}(\mathcal{D})$ has the 0-simplices of $\mathcal{D}$ as objects and homotopy classes of 1-simplices as morphisms; composition is read off any 2-simplex, well-defined up to homotopy by inner-horn filling. For a nerve, $\mathrm{ho}(N(\mathcal{C})) \cong \mathcal{C}$, and if $\mathcal{D}$ is a Kan complex then $\mathrm{ho}(\mathcal{D})$ is a [[Def - Groupoid|groupoid]]. It is the truncation that forgets all higher cells and keeps only "morphisms up to homotopy".

> [!tip] Unlocked: ∞-Topoi *(from Lurie's Higher Topos Theory)*
> A presheaf of *spaces* on a quasi-category, sheafified, is an object of an **∞-topos** — the $\infty$-categorical analogue of a Grothendieck topos and the setting in which **derived algebraic geometry** and nonabelian cohomology live. The Yoneda lemma, limits, and adjunctions of Chapters II–IV all have $\infty$-categorical upgrades that make this possible.

> [!note] Exercise Index — §H.4
> [[Exercise Index - §H.4 Quasi-Categories as a Model for ∞-Categories]]

- **[[Ex - The nerve of a category is a quasi-category]]** (⭐⭐⭐)
	- Prove that for any category $\mathcal{C}$ the nerve $N(\mathcal{C})$ admits unique fillers for all inner horns, hence is a quasi-category — the special case where composition is honestly unique.

- **[[Ex - Every Kan complex is a quasi-category]]** (⭐⭐)
	- Observe that inner horns are among all horns, so the Kan condition (all horns fill) implies the inner-horn condition; conclude every [[Def - Kan Complex and the Nerve|Kan complex]] is a quasi-category, and identify Kan complexes as the **∞-groupoids**.

- **[[Ex - The homotopy category of a quasi-category]]** (⭐⭐⭐)
	- Verify that $\mathrm{ho}(\mathcal{D})$ is a well-defined category: homotopy of 1-simplices is an equivalence relation, composition via 2-simplices is independent of the filler chosen, and associativity follows from a 3-simplex.

## §H.5 Homotopy-Coherent Composition

- **[[Thm - Strictification of Bicategories]]**
	- Every [[Def - 2-Category and Bicategory|bicategory]] is biequivalent to a strict 2-category — the coherence theorem for bicategories, of which [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] for monoidal categories is the one-object case. The failure begins one dimension up: not every tricategory is equivalent to a strict 3-category. So weakness is *removable* at dimension two but *essential* at dimension three.

- **[[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]**
	- Geometric realisation $|{-}| : \mathbf{sSet} \to \mathbf{Top}$ is left [[Def - Adjunction|adjoint]] to the singular nerve $\mathrm{Sing}$, where $|X| = \mathrm{colim}_{\Delta^n \to X} |\Delta^n|$ and $\mathrm{Sing}(X)_n = \mathbf{Top}(|\Delta^n|, X)$ — the set of [[Def - Singular Simplex|singular simplices]]. For any space $X$, $\mathrm{Sing}(X)$ is a Kan complex, the **fundamental ∞-groupoid** of $X$: Kan complexes *are* the $\infty$-groupoids, the content of the homotopy hypothesis.

> [!tip] Unlocked: The Homotopy Hypothesis and Homotopy Type Theory *(from Foundations)*
> That $\infty$-groupoids and spaces are the same thing (**the homotopy hypothesis**, Grothendieck) is the bridge from homotopy theory to logic: in **homotopy type theory** a type *is* an $\infty$-groupoid, equality is a path, and proofs of equality of proofs are higher paths — coherence becomes a foundational principle rather than a bookkeeping nuisance.

> [!note] Exercise Index — §H.5
> [[Exercise Index - §H.5 Homotopy-Coherent Composition]]

- **[[Ex - The singular simplicial set is a Kan complex]]** (⭐⭐⭐)
	- Show $\mathrm{Sing}(X)$ satisfies all horn-filling conditions, using that the horn $|\Lambda^n_i|$ is a retract of $|\Delta^n|$ so any map out of it extends; recall the [[Def - Singular Simplex|singular simplex]] $\mathrm{Sing}(X)_n = \mathbf{Top}(|\Delta^n|, X)$.

- **[[Ex - Inner horn fillers as composition]]** (⭐⭐)
	- Interpret an inner 2-horn $\Lambda^2_1 \to \mathcal{D}$ as "two composable morphisms" and its filler as a choice of composite; explain why the contractibility of the space of fillers is the right notion of "well-defined up to homotopy".

- **[[Ex - The derived category needs higher categorical machinery]]** (⭐⭐⭐)
	- A motivational exercise: explain why the triangulated/derived category of complexes is *non-functorial* (cones are not canonical) and how an $\infty$-categorical enhancement repairs it.

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of higher category theory chase a handful of recurring goals. The first is **"this familiar gadget is secretly a higher category"**: that categories-functors-natural-transformations form a 2-category, that bimodules form a bicategory, that hom-spaces make a topological category. The second is **"these two definitions of higher category agree"** — the recognition theorems, of which the king is the characterisation of nerves by unique inner-horn fillers; proving an equivalence of formalisms is the bread and butter of the subject because there are so many models. The third is **"this weak structure can (or cannot) be strictified"**: coherence theorems and their limits, telling you when the bookkeeping of associators can be wished away. The fourth is **"composition is well-defined up to coherent homotopy"** — verifying horn-filling, checking that a homotopy category is a genuine category, showing a space of composites is contractible. The fifth is **"this construction is an adjunction / preserves the structure"**: realisation against singular nerve, nerve against homotopy category, identifying left and right adjoints between the worlds of spaces, simplicial sets, and categories. Identify, equate, strictify, fill, adjoin — every problem in the chapter is one of these.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **Enrichment data is given** — hom-objects in some monoidal $\mathcal{V}$ — and the move is to unwind the axioms in $\mathcal{V}$ and recognise a known structure; this is how 2-categories, preadditive categories, $k$-linear categories, and metric spaces all fall out of one definition. **A simplicial set is given by a universal property** — it is representable ($\Delta^n$), a nerve, or a singular complex — and the move is to compute its simplices via Yoneda or via the defining mapping property. **A horn-filling hypothesis is given** (inner only, or all horns) and the move is to translate filling into the existence or uniqueness of composites. **An adjunction is suspected** between two functors relating $\mathbf{sSet}, \mathbf{Top}, \mathbf{Cat}$, and the move is to exhibit a natural hom-set bijection or to recognise one side as a left Kan extension of a cosimplicial object. **A coherence diagram is given** (pentagon, triangle, interchange) and the move is to paste 2-cells and check two routes agree. The recurring routing is: enrichment data routes through "unwind in $\mathcal{V}$" to an identification; a representability or nerve hypothesis routes through Yoneda to a simplex computation; a filling hypothesis routes through the nerve characterisation to a statement about composition. The [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Problem-Solving Strategy|Problem-Solving Strategy]] makes these explicit.

---

# Legal Operations

These are the moves nearly every problem in the chapter is assembled from. When stuck, scan the list and try each. Everything is self-contained.

**Legal operations:**

1. **Unwind an enriched definition in the base $\mathcal{V}$.** Given a $\mathcal{V}$-category, replace each abstract axiom (associativity, unit) by the corresponding commuting diagram *in $\mathcal{V}$* and read off what it says concretely. *Trigger:* you are told "category enriched in $\mathcal{V}$" and asked what it is. *Pattern:* "the composition morphism $\mathcal{C}(B,C) \otimes \mathcal{C}(A,B) \to \mathcal{C}(A,C)$, when $\otimes = +$ and the order is $\geq$, becomes the inequality $d(b,c) + d(a,b) \geq d(a,c)$" — the triangle inequality. See [[Def - Enriched Category]].

2. **Compute the simplices of a simplicial set via its universal property.** $\Delta^n_k = \Delta([k],[n])$ is the set of order-preserving maps (Yoneda); $N(\mathcal{C})_n = \mathrm{Fun}([n],\mathcal{C})$ is the strings of composable arrows; $\mathrm{Sing}(X)_n = \mathbf{Top}(|\Delta^n|, X)$ is the [[Def - Singular Simplex|singular simplices]]. *Trigger:* a simplicial set defined as representable, a nerve, or a singular complex. *Pattern:* never enumerate simplices by hand — read them off the defining mapping property.

3. **Translate horn-filling into a statement about composites.** An inner 2-horn $\Lambda^2_1 \to X$ is a pair of composable 1-simplices; a filler is a composite; uniqueness of fillers means the composite is honest, mere existence means it is defined up to homotopy. *Trigger:* the word "horn", "filler", or "lifting property". *Pattern:* a 3-simplex witnesses associativity, a $\Lambda^3_1$- or $\Lambda^3_2$-filler identifies two composites. See [[Def - Quasi-Category]].

4. **Apply the nerve characterisation.** To decide whether a simplicial set is a category (unique inner fillers), a quasi-category (some inner fillers), or a Kan complex (all fillers), check which horns fill and how uniquely. *Trigger:* "is this simplicial set an $\infty$-category / a nerve / an $\infty$-groupoid?". *Pattern:* unique inner $\Rightarrow$ nerve of a category; some inner $\Rightarrow$ quasi-category; all $\Rightarrow$ Kan. See [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers]].

5. **Paste 2-cells and use interchange.** In a 2-category or bicategory, a pasting diagram of 2-cells can be evaluated by composing in any order consistent with the shapes; the [[Thm - The Interchange Law|interchange law]] guarantees the answers agree. *Trigger:* a grid or string of 2-cells. *Pattern:* compute "rows then columns" and "columns then rows" and equate.

6. **Recognise a one-object case as a monoid-like structure.** A one-object $\mathcal{V}$-category is a monoid in $\mathcal{V}$; a one-object bicategory is a [[Def - Monoidal Category|monoidal category]]; a one-object-one-1-cell bicategory has a commutative monoid of 2-cells (Eckmann–Hilton). *Trigger:* "one object" anywhere. *Pattern:* collapse the object away and read the remaining data as an algebraic structure.

7. **Build an adjunction from a (co)simplicial object.** Any functor $\Delta \to \mathcal{E}$ into a cocomplete category (here $\Delta^n \mapsto |\Delta^n|$) extends to a colimit-preserving "realisation" $\mathbf{sSet} \to \mathcal{E}$ with a right adjoint "singular nerve" $\mathcal{E}(|\Delta^\bullet|, -)$. *Trigger:* a functor relating $\mathbf{sSet}$ to a cocomplete target. *Pattern:* realisation $\dashv$ singular nerve; see [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]].

8. **Pass to the homotopy category to extract an ordinary category.** From any quasi-category $\mathcal{D}$, form $\mathrm{ho}(\mathcal{D})$ by taking 1-simplices modulo homotopy. *Trigger:* you want an ordinary-categorical shadow of an $\infty$-categorical fact. *Pattern:* $\mathrm{ho}(N(\mathcal{C})) \cong \mathcal{C}$, and $\mathrm{ho}$ of a Kan complex is a [[Def - Groupoid|groupoid]]. See [[Thm - The Homotopy Category of a Quasi-Category]].

9. **Strictify when the dimension allows.** Replace a bicategory by a biequivalent strict 2-category (coherence). *Trigger:* a proof that would be cluttered by associators at dimension $\le 2$. *Pattern:* "by [[Thm - Strictification of Bicategories|coherence]] we may assume the bicategory is strict" — but never above dimension two, where it is false.

**Illegal but tempting operations:**

> [!warning] 1. Treating "the composite" of two 1-simplices in a quasi-category as a single thing
> In an ordinary category $g \circ f$ is one morphism; in a [[Def - Quasi-Category|quasi-category]] it is tempting to speak of "the" composite and manipulate it as such. But a filler of the inner horn $\Lambda^2_1$ is only *a* composite, and there are generally many. The clash: in $\mathrm{Sing}(X)$ the composite of two paths is any path homotopic to their concatenation — a whole contractible space of them. The operation becomes legal only after passing to the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]], where composites are taken up to homotopy and uniqueness is restored.

> [!warning] 2. Assuming every weak higher category can be strictified
> [[Thm - Strictification of Bicategories|Coherence]] for bicategories tempts one to believe weakness is always cosmetic. It is not. Already at dimension three there are tricategories not equivalent to any strict 3-category — the **Gray tensor product** and the braiding obstructions are genuine. The repair condition is dimension: strictification of *all* the structure is legal at dimension $\le 2$ and fails from dimension $3$ onward; what survives in general is strictification of associativity *or* of units, but not both at once.

> [!warning] 3. Filling outer horns to get composition
> Inner horns $\Lambda^n_i$ ($0 < i < n$) encode composition, so one is tempted to demand outer-horn ($i = 0$ or $i = n$) fillers too "for symmetry". But requiring outer fillers is a *different and stronger* condition: a simplicial set with all horn fillers is a [[Def - Kan Complex and the Nerve|Kan complex]], an $\infty$-*groupoid*, in which every morphism is invertible. The nerve $N(\mathcal{C})$ fails the outer condition exactly when $\mathcal{C}$ has non-invertible morphisms. Outer filling is legal precisely for groupoids; demanding it of a general $\infty$-category throws away all non-invertible arrows.

> [!warning] 4. Confusing internal and enriched categories
> Given "categories and topology", it is tempting to conflate a *topological category* (enriched in $\mathbf{Top}$: a topology on each hom-set) with an *internal category in $\mathbf{Top}$* (a topology on the whole set of objects and the whole set of arrows). These are different: the enriched version has a discrete set of objects, the internal version topologises objects too. They agree only when the object set is discrete. The distinction matters because $\infty$-categories arise from the *enriched* notion (homs are spaces), not the internal one.

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you decide *which dimension and which model* you are working in, so begin there. Almost every exercise is one of five types, each with a characteristic source and route.

If the problem **hands you enrichment data** — hom-objects in a [[Def - Monoidal Category|monoidal category]] $\mathcal{V}$ — and asks what structure results, you are in an *identification by unwinding* problem, and the route is mechanical: write the composition morphism $\mathcal{C}(B,C) \otimes \mathcal{C}(A,B) \to \mathcal{C}(A,C)$ and the unit $I \to \mathcal{C}(A,A)$, then translate $\otimes$, $I$, and the associativity/unit diagrams into the concrete language of $\mathcal{V}$. Over $\mathbf{Ab}$ this produces "hom-sets are groups, composition bilinear"; over $\mathbf{Vect}_k$, a $k$-linear category; over $\mathbf{Cat}$, a 2-category; over the poset $([0,\infty], \geq, +)$, the triangle inequality of a metric space. The single most useful realisation is that *the axioms do not change — only the category they are interpreted in does* — so the entire difficulty is fluency in reading a diagram inside an unfamiliar $\mathcal{V}$.

If the problem **gives you a simplicial set and asks you to compute or classify it**, the assumption pattern is that the simplicial set is *defined by a universal property* — representable, a nerve, or a singular complex — and the route runs through Yoneda. Never enumerate simplices by hand. For $\Delta^n$, the $k$-simplices are order-preserving maps $[k] \to [n]$, by the Yoneda lemma applied to the representable [[Def - Presheaf|presheaf]]. For $N(\mathcal{C})$, the $n$-simplices are strings of $n$ composable arrows, because $\mathrm{Fun}([n], \mathcal{C})$ unwinds to exactly that. For $\mathrm{Sing}(X)$, they are [[Def - Singular Simplex|singular simplices]] $|\Delta^n| \to X$. Having the simplices in this form, faces and degeneracies are read off as "drop a vertex / compose two arrows" and "repeat a vertex / insert an identity".

If the problem **concerns horn-filling**, decide first whether you are testing *inner* horns (composition) or *all* horns (invertibility). This is the chapter's sharpest fork. To show something is a [[Def - Quasi-Category|quasi-category]], you fill only inner horns, and the canonical instance is [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|the nerve]], where the fill is not just possible but unique. To show something is a [[Def - Kan Complex and the Nerve|Kan complex]] you must fill outer horns too, which is exactly the extra demand that makes every morphism invertible — so Kan complexes are $\infty$-groupoids and arise from spaces, as in [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|$\mathrm{Sing}(X)$]]. The trigger for "this is a quasi-category but not Kan" is the presence of genuinely non-invertible morphisms; the trigger for "this is Kan" is that the simplicial set comes from a space or a groupoid.

If the problem **asks for an adjunction** between two of the categories $\mathbf{sSet}, \mathbf{Top}, \mathbf{Cat}$, the route is almost always the realisation/nerve template: a cosimplicial object $\Delta \to \mathcal{E}$ (a choice of "geometric $n$-simplex" in the target) induces a colimit-preserving realisation with a right-adjoint singular nerve, by the general nonsense of left Kan extension along the Yoneda embedding. Geometric realisation $\dashv \mathrm{Sing}$ is the topological instance; the nerve $\dashv$ the fundamental-category functor is the categorical instance. Recognising the template saves you from constructing the hom-set bijection by brute force.

Finally, a meta-strategy threads through everything: **when composition refuses to be unique, do not force it — keep the higher cells and demand only coherence.** Every difficulty in this chapter is a symptom of insisting on strictness where the mathematics is only weak. The 2-categorical fix is an associator with a pentagon; the $\infty$-categorical fix is a horn-filler with all its higher fillers; the geometric content is that "the composite" is a contractible space of choices, not a point. The single unifying question of the chapter is: *what is the minimal coherence data that lets composition be defined up to homotopy without lying about uniqueness?*

---

# Most Reusable Properties

- **[[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|The nerve characterisation]]**: a simplicial set is $N(\mathcal{C})$ iff inner horns fill *uniquely*. This is the most-used single fact in the chapter because it pins down the exact sense in which $\infty$-categories generalise categories: relax "unique" to "exists". Reach for it whenever you must decide what kind of higher category a simplicial set models, whenever you want to embed ordinary category theory into the simplicial world ($N$ is fully faithful, so $\mathbf{Cat}$ sits inside $\mathbf{sSet}$ as a full subcategory), and whenever you need to know that a construction on quasi-categories restricts correctly to ordinary categories.

- **[[Def - Enriched Category|Enrichment]]**: hom-objects live in a monoidal $\mathcal{V}$, with composition a morphism of $\mathcal{V}$. Its reusability is that it is the *single definition* behind 2-categories ($\mathcal{V} = \mathbf{Cat}$), additive and linear categories ($\mathcal{V} = \mathbf{Ab}, \mathbf{Vect}_k$), metric spaces ($\mathcal{V} = [0,\infty]$), and simplicial categories ($\mathcal{V} = \mathbf{sSet}$). The recognisable setup is "the homs carry extra structure compatible with composition"; the typical use is to import all of category theory wholesale into the enriched setting and to recognise an exotic structure (like a metric space) as a category in disguise.

- **[[Thm - The Interchange Law|The interchange law]]**: $(\beta' \ast \beta) \circ (\alpha' \ast \alpha) = (\beta' \circ \alpha') \ast (\beta \circ \alpha)$. This is the compatibility of the two composition directions, and it is what makes pasting diagrams unambiguous. Its highest-leverage disguised use is the Eckmann–Hilton argument: any two unital operations satisfying interchange on a shared unit coincide and commute — which is *why* $\pi_2$ and all higher homotopy groups are abelian, and why a doubly-degenerate monoidal category is commutative.

- **[[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|Realisation $\dashv$ singular nerve]]** and the fact that $\mathrm{Sing}(X)$ is a Kan complex. This is the bridge between topology and combinatorics: it lets you replace a space by a simplicial set with the same homotopy type, and it certifies that *Kan complexes are $\infty$-groupoids* — the homotopy hypothesis in usable form. Reach for it whenever a homotopy-theoretic question should be made combinatorial, and whenever you need a concrete $\infty$-groupoid to compute with.

- **[[Thm - The Homotopy Category of a Quasi-Category|The homotopy category]] $\mathrm{ho}(\mathcal{D})$**: the ordinary category of objects and morphisms-up-to-homotopy. Its typical use is as the truncation that lets ordinary-categorical intuition survive into the $\infty$-world: composites become unique again, $\mathrm{ho}(N(\mathcal{C})) \cong \mathcal{C}$ recovers the original category, and $\mathrm{ho}$ of a Kan complex is the fundamental [[Def - Groupoid|groupoid]]. It is the safety rail you grab when the higher structure is not what the problem actually needs.

---

# Bridges

1. **Algebraic topology — the fundamental ∞-groupoid replaces $\pi_1$.** Classical algebraic topology assigns to a space $X$ its [[Def - Path-Product and the Fundamental Group|fundamental group]] $\pi_1(X)$ and higher homotopy groups, discarding most of the homotopy type along the way. The singular nerve $\mathrm{Sing}(X)$ does better: it is a [[Def - Kan Complex and the Nerve|Kan complex]] whose 0-simplices are points, 1-simplices are paths, 2-simplices are homotopies of paths, and so on, *retaining all of it*. Its homotopy category is the fundamental groupoid, and its full simplicial structure is the **fundamental ∞-groupoid**. The deep statement, the **homotopy hypothesis**, is that this assignment is an equivalence between spaces (up to weak homotopy equivalence) and $\infty$-groupoids — so an $\infty$-groupoid simply *is* a space, presented combinatorially.

2. **Homological and derived algebra — chain complexes and stable ∞-categories.** A category of chain complexes is naturally enriched in [[Def - Abelian Group|abelian groups]] (and, refined, in simplicial abelian groups), with chain homotopies as 2-cells; this is the [[Def - Enriched Category|$\mathbf{Ab}$-enriched]] / 2-categorical structure of Example 1.4.3 in Leinster. The **derived category** $D(\mathcal{A})$ of an abelian category is obtained by formally inverting the quasi-isomorphisms, and as a mere triangulated category it is badly behaved — the cone of a map is only defined up to non-canonical isomorphism and the construction is non-functorial. The repair, explained in §H.5, is to take the *$\infty$-categorical* (or dg-) enhancement, a **stable ∞-category** whose mapping objects are spaces; there the cone becomes a genuine functor and **Tor**, **Ext**, and derived functors are recovered with all their coherence intact.

3. **Monoidal categories and TQFT — one object up.** A [[Def - Monoidal Category|monoidal category]] is exactly a one-object bicategory, with the tensor product reincarnated as horizontal composition of 1-cells; [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] is then the one-object case of [[Thm - Strictification of Bicategories|bicategorical strictification]]. Pushing this to symmetric monoidal $(\infty, n)$-categories is the language of **topological quantum field theory**: a TQFT is a symmetric monoidal functor from a higher category of cobordisms to a higher category of vector spaces, and **the cobordism hypothesis** classifies such functors by their value on a point. The enrichment and coherence of this chapter are the entry fee.

4. **Foundations and type theory — coherence as a logical principle.** In **homotopy type theory** the homotopy hypothesis is taken as a definition: a type is interpreted as an $\infty$-groupoid, the identity type $\mathrm{Id}_A(x,y)$ as the space of paths from $x$ to $y$, and iterated identity types as higher paths. The coherence data that this chapter tracks by hand — associators, horn-fillers, the contractibility of spaces of composites — becomes the univalence and higher-path structure built into the foundations. The bridge is the same observation made by Voevodsky and the homotopy hypothesis: equality is not a proposition but a space, and managing its higher structure is exactly $\infty$-category theory.

---

# Insights

**The unifying frame: turn one dial, "how unique is composition", and you get the whole hierarchy.** Ordinary categories, bicategories, and $\infty$-categories are not three unrelated theories; they are three settings of a single parameter. In a category, the composite of two morphisms is a *unique value*. In a bicategory, associativity of composition holds only *up to a specified isomorphism* — the associator — and the cost is one coherence law (the pentagon). In a quasi-category, composition is not even an operation: a 2-simplex *exhibits* a composite, there are many such 2-simplices, and the family of them is *contractible*. The single cleanest expression of this is the nerve characterisation: unique inner-horn fillers ⟺ ordinary category; some inner-horn fillers ⟺ $\infty$-category. The entire subject is the study of what coherence data is needed to run category theory once you have moved the dial off "unique".

**The true name of an $\infty$-category is "a simplicial set where composition is defined up to a contractible space of choices".** The official definition — a simplicial set with inner-horn fillers — is the right thing to *check* but the wrong thing to *think*. What you should picture is $\mathrm{Sing}(X)$: objects are points, morphisms are paths, and the composite of two paths is not a path but the contractible space of all paths homotopic to their concatenation, with the 2-simplex as witness. This is why simplicial sets, of all things, model $\infty$-categories: the simplicial identities are precisely the bookkeeping that packages *all* the coherence homotopies — associativity (a 3-simplex), the identification of two composites (a $\Lambda^3_1$-filler), the identification of those identifications (a 4-simplex), and so on without end — into one finite combinatorial gadget. Strict composition is a fiction that picks one point of a contractible space and forgets the rest.

**Eckmann–Hilton is the reason high-dimensional algebra is commutative, and it is a one-line consequence of interchange.** If a set carries two unital binary operations that satisfy the interchange law and share a unit, the two operations are equal and commutative — proved in two lines by inserting units. The payoff is structural and surprising: a one-object, one-1-cell bicategory is a *commutative* monoid of 2-cells; the second homotopy group $\pi_2(X)$, which can be computed as 2-cells in a 2-truncated fundamental groupoid, is therefore abelian, as are all $\pi_n$ for $n \ge 2$. The same argument explains why a "doubly degenerate" monoidal category is symmetric. Whenever you find two compatible compositions sharing a unit, expect commutativity, and expect interchange to be the mechanism.

**Weakness is removable at dimension two and essential from dimension three — and this is not a technicality but the shape of the subject.** [[Thm - Strictification of Bicategories|Coherence for bicategories]] says every bicategory is biequivalent to a strict 2-category, so for most purposes one may pretend associators are identities. It is tempting to extrapolate that all higher weakness is bookkeeping. The extrapolation is false: tricategories are *not* all strictifiable, and the obstruction is genuine (it is detected by braidings, the same phenomenon that makes $\pi_3(S^2) = \mathbb{Z}$). The lesson is that the difficulty of higher category theory is real and grows with dimension; the simplicial models of this chapter are valuable precisely because they sidestep the impossible task of writing down all the coherence laws by hand and replace it with the single, uniform, dimension-independent condition of horn-filling.
