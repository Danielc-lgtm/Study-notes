---
type: theorem
subject: category-theory
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Preservation, Reflection, and Creation of Limits"
  - "Def - The Yoneda Embedding"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a locally small [[Def - Category|category]], $X \in \mathcal{C}$ an object, and $\mathcal{C}(X, -) : \mathcal{C} \to \mathbf{Set}$ the covariant **hom-functor**, sending $Y$ to the hom-set $\mathcal{C}(X, Y)$ and $h : Y \to Y'$ to post-composition $h \circ (-)$. Its contravariant sibling is $\mathcal{C}(-, X) : \mathcal{C}^{op} \to \mathbf{Set}$. We write $D : J \to \mathcal{C}$ for a diagram, $\lim D$, $\operatorname{colim} D$ for its [[Def - Limit and Colimit|limit and colimit]], and $\mathbf{y}$ for the [[Def - The Yoneda Embedding|Yoneda embedding]]. The full registry is on [[Category Theory III — Limits and Colimits]].

---

# Statement

> **Theorem (representable functors preserve limits).** For any object $X$ of a locally small category $\mathcal{C}$, the covariant hom-functor $\mathcal{C}(X, -) : \mathcal{C} \to \mathbf{Set}$ [[Def - Preservation, Reflection, and Creation of Limits|preserves]] all limits that exist in $\mathcal{C}$. Explicitly, for any diagram $D : J \to \mathcal{C}$ whose limit exists, there is an isomorphism, natural in $X$,
> $$\mathcal{C}\big(X, \lim_J D\big) \;\cong\; \lim_J\, \mathcal{C}(X, D_-) \;=\; \Big\{\,(\phi_j)_j \in \textstyle\prod_j \mathcal{C}(X, D_j) : D(f) \circ \phi_j = \phi_k \,\Big\}.$$

> **Corollary (contravariant form).** The contravariant hom-functor $\mathcal{C}(-, X) : \mathcal{C}^{op} \to \mathbf{Set}$ sends colimits in $\mathcal{C}$ to limits in $\mathbf{Set}$:
> $$\mathcal{C}\big(\operatorname{colim}_J D, X\big) \;\cong\; \lim_{J^{op}}\, \mathcal{C}(D_-, X).$$

> **Corollary (Yoneda embedding).** The Yoneda embedding $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$ preserves and reflects all limits. (It does not in general *create* them.)

---

# Motivation

This theorem is the precise statement of why universal properties are *always phrased through hom-sets*. Every limit in this chapter was defined by a clause about maps into it — "a map into the [[Def - Product and Coproduct|product]] is a pair of maps", "a map into the [[Def - Pullback and Pushout|pullback]] is a compatible pair", "a map into the limit is a [[Def - Cone and Cocone|cone]]". This theorem says those clauses are not coincidences of presentation; they are the *single fact* that mapping into a limit is the same as forming a limit of mappings. The hom-functor $\mathcal{C}(X, -)$ turns the limit $\lim D$ inside $\mathcal{C}$ into the limit of the hom-sets $\mathcal{C}(X, D_j)$ inside $\mathbf{Set}$, and the elements of that limit of sets are exactly compatible families of maps — which is to say, cones with apex $X$.

The motivation is twofold. First, it *explains* the definitions: the universal property of a limit is literally the assertion that $\mathcal{C}(X, \lim D) = \mathrm{Cone}(X, D)$, and this theorem is that assertion read as "hom preserves limits". Second, it is the *seed of RAPL* — [[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]] — because every right adjoint $G$ satisfies $\mathcal{D}(X, G-) \cong \mathcal{C}(FX, -)$, a hom-functor in disguise, so its limit-preservation reduces to this theorem. It is also the engine that lets the $\mathbf{Set}$-level computation of limits ([[Thm - Limits in Set and in Functor Categories]]) govern *every* category: because hom-sets into a limit form a limit of sets, and limits of sets are compatible families, every limit anywhere is detected by compatible families of maps.

The contravariant corollary is equally important and slightly surprising: maps *out of* a colimit form a *limit* of hom-sets. This is the duality that explains why coproducts turn into products under hom ($\mathcal{C}(A + B, X) \cong \mathcal{C}(A, X) \times \mathcal{C}(B, X)$) and is, geometrically, why $\mathrm{Spec}$ sends colimits of rings to limits of schemes.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "the functor is (or contains) a hom-functor". The skill is recognising hom-functors in disguise, because almost every concretely-defined functor to $\mathbf{Set}$ is one.

