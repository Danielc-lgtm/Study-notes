---
type: theorem
subject: model-categories
prereqs:
  - "Def - Quillen Adjunction and Quillen Equivalence"
  - "Def - Cofibrant and Fibrant Objects"
  - "Thm - The Homotopy Category of a Model Category"
  - "Def - Adjunction"
  - "Thm - Right Adjoints Preserve Limits"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}, \mathcal{N}$ are model categories and $F \dashv U$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]], with $F : \mathcal{M} \to \mathcal{N}$ the left Quillen functor and $U : \mathcal{N} \to \mathcal{M}$ the right Quillen functor, adjunction isomorphism $\varphi : \mathcal{N}(FA, B) \cong \mathcal{M}(A, UB)$, [[Def - Unit and Counit of an Adjunction|unit]] $\eta$, and counit $\varepsilon$. We write $Q$ for cofibrant replacement, $R$ for fibrant replacement, $\mathbf{L}F = F \circ Q$ for the **total left derived functor**, $\mathbf{R}U = U \circ R$ for the **total right derived functor**, and $\mathrm{Ho}(-)$ for the homotopy category (see [[Thm - The Homotopy Category of a Model Category]]). The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

---

# Statement

> **Quillen Adjunctions Descend to Derived Adjunctions.** Let $F \dashv U$ be a Quillen adjunction between model categories $\mathcal{M}$ and $\mathcal{N}$. Then:
> 1. The total derived functors exist as functors on homotopy categories, $\mathbf{L}F : \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{N})$ given by $\mathbf{L}F = F \circ Q$, and $\mathbf{R}U : \mathrm{Ho}(\mathcal{N}) \to \mathrm{Ho}(\mathcal{M})$ given by $\mathbf{R}U = U \circ R$.
> 2. They form an **adjunction** $\mathbf{L}F \dashv \mathbf{R}U$ on homotopy categories.
> 3. If the Quillen adjunction is a **Quillen equivalence**, then $\mathbf{L}F$ and $\mathbf{R}U$ are mutually inverse **equivalences of categories**, so $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$.

---

# Motivation

This theorem is what makes "map of model categories" mean something. A model category presents a homotopy theory; a Quillen adjunction is supposed to be a structure-preserving comparison between two such presentations. But the comparison only earns its keep if it actually descends to the homotopy categories — the intrinsic objects — and this theorem is the guarantee that it does. Without it, a Quillen adjunction would be a relationship between two pieces of scaffolding with no consequence for the homotopy theories the scaffolding presents.

The theorem also unifies a sprawl of constructions you have met under different names. The **derived tensor product**, **Tor**, **Ext**, **homotopy colimits**, **homotopy limits**, and the comparison of **spaces with simplicial sets** are all instances of "a Quillen adjunction, derived." The total left derived functor $\mathbf{L}F = F \circ Q$ is the abstract template for "apply the functor after cofibrant replacement," and part (3) is the abstract template for "two presentations describe the same thing." Recognizing that all these are one theorem is the conceptual payoff: derived functors are not an ad hoc list but the systematic shadow of adjunctions on homotopy categories. The role of part (3) in particular is to provide the *only* general method for proving two model categories present the same homotopy theory — exhibit a Quillen equivalence — which is how the foundational comparisons of the subject ($\mathbf{Top} \simeq \mathbf{sSet}$, projective $\simeq$ injective resolutions) are all established.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a Quillen adjunction," but you recognize the situation from several disguises.

The first disguised source is **a functor you want to make homotopy-invariant.** Whenever you have a functor $F$ that fails to respect weak equivalences but is a left adjoint, you suspect it is left Quillen and seek its derived functor. The non-obvious step is checking the Quillen condition (preserves cofibrations and trivial cofibrations) rather than the impossible condition (preserves all weak equivalences). *Example problem:* the tensor product $-\otimes_R N$ does not respect quasi-isomorphisms, but it is left Quillen, so $\mathbf{L}(-\otimes N)$ exists and computes $\mathbf{Tor}$ — see [[Ex - The derived tensor product computes Tor]].

