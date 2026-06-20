---
type: theorem
subject: model-categories
prereqs:
  - "Def - Stable Model Category"
  - "Def - Triangulated Category"
  - "Thm - The Homotopy Category of a Stable Model Category is Triangulated"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$\mathcal{M}$ is a pointed [[Def - Model Category|model category]] with zero object $0$, suspension $\Sigma$, loop $\Omega$, and adjunction $\Sigma \dashv \Omega$ on $\mathrm{Ho}(\mathcal{M})$. The homotopy category $\mathrm{Ho}(\mathcal{M})$, equipped with its compatible cofiber and fiber sequences and the adjunction, is a **pre-triangulated category** — all the data of a [[Def - Triangulated Category|triangulated category]] except that $\Sigma$ need not be invertible. The pre-triangulated structure and the suspension/loop apparatus come from the previous chapter on **pointed model categories and cofiber/fiber sequences** (named in bold, not yet written up). The full registry is on [[Model Categories — Stable Model Categories and Triangulated Categories]].

---

# Statement

> **Theorem (Characterization of stable model categories).** Let $\mathcal{M}$ be a pointed [[Def - Model Category|model category]], so that $\mathrm{Ho}(\mathcal{M})$ is a **pre-triangulated category**. The following are equivalent:
> 1. $\mathcal{M}$ is a [[Def - Stable Model Category|stable model category]] (the suspension $\Sigma$ is an equivalence on $\mathrm{Ho}(\mathcal{M})$).
> 2. The loop functor $\Omega$ is an equivalence on $\mathrm{Ho}(\mathcal{M})$.
> 3. The unit $\eta \colon \mathrm{id} \to \Omega\Sigma$ and counit $\varepsilon \colon \Sigma\Omega \to \mathrm{id}$ of $\Sigma \dashv \Omega$ are natural isomorphisms.
> 4. The pre-triangulated category $\mathrm{Ho}(\mathcal{M})$ is a [[Def - Triangulated Category|triangulated category]] (with shift $\Sigma$ and distinguished triangles the cofiber sequences).
>
> In words: **a pre-triangulated category is triangulated if and only if its suspension is invertible**, and this happens exactly when the model category is stable.

---

# Motivation

The previous theorem proved one direction — stable model categories have triangulated homotopy categories. But it left the natural question open: is stability *necessary*, or merely sufficient? Could some non-stable pointed model category sneak in a triangulated structure by another route? This theorem answers no, and in doing so it pins down stability as the *exact* boundary between two worlds: the directional, unstable world of pointed homotopy theory and the symmetric, linear, triangulated world.

The phrasing "pre-triangulated $+$ $\Sigma$ invertible $\Leftrightarrow$ triangulated" is what makes the theorem a genuine *characterization* rather than a one-way implication. It says the entire content of "triangulated" beyond "pre-triangulated" is a single invertibility condition. This is enormously clarifying: it tells you that you never need to verify TR1–TR4 from scratch for a pointed model category — the pre-triangulated structure already supplies their pre-images — and that the only thing standing between any pointed homotopy theory and a triangulated one is whether you can desuspend.

It also explains *why* the canonical non-examples fail. Pointed spaces are pre-triangulated but not triangulated, and the theorem locates the failure precisely: $\Sigma$ is not invertible there. Conversely it explains why stabilization works: stabilization is, by definition, the operation of forcing $\Sigma$ to be invertible, so the theorem guarantees that the result is triangulated.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a pointed model category" (so $\mathrm{Ho}(\mathcal{M})$ is pre-triangulated) together with one of the equivalent invertibility conditions. The skill is recognizing each disguised form of "$\Sigma$ invertible."

The first disguised source is **"the unit $X \to \Omega\Sigma X$ is an isomorphism for all $X$" stated as a stabilization or connectivity statement**. In topology, the Freudenthal suspension theorem says the unit is an isomorphism in a range; demanding it in *all* degrees is exactly stability. The bridge $B \to A$ is "unit iso everywhere $=$ $\Sigma$ fully faithful, and with the counit also iso, $\Sigma$ an equivalence." *Example problem:* show spectra are stable by checking the unit $\mathbb{S} \to \Omega\Sigma\mathbb{S}$ is an isomorphism — which is built into the definition of spectra.

The second disguised source is **"cofiber sequences agree with fiber sequences."** If a problem tells you that the homotopy cofiber of a map equals (up to shift) its homotopy fiber, that is condition (3) in disguise, because cofibers are built from $\Sigma$ and fibers from $\Omega$. The bridge is "cofiber $=$ fiber $\Rightarrow$ $\Sigma$ and $\Omega$ mutually inverse." *Example problem:* in $D(R)$, observe that the mapping cone and mapping fiber of a chain map agree up to shift, concluding stability.

