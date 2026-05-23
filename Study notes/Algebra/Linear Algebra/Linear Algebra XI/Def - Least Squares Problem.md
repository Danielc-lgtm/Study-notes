---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal Projection"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Let $A$ be an $m \times n$ matrix, $b$ an $m$-vector, $x$ an $n$-vector. The default convention (Boyd) is that $A$ is *tall*: $m \geq n$. The Euclidean norm is $\|v\|^2 = v^T v$, and the *residual* of a candidate $x$ is $r = Ax - b$. We write $\hat{x}$ for the least squares solution. See the parent topic page [[Linear Algebra XI — Applied II — Least Squares]] for the full registry.

---

# Axiom Motivation

Suppose you have $m$ noisy linear measurements of an $n$-dimensional unknown $x$, with $m > n$. The measurement equations are $A x = b$, but the system is generically inconsistent — there is no $x$ that satisfies all $m$ equations simultaneously, because $b$ does not lie in the $n$-dimensional column space of $A$. Sitting in $\mathbb{R}^m$, the column space $\mathrm{col}(A)$ is an $n$-dimensional [[Def - Subspace|subspace]]; $b$ is a generic point in $\mathbb{R}^m$ that is *not* in this [[Def - Subspace|subspace]]. What do we do?

Three natural responses suggest themselves, and each is wrong for a subtle reason.

First, we might try to satisfy *some* of the equations exactly — say, choose $n$ of the $m$ equations and solve them, ignoring the rest. The problem is that this is arbitrary; different choices of $n$ equations give different "solutions," and the answer depends entirely on which equations we trust. Worse, in many applications all measurements are equally good and there is no principled basis for discarding any of them.

Second, we might try to minimize $\|Ax - b\|$ in some norm — say, the $L^1$ norm $\sum_i |r_i|$ or the $L^\infty$ norm $\max_i |r_i|$. Both give valid notions of "closest fit." The $L^\infty$ norm — *Chebyshev approximation* — minimizes the worst-case residual; the $L^1$ norm gives a robust solution insensitive to outliers. But neither has a closed-form linear solution, and both lead to optimization problems (linear programs in fact) that are computationally much harder than what we are about to construct.

Third, we minimize $\|Ax - b\|^2$, the *squared Euclidean norm* of the residual. This is the choice that makes the problem tractable, and the reason is geometric: the squared Euclidean norm is the squared distance in $\mathbb{R}^m$, and minimizing it amounts to finding the point in the subspace $\mathrm{col}(A)$ closest to $b$ in the *Euclidean* sense. This is exactly the orthogonal-projection problem, and orthogonal projection in a Hilbert space is the cleanest, most computable, most theoretically transparent kind of "closest point" you can ask for.

So the choice of $\|\cdot\|^2$ as the objective is not arbitrary: it is the only norm whose minimization is *linear in $b$*, *closed-form in $A$*, and *geometrically interpretable* as projection. The cost is that LS is sensitive to outliers (a single large residual contributes its square, which can dominate the objective), but for Gaussian-noise models this sensitivity is correctly calibrated: LS is the maximum-likelihood estimator under Gaussian noise. The bridge to **Linear Regression** in statistics is exactly this — what statisticians call "OLS" (ordinary least squares) is this definition applied to a regression model.

The further axiom-level requirement is that the *columns of $A$ be linearly independent*. Without this assumption, the LS solution exists but is not unique; the set of LS minimizers is an affine subspace of [[Def - Dimension|dimension]] equal to the [[Def - Dimension|dimension]] of $\ker A$. We do not "drop" this axiom — instead, the rank-deficient case is handled by the [[Def - Pseudoinverse|pseudoinverse]] from SVD (see [[Def - Pseudoinverse]]), which picks out the *minimum-norm* minimizer as the canonical answer. So the linear-independence-of-columns assumption is really a *cleanness* assumption: it makes the minimizer unique, the formula explicit, and the algorithm well-conditioned. Without it, the problem is still well-posed; the solution just needs more machinery to express.

Could a reader who has never seen this definition invent it? The path would be: recognize the situation (overdetermined linear system, no exact solution); reject discarding measurements as arbitrary; minimize some norm of the residual; choose the squared Euclidean norm because (a) it is differentiable and admits gradient-based optimization, (b) it has the geometric interpretation of orthogonal projection, (c) under Gaussian noise it is the MLE. The squared norm is the unique choice that makes all three of these properties simultaneously hold, so a thoughtful reader would arrive at it.

---

# The Definition

