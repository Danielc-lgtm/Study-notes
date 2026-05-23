---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Lp Spaces"
  - "Thm - Hölder and Minkowski Inequalities"
  - "Thm - Monotone Convergence Theorem"
  - "Thm - Dominated Convergence Theorem"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $1\le p\le\infty$; $\|\cdot\|_p$ the [[Def - Lp Spaces|Lᵖ norm]]. A sequence is **Cauchy** if $\|f_n-f_m\|_p\to0$ as $n,m\to\infty$.

---

# Motivation

A normed space is *useful* in analysis only if it is **complete** — if Cauchy sequences converge — because completeness is what licenses every limiting argument: fixed-point theorems, the construction of solutions as limits of approximants, the passage from a formal series to an honest function. The theorem (the **Riesz–Fischer theorem**) states that $L^p(\mu)$ is complete, hence a **Banach space** (and $L^2$ a **Hilbert space**). This is the property that makes $L^p$ the natural arena for PDE, Fourier analysis, and probability — and it is the deep payoff of having built the Lebesgue integral, since completeness is precisely what the *Riemann*-integral space of functions lacks.

---

# Sources and Targets

**Sources.** The hypothesis is "$(f_n)$ Cauchy in $L^p$." The proof's broadening: a Cauchy sequence has a **rapidly Cauchy subsequence** ($\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}$), and that subsequence admits a *dominating function*. Recognising "extract a fast subsequence, dominate it" is the transferable technique.

**Targets.** Completeness makes $L^p$ a **Banach space**; $L^2$ a **Hilbert space**, which unlocks orthogonal projection — the construction of [[Def - Conditional Expectation|conditional expectation]]. It is also the hypothesis behind the [[Thm - Almost Sure Martingale Convergence|Lᵖ martingale convergence theorem]] and every "limit of approximants is a genuine function" argument.

---

# Statement

For every measure space $(X,\mathcal{A},\mu)$ and every $1\le p\le\infty$, the normed space $(L^p(\mu),\|\cdot\|_p)$ is **complete**: every Cauchy sequence in $L^p(\mu)$ converges in $\|\cdot\|_p$ to an element of $L^p(\mu)$. Hence $L^p(\mu)$ is a **Banach space**, and $L^2(\mu)$ a **Hilbert space**.

---

# Why Is It True

Completeness of $L^p$ is **completeness of $\mathbb{R}$, transmitted through the integral**. The transmission is the standard "fast subsequence" argument.

*Step 1 — a Cauchy sequence is determined by a fast subsequence.* A Cauchy sequence converges iff some subsequence does (Cauchy + convergent subsequence $\Rightarrow$ convergent). So extract $n_1<n_2<\cdots$ with $\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}$ — possible because the tail differences shrink. It suffices to converge this fast subsequence.

*Step 2 — build a dominating function from the gaps.* Set $g=\sum_{k\ge1}|f_{n_{k+1}}-f_{n_k}|$, the total variation of the subsequence. By [[Thm - Hölder and Minkowski Inequalities|Minkowski]] and [[Thm - Monotone Convergence Theorem|MCT]], $\|g\|_p\le\sum_k\|f_{n_{k+1}}-f_{n_k}\|_p\le\sum_k2^{-k}=1<\infty$. So $g\in L^p$, hence **$g<\infty$ a.e.** — at almost every $x$ the series $\sum_k(f_{n_{k+1}}(x)-f_{n_k}(x))$ is *absolutely* convergent.

*Step 3 — define the limit pointwise.* Where $g(x)<\infty$, the telescoping series converges absolutely in $\mathbb{R}$ (completeness of $\mathbb{R}$!), so $f(x):=\lim_k f_{n_k}(x)=f_{n_1}(x)+\sum_k(f_{n_{k+1}}(x)-f_{n_k}(x))$ exists; set $f=0$ on the null set where $g=\infty$. This $f$ is measurable.

