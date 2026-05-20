---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Subspace Topology"
  - "Def - Closure, Interior, and Boundary"
  - "Thm - Characterizations of the Closure"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space, $Y \subseteq X$ a subspace (carrying the subspace topology $\tau_Y$ — see [[Def - Subspace Topology]]), and $A \subseteq Y \subseteq X$. The closure of $A$ taken in $Y$ is $\overline{A}^Y$; the closure of $A$ taken in $X$ is $\overline{A}^X$. The interior of $A$ in $Y$ is $A^{\circ,Y}$, etc. The full notation registry is on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Motivation

When we restrict attention from an ambient space $X$ to a subspace $Y$, the topology on $Y$ changes (it gains sets that were not open in $X$ — see [[Def - Subspace Topology]]), and we must ask how the standard topological operations transform. The first natural question is how the closure operation behaves: given a subset $A \subseteq Y$, does its closure in $Y$ equal its closure in $X$, or differ?

The answer is clean: the closure of $A$ in $Y$ is the *trace* of the closure of $A$ in $X$:
$$\overline{A}^Y = \overline{A}^X \cap Y.$$
The closure shrinks by exactly the amount of the closure that lies outside $Y$. Intuitively, when you restrict to $Y$, the points outside $Y$ are no longer available to be limits, so they are discarded — but the points inside $Y$ that were closure-points in $X$ remain closure-points in $Y$, because the basis elements meeting $A$ in $X$ trace down to basis elements meeting $A$ in $Y$.

The result is more than a curiosity. It is the source of a standard discipline in topology: when you see a closure inside a subspace, the safer reflex is to *compute it in the ambient* and intersect. This avoids the subtle errors that come from working purely in the subspace topology, where one might lose track of which open sets are available.

The corresponding statement for *interiors* is not equally clean — there is only a one-sided containment $A^{\circ, Y} \supseteq A^{\circ, X} \cap Y$, and this can be strict. The asymmetry between closure and interior is a small but persistent source of bugs, and understanding *why* the closure result is symmetric while the interior result is not is part of the working topologist's basic equipment.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is the inclusion chain $A \subseteq Y \subseteq X$ with $Y$ a subspace.

The first source is **a nested chain of subspaces.** Property $B$: $A \subseteq Z \subseteq Y \subseteq X$ with $Y$ a subspace of $X$ and $Z$ a subspace of $Y$. Then $Z$ is also a subspace of $X$ (transitivity), and the formula applies in any pair: $\overline{A}^Z = \overline{A}^Y \cap Z = \overline{A}^X \cap Z$, allowing computation at the most convenient level. *Example:* computing closures in a submanifold by lifting to Euclidean space and intersecting back.

The second source is **a closed subspace.** Property $B$: $Y$ is closed in $X$. Then $\overline{A}^X \subseteq Y$ (the closure of a subset of a closed set is contained in the closed set), so $\overline{A}^Y = \overline{A}^X$ — the closures coincide. The intersection with $Y$ becomes trivial because the entire closure is already in $Y$. *Example:* the closure of $\mathbb{Q} \cap [0, 1]$ inside $[0, 1]$ equals the closure inside $\mathbb{R}$ (both equal $[0, 1]$), because $[0, 1]$ is closed in $\mathbb{R}$.

The third source is **dense subset condition.** Property $B$: $A$ is dense in $Y$, i.e. $\overline{A}^Y = Y$. By the formula, this happens iff $\overline{A}^X \cap Y = Y$ iff $Y \subseteq \overline{A}^X$. So density of $A$ in $Y$ is the same as $Y \subseteq \overline{A}^X$ — a containment in the ambient closure. *Example:* $\mathbb{Q}$ dense in $\mathbb{R}$ implies $\mathbb{Q} \cap (0, 1)$ dense in $(0, 1)$, since $(0, 1) \subseteq \mathbb{R} = \overline{\mathbb{Q}}^\mathbb{R}$.

