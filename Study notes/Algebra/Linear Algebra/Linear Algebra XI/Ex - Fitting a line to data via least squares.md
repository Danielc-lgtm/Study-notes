---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Least Squares Problem"
  - "Def - Normal Equations"
  - "Thm - Existence and Uniqueness of Least Squares Solution"
tags: [algebra, linear-algebra, applied, regression]
---

# Problem Statement

Given $N$ data points $(x_1, y_1), \ldots, (x_N, y_N)$ in the plane, find the parameters $\theta_1, \theta_2$ of the line $\hat{y} = \theta_1 + \theta_2 x$ that minimize the sum of squared vertical residuals
$$L(\theta_1, \theta_2) = \sum_{i=1}^N (y_i - \theta_1 - \theta_2 x_i)^2.$$
Show that the unique minimizer (assuming the $x_i$ are not all equal) is
$$\hat{\theta}_2 = \rho \frac{\mathrm{std}(y)}{\mathrm{std}(x)}, \qquad \hat{\theta}_1 = \mathrm{avg}(y) - \hat{\theta}_2 \mathrm{avg}(x),$$
where $\rho$ is the *correlation coefficient* between the $x_i$ and $y_i$, and the line passes through the centroid $(\mathrm{avg}(x), \mathrm{avg}(y))$.

**Recall:**

A [[Def - Least Squares Problem|least squares problem]] minimizes $\|A\theta - b\|^2$ over $\theta \in \mathbb{R}^n$. When the columns of $A$ are linearly independent, the unique minimizer is given by the [[Def - Normal Equations|normal equations]]
$$A^T A \theta = A^T b,$$
with explicit solution $\hat{\theta} = (A^T A)^{-1} A^T b$. See [[Thm - Existence and Uniqueness of Least Squares Solution]] for the existence-uniqueness statement.

The *correlation coefficient* between two $N$-vectors $u$ and $v$ is
$$\rho = \frac{(u - \mathrm{avg}(u) \mathbf{1})^T (v - \mathrm{avg}(v) \mathbf{1})}{\|u - \mathrm{avg}(u) \mathbf{1}\| \cdot \|v - \mathrm{avg}(v) \mathbf{1}\|}.$$
The *standard deviation* of $u$ is $\mathrm{std}(u) = \|u - \mathrm{avg}(u) \mathbf{1}\|/\sqrt{N}$.

---

# Convergent Strategy

**Problem class:** This is a *closed-form coefficient computation* for a 2-parameter linear regression, following the LS template. The problem class is "fit a linear-in-parameters model to data and derive an explicit formula for the coefficients." Such problems route through the normal equations, with the only labor being symbolic computation of $A^T A$ (the $2 \times 2$ Gram matrix) and $A^T b$ (the 2-vector right-hand side), then inversion of the $2 \times 2$ matrix.

**Assumption pattern:** The data is given as scalar pairs $(x_i, y_i)$, with the assumption that not all $x_i$ are equal (ensuring the design matrix has linearly independent columns). The first column of the design matrix is $\mathbf{1}$ (the intercept); the second column is $x^d = (x_1, \ldots, x_N)$. The two columns are independent iff $x^d$ is not a multiple of $\mathbf{1}$, iff not all $x_i$ are equal. With this assumption, the LS theorem guarantees a unique solution.

**Theorem routing:** Apply [[Thm - Existence and Uniqueness of Least Squares Solution]] to the design matrix $A = [\mathbf{1} | x^d]$. The normal equations $A^T A \hat{\theta} = A^T y$ give the LS solution. Computing $A^T A$ involves the inner products $\mathbf{1}^T \mathbf{1} = N, \mathbf{1}^T x^d = \sum x_i, (x^d)^T x^d = \sum x_i^2$; computing $A^T y$ involves $\mathbf{1}^T y = \sum y_i, (x^d)^T y = \sum x_i y_i$. Invert the $2 \times 2$ matrix using the standard formula, simplify, and express the result in terms of $\mathrm{avg}, \mathrm{std}, \rho$.

**Key decision point:** The non-obvious step is expressing the result in terms of *statistical* quantities (means, standard deviations, correlation coefficient) rather than the raw sums $\sum x_i, \sum x_i^2$. This requires using the *de-meaning* identity: $(u - \mathrm{avg}(u) \mathbf{1})^T (v - \mathrm{avg}(v) \mathbf{1}) = u^T v - N \mathrm{avg}(u) \mathrm{avg}(v)$. With this identity, the LS formula reorganizes into the elegant statistical form $\hat{\theta}_2 = \rho \cdot \mathrm{std}(y)/\mathrm{std}(x)$.

