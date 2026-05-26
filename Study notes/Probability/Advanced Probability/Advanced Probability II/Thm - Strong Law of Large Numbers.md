---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Modes of Convergence"
  - "Thm - Kolmogorov 0-1 Law"
  - "Thm - Borel-Cantelli Lemmas"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ i.i.d. random variables with $\mathbb{E}|X_1|<\infty$, $\mu=\mathbb{E}[X_1]$; $S_n=X_1+\cdots+X_n$.

---

# Motivation

The [[Thm - Weak Law of Large Numbers|weak law]] says the sample mean is *probably* close to $\mu$ for large $n$. The strong law says more: with probability one, the *entire sequence* $S_n/n$ converges to $\mu$. A single realisation — one infinite run of the experiment — has its averages settling down to the theoretical mean, no exceptions off a null set. This is the theorem that makes "probability $=$ long-run frequency" a *theorem* rather than a definition, and it converges in the strongest mode, **almost surely**, under the *minimal* hypothesis $\mathbb{E}|X_1|<\infty$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is i.i.d. with $\mathbb{E}|X_1|<\infty$, but "a.s. convergence of sample averages" survives, with minor adjustments, far beyond the i.i.d. world. Recognising a problem as having SLLN-flavoured structure lets one invoke a law-of-averages conclusion without literally having an i.i.d. sample.

The first source is **a sequence of independent but not identically distributed variables with $\sum_n\mathrm{Var}(X_n)/n^2<\infty$**. Variability across the sequence is often unavoidable: measurement errors with drifting variance, contributions of differently-sized experiments, returns of an evolving portfolio. The bridge is **Kolmogorov's variant of the SLLN**: under independence and $\sum_n\mathrm{Var}(X_n)/n^2<\infty$, one has $\frac1n\sum_k(X_k-\mathbb{E}X_k)\to0$ a.s. The example: estimating a slowly-varying mean from sensor readings $X_k=\mu_k+\varepsilon_k$ with $\mathrm{Var}(\varepsilon_k)\le k^{3/2}$ — the variance grows but slower than $k^2$, so the centred sample average still converges a.s. around the true mean trajectory.

The second source is **a stationary ergodic sequence**. Sequences with memory but no time-drift appear everywhere — outputs of a stationary Markov chain at equilibrium, returns of a financial time series with no regime change, samples from a Gibbs distribution by MCMC. The bridge is **Birkhoff's pointwise ergodic theorem**: for a measure-preserving $T$ on $(\Omega,\mathcal{F},\mathbb{P})$ and integrable $f$, $\frac1n\sum_{k=0}^{n-1}f(T^k\omega)\to\mathbb{E}[f\mid\mathcal{I}]$ a.s., where $\mathcal{I}$ is the invariant $\sigma$-algebra; if $T$ is ergodic, the limit collapses to $\mathbb{E}f$ — recovering the SLLN exactly (the i.i.d. case being $T$ a Bernoulli shift). The example: the sample autocorrelation $\frac1n\sum_k X_k X_{k+1}$ of a stationary AR(1) sequence $X_{n+1}=\rho X_n+\varepsilon_n$ converges a.s. to its expectation despite dependence between consecutive terms.

The third source is **time averages of an ergodic Markov chain**. Markov chains arrive without literal i.i.d. structure: successive states are dependent, but the chain spends a fraction $\pi(x)$ of its time in each state $x$, where $\pi$ is the stationary distribution. The bridge: the **Markov chain ergodic theorem** says that if a chain is irreducible, aperiodic, and positive recurrent with stationary $\pi$, then for any $f\in L^1(\pi)$, $\frac1n\sum_{k=1}^n f(X_k)\to\int f\,d\pi$ a.s. — proved by realising the time average as a Birkhoff average over a measure-preserving shift on path space. The example: estimating $\int f\,d\pi$ for an unknown $\pi$ on a high-dimensional state space by running an MCMC chain — convergence of the sample average is exactly an SLLN for an ergodic stationary sequence.

