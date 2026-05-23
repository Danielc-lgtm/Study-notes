---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Def - The Tangent Space"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, gauge-theory, topology, index]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold and $v$ is a smooth tangent vector field on $M$ — a section of $TM$ in the sense of [[Def - Vector Field on a Manifold]]. A point $p \in M$ is a **zero** (or *singularity*) of $v$ if $v(p) = 0$; we assume zeros are *isolated*. We write $S^{n-1}_\epsilon(p)$ for a sufficiently small geodesic sphere around $p$ (in any Riemannian metric on $M$); $S^{n-1}$ for the unit sphere in $\mathbb{R}^n$. The index is denoted $j_v(p)$ (Frankel's notation, from "Kronecker index") or sometimes $\mathrm{ind}_p(v)$. For the parent notation registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

We want to attach to each zero of a vector field a *single integer* that encodes "how the field rotates around the zero". The motivating examples are clear-cut. On the plane $\mathbb{R}^2$, the field $v(x, y) = (x, y)$ (a *source*) has all arrows pointing radially outward; walking once counterclockwise around the origin, the arrow rotates once counterclockwise too. The field $v(x, y) = (-x, -y)$ (a *sink*) similarly has all arrows pointing inward; walking around, the arrow still rotates once counterclockwise. The field $v(x, y) = (x, -y)$ (a *saddle*) has two horizontal arrows outward and two vertical arrows inward; walking around, the arrow rotates *backwards*, completing one full turn clockwise. We want the index to be $+1$ for source and sink, $-1$ for saddle, and we want it to encode this rotation count cleanly.

The first decision is what to count rotations of. The vector field $v$ at a point $q$ near $p$ is non-zero (since $p$ is the only zero in a small ball), so it has a direction $v(q)/|v(q)|$. As $q$ traces out a small sphere around $p$, this unit vector traces out a curve in the unit sphere of the tangent space — and that curve's winding (its **Brouwer degree**) is the integer we want. There is one immediate complication: $v(q)$ lives in $T_qM$, which is *not* the same vector space as $T_pM$. To compare directions at different $q$'s we need either a Riemannian metric (giving an orthonormal frame to express each vector in) or a local coordinate chart (giving a basis at every point). Either choice works and gives the same answer, because the index turns out to be invariant under both — which is the main thing the definition needs to verify.

Why insist on isolated zeros? A vector field with a *continuous family* of zeros (say $v = 0$ on a curve) has no single point at which to evaluate an index. Restricting to isolated zeros covers all generic cases — for *generic* fields, the simultaneous vanishing of $n$ component functions is a codimension-$n$ condition, hence isolated points in an $n$-manifold — and is enough for the most important downstream theorem, [[Thm - Poincare-Hopf Theorem|Poincaré-Hopf]]. The definition does extend to higher-dimensional zero sets via a different machinery (intersection theory of the zero section), but this is not needed here.

Why the small-sphere construction rather than (say) the Hessian eigenvalues? For non-degenerate zeros — those where the linearization $Dv_p$ is invertible — the index is $\mathrm{sign}(\det Dv_p) \in \{\pm 1\}$, a single bit. But for *degenerate* zeros (where $Dv_p$ is singular) the index can be any integer, positive or negative, with absolute value as large as you like. The stereographic-projection field on $S^2$ has a single zero of index $+2$ at the north pole; multiplying that field by itself (in a complex sense) gives a field with a single zero of index $+k$ for any $k$. The sphere construction handles degenerate and non-degenerate cases uniformly: just count rotations.

Why does the index need to be an integer? Because a continuous map $S^{n-1} \to S^{n-1}$ has an integer degree — this is the [[Def - Brouwer Degree of a Map|Brouwer degree]] (or equivalently the winding number when $n = 2$). The integrality is *forced* by the topology of spheres, not chosen by us. The deeper meaning: a small perturbation of $v$ might split a degenerate zero into several non-degenerate ones, with the algebraic sum of their indices equalling the original index. The total index of a finite collection of zeros is therefore stable under deformation — this stability is what makes Poincaré-Hopf's claim (total index $= \chi(M)$) sensible at all.

Finally, why call this a *Kronecker* index? Kronecker introduced this construction in 19th-century classical algebraic topology — long before the language of degree theory was systematic — when studying the count of solutions of a system of polynomial equations. The modern Brouwer-degree formulation and the topological intuition are due to Brouwer (1911) and Heinz Hopf (whose proof of Poincaré-Hopf in arbitrary dimensions appeared in 1926). The name "Kronecker" is preserved as a historical marker.

---

# The Definition

Let $v$ be a smooth vector field on a smooth $n$-manifold $M$ and let $p \in M$ be an *isolated zero* of $v$ — meaning there is an open neighbourhood $U$ of $p$ in which $p$ is the only zero of $v$.

