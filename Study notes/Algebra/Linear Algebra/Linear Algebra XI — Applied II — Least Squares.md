---
type: topic
subject: linear-algebra
chapter: "Boyd 12-17"
title: "Linear Algebra XI — Applied II: Least Squares"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation Registry

This chapter follows Boyd & Vandenberghe's notation. The convention worth flagging up front is that $x$ is the *unknown* vector to be chosen, and $b$ is the *data* — the right-hand side we are trying to approximate. In Chapter 13 onward, when we move to data fitting, the symbol $x$ is recycled to mean *feature vector* and the unknown becomes $\theta$ (or $\beta$, $v$ in regression form); the right-hand side becomes $y^d$. We mention this clash explicitly because it confuses everyone the first time. When a constrained problem appears, $C$ and $d$ are the constraint matrix and right-hand side, $\nu$ (or $z$) is the Lagrange multiplier vector, and the augmented system is the *KKT system*.

> [!warning] Convention: residual sign
> Some authors define the residual as $r = b - Ax$ rather than $r = Ax - b$. The two definitions differ only by a sign and have the same squared norm, so no result changes. We follow Boyd: $r = Ax - b$.

- $A$ — an $m \times n$ data matrix. When tall ($m \geq n$) with linearly independent columns, $A^T A$ is invertible and the least squares problem has a unique solution.
- $b$ — the $m$-vector right-hand side ("target").
- $x$ — the $n$-vector unknown (or $\theta$ in data-fitting contexts, or $w$ in portfolio contexts).
- $r = Ax - b$ — the residual. $\|r\|^2 = \|Ax - b\|^2$ is the *least squares objective*.
- $\hat{x}$ — the least squares solution, $\hat{x} = (A^T A)^{-1} A^T b = A^\dagger b$.
- $A^\dagger$ — the (left) pseudoinverse, $A^\dagger = (A^T A)^{-1} A^T$ when $A$ has linearly independent columns.
- $A^T A$ — the *Gram matrix* of $A$.
- $A = QR$ — the QR factorization, $Q$ with orthonormal columns, $R$ upper triangular and invertible.
- $C, d$ — constraint matrix ($p \times n$) and right-hand side ($p$-vector) for constrained problems $Cx = d$.
- $\nu$ — Lagrange multiplier vector for equality constraints.
- $\lambda$ (or $\lambda_i$) — regularization weight (always $\lambda > 0$).
- $x^{(i)}, y^{(i)}$ — the $i$th data point (feature vector and outcome) in data-fitting problems.
- $\theta$ — model parameter vector in data-fitting; $\hat{\theta}$ is its least squares fit.
- $f_1, \ldots, f_p$ — basis functions in a "linear in the parameters" model $\hat{f}(x) = \sum_j \theta_j f_j(x)$.
- $A^{(t)}, B^{(t)}, C^{(t)}$ — time-varying dynamics, input, and output matrices in control/estimation.
- $x_t, u_t, y_t$ — state, input, output at time $t$ in a dynamical system.

---

# Motivation

Here is the entire chapter in one sentence: when you cannot solve $Ax = b$, project $b$ onto the column space of $A$ and call the projection the solution. Everything else — data fitting, classification, regularization, constrained problems, the Kalman filter — is a variation on that one move.

The reason this matters is that "cannot solve $Ax = b$" is the *normal case*, not the exception. Whenever you have more equations than unknowns ($A$ is tall), the system is overdetermined and typically inconsistent; whenever you have a model with parameters fewer than your data points, you are in exactly this situation. The least squares solution is the unique point in the column space of $A$ closest to $b$, and the residual $b - A\hat{x}$ is orthogonal to that column space. This is the *orthogonality principle*, and it is the geometric heart of the whole chapter.

If the abstract picture in Topic VI — "best approximation by orthogonal projection in a Hilbert space" — felt theoretical, this is what it looks like applied. Boyd's $\hat{x} = (A^T A)^{-1} A^T b$ is *literally* the formula for the coordinates of the orthogonal projection of $b$ onto the [[Def - Subspace|subspace]] spanned by the columns of $A$, expressed in those columns as a basis. The formula $A\hat{x} = $ (orthogonal projection of $b$) is the operator-side identity. Everything in this chapter that looks computational is the geometric content of [[Thm - Best Approximation by Orthogonal Projection]] applied to a concrete numerical problem.

The structural backbone of the chapter is the following hierarchy of problems:

$$
\text{LS} \subset \text{multi-objective LS} \subset \text{regularized LS} \subset \text{constrained LS (KKT)}
$$

Each layer adds one element: multi-objective LS stacks several least squares objectives with weights; regularized LS is the special case where one of the stacked objectives is $\|x\|^2$ or $\|x - x_{\text{prior}}\|^2$; constrained LS is the limit where one weight goes to infinity, replacing a soft objective with a hard constraint. The Lagrange-multiplier formulation of the constraint is the *KKT system*, and the trick that unifies everything is to recognize that all four problems are solved by a single linear system whose matrix is built from $A^T A$ and $C^T$ blocks.

The three "applications" sections of Chapter 17 — portfolio optimization, linear quadratic control, and Kalman state estimation — are not three different topics. They are *the same constrained least squares problem* with three different interpretations of what the matrix $A$, the vector $b$, and the constraint $Cx = d$ mean. In portfolio optimization, $A$ is the asset-return matrix and the constraint fixes the budget and target return. In linear quadratic control, $A$ is built from output matrices $C_t$ and input weights, and the constraint encodes the dynamics. In Kalman estimation, $A$ is the measurement matrix and the constraint *also* encodes the dynamics. Recognizing that these three "different" problems share one KKT structure is the highest-leverage insight in the chapter.

This chapter assumes you have worked through (or can refresh) [[Linear Algebra VI — §6 Inner Product Spaces]] (inner products, orthogonality, orthogonal projection, [[Def - Pseudoinverse|pseudoinverse]] — the abstract origin of least squares) and [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] (QR factorization and SVD — the practical algorithms). The Boyd applied-I notes [[Linear Algebra X — Applied I — Vectors, Distance, Equations, Dynamics]] are not a strict prerequisite but provide the matrix-side concreteness that this chapter builds on. We will use [[Thm - QR Factorization]] freely and refer to [[Thm - Singular Value Decomposition]] when the full pseudoinverse machinery is invoked.

---

# Concept Map

## §XI.1 The Least Squares Problem

