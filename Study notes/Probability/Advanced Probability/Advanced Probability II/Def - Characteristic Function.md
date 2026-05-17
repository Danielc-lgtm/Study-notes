---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Random Variable"
  - "Def - Expectation and Moments"
tags: [probability, advanced-probability]
---

# Notation

$X$ an $\mathbb{R}^d$-valued [[Def - Random Variable|random variable]], law $\mu_X$; $\varphi_X$ its characteristic function; $\langle\cdot,\cdot\rangle$ the Euclidean inner product.

---

# Axiom Motivation

A [[Def - Random Variable|law]] $\mu_X$ is a measure — awkward to manipulate directly, especially under *addition* of independent variables, where the law of a sum is a [[Ex - Independence and the factorisation of expectation|convolution]] $\mu_X*\mu_Y$. The **characteristic function** is the Fourier transform of the law, and it converts the intractable convolution into a simple *product*: $\varphi_{X+Y}=\varphi_X\varphi_Y$ for independent $X,Y$. This single fact is why characteristic functions exist — they linearise the addition of independent variables, turning the study of $S_n=\sum_{k=1}^n X_k$ into the study of $\varphi_X^n$.

Three properties make $\varphi_X$ the perfect tool. (i) It is **defined for every law** — $|e^{i\langle t,X\rangle}|=1$, so the expectation always exists (unlike the moment generating function). (ii) It **determines the law** — $\varphi_X=\varphi_Y\Rightarrow\mu_X=\mu_Y$ (Fourier inversion). (iii) It **encodes moments** as derivatives at $0$ — $\varphi_X^{(k)}(0)=i^k\mathbb{E}[X^k]$ — and convergence of $\varphi_{X_n}$ to $\varphi_X$ *pointwise* is equivalent to [[Def - Weak Convergence|weak convergence]] of the laws ([[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]]).

Together these make the characteristic function the engine of the [[Thm - Central Limit Theorem|central limit theorem]]: write $S_n/\sqrt n$, factor its characteristic function as a product, Taylor-expand each factor using the moment property, and watch $\varphi_X(t/\sqrt n)^n\to e^{-t^2/2}$ — the Gaussian's characteristic function. The Gaussian is *self-dual* (its own Fourier transform up to scaling), which is why it is the universal limit.

---

# The Definition

The **characteristic function** of an $\mathbb{R}^d$-valued random variable $X$ (with law $\mu_X$) is $\varphi_X:\mathbb{R}^d\to\mathbb{C}$,
$$\varphi_X(t)=\mathbb{E}\big[e^{i\langle t,X\rangle}\big]=\int_{\mathbb{R}^d}e^{i\langle t,x\rangle}\,d\mu_X(x).$$

It satisfies: $\varphi_X(0)=1$; $|\varphi_X(t)|\le1$; $\varphi_X$ is **uniformly continuous**; $\varphi_X(-t)=\overline{\varphi_X(t)}$; and it is **positive definite**.

**Key properties.** (i) **Determination:** $\varphi_X=\varphi_Y\implies\mu_X=\mu_Y$. (ii) **Convolution $\to$ product:** if $X,Y$ are [[Def - Independence|independent]], $\varphi_{X+Y}=\varphi_X\,\varphi_Y$. (iii) **Affine maps:** $\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$. (iv) **Moments:** if $\mathbb{E}|X|^k<\infty$, then $\varphi_X\in C^k$ and $\varphi_X^{(k)}(0)=i^k\mathbb{E}[X^k]$.

For the standard Gaussian $N(0,1)$, $\varphi(t)=e^{-t^2/2}$ — the Gaussian is its own characteristic function up to scaling (**self-dual**).

---

# Relate to Other Fields / Compression

The characteristic function is the **Fourier transform of the law** — exactly the Fourier transform of analysis, applied to a probability measure. Property (ii) is the Fourier-analytic fact "$\widehat{f*g}=\hat f\hat g$": Fourier diagonalises convolution. Property (iv), moments-as-derivatives, is the Fourier "smoothness $\leftrightarrow$ decay" duality. The *self-duality of the Gaussian* is the analytic heart of the [[Thm - Central Limit Theorem|CLT]] and of the heat equation. The moment generating function $\mathbb{E}[e^{tX}]$ is the real-exponential analogue — better for [[Thm - Cramér's Theorem|large deviations]] but not always finite.

---

# Examples / Corollaries

$N(m,\sigma^2)$: $\varphi(t)=e^{imt-\sigma^2t^2/2}$. Bernoulli($p$): $\varphi(t)=1-p+pe^{it}$. Poisson($\lambda$): $\varphi(t)=e^{\lambda(e^{it}-1)}$. Exponential($\lambda$): $\varphi(t)=\lambda/(\lambda-it)$.

The convolution property *recovers* "sum of independent Gaussians is Gaussian" instantly: multiply the exponentials. The moment property reads $\mathbb{E}X$ and $\mathrm{Var}(X)$ off $\varphi'(0),\varphi''(0)$.

Calibration: (i) Does $\varphi_X$ always exist? Yes — $|e^{itX}|=1$. (ii) Does $\varphi_X$ determine $\mathbb{E}X$? Only if $\mathbb{E}|X|<\infty$, via $\varphi'(0)=i\mathbb{E}X$. (iii) Is $|\varphi_X|=1$ possible for non-constant $X$? On a lattice, partially — but $|\varphi_X(t)|<1$ for $t\neq0$ small unless $X$ is degenerate.

---

# Unlocked by This

> [!tip] Lévy's continuity theorem and the CLT
> [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]] makes pointwise convergence of $\varphi_{X_n}$ equivalent to [[Def - Weak Convergence|weak convergence]]; combined with the convolution-to-product and moment properties, it proves the [[Thm - Central Limit Theorem|central limit theorem]].
