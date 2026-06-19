---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - 2-Category and Bicategory"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Functor Category"
  - "Thm - The Interchange Law"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that small categories, [[Def - Functor|functors]], and [[Def - Natural Transformation|natural transformations]] form a strict [[Def - 2-Category and Bicategory|2-category]] $\mathbf{Cat}$. Concretely:

1. Identify the $0$-cells, $1$-cells, and $2$-cells.
2. Describe **vertical** composition $\beta \circ \alpha$ of natural transformations and check it makes each hom-collection a category (so $\mathbf{Cat}(\mathcal{C},\mathcal{D}) = [\mathcal{C},\mathcal{D}]$).
3. Describe **horizontal** composition $\gamma \ast \alpha$ and verify the [[Thm - The Interchange Law|interchange law]], thereby confirming horizontal composition is a functor.
4. Confirm that horizontal composition of $1$-cells (functor composition) is *strictly* associative and unital, so $\mathbf{Cat}$ is strict, not merely a bicategory.

**Recall:**

A [[Def - 2-Category and Bicategory|2-category]] is a category enriched in $\mathbf{Cat}$: a class of $0$-cells; for each pair $A,B$ a hom-*category* $\mathcal{B}(A,B)$ (objects the $1$-cells, morphisms the $2$-cells, composition the *vertical* composition $\circ$); composition functors $\mathcal{B}(B,C)\times\mathcal{B}(A,B)\to\mathcal{B}(A,C)$ (the *horizontal* composition $\ast$); identity $1$-cells; with strict associativity and unit laws.

