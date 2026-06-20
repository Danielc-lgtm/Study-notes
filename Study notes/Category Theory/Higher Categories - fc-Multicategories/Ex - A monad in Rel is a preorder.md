---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Monad Monoid and Module in a Bicategory"
  - "Def - 2-Category and Bicategory"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $\mathbf{Rel}$ be the [[Def - 2-Category and Bicategory|bicategory]] whose objects are sets, whose $1$-cells $X \to Y$ are relations $R \subseteq X \times Y$ (composed by relational composition), and whose $2$-cells $R \Rightarrow R'$ are inclusions $R \subseteq R'$. Show that a [[Def - Monad Monoid and Module in a Bicategory|monad]] in $\mathbf{Rel}$ on a set $X$ is exactly a **preorder** on $X$ (a reflexive transitive relation), and explain why the monad axioms (associativity, unit laws) are *automatically* satisfied — so that monad structure here is a *property* of a relation, not extra data.

**Recall:**

![[Def - Monad Monoid and Module in a Bicategory#The Definition]]

In $\mathbf{Rel}$: the composite of relations $R\subseteq X\times Y$ and $S\subseteq Y\times Z$ is $S\circ R = \{(x,z) : \exists\, y,\ (x,y)\in R,\ (y,z)\in S\}$. The identity $1$-cell on $X$ is the equality relation $\Delta_X = \{(x,x)\}$. The hom-set $\mathbf{Rel}(X, Y)$ is the *poset* of relations ordered by inclusion: there is at most one $2$-cell between any two parallel $1$-cells. A **preorder** is a relation $R$ that is reflexive ($xRx$) and transitive ($xRy \wedge yRz \Rightarrow xRz$).

---

# Convergent Strategy

**Problem class:** A *dictionary-translation* problem, parallel to [[Ex - A monad in Span Set is a small category]] but in a bicategory whose $2$-cells are *inclusions*, which makes the monad axioms degenerate into properties.

**Assumption pattern:** The crucial feature of $\mathbf{Rel}$ is that hom-sets are *thin* posets — at most one $2$-cell between two $1$-cells. So a $2$-cell $\mu : RR\Rightarrow R$ is just the assertion $R\circ R\subseteq R$, and $\eta : \Delta_X\Rightarrow R$ is just $\Delta_X\subseteq R$. There is no data to carry beyond the relation itself.

**Theorem routing:** This is one of the three signature identifications of [[Def - Monad Monoid and Module in a Bicategory]]. The route is to interpret $t, \mu, \eta$ in $\mathbf{Rel}$ (legal operation 5) and observe that thinness collapses the monad axioms.

**Key decision point:** The non-obvious realisation is that, because $\mathbf{Rel}$'s $2$-cells are mere inclusions, "monad structure" is a *property* (the inclusions either hold or do not) rather than *data* (a chosen composition). This is exactly why a preorder is "a category with at most one arrow between objects" — the thinness of $\mathbf{Rel}$ is the source of the thinness of the preorder.

---

# Legal Operations Used

1. **Operation 4 (transcribe the monad notion into $\mathbf{Rel}$).** Write $t = R$, $\mu : RR\Rightarrow R$, $\eta : \Delta_X\Rightarrow R$.

2. **Operation 5 (read via the concrete description).** Composition is relational composition; $2$-cells are inclusions, so $\mu$ and $\eta$ are inclusions $R\circ R\subseteq R$ and $\Delta_X\subseteq R$.

---

# Hints

> [!note]- Hint 1
> An endo-$1$-cell on $X$ in $\mathbf{Rel}$ is a relation $R\subseteq X\times X$. Its self-composite $R\circ R$ is $\{(x,z) : \exists y,\ xRy\wedge yRz\}$. A $2$-cell $\mu : R\circ R\Rightarrow R$ is an inclusion — write down which inclusion.

> [!note]- Hint 2
> $\mu$ says $R\circ R\subseteq R$: whenever $xRy$ and $yRz$, also $xRz$. That is **transitivity**. The unit $\eta : \Delta_X\Rightarrow R$ says $\Delta_X\subseteq R$, i.e. $xRx$ for all $x$ — **reflexivity**.

> [!note]- Hint 3
> Why are the monad axioms automatic? Because between any two parallel $1$-cells in $\mathbf{Rel}$ there is at most one $2$-cell (the poset is thin). So any two parallel composites of $2$-cells are equal *by default*, and the associativity and unit equations hold trivially. Conclude that monad structure on $R$ is just the property "reflexive and transitive".

---

# Solution

We interpret the monad data as inclusions and observe the axioms are automatic.

**Step 1: The endo-$1$-cell is a relation; multiplication is transitivity.**

> [!note]- Derivation
> A [[Def - Monad Monoid and Module in a Bicategory|monad]] in $\mathbf{Rel}$ on $X$ has endo-$1$-cell a relation $R\subseteq X\times X$. The self-composite is $R\circ R = \{(x,z) : \exists y,\ (x,y)\in R \wedge (y,z)\in R\}$. The multiplication $\mu : R\circ R\Rightarrow R$, being a $2$-cell in $\mathbf{Rel}$, is the inclusion $R\circ R\subseteq R$: for all $x, y, z$, if $xRy$ and $yRz$ then $xRz$. This is **transitivity**.

**Step 2: The unit is reflexivity.**

> [!note]- Derivation
> The unit $\eta : \Delta_X\Rightarrow R$ is the inclusion $\Delta_X\subseteq R$, i.e. $(x,x)\in R$ for all $x\in X$: $xRx$. This is **reflexivity**. So a relation carrying monad data is reflexive and transitive — a **preorder**.

**Step 3: The axioms are automatic because $\mathbf{Rel}$ is locally thin.**

> [!note]- Derivation
> The monad associativity law $\mu\cdot(\mu\ast 1) = \mu\cdot(1\ast\mu)$ and the unit laws $\mu\cdot(\eta\ast 1) = 1 = \mu\cdot(1\ast\eta)$ are equalities of $2$-cells. But in $\mathbf{Rel}$ each hom-set is a *poset*: there is at most one $2$-cell between any two parallel $1$-cells. Hence any two parallel $2$-cells are *equal automatically*, and all the monad equations hold trivially — there is nothing to check. Consequently a monad in $\mathbf{Rel}$ is precisely a reflexive transitive relation, i.e. a **preorder**, and the monad structure is a *property* of $R$ (it either is or is not reflexive and transitive), carrying no extra data. Conversely every preorder is such a monad.

> [!note]- Complete formal solution
> A monad in $\mathbf{Rel}$ on $X$ is a relation $R\subseteq X\times X$ with $2$-cells $\mu : R\circ R\Rightarrow R$ and $\eta : \Delta_X\Rightarrow R$. Since $\mathbf{Rel}$'s $2$-cells are inclusions, $\mu$ is $R\circ R\subseteq R$ (transitivity: $xRy\wedge yRz\Rightarrow xRz$) and $\eta$ is $\Delta_X\subseteq R$ (reflexivity: $xRx$). The monad axioms are equalities of $2$-cells; as each hom-poset of $\mathbf{Rel}$ is thin, all parallel $2$-cells coincide, so the axioms hold automatically. Therefore a monad in $\mathbf{Rel}$ is exactly a reflexive transitive relation — a preorder — and monad structure is a property, not data. $\blacksquare$

---

# Key Takeaways

**Thin $2$-cells turn monad data into a property.** The signature feature of this example is that $\mathbf{Rel}$ has at most one $2$-cell between parallel $1$-cells, so the monad multiplication and unit are *inclusions* (which hold or fail) rather than chosen maps, and the monad axioms — being equalities of $2$-cells in a thin hom-poset — are vacuous. This is why a preorder, unlike a general category, carries *no extra structure* beyond the relation: monad-ness is a property. The transferable diagnostic: when the ambient bicategory is *locally thin* (hom-posets), "monad" degenerates to a property and the resulting structures are "thin" versions (preorders rather than categories, suplattices rather than ...). The richness of monad data is governed by the richness of the bicategory's $2$-cells.

**Reflexive-and-transitive *is* unit-and-multiplication.** The exercise makes precise the slogan "a preorder is a category with at most one arrow between objects": reflexivity is the unit (identity arrows), transitivity is the multiplication (composition), and uniqueness of arrows is the thinness of $\mathbf{Rel}$. Placed beside [[Ex - A monad in Span Set is a small category]], it shows the *same* monad template producing a category in $\mathbf{Span}(\mathbf{Set})$ and a preorder in $\mathbf{Rel}$ — the difference being entirely the $2$-cell structure (sets of arrows versus inclusions). The trigger to remember: "reflexive + transitive" $\Rightarrow$ "monad in $\mathbf{Rel}$" $\Rightarrow$ "thin category".

**The bicategory is the dial; the monad is fixed.** This is the smallest, cleanest instance of the unifying frame of §3: one definition (monad in $\mathcal{K}$) refracts into many concrete structures as $\mathcal{K}$ varies, and the *texture* of the resulting structure (data versus property, set-of-arrows versus inclusion) is read off from the texture of $\mathcal{K}$'s $2$-cells. Internalising this lets you predict, before any computation, that a monad in a thin bicategory will be a "property-like" structure and a monad in a bicategory with genuine $2$-cell sets will be a "data-like" structure. It is the same principle that, in [[Thm - Monoids and Modules Form a Bicategory]], makes $\mathrm{Mod}(\mathbf{Rel})$ a calculus of ordered sets rather than of categories.
