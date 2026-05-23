---
type: exercise-index
subject: differential-geometry
section: "10.3"
tags: [geometry, differential-geometry, frobenius]
---

## §10.3 Distributions and the Frobenius Theorem — Exercises

This section's exercises drill the involutivity test for distributions and its consequences via Frobenius's theorem. The unifying theme is the dichotomy involutive (integrable, foliation exists) versus non-involutive (no integral submanifolds, "twisted" plane field), with the test reducible to either a Lie-bracket computation on a local frame or the algebraic identity $\omega \wedge d\omega = 0$ for codimension-$1$ distributions. The PDE-compatibility exercise extends this to overdetermined first-order systems, showing how Frobenius is the geometric content of every classical PDE existence theorem.

- [[Ex - An Involutive Distribution from Three Vector Fields]] (⭐⭐) — bracket computation for three explicit vector fields on $\mathbb{R}^4$; checking whether each pairwise bracket lies in the spanning subspace. Illustrates both the local-frame criterion and the failure mode of "natural-looking" distributions ([[Def - Distribution on a Manifold]], [[Def - Involutive Distribution]], [[Def - The Lie Bracket of Vector Fields]])
- [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]] (⭐⭐) — direct computation of $\alpha \wedge d\alpha = dx \wedge dy \wedge dz$ for the standard contact form; geometric picture of the helical screw twist. Cross-checks via the bracket $[X, Y] = \partial_z \notin D$. The prototype non-integrable example, foundational to contact geometry ([[Def - Distribution on a Manifold]], [[Def - Involutive Distribution]], [[Thm - Frobenius Theorem in Forms Language]])
- [[Ex - Frobenius Theorem Applied to an Overdetermined PDE]] (⭐⭐⭐) — reformulating an overdetermined system $\partial u/\partial x = \alpha, \partial u/\partial y = \beta$ as an integrability problem for a distribution on $\mathbb{R}^3$; the compatibility condition $\partial_y\alpha + \beta\partial_z\alpha = \partial_x\beta + \alpha\partial_z\beta$ as the involutivity test ([[Def - Involutive Distribution]], [[Thm - The Frobenius Theorem]])
