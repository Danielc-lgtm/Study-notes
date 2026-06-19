---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Functor Category"
  - "Def - Monoidal Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

We work one dimension above ordinary categories. A 2-category or bicategory $\mathcal{B}$ has three layers of data: **0-cells** (objects) $A, B, C, \dots$; **1-cells** (morphisms) $f, g, h : A \to B$; and **2-cells** $\alpha, \beta : f \Rightarrow g$ between *parallel* 1-cells (same source and target). We write a 2-cell as $A \overset{f}{\underset{g}{\rightrightarrows}} B$ with $\alpha$ filling the bigon. Composition comes in two flavours: **vertical** composition $\beta \circ \alpha$ of 2-cells $\alpha : f \Rightarrow g$, $\beta : g \Rightarrow h$ (stacking along a shared 1-cell), and **horizontal** composition, written $\ast$, both of 1-cells ($g \ast f$ or $g \circ f$ when no confusion) and of 2-cells along a shared 0-cell. The hom-data $\mathcal{B}(A,B)$ — 1-cells and 2-cells from $A$ to $B$ — forms an ordinary [[Def - Category|category]] under vertical composition. The associator is $a_{f,g,h}$, the unitors $l_f$ (left) and $r_f$ (right). The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

This is a compound page: it defines two interlocking notions — the **2-category** (strict) and the **bicategory** (weak) — because the bicategory is precisely the 2-category with its 1-cell associativity and unit laws relaxed, and neither is fully understood without the other.

---

# Axiom Motivation

The right way to discover these definitions is to ask: *where do morphisms between morphisms come from, and what must we be able to do with them?* The answer is everywhere. Between two [[Def - Functor|functors]] $F, G : \mathcal{C} \to \mathcal{D}$ sit [[Def - Natural Transformation|natural transformations]]; between two continuous maps sit homotopies; between two chain maps sit chain homotopies. In each case the "morphisms" $F, G$ are themselves arrows, and the [[Def - Natural Transformation|natural transformations]] are arrows between arrows. An ordinary [[Def - Category|category]] has no room for this — it composes along exactly one dimension. We need a structure that composes 1-cells end-to-end *and* composes 2-cells.

Once 2-cells are admitted, there are two genuinely different ways to compose them, and getting both is the whole point. Given $\alpha : f \Rightarrow g$ and $\beta : g \Rightarrow h$ with $f, g, h : A \to B$ all parallel, we can stack them along the shared 1-cells: this is **vertical** composition $\beta \circ \alpha : f \Rightarrow h$, and it is just composition in the hom-category $\mathcal{B}(A,B)$. But given $\alpha : f \Rightarrow f'$ with $f, f' : A \to B$ and $\gamma : g \Rightarrow g'$ with $g, g' : B \to C$, the 1-cells compose ($g \ast f, g' \ast f' : A \to C$) and so should the 2-cells: this is **horizontal** composition $\gamma \ast \alpha : g \ast f \Rightarrow g' \ast f'$. The demand that horizontal composition be a *functor* $\mathcal{B}(B,C) \times \mathcal{B}(A,B) \to \mathcal{B}(A,C)$ — that it respect vertical composition and identities — is exactly the [[Thm - The Interchange Law|interchange law]], and it is not optional: without it the two composites of a grid of 2-cells disagree and "pasting" is meaningless.

Now, what laws should the 1-cells obey? The obvious answer, "the same as in a category — strict associativity and unit", gives the **2-category**. And for algebra this is correct: [[Def - Functor|functor]] composition is associative on the nose, $(H \circ G) \circ F = H \circ (G \circ F)$, with the identity functor a strict unit. So $\mathbf{Cat}$ is a strict 2-category, and the strict definition loses nothing there.

But strict associativity of 1-cells is the wrong demand in general, and seeing *why* forces the bicategory on us. Consider the prototype: 0-cells are rings, 1-cells $A \to B$ are $(B,A)$-bimodules, and horizontal composition is tensor product over the middle ring, $N \ast M = N \otimes_B M$. Tensor product is associative only **up to a canonical isomorphism** $(P \otimes_C N) \otimes_B M \cong P \otimes_C (N \otimes_B M)$, never on the nose — the two iterated tensor products are literally different sets with the same universal property. Demanding strict equality here would exclude the single most important example. The honest move is to record the canonical isomorphism as part of the data: a 2-isomorphism $a_{f,g,h} : (h \ast g) \ast f \Rightarrow h \ast (g \ast f)$, the **associator**, together with unit isomorphisms $l_f : 1_B \ast f \Rightarrow f$ and $r_f : f \ast 1_A \Rightarrow f$, the **unitors**.

