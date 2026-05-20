---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Subspace Topology"
  - "Def - Neighbourhood and Neighbourhood Basis"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space and $A, B \subseteq X$ subsets. The **closure** of $A$ in $X$ is written $\overline{A}$ or $\operatorname{cl}(A)$; the **interior** is $A^\circ$ or $\operatorname{int}(A)$; the **boundary** (or **frontier**) is $\partial A$ or $\operatorname{bdry}(A)$. When the ambient space matters, we write $\overline{A}^X$ or $\operatorname{cl}_X(A)$. The complement of $A$ in $X$ is $X \setminus A$ or $A^c$. The full notation registry sits on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

We have a topological space $X$ and a subset $A$. The intuition we want to capture has three pieces. There are points *strictly inside* $A$ — surrounded by other points of $A$, with room to move without leaving. There are points *strictly outside* — surrounded by non-$A$ with room to move without entering. And there is a middle region of points *on the edge* — touching both $A$ and its complement. The three corresponding sets are called the **interior**, the **exterior**, and the **boundary**. The interior and the closure are the two primary objects, with the boundary derived from them.

A naive attempt to define these uses the metric: "$x$ is in the interior of $A$ if some ball around $x$ lies in $A$"; "$x$ is in the closure if every ball around $x$ meets $A$". This works in a metric space but is unavailable in a general topological space — there are no balls. The fix is to translate "ball" into "open set", and the conditions become: "$x$ is interior if some open set containing $x$ lies in $A$"; "$x$ is in the closure if every open set containing $x$ meets $A$". These conditions use only the topology and recover the metric definitions when one is present.

There is an equivalent, more global formulation that does not refer to points at all. The interior is the *largest open set contained in $A$* — equivalently, the union of all open subsets of $A$. The closure is the *smallest closed set containing $A$* — equivalently, the intersection of all closed supersets of $A$. The point-based and set-based descriptions are equivalent, but the set-based one is more powerful because it is a *universal property*: $A^\circ$ is universal among opens in $A$ (every other open in $A$ is contained in $A^\circ$), and $\overline{A}$ is universal among closeds containing $A$.

The universal property forces existence: arbitrary unions of opens are open (a topology axiom), so the union of all opens in $A$ is itself an open set contained in $A$, automatically the largest. Dually, arbitrary intersections of closeds are closed, so the intersection of all closeds containing $A$ is itself a closed set containing $A$, automatically the smallest. Both operations are well-defined for *every* subset of *every* topological space — there is no "exists" hypothesis to check. This contrasts with operations like "infimum" in a partial order, where existence requires a completeness condition.

The boundary $\partial A = \overline{A} \setminus A^\circ$ is then forced: it is the set of points in the closure but not in the interior, which is exactly the "on the edge" intuition. A point in $\partial A$ is approached arbitrarily closely by both $A$ and $X \setminus A$. The space decomposes into three disjoint pieces — interior, boundary, and exterior $X \setminus \overline{A}$ — with the closure being the union of the first two and the open exterior being the third.

Why are these the right notions? Because they are exactly what makes topological reasoning *robust*. Continuous functions preserve closure containment: $f(\overline{A}) \subseteq \overline{f(A)}$ (the image of the closure lies in the closure of the image). They preserve the closed-set definition of closure (preimage of a closed set is closed). The interior is what controls the existence of differentiable structure in open sets. The boundary is what supports integration-by-parts formulas in calculus. Each notion fits a place in the structural ecology of the subject, and that ecology is what motivates the definitions.

---

# The Definition

Let $X$ be a topological space and $A \subseteq X$.

**Closure.** The **closure** of $A$ in $X$ is
$$\overline{A} = \bigcap \{F \subseteq X : F \supseteq A,\ F \text{ closed in } X\}.$$
Equivalently, $\overline{A}$ is the smallest closed set containing $A$ (smallest under inclusion). $A$ is closed if and only if $A = \overline{A}$.

**Interior.** The **interior** of $A$ in $X$ is
$$A^\circ = \bigcup \{U \subseteq X : U \subseteq A,\ U \text{ open in } X\}.$$
Equivalently, $A^\circ$ is the largest open set contained in $A$. $A$ is open if and only if $A = A^\circ$.

**Boundary.** The **boundary** of $A$ in $X$ is
$$\partial A = \overline{A} \setminus A^\circ.$$
Equivalently, $\partial A = \overline{A} \cap \overline{X \setminus A}$.

**The decomposition.** Every topological space decomposes as a disjoint union with respect to any subset $A$:
$$X = A^\circ \,\sqcup\, \partial A \,\sqcup\, (X \setminus \overline{A}).$$
The three pieces are the **interior**, the **boundary**, and the **exterior** of $A$. The closure is the union of the first two, and the exterior is open (being the complement of the closure).

