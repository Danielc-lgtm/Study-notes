---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Quasi-Category"
  - "Thm - The Homotopy Category of a Quasi-Category"
  - "Def - Enriched Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

This is a motivational exercise. Explain, at a conceptual level, why the **derived category** $D^b(\mathrm{Coh}\,X)$ of coherent sheaves on a variety $X$ is *defective* as an ordinary (triangulated) category — specifically, why the **mapping cone** of a morphism of complexes is only well-defined *up to non-canonical isomorphism* and why functoriality fails at the level of the triangulated category — and explain how an **∞-categorical (or dg-) enhancement** repairs the defect by making mapping objects into *spaces* and the cone into a genuine [[Def - Functor|functor]]. State the categorical principle: *an ∞-categorical enhancement repairs the non-functoriality of triangulated/derived categories*, and say why it is illuminating.

> [!note]- Algebraic geometry background
> A **commutative ring** $R$ is a set with $+$ and $\times$ (commutative, associative, distributive, with $0$ and $1$). The basic example is a polynomial ring $k[x_1,\dots,x_n]$ over a field $k$. An **affine variety** is the common zero set in $k^n$ of a collection of polynomials — e.g. the parabola $\{y = x^2\}\subset k^2$ — and its **coordinate ring** is $k[x_1,\dots,x_n]$ modulo the ideal of polynomials vanishing on it. A general **variety** (or **scheme**) is glued from affine pieces, just as a manifold is glued from open balls; think of it as a geometric space carrying, on each open piece, a ring of functions.
>
> A **sheaf** on $X$ is a rule assigning to each open set $U$ a set (or group, or module) $\mathcal{F}(U)$ of "sections" — think "functions of a certain type defined on $U$" — compatibly with restriction to smaller opens and with gluing of local data. A **coherent sheaf** is, locally on each affine piece $\mathrm{Spec}\,R$, the sheaf associated to a finitely generated $R$-module; the prototype is the sheaf of sections of a vector bundle (locally free), but coherent sheaves also include "singular" objects like the structure sheaf of a subvariety. The coherent sheaves on $X$ form an **abelian category** $\mathrm{Coh}\,X$: one can take kernels, cokernels, images, and direct sums of morphisms, and there is a good notion of exact sequence. This is the category whose **derived category** we discuss.

**Recall:**

A **chain complex** is a sequence $\cdots\to C^{n}\xrightarrow{d}C^{n+1}\xrightarrow{d}\cdots$ with $d^2 = 0$; a **morphism of complexes** is a degreewise map commuting with $d$; a **quasi-isomorphism** is a morphism inducing isomorphisms on cohomology. The **derived category** $D^b(\mathcal{A})$ of an abelian category $\mathcal{A}$ is obtained by formally inverting the quasi-isomorphisms. A **stable ∞-category** is an $\infty$-category (a [[Def - Quasi-Category|quasi-category]]) that is pointed with invertible suspension; its [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] is triangulated.

---

# Convergent Strategy

**Problem class:** This is a motivational / "why we need the machinery" exercise — the algebraic-geometry bridge of the topic page. There is no computation; the task is to articulate a structural defect and its $\infty$-categorical repair, in the spirit of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Bridges|Bridges]].

**Assumption pattern:** The recognisable feature is "a construction defined only up to non-canonical isomorphism" — the mapping cone. This is the classic symptom of having passed to a [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] *too early*, discarding the higher cells that would have made the construction canonical.

**Theorem routing:** The route is the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] perspective: the derived/triangulated category is $\mathrm{ho}$ of a stable $\infty$-category, and the defects are exactly the data $\mathrm{ho}$ forgets. The repair is to work in the $\infty$-category (or its dg-model, a [[Def - Enriched Category|category enriched]] in chain complexes) before truncating.

**Key decision point:** The non-obvious recognition is that the cone's non-functoriality is *not* a failure of the cone construction but a failure of the *target* category to remember enough — the cone *is* functorial in the $\infty$-category, and only becomes non-functorial after applying $\mathrm{ho}$, which collapses the contractible space of choices to a non-canonical point.

---

# Legal Operations Used

1. **Operation 8 (pass to the homotopy category).** The derived/triangulated category is $\mathrm{ho}$ of a stable $\infty$-category; the defects are what $\mathrm{ho}$ discards.

2. **Operation 1 (unwind an enriched definition).** The dg-enhancement is a category [[Def - Enriched Category|enriched]] in chain complexes, where mapping objects are complexes (hence "spaces") rather than mere sets.

---

# Hints

> [!note]- Hint 1
> The mapping cone $\mathrm{Cone}(f)$ of a chain map $f$ is built from a *choice* — and in the derived category, where quasi-isomorphisms are inverted, the choice is only pinned down up to a non-canonical isomorphism. What data, present at the chain level, is lost when you pass to cohomology classes of maps?

