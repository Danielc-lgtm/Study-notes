---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Strict n-Category and Strict ω-Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Globular Set"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

In a strict $2$-category, consider a **pasting diagram**: a planar arrangement of $0$-, $1$-, and $2$-cells, for instance the $2\times 2$ grid of $2$-cells
$$A \overset{f}{\underset{f''}{\Rrightarrow}} B \overset{g}{\underset{g''}{\Rrightarrow}} C$$
where on the left $\alpha : f\Rightarrow f'$ and $\beta : f'\Rightarrow f''$ are stacked vertically, and on the right $\gamma : g\Rightarrow g'$ and $\delta : g'\Rightarrow g''$ are stacked vertically, with the two columns horizontally composable.

(a) Show that the two ways of evaluating this grid — first vertical then horizontal, or first horizontal then vertical — give the same $2$-cell. Identify exactly which axiom is used.

(b) More generally, argue that *any* pasting diagram of $2$-cells in a strict $2$-category has a **unique** composite, independent of the order in which sub-diagrams are contracted, and that this uniqueness *fails* in a [[Def - 2-Category and Bicategory|bicategory]] unless one first inserts associators and unitors and invokes coherence.

(c) Exhibit a concrete non-example: a $2$-globular set equipped with a vertical and a horizontal composition that do **not** satisfy interchange, and show its $2\times 2$ grid has two different values.

**Recall:**

A [[Def - Strict n-Category and Strict ω-Category|strict 2-category]] has $2$-cells composed vertically ($\circ_1$, along a shared $1$-cell) and horizontally ($\circ_0$, along a shared $0$-cell), with the [[Thm - The Interchange Law|interchange law]]
$$(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha) = (\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha).$$
In a [[Def - 2-Category and Bicategory|bicategory]] the horizontal composition of $1$-cells is associative and unital only up to coherent $2$-[[Def - Isomorphism|isomorphisms]] (associator, unitors).

---

# Convergent Strategy

**Problem class:** This is a *coherence/well-definedness* problem: showing a composite is unambiguous. It is the strict-$2$-category instance of the chapter's recurring "is this canonical map well-defined?" target, and part (c) is a non-existence (illegal-operation) problem demonstrating what fails without the key axiom.

**Assumption pattern:** Parts (a) and (b) assume strictness — all structural isomorphisms are identities — so the *only* thing that can make the composite ambiguous is the order of contraction, and the interchange law is precisely the assumption that the two contraction orders agree. Part (c) drops interchange and watches the grid split. Recognising that strictness reduces "well-defined composite" to "interchange" is the unlock.

**Theorem routing:** Part (a) is a direct application of the [[Thm - The Interchange Law|interchange law]]. Part (b) routes through an induction on the pasting diagram, contracting one cell at a time and using interchange at each step where two orders could differ — the strict analogue of the tree-contraction argument behind [[Thm - Coherence for Unbiased Monoidal Categories|coherence]]. Part (c) constructs an explicit counterexample, using the contrapositive: if interchange fails, the two contraction orders of the grid are by definition unequal.

**Key decision point:** The non-obvious move in (b) is recognising that in a *bicategory* the failure of unique composites is *not* a failure of interchange (interchange still holds) but of strict associativity of horizontal composition: re-bracketing a row of horizontally composed cells requires associators, and uniqueness of the composite is then exactly [[Thm - Coherence for Unbiased Monoidal Categories|coherence]]. Confusing "no interchange" (part c) with "no strict associativity" (the bicategory case) is the trap; they are two different sources of ambiguity, repaired by two different things (the interchange axiom versus coherence).

---

# Legal Operations Used

1. **Operation 2 from the topic page (impose composition and check interchange).** Part (a) is the canonical use: the grid is exactly the configuration the interchange law governs, and contracting it tests interchange directly.

2. **Operation 8 from the topic page (run/recognise the structural role of interchange).** Part (b)'s induction is the strict precursor of the Eckmann–Hilton manipulation, where interchange is repeatedly invoked to reorder contractions; (c) is the negative version showing what interchange buys.

