---
type: exercise-index
subject: linear-algebra
section: "9B-9C"
tags: [algebra, linear-algebra]
---

## §9B–C Alternating Multilinear Forms and Determinants — Exercises

The exercises of §9B–C exercise the chapter's central machinery: alternating multilinear forms, the one-dimensionality $\dim V^{(n)}_{\mathrm{alt}} = 1$ that defines the determinant, the Leibniz formula and its corollaries (multiplicativity, eigenvalue product, cofactor expansion), and the bridges to volume scaling and matrix factorisation. The master pattern is "alternating multilinear-on-$n$-tuples-of-$n$-vectors uniquely determines a scalar — and that scalar is the determinant", with consequences flowing through multiplicativity and the upper-triangular reduction.

- [[Ex - The wedge product as an alternating multilinear form]] (⭐⭐) — show that the wedge product $\varphi_1 \wedge \cdots \wedge \varphi_m$ of dual vectors, defined via the determinant of $[\varphi_i(v_j)]$, is alternating $m$-linear and that sorted wedges of basis dual vectors form a basis of $V^{(m)}_{\mathrm{alt}}$ ([[Def - Multilinear Form]], [[Def - Alternating Multilinear Form]], [[Def - Dual Space]])

- [[Ex - Determinant of an upper-triangular matrix is the product of diagonal entries]] (⭐) — show $\det A = \prod \lambda_i$ for upper-triangular $A$ via the Leibniz formula collapse: only the identity permutation contributes, because any other permutation forces an entry below the diagonal ([[Def - Determinant]])

- [[Ex - Determinant of a block matrix]] (⭐⭐) — prove the block-triangular determinant formula $\det \begin{pmatrix} A & B \\ 0 & D\end{pmatrix} = \det A \cdot \det D$ via Leibniz, and the Schur complement formula $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det D \cdot \det(A - B D^{-1} C)$ via Schur factorisation. Drills the technique of computing [[Def - Determinant|determinants]] by matrix factorisation ([[Def - Determinant]], [[Thm - Determinant is Multiplicative]])

- [[Ex - Cayley-Hamilton via determinants and via the minimal polynomial agree]] (⭐⭐⭐) — reconcile LADR's two proofs of the [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley-Hamilton]] theorem: the determinantal proof via the adjugate identity $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$ (treating both sides as matrix-coefficient polynomials in $z$), and the spectral proof via the generalised eigenspace decomposition. Both establish $p_T(T) = 0$, with each proof working in different generality ([[Def - Determinant]], [[Def - Minimal Polynomial]], [[Thm - Cofactor Expansion and Cramer's Rule]], [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity]])

- **Vandermonde determinant exercise (⭐⭐).** Compute $\det V(x_1, \dots, x_n) = \prod_{i < j} (x_j - x_i)$ for the Vandermonde matrix $V_{ij} = x_j^{i-1}$. Use alternating-multilinearity and the unique determination of an alternating $n$-linear form by its value on a single basis. *Technique drilled:* applying the "two alternating $n$-linear forms agree on a basis $\Rightarrow$ equal" identification. Uses [[Def - Determinant]], [[Def - Alternating Multilinear Form]].