The first disguised source is **a right adjoint**. If $G : \mathcal{D} \to \mathcal{C}$ has a left adjoint $F$, then $\mathcal{C}(c, G d) \cong \mathcal{D}(Fc, d)$, so $G$'s effect on hom-sets is governed by a hom-functor; this theorem then forces $G$ to preserve limits. The non-obvious step is recognising a functor as a right adjoint (forgetful functors, the inclusion of a reflective subcategory). *Example problem:* prove the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ preserves products by exhibiting it as a right adjoint to the free-group functor, then invoking limit-preservation.

The second disguised source is **any "set of structure-preserving maps" functor**. Functors like "global sections", "points", "invariants $(-)^G$", "elements satisfying an equation" are typically representable: $(-)^G \cong \mathcal{C}(\mathbb{Z}[G/G], -)$-style. The non-obvious step is identifying the representing object. *Example problem:* show that the functor $R \mapsto \{r \in R : r^2 = r\}$ on commutative rings (idempotents) is representable, hence preserves limits of rings.

The third disguised source is **the Yoneda embedding applied to recognise a limit**. Because $\mathbf{y}$ preserves and reflects limits, to check that a cone in $\mathcal{C}$ is a limit it suffices to check that the induced cone of representables is a limit of presheaves — computed [[Thm - Limits in Set and in Functor Categories|pointwise]] in $\mathbf{Set}$. The non-obvious use is *reducing a limit question in an abstract category to compatible families of maps*. *Example problem:* verify a candidate pullback square is cartesian by checking that for every test object $X$ the induced square of hom-sets is a pullback of sets.

**Targets (Output Amplification)**

The conclusion is "$\mathcal{C}(X, \lim D) \cong \lim \mathcal{C}(X, D_j)$".

Combine with **the $\mathbf{Set}$ description of limits**. The right-hand side is a limit *in $\mathbf{Set}$*, hence the set of compatible families of maps $X \to D_j$. The further result is the operational definition "a map into a limit is a compatible family of maps into the diagram", which is how one *constructs* maps into any limit in practice — produce the components, check compatibility. This is the most-used consequence.

Combine with **reflection to certify limits**. Since $\mathbf{y}$ reflects limits, if the hom-functors $\mathcal{C}(X, -)$ all carry a candidate cone to a limit of sets, the candidate was a limit. The further result is a *test for limithood*: a cone is a limit iff it induces a limit on all hom-sets — the representable criterion, used to verify universal constructions without building the limit by hand.

Combine with **the contravariant form and adjunctions**. $\mathcal{C}(\operatorname{colim} D, X) \cong \lim \mathcal{C}(D_j, X)$ is the basis of "a map out of a colimit is a compatible family of maps out of the pieces", which combined with an adjunction $F \dashv G$ shows left adjoints preserve colimits. The further result is the full RAPL/LAPC dictionary and, via $\mathrm{Spec}$, the colimit-to-limit transfer in algebraic geometry.

---

# Why Is It True

The proof is almost a tautology once you see what the two sides *say*. The left side, $\mathcal{C}(X, \lim D)$, is the set of maps from $X$ into the limit. By the very [[Def - Limit and Colimit|definition of the limit]], a map $X \to \lim D$ is the same thing as a [[Def - Cone and Cocone|cone over $D$ with apex $X$]] — that is the universal property, no more. The right side, $\lim_J \mathcal{C}(X, D_-)$, computed in $\mathbf{Set}$, is the set of compatible families $(\phi_j : X \to D_j)$ with $D(f)\phi_j = \phi_k$ — which is *also* exactly a cone over $D$ with apex $X$. So both sides are the set of cones $\mathrm{Cone}(X, D)$, and the isomorphism is the identity on cones.

> **Mapping into a limit = a compatible family of mappings = a limit of hom-sets.** The hom-functor preserves the limit because "cone with apex $X$" can be read either as "a single map into $\lim D$" or as "a compatible family of maps", and these are the two sides of the equation.