![[Def - Natural Transformation#The Definition]]

A [[Def - Functor|functor]] $F:\mathcal{C}\to\mathcal{D}$ assigns objects and morphisms preserving composition and identities. A [[Def - Natural Transformation|natural transformation]] $\alpha:F\Rightarrow G$ is a family of morphisms $\alpha_X:FX\to GX$ such that for every $f:X\to Y$ the square $\alpha_Y\circ Ff = Gf\circ\alpha_X$ commutes.

The [[Thm - The Interchange Law|interchange law]] is $(\beta'\ast\beta)\circ(\alpha'\ast\alpha) = (\beta'\circ\alpha')\ast(\beta\circ\alpha)$.

---

# Convergent Strategy

**Problem class:** This is a "recognise a familiar structure as a higher category" verification, the first target named in the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to *match data* — write down what $\mathbf{Cat}$ provides, line it up against the 2-category axioms, and check each axiom holds. Nothing is invented; everything is unwound from definitions you already know.

**Assumption pattern:** The recognisable feature is that "the morphisms between two categories themselves form a category" — namely the [[Def - Functor Category|functor category]] $[\mathcal{C},\mathcal{D}]$. This is exactly the enrichment-in-$\mathbf{Cat}$ data: hom-objects that are categories. Once you see $\mathbf{Cat}(\mathcal{C},\mathcal{D}) = [\mathcal{C},\mathcal{D}]$, the 2-cells (natural transformations) and their vertical composition are handed to you for free.

**Theorem routing:** The single non-trivial check routes through the [[Thm - The Interchange Law|interchange law]], which here *is* the well-definedness of horizontal composition of natural transformations — the two formulas $(\gamma\ast\alpha)_X = G'(\alpha_X)\circ\gamma_{FX}$ and $\gamma_{F'X}\circ G(\alpha_X)$ agreeing is precisely the naturality square of $\gamma$, and that agreement is interchange.

**Key decision point:** The non-obvious choice is *which* composition is "vertical" and which is "horizontal", because both are called "composition of natural transformations" in different texts. Vertical composition stacks transformations between *parallel* functors (same source and target categories); horizontal composition composes transformations along a *shared middle* category. Getting this backwards makes the interchange law unparseable.

---

# Legal Operations Used

1. **Operation 1 (unwind an enriched definition in the base).** We unwind "enriched in $\mathbf{Cat}$" by identifying the hom-objects as functor categories and the composition functors as horizontal composition.

2. **Operation 5 (paste 2-cells and use interchange).** The interchange check is the one place pasting matters; we evaluate a $2\times 2$ grid of natural transformations two ways and confirm agreement.

---

# Hints

> [!note]- Hint 1
> The $0$-cells are categories and the $1$-cells are functors. What are the $2$-cells, and what is the hom-*category* $\mathbf{Cat}(\mathcal{C},\mathcal{D})$? You have already met it under another name.

> [!note]- Hint 2
> Vertical composition is componentwise: $(\beta\circ\alpha)_X = \beta_X\circ\alpha_X$ in $\mathcal{D}$. Check this is a natural transformation and that it is associative and unital — i.e. that $[\mathcal{C},\mathcal{D}]$ is a category.

> [!note]- Hint 3
> Horizontal composition of $\alpha:F\Rightarrow F'$ and $\gamma:G\Rightarrow G'$ has two candidate component formulas; they agree by the naturality of $\gamma$. That agreement is the interchange law. Write the naturality square of $\gamma$ at the morphism $\alpha_X$.

---

# Solution

The proof matches the four pieces of 2-category data against $\mathbf{Cat}$ in order. Step 1 names the cells. Step 2 shows the hom-collection is the functor category, so vertical composition is its composition. Step 3 builds horizontal composition and verifies interchange. Step 4 checks strictness. The only computation is the interchange/naturality identity in Step 3.

**Step 1: The cells.** $0$-cells are small [[Def - Category|categories]] $\mathcal{C}$; $1$-cells $\mathcal{C}\to\mathcal{D}$ are [[Def - Functor|functors]]; $2$-cells $\alpha:F\Rightarrow G$ (for parallel functors $F,G:\mathcal{C}\to\mathcal{D}$) are [[Def - Natural Transformation|natural transformations]].

> [!note]- Derivation
> A $2$-cell must sit between two *parallel* $1$-cells, i.e. two functors with the same source $\mathcal{C}$ and target $\mathcal{D}$. The structure-respecting "morphism of functors" is exactly a natural transformation: a family $\alpha_X:FX\to GX$ with $\alpha_Y\circ Ff = Gf\circ\alpha_X$ for all $f:X\to Y$. So the $2$-cells are natural transformations.

**Step 2: The hom-category is $[\mathcal{C},\mathcal{D}]$, with vertical composition.** Define $(\beta\circ\alpha)_X = \beta_X\circ\alpha_X$. This is natural, associative, and unital, so $\mathbf{Cat}(\mathcal{C},\mathcal{D})$ is the [[Def - Functor Category|functor category]] $[\mathcal{C},\mathcal{D}]$.

> [!note]- Derivation
> *Naturality of $\beta\circ\alpha$:* for $f:X\to Y$, using naturality of $\alpha$ then $\beta$,
> $$(\beta\circ\alpha)_Y\circ Ff = \beta_Y\circ\alpha_Y\circ Ff = \beta_Y\circ Gf\circ\alpha_X = Hf\circ\beta_X\circ\alpha_X = Hf\circ(\beta\circ\alpha)_X,$$
> where $H$ is the target of $\beta$. So $\beta\circ\alpha:F\Rightarrow H$ is natural.
> *Identity:* the identity natural transformation $\mathrm{id}_F$ has components $\mathrm{id}_{FX}$; clearly $\mathrm{id}_G\circ\alpha = \alpha = \alpha\circ\mathrm{id}_F$.
> *Associativity:* componentwise composition in $\mathcal{D}$ is associative. Hence the natural transformations $F\Rightarrow G$ form the morphisms of a category whose objects are functors — exactly $[\mathcal{C},\mathcal{D}]$.

**Step 3: Horizontal composition and interchange.** For $\alpha:F\Rightarrow F'$ ($\mathcal{C}\to\mathcal{D}$) and $\gamma:G\Rightarrow G'$ ($\mathcal{D}\to\mathcal{E}$), define $\gamma\ast\alpha:GF\Rightarrow G'F'$ by $(\gamma\ast\alpha)_X = G'(\alpha_X)\circ\gamma_{FX} = \gamma_{F'X}\circ G(\alpha_X)$. The two formulas agree by naturality of $\gamma$, and this agreement *is* the interchange law.

> [!note]- Derivation
> The two formulas agree because the naturality square of $\gamma$ at the morphism $\alpha_X:FX\to F'X$ commutes:
> $$\gamma_{F'X}\circ G(\alpha_X) = G'(\alpha_X)\circ\gamma_{FX}.$$
> This is well-definedness of $\gamma\ast\alpha$. To see it as the [[Thm - The Interchange Law|interchange law]], take the $2\times 2$ grid with $\alpha,\alpha'$ stacked vertically in the first column ($F\Rightarrow F'\Rightarrow F''$) and $\gamma,\gamma'$ in the second ($G\Rightarrow G'\Rightarrow G''$). Computing "first vertical, then horizontal" gives $(\gamma'\circ\gamma)\ast(\alpha'\circ\alpha)$; computing "first horizontal, then vertical" gives $(\gamma'\ast\alpha')\circ(\gamma\ast\alpha)$. Equality of the two,
> $$(\gamma'\circ\gamma)\ast(\alpha'\circ\alpha) = (\gamma'\ast\alpha')\circ(\gamma\ast\alpha),$$
> follows componentwise from functoriality of $G,G'$ and naturality, and is exactly the statement that $\ast$ is a [[Def - Functor|functor]] $[\mathcal{D},\mathcal{E}]\times[\mathcal{C},\mathcal{D}]\to[\mathcal{C},\mathcal{E}]$.

