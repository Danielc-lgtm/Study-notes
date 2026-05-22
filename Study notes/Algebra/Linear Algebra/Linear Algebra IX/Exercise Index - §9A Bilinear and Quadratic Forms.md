---
type: exercise-index
subject: linear-algebra
section: "9A"
tags: [algebra, linear-algebra]
---

## §9A Bilinear and Quadratic Forms — Exercises

The exercises of §9A drill the foundational toolkit of symmetric bilinear forms and quadratic forms: the matrix-of-a-bilinear-form correspondence, the symmetric/alternating decomposition, the polarisation identity that converts quadratic forms into symmetric bilinear forms, and the structural classification of real symmetric forms by their signature. The master pattern is "bilinear-form-with-a-symmetric-matrix has all of $\mathbb{R}^n$-linear-algebra at its disposal" — diagonalisation, spectral theorem, Sylvester's law, congruence classification — and the exercises here exercise each piece of that toolkit.

- [[Ex - The bilinear form determined by a symmetric matrix]] (⭐) — verify directly that a symmetric matrix $M$ gives a symmetric bilinear form $\beta_M(u, v) = u^t M v$, compute its matrix in the standard basis, and characterise positive-definiteness via the eigenvalues of $M$ ([[Def - Bilinear Form]], [[Def - Symmetric and Alternating Bilinear Form]], [[Thm - Real Spectral Theorem]])

- [[Thm - Diagonalization of a Symmetric Bilinear Form]] is the headline result of this section, with proof via induction-and-non-isotropic-vector. The diagonalisation is the necessary input to **[[Thm - Sylvester's Law of Inertia]]**, which classifies real symmetric bilinear forms up to congruence by their signature.

- **Polarisation exercise (⭐).** Given a quadratic form $q(x, y) = 3x^2 - 4xy + 7y^2$ on $\mathbb{R}^2$, find the unique symmetric bilinear form $\rho$ with $q = q_\rho$, write out its matrix, and check positive-definiteness. *Technique drilled:* the polarisation identity $\rho(u, w) = \tfrac{1}{2}(q(u+w) - q(u) - q(w))$, converting quadratic to bilinear data. Uses [[Def - Quadratic Form]], [[Def - Symmetric and Alternating Bilinear Form]].

- **Signature computation exercise (⭐⭐).** For the symmetric matrix $M = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 1 \\ 0 & 1 & 0 \end{pmatrix}$, find the signature of the associated symmetric bilinear form on $\mathbb{R}^3$ by simultaneous row-and-column operations (congruence diagonalisation). *Technique drilled:* Sylvester's law of inertia applied via the congruence-class normal form. Uses [[Thm - Diagonalization of a Symmetric Bilinear Form]], [[Thm - Sylvester's Law of Inertia]].
