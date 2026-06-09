---
type: theorem
subject: advanced-probability
prereqs:
  - "Thm - Lévy's Continuity Theorem"
  - "Def - Characteristic Function"
  - "Def - Weak Convergence"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ i.i.d. with $\mathbb{E}[X_1]=\mu$, $\mathrm{Var}(X_1)=\sigma^2\in(0,\infty)$; $S_n=X_1+\cdots+X_n$; $N(0,1)$ the standard Gaussian, characteristic function $e^{-t^2/2}$.

---

# Motivation

The [[Thm - Strong Law of Large Numbers|law of large numbers]] says $S_n/n\to\mu$ — the average has *no fluctuation* in the limit. The central limit theorem describes the fluctuation that the law of large numbers discards: $S_n-n\mu$ is of order $\sqrt n$, and once rescaled by $\sqrt n$ it converges to a **Gaussian** — *regardless of the distribution of $X_1$*. This universality is the most important fact in probability and statistics: it is why the bell curve is everywhere, why measurement errors are Gaussian, why confidence intervals have their form. The CLT says the Gaussian is the universal *attractor* for normalised sums of independent pieces, each individually negligible.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "i.i.d. with finite non-zero variance," but the CLT is the universal attractor for normalised sums of small, roughly independent pieces. Recognising a problem as *secretly* such a sum is what makes the theorem deployable far outside its textbook statement.

The first source is **sums of independent but not identically distributed variables satisfying the Lindeberg condition**. Real applications routinely aggregate heterogeneous contributions — measurement errors of different magnitudes, returns of a portfolio of different assets, contributions of distinct neurons to a firing rate. Here the summands $X_{n,k}$ form a triangular array of independent but non-identical pieces. The bridge: with $s_n^2=\sum_k\mathrm{Var}(X_{n,k})$, the **Lindeberg–Feller CLT** says that if $\frac{1}{s_n^2}\sum_k\mathbb{E}[X_{n,k}^2\mathbf{1}_{|X_{n,k}|>\varepsilon s_n}]\to0$ (no single summand dominates the variance), then $\frac{1}{s_n}\sum_k(X_{n,k}-\mathbb{E}X_{n,k})\xrightarrow{d}N(0,1)$. The example: aggregate returns $R_k=\sigma_k Z_k$ of uncorrelated assets with different volatilities $\sigma_k$ — if no $\sigma_k^2$ dominates $\sum_k\sigma_k^2$, the rescaled total return is asymptotically Gaussian even though no two assets share a distribution.

The second source is **martingale difference sequences with bounded second moments**. Pure independence is often absent — the increments of a learning algorithm, the score function evaluated along a Markov chain, the residuals of a regression — yet these are uncorrelated and have zero conditional mean given the past, i.e. they form a [[Def - Martingale|martingale difference sequence]]. The bridge: the **martingale CLT** says that if $D_k=M_k-M_{k-1}$ are martingale differences with $\frac1n\sum_k\mathbb{E}[D_k^2\mid\mathcal{F}_{k-1}]\xrightarrow{\mathbb{P}}\sigma^2$ and a conditional Lindeberg condition holds, then $M_n/\sqrt n\xrightarrow{d}N(0,\sigma^2)$. The example: the cumulative log-likelihood ratio in a sequential test is a martingale under the null; once recognised, asymptotic normality of the test statistic follows without independence of the observations.

The third source is **U-statistics and other smooth functionals of i.i.d. samples**. The sample variance, the Wilcoxon rank statistic, the Gini coefficient, a kernel density estimator at a fixed point — none is literally a sum of i.i.d. summands. The bridge is **Hoeffding's decomposition**: any U-statistic $U_n=\binom{n}{m}^{-1}\sum_{i_1<\cdots<i_m}h(X_{i_1},\dots,X_{i_m})$ projects onto its leading linear part $\frac{m}{n}\sum_i h_1(X_i)$ with $h_1(x)=\mathbb{E}[h(x,X_2,\dots,X_m)]-\theta$, the remainder being negligible at the $1/\sqrt n$ scale. The example: the sample variance $s_n^2=\frac1{n-1}\sum_i(X_i-\bar X_n)^2$ is the U-statistic for $h(x,y)=\tfrac12(x-y)^2$; its linearised part is a sum of i.i.d. $(X_i-\mu)^2-\sigma^2$, and the ordinary CLT delivers $\sqrt n(s_n^2-\sigma^2)\xrightarrow{d}N(0,\mathrm{Var}((X_1-\mu)^2))$.

