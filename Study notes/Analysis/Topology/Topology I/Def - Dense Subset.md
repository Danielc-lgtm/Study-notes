---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Closure, Interior, and Boundary"
  - "Def - First and Second Countable"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space, $A \subseteq X$ a subset. The closure of $A$ in $X$ is $\overline{A}$. We say $A$ is **dense in $X$** when the relevant condition holds; the qualifier is sometimes elided if the ambient space is clear. The collection of continuous real-valued functions on $[0,1]$ is $C[0,1]$; the $L^p$-space on a measure space is $L^p$; the smooth compactly supported functions are $C^\infty_c$. The full notation registry sits on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

We have a topological space $X$ and we want to identify the subsets $A$ that are *spread out everywhere* — that come arbitrarily close to every point of $X$. The intuition is approximation: a dense set is one any element of which can be substituted for any point of $X$ to within arbitrary "topological accuracy". The rationals approximate the reals; the polynomials approximate the continuous functions; the smooth compactly supported functions approximate the integrable functions. The definition of density should be the precise topological encoding of this approximation property.

The first formulation one writes is: "$A$ is dense if every point of $X$ is a limit of points of $A$". In a metric space this works: it says every $x \in X$ has a sequence $a_n \in A$ with $a_n \to x$. But in a general topological space, "limit of a sequence" is too weak (see [[Thm - Characterizations of the Closure]]). The right formulation drops sequences and uses the topology directly: $A$ is dense if it can be *touched* from every point — every open neighbourhood of every point contains a point of $A$. Equivalently — and this is the clean form — $A$ is dense if its closure is the whole space:
$$\overline{A} = X.$$
This is the formula one carries. It says: "$A$ already includes everything topologically reachable from itself, which is everything". The equivalence to "every nonempty open set meets $A$" follows from the closure characterization (see [[Thm - Characterizations of the Closure]]).

Why is this the right notion? Because it is exactly the condition that makes the strategic move of **density-as-approximation** legitimate. Suppose you want to prove a property $P$ holds for every $x \in X$. Three steps: (i) prove $P$ for $x \in A$ — often easier because $A$ consists of "nice" objects; (ii) show that $P$ is preserved by limits — a continuity argument; (iii) since every $x \in X$ is in $\overline{A}$, the limit-preservation extends $P$ from $A$ to $X$. The strategy is overwhelmingly common — it threads through analysis, probability, PDE — and the topological prerequisite for step (iii) is precisely *density*.

