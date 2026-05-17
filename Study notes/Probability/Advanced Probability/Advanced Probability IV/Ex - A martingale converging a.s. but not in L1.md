---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Almost Sure Martingale Convergence"
  - "Thm - Lp and L1 Martingale Convergence"
  - "Def - Uniform Integrability"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(Y_k)$ be i.i.d. with $\mathbb{P}(Y_k=0)=\mathbb{P}(Y_k=2)=\tfrac12$, and $X_n=\prod_{k=1}^n Y_k$ ($X_0=1$), with $\mathcal{F}_n=\sigma(Y_1,\dots,Y_n)$.

**(a)** Show $(X_n)$ is a non-negative [[Def - Martingale|martingale]] with $\mathbb{E}[X_n]=1$ for all $n$.

**(b)** Show $X_n\to0$ almost surely.

**(c)** Conclude $(X_n)$ converges a.s. but **not** in $L^1$, and identify the failed hypothesis.

**Recall:**

[[Thm - Almost Sure Martingale Convergence|A.s. convergence]]: an $L^1$-bounded martingale converges a.s. [[Thm - Lp and L1 Martingale Convergence|L¹-convergence]] needs [[Def - Uniform Integrability|uniform integrability]].

---

# Convergent Strategy

**Problem class:** the canonical example separating a.s. convergence from $L^1$-convergence for martingales.

**Assumption pattern:** $(X_n)$ is non-negative with constant expectation $1$ — so $L^1$-bounded, hence a.s. convergent. But once a single $Y_k=0$, the product is $0$ forever; this happens a.s., so the limit is $0$ — and $\mathbb{E}[0]=0\neq1$. Mass escapes; UI fails.

---

# Legal Operations Used

1. **Verify the martingale property** via independence.
2. **Borel–Cantelli / absorption at $0$** for the a.s. limit.
3. **Compare $\mathbb{E}[\lim]$ with $\lim\mathbb{E}$** to detect non-UI.

---

# Hints

> [!note]- Hint 1
> $X_{n+1}=X_nY_{n+1}$; $\mathbb{E}[Y_{n+1}]=\tfrac12\cdot0+\tfrac12\cdot2=1$.

> [!note]- Hint 2
> Once some $Y_k=0$, all later $X_n=0$. $\mathbb{P}(\text{some }Y_k=0\text{ eventually})=1$.

> [!note]- Hint 3
> $\mathbb{E}[X_n]=1$ for all $n$, but $\mathbb{E}[\lim X_n]=\mathbb{E}[0]=0$.

---

# Solution

**Step 1 — (a).** $X_n\ge0$, adapted, integrable. Since $Y_{n+1}\perp\mathcal{F}_n$ and $X_n$ is $\mathcal{F}_n$-measurable,
$$\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=\mathbb{E}[X_nY_{n+1}\mid\mathcal{F}_n]=X_n\,\mathbb{E}[Y_{n+1}]=X_n\cdot1=X_n.$$
So $(X_n)$ is a martingale, and $\mathbb{E}[X_n]=\mathbb{E}[X_0]=1$ for every $n$ — it is non-negative and $L^1$-bounded.

**Step 2 — (b).** The product $X_n=\prod_{k\le n}Y_k$ is *absorbed at $0$*: if any factor $Y_k=0$, then $X_m=0$ for all $m\ge k$. The event "no $Y_k$ ever equals $0$" is $\bigcap_k\{Y_k\neq0\}$, with probability $\prod_k\mathbb{P}(Y_k\neq0)=\prod_k\tfrac12=0$. So almost surely some $Y_k=0$, and from then on $X_n=0$:
$$X_n\xrightarrow{\text{a.s.}}0.$$
(Consistent with the [[Thm - Almost Sure Martingale Convergence|a.s. convergence theorem]]: an $L^1$-bounded martingale converges a.s.)

**Step 3 — (c).** The limit is $X_\infty=0$ a.s., so $\mathbb{E}[X_\infty]=0$. But $\mathbb{E}[X_n]=1$ for every $n$, so $\mathbb{E}[X_n]=1\not\to0=\mathbb{E}[X_\infty]$ — in particular $\mathbb{E}|X_n-X_\infty|=\mathbb{E}[X_n]=1\not\to0$: **$(X_n)$ does not converge in $L^1$**. The failed hypothesis of the [[Thm - Lp and L1 Martingale Convergence|L¹-convergence theorem]] is *uniform integrability*: $(X_n)$ is $L^1$-bounded but not UI. (Indeed $X_n$ takes the value $2^n$ with probability $2^{-n}$ — a tall, rare spike — so $\mathbb{E}[X_n\mathbf{1}_{X_n>M}]=1$ for all $n$ with $2^n>M$; mass concentrates and escapes.)

> [!note]- Complete formal solution
> (a) $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n\mathbb{E}[Y_{n+1}]=X_n$; $\mathbb{E}[X_n]=1$, non-negative, $L^1$-bounded. (b) $X_n$ is absorbed at $0$ once any $Y_k=0$, and $\mathbb{P}(\text{no }Y_k=0)=\prod\tfrac12=0$, so $X_n\to0$ a.s. (c) $\mathbb{E}[X_n]=1\not\to0=\mathbb{E}[X_\infty]$, so no $L^1$-convergence; $(X_n)$ is $L^1$-bounded but not UI (the spike $2^n$ at probability $2^{-n}$). $\blacksquare$

---

# Key Takeaways

**The martingale convergence theorem gives *only* almost-sure convergence — $L^1$-convergence is a strictly stronger conclusion needing uniform integrability.** This product martingale is the canonical witness: non-negative, constant expectation $1$, hence $L^1$-bounded and a.s.-convergent — but it converges a.s. to $0$, while $\mathbb{E}[X_n]\equiv1$. The expectation does *not* survive the limit, so there is no $L^1$-convergence. The lesson: after invoking [[Thm - Almost Sure Martingale Convergence|a.s. martingale convergence]], one has a pointwise limit but *cannot* conclude $\mathbb{E}[X_n]\to\mathbb{E}[X_\infty]$ — that requires separately checking [[Def - Uniform Integrability|uniform integrability]] (or $L^p$-boundedness, $p>1$).

**The failure is escape of mass through a tall, rare spike — $X_n=2^n$ with probability $2^{-n}$.** $L^1$-boundedness controls only *average* mass; it cannot prevent that mass concentrating into an ever-taller, ever-rarer spike that vanishes pointwise yet keeps $\mathbb{E}[X_n]=1$. Uniform integrability is precisely the no-spike condition. This is the same escape mechanism as the [[Ex - Optional stopping fails for unbounded times|doubling strategy]] and every failed limit–integral interchange — and it is why the [[Thm - Lp and L1 Martingale Convergence|L¹ martingale convergence theorem]] identifies the *uniformly integrable* martingales as exactly the well-behaved (closed) ones.
