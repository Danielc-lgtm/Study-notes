---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Limit and Colimit"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Functor"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{R}$ is a small category equipped with the extra Reedy data described below, and $\mathcal{M}$ is a [[Def - Model Category|model category]]. The **diagram category** $\mathcal{M}^{\mathcal{R}}$ has objects the [[Def - Functor|functors]] $X : \mathcal{R} \to \mathcal{M}$ and morphisms the natural transformations; we write $X_r := X(r)$ for the value of the diagram at an object $r \in \mathcal{R}$. The two distinguished subcategories are $\mathcal{R}^{+}$ (the **direct** part) and $\mathcal{R}^{-}$ (the **inverse** part), and $\deg : \mathrm{ob}(\mathcal{R}) \to \lambda$ is a **degree function** valued in some ordinal $\lambda$. For an object $r$ we write $L_r X$ for its **latching object** and $M_r X$ for its **matching object**; the **latching map** is $L_r X \to X_r$ and the **matching map** is $X_r \to M_r X$. The arrows $\rightarrowtail$, $\twoheadrightarrow$, $\xrightarrow{\sim}$ denote cofibrations, fibrations, and weak equivalences in $\mathcal{M}$. The full symbol registry is on [[Model Categories — Framings and Function Complexes]].

This is a compound page: it defines two interlocking notions — the **Reedy category** (a combinatorial structure on the indexing category $\mathcal{R}$) and the **Reedy model structure** (the model structure it induces on $\mathcal{M}^{\mathcal{R}}$) — because the second is the entire reason the first is worth isolating, and the model structure cannot even be stated without the latching/matching machinery that the Reedy data supplies.

---

# Axiom Motivation

The problem this definition solves is concrete and unavoidable: given a [[Def - Model Category|model category]] $\mathcal{M}$, how do you put a model structure on a category of $\mathcal{R}$-shaped diagrams $\mathcal{M}^{\mathcal{R}}$? You want to do homotopy theory not just with single objects but with whole diagrams — a cosimplicial object, a tower, a cube, a sequence of spaces — and to do that you need to know which maps of diagrams are the weak equivalences, the cofibrations, and the fibrations.

There is an obvious first guess, and it is worth seeing why it is not enough. Take the **projective** structure, where a map $X \to Y$ of diagrams is a weak equivalence or fibration if and only if each component $X_r \to Y_r$ is one in $\mathcal{M}$; or dually the **injective** structure, where weak equivalences and cofibrations are checked componentwise. Both exist for nice $\mathcal{M}$, but each is lopsided: the projective structure makes fibrations cheap and cofibrations expensive (they are not componentwise), the injective structure does the reverse, and crucially *neither* is easy to build by hand for a general $\mathcal{M}$ — they require $\mathcal{M}$ to be cofibrantly generated. The Reedy idea is to find a third structure, sitting between the two, that exists for *every* model category $\mathcal{M}$ and in which cofibrations and fibrations both have a clean, checkable description. The price is a restriction on $\mathcal{R}$: it must be a Reedy category.

So what must $\mathcal{R}$ look like? The guiding picture is the simplex category $\Delta$. There, every morphism factors uniquely as a surjection (a codegeneracy, lowering dimension) followed by — no, the other way: every order-preserving map factors as a surjection then an injection, but in terms of building objects up, the *injections raise degree* and the *surjections lower degree*. This is the structure we abstract. We ask for two wide subcategories: $\mathcal{R}^{+}$, the **direct** maps that strictly raise degree, and $\mathcal{R}^{-}$, the **inverse** maps that strictly lower degree, with a degree function $\deg$ assigning an ordinal to each object so that the two classes are recognizable. The decisive axiom is **unique factorization**: every morphism of $\mathcal{R}$ factors uniquely as a map in $\mathcal{R}^{-}$ followed by a map in $\mathcal{R}^{+}$. This is exactly the epi-mono factorization in $\Delta$, abstracted.

