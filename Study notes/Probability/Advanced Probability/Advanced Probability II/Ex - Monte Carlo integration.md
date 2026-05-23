---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Strong Law of Large Numbers"
  - "Thm - Central Limit Theorem"
tags: [probability, advanced-probability]
---

# Problem Statement

To estimate an integral $I=\int_{[0,1]^d}f(x)\,dx$ of a bounded measurable $f$, draw i.i.d. uniform points $U_1,U_2,\dots$ in $[0,1]^d$ and form $\widehat I_n=\frac1n\sum_{k=1}^n f(U_k)$.

**(a)** Show $\widehat I_n\to I$ almost surely.

**(b)** Show the error $\widehat I_n-I$ is of order $n^{-1/2}$, with $\sqrt n(\widehat I_n-I)\xrightarrow{d}N(0,\sigma^2)$, $\sigma^2=\mathrm{Var}(f(U_1))$.

**(c)** Note that this $n^{-1/2}$ rate is **independent of the dimension $d$** — and explain why this beats grid-based quadrature in high [[Def - Dimension|dimensions]].

**Recall:**

[[Thm - Strong Law of Large Numbers|SLLN]]: $\frac1n\sum X_k\to\mathbb{E}X_1$ a.s. [[Thm - Central Limit Theorem|CLT]]: $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$.

---

# Convergent Strategy

**Problem class:** recognising an estimator as a sample mean, so the limit theorems apply verbatim.

**Assumption pattern:** $f(U_k)$ are i.i.d. (functions of i.i.d. variables), bounded hence in every $L^p$. So $\widehat I_n$ is a sample mean — SLLN for consistency, CLT for the error.

---

# Legal Operations Used

1. **Recognise a sample mean** $\widehat I_n=\frac1n\sum f(U_k)$.
2. **SLLN** for a.s. convergence; **CLT** for the fluctuation scale.

---

# Hints

> [!note]- Hint 1
> $X_k=f(U_k)$ are i.i.d.; $\mathbb{E}[X_1]=\int_{[0,1]^d}f\,dx=I$ by [[Ex - Expectation via the law|change of variables]] (the law of $U_1$ is Lebesgue measure on $[0,1]^d$).

> [!note]- Hint 2
> $\widehat I_n$ is exactly the sample mean of the $X_k$. Apply SLLN, then CLT.

---

# Solution

**Step 1 — (a).** Set $X_k=f(U_k)$. The $U_k$ are i.i.d. uniform, so the $X_k$ are i.i.d.; $f$ bounded $\Rightarrow X_k\in L^\infty\subseteq L^1$. By [[Ex - Expectation via the law|change of variables]], $\mathbb{E}[X_1]=\int_{[0,1]^d}f(x)\,dx=I$ (the law of $U_1$ is Lebesgue measure on the cube). Now $\widehat I_n=\frac1n\sum_{k=1}^n X_k$ is the sample mean, so by the [[Thm - Strong Law of Large Numbers|strong law]],
$$\widehat I_n\xrightarrow{\text{a.s.}}\mathbb{E}[X_1]=I.$$
Monte Carlo estimation is *consistent*: the estimate converges to the true integral, almost surely.

**Step 2 — (b).** $f$ bounded $\Rightarrow X_1\in L^2$, so $\sigma^2=\mathrm{Var}(X_1)<\infty$. By the [[Thm - Central Limit Theorem|central limit theorem]],
$$\sqrt n\,(\widehat I_n-I)=\frac{S_n-nI}{\sqrt n}\xrightarrow{d}N(0,\sigma^2),\qquad S_n=\sum_{k\le n}X_k.$$
So the error $\widehat I_n-I$ is, in distribution, $\approx\sigma\,n^{-1/2}\,Z$ with $Z\sim N(0,1)$ — the **root-$n$ rate**, and the CLT even supplies the constant $\sigma$ for error bars / confidence intervals.

**Step 3 — (c).** The rate $n^{-1/2}$ in (b) contains *no $d$*. By contrast, a grid quadrature with $n$ points puts $n^{1/d}$ points per axis, achieving accuracy $\sim n^{-r/d}$ for an order-$r$ rule — which *degrades catastrophically as $d$ grows* (the curse of dimensionality). Monte Carlo's $n^{-1/2}$ is dimension-blind because it relies only on $\mathrm{Var}(f(U_1))$, a single number, not on resolving $f$ along each axis. For large $d$, $n^{-1/2}$ eventually beats $n^{-r/d}$ — which is why Monte Carlo is the method of choice for high-dimensional integrals (statistical physics, Bayesian computation, finance).

> [!note]- Complete formal solution
> (a) $X_k=f(U_k)$ i.i.d., $\mathbb{E}X_1=\int f=I$; SLLN gives $\widehat I_n\to I$ a.s. (b) $f$ bounded $\Rightarrow\sigma^2=\mathrm{Var}(X_1)<\infty$; CLT gives $\sqrt n(\widehat I_n-I)\xrightarrow{d}N(0,\sigma^2)$. (c) The $n^{-1/2}$ rate is $d$-independent, beating grid quadrature's $n^{-r/d}$ for large $d$. $\blacksquare$

---

# Key Takeaways

**Monte Carlo integration is the [[Thm - Strong Law of Large Numbers|law of large numbers]] put to work: an integral is an expectation, and a sample mean estimates it — consistently (SLLN) with root-$n$ error (CLT).** The recognition "$\widehat I_n$ is a sample mean of i.i.d. $f(U_k)$" is the whole modelling step; the two limit theorems then deliver the convergence and its rate *for free*, the CLT even handing over the constant $\sigma=\sqrt{\mathrm{Var}(f(U_1))}$ for confidence intervals. Any randomised estimator built as an average of i.i.d. terms inherits this analysis.

**The $n^{-1/2}$ rate is independent of dimension — the structural reason Monte Carlo defeats the curse of dimensionality.** Deterministic quadrature must resolve $f$ along every axis, so its accuracy decays like $n^{-r/d}$; the probabilistic method depends only on a *scalar*, $\mathrm{Var}(f(U_1))$, and so does not see $d$ at all. The price is that the error is *random* (a Gaussian fluctuation, not a deterministic bound) and the rate $n^{-1/2}$ is mediocre in low dimensions. The trade — randomness and a slow but dimension-free rate — is exactly why high-dimensional integration in physics, statistics, and finance is done by sampling.
