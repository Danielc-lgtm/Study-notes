---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A})$ a [[Def - Measurable Space|measurable space]]. $\alpha$ denotes a signed measure. A set $A$ is *positive* / *negative* for $\alpha$ as defined below.

---

# Axiom Motivation

A [[Def - Measure and Measure Space|measure]] models a non-negative quantity — mass, length, probability. But many natural quantities take *both signs*: electric charge, a profit-and-loss, the difference of two mass distributions, the integral $\int_A f\,d\mu$ of a function $f$ that is sometimes negative. A **signed measure** is the object that drops the non-negativity axiom while keeping $\sigma$-additivity.

The one technical care: $\sigma$-additivity $\alpha(\bigsqcup A_n)=\sum\alpha(A_n)$ now involves a series of terms of *both signs*, and for the value to be unambiguous one demands the series *converge absolutely* whenever the union has finite measure (so rearrangement is harmless), and one forbids the indeterminate "$+\infty-\infty$" by allowing $\alpha$ to take at most one of the values $\pm\infty$.

The deep question a signed measure poses: can the positive and negative "parts" always be *cleanly separated*? Is there a single set $A$ carrying all the positive charge and its complement $B$ all the negative charge? The [[Thm - Hahn and Jordan Decomposition|Hahn decomposition theorem]] answers *yes* — and to state it one needs the notions of **positive** and **negative set**: a set on every measurable subset of which $\alpha$ is, respectively, $\ge0$ or $\le0$. These are the building blocks: a positive set is a region of "pure positive charge." The whole theory of signed measures, and the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]], rests on being able to perform this separation.

---

# The Definition

Let $(X,\mathcal{A})$ be a measurable space. A **signed measure** is a function $\alpha:\mathcal{A}\to(-\infty,\infty]$ (or $[-\infty,\infty)$ — at most one infinite value allowed) such that

1. $\alpha(\emptyset)=0$;
2. ($\sigma$-additivity) for pairwise disjoint $A_1,A_2,\dots\in\mathcal{A}$, $\ \alpha\big(\bigsqcup_n A_n\big)=\sum_n\alpha(A_n)$, the series converging absolutely whenever $\alpha(\bigsqcup_n A_n)$ is finite.

A set $A\in\mathcal{A}$ is **positive** for $\alpha$ if $\alpha(B)\ge0$ for every measurable $B\subseteq A$; **negative** if $\alpha(B)\le0$ for every measurable $B\subseteq A$; **null** if $\alpha(B)=0$ for every measurable $B\subseteq A$.

A genuine (non-negative) measure is a signed measure for which every set is positive.

---

# Relate to Other Fields / Compression

A signed measure generalises a measure by *dropping positivity* — the same move that takes a norm to a signed/oscillating quantity, or a probability to a *finite signed* charge. The prototype is $\alpha(A)=\int_A f\,d\mu$ for a $\mu$-integrable $f$ of either sign — a "measure with a signed density." In physics it is a charge distribution; the [[Thm - Hahn and Jordan Decomposition|Jordan decomposition]] $\alpha=\alpha^+-\alpha^-$ is the splitting into positive and negative charge, and $|\alpha|=\alpha^++\alpha^-$ is the total-variation measure. Signed measures form a *vector space* (measures only a cone) — which is what makes the space of measures a Banach space under the total-variation norm, the dual of $C(X)$ in the Riesz representation theorem.

---

# Examples / Corollaries

**Density of a signed function.** For $\mu$ a measure and $f$ with $\int f^-\,d\mu<\infty$, $\alpha(A)=\int_A f\,d\mu$ is a signed measure; here a set is positive iff $\mu(A\cap\{f<0\})=0$ — positivity localises where $f\ge0$.

**Difference of measures.** For finite measures $\mu_1,\mu_2$, $\alpha=\mu_1-\mu_2$ is a signed measure. The [[Thm - Hahn and Jordan Decomposition|Jordan decomposition]] theorem says *every* signed measure has this form.

Non-example: a set function taking *both* $+\infty$ and $-\infty$ is not a signed measure — the "$\infty-\infty$" ambiguity is forbidden.

Calibration: (i) Is a probability measure a signed measure? Yes — every measure is. (ii) Is $X$ itself positive for a genuine measure? Yes. (iii) Can a set be both positive and negative? Yes — exactly the *null* sets.

---

# Unlocked by This

> [!tip] Hahn and Jordan decompositions
> Every signed measure splits its space into a positive set and a negative set ([[Thm - Hahn and Jordan Decomposition|Hahn]]), equivalently writes as $\alpha=\alpha^+-\alpha^-$ for mutually [[Def - Mutual Singularity|singular]] measures (Jordan). This is the structural prelude to [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]].