The second disguised source is **a (co)limit construction.** The colimit and limit functors are the left and right adjoints to the constant-diagram functor; recognizing them as adjoints feeds them into this theorem, yielding homotopy (co)limits as their derived functors. The non-obvious step is seeing $\mathrm{colim}$ as a left adjoint at all. *Example problem:* the homotopy pushout is $\mathbf{L}\,\mathrm{colim}$ over a span — see [[Def - Homotopy Limit and Colimit]].

The third disguised source is **an adjunction between two models of "the same" objects.** When two categories both purport to model a homotopy theory (spaces and simplicial sets; topological and combinatorial; algebraic and geometric), the comparison adjunction is the input, and you check it is a Quillen equivalence to certify the models agree. The non-obvious step is that an *adjunction*, not an equivalence of categories, is the right comparison — the categories are genuinely different, only their homotopy theories agree. *Example problem:* $|{-}| \dashv \mathrm{Sing}$ is a Quillen equivalence, so $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$ — see [[Ex - Geometric realization and singular nerve form a Quillen equivalence]].

**Targets (Output Amplification)**

The conclusion is the derived adjunction (and equivalence); combined with other facts it amplifies.

Combine part (2) with **a computation in one homotopy category.** The adjunction $\mathbf{L}F \dashv \mathbf{R}U$ lets you transport a computation across: $\mathrm{Ho}(\mathcal{N})(\mathbf{L}F X, Y) \cong \mathrm{Ho}(\mathcal{M})(X, \mathbf{R}U Y)$. The amplified result $E$ is the universal-property characterization of derived functors — e.g. $\mathbf{Ext}^*(M, N)$ as derived homs — which turns a calculation in complexes into a calculation in the derived category.

Combine part (3) with **a chain of Quillen equivalences.** Equivalences of homotopy categories compose, so a zig-zag of Quillen equivalences $\mathcal{M}_1 \simeq \mathcal{M}_2 \simeq \cdots \simeq \mathcal{M}_n$ shows all the $\mathrm{Ho}(\mathcal{M}_i)$ agree. The amplified result is the comparison of *many* models at once — the standard method for proving that all known models of $\infty$-categories (quasi-categories, complete Segal spaces, Segal categories, relative categories) present the same theory.

Combine part (1) with **the projection/identity special cases.** Taking $F$ to be a (co)limit or a base-change functor yields homotopy (co)limits, derived base change, and derived pushforward; the amplified result is the entire toolkit of derived functors in algebraic geometry and homological algebra as instances.

---

# Why Is It True

The mechanism is Ken Brown's lemma, and once you have it the rest is bookkeeping. The obstruction to $F$ descending to homotopy categories is that $F$ need not send weak equivalences to weak equivalences. **Ken Brown's lemma removes the obstruction on cofibrant objects:** a functor that sends trivial cofibrations between cofibrant objects to weak equivalences automatically sends *all* weak equivalences between cofibrant objects to weak equivalences. A left Quillen functor preserves trivial cofibrations, so by Brown's lemma it preserves weak equivalences between cofibrant objects. Therefore $F \circ Q$ — apply $F$ after cofibrant replacement, where everything is cofibrant — respects the morphisms of $\mathrm{Ho}(\mathcal{M})$, so $\mathbf{L}F = F \circ Q$ is a well-defined functor on homotopy categories. This is part (1), and the one-line summary is:

**$F$ misbehaves on bad objects but behaves on cofibrant ones, so derive it by replacing with cofibrant objects first; Ken Brown's lemma is the precise statement that the replacement suffices.**

For the adjunction (part 2), the derived unit and counit are built from the ordinary $\eta, \varepsilon$ inserted with replacements: the derived adjunction's hom-isomorphism is $\mathrm{Ho}(\mathcal{N})(\mathbf{L}F X, Y) \cong \pi(F QX, RY) \cong \pi(QX, U RY) \cong \mathrm{Ho}(\mathcal{M})(X, \mathbf{R}U Y)$, where the middle isomorphism is the *original* adjunction $\varphi$ applied between cofibrant $QX$ and fibrant $RY$ — exactly the objects on which $F$ and $U$ are homotopically meaningful. The adjunction descends because $\varphi$ is natural and survives passage to homotopy classes on the good objects.

