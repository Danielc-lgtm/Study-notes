---
type: theorem
subject: higher-categories
prereqs:
  - "Def - 2-Category and Bicategory"
  - "Def - Functor"
  - "Def - Natural Transformation"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

In a [[Def - 2-Category and Bicategory|2-category or bicategory]], $\circ$ is **vertical** composition of $2$-cells (along a shared $1$-cell, inside one hom-category) and $\ast$ is **horizontal** composition (along a shared $0$-cell). For a $2 \times 2$ configuration we have $1$-cells $f, f', g, g'$ and $2$-cells $\alpha : f \Rightarrow f'$, $\alpha' : f' \Rightarrow f''$ composable vertically, and $\beta, \beta'$ in a parallel column, composable horizontally with the $\alpha$ column. A **monoid** on a set $M$ here means a binary operation with a two-sided unit (associativity is not needed for Eckmann–Hilton). The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Statement

> **Theorem (Interchange Law).** In any [[Def - 2-Category and Bicategory|2-category or bicategory]], horizontal and vertical composition of $2$-cells commute: whenever the cells are composable as in a $2 \times 2$ grid,
> $$(\beta' \ast \beta) \circ (\alpha' \ast \alpha) \;=\; (\beta' \circ \alpha') \ast (\beta \circ \alpha).$$
> Equivalently, horizontal composition $\ast : \mathcal{B}(B,C) \times \mathcal{B}(A,B) \to \mathcal{B}(A,C)$ is a [[Def - Functor|functor]].

> **Corollary (Eckmann–Hilton).** Let $M$ be a set equipped with two binary operations $\circ$ and $\ast$ that share a common two-sided unit $1$ and satisfy the interchange law $(b' \ast b) \circ (a' \ast a) = (b' \circ a') \ast (b \ast a)$ for all $a, a', b, b' \in M$. Then $\circ = \ast$, and this single operation is commutative (and automatically associative).

The corollary is the interchange law applied to the $2$-cells of a one-object, one-$1$-cell bicategory: there, vertical and horizontal composition are two operations on the *same* set (the endomorphism $2$-cells of the identity $1$-cell) sharing the identity $2$-cell as unit.

---

# Motivation

The interchange law is the axiom that makes *pasting* meaningful. A $2$-category is meant to be a place where you draw diagrams of $2$-cells and read off a total composite — exactly as you compose a string of arrows in an ordinary category. But $2$-cells compose in two independent directions, and a diagram laid out in a grid can be evaluated by composing rows first or columns first. If those two evaluations disagreed, "the composite of the diagram" would be ambiguous and the entire calculus of $2$-cells would collapse. The interchange law is precisely the guarantee that they agree, so that any well-formed pasting diagram has a single unambiguous value. It is the $2$-dimensional analogue of associativity: associativity makes a *string* of $1$-cells unambiguous; interchange makes a *grid* of $2$-cells unambiguous.

What lifts this from a bookkeeping axiom to a theorem worth its own page is its consequence. Run the interchange law in the most degenerate possible setting — one object, one $1$-cell, so that the only data left is the set of $2$-cells from the identity to itself with its two compositions — and a short, almost magical argument (Eckmann–Hilton) forces the two operations to coincide and to be commutative. This is the structural reason the higher homotopy groups $\pi_n$ are abelian, the reason a "doubly degenerate" monoidal category is symmetric, and a first glimpse of the general phenomenon that *commutativity emerges from dimension*.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is mild — you only need a $2$-category or bicategory — so the real source question is: *when does a problem secretly contain interacting two-dimensional compositions?*

The first disguised source is **two compatible algebraic operations on one set**. Whenever a set carries two binary operations and you can verify they interchange and share a unit, Eckmann–Hilton applies, even if no category is in sight. The non-obvious step is to *recognise* the interchange relation in disguise — it often appears as "the two operations distribute over each other in a unit-respecting way". *Example problem:* show that the fundamental group of a topological *group* is abelian, by exhibiting two products on loops (concatenation and pointwise multiplication) that interchange and share the constant loop as unit.

