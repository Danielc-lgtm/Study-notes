---
type: topic
subject: advanced-probability
chapter: "4.1-4.3"
title: "Advanced Probability IV — Martingales in Discrete Time"
tags: [probability, advanced-probability]
---

# Notation Registry

- $(\Omega,\mathcal{F},(\mathcal{F}_n)_{n\ge0},\mathbb{P})$ — a [[Def - Filtration|filtered probability space]]; $\mathcal{F}_\infty=\sigma(\bigcup_n\mathcal{F}_n)$
- $(X_n),(M_n)$ — stochastic processes; **adapted**, **predictable**, **integrable** as in [[Def - Filtration]]
- [[Def - Martingale|martingale]]: $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$; **supermartingale** ($\le$), **submartingale** ($\ge$)
- $T,S$ — [[Def - Stopping Time|stopping times]] ($\{T\le n\}\in\mathcal{F}_n$); $X_n^T=X_{T\wedge n}$ — stopped process; $\mathcal{F}_T$ — stopping-time $\sigma$-algebra
- $X_n^*=\max_{k\le n}|X_k|$ — running maximum; $U_n[a,b]$ — number of upcrossings
- $X_\infty=\lim X_n$ — the a.s. (and, when UI, $L^1$) limit
- $X_n=X_0+M_n+A_n$ — the [[Ex - The Doob decomposition|Doob decomposition]] (martingale $+$ predictable)

---

# Motivation

A **martingale** models a *fair game*: a process whose expected future value, given everything known so far, equals its present value, $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$. It is [[Def - Conditional Expectation|conditional expectation]] set in motion — the [[Thm - Properties of Conditional Expectation|tower property]] indexed by an increasing [[Def - Filtration|filtration]] of information.

Three features make martingales the central objects of dynamic probability. They arise *everywhere* — sums of independent mean-zero variables, products of independent mean-one variables, conditional expectations $\mathbb{E}[Z\mid\mathcal{F}_n]$ of a fixed variable, [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] densities, harmonic functions of Markov chains. They are *remarkably regular*: the [[Thm - Optional Stopping Theorem|optional stopping theorem]] says fairness survives stopping at a random ([[Def - Stopping Time|non-anticipating]]) time; [[Thm - Doob's Maximal Inequality|Doob's inequalities]] bound the whole trajectory by its endpoint; the [[Thm - Almost Sure Martingale Convergence|convergence theorems]] say an $L^1$-bounded martingale *settles down* almost surely. And they *unify* — the [[Thm - Strong Law of Large Numbers|strong law]], the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]], the [[Thm - Kolmogorov 0-1 Law|0–1 laws]], and the convergence of conditional expectations are all martingale theorems.

The chapter develops the calculus: the [[Def - Filtration|filtration]] (accumulating information), the [[Def - Martingale|martingale]] (fair game), the [[Def - Stopping Time|stopping time]] (a non-anticipating decision); then the three pillars — [[Thm - Optional Stopping Theorem|optional stopping]] (compute hitting probabilities and times), [[Thm - Doob's Maximal Inequality|Doob's inequalities]] (control the maximum), and [[Thm - Almost Sure Martingale Convergence|convergence]] (a.s., and — under [[Def - Uniform Integrability|uniform integrability]] — in $L^1$).

---

# Concept Map

## §4.1 Filtrations and Martingales

- **[[Def - Filtration]]**
	- An increasing chain $\mathcal{F}_0\subseteq\mathcal{F}_1\subseteq\cdots$ of sub-$\sigma$-algebras — accumulating information. A process is *adapted* if observable by its time, *predictable* if known one step early. The stage for all dynamic probability.
- **[[Def - Martingale]]**
	- An adapted integrable process with $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$ — a fair game; super-/sub- for unfavourable/favourable. Conditional expectation iterated along a filtration; the tower property in motion. A convex function of a martingale is a submartingale.

> [!note] Exercise Index — §4.1
> [[Exercise Index - §4.1 Filtrations and Martingales]]

## §4.2 Stopping Times and Optional Stopping

