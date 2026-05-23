---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Multi-Objective Least Squares"
  - "Def - Validation (Training and Test Error)"
tags: [algebra, linear-algebra, applied, optimization, regularization]
---

# Notation

In the Tikhonov regularization setting, $A$ is the data matrix (typically $N \times p$ with $N$ data points and $p$ features), $b$ is the target vector ($y^d$ in data-fitting), $\lambda > 0$ is the *regularization parameter*. The *regularized LS solution* is denoted $\hat{x}(\lambda)$ to emphasize its dependence on $\lambda$. The *regularization path* is the trajectory $\{\hat{x}(\lambda) : \lambda > 0\}$ in parameter space. The *bias* of $\hat{x}(\lambda)$ as an estimator of an unknown "true" $x^*$ is $\mathbb{E}[\hat{x}(\lambda)] - x^*$; the *variance* is $\mathbb{E}\|\hat{x}(\lambda) - \mathbb{E}[\hat{x}(\lambda)]\|^2$.

When the first column of $A$ is the constant vector $\mathbf{1}$ (the intercept term), regularization typically penalizes only $\theta_{2:p}$ — the non-intercept parameters; this is called *ridge regression* in statistics.

---

# Axiom Motivation

Regularization solves an empirical problem: ordinary least squares overfits, especially when the number of features $p$ is large or the design matrix $A$ is ill-conditioned. The signature is the training/test error gap: training error is much smaller than test error, indicating that the fitted parameters $\hat{\theta}$ depend too sensitively on the particular training data and do not generalize.

The diagnosis: when $A^T A$ is nearly singular (e.g., near-collinear features, or $p \approx N$), its inverse is large, and small perturbations in $b$ produce large perturbations in $\hat{x} = (A^T A)^{-1} A^T b$. The LS solution is *high-variance*: sensitive to noise in the training data.

The remedy: shrink $\hat{x}$ toward zero (or toward some other reference point) by *adding a penalty* on its norm. The simplest form, due to Tikhonov, is
$$\min_x \|Ax - b\|^2 + \lambda \|x\|^2.$$
This is a multi-objective LS problem (see [[Def - Multi-Objective Least Squares]]) with two objectives: data fidelity $\|Ax - b\|^2$ and parameter norm $\|x\|^2$, weighted by $\lambda$. As $\lambda$ increases from $0$ to $\infty$, the solution interpolates from the unregularized LS solution to zero.

Why does this work? Two complementary explanations.

*Numerical stability.* The regularized normal equation system $(A^T A + \lambda I) x = A^T b$ has matrix $A^T A + \lambda I$, which is positive definite for any $\lambda > 0$, *even when $A^T A$ alone is singular*. The smallest eigenvalue is shifted up by $\lambda$, so the condition number is bounded above by $(\sigma_{\max}^2 + \lambda)/\lambda$ where $\sigma_{\max}$ is the largest singular value of $A$. As $\lambda \to \infty$, the condition number approaches 1 — perfectly conditioned. As $\lambda \to 0^+$, the condition number approaches the unregularized value, possibly very large. So regularization buys numerical stability monotonically with $\lambda$.

*Bias-variance tradeoff.* As an estimator of an unknown "true" parameter $x^*$ (assuming $b = A x^* + \text{noise}$), $\hat{x}(\lambda)$ has bias proportional to $\lambda$ (it is shrunk toward zero, away from $x^*$, by an amount that grows with $\lambda$) and variance that decreases with $\lambda$ (the shrinkage makes it less sensitive to noise). The mean squared error $\mathbb{E}\|\hat{x}(\lambda) - x^*\|^2$ has a U-shape in $\lambda$: zero at $\lambda = 0$ (but with large variance), large at $\lambda \to \infty$ (large bias toward zero). The minimum MSE is at some $\lambda^* > 0$. This is the classical bias-variance tradeoff, made precise by the explicit ridge-regression formula.

The Bayesian interpretation is illuminating: if we assume $b = Ax + \epsilon$ with $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$ and a Gaussian prior $x \sim \mathcal{N}(0, \tau^2 I)$, then the MAP estimator is
$$\hat{x}_{\text{MAP}} = \arg\max_x p(x | b) = \arg\min_x \frac{1}{2\sigma^2}\|Ax - b\|^2 + \frac{1}{2\tau^2}\|x\|^2.$$
This is Tikhonov regularization with $\lambda = \sigma^2 / \tau^2$. The *bias toward zero* is exactly the prior assumption that $x$ is "small" with typical scale $\tau$. The regularization parameter has a principled probabilistic interpretation: the ratio of noise variance to prior variance. The bridge to **Bayesian Linear Regression** is exact.

The further generalizations:

(i) *Regularization toward a non-zero target.* Replace $\|x\|^2$ with $\|x - x_{\text{prior}}\|^2$ when prior information suggests a specific reference value (not zero). The Bayesian interpretation: a Gaussian prior centered at $x_{\text{prior}}$ rather than at zero.

