---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Normal Equations"
  - "Thm - Existence and Uniqueness of Least Squares Solution"
tags: [algebra, linear-algebra, applied, optimization, numerical-methods]
---

# Notation

$A$ is an $m \times n$ matrix with linearly independent columns. The *Gram matrix* is $G = A^T A$, symmetric positive definite under the assumption. The right-hand side is $h = A^T b$. The *condition number* of a matrix $M$ is $\kappa(M) = \sigma_{\max}/\sigma_{\min}$ (ratio of largest to smallest singular value).

---

# Statement

> **Theorem (Least Squares via [[Def - Normal Equations|Normal Equations]]).** Let $A$ be an $m \times n$ matrix with linearly independent columns, and $b$ an $m$-vector.
> 1. The least squares solution $\hat{x}$ is uniquely determined by the *normal equations* $A^T A x = A^T b$.
> 2. The Gram matrix $G = A^T A$ is symmetric positive definite, so the system $Gx = h$ can be solved by *Cholesky factorization* in $\frac{1}{3} n^3 + mn^2$ flops (the $mn^2$ comes from forming $G$, the $\frac{1}{3} n^3$ from Cholesky).
> 3. The condition number satisfies $\kappa(A^T A) = \kappa(A)^2$, so the normal-equation approach *squares the condition number* relative to operating on $A$ directly.

---

# Motivation

The normal equations are the *theoretically clean* characterization of the LS solution: they capture the orthogonality principle ("residual is orthogonal to column space") as a linear-algebraic statement, and they reduce the LS optimization problem to a single $n \times n$ linear system with a nice (symmetric positive definite) coefficient matrix. The system is square, the matrix is invertible, and Cholesky factorization is fast — so the normal-equation method *looks* like the obvious algorithm.

Why does this theorem need to be stated? Because despite its apparent simplicity, the normal-equation method has a *numerical pathology*: it squares the condition number of $A$. If $\kappa(A) = 10^5$ (perfectly reasonable for a real-world design matrix), then $\kappa(A^T A) = 10^{10}$, and a double-precision Cholesky solve loses about 10 digits — half its accuracy. For ill-conditioned design matrices, the normal-equation method can produce garbage.

The theorem records this fact carefully: the normal equations are *correct in exact arithmetic* but *fragile in floating-point arithmetic* for ill-conditioned $A$. The standard practical recommendation is to *not* use the normal equations for LS — use QR factorization instead (see [[Thm - Least Squares via QR Factorization]]). But the normal equations remain *theoretically* the cleanest derivation, and they have practical use when $A$ is sparse and well-conditioned (the resulting $A^T A$ can be even sparser and faster to factor than a sparse QR).

