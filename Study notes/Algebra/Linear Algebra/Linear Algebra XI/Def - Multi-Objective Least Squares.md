---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

A multi-objective LS problem has $k$ objectives, each a squared norm $J_i = \|A_i x - b_i\|^2$, with $A_i$ an $m_i \times n$ matrix and $b_i$ an $m_i$-vector. The weights $\lambda_1, \ldots, \lambda_k > 0$ trade off the objectives. The *stacked matrix* and *stacked vector* are
$$\tilde{A} = \begin{pmatrix} \sqrt{\lambda_1} A_1 \\ \sqrt{\lambda_2} A_2 \\ \vdots \\ \sqrt{\lambda_k} A_k \end{pmatrix}, \qquad \tilde{b} = \begin{pmatrix} \sqrt{\lambda_1} b_1 \\ \sqrt{\lambda_2} b_2 \\ \vdots \\ \sqrt{\lambda_k} b_k \end{pmatrix},$$
of size $(m_1 + \cdots + m_k) \times n$ and $m_1 + \cdots + m_k$ respectively. A point $\hat{x}(\lambda)$ in the *Pareto-optimal set* is one for which no other point dominates it in all objectives simultaneously.

---

# Axiom Motivation

In many problems we want $x$ to simultaneously achieve several things — small training error *and* small parameter norm, fast tracking of a target *and* small control effort, fidelity to noisy measurements *and* consistency with a model. Each desideratum is naturally expressed as "make $\|A_i x - b_i\|^2$ small" for some matrix $A_i$ and target $b_i$. There are $k$ such desiderata.

The naive approach — try to minimize each $J_i$ separately — typically gives $k$ different minimizers, no single $x$. We have to *commit* to a tradeoff: how much do we care about each $J_i$ relative to the others?

The cleanest formalization is a *weighted sum*:
$$J(x) = \lambda_1 J_1(x) + \lambda_2 J_2(x) + \cdots + \lambda_k J_k(x),$$
where $\lambda_i > 0$ are positive weights expressing the relative importance of each objective. Minimizing $J$ gives a single $x = \hat{x}(\lambda_1, \ldots, \lambda_k)$. Sweeping the weights traces out the *Pareto-optimal set* — the set of $x$ that cannot be improved in any one objective without worsening another.

Why a *weighted sum* and not some other aggregation (max, geometric mean, etc.)? Three reasons:

(i) *Convexity preservation.* The sum of convex functions is convex; in particular, the sum of quadratic functions is quadratic. The weighted-sum objective $J(x)$ is itself a quadratic function of $x$, so its minimization is itself a least squares problem — solvable in closed form by the same machinery as §XI.1.

(ii) *Pareto-optimality.* Any minimizer of a positive weighted sum is Pareto-optimal: no other point achieves all $J_i$ values less than or equal to the minimizer's, with at least one strict. The proof is one line: if $z$ dominates $\hat{x}(\lambda)$, then $\sum \lambda_i J_i(z) < \sum \lambda_i J_i(\hat{x}(\lambda))$, contradicting the minimization. So the weighted-sum minimizers are *all* Pareto-optimal; sweeping weights generates the entire Pareto frontier (or at least its convex hull).

(iii) *Interpretation.* The weight $\lambda_i$ can be read as "the rate at which we are willing to trade off $J_1$ for $J_i$" near the optimum — at $\hat{x}(\lambda)$, the gradient $\nabla J_i$ is proportional to $1/\lambda_i$ in some direction sense. This makes $\lambda$ tunable: increase $\lambda_2$ if you want $J_2$ smaller (at the cost of bigger $J_1$, $J_3$, etc.).

The deep observation is that the weighted-sum problem reduces to a *single* LS problem with stacked matrices. Define $\tilde{A}$ to stack $\sqrt{\lambda_i} A_i$ vertically and $\tilde{b}$ to stack $\sqrt{\lambda_i} b_i$ vertically. Then
$$J(x) = \sum_i \lambda_i \|A_i x - b_i\|^2 = \sum_i \|\sqrt{\lambda_i}(A_i x - b_i)\|^2 = \|\tilde{A} x - \tilde{b}\|^2.$$
So the multi-objective LS problem is *literally* an LS problem with the stacked matrix and right-hand side. All the §XI.1 machinery — normal equations, QR factorization, pseudoinverse — applies unchanged. No new mathematics is needed; what is new is the *recognition* that the problem has this structure.

