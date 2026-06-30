---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Unbiased Monoidal Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

(a) Recall (from [[Def - Monoidal Category]]) that a [[Def - Monoidal Category|monoidal category]] is the same as a one-object [[Def - 2-Category and Bicategory|bicategory]]. State the dictionary precisely: objects of the monoidal category $\leftrightarrow$ $1$-cells, morphisms $\leftrightarrow$ $2$-cells, tensor $\leftrightarrow$ horizontal composition, unit $\leftrightarrow$ identity $1$-cell, associator/unitors $\leftrightarrow$ the bicategory's coherence cells.

(b) Now give the **unbiased** version of both sides: an [[Def - Unbiased Monoidal Category|unbiased monoidal category]] is a one-object **unbiased bicategory** (a bicategory presented with chosen composites of horizontal strings of *every* length). Show the $n$-ary tensor $\otimes_n$ corresponds to the chosen $n$-fold horizontal composite, and the composition [[Def - Isomorphism|isomorphisms]] $\gamma$ correspond to the comparison cells between different ways of composing a string.

(c) Conclude that "monoidal $=$ one-object bicategory" holds verbatim in biased and unbiased form, and that this is the **bottom row** of the periodic table: a $1$-tuply monoidal $0$-category (a monoid) is to a category as a $1$-tuply monoidal $1$-category (a monoidal category) is to a bicategory.

**Recall:**

