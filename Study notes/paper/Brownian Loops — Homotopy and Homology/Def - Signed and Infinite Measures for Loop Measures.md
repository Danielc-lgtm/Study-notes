---
type: definition
subject: measure-theory
prereqs:
  - "Def - σ-Finite Measure"
tags: [measure-theory, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$(\Omega,\mathcal F)$ a measurable space: a set $\Omega$ with a σ-algebra $\mathcal F$ (a collection of "measurable" subsets closed under complements and countable unions). All the loop "measures" of the paper are measures on such spaces, but with a twist explained below.

---

# Axiom Motivation

Elementary probability lives with *probability measures* — total mass 1. The paper's central object, the Brownian loop measure, is deliberately **not** a probability measure: its total mass is infinite. It is still a genuine measure (it assigns a size to each measurable set of loops, countably additively), just not normalised. Calling it a "measure" and manipulating it — restricting it to a subset of loops, integrating a function against it, pushing it forward under a map — needs only the general notion of a (possibly infinite) measure, not total mass 1. Two properties keep an infinite measure usable, and both hold here: **σ-finiteness** (the space is a countable union of finite-mass pieces, so Tonelli/Fubini and disintegration still work) and, at intermediate stages, being a **signed measure** (differences of measures, which can take negative values — the interaction measures of §2's Lévy–Khintchine data and the loop-measure identities involve such differences).

The point is modest but essential to state: everything you know about integrating against a probability measure — linearity, monotone and dominated convergence, Tonelli — carries over verbatim to a σ-finite measure. The only thing you lose is that "total mass" may be $+\infty$, so you cannot divide by it to normalise until you have first cut the space into finite-mass pieces. Cutting the loop measure into finite-mass pieces (one per homotopy class) and *then* normalising is precisely the paper's programme.

---

# The Definition

> **Definition (measure; σ-finite; signed).** A **measure** on $(\Omega,\mathcal F)$ is a function $\mu:\mathcal F\to[0,\infty]$ with $\mu(\varnothing)=0$ that is countably additive: $\mu(\bigsqcup_n A_n)=\sum_n\mu(A_n)$ for disjoint $A_n$. It is a **probability measure** if $\mu(\Omega)=1$, **finite** if $\mu(\Omega)<\infty$, and **[[Def - σ-Finite Measure|σ-finite]]** if $\Omega=\bigcup_n \Omega_n$ with $\mu(\Omega_n)<\infty$ for all $n$. A **signed measure** is a countably additive $\mu:\mathcal F\to(-\infty,\infty]$ (or $[-\infty,\infty)$) with $\mu(\varnothing)=0$; every signed measure splits as a difference $\mu=\mu^+-\mu^-$ of two measures (Hahn–Jordan decomposition). The **pushforward** of $\mu$ under a measurable $T:\Omega\to\Omega'$ is $(T_*\mu)(A)=\mu(T^{-1}A)$; the **restriction** to $B\in\mathcal F$ is $(\mu|_B)(A)=\mu(A\cap B)$, i.e. $d(\mu|_B)=\mathbf 1_B\,d\mu$.

**Concrete unpacking.** Lebesgue measure on $\mathbb{R}$ has total mass $+\infty$ but is σ-finite ($\mathbb{R}=\bigcup_n[-n,n]$, each of finite length), and you integrate against it exactly as against a probability measure. The multiplicative measure $\frac{dt}{t}$ on $(0,\infty)$ (the "Haar measure" weighting loop durations in the paper) is another infinite-but-σ-finite example: $\int_1^\infty \frac{dt}{t}=\infty$ and $\int_0^1\frac{dt}{t}=\infty$, yet $\int_a^b\frac{dt}{t}=\log(b/a)<\infty$ on each bounded-away-from-$0$-and-$\infty$ piece.

**Standard names.** σ-finite measure, signed measure, Hahn–Jordan decomposition, pushforward measure, restriction of a measure — all standard measure theory.

---

# Examples and Non-Examples

**Is an instance.** Lebesgue measure; counting measure on $\mathbb{Z}$; $\frac{dt}{t}$ on $(0,\infty)$; the Brownian loop measure $\mu_X$ (σ-finite, infinite total mass). A difference $P-Q$ of two probability measures is a signed measure with total mass 0.

**Is NOT an instance.** Counting measure on an uncountable set (e.g. $\mathbb{R}$) is a measure but **not** σ-finite — it cannot be cut into countably many finite pieces — so Tonelli and disintegration can fail for it. This is exactly the hypothesis the loop measure is careful to satisfy.

**Calibration check.** (1) Verify $\frac{dt}{t}$ is σ-finite via $\Omega_n=[1/n,\,n]$. (2) Confirm the restriction identity $d(\mu|_B)=\mathbf 1_B\,d\mu$ gives $\mu|_B(A)=\mu(A\cap B)$. (3) Write the signed measure $P-Q$ for $P=\delta_0$, $Q=\delta_1$ and identify $\mu^+,\mu^-$.

---

# Where the paper uses this

The rooted Brownian loop measure $\mu^*_X$ is "infinite but σ-finite" — the paper says so verbatim. Restriction and pushforward are its two defining operations (restrict to loops inside $X'$; push forward from rooted to unrooted loops). The Lévy measure $\nu$ and interaction differences are (signed/positive) infinite measures. σ-finiteness is what licenses Tonelli in every mass computation (e.g. [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]). **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2]]**.

---

# Verified against

Folland, *Real Analysis* (2nd ed.), §1.3 (measures, σ-finite), §3.1 (signed measures, Hahn–Jordan); Bogachev, *Measure Theory*, Vol. 1, for pushforward and restriction. Standard.
