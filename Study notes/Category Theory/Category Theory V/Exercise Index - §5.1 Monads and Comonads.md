---
type: exercise-index
subject: category-theory
section: "5.1"
tags: [category-theory, foundations]
---

## §5.1 Monads and Comonads — Exercises

This section drills the core skill of §5.1: recognizing a [[Def - Monad and Comonad|monad]] either by checking its axioms directly or — far more usefully — by spotting the [[Def - Adjunction|adjunction]] it is the shadow of, via [[Thm - Every Adjunction Gives a Monad]]. The two computational exercises (power set, free monoid) are the prototypes of "collect-and-flatten" monads, where the multiplication is union or concatenation and the unit is a singleton; the third addresses the subtler structural point that a single monad has many resolutions into adjunctions, with [[Def - Kleisli Category|Kleisli]] and [[Def - Algebra for a Monad|Eilenberg–Moore]] as the extremes. Master the reflex of reading "free $X$" as "adjunction, hence monad," and of identifying the multiplication as the whiskered counit.

- [[Ex - The power-set monad]] (⭐⭐) — verifying the monad axioms by hand and re-deriving them from the free-sup-lattice adjunction; union as the lattice join ([[Def - Monad and Comonad]], [[Def - Adjunction]], [[Thm - Every Adjunction Gives a Monad]])
- [[Ex - The free monoid monad]] (⭐⭐) — the list monad from the free–forgetful adjunction with monoids; concatenation as the whiskered counit, and a preview that its algebras are monoids ([[Def - Monad and Comonad]], [[Def - Free-Forgetful Adjunction]], [[Thm - Every Adjunction Gives a Monad]], [[Def - Monoid in a Monoidal Category]])
- [[Ex - Adjunctions inducing the same monad]] (⭐⭐⭐) — non-uniqueness of resolutions: two different adjunctions inducing one monad, with Kleisli initial and Eilenberg–Moore terminal ([[Def - Monad and Comonad]], [[Def - Algebra for a Monad]], [[Def - Kleisli Category]], [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]])