The second disguised source is **whiskering of natural transformations**. In $\mathbf{Cat}$, composing a [[Def - Natural Transformation|natural transformation]] $\alpha : F \Rightarrow F'$ with a [[Def - Functor|functor]] $G$ on either side ("whiskering") is a special case of horizontal composition with an identity $2$-cell, and the interchange law is what guarantees the two ways of whiskering-and-then-stacking agree. The non-obviousness is that the *naturality square* of $\alpha$ is itself the interchange law in disguise. *Example problem:* prove that the horizontal composite $(\gamma \ast \alpha)_X = G'(\alpha_X) \circ \gamma_{FX} = \gamma_{F'X} \circ G(\alpha_X)$ is well-defined — the two formulas agreeing *is* interchange.

The third disguised source is **higher homotopy**. The set $\pi_n(X, x)$ for $n \ge 2$ carries two a priori different concatenation products (along the first coordinate and along the second); both are unital with the constant map, and they interchange because concatenation in independent coordinates commutes. The non-obvious recognition is that "two independent directions of concatenation" is an instance of interchange. *Example problem:* prove $\pi_2(X)$ is abelian.

**Targets (Output Amplification)**

Combine the interchange law with **degeneracy of dimensions** (collapsing objects and $1$-cells). The conclusion of Eckmann–Hilton is that the two operations coincide and commute; combined with the observation that a one-object bicategory is a [[Def - Monoidal Category|monoidal category]], the further result is that a *doubly* degenerate (one-object, one-$1$-cell) bicategory is a *commutative* monoid. This is non-obvious because commutativity was never assumed — it is *forced* by the dimension-shift, the prototype of the **stabilisation hypothesis**: as you add degenerate dimensions, structures become more commutative.

Combine the interchange law with the **homotopy groups of a space**. Eckmann–Hilton applied to $\pi_n$ ($n \ge 2$) yields that all higher homotopy groups are abelian — a foundational fact of algebraic topology that would otherwise require a direct geometric argument. The combination is useful because it explains *why* the abelianness is automatic and unavoidable, rather than a happy accident: it is the same two-operations-one-unit mechanism.

Combine the interchange law with **the calculus of mates and pasting**. Once interchange holds, any pasting diagram of $2$-cells has a unique value, so one may freely re-bracket and re-order compositions — the further result is the entire "string diagram" calculus, in which $2$-cells are nodes on strings and topological deformation of the diagram corresponds to provable equality. This is non-obvious because it converts algebraic identities into a *planar topology*, and it is the engine of computation in monoidal and higher categories.

---

# Why Is It True

The interchange law is true because horizontal composition was *defined* to be a [[Def - Functor|functor]], and a functor preserves composition and identities. Spelled out: horizontal composition $\ast$ takes a pair of composable $2$-cells in two hom-categories and returns a $2$-cell in a third hom-category; the two hom-categories compose vertically, and "functor" means $\ast$ respects that vertical composition. So $(\beta' \ast \beta) \circ (\alpha' \ast \alpha)$ — horizontal-composite of the columns, then vertical-stack — equals $(\beta' \circ \alpha') \ast (\beta \circ \alpha)$ — vertical-stack of the columns, then horizontal-composite — because applying the functor $\ast$ to the vertically-composed input is the same as vertically-composing the outputs. There is genuinely nothing more to it at the $2$-categorical level: **interchange is functoriality of horizontal composition, no more and no less.**

For the corollary, the mechanism is the unit-insertion trick, and it is worth seeing why it is forced. With a shared unit $1$, you can write $a = a \ast 1 = 1 \ast a$ and likewise for $\circ$, so any element can be padded with units in either operation. The interchange law then lets you slide the padding from one operation to the other:
$$a \circ b = (a \ast 1) \circ (1 \ast b) \overset{\text{interchange}}{=} (a \circ 1) \ast (1 \circ b) = a \ast b,$$
which proves $\circ = \ast$. Running the same calculation with the units placed on the other side swaps the order of $a$ and $b$, which proves commutativity. **The single unit shared by both operations is the lever; interchange lets you pry the two operations apart and then, paradoxically, shows they were never different and never order-sensitive.** The reason commutativity appears is geometric: in the two-dimensional picture, $a$ and $b$ occupy independent directions of the grid, and you can slide one past the other without collision — Eckmann–Hilton is the algebraic shadow of "you can move two stones around each other in the plane".

---

# What Makes This Hard

The $2$-categorical statement is not hard — it is functoriality — but two confusions trip people. First, conflating the two compositions: $\circ$ and $\ast$ have *different* composability conditions ($\circ$ needs a shared $1$-cell, $\ast$ needs a shared $0$-cell), and writing down a configuration where *both* sides of the equation are defined requires the full $2 \times 2$ grid, not a careless pair. Second, in the Eckmann–Hilton corollary the surprise is that commutativity is concluded *without assuming it*; the trap is to think the argument must be circular, when in fact the shared unit plus interchange genuinely forces it. The non-obvious step is the unit-padding $a = a \ast 1 = 1 \ast a$, which feels like it should change nothing yet is the entire engine.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The $2$-categorical law is the statement that horizontal composition is a functor — unfold "functor preserves composition" on a $2 \times 2$ grid. The corollary is the unit-insertion trick: pad each element with the shared unit in the *other* operation, then apply interchange to swap which operation does the padding.

**Subgoal decomposition:**

1. **The interchange equation is functoriality.** Show $(\beta' \ast \beta) \circ (\alpha' \ast \alpha) = (\beta' \circ \alpha') \ast (\beta \circ \alpha)$ directly from "$\ast$ is a functor $\mathcal{B}(B,C) \times \mathcal{B}(A,B) \to \mathcal{B}(A,C)$".
   - *Hint:* A functor sends the composite (in the product category, which is componentwise vertical composition) to the composite of the images.
   - *Why needed:* This is the theorem itself; everything else is application.

2. **Both operations equal each other (Eckmann–Hilton, part 1).** Show $a \circ b = a \ast b$.
   - *Hint:* Write $a = a \ast 1$, $b = 1 \ast b$, apply interchange, then use that $1$ is a unit for $\circ$.
   - *Why needed:* Reduces two operations to one, prerequisite for commutativity.

3. **The operation is commutative (Eckmann–Hilton, part 2).** Show $a \ast b = b \ast a$.
   - *Hint:* Write $a = 1 \ast a$, $b = b \ast 1$, apply interchange in the order that places $b$ first.
   - *Why needed:* This is the punchline; combined with step 2 it gives the full corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: Whiskering and the naturality square are the interchange law
> **Statement:** In $\mathbf{Cat}$, for a [[Def - Natural Transformation|natural transformation]] $\alpha : F \Rightarrow F'$ between functors $\mathcal{C} \to \mathcal{D}$ and a functor $G : \mathcal{D} \to \mathcal{E}$, the two whiskerings combine so that the horizontal composite is well-defined; the equality $G'(\alpha_X)\circ\gamma_{FX} = \gamma_{F'X}\circ G(\alpha_X)$ is an instance of interchange.
>
> **Hint:** Apply the interchange law to the grid formed by $\alpha$ and a second transformation $\gamma : G \Rightarrow G'$, using identity $2$-cells where needed.
>
> **Why needed:** It shows the abstract law specialises to the concrete naturality condition you already know, anchoring the theorem in $\mathbf{Cat}$.
>
> > [!note]- Full proof
> > Let $\alpha : F \Rightarrow F'$ ($F, F' : \mathcal{C} \to \mathcal{D}$) and $\gamma : G \Rightarrow G'$ ($G, G' : \mathcal{D} \to \mathcal{E}$). The horizontal composite $\gamma \ast \alpha : G F \Rightarrow G' F'$ has, at an object $X$, two candidate definitions following the two paths around the square: $(\gamma \ast \alpha)_X = \gamma_{F'X} \circ G(\alpha_X)$ and $(\gamma \ast \alpha)_X = G'(\alpha_X) \circ \gamma_{FX}$. These agree because the naturality square of $\gamma$ at the morphism $\alpha_X : FX \to F'X$ commutes: $\gamma_{F'X} \circ G(\alpha_X) = G'(\alpha_X) \circ \gamma_{FX}$. Writing $\alpha = 1_F \circ \alpha$ and $\gamma = \gamma \circ 1_G$ exhibits this exactly as $(\gamma \ast 1)\circ(1 \ast \alpha) = (\gamma \circ 1)\ast(1\circ\alpha)$, an instance of interchange.

