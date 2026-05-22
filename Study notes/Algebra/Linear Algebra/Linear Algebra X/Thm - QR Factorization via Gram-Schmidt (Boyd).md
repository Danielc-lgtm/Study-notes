---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Left and Right Inverse of a Matrix"
tags: [algebra, linear-algebra, applied, factorization]
---

# Notation

Throughout, $A \in \mathbb R^{n \times k}$ is a matrix with columns $a_1, \dots, a_k \in \mathbb R^n$. By assumption, the columns are linearly independent, which forces $n \geq k$. The QR factorization expresses $A = QR$ with $Q \in \mathbb R^{n \times k}$ having orthonormal columns ($Q^T Q = I_k$) and $R \in \mathbb R^{k \times k}$ upper triangular with positive diagonal entries. Throughout, $q_i$ denotes the $i$-th column of $Q$ and $\tilde q_i$ the unnormalised intermediate residual in the Gram-Schmidt algorithm.

---

# Statement

> **Theorem (QR factorization via Gram-Schmidt).** Let $A \in \mathbb R^{n \times k}$ have linearly independent columns $a_1, \dots, a_k$ (so $n \geq k$). Then $A$ admits a **QR factorization** $A = QR$ where:
> - $Q \in \mathbb R^{n \times k}$ has orthonormal columns: $Q^T Q = I_k$.
> - $R \in \mathbb R^{k \times k}$ is upper triangular with strictly positive diagonal entries.
> 
> The factorization is unique. The columns of $Q$ are obtained by applying the Gram-Schmidt orthogonalisation algorithm to $a_1, \dots, a_k$, the diagonal entries of $R$ are the norms of the residual vectors, and the off-diagonal entries are the projection coefficients: $R_{ii} = \|\tilde q_i\|$ and $R_{ij} = q_i^T a_j$ for $i < j$, with $R_{ij} = 0$ for $i > j$.

> **Corollary (square case).** When $A$ is square ($n = k$) with linearly independent columns, $Q$ is an *orthogonal* matrix ($Q^T Q = QQ^T = I_n$), and $A^{-1} = R^{-1} Q^T$.

The factorization is sometimes also called the **modified Gram-Schmidt** factorization or **classical Gram-Schmidt** depending on the precise numerical procedure used (Boyd uses classical Gram-Schmidt, but modified Gram-Schmidt produces the same $Q, R$ and is more numerically stable).

---

# Motivation

Why is QR factorization important? Three reasons.

**(i) It gives a canonical orthonormal basis for the column space of $A$.** The columns of $Q$ are an orthonormal basis of $\operatorname{span}\{a_1, \dots, a_k\}$, with the first $i$ columns of $Q$ spanning the same subspace as the first $i$ columns of $A$. This is what one needs whenever working with subspaces: projection onto the column space is $QQ^T$, the distance from a vector to the subspace is $\|b - QQ^T b\|$, and so on. QR is the *constructive* way to produce this orthonormal basis.

**(ii) It is the numerically standard algorithm for solving $Ax = b$.** When $A$ is square and invertible, $Ax = b$ becomes $QRx = b$, hence $Rx = Q^T b$. The right-hand side $Q^T b$ is computed in $O(nk)$ flops, and then $Rx = Q^T b$ is solved by back-substitution in $O(k^2)$ flops since $R$ is upper triangular. The total cost is dominated by the QR factorization itself ($O(nk^2)$ flops), and the algorithm is numerically more stable than computing $A^{-1}$ directly or using LU factorization.

**(iii) It is the foundation of least-squares.** For an over-determined system $Ax = b$ (with $n > k$ and $A$ full-rank), the least-squares solution $\hat x = A^\dagger b = (A^T A)^{-1} A^T b$ can be rewritten as $\hat x = R^{-1} Q^T b$ using the QR factorization. This is much more numerically stable than forming $A^T A$ explicitly (which has condition number squared of $A$) and is the standard algorithm in statistical software.

The existence-part of the theorem is constructive: the Gram-Schmidt algorithm explicitly produces $Q$ and $R$ from $A$. The uniqueness-part says these are essentially the only choices (given the sign convention $R_{ii} > 0$), so QR factorization is a *canonical* factorization, not one of many.

