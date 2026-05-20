---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Fubini-Tonelli Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

**(a)** On $X=Y=\mathbb{N}$ with counting measure, define $f(n,m)=1$ if $n=m$, $f(n,m)=-1$ if $n=m+1$, and $0$ otherwise. Compute the two iterated sums $\sum_n\sum_m f$ and $\sum_m\sum_n f$ and show they *differ*.

**(b)** Explain precisely which hypothesis of [[Thm - Fubini-Tonelli Theorem|Fubini's theorem]] fails, and why [[Thm - Fubini-Tonelli Theorem|Tonelli]] does not rescue the situation.

**(c)** State the practical rule this enforces for interchanging the order of a double integral.

**Recall:**

![[Thm - Fubini-Tonelli Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** a counterexample isolating *why* absolute integrability is indispensable for Fubini.

**Assumption pattern:** Tonelli (no hypothesis) applies to $|f|$; Fubini (interchange) needs $f\in L^1$. The example is engineered so $\int|f|=\infty$ — the positive and negative masses each total $\infty$, and the iterated sums cancel them in *different orders*.

**Theorem routing:** compute both iterated sums directly; observe $\iint|f|=\infty$, so $f\notin L^1$, so Fubini's hypothesis fails.

---

# Legal Operations Used

1. **Direct computation** of iterated sums.
2. **Tonelli on $|f|$** to test the Fubini hypothesis.

---

# Hints

> [!note]- Hint 1
> Fix $m$: $\sum_n f(n,m)=f(m,m)+f(m+1,m)=1+(-1)=0$. So $\sum_m\sum_n f=0$.

> [!note]- Hint 2
> Fix $n$: $\sum_m f(n,m)=f(n,n)+f(n,n-1)$. For $n=1$ there is no $m=0$ term... $f(1,m)=1$ at $m=1$, $-1$ at $m=0$ (excluded). So $\sum_m f(1,m)=1$, and $\sum_m f(n,m)=0$ for $n\ge2$.

> [!note]- Hint 3
> $\sum_{n,m}|f(n,m)|$ counts $2$ for each diagonal — infinitely many. So $\iint|f|=\infty$.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) computes the two iterated sums directly: the $n$-first order gives $0$ (each $m$-column cancels), while the $m$-first order gives $1$ (only the $n = 1$ row survives because $m = n - 1 = 0$ is excluded); Step 2 (part b) identifies the failed hypothesis as $f \notin L^1$ by computing $\iint|f| = \infty$ via Tonelli, and notes Tonelli does not save signed integrands; Step 3 (part c) extracts the practical rule "Tonelli first on $|f|$, Fubini second on $f$." The non-obvious move is in Step 1 — the asymmetry comes from the boundary index $m = 0$ being excluded from $\mathbb{N}$, which is what breaks the symmetry between the two orders.

**Step 1 — (a) The two iterated sums.** Sum over $n$ first: for fixed $m\ge1$, the only nonzero terms are $f(m,m)=1$ and $f(m+1,m)=-1$, so $\sum_n f(n,m)=0$, and
$$\sum_m\Big(\sum_n f(n,m)\Big)=\sum_m 0=0.$$
Sum over $m$ first: for fixed $n$, the nonzero terms are $f(n,n)=1$ and $f(n,n-1)=-1$ — but the term $m=n-1$ exists only for $n\ge2$. So $\sum_m f(1,m)=1$ and $\sum_m f(n,m)=0$ for $n\ge2$, giving
$$\sum_n\Big(\sum_m f(n,m)\Big)=1+0+0+\cdots=1.$$
The iterated sums are $0$ and $1$ — **unequal**.

**Step 2 — (b) Which hypothesis fails.** $|f(n,m)|=1$ on the two diagonals $\{n=m\}$ and $\{n=m+1\}$, each infinite, so
$$\iint|f|\,d(\#\otimes\#)=\sum_{n,m}|f(n,m)|=\infty.$$
Hence $f\notin L^1(\#\otimes\#)$ — Fubini's hypothesis *fails*. Tonelli does not rescue it: Tonelli applies to *non-negative* functions, and $f$ takes both signs; applying Tonelli to $|f|$ correctly gives $\iint|f|=\infty$ (consistently, in both orders), but says nothing about $f$ itself. The interchange of orders is simply not licensed.

**Step 3 — (c) The rule.** Before swapping the order of a double integral of a *signed* (or complex) integrand, **first apply Tonelli to $|f|$**. Only if $\iint|f|<\infty$ — equivalently $f\in L^1(\mu_1\otimes\mu_2)$ — may Fubini be invoked to interchange. If $\iint|f|=\infty$, the two iterated integrals may legitimately disagree, as here.

> [!note]- Complete formal solution
> (a) $\sum_n f(n,m)=0$ for every $m$, so the $n$-first iterated sum is $0$; $\sum_m f(n,m)=1$ for $n=1$ and $0$ for $n\ge2$, so the $m$-first iterated sum is $1$. (b) $\iint|f|=\sum_{n,m}|f(n,m)|=\infty$ (two infinite diagonals), so $f\notin L^1$ and Fubini does not apply; Tonelli concerns only $f\ge0$. (c) Always verify $\iint|f|<\infty$ (Tonelli on $|f|$) before interchanging the order for a signed integrand. $\blacksquare$

---

# Key Takeaways

**Fubini's interchange of integration order is *false* without absolute integrability — the two iterated integrals can both exist finitely and still disagree.** The mechanism is conditional cancellation: when the positive and negative masses are each infinite, summing in different orders cancels them differently, exactly as a conditionally convergent series can be rearranged to any value. This is why Fubini carries the hypothesis $f\in L^1(\mu_1\otimes\mu_2)$ and Tonelli (which has none) is restricted to $f\ge0$.

**The operative discipline: Tonelli first, on $|f|$; Fubini second, on $f$.** [[Thm - Fubini-Tonelli Theorem|Tonelli]] applied to $|f|$ always succeeds and tells you whether $\iint|f|<\infty$ — the precise gate to Fubini. Recognising this two-step ("check absolute integrability with the free theorem, then interchange with the conditional one") is the single most important habit for using Fubini correctly, and it is the same "is the double sum *absolutely* convergent?" question as in [[Ex - Term-by-term integration of series|term-by-term integration of series]].
