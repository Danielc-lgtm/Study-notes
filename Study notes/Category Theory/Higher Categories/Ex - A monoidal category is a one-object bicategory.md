---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that a one-object [[Def - 2-Category and Bicategory|bicategory]] is the same data as a [[Def - Monoidal Category|monoidal category]]. Precisely: given a bicategory $\mathcal{B}$ with a single $0$-cell $\star$, construct a monoidal category $\mathcal{M}$, and conversely; verify that the associator/unitor data and the pentagon/triangle axioms correspond exactly under the dictionary

$$\text{1-cells } \star\to\star \;\longleftrightarrow\; \text{objects of } \mathcal{M}, \qquad \text{horizontal composition} \;\longleftrightarrow\; \otimes, \qquad \text{identity 1-cell } 1_\star \;\longleftrightarrow\; \text{unit } I.$$

**Recall:**

![[Def - Monoidal Category#The Definition]]

A [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$ has $0$-cells; for each pair of $0$-cells a hom-*category* of $1$-cells and $2$-cells; horizontal composition functors; identity $1$-cells; and coherent invertible $2$-cells — the associator $a_{f,g,h}:(h\ast g)\ast f\Rightarrow h\ast(g\ast f)$ and unitors $l_f, r_f$ — satisfying the pentagon and triangle axioms. A [[Def - Monoidal Category|monoidal category]] $(\mathcal{M},\otimes,I,a,l,r)$ is a category with a tensor bifunctor, a unit object, and coherent associativity/unit isomorphisms satisfying pentagon and triangle.

---

# Convergent Strategy

**Problem class:** This is an "equate two definitions" / "recognise a degenerate case" problem — the second target in the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to set up a dictionary between the two structures' data, then check that each axiom of one becomes an axiom of the other under the dictionary. The difficulty is bookkeeping: there is a lot of data, and a single mismatched arrow (e.g. an associator pointing the wrong way) breaks the correspondence.

**Assumption pattern:** The recognisable feature is "one object". Collapsing the unique $0$-cell removes the source/target bookkeeping of $1$-cells: every $1$-cell is an endo-$1$-cell $\star\to\star$, so *all* $1$-cells are composable with all others. This is exactly what makes horizontal composition into a single binary operation on one collection — a tensor product — rather than a partially-defined composition.

**Theorem routing:** No external theorem is needed; the route is purely the unwinding of [[Def - 2-Category and Bicategory|the bicategory definition]] against [[Def - Monoidal Category|the monoidal category definition]], using Legal Operation 6 (recognise a one-object case as a monoid-like structure). The pentagon and triangle of the bicategory map term-for-term onto those of the monoidal category.

**Key decision point:** The non-obvious choice is recognising that the bicategory's *hom-category* $\mathcal{B}(\star,\star)$ becomes the *whole* monoidal category $\mathcal{M}$ — its objects (the $1$-cells) become the objects of $\mathcal{M}$, and its morphisms (the $2$-cells) become the morphisms of $\mathcal{M}$. The most common error is to look for the objects of $\mathcal{M}$ among the $0$-cells of $\mathcal{B}$; there is only one $0$-cell, and it disappears entirely.

---

# Legal Operations Used

1. **Operation 6 (recognise a one-object case as a monoid-like structure).** A one-object bicategory has all its content in the single hom-category, with horizontal composition a binary operation on it — a categorified monoid, i.e. a monoidal category.

2. **Operation 5 (paste 2-cells / coherence).** Matching the pentagon and triangle requires identifying the associator and unitor $2$-cells of $\mathcal{B}$ with the coherence isomorphisms of $\mathcal{M}$ and checking the coherence diagrams coincide.

---

# Hints

> [!note]- Hint 1
> With one $0$-cell, how many hom-categories are there, and what plays the role of "the category $\mathcal{M}$"? Where do the objects of $\mathcal{M}$ come from — the $0$-cells, the $1$-cells, or the $2$-cells?

> [!note]- Hint 2
> Horizontal composition of $1$-cells is a functor $\mathcal{B}(\star,\star)\times\mathcal{B}(\star,\star)\to\mathcal{B}(\star,\star)$. A functor of this shape on a category is exactly a tensor bifunctor. The identity $1$-cell $1_\star$ is the unit object.

> [!note]- Hint 3
> The associator $a_{f,g,h}:(h\ast g)\ast f\Rightarrow h\ast(g\ast f)$, read with $\ast = \otimes$ and $1$-cells as objects, is exactly $a_{A,B,C}:(A\otimes B)\otimes C\to A\otimes(B\otimes C)$ (after matching the variable order). The bicategory pentagon becomes the monoidal pentagon verbatim.

---

# Solution

The proof is a dictionary plus two axiom checks. The plan: Step 1 sets up the data correspondence (objects, tensor, unit, coherence cells); Step 2 verifies that bicategory composition gives a bifunctor (interchange becomes bifunctoriality of $\otimes$); Step 3 matches the pentagon and triangle; Step 4 notes the construction is invertible, giving an equivalence of the two notions.

**Step 1: The data dictionary.** Set $\mathcal{M} = \mathcal{B}(\star,\star)$: objects of $\mathcal{M}$ are the $1$-cells $\star\to\star$, morphisms of $\mathcal{M}$ are the $2$-cells. Tensor $A\otimes B := A\ast B$ (horizontal composition), unit $I := 1_\star$, and the coherence isomorphisms of $\mathcal{M}$ are the associator and unitors of $\mathcal{B}$.

> [!note]- Derivation
> Because $\mathcal{B}$ has a single $0$-cell, there is exactly one hom-category, $\mathcal{B}(\star,\star)$, and we take it to be $\mathcal{M}$. Its objects are the $1$-cells (which all share source and target $\star$, hence are all mutually composable), and its morphisms are the $2$-cells, with vertical composition $\circ$ as composition in $\mathcal{M}$. The $0$-cell $\star$ carries no further data and is discarded. Horizontal composition restricts to a functor on $\mathcal{B}(\star,\star)\times\mathcal{B}(\star,\star)$, which we call $\otimes$. The identity $1$-cell $1_\star$ has no other role than to be a tensor unit, so $I := 1_\star$.

**Step 2: Tensor is a bifunctor.** Horizontal composition is a functor in $\mathcal{B}$, so $\otimes$ is a bifunctor; the underlying interchange law becomes the bifunctoriality $(\beta'\circ\beta)\otimes(\alpha'\circ\alpha) = (\beta'\otimes\alpha')\circ(\beta\otimes\alpha)$.

> [!note]- Derivation
> In a bicategory, horizontal composition $\ast:\mathcal{B}(\star,\star)\times\mathcal{B}(\star,\star)\to\mathcal{B}(\star,\star)$ is a [[Def - Functor|functor]]. Under the dictionary this is exactly a bifunctor $\otimes:\mathcal{M}\times\mathcal{M}\to\mathcal{M}$. Functoriality on the product category — preservation of (vertical) composition and identities — is precisely the [[Thm - The Interchange Law|interchange law]], which reads as the bifunctoriality (Godement) law for $\otimes$. So $\otimes$ is a genuine bifunctor, the first requirement of a monoidal category.

**Step 3: Pentagon and triangle match.** The associator and unitors of $\mathcal{B}$, transported by the dictionary, satisfy the monoidal pentagon and triangle because they satisfy the bicategory pentagon and triangle.

> [!note]- Derivation
> The associator $a_{f,g,h}:(h\ast g)\ast f\Rightarrow h\ast(g\ast f)$ becomes, writing $1$-cells as objects $A=f, B=g, C=h$ and $\ast=\otimes$, the natural isomorphism $a_{A,B,C}:(A\otimes B)\otimes C\to A\otimes(B\otimes C)$ (matching Leinster's variable order). The unitors $l_f:1_\star\ast f\Rightarrow f$ and $r_f:f\ast 1_\star\Rightarrow f$ become $l_A:I\otimes A\to A$ and $r_A:A\otimes I\to A$. The bicategory pentagon — the commuting pentagon of associators for four composable $1$-cells — is, term for term, the monoidal pentagon for four objects; the bicategory triangle is the monoidal triangle. No new content appears; the axioms are literally the same diagrams. Hence $(\mathcal{M},\otimes,I,a,l,r)$ is a monoidal category.

**Step 4: The correspondence is invertible.** Conversely, a monoidal category yields a one-object bicategory by reversing the dictionary, and the two constructions are mutually inverse.

> [!note]- Derivation
> Given $(\mathcal{M},\otimes,I,a,l,r)$, define a bicategory $\mathcal{B}$ with one $0$-cell $\star$, hom-category $\mathcal{B}(\star,\star) := \mathcal{M}$, horizontal composition $\otimes$, identity $1$-cell $I$, and associator/unitors $a,l,r$. The pentagon and triangle of $\mathcal{M}$ are exactly those required of $\mathcal{B}$. Starting from a one-object bicategory, building $\mathcal{M}$, then rebuilding the bicategory returns the original data (and similarly the other way round), since at each step the dictionary is a bijection on data preserving all axioms. Hence one-object bicategories and monoidal categories are the same notion.

> [!note]- Complete formal solution
> Let $\mathcal{B}$ be a bicategory with one $0$-cell $\star$. Define $\mathcal{M} := \mathcal{B}(\star,\star)$, with $\otimes := \ast$ (horizontal composition), $I := 1_\star$, and coherence isomorphisms $a,l,r$ those of $\mathcal{B}$.
>
> - *$\mathcal{M}$ is a category:* its objects are the $1$-cells and its morphisms the $2$-cells, with vertical composition; this is a hom-category of $\mathcal{B}$, hence a category.
> - *$\otimes$ is a bifunctor:* horizontal composition is a functor $\mathcal{B}(\star,\star)^2\to\mathcal{B}(\star,\star)$, and its bifunctoriality is the [[Thm - The Interchange Law|interchange law]].
> - *Coherence:* $a_{A,B,C}, l_A, r_A$ are the associator and unitors of $\mathcal{B}$, natural and invertible, and they satisfy the monoidal pentagon and triangle because these are precisely the bicategory pentagon and triangle.
>
> Thus $(\mathcal{M},\otimes,I,a,l,r)$ is a [[Def - Monoidal Category|monoidal category]]. The reverse construction (Step 4) builds a one-object bicategory from a monoidal category, and the two are mutually inverse, establishing that the two notions coincide. $\quad\blacksquare$

> [!warning] Illegal but tempting: looking for $\mathcal{M}$'s objects among the $0$-cells
> One is tempted to make the objects of $\mathcal{M}$ correspond to $0$-cells of $\mathcal{B}$ — that is the dictionary for ordinary "category = special bicategory" intuition. But here there is *one* $0$-cell, and it has no internal structure to become the objects of $\mathcal{M}$. The objects of $\mathcal{M}$ are the *$1$-cells*. The categorical slogan that resolves the confusion: a monoidal category is a *one-object bicategory*, just as a monoid is a *one-object category* — in each case the structure shifts up one dimension, and the single bottom-dimensional cell vanishes.

---

# Key Takeaways

**Degeneracy shifts structure up a dimension — this is the master pattern of higher algebra.** A monoid is a one-object category (the single object's endomorphisms, under composition, form the monoid). A monoidal category is a one-object bicategory (the single object's endo-$1$-cells, under horizontal composition, form the tensor). A braided monoidal category is a one-object, one-$1$-cell tricategory. Each time you collapse the bottom dimension, the next-dimension composition becomes a binary operation on the surviving cells, and the coherence laws shift up too. Recognising "one object" as a trigger for this dimension shift lets you instantly translate between the language of higher categories and the language of monoidal/algebraic structures.

**The pentagon and triangle are dimension-independent — the same diagrams recur at every level.** What makes this correspondence clean is that the bicategory associator and the monoidal associator satisfy *identical* coherence diagrams; nothing is lost or added in the translation. This is why [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] for monoidal categories is exactly the one-object case of [[Thm - Strictification of Bicategories|coherence for bicategories]] — the proofs are the same Yoneda argument, run with $\otimes$ in place of horizontal composition. When you meet a pentagon in any context (monoidal categories, bicategories, $A_\infty$-structures), expect it to be the same coherence demand wearing different clothes, and expect a coherence theorem to tame it.

**Horizontal composition *is* the tensor product, and seeing this unifies two apparently separate theories.** Before this exercise, "monoidal category" and "bicategory" look like unrelated pieces of machinery; afterward they are one structure at two levels of degeneracy. The operational payoff is that every construction you know for monoidal categories — monoids in $\mathcal{M}$, module objects, the graphical/string-diagram calculus — immediately becomes a construction in a general bicategory by reading $\otimes$ as horizontal composition. A monoid in a monoidal category becomes a [[Def - 2-Category and Bicategory|monad]] in the corresponding bicategory; a module becomes a module over that monad. This translation is used constantly in higher algebra, and it all rests on the single identification proved here.
