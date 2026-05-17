---
type: definition
subject: measure-theory
prereqs:
  - "Def - Algebra and σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

$X$ is a set, $\mathcal{A} \subseteq 2^X$ a [[Def - Algebra and σ-Algebra|$\sigma$-algebra]]. The pair $(X, \mathcal{A})$ is a measurable space; elements of $\mathcal{A}$ are measurable sets.

---

# Axiom Motivation

Before we can measure, we must declare *what* is measurable. A measurable space is that declaration, frozen into a single object: the set $X$ of points, together with the $\sigma$-algebra $\mathcal{A}$ of subsets we are entitled to assign a size to. No measure is attached yet — a measurable space is the *stage*, not the *play*.

Bundling $X$ and $\mathcal{A}$ into one symbol is not bookkeeping pedantry. The same $X$ carries many different $\sigma$-algebras, and the choice genuinely changes the mathematics: which functions count as [[Def - Measurable Function|measurable]], which sets count as events, how much information is resolvable. In analysis one usually fixes $\mathcal{A}$ (the Borel sets) and varies the measure; in probability the measure $\mathbb{P}$ is fixed and the sub-$\sigma$-algebra varies, encoding "how much one is allowed to observe." Naming the pair makes the dependence on $\mathcal{A}$ explicit and lets us speak of maps *between* measurable spaces — the measurable functions — which are the morphisms of the whole theory.

---

# The Definition

A **measurable space** is a pair $(X, \mathcal{A})$ where $X$ is a set and $\mathcal{A} \subseteq 2^X$ is a $\sigma$-algebra over $X$. The elements of $\mathcal{A}$ are called **measurable sets**.

A measurable space carries no measure. To obtain a [[Def - Measure and Measure Space|measure space]] one additionally specifies a measure $\mu : \mathcal{A} \to [0,\infty]$.

---

# Categorical Definition

Measurable spaces are the objects of a category $\mathbf{Meas}$; its morphisms $(X,\mathcal{A}) \to (Y,\mathcal{B})$ are the [[Def - Measurable Function|measurable maps]] $f$, those with $f^{-1}(B) \in \mathcal{A}$ for all $B \in \mathcal{B}$. This is the exact analogue of $\mathbf{Top}$ (topological spaces, continuous maps): a measurable map is "continuous for the $\sigma$-algebra structure," with preimages of measurable sets measurable just as preimages of open sets are open. The forgetful functor $\mathbf{Meas} \to \mathbf{Set}$ has a left adjoint (the discrete $\sigma$-algebra $2^X$) and a right adjoint (the indiscrete $\{\emptyset,X\}$).

---

# Relate to Other Fields / Compression

A measurable space is to measure theory what a topological space is to analysis and what a set-with-a-base-point is to homotopy theory: the minimal carrier on which the real structure (a measure) will later be imposed. In probability the measurable space is $(\Omega, \mathcal{F})$ — the [[Def - Probability Space|sample space and its events]] — and a sub-$\sigma$-algebra $\mathcal{G} \subseteq \mathcal{F}$ on the *same* $\Omega$ is "the same stage observed with less resolution," the seed of [[Def - Conditional Expectation|conditional expectation]] and [[Def - Filtration|filtrations]].

---

# Examples / Corollaries

$(X, 2^X)$ — every set with its power set — is a measurable space, the finest possible. $(X, \{\emptyset, X\})$ is the coarsest. $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ with the [[Def - Borel σ-Algebra|Borel $\sigma$-algebra]] is the default measurable space of analysis. $(\Omega, \mathcal{F})$ in probability is a measurable space awaiting a probability measure.

Corollary (restriction): if $(X, \mathcal{A})$ is a measurable space and $A \subseteq X$, then $\mathcal{A}|_A = \{A \cap B : B \in \mathcal{A}\}$ is a $\sigma$-algebra on $A$, so $(A, \mathcal{A}|_A)$ is again a measurable space — the **trace** or restricted measurable space.

Calibration: (i) Is $(\mathbb{R}, \{\emptyset, \mathbb{Q}, \mathbb{Q}^c, \mathbb{R}\})$ a measurable space? Yes — that four-element family is a $\sigma$-algebra. (ii) Is $(\mathbb{N}, \{\text{finite subsets of } \mathbb{N}\})$ a measurable space? No — finite subsets do not form a $\sigma$-algebra. (iii) Does a measurable space determine a measure? No — that requires the extra datum $\mu$.
