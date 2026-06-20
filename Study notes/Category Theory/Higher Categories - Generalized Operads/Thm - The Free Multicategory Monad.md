---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Cartesian Monad"
  - "Def - Generalized Multicategory"
  - "Def - Generalized Operad"
  - "Def - Free-Forgetful Adjunction"
  - "Def - Monad and Comonad"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $(T, \eta, \mu)$ is a [[Def - Cartesian Monad|cartesian monad]] on a category $\mathcal{E}$ with [[Def - Pullback and Pushout|pullbacks]] (and, for existence, suitable colimits). A **$T$-graph** is the data $(C_0, C_1, \mathrm{dom} : C_1 \to T C_0, \mathrm{cod} : C_1 \to C_0)$ — a [[Def - Generalized Multicategory|$T$-multicategory]] without identities or composition. We write $T\text{-}\mathbf{Gph}$ for the category of $T$-graphs and $(\mathcal{E}, T)\text{-}\mathbf{Multicat}$ for the category of $T$-multicategories. The **forgetful functor** $U : (\mathcal{E}, T)\text{-}\mathbf{Multicat} \to T\text{-}\mathbf{Gph}$ drops identities and composition. The monad it induces is written $T^{+}$ (the **free $T$-multicategory monad**). The full symbol registry is on [[Higher Categories — Generalized Operads via Cartesian Monads]].

---

# Statement

> **Theorem (Free $T$-multicategory monad).** Let $(T, \eta, \mu)$ be a [[Def - Cartesian Monad|cartesian monad]] on a category $\mathcal{E}$ with pullbacks and the colimits needed for the construction below. Then:
> 1. The forgetful functor $U : (\mathcal{E}, T)\text{-}\mathbf{Multicat} \to T\text{-}\mathbf{Gph}$ has a left adjoint $F$ (the **free $T$-multicategory** on a $T$-graph), so there is a [[Def - Free-Forgetful Adjunction|free–forgetful adjunction]] $F \dashv U$.
> 2. The induced [[Def - Monad and Comonad|monad]] $T^{+} = U F$ on $T\text{-}\mathbf{Gph}$ is again **cartesian**, and its [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] are exactly the $T$-multicategories: $(\mathcal{E}, T)\text{-}\mathbf{Multicat} \cong (T\text{-}\mathbf{Gph})^{T^{+}}$.

> **Corollary (instances).** Over $\mathcal{E} = \mathbf{Set}$: with $T = \mathrm{id}$, $T^{+}$ is the **free-category monad** on directed graphs, whose algebras are small [[Def - Category|categories]]; with $T = (-)^{*}$, $T^{+}$ is the **free-(plain)-multicategory monad**, whose algebras are classical multicategories. Because $T^{+}$ is cartesian, the construction can be iterated, $T \mapsto T^{+} \mapsto T^{++} \mapsto \cdots$, which is the engine behind opetopes (HC6).

---

# Motivation

This theorem is the framework's self-closure: it says that the operation "freely build a generalized multicategory" lives *inside* the framework rather than escaping it. There are two reasons to care, and they are different in kind.

The first is existential. Many constructions in the chapter — "the free operad on a signature", "the operations of a globular operad are all formal pasting diagrams", "the terminal operad's operations are the arity-shapes" — silently assume that free $T$-multicategories exist. Without a theorem guaranteeing the left adjoint $F$, these phrases are wishful. Part (1) supplies the guarantee: a cartesian monad always admits free $T$-multicategories, so every "freely generated" object in the chapter is legitimate.

The second reason is structural and is the deeper point. Part (2) says $T^{+}$ is *again cartesian*. This is what makes the framework recursive. The output of "freely generate multicategories" is a new cartesian monad, so the entire machinery applies to *it*: one can form $T^{+}$-multicategories, $T^{+}$-operads, and — crucially — $T^{++}$. Iterating this from the simplest starting point produces, dimension by dimension, the combinatorial shapes (opetopes) on which an entire definition of weak $n$-category is built. The theorem is therefore not a technical lemma but the inductive step of higher category theory: it is the reason the tower of dimensions can be climbed using one construction applied repeatedly.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is "$T$ is a cartesian monad with enough colimits", but the productive question is: when does a problem secretly present a free $T$-multicategory, so that this theorem applies even though no adjoint is named?

