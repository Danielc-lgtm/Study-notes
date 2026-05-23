---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Lp and L1 Martingale Convergence"
  - "Def - Conditional Expectation"
  - "Thm - Dynkin's π-λ Theorem"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $Z\in L^1(\Omega,\mathcal{F},\mathbb{P})$ and $(\mathcal{F}_n)$ a [[Def - Filtration|filtration]] with $\mathcal{F}_\infty=\sigma(\bigcup_n\mathcal{F}_n)$.

**(a) (Lévy's upward theorem.)** Show $\mathbb{E}[Z\mid\mathcal{F}_n]\to\mathbb{E}[Z\mid\mathcal{F}_\infty]$ almost surely and in $L^1$.

**(b) (Lévy's 0–1 law.)** Deduce that for $A\in\mathcal{F}_\infty$, $\mathbb{P}(A\mid\mathcal{F}_n)\to\mathbf{1}_A$ a.s. — partial information eventually resolves every event.

**(c)** Recover the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]] as a corollary for an independent sequence.

**Recall:**

[[Thm - Lp and L1 Martingale Convergence|Closed martingales]]: $\mathbb{E}[Z\mid\mathcal{F}_n]$ is a uniformly integrable martingale, converging a.s. and in $L^1$.

---

# Convergent Strategy

**Problem class:** identifying the limit of a *closed* martingale, then applying it to indicator variables.

**Assumption pattern:** $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ is a [[Thm - Lp and L1 Martingale Convergence|uniformly integrable martingale]] (conditional expectations of a fixed $Z$), so it converges a.s. and in $L^1$ — the only task is to *identify* the limit as $\mathbb{E}[Z\mid\mathcal{F}_\infty]$, via the averaging identity on the generating $\pi$-system $\bigcup_n\mathcal{F}_n$.

---

# Legal Operations Used

