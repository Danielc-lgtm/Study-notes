---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Pullback and Pushout"
  - "Thm - Representable Functors Preserve Limits"
  - "Def - The Yoneda Embedding"
  - "Def - Tensor Product of Modules"
tags: [category-theory, foundations]
---

# Problem Statement

Show that the **fibre product of affine schemes** is a categorical [[Def - Pullback and Pushout|pullback]], computed by tensoring rings:
$$\mathrm{Spec}(R_1 \otimes_S R_2) \;\cong\; \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2.$$
Prove this from the categorical facts: the coproduct in $\mathbf{CRing}$ over $S$ is the [[Def - Tensor Product of Modules|tensor product]] $\otimes_S$ (a *pushout* of rings), and $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]], so by [[Thm - Representable Functors Preserve Limits|the contravariant representable theorem]] it sends pushouts of rings to pullbacks of schemes. Conclude that intersections of subvarieties, fibres of a morphism, and **base change** are all instances of one categorical construction.

**Recall:**

> [!note]- Algebraic geometry background
> A **commutative ring** $R$ is a set with $+, \times$ satisfying the usual axioms and $xy = yx$, with a unit $1$; ring homomorphisms preserve $+, \times, 1$. The **functor of points** approach models a geometric object as a functor $X : \mathbf{CRing} \to \mathbf{Set}$, where $X(R)$ is the "set of $R$-points". An **affine scheme** is a *representable* such functor: $\mathrm{Spec}\,R := \mathbf{CRing}(R, -)$, so its $A$-points are ring maps $R \to A$. For example the curve $y^2 = x^3 - 1$ is $\mathrm{Spec}\,\mathbb{Z}[x,y]/(y^2 - x^3 + 1)$, whose $A$-points are pairs $(a,b) \in A^2$ with $b^2 = a^3 - 1$. The assignment $R \mapsto \mathrm{Spec}\,R$ is the contravariant functor $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$; by Yoneda it is a fully faithful embedding (a contravariant equivalence onto affine schemes), $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$. The ring of functions on $\mathrm{Spec}\,R$ is $\mathcal{O}(\mathrm{Spec}\,R) \cong R$. A morphism of schemes over $S$ is "base change relative to the base $\mathrm{Spec}\,S$".

![[Def - Pullback and Pushout#The Definition]]

The [[Def - Tensor Product of Modules|tensor product]] $R_1 \otimes_S R_2$ of two $S$-algebras is the coproduct in the category of $S$-algebras, with structure maps $r \mapsto r \otimes 1$ and $r \mapsto 1 \otimes r$.

---

# Convergent Strategy

**Problem class:** This is a top-tier "transport a colimit to a limit through a contravariant equivalence" problem, the algebraic-geometry payoff of the chapter. The routine: identify the ring-side coproduct/pushout, recognise $\mathrm{Spec}$ as a (contravariant) Yoneda embedding, and apply the colimit-to-limit theorem.

**Assumption pattern:** Two structural facts are the assumptions. First, $\otimes_S$ is the coproduct of $S$-algebras — equivalently a *pushout* in $\mathbf{CRing}$ under $S$. Second, $\mathrm{Spec}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]] of $\mathbf{CRing}^{op}$, hence a contravariant representable functor. Recognising "tensor = pushout of rings" and "Spec = contravariant Yoneda" unlocks the entire argument.

**Theorem routing:** The route is: the pushout of $S \to R_1$, $S \to R_2$ in $\mathbf{CRing}$ is $R_1 \otimes_S R_2$; by [[Thm - Representable Functors Preserve Limits|the contravariant representable theorem]], $\mathrm{Spec}$ (a contravariant hom-functor) sends this colimit (pushout) of rings to a limit (pullback) of schemes; therefore $\mathrm{Spec}(R_1 \otimes_S R_2) = \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2$. The pointwise/functor-of-points check ([[Thm - Limits in Set and in Functor Categories]]) confirms it on $A$-points.

