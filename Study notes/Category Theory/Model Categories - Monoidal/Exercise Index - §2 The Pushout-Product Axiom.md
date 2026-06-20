---
type: exercise-index
subject: model-categories
section: "2"
tags: [category-theory, homotopy-theory, foundations]
---

## §2 The Pushout-Product Axiom — Exercises

This section is the technical heart of the chapter: the pushout-product axiom (Quillen's SM7) is the one condition that makes a tensor product respect homotopy, and the pullback-hom is its adjoint twin. The exercises drill the three skills every monoidal-model-category verification needs: computing a pushout-product on generators and recognizing it as a boundary-relative inclusion; reducing the "for all cofibrations" axiom to a finite check on generators via a closure argument; and transposing between the pushout-product (tensor) side and the pullback-hom (internal hom) side through the adjunction. The first exercise is the canonical $\mathbf{sSet}$ computation (prism boundaries); the second proves the reduction-to-generators lemma that makes the axiom checkable; the third establishes the lifting-adjunction at the core of the Quillen-bifunctor theorem. Mastering these three is mastering the chapter's machinery.

- [[Ex - The pushout-product of boundary inclusions of simplices]] (⭐⭐) — computes $\partial\Delta^m \mathbin{\square} \partial\Delta^n$ as the boundary inclusion of the prism, a monomorphism, verifying the axiom on $\mathbf{sSet}$ generators ([[Def - Monoidal Model Category]], [[Def - Pullback and Pushout]], [[Def - Simplicial Set]])
- [[Ex - Reducing the pushout-product axiom to generating cofibrations]] (⭐⭐) — proves the closure lemma (the pushout-product class is saturated) using colimit-preservation of $\otimes$, justifying "reduce to generators" ([[Def - Monoidal Model Category]], [[Def - Closed Monoidal Category]], [[Def - Pullback and Pushout]])
- [[Ex - Transposing the pushout-product to the pullback-hom]] (⭐⭐⭐) — establishes the bijection of lifting problems $i \mathbin{\square} j \perp p \iff i \perp \langle j, p\rangle$ and the equivalence of the two axiom forms ([[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor]], [[Def - Closed Monoidal Category]], [[Def - Pullback and Pushout]], [[Def - Monoidal Model Category]])
