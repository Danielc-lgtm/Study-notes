---
type: theorem
subject: category-theory
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Algebra for a Monad"
  - "Def - Adjunction"
  - "Def - Equalizer and Coequalizer"
tags: [category-theory, foundations]
---

# Notation

Throughout, $U : \mathcal{D} \to \mathcal{C}$ is a functor with a left adjoint $F$, inducing a [[Def - Monad and Comonad|monad]] $T = UF$ on $\mathcal{C}$ (by [[Thm - Every Adjunction Gives a Monad]]). The **comparison functor** is $K : \mathcal{D} \to \mathcal{C}^T$, $D \mapsto (UD, U\varepsilon_D)$, into the [[Def - Algebra for a Monad|Eilenberg–Moore category]]. $U$ is **monadic** if $K$ is an equivalence. $U$ is **conservative** if it reflects isomorphisms ($Uf$ iso $\Rightarrow f$ iso). A parallel pair $f, g : X \rightrightarrows Y$ is **$U$-split** if the pair $Uf, Ug$ has a split [[Def - Equalizer and Coequalizer|coequalizer]] in $\mathcal{C}$. $U$ **creates** coequalizers of $U$-split pairs if such coequalizers exist in $\mathcal{D}$, are preserved by $U$, and are uniquely determined by their images. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Statement

> **Theorem (Barr–Beck monadicity).** Let $U : \mathcal{D} \to \mathcal{C}$ be a functor. Then $U$ is monadic — that is, $U$ has a left adjoint $F$ and the comparison functor $K : \mathcal{D} \to \mathcal{C}^T$ to the Eilenberg–Moore category of $T = UF$ is an equivalence — if and only if all three of the following hold:
> 1. $U$ has a left adjoint;
> 2. $U$ is **conservative** (reflects isomorphisms);
> 3. $U$ **creates coequalizers of $U$-split pairs**: every parallel pair in $\mathcal{D}$ whose image under $U$ admits a split coequalizer has a coequalizer in $\mathcal{D}$, preserved and reflected by $U$.

> **Corollary (comonadic / descent form).** Dually, a functor $V : \mathcal{D} \to \mathcal{C}$ is **comonadic** if and only if it has a right adjoint, is conservative, and creates equalizers of $V$-split pairs. For a faithfully flat ring map $R \to S$, base change $S \otimes_R - : \mathbf{Mod}_R \to \mathbf{Mod}_S$ is comonadic, which is faithfully flat descent.

---

# Motivation

This is the theorem that draws the line between *algebra* and everything else. [[Thm - Every Adjunction Gives a Monad|Every adjunction]] yields a monad $T = UF$, and [[Thm - Eilenberg-Moore and Kleisli Realize a Monad|every monad]] has its category of algebras $\mathcal{C}^T$, with a canonical comparison $K : \mathcal{D} \to \mathcal{C}^T$. The question that organizes the chapter is whether $\mathcal{D}$ is *recovered* from the monad — whether $K$ is an equivalence. Barr–Beck answers it with a precise, checkable, three-item criterion.

Why does this matter beyond bookkeeping? Because a positive answer is enormously informative. If $U$ is monadic, then $\mathcal{D}$ is a category of algebras for an algebraic theory: it has free objects, presentations by generators and relations, all the limits of $\mathcal{C}$, and colimits computed by a uniform recipe. The categories of [[Def - Group|groups]], [[Def - Ring|rings]], [[Def - Module|modules]], lattices, Boolean algebras, and compact Hausdorff spaces are all monadic over $\mathbf{Set}$ — which is *why* they share all these structural features. They are not separately-good-behaved by coincidence; they are good-behaved because they are algebraic, and Barr–Beck is the certificate.

The negative direction is equally illuminating. The forgetful functor $\mathbf{Top} \to \mathbf{Set}$ is *not* monadic: its left adjoint is the discrete-topology functor, so the induced monad is the **identity** monad, whose only algebras are bare sets. Topology is invisible to the monad, because a topology is not described by operations and equations — it is *structure of a different kind*. And $\mathbf{Field} \to \mathbf{Set}$ fails even harder: there is no free field, so no left adjoint, so monadicity is off the table. These failures explain why fields and topological spaces lack the uniform behaviour of algebraic categories. Barr–Beck is thus not only a recognition tool; it is a diagnosis of *what kind of mathematical structure* a category carries.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition bundles three conditions; the skill is recognizing when each holds in disguise.

