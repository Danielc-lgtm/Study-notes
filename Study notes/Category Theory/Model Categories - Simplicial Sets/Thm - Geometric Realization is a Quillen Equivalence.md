---
type: theorem
subject: model-categories
prereqs:
  - "Thm - Simplicial Sets Form a Model Category"
  - "Def - Quillen Adjunction and Quillen Equivalence"
  - "Thm - Geometric Realization is Left Adjoint to the Singular Nerve"
  - "Def - Minimal Fibration"
  - "Def - Simplicial Homotopy Group"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ carries the Kan–Quillen [[Thm - Simplicial Sets Form a Model Category|model structure]] (cofibrations monomorphisms, fibrations [[Def - Kan Fibration and Anodyne Extension|Kan fibrations]], weak equivalences the realisation-weak-equivalences). $\mathbf{Top}$ is a convenient category of [[Def - Topological Space|spaces]] (compactly generated weak Hausdorff) with the Quillen model structure (weak equivalences the weak homotopy equivalences, fibrations the Serre fibrations, cofibrations the retracts of relative cell complexes). The adjunction $|{-}| \dashv \mathrm{Sing}$ is the [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|realisation–singular adjunction]], with unit $\eta_X : X \to \mathrm{Sing}|X|$ and counit $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$. We write $\simeq_Q$ for "Quillen equivalent" and $\mathrm{Ho}(-)$ for the [[Thm - The Homotopy Category of a Model Category|homotopy category]]. The full registry is on [[Model Categories — The Model Category of Simplicial Sets]].

---

# Statement

> **Theorem (Quillen).** The adjunction
> $$|{-}| : \mathbf{sSet} \rightleftarrows \mathbf{Top} : \mathrm{Sing}$$
> is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]: geometric realisation is a left Quillen functor (it preserves cofibrations and trivial cofibrations), the singular nerve is a right Quillen functor (it preserves fibrations and trivial fibrations), and the derived unit and counit are weak equivalences. Consequently the total derived functors induce an equivalence of [[Thm - The Homotopy Category of a Model Category|homotopy categories]]
> $$\mathbf{L}|{-}| : \mathrm{Ho}(\mathbf{sSet}) \;\xrightarrow{\ \simeq\ }\; \mathrm{Ho}(\mathbf{Top}) : \mathbf{R}\,\mathrm{Sing}.$$

> **Corollary.** For every [[Def - Simplicial Set|simplicial set]] $X$ the unit $\eta_X : X \to \mathrm{Sing}|X|$ is a weak equivalence, and for every space $Y$ the counit $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence. The simplicial homotopy groups agree with the topological ones: $\pi_n(\mathrm{Sing}\,Y, y) \cong \pi_n(Y, y)$. This is the **homotopy hypothesis** in usable form: the homotopy theory of [[Def - Kan Complex and the Nerve|Kan complexes]] (∞-groupoids) is the homotopy theory of spaces.

---

# Motivation

This is the theorem the whole chapter was built to prove. Everything before it — the [[Thm - Simplicial Sets Form a Model Category|model structure on simplicial sets]], the [[Def - Simplicial Homotopy Group|homotopy groups]], the [[Def - Minimal Fibration|minimal fibrations]] — is apparatus, and this is the payoff: a precise, structural statement that simplicial sets and topological spaces carry *the same* homotopy theory, with no information lost in either direction. After this theorem, one may do homotopy theory entirely in $\mathbf{sSet}$, secure that the answers are the topological answers; this is why modern homotopy theory is combinatorial.

The reason the statement has real content, rather than being a tautology, is that simplicial sets are *enormously* more rigid than spaces. A simplicial set is a presheaf on a small category — discrete, finite in each dimension, fully algebraic — while a space carries a topology with all its point-set subtleties. It is genuinely surprising that this rigid combinatorial gadget loses nothing: that the unit $X \to \mathrm{Sing}|X|$ and the counit $|\mathrm{Sing}\,Y| \to Y$ are always weak equivalences, so the two worlds are interchangeable up to homotopy. The theorem is the assertion that homotopy type is *combinatorial in nature* — it can be captured by sets and face maps, the topology being inessential scaffolding.

