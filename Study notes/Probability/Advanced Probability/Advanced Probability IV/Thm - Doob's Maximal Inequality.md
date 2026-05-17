---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Martingale"
  - "Thm - Optional Stopping Theorem"
  - "Thm - Hölder and Minkowski Inequalities"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ a [[Def - Martingale|martingale]] or non-negative submartingale; $X_n^*=\max_{k\le n}|X_k|$ the running maximum; $\lambda>0$.

---

# Motivation

[[Ex - Markov's inequality|Markov's inequality]] bounds the tail of a *single* random variable $X_n$ by $\mathbb{E}|X_n|$. Doob's maximal inequality does something far stronger: it bounds the tail of the **running maximum** $X_n^*=\max_{k\le n}|X_k|$ — the *worst value over the whole history* — by the *same* $\mathbb{E}|X_n|$, the final term alone. The entire trajectory is controlled by the endpoint. The $L^p$ version then bounds $\|X_n^*\|_p$ by $\|X_n\|_p$ (up to $\frac{p}{p-1}$). These inequalities are the engine of the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorems]] and the discrete twin of the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal inequality]].

---

# Sources and Targets

**Sources.** Hypotheses: $(X_n)$ a martingale, or a *non-negative* submartingale (then $|X_n|$ may be dropped). By [[Thm - Properties of Conditional Expectation|conditional Jensen]], $|X_n|$ is a submartingale when $X_n$ is a martingale — so the non-negative-submartingale form is the general one.

**Targets.** The maximal inequality $\lambda\,\mathbb{P}(X_n^*\ge\lambda)\le\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]$ feeds the **upcrossing argument** and hence [[Thm - Almost Sure Martingale Convergence|a.s. convergence]]; the $L^p$ inequality $\|X_n^*\|_p\le\frac{p}{p-1}\|X_n\|_p$ feeds [[Thm - Lp and L1 Martingale Convergence|Lᵖ-convergence]] of martingales and the Burkholder–Davis–Gundy inequalities.

---

# Formal Statement

Let $(X_n)$ be a martingale or a non-negative submartingale, $X_n^*=\max_{k\le n}|X_k|$.

**(Maximal inequality, weak-type.)** For every $\lambda>0$,
$$\lambda\,\mathbb{P}(X_n^*\ge\lambda)\ \le\ \mathbb{E}\big[|X_n|\,\mathbf{1}_{\{X_n^*\ge\lambda\}}\big]\ \le\ \mathbb{E}|X_n|.$$

**(Doob's $L^p$ inequality.)** For $1<p<\infty$,
$$\|X_n^*\|_p\ \le\ \frac{p}{p-1}\,\|X_n\|_p.$$

(The $L^p$ inequality fails at $p=1$ — only the weak-type bound holds there, as for the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal function]].)

---

# Why Is It True

**Maximal inequality — a stopping-time argument.** The event $\{X_n^*\ge\lambda\}$ is "$|X_k|$ reaches $\lambda$ at *some* $k\le n$." Introduce the [[Def - Stopping Time|stopping time]] $T=\inf\{k:|X_k|\ge\lambda\}$ — the first time the level is breached. On $\{X_n^*\ge\lambda\}$, $T\le n$ and $|X_T|\ge\lambda$. Now $|X_n|$ is a non-negative submartingale, so by [[Thm - Optional Stopping Theorem|optional stopping]] (submartingale form, applied to the bounded times $T\wedge n\le n$), $\mathbb{E}[|X_n|\mid\mathcal{F}_{T\wedge n}]\ge|X_{T\wedge n}|$, hence $\mathbb{E}[|X_n|\mathbf{1}_{\{T\le n\}}]\ge\mathbb{E}[|X_T|\mathbf{1}_{\{T\le n\}}]\ge\lambda\,\mathbb{P}(T\le n)=\lambda\,\mathbb{P}(X_n^*\ge\lambda)$. The slogan: **the first-passage time across level $\lambda$ is a stopping time; optional stopping says the submartingale, observed at that time, is on average no less than the endpoint — and at that time it is $\ge\lambda$.**

**$L^p$ inequality — the layer-cake plus Hölder.** Integrate the maximal inequality against the [[Ex - The area under a graph|layer-cake]] representation $\mathbb{E}[(X_n^*)^p]=\int_0^\infty p\lambda^{p-1}\mathbb{P}(X_n^*\ge\lambda)\,d\lambda$. The maximal inequality bounds $\mathbb{P}(X_n^*\ge\lambda)\le\lambda^{-1}\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]$, so by [[Thm - Fubini-Tonelli Theorem|Fubini]],
$$\mathbb{E}[(X_n^*)^p]\le\int_0^\infty p\lambda^{p-2}\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]\,d\lambda=\tfrac{p}{p-1}\,\mathbb{E}\big[|X_n|\,(X_n^*)^{p-1}\big].$$
Apply [[Thm - Hölder and Minkowski Inequalities|Hölder]] with exponents $p$ and $q=\tfrac{p}{p-1}$: $\mathbb{E}[|X_n|(X_n^*)^{p-1}]\le\|X_n\|_p\,\|(X_n^*)^{p-1}\|_q=\|X_n\|_p\,\|X_n^*\|_p^{p-1}$. Substituting, $\|X_n^*\|_p^p\le\tfrac{p}{p-1}\|X_n\|_p\|X_n^*\|_p^{p-1}$; divide by $\|X_n^*\|_p^{p-1}$ (finite, as the max of finitely many $L^p$ variables). The constant $\frac{p}{p-1}$ blows up as $p\downarrow1$ — which is why there is no $L^1$ version.

---

# What Makes This Hard