- **[[Def - Least Squares Problem]]**
	- Given an $m \times n$ matrix $A$ (typically tall) and an $m$-vector $b$, the least squares problem is to find an $n$-vector $\hat{x}$ that minimizes $\|Ax - b\|^2$. When the columns of $A$ are linearly independent, the solution is unique. The residual $r = A\hat{x} - b$ is generally nonzero — least squares does *not* solve $Ax = b$; it finds the $x$ that comes closest. Geometrically, $A\hat{x}$ is the orthogonal projection of $b$ onto the column space of $A$.

- **[[Def - Normal Equations]]**
	- The normal equations are the linear system $A^T A x = A^T b$. Any minimizer of $\|Ax - b\|^2$ satisfies them, and under the standard assumption that $A$ has linearly independent columns, the Gram matrix $A^T A$ is invertible and the system has the unique solution $\hat{x} = (A^T A)^{-1} A^T b$. The equations express the orthogonality principle algebraically: $A^T(A\hat{x} - b) = 0$ says the residual is orthogonal to every column of $A$.

- **[[Thm - Existence and Uniqueness of Least Squares Solution]]**
	- If $A$ has linearly independent columns, then $\|Ax - b\|^2$ has a unique minimizer $\hat{x} = (A^T A)^{-1} A^T b$. The proof has two parts: (i) any minimizer satisfies $A^T(A\hat{x} - b) = 0$ by direct calculation of the gradient or by completing the square; (ii) the linear-independence assumption makes $A^T A$ invertible so the normal equations have a unique solution. Without linear independence, a minimizer still exists but is not unique — the [[Def - Pseudoinverse|pseudoinverse]] from [[Thm - Singular Value Decomposition|SVD]] picks the minimum-norm one.

- **[[Thm - Least Squares via Normal Equations]]**
	- The least squares solution can be computed by forming the Gram matrix $G = A^T A$ and the vector $h = A^T b$, then solving $Gx = h$ by Cholesky factorization (since $G$ is positive definite under the linear-independence assumption). This is theoretically clean and conceptually simple, but it is numerically dangerous: forming $A^T A$ *squares the condition number* of $A$, which can make the linear system catastrophically more sensitive to floating-point error than the original problem. In practice, it is rarely the algorithm of choice.

- **[[Thm - Least Squares via QR Factorization]]**
	- With $A = QR$ (the QR factorization, $Q$ with orthonormal columns and $R$ upper-triangular and invertible), the pseudoinverse becomes $A^\dagger = R^{-1} Q^T$, and the least squares solution is found by computing $Q^T b$ and then back-solving $R\hat{x} = Q^T b$. This is the *practical workhorse* of least squares — it has half the condition number issue of the normal equations approach and is numerically stable. The total cost is $2mn^2$ flops, dominated by the QR factorization itself. When a software package writes `A\b` for an overdetermined system, this is what it does.

> [!tip] Unlocked: [[Def - Pseudoinverse|Pseudoinverse]] for Underdetermined Systems *(from Numerical Linear Algebra)*
> Now that $A^\dagger = (A^T A)^{-1} A^T$ is recognized as the LS solver for tall $A$ with independent columns, the **full pseudoinverse** $A^+ = V \Sigma^+ U^*$ (from [[Thm - Singular Value Decomposition|SVD]]) handles every case: tall and skinny, fat and wide, rank-deficient, exact, or approximate. For an underdetermined system ($A$ wide, with linearly independent rows), $A^+ b$ is the *minimum-norm solution* of $Ax = b$, and the formula switches to $A^+ = A^T (A A^T)^{-1}$. The "true name" of the pseudoinverse is "the least squares solver that always gives a unique answer."

- **[[Ex - Fitting a line to data via least squares]]** (⭐)
	- Given data points $(x_1, y_1), \ldots, (x_N, y_N)$, fit the model $y \approx \theta_1 + \theta_2 x$ by least squares. Derive the closed-form solution and recognize that the slope can be written as $\hat{\theta}_2 = \rho \cdot \mathrm{std}(y)/\mathrm{std}(x)$ where $\rho$ is the correlation coefficient. This is the simplest non-trivial use of least squares and the algebraic skeleton of every regression analysis.

> [!note] Exercise Index — §XI.1
> [[Exercise Index - §XI.1 The Least Squares Problem]]

## §XI.2 Data Fitting and Classification

- **[[Def - Least Squares Data Fitting]]**
	- Given $N$ data pairs $(x^{(i)}, y^{(i)})$ with $x^{(i)} \in \mathbb{R}^n$ and $y^{(i)} \in \mathbb{R}$, a "linear in the parameters" model has the form $\hat{f}(x) = \theta_1 f_1(x) + \cdots + \theta_p f_p(x)$ for chosen basis functions $f_1, \ldots, f_p$. The least squares fit minimizes the residual sum of squares $\sum_i (y^{(i)} - \hat{f}(x^{(i)}))^2$. The clever observation is that this is just a least squares problem $\min \|A\theta - y^d\|^2$ with $A_{ij} = f_j(x^{(i)})$, so the entire machinery of §XI.1 applies unchanged.

- **[[Def - Validation (Training and Test Error)]]**
	- The model fitted on observed data — the *training set* — may not predict well on unseen data. To assess generalization, split the data into a training set (typically 80%) used to fit the model and a *test set* (the remaining 20%) used only to evaluate it. The RMS prediction error on the test set is what we expect on future data. *Cross-[[Def - Validation (Training and Test Error)|validation]]* extends this by splitting into $k$ folds and rotating which fold is held out, producing $k$ estimates and a check for parameter stability. When training error is small but test error is much larger, the model is *overfit* — it has memorized noise.

- **[[Def - Feature Engineering]]**
	- Feature engineering is the (often application-specific) construction of new basis functions from raw data. Common moves: encode categoricals as one-hot vectors, add piecewise-linear functions $\max\{x_i - b, 0\}$ for nonlinear effects, take pairwise products $x_i x_j$ for interactions, stratify by a categorical to fit submodels, and (more exotically) random features $(Rx)_+$ for high-capacity universal approximation. The training error always decreases with more features; whether the test error improves is the empirical question that validation is designed to answer.

- **[[Def - Least Squares Classifier]]**
	- For binary classification, encode the labels as $y \in \{-1, +1\}$ and fit a real-valued least squares regression $\tilde{f}(x) = x^T \beta + v$ to the labels, ignoring that the labels are discrete. The classifier is $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x))$. The continuous output $\tilde{f}(x)$ can be interpreted as a confidence score, and shifting the decision threshold ($\hat{f}(x) = \mathrm{sign}(\tilde{f}(x) - \alpha)$) trades off false positives against false negatives — sweeping $\alpha$ traces out the ROC curve. For multi-class problems, the *one-versus-rest* trick fits one Boolean classifier per class and predicts $\arg\max_k \tilde{f}_k(x)$.