The instant you make associativity a chosen isomorphism rather than an equality, you must ask whether the choices *cohere*. Reassociating a product of four 1-cells $((k \ast h) \ast g) \ast f$ to $k \ast (h \ast (g \ast f))$ can be done along two different routes through the associator, and there is no reason a priori that they agree. The **pentagon axiom** demands exactly that they do: the pentagon of associators commutes. Likewise, the two ways of cancelling a unit inserted in the middle of $f \ast 1 \ast g$ must agree — the **triangle axiom**. Drop the pentagon and associativity becomes genuinely ambiguous for products of four or more 1-cells, so "the composite" of a long string is undefined; this is exactly the failure the pentagon rules out. Drop the triangle and the left and right unit conventions can clash. With pentagon and triangle in place, Mac Lane's coherence theorem (the [[Thm - Strictification of Bicategories|bicategorical version]]) guarantees that *every* diagram built from associators and unitors commutes, so the ambiguity is fully tamed: weak associativity behaves, for all practical purposes, like strict associativity.

Why not weaken further — make the associator a non-invertible 2-cell? Because then reassociation could not be undone, and composition would no longer be associative even up to homotopy; you would have a lax structure, useful but no longer a "category" in any reasonable sense. And why not strengthen back to equality? Because, as the bimodule example shows, equality excludes the examples we care about. The bicategory is the Goldilocks notion: associativity weak enough to admit tensor products of bimodules, coherent enough that the weakness never bites.

---

# The Definition

**Strict 2-category.** A **2-category** $\mathcal{B}$ is a [[Def - Category|category]] *enriched* in $\mathbf{Cat}$ (see [[Def - Enriched Category]]). Concretely it consists of:

- a class $\mathcal{B}_0$ of **0-cells** (objects);
- for each pair $A, B \in \mathcal{B}_0$, an ordinary category $\mathcal{B}(A,B)$, whose objects are the **1-cells** $f : A \to B$ and whose morphisms are the **2-cells** $\alpha : f \Rightarrow g$; composition in this category is **vertical** composition $\circ$;
- for each $A, B, C$, a composition **functor** $\mathcal{B}(B,C) \times \mathcal{B}(A,B) \to \mathcal{B}(A,C)$, on 1-cells $(g,f) \mapsto g \ast f$ and on 2-cells $(\gamma, \alpha) \mapsto \gamma \ast \alpha$ (**horizontal** composition);
- for each $A$, an identity 1-cell $1_A \in \mathcal{B}(A,A)$,

such that horizontal composition is *strictly* associative and unital on both 1-cells and 2-cells: $(h \ast g) \ast f = h \ast (g \ast f)$, $1_B \ast f = f = f \ast 1_A$, and likewise for 2-cells. That horizontal composition is a functor is precisely the [[Thm - The Interchange Law|interchange law]]: $(\gamma' \circ \gamma) \ast (\alpha' \circ \alpha) = (\gamma' \ast \alpha') \circ (\gamma \ast \alpha)$ and $1_g \ast 1_f = 1_{g \ast f}$.

**Bicategory.** A **bicategory** $\mathcal{B}$ has the same data — 0-cells, hom-categories $\mathcal{B}(A,B)$, composition functors, identity 1-cells — but with the associativity and unit laws of 1-cells replaced by specified invertible 2-cells, *natural* in their arguments:

$$a_{f,g,h} : (h \ast g) \ast f \;\overset{\cong}{\Longrightarrow}\; h \ast (g \ast f), \qquad l_f : 1_B \ast f \overset{\cong}{\Longrightarrow} f, \qquad r_f : f \ast 1_A \overset{\cong}{\Longrightarrow} f,$$

(the **associator** and the left/right **unitors**), subject to two coherence axioms. The **pentagon axiom** states that for composable 1-cells $A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} D \xrightarrow{k} E$ the two routes from $((k \ast h) \ast g) \ast f$ to $k \ast (h \ast (g \ast f))$ built from associators agree:

$$
a_{f,\,g,\,k\ast h} \circ a_{g\ast f,\,h,\,k} \;=\; (1_k \ast a_{f,g,h}) \circ a_{f,\,h\ast g,\,k} \circ (a_{g,h,k} \ast 1_f).
$$

