---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Weak Double Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Prove that a [[Def - Weak Double Category|weak double category]] in which the only vertical $1$-cells are identities (trivial vertical structure) is exactly a [[Def - 2-Category and Bicategory|bicategory]]. Make the correspondence precise: the objects coincide; the horizontal $1$-cells of the double category become the $1$-cells of the bicategory; the $2$-cells (squares with identity vertical sides) become the bicategory $2$-cells; horizontal composition $\odot$ becomes $1$-cell composition $\circ$; and the double category's associator, unitors, pentagon, and triangle become the bicategory's. Deduce as a corollary that a [[Def - Monoidal Category|monoidal category]] is a one-object such weak double category (a one-object bicategory).

**Recall:**

![[Def - Weak Double Category#The Definition]]

A **[[Def - 2-Category and Bicategory|bicategory]]** $\mathcal{B}$ has objects, $1$-cells composed by $\circ$ (associative and unital up to coherent invertible $2$-cells), and $2$-cells composed vertically and horizontally, with associator $a$, unitors $l, r$, and the pentagon and triangle coherence axioms. A **[[Def - Monoidal Category|monoidal category]]** is a one-object bicategory ("delooping": the single hom-category is $\mathcal{V}$, the tensor is $1$-cell composition).

---

# Convergent Strategy

**Problem class:** A *dial-setting* problem: turn off the vertical structure of a weak double category and show what remains is a bicategory. This is the topic page's recognition routine applied in the reverse direction (from the richer structure down to the special case).

**Assumption pattern:** "Trivial vertical structure" means every $2$-cell has identity vertical sides, so a $2$-cell is a square with no genuine side data — top $m$, bottom $m'$, identity sides — which is exactly a $2$-cell $m\Rightarrow m'$ of a bicategory. With the sides trivial, horizontal composition $\odot$ becomes the only composition of $1$-cells, i.e. $\circ$.

**Theorem routing:** This is part (1) of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]], read for weak double categories: vertically-trivial weak double categories $=$ bicategories. The monoidal corollary is part (2), via the delooping identification (Lemma 3 of that theorem).

**Key decision point:** The non-obvious point is that a square with *identity vertical sides* and top $m$, bottom $m'$ is the *same datum* as a globular $2$-cell $m\Rightarrow m'$. Once you see that, the associator/unitor/pentagon/triangle of the double category transport verbatim. The temptation is to think the square's two extra (vertical) edges carry information; with trivial vertical structure they do not.

---

# Legal Operations Used

1. **Operation 1 (set the dials).** Turn off vertical structure; read off the collapsed structure.

2. **Operation 9 (specialise / deloop).** Deduce the monoidal case from the bicategory case by restricting to one object.

3. **Operation 3 (the double category's coherent associator becomes the bicategory's).** The associator and pentagon transport directly.

---

# Hints

> [!note]- Hint 1
> A $2$-cell in a weak double category is a square with a top horizontal $1$-cell, a bottom horizontal $1$-cell, and two vertical side $1$-cells. If the vertical sides must be identities, what is left? Compare with the shape of a bicategory $2$-cell.

> [!note]- Hint 2
> With identity sides, horizontal composition $\odot$ of horizontal $1$-cells is the *only* composition law for these arrows; rename it $\circ$. The double category's associator $a$ and unitors $l, r$ are invertible $2$-cells with identity vertical boundaries — i.e. invertible globular $2$-cells — exactly the bicategory's $a, l, r$.

> [!note]- Hint 3
> For the corollary: a one-object bicategory is a monoidal category (delooping), where the single hom-category is $\mathcal{V}$, the tensor is $\circ$, and the unit object is the identity $1$-cell. So "one object $+$ trivial vertical $+$ weak double category" $=$ "one-object bicategory" $=$ "monoidal category".

---

# Solution

We match the data and the coherence, then specialise to one object.

**Step 1: With trivial vertical structure, $2$-cells are globular.**

> [!note]- Derivation
> In a [[Def - Weak Double Category|weak double category]] a $2$-cell is a square
> $$\begin{array}{ccc} A & \xrightarrow{m} & B \\ f\downarrow & \alpha\Downarrow & \downarrow g \\ A' & \xrightarrow{m'} & B' \end{array}$$
> When the only vertical $1$-cells are identities, $f = 1_A$ and $g = 1_B$ (forcing $A' = A$, $B' = B$), so the square degenerates to a globular $2$-cell $\alpha : m\Rightarrow m'$ between parallel horizontal $1$-cells $m, m' : A\nrightarrow B$. Thus $2$-cells of the double category are exactly $2$-cells between parallel $1$-cells — the shape of a [[Def - 2-Category and Bicategory|bicategory]] $2$-cell. Vertical composition of squares becomes vertical composition of globular $2$-cells; horizontal composition of squares becomes horizontal composition of globular $2$-cells.