- **[[Def - Stopping Time]]**
	- A random time $T$ with $\{T\le n\}\in\mathcal{F}_n$ — decidable from current information, non-anticipating. Hitting times are stopping times; last-exit times are not. The stopped process and $\mathcal{F}_T$ are built on it.
- **[[Thm - Optional Stopping Theorem]]**
	- A martingale stopped at a stopping time is a martingale; for $T$ bounded (or a.s. finite with the stopped process uniformly integrable), $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ — fairness survives random stopping. The tool that computes hitting probabilities and times.

> [!note] Exercise Index — §4.2
> [[Exercise Index - §4.2 Stopping Times and Optional Stopping]]

## §4.3 Martingale Convergence Theorems

- **[[Thm - Doob's Maximal Inequality]]**
	- $\lambda\,\mathbb{P}(X_n^*\ge\lambda)\le\mathbb{E}[|X_n|\mathbf{1}_{X_n^*\ge\lambda}]$ and $\|X_n^*\|_p\le\frac{p}{p-1}\|X_n\|_p$ ($p>1$) — the running maximum is controlled by the endpoint. Proved by a first-passage stopping time; the discrete twin of the Hardy–Littlewood maximal inequality.
- **[[Thm - Almost Sure Martingale Convergence]]**
	- An $L^1$-bounded (super)martingale converges almost surely. Proved by Doob's upcrossing lemma — a buy-low/sell-high strategy makes oscillations into profit, which a fair game forbids. Every non-negative supermartingale converges a.s.
- **[[Thm - Lp and L1 Martingale Convergence]]**
	- Upgrades a.s. convergence to $L^p$ (if $L^p$-bounded, $p>1$) or to $L^1$ (iff [[Def - Uniform Integrability|uniformly integrable]]). The UI martingales are exactly the closed ones, $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$.

> [!note] Exercise Index — §4.3
> [[Exercise Index - §4.3 Martingale Convergence]]

---

# Sources and Targets

**Targets — What do we prove?** (1) *That a process is a (sub/super)martingale* — by checking $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]$ vs $X_n$. (2) *Hitting probabilities and expected hitting times* — by optional stopping on the right martingale. (3) *Trajectory bounds* — control of the running maximum, via Doob. (4) *Almost-sure and $L^p$/$L^1$ convergence* of a martingale, and the *identification of the limit*. (5) Classical theorems — the [[Thm - Strong Law of Large Numbers|SLLN]], [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]], the [[Thm - Kolmogorov 0-1 Law|0–1 laws]] — recast and proved as martingale statements.

**Sources — What do we leverage?** *A filtration* is the standing structure. *Independence of an increment from the past* is what makes sums/products of independent variables martingales. *A bounded or $L^1$-bounded martingale* routes to a.s. convergence; *$L^p$-boundedness ($p>1$) or [[Def - Uniform Integrability|uniform integrability]]* upgrades to norm convergence. *A bounded stopping time, or a uniformly integrable stopped process* is the hypothesis of optional stopping. *Convexity* turns martingales into submartingales (the input to Doob). The skill is recognising these — and *manufacturing* a martingale (a [[Ex - The Doob decomposition|compensated process]], an exponential martingale) when the process at hand is not one.

---

# Legal Operations

1. **Verify the martingale property.** Split $X_{n+1}$ into a $\mathcal{F}_n$-measurable part (taken out) and an independent increment (averaged); check $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$.

2. **Manufacture a martingale.** When the process is not a martingale, build one: subtract the [[Ex - The Doob decomposition|predictable compensator]] ($S_n^2\to S_n^2-n\sigma^2$), or form the exponential martingale $e^{uS_n}/\mathbb{E}[e^{uX}]^n$, or apply a convex $\varphi$ to get a submartingale.

3. **Apply optional stopping.** For a hitting/exit problem, apply [[Thm - Optional Stopping Theorem|optional stopping]] to a suitable martingale at the stopping time — $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ — and solve, using the boundary values of $X_T$. Check the boundedness/UI hypothesis.

4. **Use $S_n$ for probabilities, $S_n^2-n\sigma^2$ for times.** The two random-walk martingales give two equations: the first solves a hitting probability, the second (once the probability is known) an expected hitting time.

