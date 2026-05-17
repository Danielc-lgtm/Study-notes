---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Vector"
  - "Def - Minkowski Space and the Metric"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. A four-vector is $X$ with components $X^\mu = (X^0, X^1, X^2, X^3)$, $X^0$ the time component. The metric is $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$; the norm-squared is $X\cdot X = \eta_{\mu\nu}X^\mu X^\nu = (X^0)^2 - |\mathbf{X}|^2$, where $\mathbf{X} = (X^1,X^2,X^3)$ is the spatial part and $|\mathbf{X}|^2 = (X^1)^2+(X^2)^2+(X^3)^2$. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

A [[Def - Four-Vector|four-vector]]'s components are frame-dependent — a boost scrambles them. But its norm-squared $X\cdot X$ is a Lorentz *invariant*; every observer computes the same value. The question this definition answers is: what does that one invariant number tell us, and how should we organise four-vectors according to it?

In Euclidean geometry the analogous invariant — the squared length $|\mathbf{X}|^2$ — carries little structural information: it is always $\ge 0$, zero only for the zero vector, and "classifying vectors by the sign of their length" would be vacuous. The Minkowski norm is different precisely because the metric is **indefinite**: $X\cdot X$ can be positive, negative, or zero. The sign is a genuine three-way choice, and since the sign is Lorentz invariant, it is a *frame-independent, intrinsic attribute* of the four-vector. That is the raw material for a meaningful classification, and the desideratum is to read off what each sign means physically.

The meaning comes from the [[Def - The Spacetime Interval|interval]]. For a displacement four-vector $X$ between two events, $X\cdot X = \Delta t^2 - |\Delta\mathbf{x}|^2$. If $X\cdot X > 0$ the events are closer in space than in time — a particle slower than light can be at both, so they are *causally connectible*. If $X\cdot X < 0$ they are closer in time than in space — no signal at or below $c$ joins them, so they are *causally disconnected*. If $X\cdot X = 0$ they sit on a light ray. So the sign of the norm is nothing less than the *causal relationship* between the events, and the classification is the causal structure of spacetime made into a definition.

A second invariant emerges for the non-spacelike vectors. For timelike and null $X$, the *sign of the time component* $X^0$ is also Lorentz invariant — a boost cannot flip a future-pointing timelike vector to past-pointing (a boost would have to be superluminal to do so). This gives a finer split, future-pointing versus past-pointing, which is what makes "cause precedes effect" a frame-independent statement and protects causality. For *spacelike* vectors, by contrast, $\mathrm{sign}(X^0)$ is *not* invariant — a boost can reverse it — which is the precise reason the time-order of spacelike-separated events depends on the frame ([[Ex - The relativity of simultaneity]]).

Why classify by the sign of the *norm* and not, say, by the size of the components? Because the components are frame-dependent and carry no invariant content on their own, while the norm's sign is intrinsic. The classification works *because* it is built from an invariant — and it would be impossible in a positive-definite geometry, where the norm has no sign to speak of. The trichotomy is the indefiniteness of the metric, cashed out.

---

# The Definition

Let $X$ be a nonzero [[Def - Four-Vector|four-vector]] with norm-squared $X\cdot X = \eta_{\mu\nu}X^\mu X^\nu = (X^0)^2 - |\mathbf{X}|^2$. Then $X$ is:

$$
\boxed{\;
\begin{aligned}
&\textbf{timelike} && \text{if } X\cdot X > 0 && (\text{"more time than space"}),\\
&\textbf{spacelike} && \text{if } X\cdot X < 0 && (\text{"more space than time"}),\\
&\textbf{null (lightlike)} && \text{if } X\cdot X = 0, \ X \ne 0 && (\text{"light-like"}).
\end{aligned}
\;}
$$

(Under the opposite "mostly plus" signature the inequalities for timelike and spacelike are reversed; the classification itself is convention-independent.) Because $X\cdot X$ is **Lorentz invariant**, the class of $X$ is the **same in every inertial frame** — it is an intrinsic, frame-independent property.

**Time orientation.** For a *timelike or null* four-vector, the sign of the time component $X^0$ is also Lorentz invariant (under proper orthochronous transformations). Such a vector is:
$$
\textbf{future-pointing} \ \text{ if } X^0 > 0, \qquad
\textbf{past-pointing} \ \text{ if } X^0 < 0.
$$
For a *spacelike* four-vector, $\mathrm{sign}(X^0)$ is **not** invariant — a boost can reverse it — so future/past is not defined for spacelike vectors.

**The light cone.** Fixing an event as origin, the null four-vectors form the **light cone**, the double cone $(X^0)^2 = |\mathbf{X}|^2$. It has two sheets: the **future light cone** ($X^0 > 0$) and the **past light cone** ($X^0 < 0$), meeting at the apex. Timelike vectors lie *inside* the cone, spacelike vectors *outside* it. For displacement vectors, the cone separates the events causally connectible to the origin (inside) from those that are not (outside).