> [!tip] Unlocked: Bias-Variance Tradeoff *(from Statistical Learning)*
> Increasing the number of basis functions $p$ moves the model along the **bias-variance tradeoff**: bias (systematic error from a too-simple model) decreases monotonically with $p$, while variance (sensitivity to the particular training sample) increases. Training error tracks bias-plus-square-bias-only, while test error tracks bias plus variance. The U-shaped test-error curve seen in validation is the classical signature of this tradeoff. In a Bayesian reading, model complexity is controlled by a prior; in a frequentist reading, by a regularization parameter. Both give the same picture: there is an optimal $p$ that balances the two failure modes.

> [!tip] Unlocked: Cross-[[Def - Validation (Training and Test Error)|Validation]] *(from Machine Learning)*
> The 5- or 10-fold cross-validation procedure introduced here is the standard model-selection technique throughout machine learning. It generalizes naturally to **nested cross-validation** (outer loop for performance estimation, inner loop for hyperparameter tuning) and to **leave-one-out CV** ($N$-fold with $N$ = sample size, useful when data is scarce). All these methods rest on the same logic: the only honest measure of generalization is predictive performance on data the model has never seen.

- **[[Ex - Polynomial fitting and overfitting]]** (⭐⭐)
	- Fit polynomials of degrees 0 through 20 to a small noisy dataset, and use a held-out test set to identify the degree that best balances bias and variance. The exercise drills the diagnostic: training error decreases monotonically with degree, but test error exhibits the canonical U-shape, with the minimum identifying the "right" model complexity.

- **[[Ex - Binary classifier via least squares]]** (⭐⭐)
	- On the Iris dataset (or any two-class problem), fit a least squares classifier $\mathrm{sign}(x^T \beta + v)$ distinguishing one species from the others. Compute the confusion matrix, vary the decision threshold $\alpha$ to trace the ROC curve, and verify that this simple method achieves a modest but real classification error rate.

> [!note] Exercise Index — §XI.2
> [[Exercise Index - §XI.2 Data Fitting and Classification]]

## §XI.3 Multi-Objective and Constrained Least Squares

- **[[Def - Multi-Objective Least Squares]]**
	- A multi-objective least squares problem has $k$ objectives $J_i = \|A_i x - b_i\|^2$ that we want simultaneously small. The standard approach minimizes the weighted sum $J = \lambda_1 J_1 + \cdots + \lambda_k J_k$ for positive weights $\lambda_i$. The minimizer is itself a least squares solution of a *single* problem with a stacked matrix $\tilde{A}$ and stacked right-hand side $\tilde{b}$, where $\tilde{A}$ vertically stacks $\sqrt{\lambda_i} A_i$ and $\tilde{b}$ stacks $\sqrt{\lambda_i} b_i$. As $\lambda$ varies, the solution traces the Pareto-optimal trade-off curve.

- **[[Def - Regularized Least Squares]]**
	- A regularized least squares problem is the multi-objective LS problem $\min \|Ax - b\|^2 + \lambda \|x - x_{\text{prior}}\|^2$ (Tikhonov form). The secondary objective expresses a prior assumption — that $x$ should be small, smooth, near a known reference vector, or otherwise "well-behaved" — and trades off fidelity to the data against this prior. The Tikhonov solution $\hat{x} = (A^T A + \lambda I)^{-1} A^T b$ is *always* well-defined, even when $A$ has linearly dependent columns or is wide, because $A^T A + \lambda I$ is invertible for any $\lambda > 0$.

- **[[Def - Constrained Least Squares]]**
	- A constrained least squares problem has the form $\min \|Ax - b\|^2$ subject to $Cx = d$. The constraint must be feasible (the rows of $C$ are linearly independent and consistent), and $A$ together with $C$ must satisfy a joint-rank condition. Geometrically, the solution is the projection of $b$ onto the column space of $A$ *restricted* to the affine [[Def - Subspace|subspace]] $\{x : Cx = d\}$. This generalizes least squares (no constraint, $C = 0$) and least norm (zero data, $A = I, b = 0$).

- **[[Def - KKT System]]**
	- The KKT system for constrained LS $\min \|Ax - b\|^2$ subject to $Cx = d$ is the augmented linear system $\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix}$. The $x$ block encodes optimality (gradient of the Lagrangian equals zero), the $\nu$ block encodes feasibility ($Cx = d$). This square system has $n + p$ equations in $n + p$ unknowns and is invertible iff (i) rows of $C$ are linearly independent and (ii) the stacked matrix $\binom{A}{C}$ has linearly independent columns. The same matrix structure governs all constrained-LS applications in §XI.4.

- **[[Thm - Constrained Least Squares via KKT System]]**
	- Under the conditions that $C$ has linearly independent rows and $\binom{A}{C}$ has linearly independent columns, the constrained LS problem has the unique solution given by the KKT system, with $\hat{x}$ being a linear function of $b$ and $d$. The proof has three parts: existence/uniqueness via Lagrange multipliers, direct verification via "completing the square" (no calculus needed), and computational implementation via either (i) solving the augmented KKT linear system directly or (ii) a QR-based algorithm of order $(m + p) n^2$ flops.

- **[[Thm - Bias-Variance Tradeoff in Regularized LS]]**
	- For Tikhonov regularization $\min \|Ax - b\|^2 + \lambda \|x\|^2$, the solution $\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b$ shrinks toward zero as $\lambda \to \infty$ and equals the unregularized LS solution as $\lambda \to 0^+$. The bias of the estimator (as a function of an unknown "true" $x^*$ generating the data) grows with $\lambda$, while the variance shrinks. There is an optimal $\lambda^*$ minimizing total mean squared error; in practice $\lambda^*$ is chosen by cross-validation. This is the mathematical content of "ridge regression as a regularizer of ordinary least squares."

> [!tip] Unlocked: Quadratic Programming *(from Optimization)*
> Constrained least squares is the simplest case of **quadratic programming (QP)**: minimize a convex quadratic $\frac{1}{2} x^T P x + q^T x$ subject to linear equality and/or inequality constraints. The equality-only case (this chapter) admits closed-form KKT solutions; adding inequality constraints requires iterative active-set or interior-point methods. The pattern carries: the KKT optimality conditions stay the same, with additional complementary-slackness conditions for the inequalities.

