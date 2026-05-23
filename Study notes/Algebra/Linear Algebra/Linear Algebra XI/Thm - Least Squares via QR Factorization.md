---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
  - "Thm - QR Factorization"
tags: [algebra, linear-algebra, applied, optimization, numerical-methods]
---

# Notation

$A$ is an $m \times n$ matrix ($m \geq n$) with linearly independent columns. The *QR factorization* is $A = QR$, where $Q$ is $m \times n$ with orthonormal columns ($Q^T Q = I_n$) and $R$ is $n \times n$ upper triangular and invertible. The LS solution is $\hat{x}$.

---

# Statement

> **Theorem (Least Squares via [[Thm - QR Factorization|QR Factorization]]).** Let $A$ be an $m \times n$ matrix with linearly independent columns, factored as $A = QR$ (QR factorization), and let $b$ be an $m$-vector.
> 1. The [[Def - Pseudoinverse|pseudoinverse]] of $A$ is $A^\dagger = R^{-1} Q^T$.
> 2. The least squares solution is
> $$\hat{x} = R^{-1} Q^T b,$$
> computed by first forming $Q^T b$ (a matrix-vector product) and then solving the upper-triangular system $R \hat{x} = Q^T b$ by back-substitution.
> 3. The algorithm (called *least squares via QR factorization*) is summarized as:
> ```
>   1. Compute QR factorization A = QR.    (cost: 2mn² flops)
>   2. Compute Q^T b.                       (cost: 2mn flops)
>   3. Solve R x̂ = Q^T b by back-substitution.   (cost: n² flops)
> ```
> The total cost is $2 m n^2 + 2 m n + n^2 \approx 2 m n^2$ flops, dominated by the QR factorization step.
> 4. The numerical conditioning is governed by $\kappa(A)$ (not $\kappa(A^T A) = \kappa(A)^2$), making this method substantially more accurate than the normal-equation approach for ill-conditioned problems.

---

# Motivation

The QR-based LS method is the *practical workhorse* of every numerical linear algebra package. When MATLAB or NumPy computes `A \ b` (or `np.linalg.lstsq(A, b)`) for an overdetermined system, the underlying algorithm is QR factorization. The reason is the combination of:

(i) *Numerical stability* — QR uses orthogonal transformations, which preserve the 2-norm and do not amplify errors. The condition number of the linear system being solved is $\kappa(A)$ rather than $\kappa(A^T A) = \kappa(A)^2$, saving roughly half the digits in floating-point arithmetic.

(ii) *Computational efficiency* — the cost is $O(m n^2)$, the same order as the normal-equation method, but the constant is slightly worse (factor of 2 vs 1/3 for Cholesky). For typical problem sizes the QR cost is acceptable; the stability advantage usually outweighs the modest extra cost.

(iii) *Conceptual cleanliness* — the QR factorization explicitly orthogonalizes the columns of $A$ via Gram-Schmidt (or Householder reflections, the numerically stable version). The orthonormal basis $Q$ for $\mathrm{col}(A)$ is constructed, and the LS solution is the projection in this orthonormal coordinate system, which is just $Q^T b$.

The theorem unifies these strands: the QR factorization gives a clean pseudoinverse formula $A^\dagger = R^{-1} Q^T$, a stable algorithm, and a clear interpretation in terms of orthogonal projection.

The role of the theorem in the chapter is to *give the practical recipe* for solving LS problems. Every subsequent application (regularized LS, constrained LS, LQR, Kalman) ultimately runs this algorithm (or an extended version of it) on appropriate stacked matrices.

---

# Sources and Targets

**Sources (input broadening)**

The theorem assumes $A$ has linearly independent columns and a QR factorization $A = QR$. The non-obvious bridges:

*Source 1: Stacked matrices from multi-objective LS.* For a multi-objective LS problem, the stacked matrix $\tilde{A}$ has linearly independent columns under mild conditions (see [[Def - Multi-Objective Least Squares]]), so QR-based LS solves the stacked system. *Example*: Tikhonov LS solves the stacked system $\binom{A}{\sqrt{\lambda} I}$ via QR, even when $A$ alone has dependent columns.

