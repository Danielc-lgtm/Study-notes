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

A **martingale** models a **fair game**: a process whose *expected future value, given everything known so far, equals its present value*. If $X_n$ is a gambler's fortune after round $n$, the martingale condition $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$ says the game is fair — no betting strategy, using only past information, can change the expected fortune. The three axioms — adaptedness, integrability, and the martingale identity — together axiomatise this "fair game" intuition, and each is forced by a specific requirement of the formalism. Dropping any one creates a concrete failure, and understanding *which* failure each axiom prevents is the route to inventing the definition.

The first axiom is **adaptedness to the filtration $(\mathcal{F}_n)$**: $X_n$ is $\mathcal{F}_n$-measurable for every $n$. This says the process is *observable by its own time* — the value of $X_n$ uses only information available at time $n$. Drop adaptedness and the process becomes *anticipative*: $X_n$ could depend on $\mathcal{F}_{n+1}$ or beyond, peeking into the future. The gambling interpretation makes the pathology vivid: an unadapted process is a "fortune" whose value tomorrow has been smuggled into the bookkeeping today, which is not a game at all but a clairvoyant fraud. More formally, the conditional expectation $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n]$ in the martingale identity *requires* $X_{n+1}$ to be defined as a random variable on $(\Omega, \mathcal{F}, \mathbb{P})$, and equating it to $X_n$ requires $X_n$ to be $\mathcal{F}_n$-measurable (otherwise the equality $\mathbb{E}[\cdot \mid \mathcal{F}_n] = X_n$ has the wrong type — the left side is $\mathcal{F}_n$-measurable, the right side is not). Adaptedness is what makes the martingale identity *typecheck*. Concrete witness: if $S_n = X_1 + \cdots + X_n$ is the random walk and we naively defined $Y_n = X_1 + \cdots + X_{n+1}$ (one increment ahead), then $Y_n$ knows tomorrow's news today, $\mathbb{E}[Y_{n+1} \mid \mathcal{F}_n] = Y_n + \mathbb{E}[X_{n+2} \mid \mathcal{F}_n]$, and the structure breaks. Every [[Def - Stopping Time|stopping time]] argument also depends on adaptedness: the decision to stop must use only $\mathcal{F}_n$, and stopping rules that anticipate the future ("sell at the maximum") break optional stopping precisely because they violate this constraint.

The second axiom is **integrability**, $X_n \in L^1(\mathbb{P})$, i.e. $\mathbb{E}|X_n| < \infty$ for every $n$. The role here is foundational rather than conceptual: [[Def - Conditional Expectation|conditional expectation]] is defined only for $L^1$ random variables (its existence proof uses [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]], which needs $\sigma$-finiteness, but the standard formulation requires $X \in L^1$). Drop integrability and $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n]$ is undefined; the martingale identity has no meaning to begin with. The concrete pathology: take $X_n$ to be a Cauchy-distributed random variable; $\mathbb{E}|X_n| = \infty$, so conditional expectation is not defined for the standard construction, and any attempt to write $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$ is a category error. There are extensions of the martingale theory to local martingales (where each $X_n$ is allowed to fail integrability but the martingale identity is recovered along a localising sequence of stopping times), and these are essential in continuous-time stochastic calculus where the Itô integral lives, but the elementary discrete-time definition requires $L^1$ outright. The integrability hypothesis is also what makes the *taking-expectations* identity $\mathbb{E}[X_n] = \mathbb{E}[X_0]$ valid: $\mathbb{E}|X_n| < \infty$ ensures the expectation is a well-defined finite number, and the constancy of $\mathbb{E}[X_n]$ in $n$ is the *headline scalar consequence* of the martingale property, used in nearly every application.

The third and decisive axiom is the **martingale identity** $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$. This is the *equality* in three possible relations $\le, =, \ge$, and the choice of equality is what makes the definition *the* fair game rather than a one-sided variant. Relax the equality to $\le$ and one obtains a **supermartingale**: $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \le X_n$, modelling an *unfavourable* game whose expected value drifts down — the casino's game from the gambler's perspective, or a fortune subject to taxation. Relax in the other direction to $\ge$ and one obtains a **submartingale**: an expected value drifts up — a favourable game, or the modulus $|M_n|$ of a martingale (which by conditional [[Thm - Jensen's Inequality|Jensen]] satisfies $\mathbb{E}[|M_{n+1}| \mid \mathcal{F}_n] \ge |M_n|$). Each is a perfectly good object with its own theory — the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] is stated for *supermartingales*, and the standard random-walk analysis uses $S_n$ as a martingale together with $S_n^2 - n\sigma^2$ as another martingale (and convex functions of either as submartingales). The exact equality is the symmetric special case where both relaxations hold simultaneously: $(X_n)$ is a martingale iff it is both a sub- and a supermartingale.

Why is the **exact equality** the right choice for the central definition? Because it is precisely the [[Thm - Properties of Conditional Expectation|tower property]] held fixed across time, and equality is what makes the martingale identity *self-iterating*: from $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$ one obtains $\mathbb{E}[X_m \mid \mathcal{F}_n] = X_n$ for all $m \ge n$ by repeated application of the tower property — the process *is its own best prediction* at every horizon. With $\le$ or $\ge$ this self-iteration produces only inequalities, losing the symmetric "best prediction" reading. More importantly, exact equality is what makes the [[Thm - Optional Stopping Theorem|optional stopping theorem]] state $\mathbb{E}[X_T] = \mathbb{E}[X_0]$ as an *equality* — for a supermartingale one gets only $\mathbb{E}[X_T] \le \mathbb{E}[X_0]$, which is far weaker and cannot be used to *solve* for hitting probabilities. The entire computational engine of martingale theory — the random-walk hitting calculations, the Wald identities, the option pricing arguments — depends on the equality at $T$ being an actual equation one can rearrange, and that traces back to the equality in the defining axiom. The exact equality is also what makes a martingale a *gauge* concept in the sense of physics: there is a natural symmetry $X_n \to X_n + c$ and a natural decomposition theorem ([[Ex - The Doob decomposition|Doob decomposition]]) splitting any adapted integrable process into a martingale plus a predictable drift; without the symmetric equality, neither the symmetry nor the decomposition is clean. Forward-reference: the [[Thm - Optional Stopping Theorem|optional stopping theorem]], the [[Thm - Doob's Maximal Inequality|Doob inequalities]], and the [[Thm - Almost Sure Martingale Convergence|convergence theorem]] all use the exact equality at decisive steps — relax it and each weakens to a one-sided statement, costing the user the ability to compute, only the ability to bound.

A final remark on the **structural unity** the three axioms produce. A martingale is exactly [[Def - Conditional Expectation|conditional expectation]] iterated along a [[Def - Filtration|filtration]] — the [[Thm - Properties of Conditional Expectation|tower property]] in motion. Two facts then deliver the entire downstream theory. First, *martingales arise everywhere*: any $X_n = \mathbb{E}[Z \mid \mathcal{F}_n]$ for a fixed $Z \in L^1$ is a martingale (a "closed" one); sums of independent mean-zero variables, products of independent mean-one variables, [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] derivatives along a filtration, harmonic functions of Markov chains — all are martingales by direct verification of the three axioms. Second, they have *spectacular regularity*: optional stopping (fairness survives random stopping), Doob's inequalities (the trajectory maximum is controlled by the endpoint), and the convergence theorems ($L^1$-bounded martingales converge a.s.) — all flow from the three-axiom definition. Defining "fair game" precisely is what unlocks all of this; relax any axiom and the chain breaks at the corresponding link.

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
