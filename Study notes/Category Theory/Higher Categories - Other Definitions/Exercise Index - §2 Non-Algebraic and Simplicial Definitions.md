---
type: exercise-index
subject: higher-categories
section: "2"
tags: [category-theory, higher-categories, foundations]
---

## §2 Non-Algebraic and Simplicial Definitions — Exercises

The non-algebraic definitions treat composition as a *property* — the Segal condition, the inner-horn condition — and never name a composite. The exercises here drill the reflexes of that stance. The first is *reading a Segal condition as composition*: a spine map that is a bijection (or weak equivalence) lets you reconstruct composition from the fillers, and the bijective/strict case recovers exactly ordinary categories, the prototype the whole machinery generalises. The second is *understanding completeness*: a bare Segal space can record the wrong object data, and the canonical witness is two equivalent objects in different path-components — the diagnostic for "wrong homotopy theory" is non-invariance under the localisation that should identify them. The third is the *level-$2$ sanity check*: unwinding the iterated-Segal definition at $n=2$ must yield bicategories, with the associator forced by the gap between "equivalence" and "isomorphism" in the Segal map, and the pentagon derived from functoriality on $\Delta$ rather than checked by hand.

- [[Ex - The Segal condition recovers ordinary categories]] (⭐⭐) — bijective Segal maps reconstruct a category; the strict prototype of the Segal-space machinery ([[Def - Segal Category and Complete Segal Space]], [[Def - Kan Complex and the Nerve]], [[Def - Category]], [[Def - Simplicial Set]])
- [[Ex - A Segal space that fails completeness]] (⭐⭐) — build the walking isomorphism with under-recorded objects; completeness is the condition that the object-space is an equivalence-invariant ([[Def - Segal Category and Complete Segal Space]], [[Def - Simplicial Set]], [[Def - Category]])
- [[Ex - Tamsamani-Simpson 2-categories are bicategories]] (⭐⭐⭐) — level-$2$ check: equivalence-not-isomorphism in the Segal map forces the associator; the pentagon follows from functoriality on $\Delta$ ([[Def - Tamsamani-Simpson n-Category]], [[Def - Segal Category and Complete Segal Space]], [[Def - 2-Category and Bicategory]], [[Def - Category]])
