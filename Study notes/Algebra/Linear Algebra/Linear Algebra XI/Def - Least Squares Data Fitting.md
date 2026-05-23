---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
  - "Def - Normal Equations"
tags: [algebra, linear-algebra, applied, data-fitting]
---

# Notation

A data set consists of $N$ examples, each comprising a *feature vector* $x^{(i)} \in \mathbb{R}^n$ and a scalar *outcome* $y^{(i)} \in \mathbb{R}$, for $i = 1, \ldots, N$. The model $\hat{f}$ is a function $\mathbb{R}^n \to \mathbb{R}$; the predicted outcome at feature vector $x$ is $\hat{y} = \hat{f}(x)$. The residual for the $i$th example is $r^{(i)} = y^{(i)} - \hat{f}(x^{(i)})$, and the $N$-vector of residuals is $r^d = y^d - \hat{y}^d$ where $y^d = (y^{(1)}, \ldots, y^{(N)})$ and $\hat{y}^d = (\hat{f}(x^{(1)}), \ldots, \hat{f}(x^{(N)}))$.

**Convention warning:** in §XI.2 onward, the symbol $x$ refers to *feature vectors*, not to the unknown variable being optimized over (which is now $\theta$). This is a deliberate naming clash inherited from data-fitting and statistical practice; the reader should mentally translate "$x$ in §XI.1" to "$\theta$ in §XI.2+" and "$b$ in §XI.1" to "$y^d$ in §XI.2+".

---

# Axiom Motivation

You have data — $N$ measurements of some scalar outcome $y$ as a function of an $n$-dimensional input $x$ — and you want a *model*: a function $\hat{f}$ that predicts $y$ from $x$, both on the observed examples and (more importantly) on new examples you have not seen. The question is: among all possible functions $\hat{f}$, which should you choose?

Choosing nothing is one extreme: predict $\hat{y} = 0$ always. This has zero parameters and so cannot overfit, but it makes no use of the data. Choosing arbitrarily expressive functions is the other extreme: take $\hat{f}$ to interpolate the data exactly, so $\hat{f}(x^{(i)}) = y^{(i)}$ for all $i$. This has zero training error but, unless the data are noise-free and the underlying $f$ is exactly representable by $\hat{f}$, it will predict wildly on any new point not in the training set — the *overfitting* failure mode.

The compromise: choose $\hat{f}$ from a *parametric family* $\{\hat{f}_\theta : \theta \in \mathbb{R}^p\}$ that is rich enough to capture the relevant variation in the data, but not so rich that it overfits. The Boyd choice is the *linear in the parameters* family:
$$\hat{f}_\theta(x) = \theta_1 f_1(x) + \theta_2 f_2(x) + \cdots + \theta_p f_p(x),$$
where $f_1, \ldots, f_p : \mathbb{R}^n \to \mathbb{R}$ are *basis functions* chosen ahead of time. The name reflects what is and isn't linear: for any *fixed* $x$, the model is a linear function of the parameter vector $\theta$, but as a function of $x$, the model can be highly nonlinear (since the $f_j$ can be polynomials, sinusoids, indicators, etc.). The model is "linear in the parameters" but not in general "linear in $x$."

Why this choice? Three reasons. First, *computational*: linear-in-parameters models give a *quadratic-in-$\theta$* loss function (sum of squared residuals), and minimizing quadratic functions is the least squares problem. The model fits as a matrix-vector LS solve. Second, *flexibility*: the family is dense in many function classes — polynomials approximate continuous functions on compact sets (Weierstrass), sinusoids approximate periodic functions (Fourier), Gaussians approximate smooth bumps. Choosing the basis is application-dependent feature engineering, but for almost any prediction problem, a rich enough linear-in-parameters basis exists. Third, *interpretability*: each parameter $\theta_j$ has the clear interpretation "the contribution of basis function $f_j$ to the prediction." This is the source of regression coefficient interpretation in statistics.

The choice of squared loss (rather than absolute loss or other) is the same choice as in §XI.1: it gives a quadratic objective with closed-form solution, and under Gaussian-noise modelling it is the MLE. We accept the same tradeoffs — outliers have outsized influence — for the same gains.

