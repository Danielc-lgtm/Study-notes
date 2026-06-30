---
type: theorem
subject: model-categories
prereqs:
  - "Def - Cofiber and Fiber Sequence"
  - "Def - Pointed Model Category Suspension and Loop"
  - "Thm - The Suspension-Loop Adjunction"
  - "Def - Pre-Triangulated Category"
  - "Thm - The Homotopy Category of a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Pointed Model Category Suspension and Loop|pointed model category]] with homotopy category $\mathrm{Ho}(\mathcal{C})$, suspension $\Sigma$, loop $\Omega$, and $[X, Y] = \mathrm{Ho}(\mathcal{C})(X, Y)$ a pointed set with basepoint the zero map. For $f : X \to Y$ we write $C_f$ for the [[Def - Cofiber and Fiber Sequence|homotopy cofiber]] and $F_f$ for the homotopy fiber, with connecting maps $\partial : C_f \to \Sigma X$ and $\partial : \Omega Y \to F_f$. The [[Thm - The Suspension-Loop Adjunction|adjunction]] bijection is $[\Sigma X, Z] \cong [X, \Omega Z]$. We say two sequences of pointed sets **agree up to sign** if there is an isomorphism between them commuting with all maps except possibly for an overall sign on the connecting maps (a sign meaningful once the terms are groups). The full symbol registry is on [[Model Categories — Pointed Model Categories and Cofiber Sequences]].

---

# Statement

> **Theorem (Agreement of Puppe sequences).** Let $\mathcal{C}$ be a pointed model category and $f : X \to Y$ a map. Then the cofiber sequence and the fiber sequence of $f$ induce, for every object $Z$, the same long exact sequence of pointed sets, up to sign. Precisely:
> 1. Applying $[-, Z]$ to the [[Def - Cofiber and Fiber Sequence|cofiber sequence]] $X \xrightarrow{f} Y \to C_f \xrightarrow{\partial} \Sigma X \to \cdots$ gives a long exact sequence
> $$\cdots \to [\Sigma X, Z] \to [C_f, Z] \to [Y, Z] \xrightarrow{f^*} [X, Z].$$
> 2. Applying $[Z, -]$ to the [[Def - Cofiber and Fiber Sequence|fiber sequence]] $\cdots \to \Omega Y \xrightarrow{\partial} F_f \to X \xrightarrow{f} Y$ gives a long exact sequence
> $$[Z, \Omega Y] \to [Z, F_f] \to [Z, X] \xrightarrow{f_*} [Z, Y].$$
> 3. Under the [[Thm - The Suspension-Loop Adjunction|adjunction]] [[Def - Isomorphism|isomorphisms]] $[\Sigma X, Z] \cong [X, \Omega Z]$ and the natural identification of the [[Def - Homotopy|homotopy]] cofiber and homotopy fiber connecting maps, these two long exact sequences are isomorphic up to sign on the connecting maps. Consequently $\mathrm{Ho}(\mathcal{C})$ is a [[Def - Pre-Triangulated Category|pre-triangulated category]].

---

# Motivation

The point of this theorem is to certify that a pointed model category carries **one** coherent homotopy theory of exact sequences, not two unrelated ones. The previous page produced, from any map $f$, two infinite sequences — a cofiber sequence built from homotopy pushouts and a fiber sequence built from homotopy pullbacks — and each yielded a long exact sequence of mapping sets. A natural worry is that these are independent gadgets that merely happen to coexist. This theorem dispels the worry: they are two presentations of the same data, locked together by the suspension–loop adjunction. The cofiber sequence is the natural home for *maps out* ($[-, Z]$, cohomology-flavored); the fiber sequence is the natural home for *maps in* ($[Z, -]$, homotopy-flavored); and the adjunction is the dictionary translating one into the other.

The deeper reason this matters is that it is the verification that $\mathrm{Ho}(\mathcal{C})$ is **pre-triangulated**. The pre-triangulated axioms demand precisely that the cofiber and fiber classes be compatible through the adjunction's unit and counit. This theorem is that compatibility, made concrete: it is the abstract analogue of the fact in a triangulated category that "rotating a triangle and applying the shift" relates the two ways of reading exactness. Once it is proved, the entire pre-triangulated apparatus — and, in the stable case, the triangulated apparatus — is available without ever touching the model category again.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is having both a cofiber sequence and a fiber sequence of the same map $f$; the source question is when a problem secretly hands you a comparison between maps-out exactness and maps-in exactness.

