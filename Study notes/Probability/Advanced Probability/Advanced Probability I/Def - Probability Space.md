---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Measure and Measure Space"
  - "Def - Algebra and σ-Algebra"
tags: [probability, advanced-probability, measure-theory]
---

# Notation

$\Omega$ — the sample space; $\mathcal{F}\subseteq 2^\Omega$ — the $\sigma$-algebra of events; $\mathbb{P}$ — the probability measure. $\omega\in\Omega$ — an outcome. "a.s." — almost surely.

---

# Axiom Motivation

Probability theory needs a rigorous home for the words *outcome*, *event*, and *probability*. Kolmogorov's insight (1933) was that the home already exists: it is a [[Def - Measure and Measure Space|measure space]] of total mass $1$. Nothing new is invented — probability is measure theory with a normalisation and a change of vocabulary.

Why is this the *right* formalism? Three demands. (i) An *event* should be assigned a number in $[0,1]$, and events should combine: "$A$ or $B$" for disjoint $A,B$ should add. That is a finitely additive set function. (ii) Events should be closed under the operations one performs on them — complement ("not $A$"), countable union ("at least one of $A_1,A_2,\dots$"). That forces the events to be a [[Def - Algebra and σ-Algebra|$\sigma$-algebra]] $\mathcal{F}$. (iii) The continuity axiom — $A_n\downarrow\emptyset\Rightarrow\mathbb{P}(A_n)\to0$ — upgrades finite to countable additivity, which is exactly what makes *limiting* events ("$X_n$ converges," "$A_n$ infinitely often") tractable. The triple $(\Omega,\mathcal{F},\mathbb{P})$ with $\mathbb{P}(\Omega)=1$ is the result.

The normalisation $\mathbb{P}(\Omega)=1$ is not cosmetic: it makes $\mathbb{P}$ a *finite* measure, so all of finite-measure technology — [[Thm - Egorov's Theorem|Egorov]], [[Thm - Lusin's Theorem|Lusin]], bounded convergence, the [[Def - Lp Spaces|$L^p$ inclusions]] $L^q\subseteq L^p$ for $q\ge p$ — is automatic. And it gives the *interpretation*: $\mathbb{P}(A)$ is the fraction of "probability mass" on $A$. What distinguishes probability from bare measure theory is not the axioms but the questions — *independence*, *conditioning*, *limit laws* — and the reading of a sub-$\sigma$-algebra as *partial information*.

---

# The Definition

A **probability space** is a triple $(\Omega,\mathcal{F},\mathbb{P})$ where:

- $\Omega$ is a set, the **sample space** — the set of possible outcomes;
- $\mathcal{F}\subseteq 2^\Omega$ is a [[Def - Algebra and σ-Algebra|$\sigma$-algebra]], whose elements are called **events**;
- $\mathbb{P}:\mathcal{F}\to[0,1]$ is a [[Def - Measure and Measure Space|measure]] with $\mathbb{P}(\Omega)=1$ — a **probability measure**.

Thus a probability space is exactly a measure space of total mass $1$. An event $A$ holds **almost surely** (a.s.) if $\mathbb{P}(A)=1$ — i.e. its complement is [[Def - Null Set and Completion|null]]. From the [[Thm - Properties of Measures|measure axioms]]: $\mathbb{P}(A^c)=1-\mathbb{P}(A)$, monotonicity, [[Thm - Properties of Measures|continuity]] along monotone sequences of events, and inclusion–exclusion.

---

# Relate to Other Fields / Compression

A probability space *is* a [[Def - Measure and Measure Space|measure space]] with $\mu(\Omega)=1$ — Kolmogorov's reduction of probability to measure theory. The dictionary: measurable set $\to$ event; [[Def - Measurable Function|measurable function]] $\to$ [[Def - Random Variable|random variable]]; [[Def - The Integral|integral]] $\to$ expectation; [[Def - Almost Everywhere|almost everywhere]] $\to$ almost surely; [[Thm - Properties of Measures|continuity of measures]] $\to$ continuity of probability. What is *genuinely new* in probability — absent from measure theory — is the reading of a *sub-$\sigma$-algebra* as a state of partial information ([[Def - Filtration|filtrations]], [[Def - Conditional Expectation|conditioning]]) and the notion of [[Def - Independence|independence]].

---

# Examples / Corollaries

**Discrete.** $\Omega$ countable, $\mathcal{F}=2^\Omega$, $\mathbb{P}(\{\omega\})=p_\omega\ge0$ with $\sum p_\omega=1$ — coin tosses, dice, the geometric and Poisson laws.

**The unit interval.** $\Omega=[0,1]$, $\mathcal{F}=\mathcal{B}([0,1])$, $\mathbb{P}=\lambda$ — the uniform distribution. By the [[Def - Distribution Function|quantile transform]] this single space supports *every* law on $\mathbb{R}$.

**Coin-toss space.** $\Omega=\{0,1\}^{\mathbb{N}}$ with the product $\sigma$-algebra and the $(\tfrac12,\tfrac12)$ [[Thm - Product Measure|product measure]] — the canonical model of an infinite sequence of fair coin tosses.

Calibration: (i) Is $(\mathbb{R},\mathcal{B}(\mathbb{R}),\lambda)$ a probability space? No — $\lambda(\mathbb{R})=\infty\neq1$. (ii) Must every event have a probability? Only events in $\mathcal{F}$; the [[Thm - Existence of a Non-Measurable Set|Vitali set]] shows one cannot take $\mathcal{F}=2^\Omega$ in general. (iii) Does "a.s." mean "always"? No — it means "off a null set."

---

# Unlocked by This

> [!tip] Random variables, expectation, independence
> On a probability space one defines [[Def - Random Variable|random variables]] (measurable functions), [[Def - Expectation and Moments|expectation]] (the integral), and — the genuinely probabilistic notion — [[Def - Independence|independence]] of events and variables.

> [!tip] Filtrations *(Martingale Theory)*
> An increasing chain of sub-$\sigma$-algebras $\mathcal{F}_0\subseteq\mathcal{F}_1\subseteq\cdots$ of $\mathcal{F}$ is a [[Def - Filtration|filtration]], modelling information revealed over time.
