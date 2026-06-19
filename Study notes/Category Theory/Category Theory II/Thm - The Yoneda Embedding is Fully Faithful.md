---
type: theorem
subject: category-theory
prereqs:
  - "Def - The Yoneda Embedding"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
  - "Thm - The Yoneda Lemma"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a locally small category, $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$ the [[Def - The Yoneda Embedding|Yoneda embedding]] ($\mathbf{y}A = \mathcal{C}(-, A)$), and $\mathrm{Nat}(-, -)$ the set of [[Def - Natural Transformation|natural transformations]]. Objects $A, B$; morphism $f : A \to B$; $f_* = \mathcal{C}(-, f)$ its image under $\mathbf{y}$. A functor is **fully faithful** if it is bijective on each hom-set (see [[Def - Full, Faithful, and Essentially Surjective Functor]]). The full registry is on [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

---

# Statement

> **Theorem (The Yoneda Embedding is Fully Faithful).** Let $\mathcal{C}$ be a locally small category. The [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, $A \mapsto \mathcal{C}(-, A)$, is **fully faithful**: for all objects $A, B$, the function
> $$\mathbf{y} : \mathcal{C}(A, B) \longrightarrow \mathrm{Nat}\big(\mathcal{C}(-, A),\, \mathcal{C}(-, B)\big), \qquad f \mapsto f_* = \mathcal{C}(-, f),$$
> is a bijection. Equivalently, $\mathcal{C}(A, B) \cong \mathrm{Nat}(\mathbf{y}A, \mathbf{y}B)$ naturally.
>
> Consequently $\mathbf{y}$ is injective on objects up to isomorphism: $\mathbf{y}A \cong \mathbf{y}B$ in $[\mathcal{C}^{op}, \mathbf{Set}]$ if and only if $A \cong B$ in $\mathcal{C}$, and $\mathcal{C}$ is isomorphic to the full subcategory of $[\mathcal{C}^{op}, \mathbf{Set}]$ on the [[Def - Hom-Functor and Representable Functor|representable presheaves]]. The dual statement holds for the contravariant Yoneda embedding $\mathcal{C}^{op} \to [\mathcal{C}, \mathbf{Set}]$.

The slogan: **a category embeds into its presheaves, and objects are determined up to isomorphism by their representable functors.**

---

# Motivation

The chapter opened with a slogan borrowed from Grothendieck and Mazur: an object is best understood through the network of relations it enjoys with everything around it, and to understand $A$ it is often more useful to deal directly with the functor representing it. This theorem is that slogan promoted to a theorem with no slack. It says the passage from an object $A$ to its representable presheaf $\mathcal{C}(-, A)$ loses *nothing*: not the object (recoverable up to isomorphism) and not the morphisms (recovered exactly, on the nose). The functor of relationships is a complete invariant.

The practical force is enormous. It licenses the entire functor-of-points method: to define or study an object, define or study its representable functor instead. In algebraic geometry this is not a technique but the *definition* of the objects — **Spec** is the Yoneda embedding, the category of affine schemes is by definition its image, and "morphisms of schemes = ring maps backwards" is exactly full faithfulness. More mundanely, it gives a uniform way to prove two objects isomorphic (show their representable functors are isomorphic) and to compute morphisms (compute natural transformations of representables). And, applied to a one-object category, it is Cayley's theorem. The whole apparatus rests on this one corollary of the Yoneda lemma.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is merely "$\mathcal{C}$ is locally small". The interesting question is which problems are secretly asking you to use full faithfulness.

The first disguised source is **a problem about isomorphism of objects that is easier at the level of functors**. If you can build a natural isomorphism $\mathcal{C}(-, A) \cong \mathcal{C}(-, B)$ — typically out of natural bijections of hom-sets — full faithfulness hands you back an isomorphism $A \cong B$, and it is canonical. The non-obvious step is to *reformulate the object-level question as a functor-level one*. *Example problem:* prove $V \otimes W \cong W \otimes V$ by a natural isomorphism of the bilinear-map functors they represent (see [[Thm - Universal Property of the Tensor Product]]).

The second disguised source is **a problem about morphisms phrased via natural transformations**. Any natural family of operations on hom-sets $\mathcal{C}(-, A) \Rightarrow \mathcal{C}(-, B)$ must come from a single morphism $A \to B$. The non-obviousness is recognizing a construction as such a natural family. *Example problem:* show every "natural way to turn a map into $A$ into a map into $B$" is postcomposition by a fixed arrow — there are no exotic natural operations.

The third disguised source is **a one-object category**. When $\mathcal{C} = BG$ is a group (or monoid) viewed as a one-object category, full faithfulness becomes a faithful representation of $G$ on a set, i.e. Cayley's theorem. The non-obvious bridge is to *recognize an algebraic structure as a one-object category* so the embedding theorem applies. *Example problem:* derive Cayley's theorem, and its monoid analogue, as instances (see [[Ex - Yoneda generalizes Cayley's theorem]] and [[Ex - The Yoneda lemma for posets and monoids]]).

**Targets (Output Amplification)**

The bare conclusion is "$\mathbf{y}$ is fully faithful". Combined with other facts it produces the structural backbone of the subject.

Combine with **representability**. A functor $F$ is representable exactly when it is isomorphic to some $\mathbf{y}A$; full faithfulness then says the representing object $A$ is determined up to *unique* isomorphism, recovering [[Thm - Uniqueness of Universal Objects]] by a second route. The further result is that "$F$ is representable" determines $A$ canonically, which is what makes "*the* representing object" legitimate.

Combine with **essential surjectivity onto a subcategory**. $\mathbf{y}$ is fully faithful but not essentially surjective (most presheaves are not representable); restricting the codomain to the representable presheaves makes it an *equivalence* $\mathcal{C} \simeq \{\text{representables}\}$. The further result is $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$ in algebraic geometry — an equivalence of categories obtained by carving out the essential image. This is non-obvious because it converts a non-surjective embedding into an equivalence by a definitional restriction.

Combine with **a forgetful functor to $\mathbf{Set}$**. Composing the embedding of a one-object category with the forgetful functor $[\mathcal{C}^{op}, \mathbf{Set}] \to \mathbf{Set}$ realizes $\mathcal{C}(A, A)$ as an honest endomorphism monoid of a set; for a group this is the symmetric group, giving Cayley. The further result is a concrete permutation/transformation representation extracted from the abstract embedding.

---

# Why Is It True

This is not a new theorem; it is the [[Thm - The Yoneda Lemma|Yoneda lemma]] read with a particular codomain. The Yoneda lemma says, for any presheaf $F$,
$$\mathrm{Nat}(\mathcal{C}(-, A), F) \cong F(A).$$
Now choose $F = \mathcal{C}(-, B) = \mathbf{y}B$, which is itself a presheaf. Then $F(A) = \mathcal{C}(A, B)$, so the lemma reads
$$\mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B)) \cong \mathcal{C}(A, B).$$
That is precisely the claim that $\mathbf{y}$ induces a bijection on hom-sets. And tracking the Yoneda bijection through this special case shows the bijection is *exactly* the action of $\mathbf{y}$ on morphisms: the natural transformation corresponding to $f \in \mathcal{C}(A, B)$ is the one whose value on $1_A$ is $f$, which is postcomposition $f_*$.

> **Full faithfulness is the Yoneda lemma evaluated at a representable target: natural transformations between two representables are just morphisms between the representing objects, because each is pinned down by where it sends the identity.**

The "objects determined up to isomorphism" corollary follows because any fully faithful functor reflects isomorphisms: if $\mathbf{y}A \cong \mathbf{y}B$, the inverse natural isomorphisms come from morphisms $A \to B$ and $B \to A$ (fullness), and these compose to the identities because $\mathbf{y}$ is faithful and the composites map to identities. So $\mathbf{y}A \cong \mathbf{y}B$ forces $A \cong B$. The object is its functor of points.

---

# What Makes This Hard

There is almost no difficulty *given* the Yoneda lemma — the entire proof is "set $F = \mathbf{y}B$". The traps are conceptual. First, one must verify that the Yoneda bijection, in this special case, *coincides with the map $\mathbf{y}$ does on morphisms* — that the abstract bijection and the concrete functor agree — rather than merely that some bijection exists; otherwise one has proved a bijection of the right cardinality without identifying it with $\mathbf{y}$. Second, the distinction between **fully faithful** and **an equivalence** is routinely blurred: $\mathbf{y}$ is *not* an equivalence onto all presheaves (it is not essentially surjective — the covariant power-set presheaf and most others are not representable), only onto the representable ones. Third, "objects determined up to isomorphism" is a *reflection of isomorphisms* statement that needs both fullness and faithfulness; with only faithfulness one cannot recover the inverse morphism.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Specialize the Yoneda lemma to $F = \mathbf{y}B$ to get a bijection $\mathrm{Nat}(\mathbf{y}A, \mathbf{y}B) \cong \mathcal{C}(A, B)$, then check this bijection is inverse to $\mathbf{y}$ on morphisms. Deduce the object-level corollary from reflection of isomorphisms.

**Subgoal decomposition:**

1. **Specialize Yoneda.** Put $F = \mathcal{C}(-, B)$ in the [[Thm - The Yoneda Lemma|Yoneda lemma]] to obtain $\mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B)) \cong \mathcal{C}(A, B)$.
   - *Hint:* $F(A) = \mathcal{C}(A, B)$ when $F = \mathcal{C}(-, B)$.
   - *Why needed:* This is the bijection of hom-sets; the only remaining task is to identify it with $\mathbf{y}$.

2. **Identify the bijection with $\mathbf{y}$.** Show the natural transformation assigned to $f$ by the inverse Yoneda map is $f_* = \mathbf{y}f$.
   - *Hint:* The Yoneda inverse sends $f$ to the transformation $\Psi(f)$ with $\Psi(f)_X(g) = \mathcal{C}(-, B)(g)(f)$; unwind to get $\Psi(f)_X(g) = f \circ g = (f_*)_X(g)$.
   - *Why needed:* It proves the *functor* $\mathbf{y}$ — not merely some abstract map — is bijective on hom-sets.

3. **Reflect isomorphisms.** Show $\mathbf{y}A \cong \mathbf{y}B \Rightarrow A \cong B$.
   - *Hint:* A natural isomorphism $\mathbf{y}A \cong \mathbf{y}B$ and its inverse come, by fullness, from morphisms $f : A \to B$, $g : B \to A$; faithfulness forces $g \circ f = 1_A$ and $f \circ g = 1_B$ because their images are identities.
   - *Why needed:* It is the "objects determined by their functors" corollary that powers the functor-of-points method.

4. **Carve out the equivalence.** Restrict the codomain to the essential image (the representable presheaves) to upgrade the embedding to an equivalence onto that subcategory.
   - *Hint:* A fully faithful functor is an equivalence onto its essential image.
   - *Why needed:* It yields $\mathcal{C} \simeq \{\text{representables}\}$, hence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$ in the AG instance.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Yoneda bijection at a representable target
> **Statement:** For all $A, B$, the Yoneda lemma gives a bijection $\mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B)) \cong \mathcal{C}(A, B)$ by evaluation at $1_A$.
>
> **Hint:** Apply [[Thm - The Yoneda Lemma|the Yoneda lemma]] with the presheaf $F = \mathcal{C}(-, B)$, whose value at $A$ is $\mathcal{C}(A, B)$.
>
> **Why needed:** It is the bijection of hom-sets that fully faithfulness asserts.
>
> > [!note]- Full proof
> > The contravariant Yoneda lemma states that for any presheaf $F : \mathcal{C}^{op} \to \mathbf{Set}$ and any $A$, evaluation at $1_A$ is a bijection $\mathrm{Nat}(\mathcal{C}(-, A), F) \cong F(A)$. Take $F = \mathcal{C}(-, B)$, a presheaf. Then $F(A) = \mathcal{C}(A, B)$, and the bijection reads $\mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B)) \cong \mathcal{C}(A, B)$, with $\alpha \mapsto \alpha_A(1_A)$.