For the equivalence (part 3), the Quillen-equivalence condition says precisely that the derived unit $X \to \mathbf{R}U\mathbf{L}F X$ and derived counit $\mathbf{L}F\mathbf{R}U Y \to Y$ are weak equivalences (on cofibrant $X$, fibrant $Y$) — because "$FA \to B$ is a weak equivalence iff its adjunct $A \to UB$ is" is exactly the statement that the unit/counit of the adjunction are weak equivalences after deriving. A derived adjunction whose unit and counit are isomorphisms in the homotopy categories is an adjoint equivalence. So part (3) is the definitional translation of "Quillen equivalence" into "derived unit and counit are isomorphisms," which is the standard criterion for an adjunction to be an equivalence.

---

# What Makes This Hard

The crux is Ken Brown's lemma — proving that preserving trivial cofibrations between cofibrant objects upgrades to preserving all weak equivalences between cofibrant objects. The trick (factoring a weak equivalence $f : A \to B$ between cofibrant objects through the cofibrant object $A \sqcup B$ via the cylinder-like construction and applying the trivial-cofibration hypothesis to each leg) is genuinely non-obvious, and most people cannot reconstruct it without having seen it. The second difficulty is keeping straight *which* replacement goes where: $\mathbf{L}F$ uses cofibrant replacement $Q$ (a left adjoint wants cofibrant input), $\mathbf{R}U$ uses fibrant replacement $R$ (a right adjoint wants fibrant input), and swapping them is the most common error. The third subtlety is part (3): one must recognize that the Quillen-equivalence condition is *literally* the statement "derived unit and counit are weak equivalences," not a separate hypothesis to be verified by other means.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use Ken Brown's lemma to show $F$ preserves weak equivalences between cofibrant objects, hence $\mathbf{L}F = F\circ Q$ descends to homotopy categories (dually for $U$ and $\mathbf{R}U$). Build the derived hom-isomorphism by applying the original adjunction $\varphi$ between cofibrant $QX$ and fibrant $RY$. Finally, translate the Quillen-equivalence condition into "derived unit and counit are weak equivalences" and conclude an adjoint equivalence.

**Subgoal decomposition:**

1. **Ken Brown's lemma.** A left Quillen functor preserves weak equivalences between cofibrant objects.
   - *Hint:* For a weak equivalence $f : A \to B$ between cofibrant objects, factor $(f, \mathrm{id}) : A \sqcup B \to B$ as a cofibration then trivial fibration; the two legs are trivial cofibrations between cofibrant objects.
   - *Why needed:* It is the entire content of part (1); without it $\mathbf{L}F$ is not well-defined.

2. **$\mathbf{L}F$ and $\mathbf{R}U$ descend.** Conclude $F \circ Q$ and $U \circ R$ respect homotopy and weak equivalences, hence define functors on $\mathrm{Ho}$.
   - *Hint:* On cofibrant objects $F$ preserves weak equivalences (step 1) and homotopies (it preserves cylinders of cofibrant objects).
   - *Why needed:* It produces the functors whose adjunction is claimed.

3. **The derived hom-isomorphism.** Build $\mathrm{Ho}(\mathcal{N})(\mathbf{L}F X, Y) \cong \mathrm{Ho}(\mathcal{M})(X, \mathbf{R}U Y)$.
   - *Hint:* Both sides are $\pi(\cdot, \cdot)$ between cofibrant/fibrant objects; apply $\varphi$ between $QX$ and $RY$ and check it respects homotopy.
   - *Why needed:* It is part (2), the adjunction.

