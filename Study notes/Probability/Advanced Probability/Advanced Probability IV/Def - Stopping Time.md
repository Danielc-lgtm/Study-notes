---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Filtration"
tags: [probability, advanced-probability]
---

# Notation

$(\mathcal{F}_n)_{n\ge0}$ a [[Def - Filtration|filtration]]; $T:\Omega\to\{0,1,2,\dots\}\cup\{\infty\}$ a random time; $X_T$, $X_n^T$ as below.

---

# Axiom Motivation

We often want to stop a process at a *random* time — the moment a stock first hits a target, the round a gambler quits, the first time a random walk reaches a level. For such a random time to be *usable* — to talk about $X_T$, to apply theorems — it must be **non-anticipating**: the decision to stop *at or before time $n$* must rely only on the information available *by time $n$*. One cannot stop "the day before the market peaks" — that needs the future.

A **stopping time** is the formalisation: a random time $T$ such that $\{T\le n\}\in\mathcal{F}_n$ for every $n$. Equivalently $\{T=n\}\in\mathcal{F}_n$ — at each instant one can *decide, from current information, whether $T$ has occurred*. The hitting time of a set is a stopping time ("have I reached it yet?" is answerable now); the *last* visit to a set is not ("is this the last time?" needs the future).

The point of the definition is everything it unlocks. Stopping times can be combined ($T\wedge S$, $T\vee S$ are stopping times); the *stopped process* $X_n^T=X_{T\wedge n}$ inherits adaptedness and the (sub/super)[[Def - Martingale|martingale]] property; the $\sigma$-algebra $\mathcal{F}_T$ of "information up to the random time $T$" makes sense; and — the headline — the [[Thm - Optional Stopping Theorem|optional stopping theorem]] says a martingale's fairness *survives* being stopped: $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ for bounded $T$. Non-anticipation is exactly the property that makes this true; without it, "stop just before the peak" would manufacture a free lunch.

---

# The Definition

Let $(\mathcal{F}_n)_{n\ge0}$ be a [[Def - Filtration|filtration]]. A random variable $T:\Omega\to\{0,1,2,\dots\}\cup\{\infty\}$ is a **stopping time** if
$$\{T\le n\}\in\mathcal{F}_n\qquad\text{for every }n\ge0,$$
equivalently $\{T=n\}\in\mathcal{F}_n$ for every $n$.

Associated objects:
- the **stopped process** $X_n^T:=X_{T\wedge n}$, which equals $X_n$ before $T$ and freezes at $X_T$ after;
- $X_T$, defined on $\{T<\infty\}$ by $X_T(\omega)=X_{T(\omega)}(\omega)$;
- the **stopping-time $\sigma$-algebra** $\mathcal{F}_T=\{A\in\mathcal{F}_\infty:A\cap\{T\le n\}\in\mathcal{F}_n\ \forall n\}$ — "the information known by time $T$."

If $S,T$ are stopping times, so are $S\wedge T$, $S\vee T$, $S+T$; constants are stopping times; $S\le T\Rightarrow\mathcal{F}_S\subseteq\mathcal{F}_T$.

---

# Relate to Other Fields / Compression

A stopping time is a *non-anticipating random time* — the discrete shadow of the continuous-time concept central to the Itô calculus, optimal stopping, and sequential analysis. In decision theory it is an *admissible stopping rule* (a quitting decision using only observed history); in finance, an *exercise time* for an American option. The defining property "$\{T\le n\}\in\mathcal{F}_n$" is the [[Def - Filtration|adaptedness/causality]] condition applied to a *time* rather than a value.

---

# Examples / Corollaries

**Hitting time.** For $B\in\mathcal{B}(\mathbb{R})$ and an adapted $(X_n)$, $T_B=\inf\{n:X_n\in B\}$ is a stopping time: $\{T_B\le n\}=\bigcup_{k\le n}\{X_k\in B\}\in\mathcal{F}_n$.

**Not a stopping time.** The *last* time in $B$, $L_B=\sup\{n:X_n\in B\}$, is generally *not* — $\{L_B\le n\}$ needs to know the process never returns to $B$ after $n$, a future event.

**Stopped process.** If $(M_n)$ is a martingale and $T$ a stopping time, the stopped process $(M_n^T)=(M_{T\wedge n})$ is again a martingale ([[Thm - Optional Stopping Theorem|optional stopping]]).

**Calibration check.** Verify that a constant time $T \equiv m$ is a stopping time, because $\{m \leq n\}$ is either $\emptyset$ or $\Omega$, both in $\mathcal{F}_n$. Verify that the hitting time $T_B = \inf\{n : X_n \in B\}$ is a stopping time, by writing $\{T_B \leq n\} = \bigcup_{k \leq n} \{X_k \in B\}$ as a finite union of $\mathcal{F}_n$-events. And verify that $\inf\{n : X_{n+1} > X_n\}$ is *not* a stopping time, because deciding whether to stop at time $n$ requires knowing $X_{n+1}$ — a one-step peek into the future, exactly the anticipation that the definition forbids.

---

# Unlocked by This

> [!tip] Optional stopping theorem
> A martingale stopped at a (bounded, or uniformly integrable) stopping time keeps $\mathbb{E}[X_T]=\mathbb{E}[X_0]$ — [[Thm - Optional Stopping Theorem|the optional stopping theorem]], the workhorse for computing hitting probabilities and expected hitting times.