5. **Bound the trajectory by the endpoint.** [[Thm - Doob's Maximal Inequality|Doob's inequalities]] control $X_n^*=\max_{k\le n}|X_k|$ by $\mathbb{E}|X_n|$ or $\|X_n\|_p$ — the route to a.s. convergence and to $L^p$-control of $\sup_n|X_n|$.

6. **Conclude a.s. convergence.** An $L^1$-bounded (super)martingale — in particular *any non-negative supermartingale*, or *any bounded martingale* — converges a.s. by the [[Thm - Almost Sure Martingale Convergence|convergence theorem]].

7. **Upgrade to $L^1$/$L^p$.** A.s. convergence becomes $L^p$ ($p>1$) under $L^p$-boundedness, or $L^1$ under [[Def - Uniform Integrability|uniform integrability]] — and then $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$, the martingale is *closed*.

8. **Take the limit of conditional expectations.** $\mathbb{E}[Z\mid\mathcal{F}_n]\to\mathbb{E}[Z\mid\mathcal{F}_\infty]$ ([[Ex - Closed martingales and Levy's 0-1 law|Lévy's upward theorem]]) — to evaluate or compare limits of conditional expectations.

**Illegal but tempting operations:**

> [!warning] 1. Applying optional stopping without a boundedness/UI hypothesis
> $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ needs $T$ *bounded*, or the stopped process *uniformly integrable*. The first hitting time of level $1$ by a fair walk is a.s. finite yet $\mathbb{E}[X_T]=1\neq0$ — see [[Ex - Optional stopping fails for unbounded times]]. The doubling strategy is the eternal warning.

> [!warning] 2. Concluding $L^1$-convergence from a.s. convergence
> The [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] gives *only* a.s. convergence; $\mathbb{E}[X_n]\to\mathbb{E}[X_\infty]$ needs [[Def - Uniform Integrability|uniform integrability]]. The [[Ex - A martingale converging a.s. but not in L1|product martingale]] converges a.s. to $0$ while $\mathbb{E}[X_n]\equiv1$.

> [!warning] 3. Treating "last exit" or "peak" times as stopping times
> $\{T\le n\}$ must lie in $\mathcal{F}_n$. The *last* visit to a set, or the time of a maximum, needs the future — not a stopping time. Only "have I reached it yet?"-type times qualify.

> [!warning] 4. Expecting the martingale limit to be a constant
> An [[Def - Independence|independent]]-increment martingale has a constant limit (the [[Thm - Kolmogorov 0-1 Law|0–1 law]]); a *dependent* one like [[Ex - Polya's urn|Pólya's urn]] converges to a genuinely *random* limit. Convergence does not mean degeneracy.

---

# Problem-Solving Strategy

The problems are of three kinds: *check a martingale*, *compute via optional stopping*, *conclude convergence*.

To **check the martingale property**, condition $X_{n+1}$ on $\mathcal{F}_n$ and split into the part known to $\mathcal{F}_n$ (which [[Thm - Properties of Conditional Expectation|comes out]]) and the genuinely new part (whose conditional mean is computed, usually via independence of the increment from the past). If the process is *not* a martingale, *manufacture* one: subtract the predictable [[Ex - The Doob decomposition|compensator]] to kill the drift, or form an exponential martingale by tuning a parameter so the per-step multiplier has mean $1$, or apply a convex $\varphi$ to get a submartingale. Recognising "which function of the process is a martingale" is the move that unlocks everything else.

To **compute a hitting probability or expected hitting time**, the route is fixed: identify the exit/hitting [[Def - Stopping Time|stopping time]] $T$, choose a martingale, and apply [[Thm - Optional Stopping Theorem|optional stopping]] $\mathbb{E}[X_T]=\mathbb{E}[X_0]$. Because $X_T$ takes only the boundary values, this single equation *solves* for the hitting probability; the compensated-square martingale $S_n^2-n\sigma^2$ then gives a second equation for the expected time. The non-negotiable check: the boundedness or uniform-integrability hypothesis — for an exit time of a *bounded* region it holds (the stopped process is bounded); for first passage to a *single* level it typically fails, and optional stopping must not be applied.