Choose a coordinate chart $(U, \varphi)$ centred at $p$ (so $\varphi(p) = 0$) and a small enough $\epsilon > 0$ that the closed ball $\overline{B_\epsilon(0)} \subset \varphi(U)$ contains no zero of $v$ other than $p$ itself. Inside this chart $v$ has components $v^1, \dots, v^n$. Define the map

$$\Phi_v : S^{n-1}_\epsilon \to S^{n-1}, \qquad q \mapsto \frac{(v^1(q), \dots, v^n(q))}{\sqrt{(v^1(q))^2 + \dots + (v^n(q))^2}},$$

where $S^{n-1}_\epsilon = \{x \in \mathbb{R}^n : |x| = \epsilon\}$ is the small sphere around $p$ in chart coordinates and $S^{n-1}$ is the unit sphere in $\mathbb{R}^n$. The map $\Phi_v$ is smooth because $v$ has no zero on $S^{n-1}_\epsilon$.

The **index** (or **Kronecker index**) of $v$ at $p$ is

$$j_v(p) := \deg(\Phi_v) \in \mathbb{Z},$$

the Brouwer degree of $\Phi_v$ (see [[Def - Brouwer Degree of a Map]]).

**Two-dimensional explicit formula.** For $n = 2$, parameterize $S^1_\epsilon$ by an angle $s \in [0, 2\pi)$ and let $\theta(s)$ be the angle that $v(\gamma(s))$ makes with the $+x$-axis. Then

$$j_v(p) = \frac{1}{2\pi}\oint_{S^1_\epsilon} d\theta = \frac{1}{2\pi}\int_0^{2\pi} \theta'(s)\,ds.$$

**Well-definedness.** The integer $j_v(p)$ is independent of the choice of chart, the choice of $\epsilon$ (for sufficiently small $\epsilon$), and any Riemannian metric used to identify directions. The independence follows because the degree of a map varies continuously in the data, and the integer it produces cannot jump.

---

# Categorical / Structural Definition

In the language of intersection theory, the index $j_v(p)$ is the **local intersection number** of the section $v : M \to TM$ with the zero section $0 : M \to TM$ at the point $p$. More precisely: $v$ and $0$ are two sections of $TM$ that meet at $p$ (since $v(p) = 0 = 0(p)$), and the local intersection number is the signed count of how transversely they meet — the sign of $\det Dv_p$ when this is non-zero, and a higher-multiplicity Brouwer degree otherwise. The global statement $\sum_p j_v(p) = \chi(M)$ of Poincaré-Hopf is then the equation $[v] \cdot [0] = \chi(M)$ in the intersection ring of $TM$, expressing the **Euler class** of $TM$ as $\chi(M) \cdot [\mathrm{pt}]$ on $M$.

---

# Relate to Other Fields / Compression

The index is a special case of the **degree of a map**, which is the simplest non-trivial topological invariant. For a smooth map $f : N \to N$ between closed oriented $n$-manifolds of the same dimension, the degree counts (with sign) the preimages of a regular value. The index of a vector field at a zero is the degree of the "direction-of-$v$" map on a small sphere. Other instances of the same construction: the **winding number** of a closed plane curve around a point is the degree of $\gamma : S^1 \to S^1$; the **linking number** of two disjoint closed curves in $\mathbb{R}^3$ is the degree of a Gauss map $T^2 \to S^2$; the **Brouwer fixed point theorem** is a degree-theoretic statement.

**True name:** The index of $v$ at $p$ is **"the number of times the direction of $v$ rotates as you walk once counterclockwise around $p$"**. In two dimensions this is literally a winding number; in higher dimensions it is the Brouwer degree of the direction map, but the intuition "how many times does $v/|v|$ wind around" remains the right mental picture.

---

# Examples / Corollaries

**Is an instance: Source $v = (x, y)$ on $\mathbb{R}^2$.** Around any small circle, $v$ points radially outward, and its direction rotates exactly one full counterclockwise turn as you walk once around. Index $= +1$. Same for a sink $v = (-x, -y)$: direction rotates one full counterclockwise turn despite arrows pointing inward.

**Is an instance: Saddle $v = (x, -y)$ on $\mathbb{R}^2$.** Pointing rightward at $(1, 0)$, downward at $(0, 1)$, leftward at $(-1, 0)$, upward at $(0, -1)$. As you walk counterclockwise around the origin, $v$ rotates *clockwise* — once backwards. Index $= -1$.

**Is an instance: Centre $v = (-y, x)$ on $\mathbb{R}^2$.** Tangent to circles, rotating with you. Walking counterclockwise, $v$ rotates counterclockwise too, once. Index $= +1$. A centre is structurally different from a source (no integral curves escape), but has the same index — index sees only the rotation count, not the qualitative dynamics.