1. **Closed martingale $\Rightarrow$ a.s. + $L^1$ convergence.**
2. **Identify the limit** by the averaging identity on a $\pi$-system ([[Thm - Dynkin's π-λ Theorem|Dynkin]]).
3. **Specialise to $Z=\mathbf{1}_A$.**

---

# Hints

> [!note]- Hint 1
> $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ is a UI martingale, so $X_n\to X_\infty$ a.s. and in $L^1$ for some $X_\infty$.

> [!note]- Hint 2
> Identify $X_\infty$: it is $\mathcal{F}_\infty$-measurable, and for $A\in\mathcal{F}_m$, $\mathbb{E}[X_\infty\mathbf{1}_A]=\lim\mathbb{E}[X_n\mathbf{1}_A]=\mathbb{E}[Z\mathbf{1}_A]$. The sets $\bigcup_m\mathcal{F}_m$ are a $\pi$-system generating $\mathcal{F}_\infty$.

> [!note]- Hint 3
> (b): take $Z=\mathbf{1}_A$ with $A\in\mathcal{F}_\infty$; then $\mathbb{E}[Z\mid\mathcal{F}_\infty]=\mathbf{1}_A$.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) observes $X_n = \mathbb{E}[Z \mid \mathcal{F}_n]$ is a UI martingale (closed [[Def - Martingale|martingales]] are UI), so it converges a.s. and in $L^1$ to some $X_\infty$, then identifies $X_\infty = \mathbb{E}[Z \mid \mathcal{F}_\infty]$ via the averaging identity on the generating $\pi$-system $\bigcup_m \mathcal{F}_m$ and Dynkin's lemma; Step 2 (part b) specialises to $Z = \mathbf{1}_A$ for $A \in \mathcal{F}_\infty$, where the limit is $\mathbf{1}_A$; Step 3 (part c) recovers Kolmogorov by noting that for a tail event of an independent sequence, $\mathbb{P}(A \mid \mathcal{F}_n) = \mathbb{P}(A)$ is constant, which forces $\mathbf{1}_A = \mathbb{P}(A)$ a.s. The non-obvious move is in Step 1 — the identification of $X_\infty$ uses *Dynkin* to extend the averaging identity from the $\pi$-system to all of $\mathcal{F}_\infty$, which is what makes "closed martingale converges to the conditional expectation it closes to" rigorous.

**Step 1 — (a) Lévy's upward theorem.** $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ is a [[Thm - Lp and L1 Martingale Convergence|uniformly integrable]] martingale (conditional expectations of the fixed $Z\in L^1$), so $X_n\to X_\infty$ a.s. and in $L^1$ for some $X_\infty\in L^1$.

> [!note]- Derivation
> *Identify $X_\infty=\mathbb{E}[Z\mid\mathcal{F}_\infty]$.* $X_\infty$ is $\mathcal{F}_\infty$-measurable (a.s. limit of $\mathcal{F}_n$-measurable functions). For the averaging identity: fix $m$ and $A\in\mathcal{F}_m$. For $n\ge m$, the martingale/tower property gives $\mathbb{E}[X_n\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[Z\mid\mathcal{F}_n]\mathbf{1}_A]=\mathbb{E}[Z\mathbf{1}_A]$; $L^1$-convergence lets $n\to\infty$, so $\mathbb{E}[X_\infty\mathbf{1}_A]=\mathbb{E}[Z\mathbf{1}_A]$. This holds for all $A$ in the $\pi$-system $\bigcup_m\mathcal{F}_m$, which generates $\mathcal{F}_\infty$; by [[Thm - Dynkin's π-λ Theorem|Dynkin's lemma]] it extends to all $A\in\mathcal{F}_\infty$. So $X_\infty$ satisfies the [[Def - Conditional Expectation|characterisation]] of $\mathbb{E}[Z\mid\mathcal{F}_\infty]$ — by uniqueness, $X_\infty=\mathbb{E}[Z\mid\mathcal{F}_\infty]$.

So $\mathbb{E}[Z\mid\mathcal{F}_n]\to\mathbb{E}[Z\mid\mathcal{F}_\infty]$ a.s. and in $L^1$ — *as information accumulates, the conditional expectation converges to the fully-informed one.*

**Step 2 — (b) Lévy's 0–1 law.** Apply (a) to $Z=\mathbf{1}_A$ for $A\in\mathcal{F}_\infty$. Since $A\in\mathcal{F}_\infty$, $\mathbb{E}[\mathbf{1}_A\mid\mathcal{F}_\infty]=\mathbf{1}_A$. So
$$\mathbb{P}(A\mid\mathcal{F}_n)=\mathbb{E}[\mathbf{1}_A\mid\mathcal{F}_n]\xrightarrow{\text{a.s.}}\mathbf{1}_A.$$
The conditional probability of *any* $\mathcal{F}_\infty$-event, given the partial information $\mathcal{F}_n$, converges to $0$ or $1$ — the event is eventually *decided* by the accumulating information.

**Step 3 — (c) Kolmogorov 0–1 law.** Let $(Y_k)$ be independent, $\mathcal{F}_n=\sigma(Y_1,\dots,Y_n)$, and $A$ a [[Thm - Kolmogorov 0-1 Law|tail event]] — so $A\in\mathcal{F}_\infty$ but $A$ is *independent of each $\mathcal{F}_n$* (it depends only on coordinates beyond $n$). Independence gives $\mathbb{P}(A\mid\mathcal{F}_n)=\mathbb{P}(A)$, a constant. By (b), $\mathbb{P}(A\mid\mathcal{F}_n)\to\mathbf{1}_A$ a.s. A constant sequence equal to $\mathbb{P}(A)$ converging to $\mathbf{1}_A$ forces $\mathbf{1}_A=\mathbb{P}(A)$ a.s. — so $\mathbf{1}_A$ is a.s. constant, i.e. $\mathbb{P}(A)\in\{0,1\}$. The [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]] drops out.

> [!note]- Complete formal solution
> (a) $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ is a UI martingale, $X_n\to X_\infty$ a.s. and $L^1$; $X_\infty$ is $\mathcal{F}_\infty$-measurable with $\mathbb{E}[X_\infty\mathbf{1}_A]=\mathbb{E}[Z\mathbf{1}_A]$ on the generating $\pi$-system $\bigcup_m\mathcal{F}_m$, so (Dynkin, uniqueness) $X_\infty=\mathbb{E}[Z\mid\mathcal{F}_\infty]$. (b) $Z=\mathbf{1}_A$, $A\in\mathcal{F}_\infty$: $\mathbb{P}(A\mid\mathcal{F}_n)\to\mathbf{1}_A$ a.s. (c) For a tail event of an independent sequence, $\mathbb{P}(A\mid\mathcal{F}_n)=\mathbb{P}(A)$ constant; the limit $\mathbf{1}_A$ forces $\mathbb{P}(A)\in\{0,1\}$. $\blacksquare$

---

# Key Takeaways

**Lévy's upward theorem says conditional expectations converge as information accumulates: $\mathbb{E}[Z\mid\mathcal{F}_n]\to\mathbb{E}[Z\mid\mathcal{F}_\infty]$, a.s. and in $L^1$.** A *closed* martingale — one of the form $\mathbb{E}[Z\mid\mathcal{F}_n]$ — is automatically [[Def - Uniform Integrability|uniformly integrable]], so it converges; the work is *identifying* the limit, done by verifying the averaging identity on the generating $\pi$-system $\bigcup_n\mathcal{F}_n$ and invoking [[Thm - Dynkin's π-λ Theorem|Dynkin]] and uniqueness. This "the limit is the conditional expectation given the limit $\sigma$-algebra" is the dynamic content of the [[Thm - Lp and L1 Martingale Convergence|martingale convergence theorem]].

**Lévy's 0–1 law — $\mathbb{P}(A\mid\mathcal{F}_n)\to\mathbf{1}_A$ for $A\in\mathcal{F}_\infty$ — says accumulating information eventually *resolves* every event, and it contains the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]] as a special case.** The conditional probability of a future-determined event swings to $0$ or $1$ as the present catches up. For a *tail* event of an *independent* sequence, the conditional probability is *frozen* at the constant $\mathbb{P}(A)$ — yet it must converge to $\mathbf{1}_A$, and a constant equal to a $\{0,1\}$-valued limit must itself be $0$ or $1$. So the Kolmogorov 0–1 law is "Lévy's 0–1 law applied where the information is inert." Two of probability's deepest zero–one phenomena unified by the closed-martingale convergence theorem.
