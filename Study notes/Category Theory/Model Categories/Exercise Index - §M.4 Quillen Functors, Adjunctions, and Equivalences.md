---
type: exercise-index
subject: model-categories
section: "M.4"
tags: [category-theory, homotopy-theory, foundations]
---

## §M.4 Quillen Functors, Adjunctions, and Equivalences — Exercises

These exercises drill the morphisms of model categories and their derived functors. The first proves the flagship Quillen equivalence $\mathbf{Top} \simeq \mathbf{sSet}$, the prototype for comparing two presentations of a homotopy theory and a form of the homotopy hypothesis. The second computes the total left derived functor of the tensor product and identifies it with the classical $\mathrm{Tor}$, showing derived functors of homological algebra are derived adjoints. The third proves the adjoint lifting lemma and uses it to establish the symmetry of the Quillen-adjunction definition and the reduction of cofibration-preservation to the generators. The thread is that Quillen adjunctions descend to derived adjunctions, manufacturing $\mathrm{Tor}$, $\mathrm{Ext}$, homotopy (co)limits, and the comparison of models all at once.

- [[Ex - Geometric realization and singular nerve form a Quillen equivalence]] (⭐⭐⭐) — verifying $|{-}| \dashv \mathrm{Sing}$ is a Quillen adjunction and equivalence, giving $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$ ([[Def - Quillen Adjunction and Quillen Equivalence]], [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]], [[Def - Simplicial Set]], [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]])
- [[Ex - The derived tensor product computes Tor]] (⭐⭐⭐) — showing $-\otimes_R N$ is left Quillen and its total left derived functor has homology $\mathrm{Tor}^R_*$, with independence of resolution as homotopy-invariance ([[Def - Quillen Adjunction and Quillen Equivalence]], [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]], [[Def - Tensor Product of Modules]], [[Def - Chain Map and Chain Homotopy]])
- [[Ex - A left Quillen functor preserves cofibrations]] (⭐⭐) — the adjoint lifting lemma, the equivalence of the two Quillen conditions, and preservation from generators via cofibrant generation ([[Def - Quillen Adjunction and Quillen Equivalence]], [[Def - Lifting Property and the Retract Argument]], [[Def - Adjunction]], [[Thm - Closure Properties of the Model Structure]])
