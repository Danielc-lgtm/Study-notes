---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Regularized Least Squares"
  - "Def - Multi-Objective Least Squares"
tags: [algebra, linear-algebra, applied, regularization]
---

# Problem Statement

Show that the *Tikhonov regularized least squares problem*
$$\min_x \|Ax - b\|^2 + \lambda \|x\|^2,$$
with $A$ an $m \times n$ matrix, $b$ an $m$-vector, and $\lambda > 0$, is *literally* a single ordinary least squares problem with a *stacked* design matrix and a stacked right-hand side. Specifically:

1. Construct the stacked matrix $\tilde{A}$ and vector $\tilde{b}$ such that
$$\|Ax - b\|^2 + \lambda \|x\|^2 = \|\tilde{A} x - \tilde{b}\|^2.$$

2. Verify that $\tilde{A}$ has linearly independent columns for *any* $\lambda > 0$, regardless of properties of $A$ alone (which can be wide, tall, or rank-deficient).

3. Show that the resulting LS solution $\hat{x}(\lambda) = (\tilde{A}^T \tilde{A})^{-1} \tilde{A}^T \tilde{b}$ matches the standard Tikhonov formula
$$\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b.$$

**Recall:**

A [[Def - Multi-Objective Least Squares|multi-objective least squares problem]] $\min \sum_i \lambda_i \|A_i x - b_i\|^2$ can be expressed as a single LS problem $\min \|\tilde{A} x - \tilde{b}\|^2$ with the stacked matrix and right-hand side
$$\tilde{A} = \begin{pmatrix} \sqrt{\lambda_1} A_1 \\ \sqrt{\lambda_2} A_2 \\ \vdots \\ \sqrt{\lambda_k} A_k \end{pmatrix}, \qquad \tilde{b} = \begin{pmatrix} \sqrt{\lambda_1} b_1 \\ \sqrt{\lambda_2} b_2 \\ \vdots \\ \sqrt{\lambda_k} b_k \end{pmatrix}.$$
[[Def - Regularized Least Squares|Tikhonov regularization]] is the special case $k = 2$ with $A_1 = A, b_1 = b, A_2 = I, b_2 = 0, \lambda_1 = 1, \lambda_2 = \lambda$.

---

# Convergent Strategy

**Problem class:** This is a *recognition* exercise: show that one well-known problem (Tikhonov) is a specialization of a more general framework (multi-objective LS). The class is "verify that two formulations of an optimization problem are equivalent by showing they have the same objective function." Such recognitions are at the heart of structural understanding in linear algebra; the payoff is that algorithms developed for the general framework apply unchanged to the specialized problem.

**Assumption pattern:** $A$ is an arbitrary $m \times n$ matrix (no rank assumption), $b$ an arbitrary $m$-vector, $\lambda > 0$ a positive regularization parameter. The flexibility — no rank assumption on $A$ — is what makes Tikhonov robust to ill-conditioned and even rank-deficient problems. The single positivity assumption $\lambda > 0$ is what makes the regularized problem well-posed.

**Theorem routing:** Apply [[Def - Multi-Objective Least Squares|the multi-objective LS framework]] with $k = 2$: form the stacked matrix $\tilde{A} = \binom{A}{\sqrt{\lambda} I}$ and stacked vector $\tilde{b} = \binom{b}{0}$. Verify by direct computation that $\|\tilde{A} x - \tilde{b}\|^2 = \|Ax - b\|^2 + \lambda \|x\|^2$. Verify that $\tilde{A}^T \tilde{A} = A^T A + \lambda I$, which is positive definite for any $\lambda > 0$. Apply [[Thm - Existence and Uniqueness of Least Squares Solution]] to conclude that the LS solution is $\hat{x}(\lambda) = (\tilde{A}^T \tilde{A})^{-1} \tilde{A}^T \tilde{b} = (A^T A + \lambda I)^{-1} A^T b$.

**Key decision point:** The non-obvious step is recognizing that the $\sqrt{\lambda}$ factor (rather than $\lambda$) is what gets stacked into $\tilde{A}$ — this is because the objective involves *squared* terms $\lambda \|x\|^2 = \|\sqrt{\lambda} x\|^2$, so the multiplier inside the norm-squared is $\sqrt{\lambda}$. A common mistake is to put $\lambda$ instead of $\sqrt{\lambda}$; this gives the wrong objective by a factor.

---

# Legal Operations Used

1. **Stack matrices to convert multi-objective LS to single-objective LS.** (Operation 3 from the topic page.) Vertically stack $A$ on top of $\sqrt{\lambda} I$ to form the augmented design matrix. The objective $\|Ax - b\|^2 + \lambda \|x\|^2$ becomes $\|\tilde{A} x - \tilde{b}\|^2$ for $\tilde{b} = (b, 0)^T$.

