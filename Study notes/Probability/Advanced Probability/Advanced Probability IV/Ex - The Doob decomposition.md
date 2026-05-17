---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Martingale"
  - "Def - Filtration"
  - "Thm - Properties of Conditional Expectation"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(X_n)_{n\ge0}$ be an integrable adapted process.

**(a)** Prove the **Doob decomposition**: $X_n=X_0+M_n+A_n$, where $(M_n)$ is a [[Def - Martingale|martingale]] with $M_0=0$ and $(A_n)$ is **predictable** ($A_n$ is $\mathcal{F}_{n-1}$-measurable) with $A_0=0$ — and this decomposition is *unique*.

**(b)** Show $(X_n)$ is a submartingale iff $(A_n)$ is a.s. non-decreasing.

**(c)** Identify $A_n$ for $X_n=S_n^2$, $(S_n)$ a mean-zero variance-$\sigma^2$ random walk.

**Recall:**

[[Def - Filtration|Predictable]]: $A_n$ is $\mathcal{F}_{n-1}$-measurable. A [[Def - Martingale|martingale]] has $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]=M_n$.

---

# Convergent Strategy

**Problem class:** a structure theorem — uniquely splitting a process into a "fair" part and a "drift" part.

**Assumption pattern:** the *drift* of $X$ at step $n$ is the conditional increment $\mathbb{E}[X_{n+1}-X_n\mid\mathcal{F}_n]$ — known one step early, hence *predictable*. Subtracting the accumulated drift leaves a martingale. The construction is forced, hence unique.

---

# Legal Operations Used

1. **Extract the predictable drift** $\mathbb{E}[X_{n}-X_{n-1}\mid\mathcal{F}_{n-1}]$.
2. **Subtract it to get a martingale.**

---

# Hints

> [!note]- Hint 1
> Define $A_n-A_{n-1}=\mathbb{E}[X_n-X_{n-1}\mid\mathcal{F}_{n-1}]$ — the predictable one-step drift. Then $A_n$ is $\mathcal{F}_{n-1}$-measurable.

> [!note]- Hint 2
> $M_n=X_n-X_0-A_n$; check $\mathbb{E}[M_n-M_{n-1}\mid\mathcal{F}_{n-1}]=0$.

> [!note]- Hint 3
> (c): the drift of $S_n^2$ is $\mathbb{E}[S_n^2-S_{n-1}^2\mid\mathcal{F}_{n-1}]=\sigma^2$.

---

# Solution

**Step 1 — (a).** Define the predictable process $A$ by $A_0=0$ and
$$A_n-A_{n-1}=\mathbb{E}[X_n-X_{n-1}\mid\mathcal{F}_{n-1}],\qquad\text{so}\qquad A_n=\sum_{k=1}^n\mathbb{E}[X_k-X_{k-1}\mid\mathcal{F}_{k-1}].$$
Each summand is $\mathcal{F}_{k-1}$-measurable, so $A_n$ is $\mathcal{F}_{n-1}$-measurable — *predictable*. Set $M_n=X_n-X_0-A_n$.

> [!note]- Derivation
> *$(M_n)$ is a martingale.* $M_n-M_{n-1}=(X_n-X_{n-1})-(A_n-A_{n-1})$, so $\mathbb{E}[M_n-M_{n-1}\mid\mathcal{F}_{n-1}]=\mathbb{E}[X_n-X_{n-1}\mid\mathcal{F}_{n-1}]-(A_n-A_{n-1})=0$ (the second term is the *definition* of $A_n-A_{n-1}$, and is $\mathcal{F}_{n-1}$-measurable so [[Thm - Properties of Conditional Expectation|comes out]]). With $M_0=0$, $(M_n)$ is a martingale.
> *Uniqueness.* If $X_n-X_0=M_n+A_n=M_n'+A_n'$ are two such decompositions, then $A_n-A_n'=M_n'-M_n$ is both predictable and a martingale with value $0$ at time $0$. Taking $\mathbb{E}[\cdot\mid\mathcal{F}_{n-1}]$ of a martingale increment that is *itself $\mathcal{F}_{n-1}$-measurable* gives $A_n-A_n'=\mathbb{E}[A_n-A_n'\mid\mathcal{F}_{n-1}]=A_{n-1}-A_{n-1}'$; inductively $A_n-A_n'\equiv0$. So the decomposition is unique.

**Step 2 — (b).** The increment $A_n-A_{n-1}=\mathbb{E}[X_n-X_{n-1}\mid\mathcal{F}_{n-1}]$ is $\ge0$ a.s. *exactly when* $\mathbb{E}[X_n\mid\mathcal{F}_{n-1}]\ge X_{n-1}$ — i.e. exactly when $(X_n)$ is a [[Def - Martingale|submartingale]]. So $(X_n)$ is a submartingale iff $(A_n)$ is a.s. non-decreasing; the predictable part $A_n$ *is* the accumulated drift, and a submartingale is "a fair game plus an increasing predictable trend."

**Step 3 — (c).** For $X_n=S_n^2$: $\mathbb{E}[S_n^2-S_{n-1}^2\mid\mathcal{F}_{n-1}]=\mathbb{E}[(S_{n-1}+X_n)^2-S_{n-1}^2\mid\mathcal{F}_{n-1}]=2S_{n-1}\mathbb{E}[X_n]+\mathbb{E}[X_n^2]=\sigma^2$. So $A_n=n\sigma^2$, and the Doob decomposition is $S_n^2=(S_n^2-n\sigma^2)+n\sigma^2$ — the [[Ex - Martingales of the random walk|martingale Sₙ²-nσ²]] plus the predictable increasing $n\sigma^2$.

> [!note]- Complete formal solution
> (a) $A_n=\sum_{k\le n}\mathbb{E}[X_k-X_{k-1}\mid\mathcal{F}_{k-1}]$ is predictable; $M_n=X_n-X_0-A_n$ has $\mathbb{E}[M_n-M_{n-1}\mid\mathcal{F}_{n-1}]=0$, a martingale; uniqueness because a predictable martingale started at $0$ is $0$. (b) $A_n-A_{n-1}\ge0\iff\mathbb{E}[X_n\mid\mathcal{F}_{n-1}]\ge X_{n-1}\iff$ submartingale. (c) For $S_n^2$, the drift is $\sigma^2$ per step, so $A_n=n\sigma^2$. $\blacksquare$

---

# Key Takeaways

**Every adapted integrable process splits *uniquely* into a martingale (the "fair" fluctuation) plus a predictable process (the "drift"), and a process is a submartingale exactly when its drift is increasing.** The Doob decomposition $X_n=X_0+M_n+A_n$ isolates the *systematic trend* $A_n$ — the accumulated conditional increments, known one step in advance — from the genuinely unpredictable martingale part. It is the discrete-time prototype of the Doob–Meyer decomposition (the foundation of stochastic calculus, where $A$ becomes the "compensator" and, for $M^2$, the "quadratic variation").

**The predictable part is the *compensator* — subtracting it is what turns a biased process into a fair one.** The exemplar: $S_n^2$ has drift $\sigma^2$ per step, so its compensator is $n\sigma^2$, and $S_n^2-n\sigma^2$ is the [[Ex - Martingales of the random walk|martingale]] used in [[Ex - Gambler's ruin via optional stopping|expected-hitting-time]] computations. This "find the compensator, subtract it, get a martingale" move is how one *manufactures* martingales from non-martingale processes — the systematic technique behind martingale methods for Markov chains, branching processes, and the variance/quadratic-variation analysis of any adapted process.