The role of this theorem is to formalize when the normal-equation approach is valid (linear independence of $A$'s columns) and to warn about its numerical limitations.

---

# Sources and Targets

**Sources (input broadening)**

The theorem assumes $A$ has linearly independent columns. The non-obvious bridges to this assumption from other situations:

*Source 1: $A$ is the design matrix of a regularized LS problem.* For Tikhonov $\min \|Ax - b\|^2 + \lambda \|x\|^2$, the stacked design matrix $\binom{A}{\sqrt{\lambda} I}$ has linearly independent columns for any $\lambda > 0$, *even if $A$ alone has linearly dependent columns*. So the normal-equation form $(A^T A + \lambda I) x = A^T b$ is always solvable. The regularization parameter $\lambda$ acts as a numerical stabilizer.

*Source 2: $A$ is the QR-orthogonalized design.* If $A = QR$ is the QR factorization, then $R$ has linearly independent columns (it is upper triangular and invertible), and the normal equations on $R$ have an even nicer form: $R^T R x = R^T Q^T b$, or equivalently $R x = Q^T b$ (since $R^T$ is invertible). This is exactly the QR-based LS method.

*Source 3: $A$ is well-conditioned (small $\kappa(A)$).* In this case, $\kappa(A^T A) = \kappa(A)^2$ remains manageable, and the normal-equation method is safe in floating-point. For example, in Boyd's recursive least squares with random projections (exercise 12.16), the projected $A$ is often well-conditioned and the Gram method becomes competitive.

**Targets (output amplification)**

The theorem gives: the LS solution as the solution of a square $n \times n$ linear system with a positive definite coefficient matrix. The non-obvious uses:

*Target 1 (recursive LS — combining the Gram matrix).* If new data $(a_{m+1}, b_{m+1})$ becomes available, the new Gram matrix $A^T A + a_{m+1} a_{m+1}^T$ can be updated by a rank-1 outer product. The new right-hand side $A^T b + b_{m+1} a_{m+1}$ updates similarly. This is the basis of *recursive least squares* (RLS) algorithms used in adaptive filtering and online learning. *Example use*: training a regression model on streaming data, updating it as each new sample arrives.

*Target 2 (combining LS subproblems).* In a multi-objective LS problem, the Gram matrices and right-hand sides combine linearly: $G = \sum \lambda_i G_i$, $h = \sum \lambda_i h_i$. This makes the Gram-caching algorithm of Boyd §15.5.1 very efficient: compute each $G_i, h_i$ once, then assemble different weighted sums for different $\lambda$ values. *Example use*: regularization-path computation across many $\lambda$ values.

*Target 3 (kernel trick).* The normal equations involve $A^T A$, an $n \times n$ matrix. When $n$ is huge (e.g., infinite-dimensional kernel features), this is impossible to form explicitly. The kernel trick exploits the matrix identity $A^T A + \lambda I)^{-1} A^T = A^T (A A^T + \lambda I)^{-1}$, which moves the inverse to an $m \times m$ matrix — manageable when the number of data points $m$ is small. *Example use*: kernel ridge regression with infinite-dimensional feature maps (Gaussian, polynomial kernels).

---

# Why Is It True

**The mechanism in one sentence: $\hat{x}$ minimizes $\|Ax - b\|^2$ iff its residual is orthogonal to all columns of $A$, which is the equation $A^T(A\hat{x} - b) = 0$ — the normal equations.**

The full intuition is the orthogonality principle from §XI.1. The closest point in $\mathrm{col}(A)$ to $b$ is the orthogonal projection of $b$ onto $\mathrm{col}(A)$. The vector from this projection to $b$ — the residual — must be orthogonal to $\mathrm{col}(A)$, hence orthogonal to every column of $A$. Algebraically, "$r$ orthogonal to column $a_j$" means $a_j^T r = 0$, and stacking these for $j = 1, \ldots, n$ gives $A^T r = 0$, i.e., $A^T(A\hat{x} - b) = 0$ — the normal equations.

The squaring of the condition number is also intuitive: $A^T A$ amplifies the *largest* direction by $\sigma_{\max}^2$ and the *smallest* direction by $\sigma_{\min}^2$, so the ratio (condition number) is squared. In floating point, the relative error of solving $Gx = h$ is bounded by $\kappa(G) \cdot$ machine epsilon, so squaring $\kappa(A)$ doubles the digits lost.

---

# What Makes This Hard

The main difficulty is *appreciating the numerical pathology*. In exact arithmetic, the normal equations work perfectly. In floating-point, they can fail catastrophically. Students often write down the normal-equation formula $\hat{x} = (A^T A)^{-1} A^T b$ as if it were the standard algorithm; they need to learn that it is the *cleanest derivation* but the *worst practical algorithm* for ill-conditioned problems. The QR-based method (next theorem) is what you actually use.

A secondary difficulty is the orthogonality principle. Even though it is "intuitive" — projections give closest points, residuals are orthogonal — connecting this geometric intuition to the algebraic equation $A^T r = 0$ requires identifying "orthogonal to the column space" with "orthogonal to all columns" with "$A^T r = 0$." Each step is a logical equivalence, but the chain is non-trivial.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the orthogonality principle to derive the normal equations directly. Verify invertibility of $A^T A$ under the linear-independence assumption. Compute the condition-number squaring as a consequence of singular-value relations between $A$ and $A^T A$.

**Subgoal decomposition:**

1. **Derive the normal equations.** Use the orthogonality principle.
   - *Hint:* "$\hat{x}$ minimizes $\|Ax - b\|^2$" iff "$A\hat{x} - b \perp \mathrm{col}(A)$" iff "$A^T(A\hat{x} - b) = 0$."
   - *Why needed:* Establishes the equivalence between the LS optimization and the linear system.

