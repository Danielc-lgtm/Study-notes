---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Kan Complex and the Nerve"
  - "Def - Simplicial Set"
  - "Def - Topological Space"
  - "Def - Higher Homotopy Group"
  - "Def - Homotopy"
tags: [category-theory, higher-categories, foundations]
---

# Notation

$T$ denotes a [[Def - Topological Space|topological space]]; $\pi_n(T,t)$ its $n$th [[Def - Higher Homotopy Group|homotopy group]] at a basepoint $t$. A **weak homotopy equivalence** is a continuous map inducing isomorphisms on all $\pi_n$ (and a bijection on $\pi_0$); a **homotopy type** is a space considered up to weak homotopy equivalence. $\mathrm{Sing}(T)$ is the **singular [[Def - Simplicial Set|simplicial set]]** of $T$, with $\mathrm{Sing}(T)_n = \{\text{continuous } \Delta^n_{\mathrm{top}} \to T\}$; $|{-}|$ is **geometric realisation**, left adjoint to $\mathrm{Sing}$. A **[[Def - Kan Complex and the Nerve|Kan complex]]** is a simplicial set in which every horn $\Lambda^n_i \to X$ ($0 \le i \le n$) fills. An **$\infty$-groupoid** is an $(\infty,0)$-category — a higher category all of whose cells (in every dimension) are invertible up to higher cells; in the simplicial model an $\infty$-groupoid *is* a Kan complex. We write $\Pi_\infty(T)$ for the **fundamental $\infty$-groupoid** of $T$. The terms "weak ω-groupoid" and "coherator" refer to the algebraic (globular) definitions developed in companion chapters not yet in this vault; they appear as **bold plain text**. The full registry is on [[Higher Categories — Other Definitions of Weak n-Categories]].

---

# Statement

> **The Homotopy Hypothesis (Grothendieck).** The construction of the fundamental $\infty$-groupoid induces an equivalence between the homotopy theory of **$\infty$-groupoids** and the homotopy theory of **[[Def - Topological Space|topological spaces]]** (homotopy types):
> $$
> \Pi_\infty : \{\text{homotopy types}\} \;\xrightarrow{\;\simeq\;}\; \{\infty\text{-groupoids}\}, \qquad \text{with inverse } |{-}|.
> $$
> Concretely, $\Pi_\infty(T)$ has the points of $T$ as objects, paths as $1$-cells, homotopies of paths as $2$-cells, and so on, with every cell invertible; the geometric realisation $|{-}|$ recovers a space from an $\infty$-groupoid, and the unit and counit of $\Pi_\infty \dashv |{-}|$ are weak homotopy equivalences / equivalences.

> **Theorem (simplicial form — Milnor).** For the model in which an $\infty$-groupoid is a **[[Def - Kan Complex and the Nerve|Kan complex]]**, the adjunction
> $$
> |{-}| : \mathbf{sSet} \;\rightleftarrows\; \mathbf{Top} : \mathrm{Sing}
> $$
> is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] between simplicial sets (with the Kan–Quillen model structure) and topological spaces (with the Quillen model structure). Restricted to fibrant objects it gives an equivalence of homotopy theories between Kan complexes and homotopy types — a *theorem*. For the **algebraic** (globular, Grothendieck–Maltsiniotis) definitions of weak ω-groupoid, the corresponding statement remains a *conjecture*.

---

# Motivation

This is the theorem that tells you higher category theory is *about something*. A definition of weak higher category is a large piece of machinery, and one's first worry is whether it captures anything real or is just an elaborate formalism. The homotopy hypothesis answers the worry for the simplest case — the case where everything is invertible. It says that an $\infty$-groupoid, the higher category with no non-invertible cells, is exactly a **space up to homotopy**: the objects, paths, homotopies, and higher homotopies of an $\infty$-groupoid *are* the points, paths, and homotopies of a space. So the invertible part of higher category theory is not a new subject at all — it is the homotopy theory that topologists have been doing since Poincaré.

