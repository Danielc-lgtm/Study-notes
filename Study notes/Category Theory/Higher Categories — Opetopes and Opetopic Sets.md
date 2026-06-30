---
type: topic
subject: higher-categories
chapter: "7.1-7.6, App E"
title: "Higher Categories — Opetopes and Opetopic Sets"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

A standing convention for this chapter: by a **multicategory** we always mean a *non-symmetric* (plain) multicategory unless we explicitly say "symmetric". Baez and Dolan worked with symmetric multicategories, but the combinatorics of opetopes is cleaner in the plain, non-symmetric setting, where operations come with a fixed *linear order* on their inputs. This is why the trees of Appendix E are **planar**: a planar tree records an ordering of its branches, and that ordering is the data a non-symmetric operation carries. When the symmetric version differs in a way that matters, a `> [!warning]` callout flags it.

- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ — categories; **multicategory** written $C$ (a category-like structure whose arrows have a finite list of inputs and one output)
- $\mathrm{ob}(C)$ — the set (or class) of objects of a multicategory $C$
- $(a_1, \dots, a_n) \to b$ — a **multimap** (also: operation, multimorphism) of $C$ with input list $a_1, \dots, a_n$ and output $b$
- $C(a_1, \dots, a_n;\, b)$ — the set of multimaps with that signature; the **arity** of such a multimap is $n$
- $\circ$ — multicategory composition: substitute multimaps into the inputs of a multimap
- $1$ — the **terminal** multicategory / the **identity operad** (one object, one operation in each arity, the operad $I$ whose algebras are objects of a category; depending on context, the operad with exactly one $n$-ary operation for each $n$)
- $C^+$ — the **slice** of the multicategory $C$ (Section 7.1); also written $C^{+}$
- $I = 1$ — the initial object of the slicing process; $I^+, I^{++}, \dots$ — the iterated slices
- $\mathcal{O}_n$ — the set of **$n$-opetopes** (the objects of the $n$-th iterated slice, equivalently the $n$-cells)
- $\mathbb{O}$ — the **category of opetopes**, the indexing category for opetopic sets
- $\mathbf{Set}$ — the category of sets; $\mathbf{Set}^{\mathbb{O}^{op}} = [\mathbb{O}^{op}, \mathbf{Set}]$ — the category of **opetopic sets**
- $X_O$ — for an opetopic set $X$ and an opetope $O$, the set $X(O)$ of **$O$-cells** of $X$ (the cells of $X$ shaped like $O$)
- $s, t$ — source and target operations on cells (for opetopes, the target is a single cell; the source is a configuration/pasting of cells)
- $\Delta$ — the simplex category; $\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ — simplicial sets; $\mathbb{G}$ — the globe category; **globular sets** $= [\mathbb{G}^{op}, \mathbf{Set}]$
- $\mathbf{y}$ — the Yoneda embedding $\mathbb{O} \to \mathbf{Set}^{\mathbb{O}^{op}}$, sending an opetope $O$ to the representable $\mathbf{y}O = \mathbb{O}(-, O)$
- "many-in, one-out" — the defining shape of an opetope: a pasting diagram of cells with several source faces and exactly one target face

---

# Motivation

Here is the entire chapter in one sentence: an **opetope** is the shape of a "many-inputs, one-output" composition, and you build all such shapes — in every dimension — by repeating a single construction, slicing, starting from nothing. Everything else is bookkeeping.

To see why anyone would want this, recall the problem that all of higher category theory is trying to solve. In an ordinary category, composition is a strict, on-the-nose operation: given $f : a \to b$ and $g : b \to c$ there is *one* composite $g \circ f$. In a weak higher category this breaks down. We want composites to exist, but only **up to a higher cell**: $g \circ f$ is not a single canonical arrow but a chosen one, witnessed by a 2-cell, and that choice is governed by coherence cells one dimension up, and so on forever. To even write down such a structure you first need a vocabulary of *shapes*: what does a 2-cell look like, what does a 3-cell look like, what is the shape of "five 1-cells composed in a row with a 2-cell sitting on top"? Different schools of higher category theory answer "what are the shapes?" differently, and that single choice fans out into genuinely different definitions of weak $n$-category. The **opetopic** answer, due to Baez and Dolan (and reworked by Hermida–Makkai–Power and by Leinster), is the one this chapter develops.

The opetopic shapes are organised by a beautiful recursion. The slogan is:

$$\text{0-opetope} = \text{point}, \quad \text{1-opetope} = \text{arrow}, \quad \text{2-opetope} = \text{a "many-in, one-out" diagram of arrows}, \quad \dots$$

$$\boxed{\ \text{an } n\text{-opetope is a pasting diagram of } (n-1)\text{-opetopes}\ }$$