> [!tip] Unlocked: Lagrange Multipliers *(from Multivariate Analysis)*
> The KKT system is the linear-algebraic shadow of the **Lagrange multiplier method** for constrained optimization with smooth objectives. The Lagrangian $L(x, \nu) = f(x) + \nu^T (Cx - d)$ has stationarity $\nabla_x L = 0$ at any constrained optimum, which gives $\nabla f = -C^T \nu$ — the gradient of the objective is a linear combination of the gradients of the constraint functions. In our quadratic-objective setting, this stationarity equation is linear, and combining with feasibility $Cx = d$ produces exactly the KKT system. See [[Def - The Total Derivative and Differentiability]] for the smooth-objective foundation.

- **[[Ex - Tikhonov regularization is a multi-objective LS problem]]** (⭐)
	- Show that $\min \|Ax - b\|^2 + \lambda \|x\|^2$ is itself a standard least squares problem with stacked matrix $\tilde{A} = \binom{A}{\sqrt{\lambda}I}$ and stacked right-hand side $\tilde{b} = \binom{b}{0}$. Verify that $\tilde{A}^T \tilde{A} = A^T A + \lambda I$ is always invertible for $\lambda > 0$, regardless of properties of $A$.

> [!note] Exercise Index — §XI.3
> [[Exercise Index - §XI.3 Multi-Objective and Constrained Least Squares]]

## §XI.4 Constrained Least Squares Applications: Portfolio, LQR, Kalman

- **[[Def - Linear Quadratic Control]]**
	- Linear quadratic (LQ) control finds an input trajectory $u_1, \ldots, u_{T-1}$ for a linear dynamical system $x_{t+1} = A_t x_t + B_t u_t$ with output $y_t = C_t x_t$ that minimizes $J_{\text{output}} + \rho J_{\text{input}} = \sum \|y_t\|^2 + \rho \sum \|u_t\|^2$ subject to initial-state and (optionally) final-state constraints. The whole problem stacks as one large constrained least squares problem in the variable $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$. The KKT system has a *block-banded* structure because each dynamics constraint couples only consecutive time steps; exploiting this sparsity reduces the cost from $O(T^3)$ to $O(T)$.

- **[[Def - Linear Quadratic State Estimation]]**
	- Linear quadratic state estimation — the *Kalman filter* (in its batch, linear-algebra form) — recovers the state trajectory $x_1, \ldots, x_T$ of a linear dynamical system $x_{t+1} = A_t x_t + B_t w_t$ with noisy measurements $y_t = C_t x_t + v_t$, when only $y_t$ and the system matrices are observed. The formulation minimizes $\sum \|C_t x_t - y_t\|^2 + \lambda \sum \|w_t\|^2$ subject to the dynamics constraint. The parameter $\lambda$ trades trust in the measurements against trust in the dynamics model. Estimation is the *dual* of control: same KKT structure, opposite interpretation.

- **[[Ex - Portfolio optimization as constrained LS]]** (⭐⭐)
	- Given a $T \times n$ return matrix $R$ for $n$ assets over $T$ periods, find allocation weights $w$ with $1^T w = 1$ (budget constraint) and $\mu^T w = \rho$ (target return), minimizing the realized risk $\|Rw - \rho \mathbf{1}\|^2$. This is constrained LS with two scalar constraints; the KKT system is small ($n + 2$ equations). Sweeping $\rho$ traces the *efficient frontier*; the *two-fund theorem* says all efficient portfolios are affine combinations of any two of them.

- **[[Ex - Linear quadratic control via constrained LS]]** (⭐⭐⭐)
	- Set up the full LQR problem (linear dynamics, quadratic cost, initial and final state constraints) as a single constrained LS problem and solve via the KKT system. Verify that the resulting input trajectory drives the state from initial to final value while balancing input effort against output deviation; observe that the solution is linear in the initial and final states (foreshadowing *linear state feedback*).

- **[[Ex - Kalman state estimation as constrained LS]]** (⭐⭐⭐)
	- Set up the batch Kalman estimation problem (dynamics + noisy measurements) as a constrained LS problem and solve. Verify experimentally that small $\lambda$ over-trusts the measurements (estimated state is noisy), large $\lambda$ over-trusts the dynamics (estimated state is too smooth), and the value of $\lambda$ chosen by validation against held-out measurements gives a good estimate.

> [!tip] Unlocked: Optimal Control *(from Control Theory)*
> The LQ problem solved here is the **finite-horizon discrete-time LQR** — the entry point to a much larger theory. The infinite-horizon version reveals the *algebraic Riccati equation*; the continuous-time version is governed by Pontryagin's maximum principle; the stochastic version is **LQG** (linear quadratic Gaussian), which combines LQR with Kalman filtering and is *separation-principle-optimal* — you can design the estimator and controller independently and combine them. All these are linear-algebraic generalizations of the constrained-LS problem solved in this chapter.

> [!tip] Unlocked: Kalman-Bucy Filter *(from Stochastic Control)*
> The batch Kalman estimator here is the *least-squares* face of a deeper *Bayesian* object. In the stochastic framework, Gaussian noise and Gaussian priors make the conditional expectation $\mathbb{E}[x_t | y_1, \ldots, y_t]$ analytically tractable, and the recursive update rule is the **Kalman-Bucy filter**. The connection to this chapter is exact: under Gaussian assumptions, the maximum-a-posteriori (MAP) estimator coincides with the constrained least squares solution, and the recursive Kalman gain $K = P H^T (H P H^T + R)^{-1}$ is the recursive solver of the same linear system. See **Bayesian Linear Regression** for the static-parameter version of the same identification.

> [!tip] Unlocked: Mean-Variance Portfolio Theory *(from Math Finance)*
> Markowitz's 1953 portfolio theory is the constrained LS problem solved in §XI.4, with one twist: where Boyd uses *realized* historical returns to estimate risk via the sample covariance $R^T R / T$, classical Markowitz uses an *assumed* covariance matrix $\Sigma$ derived from a statistical model. The two-fund theorem (every efficient portfolio is an affine combination of any two efficient portfolios) is the same result either way. The deeper unifications — **CAPM**, factor models, the Sharpe ratio — all build on this least-squares skeleton.