The role of the theorem is therefore twofold. As a *bridge*, it lets the entire toolkit of algebraic topology — homotopy groups, fibrations, Postnikov towers, obstruction theory, the whole machinery — flow into higher category theory, and lets the categorical reorganisation flow back into topology. As a *specification*, it is the acceptance test for every proposed definition of weak ω-category: restrict the definition to its invertible objects, and you must get homotopy types. Grothendieck elevated this from a check to a *program* — in *Pursuing Stacks* he proposed building higher category theory so that the homotopy hypothesis would be true *by construction*, taking spaces as the very meaning of higher groupoids. That is why a "hypothesis" that is a theorem in the simplicial models is still the organising idea: it is the demand that disciplines the algebraic definitions, and proving it for them (the Grothendieck–Maltsiniotis coherators) is one of the deep open problems of the subject.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "an $\infty$-groupoid" (in some model) or "a homotopy type"; the skill is recognising when a problem secretly hands you one.

The first disguised source is **a structure in which everything is invertible up to coherent higher data**. Whenever you build a higher category and then observe that every $1$-cell has a (weak) inverse, every $2$-cell has one, and so on, you have an $\infty$-groupoid, and the homotopy hypothesis lets you treat it as a space — importing homotopy groups and the rest. The non-obvious step is *checking invertibility coherently*, not just dimension-by-dimension. *Example problem:* given a [[Def - Quasi-Category|quasi-category]] in which every morphism is an equivalence, recognise it as a [[Def - Kan Complex and the Nerve|Kan complex]] (all horns, not just inner, fill) and hence as a space, so that its "categorical" invariants are homotopy groups.

The second disguised source is **a space presented by generators and relations between paths**, i.e. a CW complex or a presentation of a homotopy type. Such a presentation is literally a recipe for an $\infty$-groupoid: $0$-cells are vertices, $1$-cells are edges (paths), $2$-cells are the relations (homotopies), and so on. The non-obvious recognition is that *attaching an $n$-cell to a space* is the same move as *imposing an $n$-morphism in a groupoid*. *Example problem:* compute $\pi_1$ of a presented space by reading the presentation as the fundamental groupoid and abelianising/truncating — the categorical and topological computations coincide.

The third disguised source is **a homotopy-coherent algebraic structure with invertible operations** — a grouplike $E_\infty$- or $A_\infty$-space, or a simplicial group. These are $\infty$-groupoids with extra (monoidal) structure, hence *spaces with extra structure*; the homotopy hypothesis underlies the equivalence "grouplike $E_\infty$-spaces $=$ connective spectra $=$ infinite loop spaces". The non-obviousness is that the algebraic invertibility is exactly groupoidal invertibility. *Example problem:* recognise the classifying space of a group as the $\infty$-groupoid $BG$ with one object and automorphism group $G$, so that $\pi_1(BG) = G$ and all higher $\pi_n$ vanish.

**Targets (Output Amplification)**

The bare conclusion is "$\infty$-groupoids $=$ spaces". Combined with other facts it does much more.

Combine the conclusion with **the existence of homotopy groups**. Since an $\infty$-groupoid is a space, it has homotopy groups $\pi_n$, and these become *invariants of the higher category*. The further result is that an $\infty$-groupoid is determined (up to equivalence) by its Postnikov tower — its homotopy groups and the $k$-invariants gluing them — so the classification of $\infty$-groupoids is the classification of homotopy types, a known (if hard) theory. This is non-obvious because it imports an entire classification machinery into category theory for free.

Combine the conclusion with **a definition of weak ω-category**. Restricting any proposed definition to its invertible objects must reproduce homotopy types; this is the *target as test*. The further result $E$ is a *rejection criterion*: a definition whose groupoidal part gives the wrong answer (for instance, the strict ω-groupoids, which fail to model $S^2$) is thereby shown to be inadequate as a definition of *weak* higher category. This is non-obvious because it turns a positive equivalence into a negative diagnostic.

