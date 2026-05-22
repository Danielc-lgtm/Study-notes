---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Nonlinear Least Squares Problem"
  - "Def - Levenberg-Marquardt Algorithm"
  - "Def - Least Squares Classifier"
  - "Def - Regularized Least Squares"
tags: [algebra, linear-algebra, applied, classification, machine-learning]
---

# Problem Statement

Consider a binary classification problem with training data $\{(x^{(i)}, y^{(i)})\}_{i=1}^N$, where each $x^{(i)} \in \mathbb{R}^p$ is a feature vector and each $y^{(i)} \in \{-1, +1\}$ is a Boolean label. The (linear) least squares classifier of Boyd Chapter 14 fits $f(x) = \beta^T x + v$ to the data by minimizing $\sum_i (f(x^{(i)}) - y^{(i)})^2$; the classifier outputs $\operatorname{sign}(\beta^T x + v)$.

Replace the sign function by the smooth **sigmoid** $\phi(u) = (e^u - e^{-u})/(e^u + e^{-u}) = \tanh(u)$, and define the **nonlinear least squares classification** problem:
$$\min_{\beta, v} \quad \sum_{i=1}^N \big( \phi(\beta^T x^{(i)} + v) - y^{(i)} \big)^2 + \lambda \|\beta\|^2,$$
where $\lambda > 0$ is a regularization parameter.

**(a)** Set up this problem as an unconstrained nonlinear least squares problem in the variable $\theta = (\beta, v) \in \mathbb{R}^{p+1}$, and write the residual map $r(\theta)$ explicitly. Derive the Jacobian $Dr(\theta)$.

**(b)** Explain why this formulation is preferable to the bare linear-LS classifier of Boyd Chapter 14. What does the sigmoid replacement gain?

**(c)** Sketch the Levenberg–Marquardt algorithm for this problem, identifying which steps are standard (LM machinery) and which are problem-specific (Jacobian evaluation).

**Recall:**

A [[Def - Least Squares Classifier|least squares classifier]] $\hat f(x) = \operatorname{sign}(\beta^T x + v)$ is trained by minimizing the *continuous* prediction error $\sum_i (\beta^T x^{(i)} + v - y^{(i)})^2$ — a linear LS problem. This is a *surrogate* for the (non-differentiable) classification error $\sum_i (\operatorname{sign}(\beta^T x^{(i)} + v) - y^{(i)})^2$, which equals $4 \times$ the number of misclassifications.