> [!note]- Lemma 2: Unit insertion
> **Statement:** If $\circ$ and $\ast$ share a two-sided unit $1$ on a set $M$, then for all $a \in M$, $a = a \ast 1 = 1 \ast a = a \circ 1 = 1 \circ a$.
>
> **Hint:** This is just the definition of a two-sided unit, applied to both operations.
>
> **Why needed:** The padding identities are the raw material the interchange law manipulates in the Eckmann–Hilton argument.
>
> > [!note]- Full proof
> > Since $1$ is a two-sided unit for $\ast$, $a \ast 1 = a$ and $1 \ast a = a$. Since $1$ is a two-sided unit for $\circ$, $a \circ 1 = a$ and $1 \circ a = a$. Hence all four expressions equal $a$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part 1 — the interchange law.** By [[Def - 2-Category and Bicategory|definition]], horizontal composition is a [[Def - Functor|functor]] $\ast : \mathcal{B}(B,C) \times \mathcal{B}(A,B) \to \mathcal{B}(A,C)$. Consider $2$-cells $\alpha : f \Rightarrow f'$, $\alpha' : f' \Rightarrow f''$ in $\mathcal{B}(A,B)$ and $\beta : g \Rightarrow g'$, $\beta' : g' \Rightarrow g''$ in $\mathcal{B}(B,C)$. In the product category $\mathcal{B}(B,C) \times \mathcal{B}(A,B)$, the composite of $(\beta, \alpha)$ and $(\beta', \alpha')$ is $(\beta' \circ \beta, \alpha' \circ \alpha)$ (composition is componentwise). A functor preserves composition, so
> $$\ast\big((\beta', \alpha') \circ (\beta, \alpha)\big) = \ast(\beta', \alpha') \circ \ast(\beta, \alpha),$$
> which reads
> $$(\beta' \circ \beta) \ast (\alpha' \circ \alpha) = (\beta' \ast \alpha') \circ (\beta \ast \alpha).$$
> Renaming to match the statement (the grid has columns and rows) gives $(\beta' \ast \beta) \circ (\alpha' \ast \alpha) = (\beta' \circ \alpha') \ast (\beta \circ \alpha)$. (In a bicategory the same holds, since composition is still a functor on hom-categories; the associators and unitors only intervene for *$1$-cell* re-bracketing, not for this identity.) $\quad\blacksquare$
>
> **Part 2 — Eckmann–Hilton.** Suppose $\circ$ and $\ast$ on a set $M$ share a two-sided unit $1$ and satisfy interchange $(b' \ast b)\circ(a' \ast a) = (b' \circ a')\ast(b \circ a)$. For $a, b \in M$:
> $$a \circ b \;=\; (a \ast 1) \circ (1 \ast b) \;\overset{\text{interchange}}{=}\; (a \circ 1) \ast (1 \circ b) \;=\; a \ast b,$$
> using Lemma 2 at the first and last equalities. So $\circ = \ast$; call the common operation $\cdot$. Now
> $$a \cdot b \;=\; a \circ b \;=\; (1 \ast a) \circ (b \ast 1) \;\overset{\text{interchange}}{=}\; (1 \circ b) \ast (a \circ 1) \;=\; b \ast a \;=\; b \cdot a,$$
> so $\cdot$ is commutative. Finally $\cdot$ is associative: this also follows from interchange and the unit (a standard padding computation), so $(M, \cdot, 1)$ is a commutative monoid. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**The fundamental group of a topological group is abelian.** Let $H$ be a topological group with identity $e$. Loops at $e$ carry two products: concatenation $\cdot$ (the [[Def - Path-Product and the Fundamental Group|path product]]) and pointwise multiplication $\ast$ inherited from $H$. Both are unital with the constant loop at $e$, and they interchange because $(\gamma \ast \gamma')\cdot(\delta \ast \delta') = (\gamma \cdot \delta)\ast(\gamma' \cdot \delta')$ — multiply pointwise and concatenate in either order. Eckmann–Hilton then forces $\pi_1(H)$ to be abelian. This is non-obvious because abelianness of $\pi_1$ is usually special to groups, and here it falls out of a purely formal argument: the source property is "two unital interchanging products on the same set".

