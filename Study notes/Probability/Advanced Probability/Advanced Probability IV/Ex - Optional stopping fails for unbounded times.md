---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Optional Stopping Theorem"
  - "Def - Uniform Integrability"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(S_n)$ be a simple symmetric random walk, $S_0=0$, and $T=\inf\{n:S_n=1\}$ the first hitting time of level $1$.

**(a)** Show $T<\infty$ almost surely, yet $\mathbb{E}[S_T]=1\neq0=\mathbb{E}[S_0]$ — the [[Thm - Optional Stopping Theorem|optional stopping]] conclusion *fails*.

**(b)** Identify which hypothesis of optional stopping is violated: show $(S_{T\wedge n})$ is not [[Def - Uniform Integrability|uniformly integrable]].

**(c)** State the moral: a fair game *can* be beaten by an unbounded quitting rule — but only at the cost of unbounded losses along the way.

**Recall:**

[[Thm - Optional Stopping Theorem|Optional stopping]] needs $T$ **bounded**, or $T<\infty$ a.s. with $(S_{T\wedge n})$ **uniformly integrable**.

---

# Convergent Strategy

**Problem class:** a counterexample exposing the necessity of the boundedness / UI hypothesis in optional stopping.

**Assumption pattern:** the recurrence of simple random walk makes $T<\infty$ a.s.; but the walk wanders arbitrarily far *negative* before hitting $1$, so the stopped process is unbounded below and *not* UI — exactly the hypothesis optional stopping needs and this $T$ lacks.

---

# Legal Operations Used

1. **Recurrence** of simple random walk ($T<\infty$ a.s.).
2. **Negate uniform integrability** of the stopped process.

---

# Hints

> [!note]- Hint 1
> Simple symmetric random walk is recurrent — it hits every level a.s. So $S_T=1$ on $\{T<\infty\}$, and $\mathbb{P}(T<\infty)=1$.

> [!note]- Hint 2
> $\mathbb{E}[S_{T\wedge n}]=\mathbb{E}[S_0]=0$ for every $n$ ([[Thm - Optional Stopping Theorem|stopped process is a martingale]]) — yet $S_{T\wedge n}\to S_T=1$. The limit of the expectations is not the expectation of the limit.

> [!note]- Hint 3
> Before hitting $1$, the walk dips to $\inf_{k\le T}S_k=-\infty$ with positive... in fact the minimum is a.s. finite but has infinite expectation; $\mathbb{E}[\inf_{k}S_{T\wedge k}^-]=\infty$.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) uses recurrence of simple random walk to deduce $T < \infty$ a.s. with $S_T = 1$, then observes $\mathbb{E}[S_T] = 1 \neq 0 = \mathbb{E}[S_0]$; Step 2 (part b) identifies the broken hypothesis as uniform integrability of $(S_{T \wedge n})$ — the stopped martingale has $\mathbb{E}[S_{T\wedge n}] = 0$ for all $n$ but $S_{T\wedge n} \to 1$, so mass escapes via the unbounded pre-$T$ minimum; Step 3 (part c) extracts the moral that fair games can be beaten only with unbounded resources. The non-obvious move is in Step 2 — recognising that "limit of expectations ≠ expectation of limit" is *exactly* a failure of uniform integrability, which is the missing hypothesis of optional stopping.

**Step 1 — (a).** Simple symmetric random walk on $\mathbb{Z}$ is *recurrent*: it visits every integer infinitely often a.s. In particular it a.s. reaches level $1$, so $T<\infty$ almost surely and $S_T=1$. Hence $\mathbb{E}[S_T]=1$. But $\mathbb{E}[S_0]=0$. So $\mathbb{E}[S_T]=1\neq0=\mathbb{E}[S_0]$ — the [[Thm - Optional Stopping Theorem|optional stopping]] identity *fails* for this (a.s. finite, but unbounded) stopping time.

**Step 2 — (b).** No contradiction: optional stopping requires $T$ *bounded*, or $(S_{T\wedge n})$ *uniformly integrable* — and here neither holds. The stopped process *is* a martingale, so $\mathbb{E}[S_{T\wedge n}]=0$ for every $n$, and $S_{T\wedge n}\to S_T=1$ a.s.; the failure $\mathbb{E}[\lim]\neq\lim\mathbb{E}$ is exactly a failure of uniform integrability.

> [!note]- Derivation
> Concretely, $(S_{T\wedge n})$ is *not* UI. Before hitting $+1$, the walk must, with substantial probability, descend to arbitrarily negative levels — $\inf_{k\le T}S_k$ is a.s. finite but heavy-tailed, with $\mathbb{E}[|\inf_{k\le T}S_k|]=\infty$ (it has the same distribution, up to sign, as $T^{1/2}$-scale fluctuations, and $\mathbb{E}[T]=\infty$). So $\sup_n\mathbb{E}[|S_{T\wedge n}|\mathbf{1}_{|S_{T\wedge n}|>M}]\not\to0$: mass at large negative values is never uniformly small. The stopped martingale carries its "fortune" through unboundedly large excursions, and that is precisely the escape of mass UI forbids.

**Step 3 — (c) Moral.** A fair game *can* be "beaten" by the unbounded rule "play until you are £1 ahead, then quit" — it succeeds with probability $1$. But this is no contradiction of fairness: the strategy requires being prepared to fall *arbitrarily* far behind first ($\mathbb{E}[T]=\infty$, unbounded losses en route). The boundedness / UI hypothesis of [[Thm - Optional Stopping Theorem|optional stopping]] is exactly the prohibition of such "double-or-nothing" schemes. *You cannot beat a fair game with bounded resources.*

> [!note]- Complete formal solution
> (a) Recurrence $\Rightarrow T<\infty$ a.s., $S_T=1$, so $\mathbb{E}[S_T]=1\neq0=\mathbb{E}[S_0]$. (b) $(S_{T\wedge n})$ is a martingale with $\mathbb{E}[S_{T\wedge n}]=0$ but $S_{T\wedge n}\to1$ a.s.; the discrepancy is non-uniform-integrability — the walk's pre-$T$ minimum has infinite expectation, so mass at large negative values is not uniformly controlled. (c) Optional stopping's boundedness/UI hypothesis forbids exactly such unbounded-resource strategies. $\blacksquare$

---

# Key Takeaways

**Optional stopping genuinely needs its boundedness / uniform-integrability hypothesis — drop it and a fair game *can* be beaten.** The first-passage time of a simple random walk to level $1$ is a.s. finite, yet $\mathbb{E}[S_T]=1\neq0$: the conclusion $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ fails outright. There is no paradox — the stopped process $(S_{T\wedge n})$ is a martingale ($\mathbb{E}[S_{T\wedge n}]=0$ always), but it is *not* uniformly integrable, so $\lim\mathbb{E}[S_{T\wedge n}]\neq\mathbb{E}[\lim S_{T\wedge n}]$. This is the standard cautionary example, and the lesson is to *always check boundedness or UI before invoking optional stopping*.

**The mechanism of failure is escape of mass — the same mechanism behind every failed limit–integral interchange.** The "buy until £1 ahead" strategy works only because it tolerates unbounded losses first ($\mathbb{E}[T]=\infty$, the pre-$T$ minimum has infinite expectation). Uniform integrability is the no-escape condition; without it the [[Thm - Vitali Convergence Theorem|Vitali]] upgrade from a.s. to $L^1$ convergence is unavailable, and $\mathbb{E}[S_{T\wedge n}]\to0$ does not transmit to $\mathbb{E}[S_T]$. "You cannot beat a fair game" is true *for bounded resources*; the doubling strategy is the eternal reminder that the resource bound is not optional.
