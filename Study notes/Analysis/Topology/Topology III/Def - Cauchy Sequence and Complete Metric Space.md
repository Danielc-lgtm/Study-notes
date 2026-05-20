---
type: definition
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Notation

$(X, d)$ is a metric space — a set $X$ with a function $d : X \times X \to [0, \infty)$ satisfying positivity (with $d(x, y) = 0 \iff x = y$), symmetry, and the triangle inequality. A sequence in $X$ is $\{x_n\}_{n \in \mathbb{N}}$. We write $x_n \to x$ when $d(x_n, x) \to 0$ in $\mathbb{R}$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

A Cauchy sequence is the formal name for a sequence that *looks like* it is converging — its terms are getting closer to each other — even if we have not yet identified a limit. The motivation is operational: in many constructions, you produce a sequence of approximations and you want to argue that they converge to *something*, without needing to know in advance what that something is. The Cauchy condition is the intrinsic version of "convergent": it can be checked using only the terms of the sequence, with no reference to an external limit point.

Here is why this is the right definition. Suppose $x_n \to x$ in some metric space. By the triangle inequality, $d(x_n, x_m) \leq d(x_n, x) + d(x, x_m) \to 0$, so every convergent sequence is Cauchy. The Cauchy condition is therefore *necessary* for convergence. The question becomes: when is it also *sufficient*? When does every Cauchy sequence have a limit in the space? The answer is captured by the property of **completeness**: a metric space $X$ is complete if every Cauchy sequence in $X$ converges to a point of $X$.

Completeness matters because most existence arguments in analysis run as follows: produce a sequence of approximate solutions; show it is Cauchy; appeal to completeness to extract a limit; verify the limit is a genuine solution. Without completeness this argument fails — the sequence may be Cauchy but limit-less, and the existence claim collapses. The Banach fixed-point theorem, the Picard–Lindelöf existence theorem for ODEs, the construction of the integral, the construction of $L^p$ spaces — all are existence theorems whose engine is completeness.

Why define completeness in terms of *all* Cauchy sequences having limits, rather than some weaker condition? Because that is the minimum required for the existence arguments above. A space could have *some* Cauchy sequences converging — say, eventually constant ones, which converge trivially — but the analysis machinery needs every Cauchy sequence to find its limit, since you cannot in general arrange for your approximation sequence to be of any special type.

There is a subtle point: completeness is a property of the *metric*, not of the topology. The interval $(0, 1)$ with the usual metric is not complete (the Cauchy sequence $1/n$ has no limit in $(0, 1)$), but $\mathbb{R}$ with the usual metric is. Yet $(0, 1)$ and $\mathbb{R}$ are *homeomorphic*: the map $x \mapsto \tan(\pi x - \pi/2)$ is a homeomorphism. So homeomorphism does not preserve completeness — two homeomorphic spaces can disagree on whether they are complete. The reason: completeness uses the metric to define Cauchy sequences, and a homeomorphism need not preserve the metric, only the open sets. To get a topological invariant, one defines **completely metrizable** — admitting *some* metric in which the space is complete — and this is genuinely a topological property.

A natural follow-up question: given an incomplete metric space, can we *complete* it? Yes — there is a canonical construction (equivalence classes of Cauchy sequences) producing a complete space $\widehat{X}$ with $X$ embedded as a dense subspace. This is the completion, and it is the right way to think of complete spaces as universal among "completions of $X$". It is also how $\mathbb{R}$ is constructed from $\mathbb{Q}$, and how $L^p$ spaces are constructed from $C_c$ in the $L^p$ norm.

---

# The Definition

Let $(X, d)$ be a metric space.

**Cauchy sequence.** A sequence $\{x_n\}_{n \in \mathbb{N}}$ in $X$ is a **Cauchy sequence** if for every $\varepsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$d(x_n, x_m) < \varepsilon \quad \text{for all } n, m \geq N.$$

Equivalently, $\sup\{d(x_n, x_m) : n, m \geq N\} \to 0$ as $N \to \infty$.

**Complete metric space.** $(X, d)$ is **complete** if every Cauchy sequence $\{x_n\}$ in $X$ converges to a point $x \in X$ — i.e., $d(x_n, x) \to 0$.

**Completion.** The **completion** of a metric space $(X, d)$ is a complete metric space $(\widehat{X}, \widehat{d})$ together with an isometric embedding $\iota : X \to \widehat{X}$ with dense image. It is unique up to canonical isometry, and is constructed by taking the set of equivalence classes of Cauchy sequences in $X$ — where $\{x_n\} \sim \{y_n\}$ if $d(x_n, y_n) \to 0$ — with metric $\widehat{d}([\{x_n\}], [\{y_n\}]) = \lim_n d(x_n, y_n)$ and embedding $\iota(x) = [\{x, x, x, \dots\}]$.

A topological space is **completely metrizable** if it admits *some* metric $d$ in which it is complete; this is a property of the topology, not of any particular metric.

---

# Relate to Other Fields / Compression

The Cauchy condition is the metric-space version of a much broader **net convergence** condition: in a uniform space (which generalizes metric spaces), a **Cauchy net** is one whose tails get arbitrarily small in the uniform structure. Metric spaces are uniform spaces in a canonical way, and metric Cauchy sequences are exactly uniform Cauchy sequences for the induced uniform structure. The general notion of completeness in uniform spaces underlies the existence of Haar measure on locally compact groups and the construction of universal compactifications.

In **functional analysis**, a **Banach space** is a complete normed vector space — the norm gives a metric, and completeness in that metric is the defining property. A **Hilbert space** is a complete inner product space. Completeness is exactly what allows infinite-dimensional vector spaces to support analysis: convergent series of vectors are guaranteed to have limit vectors in the space.

