---
type: exercise-index
subject: category-theory
section: "4.1"
tags: [category-theory, foundations]
---

## §4.1 Adjunctions via the Hom-Set Isomorphism — Exercises

These exercises drill the defining move of the chapter: exhibiting an adjunction as a natural isomorphism of hom-sets $\mathcal{D}(FA, B)\cong\mathcal{C}(A, GB)$, and recognising familiar constructions — free objects and the tensor product — as one half of such an isomorphism. The recurring technique is to read a universal property as a bijection of hom-sets, then verify naturality (usually by checking on generators, where homomorphisms are determined). Together they install the slogan "maps out of $F$ equal maps into $G$" and the handedness convention (left adjoint on the source, right adjoint on the target) that the rest of the chapter depends on.

- [[Ex - The free-forgetful adjunction for groups]] (⭐⭐) — read the free-group universal property as the hom-set bijection and verify naturality on generators ([[Def - Adjunction]], [[Def - Free-Forgetful Adjunction]], [[Def - Free Group and Free Product]], [[Def - Group]])
- [[Ex - The tensor-hom adjunction]] (⭐⭐) — establish $\mathrm{Hom}(A\otimes M, B)\cong\mathrm{Hom}(A,\mathrm{Hom}(M,B))$ via the universal property of $\otimes$ and currying, then read exactness off the handedness ([[Def - Adjunction]], [[Def - Tensor Product of Modules]], [[Def - The Hom Functor and Left Exactness]], [[Thm - Universal Property of the Tensor Product of Modules]], [[Thm - Right Adjoints Preserve Limits]])
- [[Ex - The free vector space adjunction]] (⭐) — show $S\mapsto k^{(S)}$ is left adjoint to the underlying-set functor, with the basis as unit ([[Def - Adjunction]], [[Def - Free-Forgetful Adjunction]], [[Def - Vector Space]])