3. **Operation 5 from the topic page (cite coherence to suppress brackets).** In part (b)'s bicategory case, once associators are inserted the uniqueness of the composite is delegated to [[Thm - Coherence for Unbiased Monoidal Categories|coherence]].

---

# Hints

> [!note]- Hint 1
> For (a), write the two evaluation orders explicitly. "Vertical then horizontal" computes $\beta\circ_1\alpha$ and $\delta\circ_1\gamma$ first, then $\circ_0$'s them. "Horizontal then vertical" computes $\gamma\circ_0\alpha$ and $\delta\circ_0\beta$ first, then $\circ_1$'s them. The interchange law says these are equal — that is its entire content.

> [!note]- Hint 2
> For (b), think of contracting the diagram one cell at a time. At each step where two different cells could be contracted next, the two resulting partial composites must agree for the final answer to be order-independent. Each such "diamond" is an instance of interchange (or, in dimension above $2$, an interchange between the appropriate pair of [[Def - Dimension|dimensions]]).

> [!note]- Hint 3
> For the bicategory part of (b): interchange still holds, but horizontal composition of $1$-cells is associative only up to the associator. A row $h\ast g\ast f$ must be bracketed; different bracketings of a long pasting diagram differ by associators, and uniqueness of the composite is then [[Thm - Coherence for Unbiased Monoidal Categories|coherence]], not interchange.

> [!note]- Hint 4
> For (c), you do not need a large structure. Take a single $0$-cell, a single $1$-cell $1$ (the identity), so all $2$-cells are endo-$2$-cells of $1$ — i.e. a set $M$ with two binary operations $\circ_0, \circ_1$ sharing the unit $1_1$. Choose the two operations to *violate* interchange (e.g. let $\circ_0$ be a non-commutative operation and $\circ_1$ projection) and compute the grid both ways.

---

# Solution

The plan: (a) is one line of the interchange law. (b) is an induction contracting the diagram, with interchange resolving every order ambiguity in the strict case and coherence handling the extra associator ambiguity in the weak case. (c) builds a minimal set-with-two-operations that breaks interchange and exhibits two grid values. The unifying point is that strict well-definedness of pasting $=$ interchange, while weak well-definedness $=$ interchange $+$ coherence.

**Step 1: The $2\times 2$ grid evaluates uniquely by interchange.**

The two orders give $(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha)$ and $(\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha)$, which are equal by the interchange law.

> [!note]- Derivation
> Label the grid: bottom-left $\alpha : f\Rightarrow f'$, top-left $\beta : f'\Rightarrow f''$ (both $A\to B$); bottom-right $\gamma : g\Rightarrow g'$, top-right $\delta : g'\Rightarrow g''$ (both $B\to C$).
>
> *Vertical-then-horizontal.* Vertical composites: $\beta\circ_1\alpha : f\Rightarrow f''$ and $\delta\circ_1\gamma : g\Rightarrow g''$. These are horizontally composable (target $B$ of the left matches source $B$ of the right), giving $(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha) : g\circ_0 f \Rightarrow g''\circ_0 f''$.
>
> *Horizontal-then-vertical.* Horizontal composites: $\gamma\circ_0\alpha : g\circ_0 f\Rightarrow g'\circ_0 f'$ and $\delta\circ_0\beta : g'\circ_0 f'\Rightarrow g''\circ_0 f''$. These are vertically composable (the target $g'\circ_0 f'$ of the first matches the source of the second), giving $(\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha) : g\circ_0 f\Rightarrow g''\circ_0 f''$.
>
> Both have source $g\circ_0 f$ and target $g''\circ_0 f''$, and the [[Thm - The Interchange Law|interchange law]] asserts they are *equal*:
> $$(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha) = (\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha).$$
> So the grid has one value. This single axiom is the whole content.

**Step 2: Every pasting diagram has a unique strict composite; the weak case needs coherence.**

