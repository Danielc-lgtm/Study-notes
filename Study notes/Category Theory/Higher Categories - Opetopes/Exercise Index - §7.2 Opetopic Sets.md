---
type: exercise-index
subject: higher-categories
section: "7.2"
tags: [category-theory, higher-categories, foundations]
---

## §7.2 Opetopic Sets — Exercises

These exercises drill the structural side of the chapter: an [[Def - Opetopic Set|opetopic set]] is a presheaf on the category of opetopes, and *every* good property follows from that single identification by general presheaf theory. The aim is to internalise the move "forget that the shapes are opetopes; prove the general presheaf statement; re-specialise." The first exercise unwinds the abstract presheaf into elementary cell-and-restriction data (with the all-important contravariance); the second instantiates the [[Thm - The Yoneda Lemma|Yoneda lemma]] to identify cells with maps out of standard cells; the third inherits cocompleteness and computes a concrete gluing pushout pointwise. Across all three, the reflex being trained is to import ordinary category theory wholesale by recognising the presheaf structure. These are conceptual problems with complete rigorous solutions.

- [[Ex - An opetopic set is a presheaf, unwound]] (⭐) — translate "presheaf on $\mathbb{O}$" into cells, restrictions, and functoriality, getting the variance right ([[Def - Opetopic Set]], [[Def - Presheaf]], [[Def - Natural Transformation]], [[Thm - The Yoneda Lemma]])
- [[Ex - The representable opetope as the standard cell via Yoneda]] (⭐⭐) — apply Yoneda at $\mathbb{O}$ to identify $O$-cells with maps from $\mathbf{y}O$, deduce the standard cell and full faithfulness ([[Def - Opetopic Set]], [[Thm - The Yoneda Lemma]], [[Def - The Yoneda Embedding]], [[Thm - The Yoneda Embedding is Fully Faithful]], [[Def - Presheaf]])
- [[Ex - Colimits of opetopic sets are computed pointwise]] (⭐⭐) — inherit cocompleteness from the presheaf setting and glue standard cells via a pointwise pushout ([[Def - Opetopic Set]], [[Def - Limit and Colimit]], [[Def - Presheaf]], [[Def - Pullback and Pushout]], [[Thm - The Yoneda Lemma]])
