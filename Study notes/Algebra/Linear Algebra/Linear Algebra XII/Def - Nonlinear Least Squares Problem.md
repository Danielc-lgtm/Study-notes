---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - The Total Derivative and Differentiability"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Let $f : \mathbb{R}^n \to \mathbb{R}^m$ be a differentiable function, with component functions $f_1, \ldots, f_m$. The Euclidean norm is $\|y\|^2 = \sum_i y_i^2$. The **Jacobian** of $f$ at a point $x$ is the $m \times n$ matrix
$$Df(x)_{ij} = \frac{\partial f_i}{\partial x_j}(x), \qquad i = 1, \ldots, m, \quad j = 1, \ldots, n,$$
which is also called the *derivative matrix*. The **Taylor affine approximation** of $f$ at a basepoint $x_0$ is
$$\hat f(x; x_0) = f(x_0) + Df(x_0)(x - x_0).$$
We always assume $f$ is at least once continuously differentiable on the domain of interest. The full symbol registry is on the parent page [[Linear Algebra XII — Applied III — Nonlinear Least Squares]].

---

# Axiom Motivation

The [[Def - Least Squares Problem|linear least squares problem]] is the question: among all $x$, which minimizes $\|Ax - b\|^2$ for a given matrix $A$ and vector $b$? The answer is a single closed-form formula, the [[Def - Normal Equations|normal equations]] $A^T A x = A^T b$, valid because the gradient $\nabla \|Ax - b\|^2 = 2 A^T(Ax - b)$ is *linear* in $x$ and so the optimality condition $\nabla = 0$ is one linear system. The clean closed form is a privilege of linearity.

Now ask the same question but with a general nonlinear function $f$ in place of the affine map $x \mapsto Ax - b$. We want the $x$ that minimizes $\|f(x)\|^2$ for a differentiable but otherwise arbitrary residual map. The gradient is still computable — by the chain rule it is $\nabla \|f(x)\|^2 = 2 Df(x)^T f(x)$ — but now this gradient depends nonlinearly on $x$, so setting it to zero gives a *nonlinear* system $Df(x)^T f(x) = 0$ in $n$ unknowns. The set of zeros of a nonlinear vector field can have many components, no closed-form parameterization, and pathological geometry. There is no analogue of the normal equations; there is no global solver.

So why call this a "problem class" at all, if there is no general solver? The reason is that *applied* problems do not need a global solver — they need a *local* one. Almost every nonlinear least squares problem in practice comes equipped with a sensible starting point $x^{(1)}$ — a previous solution, a domain-informed guess, an approximation by a related linear problem — and we want the algorithm to find a local minimum near that starting point. The class of problems we can solve well is exactly the class for which "find a local minimum starting from $x^{(1)}$" is the right question. That is the question this chapter answers.

Why insist on the **squared** norm rather than $\|f(x)\|$ or $\|f(x)\|_1$ or $\max_i |f_i(x)|$? Three reasons combine. First, the squared norm $\|f(x)\|^2 = \sum_i f_i(x)^2$ is *differentiable* as a function of $x$ wherever $f$ is — no kinks at the origin (as $\|f\|$ has) and no kinks at the coordinate hyperplanes (as $\|f\|_1$ and $\|f\|_\infty$ have). Differentiability is the prerequisite for all the iterative algorithms below. Second, the gradient $2 Df^T f$ exposes the **Jacobian** $Df$ in a particularly clean way — the same Jacobian also appears in the Taylor approximation $\hat f$, so a single linearization of $f$ serves both purposes (computing the gradient *and* approximating the objective near the iterate). Third, the squared norm is the natural objective from a probabilistic standpoint: if the residuals $f_i(x)$ represent additive Gaussian errors in a model fit, the maximum-likelihood estimator is exactly the minimizer of $\|f(x)\|^2$. Three different criteria — differentiability, structural cleanness, statistical justification — all point to squared norm.

