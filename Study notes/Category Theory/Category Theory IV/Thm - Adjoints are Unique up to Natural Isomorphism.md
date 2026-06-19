---
type: theorem
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Thm - The Yoneda Lemma"
  - "Thm - Uniqueness of Universal Objects"
tags: [category-theory, foundations]
---

# Notation

$F, F' : \mathcal{C} \to \mathcal{D}$ and $G, G' : \mathcal{D} \to \mathcal{C}$ are [[Def - Functor|functors]]; $F \dashv G$ means $F$ is left adjoint to $G$ (see [[Def - Adjunction]]). We write $\mathbf{y}$ for the [[Def - The Yoneda Embedding|Yoneda embedding]], $\eta, \eta'$ for units and $\varepsilon, \varepsilon'$ for counits. The full symbol registry is on [[Category Theory IV — Adjunctions]].

---

# Statement

> **Theorem (Uniqueness of Adjoints).** Let $G : \mathcal{D} \to \mathcal{C}$ be a functor. If $F$ and $F'$ are both left adjoint to $G$, then there is a *unique* natural isomorphism $\theta : F \xrightarrow{\cong} F'$ that is compatible with the units, i.e. $\theta_A \text{-translate of } \eta_A$ equals $\eta'_A$ in the sense $G\theta_A \circ \eta_A = \eta'_A$ for all $A$. Dually, if $G$ and $G'$ are both right adjoint to a functor $F$, then $G \cong G'$ by a unique natural isomorphism compatible with the counits.
>
> In particular, a left adjoint to $G$ (or a right adjoint to $F$), *if it exists*, is determined up to unique natural isomorphism.

---

# Motivation

This theorem is what licenses the word "**the**". We speak of *the* free group, *the* tensor product, *the* Stone–Čech compactification, *the* product — but each is defined only by a universal property or an adjunction, not by an explicit formula, and different textbooks build them differently (reduced words versus equivalence classes of words; one tensor construction versus another). The theorem guarantees these are all the same up to a *canonical* isomorphism, so the choice of construction does not matter and the definite article is justified.

It also justifies a powerful laziness. To find an adjoint you may use *any* convenient construction — whichever is easiest to write down — and the theorem assures you that you have found the only one. There is never a worry that a cleverer construction would give a genuinely different adjoint; adjoints are rigid.

The deeper message is that an adjoint is a *solution to a universal problem*, and universal problems have unique solutions. The left adjoint $F$ is the functor solving "represent $\mathcal{C}(A, G-)$ for each $A$", and representing objects are unique up to unique isomorphism. So the uniqueness of adjoints is not a separate fact — it is uniqueness of representing objects, applied uniformly in $A$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "two functors, both adjoint on the same side to the same functor", so the source question is: *when do you secretly have two adjoints to compare?*

The first source is **two constructions claimed to solve the same universal problem**. Whenever a definition is given by a universal property and you have two candidate constructions, you have two adjoints (or two universal objects) and the theorem identifies them. *Example problem:* show the two standard constructions of the [[Def - Tensor Product of Modules|tensor product]] (via the free module on $A\times M$ modulo bilinearity, versus via generators-and-relations on symbols $a\otimes m$) are canonically isomorphic — both are left adjoint to $\mathrm{Hom}_R(M,-)$, so they agree.

The second source is **a functor known to have an adjoint, plus a guessed formula**. If you can prove $G$ has *some* left adjoint (say by the [[Thm - The Adjoint Functor Theorem|Adjoint Functor Theorem]]) and you can also write down a candidate $F'$ satisfying the adjunction, the theorem tells you $F' $ *is* the left adjoint. *Example problem:* the AFT proves the forgetful functor $\mathbf{Grp}\to\mathbf{Set}$ has a left adjoint without naming it; the explicit free-group construction is then *the* left adjoint by uniqueness.

The third source is **comparing adjunctions built from different presentations**. Given an adjunction presented via a hom-set bijection and another via unit-counit, if both are left adjoint to the same $G$, they coincide. *Example problem:* two authors define abelianisation differently (quotient by commutators versus universal abelian quotient); both are left adjoint to $\mathbf{Ab}\hookrightarrow\mathbf{Grp}$, so they are canonically isomorphic.

**Targets (Output Amplification)**

The conclusion is "$F \cong F'$ canonically"; combined with other facts it does more.

Combine with **a symmetry or duality of the situation**: if a construction is left adjoint to $G$ and *also*, by some symmetry, manifestly isomorphic to another construction, uniqueness forces a nontrivial identity. The further result $E$ is an isomorphism you might not have guessed — for instance, two different colimit formulas for the same left adjoint must agree.