*Step 4 — convergence is in $L^p$, not just pointwise.* The tail is dominated: $|f-f_{n_k}|=\big|\sum_{j\ge k}(f_{n_{j+1}}-f_{n_j})\big|\le g\in L^p$, and $|f-f_{n_k}|^p\le g^p\in L^1$, with $|f-f_{n_k}|\to0$ a.e. By the [[Thm - Dominated Convergence Theorem|dominated convergence theorem]], $\|f-f_{n_k}\|_p^p=\int|f-f_{n_k}|^p\to0$. So $f_{n_k}\to f$ in $L^p$; with $f\in L^p$ (it is $\le|f_{n_1}|+g$) and the original sequence Cauchy, the *whole* sequence converges to $f$.

The mechanism: **a fast subsequence has a finite-$L^p$-norm dominating function $g$; finiteness of $\|g\|_p$ forces $g<\infty$ a.e.; where $g<\infty$, completeness of $\mathbb{R}$ supplies the pointwise limit; domination by $g$ lets DCT upgrade pointwise convergence to $L^p$ convergence.** The case $p=\infty$ is even more direct — Cauchy in $\|\cdot\|_\infty$ means uniformly Cauchy off a null set, and uniform limits of bounded functions are bounded.

---

# What Makes This Hard

The whole proof is one strategic idea — **pass to a rapidly-Cauchy subsequence and dominate it by the sum of its gaps** — and everything else is routine. The non-obvious moves: (i) reducing to a subsequence (legitimate because Cauchy sequences inherit limits from subsequences); (ii) realising the *gap-sum* $g=\sum|f_{n_{k+1}}-f_{n_k}|$ is the dominating function, with $\|g\|_p$ finite by Minkowski+MCT; (iii) reading "$g\in L^p$" as "$g<\infty$ a.e.", which is what makes the pointwise series converge. Students often try to extract a limit directly from the Cauchy sequence without the subsequence, and get stuck because there is no pointwise control.

---

# Rederivation Scaffold

**High-level strategy.** Extract a subsequence with gaps $\le2^{-k}$; dominate it by $g=\sum$ gaps, $\|g\|_p\le1$; $g<\infty$ a.e. gives a pointwise limit $f$; DCT upgrades to $L^p$ convergence; Cauchy + convergent subsequence $\Rightarrow$ whole sequence converges.

**Subgoal decomposition.**

1. **Fast subsequence.** $(f_n)$ Cauchy $\Rightarrow$ pick $n_k$ with $\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}$.
2. **Dominating function.** $g=\sum_k|f_{n_{k+1}}-f_{n_k}|$; Minkowski + MCT $\Rightarrow\|g\|_p\le1$, so $g\in L^p$ and $g<\infty$ a.e.
3. **Pointwise limit.** Where $g<\infty$, $\sum_k(f_{n_{k+1}}-f_{n_k})$ converges absolutely; define $f$ as the limit (and $0$ on the null set).
4. **$L^p$ convergence.** $|f-f_{n_k}|\le g$, so $|f-f_{n_k}|^p\le g^p\in L^1$; [[Thm - Dominated Convergence Theorem|DCT]] $\Rightarrow\|f-f_{n_k}\|_p\to0$.
5. **Whole sequence.** Cauchy + $f_{n_k}\to f$ $\Rightarrow f_n\to f$ in $L^p$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A rapidly-Cauchy subsequence has an $L^p$ dominator
> **Statement:** If $\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}$, then $g=\sum_k|f_{n_{k+1}}-f_{n_k}|$ satisfies $\|g\|_p\le1$, so $g\in L^p$ and $g<\infty$ a.e.
>
> **Hint:** Bound each term of the series by $2^{-k}$ so the partial sums are Minkowski-controlled by the geometric series $\sum 2^{-k}=1$, then push the bound through monotone convergence.
>
> **Why needed:** The dominator $g$ is the universal envelope of the telescoping series: it makes the rearranged tail $|f-f_{n_k}|\le\sum_{j\ge k}|f_{n_{j+1}}-f_{n_j}|\le g$ pointwise, supplying the integrable bound that DCT requires in Lemma 2.
>
> > [!note]- Full proof
> > Let $g_m=\sum_{k=1}^m|f_{n_{k+1}}-f_{n_k}|\uparrow g$. By [[Thm - Hölder and Minkowski Inequalities|Minkowski]], $\|g_m\|_p\le\sum_{k=1}^m\|f_{n_{k+1}}-f_{n_k}\|_p\le\sum_{k=1}^\infty2^{-k}=1$. By [[Thm - Monotone Convergence Theorem|MCT]] ($g_m^p\uparrow g^p$), $\|g\|_p^p=\lim\|g_m\|_p^p\le1$. So $g\in L^p$; an $L^p$ function is finite a.e. (else $\int g^p=\infty$). $\square$