Combine the conclusion with **the loop-space functor**. For a pointed $\infty$-groupoid (pointed space) $X$, the loop space $\Omega X$ is again an $\infty$-groupoid, and delooping/looping become categorical operations. The further result is the **stabilisation** picture: iterating $\Omega$ and asking what is preserved produces spectra and the stable homotopy category, so the homotopy hypothesis is the entry point to **stable** higher category theory. This is useful because it locates spectra — the central objects of modern homotopy theory — as a limit of the groupoidal world.

---

# Why Is It True

Forget the formalism and look at what the singular complex of a space *is*. Take a space $T$. Its points are the $0$-simplices; a continuous map of the interval $\Delta^1_{\mathrm{top}} \to T$, i.e. a path, is a $1$-simplex; a continuous map of the triangle $\Delta^2_{\mathrm{top}} \to T$ is a $2$-simplex, and so on. This is the [[Def - Simplicial Set|simplicial set]] $\mathrm{Sing}(T)$, and the claim is that it *is* the fundamental $\infty$-groupoid of $T$ — objects are points, $1$-cells are paths, $2$-cells are homotopies-of-paths, with everything invertible because a path can be run backwards. The reason this should be an $\infty$-groupoid is geometric and immediate: **every horn fills because you can always extend a partial map of a triangle's boundary to the whole filled-in triangle, since the topological horn $\Lambda^n_i$ is a deformation retract of the solid simplex $\Delta^n$.** That one fact — the horn retracts onto the simplex — is the entire reason $\mathrm{Sing}(T)$ is a Kan complex, and a Kan complex is precisely the simplicial notion of $\infty$-groupoid.

> The homotopy hypothesis is true for the simplicial model because $\mathrm{Sing}(T)$ is a Kan complex *for free* — the topological horn deformation-retracts onto the solid simplex, so filling is automatic — and because $\mathrm{Sing}$ and $|{-}|$ lose no homotopical information.

That composability never fails, that composites are unique up to homotopy, that paths invert — all of this is *inherited from the topology of the simplex* and costs nothing to verify. Going the other way, geometric realisation $|X|$ glues topological simplices according to the combinatorics of $X$, and Milnor's theorem says the unit $X \to \mathrm{Sing}|X|$ and counit $|\mathrm{Sing}(T)| \to T$ are weak homotopy equivalences: nothing is lost in either direction. So $\mathrm{Sing}$ and $|{-}|$ are mutually inverse on homotopy categories, which is the theorem.

The deep point — and the reason the *algebraic* version is hard — is that this argument leans entirely on invertibility being *built into the geometry*. In the simplicial world, the invertibility of cells is the all-horns Kan condition, and it holds automatically for $\mathrm{Sing}(T)$. In an algebraic (globular) definition, you do not get invertibility for free: you have only *weak* inverses, specified cell by cell, and you must *prove* they assemble into the genuine homotopical inverses that a space has. Showing that the algebraically-defined weak inverses cohere into the homotopy type of a space — that the algebraic ω-groupoid "is" a space — is exactly the unproven content of the conjecture. The simplicial models finesse this by *defining* $\infty$-groupoid as "Kan complex", at which point the hypothesis is Milnor's theorem; the algebraic models earn it the hard way, or not yet at all.

---

# What Makes This Hard

The conceptual statement is easy to believe and easy to prove *in the simplicial model*, where "$\infty$-groupoid" is defined as "Kan complex" and the theorem is Milnor's. The genuine difficulty is entirely on the **algebraic** side: there, an ω-groupoid is an algebra for a coherator with only *weak, chosen* inverses in each dimension, and one must prove these assemble into a structure with the homotopy type of a space — equivalently, that the algebraically-defined homotopy groups satisfy the right relations and that no homotopical information is lost or spuriously added. Most attempts get stuck precisely at coherence: showing the infinite tower of weak inverses and weak units fits together into honest invertibility. The common error is to conflate the two situations — to "prove" the hypothesis by silently working in the simplicial model and then claim it for the algebraic one, which is exactly the gap that keeps the general statement a conjecture.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire (simplicial) proof.**

