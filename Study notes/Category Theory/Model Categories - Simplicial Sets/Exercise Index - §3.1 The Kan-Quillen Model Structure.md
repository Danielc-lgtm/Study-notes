---
type: exercise-index
subject: model-categories
section: "3.1"
tags: [category-theory, homotopy-theory, foundations]
---

## §3.1 The Kan-Quillen Model Structure — Exercises

These exercises drill the lifting-and-factorisation calculus that underlies the Kan–Quillen [[Thm - Simplicial Sets Form a Model Category|model structure]] on $\mathbf{sSet}$. The recurring technique is to identify a class defined by a [[Def - Lifting Property and the Retract Argument|lifting property]] with an elementary class, and to propagate lifting properties from the generating sets $I = \{\partial\Delta^n \hookrightarrow \Delta^n\}$ and $J = \{\Lambda^n_k \hookrightarrow \Delta^n\}$ to their full saturations. Together they establish the three classes of the model structure: cofibrations are monomorphisms, trivial fibrations are the $I$-injectives, and fibrations are the [[Def - Kan Fibration and Anodyne Extension|Kan fibrations]]. Master the "reduce to generators, then propagate through pushout / transfinite composition / retract" pattern here and the rest of the chapter's lifting arguments become routine.

- [[Ex - Monomorphisms are the cofibrations]] (⭐⭐) — identifies cofibrations with monomorphisms by the skeletal cell-attachment construction; the two-inclusion saturation argument ([[Def - Kan Fibration and Anodyne Extension]], [[Def - Pullback and Pushout]], [[Thm - Simplicial Sets Form a Model Category]], [[Def - Cofibrant and Fibrant Objects]])
- [[Ex - Kan fibrations are closed under pullback]] (⭐) — closure of a right lifting class under pullback by a single diagram chase; deduces that fibres of Kan fibrations are Kan complexes ([[Def - Kan Fibration and Anodyne Extension]], [[Def - Pullback and Pushout]], [[Def - Kan Complex and the Nerve]], [[Def - Lifting Property and the Retract Argument]])
- [[Ex - Trivial fibrations lift against all monomorphisms]] (⭐⭐) — promotes lifting against the generators $I$ to lifting against the whole saturated class, and shows trivial fibrations are Kan fibrations ([[Def - Kan Fibration and Anodyne Extension]], [[Def - Lifting Property and the Retract Argument]], [[Ex - Monomorphisms are the cofibrations]], [[Thm - Simplicial Sets Form a Model Category]])
