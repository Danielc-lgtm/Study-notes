---
type: exercise
subject: riemannian-geometry
difficulty: "⭐"
prereqs:
  - "Def - Geodesic"
  - "Thm - Existence and Uniqueness of Geodesics"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, geodesics, sphere]
---

# Problem Statement

Let $S^n \subseteq \mathbb{R}^{n+1}$ be the unit sphere with the Riemannian metric $g$ induced from the Euclidean metric on $\mathbb{R}^{n+1}$. Show that the [[Def - Geodesic|geodesics]] of $(S^n, g)$ are exactly the *great circles*: parametrised at constant speed, they have the form $\gamma(t) = \cos(|v|\, t)\, p + \sin(|v|\, t)\, v/|v|$ for $p \in S^n$ and $v \in T_p S^n$.

**Recall:**

A [[Def - Geodesic|geodesic]] of a Riemannian manifold $(M, g)$ is a curve $\gamma : I \to M$ satisfying $\nabla_{\dot\gamma}\dot\gamma = 0$, where $\nabla$ is the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]]. By [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness]], a geodesic is uniquely determined by its initial position $\gamma(0) = p$ and initial velocity $\dot\gamma(0) = v$.

A **great circle** on $S^n$ is the intersection of $S^n$ with a 2-plane through the origin in $\mathbb{R}^{n+1}$.

For a submanifold $M \subseteq \tilde M$ with induced Riemannian metric, the covariant acceleration $\nabla_{\dot\gamma}\dot\gamma$ of a curve $\gamma \subseteq M$ is the **tangential projection** of the ambient covariant acceleration $\tilde\nabla_{\dot\gamma}\dot\gamma$ (which, for $\tilde M = \mathbb{R}^{n+1}$, is just the ordinary second derivative $\ddot\gamma$).

---

# Convergent Strategy

**Problem class:** Identification of geodesics on a specific manifold. The exercise is in the class "given an explicit metric, characterise the geodesics" — see the [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles#Problem-Solving Strategy|topic page's problem-solving strategy]]. Such problems typically yield to one of three approaches: direct ODE integration in coordinates, symmetry/uniqueness, or — for embedded submanifolds — projection of the ambient acceleration.

**Assumption pattern:** The sphere $S^n$ comes with massive symmetry: the orthogonal group $O(n+1)$ acts by [[Def - Isometry|isometries]]. So we have a rich Killing-vector structure and many opportunities to apply the uniqueness theorem. Additionally, the sphere is *embedded* in $\mathbb{R}^{n+1}$, which lets us use the projection formula for the induced connection.

**Theorem routing:** Two routes. **Route A (embedding):** for $\gamma \subseteq S^n \subseteq \mathbb{R}^{n+1}$, the covariant acceleration $\nabla_{\dot\gamma}\dot\gamma$ equals the tangential part of $\ddot\gamma$ (ambient second derivative). Compute $\ddot\gamma$ for the candidate $\gamma(t) = \cos(|v|t)p + \sin(|v|t)v/|v|$; show it is *parallel* to $\gamma$ (i.e., radial), hence its tangential part vanishes. **Route B (symmetry / uniqueness):** by [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness]], the geodesic with $\gamma(0) = p, \dot\gamma(0) = v$ is unique. Show that the reflection $\sigma$ across the plane through $p$ and $v$ is an isometry of $S^n$ fixing $p$ and $v$; then $\sigma \circ \gamma$ is also a geodesic with the same initial conditions, hence $\sigma \circ \gamma = \gamma$; the fixed-point set of $\sigma$ is exactly the great circle through $p$ in direction $v$, so the geodesic lies on that great circle.

**Key decision point:** Route A is computational and works directly with the geodesic equation; Route B is the *uniqueness trick* that generalises to any symmetric space. Route B is more elegant and the technique transfers (e.g., to hyperbolic space, Schwarzschild, Lie [[Def - Group|groups]] with bi-invariant metric), so we present it as the main solution with Route A as a verification.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the geodesic equation in coordinates).** We *don't* use this directly — the symmetry trick avoids computing Christoffel symbols. But it would be the fallback if the symmetry argument failed.

2. **Operation 2 from the topic page (use a Killing vector / symmetry).** The full orthogonal group $O(n+1)$ acts by isometries on $S^n$; we use the reflections (discrete symmetries — not Killing vectors per se, but the same uniqueness-of-fixed-set logic applies).

3. **Operation 3 from the topic page (exploit uniqueness to identify a geodesic).** The core move: a reflection isometry that fixes $(p, v)$ in $TS^n$ also fixes the geodesic with that initial data; the fixed-set of the reflection is the great circle, so the geodesic must lie on it.

---

# Hints

> [!note]- Hint 1
> Use the symmetry of $S^n$. What isometry fixes the initial point $p$ and the initial velocity $v \in T_p S^n$?