4. **Quillen equivalence $\Rightarrow$ derived unit/counit are weak equivalences.** Translate the definition.
   - *Hint:* "$FA \to B$ weak equiv iff adjunct $A \to UB$ weak equiv" with $B = RFA$ gives the derived unit a weak equivalence.
   - *Why needed:* It is the hypothesis of part (3) in usable form.

5. **Conclude an equivalence.** A derived adjunction with invertible unit and counit is an adjoint equivalence.
   - *Hint:* Isomorphic unit and counit in $\mathrm{Ho}$ is the standard criterion.
   - *Why needed:* It is the conclusion $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Ken Brown's lemma
> **Statement:** Let $F : \mathcal{M} \to \mathcal{N}$ be a functor sending trivial cofibrations between cofibrant objects to weak equivalences. Then $F$ sends all weak equivalences between cofibrant objects to weak equivalences.
>
> **Hint:** Factor the "graph" map $A \sqcup B \to B$ of a weak equivalence $f$ into a cofibration followed by a trivial fibration; the two coproduct inclusions composed with the cofibration are trivial cofibrations between cofibrant objects.
>
> **Why needed:** It is the mechanism making $\mathbf{L}F = F \circ Q$ well-defined; the whole theorem rests on it.
>
> > [!note]- Full proof
> > Let $f : A \to B$ be a weak equivalence between cofibrant objects. Form the coproduct $A \sqcup B$ (cofibrant, as a coproduct of cofibrant objects) and the map $(f, \mathrm{id}_B) : A \sqcup B \to B$. Factor it as $A \sqcup B \xrightarrow{j} C \xrightarrow{q} B$ with $j$ a cofibration and $q$ a trivial fibration. Let $i_A, i_B : A, B \to A \sqcup B$ be the inclusions. Then $j \circ i_B : B \to C$ satisfies $q \circ (j i_B) = \mathrm{id}_B$, and since $\mathrm{id}_B$ and $q$ are weak equivalences, $j i_B$ is too (2-out-of-3); it is also a cofibration with cofibrant domain $B$, so a trivial cofibration between cofibrant objects, hence $F(j i_B)$ is a weak equivalence. Similarly $j \circ i_A : A \to C$ satisfies $q \circ (j i_A) = f$, a weak equivalence, so by 2-out-of-3 $j i_A$ is a weak equivalence; it is a cofibration between cofibrant objects, hence trivial, so $F(j i_A)$ is a weak equivalence. Now $F(q) \circ F(j i_A) = F(f)$ and $F(q) \circ F(j i_B) = F(\mathrm{id}) = \mathrm{id}$; the latter shows $F(q)$ is a weak equivalence (2-out-of-3 with $F(j i_B)$), and then the former shows $F(f)$ is a weak equivalence (2-out-of-3). $\square$

> [!note]- Lemma 2: The total derived functors are well-defined on homotopy categories
> **Statement:** $\mathbf{L}F = F \circ Q$ and $\mathbf{R}U = U \circ R$ define functors $\mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{N})$ and $\mathrm{Ho}(\mathcal{N}) \to \mathrm{Ho}(\mathcal{M})$.
>
> **Hint:** $F$ preserves weak equivalences (Lemma 1) and homotopies between cofibrant objects, so it descends after cofibrant replacement.
>
> **Why needed:** It is part (1), producing the functors to be adjoint.
>
> > [!note]- Full proof
> > By Lemma 1, $F$ sends weak equivalences between cofibrant objects to weak equivalences. $F$ also preserves left homotopies between cofibrant objects: a cylinder $\mathrm{Cyl}(A)$ for cofibrant $A$ maps to a cylinder for $FA$ (as $F$ preserves the coproduct $A \sqcup A$ and the cofibration into the cylinder, and weak equivalences between cofibrant objects), so a homotopy $\mathrm{Cyl}(A) \to B$ maps to a homotopy $F\mathrm{Cyl}(A) \to FB$. Hence $F \circ Q$ sends weakly equivalent objects to isomorphic objects and homotopic maps to homotopic maps, inducing $\mathbf{L}F$ on $\mathrm{Ho}$. The statement for $\mathbf{R}U$ is dual (fibrant replacement, right homotopies).

