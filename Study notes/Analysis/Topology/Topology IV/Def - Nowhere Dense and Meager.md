---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Closure, Interior, and Boundary"
  - "Def - Cauchy Sequence and Complete Metric Space"
tags: [analysis, topology, baire]
---

# Notation

$X$ a topological space, $A \subseteq X$ a subset. $\overline{A}$ the closure of $A$, $\operatorname{int}(A)$ the interior. "First category" and "meager" are synonyms; "second category" means not first category. A "residual" set is one whose complement is meager (sometimes also called **comeager** or **generic**). The full registry is on the topic page.

---

# Axiom Motivation

The notion is built to formalize "smallness" for a topological space — a notion of size that is purely topological, requiring no measure. The motivating examples: $\mathbb{Q} \subseteq \mathbb{R}$ is small (countable, dense but "thin"); a countable discrete set is small; a Cantor set has measure zero but is *not* topologically small (it has empty interior but is *closed*, so its closure has empty interior, making it "borderline"). We want a hierarchy of smallness that captures this.

**Nowhere dense** is the basic notion of topological smallness. A set $A$ is nowhere dense if its closure $\overline{A}$ has empty interior — i.e., $\overline{A}$ contains no nonempty open set. Equivalently: every nonempty open set in $X$ contains a smaller nonempty open subset disjoint from $A$. The set is "thin everywhere" — wherever you look, you can find an open set with no $A$-points. Examples: a finite or convergent sequence in $\mathbb{R}$; the Cantor set in $[0, 1]$; the $x$-axis in $\mathbb{R}^2$. Non-examples: $\mathbb{Q} \subseteq \mathbb{R}$ (not nowhere dense; its closure is $\mathbb{R}$, which has nonempty interior).

Why "the closure has empty interior" and not just "the set itself has empty interior"? Because the set itself might have empty interior while its closure does not — e.g., $\mathbb{Q} \subseteq \mathbb{R}$ has empty interior (any open set contains irrationals) but $\overline{\mathbb{Q}} = \mathbb{R}$ which has all of $\mathbb{R}$ as interior. The closure condition correctly distinguishes the dense (and thus not "thin everywhere") $\mathbb{Q}$ from the genuinely thin Cantor set.

**Meager** (or "first category") generalizes from a single nowhere dense set to a *countable union* of them. The intuition: a meager set is one that can be covered by countably many "very thin" sets, hence is itself "thin". The countability is essential — an uncountable union of nowhere dense sets can cover the whole space (e.g., $\mathbb{R} = \bigcup_{x \in \mathbb{R}} \{x\}$ is an uncountable union of singletons, each nowhere dense). The Baire category theorem says that in a complete metric space (or LCH space), the whole space is not meager — *countably many* nowhere dense sets cannot exhaust it.

If we *weaken* "nowhere dense" by dropping the closure (just "empty interior"), the notion becomes too weak to support the Baire conclusion. If we *strengthen* by requiring "finite" union instead of countable, we lose the most important applications: the rationals are a *countable* union of singletons, and the meaningful statement is that they cannot equal $\mathbb{R}$.

**Second category** is the negation of first category: a set is second category in itself if it is not meager. The Baire category theorem produces second-category sets: $\mathbb{R}$ is second category in itself, every Banach space is, every locally compact Hausdorff space is. These are the spaces where "the generic element exists" — where the intersection of countably many dense opens is nonempty.

**Residual** (or **comeager**, or **generic**): the complement of a meager set. In Baire's setting, residual sets are dense; they are the "large" sets in the topological sense. The "generic continuous function is nowhere differentiable" statement asserts that the nowhere-differentiable functions form a residual set in $C[0, 1]$ — see [[Ex - A continuous nowhere differentiable function exists]].

The intuitive picture: nowhere dense = topologically null on a single set; meager = topologically null up to countable union; second category = topologically not-null; residual = topologically "almost everywhere", in the categorical sense. The analogy with measure theory is: nowhere dense ~ measure-zero closed set; meager ~ measure-zero set ($\sigma$-ideal); residual ~ full-measure set. The Baire category theorem is then the topological analogue of "the whole space has positive measure".

---

# The Definition

Let $X$ be a topological space.

**Nowhere dense.** A subset $A \subseteq X$ is **nowhere dense** in $X$ if its closure has empty interior:
$$\operatorname{int}(\overline{A}) = \emptyset.$$
Equivalently: $X \setminus \overline{A}$ is dense in $X$; or, every nonempty open subset of $X$ contains a nonempty open subset disjoint from $A$.

**First category (meager).** A subset $S \subseteq X$ is **of first category** (synonymously **meager**) in $X$ if $S$ is a countable union of nowhere dense subsets:
$$S = \bigcup_{n=1}^{\infty} A_n \quad \text{with each } A_n \text{ nowhere dense in } X.$$

**Second category.** A subset is **of second category** in $X$ if it is not of first category.

**Residual.** A subset $R \subseteq X$ is **residual** (or **comeager**) if its complement $X \setminus R$ is meager. Equivalently, $R$ contains a countable intersection of dense open sets.

---

# Relate to Other Fields / Compression