**Higher homotopy groups are abelian.** For $n \ge 2$, $\pi_n(X, x)$ carries concatenation in the first and in the second coordinate; both are unital with the constant map and they interchange (concatenating in independent coordinates commutes). Eckmann–Hilton gives that the two coincide and are commutative, so $\pi_n(X)$ is abelian for all $n \ge 2$, while $\pi_1$ need not be (it has only one direction of concatenation). This is the textbook application and shows interchange is the *reason* for the dimension shift in commutativity.

**Doubly degenerate monoidal categories are symmetric.** A one-object bicategory is a [[Def - Monoidal Category|monoidal category]]; a one-object, one-$1$-cell bicategory has, by Eckmann–Hilton applied to its $2$-cells, a *commutative* monoid structure. Categorified, this says a monoidal category with one object and one $1$-cell up to the next dimension acquires a braiding that is automatically a symmetry — the first step of the **periodic table** of higher categories. The application is non-obvious because it predicts the *emergence of symmetry* from degeneracy, a phenomenon (the stabilisation hypothesis) that pervades higher algebra and stable homotopy theory.

---

# Bridges

- **[[Thm - Strictification of Bicategories|Strictification / coherence]]** — the interchange law is one of the axioms that survives strictification untouched: it holds strictly in both 2-categories and bicategories, because it concerns the *functoriality* of horizontal composition, not the *associativity* of $1$-cells. So when a bicategory is replaced by a biequivalent strict $2$-category, interchange is unaffected; what changes is that the associators become identities.