and the engine that produces this recursion is the **slice construction** $C \mapsto C^+$. Given a multicategory $C$ — a category-like gadget whose arrows take a *list* of inputs to one output — the slice $C^+$ is a new multicategory whose objects are the operations of $C$ and whose operations are the *ways of pasting operations of $C$ together*. Slicing turns "operations" into "objects" and "pasting diagrams of operations" into the new "operations". So if you start from the trivial multicategory $1$ — the **identity operad**, the simplest possible composition law — and slice repeatedly, you climb the [[Def - Dimension|dimensions]]: $1$ has one object (the point, a $0$-opetope); $1^+$ has objects that are the operations of $1$ (the arrows, $1$-[[Def - Opetope|opetopes]]); $1^{++}$ has objects that are the operations of $1^+$, namely the pasting diagrams of arrows ($2$-opetopes); and in general the $n$-fold slice $1^{+\cdots+}$ delivers the $n$-opetopes. The shapes are not postulated; they are *generated*, each dimension from the one below, by one operation applied over and over.

Once you have the shapes, the rest is a familiar move. Just as the simplices $\Delta^n$ assemble into the simplex category $\Delta$, and a **simplicial set** is a presheaf $\Delta^{op} \to \mathbf{Set}$ — a collection of cells of every simplicial shape, glued along their faces — the opetopes assemble into a category $\mathbb{O}$, and an **opetopic set** is a presheaf $\mathbb{O}^{op} \to \mathbf{Set}$: a collection of cells of every opetopic shape, glued along their source and target faces. This is the central analogy of the chapter, and it is exact:

$$\text{opetopic sets} : \text{opetopes} \quad = \quad \text{simplicial sets} : \text{simplices} \quad = \quad \text{globular sets} : \text{globes}.$$

A weak $n$-category is then an opetopic set in which the "many-in, one-out" niches can be filled — where every diagram waiting to be composed has a chosen composite and a witnessing cell, in a way governed by universal properties. That is the Baez–Dolan definition, sketched in Section 7.5.

This chapter assumes you are comfortable with categories, functors, and natural transformations; with presheaves and the Yoneda lemma (a presheaf is a functor $\mathcal{C}^{op} \to \mathbf{Set}$, and Yoneda embeds $\mathcal{C}$ into its presheaves); and ideally with the multicategory/operad language of the preceding chapters of this part — what a multicategory is, what an operad is, and what a *generalized* multicategory is. If those are rusty, refresh the **multicategory** and **operad** definitions and the [[Def - Presheaf|presheaf]] and [[Thm - The Yoneda Lemma|Yoneda]] pages before continuing; the slice construction is most naturally phrased for generalized [[Def - Multicategory|multicategories]], but the plain multicategory case carries all the geometry.

---

# Concept Map

## §7.1 Opetopes and the Slice Construction

- **[[Def - The Slice of a Generalized Multicategory]]**
	- For a multicategory $C$, the **slice** $C^+$ is a new multicategory whose objects are the operations (multimaps) of $C$, and whose multimaps are the configurations in which several operations of $C$ are pasted together to build one operation of $C$. Slicing is defined so that $\mathrm{Alg}(C^+) \simeq \mathbf{Multicat}_{\mathrm{ob}(C)}/C$ — algebras for the slice are multicategories-over-$C$ — which pins down its operations as "pasting diagrams of operations of $C$". It is the categorical incarnation of "raise the dimension by one": objects of $C^+$ live one level up from objects of $C$. For generalized (cartesian-monad) multicategories the same construction works verbatim, which is the version Baez and Dolan needed.

- **[[Def - Opetope]]**
	- An **opetope** is a cell shape produced by iterating the slice construction on the identity operad $I = 1$. The $0$-opetope is the point; the $1$-opetope is the arrow; an $n$-opetope (for $n \geq 1$) is a "many-in, one-out" pasting diagram of $(n-1)$-opetopes, recorded combinatorially by a tree (Appendix E). Equivalently, the set $\mathcal{O}_n$ of $n$-opetopes is the object-set of the $n$-fold slice $1^{+\cdots+}$. There is exactly one $0$- and one $1$-opetope; the $2$-opetopes are indexed by arities $0, 1, 2, \dots$ (the "$n$ inputs, one output" cells); higher opetopes proliferate as labelled trees of trees.

> [!tip] Unlocked: The Free Multicategory on a Graph *(from [[Def - Operad|Operad]] Theory)*
> The operations of a free multicategory are exactly **trees** whose edges are typed by objects and whose vertices are typed by generating operations — and trees are the combinatorial backbone of the slice construction. Once you can describe the slice $C^+$, you can describe **free multicategories** and the monad that builds them, because a pasting diagram of operations *is* an element of the free multicategory on the underlying data.

