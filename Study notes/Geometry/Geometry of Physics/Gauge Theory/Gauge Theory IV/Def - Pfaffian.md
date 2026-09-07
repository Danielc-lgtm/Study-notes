---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Linear Map"
tags: [geometry, gauge-theory, algebra, characteristic-classes]
---

# Prerequisite Concepts

- [[Def - Linear Map]]

# Notation

For a $2n \times 2n$ skew-symmetric matrix $A = -A^T$, the Pfaffian is denoted $\mathrm{Pf}(A)$. It is a polynomial of degree $n$ in the entries $A_{ij}$, satisfying $\mathrm{Pf}(A)^2 = \det(A)$. When $A$ is the matrix of a $2$-form $\Omega$ on a $2n$-dimensional oriented vector space with respect to an oriented basis, $\mathrm{Pf}(\Omega)$ is the canonical "top exterior power" of $\Omega$. For an $\mathfrak{so}(2n)$-valued differential $2$-form $\Omega \in \Omega^2(M; \mathfrak{so}(2n))$ on a manifold $M$, $\mathrm{Pf}(\Omega)$ is the resulting scalar-valued $2n$-form, written componentwise in terms of an orthonormal frame. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the registry.

---

# Axiom Motivation

The Pfaffian is the **unique square root of the determinant of a skew-symmetric matrix**, with the sign fixed by the orientation. Why do we need a square root? Because the determinant of a $2n \times 2n$ skew-symmetric matrix is always the square of a polynomial in the entries — and that polynomial *is* the Pfaffian. This is a structural feature of $\mathfrak{so}(2n)$ (the Lie algebra of skew-symmetric matrices): the invariant polynomial of degree $n$ that is "the square root of the determinant" is a genuine polynomial (not just a square-root expression), and it is the most important $\mathrm{SO}(2n)$-invariant of degree $n$ on $\mathfrak{so}(2n)$. The discovery that this square root is polynomial — and not, say, $\sqrt{\det}$ in some analytic sense — is the substance of the construction.

Why is the determinant a perfect square in this case? Because every skew-symmetric matrix is conjugate (by an orthogonal matrix) to a block-diagonal form with $2 \times 2$ blocks $\lambda_j J = \begin{pmatrix}0 & \lambda_j \\ -\lambda_j & 0\end{pmatrix}$. The determinant is then $\prod_j \lambda_j^2 = (\prod \lambda_j)^2$, and the product $\prod_j \lambda_j$ is precisely the Pfaffian in canonical form. Going back to general skew-symmetric $A$, the Pfaffian is the unique polynomial that reduces to $\prod \lambda_j$ in this canonical form and is $\mathrm{SO}(2n)$-invariant (transforming by $\det g = \pm 1$ under change of basis by $g \in \mathrm{O}(2n)$; the sign $+1$ for $g \in \mathrm{SO}(2n)$).

Why insist on the **polynomial** form $\mathrm{Pf}(A) = \frac{1}{2^n n!}\sum_\sigma \mathrm{sgn}(\sigma)\prod A_{\sigma(2i-1),\sigma(2i)}$? Because it gives an *explicit*, sign-canonical formula that does not require diagonalization. The polynomial form is what allows us to define the Pfaffian of a *differential-form-valued* skew-symmetric matrix — the curvature 2-form of an $\mathrm{SO}(2n)$-bundle — where diagonalization is meaningless but polynomial substitution is straightforward. This is the entire content of the Gauss-Bonnet-Chern theorem: $\mathrm{Pf}(\Omega)$ for $\Omega$ a curvature 2-form is the right "top form" because of the polynomial definition.

Why **odd-dimensional** skew-symmetric matrices have $\mathrm{Pf} = 0$? An odd-sized skew-symmetric matrix has $\det = 0$ (as $\det(-A) = (-1)^{n}\det(A) = -\det(A)$ for $n$ odd, forcing $\det = 0$). The Pfaffian is the square root, so it too must vanish. This is why the Gauss-Bonnet-Chern theorem holds only in even dimensions: in odd dimensions, $\chi(M) = 0$ automatically (by Poincaré duality), matching the vanishing of $\mathrm{Pf}$.

The **sign convention** is fixed by orientation. The naive square-root $\pm\sqrt{\det A}$ is ambiguous; the Pfaffian's polynomial formula picks the canonical sign by the explicit signed sum over pairings of indices. Specifically, $\mathrm{Pf}(J^{\oplus n}) = +1$ where $J = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$, fixing the sign on the standard skew form, and the $\mathrm{SO}(2n)$-equivariance fixes the sign everywhere else. Without this convention, the Euler class would be defined only up to sign, and the Euler characteristic could not be recovered as $\int \mathrm{Pf}(\Omega)/(2\pi)^n$ with the correct sign.

---

# The Definition

