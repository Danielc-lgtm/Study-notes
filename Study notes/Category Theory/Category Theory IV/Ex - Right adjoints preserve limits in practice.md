---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Right Adjoints Preserve Limits"
  - "Def - Free-Forgetful Adjunction"
  - "Def - Product and Coproduct"
tags: [category-theory, foundations]
---

# Problem Statement

**(a)** Using [[Thm - Right Adjoints Preserve Limits|RAPL/LAPC]], explain why the forgetful functor $U : \mathbf{Grp}\to\mathbf{Set}$ preserves products (and all limits), but the free functor $F : \mathbf{Set}\to\mathbf{Grp}$ does **not** preserve products.

**(b)** Show that $F$ *does* preserve coproducts: $F(S\sqcup T)\cong FS * FT$, the [[Def - Free Group and Free Product|free product]]. Verify the failure of products explicitly with $S = T = \{*\}$.

**(c)** Give a "contrapositive" argument: deduce that a functor failing to preserve the terminal object cannot be a right adjoint, and use it to show $U : \mathbf{Grp}\to\mathbf{Set}$ cannot be a *left* adjoint (it has no right adjoint of the naive kind, sending products to coproducts).

**Recall:**

![[Thm - Right Adjoints Preserve Limits#Statement]]

A *product* is a [[Def - Limit and Colimit|limit]]; a *coproduct* a colimit. The [[Def - Free Group and Free Product|free product]] $G * H$ is the coproduct in $\mathbf{Grp}$. $F\dashv U$ is the [[Def - Free-Forgetful Adjunction|free-forgetful adjunction]] for groups.

---

# Convergent Strategy

**Problem class:** This is a "use RAPL/LAPC to predict and compute (co)limit behaviour" problem, and a "contrapositive non-existence" problem. It drills the single most error-prone fact in the chapter: which handedness preserves which (co)limit.

**Assumption pattern:** The only inputs are the handedness of each functor in $F\dashv U$ — $F$ left, $U$ right — and the theorem. From handedness alone the answers are forced: $U$ (right) preserves limits including products; $F$ (left) preserves colimits including coproducts but not products.

**Theorem routing:** [[Thm - Right Adjoints Preserve Limits|RAPL]] $\Rightarrow$ $U$ preserves products (a). LAPC $\Rightarrow$ $F$ preserves coproducts, i.e. $F(S\sqcup T) = FS * FT$ (b). The contrapositive of RAPL $\Rightarrow$ a non-limit-preserving functor is not a right adjoint (c).

**Key decision point:** The crux is resisting the intuition that "free" should distribute over everything. The free functor preserves coproducts (because it is a left adjoint) and destroys products. The explicit witness $F(\{*\}\times\{*\}) = F(\{*\}) = \mathbb{Z}$ versus $F\{*\}\times F\{*\} = \mathbb{Z}\times\mathbb{Z}$ makes the failure concrete: $\mathbb{Z}\not\cong\mathbb{Z}^2$.

---

# Legal Operations Used

1. **Operation 4 from the topic page (apply RAPL/LAPC to transport (co)limits).** Every part is an application of preservation by the appropriate adjoint.

2. **Operation 2 from the topic page (recognise the free-forgetful adjunction).** Identifying $F$ as left and $U$ as right adjoint is what supplies the handedness.

3. **The contrapositive of RAPL** (operation 4's negative form): non-preservation forbids being a right adjoint.

---

# Hints

> [!note]- Hint 1
> $U$ is a *right* adjoint (right adjoint to nothing-on-its-right? No — $U$ is the *right* adjoint in $F\dashv U$). Right adjoints preserve limits, and products are limits.

> [!note]- Hint 2
> $F$ is a *left* adjoint, so it preserves *colimits*. Coproducts are colimits, so $F(S\sqcup T)\cong FS\sqcup FT$ in $\mathbf{Grp}$, and the coproduct in $\mathbf{Grp}$ is the free product $*$.

> [!note]- Hint 3
> Test products with one-point sets: $\{*\}\times\{*\} = \{*\}$, so $F(\{*\}\times\{*\}) = F\{*\} = \mathbb{Z}$, whereas $F\{*\}\times F\{*\} = \mathbb{Z}\times\mathbb{Z}$. Since $\mathbb{Z}\not\cong\mathbb{Z}^2$, $F$ does not preserve this product.

---

# Solution

Everything follows from handedness: $U$ right adjoint preserves limits; $F$ left adjoint preserves colimits. The product/coproduct behaviour is then forced, and the contrapositive gives non-existence results.

**Step 1: $U$ preserves limits; $F$ does not preserve products (part a).**

> [!note]- Derivation
> In $F\dashv U$, the forgetful functor $U$ is the *right* adjoint. By [[Thm - Right Adjoints Preserve Limits|RAPL]], $U$ preserves all limits — in particular products, equalizers, kernels, and inverse limits. Concretely: the underlying set of a product of groups $\prod_i G_i$ is the product of the underlying sets $\prod_i UG_i$, the underlying set of a kernel is the set-theoretic kernel, etc. This is why algebraic limits are "computed on elements".
>
> The free functor $F$ is the *left* adjoint. RAPL says nothing forces a *left* adjoint to preserve limits, and in fact $F$ does not: a left adjoint preserves *colimits*, not limits. So $F$ has no obligation to preserve products, and (part b) it genuinely fails to.

**Step 2: $F$ preserves coproducts; explicit product failure (part b).**

> [!note]- Derivation
> By LAPC (the dual of RAPL), the left adjoint $F$ preserves colimits. The coproduct in $\mathbf{Set}$ is disjoint union $\sqcup$; the coproduct in $\mathbf{Grp}$ is the [[Def - Free Group and Free Product|free product]] $*$. So
> $$F(S\sqcup T)\;\cong\;FS * FT.$$
> Indeed the free group on a disjoint union of generating sets is the free product of the free groups — both have the universal property "a homomorphism is a pair of homomorphisms", which is the coproduct property.
>
> **Product failure.** Take $S = T = \{*\}$. In $\mathbf{Set}$, $\{*\}\times\{*\} = \{*\}$, so $F(\{*\}\times\{*\}) = F\{*\} = \mathbb{Z}$ (the free group on one generator). But the product in $\mathbf{Grp}$ is the direct product, so $F\{*\}\times F\{*\} = \mathbb{Z}\times\mathbb{Z} = \mathbb{Z}^2$. Since $\mathbb{Z}$ is not isomorphic to $\mathbb{Z}^2$ (different ranks: $\mathbb{Z}$ is cyclic, $\mathbb{Z}^2$ is not), $F(\{*\}\times\{*\})\not\cong F\{*\}\times F\{*\}$. So $F$ does not preserve products — exactly as RAPL's handedness predicts.

**Step 3: Contrapositive non-existence (part c).**

> [!note]- Derivation
> The terminal object is the empty product (a limit over the empty diagram). By [[Thm - Right Adjoints Preserve Limits|RAPL]], a right adjoint preserves the terminal object. **Contrapositive:** a functor that does *not* send the terminal object to a terminal object is *not* a right adjoint, hence has *no* left adjoint.
>
> Application: consider whether $U : \mathbf{Grp}\to\mathbf{Set}$ could be a *left* adjoint (i.e. have a right adjoint making $U$ the left member). If it were, $U$ would preserve colimits, in particular coproducts: $U(G * H)$ would equal $UG\sqcup UH$. But the underlying set of a free product $G * H$ is much larger than the disjoint union $UG\sqcup UH$ — it contains all reduced words alternating between $G$ and $H$, not just the elements of $G$ and $H$ separately. For instance $U(\mathbb{Z} * \mathbb{Z})$ is the underlying set of the free group on two generators (countably infinite, all reduced words), whereas $U\mathbb{Z}\sqcup U\mathbb{Z}$ is just two disjoint copies of $\mathbb{Z}$. They differ, so $U$ does *not* preserve coproducts, hence $U$ is *not* a left adjoint and has no right adjoint. (It is *only* a right adjoint, to $F$.)

> [!note]- Complete formal solution
> **(a)** In $F\dashv U$: $U$ is the right adjoint, so by RAPL it preserves all limits, including products (underlying set of a product of groups = product of underlying sets). $F$ is the left adjoint, so it preserves colimits, not limits, and need not preserve products.
>
> **(b)** By LAPC, $F$ preserves coproducts: $F(S\sqcup T)\cong FS * FT$ (free product = coproduct in $\mathbf{Grp}$). Product failure: $F(\{*\}\times\{*\}) = F\{*\} = \mathbb{Z}$ but $F\{*\}\times F\{*\} = \mathbb{Z}^2$, and $\mathbb{Z}\not\cong\mathbb{Z}^2$.
>
> **(c)** A right adjoint preserves the terminal object (empty product), so a functor not preserving it is not a right adjoint. $U : \mathbf{Grp}\to\mathbf{Set}$ does not preserve coproducts ($U(\mathbb{Z}*\mathbb{Z})\neq U\mathbb{Z}\sqcup U\mathbb{Z}$), so it is not a left adjoint; it has no right adjoint. $\blacksquare$

---

# Key Takeaways

**Handedness is destiny: right adjoints preserve limits, left adjoints preserve colimits, and nothing more is needed to predict (co)limit behaviour.** The entire exercise is a single principle applied repeatedly: once you know whether a functor is a left or right adjoint, you know exactly which (co)limits it preserves. The forgetful functor (right adjoint) preserves products; the free functor (left adjoint) preserves coproducts but destroys products. You never recompute this — identify the handedness and read off the answer. The mnemonic that prevents the universal error ("free preserves products"): a limit is a way of mapping *in*, so it lives on the right of the hom-set and is preserved by the *right* adjoint. Free is a *left* adjoint, so it preserves coproducts (the free group on a disjoint union is the free product), not products.

**The explicit witness $\mathbb{Z}$ vs $\mathbb{Z}^2$ is the canonical proof that left adjoints break products.** When you need to *demonstrate* (not just assert) that a left adjoint fails to preserve a limit, test it on the smallest nontrivial case. For the free group, $F(\{*\}\times\{*\}) = F\{*\} = \mathbb{Z}$ while $F\{*\}\times F\{*\} = \mathbb{Z}^2$, and these differ because freeness multiplies generators (the product of generating sets is a single point, giving one generator) rather than pairing structures. This concrete failure is worth memorizing: it is the standard counterexample in the subject, and the same shape recurs (the free module on $S\times T$ is not the tensor/product of free modules; the polynomial ring on a product is not the product of polynomial rings).

**The contrapositive of RAPL is the fastest non-existence test in category theory.** Because preserving limits is *necessary* for being a right adjoint, any failure of preservation immediately forbids an adjoint. To show a functor $G$ has no left adjoint, exhibit a single limit it does not preserve — often the terminal object, the simplest limit. To show $G$ has no right adjoint, exhibit a colimit it does not preserve. This turns hard existence questions into easy refutations: "this functor does not preserve the terminal object, therefore it is not a right adjoint, therefore it has no left adjoint" is a complete argument. It is how one knows the free field functor cannot exist, why the forgetful functor from groups is *only* a right adjoint, and the working tool behind countless "this adjoint does not exist" claims. The positive converse — when *does* a limit-preserving functor have an adjoint — is exactly what [[Thm - The Adjoint Functor Theorem|the Adjoint Functor Theorem]] answers, supplying the missing solution set condition.
