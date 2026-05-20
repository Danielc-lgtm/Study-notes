---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Martingale"
  - "Thm - Optional Stopping Theorem"
  - "Thm - Fatou's Lemma"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ a [[Def - Martingale|martingale]] or supermartingale; $U_n[a,b]$ the number of upcrossings of an interval $[a,b]$ by $X_0,\dots,X_n$; $X_\infty=\lim X_n$.

---

# Motivation

The single most useful structural theorem about [[Def - Martingale|martingales]]: **an $L^1$-bounded martingale converges almost surely**. A fair game whose fortune stays bounded in expectation *settles down* — the trajectory has a definite limit, with probability one. This is the discrete-time analogue of the [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]] and the workhorse behind the [[Thm - Strong Law of Large Numbers|strong law of large numbers]], the convergence of [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] approximations, branching-process limits, and Pólya's-urn-type results. The proof rests on a beautiful gambling idea — **Doob's upcrossing lemma** — quantifying that a martingale cannot oscillate across an interval too many times.

---

# Sources and Targets

**Sources.** Hypothesis: $(X_n)$ a supermartingale (hence martingale) **bounded in $L^1$**: $\sup_n\mathbb{E}|X_n|<\infty$. For a *non-negative* supermartingale this is automatic ($\mathbb{E}|X_n|=\mathbb{E}X_n\le\mathbb{E}X_0$), so **every non-negative supermartingale converges a.s.**

