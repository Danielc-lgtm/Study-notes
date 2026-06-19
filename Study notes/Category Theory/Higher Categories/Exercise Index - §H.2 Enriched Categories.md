---
type: exercise-index
subject: higher-categories
section: "H.2"
tags: [category-theory, homotopy-theory, foundations]
---

## §H.2 Enriched Categories — Exercises

These exercises drill the single reflex of enriched category theory: substitute a base [[Def - Monoidal Category|monoidal category]] $\mathcal{V}$ into the enriched-category definition and read off what structure results. Each exercise picks a different $\mathcal{V}$ and unwinds the axioms in it. The $\mathbf{Ab}$ case produces preadditive categories, with bilinearity forced by the tensor product; the $\mathbf{Vect}_k$ case produces $k$-linear categories and (one object) $k$-algebras; the Lawvere case produces metric spaces, with the triangle inequality *as* composition — the most surprising instance of the enrichment idea. The common technique is "morphism out of a tensor = bilinear map" for the algebraic bases, and "morphism in a poset = inequality" for the metric base. Together they show one definition unifies algebra, linear algebra, and metric geometry.

- [[Ex - An Ab-enriched category is a preadditive category]] (⭐⭐) — unwinding $\mathbf{Ab}$-enrichment, bilinear composition from the tensor's universal property ([[Def - Enriched Category]], [[Def - Monoidal Category]], [[Def - Abelian Group]])
- [[Ex - A metric space is a Lawvere-enriched category]] (⭐⭐⭐) — enriching over $([0,\infty],\geq,+,0)$, composition as the triangle inequality, identities as $d(a,a)=0$ ([[Def - Enriched Category]], [[Def - Monoidal Category]])
- [[Ex - Vect-enriched categories]] (⭐⭐) — $k$-linear categories and the one-object $k$-algebra case ([[Def - Enriched Category]], [[Def - Monoidal Category]], [[Def - Vector Space]])
