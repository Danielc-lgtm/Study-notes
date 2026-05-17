---
type: definition
subject: measure-theory
prereqs:
  - "Def - Algebra and σ-Algebra"
  - "Def - Measurable Space"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X, \mathcal{A})$ is a [[Def - Measurable Space|measurable space]]. The extended half-line is $[0,\infty] = [0,\infty) \cup \{\infty\}$, with the conventions $x + \infty = \infty$ and $x \cdot \infty = \infty$ for $x > 0$, and $0 \cdot \infty = 0$. We write $\mu, \nu$ for measures and $\mathbb{P}$ for a probability measure. Sets $A_1, A_2, \dots$ are **pairwise disjoint** if $A_k \cap A_\ell = \emptyset$ for $k \neq \ell$; we write $\bigsqcup$ for a disjoint union.

---

# Axiom Motivation

We now put the *measure* on the stage. A measure must turn each measurable set into a number in $[0,\infty]$ — its size — in a way faithful to our intuition of length, area, volume, mass, probability. Two demands pin down the definition.

First, **the empty set has size zero**: $\mu(\emptyset) = 0$. Without this every measure would be the constant $\infty$ (since $\emptyset = \emptyset \sqcup \emptyset$ would force $\mu(\emptyset) = 2\mu(\emptyset)$, allowing only $0$ or $\infty$, and $\infty$ everywhere is useless). So $\mu(\emptyset)=0$ is the normalisation that rules out the trivial measure.

Second, **size is additive over disjoint pieces**. If you cut a region into non-overlapping parts, the sizes add. The genuine question is *how many* pieces: finitely many, or countably many? Finite additivity is too weak — it cannot relate $\mu$ of a limiting set to $\mu$ of its approximants, and so supports no convergence theorem. Arbitrary (uncountable) additivity is too strong — it would force $\mu([0,1]) = \sum_{x \in [0,1]} \mu(\{x\})$, which is $0$ or $\infty$, never $1$. **Countable additivity** is the precise compromise: it is exactly strong enough to make $\mu$ continuous along monotone sequences of sets (see [[Thm - Properties of Measures]]), hence to support [[Thm - Monotone Convergence Theorem|limit theorems]], and exactly weak enough that nontrivial measures exist. The whole power of Lebesgue's theory over Riemann's traces back to this one choice of "$\sigma$" — countable — additivity.

Why allow the value $\infty$? Because $\mathbb{R}$ has infinite length and we want $\mu$ defined on all Borel sets, not just bounded ones. The extended target $[0,\infty]$ is the price of working with unbounded spaces; the conventions on $\infty$ are chosen to keep countable additivity meaningful even when sizes diverge.

---

# The Definition

Let $(X, \mathcal{A})$ be a measurable space. A **measure** on $(X,\mathcal{A})$ is a function $\mu : \mathcal{A} \to [0,\infty]$ such that

1. $\mu(\emptyset) = 0$;
2. (**$\sigma$-additivity**) for every sequence $A_1, A_2, \dots \in \mathcal{A}$ of pairwise disjoint sets,
$$\mu\!\left( \bigsqcup_{k=1}^\infty A_k \right) = \sum_{k=1}^\infty \mu(A_k).$$

A **measure space** is a triple $(X, \mathcal{A}, \mu)$ consisting of a set $X$, a $\sigma$-algebra $\mathcal{A} \subseteq 2^X$, and a measure $\mu$ on $(X,\mathcal{A})$.

The measure is **finite** if $\mu(X) < \infty$; it is **$\sigma$-finite** if $X = \bigcup_k S_k$ for some $S_k \in \mathcal{A}$ with $\mu(S_k) < \infty$ (see [[Def - σ-Finite Measure]]); it is a **[[Def - Probability Space|probability measure]]** if $\mu(X) = 1$.

There is no convergence issue in (2): the series has non-negative terms, so it converges in $[0,\infty]$ (possibly to $\infty$), and rearrangement is irrelevant.

