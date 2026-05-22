---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Norm and Distance"
tags: [algebra, linear-algebra, applied, statistics]
---

# Notation

Throughout, $x, y, a, b$ are real $n$-vectors. The all-ones vector is $\mathbf 1$, the average is $\operatorname{avg}(x) = \mathbf 1^T x / n$, and the RMS is $\operatorname{rms}(x) = \|x\|/\sqrt n$. The **de-meaned vector** is $\tilde x = x - \operatorname{avg}(x) \mathbf 1$; it has $\operatorname{avg}(\tilde x) = 0$. The traditional Greek-letter conventions $\mu = \operatorname{avg}(x)$ and $\sigma = \operatorname{std}(x)$ are used in the statistics-of-returns context.

This is a compound page: it defines four interlocking notions — the **de-meaned vector**, the **standard deviation**, the **standardized vector** (or **$z$-score**), and the **correlation coefficient** — because they form the basic statistical-summary toolkit and each is defined in terms of the previous.

---

# Axiom Motivation

The desideratum is to measure how much the entries of a vector $x$ *differ from each other*, separating two effects: the overall "level" of the vector (its average), and the "variation" around that level. The norm $\|x\|$ confuses these: a constant vector $\alpha \mathbf 1$ has norm $|\alpha|\sqrt n$, even though its entries all agree. The RMS value $\operatorname{rms}(x) = \|x\|/\sqrt n$ is closer — it equals $|\alpha|$ for a constant vector — but it still treats the constant vector as having "size $|\alpha|$", which is the *level*, not the *variation*. To isolate variation we must first subtract the mean.

The **de-meaned vector** $\tilde x = x - \operatorname{avg}(x)\mathbf 1$ does exactly this: it subtracts the average from every entry, leaving a vector with zero average. The original $x$ decomposes as
$$x = \underbrace{\operatorname{avg}(x)\mathbf 1}_{\text{level}} + \underbrace{\tilde x}_{\text{variation}},$$
and these two parts are orthogonal: $\mathbf 1^T \tilde x = \mathbf 1^T x - \operatorname{avg}(x) \mathbf 1^T \mathbf 1 = n \operatorname{avg}(x) - n \operatorname{avg}(x) = 0$. By the Pythagorean theorem,
$$\|x\|^2 = \|\operatorname{avg}(x)\mathbf 1\|^2 + \|\tilde x\|^2 = n \operatorname{avg}(x)^2 + \|\tilde x\|^2.$$
Dividing by $n$ gives the **variance decomposition** $\operatorname{rms}(x)^2 = \operatorname{avg}(x)^2 + \operatorname{std}(x)^2$, where $\operatorname{std}(x) = \|\tilde x\|/\sqrt n$ is the standard deviation. So:
- $\operatorname{avg}(x)$ = the level.
- $\operatorname{std}(x)$ = the RMS of the de-meaned vector = the typical deviation from the level.
- $\operatorname{rms}(x)^2 = \operatorname{avg}(x)^2 + \operatorname{std}(x)^2$ — the Pythagorean separation of these two effects.

This is the same algebra as $\mathbb E[X^2] = (\mathbb E X)^2 + \operatorname{Var}(X)$ in probability, with the inner product $\mathbf 1^T \cdot / n$ playing the role of the expectation.

**Why divide by $\sqrt n$ rather than $\sqrt{n-1}$?** Boyd's convention divides by $\sqrt n$, which makes the standard deviation a *deterministic average* of squared deviations. The alternative $\sqrt{n-1}$ convention (Bessel's correction) is used in statistics when $x$ is regarded as a *sample* from a distribution and we want an unbiased estimate of the population variance. For deterministic algorithms — where $x$ is a fixed vector, not a sample — Boyd's $\sqrt n$ convention is cleaner and the choice does not affect the structural identities.

The **standardized vector** $z = (x - \operatorname{avg}(x)\mathbf 1) / \operatorname{std}(x)$ removes both the level and the scale: it has mean zero and standard deviation one, putting different vectors on a common footing. The entries of $z$ are called **$z$-scores**, with $z_i$ measuring "how many standard deviations above the mean is $x_i$".

