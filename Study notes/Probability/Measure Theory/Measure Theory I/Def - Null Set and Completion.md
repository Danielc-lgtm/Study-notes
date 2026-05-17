---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measure and Measure Space"
  - "Def - Borel σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ is a [[Def - Measure and Measure Space|measure space]]. $\mathcal{N}$ is the family of (sub-)null sets; $(X,\mathcal{A}^*,\mu^*)$ the completion.

---

# Axiom Motivation

A **null set** is a set of measure zero — negligible, invisible to the measure. The whole style of measure theory is to ignore what happens on null sets: functions equal "[[Def - Almost Everywhere|almost everywhere]]" are identified, convergence is demanded only "almost everywhere," $L^p$ is a space of equivalence classes. For this to be coherent, the negligible sets had better behave well.

They do, up to one annoyance. The null sets of a $\sigma$-algebra are closed under countable unions ([[Thm - Properties of Measures|σ-subadditivity]]: a countable union of measure-zero sets has measure zero). But they need not be closed under taking *subsets within the $\sigma$-algebra* — and worse, a subset $N'\subseteq N$ of a Borel null set $N$ need not itself be *Borel*. Then "$\mu(N')$" is literally undefined, even though $N'$ is morally negligible (it sits inside something of measure $0$). This is not a rare pathology: most subsets of the Cantor set are not Borel, yet the Cantor set is Lebesgue-null, so *most negligible sets are not in the Borel $\sigma$-algebra at all*.

The fix is **completion**: enlarge the $\sigma$-algebra by *declaring every subset of a null set measurable*, with measure $0$. A measure space where this already holds — every subset of a null set is measurable — is called **complete**. Completion is the smallest enlargement making a measure space complete. The payoff is technical hygiene: in a complete space, "a function defined almost everywhere" or "a function equal a.e. to a measurable one" is automatically measurable, and one never has to check that an exceptional set is Borel. The [[Def - Carathéodory Measurable Sets|Carathéodory construction]] produces complete measures automatically — which is why the **Lebesgue $\sigma$-algebra** is complete and strictly larger than the Borel one.

---

# The Definition

Let $(X,\mathcal{A},\mu)$ be a measure space.

A set $N\in\mathcal{A}$ is **$\mu$-null** if $\mu(N)=0$. A property holds **[[Def - Almost Everywhere|μ-almost everywhere]]** ($\mu$-a.e.) if the set where it fails is contained in a null set.

The measure space is **complete** if every subset of a null set is itself measurable: $N\in\mathcal{A}$, $\mu(N)=0$, $N'\subseteq N\implies N'\in\mathcal{A}$.

The **completion** of $(X,\mathcal{A},\mu)$ is $(X,\mathcal{A}^*,\mu^*)$ where
$$\mathcal{A}^*=\sigma\big(\mathcal{A}\cup\mathcal{N}\big),\qquad \mathcal{N}=\{N'\subseteq X : N'\subseteq N\text{ for some }N\in\mathcal{A}\text{ with }\mu(N)=0\},$$
equivalently $\mathcal{A}^*=\{A\,\triangle\,N' : A\in\mathcal{A},\ N'\in\mathcal{N}\}$, with $\mu^*(A\,\triangle\,N')=\mu(A)$. This is the smallest complete $\sigma$-algebra containing $\mathcal{A}$, and $\mu^*$ the unique extension of $\mu$ to it.

For $(\mathbb{R}^n,\mathcal{B}(\mathbb{R}^n),\lambda)$, the completion is the **Lebesgue $\sigma$-algebra** $\mathcal{B}^*(\mathbb{R}^n)$; its members are the **Lebesgue-measurable** sets.

---

# Relate to Other Fields / Compression

Completion is the measure-theoretic analogue of *completing a metric space* (adjoin limit points) or *taking the integral closure of a ring* — adjoin the "missing" elements forced by the structure, here the subsets of null sets. It is idempotent: completing a complete space changes nothing. In probability the completion is standard practice: the "[[Def - Filtration|usual conditions]]" on a filtration demand $\mathcal{F}_0$ contain all $\mathbb{P}$-null sets, precisely so that a.s.-defined random variables are honestly measurable and one never argues about exceptional Borel sets.

---

# Examples / Corollaries

In $\mathbb{R}$: every countable set is Lebesgue-null ($\lambda(\{x\})=0$, [[Thm - Properties of Measures|σ-subadditivity]]), so $\mathbb{Q}$ is null. The Cantor set is an *uncountable* null set. Since the Cantor set has $2^{\aleph_0}$ subsets but the Borel $\sigma$-algebra has only $2^{\aleph_0}$ *total* elements while the Lebesgue $\sigma$-algebra has $2^{2^{\aleph_0}}$, **most subsets of the Cantor set are Lebesgue-measurable but not Borel** — this is the strict inclusion $\mathcal{B}(\mathbb{R})\subsetneq\mathcal{B}^*(\mathbb{R})$, and it is *why* completion is necessary.

The Carathéodory construction is automatically complete: any subset of a $\mu^*$-outer-measure-zero set satisfies the [[Def - Carathéodory Measurable Sets|Carathéodory criterion]]. So Lebesgue measure, built that way, is already complete on $\Sigma$.

Calibration: (i) Is $\{0\}$ a null set in $(\mathbb{R},\mathcal{B},\lambda)$? Yes. (ii) Is $(\mathbb{R},\mathcal{B}(\mathbb{R}),\lambda)$ complete? No — a non-Borel subset of the Cantor set is null-but-unmeasurable; this is the very reason completion exists. (iii) Does completion change the measure of a Borel set? No — $\mu^*$ extends $\mu$ without altering it.

---

# Unlocked by This

> [!tip] Almost-everywhere reasoning and $L^p$ spaces
> Completion makes "[[Def - Almost Everywhere|μ-a.e.]]" reasoning friction-free: a function equal a.e. to a measurable function is measurable. This underlies the construction of [[Def - Lp Spaces|Lᵖ spaces]] as spaces of equivalence classes modulo a.e. equality.

> [!tip] Usual conditions on a filtration *(from Martingale Theory)*
> Augmenting a [[Def - Filtration|filtration]] with all null sets — part of the "usual conditions" — is exactly completion applied in continuous-time probability.
