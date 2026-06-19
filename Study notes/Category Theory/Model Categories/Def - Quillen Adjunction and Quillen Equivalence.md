---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ and $\mathcal{N}$ are model categories and $F \dashv U$ is an [[Def - Adjunction|adjunction]] with $F : \mathcal{M} \to \mathcal{N}$ the **left adjoint** and $U : \mathcal{N} \to \mathcal{M}$ the **right adjoint**, expressed by a natural isomorphism $\varphi : \mathcal{N}(FA, B) \xrightarrow{\cong} \mathcal{M}(A, UB)$. The maps $\eta : \mathrm{id}_{\mathcal{M}} \Rightarrow UF$ and $\varepsilon : FU \Rightarrow \mathrm{id}_{\mathcal{N}}$ are the [[Def - Unit and Counit of an Adjunction|unit and counit]]. We write $\tilde{h} = \varphi(h)$ for the **adjunct** (transpose) of a map $h : FA \to B$, so $\tilde{h} : A \to UB$. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

This is a compound page: it defines two interlocking notions — the **Quillen adjunction** (a map of model categories) and the **Quillen equivalence** (when that map is invertible on homotopy categories) — because the second is the special case of the first that one actually cares about, and it is not statable without the first.

---

# Axiom Motivation

The motivation is to find the right notion of "map between model categories." A model category is a presentation of a homotopy theory, so a map should be something that descends to a functor on homotopy categories. The naive guess — a functor preserving the three classes — is both too strong and the wrong shape, because the constructions we care about ([[Def - Free-Forgetful Adjunction|free-forgetful]], geometric realization, tensor product) come in adjoint *pairs*, and asking a single functor to preserve everything ignores how the pair cooperates. The productive notion is built around an adjunction.

Start from what we need: the pair $F \dashv U$ should induce functors $\mathbf{L}F$ and $\mathbf{R}U$ on homotopy categories, and these should remain adjoint. Recall that $\mathbf{L}F = F \circ Q$ applies $F$ after cofibrant replacement, and $\mathbf{R}U = U \circ R$ applies $U$ after fibrant replacement (see [[Def - Cofibrant and Fibrant Objects]]). For $\mathbf{L}F$ to be well-defined on the homotopy category, $F$ must send weak equivalences between cofibrant objects to weak equivalences — otherwise $F \circ Q$ would not respect the morphisms of $\mathrm{Ho}(\mathcal{M})$. The cleanest hypothesis that guarantees this is **Ken Brown's lemma**: a functor sending trivial cofibrations between cofibrant objects to weak equivalences automatically preserves *all* weak equivalences between cofibrant objects. So we should ask $F$ to preserve trivial cofibrations. And to make $F \circ Q$ land in good objects and behave, we ask $F$ to preserve cofibrations too. That is the definition of a left Quillen functor, and it is forced by the requirement that the derived functor exist.

Why is "$F$ preserves cofibrations and trivial cofibrations" the *same* as "$U$ preserves fibrations and trivial fibrations"? This is the adjoint lifting equivalence, and it is worth understanding because it is the reason the definition is symmetric. A cofibration is detected by lifting against trivial fibrations; an adjunction converts a lifting problem for $F(\text{cofibration})$ against a fibration into a lifting problem for the cofibration against $U(\text{fibration})$, by transposing the square. So "$F$ sends cofibrations to maps lifting against trivial fibrations" transposes to "$U$ sends trivial fibrations to maps that cofibrations lift against" — and unwinding, the two preservation conditions are adjoint to each other. You may check whichever class is convenient. In $\mathbf{Top} \rightleftarrows \mathbf{sSet}$ it is easier to see that the right adjoint $\mathrm{Sing}$ preserves fibrations; in $\mathbf{Ch}(R)$ it is easier to see the left adjoint $-\otimes N$ preserves cofibrations.

Now the equivalence. A Quillen adjunction always induces an adjunction on homotopy categories, but we want to know *when it is an equivalence* — when the two model categories present the *same* homotopy theory. The derived adjunction $\mathbf{L}F \dashv \mathbf{R}U$ is an equivalence exactly when its unit and counit are isomorphisms in the homotopy categories. Unwinding what that means at the object level gives the Quillen-equivalence condition: for cofibrant $A$ and fibrant $B$, the derived unit/counit being an isomorphism translates to "a map $FA \to B$ is a weak equivalence if and only if its adjunct $A \to UB$ is." The restriction to cofibrant $A$ and fibrant $B$ is not optional — it is exactly the range on which $F$ and $U$ are homotopically meaningful, and outside it the iff can fail. So the Quillen-equivalence condition is the object-level shadow of "the derived adjunction is an equivalence of categories."

