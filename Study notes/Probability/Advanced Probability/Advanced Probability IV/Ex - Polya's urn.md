---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Martingale"
  - "Thm - Almost Sure Martingale Convergence"
  - "Thm - Lp and L1 Martingale Convergence"
tags: [probability, advanced-probability]
---

# Problem Statement

An urn starts with one red and one black ball. At each step a ball is drawn uniformly at random and returned together with a new ball of the *same* colour. Let $R_n$ be the number of red balls after $n$ steps (so $n+2$ balls total) and $X_n=R_n/(n+2)$ the red *fraction*.

**(a)** Show $(X_n)$ is a [[Def - Martingale|martingale]].

**(b)** Conclude $X_n$ converges almost surely and in $L^1$ to a limit $X_\infty$.

**(c)** State (it can be shown) that $X_\infty$ is **uniform on $[0,1]$** — the limiting red fraction is *random*, not deterministic.

**Recall:**

[[Thm - Almost Sure Martingale Convergence|A.s. convergence]]: a bounded martingale converges a.s. [[Thm - Lp and L1 Martingale Convergence|L¹-convergence]]: under uniform integrability.

---

# Convergent Strategy

**Problem class:** recognising a self-reinforcing process as a *bounded* martingale, hence convergent.

**Assumption pattern:** the red fraction $X_n\in[0,1]$ — *bounded*, hence trivially [[Def - Uniform Integrability|uniformly integrable]] and $L^1$-bounded. So both convergence theorems apply once the martingale property is checked.

---

# Legal Operations Used

1. **Check the martingale property** by conditioning on the current composition.
2. **Bounded $\Rightarrow$ UI $\Rightarrow$ a.s. and $L^1$ convergence.**

---

# Hints

> [!note]- Hint 1
> Given $R_n=r$ (so $X_n=r/(n+2)$), the next draw is red with probability $r/(n+2)=X_n$. Compute $\mathbb{E}[R_{n+1}\mid\mathcal{F}_n]$.

> [!note]- Hint 2
> $R_{n+1}=R_n+1$ w.p. $X_n$, else $R_n$. So $\mathbb{E}[R_{n+1}\mid\mathcal{F}_n]=R_n+X_n$. Divide by $n+3$.

> [!note]- Hint 3
> $X_n\in[0,1]$ — bounded. Which convergence theorems apply for free?

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) computes $\mathbb{E}[R_{n+1} \mid \mathcal{F}_n] = R_n + X_n = R_n \cdot \frac{n+3}{n+2}$ by conditioning on the urn composition, then divides by the new total to read off $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$; Step 2 (part b) uses $X_n \in [0, 1]$ to invoke both convergence theorems simultaneously — bounded $\Rightarrow$ $L^1$-bounded (a.s. convergence) *and* UI ($L^1$-convergence); Step 3 (part c) states the additional Beta-Binomial computation showing $X_\infty \sim \text{Uniform}[0, 1]$. The non-obvious move is in Step 1 — taking the martingale to be the *fraction* (not the count) is what works, because the fraction is conserved in conditional mean even as the count grows.

**Step 1 — (a).** Condition on $\mathcal{F}_n$ (the history through step $n$); the urn has $R_n$ red of $n+2$ balls, so the next draw is red with probability $X_n=R_n/(n+2)$. Thus $R_{n+1}=R_n+1$ with probability $X_n$ and $R_{n+1}=R_n$ otherwise:
$$\mathbb{E}[R_{n+1}\mid\mathcal{F}_n]=(R_n+1)\,X_n+R_n\,(1-X_n)=R_n+X_n=R_n+\frac{R_n}{n+2}=R_n\cdot\frac{n+3}{n+2}.$$
Dividing by the new total $n+3$:
$$\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=\frac{\mathbb{E}[R_{n+1}\mid\mathcal{F}_n]}{n+3}=\frac{R_n}{n+2}=X_n.$$
So the red fraction $(X_n)$ is a martingale — the *fraction* is conserved in conditional mean even though the *count* grows.

**Step 2 — (b).** $X_n=R_n/(n+2)\in[0,1]$ is bounded. A bounded martingale is $L^1$-bounded, so by the [[Thm - Almost Sure Martingale Convergence|a.s. convergence theorem]] $X_n\to X_\infty$ almost surely. It is also bounded hence [[Def - Uniform Integrability|uniformly integrable]], so by the [[Thm - Lp and L1 Martingale Convergence|L¹-convergence theorem]] the convergence is also in $L^1$ — and indeed in every $L^p$. In particular $\mathbb{E}[X_\infty]=\lim\mathbb{E}[X_n]=\mathbb{E}[X_0]=\tfrac12$.

**Step 3 — (c).** A direct computation of the distribution of $R_n$ (a Beta–Binomial / exchangeability argument) shows $R_n-1$ is uniform on $\{0,1,\dots,n\}$, so $X_n$ is uniform on a grid in $[0,1]$, and in the limit $X_\infty\sim\text{Uniform}[0,1]$. The striking conclusion: **the limiting red fraction is genuinely random** — it converges, with probability one, but the value it converges to is uniformly spread over $[0,1]$. Early draws "lock in" a random proportion. (This is consistent with $\mathbb{E}[X_\infty]=\tfrac12$ — the *mean* of the limit is the start, but the limit itself is far from deterministic.)

> [!note]- Complete formal solution
> (a) $\mathbb{E}[R_{n+1}\mid\mathcal{F}_n]=R_n+X_n=R_n\frac{n+3}{n+2}$, so $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=R_n/(n+2)=X_n$ — a martingale. (b) $X_n\in[0,1]$ bounded $\Rightarrow$ $L^1$-bounded and UI $\Rightarrow$ a.s. and $L^1$ convergence to $X_\infty$, $\mathbb{E}X_\infty=\tfrac12$. (c) $R_n-1$ is uniform on $\{0,\dots,n\}$, so $X_\infty\sim\text{Uniform}[0,1]$. $\blacksquare$

---

# Key Takeaways

**Pólya's urn is the model example of a *bounded* martingale: the red fraction is conserved in conditional mean, lies in $[0,1]$, hence converges both almost surely and in $L^1$.** Recognising the right quantity — the *fraction*, not the *count* — as a martingale is the key step; the count $R_n$ grows, but the proportion is a fair game. Once a bounded martingale is in hand, *both* convergence theorems apply with no further work: boundedness gives $L^1$-boundedness (a.s. convergence) and [[Def - Uniform Integrability|uniform integrability]] (the $L^1$/$L^p$ upgrade) simultaneously.

**The limit is *random* — convergence does not mean convergence to a constant.** Pólya's urn converges a.s. to $X_\infty\sim\text{Uniform}[0,1]$: the proportion settles down, but *to a random value*, because early draws self-reinforce ("rich get richer"). This is the qualitative opposite of the [[Thm - Strong Law of Large Numbers|strong law]] — there the [[Thm - Kolmogorov 0-1 Law|0–1 law]] forces the limit to be a *constant* (the steps are independent, the limit is a tail variable); here the steps are *dependent*, $X_\infty$ is *not* tail-measurable, and a non-degenerate limit law is exactly what one should expect. Martingale convergence guarantees a limit *exists*; whether it is deterministic depends on the dependence structure.