---

# Legal Operations Used

1. **Form the normal equations.** (Operation 1 from the topic page.) Set up $A^T A \theta = A^T b$ for the design matrix $A = [\mathbf{1} | x^d]$ and the target $b = y^d$. The Gram matrix is $2 \times 2$ and easily inverted in closed form.

2. **Compute Gram matrix entries directly.** (Operation 1 from the topic page, refined.) $A^T A$ has entries $(A^T A)_{11} = \mathbf{1}^T \mathbf{1} = N$, $(A^T A)_{12} = (A^T A)_{21} = \mathbf{1}^T x^d = \sum x_i$, $(A^T A)_{22} = (x^d)^T x^d = \sum x_i^2$.

3. **Apply the de-meaning identity to recognize statistical quantities.** This is the key algebraic move that converts raw sums to standard statistical formulae.

---

# Hints

> [!note]- Hint 1
> Set up the design matrix $A$ as an $N \times 2$ matrix with first column all-ones and second column the $x$-values. The LS problem is $\min \|A\theta - y\|^2$.

> [!note]- Hint 2
> Compute the $2 \times 2$ Gram matrix $A^T A$ and the 2-vector $A^T y$. Apply the formula for the inverse of a $2 \times 2$ matrix.

> [!note]- Hint 3
> The slope $\hat{\theta}_2$ involves $N \sum x_i y_i - (\sum x_i)(\sum y_i)$ in the numerator and $N \sum x_i^2 - (\sum x_i)^2$ in the denominator. These are $N \cdot \sum (x_i - \mathrm{avg}(x))(y_i - \mathrm{avg}(y))$ and $N \cdot \sum (x_i - \mathrm{avg}(x))^2$ respectively. Use this to simplify.

> [!note]- Hint 4 (near giveaway)
> The slope simplifies to $\hat{\theta}_2 = (\sum (x_i - \bar{x})(y_i - \bar{y}))/(\sum (x_i - \bar{x})^2)$. Divide numerator and denominator by $N \cdot \mathrm{std}(x) \cdot \mathrm{std}(y)$ in the right way to identify $\rho$. The intercept follows from the first normal equation.

---

# Solution

The proof breaks into three steps. Step 1 forms the design matrix and computes the Gram matrix entries. Step 2 inverts the $2 \times 2$ Gram matrix and applies the LS formula. Step 3 simplifies the result by expressing raw sums in terms of statistical quantities (means, standard deviations, correlation coefficient). The non-obvious step is in Step 3, where the de-meaning identity converts the somewhat opaque LS formula into the elegant slope-via-correlation form.

**Step 1: Form the design matrix and Gram matrix.**

The model $\hat{y} = \theta_1 + \theta_2 x$ has design matrix
$$A = \begin{pmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_N \end{pmatrix} = [\mathbf{1} \,|\, x^d],$$
where $x^d = (x_1, \ldots, x_N)$. The columns of $A$ are linearly independent iff $x^d$ is not a multiple of $\mathbf{1}$, iff not all $x_i$ are equal.

> [!note]- Derivation
> The two columns are linearly dependent iff there exist $a, b$ not both zero with $a \mathbf{1} + b x^d = 0$, i.e., $a + b x_i = 0$ for all $i$. If $b = 0$, then $a = 0$ — contradicting "not both zero." If $b \neq 0$, then $x_i = -a/b$ for all $i$ — all $x_i$ equal. Hence linear independence ⟺ not all $x_i$ equal.

**Step 2: Compute the Gram matrix and right-hand side, then invert.**

$A^T A$ and $A^T y$ have entries:

> [!note]- Derivation
> $A^T A = \begin{pmatrix} \mathbf{1}^T \mathbf{1} & \mathbf{1}^T x^d \\ (x^d)^T \mathbf{1} & (x^d)^T x^d \end{pmatrix} = \begin{pmatrix} N & \sum_i x_i \\ \sum_i x_i & \sum_i x_i^2 \end{pmatrix}$.
>
> $A^T y = \begin{pmatrix} \mathbf{1}^T y \\ (x^d)^T y \end{pmatrix} = \begin{pmatrix} \sum_i y_i \\ \sum_i x_i y_i \end{pmatrix}$.

The determinant of $A^T A$ is $N \sum x_i^2 - (\sum x_i)^2$. The inverse is
$$(A^T A)^{-1} = \frac{1}{N \sum x_i^2 - (\sum x_i)^2} \begin{pmatrix} \sum x_i^2 & -\sum x_i \\ -\sum x_i & N \end{pmatrix}.$$

Multiplying $A^T A)^{-1} \cdot A^T y$:

