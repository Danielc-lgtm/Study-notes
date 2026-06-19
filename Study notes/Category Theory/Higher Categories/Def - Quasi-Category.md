---
type: definition
subject: higher-categories
prereqs:
  - "Def - Simplicial Set"
  - "Def - Kan Complex and the Nerve"
  - "Def - Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathcal{D}$ denotes a [[Def - Simplicial Set|simplicial set]] that is a quasi-category. Its $0$-simplices $\mathcal{D}_0$ are called **objects**, its $1$-simplices $\mathcal{D}_1$ are called **morphisms** (an edge $\sigma$ has source $d_1\sigma$ and target $d_0\sigma$), and a $2$-simplex $\tau$ has faces $d_0\tau, d_1\tau, d_2\tau$ which are edges. The **inner horns** are $\Lambda^n_i \hookrightarrow \Delta^n$ with $0 < i < n$; a **filler** of $\Lambda^n_i \to \mathcal{D}$ is an extension to $\Delta^n \to \mathcal{D}$. We write $f : x \to y$ for a $1$-simplex with $d_1 f = x$, $d_0 f = y$, and $\mathrm{id}_x = s_0 x$ for the degenerate edge on a vertex. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Axiom Motivation

The motivation is the whole point of the chapter, so let us take it slowly. We want a notion of category in which "the morphisms between two objects form a *space*, not a set" — so that there are morphisms between morphisms, homotopies between those, and so on without end. The naive approach, "a category enriched in spaces", works (it gives a simplicial or topological category) but is unpleasant: composition in such a thing is strictly associative, which forces awkward fibrant-replacement gymnastics every time you build one, because the natural composition of, say, *paths* in a space is not strictly associative. We want a definition where the non-strictness is built in from the start, so that nothing ever has to be rigidified.

The decisive idea, due to Boardman and Vogt, is to *not encode composition as an operation at all*. Recall from [[Def - Kan Complex and the Nerve]] the translation: a map from the inner horn $\Lambda^2_1$ into a simplicial set is a pair of composable edges $x \xrightarrow{f} y \xrightarrow{g} z$, and a filler — an extension to the solid triangle $\Delta^2$ — supplies a long edge $h : x \to z$ together with a $2$-simplex witnessing "$h$ is a composite of $f$ and $g$". In the nerve of an ordinary category, this filler is *unique*: there is exactly one composite. The single, surgical move that creates $\infty$-category theory is to **drop the uniqueness** and keep only existence:

> A quasi-category is a simplicial set in which every inner horn has a filler — possibly many.

That is the entire definition. And it is exactly the right relaxation, for three reasons. First, it makes composition *exist* — you can always find a composite of two composable morphisms — so the structure deserves the name "category". Second, it makes composition *non-unique*, which is honest: the composite of two paths in a space is genuinely not a single path, but any of a contractible family. Third, the higher fillers control the ambiguity coherently. If $h_1$ and $h_2$ are two composites of the same $f$ and $g$, you can assemble a horn $\Lambda^3_1$ whose filler exhibits a homotopy $h_1 \simeq h_2$; if there are two such homotopies, a $\Lambda^4$-filler identifies *them*; and so on up every dimension. The inner-horn condition, applied in all dimensions at once, says that the space of composites is *contractible* — there is essentially one composite, but only up to coherent higher homotopy. This is why uniqueness can be safely dropped: the higher cells restore it in the only sense that survives homotopy.

Now, why *inner* horns and not all horns? Filling outer horns ($\Lambda^n_0$, $\Lambda^n_n$) is the geometric form of inverting morphisms, as explained on [[Def - Kan Complex and the Nerve]]: filling $\Lambda^2_0$ given $f : x \to y$ and $h : x \to z$ amounts to solving $h = ? \circ f$, which needs $f$ invertible. A general category has non-invertible morphisms, and we want $\infty$-categories to generalise *categories*, not just groupoids — so we must *not* demand outer fillers. Demanding only inner fillers leaves non-invertible morphisms intact; demanding all fillers (the [[Def - Kan Complex and the Nerve|Kan condition]]) forces everything invertible and gives an $\infty$-*groupoid*. The inner/outer line is exactly the $\infty$-category / $\infty$-groupoid line.

What if we kept uniqueness of inner fillers? Then by the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]] we would be back to ordinary categories — no higher structure, no spaces of morphisms. What if we dropped inner fillers too? Then composition would not even exist, and the structure would be a mere simplicial set with no categorical content. The quasi-category sits at precisely the productive point: inner fillers exist (composition works), they are not unique (homotopy lives), and outer fillers are not required (non-invertible morphisms allowed).

---

# The Definition

