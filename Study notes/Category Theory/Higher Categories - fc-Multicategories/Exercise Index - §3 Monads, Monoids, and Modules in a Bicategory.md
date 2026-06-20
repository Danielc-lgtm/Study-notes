---
type: exercise-index
subject: higher-categories
section: "3"
tags: [category-theory, higher-categories, foundations]
---

## §3 Monads, Monoids, and Modules in a Bicategory — Exercises

These exercises drill the unifying dictionary of §3: one definition — a [[Def - Monad Monoid and Module in a Bicategory|monad in a bicategory 𝒦]] — refracts into a small [[Def - Category|category]], a preorder, or an ordinary [[Def - Monad and Comonad|monad]] depending on which $\mathcal{K}$ you name. The first three exercises are the three signature identifications (in $\mathbf{Span}(\mathbf{Set})$, $\mathbf{Rel}$, and $\mathbf{Cat}$), and the recurring technique is "name the bicategory, then interpret $t, \mu, \eta$ via its concrete composition" — with the *texture* of the result (data versus property) read off from the texture of $\mathcal{K}$'s $2$-cells. The final exercise assembles monads and bimodules into the bicategory $\mathrm{Mod}(\mathcal{K})$ and shows Morita theory is exactly equivalence of objects there, illustrating the target-amplification of [[Thm - Monoids and Modules Form a Bicategory]].

- [[Ex - A monad in Span Set is a small category]] (⭐⭐) — interpreting monad data in $\mathbf{Span}(\mathbf{Set})$; the pullback as composable pairs makes $\mu$ composition and $\eta$ identities ([[Def - Monad Monoid and Module in a Bicategory]], [[Def - Category]], [[Def - Pullback and Pushout]])
- [[Ex - A monad in Rel is a preorder]] (⭐) — thin $2$-cells turn monad data into the property "reflexive and transitive"; monad structure as a property, not data ([[Def - Monad Monoid and Module in a Bicategory]], [[Def - 2-Category and Bicategory]])
- [[Ex - A monad in Cat recovers the ordinary monad]] (⭐) — the consistency check: whiskering is bicategorical horizontal composition, so the bicategorical axioms become the ordinary monad laws ([[Def - Monad Monoid and Module in a Bicategory]], [[Def - Monad and Comonad]], [[Def - Functor]], [[Def - Natural Transformation]])
- [[Ex - Bimodules over rings and the tensor as composition]] (⭐⭐⭐) — $\mathrm{Mod}(\mathcal{K})$ for the ring base; composition is $\otimes_S$, associativity from the balanced coequalizer, and Morita equivalence as equivalence of objects ([[Def - Monad Monoid and Module in a Bicategory]], [[Thm - Monoids and Modules Form a Bicategory]], [[Def - Ring]], [[Def - Tensor Product of Modules]])
