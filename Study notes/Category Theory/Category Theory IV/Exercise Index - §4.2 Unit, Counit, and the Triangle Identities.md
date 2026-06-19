---
type: exercise-index
subject: category-theory
section: "4.2"
tags: [category-theory, foundations]
---

## §4.2 Unit, Counit, and the Triangle Identities — Exercises

These exercises develop the $2$-categorical face of an adjunction: the unit $\eta : 1\Rightarrow GF$ (insertion of generators), the counit $\varepsilon : FG\Rightarrow 1$ (evaluation), and the triangle identities that make them an adjunction. The recurring technique is to compute the unit and counit as transposes of identity morphisms, then verify the triangle identities by re-expressing whiskered composites as single transposes and invoking bijectivity. The Galois-connection exercise shows the whole apparatus degenerating to order inequalities in the poset case, where naturality and the triangle identities become automatic — a clarifying limiting case. This is the data that carries forward into monad theory (Chapter V).

- [[Ex - Unit and counit of the free-forgetful adjunction]] (⭐⭐) — compute $\eta_S$ (insertion of generators) and $\varepsilon_H$ (multiply a word out), and read the counit's surjectivity as "every group is a quotient of a free group" ([[Def - Unit and Counit of an Adjunction]], [[Def - Free-Forgetful Adjunction]], [[Def - Free Group and Free Product]], [[Thm - First Isomorphism Theorem]])
- [[Ex - Verifying the triangle identities]] (⭐⭐) — prove $(\varepsilon F)(F\eta) = 1_F$ and $(G\varepsilon)(\eta G) = 1_G$ from the hom-set definition, and check them concretely on the free group ([[Def - Unit and Counit of an Adjunction]], [[Thm - Equivalence of the Definitions of Adjunction]], [[Def - Free-Forgetful Adjunction]])
- [[Ex - An adjunction from a Galois connection]] (⭐⭐) — identify a monotone Galois connection with an adjunction between posets; the unit/counit are the order inequalities and $gf$ is a closure operator ([[Def - Adjunction]], [[Def - Unit and Counit of an Adjunction]], [[Def - Category]])
