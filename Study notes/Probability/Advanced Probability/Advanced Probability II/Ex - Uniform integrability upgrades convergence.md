---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Uniform Integrability"
  - "Def - Modes of Convergence"
  - "Thm - Vitali Convergence Theorem"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** Show that if $X_n\xrightarrow{\mathbb{P}}X$ and $(X_n)$ is [[Def - Uniform Integrability|uniformly integrable]], then $X_n\xrightarrow{L^1}X$ — in particular $\mathbb{E}[X_n]\to\mathbb{E}[X]$.

**(b)** Show that an $L^1$-bounded sequence need *not* satisfy $\mathbb{E}[X_n]\to\mathbb{E}[X]$ even when $X_n\to X$ a.s. — uniform integrability cannot be dropped.

**(c)** Show that $L^2$-boundedness ($\sup_n\mathbb{E}X_n^2<\infty$) *does* suffice.

**Recall:**

![[Thm - Vitali Convergence Theorem#Formal Statement]]

A family is [[Def - Uniform Integrability|uniformly integrable]] if $\sup_n\mathbb{E}[|X_n|\mathbf{1}_{|X_n|>M}]\to0$ as $M\to\infty$.

---

# Convergent Strategy

**Problem class:** identifying the exact hypothesis that upgrades convergence in probability to $L^1$ — and hence licenses $\lim\mathbb{E}=\mathbb{E}\lim$.

**Assumption pattern:** convergence in probability + uniform integrability is *exactly* $L^1$-convergence ([[Thm - Vitali Convergence Theorem|Vitali]]). The probability space being finite, $L^p$-boundedness for $p>1$ supplies UI for free.

---

# Legal Operations Used

1. **Vitali convergence theorem** on the probability space.
2. **$L^p$-boundedness ($p>1$) $\Rightarrow$ UI.**
3. **Escape-of-mass counterexample.**

---

# Hints

> [!note]- Hint 1
> $(\Omega,\mathcal{F},\mathbb{P})$ has finite measure. [[Thm - Vitali Convergence Theorem|Vitali]]: $L^1$-convergence $\iff$ convergence in measure $+$ UI.

> [!note]- Hint 2
> (b): the spike $X_n=n\mathbf{1}_{[0,1/n]}$ is $L^1$-bounded ($\mathbb{E}X_n=1$) but not UI.

> [!note]- Hint 3
> (c): $L^2$-bounded $\Rightarrow$ UI by the [[Ex - Lp boundedness implies uniform integrability|μ(A)¹ᐟq estimate]].

---

# Solution

**Step 1 — (a).** The probability space is finite ($\mathbb{P}(\Omega)=1$), [[Def - Modes of Convergence|convergence in probability]] is [[Def - Convergence in Measure|convergence in measure]], and $(X_n)$ is uniformly integrable. By the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]], $X_n\xrightarrow{L^1}X$, i.e. $\mathbb{E}|X_n-X|\to0$. Then $|\mathbb{E}X_n-\mathbb{E}X|\le\mathbb{E}|X_n-X|\to0$, so $\mathbb{E}[X_n]\to\mathbb{E}[X]$.

**Step 2 — (b).** On $([0,1],\lambda)$, $X_n=n\mathbf{1}_{[0,1/n]}$ has $X_n\to0$ a.s. (hence in probability) and $\mathbb{E}X_n=n\cdot\tfrac1n=1$ for all $n$ — so $\mathbb{E}X_n=1\not\to0=\mathbb{E}[0]$. The sequence is $L^1$-bounded ($\sup\mathbb{E}|X_n|=1$) but **not** uniformly integrable: $\mathbb{E}[X_n\mathbf{1}_{X_n>M}]=1$ for every $n>M$. So $L^1$-boundedness alone fails to give $\lim\mathbb{E}=\mathbb{E}\lim$; UI is indispensable.

**Step 3 — (c).** If $\sup_n\mathbb{E}X_n^2<\infty$, then $(X_n)$ is bounded in $L^2$, hence — by the [[Ex - Lp boundedness implies uniform integrability|Hölder estimate]] $\mathbb{E}[|X_n|\mathbf{1}_A]\le\|X_n\|_2\,\mathbb{P}(A)^{1/2}$ — uniformly integrable. By (a), convergence in probability then upgrades to $L^1$, and $\mathbb{E}X_n\to\mathbb{E}X$. ($L^p$-boundedness for *any* $p>1$ works identically.)

> [!note]- Complete formal solution
> (a) On the finite space, convergence in probability $+$ UI $\Rightarrow$ ([[Thm - Vitali Convergence Theorem|Vitali]]) $L^1$-convergence, whence $\mathbb{E}X_n\to\mathbb{E}X$. (b) $n\mathbf{1}_{[0,1/n]}\to0$ a.s., $L^1$-bounded, not UI, $\mathbb{E}X_n=1\not\to0$. (c) $L^2$-bounded $\Rightarrow$ UI (Hölder), so (a) applies. $\blacksquare$

---

# Key Takeaways

**Uniform integrability is the precise condition upgrading convergence in probability (or a.s.) to convergence in $L^1$ — and hence licensing $\lim\mathbb{E}[X_n]=\mathbb{E}[\lim X_n]$.** By the [[Thm - Vitali Convergence Theorem|Vitali theorem]], "in probability $+$ UI" is *equivalent* to $L^1$-convergence — UI is not a sufficient technicality but the exact missing ingredient. Whenever a proof has pointwise or in-probability convergence and *wants* convergence of expectations, the question to ask is: *is the sequence uniformly integrable?*

**$L^1$-boundedness is never enough — mass can escape — but $L^p$-boundedness for any $p>1$ is.** The escaping spike is $L^1$-bounded yet loses its mass in the limit; the *extra* integrability of $p>1$ forbids the concentration, supplying UI by a one-line Hölder estimate. This $p>1$ threshold recurs throughout: it is why [[Thm - Almost Sure Martingale Convergence|Lᵖ-bounded martingales]] ($p>1$) converge in $L^p$ automatically while $L^1$-bounded ones need UI bolted on, and why finite *variance* (an $L^2$ condition) makes the [[Thm - Weak Law of Large Numbers|weak law]] and many estimates effortless.