The same three words classify the **separation** between two events (via the displacement four-vector) and a **worldline** (timelike if its tangent is everywhere timelike — the only physically allowed kind for a massive particle; null for a light ray).

---

# Relate to Other Fields / Compression

The classification has no Euclidean analogue, and that absence is informative. In Euclidean space the norm-squared is positive definite, so every nonzero vector is "spacelike" in the trivial sense — there is one class, no structure. The trichotomy exists *only* because the Minkowski metric is indefinite, and it is the cleanest single illustration of what indefiniteness buys.

The closest mathematical relative is the classification of points relative to a quadric. The light cone is the zero set of the quadratic form $\eta(X,X)$; timelike and spacelike vectors are the two "sides" of this quadric, the regions where the form is positive and negative. This is the same picture as the interior and exterior of a conic in projective geometry, or the classification of a real symmetric matrix's vectors by the sign of the associated quadratic form. The novelty in relativity is the *physical* reading: the two sides of the cone are not just algebraic regions but the causally-connected and causally-disconnected parts of spacetime.

In the theory of partial differential equations the same word "timelike/spacelike" classifies surfaces and directions for a hyperbolic equation — the wave equation $\partial_t^2 u = \nabla^2 u$ has exactly the Minkowski light cone as its characteristic cone, and "domain of dependence" is the timelike-past region. The causal structure of relativity is the characteristic structure of the wave equation.

---

# Examples / Corollaries

**Is an instance — a timelike vector.** $X = (2, 1, 0, 0)$ has $X\cdot X = 4 - 1 = 3 > 0$: timelike, and future-pointing since $X^0 = 2 > 0$. The displacement between "a clock here now" and "the same clock later" is timelike — a worldline of a massive particle has timelike tangent everywhere.

**Is an instance — a spacelike vector.** $X = (1, 2, 0, 0)$ has $X\cdot X = 1 - 4 = -3 < 0$: spacelike. The displacement between the two ends of a rod *at one instant* is spacelike (in [[Ex - Length contraction]], the simultaneous endpoints had $\Delta s^2 = -L^2$). No signal connects spacelike-separated events.

**Is an instance — a null vector.** $X = (1, 1, 0, 0)$ has $X\cdot X = 1 - 1 = 0$, yet $X \ne 0$: null. The displacement between emission and absorption of a photon is null; a light ray's tangent is null everywhere. A null vector is nonzero with zero norm — impossible in Euclidean geometry, routine here.

**Is NOT an instance of "future-pointing is frame-independent" — a spacelike vector.** Take the spacelike $X = (1,2,0,0)$, with $X^0 = 1 > 0$. A boost with $v > 1/2$ sends $X^0 \to \gamma(X^0 - vX^1) = \gamma(1 - 2v) < 0$. The time component flipped sign. So "future-pointing" is *meaningless* for spacelike vectors — exactly why two observers can disagree on which of two spacelike-separated events came first.

**Corollary — the class is the same in every frame.** Since $X\cdot X$ is invariant, a timelike vector is timelike for all observers, a null vector null for all, a spacelike vector spacelike for all. All observers agree on the causal classification, even while disagreeing on the components and (for spacelike vectors) on the time order.

**Corollary — a massive particle's worldline is timelike; a light ray's is null.** A massive particle moves slower than light, so over any segment $|\Delta\mathbf{x}| < \Delta t$ and the tangent has $X\cdot X > 0$. Light moves at $c$, so $|\Delta\mathbf{x}| = \Delta t$ and the tangent is null. A *spacelike* worldline would describe faster-than-light motion — forbidden, because it would let causes and effects be reordered ([[Ex - Causal structure and the light cone]]).

**Corollary — sum of two future-pointing timelike vectors is future-pointing timelike.** This is not obvious and is proved in [[Thm - The Reversed Triangle Inequality]]; it is what makes the future-pointing timelike vectors a *cone* closed under addition, the geometric home of the reversed triangle inequality and the twin paradox.

---

# Unlocked by This

> [!tip] The Reversed Triangle Inequality *(from §1.3)*
> The future-pointing timelike four-vectors form a convex cone, and on it the Euclidean triangle inequality *reverses* ([[Thm - The Reversed Triangle Inequality]]): the straight worldline has the *longest* proper time. This is the geometry behind the [[Ex - The twin paradox|twin paradox]].

> [!tip] The Causal Structure of Spacetime *(from General Relativity)*
> The light cone at each event, and the timelike/spacelike split, generalise to the **causal structure** of a curved spacetime — the foundation of the singularity theorems, black-hole event horizons, and the global geometry of general relativity.

> [!tip] Classification of Four-Momenta *(from Relativistic Kinematics)*
> A massive particle's [[Def - Four-Momentum and Rest Mass|four-momentum]] is future-pointing timelike ($P\cdot P = m^2 > 0$); a photon's is future-pointing null ($P\cdot P = 0$). The classification of four-vectors becomes the distinction between massive and massless particles.