---

# The Definition

Let $\mathcal{M}, \mathcal{N}$ be model categories.

**Left and right Quillen functors.** A functor $F : \mathcal{M} \to \mathcal{N}$ that is a left adjoint is a **left Quillen functor** if it preserves cofibrations and trivial cofibrations. A functor $U : \mathcal{N} \to \mathcal{M}$ that is a right adjoint is a **right Quillen functor** if it preserves fibrations and trivial fibrations.

**Quillen adjunction.** An adjunction $(F, U, \varphi)$ with $F : \mathcal{M} \to \mathcal{N}$ left adjoint to $U : \mathcal{N} \to \mathcal{M}$ is a **Quillen adjunction** if $F$ is a left Quillen functor. Equivalently — and this equivalence is part of the definition's usefulness — if $U$ is a right Quillen functor. (The two conditions are adjoint and either implies the other.) One usually names a Quillen adjunction by its left or right adjoint alone, but the full adjunction is always meant.

**Quillen equivalence.** A Quillen adjunction $(F, U, \varphi)$ is a **Quillen equivalence** if for every **cofibrant** object $A \in \mathcal{M}$ and every **fibrant** object $B \in \mathcal{N}$, a map $h : FA \to B$ is a weak equivalence in $\mathcal{N}$ **if and only if** its adjunct $\tilde{h} = \varphi(h) : A \to UB$ is a weak equivalence in $\mathcal{M}$.

Equivalently, $(F, U, \varphi)$ is a Quillen equivalence if and only if the induced total derived adjunction $\mathbf{L}F \dashv \mathbf{R}U$ is an equivalence of categories $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$ — this is the content of [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]].

---

# Categorical / Structural Definition

The structural content is cleanest through derived functors. By Ken Brown's lemma, a left Quillen functor $F$ preserves weak equivalences between cofibrant objects, so $F \circ Q$ descends to a functor $\mathbf{L}F : \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{N})$, the **total left derived functor**, characterized as the right Kan extension of the localization of $F$ along the localization of $\mathcal{M}$. Dually $U$ yields $\mathbf{R}U$, the **total right derived functor**, a left Kan extension. The defining feature of a Quillen adjunction is then exactly that **these derived functors form an adjunction** $\mathbf{L}F \dashv \mathbf{R}U$, and a Quillen equivalence is exactly that this derived adjunction is an adjoint equivalence — its unit and counit are natural isomorphisms in the homotopy categories.

From the (∞,1)-categorical perspective, a Quillen adjunction presents an **adjunction of (∞,1)-categories** between the homotopy theories $\mathcal{M}[\mathcal{W}^{-1}]$ and $\mathcal{N}[\mathcal{W}^{-1}]$, and a Quillen equivalence presents an **equivalence of (∞,1)-categories**. So the model-categorical notions are presentations, computable on the point set, of the genuinely intrinsic ∞-categorical notions — the same way a model structure presents an (∞,1)-category in [[Def - Model Category]].

---

# Relate to Other Fields / Compression

A Quillen adjunction is the homotopical upgrade of an ordinary [[Def - Adjunction|adjunction]], and the most familiar adjunctions become Quillen adjunctions in their natural model structures. The [[Def - Free-Forgetful Adjunction|free-forgetful adjunction]] between simplicial sets and topological spaces, the tensor-hom adjunction in chain complexes, and the realization-nerve adjunction all become Quillen adjunctions, and in each the left adjoint is the "free/geometric" construction and the right adjoint the "underlying/combinatorial" one. The Quillen-equivalence condition is the homotopical analogue of an adjunction being an *adjoint equivalence*: ordinarily $F \dashv U$ is an equivalence when the unit and counit are isomorphisms, and a Quillen equivalence is when the *derived* unit and counit are isomorphisms — the iff in the definition is precisely the statement that the derived unit (on cofibrant $A$) and derived counit (on fibrant $B$) are weak equivalences.

In homological algebra this specializes to the comparison of resolutions: the projective and injective model structures on $\mathbf{Ch}(R)$ are Quillen equivalent (both present $D(R)$), which is the abstract reason left-derived functors computed via projectives and right-derived functors computed via injectives describe the same derived category. And the equivalence $\mathbf{Top} \simeq_Q \mathbf{sSet}$ is the statement that combinatorial and topological homotopy theory coincide.