The corollary is where the abstraction becomes the famous slogan. Restricted to fibrant objects, the equivalence says **Kan complexes are spaces**: an ∞-groupoid (a Kan complex) is the same thing, homotopically, as a homotopy type. This is the form of Grothendieck's *homotopy hypothesis* that is actually used: every comparison of models for $\infty$-categories — quasi-categories, Segal categories, complete Segal spaces, simplicial categories — is proved by a zig-zag of [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalences]] anchored on this one, and the entire edifice of higher category theory rests on the fact that the bottom rung, ∞-groupoids = spaces, is solid.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypotheses are the two model structures and the adjunction, so the source question is *when a homotopy-theoretic problem should be moved across the equivalence.*

The first disguised source is **a homotopy-theoretic invariant of a space you want to compute combinatorially**. Homology, homotopy groups, cohomology operations, the homotopy type itself — all are computed by replacing $Y$ with $\mathrm{Sing}(Y)$ and working in $\mathbf{sSet}$, because the equivalence guarantees the answer is unchanged. The non-obvious step is that $\mathrm{Sing}$ loses nothing: it is the *right derived* functor of an equivalence, so it is fully faithful on homotopy categories. *Example problem:* compute the homology of $Y$ as the homology of the [[Def - Singular Homology|Moore complex]] of $\mathrm{Sing}(Y)$.

The second disguised source is **a combinatorial model whose topological meaning you want**. A nerve, a classifying complex, a bar construction, a simplicial group — each presents a space via realisation, and the equivalence certifies that $|X|$ has exactly the homotopy type $X$ encodes. The non-obvious recognition is that $\mathbf{L}|{-}| = |{-}|$ on cofibrant objects (everything is cofibrant), so realisation is already derived — no replacement needed. *Example problem:* identify $|N(G)| \simeq BG$, the classifying space of a group, by realising the nerve.

The third disguised source is **a comparison of two homotopy theories you suspect agree**. The standard method is to build a Quillen adjunction between them and check the equivalence condition; this theorem is the template and the anchor. The non-obvious step is that proving a Quillen *equivalence* reduces, by this theorem's method, to checking the derived unit and counit on cofibrant/fibrant objects. *Example problem:* prove the Joyal and Kan–Quillen structures, or two models of ∞-categories, are related by checking unit/counit on Kan complexes.

**Targets (Output Amplification)**

The bare conclusion is $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$. Combined with other facts it does much more.

Combine the equivalence with **the simplicial mapping space**. Because the equivalence is compatible with the simplicial enrichment, the derived mapping space $\mathrm{Map}(X, Y)$ in $\mathbf{sSet}$ models the topological mapping space $\mathrm{Map}(|X|, |Y|)$, so function spaces — the home of higher homotopies — are computed combinatorially. The further result $E$ is that the *homotopy-coherent* structure, not just the homotopy category, transfers: $\mathbf{sSet}$ and $\mathbf{Top}$ are equivalent as $(\infty,1)$-categories. Non-obvious because a plain equivalence of homotopy categories would lose the higher structure; the Quillen equivalence keeps it.

Combine the corollary with **the chain of model comparisons for ∞-categories**. The equivalence $\mathbf{sSet} \simeq_Q \mathbf{Top}$ is the base case; combined with the Quillen equivalences relating quasi-categories, complete Segal spaces, and simplicial categories, it yields the theorem that *all* models of $(\infty,1)$-categories agree. The further result is the well-definedness of "the" homotopy theory of ∞-categories, independent of model. Non-obvious because each link is a separate hard theorem, anchored on this one.

Combine the equivalence with **product preservation**. Because $|{-}|$ preserves finite products (the key lemma, via minimal fibrations), the equivalence respects the cartesian-monoidal structure, so it is a *monoidal* Quillen equivalence. The further result is that simplicial and topological models agree on all product-built constructions: loop spaces, mapping tori, fibre products. Non-obvious because left adjoints do not generally preserve products — this is special to realisation and requires the minimal-fibration argument.