**High-level strategy:**
Work in the simplicial model, where $\infty$-groupoid $=$ Kan complex. Establish two things: that $\mathrm{Sing}(T)$ is always a Kan complex (so the right adjoint lands among $\infty$-groupoids), and that the adjunction $|{-}| \dashv \mathrm{Sing}$ is a Quillen equivalence (so it induces an equivalence of homotopy categories). The first is geometry of the simplex; the second is Milnor's theorem plus the model structures.

**Subgoal decomposition:**

1. **$\mathrm{Sing}(T)$ is a Kan complex.** Show every horn $\Lambda^n_i \to \mathrm{Sing}(T)$ fills.
   - *Hint:* A horn in $\mathrm{Sing}(T)$ is a continuous map from the topological horn $|\Lambda^n_i|$ to $T$; use that $|\Lambda^n_i|$ is a deformation retract of $|\Delta^n|$ to extend the map.
   - *Why needed:* It puts the right adjoint into the category of $\infty$-groupoids, so the adjunction is between the right things.

2. **$|{-}| \dashv \mathrm{Sing}$ is a Quillen adjunction.** Show $|{-}|$ is left Quillen.
   - *Hint:* Realisation sends generating (trivial) cofibrations of $\mathbf{sSet}$ (boundary and horn inclusions) to (trivial) cofibrations of spaces (relative CW inclusions).
   - *Why needed:* A [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]] is the precondition for asking whether it is a Quillen equivalence.

3. **The unit is a weak equivalence on cofibrant objects.** Show $X \to \mathrm{Sing}|X|$ is a weak homotopy equivalence for every simplicial set $X$.
   - *Hint:* Reduce to $X = \Delta^n$ by skeletal induction and gluing; for $\Delta^n$ both sides are contractible.
   - *Why needed:* The unit being an equivalence is half the definition of Quillen equivalence.

4. **The counit is a weak equivalence on fibrant objects.** Show $|\mathrm{Sing}(T)| \to T$ is a weak homotopy equivalence for every space $T$.
   - *Hint:* This is Milnor's theorem; both sides have the same singular homology and $\pi_n$ by construction, and a $\pi_*$-iso between CW-ish spaces is a homotopy equivalence (Whitehead).
   - *Why needed:* Together with step 3 it gives a Quillen equivalence, hence the equivalence of homotopy theories.

---

# Lemma Decomposition

> [!note]- Lemma 1: The singular complex of a space is a Kan complex
> **Statement:** For any [[Def - Topological Space|topological space]] $T$, the simplicial set $\mathrm{Sing}(T)$ satisfies the Kan condition: every horn $\Lambda^n_i \to \mathrm{Sing}(T)$, $0 \le i \le n$, extends to $\Delta^n \to \mathrm{Sing}(T)$.
>
> **Hint:** Adjointly, a horn is a continuous map $|\Lambda^n_i| \to T$; the topological horn deformation-retracts onto $|\Delta^n|$.
>
> **Why needed:** It is the statement "$\mathrm{Sing}(T)$ is an $\infty$-groupoid", placing the right adjoint among the objects the theorem is about.
>
> > [!note]- Full proof
> > By the realisation–singular adjunction, a map of simplicial sets $\Lambda^n_i \to \mathrm{Sing}(T)$ corresponds to a continuous map $g : |\Lambda^n_i| \to T$, and an extension to $\Delta^n$ corresponds to a continuous extension to $|\Delta^n|$. The geometric horn $|\Lambda^n_i|$ — the union of all faces of the solid simplex $|\Delta^n| = \{(t_0,\dots,t_n) : t_j \ge 0, \sum t_j = 1\}$ except the $i$th — is a strong deformation retract of $|\Delta^n|$: there is a continuous $r : |\Delta^n| \to |\Lambda^n_i|$ and a homotopy $|\Delta^n| \times [0,1] \to |\Delta^n|$ from the identity to (inclusion $\circ\, r$) fixing $|\Lambda^n_i|$ (project radially from the barycentre of the missing face). Then $g \circ r : |\Delta^n| \to T$ extends $g$, and its adjoint is the required filler. This holds for *all* $i$, inner and outer, because the retraction exists for every face — which is exactly why $\mathrm{Sing}(T)$ is a Kan complex (all horns) and not merely a quasi-category (inner horns). $\square$

