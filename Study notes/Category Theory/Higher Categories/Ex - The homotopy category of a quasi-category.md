---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Quasi-Category"
  - "Thm - The Homotopy Category of a Quasi-Category"
  - "Def - Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{D}$ be a [[Def - Quasi-Category|quasi-category]]. Verify in detail that its [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] $\mathrm{ho}(\mathcal{D})$ is a well-defined [[Def - Category|category]]:

1. **Homotopy** of parallel $1$-simplices ($f\simeq g$ via a $2$-simplex with $d_0=\mathrm{id}$, $d_1=g$, $d_2=f$) is an **equivalence relation**.
2. **Composition** $[g]\circ[f]:=[d_1\sigma]$, defined by filling the inner horn $(f,g)$ to a $2$-simplex $\sigma$, is **independent of the chosen filler** and of the representatives.
3. **Associativity** holds, via an inner $3$-horn filler.

Conclude that $\mathrm{ho}(\mathcal{D})$ is a category with objects $\mathcal{D}_0$ and morphisms the homotopy classes of $1$-simplices.

**Recall:**

![[Thm - The Homotopy Category of a Quasi-Category#Statement]]

In a [[Def - Quasi-Category|quasi-category]], inner horns fill (not uniquely). Two parallel edges $f,g:x\to y$ are *homotopic* if a $2$-simplex $\sigma$ has $d_2\sigma=f$, $d_1\sigma=g$, $d_0\sigma=\mathrm{id}_y=s_0 y$. A $2$-simplex with $d_2=f$, $d_0=g$ exhibits $d_1$ as a composite of $f$ and $g$.

---

# Convergent Strategy

**Problem class:** This is a "well-definedness of a quotient construction" problem — verifying that the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] really is a category, the "fill"/"compose" target of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to construct the right inner horns whose fillers witness the needed equalities-up-to-homotopy.

**Assumption pattern:** The recognisable feature is that composition is defined by a *choice* (a filler), so the danger is dependence on the choice. The assumption that saves us is the *inner*-horn-filling axiom in *all* dimensions: the higher fillers are exactly the homotopies that make the choice immaterial.

**Theorem routing:** The route is repeated application of inner-horn filling: $\Lambda^2_1$ for existence of composites, $\Lambda^3_1$ (or $\Lambda^3_2$) for independence of the filler and for transitivity of homotopy, $\Lambda^4_\bullet$ for associativity. Degenerate $2$-simplices supply reflexivity and units.

**Key decision point:** The non-obvious choice is the *assembly of the correct inner $3$-horn* whose filler witnesses that two composites are homotopic. One must choose which three of the four faces of $\Delta^3$ to prescribe (two genuine triangles plus a degeneracy), so that the horn is *inner* (fillable) and the missing face is the homotopy sought. Picking an outer horn here would be unfillable; picking the wrong faces gives the wrong conclusion.

---

# Legal Operations Used

1. **Operation 3 (translate horn-filling into composites).** Fill $\Lambda^2_1$ for composition; fill $\Lambda^3_\bullet$ for the homotopies witnessing well-definedness and associativity.

2. **Operation 8 (pass to the homotopy category).** This exercise *is* the construction of $\mathrm{ho}(\mathcal{D})$, verifying it satisfies the category axioms.

---

# Hints

> [!note]- Hint 1
> Reflexivity of $\simeq$: find a *degenerate* $2$-simplex on $f$ with the right faces. ($s_1 f$ has $d_2 = f$, $d_1 = f$, $d_0 = \mathrm{id}$.) Symmetry and transitivity: build inner horns from the given homotopy $2$-simplices and fill.

> [!note]- Hint 2
> For composition's independence of the filler: given two fillers $\sigma,\sigma'$ of the same horn $(f,g)$, with long edges $h,h'$, assemble a $3$-simplex with faces $\sigma$, $\sigma'$, and a degeneracy, forming an *inner* $\Lambda^3_1$. Its filler's remaining face is a homotopy $h\simeq h'$.

> [!note]- Hint 3
> Associativity: three composable edges $f,g,h$ give two bracketings of the triple composite, each a face of a $3$-simplex; assemble an inner $\Lambda^3_\bullet$ (or $\Lambda^4$) whose filler exhibits the two bracketings as homotopic.

---

# Solution

The plan: Step 1 establishes that homotopy is an equivalence relation. Step 2 defines composition and proves it independent of the filler and representatives. Step 3 handles units. Step 4 proves associativity. Together these are the category axioms.

**Step 1: Homotopy is an equivalence relation.** $\simeq$ on parallel edges is reflexive (degenerate $2$-simplex), symmetric, and transitive (inner-horn fillers).

> [!note]- Derivation
> *Reflexive:* the degenerate $2$-simplex $s_1 f$ has $d_2 = f$, $d_1 = f$, $d_0 = s_0 y = \mathrm{id}_y$, witnessing $f\simeq f$.
> *Symmetric and transitive:* given homotopies $f\simeq g$ and $g\simeq k$ as $2$-simplices, build an inner $3$-horn $\Lambda^3_1$ whose prescribed faces are these two homotopy-triangles together with a degeneracy on $\mathrm{id}_y$; filling it (quasi-category axiom) yields a $3$-simplex whose remaining face is a $2$-simplex witnessing $f\simeq k$ (transitivity). Symmetry is the special case $k = f$ using the reflexive witness, run through the same construction. Hence $\simeq$ is an equivalence relation on each set of parallel edges, and $\mathrm{ho}(\mathcal{D})(x,y) := \{x\to y\}/\simeq$ is well-defined.

**Step 2: Composition is well-defined.** Fill $\Lambda^2_1$ to define $[g]\circ[f] = [d_1\sigma]$; independence of the filler and representatives follows from an inner $\Lambda^3_1$ filler.

> [!note]- Derivation
> *Existence:* given $f:x\to y$, $g:y\to z$, the inner horn $\Lambda^2_1\to\mathcal{D}$ with $d_2 = f$, $d_0 = g$ has a filler $\sigma$; set $[g]\circ[f] := [d_1\sigma]$.
> *Independence of filler:* let $\sigma,\sigma'$ be two fillers of the same horn, with $h = d_1\sigma$, $h' = d_1\sigma'$. Consider a $3$-simplex whose faces are prescribed as $d_3 = \sigma$, with $d_2$ a degenerate triangle on $g$, and $d_0 = \sigma'$, with $d_1$ free — this is an inner horn $\Lambda^3_1$. Filling it gives a $3$-simplex whose face $d_1$ is a $2$-simplex with edges $h$, $h'$, $\mathrm{id}$, i.e. a homotopy $h\simeq h'$. So $[d_1\sigma] = [d_1\sigma']$: the composite class is independent of the filler.
> *Independence of representatives:* if $f\simeq f'$ and $g\simeq g'$, insert the homotopy-triangles into a $3$-horn alongside the composing triangles and fill; the resulting homotopy shows the composite class is unchanged. Hence $\circ$ is well-defined on homotopy classes.

**Step 3: Units.** $[\mathrm{id}_x] = [s_0 x]$ is a two-sided unit.

> [!note]- Derivation
> The degenerate $2$-simplex $s_1 f$ exhibits $f$ as a composite $f\circ\mathrm{id}_x$ (its faces are $d_2 = \mathrm{id}_x$... more precisely a suitable degeneracy realises $[f]\circ[\mathrm{id}_x] = [f]$), and $s_0 f$ realises $[\mathrm{id}_y]\circ[f] = [f]$. Concretely, the degenerate simplices provide canonical fillers of the horns $(\mathrm{id}_x, f)$ and $(f, \mathrm{id}_y)$ whose long edge is $f$ itself, so composing with an identity class returns the original class. Thus $[\mathrm{id}_x]$ and $[\mathrm{id}_y]$ are two-sided units.

**Step 4: Associativity.** $([h]\circ[g])\circ[f] = [h]\circ([g]\circ[f])$ via an inner higher-horn filler.

> [!note]- Derivation
> Given $w\xrightarrow{f}x\xrightarrow{g}y\xrightarrow{h}z$, choose fillers realising $gf$, $hg$, and the two bracketings. These $2$-simplices are the faces of a $3$-simplex; assembling them into an inner $3$-horn $\Lambda^3_1$ (or $\Lambda^3_2$) and filling it produces a $3$-simplex whose faces force the two long edges — the value of $(h\circ g)\circ f$ and of $h\circ(g\circ f)$ — to be homotopic. (Equivalently, an inner $\Lambda^4_\bullet$ filler handles all the compatibilities at once.) Hence the two bracketings define the same morphism in $\mathrm{ho}(\mathcal{D})$, so composition is associative.

> [!note]- Complete formal solution
> Let $\mathcal{D}$ be a quasi-category. Define $\mathrm{ho}(\mathcal{D})$ with objects $\mathcal{D}_0$ and morphisms $\mathrm{ho}(\mathcal{D})(x,y) = \{1\text{-simplices } x\to y\}/\simeq$.
>
> - *Equivalence relation (Step 1):* reflexivity from $s_1 f$; symmetry and transitivity from inner $\Lambda^3_1$ fillers. So homotopy classes are well-defined.
> - *Composition (Step 2):* $[g]\circ[f] := [d_1\sigma]$ for a filler $\sigma$ of the inner horn $(f,g)$; independence of $\sigma$ and of the representatives follows from inner $\Lambda^3_1$ fillers exhibiting any two composites as homotopic.
> - *Units (Step 3):* $[\mathrm{id}_x] = [s_0 x]$ is a two-sided unit, via degenerate $2$-simplices.
> - *Associativity (Step 4):* the two bracketings of a triple composite are exhibited as homotopic by an inner higher-horn filler.
>
> All category axioms hold, so $\mathrm{ho}(\mathcal{D})$ is a category. $\quad\blacksquare$

---

# Key Takeaways

**The higher inner fillers are precisely the homotopies that make composition well-defined — this is the mechanism, not a side remark.** Composition in a quasi-category is defined by *choosing* a filler, and the entire worry is dependence on the choice. The resolution is structural: any two choices are exhibited as homotopic by filling an inner $3$-horn assembled from them. So the non-uniqueness of composites (the defining feature of $\infty$-categories) and the well-definedness of composition *up to homotopy* are two sides of one coin — the higher fillers supply exactly the coherence that uniqueness would have given for free. The reusable insight: in any homotopy-coherent construction, "well-defined up to homotopy" means "the choices are connected by the next layer of cells".

**Assembling the correct inner horn is the whole skill — and it must be inner.** The technical heart of every step is building a horn whose filler witnesses the needed homotopy, and getting two things right: the horn must be *inner* (so the quasi-category axiom applies and a filler exists), and its missing face must be the homotopy you want. This is a recurring move in simplicial homotopy theory — for transitivity, well-definedness, associativity, one constructs a higher simplex with prescribed faces and reads the conclusion off the free face. The diagnostic: when you need "$A$ is homotopic to $B$", look for a higher simplex two of whose faces are $A$ and $B$ (plus degeneracies), arranged so the horn is inner.

**Passing to $\mathrm{ho}(\mathcal{D})$ restores ordinary-categorical intuition, and is the safety rail of the subject.** Once well-definedness is established, $\mathrm{ho}(\mathcal{D})$ is a genuine category where composites are unique and you may reason as usual — losing the higher structure but keeping a faithful $1$-dimensional shadow. This is how one extracts computable invariants (the [[Def - Path-Product and the Fundamental Group|fundamental group]] from $\mathrm{Sing}\,X$, the triangulated structure from a stable $\infty$-category). The trigger to remember: when the higher structure is more than the problem needs, pass to $\mathrm{ho}$ — and this exercise is the guarantee that doing so always lands you in a legitimate category.