---

# Why Is It True

The Quillen-adjunction half is easy and structural; the equivalence half is where the geometry lives.

First, why it is a Quillen *adjunction*. Geometric realisation sends a monomorphism of simplicial sets to a relative cell complex of spaces — it glues geometric simplices along faces, which is exactly building a CW complex — so it preserves cofibrations; and it sends anodyne maps to trivial cofibrations because horns realise to deformation retracts. Dually $\mathrm{Sing}$ sends Serre fibrations to [[Def - Kan Fibration and Anodyne Extension|Kan fibrations]] (a horn-lifting problem for $\mathrm{Sing}(p)$ transposes to a homotopy-lifting problem for $p$, solved by the homotopy lifting property because $|\Lambda^n_k|$ retracts onto... no — because $|\Lambda^n_k| \hookrightarrow |\Delta^n|$ is a trivial cofibration that a Serre fibration lifts against). So the adjunction is Quillen by transposing lifting problems — operation 4 of the topic page.

Now why it is an *equivalence*. By the definition of [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]], it suffices to show the derived unit $X \to \mathrm{Sing}|X|$ is a weak equivalence for cofibrant $X$ (everything is cofibrant) and the derived counit $|\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence for fibrant $Y$ (every space is fibrant). Both reduce to a single fact: **$\pi_n(\mathrm{Sing}\,Y) \cong \pi_n(Y)$ and realisation preserves these groups.** The counit is a $\pi_n$-isomorphism because $\pi_n(|\mathrm{Sing}\,Y|) = \pi_n(\mathrm{Sing}\,Y) = \pi_n(Y)$, the first equality being that realisation preserves homotopy groups and the second being the agreement theorem; the unit is then a weak equivalence by a triangle-identity argument.

The one genuinely hard input is that **realisation preserves finite products**, $|X \times Y| \cong |X| \times |Y|$ (in compactly generated spaces). This is *false* for general left adjoints and *true* here only by a delicate argument, which is where [[Def - Minimal Fibration|minimal fibrations]] enter Quillen's original proof: one shows realisation sends a minimal fibration to a Serre fibre bundle (using that a minimal fibration is locally a product), and the product-preservation and homotopy-group-preservation follow from this local triviality. **The whole equivalence turns on the single geometric fact that realisation carries combinatorial bundles to topological bundles, which is exactly what minimisation provides.**

---

# What Makes This Hard

The Quillen-adjunction part is routine — preservation of cofibrations and fibrations by transposing lifting problems. The difficulty is concentrated in two places. First, proving the derived counit $|\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence requires knowing that realisation preserves homotopy groups, which in turn requires that **realisation sends Kan fibrations to Serre fibrations** — and this is *not* formal: a left adjoint need not preserve fibrations at all. Quillen's route is through [[Def - Minimal Fibration|minimal fibrations]]: every Kan fibration is fibrewise equivalent to a minimal one, a minimal fibration is a combinatorial bundle, and realisation sends bundles to bundles (Serre fibrations). The common error is to assume realisation preserves fibrations for the same easy reason it preserves cofibrations — it does not, and the minimal-fibration detour is unavoidable. Second, **realisation preserves finite products** only in a convenient category of spaces; in plain $\mathbf{Top}$ the product $|X| \times |Y|$ may have the wrong topology, and the identity $|X \times Y| \cong |X| \times |Y|$ fails. Working in compactly generated weak Hausdorff spaces is not a cosmetic choice — it is what makes the product-preservation, and hence the monoidal equivalence, true.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show $|{-}| \dashv \mathrm{Sing}$ is a Quillen adjunction by transposing lifting problems (realisation preserves cofibrations and anodyne maps; equivalently $\mathrm{Sing}$ preserves Serre fibrations and trivial fibrations). Then show it is a Quillen equivalence by checking the derived unit and counit are weak equivalences, which reduces to: realisation preserves homotopy groups, $\pi_n(\mathrm{Sing}\,Y) = \pi_n(Y)$, and (the hard lemma) realisation sends minimal fibrations to Serre fibre bundles and preserves finite products.