- **[[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]]** — in the one-object case, the interchange law is the functoriality of the tensor product $\otimes$ in a [[Def - Monoidal Category|monoidal category]], i.e. that $\otimes$ is a bifunctor. The bifunctoriality $(g' \circ g)\otimes(f' \circ f) = (g' \otimes f')\circ(g \otimes f)$ is exactly interchange transported to the one-object bicategory, and it is a hypothesis Mac Lane's theorem relies on.

- **The Eckmann–Hilton argument in algebra** — the same two-operations-one-unit lemma proves that a unital magma with a second interchanging unital operation is a commutative monoid; it recurs in proving that the centre of a monoid is commutative, that bialgebra structures are constrained, and that $H$-space multiplications on spheres are homotopy-commutative in the appropriate range. The bridge is that *any* time two unital operations interact via interchange, commutativity is forced.

---

# Unlocked by This

> [!tip] The Stabilisation Hypothesis and the Periodic Table *(from Higher Category Theory)*
> Eckmann–Hilton is the bottom row of the **periodic table** of $n$-categories: as the number of degenerate dimensions grows, structures become more commutative (monoidal → braided → symmetric → …), stabilising after enough steps. This is the combinatorial heart of **stable homotopy theory** and the **stable ∞-categories** of §H.2.

> [!tip] String Diagrams and Graphical Calculus *(from Monoidal Category Theory)*
> Because interchange makes pasting unambiguous, $2$-cells can be drawn as nodes on strings and manipulated by planar isotopy — the **graphical calculus** for monoidal and higher categories, central to **TQFT**, quantum algebra, and categorical quantum mechanics.