> [!note]- Hint 2
> The derived category's morphisms are *homotopy classes* of (roofs of) chain maps. So $D^b(\mathcal{A}) = \mathrm{ho}$ of something richer: the [[Def - Quasi-Category|∞-category]] (or dg-category) of complexes, whose mapping objects are whole complexes of maps, not just their $H^0$.

> [!note]- Hint 3
> In the $\infty$-category, the cone is a colimit (a pushout of $A\to B$ along $A\to 0$), and colimits are functorial. Truncating to $\mathrm{ho}$ collapses the contractible space of cones to a single object chosen non-canonically — losing functoriality. The repair is: don't truncate; work in the stable $\infty$-category.

---

# Solution

The plan: Step 1 describes the derived category and the cone. Step 2 locates the defect (non-canonical cone, non-functoriality) as a consequence of truncating to $\mathrm{ho}$. Step 3 describes the $\infty$-categorical / dg-enhancement and how it repairs the defect. Step 4 states the principle and why it illuminates.

**Step 1: The derived category and the mapping cone.** $D^b(\mathrm{Coh}\,X)$ is obtained from chain complexes of coherent sheaves by inverting quasi-isomorphisms; the mapping cone $\mathrm{Cone}(f)$ of a chain map $f:A\to B$ is the complex implementing "$B$ modulo the image of $A$" homotopically, fitting into a distinguished triangle $A\to B\to\mathrm{Cone}(f)\to A[1]$.

> [!note]- Derivation
> Coherent sheaves form an abelian category $\mathrm{Coh}\,X$ (AG-background callout). To do homological algebra — compute $\mathrm{Ext}$, $\mathrm{Tor}$, derived pushforwards — one passes to complexes and *inverts quasi-isomorphisms* (maps that are isomorphisms on cohomology), since complexes that compute the same cohomology should be identified. The result is the derived category $D^b(\mathrm{Coh}\,X)$. The mapping cone $\mathrm{Cone}(f)$ of $f:A\to B$ is the complex with $\mathrm{Cone}(f)^n = A^{n+1}\oplus B^n$ and a twisted differential; it is the homotopical "cokernel" of $f$, and the sequence $A\to B\to\mathrm{Cone}(f)\to A[1]$ is the basic **distinguished triangle**, the derived replacement for a short exact sequence.

**Step 2: The defect — the cone is non-canonical, functoriality fails.** In the triangulated $D^b$, $\mathrm{Cone}(f)$ is determined only *up to non-canonical isomorphism*, and there is no functorial way to choose it; this is the standard pathology of triangulated categories.

> [!note]- Derivation
> A morphism in $D^b$ is a *homotopy class* of roofs $A\xleftarrow{\sim}\tilde A\to B$ of chain maps — the higher structure (the actual homotopies, and homotopies between them) is discarded, only its $H^0$ retained. The cone construction at the chain level is functorial, but after inverting quasi-isomorphisms two issues arise. First, the cone is defined only up to (non-canonical) isomorphism: given $f$, any complex fitting in the triangle is "a" cone, and there is no canonical choice. Second, and worse, **the cone is not a functor on $D^b$**: a commuting square in $D^b$ (i.e. commuting up to homotopy) induces a map on cones, but *not canonically* — different fillers of the homotopy give different maps, and there is no consistent choice. This is the failure of functoriality of the cone, and it propagates: the octahedral axiom is a partial, axiomatic patch for compatibilities that *should* be theorems. The root cause is that $D^b = \mathrm{ho}(\text{something richer})$, and [[Thm - The Homotopy Category of a Quasi-Category|the homotopy-category functor]] $\mathrm{ho}$ discards exactly the higher cells that made the cone canonical.

**Step 3: The repair — the ∞-categorical / dg-enhancement.** Work in the **stable ∞-category** of complexes (equivalently the **dg-category**, a [[Def - Enriched Category|category enriched]] in chain complexes), where mapping objects are *spaces* (complexes) and the cone is a genuine functorial colimit.

> [!note]- Derivation
> Instead of truncating, retain the full homotopy-coherent structure. The complexes of coherent sheaves form a [[Def - Enriched Category|dg-category]] — enriched in chain complexes, so each $\mathrm{Hom}(A,B)$ is a *complex* of maps, not just its $H^0$. Its associated [[Def - Quasi-Category|∞-category]] (via the dg-nerve) is a **stable ∞-category** $\mathcal{D}(\mathrm{Coh}\,X)$, in which mapping objects are spaces (Kan complexes / mapping complexes) recording not only maps but homotopies between them and higher homotopies. In this $\infty$-category the cone is the **pushout** of the span $0\leftarrow A\xrightarrow{f}B$ — a colimit — and colimits in an $\infty$-category are *functorial and unique up to a contractible space of choices* (as in [[Ex - Inner horn fillers as composition|the contractibility of composites]]). So $\mathrm{Cone}(f)$ is a genuine functor of $f$, with the higher coherences automatic. Applying [[Thm - The Homotopy Category of a Quasi-Category|ho]] to this stable $\infty$-category recovers the triangulated $D^b(\mathrm{Coh}\,X)$ — but now as the *shadow* of a well-behaved object, with the triangulated structure (shift, distinguished triangles) inherited from the $\infty$-categorical (co)fibre sequences, and the octahedral axiom a *theorem* rather than an axiom.

