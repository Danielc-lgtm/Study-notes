---
type: exercise-index
subject: higher-categories
section: "7.1"
tags: [category-theory, higher-categories, foundations]
---

## §7.1 Opetopes and the Slice Construction — Exercises

These exercises drill the single generative engine of the chapter: the [[Def - The Slice of a Generalized Multicategory|slice construction]] and the way iterating it on the identity operad produces the [[Def - Opetope|opetopes]]. The aim is to make the recursion "an $n$-opetope is a pasting diagram of $(n-1)$-opetopes" concrete — by drawing the low cells as trees, by computing the slices directly, and by watching the construction degenerate when applied to an ordinary category. Together they install the two core reflexes: when you need cells one dimension up, slice; and when you need to manipulate a cell, draw its tree. Because this material is research-level, the exercises are conceptual — unwind the definition, draw the shapes, verify the slicing — rather than computational, but each has a full rigorous solution.

- [[Ex - Drawing the low-dimensional opetopes as trees]] (⭐) — instantiate the opetope recursion in dimensions $0$–$3$ and read off source/target faces from trees; surfaces that $\mathcal{O}_2$ is infinite ([[Def - Opetope]], [[Def - The Slice of a Generalized Multicategory]], [[Thm - Opetopes via Iterated Slicing of the Identity Operad]])
- [[Ex - The 2-opetopes are indexed by arity via the first slice]] (⭐⭐) — compute $\mathrm{ob}(I^{++})$ directly from the terminality of the identity operad, proving $\mathcal{O}_2 \cong \mathbb{N}$ ([[Def - The Slice of a Generalized Multicategory]], [[Def - Opetope]], [[Def - Initial and Terminal Object]], [[Thm - Opetopes via Iterated Slicing of the Identity Operad]])
- [[Ex - The slice of an ordinary category records factorisations]] (⭐⭐) — unwind the slice on an arity-one multicategory and distinguish it from the ordinary slice category ([[Def - The Slice of a Generalized Multicategory]], [[Def - Category]], [[Def - Functor]])
