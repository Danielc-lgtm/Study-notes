---
type: definition
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ denotes a set and $\tau$ a candidate collection of subsets of $X$ — the prospective open sets. We write $\mathcal{P}(X)$ for the power set of $X$, so $\tau \subseteq \mathcal{P}(X)$. The pair $(X, \tau)$ is a **topological space**. We will reserve $U, V$ for open sets and $F, C$ for closed sets; $\{U_\alpha\}_{\alpha \in I}$ denotes an indexed family of open sets, where $I$ is an arbitrary (possibly uncountable) index set. We say "$\tau$ is *finer* than $\tau'$" if $\tau \supseteq \tau'$ (more sets are open) and "$\tau$ is *coarser* than $\tau'$" if $\tau \subseteq \tau'$ (fewer sets are open). For the full registry of symbols see [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

The story so far: a metric on a set $X$ gives a notion of open set, which gives a notion of continuity. The next move is to ask whether we *need* the metric. The answer turns out to be no — the continuity definition uses the open sets but not the actual distances. So we should be able to state the same theory using only the open-set collection, and the rest of the structure of "metric" should be revealed as not load-bearing.

But which collections of subsets *are* allowed to play the role of "open sets"? Not every collection works: if we declared, say, that the open sets of $\mathbb{R}$ are $\{\emptyset, [0,1], [0,2], \mathbb{R}\}$, we would have trouble defining continuity, because the natural manipulations of the $\varepsilon$–$\delta$ proofs — taking unions and intersections of open sets — would not preserve membership in our class. So we must axiomatize *which* features of the collection of metric-open-sets are essential.

Look at what we proved about the metric open sets in [[Def - Open and Closed Sets in a Metric Space]]. The four properties:

(i) The empty set and the whole space are open. *Reason*: empty set vacuously, whole space because every ball lies in it; both are edge cases needed for closure under intersection/union when the index family is empty.

(ii) The union of any family of open sets is open. *Reason*: a point in the union lies in some particular open set $U_\alpha$, which contains a ball about that point, and that ball lies in the union.

(iii) The intersection of *finitely many* open sets is open. *Reason*: each gives wiggle room of some size; the minimum of finitely many positive sizes is positive; the minimum-radius ball lies in all of them.

(iv) Open balls are open. *Reason*: triangle inequality.

Property (iv) is metric-specific — it mentions balls, which only exist if we have a metric. The other three are *agnostic* to where the open sets came from. Could we throw away the metric and keep just (i), (ii), (iii) as axioms? Yes — and that is the abstraction.

There is one subtle point. Property (iii) restricts to *finite* intersections, not arbitrary ones. We saw in [[Def - Open and Closed Sets in a Metric Space]] that arbitrary intersections fail to be open in general: $\bigcap_n (-1/n, 1/n) = \{0\}$ is not open in $\mathbb{R}$. So the axiom must respect this. Why are arbitrary unions fine but arbitrary intersections not? Because *unions preserve wiggle room*: if a point has wiggle room in one of the sets being unioned, it has wiggle room in the union. *Intersections compress wiggle room*: each set in the intersection imposes its own size constraint, and the constraints can shrink without bound as the family grows. The minimum of $\{1/n\}_n$ is $0$. So we must restrict intersections to be finite.

If we *demand* arbitrary intersections of opens be open, the resulting structure is too rigid for analysis. Specifically, for *every* point $x$ in a "topological" space with this rule, the singleton $\{x\}$ would be open — because it is the intersection of all open sets containing $x$. So the topology would be the discrete topology, and continuity would mean: every function on the space is continuous. That is correct on a discrete space, but it would force *every* space to be discrete, eliminating any interesting analysis. The "finite intersections" restriction is exactly what makes topology a non-trivial subject.

Now ask why these axioms — closed under arbitrary unions and finite intersections — and not, say, the dual: closed under arbitrary intersections and finite unions? Because that is the axiomatization of *closed* sets, and we choose to take open sets as primary. The choice is *largely* conventional; one could equivalently develop topology in terms of closed sets, where the axioms would be: $\emptyset, X$ closed; arbitrary intersections of closeds are closed; finite unions of closeds are closed. The two are duals via complementation, and one passes between them as convenient. Open sets are the standard choice because the $\varepsilon$–$\delta$ definition of continuity uses balls, which are open in a metric space.