> [!note]- Hint 2
> The reflection $\sigma : \mathbb{R}^{n+1} \to \mathbb{R}^{n+1}$ across the 2-plane spanned by $p$ and $v$ is an orthogonal transformation, hence an isometry of $S^n$. It fixes the great circle through $p$ in direction $v$ and reflects everything else.

> [!note]- Hint 3
> If $\gamma$ is the geodesic with $\gamma(0) = p, \dot\gamma(0) = v$, what does the uniqueness theorem say about $\sigma \circ \gamma$? Use [[Thm - Existence and Uniqueness of Geodesics|the uniqueness of the geodesic with given initial conditions]].

> [!note]- Hint 4
> Verify directly that the candidate curve $\gamma(t) = \cos(|v|t)\, p + \sin(|v|t)\, v/|v|$ has tangential acceleration zero on $S^n$. Differentiate twice: $\ddot\gamma = -|v|^2 \gamma$, which is parallel to $\gamma$ (the radial direction in $\mathbb{R}^{n+1}$), hence its tangential projection on $S^n$ is zero.

---

# Solution

The proof has two steps. **Step 1** uses the symmetry/uniqueness argument to show *any* geodesic on $S^n$ lies on a great circle. **Step 2** verifies that the explicit parametrisation $\gamma(t) = \cos(|v|t)\, p + \sin(|v|t)\, v/|v|$ is in fact a geodesic by directly computing its covariant acceleration. Together, these establish that geodesics are exactly great circles with constant-speed parametrisation.

**Step 1: any geodesic on $S^n$ lies on a great circle through its initial point in its initial direction.**

Let $\gamma$ be the unique geodesic on $S^n$ with $\gamma(0) = p$ and $\dot\gamma(0) = v \in T_p S^n$.

> [!note]- Derivation
> Consider the 2-plane $P := \mathrm{span}\{p, v\} \subseteq \mathbb{R}^{n+1}$. (Recall $v \in T_p S^n$ means $v \perp p$ in the ambient Euclidean structure, so $p$ and $v$ are linearly independent — assuming $v \neq 0$, otherwise $\gamma$ is the trivial constant geodesic.)
>
> Let $\sigma : \mathbb{R}^{n+1} \to \mathbb{R}^{n+1}$ be the *reflection across the 2-plane $P$*: it fixes $P$ pointwise and reflects $P^\perp$ by $-1$. Then $\sigma$ is an orthogonal transformation of $\mathbb{R}^{n+1}$, hence preserves $S^n$ (since $|\sigma(x)| = |x|$) and acts as an isometry of the induced metric on $S^n$. In particular, $\sigma(p) = p$ (since $p \in P$) and $d\sigma_p(v) = v$ (since $v \in P$).
>
> By [[Def - Geodesic|the geodesic equation]] and [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness]], the curve $\sigma \circ \gamma$ is also a geodesic, with $(\sigma \circ \gamma)(0) = \sigma(p) = p$ and $(\sigma \circ \gamma)'(0) = d\sigma_p(\dot\gamma(0)) = d\sigma_p(v) = v$. Both $\gamma$ and $\sigma \circ \gamma$ are geodesics with the same initial data, so by uniqueness $\sigma \circ \gamma = \gamma$.
>
> This means $\gamma(t) = \sigma(\gamma(t))$ for all $t$, so $\gamma(t)$ lies in the fixed-point set of $\sigma$ for all $t$. The fixed-point set of $\sigma$ in $\mathbb{R}^{n+1}$ is exactly the 2-plane $P$. So $\gamma(t) \in P \cap S^n =$ the great circle of $S^n$ through $p$ in direction $v$ (the intersection of $S^n$ with the 2-plane $P$).
>
> So the image of $\gamma$ is contained in this great circle.

**Step 2: the explicit candidate $\gamma(t) = \cos(|v|t)\, p + \sin(|v|t)\, v/|v|$ is a geodesic.**

> [!note]- Derivation
> Set $\omega := |v|$ for clarity, and write $\hat v := v/|v|$ — the unit vector in the direction of $v$. So $\gamma(t) = \cos(\omega t)\, p + \sin(\omega t)\, \hat v$.
>
> First, verify $\gamma(t) \in S^n$: $|\gamma(t)|^2 = \cos^2(\omega t)|p|^2 + 2\cos(\omega t)\sin(\omega t) g(p, \hat v) + \sin^2(\omega t)|\hat v|^2 = \cos^2(\omega t) \cdot 1 + 0 + \sin^2(\omega t) \cdot 1 = 1$, using $|p| = |\hat v| = 1$ and $p \perp \hat v$ (since $\hat v \in T_p S^n$). So $\gamma(t) \in S^n$.
>
> Verify $\dot\gamma(0) = v$: $\dot\gamma(t) = -\omega \sin(\omega t)\, p + \omega \cos(\omega t)\, \hat v$. At $t = 0$: $\dot\gamma(0) = \omega \hat v = v$. Good.
>
> Compute the ambient second derivative: $\ddot\gamma(t) = -\omega^2 \cos(\omega t)\, p - \omega^2 \sin(\omega t)\, \hat v = -\omega^2 \gamma(t)$.
>
> So $\ddot\gamma$ is parallel to $\gamma$ — i.e., the ambient acceleration is *radial* in $\mathbb{R}^{n+1}$, pointing from $\gamma(t)$ toward the origin. But the radial direction at $\gamma(t) \in S^n$ is *normal* to $S^n$ (the outward normal at $\gamma(t)$ is $\gamma(t)$ itself, since $S^n$ is the unit sphere). So $\ddot\gamma \perp T_{\gamma(t)}S^n$.
>
> The covariant acceleration on $S^n$ is the *tangential* part of $\ddot\gamma$: $\nabla_{\dot\gamma}\dot\gamma = (\ddot\gamma)^{\mathrm{tan}}$. Since $\ddot\gamma$ is entirely normal, $(\ddot\gamma)^{\mathrm{tan}} = 0$. So $\nabla_{\dot\gamma}\dot\gamma = 0$, and $\gamma$ is a geodesic.