The **correlation coefficient** answers the question: how much do two vectors $a$ and $b$ vary together? The de-meaned versions $\tilde a, \tilde b$ are the variations, and the natural similarity measure is the angle between them via the inner product. The **correlation coefficient** is
$$\rho(a, b) = \frac{\tilde a^T \tilde b}{\|\tilde a\| \|\tilde b\|} = \cos \angle(\tilde a, \tilde b).$$
By Cauchy–Schwarz, $-1 \leq \rho \leq 1$. The extreme cases are interpretable: $\rho = 1$ means $\tilde a$ and $\tilde b$ are positively aligned (each is a positive scalar multiple of the other) — when one is above its mean, so is the other; $\rho = -1$ means they are anti-aligned — when one is above its mean, the other is below; $\rho = 0$ means orthogonality — no linear relationship.

What if we had defined correlation using the un-de-meaned inner product $a^T b / (\|a\|\|b\|) = \cos \angle(a, b)$? This is the cosine *similarity* used in information retrieval, and it is different: two vectors of all-positive entries can have cosine similarity near $1$ even if they vary together very weakly. The de-meaning is what makes correlation track *covariation* rather than mere alignment of the raw vectors. Both quantities are useful; the correlation coefficient is the right one for statistical interpretation.

What if we had defined standard deviation as the absolute average deviation $\sum_i |x_i - \operatorname{avg}(x)|/n$? This is the **mean absolute deviation**, and it is sometimes used (especially in robust statistics) but it lacks the rich Euclidean-geometry-and-Pythagorean-theorem structure of the standard deviation. The standard deviation is the *Euclidean* measure of variation, and it interacts cleanly with sums of vectors via the formula $\operatorname{std}(a + b)^2 = \operatorname{std}(a)^2 + 2\rho \operatorname{std}(a)\operatorname{std}(b) + \operatorname{std}(b)^2$, which is what makes correlation operational in portfolio theory.

---

# The Definition

**De-meaned vector.** For $x \in \mathbb R^n$, the **de-meaned vector** is
$$\tilde x = x - \operatorname{avg}(x) \mathbf 1.$$
It satisfies $\operatorname{avg}(\tilde x) = 0$.

**Standard deviation.** For $x \in \mathbb R^n$, the **standard deviation** is
$$\operatorname{std}(x) = \frac{\|x - \operatorname{avg}(x)\mathbf 1\|}{\sqrt n} = \operatorname{rms}(\tilde x).$$
It satisfies $\operatorname{std}(x) \geq 0$, with equality if and only if all entries of $x$ are equal. In the Greek-letter convention $\sigma = \operatorname{std}(x)$ and $\mu = \operatorname{avg}(x)$.

**Variance decomposition.** For any $x \in \mathbb R^n$,
$$\operatorname{rms}(x)^2 = \operatorname{avg}(x)^2 + \operatorname{std}(x)^2.$$

**Standardized vector.** For $x$ with $\operatorname{std}(x) > 0$, the **standardized vector** (or **$z$-score** vector) is
$$z = \frac{1}{\operatorname{std}(x)}\big(x - \operatorname{avg}(x)\mathbf 1\big).$$
It satisfies $\operatorname{avg}(z) = 0$ and $\operatorname{std}(z) = 1$.

**Correlation coefficient.** For two vectors $a, b \in \mathbb R^n$ both with $\operatorname{std} > 0$, the **correlation coefficient** is
$$\rho(a, b) = \frac{\tilde a^T \tilde b}{\|\tilde a\|\|\tilde b\|} = \frac{1}{n} u^T v,$$
where $u, v$ are the standardized versions of $a, b$. Equivalently $\rho = \cos\angle(\tilde a, \tilde b)$. The correlation coefficient always satisfies $-1 \leq \rho \leq 1$ (Cauchy–Schwarz), and the convention sets $\rho = 0$ when either of $a, b$ is constant.

**Standard deviation of a sum.** For $a, b \in \mathbb R^n$,
$$\operatorname{std}(a + b)^2 = \operatorname{std}(a)^2 + 2 \rho(a, b)\operatorname{std}(a)\operatorname{std}(b) + \operatorname{std}(b)^2.$$

