---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - The Riemannian Exponential Map"
  - "Def - Geodesic"
  - "Def - Jacobi Field"
tags: [geometry, riemannian-geometry, exponential-map, gauss-lemma]
---

# Notation

$(M, g)$ a Riemannian manifold, $p \in M$, $\exp_p : V_p \subseteq T_pM \to M$ the [[Def - The Riemannian Exponential Map|exponential map]]. For $v \in T_pM$ with $\exp_p$ defined near $v$, $d(\exp_p)_v : T_v(T_pM) = T_pM \to T_{\exp_p(v)}M$ is its differential. We use the canonical identification $T_v(T_pM) \cong T_pM$ throughout. The geodesic sphere of radius $r$ at $p$ is $S_r(p) := \exp_p(\{w \in T_pM : g_p(w, w) = r^2\})$, defined when $r < \mathrm{inj}_g(p)$. Full registry on [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (Gauss Lemma).** Let $(M, g)$ be a Riemannian manifold, $p \in M$, and $v \in V_p \subseteq T_pM$. For any $w \in T_pM$, decomposing $w = w^\parallel + w^\perp$ with $w^\parallel$ parallel to $v$ and $w^\perp$ orthogonal to $v$ (with respect to $g_p$),
> $$g_{\exp_p(v)}\bigl(d(\exp_p)_v(w^\parallel),\ d(\exp_p)_v(w^\perp)\bigr) = 0.$$
> Equivalently: $d(\exp_p)_v$ preserves the orthogonality between the radial direction (the line $\mathbb{R} v$) and its orthogonal complement.

> **Corollary (geodesic polar form of the metric).** In geodesic polar coordinates $(r, \omega) \in (0, \mathrm{inj}_g(p)) \times S^{n-1}$ at $p$, the metric takes the form
> $$g = dr^2 + h(r, \omega),$$
> where $h(r, \omega)$ is a Riemannian metric on the geodesic sphere of radius $r$, with no $dr\, d\omega$ cross-terms.

> **Corollary (local length-minimisation).** For $r < \mathrm{inj}_g(p)$, the radial geodesic from $p$ to $\exp_p(rv)$ (with $|v| = 1$) is the unique length-minimising curve between these points; its length is exactly $r$.

---

# Motivation

This is the technical workhorse of local Riemannian geometry. It says that the exponential map, even though it does not in general preserve the *full* metric (which would require flatness), *does* preserve one specific piece of metric structure: the orthogonality between the radial direction and the tangent direction to the geodesic sphere.

The reason this matters is that it is *exactly* the piece of structure needed to prove [[Def - Geodesic|geodesics]] are locally length-minimising. The intuition: in geodesic polar coordinates the metric has the form $dr^2 + h_{\alpha\beta}\, d\omega^\alpha d\omega^\beta$ — no cross-terms. So the length of any curve $\gamma(t) = (r(t), \omega(t))$ is
$$L(\gamma) = \int \sqrt{\dot r^2 + h_{\alpha\beta}(r, \omega)\dot\omega^\alpha \dot\omega^\beta}\, dt \geq \int |\dot r|\, dt \geq |\Delta r|,$$
the second inequality coming from $h_{\alpha\beta}\dot\omega^\alpha\dot\omega^\beta \geq 0$. So any curve from a point at radius $r_1$ to a point at radius $r_2$ has length at least $|r_2 - r_1|$, with equality iff $\dot\omega = 0$ throughout — i.e., iff the curve is a *radial geodesic*. So radial geodesics minimise length within the geodesic ball.

Without the Gauss lemma — if the metric in polar coordinates had cross-terms $g_{r\omega}\, dr\, d\omega$ — this length-minimisation argument would fail: a curve with $\dot\omega \neq 0$ could *cancel* the radial contribution against an angular one, and the length could be less than $|\Delta r|$. So the absence of cross-terms is exactly the structural fact that lets the local minimisation theorem go through.

The Gauss lemma is the precise place in the theory where the metric and the connection cooperate: the exponential map is built from the connection (via geodesics), and the lemma extracts a metric statement (orthogonality) from this connection-built construction. The cooperation works because the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]] is *metric-compatible* — parallel transport preserves inner products — and "geodesic = velocity is parallel-transported along itself" then makes the velocity preserve its inner product structure with orthogonal complement-fields.

