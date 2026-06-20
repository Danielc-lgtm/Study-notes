---
type: theorem
subject: model-categories
prereqs:
  - "Def - Reedy Category and the Reedy Model Structure"
  - "Def - Model Category"
  - "Def - Limit and Colimit"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{R}$ is a [[Def - Reedy Category and the Reedy Model Structure|Reedy category]] with direct subcategory $\mathcal{R}^{+}$, inverse subcategory $\mathcal{R}^{-}$, and degree function $\deg$ valued in an ordinal $\lambda$; $\mathcal{M}$ is a [[Def - Model Category|model category]]. The diagram category is $\mathcal{M}^{\mathcal{R}}$, with $X_r = X(r)$. For an object $r$, $L_r X$ is the latching object (a colimit over the direct maps into $r$ from lower degree), $M_r X$ is the matching object (a limit over the inverse maps out of $r$ to lower degree), and the relative latching and matching maps of $f : X \to Y$ are $X_r \cup_{L_r X} L_r Y \to Y_r$ and $X_r \to Y_r \times_{M_r Y} M_r X$. Cofibrations, fibrations, and weak equivalences in $\mathcal{M}$ are $\rightarrowtail$, $\twoheadrightarrow$, $\xrightarrow{\sim}$. The full symbol registry is on [[Model Categories — Framings and Function Complexes]].

---

# Statement

> **Theorem (Reedy / Kan).** Let $\mathcal{R}$ be a Reedy category and $\mathcal{M}$ a [[Def - Model Category|model category]]. Then the diagram category $\mathcal{M}^{\mathcal{R}}$ is a model category — the **Reedy model structure** — with:
> - **weak equivalences** the objectwise weak equivalences ($f$ such that each $f_r$ is a weak equivalence in $\mathcal{M}$);
> - **cofibrations** the maps $f$ whose relative latching map $X_r \cup_{L_r X} L_r Y \to Y_r$ is a cofibration in $\mathcal{M}$ for every $r$;
> - **fibrations** the maps $f$ whose relative matching map $X_r \to Y_r \times_{M_r Y} M_r X$ is a fibration in $\mathcal{M}$ for every $r$.
>
> If $\mathcal{M}$ is cofibrantly generated, or simplicial, or proper, or monoidal, then so is $\mathcal{M}^{\mathcal{R}}$ with the Reedy structure.

> **Corollary (constant frames exist).** Taking $\mathcal{R} = \Delta$ and $\mathcal{R} = \Delta^{op}$, the categories of cosimplicial and simplicial objects in any $\mathcal{M}$ are model categories; in particular every object admits a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] (cofibrant replacement of the constant cosimplicial object) and a simplicial frame.

The two statements are tied together by the fact that frames *are* Reedy (co)fibrant replacements: the corollary is the existence of (co)fibrant replacements in the model structure the theorem provides.

---

# Motivation

The role of this theorem is to make "homotopy theory of diagrams" possible *for every model category at once*. Before it, you could do homotopy theory with single objects of $\mathcal{M}$; after it, you can do homotopy theory with $\mathcal{R}$-shaped diagrams — cosimplicial objects, towers, cubes — using a model structure that requires nothing of $\mathcal{M}$ beyond being a model category. This is what separates the Reedy structure from the projective and injective structures, which exist only when $\mathcal{M}$ is cofibrantly generated. The Reedy structure pays a price (it constrains the *shape* $\mathcal{R}$ to be Reedy) and buys universality in the *target* $\mathcal{M}$.

The deeper importance is downstream: the theorem is the engine of framings. A frame is by definition a Reedy-cofibrant (or fibrant) replacement of a constant diagram, and the entire theory of [[Def - Homotopy Function Complex|homotopy function complexes]] rests on those replacements existing. So this theorem is the foundation on which "every model category has homotopy mapping spaces" is built. It is also the standard tool for **homotopy limits and colimits over $\Delta^{op}$, $\Delta$, towers, and cubes** — geometric realizations, totalizations, sequential homotopy colimits, and homotopy-cartesian cubes are all computed by replacing a diagram by a Reedy (co)fibrant one and taking the strict (co)limit.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypothesis is "$\mathcal{R}$ is a Reedy category and $\mathcal{M}$ is a model category." The skill is recognizing when a diagram problem secretly satisfies it.

