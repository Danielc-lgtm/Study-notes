---
type: theorem
subject: linear-algebra
prereqs:
  - "Thm - Gram-Schmidt Procedure"
  - "Def - Isometry"
  - "Def - Unitary Operator"
  - "Def - Orthonormal Basis"
tags: [algebra, linear-algebra]
---

# Notation

$\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. A matrix $A \in \mathbb{F}^{m \times n}$ has columns $a_1, \ldots, a_n$ in $\mathbb{F}^m$. A matrix has **orthonormal columns** if its columns form an orthonormal list in the standard inner product of $\mathbb{F}^m$. A matrix is **upper-triangular** if $R_{ij} = 0$ for $i > j$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (QR Factorisation).** Let $A \in \mathbb{F}^{m \times n}$ with $m \geq n$ have linearly independent columns. Then there exist unique:
> - $Q \in \mathbb{F}^{m \times n}$ with orthonormal columns (an [[Def - Isometry|isometry]]),
> - $R \in \mathbb{F}^{n \times n}$ upper-triangular with positive real diagonal entries,
>
> such that
> $$A = QR.$$
>
> When $m = n$ (and $A$ is square invertible), $Q$ is unitary and $R$ is invertible upper-triangular. The factorisation is then called the **full QR factorisation** of $A$.

> [!warning] "QR factorisation" sometimes means the "full" form with $Q$ unitary.
> When $A$ is rectangular $m \times n$ with $m > n$, two conventions exist: the **economy QR** (or **thin QR**) with $Q$ being $m \times n$ isometric and $R$ being $n \times n$ upper-triangular; the **full QR** with $Q$ being $m \times m$ unitary and $R$ being $m \times n$ upper-triangular with zero rows below the $n$-th. We use the economy form; the full form is recovered by padding $Q$ with an orthonormal basis of $(\operatorname{range} A)^\perp$ and $R$ with zero rows.

---

# Motivation

QR factorisation is the **Gram–Schmidt orthogonalisation procedure read in matrix form**. Apply Gram–Schmidt to the columns of $A$ to produce an orthonormal list spanning the same column space; the orthogonalisation coefficients fill in an upper-triangular matrix $R$ such that $A = QR$.

The motivation is computational. Linear systems $Ax = b$ for invertible square $A$ can be solved in three ways: by direct inversion ($x = A^{-1} b$, requiring full inversion); by LU factorisation ($A = LU$, half the work but requires non-zero pivots); or by QR factorisation ($A = QR$, requiring orthogonalisation but **numerically stable**). The QR approach computes $x = R^{-1} Q^* b$, where $R^{-1}$ requires back-substitution on a triangular system (linear in $n^2$ operations once $R$ is known). The crucial advantage is that the condition number of $R$ equals the condition number of $A$ (since $\|Q\|_{\text{op}} = 1$), so no spurious ill-conditioning is introduced.

The QR factorisation also has theoretical applications: it constitutes a smooth parameterisation of the **Stiefel manifold** $V_n(\mathbb{F}^m)$ (the set of orthonormal $n$-frames in $\mathbb{F}^m$) as a quotient of $\operatorname{GL}_n(\mathbb{F})$. The map $A \mapsto Q$ (taking only the orthonormal part of QR) is a smooth retraction from $\operatorname{GL}_n$ onto its maximal compact subgroup (when $m = n$). This is the Iwasawa decomposition $\operatorname{GL}_n = U(n) \cdot N$ (with $N$ the upper-triangular matrices with positive diagonal) realised as QR.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A$ has linearly independent columns".

The first disguised source is **a list of vectors needing orthonormalisation**. Given vectors $a_1, \ldots, a_n \in \mathbb{F}^m$, applying Gram–Schmidt to them produces orthonormal $q_1, \ldots, q_n$. The matrix $Q$ with columns $q_j$ and $R$ with entries the Gram–Schmidt orthogonalisation coefficients gives $A = QR$. The Gram–Schmidt procedure and QR factorisation are two phrasings of the same algorithm.

The second disguised source is **a linear system $Ax = b$ where $A$ is full column rank**. QR gives the solution stably: $x = R^{-1} Q^* b$. *Example problem:* solve a system with $A$ a Vandermonde matrix (which is full rank but ill-conditioned); QR factorisation is the standard approach.

The third disguised source is **an overdetermined least-squares problem**. To find $x$ minimising $\|Ax - b\|$ when $A \in \mathbb{F}^{m \times n}$ with $m > n$, the least-squares solution is $x = R^{-1} Q^* b$ from QR. The reason is that $A^* A = R^* Q^* Q R = R^* R$, so the normal equations $A^* A x = A^* b$ become $R^* R x = R^* Q^* b$, which simplifies to $R x = Q^* b$ on $R$-invertibility (which holds since $A$ has full column rank, hence $R$ is invertible upper triangular).