**Targets (Output Amplification)**

The conclusion $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$ is the asymptotic distribution of one sample mean. Each amplification turns this into a far stronger statement by composing with a separate principle.

The first amplification is **CLT combined with the delta method**: if $g$ is differentiable at $\mu$ with $g'(\mu)\ne0$, then $\sqrt n(g(\bar X_n)-g(\mu))\xrightarrow{d}N(0,g'(\mu)^2\sigma^2)$. The non-obvious upshot is that every smooth statistic of a sample mean is asymptotically Gaussian, with explicit variance — this is the workhorse of inferential statistics, since most estimators of interest are nonlinear functions of empirical averages. The example: the log-odds estimator $\log(\hat p/(1-\hat p))$ from a sample proportion $\hat p$ is asymptotically Gaussian with variance $1/(np(1-p))$, computed in one line via $g(p)=\log(p/(1-p))$ and $g'(p)=1/(p(1-p))$ — the foundation of logistic regression standard errors.

The second amplification is **CLT combined with [[Thm - Slutsky's Theorem|Slutsky's theorem]]**: if $T_n\xrightarrow{d}T$ and $V_n\xrightarrow{\mathbb{P}}c$, then $T_n/V_n\xrightarrow{d}T/c$. The non-obvious upshot is that estimated nuisance parameters do not break asymptotic normality: in $\sqrt n(\bar X_n-\mu)/\hat\sigma_n$, the denominator $\hat\sigma_n$ is the sample standard deviation, yet Slutsky replaces it by $\sigma$ in the limit because $\hat\sigma_n\xrightarrow{\mathbb{P}}\sigma$ (by [[Thm - Strong Law of Large Numbers|SLLN]]). The example: the Student $t$-statistic is asymptotically $N(0,1)$ even with the variance estimated from the sample — this is why $z$-intervals continue to work when one plugs in $\hat\sigma_n$ for the unknown $\sigma$.

The third amplification is **CLT combined with the [[Def - Characteristic Function|Cramér–Wold device]]**: a sequence of random vectors $Y_n\in\mathbb{R}^d$ converges in distribution to $Y$ iff $\langle t,Y_n\rangle\xrightarrow{d}\langle t,Y\rangle$ for every $t\in\mathbb{R}^d$. The non-obvious upshot is the **multivariate CLT** for free: $\sqrt n(\bar{\mathbf X}_n-\boldsymbol\mu)\xrightarrow{d}N(0,\Sigma)$ with $\Sigma$ the covariance matrix of $\mathbf X_1$, since each linear combination $\langle t,\sqrt n(\bar{\mathbf X}_n-\boldsymbol\mu)\rangle$ is a one-dimensional sum to which the scalar CLT applies. The example: joint asymptotic normality of $(\bar X_n,s_n^2)$ — needed for the limit laws of $t$-statistics, regression coefficients, and likelihood-ratio statistics — drops out of Cramér–Wold plus the scalar CLT on each linear combination, with no separate multivariate machinery.

---

# Statement

Let $(X_n)_{n\ge1}$ be **independent and identically distributed** with $\mathbb{E}[X_1]=\mu$ and $0<\sigma^2=\mathrm{Var}(X_1)<\infty$. Then
$$\frac{S_n-n\mu}{\sigma\sqrt n}\ \xrightarrow{\ d\ }\ N(0,1)\qquad\text{as }n\to\infty,$$
i.e. for every $a\in\mathbb{R}$, $\ \mathbb{P}\big(\tfrac{S_n-n\mu}{\sigma\sqrt n}\le a\big)\to\Phi(a)=\int_{-\infty}^a\frac{e^{-x^2/2}}{\sqrt{2\pi}}\,dx$.

---

# Why Is It True

The proof is a *characteristic-function computation*, made legitimate by [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]]: it suffices to show the characteristic function of the normalised sum converges, pointwise, to $e^{-t^2/2}$ — the Gaussian's.

Centre and rescale: assume $\mu=0$, $\sigma^2=1$ (replace $X_k$ by $(X_k-\mu)/\sigma$), and set $Z_n=S_n/\sqrt n$. The two structural facts:

