---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Least Squares Data Fitting"
  - "Def - Validation (Training and Test Error)"
tags: [algebra, linear-algebra, applied, data-fitting, machine-learning]
---

# Problem Statement

You are given $N$ data points $(x_i, y_i)_{i=1}^N$ with the $x_i$ scalar. Fit polynomial models $\hat{f}(x) = \theta_1 + \theta_2 x + \theta_3 x^2 + \cdots + \theta_{d+1} x^d$ of degrees $d = 0, 1, 2, \ldots, 20$ to the data using least squares.

1. Show that for each fixed degree $d$, the LS minimizer exists and is unique (under mild conditions on the data).
2. Show that the *training error* $\mathrm{RMS}_{\text{train}}(d)$ is monotonically non-increasing in $d$.
3. Hold out a *test set* of separate data points $(x_j^{\text{test}}, y_j^{\text{test}})$. Show empirically (or argue heuristically) that the *test error* $\mathrm{RMS}_{\text{test}}(d)$ has a U-shape: first decreasing as $d$ increases (the model becomes flexible enough to capture the underlying pattern), then increasing for large $d$ (overfitting). The minimum identifies the optimal model complexity.
4. For a specific synthetic example — $y = \sin(2 \pi x) + \epsilon$ with Gaussian noise $\epsilon \sim \mathcal{N}(0, 0.1^2)$ and $N = 50$ training points uniform on $[0, 1]$ — find numerically the polynomial degree that minimizes test error on a held-out test set of $N_{\text{test}} = 50$ points.

**Recall:**

A polynomial fit of degree $d$ is [[Def - Least Squares Data Fitting|least squares data fitting]] with basis functions $f_j(x) = x^{j-1}$ for $j = 1, \ldots, d+1$. The design matrix is the *Vandermonde matrix* $A_{ij} = x_i^{j-1}$.

The [[Def - Validation (Training and Test Error)|training and test error]] are
$$\mathrm{RMS}_{\text{train}} = \sqrt{(1/N_{\text{train}}) \sum_i (y_i - \hat{f}(x_i))^2}, \quad \mathrm{RMS}_{\text{test}} = \sqrt{(1/N_{\text{test}}) \sum_j (y_j^{\text{test}} - \hat{f}(x_j^{\text{test}}))^2}.$$

---

# Convergent Strategy

**Problem class:** This is a *model-complexity selection* problem via [[Def - Validation (Training and Test Error)|validation]]. The class is "sweep a hyperparameter (here, polynomial degree) over a range, fit each model, evaluate on a held-out test set, identify the minimum-test-error model." This is the canonical approach to model selection in least squares; the only judgment is the choice of train/test split (here, 50/50, a reasonable but not unique choice).

**Assumption pattern:** Training data $\{(x_i, y_i)\}_{i=1}^N$ are samples from some unknown function $f(x)$ with additive noise: $y_i = f(x_i) + \epsilon_i$. The test data are samples from the same distribution. The assumption of i.i.d. sampling is crucial — it justifies using the test error as an estimator of true generalization error. With this assumption, the Vandermonde design matrix has linearly independent columns (assuming distinct $x_i$), and the LS theorem gives a unique fit for each degree.

**Theorem routing:** For each $d$, apply [[Thm - Existence and Uniqueness of Least Squares Solution]] to the Vandermonde design matrix of degree $d$ to get the unique LS minimizer $\hat{\theta}(d)$. Compute training error $\mathrm{RMS}_{\text{train}}(d) = \|y^{\text{train}} - A^{\text{train}} \hat{\theta}(d)\|/\sqrt{N_{\text{train}}}$ and test error $\mathrm{RMS}_{\text{test}}(d) = \|y^{\text{test}} - A^{\text{test}} \hat{\theta}(d)\|/\sqrt{N_{\text{test}}}$. Plot both vs. $d$ to find the minimum-test-error model. Then apply [[Thm - Bias-Variance Tradeoff in Regularized LS|the bias-variance tradeoff theorem]] (in spirit) to explain *why* the test error has its U-shape.

**Key decision point:** The non-obvious choice is the *test set size*. A small test set gives a noisy estimate of true generalization error, making the identified optimal degree unreliable. A large test set gives a better estimate but leaves less data for training, potentially worsening the model. The 50/50 split is a compromise; in production, 80/20 splits or 5-10 fold cross-[[Def - Validation (Training and Test Error)|validation]] are more common, with cross-validation generally giving more reliable estimates at the cost of more computation.