Historically, Gauss proved this for surfaces in $\mathbb{R}^3$ (the local picture of any 2-dimensional Riemannian manifold), and it was the key step in his proof of the *Theorema Egregium* and his characterisation of intrinsic geometry. The generalisation to $n$ [[Def - Dimension|dimensions]] is straightforward but indispensable.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem is just "we have a Riemannian manifold, a point $p$, and the exponential map at $p$ defined near $v$". So sources here are recognising hidden uses of the lemma.

A common source is **any problem asking about radial geodesics and their orthogonality properties**. When the problem mentions "the geodesic from $p$ in direction $\omega$" and "the geodesic sphere", the Gauss lemma is the structural fact connecting them. Bridge: any problem with both radial geodesics and geodesic spheres has the Gauss lemma in the background, even when it is not explicitly named.

A subtler source is **a problem about the distance function $d_g(p, \cdot)$**. Inside the injectivity radius, $d_g(p, q) = r$ where $q = \exp_p(rv)$ for unit $v$. The gradient of $d_g(p, \cdot)$ is the radial unit vector $\partial_r$, and the Gauss lemma is what makes $|\nabla d_g(p, \cdot)| = 1$ (so $d_g(p, \cdot)$ is a *distance function* in the sense of having unit gradient). Bridge: a problem involving $\nabla d_g(p, \cdot)$, the eikonal equation, or the gradient flow of the distance function uses the Gauss lemma to control the angular direction.

A third source is **a problem about constant-speed geodesic variations**. A normal Jacobi field $J$ along a geodesic $\gamma$ from $p$ (with $J(0) = 0$) corresponds to $\dot\omega \neq 0$, and the Gauss lemma's orthogonality is what makes $J$ orthogonal to $\dot\gamma$ throughout — not just at the start.

**Targets (Output Amplification)**

The conclusion is the orthogonality $d(\exp_p)_v(v) \perp d(\exp_p)_v(w)$ for $w \perp v$. The targets are the constructions that use this.

The most important combination is **Gauss lemma + length functional ⟹ local length-minimisation**. With the orthogonality, the metric in polar coordinates has no cross-terms, and the length of any curve from $p$ to a point at radius $r$ is at least $r$ (the radial distance), with equality only for the radial geodesic. So *radial geodesics are length-minimising within the geodesic ball*. This is the local statement; combined with [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]] it upgrades to a global existence-of-minimisers result on complete manifolds.

A second combination is **Gauss lemma + the distance function ⟹ smoothness of $d_g(p, \cdot)$ within the injectivity radius**. Inside the injectivity radius, $d_g(p, q) = |\exp_p^{-1}(q)|$, a smooth function with unit gradient. The Gauss lemma is what gives the unit gradient. Beyond the injectivity radius (specifically at the cut locus), $d_g(p, \cdot)$ becomes non-smooth, and the structure of the failure is governed by conjugate points and the second variation.

A third combination is **Gauss lemma + the second variation formula ⟹ index form on normal variations is well-defined**. The index form is computed on *normal* variation fields along a geodesic, and the Gauss lemma is implicit in saying that variations from geodesics through $p$ (with vanishing initial value) are automatically orthogonal to the geodesic. Without it, the decomposition into tangential and normal variations would be more delicate.

---

# Why Is It True

**Mechanism summary:** **the differential of the exponential map sends the *radial* direction in $T_pM$ to the *tangent to the geodesic* in $TM$, which by the geodesic equation has constant norm and stays orthogonal to perpendicular Jacobi fields by metric compatibility — and Jacobi fields with $J(0) = 0$ are exactly the differential of $\exp_p$ on the orthogonal complement.**

Here is the intuition with all the moving parts in place.

The radial direction in $T_pM$ at the point $v$ is the line $\mathbb{R} v$ (the direction of $v$ itself). Under $d(\exp_p)_v$, this maps to the velocity of the geodesic $\gamma_v$ at time $1$: indeed, $d(\exp_p)_v(tv) = \frac{d}{ds}\big|_{s=0}\exp_p(v + s \cdot tv) =$ (some computation) $= t \dot\gamma_v(1)$.

