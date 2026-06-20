---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Weak Double Category"
  - "Def - Pullback and Pushout"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $\mathcal{E}$ be a [[Def - Category|category]] with [[Def - Pullback and Pushout|pullbacks]]. Construct the [[Def - Weak Double Category|weak double category]] $\mathbb{S}\mathrm{pan}(\mathcal{E})$ with:

- **objects:** objects of $\mathcal{E}$;
- **vertical $1$-cells** $A \to A'$: morphisms of $\mathcal{E}$;
- **horizontal $1$-cells** $A \nrightarrow B$: spans $A \xleftarrow{p} S \xrightarrow{q} B$;
- **$2$-cells:** morphisms of spans (a map of the apex commuting with both legs, with the given vertical boundaries);

and horizontal composition given by [[Def - Pullback and Pushout|pullback]] over the shared object. Verify the interchange law, and show that $\mathbb{S}\mathrm{pan}(\mathcal{E})$ is *weak* — the associator is the canonical iso between two pullbacks that is not in general an identity. Identify the horizontal unit and the unitors.

**Recall:**

![[Def - Weak Double Category#The Definition]]

A **span** from $A$ to $B$ in $\mathcal{E}$ is a diagram $A\xleftarrow{p}S\xrightarrow{q}B$. The **[[Def - Pullback and Pushout|pullback]]** of $B\xleftarrow{q}S\to ?$ and $B\xleftarrow{p'}S'\to ?$ over $B$ is the universal object $S\times_B S'$ with projections making the square commute, sitting over both $S$ and $S'$. Pullbacks are determined only up to unique isomorphism.

---

# Convergent Strategy

**Problem class:** A *template-identification plus genuine-weakness* problem, parallel to the bimodule case but with [[Def - Pullback and Pushout|pullback]] in place of tensor as the weak horizontal composition.

**Assumption pattern:** Horizontal composition is by pullback, which — like every limit — is associative only up to canonical iso. The vertical $1$-cells are honest morphisms of $\mathcal{E}$, composing strictly. So the "vertical strict / horizontal weak" pattern recurs, now with the weakness coming from the universal property of pullback rather than of tensor.

**Theorem routing:** $\mathbb{S}\mathrm{pan}(\mathcal{E})$ is representable (every string of spans has the iterated pullback as composite), so by the Categorical/Structural definition of [[Def - Weak Double Category|weak double category]] as a representable [[Def - fc-Multicategory|fc-multicategory]], it is a weak double category. It is the bicategory/double-category prototype behind [[Def - Monad Monoid and Module in a Bicategory|monads in Span(Set)]] and [[Thm - Monoids and Modules Form a Bicategory]].

**Key decision point:** The non-obvious choice is to compose spans by pullback (not by some other gluing) — the pullback is exactly the object of "matching pairs $(s, s')$ with $q(s) = p'(s')$", which is the span-theoretic analogue of "composable pairs". The temptation to compose by, say, the disjoint union of apexes gives the wrong (non-associative, non-universal) operation; the pullback is the unique choice with the right universal property.

---

# Legal Operations Used

1. **Operation 6 (horizontal composition as a universal construction).** Here the universal construction is the pullback rather than a coequalizer.

2. **Operation 2 (representability upgrades fc-multicategory to weak double category).** Iterated pullbacks are the universal composites of strings of spans.

3. **Operation 3 (associator from uniqueness of the universal object).** The two iterated pullbacks both compute the limit of the same diagram, so the associator is the unique comparison iso.

4. **Operation 8 (identity span as the horizontal unit).** $\mathrm{U}_A$ is the trivial span $A\xleftarrow{1}A\xrightarrow{1}A$.

---

# Hints

> [!note]- Hint 1
> Composition: given spans $A\xleftarrow{}S\xrightarrow{q}B$ and $B\xleftarrow{p'}S'\xrightarrow{}C$, form the pullback $S\times_B S'$ of $q$ and $p'$; the composite span is $A\leftarrow S\times_B S'\to C$. The horizontal unit at $A$ is the identity span $A\xleftarrow{1}A\xrightarrow{1}A$. Check $\mathrm{U}_A\odot(A\leftarrow S\to B)\cong(A\leftarrow S\to B)$.

> [!note]- Hint 2
> For interchange, a $2$-cell is a map of apexes commuting with the legs. Both ways of pasting a $2\times 2$ grid induce the same map on the pullback apex, by the universal property of pullback. Spell out that the induced maps agree.

> [!note]- Hint 3
> For weakness: $(S\times_B S')\times_C S''$ and $S\times_B(S'\times_C S'')$ are both limits of the diagram $S\to B\leftarrow S'\to C\leftarrow S''$. By uniqueness of limits, there is a canonical iso between them — the associator — but it is not in general an identity, because the two iterated pullbacks are constructed by different sequences of universal constructions.

---

# Solution

We construct $\mathbb{S}\mathrm{pan}(\mathcal{E})$, check interchange, and exhibit weakness from uniqueness of pullbacks.

**Step 1: The four layers, horizontal composition by pullback, and the unit.**

> [!note]- Derivation
> Objects: objects of $\mathcal{E}$. Vertical $1$-cells: morphisms of $\mathcal{E}$, composed strictly. Horizontal $1$-cells $A\nrightarrow B$: spans $A\xleftarrow{p}S\xrightarrow{q}B$. A $2$-cell with top $A\xleftarrow{}S\xrightarrow{}B$, bottom $A'\xleftarrow{}S'\xrightarrow{}B'$, left $f : A\to A'$, right $g : B\to B'$ is a morphism $\alpha : S\to S'$ commuting with the legs via $f, g$. Horizontal composition of $A\xleftarrow{}S\xrightarrow{q}B$ and $B\xleftarrow{p'}S'\xrightarrow{}C$ is $A\leftarrow S\times_B S'\to C$, where $S\times_B S'$ is the [[Def - Pullback and Pushout|pullback]] of $q$ and $p'$. The horizontal unit at $A$ is $\mathrm{U}_A = (A\xleftarrow{1}A\xrightarrow{1}A)$; the left unitor is the iso $A\times_A S\cong S$ from the pullback of an identity, which is canonical.

**Step 2: Interchange.**

> [!note]- Derivation
> Take a $2\times 2$ grid of $2$-cells (span maps). Composing each row horizontally induces, on each row's pullback apex, the unique map determined by the components; then composing vertically stacks these. Composing each column vertically first, then horizontally, induces a map on the same pullback apex. Both induced maps satisfy the same defining equations with respect to the pullback projections, so by the *uniqueness* clause of the pullback's universal property they are equal. Hence interchange holds.

**Step 3: Representability and genuine weakness.**

> [!note]- Derivation
> A string of spans $A_0\nrightarrow A_1\nrightarrow\cdots\nrightarrow A_n$ has the iterated pullback $S_1\times_{A_1}S_2\times_{A_2}\cdots\times_{A_{n-1}}S_n$ as its universal composite (the limit of the zig-zag diagram), so every string is representable and $\mathbb{S}\mathrm{pan}(\mathcal{E})$ is a [[Def - Weak Double Category|weak double category]] by the representable-fc-multicategory criterion. Weakness: for three composable spans, $(S\times_B S')\times_C S''$ and $S\times_B(S'\times_C S'')$ are both limits of the single diagram $S\xrightarrow{q}B\xleftarrow{p'}S'\xrightarrow{q'}C\xleftarrow{p''}S''$. By uniqueness of limits there is a unique iso $a$ between them commuting with the projections — the associator — but it is *not* generally an identity, since the two objects are constructed by different orders of pullback and need not be literally equal even in $\mathcal{E}=\mathbf{Set}$ (their elements are nested pairs $((s,s'),s'')$ versus $(s,(s',s''))$). The pentagon holds because all bracketings compute the same limit and the comparison maps are unique.

> [!note]- Complete formal solution
> For $\mathcal{E}$ with pullbacks, define $\mathbb{S}\mathrm{pan}(\mathcal{E})$: objects $=$ objects of $\mathcal{E}$; vertical $1$-cells $=$ morphisms (strict); horizontal $1$-cells $A\nrightarrow B$ $=$ spans $A\leftarrow S\to B$; $2$-cells $=$ span maps with the given boundaries. Horizontal composition is the pullback $S\times_B S'$; the horizontal unit at $A$ is the identity span, with unitors the canonical isos $A\times_A S\cong S\cong S\times_B B$. Interchange holds by uniqueness of maps into a pullback. Every string of spans has the iterated pullback as universal composite, so $\mathbb{S}\mathrm{pan}(\mathcal{E})$ is a representable [[Def - fc-Multicategory|fc-multicategory]], i.e. a [[Def - Weak Double Category|weak double category]]. It is genuinely weak: $(S\times_B S')\times_C S''$ and $S\times_B(S'\times_C S'')$ both compute the limit of the zig-zag $S\to B\leftarrow S'\to C\leftarrow S''$, so the associator is the unique comparison iso, which (in $\mathbf{Set}$, on nested pairs $((s,s'),s'')\leftrightarrow(s,(s',s''))$) is not the identity. $\blacksquare$

---

# Key Takeaways

**Spans compose by pullback because pullback is "the object of matching pairs".** The single most important recognition is that the pullback $S\times_B S'$ is exactly the object whose elements are pairs $(s, s')$ with $q(s) = p'(s')$ — the span analogue of "composable pairs of arrows". This is why composition of spans is by pullback and nothing else, and it is the same pullback that, for $\mathcal{E}=\mathbf{Set}$, makes a [[Def - Monad Monoid and Module in a Bicategory|monad in Span(Set)]] into a category (the multiplication composes matching pairs of arrows). The trigger: "compose correspondences / relations / spans" $\Rightarrow$ "pullback over the shared object". Recognising this links the span double category to the entire $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$ story of [[Thm - Monoids and Modules Form a Bicategory]].

**Limits (pullbacks) associate weakly for the same reason colimits (tensors) do.** This exercise and [[Ex - The double category of rings and bimodules is weak not strict]] are the dual pair: tensor is a colimit, pullback is a limit, and *both* are universal constructions, hence both associate only up to canonical iso. The associator is, in each case, the unique comparison map between two ways of building the same universal object. The unifying principle is that weakness is the universal property's shadow — and the transferable diagnostic is that *any* horizontal composition defined as a limit or colimit will be weak, so a double category built on one should never be expected to be strict.

**The associator is the unique comparison map, and weakness is its non-triviality.** For three composable spans, the two bracketings both compute the limit of one fixed zig-zag diagram; uniqueness of limits gives a canonical iso (legal operation 3), and that iso is the associator. The pentagon is then free because all bracketings compute the same limit. The element-level picture — nested pairs $((s,s'),s'')$ versus $(s,(s',s''))$ — makes vivid that the iso genuinely relabels data and is not an identity. This is the cleanest possible illustration that "weak" means "coherent comparison maps between universal objects", and that the coherence (pentagon) is automatic precisely because the objects are universal.