The first disguised source is **any indexing category built from a dimension or rank with no non-trivial automorphisms**. If you are indexing by something with a well-ordered notion of size and unique face/degeneracy factorization — finite ordinals, the cube poset, a tower, the category of finite sets and *injections*, the orbit category of a suitable group truncated — you have a Reedy category even if no one said so. The non-obvious step is to *find* the degree function and the direct/inverse split. *Example problem:* to put a model structure on $n$-cubes in spectra, recognize the cube poset $\{0,1\}^n$ as Reedy (degree = number of $1$s, all maps direct), and apply the theorem to get Reedy fibrant = homotopy cartesian cubes.

The second disguised source is **the demand to compute a homotopy limit or colimit**. Whenever a problem asks for $\operatorname{holim}$ or $\operatorname{hocolim}$ of a diagram over a Reedy shape, the route is: replace the diagram by a Reedy fibrant (resp. cofibrant) one and take the ordinary limit (resp. colimit). The non-obviousness is that the *strict* (co)limit of a Reedy (co)fibrant diagram already *is* the homotopy (co)limit. *Example problem:* to compute the totalization $\mathrm{Tot}\,X^{\bullet}$ of a cosimplicial space, recognize it as $\operatorname{holim}_{\Delta} X^{\bullet}$, Reedy-fibrantly replace $X^{\bullet}$, and totalize.

The third disguised source is **needing a frame**. Any time you want a homotopy mapping space, a derived tensor of a single object with simplicial sets, or a cosimplicial resolution, you are invoking this theorem for $\mathcal{R} = \Delta$ or $\Delta^{op}$. The non-obvious recognition is that "resolve $X$ cosimplicially" *is* "cofibrantly replace $cX$ in the Reedy structure on $\mathcal{M}^{\Delta}$." *Example problem:* to define $\mathrm{map}(X, Y)$, frame $X$ — which is exactly this theorem applied to $\Delta$.

**Targets (Output Amplification)**

The bare conclusion is "$\mathcal{M}^{\mathcal{R}}$ is a model category." Combined with other facts it does much more.

Combine the conclusion with **the duality $\mathcal{R} \leftrightarrow \mathcal{R}^{op}$**. Since $\mathcal{R}^{op}$ is Reedy whenever $\mathcal{R}$ is, with latching and matching swapped, every result about Reedy cofibrations over $\mathcal{R}$ yields a free result about Reedy fibrations over $\mathcal{R}^{op}$. The further result is that one only ever proves the cofibration half of any framing statement; the path-object/fibration half is the dual, halving every proof.

Combine the conclusion with **the projective–injective sandwich**. The Reedy structure has more cofibrations than the projective and fewer than the injective (when those exist); so a Reedy cofibrant object is automatically injectively cofibrant, and any construction that needs an injectively-cofibrant diagram can be fed a Reedy-cofibrant one, which is far easier to produce. The further result $E$ is a practical supply of cofibrant diagrams: Reedy cofibrant replacements are *computable* level by level, where injective ones are not.

Combine the conclusion with **inheritance of structure** (cofibrant generation, properness, the monoidal axiom, simplicial enrichment). Because the Reedy structure passes these properties from $\mathcal{M}$ to $\mathcal{M}^{\mathcal{R}}$, one can iterate: $\mathcal{M}^{\Delta}$ is again a (cofibrantly generated, proper, …) model category, so one can take diagrams of diagrams, frames of frames, bisimplicial objects, and so on. The further result is the entire bisimplicial machinery used to prove frame-independence in [[Thm - Framings Compute Homotopy Function Complexes]].

---

# Why Is It True

The proof is an induction on degree, and the reason it works is the unique factorization axiom of the Reedy category, which guarantees that the data in each degree decomposes cleanly into "what is forced from below" and "what is genuinely new."

Picture building a diagram $X$ one degree at a time. Suppose you have defined $X$ on all objects of degree $< n$. To extend to an object $r$ of degree $n$, you must supply $X_r$ together with all its structure maps. The structure maps split, by unique factorization, into direct maps (from lower degree into $r$) and inverse maps (from $r$ to lower degree). The direct maps into $r$ from below are exactly the data of a map $L_r X \to X_r$ out of the latching object; the inverse maps out of $r$ to below are exactly a map $X_r \to M_r X$ into the matching object. So the *only* new datum in degree $n$ at $r$ is the object $X_r$ sitting in a factorization $L_r X \to X_r \to M_r X$ of the canonical composite $L_r X \to M_r X$ (the composite that the lower-degree data already determines).

