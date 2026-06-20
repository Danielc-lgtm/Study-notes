---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Tamsamani-Simpson n-Category"
  - "Def - Segal Category and Complete Segal Space"
  - "Def - 2-Category and Bicategory"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Unwind the $n = 2$ case of the **[[Def - Tamsamani-Simpson n-Category|Tamsamani–Simpson]]** definition and show it recovers **bicategories**. Concretely: a Tamsamani–Simpson $2$-category is a functor $A : \Delta^{op} \to \mathbf{Cat}$ (a simplicial object in categories) with $A_0$ a *discrete* category (a set) and Segal maps $A_m \to A_1 \times_{A_0} \cdots \times_{A_0} A_1$ that are *equivalences of categories* for $m \ge 2$. Extract from this data: objects, hom-categories, horizontal composition, an associator, and unitors, and verify they satisfy the pentagon and triangle coherences — i.e. assemble a **[[Def - 2-Category and Bicategory|bicategory]]**. This is the level-$2$ sanity check for the geometric/iterated-Segal definitions.

**Recall:**

![[Def - Tamsamani-Simpson n-Category#The Definition]]

A **[[Def - 2-Category and Bicategory|bicategory]]** $\mathcal{B}$ has objects, hom-*categories* $\mathcal{B}(x,y)$, a horizontal composition functor $\circ : \mathcal{B}(y,z) \times \mathcal{B}(x,y) \to \mathcal{B}(x,z)$, identities, and *natural isomorphisms* — the associator $a_{f,g,h}$ and unitors $l_f, r_f$ — satisfying the pentagon and triangle axioms.

The **Segal map** for $A : \Delta^{op} \to \mathbf{Cat}$ sends an object of $A_m$ to its spine in $A_1 \times_{A_0} \cdots \times_{A_0} A_1$; "$\times_{A_0}$" is the pullback of categories over the discrete $A_0$.

---

# Convergent Strategy

**Problem class:** This is the *level-$2$ sanity check* — the mandatory test that a definition of weak $n$-category recovers bicategories at $n=2$. It is harder than the level-$1$ check because the coherence data (associator, unitors) is now nontrivial and must be *produced from the equivalences*, and the pentagon/triangle must be *verified*, not just stated. The routine is to invert the Segal equivalences (up to coherence) to define composition, and to extract the associator from the $A_3$-level equivalence.

**Assumption pattern:** Two assumptions do the work. First, $A_0$ is *discrete* — so objects form a set and the hom-fibres are genuine categories. Second, the Segal maps are *equivalences of categories* (not isomorphisms) — so composition exists and is associative only up to a *natural isomorphism*, which is exactly the associator of a bicategory. The gap between "isomorphism" (which would give a strict $2$-category) and "equivalence" (which gives a bicategory) is the entire source of the weak coherence.

**Theorem routing:** The route is: the hom-category $\mathcal{B}(x,y)$ is the fibre of $A_1 \to A_0 \times A_0$ over $(x,y)$ (a category, since $A_0$ is discrete). Horizontal composition is the composite $A_1 \times_{A_0} A_1 \xleftarrow{\simeq} A_2 \xrightarrow{d_1} A_1$ — a *pseudo-inverse* of the Segal equivalence followed by the long-edge face. The associator comes from the $m=3$ Segal equivalence $A_3 \simeq A_1\times_{A_0}A_1\times_{A_0}A_1$: the two bracketings are two functors that become naturally isomorphic through $A_3$. The pentagon is the coherence of these natural isomorphisms, which holds because the Segal equivalences are coherent (a consequence of $A$ being a functor on $\Delta$).

**Key decision point:** The non-obvious step is that composition is only defined *up to natural isomorphism*, because inverting an *equivalence* of categories requires choosing a pseudo-inverse, and different choices differ by natural isomorphism. The associator is not an afterthought patched on; it is *forced* by the fact that the Segal map is invertible only up to equivalence. Recognising "equivalence-not-isomorphism $\Rightarrow$ associator" is the crux.

---

# Legal Operations Used

1. **Operation 1 from the topic page (read the Segal condition as composition).** The hom-categories and horizontal composition are extracted from the Segal maps, read as "composable pairs determine, up to equivalence, a $2$-simplex".

2. **Operation 8 from the topic page (recover the low-dimensional case).** The exercise *is* the level-$2$ truncation of the iterated-Segal definition, the mandatory bicategory sanity check.

3. **Operation 3 from the topic page (contraction / coherence), in geometric form.** The associator and unitors are the coherence cells, here produced as the natural isomorphisms witnessing that the Segal maps are equivalences.

---

# Hints

> [!note]- Hint 1
> Where do the hom-*categories* of the bicategory come from? $A_1$ is a category, and it maps to $A_0 \times A_0$ (source, target). Since $A_0$ is discrete, the fibre over a pair $(x,y)$ is a category — that is $\mathcal{B}(x,y)$, and its morphisms are the $2$-cells.

> [!note]- Hint 2
> Horizontal composition wants a functor $A_1 \times_{A_0} A_1 \to A_1$. You have $d_1 : A_2 \to A_1$ (the long edge) and the Segal equivalence $A_2 \xrightarrow{\simeq} A_1 \times_{A_0} A_1$. Compose $d_1$ with a *pseudo-inverse* of the Segal equivalence. Why is the pseudo-inverse only defined up to natural isomorphism?

> [!note]- Hint 3
> The associator compares $(h\circ g)\circ f$ with $h\circ(g\circ f)$. Both are built from two applications of composition, i.e. from $A_3$ via two different pairs of faces. The $m=3$ Segal equivalence $A_3 \simeq A_1\times_{A_0}A_1\times_{A_0}A_1$ exhibits a single $A_3$-object over a triple, and the two bracketings are two functors out of it that the equivalence makes naturally isomorphic.

> [!note]- Hint 4
> The pentagon is a statement about *four* composable $1$-cells, so it lives at the $A_4$ level. Coherence of the Segal equivalences across $\Delta$ (they are induced by the simplicial structure, which is functorial) forces the five associator-isomorphisms to compose to the identity. You do not check the pentagon by hand on cells; you derive it from the functoriality of $A$ on $\Delta$.

---

# Solution

The extraction has four parts. Step 1 produces objects and hom-categories. Step 2 produces horizontal composition from the Segal equivalence. Step 3 produces the associator and unitors. Step 4 derives the pentagon and triangle from functoriality on $\Delta$.

**Step 1: objects and hom-categories.**

> [!note]- Derivation
> Objects: $\mathrm{ob}\,\mathcal{B} := A_0$ (a set, since $A_0$ is discrete). $1$-cells and $2$-cells: $A_1$ is a category; its *objects* are the $1$-cells of $\mathcal{B}$ and its *morphisms* are the $2$-cells. The functor $(d_1, d_0) : A_1 \to A_0 \times A_0$ assigns source and target; because $A_0$ is discrete, the fibre
> $$\mathcal{B}(x,y) := (d_1,d_0)^{-1}(x,y)$$
> is a genuine category — objects are $1$-cells $x \to y$, morphisms are $2$-cells between them, with vertical composition the composition in $A_1$. The identity $1$-cell $\mathrm{id}_x$ is $s_0(x) \in A_1$.

**Step 2: horizontal composition.**

> [!note]- Derivation
> The Segal map $\xi_2 : A_2 \xrightarrow{\simeq} A_1 \times_{A_0} A_1$ is an *equivalence of categories*. Choose a pseudo-inverse $\xi_2^{-1}$ (a functor with $\xi_2 \xi_2^{-1} \cong \mathrm{id}$ and $\xi_2^{-1}\xi_2 \cong \mathrm{id}$; it exists because $\xi_2$ is an equivalence, and is unique up to natural isomorphism). Horizontal composition is
> $$\circ \;:=\; d_1 \circ \xi_2^{-1} : A_1 \times_{A_0} A_1 \longrightarrow A_1,$$
> a functor sending a composable pair $(f,g)$ to the long edge of (a chosen $2$-simplex on) its spine. Because it involves $\xi_2^{-1}$, it is well-defined only up to natural isomorphism — and that ambiguity is exactly where the bicategory's weakness will live. It is a *functor* of the hom-categories, so it acts on $2$-cells too: this is horizontal composition of $2$-cells (whiskering and the interchange built in).

**Step 3: associator and unitors.**

> [!note]- Derivation
> *Associator.* Consider three composable $1$-cells $f, g, h$ and the Segal equivalence $\xi_3 : A_3 \xrightarrow{\simeq} A_1\times_{A_0}A_1\times_{A_0}A_1$. The two bracketings are the two functors
> $$(f,g,h) \mapsto (h\circ g)\circ f \quad\text{and}\quad (f,g,h)\mapsto h\circ(g\circ f),$$
> each obtained by applying $\circ$ twice using different faces of an $A_3$-object. Both factor through the single object $\xi_3^{-1}(f,g,h) \in A_3$ via the face maps $d_i : A_3 \to A_2$, and the simplicial identities together with the equivalences $\xi_2, \xi_3$ supply a *natural isomorphism*
> $$a_{f,g,h} : (h\circ g)\circ f \;\xrightarrow{\ \cong\ }\; h\circ(g\circ f)$$
> in $\mathcal{B}(x,w)$. It is an isomorphism (not just a morphism) because the comparison is built from the invertible coherence isomorphisms of the equivalences $\xi_2, \xi_3$. *Unitors.* The degeneracies $s_0, s_1 : A_1 \to A_2$ exhibit $\mathrm{id}\circ f$ and $f\circ\mathrm{id}$, and the simplicial identities $d_1 s_0 = d_1 s_1 = \mathrm{id}$ give natural isomorphisms $l_f : \mathrm{id}\circ f \cong f$ and $r_f : f\circ\mathrm{id}\cong f$.

**Step 4: pentagon and triangle.**

> [!note]- Derivation
> The pentagon concerns four composable $1$-cells and lives at the $A_4$ level. The five associator-isomorphisms in the pentagon are all induced from face maps $A_4 \to A_3 \to A_2$ applied to a single $A_4$-object $\xi_4^{-1}(f,g,h,k)$, together with the coherence isomorphisms of the Segal equivalences. Because $A$ is a *functor* on $\Delta$, these face maps satisfy the simplicial identities *strictly*, and the coherence isomorphisms of an adjoint equivalence satisfy the triangle identities; the composite of the five associators around the pentagon therefore equals the identity natural isomorphism. The triangle axiom (relating $a$ to the unitors) is the analogous $A_3$-level statement using $s_0, s_1$. Thus all bicategory coherences hold, and $\mathcal{B}$ is a [[Def - 2-Category and Bicategory|bicategory]]. (Conversely, every bicategory yields a Tamsamani–Simpson $2$-category by its nerve-in-categories, and Tamsamani proved the two constructions are mutually inverse up to equivalence.)

> [!note]- Complete formal solution
> Let $A : \Delta^{op} \to \mathbf{Cat}$ be a Tamsamani–Simpson $2$-category: $A_0$ discrete, $\xi_m : A_m \xrightarrow{\simeq} A_1\times_{A_0}\cdots\times_{A_0}A_1$ for $m \ge 2$.
>
> **Objects/homs:** $\mathrm{ob}\,\mathcal{B} = A_0$; $\mathcal{B}(x,y) =$ fibre of $(d_1,d_0):A_1\to A_0\times A_0$ over $(x,y)$, a category ($1$-cells $=$ objects, $2$-cells $=$ morphisms, vertical composition from $A_1$); $\mathrm{id}_x = s_0 x$.
>
> **Horizontal composition:** $\circ = d_1\circ\xi_2^{-1} : A_1\times_{A_0}A_1 \to A_1$, a functor (well-defined up to natural iso, since $\xi_2$ is an equivalence).
>
> **Coherence:** the $A_3$-Segal equivalence yields a natural isomorphism $a_{f,g,h} : (h\circ g)\circ f \cong h\circ(g\circ f)$; degeneracies $s_0, s_1$ yield unitors $l_f, r_f$. The pentagon and triangle follow from the strict simplicial identities of the functor $A$ on $\Delta$ together with the triangle identities of the (adjoint) Segal equivalences. Hence $\mathcal{B}$ is a bicategory.
>
> **Converse:** a bicategory's nerve-in-categories is a Tamsamani–Simpson $2$-category; the two are mutually inverse up to equivalence (Tamsamani). $\blacksquare$

---

# Key Takeaways

**Equivalence-not-isomorphism in the Segal map is the source of the associator.** This is the single deepest takeaway and the reason the level-$2$ check is genuinely harder than level $1$. If the Segal maps were *isomorphisms* of categories, composition would be associative on the nose and you would get a strict $2$-category. Because they are only *equivalences*, inverting them requires a pseudo-inverse, well-defined only up to natural isomorphism, and that natural isomorphism *is* the associator. So the weakness of the bicategory is not added by hand — it is exactly the slack between "isomorphism" and "equivalence" in the Segal condition. The trigger is "a Segal/spine map that is an equivalence rather than an iso", and the reaction is "composition is associative only up to a natural isomorphism — there will be an associator, and it will need to satisfy a pentagon".

**Coherence laws are derived from functoriality on $\Delta$, not checked cell-by-cell.** A novice would try to verify the pentagon by chasing $2$-cells, which is hopeless. The correct move is to observe that all the associators in the pentagon descend from a *single* object at the next simplicial level ($A_4$), pushed through face maps that satisfy the simplicial identities *strictly* because $A$ is an honest functor on $\Delta$. The strictness of the simplicial structure, combined with the coherence (triangle identities) of the Segal equivalences, *forces* the pentagon. This is the recurring payoff of the simplicial/geometric definitions: the infinite list of coherence laws is generated by the single fact that the data is a functor on $\Delta$ satisfying Segal conditions, so you never write the laws down — you derive them. The same mechanism gives the coherences in [[Def - Quasi-Category|quasi-categories]] and complete Segal spaces.

**The level-$2$ check certifies that the iterated-Segal idea is correct, and its converse certifies it is conservative.** Recovering bicategories — and recovering *all* of them, via the converse — is what licenses trusting the Tamsamani–Simpson definition at higher $n$. Several proposed definitions of weak higher category passed level $1$ but stumbled at level $2$ (getting the coherences wrong, or recovering only strict $2$-categories); passing level $2$ with the *correct* weak coherences is the real evidence of correctness. When you meet a new geometric definition of weak $n$-category, this is the test that matters most: not "does it give categories" (easy) but "does it give *bicategories*, with a genuine associator satisfying the pentagon" (hard, and decisive). The converse — every bicategory arises — then upgrades "models bicategories" to "is equivalent to bicategories", the conservativity that makes the higher definition a true extension of the classical one.