A **quasi-category** (equivalently **weak Kan complex**, or **$\infty$-category** in the sense of Joyal and Lurie) is a [[Def - Simplicial Set|simplicial set]] $\mathcal{D}$ satisfying the **inner horn condition**: for every $n \ge 2$ and every $0 < i < n$, each map of simplicial sets $\Lambda^n_i \to \mathcal{D}$ extends along the inclusion $\Lambda^n_i \hookrightarrow \Delta^n$ to a map $\Delta^n \to \mathcal{D}$,
$$
\begin{array}{ccc}
\Lambda^n_i & \xrightarrow{\;f\;} & \mathcal{D} \\
\big\downarrow & \nearrow_{\;\bar f} & \\
\Delta^n & &
\end{array}
\qquad (0 < i < n),
$$
where the lift $\bar f$ is *not* required to be unique. A **functor of $\infty$-categories** $\mathcal{C} \to \mathcal{D}$ is simply a map of simplicial sets.

The simplices acquire categorical names:
- the **objects** of $\mathcal{D}$ are the $0$-simplices $\mathcal{D}_0$;
- the **morphisms** are the $1$-simplices $\mathcal{D}_1$; a morphism $f$ has source $d_1 f$ and target $d_0 f$, and the identity of an object $x$ is the degenerate edge $\mathrm{id}_x = s_0 x : x \to x$;
- a **$2$-simplex** $\tau$ with $d_2\tau = f : x \to y$, $d_0\tau = g : y \to z$, $d_1\tau = h : x \to z$ **exhibits $h$ as a composite** $g \circ f$ (drawn as a commuting triangle with edges $f, g$ and long edge $h$);
- two parallel morphisms $f, g : x \to y$ are **homotopic**, written $f \simeq g$, when there is a $2$-simplex $\tau$ with $d_0\tau = \mathrm{id}_y$, $d_1\tau = g$, $d_2\tau = f$ (so $\tau$ witnesses $g = \mathrm{id}_y \circ f$).

By the inner-horn condition, composites exist (fill $\Lambda^2_1$); they are unique up to homotopy (fill $\Lambda^3_1$ or $\Lambda^3_2$); and homotopy is an equivalence relation on each $\mathcal{D}(x,y)$.

---

# Categorical / Structural Definition

The definition *is* the structural one: a quasi-category is an object of $\mathbf{sSet}$ satisfying a right-lifting property, namely against the **inner** horn inclusions only. This places quasi-categories precisely between two familiar classes:

$$
\underbrace{\text{unique inner fillers}}_{\text{nerves} = \mathbf{Cat}}
\;\subsetneq\;
\underbrace{\text{some inner fillers}}_{\text{quasi-categories} = \infty\text{-}\mathbf{Cat}}
\;\supsetneq\;
\underbrace{\text{all fillers}}_{\text{Kan complexes} = \infty\text{-}\mathbf{Grpd}}.
$$

The fully-faithful [[Def - Kan Complex and the Nerve|nerve]] $N : \mathbf{Cat} \to \mathbf{sSet}$ exhibits ordinary categories as the quasi-categories with *unique* inner fillers, and [[Thm - The Homotopy Category of a Quasi-Category|the homotopy category]] $\mathrm{ho} : \{\text{quasi-categories}\} \to \mathbf{Cat}$ is a one-sided inverse: $\mathrm{ho}(N(\mathcal{C})) \cong \mathcal{C}$. In Lurie's framework, $\infty\text{-}\mathbf{Cat}$ is itself organised into a quasi-category (via the simplicial nerve of the simplicial category of quasi-categories), so the theory is self-supporting in the same way $\mathbf{Cat}$ is a $2$-category. The structural payoff is that *every* concept of ordinary category theory — [[Def - Functor|functor]], [[Def - Natural Transformation|natural transformation]], [[Def - Adjunction|adjunction]], limit, the [[Thm - The Yoneda Lemma|Yoneda lemma]] — has an $\infty$-categorical upgrade obtained by reinterpreting it in $\mathbf{sSet}$ with horn-filling standing in for composition.

---

# Relate to Other Fields / Compression

A quasi-category compresses to one sentence: **it is a category in which composition is defined only up to a contractible space of choices, encoded by the fillability of inner horns.** It is the model of an $\infty$-category in which everything is combinatorial — no topology, no strict enrichment, just sets of simplices and a lifting property.

**True name:** a quasi-category is "a simplicial set where you can compose (fill inner horns) but the composite is unique only up to homotopy." When you see "quasi-category" or "$\infty$-category", do not picture an enriched category with strict composition; picture $\mathrm{Sing}(X)$, where the composite of two paths is the contractible family of paths homotopic to their concatenation, with the $2$-simplex as witness.