Why allow the [[Def - Dimension|dimensions]] $m$ and $n$ to differ? Two reasons. When $m = n$ and we ask for $\|f(x)\|^2 = 0$, we are *solving* the nonlinear equations $f(x) = 0$ — this is the special case relevant to physics (mechanical equilibrium), economics (Nash equilibrium), and root-finding. When $m > n$ (more residuals than variables) the problem is **overdetermined**: typically there is no $x$ with $f(x) = 0$ exactly and we are finding the best approximation. This is the model-fitting regime, with $m$ data points and $n$ parameters, and is the dominant case in applications. The setup with general $m \neq n$ unifies these two regimes; the algorithms work for both.

A small extension subtlety: must $f$ be *globally* differentiable, or only at the iterates? Theoretically the global view is cleanest — we want $f \in C^1$ on the whole domain. Practically the algorithms only ever evaluate $Df$ at the current iterate, so $f$ needs to be differentiable along the iterates' trajectory. A function with isolated points of non-differentiability (like the friction-cable example in Boyd Exercise 18.5, with a $\max(0, \cdot)$ in the tension) is acceptable provided the iterates avoid those points — and a careful initialization can ensure they do. If the algorithm wanders into a non-smooth region, the Jacobian becomes ill-defined and the algorithm fails; the fix is either to smooth the function (see legal operation 6 of the topic page) or to choose a better starting point.

---

# The Definition

The **nonlinear least squares problem** with residual map $f : \mathbb{R}^n \to \mathbb{R}^m$ is the optimization problem
$$\min_{x \in \mathbb{R}^n} \; \|f(x)\|^2 = \min_{x \in \mathbb{R}^n} \; \sum_{i=1}^m f_i(x)^2.$$

The vector-valued function $f$ is called the **residual** (or **residual map**); its components $f_i$ are the **scalar residuals**. The function $f$ is required to be at least once continuously differentiable in a neighborhood of any iterate the algorithm visits. When $m = n$ and the minimum value is zero, the problem reduces to **solving the nonlinear equations** $f(x) = 0$.

The first-order optimality condition (necessary condition for a local minimizer $\hat x$) is
$$2 \, Df(\hat x)^T \, f(\hat x) = 0,$$
that is, $Df(\hat x)^T f(\hat x) = 0$. Any local minimizer must satisfy this, but the condition is also satisfied by saddle points and local maxima; the condition is necessary, not sufficient.

A **solution** to the problem is a *local* minimizer: a point $\hat x$ for which $\|f(\hat x)\|^2 \leq \|f(x)\|^2$ for all $x$ in some neighborhood of $\hat x$. We do not generally have a global minimizer in mind, and we have no algorithm that guarantees finding one.

A **zero-residual solution** is one with $f(\hat x) = 0$. Zero-residual solutions automatically satisfy the optimality condition and are global minimizers (of $\|f\|^2$, which is nonnegative). The special case $m = n$ with a zero-residual solution is the **nonlinear equations problem**.

---

# Relate to Other Fields / Compression

The nonlinear least squares problem is the natural generalization of the [[Def - Least Squares Problem|linear least squares problem]] obtained by allowing the residual to be a general differentiable map rather than an affine one. The linear case is recovered by setting $f(x) = Ax - b$, in which case $Df(x) = A$ is constant and the algorithms of this chapter all terminate in one step at the solution $x = (A^T A)^{-1} A^T b$.

From the angle of **statistical estimation**, the nonlinear least squares problem is the maximum-likelihood estimator for a nonlinear regression model with additive independent Gaussian errors. If $y_i = h_i(x) + \varepsilon_i$ with $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$ independent, then the log-likelihood of the data given $x$ is, up to constants, $-\frac{1}{2\sigma^2} \sum_i (y_i - h_i(x))^2$, and maximizing this is exactly minimizing the nonlinear least squares objective with $f_i(x) = h_i(x) - y_i$. This is why the algorithms of this chapter dominate practical regression: they compute the maximum-likelihood estimator for the most common noise model.

