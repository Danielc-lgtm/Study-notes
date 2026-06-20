---
type: exercise-index
subject: model-categories
section: "2"
tags: [category-theory, homotopy-theory, foundations]
---

## §2 Framings — Exercises

This section turns the Reedy machinery into the device that makes every model category behave, up to homotopy, like a simplicial one: the [[Def - Cosimplicial and Simplicial Frame|frame]]. A cosimplicial frame on $X$ is a Reedy-cofibrant cosimplicial object interpolating $X$ with all its iterated cylinders — a homotopically correct "$X\otimes\Delta^{\bullet}$." The exercises drill the discipline of *certifying* a frame, which always means checking two conditions together: Reedy cofibrancy (the latching maps are cofibrations) and homotopical constancy (the structure maps are weak equivalences). The first exercise shows the naive candidate — the constant object — fails the cofibrancy condition, the canonical instructive non-example; the second shows that in a simplicial model category the genuine tensoring $X\otimes\Delta^{\bullet}$ *is* a frame, so framings extend rather than replace strict enrichment; the third extracts from any frame the degree-$1$ [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]], anchoring the abstract construction to elementary homotopy. Mastering "what makes something a frame" here is what makes the function complexes of §3 computable.

- [[Ex - The constant cosimplicial object is rarely a frame]] (⭐⭐) — the degree-$1$ latching map is the fold map; Reedy cofibrancy fails for the constant object ([[Def - Cosimplicial and Simplicial Frame]], [[Def - Reedy Category and the Reedy Model Structure]], [[Def - Cylinder Object, Path Object, and Homotopy]])
- [[Ex - In a simplicial model category the tensor with simplices is a frame]] (⭐⭐) — SM7 makes $X\otimes\Delta^{\bullet}$ Reedy cofibrant; framings recover the strict mapping object ([[Def - Cosimplicial and Simplicial Frame]], [[Def - Simplicial Set]], [[Def - Reedy Category and the Reedy Model Structure]])
- [[Ex - Level one of a frame is a cylinder object]] (⭐) — extracting the cylinder $X^1$ from a frame's degree-$1$ data, recovering left homotopy ([[Def - Cosimplicial and Simplicial Frame]], [[Def - Cylinder Object, Path Object, and Homotopy]], [[Def - Reedy Category and the Reedy Model Structure]])
