---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Equivalence of Categories"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, foundations]
---

# Problem Statement

Let $(F, G, \eta, \varepsilon)$ be an [[Def - Equivalence of Categories|equivalence]] $\mathcal{C} \simeq \mathcal{D}$. Show that $F$ **preserves and reflects** monomorphisms and epimorphisms:
$$f \text{ is a monomorphism in } \mathcal{C} \iff Ff \text{ is a monomorphism in } \mathcal{D},$$
and the same for epimorphisms. (More generally, an equivalence preserves and reflects every property expressible in the language of categories, including [[Def - Limit and Colimit|limits and colimits]]; state this and sketch why, using that a fully faithful functor preserves and reflects [[Def - Limit and Colimit|limit cones]].)

**Recall:**

![[Def - Isomorphism, Monomorphism, Epimorphism#The Definition]]

An [[Def - Equivalence of Categories|equivalence]] is [[Def - Full, Faithful, and Essentially Surjective Functor|full, faithful, and essentially surjective]]; in particular fully faithful, so each $\mathcal{C}(A,B) \to \mathcal{D}(FA, FB)$ is a bijection.

---

# Convergent Strategy

**Problem class:** This is a "show a functor preserves/reflects a categorical property" exercise. The route is to translate the cancellation definition of mono/epi across the hom-set bijection that a fully faithful functor provides, using essential surjectivity to cover all test objects.

**Assumption pattern:** The key leverage is full faithfulness (hom-set bijections) plus essential surjectivity (every test object of $\mathcal{D}$ is iso to $FX$ for some $X$). Mono is a cancellation property quantified over test objects; the bijection turns the cancellation upstairs into the cancellation downstairs, and essential surjectivity ensures *all* downstairs test objects are accounted for.

**Theorem routing:** Use that fully faithful functors induce bijections $\mathcal{C}(X, A) \cong \mathcal{D}(FX, FA)$, so $f$ left-cancellable against $\mathcal{C}$-test-objects iff $Ff$ left-cancellable against $\mathcal{D}$-test-objects of the form $FX$. Then essential surjectivity extends "test objects $FX$" to "all test objects" up to iso. The general limit statement routes through "fully faithful functors reflect limit cones".

**Key decision point:** The non-obvious step is handling the *quantifier over all test objects*. Full faithfulness alone gives cancellation against test objects in the image of $F$; one needs essential surjectivity to conclude cancellation against *every* object of $\mathcal{D}$ (any test object is isomorphic to some $FX$, and cancellation is invariant under pre-composing with an iso).

---

# Legal Operations Used

1. **Operation: translate a cancellation property across a hom-set bijection** (topic page, Legal Operation 11). Full faithfulness moves mono/epi between $\mathcal{C}$ and $\mathcal{D}$.

2. **Operation: cover all test objects via essential surjectivity** (topic page, Legal Operation 4). Every $\mathcal{D}$-object is iso to some $FX$, extending the quantifier.

3. **Operation: invariance of mono/epi under composition with isomorphisms** (topic page, Legal Operation 6). Replacing a test object by an isomorphic one preserves cancellation.

---

# Hints

> [!note]- Hint 1
> Write "$f$ mono" as: for all test objects $X$ and $g, h : X \to A$, $fg = fh \Rightarrow g = h$. You want to transport this to $Ff$.

> [!note]- Hint 2
> Full faithfulness gives a bijection $\mathcal{C}(X, A) \cong \mathcal{D}(FX, FA)$ compatible with composition. So $fg = fh$ in $\mathcal{C}$ corresponds to $Ff \cdot Fg = Ff \cdot Fh$ in $\mathcal{D}$, and $g = h$ iff $Fg = Fh$.

> [!note]- Hint 3
> This handles test objects of the form $FX$. For an arbitrary test object $Y$ in $\mathcal{D}$, use essential surjectivity: $Y \cong FX$ for some $X$, and pre-composing with the iso $Y \cong FX$ does not affect cancellation.

> [!note]- Hint 4
> For limits: a fully faithful functor reflects limit cones, and an essentially surjective fully faithful functor (an equivalence) preserves them too — because the universal property is a statement about hom-sets, which the bijection transports.

---

# Solution

The plan: prove $F$ preserves and reflects monos using the hom-set bijection (full faithfulness) to transport the cancellation property, and essential surjectivity to cover all test objects. Epis are dual. The general limit statement is sketched via "the universal property is a hom-set statement, transported by the bijection".

**Step 1: $F$ preserves and reflects monomorphisms.**

> [!note]- Derivation
> Let $f : A \to B$ in $\mathcal{C}$. Recall $f$ is a [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] iff for every $X$ and $g, h : X \to A$, $fg = fh \Rightarrow g = h$.
>
> ($f$ mono $\Rightarrow Ff$ mono.) Take any $Y$ in $\mathcal{D}$ and $p, q : Y \to FA$ with $Ff \circ p = Ff \circ q$. By essential surjectivity, choose $X$ and an iso $\theta : FX \xrightarrow{\sim} Y$. Then $Ff \circ (p\theta) = Ff \circ (q\theta)$ with $p\theta, q\theta : FX \to FA$. By full faithfulness, $p\theta = Fg$ and $q\theta = Fh$ for unique $g, h : X \to A$, and $Ff \circ Fg = Ff \circ Fh$ means $F(fg) = F(fh)$, so $fg = fh$ by faithfulness. Since $f$ is mono, $g = h$, hence $Fg = Fh$, i.e. $p\theta = q\theta$, and as $\theta$ is iso (hence epi), $p = q$. So $Ff$ is mono.
>
> ($Ff$ mono $\Rightarrow f$ mono.) Take $g, h : X \to A$ with $fg = fh$. Then $F(fg) = F(fh)$, i.e. $Ff \circ Fg = Ff \circ Fh$. Since $Ff$ is mono, $Fg = Fh$, and by faithfulness $g = h$. So $f$ is mono. Hence $F$ preserves and reflects monomorphisms.

**Step 2: $F$ preserves and reflects epimorphisms.**

> [!note]- Derivation
> By [[Thm - The Duality Principle|duality]], epimorphism is the dual of monomorphism, and an [[Def - Equivalence of Categories|equivalence]] $\mathcal{C} \simeq \mathcal{D}$ induces an equivalence $\mathcal{C}^{\mathrm{op}} \simeq \mathcal{D}^{\mathrm{op}}$ (same functors, arrows reversed). A morphism $f$ is epi in $\mathcal{C}$ iff $f^{\mathrm{op}}$ is mono in $\mathcal{C}^{\mathrm{op}}$; applying Step 1 to the opposite equivalence shows $F^{\mathrm{op}}$ preserves and reflects monos, i.e. $F$ preserves and reflects epis. (One may also redo Step 1 verbatim with composition order swapped.) So $F$ preserves and reflects epimorphisms.

**Step 3: Limits, and the general principle.**

> [!note]- Derivation
> A [[Def - Limit and Colimit|limit]] of a diagram $D : \mathcal{J} \to \mathcal{C}$ is an object $L$ with a universal cone, and "universal" is a statement purely about hom-sets: $\mathcal{C}(X, L) \cong \mathrm{Cone}(X, D)$ naturally in $X$. A [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]] functor transports such hom-set statements (it induces natural bijections $\mathcal{C}(X, L) \cong \mathcal{D}(FX, FL)$), so it *reflects* limit cones; an equivalence, being additionally essentially surjective, also *preserves* them (every diagram and every cone in $\mathcal{D}$ comes, up to iso, from one in $\mathcal{C}$). The general principle: **an equivalence preserves and reflects every property expressible in the language of categories** — isos, monos, epis, limits, colimits, initial/terminal objects, [[Def - Adjunction|adjunctions]] — because all such properties are statements about objects, morphisms, and composition, which the equivalence transports faithfully both ways. This is why one may verify a categorical property in whichever of two equivalent categories is easier.

> [!note]- Complete formal solution
> *Mono preserved:* if $f$ is mono and $Ff\,p = Ff\,q$ for $p, q : Y \to FA$, write $Y \cong FX$ (essential surjectivity), reduce to $p\theta = Fg$, $q\theta = Fh$ (full faithfulness), get $fg = fh$ (faithfulness), so $g = h$ (mono), so $p = q$.
>
> *Mono reflected:* if $Ff$ mono and $fg = fh$, then $Ff\,Fg = Ff\,Fh$, so $Fg = Fh$, so $g = h$.
>
> *Epi:* dual, via the equivalence $\mathcal{C}^{\mathrm{op}} \simeq \mathcal{D}^{\mathrm{op}}$.
>
> *Limits and general principle:* limits are hom-set universal properties; fully faithful functors transport these (reflect), equivalences also preserve (essential surjectivity). An equivalence preserves and reflects every categorical property. $\blacksquare$

---

# Key Takeaways

**Equivalences transport every categorical property in both directions.** The headline lesson is the licence this gives: if $\mathcal{C} \simeq \mathcal{D}$, then any property statable in the language of categories — mono, epi, iso, [[Def - Limit and Colimit|limit, colimit]], initial/terminal, [[Def - Adjunction|adjunction]], cartesian closure — holds in $\mathcal{C}$ exactly when it holds in $\mathcal{D}$. So you may always verify such a property in whichever equivalent category is more concrete, and transport the conclusion. This is the practical reason equivalences matter: $\mathbf{FinVect}_k \simeq \mathbf{Mat}_k$ means you can check a property in coordinates and conclude it abstractly. The trigger: facing a categorical property in an awkward category, look for an equivalence to a friendlier one.

**Full faithfulness moves cancellation; essential surjectivity handles the quantifier.** The two ingredients of an equivalence do distinct jobs, and seeing the division of labour is the reusable insight. Full faithfulness provides hom-set bijections, which transport any property phrased through composition (cancellation, universal properties) between the two categories. Essential surjectivity is what lets a property quantified over *all* test objects downstairs be checked against test objects in the image — every downstairs object is isomorphic to an upstairs image, and the property is iso-invariant. Whenever you transport a quantified categorical property, full faithfulness handles the equational core and essential surjectivity discharges the "for all objects" quantifier.

**Preservation and reflection together are what "the same category" should mean.** The fact that an equivalence both preserves (forward) and reflects (backward) categorical properties is precisely the formal content of "$\mathcal{C}$ and $\mathcal{D}$ are categorically the same". A mere functor might preserve a property without reflecting it (the forgetful functor preserves but does not reflect epis); an equivalence does both, which is why it is the right notion of sameness. The diagnostic: a functor that preserves *and reflects* all categorical structure is an equivalence onto its essential image, and recognizing this two-way transport is how one certifies that two categories carry identical categorical information — the foundation of Morita equivalence, derived equivalence, and every "reconstruction" theorem.
