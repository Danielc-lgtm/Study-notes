---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
  - "Def - Normal Equations"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

$A$ is an $m \times n$ matrix, $b$ is an $m$-vector. The Gram matrix $A^T A$ is $n \times n$, symmetric positive semidefinite. The columns of $A$ are *linearly independent* iff $A^T A$ is positive definite (equivalently, invertible). The LS solution is denoted $\hat{x}$.

---

# Statement

> **Theorem (Existence and Uniqueness of Least Squares Solution).** Let $A$ be an $m \times n$ matrix and $b$ an $m$-vector.
> 1. *Existence*: The least squares problem $\min_x \|Ax - b\|^2$ always has at least one minimizer.
> 2. *Uniqueness*: The minimizer is unique if and only if the columns of $A$ are linearly independent.
> 3. *Closed form (full column rank case)*: If the columns of $A$ are linearly independent, the unique minimizer is
> $$\hat{x} = (A^T A)^{-1} A^T b.$$

> **Corollary (Minimum-norm LS solution).** Without the linear-independence assumption, the set of LS minimizers is an affine subspace of $\mathbb{R}^n$ (a coset of $\ker A$); the unique element of this set with minimum Euclidean norm is $\hat{x}^+ = A^+ b$, where $A^+$ is the [[Def - Pseudoinverse|pseudoinverse]] of $A$ defined via [[Thm - Singular Value Decomposition|SVD]].

---

# Motivation

This theorem is the foundation of every subsequent result in the chapter. Without it, we have a problem with no guaranteed answer, an uncertain algorithm, no explicit formula. With it, we have: a closed-form solution under a mild and easily-checked assumption, a clear understanding of what happens when the assumption fails, and the recipe that QR factorization and SVD will compute reliably.

The role of the theorem is to *certify* that the LS problem is well-posed: that the optimization has a well-defined answer, and to *identify* that answer with an explicit linear-algebraic formula. The geometric content — orthogonal projection — was clear from the start, but this theorem makes it computable. The formula $\hat{x} = (A^T A)^{-1} A^T b$ is the recipe for projecting and inverting.

The existence claim (1) deserves emphasis: minimization of a non-negative quadratic always has a minimum (the objective is bounded below by zero and is continuous, and the lower bound is attained — though showing attainment in unbounded domains requires a bit of work). What is non-trivial is *uniqueness*: even though the objective is convex, it need not be *strictly* convex, and convex (but not strictly convex) functions can have flat minima — affine subspaces of minimizers. The strictness of convexity is what makes the minimizer unique, and that strictness is exactly what linear independence of columns provides.

---

# Sources and Targets

**Sources (input broadening)**

The theorem requires: $A$ is an $m \times n$ matrix, $b$ is an $m$-vector, the columns of $A$ are linearly independent. The third condition is the non-trivial one; here are non-obvious situations where it holds.

*Source 1: $A$ comes from a Vandermonde construction with distinct nodes.* If $A_{ij} = (x_i)^{j-1}$ for distinct $x_1, \ldots, x_m$ (with $m \geq n$), then $A$ has linearly independent columns. The Vandermonde determinant is $\prod_{i < j}(x_j - x_i)$, which is nonzero when the nodes are distinct, ensuring full column rank. *Example problem*: polynomial fitting of degree $n - 1$ to $m \geq n$ data points at distinct $x$-values — the LS theorem guarantees a unique fit.

*Source 2: $A$ comes from one-hot encoding of a categorical with an intercept dropped.* If the columns of $A$ encode a categorical variable with $K$ levels, plus an intercept, the linear dependence between the intercept and the sum-of-categorical-indicators forces us to drop one level. The remaining columns are linearly independent; the LS theorem then ensures a unique fit. *Example problem*: house-price prediction using categorical ZIP-code-cluster encoding — drop one level (chosen as the default cluster), and LS works.

*Source 3: $A$ is the row-stacked design matrix of a multi-objective LS problem.* For multi-objective LS $\sum_i \lambda_i \|A_i x - b_i\|^2$, the stacked matrix $\tilde{A} = (\sqrt{\lambda_i} A_i)_{i=1}^k$ has linearly independent columns iff no nonzero $x$ satisfies $A_i x = 0$ for all $i$. This is *weaker* than each $A_i$ having independent columns: different objectives can constrain different directions. *Example problem*: regularized LS where the original $A$ is rank-deficient but $\tilde{A} = (A^T, \sqrt{\lambda} I)^T$ has independent columns by virtue of $\sqrt{\lambda} I$ — this is why regularization always produces a unique solution.