---

# Relate to Other Fields / Compression

The standard deviation and correlation coefficient are the discrete deterministic analogues of probabilistic variance and correlation. If we regard $x$ as the values of a random variable $X$ taking each of its values with probability $1/n$, then $\operatorname{avg}(x) = \mathbb E[X]$, $\operatorname{std}(x)^2 = \operatorname{Var}(X)$, and $\rho(a, b)$ is exactly the Pearson correlation coefficient of $A, B$ regarded as random variables on the uniform probability space. The variance decomposition $\operatorname{rms}^2 = \operatorname{avg}^2 + \operatorname{std}^2$ is the deterministic version of $\mathbb E[X^2] = (\mathbb E X)^2 + \operatorname{Var}(X)$.

In portfolio theory, $\operatorname{avg}(x)$ is the average **return** of an investment over time, $\operatorname{std}(x)$ is the **risk**, and $\rho(a, b)$ measures how much two investments move together. The standard-deviation-of-sum formula then encodes the central insight of diversification: combining two assets with $\rho < 1$ produces a portfolio with lower risk than either alone, because the negative correlation cancels some of the variation.

In statistics, the *autocorrelation* of a time series is $\rho(x, \operatorname{shift}_\tau(x))$ where $\operatorname{shift}_\tau$ is a circular or zero-padded shift; this is the standard tool for detecting periodicity in a signal. In signal processing, the standardised inner product $u^T v / n$ recovers the angle between de-meaned signals, the basis of matched filtering.

**True name:** The standard deviation $\operatorname{std}(x)$ is *the typical amount by which an entry of $x$ deviates from the mean*. The correlation coefficient $\rho(a, b)$ is *the cosine of the angle between the de-meaned versions of $a$ and $b$* — equivalently, a normalized covariance.

---

# Examples / Corollaries

**Is an instance — small dataset.** For $x = (1, -2, 3, 2)$, $\operatorname{avg}(x) = (1 - 2 + 3 + 2)/4 = 1$, so $\tilde x = (0, -3, 2, 1)$, $\|\tilde x\|^2 = 0 + 9 + 4 + 1 = 14$, and $\operatorname{std}(x) = \sqrt{14/4} \approx 1.871$. The entries $\tilde x = (0, -3, 2, 1)$ are themselves deviations of magnitudes $0, 3, 2, 1$ from the mean $1$, so $1.871$ as the "typical deviation" is plausible.

**Is an instance — return series and risk.** If $r$ is a $T$-vector of asset returns over $T$ periods, $\operatorname{avg}(r)$ is the average return and $\operatorname{std}(r)$ is the risk. Annualised values multiply by $\sqrt T$ if the periods are sub-annual, by the standard scaling of standard deviations under independent additive aggregation. A "Sharpe ratio" is $(\operatorname{avg}(r) - r_f)/\operatorname{std}(r)$, comparing excess return per unit of risk.

**Is an instance — perfectly correlated vectors.** For $a = (1, 2, 3, 4, 5)$ and $b = (2, 4, 6, 8, 10) = 2a$, we have $\tilde b = 2 \tilde a$, so $\rho(a, b) = (2 \tilde a^T \tilde a)/(2 \|\tilde a\|^2) = 1$. Any positive scalar multiple gives correlation exactly $+1$. For $b = -2a$, we get $\rho = -1$.

**Is NOT an instance — uncorrelated but dependent.** For $a = (-2, -1, 0, 1, 2)$ and $b = (4, 1, 0, 1, 4) = a^2$ entrywise, $\operatorname{avg}(a) = 0$, $\operatorname{avg}(b) = 2$, $\tilde a = a$, $\tilde b = (2, -1, -2, -1, 2)$, $\tilde a^T \tilde b = -4 + 1 + 0 -1 + 4 = 0$, so $\rho(a, b) = 0$. The vectors are uncorrelated even though $b$ is a *deterministic function* of $a$ (namely, $b_i = a_i^2$). This is the deterministic counterpart of "uncorrelated does not mean independent" in probability.

