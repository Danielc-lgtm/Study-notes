---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Absolute Continuity and Density"
  - "Def - Lp Spaces"
  - "Thm - Vitali Convergence Theorem"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space.

**(a)** Show that a family $(f_i)_{i\in I}\subseteq L^1(\mu)$ **dominated** by a single $g\in L^1$ (i.e. $|f_i|\le g$ for all $i$) is [[Def - Absolute Continuity and Density|uniformly integrable]].

**(b)** Show that if $\mu(X)<\infty$ and $(f_i)$ is **bounded in $L^p$** for some $p>1$ — $\sup_i\|f_i\|_p<\infty$ — then $(f_i)$ is uniformly integrable.

**(c)** Show by example ($p=1$) that $L^1$-boundedness alone does *not* imply uniform integrability.

**Recall:**

A family has [[Def - Absolute Continuity and Density|uniformly absolutely continuous integrals]] (is **uniformly integrable**, UI) if $\forall\varepsilon\,\exists\delta:\ \mu(A)<\delta\Rightarrow\sup_i\int_A|f_i|\,d\mu<\varepsilon$.

---

# Convergent Strategy

**Problem class:** verifying uniform integrability — establishing that an *infinite* family has uniformly small integrals over small sets.

**Assumption pattern:** (a) domination — a single $g$ controls everyone, so the family inherits $g$'s [[Def - Absolute Continuity and Density|absolute continuity]]. (b) $L^p$-boundedness with $p>1$ — the *extra integrability* ($p>1$) gives, via [[Thm - Hölder and Minkowski Inequalities|Hölder]], a quantitative gain on small sets.

**Theorem routing:** (a) $\int_A|f_i|\le\int_A g$, and a single $L^1$ function is absolutely continuous. (b) Hölder: $\int_A|f_i|\le\|f_i\|_p\,\mu(A)^{1/q}\le M\mu(A)^{1/q}$.

**Key decision point:** the exponent $1/q>0$ in (b) — that positive power of $\mu(A)$ is what makes the bound vanish as $\mu(A)\to0$; it exists only because $p>1$.

---

# Legal Operations Used

1. **Domination transfers absolute continuity** from $g$ to the whole family.
2. **Hölder's inequality** to extract a power of $\mu(A)$.
3. **Escape-to-spike counterexample** for the $p=1$ failure.

---

# Hints

> [!note]- Hint 1
> (a): $\int_A|f_i|\le\int_A g$ uniformly in $i$. A single $g\in L^1$ has absolutely continuous integral ([[Def - Absolute Continuity and Density|ε–δ form]]).

> [!note]- Hint 2
> (b): $\int_A|f_i|=\int|f_i|\mathbf{1}_A\le\|f_i\|_p\|\mathbf{1}_A\|_q$ by Hölder. Compute $\|\mathbf{1}_A\|_q$.

> [!note]- Hint 3
> (c): the spike $f_n=n\mathbf{1}_{[0,1/n]}$ on $[0,1]$ has $\|f_n\|_1=1$ but $\int_{[0,1/n]}f_n=1\not\to0$ though $\mu([0,1/n])\to0$.

---

# Solution

**Step 1 — (a) Domination $\Rightarrow$ UI.** For any $A$ and any $i$, $|f_i|\le g$ gives $\int_A|f_i|\,d\mu\le\int_A g\,d\mu$. Since $g\in L^1$, by the [[Def - Absolute Continuity and Density|ε–δ characterisation]] there is $\delta>0$ with $\mu(A)<\delta\Rightarrow\int_A g<\varepsilon$. Then $\sup_i\int_A|f_i|\le\int_A g<\varepsilon$ — the same $\delta$ works for every $i$, so $(f_i)$ is UI.

**Step 2 — (b) $L^p$-boundedness ($p>1$) $\Rightarrow$ UI.** Let $q$ be conjugate to $p$ ($1/p+1/q=1$, $q<\infty$) and $M=\sup_i\|f_i\|_p$. By [[Thm - Hölder and Minkowski Inequalities|Hölder]],
$$\int_A|f_i|\,d\mu=\int|f_i|\,\mathbf{1}_A\,d\mu\le\|f_i\|_p\,\|\mathbf{1}_A\|_q=\|f_i\|_p\,\mu(A)^{1/q}\le M\,\mu(A)^{1/q}.$$
Given $\varepsilon>0$, choose $\delta=(\varepsilon/M)^q$; then $\mu(A)<\delta\Rightarrow\sup_i\int_A|f_i|\le M\delta^{1/q}=\varepsilon$. So $(f_i)$ is UI.

> [!note]- Derivation
> The exponent $1/q$ is *strictly positive* exactly because $p>1$ (so $q<\infty$). That positive power makes $M\mu(A)^{1/q}\to0$ as $\mu(A)\to0$. For $p=1$, $q=\infty$ and $\mu(A)^{1/q}=\mu(A)^0=1$ — no gain, the argument collapses.

**Step 3 — (c) $p=1$ fails.** On $([0,1],\lambda)$, $f_n=n\mathbf{1}_{[0,1/n]}$ has $\|f_n\|_1=n\cdot\tfrac1n=1$, so $(f_n)$ is $L^1$-bounded. But for $A_n=[0,1/n]$, $\lambda(A_n)=1/n\to0$ while $\int_{A_n}|f_n|=1\not\to0$. So no $\delta$ works uniformly — $(f_n)$ is **not** UI. The mass concentrates into a spike, defeating absolute continuity.

> [!note]- Complete formal solution
> (a) $\int_A|f_i|\le\int_A g$, and $g\in L^1$ is absolutely continuous, so the same $\delta$ serves all $i$. (b) Hölder gives $\int_A|f_i|\le\|f_i\|_p\mu(A)^{1/q}\le M\mu(A)^{1/q}$; with $q<\infty$ (as $p>1$), $\delta=(\varepsilon/M)^q$ works. (c) $f_n=n\mathbf{1}_{[0,1/n]}$: $\|f_n\|_1=1$ but $\int_{[0,1/n]}f_n=1$ with $\lambda([0,1/n])\to0$ — not UI. $\blacksquare$

---

# Key Takeaways

**Uniform integrability has two standard sufficient conditions — domination, and $L^p$-boundedness for $p>1$ — and recognising either is how one *verifies* UI in practice.** Domination makes UI obvious (everyone inherits one function's absolute continuity); $L^p$-boundedness with $p>1$ makes it a one-line Hölder estimate, the positive power $\mu(A)^{1/q}$ doing the work. Since UI is the exact hypothesis of the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]], these two recognitions are how one upgrades convergence in measure (or a.s.) to $L^1$ — and they show DCT (dominated case) is a special case of Vitali.

**The threshold is sharp: $p>1$ gives UI for free, $p=1$ does not.** $L^1$-boundedness only controls *total* mass; it cannot stop that mass from concentrating into a spike, which is exactly the [[Ex - Strict inequality in Fatou's lemma|escape mechanism]] that defeats absolute continuity. The extra integrability $p>1$ is what forbids concentration. This is the same threshold that appears in the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorems]]: $L^p$-bounded martingales ($p>1$) converge in $L^p$ automatically, while $L^1$-bounded ones need the *extra* hypothesis of uniform integrability bolted on.