A [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$ has $0$-cells, $1$-cells, $2$-cells, horizontal composition (weakly associative), and coherence cells (associator $a$, unitors $l,r$):

![[Def - 2-Category and Bicategory#The Definition]]

An [[Def - Unbiased Monoidal Category|unbiased monoidal category]] has $\otimes_n:\mathcal{C}^n\to\mathcal{C}$ for all $n$ with composition isomorphisms $\gamma$; a [[Def - Monoidal Category|monoidal category]] is its binary, biased shadow.

---

# Convergent Strategy

**Problem class:** This is a *[[Def - Dimension|dimension]]-shift identification* problem (topic-page target four): recognising a monoidal category as a degenerate (one-object) higher structure. It establishes the bottom row of the periodic table, the foundation for the climbing exercise.

**Assumption pattern:** A bicategory with a *single* $0$-cell $\star$ has only one hom-category $\mathcal{B}(\star,\star)$, and all the bicategory data lives inside it. The unlock is that with one object, horizontal composition $\mathcal{B}(\star,\star)\times\mathcal{B}(\star,\star)\to\mathcal{B}(\star,\star)$ is an endofunctor on a single category — exactly a tensor product. Recognising that "one object collapses the two-variable composition into a tensor on the single hom-category" is the key.

**Theorem routing:** Part (a) routes through the [[Def - 2-Category and Bicategory|bicategory]] definition with $\mathcal{B}_0=\{\star\}$, reading off the [[Def - Monoidal Category|monoidal category]] axioms (pentagon $=$ pentagon, triangle $=$ triangle). Part (b) routes through the [[Def - Unbiased Monoidal Category|unbiased]] definitions on both sides: an unbiased bicategory has chosen $n$-fold horizontal composites, which at one object are the $\otimes_n$, and the comparison cells are the $\gamma$. Part (c) reads off the periodic-table row by analogy with monoid $=$ one-object category.

**Key decision point:** The non-obvious point is that the *unbiased* identification is the cleaner one, even though the biased version is more familiar. Biasedly, "monoidal $=$ one-object bicategory" requires matching pentagon to pentagon; unbiasedly, it is a transparent equality of the chosen-composite data ($\otimes_n=$ $n$-fold horizontal composite, $\gamma=$ comparison cells), with coherence automatic. Insisting on the biased dictionary obscures why the identification is so clean; the unbiased dictionary makes it manifest.

---

# Legal Operations Used

1. **Operation 7 from the topic page (restrict to one object to descend the periodic table).** This is the defining move: set $\mathcal{B}_0=\{\star\}$ to turn a bicategory into a monoidal category.

2. **Operation 4 from the topic page (pass between biased and unbiased).** Part (b) uses the unbiased presentation of *both* a bicategory and a monoidal category to make the dictionary an equality of chosen-composite data rather than a pentagon match.

---

# Hints

> [!note]- Hint 1
> A bicategory with one object $\star$ has a single hom-category $\mathcal{M}:=\mathcal{B}(\star,\star)$. Its objects are the $1$-cells $\star\to\star$ and its morphisms are the $2$-cells. This $\mathcal{M}$ will be the underlying category of the monoidal category.

> [!note]- Hint 2
> Horizontal composition $\mathcal{B}(\star,\star)\times\mathcal{B}(\star,\star)\to\mathcal{B}(\star,\star)$ is a functor $\mathcal{M}\times\mathcal{M}\to\mathcal{M}$ — this *is* the tensor $\otimes$. The identity $1$-cell $1_\star$ is the unit object $I$. The associator and unitors of $\mathcal{B}$ are the associator and unitors of $\mathcal{M}$.

> [!note]- Hint 3
> For (b), an *unbiased* bicategory comes with, for each $n$, a chosen $n$-fold horizontal composite of strings of $1$-cells, together with comparison $2$-isomorphisms between different ways of composing. At one object, the chosen $n$-fold composite is $\otimes_n:\mathcal{M}^n\to\mathcal{M}$ and the comparisons are the $\gamma$.

> [!note]- Hint 4
> For (c), recall a monoid is a one-object category (objects collapse, the single hom-set with composition is the monoid). One dimension up: a monoidal category is a one-object bicategory. The periodic-table entry $k$-tuply monoidal $n$-category $=$ $(n+k)$-category with one cell below dimension $k$ gives, for $k=1$, exactly this.

---

# Solution

The plan: (a) collapse a one-object bicategory to its single hom-category and read off the monoidal structure; (b) do the same in the unbiased presentation, matching $\otimes_n$ to $n$-fold horizontal composites and $\gamma$ to comparison cells; (c) place the result as the bottom row of the periodic table by analogy with monoid $=$ one-object category. The single idea is that one object turns two-variable composition into a one-variable tensor.

**Step 1: The biased dictionary.**

A one-object [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$ with object $\star$ is precisely a [[Def - Monoidal Category|monoidal category]] $\mathcal{M}=\mathcal{B}(\star,\star)$.

> [!note]- Derivation
> Let $\mathcal{B}$ be a bicategory with $\mathcal{B}_0=\{\star\}$. Define $\mathcal{M}:=\mathcal{B}(\star,\star)$, the unique hom-category:
> - **objects of $\mathcal{M}$** $=$ $1$-cells $\star\to\star$;
> - **morphisms of $\mathcal{M}$** $=$ $2$-cells (composed by vertical composition, which is the composition of the category $\mathcal{B}(\star,\star)$);
> - **tensor** $\otimes :=$ horizontal composition, a functor $\mathcal{B}(\star,\star)\times\mathcal{B}(\star,\star)\to\mathcal{B}(\star,\star)$, i.e. $\otimes:\mathcal{M}\times\mathcal{M}\to\mathcal{M}$;
> - **unit** $I := 1_\star$, the identity $1$-cell;
> - **associator** $\alpha := a$ (the bicategory's associator), **unitors** $\lambda := l$, $\rho := r$.
>
> The bicategory's pentagon axiom for $a$ is exactly the monoidal pentagon for $\alpha$; the triangle for $l,r,a$ is the monoidal triangle. So $(\mathcal{M},\otimes,I,\alpha,\lambda,\rho)$ is a [[Def - Monoidal Category|monoidal category]]. Conversely a monoidal category builds a one-object bicategory by reversing the dictionary (set $\mathcal{B}(\star,\star)=\mathcal{M}$, horizontal composition $=\otimes$). The two constructions are mutually inverse. (This is the statement on [[Def - Monoidal Category]] and [[Def - 2-Category and Bicategory]], here made into a precise dictionary.)

**Step 2: The unbiased dictionary.**

> [!note]- Derivation
> An *unbiased* bicategory is presented not by a single binary horizontal composition but by, for each $n\geq 0$, a chosen $n$-fold horizontal composite of a string of composable $1$-cells, together with comparison $2$-isomorphisms relating different ways of forming such composites (this is the bicategorical analogue of the unbiased monoidal data — composites of pasting strings of every length).
>
> Restrict to one object $\star$. A string of $n$ composable $1$-cells $\star\to\star$ is just an $n$-tuple of objects of $\mathcal{M}=\mathcal{B}(\star,\star)$. The chosen $n$-fold horizontal composite is therefore a functor
> $$\otimes_n := (\text{$n$-fold horizontal composite}) : \mathcal{M}^n\to\mathcal{M},$$
> with $\otimes_0() = 1_\star = I$ (the empty composite is the identity $1$-cell) and $\otimes_1=\mathrm{id}$. The comparison $2$-isomorphisms — relating "compose the string in sub-blocks, then compose the results" with "compose the whole string at once" — are exactly the composition isomorphisms
> $$\gamma_{k_1,\dots,k_n}:\otimes_n(\otimes_{k_1}(-),\dots,\otimes_{k_n}(-))\cong\otimes_{\sum k_i}(-)$$
> of an [[Def - Unbiased Monoidal Category|unbiased monoidal category]], and the unbiased associativity/unit coherence axioms are the corresponding coherence of the unbiased bicategory. So a one-object unbiased bicategory is exactly an unbiased monoidal category. The dictionary is now an *equality of chosen-composite data*, with no pentagon to match — coherence is automatic on both sides.

**Step 3: The bottom row of the periodic table.**

> [!note]- Derivation
> Recall a [[Def - Monoid in a Monoidal Category|monoid]] is a one-object category: collapse all objects to one, and the single hom-set $\mathcal{C}(\star,\star)$ with composition and identity is exactly a monoid. The periodic-table principle
> $$k\text{-tuply monoidal } n\text{-category} = (n+k)\text{-category with one cell in each dimension} < k$$
> at $k=1$ reads: a $1$-tuply monoidal $n$-category is an $(n+1)$-category with one $0$-cell. For $n=0$ this is a $1$-category (a [[Def - Category|category]]) with one object $=$ a monoid; for $n=1$ it is a $2$-category/bicategory with one object $=$ a [[Def - Monoidal Category|monoidal category]]. So the proportion
> $$\text{monoid} : \text{category} \;::\; \text{monoidal category} : \text{bicategory}$$
> holds exactly, and Steps 1–2 are the $n=1$ instance. This is the **bottom (and second) row** of the periodic table: each step up the column adds a dimension and keeps a single bottom cell; each step right (to braided, symmetric) will add an Eckmann–Hilton-forced commutativity, the subject of the climbing exercise.

> [!note]- Complete formal solution
> **(a)** A one-object [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{B}$ ($\mathcal{B}_0=\{\star\}$) yields the [[Def - Monoidal Category|monoidal category]] $\mathcal{M}=\mathcal{B}(\star,\star)$ with $\otimes=$ horizontal composition, $I=1_\star$, $\alpha=a$, $\lambda=l$, $\rho=r$; the bicategory pentagon/triangle are the monoidal pentagon/triangle. The construction is invertible, so monoidal categories $=$ one-object bicategories.
>
> **(b)** A one-object *unbiased* bicategory has chosen $n$-fold horizontal composites $\otimes_n:\mathcal{M}^n\to\mathcal{M}$ ($\otimes_0()=1_\star=I$) and comparison cells $\gamma$, satisfying the unbiased coherence axioms — exactly an [[Def - Unbiased Monoidal Category|unbiased monoidal category]]. The dictionary is an equality of chosen-composite data.
>
> **(c)** A monoid is a one-object category; by the periodic-table rule ($k=1$), monoid $:$ category $::$ monoidal category $:$ bicategory, the $n=1$ case of which is Steps 1–2. This is the bottom row of the periodic table. $\qquad\blacksquare$

---

# Key Takeaways

**One object turns two-variable composition into a one-variable tensor — the engine of the entire periodic table.** The single mechanism behind this exercise is that a higher structure with exactly one cell in some bottom dimension has all its composition concentrated in a single hom-object, where two-variable horizontal composition becomes a one-variable tensor product. This is *why* climbing a dimension and restricting to one object produces a multiplication: the restriction removes the "which objects" bookkeeping and leaves pure algebra. The trigger to internalise: whenever a structure is described as "one object" (or "one $1$-cell," etc.), expect a tensor (or a braiding) to appear, and identify it as the residual composition. Monoid from one-object category, monoidal category from one-object bicategory, braided monoidal from one-object-one-$1$-cell tricategory — all are this same collapse, one dimension apart.

**The unbiased dictionary is cleaner than the biased one because it matches data, not axioms.** The exercise shows that the famous identification "monoidal $=$ one-object bicategory," usually stated biasedly (and requiring one to check pentagon-against-pentagon), becomes a transparent *equality of chosen-composite data* in the unbiased presentation: $\otimes_n$ is literally the $n$-fold horizontal composite, $\gamma$ is literally the comparison cell, and coherence is automatic. This is a general phenomenon — unbiased presentations make dimension-shift identifications manifest because both sides carry the same all-arity operations. When an identification between two structures feels like it requires checking coherence by hand, try the unbiased presentation of both; the coherence usually evaporates into matching primitive data.

**The periodic table is a literal proportion, and recognising the proportion lets you transport intuition between rows.** Part (c) makes precise that monoid $:$ category $::$ monoidal category $:$ bicategory, and this proportion is not a loose analogy but the $k=1$ case of the exact periodic-table formula. Its value is transport: anything you know about monoids inside categories ([[Def - Homomorphism|homomorphisms]], [[Def - Module|modules]], the bar construction, [[Def - Group|group]] completion) has a one-dimension-up analogue for monoidal categories inside bicategories, obtained by reading the proportion. This is the practical use of the unifying frame — when stuck on a monoidal-categorical question, drop down the proportion to the monoid case, solve it there where intuition is strong, and lift the answer back up. The periodic table is, among other things, a machine for generating such analogies systematically.
