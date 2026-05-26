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

**Sources (Input Broadening)**

The literal hypothesis is "$(X_n)$ a non-negative submartingale" — a narrow-looking class. In practice almost every interesting trajectory-control problem can be reshaped into a non-negative submartingale, and the work is recognising the disguise.

The first source is **any martingale $(M_n)$ via the convex transform $|M_n|^p$ for $p\ge1$**. The map $x\mapsto|x|^p$ is convex on $\mathbb{R}$, so [[Thm - Properties of Conditional Expectation|conditional Jensen]] gives $\mathbb{E}[|M_{n+1}|^p\mid\mathcal{F}_n]\ge|\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]|^p=|M_n|^p$ — exactly the non-negative submartingale property. The bridge $B\to A$ is "any martingale, transformed by $|\cdot|^p$, becomes a non-negative submartingale." A concrete example: a centered random walk $S_n=\xi_1+\cdots+\xi_n$ with $\mathbb{E}\xi_k=0$ is a martingale, but the question one cares about is "how big does $\sup_{k\le n}|S_k|$ get?" Applying the maximal inequality to $|S_n|$ directly gives $\lambda\,\mathbb{P}(\max_{k\le n}|S_k|\ge\lambda)\le\mathbb{E}|S_n|$, the [[Thm - Kolmogorov Maximal Inequality|Kolmogorov maximal inequality]] for sums of independent centered variables. Applying it to $|S_n|^2$ gives Kolmogorov's $L^2$ form $\lambda^2\,\mathbb{P}(\max|S_k|\ge\lambda)\le\mathbb{E}S_n^2=\sum\mathrm{Var}(\xi_k)$ — the cornerstone of [[Thm - Strong Law of Large Numbers|Kolmogorov's strong law]].

The second source is **any supermartingale $(Y_n)$ via the reversal $-Y_n$, restricted to the non-negative case**. A non-negative supermartingale is not a submartingale, but one frequently has a non-negative submartingale arising as $f(Y_n)$ for $f$ convex and increasing (e.g.\ $f(y)=e^{\alpha y}$ with $\alpha>0$ for an [[Def - Exponential Martingale|exponential supermartingale]] reversed) when $Y_n$ has the right monotonicity. The bridge $B\to A$ is: take a convex, non-decreasing transform that flips the supermartingale to a submartingale, then apply Doob. A concrete example: the trajectory bound for a non-negative supermartingale, $\lambda\,\mathbb{P}(\sup_{k\le n}Y_k\ge\lambda)\le\mathbb{E}Y_0$ (note the $0$, not $n$ — the *initial* value bounds the maximum), is itself a maximal inequality, derivable by first-passage stopping. This is the form one needs for [[Thm - Almost Sure Martingale Convergence|Doob's supermartingale convergence]] proofs and for controlling the maximum of Markov chain potentials.

The third source is **any $L^p$-bounded martingale or martingale-difference sum**, where $|M_n|^p$ is the submartingale to feed in. Here "$L^p$-bounded" means $\sup_n\mathbb{E}|M_n|^p<\infty$, and applying the $L^p$ inequality to the submartingale $|M_n|^p$ yields $\|M^*_n\|_p\le\frac{p}{p-1}\|M_n\|_p$ — the running maximum is in $L^p$ with the same uniform bound (up to the $p/(p-1)$ constant). The bridge $B\to A$ is the conjunction of conditional Jensen plus a uniform $L^p$-norm bound. A concrete example: a square-integrable martingale-difference sequence $\sum\Delta M_k$ with $\sum\mathbb{E}\Delta M_k^2<\infty$ has $\sup_n\mathbb{E}M_n^2<\infty$, and Doob's $L^2$ inequality gives $\mathbb{E}[\sup_n M_n^2]\le 4\sup_n\mathbb{E}M_n^2<\infty$. This is the input to the [[Thm - Burkholder-Davis-Gundy Inequalities|Burkholder–Davis–Gundy inequalities]] and the canonical control of stochastic-integral trajectories.

**Targets (Output Amplification)**

The bare conclusions are the weak-type bound and the $L^p$ bound on $X_n^*$. The amplifications turn endpoint control into trajectory control, the form actually used in convergence theorems and concentration arguments.

The first amplification combines the maximal inequality with **the Cauchy criterion for a.s.\ and $L^p$-convergence**. For a martingale $(M_n)$ with $\sup_n\mathbb{E}|M_n|^p<\infty$ ($p>1$), Doob's $L^p$ inequality bounds $\|\sup_{k\le n}|M_k-M_m|\|_p$ by $\frac{p}{p-1}\|M_n-M_m\|_p$ — *the running maximum of the increment martingale is controlled in $L^p$ by its endpoint*. Combined with $\|M_n-M_m\|_p\to0$ (the $L^p$ Cauchy property, which follows from $L^p$-boundedness via [[Thm - Almost Sure Martingale Convergence|a.s.\ convergence]] and Fatou), this gives $\sup_{k>m}|M_k-M_m|\to0$ in $L^p$ and hence in probability. The combination is non-obvious because $L^p$-Cauchy of the *endpoint* differences is a much weaker statement than $L^p$-control of the *trajectory's worst deviation* — Doob's inequality is precisely the bridge. This is how the maximal inequality enters every $L^p$-martingale convergence proof, including [[Thm - Lp and L1 Martingale Convergence|Doob's Lᵖ convergence theorem]] giving $M_n\to M_\infty$ in $L^p$.