*Independence linearises the sum.* Because the $X_k$ are independent, the [[Def - Characteristic Function|characteristic function of a sum is a product]]:
$$\varphi_{Z_n}(t)=\mathbb{E}\big[e^{it S_n/\sqrt n}\big]=\prod_{k=1}^n\mathbb{E}\big[e^{i(t/\sqrt n)X_k}\big]=\varphi_X\!\left(\frac{t}{\sqrt n}\right)^{\!n}.$$
The whole problem is now to understand one characteristic function, $\varphi_X$, near $0$, raised to a high power.

*Finite variance gives a Taylor expansion.* Since $\mathbb{E}X=0$, $\mathbb{E}X^2=1$, the [[Def - Characteristic Function|moment property]] ($\varphi_X^{(k)}(0)=i^k\mathbb{E}X^k$) gives the second-order expansion
$$\varphi_X(s)=1+is\,\mathbb{E}X-\tfrac{s^2}{2}\mathbb{E}X^2+o(s^2)=1-\tfrac{s^2}{2}+o(s^2)\quad(s\to0).$$
Substitute $s=t/\sqrt n$ — which $\to0$ as $n\to\infty$:
$$\varphi_{Z_n}(t)=\left(1-\frac{t^2}{2n}+o\!\left(\frac1n\right)\right)^{\!n}\ \xrightarrow[n\to\infty]{}\ e^{-t^2/2},$$
by the standard limit $(1+c/n+o(1/n))^n\to e^c$. The limit $e^{-t^2/2}$ is the characteristic function of $N(0,1)$, and it is continuous at $0$ — so [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]] converts pointwise convergence of characteristic functions into [[Def - Weak Convergence|weak convergence]] of laws: $Z_n\xrightarrow{d}N(0,1)$.

The slogan: **independence turns $\varphi_{S_n/\sqrt n}$ into $\varphi_X(t/\sqrt n)^n$; finite variance gives $\varphi_X(s)\approx1-s^2/2$; and $(1-\frac{t^2}{2n})^n\to e^{-t^2/2}$ — the Gaussian appears because it is the function whose log is exactly quadratic.** Universality is built in: only $\mathbb{E}X=0$ and $\mathbb{E}X^2=1$ enter — the mean and variance — so *every* distribution with those two normalised moments has the same limit. The third and higher moments wash out under the $1/\sqrt n$ scaling.

---

# What Makes This Hard

The proof, *given* [[Thm - Lévy's Continuity Theorem|Lévy's theorem]] and the [[Def - Characteristic Function|moment expansion]], is short — but each ingredient is substantial. The genuine subtleties: (i) one must know that finite *second* moment licenses the *second-order* Taylor expansion of $\varphi_X$ with an $o(s^2)$ remainder — this is exactly the regularity the hypothesis $\sigma^2<\infty$ buys, and no more; (ii) the rescaling $s=t/\sqrt n$ is what makes the linear term vanish (mean $0$) and the quadratic term survive at the right rate — *why $\sqrt n$* is the content; (iii) the heavy lifting is hidden in Lévy's theorem (tightness, Prokhorov). The common error is to forget that finite variance is *essential* — infinite variance gives a different ($\sqrt n$ becomes $n^{1/\alpha}$) scaling and a stable, non-Gaussian limit.

---

# Rederivation Scaffold

**High-level strategy.** Reduce to $\mu=0,\sigma^2=1$. Factor $\varphi_{S_n/\sqrt n}=\varphi_X(t/\sqrt n)^n$ by independence. Taylor-expand $\varphi_X(s)=1-s^2/2+o(s^2)$ using finite variance. Take the $n$-th power, get $e^{-t^2/2}$. Apply Lévy's continuity theorem.

**Subgoal decomposition.**

