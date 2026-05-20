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

**Sources.** Hypotheses: $(X_n)$ **i.i.d.** and $\mathbb{E}|X_1|<\infty$ — a finite *first* moment, no more. (An elementary proof needs a finite *fourth* moment; the sharp $L^1$ result needs a [[Def - Martingale|backward-martingale]] or a truncation argument.)

**Targets.** $S_n/n\to\mu$ a.s. is the rigorous law of averages; it underlies the *consistency* of statistical estimators, the **Glivenko–Cantelli theorem** (empirical distribution functions converge uniformly), Monte Carlo integration, and the ergodic theorem (of which the SLLN is the i.i.d. case).

---

# Statement

Let $(X_n)_{n\ge1}$ be **independent and identically distributed** with $\mathbb{E}|X_1|<\infty$ and $\mu=\mathbb{E}[X_1]$. Then
$$\frac{S_n}{n}=\frac{X_1+\cdots+X_n}{n}\ \xrightarrow{\ \text{a.s.}\ }\ \mu\qquad\text{(and also in }L^1\text{)}.$$

---

# Why Is It True

Two ideas combine: the limit is *automatically a constant*, and *backward averaging* identifies which constant.

**The limit is constant.** Whether $S_n/n$ converges, and to what, is a [[Thm - Kolmogorov 0-1 Law|tail]] property — unchanged by altering finitely many $X_k$ (they contribute $O(1/n)\to0$). So by the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]], $\limsup S_n/n$ and $\liminf S_n/n$ are a.s. *constants*. Half the work is done before any estimate: *if* $S_n/n$ converges a.s., the limit is a deterministic number.

**Backward martingale identifies the constant.** The clean modern proof: the symmetry of i.i.d. variables makes $S_n/n$ a *[[Def - Martingale|backward martingale]]*. Concretely, $\mathbb{E}[X_1\mid S_n,S_{n+1},\dots]=S_n/n$ — given the sum $S_n$, each summand is exchangeable, so each has conditional mean $S_n/n$. The $\sigma$-algebras $\mathcal{G}_n=\sigma(S_n,S_{n+1},\dots)$ *decrease*, and $(S_n/n)$ is the backward martingale $\mathbb{E}[X_1\mid\mathcal{G}_n]$. The **backward martingale convergence theorem** then gives $S_n/n\to\mathbb{E}[X_1\mid\mathcal{G}_\infty]$ a.s. and in $L^1$. Finally $\mathcal{G}_\infty$ is the *exchangeable / tail* $\sigma$-algebra, trivial by the 0–1 law, so the conditional expectation collapses to the unconditional one: $S_n/n\to\mathbb{E}[X_1]=\mu$.

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
> > [!note]- Full proof
> > Given $S_n$, the summands $X_1,\dots,X_n$ are *exchangeable* (i.i.d. $\Rightarrow$ their joint law is invariant under permutation, and conditioning on the symmetric function $S_n$ preserves this). So $\mathbb{E}[X_k\mid\mathcal{G}_n]$ is the same for all $k\le n$; averaging, $\mathbb{E}[X_k\mid\mathcal{G}_n]=\frac1n\mathbb{E}[\sum_{j\le n}X_j\mid\mathcal{G}_n]=\frac1n\mathbb{E}[S_n\mid\mathcal{G}_n]=S_n/n$. Adding $X_{n+1},\dots$ as "independent information" does not change this, so $(S_n/n)$ is a backward martingale for the decreasing filtration $(\mathcal{G}_n)$. $\square$

> [!note]- Lemma 2: Identification of the limit
> **Statement:** The backward-martingale limit equals $\mu$.
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