The meager/residual dichotomy is the topological analogue of the measure-zero/full-measure dichotomy. Both define a $\sigma$-ideal of "small" sets and a complementary class of "large" sets, but they are *independent*: a set can be meager and have full measure (e.g., the residual set of irrationals containing every "good" point can be Lebesgue null), and conversely a set can be measure-zero but residual. The two notions capture different aspects of "smallness".

In **descriptive set theory**, meagerness is a $\sigma$-ideal (closed under countable union and subset), and the **Banach-Mazur game** is a way of detecting meager sets via game theory. Meager sets correspond to "small" sets in the Polish-space sense.

In **functional analysis**, the meager/residual distinction is the topological foundation of "genericity" arguments: the generic continuous function is nowhere differentiable, the generic bounded operator has nontrivial spectrum, etc. The Baire category theorem is what makes these statements honest.

---

# Examples and Corollaries

**Is an instance of nowhere dense — the Cantor set $C \subseteq [0, 1]$.** $C$ is closed (intersection of closed sets), and its interior is empty: any open interval in $[0, 1]$ intersects the "removed thirds" at some stage. So $\overline{C} = C$ has empty interior, hence $C$ is nowhere dense.

**Is an instance of nowhere dense — a single point in a $T_1$ space without isolated points.** $\{x\} \subseteq \mathbb{R}^n$ is closed and has empty interior. Nowhere dense.

**Is an instance of nowhere dense — a lower-dimensional submanifold.** A $k$-dimensional smooth submanifold of $\mathbb{R}^n$ for $k < n$ is closed (if proper) and has empty interior in $\mathbb{R}^n$. Nowhere dense.

**Is an instance of meager — the rationals $\mathbb{Q} \subseteq \mathbb{R}$.** $\mathbb{Q} = \bigcup_q \{q\}$, a countable union of singletons, each nowhere dense. So $\mathbb{Q}$ is meager. See [[Ex - The rationals are first category in R]].

**Is an instance of meager — the union of all $k$-dimensional rational lines in $\mathbb{R}^n$ for $k < n$.** Each line is nowhere dense (it has Lebesgue measure zero and is closed); there are countably many. So the union is meager.

**Is an instance of residual — the irrationals in $\mathbb{R}$.** $\mathbb{R} \setminus \mathbb{Q}$ is the complement of a meager set, hence residual.

**Is NOT an instance of nowhere dense — $\mathbb{Q} \subseteq \mathbb{R}$.** $\mathbb{Q}$ is dense, so $\overline{\mathbb{Q}} = \mathbb{R}$, which has nonempty interior. So $\mathbb{Q}$ is *not* nowhere dense — even though it is meager (a countable union of nowhere dense singletons). This is a key distinction: a dense set can be meager.

**Is NOT an instance of meager — a complete metric space in itself.** The Baire category theorem says a complete metric space (or LCH space) is *not* meager in itself. So $\mathbb{R}$ is second category in itself; every Banach space is; every CH locally compact space is.

**Is NOT an instance of meager — a non-empty open set in a Baire space.** Open subsets of Baire spaces are also Baire — second category in themselves.

**Corollary — countable unions of meager sets are meager.** $\sigma$-additivity of the meager ideal: $\bigcup_n S_n$ where each $S_n = \bigcup_k A_{n, k}$ with $A_{n,k}$ nowhere dense gives $\bigcup_{n, k} A_{n, k}$, a countable union of nowhere dense sets.

**Corollary — subsets of meager sets are meager.** Subsets inherit the "smallness": if $S \subseteq T$ and $T$ is meager, the same nowhere dense covering of $T$ covers $S$.

**Corollary — Baire category theorem reformulation.** A space $X$ satisfies Baire if and only if every nonempty open subset is non-meager. Equivalently, the intersection of countably many dense open sets is dense.

**Calibration check.** Verify: the set of polynomial functions in $C[0, 1]$ is dense (Stone-Weierstrass) but is it meager? Yes — each "polynomial of degree at most $n$" forms a finite-dimensional subspace, which is closed and has empty interior in $C[0, 1]$; the polynomials are the countable union of these. Verify: the union of all rational affine lines in $\mathbb{R}^2$ is meager but dense. Verify: $\mathbb{Q}$ is meager and dense in $\mathbb{R}$ (so meager does not preclude dense).

---

# Unlocked by This

> [!tip] Baire Category Theorem *(from this topic)*
> The **Baire category theorem** asserts that a complete metric space (or LCH space) is second category in itself. Equivalently, a countable intersection of dense open sets is dense. This is the existence theorem for "generic" points and the foundation of Banach-Steinhaus, open mapping, and closed graph theorems.

> [!tip] Generic Property *(from Dynamical Systems / Descriptive Set Theory)*
> A property "holds generically" if the set of points satisfying it is residual. The standard examples: a generic continuous function is nowhere differentiable; a generic homeomorphism of a compact manifold is topologically transitive (Birkhoff); a generic $L^1$ function on $[0, 1]$ has bad pointwise behavior.

> [!tip] Topological Genericity vs Measure-Theoretic Genericity
> Meager sets can have full Lebesgue measure (e.g., a residual set of Liouville numbers is null), and conversely measure-zero sets can be residual. The two notions of "generic" are *independent*. Choosing which to use depends on the application: topological for stability properties, measure-theoretic for probabilistic arguments.
