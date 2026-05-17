---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Optional Stopping Theorem"
  - "Ex - Martingales of the random walk"
tags: [probability, advanced-probability]
---

# Problem Statement

A biased random walk on $\mathbb{Z}$ takes steps $+1$ with probability $p$ and $-1$ with probability $q=1-p$, $p\neq\tfrac12$; $S_0=k$, $0<k<N$. Let $T$ be the exit time of $\{0,\dots,N\}$.

**(a)** Verify that $M_n=(q/p)^{S_n}$ is a [[Def - Martingale|martingale]].

**(b)** Use [[Thm - Optional Stopping Theorem|optional stopping]] on $M_n$ to compute the hitting probability $\mathbb{P}(S_T=N)$.

**(c)** Contrast with the *fair* case $p=\tfrac12$ — recover $\mathbb{P}(S_T=N)=k/N$ as the limit $p\to\tfrac12$.

**Recall:**

[[Thm - Optional Stopping Theorem|Optional stopping]]: $\mathbb{E}[M_T]=\mathbb{E}[M_0]$ for a martingale and a bounded-stopped-process stopping time.

---

# Convergent Strategy

**Problem class:** computing a hitting probability for a *biased* walk — the fair-case martingale $S_n$ no longer works (it has drift), so one needs the *right* martingale.

**Assumption pattern:** $S_n$ is not a martingale when $p\neq\tfrac12$; the exponential $(q/p)^{S_n}$ *is* — the ratio $q/p$ is chosen precisely so the per-step factor has mean $1$. Then optional stopping gives one linear equation, solved by the boundary values.

---

# Legal Operations Used

1. **Find the martingale** $(q/p)^{S_n}$ by tuning the base.
2. **Optional stopping** at the exit time; solve.

---

# Hints

> [!note]- Hint 1
> $\mathbb{E}[(q/p)^{X}]=p\cdot(q/p)+q\cdot(q/p)^{-1}=q+p=1$. So $(q/p)^{S_n}$ has a mean-$1$ per-step multiplier.

> [!note]- Hint 2
> Optional stopping: $\mathbb{E}[M_T]=M_0=(q/p)^k$. And $M_T\in\{(q/p)^0,(q/p)^N\}=\{1,(q/p)^N\}$.

> [!note]- Hint 3
> Solve $(q/p)^k=1\cdot\mathbb{P}(S_T=0)+(q/p)^N\mathbb{P}(S_T=N)$ with $\mathbb{P}(S_T=0)+\mathbb{P}(S_T=N)=1$.

---

# Solution

**Step 1 — (a).** Let $r=q/p$. For one step, $\mathbb{E}[r^{X_{n+1}}]=p\cdot r+q\cdot r^{-1}=p\cdot\frac qp+q\cdot\frac pq=q+p=1$. Since $S_{n+1}=S_n+X_{n+1}$, $X_{n+1}\perp\mathcal{F}_n$, and $r^{S_n}$ is $\mathcal{F}_n$-measurable,
$$\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]=\mathbb{E}[r^{S_n}r^{X_{n+1}}\mid\mathcal{F}_n]=r^{S_n}\,\mathbb{E}[r^{X_{n+1}}]=r^{S_n}\cdot1=M_n.$$
So $M_n=(q/p)^{S_n}$ is a martingale — the base $q/p$ is *exactly* the value making the multiplier fair.

**Step 2 — (b).** $T$ is a.s. finite and the stopped $M_{T\wedge n}$ is bounded ($S$ confined to $[0,N]$, so $M\in[\min(1,r^N),\max(1,r^N)]$). By [[Thm - Optional Stopping Theorem|optional stopping]], $\mathbb{E}[M_T]=M_0=r^k$. Since $S_T\in\{0,N\}$, $M_T\in\{r^0,r^N\}=\{1,r^N\}$, so with $\pi:=\mathbb{P}(S_T=N)$,
$$r^k=\mathbb{E}[M_T]=1\cdot(1-\pi)+r^N\cdot\pi\quad\Longrightarrow\quad\boxed{\ \mathbb{P}(S_T=N)=\dfrac{r^k-1}{r^N-1}=\dfrac{(q/p)^k-1}{(q/p)^N-1}\ }.$$

**Step 3 — (c).** As $p\to\tfrac12$, $r=q/p\to1$; writing $r=1+\varepsilon$, $\frac{r^k-1}{r^N-1}=\frac{k\varepsilon+O(\varepsilon^2)}{N\varepsilon+O(\varepsilon^2)}\to\frac kN$. So the biased formula degenerates continuously to the fair-walk answer $\mathbb{P}(S_T=N)=k/N$ ([[Ex - Gambler's ruin via optional stopping|gambler's ruin]]) — consistent, since for $p=\tfrac12$ the martingale $(q/p)^{S_n}$ collapses to the constant $1$ and one uses $S_n$ instead.

> [!note]- Complete formal solution
> (a) $\mathbb{E}[(q/p)^X]=p(q/p)+q(p/q)=q+p=1$, so $(q/p)^{S_n}$ is a martingale by independence. (b) Optional stopping: $(q/p)^k=\mathbb{E}[M_T]=(1-\pi)+(q/p)^N\pi$, giving $\pi=\frac{(q/p)^k-1}{(q/p)^N-1}$. (c) As $p\to\tfrac12$, $q/p\to1$ and the ratio $\to k/N$. $\blacksquare$

---

# Key Takeaways

**For a biased walk the fair-case martingale $S_n$ fails — it has drift — and one must *find the right martingale*, here the exponential $(q/p)^{S_n}$ with the base tuned to make the per-step multiplier mean-$1$.** This is the recurring move in martingale methods: the process at hand is not a martingale, so one *manufactures* one (an exponential martingale, a [[Ex - The Doob decomposition|compensated]] process) on which [[Thm - Optional Stopping Theorem|optional stopping]] can act. The base $q/p$ is not guessed — it is the root of $\mathbb{E}[r^X]=1$, the "Cramér root" that also governs the exponential change of measure and large-deviation rates.

**Optional stopping plus the boundary values turns one martingale identity into the hitting probability — and the biased and fair formulas connect continuously.** $\mathbb{E}[M_T]=M_0$ is a single equation; because $S_T$ takes only the two boundary values, it *determines* $\mathbb{P}(S_T=N)$. The biased answer $\frac{(q/p)^k-1}{(q/p)^N-1}$ degenerates to the fair $k/N$ as $p\to\tfrac12$ — and the exponential nature of the biased formula (a slight drift makes escape probabilities decay *geometrically* in distance) is the qualitative signature of bias, the same exponential that reappears in queueing, ruin theory, and the Chernoff/large-deviation bound.