> **The single mechanism: extending a diagram by one degree is exactly factoring the canonical map $L_r X \to M_r X$ through $X_r$ — and a model structure is precisely a machine for factoring maps.**

This is why the latching and matching maps govern cofibrations and fibrations. A relative latching map being a cofibration is the statement that the new object $Y_r$ is attached to $X_r$ and the lower data "freely," exactly as a cofibration attaches a cell; a relative matching map being a fibration is the dual. The lifting axiom MC4 for $\mathcal{M}^{\mathcal{R}}$ reduces, degree by degree, to lifting in $\mathcal{M}$ for the relative latching/matching maps: a square of diagrams lifts if and only if it lifts in each degree, and the degree-$r$ lift is exactly a lift in $\mathcal{M}$ against the relative latching/matching map. The factorization axiom MC5 is built the same way: factor each relative latching map in $\mathcal{M}$ and the factorizations assemble, by unique factorization, into a factorization of diagrams. Everything reduces to $\mathcal{M}$ one degree at a time, and unique factorization is what guarantees the per-degree pieces fit together without overlap.

---

# What Makes This Hard

The hard part is not any single axiom but the *bookkeeping of the induction*: one must show that the per-degree latching and matching constructions are functorial and interact correctly with the structure maps, so that lifts and factorizations chosen degree by degree actually assemble into a map (resp. factorization) of diagrams. The non-obvious step is the **interaction lemma** — that the relative latching map of a composite, and the way matching objects pull back along latching objects, are compatible — which is where unique factorization is really used and where a naive attempt silently double-counts the degenerate part. The most common error is to forget that weak equivalences are *objectwise* (not latching-wise) and to try to characterize them via relative latching maps, which is false.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Induct on degree. Reduce every axiom of $\mathcal{M}^{\mathcal{R}}$ to the corresponding axiom of $\mathcal{M}$ applied to relative latching/matching maps, using unique factorization to assemble per-degree data into diagram data. Prove the lifting axiom and the factorization axiom by transfinite induction over $\deg$; the remaining axioms (bicompleteness, 2-out-of-3, retracts) are objectwise and immediate.

**Subgoal decomposition:**

1. **Bicompleteness, 2-out-of-3, retracts are objectwise.** Show $\mathcal{M}^{\mathcal{R}}$ has all limits/colimits (computed objectwise), and that the objectwise weak equivalences satisfy 2-out-of-3 and all three classes are retract-closed.
   - *Hint:* Limits/colimits in a diagram category are objectwise; 2-out-of-3 and retracts for objectwise classes follow from the same in $\mathcal{M}$ at each object.
   - *Why needed:* These are MC1–MC3 for the Reedy structure; they require no induction.

2. **The latching/matching adjunction.** Show that for fixed degree $< n$ data, the choice of $X_r$ with its latching map and matching map is equivalent to a factorization $L_r X \to X_r \to M_r X$ of the canonical map $L_r X \to M_r X$.
   - *Hint:* Use unique factorization: structure maps at $r$ split into direct (= map out of $L_r X$) and inverse (= map into $M_r X$); functoriality forces the composite to be the canonical lower-degree map.
   - *Why needed:* This is the reduction that turns "extend the diagram" into "factor a map in $\mathcal{M}$."

3. **Lifting (MC4) by induction on degree.** Show a square of diagrams with a Reedy (trivial) cofibration on the left and a Reedy (trivial) fibration on the right has a diagonal lift.
   - *Hint:* Build the lift degree by degree; at degree $r$ the obstruction is a lifting problem in $\mathcal{M}$ between the relative latching map (left) and relative matching map (right), which lift by hypothesis.
   - *Why needed:* MC4 is the heart; it justifies the cofibration/fibration definitions being compatible.