**Targets (Output Amplification)**

The conclusion is the factorisation $A = QR$.

Combine with **the [[Thm - Cholesky Factorization|Cholesky decomposition]]**: $A^* A = R^* Q^* Q R = R^* R$ is the Cholesky factorisation of $A^* A$. The further result $E$: QR and Cholesky are related — Cholesky of $A^* A$ is the upper triangular factor $R$ of QR of $A$. Numerically, computing QR avoids forming $A^* A$, which would square the condition number.

Combine with **solving systems**: $Ax = b$ becomes $QR x = b$ becomes $R x = Q^* b$ (multiply by $Q^*$, using $Q^* Q = I$). Back-substitution then gives $x$.

Combine with **least squares**: minimise $\|Ax - b\|^2 = \|QR x - b\|^2 = \|R x - Q^* b\|^2 + \|(I - QQ^*) b\|^2$, where the second term is the residual in $(\operatorname{range} A)^\perp$, independent of $x$. So minimise $\|R x - Q^* b\|^2$ over $x$; for full column rank $A$, this is uniquely minimised at $R x = Q^* b$.

---

# Why Is It True

The proof is the [[Thm - Gram-Schmidt Procedure|Gram–Schmidt procedure]] read in matrix form.

**The one-liner mechanism: Gram–Schmidt applied to the columns $a_1, \ldots, a_n$ of $A$ produces orthonormal $q_1, \ldots, q_n$ with $a_k = \sum_{j \leq k} r_{jk} q_j$ for upper-triangular coefficients $r_{jk}$ — exactly $A = QR$ in matrix form.**

Gram–Schmidt processes the columns one at a time:
- $q_1 = a_1 / \|a_1\|$, so $a_1 = r_{11} q_1$ with $r_{11} = \|a_1\| > 0$.
- $\tilde q_2 = a_2 - \langle a_2, q_1 \rangle q_1$; then $q_2 = \tilde q_2 / \|\tilde q_2\|$; so $a_2 = r_{12} q_1 + r_{22} q_2$ with $r_{12} = \langle a_2, q_1 \rangle$ and $r_{22} = \|\tilde q_2\| > 0$.
- In general, $\tilde q_k = a_k - \sum_{j < k} \langle a_k, q_j \rangle q_j$; $q_k = \tilde q_k / \|\tilde q_k\|$; $a_k = \sum_{j \leq k} r_{jk} q_j$ with $r_{jk} = \langle a_k, q_j \rangle$ for $j < k$ and $r_{kk} = \|\tilde q_k\| > 0$.

