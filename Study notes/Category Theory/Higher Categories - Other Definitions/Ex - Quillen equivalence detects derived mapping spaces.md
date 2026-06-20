---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - Comparison of Models for (∞,1)-Categories"
  - "Def - Quillen Adjunction and Quillen Equivalence"
  - "Def - Model Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $F : \mathcal{M} \rightleftarrows \mathcal{N} : G$ be a **[[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]** between [[Def - Model Category|model categories]]. Show that it induces, for all objects, an equivalence of **derived mapping spaces**
$$
\mathrm{Map}_{\mathcal{M}}(X, Y) \;\simeq\; \mathrm{Map}_{\mathcal{N}}(\mathbb{L}F\,X,\ \mathbb{L}F\,Y),
$$
not merely an equivalence of homotopy *categories* (which only sees $\pi_0$ of these spaces). Conclude that a Quillen equivalence certifies that two models of $(\infty,1)$-categories carry the *same homotopy theory* — the criterion behind the **[[Thm - Comparison of Models for (∞,1)-Categories|comparison theorem]]** — and exhibit, by contrast, a functor that induces an equivalence of homotopy categories but is *not* a Quillen equivalence, to show the two notions differ.

**Recall:**

![[Def - Quillen Adjunction and Quillen Equivalence#The Definition]]

The **derived mapping space** $\mathrm{Map}_{\mathcal{M}}(X,Y)$ is the homotopy type (a [[Def - Simplicial Set|simplicial set]], well-defined up to weak equivalence) of maps from a cofibrant replacement of $X$ to a fibrant replacement of $Y$, computed via a framing or simplicial resolution; its $\pi_0$ is $\mathrm{Ho}(\mathcal{M})(X,Y)$, and its higher $\pi_n$ record higher homotopies between maps.

A Quillen adjunction $F \dashv G$ is a **Quillen equivalence** if for cofibrant $X \in \mathcal{M}$ and fibrant $Y \in \mathcal{N}$, a map $FX \to Y$ is a weak equivalence iff its adjunct $X \to GY$ is.

---

# Convergent Strategy

**Problem class:** This is a *strengthen-the-conclusion* problem: a Quillen equivalence is usually stated as inducing an equivalence of homotopy categories, and the task is to show it does more — it preserves the full mapping *spaces*. The routine is to compute the derived mapping space as a derived hom and check the derived functors preserve it.

**Assumption pattern:** The Quillen-equivalence hypothesis gives two things: the derived adjunction $\mathbb{L}F \dashv \mathbb{R}G$ on homotopy categories, *and* the derived unit/counit being weak equivalences. The second is the stronger input — it is what upgrades "equivalence of $\pi_0$" to "equivalence of the whole space", because mapping spaces are computed by deriving the hom, and the derived unit/counit being equivalences makes the adjunction-isomorphism hold at the spectral (full mapping-space) level.

**Theorem routing:** The route is: express $\mathrm{Map}_{\mathcal{M}}(X,Y)$ as a derived hom (via a cosimplicial/simplicial framing $X^\bullet$, $Y_\bullet$); use that $\mathbb{L}F$ preserves these framings up to weak equivalence (a left Quillen functor preserves cofibrant objects and the framings built from them); apply the derived adjunction degreewise to get $\mathrm{Map}_{\mathcal{M}}(X,Y) \simeq \mathrm{Map}_{\mathcal{N}}(\mathbb{L}FX, \mathbb{L}FY)$; the derived unit/counit being weak equivalences makes this a genuine equivalence of spaces, not just of $\pi_0$.

**Key decision point:** The non-obvious step is to compute the mapping space as a *derived* hom (using framings/resolutions) rather than a naive hom, and to recognise that "Quillen equivalence" is exactly the condition that this derived hom is preserved *spacewise*. The counterexample (equivalence of homotopy categories that is not a Quillen equivalence) is what shows the distinction is real: $\pi_0$ can be preserved while higher $\pi_n$ are not.

---

# Legal Operations Used

1. **Operation 5 from the topic page (compare models by a Quillen equivalence).** The exercise establishes *what* a Quillen equivalence buys you — the preservation of derived mapping spaces — which is the engine of every comparison in §3.

2. **Operation 6 from the topic page (pass to derived mapping spaces to compare invariants).** We compute and compare the $\mathrm{Map}(X,Y)$ explicitly, the refined invariant beyond the homotopy category.

3. **Illegal operation (examined): treating "equivalence of homotopy categories" as "same homotopy theory".** The counterexample shows this is illegal — the repair is to demand a Quillen equivalence, which preserves mapping spaces.

---

# Hints

> [!note]- Hint 1
> "Equivalence of homotopy categories" only preserves $\pi_0$ of mapping spaces (the hom-sets of $\mathrm{Ho}$). To preserve the whole space you need to preserve the higher $\pi_n$ too. Which extra part of the Quillen-equivalence definition could control the higher homotopies?

> [!note]- Hint 2
> Compute $\mathrm{Map}(X,Y)$ as a *derived* hom using a cosimplicial framing $X^\bullet$ of $X$: $\mathrm{Map}(X,Y)_n = \mathrm{Ho}(X^n, Y)$, roughly. A left Quillen functor preserves cofibrations and hence carries a framing of $X$ to a framing of $FX$.

> [!note]- Hint 3
> Apply the derived adjunction $\mathbb{L}F \dashv \mathbb{R}G$ *degreewise* to the framing. The Quillen-equivalence condition (derived unit/counit are weak equivalences) is exactly what makes the degreewise adjunction iso into a weak equivalence of the whole mapping spaces, not just a bijection on $\pi_0$.

> [!note]- Hint 4
> For the counterexample, look for an adjunction whose derived functors induce an equivalence on $\mathrm{Ho}$ but where a *derived unit or counit fails to be a weak equivalence* — for instance, comparing two model structures on the same category with the same homotopy category but different mapping spaces, or a functor that is essentially surjective and full+faithful on $\mathrm{Ho}$ yet does not lift to a Quillen equivalence.

---

# Solution

The proof computes the mapping space as a derived hom and transports it along the derived adjunction. Step 1 sets up framings. Step 2 transports degreewise. Step 3 upgrades to a space-level equivalence using the unit/counit condition. Step 4 gives the counterexample.

**Step 1: derived mapping spaces via framings.**

> [!note]- Derivation
> For $X \in \mathcal{M}$ choose a cofibrant cosimplicial framing $X^\bullet$ (a cosimplicial object with $X^0 = X^{\mathrm{cof}}$ and the latching maps cofibrations, modelling "$X \otimes \Delta^\bullet$"), and for $Y$ a fibrant replacement $Y^{\mathrm{fib}}$. The derived mapping space is
> $$\mathrm{Map}_{\mathcal{M}}(X,Y)_n \;=\; \mathcal{M}(X^n,\ Y^{\mathrm{fib}}),$$
> a simplicial set whose homotopy type is independent of the chosen framing and whose $\pi_0$ is $\mathrm{Ho}(\mathcal{M})(X,Y)$. The higher $\pi_n$ record homotopies and higher homotopies between maps $X \to Y$ — exactly the data the homotopy *category* discards.

**Step 2: transport along the derived adjunction degreewise.**

> [!note]- Derivation
> $F$ is left Quillen, so it preserves cofibrations and cofibrant objects; applying $F$ to the framing $X^\bullet$ yields a cosimplicial framing $F(X^\bullet)$ of $FX = \mathbb{L}FX$ (left Quillen functors preserve framings up to weak equivalence — this is a standard property, since framings are built from cofibrations and tensorings that $F$ respects). For each $n$, the Quillen adjunction gives a natural bijection
> $$\mathcal{N}(F(X^n),\ Y') \;\cong\; \mathcal{M}(X^n,\ G(Y'))$$
> for fibrant $Y'$. Taking $Y' = (\mathbb{L}FY)^{\mathrm{fib}}$ and assembling over $n$ produces a map of simplicial sets
> $$\mathrm{Map}_{\mathcal{M}}(X, GY') \;\xrightarrow{\ \cong\ }\; \mathrm{Map}_{\mathcal{N}}(\mathbb{L}FX,\ Y').$$

**Step 3: upgrade to an equivalence of spaces using the unit/counit condition.**

> [!note]- Derivation
> The map in Step 2 relates $\mathrm{Map}_{\mathcal{M}}(X, \mathbb{R}G\,Y')$ to $\mathrm{Map}_{\mathcal{N}}(\mathbb{L}FX, Y')$. Setting $Y' = \mathbb{L}FY$ (fibrantly replaced), the derived unit $\eta_Y : Y \to \mathbb{R}G\mathbb{L}FY$ is a **weak equivalence** — this is precisely the Quillen-*equivalence* hypothesis. Since $\mathrm{Map}_{\mathcal{M}}(X,-)$ sends weak equivalences between fibrant objects to weak equivalences of spaces, $\eta_Y$ induces
> $$\mathrm{Map}_{\mathcal{M}}(X, Y) \;\xrightarrow{\ \simeq\ }\; \mathrm{Map}_{\mathcal{M}}(X, \mathbb{R}G\mathbb{L}FY) \;\xrightarrow[\ \cong\ ]{\text{Step 2}}\; \mathrm{Map}_{\mathcal{N}}(\mathbb{L}FX, \mathbb{L}FY),$$
> a weak equivalence of the *whole* derived mapping spaces. So a Quillen equivalence preserves derived mapping spaces, including all higher $\pi_n$ — not just $\pi_0$. This is exactly "the two models carry the same homotopy theory": the $(\infty,1)$-categories they present are equivalent because they have equivalent objects (homotopy categories agree) *and* equivalent mapping spaces.

**Step 4: a homotopy-category equivalence that is not a Quillen equivalence.**

> [!note]- Derivation
> The two notions genuinely differ. Consider two model structures on the *same* underlying category with the *same* weak equivalences but different cofibrations/fibrations, related by the identity adjunction $\mathrm{id} \dashv \mathrm{id}$; these have identical homotopy categories (same weak equivalences), so the identity induces an equivalence of $\mathrm{Ho}$. But if the framings differ, the derived mapping spaces can differ in higher $\pi_n$, and the identity need not be a Quillen equivalence in the strong sense unless the structures are Quillen equivalent. More pointedly: there exist functors between model categories inducing an equivalence on homotopy categories (essentially surjective, and bijective on $\mathrm{Ho}$-hom-sets) whose derived unit fails to be a weak equivalence on mapping spaces — the classic caution is that an equivalence of homotopy categories detects only $\pi_0$ of mapping spaces, so two model categories can have equivalent $\mathrm{Ho}$ while presenting *different* $(\infty,1)$-categories (different mapping-space higher homotopy). This is why the comparison theorem insists on *Quillen* equivalences, not mere equivalences of homotopy categories.

> [!note]- Complete formal solution
> Let $F\dashv G$ be a Quillen equivalence.
>
> **(1)** Compute $\mathrm{Map}_{\mathcal{M}}(X,Y)_n = \mathcal{M}(X^n, Y^{\mathrm{fib}})$ via a cofibrant cosimplicial framing $X^\bullet$ and fibrant $Y^{\mathrm{fib}}$; $\pi_0 = \mathrm{Ho}(\mathcal{M})(X,Y)$, higher $\pi_n$ encode higher homotopies.
>
> **(2)** $F$ left Quillen preserves the framing: $F(X^\bullet)$ frames $\mathbb{L}FX$. The Quillen adjunction gives degreewise $\mathcal{N}(F(X^n),Y')\cong\mathcal{M}(X^n,GY')$, hence $\mathrm{Map}_{\mathcal{M}}(X,\mathbb{R}GY')\cong\mathrm{Map}_{\mathcal{N}}(\mathbb{L}FX,Y')$.
>
> **(3)** With $Y'=\mathbb{L}FY$, the derived unit $\eta_Y:Y\to\mathbb{R}G\mathbb{L}FY$ is a weak equivalence (Quillen-equivalence hypothesis), and $\mathrm{Map}_{\mathcal{M}}(X,-)$ preserves it; composing gives $\mathrm{Map}_{\mathcal{M}}(X,Y)\simeq\mathrm{Map}_{\mathcal{N}}(\mathbb{L}FX,\mathbb{L}FY)$, a space-level equivalence.
>
> **(4)** Counterexample: an equivalence of homotopy categories sees only $\pi_0$ of mapping spaces; two model categories can have equivalent $\mathrm{Ho}$ but inequivalent higher mapping-space homotopy, hence present different $(\infty,1)$-categories. Thus Quillen equivalence is strictly stronger, which is why the comparison theorem requires it. $\blacksquare$

---

# Key Takeaways

**"Same homotopy theory" means same mapping spaces, not same homotopy category.** This is the precise content of why the comparison theorem demands *Quillen* equivalences and the most important distinction in the chapter's machinery. The homotopy category records only $\pi_0$ of each mapping space — the *set* of maps up to homotopy — and discards all the higher homotopies between maps. An $(\infty,1)$-category is exactly the data of objects *plus the full mapping spaces*, so two presentations model the same $(\infty,1)$-category only if they have equivalent mapping spaces in every degree. A Quillen equivalence guarantees this; a mere equivalence of homotopy categories does not. The trigger is "are these two models the same?", and the reaction is "check the derived mapping spaces agree, not just the homotopy categories — demand a Quillen equivalence".

**The derived unit/counit condition is where the higher homotopies are controlled.** Notice that the upgrade from "$\pi_0$ agrees" to "the whole space agrees" used *exactly* the extra clause of the Quillen-equivalence definition — the derived unit being a weak equivalence. This is a reusable diagnostic: whenever you need to preserve more than $\pi_0$, the lever is the unit/counit being equivalences, because that is what makes an adjunction iso hold at the full spectral level rather than only after applying $\pi_0$. The same mechanism underlies "fully faithful at the $\infty$-level" and the recognition criteria for equivalences of $\infty$-categories. When a proof only gives you $\pi_0$, go back and check whether the unit/counit is a genuine weak equivalence — that is usually the missing strength.

**Computing mapping spaces requires resolutions (framings), and left Quillen functors respect them.** The technical engine is that the derived mapping space is not the naive hom but a *derived* hom, computed via a cosimplicial framing or simplicial resolution, and that a left Quillen functor preserves these resolutions because it preserves cofibrations. This is the same pattern as computing derived functors ($\mathrm{Tor}$, $\mathrm{Ext}$, derived tensor) by resolving and then applying the functor: the resolution is what makes the derived object homotopy-invariant, and the (left/right) Quillen functor is what makes the resolution transport correctly. Recognising "to get the derived mapping space, frame and then apply" — and "left Quillen functors commute with framing up to weak equivalence" — is the reusable skill that makes every comparison computation in §3 go through.