**Subgoal decomposition:**

1. **Quillen adjunction.** Show $|{-}|$ preserves cofibrations and trivial cofibrations.
   - *Hint:* Monomorphisms realise to relative cell complexes; horn inclusions realise to deformation retracts; transpose to check $\mathrm{Sing}$ preserves fibrations.
   - *Why needed:* It is the precondition for deriving the functors at all.

2. **Realisation preserves finite products.** Show $|X \times Y| \cong |X| \times |Y|$ in compactly generated spaces.
   - *Hint:* Reduce to standard simplices $|\Delta^m \times \Delta^n| \cong |\Delta^m| \times |\Delta^n|$ (a triangulation of the prism) and use that $|{-}|$ preserves colimits and the product is compactly generated.
   - *Why needed:* Makes the equivalence monoidal and is used in the homotopy-group comparison.

3. **Realisation of a minimal fibration is a Serre bundle.** Show $|p|$ is a Serre fibration for a minimal $p$.
   - *Hint:* A [[Def - Minimal Fibration|minimal fibration]] is locally a product (pullback along any simplex is $F \times \Delta^n$); realise the local triviality to a topological bundle.
   - *Why needed:* It is the geometric input that realisation preserves homotopy groups.

4. **Counit is a weak equivalence.** Show $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence for all $Y$.
   - *Hint:* $\pi_n(|\mathrm{Sing}\,Y|) = \pi_n(\mathrm{Sing}\,Y) = \pi_n(Y)$ (realisation preserves $\pi_n$ by Steps 2–3; agreement theorem); $\varepsilon$ induces the identity on $\pi_n$.
   - *Why needed:* Half the Quillen-equivalence condition (every space is fibrant).

5. **Unit is a weak equivalence.** Show $\eta_X : X \to \mathrm{Sing}|X|$ is a weak equivalence for all $X$.
   - *Hint:* Use the triangle identity $\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}_{|X|}$: since $\varepsilon_{|X|}$ is a weak equivalence (Step 4), so is $|\eta_X|$, hence $\eta_X$.
   - *Why needed:* The other half (every object is cofibrant); together they give the equivalence.

---

# Lemma Decomposition

> [!note]- Lemma 1: $|{-}|$ is a left Quillen functor
> **Statement:** Geometric realisation preserves cofibrations (sends monomorphisms to relative cell complexes) and trivial cofibrations (sends anodyne maps to trivial cofibrations of spaces).
>
> **Hint:** A monomorphism is built by attaching cells $\partial\Delta^n \hookrightarrow \Delta^n$; realisation turns each into the topological cell attachment $S^{n-1} \hookrightarrow D^n$. Horn inclusions realise to deformation retracts.
>
> **Why needed:** It makes $|{-}| \dashv \mathrm{Sing}$ a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]], so the derived functors exist.
>
> > [!note]- Full proof
> > $|{-}|$ preserves colimits (left adjoint). A monomorphism $A \hookrightarrow B$ is a transfinite composite of pushouts of $\partial\Delta^n \hookrightarrow \Delta^n$ (Lemma 1 of [[Thm - Simplicial Sets Form a Model Category]]); applying $|{-}|$ gives a transfinite composite of pushouts of $|\partial\Delta^n| = S^{n-1} \hookrightarrow |\Delta^n| = D^n$, i.e. a relative cell complex, which is a cofibration of spaces. For trivial cofibrations: anodyne maps are built from horn inclusions, and $|\Lambda^n_k| \hookrightarrow |\Delta^n|$ is a deformation retract (hence a trivial cofibration of spaces); the saturation operations are preserved by $|{-}|$. Hence $|{-}|$ preserves both classes and is left Quillen.