2. **Recognize Tikhonov as multi-objective LS.** (Operation 4 from the topic page.) Specialize the multi-objective framework with $k = 2$, $\lambda_1 = 1$, $\lambda_2 = \lambda$, $A_2 = I$, $b_2 = 0$.

3. **Form the regularized normal equations and verify invertibility.** $\tilde{A}^T \tilde{A} = A^T A + \lambda I$ is positive definite for $\lambda > 0$, even when $A^T A$ alone is singular. This is the cleanness benefit of Tikhonov: the regularization parameter makes the problem unconditionally well-posed.

---

# Hints

> [!note]- Hint 1
> Use the multi-objective LS stacking trick: $\|A_1 x - b_1\|^2 + \lambda \|A_2 x - b_2\|^2 = \|\tilde{A} x - \tilde{b}\|^2$ with $\tilde{A}$ stacking $\sqrt{\lambda}$-scaled rows.

> [!note]- Hint 2
> The Tikhonov problem fits with $A_1 = A, A_2 = I, b_1 = b, b_2 = 0$ and weights $\lambda_1 = 1, \lambda_2 = \lambda$.

> [!note]- Hint 3
> Compute $\tilde{A}^T \tilde{A}$ directly. The block structure of $\tilde{A}$ makes the calculation easy.

> [!note]- Hint 4 (near giveaway)
> $\tilde{A}^T \tilde{A} = A^T A + \lambda I$, which is the *regularized Gram matrix* — invertible for any $\lambda > 0$.

---

# Solution

The proof has three steps. Step 1 constructs the stacked matrix and verifies the objective equivalence. Step 2 verifies the invertibility of $\tilde{A}^T \tilde{A}$ for any $\lambda > 0$, regardless of $A$'s rank. Step 3 computes the LS formula and matches the standard Tikhonov solution.

**Step 1: Construct the stacked matrix and verify objective equivalence.**

Define
$$\tilde{A} = \begin{pmatrix} A \\ \sqrt{\lambda} I_n \end{pmatrix}, \qquad \tilde{b} = \begin{pmatrix} b \\ 0_n \end{pmatrix},$$
where $\tilde{A}$ is $(m + n) \times n$ and $\tilde{b}$ is an $(m + n)$-vector. Compute the squared norm of the residual:

> [!note]- Derivation
> $$\tilde{A} x - \tilde{b} = \begin{pmatrix} A \\ \sqrt{\lambda} I \end{pmatrix} x - \begin{pmatrix} b \\ 0 \end{pmatrix} = \begin{pmatrix} Ax - b \\ \sqrt{\lambda} x \end{pmatrix}.$$
> The squared norm is
> $$\|\tilde{A} x - \tilde{b}\|^2 = \left\| \begin{pmatrix} Ax - b \\ \sqrt{\lambda} x \end{pmatrix} \right\|^2 = \|Ax - b\|^2 + \|\sqrt{\lambda} x\|^2 = \|Ax - b\|^2 + \lambda \|x\|^2.$$
> So $\|\tilde{A} x - \tilde{b}\|^2 = \|Ax - b\|^2 + \lambda \|x\|^2$ exactly — the Tikhonov objective is identically the LS objective with the stacked matrices.

**Step 2: Verify invertibility of $\tilde{A}^T \tilde{A}$ for any $\lambda > 0$.**

Compute $\tilde{A}^T \tilde{A}$:

> [!note]- Derivation
> $$\tilde{A}^T \tilde{A} = \begin{pmatrix} A^T & \sqrt{\lambda} I \end{pmatrix} \begin{pmatrix} A \\ \sqrt{\lambda} I \end{pmatrix} = A^T A + \lambda I.$$
> For any vector $v \neq 0$, $v^T (\tilde{A}^T \tilde{A}) v = v^T A^T A v + \lambda v^T v = \|Av\|^2 + \lambda \|v\|^2$. Since $\lambda > 0$ and $\|v\|^2 > 0$, this is strictly positive. Hence $\tilde{A}^T \tilde{A}$ is positive definite, so $\tilde{A}$ has linearly independent columns. By [[Thm - Existence and Uniqueness of Least Squares Solution]], the LS solution is unique.

**Step 3: Compute the LS formula and match the standard Tikhonov solution.**

The unique LS minimizer of $\|\tilde{A} x - \tilde{b}\|^2$ is given by