The second amplification combines the $L^p$ inequality with **the strong-type bound on the limit's supremum**: $\|\sup_n M_n\|_p\le\frac{p}{p-1}\|M_\infty\|_p$ for an $L^p$-bounded martingale. The amplification is "endpoint $L^p$-bound + Doob + monotone convergence = $L^p$-bound on the *entire-history* supremum." This is the discrete-martingale form of the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood inequality]] for the maximal function of an $L^p$-function, and it underlies the boundedness of the martingale maximal operator on $L^p$. Applied to the [[Def - Brownian Motion|Brownian]] discrete-time skeleton, it gives $\mathbb{E}[\sup_{t\le T}B_t^2]\le 4\mathbb{E}B_T^2=4T$ — a uniform path bound that no single-time inequality could produce. This is the central tool for proving tightness of martingale sequences and continuity of stochastic-integral paths.

The third amplification combines the maximal inequality with **exponential martingales and Cramér-type generating functions** to obtain concentration inequalities. For a martingale $(M_n)$ with bounded increments $|\Delta M_k|\le c$, the process $Z_n=\exp(\alpha M_n-\frac12\alpha^2 c^2 n)$ is a non-negative supermartingale (Azuma's exponential martingale). Doob's maximal inequality applied to $Z_n$ gives $\mathbb{P}(\sup_{k\le n}M_k\ge\lambda)\le e^{-\alpha\lambda+\frac12\alpha^2c^2n}$; optimising $\alpha=\lambda/(c^2n)$ yields $\mathbb{P}(\sup_{k\le n}M_k\ge\lambda)\le\exp(-\lambda^2/(2c^2 n))$ — [[Thm - Azuma-Hoeffding Inequality|Azuma–Hoeffding]] with the supremum on the left, not just $M_n$. The combination is non-obvious because Azuma's standard proof gives a tail bound on $M_n$ alone; Doob's inequality upgrades the bound *for free* to the entire-history supremum, which is what concentration-of-measure arguments actually need in machine learning (online learning regret bounds), in random graph theory (subgraph counts), and in stochastic optimisation (running-max guarantees on iterates).

---

# Statement

Let $(X_n)$ be a [[Def - Martingale|martingale]] or a non-negative submartingale, $X_n^*=\max_{k\le n}|X_k|$.

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
> **Hint:** Stop at $T=\inf\{k:|X_k|\ge\lambda\}$; on the bad event $\{X_n^*\ge\lambda\}=\{T\le n\}$, optional stopping for the submartingale $|X_k|$ at the bounded time $T\wedge n$ gives the lower bound $\mathbb{E}[|X_n|\mathbf{1}_{\{T\le n\}}]\ge\lambda\,\mathbb{P}(T\le n)$.
>
> **Why needed:** This is the weak-$(1,1)$-type maximal inequality — it controls the *probability* of the maximum being large by an expectation, which is the kind of fact one would normally need much finer structure for. The whole $L^p$ inequality is built by integrating it via layer-cake.
>
> > [!note]- Full proof
> > $|X_n|$ is a non-negative submartingale ([[Thm - Properties of Conditional Expectation|conditional Jensen]] if $X_n$ is a martingale). Let $T=\inf\{k:|X_k|\ge\lambda\}$, a [[Def - Stopping Time|stopping time]]; $A:=\{X_n^*\ge\lambda\}=\{T\le n\}\in\mathcal{F}_n$, and on $A$, $|X_T|\ge\lambda$. By the submartingale [[Thm - Optional Stopping Theorem|optional stopping]] inequality at the bounded times $T\wedge n\le n$, $\mathbb{E}[|X_n|\mathbf{1}_A]\ge\mathbb{E}[|X_{T\wedge n}|\mathbf{1}_A]=\mathbb{E}[|X_T|\mathbf{1}_A]\ge\lambda\,\mathbb{P}(A)$. $\square$

> [!note]- Lemma 2: Doob's $L^p$ inequality
> **Statement:** $\|X_n^*\|_p\le\frac{p}{p-1}\|X_n\|_p$ for $1<p<\infty$.
>
> **Hint:** Use the layer-cake formula $\mathbb{E}[(X_n^*)^p]=\int_0^\infty p\lambda^{p-1}\mathbb{P}(X_n^*\ge\lambda)\,d\lambda$, insert Lemma 1, swap order of integration (Fubini), and finish with Hölder using conjugate exponents $(p,p/(p-1))$.
>
> **Why needed:** This is what makes $X_n\mapsto X_n^*$ a bounded operator on $L^p$ for $1<p<\infty$ — exactly the right tool for $L^p$-martingale convergence (where it controls the maximal function by the terminal $L^p$-norm) and for Burkholder-Davis-Gundy-type inequalities.
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
