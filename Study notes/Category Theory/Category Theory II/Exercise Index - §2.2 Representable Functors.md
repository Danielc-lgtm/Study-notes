---
type: exercise-index
subject: category-theory
section: "2.2"
tags: [category-theory, foundations]
---

## §2.2 Representable Functors — Exercises

These exercises build the central skill of the section: recognizing when a $\mathbf{Set}$-valued functor is secretly a hom-functor, and finding the representing object together with its universal element. The first establishes the prototype — forgetful functors are represented by free objects on one generator — across groups, rings, and spaces. The second carries the same technique into algebraic geometry, showing the affine line, affine space, and the multiplicative group are representable functors of points, i.e. affine schemes. The third sharpens the concept by exhibiting a functor that is *not* representable (the covariant power set) and giving two refutation techniques: limit-preservation and the category-of-elements criterion. The recurring move is "guess the universal element, then evaluation is the natural isomorphism", and the recurring diagnostic is "representable functors preserve limits".

- [[Ex - Representable forgetful functors]] (⭐⭐) — forgetful functors are represented by free objects on one generator; the universal element is the generic generator ([[Def - Hom-Functor and Representable Functor]], [[Def - Group]], [[Def - Ring]], [[Def - Topological Space]])
- [[Ex - The affine line is a representable functor]] (⭐⭐) — the functors of points $\mathbb{A}^1, \mathbb{A}^n, \mathbb{G}_m$ are representable by $k[x], k[x_1,\dots,x_n], k[x,x^{-1}]$; adjoining an inverse encodes "image must be a unit" ([[Def - Hom-Functor and Representable Functor]], [[Def - Ring]], [[Def - Universal Element]])
- [[Ex - A non-representable functor]] (⭐⭐) — refuting representability of the covariant power-set functor via limit-preservation and the absence of an initial object in its category of elements; pushforward vs. pullback ([[Def - Hom-Functor and Representable Functor]], [[Def - Category of Elements]], [[Def - Limit and Colimit]])