> [!note]- Derivation
> $$\hat{x}(\lambda) = (\tilde{A}^T \tilde{A})^{-1} \tilde{A}^T \tilde{b}.$$
> Compute $\tilde{A}^T \tilde{b}$:
> $$\tilde{A}^T \tilde{b} = \begin{pmatrix} A^T & \sqrt{\lambda} I \end{pmatrix} \begin{pmatrix} b \\ 0 \end{pmatrix} = A^T b.$$
> Combining with the Gram matrix from Step 2:
> $$\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b.$$
> This is exactly the standard Tikhonov solution.

> [!note]- Complete formal solution
> *Step 1:* Define $\tilde{A} = \binom{A}{\sqrt{\lambda} I}$ and $\tilde{b} = \binom{b}{0}$. Direct computation:
> $$\|\tilde{A} x - \tilde{b}\|^2 = \|Ax - b\|^2 + \|\sqrt{\lambda} x\|^2 = \|Ax - b\|^2 + \lambda \|x\|^2.$$
>
> *Step 2:* $\tilde{A}^T \tilde{A} = A^T A + \lambda I$. For any $v \neq 0$, $v^T (\tilde{A}^T \tilde{A}) v = \|Av\|^2 + \lambda \|v\|^2 > 0$ (since $\lambda > 0, \|v\| > 0$). Hence positive definite, invertible.
>
> *Step 3:* $\tilde{A}^T \tilde{b} = A^T b$, so
> $$\hat{x}(\lambda) = (\tilde{A}^T \tilde{A})^{-1} \tilde{A}^T \tilde{b} = (A^T A + \lambda I)^{-1} A^T b,$$
> matching the standard Tikhonov solution. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to express Tikhonov via the *unstacked* form $\hat{x} = A^\dagger b$ where $A^\dagger$ is the pseudoinverse, on the grounds that "regularization is automatic in the pseudoinverse." This is wrong: the pseudoinverse $A^\dagger = (A^T A)^{-1} A^T$ (for full-column-rank $A$) does *not* incorporate $\lambda$. The SVD-based pseudoinverse $A^+ = V \Sigma^+ U^T$ does provide a minimum-norm solution for the *unregularized* problem, but this is *different from* Tikhonov: Tikhonov $\hat{x}(\lambda) \to A^+ b$ as $\lambda \to 0^+$, but for $\lambda > 0$, Tikhonov gives a *biased* estimator that is *not* the unregularized minimum-norm solution. The two are limits of each other, not the same object.

---

# Key Takeaways

**The stacking trick is the foundation of all multi-objective LS problems.**

Whenever you have two quadratic objectives in $x$, you can express their weighted sum as a *single* LS problem by vertically stacking the matrices (with $\sqrt{\lambda_i}$ weights). This unifies Tikhonov regularization, smoothness-penalty regression, LQR with output and input costs, Kalman estimation with measurement and process noise, and many more. The trigger for using this trick: any problem objective of the form "$\sum_i \lambda_i \|\text{some linear thing}\|^2$"; the reaction is to stack into a single big LS problem.

**Tikhonov regularization makes any LS problem well-posed.**

The remarkable property of Tikhonov is that *any* matrix $A$ — tall, wide, rank-deficient, ill-conditioned — combined with *any* $\lambda > 0$ gives a unique, well-defined LS solution. The Gram matrix $A^T A + \lambda I$ is positive definite for any $\lambda > 0$, regardless of $A$. This is the cleanness that makes Tikhonov the *standard fallback* for any LS problem where ordinary LS would fail or warn. The trigger: any LS problem with ill-conditioned $A$ or unsure column independence; the reaction is to add a small $\lambda > 0$ to regularize.

**The $\sqrt{\lambda}$ factor (not $\lambda$) is what stacks into the matrix.**

This is a notational subtlety that catches almost everyone the first time: the objective $\lambda \|x\|^2$ has its scalar *inside* the norm-squared as $\sqrt{\lambda}$, since $\lambda \|x\|^2 = \|\sqrt{\lambda} x\|^2$. So the stacked matrix has $\sqrt{\lambda} I$, not $\lambda I$. The pattern: if your weighted objective is $\lambda_i \|A_i x - b_i\|^2$, the stacked matrix row is $\sqrt{\lambda_i} A_i$ and the stacked right-hand side is $\sqrt{\lambda_i} b_i$.

This exercise connects directly to [[Thm - Bias-Variance Tradeoff in Regularized LS]] (which uses the regularized formula to derive the MSE-optimal $\lambda$) and to [[Def - Regularized Least Squares]] (which is the definition this exercise is verifying as a stacked-LS problem). It is also the algebraic prerequisite for understanding cross-validation in regularized LS: changing $\lambda$ corresponds to re-solving the stacked LS problem with a different scale on the bottom block.