**Targets (Output Amplification)**

The conclusion is the equality $\overline{A}^Y = \overline{A}^X \cap Y$.

Combine with **a continuity argument.** Property $D$: $f : X \to W$ is continuous and $A \subseteq Y$. The amplified result $E$: the restriction $f|_Y$ has $f|_Y(\overline{A}^Y) \subseteq \overline{f(A)}^W$, derivable from $f(\overline{A}^X) \subseteq \overline{f(A)}^W$ and the closure-in-subspace formula. This is how one transfers approximation arguments between a subspace and the ambient.

Combine with **density transfer.** Property $D$: $A$ is dense in $X$. The amplified result $E$: $A \cap Y$ is dense in $Y$ if and only if $Y \subseteq \overline{A}^X = X$ — automatically true. So a dense subset of $X$ traces to a dense subset of *any* subspace $Y$ — *provided* $A$ actually meets $Y$ (otherwise $A \cap Y = \emptyset$ has empty closure). The combination is the standard route to building dense subsets of subspaces from dense subsets of the ambient.

Combine with **the boundary of a subspace.** Property $D$: $A \subseteq Y \subseteq X$. The amplified result $E$: $\partial^Y A = (\overline{A}^X \cap Y) \setminus (A^{\circ, Y})$, where the interior part is *not* in general $A^{\circ, X} \cap Y$. The boundary in the subspace can be *smaller* than the trace of the boundary in the ambient — points that were boundary points of $A$ in $X$ may have been "moved into the interior" because the subspace has more open sets available.

---

# Why Is It True

The cleanest reason runs through the characterization of closure as "every basis element containing $x$ meets $A$" (see [[Thm - Characterizations of the Closure]]).

A basis for the subspace topology on $Y$ consists of intersections $B \cap Y$ where $B$ is a basis element of $X$. So saying "$x \in \overline{A}^Y$" is saying "every basis element of $Y$ containing $x$ meets $A$", which is "every set of the form $B \cap Y$ containing $x$ (i.e. $B$ contains $x$, automatically since $x \in Y$, and $B$ is a basis element of $X$) meets $A$".

But $A \subseteq Y$, so $(B \cap Y) \cap A = B \cap A$ — the intersection with $Y$ is silent because $A$ is already in $Y$. So "every $B \cap Y$ containing $x$ meets $A$" is the same as "every basis element $B$ of $X$ containing $x$ meets $A$", which is precisely "$x \in \overline{A}^X$". Combined with $x \in Y$, we have $x \in \overline{A}^X \cap Y$ iff $x \in \overline{A}^Y$, which is the formula.

The deeper structural reason: the closure operator is *built from* the open-set structure, and the subspace topology is *built from* the ambient open sets by tracing them onto $Y$. So the operations stack in the obvious way: the closure operator on $Y$ is the closure operator on $X$ followed by intersection with $Y$. The formula is the algebraic expression of this stacking.

**Why does this fail for interiors?** The interior of $A$ in $X$ uses open sets of $X$; the interior in $Y$ uses open sets of $Y$, which include intersections $U \cap Y$ for open $U$ in $X$. A point $x$ can be in the $Y$-interior of $A$ (some $Y$-open set $V \subseteq A$ contains $x$) without being in the $X$-interior of $A$, because the $Y$-open set $V$ might not be open in $X$. The interior has a *larger* family of test sets in the subspace, so the interior in $Y$ can be *bigger* than the trace of the interior in $X$. The inclusion $A^{\circ, Y} \supseteq A^{\circ, X} \cap Y$ is the corresponding statement, and it is in general strict.

Closure does not suffer this because the closure characterization uses the *meet-property* of open sets, which is preserved under intersection with $Y$: an open set meeting $A$ in $X$, traced down, becomes an open set in $Y$ meeting $A$. Going the other way is also automatic: a subspace-open set meeting $A$ comes from an ambient-open set meeting $A$. So the closure characterization symmetrizes, while the interior characterization does not.