**Targets.** A.s. convergence to a limit $X_\infty\in L^1$ ([[Thm - Fatou's Lemma|Fatou]] gives integrability). Note this is *only* a.s. convergence — *not* $L^1$ (the limit may have smaller expectation; mass can escape). Upgrading to $L^1$ needs [[Def - Uniform Integrability|uniform integrability]] ([[Thm - Lp and L1 Martingale Convergence|next theorem]]). Combined with the [[Thm - Strong Law of Large Numbers|backward-martingale]] machinery it yields the SLLN.

---

# Statement

Let $(X_n)$ be a supermartingale (in particular, a martingale) **bounded in $L^1$**: $\sup_n\mathbb{E}|X_n|<\infty$. Then there is an $\mathcal{F}_\infty$-measurable random variable $X_\infty\in L^1$ with
$$X_n\ \xrightarrow{\ \text{a.s.}\ }\ X_\infty\qquad\text{as }n\to\infty.$$
In particular, **every non-negative supermartingale converges almost surely**. (The convergence need not hold in $L^1$.)

---

# Why Is It True

A real sequence $(x_n)$ *fails* to converge in $[-\infty,\infty]$ exactly when it oscillates: for some rationals $a<b$ it drops below $a$ and rises above $b$ infinitely often — it makes *infinitely many upcrossings of $[a,b]$*. So to prove a.s. convergence it suffices to show, for every fixed pair $a<b$, that the martingale makes only finitely many upcrossings of $[a,b]$ almost surely.

**Doob's upcrossing lemma** bounds the *expected* number of upcrossings. The idea is a gambling strategy: *buy when the process drops to $a$, hold until it rises to $b$, then sit out.* This strategy is *predictable* (each decision uses only the past), so the resulting "gambler's fortune" is again a supermartingale ([[Thm - Optional Stopping Theorem|the stopped/transformed process]]). Each completed upcrossing earns the gambler at least $b-a$; the only loss is on an incomplete final upcrossing, at most $(X_n-a)^-$. Since a supermartingale game has non-positive expected gain,
$$(b-a)\,\mathbb{E}[U_n[a,b]]\ \le\ \mathbb{E}[(X_n-a)^-]\ \le\ |a|+\sup_n\mathbb{E}|X_n|.$$
Letting $n\to\infty$, $\mathbb{E}[U_\infty[a,b]]<\infty$ (using $L^1$-boundedness), so $U_\infty[a,b]<\infty$ **almost surely**.

Take the *union over all rational pairs* $a<b$ — countably many — of the null events $\{U_\infty[a,b]=\infty\}$: still null. Off this null set, the sequence $(X_n)$ has finitely many upcrossings of *every* rational interval, hence converges in $[-\infty,\infty]$. Finally $L^1$-boundedness rules out the limit being $\pm\infty$: by [[Thm - Fatou's Lemma|Fatou's lemma]], $\mathbb{E}|X_\infty|=\mathbb{E}[\liminf|X_n|]\le\liminf\mathbb{E}|X_n|\le\sup_n\mathbb{E}|X_n|<\infty$, so $X_\infty$ is a.s. finite and in $L^1$.

The slogan: **a sequence diverges iff it upcrosses some interval infinitely often; a "buy low, sell high" strategy turns each upcrossing into a guaranteed profit, but a supermartingale forbids expected profit — so the expected number of upcrossings is finite, hence upcrossings are a.s. finite, hence the martingale converges.** Doob's upcrossing lemma converts "no free lunch" into "no oscillation."

---

# What Makes This Hard

The genuinely clever step is the **upcrossing lemma** and its gambling interpretation — realising that "count the oscillations" is the right reformulation of convergence, and that a *predictable* buy-low/sell-high strategy is a [[Def - Martingale|martingale transform]] whose non-positive expected gain bounds the upcrossing count. After that, two routine but essential moves: *take a countable union over rational intervals* (uncountably many would not work — this is why rationals), and use [[Thm - Fatou's Lemma|Fatou]] to confirm the a.s. limit is finite. The classic warning: this is **a.s. convergence only** — the [[Thm - Lp and L1 Martingale Convergence|product martingale]] $X_n=\prod Y_k$ with $\mathbb{P}(Y_k=0)=\mathbb{P}(Y_k=2)=\tfrac12$ converges a.s. to $0$ while $\mathbb{E}X_n=1$, so $L^1$-convergence fails.

---

# Rederivation Scaffold

**High-level strategy.** "Diverges" $=$ "infinitely many upcrossings of some rational $[a,b]$." Bound $\mathbb{E}[U_n[a,b]]$ by Doob's upcrossing lemma (a buy-low/sell-high predictable strategy + supermartingale). $L^1$-boundedness $\Rightarrow U_\infty<\infty$ a.s.; union over rational pairs; Fatou for finiteness of the limit.

**Subgoal decomposition.**

1. **Convergence $\iff$ no infinite upcrossing.** $(x_n)$ converges in $[-\infty,\infty]$ iff $U_\infty[a,b]<\infty$ for all rational $a<b$.
2. **Upcrossing lemma.** $(b-a)\mathbb{E}[U_n[a,b]]\le\mathbb{E}[(X_n-a)^-]$ — buy-low/sell-high is a supermartingale transform.
3. **Finitely many upcrossings.** $L^1$-bounded $\Rightarrow\mathbb{E}[U_\infty[a,b]]<\infty\Rightarrow U_\infty[a,b]<\infty$ a.s.
4. **Conclude.** Countable union over rational $(a,b)$; off the null set $X_n\to X_\infty\in[-\infty,\infty]$; [[Thm - Fatou's Lemma|Fatou]] $\Rightarrow X_\infty\in L^1$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Doob's upcrossing lemma
> **Statement:** For a supermartingale $(X_n)$, $(b-a)\,\mathbb{E}[U_n[a,b]]\le\mathbb{E}[(X_n-a)^-]$.
>
> **Hint:** Buy when the process hits $a$, sell when it hits $b$ — a predictable strategy.
>
> **Why needed:** This converts the abstract supermartingale property into a quantitative bound on upcrossings, which is the only quantity a non-convergent sequence is forced to make infinite. Bounding $\mathbb{E}[U_n[a,b]]$ uniformly in $n$ rules out infinitely many oscillations across $[a,b]$, the only obstruction to convergence.
>
> > [!note]- Full proof
> > Define the predictable strategy $C_k\in\{0,1\}$: $C_k=1$ ("invested") if the process is, at time $k-1$, in an interval it entered below $a$ and has not yet pushed above $b$; $C_k=0$ otherwise. $C_k$ is $\mathcal{F}_{k-1}$-measurable. The gambler's fortune $G_n=\sum_{k=1}^n C_k(X_k-X_{k-1})$ is a [[Def - Martingale|martingale transform]] of a supermartingale by a non-negative predictable $C$, hence a supermartingale with $\mathbb{E}[G_n]\le\mathbb{E}[G_0]=0$. Each completed upcrossing of $[a,b]$ contributes $\ge(b-a)$ to $G_n$; an incomplete final upcrossing contributes $\ge-(X_n-a)^-$. So $G_n\ge(b-a)U_n[a,b]-(X_n-a)^-$. Take expectations: $0\ge\mathbb{E}[G_n]\ge(b-a)\mathbb{E}[U_n[a,b]]-\mathbb{E}[(X_n-a)^-]$. $\square$

> [!note]- Lemma 2: From finite upcrossings to convergence
> **Statement:** If $\sup_n\mathbb{E}|X_n|<\infty$, then $X_n$ converges a.s. to a finite limit.
>
> **Hint:** Lemma 1 plus the $L^1$-bound forces $\mathbb{E}[U_\infty[a,b]]<\infty$ for every rational pair $a<b$; outside the countable union of null sets where some $U_\infty[a,b]=\infty$, oscillation across every rational interval is finite, so $X_n$ has a limit. Fatou keeps the limit in $L^1$ hence a.s. finite.
>
> **Why needed:** This is the main theorem — Lemma 1 provides the inequality, but Lemma 2 actually performs the "no infinite oscillation across rationals $\Rightarrow$ pointwise limit exists" argument that concludes a.s. convergence to a finite limit. It is the input-broadening step that turns Doob's quantitative bound into the qualitative convergence statement.
>
> > [!note]- Full proof
> > By Lemma 1 and $(X_n-a)^-\le|X_n|+|a|$, $(b-a)\mathbb{E}[U_n[a,b]]\le\sup_n\mathbb{E}|X_n|+|a|<\infty$; monotone convergence gives $\mathbb{E}[U_\infty[a,b]]<\infty$, so $U_\infty[a,b]<\infty$ a.s. The union $N=\bigcup_{a<b\text{ rational}}\{U_\infty[a,b]=\infty\}$ is a countable union of null sets, null. Off $N$, $(X_n)$ upcrosses no rational interval infinitely often, so $X_n\to X_\infty\in[-\infty,\infty]$. By [[Thm - Fatou's Lemma|Fatou]], $\mathbb{E}|X_\infty|\le\liminf\mathbb{E}|X_n|<\infty$, so $X_\infty\in L^1$, a.s. finite. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 (upcrossing lemma) bounds $\mathbb{E}[U_n[a,b]]$; Lemma 2 uses $L^1$-boundedness to deduce $U_\infty[a,b]<\infty$ a.s. for every rational pair, takes the countable union of exceptional null sets, concludes $X_n\to X_\infty$ a.s., and applies [[Thm - Fatou's Lemma|Fatou]] for $X_\infty\in L^1$. A non-negative supermartingale has $\mathbb{E}|X_n|=\mathbb{E}X_n\le\mathbb{E}X_0$, automatically $L^1$-bounded. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The convergence theorem proves the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] (for a countably generated $\sigma$-algebra: the approximating densities form a UI martingale), gives Kolmogorov's three-series theorem, and — via [[Thm - Strong Law of Large Numbers|backward martingales]] — the strong law of large numbers. Pólya's urn proportion is a bounded martingale, so it converges a.s. (to a random Beta-distributed limit). It is the discrete sibling of [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation]].

---

# Bridges

- **[[Thm - Optional Stopping Theorem]]** — the buy-low/sell-high strategy is a martingale transform; its supermartingale property is optional stopping in disguise.
- **[[Thm - Lp and L1 Martingale Convergence]]** — upgrades a.s. convergence to $L^1$/$L^p$ under uniform integrability / $L^p$-boundedness.
- **[[Thm - Doob's Maximal Inequality]]** — the companion control of the trajectory's *maximum*.
