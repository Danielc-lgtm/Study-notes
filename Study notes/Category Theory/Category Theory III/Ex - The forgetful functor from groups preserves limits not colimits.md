---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Preservation, Reflection, and Creation of Limits"
  - "Def - Product and Coproduct"
  - "Def - Free Group and Free Product"
tags: [category-theory, foundations]
---

# Problem Statement

Let $U : \mathbf{Grp} \to \mathbf{Set}$ be the forgetful functor. Show that $U$ [[Def - Preservation, Reflection, and Creation of Limits|preserves]] all limits — concretely, that $U(G \times H) = U(G) \times U(H)$ and $U(\mathrm{eq}(f,g)) = \mathrm{eq}(Uf, Ug)$ — but does **not** preserve colimits: the coproduct of groups is the [[Def - Free Group and Free Product|free product]], whose underlying set is *not* the disjoint union of the underlying sets. Explain the asymmetry via adjunctions: $U$ is a right adjoint (to the free-group functor), so it preserves limits but need not preserve colimits.

**Recall:**

![[Def - Preservation, Reflection, and Creation of Limits#The Definition]]

The **free product** $G * H$ is the coproduct in $\mathbf{Grp}$: reduced alternating words in $G$ and $H$. The **forgetful functor** $U : \mathbf{Grp} \to \mathbf{Set}$ sends a group to its underlying set and a homomorphism to its underlying function.

---

# Convergent Strategy

**Problem class:** This is a "test preservation of (co)limits by a functor" problem — checking whether $U$ commutes with limits and colimits, and diagnosing the asymmetry. The routine: verify preservation on products and equalizers (limits), exhibit a counterexample for coproducts (colimits), then explain via the adjoint structure.

**Assumption pattern:** The structural fact is that $U$ has a left adjoint (the free-group functor $F$), making $U$ a *right adjoint*. The unlocking principle is [[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]] (RAPL): $U$ preserves limits because it is a right adjoint; it need not preserve colimits because it is not a left adjoint. Recognising "$U$ is a right adjoint" predicts the entire answer before any computation.

**Theorem routing:** Preservation routes through the concrete fact that limits in $\mathbf{Grp}$ are [[Def - Preservation, Reflection, and Creation of Limits|created]] on underlying sets — the direct product's underlying set is the cartesian product, the equalizer's underlying set is the agreement-set — so $U$ preserves them. Failure routes through the [[Def - Free Group and Free Product|free product]] counterexample: $U(C_2 * C_2)$ is infinite while $U(C_2) \sqcup U(C_2)$ has $4$ elements, so $U(G \sqcup H) \ne U(G) \sqcup U(H)$.

**Key decision point:** The decisive insight is the adjoint diagnosis: rather than checking each colimit, observe that $U$ being a right adjoint *guarantees* limit-preservation and *predicts* possible colimit-failure, then confirm the failure with one example. The natural-but-wrong expectation "underlying set of a coproduct = disjoint union of underlying sets" is exactly what fails, and the free product is the witness.

---

# Legal Operations Used

1. **Compute limits on underlying sets (from the topic page: $U$ creates limits).** Verify $U(G \times H) = U(G) \times U(H)$ and $U(\mathrm{eq}) = \mathrm{eq}(U-)$ by noting limits in $\mathbf{Grp}$ are built on underlying sets.

2. **Exhibit a colimit counterexample (operation: compute the free product).** Show $U(C_2 * C_2)$ is infinite, hence $\ne U(C_2) \sqcup U(C_2)$.

3. **Diagnose via adjunction (operation: apply RAPL).** Use that $U$ is right adjoint to the free functor $F$ to explain why limits are preserved and colimits need not be.

---

# Hints

> [!note]- Hint 1
> Limits in $\mathbf{Grp}$ are computed on underlying sets: the direct product has underlying set the cartesian product, the equalizer has underlying set the agreement-set. So $U$ preserves them by inspection.

> [!note]- Hint 2
> For colimits, look at the coproduct. The coproduct in $\mathbf{Grp}$ is the [[Def - Free Group and Free Product|free product]] $G * H$, not the disjoint union. Compute its underlying set.

> [!note]- Hint 3
> $U(C_2 * C_2)$: the free product $C_2 * C_2 = \langle a, b \mid a^2 = b^2 = 1\rangle$ is the infinite dihedral group ($ab$ has infinite order). So $|U(C_2 * C_2)| = \infty \ne 4 = |U(C_2) \sqcup U(C_2)|$.

> [!note]- Hint 4
> Why the asymmetry? $U$ has a left adjoint $F$ (free group). [[Thm - Right Adjoints Preserve Limits|Right adjoints preserve limits]]; $U$ is a right adjoint, hence preserves limits but carries no guarantee for colimits.

---

# Solution

The plan: verify $U$ preserves products and equalizers by computing limits on underlying sets; exhibit the free-product counterexample showing $U$ fails to preserve coproducts; then explain both via $U$ being a right adjoint, so RAPL forces limit-preservation while leaving colimits unprotected.

**Step 1: $U$ preserves products and equalizers.**

> [!note]- Derivation
> The [[Def - Product and Coproduct|product]] in $\mathbf{Grp}$ is the direct product $G \times H$ with underlying set $U(G) \times U(H)$ (the cartesian product) and componentwise operation; $U$ applied to the projections gives the set-projections, so $U(G \times H) = U(G) \times U(H)$ as a product in $\mathbf{Set}$. The [[Def - Equalizer and Coequalizer|equalizer]] of $f, g : G \rightrightarrows H$ in $\mathbf{Grp}$ is the agreement-subgroup $\{x : f(x) = g(x)\}$, whose underlying set is the agreement-set $\mathrm{eq}(Uf, Ug)$ in $\mathbf{Set}$. So $U$ preserves equalizers. Since by [[Thm - Products and Equalizers Give All Limits|the reduction theorem]] all limits are built from products and equalizers, and $U$ preserves both, $U$ preserves all limits (indeed it [[Def - Preservation, Reflection, and Creation of Limits|creates]] them).

**Step 2: $U$ does not preserve coproducts.**

> [!note]- Derivation
> The [[Def - Product and Coproduct|coproduct]] in $\mathbf{Grp}$ is the [[Def - Free Group and Free Product|free product]] $G * H$. Take $G = H = C_2 = \langle a \mid a^2\rangle$. Then $C_2 * C_2 = \langle a, b \mid a^2 = b^2 = 1\rangle$, the infinite dihedral group: the element $ab$ has infinite order, since reduced words $abab\cdots$ never collapse. So $U(C_2 * C_2)$ is *infinite*. But $U(C_2) \sqcup U(C_2)$ — the disjoint union, which is the coproduct of the underlying sets in $\mathbf{Set}$ — has $2 + 2 = 4$ elements. Hence $U(C_2 * C_2) \ne U(C_2) \sqcup U(C_2)$, so $U$ does not preserve the coproduct, and therefore does not preserve colimits.

**Step 3: Adjoint diagnosis of the asymmetry.**

> [!note]- Derivation
> The forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$ has a left adjoint, the free-group functor $F : \mathbf{Set} \to \mathbf{Grp}$ (with $\mathbf{Grp}(FS, G) \cong \mathbf{Set}(S, UG)$). By [[Thm - Right Adjoints Preserve Limits|RAPL]], every right adjoint preserves limits — so $U$ preserves all limits, confirming Step 1 *without* case analysis. Dually, *left* adjoints preserve colimits; $U$ is a right adjoint, not a left one, so it carries no guarantee for colimits, and Step 2 shows the guarantee genuinely fails. The free functor $F$, being a left adjoint, *does* preserve colimits — for instance $F(S \sqcup T) = FS * FT$, the free product, which is the source of the asymmetry: the coproduct of free groups *is* free on the disjoint union, but $U$ runs the wrong way.

> [!note]- Complete formal solution
> **Preservation of limits.** In $\mathbf{Grp}$ the [[Def - Product and Coproduct|product]] $G \times H$ has underlying set $U(G)\times U(H)$ and the [[Def - Equalizer and Coequalizer|equalizer]] of $f,g$ has underlying set $\{x : f(x)=g(x)\} = \mathrm{eq}(Uf,Ug)$; $U$ sends projections/inclusions to their set-versions, so $U$ preserves products and equalizers, hence (by [[Thm - Products and Equalizers Give All Limits|the reduction theorem]]) all limits.
> **Failure for colimits.** The coproduct in $\mathbf{Grp}$ is the [[Def - Free Group and Free Product|free product]]; $C_2 * C_2 = \langle a,b \mid a^2=b^2=1\rangle$ is infinite (as $ab$ has infinite order), so $U(C_2 * C_2)$ is infinite while $U(C_2)\sqcup U(C_2)$ has $4$ elements. Thus $U$ does not preserve coproducts.
> **Diagnosis.** $U$ is right adjoint to the free-group functor $F$; by [[Thm - Right Adjoints Preserve Limits|RAPL]] right adjoints preserve limits (explaining the first part) and left adjoints preserve colimits (so $U$, not being left adjoint, has no colimit guarantee — explaining the second). $\blacksquare$

---

# Key Takeaways

**Right adjoints preserve limits; left adjoints preserve colimits — this single principle predicts the whole answer.** The reusable diagnostic is to identify a functor's adjoint side *before* checking preservation: $U : \mathbf{Grp} \to \mathbf{Set}$ is a right adjoint (to the free functor), so [[Thm - Right Adjoints Preserve Limits|RAPL]] guarantees it preserves all limits, and the absence of a *right* adjoint to $U$ leaves colimits unprotected. This converts "does $F$ preserve (co)limits?" from a case-by-case computation into a structural lookup: forgetful functors (right adjoints) preserve limits; free functors, tensoring, and other left adjoints preserve colimits. The trigger: whenever you must check (co)limit preservation, first ask "is this functor a left or right adjoint?"

**The free product is the canonical witness that forgetting destroys colimits.** The computation $C_2 * C_2 = D_\infty$ (infinite) versus $U(C_2) \sqcup U(C_2)$ (four elements) is the example to keep in working memory: it shows concretely that the underlying set of a colimit is generally *not* the colimit of the underlying sets, because building the free group on a disjoint union introduces vastly many new elements (all the reduced words). The transferable principle is that colimits in algebraic categories are "expensive" — they freely generate new elements subject only to forced relations — whereas limits are "cheap", computed directly on underlying sets. This asymmetry recurs everywhere: tensor products, pushouts, and amalgamated free products all enlarge the underlying set, while products, equalizers, and pullbacks do not.

**Creation is stronger than preservation, and $U$ creating limits is what makes $\mathbf{Grp}$ complete.** Beyond merely *preserving* limits, $U : \mathbf{Grp} \to \mathbf{Set}$ [[Def - Preservation, Reflection, and Creation of Limits|creates]] them: a limit of underlying sets lifts uniquely to a group, so $\mathbf{Grp}$ inherits completeness from $\mathbf{Set}$. The diagnostic to carry forward is that for algebraic categories (groups, rings, modules, algebras over an operad), the forgetful functor to $\mathbf{Set}$ creates limits, which is the engine of [[Ex - Set is complete and cocomplete|bootstrapping completeness]] from $\mathbf{Set}$. But creation of *colimits* fails for the same reason preservation does — the free product shows the colimit is not built on the underlying set — which is precisely why colimits in algebraic categories require the more elaborate construction (coproducts plus coequalizers, or the monad's algebra structure) developed in Chapter V.