> [!note] Exercise Index — §XI.4
> [[Exercise Index - §XI.4 Control and Estimation]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

The recurring proof targets in this chapter, gathered from the exercises, fall into a small number of patterns. First and most common: *existence-uniqueness of an optimizer*, typically proved by writing the gradient of the objective, setting it to zero, and checking that the resulting linear system is invertible. The exercises on the line fit, polynomial fitting, regularized regression, and portfolio optimization all reduce to this pattern. Second: *equivalence of two formulations*, typically showing that a problem stated as multi-objective LS is the same as a problem stated as single-objective LS with stacked matrices, or that a constrained problem is the limit of a regularized problem. The exercise on Tikhonov as multi-objective LS exemplifies this, as does the equivalence between two portfolio formulations. Third: *characterization of the solution as a linear function* of the data (the right-hand side $b$, or the constraint $d$); this lets us "precompute" solvers and is the foundation of linear state feedback and the matrix-inversion-lemma tricks. Fourth: *complexity bounds*, typically showing that an algorithm runs in $O(mn^2)$ or $O((m+p)n^2)$ flops, and that exploiting sparsity reduces this further; the LQR and Kalman complexity calculations are the canonical examples. Fifth: *qualitative behavior of the solution as a parameter varies* — the regularization path, the efficient frontier, the trade-off curve — typically requiring monotonicity arguments based on Pareto optimality.

**Sources — What assumptions do we usually leverage?**

Five recurring assumption patterns drive nearly every result in this chapter. (i) *Linear independence of the columns of $A$* (or, in constrained problems, of the stacked $\binom{A}{C}$); this is what makes the Gram matrix invertible and gives the closed-form solution. (ii) *Tall data matrix*: $m \geq n$, signalling an overdetermined system, hence a least-squares problem rather than an exact-solution problem. (iii) *Positive regularization weight* $\lambda > 0$; this is what makes the regularized problem well-posed even when the unregularized one is not. (iv) *Linear independence of the rows of $C$* in constrained problems; this is the feasibility condition — fewer constraints than variables, no redundancy among constraints. (v) *Linear dynamics* $x_{t+1} = A_t x_t + B_t u_t$ (or $+ B_t w_t$ in estimation); the linearity is what reduces a problem about trajectories to a problem about a single big vector $z$.

The *routes* between sources and targets are largely uniform: every existence-uniqueness target routes through invertibility of a Gram-type matrix, which routes through linear independence of columns. Every "linear function of the data" target routes through the explicit closed-form solution formula. Every complexity target routes through the QR factorization cost ($2mn^2$) plus a sparsity-exploitation argument. The pattern is striking: this chapter has one theorem proved many ways, with the variation being in *which* matrix happens to be $A$.

---

# Legal Operations

The operations below are the standard moves in solving any least-squares-flavored problem in this chapter. Many problems combine several; the key recognition skill is identifying which operations apply.

1. **Form the normal equations.** *Trigger:* unconstrained minimization of $\|Ax - b\|^2$. *Pattern:* set $A^T(Ax - b) = 0$, solve $A^T A x = A^T b$. Useful theoretically (cleanest derivation) but numerically dangerous (squares the condition number). See [[Thm - Least Squares via Normal Equations]].

2. **Use the QR factorization.** *Trigger:* you actually need to compute the LS solution. *Pattern:* factor $A = QR$, set $\hat{x} = R^{-1} Q^T b$ via back substitution. This is the numerically stable workhorse, $2mn^2$ flops. See [[Thm - Least Squares via QR Factorization]].

3. **Stack matrices to convert multi-objective LS to single-objective LS.** *Trigger:* weighted sum $\sum \lambda_i \|A_i x - b_i\|^2$. *Pattern:* form $\tilde{A}$ by stacking $\sqrt{\lambda_i} A_i$ vertically, $\tilde{b}$ by stacking $\sqrt{\lambda_i} b_i$. The resulting single-objective LS has the same minimizer.

4. **Recognize Tikhonov regularization as multi-objective LS.** *Trigger:* $\min \|Ax - b\|^2 + \lambda \|x\|^2$, or any quadratic-penalty term. *Pattern:* stack $A$ on top of $\sqrt{\lambda} I$; this is operation 3 specialized to $A_2 = I$, $b_2 = 0$.

5. **Build the KKT system for an equality-constrained problem.** *Trigger:* $\min \|Ax - b\|^2$ subject to $Cx = d$. *Pattern:* form the Lagrangian $L = \|Ax - b\|^2 + \nu^T(Cx - d)$, set partials to zero, write the resulting linear system as $\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \binom{x}{\nu} = \binom{2 A^T b}{d}$. Solve directly. See [[Thm - Constrained Least Squares via KKT System]].

6. **Apply the orthogonality principle to verify or characterize an LS solution.** *Trigger:* you want to check whether a candidate $\hat{x}$ is the LS solution, or to bound the optimal residual. *Pattern:* check that $A^T(A\hat{x} - b) = 0$, i.e., the residual is orthogonal to every column of $A$. This is the algebraic form of "the projection is the closest point."

7. **Complete the square to verify an LS minimizer without calculus.** *Trigger:* you want a clean direct proof, possibly because the calculus argument is opaque or you doubt regularity. *Pattern:* write $\|Ax - b\|^2 = \|A(x - \hat{x}) + (A\hat{x} - b)\|^2$, expand, use the orthogonality of the cross term to get $\|Ax - b\|^2 = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2$, and conclude the right-hand side is minimized at $x = \hat{x}$.

8. **Use the pseudoinverse to write the solution in one line.** *Trigger:* you want a compact formula or you want to handle the rank-deficient case. *Pattern:* $\hat{x} = A^\dagger b$ (or $A^+ b$ in the rank-deficient/SVD sense). When $A$ has linearly independent columns, $A^\dagger = (A^T A)^{-1} A^T$; in general $A^+ = V \Sigma^+ U^*$ via [[Thm - Singular Value Decomposition]]. See [[Def - Pseudoinverse]].

9. **Split-and-validate to choose a regularization parameter $\lambda$.** *Trigger:* a regularized LS problem with a free $\lambda$, where you do not know which value to use. *Pattern:* split the data into training and test sets (or use cross-validation), fit on the training set for a range of $\lambda$ values, evaluate the test RMS error for each, pick the $\lambda$ that minimizes test error (or a slightly larger one for simplicity).

10. **Exploit sparsity in time-series LS problems.** *Trigger:* a control or estimation problem with $T$ time steps. *Pattern:* the KKT matrix has block-banded sparsity because each dynamics constraint couples only consecutive time steps. A banded LU or QR solve costs $O(T)$ instead of the naïve $O(T^3)$. The Kalman filter's recursive form is this exploitation written sequentially.

11. **Set up "one-versus-rest" for multi-class classification.** *Trigger:* a $K$-class classification problem. *Pattern:* fit $K$ binary classifiers $\tilde{f}_k$, each distinguishing class $k$ from the rest. Predict $\hat{y} = \arg\max_k \tilde{f}_k(x)$. The $K$ least squares problems share the same matrix $A$, so the QR factorization is computed only once.

**Illegal but tempting operations:**

> [!warning] 1. Solving the normal equations $A^T A x = A^T b$ as your default algorithm.
> It is tempting because it is one line of math and looks computationally simple. But forming $A^T A$ squares the condition number $\kappa(A)$ — if $\kappa(A) = 10^5$ (perfectly reasonable for a real data matrix), then $\kappa(A^T A) = 10^{10}$, and a double-precision Cholesky factorization can lose half its digits. Concrete counterexample: the **Vandermonde matrix** for polynomial fitting at evenly spaced points has condition number that grows exponentially with the polynomial degree; for degree 15, the QR method works, the normal-equations method gives garbage. **Becomes legal when:** $A$ is well-conditioned (small $\kappa(A)$) and you can afford to lose a few digits, or when you are working theoretically and not numerically.

> [!warning] 2. Trusting low training error as evidence of a good model.
> A high-capacity model with many parameters can drive training error to zero by memorizing the training set; this gives no information about its performance on new data. Concrete counterexample: a 20-degree polynomial fit to 21 noisy data points has zero training error but oscillates wildly between the points and predicts catastrophically on a held-out test set. **Becomes legal when:** you have validated the model on a held-out test set or via cross-validation, and the test error is comparable to the training error.

> [!warning] 3. Treating the constrained LS problem $\min \|Ax - b\|^2$ s.t. $Cx = d$ as if you could just stack and ignore the constraint.
> If you naïvely stack $\binom{A}{\sqrt{\lambda} C}$ with $\lambda$ large, you only *approximate* satisfaction of the constraint — for any finite $\lambda$, $Cx \neq d$ in general. Concrete counterexample: in portfolio optimization with $1^T w = 1$ as a budget constraint, treating this as a soft penalty with $\lambda = 10^4$ gives a portfolio whose budget is off by a tiny amount, but that tiny amount can flip the sign of leverage in a low-margin situation. **Becomes legal when:** you actually solve the KKT system (with the constraint as an equality block), or in the limit $\lambda \to \infty$ the soft formulation converges to the constrained one.

> [!warning] 4. Using the same data to train the model and to choose the regularization parameter $\lambda$.
> Picking the $\lambda$ that minimizes training error is meaningless — training error always decreases as $\lambda$ decreases (less regularization, better fit on the training data). The minimizing $\lambda$ is always $\lambda = 0$, recovering ordinary LS with all its overfitting pathologies. Concrete counterexample: fitting a 15-degree polynomial with $\lambda$ chosen to minimize training error reproduces the catastrophic overfit from the unregularized case. **Becomes legal when:** $\lambda$ is chosen on a held-out validation set, separately from both the training set and the final test set.

> [!warning] 5. Forgetting the "future returns are similar to past returns" assumption in portfolio optimization.
> The portfolio LS problem uses the *realized* historical returns as if they were the relevant distribution; this is a model-fit on past data assumed to predict future. Markets shift — a portfolio efficient over the 2010s may be inefficient or even ruinous over the 2020s. Concrete counterexample: any portfolio optimized on pre-2008 historical data heavily weighted financials, which then crashed. **Becomes legal when:** you back-test the strategy on out-of-sample historical periods, accept stationarity as an assumption, and incorporate regularization (e.g., shrinkage of the sample covariance) to reduce sensitivity to estimation noise.

---

# Problem-Solving Strategy

The unifying question of this chapter is: *given a quadratic objective and linear structure, how do you find the optimum, and what does the optimum tell you?* All exercises route through some version of "set the gradient to zero, solve a linear system." The skill is in recognizing the version.

When you encounter an unconstrained problem of the form "minimize $\|Ax - b\|^2$", the route is direct: this is a basic LS problem, and the QR-factorization solver gives the answer. The only judgment call is whether to also compute the SVD (when $A$ might be rank-deficient), use the normal equations (almost never the right choice in practice), or exploit sparsity (when $A$ is large and structured).

When you encounter a problem with *two* objectives that are both quadratic in $x$, recognize multi-objective LS. Stack the matrices with $\sqrt{\lambda_i}$ weights, and you are back to a basic LS problem. The only judgment is the weight $\lambda$, which is chosen by validation when one of the objectives is a regularization term, or by problem-context tuning otherwise.

When you encounter an *equality constraint* of the form $Cx = d$, build the KKT system. The augmented matrix $\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix}$ is square and invertible under the joint linear-independence condition; solve it for $(x, \nu)$. The Lagrange multipliers $\nu$ are usually not interesting in themselves, but they are *necessary* to satisfy the constraint exactly. Approximating with a large soft penalty is the most common error.