*Source 2: $A$ after column scaling.* Multiplying $A$ by a diagonal matrix from the right doesn't change the column space, but can dramatically improve conditioning. Scaling each column to have unit norm gives a column-normalized $A$, and QR is then applied to the normalized matrix. *Example*: in polynomial fitting, column normalization can be the difference between numerical success and failure.

*Source 3: Sparse $A$.* When $A$ is sparse (most entries zero), specialized *sparse QR* algorithms (e.g., the *Givens-rotation* approach or *Householder with row pivoting*) preserve sparsity and run in time proportional to the number of nonzeros plus the fill-in. *Example*: in linear-algebraic problems arising from PDEs on grids, $A$ is highly sparse and sparse-QR is essential.

**Targets (output amplification)**

The theorem gives a numerically stable algorithm. The non-obvious uses:

*Target 1 (one-versus-rest classification).* When the design matrix $A$ is shared across many LS problems (with different right-hand sides $y^{(k)}$), the QR factorization is computed *once* and reused across all problems. The total cost is $2 m n^2 + K \cdot 2 m n$ for $K$ problems — almost the cost of one problem when $K$ is small. *Example use*: 10-way one-vs-rest classification on MNIST: one QR, 10 back-substitutions.

*Target 2 (regularization path).* The same $A$ is used across many $\lambda$ values in Tikhonov regularization. The Gram-caching trick applies, but a more elegant trick is the *SVD-based* solution path: factor $A = U \Sigma V^T$ once, then $\hat{x}(\lambda) = V \Sigma_\lambda^+ U^T b$ for each $\lambda$ with $\Sigma_\lambda^+ = \mathrm{diag}(\sigma_i / (\sigma_i^2 + \lambda))$. The cost per $\lambda$ is just an $O(mn)$ matrix-vector product. *Example use*: computing 100 points on the regularization path in $O(mn^2 + 100 mn) = O(mn^2)$ total — same cost as one LS solve.

*Target 3 (recursive updating).* When new rows are added to $A$, the QR factorization can be updated in $O(mn)$ flops per row, rather than recomputed from scratch. This *QR updating* algorithm is the basis of recursive LS and online regression. *Example use*: streaming regression where data arrives in real time.

---

# Why Is It True

**The mechanism in one sentence: $Q$'s orthonormality reduces the LS problem to a triangular solve, and the triangular system $R \hat{x} = Q^T b$ has the same condition number as $A$, not its square.**

The derivation has two essential pieces.

*The pseudoinverse formula.* From $A = QR$, compute
$$A^T A = (QR)^T (QR) = R^T Q^T Q R = R^T R$$
(using $Q^T Q = I$ from orthonormality). The pseudoinverse is then
$$A^\dagger = (A^T A)^{-1} A^T = (R^T R)^{-1} R^T Q^T = R^{-1} R^{-T} R^T Q^T = R^{-1} Q^T.$$
So $\hat{x} = A^\dagger b = R^{-1} Q^T b$, computed by first forming $Q^T b$ and then solving $R \hat{x} = Q^T b$.

*The conditioning improvement.* The QR factorization "isolates" the conditioning of $A$ in the triangular factor $R$: $\kappa(A) = \kappa(R)$. Solving $R \hat{x} = Q^T b$ by back-substitution has accuracy governed by $\kappa(R) = \kappa(A)$, whereas solving $(A^T A) \hat{x} = A^T b$ by Cholesky has accuracy governed by $\kappa(A^T A) = \kappa(A)^2$. The savings is roughly half the digits lost.