> [!note]- Lemma 2: Realisation preserves finite products
> **Statement:** For all simplicial sets $X, Y$, the canonical map $|X \times Y| \to |X| \times |Y|$ is a homeomorphism, the product taken in compactly generated weak Hausdorff spaces.
>
> **Hint:** Both sides preserve colimits in each variable, so reduce to $X = \Delta^m$, $Y = \Delta^n$; then $|\Delta^m \times \Delta^n| \cong |\Delta^m| \times |\Delta^n|$ is the standard triangulation of the prism.
>
> **Why needed:** It makes the equivalence monoidal and is the input to preserving homotopy groups (which are defined via products with $\Delta^1$).
>
> > [!note]- Full proof
> > Fix $Y$. The functors $X \mapsto |X \times Y|$ and $X \mapsto |X| \times |Y|$ both preserve colimits in $X$ ($|{-}|$ and $-\times Y$ and $-\times|Y|$ are colimit-preserving in compactly generated spaces, where the product is a left adjoint). A natural transformation between colimit-preserving functors on a presheaf category is an isomorphism iff it is on representables (density). On representables the map is $|\Delta^m \times \Delta^n| \to |\Delta^m| \times |\Delta^n|$; the simplicial set $\Delta^m \times \Delta^n$ is the nerve of the poset $[m] \times [n]$, whose non-degenerate simplices are the monotone lattice paths, and these triangulate the geometric prism $|\Delta^m| \times |\Delta^n|$ exactly. Hence the map is a homeomorphism on representables, so for all $X$, and then for all $Y$ by symmetry.

> [!note]- Lemma 3: Realisation sends minimal fibrations to Serre fibrations
> **Statement:** If $p : E \to B$ is a [[Def - Minimal Fibration|minimal fibration]], then $|p| : |E| \to |B|$ is a Serre fibration (indeed a fibre bundle).
>
> **Hint:** A minimal fibration is locally trivial — pullback along any simplex $\Delta^n \to B$ is a product $F \times \Delta^n$. Realise the local triviality.
>
> **Why needed:** It is the geometric core: it gives that realisation preserves homotopy groups (every Kan fibration is fibrewise equivalent to a minimal one), which drives the counit being a weak equivalence.
>
> > [!note]- Full proof
> > By the bundle property of minimal fibrations, for each simplex $\beta : \Delta^n \to B$ the pullback $\beta^* E \to \Delta^n$ is isomorphic over $\Delta^n$ to the projection $F \times \Delta^n \to \Delta^n$, compatibly with faces. Applying $|{-}|$ and using Lemma 2 (product preservation), $|\beta^* E| \cong |F| \times |\Delta^n| \to |\Delta^n|$ is a trivial bundle, and the trivialisations glue (realisation preserves the gluing colimit) to exhibit $|p|$ as a fibre bundle with fibre $|F|$ over $|B|$. A fibre bundle over a CW base is a Serre fibration. Since every Kan fibration is fibrewise homotopy equivalent to a minimal one, realisation sends every Kan fibration to a Serre fibration up to weak equivalence, hence preserves homotopy groups.