**Targets (Output Amplification)**

The conclusion is "the sample mean of an i.i.d. sequence converges a.s. to its expectation." Composed with other tools, each instance of this conclusion becomes a much stronger uniform or operational statement.

The first amplification is **SLLN applied to a parametric family of indicator functions**: take $X_k=\mathbf{1}_{\{Y_k\le t\}}$ for i.i.d. $Y_k$ and fixed $t$. The SLLN gives the empirical c.d.f. $F_n(t)=\frac1n\sum_k\mathbf{1}_{\{Y_k\le t\}}\to F(t)$ a.s. at every fixed $t$. Combined with monotonicity of $F$ and a separability argument, this upgrades to uniform a.s. convergence $\sup_t|F_n(t)-F(t)|\to0$ — the **Glivenko–Cantelli theorem**, foundation of nonparametric statistics and the Kolmogorov–Smirnov test. The non-obvious upshot is that pointwise SLLN plus the structural fact that c.d.f.s are monotone delivers the supremum norm for free. The example: the bootstrap is valid because $F_n\to F$ uniformly, so resampling from $F_n$ approximates resampling from $F$ at all confidence levels simultaneously.

The second amplification is **SLLN combined with Monte Carlo integration**. To compute $I=\int_{\mathbb{R}^d}f(x)\,p(x)\,dx$ for a probability density $p$ in high dimension, draw $X_1,\dots,X_n\sim p$ i.i.d. and average: $\hat I_n=\frac1n\sum_k f(X_k)\to I$ a.s. by the SLLN. The non-obvious upshot is dimension-independent convergence: the a.s. rate is governed by $\mathrm{Var}(f(X))$ alone, not by the dimension $d$ — in stark contrast to deterministic quadrature, which suffers an $n^{-1/d}$ rate. The example: every Bayesian posterior expectation computed by MCMC, every reinforcement-learning value estimate, every quantum Monte Carlo energy is an SLLN amplification applied to ergodic samples from $p$.

The third amplification is **SLLN combined with [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] to extract fluctuation control**. SLLN says $S_n/n\to\mu$ a.s. but says nothing about the *rate*. Combining with Chebyshev gives $\sum_n\mathbb{P}(|S_n/n-\mu|>\varepsilon)<\infty$ along geometric subsequences, and BC1 promotes this to almost-sure summability of deviation events; iterating with sharper concentration bounds (Hoeffding, Cramér–Chernoff) yields the **law of the iterated logarithm**, $\limsup_n(S_n-n\mu)/\sqrt{2n\sigma^2\log\log n}=1$ a.s. — a precise envelope for the fluctuations the SLLN merely shows are $o(n)$. The example: in fair-coin tosses, SLLN says the head-fraction tends to $1/2$; the iterated-log law amplifies this to "the cumulative excess of heads oscillates within $\pm\sqrt{2n\log\log n}$ infinitely often and never beyond" — a far sharper operational guarantee downstream of the SLLN's a.s. statement.

---

# Statement

Let $(X_n)_{n\ge1}$ be **independent and identically distributed** with $\mathbb{E}|X_1|<\infty$ and $\mu=\mathbb{E}[X_1]$. Then
$$\frac{S_n}{n}=\frac{X_1+\cdots+X_n}{n}\ \xrightarrow{\ \text{a.s.}\ }\ \mu\qquad\text{(and also in }L^1\text{)}.$$

---

# Why Is It True

Two ideas combine: the limit is *automatically a constant*, and *backward averaging* identifies which constant.

**The limit is constant.** Whether $S_n/n$ converges, and to what, is a [[Thm - Kolmogorov 0-1 Law|tail]] property — unchanged by altering finitely many $X_k$ (they contribute $O(1/n)\to0$). So by the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]], $\limsup S_n/n$ and $\liminf S_n/n$ are a.s. *constants*. Half the work is done before any estimate: *if* $S_n/n$ converges a.s., the limit is a deterministic number.