> [!note]- Lemma 2: Pointwise limit and $L^p$ convergence of the subsequence
> **Statement:** $f_{n_k}$ converges a.e. to a measurable $f\in L^p$, and $\|f-f_{n_k}\|_p\to0$.
>
> **Hint:** Use absolute convergence in the complete field $\mathbb{R}$ at each $x$ with $g(x)<\infty$ to produce $f(x)$, then control the $L^p$-distance via DCT with dominator $g^p$.
>
> **Why needed:** This is the actual completeness conclusion for the subsequence; once $f_{n_k}\to f$ in $L^p$, a Cauchy-plus-convergent-subsequence argument upgrades it to $f_n\to f$ in $L^p$ for the original sequence, which is the theorem.
>
> > [!note]- Full proof
> > Where $g(x)<\infty$ (a.e., by Lemma 1) the telescoping series $f_{n_1}(x)+\sum_k(f_{n_{k+1}}(x)-f_{n_k}(x))$ is absolutely convergent in the complete field $\mathbb{R}$, so $f(x)=\lim_k f_{n_k}(x)$ exists; set $f=0$ on the null exceptional set. Then $|f-f_{n_k}|=|\sum_{j\ge k}(f_{n_{j+1}}-f_{n_j})|\le g$, so $f\in L^p$ ($|f|\le|f_{n_1}|+g$) and $|f-f_{n_k}|^p\le g^p\in L^1$ with $|f-f_{n_k}|^p\to0$ a.e. [[Thm - Dominated Convergence Theorem|DCT]] gives $\|f-f_{n_k}\|_p^p\to0$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(f_n)$ be Cauchy in $L^p$, $1\le p<\infty$. Extract $n_k$ with $\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}$. Lemma 1 builds $g\in L^p$, $g<\infty$ a.e.; Lemma 2 produces $f\in L^p$ with $\|f-f_{n_k}\|_p\to0$. Given $\varepsilon>0$, pick $N$ with $\|f_n-f_m\|_p<\varepsilon$ for $n,m\ge N$ and $k$ with $n_k\ge N$, $\|f-f_{n_k}\|_p<\varepsilon$; then $\|f_n-f\|_p\le\|f_n-f_{n_k}\|_p+\|f_{n_k}-f\|_p<2\varepsilon$ for $n\ge N$. So $f_n\to f$ in $L^p$. For $p=\infty$: a Cauchy sequence in $\|\cdot\|_\infty$ is uniformly Cauchy off a null set; the uniform limit $f$ is essentially bounded and $\|f_n-f\|_\infty\to0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Completeness of $L^2$ makes it a **Hilbert space**, which gives orthogonal projection onto closed [[Def - Subspace|subspaces]] — and projecting a random variable onto $L^2(\mathcal{G})$ for a sub-$\sigma$-algebra $\mathcal{G}$ *is* [[Def - Conditional Expectation|conditional expectation]]. Completeness of $L^p$ also makes the [[Thm - Almost Sure Martingale Convergence|Lᵖ-bounded martingale]]'s limit a genuine $L^p$ random variable, and is the property invoked whenever a function is constructed as the $L^p$-limit of approximants (Fourier series, solutions of PDE).

---

# Bridges

- **[[Thm - Dominated Convergence Theorem]]** — the upgrade from pointwise to $L^p$ convergence; the dominator $g$ is custom-built for it.
- **[[Thm - Hölder and Minkowski Inequalities]]** — Minkowski bounds $\|g\|_p$, the step that makes the dominator integrable.
- **[[Def - Lp Spaces]]** — completeness is the property promoting the normed space $L^p$ to a Banach (and $L^2$ to a Hilbert) space.
