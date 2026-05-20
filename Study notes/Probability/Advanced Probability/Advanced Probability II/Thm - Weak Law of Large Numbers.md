---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Modes of Convergence"
  - "Def - Expectation and Moments"
  - "Ex - Markov's inequality"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ i.i.d. (or just uncorrelated, identically distributed) random variables, mean $\mu=\mathbb{E}[X_1]$, variance $\sigma^2=\mathrm{Var}(X_1)<\infty$; $S_n=X_1+\cdots+X_n$.

---

# Motivation

The intuitive content of probability: *the average of many independent repetitions of an experiment converges to the theoretical mean*. The weak law of large numbers is the first rigorous form — the sample mean $S_n/n$ converges to $\mu$ **in probability**. It is the theorem that justifies estimating an expectation by an average, and its proof is a one-line application of [[Ex - Markov's inequality|Chebyshev's inequality]], exposing the mechanism transparently: averaging *kills variance*.

---

# Sources and Targets

**Sources.** Hypotheses: identically distributed, *finite variance*, and *uncorrelated* (pairwise — full [[Def - Independence|independence]] is not needed, since only variance is used). The finite-variance hypothesis is what the proof consumes; it can be relaxed (the weak law holds under just $\mathbb{E}|X_1|<\infty$) at the cost of a harder truncation argument.

**Targets.** $S_n/n\xrightarrow{\mathbb{P}}\mu$ — combines with [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] (and a sharper variance bound) to yield the [[Thm - Strong Law of Large Numbers|strong law]]; it is the prototype *concentration* statement, refined by large deviations.

---

# Statement

Let $(X_n)_{n\ge1}$ be identically distributed and **pairwise uncorrelated**, with $\mu=\mathbb{E}[X_1]$ and $\sigma^2=\mathrm{Var}(X_1)<\infty$. Then
$$\frac{S_n}{n}=\frac{X_1+\cdots+X_n}{n}\ \xrightarrow{\ \mathbb{P}\ }\ \mu\qquad\text{as }n\to\infty,$$
i.e. $\mathbb{P}(|S_n/n-\mu|>\varepsilon)\to0$ for every $\varepsilon>0$.

---

# Why Is It True

The sample mean has the *same expectation* as a single variable but a *much smaller variance* — and small variance forces concentration.

$\mathbb{E}[S_n/n]=\frac1n\sum\mathbb{E}[X_k]=\mu$. For the variance, uncorrelatedness makes variance additive: $\mathrm{Var}(S_n)=\sum_k\mathrm{Var}(X_k)=n\sigma^2$, so
$$\mathrm{Var}\!\left(\frac{S_n}{n}\right)=\frac{1}{n^2}\mathrm{Var}(S_n)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}\ \xrightarrow[n\to\infty]{}\ 0.$$
The averaging divides the variance by $n$. Now [[Ex - Markov's inequality|Chebyshev's inequality]] converts "small variance" into "concentration near the mean":
$$\mathbb{P}\!\left(\left|\frac{S_n}{n}-\mu\right|>\varepsilon\right)\le\frac{\mathrm{Var}(S_n/n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\ \xrightarrow[n\to\infty]{}\ 0.$$
The slogan: **averaging $n$ uncorrelated copies leaves the mean fixed but shrinks the variance by a factor $n$; Chebyshev turns vanishing variance into convergence in probability.** Uncorrelatedness is used *once* — to make $\mathrm{Var}(S_n)=n\sigma^2$ rather than something larger.

---

# What Makes This Hard

It is not hard — that is the point. The only things to see: (i) variance is additive *for uncorrelated* summands (the cross terms $\mathrm{Cov}(X_j,X_k)$ vanish), so $\mathrm{Var}(S_n/n)=\sigma^2/n$; (ii) [[Ex - Markov's inequality|Chebyshev]] is the bridge from variance to probability. The genuine subtlety is *what is not needed*: full independence is overkill (uncorrelated suffices), and finite variance, while convenient, is more than necessary (the weak law survives under $\mathbb{E}|X_1|<\infty$ via truncation).

---

# Rederivation Scaffold

**High-level strategy.** Compute $\mathbb{E}[S_n/n]=\mu$ and $\mathrm{Var}(S_n/n)=\sigma^2/n$ (additivity of variance for uncorrelated summands); apply Chebyshev.

**Subgoal decomposition.**

1. **Mean.** $\mathbb{E}[S_n/n]=\mu$ by linearity.
2. **Variance.** Uncorrelated $\Rightarrow\mathrm{Var}(S_n)=n\sigma^2\Rightarrow\mathrm{Var}(S_n/n)=\sigma^2/n$.
3. **Chebyshev.** $\mathbb{P}(|S_n/n-\mu|>\varepsilon)\le\sigma^2/(n\varepsilon^2)\to0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Variance of the sample mean
> **Statement:** $\mathrm{Var}(S_n/n)=\sigma^2/n$.
>
> > [!note]- Full proof
> > $\mathrm{Var}(S_n)=\mathrm{Var}(\sum_k X_k)=\sum_k\mathrm{Var}(X_k)+2\sum_{j<k}\mathrm{Cov}(X_j,X_k)=n\sigma^2$, the cross terms vanishing since the $X_k$ are uncorrelated. Then $\mathrm{Var}(S_n/n)=n^{-2}\mathrm{Var}(S_n)=\sigma^2/n$. $\square$

> [!note]- Lemma 2: Chebyshev finishes
> **Statement:** $\mathbb{P}(|S_n/n-\mu|>\varepsilon)\le\sigma^2/(n\varepsilon^2)$.
>
> > [!note]- Full proof
> > $S_n/n$ has mean $\mu$ and variance $\sigma^2/n$ (Lemma 1). [[Ex - Markov's inequality|Chebyshev's inequality]] $\mathbb{P}(|Y-\mathbb{E}Y|>\varepsilon)\le\mathrm{Var}(Y)/\varepsilon^2$ with $Y=S_n/n$ gives the bound, which $\to0$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 gives $\mathrm{Var}(S_n/n)=\sigma^2/n$; Lemma 2 (Chebyshev) gives $\mathbb{P}(|S_n/n-\mu|>\varepsilon)\le\sigma^2/(n\varepsilon^2)\to0$ for every $\varepsilon>0$, i.e. $S_n/n\xrightarrow{\mathbb{P}}\mu$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The same Chebyshev argument, with a sharper variance bound, gives **Bernstein's polynomial approximation** of continuous functions (a probabilistic proof of the Weierstrass theorem) and the **estimate of a probability by a frequency** that underlies statistics. Refining "variance small" to "exponentially small tails" upgrades the weak law to a [[Thm - Cramér's Theorem|large-deviation]] statement.

---

# Bridges

- **[[Thm - Strong Law of Large Numbers]]** — strengthens "in probability" to "almost surely," requiring more work (a martingale or a fourth-moment argument).
- **[[Ex - Markov's inequality]]** — Chebyshev is the engine; the weak law is its headline application.
- **[[Thm - Central Limit Theorem]]** — describes the *fluctuations* $S_n/n-\mu$, of order $1/\sqrt n$, that the weak law only says vanish.
