---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - 2-Category and Bicategory"
  - "Thm - The Interchange Law"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Consider a $2\times 2$ pasting configuration of $2$-cells in a [[Def - 2-Category and Bicategory|2-category]]: objects $A,B,C$, parallel $1$-cells $f,f',f'':A\to B$ with $2$-cells $\alpha:f\Rightarrow f'$ and $\alpha':f'\Rightarrow f''$, and parallel $1$-cells $g,g',g'':B\to C$ with $2$-cells $\beta:g\Rightarrow g'$ and $\beta':g'\Rightarrow g''$.

1. Compute the total composite of the grid by first composing **horizontally** (along $B$) and then **vertically**, obtaining $(\beta'\circ\beta)\ast(\alpha'\circ\alpha)$.
2. Compute it by first composing **vertically** and then **horizontally**, obtaining $(\beta'\ast\alpha')\circ(\beta\ast\alpha)$.
3. Confirm the two agree, isolating exactly where the [[Thm - The Interchange Law|interchange law]] is used, and explain why this is what makes "the composite of the pasting diagram" well-defined.

**Recall:**

In a [[Def - 2-Category and Bicategory|2-category]], $\circ$ is vertical composition of $2$-cells (within a hom-category) and $\ast$ is horizontal composition (across a shared object). The [[Thm - The Interchange Law|interchange law]] states
$$(\beta'\circ\beta)\ast(\alpha'\circ\alpha) \;=\; (\beta'\ast\alpha')\circ(\beta\ast\alpha),$$
and is equivalent to horizontal composition being a functor.

---

# Convergent Strategy

**Problem class:** This is a "verify a coherence diagram by computing two routes" problem — the "fill" / pasting target of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to evaluate a fixed diagram by two orders of composition and confirm agreement, which is the entire content of "pasting is well-defined".

**Assumption pattern:** The recognisable feature is a *grid* of $2$-cells — two rows, two columns — where both compositions are available. A grid is exactly the configuration in which interchange has bite: a single column or row can be composed in only one order, but a $2\times 2$ grid offers two genuinely different evaluation orders.

**Theorem routing:** The route is a single application of the [[Thm - The Interchange Law|interchange law]]. There is no further machinery: the law *says* the two orders agree, so the exercise is to lay out the grid carefully enough that the law applies, and to see that nothing else is needed.

**Key decision point:** The non-obvious choice is keeping track of *which composites are even defined*. Horizontal composition needs a shared object ($B$); vertical composition needs parallel $1$-cells (shared $A$ and $B$, or $B$ and $C$). The decision is to compose only along legal adjacencies; attempting an illegal composite (e.g. $\alpha$ with $\beta$ vertically) is a type error and produces nonsense.

---

# Legal Operations Used

1. **Operation 5 (paste 2-cells and use interchange).** This is the operation in its purest form: lay out the grid, compose rows then columns and columns then rows, and invoke interchange to equate them.

---

# Hints

> [!note]- Hint 1
> Draw the grid: the left column is $\alpha$ above $\alpha'$ (a vertical composite $f\Rightarrow f''$), the right column is $\beta$ above $\beta'$ ($g\Rightarrow g''$). Horizontally, the top row is $\beta\ast\alpha$ and the bottom row is $\beta'\ast\alpha'$. Which composites are defined?

> [!note]- Hint 2
> Route 1: form the two columns first (vertical composites $\alpha'\circ\alpha$ and $\beta'\circ\beta$), then horizontally compose them. Route 2: form the two rows first (horizontal composites $\beta\ast\alpha$ and $\beta'\ast\alpha'$), then vertically compose them.

> [!note]- Hint 3
> The two routes give $(\beta'\circ\beta)\ast(\alpha'\circ\alpha)$ and $(\beta'\ast\alpha')\circ(\beta\ast\alpha)$. The interchange law says these are equal — that single equation is the whole verification.

---

# Solution

The plan is to lay out the grid, compute the two evaluation orders, and apply interchange once. Step 1 fixes the legal adjacencies. Step 2 computes Route 1 (columns then rows). Step 3 computes Route 2 (rows then columns). Step 4 equates them by interchange and draws the conclusion about well-definedness.

**Step 1: The legal composites.** The left column $\alpha,\alpha'$ are parallel ($f,f',f'':A\to B$) so compose vertically to $\alpha'\circ\alpha:f\Rightarrow f''$; the right column $\beta,\beta'$ compose vertically to $\beta'\circ\beta:g\Rightarrow g''$. Each row is a horizontal pair sharing $B$, so $\beta\ast\alpha:g\ast f\Rightarrow g'\ast f'$ and $\beta'\ast\alpha':g'\ast f'\Rightarrow g''\ast f''$ are defined.

> [!note]- Derivation
> Vertical composition requires a shared $1$-cell: $\alpha:f\Rightarrow f'$ and $\alpha':f'\Rightarrow f''$ share $f'$, so $\alpha'\circ\alpha:f\Rightarrow f''$ is defined; likewise $\beta'\circ\beta:g\Rightarrow g''$. Horizontal composition requires a shared $0$-cell: $\alpha$ (over $A\to B$) and $\beta$ (over $B\to C$) share $B$, so $\beta\ast\alpha:(g\ast f)\Rightarrow(g'\ast f')$ is defined; likewise $\beta'\ast\alpha':(g'\ast f')\Rightarrow(g''\ast f'')$. The two row-composites are themselves parallel ($g\ast f$ and $g''\ast f''$ via $g'\ast f'$), so they may be composed vertically.