In **probability theory**, a **Polish space** is a separable completely metrizable space — the setting for most of measure-theoretic probability, including the construction of stochastic processes via the Daniell–Kolmogorov theorem and the existence of regular conditional probabilities. A great deal of probability theory implicitly assumes Polish, and what is being assumed is exactly completeness (in some compatible metric) together with separability.

In **number theory** and **$p$-adic analysis**, the **$p$-adic numbers** $\mathbb{Q}_p$ are constructed by completing $\mathbb{Q}$ with respect to the $p$-adic metric, parallel to the construction of $\mathbb{R}$ as the completion in the usual metric. The same construction yields wildly different completions depending on the choice of metric — a striking illustration that completeness depends on the metric and not just the topology.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}^n$ with the Euclidean metric.** Every Cauchy sequence in $\mathbb{R}^n$ converges. This is the defining property of the real numbers as a complete ordered field, and it is the cornerstone of all of real analysis. The Bolzano–Weierstrass theorem (every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence) is essentially equivalent.

**Is NOT an instance — the rationals $\mathbb{Q}$.** The sequence $x_n = (1 + 1/n)^n$ is Cauchy in $\mathbb{Q}$ (it converges in $\mathbb{R}$, hence is Cauchy in $\mathbb{R}$, hence in $\mathbb{Q}$), but its limit $e$ is irrational. So $\mathbb{Q}$ is incomplete; one of the defining properties of $\mathbb{R}$ is being the completion of $\mathbb{Q}$.

**Is NOT an instance — the open interval $(0, 1)$ with the usual metric.** The sequence $1/n$ is Cauchy in $(0, 1)$ but does not converge in $(0, 1)$ (its limit $0$ is not in the space). Yet $(0, 1)$ is homeomorphic to $\mathbb{R}$, which is complete. This is the canonical example that completeness is a metric property, not a topological one. By switching to the metric $d'(x, y) = |\tan(\pi x - \pi/2) - \tan(\pi y - \pi/2)|$, the *same* topological space $(0, 1)$ becomes complete (now $1/n$ is not Cauchy in this new metric, since $\tan(\pi/n - \pi/2) \to -\infty$).

**Is an instance — the Hilbert cube $[0, 1]^\mathbb{N}$ with $d(x, y) = \sum_n |x_n - y_n|/2^n$.** This is a complete metric space, and it is also compact (by Tychonoff and metrizability of countable products). Every Cauchy sequence converges by direct argument: each coordinate sequence is Cauchy in $[0, 1]$ (which is complete), so converges coordinatewise, and coordinatewise convergence in the product topology matches the metric.

**Is an instance — function spaces with uniform convergence.** $C([0, 1])$, the space of continuous real-valued functions on $[0, 1]$ with the supremum norm $\lVert f\rVert_\infty = \sup_x|f(x)|$, is complete. A Cauchy sequence of continuous functions is uniformly Cauchy, hence uniformly convergent, and the uniform limit of continuous functions is continuous. By contrast, $C([0, 1])$ with the $L^1$ norm is *not* complete; its completion is $L^1([0, 1])$.

**Corollary — closed subset of complete is complete.** If $(X, d)$ is complete and $F \subseteq X$ is closed, then $F$ with the inherited metric is complete. A Cauchy sequence in $F$ is Cauchy in $X$, so it converges to some $x \in X$; by closedness of $F$, $x \in F$.

**Corollary — products of complete metric spaces are complete.** A countable product of complete metric spaces $\prod_n X_n$ with the metric $d(x, y) = \sum_n d_n(x_n, y_n)/(2^n(1 + d_n(x_n, y_n)))$ is complete. Each coordinate is Cauchy by the construction, so converges by completeness of $X_n$, and coordinatewise convergence equals product topology convergence.

**Calibration check.** Verify: (i) every convergent sequence is Cauchy; (ii) the sequence $1/n$ in $\mathbb{Q}$ is Cauchy (since $|1/n - 1/m| \to 0$); (iii) the space $C^\infty([0, 1])$ with the sup-norm is *not* complete (the uniform limit of smooth functions need not be smooth); (iv) every Cauchy sequence is bounded (eventually within distance $1$ of $x_N$, hence bounded). If you can explain why $(0, 1) \cong \mathbb{R}$ topologically without contradicting that the former is incomplete and the latter complete, you have understood the distinction between topology and metric.

---

# Unlocked by This

> [!tip] The Banach Fixed Point Theorem *(from Functional Analysis)*
> A strict contraction $T : X \to X$ on a complete metric space has a unique fixed point. The proof iterates the contraction to produce a Cauchy sequence and uses completeness to extract a limit, which is the fixed point. This is the engine of the Picard–Lindelöf theorem, the implicit function theorem, and dozens of other existence proofs. See **Banach contraction mapping principle**.

> [!tip] Baire Category Theorem *(from Functional Analysis)*
> In a complete metric space, the intersection of countably many dense open sets is dense. This is the topological foundation for the **open mapping theorem**, the **closed graph theorem**, and the **uniform boundedness principle** in functional analysis. Completeness is the hypothesis.

> [!tip] Polish Spaces and Regular Conditional Probabilities *(from Probability)*
> A **Polish space** is separable and completely metrizable. The Daniell–Kolmogorov existence theorem for stochastic processes, the existence of regular conditional probabilities, and the disintegration of measures all require Polish-space assumptions, which are completeness assumptions on a compatible metric.

> [!tip] $L^p$ Spaces *(from Measure Theory)*
> $L^p(X, \mu)$ for $1 \leq p \leq \infty$ is complete (the Riesz–Fischer theorem). Its completeness is the technical heart of $L^p$ space theory: it allows Cauchy-in-$L^p$ sequences of functions to have an $L^p$ limit, hence the existence of weak and strong solutions to PDE.
