---
type: exercise-index
subject: linear-algebra
section: "7E-7F"
tags: [algebra, linear-algebra]
---

## §7E–F SVD and Polar Decomposition — Exercises

The exercises of §7E–F drill the universality of the singular value decomposition: every linear map has one, and from it one reads off the operator norm, the rank, the best low-rank approximation, and the polar decomposition. The recurring techniques are: spectrally decompose $T^*T$ to get the singular values; expand in the right-singular basis to compute norms and extremal vectors; use a dimension argument for lower bounds in low-rank approximation. Each entry below names the exercise, summarises the technique it drills in one line, and lists in parentheses every definition and theorem invoked.

- [[Ex - SVD computes the operator norm]] (⭐⭐) — expand the supremum $\sup_{\|v\| = 1} \|Tv\|$ in the right-singular orthonormal basis; the maximum of a weighted sum is its largest weight, attained at the top right-singular vector ([[Thm - Singular Value Decomposition]], [[Def - Singular Values]])
- [[Ex - Polar decomposition unique for invertible operators]] (⭐⭐) — exploit uniqueness of the positive square root to make the polar factor $R = |T|$ unique always, and use invertibility to pin down $S = TR^{-1}$ uniquely when $T$ is invertible ([[Thm - Polar Decomposition]], [[Thm - Positive Operators Have a Unique Square Root]], [[Def - Unitary Operator]])
- [[Ex - Best low-rank approximation via SVD]] (⭐⭐⭐) — Eckart–Young theorem: truncate the SVD to its top $k$ singular components for the best rank-$k$ approximation, with the lower bound proved by the **dimension intersection argument** (kernel of $B$ intersects top-$(k+1)$ right-singular span in a non-trivial vector) ([[Thm - Singular Value Decomposition]], [[Def - Singular Values]], [[Ex - SVD computes the operator norm]])