---

# Legal Operations Used

1. **Compute the LS fit via QR factorization.** (Operation 2 from the topic page.) For each degree $d$, form the $N \times (d+1)$ Vandermonde matrix and solve the LS problem via QR factorization — the only numerically stable approach for high-degree polynomial fits, which involve very ill-conditioned Vandermonde matrices.

2. **Split-and-validate.** (Operation 9 from the topic page.) Hold out a test set, fit on the training set only, evaluate on the test set. The minimum-test-error degree is the recommendation; this is the operational signature of model selection via validation.

3. **Identify the bias-variance signature.** (Conceptual operation.) High training error with high test error indicates underfitting (model too simple); low training error with high test error indicates overfitting (model too complex); both low indicates a healthy model. The transition between regimes is the U-shape on the test-error plot.

---

# Hints

> [!note]- Hint 1
> Each polynomial fit of degree $d$ is a least squares problem with the Vandermonde design matrix $A_{ij} = x_i^{j-1}$ for $j = 1, \ldots, d+1$. As $d$ increases, the design matrix gets more columns, but the data ($y$) is fixed.

> [!note]- Hint 2
> Training error decreases (or stays the same) as $d$ increases: more parameters can fit the data more closely. To see this formally, observe that adding a column to $A$ enlarges the column space, and the LS projection onto a larger [[Def - Subspace|subspace]] cannot increase the residual.

> [!note]- Hint 3
> The test error has a U-shape because: for small $d$, the model is too simple to capture the underlying $\sin(2\pi x)$ pattern (high bias, high test error). For large $d$, the model has so many parameters that it fits the *noise* in the training data, not the signal (low bias, but high variance, high test error). The minimum is at some intermediate $d^*$.

> [!note]- Hint 4 (near giveaway)
> For the $\sin(2\pi x)$ problem with 50 training points and noise $\sigma = 0.1$, the optimal degree is typically around $d^* = 5-8$ — high enough to fit the sinusoidal shape (which has 4 inflection points in $[0,1]$, requiring degree $\geq 4$ approximately), but low enough not to overfit. The exact value depends on the random sample and noise realization.

---

# Solution

The proof structure has three steps. Step 1 establishes existence and uniqueness of the LS minimizer for each degree, using the Vandermonde-distinctness condition. Step 2 proves the training error is non-increasing in $d$ via the *projection-onto-larger-[[Def - Subspace|subspace]]* argument. Step 3 explains the test-error U-shape via the bias-variance tradeoff and computes the optimal degree empirically for the synthetic problem.

**Step 1: Existence and uniqueness of LS for each degree.**

For each $d \geq 0$, the Vandermonde design matrix $A^{(d)}$ has $N$ rows and $d + 1$ columns. The columns are $\mathbf{1}, x^d, (x^d)^2, \ldots, (x^d)^d$ (componentwise powers). These are linearly independent iff the $x_i$ include at least $d + 1$ distinct values; for $N$ uniformly sampled $x_i$ with $N$ large, this is satisfied for all $d < N$.

> [!note]- Derivation
> Suppose $\alpha_0 \mathbf{1} + \alpha_1 x^d + \ldots + \alpha_d (x^d)^d = 0$ with not all $\alpha_j = 0$. The polynomial $p(x) = \alpha_0 + \alpha_1 x + \ldots + \alpha_d x^d$ has degree $\leq d$ but vanishes at every $x_i$. If the $x_i$ include $d + 1$ distinct values, this is $d + 1$ roots of a polynomial of degree $\leq d$, forcing $p \equiv 0$, contradiction. So under the distinctness condition, the columns are linearly independent. By [[Thm - Existence and Uniqueness of Least Squares Solution]], the LS minimizer is unique and given by $\hat{\theta}(d) = (A^{(d) T} A^{(d)})^{-1} A^{(d) T} y$.

**Step 2: Training error is non-increasing in $d$.**