The orthogonal direction in $T_pM$ — a vector $w \perp v$ — maps to the value at $t = 1$ of a Jacobi field. Specifically, $d(\exp_p)_v(w) = J(1)$ where $J$ is the Jacobi field along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$. This is the Jacobi-field identity stated in [[Def - Jacobi Field]].

So we need: $\langle \dot\gamma_v(1), J(1)\rangle = 0$ whenever $J$ is a Jacobi field with $J(0) = 0$ and $J'(0) \perp \dot\gamma_v(0) = v$.

Compute $\frac{d}{dt}\langle \dot\gamma, J\rangle$ using metric compatibility:
$$\frac{d}{dt}\langle \dot\gamma, J\rangle = \langle \nabla_{\dot\gamma}\dot\gamma, J\rangle + \langle \dot\gamma, J'\rangle = 0 + \langle \dot\gamma, J'\rangle,$$
because $\gamma$ is a geodesic. So $\frac{d}{dt}\langle \dot\gamma, J\rangle = \langle \dot\gamma, J'\rangle$.

Now differentiate again:
$$\frac{d^2}{dt^2}\langle \dot\gamma, J\rangle = \langle \nabla_{\dot\gamma}\dot\gamma, J'\rangle + \langle \dot\gamma, J''\rangle = \langle \dot\gamma, J''\rangle = -\langle \dot\gamma, R(J, \dot\gamma)\dot\gamma\rangle = 0,$$
using the Jacobi equation $J'' + R(J, \dot\gamma)\dot\gamma = 0$ and the *antisymmetry* of $R(\cdot, \cdot)Z$ in the first two arguments (so $R(\dot\gamma, J)\dot\gamma = -R(J, \dot\gamma)\dot\gamma$, but more directly, $\langle \dot\gamma, R(J, \dot\gamma)\dot\gamma\rangle =$ — well, this is $0$ because the (1,3)-curvature $R$ has the symmetry $g(R(X, Y)Z, W) = -g(R(X, Y)W, Z)$ from metric-compatibility, so with $X = J, Y = Z = W = \dot\gamma$, $g(R(J, \dot\gamma)\dot\gamma, \dot\gamma) = -g(R(J, \dot\gamma)\dot\gamma, \dot\gamma)$, hence $= 0$).

So $\langle \dot\gamma, J\rangle$ is a *linear* function of $t$, of the form $at + b$. The initial conditions: $\langle \dot\gamma(0), J(0)\rangle = \langle v, 0\rangle = 0$ (so $b = 0$), and $\frac{d}{dt}\langle \dot\gamma, J\rangle\big|_0 = \langle \dot\gamma(0), J'(0)\rangle = \langle v, w\rangle = 0$ (so $a = 0$, using the hypothesis $w \perp v$). Hence $\langle \dot\gamma(t), J(t)\rangle \equiv 0$ for all $t$, in particular at $t = 1$:
$$\langle d(\exp_p)_v(v), d(\exp_p)_v(w)\rangle = \langle \dot\gamma_v(1), J(1)\rangle = 0,$$
which is the Gauss lemma (up to a factor of $|v|$ on the radial direction, which we have suppressed).

So the lemma is a clean three-step calculation: differentiate the inner product, use the geodesic equation and the Jacobi equation, observe that the curvature symmetry kills the curvature contribution, integrate using the initial conditions. The orthogonality is preserved by parallel transport along the geodesic, which is the metric-compatibility of the connection.

---

# What Makes This Hard

The conceptual difficulty is **identifying $d(\exp_p)_v(w)$ with a Jacobi field**. Once this identification is made, the calculation is routine, but the identification itself is non-obvious — it requires writing $\exp_p$ as a time-$1$ flow and then differentiating in the *initial-velocity* direction, which produces a one-parameter family of geodesics whose variation is exactly the Jacobi field.

The technical difficulty is **separating the radial and orthogonal directions in $T_v(T_pM)$**. The space $T_v(T_pM)$ is canonically $T_pM$ via the linear structure, but it is natural to think of it as "directions of variation of $v$", and the splitting into "the direction of $v$ itself" (radial) and "the orthogonal directions" requires the metric $g_p$ — there is no canonical splitting without it.