**Step 2: Horizontal composition becomes $1$-cell composition; coherence transports.**

> [!note]- Derivation
> Rename the horizontal $1$-cells as $1$-cells and $\odot$ as $\circ$. The double category's associativity isomorphism $a : (m\odot m')\odot m''\Rightarrow m\odot(m'\odot m'')$ has identity vertical boundaries, so it is an invertible globular $2$-cell — exactly a bicategory associator. Likewise the unitors $l : \mathrm{U}_A\odot m\Rightarrow m$ and $r : m\odot\mathrm{U}_B\Rightarrow m$ become the bicategory unitors (with $\mathrm{U}_A$ the identity $1$-cell $1_A$). The interchange law of the double category, restricted to globular $2$-cells, is the bicategory's interchange. The pentagon and triangle of the double category become the bicategory's pentagon and triangle. So the data and axioms are exactly those of a bicategory. Conversely any bicategory yields a vertically-trivial weak double category by reversing each step (no vertical $1$-cells but identities, $1$-cells as horizontal $1$-cells, globular $2$-cells as squares with identity sides).

**Step 3: Corollary — a monoidal category is a one-object such double category.**

> [!note]- Derivation
> Apply Step 1–2 with a single object. A one-object bicategory is, by delooping, a [[Def - Monoidal Category|monoidal category]]: the single hom-category $\mathcal{B}(\ast,\ast)$ is $\mathcal{V}$, the horizontal composition $\circ$ is the tensor $\otimes$, the identity $1$-cell $1_\ast$ is the unit object $I$, and the associator/unitors/pentagon/triangle are exactly those of $\mathcal{V}$. Hence a one-object, vertically-trivial weak double category is a monoidal category. This is part (2) of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]] obtained by composing "trivial vertical $\Rightarrow$ bicategory" with "one object $\Rightarrow$ delooping".

> [!note]- Complete formal solution
> Let $\mathbb{D}$ be a weak double category with only identity vertical $1$-cells. Every $2$-cell of $\mathbb{D}$ is a square with identity vertical sides, hence a globular $2$-cell $\alpha : m\Rightarrow m'$ between parallel horizontal $1$-cells; horizontal $1$-cells, renamed $1$-cells with composition $\circ := \odot$, together with these globular $2$-cells, the associator and unitors of $\mathbb{D}$ (invertible globular $2$-cells), and the interchange/pentagon/triangle of $\mathbb{D}$, constitute exactly a [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$. Conversely a bicategory gives such a $\mathbb{D}$. The correspondence is an isomorphism of the two notions. Specialising to one object and invoking delooping (a one-object bicategory is a [[Def - Monoidal Category|monoidal category]]), a one-object vertically-trivial weak double category is a monoidal category, with $\otimes=\circ$ and $I=1_\ast$. $\blacksquare$

---

# Key Takeaways

**Turning off the vertical dial collapses squares to globes.** The whole exercise is the observation that a $2$-cell's two vertical sides carry information *only when the vertical structure is non-trivial*; force the sides to be identities and the square becomes a globular $2$-cell between parallel horizontal arrows — precisely a bicategory $2$-cell. This is the cleanest instance of the dial-setting routine: the *shape* of the $2$-cell changes from a square to a globe as you turn the vertical dial off. The transferable trigger: whenever you see "trivial vertical structure", expect the four-layer structure to collapse to a globular ($1$-dimensional-composition) one, i.e. a bicategory or, with one object, a monoidal category.

**Coherence transports verbatim across the collapse.** Because the associator, unitors, pentagon, and triangle of a weak double category are *already* invertible $2$-cells with identity vertical boundaries (when the vertical structure is trivial), they are *already* bicategory coherence data — nothing needs re-proving. This is why the embedding of bicategories into weak double categories (and of monoidal categories into both) is full and faithful: the coherence is shared. The general lesson is that the chapter's structures form a tower in which coherence data at the richer level *restricts* to coherence data at the poorer level, so results proved once at the top descend for free. This is exactly the mechanism of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]].

**Delooping is the one-object dial, and it links every level of the tower.** A one-object bicategory is a monoidal category; a one-object $2$-category (strict bicategory) is a strict monoidal category; a one-object weak double category with trivial vertical structure is again a monoidal category. The "number of objects" dial, when turned to one, *deloops* — the single hom-category becomes the monoidal category and composition becomes the tensor. Recognising delooping lets you deduce monoidal statements from bicategorical ones (legal operation 9) and is the reason monoidal categories, braided monoidal categories, and symmetric monoidal categories sit in the Baez–Dolan periodic table as one-object, one-$1$-cell, and stabilised instances of higher categories. See [[Ex - A monoidal category as a one-object fc-multicategory]] for the same delooping at the fc-multicategory level.