From the angle of **functional analysis**, the problem can be read as projecting the origin onto the image $f(\mathbb{R}^n) \subseteq \mathbb{R}^m$, in the sense of finding $f(\hat x)$ closest to $0$. When $f$ is affine, this image is an affine subspace and the projection is computed by the [[Thm - Least Squares via Normal Equations|normal equations]]. When $f$ is nonlinear, the image is a curved manifold (an $n$-dimensional manifold immersed in $\mathbb{R}^m$, near regular points of $f$), and projecting onto a curved manifold has no closed form — it requires the iterative geometry of this chapter.

**True name.** The operational characterization of the problem — the one that drives every algorithm — is: *we want to find $x$ where the gradient $Df(x)^T f(x)$ vanishes, by repeatedly linearizing $f$ around the current iterate and solving a linear least squares subproblem.* This is the true name of the problem; the "minimize $\|f\|^2$" framing is a clean statement, but the working definition is the optimality condition combined with the linearize-and-iterate strategy.

---

# Examples / Corollaries

**Example 1 (location from range measurements).** A target is at unknown position $x \in \mathbb{R}^2$, and we measure noisy distances $\rho_i$ from $x$ to $m$ known beacons $a_i \in \mathbb{R}^2$:
$$\rho_i = \|x - a_i\| + \text{noise}, \qquad i = 1, \ldots, m.$$
The residual $f_i(x) = \|x - a_i\| - \rho_i$ is nonlinear in $x$ (because of the square root in $\|\cdot\|$), so this is a nonlinear least squares problem with $m$ residuals and $n = 2$ unknowns. This is the basis of GPS localization. Here $m$ is typically larger than $n$, so the problem is overdetermined and the residual minimum is not zero (because of measurement noise).

**Example 2 (Nash equilibrium of a finite game).** Each of $n$ agents chooses a strategy $x_i \in \mathbb{R}$ to maximize her own payoff $R_i(x_1, \ldots, x_n)$. At a Nash equilibrium, each agent's choice is a best response to the others, so $\partial R_i / \partial x_i = 0$ for each $i$. Setting $f_i(x) = \partial R_i / \partial x_i$, we have a square ($m = n$) nonlinear system $f(x) = 0$; solving it (locally, near a starting guess) by Newton's method — the $m = n$ specialization of Gauss–Newton — is a standard approach.

**Example 3 (nonlinear model fitting).** Given data $(x^{(i)}, y^{(i)})$ for $i = 1, \ldots, N$, fit a model $y \approx \hat f(x; \theta)$ where $\hat f$ depends nonlinearly on the parameter vector $\theta \in \mathbb{R}^p$. The residuals are
$$f_i(\theta) = \hat f(x^{(i)}; \theta) - y^{(i)}, \qquad i = 1, \ldots, N,$$
so this is a nonlinear least squares problem in the variable $\theta$ with $N$ residuals. A specific instance from Boyd §18.4 is $\hat f(x; \theta) = \theta_1 e^{\theta_2 x} \cos(\theta_3 x + \theta_4)$, an exponentially decaying sinusoid with four parameters.

**Non-example 1 (linear least squares).** When $f(x) = Ax - b$, the problem is the [[Def - Least Squares Problem|linear least squares problem]], which is *not* what we mean by nonlinear least squares — it has a closed form and does not require iteration. Conceptually it is a degenerate special case; algorithmically it is treated by the previous chapter's methods.

**Non-example 2 (non-differentiable objective).** Minimizing $\sum_i |f_i(x)|$ (the $\ell^1$ analogue) or $\max_i |f_i(x)|$ (the Chebyshev analogue) is *not* a nonlinear least squares problem — the objective is not differentiable, the algorithms of this chapter do not apply, and one needs the machinery of non-smooth or linear programming.

**Corollary (gradient form).** For any differentiable $f$, the gradient of $\|f(x)\|^2$ is exactly $2 Df(x)^T f(x)$. Proof: by the chain rule applied to $g(x) = \|f(x)\|^2 = f(x)^T f(x)$, we have $\nabla g(x) = 2 Df(x)^T f(x)$. The optimality condition $\nabla g = 0$ becomes $Df(\hat x)^T f(\hat x) = 0$.