Why is unique factorization the load-bearing axiom? Because it is what makes the inductive construction of the model structure work. The idea is to build a map of diagrams one degree at a time: having defined everything in degrees below $n$, the data needed to extend to degree $n$ is governed by two objects. The **latching object** $L_r X$ is the colimit of $X$ over the direct maps *into* $r$ from strictly lower degree — it is "the part of $X_r$ already forced by the lower-degree data," the degenerate or built-from-below part. The **matching object** $M_r X$ is the limit of $X$ over the inverse maps *out of* $r$ to strictly lower degree — it is "the boundary data that $X_r$ must be compatible with." Unique factorization is precisely what guarantees these two constructions interact correctly: the direct maps and inverse maps do not interfere, so the latching colimit and matching limit can be taken independently, and the relative latching map $L_r X \to X_r$ and relative matching map $X_r \to M_r X$ carry exactly the new information in degree $r$.

Drop unique factorization and the whole scheme collapses. If a morphism could factor through low degree in two genuinely different ways, the latching object would not be well-defined as "everything forced from below," and the induction would either over- or under-count the degenerate part — you would be unable to define the relative latching map cleanly. Drop the requirement that $\mathcal{R}^{+}$ and $\mathcal{R}^{-}$ contain only degree-raising and degree-lowering maps respectively (and that only identities lie in both) and the induction has no base: there is no notion of "strictly lower degree" to recurse on, and the latching/matching objects could reference $X_r$ itself, making the definition circular. The degree function must be ordinal-valued (well-ordered) precisely so that transfinite induction terminates; with a non-well-ordered "degree" you could descend forever.

The final test: could a reader invent this? Yes — start from "I want to build maps of diagrams degree by degree," realize you need to separate the data that *raises* degree from the data that *constrains against lower* degree, demand that the two separations be unique and compatible (unique factorization), and impose a well-ordered degree so the induction runs. The latching and matching objects are then forced as "the colimit of the lower direct data" and "the limit of the lower inverse data," and the relative maps are the only sensible carriers of new information.

---

# The Definition

**Reedy category.** A **Reedy category** is a small category $\mathcal{R}$ together with:

1. a **degree function** $\deg : \mathrm{ob}(\mathcal{R}) \to \lambda$ to some ordinal $\lambda$ (often $\lambda = \omega$, so degrees are natural numbers);
2. two wide subcategories $\mathcal{R}^{+}$ (the **direct subcategory**) and $\mathcal{R}^{-}$ (the **inverse subcategory**), both containing all objects;

subject to the axioms:

- every non-identity morphism of $\mathcal{R}^{+}$ **strictly raises degree** ($\deg(\mathrm{source}) < \deg(\mathrm{target})$), and every non-identity morphism of $\mathcal{R}^{-}$ **strictly lowers degree**;
- (**unique factorization**) every morphism $\phi$ of $\mathcal{R}$ factors as $\phi = \phi^{+} \circ \phi^{-}$ with $\phi^{-} \in \mathcal{R}^{-}$ and $\phi^{+} \in \mathcal{R}^{+}$, and this factorization is *unique*.

It follows that $\mathcal{R}^{+} \cap \mathcal{R}^{-}$ consists of the identities only.