The third disguised source is **"the shift on the homotopy category is invertible,"** stated about a concrete shift operator. Whenever the homotopy category carries a manifestly invertible shift — the degree shift of complexes, the formal suspension of spectra — condition (4)'s shift requirement is met, and the theorem upgrades pre-triangulated to triangulated. The bridge is "invertible shift operator $=$ $\Sigma$ an automorphism." *Example problem:* recognize $D(R)$ as triangulated purely from the invertibility of $X \mapsto X[1]$.

**Targets (Output Amplification)**

The conclusion is a four-way equivalence. Combined with other facts it does more than label a category.

Combine with **a Quillen equivalence**. Since all four conditions are homotopy-invariant, a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] transports stability and hence triangulation. The further result $E$ is that you may verify the invertibility of $\Sigma$ in *whichever model is easiest* and conclude triangulation for all equivalent models. Nonobvious because triangulation looks like structure on a specific category, yet it is actually a transportable property.

Combine with **a no-go observation about a candidate category**. If you can show $\Sigma$ is *not* essentially surjective in some pointed model category, the theorem's contrapositive immediately gives "not triangulated," with no need to hunt for a failing instance of TR1–TR4. The further result is a clean impossibility proof. Nonobvious because it reduces "this category is not triangulated" — a statement about four axioms — to a single property of one functor.

Combine with **the main theorem and a generator**. Conditions (1) and (4) together feed the pipeline: stable $\Rightarrow$ triangulated $\Rightarrow$ (with a compact generator) modules over a ring spectrum. The further result is that recognizing stability is the *first* step of identifying a homotopy theory as algebra. Nonobvious because a single invertibility check unlocks the entire Schwede–Shipley machinery downstream.

---

# Why Is It True

The equivalence of (1), (2), (3) is pure adjunction formalism, and the equivalence with (4) is where the homotopy theory lives.

For the formal part: $\Sigma \dashv \Omega$ is an adjunction, and there is a general categorical fact that **an adjunction is an adjoint equivalence iff its unit and counit are isomorphisms iff either functor is an equivalence**. A left adjoint that is an equivalence has its right adjoint as an inverse equivalence; so (1) $\Leftrightarrow$ (2) $\Leftrightarrow$ (3) needs nothing beyond the formal theory of adjoint equivalences. There is no homotopy theory in this part at all.

For the substantive part, (1) $\Leftrightarrow$ (4): the previous theorem already gives (1) $\Rightarrow$ (4). The new content is (4) $\Rightarrow$ (1). Suppose $\mathrm{Ho}(\mathcal{M})$ is triangulated with shift $\Sigma$. By the very definition of a triangulated category the shift is an **automorphism** — that is the standing requirement, the thing distinguishing a triangulated category from a mere pre-triangulated one. But "the shift $\Sigma$ is an automorphism of $\mathrm{Ho}(\mathcal{M})$" is, word for word, the definition of stability. So triangulation *forces* stability because triangulation has invertibility of the shift baked into it.

The one-line mechanism: **a triangulated category is by definition equipped with an invertible shift, and the shift of $\mathrm{Ho}(\mathcal{M})$ is the suspension — so "triangulated" cannot hold without "$\Sigma$ invertible," which is exactly "stable."** Everything else (TR1–TR3, the octahedron) the pre-triangulated structure already had; the single new bit that "triangulated" demands over "pre-triangulated" is the invertibility, and that bit is stability.

---

# What Makes This Hard

The conceptual trap is thinking the theorem is harder than it is: the equivalence (1)–(3) is *formal* (adjoint-equivalence yoga) and the equivalence with (4) is *almost definitional* (invertible shift is built into "triangulated"), so the difficulty is recognizing that there is *not* a deep computation hiding here — the depth is all in the previous theorem's construction of the pre-triangulated structure. The genuine subtlety is keeping straight what "pre-triangulated" already provides (rotation in the *forward* direction, the octahedron) versus what fails without stability (rotation *backward*, which needs $\Sigma^{-1}$). The most common error is to try to prove (4) $\Rightarrow$ (1) by re-deriving the axioms instead of simply reading off that the triangulated shift is an automorphism.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Split into the formal equivalence (1) $\Leftrightarrow$ (2) $\Leftrightarrow$ (3), proved by adjoint-equivalence formalism, and the equivalence (1) $\Leftrightarrow$ (4). For the latter, get (1) $\Rightarrow$ (4) from the previous theorem, and (4) $\Rightarrow$ (1) by observing that a triangulated category's shift is by definition invertible, which is stability.

**Subgoal decomposition:**

1. **(1) $\Leftrightarrow$ (3).** $\Sigma$ is an equivalence iff unit and counit are isos.
   - *Hint:* This is the standard characterization of an adjoint equivalence; one direction is "an equivalence's adjoint is its inverse," the other is "iso unit/counit $\Rightarrow$ mutually inverse."
   - *Why needed:* Reduces the property "equivalence" to a pointwise iso condition usable in examples.