---

# Sources and Targets

**Sources (Input Broadening)**

**Source 1 — any tall full-column-rank matrix.** Boyd's hypothesis "linearly independent columns" is automatically satisfied when, for example, the columns of $A$ are sample data and the dimensions exceed the number of samples (or vice versa, depending on orientation). In statistics, this is the "no perfect multicollinearity" condition; in numerical linear algebra, it is the "full column rank" condition. The bridge from "applied modelling assumption" to "QR factorization applies" is automatic in well-designed experiments.

**Source 2 — a matrix obtained by stacking sample vectors.** Suppose you have $N$ feature vectors $x_1, \dots, x_N$ and want to fit a linear regression. The data matrix $A$ has these as columns, and the QR factorization of $A$ exposes the orthonormal basis of the feature space — useful for understanding which directions in feature space are "well-sampled" (large diagonal entries of $R$) and which are "barely sampled" (small diagonal entries). The bridge: a "well-conditioned" regression has well-balanced diagonal entries of $R$.

**Source 3 — a basis-extension problem.** Given $k$ linearly independent vectors in $\mathbb R^n$ and the task of finding $n - k$ additional vectors to complete them to a basis of $\mathbb R^n$, the QR factorization is the cleanest tool: compute the QR of the given vectors, then extend $Q$ to an orthogonal matrix by appending $n - k$ unit vectors orthogonal to the existing columns. The bridge: "complete to a basis" $\to$ "extend to an orthogonal matrix" $\to$ "apply QR".

**Targets (Output Amplification)**

**Target 1 — projection onto the column space.** Once $A = QR$ is computed, the projection of any vector $v$ onto $\operatorname{span}\{a_1, \dots, a_k\}$ is $QQ^T v$, and the residual $v - QQ^T v$ is the orthogonal complement. This decomposition is the foundation of least-squares: the least-squares solution makes the residual $b - A\hat x$ orthogonal to the column space, equivalent to $A^T(b - A\hat x) = 0$, which solves via the QR factorization to $\hat x = R^{-1} Q^T b$.

**Target 2 — efficient solution of $Ax = b$ and back-substitution.** With $A = QR$ in hand, $Ax = b \Leftrightarrow Rx = Q^T b$. The triangular system $Rx = Q^T b$ is solved by back-substitution: $x_k = (Q^T b)_k / R_{kk}$, then $x_{k-1} = ((Q^T b)_{k-1} - R_{k-1, k} x_k)/R_{k-1, k-1}$, and so on. This is the standard "solve $Ax = b$" routine in numerical libraries (LAPACK, etc.).

**Target 3 — least-squares without normal equations.** For an over-determined $Ax = b$, the normal equations $A^T A x = A^T b$ involve computing the Gram matrix $A^T A$, which has condition number $\kappa(A)^2$ — squaring the conditioning. The QR route, $\hat x = R^{-1} Q^T b$, avoids forming $A^T A$ and preserves $\kappa(A)$. This is one of the most important examples of using QR for numerical stability.

**Target 4 — eigenvalue computation via QR iteration.** The **QR algorithm** for eigenvalues — factor $A_0 = A$, then iterate $A_{k+1} = R_k Q_k$ where $A_k = Q_k R_k$ — produces a sequence of matrices converging (under appropriate conditions) to an upper-triangular matrix whose diagonal entries are the eigenvalues of $A$. This is the standard eigenvalue algorithm and the most important computational application of QR after least-squares.

---

# Why Is It True

**The mechanism in one bolded line: Gram-Schmidt orthogonalises the columns of $A$ one at a time, projecting each new column orthogonally onto the span of the previous ones and normalising the residual — the columns of $Q$ are the normalised residuals, the diagonal of $R$ records the residual norms, and the off-diagonal entries of $R$ record the projection coefficients.**

The Gram-Schmidt algorithm is the constructive engine of the theorem. Starting from $a_1$, the first orthonormal vector is $q_1 = a_1/\|a_1\|$, so $a_1 = \|a_1\| q_1 = R_{11} q_1$ with $R_{11} = \|a_1\|$. Now $a_1, q_1$ are linked by a single coefficient, and the rest is induction.

