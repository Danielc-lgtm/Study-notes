---
type: exercise-index
subject: category-theory
section: "5.4"
tags: [category-theory, foundations]
---

## §5.4 Monoidal and Symmetric Monoidal Categories — Exercises

This section drills the [[Def - Monoidal Category|monoidal]] vocabulary and the unifying punchline of the chapter: [[Def - Monoid in a Monoidal Category|monoid objects]] in different monoidal categories are rings, algebras, and monads. The first exercise unwinds the monoid-object axioms in $(\mathbf{Ab},\otimes)$, $(\mathbf{Vect}_k,\otimes)$, and the endofunctor category, recovering rings, $k$-algebras, and monads — closing the loop with §5.1 — via the workhorse "linear map out of a tensor = bilinear map." The second builds the distribution monad and its Kleisli category of stochastic maps, then adds the copy-discard structure that names a Markov category, the categorical foundation of probability. The third calibrates the strict hierarchy monoidal ⊃ braided ⊃ symmetric, showing $\mathbf{Vect}_k$ is symmetric while composition of endofunctors is not even braided, and explaining why the braiding is what makes commutativity expressible.

- [[Ex - Monoids in Vect are algebras and in Ab are rings]] (⭐⭐) — monoid objects as rings, $k$-algebras, and monads depending on the ambient monoidal category; the unit object selects the structure ([[Def - Monoid in a Monoidal Category]], [[Def - Monoidal Category]], [[Def - Ring]], [[Def - Tensor Product of Vector Spaces]])
- [[Ex - The distribution monad and Markov categories]] (⭐⭐⭐) — the probability monad, Kleisli arrows as stochastic maps with Chapman–Kolmogorov composition, copy/discard and the non-naturality of copy as the signature of randomness ([[Def - Monad and Comonad]], [[Def - Kleisli Category]], [[Def - Monoidal Category]])
- [[Ex - Braidings and symmetry]] (⭐⭐) — symmetry of $\mathbf{Vect}_k$, the absence of a braiding on endofunctors, and one-object symmetric monoidal categories as commutative monoids ([[Def - Monoidal Category]], [[Def - Monoid in a Monoidal Category]], [[Def - Tensor Product of Vector Spaces]])