The most common error is to forget the **antisymmetry of the curvature operator** in the calculation. Without this symmetry, $\langle \dot\gamma, R(J, \dot\gamma)\dot\gamma\rangle$ would not vanish, and the computation would not yield a linear function of $t$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Identify $d(\exp_p)_v(w)$ with the value at $t = 1$ of a Jacobi field along $\gamma_v$ with prescribed initial conditions. Compute the second derivative of $\langle \dot\gamma_v(t), J(t)\rangle$ in $t$; use the geodesic equation, the Jacobi equation, and the curvature antisymmetry to show it vanishes identically. Conclude that $\langle \dot\gamma_v(t), J(t)\rangle$ is linear in $t$, then use the initial conditions to show it equals zero.

**Subgoal decomposition:**

1. **Identify $d(\exp_p)_v(w)$ as a Jacobi field value.** Show that for $w \in T_pM$, $d(\exp_p)_v(w) = J(1)$ where $J$ is the Jacobi field along $\gamma_v$ with $J(0) = 0, J'(0) = w$.
   - *Hint:* differentiate $\exp_p(v + sw)$ in $s$ at $s = 0$; this produces the variation of the geodesic $\gamma_v$ through nearby geodesics with initial velocity $v + sw$, which is by definition a Jacobi field.
   - *Why needed:* Translates the differential statement into a statement about Jacobi fields, where the geodesic and Jacobi equations are available.

2. **Compute the second derivative of $\langle \dot\gamma_v, J\rangle$.** Show $\frac{d^2}{dt^2}\langle \dot\gamma_v(t), J(t)\rangle = -\langle \dot\gamma_v, R(J, \dot\gamma_v)\dot\gamma_v\rangle$, which vanishes by curvature symmetry.
   - *Hint:* differentiate once using metric compatibility and the geodesic equation; differentiate again using the Jacobi equation; use the symmetry $g(R(\cdot, \cdot)X, X) = 0$.
   - *Why needed:* This is the key calculation showing $\langle \dot\gamma_v, J\rangle$ is linear.

3. **Apply initial conditions.** $\langle \dot\gamma_v(0), J(0)\rangle = 0$ (since $J(0) = 0$) and $\frac{d}{dt}\langle \dot\gamma_v, J\rangle|_0 = \langle \dot\gamma_v(0), J'(0)\rangle = \langle v, w\rangle$.
   - *Hint:* substitute directly into the formulas from steps 1 and 2.
   - *Why needed:* Linear function vanishing at $t = 0$ with derivative $\langle v, w\rangle$ is $t \langle v, w\rangle$ — so it vanishes identically iff $\langle v, w\rangle = 0$, which is the hypothesis $w \perp v$.

4. **Conclude.** $\langle \dot\gamma_v(1), J(1)\rangle = 0$, which after the identifications of step 1 gives $\langle d(\exp_p)_v(v), d(\exp_p)_v(w)\rangle = 0$ (up to a factor for the radial direction).
   - *Hint:* $d(\exp_p)_v(v)$ is the velocity $\dot\gamma_v(1)$ (compute by homogeneity).
   - *Why needed:* This is the statement of the lemma.

---

# Lemma Decomposition

> [!note]- Lemma 1: $d(\exp_p)_v(w) = J(1)$ where $J$ is a Jacobi field
> **Statement:** Let $\exp_p$ be defined near $v \in T_pM$, and let $w \in T_pM$. Then $d(\exp_p)_v(w) = J(1)$, where $J$ is the Jacobi field along the geodesic $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$.
>
> **Hint:** Define a one-parameter family of geodesics by $\gamma_s(t) := \exp_p(t(v + sw))$, with $\gamma_0 = \gamma_v$. The variation field $J(t) = \partial_s|_{s=0} \gamma_s(t)$ is a Jacobi field by definition, with $J(0) = \partial_s|_0 p = 0$ and $J'(0) = w$. Evaluate at $t = 1$.
>
> **Why needed:** Reduces the differential of the exponential to a known object (Jacobi field), to which the Jacobi equation and metric-compatibility apply.
>
> > [!note]- Full proof
> > Define $\gamma_s(t) := \exp_p(t(v + sw))$. For each fixed $s$, $\gamma_s$ is the geodesic starting at $p$ with initial velocity $v + sw$ — so $\gamma_s$ is a geodesic for each $s$. The variation field $J(t) := \partial_s|_{s=0}\gamma_s(t)$ is therefore a Jacobi field along $\gamma_0 = \gamma_v$, by [[Def - Jacobi Field|the definition of Jacobi field as variation through geodesics]].
> >
> > Initial values: $J(0) = \partial_s|_{s=0}\gamma_s(0) = \partial_s|_{s=0}\exp_p(0) = \partial_s|_{s=0} p = 0$ and
> > $$J'(0) = \nabla_{\partial_t}\partial_s|_{s=0,t=0}\exp_p(t(v + sw)) = \nabla_{\partial_s}\partial_t|_{s=0,t=0}\exp_p(t(v+sw)) = \partial_s|_{s=0}(v + sw) = w$$
> > (using the swap of mixed covariant derivatives — which is fine here since $[\partial_s, \partial_t] = 0$ on the parameter space and torsion-freeness of $\nabla$).
> >
> > Evaluating at $t = 1$: $J(1) = \partial_s|_{s=0}\exp_p(v + sw) = d(\exp_p)_v(w)$.