*Source 4: $A$ comes from a smooth basis evaluated on distinct points, even if non-polynomial.* The Gram matrix $A^T A$ is closely related to *positive-definiteness of the kernel* $K(x, x') = \sum_j f_j(x) f_j(x')$. For many natural bases (Gaussians, sinusoids, ReLU random features), $K$ is positive definite on any set of distinct inputs, so $A^T A$ is positive definite. *Example problem*: kernel ridge regression with a positive-definite kernel — LS always has a unique solution by the theorem.

**Targets (output amplification)**

The theorem gives: the LS minimizer exists and (under the assumption) is the linear function $\hat{x} = (A^T A)^{-1} A^T b$ of $b$. Here are non-obvious uses of this conclusion.

*Target 1 (linear-in-$b$ property → precomputed solvers).* Because $\hat{x}$ is a linear function of $b$ via the matrix $A^\dagger = (A^T A)^{-1} A^T$, we can *precompute* $A^\dagger$ (or, more efficiently, the QR factorization of $A$) and apply it to many right-hand sides $b$ in succession. *Example use*: in multi-class one-versus-rest classification, the same $A$ is used for $K$ different $y$'s; precompute once, fit $K$ times.

*Target 2 (uniqueness → cross-validation interpretability).* Under the assumption, the LS solution is *deterministic* — there is one answer, not a set. This is what makes cross-validation meaningful: each fold gives one parameter estimate, and we can compare them for stability. Without uniqueness, the comparison would be confounded by the choice of which LS minimizer is reported. *Example use*: in 5-fold CV, parameter stability across folds is interpreted as a sign of well-conditioned LS — implicitly assuming uniqueness via this theorem.

*Target 3 (existence → optimization terminates).* The existence claim guarantees that algorithms like QR-based LS terminate with a solution. Algorithms that iterate (gradient descent, conjugate gradient applied to normal equations) converge to a minimizer because one exists. *Example use*: in massive-scale LS problems (sparse $A$ with millions of rows), iterative methods like LSQR exploit this guarantee.

