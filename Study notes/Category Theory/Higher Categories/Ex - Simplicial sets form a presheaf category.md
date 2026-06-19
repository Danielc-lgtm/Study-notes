---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Simplicial Set"
  - "Def - Presheaf"
  - "Thm - Limits in Set and in Functor Categories"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that the category of [[Def - Simplicial Set|simplicial sets]] is a [[Def - Presheaf|presheaf]] category,
$$\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}],$$
and deduce that it is **complete and cocomplete**, with all limits and colimits computed **pointwise** (level by level). Spell out the pointwise formulas for the product $X\times Y$, the coproduct $X\sqcup Y$, and a pushout, and explain why this immediately gives the gluing constructions used throughout the chapter (subobjects, boundaries $\partial\Delta^n$, horns $\Lambda^n_i$, geometric realisation as a colimit).

**Recall:**

A [[Def - Simplicial Set|simplicial set]] is by definition a functor $X:\Delta^{op}\to\mathbf{Set}$, and a morphism is a natural transformation; so $\mathbf{sSet}$ *is* the [[Def - Presheaf|presheaf]] category $[\Delta^{op},\mathbf{Set}]$. The theorem [[Thm - Limits in Set and in Functor Categories]] states that $\mathbf{Set}$ is complete and cocomplete and that in any functor category $[\mathcal{C},\mathbf{Set}]$ limits and colimits exist and are computed objectwise (pointwise).

---

# Convergent Strategy

**Problem class:** This is a "recognise a presheaf category and inherit its (co)completeness" problem — an instance of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]] move "a simplicial set is defined by a universal property". The routine is to invoke the general theorem about functor categories and read off the pointwise formulas.

**Assumption pattern:** The recognisable feature is that $\mathbf{sSet}$ is *by definition* a functor category $[\Delta^{op},\mathbf{Set}]$. Once this is named, no special property of $\Delta$ is needed: every functor category into a complete-and-cocomplete category inherits those properties pointwise.

**Theorem routing:** The route is [[Thm - Limits in Set and in Functor Categories]]: $\mathbf{Set}$ is complete and cocomplete, and limits/colimits in $[\mathcal{C},\mathbf{Set}]$ are computed pointwise. Applying it with $\mathcal{C}=\Delta^{op}$ gives completeness and cocompleteness of $\mathbf{sSet}$ with level-wise formulas.

**Key decision point:** The non-obvious choice is realising there is *nothing special to prove about simplicial sets* — the result is a corollary of a general fact about presheaf categories, and the only content is writing out the pointwise formulas and connecting them to the chapter's gluing constructions. The temptation is to verify (co)completeness from scratch; the efficient route is to cite the general theorem.

---

# Legal Operations Used

1. **Operation 2 (compute via the universal property / presheaf structure).** We use that $\mathbf{sSet}=[\Delta^{op},\mathbf{Set}]$ to inherit limits and colimits pointwise.

---

# Hints

> [!note]- Hint 1
> What is the *definition* of a simplicial set? If it is literally a functor $\Delta^{op}\to\mathbf{Set}$, then $\mathbf{sSet}$ is a functor category, and you should look for a general theorem about functor categories.

> [!note]- Hint 2
> In any functor category $[\mathcal{C},\mathbf{Set}]$, a (co)limit is computed objectwise: $(\lim_i X^i)_n = \lim_i (X^i_n)$ and $(\mathrm{colim}_i X^i)_n = \mathrm{colim}_i (X^i_n)$, with structure maps induced. Apply with $\mathcal{C}=\Delta^{op}$.

> [!note]- Hint 3
> So $(X\times Y)_n = X_n\times Y_n$, $(X\sqcup Y)_n = X_n\sqcup Y_n$, and a pushout is the levelwise pushout of sets. The boundary $\partial\Delta^n$ and the horn $\Lambda^n_i$ are colimits (unions) of faces — hence they exist by cocompleteness.

---

# Solution

The plan: Step 1 identifies $\mathbf{sSet}$ as a presheaf category. Step 2 applies the general functor-category theorem to get (co)completeness with pointwise formulas. Step 3 writes the formulas for products, coproducts, pushouts. Step 4 connects to the chapter's gluing constructions.

**Step 1: $\mathbf{sSet}$ is a presheaf category.** By definition a [[Def - Simplicial Set|simplicial set]] is a functor $\Delta^{op}\to\mathbf{Set}$ and a morphism is a natural transformation, so $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$ is the [[Def - Presheaf|presheaf]] category on $\Delta$.

> [!note]- Derivation
> The definition of $\mathbf{sSet}$ — objects are functors $\Delta^{op}\to\mathbf{Set}$, morphisms are natural transformations — is exactly the definition of the functor (presheaf) category $[\Delta^{op},\mathbf{Set}]$. There is nothing to check; this is a renaming, and it is the whole point of defining a simplicial set as a presheaf rather than as raw face/degeneracy data.

**Step 2: Completeness and cocompleteness, pointwise.** Since $\mathbf{Set}$ is complete and cocomplete, [[Thm - Limits in Set and in Functor Categories]] gives that $[\Delta^{op},\mathbf{Set}]$ is complete and cocomplete with limits and colimits computed level by level.

> [!note]- Derivation
> [[Thm - Limits in Set and in Functor Categories]] states: $\mathbf{Set}$ has all small limits and colimits, and for any small category $\mathcal{C}$, the functor category $[\mathcal{C},\mathbf{Set}]$ has all small limits and colimits, computed *objectwise* — for a diagram $i\mapsto X^i$ of functors, $(\lim_i X^i)(c) = \lim_i (X^i(c))$ and $(\mathrm{colim}_i X^i)(c) = \mathrm{colim}_i (X^i(c))$, with the structure maps induced by those of the $X^i$. Taking $\mathcal{C}=\Delta^{op}$ and writing $X^i(c) = X^i_n$ for $c=[n]$, $\mathbf{sSet}$ is complete and cocomplete with all (co)limits computed *level by level* (in each simplicial degree $n$).