For $a_2$, we orthogonally project $a_2$ onto $\operatorname{span}\{q_1\}$ — the coefficient is $q_1^T a_2 = R_{12}$ — and subtract: the residual $\tilde q_2 = a_2 - R_{12} q_1$ is orthogonal to $q_1$. Then we normalise: $q_2 = \tilde q_2 / \|\tilde q_2\|$, with $R_{22} = \|\tilde q_2\|$. Now $a_2 = R_{12} q_1 + R_{22} q_2$, the second column of $A$ expressed as a linear combination of $q_1, q_2$ — exactly what an upper-triangular $R$ encodes.

Iterating: at step $i$, project $a_i$ onto $\operatorname{span}\{q_1, \dots, q_{i-1}\}$ — coefficients $R_{ji} = q_j^T a_i$ for $j < i$ — subtract, get $\tilde q_i = a_i - \sum_{j < i} R_{ji} q_j$, normalise $q_i = \tilde q_i/\|\tilde q_i\|$, and set $R_{ii} = \|\tilde q_i\|$. The result is $a_i = R_{1i} q_1 + \cdots + R_{ii} q_i$, an upper-triangular linear combination.

Why are the diagonal entries $R_{ii}$ positive? Because the columns $a_i$ are linearly *independent*. If $a_i$ were in $\operatorname{span}\{q_1, \dots, q_{i-1}\}$ — equivalently, in $\operatorname{span}\{a_1, \dots, a_{i-1}\}$ — then the residual $\tilde q_i$ would be zero, and $R_{ii} = 0$. Linear independence guarantees $\tilde q_i \neq 0$, hence $R_{ii} > 0$.

Why is the orthonormality $Q^T Q = I$? Because each $q_i$ is constructed to be orthogonal to all previous $q_j$ (by the projection-and-subtract step) and is normalised to have unit length.

Uniqueness: suppose $A = Q' R'$ is another QR factorization with the same constraints on $Q', R'$. Then $Q^T Q' R' = Q^T A = R$ (using $Q^T Q = I$), so $R' = (Q^T Q')^{-1} R$... working through the algebra (and using the fact that an upper-triangular matrix with positive diagonal that is also orthogonal must be the identity), one gets $Q = Q'$ and $R = R'$. The sign convention on the diagonal is what enforces uniqueness.

---

# What Makes This Hard

The Gram-Schmidt algorithm itself is straightforward, but two subtleties are easy to miss.

First, **the algorithm requires that the columns of $A$ be processed in order**, with each new column orthogonalised against all previous columns. Changing the order of columns changes the QR factorization (since $R$ records the projection onto previous columns, which depends on the order). The factorization is unique only after the order of columns is fixed.

Second, **classical Gram-Schmidt is numerically unstable** for nearly-linearly-dependent columns. In floating-point arithmetic, the computed $Q$ can have columns that are not exactly orthogonal due to cumulative roundoff errors. **Modified Gram-Schmidt** — which orthogonalises against previous columns one at a time and updates the remaining columns immediately — is mathematically equivalent but numerically more stable. Both produce the same $Q, R$ in exact arithmetic, but in floating point modified Gram-Schmidt is preferred. The theorem is about the *exact* factorization; the numerical implementation requires care.

A common error is to compute QR by forming $A^T A$ first and then trying to factor it. This computes the Gram matrix, which has condition number $\kappa(A)^2$ — squaring the conditioning. QR via Gram-Schmidt computes $Q, R$ directly from $A$ without going through $A^T A$, preserving the condition number $\kappa(A)$. This is the numerical-stability reason for QR's centrality in modern numerical linear algebra.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Construct $Q$ and $R$ inductively, column by column, using Gram-Schmidt orthogonalisation. At each step, the new column of $Q$ is a normalised residual after projection onto previous columns, and the new column of $R$ records the projection coefficients and the residual norm.

**Subgoal decomposition:**

