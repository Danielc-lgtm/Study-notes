---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Martingale"
  - "Def - Stopping Time"
  - "Thm - Properties of Conditional Expectation"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ a [[Def - Martingale|martingale]] (or super/submartingale) on a [[Def - Filtration|filtered space]]; $S\le T$ [[Def - Stopping Time|stopping times]]; $X_n^T=X_{T\wedge n}$ the stopped process.

---

# Motivation

A [[Def - Martingale|martingale]] is a fair game: $\mathbb{E}[X_n]=\mathbb{E}[X_0]$ at every *fixed* time. The optional stopping theorem asserts the far stronger statement that fairness *survives stopping at a random time*: $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ for a [[Def - Stopping Time|stopping time]] $T$ (under a boundedness or uniform-integrability hypothesis). No betting strategy and no quitting rule that uses only past information can beat a fair game — "you cannot get rich on a [[Def - Martingale|martingale]]." This is the theorem that *computes* hitting probabilities and expected hitting times, and the boundedness hypothesis is exactly what rules out the gambler's-ruin / doubling-strategy paradoxes.

---

# Sources and Targets

**Sources.** Hypotheses: $(X_n)$ a (super)martingale and the stopping time $T$ **bounded** ($T\le N$), *or* $T$ a.s. finite with $(X_n^T)$ **uniformly integrable**. The boundedness/UI hypothesis is essential — without it the conclusion fails (a random walk's first hitting time of $1$ has $\mathbb{E}[X_T]=1\neq0=\mathbb{E}[X_0]$).

**Targets.** $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ — and, applied to the two-sided hitting time of a random walk, it yields **gambler's ruin** probabilities and (with the martingale $X_n^2-n$) **expected hitting times**; applied to $\{X_n^T\}$ it shows the stopped process is itself a martingale.

---

# Statement

Let $(X_n)$ be a martingale and $S\le T$ stopping times.

**(Bounded case.)** If $T$ is **bounded** ($T\le N$ for a constant $N$), then $X_S,X_T\in L^1$ and
$$\mathbb{E}[X_T\mid\mathcal{F}_S]=X_S,\qquad\text{hence}\qquad\mathbb{E}[X_T]=\mathbb{E}[X_S]=\mathbb{E}[X_0].$$
For a *super*martingale, $\mathbb{E}[X_T\mid\mathcal{F}_S]\le X_S$; for a *sub*martingale, $\ge$.

**(Stopped process.)** For *any* stopping time $T$, the stopped process $(X_n^T)=(X_{T\wedge n})$ is a martingale (resp. super/sub) — so $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$ always.

**(Unbounded case.)** If $T<\infty$ a.s. and $(X_n^T)$ is [[Def - Uniform Integrability|uniformly integrable]] (e.g. $|X_n^T|\le Y$ for $Y\in L^1$, or $T\in L^1$ with bounded increments), then $X_{T\wedge n}\to X_T$ in $L^1$ and again $\mathbb{E}[X_T]=\mathbb{E}[X_0]$.

---

# Why Is It True

**The stopped process is a martingale** — this is the engine. Write the increment of the stopped process: $X_{(n+1)\wedge T}-X_{n\wedge T}=(X_{n+1}-X_n)\mathbf{1}_{\{T>n\}}$ — the process moves on step $n+1$ *only if it has not yet stopped*. Now $\{T>n\}=\{T\le n\}^c\in\mathcal{F}_n$ (the defining property of a [[Def - Stopping Time|stopping time]]!), so the indicator $\mathbf{1}_{\{T>n\}}$ is $\mathcal{F}_n$-measurable. Taking $\mathbb{E}[\cdot\mid\mathcal{F}_n]$ and *[[Thm - Properties of Conditional Expectation|taking out what is known]]*,
$$\mathbb{E}[X_{(n+1)\wedge T}-X_{n\wedge T}\mid\mathcal{F}_n]=\mathbf{1}_{\{T>n\}}\,\mathbb{E}[X_{n+1}-X_n\mid\mathcal{F}_n]=\mathbf{1}_{\{T>n\}}\cdot0=0.$$
So $(X_n^T)$ is a martingale. *The stopping decision is $\mathcal{F}_n$-measurable, so it cannot exploit the next increment — fairness is untouched.* This is the whole idea, and it is exactly where non-anticipation of $T$ is used.

**Bounded case.** Since $(X_n^T)$ is a martingale, $\mathbb{E}[X_{n\wedge T}]=\mathbb{E}[X_0]$ for *every* $n$. With $T\le N$, take $n=N$: $T\wedge N=T$, so $\mathbb{E}[X_T]=\mathbb{E}[X_0]$. The conditional statement $\mathbb{E}[X_T\mid\mathcal{F}_S]=X_S$ follows by applying the same to the martingale stopped between $S$ and $T$.

**Unbounded case.** $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$ holds for all $n$; one wants to let $n\to\infty$. Since $T<\infty$ a.s., $X_{T\wedge n}\to X_T$ a.s.; *uniform integrability* of $(X_n^T)$ then upgrades this to $L^1$-convergence ([[Thm - Vitali Convergence Theorem|Vitali]]), so $\mathbb{E}[X_T]=\lim\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$.

The slogan: **a stopping time's decision uses only past information, so stopping cannot tilt the next fair increment — the stopped process is still a martingale; then "stop at a fixed time $N\ge T$" (bounded case) or "pass to the limit, controlled by uniform integrability" (unbounded case) reads off $\mathbb{E}[X_T]=\mathbb{E}[X_0]$.**

---

# What Makes This Hard

The clean idea — *the stopped process is a martingale* — is easy *once* one sees the increment identity $X_{(n+1)\wedge T}-X_{n\wedge T}=(X_{n+1}-X_n)\mathbf{1}_{\{T>n\}}$ and recognises $\mathbf{1}_{\{T>n\}}$ as $\mathcal{F}_n$-measurable. The genuine pitfall is the **unbounded case**: $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$ always holds, but *passing to the limit is illegitimate without uniform integrability*. The standard cautionary example: simple random walk, $T=\inf\{n:X_n=1\}$ is a.s. finite, yet $\mathbb{E}[X_T]=1\neq0=\mathbb{E}[X_0]$ — because $(X_n^T)$ is not uniformly integrable (the walk can go arbitrarily negative before hitting $1$). Forgetting the boundedness/UI hypothesis is *the* classic error and the source of every "free lunch" fallacy.

---

# Rederivation Scaffold

**High-level strategy.** Show the stopped process is a martingale via the increment identity (the stopping decision is $\mathcal{F}_n$-measurable). Bounded $T$: evaluate at $n=N\ge T$. Unbounded $T$: $X_{T\wedge n}\to X_T$ a.s., upgrade to $L^1$ by uniform integrability.

**Subgoal decomposition.**

1. **Increment identity.** $X_{(n+1)\wedge T}-X_{n\wedge T}=(X_{n+1}-X_n)\mathbf{1}_{\{T>n\}}$, with $\{T>n\}\in\mathcal{F}_n$.
2. **Stopped process is a martingale.** $\mathbb{E}[\text{increment}\mid\mathcal{F}_n]=\mathbf{1}_{\{T>n\}}\mathbb{E}[X_{n+1}-X_n\mid\mathcal{F}_n]=0$.
3. **Bounded case.** $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$; set $n=N\ge T$.
4. **Unbounded case.** $X_{T\wedge n}\to X_T$ a.s.; UI of $(X_n^T)$ $\Rightarrow L^1$-convergence $\Rightarrow\mathbb{E}[X_T]=\mathbb{E}[X_0]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The stopped process is a martingale
> **Statement:** For a martingale $(X_n)$ and stopping time $T$, $(X_n^T)=(X_{T\wedge n})$ is a martingale.
>
> **Hint:** The increment $X_{(n+1)\wedge T}-X_{n\wedge T}=(X_{n+1}-X_n)\mathbf{1}_{\{T>n\}}$ telescopes, and $\{T>n\}\in\mathcal{F}_n$ is the defining property of a stopping time — pull it out of the conditional expectation.
>
> **Why needed:** Stopped processes preserve the martingale structure, so $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$ for *every* $n$. This is the basic identity that the unbounded case (Lemma 2) extends by sending $n\to\infty$ — without preservation of martingaleness under stopping, there would be no anchor identity to pass to the limit.
>
> > [!note]- Full proof
> > $X_{(n+1)\wedge T}-X_{n\wedge T}=(X_{n+1}-X_n)\mathbf{1}_{\{T>n\}}$: if $T\le n$ both stopped values are $X_T$, difference $0$; if $T>n$ the difference is the genuine increment. Now $\{T>n\}=\{T\le n\}^c\in\mathcal{F}_n$ since $T$ is a [[Def - Stopping Time|stopping time]], so by [[Thm - Properties of Conditional Expectation|taking out what is known]], $\mathbb{E}[X_{(n+1)\wedge T}-X_{n\wedge T}\mid\mathcal{F}_n]=\mathbf{1}_{\{T>n\}}\,\mathbb{E}[X_{n+1}-X_n\mid\mathcal{F}_n]=0$. With $(X_n^T)$ adapted and integrable ($|X_{T\wedge n}|\le\max_{k\le n}|X_k|$), it is a martingale. $\square$

> [!note]- Lemma 2: Passing to the limit
> **Statement:** If $T<\infty$ a.s. and $(X_n^T)$ is uniformly integrable, $\mathbb{E}[X_T]=\mathbb{E}[X_0]$.
>
> **Hint:** $T<\infty$ a.s. forces $X_{T\wedge n}\to X_T$ a.s.; Vitali (a.s. + UI $\Rightarrow$ $L^1$) upgrades convergence of the random variables to convergence of their expectations.
>
> **Why needed:** This is where uniform integrability earns its keep — without UI, the gambler's-ruin counterexample (asymmetric random walks reaching $1$ with probability $1$) shows $\mathbb{E}[X_T]\ne\mathbb{E}[X_0]$ even though $T<\infty$ a.s. UI rules out the escape-of-mass mechanism that prevents expectations from passing to the limit.
>
> > [!note]- Full proof
> > By Lemma 1, $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_{T\wedge 0}]=\mathbb{E}[X_0]$ for all $n$. Since $T<\infty$ a.s., $T\wedge n=T$ for $n$ large, so $X_{T\wedge n}\to X_T$ a.s. Uniform integrability of $(X_{T\wedge n})_n$ upgrades a.s. convergence to $L^1$-convergence ([[Thm - Vitali Convergence Theorem|Vitali]]), so $\mathbb{E}[X_T]=\lim_n\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1: $(X_n^T)$ is a martingale, so $\mathbb{E}[X_{T\wedge n}]=\mathbb{E}[X_0]$ for all $n$. Bounded case: $T\le N\Rightarrow X_{T\wedge N}=X_T$, giving $\mathbb{E}[X_T]=\mathbb{E}[X_0]$; the conditional form $\mathbb{E}[X_T\mid\mathcal{F}_S]=X_S$ follows by applying this between the stopping times $S$ and $T$. Unbounded case: Lemma 2. The supermartingale/submartingale versions replace "$=0$" by "$\le0$"/"$\ge0$" in Lemma 1. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Optional stopping *computes*. For simple random walk on $\{0,\dots,N\}$ started at $k$, applying it to the martingale $(X_n)$ at the exit time gives the **gambler's ruin probability** $k/N$; applying it to $(X_n^2-n)$ gives the **expected exit time** $k(N-k)$. The same theorem prices American options (the optimal exercise time is a stopping time) and proves Wald's identities in sequential analysis.

---

# Bridges

- **[[Def - Stopping Time]]** — non-anticipation is exactly what makes $\mathbf{1}_{\{T>n\}}\in\mathcal{F}_n$, the crux of Lemma 1.
- **[[Thm - Properties of Conditional Expectation]]** — "taking out what is known" is the one tool the proof needs.
- **[[Thm - Almost Sure Martingale Convergence]]** — the unbounded case's limiting argument is the same a.s.+UI machinery.