**Step 4: Strictness.** Functor composition is strictly associative and unital, so the associator and unitors are identities and $\mathbf{Cat}$ is a *strict* 2-category.

> [!note]- Derivation
> For functors $F,G,H$, both $(H\circ G)\circ F$ and $H\circ(G\circ F)$ send an object $X$ to $H(G(FX))$ and a morphism to $H(G(Ff))$ — equal as assignments, so associativity is an equality, not merely an isomorphism. The identity functor is a strict two-sided unit. Hence all coherence cells are identities: $\mathbf{Cat}$ is strict.

> [!note]- Complete formal solution
> **$0$-, $1$-, $2$-cells.** Categories, functors, natural transformations.
>
> **Hom-categories.** For each pair $\mathcal{C},\mathcal{D}$, $\mathbf{Cat}(\mathcal{C},\mathcal{D}) := [\mathcal{C},\mathcal{D}]$, objects functors, morphisms natural transformations, composition vertical: $(\beta\circ\alpha)_X = \beta_X\circ\alpha_X$. This is a category (naturality, associativity, identities verified in Step 2).
>
> **Composition functors.** $\ast:[\mathcal{D},\mathcal{E}]\times[\mathcal{C},\mathcal{D}]\to[\mathcal{C},\mathcal{E}]$ sends $(G,F)\mapsto G\circ F$ on $1$-cells and $(\gamma,\alpha)\mapsto\gamma\ast\alpha$ on $2$-cells, with $(\gamma\ast\alpha)_X = G'(\alpha_X)\circ\gamma_{FX}$. Well-definedness is naturality of $\gamma$; functoriality (preservation of vertical composition and identities) is the interchange law, verified in Step 3.
>
> **Identities.** The identity $1$-cell on $\mathcal{C}$ is $\mathrm{id}_\mathcal{C}$; the identity $2$-cell on $F$ is $\mathrm{id}_F$.
>
> **Strictness.** Functor composition is strictly associative and unital (Step 4), so all associators and unitors are identities.
>
> All the data and axioms of a strict 2-category are present and verified; therefore $\mathbf{Cat}$ is a strict 2-category. $\quad\blacksquare$

---

# Key Takeaways

**The interchange law is not an extra axiom in $\mathbf{Cat}$ — it is the naturality of natural transformations.** The single computation that gives $\mathbf{Cat}$ its 2-categorical structure is that the two ways of forming the horizontal composite $\gamma\ast\alpha$ agree, and that agreement is literally the commuting naturality square of $\gamma$ evaluated at the morphism $\alpha_X$. So a fact you already accept (naturality) is precisely the higher-categorical coherence (interchange). Whenever you are asked to verify interchange in a concrete 2-category, look for the underlying naturality or functoriality statement: it is almost always already known to you under a different name, and recognising it saves the entire calculation.

**Vertical and horizontal composition are distinguished by *what they share*, and confusing them is the standard error.** Vertical composition stacks $2$-cells between *parallel* $1$-cells — same source and target objects — and is just composition in the hom-category. Horizontal composition composes $2$-cells along a *shared object* in the middle, producing a $2$-cell between composite $1$-cells. The diagnostic to keep: vertical lives inside one hom-category; horizontal crosses between hom-categories via the composition functor. Any time a problem mentions "composition of natural transformations" without saying which, this is the first thing to pin down, because the interchange law only typechecks once the two are correctly assigned.

**$\mathbf{Cat}$ is the strict example, and its strictness is exactly why it is the *motivating* 2-category rather than a bicategory.** Functor composition is associative on the nose because it is ultimately composition of object- and morphism-assignments, i.e. set-function composition, which is strictly associative. This is in sharp contrast to the bicategory of bimodules, where horizontal composition is a tensor product and associativity holds only up to canonical isomorphism. The lesson, reusable across the chapter, is that *strictness is a property of the composition operation*: when horizontal composition is "do one thing then another" (functors, relations-by-strict-composition) it is strict; when it is "form a universal object" (tensor, pullback, coend) it is weak. Diagnosing which you have tells you immediately whether you are in a 2-category or only a bicategory.