The first disguised source is **a single homotopy-(co)cartesian square**. A square that is simultaneously a homotopy pushout and a homotopy pullback (which happens for any square in a *stable* category, and for special squares otherwise) provides both a cofiber and a fiber sequence at once, and the theorem identifies their exact sequences. *Example problem:* in $\mathrm{Ch}(R)$, a short exact sequence of complexes gives a square that is both a homotopy pushout and pullback in $D(R)$; the theorem says the Ext long exact sequence read via $\mathrm{Hom}(-, Z)$ and the one read via $\mathrm{Hom}(Z, -)$ are the same up to sign.

The second disguised source is **a contractible end object**. If $C_f \simeq *$ (the cofiber is null), exactness collapses the cofiber sequence to a suspension isomorphism $[Y, Z] \cong [\Sigma X, Z]$; dually if $F_f \simeq *$ the fiber sequence gives $[Z, X] \cong [Z, \Omega Y]$. The theorem says these two isomorphisms correspond under the adjunction. *Example problem:* for a fibration with contractible total space, the long exact sequence of the fibration degenerates to $\pi_n(F) \cong \pi_{n+1}(B)$, and the dual cofiber statement matches it.

The third disguised source is **any (co)homology or homotopy functor applied to a cofibration or fibration**. A cohomology theory $E^*$ is exactly a functor sending cofiber sequences to long exact sequences; a homotopy functor $\pi_*$ sends fiber sequences to long exact sequences. The theorem guarantees that for the same map, the $E$-cohomology sequence and the $\pi$-homotopy sequence are governed by the same connecting maps. *Example problem:* compare the long exact sequence of a pair in $E$-cohomology with the long exact sequence of the associated fibration in homotopy; the theorem is what makes the two connecting homomorphisms "the same map" up to the adjunction.

**Targets (Output Amplification)**

The bare conclusion is "two long exact sequences agree up to sign." Combined with structure it gives the foundational results of the chapter.

Combine the conclusion with **the rotation of sequences**. Since cofiber and fiber sequences agree, rotating a cofiber sequence (shifting it along, with a sign) corresponds to rotating the matching fiber sequence. The further result is the full **rotation axiom of a pre-triangulated category**, which is what makes a three-term sequence equivalent to its infinite Puppe extension.

Combine the conclusion with **invertibility of $\Sigma$**. If $\Sigma$ is an equivalence, the adjunction unit/counit are isomorphisms, the cofiber and fiber sequences literally coincide (not merely agree on mapping sets), and the two classes merge into one class of **distinguished triangles**. The further result $E$ is that $\mathrm{Ho}(\mathcal{C})$ is **triangulated** — this theorem is the precise input that the stable-category theorem of the next chapter promotes.

Combine the conclusion with **a long exact sequence of a fixed (co)homology theory**. Knowing the cofiber and fiber connecting maps agree, one can compute a connecting homomorphism in whichever picture is easier and transport it to the other. The further result is a practical computational tool: the **Mayer–Vietoris and snake-lemma boundary maps** can be identified across the two presentations, which is how one proves naturality of connecting homomorphisms in practice.

---

# Why Is It True

Think first about what a connecting map *is*, on both sides. In the cofiber sequence, the connecting map $\partial : C_f \to \Sigma X$ arises because the cofiber of $Y \to C_f$ is $\Sigma X$: you collapse $Y$ inside the mapping cone and the leftover cone on $X$ becomes the suspension. In the fiber sequence, the connecting map $\partial : \Omega Y \to F_f$ arises dually, because the fiber of $F_f \to X$ is $\Omega Y$. These two $\partial$'s are built by formally dual constructions — pushout-collapse versus pullback-restriction — and the suspension–loop adjunction is exactly the statement that pushout-collapse and pullback-restriction are adjoint operations. So when you map out of the cofiber connecting map, $\partial^* : [\Sigma X, Z] \to [C_f, Z]$, and rewrite the source via the adjunction as $[X, \Omega Z]$, you land on the *same map* the fiber connecting map would produce reading into $Z$.