The minimum-RSS principle gives the *training loss*:
$$L(\theta) = \sum_{i=1}^N (y^{(i)} - \hat{f}_\theta(x^{(i)}))^2 = \|y^d - A \theta\|^2$$
where the *data matrix* (or *design matrix*) $A$ is the $N \times p$ matrix with $A_{ij} = f_j(x^{(i)})$. This is a standard least squares problem in $\theta$, with $A$ a known matrix and $y^d$ a known vector. The LS solution $\hat{\theta} = (A^T A)^{-1} A^T y^d$ is then the model parameter vector.

The reader has now invented the LS data-fitting framework. The remaining content of §XI.2 is about *which basis functions to use* (feature engineering, §13.3) and *how to detect and prevent overfitting* ([[Def - Validation (Training and Test Error)|validation]], §13.2). Both of these are addressed in their own definition pages.

---

# The Definition

> **Definition (Least Squares Data Fitting).** Given a data set $\{(x^{(i)}, y^{(i)})\}_{i=1}^N$ and chosen basis functions $f_1, \ldots, f_p$, the *linear-in-parameters model* is the function family
> $$\hat{f}_\theta(x) = \theta_1 f_1(x) + \cdots + \theta_p f_p(x), \qquad \theta \in \mathbb{R}^p.$$
> The *least squares data fitting problem* is to find the parameter vector $\hat{\theta}$ that minimizes the residual sum of squares
> $$L(\theta) = \sum_{i=1}^N (y^{(i)} - \hat{f}_\theta(x^{(i)}))^2 = \|y^d - A\theta\|^2,$$
> where the *data matrix* (or *design matrix*) is the $N \times p$ matrix $A$ with $A_{ij} = f_j(x^{(i)})$ and $y^d = (y^{(1)}, \ldots, y^{(N)})$. Provided $A$ has linearly independent columns, the solution is
> $$\hat{\theta} = (A^T A)^{-1} A^T y^d = A^\dagger y^d.$$

The fitted model is $\hat{f}(x) = \hat{\theta}_1 f_1(x) + \cdots + \hat{\theta}_p f_p(x)$.

---

# Relate to Other Fields / Compression

**True name:** least squares data fitting is *linear regression with arbitrary nonlinear features*. The model is *linear in the parameters but nonlinear in the input* — a fact often missed by students who conflate "linear regression" with "fitting straight lines." Once basis functions are introduced, polynomial fitting, sinusoidal fitting, exponential fitting, and feature-engineered fitting are *all* linear regression, just with different design matrices.

This is the same construction as:
- **Linear Regression** in statistics: the explicit identification of LS data fitting with the classical OLS framework. The basis functions are called *features* or *covariates*; the design matrix $A$ is sometimes called $X$.
- **Polynomial Interpolation** in numerical analysis: when $p = N$ and the basis functions are chosen so that $A$ is square and invertible (e.g., Vandermonde at distinct nodes), LS data fitting reduces to exact interpolation: $\hat{f}(x^{(i)}) = y^{(i)}$ for all $i$.
- **Fourier Series**: choosing $f_j(x) = \cos(\omega_j x), \sin(\omega_j x)$ as basis functions and applying LS data fitting computes the best-fitting Fourier series of given truncation length. The orthogonality of sinusoids over a symmetric grid makes the Gram matrix $A^T A$ nearly diagonal, which is why FFT-based methods are so efficient.
- **Generalized Linear Models** in statistics: extending LS data fitting by replacing the squared loss with a different log-likelihood (logistic, Poisson) gives logistic regression, Poisson regression, and other GLMs. The structural connection is that all GLMs are linear in the parameters $\theta$.

---

# Examples / Corollaries

*Example 1 (constant fit).* Take $p = 1$ with $f_1(x) = 1$. The data matrix is the $N \times 1$ matrix $\mathbf{1} = (1, \ldots, 1)^T$. The LS solution is $\hat{\theta}_1 = (\mathbf{1}^T \mathbf{1})^{-1} \mathbf{1}^T y^d = (1/N) \sum_i y^{(i)} = \overline{y}$, the sample mean. The residual RMS is $\sqrt{(1/N) \sum_i (y^{(i)} - \overline{y})^2} = \mathrm{std}(y^d)$, the sample standard deviation. So the optimal constant fit is the mean, with residual RMS equal to the standard deviation — recovering the elementary identification of mean as minimizer-of-squared-deviations.