The deeper picture is that QR factorization is the *constructive* version of the orthogonal-projection geometry. The columns of $Q$ are an orthonormal basis for $\mathrm{col}(A)$; the columns of $A$ are expressed in this basis via $R$. The LS problem becomes: project $b$ onto the column space (which in the orthonormal basis is just $Q^T b$), then map back to the original $\theta$ coordinates (which uses the triangular $R$). The triangular structure of $R$ makes the second step trivial.

---

# What Makes This Hard

The hard step is *internalizing why $Q$'s orthonormality is the source of the conditioning advantage*. Students often see QR as just one of many factorizations and don't immediately see why it is *better* than Cholesky on the normal equations. The key is that orthogonal transformations preserve 2-norms exactly — so applying $Q^T$ to $b$ does not amplify errors. The Cholesky step, by contrast, operates on the *squared* matrix $A^T A$, where small errors get squared in the conditioning.

A secondary difficulty is computing the QR factorization itself. The classical Gram-Schmidt algorithm is *numerically unstable* (loss of orthogonality after many steps); the *modified Gram-Schmidt* is more stable but still imperfect; the *Householder reflections* approach is the gold standard for numerical stability but is harder to derive. Boyd treats this implementation detail lightly; numerical linear algebra textbooks (Trefethen-Bau, Golub-Van Loan) cover it carefully.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the QR factorization to expand the pseudoinverse formula and simplify via orthonormality. Establish the algorithm by extracting the computation steps. Justify the conditioning improvement via singular-value-decomposition relations.

**Subgoal decomposition:**

1. **Compute $A^T A$ in terms of QR.** Show that $A^T A = R^T R$.
   - *Hint:* $A^T A = (QR)^T(QR) = R^T Q^T Q R = R^T R$ since $Q^T Q = I$.
   - *Why needed:* Lets us simplify the pseudoinverse formula.

2. **Derive the pseudoinverse formula.** Show that $A^\dagger = R^{-1} Q^T$.
   - *Hint:* $A^\dagger = (A^T A)^{-1} A^T = (R^T R)^{-1} R^T Q^T = R^{-1} R^{-T} R^T Q^T = R^{-1} Q^T$.
   - *Why needed:* Gives the explicit formula for $\hat{x}$ in terms of QR.

3. **Identify the algorithm.** The LS solution $\hat{x} = R^{-1} Q^T b$ is computed by first forming $Q^T b$ (matrix-vector multiplication, $2 m n$ flops), then solving the triangular system $R \hat{x} = Q^T b$ by back-substitution ($n^2$ flops).
   - *Hint:* Total cost $2 m n^2$ (QR factorization) $+ 2 m n$ (matrix-vector multiply) $+ n^2$ (triangular solve) $\approx 2 m n^2$ flops.
   - *Why needed:* Verifies the complexity claim.

4. **Conditioning comparison.** Show $\kappa(A) = \kappa(R)$, and explain why this beats $\kappa(A^T A) = \kappa(A)^2$.
   - *Hint:* $A = QR$ with $Q$ orthonormal preserves singular values: $A$ and $R$ have the same singular values.
   - *Why needed:* Justifies the numerical-stability claim of the QR method over normal-equation method.

---

# Lemma Decomposition

> [!note]- Lemma 1: $A^T A = R^T R$ when $A = QR$ with $Q^T Q = I$.
> **Statement:** If $A = QR$ is a QR factorization with $Q^T Q = I_n$, then $A^T A = R^T R$.
>
> **Hint:** Direct computation. $A^T A = (QR)^T(QR) = R^T (Q^T Q) R = R^T R$.
>
> **Why needed:** Allows us to express the inverse Gram matrix in terms of $R$ alone, eliminating $Q$ from the formula.
>
> > [!note]- Full proof
> > $A^T A = (QR)^T (QR) = R^T Q^T Q R = R^T I_n R = R^T R$. The key step uses $Q^T Q = I_n$, the defining property of $Q$'s orthonormal columns.