> [!note]- Lemma 4: The counit $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence
> **Statement:** For every space $Y$, the counit $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$ induces isomorphisms on all homotopy groups.
>
> **Hint:** $\pi_n(|\mathrm{Sing}\,Y|) = \pi_n(\mathrm{Sing}\,Y)$ (realisation preserves $\pi_n$, Lemma 3) $= \pi_n(Y)$ (agreement theorem); check $\varepsilon$ realises the identity.
>
> **Why needed:** It is half the Quillen-equivalence condition (every space is fibrant), and the corollary's "counit is a weak equivalence".
>
> > [!note]- Full proof
> > The [[Def - Simplicial Homotopy Group|simplicial homotopy group]] $\pi_n(\mathrm{Sing}\,Y, y)$ is, by definition, based homotopy classes of spheroids — singular simplices $|\Delta^n| \to Y$ collapsing the boundary to $y$ — modulo simplicial homotopy, which is exactly $\pi_n(Y, y)$ (agreement theorem). By Lemma 3 (realisation preserves $\pi_n$ via minimal models), $\pi_n(|\mathrm{Sing}\,Y|) \cong \pi_n(\mathrm{Sing}\,Y) \cong \pi_n(Y)$. The counit $\varepsilon_Y$ sends the realisation of a singular simplex $\sigma : |\Delta^n| \to Y$ to its value, inducing on $\pi_n$ exactly the identity under these isomorphisms. Hence $\varepsilon_Y$ is a $\pi_n$-isomorphism for all $n$ and all basepoints, i.e. a weak homotopy equivalence.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — preconditions.** Both $\mathbf{sSet}$ (by [[Thm - Simplicial Sets Form a Model Category]]) and $\mathbf{Top}$ (compactly generated, Quillen structure) are model categories; $|{-}| \dashv \mathrm{Sing}$ is an adjunction by [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]. In $\mathbf{sSet}$ every object is [[Def - Cofibrant and Fibrant Objects|cofibrant]]; in $\mathbf{Top}$ every object is fibrant.
>
> **Step 1 — Quillen adjunction.** By Lemma 1, $|{-}|$ is left Quillen, so $(|{-}|, \mathrm{Sing})$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]]; the total derived functors $\mathbf{L}|{-}| = |{-}|$ (source already cofibrant) and $\mathbf{R}\,\mathrm{Sing} = \mathrm{Sing} \circ R$ exist.
>
> **Step 2 — product preservation.** By Lemma 2, $|{-}|$ preserves finite products in compactly generated spaces; in particular $|X \times \Delta^1| \cong |X| \times [0,1]$, so realisation carries simplicial homotopies to topological homotopies.
>
> **Step 3 — realisation preserves homotopy groups.** By Lemma 3, realisation sends minimal fibrations to Serre fibre bundles; since every [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] is fibrewise homotopy equivalent to a [[Def - Minimal Fibration|minimal]] one, $|{-}|$ sends Kan fibrations to Serre fibrations up to weak equivalence and hence preserves the long exact sequence of homotopy groups; combined with Step 2 this gives $\pi_n(|X|) \cong \pi_n(X)$ for Kan $X$ (and for all $X$ after fibrant replacement).
>
> **Step 4 — the counit is a weak equivalence.** By Lemma 4, $\varepsilon_Y : |\mathrm{Sing}\,Y| \to Y$ is a weak homotopy equivalence for every (fibrant) space $Y$.
>
> **Step 5 — the unit is a weak equivalence.** For every (cofibrant) simplicial set $X$, the triangle identity gives $\varepsilon_{|X|} \circ |\eta_X| = \mathrm{id}_{|X|}$. Since $\varepsilon_{|X|}$ is a weak homotopy equivalence (Step 4) and the identity is one, two-out-of-three forces $|\eta_X|$ to be a weak homotopy equivalence; by definition of the weak equivalences of $\mathbf{sSet}$, $\eta_X : X \to \mathrm{Sing}|X|$ is a weak equivalence.
>
> **Step 6 — conclude.** A Quillen adjunction whose derived unit (on cofibrant objects) and derived counit (on fibrant objects) are weak equivalences is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]. By Steps 1, 4, 5 this holds, so $|{-}| \dashv \mathrm{Sing}$ is a Quillen equivalence and $\mathbf{L}|{-}| \dashv \mathbf{R}\,\mathrm{Sing}$ is an equivalence $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$. The corollary's $\pi_n$-agreement is Step 3 applied to $\mathrm{Sing}\,Y$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**The homotopy hypothesis for groupoids.** Restrict the equivalence to $1$-truncated objects: [[Def - Groupoid|groupoids]] (as $1$-types) correspond to homotopy $1$-types (spaces with $\pi_n = 0$ for $n \ge 2$). The exercise: show that the nerve $N : \mathbf{Grpd} \to \mathbf{sSet}$ lands in Kan complexes and that $|N(\mathcal{G})|$ is a $K(\pi, 1)$ for each component, recovering the classical fact that groupoids model $1$-types. Non-obvious because it is the bottom truncation of the homotopy hypothesis, the case where everything is computable by hand.

