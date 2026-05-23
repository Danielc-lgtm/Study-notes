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

A gambler starts with $k$ pounds and bets £1 on fair coin tosses, stopping on reaching either $0$ (ruin) or $N$ (target), $0<k<N$. Let $S_n$ be the fortune, $T=\inf\{n:S_n\in\{0,N\}\}$ the exit time.

**(a)** Compute the **ruin probability** $\mathbb{P}(S_T=N)$ (reaching the target before ruin).

**(b)** Compute the **expected duration** $\mathbb{E}[T]$.

**Recall:**

[[Thm - Optional Stopping Theorem|Optional stopping]]: $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ for a martingale and a bounded stopping time (here $T$ is a.s. finite with $S_n^T$ bounded — the UI form applies).

---

# Convergent Strategy

**Problem class:** computing a hitting probability and an expected hitting time by applying [[Thm - Optional Stopping Theorem|optional stopping]] to the *right* martingale.

**Assumption pattern:** $T$ is the exit time of a bounded interval — a.s. finite, and the stopped fortune $S_n^T$ is bounded (in $[0,N]$), so the [[Thm - Optional Stopping Theorem|optional stopping theorem]] applies. Two [[Def - Martingale|martingales]] of the [[Ex - Martingales of the random walk|random walk]] give two equations: $S_n$ for the probability, $S_n^2-n$ for the time.

---

# Legal Operations Used

1. **Apply optional stopping** to $S_n$ and to $S_n^2-n$ at $T$.
2. **Solve the resulting linear equations.**

---

# Hints

> [!note]- Hint 1
> $T<\infty$ a.s. and $0\le S_n^T\le N$ — bounded, so optional stopping gives $\mathbb{E}[S_T]=\mathbb{E}[S_0]=k$.

> [!note]- Hint 2
> $S_T\in\{0,N\}$, so $\mathbb{E}[S_T]=N\,\mathbb{P}(S_T=N)$.

> [!note]- Hint 3
> $S_n^2-n$ is a martingale ($\sigma^2=1$); optional stopping gives $\mathbb{E}[S_T^2]-\mathbb{E}[T]=\mathbb{E}[S_0^2]=k^2$.

---

# Solution

The proof breaks into two steps. Step 1 (part a) applies optional stopping to the martingale $S_n$ at the bounded exit time $T$: $\mathbb{E}[S_T] = k$, and since $S_T \in \{0, N\}$, this single equation gives $\mathbb{P}(S_T = N) = k/N$; Step 2 (part b) applies optional stopping to the compensated martingale $S_n^2 - n$ to get $\mathbb{E}[S_T^2] - \mathbb{E}[T] = k^2$, then substitutes $\mathbb{E}[S_T^2] = N^2 \cdot (k/N) = Nk$ to read off $\mathbb{E}[T] = k(N-k)$. The non-obvious move is the *pair* of martingales — $S_n$ supplies one equation that pins the hitting probability, and $S_n^2 - n$ supplies a second equation that, *after the probability is known*, pins the expected hitting time.

**Step 1 — (a) Ruin probability.** $T$ is a.s. finite (the walk a.s. exits a bounded interval), and the stopped fortune $S_{T\wedge n}\in[0,N]$ is bounded — so the [[Thm - Optional Stopping Theorem|optional stopping theorem]] applies to the martingale $(S_n)$:
$$\mathbb{E}[S_T]=\mathbb{E}[S_0]=k.$$
But $S_T\in\{0,N\}$, so $\mathbb{E}[S_T]=0\cdot\mathbb{P}(S_T=0)+N\cdot\mathbb{P}(S_T=N)=N\,\mathbb{P}(S_T=N)$. Equating,
$$\mathbb{P}(S_T=N)=\frac{k}{N},\qquad\mathbb{P}(S_T=0)=1-\frac kN.$$
The probability of reaching the target is the starting fraction of the way there.

**Step 2 — (b) Expected duration.** $(S_n^2-n)$ is a martingale ([[Ex - Martingales of the random walk|with σ²=1]]), and again the stopped process is bounded ($S_{T\wedge n}^2\le N^2$, and $T\wedge n\le n$; uniform integrability holds since $T\in L^1$ — itself a consequence below — but one applies optional stopping to $S_{T\wedge n}^2-(T\wedge n)$ and lets $n\to\infty$ by monotone convergence on $T\wedge n\uparrow T$). This gives
$$\mathbb{E}[S_T^2]-\mathbb{E}[T]=\mathbb{E}[S_0^2]=k^2.$$
Now $\mathbb{E}[S_T^2]=0^2\cdot\mathbb{P}(S_T=0)+N^2\cdot\mathbb{P}(S_T=N)=N^2\cdot\frac kN=Nk$. So
$$\mathbb{E}[T]=\mathbb{E}[S_T^2]-k^2=Nk-k^2=k(N-k).$$
The expected duration is the product of the two distances to the boundaries.

> [!note]- Complete formal solution
> (a) $(S_n)$ martingale, $T$ exit time of $[0,N]$ with bounded stopped process; optional stopping: $k=\mathbb{E}[S_T]=N\mathbb{P}(S_T=N)$, so $\mathbb{P}(S_T=N)=k/N$. (b) $(S_n^2-n)$ martingale; optional stopping: $k^2=\mathbb{E}[S_T^2]-\mathbb{E}[T]=Nk-\mathbb{E}[T]$, so $\mathbb{E}[T]=k(N-k)$. $\blacksquare$

---

# Key Takeaways

**Optional stopping computes hitting probabilities and expected hitting times by applying it to the right martingale of the random walk.** The fortune $S_n$ at the exit time gives one linear equation — $\mathbb{E}[S_T]=k$ — and since $S_T$ takes only the boundary values $\{0,N\}$, that equation *solves for the hitting probability*: $\mathbb{P}(\text{target})=k/N$. The compensated square $S_n^2-n$ gives a second equation that, once the probability is known, *solves for the expected time*: $\mathbb{E}[T]=k(N-k)$. This "apply optional stopping to $S_n$ for the probability, to $S_n^2-n\sigma^2$ for the time" is the standard two-step for any boundary-hitting problem.

**The hypothesis that makes this rigorous — and rules out the gambler's fallacy — is the boundedness of the stopped process.** The exit time $T$ of a *bounded* interval has the stopped fortune confined to $[0,N]$, so [[Thm - Optional Stopping Theorem|optional stopping]] genuinely applies. Drop the upper barrier $N$ and the story changes: the first-passage time to a *single* level has $\mathbb{E}[S_T]\neq\mathbb{E}[S_0]$ ([[Ex - Optional stopping fails for unbounded times|optional stopping fails]]) — there is no winning quitting rule. The bounded-barrier setting is exactly where the theorem bites, and the answers $k/N$ and $k(N-k)$ are the canonical illustration of "fair game $+$ non-anticipating stopping $=$ no edge."