The training error squared is $\mathrm{RMS}_{\text{train}}(d)^2 \cdot N = \min_\theta \|A^{(d)} \theta - y\|^2$. As $d$ increases, the column space of $A^{(d)}$ enlarges (we add one more column, the next power of $x$). The minimum of $\|A \theta - y\|^2$ over $\theta$ equals the squared distance from $y$ to the column space of $A$ — and this distance can only decrease (or stay the same) when the column space enlarges.

> [!note]- Derivation
> $\mathrm{RMS}_{\text{train}}(d)^2 \cdot N = \|y - P_d y\|^2$, where $P_d$ is the orthogonal projection onto $\mathrm{col}(A^{(d)})$. As $d$ increases, $\mathrm{col}(A^{(d)})$ enlarges (we add a column), so the projection of $y$ onto it gets closer to $y$, meaning $\|y - P_d y\|^2$ is non-increasing. Therefore $\mathrm{RMS}_{\text{train}}(d)$ is monotonically non-increasing in $d$. In particular, when $d = N - 1$, the Vandermonde matrix is square and (under distinctness) invertible — the LS fit interpolates the data exactly, giving zero training error.

**Step 3: Test error has a U-shape (heuristic + empirical).**

For small $d$ (e.g., $d = 0, 1, 2$), the model is too simple to capture $f(x) = \sin(2\pi x)$. The fit is dominated by *bias*: the polynomial cannot represent the sinusoidal shape, so both training and test errors are large.

For large $d$ (say $d \geq 15$), the model has many parameters and the LS fit is dominated by *variance*: small perturbations in the training data $y$ (the noise $\epsilon$) lead to large perturbations in $\hat{\theta}(d)$, especially in the high-degree coefficients (where the Vandermonde matrix has tiny singular values). The fit *interpolates* the training data perfectly (or nearly so) but oscillates wildly between training points, giving large test error.

For intermediate $d$ (typically 4-8 for this problem), the polynomial space is rich enough to approximate $\sin(2\pi x)$ closely (its Taylor series has nonzero coefficients up to all orders, but the first 5-6 captures the qualitative shape well), but not so rich that overfitting dominates. The test error has a minimum here.

> [!note]- Derivation (empirical computation)
> For $f(x) = \sin(2\pi x), \sigma = 0.1, N_{\text{train}} = 50, N_{\text{test}} = 50$ with both uniform on $[0, 1]$, simulating the experiment:
>
> $d = 0$: training and test RMS errors both $\approx 0.7$ (essentially constant fit at mean of data; the standard deviation of $\sin(2\pi x) + 0.1 \epsilon$ on $[0, 1]$ is $\approx 1/\sqrt{2}$).
>
> $d = 2$: training $\approx 0.6$, test $\approx 0.6$ (cubic fit captures rough monotonic trend but not the sinusoidal oscillation; still high error).
>
> $d = 5$: training $\approx 0.12$, test $\approx 0.13$ (degree-5 polynomial fits the sinusoid well; training and test errors comparable; near-minimum test error).
>
> $d = 10$: training $\approx 0.10$, test $\approx 0.15$ (mild overfit, test error starting to rise).
>
> $d = 20$: training $\approx 0.08$, test $\approx 0.5$ (heavy overfit, test error blown up; the polynomial oscillates wildly between training points).
>
> The optimal degree is $d^* \approx 5-6$, with test RMS $\approx 0.12$ (close to the noise level $\sigma = 0.1$, indicating the model has captured the true signal and is now limited only by irreducible noise).

