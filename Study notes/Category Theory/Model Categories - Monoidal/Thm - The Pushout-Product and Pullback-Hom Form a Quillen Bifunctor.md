---
type: theorem
subject: model-categories
prereqs:
  - "Def - Monoidal Model Category"
  - "Def - Closed Monoidal Category"
  - "Def - Pullback and Pushout"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Quillen Adjunction and Quillen Equivalence"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $(\mathcal{C}, \otimes, I, [-,-])$ is a [[Def - Closed Monoidal Category|closed symmetric monoidal category]] that is also a [[Def - Model Category|model category]]. For maps $f : U \to V$ and $g : X \to Y$, the **pushout-product** is
$$f \mathbin{\square} g : (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y) \to V \otimes Y,$$
induced from the [[Def - Pullback and Pushout|pushout]] of $V \otimes X \xleftarrow{f \otimes 1} U \otimes X \xrightarrow{1 \otimes g} U \otimes Y$. For a map $g : X \to Y$ and a map $p : Z \to W$, the **pullback-hom** (Leibniz cotensor) is
$$\langle g, p\rangle : [Y, Z] \to [X, Z] \times_{[X, W]} [Y, W],$$
the map into the [[Def - Pullback and Pushout|pullback]] induced by $[g, Z] : [Y, Z] \to [X, Z]$ and $[Y, p] : [Y, Z] \to [Y, W]$. Cofibrations are $\rightarrowtail$, fibrations $\twoheadrightarrow$, weak equivalences $\xrightarrow{\sim}$. The full symbol registry is on [[Model Categories — Monoidal Model Categories]].

---

# Statement

> **Theorem (Pushout-Product / Pullback-Hom Quillen Bifunctor).** Let $\mathcal{C}$ be a closed symmetric monoidal model category. For maps $f, g, p$ in $\mathcal{C}$, with $f, g$ cofibrations and $p$ a fibration, the following three conditions are **equivalent**:
> 1. **(pushout-product side)** $f \mathbin{\square} g$ is a cofibration, and it is a trivial cofibration if either $f$ or $g$ is;
> 2. **(pullback-hom side)** for every cofibration $i$ and fibration $p$, the pullback-hom $\langle i, p\rangle$ is a fibration, and it is a trivial fibration if either $i$ or $p$ is;
> 3. **(lifting side)** for cofibrations $i, j$ and fibration $p$, there is a lifting correspondence: a lift of $i \mathbin{\square} j$ against $p$ exists if and only if a lift of $i$ against $\langle j, p\rangle$ exists.
>
> When these hold, the two-variable adjunction $(\otimes, [-,-], [-,-])$ is a **Quillen bifunctor**: the pushout-product axiom (equivalently the pullback-hom condition) is exactly the statement that this two-variable adjunction is "left Quillen". Consequently $\otimes$ admits a total left derived functor $\otimes^{\mathbf{L}} : \mathrm{Ho}(\mathcal{C}) \times \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$ and $[-,-]$ a total right derived functor $\mathbf{R}[-,-]$, and these are adjoint in each variable.

---

# Motivation

The role of this theorem is to package the entire homotopical compatibility of a tensor product into one self-dual statement, and to make the two derived functors — the derived tensor and the derived internal hom — fall out *together* rather than being constructed separately. Before this theorem, one might prove "tensoring with a cofibrant object preserves weak equivalences" and, separately, "the internal hom of a fibrant object is homotopical", as if they were two facts. The theorem says they are *one* fact viewed through the [[Def - Closed Monoidal Category|tensor-hom adjunction]], exactly as in ordinary category theory a closed monoidal structure is the single adjunction $- \otimes B \dashv [B, -]$ rather than two unrelated functors.