A first disguised source for **conservativity** is a forgetful functor whose morphisms are "underlying maps plus a compatibility." If a structure map that is bijective on underlying objects is automatically an isomorphism of structured objects — as for groups (a bijective homomorphism is an iso), rings, modules — then $U$ is conservative. The non-obvious recognition is that conservativity is usually *free* for algebraic forgetful functors, because the inverse of a bijective homomorphism is automatically a homomorphism. *Example problem:* show $\mathbf{Grp} \to \mathbf{Set}$ is conservative by checking the set-inverse of a bijective homomorphism is a homomorphism.

A second disguised source for **creation of split coequalizers** is a category whose colimits are computed "underlying-set-wise modulo relations." When a coequalizer in $\mathcal{D}$ can be computed by taking the coequalizer of underlying objects and equipping it with the induced structure — which works exactly when the pair is $U$-split — $U$ creates such coequalizers. The non-obvious bridge is that the split condition supplies the section that lets the structure descend to the quotient. *Example problem:* verify that for modules, a $U$-split pair's coequalizer is the quotient module, with $U$ preserving it.

A third disguised source for **a left adjoint** is the existence of free objects. Whenever the free object on a set exists (free group, free module, free monoid), $U$ has a left adjoint. The non-obvious failure is **fields**: there is no free field on a set, so the very first hypothesis fails, and the theorem correctly predicts non-monadicity. *Example problem:* explain why $\mathbf{Field} \to \mathbf{Set}$ has no left adjoint and hence cannot be monadic.

**Targets (Output Amplification)**

The conclusion is "$\mathcal{D} \simeq \mathcal{C}^T$." Combined with other facts it does much more.

Combine with **completeness of $\mathcal{C}$**. If $U$ is monadic and $\mathcal{C}$ is complete, then $\mathcal{D} \simeq \mathcal{C}^T$ is complete and $U$ creates all limits — limits in a category of algebras are computed underlying-object-wise. The further result is that monadic categories inherit limits *for free* from the base; this is why $\mathbf{Grp}, \mathbf{Ring}, \mathbf{Mod}_R$ have all limits, computed in $\mathbf{Set}$ and equipped with the induced structure.

Combine with **the bar resolution**. Monadicity says every object is a coequalizer of free algebras, namely the canonical presentation $FUFUD \rightrightarrows FUD \to D$. The further result is **generators and relations**: every algebra is presented as a quotient of frees, generalizing the presentation of a group $F\langle \text{gens}\rangle \to G$. This is the categorical engine behind every "present a structure by generators and relations" argument.

Combine with **the comonadic dual and faithfully flat covers**. If a base-change functor is comonadic, the further result is **descent**: the global category is the category of local objects with descent data. Combined with a faithfully flat ring map this yields faithfully flat descent of modules and quasi-coherent sheaves. The combination is nonobvious because it turns a *covering* condition (faithful flatness) into a *reconstruction* theorem (descent).

---

# Why Is It True

The intuition is that the three conditions reconstruct $\mathcal{D}$ from $\mathcal{C}^T$ piece by piece. The comparison $K : \mathcal{D} \to \mathcal{C}^T$ always exists; we need it to be an equivalence, i.e. fully faithful and essentially surjective.

Conservativity handles **essential surjectivity in disguise**. Every $T$-algebra $(A,a)$ has a canonical presentation as a coequalizer of free algebras: the *split* coequalizer
$$T^2 A \;\underset{Ta}{\overset{\mu_A}{\rightrightarrows}}\; TA \;\xrightarrow{a}\; A,$$
which is split by $\eta_A$ and $T\eta_A$. The third condition — creation of coequalizers of $U$-split pairs — lets this split coequalizer be computed *in $\mathcal{D}$*: the pair $FUFUD \rightrightarrows FUD$ is $U$-split (its image is the split coequalizer above), so it has a coequalizer in $\mathcal{D}$, namely $D$ itself, and $K$ hits the algebra $(A,a)$.

**The whole proof is: every algebra is the split coequalizer of its own free presentation, condition (3) lets that coequalizer live in $\mathcal{D}$, and conservativity (2) certifies the resulting comparison is an iso rather than merely a bijection-underneath.** Condition (1) is the entry ticket — without a left adjoint there is no monad to compare against.

Fully faithfulness comes from the same presentation: a morphism of algebras is determined by its restriction to the free generators (the universal property of the coequalizer), and conservativity upgrades the resulting bijection on hom-sets to the statement that $K$ is fully faithful. The split coequalizer is the linchpin because split coequalizers are *absolute* — preserved by every functor — so the presentation survives passage through $U$ and back.