> **Definition (Least Squares Problem).** Given an $m \times n$ matrix $A$ and an $m$-vector $b$, the *least squares problem* is to find an $n$-vector $\hat{x}$ that minimizes the objective
> $$\|Ax - b\|^2 = (Ax - b)^T (Ax - b) = \sum_{i=1}^m \left(\sum_{j=1}^n A_{ij} x_j - b_i\right)^2.$$
> Any vector $\hat{x}$ satisfying $\|A\hat{x} - b\|^2 \leq \|Ax - b\|^2$ for all $x \in \mathbb{R}^n$ is called a *least squares approximate solution* of the equation $Ax = b$, or simply *the* LS solution when uniqueness is guaranteed.

When the columns of $A$ are linearly independent, the LS solution is unique and given by $\hat{x} = (A^T A)^{-1} A^T b = A^\dagger b$, where $A^\dagger = (A^T A)^{-1} A^T$ is the (left) [[Def - Pseudoinverse|pseudoinverse]]. See [[Thm - Existence and Uniqueness of Least Squares Solution]] for the precise statement and [[Thm - Least Squares via Normal Equations]] and [[Thm - Least Squares via QR Factorization]] for the algorithms.

---

# Categorical / Structural Definition

In the abstract Hilbert-space setting, the LS solution is the orthogonal projection of $b$ onto the closed subspace $\mathrm{col}(A) \subseteq \mathbb{R}^m$. More precisely, the linear map $A : \mathbb{R}^n \to \mathbb{R}^m$ has range $\mathrm{col}(A)$, and the *closest-point projection* $P_{\mathrm{col}(A)} : \mathbb{R}^m \to \mathrm{col}(A)$ is well-defined because $\mathrm{col}(A)$ is a closed (in fact, finite-dimensional) subspace of the Hilbert space $\mathbb{R}^m$. The LS solution is then any preimage of this projection under $A$:

$$\hat{x} \in A^{-1}\big(P_{\mathrm{col}(A)}(b)\big).$$

When $A$ has linearly independent columns (i.e., $\ker A = \{0\}$), $A$ is injective on $\mathbb{R}^n$ and the preimage is a single point — the unique LS solution. When $A$ has a nontrivial kernel, the preimage is a [[Def - Coset|coset]] of $\ker A$, and the LS solutions form an affine subspace of $\mathbb{R}^n$.

This is exactly the content of [[Thm - Best Approximation by Orthogonal Projection]] in [[Linear Algebra VI — §6 Inner Product Spaces]]: the orthogonal projection onto a closed subspace gives the unique closest point in that subspace to any point outside. Boyd's definition is this projection theorem made concrete and computational: the projection $P_{\mathrm{col}(A)} = A(A^T A)^{-1} A^T$ is the explicit form of the abstract projection, and the LS solution is its coordinate expression in the basis given by the columns of $A$.

---

# Relate to Other Fields / Compression

**True name:** the LS problem is the *orthogonal projection of $b$ onto the column space of $A$*, expressed in the coordinate system of the columns of $A$. The squared-norm objective is incidental; the geometric content is projection.

This is the same construction as best approximation in any inner product space: given a closed subspace $W \subseteq V$ and a point $v \in V$, the closest point in $W$ to $v$ is the orthogonal projection of $v$ onto $W$. Specializing to $V = \mathbb{R}^m$ with the standard inner product and $W = \mathrm{col}(A)$ recovers the LS problem.

The same construction also appears in:
- **Linear Regression** (statistics): when the data are $(x_i, y_i)$ and the model is $y \approx X\beta$, the LS estimator $\hat{\beta} = (X^T X)^{-1} X^T y$ is exactly this projection, with $X$ playing the role of $A$ and $y$ the role of $b$.
- **Fourier series**: the partial sums of the Fourier series of $f$ are orthogonal projections of $f$ onto finite-dimensional subspaces spanned by sines and cosines. The "best approximation in $L^2$ norm" interpretation of Fourier series is the LS problem in an infinite-dimensional Hilbert space.
- **Kalman filtering**: the Kalman state estimate is the orthogonal projection of the (joint) observation/state vector onto the (joint) constraint subspace defined by the dynamics, which gives the conditional-mean interpretation of the filter.

---

# Examples / Corollaries