The deeper purpose is to identify the [[Def - Monoidal Model Category|pushout-product axiom]] with a recognizable structural notion. A Quillen bifunctor is the two-variable analogue of a left Quillen functor: a [[Def - Quillen Adjunction and Quillen Equivalence|left Quillen functor]] preserves cofibrations and trivial cofibrations, and a Quillen bifunctor does the same "in two variables at once" through the pushout-product. Recognizing the pushout-product axiom as "$\otimes$ is a Quillen bifunctor" means every theorem about left Quillen functors — Ken Brown's lemma, existence of derived functors, descent to homotopy categories — applies, and the derived monoidal structure of the next theorem becomes a corollary rather than a fresh construction.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is the pushout-product axiom, but the skill is recognizing when a problem secretly hands you that axiom, or one of its equivalent forms, even though "pushout-product" is never mentioned.

The first disguised source is **cofibrant generation**. If $\mathcal{C}$ is cofibrantly generated with generating cofibrations $I$ and trivial cofibrations $J$, then to get the full pushout-product axiom it suffices to check it on the *generators*: $I \mathbin{\square} I \subseteq \text{cof}$ and $I \mathbin{\square} J \subseteq \text{triv-cof}$. The bridge is that the class $\{f : f \mathbin{\square} g \in \text{cof for all cofibrations } g\}$ is closed under pushout, transfinite composition, and retract — the closure operations the small object argument respects — so it suffices to contain the generators. The non-obvious part is that an "all cofibrations" quantifier collapses to a finite check. *Example problem:* verify $\mathbf{sSet}$ is a monoidal model category by computing $\partial\Delta^m \mathbin{\square} \partial\Delta^n$ on the generating boundary inclusions and recognizing it as a monomorphism.

The second disguised source is **a visible right lifting property on the internal hom**. Often the tensor side is opaque but the internal hom wears its fibration property on its sleeve. If you can see directly that $\langle i, p\rangle$ has the right lifting property against the (trivial) cofibrations — i.e. is a (trivial) fibration — then by the equivalence in the theorem the pushout-product axiom holds. The bridge is transposition: $i \mathbin{\square} j \perp p \iff i \perp \langle j, p\rangle$. *Example problem:* in $\mathbf{Top}$ (compactly generated), show the mapping space $[Y, Z] \to [X, Z] \times_{[X, W]} [Y, W]$ is a Serre fibration when $X \hookrightarrow Y$ is a cofibration and $Z \to W$ a fibration, deducing the pushout-product axiom for $\times$.

The third disguised source is **an enrichment over a known monoidal model category**. If $\mathcal{M}$ is a $\mathcal{V}$-model category for a monoidal model category $\mathcal{V}$ (e.g. $\mathcal{V} = \mathbf{sSet}$, a simplicial model category), then the action $\otimes : \mathcal{V} \times \mathcal{M} \to \mathcal{M}$ is by definition a Quillen bifunctor — this is the SM7 axiom of enrichment. The bridge is that "simplicial model category" *is* the statement "the tensoring is a Quillen bifunctor". *Example problem:* given that $\mathcal{M}$ is a simplicial model category, deduce that the cotensor $X^K$ for $K \in \mathbf{sSet}$ preserves fibrations of fibrant objects.

**Targets (Output Amplification)**

The bare conclusion is "the two-variable adjunction is a Quillen bifunctor". Combined with other facts it yields the homotopical algebra of the chapter.

Combine the conclusion with **Ken Brown's lemma**. A Quillen bifunctor, restricted to one cofibrant variable, is a left Quillen functor, hence (by Ken Brown) preserves weak equivalences between cofibrant objects. The further result $E$ is that $A \otimes^{\mathbf{L}} B := QA \otimes QB$ is well-defined — independent of the cofibrant replacements chosen — which is the existence of the derived tensor. This is non-obvious because the *bifunctor* statement is about (trivial) cofibrations, and Ken Brown is what converts it into a statement about *all* weak equivalences, the form actually needed to descend to $\mathrm{Ho}$.

