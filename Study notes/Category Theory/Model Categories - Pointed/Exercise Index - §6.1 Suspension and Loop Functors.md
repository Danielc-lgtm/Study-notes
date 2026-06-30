---
type: exercise-index
subject: model-categories
section: "6.1"
tags: [category-theory, homotopy-theory, foundations]
---

## §6.1 Suspension and Loop Functors — Exercises

This section drills the single most important reflex of the chapter: that suspension and loop are **derived** ([[Def - Homotopy|homotopy]]) (co)limits, not strict ones. The first exercise exposes why the strict construction is degenerate (it returns the zero object) and forces the homotopy version; the second computes the flagship example $\Sigma S^n = S^{n+1}$ and reads off the suspension isomorphism; the third identifies the suspension with the degree shift in chain complexes, where it is invertible and previews the stable/triangulated world. Across all three, the techniques are: recognize a strict (co)limit against the zero object, replace it by the cofibrant/fibrant homotopy version, and use the explicit cone/cylinder or mapping-cone model to compute.

- [[Ex - The strict suspension is the trivial functor]] (⭐) — the strict pushout of $* \leftarrow X \rightarrow *$ collapses to the zero object, forcing the homotopy pushout; computes the reduced suspension in spaces ([[Def - Pointed Model Category Suspension and Loop]], [[Def - Pullback and Pushout]], [[Def - Initial and Terminal Object]], [[Def - Cylinder Object, Path Object, and Homotopy]])
- [[Ex - Suspension of the sphere is the next sphere]] (⭐⭐) — sphere as double cone on its equator, suspension isomorphism via a contractible-cone cofiber sequence ([[Def - Pointed Model Category Suspension and Loop]], [[Def - Higher Homotopy Group]], [[Thm - The Suspension-Loop Adjunction]], [[Def - Pullback and Pushout]])
- [[Ex - The shift is suspension in chain complexes]] (⭐⭐) — $\Sigma X = X[1]$ via the mapping cone of $X \to 0$; the shift adjunction in $D(R)$ and invertibility of $\Sigma$ ([[Def - Pointed Model Category Suspension and Loop]], [[Thm - The Suspension-Loop Adjunction]], [[Def - Chain Map and Chain Homotopy]], [[Def - Pullback and Pushout]])