There is nothing to compute; the content is the *recognition* that the universal property of $\lim D$ and the $\mathbf{Set}$-construction of $\lim \mathcal{C}(X, D_j)$ describe the same object — cones. The naturality in $X$ is automatic because precomposition by $X' \to X$ acts the same way on both descriptions.

The contravariant corollary follows by the same move in $\mathcal{C}^{op}$: a colimit in $\mathcal{C}$ is a limit in $\mathcal{C}^{op}$, and $\mathcal{C}(-, X)$ is a covariant hom-functor on $\mathcal{C}^{op}$, so it preserves that limit — which is a colimit downstairs being turned into a limit of sets. The Yoneda corollary is then "preserves limits, one representable at a time, and reflects because a cone is a limit iff it is a limit on all hom-sets".

---

# What Makes This Hard

The difficulty is not the proof — it is *believing it is that easy* and not over-complicating it. The genuine subtleties are two. First, the theorem is about *covariant* hom and *limits*: the contravariant hom sends *colimits* (not limits) to limits, and getting the variance/duality backwards is the standard error. Second, "preserves and reflects but does not create" for the Yoneda embedding trips people up: $\mathbf{y}$ detecting limits (reflection) does not mean it manufactures them in $\mathcal{C}$ — a limit of representables may exist in the presheaf category without being representable, so the limit need not exist in $\mathcal{C}$, which is exactly why $\mathbf{y}$ creates nothing. The conceptual hurdle is internalising that the universal property of a limit *is* the preservation statement, so that the theorem reads as a definition unwound.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Identify both $\mathcal{C}(X, \lim D)$ and $\lim \mathcal{C}(X, D_j)$ with the set of cones $\mathrm{Cone}(X, D)$, the first by the limit's universal property and the second by the $\mathbf{Set}$-description of limits. The isomorphism is the identity on cones.

**Subgoal decomposition:**

1. **Maps into the limit are cones.** Show $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$.
   - *Hint:* This is the universal property of $\lim D$: post-compose the limit projections with a map $X \to \lim D$ to get a cone, and conversely.
   - *Why needed:* It computes the left-hand side.

2. **Compatible families of maps are cones.** Show $\lim_J \mathcal{C}(X, D_-) \cong \mathrm{Cone}(X, D)$.
   - *Hint:* By the $\mathbf{Set}$-limit description, an element of $\lim_J \mathcal{C}(X, D_-)$ is a compatible family $(\phi_j)$ with $D(f)\phi_j = \phi_k$ — precisely a cone.
   - *Why needed:* It computes the right-hand side.

3. **Match the two.** Conclude $\mathcal{C}(X, \lim D) \cong \lim_J \mathcal{C}(X, D_-)$, naturally in $X$.
   - *Hint:* Both are $\mathrm{Cone}(X, D)$; the comparison map sends a map $X \to \lim D$ to the family of its composites with the projections, and this is the identity on cones.
   - *Why needed:* It is the theorem; naturality makes it functorial.

4. **Dualize and Yoneda-ize.** Apply in $\mathcal{C}^{op}$ for the contravariant/colimit form; conclude $\mathbf{y}$ preserves and reflects limits.
   - *Hint:* $\mathbf{y}(c) = \mathcal{C}(-, c)$; limits of presheaves are pointwise, and pointwise this is the preservation statement.
   - *Why needed:* It delivers the corollaries.

---

# Lemma Decomposition

> [!note]- Lemma 1: Maps into a limit are cones
> **Statement:** For a diagram $D : J \to \mathcal{C}$ with limit $(\pi_j : \lim D \to D_j)$, post-composition $h \mapsto (\pi_j \circ h)_j$ is a natural bijection $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$.
>
> **Hint:** This is the universal property of the limit verbatim: every cone factors uniquely through the limit cone.
>
> **Why needed:** It evaluates the left-hand side of the theorem.
>
> > [!note]- Full proof
> > Given $h : X \to \lim D$, the family $(\pi_j h)$ satisfies $D(f)(\pi_j h) = (D(f)\pi_j) h = \pi_k h$, so it is a cone. Conversely, by the universal property, every cone $(\lambda_j : X \to D_j)$ factors as $\lambda_j = \pi_j h$ for a unique $h$. So $h \mapsto (\pi_j h)$ is a bijection, natural in $X$ since precomposing $h$ by $g : X' \to X$ precomposes each $\pi_j h$ by $g$.