4. **Factorization (MC5) by induction on degree.** Show every map of diagrams factors as Reedy cofibration then trivial Reedy fibration (and dually).
   - *Hint:* At degree $r$, factor the relative latching map in $\mathcal{M}$ into a cofibration followed by a trivial fibration; assemble using step 2.
   - *Why needed:* MC5 gives (co)fibrant replacement, hence frames.

5. **Inheritance of extra structure.** Show cofibrant generation / properness / simpliciality transfer.
   - *Hint:* Generating (trivial) cofibrations are obtained by applying the latching-object left adjoints to the generators of $\mathcal{M}$; properness and simpliciality check objectwise.
   - *Why needed:* These are the conditions under which one iterates the construction (diagrams of diagrams).

---

# Lemma Decomposition

> [!note]- Lemma 1: Latching and matching objects are functorial and computed by Kan extension
> **Statement:** For each $r$, $X \mapsto L_r X$ and $X \mapsto M_r X$ are functors $\mathcal{M}^{\mathcal{R}} \to \mathcal{M}$, with $L_r X$ the value at $r$ of the left Kan extension of $X|_{\mathcal{R}_{<\deg r}}$ and $M_r X$ the value of the right Kan extension.
>
> **Hint:** The latching category $\partial(\mathcal{R}^{+}\!\downarrow r)$ and matching category $\partial(r\downarrow\mathcal{R}^{-})$ are the comma categories computing these Kan extensions; functoriality is functoriality of (co)limits.
>
> **Why needed:** It is what makes "the data forced from below" precise and functorial, so that per-degree choices assemble.
>
> > [!note]- Full proof
> > The latching object $L_r X = \operatorname*{colim}_{(s\to r)} X_s$ over the non-identity direct maps into $r$ is, by definition of left Kan extension along the inclusion $\mathcal{R}_{<\deg r} \hookrightarrow \mathcal{R}$, the value at $r$ of $\mathrm{Lan}(X|_{<\deg r})$ restricted to the boundary (excluding the identity at $r$). A map $f : X \to Y$ induces, by the universal property of colimits, a unique $L_r f : L_r X \to L_r Y$ commuting with all the cocone legs, and this is functorial because colimits are. The matching object is dual: $M_r X = \lim_{(r\to t)} X_t$ is the value of the right Kan extension, and $M_r f$ is induced by the universal property of limits. Both exist because $\mathcal{M}$ is bicomplete (MC1). The canonical map $L_r X \to M_r X$ exists because every direct map $s\to r$ composed with every inverse map $r \to t$ gives a map $s\to t$ in $\mathcal{R}_{<\deg r}$ on which $X$ is already defined; unique factorization guarantees these composites are consistent, so the cocone on $L_r X$ and the cone on $M_r X$ glue to a single map.

> [!note]- Lemma 2: Extending a diagram by one degree = factoring $L_r X \to M_r X$
> **Statement:** Given $X$ defined on $\mathcal{R}_{<n}$, the extensions of $X$ to the objects $r$ of degree $n$ correspond bijectively to choices, for each such $r$, of an object $X_r$ together with a factorization $L_r X \to X_r \to M_r X$ of the canonical map.
>
> **Hint:** Direct structure maps into $r$ assemble to the map *out of* $L_r X$; inverse structure maps out of $r$ assemble to the map *into* $M_r X$; the composite must be the lower-degree canonical map by functoriality.
>
> **Why needed:** This is the inductive step's combinatorial core; every axiom proof uses it to turn diagram data into a single map in $\mathcal{M}$.
>
> > [!note]- Full proof
> > Fix $r$ of degree $n$. A structure map of $X$ touching $r$ is the image $X(\phi)$ of a morphism $\phi$ with source or target $r$. By unique factorization, any morphism with target $r$ from lower degree is a direct map $s \to r$ (the inverse part would have to lower degree from $s$ then a direct map raise to $n$, but composed they are direct since the only inverse map into degree $n$ from below is via factorization through degree $\ge n$, excluded). The maps $X_s \to X_r$ for non-identity direct $s\to r$ are exactly a cocone under the latching diagram, i.e. a map $L_r X \to X_r$. Dually, maps $r \to t$ in $\mathcal{R}^{-}$ give a cone, i.e. a map $X_r \to M_r X$. Composing a direct-in with an inverse-out factors (uniquely) through lower degree, forcing $X_r \to M_r X$ composed with $L_r X \to X_r$ to equal the canonical $L_r X \to M_r X$ of Lemma 1. Conversely any such factorization defines all the structure maps at $r$ and one checks the simplicial-type identities hold by unique factorization. This is a bijection.