The **triangle axiom** states that for $A \xrightarrow{f} B \xrightarrow{g} C$ the associator and unitors are compatible:

$$(1_g \ast l_f) \circ a_{f,\,1_B,\,g} = r_g \ast 1_f.$$

A 2-category is exactly a bicategory in which all $a_{f,g,h}$, $l_f$, $r_f$ are identity 2-cells.

---

# Categorical / Structural Definition

The strict 2-category has the cleanest possible structural description: **a 2-category is a category enriched in $\mathbf{Cat}$.** Enrichment (see [[Def - Enriched Category]]) replaces the hom-*set* $\mathcal{C}(A,B)$ by a hom-*object* in a [[Def - Monoidal Category|monoidal category]] $\mathcal{V}$, with composition a morphism $\mathcal{V}$ and identities picked out by maps from the unit. Take $\mathcal{V} = \mathbf{Cat}$ with monoidal product the cartesian product $\times$ and unit the terminal category $\mathbf{1}$. A $\mathbf{Cat}$-category then has, for each pair of objects, a *category* $\mathcal{B}(A,B)$; the composition morphism is a *functor* $\mathcal{B}(B,C) \times \mathcal{B}(A,B) \to \mathcal{B}(A,C)$; the unit is a functor $\mathbf{1} \to \mathcal{B}(A,A)$ picking out $1_A$; and the enriched associativity and unit laws are *equalities* of functors, which is exactly strict 2-category associativity. The interchange law is not an extra axiom in this picture — it is functoriality of the composition functor, automatic from enrichment.

The bicategory is the "weak" or "homotopy-coherent" version of the same idea: a category *weakly* enriched in $\mathbf{Cat}$, where the associativity and unit equalities are upgraded to coherent natural isomorphisms. This is the dimension-two instance of the chapter's recurring pattern — strict equality, then equality up to coherent isomorphism, then equality up to coherent homotopy — and it is precisely parallel to the passage from a strict monoidal category to a [[Def - Monoidal Category|weak monoidal category]]: a one-object 2-category is a strict monoidal category, a one-object bicategory is a weak one.

---

# Relate to Other Fields / Compression

A bicategory compresses to a single slogan: **it is a category whose hom-sets have themselves become categories, with composition associative only up to coherent isomorphism.** Every place in mathematics where "maps between maps" appear is secretly bicategorical. In topology, spaces / continuous maps / homotopies form a (bi)category — the homotopies are the 2-cells, and they only compose associatively up to reparametrisation, which is why the structure is weak. In algebra, rings / bimodules / bimodule maps form the bicategory $\mathbf{Bimod}$, with tensor product as horizontal composition. In logic, theories / interpretations / proofs of equivalence sit in a 2-category. The reason these all look alike is that they *are* alike: each is a category enriched (strictly or weakly) in $\mathbf{Cat}$, and the choice of strict versus weak is dictated by whether the horizontal composition is honestly associative (functor composition: strict) or only up to canonical isomorphism (tensor product: weak).

**True name:** a 2-category is "a category enriched in categories"; a bicategory is "a category enriched in categories, but only up to coherent isomorphism." When you see 2-cells, do not picture an exotic new axiom system — picture ordinary [[Def - Enriched Category|enrichment]] with $\mathcal{V} = \mathbf{Cat}$, and ask only whether the enrichment is strict.

---

# Examples / Corollaries

**Is an instance — $\mathbf{Cat}$ is a strict 2-category.** The 0-cells are (small) [[Def - Category|categories]], the 1-cells are [[Def - Functor|functors]], and the 2-cells $\alpha : F \Rightarrow G$ are [[Def - Natural Transformation|natural transformations]]. The hom-category $\mathbf{Cat}(\mathcal{C}, \mathcal{D})$ is exactly the [[Def - Functor Category|functor category]] $[\mathcal{C}, \mathcal{D}]$, with vertical composition $(\beta \circ \alpha)_X = \beta_X \circ \alpha_X$ computed componentwise. Horizontal composition of $\alpha : F \Rightarrow F'$ (functors $\mathcal{C} \to \mathcal{D}$) and $\gamma : G \Rightarrow G'$ (functors $\mathcal{D} \to \mathcal{E}$) is the natural transformation $\gamma \ast \alpha : G \circ F \Rightarrow G' \circ F'$ with component $(\gamma \ast \alpha)_X = G'(\alpha_X) \circ \gamma_{FX} = \gamma_{F'X} \circ G(\alpha_X)$ (the two expressions agree precisely by naturality of $\gamma$ — this *is* the interchange law). Functor composition is strictly associative and unital, so $\mathbf{Cat}$ is strict; it is the motivating example and the source of the name "2-category".