**Latching and matching objects.** Fix a [[Def - Functor|functor]] $X : \mathcal{R} \to \mathcal{M}$ and an object $r$ of degree $n$. The **latching category** $\partial(\mathcal{R}^{+} \!\downarrow r)$ has objects the non-identity maps $s \to r$ in $\mathcal{R}^{+}$ (so $\deg s < n$); the **latching object** is the colimit
$$L_r X \;=\; \operatorname*{colim}_{(s \to r) \in \partial(\mathcal{R}^{+}\downarrow r)} X_s,$$
and the universal maps assemble into the **latching map** $\ell_r : L_r X \to X_r$. Dually, the **matching category** $\partial(r \downarrow \mathcal{R}^{-})$ has objects the non-identity maps $r \to t$ in $\mathcal{R}^{-}$; the **matching object** is the limit
$$M_r X \;=\; \lim_{(r \to t) \in \partial(r\downarrow \mathcal{R}^{-})} X_t,$$
with the universal maps assembling into the **matching map** $m_r : X_r \to M_r X$. (Both colimit and limit are taken in $\mathcal{M}$ and exist because $\mathcal{M}$ is bicomplete; see [[Def - Limit and Colimit]].) For a map $f : X \to Y$ of diagrams, the **relative latching map** at $r$ is the canonical map
$$X_r \cup_{L_r X} L_r Y \;\longrightarrow\; Y_r$$
out of the pushout, and the **relative matching map** at $r$ is the canonical map
$$X_r \;\longrightarrow\; Y_r \times_{M_r Y} M_r X$$
into the pullback.

**Reedy model structure.** Let $\mathcal{R}$ be a Reedy category and $\mathcal{M}$ a model category. The **Reedy model structure** on $\mathcal{M}^{\mathcal{R}}$ is defined by:

- $f : X \to Y$ is a **Reedy weak equivalence** if each component $f_r : X_r \to Y_r$ is a weak equivalence in $\mathcal{M}$;
- $f$ is a **Reedy cofibration** if for every $r$ the relative latching map $X_r \cup_{L_r X} L_r Y \to Y_r$ is a cofibration in $\mathcal{M}$;
- $f$ is a **Reedy fibration** if for every $r$ the relative matching map $X_r \to Y_r \times_{M_r Y} M_r X$ is a fibration in $\mathcal{M}$.

That these three classes form a model structure is [[Thm - Diagrams over a Reedy Category Form a Model Category]]. In particular, taking $Y = X$ trivial, an object $X$ is **Reedy cofibrant** when each absolute latching map $L_r X \to X_r$ is a cofibration, and **Reedy fibrant** when each absolute matching map $X_r \to M_r X$ is a fibration.

---

# Categorical / Structural Definition

The structural content is that a Reedy category is the indexing data for which diagrams admit a *transfinite cell-by-cell* description, organized by degree. The category $\mathcal{R}$ filters: let $\mathcal{R}_{\le n}$ be the full subcategory on objects of degree $\le n$. Restriction $\mathcal{M}^{\mathcal{R}} \to \mathcal{M}^{\mathcal{R}_{\le n}}$ and its left/right Kan extensions make $\mathcal{M}^{\mathcal{R}}$ the (inverse) limit of the tower $\cdots \to \mathcal{M}^{\mathcal{R}_{\le n}} \to \mathcal{M}^{\mathcal{R}_{\le n-1}} \to \cdots$, and the latching object $L_r X$ is exactly the value at $r$ of the *left Kan extension* of $X|_{\mathcal{R}_{<n}}$ along the inclusion, while the matching object $M_r X$ is the value of the *right Kan extension*. So latching is "freely extend the lower data up" and matching is "cofreely restrict the lower data down," and the relative latching/matching maps measure the difference between the actual degree-$n$ data and what the lower data forces.

This is the precise sense in which the Reedy structure interpolates between projective and injective. The Reedy cofibrations are sandwiched: every projective cofibration is a Reedy cofibration is an injective cofibration, and dually for fibrations. The interpolation is what buys universality — the Reedy structure exists for *any* $\mathcal{M}$ because the latching/matching objects are built from finite (co)limits over the well-founded degree filtration, requiring no cofibrant generation of $\mathcal{M}$.

A self-dual remark worth recording: if $\mathcal{R}$ is a Reedy category then so is $\mathcal{R}^{op}$, with the roles of $\mathcal{R}^{+}$ and $\mathcal{R}^{-}$ swapped and the degree function reused. Latching objects in $\mathcal{R}$ become matching objects in $\mathcal{R}^{op}$, cofibrations become fibrations, and the Reedy model structure on $\mathcal{M}^{\mathcal{R}}$ corresponds to the one on $(\mathcal{M}^{op})^{\mathcal{R}^{op}}$. Every theorem about Reedy cofibrations therefore has a free dual about Reedy fibrations.