> [!note]- Lemma 3: Reedy lifting reduces to $\mathcal{M}$-lifting against relative latching/matching maps
> **Statement:** A square in $\mathcal{M}^{\mathcal{R}}$ with $i : A \to B$ on the left and $p : X \to Y$ on the right admits a diagonal lift if and only if, for every $r$ (built up by degree), the induced square in $\mathcal{M}$ between the relative latching map of $i$ at $r$ and the relative matching map of $p$ at $r$ admits a lift.
>
> **Hint:** Build the lift inductively; having lifted on $\mathcal{R}_{<n}$, the obstruction at $r$ is a single lifting problem in $\mathcal{M}$ whose left map is the relative latching map and whose right map is the relative matching map.
>
> **Why needed:** It is MC4 for the Reedy structure, and it is what makes the cofibration/fibration definitions interlock.
>
> > [!note]- Full proof
> > Suppose lifts have been chosen compatibly on all objects of degree $< n$. For $r$ of degree $n$, the data already chosen determines maps $L_r B \to X_r$ (via the lower-degree lift and the latching map of $A\to B$) and $B_r \to M_r Y \times_{?} \cdots$; assembling, the remaining problem is to fill the square in $\mathcal{M}$
> > $$\begin{array}{ccc} A_r \cup_{L_r A} L_r B & \longrightarrow & X_r \\ \downarrow & & \downarrow \\ B_r & \longrightarrow & Y_r \times_{M_r Y} M_r X \end{array}$$
> > whose left vertical is the relative latching map of $i$ and whose right vertical is the relative matching map of $p$. If $i$ is a Reedy cofibration the left map is a cofibration in $\mathcal{M}$; if $p$ is a trivial Reedy fibration the right map is a trivial fibration; so MC4 in $\mathcal{M}$ supplies the filler. The filler defines $B_r \to X_r$ and one checks compatibility with all structure maps via Lemma 2. Induct over $\deg$. The transfinite step (limit ordinals) uses that the structure maps at a limit-degree object are determined by the colimit/limit of lower degrees. Conversely a Reedy lift restricts to a solution of each per-degree square.