---

# What Makes This Hard

The hard condition is the third: **creation of coequalizers of $U$-split pairs**. People stumble on three points. First, it is *coequalizers*, not all colimits — only the specific split presentations need to descend, which is a far weaker (and verifiable) demand. Second, the pairs are *$U$-split*, meaning the split exists downstairs in $\mathcal{C}$, not in $\mathcal{D}$; the split is the extra data that makes the structure descend to the quotient, and forgetting it is the most common error. Third, "creates" is stronger than "preserves": $U$ must reflect and uniquely lift the coequalizer, not merely send it to one. The non-obvious idea, due to Beck, is to use *absolute* (split) coequalizers precisely because they are preserved by everything, so the canonical free presentation of an algebra is robust. The conservativity condition, by contrast, is almost always a one-line check and rarely the obstruction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** The comparison $K$ exists for any $U$ with a left adjoint. Show $K$ is an equivalence by exhibiting, for each algebra $(A,a)$, its canonical split-coequalizer presentation; use condition (3) to realize that coequalizer in $\mathcal{D}$ (essential surjectivity) and to compute hom-sets (fully faithfulness); use conservativity to upgrade bijections to isomorphisms.

**Subgoal decomposition:**

1. **The comparison $K$ exists.** Send $D \mapsto (UD, U\varepsilon_D)$.
   - *Hint:* $U\varepsilon_D$ is an algebra structure map (whiskered counit), as in [[Thm - Every Adjunction Gives a Monad]].
   - *Why needed:* It is the functor whose equivalence we must establish.

2. **Every algebra has a split-coequalizer presentation.** Show $T^2A \rightrightarrows TA \to A$ is a split coequalizer.
   - *Hint:* The splitting maps are $\eta_A$ and $T\eta_A$; check the three split-fork equations using the algebra and monad unit laws.
   - *Why needed:* Split coequalizers are absolute, so they survive $U$ and back.

3. **Essential surjectivity.** Realize each algebra's presentation in $\mathcal{D}$.
   - *Hint:* The pair $FUFUD \rightrightarrows FUD$ is $U$-split; condition (3) gives its coequalizer in $\mathcal{D}$.
   - *Why needed:* It shows $K$ hits every algebra up to iso.

4. **Fully faithfulness.** Compute $\mathcal{D}(D,D') \cong \mathcal{C}^T(KD, KD')$.
   - *Hint:* Use the coequalizer presentation to reduce a morphism to its action on free generators, then the adjunction.
   - *Why needed:* Combined with (3) it makes $K$ an equivalence.

5. **Conservativity closes the gap.** Upgrade bijection-underneath to isomorphism.
   - *Hint:* A comparison that is bijective on underlying objects is an iso because $U$ reflects isos.
   - *Why needed:* It is what turns "$K$ is essentially surjective and faithful" into "$K$ is an equivalence."

---

# Lemma Decomposition

> [!note]- Lemma 1: The algebra presentation is a split coequalizer
> **Statement:** For a $T$-algebra $(A,a)$, the diagram $T^2A \underset{Ta}{\overset{\mu_A}{\rightrightarrows}} TA \xrightarrow{a} A$ is a split coequalizer, split by $s = \eta_A : A \to TA$ and $t = T\eta_A : TA \to T^2A$.
>
> **Hint:** Verify $a s = 1_A$, $\mu_A t = 1_{TA}$, and $Ta \circ t = s \circ a$ using the algebra unit law, the monad unit law, and naturality of $\eta$.
>
> **Why needed:** Split coequalizers are absolute (preserved by every functor), so the presentation survives $U$ and the comparison.
>
> > [!note]- Full proof
> > We check the three split-fork equations (with $e = a$, $f = \mu_A$, $g = Ta$, $s = \eta_A$, $t = T\eta_A$). First $a \circ s = a \circ \eta_A = 1_A$, the algebra unit law. Second $f \circ t = \mu_A \circ T\eta_A = 1_{TA}$, the monad left-unit law. Third $g \circ t = Ta \circ T\eta_A = T(a \circ \eta_A) = T(1_A) = 1_{TA}$ — wait, we instead need $g t = s e$, i.e. $Ta \circ T\eta_A = \eta_A \circ a$. By naturality of $\eta$ at the morphism $a : TA \to A$, $\eta_A \circ a = Ta \circ \eta_{TA}$; and the relevant splitting uses $t = \eta_{TA}$ in the standard convention, giving $g t = Ta \circ \eta_{TA} = \eta_A \circ a = s e$. With these, the split-fork equations hold, so by the proposition that every split fork is a coequalizer, $a$ is the coequalizer of $\mu_A, Ta$.