- **[[Thm - Opetopes via Iterated Slicing of the Identity Operad]]**
	- Starting from the identity operad $I = 1$ and forming the chain $I, I^+, I^{++}, \dots$, the objects of the $n$-th term are precisely the $n$-opetopes, and the operations of the $n$-th term are the $(n+1)$-opetopes. This is the theorem that makes "an $n$-opetope is a pasting diagram of $(n-1)$-opetopes" literally true rather than a slogan: the slice turns the operations of one level into the objects of the next. The base cases recover the point and the arrow, and the first slice recovers the classical "many-in, one-out" 2-cells whose arities are the natural numbers.

- **[[Ex - Drawing the low-dimensional opetopes as trees]]** (⭐)
	- Instantiate the opetope recursion in dimensions $0$–$3$, drawing each cell as a finite rooted planar tree and reading off its source and target faces; confirm $|\mathcal{O}_0| = |\mathcal{O}_1| = 1$ while $\mathcal{O}_2$ is already infinite.

- **[[Ex - The 2-opetopes are indexed by arity via the first slice]]** (⭐⭐)
	- Compute $\mathrm{ob}(I^{++})$ directly from the terminality of the identity operad to prove $\mathcal{O}_2 \cong \mathbb{N}$, one $2$-opetope per arity, watching the arity grading of $I$'s operations survive the slice.

- **[[Ex - The slice of an ordinary category records factorisations]]** (⭐⭐)
	- Unwind the slice on an arity-one multicategory (an ordinary category): its objects are the arrows, its operations are factorisations, and it is *not* the ordinary slice category $\mathcal{D}/X$ — the arity-one degeneration sits inside the opetopic world.

> [!note] Exercise Index — §7.1
> [[Exercise Index - §7.1 Opetopes and the Slice Construction]]

## §7.2 Opetopic Sets

- **[[Def - Opetopic Set]]**
	- The opetopes form a category $\mathbb{O}$ (objects: all opetopes of all dimensions; morphisms: the face inclusions and degeneracy-like maps assembling lower opetopes into the boundary of higher ones). An **opetopic set** is a presheaf $X : \mathbb{O}^{op} \to \mathbf{Set}$: it assigns to each opetope $O$ a set $X_O$ of "$O$-shaped cells" and to each face map a restriction operation, compatibly. This is the exact analogue of a [[Def - Simplicial Set|simplicial set]] (a presheaf on $\Delta$) and of a globular set (a presheaf on $\mathbb{G}$): the same *idea*, with the indexing category swapped from simplices or globes to opetopes. The representable opetopic sets $\mathbf{y}O$ are the "standard cells", the analogues of $\Delta^n$.

> [!tip] Unlocked: Nerve Construction for Opetopic Categories *(from Higher Category Theory)*
> Just as the **nerve** turns a category into a [[Def - Simplicial Set|simplicial set]] and the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterizes categories among simplicial sets]] by a unique-filler condition, an opetopic-set nerve will turn an opetopic structure into a presheaf on $\mathbb{O}$, and "being a weak $n$-category" becomes a filler condition (next section). The presheaf-on-shapes pattern is one machine reused with three different shape categories: $\Delta$, $\mathbb{G}$, $\mathbb{O}$.

> [!tip] Unlocked: Topos of [[Def - Opetopic Set|Opetopic Sets]] *(from Topos Theory)*
> Any presheaf category $[\mathbb{O}^{op}, \mathbf{Set}]$ is an elementary **topos**: it has all [[Def - Limit and Colimit|limits and colimits]], exponentials, and a subobject classifier, computed pointwise. So opetopic sets inherit, for free, a logic and a geometry — the same structural windfall that makes [[Def - Simplicial Set|simplicial sets]] and presheaves so workable.

- **[[Ex - An opetopic set is a presheaf, unwound]]** (⭐)
	- Translate "presheaf on $\mathbb{O}$" into elementary data — a set of cells per opetope, restriction maps per face, functoriality — getting the contravariance right, and spell out what the arity-$2$ restrictions impose (two source and one target $1$-cell).

- **[[Ex - The representable opetope as the standard cell via Yoneda]]** (⭐⭐)
	- Instantiate the [[Thm - The Yoneda Lemma|Yoneda lemma]] at $\mathbb{O}$ to show $O$-cells of $X$ are maps $\mathbf{y}O \to X$; deduce $\mathbf{y}O$ is the free opetopic set on one $O$-cell (the analogue of $\Delta^n$) and that the Yoneda embedding is fully faithful.

- **[[Ex - Colimits of opetopic sets are computed pointwise]]** (⭐⭐)
	- Inherit cocompleteness from the presheaf setting — colimits computed pointwise — and glue two standard cells along a shared boundary arrow via a pointwise pushout, the opetopic version of attaching cells in a complex.

> [!note] Exercise Index — §7.2
> [[Exercise Index - §7.2 Opetopic Sets]]

## §7.3 The Opetopic Definition of Weak n-Categories

