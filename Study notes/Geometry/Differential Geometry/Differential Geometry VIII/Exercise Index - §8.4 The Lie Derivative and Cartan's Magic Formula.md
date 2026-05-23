---
type: exercise-index
subject: differential-geometry
section: "8.4"
tags: [geometry, differential-geometry]
---

## §8.4 The Lie Derivative and Cartan's Magic Formula — Exercises

This section's exercises drill the central algebraic identity of the chapter: Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$, which connects the geometric Lie derivative (defined via flows) to the algebraic operators $d$ and $\iota_X$. The exercises train the reflex of *never* using the flow definition for computation and *always* using Cartan's formula. The Leibniz-rule exercise shows that $\mathcal{L}_X$ is an ungraded derivation (distinct from $d$ and $\iota_X$, which are graded), and the consequences include the commutation $\mathcal{L}_X d = d \mathcal{L}_X$ that organizes equivariant cohomology.

- [[Ex - Cartan's Magic Formula via a Direct Computation]] (⭐⭐) — verify $\mathcal{L}_X = d\iota_X + \iota_X d$ on functions and on $\omega = u\,dv$ by direct computation, propagate by linearity, and derive $\mathcal{L}_X d = d\mathcal{L}_X$ in one line ([[Thm - Cartan's Magic Formula]], [[Def - Lie Derivative of a Differential Form]], [[Def - Exterior Derivative on a Manifold]], [[Def - Interior Product (Contraction with a Vector Field)]])
- [[Ex - The Lie Derivative Satisfies the Leibniz Rule]] (⭐) — prove $\mathcal{L}_X(\omega \wedge \eta) = \mathcal{L}_X\omega \wedge \eta + \omega \wedge \mathcal{L}_X\eta$ via the flow definition (using that pullback respects wedge) and alternatively via Cartan's formula (with the sign cross-terms canceling) ([[Def - Lie Derivative of a Differential Form]], [[Thm - Cartan's Magic Formula]])
- **Compute $\mathcal{L}_{\partial_x}(y\,dz)$ and $\mathcal{L}_{\partial_x}(dy \wedge dz)$ on $\mathbb{R}^3$ via Cartan's formula** (⭐) — mechanical practice with the algebraic side of Cartan; verify the answer matches the geometric expectation (translation-invariant forms have zero $\mathcal{L}_{\partial_x}$) ([[Thm - Cartan's Magic Formula]])
- **Prove Liouville's theorem: a Hamiltonian vector field preserves the symplectic form** (⭐⭐) — for a symplectic manifold $(M, \omega)$ with $d\omega = 0$, define $X_H$ by $\iota_{X_H}\omega = dH$, then show $\mathcal{L}_{X_H}\omega = d^2 H + 0 = 0$ in one Cartan + $d^2 = 0$ application ([[Thm - Cartan's Magic Formula]], [[Thm - d-Squared-is-Zero]])
- **Show $[\mathcal{L}_X, \iota_Y] = \iota_{[X, Y]}$ using Cartan's formula and properties of the Lie bracket** (⭐⭐) — apply Cartan to both sides and use the commutators of $d$ and $\iota_X$ with the Lie derivative ([[Thm - Cartan's Magic Formula]], [[Def - The Lie Bracket of Vector Fields]])
