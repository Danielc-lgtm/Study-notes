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

**Sources (Input Broadening)**

The literal hypothesis is "$(X_n)$ a martingale and $T$ bounded, or $T$ a.s. finite with $(X_n^T)$ uniformly integrable." Many concrete problems do not arrive in this form; the most common disguises are below.

The first source is **any stopping time $T$ that admits an a.s. upper bound by a constant deterministic time** — even if the problem does not call $T$ "bounded." For instance, the exit time of a finite-state Markov chain from a finite domain is bounded above by the chain's "maximum-detour" deterministic time; the time at which a sequential statistical test must terminate by experimental protocol is bounded by sample size; the maturity of a barrier option is bounded by expiry. The bridge $B \to A$ is trivial — $T \le N$ a.s. *is* the bounded-stopping-time hypothesis — but recognising the boundedness in disguise is the work. A concrete example: a gambler must quit by closing time at $N=100$ rounds, even if their personal rule is "quit when ahead by $\$10$." The hitting time $T$ might be unbounded by the personal rule alone, but $T \wedge 100$ is bounded, and the optional stopping theorem applies to the truncated stopping time, yielding $\mathbb{E}[X_{T\wedge 100}] = \mathbb{E}[X_0]$ — exactly what is needed to compute the gambler's expected fortune at closing.

The second source is **any closed martingale $X_n = \mathbb{E}[X_\infty\mid\mathcal{F}_n]$ with an a.s.-finite stopping time $T$**. Closed martingales are automatically uniformly integrable (the family $\{\mathbb{E}[X_\infty\mid\mathcal{G}] : \mathcal{G} \text{ sub-}\sigma\text{-algebra}\}$ is UI), so the stopped process $(X_n^T)$ is UI as a sub-collection. The bridge $B \to A$: closed $\Rightarrow$ UI $\Rightarrow$ $(X_n^T)$ UI. A concrete example: $X_n = \mathbb{E}[Y\mid\mathcal{F}_n]$ for some $Y\in L^1$ — a [[Thm - Almost Sure Martingale Convergence|Doob–Lévy martingale]] — appears every time one writes "best estimate of $Y$ given information up to time $n$." For any a.s.-finite stopping time $T$, optional stopping gives $\mathbb{E}[X_T] = \mathbb{E}[Y]$. This is the cleanest form of the theorem and the one used in nearly all filtration-tracking arguments.

The third source is **any bounded $L^\infty$ martingale stopped at any a.s.-finite stopping time**: $|X_n|\le M$ a.s. for some constant $M$ forces $|X_n^T|\le M$, and a uniformly bounded family is uniformly integrable. The bridge $B \to A$: $L^\infty$-boundedness $\Rightarrow$ trivial UI. A concrete example: the proportion of red balls in [[Def - Martingale|Pólya's urn]] is a martingale in $[0,1]$, hence bounded. For any random time $T$ at which one inspects the urn (say, "the first time both colours have been drawn at least once"), the expected proportion at time $T$ equals the initial proportion — instantly, by optional stopping applied to a bounded martingale, with no need to check UI by hand.

**Targets (Output Amplification)**

The bare conclusion $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ is a single number identity. The amplifications below are where it becomes a computational engine.

The first amplification combines optional stopping with **the martingales of a random walk**. For simple symmetric random walk on $\mathbb{Z}$ started at $k$ with exit time $T$ from $\{0,\dots,N\}$: the linear martingale $X_n$ gives $\mathbb{E}[X_T] = k$, and since $X_T \in \{0,N\}$, the *hitting probability* $\mathbb{P}(X_T = N) = k/N$ — the celebrated gambler's ruin formula. The quadratic martingale $X_n^2 - n$ gives $\mathbb{E}[X_T^2] - \mathbb{E}[T] = k^2$, whence the *expected hitting time* $\mathbb{E}[T] = k(N-k)$. The combination is non-obvious because nothing in "fair-game preservation under stopping" overtly mentions hitting probabilities — yet picking the right martingale and the right stopping time *computes* them. This same pattern (find the right martingale, apply optional stopping) handles every first-passage computation in the random-walk world.

The second amplification combines optional stopping with **martingale constructions on Markov chains**, identifying entrance/exit distributions and harmonic functions. For a Markov chain $(Y_n)$ on a state space $S$ and a bounded harmonic function $h : S \to \mathbb{R}$ (i.e., $h(y) = \mathbb{E}[h(Y_1)\mid Y_0 = y]$), the process $h(Y_n)$ is a martingale. Optional stopping at the exit time $T$ from a subset gives $h(y) = \mathbb{E}_y[h(Y_T)]$ — the value of any harmonic function at $y$ equals its average value on the exit distribution. This is the discrete Dirichlet principle: harmonic functions are determined by their boundary values, and the boundary distribution is exactly the exit distribution of the chain. Electrical-network identities for random walks on graphs (effective resistance, voltage as hitting probability) are direct corollaries.

The third amplification combines optional stopping with **change of measure (Doob $h$-transform) to condition Markov chains on rare events**. Given a Markov chain $(Y_n)$ and a positive harmonic function $h$ vanishing off a target set $A$, the process $M_n = h(Y_n)/h(Y_0)$ is a martingale, and the measure $d\mathbb{Q}/d\mathbb{P} = M_n$ on $\mathcal{F}_n$ defines a new Markov chain — the chain $(Y_n)$ *conditioned to hit $A$*. Optional stopping ensures the change of measure is consistent across stopping times (the [[Thm - Almost Sure Martingale Convergence|martingale property survives sampling at T]]), and the conditioned chain's transition law is the $h$-transform $p_h(x,y) = p(x,y)h(y)/h(x)$. This construction is the engine behind quasi-stationary distributions, ballot problems conditioned on the winning margin, and the rigorous theory of Brownian motion conditioned to hit a point. In each case the amplification is "OST + martingale density = legitimate conditioning on an event of positive but small probability."

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