The first disguised source is **a structure described by "all formal composites of given generators"**. Whenever a problem says "the operations are all the ways of composing the basic operations", "the arrows are all paths", or "the cells are all pasting diagrams built from the basic cells", it is describing a *free* object on a $T$-graph of generators. The non-obvious step is recognizing the generators as a $T$-graph and "formal composites" as the free $T$-multicategory on it. *Example problem:* show that the operations of the free operad on a single binary operation are exactly the planar binary trees — this is $F$ applied to the one-arity-two $T$-graph, and the theorem certifies the free object exists and computes it as trees.

The second disguised source is **a category presented as "the free category on a quiver/graph"**. A directed graph is a $\mathrm{id}$-graph, and the free category on it (objects = vertices, arrows = paths) is $F$ for $T = \mathrm{id}$. The non-obviousness is that the familiar "path category" is an instance of a general adjunction whose existence requires nothing special about $\mathbf{Set}$. *Example problem:* identify the free category on the graph with one vertex and one loop as the monoid $\mathbb{N}$, recovering it as the arrows-are-paths description.

The third disguised source is **a need to iterate a construction by dimension**. When a problem builds objects in dimension $n+1$ out of "diagrams of dimension-$n$ objects", it is implicitly applying $(-)^{+}$ to a cartesian monad and using that the result is again cartesian so the next dimension can be built. The non-obvious recognition is that "diagrams of the previous level" is a free $T^{(n)}$-multicategory construction. *Example problem:* explain why opetopes in dimension $n+1$ are pasting diagrams of opetopes in dimension $n$ — this is the iterated $(-)^{+}$ applied to the identity operad (HC6).

**Targets (Output Amplification)**

The bare conclusion is "$F \dashv U$ exists and $T^{+}$ is cartesian". Combined with other facts it does much more.

Combine the conclusion with **the monadicity of $U$**. Since $T$-multicategories are the Eilenberg–Moore algebras of $T^{+}$, the forgetful functor $U$ is [[Def - Algebra for a Monad|monadic]], so $(\mathcal{E}, T)\text{-}\mathbf{Multicat}$ inherits all limits from $T\text{-}\mathbf{Gph}$ and is well-behaved (complete, with a free–forgetful adjunction). The further result is that one may compute limits of $T$-multicategories pointwise on the underlying $T$-graphs, a workhorse for constructing new multicategories as limits of old ones.

Combine the conclusion with **iterability**. Because $T^{+}$ is cartesian, the theorem applies to $T^{+}$ in place of $T$, yielding $T^{++}$, again cartesian. The further result $E$ is an infinite tower of cartesian monads from a single seed, which is exactly the data needed for the **slice construction** producing opetopes: each level's operations are the previous level's pasting diagrams.

Combine the conclusion with **the terminal $T$-operad**. Applying $F$ to the terminal $T$-graph, or studying $T^{+}$ acting on the terminal object, computes the *arity-shapes* of the free multicategory. The further result is an explicit description of $T1$, $T^{+}1$, etc. — for the identity monad these are points, then finite linear graphs, then trees of linear graphs — which is how the combinatorics of pasting shapes is generated mechanically.

---

# Why Is It True

The free $T$-multicategory on a $T$-graph $X$ is built by the only construction that could possibly work: throw in all the *formal composites* of the arrows of $X$ and nothing else. An arrow of the free object is a *tree of arrows of $X$*, where the tree-shape is dictated by $T$. For $T = \mathrm{id}$ a tree is a *path* (you can only compose linearly), so the free $\mathrm{id}$-multicategory is the path category. For $T = (-)^{*}$ a tree is an honest rooted tree (each node has a list of children), so the free $(-)^{*}$-multicategory's operations are trees of multimaps. Composition in the free object is *grafting trees*, which is automatically associative and unital because grafting trees is associative and unital — there are no relations to impose, which is exactly what "free" means.

The cartesianness of $T^{+}$ is where the cartesianness of $T$ pays off, and the mechanism is clean:

> **$T^{+}$ is cartesian because its operations are *trees*, and trees form a rigid, symmetry-free family of arities — inherited directly from the rigidity of $T$'s own arities.**

Spelled out: an arrow of the free multicategory is a tree whose nodes are labelled by arrows of $X$, and the shape of the tree at each node is a $T$-shape. Cartesianness of $T$ says the $T$-shapes have no collapsing symmetries; building trees out of such shapes preserves that rigidity, because a tree records exactly *which* arrow sits at each node and *how* the shapes nest, with nothing forgotten. So the naturality squares of $T^{+}$'s unit and multiplication are pullbacks for the same reason $T$'s are: from a composite tree together with its abstract shape you can reconstruct the constituent labels uniquely. Symmetry would ruin this — if the children of a node were unordered, two labellings could give the same tree and the pullback would fail — which is the precise sense in which $T^{+}$ inherits cartesianness from $T$.

