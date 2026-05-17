---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Hahn-Carathéodory Extension Theorem"
  - "Def - Outer Measure"
  - "Def - σ-Finite Measure"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $\mathcal{A}$ be an algebra on a set $X$ and $\mu$ a measure on $\sigma(\mathcal{A})$ that is $\sigma$-finite on $\mathcal{A}$ (there exist $X=\bigcup_k X_k$, $X_k\in\mathcal{A}$, $\mu(X_k)<\infty$). Prove the **approximation theorem**: for every $A\in\sigma(\mathcal{A})$ and every $\varepsilon>0$ there exist pairwise disjoint $A_1,A_2,\dots\in\mathcal{A}$ with
$$A\subseteq\bigcup_{n=1}^\infty A_n\qquad\text{and}\qquad\mu\Big(\bigcup_{n=1}^\infty A_n\,\setminus\,A\Big)<\varepsilon.$$
Deduce the finite version: if $\mu(A)<\infty$, there is a *single* set $E\in\mathcal{A}$ with $\mu(A\,\triangle\,E)<\varepsilon$.

**Recall:**

In the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory construction]] the measure on $\sigma(\mathcal{A})$ is the restriction of the [[Def - Outer Measure|outer measure]] $\mu^*(A)=\inf\{\sum_j\widetilde\mu(K_j):K_j\in\mathcal{A},\ A\subseteq\bigcup_j K_j\}$, and $\mu^*=\mu$ on $\sigma(\mathcal{A})$. $A\,\triangle\,E=(A\setminus E)\cup(E\setminus A)$.

---

# Convergent Strategy

**Problem class:** showing the generating algebra is "dense" in the generated $\sigma$-algebra, in the measure-gap sense.

**Assumption pattern:** the measure is the *restriction of an outer measure*, and an outer measure is *by definition* an infimum over algebra-covers. So an $\varepsilon$-economical algebra-cover always exists — that is not something to prove, it is the definition of $\mu^*$ unwound.

**Theorem routing:** $\mu(A)=\mu^*(A)=\inf\{\sum\widetilde\mu(K_j)\}$ supplies a cover $\bigcup K_j$ with $\sum\widetilde\mu(K_j)\le\mu(A)+\varepsilon$; this cover overshoots $A$ by at most $\varepsilon$ in measure. Disjointify the cover to get the $A_n$.

**Key decision point:** to get the *finite* version, truncate the countable cover — the tail has small measure because the total is finite.

---

# Legal Operations Used

1. **Unwind the outer measure** as an infimum over algebra-covers.
2. **Disjointify** a countable cover, $A_n=K_n\setminus\bigcup_{j<n}K_j\in\mathcal{A}$.
3. **Reduce to finite measure** via the $\sigma$-finite decomposition (split $A$ across the $X_k$).
4. **Truncate a convergent series** to pass from countable to finite.

---

# Hints

> [!note]- Hint 1
> By definition of the outer measure, $\mu(A)=\mu^*(A)$ is an *infimum* over algebra-covers. So for any $\varepsilon$ there is a cover $\bigcup_j K_j\supseteq A$, $K_j\in\mathcal{A}$, with $\sum_j\widetilde\mu(K_j)\le\mu(A)+\varepsilon$.

> [!note]- Hint 2
> First do the case $\mu(A)<\infty$. Then $\mu(\bigcup K_j)\le\sum\widetilde\mu(K_j)\le\mu(A)+\varepsilon$, so $\mu(\bigcup K_j\setminus A)\le\varepsilon$. Disjointify the $K_j$.

> [!note]- Hint 3
> For general $A$, split it by the $\sigma$-finite pieces: $A=\bigsqcup_k(A\cap X_k)$, each of finite measure; approximate each within $\varepsilon 2^{-k}$ and union the covers. For the finite single-set version, truncate the countable disjoint cover to $\bigcup_{n\le N}A_n$.

---

# Solution

**Step 1 — Finite-measure case.** Suppose $\mu(A)<\infty$. Since $\mu(A)=\mu^*(A)$ is an infimum over algebra-covers, pick $K_j\in\mathcal{A}$ with $A\subseteq\bigcup_j K_j$ and $\sum_j\widetilde\mu(K_j)\le\mu(A)+\varepsilon$.

> [!note]- Derivation
> By $\sigma$-subadditivity, $\mu(\bigcup_j K_j)\le\sum_j\mu(K_j)=\sum_j\widetilde\mu(K_j)\le\mu(A)+\varepsilon$. As $A\subseteq\bigcup_j K_j$ and $\mu(A)<\infty$,
> $$\mu\Big(\bigcup_j K_j\setminus A\Big)=\mu\Big(\bigcup_j K_j\Big)-\mu(A)\le\varepsilon.$$
> Now disjointify: $A_n=K_n\setminus\bigcup_{j<n}K_j\in\mathcal{A}$ are pairwise disjoint with $\bigcup_n A_n=\bigcup_j K_j$. This proves the countable statement when $\mu(A)<\infty$.

