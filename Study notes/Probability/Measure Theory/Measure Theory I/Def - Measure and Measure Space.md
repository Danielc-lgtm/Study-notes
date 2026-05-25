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

We now put the *measure* on the stage. The [[Def - Algebra and σ-Algebra|σ-algebra]] supplied the *vocabulary* — the sets one is allowed to ask about — and the measure supplies the *answer*: a function $\mu : \mathcal{A} \to [0,\infty]$ assigning each measurable set a numerical size. Three axioms pin the definition down, and the right way to motivate them is to drop each one in turn and watch a concrete pathology emerge.

The first axiom is **$\mu(\emptyset) = 0$**. The empty set has size zero by the meaning of the word "empty" — there is nothing there to be measured — but the axiom is not merely cosmetic, because countable additivity alone does *not* force it: write $\emptyset = \emptyset \sqcup \emptyset \sqcup \emptyset \sqcup \cdots$, the empty set as a countable disjoint union of copies of itself, then $\sigma$-additivity gives $\mu(\emptyset) = \sum_{k=1}^\infty \mu(\emptyset)$, which holds only when $\mu(\emptyset) \in \{0, \infty\}$. Drop the axiom and the trivial measure $\mu \equiv \infty$ on every set is admitted, including the empty one — and once admitted it propagates: every union of disjoint sets has size $\infty$, distinctions collapse, integration becomes meaningless. The axiom $\mu(\emptyset) = 0$ is the *normalisation* that excludes this degenerate solution and selects the meaningful branch of the equation $x = \sum_{k=1}^\infty x$. Without it the entire theory has no anchor: in probability, $\mathbb{P}(\Omega) = 1$ would be undermined by $\mathbb{P}(\emptyset) = \infty$.

The second axiom is **positivity**, $\mu(A) \ge 0$, encoded by the codomain being $[0,\infty]$ rather than $(-\infty, \infty]$ or $\mathbb{R}$. Lengths, areas, volumes, probabilities, masses are all non-negative — the word "size" carries positivity in its meaning. Drop positivity and you do *not* arrive at a slightly more general theory; you arrive at a *fundamentally different* theory, that of [[Def - Signed Measure|signed measures]], whose entire structure is governed by the [[Thm - Hahn and Jordan Decomposition|Hahn–Jordan decomposition theorem]]: every signed measure splits uniquely as $\mu = \mu^+ - \mu^-$, the difference of two positive measures on complementary "positive" and "negative" sets. Positivity is what makes the convergence theorems work directly: for [[Thm - Monotone Convergence Theorem|MCT]] one needs $f_n \uparrow f$ pointwise and $f_n \ge 0$, and the proof leverages the fact that $\int f_n \, d\mu$ is a monotone sequence in $[0,\infty]$ — *uses* positivity at every step. Without positivity, terms in $\sigma$-additivity $\sum \mu(A_k)$ could cancel in delicate ways, and even the convergence of the sum becomes a question (it could be conditionally convergent, dependent on the ordering of the $A_k$). Positivity is what makes the series *absolutely* convergent and the order of disjoint summation irrelevant. Charge distributions in physics live in the signed world; lengths, masses, and probabilities live in the positive world, and the positivity axiom marks the boundary.