(ii) *Weighted regularization.* Use $\|Dx\|^2$ for some weighting matrix $D$ — e.g., $D$ = first-difference matrix to penalize roughness (smoothness regularization), or $D$ = incidence matrix of a graph to penalize variation across the graph (Laplacian regularization for tomography and image processing).

(iii) *Norm choice.* L1 regularization $\lambda \|x\|_1$ (LASSO) produces *sparse* solutions (many $\hat{x}_i = 0$) — useful for feature selection but breaks the LS framework (non-quadratic penalty). L2 (this definition) does not produce sparsity but is closed-form. The choice between L1 and L2 depends on whether sparsity is desired.

The *choice of $\lambda$* is the practical art. Cross-[[Def - Validation (Training and Test Error)|validation]] gives a principled procedure: fit on training data for a grid of $\lambda$ values (typically logarithmic, $\lambda \in \{10^{-4}, 10^{-3}, \ldots, 10^{4}\}$), evaluate test error on held-out data, pick the $\lambda$ minimizing test error. When ties exist, choose the *largest* $\lambda$ among the near-minimum, on the principle that "simpler is better."

---

# The Definition

> **Definition (Regularized Least Squares).** Given an $m \times n$ matrix $A$, an $m$-vector $b$, a regularization parameter $\lambda > 0$, and (optionally) a reference vector $x_{\text{prior}}$ and weighting matrix $D$, the *regularized least squares problem* is to find $\hat{x}$ minimizing
> $$\|Ax - b\|^2 + \lambda \|D(x - x_{\text{prior}})\|^2.$$
> The *Tikhonov* (or *ridge regression*) case is $D = I$ and $x_{\text{prior}} = 0$:
> $$\hat{x}(\lambda) = \arg\min_x \|Ax - b\|^2 + \lambda \|x\|^2 = (A^T A + \lambda I)^{-1} A^T b.$$
> The matrix $A^T A + \lambda I$ is positive definite for any $\lambda > 0$, so the solution exists and is unique *regardless* of the properties of $A$ alone (it can be wide, tall, or rank-deficient).
>
> The *regularization path* is the curve $\{\hat{x}(\lambda) : \lambda > 0\} \subset \mathbb{R}^n$. As $\lambda \to 0^+$, $\hat{x}(\lambda)$ approaches the unregularized LS solution (when defined) or the SVD-based minimum-norm LS solution. As $\lambda \to \infty$, $\hat{x}(\lambda) \to 0$ (or $\to x_{\text{prior}}$ in the general case).

---

# Relate to Other Fields / Compression

**True name:** regularized LS is *maximum a posteriori (MAP) estimation* under a Gaussian prior on the parameter $x$. The data-fidelity term is the negative log-likelihood; the regularization term is the negative log-prior; the regularization parameter is the noise-to-prior variance ratio. This is the Bayesian interpretation, and it makes the otherwise-arbitrary choice of $\lambda$ principled.

This is the same construction as:
- **Tikhonov Regularization** (numerical analysis): the classical term in inverse-problems theory, where regularization is essential to make ill-posed problems well-posed.
- **Ridge Regression** (statistics): the same procedure under a different name; common usage distinguishes regularization-of-the-intercept (Tikhonov includes it, ridge typically excludes it).
- **Shrinkage Estimation** (statistics): a broader concept including the James-Stein estimator and empirical Bayes; the connection is that all shrinkage estimators bias the parameter toward some reference value to reduce variance.
- **Weight Decay** (deep learning): adding $\lambda \|\theta\|^2$ to the loss function of a neural network is called weight decay. The justification is the same: control variance by penalizing parameter norm.
- **Penalized Likelihood** (statistics): generalizes ridge to non-Gaussian likelihoods (e.g., logistic-with-ridge). The penalty term is still $\lambda \|\theta\|^2$ (or $\|D\theta\|^2$), but the data term is the appropriate log-likelihood.

---

# Examples / Corollaries

*Example 1 (curing rank deficiency).* If $A$ is rank-deficient (e.g., has a repeated column), $A^T A$ is singular and the unregularized LS problem has infinitely many solutions. Adding $\lambda I$ for any $\lambda > 0$ makes $A^T A + \lambda I$ invertible; the regularized solution picks out the *unique minimum-norm* LS minimizer as $\lambda \to 0^+$. So Tikhonov regularization is also a *way to handle rank-deficient problems*.

*Example 2 (wide $A$).* If $A$ is wide ($m < n$, more unknowns than equations), the system $Ax = b$ has infinitely many solutions and the unregularized LS objective is identically zero on the entire affine [[Def - Subspace|subspace]] of solutions. The regularized solution $\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b$ for any $\lambda > 0$ is uniquely defined. The kernel-trick identity $(A^T A + \lambda I)^{-1} A^T = A^T (A A^T + \lambda I)^{-1}$ lets you compute this efficiently for wide $A$ (the $m \times m$ matrix $A A^T + \lambda I$ is smaller than the $n \times n$ matrix $A^T A + \lambda I$).

