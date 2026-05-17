---
type: definition
subject: measure-theory
prereqs:
  - "Def - Algebra and σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

Points of $\mathbb{R}^n$ are $a=(a_1,\dots,a_n)$, $b=(b_1,\dots,b_n)$. An interval (box) is a product $\prod_{k=1}^n I_k$ of one-dimensional intervals. $\widetilde\lambda$ denotes elementary volume.

---

# Axiom Motivation

Lebesgue measure must come from *somewhere* — and the only sets in $\mathbb{R}^n$ whose volume is genuinely beyond dispute are **boxes**: the volume of $\prod_k(a_k,b_k)$ is the product of side lengths $\prod_k(b_k-a_k)$. That formula is the bedrock. The entire theory is the project of *propagating* this one indisputable formula to all Borel sets.

But a single box is not enough structure to start the [[Thm - Hahn-Carathéodory Extension Theorem|extension machine]]: the machine needs a [[Def - Pre-Measure|pre-measure]] on an *algebra*. Boxes do not form an algebra — the complement of a box is not a box. The smallest algebra they generate is the **elementary figures**: finite unions of boxes. This family *is* closed under complement (the complement of a box is a finite union of boxes) and under finite union and intersection, so it is an algebra — and the smallest one supporting our intended volume. Elementary figures are the minimal launchpad: small enough that "volume" is unambiguous on them (just add up disjoint boxes), large enough to be an algebra and feed the extension theorem.

The half-open convention $(a,b]$ is preferred for the boxes because half-open boxes *tile* without overlap — $(0,1]=(0,\tfrac12]\sqcup(\tfrac12,1]$ — so a finite union of boxes can always be rewritten as a *disjoint* finite union, making the volume well-defined by simple addition.

---

# The Definition

For $a,b\in\mathbb{R}^n$, an **interval** (or **box**) is a set
$$(a,b)=\prod_{k=1}^n(a_k,b_k)=\{x\in\mathbb{R}^n : a_k<x_k<b_k\ \forall k\},$$
with $(a,b)=\emptyset$ unless $a_k<b_k$ for all $k$. The variants $[a,b],\ (a,b],\ [a,b)$ are defined analogously, and endpoints $\pm\infty$ are permitted (for the open side). Any such product set is an **interval**.

An **elementary figure** is a finite union $\bigcup_{k=1}^m I_k$ of finitely many disjoint intervals $I_1,\dots,I_m$. The collection
$$\mathcal{A}=\{A\subseteq\mathbb{R}^n : A\text{ is an elementary figure}\}$$
is an **algebra** over $\mathbb{R}^n$.

The **elementary volume** is the [[Def - Pre-Measure|pre-measure]] $\widetilde\lambda:\mathcal{A}\to[0,\infty]$ given on a box by
$$\widetilde\lambda\big(\textstyle\prod_k(a_k,b_k)\big)=\prod_{k=1}^n(b_k-a_k)\quad(\text{and }=0\text{ if degenerate}),$$
and extended additively: $\widetilde\lambda(\bigsqcup_{k=1}^m I_k)=\sum_{k=1}^m\widetilde\lambda(I_k)$ for disjoint boxes.

---

# Relate to Other Fields / Compression

Elementary figures are to Lebesgue measure what *step functions* are to the integral and what *simple functions* are to integration theory: the explicitly-computable building blocks on which the theory is *defined*, before any limiting process. The pattern "define on a hand-computable algebra/class, extend by approximation" is universal — step functions $\to$ Riemann integral, [[Def - Simple Function|simple functions]] $\to$ Lebesgue integral, elementary figures $\to$ Lebesgue measure. The half-open convention is the same device that makes the algebra of half-open intervals work in the one-dimensional [[Def - Algebra and σ-Algebra|algebra/$\sigma$-algebra]] counterexample.

---

# Examples / Corollaries

The unit cube $(0,1]^n$ is a box, $\widetilde\lambda=1$. The set $(0,1]\setminus(\tfrac13,\tfrac23]=(0,\tfrac13]\sqcup(\tfrac23,1]$ is an elementary figure of volume $\tfrac23$. A degenerate box like $\{0\}\times(0,1)$ has $\widetilde\lambda=0$.

**Why $\mathcal{A}$ is an algebra:** $\mathbb{R}^n$ is a box; the intersection of two boxes is a box (intersect coordinatewise); the complement of a box is a finite union of disjoint boxes (in 1D, $(a,b]^c=(-\infty,a]\cup(b,\infty)$); finite unions and complements then stay in $\mathcal{A}$ by De Morgan.

**Why $\mathcal{A}$ is *not* a $\sigma$-algebra:** $\bigcup_k(0,1-\tfrac1k]=(0,1)$ is not a *finite* union of intervals' worth of structure that stays in $\mathcal{A}$ — more pointedly, $\mathbb{Q}\cap(0,1)$ is a countable union of singletons but is no elementary figure. This is exactly the gap the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] closes.

Calibration: (i) Is a single point an elementary figure? Yes — the degenerate box $[x,x]$, volume $0$. (ii) Is an open disc an elementary figure? No — not a finite union of boxes. (iii) Is $\widetilde\lambda$ already a measure? No — only a [[Def - Pre-Measure|pre-measure]], since $\mathcal{A}$ is not a $\sigma$-algebra; that it satisfies countable-additivity-within-$\mathcal{A}$ needs a Heine–Borel argument.

---

# Unlocked by This

> [!tip] Lebesgue measure
> Feeding the pre-measure $\widetilde\lambda$ on the algebra of elementary figures into the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory extension theorem]] produces [[Def - Lebesgue Measure|Lebesgue measure]] $\lambda$ on the Borel (and Lebesgue) $\sigma$-algebra of $\mathbb{R}^n$.