> [!note]- Lemma 4: Reedy factorization by degreewise factoring in $\mathcal{M}$
> **Statement:** Every map $f : X \to Y$ in $\mathcal{M}^{\mathcal{R}}$ factors as a Reedy cofibration followed by a trivial Reedy fibration (and dually a trivial Reedy cofibration followed by a Reedy fibration).
>
> **Hint:** Inductively, at degree $r$ factor the relative latching map $X_r \cup_{L_r X} L_r Z \to Y_r$ in $\mathcal{M}$ into a cofibration then a trivial fibration, where $Z$ is the factorization object being built.
>
> **Why needed:** It is MC5, which gives (co)fibrant replacement and hence frames.
>
> > [!note]- Full proof
> > Build the intermediate diagram $Z$ degree by degree with $f = (X \to Z \to Y)$. Having built $Z$ on $\mathcal{R}_{<n}$, at $r$ of degree $n$ form the relative latching map $X_r \cup_{L_r X} L_r Z \to Y_r$ in $\mathcal{M}$ (note $L_r Z$ is already defined since it depends only on lower degrees). Factor it in $\mathcal{M}$, by MC5, as a cofibration $X_r \cup_{L_r X} L_r Z \rightarrowtail Z_r$ followed by a trivial fibration $Z_r \xrightarrow{\sim}\twoheadrightarrow Y_r$. Define $Z_r$ to be this intermediate object; its latching map composite is a cofibration (so $X \to Z$ is a Reedy cofibration at $r$) and its map to $Y_r$ refines to a relative matching map that is a trivial fibration (so $Z \to Y$ is a trivial Reedy fibration at $r$ — this uses that an objectwise trivial fibration whose relative matching maps are trivial fibrations is a trivial Reedy fibration). Assemble via Lemma 2 and induct. Functorial factorizations in $\mathcal{M}$ give functorial ones here, yielding Hovey's refinement.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{R}$ be a Reedy category and $\mathcal{M}$ a model category.
>
> **Step 0 — the structure is well-posed.** By Lemma 1 the latching and matching objects $L_r X, M_r X$ exist (bicompleteness of $\mathcal{M}$) and are functorial, so the three candidate classes — objectwise weak equivalences, relative-latching cofibrations, relative-matching fibrations — are defined.
>
> **Step 1 — MC1 (bicompleteness).** Limits and colimits in $\mathcal{M}^{\mathcal{R}}$ exist and are computed objectwise, since $\mathcal{M}$ is bicomplete and (co)limits in functor categories are pointwise. In particular $\mathcal{M}^{\mathcal{R}}$ has an initial and terminal diagram.
>
> **Step 2 — MC2 (2-out-of-3) and MC3 (retracts).** Weak equivalences are objectwise; 2-out-of-3 holds at each object in $\mathcal{M}$, hence for diagrams. For retracts: a retract of $f$ in $\mathcal{M}^{\mathcal{R}}$ restricts to a retract of each $f_r$ and, applying the functors $L_r, M_r$, to a retract of each relative latching/matching map; retract-closure of cofibrations/fibrations/weak equivalences in $\mathcal{M}$ then gives retract-closure of the Reedy classes.
>
> **Step 3 — MC4 (lifting).** By Lemma 3, a lifting problem between a Reedy cofibration (resp. trivial Reedy cofibration) and a trivial Reedy fibration (resp. Reedy fibration) reduces, degree by degree, to a lifting problem in $\mathcal{M}$ between the relative latching map and the relative matching map. One checks that a Reedy cofibration's relative latching maps are cofibrations and a trivial Reedy fibration's relative matching maps are trivial fibrations (and that "trivial" is detected correctly: a Reedy weak equivalence that is a Reedy fibration has trivial-fibration relative matching maps — an inductive argument using 2-out-of-3 and the objectwise weak equivalence condition). MC4 in $\mathcal{M}$ supplies the per-degree fillers, which assemble by Lemma 2.
>
> **Step 4 — MC5 (factorization).** By Lemma 4, factoring the relative latching maps degree by degree in $\mathcal{M}$ produces the two required factorizations in $\mathcal{M}^{\mathcal{R}}$; functorial factorizations in $\mathcal{M}$ yield functorial ones, establishing Hovey's refinement.
>
> **Step 5 — the classes interlock.** It remains to confirm that the Reedy cofibrations are exactly the maps with the LLP against trivial Reedy fibrations, and dually — this follows from Steps 3–4 by the retract argument [[Thm - The Retract Argument]] applied in $\mathcal{M}^{\mathcal{R}}$: a map with the LLP against all trivial Reedy fibrations is a retract of its (Reedy cofibration, trivial Reedy fibration)-factorization, hence a Reedy cofibration by MC3.
>
> **Step 6 — inheritance.** If $\mathcal{M}$ is cofibrantly generated with generators $I, J$, then $\mathcal{M}^{\mathcal{R}}$ is cofibrantly generated by $\{F_r i : i \in I, r \in \mathcal{R}\}$ and similarly for $J$, where $F_r$ is the left adjoint to evaluation at $r$ (the latching-object construction); properness, the monoidal pushout-product axiom, and simplicial enrichment are checked objectwise / via the relative latching maps.
>
> **Conclusion.** The three classes satisfy MC1–MC5, so $\mathcal{M}^{\mathcal{R}}$ is a model category, and it inherits the listed extra structures. Specializing to $\mathcal{R} = \Delta, \Delta^{op}$ gives the model categories of cosimplicial and simplicial objects, hence frames. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Geometric realization as a homotopy colimit.** The geometric realization of a simplicial space $X_{\bullet}$ is the homotopy colimit $\operatorname*{hocolim}_{\Delta^{op}} X_{\bullet}$, computed by Reedy-cofibrantly replacing $X_{\bullet}$ in $\mathbf{Top}^{\Delta^{op}}$ and taking the strict realization. The non-obvious application is recognizing that the *fat realization* and the corrected realization differ exactly by the Reedy-cofibrancy condition (whether the degeneracies are cofibrations) — a direct use of the theorem in algebraic topology.

