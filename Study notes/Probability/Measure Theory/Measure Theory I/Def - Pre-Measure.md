---
type: definition
subject: measure-theory
prereqs:
  - "Def - Algebra and σ-Algebra"
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory]
---

# Notation

$X$ is a set, $\mathcal{A} \subseteq 2^X$ an [[Def - Algebra and σ-Algebra|algebra]] (not necessarily a $\sigma$-algebra). $\widetilde\mu$ denotes a pre-measure. $[0,\infty]$ is the extended half-line.

---

# Axiom Motivation

Here is the practical obstacle the whole construction of measures answers. We *know* what volume we want to assign to simple sets — a box should get its elementary volume $\prod(b_k-a_k)$, an interval should get its length. These simple sets form an [[Def - Algebra and σ-Algebra|algebra]] (closed under finite unions, complements), and on that algebra our intended size function is easy to write down. What we cannot do directly is define a size on the full Borel $\sigma$-algebra — there is no formula for "the volume of an arbitrary Borel set."

So the strategy is: define the size *only* on the algebra, where it is easy, and then *extend* it to the generated $\sigma$-algebra by a machine. A **pre-measure** is the input to that machine: a set function on an algebra that is already as good as a measure *to the extent the algebra allows*. It satisfies $\widetilde\mu(\emptyset)=0$ and it is countably additive — but the countable-additivity demand can only be tested on those countable disjoint unions that *happen to land back inside the algebra*, since the algebra is not closed under countable unions.

That last clause is the entire subtlety. Finite additivity on an algebra is cheap. Demanding countable additivity *whenever the union stays in the algebra* is a genuine, checkable condition — it is equivalent to the **continuity property** (if $A_k \downarrow \emptyset$ in $\mathcal{A}$ with $\widetilde\mu(A_1)<\infty$ then $\widetilde\mu(A_k)\to 0$), and verifying it for the elementary-volume function is exactly where a *compactness* argument (Heine–Borel) enters. A pre-measure is a finitely additive set function that has *passed* this countable-additivity test; the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] then guarantees it extends, and the test is precisely what is needed for the extension to be countably additive.

---

# The Definition

Let $\mathcal{A} \subseteq 2^X$ be an **algebra**. A **pre-measure** on $X$ is a function $\widetilde\mu : \mathcal{A} \to [0,\infty]$ such that

1. $\widetilde\mu(\emptyset) = 0$;
2. (**countable additivity within $\mathcal{A}$**) whenever $A_1, A_2, \dots \in \mathcal{A}$ are pairwise disjoint **and** $\bigsqcup_{k=1}^\infty A_k \in \mathcal{A}$,
$$\widetilde\mu\!\left(\bigsqcup_{k=1}^\infty A_k\right) = \sum_{k=1}^\infty \widetilde\mu(A_k).$$

The difference from a genuine [[Def - Measure and Measure Space|measure]] is solely the domain: a measure lives on a $\sigma$-algebra, where every countable union is in the domain; a pre-measure lives on an algebra, where (2) is a *conditional* statement, vacuous unless the union happens to lie in $\mathcal{A}$.

---

# Relate to Other Fields / Compression

A pre-measure is to a measure what a *recipe defined on a generating set* is to the structure it generates — the same relationship as a bilinear form on a basis (extends to all of $V\otimes V$), or a homomorphism defined on generators of a group (extends if the relations are respected). The "relations" that must be respected here are exactly countable additivity-within-$\mathcal{A}$. In probability, a pre-measure on the algebra of *cylinder sets* of an infinite product, satisfying a compatibility condition, extends to a measure on the product $\sigma$-algebra — this is the Kolmogorov extension theorem, the device that constructs stochastic processes.

---

# Examples / Corollaries

**Elementary volume.** On $\mathbb{R}^n$, let $\mathcal{A}$ be the algebra of [[Def - Interval and Elementary Figure|elementary figures]] (finite disjoint unions of boxes). Define $\widetilde\lambda$ of a box to be $\prod_k(b_k-a_k)$, extended additively. That $\widetilde\lambda$ is a pre-measure — countably additive within $\mathcal{A}$ — is a genuine theorem ([[Thm - Hahn-Carathéodory Extension Theorem|Lemma 1.16]]), whose proof needs the Heine–Borel compactness of closed bounded boxes. This pre-measure is the seed of [[Def - Lebesgue Measure|Lebesgue measure]].

**A finitely additive non-pre-measure.** A finitely additive set function on an algebra that *fails* the countable-additivity test is not a pre-measure and does not extend to a measure; "limiting density" on subsets of $\mathbb{N}$ is the standard example.

Calibration: (i) Is every measure a pre-measure? Yes — restrict the domain from a $\sigma$-algebra to itself qua algebra; condition (2) is then unconditional. (ii) Is a finitely additive set function on an algebra automatically a pre-measure? No — countable additivity-within-$\mathcal{A}$ can fail. (iii) Where in the box example is compactness used? To pass from a countable cover of a *closed bounded* box to a finite subcover, converting countable additivity into finite additivity.

---

# Unlocked by This

> [!tip] The extension machine
> A pre-measure feeds into the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory extension theorem]]: it is extended first to an [[Def - Outer Measure|outer measure]] on all of $2^X$, then restricted to the [[Def - Carathéodory Measurable Sets|Carathéodory $\sigma$-algebra]], on which it becomes a genuine measure.
