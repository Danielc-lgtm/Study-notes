---
type: exercise-index
subject: linear-algebra
section: "7C-7D"
tags: [algebra, linear-algebra]
---

## §7C–D Positive Operators, Isometries, and Matrix Factorisations — Exercises

The exercises of §7C–D drill the constructive machinery of positive operators, [[Def - Isometry|isometries]], and the corresponding matrix factorisations (Cholesky, QR-style orthonormalisation). The recurring techniques are: take square roots via the spectral theorem; verify [[Def - Isometry|isometry]] via columns or $S^*S = I$; compute triangular factors directly from the matrix equations. Each entry below names the exercise, summarises the technique it drills in one line, and lists in parentheses every definition and theorem invoked.

- [[Ex - Square root of a 2x2 positive matrix]] (⭐) — compute $\sqrt T$ for a specific positive definite matrix via spectral decomposition: diagonalise, square-root eigenvalues, reassemble ([[Thm - Positive Operators Have a Unique Square Root]], [[Def - Positive Operator]], [[Thm - Real Spectral Theorem]])
- [[Ex - Cholesky factorization by hand]] (⭐⭐) — direct algorithmic computation of the Cholesky factor: walk through $T_{ij} = (R^*R)_{ij}$ to determine the entries of $R$ one at a time, with the algorithm's positive-diagonal check serving as a positive-definiteness check ([[Thm - Cholesky Factorization]], [[Def - Positive Operator]])
- [[Ex - Unitary 2x2 matrices form a Lie group]] (⭐⭐) — parameterise $U(2)$ explicitly and compute its real [[Def - Dimension|dimension]]; bridge to Lie theory ([[Def - Unitary Operator]], [[Def - Isometry]], [[Def - Group]], [[Def - Subgroup]])
