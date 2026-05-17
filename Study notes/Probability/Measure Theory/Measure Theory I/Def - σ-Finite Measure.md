---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ is a [[Def - Measure and Measure Space|measure space]]. We write $X = \bigcup_k S_k$ for an exhaustion by a sequence of sets.

---

# Axiom Motivation

Finite measures ($\mu(X)<\infty$) are wonderfully well-behaved: one can subtract, take complements inside $X$, apply [[Thm - Properties of Measures|continuity from above]] freely, and uniqueness theorems hold. Infinite measures break all of this. Lebesgue measure on $\mathbb{R}^n$ is infinite, so we cannot simply restrict attention to finite measures — yet we still want their good behaviour.

The observation that rescues us: Lebesgue measure is infinite only because $\mathbb{R}^n$ is *unbounded*; on each bounded box it is finite. Tile $\mathbb{R}^n$ by unit cubes and you have written the whole space as a *countable union of finite-measure pieces*. A measure that admits such an exhaustion is called **$\sigma$-finite**. It is the precise hypothesis under which "finite-measure technology" can be deployed piecewise and then assembled — apply a finite-measure argument on each $S_k$, then let $k\to\infty$ using countable additivity.

$\sigma$-finiteness is exactly the hypothesis needed for the *uniqueness* half of the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]], for the existence of [[Def - Product σ-Algebra|product measures]], for [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]], and for the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]]. Without it these theorems genuinely fail. It is the standing background assumption of measure theory — almost every measure one meets in practice is $\sigma$-finite, and the few that are not (like counting measure on an uncountable set) are pathological precisely because they are not.

---

# The Definition

A measure $\mu$ on $(X,\mathcal{A})$ is **$\sigma$-finite** if there exists a sequence $S_1, S_2, \dots \in \mathcal{A}$ with
$$X = \bigcup_{k=1}^\infty S_k \quad\text{and}\quad \mu(S_k) < \infty \ \text{ for all } k.$$
One may always take the $S_k$ to be **increasing** ($S_k \uparrow X$, replace $S_k$ by $S_1\cup\cdots\cup S_k$) or **pairwise disjoint** (replace $S_k$ by $S_k\setminus\bigcup_{j<k}S_j$).

A measure is **finite** if $\mu(X)<\infty$ (the strictly stronger condition, $S_1 = X$). The analogous notion for a [[Def - Pre-Measure|pre-measure]] $\widetilde\mu$ on an algebra requires the $S_k$ to lie in the algebra.

---

# Relate to Other Fields / Compression

$\sigma$-finiteness is the measure-theoretic analogue of *$\sigma$-compactness* in topology (a space that is a countable union of compact sets) and of *exhaustion by finite-dimensional subspaces* in functional analysis. In every case the pattern is: a possibly-infinite object is approximated by an increasing sequence of well-behaved finite pieces, and theorems are proved finite-piece-by-finite-piece, then assembled by a limiting argument. A probability measure is the extreme finite case, $\mu(X)=1$ — which is why probability theory enjoys all the good behaviour automatically and never worries about $\sigma$-finiteness.

---

# Examples / Corollaries

**$\sigma$-finite.** Lebesgue measure on $\mathbb{R}^n$: take $S_k = [-k,k]^n$, each of finite volume $(2k)^n$. Counting measure on a *countable* set: each singleton has measure $1$. Every finite measure, in particular every probability measure.

**Not $\sigma$-finite.** Counting measure on an *uncountable* set $X$: any countable union of finite-measure (hence finite) sets is countable, never all of $X$. The measure $\mu(A) = \infty$ for $A\neq\emptyset$.

**Why uniqueness needs it.** Without $\sigma$-finiteness the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory extension]] need not be unique: a pre-measure can extend to genuinely different measures. The $\sigma$-finite exhaustion forces agreement on each finite piece, hence everywhere.

Calibration: (i) Is every $\sigma$-finite measure finite? No — Lebesgue measure is the counterexample. (ii) Is the sum of countably many finite measures $\sigma$-finite? Not necessarily — but a *single* measure that is a countable sum of probability measures has total mass possibly $\infty$ yet is $\sigma$-finite if... actually it is finite-or-not depending; the safe statement is that $\sigma$-finiteness is about exhausting $X$, not about $\mu(X)$. (iii) Is counting measure on $\mathbb{Q}$ $\sigma$-finite? Yes — $\mathbb{Q}$ is countable.

---

# Unlocked by This

> [!tip] Uniqueness, product measures, Fubini, Radon–Nikodym
> $\sigma$-finiteness is the recurring hypothesis of the deep theorems: uniqueness in [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory]], existence of the [[Def - Product σ-Algebra|product measure]], the equality of iterated integrals in [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]], and the existence of a density in [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]].