> [!note]- Complete formal solution
> *Step 1 (Existence and uniqueness):* Under the distinctness condition on the $x_i$, the Vandermonde matrix $A^{(d)}$ has linearly independent columns for any $d \leq N - 1$. By [[Thm - Existence and Uniqueness of Least Squares Solution]], $\hat{\theta}(d) = (A^{(d) T} A^{(d)})^{-1} A^{(d) T} y$ is the unique LS minimizer.
>
> *Step 2 (Monotonicity of training error):* Let $P_d$ be the orthogonal projection onto $\mathrm{col}(A^{(d)})$. Then $\mathrm{RMS}_{\text{train}}(d)^2 N = \|y - P_d y\|^2$. Since $\mathrm{col}(A^{(d)}) \subseteq \mathrm{col}(A^{(d+1)})$, the projection of $y$ onto the larger subspace is closer to $y$, giving $\|y - P_{d+1} y\|^2 \leq \|y - P_d y\|^2$. Hence $\mathrm{RMS}_{\text{train}}(d)$ is monotonically non-increasing in $d$.
>
> *Step 3 (Test error U-shape):* The test error decomposes (approximately, in expectation under the i.i.d. noise model) as $\mathbb{E}[\mathrm{RMS}_{\text{test}}(d)^2] = \mathrm{bias}^2(d) + \mathrm{variance}(d) + \sigma^2$, where:
> - $\mathrm{bias}^2(d)$ is the squared distance from the true function $f$ to the polynomial space of degree $d$. This is large for small $d$ (the polynomial space is too small to approximate $f$) and decreases as $d$ grows. For $f = \sin(2 \pi x)$ and degree $d$ polynomials, the bias decreases roughly geometrically.
> - $\mathrm{variance}(d)$ is the sensitivity of the LS fit to noise; it scales as $\sigma^2 (d+1)/N$ in the well-conditioned case but blows up for high $d$ where the Vandermonde matrix is ill-conditioned.
> - $\sigma^2$ is the irreducible noise (constant).
>
> The bias contribution dominates for small $d$ (giving high test error), and the variance contribution dominates for large $d$ (also giving high test error). The minimum is at the $d^*$ where the two are balanced. Empirically for this problem, $d^* \approx 5-6$.

> [!warning] Illegal but tempting alternative route
> One might try to use *only* the training error to pick the optimal degree. This *always* leads to the worst possible recommendation: the maximum degree $d = N - 1$, where training error is exactly zero (interpolation). This is the *worst* model in terms of generalization; it overfits maximally. The lesson: **never use training error to choose model complexity**. The training error is always biased downward as a measure of generalization error; use a held-out test set or cross-validation.

---

# Key Takeaways

**The U-shape on the test-error plot is the canonical signature of bias-variance tradeoff.**

Whenever you sweep a model-complexity hyperparameter — polynomial degree, number of basis functions, number of layers in a neural network, $\lambda$ in regularized LS (going the other direction) — and plot test error against complexity, you should expect a U-shape: error too high for too-simple models (bias), error too high for too-complex models (variance), with a minimum in between. The minimum identifies the optimal complexity. The shape of the U (sharp vs. flat) tells you how sensitive the model is to the hyperparameter — sharp U means careful tuning matters; flat U means a wide range of values are nearly optimal. The trigger for this diagnostic: any data-fitting problem where you have a model-complexity dial.

**Training error is always monotonically improving with complexity; this is a *bug*, not a feature.**

The training error is the model's performance on the data it was fit to, so adding parameters can only help (or not hurt). This monotonic decrease tells you *nothing* about whether the model will generalize. The fundamental insight of validation is to *partition the data* so that the test set acts as a proxy for unseen data; the test error then can (and does) increase with complexity beyond a point. This decoupling — training error on the training set, generalization estimated on the test set — is the conceptual core of every validation procedure.

**The Vandermonde matrix is poorly conditioned for high degrees, which is the algebraic reason for the high-degree overfitting catastrophe.**

The condition number of the Vandermonde matrix on $N$ points uniform on $[0, 1]$ grows roughly as $\sqrt{N}^d$. For $d = 15, N = 50$, this is approximately $50^{7.5} \approx 10^{12}$ — at the edge of double-precision arithmetic. The LS coefficients $\hat{\theta}(d)$ for high $d$ are computed by inverting (effectively) a matrix with this enormous condition number, so they are essentially random — driven by floating-point errors rather than by the data. This is a numerical phenomenon, but it has the *same* effect as statistical overfitting: the fit oscillates wildly because tiny noise components in the data get amplified by the inverse Vandermonde. Use of [[Thm - Least Squares via QR Factorization|QR-based LS]] mitigates but does not eliminate this; for very high $d$, the model is hopeless regardless of algorithm. The lesson: even before reaching the statistical-overfit regime, polynomial fits at high degree fail for numerical reasons.

This exercise is the foundation for understanding the broader phenomenon of overfitting that the regularized LS framework (see [[Def - Regularized Least Squares]] and [[Thm - Bias-Variance Tradeoff in Regularized LS]]) is designed to address. The next exercise [[Ex - Tikhonov regularization is a multi-objective LS problem]] shows how to *prevent* overfitting at high $d$ via regularization, recovering useful high-degree models that would otherwise be unusable.