**Key decision point:** The crux is the *variance flip*: a pushout (colimit) of rings becomes a pullback (limit) of schemes, because $\mathrm{Spec}$ is *contravariant*. Getting the direction right — coproduct of rings $\leftrightarrow$ product of schemes, pushout of rings $\leftrightarrow$ pullback of schemes — is the whole content, and it is exactly the contravariant clause of [[Thm - Representable Functors Preserve Limits|"representable functors preserve limits"]].

---

# Legal Operations Used

1. **Identify the tensor product as a ring pushout (from the topic page: coproduct in $\mathbf{CRing}$ is $\otimes$).** $R_1 \otimes_S R_2$ is the pushout of $S \to R_1$, $S \to R_2$.

2. **Recognise $\mathrm{Spec}$ as the contravariant Yoneda embedding (operation: representable functor).** $\mathrm{Spec}\,R = \mathbf{CRing}(R,-)$, so $\mathrm{Spec}$ is a contravariant hom-functor and a fully faithful embedding.

3. **Apply the colimit-to-limit theorem (operation: [[Thm - Representable Functors Preserve Limits|contravariant representables send colimits to limits]]).** Transport the ring pushout to a scheme pullback.

4. **Verify on points (operation: [[Thm - Limits in Set and in Functor Categories|pointwise limits in functor categories]]).** Confirm $(X\times_Z Y)(A) = X(A) \times_{Z(A)} Y(A)$ as a pullback of sets.

---

# Hints

> [!note]- Hint 1
> The tensor product $R_1 \otimes_S R_2$ is the coproduct of $R_1, R_2$ in the category of $S$-algebras — equivalently the *pushout* of $S \to R_1$ and $S \to R_2$ in $\mathbf{CRing}$. A pushout is a colimit.

> [!note]- Hint 2
> $\mathrm{Spec}\,R = \mathbf{CRing}(R, -)$ is a representable functor, and $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]] — a *contravariant* hom-functor on $\mathbf{CRing}$.

> [!note]- Hint 3
> [[Thm - Representable Functors Preserve Limits|Contravariant representable functors send colimits to limits]]: $\mathcal{C}(\operatorname{colim} D, X) \cong \lim \mathcal{C}(D_-, X)$. With $\mathcal{C} = \mathbf{CRing}$ and the colimit the pushout $R_1 \otimes_S R_2$, this turns the pushout of rings into a pullback of schemes.

> [!note]- Hint 4
> Check on $A$-points: $\mathrm{Spec}(R_1\otimes_S R_2)(A) = \mathbf{CRing}(R_1\otimes_S R_2, A) \cong \mathbf{CRing}(R_1, A) \times_{\mathbf{CRing}(S,A)} \mathbf{CRing}(R_2, A)$, the pullback of sets — the universal property of $\otimes_S$. By [[Thm - Limits in Set and in Functor Categories|pointwise limits]] this *is* the pullback of schemes.

---

# Solution

The plan: identify $\otimes_S$ as the pushout of rings, recognise $\mathrm{Spec}$ as the contravariant Yoneda embedding, apply the contravariant representable theorem to flip the pushout into a pullback, and confirm on $A$-points via the tensor product's universal property and pointwise limits.

**Step 1: The tensor product is the pushout of rings under $S$.**

> [!note]- Derivation
> For $S$-algebras $R_1, R_2$ (rings with maps $S \to R_i$), the [[Def - Tensor Product of Modules|tensor product]] $R_1 \otimes_S R_2$ with $\iota_1 : r \mapsto r \otimes 1$, $\iota_2 : r \mapsto 1 \otimes r$ is the coproduct in the category of $S$-algebras: a pair of $S$-algebra maps $R_1 \to T$, $R_2 \to T$ glues into a unique $R_1 \otimes_S R_2 \to T$, $r_1 \otimes r_2 \mapsto$ (product of images), well-defined because $T$ is commutative and the two images agree on $S$. As a coproduct under $S$, this is exactly the **pushout** of $S \to R_1$, $S \to R_2$ in $\mathbf{CRing}$ — a colimit.