Combine the conclusion with **the unit axiom**. The Quillen-bifunctor property makes $\otimes^{\mathbf{L}}$ associative on $\mathrm{Ho}(\mathcal{C})$; adding the unit axiom makes $QI$ a unit. The further result is the full monoidal structure on $\mathrm{Ho}(\mathcal{C})$ of [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|the next theorem]] — the bifunctor theorem supplies the multiplication, the unit axiom supplies the unit, and together they give a monoidal category.

Combine the conclusion with **the closed structure**. Because the bifunctor condition is self-dual under the tensor-hom adjunction, the *same* hypothesis that derives $\otimes^{\mathbf{L}}$ simultaneously derives $\mathbf{R}[-,-] = [Q(-), R(-)]$, with $\mathrm{Ho}(\mathcal{C})(A \otimes^{\mathbf{L}} B, C) \cong \mathrm{Ho}(\mathcal{C})(A, \mathbf{R}[B, C])$. The further result is that $\mathrm{Ho}(\mathcal{C})$ is *closed* monoidal, with a derived internal hom computing, e.g., Ext in $\mathbf{Ch}(R)$. This is non-obvious because nothing in the pushout-product side mentions the internal hom; the closed structure is what makes the single axiom do double duty.

---

# Why Is It True

The heart of the matter is one adjunction identity, applied to a *square*. In a [[Def - Closed Monoidal Category|closed monoidal category]], a map $A \otimes B \to C$ is the same as a map $A \to [B, C]$. The pushout-product and the pullback-hom are what this identity becomes when you feed it *morphisms* (maps of arrows) instead of objects: a lifting problem is a commuting square, and the tensor-hom adjunction turns a square involving $\otimes$ into a square involving $[-,-]$.

Spell it out. A lifting problem of $i \mathbin{\square} j$ against $p$ is, by the universal property of the defining pushout, the same as a *pair* of compatible squares — one for $i$ and one for $j$ — mapping into $p$. Transposing across $- \otimes (\text{second variable}) \dashv [\,(\text{second variable}), -\,]$ turns "maps out of a tensor" into "maps into an internal hom", and the pair of compatible squares becomes a single square of $i$ against the pullback $\langle j, p\rangle$. The pullback is forced: it is exactly the object that records "compatible target data for both faces". So:

> **A lift of $i \mathbin{\square} j$ against $p$ is literally the same datum as a lift of $i$ against $\langle j, p\rangle$ — they are adjoint transposes of one lifting problem.**

Once you believe this, everything follows by abstract nonsense about lifting. Cofibrations are characterized by the left lifting property against trivial fibrations, fibrations by the right lifting property against trivial cofibrations. So "$i \mathbin{\square} j$ is a cofibration" means "$i \mathbin{\square} j$ lifts against every trivial fibration $p$", which transposes to "$i$ lifts against every $\langle j, p\rangle$ for $p$ a trivial fibration" — and that says $\langle j, p\rangle$ is a trivial fibration, i.e. the pullback-hom condition. The equivalence of the two axioms is not a computation; it is the lifting-property characterization run through the adjunction. The triviality clauses match up the same way, by swapping which class ($\text{cof}$ or $\text{triv-cof}$) you test against. The theorem is true because **the pushout-product and the pullback-hom are the two faces of a single adjunction transpose of lifting problems**.

---

# What Makes This Hard

The hard step is not the adjunction itself but seeing that the pushout *corner* on one side corresponds to the pullback *corner* on the other — that $f \mathbin{\square} g$ uses the pushout $(V \otimes X) \sqcup_{U \otimes X}(U \otimes Y)$ precisely so that, after transposing, it matches the pullback $[X, Z] \times_{[X, W]} [Y, W]$ in $\langle g, p\rangle$. Most people get stuck trying to transpose the maps $f \otimes 1$ and $1 \otimes g$ separately and lose track of how the universal properties of the pushout (a colimit, hence "maps out") and the pullback (a limit, hence "maps in") dualize. The common error is to forget the corner entirely and try to relate $f \otimes g$ to $[g, p]$, which simply does not transpose correctly. The discipline is to always phrase both sides as *lifting problems* and let the adjunction act on the whole square at once.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce both axioms to lifting-property characterizations of (trivial) cofibrations and fibrations, then show the two lifting problems — $i \mathbin{\square} j$ against $p$, and $i$ against $\langle j, p\rangle$ — are adjoint transposes of each other. The triviality clauses come for free by swapping which class you test against.