Let $A = (A_{ij})$ be a $2n \times 2n$ real (or complex) skew-symmetric matrix, $A_{ij} = -A_{ji}$. The **Pfaffian** of $A$ is the polynomial
$$\mathrm{Pf}(A) \;=\; \frac{1}{2^n \, n!} \sum_{\sigma \in S_{2n}} \mathrm{sgn}(\sigma) \prod_{i=1}^n A_{\sigma(2i-1),\,\sigma(2i)}.$$
Equivalently, in terms of "pairings" (partitions of $\{1, \ldots, 2n\}$ into ordered pairs):
$$\mathrm{Pf}(A) \;=\; \sum_{\alpha \in \mathcal{P}_n} \mathrm{sgn}(\alpha) \prod_{(i, j) \in \alpha} A_{i, j},$$
where $\mathcal{P}_n$ is the set of pairings $\{(i_1, j_1), \ldots, (i_n, j_n)\}$ of $\{1, \ldots, 2n\}$ with $i_k < j_k$ and $i_1 < i_2 < \cdots < i_n$, and $\mathrm{sgn}(\alpha)$ is the sign of the permutation $(i_1, j_1, i_2, j_2, \ldots, i_n, j_n)$.

The Pfaffian satisfies the **fundamental identity**
$$\mathrm{Pf}(A)^2 \;=\; \det(A),$$
the **transformation law**
$$\mathrm{Pf}(BAB^T) \;=\; \det(B) \cdot \mathrm{Pf}(A) \qquad \text{for any } B \in M_{2n \times 2n},$$
and is the **unique** $\mathrm{SO}(2n)$-invariant polynomial of degree $n$ on $\mathfrak{so}(2n)$ (up to scalar), normalized by $\mathrm{Pf}(J^{\oplus n}) = +1$ where $J = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$.

For an $\mathfrak{so}(2n)$-valued differential $2$-form $\Omega = (\Omega^a{}_b) \in \Omega^2(M; \mathfrak{so}(2n))$ on a smooth manifold $M$, the **Pfaffian** $\mathrm{Pf}(\Omega) \in \Omega^{2n}(M)$ is the scalar-valued $2n$-form obtained by substituting wedge products for matrix products in the polynomial formula:
$$\mathrm{Pf}(\Omega) \;=\; \frac{1}{2^n \, n!} \sum_{\sigma \in S_{2n}} \mathrm{sgn}(\sigma) \, \Omega^{\sigma(1)}{}_{\sigma(2)} \wedge \Omega^{\sigma(3)}{}_{\sigma(4)} \wedge \cdots \wedge \Omega^{\sigma(2n-1)}{}_{\sigma(2n)}.$$

For an odd-sized skew-symmetric matrix $A$ ($n$ odd), $\mathrm{Pf}(A) = 0$.

---

# Relate to Other Fields / Compression

The Pfaffian is **the natural top exterior power of a 2-form**. Given a 2-form $\omega = \tfrac{1}{2}\omega_{ij} dx^i \wedge dx^j$ on a $2n$-dimensional oriented vector space, the $n$-fold wedge $\omega \wedge \omega \wedge \cdots \wedge \omega$ (with $n$ copies) is a top form, and after dividing by $n!$ it equals $\mathrm{Pf}(\omega) \cdot dx^1 \wedge \cdots \wedge dx^{2n}$ — the Pfaffian appears as the coefficient. So $\mathrm{Pf}$ is the polynomial that converts the matrix data of a $2$-form into its $n$-fold wedge.

The Pfaffian is the **degree-$n$ Chern-Weil polynomial for $\mathrm{SO}(2n)$**: in the Chern-Weil construction, $\mathrm{SO}(2n)$-invariant polynomials on $\mathfrak{so}(2n)$ produce characteristic classes of oriented Riemannian vector bundles. The space of $\mathrm{SO}(2n)$-invariant polynomials is generated by the elementary symmetric polynomials in the eigenvalues of $A/i$ (giving the Pontryagin classes) *plus* the Pfaffian (giving the Euler class). The Pfaffian is special because it is *not* expressible as a polynomial in those elementary symmetric polynomials over the rationals — the Euler class has nontrivial information beyond the Pontryagin classes.

In **physics**, the Pfaffian appears as the partition function of a system of Majorana fermions: $\int e^{i \bar\psi^T A \psi/2} D\psi = \mathrm{Pf}(A)$. The square-root-of-determinant character reflects that Majorana fermions are "half" of Dirac fermions, with $\det A$ being the Dirac partition function and $\mathrm{Pf}(A)$ its Majorana square root.

**True name:** the Pfaffian is **the canonical-sign square root of the determinant of a skew-symmetric matrix, given as an explicit signed sum over pairings of indices**. The polynomial form is what makes it computable on form-valued matrices (where diagonalization is meaningless), and the sign canonization makes it the right object for orientation-dependent integrals like the Euler characteristic.

---

# Examples / Corollaries

**Is an instance: $\mathrm{Pf}\begin{pmatrix}0 & a \\ -a & 0\end{pmatrix} = a$.** The $2 \times 2$ case: the matrix has determinant $a^2$, and the polynomial Pfaffian is the single entry $A_{12} = a$. Note $a^2 = \det A$ is squared, confirming $\mathrm{Pf}^2 = \det$.

