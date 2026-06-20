---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - Baez-Dolan Opetopic Weak n-Categories"
  - "Def - Opetopic Set"
  - "Def - Category"
  - "Def - Limit and Colimit"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Verify the $n = 1$ calibration of the opetopic definition: show that an [[Def - Opetopic Set|opetopic set]] satisfying the universal-filler condition, with all cells above dimension $1$ forced unique/trivial, is exactly an ordinary [[Def - Category|category]]. Concretely, show that the universal fillers of the $2$-dimensional niches supply a unique composite for every composable string of $1$-cells, and that universality forces associativity and the unit laws.

**Recall:**

![[Thm - Baez-Dolan Opetopic Weak n-Categories#Statement]]

A **niche** is a many-in, one-out configuration of cells awaiting a composite: the source pasting diagram and the boundary are given, the filling cell is not. A **universal filler** is a filler that is initial (or terminal) among all fillers of the niche — the opetopic analogue of a [[Def - Limit and Colimit|universal cone]]. An ordinary [[Def - Category|category]] has objects, morphisms, a unique composite $g \circ f$ for composable $f, g$, satisfying associativity and unit laws.

---

# Convergent Strategy

**Problem class:** This is a *validate-a-definition-in-a-low-case* problem — the validation problem class from the topic page. The goal is to unwind the abstract universal-filler condition at $n = 1$ and match it against the explicit category axioms, confirming the opetopic definition reproduces the known notion.

**Assumption pattern:** The decisive assumption is that *cells above dimension $1$ are forced unique/trivial*. This collapses "universal up to a higher cell" into "unique on the nose", which is exactly what turns a weak composite into a strict one. Tracking what this triviality does at each step is the key to the whole calibration.

**Theorem routing:** We route through the calibration theorem ([[Thm - Baez-Dolan Opetopic Weak n-Categories|Baez–Dolan opetopic weak n-categories]], $n = 1$ case) and its supporting lemmas — essential uniqueness of universal fillers (Lemma 1) and the derivation of the category laws (Lemma 2). We use the universal property in the [[Def - Limit and Colimit|universal-cone]] sense.

**Key decision point:** The non-obvious choice is to use *triviality of $2$-cells* to upgrade "universal filler" (a priori unique only up to iso) to "unique composite" (equal on the nose), and then to read associativity off as "two bracketings are fillers of the same niche, hence equal". The tempting error is to expect associativity to be a separate axiom one must impose; in fact universality plus triviality forces it.

---

# Legal Operations Used

1. **Operation 5 (recognise a niche and demand a filler)** from the topic page. Composing a string of $1$-cells means forming its niche and taking the universal filler; the filler's output $1$-cell is the composite.

2. **Operation 6 (identify a universal property in lieu of an equation)** from the topic page. Associativity and the unit laws are *not* imposed; they emerge from the universal property of the fillers together with the triviality of $2$-cells.

3. **Operation 7 (truncate to recover a known structure)** from the topic page. Forcing cells above dimension $1$ to be trivial is exactly the truncation that should reproduce ordinary categories.

---

# Hints

> [!note]- Hint 1
> A $2$-dimensional niche at $n = 1$ is a composable string of $1$-cells $f_1, \dots, f_k$ awaiting one output $1$-cell. Its universal filler is a $1$-cell $g$ together with a $2$-cell witnessing $g$ is the composite. But $2$-cells are trivial, so the witness is an equality.

> [!note]- Hint 2
> Use essential uniqueness of universal fillers (Lemma 1 of the theorem). Two universal fillers are uniquely isomorphic via a $2$-cell; since $2$-cells are trivial, the isomorphism is an identity, so the composite is *unique*.

> [!note]- Hint 3
> For associativity, note that $h \circ (g \circ f)$ and $(h \circ g) \circ f$ are universal fillers of niches with the *same* source $f, g, h$ and the same boundary. By uniqueness they are equal. The unit laws come from the arity-$1$ and arity-$0$ niches.

---

# Solution

The route is to identify niches and fillers at $n = 1$, use triviality of $2$-cells to make composites unique, then read the category laws off universality.

**Step 1: Niches and fillers at $n = 1$ give composites.**

> [!note]- Derivation
> At $n = 1$, the cells of the [[Def - Opetopic Set|opetopic set]] $X$ are $0$-cells (objects), $1$-cells (morphisms), and $2$-cells, with the $2$-cells (and higher) forced unique/trivial. A $2$-dimensional niche is a composable string of $1$-cells $f_1, \dots, f_k$ (arranged head-to-tail) awaiting a single output $1$-cell. By Operation 5, the universal filler supplies an output $1$-cell $g$ — the **composite** — together with a $2$-cell witnessing that $g$ is the composite of the string. We write $g = f_k \circ \dots \circ f_1$. The arity-$2$ case gives the binary composite $g \circ f$; the existence of a filler for *every* niche is exactly the existence of composites for every composable pair.

**Step 2: Triviality of $2$-cells makes the composite unique.**

> [!note]- Derivation
> By Lemma 1 of [[Thm - Baez-Dolan Opetopic Weak n-Categories|the calibration theorem]], any two universal fillers of the same niche are connected by a unique invertible cell one dimension up — here, a $2$-cell. But $2$-cells are forced trivial (unique/identity), so the invertible cell is an identity, and the two universal fillers are *equal*. Hence the composite output $1$-cell is unique: there is exactly one composite for each composable string. This is precisely the composition *function* of a category, $\mathrm{Hom}(b,c) \times \mathrm{Hom}(a,b) \to \mathrm{Hom}(a,c)$, $(g, f) \mapsto g \circ f$.

**Step 3: Universality forces associativity and the unit laws.**

> [!note]- Derivation
> **Associativity.** Consider three composable $1$-cells $f, g, h$. The composites $h \circ (g \circ f)$ and $(h \circ g) \circ f$ are each obtained as universal fillers of niches whose source is the string $f, g, h$ and whose boundary (outermost source and target objects) coincide. They are therefore universal fillers of niches with the *same* source configuration and boundary; by the uniqueness of Step 2, they are equal:
> $$h \circ (g \circ f) \;=\; (h \circ g) \circ f.$$
> (Operation 6: associativity is not imposed; it is forced by universality plus triviality.)
>
> **Unit laws.** The arity-$1$ niche on a single $1$-cell $f$ has $f$ itself as its universal filler, so composing the one-element string $f$ gives back $f$. The arity-$0$ niche at an object $a$ — a niche with empty source — has as universal filler the identity $1$-cell $\mathrm{id}_a$. Then $f \circ \mathrm{id}_a$ and $\mathrm{id}_b \circ f$ are universal fillers of the same niche as $f$ (their source strings reduce to $f$ after the identity is inserted), hence equal to $f$ by uniqueness:
> $$f \circ \mathrm{id}_a = f = \mathrm{id}_b \circ f.$$
>
> So $X$ has objects, morphisms, a unique associative unital composite — it is exactly a [[Def - Category|category]]. Conversely, any category gives such an $X$ (its opetopic nerve with unique fillers), so the $n = 1$ opetopic weak categories are precisely categories.

> [!note]- Complete formal solution
> Let $X$ be an [[Def - Opetopic Set|opetopic set]] with universal fillers and trivial cells above dimension $1$.
>
> *Composites.* A $2$-dimensional niche is a composable string of $1$-cells; its universal filler (Operation 5) outputs a $1$-cell $g$, the composite $f_k \circ \dots \circ f_1$. By Lemma 1 of [[Thm - Baez-Dolan Opetopic Weak n-Categories|the theorem]], two universal fillers differ by a $2$-cell; triviality of $2$-cells makes them equal, so the composite is unique — the composition function of a category.
>
> *Associativity.* $h \circ (g \circ f)$ and $(h \circ g) \circ f$ are universal fillers of niches with the same source $f, g, h$ and boundary, hence equal.
>
> *Units.* The arity-$0$ niche gives $\mathrm{id}_a$; the arity-$1$ niche gives $f \mapsto f$; so $f \circ \mathrm{id}_a = f = \mathrm{id}_b \circ f$.
>
> Thus $X$ is a [[Def - Category|category]], and conversely every category arises this way. $\blacksquare$

---

# Key Takeaways

**Triviality of top cells is what turns weak into strict.** The entire $n = 1$ calibration hinges on a single mechanism: when the cells one dimension above the composites are forced trivial, "universal up to a higher cell" collapses to "unique on the nose", and a weak composite becomes a strict one. The trigger to watch for is any truncation or strictness hypothesis in a higher-categorical definition: ask what becomes *unique* when the top cells are killed, and the strict structure falls out. This is the same mechanism by which a Kan complex with trivial higher homotopy is a set, and by which a bicategory with trivial $2$-cells is a category — strictness is the shadow of triviality one dimension up.

**Universality manufactures the laws you would otherwise have to impose.** The striking feature of this calibration is that associativity and the unit laws are *not* separate axioms — they are forced by the universal property of the fillers. The reusable insight is that a universal characterisation of an operation automatically carries its coherence: if a composite is *the* universal filler, then two ways of computing it are the same universal filler, hence equal. The trigger is any time you are tempted to bolt on associativity/coherence axioms by hand; check first whether characterising the operation universally already forces them. This is the deepest reason the opetopic (and limit-based) approach scales to all dimensions without an infinite regress of equations.

**A composite is a universal filler — composition is recognised, not computed.** The exercise makes concrete the chapter's central reframing: even in an ordinary category, the composite $g \circ f$ can be seen as the universal filler of the niche formed by $f$ and $g$, rather than as the output of a composition function. The reusable principle is that operations defined by output-of-a-function and operations defined by universal-property-of-a-witness are interchangeable when fillers are unique, and only the latter survives weakening. The trigger is any composition-like operation in a context where uniqueness might fail (bicategories, homotopy categories, derived functors): replace "the composite" by "the universal filler", and the definition becomes weakening-robust. See [[Ex - At n equals 2 the universal fillers reproduce a bicategory]] for what happens when the top cells are *not* trivial, and [[Ex - A niche without a filler is the obstruction to composition]] for the failure mode when fillers are merely required to exist.