This is the structural reason why so many applications in §XI.2–§XI.3 reduce to LS: they are multi-objective problems whose objectives are all quadratic in the unknown. Data fitting with regularization (Tikhonov), constrained problems (in the limit of large weight on the constraint), control (output vs. input cost), estimation (measurement consistency vs. model consistency) — all are multi-objective LS in disguise.

The remaining question is *how to choose the weights*. There is no universal answer; it depends on the application. In data fitting with regularization, $\lambda$ is chosen by cross-validation to minimize test error. In control, $\rho$ (the weight on input cost) is chosen by hand-tuning until the system behaves acceptably. In estimation, $\lambda$ is chosen by validation against held-out measurements. The weights are *knobs* that tune the trade-off; choosing them well is part of the engineering practice.

---

# The Definition

> **Definition (Multi-Objective Least Squares).** Given $k$ objectives, each defined by an $m_i \times n$ matrix $A_i$ and an $m_i$-vector $b_i$, and positive weights $\lambda_1, \ldots, \lambda_k > 0$, the *multi-objective least squares problem* is to find an $n$-vector $\hat{x}$ that minimizes the weighted sum
> $$J(x) = \lambda_1 \|A_1 x - b_1\|^2 + \cdots + \lambda_k \|A_k x - b_k\|^2.$$
> Equivalently, $J(x) = \|\tilde{A} x - \tilde{b}\|^2$ where $\tilde{A}$ and $\tilde{b}$ are the stacked matrix and vector (with rows scaled by $\sqrt{\lambda_i}$). Provided the stacked matrix $\tilde{A}$ has linearly independent columns, the solution is unique and given by
> $$\hat{x} = (\tilde{A}^T \tilde{A})^{-1} \tilde{A}^T \tilde{b} = \left(\sum_i \lambda_i A_i^T A_i\right)^{-1} \left(\sum_i \lambda_i A_i^T b_i\right).$$
> The set of $\hat{x}(\lambda)$ as the weights vary over $(\mathbb{R}_{>0})^k$ is contained in the *Pareto-optimal set*: no $\hat{x}(\lambda)$ can be improved in all $k$ objectives simultaneously.

**Note on independent-column assumption.** The stacked matrix $\tilde{A}$ has linearly independent columns iff no nonzero $x$ satisfies $A_i x = 0$ for *all* $i$. This is *weaker* than requiring each individual $A_i$ to have linearly independent columns — even if every $A_i$ is wide (rank-deficient), their stacking can have full column rank, because different objectives can constrain different directions in $x$-space.

---

# Relate to Other Fields / Compression

**True name:** multi-objective LS is *single-objective LS with stacked data*. The "multi-objective" framing is a *conceptual* organization (what does each objective represent?) but the *computational* content is one ordinary LS problem with a vertically concatenated matrix. The trick is the recognition that quadratic objectives compose by stacking, with the weights becoming square-root scalings.

This is the same construction as:
- **Tikhonov Regularization** (numerical analysis): the regularized LS problem $\min \|Ax - b\|^2 + \lambda \|x\|^2$ is multi-objective LS with $k = 2$, $A_1 = A, b_1 = b, A_2 = I, b_2 = 0$. See [[Def - Regularized Least Squares]].
- **Scalarization in Multi-Objective Optimization**: in optimization theory, replacing a multi-objective problem $\min (f_1(x), \ldots, f_k(x))$ with a weighted sum $\min \sum \lambda_i f_i(x)$ is called *linear scalarization*. It is one of several scalarization techniques; others (Tchebycheff, $\varepsilon$-constraint) recover non-convex parts of the Pareto front that linear scalarization misses.
- **Bayesian MAP Estimation**: in Bayesian regression, the MAP estimator under a Gaussian prior and Gaussian likelihood is $\arg\min \|Ax - b\|^2 / \sigma^2 + \|x\|^2 / \tau^2$ — exactly multi-objective LS with the variances as weights.

---

# Examples / Corollaries