*Example 2 (straight-line fit).* Take $n = 1$, $p = 2$, $f_1(x) = 1$, $f_2(x) = x$. The design matrix is $A = (\mathbf{1}, x^d)$ where $x^d = (x^{(1)}, \ldots, x^{(N)})$. The LS solution can be worked out explicitly (Boyd does so on page 250) and gives:
$$\hat{\theta}_2 = \rho \frac{\mathrm{std}(y^d)}{\mathrm{std}(x^d)}, \qquad \hat{\theta}_1 = \mathrm{avg}(y^d) - \hat{\theta}_2 \mathrm{avg}(x^d),$$
where $\rho$ is the *correlation coefficient* between $x^d$ and $y^d$. So the LS slope is the correlation times the ratio of standard deviations, and the LS intercept makes the line pass through the centroid $(\mathrm{avg}(x^d), \mathrm{avg}(y^d))$. This is the form taught in every elementary regression course; the LS data-fitting framework derives it cleanly.

*Example 3 (polynomial fitting).* Take $n = 1$, $p = d+1$, and $f_j(x) = x^{j-1}$ for $j = 1, \ldots, p$. The design matrix is the Vandermonde matrix at the data points $x^{(i)}$. Polynomial fitting is LS data fitting with this choice of basis; the Vandermonde matrix has linearly independent columns iff the $x^{(i)}$ include at least $p$ distinct values, so LS has a unique solution under mild conditions. For very high degrees, the Vandermonde matrix is famously ill-conditioned, making the LS problem numerically delicate — this is one canonical case where QR factorization is essential and the normal equations approach fails.

*Example 4 (NOT a linear-in-parameters model).* The model $\hat{f}(x) = e^{\theta_1 x}$ is *not* linear in $\theta_1$, so LS data fitting in this form does not apply directly. (A *log-transform* $\log \hat{y} = \theta_1 x$ turns this into a linear model in $\log y$, which is a common trick but changes the loss function — see Boyd §13.1.3.) The nonlinear case is handled by [[Linear Algebra XII — Applied III — Nonlinear Least Squares|nonlinear least squares]], specifically Gauss-Newton and Levenberg-Marquardt.

*Example 5 (multi-feature regression with interactions).* For $n = 2$ features, basis functions $1, x_1, x_2, x_1^2, x_2^2, x_1 x_2$ give a quadratic model with interaction terms; this is still linear-in-parameters with $p = 6$ parameters, and LS data fitting applies. The interaction term $x_1 x_2$ allows the model to capture the joint effect of the two features beyond their separate effects.

**Calibration check.** Verify: (i) when $p = 1$ and $f_1 \equiv 1$, the LS fit is the sample mean; (ii) when $p = N$ and the basis functions make $A$ square and invertible (interpolation regime), the LS fit reduces to exact interpolation; (iii) the LS fit is invariant under affine reparametrization of the basis — replacing $f_j$ with $\sum_k M_{jk} f_k$ for invertible $M$ does not change $\hat{f}$ (only changes $\hat{\theta}$).

---

# Unlocked by This

> [!tip] Generalized Linear Models *(from Statistics)*
> Replacing the squared loss in LS data fitting with other log-likelihoods gives the **generalized linear model** (GLM) family. Replacing Gaussian noise with Bernoulli noise gives logistic regression, with Poisson noise gives Poisson regression, with binomial noise gives binomial regression. All GLMs are linear in the parameters; the loss function changes (and is no longer quadratic), so the solution requires iterative methods (Newton-Raphson, equivalent to iteratively reweighted least squares). The structural unification is that the *parameter vector* $\theta$ enters linearly; the only choice is which log-likelihood to use.

> [!tip] Spline Fitting *(from Approximation Theory)*
> Choosing the basis functions to be piecewise polynomials with specified continuity at "knot" points gives a **spline fit**. Cubic splines (piecewise cubic, continuous through second derivatives) are the workhorse of smoothing in many applied fields. The LS spline fit problem is still linear-in-parameters but the basis is local, which gives a sparse design matrix and efficient algorithms; the continuity constraints at knots are encoded as constrained-LS conditions, which is exactly the structure of §XI.3.