**Subgoal decomposition:**

1. **Recast as lifting.** Express "$i \mathbin{\square} j$ is a (trivial) cofibration" and "$\langle j, p\rangle$ is a (trivial) fibration" purely as lifting statements.
   - *Hint:* A map is a cofibration iff it has the left lifting property against all trivial fibrations; a fibration iff it has the right lifting property against all trivial cofibrations.
   - *Why needed:* It removes the model-categorical classes and leaves only lifting, the only thing the adjunction can act on.

2. **Decompose the pushout-product lifting problem.** Show a square from $i \mathbin{\square} j$ to $p$ is the same as a pair of compatible squares (one for $i$, one for $j$) into $p$.
   - *Hint:* Use the universal property of the pushout $(V \otimes X) \sqcup_{U \otimes X} (U \otimes Y)$: a map out of it is a compatible pair of maps out of $V \otimes X$ and $U \otimes Y$.
   - *Why needed:* It exposes the two-variable nature so each variable can be transposed.

3. **Transpose along $- \otimes (\text{var}) \dashv [(\text{var}), -]$.** Convert the "maps out of $\otimes$" into "maps into $[-,-]$", turning the compatible pair into a single square of $i$ against $\langle j, p\rangle$.
   - *Hint:* The pullback $[X, Z] \times_{[X, W]} [Y, W]$ is the transpose of the pushout; maps into it are compatible pairs of maps into the two internal homs.
   - *Why needed:* This is the bijection of lifting problems, the crux of the theorem.

4. **Read off the equivalence.** Conclude that $i \mathbin{\square} j \perp p$ for all trivial fibrations $p$ iff $i \perp \langle j, p\rangle$ for all such $p$, i.e. the two axioms coincide; repeat with classes swapped for the trivial clauses.
   - *Hint:* "Has LLP against all trivial fibrations" = cofibration; "is a trivial fibration" = "has RLP against all cofibrations".
   - *Why needed:* It packages the lifting bijection back into the model-categorical language of the statement.

5. **Derive the bifunctor consequences.** From the equivalent axioms, restrict to one cofibrant variable, apply Ken Brown, and conclude the total derived functors exist and are adjoint.
   - *Hint:* $- \otimes Z$ for cofibrant $Z$ is a left Quillen functor; Ken Brown gives preservation of weak equivalences between cofibrant objects.
   - *Why needed:* It produces $\otimes^{\mathbf{L}}$ and $\mathbf{R}[-,-]$, the payoff of calling it a Quillen bifunctor.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pushout-product / pullback-hom adjunction of lifting problems