The sign is the only subtlety, and it has an honest source. Re-suspending a cofiber sequence introduces a sign because $\Sigma$ applied to the co-multiplication on $\Sigma X$ flips orientation — the same reason the boundary map in the cofiber sequence of the cofiber sequence is $-\Sigma\partial$. When you transport across the adjunction, this orientation flip is what shows up as the overall sign relating the two long exact sequences. It is not an error term; it is the bookkeeping of how the suspension coordinate is oriented, and it is exactly the sign that appears in the rotation axiom of triangulated categories.

**The one-line mechanism: the cofiber connecting map $C_f \to \Sigma X$ and the fiber connecting map $\Omega Y \to F_f$ are adjoint transposes of each other under $\Sigma \dashv \Omega$, so mapping out of one equals mapping into the other.** The agreement of the long exact sequences is the naturality of the adjunction applied term by term, and the sign is the orientation of the suspension coordinate.

---

# What Makes This Hard

The difficulty is **keeping the dualization honest while tracking the sign**. The cofiber and fiber stories are formally dual, so the temptation is to assert "by duality they agree" and stop — but duality alone does not produce the *specific* isomorphism between the two long exact sequences, nor explain the sign, and a wrong identification of the connecting maps gives a sequence that is off by more than a sign. The non-obvious step is recognizing that the adjunction's unit $\eta : X \to \Omega\Sigma X$ and counit $\varepsilon : \Sigma\Omega Y \to Y$ are exactly the natural transformations that mediate the comparison — the connecting maps are not equal but are related through $\eta$ and $\varepsilon$. The common error is to forget the sign (claiming the sequences are isomorphic on the nose), which then breaks the rotation axiom and gives an inconsistent pre-triangulated structure; the sign is forced and must be carried.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove exactness of each long exact sequence from the universal property of the homotopy pushout (for the cofiber sequence) and homotopy pullback (for the fiber sequence), term by term. Then identify the two sequences by transporting the cofiber sequence's tail across the suspension–loop adjunction, checking that the connecting maps correspond up to the orientation sign.

**Subgoal decomposition:**

1. **Exactness of the cofiber long exact sequence at $[Y, Z]$.** Show $\mathrm{im}([C_f, Z] \to [Y, Z]) = \ker([Y, Z] \xrightarrow{f^*} [X, Z])$.
   - *Hint:* A map $Y \to Z$ factors through $C_f$ iff its composite with $f$ is null — the universal property of the homotopy pushout square with corner $*$.
   - *Why needed:* Exactness at one term, plus rotation, gives exactness everywhere by the Puppe iteration.

2. **Exactness of the fiber long exact sequence at $[Z, X]$.** Dually, show $\mathrm{im}([Z, F_f] \to [Z, X]) = \ker([Z, X] \xrightarrow{f_*} [Z, Y])$.
   - *Hint:* A map $Z \to X$ lifts to $F_f$ iff its composite with $f$ is null — the universal property of the homotopy pullback.
   - *Why needed:* It is the dual exactness, and the two must be shown to be the same statement.

3. **Identify the connecting maps as adjoint transposes.** Show the cofiber connecting map $\partial : C_f \to \Sigma X$ and the fiber connecting map $\partial : \Omega Y \to F_f$ correspond under $\Sigma \dashv \Omega$.
   - *Hint:* Both are built from the "(co)fiber of the (co)fiber = (co)suspension" identity; transpose one across the adjunction unit/counit and compare.
   - *Why needed:* It is the heart of the agreement — without it the two sequences would merely both be exact, not the same.

4. **Match the sequences up to sign.** Use the adjunction $[\Sigma X, Z] \cong [X, \Omega Z]$ to rewrite the cofiber sequence's $\Sigma$-terms as $\Omega$-terms and check the maps agree up to the suspension orientation sign.
   - *Hint:* The sign enters from $-\Sigma f$ in the rotated cofiber sequence; it is the sign that re-suspension introduces.
   - *Why needed:* It produces the explicit isomorphism (up to sign) asserted in the theorem and verifies the pre-triangulated compatibility axiom.

---

# Lemma Decomposition