The two foundational examples are the two ends of the chapter. From category theory, $N(\mathcal{C})$ is the quasi-category with unique fillers — ordinary categories sit inside $\infty$-categories. From topology, $\mathrm{Sing}(X)$ is the quasi-category (in fact Kan complex) of a space — spaces are $\infty$-groupoids. Every $\infty$-category interpolates: it has both non-invertible morphisms (like a category) and a genuine space of morphisms (like a space). This is why $\infty$-categories are the right setting for **derived algebraic geometry**, **stable homotopy theory**, and the homotopy-coherent algebra of §H.5: they are the common generalisation of "category" and "space".

---

# Examples / Corollaries

**Is an instance — the nerve $N(\mathcal{C})$.** Every [[Def - Kan Complex and the Nerve|nerve]] of an ordinary category is a quasi-category: inner horns fill, in fact uniquely (see [[Ex - The nerve of a category is a quasi-category]]). Here the composite of two morphisms is honestly unique, so $\mathrm{ho}(N(\mathcal{C})) \cong \mathcal{C}$ recovers the category on the nose. This is the case where the $\infty$-categorical structure adds nothing.

**Is an instance — the singular complex $\mathrm{Sing}(X)$.** For a [[Def - Topological Space|space]] $X$, $\mathrm{Sing}(X)$ is a [[Def - Kan Complex and the Nerve|Kan complex]], hence a quasi-category. Its objects are points, its morphisms are paths, and the composite of two paths is *any* path homotopic to their concatenation — non-unique, which is exactly why this is not a nerve. Its homotopy category is the fundamental groupoid; every morphism is invertible (paths can be reversed up to homotopy), so this is an $\infty$-groupoid.

**Is an instance — the $\infty$-category of spaces.** Let $\mathrm{Kan} \subseteq \mathbf{sSet}$ be the full subcategory of Kan complexes; it is enriched in simplicial sets, hence by the homotopy-coherent (Cordier) simplicial nerve it gives a quasi-category $\mathcal{S}$ whose objects are spaces and whose morphism spaces are the mapping Kan complexes. This is the home of homotopy theory done $\infty$-categorically — and the basic example of an $\infty$-category that is neither a nerve nor a single space.

**Is NOT a quasi-category — a simplicial set with an unfillable inner horn.** Take the boundary $\partial\Delta^2$ — the three edges of a triangle, *without* the interior $2$-simplex. The inner horn $\Lambda^2_1 \hookrightarrow \partial\Delta^2$ (the two edges $0 \to 1 \to 2$) has *no* filler in $\partial\Delta^2$, because the only $2$-simplices of $\partial\Delta^2$ are degenerate and there is no non-degenerate triangle to serve as the filler. So $\partial\Delta^2$ is *not* a quasi-category: it has composable morphisms with no composite. (It becomes one upon filling in the triangle, i.e. upon passing to $\Delta^2$.)

**Corollary — composites are unique up to homotopy.** If $h_1, h_2$ are both composites of $f$ and $g$ (each appears as the long edge $d_1$ of a $2$-simplex over the inner horn $(f,g)$), then filling a suitable inner $3$-horn produces a homotopy $h_1 \simeq h_2$. Hence "the composite" is well-defined as a homotopy class — which is exactly what makes [[Thm - The Homotopy Category of a Quasi-Category|the homotopy category]] a genuine category.

**Calibration check.** Verify that the identity edge $\mathrm{id}_x = s_0 x$ really is a two-sided unit up to homotopy, using a degenerate $2$-simplex. Confirm that a $2$-simplex with $d_0 = \mathrm{id}_y$, $d_2 = f$, $d_1 = g$ exhibits $f \simeq g$, and check that $\simeq$ is reflexive (use $s_0 f$) and symmetric (fill an inner horn). And confirm that the boundary $\partial\Delta^2$ fails the inner-horn condition while $\Delta^2$ satisfies it.

---

# Unlocked by This

> [!tip] The Homotopy Category and ∞-Categorical Limits *(from this chapter and beyond)*
> Every quasi-category $\mathcal{D}$ has a [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] $\mathrm{ho}(\mathcal{D})$, and the full apparatus of **∞-categorical limits and colimits** (terminal objects, pullbacks, totalisations) is defined by horn-like lifting conditions on $\mathcal{D}$, refining Chapter III to the homotopy-coherent world.

> [!tip] ∞-Topoi and Derived Algebraic Geometry *(from Lurie's Higher Topos Theory)*
> Presheaves of spaces on a quasi-category, with a Grothendieck topology, form an **∞-topos** — the setting for **derived algebraic geometry**, where schemes are upgraded so that intersection multiplicities and cotangent complexes become functorial. The quasi-category is the substrate on which all of this is built.

> [!tip] Stable ∞-Categories and the Derived Category *(from Higher Algebra)*
> Adding the axiom that the $\infty$-category is pointed with invertible suspension yields a **stable ∞-category**, whose homotopy category is [[Thm - The Homotopy Category of a Quasi-Category|triangulated]]. This is the coherent fix for the **derived category** discussed in §H.5 — the cone becomes functorial.
