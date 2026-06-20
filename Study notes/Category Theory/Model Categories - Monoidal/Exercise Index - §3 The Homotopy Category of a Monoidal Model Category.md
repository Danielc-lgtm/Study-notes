---
type: exercise-index
subject: model-categories
section: "3"
tags: [category-theory, homotopy-theory, foundations]
---

## §3 The Homotopy Category of a Monoidal Model Category — Exercises

This section delivers the payoff: the homotopy category of a monoidal model category is closed symmetric monoidal under the derived tensor $\otimes^{\mathbf{L}}$, with unit $QI$. The exercises drill the three things one must understand about the derived tensor — that it computes the classical derived functors (Tor), that its unit requires the separate unit axiom when the monoidal unit is not cofibrant, and that it is well-defined independent of the cofibrant replacements chosen. The first exercise grounds the abstract $\otimes^{\mathbf{L}}$ in homological algebra, recovering Tor and exhibiting the $\mathbb{Z}/2 \otimes^{\mathbf{L}} \mathbb{Z}/2$ obstruction; the second isolates the role of the unit axiom using symmetric spectra as the non-cofibrant-unit example; the third proves the well-definedness on which the whole derived monoidal structure rests. Together they show how the chapter's machinery produces computable, model-independent structure.

- [[Ex - The derived tensor on chain complexes computes Tor]] (⭐⭐) — computes $H_n(M \otimes^{\mathbf{L}}_R N) = \mathrm{Tor}^R_n(M, N)$ via projective resolution, with the $\mathbb{Z}/2 \otimes^{\mathbf{L}} \mathbb{Z}/2$ example ([[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal]], [[Def - Monoidal Model Category]], [[Def - Cofibrant and Fibrant Objects]], [[Def - Tensor Product of Modules]])
- [[Ex - The unit of the derived tensor and non-cofibrant units]] (⭐⭐) — traces the role of the unit axiom, showing it is automatic when $I$ is cofibrant and irreducible to the pushout-product axiom otherwise (symmetric spectra) ([[Def - Monoidal Model Category]], [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal]], [[Def - Cofibrant and Fibrant Objects]])
- [[Ex - The derived tensor is well-defined independent of replacement]] (⭐⭐) — proves $\otimes^{\mathbf{L}}$ is independent of cofibrant replacement and functorial, localizing where the pushout-product axiom is used ([[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor]], [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal]], [[Def - Cofibrant and Fibrant Objects]], [[Def - Monoidal Model Category]])