> [!note]- Lemma 2: Geometric realisation is left Quillen
> **Statement:** $|{-}| : \mathbf{sSet} \to \mathbf{Top}$ sends the generating cofibrations $\partial\Delta^n \hookrightarrow \Delta^n$ to relative CW inclusions and the generating trivial cofibrations (horn inclusions) $\Lambda^n_i \hookrightarrow \Delta^n$ to trivial cofibrations of spaces; hence $|{-}|$ is a left [[Def - Quillen Adjunction and Quillen Equivalence|Quillen functor]] with right adjoint $\mathrm{Sing}$.
>
> **Hint:** Realisation is a left adjoint, so it preserves colimits and in particular the pushouts that build cofibrations; compute it on the generators directly.
>
> **Why needed:** It makes $|{-}| \dashv \mathrm{Sing}$ a Quillen adjunction, the precondition for being a Quillen equivalence.
>
> > [!note]- Full proof
> > $|\Delta^n| = \Delta^n_{\mathrm{top}}$ and $|\partial\Delta^n| = \partial\Delta^n_{\mathrm{top}} = S^{n-1}$, so $|\partial\Delta^n \hookrightarrow \Delta^n|$ is the inclusion $S^{n-1} \hookrightarrow D^n$, a generating cofibration of $\mathbf{Top}$ — hence a cofibration. Because $|{-}|$ is a left adjoint it preserves the pushouts and transfinite compositions out of which all cofibrations are built (the [[Def - Simplicial Set|simplicial set]] cofibrations are the monomorphisms, generated by the $\partial\Delta^n \hookrightarrow \Delta^n$), so $|{-}|$ sends cofibrations to cofibrations. For the horns, $|\Lambda^n_i| \hookrightarrow |\Delta^n|$ is the inclusion of a deformation retract (Lemma 1's retraction), hence a trivial cofibration. Therefore $|{-}|$ preserves cofibrations and trivial cofibrations and is left Quillen. $\square$

> [!note]- Lemma 3: The counit is a weak homotopy equivalence (Milnor)
> **Statement:** For every space $T$ the counit $\varepsilon_T : |\mathrm{Sing}(T)| \to T$ is a weak homotopy equivalence; for every simplicial set $X$ the unit $\eta_X : X \to \mathrm{Sing}|X|$ is a weak equivalence.
>
> **Hint:** $\mathrm{Sing}(T)$ has, by construction, the same singular homology and homotopy groups as $T$; invoke Whitehead's theorem after checking $\pi_*$.
>
> **Why needed:** Unit and counit both being weak equivalences is the definition of a Quillen equivalence, giving the equivalence of homotopy theories.
>
> > [!note]- Full proof
> > By definition $\mathrm{Sing}(T)_n$ is the set of singular $n$-simplices of $T$, so the simplicial homotopy groups $\pi_n(\mathrm{Sing}(T))$ are *defined* to be the singular homotopy groups $\pi_n(T)$, and likewise for homology; the counit $\varepsilon_T$ induces these identifications, hence is a $\pi_*$-isomorphism, i.e. a weak homotopy equivalence. For the unit, both $X$ and $\mathrm{Sing}|X|$ are Kan-replaced and one checks $\eta$ is a weak equivalence on the generators $\Delta^n$ (both contractible) and propagates along skeleta by gluing, using that realisation and $\mathrm{Sing}$ preserve the relevant homotopy pushouts. A left Quillen functor whose derived unit and counit are weak equivalences is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]; therefore $|{-}| \dashv \mathrm{Sing}$ is one, and it induces an equivalence $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof (simplicial form)
> We prove the simplicial form: $|{-}| : \mathbf{sSet} \rightleftarrows \mathbf{Top} : \mathrm{Sing}$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] for the Kan–Quillen and Quillen model structures, whence Kan complexes (the fibrant objects, $=$ $\infty$-groupoids) model homotopy types.
>
> **Step 0 — the adjunction and the model structures.** Geometric realisation $|{-}|$ is the left Kan extension of $[n] \mapsto \Delta^n_{\mathrm{top}}$ along the Yoneda embedding, with right adjoint $\mathrm{Sing}(T)_n = \mathrm{Top}(\Delta^n_{\mathrm{top}}, T)$; this is a genuine adjunction $|{-}| \dashv \mathrm{Sing}$. Equip $\mathbf{Top}$ with the Quillen model structure (weak equivalences $=$ weak homotopy equivalences, fibrations $=$ Serre fibrations, cofibrations $=$ retracts of relative cell complexes) and $\mathbf{sSet}$ with the Kan–Quillen model structure (cofibrations $=$ monos, fibrations $=$ Kan fibrations, weak equivalences $=$ maps whose realisation is a weak homotopy equivalence). The fibrant objects of $\mathbf{sSet}$ are exactly the **[[Def - Kan Complex and the Nerve|Kan complexes]]**, which is our model of $\infty$-groupoid.
>
> **Step 1 — $\mathrm{Sing}$ lands in $\infty$-groupoids.** By Lemma 1, $\mathrm{Sing}(T)$ is a Kan complex for every $T$, so the right adjoint takes values among $\infty$-groupoids.
>
> **Step 2 — the adjunction is Quillen.** By Lemma 2, $|{-}|$ preserves cofibrations and trivial cofibrations, so $|{-}| \dashv \mathrm{Sing}$ is a Quillen adjunction.
>
> **Step 3 — it is a Quillen equivalence.** By Lemma 3, for cofibrant $X$ (every simplicial set is cofibrant) the unit $X \to \mathrm{Sing}|X|$ is a weak equivalence, and for every $T$ the counit $|\mathrm{Sing}(T)| \to T$ is a weak homotopy equivalence. These are exactly the conditions for a Quillen equivalence.
>
> **Step 4 — conclude.** A Quillen equivalence induces an equivalence of homotopy categories $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$, restricting to an equivalence between fibrant objects up to weak equivalence: Kan complexes (= $\infty$-groupoids) and homotopy types. Identifying $\Pi_\infty(T) := \mathrm{Sing}(T)$, this is the homotopy hypothesis in the simplicial model. $\blacksquare$
>
> **Remark (the algebraic case).** For an algebraic definition of weak ω-groupoid (algebras for a Grothendieck–Maltsiniotis coherator), one must construct a functor to spaces and prove it an equivalence without the free invertibility of Lemma 1. This is open in general; partial results exist for low truncations and for specific coherators. The simplicial proof above does *not* transfer, because it uses the Kan (all-horns) condition, which the algebraic models do not satisfy on the nose.