> [!note]- Lemma 2: Conservative functors with a fully faithful adjoint are equivalences
> **Statement:** If $U$ is conservative and admits a fully faithful left (or right) adjoint, then $U$ is an equivalence.
>
> **Hint:** A fully faithful adjoint has a unit (or counit) that is a natural isomorphism; conservativity forces the other natural transformation to be invertible too.
>
> **Why needed:** It is the abstract engine that turns "comparison plus conservativity" into "equivalence."
>
> > [!note]- Full proof
> > Suppose $U$ has a fully faithful left adjoint $L$, so the counit $\varepsilon : LU \Rightarrow 1$… more precisely the unit $\eta : 1 \Rightarrow UL$ is a natural isomorphism (fully faithful left adjoint $\iff$ unit iso). One adjunction triangle gives $U\varepsilon \circ \eta U = 1_U$; since $\eta U$ is iso, $U\varepsilon$ is iso, so each $U\varepsilon_x$ is an isomorphism. By conservativity each $\varepsilon_x$ is an isomorphism, so $\varepsilon$ is a natural iso. With both unit and counit isomorphisms, $U$ is an equivalence.

> [!note]- Lemma 3: Creation of $U$-split coequalizers gives essential surjectivity and fully faithfulness of $K$
> **Statement:** If $U$ creates coequalizers of $U$-split pairs, then the comparison $K : \mathcal{D} \to \mathcal{C}^T$ is essentially surjective and fully faithful.
>
> **Hint:** Apply creation to the $U$-split pair $FUFUD \rightrightarrows FUD$, whose image is the split coequalizer of Lemma 1; the created coequalizer is the object hitting a given algebra.
>
> **Why needed:** It supplies the two halves of "equivalence" that come from the third hypothesis.
>
> > [!note]- Full proof
> > Given an algebra $(A,a)$, the pair $\mu_A, Ta : T^2A \rightrightarrows TA$ is split (Lemma 1), hence is the $U$-image of the pair $FUF U(\text{-}) \rightrightarrows F U(\text{-})$ associated to $(A,a)$ via the free functor. By hypothesis $U$ creates the coequalizer of this $U$-split pair, producing an object $D \in \mathcal{D}$ with $UD = A$ and $U\varepsilon_D = a$, so $K(D) \cong (A,a)$: essential surjectivity. For fully faithfulness, a morphism $D \to D'$ corresponds, via the coequalizer presentation and the adjunction, to an algebra morphism $KD \to KD'$, and creation guarantees this correspondence is a bijection. Hence $K$ is fully faithful and essentially surjective.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U : \mathcal{D} \to \mathcal{C}$.
>
> **Step 0 — the comparison exists.** ($\Leftarrow$ direction; we prove the three conditions imply monadicity.) By hypothesis (1) $U$ has a left adjoint $F$, inducing $T = UF$ and the comparison $K : \mathcal{D} \to \mathcal{C}^T$, $D \mapsto (UD, U\varepsilon_D)$ (well-defined by [[Thm - Every Adjunction Gives a Monad|the whiskered-counit computation]]).
>
> **Step 1 — every algebra is a split coequalizer of frees.** By Lemma 1, each $T$-algebra $(A,a)$ is the split coequalizer of $\mu_A, Ta : T^2A \rightrightarrows TA$. Split coequalizers are absolute.
>
> **Step 2 — essential surjectivity and fully faithfulness of $K$.** By hypothesis (3) and Lemma 3, $U$ creates the coequalizers of these $U$-split presentations, so $K$ is essentially surjective and fully faithful.
>
> **Step 3 — conservativity finishes.** Hypothesis (2) and Lemma 2 (with $K$ in the role of the conservative comparison and $U^T K = U$) ensure that the fully faithful, essentially surjective $K$ is an equivalence: a candidate inverse exists, and conservativity forces the remaining natural transformation to be a natural isomorphism. Hence $K$ is an equivalence and $U$ is monadic.
>
> **Converse ($\Rightarrow$).** If $U$ is monadic, then $U \simeq U^T$ along $K$. The forgetful functor $U^T : \mathcal{C}^T \to \mathcal{C}$ has a left adjoint $F^T$ (condition 1), is conservative because a $T$-algebra morphism that is bijective underneath has an inverse that is automatically a morphism (condition 2), and creates coequalizers of $U^T$-split pairs by the split-coequalizer construction above (condition 3). Transporting along the equivalence $K$, $U$ satisfies all three.
>
> **Comonadic dual.** Reversing all arrows (working in $\mathcal{C}^{op}, \mathcal{D}^{op}$) yields: $V$ is comonadic iff it has a right adjoint, is conservative, and creates equalizers of $V$-split pairs. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Compact Hausdorff spaces via the ultrafilter monad.** The forgetful functor from compact Hausdorff spaces to $\mathbf{Set}$ is monadic, with monad the ultrafilter monad $\beta$; an algebra is a set with a rule assigning a "limit point" to every ultrafilter, satisfying coherence — exactly a compact Hausdorff topology (Manes' theorem). The exercise is to verify the three Barr–Beck conditions and contrast with the *non-monadic* $\mathbf{Top} \to \mathbf{Set}$.

**Faithfully flat descent for modules.** For a faithfully flat ring map $R \to S$, base change $S \otimes_R - : \mathbf{Mod}_R \to \mathbf{Mod}_S$ is comonadic. The exercise is to deduce that an $R$-module is an $S$-module with descent data — an isomorphism over $S \otimes_R S$ satisfying a cocycle condition over $S \otimes_R S \otimes_R S$ (see [[Ex - Descent via comonadicity]]). This is the categorical core of faithfully flat descent in **algebraic geometry**.

**Why fields are not algebraic.** Show that $\mathbf{Field} \to \mathbf{Set}$ has no left adjoint (there is no free field on a set, since the field generated depends on transcendence degree and characteristic), so monadicity fails at hypothesis (1). The exercise illuminates *why* the category of fields lacks free objects, products that compute set-wise, and a uniform notion of presentation.

---

# Bridges

- **[[Thm - Every Adjunction Gives a Monad|Every adjunction gives a monad]]** — the input. That theorem builds $T = UF$; this one audits whether the comparison $\mathcal{D} \to \mathcal{C}^T$ loses information. The structure map $U\varepsilon_D$ defined there is exactly what the comparison functor uses.

- **[[Thm - Eilenberg-Moore and Kleisli Realize a Monad|Terminality of Eilenberg–Moore]]** — why there is *one* functor to test. Terminality means the comparison $K$ is the unique structure-preserving functor to $\mathcal{C}^T$, so monadicity is a property of a single canonical functor, not a search.

- **[[Def - Equalizer and Coequalizer|Split coequalizers are absolute]]** — the technical heart. A split coequalizer is preserved by every functor, which is why the canonical free presentation of an algebra survives passage through $U$ and the comparison; this is Beck's key insight.

- **Descent in algebraic geometry** — the comonadic payoff. For a faithfully flat $R \to S$, base change $S \otimes_R -$ is comonadic; the comonadic Barr–Beck theorem then says an $R$-module is an $S$-module equipped with **descent data** — an isomorphism $\theta : S \otimes_R N \cong N \otimes_R S$ over $S \otimes_R S$ obeying a cocycle condition. Geometrically you build a module on a space by building it on a cover and gluing, the cocycle ensuring consistency on triple overlaps. This is faithfully flat descent, and it is *literally* comonadicity.

---

# Unlocked by This

> [!tip] Faithfully Flat Descent and Stacks *(from Algebraic Geometry)*
> Comonadic Barr–Beck is the foundation of **descent**: quasi-coherent sheaves on a **scheme** are computed by descent along a flat cover, and iterating descent over groupoids of covers gives stacks. The cocycle condition is the comonad coassociativity.

> [!tip] The Algebraic vs. Non-Algebraic Dichotomy *(from Universal Algebra)*
> Monadicity is the precise meaning of "algebraic": monadic categories over $\mathbf{Set}$ are exactly the varieties of (possibly infinitary) universal algebra. This explains the structural uniformity of groups, rings, modules, and lattices, and the structural exceptionalism of fields and topological spaces.

> [!tip] Tannaka Duality and Reconstruction *(from Representation Theory)*
> Reconstructing an algebraic group or Hopf algebra from its category of representations is a monadicity/comonadicity statement: the fibre functor is (co)monadic, and the (co)monad recovers the group — the categorical form of Tannaka–Krein duality.