*Example 3 (smoothness regularization).* For a signal $x$ that we believe should be smooth, regularize with $\|Dx\|^2$ where $D$ is the first-difference matrix. The objective $\|x - y\|^2 + \lambda \|Dx\|^2$ has solution that interpolates between $y$ (at $\lambda \to 0$) and a constant (at $\lambda \to \infty$). The regularization implements the prior assumption "$x$ varies slowly."

*Example 4 (is NOT regularization in the LS sense — L1/LASSO).* The LASSO objective $\|Ax - b\|^2 + \lambda \|x\|_1$ is *not* an LS problem because of the L1 penalty. Its solution requires non-smooth convex optimization (coordinate descent, ADMM) and the regularization path is piecewise linear with breakpoints where individual coordinates of $\hat{x}$ "activate" or "deactivate." LASSO produces sparse solutions that pure Tikhonov cannot.

*Example 5 (Bayesian interpretation).* If $b = Ax^* + \epsilon$ with $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$ and $x \sim \mathcal{N}(0, \tau^2 I)$, then the posterior is $x | b \sim \mathcal{N}(\hat{x}(\lambda), \Sigma_{\text{post}})$ with $\lambda = \sigma^2/\tau^2$ and $\Sigma_{\text{post}} = \sigma^2 (A^T A + \lambda I)^{-1}$. The Tikhonov solution is the posterior mean, and the posterior covariance quantifies uncertainty. This is the basis of **Bayesian Linear Regression**.

**Calibration check.** Verify: (i) $\hat{x}(\lambda = 0) = (A^T A)^{-1} A^T b$ recovers ordinary LS (when defined); (ii) $\hat{x}(\lambda) \to 0$ as $\lambda \to \infty$ (the regularization eventually dominates); (iii) when $A$ is square and invertible with $\lambda = 0$, $\hat{x} = A^{-1} b$ — the exact solution; (iv) for SVD $A = U \Sigma V^T$, the Tikhonov solution becomes $\hat{x}(\lambda) = V \Sigma_\lambda^+ U^T b$ where $\Sigma_\lambda^+$ has diagonal entries $\sigma_i / (\sigma_i^2 + \lambda)$ — the *filtered [[Def - Pseudoinverse|pseudoinverse]]*, with small singular values shrunk away from infinity.

---

# Unlocked by This

> [!tip] Bayesian Linear Regression *(from Bayesian Statistics)*
> Tikhonov regularization is the MAP estimator of the **Bayesian linear regression** model with Gaussian prior $x \sim \mathcal{N}(0, \tau^2 I)$ and Gaussian likelihood $b | x \sim \mathcal{N}(Ax, \sigma^2 I)$. The full posterior is Gaussian, $x | b \sim \mathcal{N}(\hat{x}(\lambda), \Sigma_{\text{post}})$, providing not just a point estimate but a full uncertainty quantification. The regularization parameter $\lambda = \sigma^2/\tau^2$ has the principled interpretation of the *noise-to-signal precision ratio*. Hyperparameter estimation (estimating $\lambda$ from the data, by empirical Bayes or hierarchical priors) gives a fully principled procedure that recovers cross-validation as a special case.

> [!tip] Gaussian Processes *(from Bayesian ML)*
> The infinite-dimensional generalization of Bayesian linear regression is **Gaussian process regression**, where the prior is over functions rather than parameters. The kernel function plays the role of the prior covariance, and the GP posterior gives both a mean (point prediction) and a covariance (uncertainty). Regularized LS is the finite-dimensional restriction of GP regression to a finite basis. The connection makes GP regression "regularization with infinite features and an explicit kernel."

> [!tip] LASSO and Sparse Regression *(from High-Dimensional Statistics)*
> Replacing the L2 penalty $\|x\|^2$ with L1 $\|x\|_1$ gives the **LASSO** estimator, which produces *sparse* solutions (many $\hat{x}_i = 0$). The L1 penalty performs *feature selection* implicitly. The downside is that the LASSO problem is no longer LS and requires iterative optimization. The regularization path now has breakpoints, and computing the entire path is a more delicate (but well-studied) problem. Modern variants — elastic net (L1 + L2), group LASSO, fused LASSO — all extend the regularized-LS framework into sparse modeling.

> [!tip] Weight Decay in Neural Networks *(from Deep Learning)*
> Adding $\lambda \|\theta\|^2$ to a neural network's loss function is called **weight decay** and is the deep-learning incarnation of Tikhonov regularization. It controls the magnitude of network weights, reduces overfitting on the training set, and (in modern networks) interacts subtly with optimization dynamics. The conceptual justification — penalize parameter norm to reduce variance — is identical to the ridge-regression motivation here.