Combine with **functoriality in a parameter**: if $G_t$ varies in a parameter $t$ and each has a left adjoint $F_t$, uniqueness makes $t \mapsto F_t$ functorial automatically, because the comparison isomorphisms are canonical and compose coherently. The further result is that adjoints can be chosen to vary continuously/functorially without extra work.

Combine with **the Eilenberg–Moore comparison** (Chapter V): different adjunctions can induce the *same* monad $GF$; uniqueness of adjoints does *not* say the adjunctions are the same (they need not be — Kleisli and Eilenberg–Moore both realise a monad), but it does pin down each adjoint relative to its own right adjoint. Recognising this boundary — adjoints to a *fixed* functor are unique, but a monad's resolutions are not — is itself a useful target.

---

# Why Is It True

The reason is the [[Thm - The Yoneda Lemma|Yoneda lemma]] applied through the adjunction. To say $F$ is left adjoint to $G$ is to say $FA$ **represents** the functor $\mathcal{C}(A, G-) : \mathcal{D} \to \mathbf{Set}$, for each $A$, with representing element the unit $\eta_A$. If $F'$ is also left adjoint to $G$, then $F'A$ represents *the same functor* $\mathcal{C}(A, G-)$. But a representable functor has a representing object that is unique up to a unique isomorphism — that is precisely [[Thm - Uniqueness of Universal Objects|uniqueness of universal/representing objects]]. So for each $A$ there is a unique isomorphism $\theta_A : FA \xrightarrow{\cong} F'A$ matching the two units, and naturality of the family $\{\theta_A\}$ is forced because all the comparison maps are canonical.

> **The mechanism in one line:** a left adjoint represents $\mathcal{C}(A, G-)$, and representing objects are unique up to unique isomorphism — so two left adjoints to $G$ represent the same functor and must be canonically isomorphic.

Phrased via the Yoneda embedding: the adjunction says $\mathbf{y}(FA) \cong \mathcal{C}(A, G-) \cong \mathbf{y}(F'A)$ as functors, and $\mathbf{y}$ is [[Thm - The Yoneda Embedding is Fully Faithful|fully faithful]], so an isomorphism between the representing functors comes from a unique isomorphism $FA \cong F'A$. Fully-faithfulness of Yoneda is exactly what turns "the represented functors are isomorphic" into "the representing objects are isomorphic, uniquely". There is no room for a non-canonical or non-unique comparison.

---

# What Makes This Hard

The subtlety is the word *unique* and the *compatibility with units*. It is easy to produce *some* isomorphism $FA \cong F'A$ for each $A$; the work is checking it is (a) natural in $A$ and (b) the *unique* one matching the units — and that these two requirements are in fact automatic from Yoneda rather than extra conditions to impose. The common error is to construct the pointwise isomorphisms and forget to verify naturality, or to claim uniqueness without pinning down *which* isomorphism (there can be many isomorphisms $FA \cong F'A$ in general; only one respects the units). A second pitfall is over-claiming: the theorem says adjoints to a *fixed* functor are unique, not that a given functor has at most one adjunction structure floating around or that a monad has a unique resolution.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Both adjunctions exhibit $FA$ and $F'A$ as representing objects of the *same* functor $\mathcal{C}(A, G-)$. Invoke uniqueness of representing objects to get a canonical iso $\theta_A$ at each $A$, then show naturality follows from the canonicity.

**Subgoal decomposition:**