What about more exotic axiom systems? In **algebraic geometry**, a *Grothendieck topology* on a category replaces the open-set collection with a notion of *covering* — a family of morphisms $\{U_i \to X\}$ that "covers" $X$ in a certain axiomatic sense. The reason for this generalization is that on a scheme, the Zariski-open sets are sometimes too coarse, and one needs étale or fppf coverings instead. The axioms are different — there is no notion of "open set" in the usual sense — but the spirit is the same: minimal data needed for *sheaf theory*, which is the algebraic-geometric analogue of "continuity of sections". Our topology axioms are the right ones for analysis; Grothendieck topologies are the right ones for algebraic geometry. The two diverge because the natural notion of "local" is different in each subject.

The empty-set and whole-space axiom is sometimes derivable from the other two: if $\tau$ is closed under arbitrary unions, the union of the empty family is $\emptyset$ (so $\emptyset \in \tau$); if $\tau$ is closed under finite intersections, the intersection of the empty family is $X$ (so $X \in \tau$). Strictly, this is a vacuous convention — many texts simply list it as a separate axiom for explicitness. We will follow that convention.

Finally, observe that the three axioms have a deeply *minimal* flavour. They are exactly what we need for the four following statements to make sense and hold:
- Preimage of an open set under a continuous map is open (definition).
- Composition of continuous maps is continuous (uses: preimage commutes with composition).
- Finite intersections of opens can be checked by checking each component (uses: closure under finite intersection).
- Arbitrary unions can be assembled point by point from local data (uses: closure under arbitrary union).

Every one of these statements is the topological version of a tool in $\varepsilon$–$\delta$ analysis. The axioms are the minimal data needed for the tools to work; anything weaker would break the tools, and anything stronger would exclude examples (like the cofinite topology, or the Zariski topology) that have a perfectly reasonable notion of continuity.

---

# The Definition

Let $X$ be a set. A **topology** on $X$ is a collection $\tau \subseteq \mathcal{P}(X)$ of subsets of $X$ such that:

1. **(Edge cases.)** $\emptyset \in \tau$ and $X \in \tau$.

2. **(Closure under arbitrary unions.)** If $\{U_\alpha\}_{\alpha \in I}$ is any family of elements of $\tau$ (with $I$ any index set), then
   $$\bigcup_{\alpha \in I} U_\alpha \in \tau.$$

3. **(Closure under finite intersections.)** If $U_1, \dots, U_n \in \tau$ (with $n$ a positive integer), then
   $$U_1 \cap U_2 \cap \dots \cap U_n \in \tau.$$

The pair $(X, \tau)$ is a **topological space**. Elements of $\tau$ are **open sets**; their complements are **closed sets**. When the topology is understood from context we refer to $X$ alone as the topological space.

**Comparison of topologies.** Given two topologies $\tau, \tau'$ on the same set $X$, $\tau$ is **finer** (or *stronger*, or *larger*) than $\tau'$ if $\tau \supseteq \tau'$. Equivalently, $\tau'$ is **coarser** (or *weaker*, or *smaller*) than $\tau$. The finest topology on $X$ is the **discrete topology** $\tau = \mathcal{P}(X)$, where every subset is open. The coarsest is the **indiscrete topology** $\tau = \{\emptyset, X\}$.

---

# Relate to Other Fields / Compression

The three axioms are *precisely* the right amount of structure for continuity to make sense. They are weaker than the σ-algebra axioms of measure theory (which require countable unions and complementation, not arbitrary unions and finite intersections), so a topology gives *less* information than a σ-algebra in some respects; but a topology has the asymmetric advantage that *finite* intersections (not just countable) and *arbitrary* unions (not just countable) are allowed. The asymmetry is what makes topology the right framework for analysis: arbitrary unions assemble local data into global, and finite intersections preserve "neighbourhood" structure without collapsing to a point.

In **category-theoretic language**, a topology on $X$ is the data of a *frame* (or *locale*) — a complete lattice in which arbitrary joins distribute over finite meets. This compresses the three axioms into a single algebraic structure. The dual notion — looking at the lattice of open sets *abstractly*, forgetting the points of $X$ — leads to *pointless topology* and the theory of *locales*, which is the foundation of constructive analysis and of topos theory.

In **algebraic geometry**, the **Zariski topology** on $\mathbb{R}^n$ (or $\mathbb{C}^n$, or an algebraic variety) declares the closed sets to be the zero sets of polynomials. There are very few open sets — vastly fewer than in the Euclidean topology — and the resulting topological space has very different properties (every nonempty open set is dense; the topology is non-Hausdorff). Yet the same three axioms hold, and the same notion of continuity applies. This shows the axioms are agnostic to which kind of "smallness" they encode.