**Step 4: The principle and why it illuminates.** *An ∞-categorical enhancement repairs the non-functoriality of triangulated/derived categories* by retaining the higher cells that $\mathrm{ho}$ discards, turning the cone from an up-to-non-canonical-isomorphism gadget into a functorial colimit.

> [!note]- Derivation
> The principle is that the defects of triangulated categories are *artifacts of premature truncation*. The derived category is $\mathrm{ho}$ of a stable $\infty$-category, and $\mathrm{ho}$ forgets the contractible spaces of choices that made constructions canonical; working in the $\infty$-category before truncating restores functoriality. This is illuminating for three reasons. First, it *explains* the pathologies — the non-canonical cone, the awkward octahedral axiom, the failure of the derived functor of a composite to be the composite of derived functors — as one phenomenon: lost higher cells. Second, it is *constructive* — derived algebraic geometry, derived intersection theory, and the functoriality of $Rf_*$, $Lf^*$, $\otimes^L$ all become clean in the $\infty$-categorical framework. Third, it *unifies* — the same enhancement repairs the derived category, the stable homotopy category, and the homotopy theory of spaces, all instances of "do not truncate; keep the $\infty$-structure". The whole chapter — enrichment (mapping objects are spaces), quasi-categories (composition up to coherent homotopy), the homotopy category (the lossy truncation) — is exactly the machinery this repair requires.

> [!note]- Complete formal solution
> The derived category $D^b(\mathrm{Coh}\,X)$ inverts quasi-isomorphisms of complexes of coherent sheaves (Step 1). As a triangulated category it is defective: the mapping cone is defined only up to non-canonical isomorphism and is *not* a functor, because $D^b = \mathrm{ho}$ of a richer object and [[Thm - The Homotopy Category of a Quasi-Category|ho]] discards the higher homotopies that pinned the cone down (Step 2). The repair is to work in the **stable ∞-category** (equivalently dg-category, [[Def - Enriched Category|enriched]] in complexes) of complexes, where mapping objects are spaces and the cone is the functorial pushout $0\leftarrow A\to B$ (Step 3). The principle: *an ∞-categorical enhancement repairs the non-functoriality of triangulated/derived categories* by retaining the cells $\mathrm{ho}$ forgets — illuminating because it diagnoses the pathologies as premature truncation and makes derived algebraic geometry functorial (Step 4). $\quad\blacksquare$

---

# Key Takeaways

**Triangulated categories are defective because they are homotopy categories — truncated too early.** The non-canonical cone, the clumsy octahedral axiom, the failure of cones to be functorial: every classical pathology of triangulated and derived categories is a symptom of having applied [[Thm - The Homotopy Category of a Quasi-Category|ho]] before doing the constructions, collapsing the contractible spaces of choices that made those constructions canonical. The reusable diagnostic: whenever a construction is "well-defined only up to non-canonical isomorphism", suspect that you are working in a homotopy category and that the canonical version lives one level up, in the $\infty$-category before truncation. The cure is almost never to patch the truncated category with more axioms; it is to refuse to truncate.

**Mapping objects should be *spaces*, and this is what enrichment in chain complexes / spectra delivers.** The dg- or $\infty$-categorical enhancement replaces the hom-*set* of the derived category by a hom-*complex* (or mapping space), recording maps, homotopies between maps, and homotopies between those. With mapping objects that are spaces, colimits like the cone are functorial and unique up to contractible choice — exactly the [[Def - Enriched Category|enrichment]] idea of §H.2 applied to homological algebra. The trigger: when a category's morphisms "really" come with homotopies (chain maps up to chain homotopy, continuous maps up to homotopy), the right object is enriched in spaces, and forcing it down to sets is what creates the defects.

**The whole chapter is the toolkit for this one repair — enrichment, quasi-categories, and the homotopy category fit together precisely here.** Enrichment (§H.2) makes mapping objects into spaces; quasi-categories (§H.4) encode composition up to coherent homotopy so that colimits like the cone are functorial; the homotopy category (the lossy truncation) is *exactly* the operation whose premature application caused the trouble. So the motivation for higher category theory is not abstract aesthetics but a concrete need: to do homological algebra, derived algebraic geometry, and stable homotopy theory *functorially*. The derived category of coherent sheaves is the canonical illustration — its defects are real, they obstruct working algebraic geometry, and the $\infty$-categorical enhancement (**derived algebraic geometry**, Lurie–Toën–Vezzosi) is what makes the subject go through.