---

# Cross-Field Exercise Suggestions

**Classifying spaces of groups (algebra ↔ topology).** For a discrete group $G$, the $\infty$-groupoid $BG$ with one object and automorphisms $G$ realises to the classifying space $BG$ with $\pi_1 = G$ and all higher $\pi_n = 0$. Use the homotopy hypothesis to show that group cohomology $H^*(G;A)$ equals the singular cohomology $H^*(BG;A)$ — the categorical $\infty$-groupoid and the topological space carry the same cohomology. The application is non-obvious because group cohomology is defined purely algebraically (derived functors of invariants) yet computes a topological invariant.

**Eilenberg–MacLane spaces and cohomology operations (homotopy theory).** The space $K(A,n)$ is the $\infty$-groupoid with a single nontrivial homotopy group $A$ in dimension $n$; the homotopy hypothesis lets one read $[X, K(A,n)] = H^n(X;A)$ as a statement about maps of $\infty$-groupoids. Cohomology operations then become *natural transformations of representable $\infty$-groupoid-valued functors*, which is why they are classified by the cohomology of the $K(A,n)$ themselves. The non-obvious recognition is that a cohomology class is a morphism of higher groupoids.

**Homotopy type theory and univalence (logic / type theory).** In **homotopy type theory** every type is a weak ω-groupoid (its iterated identity types), so the homotopy hypothesis predicts that types model spaces. Use this to interpret the **univalence axiom** — equivalent types are equal — as the type-theoretic shadow of "equivalent $\infty$-groupoids are connected by a path in the $\infty$-groupoid of all $\infty$-groupoids". The application is non-obvious because a syntactic logical axiom turns out to be a homotopy-theoretic statement about the space of spaces.