> [!note]- Lemma 2: Elements of a limit of hom-sets are compatible families of maps
> **Statement:** For $D : J \to \mathcal{C}$, the limit in $\mathbf{Set}$ of the diagram $j \mapsto \mathcal{C}(X, D_j)$ is the set of families $(\phi_j) \in \prod_j \mathcal{C}(X, D_j)$ with $D(f) \circ \phi_j = \phi_k$ for all $f : j \to k$, i.e. the set of cones $\mathrm{Cone}(X, D)$.
>
> **Hint:** Apply the compatible-family description of limits in $\mathbf{Set}$ to the hom-set diagram, whose transition maps are post-composition by $D(f)$.
>
> **Why needed:** It evaluates the right-hand side.
>
> > [!note]- Full proof
> > The diagram $\mathcal{C}(X, D_-) : J \to \mathbf{Set}$ sends $f : j \to k$ to $\mathcal{C}(X, D(f)) = D(f) \circ (-)$. By the $\mathbf{Set}$-limit description ([[Thm - Limits in Set and in Functor Categories]]), its limit is $\{(\phi_j) : D(f)\circ\phi_j = \phi_k\}$ — exactly the cones over $D$ with apex $X$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{C}$ be locally small, $X \in \mathcal{C}$, and $D : J \to \mathcal{C}$ a diagram whose limit exists.
>
> **Step 0 — both sides are defined.** $\mathcal{C}$ is locally small so all hom-sets are sets; $\lim D$ exists by hypothesis; the diagram $\mathcal{C}(X, D_-) : J \to \mathbf{Set}$ has a limit since $\mathbf{Set}$ is complete. So both sides of the claimed isomorphism exist.
>
> **Step 1 — left side.** By Lemma 1, $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$, naturally in $X$.
>
> **Step 2 — right side.** By Lemma 2, $\lim_J \mathcal{C}(X, D_-) \cong \mathrm{Cone}(X, D)$.
>
> **Step 3 — compose.** Combining, $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D) \cong \lim_J \mathcal{C}(X, D_-)$, and the composite is $h \mapsto (\pi_j \circ h)_j$. This is natural in $X$ by the naturality in Lemmas 1–2, and is exactly the canonical comparison map for $\mathcal{C}(X,-)$ applied to the limit; being an isomorphism, $\mathcal{C}(X, -)$ preserves the limit of $D$.
>
> **Step 4 — contravariant corollary.** Apply Steps 1–3 in $\mathcal{C}^{op}$, where $\operatorname{colim}_J D$ is the limit of $D^{op} : J^{op} \to \mathcal{C}^{op}$ and $\mathcal{C}(-, X) = \mathcal{C}^{op}(X, -)$ is a covariant hom-functor. This gives $\mathcal{C}(\operatorname{colim}_J D, X) \cong \lim_{J^{op}} \mathcal{C}(D_-, X)$.
>
> **Step 5 — Yoneda corollary.** $\mathbf{y}(c) = \mathcal{C}(-, c)$, and limits in $[\mathcal{C}^{op}, \mathbf{Set}]$ are computed pointwise. At each object $X$, $\mathbf{y}(\lim D)(X) = \mathcal{C}(X, \lim D) \cong \lim \mathcal{C}(X, D_j) = (\lim \mathbf{y}D)(X)$ by Steps 1–3, so $\mathbf{y}$ preserves limits. It reflects limits because a cone is a limit cone iff it induces a limit on every hom-set (a cone $\lambda$ over $D$ is a limit iff $\mathcal{C}(X,-)\lambda$ is a limit cone for all $X$, by the Yoneda lemma). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Why $\mathrm{Hom}(M, -)$ is left exact in module theory.** For a fixed module $M$, the functor $\mathrm{Hom}_R(M, -)$ preserves kernels (which are equalizers) and products, hence is left exact — this is the categorical content of [[Def - The Hom Functor and Left Exactness|the Hom functor's left exactness]]. The application is non-obvious because left-exactness is usually proved by diagram-chasing; recognising $\mathrm{Hom}_R(M, -)$ as the representable functor $\mathbf{Mod}_R(M, -)$ shows it preserves all limits, with left-exactness the finite-limit case. (Note: this is the module-specific Hom; the general categorical hom is [[Def - Hom-Functor and Representable Functor]].)

**Continuity of the points functor in algebraic geometry.** The functor "$R$-points", $X \mapsto X(R)$, evaluated on schemes-as-functors, is a representable-style evaluation and preserves limits; this is why $(X \times_Z Y)(R) = X(R) \times_{Z(R)} Y(R)$. The application is non-obvious because fibre products of schemes seem geometric, but their points are computed by a limit-preserving evaluation. See [[Ex - Fibre products of schemes are pullbacks]].

**Limits in a category detected by a separator.** If $\mathcal{C}$ has a *separating* object $X$ (so $\mathcal{C}(X, -)$ is faithful), then preservation plus near-reflection lets limits be detected on the single hom-set $\mathcal{C}(X, -)$. This is how one verifies limits in categories with a generator — e.g. $\mathbb{Z}$ separates $\mathbf{Ab}$, so abelian-group limits are governed by underlying sets. The application is non-obvious because it reduces an abstract limit check to one representable functor.

---

# Bridges

- **[[Thm - Right Adjoints Preserve Limits|Right adjoints preserve limits (RAPL)]]** — the grand generalisation, and this theorem is its prototype. A right adjoint $G$ satisfies $\mathcal{C}(c, Gd) \cong \mathcal{D}(Fc, d)$; since the right side is a hom-functor in $d$, $G$ preserves limits by the same compatible-family argument applied with a twist by the adjunction. The bridge: every right adjoint *is*, up to the adjunction isomorphism, a hom-functor, so RAPL is "hom preserves limits" transported along $F \dashv G$.

- **[[Thm - The Yoneda Lemma|The Yoneda lemma]] and the embedding** — the reason reflection holds. The Yoneda lemma says an object is determined by its functor of maps-in $\mathcal{C}(-, X)$; consequently a cone is a limit iff it becomes a limit after applying every $\mathcal{C}(X, -)$, which is exactly reflection of limits by $\mathbf{y}$. The bridge: representability detects limits because it detects *everything*, by Yoneda.

- **[[Thm - Limits in Set and in Functor Categories|Limits in Set]]** — the partner that makes the theorem computational. The right-hand side $\lim \mathcal{C}(X, D_j)$ is a limit *in $\mathbf{Set}$*, so it equals the set of compatible families. The bridge: this theorem says "hom turns a limit into a limit of sets", and the $\mathbf{Set}$ theorem says "that limit of sets is the compatible families" — together they give "a map into a limit is a compatible family of maps", the working definition used in every limit computation.

---

# Unlocked by This

> [!note]- Algebraic geometry background
> A **commutative ring** is a set with $+, \times$ and $xy=yx$; the **functor of points** encodes a geometric object as $X : \mathbf{CRing} \to \mathbf{Set}$, and an **affine scheme** is a representable one, $\mathrm{Spec}\,R = \mathbf{CRing}(R, -)$. The spectrum $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]] of $\mathbf{CRing}^{op}$.
>
> This theorem is *why* $\mathrm{Spec}$ converts ring colimits into scheme limits. The contravariant hom corollary, $\mathcal{C}(\operatorname{colim} D, X) \cong \lim \mathcal{C}(D_-, X)$, applied with $\mathcal{C} = \mathbf{CRing}$, says exactly that $\mathrm{Spec}$ (a contravariant representable embedding) sends a colimit of rings to a limit of schemes. The coproduct of rings being the [[Def - Tensor Product of Modules|tensor product]], this yields $\mathrm{Spec}(R_1 \otimes_S R_2) \cong \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2$ — the **fibre product of schemes** is a [[Def - Pullback and Pushout|pullback]], computed by tensoring. So the geometry of intersections, fibres, and **base change** is the contravariant face of this theorem. Developed on [[Ex - Fibre products of schemes are pullbacks]].

> [!tip] RAPL and the Adjoint Functor Theorem *(from Chapter IV)*
> Limit-preservation is the *first obstruction* checked when asking whether a functor has a left adjoint: a right adjoint must preserve limits, so a functor that fails to is provably not a right adjoint. The **Adjoint Functor Theorem** turns the converse into a near-equivalence (limit-preservation plus a solution-set condition gives a left adjoint). This theorem, generalised to RAPL, is the foundation of that program.
