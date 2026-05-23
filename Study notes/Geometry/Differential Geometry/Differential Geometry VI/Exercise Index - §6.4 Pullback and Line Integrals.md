---
type: exercise-index
subject: differential-geometry
section: "6.4"
tags: [geometry, differential-geometry, pullback, line-integral]
---

## §6.4 Pullback and Line Integrals — Exercises

This section drills the pullback formalism for 1-forms and the line integral. The reparameterization-invariance exercise establishes the well-posedness of the line integral as a function of the oriented arc, not the parametrization — the structural foundation for all line-integral computations. The conservative-form-on-the-punctured-plane exercise gives the canonical illustration of the closed-but-not-exact phenomenon: a closed 1-form whose loop integral is nonzero, detecting the failure of simple connectivity of the underlying manifold. Together these exercises establish the language and tools that flow into Stokes's theorem and de Rham cohomology in later chapters.

- [[Ex - Line Integral is Independent of Parameterization]] (⭐) — Verify that the line integral $\int_\gamma \omega$ is invariant under orientation-preserving reparameterization and reverses sign under orientation-reversal. ([[Def - Line Integral of a 1-Form]], [[Def - Covector Field and Differential 1-Form]], [[Def - Smooth Map between Manifolds]])
- [[Ex - A Conservative 1-Form on R² Minus Origin]] (⭐⭐) — Demonstrate that the angle-form $(x dy - y dx)/(x^2+y^2)$ on the punctured plane is closed but not exact, by computing $\int_\gamma \omega = 2\pi$ around the unit circle. ([[Def - Covector Field and Differential 1-Form]], [[Def - Line Integral of a 1-Form]], [[Def - The Differential of a Function as a 1-Form]], [[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact]])
- [[Ex - Constructing the Cotangent Bundle from Transition Functions]] (⭐⭐) — Apply the construction lemma to assemble $T^*M$ from its coordinate-frame trivialization data, the source of all 1-form pullback computations in coordinates. ([[Thm - Vector Bundle Construction Lemma]], [[Def - Cotangent Space and Cotangent Bundle]], [[Def - Pullback of a Covector Field]], [[Def - Transition Function of a Vector Bundle]])