2. **Invertibility of $A^T A$.** Show that linear independence of columns implies $A^T A$ invertible.
   - *Hint:* $v^T A^T A v = \|Av\|^2$; this is zero iff $Av = 0$. Use to identify kernels.
   - *Why needed:* Guarantees the normal equations have a unique solution.

3. **Cholesky factorization complexity.** Counting flops.
   - *Hint:* Forming $A^T A$ is $mn^2$ flops (with the symmetry trick — only the upper triangle); Cholesky on the $n \times n$ matrix is $\frac{1}{3} n^3$.
   - *Why needed:* Establishes the complexity claim.

4. **Condition-number squaring.** Relate $\kappa(A)$ and $\kappa(A^T A)$.
   - *Hint:* Use the SVD $A = U \Sigma V^T$ to compute $A^T A = V \Sigma^2 V^T$. The singular values of $A^T A$ are $\sigma_i^2$, so $\kappa(A^T A) = (\sigma_{\max}/\sigma_{\min})^2 = \kappa(A)^2$.
   - *Why needed:* Quantifies the numerical pathology.

---

# Lemma Decomposition

> [!note]- Lemma 1: The orthogonality principle implies the normal equations.
> **Statement:** $\hat{x}$ minimizes $\|Ax - b\|^2$ iff $A^T(A\hat{x} - b) = 0$.
>
> **Hint:** Use the orthogonal-decomposition lemma: $b = b_\parallel + b_\perp$ with $b_\parallel \in \mathrm{col}(A)$ and $b_\perp \in \mathrm{col}(A)^\perp$.
>
> **Why needed:** This is the heart of the normal-equation derivation. The orthogonality principle is the geometric statement; the normal equations are its algebraic restatement.
>
> > [!note]- Full proof
> > $(\Rightarrow)$ Suppose $\hat{x}$ minimizes $\|Ax - b\|^2$. For any direction $d \in \mathbb{R}^n$ and any $\epsilon \in \mathbb{R}$, the function $g(\epsilon) = \|A(\hat{x} + \epsilon d) - b\|^2$ has minimum at $\epsilon = 0$. Computing: $g(\epsilon) = g(0) + 2 \epsilon \cdot (A d)^T(A \hat{x} - b) + \epsilon^2 \|Ad\|^2$. The linear term in $\epsilon$ must vanish at the minimum: $(Ad)^T(A\hat{x} - b) = d^T A^T(A\hat{x} - b) = 0$ for all $d$. So $A^T(A\hat{x} - b) = 0$.
> >
> > $(\Leftarrow)$ Suppose $A^T(A\hat{x} - b) = 0$. For any $x \in \mathbb{R}^n$, write $\|Ax - b\|^2 = \|A(x - \hat{x}) + (A\hat{x} - b)\|^2 = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2 + 2 (A(x - \hat{x}))^T(A\hat{x} - b) = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2 + 2 (x - \hat{x})^T A^T(A\hat{x} - b) = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2$, where the cross-term vanished by hypothesis. Since $\|A(x - \hat{x})\|^2 \geq 0$, we have $\|Ax - b\|^2 \geq \|A\hat{x} - b\|^2$, so $\hat{x}$ is a minimizer.

