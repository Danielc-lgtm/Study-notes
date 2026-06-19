---
type: exercise-index
subject: category-theory
section: "4.4"
tags: [category-theory, foundations]
---

## §4.4 Adjoints, Limits, and the Adjoint Functor Theorem — Exercises

These exercises tie adjunctions to (co)limits and to existence. The recurring technique is to read off (co)limit-preservation from a functor's handedness — right adjoints preserve limits, left adjoints preserve colimits — and to use the contrapositive as a non-existence test. The cartesian-closed exercises drill the currying adjunction $(-\times B)\dashv(-)^B$, whose exponential laws are RAPL in disguise, and culminate in the Curry-Howard-Lambek correspondence, the chapter's deepest bridge to logic and type theory. The Adjoint Functor Theorem itself supplies the converse to RAPL: limit-preservation plus a solution set condition guarantees an adjoint exists.

- [[Ex - Right adjoints preserve limits in practice]] (⭐⭐) — use RAPL/LAPC to show $\mathbf{Grp}\to\mathbf{Set}$ preserves products while the free functor does not, with the $\mathbb{Z}$-vs-$\mathbb{Z}^2$ witness and the contrapositive non-existence test ([[Thm - Right Adjoints Preserve Limits]], [[Def - Free-Forgetful Adjunction]], [[Def - Product and Coproduct]], [[Def - Free Group and Free Product]])
- [[Ex - The exponential and currying in a cartesian closed category]] (⭐⭐) — verify $\mathbf{Set}(A\times B, C)\cong\mathbf{Set}(A, C^B)$, identify evaluation as the counit, and derive the exponential laws from iteration and RAPL ([[Def - Cartesian Closed Category]], [[Def - Adjunction]], [[Def - Product and Coproduct]], [[Thm - Right Adjoints Preserve Limits]])
- [[Ex - Curry-Howard-Lambek correspondence]] (⭐⭐⭐) — match CCCs, the simply typed lambda calculus, and intuitionistic logic; currying is the deduction theorem and $\lambda$-abstraction, and the free CCC is the calculus ([[Def - Cartesian Closed Category]], [[Def - Adjunction]], [[Def - Initial and Terminal Object]])