> [!note]- Complete formal solution
> **Claim.** The geodesics of $(S^n, g)$ with initial data $(\gamma(0), \dot\gamma(0)) = (p, v)$ are exactly the curves
> $$\gamma(t) = \cos(|v|t)\, p + \sin(|v|t)\, \frac{v}{|v|},$$
> for $v \neq 0$ (and the constant geodesic $\gamma \equiv p$ for $v = 0$).
>
> *Proof.* First, the explicit formula gives a geodesic. The curve $\gamma$ lies in $S^n$ since $|\gamma(t)|^2 = \cos^2(|v|t) + \sin^2(|v|t) = 1$ (using $|p| = 1$, $p \perp v$, $|v/|v|| = 1$). The ambient second derivative is $\ddot\gamma = -|v|^2 \gamma$, parallel to $\gamma$, hence orthogonal to $T_{\gamma(t)}S^n$ (the tangent space at $\gamma(t)$ is the orthogonal complement of $\gamma(t)$ in $\mathbb{R}^{n+1}$). The covariant acceleration on $S^n$ is the tangential projection of the ambient: $\nabla_{\dot\gamma}\dot\gamma = (\ddot\gamma)^{\mathrm{tan}} = 0$. So $\gamma$ is a geodesic, with $\gamma(0) = p, \dot\gamma(0) = |v|\cdot v/|v| = v$, as desired.
>
> Second, by [[Thm - Existence and Uniqueness of Geodesics|uniqueness]], $\gamma$ is *the* geodesic with these initial conditions. So this is the entire geodesic.
>
> The image of $\gamma$ is the great circle $S^n \cap \mathrm{span}\{p, v\}$ (by the symmetry argument in Step 1, or by directly observing that $\gamma(t) \in \mathrm{span}\{p, \hat v\}$ for all $t$).
>
> Conversely, every great circle on $S^n$ has constant-speed parametrisations of this form (varying $p$ and $v$ produces all great circles). So the geodesics are exactly the great circles, with constant-speed parametrisation. $\qquad\blacksquare$

---

# Key Takeaways

**The uniqueness trick is the most efficient way to identify geodesics on symmetric spaces.** Whenever you have an isometry that fixes the initial point and initial velocity, the geodesic with that initial data must lie in the fixed-point set of the isometry — by uniqueness of geodesics from given initial data. On the sphere, the fixed set of a reflection across the 2-plane spanned by $p$ and $v$ is a great circle; on hyperbolic space, similar reflections give vertical lines and orthogonal semicircles; on a Lie group with bi-invariant metric, conjugation gives one-parameter [[Def - Subgroup|subgroups]]. The pattern is the same: find a symmetry, identify its fixed-point set, conclude the geodesic lies there. This is much faster than computing Christoffel symbols and integrating the geodesic ODE.

**The "tangential acceleration" formula for submanifold geodesics is the cleanest computational route.** For a submanifold $M \subseteq \tilde M$ with induced metric (the standard setting in differential geometry), the geodesic equation on $M$ reduces to "the tangential part of the ambient acceleration vanishes". For the sphere in Euclidean space, the ambient acceleration of $\cos(\omega t)p + \sin(\omega t)\hat v$ is $-\omega^2 \gamma$, pointing radially inward — entirely normal to the sphere, hence with zero tangential part. This three-line calculation replaces the entire Christoffel-symbol computation, and the same technique works for any surface or submanifold in $\mathbb{R}^N$.

**Great circles minimise length up to (and including) the antipode, but not beyond.** A great-circle arc of angular length $\theta < \pi$ is the unique minimising geodesic between its endpoints. At $\theta = \pi$ (antipodal points), there are infinitely many minimising great-circle arcs (any half-great-circle through the two points). For $\theta > \pi$, the corresponding arc is *not* minimising — there is a shorter great-circle arc going the other way around. This non-minimisation past the antipode is reflected in the conjugate-point structure (see [[Ex - Conjugate Points on the Round Sphere are Antipodal]]) and is the prototype example for understanding how curvature breaks length-minimisation.