For *time-series problems* — control, estimation — the constrained-LS structure is hidden inside a big stacked variable $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$. The dynamics equations $x_{t+1} = A_t x_t + B_t u_t$ become a sparse band of equality constraints, the initial-state and final-state conditions become additional equality constraints, and the objective becomes a quadratic in $z$. The whole problem is a single big constrained LS problem, and the KKT matrix is block-banded. The recursive Kalman algorithm and the LQR Riccati equation are both efficient *sparse solvers* of this same KKT system.

The diagnostic for *overfitting* is the gap between training and test error. A model with low training error and high test error is overfit (too many parameters relative to data); a model with high training and high test error is underfit (too few parameters); a model with low training error and similar low test error is healthy. The two remedies are: (i) reduce model complexity (use fewer features), or (ii) keep features but regularize (penalize $\|\theta\|$). Both move the model along the bias-variance tradeoff toward lower variance; regularization is often easier than principled feature selection.

The unifying meta-strategy is to recognize that every problem in this chapter is the same problem — *minimize a quadratic in $x$ subject to optionally some linear constraints* — and that the answer is always given by a single linear system whose matrix is built from $A^T A$ and $C^T$ blocks. Once you see this, the chapter has one theorem, deployed in twelve different ways.

---

# Most Reusable Properties