---

# Categorical Definition

A measure can be viewed as a $\sigma$-additive functional, and measure spaces with measure-preserving maps form a category. More structurally: a finite measure on $(X,\mathcal{A})$ is the same data as a *positive normalised $\sigma$-additive functional* — by the [[Thm - Monotone Convergence Theorem|integration construction]], $\mu$ extends uniquely to a linear, monotone, monotone-continuous functional $f \mapsto \int f\,d\mu$ on non-negative measurable functions. The Riesz representation theorem makes this precise on locally compact spaces: measures *are* the non-negative continuous linear functionals on $C_c(X)$. So a measure is simultaneously a set function and a functional; the two views are equivalent and one passes between them by integration.

---

# Relate to Other Fields / Compression

A measure generalises *length/area/volume* by dropping all dependence on geometry — only the $\sigma$-algebra and additivity remain. A **probability measure** is a measure normalised to total mass $1$; nothing else distinguishes probability theory from measure theory at the foundational level, which is exactly Kolmogorov's insight. The **counting measure** recovers cardinality and turns sums into integrals, so series are a special case of Lebesgue integration. In physics a measure is a *mass distribution* or *charge distribution*; a [[Def - Signed Measure|signed measure]] drops positivity to model charge of both signs. The Dirac measure $\delta_x$ is the point mass / "delta function" made rigorous as an honest measure rather than a function.

---

# Examples / Corollaries

**Counting measure.** On any $(X,\mathcal{A})$, set $\mu(A) = \#A$ (the number of elements, $\infty$ if infinite). $\sigma$-additivity holds because cardinalities of disjoint sets add. On $(\mathbb{N}, 2^{\mathbb{N}})$ this turns the integral into the sum $\int a\, d\mu = \sum_n a_n$.

**Dirac measure.** Fix $x \in X$. Define $\delta_x(A) = 1$ if $x \in A$, and $0$ if $x \notin A$. This is a probability measure — the law of a "random variable" that is deterministically $x$.

**Lebesgue measure.** On $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$, the unique [[Def - Lebesgue Measure|measure λ]] assigning each box its elementary volume. It is $\sigma$-finite but not finite.

**A finite measure built from a density.** For $f \geq 0$ measurable, $\nu(A) = \int_A f\,d\mu$ is a measure ([[Def - Absolute Continuity and Density|with density f]]); $\sigma$-additivity is the [[Thm - Monotone Convergence Theorem|monotone convergence theorem]].

Non-example: finitely additive set functions that fail countable additivity exist (e.g. a "limit density" on $\mathbb{N}$), but they are *not* measures and support no integration theory.

Calibration: (i) Is $\mu(A) = 1$ for all $A \neq \emptyset$, $\mu(\emptyset)=0$, a measure? No — take two disjoint nonempty sets: $\mu(A \sqcup B) = 1 \neq 2 = \mu(A)+\mu(B)$. (ii) Is $\mu(A) = \infty$ for all $A$ a measure? No — $\mu(\emptyset) \neq 0$. (iii) Must a measure be monotone? Yes — that is a *theorem*, not an axiom; see [[Thm - Properties of Measures]].

---

# Unlocked by This

> [!tip] Probability measure *(from [[Advanced Probability I — Probability Spaces and Random Variables|Advanced Probability]])*
> A probability measure is a measure with $\mu(X)=1$. The triple $(\Omega,\mathcal{F},\mathbb{P})$ is a probability space; "measurable function" becomes "[[Def - Random Variable|random variable]]" and "integral" becomes "expectation." See [[Def - Probability Space]].

> [!tip] Integration *(from [[Measure Theory II — Integration|Measure Theory II]])*
> Once a measure is in hand, one builds the integral $\int f\,d\mu$ — first for simple functions, then for non-negative measurable functions by approximation, then for signed integrable functions. See [[Def - The Integral]].
