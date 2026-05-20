---
type: theorem
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Def - Simple Function"
  - "Thm - Approximation by Simple Functions"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $f_n,f:X\to[0,\infty]$ measurable; $f_n\uparrow f$ means $0\le f_1\le f_2\le\cdots$ with $f_n(x)\to f(x)$ for every $x$.

---

# Motivation

The single deepest fact distinguishing Lebesgue's integral from Riemann's is that **the integral commutes with monotone limits**: if $f_n$ increases to $f$, then $\int f_n$ increases to $\int f$. Riemann's integral has no such theorem — a pointwise-increasing limit of Riemann-integrable functions need not be Riemann-integrable. The monotone convergence theorem (MCT) is what makes the Lebesgue integral *robust under limits*, and it is the foundation from which [[Thm - Fatou's Lemma|Fatou]], [[Thm - Dominated Convergence Theorem|DCT]], [[Thm - Fubini-Tonelli Theorem|Fubini]], and the $\sigma$-additivity of [[Def - Absolute Continuity and Density|density measures]] all follow. MCT is also what *defines computation*: since [[Thm - Approximation by Simple Functions|simple functions]] increase up to any $f\ge0$, MCT says $\int f=\lim\int s_n$ — the integral is computed by monotone approximation.

---

# Sources and Targets

**Sources.** The hypotheses are "$f_n\ge0$, $f_n\uparrow f$." Crucial source-broadenings: (i) the increase need only hold [[Def - Almost Everywhere|a.e.]]; (ii) *any* sequence of [[Def - Simple Function|simple functions]] increasing to $f$ qualifies — this is how MCT is invoked to *define* $\int f$; (iii) **partial sums of a non-negative series** $\sum_k g_k$ increase, so MCT gives $\int\sum_k g_k=\sum_k\int g_k$ — term-by-term integration of non-negative series, free.

**Targets.** "$\int f_n\uparrow\int f$" combines with: (i) [[Thm - Approximation by Simple Functions|simple approximation]] to *define and compute* every integral; (ii) the "standard machine" — prove any integral identity for indicators, extend to simple by linearity, to $f\ge0$ by MCT; (iii) it yields, immediately, that $\nu(A)=\int_A f\,d\mu$ is $\sigma$-additive, i.e. a [[Def - Absolute Continuity and Density|measure]].

---

# Statement

Let $f_n:X\to[0,\infty]$ be measurable with $f_n\uparrow f$ (pointwise, or $\mu$-a.e.). Then $f$ is measurable and
$$\int_X f_n\,d\mu\ \xrightarrow[n\to\infty]{}\ \int_X f\,d\mu,\qquad\text{equivalently}\qquad \lim_{n\to\infty}\int f_n\,d\mu=\int\lim_{n\to\infty}f_n\,d\mu.$$

---

# Why Is It True

One inequality is free. Since $f_n\le f_{n+1}\le f$, [[Thm - Properties of the Integral|monotonicity of the integral]] gives $\int f_n\le\int f_{n+1}\le\int f$; the left side is increasing and bounded, so $\lim\int f_n$ exists and is $\le\int f$.

The reverse, $\lim\int f_n\ge\int f$, is the content. By definition $\int f=\sup\{\int s:s\le f\text{ simple}\}$, so it suffices to show $\lim\int f_n\ge\int s$ for every simple $s\le f$. Fix such an $s$ and a slack factor $\varepsilon\in(0,1)$, and look at
$$G_n=\{x:f_n(x)\ge(1-\varepsilon)s(x)\}.$$
This is the set where $f_n$ has "caught up to within $(1-\varepsilon)$" of $s$. Because $f_n\uparrow f\ge s>(1-\varepsilon)s$ (where $s>0$), every point is eventually caught: $G_n\uparrow X$. Now
$$\int f_n\ \ge\ \int_{G_n}f_n\ \ge\ (1-\varepsilon)\int_{G_n}s\ =\ (1-\varepsilon)\sum_i\alpha_i\,\mu(A_i\cap G_n).$$
Here is the engine: $G_n\uparrow X$ forces $A_i\cap G_n\uparrow A_i$, and by [[Thm - Properties of Measures|continuity of the measure from below]], $\mu(A_i\cap G_n)\uparrow\mu(A_i)$. Let $n\to\infty$: $\lim\int f_n\ge(1-\varepsilon)\sum_i\alpha_i\mu(A_i)=(1-\varepsilon)\int s$. Let $\varepsilon\downarrow0$: $\lim\int f_n\ge\int s$. Sup over $s$: $\lim\int f_n\ge\int f$.