---

# Bridges

- **[[Def - Kan Complex and the Nerve|Kan complexes]] as $\infty$-groupoids** — the load-bearing identification. A Kan complex is a [[Def - Simplicial Set|simplicial set]] where *every* horn fills, inner and outer; outer-horn filling is the simplicial expression of invertibility (it lets you solve $h = ? \circ f$, which needs $f$ invertible). So "all horns fill" means "all morphisms invert", i.e. $\infty$-groupoid. The homotopy hypothesis in the simplicial model is then nothing but the statement that the fibrant simplicial sets are the homotopy types, which is Milnor's Quillen equivalence — the bridge is that the Kan condition *is* the groupoidal condition.

- **[[Def - Quasi-Category|Quasi-categories]] and the inner/outer line** — the non-invertible generalisation. Dropping outer-horn filling from a Kan complex gives a quasi-category: an $(\infty,1)$-category, with possibly non-invertible morphisms. The homotopy hypothesis is the *boundary case* of this picture — the case where outer horns do fill, so everything is invertible and the $\infty$-category is an $\infty$-groupoid, i.e. a space. The whole subject sits between these: $\infty$-groupoids (all horns, = spaces) at one end, $\infty$-categories (inner horns) at the other.

- **The [[Thm - Comparison of Models for (∞,1)-Categories|comparison theorem]]** — the $(\infty,1)$ analogue. Where the homotopy hypothesis identifies $(\infty,0)$-categories with spaces, the comparison theorem identifies the various models of $(\infty,1)$-categories with one another. The two together are the foundational sanity of the subject: the simplest higher categories are spaces (a known theory), and the next-simplest are modelled uniquely up to equivalence.

- **Strict ω-groupoids and crossed complexes** — the cautionary boundary. Strict $\infty$-groupoids correspond (Brown–Higgins) to **crossed complexes**, which model only *homotopy types with vanishing Whitehead products* — strictly fewer than all spaces ($S^2$ is not among them). This is precisely why "weak" is essential: the homotopy hypothesis is *false* for strict ω-groupoids, and that failure is the sharpest evidence that the weakening built into every definition in this chapter is mathematically forced, not a matter of taste.

---

# Unlocked by This

> [!tip] Stable Homotopy Theory and Spectra *(from Higher Algebra)*
> Iterating the loop-space functor on pointed $\infty$-groupoids (pointed spaces) and asking what survives stabilisation produces **spectra** and the **stable homotopy category**. The homotopy hypothesis is the entry point: it identifies the unstable groupoidal world with spaces, and stabilisation then carves out the stable one — the home of generalised cohomology theories.

> [!tip] The Grothendieck–Maltsiniotis Program *(from Higher Algebra)*
> Grothendieck's *Pursuing Stacks* proposed defining weak ω-groupoids algebraically (via **coherators**) so that the homotopy hypothesis would hold *by construction*. Proving it for these algebraic definitions — that algebraically-defined weak ω-groupoids model homotopy types — is one of the central open problems of higher category theory, with partial results by Maltsiniotis, Ara, and others.