> [!note]- Lemma 2: Cholesky factorization of a positive definite matrix.
> **Statement:** A symmetric positive definite $n \times n$ matrix $G$ admits a factorization $G = L L^T$, where $L$ is lower triangular with positive diagonal entries. The factorization is unique, costs $\frac{1}{3} n^3$ flops, and solving $Gx = h$ via $L L^T x = h$ takes $2 n^2$ flops.
>
> **Hint:** Construct $L$ column by column using the recursive formula $L_{jj} = \sqrt{G_{jj} - \sum_{k < j} L_{jk}^2}$, $L_{ij} = (G_{ij} - \sum_{k < j} L_{ik} L_{jk})/L_{jj}$ for $i > j$.
>
> **Why needed:** Cholesky is the standard algorithm for solving the normal equations; this lemma establishes its existence and complexity.
>
> > [!note]- Full proof
> > The construction proceeds column by column. Assuming the first $j - 1$ columns of $L$ are constructed correctly, the diagonal entry of the $j$th column of $G$ is $G_{jj} = \sum_{k \leq j} L_{jk}^2$, so $L_{jj} = \sqrt{G_{jj} - \sum_{k < j} L_{jk}^2}$. This square root is real (positive) because the principal $j \times j$ submatrix of $G$ is positive definite (by the positive-definiteness of $G$ itself). The off-diagonal entries for $i > j$ in column $j$ of $L$ are given by $G_{ij} = \sum_{k \leq j} L_{ik} L_{jk}$, so $L_{ij} = (G_{ij} - \sum_{k < j} L_{ik} L_{jk})/L_{jj}$. The cost is $n^3/3$ flops (counting only nontrivial work). Solving $Gx = h$ then reduces to two triangular solves: $L y = h$ by forward substitution, then $L^T x = y$ by back substitution, each costing $n^2$ flops.

> [!note]- Lemma 3: Singular values of $A^T A$ are the squares of singular values of $A$.
> **Statement:** Let $A = U \Sigma V^T$ be the singular value decomposition of $A$. Then $A^T A = V \Sigma^2 V^T$, and the singular values of $A^T A$ are $\sigma_1^2 \geq \cdots \geq \sigma_n^2$, where $\sigma_i$ are the singular values of $A$.
>
> **Hint:** Direct computation. $A^T A = (U \Sigma V^T)^T (U \Sigma V^T) = V \Sigma^T U^T U \Sigma V^T = V \Sigma^T \Sigma V^T = V \Sigma^2 V^T$.
>
> **Why needed:** Identifies the singular values of the Gram matrix in terms of those of $A$, which gives the condition number squaring.
>
> > [!note]- Full proof
> > For the SVD $A = U \Sigma V^T$ with $U$ orthonormal ($m \times n$), $\Sigma$ diagonal ($n \times n$ with $\sigma_1 \geq \cdots \geq \sigma_n \geq 0$), and $V$ orthonormal ($n \times n$), compute $A^T A = V \Sigma^T U^T U \Sigma V^T = V \Sigma^2 V^T$ (since $U^T U = I$). This is the SVD of $A^T A$ (modulo possible sign changes), with singular values $\sigma_i^2$. Hence $\kappa(A^T A) = \sigma_1^2/\sigma_n^2 = (\sigma_1/\sigma_n)^2 = \kappa(A)^2$.

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 1: Derive the normal equations.* By Lemma 1, $\hat{x}$ minimizes $\|Ax - b\|^2$ iff $A^T(A\hat{x} - b) = 0$, i.e., $A^T A \hat{x} = A^T b$.
>
> *Step 2: Invertibility of $A^T A$.* Under the linear-independence assumption, $A^T A$ is positive definite by the argument in [[Thm - Existence and Uniqueness of Least Squares Solution]] (Lemma 2 of that theorem). So $A^T A$ is invertible and the normal equations have a unique solution.
>
> *Step 3: Cholesky algorithm and complexity.* By Lemma 2, $G = A^T A$ admits a Cholesky factorization $G = L L^T$, and solving $G \hat{x} = h$ via $L L^T \hat{x} = h$ takes $\frac{1}{3} n^3 + 2 n^2$ flops. Forming the Gram matrix $G = A^T A$ requires $m n^2$ flops (taking advantage of symmetry). Forming $h = A^T b$ takes $2 m n$ flops. The total is $m n^2 + \frac{1}{3} n^3 + O(\max(mn, n^2))$ flops, dominated by $m n^2$ when $m \gg n$ (the typical tall-design-matrix case) or by $\frac{1}{3} n^3$ when $m \approx n$.
>
> *Step 4: Condition-number squaring.* By Lemma 3, the singular values of $A^T A$ are the squares of those of $A$, so $\kappa(A^T A) = \kappa(A)^2$. In floating-point arithmetic, the relative error in solving $Gx = h$ via Cholesky scales as $\kappa(G) \cdot u$, where $u$ is the machine epsilon (about $10^{-16}$ in double precision). So the normal-equation method loses about $2 \log_{10} \kappa(A)$ digits, whereas the QR-based method (next theorem) loses only $\log_{10} \kappa(A)$. For $\kappa(A) = 10^5$, the normal-equation method gives 6 correct digits, the QR method gives 11.