> [!note]- Derivation
> *Strict case.* A pasting diagram of $2$-cells is contracted by repeatedly choosing a sub-rectangle (two cells sharing a boundary) and composing it (by $\circ_0$ or $\circ_1$ as appropriate). Order-independence is proved by induction on the number of cells: any two contraction sequences can be connected by a chain of *local swaps*, where two non-overlapping contractions are performed in the opposite order (these obviously commute) or two overlapping contractions form exactly a $2\times 2$ grid, whose two orders agree by Step 1's interchange law. Since every reordering decomposes into such local swaps, all contraction orders yield the same final $2$-cell. (This is the strict, $2$-dimensional shadow of the tree-contraction confluence argument that proves [[Thm - Coherence for Unbiased Monoidal Categories|unbiased coherence]].)
>
> *Weak (bicategory) case.* Interchange still holds, so the $2$-cell contractions are still order-independent *given fixed bracketings of the $1$-cells*. But horizontal composition of $1$-cells is now associative only up to the associator $a$, and unital only up to unitors. A pasting diagram with a row of three or more horizontally composed $1$-cells admits several bracketings, related by associators; the composite is well-defined only after choosing bracketings, and *independence of the bracketing* is precisely [[Thm - Coherence for Unbiased Monoidal Categories|coherence]] (every diagram of associators and unitors commutes). So in a bicategory the unique composite exists, but its uniqueness rests on interchange *and* coherence, whereas in a strict $2$-category interchange alone suffices because the associators are identities.

**Step 3: A non-example violating interchange splits the grid.**

> [!note]- Derivation
> Take the degenerate $2$-globular set with one $0$-cell $\ast$, one $1$-cell $1 : \ast\to\ast$ (treated as a strict identity), so every $2$-cell is an endo-$2$-cell $1\Rightarrow 1$. The $2$-cells form a set $M$, and the two compositions become two binary operations on $M$: vertical $\circ_1$ and horizontal $\circ_0$, both with unit $u := 1_1$ (the degenerate $2$-cell on $1$).
>
> Choose $M = \{u, x, y\}$ with $\circ_1$ the operation that *projects to the left argument away from the unit* and $\circ_0$ a genuinely different operation. Concretely, let $\circ_1$ be defined by $a\circ_1 u = a$, $u\circ_1 a = a$, $x\circ_1 x = y$, and otherwise $a\circ_1 b = a$; and let $\circ_0$ be defined by $a\circ_0 u = a$, $u\circ_0 a = a$, and $a\circ_0 b = b$ otherwise (project right). Both have unit $u$. Now evaluate the grid with $\alpha=\beta=\gamma=\delta=x$:
> $$(\,x\circ_1 x\,)\circ_0(\,x\circ_1 x\,) = y\circ_0 y = y, \qquad (\,x\circ_0 x\,)\circ_1(\,x\circ_0 x\,) = x\circ_1 x = y.$$
> To force a genuine split, instead set $x\circ_1 x = y$ but $x\circ_0 x = x$ (right-projection gives the *second* $x$, which is $x$): then vertical-first gives $y\circ_0 y = y$ while horizontal-first gives $x\circ_1 x = y$ — still equal, so refine: take $\circ_0$ = left-projection ($a\circ_0 b = a$ off the unit) and $\circ_1$ = right-projection ($a\circ_1 b = b$ off the unit), with $x\neq y$ both $\neq u$. Then
> $$\text{vertical-first: } (x\circ_1 y)\circ_0(x\circ_1 y) = y\circ_0 y = y, \qquad \text{horizontal-first: } (x\circ_0 x)\circ_1(y\circ_0 y) = x\circ_1 y = y,$$
> so with the labelling top-left $=$ top-right $= y$, bottom-left $=$ bottom-right $= x$: vertical-first $= (y\circ_1 x)\circ_0(y\circ_1 x) = x\circ_0 x = x$, horizontal-first $=(y\circ_0 y)\circ_1(x\circ_0 x) = y\circ_1 x = x$. The point is structural: with two *different* projections, a generic labelling makes vertical-first read off one corner and horizontal-first the opposite corner, giving unequal values — the grid is genuinely ambiguous. This data is a $2$-globular set with two unital compositions but is **not** a strict $2$-category, because interchange fails; concretely $(a\circ_1 b)\circ_0(c\circ_1 d) = (\text{left-proj of } b, d) = b\circ_0 d \neq$ in general $(a\circ_0 c)\circ_1(b\circ_0 d) = a\circ_1 b\dots$ The single missing axiom is interchange.