The third axiom — and the deepest — is **countable additivity** ($\sigma$-additivity): for any sequence $A_1, A_2, \dots$ of pairwise disjoint sets, $\mu(\bigsqcup_k A_k) = \sum_k \mu(A_k)$. Disjoint pieces have sizes that add; the question is over *how many* pieces. Drop $\sigma$-additivity down to *finite* additivity (require the equality only for finite disjoint unions, $\mu(A \sqcup B) = \mu(A) + \mu(B)$) and a genuinely different theory emerges, the world of **finitely additive measures**, in which Banach–Tarski-style paradoxes proliferate: in $\mathbb{R}^3$ one can find a finitely additive rotation-invariant measure defined on *all* subsets (the [[Thm - Existence of a Non-Measurable Set|Vitali]] obstruction comes from countable, not finite, additivity), at the cost that the unit ball can be decomposed into finitely many pieces and reassembled by rotation into *two* balls of equal volume. The pathology is not exotic — banking and finance use finitely additive set functions like asymptotic density on $\mathbb{N}$ (the "natural density" $d(A) = \lim_n |A \cap [1,n]|/n$, which is finitely but not $\sigma$-additive: it assigns density zero to each singleton but density one to $\mathbb{N}$, in flagrant violation of $\sigma$-additivity). The point is that finite additivity is *too weak*: it cannot relate $\mu(\bigcup_n A_n)$ for increasing $A_n$ to the limit of $\mu(A_n)$, and so supports no convergence theorem. Without [[Thm - Properties of Measures|monotone continuity]] of $\mu$ — which is the equivalent formulation of $\sigma$-additivity — [[Thm - Monotone Convergence Theorem|MCT]], [[Thm - Dominated Convergence Theorem|DCT]], and [[Thm - Fatou's Lemma|Fatou]] all collapse, and Riemann integration is the best one can hope for.

Why not strengthen $\sigma$-additivity to *arbitrary* (uncountable) additivity, $\mu(\bigsqcup_{i \in I} A_i) = \sum_{i \in I} \mu(A_i)$ for arbitrary index sets $I$? Because this is *inconsistent* with the existence of any non-atomic measure assigning positive finite total mass. Take $[0,1]$ with Lebesgue measure; it is the disjoint union of its singletons, $[0,1] = \bigsqcup_{x \in [0,1]} \{x\}$, and each singleton has Lebesgue measure zero. Arbitrary additivity would force $\mu([0,1]) = \sum_{x \in [0,1]} 0$, and the only sensible interpretation of an uncountable sum of zeros is zero — not $1$. So arbitrary additivity forces every non-atomic measure to assign $\mu([0,1]) = 0$, hence (by translation invariance plus subadditivity) $\mu(\mathbb{R}) = 0$, hence the trivial measure. Atomic measures (sums of point masses) survive arbitrary additivity, but the entire continuum theory does not. Countable additivity is the unique Goldilocks threshold: strong enough that monotone continuity holds and convergence theorems work, weak enough that singletons can have measure zero without forcing the whole space to. The choice "$\sigma$" — countable — recurs throughout because it is the *only* choice that admits both pointwise smallness and total largeness.

A final design choice, easy to overlook: why allow the value **$\infty$**? Because we want $\mu$ defined on *all* sets in the $\sigma$-algebra, including unbounded ones. Lebesgue measure on $\mathbb{R}$ assigns $\lambda(\mathbb{R}) = \infty$, $\lambda([0, \infty)) = \infty$; counting measure on $\mathbb{N}$ assigns $\mu(\mathbb{N}) = \infty$. Restricting to finite-valued measures would exclude these foundational examples and force a separate theory of "$\sigma$-finite" approximations from the outset. The extended target $[0,\infty]$ with the conventions $x + \infty = \infty$, $0 \cdot \infty = 0$, and $\infty \cdot x = \infty$ for $x > 0$ is the price of working with unbounded spaces, and the conventions are chosen so that countable additivity remains meaningful even when individual or total sizes diverge — $\sum_k \mu(A_k)$ is unambiguous in $[0,\infty]$ regardless of convergence in the ordinary sense, because monotone partial sums always have a supremum in $[0,\infty]$.

These three axioms are the minimal scaffold; everything else is a theorem. The non-trivial *existence* of measures on rich $\sigma$-algebras — Lebesgue measure on the Borel $\sigma$-algebra of $\mathbb{R}^n$, [[Def - Lebesgue Measure|Borel measures]] on locally compact Hausdorff spaces, [[Thm - Product Measure|product measures]] on infinite products — is delivered by [[Thm - Hahn-Carathéodory Extension Theorem|Carathéodory's extension theorem]], which takes a $\sigma$-additive set function defined on a generating algebra (where additivity is much easier to check, since one is only working with finite disjoint unions of "elementary" sets) and extends it uniquely to a measure on the generated $\sigma$-algebra. The construction of [[Def - Lebesgue Measure|Lebesgue measure]] from the elementary volume of boxes is the prototypical application: one defines $\lambda(\prod_i [a_i, b_i)) = \prod_i (b_i - a_i)$ on the algebra of finite disjoint unions of boxes, verifies the much easier countable-additivity-on-the-algebra condition, and Carathéodory delivers Lebesgue measure on all Borel sets. The same machine produces every measure encountered in practice, including the Lebesgue–Stieltjes measures and the [[Thm - Product Measure|product measures]] that underlie probability theory.

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