> [!note]- Derivation
> $$\hat{\theta} = \frac{1}{N \sum x_i^2 - (\sum x_i)^2} \begin{pmatrix} \sum x_i^2 \cdot \sum y_i - \sum x_i \cdot \sum x_i y_i \\ -\sum x_i \cdot \sum y_i + N \sum x_i y_i \end{pmatrix}.$$
> The slope is the second component:
> $$\hat{\theta}_2 = \frac{N \sum x_i y_i - \sum x_i \sum y_i}{N \sum x_i^2 - (\sum x_i)^2}.$$

**Step 3: Simplify to obtain the statistical form.**

The numerator of $\hat{\theta}_2$ is $N \sum x_i y_i - (\sum x_i)(\sum y_i) = N \sum (x_i - \bar{x})(y_i - \bar{y})$ (using the de-meaning identity). The denominator is $N \sum x_i^2 - (\sum x_i)^2 = N \sum (x_i - \bar{x})^2$. Hence
$$\hat{\theta}_2 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}.$$

> [!note]- Derivation of de-meaning identity
> $$\sum (x_i - \bar{x})(y_i - \bar{y}) = \sum x_i y_i - \bar{x} \sum y_i - \bar{y} \sum x_i + N \bar{x} \bar{y} = \sum x_i y_i - 2 N \bar{x} \bar{y} + N \bar{x} \bar{y} = \sum x_i y_i - N \bar{x} \bar{y} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{N},$$
> so $N \sum (x_i - \bar{x})(y_i - \bar{y}) = N \sum x_i y_i - (\sum x_i)(\sum y_i)$. Similarly $N \sum (x_i - \bar{x})^2 = N \sum x_i^2 - (\sum x_i)^2$.

To recognize the correlation form, divide both numerator and denominator by $N \cdot \mathrm{std}(x) \cdot \mathrm{std}(y)$:

> [!note]- Derivation of correlation form
> $$\hat{\theta}_2 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y}) / (N \mathrm{std}(x) \mathrm{std}(y))}{\sum (x_i - \bar{x})^2 / (N \mathrm{std}(x) \mathrm{std}(y))} = \frac{\rho}{(\mathrm{std}(x))^2 / (\mathrm{std}(x) \mathrm{std}(y))} = \rho \frac{\mathrm{std}(y)}{\mathrm{std}(x)},$$
> where $\rho = \frac{1}{N \mathrm{std}(x) \mathrm{std}(y)} \sum (x_i - \bar{x})(y_i - \bar{y})$ is the correlation coefficient and $(\mathrm{std}(x))^2 = (1/N) \sum (x_i - \bar{x})^2$.

The intercept $\hat{\theta}_1$ follows from the first normal equation $N \hat{\theta}_1 + (\sum x_i) \hat{\theta}_2 = \sum y_i$, i.e., $\hat{\theta}_1 = \bar{y} - \hat{\theta}_2 \bar{x}$. This shows the line passes through the centroid $(\bar{x}, \bar{y})$.