*Target 4 (closed form → sensitivity analysis).* The explicit formula $\hat{x} = (A^T A)^{-1} A^T b$ lets us compute the *sensitivity* of $\hat{x}$ to changes in $b$ (it's just $A^\dagger$), to changes in $A$ (via matrix-perturbation analysis), and to outliers (one row of $A$ and entry of $b$). This sensitivity analysis is the basis of *robust regression* methods. *Example use*: identifying influential observations in a regression by computing the *leverage* $h_{ii} = e_i^T A (A^T A)^{-1} A^T e_i$ — points with high leverage have outsized influence on $\hat{x}$.

---

# Why Is It True

**The mechanism in one sentence: $A^T A$ is invertible iff $A$ has injective columns, which is exactly the condition that no nonzero direction in $x$-space is "flat" for the objective.**

The intuition has two parts.

*Existence of a minimizer.* The objective $\|Ax - b\|^2$ is a continuous, non-negative function of $x \in \mathbb{R}^n$, bounded below by zero. Moreover, the objective tends to infinity in any direction where $Ax$ is unbounded — specifically, in any direction *outside* $\ker A$, the value $\|Ax - b\|^2$ grows quadratically as $\|x\|$ grows. So minimizers are confined to a bounded region (or, more precisely, the function is *coercive modulo $\ker A$*), and any minimizing sequence has a convergent subsequence by Bolzano-Weierstrass. The limit is a minimizer by continuity. This is the standard *coercivity + lower-semicontinuity* argument for existence.

*Uniqueness iff column rank.* The objective is a quadratic function $f(x) = x^T A^T A x - 2 b^T A x + \|b\|^2$. The Hessian is $\nabla^2 f = 2 A^T A$, positive semidefinite. The objective is *strictly* convex (and hence has a unique minimizer) iff the Hessian is positive definite, i.e., iff $A^T A$ is invertible. Now $A^T A v = 0$ iff $v^T A^T A v = \|Av\|^2 = 0$ iff $Av = 0$, so $A^T A$ is invertible iff $A$ has trivial kernel iff the columns of $A$ are linearly independent. This chain of equivalences is the entire content of the uniqueness claim.

*The closed-form formula.* The first-order optimality condition (gradient equals zero) gives $\nabla f(\hat{x}) = 2 A^T(A\hat{x} - b) = 0$, i.e., $A^T A \hat{x} = A^T b$ (the normal equations). Under invertibility of $A^T A$, multiply by $(A^T A)^{-1}$ to get $\hat{x} = (A^T A)^{-1} A^T b$.

The deeper geometric story: the LS problem is to project $b$ orthogonally onto $\mathrm{col}(A)$. This projection always exists (the orthogonal projection onto a finite-dimensional subspace of a Hilbert space always exists and is unique — that's [[Thm - Best Approximation by Orthogonal Projection]]). The *projection* $P b$ is unique; what is *not unique* is the choice of $x$ such that $Ax = Pb$. Such an $x$ is determined by $A^{-1}(Pb)$ when $A$ is injective on $\mathbb{R}^n$ (linearly independent columns); otherwise, multiple $x$'s map to the same $Pb$, and the set of LS minimizers is the affine subspace $A^{-1}(Pb) = \hat{x} + \ker A$.

---

# What Makes This Hard

The hard step for most students is the *equivalence* "$A^T A$ invertible ⟺ $A$ has linearly independent columns." This is the link between the algebraic condition (invertibility of the Gram matrix) and the geometric condition (injectivity of $A$ as a map). The proof is short — $v^T A^T A v = \|Av\|^2$, which is zero iff $Av = 0$ — but it must be internalized. The most common error is to assume that $A$ being "tall" ($m \geq n$) implies its columns are independent, which is *not* automatic — a tall matrix with a repeated column has linearly dependent columns.

The second tricky step is the *transition from "the projection exists" to "the LS minimizer exists."* These are different objects: the projection is in $\mathrm{col}(A) \subseteq \mathbb{R}^m$; the LS minimizer is in $\mathbb{R}^n$ and maps via $A$ to the projection. The existence of the projection is automatic (orthogonal projection theorem); the existence of an $x$ mapping to it is the existence of *some* preimage under $A$, which is the surjectivity of $A: \mathbb{R}^n \to \mathrm{col}(A)$ — guaranteed by the definition of the column space.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish existence by convexity + coercivity-modulo-kernel of the objective. Establish uniqueness by strict convexity, which equals positive definiteness of the Hessian $2 A^T A$, which equals linear independence of the columns of $A$. The closed-form solution comes from solving the first-order condition $\nabla f = 0$, which is the normal equations.

**Subgoal decomposition:**

1. **Existence.** Show that $f(x) = \|Ax - b\|^2$ attains its infimum on $\mathbb{R}^n$.
   - *Hint:* Show the sublevel sets are bounded modulo $\ker A$; alternatively, show that $f$ is convex and continuous, and apply Bolzano-Weierstrass on a minimizing sequence.
   - *Why needed:* Sets up the existence claim.

2. **Hessian computation.** Show $\nabla^2 f = 2 A^T A$.
   - *Hint:* Expand $f(x) = x^T A^T A x - 2 b^T A x + b^T b$ and differentiate twice.
   - *Why needed:* Characterizes strict convexity in terms of $A^T A$ positive definite.

3. **Equivalence of column rank and $A^T A$ invertibility.** Show: $A^T A$ is invertible iff columns of $A$ are linearly independent.
   - *Hint:* $v^T A^T A v = \|Av\|^2$, so $A^T A v = 0$ iff $Av = 0$. Use this to identify kernels.
   - *Why needed:* This is the conversion between the algebraic and geometric versions of the assumption.

4. **First-order condition.** Compute $\nabla f$ and set to zero.
   - *Hint:* $\nabla f(x) = 2 A^T (Ax - b)$, so setting $\nabla f(\hat{x}) = 0$ gives $A^T A \hat{x} = A^T b$.
   - *Why needed:* This is the normal equations, which under invertibility of $A^T A$ have a unique solution.

5. **Conclude uniqueness and closed form.** Combine: under the linear-independence assumption, $A^T A$ is invertible, the normal equations have unique solution $\hat{x} = (A^T A)^{-1} A^T b$, and this is the unique LS minimizer.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\nabla f(x) = 2 A^T (Ax - b)$, $\nabla^2 f(x) = 2 A^T A$.
> **Statement:** Let $f(x) = \|Ax - b\|^2$. Then $\nabla f(x) = 2 A^T (Ax - b)$ and $\nabla^2 f(x) = 2 A^T A$.
>
> **Hint:** Expand $f(x) = (Ax - b)^T(Ax - b) = x^T A^T A x - 2 b^T A x + b^T b$ and differentiate component-by-component.
>
> **Why needed:** The gradient gives the first-order optimality condition (the normal equations); the Hessian gives the second-order strict-convexity condition (positive definiteness of $A^T A$).
>
> > [!note]- Full proof
> > Expanding the squared norm:
> > $$f(x) = (Ax - b)^T(Ax - b) = (Ax)^T(Ax) - 2 b^T (Ax) + b^T b = x^T A^T A x - 2 b^T A x + b^T b.$$
> > The first-order derivative of $x^T A^T A x$ with respect to $x_k$ is $\sum_j (A^T A)_{kj} x_j + \sum_i (A^T A)_{ik} x_i = 2(A^T A x)_k$ (using symmetry of $A^T A$). The derivative of $b^T A x$ with respect to $x_k$ is $(A^T b)_k$. The constant $b^T b$ has zero derivative. Combining: $\nabla f(x) = 2 A^T A x - 2 A^T b = 2 A^T(Ax - b)$. The second derivative (Hessian) is $\nabla^2 f(x) = 2 A^T A$, a constant matrix.

> [!note]- Lemma 2: $A^T A$ is positive definite iff columns of $A$ are linearly independent.
> **Statement:** The Gram matrix $A^T A$ is positive definite (and hence invertible) iff the columns of $A$ are linearly independent.
>
> **Hint:** Compute $v^T A^T A v$ and recognize it as $\|Av\|^2$. Use the kernel characterization.
>
> **Why needed:** Identifies the algebraic invertibility condition with the geometric linear-independence condition, which is the assumption stated in the theorem.
>
> > [!note]- Full proof
> > For any $v \in \mathbb{R}^n$, $v^T A^T A v = (Av)^T(Av) = \|Av\|^2 \geq 0$. So $A^T A$ is positive *semi*-definite always. Equality $v^T A^T A v = 0$ holds iff $Av = 0$, i.e., $v \in \ker A$. So $A^T A$ is strictly positive (i.e., $v^T A^T A v > 0$ for all $v \neq 0$) iff $\ker A = \{0\}$ iff the columns of $A$ are linearly independent. Positive definiteness implies invertibility (no zero eigenvalues), and the implication is reversible (a positive-semidefinite matrix is positive definite iff invertible). So $A^T A$ is invertible iff columns of $A$ are independent.

> [!note]- Lemma 3: Strict convexity of $f$ implies uniqueness of minimizer.
> **Statement:** If a function $f : \mathbb{R}^n \to \mathbb{R}$ is strictly convex and has a minimizer, the minimizer is unique.
>
> **Hint:** Use the definition of strict convexity to derive a contradiction from two distinct minimizers.
>
> **Why needed:** Combined with Lemma 2 (which gives strict convexity from the column-independence assumption), this gives uniqueness of the LS minimizer.
>
> > [!note]- Full proof
> > Suppose $x^*$ and $y^*$ are two distinct minimizers of $f$, so $f(x^*) = f(y^*) = m$. By strict convexity, $f(\lambda x^* + (1 - \lambda) y^*) < \lambda f(x^*) + (1 - \lambda) f(y^*) = m$ for any $\lambda \in (0, 1)$. This contradicts $m$ being the minimum, since we have found a point with $f$-value strictly less than $m$. So the minimizer is unique.

> [!note]- Lemma 4: Existence of an LS minimizer.
> **Statement:** The function $f(x) = \|Ax - b\|^2$ attains its infimum on $\mathbb{R}^n$.
>
> **Hint:** Show that the sublevel sets of $f$ are closed and bounded modulo $\ker A$; equivalently, take a minimizing sequence and use coercivity to extract a convergent subsequence.
>
> **Why needed:** This is part (1) of the theorem, the existence claim. Even without uniqueness, we need at least one minimizer to exist.
>
> > [!note]- Full proof
> > Let $m^* = \inf_x f(x) \geq 0$, and take a minimizing sequence $\{x_k\}$ with $f(x_k) \to m^*$. Decompose each $x_k$ as $x_k = x_k^\parallel + x_k^\perp$ where $x_k^\perp \in \ker A$ and $x_k^\parallel$ is in the orthogonal complement (the row space of $A$). Then $A x_k = A x_k^\parallel$, so $f(x_k) = \|A x_k^\parallel - b\|^2$ depends only on $x_k^\parallel$. Now $f(x_k^\parallel)$ is a quadratic in $x_k^\parallel$ that *is coercive* on the row space of $A$ (since $A$ is injective there), so $\|x_k^\parallel\|$ is bounded for a minimizing sequence. By Bolzano-Weierstrass, a subsequence $x_{k_j}^\parallel \to \hat{x}^\parallel$. By continuity, $f(\hat{x}^\parallel) = m^*$. So $\hat{x}^\parallel$ is a minimizer of $f$ in the row space, and any element of $\hat{x}^\parallel + \ker A$ is a minimizer of $f$ on $\mathbb{R}^n$.

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 1: Existence.* Apply Lemma 4 to conclude that a minimizer of $f(x) = \|Ax - b\|^2$ exists.
>
> *Step 2: Compute the gradient and Hessian.* By Lemma 1, $\nabla f(x) = 2 A^T (Ax - b)$ and $\nabla^2 f(x) = 2 A^T A$.
>
> *Step 3: First-order condition.* If $\hat{x}$ minimizes $f$, then $\nabla f(\hat{x}) = 0$, i.e., $A^T A \hat{x} = A^T b$ — the normal equations.
>
> *Step 4: Uniqueness under linear independence.* If the columns of $A$ are linearly independent, then by Lemma 2, $A^T A$ is positive definite (hence invertible). The normal equations then have the unique solution $\hat{x} = (A^T A)^{-1} A^T b$. Since the Hessian is positive definite, $f$ is strictly convex; by Lemma 3, the LS minimizer is unique.
>
> *Step 5: Conversely, if the columns of $A$ are linearly dependent.* Then $A^T A$ is positive semidefinite but not positive definite; there is some nonzero $v$ with $A^T A v = 0$, hence $Av = 0$. For any LS minimizer $\hat{x}$, the point $\hat{x} + v$ is also an LS minimizer: $\|A(\hat{x} + v) - b\|^2 = \|A\hat{x} + Av - b\|^2 = \|A\hat{x} - b\|^2$. So the LS minimizer is not unique.
>
> *Step 6: Closed form.* Under the linear-independence assumption, the unique minimizer is given by the explicit formula $\hat{x} = (A^T A)^{-1} A^T b$ from step 4.
>
> *Step 7 (Corollary): SVD-based minimum-norm solution.* When the columns of $A$ are linearly dependent, the set of LS minimizers is $\hat{x}_0 + \ker A$ for any particular minimizer $\hat{x}_0$. The minimum-norm element of this affine subspace is the projection of zero onto it, which by the SVD-based pseudoinverse formula equals $A^+ b$ where $A^+ = V \Sigma^+ U^*$ for the SVD $A = U \Sigma V^*$. See [[Thm - Singular Value Decomposition]] and [[Def - Pseudoinverse]].

---

# Cross-Field Exercise Suggestions

*Suggestion 1 (Probability — Gaussian MLE):* The maximum likelihood estimator for the mean of a Gaussian with known covariance, given i.i.d. samples, is the sample mean. Show that this is an LS problem (with the design matrix being all-ones, $A = \mathbf{1}$) and apply the theorem to recover the sample-mean formula, plus the fact that uniqueness follows from linear independence (trivially satisfied since $\mathbf{1}$ has one column, which is nonzero).

*Suggestion 2 (Functional Analysis — Riesz Representation):* In an inner product space, the Riesz representation theorem says every bounded linear functional is the inner product with some vector. The LS problem in coordinates is a finite-dimensional Riesz: given a linear functional $\phi(x) = \langle a, x \rangle$ defined on $\mathrm{col}(A)$, find the $x$ representing it as $\langle Ax, b \rangle = b^T A x$. Existence and uniqueness of the LS solution is the finite-dimensional case of the Riesz representation theorem.

*Suggestion 3 (Convex Optimization — Pareto fronts):* The set of LS minimizers (when not unique) is an affine subspace, hence convex. This is a special case of the general fact: the set of minimizers of a convex function is convex. Apply this to multi-objective LS to understand the structure of Pareto-optimal sets, and to constrained LS to understand when the constrained problem has multiple optimizers.

*Suggestion 4 (Algebra — Solving Linear Systems via LS):* Solving a square invertible system $Ax = b$ via LS gives the same answer as $A^{-1} b$: when $A$ is square and invertible, $A^T A$ is also invertible, and $(A^T A)^{-1} A^T = A^{-1}$ (left inverse equals true inverse for invertible square matrices). LS is a *generalization* of exact solution. Use this to interpret the LS-via-QR algorithm as a *generalization* of QR-based solution of square systems.

---

# Bridges

- **[[Thm - Best Approximation by Orthogonal Projection]]** — The LADR theorem from inner product space theory says that the orthogonal projection onto a closed subspace gives the unique closest point. The LS existence-uniqueness theorem is this projection theorem made coordinate-explicit: the projection of $b$ onto $\mathrm{col}(A)$ is $P b = A(A^T A)^{-1} A^T b$, and the LS solution is the preimage $\hat{x}$ such that $A\hat{x} = Pb$. Uniqueness of $\hat{x}$ requires injectivity of $A$, i.e., linear independence of its columns.

- **[[Thm - Singular Value Decomposition]]** — The SVD provides the general LS solver via the pseudoinverse $A^+$. In the full-column-rank case, $A^+ = (A^T A)^{-1} A^T$ coincides with the standard LS formula. In the rank-deficient case, $A^+$ gives the minimum-norm LS solution among all minimizers, which is the canonical choice when uniqueness fails. The SVD perspective unifies the full-rank and rank-deficient cases under one formula.

- **[[Def - Pseudoinverse]]** — The pseudoinverse of $A$, denoted $A^+$ or $A^\dagger$, is exactly the operator that, applied to $b$, gives the LS solution (when full rank) or the minimum-norm LS solution (when rank-deficient). The pseudoinverse is the *unifying object* of LS: every formula in the chapter can be written compactly using it.

- **Tikhonov regularization** (see [[Def - Regularized Least Squares]]) — When the columns of $A$ are dependent, the LS minimizer is not unique. Adding $\lambda \|x\|^2$ to the objective restores uniqueness (the regularized normal equations $(A^T A + \lambda I) x = A^T b$ have invertible coefficient matrix for any $\lambda > 0$). The regularized solution converges, as $\lambda \to 0^+$, to the SVD-based minimum-norm LS solution.

---

# Unlocked by This

> [!tip] Iterative Solvers for Large-Scale LS *(from Numerical Linear Algebra)*
> The closed-form LS solution requires direct linear algebra ($O(mn^2)$ flops via QR). For very large $A$ (millions of rows), iterative methods are required. **LSQR** (Paige & Saunders 1982) and **LSMR** are Krylov-subspace iterative methods that exploit only matrix-vector products $Av$ and $A^T u$, with cost per iteration $O(\text{nnz}(A))$. For sparse $A$, this can be much faster than direct methods. The existence-uniqueness theorem here is what guarantees the iterations have a target to converge to.

> [!tip] Compressed Sensing *(from Signal Processing)*
> When $A$ is *wide* (more columns than rows, $n > m$) and the true solution $x^*$ is *sparse* (most components zero), the LS theorem alone cannot recover $x^*$ — there are infinitely many LS minimizers. **Compressed sensing** adds an L1 penalty $\lambda \|x\|_1$ to the LS objective; under conditions on $A$ (restricted isometry property), the L1-regularized problem recovers $x^*$ exactly. This is one of the most striking modern extensions of the LS framework, and it shows the limits of L2 LS in the rank-deficient case.
