---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Filtration"
  - "Def - Conditional Expectation"
tags: [probability, advanced-probability]
---

# Notation

$(\Omega,\mathcal{F},(\mathcal{F}_n),\mathbb{P})$ a [[Def - Filtration|filtered probability space]]; $(X_n)_{n\ge0}$ an adapted, integrable process.

---

# Axiom Motivation

A **martingale** models a **fair game**: a process whose *expected future value, given everything known so far, equals its present value*. If $X_n$ is a gambler's fortune after round $n$, the martingale condition $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$ says the game is fair — no betting strategy, using only past information, can change the expected fortune. A **supermartingale** ($\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]\le X_n$) is unfavourable (the fortune drifts down — the casino's game); a **submartingale** ($\ge X_n$) is favourable.

Why is this the structurally right definition? Because it is *exactly* [[Def - Conditional Expectation|conditional expectation]] held fixed in time — the [[Thm - Properties of Conditional Expectation|tower property]] in motion. The martingale identity says the process *is its own best prediction*: $\mathbb{E}[X_m\mid\mathcal{F}_n]=X_n$ for all $m\ge n$ (iterate, using the tower property). Two facts make martingales powerful far beyond gambling. First, they arise *everywhere*: any $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ for a fixed $Z\in L^1$ is a martingale (a "closed" one); sums of independent mean-zero variables, products of independent mean-one variables, [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] derivatives along a filtration, harmonic functions of Markov chains — all are martingales. Second, they have spectacular *regularity*: the [[Thm - Optional Stopping Theorem|optional stopping theorem]] (fairness survives random stopping), [[Thm - Doob's Maximal Inequality|Doob's inequalities]] (the maximum is controlled), and the [[Thm - Almost Sure Martingale Convergence|convergence theorems]] (bounded martingales converge almost surely). Defining "fair game" precisely unlocks all of this.

---

# The Definition

Let $(X_n)_{n\ge0}$ be a process that is **adapted** to $(\mathcal{F}_n)$ and **integrable** ($X_n\in L^1$ for all $n$). It is a:

- **martingale** if $\ \mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n\ $ for all $n\ge0$;
- **supermartingale** if $\ \mathbb{E}[X_{n+1}\mid\mathcal{F}_n]\le X_n$;
- **submartingale** if $\ \mathbb{E}[X_{n+1}\mid\mathcal{F}_n]\ge X_n$.

(All a.s.) By the [[Thm - Properties of Conditional Expectation|tower property]] this extends to $\mathbb{E}[X_m\mid\mathcal{F}_n]=X_n$ (resp. $\le,\ge$) for all $m\ge n$, and taking expectations, $n\mapsto\mathbb{E}[X_n]$ is constant (resp. non-increasing, non-decreasing). $(X_n)$ is a martingale iff it is both a sub- and a supermartingale; $(X_n)$ is a supermartingale iff $(-X_n)$ is a submartingale.

---

# Relate to Other Fields / Compression

A martingale is [[Def - Conditional Expectation|conditional expectation]] frozen along a [[Def - Filtration|filtration]] — the dynamic form of the [[Thm - Properties of Conditional Expectation|tower property]]. It is the probabilistic counterpart of a **harmonic function** (whose value is its own average over a neighbourhood — indeed $f(\text{Markov chain})$ is a martingale iff $f$ is harmonic), and the continuous-time version (Brownian martingales) is the foundation of the Itô calculus and mathematical finance (a "fair price" is a martingale under the risk-neutral measure). A submartingale is "subharmonic"; the [[Thm - Hahn and Jordan Decomposition|Doob decomposition]] splits any submartingale into a martingale plus an increasing predictable part.

---

# Examples / Corollaries

**Random walk.** $S_n=\sum_{k\le n}X_k$ with $X_k$ independent, $\mathbb{E}X_k=0$: a martingale. With $\mathbb{E}X_k\le0$: a supermartingale.

**Closed martingale.** For fixed $Z\in L^1$, $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ is a martingale (by the tower property) — and these are exactly the [[Def - Uniform Integrability|uniformly integrable]] martingales.

**Product martingale.** $X_n=\prod_{k\le n}Y_k$ with $Y_k$ independent, $\mathbb{E}Y_k=1$, $Y_k\ge0$: a martingale.

**Convex functions.** If $(M_n)$ is a martingale and $\varphi$ convex with $\varphi(M_n)\in L^1$, then $(\varphi(M_n))$ is a *submartingale* — by [[Thm - Properties of Conditional Expectation|conditional Jensen]]. In particular $|M_n|$ and $M_n^2$ are submartingales.

Calibration: (i) Is $n\mapsto\mathbb{E}[X_n]$ constant for a martingale? Yes. (ii) Is a martingale a Markov process? Not necessarily — the two notions are independent. (iii) Is $|M_n|$ a martingale? No — a submartingale (convex $\varphi$).

---

# Unlocked by This

> [!tip] Optional stopping, Doob's inequalities, convergence
> The martingale property is preserved under stopping ([[Thm - Optional Stopping Theorem|optional stopping]]); the maximum is controlled ([[Thm - Doob's Maximal Inequality|Doob's inequalities]]); $L^1$-bounded martingales converge a.s. ([[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]]).