- **[[Thm - Least Squares via QR Factorization|QR-based LS solver]]**: $\hat{x} = R^{-1} Q^T b$ when $A = QR$. **Typical use:** the default numerical recipe whenever you need to solve a least squares problem in practice. It is the right answer to "how do I compute $\hat{x}$" 95% of the time. The QR factorization is reusable: if the right-hand side $b$ changes but $A$ stays fixed (as in matrix least squares, or in one-versus-rest multi-class classification), the factorization is computed once and applied many times.

- **[[Thm - Constrained Least Squares via KKT System|KKT system for constrained LS]]**: $\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \binom{x}{\nu} = \binom{2 A^T b}{d}$. **Typical use:** every equality-constrained quadratic problem in the chapter — portfolio optimization, LQR, Kalman estimation — *is* a KKT system. Recognizing this in a new problem turns it into a standard solve. The block-banded version (when constraints couple only adjacent time steps) is the basis of all efficient algorithms in §XI.4.

- **Tikhonov regularization formula**: $\hat{x} = (A^T A + \lambda I)^{-1} A^T b$. **Typical use:** any time you suspect overfitting or rank deficiency, this formula gives a well-defined answer for any $\lambda > 0$, even when $A^T A$ alone is singular. It is the practical fallback when ordinary LS fails or warns, and it has a Bayesian interpretation as the MAP estimator under a Gaussian prior on $x$ — connecting LS directly to **Bayesian Linear Regression**.

- **The orthogonality principle**: $A^T(A\hat{x} - b) = 0$, equivalently $A\hat{x}$ is the orthogonal projection of $b$ onto $\mathrm{col}(A)$. **Typical use:** this is the *geometric* characterization of the LS solution, and it is the tool for proving that a candidate $\hat{x}$ is optimal without doing calculus. It is also the characterization that lets [[Thm - Best Approximation by Orthogonal Projection]] from abstract inner product space theory translate into Boyd's concrete algorithms.

- **Linear-in-data property**: $\hat{x}$ is a linear function of $b$ (and of $d$ in constrained problems). **Typical use:** this is what makes precomputed solvers possible — factor the KKT matrix once, apply to many right-hand sides — and what underpins linear state feedback in LQR. It is also what makes Bayesian linear regression analytically tractable: posterior over $x$ is linear-Gaussian in the observations.

---

# Bridges

- **Inner product spaces and orthogonal projection ([[Linear Algebra VI — §6 Inner Product Spaces]]).** Boyd's least squares problem is the abstract orthogonal-projection theorem from Hilbert space theory made concrete. The statement "the closest point in $\mathrm{col}(A)$ to $b$ is the orthogonal projection of $b$ onto $\mathrm{col}(A)$" is [[Thm - Best Approximation by Orthogonal Projection]] in disguise — but where LADR proves it abstractly for any inner product space, Boyd makes it computational by giving the explicit formula $A\hat{x} = A(A^T A)^{-1} A^T b$. The projection operator $P = A(A^T A)^{-1} A^T$ satisfies $P^2 = P$ and $P^T = P$, the algebraic characterization of an orthogonal projection (see [[Def - Orthogonal Projection]]). The residual $b - A\hat{x} = (I - P)b$ lives in $\mathrm{col}(A)^\perp$, exactly the orthogonal-decomposition statement.

- **QR factorization and SVD ([[Linear Algebra VII — §7 Operators on Inner Product Spaces]]).** The QR factorization $A = QR$ from LADR is the practical engine of Boyd's LS solver. The columns of $Q$ are an orthonormal basis for $\mathrm{col}(A)$, obtained by [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] from the columns of $A$; the upper-triangular $R$ records the change-of-basis coefficients. The LS solution then becomes $\hat{x} = R^{-1} Q^T b$, computable by one matrix-vector multiply and one triangular solve. The [[Thm - Singular Value Decomposition|SVD]] provides the broader [[Def - Pseudoinverse|pseudoinverse]] $A^+ = V \Sigma^+ U^*$, which extends LS to rank-deficient and wide matrices: the SVD-based LS solver gives the minimum-norm solution when there are multiple LS solutions, generalizing $A^\dagger$ to every matrix.

- **The pseudoinverse ([[Def - Pseudoinverse]]).** Boyd writes $\hat{x} = A^\dagger b$, recognizing the pseudoinverse as the LS solver. When $A$ has linearly independent columns, $A^\dagger = (A^T A)^{-1} A^T$ is a left inverse. When $A$ has linearly independent rows (wide $A$), $A^\dagger = A^T(AA^T)^{-1}$ is a right inverse and solves the least-norm problem $\min \|x\|$ subject to $Ax = b$. In the general rank-deficient case, the SVD-based pseudoinverse $A^+$ from [[Thm - Singular Value Decomposition|SVD]] is the universal LS solver, always returning the minimum-norm minimizer of $\|Ax - b\|$. The bridge to LADR's abstract pseudoinverse machinery is exact: same object, two computational routes (QR or SVD), one unifying geometric interpretation (projection onto the column space).

- **Statistics — Linear Regression.** Least squares is the maximum-likelihood estimator under the assumption that the residuals are i.i.d. Gaussian. If $y = X\beta + \epsilon$ with $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$, then the log-likelihood is $-\frac{1}{2\sigma^2} \|y - X\beta\|^2$ plus a constant, and maximizing it is exactly minimizing the LS objective. This is why **Linear Regression** in statistics shares the formula $\hat{\beta} = (X^T X)^{-1} X^T y$ with Boyd's LS solver — and why the standard error of the regression coefficients, the $t$-statistics, the $R^2$ value, and the F-test all flow naturally once you accept the Gaussian-noise assumption. The bridge tells you that what statisticians call "OLS" is what numerical analysts call "least squares," and the formal machinery (sampling distributions, confidence intervals) is the *probabilistic upgrade* of the geometric setup here.

- **Bayesian Linear Regression.** Tikhonov regularization is *maximum a posteriori* (MAP) estimation under a Gaussian prior on the parameter $x$. If we assume $y = Ax + \epsilon$ with $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$ and a prior $x \sim \mathcal{N}(0, \tau^2 I)$, then the posterior mean (and mode) is $\hat{x} = (A^T A + (\sigma^2/\tau^2) I)^{-1} A^T y$ — exactly Tikhonov with $\lambda = \sigma^2/\tau^2$. The bias of the estimator (toward the prior mean zero) is a feature, not a bug: it expresses the prior belief that $x$ should be small. The regularization parameter $\lambda$ has a Bayesian interpretation as the *ratio of noise variance to prior variance*. This bridge is one of the cleanest connections between numerical linear algebra and probability theory, and it provides a principled way to choose $\lambda$ in problems where prior knowledge can be quantified.