**Standard identities.** For any $A, B \subseteq X$:
- $A^\circ \subseteq A \subseteq \overline{A}$.
- $\overline{\overline{A}} = \overline{A}$ and $(A^\circ)^\circ = A^\circ$ (both operations are idempotent).
- $\overline{A \cup B} = \overline{A} \cup \overline{B}$ (closure distributes over finite unions).
- $\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$, with strict containment possible.
- $(A \cap B)^\circ = A^\circ \cap B^\circ$ (interior distributes over finite intersections).
- $(A \cup B)^\circ \supseteq A^\circ \cup B^\circ$, with strict containment possible.
- $X \setminus \overline{A} = (X \setminus A)^\circ$ and $X \setminus A^\circ = \overline{X \setminus A}$ (de Morgan duality between closure and interior).

---

# Relate to Other Fields / Compression

Closure and interior are an instance of a **Galois connection** between the lattice of subsets of $X$ and the lattices of closed (resp. open) subsets. The closure operator $\overline{\cdot}$ is a **Kuratowski closure operator** — characterized abstractly by the four Kuratowski axioms: $\overline{\emptyset} = \emptyset$, $A \subseteq \overline{A}$, $\overline{\overline{A}} = \overline{A}$, and $\overline{A \cup B} = \overline{A} \cup \overline{B}$. A topological space can equivalently be defined as a set $X$ together with any operator $\overline{\cdot} : \mathcal{P}(X) \to \mathcal{P}(X)$ satisfying these axioms, with closed sets being the fixed points. This is **Kuratowski's axiomatization**, an alternative starting point for topology that takes closure as primitive rather than open sets.

In **algebraic geometry**, the Zariski closure of a set is the smallest algebraic subvariety containing it — same closure operator, different ambient lattice (the lattice of Zariski closeds is much smaller than the lattice of analytic closeds, because polynomial relations are much stronger constraints than continuous ones). The interior in the Zariski topology is wild: most "natural" sets have empty Zariski interior because Zariski opens are dense.

In **lattice theory and order theory**, the closure of $A$ in a partially ordered set with respect to a closure operator is the same construction — and operators like *taking the linear span* in a vector space, *the convex hull* in $\mathbb{R}^n$, *the generated subgroup* in a group all fit the same pattern. The topological closure is the instance specialized to: ambient lattice = $\mathcal{P}(X)$, closed sets = the topology's closed sets, generator = the subset $A$. The unified perspective is that all of these are universal-property constructions: the smallest object of the desired type containing the input.

---

# Examples / Corollaries

**Standard examples in $\mathbb{R}$.** The closure of $(0, 1)$ in $\mathbb{R}$ is $[0, 1]$; its interior is $(0, 1)$ itself (already open); its boundary is $\{0, 1\}$. The closure of $[0, 1]$ is itself; its interior is $(0, 1)$; its boundary is $\{0, 1\}$. The closure of $\{0\}$ is itself (singletons are closed in $\mathbb{R}$); its interior is empty; its boundary is $\{0\}$. The closure of $(-\infty, 0) \cup (0, \infty) = \mathbb{R} \setminus \{0\}$ is $\mathbb{R}$ (the missing point is a boundary point); its interior is itself.

**The rationals — closure, interior, boundary all surprising.** Take $A = \mathbb{Q} \subseteq \mathbb{R}$. The closure $\overline{\mathbb{Q}}$ is *all of $\mathbb{R}$*, because every real is a limit of rationals, equivalently every open interval meets $\mathbb{Q}$. The interior $\mathbb{Q}^\circ$ is *empty*, because no open interval lies entirely in $\mathbb{Q}$ (irrationals are dense too). The boundary $\partial \mathbb{Q}$ is $\overline{\mathbb{Q}} \setminus \mathbb{Q}^\circ = \mathbb{R} \setminus \emptyset = \mathbb{R}$ — every real is on the boundary of $\mathbb{Q}$. This is the prototype of a set with maximum closure, minimum interior, and "everywhere" boundary; it is what it means for $\mathbb{Q}$ to be **dense** in $\mathbb{R}$ (closure = whole space) and **nowhere dense** is the dual condition (closure has empty interior, which fails for $\mathbb{Q}$).

**An example where $\overline{A \cap B} \neq \overline{A} \cap \overline{B}$.** Let $A = \mathbb{Q}$ and $B = \mathbb{R} \setminus \mathbb{Q}$ (the irrationals) in $\mathbb{R}$. Then $A \cap B = \emptyset$, so $\overline{A \cap B} = \emptyset$. But $\overline{A} = \mathbb{R}$ and $\overline{B} = \mathbb{R}$ (the irrationals are also dense), so $\overline{A} \cap \overline{B} = \mathbb{R}$. The two sides differ as much as possible. The containment $\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$ holds; equality is special.