---

# Relate to Other Fields / Compression

The Reedy condition is the categorical distillation of "**a CW-style filtration on the indexing shape.**" A CW complex is built by attaching cells of increasing dimension, where attaching an $n$-cell means gluing along a map of its boundary into the existing skeleton. A Reedy category is the shape-level analogue: degree plays the role of dimension, the direct maps are the "is a face/sub-cell of" relations, and the latching object $L_r X$ is the abstract "boundary" along which the degree-$r$ cell is attached. Building a Reedy-cofibrant diagram is exactly building a CW complex of $\mathcal{M}$-objects indexed by $\mathcal{R}$.

**True name:** a Reedy category is "**a category whose objects have a well-ordered dimension and whose maps split uniquely into a face-part and a degeneracy-part**," and the Reedy model structure is "**build the diagram one dimension at a time, where the new data in dimension $r$ is the relative latching (cofibration side) or relative matching (fibration side) map.**" The operational reading to carry around: *to check Reedy cofibrancy, check that each latching map $L_r X \to X_r$ is a cofibration*; this is the form you actually verify.

The construction is module-theoretically familiar to anyone who has built a free resolution: there too one builds a complex degree by degree, choosing in each degree generators that surject onto the syzygies (kernel) computed from below — the latching object is the homotopical analogue of "the part already generated," and the relative latching map is the homotopical analogue of "the newly chosen generators." The framings of [[Def - Cosimplicial and Simplicial Frame]] are exactly such resolutions for $\Delta$ and $\Delta^{op}$.

---

# Examples / Corollaries

**Is an instance — the simplex category $\Delta$.** This is *the* example. Take $\deg[n] = n$, let $\Delta^{+}$ be the injective order-preserving maps (the cofaces, raising degree) and $\Delta^{-}$ the surjective ones (the codegeneracies, lowering degree). Unique factorization is the classical epi-mono factorization: every order-preserving map factors uniquely as a surjection followed by an injection. So $\Delta$ is a Reedy category, and $\mathcal{M}^{\Delta}$ — the category of **cosimplicial objects** in $\mathcal{M}$ — carries the Reedy model structure. For a [[Def - Simplicial Set|simplicial set]] $X$ viewed as $X : \Delta^{op} \to \mathbf{Set}$, the latching object $L_n X$ is the set of *degenerate* $n$-simplices and the latching map $L_n X \to X_n$ is the inclusion of degeneracies; this is why Reedy cofibrant simplicial sets are exactly those where the degeneracies are "as free as possible" — and in $\mathbf{sSet}$ with monomorphisms as cofibrations, *every* simplicial set is Reedy cofibrant.

**Is an instance — $\Delta^{op}$ and simplicial objects.** Since $\Delta$ is Reedy, so is $\Delta^{op}$ (swap $+$ and $-$). The diagrams $\mathcal{M}^{\Delta^{op}}$ are the **simplicial objects** in $\mathcal{M}$, and now the *matching* object $M_n X$ is the object of "compatible boundaries" — for a simplicial object the matching map encodes the boundary $\partial$ of the $n$-simplices. Reedy fibrancy of a simplicial object is the abstract form of the **Kan condition**.

**Is an instance — any well-ordered poset / tower.** The poset $\omega = (0 \to 1 \to 2 \to \cdots)$ with $\deg n = n$, all non-identity maps direct ($\mathcal{R}^{+} = \omega$, $\mathcal{R}^{-} =$ identities only), is a Reedy category. Here $M_r X = *$ (the inverse category is trivial) so every map is a Reedy fibration, and $L_n X = X_{n-1}$ so Reedy cofibrations of towers are the maps that are "levelwise cofibrations relative to the previous stage" — the right notion for building **homotopy colimits of sequences**. Dually $\omega^{op}$ governs towers whose homotopy *limits* one computes.