In **functional analysis**, a single vector space often carries many topologies of interest: the norm topology, the weak topology, the weak-$*$ topology, the strong operator topology, the ultraweak topology, etc. Each is a topology in the sense of these three axioms, but they differ in which sets are open, and hence in which sequences converge, which functions are continuous, which sets are compact. The choice of topology is a strategic decision based on what one wants to prove.

The **Grothendieck topology** of algebraic geometry replaces the open-set collection with a notion of *covering family* — a sieve of morphisms into $X$ that satisfies axioms about pullback and composition. It is the right framework for *sheaves* on schemes, where the Zariski topology is sometimes too coarse for the cohomology one wants to compute. The Grothendieck topology axioms are *not* the topology axioms above; they are a genuine generalization, suited to algebraic geometry rather than analysis.

---

# Examples / Corollaries

**Is an instance — the metric topology.** Every metric space $(X, d)$ gives a topological space $(X, \tau_d)$, where $\tau_d$ consists of the metric-open sets. The three axioms are verified in [[Def - Open and Closed Sets in a Metric Space]]. So topological spaces *generalize* metric spaces: every metric space is a topological space, but not conversely (the topology may not be metrizable).

**Is an instance — the discrete topology.** $\tau = \mathcal{P}(X)$: every subset is open. The three axioms trivially hold. This is the finest topology on $X$. In this topology every function $X \to Y$ (for any $Y$) is continuous, because $f^{-1}(U) \subseteq X$ is automatically open. The discrete topology arises from the discrete metric.

**Is an instance — the indiscrete (trivial) topology.** $\tau = \{\emptyset, X\}$: only the empty set and the whole space are open. This is the coarsest topology on $X$. Continuous functions out of $X$ are exactly the constant functions (if $X$ has at least two points). The indiscrete topology is *not* metrizable on a space with more than one point: any metric distinguishes points, and the open ball of half-the-distance separates them, contradicting indiscreteness.

**Is an instance — the cofinite topology.** Take any infinite set $X$ and declare a set open if it is empty or has finite complement. Equivalently, the closed sets are the empty set together with the finite subsets. Check the axioms: $\emptyset$ and $X$ are open ($X$ has complement $\emptyset$, finite); a union of cofinite sets has complement an intersection of finite sets, hence finite; an intersection of finitely many cofinite sets has complement a finite union of finite sets, hence finite. So this is a topology. On a finite set the cofinite topology equals the discrete topology (every set is finite, so every set is cofinite). On an infinite set the cofinite topology is genuinely strange: every nonempty open set is dense, no two distinct points can be separated by disjoint open sets (the topology is *not Hausdorff*), and every continuous function from $X$ to a Hausdorff space (like $\mathbb{R}$ with the standard topology) is constant.

**Is an instance — the Zariski topology on $\mathbb{R}$.** Declare the closed sets to be the finite subsets of $\mathbb{R}$ together with $\mathbb{R}$ itself; open sets are the empty set and the cofinite sets. (On $\mathbb{R}$ this is the same as the cofinite topology, but on $\mathbb{R}^n$ for $n \geq 2$ the Zariski topology is genuinely richer: closed sets are zero sets of polynomials, e.g. the unit circle $\{(x, y) : x^2 + y^2 = 1\}$ is closed.) The Zariski topology is the basic topology of *algebraic geometry*; it is far coarser than the Euclidean topology but captures the algebraic structure of varieties.

**Is an instance — the order topology.** On a totally ordered set $X$ (say $\mathbb{R}$ with its usual order, or an ordinal number), the *order topology* is generated by the open intervals $(a, b) = \{x : a < x < b\}$. On $\mathbb{R}$ this gives the standard topology. On the first uncountable ordinal $\omega_1$ it gives a topology that is first-countable but not second-countable and not metrizable.

**Is an instance — the Sorgenfrey line.** Take $\mathbb{R}$ with the topology whose basis is the collection of half-open intervals $\{[a, b) : a < b\}$. Each $[a, b)$ is open in this topology; a finite intersection of such intervals is again of this form; arbitrary unions give all open sets. The Sorgenfrey line is *finer* than the standard $\mathbb{R}$ (every standard open interval $(a, b)$ is the union of $[a + 1/n, b)$ for $n$ large, so it is Sorgenfrey-open), but it is *not* metrizable (it is not second countable). Every $[a, b)$ is both open *and* closed (its complement $(-\infty, a) \cup [b, \infty)$ is open: $(-\infty, a) = \bigcup_n [a - n, a)$ and $[b, \infty) = \bigcup_n [b, b + n)$). So the Sorgenfrey line is totally disconnected.

