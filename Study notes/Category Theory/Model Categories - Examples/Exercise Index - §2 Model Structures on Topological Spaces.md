---
type: exercise-index
subject: model-categories
section: "2"
tags: [category-theory, homotopy-theory, foundations]
---

## §2 Topological Spaces — Exercises

These exercises build the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure]] on $\mathbf{Top}$ from the ground up and probe its boundaries. The first establishes that fibrancy is free (every space is fibrant), so all the difficulty lives in cofibrancy. The second identifies the fibrations with Serre fibrations by translating lifting-against-cylinders into the homotopy lifting property, using the exponential adjunction. The third classifies the two generating sets — the cell inclusion $S^{n-1}\hookrightarrow D^n$ generating cofibrations, the cylinder inclusion generating trivial cofibrations — and the fourth exhibits the classic pathology that forces the homotopy category to be built from cofibrant objects: a weak equivalence that is not a homotopy equivalence. The unifying skill is recognising when a topological condition (surjection, deformation retract, contractibility) is the geometric face of a model-category property (fibration, trivial cofibration, weak equivalence).

- [[Ex - Every space is fibrant in the Quillen model structure]] (⭐) — the map to a point lifts every homotopy trivially, so fibrancy is automatic ([[Def - The Quillen Model Structure on Topological Spaces]], [[Def - Cofibrant and Fibrant Objects]], [[Def - Topological Space]])
- [[Ex - Serre fibrations via the homotopy lifting property]] (⭐⭐) — RLP against cylinder bottom-inclusions equals the homotopy lifting property, via the exponential adjunction $-\times I \dashv (-)^I$ ([[Def - The Quillen Model Structure on Topological Spaces]], [[Def - Topological Space]], [[Def - Model Category]])
- [[Ex - The inclusion of a sphere into a disk is a cofibration]] (⭐⭐) — classifying the two generators: $S^{n-1}\hookrightarrow D^n$ a non-trivial cofibration, the cylinder inclusion a trivial cofibration ([[Def - The Quillen Model Structure on Topological Spaces]], [[Def - Higher Homotopy Group]], [[Def - Cofibrant and Fibrant Objects]])
- [[Ex - Weak homotopy equivalence need not be a homotopy equivalence]] (⭐⭐⭐) — the Warsaw circle is weakly contractible but not contractible; the CW hypothesis of Whitehead's theorem is cofibrancy, and cofibrant replacement washes out the pathology ([[Def - The Quillen Model Structure on Topological Spaces]], [[Def - Higher Homotopy Group]], [[Def - Homotopy Equivalence and Contractible Space]], [[Def - Cofibrant and Fibrant Objects]])