*Example 1 (Tikhonov as multi-objective LS).* The Tikhonov problem $\min \|Ax - b\|^2 + \lambda \|x\|^2$ is multi-objective LS with two objectives: $J_1 = \|Ax - b\|^2$ (data fidelity) and $J_2 = \|x\|^2$ (parameter norm), with weights $\lambda_1 = 1, \lambda_2 = \lambda$. The stacked matrix is $\tilde{A} = \binom{A}{\sqrt{\lambda} I}$ and the LS solution is $\hat{x} = (A^T A + \lambda I)^{-1} A^T b$. See [[Ex - Tikhonov regularization is a multi-objective LS problem]].

*Example 2 (smoothness regularization).* Fit a smooth signal $x$ to noisy data $y$: minimize $\|x - y\|^2 + \lambda \|Dx\|^2$, where $D$ is the first-difference matrix (with $(Dx)_i = x_{i+1} - x_i$). The two objectives are data fidelity and total variation of the signal; large $\lambda$ smooths heavily, small $\lambda$ follows the data. The stacked matrix is $\binom{I}{\sqrt{\lambda} D}$.

*Example 3 (bi-criterion trade-off curve).* For $k = 2$, varying $\lambda = \lambda_2 / \lambda_1$ over $(0, \infty)$ traces out the *optimal trade-off curve* in the $(J_1, J_2)$ plane. The curve is convex and decreasing: large $\lambda$ gives small $J_2$ and large $J_1$, small $\lambda$ gives the opposite. The shape of the curve is the key diagnostic — a sharp "knee" identifies the natural tradeoff point.

*Example 4 (control problem — output vs. input cost).* In linear quadratic control (§17.2), $J_1 = \sum \|y_t\|^2$ (output deviation from target) and $J_2 = \rho \sum \|u_t\|^2$ (input effort). The two objectives are stacked, the dynamics constraint is added, and the result is a constrained multi-objective LS problem. Sweeping $\rho$ traces a Pareto front of "track output well at high input cost" through "save input at the cost of output accuracy."

*Example 5 (NOT a multi-objective LS — non-quadratic objective).* The problem $\min \|Ax - b\|^2 + \lambda \|x\|_1$ (LASSO) has a quadratic data-fidelity term and a *non-quadratic* (L1) penalty. This is not a multi-objective LS problem in the sense of this definition; the L1 penalty makes the problem non-quadratic and the solution is no longer closed-form. The LASSO is the canonical example of a regularized LS variant that *breaks* the multi-objective LS framework, and it requires different algorithms (coordinate descent, ADMM).

**Calibration check.** Verify: (i) when $k = 1$, multi-objective LS reduces to ordinary LS; (ii) when $A_i = I, b_i = b^{(i)}$ for $i = 1, \ldots, k$ (scalar case), the solution is the *weighted average* $\hat{x} = (\sum \lambda_i b^{(i)})/(\sum \lambda_i)$ — multi-objective LS recovers weighted averaging; (iii) for $k = 2$, increasing $\lambda_2 / \lambda_1$ monotonically increases $J_1(\hat{x})$ and monotonically decreases $J_2(\hat{x})$, sweeping along the Pareto curve.

---

# Unlocked by This

> [!tip] Scalarization Methods *(from Multi-Objective Optimization)*
> Multi-objective LS is the linear-scalarization approach to vector optimization. Other approaches — **Tchebycheff scalarization** ($\min \max_i \lambda_i (J_i - J_i^*)$), **$\varepsilon$-constraint method** (minimize $J_1$ subject to $J_i \leq \varepsilon_i$ for $i \geq 2$) — can recover Pareto-optimal points that linear scalarization misses (when the Pareto front is non-convex). The $\varepsilon$-constraint form, in particular, is the limit of multi-objective LS as one weight goes to infinity, recovering constrained LS.

> [!tip] Bayesian Hierarchical Models *(from Bayesian Statistics)*
> Multi-objective LS with weights chosen by validation has a Bayesian interpretation as a hierarchical model with a Gaussian prior on $x$ and a Gaussian likelihood for $b$. The weights $\lambda_i$ are the *precisions* (inverse variances) of the respective distributions. Estimating the weights themselves by empirical Bayes (or by hyperparameter cross-validation) puts a prior on the priors, giving a fully principled framework for model selection. The bridge: validation chooses the noise-to-prior ratio, and the result is the MAP estimator of the Bayesian hierarchical model.
