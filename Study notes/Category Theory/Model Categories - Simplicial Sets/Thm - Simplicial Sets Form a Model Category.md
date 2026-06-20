---
type: theorem
subject: model-categories
prereqs:
  - "Def - Kan Fibration and Anodyne Extension"
  - "Def - Simplicial Homotopy Group"
  - "Def - Model Category"
  - "Def - Kan Complex and the Nerve"
  - "Def - Lifting Property and the Retract Argument"
  - "Thm - The Retract Argument"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ is the category of [[Def - Simplicial Set|simplicial sets]]. A **cofibration** is a monomorphism (level-wise injection); a **fibration** is a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] ($\mathrm{RLP}$ against horn inclusions); a **weak equivalence** is a map $f$ whose geometric realisation $|f|$ is a weak homotopy equivalence of [[Def - Topological Space|spaces]] — equivalently (between Kan complexes) a map inducing isomorphisms on all [[Def - Simplicial Homotopy Group|simplicial homotopy groups]]. The generating sets are $I = \{\partial\Delta^n \hookrightarrow \Delta^n : n \ge 0\}$ (boundary inclusions) and $J = \{\Lambda^n_k \hookrightarrow \Delta^n : n \ge 1,\ 0 \le k \le n\}$ (horn inclusions). $\mathrm{LLP}(\mathcal{S})$ and $\mathrm{RLP}(\mathcal{S})$ denote the left and right [[Def - Lifting Property and the Retract Argument|lifting classes]]. The full registry is on [[Model Categories — The Model Category of Simplicial Sets]].

---

# Statement

> **Theorem (Kan–Quillen).** The category $\mathbf{sSet}$ of [[Def - Simplicial Set|simplicial sets]] is a [[Def - Model Category|model category]] with
> - **cofibrations** = monomorphisms,
> - **fibrations** = [[Def - Kan Fibration and Anodyne Extension|Kan fibrations]],
> - **weak equivalences** = maps whose geometric realisation is a weak homotopy equivalence.
>
> In this structure every object is [[Def - Cofibrant and Fibrant Objects|cofibrant]], and the fibrant objects are exactly the [[Def - Kan Complex and the Nerve|Kan complexes]]. The model structure is **cofibrantly generated**, with generating cofibrations $I = \{\partial\Delta^n \hookrightarrow \Delta^n\}$ and generating trivial cofibrations $J = \{\Lambda^n_k \hookrightarrow \Delta^n\}$.

> **Corollary (internal description).** The trivial cofibrations are exactly the [[Def - Kan Fibration and Anodyne Extension|anodyne extensions]] (Gabriel–Zisman), the trivial fibrations are exactly the maps with $\mathrm{RLP}$ against all boundary inclusions, and between [[Def - Kan Complex and the Nerve|Kan complexes]] the weak equivalences are exactly the maps inducing isomorphisms on all [[Def - Simplicial Homotopy Group|simplicial homotopy groups]]. Thus the entire model structure is describable inside $\mathbf{sSet}$, with no reference to $\mathbf{Top}$.

---

# Motivation