1. **Base case: $i = 1$.** Set $R_{11} = \|a_1\|$, $q_1 = a_1/R_{11}$. Then $a_1 = R_{11} q_1$, $\|q_1\| = 1$. By linear independence of $a_1, \dots, a_k$, $a_1 \neq 0$, so $R_{11} > 0$.
   - *Hint:* Normalisation of a single nonzero vector.
   - *Why needed:* Initialises the induction.

2. **Inductive step: assume $q_1, \dots, q_{i-1}$ are orthonormal and $a_j = \sum_{l \leq j} R_{lj} q_l$ for $j < i$.** Define the projection coefficients $R_{li} = q_l^T a_i$ for $l < i$, then the residual $\tilde q_i = a_i - \sum_{l < i} R_{li} q_l$, then $R_{ii} = \|\tilde q_i\|$, then $q_i = \tilde q_i/R_{ii}$. Show $q_i \perp q_l$ for $l < i$, $\|q_i\| = 1$, and $a_i = \sum_{l \leq i} R_{li} q_l$.
   - *Hint:* $q_l^T \tilde q_i = q_l^T a_i - \sum_{m < i} R_{mi} q_l^T q_m = q_l^T a_i - R_{li} = 0$.
   - *Why needed:* Propagates the construction one step forward.

3. **Linear independence guarantees $R_{ii} > 0$.** Show that if $R_{ii} = 0$, then $a_i \in \operatorname{span}\{q_1, \dots, q_{i-1}\} = \operatorname{span}\{a_1, \dots, a_{i-1}\}$, contradicting linear independence.
   - *Hint:* $R_{ii} = 0 \Rightarrow \tilde q_i = 0 \Rightarrow a_i = \sum_{l < i} R_{li} q_l$, which is in the span of previous columns of $Q$ = span of previous columns of $A$.
   - *Why needed:* Ensures the algorithm does not divide by zero and that $R$ has positive diagonal.

4. **Termination: after $k$ steps, $Q, R$ are constructed.** $Q$ has $k$ orthonormal columns, $R$ is $k \times k$ upper triangular with positive diagonal, and the relation $a_j = \sum_{l \leq j} R_{lj} q_l$ for all $j$ is exactly $A = QR$.
   - *Hint:* Re-read the per-column relation as matrix multiplication.
   - *Why needed:* Concludes existence of the factorization.

5. **Uniqueness.** Suppose $A = QR = Q'R'$ are two factorisations with the stipulated constraints. Then $Q^T Q' R' = R$, so the columns of $Q'$ can be expressed via $Q$ and an upper-triangular sign-positive matrix. Working through, $Q = Q'$ and $R = R'$.
   - *Hint:* The key is that an upper-triangular orthogonal matrix with positive diagonal is the identity.
   - *Why needed:* Establishes the factorization is unique.

---

# Lemma Decomposition

> [!note]- Lemma 1: Orthogonal projection coefficient
> **Statement:** For orthonormal vectors $q_1, \dots, q_{i-1}$ and any vector $a_i$, the residual $\tilde q_i = a_i - \sum_{l < i}(q_l^T a_i) q_l$ is orthogonal to each $q_l$ for $l < i$.
>
> **Hint:** Compute $q_m^T \tilde q_i$ directly using orthonormality.
>
> **Why needed:** This is the key step of Gram-Schmidt: it produces vectors orthogonal to all previous orthonormal vectors.
>
> > [!note]- Full proof
> > For any $m < i$, compute
> > $$q_m^T \tilde q_i = q_m^T a_i - \sum_{l < i}(q_l^T a_i)(q_m^T q_l) = q_m^T a_i - (q_m^T a_i)(q_m^T q_m) = q_m^T a_i - q_m^T a_i = 0,$$
> > using $q_m^T q_l = 0$ for $l \neq m$ and $q_m^T q_m = 1$.