> [!note]- Lemma 2: $(R^T R)^{-1} R^T = R^{-1}$.
> **Statement:** For invertible upper triangular $R$, $(R^T R)^{-1} R^T = R^{-1}$.
>
> **Hint:** Use associativity and the fact that $R^{-1}$ commutes through the inverse.
>
> **Why needed:** Simplifies the pseudoinverse formula from $A^\dagger = (A^T A)^{-1} A^T = (R^T R)^{-1} R^T Q^T$ to $R^{-1} Q^T$.
>
> > [!note]- Full proof
> > $(R^T R)^{-1} R^T = (R^T R)^{-1} R^T = R^{-1} (R^T)^{-1} R^T = R^{-1} I = R^{-1}$. We used $(R^T R)^{-1} = R^{-1} (R^T)^{-1}$ for invertible $R$.

> [!note]- Lemma 3: $A$ and $R$ have the same singular values when $A = QR$, $Q^T Q = I$.
> **Statement:** If $A = QR$ is a QR factorization with $Q^T Q = I$, then $A$ and $R$ have the same singular values, hence $\kappa(A) = \kappa(R)$.
>
> **Hint:** Use the SVD of $R$ and combine with the orthonormality of $Q$ to obtain an SVD of $A$.
>
> **Why needed:** Establishes that the conditioning of the LS algorithm via QR depends on $\kappa(A)$, not $\kappa(A)^2$.
>
> > [!note]- Full proof
> > Let $R = U_R \Sigma_R V_R^T$ be the SVD of $R$ (with $U_R, V_R$ orthonormal $n \times n$, $\Sigma_R$ diagonal $n \times n$). Then $A = QR = Q U_R \Sigma_R V_R^T = (Q U_R) \Sigma_R V_R^T$. The matrix $Q U_R$ is $m \times n$ with orthonormal columns (orthonormality is preserved by products of orthonormal matrices). So $A = (Q U_R) \Sigma_R V_R^T$ is an SVD of $A$, with singular values $\sigma_1, \ldots, \sigma_n$ given by the diagonal of $\Sigma_R$ — same as those of $R$. Hence $\kappa(A) = \kappa(R)$.

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 1: [[Def - Pseudoinverse|Pseudoinverse]] formula.* By Lemma 1, $A^T A = R^T R$. Then
> $$A^\dagger = (A^T A)^{-1} A^T = (R^T R)^{-1} (QR)^T = (R^T R)^{-1} R^T Q^T = R^{-1} Q^T$$
> using Lemma 2 in the last step.
>
> *Step 2: LS solution.* By definition, $\hat{x} = A^\dagger b = R^{-1} Q^T b$.
>
> *Step 3: Algorithm.* Compute $\hat{x}$ in three steps:
> - Compute the QR factorization $A = QR$ (cost: $2 m n^2$ flops via Householder reflections).
> - Compute $y = Q^T b$ (cost: $2 m n$ flops, matrix-vector multiplication).
> - Solve $R \hat{x} = y$ by back-substitution (cost: $n^2$ flops, upper-triangular solve).
>
> Total cost: $2 m n^2 + 2 m n + n^2 \approx 2 m n^2$ flops (dominant term when $m \gg n$ or $m \approx n$).
>
> *Step 4: Conditioning.* By Lemma 3, $\kappa(A) = \kappa(R)$, so the back-substitution step has accuracy governed by $\kappa(A) \cdot u$ (where $u$ is the machine epsilon). The Householder QR algorithm has accuracy similarly governed by $\kappa(A) \cdot u$. The overall LS-via-QR algorithm therefore loses about $\log_{10} \kappa(A)$ digits in double precision, compared to $2 \log_{10} \kappa(A)$ for the normal-equation approach.

---

# Cross-Field Exercise Suggestions

*Suggestion 1 (Linear Algebra — Sequential QR for streaming data):* When rows are added to $A$ one at a time, the QR factorization can be updated by Givens rotations in $O(mn)$ flops per new row. This gives an online algorithm for LS regression on streaming data. Apply this theorem as the offline batch baseline that the online algorithm matches.