---

# Cross-Field Exercise Suggestions

*Suggestion 1 (Statistics — OLS):* The normal equations $X^T X \hat{\beta} = X^T y$ are the standard formula for OLS regression coefficients in statistics. Apply this theorem to verify when OLS is well-defined (full column rank of $X$) and to compute the standard error of the regression coefficients via the formula $\mathrm{Cov}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$.

*Suggestion 2 (PDEs — Galerkin finite elements):* The Galerkin formulation of a self-adjoint elliptic PDE gives normal equations on a finite-element [[Def - Subspace|subspace]]. Apply this theorem to show that the FE solution exists and is unique (under positivity / coercivity of the bilinear form), and to interpret the FE conditioning issues as condition-number-squared phenomena.

*Suggestion 3 (Numerical analysis — recursive least squares):* When new data arrives sequentially, the Gram matrix updates by a rank-1 outer product, and the LS solution can be updated in $O(n^2)$ flops per new sample (rather than recomputing from scratch in $O(mn^2)$). This is the *recursive least squares* (RLS) algorithm. Use this theorem as the offline batch version that the recursive algorithm incrementally builds.

---

# Bridges

- **[[Thm - Least Squares via QR Factorization]]** — The QR-based LS method is the practical alternative to the normal-equation method. They give the same answer in exact arithmetic, but QR has half the condition number cost. The conceptual relationship: QR explicitly orthogonalizes the columns of $A$, computing $Q^T b$ directly instead of forming the explicit Gram matrix.

- **[[Thm - Singular Value Decomposition]]** — The SVD gives the relation $\kappa(A^T A) = \kappa(A)^2$ via singular-value identities. The SVD-based pseudoinverse $A^+ = V \Sigma^+ U^T$ is the general LS solver, working for both full-rank and rank-deficient $A$.

- **Recursive Least Squares (RLS)** — Updating the Gram matrix by rank-1 outer products allows online learning with $O(n^2)$ updates per new sample. The Sherman-Morrison-Woodbury formula gives the inverse-update form $(A + uv^T)^{-1} = A^{-1} - A^{-1} u (1 + v^T A^{-1} u)^{-1} v^T A^{-1}$, allowing the LS solution to be updated without recomputing the inverse from scratch. RLS is the basis of adaptive filtering and online regression.

- **[[Def - Pseudoinverse]]** — The expression $(A^T A)^{-1} A^T$ is the *left pseudoinverse* of $A$ when its columns are linearly independent. For wide $A$ (linearly independent rows), the right pseudoinverse is $A^T (A A^T)^{-1}$. The unified SVD-based pseudoinverse handles both cases.

---

# Unlocked by This

> [!tip] Kernel Ridge Regression *(from Machine Learning)*
> The normal equations for Tikhonov $(A^T A + \lambda I) x = A^T b$ become problematic when $n$ is very large (or infinite, via kernel methods). The **kernel trick** uses the identity $(A^T A + \lambda I)^{-1} A^T = A^T (A A^T + \lambda I)^{-1}$ to switch from the $n \times n$ Gram matrix to the $m \times m$ kernel matrix. With $K = A A^T$ becoming the Gram matrix of the data points in feature space, kernel ridge regression solves $(K + \lambda I) \alpha = b$ and predicts via $\hat{f}(x_{\text{new}}) = \alpha^T K(x_{\text{new}}, \cdot)$. This is the LS-based form of Gaussian process regression.

> [!tip] Statistical Inference via the Inverse Gram Matrix *(from Statistics)*
> The covariance matrix of the OLS estimator is $\mathrm{Cov}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$. The diagonal entries give the variance of each regression coefficient; the off-diagonals give the covariance between coefficients. From this matrix, one constructs the *standard errors*, *t-statistics*, *confidence intervals*, and *Wald tests* of statistical inference. The entire frequentist regression theory is built on the inverse Gram matrix that the normal-equation approach computes.