2. **(1) $\Leftrightarrow$ (2).** $\Sigma$ is an equivalence iff $\Omega$ is.
   - *Hint:* A right adjoint to an equivalence is an equivalence (its inverse), and vice versa.
   - *Why needed:* Lets you check invertibility on whichever of $\Sigma, \Omega$ is more accessible.

3. **(1) $\Rightarrow$ (4).** Stable implies triangulated.
   - *Hint:* This is exactly the previous theorem.
   - *Why needed:* Supplies the "sufficient" half.

4. **(4) $\Rightarrow$ (1).** Triangulated implies stable.
   - *Hint:* By definition a triangulated category's shift is an automorphism; the shift here is $\Sigma$, and "$\Sigma$ an automorphism" is stability.
   - *Why needed:* Supplies the "necessary" half, turning the implication into a characterization.

---

# Lemma Decomposition

> [!note]- Lemma 1: An adjunction is an adjoint equivalence iff unit and counit are isomorphisms
> **Statement:** For an adjunction $F \dashv G$ with unit $\eta$ and counit $\varepsilon$, the following are equivalent: $F$ is an equivalence; $G$ is an equivalence; $\eta$ and $\varepsilon$ are natural isomorphisms.
>
> **Hint:** If $\eta, \varepsilon$ are isos then $G$ is a two-sided inverse to $F$; conversely an equivalence's adjoint is its quasi-inverse, forcing the triangle identities to make $\eta, \varepsilon$ isos.
>
> **Why needed:** It is the entire content of (1) $\Leftrightarrow$ (2) $\Leftrightarrow$ (3); the homotopy theory contributes nothing here.
>
> > [!note]- Full proof
> > ($\eta, \varepsilon$ iso $\Rightarrow$ $F$ equivalence.) The triangle identities $\varepsilon F \circ F\eta = \mathrm{id}_F$ and $G\varepsilon \circ \eta G = \mathrm{id}_G$ together with $\eta, \varepsilon$ being isomorphisms exhibit $G$ as a two-sided inverse of $F$ up to natural isomorphism: $GF \cong \mathrm{id}$ via $\eta^{-1}$ and $FG \cong \mathrm{id}$ via $\varepsilon$. Hence $F$ is an equivalence with quasi-inverse $G$.
> >
> > ($F$ equivalence $\Rightarrow$ $\eta, \varepsilon$ iso.) If $F$ is an equivalence, it has a quasi-inverse $F'$ with $F'F \cong \mathrm{id} \cong FF'$. A right adjoint is unique up to natural isomorphism, so $G \cong F'$, whence $GF \cong \mathrm{id}$ and $FG \cong \mathrm{id}$. Under these isomorphisms the unit and counit become the identity natural transformations, so $\eta$ and $\varepsilon$ are isomorphisms. The case for $G$ is symmetric. $\blacksquare$

> [!note]- Lemma 2: The shift of a triangulated category is an automorphism
> **Statement:** In any triangulated category, the shift functor $\Sigma = [1]$ is an automorphism (equivalence) of the category; equivalently $\Sigma^{-1}$ exists.
>
> **Hint:** This is part of the *definition* of a triangulated category — read it off the axioms.
>
> **Why needed:** It is the engine of (4) $\Rightarrow$ (1): triangulation includes invertibility of the shift, which is stability.
>
> > [!note]- Full proof
> > By definition (see [[Def - Triangulated Category]]) a triangulated category comes equipped with an *additive automorphism* $\Sigma$; "automorphism" means $\Sigma$ is invertible (an equivalence with a strict or coherent inverse $\Sigma^{-1}$). Rotation (TR2) in the *backward* direction, $\Sigma^{-1}Z \to X \to Y \to Z$, already presupposes $\Sigma^{-1}$, so even the axioms as used require invertibility. Hence the shift is an automorphism. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{M}$ be a pointed model category, so $\mathrm{Ho}(\mathcal{M})$ is pre-triangulated with adjunction $\Sigma \dashv \Omega$.
>
> **Step 0 — preconditions.** Pointedness gives the zero object and the functors $\Sigma, \Omega$ with the adjunction $\Sigma \dashv \Omega$ and the pre-triangulated cofiber/fiber sequences (previous chapter). All four conditions are statements about $\mathrm{Ho}(\mathcal{M})$, hence homotopy-invariant.
>
> **Step 1 — (1) $\Leftrightarrow$ (2) $\Leftrightarrow$ (3).** Apply Lemma 1 to $F = \Sigma$, $G = \Omega$: $\Sigma$ is an equivalence iff $\Omega$ is iff the unit and counit are isomorphisms. This is precisely the equivalence of conditions (1), (2), (3).
>
> **Step 2 — (1) $\Rightarrow$ (4).** This is the content of [[Thm - The Homotopy Category of a Stable Model Category is Triangulated|the previous theorem]]: if $\Sigma$ is an equivalence then $\mathrm{Ho}(\mathcal{M})$ is triangulated with shift $\Sigma$ and distinguished triangles the cofiber sequences. (The previous theorem uses exactly the invertibility of $\Sigma$ to install the triangulated axioms on top of the pre-triangulated structure.)
>
> **Step 3 — (4) $\Rightarrow$ (1).** Suppose $\mathrm{Ho}(\mathcal{M})$ is triangulated, with the triangulated shift being the suspension $\Sigma$ (as in (4)). By Lemma 2 the shift of any triangulated category is an automorphism, so $\Sigma$ is an equivalence on $\mathrm{Ho}(\mathcal{M})$. By the definition of stability (invertibility of $\Sigma$), $\mathcal{M}$ is stable, which is (1).
>
> **Step 4 — conclude.** Steps 1–3 give (1) $\Leftrightarrow$ (2) $\Leftrightarrow$ (3) and (1) $\Leftrightarrow$ (4), so all four conditions are equivalent. Hence a pointed model category is stable — equivalently its pre-triangulated homotopy category is triangulated — exactly when the suspension is invertible. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebra — recognizing $D(R)$ as triangulated without checking axioms.** Show that $\mathbf{Ch}(R)$ is stable by verifying only that the degree shift $X \mapsto X[1]$ is invertible on $D(R)$, then invoke the characterization to conclude $D(R)$ is triangulated. Nonobvious because the naive approach re-checks TR1–TR4; the characterization reduces it to one invertibility.