**True name:** a Quillen adjunction is **"an adjunction whose left adjoint respects cofibrant building"** (equivalently whose right adjoint respects fibrant targets), and a Quillen equivalence is **"an adjunction that becomes an equivalence after deriving"** — the derived unit and counit are weak equivalences on cofibrant/fibrant objects.

---

# Examples / Corollaries

**Is an instance — geometric realization and singular nerve.** The adjunction $|{-}| \dashv \mathrm{Sing}$ between $\mathbf{sSet}$ and $\mathbf{Top}$ is a Quillen adjunction: $|{-}|$ sends monomorphisms (the cofibrations of $\mathbf{sSet}$) to relative cell complexes (cofibrations of $\mathbf{Top}$), and it is a Quillen equivalence, so $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$. See [[Ex - Geometric realization and singular nerve form a Quillen equivalence]] and [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]].

**Is an instance — derived tensor product.** For an $R$-module $N$, the adjunction $-\otimes_R N \dashv \mathrm{Hom}_R(N, -)$ on $\mathbf{Ch}(R)$ is a Quillen adjunction (the left adjoint preserves cofibrations because tensoring a complex of projectives with $N$ stays cofibrant when $N$ is suitably flat, and preserves trivial cofibrations). Its total left derived functor is $-\otimes^{\mathbf{L}}_R N$, whose homology is $\mathrm{Tor}^R_*(-, N)$. See [[Ex - The derived tensor product computes Tor]].

**Is an instance — the trivial Quillen adjunction.** The identity functor on a model category is a Quillen equivalence with itself. More usefully, when a single category carries two model structures with the same weak equivalences but different cofibrations (e.g. the projective and injective structures on $\mathbf{Ch}(R)$), the identity functor is a Quillen equivalence between them, certifying they present the same homotopy theory.

**Is NOT an instance — a Quillen adjunction that is not a Quillen equivalence.** The adjunction between $\mathbf{Top}$ with the Quillen model structure and $\mathbf{Set}$ with the trivial (isomorphisms only) model structure, given by $\pi_0 \dashv (\text{discrete space})$, is a Quillen adjunction but emphatically *not* a Quillen equivalence: it collapses all homotopical information to connected components. A map $\pi_0(A) \to B$ of sets being an isomorphism does not detect whether $A \to (\text{discrete } B)$ is a weak homotopy equivalence, because the latter sees all the $\pi_n$. This is the standard reminder that being a Quillen adjunction is far weaker than being an equivalence.

**Is NOT an instance — preserving weak equivalences is neither necessary nor sufficient.** A left Quillen functor need not preserve all weak equivalences (only those between cofibrant objects), and a functor preserving all weak equivalences need not be a left Quillen functor (it might not preserve cofibrations). The two conditions are independent; conflating them is the most common error. Ken Brown's lemma is exactly the bridge that recovers the restricted preservation from the Quillen condition.

**Calibration check.** Verify that the composite of two Quillen adjunctions is a Quillen adjunction (compose the left adjoints; preservation of cofibrations is preserved under composition). Verify that in a Quillen adjunction the left adjoint $F$ sends the initial object $\varnothing$ to the initial object (left adjoints preserve colimits, and $\varnothing$ is the empty colimit), so $F$ sends cofibrant objects to cofibrant objects. If you can state why the equivalence condition is restricted to cofibrant $A$ and fibrant $B$ — because that is the range where $F$ and $U$ are homotopically meaningful and where the derived unit and counit live — you have understood the definition.

---

# Unlocked by This

> [!tip] Total Derived Adjunctions and Equivalences of Homotopy Theories *(from this chapter)*
> [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] turns a Quillen adjunction into $\mathbf{L}F \dashv \mathbf{R}U$ on homotopy categories and a Quillen equivalence into an equivalence $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$ — the precise sense in which two model structures present the same homotopy theory.

> [!tip] The Homotopy Hypothesis *(from Higher Category Theory)*
> The Quillen equivalence $\mathbf{Top} \simeq_Q \mathbf{sSet}$ is a rigorous form of the **homotopy hypothesis** — that ∞-groupoids (modelled by Kan complexes) are the same as spaces. Chains of Quillen equivalences are how one proves different models of **∞-categories** agree.

> [!tip] Derived Functors, Tor, and Ext *(from Homological Algebra)*
> Quillen adjunctions on $\mathbf{Ch}(R)$ produce the classical **derived functors**: $\mathbf{L}(-\otimes N)$ has homology **Tor**, and $\mathbf{R}\,\mathrm{Hom}(N, -)$ has cohomology **Ext**. The derived-functor formalism of homological algebra is a special case of the derived-adjunction formalism here.