> [!note]- Lemma 3: The derived hom-isomorphism
> **Statement:** For $X \in \mathcal{M}$, $Y \in \mathcal{N}$, there is a natural isomorphism $\mathrm{Ho}(\mathcal{N})(\mathbf{L}F X, Y) \cong \mathrm{Ho}(\mathcal{M})(X, \mathbf{R}U Y)$.
>
> **Hint:** Reduce both sides to $\pi$ between cofibrant/fibrant objects and apply the original adjunction $\varphi$ between $QX$ and $RY$.
>
> **Why needed:** It is part (2), the derived adjunction.
>
> > [!note]- Full proof
> > By [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]], $\mathrm{Ho}(\mathcal{N})(\mathbf{L}F X, Y) = \mathrm{Ho}(\mathcal{N})(FQX, Y) \cong \pi(F QX, RY)$, since $FQX$ is cofibrant ($F$ preserves cofibrant objects) and $RY$ is fibrant. The adjunction $\varphi : \mathcal{N}(FQX, RY) \cong \mathcal{M}(QX, URY)$ descends to homotopy classes (it respects cylinders/path objects on the cofibrant/fibrant objects), giving $\pi(FQX, RY) \cong \pi(QX, URY)$. Finally $\pi(QX, URY) \cong \mathrm{Ho}(\mathcal{M})(X, URY) = \mathrm{Ho}(\mathcal{M})(X, \mathbf{R}U Y)$ since $QX$ is cofibrant and $URY$ is fibrant ($U$ preserves fibrant objects). Naturality is inherited from $\varphi$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — preconditions.** $F \dashv U$ is a Quillen adjunction: $F$ is a left adjoint preserving cofibrations and trivial cofibrations, $U$ a right adjoint preserving fibrations and trivial fibrations. In particular $F$ preserves cofibrant objects (it preserves the initial object as a left adjoint and cofibrations) and $U$ preserves fibrant objects.
>
> **Step 1 — derived functors exist (part 1).** By Lemma 1 (Ken Brown), $F$ preserves weak equivalences between cofibrant objects, and by Lemma 2, $\mathbf{L}F = F \circ Q$ descends to a functor $\mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathcal{N})$. Dually $\mathbf{R}U = U \circ R$ descends.
>
> **Step 2 — the adjunction (part 2).** By Lemma 3, there is a natural isomorphism $\mathrm{Ho}(\mathcal{N})(\mathbf{L}F X, Y) \cong \mathrm{Ho}(\mathcal{M})(X, \mathbf{R}U Y)$, exhibiting $\mathbf{L}F \dashv \mathbf{R}U$.
>
> **Step 3 — Quillen equivalence gives an equivalence (part 3).** Suppose the Quillen adjunction is a Quillen equivalence. The derived unit at a cofibrant $X$ is the composite $X \to U R F Q X$ obtained from the adjunction unit; by definition of Quillen equivalence, the map $FQX \to RFQX$ (a fibrant replacement, hence a weak equivalence) has adjunct $QX \to URFQX$ which is therefore a weak equivalence — this is exactly the statement "$FQX \to RFQX$ weak equiv iff its adjunct is," and the left side is a weak equivalence. So the derived unit is a weak equivalence, i.e. an isomorphism in $\mathrm{Ho}(\mathcal{M})$. Dually the derived counit $\mathbf{L}F\mathbf{R}U Y \to Y$ is an isomorphism in $\mathrm{Ho}(\mathcal{N})$ for fibrant $Y$. An adjunction whose unit and counit are isomorphisms is an adjoint equivalence, so $\mathbf{L}F$ and $\mathbf{R}U$ are mutually inverse equivalences and $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Derived functors in homological algebra.** Apply the theorem to the adjunction $-\otimes_R N \dashv \mathrm{Hom}_R(N, -)$ on $\mathbf{Ch}(R)$: the left derived functor $\mathbf{L}(-\otimes N)$ computes $\mathbf{Tor}^R_*(-, N)$ and the right derived functor $\mathbf{R}\,\mathrm{Hom}(N, -)$ computes $\mathbf{Ext}_R^*(N, -)$. The theorem is the abstract statement that classical derived functors are derived adjoints — see [[Ex - The derived tensor product computes Tor]].

