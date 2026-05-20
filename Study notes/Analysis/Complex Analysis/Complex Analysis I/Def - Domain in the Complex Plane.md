---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Topological Space"
  - "Def - Path-Connected Space"
  - "Def - Connected Space"
tags: [analysis, complex-analysis]
---

# Notation

Throughout, $\mathbb{C}$ is the complex plane, identified as a topological space with $\mathbb{R}^2$ via $z = x + iy \leftrightarrow (x, y)$. An **open set** $U \subseteq \mathbb{C}$ is a subset such that for every $a \in U$ there is some $r > 0$ with $D(a, r) = \{z : |z - a| < r\} \subseteq U$. We write $D \subseteq \mathbb{C}$ for a domain in this technical sense (not to be confused with "domain of a function"). The full notation registry is on the parent topic page [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

The whole point of complex analysis is that holomorphic functions are *rigid* — determined by their values on tiny pieces. But for any rigidity statement to make sense, the underlying set must not be allowed to break into independent islands. If $U = U_1 \sqcup U_2$ is the union of two disjoint open pieces, a function holomorphic on $U$ can take *one* analytic identity on $U_1$ and a completely independent one on $U_2$ — its values on $U_1$ tell you nothing about $U_2$. The identity theorem, the constancy-from-zero-derivative argument, analytic continuation: all of them implicitly require that information can *propagate* from one point to another, and the carrier of that propagation is a path.

So the first axiom is **path-connectedness**. We want every two points $z, w \in D$ joined by a continuous curve $\gamma : [0, 1] \to D$ with $\gamma(0) = z, \gamma(1) = w$. This is exactly the condition that lets us run a chain-rule argument along a path — for instance, to show that a holomorphic function with zero derivative is constant: integrate the derivative along the path between $z$ and $w$. Without connectedness, the argument stops at the first gap. (One could try ordinary [[Def - Connected Space|topological connectedness]] instead, but for open subsets of $\mathbb{C} \cong \mathbb{R}^2$ — which is locally path-connected — the two notions coincide, so the choice is harmless.)

The second axiom is **openness**. Differentiability is a local condition: $f'(w)$ asks about the behaviour of $f$ on an arbitrarily small disc around $w$. If $w$ is a boundary point of the set, then $f$ is not defined on some directions of approach, and the limit defining $f'(w)$ does not make sense. The cleanest setting is an open set, where every point has a full disc neighbourhood. Closed sets, half-open sets, and curves in $\mathbb{C}$ are *not* domains in our sense — they are too small to support an honest theory of complex differentiation.

The third is **non-emptiness**. The empty set satisfies the other two conditions vacuously but is uninteresting; ruling it out spares us from having to say "non-empty $D$" in every theorem. It is a convenience, not a deep requirement.

The discipline of working *only on domains* — rather than on arbitrary open sets — is what makes Cauchy's theorem, the identity theorem, the maximum modulus principle, and the existence of branches of the logarithm tractable. Each of these statements *fails* on disconnected open sets in a trivial way: take a different function on each component. Restricting to domains rules out the trivial counterexamples and leaves only the genuine analytic content.

---

# The Definition

A **domain** in $\mathbb{C}$ is a non-empty, path-connected, open subset $D \subseteq \mathbb{C}$.

Equivalently (since $\mathbb{C} \cong \mathbb{R}^2$ is locally path-connected): a non-empty, connected, open subset. The equivalence is a standard topology result — for locally path-connected spaces, connectedness and path-connectedness agree.

A **simply connected domain** is a domain in which every closed curve is contractible (can be continuously deformed to a point inside $D$). This stronger condition will be needed for the existence of branches of the logarithm and for the strongest form of Cauchy's theorem.

---

# Categorical Definition

A domain in $\mathbb{C}$ is a **connected non-empty open subobject of $\mathbb{C}$** in the category $\mathbf{Top}$, equipped with the additional complex-analytic structure inherited from $\mathbb{C}$. The categorical viewpoint usefully separates two pieces of data: the underlying topological subobject and the [[Def - Holomorphic Function|holomorphic]] structure.

The vocabulary: in any category $\mathcal{C}$, a *subobject* of an object $X$ is an equivalence class of monomorphisms into $X$. In $\mathbf{Top}$, the monomorphisms into $\mathbb{C}$ are exactly the injective continuous maps, and the subobjects relevant for analysis are the topological subspaces — pairs $(D, \iota)$ where $D \subseteq \mathbb{C}$ carries the [[Def - Subspace Topology|subspace topology]] and $\iota : D \hookrightarrow \mathbb{C}$ is the inclusion. Among all such subobjects, the *open* ones are distinguished by the further condition that $D \in \tau_{\mathbb{C}}$; equivalently, the inclusion $\iota$ is an *open embedding*, meaning it is a topological embedding whose image is open. Open subobjects form a sub-poset of the subobject lattice — closed under finite intersection and arbitrary union, in line with the topology axioms.

Connectedness is the further categorical property: in $\mathbf{Top}$, an object $D$ is **connected** if $\operatorname{Hom}_{\mathbf{Top}}(D, \{0, 1\}_{\text{disc}})$ has exactly two elements (the two constant maps) — i.e., no non-trivial continuous map to the two-point discrete space. Equivalently, $D$ is connected if it cannot be written as the coproduct $D \cong A \sqcup B$ of two non-empty open subobjects of itself. Path-connectedness is the stronger condition that the connected component of every pair of points contains a path, expressible as: the canonical map $\pi_0^{\text{path}}(D) \to \pi_0(D)$ from path-components to connected components is a bijection. For open subobjects of $\mathbb{C} \cong \mathbb{R}^2$ — which is locally path-connected — the two notions agree, so a domain is unambiguously a connected non-empty open subobject.

The complex structure adds another layer. Above $\mathbf{Top}$ sits the category $\mathbf{CplxMan}$ of complex manifolds (one-dimensional), and $\mathbb{C}$ is its tautological object of complex dimension $1$. Every open subobject $D \hookrightarrow \mathbb{C}$ inherits a unique complex structure from $\mathbb{C}$ such that the inclusion is holomorphic — this is the *pullback of the complex structure along the inclusion*, the complex-analytic counterpart of the subspace topology. A domain is thus precisely a connected non-empty open subobject of $\mathbb{C}$ *in $\mathbf{CplxMan}$* — a 1-dimensional complex submanifold of $\mathbb{C}$ that happens to be an open subset. Simply connected domains form an even more restrictive subclass, distinguished by the categorical condition $\pi_1(D) = 0$ (the trivial fundamental group), which is the universal cover condition that makes every multi-valued holomorphic function on $D$ (such as the logarithm or fractional powers) split into single-valued branches.

---

# Relate to Other Fields / Compression

In **topology**, a domain in $\mathbb{C}$ is a connected open subset of a metric space — the standard setting in which one does analysis. The same notion appears in real multivariable analysis: a "domain" in $\mathbb{R}^n$ is a connected open subset, and statements like "a $C^1$ function on a domain with zero gradient is constant" require exactly this hypothesis.

In **algebraic geometry**, the analogous notion is an *irreducible* open subset of an algebraic variety — algebraic geometry replaces path-connectedness with the algebraic condition that the coordinate ring has no nontrivial idempotents. The intuition is the same: a "domain" is a set on which one cannot perform a trivial decomposition.

In **PDE theory**, "domain" is the standard name for the region on which a PDE is posed — exactly because the boundary value problem only makes sense for an open set with a well-defined boundary, and connectedness is needed for uniqueness arguments to propagate from one boundary piece to the others.

---

# Examples / Corollaries

**Is an instance — the whole plane $\mathbb{C}$.** Open (every point has a disc neighbourhood), path-connected (every two points joined by a line segment), non-empty. This is the most permissive domain, where entire functions live.

**Is an instance — the open disc $D(a, r)$.** Open by definition; path-connected because any two points $z_1, z_2 \in D(a, r)$ are joined by the line segment $t \mapsto (1-t)z_1 + tz_2$, which lies in $D(a, r)$ by convexity (a disc is convex). Non-empty when $r > 0$. The prototypical local domain.

**Is an instance — the slit plane $\mathbb{C} \setminus (-\infty, 0]$.** Open (the complement of a closed set), path-connected (any two points are joined by a path that detours around the slit), non-empty. This is the canonical domain on which the principal branch of the logarithm is defined.

**Is an instance — the punctured plane $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$.** Open, path-connected (go through a path avoiding the origin), non-empty. It is a domain, but *not* simply connected — there are loops around the origin that cannot be contracted. This is the canonical example of "domain without a branch of $\log$".

**Is NOT an instance — the closed disc $\overline{D(a, r)} = \{z : |z - a| \leq r\}$.** The boundary points are not interior, so the set is not open. Complex differentiability at a boundary point is not well-defined.

**Is NOT an instance — $D(0, 1) \cup D(3, 1)$.** Two disjoint discs: open and non-empty, but not path-connected (no path in the set joins a point in one disc to a point in the other). A holomorphic function on this set is two independent holomorphic functions, and theorems fail trivially.

**Is NOT an instance — the real line $\mathbb{R} \subseteq \mathbb{C}$.** Not open in $\mathbb{C}$: any point of $\mathbb{R}$ has no disc neighbourhood in $\mathbb{R}$. Not a domain in the complex sense, though it is a perfectly good domain in real analysis (where openness is taken in $\mathbb{R}$).

**Corollary — a holomorphic function on a domain with zero derivative is constant.** This is the prototype consequence: see [[Thm - Constant on a Domain if Derivative is Zero]]. The path-connectedness is essential — without it, the function can be different constants on different components.

**Calibration check.** Verify that the closed disc $\overline{D(0, 1)}$ is *not* a domain, because boundary points have no disc neighbourhood — complex differentiability at the boundary is not well-defined. Verify that the union of two disjoint open discs $D(0, 1) \cup D(3, 1)$ is *not* a domain, because path-connectedness fails — a holomorphic function on this set decouples into two independent functions on the two components. And verify that the slit plane $\mathbb{C} \setminus (-\infty, 0]$ *is* a domain (open, path-connected via detours around the slit, non-empty), but the punctured plane $\mathbb{C}^\times$ is a domain that is *not simply connected* — loops around the origin cannot be contracted.

---

# Unlocked by This

> [!tip] Cauchy's Theorem and the Identity Theorem *(from this topic)*
> The hypothesis "$f$ holomorphic on a domain $D$" is the universal precondition for every major theorem of the subject: Cauchy's theorem on a simply connected domain, the identity theorem on a connected open set, the maximum modulus principle. The classification of domains by their topology — simply connected, multiply connected — directly governs what theorems apply.

> [!tip] Riemann Surfaces *(from Complex Geometry)*
> A **Riemann surface** is a one-dimensional complex manifold — locally biholomorphic to a domain in $\mathbb{C}$. The data of domains and biholomorphisms between them is exactly the local data needed to build a Riemann surface, and the global topology (simply connected, genus, etc.) becomes the central object of study.