**Is an instance: Dipole $v = (x^2 - y^2, 2xy)$ on $\mathbb{R}^2$.** This is the real and imaginary parts of $z^2 = (x + iy)^2$. As $z$ goes around the unit circle, $z^2$ goes around twice. Index $= +2$. More generally, $v = \mathrm{Re}(z^k), \mathrm{Im}(z^k)$ has index $k$ at the origin; you can manufacture any integer index this way.

**Is an instance: Stereographic-projection field on $S^2$.** Project a uniform field $\partial/\partial u$ on $\mathbb{R}^2$ stereographically onto $S^2$ from the north pole, then push forward. Result: a smooth field on $S^2$ with a single zero at the north pole. In the chart near the north pole the field looks like $-z^2 \partial/\partial\bar z$ for the complex coordinate $z$; index $= +2$. Matches $\chi(S^2) = 2$.

**Is NOT an instance (degenerate): $v = 0$ identically on $\mathbb{R}^2$.** Every point is a zero, none isolated; the index is undefined. The definition requires an isolated zero.

**Is NOT an instance (degenerate): $v = (x, 0)$ on $\mathbb{R}^2$.** Vanishes along the entire $y$-axis. Not isolated; index undefined at any single point.

**Corollary (non-degenerate zeros).** If the linearization $Dv_p$ at a zero $p$ is invertible, then $j_v(p) = \mathrm{sign}(\det Dv_p) \in \{+1, -1\}$. Proof sketch: near such a zero, $v$ is approximated by the linear map $Dv_p$, and a linear isomorphism $L : \mathbb{R}^n \to \mathbb{R}^n$ has degree $\mathrm{sign}(\det L)$.

**Corollary (Morse-theoretic interpretation).** If $v = \nabla h$ for a Morse function $h : M \to \mathbb{R}$, then at each critical point $p$ the index is $(-1)^{m_p}$, where $m_p$ is the Morse index (number of negative eigenvalues of $\mathrm{Hess}(h)_p$). Maximum: index $(-1)^n$. Minimum: index $+1$. Saddle: $(-1)$ for each "saddle direction".

**Corollary (additivity under splitting).** If a single degenerate zero is perturbed slightly into several non-degenerate zeros, the algebraic sum of their indices equals the index of the original. The total index is stable under deformation. This is what makes the [[Thm - Poincare-Hopf Theorem|Poincaré-Hopf theorem]] possible: $\sum j_v(p)$ depends only on the field's *homotopy class* among fields with isolated zeros, and is independent of the field itself.

**Calibration check.** (1) For the saddle $v = (x, -y)$, count: at $(1, 0)$, $v$ points right; at $(0, 1)$, $v$ points down. The rotation from right to down going counterclockwise (i.e., from $(1, 0)$ to $(0, 1)$, a $90°$ counterclockwise step) is $90°$ *clockwise*. Total around the circle: $360°$ clockwise, i.e. index $-1$. (2) Find a field on $S^2$ with two zeros each of index $+1$ — answer: $\partial/\partial\theta$ (lines of longitude). (3) Find one with a single zero of index $+2$ — answer: the stereographic-projection field above.

---

# Unlocked by This

> [!tip] Brouwer Degree as a Universal Tool *(from Topology and Analysis)*
> The Brouwer degree, of which the index is one of the simplest instances, is the universal tool for converting topological questions into algebraic ones. Applications: **proving the fundamental theorem of algebra** (every non-constant polynomial $p(z) : \mathbb{C} \to \mathbb{C}$ has degree equal to its algebraic degree, so it covers every value exactly that many times — including $0$); **Brouwer fixed-point theorem** (any continuous map $f : D^n \to D^n$ has a fixed point, because the degree-counting of $f(x) - x$ forces a zero); the **Leray-Schauder degree** in infinite dimensions, which underlies modern PDE existence theory (Schauder fixed-point, monotone operator methods).

> [!tip] Euler Class as the Universal Source of Indices *(from Algebraic Topology)*
> The collection of vector-field indices on a closed manifold sum to the **Euler class** $e(TM) \in H^n(M, \mathbb{Z})$ evaluated on the fundamental class — which equals $\chi(M)$. The Euler class is one of the basic [[Algebraic Topology III — Higher Homotopy and Chern Forms|characteristic classes]], a topological invariant attached to every oriented vector bundle. For complex line bundles the Euler class equals the first **Chern class** (under the identification of complex line bundles with oriented real 2-plane bundles). Indices of sections of $E$ are thus a unified topological notion across all bundles, and the local-to-global theorem (sum of indices = topological invariant) generalizes Poincaré-Hopf to every oriented vector bundle.
