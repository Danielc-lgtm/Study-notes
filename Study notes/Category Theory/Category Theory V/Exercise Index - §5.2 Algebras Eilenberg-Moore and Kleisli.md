---
type: exercise-index
subject: category-theory
section: "5.2"
tags: [category-theory, foundations]
---

## §5.2 Algebras Eilenberg-Moore and Kleisli — Exercises

This section drills the two ways a [[Def - Monad and Comonad|monad]] resolves back into structure: its [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] (the full category of structured objects the monad describes) and its [[Def - Kleisli Category|Kleisli category]] (the free algebras, equivalently the category of "$T$-effectful maps"). The recurring technique for the algebra exercises is to read the structure map $a : TA\to A$ as "evaluate the formal expression" and let the two algebra laws reproduce the defining axioms of a known structure — groups, vector spaces. The Kleisli exercise drills the dual reflex: recognizing relations, partial functions, and stochastic maps as Kleisli arrows whose composition is forced by the monad multiplication. Together they establish that the *name* of a free-construction monad announces its category of algebras.

- [[Ex - Algebras for the free-group monad are groups]] (⭐⭐⭐) — extracting a [[Def - Group|group]] structure from an algebra structure map; how the free group's reduction relation produces the inverse axiom ([[Def - Algebra for a Monad]], [[Def - Monad and Comonad]], [[Def - Group]], [[Def - Free Group and Free Product]])
- [[Ex - The Kleisli category of the powerset monad is Rel]] (⭐⭐) — identifying $\mathbf{Set}_P\cong\mathbf{Rel}$; Kleisli composition as relational composition via the union multiplication ([[Def - Kleisli Category]], [[Def - Monad and Comonad]])
- [[Ex - Algebras for the free-vector-space monad]] (⭐⭐) — algebras for $X\mapsto k[X]$ are vector spaces; the structure map is the linear-combination evaluation and inherits the axioms from formal arithmetic ([[Def - Algebra for a Monad]], [[Def - Monad and Comonad]], [[Def - Vector Space]], [[Def - Free Module]])