> [!note]- Lemma 2: The bijection is the action of $\mathbf{y}$ on morphisms
> **Statement:** The inverse of the bijection of Lemma 1 sends $f : A \to B$ to $f_* = \mathcal{C}(-, f) = \mathbf{y}f$. Hence $\mathbf{y} : \mathcal{C}(A, B) \to \mathrm{Nat}(\mathbf{y}A, \mathbf{y}B)$ is itself the bijection.
>
> **Hint:** Plug $F = \mathcal{C}(-, B)$ into the transport formula $\Psi(f)_X(g) = F(g)(f)$ and simplify $F(g)(f) = f \circ g$.
>
> **Why needed:** Without this, Lemma 1 only gives *a* bijection; this identifies it with the functor $\mathbf{y}$, which is what the theorem claims.
>
> > [!note]- Full proof
> > By the Yoneda lemma, the inverse $\Psi$ sends $f \in \mathcal{C}(A, B) = F(A)$ to the natural transformation $\Psi(f)$ with $\Psi(f)_X(g) = F(g)(f)$ for $g \in \mathcal{C}(X, A)$. Here $F = \mathcal{C}(-, B)$, so $F(g) = \mathcal{C}(g, B)$ is precomposition by $g$, and $F(g)(f) = f \circ g$. Thus $\Psi(f)_X(g) = f \circ g$, which is precisely the component at $X$ of postcomposition $f_* = \mathcal{C}(-, f) = \mathbf{y}f$. Therefore $\mathbf{y}$ on morphisms equals the inverse Yoneda bijection, and is itself bijective.