- **Algorithmic information theory and minimum description length.** Regularization is the linear-algebra shadow of *Occam's razor*: prefer simpler models over more complex ones. In algorithmic information theory, the "complexity" of a model is its description length (or Kolmogorov complexity); in regularized LS, complexity is the norm $\|\theta\|^2$. Both pick out shorter / smaller models as a way to control overfitting, and both can be derived from a Bayesian setting with a prior favoring simple hypotheses. The Bayesian information criterion (BIC) and Akaike information criterion (AIC) are explicit penalties on model size that play the same role as $\lambda \|\theta\|^2$.

- **Group theory and the structure of solutions ([[Def - Group]]).** A subtle bridge: the set of solutions to $Ax = b$ when one solution exists is a coset of the kernel $\ker A = \{x : Ax = 0\}$ — and cosets of a subgroup of $(\mathbb{R}^n, +)$ are exactly the objects [[Def - Coset|cosets]] describes. In the rank-deficient LS problem, the set of *least-squares solutions* is a coset of $\ker A$ within $\mathbb{R}^n$, parametrized by the choice of element in this coset. The pseudoinverse picks out the minimum-norm element. This is the linear-algebraic instance of a more general fact: when a structure has a "kernel-and-quotient" decomposition (as in [[Thm - First Isomorphism Theorem|the first isomorphism theorem]]), solution sets to inverse problems naturally have coset structure.

---

# Insights

**The unifying frame.** Every problem in this chapter is the projection of $b$ onto the column space of some matrix $A$, possibly intersected with an affine subspace of constraints. The "matrix $A$" varies — sometimes it is a data matrix, sometimes a stack of dynamics matrices, sometimes a Gram-weighted concatenation — but the operation is always orthogonal projection. This is the geometric content of LS, and it is what makes the chapter feel like one theorem in twelve disguises: there is genuinely *one* geometric move (project onto a subspace), one algebraic representation of that move (solve a linear system), and one stable numerical algorithm (QR factorization). Once you see this, the rest is recognition: figuring out what $A$, $b$, $C$, $d$ are in any given problem.

**The true name of "least squares."** The "true name" is *orthogonal projection*. The formula $\hat{x} = (A^T A)^{-1} A^T b$ is operationally useful but conceptually opaque; the orthogonality principle $A^T(A\hat{x} - b) = 0$ is the same content stated as the actual geometric fact. When checking whether a candidate is the LS solution, the orthogonality principle is the test. When characterizing the LS solution in a new context (rank-deficient, constrained, regularized), the orthogonality principle generalizes; the formula doesn't. The formula is the "official" definition; the orthogonality principle is the operational one.

**The true name of "regularization."** The "true name" is *prior*. A regularization term $\lambda \|x\|^2$ added to an LS objective is exactly the log-density of a Gaussian prior on $x$ (up to constants); the resulting MAP estimator is exactly the regularized LS solution. This is why regularization works — it incorporates information beyond the data — and why $\lambda$ has a principled interpretation (the ratio of noise variance to prior variance). The bridge to **Bayesian Linear Regression** is exact, not analogical.

**A trigger-reaction pattern: "overdetermined → LS."** Whenever you see a tall matrix $A$ ($m \geq n$) and a system $Ax \approx b$ that you do not expect to be consistent, the reaction is "least squares." This is the most common application of LS in practice — you have $m$ noisy measurements of an $n$-parameter model and you want the best fit. The trigger is "more equations than unknowns"; the reaction is "minimize $\|Ax - b\|^2$."

**A trigger-reaction pattern: "underdetermined with constraints → constrained LS (KKT)."** When you have *fewer* equations than unknowns ($A$ wide), $Ax = b$ has infinitely many solutions; the reaction is to add a secondary criterion (typically "minimize $\|x\|^2$") and solve as a constrained LS or least-norm problem. The KKT system is the universal tool. This pattern shows up in portfolio optimization (constraints + objective), control (dynamics constraints + cost objective), and estimation (dynamics constraints + measurement objective).

**A trigger-reaction pattern: "fitting overfits → add regularization (Tikhonov)."** When training error is small but test error is large, the model is overfit and the immediate remedy is regularization. Add $\lambda \|x\|^2$ to the objective, sweep $\lambda$ on a logarithmic grid, pick the value that minimizes test error. This is the most reliable single fix for the most common failure mode in least squares modelling.

**A trigger-reaction pattern: "high training error → not enough features; high test error with low training error → too many features."** The bias-variance tradeoff has a clean operational signature in the training/test error gap. If both are high, the model lacks capacity; add features or use a more flexible basis. If training is low but test is high, the model has too much capacity (or too little regularization); remove features or increase $\lambda$. If both are low, the model is correctly calibrated.

**A trigger-reaction pattern: "competing objectives → multi-objective LS with scan over $\lambda$."** Whenever you have two desiderata in tension — accuracy vs. simplicity, fit vs. smoothness, return vs. risk — the standard move is to write the weighted sum, sweep the weight on a logarithmic grid, and trace out the Pareto front. The qualitative shape (steep at one end, flat at the other) gives you visual diagnostic of where the natural tradeoff lies. This applies to portfolio optimization (return vs. risk), LQR (output vs. input effort), and regularized fitting (RSS vs. parameter norm) — three "different" problems with one shared methodology.

**Inheritance — where does invertibility of the KKT matrix come from?** The invertibility of the augmented $\begin{pmatrix} A^T A & C^T \\ C & 0 \end{pmatrix}$ is *inherited* from two separate properties: (i) linear independence of the rows of $C$ (otherwise the constraint set is overdetermined or redundant), and (ii) linear independence of the columns of $\binom{A}{C}$ (otherwise the joint problem is underdetermined). Neither property alone suffices; both are needed. This is a pattern that recurs in any joint-constraint problem: a unique solution requires both that the constraints be non-redundant *and* that they together with the objective uniquely identify the unknown.

**Why does the same KKT structure govern portfolio, control, and estimation?** The reason is *Lagrangian duality*: any equality-constrained quadratic minimization has the form $\min x^T P x + q^T x$ s.t. $Cx = d$, and the KKT optimality conditions are linear. The "different" problems differ in *what* $P$, $q$, $C$, $d$ are, but the *form* of the solution is the same: solve a single linear system. The three applications of §XI.4 are not three separate techniques; they are three substitutions into one formula. Recognizing this turns the chapter from a list of disconnected applications into one unified theory with three case studies.
