---
type: exercise-index
subject: linear-algebra
section: "5A-5B"
tags: [algebra, linear-algebra]
---

## §5A–B Eigenvalues and Minimal Polynomial — Exercises

The §5A–B exercises drill the core structural content of the chapter: **invariant subspaces, eigenvalues, eigenvectors, and the minimal polynomial**. The unifying frame is that an eigenvalue is the scalar by which $T$ acts on a one-dimensional invariant subspace, and the minimal polynomial $m_T$ is the monic generator of the principal ideal of polynomials annihilating $T$. Over $\mathbb{C}$, eigenvalues exist by the [[Thm - Existence of Eigenvalues on Complex Vector Spaces|existence-of-eigenvalues theorem]]; over $\mathbb{R}$, the parity of $\dim V$ matters. The exercises drill: finding eigenvalues of concrete operators, identifying minimal polynomials by operator equations, recognising the connection between $m_T$'s roots and the spectrum.

- [[Ex - The differentiation operator on polynomials has eigenvalue zero only]] (⭐) — degree-decrease argument showing zero is the only eigenvalue of a graded operator with strictly-lowering action ([[Def - Eigenvalue and Eigenvector]], [[Def - Polynomial of an Operator]]).
- [[Ex - Operators on real odd-dimensional spaces have eigenvalues]] (⭐⭐⭐) — parity argument via the real factorisation theorem; uses an induction-by-2 on the dimension of an invariant subspace constructed from irreducible quadratic factors of $m_T$ ([[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], [[Def - Minimal Polynomial]], [[Def - Division Algorithm and Factorization]], [[Def - Invariant Subspace]]).
- [[Ex - Minimal polynomial of a diagonal matrix]] (⭐) — direct computation showing the minimal polynomial has distinct linear factors corresponding to distinct eigenvalues, not algebraic multiplicities ([[Def - Minimal Polynomial]], [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], [[Thm - Conditions for Diagonalizability]]).
- [[Ex - Powers of an operator and the minimal polynomial]] (⭐⭐) — translates the operator equation $T^k = I$ to $m_T \mid z^k - 1$; on $\mathbb{C}$ this forces distinct linear factors, hence diagonalisability ([[Def - Minimal Polynomial]], [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]], [[Thm - Conditions for Diagonalizability]]).
- **(Web exercise — qualifying-exam classic)** (⭐⭐) — show that if $T \in \mathcal{L}(\mathbb{C}^n)$ is such that $T^2 = T$, then $T$ is the identity, the zero operator, or a non-trivial projection. The minimal polynomial argument: $m_T \mid z^2 - z = z(z-1)$, so $m_T \in \{z, z-1, z(z-1)\}$; the three cases correspond to the three classifications ([[Def - Minimal Polynomial]], [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]]).