That the algebras are $T$-multicategories is the universal property read backwards: a $T^{+}$-algebra structure on a $T$-graph is a rule for evaluating every formal tree of arrows into a single arrow, coherently — and "evaluate trees coherently" is exactly "have identities and an associative, unital composition", i.e. be a $T$-multicategory.

---

# What Makes This Hard

The genuinely hard part is proving the existence of the free object and the cartesianness of $T^{+}$ *simultaneously and at the right level of generality* — the construction of trees must be carried out internally to $\mathcal{E}$ (as a colimit of iterated pullbacks), not just in $\mathbf{Set}$, and one must verify that this internal "object of trees" exists and that its unit/multiplication squares are pullbacks. The most common error is to prove existence by an abstract adjoint-functor-theorem argument and then have no handle on $T^{+}$, leaving cartesianness unproved; the explicit "arrows are trees" construction is needed precisely because cartesianness must be *read off* the trees. The second subtlety is the colimit hypothesis: the tree construction is a transfinite colimit (free objects are built by iterating "add one more layer of composites"), so $\mathcal{E}$ must admit those colimits and $T$ must be suitably finitary for the iteration to converge.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Build the free $T$-multicategory on a $T$-graph $X$ explicitly as an "object of $T$-trees" via a colimit of iterated pullbacks; check it satisfies the universal property of $F \dashv U$; then read cartesianness of $T^{+} = UF$ off the tree description, inheriting it from the cartesianness of $T$.

**Subgoal decomposition:**

1. **Define $T$-trees.** Construct, for a $T$-graph $X$, the object of formal composites ($T$-trees of arrows of $X$) as a colimit $\mathrm{tr}(X) = \mathrm{colim}_n \mathrm{tr}_n(X)$, where $\mathrm{tr}_0$ is identities, and $\mathrm{tr}_{n+1}$ adds one layer of $T$-shaped grafting via a pullback.
   - *Hint:* Each layer is "an arrow of $X$ with a $T$-shape of trees plugged into its inputs" — a pullback of $\mathrm{dom}_X$ against $T(\text{root-output of } \mathrm{tr}_n)$.
   - *Why needed:* This is the object underlying the free multicategory; everything else refers to it.

2. **Equip $\mathrm{tr}(X)$ with multicategory structure.** Define identities (length-zero trees) and composition (grafting trees).
   - *Hint:* Grafting is induced on the colimit by the pullbacks of step 1; associativity and unitality of grafting are formal.
   - *Why needed:* Makes $F X = \mathrm{tr}(X)$ a $T$-multicategory, the candidate free object.

3. **Verify the universal property.** Show that $T$-multicategory morphisms $F X \to C$ correspond naturally to $T$-graph morphisms $X \to U C$.
   - *Hint:* A graph map $X \to UC$ extends uniquely to trees by evaluating each tree using $C$'s composition; uniqueness is induction on tree height.
   - *Why needed:* This is exactly $F \dashv U$, giving part (1).

4. **Read off cartesianness of $T^{+}$.** Show the unit and multiplication squares of $T^{+} = UF$ are pullbacks, and $T^{+}$ preserves pullbacks.
   - *Hint:* A composite tree plus its abstract shape determines its labels uniquely, *because $T$ is cartesian at each node*; this reconstruction is exactly the pullback condition.
   - *Why needed:* This is part (2); it is what makes the construction iterable.

5. **Identify the algebras.** Show $T^{+}$-algebras are $T$-multicategories.
   - *Hint:* A $T^{+}$-algebra evaluates every tree to an arrow coherently; coherence is identities + associative unital composition.
   - *Why needed:* Completes part (2), the Eilenberg–Moore identification.

---

# Lemma Decomposition