There is also a *dual* notion to capture: subsets that are *not* spread out, that are confined to a topologically negligible part of $X$. The natural condition is: the closure of $A$ has empty interior. This is **nowhere dense**. Nowhere dense sets are the small sets of topology, in the sense that countable unions of them are still small in complete spaces (Baire's theorem). The pair (dense, nowhere dense) is a topological complementarity: dense sets are "large enough to approximate", nowhere dense sets are "small enough to be ignored".

The choice to define density via *closure* rather than via direct point-wise approximation is forced by the desire for a single condition that works in every topological space, not just metric ones. Closure is defined for every subset of every space; sequential approximation is meaningful only in first-countable spaces. So the closure formulation is the *generally correct* definition, and the sequential formulation is its (equivalent) form in first-countable settings.

---

# The Definition

Let $X$ be a topological space and $A \subseteq X$.

**Dense subset.** $A$ is **dense in $X$** if its closure equals $X$:
$$\overline{A} = X.$$
Equivalently, by the closure characterization, $A$ is dense in $X$ if and only if every nonempty open set in $X$ meets $A$:
$$U \in \tau_X,\ U \neq \emptyset \implies U \cap A \neq \emptyset.$$
In a first-countable space (in particular every metric space), this is also equivalent to: every point of $X$ is the limit of some sequence in $A$.

**Nowhere dense subset.** $A$ is **nowhere dense in $X$** if the interior of its closure is empty:
$$(\overline{A})^\circ = \emptyset.$$
Equivalently, every nonempty open set $U \subseteq X$ contains a nonempty open subset $V$ disjoint from $A$. A nowhere dense set is one such that no open set is contained in its closure.

**Separable space.** $X$ is **separable** if it has a *countable* dense subset.

A few elementary consequences of the definitions. If $A$ is dense and $A \subseteq B$, then $B$ is dense (closure of $B$ contains closure of $A$ equals $X$). The complement of an open dense set is closed nowhere dense, and vice versa. A finite union of nowhere dense sets is nowhere dense (the closure of a finite union is the union of the closures, and a finite union of closed sets with empty interior may have empty interior).

---

# Relate to Other Fields / Compression

In **measure theory**, the analogue of "dense" is "full measure" — a set $A$ with $\mu(X \setminus A) = 0$. Density and full-measure are *different* conditions, neither implying the other. The standard example separating them is the Cantor set $C \subseteq [0, 1]$: $C$ has Lebesgue measure zero (so $[0,1] \setminus C$ has full measure) but the irrationals are dense in $[0,1]$ and also have full measure, while a "fat Cantor set" can be both nowhere dense and have positive measure. The dictionary between *topological smallness* (nowhere dense, meager) and *measure-theoretic smallness* (null) is rich and surprising — see **Topology IV — Baire Category and Function Spaces** for the systematic theory.

In **algebraic geometry**, every nonempty Zariski-open subset of an irreducible variety is *automatically* dense — this is because the Zariski closed sets are the lower-dimensional subvarieties, and the complement of a proper subvariety in an irreducible variety is everything except a thin sliver. So density is a much weaker condition in the Zariski topology than in the standard topology. This is one reason Zariski opens are described as "huge".

In **functional analysis**, three of the most heavily used density theorems are: the polynomials are dense in $C[0,1]$ (Weierstrass / Stone–Weierstrass); the simple functions are dense in $L^p$ for $1 \leq p < \infty$; the smooth compactly supported functions $C^\infty_c$ are dense in $L^p(\mathbb{R}^n)$ for $1 \leq p < \infty$ and in many other Banach spaces of integrable / continuous functions. Each is a *density-as-strategy* enabler: hard analytic theorems are first proved for the nice dense subclass, then extended by continuity.

The unifying frame is that **density is the topological prerequisite for the approximation strategy**, and every analytic argument that uses approximation is using density in this sense. The strategy converts hard problems about general objects into tractable problems about nice ones, plus an approximation error to control.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Q}$ is dense in $\mathbb{R}$.** Every open interval $(a, b)$ contains a rational, so every nonempty open set in $\mathbb{R}$ meets $\mathbb{Q}$. Equivalently, $\overline{\mathbb{Q}} = \mathbb{R}$. The irrationals are also dense in $\mathbb{R}$ — both a set and its complement can be dense, which is the topological signature of the fact that "$\mathbb{Q}$ and $\mathbb{R} \setminus \mathbb{Q}$ are mixed together everywhere".

**Is an instance — polynomials dense in $C[0,1]$.** With the uniform metric $d(f,g) = \sup |f - g|$, the polynomials are dense in $C[0,1]$ — this is the **Weierstrass approximation theorem**. So every continuous function on $[0,1]$ is the uniform limit of polynomials, and density is what licenses the strategy "prove the theorem for polynomials and pass to the limit". The Stone–Weierstrass theorem generalizes this to arbitrary compact Hausdorff spaces with subalgebras separating points.

**Is an instance — $C^\infty_c$ dense in $L^p$.** The smooth compactly supported functions $C^\infty_c(\mathbb{R}^n)$ are dense in $L^p(\mathbb{R}^n)$ for $1 \leq p < \infty$, in the $L^p$ norm. So every $L^p$ function is the limit of a sequence of smooth compactly supported functions. The proof goes through the dense subclasses of simple functions then continuous compactly supported functions, each step a density argument. This is the engine of distribution theory: smooth test functions are dense, so a distribution is determined by its action on them.

**Is NOT an instance — $\{0\}$ in $\mathbb{R}$.** The singleton $\{0\}$ is closed, so $\overline{\{0\}} = \{0\} \neq \mathbb{R}$. Hence $\{0\}$ is not dense — it does not approximate every real, it is just a single point.

**Is NOT an instance — the Cantor set in $[0, 1]$.** The Cantor set $C \subseteq [0,1]$ is closed (it is the intersection of closed sets), so $\overline{C} = C \neq [0, 1]$. It is in fact **nowhere dense**: $C^\circ = \emptyset$ (no open interval is entirely contained in $C$, since $C$ misses any open interval that survives finitely many of the ternary deletion steps), and $\overline{C} = C$. The Cantor set is the prototype of a "nowhere dense but uncountable" set — small topologically (closed, nowhere dense) but large in cardinality (uncountable, in bijection with $\mathbb{R}$) and even in Hausdorff dimension ($\log 2 / \log 3 \approx 0.63$).