![[Def - Nonlinear Least Squares Problem#The Definition]]

![[Def - Levenberg-Marquardt Algorithm#The Definition]]

The sigmoid function $\phi(u) = \tanh(u)$ has range $(-1, 1)$, derivative $\phi'(u) = \mathrm{sech}^2(u) = 1 - \phi(u)^2$, and approximates $\operatorname{sign}(u)$ as $|u| \to \infty$.

[[Def - Regularized Least Squares|Tikhonov regularization]] adds $\lambda \|\beta\|^2$ to the objective to prevent overfitting; here we regularize only $\beta$ (not the offset $v$).

---

# Convergent Strategy

**Problem class.** This is the canonical **nonlinear classification** problem: a binary classifier built by minimizing a smooth surrogate of the classification error, fit by nonlinear least squares. As the [[Linear Algebra XII — Applied III — Nonlinear Least Squares#Problem-Solving Strategy|topic page strategy]] indicates, this is "want to fit a logistic-style model → write it as nonlinear LS classification with the sigmoid link, then apply Levenberg–Marquardt." The structural pattern is identical to many sigmoid-based ML methods (logistic regression, single-layer neural networks, calibration of probability classifiers).

**Assumption pattern.** Three recognizable signals: (i) labels are Boolean — *not* continuous regression targets; (ii) we want a *classifier* (output the predicted label) but the objective should be *differentiable* (so we can use gradient-based optimization); (iii) the sigmoid $\phi$ is a smooth approximation of $\operatorname{sign}$. The setup converts a non-differentiable classification problem into a differentiable nonlinear LS one, allowing the chapter's algorithms to apply. This is the **smooth-surrogate** pattern (legal operation 6).

**Theorem routing.** The route is: (a) Identify the residuals $r_i(\theta) = \phi(\beta^T x^{(i)} + v) - y^{(i)}$ and the regularization residuals $\sqrt{\lambda} \beta_j$. (b) Compute the Jacobian by chain rule on the composition $\phi \circ (\text{affine})$: each row of $Dr$ comes from differentiating one residual through the sigmoid and the affine map. (c) Apply Levenberg–Marquardt — adaptive trust parameter, regularized inner subproblem. The result is the maximum-likelihood-like classifier with smooth loss.

**Key decision point.** The non-obvious choice is *what to do with the regularization term* in the residual map. We could add $\lambda \|\beta\|^2$ to the objective and not include it in $r$, but that breaks the sum-of-squares structure. The clean fix is to *include the regularization as $p$ extra residuals* $r_{N+1}(\theta) = \sqrt{\lambda} \beta_1, \ldots, r_{N+p}(\theta) = \sqrt{\lambda} \beta_p$. The full residual map is $r : \mathbb{R}^{p+1} \to \mathbb{R}^{N+p}$, and $\|r(\theta)\|^2 = \sum_i (\phi(\cdot) - y^{(i)})^2 + \lambda \|\beta\|^2$ exactly. This way the whole objective is a sum of squares and LM applies directly.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra XII — Applied III — Nonlinear Least Squares#Legal Operations|the topic page's Legal Operations]]:

1. **Linearize the residual at the current iterate** (operation 1). The LM inner subproblem linearizes $r(\theta)$ via its Jacobian $Dr(\theta)$.

2. **Regularize the step by adding a trust-region penalty** (operation 2). The LM trust-region term $\lambda^{(k)} \|\theta - \theta^{(k)}\|^2$ keeps inner-loop steps bounded. *Note: the trust-region $\lambda^{(k)}$ has nothing to do with the regularization parameter $\lambda$ from the classification objective — they are coincidentally both called $\lambda$ in the literature.*

3. **Replace a non-differentiable component with a smooth surrogate** (operation 6). The whole exercise turns on replacing $\operatorname{sign}$ by $\phi = \tanh$. Without this replacement, the classification error $\sum (\operatorname{sign}(\cdot) - y)^2$ is non-differentiable and the chapter's algorithms do not apply.

4. **Add a regularization term to nonlinear model fitting** (operation 10). The $\lambda \|\beta\|^2$ term is added by including $p$ extra residuals $\sqrt{\lambda} \beta_j$, preserving the sum-of-squares structure.

---

# Hints

> [!note]- Hint 1
> The full variable is $\theta = (\beta, v) \in \mathbb{R}^{p+1}$. The $i$th data residual is $r_i(\theta) = \phi(\beta^T x^{(i)} + v) - y^{(i)}$ for $i = 1, \ldots, N$. The regularization residuals are $r_{N+j}(\theta) = \sqrt{\lambda} \beta_j$ for $j = 1, \ldots, p$. The total residual map $r$ has $N + p$ components.

> [!note]- Hint 2
> The derivative of a composition $u \mapsto \phi(\beta^T x + v)$ with respect to $(\beta, v)$ uses the chain rule: $\partial/\partial \beta_j (\phi \cdot) = \phi'(\cdot) \cdot x_j$ and $\partial/\partial v = \phi'(\cdot)$. So row $i$ of $Dr$ (for the data residuals) is $\phi'(\beta^T x^{(i)} + v) \cdot (x^{(i)T}, 1)$.

> [!note]- Hint 3
> The regularization residual $r_{N+j} = \sqrt{\lambda} \beta_j$ has derivative $\sqrt{\lambda}$ with respect to $\beta_j$ and $0$ otherwise. So the regularization block of $Dr$ is $\sqrt{\lambda} \begin{pmatrix} I_p & 0 \end{pmatrix}$ (an $p \times (p+1)$ block).

> [!note]- Hint 4
> The sigmoid replacement gains the differentiability needed to apply Levenberg–Marquardt. With $\operatorname{sign}$, the gradient is zero almost everywhere and undefined at zero crossings, so no gradient-based algorithm works directly. With $\phi$, the gradient is smooth, and minimizing $\sum (\phi(\cdot) - y)^2$ approximates "make $\operatorname{sign}(\beta^T x + v) = y$ on as many training examples as possible," which is what we want for classification.

> [!note]- Hint 5
> Levenberg–Marquardt is generic — at each iteration, evaluate $r(\theta^{(k)})$ and $Dr(\theta^{(k)})$, solve the regularized normal equations $(Dr^T Dr + \lambda^{(k)} I) p = -Dr^T r$, update $\theta^{(k+1)} = \theta^{(k)} + p$, adapt $\lambda^{(k)}$. The only problem-specific code is the $r$ and $Dr$ evaluation.

---

# Solution

The plan is to (i) write down the residual map and its Jacobian explicitly, (ii) explain why the smooth surrogate is preferable to the linear-LS classifier, and (iii) describe the LM iteration in a way that exposes which parts are generic and which are problem-specific.

**Step 1: The residual map and its Jacobian.**

Let $\theta = (\beta_1, \ldots, \beta_p, v) \in \mathbb{R}^{p+1}$. The residual map $r : \mathbb{R}^{p+1} \to \mathbb{R}^{N + p}$ is
$$r_i(\theta) = \phi(\beta^T x^{(i)} + v) - y^{(i)}, \quad i = 1, \ldots, N$$
(data residuals), and
$$r_{N+j}(\theta) = \sqrt{\lambda} \, \beta_j, \quad j = 1, \ldots, p$$
(regularization residuals). The objective is $\|r(\theta)\|^2$.

The Jacobian $Dr(\theta)$ is a $(N + p) \times (p + 1)$ matrix with two blocks:
$$Dr(\theta) = \begin{pmatrix} \phi'(\beta^T x^{(1)} + v) \cdot (x^{(1)T} \mid 1) \\ \phi'(\beta^T x^{(2)} + v) \cdot (x^{(2)T} \mid 1) \\ \vdots \\ \phi'(\beta^T x^{(N)} + v) \cdot (x^{(N)T} \mid 1) \\ \hline \sqrt{\lambda} \, I_p \mid 0 \end{pmatrix} = \begin{pmatrix} D r_\text{data}(\theta) \\ D r_\text{reg} \end{pmatrix}.$$

> [!note]- Derivation
> The objective $\|r(\theta)\|^2 = \sum_{i=1}^N r_i^2 + \sum_{j=1}^p r_{N+j}^2 = \sum_i (\phi(\beta^T x^{(i)} + v) - y^{(i)})^2 + \lambda \sum_j \beta_j^2$, exactly matching the problem statement. So $\|r\|^2$ *is* the regularized classification objective; LM applied to $r$ minimizes this objective.
>
> **Jacobian of the data residuals.** For $r_i(\theta) = \phi(\beta^T x^{(i)} + v) - y^{(i)}$, applying the chain rule:
> $$\frac{\partial r_i}{\partial \beta_j} = \phi'(\beta^T x^{(i)} + v) \cdot x^{(i)}_j, \qquad \frac{\partial r_i}{\partial v} = \phi'(\beta^T x^{(i)} + v).$$
> So row $i$ of $D r_\text{data}$ is $\phi'(\beta^T x^{(i)} + v) \cdot (x^{(i)}_1, \ldots, x^{(i)}_p, 1)$, where the final $1$ is the partial with respect to $v$. Compactly, if we write $u^{(i)} = \beta^T x^{(i)} + v$ and $d_i = \phi'(u^{(i)}) = 1 - \phi(u^{(i)})^2$, the data block of the Jacobian is $D r_\text{data} = \operatorname{diag}(d) \, X$, where $X \in \mathbb{R}^{N \times (p+1)}$ is the augmented data matrix with rows $(x^{(i)T}, 1)$.
>
> **Jacobian of the regularization residuals.** For $r_{N+j}(\theta) = \sqrt{\lambda} \beta_j$, $\partial r_{N+j}/\partial \beta_j = \sqrt{\lambda}$ and all other partials are $0$. So $D r_\text{reg} = \sqrt{\lambda} \begin{pmatrix} I_p & 0 \end{pmatrix}$ — a $p \times (p+1)$ block with $\sqrt{\lambda}$ on the first $p$ diagonal entries and a zero column for the partial with respect to $v$ (the offset is not regularized).
>
> Stacking: $Dr(\theta) = \begin{pmatrix} \operatorname{diag}(d) X \\ \sqrt{\lambda} (I_p \mid 0) \end{pmatrix}$.

**Step 2: Why the sigmoid surrogate is preferable.**

The sigmoid replacement gains *differentiability* and *better-than-linear-LS classification accuracy* simultaneously.

> [!note]- Derivation
> **Differentiability.** With $\phi$, the residual map $r$ is smooth, $Dr$ exists everywhere, and the algorithms of this chapter (LM in particular) apply directly. With $\operatorname{sign}$, the residual is non-differentiable at zero crossings, so the gradient is undefined; even if it were defined elsewhere (it is zero everywhere $\operatorname{sign}$ is constant), gradient-based optimization could not make progress because the gradient gives no information about the right direction.
>
> **Classification accuracy.** Boyd reports that on the MNIST digit-zero recognition problem, the linear LS classifier (minimize $\sum (\beta^T x + v - y)^2$) achieves test error $1.6\%$, while the sigmoid LS classifier (minimize $\sum (\phi(\beta^T x + v) - y)^2$) achieves test error $0.7\%$. The improvement comes from the loss function being closer to what we want: the linear LS loss $(\beta^T x + v - y)^2$ penalizes the *prediction* $\beta^T x + v$ being far from $y \in \{-1, +1\}$ even when the sign is correct — a confident correct prediction $\beta^T x + v = 10$ is "wrong" by the linear LS loss. The sigmoid LS loss $(\phi(\beta^T x + v) - y)^2 \leq (1 - (-1))^2 = 4$ saturates: it cares about the *sign* of the prediction, with the magnitude only refining confidence near the decision boundary.
>
> Geometrically, the linear LS loss is a paraboloid in $(\beta, v)$, and its minimum may not be at the maximum-classification-accuracy point. The sigmoid LS loss is a *bounded* function (each residual is at most $2$ in magnitude), and its minimum is much closer to the maximum-classification-accuracy point.

**Step 3: Levenberg–Marquardt iteration sketch.**

> [!note]- Derivation
> The LM iteration for this problem is *exactly* the standard LM iteration with the problem-specific $r$ and $Dr$ formulas plugged in:
>
> 1. **Initialize.** $\theta^{(1)}$ arbitrary (e.g., $\beta = 0$, $v = 0$, which makes the first iteration a linear-LS-classifier iteration); $\lambda^{(1)} = 1$ (trust parameter).
>
> 2. **At each iteration $k$:**
>    - *Evaluate residuals and Jacobian.* Compute $u^{(i)} = \beta^T x^{(i)} + v$ for all $i$, then $r_i = \phi(u^{(i)}) - y^{(i)}$ and $d_i = 1 - \phi(u^{(i)})^2$. Form $r(\theta^{(k)})$ and $Dr(\theta^{(k)})$ as in Step 1.
>    - *Solve regularized linear LS subproblem.* Find $p \in \mathbb{R}^{p+1}$ minimizing $\|Dr p + r\|^2 + \lambda^{(k)} \|p\|^2$. The closed form is $p = -(Dr^T Dr + \lambda^{(k)} I)^{-1} Dr^T r$, but the stacked-matrix QR factorization is numerically more stable.
>    - *Tentative update.* Set $\theta^{(k+1)} = \theta^{(k)} + p$.
>    - *Accept or reject.* Evaluate $\|r(\theta^{(k+1)})\|^2$. If smaller than $\|r(\theta^{(k)})\|^2$, accept and shrink $\lambda^{(k+1)} = 0.8 \lambda^{(k)}$. Otherwise reject ($\theta^{(k+1)} \leftarrow \theta^{(k)}$) and grow $\lambda^{(k+1)} = 2 \lambda^{(k)}$.
>    - *Termination test.* Stop when $\|r(\theta^{(k)})\|^2$ is small enough or change between iterates is negligible.
>
> 3. **Problem-specific vs generic.** The only problem-specific code is the residual and Jacobian evaluation (Step 2a). The rest of the algorithm — the regularized inner solve, the acceptance test, the trust-parameter adaptation — is *identical to any other LM application*. This is why off-the-shelf LM libraries (`scipy.optimize.leastsq`, MINPACK) take a residual map and an optional Jacobian as input, then run the generic algorithm.

> [!note]- Complete formal solution
> **(a) Residual map.** Set $\theta = (\beta, v) \in \mathbb{R}^{p+1}$. Define
> $$r_i(\theta) = \phi(\beta^T x^{(i)} + v) - y^{(i)} \;\; (i = 1, \ldots, N), \qquad r_{N+j}(\theta) = \sqrt{\lambda} \beta_j \;\; (j = 1, \ldots, p).$$
> Then $\|r(\theta)\|^2 = \sum_i (\phi(\beta^T x^{(i)} + v) - y^{(i)})^2 + \lambda \|\beta\|^2$, the regularized classification objective.
>
> The Jacobian $Dr(\theta) \in \mathbb{R}^{(N+p) \times (p+1)}$ has two blocks:
> $$D r_\text{data} = \operatorname{diag}(d) \begin{pmatrix} X & \mathbf{1} \end{pmatrix}, \qquad D r_\text{reg} = \sqrt{\lambda} \begin{pmatrix} I_p & 0 \end{pmatrix},$$
> where $X$ is the $N \times p$ data matrix with rows $x^{(i)T}$, $\mathbf{1}$ is a column of ones, and $d_i = 1 - \phi(\beta^T x^{(i)} + v)^2$.
>
> **(b) Why preferable.** The sigmoid replacement makes the objective *differentiable*, which is required for any gradient-based optimization including LM. Without the sigmoid, the classification error $\sum (\operatorname{sign}(\cdot) - y)^2$ is piecewise constant and gradient methods fail. Beyond differentiability, the sigmoid loss is *bounded* (each residual at most $2$ in magnitude), so the optimization is not dominated by a few extreme examples, and the resulting classifier achieves substantially lower test error than the linear-LS classifier — on MNIST digit zero, $0.7\%$ vs $1.6\%$ test error.
>
> **(c) Levenberg–Marquardt.** At each iteration, evaluate $r(\theta^{(k)})$ and $Dr(\theta^{(k)})$ using the formulas above; solve the regularized inner LS problem $\min_p \|Dr p + r\|^2 + \lambda^{(k)} \|p\|^2$; update $\theta^{(k+1)} = \theta^{(k)} + p$; accept or reject based on whether $\|r(\theta^{(k+1)})\|^2 < \|r(\theta^{(k)})\|^2$, adapting $\lambda^{(k)}$ accordingly. Only the residual/Jacobian evaluation is problem-specific; the rest is generic LM machinery. $\blacksquare$

> [!warning] Illegal but tempting alternative — minimize sum of cross-entropy losses instead
> A more "standard" formulation of logistic regression minimizes the cross-entropy loss $\sum_i \log(1 + e^{-y^{(i)} (\beta^T x^{(i)} + v)})$ instead of $\sum_i (\phi(\beta^T x^{(i)} + v) - y^{(i)})^2$. This is the maximum-likelihood logistic regression and is more common in statistical practice. The two loss functions give *similar* parameters in practice but are formally different. The cross-entropy loss is *not* a sum of squares, so LM does not directly apply — one uses Newton's method on the log-likelihood, or iteratively-reweighted-least-squares (IRLS), which is a *particular form* of Gauss–Newton for the cross-entropy loss. Boyd's exposition stays within the nonlinear-LS framework by using the squared-sigmoid loss; the equivalence with standard logistic regression is approximate but tight.

---

# Key Takeaways

**Smooth surrogates turn classification into nonlinear LS, unlocking the chapter's algorithms.** The single most important idea of this exercise is the *substitution* $\operatorname{sign} \to \phi$. This converts a classification problem — fundamentally about discrete labels — into a regression-style nonlinear LS problem with smooth residuals. The chapter's algorithms then apply unchanged. This substitution is the *master pattern* for converting discrete or piecewise-constant problems into smooth-optimization problems: replace $\operatorname{sign}$ by $\tanh$, replace $\max(u, 0)$ by softplus $\log(1 + e^u)$ or the smoothed-max $(u + \sqrt{u^2 + \epsilon^2})/2$, replace $\operatorname{argmax}$ by softmax. Each smooth surrogate has its own derivative formulas and its own trade-offs (steepness vs accuracy of approximation), but the framework is unified. Whenever you encounter a problem with discrete labels, indicator functions, or piecewise-constant operators, ask: *what is the smooth surrogate?* — and the chapter's nonlinear-LS toolkit will likely apply.

**The Jacobian factors via the chain rule when the residual is a composition.** The data residuals $r_i = \phi(\beta^T x^{(i)} + v) - y^{(i)}$ are compositions: an affine function $u = \beta^T x + v$, then a scalar nonlinearity $\phi$. The Jacobian is the product of the Jacobians of the pieces: $\frac{\partial r_i}{\partial \theta_j} = \phi'(u) \cdot \frac{\partial u}{\partial \theta_j}$. This factoring is generic: any composition of the form "smooth scalar nonlinearity ∘ affine map" has this Jacobian structure, and the affine-map Jacobian is just the coefficient matrix of the affine map. For neural networks, the same pattern compounds: a deep network is a sequence of compositions, and the full Jacobian factors as a product over layers — *backpropagation* is the systematic right-to-left evaluation of this product. The lesson is to recognize "smooth nonlinearity ∘ affine" structure, then write the Jacobian as a diagonal-scaled coefficient matrix; this avoids deriving partial derivatives from scratch.

**LM machinery is generic; only $r$ and $Dr$ are problem-specific.** The Levenberg–Marquardt algorithm is the *same* whether you are fitting an exponential decay model, computing camera bundle adjustment, training a neural network with squared loss, or doing logistic regression as in this exercise. The only thing that changes between applications is the residual map $r$ and its Jacobian $Dr$. This factoring is what makes off-the-shelf LM libraries (`scipy.optimize.leastsq`, `lmfit`, MATLAB `lsqnonlin`) usable: they take $r$ and $Dr$ (or compute $Dr$ by finite differences) and run the generic adaptive iteration. When implementing a new nonlinear-LS application, the engineering rule is: *spend your effort getting $r$ and $Dr$ right, and let the LM library handle the iteration*. The trust-parameter adaptation, the convergence checks, the linear-system solves — all are generic and well-tested.
