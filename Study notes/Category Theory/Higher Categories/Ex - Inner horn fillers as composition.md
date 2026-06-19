---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Quasi-Category"
  - "Def - Kan Complex and the Nerve"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Make precise the slogan "inner-horn fillers are composites".

1. Interpret an inner $2$-horn $\Lambda^2_1\to\mathcal{D}$ in a [[Def - Quasi-Category|quasi-category]] as a pair of composable morphisms, and its filler as a choice of composite.
2. Explain why, in a general quasi-category, the composite is *not* a single morphism but a **contractible space of choices**, and identify the role of the higher inner horns ($\Lambda^3_1$, $\Lambda^4$, …) in establishing contractibility.
3. Contrast with the [[Def - Kan Complex and the Nerve|nerve]] case (unique filler) and the [[Def - Singular Simplex|singular complex]] case ($\mathrm{Sing}(X)$, where the composite of two paths is the family of paths homotopic to their concatenation), explaining why "contractible space of composites" is the right notion of "well-defined up to homotopy".

**Recall:**

In a [[Def - Quasi-Category|quasi-category]], an inner $2$-horn $\Lambda^2_1$ is a pair of edges $x\xrightarrow{f}y\xrightarrow{g}z$, and a filler is a $2$-simplex whose long edge is *a* composite. The nerve has *unique* fillers ([[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]]); $\mathrm{Sing}(X)$ has [[Def - Singular Simplex|singular simplices]] $|\Delta^n|\to X$ as $n$-simplices.

---

# Convergent Strategy

**Problem class:** This is a "conceptual interpretation" exercise — translating the formal horn-filling axiom into the picture that makes $\infty$-categories intelligible, the central insight of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Insights|Insights]]. The routine is to read each piece of simplicial data as categorical/homotopical content.

**Assumption pattern:** The recognisable feature is the inner-horn axiom and the layering of horns across dimensions. The composite lives in dimension $2$; the *ambiguity* of the composite is controlled in dimensions $3$ and up. Recognising that "the space of fillers" is the object of interest — not any single filler — is the key shift.

**Theorem routing:** The route uses Legal Operation 3 (translate horn-filling into composites) at dimension $2$, then the higher fillers to argue the space of composites is contractible, and finally the contrast cases via the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]] (unique fillers) and the concrete $\mathrm{Sing}(X)$ picture.

**Key decision point:** The non-obvious choice is to stop looking for "the" composite and instead study the *space* of fillers. The insight is that the higher inner horns guarantee any two fillers are connected by a homotopy, those homotopies are connected, and so on — so the space of composites is contractible, which is the precise meaning of "essentially one composite, up to coherent homotopy".

---

# Legal Operations Used

1. **Operation 3 (translate horn-filling into composites).** Inner $2$-horn = composable pair; filler = composite.

2. **Operation 4 (apply the nerve characterisation).** Unique fillers (nerve) versus contractible-but-not-unique (general quasi-category) is the conceptual fork.

---

# Hints

> [!note]- Hint 1
> The horn $\Lambda^2_1$ has edges $d^2 = f:x\to y$ and $d^0 = g:y\to z$. A filler is a $2$-simplex; what is its third edge $d^1$, and what does the $2$-simplex assert about it?

> [!note]- Hint 2
> Two fillers $\sigma,\sigma'$ have long edges $h, h'$, both "composites of $f,g$". Are they equal? In general no — but an inner $3$-horn assembled from $\sigma,\sigma'$ has a filler exhibiting $h\simeq h'$. The next dimension identifies the identifications.

> [!note]- Hint 3
> In $\mathrm{Sing}(X)$, a composite of two paths $f,g$ is a path $h$ together with a $2$-simplex (a map of a triangle) showing $h$ is homotopic to the concatenation $g\cdot f$. There are many such $h$ (all homotopic), and the space of them is contractible — that is "well-defined up to homotopy".

---

# Solution

The plan: Step 1 reads the inner $2$-horn and its filler. Step 2 explains non-uniqueness and the role of higher horns in contractibility. Step 3 contrasts the nerve (unique) and $\mathrm{Sing}(X)$ (contractible family) cases.

**Step 1: Inner $2$-horn = composable pair; filler = composite.** $\Lambda^2_1\to\mathcal{D}$ is a pair $x\xrightarrow{f}y\xrightarrow{g}z$; a filler is a $2$-simplex $\sigma$ whose long edge $d_1\sigma = h$ is a composite, with $\sigma$ the witness "$h\simeq g\circ f$".

> [!note]- Derivation
> The inner horn $\Lambda^2_1$ consists of the two edges adjacent to vertex $1$: $d^2 = f$ ($x\to y$) and $d^0 = g$ ($y\to z$), omitting the long edge $d^1$ ($x\to z$) and the interior. A map $\Lambda^2_1\to\mathcal{D}$ is exactly this composable pair. A filler $\sigma:\Delta^2\to\mathcal{D}$ supplies the long edge $h := d_1\sigma:x\to z$ together with the solid triangle $\sigma$, which *is* the witness that $h$ is a composite of $f$ and $g$. So filling the inner $2$-horn is precisely "choose a composite, with a certificate".

**Step 2: The composite is a contractible space of choices.** Different fillers give different long edges $h,h'$; an inner $\Lambda^3_1$ filler exhibits $h\simeq h'$, an $\Lambda^4$ filler identifies the homotopies, and so on — so the space of fillers is contractible, not a point.