> [!note]- Lemma 1: A map factors through the homotopy cofiber iff it kills the source
> **Statement:** For a cofiber sequence $X \xrightarrow{f} Y \xrightarrow{i} C_f$ and any $Z$, a map $u : Y \to Z$ extends along $i$ to a map $C_f \to Z$ if and only if $u \circ f = 0$ in $[X, Z]$. Hence $\mathrm{im}(i^*) = \ker(f^*)$ in $[Y, Z]$.
>
> **Hint:** $C_f$ is the homotopy pushout of $* \leftarrow X \xrightarrow{f} Y$; extending $u$ over $C_f$ is exactly giving a cocone, which requires a null-homotopy of $u \circ f$.
>
> **Why needed:** It is exactness of the cofiber long exact sequence at $[Y, Z]$, the seed of all cofiber exactness.
>
> > [!note]- Full proof
> > The square with corners $X, Y, *, C_f$ is a homotopy pushout, so $\mathrm{Ho}(\mathcal{C})(C_f, Z)$ is the homotopy pullback (homotopy limit) of $\mathrm{Ho}(\mathcal{C})(*, Z) \to \mathrm{Ho}(\mathcal{C})(Y, Z) \leftarrow \mathrm{Ho}(\mathcal{C})(X, Z)$ along $f^*$ and the basepoint. Concretely a map $C_f \to Z$ is a map $u : Y \to Z$ together with a null-homotopy of $u \circ f$ (the data on the cone). Thus $u$ extends over $C_f$ iff $u \circ f$ is null-homotopic, i.e. $u \circ f = 0$ in $[X, Z]$, i.e. $u \in \ker(f^*)$. Conversely every $u$ in the image of $i^*$ satisfies $u \circ f = (i^* v) \circ f = v \circ (i \circ f) = v \circ 0 = 0$. Hence $\mathrm{im}(i^*) = \ker(f^*)$.

> [!note]- Lemma 2: A map lifts to the homotopy fiber iff it dies in the target
> **Statement:** For a fiber sequence $F_f \xrightarrow{p} X \xrightarrow{f} Y$ and any $Z$, a map $v : Z \to X$ lifts along $p$ to $Z \to F_f$ if and only if $f \circ v = 0$ in $[Z, Y]$. Hence $\mathrm{im}(p_*) = \ker(f_*)$ in $[Z, X]$.
>
> **Hint:** Dualize Lemma 1: $F_f$ is the homotopy pullback of $X \xrightarrow{f} Y \leftarrow *$, so lifting $v$ to $F_f$ requires a null-homotopy of $f \circ v$.
>
> **Why needed:** It is exactness of the fiber long exact sequence at $[Z, X]$, dual to Lemma 1.
>
> > [!note]- Full proof
> > The square with corners $F_f, X, *, Y$ is a homotopy pullback, so $\mathrm{Ho}(\mathcal{C})(Z, F_f)$ is the homotopy pullback of $\mathrm{Ho}(\mathcal{C})(Z, *) \to \mathrm{Ho}(\mathcal{C})(Z, Y) \leftarrow \mathrm{Ho}(\mathcal{C})(Z, X)$ along the basepoint and $f_*$. A map $Z \to F_f$ is a map $v : Z \to X$ with a null-homotopy of $f \circ v$. Thus $v$ lifts iff $f \circ v = 0$ in $[Z, Y]$, i.e. $v \in \ker(f_*)$; and any $v = p_* w$ in the image satisfies $f \circ v = f \circ p \circ w = 0 \circ w = 0$. Hence $\mathrm{im}(p_*) = \ker(f_*)$.