> [!note]- Lemma 1: The object of $T$-trees exists as an iterated-pullback colimit
> **Statement:** For a $T$-graph $X$ in a cartesian-monad setting with the requisite colimits, the object $\mathrm{tr}(X)$ of formal $T$-composites exists, built as $\mathrm{colim}_n \mathrm{tr}_n(X)$ with $\mathrm{tr}_{n+1}(X)$ obtained from $\mathrm{tr}_n(X)$ by one $T$-shaped grafting pullback.
>
> **Hint:** Model $\mathrm{tr}_{n+1}$ as "an arrow of $X$ together with a $T$-shape of height-$\leq n$ trees fitting its inputs", a pullback of $\mathrm{dom}_X : X_1 \to T X_0$ against $T$ applied to the output map of $\mathrm{tr}_n$.
>
> **Why needed:** Supplies the underlying object of the free multicategory; without it the construction is only formal.
>
> > [!note]- Full proof
> > Set $\mathrm{tr}_0(X) = X_0$ (length-zero trees, i.e. would-be identities, indexed by objects). Given $\mathrm{tr}_n(X)$ with an "output" map $\mathrm{cod}_n : \mathrm{tr}_n(X) \to X_0$ and an "input-shape" map $\mathrm{dom}_n : \mathrm{tr}_n(X) \to T X_0$, define
> > $$\mathrm{tr}_{n+1}(X) \;=\; X_1 \times_{T X_0} T\big(\mathrm{tr}_n(X)\big),$$
> > the pullback of $\mathrm{dom}_X : X_1 \to T X_0$ against $T(\mathrm{cod}_n) : T(\mathrm{tr}_n(X)) \to T X_0$. An element is "an arrow of $X$ whose inputs are filled by a $T$-shape of height-$\leq n$ trees with matching outputs". The output map is $\mathrm{cod}_X$ of the top arrow; the input-shape is $\mu_{X_0}$ applied to the $T$-shape of the children's input-shapes. The inclusions $\mathrm{tr}_n \hookrightarrow \mathrm{tr}_{n+1}$ (a tree of height $\leq n$ is a tree of height $\leq n+1$) form a chain, and $\mathrm{tr}(X) = \mathrm{colim}_n \mathrm{tr}_n(X)$ exists by the colimit hypothesis. Cartesianness of $T$ ensures $T$ commutes with these filtered colimits sufficiently for the construction to close up. $\square$

> [!note]- Lemma 2: Grafting trees is associative and unital
> **Statement:** The grafting operation $\mathrm{comp} : \mathrm{tr}(X) \times_{T X_0} T(\mathrm{tr}(X)) \to \mathrm{tr}(X)$, "plug a $T$-shape of trees into the inputs of a tree", together with identities (height-zero trees), satisfies the [[Def - Generalized Multicategory|$T$-multicategory]] axioms.
>
> **Hint:** Grafting is "stack trees"; both associativity and unitality are formal properties of stacking, with no relations imposed because the object is free.
>
> **Why needed:** Makes $\mathrm{tr}(X)$ a $T$-multicategory, the candidate value of $F$.
>
> > [!note]- Full proof
> > Identities: the map $\mathrm{ids} : X_0 \to \mathrm{tr}(X)$ picks the height-zero tree at each object. Composition: grafting is induced layerwise from the pullbacks of Lemma 1 — a $T$-shape of trees plugged into a tree's inputs yields a taller tree, using $\mu$ to flatten the nested input-shapes. Associativity: grafting trees $A$, then grafting the result into $B$, equals grafting $A$-into-$B$-into-$C$ in either order, because a tree records its full nesting and re-nesting changes nothing; precisely, this is the associativity law $\mu \circ T\mu = \mu \circ \mu T$ transported to trees. Unitality: grafting height-zero trees onto the inputs, or grafting a tree onto a height-zero tree, returns the original tree, by the monad unit laws $\mu \circ T\eta = 1 = \mu \circ \eta T$. No relations are needed: the free object imposes only the equalities forced by the monad axioms. $\square$