> [!note]- Lemma 2: $\frac{d^2}{dt^2}\langle \dot\gamma_v(t), J(t)\rangle = 0$
> **Statement:** For any Jacobi field $J$ along a geodesic $\gamma$ with velocity $T$, $\frac{d^2}{dt^2}\langle T, J\rangle = 0$. So $\langle T, J\rangle$ is linear in $t$.
>
> **Hint:** Differentiate using metric compatibility and $\nabla_T T = 0$; differentiate again using the Jacobi equation $J'' + R(J, T)T = 0$ and the curvature symmetry $\langle R(\cdot, \cdot)T, T\rangle \equiv 0$.
>
> **Why needed:** This is the key computational step — without it, the orthogonality would have to be checked separately at every $t$.
>
> > [!note]- Full proof
> > By metric compatibility and $\nabla_T T = 0$ (geodesic equation),
> > $$\frac{d}{dt}\langle T, J\rangle = \langle \nabla_T T, J\rangle + \langle T, \nabla_T J\rangle = 0 + \langle T, J'\rangle = \langle T, J'\rangle.$$
> > Differentiating again:
> > $$\frac{d^2}{dt^2}\langle T, J\rangle = \frac{d}{dt}\langle T, J'\rangle = \langle \nabla_T T, J'\rangle + \langle T, J''\rangle = \langle T, J''\rangle.$$
> > By the Jacobi equation, $J'' = -R(J, T)T$. So $\frac{d^2}{dt^2}\langle T, J\rangle = -\langle T, R(J, T)T\rangle$.
> >
> > The curvature symmetry $g(R(X, Y)Z, W) = -g(R(X, Y)W, Z)$ (metric compatibility of $\nabla$, applied to the definition of $R$) gives, with $X = J, Y = T, Z = T, W = T$: $\langle R(J, T)T, T\rangle = -\langle R(J, T)T, T\rangle$, so $\langle R(J, T)T, T\rangle = 0$. Hence $\frac{d^2}{dt^2}\langle T, J\rangle = 0$, so $\langle T, J\rangle$ is linear in $t$.