> [!note]- Lemma 3: The connecting maps are adjoint transposes (cofiber of cofiber = suspension, fiber of fiber = loop)
> **Statement:** The cofiber of $i : Y \to C_f$ is canonically $\Sigma X$, giving $\partial : C_f \to \Sigma X$; dually the fiber of $p : F_f \to X$ is canonically $\Omega Y$, giving $\partial : \Omega Y \to F_f$. Under the adjunction $\Sigma \dashv \Omega$, the map $\partial^* : [\Sigma X, Z] \to [C_f, Z]$ corresponds to the map $\partial_* : [Z, \Omega Y] \to [Z, F_f]$ via $[\Sigma X, Z] \cong [X, \Omega Z]$, up to the suspension orientation sign.
>
> **Hint:** Build $\Sigma X$ by pasting the cofiber square of $f$ onto the cofiber square of $i$; build $\Omega Y$ dually. Transpose using the unit $\eta$ and counit $\varepsilon$ of [[Thm - The Suspension-Loop Adjunction]].
>
> **Why needed:** This identifies the two families of connecting maps, which is the substance of "the sequences agree."
>
> > [!note]- Full proof
> > Paste the homotopy-pushout square $[X \to Y,\, * \to C_f]$ to the homotopy-pushout square $[Y \to C_f,\, * \to C_i]$. By the pasting lemma for homotopy pushouts the outer rectangle $[X \to *,\, * \to C_i]$ is a homotopy pushout, exhibiting $C_i = * \cup_X * \cup \cdots = \Sigma X$ (the cofiber of $i$ is the suspension of $X$). The induced map $C_f \to C_i = \Sigma X$ is the connecting map $\partial$. Dually, pasting homotopy-pullback squares gives the fiber of $p$ as $\Omega Y$ and the connecting map $\Omega Y \to F_f$. Now apply $[-, Z]$ to $\partial : C_f \to \Sigma X$ and use the adjunction bijection $[\Sigma X, Z] \cong [X, \Omega Z]$: naturality of the bijection in the suspension/loop variable, together with the dual construction of the fiber connecting map, makes $\partial^*$ and $\partial_*$ correspond. The correspondence carries a sign because the rotated cofiber sequence has connecting map $-\Sigma f$ (the suspension co-multiplication reverses orientation under one rotation), and this is the only discrepancy.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : X \to Y$ be a map in a pointed model category $\mathcal{C}$.
>
> **Step 0 — both sequences exist.** Form the [[Def - Cofiber and Fiber Sequence|cofiber sequence]] $X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X \to \cdots$ (homotopy pushouts) and the fiber sequence $\cdots \to \Omega Y \xrightarrow{\partial} F_f \xrightarrow{p} X \xrightarrow{f} Y$ (homotopy pullbacks). Both live in $\mathrm{Ho}(\mathcal{C})$ and are defined for all $f$ after cofibrant/fibrant replacement.
>
> **Step 1 — cofiber exactness.** By Lemma 1, $[-, Z]$ applied to $X \xrightarrow{f} Y \xrightarrow{i} C_f$ is exact at $[Y, Z]$. Rotating the cofiber sequence (Lemma 3 gives $C_i \simeq \Sigma X$, so each consecutive triple is again a cofiber sequence) and re-applying Lemma 1 at each spot yields exactness of the entire long sequence
> $$\cdots \to [\Sigma X, Z] \xrightarrow{\partial^*} [C_f, Z] \xrightarrow{i^*} [Y, Z] \xrightarrow{f^*} [X, Z].$$
>
> **Step 2 — fiber exactness.** Dually, by Lemma 2, $[Z, -]$ applied to the fiber sequence is exact at $[Z, X]$, and rotating (Lemma 3 gives the fiber of $p$ is $\Omega Y$) yields exactness of
> $$[Z, \Omega Y] \xrightarrow{\partial_*} [Z, F_f] \xrightarrow{p_*} [Z, X] \xrightarrow{f_*} [Z, Y].$$
>
> **Step 3 — identify the connecting maps.** By Lemma 3, the cofiber connecting map $\partial : C_f \to \Sigma X$ and the fiber connecting map $\partial : \Omega Y \to F_f$ are adjoint transposes under $\Sigma \dashv \Omega$. Using the [[Thm - The Suspension-Loop Adjunction|adjunction]] isomorphism $[\Sigma X, Z] \cong [X, \Omega Z]$ on every $\Sigma$-term of the cofiber sequence, the cofiber long exact sequence is rewritten with $\Omega$-targets, and by Lemma 3 the rewritten maps coincide with the fiber long exact sequence's maps.
>
> **Step 4 — the sign and conclusion.** The only discrepancy is an overall sign on the connecting maps, arising because the once-rotated cofiber sequence has connecting map $-\Sigma f$ (the suspension's co-multiplication reverses orientation under rotation). Hence the two long exact sequences are isomorphic up to sign. Since the cofiber and fiber classes are now matched through the adjunction's unit and counit, and the long-exact-sequence and rotation axioms hold, $\mathrm{Ho}(\mathcal{C})$ satisfies the axioms of a [[Def - Pre-Triangulated Category|pre-triangulated category]]. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Snake lemma as agreement of sequences.** In $D(R)$, take a short exact sequence of complexes and form both its cofiber sequence (giving a long exact sequence via $\mathrm{Hom}(-, Z)$, i.e. $\mathrm{Ext}^*$) and, since $D(R)$ is stable, the matching fiber sequence (via $\mathrm{Hom}(Z, -)$). Verify the two connecting [[Def - Homomorphism|homomorphisms]] are the snake-lemma boundary map, up to sign. The non-obvious content is that the "$\delta$" of homological algebra is simultaneously a cofiber and a fiber connecting map.

**Long exact sequences of a pair and of a [[Def - Fibration|fibration]].** For a cofibration pair $A \hookrightarrow X$ with quotient $X/A$ and the associated fibration story, compare the long exact sequence of the pair (cohomology, via cofiber) with the long exact sequence of a fibration (homotopy, via fiber). The theorem explains why the connecting maps are "the same" — they are adjoint transposes — even though the two sequences are usually proved by entirely separate arguments in a first algebraic topology course.

**EHP and the comparison of suspension and loop.** In unstable homotopy theory the EHP sequence interleaves a fiber sequence and a cofiber sequence to compute homotopy [[Def - Group|groups]] of spheres. Recognizing where the agreement theorem (and its failure to be an *isomorphism* on objects, only on mapping sets, because $\mathbf{Top}_*$ is not stable) enters is a genuine application; the non-obviousness is that the unstable phenomena are exactly where "agree up to sign on mapping sets" is weaker than "literally coincide."

---

# Bridges

- **[[Thm - The Suspension-Loop Adjunction]]** — the engine. The agreement is *driven* by the adjunction: the connecting maps of the cofiber and fiber sequences are adjoint transposes, so applying $[-, Z]$ to one and $[Z, -]$ to the other produces the same sequence after the bijection $[\Sigma X, Z] \cong [X, \Omega Z]$. The adjunction is the dictionary; this theorem is the sentence it translates.

- **[[Def - Pre-Triangulated Category|Pre-triangulated category]]** — the destination. This theorem is exactly the verification of the compatibility axiom that defines a pre-triangulated category, so its corollary is "$\mathrm{Ho}(\mathcal{C})$ is pre-triangulated." Everything the pre-triangulated axioms assert about coherence of cofiber and fiber sequences is the content proved here.

- **Triangulated categories and the rotation axiom** — the stable specialization. When $\Sigma$ is invertible the cofiber and fiber sequences do not merely agree on mapping sets but coincide as objects, the two classes merge into distinguished triangles, and the sign here becomes the sign in the triangulated rotation axiom $X \to Y \to Z \to \Sigma X \rightsquigarrow Y \to Z \to \Sigma X \to \Sigma Y$ with a $-1$. The forward page is **Def - Triangulated Category** in the Stable chapter.

- **[[Def - Cofiber and Fiber Sequence|Cofiber and fiber sequences]]** — the objects. This theorem is about the two sequences defined there; it certifies that the long exact sequence of $[-, Z]$ on a cofiber sequence and of $[Z, -]$ on the dual fiber sequence are not two computations but one, which is what justifies calling either "the" long exact sequence of $f$.

---

# Unlocked by This

> [!tip] Triangulated Category *(from the next chapter)*
> The agreement theorem is the model-category source of the **distinguished triangles** of a triangulated category. When $\mathcal{C}$ is stable, the cofiber and fiber sequences literally coincide, the up-to-sign agreement becomes the rotation axiom, and $\mathrm{Ho}(\mathcal{C})$ is triangulated. The octahedral axiom TR4 is the one piece not visible here; it is the further coherence of *iterated* cofibers.

> [!tip] Naturality of Connecting Homomorphisms *(from homological algebra)*
> The identification of the cofiber and fiber connecting maps as adjoint transposes is the abstract reason **connecting homomorphisms are natural** and why the "$\delta$" of the snake lemma, the Mayer–Vietoris boundary, and the long-exact-sequence boundary of a fibration are all the same kind of map. Diagram chases that prove naturality by hand are shadows of this single adjunction-driven agreement.