1. **Both adjoints represent the same functor.** Show $\mathcal{D}(FA, -) \cong \mathcal{C}(A, G-) \cong \mathcal{D}(F'A, -)$ as functors $\mathcal{D} \to \mathbf{Set}$, for each $A$.
   - *Hint:* These are just the two adjunction bijections; compose one with the inverse of the other.
   - *Why needed:* Reduces the problem to comparing two representing objects of one functor.

2. **Get a unique pointwise isomorphism.** Apply uniqueness of representing objects (Yoneda) to obtain a unique iso $\theta_A : FA \cong F'A$ matching the universal elements (units).
   - *Hint:* The composite natural iso $\mathcal{D}(FA,-)\cong\mathcal{D}(F'A,-)$ corresponds under [[Thm - The Yoneda Embedding is Fully Faithful|fully faithful Yoneda]] to a unique iso $FA\cong F'A$; track that it sends $\eta_A \mapsto \eta'_A$.
   - *Why needed:* Produces the comparison and its uniqueness simultaneously.

3. **Naturality of $\theta$.** Show $\theta$ is a natural transformation $F \Rightarrow F'$.
   - *Hint:* For $h : A\to A'$, both $\theta_{A'}\circ Fh$ and $F'h\circ\theta_A$ are morphisms $FA\to F'A'$ matching the units; uniqueness forces them equal.
   - *Why needed:* Upgrades the pointwise isos to a natural isomorphism of functors.

---

# Lemma Decomposition

> [!note]- Lemma 1: A left adjoint represents $\mathcal{C}(A, G-)$
> **Statement:** If $F \dashv G$, then for each $A \in \mathcal{C}$ the functor $\mathcal{C}(A, G-) : \mathcal{D} \to \mathbf{Set}$ is [[Def - Hom-Functor and Representable Functor|representable]], represented by $FA$ with universal element $\eta_A \in \mathcal{C}(A, GFA)$.
>
> **Hint:** The adjunction *is* the natural iso $\mathcal{D}(FA,-)\cong\mathcal{C}(A,G-)$; the universal element is the image of $1_{FA}$, which is $\eta_A$.
>
> **Why needed:** Recasts "left adjoint" as "representing object", which is the form uniqueness applies to.
>
> > [!note]- Full proof
> > By definition of $F\dashv G$, there is a natural isomorphism $\Phi_{A,-} : \mathcal{D}(FA, -) \xrightarrow{\cong} \mathcal{C}(A, G-)$ of functors $\mathcal{D}\to\mathbf{Set}$. This is exactly a representation of $\mathcal{C}(A, G-)$ by the object $FA$. The corresponding universal element is $\Phi_{A,FA}(1_{FA}) = \eta_A$ (the unit), by definition of the unit in [[Def - Unit and Counit of an Adjunction]].

> [!note]- Lemma 2: Representing objects are unique up to unique isomorphism
> **Statement:** If $X$ and $X'$ both represent a functor $K : \mathcal{D}\to\mathbf{Set}$ (with universal elements $u, u'$), there is a unique isomorphism $\theta : X \cong X'$ with $K(\theta)(u) = u'$.
>
> **Hint:** This is [[Thm - Uniqueness of Universal Objects|uniqueness of universal objects]] / fully faithful [[Thm - The Yoneda Embedding is Fully Faithful|Yoneda]]: a natural iso $\mathbf{y}X\cong\mathbf{y}X'$ comes from a unique iso $X\cong X'$.
>
> **Why needed:** Supplies the comparison isomorphism and its uniqueness in one stroke.
>
> > [!note]- Full proof
> > Both representations give natural isos $\mathbf{y}X = \mathcal{D}(X,-)\cong K \cong \mathcal{D}(X',-) = \mathbf{y}X'$. Composing yields a natural iso $\mathbf{y}X\cong\mathbf{y}X'$. Since $\mathbf{y}$ is fully faithful, this comes from a unique morphism $\theta : X\to X'$, which is an isomorphism (its inverse comes from the inverse natural iso). Tracking universal elements, $\theta$ is the unique iso with $K(\theta)(u) = u'$.

> [!note]- Lemma 3: The pointwise comparison is natural
> **Statement:** The isomorphisms $\theta_A : FA\cong F'A$ from Lemma 2 form a natural transformation $\theta : F\Rightarrow F'$.
>
> **Hint:** For $h : A\to A'$, show $\theta_{A'}\circ Fh$ and $F'h\circ\theta_A$ both match the units, then use uniqueness.
>
> **Why needed:** Naturality is what makes $\theta$ a natural isomorphism of functors, not just a family of isos.
>
> > [!note]- Full proof
> > Fix $h : A\to A'$ in $\mathcal{C}$. Both $\theta_{A'}\circ Fh$ and $F'h\circ\theta_A$ are morphisms $FA\to F'A'$. Using the unit-compatibility $G\theta_A\circ\eta_A = \eta'_A$ and naturality of $\eta, \eta'$, one computes that each of $G(\theta_{A'}\circ Fh)\circ\eta_A$ and $G(F'h\circ\theta_A)\circ\eta_A$ equals $\eta'_{A'}\circ h$. By the universal property of $\eta_A$ (initiality, from Lemma 1), there is a *unique* morphism $FA\to F'A'$ whose $G$-image composed with $\eta_A$ is $\eta'_{A'}\circ h$. Hence $\theta_{A'}\circ Fh = F'h\circ\theta_A$, the naturality square.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — setup.** Let $F\dashv G$ and $F'\dashv G$ with units $\eta, \eta'$. Fix $A\in\mathcal{C}$.
>
> **Step 1 — both represent the same functor.** By Lemma 1, $\mathcal{D}(FA,-)\cong\mathcal{C}(A,G-)$ and $\mathcal{D}(F'A,-)\cong\mathcal{C}(A,G-)$ naturally. Composing, $\mathcal{D}(FA,-)\cong\mathcal{D}(F'A,-)$ as functors $\mathcal{D}\to\mathbf{Set}$, i.e. $\mathbf{y}(FA)\cong\mathbf{y}(F'A)$.
>
> **Step 2 — unique comparison isomorphism.** By Lemma 2 (uniqueness of representing objects, via fully faithful Yoneda), there is a unique isomorphism $\theta_A : FA\xrightarrow{\cong} F'A$ corresponding to this natural iso, and it is the unique one satisfying $G\theta_A\circ\eta_A = \eta'_A$.
>
> **Step 3 — naturality.** By Lemma 3, the family $\theta = \{\theta_A\}$ is a natural transformation $F\Rightarrow F'$; being pointwise an isomorphism, it is a natural isomorphism.
>
> **Step 4 — uniqueness of $\theta$.** Any natural iso $F\cong F'$ compatible with the units restricts at each $A$ to an iso $FA\cong F'A$ matching units, which by Lemma 2 is $\theta_A$. So $\theta$ is the unique unit-compatible natural isomorphism.
>
> **Step 5 — dual statement.** Apply the argument in $\mathcal{C}^{op}, \mathcal{D}^{op}$ (where left adjoints become right adjoints) to conclude right adjoints to a fixed $F$ are unique up to unique counit-compatible natural isomorphism. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The free group, two ways.** Construct the [[Def - Free Group and Free Product|free group]] on $S$ both as reduced words and as the fundamental group of a wedge of circles indexed by $S$. Both are left adjoint to $\mathbf{Grp}\to\mathbf{Set}$; the theorem forces a canonical isomorphism, which is the topological realization of "generators = loops". This shows uniqueness of adjoints producing a non-obvious identification across algebra and topology.

**Tensor product constructions.** Show the two textbook constructions of $A\otimes_R M$ agree canonically by recognising both as the left adjoint to $\mathrm{Hom}_R(M,-)$. This is the cleanest possible proof that "the" tensor product is well-defined, and it avoids comparing the constructions element by element.

**Limits as adjoints.** The limit functor $\lim : [\mathcal{J},\mathcal{C}]\to\mathcal{C}$ is right adjoint to the constant-diagram functor $\Delta$. Any two constructions of limits (say, via products-and-equalizers versus a direct universal property) are canonically isomorphic because both are right adjoint to $\Delta$ — uniqueness of adjoints gives uniqueness of limits, recovering [[Thm - Limits are Unique up to Unique Isomorphism|the uniqueness of limits]] as a special case.

---

# Bridges

- **[[Thm - Uniqueness of Universal Objects|Uniqueness of Universal Objects]]** — this theorem is its uniform-in-$A$ version. A single universal object is unique up to unique isomorphism; an adjoint is a *functor's worth* of universal objects, and the comparison isomorphisms assemble naturally precisely because each is canonical. Uniqueness of adjoints is "uniqueness of universal objects, with a parameter".

- **[[Thm - The Yoneda Embedding is Fully Faithful|Fully Faithful Yoneda]]** — the load-bearing fact. It is what converts "the represented functors $\mathcal{D}(FA,-)$ and $\mathcal{D}(F'A,-)$ are naturally isomorphic" into "the objects $FA$ and $F'A$ are isomorphic by a unique morphism". Without full faithfulness the comparison would not be canonical.

- **[[Thm - Limits are Unique up to Unique Isomorphism|Uniqueness of Limits]]** — a special case. Limits are right adjoints to the diagonal/constant-diagram functor, so their uniqueness is this theorem applied to that adjunction.

- **[[Def - Monad and Comonad|Resolutions of a Monad]]** (Chapter V) — the boundary case. Adjoints to a *fixed* functor are unique, but a monad arises from *many* adjunctions (Kleisli and Eilenberg–Moore are both resolutions and are genuinely different). The distinction sharpens what this theorem does and does not say.

---

# Unlocked by This

> [!tip] Well-Definedness of Universal Constructions Everywhere *(from all of mathematics)*
> This theorem is the silent justification behind every "the" attached to a universal construction: **the** free object, **the** tensor product, **the** Stone–Čech compactification, **the** localization, **the** sheafification, **the** product and coproduct. Each is an adjoint or a universal object, and this theorem guarantees the construction is independent of presentation up to canonical isomorphism.

> [!tip] Coherence and Strictification *(from Higher Category Theory)*
> Uniqueness-up-to-canonical-isomorphism is the seed of **coherence theorems**: when isomorphisms are canonical, the diagrams they fill commute automatically, which is how Mac Lane's coherence for monoidal categories and the strictification of bicategories are proved. The canonicity here is the prototype.