> [!note]- Lemma 3: Initial conditions kill the linear function
> **Statement:** If $J$ is the Jacobi field with $J(0) = 0$ and $J'(0) = w \perp v$, then $\langle T(0), J(0)\rangle = 0$ and $\frac{d}{dt}\langle T, J\rangle|_0 = 0$. Hence $\langle T(t), J(t)\rangle \equiv 0$ for all $t$ where $\gamma_v$ is defined.
>
> **Hint:** Substitute $J(0) = 0$ for the first; substitute $J'(0) = w$ and $T(0) = v$ for the second, using $\langle v, w\rangle = 0$ (the orthogonality hypothesis).
>
> **Why needed:** A linear function vanishing at $t = 0$ with derivative $0$ at $t = 0$ is identically zero.
>
> > [!note]- Full proof
> > $\langle T(0), J(0)\rangle = \langle v, 0\rangle = 0$ — initial value of the linear function is zero.
> >
> > $\frac{d}{dt}\langle T, J\rangle|_{t=0} = \langle T(0), J'(0)\rangle = \langle v, w\rangle = 0$ by the orthogonality hypothesis.
> >
> > Since $\langle T, J\rangle$ is linear in $t$ (Lemma 2) and equals zero with zero derivative at $t = 0$, it is identically zero for all $t$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $v \in V_p \subseteq T_pM$ and $w \in T_pM$ with $w \perp v$ (orthogonality in $g_p$). Then
> $$g_{\exp_p(v)}(d(\exp_p)_v(v), d(\exp_p)_v(w)) = 0.$$
>
> *Proof.* By Lemma 1, $d(\exp_p)_v(w) = J(1)$, where $J$ is the Jacobi field along $\gamma_v$ with $J(0) = 0, J'(0) = w$.
>
> By the homogeneity property of the exponential map (Lemma 4 of [[Thm - Existence and Uniqueness of Geodesics]]), $\exp_p(tv) = \gamma_v(t)$, so $d(\exp_p)_v(v) = \frac{d}{dt}\big|_{t=1}\exp_p(tv) = \dot\gamma_v(1) = T(1)$ (writing $T := \dot\gamma_v$).
>
> So the quantity to compute is $\langle T(1), J(1)\rangle$.
>
> By Lemma 2, $\langle T(t), J(t)\rangle$ is linear in $t$. By Lemma 3, the linear function vanishes (initial value $0$ and initial derivative $0$). So $\langle T(1), J(1)\rangle = 0$, which gives
> $$\langle d(\exp_p)_v(v), d(\exp_p)_v(w)\rangle = 0. \qquad\blacksquare$$
>
> **Corollary (polar form of the metric).** In geodesic polar coordinates $(r, \omega)$ at $p$, with $r \in (0, \mathrm{inj}_g(p))$ and $\omega \in S^{n-1}$, the coordinate vector fields $\partial_r$ and $\partial_{\omega^\alpha}$ are pushed forward from $v/|v|$ (radial) and $w \perp v$ (angular) by $d\exp_p$. The Gauss lemma states $g(\partial_r, \partial_{\omega^\alpha}) = 0$, so the metric has no $dr\, d\omega$ cross-terms.
>
> $\langle \partial_r, \partial_r\rangle = 1$ because the radial geodesic has unit speed (by homogeneity, geodesics parametrised by the radial coordinate $r$ are unit-speed). The angular part is some metric $h_{\alpha\beta}(r, \omega)$ on the geodesic sphere. So $g = dr^2 + h_{\alpha\beta}(r, \omega)\, d\omega^\alpha d\omega^\beta$.
>
> **Corollary (local length-minimisation).** A curve $\gamma(t) = (r(t), \omega(t))$ from $(r_0, \omega_0)$ to $(r_1, \omega_1)$ with $r_0 < r_1 < \mathrm{inj}_g(p)$ has length
> $$L(\gamma) = \int \sqrt{\dot r^2 + h_{\alpha\beta}\dot\omega^\alpha \dot\omega^\beta}\, dt \geq \int |\dot r|\, dt \geq r_1 - r_0,$$
> with equality iff $\dot\omega \equiv 0$ throughout (which by the metric form gives a unit-speed parametrisation of the radial geodesic from $r_0$ to $r_1$).

---

# Cross-Field Exercise Suggestions

**Surface theory: Theorema Egregium for surfaces in $\mathbb{R}^3$.** The original Gauss lemma was proved for surfaces in $\mathbb{R}^3$ and was the key step in Gauss's proof of the **Theorema Egregium** — the Gaussian curvature of a surface is intrinsic, independent of the embedding. The lemma underlies the development of geodesic polar coordinates on surfaces, which are the natural setting in which $K$ appears as $-\frac{1}{\sqrt h}\partial_r^2 \sqrt h$ for the polar metric $g = dr^2 + h\, d\omega^2$.

**PDE: the eikonal equation.** The distance function $u(q) := d_g(p, q)$ satisfies the **eikonal equation** $|\nabla u|^2 = 1$ wherever it is smooth (inside the injectivity radius). The Gauss lemma is exactly what makes this true: $\nabla u = \partial_r$ has $|\partial_r|^2 = 1$, hence the eikonal equation. The eikonal equation is the prototype of Hamilton–Jacobi PDEs, and viscosity solutions, the method of characteristics, and the analysis of singular sets (cut locus) all interact with this setup.