**Corollary (Hessian form).** The Hessian of $\|f(x)\|^2$ is
$$\nabla^2 \|f(x)\|^2 = 2 Df(x)^T Df(x) + 2 \sum_{i=1}^m f_i(x) \nabla^2 f_i(x).$$
The first term, $2 Df^T Df$, is the **Gauss–Newton approximate Hessian**; the second term is the **curvature contribution** that depends on the residuals. When all $f_i = 0$ at $\hat x$, the curvature term vanishes and the Gauss–Newton Hessian is exact.

**Calibration check.** A reader who has understood the definition should be able to verify the following three things on a small example. (i) For $f(x) = (x_1^2 - 2, x_2^2 - 3) \in \mathbb{R}^2$ and $x = (1, 2) \in \mathbb{R}^2$, compute $f(x)$, $Df(x)$, and the gradient $2 Df^T f$. (ii) Recognize that $f(x) = 0$ at $x = (\sqrt{2}, \sqrt{3})$ and that this is a zero-residual solution. (iii) Identify whether the problem with $f_i(x) = \|x - a_i\| - \rho_i$ from Example 1 is generally zero-residual or overdetermined when $m = 5$ and $n = 2$ (overdetermined; only if the $\rho_i$ are noise-free distances from a common point is a zero-residual solution possible).

---

# Unlocked by This

> [!tip] Maximum Likelihood Estimation with Gaussian Errors *(from Statistics)*
> Given a parametric model $y_i = h_i(\theta) + \varepsilon_i$ with $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$ i.i.d., the **maximum likelihood estimator** $\hat \theta$ for $\theta$ is exactly the minimizer of the nonlinear least squares objective $\sum_i (h_i(\theta) - y_i)^2$. This unlocks vast swaths of nonlinear statistical estimation: nonlinear regression, calibration of physical models against experimental data, Kalman filter updates as iterative MLE on a quadratic likelihood. The chapter's algorithms (especially Levenberg–Marquardt) are the default implementation of "find the maximum likelihood estimator" in any Gaussian model.

> [!tip] Bundle Adjustment *(from Computer Vision)*
> In structure-from-motion, one is given many images of an unknown 3D scene from unknown camera poses and seeks both the scene geometry and the camera poses that best explain the image observations. The residuals are the reprojection errors: for each observed image point $u^{(i,j)}$ (point $j$ in image $i$), $f_{ij}(\theta) = \pi(\text{camera}_i, \text{point}_j) - u^{(i,j)}$, where $\pi$ is the perspective projection function (nonlinear in both the camera pose and the point coordinates). **Bundle adjustment** is the nonlinear least squares problem $\min_\theta \sum_{ij} \|f_{ij}(\theta)\|^2$ over all camera and point parameters jointly, typically with $\theta$ in the hundreds of thousands of variables. Levenberg–Marquardt with sparsity-exploiting linear algebra (Schur complement on the camera/point block structure) is the workhorse of every 3D reconstruction pipeline from Google Street View to SLAM in robotics.

> [!tip] Neural Network Training as Nonlinear LS *(from Deep Learning)*
> Training a neural network $\hat y = N(x; \theta)$ on data $(x^{(i)}, y^{(i)})$ with squared-error loss is the nonlinear least squares problem $\min_\theta \sum_i \|N(x^{(i)}; \theta) - y^{(i)}\|^2$ in millions of parameters $\theta$. Direct application of Levenberg–Marquardt is too expensive (the $Df^T Df$ matrix is too large), but the conceptual frame is unchanged: linearize $N$ via the chain rule (backpropagation), solve an approximate Hessian system (Adam, RMSProp use diagonal approximations to $Df^T Df$), iterate. Practical deep learning is, in spirit, Gauss–Newton with severe Hessian approximations and stochastic mini-batch gradients.