- **[[Thm - Baez-Dolan Opetopic Weak n-Categories]]**
	- A **Baez–Dolan opetopic weak $n$-category** is an opetopic set in which every "niche" — a many-in, one-out configuration of cells waiting for a composite — admits a **universal** filler, and these universal fillers exist coherently up to dimension $n$ (above which cells become unique/invertible). The universal cell plays the role of the chosen composite, and its universal property replaces the strict equations of an ordinary category. This is the opetopic answer to "what is a weak higher category": composition is not given by an operation but recognised by a universal property of certain cells, exactly as a [[Def - Limit and Colimit|limit]] is recognised by a universal property rather than constructed by a formula. For $n = 1$ it reproduces ordinary categories; the framework runs uniformly in all $n$.

> [!tip] Unlocked: Comparison of Definitions of Weak n-Category *(from Higher Category Theory)*
> The opetopic definition is one of many — Batanin–Leinster globular, Penon, Tamsamani–Simpson, Segal, quasi-categories. **Cheng's comparison** theorems and the broader **comparison problem** ask whether these agree; the opetopic and multitopic variants (**multitopes**, Hermida–Makkai–Power) are now known to be tightly related. This section is the on-ramp to that comparison.

> [!tip] Unlocked: The Stabilization Hypothesis *(from Higher Category Theory)*
> Baez and Dolan introduced opetopes precisely to state the **stabilization hypothesis** — that $k$-tuply monoidal $n$-categories stop changing once $k \geq n+2$ — and the **periodic table** of higher categories. The opetopic shapes are the scaffolding on which those conjectures are phrased.

- **[[Ex - At n equals 1 the universal filler condition gives a category]]** (⭐⭐)
	- Unwind the universal-filler condition at $n = 1$ (with trivial $2$-cells) to recover a unique composite for every composable string, and show universality forces associativity and the unit laws — the $n = 1$ calibration against ordinary categories.

- **[[Ex - At n equals 2 the universal fillers reproduce a bicategory]]** (⭐⭐⭐)
	- Extract weak horizontal composition from universal $2$-cell fillers and the associator and unitors from universal $3$-cell fillers, and show the pentagon and triangle coherence axioms are forced — the $n = 2$ calibration against [[Def - 2-Category and Bicategory|bicategories]].

- **[[Ex - A niche without a filler is the obstruction to composition]]** (⭐⭐)
	- Exhibit an opetopic set whose niches have fillers but no *universal* ones, giving a multivalued, non-canonical composition that fails to be a category; conclude that universality (not mere existence) is the indispensable hypothesis.