**Backward [[Def - Martingale|martingale]] identifies the constant.** The clean modern proof: the symmetry of i.i.d. variables makes $S_n/n$ a *[[Def - Martingale|backward martingale]]*. Concretely, $\mathbb{E}[X_1\mid S_n,S_{n+1},\dots]=S_n/n$ — given the sum $S_n$, each summand is exchangeable, so each has conditional mean $S_n/n$. The $\sigma$-algebras $\mathcal{G}_n=\sigma(S_n,S_{n+1},\dots)$ *decrease*, and $(S_n/n)$ is the backward martingale $\mathbb{E}[X_1\mid\mathcal{G}_n]$. The **backward martingale convergence theorem** then gives $S_n/n\to\mathbb{E}[X_1\mid\mathcal{G}_\infty]$ a.s. and in $L^1$. Finally $\mathcal{G}_\infty$ is the *exchangeable / tail* $\sigma$-algebra, trivial by the 0–1 law, so the conditional expectation collapses to the unconditional one: $S_n/n\to\mathbb{E}[X_1]=\mu$.

The slogan: **the 0–1 law makes the limit a constant; the backward-martingale structure makes the constant $\mu$.** (The elementary fourth-moment route instead bounds $\mathbb{E}[(S_n/n)^4]=O(n^{-2})$, sums over $n$, and applies [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] — averaging kills the fourth moment fast enough that $S_n/n\to0$ a.s. along the full sequence.)

---

# What Makes This Hard

Unlike the [[Thm - Weak Law of Large Numbers|weak law]], the strong law is genuinely deep. The hard part is upgrading "in probability" to "almost surely" *along the whole sequence* — a.s. convergence is not the limit of in-probability statements. Two honest routes, two difficulties: the **fourth-moment proof** is easy but assumes far too much ($\mathbb{E}X_1^4<\infty$); the **$L^1$ proof** assumes only $\mathbb{E}|X_1|<\infty$ but needs the [[Def - Martingale|backward-martingale]] machinery (or a delicate truncation). The non-obvious structural insight is that $S_n/n$ is a *backward* martingale — running the martingale convergence theorem in reverse time.

---

# Rederivation Scaffold

**High-level strategy.** 0–1 law $\Rightarrow$ any a.s. limit is constant. Recognise $S_n/n=\mathbb{E}[X_1\mid\mathcal{G}_n]$ as a backward martingale on the decreasing $\mathcal{G}_n=\sigma(S_n,S_{n+1},\dots)$; backward convergence gives an a.s.+$L^1$ limit; triviality of $\mathcal{G}_\infty$ identifies it as $\mu$.

**Subgoal decomposition.**