**Is NOT an instance — constant vector.** If $x = \alpha \mathbf 1$, then $\tilde x = 0$ and $\operatorname{std}(x) = 0$. The correlation coefficient with any other vector is undefined (division by zero), and by convention is set to $0$. The constant vector is the unique vector with zero standard deviation.

**Corollary — scaling and shifting.** $\operatorname{std}(\alpha x + \beta \mathbf 1) = |\alpha|\operatorname{std}(x)$: adding a constant does not change the standard deviation, but multiplying by a scalar scales it by the absolute value. Similarly, $\rho(\alpha a + \beta \mathbf 1, \gamma b + \delta \mathbf 1) = \operatorname{sgn}(\alpha \gamma)\rho(a, b)$ for $\alpha, \gamma \neq 0$: the correlation is invariant to affine reparameterisation, except for a sign flip if exactly one of $\alpha, \gamma$ is negative.

**Corollary — hedging via negative correlation.** If $\operatorname{std}(a) = \operatorname{std}(b) = \sigma$, then $\operatorname{std}((a+b)/2) = \sigma\sqrt{(1 + \rho)/2}$. When $\rho = 1$ this is $\sigma$ (no diversification); when $\rho = 0$ this is $\sigma/\sqrt 2$; when $\rho = -1$ this is $0$ (perfect hedge). This is the algebraic basis of portfolio diversification: averaging negatively-correlated assets reduces risk.

**Corollary — Chebyshev for standard deviation.** The fraction of entries of $x$ with $|x_i - \operatorname{avg}(x)| \geq c$ is at most $(\operatorname{std}(x)/c)^2$. So at most $1/9 \approx 11\%$ of entries can be three standard deviations from the mean. This is the deterministic version of Chebyshev's inequality in probability.

**Calibration check.** Verify that for $x = (1, 1, 1, 1)$, $\operatorname{std}(x) = 0$ (constant vector). Verify that the de-meaned vector $\tilde x$ is orthogonal to $\mathbf 1$, i.e., $\mathbf 1^T \tilde x = 0$, by direct computation. Verify the variance decomposition for $x = (3, 4)$: $\operatorname{avg}(x) = 3.5$, $\operatorname{rms}(x)^2 = (9 + 16)/2 = 12.5$, $\operatorname{std}(x)^2 = (0.25 + 0.25)/2 = 0.25$, and $3.5^2 + 0.25 = 12.5$ ✓.

---

# Unlocked by This

> [!tip] Sample Covariance and Principal Component Analysis *(from Statistics)*
> For a dataset $X \in \mathbb R^{n \times N}$ (each column a data point), the **sample covariance matrix** $\Sigma = (1/N)\tilde X \tilde X^T$ (where $\tilde X$ has its columns de-meaned) has entries $\Sigma_{ij} = \rho(X^i, X^j)\operatorname{std}(X^i)\operatorname{std}(X^j)$, where $X^i$ is the $i$-th feature row. The eigendecomposition of $\Sigma$ is **Principal Component Analysis**: the eigenvectors are the directions of maximal variance, and the eigenvalues are the variances along those directions.

> [!tip] Time Series Analysis: Autocorrelation and Spectra *(from Probability)*
> The **autocorrelation function** $R(\tau) = \rho(x_t, x_{t+\tau})$ of a time series $x$ measures how the series at time $t$ relates to itself at time $t + \tau$. The Fourier transform of $R(\tau)$ is the **power spectral density**, which gives the energy in the signal at each frequency. The Wiener-Khinchin theorem makes the connection precise: autocorrelation and spectrum are Fourier-dual.

> [!tip] Information-Theoretic Independence *(from Information Theory)*
> Zero correlation does not imply independence (the $a, b = a^2$ example above), but for jointly Gaussian random variables it does. The information-theoretic generalisation is **mutual information** $I(A; B)$, which equals zero if and only if $A$ and $B$ are independent. For Gaussian data $I(A; B) = -(1/2)\log(1 - \rho^2)$, recovering the correlation coefficient.