> [!note]- Lemma 2: Linear independence forces nonzero residual
> **Statement:** If $a_1, \dots, a_i$ are linearly independent and $q_1, \dots, q_{i-1}$ is an orthonormal basis of $\operatorname{span}\{a_1, \dots, a_{i-1}\}$, then the Gram-Schmidt residual $\tilde q_i = a_i - \sum_{l < i}(q_l^T a_i) q_l$ is nonzero.
>
> **Hint:** If $\tilde q_i = 0$, then $a_i \in \operatorname{span}\{q_1, \dots, q_{i-1}\} = \operatorname{span}\{a_1, \dots, a_{i-1}\}$, contradicting linear independence of $a_1, \dots, a_i$.
>
> **Why needed:** Ensures the algorithm does not divide by zero in normalising $q_i = \tilde q_i/\|\tilde q_i\|$.
>
> > [!note]- Full proof
> > By construction $\sum_{l < i}(q_l^T a_i) q_l \in \operatorname{span}\{q_1, \dots, q_{i-1}\}$. By the inductive hypothesis, $\operatorname{span}\{q_1, \dots, q_{i-1}\} = \operatorname{span}\{a_1, \dots, a_{i-1}\}$. So $\tilde q_i = a_i - (\text{linear combination of } a_1, \dots, a_{i-1})$. If $\tilde q_i = 0$, then $a_i$ is a linear combination of $a_1, \dots, a_{i-1}$, contradicting linear independence.