**Geometric realization versus simplicial sets.** Apply part (3) to $|{-}| \dashv \mathrm{Sing}$: this Quillen equivalence gives $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$, the rigorous form of "combinatorial and topological homotopy theory agree." This is the prototype for comparing models of homotopy theories.

**Base change in algebraic geometry.** For a map of rings $f : R \to S$, the extension-of-scalars and restriction-of-scalars adjunction $S \otimes_R - \dashv f^*$ on chain complexes is a Quillen adjunction; its derived functors are the **derived base change** $\mathbf{L}f^*$ and derived pushforward, the building blocks of the six-functor formalism in derived algebraic geometry. Recognizing base change as a derived adjoint is the bridge to that machinery.

---

# Bridges

- **[[Def - Quillen Adjunction and Quillen Equivalence]]** — the input. This theorem is the reason the definition is phrased as it is: "Quillen adjunction" is exactly the hypothesis making $\mathbf{L}F \dashv \mathbf{R}U$ exist, and "Quillen equivalence" is exactly the hypothesis making it an equivalence. The definition is reverse-engineered from this theorem.

- **[[Thm - The Homotopy Category of a Model Category]]** — the foundation. The derived adjunction is built using the concrete description $\mathrm{Ho}(\mathcal{M})(X,Y) = \pi(QRX, QRY)$; the hom-isomorphism of part (2) is the original adjunction applied between the cofibrant and fibrant objects that this theorem identifies.

- **[[Thm - Right Adjoints Preserve Limits]]** — the 1-categorical ancestor. Just as ordinary right adjoints preserve limits, *derived* right adjoints $\mathbf{R}U$ preserve *homotopy* limits, and derived left adjoints $\mathbf{L}F$ preserve homotopy colimits. The derived adjunction transports the limit-preservation properties to the homotopy-theoretic level.

- **[[Def - Homotopy Limit and Colimit]]** — a special case. Taking $F = \mathrm{colim}$ and $U = \lim$ (the adjoints to the constant-diagram functor) makes this theorem produce the homotopy colimit $\mathbf{L}\,\mathrm{colim}$ and homotopy limit $\mathbf{R}\lim$; the derived adjunction is the statement that homotopy colimits are left adjoint to the constant diagram.

---

# Unlocked by This

> [!tip] Tor, Ext, and the Derived Category *(from Homological Algebra)*
> The classical **derived functors** are this theorem in $\mathbf{Ch}(R)$: $\mathbf{Tor}$ from $\mathbf{L}\otimes$, $\mathbf{Ext}$ from $\mathbf{R}\,\mathrm{Hom}$. The derived adjunction between them is the source of the tensor-hom adjunction in the **derived category**, and of the universal coefficient and Künneth spectral sequences.

> [!tip] The Homotopy Hypothesis and Comparison of ∞-Category Models *(from Higher Category Theory)*
> Part (3) is how one proves models agree: the Quillen equivalence $\mathbf{Top} \simeq \mathbf{sSet}$ is the **homotopy hypothesis** for ∞-groupoids, and a chain of Quillen equivalences shows quasi-categories, complete Segal spaces, and relative categories all present the same theory of **∞-categories**. Stacking these equivalences is the technical core of the [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories|Higher Categories]] comparison program.

> [!tip] The Six-Functor Formalism and Derived Algebraic Geometry *(from Algebraic Geometry)*
> Derived base change $\mathbf{L}f^*$, derived pushforward $\mathbf{R}f_*$, and their adjoints are total derived functors of Quillen adjunctions on complexes of sheaves. This theorem is the foundation of the **six-functor formalism** and of the **derived category** of coherent sheaves that organizes modern algebraic geometry.