This theorem is the foundation stone of combinatorial homotopy theory: it certifies that $\mathbf{sSet}$ is not merely *like* a homotopy theory but *is* one, in the full technical sense of [[Def - Model Category|Quillen's axioms]]. Without it, the constructions of the subject — homotopy groups, mapping spaces, derived functors, the comparison with spaces — would be a collection of ad hoc definitions with no guarantee that they fit together. The model structure is the guarantee: it says the three classes interlock exactly as MC1–MC5 require, so that all the general machinery of [[Thm - The Homotopy Category of a Model Category|homotopy categories]], derived functors, and [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunctions]] applies verbatim.

The role of the theorem is also to make the homotopy theory *checkable*. Quillen's axioms are stated for abstract classes, but here all three classes have explicit generators: cofibrations are detected by the boundary inclusions, trivial cofibrations by the horn inclusions. This is the content of "cofibrantly generated", and it is what reduces every factorisation and lifting question to a transfinite construction against two small, fully explicit sets. The small object argument then supplies the factorisations MC5 demands, mechanically. The deep work is not in the axioms themselves but in identifying the weak equivalences correctly and proving the two hard compatibility facts — that anodyne maps are weak equivalences, and that the realisation-defined weak equivalences have the internal homotopy-group description. Those two facts are where the geometry of horns enters.

The corollary is what makes the structure self-contained. It would be unsatisfying if the weak equivalences could only be defined by exporting to $\mathbf{Top}$. The corollary says they need not be: anodyne is an internal description of the trivial cofibrations, $\mathrm{RLP}(I)$ is an internal description of the trivial fibrations, and $\pi_n$-isomorphism is an internal description of the weak equivalences between fibrant objects. So $\mathbf{sSet}$ stands on its own as a homotopy theory, and the comparison with $\mathbf{Top}$ (the next theorem) becomes a statement relating *two* self-standing homotopy theories rather than a definition of one in terms of the other.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal inputs are the two generating sets and the realisation functor, but the *use* of the theorem is triggered by recognising disguised instances of its three classes.

The first disguised source is **a map you can show is a monomorphism**. Any level-wise injection is a cofibration, and this is far more common than it looks: every inclusion of a sub-simplicial-set, every boundary or horn inclusion, every skeletal inclusion $\mathrm{sk}_n X \hookrightarrow \mathrm{sk}_{n+1}X$ is a cofibration. The non-obvious step is realising that "cofibration" imposes no condition beyond injectivity, so cofibrancy is free and every construction-by-attaching-cells produces cofibrations. *Example problem:* show that for any $X$, the inclusion of the $n$-skeleton $\mathrm{sk}_n X \hookrightarrow X$ is a cofibration, hence $X$ is built from $\varnothing$ by attaching cells.

The second disguised source is **an object of the form $\mathrm{Sing}(Y)$ or a nerve $N(G)$ of a groupoid**. These are automatically [[Def - Kan Complex and the Nerve|Kan complexes]], hence fibrant, so the homotopy-group and mapping-space machinery applies without further checking. The non-obvious recognition is that fibrancy — usually the hard property to verify — comes for free from the *source* of the object. *Example problem:* compute the mapping space $\mathrm{Map}(K, \mathrm{Sing}\,Y)$ knowing it is a Kan complex because the target is.

The third disguised source is **a map built from horn inclusions by pushout or transfinite composition**. Such a map is [[Def - Kan Fibration and Anodyne Extension|anodyne]], hence a trivial cofibration, hence a weak equivalence — and this is how most weak equivalences are *produced* rather than checked. The non-obvious step is that an explicit cellular construction (attach horn-cells) certifies a weak equivalence with no homotopy-group computation. *Example problem:* show that the inclusion $\Delta^0 \hookrightarrow \Delta^n$ of a vertex is a weak equivalence by exhibiting it as anodyne.

**Targets (Output Amplification)**

The bare conclusion is "$\mathbf{sSet}$ is a model category". Combined with other facts it does much more.

Combine the model structure with **the realisation–singular [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]]**. Once $\mathbf{sSet}$ and $\mathbf{Top}$ are both model categories and $|{-}| \dashv \mathrm{Sing}$ is a Quillen adjunction, the general theorem [[Thm - Quillen Adjunctions Descend to Derived Adjunctions|that Quillen adjunctions descend]] gives derived functors $\mathbf{L}|{-}| \dashv \mathbf{R}\,\mathrm{Sing}$ on homotopy categories. The further result is that the comparison of $\mathbf{sSet}$ and $\mathbf{Top}$ becomes a question about derived functors, set up for the [[Thm - Geometric Realization is a Quillen Equivalence|Quillen-equivalence theorem]]. Non-obvious because it turns a structural fact into the launchpad for the foundational comparison.

Combine cofibrant generation with **the transfer/recognition principle**. Because the structure is generated by the explicit sets $I, J$, one can *transfer* it along an adjunction to put a model structure on other categories (simplicial objects in an algebraic category, simplicial presheaves). The further result $E$ is a whole industry of derived model structures, all anchored on $I, J$. Non-obvious because the abstract "cofibrantly generated" hypothesis is exactly the input the transfer theorems need.

Combine "every object is cofibrant" with **the formula for derived functors**. Since cofibrant replacement is the identity, the total left derived functor of any left Quillen functor out of $\mathbf{sSet}$ is computed *without resolving the source* — $\mathbf{L}F(X) = F(X)$ when $F$ preserves weak equivalences, and otherwise only the target needs fibrant replacement. The further result is dramatically simplified derived-functor computations. Non-obvious because in most model categories cofibrant replacement is the expensive step, and here it is free.

---

# Why Is It True

Strip away the formalism and the theorem rests on two geometric facts about horns and two pieces of categorical bookkeeping.

The bookkeeping first. The lifting and factorisation axioms (MC4, MC5) are *formal consequences* of having two generating sets, via the **small object argument**: any map factors as "attach all possible cells from $I$, transfinitely" followed by "the residual map lifts against $I$", and likewise for $J$. The reason this works in $\mathbf{sSet}$ is that the sources of the generators ($\partial\Delta^n$, $\Lambda^n_k$) are *small* — finite simplicial sets, so maps out of them commute with the transfinite colimits — which is exactly the smallness hypothesis the argument needs. So the *machinery* of the model structure is automatic once the generators are chosen; nothing geometric is needed for MC4 and MC5 beyond smallness.

The geometry enters in matching the two factorisations to the *correct* weak equivalences. There are two compatibility facts to prove, and they are the heart of the theorem. **First geometric fact: anodyne maps are weak equivalences.** A horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$ realises to a deformation retract $|\Lambda^n_k| \hookrightarrow |\Delta^n|$, hence a homotopy equivalence; and the saturation operations (pushout, transfinite composition, retract) preserve "realises to a weak homotopy equivalence" for *cofibrations*, so every anodyne map realises to a weak homotopy equivalence. **Second geometric fact: a trivial fibration (RLP against all boundary inclusions) is a weak equivalence.** Lifting against every $\partial\Delta^n \hookrightarrow \Delta^n$ lets one contract the fibres simplex by simplex, and realisation turns this into a deformation retraction. These two facts say the two MC5-factorisations land in the right classes, and the [[Thm - The Retract Argument|retract argument]] then forces the trivial cofibrations to be exactly the anodyne maps and the trivial fibrations to be exactly $\mathrm{RLP}(I)$.

The one-liner: **the model structure is the weak factorisation systems generated by $I$ and by $J$, glued together by the single fact that the two notions of "trivial" agree — anodyne maps and $\mathrm{RLP}(I)$-maps are both weak equivalences, because horns deformation-retract and trivial fibrations contract fibres.**

The corollary's internal description of weak equivalences is a separate geometric input: that for [[Def - Kan Complex and the Nerve|Kan complexes]], "$|f|$ is a weak homotopy equivalence" coincides with "$f$ is a $\pi_n$-isomorphism". This is the simplicial Whitehead theorem combined with $\pi_n(\mathrm{Sing}\,Y) = \pi_n(Y)$, and it is what lets the whole structure be described without $\mathbf{Top}$.

---

# What Makes This Hard

The formal axioms (MC1–MC3) and the lifting/factorisation axioms (MC4–MC5) are the easy part — they follow from cocompleteness and the small object argument almost mechanically. The genuine difficulty is the **two-out-of-three compatibility**: proving that the class defined by realisation (weak equivalences) is correctly matched to the lifting classes, i.e. that anodyne maps are weak equivalences and trivial fibrations are weak equivalences. The non-obvious step is that anodyne extensions — defined purely by closure properties — are weak equivalences; this requires the geometric input that horns deformation-retract *plus* a careful argument that the saturation operations preserve weak equivalence among cofibrations (this is where one needs that pushouts along cofibrations are homotopy pushouts). The most common error is to assume the weak equivalences are "obviously" compatible with the lifting structure and skip the verification that anodyne $\Rightarrow$ weak equivalence; that verification is precisely the content. A second subtlety is the corollary: proving the internal $\pi_n$-description of weak equivalences requires the simplicial Whitehead theorem, which itself uses minimal fibrations.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Treat the model structure as two weak factorisation systems — one generated by the boundary inclusions $I$ (giving cofibrations / trivial fibrations), one by the horn inclusions $J$ (giving trivial cofibrations / fibrations) — produced by the small object argument, and glue them by showing the two notions of "weak equivalence among the lifting classes" coincide with the realisation-defined weak equivalences. The two geometric inputs are: horns deformation-retract (so anodyne $\Rightarrow$ weak equivalence), and trivial fibrations contract (so $\mathrm{RLP}(I) \Rightarrow$ weak equivalence).

**Subgoal decomposition:**

1. **Generators are small; factorisations exist.** Show every map factors via $I$ and via $J$ by the small object argument.
   - *Hint:* The sources $\partial\Delta^n, \Lambda^n_k$ are finite, hence small relative to monomorphisms; run the transfinite construction.
   - *Why needed:* This is MC5, and it pins $\mathrm{cof} = \mathrm{cof}(I)$, $\mathrm{fib} = \mathrm{RLP}(J)$.

2. **Cofibrations are monomorphisms.** Show $\mathrm{cof}(I) = \{$monomorphisms$\}$.
   - *Hint:* A monomorphism is a transfinite composite of pushouts of boundary inclusions (attach one non-degenerate simplex at a time, by skeleta); conversely pushouts of monos are mono.
   - *Why needed:* Identifies the cofibration class explicitly and shows every object is cofibrant.

3. **Anodyne maps are weak equivalences.** Show every $\mathrm{cof}(J)$-map realises to a weak homotopy equivalence.
   - *Hint:* $|\Lambda^n_k| \hookrightarrow |\Delta^n|$ is a deformation retract; the closure operations preserve weak equivalence among cofibrations (pushout along a cofibration is a homotopy pushout).
   - *Why needed:* Matches the $J$-factorisation's left factor to the weak equivalences.

4. **Trivial fibrations are weak equivalences.** Show $\mathrm{RLP}(I) \subseteq \{$weak equivalences$\} \cap \{$fibrations$\}$.
   - *Hint:* RLP against all boundary inclusions lets you fill all spheres, contracting the homotopy fibres; realise to a deformation retraction.
   - *Why needed:* Matches the $I$-factorisation's right factor to the trivial fibrations.

5. **Retract argument closes the loop.** Conclude trivial cofibrations $=$ anodyne, trivial fibrations $= \mathrm{RLP}(I)$, and verify two-out-of-three (MC2) and retract closure (MC3).
   - *Hint:* Use [[Thm - The Retract Argument]] on the two factorisations; MC2 follows because $|{-}|$ preserves the two-out-of-three of weak homotopy equivalences.
   - *Why needed:* Assembles the verified pieces into the model-category axioms.

---

# Lemma Decomposition

> [!note]- Lemma 1: Monomorphisms are exactly the cofibrations $\mathrm{cof}(I)$
> **Statement:** A map of [[Def - Simplicial Set|simplicial sets]] lies in $\mathrm{cof}(I) = \mathrm{LLP}(\mathrm{RLP}(I))$ if and only if it is a monomorphism.
>
> **Hint:** Build any monomorphism $A \hookrightarrow B$ by attaching the non-degenerate simplices of $B$ not in $A$, in increasing dimension, each via a [[Def - Pullback and Pushout|pushout]] of a boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$.
>
> **Why needed:** It identifies the cofibration class explicitly, proves every object is [[Def - Cofibrant and Fibrant Objects|cofibrant]] ($\varnothing \to X$ is mono), and supplies the cellular description used throughout.
>
> > [!note]- Full proof
> > ($\Leftarrow$) Let $A \hookrightarrow B$ be a monomorphism. Order the non-degenerate simplices of $B \setminus A$ by dimension. Attaching a non-degenerate $n$-simplex $\sigma$ whose boundary already lies in the partial union is a pushout of $\partial\Delta^n \hookrightarrow \Delta^n$ along the attaching map $\partial\Delta^n \to (\text{partial union})$ (the boundary $d_i\sigma$ are already present; the simplex $\sigma$ and its degeneracies are new). The transfinite composite over all such attachments is $A \hookrightarrow B$, so it lies in $\mathrm{cell}(I) \subseteq \mathrm{cof}(I)$.
> >
> > ($\Rightarrow$) Boundary inclusions are monomorphisms; monomorphisms are closed under pushout, transfinite composition, and retract in the presheaf category $\mathbf{sSet}$ (these are computed level-wise in $\mathbf{Set}$, where injections are so closed). Hence every $\mathrm{cof}(I)$-map is a monomorphism.

> [!note]- Lemma 2: The small object argument produces the two factorisations
> **Statement:** Every map $f : X \to Y$ factors as $X \xrightarrow{i} Z \xrightarrow{p} Y$ with $i \in \mathrm{cell}(I)$ and $p \in \mathrm{RLP}(I)$, and as $X \xrightarrow{j} W \xrightarrow{q} Y$ with $j \in \mathrm{cell}(J)$ and $q \in \mathrm{RLP}(J)$.
>
> **Hint:** Transfinitely attach all squares from generators: at each stage, glue a copy of the codomain of each generator for every commuting square against $f$; the colimit map is the residual lift-having map.
>
> **Why needed:** This is the factorisation axiom MC5, and it forces $\mathrm{fib} = \mathrm{RLP}(J)$ and $\mathrm{triv\text{-}fib} = \mathrm{RLP}(I)$.
>
> > [!note]- Full proof
> > The domains $\partial\Delta^n$ and $\Lambda^n_k$ of the generators are *finite* simplicial sets, hence small relative to all monomorphisms: a map out of a finite simplicial set into a transfinite colimit of monomorphisms factors through a finite stage. The small object argument therefore applies. For the $I$-factorisation: set $Z_0 = X$; given $Z_\alpha$, form $Z_{\alpha+1}$ by pushing out, for every commuting square $(\partial\Delta^n \to Z_\alpha,\ \Delta^n \to Y)$, a copy of $\Delta^n$ along $\partial\Delta^n$; take colimits at limit stages. The colimit $Z = \mathrm{colim}\,Z_\alpha$ gives $i : X \to Z \in \mathrm{cell}(I)$ and a residual $p : Z \to Y$ that has $\mathrm{RLP}(I)$ because every square against a generator factors through some $Z_\alpha$ and was filled at stage $\alpha+1$. The $J$-factorisation is identical with $J$ in place of $I$.

> [!note]- Lemma 3: Anodyne extensions are weak equivalences
> **Statement:** Every anodyne map (every $\mathrm{cof}(J)$-map) has geometric realisation a weak homotopy equivalence.
>
> **Hint:** $|\Lambda^n_k| \hookrightarrow |\Delta^n|$ is a strong deformation retract; pushout along a cofibration is a homotopy pushout, so realising the saturation operations preserves weak equivalence.
>
> **Why needed:** It matches the left factor of the $J$-factorisation to the weak equivalences, half of what the [[Thm - The Retract Argument|retract argument]] needs to identify the trivial cofibrations.
>
> > [!note]- Full proof
> > The realisation $|\Lambda^n_k| \hookrightarrow |\Delta^n|$ is a strong deformation retract (radial projection from the barycentre of the missing face), hence a weak homotopy equivalence and a cofibration of spaces. The class of cofibrations of spaces that are weak homotopy equivalences is closed under pushout (pushout along a cofibration is a homotopy pushout, and homotopy pushouts preserve weak equivalences), transfinite composition (a transfinite composite of trivial cofibrations is a trivial cofibration), and retract. Since $|{-}|$ preserves all colimits (it is a left adjoint) and sends monomorphisms to cofibrations of spaces, it carries the saturation $\mathrm{cof}(J)$ into trivial cofibrations of spaces. Hence every anodyne map realises to a weak homotopy equivalence.

> [!note]- Lemma 4: Maps with RLP against all boundary inclusions are weak equivalences
> **Statement:** If $p : E \to B$ has $\mathrm{RLP}(I)$ (lifts against every $\partial\Delta^n \hookrightarrow \Delta^n$), then $p$ is a Kan fibration and $|p|$ is a weak homotopy equivalence.
>
> **Hint:** RLP against boundary inclusions includes RLP against horns (horns are retracts of boundaries up to the relevant lifting), giving the Kan condition; and it lets you build a section up to homotopy by filling all spheres in the fibres.
>
> **Why needed:** It matches the right factor of the $I$-factorisation to the trivial fibrations, the other half the retract argument needs.
>
> > [!note]- Full proof
> > First, $\mathrm{RLP}(I) \subseteq \mathrm{RLP}(J)$: a horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$ is a retract of the boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$ in the arrow category (collapse the extra face), and RLP is closed under retracts of the test map, so RLP against boundaries gives RLP against horns; thus $p$ is a Kan fibration. Second, RLP against *all* boundary inclusions means every sphere $\partial\Delta^n \to E$ over a disk $\Delta^n \to B$ fills; in particular the relative homotopy groups $\pi_n(\text{fibre})$ vanish, so each fibre is contractible. A Kan fibration with contractible fibres is a weak equivalence: the long exact sequence of [[Def - Simplicial Homotopy Group|simplicial homotopy groups]] forces $\pi_n(E) \cong \pi_n(B)$, and realising gives $|p|$ a weak homotopy equivalence.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — preconditions.** $\mathbf{sSet} = [\Delta^{op},\mathbf{Set}]$ is a presheaf category, hence complete and cocomplete (limits and colimits computed level-wise), giving MC1. The three classes are each closed under retracts: monomorphisms are (level-wise in $\mathbf{Set}$), Kan fibrations are (RLP classes always are), and realisation-weak-equivalences are (weak homotopy equivalences are, and $|{-}|$ preserves retracts) — this is MC3. Two-out-of-three (MC2) holds because $|{-}|$ sends the three classes to weak homotopy equivalences, which satisfy two-out-of-three in $\mathbf{Top}$.
>
> **Step 1 — cofibrations.** By Lemma 1, $\mathrm{cof}(I) = \{$monomorphisms$\}$, so we *define* cofibrations to be monomorphisms; every object is cofibrant since $\varnothing \to X$ is mono.
>
> **Step 2 — factorisations.** By Lemma 2, every map factors as $\mathrm{cell}(I)$ then $\mathrm{RLP}(I)$, and as $\mathrm{cell}(J)$ then $\mathrm{RLP}(J)$. Define fibrations $= \mathrm{RLP}(J) = \{$[[Def - Kan Fibration and Anodyne Extension|Kan fibrations]]$\}$.
>
> **Step 3 — the two factorisations land correctly.** By Lemma 4, $\mathrm{RLP}(I) \subseteq \{$Kan fibrations$\} \cap \{$weak equivalences$\}$, so the $I$-factorisation is (cofibration, trivial fibration). By Lemma 3, $\mathrm{cell}(J) \subseteq \mathrm{cof}(J) \subseteq \{$weak equivalences$\}$ and $\mathrm{cof}(J) \subseteq \{$monomorphisms$\}$ (horn inclusions are mono and mono is saturated), so the $J$-factorisation is (trivial cofibration, fibration).
>
> **Step 4 — lifting axiom MC4.** A cofibration that is a weak equivalence lifts against fibrations: factor it (Lemma 2) as $\mathrm{cell}(J)$ then $\mathrm{RLP}(J)$; the second factor is a fibration that is also a weak equivalence (two-out-of-three), hence by the converse of Lemma 4 it is in $\mathrm{RLP}(I)$, so the original trivial cofibration is a retract of the $\mathrm{cell}(J)$-map by the [[Thm - The Retract Argument|retract argument]], hence anodyne, hence lifts against every fibration. Dually a cofibration lifts against trivial fibrations because trivial fibrations are $\mathrm{RLP}(I) = \mathrm{RLP}(\mathrm{cof}(I))$.
>
> **Step 5 — identify the trivial classes.** The retract argument now gives: trivial cofibrations $= \mathrm{cof}(J) =$ anodyne extensions (Gabriel–Zisman), and trivial fibrations $= \mathrm{RLP}(I)$. The fibrant objects are the $X$ with $X \to *$ a Kan fibration, i.e. exactly the [[Def - Kan Complex and the Nerve|Kan complexes]].
>
> **Step 6 — internal description (corollary).** For Kan complexes, $|f|$ is a weak homotopy equivalence iff $f$ is a $\pi_n$-isomorphism (simplicial Whitehead theorem plus $\pi_n(\mathrm{Sing}\,Y) = \pi_n(Y)$, using [[Def - Minimal Fibration|minimal fibrations]]). Combined with Steps 1–5, every class has an internal description, with no reference to $\mathbf{Top}$.
>
> All of MC1–MC5 hold, so $(\mathbf{sSet}, \text{mono}, \text{Kan fib}, \text{w.e.})$ is a cofibrantly generated model category. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Transfer to simplicial objects in algebra.** Given any "nice" algebraic category $\mathcal{A}$ (modules, groups, Lie algebras), the category $s\mathcal{A}$ of simplicial objects often inherits a model structure with weak equivalences the maps that are weak equivalences of underlying simplicial sets. The exercise: state the transfer theorem and check its hypotheses (the generating trivial cofibrations of $\mathbf{sSet}$ have anodyne images) for $\mathcal{A} =$ abelian groups, recovering the projective model structure on connective chain complexes via Dold–Kan. Non-obvious because the cofibrant generation of $\mathbf{sSet}$ is exactly the input the transfer machinery consumes.

**The model structure on simplicial groups.** A simplicial group is automatically a Kan complex (a theorem of Moore). The exercise: show that the forgetful functor $s\mathbf{Grp} \to \mathbf{sSet}$ creates a model structure in which every object is fibrant, and identify the homotopy groups as the homotopy groups of the underlying simplicial set. Non-obvious because fibrancy, the usually-hard property, is automatic for group objects — a purely algebraic source forcing a homotopical property.

**Comparing with the Joyal structure.** Both the Kan–Quillen and Joyal model structures on $\mathbf{sSet}$ have monomorphisms as cofibrations but different fibrant objects ([[Def - Kan Complex and the Nerve|Kan complexes]] versus [[Def - Quasi-Category|quasi-categories]]). The exercise: show the identity functor $\mathbf{sSet}_{\text{Joyal}} \to \mathbf{sSet}_{\text{Kan–Quillen}}$ is a left Quillen functor (it preserves cofibrations and trivial cofibrations because Joyal weak equivalences between Kan complexes are Kan–Quillen weak equivalences). Non-obvious because two model structures on the same category, with the same cofibrations, are compared by a single identity functor that is nonetheless not an equivalence.

---

# Bridges

- **[[Thm - Geometric Realization is a Quillen Equivalence|The realisation–singular Quillen equivalence]]** — the payoff. Once $\mathbf{sSet}$ and $\mathbf{Top}$ are both model categories (this theorem and its topological analogue) and $|{-}| \dashv \mathrm{Sing}$ is a Quillen adjunction, one proves it is a Quillen *equivalence*, so $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$. This theorem is the precondition; the equivalence is the conclusion.

- **[[Thm - The Retract Argument|The retract argument]]** — the engine. Identifying the trivial cofibrations as anodyne and the trivial fibrations as $\mathrm{RLP}(I)$ both run through the retract argument: a map in the left lifting class is a retract of the cellular factor produced by the small object argument. This is the categorical mechanism that converts the *generated* classes into the *defined* ones.

- **[[Def - Quillen Adjunction and Quillen Equivalence|Cofibrant generation]] and the small object argument** — the structural template. The whole proof is an instance of the recognition theorem for cofibrantly generated model categories: given two generating sets and a candidate class of weak equivalences satisfying compatibility conditions, a model structure exists. The forward link is to the **cofibrantly generated model category** machinery, where this recognition is stated in general.

- **[[Thm - The Homotopy Category of a Model Category|The homotopy category]]** — the immediate consequence. With the model structure in hand, $\mathrm{Ho}(\mathbf{sSet})$ is the localisation at weak equivalences, computed as homotopy classes of maps between bifibrant objects — here, between [[Def - Kan Complex and the Nerve|Kan complexes]] (every object being cofibrant). This is the homotopy category of spaces, realised combinatorially.

---

# Unlocked by This

> [!tip] Derived Functors and Mapping Spaces *(from this chapter)*
> With the model structure, every [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]] out of $\mathbf{sSet}$ has total derived functors, and the simplicial mapping space $\mathrm{Map}(X, Y)$ (for $Y$ Kan) is the derived mapping space — the homotopy-correct space of maps. Every object being cofibrant makes these computations skip the source-resolution step.

> [!tip] Transferred and Localised Model Structures *(from Model Categories)*
> Cofibrant generation by $I, J$ is the hypothesis that lets the structure be **transferred** along adjunctions (to simplicial algebras, simplicial sheaves) and **localised** (Bousfield localization) to invert chosen maps. The two generating sets travel, anchoring an entire ecosystem of derived homotopy theories.

> [!tip] The Joyal Model Structure and ∞-Categories *(from Higher Category Theory)*
> The same cofibrations, with [[Def - Quasi-Category|quasi-categories]] as fibrant objects (test only inner horns), give the **Joyal model structure** presenting $\infty$-categories. The Kan–Quillen structure proved here is its $\infty$-groupoid sub-theory, and the comparison of the two is the first step in the theory of $(\infty,1)$-categories.