To **conclude convergence**, first secure *a.s.* convergence: an $L^1$-bounded (super)martingale converges a.s. — and *bounded* or *non-negative supermartingale* are the common ways to get $L^1$-boundedness for free. Then decide whether *norm* convergence is needed: if so, verify $L^p$-boundedness ($p>1$, giving $L^p$-convergence via [[Thm - Doob's Maximal Inequality|Doob]]+[[Thm - Dominated Convergence Theorem|DCT]]) or [[Def - Uniform Integrability|uniform integrability]] (giving $L^1$-convergence via [[Thm - Vitali Convergence Theorem|Vitali]], and the closure $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$). Never assume the limit is deterministic — it is, for independent increments (0–1 law), but [[Ex - Polya's urn|need not be]] in general.

---

# Most Reusable Properties

- **[[Thm - Optional Stopping Theorem|The optional stopping theorem]]**: $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ for a martingale and a (bounded / UI-stopped) stopping time. The computational engine — hitting probabilities, expected hitting times, Wald's identities, option pricing — all reduce to applying it to the right martingale. Always paired with the boundedness/UI check.

- **The martingale property via conditioning**: $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$, verified by "known part out, independent increment averaged." Typical use: certify $S_n$, $S_n^2-n\sigma^2$, $e^{uS_n}/\mathbb{E}[e^{uX}]^n$, $\mathbb{E}[Z\mid\mathcal{F}_n]$ as martingales.

- **[[Thm - Doob's Maximal Inequality|Doob's inequalities]]**: the running maximum is controlled by the endpoint — weak-type at $p=1$, strong ($\|X^*\|_p\le\frac{p}{p-1}\|X_n\|_p$) for $p>1$. Typical use: bound $\sup_n|X_n|$, prove $L^p$-convergence, run the upcrossing argument.

- **[[Thm - Almost Sure Martingale Convergence|The martingale convergence theorem]]**: an $L^1$-bounded (super)martingale converges a.s. Typical use: recognise a quantity as a bounded/non-negative (super)martingale and conclude it has a limit — Pólya's urn, Radon–Nikodym approximants, branching-process ratios.

- **[[Def - Conditional Expectation|Closed-martingale]] structure**: a UI martingale is $\mathbb{E}[X_\infty\mid\mathcal{F}_n]$. Typical use: [[Ex - Closed martingales and Levy's 0-1 law|Lévy's upward theorem and 0–1 law]]; optional stopping at unbounded times; identifying limits.

---

# Bridges

1. **To conditional expectation.** A martingale *is* [[Def - Conditional Expectation|conditional expectation]] iterated along a [[Def - Filtration|filtration]] — the [[Thm - Properties of Conditional Expectation|tower property]] in time. [[Advanced Probability III — Conditional Expectation|AP III]] is the statics, AP IV the dynamics; conditional [[Thm - Jensen's Inequality|Jensen]] makes $|M_n|^p$ a submartingale, the input to Doob.

2. **To measure theory.** [[Thm - Doob's Maximal Inequality|Doob's maximal inequality]] is the martingale twin of the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal inequality]], and the [[Thm - Almost Sure Martingale Convergence|convergence theorem]]'s dense-class-and-maximal-inequality spirit mirrors the [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]]. The [[Thm - Lp and L1 Martingale Convergence|martingale proof of Radon–Nikodym]] (countably generated case) closes the loop; [[Thm - Vitali Convergence Theorem|Vitali]] and [[Def - Uniform Integrability|uniform integrability]] govern $L^1$-convergence here exactly as in integration theory.

3. **To the limit theorems.** The [[Thm - Strong Law of Large Numbers|strong law of large numbers]] is a *backward*-martingale convergence theorem; [[Ex - Closed martingales and Levy's 0-1 law|Lévy's 0–1 law]] contains the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]]. Martingale central limit theorems extend the [[Thm - Central Limit Theorem|CLT]] beyond independence.

4. **To continuous time and finance.** Discrete martingales are the gateway to continuous-time martingales, Brownian motion, and the Itô calculus; in mathematical finance a no-arbitrage price is a martingale under the risk-neutral measure, optional stopping prices American options, and Doob's inequalities bound running maxima of asset prices.

---

