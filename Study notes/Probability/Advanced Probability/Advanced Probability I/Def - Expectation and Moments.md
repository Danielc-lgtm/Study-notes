---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Random Variable"
  - "Def - The Integral"
  - "Def - Lp Spaces"
tags: [probability, advanced-probability]
---

# Notation

$X$ a [[Def - Random Variable|random variable]] on $(\Omega,\mathcal{F},\mathbb{P})$, $\mu_X$ its law. $\mathbb{E}[X]$ — expectation; $\mathrm{Var}(X)$ — variance; $\mathbb{E}[X^k]$ — the $k$-th moment.

---

# Axiom Motivation

A [[Def - Random Variable|random variable]] $X$ carries a whole distribution of values; often one wants a *single number* summarising it — its "average." The **expectation** is that number, and there is no choice in how to define it: it must be the [[Def - The Integral|integral]] of $X$ against $\mathbb{P}$. The expectation of an [[Def - Simple Function|indicator]] must be the probability of the event; the expectation must be linear and monotone; the integral against $\mathbb{P}$ is the *unique* functional with these properties. So $\mathbb{E}[X]=\int_\Omega X\,d\mathbb{P}$ — expectation is integration, renamed.

Expectation alone does not capture *spread*. The **variance** $\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}X)^2]$ measures mean-square deviation from the mean — the $L^2$-distance from $X$ to its best constant approximation. Higher **moments** $\mathbb{E}[X^k]$ encode finer shape (skewness, tails). Whether a moment *exists* is a genuine integrability question: $\mathbb{E}[|X|^k]<\infty$ means $X\in L^k(\mathbb{P})$, and since $\mathbb{P}$ is a *finite* measure, the [[Def - Lp Spaces|$L^p$-inclusions]] run $L^q\subseteq L^p$ for $q\ge p$ — *higher* moments control *lower* ones. A variable can have a mean but no variance (heavy tails); the existence of moments is a tail condition.

The decisive computational fact: expectation depends only on the **law**. By the change-of-variables / pushforward identity, $\mathbb{E}[h(X)]=\int h\,d\mu_X$ — one integrates against the law on $\mathbb{R}$, never needing the abstract $\Omega$. This is why expectation, variance, and moments are computed from the density or the distribution function alone.

---

# The Definition

Let $X$ be a random variable on $(\Omega,\mathcal{F},\mathbb{P})$.

The **expectation** (mean) of $X$ is $\mathbb{E}[X]=\int_\Omega X\,d\mathbb{P}$, defined when $X\in L^1(\mathbb{P})$, i.e. $\mathbb{E}[|X|]<\infty$ (and for $X\ge0$ always, possibly $+\infty$).

The **$k$-th moment** is $\mathbb{E}[X^k]$, defined when $X\in L^k(\mathbb{P})$; the **variance** is
$$\mathrm{Var}(X)=\mathbb{E}\big[(X-\mathbb{E}X)^2\big]=\mathbb{E}[X^2]-(\mathbb{E}X)^2\ \ge0,$$
defined when $X\in L^2(\mathbb{P})$; the **standard deviation** is $\sigma(X)=\sqrt{\mathrm{Var}(X)}$. The **covariance** of $X,Y\in L^2$ is $\mathrm{Cov}(X,Y)=\mathbb{E}[(X-\mathbb{E}X)(Y-\mathbb{E}Y)]$.

**Change of variables / law formula.** For Borel $h\ge0$ (or $h(X)\in L^1$),
$$\mathbb{E}[h(X)]=\int_\Omega h(X)\,d\mathbb{P}=\int_\mathbb{R}h(x)\,d\mu_X(x),$$
so $\mathbb{E}[X^k]=\int x^k\,d\mu_X$ — moments depend only on the law.

---

# Relate to Other Fields / Compression

Expectation is the [[Def - The Integral|Lebesgue integral]] against $\mathbb{P}$ — nothing more — so all of integration theory (linearity, monotonicity, [[Thm - Monotone Convergence Theorem|MCT]], [[Thm - Dominated Convergence Theorem|DCT]], [[Thm - Fatou's Lemma|Fatou]]) transfers verbatim. The space of variables with finite $k$-th moment is the [[Def - Lp Spaces|$L^k(\mathbb{P})$]] space; variance is the squared $L^2$-norm of the *centred* variable, and $\mathrm{Cov}$ is the $L^2$ inner product of centred variables — so [[Ex - The Cauchy-Schwarz inequality and L2 geometry|covariance is an inner product]] and the correlation coefficient is a cosine. The change-of-variables formula is the pushforward identity $\int h\,d(X_*\mathbb{P})=\int h\circ X\,d\mathbb{P}$.

---

# Examples / Corollaries

For the [[Ex - Computing an expectation by monotone convergence|geometric law]] $\mathbb{P}(X=k)=(1-p)^{k-1}p$, $\mathbb{E}[X]=1/p$. For the standard Gaussian, $\mathbb{E}[X]=0$, $\mathrm{Var}(X)=1$. **Linearity** $\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y$ holds with *no independence assumption* — a fact that trivialises many counting computations via indicator decomposition. **Variance** is *not* linear: $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\mathrm{Cov}(X,Y)$, additive only for uncorrelated variables.

A variable can have $\mathbb{E}[|X|]<\infty$ but $\mathbb{E}[X^2]=\infty$ (Cauchy-like heavy tails) — moments form a *decreasing* scale of integrability hypotheses.

Calibration: (i) Is $\mathbb{E}$ linear? Yes, always. Is $\mathrm{Var}$? No. (ii) Does $\mathrm{Var}(X)=0$ imply $X$ constant? Yes — a.s. constant. (iii) Does $\mathbb{E}[X]$ depend on $\Omega$? No — only on $\mu_X$.

---

# Unlocked by This

> [!tip] The probabilistic inequalities
> [[Ex - Markov's inequality|Markov]] and Chebyshev bound tail probabilities by moments; [[Thm - Jensen's Inequality|Jensen]] relates $\mathbb{E}[\varphi(X)]$ and $\varphi(\mathbb{E}X)$ for convex $\varphi$; Cauchy–Schwarz bounds covariance.

> [!tip] Laws of large numbers and the CLT
> The [[Thm - Strong Law of Large Numbers|law of large numbers]] says sample means converge to $\mathbb{E}[X]$; the [[Thm - Central Limit Theorem|central limit theorem]] describes the Gaussian fluctuations, scaled by $\sqrt{\mathrm{Var}(X)}$.