*Suggestion 2 (Numerical analysis — Householder vs Gram-Schmidt):* The Gram-Schmidt and Householder algorithms both produce QR factorizations; Householder is numerically more stable. Compare the loss of orthogonality $\|Q^T Q - I\|$ for the two algorithms on an ill-conditioned matrix (e.g., the Hilbert matrix). Conclude that Householder is the right choice for ill-conditioned problems.

*Suggestion 3 (Statistics — least squares regression diagnostics):* The QR factorization gives an explicit formula for the *leverage* of each data point: $h_{ii} = \|Q_{i,:}\|^2$, where $Q_{i,:}$ is the $i$th row of $Q$. High-leverage points have outsized influence on the fit. Apply this theorem to derive the regression-diagnostic formulas (leverages, Cook's distance) in terms of the QR factorization.

---

# Bridges

- **[[Thm - QR Factorization]]** — The QR factorization theorem from LADR gives the existence of $A = QR$ for any $A$ with linearly independent columns. This LS-via-QR theorem applies that factorization to LS. The QR factorization is constructed by Gram-Schmidt orthogonalization (or Householder reflections, the numerically stable version).

- **[[Thm - Singular Value Decomposition]]** — The SVD gives an alternative factorization $A = U \Sigma V^T$. The SVD-based LS formula $\hat{x} = V \Sigma^+ U^T b$ is more expensive to compute than QR-based LS ($O(mn^2)$ vs $O(mn^2)$ for square $n$, but with worse constants for SVD), but handles rank-deficient cases gracefully. For full-column-rank $A$, the two methods give the same answer.

- **[[Thm - Gram-Schmidt Procedure]]** — Gram-Schmidt is the conceptual algorithm for computing the QR factorization, although the practical algorithm uses Householder reflections for stability. The Gram-Schmidt connection is the *intuitive* derivation: orthogonalize the columns of $A$ to get $Q$; the orthogonalization coefficients are the entries of $R$.

- **[[Thm - Least Squares via Normal Equations]]** — The normal-equation method is the theoretical alternative to QR. They give identical answers in exact arithmetic; QR is preferred in floating-point. The condition-number comparison ($\kappa(A^T A) = \kappa(A)^2$ vs $\kappa(R) = \kappa(A)$) is the precise statement of QR's advantage.

---

# Unlocked by This

> [!tip] Matrix Least Squares (Multiple Right-Hand Sides) *(from Numerical Linear Algebra)*
> When LS must be solved with the *same* $A$ and *many* right-hand sides $b_1, \ldots, b_K$, the QR factorization is computed once and reused. The total cost is $2 m n^2 + 2 K m n + K n^2$ flops, dominated by $2 m n^2$ when $K \ll n$. This is the basis of efficient multi-class one-vs-rest classification, vector auto-regression in time series, and matrix least squares problems generally.

> [!tip] Iterative Refinement *(from Numerical Linear Algebra)*
> After computing an LS solution $\hat{x}$ via QR, the residual $r = A\hat{x} - b$ should be small but is computed in floating-point and has some error. **Iterative refinement** computes a correction $\Delta x = A^\dagger r$ (using the same QR factorization) and updates $\hat{x} \leftarrow \hat{x} - \Delta x$. This typically gains 2-3 digits of accuracy beyond the original QR solve, at very low cost. The technique extends to constrained LS, regularized LS, and beyond.

> [!tip] Sparse QR Factorization *(from Sparse Numerical Linear Algebra)*
> When $A$ is sparse, computing the QR factorization with general dense methods is wasteful. **Sparse QR** algorithms (using Givens rotations or column-permuted Householder) preserve sparsity, with time and memory proportional to the number of nonzeros plus the *fill-in* (new nonzeros introduced during factorization). The fill-in depends on the *sparsity pattern* of $A$, controllable via column-ordering algorithms (AMD, COLAMD). This makes LS computationally tractable for very large sparse problems arising in PDEs, networks, and graph-Laplacian estimation.