> [!note] Exercise Index — §7.3
> [[Exercise Index - §7.3 The Opetopic Definition of Weak n-Categories]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The work of this chapter, and of opetopic higher category theory generally, falls into a handful of recurring goals. The first is **identifying the opetopes in a given dimension**: write down, combinatorially, exactly which cells exist in dimension $n$, usually by exhibiting the bijection with a class of trees. A second target is **establishing that a construction is presheaf-theoretic** — showing that opetopic sets really do form a presheaf category, that the slice of a presheaf category is again one, so that all the standard machinery (limits, colimits, the [[Thm - The Yoneda Lemma|Yoneda lemma]], representables) is available. A third is **proving that the recursion bottoms out correctly**: that iterated slicing of $I = 1$ reproduces the point and arrow at the bottom and the right "many-in, one-out" shapes above. A fourth, the deepest, is **showing the opetopic definition is correct** — that it reproduces ordinary categories at $n = 1$, bicategories at $n = 2$ (where it must be compared against the [[Def - 2-Category and Bicategory|bicategory]] definition), and so on, and that it agrees with rival definitions (the comparison problem). A fifth, more conceptual, is **transporting a familiar categorical pattern to the opetopic world**: a nerve, a fundamental-groupoid-like functor, a Yoneda statement. These five — enumerate the cells, prove it is a presheaf category, verify the recursion, validate the definition, transport a pattern — are the targets, and they recur because each pins down a different face of "what the opetopic framework is and that it works".

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A multicategory or generalized multicategory is given**, which is the raw material the slice construction eats; the moment you have one, you have its slice and hence a new collection of shapes one dimension up. **The base object is the identity operad $I = 1$**, the simplest law, which is what makes the whole tower canonical rather than dependent on choices. **A cartesian monad is in play** (the generalized-multicategory setting), which is what lets the slice construction work uniformly and lets us *iterate* it; cartesianness is the property that the relevant pullbacks and free structures exist. **The shapes are trees** (Appendix E), so any claim about opetopes can be reduced to a claim about finite planar rooted trees, where induction on the number of vertices is available. **The ambient category is a presheaf topos**, so limits, colimits, exponentials, and Yoneda are free. The recurring move is to route a source to a target: a given generalized multicategory routes through the slice to a new dimension of shapes; the tree description routes through tree induction to an enumeration; the presheaf-topos source routes through Yoneda to a representability or nerve statement. The [[Higher Categories — Opetopes and Opetopic Sets#Problem-Solving Strategy|Problem-Solving Strategy]] section makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this topic is assembled from. When stuck, scan the list. Everything here is self-contained: a reader who knows only ordinary category theory should be able to follow each operation from its description.

**Legal operations:**

1. **Slice a multicategory to climb one dimension.** Given a multicategory $C$, form $C^+$: its objects are the operations of $C$, its operations are the pasting diagrams of operations of $C$. Use this whenever the problem is about cells one level above the ones you currently understand. *Trigger:* the problem mentions $(n+1)$-cells while you only have $n$-cells in hand. *Pattern:* "the $(n+1)$-opetopes are the operations of the $n$-th slice, so slice once more and read off the new objects."

2. **Read a cell off as a tree.** Every opetope corresponds to a finite, rooted, **planar** tree (Appendix E): the root edge is the output, the leaf edges are the inputs, the internal structure records how lower cells are pasted. Use this to make any opetope concrete and to enable induction. *Trigger:* "describe / count / draw the $n$-opetopes." *Pattern:* "translate to trees, then induct on the number of vertices or leaves."

3. **Take the presheaf on a shape category.** Once you have a category of shapes $\mathbb{O}$, the structures built from those shapes are presheaves $\mathbb{O}^{op} \to \mathbf{Set}$. Use this to import all of ordinary category theory at once. *Trigger:* "what is a [collection of opetopic cells glued along faces]?" *Pattern:* "it is a presheaf on $\mathbb{O}$; now [[Thm - The Yoneda Lemma|Yoneda]], representables, limits and colimits all apply."

4. **Invoke Yoneda to turn a cell into a representable.** For an opetope $O$, the representable opetopic set $\mathbf{y}O = \mathbb{O}(-, O)$ is the "standard $O$-cell". By the [[Thm - The Yoneda Lemma|Yoneda lemma]], maps $\mathbf{y}O \to X$ correspond to $O$-cells of $X$, i.e. elements of $X_O$. Use this to convert statements about cells into statements about maps of opetopic sets. *Trigger:* "an $O$-cell of $X$" appears as data. *Pattern:* "replace it by a map $\mathbf{y}O \to X$ and reason diagrammatically."

5. **Recognise a niche and demand a filler.** A *niche* is a many-in, one-out configuration of cells with the inputs and the boundary specified but the composite missing. In a weak $n$-category every niche has a chosen **universal** filler. Use this in place of "composing": you never write a formula for a composite; you assert the universal filler exists. *Trigger:* "compose these cells." *Pattern:* "form the niche, take its universal filler — that is the composite, and the filling cell is the witness."

6. **Identify a universal property in lieu of an equation.** Where an ordinary category would demand $h = g \circ f$ on the nose, the opetopic framework asks the relevant cell to be *universal* (initial/terminal among fillers of its niche), exactly as a [[Def - Limit and Colimit|limit]] is universal rather than formulaic. *Trigger:* a coherence condition that would be an equation in the strict world. *Pattern:* "weaken the equation to a universal property of a filling cell."

7. **Truncate to recover a known structure.** Discarding all opetopes above dimension $n$ (and forcing the surviving top cells to be invertible/unique) collapses the framework to a lower-dimensional one. Use this to test a definition against known cases. *Trigger:* "does this reproduce categories / bicategories?" *Pattern:* "truncate at $n = 1$ (expect ordinary categories) or $n = 2$ (expect [[Def - 2-Category and Bicategory|bicategories]])."

8. **Use that slicing preserves good ambient structure.** The slice of a presheaf category is again a presheaf category, and the slice of a cartesian monad is again cartesian. Use this to guarantee that the tower $I, I^+, I^{++}, \dots$ stays inside a world where all the tools work. *Trigger:* "is $C^+$ still nice enough to slice again?" *Pattern:* "cartesian/presheaf-ness is closed under slicing, so the iteration never leaves the good category."

**Illegal but tempting operations:**

> [!warning] 1. Treating an opetope as a globe or a simplex
> It is tempting to picture the $n$-cells of every higher-category framework as the same shape and to swap freely between opetopes, **globes**, and simplices. They differ in their *source*: a globe has a single source face and a single target face (one-in, one-out); a simplex's faces are themselves simplices in a totally ordered pattern; an opetope is **many-in, one-out** — its target is a single cell but its source is a *pasting diagram* of cells. Concretely, the $2$-globe has a $1$-cell source and a $1$-cell target, whereas a $2$-opetope can have *five* $1$-cells in its source and one in its target. They become interchangeable only after passing to the [[Def - Homotopy|homotopy]]/weak-equivalence level, where the choice of shape washes out; at the level of cells they are genuinely different categories $\mathbb{G}, \Delta, \mathbb{O}$, and a presheaf on one is not a presheaf on another.

> [!warning] 2. Defining composition as an operation on cells
> In an ordinary category, and even in a strict $n$-category, composition is a function: feed in composable cells, get out *the* composite. It is tempting to demand the same of a weak opetopic $n$-category. This fails to be the right structure: in the weak world the composite is not determined, only determined-up-to-a-universal-cell, and insisting on a chosen function reintroduces strictness and breaks the comparison with bicategories. The standard witness is already at $n = 2$: a bicategory's composition is associative only up to a non-identity associator, so a *function* "compose three 1-cells" has no well-defined value — there are two bracketings and an isomorphism between them. The repair is operation 5: replace the function by the existence of a universal filler.

> [!warning] 3. Assuming there are finitely many opetopes in each dimension
> Because there is exactly one $0$-opetope and one $1$-opetope, it is tempting to expect a small finite list in every dimension, as for globes (one globe per dimension). This is false from dimension $2$ onward: there is one $2$-opetope for *each* arity $n = 0, 1, 2, \dots$ (the "$n$ inputs, one output" cell), so already $\mathcal{O}_2$ is countably infinite, and $\mathcal{O}_3$ is the set of trees-of-those, which grows combinatorially. The globular intuition ("one shape per dimension") is exactly what opetopes give up in exchange for native many-in, one-out pasting. The fix is operation 2: count via trees, expecting infinite families.

> [!warning] 4. Symmetrising the inputs of an operation
> When working with the plain (non-symmetric) multicategories that give the cleanest opetopes, it is tempting to permute the inputs of an operation freely, as one would in a symmetric multicategory or an operad with $S_n$-action. For the opetopic combinatorics this is illegal: the inputs carry a fixed linear order, which is exactly the planarity of the trees in Appendix E. Permuting them collapses distinct opetopes together and destroys the tree bijection. The symmetric version (Baez–Dolan's original) is legitimate but produces a *different*, coarser shape category; if you want plain opetopes you must keep the order, and the repair condition is simply "stay non-symmetric, keep the trees planar."

---

# Problem-Solving Strategy

The problems in this topic are won at the moment you decide which of two worlds you are in: the **combinatorial** world of describing and counting shapes, or the **structural** world of presheaves and universal properties. Almost every exercise is one of a few types, and each has a characteristic route.

If the problem **asks you to describe, draw, or count the opetopes of a given dimension**, you are in the combinatorial world, and your primary instrument is the slice construction together with the tree description of Appendix E. The route is always the same: the $n$-opetopes are the objects of the $n$-th slice $1^{+\cdots+}$, which by [[Thm - Opetopes via Iterated Slicing of the Identity Operad|the iterated-slicing theorem]] are the *operations* of the $(n-1)$-th slice, which are *pasting diagrams* of $(n-1)$-opetopes, which are *trees* whose vertices are labelled by $(n-1)$-opetopes. So you translate the question down one dimension into a question about trees, and induct. For $n = 2$ this collapses to "how many inputs does the cell have", giving one $2$-opetope per natural number; for $n = 3$ you are counting trees built from those, and the count is no longer finite. The single most useful habit is to **draw the low cases by hand** — the unique $0$- and $1$-opetopes, the family of $2$-opetopes, the first few $3$-opetopes — because the recursion is opaque until you have seen it produce concrete shapes.

If the problem **asks you to show that the opetopic structures form a presheaf category, or to apply a categorical theorem to them**, you are in the structural world, and the route runs through the [[Def - Presheaf|presheaf]] and [[Thm - The Yoneda Lemma|Yoneda]] machinery. The key recognition is that "a collection of cells of every opetopic shape, glued along source and target faces" is *by definition* a functor $\mathbb{O}^{op} \to \mathbf{Set}$, so the question is never really about opetopes specifically — it is the same statement that holds for any presheaf category, instantiated at $\mathbb{O}$. Limits and colimits exist and are computed pointwise; representables $\mathbf{y}O$ are the standard cells; the Yoneda lemma identifies $O$-cells of $X$ with maps $\mathbf{y}O \to X$. The discipline is to *forget that the shapes are opetopes* and prove the general presheaf statement, then re-specialise.

If the problem **asks you to verify that the opetopic definition of weak $n$-category is correct in a low case** — that $n = 1$ gives ordinary categories, $n = 2$ gives [[Def - 2-Category and Bicategory|bicategories]] — the route is to unwind the universal-filler condition explicitly and match it against the known definition. The strategy is to take the abstract "every niche has a universal filler" and write out, for $n = 1$, exactly what niches and fillers are (composable arrows and their composites), checking that universality reproduces the category axioms; then for $n = 2$, that it reproduces the associator and unitor data of a bicategory. The non-obvious part is always that universality does the work of an equation: where the strict definition would impose $h = g \circ f$, the opetopic definition imposes that a certain cell be universal, and you must check these say the same thing in the low case.

Finally, a meta-strategy threads through all of the above: **every question in this chapter is the question "what is the shape, and how is it glued?"** Whether you are slicing, drawing trees, taking presheaves, or demanding fillers, you are always either generating a shape (slice / tree) or gluing shapes together (presheaf / niche). When stuck, ask which of those two you are doing, and the relevant operation from the Legal Operations list will be the next move. The reason this works is that the opetopic framework deliberately separates *shapes* (the category $\mathbb{O}$, fixed once and for all by slicing) from *structure* (presheaves on $\mathbb{O}$, and filler conditions on them) — and almost no problem requires both at once.

---

# Most Reusable Properties

- **[[Def - The Slice of a Generalized Multicategory|The slice construction C ↦ C⁺]]**: turns operations into objects and pasting-diagrams-of-operations into operations. This is the most-reused single idea in the chapter because it is the *only* generator of new dimensions: every opetope of every dimension comes from iterating it. **Typical use:** whenever a problem reaches for "$(n+1)$-cells", slice once more and read the new objects. Its most powerful disguised use is structural — slicing preserves cartesianness and presheaf-ness, so the iteration never leaves the good category, which is what licenses the infinite tower $I, I^+, I^{++}, \dots$ in the first place.

- **[[Def - Opetope|The tree description of opetopes]]**: every opetope is a finite rooted planar tree (Appendix E), with the root as output and leaves as inputs. This is more reusable than any single enumeration because it converts *every* combinatorial question about opetopes into a question about trees, where induction on vertices or leaves is available. **Typical use:** to count, draw, or define an operation on opetopes, translate to trees first; the planar structure is exactly the input-ordering data of a non-symmetric operation.

- **[[Def - Opetopic Set|Opetopic sets are a presheaf category]]**: $[\mathbb{O}^{op}, \mathbf{Set}]$. The reusable move is the identification itself — once you know your structures are presheaves, you inherit limits, colimits, exponentials, a subobject classifier, and the [[Thm - The Yoneda Lemma|Yoneda lemma]] for free, with everything computed pointwise. **Typical use:** any time you must build, glue, or quotient opetopic data, do it pointwise as a presheaf operation; any time you handle a single cell, replace it by a map out of a representable.

- **[[Thm - The Yoneda Lemma|The Yoneda lemma on 𝕆]]**: $O$-cells of an opetopic set $X$ are the same as maps $\mathbf{y}O \to X$. This is the bridge between the combinatorial and structural worlds: it lets you take a shape (an opetope $O$) and turn it into an object of the presheaf category (the representable $\mathbf{y}O$) whose maps probe $X$. **Typical use:** to phrase a filler condition, express the niche and its candidate fillers as maps of representables, then the universal property becomes a lifting/extension statement.

- **The universal-filler condition** (from [[Thm - Baez-Dolan Opetopic Weak n-Categories|the opetopic definition]]): composition is recognised, not computed. The reusable principle is that *a weak composite is a universal cell*, never a formula. **Typical use:** whenever you would write "let $g \circ f$ be the composite", instead form the niche and assert its universal filler; this is the move that makes everything coherent up the dimensions without an infinite regress of equations, exactly as universal properties tame [[Def - Limit and Colimit|limits]].

---

# Bridges

1. **Simplicial sets and the simplex category.** A [[Def - Simplicial Set|simplicial set]] is a presheaf $\Delta^{op} \to \mathbf{Set}$, where $\Delta$ is the category whose objects are the finite ordinals $[n] = \{0 < 1 < \dots < n\}$ and whose maps are the order-preserving functions; the representables $\Delta^n = \Delta(-, [n])$ are the standard simplices, and a general simplicial set is built by gluing simplices along their faces. The opetopic story is the *same construction with a different shape category*: replace $\Delta$ by the category of opetopes $\mathbb{O}$, replace the standard simplices $\Delta^n$ by the representable opetopes $\mathbf{y}O$, and a [[Def - Opetopic Set|opetopic set]] is built by gluing opetopes along their source and target faces. The reason the two theories feel parallel is that they *are* parallel — both are instances of "presheaves on a category of cell-shapes" — and the difference is entirely in the shapes: simplices are totally ordered, opetopes are many-in, one-out. Where simplicial sets model $(\infty,1)$-categories via the [[Def - Quasi-Category|quasi-category]] inner-horn-filler condition, opetopic sets model weak $n$-categories via the universal-filler condition.

2. **Globular sets and the globe category.** A globular set is a presheaf on the globe category $\mathbb{G}$, whose objects $[0], [1], [2], \dots$ are the globes and whose maps are generated by two parallel "source" and "target" inclusions $s, t : [n-1] \rightrightarrows [n]$ satisfying $ss = ts$ and $st = tt$. A globular set is thus a tower of sets of $n$-cells, each cell having a single source $(n-1)$-cell and a single target $(n-1)$-cell — the one-in, one-out shape used by Batanin–Leinster weak $\omega$-categories. Opetopes differ in precisely the source: an $n$-opetope's target is a single $(n-1)$-opetope, but its source is a *pasting diagram* of $(n-1)$-opetopes. So **globular sets are to globes as opetopic sets are to opetopes**, and the choice between them is the choice between one-in-one-out cells (globular) and many-in-one-out cells (opetopic) — two routes to the same destination of "weak higher category", whose equivalence is part of the comparison problem.

3. **Operads, multicategories, and free structures.** A multicategory is a category whose arrows accept a *list* of inputs; an operad is a one-object multicategory, i.e. a graded set of operations with a composition law (substitution). The slice $C^+$ is built directly from this composition law: its operations are pasting diagrams, which are exactly the elements of a *free* multicategory built on the operations of $C$. So the opetopic tower is a tower of free constructions, and the trees of Appendix E are nothing other than the elements of free multicategories — the same trees that index the operations of the free operad. This is why the identity operad $I = 1$ is the natural starting point: it is the operad with the simplest possible composition, and slicing it repeatedly grows the trees one level at a time.

4. **Limits and universal properties.** The single conceptual import from ordinary category theory is that **composition can be a universal property instead of a formula**. A [[Def - Limit and Colimit|limit]] of a diagram is not computed by a formula but characterised as the universal cone; the opetopic weak composite is characterised, identically, as the universal filler of a niche. This is the bridge that makes the definition coherent: just as a limit, being universal, is unique up to unique isomorphism and composes well with other limits, a universal filler is essentially unique and the coherence cells between different ways of composing are forced, not imposed. The opetopic definition is, at heart, the observation that *the category axioms themselves are universal properties* once you allow the composite to be witnessed rather than equated.

---

# Insights

**The unifying frame: separate the shapes from the structure.** The deepest organising idea of opetopic higher category theory — and of simplicial and globular theory alike — is to factor the problem into two independent halves. First, fix once and for all a *category of cell-shapes*: $\Delta$ for simplices, $\mathbb{G}$ for globes, $\mathbb{O}$ for opetopes. This half is pure combinatorics, and for opetopes it is generated mechanically by slicing the identity operad. Second, define your structures as *presheaves on those shapes*, possibly subject to a filler condition: a simplicial set is just a presheaf, a quasi-category is a presheaf with inner-horn fillers, a weak $n$-category is an opetopic set with universal fillers. Once you see this factorisation, the bewildering zoo of higher-category definitions organises itself: they differ in *which shape category* and *which filler condition*, and almost nothing else. The opetopic choice is "many-in, one-out shapes, with universal fillers", and the reason to prefer it is that many-in, one-out is the *native* shape of composition — composing several things into one is what categories actually do.

**The true name of the slice construction is "raise the dimension by one".** Officially, $C^+$ is defined by the equivalence $\mathrm{Alg}(C^+) \simeq \mathbf{Multicat}/C$, which is precise but tells you nothing about why you would build it. Operationally, slicing is the one move that turns the *operations* of a structure into the *objects* of a new structure, and the *ways of pasting those operations* into the new operations. That is exactly what "go up a dimension" means: yesterday's morphisms are today's objects, and yesterday's pasting diagrams are today's morphisms. The entire opetopic tower is this single move applied over and over, which is why a chapter that could have been a forest of combinatorial definitions reduces to "iterate one functor on one starting object." When you see $C^+$, do not picture an algebra equivalence; picture cells climbing one rung up the ladder.

**Why "many-in, one-out" is forced, not chosen.** It is natural to ask why opetopes have many sources and one target rather than the symmetric many-in-many-out, or the rigid one-in-one-out of globes. The answer is that composition is asymmetric in exactly this way: you compose a *string* of arrows (many) into a *single* arrow (one), you paste a *diagram* of 2-cells (many) into a *single* 2-cell (one). The output of a composition is always one thing; the input is always a configuration. Opetopes are the shapes that make this asymmetry primitive, which is why their source is a pasting diagram (a tree, recording the configuration) and their target is a lone cell (the result). The many-in-many-out generalisation exists (Section 7.6 of Leinster, the "many in, many out" variant) and leads to the theory of *PROPs* and string diagrams, but it is a genuinely different and more permissive world; the many-in, one-out restriction is what keeps opetopes tied to ordinary composition.

**Trigger–reaction: when you see "$(n+1)$-cell", reach for the slice; when you see "cell of $X$", reach for Yoneda.** Two reflexes carry most of the chapter. First, any time a problem escalates a dimension — asking about $(n+1)$-opetopes given $n$-opetopes, or about cells one level up — the move is to slice once more, because the operations of the $n$-th slice *are* the $(n+1)$-cells. Second, any time a single cell of an opetopic set $X$ appears as data, replace it by a map $\mathbf{y}O \to X$ out of the corresponding representable, because the [[Thm - The Yoneda Lemma|Yoneda lemma]] makes these literally the same thing, and maps of presheaves are far easier to manipulate than raw cells. Internalising these two reflexes turns most of the exercises into routine applications of the slice construction and of Yoneda.
