---
type: exercise-index
subject: model-categories
section: "1"
tags: [category-theory, homotopy-theory, foundations]
---

## §1 Closed Monoidal Categories and Modules — Exercises

This section installs the *algebraic* substrate of the chapter: a closed monoidal category is one whose tensor has an internal hom (a right adjoint), and a monoid in it is a "ring object" with modules of its own. The exercises drill the recurring reflex of the chapter — "closedness is the tensor-hom adjunction" — and the unwinding of abstract monoid/module definitions into concrete algebra. The first exercise calibrates the crucial distinction between closed monoidal (common, with $\otimes$) and cartesian closed (special, with $\times$); the second builds the internal hom of complexes and shows its low homology *is* the morphism theory; the third identifies monoids in chain complexes with differential graded algebras, exposing how compatibility axioms are forced by the chain-map condition. Together they prepare the reader to do homotopical algebra in $\mathbf{Mod}_R$ later in the chapter.

- [[Ex - Mod_R is closed monoidal but not cartesian closed]] (⭐) — distinguishes closed monoidal from cartesian closed via the tensor-hom adjunction and the contrast $\otimes_R \neq \oplus$ ([[Def - Closed Monoidal Category]], [[Def - Cartesian Closed Category]], [[Def - Tensor Product of Modules]], [[Def - Module]])
- [[Ex - The internal hom of chain complexes]] (⭐⭐) — constructs $[M, N]$ degreewise from the module adjunction, with Koszul signs, and identifies $Z_0$ as chain maps and $H_0$ as chain-homotopy classes ([[Def - Closed Monoidal Category]], [[Def - Chain Map and Chain Homotopy]], [[Def - Tensor Product of Modules]])
- [[Ex - Monoids in chain complexes are differential graded algebras]] (⭐⭐) — unwinds "monoid in a monoidal category" to a DGA, deriving the graded Leibniz rule from the chain-map condition on $\mu$ ([[Def - Monoid in a Monoidal Category]], [[Def - Module over a Monoidal Model Category]], [[Def - Closed Monoidal Category]], [[Def - Chain Map and Chain Homotopy]])