The orthonormality of $\{q_j\}$ is by construction (Gram–Schmidt's output is orthonormal). The upper-triangularity of $R$ is because $a_k$ depends on $q_1, \ldots, q_k$ but not on $q_{k+1}, \ldots$. The positivity of the diagonal entries $r_{kk} = \|\tilde q_k\| > 0$ is because $\tilde q_k \neq 0$ (since $a_k$ is linearly independent of $a_1, \ldots, a_{k-1}$, equivalently of $q_1, \ldots, q_{k-1}$).

The matrix form: setting $Q = [q_1, \ldots, q_n]$ and $R = (r_{jk})$ upper-triangular, the relations $a_k = \sum_j r_{jk} q_j$ for each $k$ are exactly $A = QR$. Done.

**Uniqueness:** if $A = Q_1 R_1 = Q_2 R_2$ with both factorisations satisfying the conditions, then $Q_2^* Q_1 = R_2 R_1^{-1}$. The left side is an isometry (product of an isometry with the inverse of an isometry); the right side is upper-triangular (product of upper-triangular with the inverse of upper-triangular). An upper-triangular isometry is diagonal with unit-modulus diagonal entries. With the positive-diagonal constraint, this is the identity. So $Q_1 = Q_2$ and $R_1 = R_2$.

---

# What Makes This Hard

The non-obvious step is **the linear independence hypothesis**. If the columns of $A$ are not linearly independent, the Gram–Schmidt procedure produces a zero vector at some stage, and the procedure breaks down (or proceeds with a non-unique answer). The hypothesis is essential.

The second subtlety is **numerical stability**: classical Gram–Schmidt is numerically unstable in finite-precision arithmetic. The **modified Gram–Schmidt** (which subtracts the projection onto $q_j$ from the running vector $\tilde q_k$ before going on to $q_{j+1}$) is more stable; **Householder reflections** are the most stable algorithm in practice. The mathematical content of QR factorisation is the same regardless of which algorithm is used to compute it.

The third subtlety is the **positive-diagonal constraint**. Without it, $R$ is determined only up to multiplication of each row by a unit-modulus scalar, with the corresponding column of $Q$ multiplied by the inverse scalar. Fixing the diagonal entries to be positive real removes this gauge freedom and makes the factorisation unique.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Apply Gram–Schmidt to the columns of $A$. The orthonormalised vectors give $Q$; the orthogonalisation coefficients give $R$.

**Subgoal decomposition:**

1. **Gram–Schmidt produces $\{q_j\}$ orthonormal.** Standard.

2. **Express each column $a_k$ as a linear combination of $q_1, \ldots, q_k$.** Direct from the Gram–Schmidt formula.

3. **Read off $R$ as the matrix of coefficients.** Upper-triangular, with positive diagonal.

4. **Matrix form $A = QR$.** Trivial.

5. **Uniqueness via the upper-triangular-and-isometric is identity argument.**

---

# Formal Proof

> [!note]- Complete formal proof
>
> By the [[Thm - Gram-Schmidt Procedure|Gram–Schmidt procedure]] applied to the columns $a_1, \ldots, a_n$ of $A$, there are orthonormal vectors $q_1, \ldots, q_n$ with $\operatorname{span}(a_1, \ldots, a_k) = \operatorname{span}(q_1, \ldots, q_k)$ for each $k$. In particular, $a_k$ is a linear combination of $q_1, \ldots, q_k$:
> $$a_k = \sum_{j = 1}^{k} r_{jk} q_j, \quad \text{where } r_{jk} = \langle a_k, q_j \rangle \text{ for } j < k, \quad r_{kk} = \|a_k - \sum_{j < k} r_{jk} q_j\| > 0.$$
>
> The positivity $r_{kk} > 0$ comes from $a_k$ being linearly independent of $a_1, \ldots, a_{k-1}$ (so the residual $a_k - \sum_{j<k} r_{jk} q_j$ is non-zero, with positive norm).
>
> Let $Q = [q_1, \ldots, q_n] \in \mathbb{F}^{m \times n}$ — its columns are orthonormal, so $Q^* Q = I_n$, i.e., $Q$ is an isometry. Let $R = (r_{jk})_{j, k = 1}^{n} \in \mathbb{F}^{n \times n}$ with $r_{jk} = 0$ for $j > k$ — upper-triangular with positive real diagonal. Then $A = QR$ entry by entry.
>
> **Uniqueness.** Suppose $A = Q_1 R_1 = Q_2 R_2$ are two such factorisations. Then $Q_1 = Q_2 R_2 R_1^{-1}$. Set $M = R_2 R_1^{-1}$, an upper-triangular invertible matrix. Then $Q_1 = Q_2 M$, so $Q_1^* Q_1 = M^* Q_2^* Q_2 M = M^* M = I$ (using isometry of $Q_1$ and $Q_2$). So $M$ is an isometry. An upper-triangular isometry is diagonal: the first column of $M$ is $m_{11} e_1$, and isometry forces $|m_{11}| = 1$; then the second column is $m_{12} e_1 + m_{22} e_2$, and orthogonality to the first column forces $m_{12} = 0$, then $|m_{22}| = 1$; continue. The diagonal entries are unit-modulus scalars. The positive-diagonal constraint on $R_1$ and $R_2$ forces these diagonals to be positive real, hence equal to $1$. So $M = I$, i.e., $R_2 = R_1$ and $Q_2 = Q_1$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Numerical linear algebra — least squares regression.** Linear regression with $n$ predictors and $m > n$ observations is the overdetermined system $X \beta \approx y$, where $X \in \mathbb{F}^{m \times n}$ has linearly independent columns. The least-squares solution is $\hat \beta = R^{-1} Q^* y$ from the QR factorisation $X = QR$. This is the standard regression algorithm in R, MATLAB, Python's NumPy, and most statistical software — chosen for numerical stability over the algebraic formula $\hat \beta = (X^*X)^{-1} X^* y$ (which numerically computes $X^*X$, squaring the condition number).

2. **Eigenvalue computation — the QR algorithm.** The standard algorithm for computing eigenvalues of a square matrix $A$ iterates: factor $A_k = Q_k R_k$ (QR factorisation), then set $A_{k+1} = R_k Q_k$ (multiply factors in reverse order). The sequence $A_k$ converges (under mild conditions) to upper-triangular form, exhibiting the eigenvalues on the diagonal. The QR algorithm is the most widely used algorithm for computing eigenvalues of medium-sized matrices.

3. **Cryptography — lattice reduction.** The LLL algorithm (Lenstra–Lenstra–Lovász) reduces a lattice basis to one with short, nearly orthogonal vectors. The procedure is built on Gram–Schmidt orthogonalisation (the GSO matrix) plus integer-coefficient adjustments. QR factorisation is the continuous-coefficient analogue; LLL is its integer version, central to cryptanalysis of lattice-based cryptosystems.

4. **Quantum chemistry — Hartree–Fock computations.** The molecular orbital coefficients in a Hartree–Fock calculation are orthonormalised at each step, traditionally by Gram–Schmidt or Löwdin's symmetric orthogonalisation. QR factorisation of the overlap matrix is the natural framework. This is the basic computational primitive in computational chemistry.

---

# Bridges

- **[[Thm - Gram-Schmidt Procedure|Gram–Schmidt procedure]]** — QR factorisation *is* Gram–Schmidt in matrix form. The orthonormal vectors $q_j$ produced by Gram–Schmidt are the columns of $Q$; the orthogonalisation coefficients $\langle a_k, q_j \rangle$ are the entries of $R$.

- **[[Thm - Cholesky Factorization]]** — The relation $A^* A = R^* R$ from QR is the Cholesky factorisation of $A^* A$. So Cholesky of a positive operator $T$ can be computed by: find $T$ as $A^*A$ for some $A$, then QR of $A$ gives Cholesky factor $R$. The two factorisations are coupled: QR is for general full-column-rank matrices; Cholesky is for positive operators; their factors agree on $A^*A$.

- **Iwasawa decomposition (Lie theory)** — For $G = \operatorname{GL}_n(\mathbb{C})$, the Iwasawa decomposition is $G = KAN$ where $K = U(n)$, $A$ is the diagonal positive matrices, and $N$ is the unit-upper-triangular matrices. QR factorisation realises $A \cdot N$ as the upper-triangular matrices with positive diagonal, so $G = K \cdot (AN) = U(n) \cdot (\text{upper-triangular with positive diagonal})$.

- **Householder reflections and Givens rotations** — Alternative algorithms for computing QR. Householder reflections orthogonalise by reflecting through hyperplanes; Givens rotations orthogonalise by rotating in 2-planes. Both are numerically more stable than classical Gram–Schmidt and are the algorithms of choice in practice. The mathematical content of the QR factorisation is independent of the algorithm.

---

# Unlocked by This

> [!tip] The QR Algorithm for Eigenvalue Computation *(from Numerical Linear Algebra)*
> The **QR algorithm** computes eigenvalues by iterating: $A_0 = A$, then $A_k = Q_k R_k$, then $A_{k+1} = R_k Q_k = Q_k^* A_k Q_k$. The transformation from $A_k$ to $A_{k+1}$ is a unitary similarity transformation, so the eigenvalues are preserved at each step. Under mild conditions (real eigenvalues, generic spacings), $A_k$ converges to upper-triangular form, with eigenvalues on the diagonal. The convergence is sped up by **shifts**: $A_k - \mu_k I = Q_k R_k$, then $A_{k+1} = R_k Q_k + \mu_k I$, with $\mu_k$ chosen close to an eigenvalue (e.g., the bottom-right entry of $A_k$). The QR algorithm with appropriate shifts is the eigenvalue solver in LAPACK and is the engine of almost every numerical eigenvalue computation in practice.

> [!tip] Stiefel Manifold and Riemannian Optimization *(from Differential Geometry / Optimization)*
> The **Stiefel manifold** $V_n(\mathbb{F}^m) = \{Q \in \mathbb{F}^{m \times n} : Q^* Q = I_n\}$ is the space of orthonormal $n$-frames in $\mathbb{F}^m$, a smooth manifold of dimension $mn - n(n + 1)/2$. The QR factorisation gives a smooth retraction from $\mathbb{F}^{m \times n}_{\text{full rank}}$ to $V_n(\mathbb{F}^m)$: given a non-orthonormal frame, the QR step orthogonalises it. This retraction is the algorithmic engine of Riemannian optimisation on Stiefel manifolds, used in eigenvalue computation, independent component analysis, low-rank matrix completion, and tensor decomposition.

> [!tip] Modified Gram–Schmidt and Householder Reflections *(from Numerical Stability)*
> The classical Gram–Schmidt procedure, while mathematically correct, is **numerically unstable** in finite precision: small errors in early steps accumulate catastrophically. The **modified Gram–Schmidt** subtracts each projection one at a time (updating $\tilde q_k$ after computing each $r_{jk}$ instead of all at once), which has better error propagation. Better still are **Householder reflections** (an isometric reflection $H = I - 2 \frac{vv^*}{v^*v}$ for unit vector $v$): these orthogonalise by reflecting subspaces, are perfectly orthogonal in exact arithmetic, and have provably small error growth in floating-point. The QR factorisation via Householder reflections is the algorithm used in LAPACK and is the recommended way to compute QR in production.
