---
type: exercise-index
subject: differential-geometry
section: "8.1"
tags: [geometry, differential-geometry]
---

## §8.1 Alternating Tensors and the Wedge Product — Exercises

This section's exercises drill the algebraic core of the calculus of forms: the wedge product as the canonical multiplication on alternating tensors, the determinant identity that makes a wedge of $1$-forms reproduce the determinant of an evaluation matrix, and the parity rule $\omega \wedge \omega = 0$ for odd-degree forms (with the symplectic-form counterexample for even degrees). The mechanical computations train the bookkeeping of anticommutativity and the reduction to increasing multi-indices; the conceptual exercises train recognition of the wedge as a determinant in disguise and of the algebra structure of $\Omega^\bullet(M)$.

- [[Ex - Wedge Product of 1-Forms is Antisymmetric]] (⭐) — direct verification of $\omega \wedge \omega = 0$ for $1$-forms, the graded commutativity rule, and a counterexample for even-degree squared ([[Def - The Wedge Product on a Manifold]], [[Thm - Wedge Product Properties]])
- **Compute the wedge of two explicit $1$-forms in coordinates and verify the determinant identity** (⭐) — take $\omega = a\,dx + b\,dy$ and $\eta = c\,dx + d\,dy$ on $\mathbb{R}^2$ and confirm $\omega \wedge \eta = (ad - bc)\,dx \wedge dy$, matching the determinant of the coefficient matrix ([[Thm - Wedge Product Properties]])
- **Show that $\omega^1, \dots, \omega^k$ are linearly independent iff $\omega^1 \wedge \cdots \wedge \omega^k \neq 0$** (⭐⭐) — uses the determinant identity in both directions: if dependent, expand one as a combination of others and the wedge picks up a repeated factor; if independent, extend to a basis and evaluate ([[Def - Alternating Tensor and Lambda^k V*]], [[Thm - Wedge Product Properties]])
- **Verify the symplectic form $\omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4$ on $\mathbb{R}^4$ has $\omega^2 = 2\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 \neq 0$** (⭐) — direct expansion of $\omega \wedge \omega$, the standard example showing even-degree forms can have nonzero squares ([[Thm - Wedge Product Properties]])
