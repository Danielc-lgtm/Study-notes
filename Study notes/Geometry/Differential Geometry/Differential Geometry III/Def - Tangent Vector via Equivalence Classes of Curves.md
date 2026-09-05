---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Tangent Space"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a [[Def - Smooth Manifold|smooth manifold]], $p \in M$. A **smooth curve through $p$** is a smooth map $\gamma : J \to M$ where $J$ is an open interval containing $0$ and $\gamma(0) = p$. We write $V_{p}M$ for the set of equivalence classes of such curves under the equivalence relation defined below. Smooth functions on $M$ are denoted $f, g \in C^{\infty}(M)$. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

The idea is geometrically immediate: a **tangent vector at $p$ should be the velocity of a curve through $p$**. Take a smooth curve $\gamma$ with $\gamma(0) = p$, and think of $\gamma'(0)$ as "the direction and speed at which $\gamma$ leaves $p$". This is the picture from one-variable calculus: the velocity of a particle moving along $\gamma$ at the moment it passes through $p$.

The wrinkle is that *many different curves have the same velocity at $p$*. The curves $\gamma_{1}(t) = (t, 0)$ and $\gamma_{2}(t) = (t, t^{2})$ both pass through the origin of $\mathbb{R}^{2}$ at $t = 0$ with velocity $(1, 0)$; the curves $\gamma_{1}(t) = (t, 0)$ and $\gamma_{3}(t) = (\sin t, 0)$ also have the same velocity at $t = 0$. So a tangent vector is not "a curve" but "an equivalence class of curves that share the same velocity at $p$".

How do we *define* "having the same velocity" without already having tangent vectors? Use the algebra of smooth functions. Two curves $\gamma_{1}, \gamma_{2}$ through $p$ "have the same velocity" if, for every smooth $f$ defined near $p$, the rates of change $(f \circ \gamma_{1})'(0)$ and $(f \circ \gamma_{2})'(0)$ agree. Geometrically: every smooth function reads the two curves as having the same instantaneous rate of change at $p$. This is the equivalence relation that defines $V_{p}M$.