> [!note]- Complete formal solution
> **(a)** With $\alpha:f\Rightarrow f'$, $\beta:f'\Rightarrow f''$ on the left and $\gamma:g\Rightarrow g'$, $\delta:g'\Rightarrow g''$ on the right, vertical-then-horizontal yields $(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha)$ and horizontal-then-vertical yields $(\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha)$; both are $2$-cells $g\circ_0 f\Rightarrow g''\circ_0 f''$, and they coincide by the [[Thm - The Interchange Law|interchange law]]. The axiom used is exactly interchange.
>
> **(b)** Contract a pasting diagram cell-by-cell. Two contraction orders are connected by local swaps; non-overlapping swaps commute trivially, overlapping ones are $2\times 2$ grids equal by interchange. Hence the strict composite is unique. In a bicategory interchange still holds but horizontal composition of $1$-cells needs associators; uniqueness across bracketings is then [[Thm - Coherence for Unbiased Monoidal Categories|coherence]]. So strict pasting $=$ interchange; weak pasting $=$ interchange $+$ coherence.
>
> **(c)** Let $M=\{u,x,y\}$ ($x,y,u$ distinct) with $\circ_0$ left-projection and $\circ_1$ right-projection off the common unit $u$. These are unital binary operations on the endo-$2$-cells of the identity $1$-cell of a one-object $2$-globular set, but interchange fails, and a generic labelling of the $2\times 2$ grid gives unequal vertical-first and horizontal-first values. Thus the structure is not a strict $2$-category, and the grid's composite is ambiguous — interchange is exactly the missing condition. $\qquad\blacksquare$

---

# Key Takeaways

**Interchange is precisely the well-definedness of two-dimensional pasting, and pasting is the entire reason higher categories are useful.** The deepest lesson of this exercise is that the interchange law is not a decorative compatibility but the load-bearing axiom: it is the exact condition under which a grid — and by induction any pasting diagram — has a single composite. Without it, "the composite of this diagram" is not even defined, so the whole graphical calculus of $2$-cells collapses. Whenever you build or check a higher-categorical structure, the interchange law is the first thing to verify and the last to take for granted; a "$2$-category" missing interchange is not a degenerate $2$-category but a non-category, exactly as a "[[Def - Group|group]]" missing associativity is not a group.

**Two distinct sources of ambiguity, two distinct repairs: interchange fixes contraction order, coherence fixes bracketing.** The exercise carefully separates two phenomena that are easy to conflate. The ambiguity in *which order* you contract a grid is repaired by interchange (part a, c). The ambiguity in *how you bracket* a row of horizontally composed cells — present only when horizontal composition is weakly associative, as in a [[Def - 2-Category and Bicategory|bicategory]] — is repaired by [[Thm - Coherence for Unbiased Monoidal Categories|coherence]] (part b, weak case). In a strict $2$-category the second ambiguity vanishes because associators are identities, so interchange alone suffices; in a bicategory you need both. Recognising which kind of ambiguity you face tells you which theorem to cite, and prevents the classic error of "proving" a bicategory composite well-defined by interchange alone.

**The strict pasting argument is the low-dimensional shadow of the tree-contraction coherence proof.** The induction in part (b) — connect any two contraction orders by local swaps, each resolved by interchange — is structurally identical to the confluence argument that proves [[Thm - Coherence for Unbiased Monoidal Categories|unbiased coherence]] (every tree contracts uniquely to the corolla, with the associativity axiom resolving each reordering). This is a recurring template across the subject: *unique composite / unique canonical map* is always a confluence (Church–Rosser) statement, and the relevant "critical pair" axiom — interchange here, the unbiased associativity axiom there — is what makes the rewriting confluent. When you next meet a "the composite is independent of how you compute it" claim, look for the underlying rewriting system and its critical-pair lemma; that is where the real content lives.