> [!note]- Lemma 3: Upper-triangular orthogonal with positive diagonal is identity
> **Statement:** Let $U$ be a $k \times k$ upper-triangular matrix that is orthogonal ($U^T U = I$) and has positive diagonal entries. Then $U = I$.
>
> **Hint:** Use orthonormality of the columns of $U$ and the upper-triangular constraint to argue inductively that each column is a standard unit vector.
>
> **Why needed:** This lemma is the crux of the uniqueness argument.
>
> > [!note]- Full proof
> > The first column of $U$ is $U_{:,1} = (U_{11}, 0, \dots, 0)^T$ (upper-triangular, so entries below $U_{11}$ are zero). Orthonormality requires $\|U_{:,1}\| = 1$, so $|U_{11}| = 1$; positivity gives $U_{11} = 1$. So $U_{:,1} = e_1$.
> >
> > By induction, assume $U_{:,1}, \dots, U_{:,m-1} = e_1, \dots, e_{m-1}$. Consider $U_{:,m}$. By upper-triangularity, $(U_{:,m})_l = 0$ for $l > m$. By orthogonality with $U_{:,l} = e_l$ for $l < m$: $0 = e_l^T U_{:,m} = (U_{:,m})_l$, so $(U_{:,m})_l = 0$ for $l < m$ too. So $U_{:,m} = (0, \dots, 0, U_{mm}, 0, \dots, 0)^T$. Unit-norm and positive diagonal give $U_{mm} = 1$, so $U_{:,m} = e_m$. By induction, $U = I$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $A \in \mathbb R^{n \times k}$ have linearly independent columns $a_1, \dots, a_k$. Then there exist unique $Q \in \mathbb R^{n \times k}$ with $Q^T Q = I$ and $R \in \mathbb R^{k \times k}$ upper triangular with positive diagonal such that $A = QR$.
>
> *Proof of existence.* We construct $Q, R$ column by column.
>
> **Step 0 (Linear independence guarantees the algorithm proceeds.)** At each step $i$, the residual $\tilde q_i$ will be shown to be nonzero (Lemma 2), so the normalisation $q_i = \tilde q_i / \|\tilde q_i\|$ is well-defined.
>
> **$i = 1$:** Set $R_{11} = \|a_1\|$, $q_1 = a_1/R_{11}$. Then $\|q_1\| = 1$, and $a_1 = R_{11} q_1$. By linear independence, $a_1 \neq 0$, so $R_{11} > 0$.
>
> **$i \geq 2$ (inductive step):** Assume $q_1, \dots, q_{i-1}$ are orthonormal, that $\operatorname{span}\{q_1, \dots, q_{i-1}\} = \operatorname{span}\{a_1, \dots, a_{i-1}\}$, and that the relation $a_j = \sum_{l \leq j} R_{lj} q_l$ has been established for $j < i$ (with the off-diagonal entries $R_{lj}$ as defined below).
>
> Define $R_{li} = q_l^T a_i$ for $l < i$, set $\tilde q_i = a_i - \sum_{l < i} R_{li} q_l$, $R_{ii} = \|\tilde q_i\|$, and $q_i = \tilde q_i / R_{ii}$.
>
> By Lemma 2, $\tilde q_i \neq 0$, so $R_{ii} > 0$ and $q_i$ is well-defined. By Lemma 1, $q_l^T q_i = 0$ for all $l < i$, so $q_1, \dots, q_i$ are orthogonal; by construction $\|q_i\| = 1$. The relation $a_i = R_{ii} q_i + \sum_{l < i} R_{li} q_l = \sum_{l \leq i} R_{li} q_l$ holds. The span statement extends: $\operatorname{span}\{q_1, \dots, q_i\} \subseteq \operatorname{span}\{a_1, \dots, a_i\}$ from the construction, and $a_i \in \operatorname{span}\{q_1, \dots, q_i\}$ from the relation, so by induction the spans coincide.
>
> Continuing inductively to $i = k$, we have orthonormal $q_1, \dots, q_k$ and upper-triangular $R$ with positive diagonal, satisfying $a_j = \sum_{l \leq j} R_{lj} q_l$ for all $j$. In matrix form, this is exactly $A = QR$.
>
> *Proof of uniqueness.* Suppose $A = QR = Q'R'$ are two factorisations with the stipulated constraints. Then $Q'^T A = Q'^T Q R = (Q'^T Q) R$. Also $Q'^T A = Q'^T Q' R' = R'$ (since $Q'^T Q' = I$). So $(Q'^T Q) R = R'$, equivalently $Q'^T Q = R' R^{-1}$.
>
> The right side $R' R^{-1}$ is upper triangular (product of upper triangulars), with diagonal $R'_{ii}/R_{ii}$. The left side $Q'^T Q$ is orthogonal: $(Q'^T Q)^T (Q'^T Q) = Q^T Q' Q'^T Q = Q^T Q = I$. So $R' R^{-1}$ is an upper-triangular orthogonal matrix with positive diagonal. By Lemma 3, $R' R^{-1} = I$, i.e., $R' = R$. And then $Q' = AR'^{-1} = AR^{-1} = Q$. So the factorization is unique.
>
> $\blacksquare$
>
> **Square case.** If $n = k$, then $Q$ has $n$ orthonormal columns in $\mathbb R^n$, so $Q$ is an orthogonal matrix and $QQ^T = I$. Then $A^{-1} = R^{-1} Q^T$.

---

# Cross-Field Exercise Suggestions

**Statistics — multiple linear regression.** The least-squares estimator for the regression model $y = X\beta + \varepsilon$ is $\hat\beta = (X^T X)^{-1} X^T y$, which via QR factorization of $X = QR$ becomes $\hat\beta = R^{-1} Q^T y$. This is the standard numerically-stable algorithm in statistical software (R's `lm`, Python's `statsmodels`). The QR-derived formula avoids forming $X^T X$, which would square the condition number.

**Numerical analysis — eigenvalue computation.** The **QR algorithm** for eigenvalues iterates $A_{k+1} = R_k Q_k$ where $A_k = Q_k R_k$ is the QR factorization. Under appropriate conditions (mainly that $A$ has distinct eigenvalues), the sequence $A_k$ converges to an upper-triangular matrix whose diagonal entries are the eigenvalues of $A$. This is the standard eigenvalue algorithm in modern numerical linear algebra packages.

**Geometry — orthogonalising frame in differential geometry.** For a moving frame on a manifold — a smoothly-varying basis at each point — the Gram-Schmidt process produces an orthonormal frame from any frame. This is the constructive way to convert a curvilinear coordinate basis into a Euclidean-orthonormal basis at each point, used in differential geometry and in finite-element methods on irregular meshes.

**Information retrieval — Gram-Schmidt in latent semantic indexing.** The columns of a term-document matrix are typically nearly-linearly-dependent (many documents on similar topics). QR factorization produces an orthonormal basis for the column space, revealing the "principal topics" — the directions in which the documents genuinely differ. This is the QR-based analogue of singular value decomposition for low-rank approximation.

---

# Bridges

- **The Moore–Penrose pseudoinverse** — for a tall full-rank $A = QR$, the pseudoinverse is $A^\dagger = R^{-1} Q^T$ (verifying: $A^\dagger A = R^{-1} Q^T QR = R^{-1} R = I$). So QR factorization is the *constructive* way to compute the pseudoinverse, and this is the formula used in least-squares applications. The link to [[Def - Left and Right Inverse of a Matrix|left/right inverses]] is direct: the QR-derived pseudoinverse is *the* canonical left inverse of $A$.

- **The classical Gram-Schmidt versus modified Gram-Schmidt versus Householder reflections** — three different algorithms producing the same QR factorization in exact arithmetic. Classical Gram-Schmidt is mathematically clean but numerically unstable. Modified Gram-Schmidt reorders the operations and is more stable. Householder reflections compute QR by applying a sequence of orthogonal reflections, are the most numerically stable, and are what production numerical libraries (LAPACK) use. The bridge: same mathematical result, different numerical algorithms.

- **Singular value decomposition (SVD)** — the SVD $A = U \Sigma V^T$ generalises the QR factorization, providing an orthonormal basis for *both* the column space and the row space, plus a diagonal matrix of singular values measuring the "stretching" amounts. QR is the SVD's simpler cousin: it gives an orthonormal basis for the column space and an upper-triangular matrix for the coordinate change. The SVD is more powerful (it handles rank deficiency and gives the spectral information directly) but more expensive to compute.

- **Cholesky factorization** — for a symmetric positive-definite matrix $S$, the Cholesky factorization $S = L L^T$ writes $S$ as the product of a lower-triangular matrix and its transpose. The connection to QR: if $A = QR$, then $A^T A = R^T Q^T Q R = R^T R$, so $A^T A$ has Cholesky factor $R^T$ (the lower-triangular transpose of $R$). So the Gram matrix's Cholesky factor is the QR factor's transpose; the two are essentially the same algorithm in disguise.

- **Orthonormalisation in functional analysis (Hilbert spaces)** — the Gram-Schmidt process generalises verbatim to any inner-product space, including infinite-dimensional Hilbert spaces of functions. Applied to $1, t, t^2, t^3, \dots$ on $[-1, 1]$ with the $L^2$ inner product, it produces the **Legendre polynomials**, an orthonormal basis for $L^2([-1, 1])$. Applied with weight functions, it produces the Chebyshev, Hermite, Laguerre, and Jacobi polynomials — the classical orthogonal polynomials. The bridge: QR factorization is the matrix-version of orthogonal-polynomial construction.

---

# Unlocked by This

> [!tip] Numerically Stable Least Squares *(from Numerical Linear Algebra)*
> The least-squares solution $\hat x = (A^T A)^{-1} A^T b$ can be computed in two ways: (a) form the normal equations and solve, or (b) use QR factorization and solve $R x = Q^T b$ by back-substitution. The QR route preserves the condition number $\kappa(A)$, while the normal-equations route degrades it to $\kappa(A)^2$. For ill-conditioned problems this difference is the difference between a usable algorithm and a numerically-singular one.

> [!tip] Sparse and Banded QR Factorization *(from Scientific Computing)*
> When $A$ is sparse (most entries zero), specialised algorithms produce $Q, R$ that are also sparse or banded, in time proportional to the number of nonzero entries rather than $O(nk^2)$. This is what enables QR-based algorithms to scale to enormous matrices (millions of rows) arising in finite-element computations, PDE solvers, and large-scale optimisation.

> [!tip] Krylov Subspace Methods (GMRES, conjugate gradient) *(from Iterative Methods)*
> When $A$ is large and dense (or sparse but huge), direct QR factorization is too expensive. **Krylov subspace methods** iteratively build an orthonormal basis of the subspace $\operatorname{span}\{b, Ab, A^2 b, \dots\}$ using a Gram-Schmidt-like process (Arnoldi for general $A$, Lanczos for symmetric $A$). This produces a small upper-Hessenberg matrix whose factorization gives an approximate solution to $Ax = b$. The GMRES and conjugate-gradient algorithms are built on this idea.