*Example 1 (regression line).* Take $A = \begin{pmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_N \end{pmatrix}$ and $b = (y_1, \ldots, y_N)$. The LS problem $\min \|A\theta - b\|^2$ fits the line $y \approx \theta_1 + \theta_2 x$ to the data; this is the simplest non-trivial LS problem and the algebraic core of every linear regression. The unique solution exists provided the $x_i$ are not all equal (so the columns of $A$ are independent). See [[Ex - Fitting a line to data via least squares]].

*Example 2 (square invertible case).* If $A$ is square and invertible, the LS problem reduces to solving $Ax = b$ exactly, with $\hat{x} = A^{-1} b$ and residual $r = 0$. LS *generalizes* exact solution: when an exact solution exists, the LS solution coincides with it.

*Example 3 (rank-deficient case — is NOT a unique LS solution).* Take $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $b = (1, 0)$. The columns of $A$ are linearly dependent (they are equal), so $A^T A = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$ is singular and the standard formula fails. The set of LS minimizers is the line $x_1 + x_2 = 1/2$ in $\mathbb{R}^2$; every point on this line gives residual $r = (-1/2, 1/2)$ and the same minimum objective $\|r\|^2 = 1/2$. The minimum-norm LS solution is the point on this line closest to the origin, $\hat{x} = (1/4, 1/4)$, recovered by the SVD-based [[Def - Pseudoinverse|pseudoinverse]].

*Example 4 (exact-solution-via-LS sanity check).* If $b = A x_0$ for some $x_0$ (i.e., $Ax = b$ has an exact solution), then $\hat{x} = x_0$. To verify: $\|A x_0 - b\|^2 = 0$, which is the minimum possible value of the objective, so $x_0$ is a minimizer. If $A$ has linearly independent columns, $x_0$ is the unique minimizer.

*Example 5 (is NOT just a regression — overdetermined inhomogeneous system).* Consider the linear system
$$2 x_1 = 1, \quad -x_1 + x_2 = 0, \quad 2 x_2 = -1.$$
This is overdetermined: 3 equations in 2 unknowns. From the first equation, $x_1 = 1/2$; from the third, $x_2 = -1/2$; substituting into the second gives $-1/2 + (-1/2) = -1 \neq 0$. So no exact solution exists. The LS problem $\min \|Ax - b\|^2$ with $A = \begin{pmatrix} 2 & 0 \\ -1 & 1 \\ 0 & 2 \end{pmatrix}$ and $b = (1, 0, -1)$ has unique solution $\hat{x} = (1/3, -1/3)$, with residual $r = (-1/3, -2/3, 1/3)$ and $\|r\|^2 = 2/3$. Note that the LS solution does *not* satisfy any individual equation exactly — it is a compromise across all three.

**Calibration check.** If you have understood the definition, you should be able to verify: (i) the LS solution to $\min \|x - c\|^2$ (with $A = I$, $b = c$) is $\hat{x} = c$, with residual zero; (ii) the LS solution to $\min \|0 \cdot x - b\|^2$ (with $A = 0$) is the empty minimization with no choice possible — every $x$ achieves the same objective $\|b\|^2$; (iii) for any $A$ with linearly independent columns and any $b$, the matrix $P = A(A^T A)^{-1} A^T$ satisfies $P^2 = P$ and $P^T = P$, the algebraic characterization of an orthogonal projection.

---

# Unlocked by This

> [!tip] Pseudoinverse for Underdetermined Systems *(from Numerical Linear Algebra)*
> Once the LS solver $A^\dagger = (A^T A)^{-1} A^T$ is in hand for tall $A$, the parallel construction for *wide* $A$ (more unknowns than equations, $A$ with linearly independent rows) is $A^\dagger = A^T(AA^T)^{-1}$, which gives the *minimum-norm solution* of $Ax = b$. The general case is handled by the SVD-based pseudoinverse $A^+ = V \Sigma^+ U^*$ from [[Thm - Singular Value Decomposition|SVD]], which works for any matrix, rank-deficient or full-rank. The conceptual unification is that "the pseudoinverse always returns the unique optimal solution under the appropriate optimality criterion" — minimum residual for tall, minimum norm for wide, minimum-norm-among-minimum-residuals for general.

> [!tip] Linear Regression *(from Statistics)*
> The LS problem in this definition is exactly **Linear Regression** in statistics, where it is derived from a probabilistic model $y = X\beta + \epsilon$ with i.i.d. Gaussian noise $\epsilon$. The LS estimator $\hat{\beta} = (X^T X)^{-1} X^T y$ is the maximum-likelihood estimator under this Gaussian-noise assumption. Statistical theory then layers on top: sampling distributions of $\hat{\beta}$, standard errors, confidence intervals, the $t$-statistic, the $F$-test, the coefficient of determination $R^2$. All of these are *probabilistic upgrades* of the geometric setup here, predicated on the noise model. The bridge tells you that what numerical analysts compute and what statisticians interpret are the same object viewed two ways.

> [!tip] Bayesian Linear Regression *(from Bayesian Statistics)*
> The Bayesian reformulation introduces a prior over $x$ — typically Gaussian, $x \sim \mathcal{N}(0, \tau^2 I)$ — and the posterior mode (MAP estimator) becomes $\hat{x} = (A^T A + (\sigma^2/\tau^2) I)^{-1} A^T b$. This is exactly Tikhonov regularization with $\lambda = \sigma^2/\tau^2$. The Bayesian picture also gives the full posterior (not just the mode), which quantifies *uncertainty* in the estimate — a piece of information the pure LS solution does not provide. **Bayesian Linear Regression** is the natural framework for combining LS estimation with prior information and uncertainty quantification.