The maximal inequality's idea — *the first-passage time is a stopping time, feed it to [[Thm - Optional Stopping Theorem|optional stopping]]* — is the non-obvious move; once seen, it is two lines. For the $L^p$ inequality the subtleties are: writing $\mathbb{E}[(X_n^*)^p]$ via the [[Ex - The area under a graph|layer-cake formula]] (so the maximal inequality can be integrated in), and applying [[Thm - Hölder and Minkowski Inequalities|Hölder]] with the *conjugate* exponent so that $(X_n^*)^{p-1}$ lands in $L^q$ — this needs $(p-1)q=p$. The division at the end requires $\|X_n^*\|_p<\infty$, true since $X_n^*$ is a max of finitely many $L^p$ variables. The $p=1$ failure is structural, not fixable.

---

# Rederivation Scaffold

**High-level strategy.** Maximal: first-passage stopping time $+$ submartingale optional stopping. $L^p$: layer-cake $\mathbb{E}[(X_n^*)^p]=\int p\lambda^{p-1}\mathbb{P}(X_n^*\ge\lambda)$, insert the maximal bound, Hölder, divide.

**Subgoal decomposition.**

1. **Maximal inequality.** $T=\inf\{k:|X_k|\ge\lambda\}$; on $\{X_n^*\ge\lambda\}$, $T\le n$, $|X_T|\ge\lambda$; submartingale optional stopping gives $\lambda\mathbb{P}(X_n^*\ge\lambda)\le\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]$.
2. **Layer-cake.** $\mathbb{E}[(X_n^*)^p]=\int_0^\infty p\lambda^{p-1}\mathbb{P}(X_n^*\ge\lambda)\,d\lambda$.
3. **Insert and Fubini.** $\le\frac{p}{p-1}\mathbb{E}[|X_n|(X_n^*)^{p-1}]$.
4. **Hölder, divide.** Exponents $p,q$: $\|X_n^*\|_p^p\le\frac{p}{p-1}\|X_n\|_p\|X_n^*\|_p^{p-1}$; divide.

---

# Lemma Decomposition

> [!note]- Lemma 1: The weak-type maximal inequality
> **Statement:** $\lambda\,\mathbb{P}(X_n^*\ge\lambda)\le\mathbb{E}[|X_n|\mathbf{1}_{\{X_n^*\ge\lambda\}}]$.
>
> > [!note]- Full proof
> > $|X_n|$ is a non-negative submartingale ([[Thm - Properties of Conditional Expectation|conditional Jensen]] if $X_n$ is a martingale). Let $T=\inf\{k:|X_k|\ge\lambda\}$, a [[Def - Stopping Time|stopping time]]; $A:=\{X_n^*\ge\lambda\}=\{T\le n\}\in\mathcal{F}_n$, and on $A$, $|X_T|\ge\lambda$. By the submartingale [[Thm - Optional Stopping Theorem|optional stopping]] inequality at the bounded times $T\wedge n\le n$, $\mathbb{E}[|X_n|\mathbf{1}_A]\ge\mathbb{E}[|X_{T\wedge n}|\mathbf{1}_A]=\mathbb{E}[|X_T|\mathbf{1}_A]\ge\lambda\,\mathbb{P}(A)$. $\square$

> [!note]- Lemma 2: Doob's $L^p$ inequality
> **Statement:** $\|X_n^*\|_p\le\frac{p}{p-1}\|X_n\|_p$ for $1<p<\infty$.
>
> > [!note]- Full proof
> > By the [[Ex - The area under a graph|layer-cake formula]], $\mathbb{E}[(X_n^*)^p]=\int_0^\infty p\lambda^{p-1}\mathbb{P}(X_n^*\ge\lambda)\,d\lambda$. Insert Lemma 1, $\mathbb{P}(X_n^*\ge\lambda)\le\lambda^{-1}\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]$, and apply [[Thm - Fubini-Tonelli Theorem|Fubini]]: $\mathbb{E}[(X_n^*)^p]\le\int_0^\infty p\lambda^{p-2}\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]\,d\lambda=\mathbb{E}[|X_n|\int_0^{X_n^*}p\lambda^{p-2}d\lambda]=\frac{p}{p-1}\mathbb{E}[|X_n|(X_n^*)^{p-1}]$. [[Thm - Hölder and Minkowski Inequalities|Hölder]] with $p,q=\frac{p}{p-1}$: $\le\frac{p}{p-1}\|X_n\|_p\|X_n^*\|_p^{p-1}$. Divide by $\|X_n^*\|_p^{p-1}<\infty$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 is the maximal inequality; the second "$\le\mathbb{E}|X_n|$" drops the indicator. Lemma 2 is the $L^p$ inequality. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Doob's maximal inequality is the *discrete-time, martingale* version of the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal inequality]] — both control a supremum by an endpoint norm, both are weak-type at $p=1$ and strong for $p>1$, both prove an a.e./a.s. convergence theorem by squeezing an exceptional set. In finance it bounds the running maximum of a discounted price; in statistics it underlies the law of the iterated logarithm and concentration for martingale-difference sequences.

---

# Bridges

- **[[Thm - Optional Stopping Theorem]]** — the first-passage stopping time and optional stopping are the engine of the maximal inequality.
- **[[Thm - Almost Sure Martingale Convergence]]** — the maximal inequality controls the trajectory; combined with the upcrossing lemma it gives a.s. convergence.
- **[[Def - Hardy-Littlewood Maximal Function]]** — the analyst's twin; same weak-type/strong-type structure.
- **[[Thm - Lp and L1 Martingale Convergence]]** — the $L^p$ inequality gives the uniform $L^p$-bound for $X^*$ that drives $L^p$-convergence.