> [!note]- Lemma 3: The universal property holds, and $T^{+}$ is cartesian
> **Statement:** $F X = \mathrm{tr}(X)$ is the free $T$-multicategory on $X$: $(\mathcal{E},T)\text{-}\mathbf{Multicat}(FX, C) \cong T\text{-}\mathbf{Gph}(X, UC)$ naturally. Moreover $T^{+} = UF$ has cartesian unit and multiplication and preserves pullbacks.
>
> **Hint:** Extend a graph map to trees by induction on height (existence and uniqueness); for cartesianness, a composite tree plus its abstract shape determines its node-labels uniquely *because each node's $T$-shape is rigid*.
>
> **Why needed:** Gives the adjunction (part 1) and the cartesianness/iterability (part 2).
>
> > [!note]- Full proof
> > *Universal property.* Given a $T$-graph map $f : X \to UC$, define $\bar f : FX \to C$ on trees by induction on height: a height-zero tree goes to the corresponding identity of $C$; a height-$(n+1)$ tree, "arrow $a$ of $X$ with children $\Theta$", goes to $\mathrm{comp}_C(f(a), T(\bar f)(\Theta))$. This respects identities and grafting by construction, so $\bar f$ is a multicategory morphism, and it is the unique one restricting to $f$ on generators (uniqueness is the same induction). Naturality in $X$ and $C$ is routine. Hence $F \dashv U$.
> >
> > *Cartesianness.* The unit $\eta^{+}_X : X \to T^{+} X$ includes generators as height-one trees; its naturality square for a graph map $g : X \to Y$ is a pullback because a tree in $T^{+} Y$ comes from $X$ exactly when all its node-labels do, reconstructed uniquely from the labels — which is exactly the pullback condition, and it holds because $T$ is cartesian at each node (no symmetry to collapse distinct labellings). The multiplication $\mu^{+}_X : T^{+} T^{+} X \to T^{+} X$ flattens trees-of-trees into trees; its naturality square is a pullback because from a flattened tree and the abstract tree-of-trees shape one recovers the partition into subtrees uniquely, again by rigidity inherited from $T$. Preservation of pullbacks by $T^{+}$ follows since $\mathrm{tr}$ is built from pullbacks and $T$ (which preserves them) by colimits that commute appropriately. Hence $T^{+}$ is cartesian.
> >
> > *Algebras.* A $T^{+}$-algebra $h : T^{+} X \to X$ on a $T$-graph $X$ assigns to every tree of arrows a single arrow, compatibly with identities (unit law) and grafting (associativity law); this is precisely a choice of identities and an associative unital composition on $X$, i.e. a $T$-multicategory structure. The correspondence is an isomorphism of categories $(T\text{-}\mathbf{Gph})^{T^{+}} \cong (\mathcal{E},T)\text{-}\mathbf{Multicat}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(T, \eta, \mu)$ be a cartesian monad on $\mathcal{E}$ with pullbacks and the filtered colimits used below.
>
> **Step 0 — preconditions.** $\mathcal{E}$ has pullbacks (so $T$-graphs and the grafting pullbacks make sense) and admits the colimit $\mathrm{tr}(X) = \mathrm{colim}_n \mathrm{tr}_n(X)$; $T$ preserves pullbacks and these colimits sufficiently (cartesian + finitary). These are exactly the hypotheses.
>
> **Step 1 — the free object.** By Lemma 1 the object of $T$-trees $\mathrm{tr}(X)$ exists for each $T$-graph $X$, and by Lemma 2 it carries identities and an associative, unital grafting, hence is a $T$-multicategory $FX$ with underlying $T$-graph containing $X$ via $\eta^{+}_X$.
>
> **Step 2 — the adjunction.** By Lemma 3, $F X$ has the universal property of the free $T$-multicategory: graph maps $X \to UC$ extend uniquely to multicategory maps $FX \to C$. Therefore $F \dashv U$, proving part (1).
>
> **Step 3 — cartesianness of $T^{+}$.** Set $T^{+} = UF$. By Lemma 3, the unit $\eta^{+}$ and multiplication $\mu^{+}$ of $T^{+}$ have pullback naturality squares, and $T^{+}$ preserves pullbacks, because the tree construction inherits rigidity from the cartesianness of $T$ node by node. Hence $T^{+}$ is a cartesian monad.
>
> **Step 4 — the algebras.** By Lemma 3, $(T\text{-}\mathbf{Gph})^{T^{+}} \cong (\mathcal{E}, T)\text{-}\mathbf{Multicat}$: a $T^{+}$-algebra is exactly a coherent rule for evaluating trees, i.e. a $T$-multicategory structure. This proves part (2).
>
> **Corollary (instances).** For $T = \mathrm{id}$ on $\mathbf{Set}$, trees are paths, so $T^{+}$ is the free-category monad and its algebras are small categories. For $T = (-)^{*}$, trees are trees of multimaps, so $T^{+}$ is the free-multicategory monad and its algebras are multicategories. Since $T^{+}$ is cartesian, the theorem applies to it, giving $T^{++}$, etc. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Free monoids and the path category.** Take $\mathcal{E} = \mathbf{Set}$, $T = \mathrm{id}$, and the $T$-graph with one vertex and one loop. The free $T$-multicategory is the free monoid on one generator, $\mathbb{N}$, realized as "paths" (powers of the loop). This is a warm-up showing the theorem's tree-construction reduces, in the simplest case, to the familiar free-monoid construction; the non-obvious recognition is that "free monoid" and "free category on a one-object graph" are the same instance of $F$.

