---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Integral"
  - "Thm - Monotone Convergence Theorem"
  - "Thm - Approximation by Simple Functions"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $X=\{1,2,3,\dots\}$, $\mathcal{A}=2^X$, and $\mathbb{P}$ the **geometric distribution**: $\mathbb{P}(\{k\})=(1-p)^{k-1}p$ for fixed $p\in(0,1)$.

**(a)** Verify $\mathbb{P}$ is a probability measure.

**(b)** Let $f(k)=k$. Compute $\mathbb{E}[f]=\int_X f\,d\mathbb{P}$ rigorously, using the [[Thm - Monotone Convergence Theorem|monotone convergence theorem]] to justify every interchange.

**(c)** State the general principle: for $f\ge0$ on a countable space, $\int f\,d\mu=\sum_k f(k)\,\mu(\{k\})$, and explain why MCT is what makes this rigorous.

**Recall:**

![[Thm - Monotone Convergence Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** computing an integral on a discrete space — where the integral *is* a series, but the equality "integral $=$ series" needs proof.

**Assumption pattern:** $f\ge0$, so $f$ is the increasing limit of its truncations $f_n=f\mathbf{1}_{\{f\le n\}}$ (or $f\cdot\mathbf{1}_{\{1,\dots,n\}}$), each a [[Def - Simple Function|simple function]] with a finite-sum integral. MCT licenses passing the limit through.

**Theorem routing:** $f_n\uparrow f$ simple $\Rightarrow\int f=\lim\int f_n=\lim\sum_{k\le n}f(k)\mathbb{P}(\{k\})=\sum_k f(k)\mathbb{P}(\{k\})$.

**Key decision point:** recognising that "integral $=$ infinite sum" is exactly an MCT statement (partial sums increase), not a definition.

---

# Legal Operations Used

1. **Truncate** $f$ to finite-range simple functions $f_n\uparrow f$.
2. **MCT** to pass the limit through the integral.
3. **Geometric series** summation.

---

# Hints

> [!note]- Hint 1
> $\mathbb{P}(X)=\sum_{k\ge1}(1-p)^{k-1}p=p\cdot\frac{1}{1-(1-p)}=1$.

> [!note]- Hint 2
> Let $f_n=\sum_{k=1}^n k\,\mathbf{1}_{\{k\}}$, a simple function with $\int f_n\,d\mathbb{P}=\sum_{k=1}^n k\,\mathbb{P}(\{k\})$. Then $f_n\uparrow f$.

> [!note]- Hint 3
> $\sum_{k\ge1}k(1-p)^{k-1}p=p\sum_{k\ge1}k(1-p)^{k-1}=p\cdot\frac{d}{dp}\big[-\sum_k(1-p)^k\big]$. Or: $\sum k x^{k-1}=(1-x)^{-2}$.

---

# Solution

**Step 1 — (a).** $\mathbb{P}(\{k\})\ge0$ and $\sum_{k\ge1}\mathbb{P}(\{k\})=p\sum_{k\ge0}(1-p)^k=p\cdot(1-(1-p))^{-1}=1$. $\sigma$-additivity on $2^X$ holds since $\mathbb{P}(A)=\sum_{k\in A}\mathbb{P}(\{k\})$ and series of non-negative terms rearrange freely. So $\mathbb{P}$ is a probability measure.

**Step 2 — (b).** Set $f_n=\sum_{k=1}^n k\,\mathbf{1}_{\{k\}}$. Each $f_n$ is a non-negative measurable [[Def - Simple Function|simple function]], $0\le f_1\le f_2\le\cdots$, and $f_n(k)\to k=f(k)$ for every $k$ — so $f_n\uparrow f$.

> [!note]- Derivation
> $\int f_n\,d\mathbb{P}=\sum_{k=1}^n k\,\mathbb{P}(\{k\})$ by the simple-function integral. By [[Thm - Monotone Convergence Theorem|MCT]], $\mathbb{E}[f]=\int f\,d\mathbb{P}=\lim_n\int f_n\,d\mathbb{P}=\sum_{k=1}^\infty k(1-p)^{k-1}p$.
> Evaluate the series: with $x=1-p$, $\sum_{k\ge1}kx^{k-1}=\frac{d}{dx}\sum_{k\ge0}x^k=\frac{d}{dx}(1-x)^{-1}=(1-x)^{-2}=p^{-2}$. Hence $\mathbb{E}[f]=p\cdot p^{-2}=\dfrac1p$.

So $\mathbb{E}[X]=1/p$, and $f\in L^1(\mathbb{P})$.

**Step 3 — (c) General principle.** On a countable space, for $f\ge0$, the truncations $f_n=\sum_{k\le n}f(k)\mathbf{1}_{\{k\}}$ are simple with $f_n\uparrow f$, so MCT gives $\int f\,d\mu=\lim\sum_{k\le n}f(k)\mu(\{k\})=\sum_k f(k)\mu(\{k\})$. MCT is exactly what justifies the interchange "$\int\lim=\lim\int$" — without it, "the integral is the infinite sum" is an unproven swap of a limit and an integral.

> [!note]- Complete formal solution
> (a) $\sum_k\mathbb{P}(\{k\})=p\sum_{k\ge0}(1-p)^k=1$; $\sigma$-additivity from non-negative series. (b) $f_n=\sum_{k\le n}k\mathbf{1}_{\{k\}}\uparrow f$, simple, so by MCT $\mathbb{E}[f]=\lim\sum_{k\le n}k\mathbb{P}(\{k\})=\sum_{k\ge1}k(1-p)^{k-1}p=p\cdot p^{-2}=1/p$. (c) Truncations $f_n\uparrow f$ are simple; MCT gives $\int f=\sum_k f(k)\mu(\{k\})$, the swap of limit and integral it licenses. $\blacksquare$

---

# Key Takeaways

**On a countable space the integral *is* a series — but "integral $=$ infinite sum" is a theorem (an MCT statement), not a definition.** The integral is defined via [[Def - Simple Function|simple functions]] and suprema; that it equals $\sum_k f(k)\mu(\{k\})$ requires passing a limit through the integral, which is exactly what MCT licenses, because the partial sums $f_n=\sum_{k\le n}f(k)\mathbf{1}_{\{k\}}$ *increase* to $f$. The discrete case makes vivid that the Lebesgue integral *generalises* summation, and the convergence theorems generalise theorems about interchanging sums and limits.

**The computational template: truncate to a simple function, integrate the truncation as a finite sum, then invoke MCT.** This three-step recipe — $f_n\uparrow f$ simple, $\int f_n=$ finite sum, $\int f=\lim\int f_n$ — is how *every* concrete integral of a non-negative function is computed rigorously, discrete or not. The same recipe computes $\mathbb{E}[X]$ for any non-negative random variable and is the discrete face of the [[Thm - Monotone Convergence Theorem|standard machine]].