**Step 2: Route 1 — columns first, then rows.** Composing each column vertically and then the two results horizontally gives
$$(\beta'\circ\beta)\ast(\alpha'\circ\alpha):\; g\ast f \Rightarrow g''\ast f''.$$

> [!note]- Derivation
> First form the vertical composites $\alpha'\circ\alpha:f\Rightarrow f''$ and $\beta'\circ\beta:g\Rightarrow g''$. These are now single $2$-cells over $A\to B$ and $B\to C$ respectively, sharing the object $B$, so they horizontally compose to $(\beta'\circ\beta)\ast(\alpha'\circ\alpha):g\ast f\Rightarrow g''\ast f''$.

**Step 3: Route 2 — rows first, then columns.** Composing each row horizontally and then the two results vertically gives
$$(\beta'\ast\alpha')\circ(\beta\ast\alpha):\; g\ast f \Rightarrow g''\ast f''.$$

> [!note]- Derivation
> First form the horizontal composites $\beta\ast\alpha:g\ast f\Rightarrow g'\ast f'$ and $\beta'\ast\alpha':g'\ast f'\Rightarrow g''\ast f''$. These are parallel $2$-cells sharing the $1$-cell $g'\ast f'$, so they vertically compose to $(\beta'\ast\alpha')\circ(\beta\ast\alpha):g\ast f\Rightarrow g''\ast f''$.

**Step 4: The two routes agree, by interchange.** The [[Thm - The Interchange Law|interchange law]] gives
$$(\beta'\circ\beta)\ast(\alpha'\circ\alpha) = (\beta'\ast\alpha')\circ(\beta\ast\alpha),$$
so the pasting composite is independent of the evaluation order, and "the composite of the grid" is well-defined.

> [!note]- Derivation
> Both routes have the same source $g\ast f$ and target $g''\ast f''$, but a priori could be different $2$-cells. The interchange law asserts exactly their equality. It is the *only* fact needed, and it is precisely the functoriality of horizontal composition: applying the functor $\ast$ to the vertically-composed pair $(\beta'\circ\beta,\,\alpha'\circ\alpha)$ equals composing the images $\ast(\beta',\alpha')$ and $\ast(\beta,\alpha)$ vertically. Because the two orders agree, any way of bracketing and ordering the four $2$-cells in the grid yields the same answer, so the pasting diagram has a single unambiguous value.

> [!note]- Complete formal solution
> Label the grid: $\alpha:f\Rightarrow f'$, $\alpha':f'\Rightarrow f''$ over $A\to B$; $\beta:g\Rightarrow g'$, $\beta':g'\Rightarrow g''$ over $B\to C$.
>
> *Route 1 (columns then rows):* vertical composites $\alpha'\circ\alpha:f\Rightarrow f''$, $\beta'\circ\beta:g\Rightarrow g''$; horizontal composite $(\beta'\circ\beta)\ast(\alpha'\circ\alpha):g\ast f\Rightarrow g''\ast f''$.
>
> *Route 2 (rows then columns):* horizontal composites $\beta\ast\alpha:g\ast f\Rightarrow g'\ast f'$, $\beta'\ast\alpha':g'\ast f'\Rightarrow g''\ast f''$; vertical composite $(\beta'\ast\alpha')\circ(\beta\ast\alpha):g\ast f\Rightarrow g''\ast f''$.
>
> By the [[Thm - The Interchange Law|interchange law]], $(\beta'\circ\beta)\ast(\alpha'\circ\alpha) = (\beta'\ast\alpha')\circ(\beta\ast\alpha)$. Hence the two evaluation orders coincide and the pasting composite is well-defined. $\quad\blacksquare$

---

# Key Takeaways

**Interchange is the two-dimensional analogue of associativity: it makes a *grid* unambiguous the way associativity makes a *string* unambiguous.** In an ordinary category, associativity guarantees that a string of composable arrows has a single composite regardless of bracketing. In a 2-category, the analogous worry is a two-dimensional array of $2$-cells, which can be evaluated row-first or column-first; interchange is exactly the law that those agree. The reusable recognition: whenever you face a diagram of $2$-cells laid out in two independent directions, the well-definedness of "the composite" is an interchange question, and interchange is the only tool needed — no associators, no unitors, just functoriality of horizontal composition.

**The hard part of pasting is type-checking, not computing.** The actual equality is one application of interchange; the work is in identifying which composites are even defined. Vertical composition demands parallel $1$-cells; horizontal composition demands a shared $0$-cell. A grid is precisely the configuration where, after composing each row or column, the *results* become composable in the other direction. The diagnostic to carry forward: before invoking interchange, confirm that both evaluation orders produce $2$-cells with the *same* source and target $1$-cells — if they do not, you have laid the grid out wrongly, and interchange does not even typecheck.

**Pasting diagrams license a graphical calculus, and interchange is what makes it sound.** Once you know any well-formed pasting diagram has a single value, you can manipulate diagrams of $2$-cells geometrically — sliding cells past one another, deforming the diagram — and trust that the algebraic value is unchanged. This is the foundation of **string diagrams**, where $2$-cells are nodes on strings and planar isotopy corresponds to provable equality. The same interchange computation done here, in one fixed grid, is what guarantees that the entire graphical language of monoidal categories, **TQFT**, and categorical quantum mechanics is well-defined. The trigger to remember: "I want to compute a complicated $2$-cell diagram" should immediately suggest "interchange makes the order irrelevant, so I may evaluate in whatever order is convenient."