**Trees as the free operad on a binary operation.** With $T = (-)^{*}$, the free $T$-operad on a single binary operation has, as its $n$-ary operations, the planar binary trees with $n$ leaves (Catalan-many). Computing these trees and their grafting is a concrete, combinatorial instance of Lemma 1 and Lemma 2; the application is non-obvious because "Catalan trees" rarely advertise themselves as a free-operad computation, yet that is exactly what they are.

**Iterating to opetopes.** Starting from the terminal $\mathrm{id}$-operad and applying $(-)^{+}$ repeatedly generates the opetopes: $0$-opetopes are points, $1$-opetopes are arrows, $2$-opetopes are "many-in one-out" trees, and so on (HC6). This battle-tests the iterability target: each application requires $T^{+}$ to be cartesian, which is exactly part (2). Recognizing the opetope tower as iterated free-multicategory monads is the surprising payoff.

**$W$-types in type theory.** In a category modelling dependent type theory, the initial algebra of a polynomial functor is the type of well-founded trees ($W$-type) of a signature. The free $T$-multicategory construction is the operadic cousin: both build "all formal trees over a signature" and both rely on the cartesian/polynomial structure to exist. Recognizing a $W$-type as a free-tree construction transfers the theorem's existence argument to type theory.

---

# Bridges

- **[[Def - Cartesian Monad|Cartesian monads]]** — the input *and* the output. The theorem takes a cartesian monad $T$ and returns a cartesian monad $T^{+}$. This closure under the free construction is what distinguishes cartesian monads as the right setting: the framework reproduces its own hypotheses, so it can be iterated. The cartesianness of $T^{+}$ is read off the rigidity of trees, which is inherited node-by-node from the rigidity of $T$'s arities.

- **[[Def - Generalized Multicategory|$T$-multicategories]] as algebras** — the theorem realizes $T$-multicategories as the Eilenberg–Moore category of $T^{+}$. This means the entire theory of [[Def - Algebra for a Monad|monad algebras]] applies to multicategories: limits are computed on underlying $T$-graphs, the free–forgetful adjunction is monadic, and "free multicategory on a signature" is a legitimate, computable object.

- **Burroni's "category = monad in spans"** — the bottom case. For $T = \mathrm{id}$ the free $T$-multicategory monad is the free-category monad on graphs, whose algebras are small categories; this is the free version of Burroni's identification of categories with monads in $\mathrm{Span}(\mathbf{Set})$. The theorem generalizes the free-category construction to every cartesian monad at once.

- **The slice construction and opetopes (HC6)** — the iterated application. Repeatedly applying $(-)^{+}$, starting from the identity/terminal operad, produces the category of opetopes, whose presheaves are opetopic sets. The theorem's part (2), cartesianness of $T^{+}$, is precisely the fact that licenses each successive application, making the opetope tower well-defined.

---

# Unlocked by This

> [!tip] Opetopes and Opetopic Sets *(from Higher Category Theory)*
> Iterating the free $T$-multicategory monad from the terminal operad generates the **opetopes** — the pasting-diagram shapes of every dimension — and presheaves on them are **opetopic sets**, the Baez–Dolan / Hermida–Makkai–Power model of weak $n$-categories (HC6). The theorem's guarantee that $T^{+}$ is again cartesian is exactly what makes each step of the iteration legal.

> [!tip] Free Operads and Trees *(from this chapter)*
> The theorem certifies that the **free $T$-operad** on a $T$-graph exists, and its operations are the formal trees of generators. For $T = (-)^{*}$ this gives free operads whose $n$-ary operations are trees, the combinatorial backbone of operad theory and of the bar/cobar constructions in homotopical algebra.

> [!tip] W-Types and Polynomial Initial Algebras *(from Categorical Logic)*
> Because cartesian monads on slice categories are polynomial monads, the free-tree construction here is the operadic face of **$W$-types** — the initial algebras of polynomial functors, i.e. the inductive types of well-founded trees. The same existence argument (build trees as an iterated-pullback colimit) underlies inductive type formation in dependent type theory.