The slogan: **MCT is continuity-of-the-measure-from-below, promoted from sets to functions.** The set-level fact "$A_i\cap G_n\uparrow A_i\Rightarrow\mu\uparrow$" *is* the heart; the $(1-\varepsilon)$ slack is only there because $f_n$ catches up to $s$ asymptotically, not exactly.

---

# What Makes This Hard

The reverse inequality is where everyone stalls. The non-obvious move is the **catching-up set** $G_n=\{f_n\ge(1-\varepsilon)s\}$ with its deliberate $(1-\varepsilon)$ slack — without the slack, $\{f_n\ge s\}$ need not increase to all of $X$ (if $f_n<f$ strictly, $f_n$ may never reach $s$). The slack converts "$f_n\uparrow f\ge s$" into "$f_n$ eventually exceeds $(1-\varepsilon)s$," which *does* give $G_n\uparrow X$. The other essential recognition: the integral of a *simple* function over $G_n$ is a finite sum $\sum\alpha_i\mu(A_i\cap G_n)$, and continuity of the *measure* from below is what is actually being used — MCT is bootstrapped from the set version.

---

# Rederivation Scaffold

**High-level strategy.** "$\le$" is monotonicity. "$\ge$": reduce to simple $s\le f$; introduce the catching-up set $G_n=\{f_n\ge(1-\varepsilon)s\}\uparrow X$; bound $\int f_n$ below on $G_n$; push $\mu(A_i\cap G_n)\uparrow\mu(A_i)$ via continuity from below; remove the slack.

**Subgoal decomposition.**

1. **"$\le$".** Monotonicity of the integral: $\int f_n\le\int f$, and $\int f_n$ increasing, so $\lim\int f_n$ exists $\le\int f$.
2. **Reduce "$\ge$" to simple functions.** $\int f=\sup_{s\le f}\int s$; show $\lim\int f_n\ge\int s$ for each simple $s\le f$.
3. **Catching-up set.** $G_n=\{f_n\ge(1-\varepsilon)s\}$; $f_n\uparrow f\ge s\Rightarrow G_n\uparrow X$.
4. **Bound and pass to the limit.** $\int f_n\ge(1-\varepsilon)\sum_i\alpha_i\mu(A_i\cap G_n)$; continuity from below $\Rightarrow\to(1-\varepsilon)\int s$; let $\varepsilon\downarrow0$, then sup over $s$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The catching-up sets exhaust $X$
> **Statement:** For simple $s\le f$ and $\varepsilon\in(0,1)$, $G_n=\{f_n\ge(1-\varepsilon)s\}$ satisfies $G_n\subseteq G_{n+1}$ and $\bigcup_n G_n=X$.
>
> **Hint:** The slack $\varepsilon$ is the trick: $f_n(x)\to f(x)\ge s(x)$ means $f_n(x)$ will eventually exceed $(1-\varepsilon)s(x)$ strictly for every $x$, even though it might never reach $s(x)$.
>
> **Why needed:** It supplies an exhausting increasing sequence of sets on which $f_n\ge(1-\varepsilon)s$ holds pointwise, so the inequality survives integration and continuity from below converts pointwise convergence into a measure-theoretic statement.
>
> > [!note]- Full proof
> > $f_n\le f_{n+1}\Rightarrow G_n\subseteq G_{n+1}$. Fix $x$. If $s(x)=0$ then $f_n(x)\ge0=(1-\varepsilon)s(x)$, so $x\in G_1$. If $s(x)>0$ then $(1-\varepsilon)s(x)<s(x)\le f(x)=\lim f_n(x)$, so $f_n(x)\ge(1-\varepsilon)s(x)$ for large $n$, i.e. $x\in G_n$ eventually. Hence $\bigcup_n G_n=X$. $\square$

