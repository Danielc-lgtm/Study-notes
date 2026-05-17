---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Monotone Convergence Theorem"
  - "Thm - Dominated Convergence Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space and $(g_k)_{k\ge1}$ measurable functions.

**(a)** If $g_k\ge0$ for all $k$, prove $\displaystyle\int_X\sum_{k=1}^\infty g_k\,d\mu=\sum_{k=1}^\infty\int_X g_k\,d\mu$ (both sides in $[0,\infty]$), with **no** integrability hypothesis.

**(b)** If instead $\sum_k\int_X|g_k|\,d\mu<\infty$, prove that $\sum_k g_k$ converges a.e. to an integrable function and the same interchange holds.

**(c)** Give an example of measurable $g_k$ for which $\int\sum g_k\neq\sum\int g_k$, and identify which hypothesis fails.

**Recall:**

![[Thm - Monotone Convergence Theorem#Formal Statement]]

[[Thm - Dominated Convergence Theorem|DCT]]: $|f_n|\le g\in L^1$, $f_n\to f$ a.e. $\Rightarrow\int f_n\to\int f$.

---

# Convergent Strategy

**Problem class:** justifying the interchange of an infinite sum and an integral.

**Assumption pattern:** an infinite sum is the *limit of its partial sums* $S_N=\sum_{k\le N}g_k$. If the $g_k\ge0$, the $S_N$ *increase* — MCT territory. If only $\sum\int|g_k|<\infty$, the $S_N$ are *dominated* by $G=\sum|g_k|\in L^1$ — DCT territory.

**Theorem routing:** (a) MCT on $S_N\uparrow\sum g_k$; (b) build the dominator $G=\sum|g_k|$, finite a.e. by (a), then DCT.

**Key decision point:** $g_k\ge0$ → MCT (free); signed → need an integrable dominator, built by applying (a) to $|g_k|$.

---

# Legal Operations Used

1. **Partial sums of a non-negative series increase** → MCT.
2. **Build a dominator** $G=\sum|g_k|$; (a) shows $\|G\|_1=\sum\|g_k\|_1<\infty$.
3. **DCT** on the partial sums dominated by $G$.

---

# Hints

> [!note]- Hint 1
> $S_N=\sum_{k=1}^N g_k$. For $g_k\ge0$, $S_N\uparrow\sum_k g_k$. Apply MCT and linearity.

> [!note]- Hint 2
> For (b), let $G=\sum_k|g_k|$. By (a), $\int G=\sum_k\int|g_k|<\infty$, so $G\in L^1$ and $G<\infty$ a.e. Then $|S_N|\le G$.

> [!note]- Hint 3
> For (c): on $\mathbb{N}$ with counting measure, find $g_k$ with $\sum_k g_k\equiv0$ but $\sum_k\int g_k\neq0$ — a "moving negative bump."

---

# Solution

**Step 1 — (a) Non-negative case.** $S_N=\sum_{k=1}^N g_k\ge0$ is measurable, and $S_N\uparrow\sum_{k=1}^\infty g_k$ since adding non-negative terms increases the partial sum. By [[Thm - Monotone Convergence Theorem|MCT]] and [[Thm - Properties of the Integral|linearity]],
$$\int\sum_{k=1}^\infty g_k\,d\mu=\lim_N\int S_N\,d\mu=\lim_N\sum_{k=1}^N\int g_k\,d\mu=\sum_{k=1}^\infty\int g_k\,d\mu.$$

**Step 2 — (b) Absolutely convergent case.** Let $G=\sum_k|g_k|\ge0$. By (a), $\int G\,d\mu=\sum_k\int|g_k|\,d\mu<\infty$, so $G\in L^1$ and $G<\infty$ $\mu$-a.e. Where $G<\infty$, the series $\sum_k g_k(x)$ is absolutely convergent in $\mathbb{R}$, defining $f(x)=\sum_k g_k(x)$ a.e.; set $f=0$ on the null set $\{G=\infty\}$.

> [!note]- Derivation
> The partial sums satisfy $|S_N|=|\sum_{k\le N}g_k|\le\sum_{k\le N}|g_k|\le G$, with $S_N\to f$ a.e. and $G\in L^1$. By [[Thm - Dominated Convergence Theorem|DCT]], $\int f=\lim_N\int S_N=\lim_N\sum_{k\le N}\int g_k=\sum_k\int g_k$. Also $f\in L^1$ since $|f|\le G$.

**Step 3 — (c) Counterexample.** On $(\mathbb{N},2^\mathbb{N},\#)$ define $g_k=\mathbf{1}_{\{k\}}-\mathbf{1}_{\{k+1\}}$. Then $\sum_{k=1}^\infty g_k(n)=\mathbf{1}_{\{1\}}(n)$ telescopes... let me instead take the standard one: $g_k=\mathbf{1}_{\{k\}}-\mathbf{1}_{\{k+1\}}$ gives $\sum_k g_k=\mathbf{1}_{\{1\}}$, $\int\sum g_k\,d\#=1$, while $\int g_k\,d\#=1-1=0$ so $\sum_k\int g_k=0\neq1$.

> [!note]- Derivation
> Each $g_k$ takes values $\pm1$, $\int g_k\,d\#=\#\{k\}-\#\{k+1\}=0$. But $\sum_{k\ge1}g_k(n)=\sum_k(\mathbf{1}_{\{k\}}(n)-\mathbf{1}_{\{k+1\}}(n))$ telescopes to $\mathbf{1}_{\{1\}}(n)$, so $\int\sum_k g_k\,d\#=1$. The interchange fails: $1\neq0$. The hypothesis that breaks is absolute summability — $\sum_k\int|g_k|\,d\#=\sum_k 2=\infty$. A negative bump "escapes to infinity."

> [!note]- Complete formal solution
> (a) $S_N\uparrow\sum g_k$ for $g_k\ge0$; MCT + linearity give the interchange. (b) $G=\sum|g_k|$ has $\int G=\sum\int|g_k|<\infty$ by (a), so $G\in L^1$, $G<\infty$ a.e.; $|S_N|\le G$, $S_N\to f$ a.e., DCT gives $\int f=\sum\int g_k$. (c) $g_k=\mathbf{1}_{\{k\}}-\mathbf{1}_{\{k+1\}}$ on $(\mathbb{N},\#)$: $\int g_k=0$ but $\sum g_k=\mathbf{1}_{\{1\}}$ has integral $1$; $\sum\int|g_k|=\infty$, so the hypothesis of (b) fails. $\blacksquare$

---

# Key Takeaways

**Term-by-term integration of a series is the convergence theorems applied to partial sums.** A series is a limit of partial sums; for non-negative terms the partial sums increase, so [[Thm - Monotone Convergence Theorem|MCT]] gives the interchange *unconditionally*; for signed terms one needs the partial sums dominated, which is exactly $\sum\int|g_k|<\infty$ (giving an integrable dominator $G=\sum|g_k|$) followed by [[Thm - Dominated Convergence Theorem|DCT]]. The trigger: "I want to swap $\int$ and $\sum$" → "non-negative terms? MCT, free. Signed? Check absolute summability, then DCT."

**The interchange fails by the same escape-to-infinity mechanism as every other convergence-theorem failure.** The counterexample's negative mass slides off to $+\infty$, present in every partial sum's integral as a cancellation but absent from the limit. Absolute summability $\sum\int|g_k|<\infty$ is the [[Def - Absolute Continuity and Density|"no escape"]] hypothesis — it is the discrete sibling of "having a dominating function." Whenever an interchange of $\sum$ and $\int$ (or $\sum$ and $\sum$, the Fubini-for-series statement) is in doubt, the question is always: is the double sum *absolutely* convergent?