**Topology — proving pointed spaces are not triangulated in one line.** Show that pointed [[Def - Topological Space|spaces]] are not stable by exhibiting a space that is not a suspension (so $\Sigma$ is not essentially surjective), then use the contrapositive of (4) $\Leftrightarrow$ (1) to conclude their homotopy category is not triangulated. Nonobvious because "not triangulated" sounds like it requires falsifying an axiom, whereas one failed property of $\Sigma$ suffices.

**Higher algebra — transporting stability across models of spectra.** Given that symmetric spectra are Quillen equivalent to classical spectra, use homotopy-invariance of the four conditions to conclude that symmetric spectra are stable and their homotopy category is triangulated and equivalent to $\mathcal{SH}$. Nonobvious because it shows triangulation need only be checked in one convenient model.

---

# Bridges

- **[[Thm - The Homotopy Category of a Stable Model Category is Triangulated|The homotopy category of a stable model category is triangulated]]** — this theorem's other half. That result is the (1) $\Rightarrow$ (4) implication; the present theorem supplies (4) $\Rightarrow$ (1) and the formal equivalences (1)–(3), upgrading a one-way implication into a four-way characterization. Read together, they assert that "stable model category" and "model category with triangulated homotopy category" are the same notion.

- **[[Def - Stable Model Category|Stable model category]]** — the definition this theorem characterizes. The definition is "$\Sigma$ an equivalence"; the theorem shows this single clause is equivalent to the full triangulated structure, justifying why a one-clause definition captures so much. It also validates the alternative formulations listed on the definition page (adjoint equivalence, cofiber $=$ fiber, infinite desuspendability) as genuinely equivalent.

- **Pre-triangulated category** (previous chapter, not yet written up) — the structure the theorem upgrades. A pre-triangulated category has every triangulated axiom *except* invertibility of the shift; the characterization theorem is precisely the statement that adding invertibility is the one and only step to triangulation. This is why the previous chapter introduced "pre-triangulated" at all — it is exactly the intermediate stage that makes the characterization clean.

- **Stabilization** — the construction the theorem justifies. Stabilization forces $\Sigma$ to become invertible; by this theorem the stabilized category is automatically triangulated, which is *why* stabilization is the universal way to produce a triangulated category from a pointed one (spectra from spaces being the prototype).

---

# Unlocked by This

> [!tip] The Universal Property of Stabilization *(from Higher Category Theory)*
> Because triangulation is equivalent to invertibility of $\Sigma$, the operation **stabilization** — universally forcing $\Sigma$ to be invertible — has a clean universal property: it is the initial stable model category (or **stable ∞-category**) under a given pointed one. Spectra are the stabilization of pointed spaces; this is the precise sense in which the stable homotopy category is "the universal place where suspension is invertible."

> [!tip] Recollements and Gluing of Triangulated Categories *(from Derived Algebra)*
> Once stability is characterized by invertible $\Sigma$, one can ask when a triangulated category is **glued** from two others along a **recollement** (the triangulated analogue of an open–closed decomposition of a space). This is the structural theory behind the derived categories of stratified spaces and perverse sheaves, and it presupposes exactly the triangulated structure this theorem certifies.