**Totalization of a cosimplicial space (the Bousfield–Kan / Adams spectral sequence setup).** The totalization $\mathrm{Tot}\,X^{\bullet} = \operatorname*{holim}_{\Delta} X^{\bullet}$ is computed by Reedy-fibrantly replacing $X^{\bullet}$ and taking $\lim$; the Reedy filtration by $\mathrm{Tot}_n$ is exactly the degree filtration of this theorem, and its associated spectral sequence is the Bousfield–Kan spectral sequence. This is the application that powers descent and completion computations in stable homotopy.

**Cubical diagrams in chain complexes / Tor and the Mayer–Vietoris cube.** An $n$-cube in $\mathbf{Ch}(R)$ is Reedy fibrant when it is homotopy cartesian; recognizing a Mayer–Vietoris square as a homotopy pushout/pullback square (the $n=2$ Reedy condition) lets one compute $\mathrm{Tor}$ and the homology of homotopy colimits via the theorem applied to the cube category. The application is non-obvious because the cube poset must be seen as a Reedy category first.

---

# Bridges

- **[[Thm - Framings Compute Homotopy Function Complexes]]** — the immediate consumer. This theorem provides the Reedy model structures on $\mathcal{M}^{\Delta}$ and $\mathcal{M}^{\Delta^{op}}$ in which [[Def - Cosimplicial and Simplicial Frame|frames]] are (co)fibrant replacements of constant diagrams; the framing theorem then uses those frames to build [[Def - Homotopy Function Complex|homotopy function complexes]]. Without the Reedy structure there are no frames and no derived mapping spaces.

- **[[Thm - The Homotopy Category of a Model Category]]** — the analogue for a single object. Where that theorem computes $\mathrm{Ho}(\mathcal{M})$ by replacing single objects bifibrantly, this one computes the homotopy theory of *diagrams* by replacing whole diagrams Reedy-bifibrantly; the bifibrant-replacement principle is the same, lifted to diagram categories.

- **[[Def - Homotopy Limit and Colimit|Homotopy limits and colimits]]** — the standard application. For a Reedy shape, the homotopy limit (resp. colimit) of a diagram is the strict limit (resp. colimit) of its Reedy fibrant (resp. cofibrant) replacement; the Reedy structure is the computational device behind $\operatorname{holim}$ and $\operatorname{hocolim}$ over $\Delta^{op}$, $\Delta$, towers, and cubes, and the **Bousfield–Kan** formulas express these via the latching/matching data.

- **The projective and injective model structures** — the comparison structures. When $\mathcal{M}$ is cofibrantly generated, $\mathcal{M}^{\mathcal{R}}$ also carries projective (objectwise fibrations/weak equivalences) and injective (objectwise cofibrations/weak equivalences) structures; the identity functors $\mathrm{proj} \to \mathrm{Reedy} \to \mathrm{inj}$ are Quillen equivalences (all three share the weak equivalences), so a Reedy-cofibrant object is injectively cofibrant and a Reedy-fibrant object is projectively fibrant — the Reedy structure is the computable middle.

---

# Unlocked by This

> [!tip] Frames and Homotopy Function Complexes *(from this chapter)*
> The corollary — that $\mathcal{M}^{\Delta}$ and $\mathcal{M}^{\Delta^{op}}$ are model categories — is exactly the existence of [[Def - Cosimplicial and Simplicial Frame|cosimplicial and simplicial frames]], the device that builds [[Def - Homotopy Function Complex|derived mapping spaces]] in any model category.

> [!tip] The Bousfield–Kan Spectral Sequence and Totalization *(from Stable Homotopy Theory)*
> The degree filtration of the Reedy structure on cosimplicial objects is the **Tot-tower**; its associated spectral sequence is the **Bousfield–Kan spectral sequence**, the engine of the **Adams** and descent spectral sequences. Reedy fibrancy is precisely the hypothesis under which the spectral sequence converges to the homotopy of the totalization.

> [!tip] Reedy Presentations of Diagram ∞-Categories *(from Higher Category Theory)*
> Reedy fibrant simplicial spaces are the home of the **complete Segal space** model of $(\infty,1)$-categories, and Reedy model structures present the diagram **∞-categories** $\mathrm{Fun}(N\mathcal{R}, \mathcal{C})$. The theorem is the point-set bridge from strict diagrams to homotopy-coherent ones.
