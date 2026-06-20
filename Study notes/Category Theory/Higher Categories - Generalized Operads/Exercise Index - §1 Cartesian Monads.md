---
type: exercise-index
subject: higher-categories
section: "1"
tags: [category-theory, higher-categories, foundations]
---

## §1 Cartesian Monads — Exercises

The exercises of this section drill the one gatekeeping condition of the whole chapter: whether a monad is **cartesian** — preserves pullbacks, with cartesian unit and multiplication. The technique split is sharp. The positive verifications (the list and identity monads) train you to read a naturality square as a fibre product and check the universal property by reconstructing apex elements from their images on the two legs; the *length/shape* data is what makes the reconstruction unique. The negative cases (the free-commutative-monoid and powerset monads) train the dual reflex: to refute a universal property, build *one* explicit witness — two distinct apex elements with the same image — and the productive place to find it is wherever a symmetry or a forgetful operation throws information away. Together they install the chapter's fastest diagnostic: cartesianness fails exactly when an order-forgetting (symmetric) quotient is present, which is why the framework delivers non-symmetric operads.

- [[Ex - The list monad is cartesian]] (⭐⭐) — verifying cartesianness by the shape-reconstruction technique: a list of structured things is a structure of equal-length lists, and the length data is the pullback ([[Def - Cartesian Monad]], [[Def - Monad and Comonad]], [[Def - Pullback and Pushout]])
- [[Ex - The free-commutative-monoid monad is not cartesian]] (⭐⭐⭐) — refuting a universal property by one explicit witness; the symmetric quotient forgets the partition of a repeated element ([[Def - Cartesian Monad]], [[Def - Monad and Comonad]], [[Def - Pullback and Pushout]])
- [[Ex - The identity and powerset monads]] (⭐) — the trivial base case (identity) and a one-line unit-square refutation (powerset); good algebras do not imply cartesianness ([[Def - Cartesian Monad]], [[Def - Monad and Comonad]], [[Def - Pullback and Pushout]])