# Insights

**A martingale is a fair game — and the unifying frame is that it is [[Def - Conditional Expectation|conditional expectation]] set in motion, the [[Thm - Properties of Conditional Expectation|tower property]] indexed by accumulating information.** $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$ says the process is, at every instant, *its own best prediction* given the past. This single identity is responsible for the ubiquity of martingales — sums and products of independent variables, conditional expectations, Radon–Nikodym densities, harmonic functions of Markov chains *all* satisfy it — and recognising a quantity as a martingale immediately imports the whole theory: optional stopping, Doob's inequalities, convergence. When a process is *not* a martingale, the [[Ex - The Doob decomposition|Doob decomposition]] reveals it as a martingale plus a predictable drift, and *subtracting the drift* (the compensator) manufactures one — the systematic way martingale methods are deployed on arbitrary adapted processes.

**Martingales have extraordinary regularity, and the deepest expression of it is "you cannot beat a fair game" — encoded by [[Thm - Optional Stopping Theorem|optional stopping]] and the [[Thm - Almost Sure Martingale Convergence|upcrossing lemma]].** Optional stopping says fairness survives any non-anticipating quitting rule: $\mathbb{E}[X_T]=\mathbb{E}[X_0]$. The upcrossing lemma says a fair game cannot oscillate — a "buy low, sell high" strategy would convert oscillations into guaranteed profit, which fairness forbids, so oscillations are finite and the martingale *converges*. Both rest on the same principle: a [[Def - Stopping Time|stopping time]]'s decision uses only the past, so it cannot tilt the next fair increment. And both come with a *resource bound* — boundedness, uniform integrability — whose necessity is dramatised by the doubling strategy: drop it and a fair game *can* be beaten, but only by tolerating unbounded losses. The boundedness hypothesis is not technical fine print; it is the precise mathematical content of "no free lunch."

**The convergence theory has a sharp two-tier structure: a.s. convergence is *cheap*, norm convergence is *not*.** Mere $L^1$-boundedness — automatic for bounded or non-negative (super)martingales — already forces almost-sure convergence, via the upcrossing lemma. But the limit may have *smaller expectation*: mass can [[Ex - A martingale converging a.s. but not in L1|escape]], and $\mathbb{E}[X_n]\to\mathbb{E}[X_\infty]$ *fails*. Upgrading to $L^1$-convergence requires the genuine extra hypothesis of [[Def - Uniform Integrability|uniform integrability]] (for $p>1$, $L^p$-boundedness, via [[Thm - Doob's Maximal Inequality|Doob's $L^p$ inequality]]). And the uniformly integrable martingales have a clean identity: they are exactly the *closed* ones, $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$ — a perfect bijection with $L^1(\mathcal{F}_\infty)$. This a.s.-versus-$L^1$ gap is the same escape-of-mass phenomenon that runs through the entire two subjects — [[Thm - Fatou's Lemma|Fatou]] strict, [[Thm - Dominated Convergence Theorem|DCT]] needing a dominator, [[Ex - Continuity from above requires finite measure|continuity from above]] needing finiteness — and uniform integrability is, here as everywhere, the precise no-escape condition.

**Martingales are where probability's two great themes meet: *fair games* and *the emergence of order from randomness*.** A martingale fluctuates unpredictably step by step, yet — if $L^1$-bounded — its trajectory *converges*, almost surely, to a definite limit. Sometimes that limit is forced to be a *constant* — when the increments are [[Def - Independence|independent]], the [[Thm - Kolmogorov 0-1 Law|0–1 law]] makes the limit tail-measurable hence deterministic, and the [[Thm - Strong Law of Large Numbers|strong law]] is the headline case. Sometimes, with dependent increments, the limit is genuinely *random* — [[Ex - Polya's urn|Pólya's urn]] settles on a uniformly-distributed proportion, early chance "locking in" a destiny. Either way, *convergence happens*: the conditional-expectation structure imposes order on the noise. This is the same miracle as the law of large numbers and the central limit theorem — randomness, accumulated and averaged, produces structure — now seen at the level of an entire evolving process, and it is why martingales are the organising concept of modern probability and the gateway to stochastic calculus.