**Eilenberg–MacLane spaces from chain complexes.** Via Dold–Kan, a chain complex concentrated in degree $n$ with group $A$ corresponds to a simplicial abelian group whose realisation is the Eilenberg–MacLane space $K(A, n)$. The exercise: build the minimal simplicial model of $K(A, n)$, realise it, and verify $\pi_n = A$, $\pi_i = 0$ otherwise. Non-obvious because a purely homological-algebra input (a complex) produces, through this equivalence, a specific space with prescribed homotopy groups — the building block of all Postnikov towers.

**Comparing models of $(\infty,1)$-categories.** This Quillen equivalence is the anchor of a web of equivalences relating quasi-categories, simplicial categories, complete Segal spaces, and Segal categories. The exercise: state the chain of Quillen equivalences (Joyal–Lurie, Bergner, Rezk) and identify where $\mathbf{sSet} \simeq_Q \mathbf{Top}$ enters as the input for the ∞-groupoid (mapping space) comparison. Non-obvious because the well-definedness of "the homotopy theory of ∞-categories" depends on this entire web, every link a Quillen equivalence proved by the unit/counit method used here.

---

# Bridges

- **[[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|The realisation–singular adjunction]]** — the underlying adjunction. That theorem establishes $|{-}| \dashv \mathrm{Sing}$ and that $\mathrm{Sing}(Y)$ is a Kan complex; this theorem upgrades the adjunction to a Quillen equivalence by adding the model structures and checking the derived unit and counit. The earlier theorem is the algebra; this one is the homotopy theory.

- **[[Def - Minimal Fibration|Minimal fibrations]]** — the technical engine. The single hard input — realisation preserves homotopy groups and finite products — is proved by minimising a Kan fibration to a bundle, realising the local triviality, and using that bundles are Serre fibrations. Without minimal fibrations the equivalence cannot be proved by Quillen's original route; they are the rigidity that makes realisation respect fibrations.

- **[[Thm - Quillen Adjunctions Descend to Derived Adjunctions|Quillen adjunctions descend to derived adjunctions]]** — the abstraction used. That theorem turns this Quillen equivalence into the equivalence of homotopy categories $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$; the general machinery does the bookkeeping once the unit/counit conditions are verified here. This theorem supplies the input; the descent theorem delivers the conclusion in invariant form.

- **The homotopy hypothesis and ∞-categories** — the conceptual destination. The corollary "Kan complexes are spaces" is the homotopy hypothesis, and it is the base case of the comparison of all models for $\infty$-categories. Each subsequent model comparison (quasi-categories, complete Segal spaces) is a Quillen equivalence proved by the same unit/counit method, anchored on this result.

---

# Unlocked by This

> [!tip] Combinatorial Homotopy Theory *(from this chapter and beyond)*
> The equivalence licenses doing *all* homotopy theory in $\mathbf{sSet}$: homotopy groups, cohomology operations, Postnikov towers, obstruction theory, and spectral sequences are all computed combinatorially, with the guarantee that the answers are the topological ones. This is why the simplicial model is the default substrate of modern homotopy theory.

> [!tip] The Homotopy Hypothesis and Higher Categories *(from Higher Category Theory)*
> "Kan complexes are spaces" is the **homotopy hypothesis**, the assertion that ∞-groupoids are homotopy types. Every model of $\infty$-**categories** — quasi-categories, Segal spaces, simplicial categories — is compared to the others by a Quillen equivalence anchored on this one, making "the homotopy theory of $\infty$-categories" well-defined independently of model.

> [!tip] Homotopy Type Theory *(from Foundations / Type Theory)*
> Read univalently, the equivalence says **a type is a space is an ∞-groupoid** — the slogan that **homotopy type theory** turns into a foundational principle, with the Kan-complex semantics of the identity type being precisely the simplicial model of spaces established here.