1. **Normalise.** Replace $X_k$ by $(X_k-\mu)/\sigma$; reduce to $Z_n=S_n/\sqrt n$, $\mathbb{E}X=0$, $\mathbb{E}X^2=1$.
2. **Factor.** Independence $\Rightarrow\varphi_{Z_n}(t)=\varphi_X(t/\sqrt n)^n$.
3. **Expand.** Finite variance $\Rightarrow\varphi_X(s)=1-s^2/2+o(s^2)$ ([[Def - Characteristic Function|moment property]]).
4. **Limit.** $(1-\frac{t^2}{2n}+o(1/n))^n\to e^{-t^2/2}$.
5. **Convert.** $e^{-t^2/2}$ is continuous at $0$ and is $\varphi_{N(0,1)}$; [[Thm - Lévy's Continuity Theorem|Lévy]] $\Rightarrow Z_n\xrightarrow{d}N(0,1)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The characteristic function factors and expands
> **Statement:** For i.i.d. $X_k$ with $\mathbb{E}X=0$, $\mathbb{E}X^2=1$: $\varphi_{S_n/\sqrt n}(t)=\varphi_X(t/\sqrt n)^n$ and $\varphi_X(s)=1-s^2/2+o(s^2)$.
>
> **Hint:** Two independent observations: independence turns the characteristic function of a sum into a product, and finite second moment lets you Taylor-expand $\varphi_X$ around $0$ with the derivatives read off from the moments.
>
> **Why needed:** The product form is what allows the Fourier transform to "see" the central limit phenomenon — [[Def - Convolution|convolutions]] of densities (sums of independent variables) become powers of characteristic functions, and second-order Taylor data is exactly what survives the $1/\sqrt n$ rescaling.
>
> > [!note]- Full proof
> > Independence and the [[Ex - Independence and the factorisation of expectation|convolution-to-product]] property give $\varphi_{S_n/\sqrt n}(t)=\mathbb{E}[\prod_k e^{i(t/\sqrt n)X_k}]=\prod_k\varphi_X(t/\sqrt n)=\varphi_X(t/\sqrt n)^n$. Since $\mathbb{E}X^2<\infty$, $\varphi_X\in C^2$ with $\varphi_X(0)=1$, $\varphi_X'(0)=i\mathbb{E}X=0$, $\varphi_X''(0)=-\mathbb{E}X^2=-1$; Taylor's theorem gives $\varphi_X(s)=1-s^2/2+o(s^2)$. $\square$

> [!note]- Lemma 2: The $n$-th power converges to the Gaussian
> **Statement:** $\varphi_X(t/\sqrt n)^n\to e^{-t^2/2}$ for every $t$.
>
> **Hint:** Take logarithms (legal for large $n$ since the argument is near $1$) and use $\log(1+u)=u+o(u)$: the leading term $-t^2/(2n)$ multiplied by $n$ converges to $-t^2/2$ while the remainder $o(1/n)\cdot n\to 0$.
>
> **Why needed:** This is the explicit Gaussian limit at the characteristic-function level. Combined with Lévy's continuity theorem, pointwise convergence of characteristic functions to $e^{-t^2/2}$ (continuous at $0$) upgrades to weak convergence of distributions to $N(0,1)$ — which is the CLT.
>
> > [!note]- Full proof
> > By Lemma 1, $\varphi_X(t/\sqrt n)=1-\frac{t^2}{2n}+o(1/n)$. Taking logarithms (defined for large $n$, since the argument $\to1$), $n\log\varphi_X(t/\sqrt n)=n(-\frac{t^2}{2n}+o(1/n))=-\frac{t^2}{2}+o(1)\to-\frac{t^2}{2}$. Exponentiate: $\varphi_X(t/\sqrt n)^n\to e^{-t^2/2}$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Reduce to $\mu=0$, $\sigma^2=1$. By Lemmas 1–2, $\varphi_{S_n/\sqrt n}(t)\to e^{-t^2/2}$ for every $t$. The limit $e^{-t^2/2}$ is continuous (everywhere, in particular at $0$) and equals $\varphi_{N(0,1)}$. By [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]], $S_n/\sqrt n\xrightarrow{d}N(0,1)$; undoing the normalisation, $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The CLT underlies **all of inferential statistics** — confidence intervals, $z$- and $t$-tests, the $\sqrt n$ rate of estimator error. Its functional version, **Donsker's invariance principle**, says the rescaled random walk converges weakly (in path space) to Brownian motion — the CLT "for the whole trajectory," and a construction of Brownian motion. The Lindeberg–Feller and [[Def - Martingale|martingale]] CLTs extend it beyond i.i.d.; Stein's method gives quantitative (Berry–Esseen) rates.

---

# Bridges

- **[[Thm - Lévy's Continuity Theorem]]** — the bridge converting "$\varphi_n\to e^{-t^2/2}$" into "$\xrightarrow{d}N(0,1)$"; without it the CLT computation is inconclusive.
- **[[Thm - Strong Law of Large Numbers]]** — the CLT refines the SLLN: it describes the $\sqrt n$-scale fluctuations the law of large numbers shows merely vanish.
- **[[Def - Characteristic Function]]** — the self-duality of the Gaussian ($\varphi=e^{-t^2/2}$, log exactly quadratic) is *why* the Gaussian is the universal limit.
