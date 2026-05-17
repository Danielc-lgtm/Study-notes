---
type: definition
subject: measure-theory
prereqs:
  - "Def - Outer Measure"
  - "Def - Algebra and σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

$\mu^*$ is an [[Def - Outer Measure|outer measure]] on $X$. $\Sigma$ denotes the family of Carathéodory-measurable sets. For $A \subseteq X$ and a "test set" $B \subseteq X$, recall $B \setminus A = B \cap A^c$.

---

# Axiom Motivation

An [[Def - Outer Measure|outer measure]] $\mu^*$ is defined on every subset of $X$ but is only *sub*additive — it can over-count. We want to isolate the subsets on which it is genuinely *additive*, because those will form a $\sigma$-algebra carrying a real measure. The question is: what is the right test for "$A$ is well-behaved"?

The naive guess — "$\mu^*(A) + \mu^*(A^c) = \mu^*(X)$" — works only when $\mu^*(X)<\infty$ and is fragile. Carathéodory's insight was to demand additivity not just for the single splitting $X = A \sqcup A^c$, but for the splitting of *every possible test set* $B$ by $A$:
$$\mu^*(B) = \mu^*(B \cap A) + \mu^*(B \setminus A) \qquad \text{for all } B \subseteq X.$$
Read this as: "$A$ slices every set cleanly into the part inside $A$ and the part outside, with no loss of measure." A set $A$ that passes this test for *all* $B$ is a set on which $\mu^*$ behaves additively in the strongest possible local sense.

Why is this the *right* criterion, as opposed to merely *a* criterion? Three reasons, and they are exactly the payoff theorem ([[Thm - Carathéodory's σ-Algebra]]). First, it is *self-improving*: the family $\Sigma$ of all such $A$ turns out to be a full $\sigma$-algebra, not just an algebra — the universal quantifier over test sets $B$ is what powers the countable-union argument. Second, $\mu^*$ *restricted to $\Sigma$ is countably additive*, a genuine measure. Third, the criterion is *checkable on generators*: to show the original algebra $\mathcal{A}$ sits inside $\Sigma$ one only verifies the splitting for $A \in \mathcal{A}$. Because subadditivity gives "$\leq$" for free, only the reverse inequality $\mu^*(B) \geq \mu^*(B\cap A)+\mu^*(B\setminus A)$ ever needs proof — the criterion is half-automatic.

---

# The Definition

Let $\mu^*$ be an outer measure on $X$. A set $A \subseteq X$ is **Carathéodory-measurable** (with respect to $\mu^*$) if
$$\mu^*(B) = \mu^*(B \cap A) + \mu^*(B \setminus A) \qquad \text{for every } B \subseteq X.$$
The collection of all such sets is denoted
$$\Sigma = \big\{ A \subseteq X : \mu^*(B) = \mu^*(B\cap A) + \mu^*(B\setminus A)\ \forall B \subseteq X \big\}.$$

By countable subadditivity of $\mu^*$, the inequality "$\leq$" always holds; hence $A \in \Sigma$ **if and only if** $\mu^*(B) \geq \mu^*(B\cap A) + \mu^*(B\setminus A)$ for all $B$. By [[Thm - Carathéodory's σ-Algebra|Carathéodory's theorem]], $\Sigma$ is a $\sigma$-algebra and $\mu := \mu^*|_\Sigma$ is a [[Def - Measure and Measure Space|measure]].

---

# Relate to Other Fields / Compression

The Carathéodory criterion is the measure-theoretic version of the principle "*an element is good if it interacts well with everything*." Compare: a vector subspace $V$ splits $H = V \oplus V^\perp$ orthogonally; a *normal* subgroup is one that conjugation leaves invariant *for every group element*; a *central* idempotent splits a ring. In each case a universal quantifier ("for all test objects") promotes a local condition into a structural decomposition. Here the condition "$A$ splits every $B$ additively" promotes $A$ into a measurable set, and the universal quantifier over $B$ is exactly what makes $\Sigma$ closed under countable unions rather than merely finite ones.

---

# Examples / Corollaries

**Null sets are always measurable.** If $\mu^*(A)=0$, then for any $B$: $\mu^*(B\cap A)\le\mu^*(A)=0$ and $\mu^*(B\setminus A)\le\mu^*(B)$, so $\mu^*(B\cap A)+\mu^*(B\setminus A)\le\mu^*(B)$ — the criterion holds. Hence $\Sigma$ is automatically **complete**: it contains every subset of a null set.

**The generating algebra is measurable.** In the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]], the algebra $\mathcal{A}$ one started from satisfies $\mathcal{A} \subseteq \Sigma$ — proved by the half-automatic inequality above. Since $\Sigma$ is a $\sigma$-algebra, $\sigma(\mathcal{A}) \subseteq \Sigma$.

**For Lebesgue outer measure**, $\Sigma$ is the $\sigma$-algebra of [[Def - Lebesgue Measure|Lebesgue-measurable sets]] $\mathcal{B}^*(\mathbb{R}^n)$, which strictly contains the Borel sets and strictly excludes the [[Thm - Existence of a Non-Measurable Set|Vitali set]].

Calibration: (i) Does $\emptyset \in \Sigma$? Yes — $\mu^*(B\cap\emptyset)+\mu^*(B\setminus\emptyset) = 0 + \mu^*(B)$. (ii) Is $\Sigma$ closed under complement? Yes, immediately — the criterion for $A$ and for $A^c$ are the *same equation* with the two terms swapped. (iii) Why need only "$\geq$" be checked? Because subadditivity gives "$\leq$" gratis.