**Step 2 — General $A$ via $\sigma$-finiteness.** For arbitrary $A\in\sigma(\mathcal{A})$, write $X=\bigsqcup_k Y_k$ with $Y_k\in\mathcal{A}$, $\mu(Y_k)<\infty$ (disjointify the $X_k$). Each $A\cap Y_k$ has $\mu(A\cap Y_k)\le\mu(Y_k)<\infty$.

> [!note]- Derivation
> By Step 1 applied to $A\cap Y_k$ with tolerance $\varepsilon 2^{-k}$, get disjoint algebra sets $(A_{k,n})_n$ covering $A\cap Y_k$ with $\mu(\bigcup_n A_{k,n}\setminus(A\cap Y_k))<\varepsilon 2^{-k}$. Intersecting with $Y_k$ keeps them in $\mathcal{A}$ and disjoint across $k$. The full family $\{A_{k,n}\cap Y_k\}_{k,n}$ is countable, pairwise disjoint, covers $A=\bigsqcup_k(A\cap Y_k)$, and
> $$\mu\Big(\bigcup_{k,n}(A_{k,n}\cap Y_k)\setminus A\Big)\le\sum_k\mu\Big(\bigcup_n A_{k,n}\setminus(A\cap Y_k)\Big)<\sum_k\varepsilon 2^{-k}=\varepsilon.$$

**Step 3 — Finite single-set version.** Suppose $\mu(A)<\infty$. From Step 1 we have disjoint $A_n\in\mathcal{A}$ with $A\subseteq\bigcup_n A_n$ and $\mu(\bigcup_n A_n\setminus A)<\varepsilon/2$. Since $\mu(\bigcup_n A_n)\le\mu(A)+\varepsilon/2<\infty$, [[Thm - Properties of Measures|continuity from below]] gives $\mu(\bigcup_{n\le N}A_n)\uparrow\mu(\bigcup_n A_n)$, so for large $N$, $\mu(\bigcup_n A_n\setminus\bigcup_{n\le N}A_n)<\varepsilon/2$. Set $E=\bigcup_{n\le N}A_n\in\mathcal{A}$.

> [!note]- Derivation
> $E\setminus A\subseteq\bigcup_n A_n\setminus A$ has measure $<\varepsilon/2$. And $A\setminus E\subseteq\bigcup_{n>N}A_n=\bigcup_n A_n\setminus E$ has measure $<\varepsilon/2$. So $\mu(A\,\triangle\,E)=\mu(A\setminus E)+\mu(E\setminus A)<\varepsilon$.

> [!note]- Complete formal solution
> The outer measure is an inf over algebra-covers, so a near-optimal cover $\bigcup K_j\supseteq A$ with $\sum\widetilde\mu(K_j)\le\mu(A)+\varepsilon$ exists; for $\mu(A)<\infty$ this gives $\mu(\bigcup K_j\setminus A)\le\varepsilon$, and disjointifying $K_j$ yields the $A_n$. For general $A$, split by a disjoint $\sigma$-finite exhaustion $Y_k$ and approximate $A\cap Y_k$ within $\varepsilon 2^{-k}$; the union of covers works by $\sigma$-subadditivity. For the single-set version with $\mu(A)<\infty$, truncate the disjoint cover at finite $N$ (continuity from below makes the tail small) and take $E=\bigcup_{n\le N}A_n$, giving $\mu(A\triangle E)<\varepsilon$. $\blacksquare$

---

# Key Takeaways

**The generating algebra is "dense" in the generated $\sigma$-algebra — every measurable set is, up to arbitrarily small measure, a finite union of algebra sets.** This is the set-level form of the master principle of analysis: *prove things on the simple class, transport across a small gap*. To establish a property for all $A\in\sigma(\mathcal{A})$, establish it for $\mathcal{A}$ (where it is computable — boxes, elementary figures, intervals) and control the $\varepsilon$-gap. The same theorem with $\mathcal{A}=$ elementary figures *is* [[Thm - Regularity of Lebesgue Measure|regularity of Lebesgue measure]]; with $\mathcal{A}=$ a generating field of events it is the standard "approximate any event by a finite-information event" used throughout probability.

**Outer-measure infima hand you economical covers for free — that is what the infimum *means*.** Whenever a measure is the restriction of an outer measure (and by the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] essentially every measure one builds is), the statement "$\mu(A)=\inf\{\sum\widetilde\mu(K_j)\}$" is not a theorem to prove but a *resource to spend*: it produces, on demand, an algebra-cover overshooting $A$ by less than $\varepsilon$. The recurring moves around it — disjointify the cover, split by a $\sigma$-finite exhaustion, truncate the resulting series — are the standard plumbing for turning "countable cover" into "finite, disjoint, single set."