**Is NOT an instance — closed under arbitrary intersections.** If we required arbitrary intersections of opens to be open, then for every point $x$, the set $\{x\} = \bigcap \{U : x \in U \text{ open}\}$ would be open. Then every singleton is open, every set is a union of singletons, every set is open — we are forced into the discrete topology. So the axiom "arbitrary intersections" is incompatible with non-discrete topologies; this is why we restrict to *finite* intersections.

**Is NOT an instance — closed under just unions, dropping the empty/full edge case.** If $\tau$ were closed only under arbitrary unions (no $\emptyset, X$ required, no finite intersections), the system would be too weak: the empty union $\bigcup \emptyset = \emptyset$ would be open *by the empty-union convention*, but the whole space $X$ would not be forced into $\tau$, and we could not check continuity at the universal level.

**Corollary — the closed sets satisfy dual axioms.** By De Morgan, the collection of closed sets is closed under arbitrary intersections, finite unions, and contains $\emptyset, X$. So one can equivalently define a topology by specifying which sets are closed.

**Corollary — every topology on a finite set is metrizable if and only if it is the discrete topology.** A finite Hausdorff space (which a metric space must be) has every singleton closed; the intersection of all open sets containing $x$ is $\{x\}$, which is finite hence open by finite intersection. So the topology is discrete. The cofinite, Zariski, and indiscrete topologies on finite sets all coincide with the discrete topology.

**Calibration check.** Verify that the topology on $\mathbb{R}^2$ generated by the open balls is the same as the topology generated by the open boxes $(a, b) \times (c, d)$ — i.e. the metric topology equals the product topology. Verify that the cofinite topology on an infinite set is not Hausdorff: any two nonempty open sets must meet (their complements being finite, the intersection is cofinite, hence nonempty). Verify that the indiscrete topology on a two-point space $\{0, 1\}$ has the property that the function $f(0) = 0, f(1) = 1$ from $\{0, 1\}_\text{discrete}$ to $\{0, 1\}_\text{indiscrete}$ is continuous, but its inverse (from indiscrete to discrete) is not — so the identity on $\{0, 1\}$ is *not* a homeomorphism between these two topologies. If you can also explain why arbitrary intersections would force the discrete topology, you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] **Continuity in the Abstract** *(from this topic)*
> Once we have topological spaces, we can define $f : X \to Y$ continuous by: $f^{-1}(U) \in \tau_X$ for every $U \in \tau_Y$. No metric needed. See [[Def - Continuous Map]].

> [!tip] **Homeomorphism** *(from this topic)*
> The notion of "two topological spaces are the same": a continuous bijection with continuous inverse. See [[Def - Homeomorphism]]. The classification of topological spaces up to homeomorphism is one of the central problems of topology.

> [!tip] **Basis and Subbasis** *(from this topic)*
> A topology can be efficiently specified by a small generating family of subsets — a **basis** (whose elements are open) or a **subbasis** (whose finite intersections are a basis). See [[Def - Basis and Subbasis for a Topology]]. The metric ball basis is the prototype.

> [!tip] **Subspace, Product, and Quotient Topologies** *(from this topic)*
> Standard constructions of new topological spaces from old ones — restriction to a subset, Cartesian product, quotient by an equivalence relation — each carry a natural topology, characterized by a universal property. The topology axioms are stable under all of these constructions.

> [!tip] **Borel σ-Algebra** *(from Measure Theory)*
> The smallest σ-algebra containing the open sets of a topological space is the **Borel σ-algebra** $\mathcal{B}(X)$. This is how a topology induces a measurable structure, and it is the standard σ-algebra on $\mathbb{R}^n$, on metric spaces, and on every topological space arising in probability theory.

> [!tip] **Sheaves and Cohomology** *(from Algebraic Geometry / Differential Geometry)*
> A **sheaf** on a topological space $X$ is an assignment of an algebraic structure (group, ring, module) to every open set, with restriction maps for inclusions and a gluing axiom. Sheaf cohomology is the universal tool for measuring how local-to-global lifting fails. The topology axioms are exactly what is needed for sheaf theory: arbitrary unions for gluing, finite intersections for restriction.