**Step 2: $\mathrm{Spec}$ is the contravariant Yoneda embedding.**

> [!note]- Derivation
> By definition $\mathrm{Spec}\,R = \mathbf{CRing}(R, -) : \mathbf{CRing} \to \mathbf{Set}$, the functor of points. As $R$ varies, $R \mapsto \mathbf{CRing}(R, -)$ is the [[Def - The Yoneda Embedding|Yoneda embedding]] of $\mathbf{CRing}^{op}$ into $[\mathbf{CRing}, \mathbf{Set}]$, hence fully faithful: $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$, a contravariant equivalence. So $\mathrm{Spec}$ is a contravariant representable functor on $\mathbf{CRing}$.

**Step 3: The pushout of rings becomes the pullback of schemes.**

> [!note]- Derivation
> By [[Thm - Representable Functors Preserve Limits|the contravariant representable theorem]], a contravariant hom-functor sends colimits to limits: $\mathbf{CRing}(\operatorname{colim} D, A) \cong \lim_{J^{op}} \mathbf{CRing}(D_-, A)$. Applying this to the pushout colimit $D = (R_1 \leftarrow S \rightarrow R_2)$ with colimit $R_1 \otimes_S R_2$, and reading the result as schemes (via the equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$, where a colimit of rings is a limit of schemes), gives that $\mathrm{Spec}(R_1 \otimes_S R_2)$ is the [[Def - Pullback and Pushout|pullback]] (fibre product) of $\mathrm{Spec}\,R_1 \to \mathrm{Spec}\,S \leftarrow \mathrm{Spec}\,R_2$:
> $$\mathrm{Spec}(R_1 \otimes_S R_2) \cong \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2.$$

**Step 4: Verification on $A$-points.**

> [!note]- Derivation
> For any ring $A$, the $A$-points are
> $$\mathrm{Spec}(R_1 \otimes_S R_2)(A) = \mathbf{CRing}(R_1 \otimes_S R_2, A) \cong \mathbf{CRing}(R_1, A) \times_{\mathbf{CRing}(S, A)} \mathbf{CRing}(R_2, A),$$
> by the universal property of $\otimes_S$ (a map out of the tensor product is a compatible pair of maps agreeing on $S$). The right side is a [[Def - Pullback and Pushout|pullback of sets]], namely $\mathrm{Spec}\,R_1(A) \times_{\mathrm{Spec}\,S(A)} \mathrm{Spec}\,R_2(A)$. Since limits in the functor category $[\mathbf{CRing}, \mathbf{Set}]$ are computed [[Thm - Limits in Set and in Functor Categories|pointwise]], this pointwise pullback *is* the pullback of schemes — confirming Step 3 explicitly on points.

**Step 5: Geometric consequences — intersection, fibre, base change.**

> [!note]- Derivation
> Three classical constructions are now one categorical pullback. *Intersection:* for closed subschemes $\mathrm{Spec}(S/I), \mathrm{Spec}(S/J) \hookrightarrow \mathrm{Spec}\,S$, their scheme-theoretic intersection is $\mathrm{Spec}(S/I \otimes_S S/J) = \mathrm{Spec}(S/(I+J))$, the pullback (cf. [[Ex - An intersection is a pullback and a limit]]). *Fibre:* the fibre of $\mathrm{Spec}\,R \to \mathrm{Spec}\,S$ over a point $\mathrm{Spec}\,\kappa \to \mathrm{Spec}\,S$ is $\mathrm{Spec}(R \otimes_S \kappa)$, the pullback against the point (cf. [[Ex - The kernel as a pullback]]). *Base change:* the functor $- \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,S'$ on $S$-schemes is the geometric face of $- \otimes_S S'$, taking a scheme over $S$ to its base-changed scheme over $S'$.