**An example where $(A \cup B)^\circ \neq A^\circ \cup B^\circ$.** Same example: $\mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q}) = \mathbb{R}$, so $(A \cup B)^\circ = \mathbb{R}^\circ = \mathbb{R}$. But $\mathbb{Q}^\circ = \emptyset$ and $(\mathbb{R} \setminus \mathbb{Q})^\circ = \emptyset$, so $A^\circ \cup B^\circ = \emptyset$. Two sets with empty interior can have nonempty interior in their union.

**Is NOT an instance — $\overline{A^\circ} = A$.** It is tempting to think the closure of the interior of $A$ recovers $A$. But $A = \mathbb{Q}$ gives $A^\circ = \emptyset$, $\overline{A^\circ} = \emptyset \neq \mathbb{Q}$. The interior of the closure also need not equal $A$: take $A = (0, 1) \cup \{2\}$, then $\overline{A} = [0, 1] \cup \{2\}$, $(\overline{A})^\circ = (0, 1) \neq A$. The point of these counterexamples is that closure and interior, while dual under complementation, are *not* mutual inverses.

**Corollary — closure characterized by points.** $x \in \overline{A}$ if and only if every open set $U$ containing $x$ meets $A$ (i.e., $U \cap A \neq \emptyset$). *Sketch:* If every open set containing $x$ meets $A$, then no closed set $F \supseteq A$ excludes $x$ (else $X \setminus F$ would be an open set containing $x$ missing $A$), so $x$ is in every closed superset, hence in their intersection $\overline{A}$. Conversely, if some open $U \ni x$ misses $A$, then $X \setminus U$ is closed, contains $A$, and excludes $x$, so $x \notin \overline{A}$. This characterization is what makes closure operational — see [[Thm - Characterizations of the Closure]] for the full list of equivalences.

**Corollary — continuity preserves closure containment.** If $f : X \to Y$ is continuous and $A \subseteq X$, then $f(\overline{A}) \subseteq \overline{f(A)}$. *Sketch:* $f(A) \subseteq \overline{f(A)}$, so $A \subseteq f^{-1}(\overline{f(A)})$. The set on the right is closed (preimage of closed), so it contains $\overline{A}$. Applying $f$, $f(\overline{A}) \subseteq \overline{f(A)}$. Strict containment can occur — $f$ need not map closures to closures, only into closures.

**Calibration check.** Compute the closure, interior, and boundary of the Cantor set $C \subseteq [0, 1]$: $\overline{C} = C$ (closed), $C^\circ = \emptyset$ (nowhere dense), $\partial C = C$. Compute these for the rationals $\mathbb{Q} \cap [0, 1] \subseteq \mathbb{R}$: closure $[0, 1]$, interior $\emptyset$, boundary $[0, 1]$. Verify by direct computation that, in the discrete topology on any set, every subset has $A^\circ = A = \overline{A}$ and $\partial A = \emptyset$ — every set is its own closure and interior, because every set is both open and closed. In the indiscrete topology, by contrast, $A^\circ = \emptyset$ if $A \neq X$, $\overline{A} = X$ if $A \neq \emptyset$.

---

# Unlocked by This

> [!tip] Dense Subsets and Approximation *(in this topic)*
> A set $A \subseteq X$ is **dense** if $\overline{A} = X$ — the closure operation is the language in which density is defined. See [[Def - Dense Subset]]. Density underwrites every "prove on a dense subclass, pass to the limit" argument in analysis, and the closure-as-limit characterization is what licenses the passage.

> [!tip] Connected Sets and Closures *(from Topology II)*
> A subset $A$ is **connected** if it cannot be written as the disjoint union of two nonempty relatively open sets. The closure $\overline{A}$ of a connected set is connected — closure preserves connectivity. This is one of the few set operations that does preserve connectivity (interior does not: $\mathbb{Q}^\circ = \emptyset$ is "connected by emptiness" but $\overline{\mathbb{Q}^\circ}= \emptyset$ behaves vacuously).

> [!tip] Baire's Theorem and Nowhere Dense Sets *(from Topology IV)*
> A set is **nowhere dense** if $(\overline{A})^\circ = \emptyset$ — its closure has empty interior. **Baire's theorem** says that in a complete metric space (or locally compact Hausdorff space), a countable union of nowhere dense sets has empty interior — equivalently, the space is not the countable union of nowhere dense sets. This is the topological foundation of generic-property arguments in analysis (open dense sets contain a residual subset of "most" points).