---

# What Makes This Hard

The non-obvious step is to realize that the closure formula is *symmetric* in the basis-element form ($A$ being a subset of $Y$ means the $\cap Y$ is silent) while the interior formula is *not* — the interior in $Y$ uses a *larger* family of opens, while the closure in $Y$ effectively uses *the same* opens (since intersecting with $Y$ doesn't change whether a set meets $A$ when $A \subseteq Y$). The most common error is to misremember the interior version as equally clean: writing $A^{\circ, Y} = A^{\circ, X} \cap Y$ is *wrong*, and the right statement is only the containment $\supseteq$.

---

# Rederivation Scaffold

**High-level strategy:**
Use the basis-element characterization of closure. Open sets of $Y$ are intersections $B \cap Y$ for $B$ open in $X$; since $A \subseteq Y$, intersecting $B$ with $Y$ does not change whether $B$ meets $A$. So the closure in $Y$ and the closure in $X$ are detected by the same "meeting" condition, modulo whether the point is in $Y$.

**Subgoal decomposition:**

1. **Show $\overline{A}^Y \subseteq \overline{A}^X \cap Y$.**
   - *Hint:* $\overline{A}^X \cap Y$ is closed in $Y$ (intersection of closed-in-$X$ with $Y$ is closed-in-$Y$) and contains $A$. By the universal property of closure, it contains $\overline{A}^Y$.
   - *Why needed:* One half of the equality, by an easy set-theoretic universal-property argument.

2. **Show $\overline{A}^X \cap Y \subseteq \overline{A}^Y$.**
   - *Hint:* Let $x \in \overline{A}^X \cap Y$. Every open neighbourhood $V$ of $x$ in $Y$ is $U \cap Y$ for some open $U$ in $X$, and $U$ contains $x$. Since $x \in \overline{A}^X$, $U \cap A \neq \emptyset$. Since $A \subseteq Y$, $U \cap A = (U \cap Y) \cap A = V \cap A$, so $V \cap A \neq \emptyset$. Hence $x \in \overline{A}^Y$.
   - *Why needed:* The other half, by the open-set characterization of closure.

3. **Note the interior counterexample.**
   - *Hint:* $A = [0, 1)$, $Y = [0, 2)$, $X = \mathbb{R}$. Then $A^{\circ, X} = (0, 1)$, so $A^{\circ, X} \cap Y = (0, 1)$. But $[0, 1/2) = (-\varepsilon, 1/2) \cap Y$ is open in $Y$ and contained in $A$, so $0 \in A^{\circ, Y}$. Hence $A^{\circ, Y} = [0, 1) \supsetneq (0, 1) = A^{\circ, X} \cap Y$.
   - *Why needed:* Calibrates the asymmetry between closure and interior.

---

# Lemma Decomposition

> [!note]- Lemma 1: $C \subseteq Y$ is closed in $Y$ iff $C = F \cap Y$ for some closed $F$ in $X$
> **Statement:** A subset $C$ of $Y$ is closed in the subspace topology iff there is a closed $F \subseteq X$ with $C = F \cap Y$.
>
> **Hint:** Take complements: $Y \setminus C$ is open in $Y$ iff $Y \setminus C = U \cap Y$ for some open $U$ in $X$.
>
> **Why needed:** Sets up the side $\overline{A}^X \cap Y$ as a closed subset of $Y$ containing $A$.
>
> > [!note]- Full proof
> > ($\Rightarrow$) $C$ closed in $Y$ means $Y \setminus C$ open in $Y$, so $Y \setminus C = U \cap Y$ for some $U$ open in $X$. Then $C = Y \cap (X \setminus U) = (X \setminus U) \cap Y$, with $X \setminus U$ closed in $X$.
> >
> > ($\Leftarrow$) If $C = F \cap Y$ with $F$ closed in $X$, then $Y \setminus C = Y \setminus (F \cap Y) = (X \setminus F) \cap Y$, and $X \setminus F$ open in $X$, so $Y \setminus C$ is open in $Y$, hence $C$ closed in $Y$.

> [!note]- Lemma 2: Basis of subspace topology
> **Statement:** If $\mathcal{B}$ is a basis for the topology of $X$, then $\{B \cap Y : B \in \mathcal{B}\}$ is a basis for the subspace topology on $Y$.
>
> **Hint:** Open sets of $Y$ are $U \cap Y$ for $U$ open in $X$; write $U = \bigcup B_\alpha$, intersect: $U \cap Y = \bigcup (B_\alpha \cap Y)$.
>
> **Why needed:** Powers the basis-element characterization argument.
>
> > [!note]- Full proof
> > Let $V \subseteq Y$ be open in $Y$. Then $V = U \cap Y$ for $U$ open in $X$, and $U = \bigcup_\alpha B_\alpha$ with $B_\alpha \in \mathcal{B}$. So $V = U \cap Y = (\bigcup B_\alpha) \cap Y = \bigcup(B_\alpha \cap Y)$, a union of elements of $\{B \cap Y : B \in \mathcal{B}\}$. This is the definition of basis.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq Y \subseteq X$ with $Y$ carrying the subspace topology.
>
> **$\overline{A}^Y \subseteq \overline{A}^X \cap Y$.**
> By Lemma 1, $\overline{A}^X \cap Y$ is closed in $Y$ (intersection of $Y$ with a closed set in $X$). It contains $A$ (since $A \subseteq \overline{A}^X$ and $A \subseteq Y$). The closure $\overline{A}^Y$ is by definition the *smallest* closed-in-$Y$ set containing $A$, so $\overline{A}^Y \subseteq \overline{A}^X \cap Y$.
>
> **$\overline{A}^X \cap Y \subseteq \overline{A}^Y$.**
> Let $x \in \overline{A}^X \cap Y$. We show $x \in \overline{A}^Y$ via the characterization of [[Thm - Characterizations of the Closure]]: every open set in $Y$ containing $x$ meets $A$.
>
> Let $V \subseteq Y$ be open in $Y$ with $x \in V$. By the definition of the subspace topology, $V = U \cap Y$ for some open $U$ in $X$; since $x \in V \subseteq U$, $U$ is an open set in $X$ containing $x$. Because $x \in \overline{A}^X$, $U \cap A \neq \emptyset$. Now $A \subseteq Y$ gives $U \cap A = U \cap A \cap Y = (U \cap Y) \cap A = V \cap A$. So $V \cap A \neq \emptyset$, and by the characterization, $x \in \overline{A}^Y$.
>
> Both containments combine to give $\overline{A}^Y = \overline{A}^X \cap Y$. $\blacksquare$
>
> **Interior counterexample.** Take $X = \mathbb{R}$, $Y = [0, 2)$, $A = [0, 1)$. Then $A^{\circ, X} = (0, 1)$, so $A^{\circ, X} \cap Y = (0, 1)$. In $Y$, the set $[0, 1/2)$ is open ($[0, 1/2) = (-1, 1/2) \cap [0, 2)$), is contained in $A$, and contains $0$. So $0 \in A^{\circ, Y}$, but $0 \notin A^{\circ, X} \cap Y$. Hence $A^{\circ, Y} = [0, 1) \neq (0, 1) = A^{\circ, X} \cap Y$, with the containment going the "wrong way" relative to the closure formula:
> $$A^{\circ, Y} \supsetneq A^{\circ, X} \cap Y \quad\text{(strict).}$$

---

# Cross-Field Exercise Suggestions

**Density of rationals in subintervals.** Use the closure-in-subspace formula to deduce that $\mathbb{Q} \cap (a, b)$ is dense in $(a, b)$ for every interval $a < b$ in $\mathbb{R}$. Compute $\overline{\mathbb{Q} \cap (a, b)}^{(a,b)} = \overline{\mathbb{Q} \cap (a, b)}^\mathbb{R} \cap (a, b)$; the ambient closure includes all of $[a, b]$ (every real is a limit of rationals), so intersecting with $(a, b)$ gives $(a, b)$. So $\mathbb{Q} \cap (a, b)$ is dense in $(a, b)$. The application uses the formula to *transfer* density between ambient and subspace.

**Closure of a subgroup.** In a topological group $G$, a subgroup $H \leq G$ has closure $\overline{H}$ that is also a subgroup (see the discussion in [[Thm - Characterizations of the Closure#Cross-Field Exercise Suggestions]]). If $K \leq G$ contains $H$, then $\overline{H}^K = \overline{H}^G \cap K$ — the closure of $H$ within any subgroup $K$ containing $H$ is the trace of the ambient closure. This is used in Lie theory to compute the closure of a subgroup inside a larger Lie subgroup.

**Submanifolds and closure.** If $M \subseteq \mathbb{R}^n$ is a submanifold and $A \subseteq M$, then $\overline{A}^M = \overline{A}^{\mathbb{R}^n} \cap M$. This lets one compute closures on a submanifold by working in Euclidean space and tracing back. The application is the standard route for analyzing limits and convergence on a submanifold via the ambient.

**Failure for the interior in distributional language.** The strictness of the interior containment is the topological reason that the *boundary* of a domain $\Omega \subseteq \mathbb{R}^n$, when viewed as a manifold-with-boundary, has its own interior structure that differs from the trace of the ambient. The "manifold interior" of $[0, 1] \subseteq \mathbb{R}$ (i.e., the set of points where $[0, 1]$ has a manifold-interior chart) is $[0, 1]$ itself; the "ambient interior" is $(0, 1)$. The distinction is what distinguishes a "manifold with boundary" from "the topological interior of a closed set in an ambient".

---

# Bridges

- **[[Def - Subspace Topology]]** — the topology on $Y$ being used. The formula is the *behaviour of closure under restriction*, dual to the universal property of the subspace topology.

- **[[Def - Closure, Interior, and Boundary]]** — the definitions being compared between $X$ and $Y$. The formula is the relationship between $\overline{\cdot}^X$ and $\overline{\cdot}^Y$.

- **[[Thm - Characterizations of the Closure]]** — the basis-element form of the closure characterization is the engine of the proof. The formula is essentially a corollary of how the characterization restricts to a subspace.

- **[[Topology I — §1–3 Metric and Topological Spaces#Most Reusable Properties|Subspace universal property]]** — the same intuition (the subspace topology forgets what is happening outside $Y$) appears in the universal property and the closure formula. Both say: "the subspace is the right shadow of the ambient onto $Y$".

---

# Unlocked by This

> [!tip] Closed Submanifold Convergence *(from Differential Geometry)*
> If $M$ is a closed submanifold of $\mathbb{R}^n$ (i.e., $M$ is closed in the topological sense in $\mathbb{R}^n$), the closure of a sequence in $M$ inside $M$ equals its closure in $\mathbb{R}^n$. This is the case where the closure-in-subspace formula has $\overline{A}^X \subseteq Y$, so the intersection is trivial. **Closed submanifolds** thus inherit completeness from the ambient — every Cauchy sequence in $M$ converges in $M$ — which is the topological substrate of geodesic completeness.

> [!tip] Boundary of a Domain in Several Variables *(from Multivariate Analysis)*
> For a domain $\Omega \subseteq \mathbb{R}^n$ (open, connected), the boundary $\partial \Omega = \overline{\Omega}^{\mathbb{R}^n} \setminus \Omega$ is the topological boundary in the ambient. When restricting to a sub-domain $\Omega' \subseteq \Omega$, the closure relations follow the subspace formula. This is used in PDE theory: the trace of a function from $\Omega$ onto $\partial\Omega$ is computed via closure operations that respect the subspace structure.