> [!note]- Complete formal solution
> The [[Def - Tensor Product of Modules|tensor product]] $R_1 \otimes_S R_2$ (with $\iota_1(r) = r\otimes 1$, $\iota_2(r) = 1\otimes r$) is the coproduct of $S$-algebras, i.e. the pushout of $S \to R_1$, $S \to R_2$ in $\mathbf{CRing}$ — a colimit. The functor $\mathrm{Spec}\,R = \mathbf{CRing}(R,-)$ is the [[Def - The Yoneda Embedding|Yoneda embedding]] of $\mathbf{CRing}^{op}$, a fully faithful contravariant representable functor with $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$. By [[Thm - Representable Functors Preserve Limits|the contravariant representable theorem]], $\mathrm{Spec}$ sends this pushout of rings to the pullback of schemes, so $\mathrm{Spec}(R_1 \otimes_S R_2) \cong \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2$. On $A$-points, $\mathbf{CRing}(R_1\otimes_S R_2, A) \cong \mathbf{CRing}(R_1,A)\times_{\mathbf{CRing}(S,A)}\mathbf{CRing}(R_2,A)$ (universal property of $\otimes_S$), a pullback of sets, which by [[Thm - Limits in Set and in Functor Categories|pointwise limits]] is the pullback of schemes — confirming the identification. Intersections ($S/(I+J)$), fibres ($R \otimes_S \kappa$), and base change ($- \otimes_S S'$) are all special cases. $\blacksquare$

---

# Key Takeaways

**Spec is a Yoneda embedding, and it flips colimits of rings into limits of schemes — the variance flip is the whole content.** The reusable principle is that $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]], a contravariant equivalence, so by [[Thm - Representable Functors Preserve Limits|"contravariant representables send colimits to limits"]] every colimit of rings becomes a limit of schemes: coproduct (tensor) of rings ↦ product of schemes, pushout of rings ↦ pullback of schemes. This is why the fibre product of schemes — the single most important construction in algebraic geometry — is *computed by tensoring rings*, and why the geometry runs opposite to the algebra. The trigger: whenever a geometric construction is "gluing/combining schemes", look for the dual ring colimit, and compute it there.

**Fibre product, intersection, fibre, and base change are one categorical pullback specialised four ways.** The decisive unification is that the scheme pullback $X \times_Z Y$ subsumes scheme-theoretic intersection ($S/I \otimes_S S/J = S/(I+J)$), the fibre of a morphism over a point ($R \otimes_S \kappa$), and base change ($- \otimes_S S'$) — exactly the way the set-level [[Def - Pullback and Pushout|pullback]] subsumes [[Ex - An intersection is a pullback and a limit|intersection]], [[Ex - The kernel as a pullback|kernel/fibre]], and preimage. Recognising all of these as the same construction means a theorem proved about pullbacks (stability under composition via the pasting lemma, base-change functoriality) applies to all four at once. The diagnostic: any "relative" or "fibred" construction in geometry is a pullback, hence governed by the universal property, hence computed by the corresponding ring tensor.

**The functor-of-points view makes scheme limits pointwise, so they exist and are computed ring-by-ring.** The deepest structural payoff is that schemes-as-functors live in a [[Thm - Limits in Set and in Functor Categories|functor category]], where limits are computed pointwise: $(X \times_Z Y)(A) = X(A) \times_{Z(A)} Y(A)$, a pullback of sets, for every test ring $A$. This is *why* fibre products of schemes exist and are well-behaved — they are pointwise pullbacks of $R$-points, inheriting completeness from $\mathbf{Set}$. The transferable insight is that the functor-of-points formalism converts hard existence questions in geometry into elementary pointwise computations in $\mathbf{Set}$, the same move that grounds the entire subject on $\mathbf{Set}$ via [[Thm - Representable Functors Preserve Limits|representability]]; this is the categorical engine behind moduli problems, descent, and the modern definition of a scheme.
