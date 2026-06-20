---
type: exercise-index
subject: higher-categories
section: "3"
tags: [category-theory, higher-categories, foundations]
---

## §3 The Comparison Problem and the Homotopy Hypothesis — Exercises

This section's two theorems are the foundational sanity of higher category theory: the homotopy hypothesis (invertible higher categories are spaces) and the comparison theorem (all models of $(\infty,1)$-categories agree). The exercises drill the machinery behind both. The first establishes the geometric fact at the heart of the homotopy hypothesis in the simplicial model — that the singular complex fills *all* horns, automatically, because the topological horn retracts onto the solid simplex — and uses it to locate the homotopy hypothesis as the all-horns boundary of the inner-horn world. The second is the sharpest negative result of the chapter: strict $\infty$-groupoids *fail* the homotopy hypothesis (they cannot model $S^2$, because strict interchange kills the Whitehead product), which is the decisive evidence that weakness is forced. The third pins down the precise sense of "same homotopy theory" that the comparison theorem delivers: a Quillen equivalence preserves not just homotopy categories but the full derived mapping spaces, and the exercise exhibits why mere equivalence of homotopy categories is not enough.

- [[Ex - The singular complex is a Kan complex]] (⭐⭐) — adjoint the horn-filling problem to topology and solve by deformation retraction; outer-horn filling is invertibility, so $\mathrm{Sing}(T)$ is an $\infty$-groupoid ([[Thm - The Homotopy Hypothesis]], [[Def - Kan Complex and the Nerve]], [[Def - Simplicial Set]], [[Def - Topological Space]])
- [[Ex - Strict omega-groupoids do not model all spaces]] (⭐⭐⭐) — strict interchange kills the Whitehead product, but $[\iota,\iota]\ne0$ for $S^2$; the homotopy hypothesis fails strictly, so weakness is forced ([[Thm - The Homotopy Hypothesis]], [[Def - Higher Homotopy Group]], [[Def - Topological Space]])
- [[Ex - Quillen equivalence detects derived mapping spaces]] (⭐⭐) — a Quillen equivalence preserves the full mapping spaces, not just $\pi_0$; the criterion behind the comparison theorem, with a homotopy-category-equivalence counterexample ([[Thm - Comparison of Models for (∞,1)-Categories]], [[Def - Quillen Adjunction and Quillen Equivalence]], [[Def - Model Category]])