Why is this the right equivalence? Because it captures *all and only* the first-order information of the curve at $p$. Two curves with the same chart components and the same first derivatives in some chart at $p$ will satisfy the equivalence (chain rule gives matching $(f \circ \gamma)'(0)$ for any smooth $f$), and two curves that satisfy the equivalence must have the same first derivatives in *every* chart (test with the coordinate functions $f = x^{i}$). So the equivalence captures the chart-component velocity in a chart-independent way.

Why quantify over *all* smooth functions $f$? It makes the definition intrinsic, without selecting a chart. For computation, however, one chart is enough: equality of the $n$ coordinate derivatives implies equality after every smooth test function by the Euclidean chain rule, and then implies equality in every other chart by applying the chain rule to the transition map. Thus “all smooth functions” is the coordinate-free definition, while “the coordinate velocities agree in one—and hence every—chart” is the finite operational test.

The deepest reason this definition works is that **the equivalence relation $\gamma_{1} \sim \gamma_{2}$ if and only if $(f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0)$ for all $f$** is exactly the relation "$\gamma_{1}$ and $\gamma_{2}$ induce the same derivation at $p$". Two curves give the same derivation precisely when they give the same first-order action on every smooth function. So the equivalence-class-of-curves definition is set up to be in canonical bijection with the derivation definition — and that bijection is the content of [[Thm - Equivalence of Tangent Vector Definitions]].

What this definition *gains* over the derivation definition is geometric intuition: it makes the picture of "tangent vector = velocity" the formal definition, not an interpretation. What it *loses* is the obvious vector-space structure: how do you add two equivalence classes of curves? The answer requires choosing a chart, adding components, and showing the answer is independent of the choice — work that is invisible in the derivation picture. So the curve picture is geometrically preferred for *intuition* and the derivation picture is algebraically preferred for *proofs*.

The curve picture is also what one uses in *concrete computations* of $dF_{p}(v)$. By Corollary 3.25 (Lee), $dF_{p}(v) = (F \circ \gamma)'(0)$ for any curve $\gamma$ realizing $v$. This makes the curve definition the operational version of the differential.

A reader who has never seen this definition could invent it by the following route. Want to define "tangent vector at $p$" geometrically. Notice tangent vectors should be velocities. Notice many curves can share a velocity. Define "shared velocity" using smooth-function rates of change. Take equivalence classes. The crucial step is the trust that this geometric definition can be made vector-space-respecting (it can, but the proof requires the equivalence with derivations).

---

# The Definition

Let $M$ be a smooth manifold and $p \in M$. Let $\mathcal{C}_{p}$ denote the set of all smooth curves $\gamma : J \to M$ with $0 \in J$ an open interval and $\gamma(0) = p$.

Define a relation $\sim$ on $\mathcal{C}_{p}$ by
$$\gamma_{1} \sim \gamma_{2} \iff (f \circ \gamma_{1})'(0) = (f \circ \gamma_{2})'(0) \;\text{ for every smooth real-valued function } f \text{ defined in a neighbourhood of } p.$$

This is an equivalence relation (reflexivity, symmetry, and transitivity are immediate). The **set of tangent vectors at $p$ in the curve picture** is
$$V_{p}M \;=\; \mathcal{C}_{p}/\!\sim,$$
and an element $[\gamma] \in V_{p}M$ is called a **tangent vector at $p$**.

**The bijection with derivations.** The map $V_{p}M \to T_{p}M$ sending $[\gamma]$ to the derivation $v_{\gamma}$ defined by $v_{\gamma}(f) = (f \circ \gamma)'(0)$ is a well-defined bijection — and it carries the vector-space structure on $T_{p}M$ back to $V_{p}M$ via this identification. This is the content of [[Thm - Equivalence of Tangent Vector Definitions]].

**Equivalent characterization in coordinates.** Given a chart $(U, \varphi)$ around $p$, two curves $\gamma_{1}, \gamma_{2}$ through $p$ are equivalent if and only if $(\varphi \circ \gamma_{1})'(0) = (\varphi \circ \gamma_{2})'(0)$ — that is, their coordinate representatives have the same velocity at $t = 0$. So in a chart, the curve definition reduces to the familiar Euclidean velocity.

---

# Relate to Other Fields / Compression

This definition is the manifold version of the **Newton picture of velocity**: a particle traversing a curve has, at each instant, a velocity that captures its first-order motion. The complication on a manifold is that velocities at different points live in different spaces, with no canonical way to compare them without further structure (a connection).

In [[Def - The Tangent Space to a Submanifold|Euclidean submanifold theory]], the curve definition is the *primary* definition of $T_{p}M$: a tangent vector to $M \subseteq \mathbb{R}^{N}$ at $p$ is any vector $\tau \in \mathbb{R}^{N}$ of the form $\gamma'(0)$ for a curve $\gamma$ in $M$ with $\gamma(0) = p$. The equivalence relation is collapsed because two curves with the same Euclidean velocity at $p$ automatically agree on every $f$ (the velocity *is* the vector). The abstract-manifold version needs the equivalence relation precisely because there is no ambient $\mathbb{R}^{N}$ in which to compare velocity vectors.

**True name:** The curve picture is the **true name** of a tangent vector. The derivation picture is a clean re-encoding of "what a velocity does to functions"; the chart-tuple picture is a chart-dependent realization. But the *thing* a tangent vector is, geometrically, is the velocity of a curve. Lee acknowledges this when he writes (p. 54) "your intuition should be guided as much as possible by the geometric picture" — and the geometric picture is the curve picture.

In **classical mechanics**, the configuration manifold $Q$ of a mechanical system has a tangent bundle $TQ$ whose elements are *velocities* — the natural setting for Lagrangian mechanics. Newton's second law $F = ma$ becomes a statement about the time derivative of a curve in $Q$, and the kinetic energy is a quadratic form on tangent vectors. The curve definition of tangent vector is, in this context, the *only* natural definition — derivations would be an unnecessary detour.

---

# Examples / Corollaries

**Velocity of a straight line in $\mathbb{R}^{n}$.** The curve $\gamma(t) = a + tv$ in $\mathbb{R}^{n}$ has velocity class $[\gamma]$ corresponding to the derivation $D_{v}|_{a}$, i.e., the geometric vector $v$ at $a$. This is the cleanest example — and the equivalence class is large: any reparametrization or higher-order perturbation of $\gamma$ that has the same first-derivative at $0$ is in the same class.

**A constant curve has zero velocity.** The constant curve $\gamma(t) \equiv p$ has $(f \circ \gamma)(t) = f(p)$ for every $f$, so $(f \circ \gamma)'(0) = 0$ for every $f$. Hence $[\gamma]$ is the zero element of $V_{p}M$, corresponding to the zero derivation. The corresponding derivation $v_{\gamma} \equiv 0$ takes every function to zero.

**Two curves through the origin of $\mathbb{R}^{2}$ with the same velocity.** $\gamma_{1}(t) = (t, 0)$ and $\gamma_{2}(t) = (t, t^{3})$ both have $\gamma_{i}(0) = (0, 0)$. For any smooth $f$, $(f \circ \gamma_{1})'(0) = \partial_{1} f(0,0)$ and $(f \circ \gamma_{2})'(0) = \partial_{1} f(0,0) + 3 \cdot 0^{2} \cdot \partial_{2} f(0,0) = \partial_{1} f(0,0)$. So $\gamma_{1} \sim \gamma_{2}$ even though $\gamma_{2}$ has a cubic deviation from the $x$-axis — the *cubic* deviation has zero first-derivative at $t = 0$, hence does not affect the velocity.

**Two curves with the same image but different velocities.** $\gamma_{1}(t) = (t, 0)$ and $\gamma_{2}(t) = (2t, 0)$ both trace the $x$-axis of $\mathbb{R}^{2}$ near the origin. Yet $(f \circ \gamma_{1})'(0) = \partial_{1} f$ while $(f \circ \gamma_{2})'(0) = 2\,\partial_{1} f$. So the two curves have *different* tangent vectors at the origin — the second is twice as fast. The same image, traversed at different speeds, gives different tangent vectors. This is the principle that tangent vectors carry *speed* as well as direction.

**Is NOT a single tangent vector: a curve with a corner.** The curve $\gamma(t) = (|t|, 0)$ on $\mathbb{R}^{2}$ is not smooth at $t = 0$, so it does not belong to $\mathcal{C}_{p}$ at all. The definition restricts to smooth curves precisely so that $(f \circ \gamma)'(0)$ is unambiguously defined.

**Corollary — the velocity map is surjective.** Every tangent vector $v \in T_{p}M$ is the velocity of *some* smooth curve through $p$. To see this, pick a chart $(U, \varphi)$ around $p$ and write $v = v^{i}\,\partial/\partial x^{i}|_{p}$ in the coordinate basis. Then the curve $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ has $\gamma(0) = p$ and $\gamma'(0) = v$. This was proved as Proposition 3.23 in Lee. So the map $V_{p}M \to T_{p}M$ is surjective, and (with injectivity from the definition of $\sim$) a bijection.

**Corollary — pre-composition with $F$ is well-defined on equivalence classes.** For a smooth map $F : M \to N$ and $[\gamma] \in V_{p}M$, the composition $F \circ \gamma$ is a smooth curve in $N$ through $F(p)$. The equivalence class $[F \circ \gamma]$ depends only on $[\gamma]$: if $\gamma_{1} \sim \gamma_{2}$ then for every $g \in C^{\infty}(N)$, $(g \circ F \circ \gamma_{1})'(0) = (g \circ F \circ \gamma_{2})'(0)$ because $g \circ F \in C^{\infty}(M)$ is smooth and the equivalence $\gamma_{1} \sim \gamma_{2}$ is tested against all such smooth functions. So $dF_{p}([\gamma]) := [F \circ \gamma]$ is a well-defined map $V_{p}M \to V_{F(p)}N$, which is the *curve-picture definition* of the differential.

**Calibration check.** Verify that $\gamma_{1}(t) = (t, 0)$ and $\gamma_{2}(t) = (\sin t, 0)$ define the same tangent vector at the origin of $\mathbb{R}^{2}$. Verify that the velocity class of a constant curve is the zero tangent vector. Verify that for a chart $(U, \varphi)$ and $v \in \mathbb{R}^{n}$, the curve $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ has velocity class corresponding to the derivation $v^{i}\,\partial/\partial x^{i}|_{p}$. If you can also explain why the equivalence relation must use *all* smooth functions, not just coordinate functions, you have understood the chart-independence of the definition.

---

# Unlocked by This

> [!tip] The Differential via Curves *(from Differential Geometry)*
> The cleanest definition of $dF_{p}$ in the curve picture is simply $dF_{p}([\gamma]) = [F \circ \gamma]$ — pre-compose the curve with $F$. This is geometrically transparent: the differential pushes a curve forward. The corresponding statement in the derivation picture is $(dF_{p}(v))(f) = v(f \circ F)$, which is the same thing read through the derivation/curve isomorphism. See [[Def - The Differential of a Smooth Map]].

> [!tip] Velocity of a Curve *(from Differential Geometry)*
> The velocity of a smooth curve $\gamma$ at $t_{0}$ is precisely the tangent vector $[\gamma_{t_{0}}]$ where $\gamma_{t_{0}}(t) = \gamma(t_{0} + t)$ — the shifted-and-restarted version of $\gamma$. See [[Def - Velocity of a Curve]].

> [!tip] Lagrangian Mechanics *(from Classical Mechanics)*
> A **Lagrangian** is a smooth function $L : TQ \to \mathbb{R}$ on the tangent bundle of the configuration manifold $Q$. The Euler–Lagrange equations are second-order ODEs whose solutions are curves $q : J \to Q$ satisfying $L_{q}(q(t), \dot q(t))$ being stationary along variations. The whole formalism uses the curve picture of tangent vectors: $\dot q(t)$ is a velocity in $T_{q(t)}Q$, and the action is an integral of $L(q, \dot q)$ along the curve. Without the curve picture, this would be unnatural to state.
