---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Monad Monoid and Module in a Bicategory"
  - "Def - Category"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $\mathbf{Span}(\mathbf{Set})$ be the [[Def - 2-Category and Bicategory|bicategory]] whose objects are sets, whose $1$-cells $X \to Y$ are spans $X \xleftarrow{} S \xrightarrow{} Y$ (composed by [[Def - Pullback and Pushout|pullback]]), and whose $2$-cells are maps of spans. Show that a [[Def - Monad Monoid and Module in a Bicategory|monad]] in $\mathbf{Span}(\mathbf{Set})$ on a set $C_0$ is exactly a small [[Def - Category|category]] with object-set $C_0$: the monad's endo-$1$-cell is a span $C_0 \xleftarrow{\mathrm{dom}} C_1 \xrightarrow{\mathrm{cod}} C_0$ (the set of arrows with domain/codomain), the multiplication $\mu$ is composition of arrows, the unit $\eta$ picks out identity arrows, and the monad axioms are the category axioms.

**Recall:**

![[Def - Monad Monoid and Module in a Bicategory#The Definition]]

In $\mathbf{Span}(\mathbf{Set})$, the composite of $1$-cells $C_0\xleftarrow{}C_1\xrightarrow{\mathrm{cod}}C_0$ and $C_0\xleftarrow{\mathrm{dom}}C_1\xrightarrow{}C_0$ (a self-composite of one endo-span) is the [[Def - Pullback and Pushout|pullback]] $C_1\times_{C_0}C_1 = \{(g, f) : \mathrm{dom}(g) = \mathrm{cod}(f)\}$ — the set of **composable pairs**. The identity $1$-cell on $C_0$ is the discrete span $C_0\xleftarrow{1}C_0\xrightarrow{1}C_0$. A small [[Def - Category|category]] has a set of objects, a set of arrows with domain/codomain maps, an associative composition of composable pairs, and identity arrows.

---

# Convergent Strategy

**Problem class:** A *dictionary-translation* problem from the topic page's targets: read the abstract notion "monad in $\mathcal{K}$" in the concrete bicategory $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$ and recognise the result.

**Assumption pattern:** The decisive structural fact about $\mathbf{Span}(\mathbf{Set})$ is that *composition of $1$-cells is pullback*, and the pullback of an endo-span with itself is the set of composable pairs of arrows. This single fact converts $\mu : tt\Rightarrow t$ into "a map (composable pairs) $\to$ arrows", i.e. composition.

**Theorem routing:** This is one of the three signature identifications of [[Def - Monad Monoid and Module in a Bicategory]] and the prototype object of [[Thm - Monoids and Modules Form a Bicategory]] (whose corollary states categories are the objects of $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$). The route is to interpret each piece of monad data via the concrete description of $\mathbf{Span}(\mathbf{Set})$ (legal operation 5).

**Key decision point:** The non-obvious move is to recognise the pullback $C_1\times_{C_0}C_1$ as the set of *composable* pairs, so that $\mu$ is forced to be composition. The temptation is to leave the pullback abstract; spelling out its elements as matching pairs $(g, f)$ with $\mathrm{dom}(g)=\mathrm{cod}(f)$ is exactly what makes the category structure appear.

---

# Legal Operations Used

1. **Operation 4 (transcribe the monad notion into the bicategory).** Write down $t, \mu, \eta$ for $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$.

2. **Operation 5 (read the monad via the concrete description of $\mathcal{K}$).** Interpret each piece using "composition $=$ pullback $=$ composable pairs".

3. **Operation 8 (the unit / identity arrows).** $\eta$ from the identity $1$-cell picks out identities.

---

# Hints

> [!note]- Hint 1
> An endo-$1$-cell $t$ on $C_0$ in $\mathbf{Span}(\mathbf{Set})$ is a span $C_0\xleftarrow{\mathrm{dom}}C_1\xrightarrow{\mathrm{cod}}C_0$. Read $C_1$ as a set of "arrows", with $\mathrm{dom}$ and $\mathrm{cod}$ telling you each arrow's source and target. What is the self-composite $tt$?

> [!note]- Hint 2
> The composite $tt$ is the pullback $C_1\times_{C_0}C_1$, whose elements are pairs $(g, f)$ with $\mathrm{dom}(g) = \mathrm{cod}(f)$ — *composable* pairs. A $2$-cell $\mu : tt\Rightarrow t$ is then a map (composable pairs) $\to C_1$ over $C_0$. What categorical operation is that?

> [!note]- Hint 3
> $\mu$ is composition of arrows: $\mu(g, f) = g\circ f$. The unit $\eta : 1_{C_0}\Rightarrow t$ is a map $C_0\to C_1$ over $C_0$, i.e. an assignment of an identity arrow $1_c$ to each object $c$. Now translate the monad associativity and unit laws.

---

# Solution

We interpret each piece of monad data in $\mathbf{Span}(\mathbf{Set})$ and read off a category.

**Step 1: The endo-$1$-cell is the set of arrows.**

> [!note]- Derivation
> A [[Def - Monad Monoid and Module in a Bicategory|monad]] in $\mathbf{Span}(\mathbf{Set})$ is an object $C_0$ (a set) with an endo-$1$-cell $t : C_0\to C_0$, which is a span $C_0\xleftarrow{\mathrm{dom}}C_1\xrightarrow{\mathrm{cod}}C_0$. Read $C_1$ as the set of **arrows**, with $\mathrm{dom}, \mathrm{cod} : C_1\to C_0$ giving each arrow's source and target. The object-set is $C_0$; the arrow-set is $C_1$.

**Step 2: Multiplication is composition; unit is identities.**

> [!note]- Derivation
> The self-composite $tt$ is the [[Def - Pullback and Pushout|pullback]]
> $$C_1\times_{C_0}C_1 = \{(g, f)\in C_1\times C_1 : \mathrm{dom}(g) = \mathrm{cod}(f)\},$$
> the set of composable pairs (with the composite span having domain $\mathrm{dom}(f)$ and codomain $\mathrm{cod}(g)$). The multiplication $\mu : tt\Rightarrow t$ is a map of spans $C_1\times_{C_0}C_1\to C_1$ over $C_0$, i.e. a function assigning to each composable pair $(g, f)$ an arrow $\mu(g, f) =: g\circ f$ with $\mathrm{dom}(g\circ f) = \mathrm{dom}(f)$ and $\mathrm{cod}(g\circ f) = \mathrm{cod}(g)$ — this is **composition of arrows**. The unit $\eta : 1_{C_0}\Rightarrow t$ is a map $C_0\to C_1$ over $C_0$, i.e. an assignment $c\mapsto 1_c$ with $\mathrm{dom}(1_c) = \mathrm{cod}(1_c) = c$ — the **identity arrows**.

**Step 3: The monad axioms are the category axioms.**

> [!note]- Derivation
> Monad **associativity** $\mu\cdot(\mu\ast 1_t) = \mu\cdot(1_t\ast\mu)$, read on triples of composable arrows $(h, g, f)$, says $(h\circ g)\circ f = h\circ(g\circ f)$ — associativity of composition. The monad **unit laws** $\mu\cdot(\eta\ast 1_t) = 1_t = \mu\cdot(1_t\ast\eta)$, read on an arrow $f$, say $1_{\mathrm{cod}(f)}\circ f = f = f\circ 1_{\mathrm{dom}(f)}$ — the identity laws. Hence the monad data and axioms are exactly those of a small [[Def - Category|category]] with objects $C_0$ and arrows $C_1$. Conversely, every small category gives such a monad by reversing each step.

> [!note]- Complete formal solution
> A monad in $\mathbf{Span}(\mathbf{Set})$ on a set $C_0$ consists of: an endo-span $C_0\xleftarrow{\mathrm{dom}}C_1\xrightarrow{\mathrm{cod}}C_0$ (objects $C_0$, arrows $C_1$); a $2$-cell $\mu : C_1\times_{C_0}C_1\to C_1$ over $C_0$, where the domain is the set of composable pairs $\{(g,f) : \mathrm{dom}(g)=\mathrm{cod}(f)\}$, so $\mu(g,f)=g\circ f$ is composition; and a $2$-cell $\eta : C_0\to C_1$ over $C_0$ assigning identities $c\mapsto 1_c$. Monad associativity is $(h\circ g)\circ f = h\circ(g\circ f)$; the unit laws are $1\circ f = f = f\circ 1$. These are precisely the axioms of a small [[Def - Category|category]]. The correspondence "monad in $\mathbf{Span}(\mathbf{Set})$ $\leftrightarrow$ small category" is a bijection. $\blacksquare$

---

# Key Takeaways

**"Monad in $\mathcal{K}$" means "name $\mathcal{K}$, then interpret".** This exercise is the archetype of the chapter's central trigger-reaction pattern: confronted with "monad in a bicategory", do not reach for commuting diagrams — name the bicategory and read off what its objects, $1$-cells, $2$-cells, and composition concretely are. In $\mathbf{Span}(\mathbf{Set})$, the decisive fact is that composition of $1$-cells is pullback, and the pullback of an endo-span with itself is the set of composable pairs of arrows; once that is in hand, $\mu$ is forced to be composition and $\eta$ to be identities. The transferable diagnostic: the *nature of $1$-cell composition* in $\mathcal{K}$ determines what the monad multiplication becomes.

**The pullback is "the object of composable pairs", and that is why categories are monads.** The single recognition that unlocks everything is reading $C_1\times_{C_0}C_1$ as $\{(g,f) : \mathrm{dom}(g)=\mathrm{cod}(f)\}$. This is the same pullback that composes spans in [[Ex - The double category of spans]], and it is the structural reason a small category is "a monad in spans": the monad multiplication acts on exactly the composable pairs that a category's composition acts on. The trigger to carry: "matching/composable pairs" $\Rightarrow$ "pullback", and conversely an endo-span with a pullback-multiplication is a category. This identification is what makes [[Thm - Monoids and Modules Form a Bicategory]] yield categories and profunctors when run on $\mathbf{Span}(\mathbf{Set})$.

**Categories, monads, preorders, and enriched categories are one definition in different bicategories.** Sitting alongside [[Ex - A monad in Rel is a preorder]] and [[Ex - A monad in Cat recovers the ordinary monad]], this exercise shows the same template — "object with associative unital multiplication on an endo-$1$-cell" — becomes a small category in $\mathbf{Span}(\mathbf{Set})$, a preorder in $\mathbf{Rel}$, an ordinary monad in $\mathbf{Cat}$, and (with the right base) an enriched category in $\mathcal{V}\text{-}\mathbf{Mat}$. The unifying lesson is that the bicategory is the parameter and the monad is the constant template; changing the bicategory changes the meaning while keeping the proofs uniform. This is the compression that organises the whole of §3 and motivates Leinster's choice to develop everything bicategorically.