**Is an instance — a monoidal category is a one-object bicategory.** Given a [[Def - Monoidal Category|monoidal category]] $(\mathcal{M}, \otimes, I, a, l, r)$, build a bicategory $\mathcal{B}$ with a single 0-cell $\star$: set $\mathcal{B}(\star, \star) = \mathcal{M}$, so the 1-cells $\star \to \star$ are the objects of $\mathcal{M}$ and the 2-cells are its morphisms; horizontal composition of 1-cells is $\otimes$, the identity 1-cell is $I$, and the associator/unitors of $\mathcal{B}$ are exactly those of $\mathcal{M}$. The pentagon and triangle axioms of the bicategory are the pentagon and triangle of the monoidal category. Conversely a one-object bicategory unwinds to a monoidal category. This is the precise sense in which "monoidal category = categorified monoid" sits one rung below "bicategory = categorified category".

**Is an instance — the bicategory of bimodules.** 0-cells are rings, a 1-cell $A \to B$ is a $(B,A)$-bimodule $M$ (a left $B$-, right $A$-module with $(bm)a = b(ma)$), 2-cells are bimodule homomorphisms, and horizontal composition is $N \ast M = N \otimes_B M$. Associativity holds only up to the canonical isomorphism $(P \otimes_C N) \otimes_B M \cong P \otimes_C (N \otimes_B M)$, so this bicategory is *genuinely weak* — it cannot be made strict on the nose while keeping the same tensor products. The identity 1-cell on $A$ is the bimodule $A$ itself. This example is the reason bicategories were invented.

**Is NOT an instance — a mere "category with a 2-cell structure" lacking interchange.** Suppose you equip a category with sets of 2-cells and both compositions, but the [[Thm - The Interchange Law|interchange law]] fails. Then a $2 \times 2$ pasting diagram has two unequal values, "horizontal-then-vertical" and "vertical-then-horizontal", so there is no well-defined notion of the composite of the diagram. This is *not* a 2-category: the whole point of the structure is that pasting is unambiguous, and interchange is exactly the condition guaranteeing it. Concretely, the failure shows up the moment you try to whisker a natural transformation by a functor in two orders and get different answers.

**Corollary — strictness is the special case $a = l = r = \mathrm{id}$.** Every 2-category is a bicategory (take all coherence cells to be identities), and every bicategory whose associator and unitors happen to be identities is a 2-category. So the two notions are nested: $\{\text{2-categories}\} \subset \{\text{bicategories}\}$, and [[Thm - Strictification of Bicategories|coherence]] says the inclusion is an equivalence "up to biequivalence".

**Calibration check.** Verify that the hom-category $\mathbf{Cat}(\mathcal{C}, \mathcal{D}) = [\mathcal{C}, \mathcal{D}]$ really is a category under vertical composition of natural transformations (associativity and identities are componentwise). Check that in any bicategory the unitors $l_{1_A}$ and $r_{1_A}$ on the identity 1-cell agree (a consequence of the triangle axiom). And confirm that taking a one-object bicategory and forgetting the object returns a [[Def - Monoidal Category|monoidal category]] with $\otimes$ given by horizontal composition.

---

# Unlocked by This

> [!tip] (∞,n)-Categories *(from Higher Category Theory)*
> Iterating the construction — categories enriched in $(n-1)$-categories — yields strict **$n$-categories**, and weakening the coherence at every level yields weak $n$-categories and ultimately **(∞,n)-categories**, the $\infty$-categories with all cells above dimension $n$ invertible. The case $n=1$ is the [[Def - Quasi-Category|quasi-category]] of §H.4.

> [!tip] The Cobordism Hypothesis *(from Topological Field Theory)*
> Symmetric monoidal $(\infty, n)$-categories are the target of an **extended TQFT**, and **the cobordism hypothesis** (Baez–Dolan, Lurie) says such a field theory is determined by a single fully dualizable object — its value on a point. The bicategorical case $n = 2$ is the first nontrivial instance.