> **Statement:** For maps $i : U \to V$, $j : X \to Y$, $p : Z \to W$ in a [[Def - Closed Monoidal Category|closed monoidal category]], there is a natural bijection between commuting squares from $i \mathbin{\square} j$ to $p$ and commuting squares from $i$ to $\langle j, p\rangle$, compatible with chosen diagonal fillers. Hence $i \mathbin{\square} j$ has the left lifting property against $p$ if and only if $i$ has the left lifting property against $\langle j, p\rangle$.
>
> **Hint:** Apply the tensor-hom adjunction $\mathcal{C}(- \otimes Y, Z) \cong \mathcal{C}(-, [Y, Z])$ to each corner of the square, using the universal property of the pushout (maps out) and the pullback (maps in).
>
> **Why needed:** This single bijection *is* the theorem; everything else is bookkeeping that translates it into the language of model-category classes.
>
> > [!note]- Full proof
> > A commuting square from $i \mathbin{\square} j$ to $p$ consists of maps $a : (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y) \to Z$ and $b : V \otimes Y \to W$ with $p \circ a = b \circ (i \mathbin{\square} j)$. By the universal property of the [[Def - Pullback and Pushout|pushout]], $a$ is a compatible pair $(a_1 : V \otimes X \to Z,\ a_2 : U \otimes Y \to Z)$ agreeing on $U \otimes X$. Transpose everything across $- \otimes Y \dashv [Y, -]$ and $- \otimes X \dashv [X, -]$: the map $b : V \otimes Y \to W$ becomes $\widehat b : V \to [Y, W]$; the map $a_1 : V \otimes X \to Z$ becomes $\widehat{a_1} : V \to [X, Z]$; the map $a_2 : U \otimes Y \to Z$ becomes $\widehat{a_2} : U \to [Y, Z]$. The compatibility of $a_1, a_2$ on $U \otimes X$ and the relation $p \circ a = b \circ (i\mathbin{\square}j)$ transpose exactly to the statement that $(\widehat{a_1}, \text{restriction of }\widehat b)$ assemble into a map $V \to [X, Z] \times_{[X, W]} [Y, W]$ and that the square
> > $$\begin{array}{ccc} U & \xrightarrow{\widehat{a_2}} & [Y, Z] \\ {\scriptstyle i}\downarrow & & \downarrow{\scriptstyle \langle j, p\rangle} \\ V & \longrightarrow & [X, Z] \times_{[X, W]} [Y, W] \end{array}$$
> > commutes. A diagonal filler $V \to [Y, Z]$ for this square transposes back, across $- \otimes Y \dashv [Y, -]$, to a diagonal filler $V \otimes Y \to Z$ for the original square, and conversely. The correspondence is natural in all three maps because the adjunction transpose is. Hence lifts correspond bijectively, proving the lifting-property equivalence.

> [!note]- Lemma 2: The pushout-product class is closed under the cellular operations
> **Statement:** Fix a cofibration $g$. The class $L_g = \{f : f \mathbin{\square} g \text{ is a cofibration}\}$ is closed under pushout, transfinite composition, and retract; likewise $L_g^{\mathrm{triv}} = \{f : f \mathbin{\square} g \text{ is a trivial cofibration}\}$ when $g$ is a trivial cofibration. Consequently, if $\mathcal{C}$ is cofibrantly generated, the pushout-product axiom holds for all cofibrations as soon as it holds for the generating cofibrations.
>
> **Hint:** $- \mathbin{\square} g$ is built from $- \otimes (\text{the objects of } g)$, and $- \otimes Z$ preserves colimits (it is a left adjoint), so it carries the cellular constructions of $f$ to cellular constructions of $f \mathbin{\square} g$; cofibrations are closed under exactly these.
>
> **Why needed:** It is the bridge from "axiom on generators" to "axiom on all cofibrations", the form used in every verification (this is the practical content of the theorem).
>
> > [!note]- Full proof
> > Since $\mathcal{C}$ is [[Def - Closed Monoidal Category|closed]], each functor $- \otimes Z$ is a left adjoint and so preserves all colimits. The pushout-product $f \mathbin{\square} g$ is assembled from $f \otimes 1$ and $1 \otimes g$ via a pushout; for a fixed $g$, the assignment $f \mapsto f \mathbin{\square} g$ commutes with pushouts, transfinite composites, and retracts of $f$, because these are colimit constructions in the arrow category and $- \otimes (\text{objects of } g)$ preserves them. Cofibrations are closed under pushout, transfinite composition, and retract (a standard consequence of their characterization by the left lifting property — by [[Thm - The Retract Argument|the retract argument]] and the closure properties of [[Thm - Closure Properties of the Model Structure]]). Therefore $L_g$ is closed under these operations. If $\mathcal{C}$ is cofibrantly generated with generating cofibrations $\mathcal{I}$, every cofibration is a retract of a transfinite composite of pushouts of maps in $\mathcal{I}$; so if $\mathcal{I} \subseteq L_g$ then all cofibrations lie in $L_g$. Running the same argument in the second variable reduces the axiom to generating cofibrations $g$ as well, and the trivial case is identical with "trivial cofibration" replacing "cofibration".