> [!note]- Lemma 2: The lower bound and its limit
> **Statement:** $\lim_n\int f_n\,d\mu\ge(1-\varepsilon)\int s\,d\mu$ for every simple $s\le f$ and $\varepsilon\in(0,1)$.
>
> **Hint:** Integrate $f_n$ only over $G_n$, expand the simple function $s=\sum_i\alpha_i\mathbf{1}_{A_i}$, and use continuity from below on each $A_i\cap G_n\uparrow A_i$.
>
> **Why needed:** This is the only nontrivial inequality in MCT — combining it with the trivial $\lim\int f_n\le\int f$ (by monotonicity), then letting $\varepsilon\downarrow 0$ and taking the supremum over simple $s\le f$, gives the full equality $\lim\int f_n=\int f$.
>
> > [!note]- Full proof
> > On $G_n$, $f_n\ge(1-\varepsilon)s$, so by monotonicity $\int f_n\ge\int f_n\mathbf{1}_{G_n}\ge(1-\varepsilon)\int s\,\mathbf{1}_{G_n}=(1-\varepsilon)\sum_i\alpha_i\mu(A_i\cap G_n)$, writing $s=\sum_i\alpha_i\mathbf{1}_{A_i}$. By Lemma 1, $A_i\cap G_n\uparrow A_i$; [[Thm - Properties of Measures|continuity from below]] gives $\mu(A_i\cap G_n)\uparrow\mu(A_i)$. Letting $n\to\infty$: $\lim_n\int f_n\ge(1-\varepsilon)\sum_i\alpha_i\mu(A_i)=(1-\varepsilon)\int s$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> $f=\lim f_n$ is measurable ([[Thm - Operations Preserve Measurability]]). Monotonicity gives $\int f_n\uparrow L\le\int f$. For the reverse: by Lemma 2, $L\ge(1-\varepsilon)\int s$ for all simple $s\le f$ and all $\varepsilon\in(0,1)$; let $\varepsilon\downarrow0$ to get $L\ge\int s$, then take the supremum over simple $s\le f$ to get $L\ge\sup_{s\le f}\int s=\int f$. Hence $L=\int f$. The a.e. version follows by modifying $f_n,f$ on a null set, which changes no integral. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Apply MCT to *partial sums* $S_N=\sum_{k\le N}g_k$ of a non-negative series: $S_N\uparrow\sum_k g_k$, so $\int\sum g_k=\sum\int g_k$ — interchange of sum and integral, the discrete face of MCT and the proof that a [[Def - Absolute Continuity and Density|density]] defines a measure. In probability, MCT for conditional expectation ($X_n\uparrow X\Rightarrow\mathbb{E}[X_n\mid\mathcal{G}]\uparrow\mathbb{E}[X\mid\mathcal{G}]$) drives the construction of [[Def - Conditional Expectation|conditional expectation]] for non-negative variables and the proof of [[Thm - Almost Sure Martingale Convergence|martingale convergence]].

---

# Bridges

- **[[Thm - Properties of Measures]]** — continuity from below for sets is MCT for indicator functions; MCT is its promotion to all $f\ge0$.
- **[[Thm - Fatou's Lemma]]**, **[[Thm - Dominated Convergence Theorem]]** — both are corollaries of MCT.
- **[[Thm - Approximation by Simple Functions]]** — together with MCT, this *defines* $\int f=\lim\int s_n$ and powers the "standard machine."
