---
type: exercise-index
subject: category-theory
section: "4.3"
tags: [category-theory, foundations]
---

## §4.3 Free-Forgetful Adjunctions and Reflective Subcategories — Exercises

These exercises cover the two great families of adjunctions in practice: free-forgetful adjunctions (left adjoints to forgetting structure) and reflective subcategories (left adjoints to full inclusions). The recurring technique is to recognise a construction as a left adjoint by exhibiting its unit's universal property — insertion of generators for free functors, the universal "best approximation" map for reflectors — and then to harvest the abstract consequences (uniqueness, closure under limits, the colimit formula). The topology exercise shows a forgetful functor with adjoints on *both* sides; the abelianisation and sheafification exercises are the same reflector pattern in algebra and in geometry, with the sheafification one delivering the algebraic-geometry payoff of the whole chapter.

- [[Ex - Discrete and indiscrete topologies as adjoints]] (⭐⭐) — establish $\mathrm{Disc}\dashv U\dashv\mathrm{Indisc}$ for $\mathbf{Top}\to\mathbf{Set}$; discrete is free (left), indiscrete is cofree (right) ([[Def - Adjunction]], [[Def - Topological Space]], [[Def - Free-Forgetful Adjunction]])
- [[Ex - Abelianization is left adjoint to inclusion]] (⭐⭐⭐) — prove $\mathbf{Ab}\hookrightarrow\mathbf{Grp}$ is reflective with reflector $G\mapsto G/[G,G]$, via the commutator subgroup and the universal property of the quotient ([[Def - Reflective Subcategory]], [[Def - Abelian Group]], [[Def - Group]], [[Thm - First Isomorphism Theorem]])
- [[Ex - Sheafification as a reflective localization]] (⭐⭐⭐) — show sheaves are reflective in presheaves with reflector sheafification; deduce limits are objectwise but colimits must be sheafified ([[Def - Reflective Subcategory]], [[Def - Adjunction]], [[Def - Presheaf]], [[Thm - Right Adjoints Preserve Limits]])