**Is an instance: $\mathrm{Pf}\begin{pmatrix}0 & a & b & c \\ -a & 0 & d & e \\ -b & -d & 0 & f \\ -c & -e & -f & 0\end{pmatrix} = af - be + cd$.** The $4 \times 4$ case: three pairings $\{(12)(34), (13)(24), (14)(23)\}$, with signs $+, -, +$ from the permutation parity. Verification: $\det A = (af - be + cd)^2$ — a classical identity.

**Is an instance: $\mathrm{Pf}(J^{\oplus n}) = 1$ for $J = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$.** The block-diagonal form with $n$ copies of $J$ has $\det = 1^{2n} = 1$ and $\mathrm{Pf} = 1$. This is the normalization that fixes the sign.

**Is an instance: Gauss curvature is $\mathrm{Pf}(\Omega)/(2\pi)$ on a 2-dimensional Riemannian manifold.** For a $2$-surface, the curvature 2-form $\Omega \in \Omega^2(M; \mathfrak{so}(2))$ is a $1 \times 1$ matrix (since $\mathfrak{so}(2) = \mathbb{R}$), with single entry $\Omega^1{}_2 = -K \,\sigma^1 \wedge \sigma^2$. The Pfaffian is just $-\Omega^1{}_2 = K \,\sigma^1 \wedge \sigma^2 = K \, dA$. Dividing by $2\pi$ and integrating gives $\chi(M)$ — the Gauss-Bonnet theorem.

**Is NOT an instance: $\mathrm{Pf}$ of a non-skew-symmetric matrix.** The Pfaffian formula assumes the polynomial inputs are antisymmetric in indices; for a non-skew matrix it is either undefined or trivially zero (after the wedge-product collapse). This is why the Pfaffian only lives in $\mathfrak{so}(2n)$, not in all of $\mathfrak{gl}(2n)$.

**Is NOT an instance: $\mathrm{Pf}$ of an odd-dimensional skew matrix.** Any $(2n+1) \times (2n+1)$ skew matrix has $\det = 0$ (as $\det(A) = \det(-A^T) = (-1)^{2n+1}\det A = -\det A$). The Pfaffian is correspondingly $0$, and the Euler class of an odd-dimensional manifold vanishes.

**Corollary ($\mathrm{Pf}(A)^2 = \det A$).** Verified by the polynomial identity above and by the eigenvalue diagonalization.

**Corollary ($\mathrm{Pf}(BAB^T) = \det(B)\mathrm{Pf}(A)$).** This is the transformation law, the algebraic reason $\mathrm{Pf}$ is $\mathrm{SO}(2n)$-invariant: if $B \in \mathrm{SO}(2n)$, $\det B = 1$, so $\mathrm{Pf}$ is unchanged. For $B \in \mathrm{O}(2n) \setminus \mathrm{SO}(2n)$, $\det B = -1$, so $\mathrm{Pf}$ changes sign — consistent with the orientation-dependence of the Euler class.

**Corollary (the de Rham cohomology class $[\mathrm{Pf}(\Omega)/(2\pi)^n] \in H^{2n}(M)$ is independent of the metric and the connection — it is a topological invariant).** This is Chern-Weil theory specialized to the Pfaffian; the class is the Euler class $e(TM)$.

**Calibration check.** Verify (i) the $2 \times 2$ formula by hand; (ii) the $4 \times 4$ formula by listing the three pairings and computing signs; (iii) for the round metric on $S^2$ with $K \equiv 1$, $\frac{1}{2\pi}\int_{S^2} \mathrm{Pf}(\Omega) = \frac{1}{2\pi}\int_{S^2} K\,dA = \frac{1}{2\pi} \cdot 4\pi = 2 = \chi(S^2)$.

---

# Unlocked by This

> [!tip] Euler Class of an Oriented Real Vector Bundle *(from Characteristic Classes)*
> The **Euler class** of a real oriented rank-$2n$ vector bundle $E \to M$ with metric is the de Rham cohomology class $e(E) = [\mathrm{Pf}(\Omega^\nabla)/(2\pi)^n] \in H^{2n}(M; \mathbb{R})$ of the Pfaffian of the curvature 2-form of any metric connection $\nabla$ on $E$. The class is independent of the connection (Chern-Weil). For $E = TM$ on a closed oriented manifold, $\int_M e(TM) = \chi(M)$. See [[Def - The Euler Class of a Real Oriented Vector Bundle]].

> [!tip] Pfaffian Line Bundle and the Cheeger–Simons Theory *(from Geometric Topology)*
> When $E$ is a *complex* vector bundle and one wishes to extract a "square root of the determinant line bundle" $\sqrt{\det E}$, the Pfaffian line bundle is the construction. It plays a central role in the modern theory of Cheeger–Simons differential characters, anomalies in quantum field theory, and the Pfaffian formula for the partition function of chiral fermions.

> [!tip] Berezinian / Super-Determinant *(from Supermathematics)*
> The Pfaffian is the bosonic shadow of the Berezinian, the super-determinant for $\mathbb{Z}/2$-graded vector spaces. Just as $\det$ is the natural top exterior power for an even vector space, the Pfaffian is the natural object for the odd part, capturing fermionic integration measures. This is the bridge from classical Pfaffian theory to the path integrals of supersymmetric quantum field theory.
