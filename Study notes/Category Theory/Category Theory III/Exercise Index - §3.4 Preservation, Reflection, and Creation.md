---
type: exercise-index
subject: category-theory
section: "3.4"
tags: [category-theory, foundations]
---

## §3.4 Preservation, Reflection, and Creation — Exercises

These exercises drill how functors interact with limits and colimits — [[Def - Preservation, Reflection, and Creation of Limits|preservation, reflection, and creation]] — and the flagship consequences. The governing principle is the adjoint diagnosis: right adjoints preserve limits, left adjoints preserve colimits ([[Thm - Right Adjoints Preserve Limits|RAPL]]), so a functor's behaviour is predicted by its adjoint side before any computation. The exercises range from the forgetful functor's asymmetry (preserves limits, destroys colimits) through the algebraic-geometry payoff (fibre products of schemes are pullbacks, via $\mathrm{Spec}$ as a Yoneda embedding) to the pointwise computation of (co)limits in presheaf categories.

- [[Ex - The forgetful functor from groups preserves limits not colimits]] (⭐⭐) — $U : \mathbf{Grp} \to \mathbf{Set}$ preserves limits (it is a right adjoint) but not coproducts (the free product); the free-product counterexample ([[Def - Preservation, Reflection, and Creation of Limits]], [[Def - Product and Coproduct]], [[Def - Free Group and Free Product]], [[Thm - Right Adjoints Preserve Limits]])
- [[Ex - Fibre products of schemes are pullbacks]] (⭐⭐⭐) — $\mathrm{Spec}$ is the Yoneda embedding of $\mathbf{CRing}^{op}$, sending the tensor-product pushout of rings to the pullback of schemes; intersection, fibre, and base change unified ([[Def - Pullback and Pushout]], [[Thm - Representable Functors Preserve Limits]], [[Def - The Yoneda Embedding]], [[Def - Tensor Product of Modules]])
- [[Ex - Limits in presheaf categories are computed pointwise]] (⭐⭐) — (co)limits of presheaves are computed objectwise in $\mathbf{Set}$; every presheaf category is bicomplete ([[Thm - Limits in Set and in Functor Categories]], [[Def - Presheaf]], [[Def - Preservation, Reflection, and Creation of Limits]])