> [!note]- Derivation
> The quasi-category axiom guarantees a filler *exists* but not that it is unique, so there may be many $2$-simplices $\sigma,\sigma',\dots$ over the same horn, with long edges $h, h',\dots$. These are all "composites of $f,g$", and they are related: as in [[Ex - The homotopy category of a quasi-category|the homotopy-category construction]], assembling $\sigma,\sigma'$ into an inner $\Lambda^3_1$ and filling it produces a homotopy $h\simeq h'$. If there are two such homotopies, an inner $\Lambda^4_\bullet$ filler identifies *them*; and so on without end. The upshot is that the *space of fillers* of the inner $2$-horn — the simplicial set of all $2$-simplices over $(f,g)$ — is **contractible**: nonempty (existence), path-connected (any two long edges homotopic), simply connected (homotopies identified), and so on in every degree. So "the composite" is not a single morphism but a contractible space of morphisms, all canonically homotopic.

**Step 3: The two ends — nerve and singular complex.** In a [[Def - Kan Complex and the Nerve|nerve]] the space of fillers is a *point* (unique composite); in $\mathrm{Sing}(X)$ it is the contractible space of paths homotopic to the concatenation. "Contractible space of composites" is the correct meaning of "well-defined up to homotopy".

> [!note]- Derivation
> *Nerve:* by the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]], $N(\mathcal{C})$ has a *unique* inner filler, so the space of composites is a single point $\{g\circ f\}$ — composition is single-valued, the ordinary-categorical case. This is the degenerate end of the spectrum, where the contractible space is as small as possible.
> *Singular complex:* in $\mathrm{Sing}(X)$, a $1$-simplex is a path and a $2$-simplex is a map of the triangle $|\Delta^2|\to X$. Given paths $f$ (from $x$ to $y$) and $g$ (from $y$ to $z$), a filler is a path $h$ from $x$ to $z$ together with a triangle witnessing $h\simeq g\cdot f$ (the concatenation). There are *many* such $h$ — every path homotopic to $g\cdot f$ — and the space of fillers is the space of these, which is contractible (it deformation-retracts onto the concatenation up to reparametrisation). So "the composite of two paths" is genuinely not a single path; it is a contractible family, and the $2$-simplex is the witness. This is why "contractible space of composites" is exactly "well-defined up to coherent homotopy": there is essentially one answer, but only after accounting for all the homotopies, and no canonical representative without extra choices.

> [!note]- Complete formal solution
> An inner $2$-horn $\Lambda^2_1\to\mathcal{D}$ is a composable pair $x\xrightarrow{f}y\xrightarrow{g}z$; a filler is a $2$-simplex whose long edge $h = d_1\sigma$ is a composite, with $\sigma$ the witness $h\simeq g\circ f$ (Step 1). In a general quasi-category fillers are not unique: distinct fillers have homotopic long edges (inner $\Lambda^3_1$ filler), the homotopies are themselves identified ($\Lambda^4$ filler), etc., so the space of fillers is *contractible* rather than a point (Step 2). The nerve is the extreme case of a one-point space of fillers (unique composite); $\mathrm{Sing}(X)$ is the prototype of a genuinely contractible space of fillers — the paths homotopic to the concatenation $g\cdot f$ — and this is the precise content of "composition is well-defined up to homotopy" (Step 3). $\quad\blacksquare$

---

# Key Takeaways

**"The composite" in an $\infty$-category is a contractible space, not a point — and internalising this is what makes the subject click.** The naive instinct is to look for *the* composite of two morphisms, as in an ordinary category. In a quasi-category there is no such single thing; there is a contractible *space* of composites, with the inner $2$-horn filler being any one point of it and the higher fillers certifying contractibility. The reusable shift in perspective: stop asking "what is the composite?" and start asking "what is the space of composites, and is it contractible?". Contractibility is the homotopy-theoretic version of "unique", and it is the right invariant because it is preserved under homotopy equivalence while "unique on the nose" is not.

**The higher inner horns are the coherence: each dimension tames the ambiguity of the dimension below.** Dimension $2$ produces composites; dimension $3$ shows any two composites are homotopic; dimension $4$ shows any two such homotopies agree; and so on. This tower is exactly why the single uniform condition "inner horns fill in all dimensions" suffices to encode all of associativity and its infinite hierarchy of coherences at once — the great advantage of the simplicial model over hand-written associators ([[Thm - Strictification of Bicategories|which become impossible above dimension two]]). The trigger to remember: whenever a construction is "defined up to homotopy", expect an infinite tower of higher cells enforcing coherence, and expect simplicial horn-filling to be the clean way to package it.

**$\mathrm{Sing}(X)$ is the picture to carry for every $\infty$-category — composition of paths is the canonical example of non-unique-but-contractible composites.** Concatenation of paths is the original motivation: $(g\cdot f)$ is one composite, but any path homotopic to it is equally good, and the space of them is contractible. This is not a pathology to be fixed but the honest structure of spaces, and forcing a single strict composite (a chosen reparametrisation) destroys the homotopy type. The lesson, the bridge to §H.5 and to the **homotopy hypothesis**: $\infty$-categories are modelled by simplicial sets precisely because the simplicial machinery encodes "composite = contractible space of choices" automatically, which is exactly what spaces — and hence all of homotopy-coherent mathematics — require.