**Is NOT an instance — the integers in $\mathbb{R}$.** $\mathbb{Z}$ is closed in $\mathbb{R}$, so $\overline{\mathbb{Z}} = \mathbb{Z} \neq \mathbb{R}$, hence not dense. It is nowhere dense: $\mathbb{Z}^\circ = \emptyset$ (no open interval lies in $\mathbb{Z}$).

**Corollary — separability of $\mathbb{R}^n$.** $\mathbb{R}^n$ is separable: $\mathbb{Q}^n$ is countable and dense. Every separable metric space is in fact second countable (the balls $B_{1/m}(q)$ for $q$ in the dense set and $m \geq 1$ form a countable basis), so $\mathbb{R}^n$ is second countable, and the three properties coincide in metric spaces.

**Corollary — density preserved under continuous surjections.** If $f : X \to Y$ is continuous and surjective and $A \subseteq X$ is dense, then $f(A) \subseteq Y$ is dense. *Proof:* $\overline{f(A)} \supseteq f(\overline{A}) = f(X) = Y$ (using continuity gives the first inclusion and surjectivity gives the last). So density transfers along continuous surjections — useful for transferring dense subsets through quotient maps.

**Corollary — density-as-strategy.** Suppose $f, g : X \to Y$ are continuous functions between topological spaces, $Y$ is Hausdorff, and $f = g$ on a dense subset $A \subseteq X$. Then $f = g$ on all of $X$. *Proof:* the set $\{x : f(x) = g(x)\}$ is closed in $X$ (it is the preimage of the diagonal in $Y \times Y$, which is closed in Hausdorff $Y$), contains $A$, hence contains $\overline{A} = X$. So a continuous map is determined by its values on a dense subset. This is the foundational instance of density-as-strategy: agreement on a dense subset forces global agreement.

**Calibration check.** Verify that $\overline{\mathbb{Q}}$ in the discrete topology on $\mathbb{R}$ is $\mathbb{Q}$ itself (the discrete topology makes every set closed), hence $\mathbb{Q}$ is not dense in $(\mathbb{R}, \tau_{\text{discrete}})$; in the cofinite topology on $\mathbb{R}$, $\mathbb{Q}$ *is* dense (every cofinite open set meets $\mathbb{Q}$ since $\mathbb{Q}$ is infinite); in the Sorgenfrey topology, $\mathbb{Q}$ is still dense (every half-open interval $[a, b)$ contains a rational). The same set $\mathbb{Q}$ has different density behaviour depending on the ambient topology, and the answer reads off from the open sets in each case.

---

# Unlocked by This

> [!tip] The Baire Category Theorem *(from Topology IV)*
> A topological space is a **Baire space** if every countable intersection of open dense sets is dense. **Baire's theorem** says every complete metric space and every locally compact Hausdorff space is Baire. The contrapositive — a space is not the countable union of nowhere dense sets — is the standard form, and it is the topological foundation for the Banach–Steinhaus theorem, the open mapping theorem, and the closed graph theorem in functional analysis.

> [!tip] The Stone–Weierstrass Theorem *(from Functional Analysis)*
> Density of polynomials in $C[0,1]$ extends to arbitrary compact Hausdorff spaces: any subalgebra of $C(X)$ (real or complex) that contains the constants and separates points is dense — see the **Stone–Weierstrass theorem**. This is the structural generalization of Weierstrass's approximation theorem, and its proof relies on closure manipulations of subalgebras under the uniform norm.

> [!tip] Density and Distribution Theory *(from Functional Analysis / PDE)*
> The density of $C^\infty_c(\mathbb{R}^n)$ in $L^p(\mathbb{R}^n)$ (for $1 \leq p < \infty$) is what makes distributions well-defined. A distribution is a continuous linear functional on $C^\infty_c$, and density ensures it extends uniquely to a much wider class of functions — the dual space is *strictly larger* than $L^p$ for these $p$. The strategy of mollification — convolve a non-smooth function with a smooth bump — is the explicit approximation that realizes this density.