**Is an instance — the cube category.** The category indexing an $n$-cube ($\{0,1\}^n$ with coordinatewise $\le$, degree = number of $1$s, all maps direct) is Reedy; Reedy fibrant $n$-cubes are exactly the **homotopy-cartesian cubes** one needs for Goodwillie calculus. A pushout/pullback square is the $n=2$ case.

**Is NOT a Reedy category — a category with a non-trivial automorphism.** A finite group $G$, viewed as a one-object category, is **not** Reedy: any degree function must assign the single object one degree $n$, but a non-identity automorphism neither raises nor lowers degree, so it can lie in neither $\mathcal{R}^{+} \setminus \mathrm{id}$ nor $\mathcal{R}^{-} \setminus \mathrm{id}$, and there is no unique direct/inverse factorization. This is exactly why ordinary diagram categories over groups (equivariant homotopy theory) need the *generalized* Reedy categories of Berger–Moerdijk, which permit automorphisms in each degree. The plain Reedy notion is rigid precisely because it forbids non-trivial automorphisms.

**Is NOT a Reedy structure — checking weak equivalences via latching maps.** It is tempting to symmetrize the definition and declare $f$ a Reedy weak equivalence when its relative latching maps are weak equivalences. This is wrong: Reedy weak equivalences are *componentwise*, full stop. The latching/matching maps govern only cofibrations and fibrations; the weak equivalences are inherited objectwise from $\mathcal{M}$, exactly as in the projective and injective structures.

**Calibration check.** Verify that $\Delta^{+} \cap \Delta^{-}$ is the identities (a map that is both injective and surjective on a finite ordinal is the identity). For the tower $\omega$, confirm that $L_0 X = \varnothing$ (the latching category at the bottom object is empty, so its colimit is the initial object), hence the relative latching map at $0$ is just $X_0 \cup_{\varnothing} Y_0 = Y_0 \leftarrow X_0$, i.e. Reedy cofibrancy at degree $0$ is cofibrancy of $X_0$. If you can also state why $\mathcal{R}^{op}$ is Reedy whenever $\mathcal{R}$ is, you have understood the direct/inverse duality.

---

# Unlocked by This

> [!tip] Framings and Cosimplicial Resolutions *(from this chapter)*
> A [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on an object $X$ is a *Reedy-cofibrant* cosimplicial resolution of $X$ — precisely a Reedy-cofibrant object of $\mathcal{M}^{\Delta}$ refining the constant diagram at $X$. The Reedy model structure on $\mathcal{M}^{\Delta}$ defined here is the ambient category in which frames live, and Reedy cofibrancy is exactly what makes a frame compute the right thing.

> [!tip] Homotopy Limits and Colimits *(from Model Categories)*
> For a Reedy category $\mathcal{R}$, the Reedy fibrant (resp. cofibrant) diagrams are the ones on which the ordinary limit (resp. colimit) already computes the **homotopy limit** (resp. **homotopy colimit**), so the Reedy structure is the standard machine for computing $\operatorname{holim}$ and $\operatorname{hocolim}$ over $\Delta^{op}$, $\Delta$, towers, and cubes. The **Bousfield–Kan** formulas for $\operatorname{holim}$ and $\operatorname{hocolim}$ are built from exactly the latching/matching data above.

> [!tip] Reedy and Generalized Reedy Categories in Higher Algebra *(from ∞-Category Theory)*
> The Reedy condition is what lets one present diagram **∞-categories** by strict model structures; the **complete Segal space** model for $(\infty,1)$-categories lives in Reedy-fibrant simplicial spaces, and **generalized Reedy categories** (allowing automorphisms) index symmetric and equivariant homotopy theories. The latching/matching formalism is the bridge from strict point-set diagrams to their homotopy-coherent meaning.