1. **Limit is constant.** Convergence of $S_n/n$ is tail-measurable; [[Thm - Kolmogorov 0-1 Law|0–1 law]].
2. **Backward martingale.** By exchangeability, $\mathbb{E}[X_1\mid\mathcal{G}_n]=S_n/n$, with $\mathcal{G}_n\downarrow$.
3. **Backward convergence.** $\mathbb{E}[X_1\mid\mathcal{G}_n]\to\mathbb{E}[X_1\mid\mathcal{G}_\infty]$ a.s. and in $L^1$.
4. **Identify the limit.** $\mathcal{G}_\infty$ trivial $\Rightarrow\mathbb{E}[X_1\mid\mathcal{G}_\infty]=\mathbb{E}[X_1]=\mu$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The sample mean is a backward martingale
> **Statement:** With $\mathcal{G}_n=\sigma(S_n,S_{n+1},\dots)$, $\mathbb{E}[X_1\mid\mathcal{G}_n]=S_n/n$.
>
> **Hint:** Use exchangeability — conditioning on the symmetric statistic $S_n$ makes $X_1,\dots,X_n$ have identical conditional law, so averaging $n$ identical conditional expectations recovers $S_n/n$.
>
> **Why needed:** Recognising $S_n/n$ as a (backward) martingale is the *unifying frame* of this proof: convergence then comes for free from the backward martingale convergence theorem, with no quantitative truncation/variance argument needed (unlike Kolmogorov's original proof).
>
> > [!note]- Full proof
> > Given $S_n$, the summands $X_1,\dots,X_n$ are *exchangeable* (i.i.d. $\Rightarrow$ their joint law is invariant under permutation, and conditioning on the symmetric function $S_n$ preserves this). So $\mathbb{E}[X_k\mid\mathcal{G}_n]$ is the same for all $k\le n$; averaging, $\mathbb{E}[X_k\mid\mathcal{G}_n]=\frac1n\mathbb{E}[\sum_{j\le n}X_j\mid\mathcal{G}_n]=\frac1n\mathbb{E}[S_n\mid\mathcal{G}_n]=S_n/n$. Adding $X_{n+1},\dots$ as "independent information" does not change this, so $(S_n/n)$ is a backward martingale for the decreasing [[Def - Filtration|filtration]] $(\mathcal{G}_n)$. $\square$

> [!note]- Lemma 2: Identification of the limit
> **Statement:** The backward-martingale limit equals $\mu$.
>
> **Hint:** The tail $\sigma$-algebra $\mathcal{G}_\infty=\bigcap_n\sigma(S_n,S_{n+1},\dots)$ is contained in the i.i.d. tail $\sigma$-algebra, which is trivial by Kolmogorov's 0-1 law; conditional expectation with respect to a trivial $\sigma$-algebra collapses to the unconditional expectation.
>
> **Why needed:** The backward martingale convergence theorem only tells you that $S_n/n$ converges — it does not say *what* the limit is. This lemma pins the limit down as the deterministic constant $\mu$, which is the entire conclusion of SLLN.
>
> > [!note]- Full proof
> > The backward martingale convergence theorem gives $S_n/n=\mathbb{E}[X_1\mid\mathcal{G}_n]\to\mathbb{E}[X_1\mid\mathcal{G}_\infty]$ a.s. and in $L^1$, where $\mathcal{G}_\infty=\bigcap_n\mathcal{G}_n$. By the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]], $\mathcal{G}_\infty$ (the tail $\sigma$-algebra) is trivial, so $\mathbb{E}[X_1\mid\mathcal{G}_\infty]$ is a.s. the constant $\mathbb{E}[X_1]=\mu$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $S_n/n=\mathbb{E}[X_1\mid\mathcal{G}_n]$ is a backward martingale on the decreasing $\mathcal{G}_n=\sigma(S_n,S_{n+1},\dots)$. The backward-martingale convergence theorem yields a.s. and $L^1$ convergence to $\mathbb{E}[X_1\mid\mathcal{G}_\infty]$, which by Lemma 2 (triviality of $\mathcal{G}_\infty$, [[Thm - Kolmogorov 0-1 Law|0–1 law]]) equals $\mu$. Hence $S_n/n\to\mu$ a.s. and in $L^1$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The SLLN applied to $X_k=\mathbf{1}_{\{Y_k\le t\}}$ gives the **Glivenko–Cantelli theorem** — the empirical distribution function converges uniformly to the true one, the foundation of nonparametric statistics. It is the i.i.d. special case of **Birkhoff's pointwise ergodic theorem** (replace independence by measure-preserving stationarity). Monte Carlo integration *is* the SLLN: $\frac1n\sum f(U_k)\to\int f$.

---

# Bridges

- **[[Thm - Weak Law of Large Numbers]]** — the SLLN's strictly weaker sibling (in probability, finite variance); the SLLN converges a.s. under only $\mathbb{E}|X_1|<\infty$.
- **[[Thm - Kolmogorov 0-1 Law]]** — guarantees the limit is a constant, doing half the work for free.
- **[[Thm - Central Limit Theorem]]** — describes the $1/\sqrt n$-scale Gaussian fluctuations around the SLLN's limit.