> [!note]- Lemma 3: A fully faithful functor reflects isomorphisms
> **Statement:** If $\mathbf{y}$ is fully faithful and $\mathbf{y}A \cong \mathbf{y}B$, then $A \cong B$ in $\mathcal{C}$.
>
> **Hint:** Pull the natural isomorphism and its inverse back to morphisms by fullness; use faithfulness to verify they compose to identities.
>
> **Why needed:** It is the "objects determined up to isomorphism" corollary, the foundation of the functor-of-points method.
>
> > [!note]- Full proof
> > Let $\varphi : \mathbf{y}A \to \mathbf{y}B$ be a natural isomorphism with inverse $\psi$. By fullness, $\varphi = \mathbf{y}f$ and $\psi = \mathbf{y}g$ for unique $f : A \to B$, $g : B \to A$. Then $\mathbf{y}(g \circ f) = \mathbf{y}g \circ \mathbf{y}f = \psi \circ \varphi = 1_{\mathbf{y}A} = \mathbf{y}(1_A)$. By faithfulness, $g \circ f = 1_A$. Symmetrically $f \circ g = 1_B$. So $f$ is an isomorphism $A \cong B$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — set-up.** Let $\mathcal{C}$ be locally small and $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, $\mathbf{y}A = \mathcal{C}(-, A)$, $\mathbf{y}f = f_* = \mathcal{C}(-, f)$.
>
> **Step 1 — bijection on hom-sets.** Fix $A, B$. By the contravariant [[Thm - The Yoneda Lemma|Yoneda lemma]] applied to the presheaf $F = \mathcal{C}(-, B)$, evaluation at $1_A$ is a bijection
> $$\mathrm{ev}_{1_A} : \mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B)) \xrightarrow{\cong} \mathcal{C}(A, B). \tag{Lemma 1}$$
>
> **Step 2 — the bijection is $\mathbf{y}$.** Its inverse $\Psi$ sends $f$ to the transformation with components $\Psi(f)_X(g) = \mathcal{C}(g, B)(f) = f \circ g$, which is exactly $(f_*)_X(g)$. Hence $\Psi(f) = \mathbf{y}f$, so the map $\mathbf{y} : \mathcal{C}(A, B) \to \mathrm{Nat}(\mathbf{y}A, \mathbf{y}B)$, $f \mapsto f_*$, is the inverse bijection $\Psi$. Therefore $\mathbf{y}$ is bijective on the hom-set $\mathcal{C}(A, B)$ — fully faithful. (Lemma 2.)
>
> **Step 3 — reflection of isomorphisms.** If $\mathbf{y}A \cong \mathbf{y}B$, write the iso and its inverse as $\mathbf{y}f$, $\mathbf{y}g$ by fullness; faithfulness gives $g \circ f = 1_A$, $f \circ g = 1_B$, so $A \cong B$. Conversely functoriality of $\mathbf{y}$ sends an iso $A \cong B$ to an iso $\mathbf{y}A \cong \mathbf{y}B$. (Lemma 3.)
>
> **Step 4 — full subcategory.** A fully faithful functor is an isomorphism onto the full subcategory on its image objects; thus $\mathbf{y}$ identifies $\mathcal{C}$ with the full subcategory of $[\mathcal{C}^{op}, \mathbf{Set}]$ spanned by the representable presheaves, and is an equivalence onto its essential image.
>
> **Dual.** Apply the covariant Yoneda lemma to obtain full faithfulness of the contravariant embedding $\mathcal{C}^{op} \to [\mathcal{C}, \mathbf{Set}]$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Cayley's theorem and its monoid version.** For $\mathcal{C} = BG$ a group as a one-object category, full faithfulness embeds $G$ into the endomorphisms of the underlying set of the regular representation — Cayley's theorem. For a monoid $M$, the same gives the regular representation of $M$ by transformations. The application is non-obvious because the abstract embedding theorem yields a concrete permutation/transformation representation. See [[Ex - Yoneda generalizes Cayley's theorem]] and [[Ex - The Yoneda lemma for posets and monoids]].

**AffSch ≃ CRing^op (algebraic geometry).** Apply to $\mathcal{C} = \mathbf{CRing}^{op}$: $\mathbf{y}$ is **Spec**, fully faithful, and its essential image is the category of affine schemes, giving the equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$ and the dictionary "scheme morphisms = ring maps backwards". The application is non-obvious because it is the *definition* of the basic objects of a major field. See [[Ex - A scheme is determined by its functor of points]].

**No exotic natural operations on a forgetful functor.** Full faithfulness, applied to representable forgetful functors, shows that the only natural operations $U \Rightarrow U$ on (say) $U : \mathbf{Grp} \to \mathbf{Set} \cong \mathbf{Grp}(\mathbb{Z}, -)$ are the power maps $g \mapsto g^n$, indexed by $\mathbb{Z}$. The application is non-obvious because one might expect more natural self-maps of the underlying-set functor than there are. See [[Ex - Computing a natural transformation set via Yoneda]].

---

# Bridges

- **[[Thm - The Yoneda Lemma|The Yoneda lemma]]** — the source. This theorem is the lemma specialized to a representable target $F = \mathbf{y}B$; the two are jointly called "Yoneda". The lemma computes natural transformations out of *any* representable into *any* functor; full faithfulness is the corner case where the target is also representable.

- **[[Def - Full, Faithful, and Essentially Surjective Functor|Fully faithful functors]]** — the property established. Fullness + faithfulness together give "reflects isomorphisms" and "isomorphism onto a full subcategory", which is exactly how $\mathbf{y}$ realizes $\mathcal{C}$ inside its presheaves.

- **[[Thm - Uniqueness of Universal Objects|Uniqueness of universal objects]]** — a parallel route. Reflection of isomorphisms gives a second proof that objects representing the same functor are uniquely isomorphic, complementing the category-of-elements argument.

- **[[Def - Equivalence of Categories|Equivalence of categories]]** — the upgrade. Restricting $\mathbf{y}$ to its essential image (the representables) turns the fully faithful embedding into an equivalence; this is the mechanism behind $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$.

---

# Unlocked by This

> [!tip] AffSch ≃ CRing^op and Spec *(from Algebraic Geometry)*
> Full faithfulness of the Yoneda embedding $\mathbf{y}$, which is **Spec** over $\mathbf{CRing}$, is the equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$: affine geometry *is* commutative algebra with arrows reversed. A **scheme** is glued from affine pieces; its functor of points determines it completely. See [[Ex - A scheme is determined by its functor of points]].

> [!tip] Cayley's Theorem and Representations *(from Algebra)*
> Specialized to a one-object category, full faithfulness is Cayley's theorem: every [[Def - Group|group]] is a subgroup of a symmetric group. The same idea, with linear targets, is the regular representation, the seed of representation theory.

> [!tip] Density and Free Cocompletion *(from this chapter and beyond)*
> Since $\mathbf{y}$ is a fully faithful embedding into the cocomplete category $[\mathcal{C}^{op}, \mathbf{Set}]$, and every presheaf is a colimit of representables, $[\mathcal{C}^{op}, \mathbf{Set}]$ is the **free cocompletion** of $\mathcal{C}$ — the universal home for freely adjoining colimits, foundational for presentable categories and Kan extensions.