**Step 3: Pointwise formulas.** For simplicial sets $X,Y$: $(X\times Y)_n = X_n\times Y_n$; $(X\sqcup Y)_n = X_n\sqcup Y_n$; and for a span $X\leftarrow Z\to Y$, the pushout $P$ has $P_n = X_n\sqcup_{Z_n} Y_n$ (pushout of sets), all with the evident face and degeneracy maps.

> [!note]- Derivation
> Specialising Step 2:
> - *Product:* $(X\times Y)_n = X_n\times Y_n$, with $d_i(x,y) = (d_i x, d_i y)$ and likewise for degeneracies — the levelwise product of sets.
> - *Coproduct:* $(X\sqcup Y)_n = X_n\sqcup Y_n$ (disjoint union), structure maps acting on each summand.
> - *Pushout:* for $Z\to X$, $Z\to Y$, the pushout $X\sqcup_Z Y$ has $n$-simplices the set pushout $X_n\sqcup_{Z_n} Y_n$ (quotient of $X_n\sqcup Y_n$ identifying the images of $Z_n$), with induced structure maps.
> Each formula is the corresponding $\mathbf{Set}$-(co)limit applied in every degree, valid because (co)limits in $\mathbf{sSet}$ are pointwise.

**Step 4: The chapter's gluing constructions are (co)limits.** Subobjects, the boundary $\partial\Delta^n$, the horns $\Lambda^n_i$, and geometric realisation are all built by limits/colimits, hence exist by cocompleteness.

> [!note]- Derivation
> The boundary $\partial\Delta^n$ is the union (a colimit — coequalizer of the overlaps of faces) of the images of the $n+1$ face inclusions $\Delta^{n-1}\to\Delta^n$; the horn $\Lambda^n_i$ is the same union omitting the $i$th face. Both are subobjects of $\Delta^n$, computed as colimits, so they exist by cocompleteness of $\mathbf{sSet}$. Geometric realisation $|X| = \mathrm{colim}_{\Delta^n\to X}|\Delta^n|$ ([[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]) is a colimit in $\mathbf{Top}$ indexed by the simplices of $X$, and the fact that *every simplicial set is a colimit of representables* (the density/co-Yoneda formula $X=\mathrm{colim}_{\Delta^n\to X}\Delta^n$) is itself a cocompleteness statement. So all the constructions of §H.3–H.5 that "glue simplices" are licensed by this exercise.

> [!note]- Complete formal solution
> By definition $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$ is a [[Def - Presheaf|presheaf]] category (Step 1). Since $\mathbf{Set}$ is complete and cocomplete, [[Thm - Limits in Set and in Functor Categories]] gives that $[\Delta^{op},\mathbf{Set}]$ is complete and cocomplete with all (co)limits computed level by level (Step 2). Hence:
> $$(X\times Y)_n = X_n\times Y_n,\quad (X\sqcup Y)_n = X_n\sqcup Y_n,\quad (X\sqcup_Z Y)_n = X_n\sqcup_{Z_n} Y_n,$$
> and more generally any (co)limit is the degreewise $\mathbf{Set}$-(co)limit (Step 3). Consequently subobjects, $\partial\Delta^n$, the horns $\Lambda^n_i$, the density formula $X=\mathrm{colim}\,\Delta^n$, and geometric realisation all exist as (co)limits (Step 4). $\quad\blacksquare$

---

# Key Takeaways

**Presheaf categories inherit all (co)limits for free, computed pointwise — this is one of the most-used facts in category theory.** As soon as you recognise a category as $[\mathcal{C},\mathbf{Set}]$ (or $[\mathcal{C},\mathcal{D}]$ for $\mathcal{D}$ complete/cocomplete), you know it is complete and cocomplete and you can compute any limit or colimit object by object. Simplicial sets, presheaves on a space, $G$-sets, graphs, and quivers are all presheaf categories, and all inherit this. The reusable trigger: "is my category a functor category into $\mathbf{Set}$?" — if yes, completeness, cocompleteness, and pointwise formulas are immediate, and no construction needs to be built by hand.

**Defining simplicial sets as presheaves (not as raw face/degeneracy data) is what makes the theory frictionless.** Had we defined a simplicial set as "sets $X_n$ with maps $d_i, s_i$ satisfying the simplicial identities", we would have to verify (co)completeness directly. Defining it as a functor $\Delta^{op}\to\mathbf{Set}$ makes (co)completeness a one-line corollary and brings the entire presheaf toolkit — [[Def - The Yoneda Embedding|Yoneda]], the density formula, left Kan extension — to bear. The lesson generalises: when a structure has a "diagram of sets with relations" description, finding the small category whose presheaves it is converts hand-built constructions into automatic categorical ones.

**Every gluing in the chapter is a colimit, so cocompleteness is the silent engine behind boundaries, horns, and realisation.** The boundary $\partial\Delta^n$ and the horns $\Lambda^n_i$ are unions of faces — colimits — and they exist precisely because $\mathbf{sSet}$ is cocomplete. The density formula $X=\mathrm{colim}_{\Delta^n\to X}\Delta^n$ (every simplicial set is glued from standard simplices) is the cocompleteness statement that lets geometric realisation be *defined* as a colimit and forces it to be a left adjoint ([[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]). Whenever a construction in this chapter "builds a simplicial set by gluing simplices", it is a colimit, and this exercise is what guarantees the gluing is legitimate.