> [!note]- Lemma 3: One cofibrant variable gives a left Quillen functor; Ken Brown applies
> **Statement:** If the pushout-product axiom holds and $Z$ is cofibrant, then $- \otimes Z$ is a [[Def - Quillen Adjunction and Quillen Equivalence|left Quillen functor]] (it preserves cofibrations and trivial cofibrations). By Ken Brown's lemma it preserves all weak equivalences between cofibrant objects.
>
> **Hint:** Apply the pushout-product axiom with $g = (\varnothing \to Z)$, the cofibration witnessing that $Z$ is cofibrant; then $f \mathbin{\square} g$ is $f \otimes Z$.
>
> **Why needed:** It converts the bifunctor condition into the homotopy-invariance of $- \otimes Z$ on cofibrant objects, which is exactly what makes $\otimes^{\mathbf{L}}$ well-defined.
>
> > [!note]- Full proof
> > Let $g : \varnothing \to Z$ be the unique map, a [[Def - Cofibrant and Fibrant Objects|cofibration]] because $Z$ is cofibrant. For a cofibration $f : U \to V$, the pushout-product $f \mathbin{\square} g$ has source $(V \otimes \varnothing) \sqcup_{U \otimes \varnothing}(U \otimes Z)$; since $- \otimes (-)$ preserves the initial object in each variable ($A \otimes \varnothing = \varnothing$, as $- \otimes A$ is a left adjoint), the pushout simplifies to $U \otimes Z$, and $f \mathbin{\square} g = f \otimes 1_Z = f \otimes Z$. The pushout-product axiom says $f \mathbin{\square} g$ is a cofibration, trivial when $f$ is — i.e. $- \otimes Z$ preserves cofibrations and trivial cofibrations. As $- \otimes Z$ is a left adjoint (with right adjoint $[Z, -]$), it is a left Quillen functor. Ken Brown's lemma: a functor sending trivial cofibrations between cofibrant objects to weak equivalences preserves all weak equivalences between cofibrant objects; the trivial-cofibration preservation just shown supplies the hypothesis. Hence $- \otimes Z$ is homotopical on cofibrant objects.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{C}$ be a closed symmetric monoidal model category.
>
> **Step 0 — the maps are defined.** The pushout-product $f \mathbin{\square} g$ exists because $\mathcal{C}$ has [[Def - Pullback and Pushout|pushouts]] (it is bicomplete as a model category), and the pullback-hom $\langle g, p\rangle$ exists because $\mathcal{C}$ has pullbacks and the internal homs $[X, Z]$ exist by [[Def - Closed Monoidal Category|closedness]].
>
> **Step 1 — equivalence of (1), (2), (3).** By Lemma 1, for any $i, j, p$ there is a natural bijection of lifting problems: $i \mathbin{\square} j$ has the LLP against $p$ if and only if $i$ has the LLP against $\langle j, p\rangle$. Now use the lifting-property characterizations in a model category: a map is a cofibration iff it has the LLP against every trivial fibration, and a trivial cofibration iff against every fibration; dually a map is a trivial fibration iff it has the RLP against every cofibration, and a fibration iff against every trivial cofibration.
>
> Condition (1) says $i \mathbin{\square} j$ is a cofibration for cofibrations $i, j$, i.e. $i \mathbin{\square} j$ has the LLP against every trivial fibration $p$. By Lemma 1 this is: $i$ has the LLP against $\langle j, p\rangle$ for every trivial fibration $p$ and every cofibration $j$. Since this holds for *all* cofibrations $i$, it says $\langle j, p\rangle$ has the RLP against all cofibrations $i$, i.e. $\langle j, p\rangle$ is a trivial fibration whenever $p$ is — which is the trivial half of condition (2). Running the same equivalence with "trivial fibration" replaced by "fibration" and tracking which of $i, j$ is trivial yields the remaining clauses, establishing (1) $\Leftrightarrow$ (2). Condition (3) is the lifting bijection of Lemma 1 itself, which is the engine of both, so (3) $\Leftrightarrow$ (1) $\Leftrightarrow$ (2).
>
> **Step 2 — reduction to generators (practical form).** By Lemma 2, when $\mathcal{C}$ is cofibrantly generated, conditions (1)–(2) for all (trivial) cofibrations follow from the same conditions on the generating (trivial) cofibrations, since the relevant classes are closed under pushout, transfinite composition, and retract. (This step is what makes the axiom checkable; it is not needed for the equivalence but is part of the theorem's content.)
>
> **Step 3 — the two-variable adjunction is a Quillen bifunctor.** The pushout-product axiom (1) is, by definition, the statement that the two-variable adjunction $(\otimes, [-,-], [-,-])$ is a left Quillen two-variable adjunction (a Quillen bifunctor): its pushout-product preserves cofibrations with the triviality propagation. The equivalent form (2) is the right Quillen statement on the pullback-hom.
>
> **Step 4 — total derived functors exist and are adjoint.** By Lemma 3, for cofibrant $Z$ the functor $- \otimes Z$ is left Quillen, hence preserves weak equivalences between cofibrant objects; symmetrically for $A \otimes -$. Therefore $\otimes \circ (Q \times Q)$ descends to a well-defined functor $\otimes^{\mathbf{L}} : \mathrm{Ho}(\mathcal{C}) \times \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$, the **total left derived functor**, independent of the choice of cofibrant replacement $Q$ up to natural isomorphism. Dually, by (2) and Ken Brown for $[Z, -]$ on fibrant objects, $[-, -] \circ (Q^{\mathrm{op}} \times R)$ descends to $\mathbf{R}[-,-]$. The point-set adjunction $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$, derived, gives a natural isomorphism $\mathrm{Ho}(\mathcal{C})(A \otimes^{\mathbf{L}} B, C) \cong \mathrm{Ho}(\mathcal{C})(A, \mathbf{R}[B, C])$ — the derived functors are adjoint in each variable. (That the derived adjunction holds follows from [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] applied to $- \otimes B \dashv [B, -]$ for each fixed cofibrant $B$.) $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Simplicial sets and the combinatorics of products of simplices.** Verify the pushout-product axiom for $(\mathbf{sSet}, \times)$ by computing $\partial\Delta^m \mathbin{\square} \partial\Delta^n$ on generators. The pushout-product is the inclusion $\partial(\Delta^m \times \Delta^n) \hookrightarrow \Delta^m \times \Delta^n$ of the boundary of the prism into the prism, which is a monomorphism, hence a cofibration. This is non-obvious as an *application* because the input is purely combinatorial — products and boundaries of simplices — yet the conclusion is the homotopical statement that the cartesian product is a Quillen bifunctor and $\mathbf{sSet}$ is a simplicial model category.

**Chain complexes and the Koszul sign rule.** In $\mathbf{Ch}(R)$, compute the pushout-product of the generating cofibrations $S^{m-1} \to D^m$ (the maps of sphere and disk complexes). The result is the analogous map for $m + n$, a degreewise-split monomorphism with projective cokernel — a cofibration. The non-obvious recognition is that the Koszul sign in the tensor differential is exactly what makes the pushout corner come out as the correct boundary; getting the signs wrong gives a map that is not even a chain map. This connects the abstract pushout-product to the concrete bookkeeping of the tensor of complexes.

**Enriched homotopy theory and SM7 for topological spaces.** In compactly generated spaces, show that for a cofibration $X \hookrightarrow Y$ and a Serre fibration $Z \to W$, the pullback-hom of mapping spaces $\mathrm{Map}(Y, Z) \to \mathrm{Map}(X, Z) \times_{\mathrm{Map}(X, W)} \mathrm{Map}(Y, W)$ is a Serre fibration, trivial if either input is. This is Quillen's original SM7, and verifying it directly (via the homotopy lifting property and the exponential law) shows the pullback-hom side can be the *easier* side to check — the disguised source where the internal hom wears its fibration property openly.

---

# Bridges

- **[[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|The derived monoidal structure on $\mathrm{Ho}(\mathcal{C})$]]** — the immediate payoff. This theorem supplies the well-defined, associative derived tensor $\otimes^{\mathbf{L}}$ and the derived internal hom; the next theorem adds the unit (via the unit axiom) and the coherence to make $(\mathrm{Ho}(\mathcal{C}), \otimes^{\mathbf{L}}, QI)$ a closed monoidal category. In other words, this theorem is the multiplication, the next is the full algebra.

- **[[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunctions and left Quillen functors]]** — the one-variable analogue. A left Quillen functor preserves cofibrations and trivial cofibrations; a Quillen bifunctor is "left Quillen in two variables at once" via the pushout-product. Fixing one cofibrant variable in a Quillen bifunctor literally produces a left Quillen functor (Lemma 3), so every theorem about derived functors of Quillen adjunctions specializes here.

- **[[Def - Cartesian Closed Category|Cartesian closed categories]]** — the un-homotopified shadow. Set the weak equivalences to be isomorphisms (the trivial model structure); then the pushout-product axiom is vacuous and the statement degenerates to the bare adjunction $- \otimes B \dashv [B, -]$ that *defines* closedness. So the Quillen-bifunctor theorem is the homotopical refinement of "a closed monoidal structure is the tensor-hom adjunction", with cofibrations and fibrations replacing nothing in the degenerate case.

- **Quillen's SM7 and simplicial model categories** — the enriched special case. When the bifunctor is an *action* $\mathcal{V} \times \mathcal{M} \to \mathcal{M}$ of a monoidal model category $\mathcal{V}$ on a model category $\mathcal{M}$, the pushout-product axiom is the SM7 axiom of a **$\mathcal{V}$-model category**. For $\mathcal{V} = \mathbf{sSet}$ this is the definition of a simplicial model category, the setting in which mapping spaces $\mathrm{map}(X, Y)$ are homotopy-invariant and the homotopy theory acquires its ∞-categorical refinement.

---

# Unlocked by This

> [!tip] Derived Tensor, Tor, and Ext *(from Homological Algebra)*
> Applied to $\mathbf{Ch}(R)$, the bifunctor theorem gives a well-defined derived tensor $\otimes^{\mathbf{L}}_R$ and derived internal hom $\mathbf{R}\mathrm{Hom}_R$ on the derived category. Their (co)homology are exactly **Tor** and **Ext**: $H_n(M \otimes^{\mathbf{L}}_R N) = \mathrm{Tor}^R_n(M, N)$ and $H^n \mathbf{R}\mathrm{Hom}_R(M, N) = \mathrm{Ext}_R^n(M, N)$. The classical balancing of Tor and Ext (compute on either variable) is the symmetry of the Quillen bifunctor.

> [!tip] Tensor-Triangulated Geometry *(from Stable Homotopy / Derived Algebra)*
> When $\mathcal{C}$ is also stable, the derived tensor makes $\mathrm{Ho}(\mathcal{C})$ a **tensor-triangulated category**, and the spectrum of prime tensor-ideals (the Balmer spectrum) reconstructs geometry from the monoidal-triangulated structure — recovering $\mathrm{Spec}$ of a ring from $D^{\mathrm{perf}}(R)$ and the chromatic primes from the stable homotopy category. The Quillen-bifunctor property is the foundation on which the tensor structure of this geometry rests.
