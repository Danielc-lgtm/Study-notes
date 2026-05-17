---
type: definition
subject: measure-theory
prereqs: []
tags: [analysis, measure-theory, probability]
---

# Notation

Throughout, $X$ is an arbitrary nonempty set and $2^X = \mathcal{P}(X) = \{A : A \subseteq X\}$ is its power set. We write $A^c = X \setminus A$ for the complement of $A$ in $X$, and $\emptyset$ for the empty set. A *family* $\mathcal{A} \subseteq 2^X$ is a collection of subsets of $X$.

---

# Axiom Motivation

We want to assign a "size" — a length, an area, a volume, a probability — to subsets of $X$. The first question is not *how* to measure, but *what* to measure: which subsets are we even allowed to ask about? The collection of "answerable" sets must be closed under exactly the operations we expect a notion of size to respect.

Start from the bare minimum. The whole space $X$ should be measurable (it has *some* size, possibly infinite). If we can measure $A$, we should be able to measure "not $A$", because knowing the size of $A$ and of $X$ ought to pin down the size of $A^c$. And if we can measure two sets, we should be able to measure their union — overlapping regions combine into regions. These three closure properties — containing $X$, closure under complement, closure under finite union — define an **algebra**. Closure under finite intersection then comes for free, since $A \cap B = (A^c \cup B^c)^c$.

An algebra is enough for *finitely* additive size, but analysis lives on limits. We constantly build sets as countable unions: an open set in $\mathbb{R}$ is a countable union of intervals, an event "$X_n$ converges" is a countable combination of simpler events. If the size of a limiting set is to be controlled by the sizes of its pieces, the limiting set must itself be measurable. This forces the decisive strengthening: closure under *countable* unions, not just finite ones. A family closed under countable unions (and complements, and containing $X$) is a **$\sigma$-algebra**. The prefix $\sigma$ signals "countable" throughout measure theory.