> [!note]- Complete formal solution
> Let $x^d, y^d \in \mathbb{R}^N$ be the data vectors, with $\bar{x} = \mathrm{avg}(x^d), \bar{y} = \mathrm{avg}(y^d)$. The design matrix $A = [\mathbf{1} \,|\, x^d]$ has linearly independent columns iff not all $x_i$ are equal.
>
> By [[Thm - Existence and Uniqueness of Least Squares Solution]], the unique LS minimizer is $\hat{\theta} = (A^T A)^{-1} A^T y^d$. Direct computation:
> $$A^T A = \begin{pmatrix} N & N \bar{x} \\ N \bar{x} & \|x^d\|^2 \end{pmatrix}, \quad A^T y^d = \begin{pmatrix} N \bar{y} \\ (x^d)^T y^d \end{pmatrix}.$$
> The determinant $\det(A^T A) = N \|x^d\|^2 - N^2 \bar{x}^2 = N \sum (x_i - \bar{x})^2 = N^2 \mathrm{std}(x)^2$. The inverse is
> $$(A^T A)^{-1} = \frac{1}{N^2 \mathrm{std}(x)^2} \begin{pmatrix} \|x^d\|^2 & -N \bar{x} \\ -N \bar{x} & N \end{pmatrix}.$$
> Multiplying:
> $$\hat{\theta}_2 = \frac{N (x^d)^T y^d - N^2 \bar{x} \bar{y}}{N^2 \mathrm{std}(x)^2} = \frac{(x^d)^T y^d - N \bar{x} \bar{y}}{N \mathrm{std}(x)^2} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}.$$
> By the de-meaning identity, $\sum (x_i - \bar{x})(y_i - \bar{y}) = N \mathrm{std}(x) \mathrm{std}(y) \rho$. So
> $$\hat{\theta}_2 = \frac{N \mathrm{std}(x) \mathrm{std}(y) \rho}{N \mathrm{std}(x)^2} = \rho \frac{\mathrm{std}(y)}{\mathrm{std}(x)}.$$
> The intercept satisfies the first normal equation $N \hat{\theta}_1 + N \bar{x} \hat{\theta}_2 = N \bar{y}$, giving $\hat{\theta}_1 = \bar{y} - \hat{\theta}_2 \bar{x}$. Thus the fitted line $\hat{y} = \hat{\theta}_1 + \hat{\theta}_2 x$ passes through the centroid $(\bar{x}, \bar{y})$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to compute the LS solution by solving the linear system $A \theta = y$ directly using the pseudoinverse formula. While this works, the pseudoinverse is $A^\dagger = (A^T A)^{-1} A^T$ — the same calculation, just hidden. The "direct" route is exactly what we did. The illegal alternative is to *minimize the perpendicular distance* from each data point to the line (orthogonal regression), which gives a different fit (the principal-component analysis fit) — useful when the noise is symmetric in $x$ and $y$, but *not* the standard LS regression. LS regression minimizes vertical residuals only, assuming $x$ is exact and $y$ is noisy.

---

# Key Takeaways

**Slope = correlation × ratio of standard deviations.**

The simple formula $\hat{\theta}_2 = \rho \cdot \mathrm{std}(y)/\mathrm{std}(x)$ encodes a deep statistical insight. The slope of the regression line is the *correlation coefficient* times the *ratio of standard deviations*. If $y$ varies more than $x$ (large $\mathrm{std}(y)/\mathrm{std}(x)$), the slope is large; if they vary equally, the slope equals the correlation. This makes correlation a *dimensionless* version of the slope, separating the *strength* of the relationship from the *scaling*. The trigger for using this form: any "fit a line to scalar data" problem; the formula gives the slope directly without explicit matrix arithmetic.

**Line passes through the centroid.**

The intercept $\hat{\theta}_1 = \bar{y} - \hat{\theta}_2 \bar{x}$ is exactly what is needed for $(\bar{x}, \bar{y})$ to satisfy $\hat{y} = \hat{\theta}_1 + \hat{\theta}_2 \bar{x}$. This is a general fact for least squares with an intercept: the fitted regression always passes through the centroid of the data. The reason: the gradient of the LS objective with respect to the intercept is $\sum (y_i - \theta_1 - \theta_2 x_i) = 0$ at the minimum, i.e., the *average residual is zero* — and average residual zero for a model with constant term means the model passes through the centroid. This generalizes to multivariate regression: the fitted hyperplane passes through the centroid of the design points.

**The de-meaning identity converts sums to centered sums.**

The trick $\sum x_i y_i - N \bar{x} \bar{y} = \sum (x_i - \bar{x})(y_i - \bar{y})$ — and its squared-norm version — is the algebraic engine of all univariate regression formulas. The "centered" sums are the *covariance* and *variance*, which have direct probabilistic interpretation. The "raw" sums obscure this. The pattern transfers: whenever a LS calculation involves the all-ones column $\mathbf{1}$, expect the de-meaning identity to clean up the result.

This exercise is the foundation for understanding the asset $\alpha$ and $\beta$ formulas in finance (Boyd §13.1.1), where the regression slope of asset returns on market returns is exactly the $\beta$ parameter, and the intercept is related to the asset's $\alpha$ (excess return over the risk-free rate). It also generalizes to multivariate regression with multiple features (see [[Def - Least Squares Data Fitting]]), where the formula becomes $\hat{\theta} = (X^T X)^{-1} X^T y$ — the same content with $X$ replacing $A$ and the de-meaning trick generalizing to a *centered* design matrix.
