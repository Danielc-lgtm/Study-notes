---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Generalized Multicategory"
  - "Def - Generalized Operad"
  - "Def - Algebra for a Generalized Operad"
  - "Def - Cartesian Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Assemble the chapter's **unifying table**. For each of the three cartesian monads $T = \mathrm{id}$, $T = (-)^{*}$ (on $\mathbf{Set}$), and $T = \mathbb{T}$ (on globular sets), fill in the four columns:

1. a **$T$-graph** (the underlying data: $C_0, C_1, \mathrm{dom} : C_1 \to T C_0, \mathrm{cod} : C_1 \to C_0$);
2. a **$T$-multicategory**;
3. a **$T$-operad** (the case $C_0 = 1$);
4. an **algebra for the $T$-operad**.

Then explain the two reading directions: why reading a *row* gives one coherent classical theory, and why reading a *column* gives one uniform construction applied to different monads. Justify each entry briefly using the chapter's results.

**Recall:**

![[Def - Generalized Multicategory#The Definition]]

A $T$-[[Def - Generalized Operad|operad]] is a $T$-multicategory with $C_0 = 1$; an [[Def - Algebra for a Generalized Operad|algebra]] for it is an object with a coherent action of its operations. The recovery of classical structures is [[Thm - Generalized Operads Recover Classical Structures]].

---

# Convergent Strategy

**Problem class:** A *recognition / synthesis* problem (the fifth target): see the classical structures as rows of one table. The routine is to apply the unwinding procedure (compute $T C_0$ and $T1$) to three monads and four constructions, then articulate the two-directional structure of the result.

**Assumption pattern:** Each cell is determined by two computations already done in earlier exercises — $T C_0$ (what an arrow's domain is) and $T1$ (the arity object). The assumption to exploit is that *nothing in the four constructions refers to the internal nature of $T$*; they use only that $T$ is cartesian, so substituting a specific $T$ specializes the cells without disturbing the construction. This uniformity is what makes the table coherent.

**Theorem routing:** Each row's first three columns are [[Thm - Generalized Operads Recover Classical Structures]] (categories/monoids, multicategories/operads, globular multicategories/globular operads). The fourth column (algebras) uses [[Def - Algebra for a Generalized Operad|the algebra definition]] and the algebra-transport part of the recovery theorem. The globular row's justification is forward to HC7.

**Key decision point:** The genuinely hard part is articulating the *two reading directions* correctly and not conflating them. A row fixes $T$ and varies the construction — it is one world (one theory). A column fixes the construction and varies $T$ — it is one recipe applied to different inputs. The tempting error (illegal-but-tempting #4 on the topic page) is to compare entries *across rows in the same column* as if "operad" meant a fixed thing; it does not, it means "$T$-operad", and the $T$ is load-bearing.

---

# Legal Operations Used

1. **Operation 1 (specialize the monad to read off a classical structure).** Applied to three monads.
2. **Operation 2 (compute $T1$ to find the arity object).** Determines the operad column.
3. **Operation 6 (collapse to the one-object case to get an operad).** The $C_0 = 1$ column.
4. **Operation 7 (turn an operad into a monad and read its algebras).** The algebra column.
5. **Illegal-but-tempting #4 (read down a column instead of across a row).** This exercise's payoff is understanding precisely why this is an error.

---

# Hints

> [!note]- Hint 1
> Build the table one *row* at a time. For each $T$, you already know $T C_0$ and $T1$ from earlier exercises: identity gives single objects and one arity; lists give list-domains and arity $\mathbb{N}$; $\mathbb{T}$ gives pasting-diagram domains and pasting-diagram arities.

> [!note]- Hint 2
> Row $\mathrm{id}$: directed graph / small category / monoid / monoid-action (a set on which a monoid acts). Row $(-)^{*}$: signature (multigraph) / multicategory / operad / operad-algebra. Row $\mathbb{T}$: globular set / globular multicategory / globular operad / weak higher category of that signature.

> [!note]- Hint 3
> For the reading directions: a *row* is internally coherent because all four constructions use the same $T$, so they fit together (a $T$-operad is a special $T$-multicategory, whose underlying data is a $T$-graph, and which has algebras). A *column* is a single functorial construction (e.g. "form the one-object case") applied to three different cartesian monads — it shows the construction is uniform, not that the three outputs are the same kind of object.

---

# Solution

The plan: build the table row by row, justifying each cell from the chapter's results (Steps 1–3, one per monad); then explain the row-reading and column-reading directions and why conflating them is the characteristic error (Step 4).

**Step 1: Row $T = \mathrm{id}$.**

> [!note]- Derivation
> $T C_0 = C_0$ (single-object domains) and $T1 = 1$ (one arity).
> - **$T$-graph:** $C_0, C_1$ with $\mathrm{dom}, \mathrm{cod} : C_1 \to C_0$ — a *directed graph* (objects = vertices, arrows = edges).
> - **$T$-multicategory:** a small [[Def - Category|category]] (composition on composable pairs), by [[Thm - Generalized Operads Recover Classical Structures]] and [[Ex - A category is an identity-multicategory]].
> - **$T$-operad** ($C_0 = 1$): a one-object category, i.e. a [[Def - Monoid in a Monoidal Category|monoid]].
> - **Algebra:** an algebra for the monoid-as-operad is a set $X$ with a monoid action (the induced monad is "$X \mapsto P \times X$" for the monoid $P$, whose algebras are $P$-sets).

**Step 2: Row $T = (-)^{*}$.**

> [!note]- Derivation
> $T C_0 = C_0^{*}$ (list domains) and $T1 = \mathbb{N}$ (one arity per natural number).
> - **$T$-graph:** $C_0, C_1$ with $\mathrm{dom} : C_1 \to C_0^{*}$ — a *signature* / multigraph (each arrow has a list of input objects and one output object).
> - **$T$-multicategory:** a classical (plain, non-symmetric) **multicategory** = coloured operad, by [[Thm - Generalized Operads Recover Classical Structures]].
> - **$T$-operad** ($C_0 = 1$): a classical non-symmetric **operad** with sets $P(n)$, by [[Ex - A classical operad is a free-monoid-operad]].
> - **Algebra:** a classical operad-algebra — a set $X$ with maps $P(n) \times X^n \to X$ coherent under substitution; for $\mathrm{Assoc}$ this is a monoid (see [[Ex - Algebras for the associative operad are monoids]]).

**Step 3: Row $T = \mathbb{T}$.**

> [!note]- Derivation
> $\mathbb{T} C_0$ is the globular set of pasting diagrams on $C_0$ (pasting-diagram domains) and $\mathbb{T}1$ is the set of globular pasting diagrams (arities = pasting shapes).
> - **$T$-graph:** a *globular set* with a domain map into pasting diagrams — the underlying data of higher cells.
> - **$T$-multicategory:** a **globular multicategory** (a many-object globular operad).
> - **$T$-operad** ($C_0 = 1$): a **globular operad** — a globular set $P$ with $\mathrm{ar} : P \to \mathbb{T}1$ cartesian, operad unit, and composition.
> - **Algebra:** a **weak higher category of that signature**; for the initial contractible globular operad, a weak $\omega$-category (Batanin–Leinster, HC7).

**Step 4: The two reading directions.**

> [!note]- Derivation
> *Reading a row (one theory).* Fix $T$. The four cells of that row fit together into one coherent world: the $T$-graph is the underlying data, the $T$-multicategory adds composition, the $T$-operad is its one-object specialization, and the algebra is what the operad acts on. Each cell refers to the *same* $T$, so they cohere — a $T$-operad really is a special $T$-multicategory, whose forgetful image is a $T$-graph, and which has a category of algebras. A row is therefore "the theory of $T$-shaped composition", a single mathematical subject (ordinary category theory, operad theory, or higher category theory).
>
> *Reading a column (one construction).* Fix a column, say "$T$-operad". Across the three rows it produces monoids, operads, and globular operads. These are *not the same kind of object*; what is the same is the *construction* — "take the one-object case of the monoid-in-$T$-spans" — applied to three different cartesian monads. A column demonstrates the *uniformity* of a construction, the fact that one generic definition specializes correctly everywhere, which is exactly what makes a generic theorem (like [[Thm - The Free Multicategory Monad|the free $T$-multicategory monad]]) a theorem about all three rows at once.
>
> *Why conflating them is the error.* The seductive mistake is to compare, say, "multicategory" (row $(-)^{*}$) with "globular operad" (row $\mathbb{T}$) because they look adjacent, and to expect "operad" to mean a fixed thing regardless of $T$. It does not: "operad" abbreviates "$T$-operad", and the $T$ changes the meaning entirely. Comparison *across rows* is a statement about the construction's uniformity, never about any one theory; comparison *within a row* is mathematics inside one theory. Keeping the two directions distinct is the whole conceptual payoff of the table.

> [!note]- Complete formal solution
> The unifying table:
>
> | $T$ | $T$-graph | $T$-multicategory | $T$-operad ($C_0 = 1$) | algebra |
> |---|---|---|---|---|
> | $\mathrm{id}$ | directed graph | small category | monoid | monoid-set |
> | $(-)^{*}$ | signature (multigraph) | multicategory | operad | operad-algebra |
> | $\mathbb{T}$ | globular set | globular multicategory | globular operad | weak higher category |
>
> Each first-three-columns entry is [[Thm - Generalized Operads Recover Classical Structures]]; the algebra column is the algebra-transport of that theorem together with [[Def - Algebra for a Generalized Operad|the algebra definition]]; the $\mathbb{T}$ row is justified in HC7. A **row** fixes $T$ and is one coherent theory (data, composed structure, one-object case, algebras all share the same $T$). A **column** fixes the construction and varies $T$, exhibiting the uniformity of that construction. Conflating the two — expecting "operad" to mean a fixed object across rows — is the error guarded against by illegal-but-tempting operation #4: "operad" means "$T$-operad", and the $T$ is load-bearing. $\blacksquare$

---

# Key Takeaways

**A row is a theory; a column is a construction — and the entire conceptual value of the framework is keeping the two straight.** The table is not a list of analogies; it is a precise statement that one definition, "monoid in $T$-spans", specializes to ordinary category theory, operad theory, and higher category theory as $T$ ranges over three cartesian monads. Reading across a row gives you a coherent subject; reading down a column gives you a uniform construction that you can prove things about once and apply everywhere. The reusable discipline is, whenever you meet a new higher-categorical structure, to ask "which row is this?" — i.e. which monad generates it — because identifying the row hands you the entire theory (graph, multicategory, operad, algebra) and lets you import every generic theorem of the framework.

**The meaning of every entry is controlled by two computations, $T C_0$ and $T1$, so the table is fully mechanical once those are known.** Building the table required no new ideas beyond the two object-computations done in §1–§2: $T C_0$ tells you what an arrow's domain is (single object / list / pasting diagram), and $T1$ tells you what the arities are (one / $\mathbb{N}$ / pasting diagrams). Every cell follows. The transferable insight is that the apparent diversity of the classical structures (categories, operads, globular operads) is an illusion of presentation: they differ only in two objects, and once those are computed, the structures and their algebras are read off uniformly. This is why "compute $T C_0$ and $T1$" is the master move of the chapter.

**Uniformity is the payoff: a generic theorem about $T$-multicategories is automatically a theorem about every row.** Because the four constructions never inspect the internal nature of $T$, anything proved generically — the existence of free $T$-multicategories ([[Thm - The Free Multicategory Monad]]), the monad-algebra characterization of algebras, the slice construction — descends to all three rows simultaneously. This is the deep economy the framework buys: instead of separately developing free categories, free operads, and free globular operads, one develops the free $T$-multicategory once and reads off all three. The trigger to carry forward is that the *thinness* of the definition (just a monoid in spans) is exactly what enables this transfer; the content lives in $T$, and the genericity lives in the framework. See [[Thm - Generalized Operads Recover Classical Structures]] for the rigorous row-by-row equivalences underpinning the table.