Why exactly countable, and not arbitrary? Closure under *arbitrary* unions would make every singleton-generated family explode into the full power set $2^X$, on which no translation-invariant notion of length can exist (this is the content of [[Thm - Existence of a Non-Measurable Set|Vitali's theorem]]). Countability is the precise amount of closure that supports limits and series — which is all analysis needs — while staying small enough to admit nontrivial measures. Weakening (1.3') back to finite unions costs us every convergence theorem; strengthening it to arbitrary unions costs us the existence of measures. The $\sigma$-algebra is the Goldilocks structure.

---

# The Definition

Let $X$ be a set. A family $\mathcal{A} \subseteq 2^X$ is an **algebra** (over $X$) if

1. $X \in \mathcal{A}$;
2. $A \in \mathcal{A} \implies A^c = X \setminus A \in \mathcal{A}$;
3. $A_1, \dots, A_m \in \mathcal{A} \implies \bigcup_{k=1}^m A_k \in \mathcal{A}$ (closure under finite unions).

$\mathcal{A}$ is a **$\sigma$-algebra** if, in addition, (3) holds for countable unions:

3'. $A_1, A_2, \dots \in \mathcal{A} \implies \bigcup_{k=1}^\infty A_k \in \mathcal{A}$.

By De Morgan's laws, a $\sigma$-algebra is automatically closed under countable intersections: $\bigcap_{k=1}^\infty A_k = \left( \bigcup_{k=1}^\infty A_k^c \right)^c$. It also contains $\emptyset = X^c$, and is closed under set difference $A \setminus B = A \cap B^c$ and symmetric difference.

---

# Categorical Definition

A $\sigma$-algebra is a *$\sigma$-complete Boolean algebra* concretely represented as subsets of $X$. The power set $2^X$ is a Boolean algebra under $(\cup, \cap, {}^c)$ — a complemented distributive lattice — and a $\sigma$-algebra is a Boolean subalgebra closed under the additional infinitary operation of countable join. The category of measurable spaces has $\sigma$-algebras as objects (paired with their underlying set) and measurable functions as morphisms; the assignment $X \mapsto 2^X$ is the "discrete" functor, free on a set, and $\{\emptyset, X\}$ is the "indiscrete" cofree one. Every other $\sigma$-algebra on $X$ sits between these two extremes in the lattice of $\sigma$-algebras ordered by inclusion.

---

# Relate to Other Fields / Compression

A $\sigma$-algebra is the same object a topologist calls a collection closed under operations — but with the *closure axioms swapped*. A topology is closed under **arbitrary** unions and **finite** intersections; a $\sigma$-algebra is closed under **countable** unions, **countable** intersections, **and** complement. Topology is asymmetric (open is privileged over closed) and tracks *nearness*; a $\sigma-$algebra is symmetric and tracks *information*. In probability the same family is read as the collection of **events** — yes/no questions one can ask — and a sub-$\sigma$-algebra encodes "partial information"; this is exactly the [[Def - Filtration|filtration]] picture. In information theory the coarser the $\sigma$-algebra, the less can be resolved about a signal. An algebra (finite-union closure only) is the natural home of *finitely additive* set functions; promoting it to a $\sigma$-algebra is what makes *countably additive* measures, and hence limits, possible.

---

# Examples / Corollaries

The smallest $\sigma$-algebra on any $X$ is the **trivial** one $\{\emptyset, X\}$; the largest is the **discrete** one $2^X$. Every $\sigma$-algebra lies between them. More generally, for any single $A \subseteq X$, the family $\{\emptyset, A, A^c, X\}$ is a $\sigma$-algebra — the smallest one containing $A$.

Every $\sigma$-algebra is an algebra, but the converse fails. The standard counterexample lives on $X = (0,1]$: let $\mathcal{A}$ consist of $\emptyset$ together with all finite disjoint unions $\bigcup_{k=1}^m (a_k, b_k]$ of half-open intervals. This $\mathcal{A}$ is an algebra — the complement of $(a,b]$ is $(0,a] \cup (b,1]$, again a finite union — but it is *not* a $\sigma$-algebra: taking $A_k = (0, 1 - \tfrac1k]$ gives $\bigcup_{k=1}^\infty A_k = (0,1) \notin \mathcal{A}$. This is the gap between finite and countable closure made concrete, and it is precisely the gap that the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] bridges.

A useful infinite example: for $X$ uncountable, the family $\mathcal{A} = \{A \subseteq X : A \text{ or } A^c \text{ is countable}\}$ — the **countable–cocountable** $\sigma$-algebra — is a genuine $\sigma$-algebra. (A countable union of countable sets is countable; if one of the $A_k$ has countable complement, so does the union.) It carries the measure $\mu(A) = 0$ if $A$ is countable, $\mu(A) = 1$ if $A^c$ is countable.

Calibration checks. (i) Is $2^{\mathbb{N}}$ a $\sigma$-algebra? Yes — every union of subsets of $\mathbb{N}$ is a subset of $\mathbb{N}$. (ii) Is the family of *finite* subsets of $\mathbb{N}$ an algebra? No — it fails (1), since $\mathbb{N}$ itself is infinite, and fails (2). (iii) Is the family of *finite-or-cofinite* subsets of $\mathbb{N}$ an algebra? Yes. A $\sigma$-algebra? No — $\bigcup_n \{2n\}$ is the evens, neither finite nor cofinite. If you can verify these three you have understood where finite closure and countable closure part ways.

---

# Unlocked by This

> [!tip] Filtration *(from [[Advanced Probability II — Convergence and Limit Theorems|Advanced Probability]] / Martingale Theory)*
> A *filtration* is an increasing chain $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots$ of sub-$\sigma$-algebras of a fixed $\sigma$-algebra $\mathcal{F}$, modelling information that accumulates with time. The $\sigma$-algebra axioms are exactly what guarantee each $\mathcal{F}_n$ is a coherent "state of knowledge." See [[Def - Filtration]].

> [!tip] Generated $\sigma$-algebra and the Borel sets
> The intersection of any collection of $\sigma$-algebras is a $\sigma$-algebra, which lets one define the smallest $\sigma$-algebra containing a prescribed family — see [[Def - Generated σ-Algebra]] and [[Def - Borel σ-Algebra]].