**Optimal transport: cost functions and $c$-convexity.** In optimal transport on Riemannian manifolds, the cost function $c(x, y) = d_g(x, y)^2/2$ has properties (regularity, convexity of $c$-transforms) controlled by the geometry of the distance function. The Gauss lemma is involved in showing $c$ is smooth on $\{c <$ injectivity radius$^2/2\}$, and in deriving the Ma–Trudinger–Wang condition for regularity of optimal-transport maps. This is a deep recent application of classical Riemannian geometry to a PDE-flavoured problem.

**Geometric analysis: harmonic coordinates.** Normal coordinates are smooth but the metric is only $C^\infty$, and the *regularity* of $g_{ij}$ in these coordinates is controlled by the Ricci tensor. Refined coordinate systems — **harmonic coordinates** — are designed to make $\Delta_g x^i = 0$, and the resulting metric is more regular (e.g., $C^{1, \alpha}$ if $\mathrm{Ric}$ is bounded). The Gauss lemma underlies the comparison between normal and harmonic coordinates and the regularity transfer.

---

# Bridges

- **[[Def - The Riemannian Exponential Map|The Exponential Map]]** — the input. The Gauss lemma is a statement about $d(\exp_p)$, so $\exp_p$ being defined and smooth is presupposed. The lemma extracts a metric statement (orthogonality) from the connection-built construction (exponential), and this is the content of "geodesic = self-parallel + Levi-Civita is metric-compatible".

- **[[Def - Normal Coordinates and Geodesic Coordinates|Normal Coordinates]] and the polar form of the metric.** In geodesic polar coordinates, the lemma says the metric has the form $dr^2 + h(r, \omega)$. This is the polar analogue of the Cartesian normal-coordinate statement $g_{ij}(0) = \delta_{ij}, \partial_k g_{ij}(0) = 0$. The polar form is what makes radial geodesics length-minimising; the Cartesian form is what makes pointwise tensorial computations clean.

- **[[Thm - First Variation of Arc Length|First Variation of Arc Length]]** — the variational sibling. Where the Gauss lemma proves "radial geodesics minimise length locally" by direct length computation, the first variation formula proves "*all* geodesics extremise length" by Euler–Lagrange. The two approaches give complementary information: Gauss gives strict minimisation in a neighbourhood of $p$ (local), first variation gives criticality in any setting (global).

- **[[Def - Jacobi Field|Jacobi Fields]]** — the dual viewpoint. The lemma can be re-read as a statement about Jacobi fields: a Jacobi field with $J(0) = 0$ and $J'(0) \perp T(0)$ is orthogonal to $T$ throughout. The proof we gave reveals that the orthogonality of $J$ to $T$ is preserved by the Jacobi equation (combined with metric compatibility and curvature symmetry). This is one example of the more general principle that *Jacobi fields are the variational version of the geometric content of the connection*.

---

# Unlocked by This

> [!tip] Local Length-Minimisation of Geodesics *(from Riemannian Geometry)*
> The Gauss lemma is what makes radial geodesics from $p$ the unique length-minimising curves to nearby points (within the injectivity radius). This is *the* foundational local statement of Riemannian geometry. Combined with [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]], it upgrades to global existence of minimising geodesics on complete manifolds.

> [!tip] The Distance Function and the Eikonal Equation *(from Riemannian Geometry / PDE)*
> The distance function $d_g(p, \cdot)$ is smooth on the open set where $\exp_p$ is a diffeomorphism (the *normal neighbourhood* of $p$), and its gradient is the unit radial vector $\partial_r$. The Gauss lemma gives $|\nabla d_g(p, \cdot)|^2 = 1$, the **eikonal equation**. This is the foundation of the theory of viscosity solutions of Hamilton–Jacobi PDEs on Riemannian manifolds.

> [!tip] **The Theorema Egregium and Intrinsic Geometry of Surfaces** *(from Differential Geometry)*
> Gauss's original lemma was for surfaces in $\mathbb{R}^3$, and using it he proved the **Theorema Egregium**: the Gaussian curvature $K$ of a surface is intrinsic — it depends only on the induced metric, not on the embedding. The lemma's polar form gives $K(p) = -\frac{1}{\sqrt h}\partial_r^2 \sqrt h$ at $r = 0$ in geodesic polar coordinates, a direct formula for $K$ in terms of the metric. See [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].
