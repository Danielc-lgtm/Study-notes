---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Baez-Dolan Opetopic Weak n-Categories"
  - "Def - 2-Category and Bicategory"
  - "Def - Opetopic Set"
  - "Def - Limit and Colimit"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Verify the $n = 2$ calibration of the opetopic definition: show that an [[Def - Opetopic Set|opetopic set]] satisfying the universal-filler condition, with cells above dimension $2$ forced unique/invertible, carries exactly the data and axioms of a [[Def - 2-Category and Bicategory|bicategory]]. Specifically, extract from the universal $2$-cell fillers a weak horizontal composite of $1$-cells (with a witnessing $2$-cell), and from the universal $3$-cell fillers the associator and unitors, and explain why the pentagon and triangle coherence axioms hold automatically.

**Recall:**

![[Thm - Baez-Dolan Opetopic Weak n-Categories#Statement]]

A [[Def - 2-Category and Bicategory|bicategory]] has objects, $1$-cells, and $2$-cells; horizontal composition of $1$-cells is associative and unital only **up to** invertible coherence $2$-cells — the associator $\alpha$ and unitors $\lambda, \rho$ — which themselves satisfy the pentagon and triangle axioms. A **universal filler** of a niche is the initial/terminal filler, characterised by a [[Def - Limit and Colimit|universal property]]; it is essentially unique.

---

# Convergent Strategy

**Problem class:** This is a *validate-a-definition-in-a-low-case* problem at the hardest rung — the validation problem class. The goal is to extract genuine bicategory data (weak composites, associators, unitors) from the universal-filler condition and to show the coherence axioms are forced, not imposed.

**Assumption pattern:** The decisive assumption is that cells above dimension $2$ are forced unique/invertible, but cells *at* dimension $2$ are genuine. This is what keeps composition weak (the witnessing $2$-cells are real) while making the coherence cells (associator, unitors) essentially unique. The difference from the $n = 1$ case is precisely that $2$-cells are no longer trivial.

**Theorem routing:** We route through the $n = 2$ case of the calibration theorem ([[Thm - Baez-Dolan Opetopic Weak n-Categories|Baez–Dolan opetopic weak n-categories]]) and Lemma 3, using essential uniqueness of universal fillers (Lemma 1) one dimension higher to obtain the coherence cells, and the [[Def - Limit and Colimit|universal-property]] characterisation throughout.

**Key decision point:** The non-obvious choice is to *keep the witnessing $2$-cells as genuine data* (not collapse them to equalities as in the $n = 1$ case), so that composition is weak, and to obtain the associator as the unique invertible $3$-cell-mediated $2$-cell between the two bracketings. The tempting error is to either strictify (collapse $2$-cells, getting a strict $2$-category instead of a bicategory) or to forget that the pentagon is forced (and try to impose it).

---

# Legal Operations Used

1. **Operation 5 (recognise a niche and demand a filler)** from the topic page. Horizontal composition of $1$-cells is the universal $2$-cell filler of their niche; the output $1$-cell is the weak composite and the $2$-cell is its witness.

2. **Operation 6 (identify a universal property in lieu of an equation)** from the topic page. The associator and unitors are universal $3$-cell-fillers; the pentagon and triangle are forced by the universal properties, not imposed.

3. **Operation 7 (truncate to recover a known structure)** from the topic page. Forcing cells above dimension $2$ to be invertible is the truncation that should reproduce bicategories.

---

# Hints

> [!note]- Hint 1
> A niche on two composable $1$-cells $f, g$ has a universal filler: an output $1$-cell (call it $g \otimes f$) and a universal $2$-cell witnessing it. Do **not** collapse the $2$-cell to an equality — at $n = 2$ it is genuine, so the composite is weak.

> [!note]- Hint 2
> For three $1$-cells $f, g, h$, the two bracketings $(h \otimes g) \otimes f$ and $h \otimes (g \otimes f)$ are universal fillers of niches over the same source. By essential uniqueness *one dimension up* (now genuine $3$-cells mediate), there is a unique invertible $2$-cell between them — the associator $\alpha$.

> [!note]- Hint 3
> The pentagon relates the five bracketings of four $1$-cells. Each composite of associators is a $2$-cell built from universal fillers over a common niche; uniqueness of universal fillers forces the two sides of the pentagon to agree. The triangle (associator vs. unitors) is forced identically.

---

# Solution

The route is to extract weak composition from universal $2$-cell fillers, the associator and unitors from universal $3$-cell fillers, and the coherence axioms from essential uniqueness applied one dimension up.

**Step 1: Universal $2$-cell fillers give weak horizontal composition.**

> [!note]- Derivation
> Let $X$ be an [[Def - Opetopic Set|opetopic set]] with universal fillers and cells above dimension $2$ forced unique/invertible; cells at dimension $2$ are genuine. A niche on two composable $1$-cells $f : a \to b$, $g : b \to c$ awaits an output $1$-cell. By Operation 5 its universal filler is an output $1$-cell $g \otimes f : a \to c$ — the **weak horizontal composite** — together with a universal $2$-cell $\mu_{g,f}$ witnessing that $g \otimes f$ is the composite. Crucially, since $2$-cells are not trivial here, $g \otimes f$ is only *a chosen* composite with a real witness, not a strict value. This is exactly a [[Def - 2-Category and Bicategory|bicategory]]'s horizontal composition: defined, but not strictly associative.

**Step 2: Universal $3$-cell fillers give the associator and unitors.**

> [!note]- Derivation
> Take three composable $1$-cells $f, g, h$. Both $(h \otimes g) \otimes f$ and $h \otimes (g \otimes f)$ are output $1$-cells of universal fillers of niches whose source is the string $f, g, h$ and whose boundary objects coincide ($a$ to $d$). By Lemma 1 of [[Thm - Baez-Dolan Opetopic Weak n-Categories|the theorem]] applied *one dimension up* — where the mediating cells are now genuine $3$-cells — there is a unique invertible $2$-cell
> $$\alpha_{h,g,f} : (h \otimes g) \otimes f \;\xrightarrow{\ \cong\ }\; h \otimes (g \otimes f),$$
> the **associator**. It is invertible because the $3$-cells above it are invertible; it is essentially unique because it is the universal-filler-mediated comparison. The **unitors** $\lambda, \rho$ arise identically: the arity-$0$ niche gives the identity $1$-cells $\mathrm{id}_a$, and the universal $3$-cell fillers comparing $\mathrm{id}_b \otimes f$ and $f \otimes \mathrm{id}_a$ with $f$ give the invertible unitor $2$-cells.

**Step 3: The pentagon and triangle are forced.**

> [!note]- Derivation
> **Pentagon.** For four composable $1$-cells $f, g, h, k$ there are five bracketings, related by associators in two paths around a pentagon. Each path is a composite of associators, i.e. a $2$-cell built from universal $3$-cell fillers over niches with the *same* source $f, g, h, k$ and boundary. By essential uniqueness of universal fillers (Lemma 1, applied to the $3$-cells), the two paths produce the *same* invertible $2$-cell, so the pentagon commutes. (Operation 6: the pentagon is not imposed; it is the equality of two universal-filler-built comparisons of the same niche.)
>
> **Triangle.** The triangle axiom relates the associator $\alpha_{g, \mathrm{id}, f}$ to the unitors $\rho, \lambda$. Both sides are $2$-cells built from universal fillers over the niche with source $f, \mathrm{id}, g$; by uniqueness they agree, so the triangle commutes.
>
> Therefore $X$ has objects, $1$-cells, $2$-cells, weak horizontal composition, invertible associator and unitors, and the pentagon and triangle hold — it is exactly a [[Def - 2-Category and Bicategory|bicategory]]. Conversely every bicategory presents such an $X$, so opetopic weak $2$-categories are precisely bicategories.

> [!note]- Complete formal solution
> Let $X$ be an [[Def - Opetopic Set|opetopic set]] with universal fillers, genuine $2$-cells, and invertible/unique cells above dimension $2$.
>
> *Weak composition.* The niche on $f, g$ has a universal filler with output $1$-cell $g \otimes f$ and a genuine witnessing $2$-cell (Operation 5); this is bicategory horizontal composition, not strict.
>
> *Associator/unitors.* For $f, g, h$, the two bracketings are universal fillers over the same niche; by Lemma 1 one dimension up (genuine $3$-cells mediating), a unique invertible $2$-cell $\alpha$ relates them. The arity-$0$ niche gives identities and unitors $\lambda, \rho$ similarly.
>
> *Coherence.* The pentagon's two paths are composites of universal-filler-built associators over the same source $f, g, h, k$; uniqueness of universal fillers forces them equal. The triangle is forced identically.
>
> Hence $X$ is a [[Def - 2-Category and Bicategory|bicategory]], and conversely. $\blacksquare$

---

# Key Takeaways

**Weakness is "keep the witnessing cell genuine"; the dimension of triviality sets the level of strictness.** The decisive difference between the $n = 1$ and $n = 2$ calibrations is one dimension: at $n = 1$ the $2$-cells are trivial and composition is strict; at $n = 2$ the $2$-cells are genuine and composition is weak. The reusable insight is that *the dimension at which cells become trivial is the dimension at which equations replace coherence cells* — push triviality up one level and you weaken composition by one level. The trigger is any question about how weak a higher structure is: locate the first trivial dimension, and everything below it is weak (coherence cells), everything at and above it is strict (equations). This single dial generates the entire ladder from strict to fully weak.

**Coherence axioms are forced because they compare the same niche two ways.** The pentagon and triangle are the most intimidating part of the bicategory definition, yet here they cost nothing: each is an equality of two universal-filler-built comparisons over a *common* niche, and uniqueness of universal fillers forces the equality. The reusable principle is that whenever a coherence law equates two composites of canonical comparisons, and those comparisons are all derived from universal properties over the same data, the law is automatic. The trigger is any pentagon/hexagon/triangle-style coherence condition: check whether all the cells involved are universal-property-derived from a common configuration; if so, the law is forced, and Mac Lane's coherence theorem is the ambient reason. This is why opetopic (and limit-based) definitions never need to *list* coherence axioms.

**Validating a definition means unwinding it against an independently known case.** The real content of this exercise is methodological: a proposed definition of weak $2$-category earns trust only by reproducing the established notion of bicategory, and the way to check this is to unwind the abstract condition (universal fillers) into concrete data and match it term-by-term against the known axioms. The trigger is any new general definition with established special cases: do not take the generality on faith — truncate to the known case and verify the match, paying special attention to where universality silently supplies data (the associator) or laws (the pentagon). This validation discipline is what separates a genuine definition of weak $n$-category from a plausible-looking one, and it is the entry point to the comparison problem. See [[Ex - At n equals 1 the universal filler condition gives a category]] for the strict ($n=1$) companion and [[Ex - A niche without a filler is the obstruction to composition]] for why *universal* (not merely existent) fillers are required.
