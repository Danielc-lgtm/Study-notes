---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - The Riemannian Exponential Map"
  - "Ex - Great Circles are the Geodesics of the Sphere"
  - "Thm - The Inverse Function Theorem"
tags: [geometry, riemannian-geometry, exponential-map, sphere]
---

# Problem Statement

Let $(S^n, g)$ be the unit $n$-sphere with the round metric. For $p \in S^n$, the [[Def - The Riemannian Exponential Map|Riemannian exponential map]] $\exp_p : T_p S^n \to S^n$ is defined by following geodesics from $p$ for unit time.

(a) Compute $\exp_p$ explicitly using the great-circle parametrisation.

(b) Show that $\exp_p$ is a diffeomorphism from the open ball $\{v \in T_p S^n : |v| < \pi\}$ onto $S^n \setminus \{-p\}$.

(c) Show that $\exp_p$ fails to be injective on the closed ball $\{|v| \leq \pi\}$: the entire boundary sphere $\{|v| = \pi\}$ is collapsed by $\exp_p$ to the single antipodal point $-p$.

**Recall:**

For a Riemannian manifold $(M, g)$ and $p \in M$, the [[Def - The Riemannian Exponential Map|exponential map]] is
$$\exp_p(v) := \gamma_v(1) = \gamma_{(p, v)}(1),$$
where $\gamma_v$ is the unique geodesic with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$.

By the homogeneity property, $\exp_p(tv) = \gamma_v(t)$, so $\exp_p$ traces geodesics in radial direction.

The differential at the origin is the identity: $d(\exp_p)_0 = \mathrm{id}_{T_pM}$. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $\exp_p$ is a local diffeomorphism on a neighbourhood of $0$.

From [[Ex - Great Circles are the Geodesics of the Sphere]]: the geodesics of $(S^n, g)$ through $p$ with initial velocity $v \neq 0$ are
$$\gamma_v(t) = \cos(|v|t)\, p + \sin(|v|t)\, v/|v|.$$

---

# Convergent Strategy

**Problem class:** Computation of the exponential map and its injective range on a specific manifold. This is the "compute the exponential" pattern of the [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles#Problem-Solving Strategy|topic page's problem-solving strategy]], typically yielding to direct evaluation when the geodesics are explicitly known.

**Assumption pattern:** We have the explicit geodesic parametrisation from [[Ex - Great Circles are the Geodesics of the Sphere]]. So computing $\exp_p$ is direct: evaluate the geodesic at $t = 1$. The injectivity question reduces to "for which $v$ does the great circle $\gamma_v$ first return to a previously visited point?"

**Theorem routing:** Three steps. **First**, write $\exp_p(v) = \gamma_v(1) = \cos(|v|)p + \sin(|v|) v/|v|$ (with the convention $\exp_p(0) = p$). **Second**, analyse the map on $\{|v| < \pi\}$: every great circle is traced for less than a half-turn, so the map is injective and a smooth diffeomorphism onto $S^n \setminus \{-p\}$. **Third**, evaluate at $|v| = \pi$: $\exp_p(v) = \cos(\pi)p + \sin(\pi) v/|v| = -p$, regardless of the direction of $v$ — so the entire $\pi$-sphere collapses.

**Key decision point:** The non-injectivity at $|v| = \pi$ is forced by the *geometry* of the sphere: every great circle through $p$ passes through $-p$ at angular distance $\pi$. This is the conjugate-point phenomenon ([[Ex - Conjugate Points on the Round Sphere are Antipodal]]). Showing injectivity on $\{|v| < \pi\}$ uses the fact that, *within a closed half-turn*, distinct great circles from $p$ visit distinct points (no two great circles intersect except at $p$ and $-p$).

---

# Legal Operations Used

1. **Operation 4 from the topic page (compute the exponential via the geodesic flow).** Direct: $\exp_p(v) = \gamma_v(1)$, with $\gamma_v$ the great-circle parametrisation.

2. **Operation 3 from the topic page (exploit uniqueness via symmetry).** Used to confirm injectivity on $\{|v| < \pi\}$: distinct $v$'s give distinct geodesics, hence distinct $\gamma_v(1)$'s (provided we are within a half-turn — beyond that, geodesics start sharing endpoints).

3. **Operation from background ([[Thm - The Inverse Function Theorem|inverse function theorem]])** — though not explicitly used, the local-diffeomorphism statement at $v = 0$ is the IFT applied to $d(\exp_p)_0 = \mathrm{id}$.

---

# Hints

> [!note]- Hint 1
> Use the great-circle formula from [[Ex - Great Circles are the Geodesics of the Sphere]] directly: $\gamma_v(t) = \cos(|v|t) p + \sin(|v|t) v/|v|$. Evaluate at $t = 1$.

> [!note]- Hint 2
> For injectivity on $\{|v| < \pi\}$: given $v_1, v_2$ with $\exp_p(v_1) = \exp_p(v_2)$, deduce that the corresponding great-circle arcs from $p$ end at the same point. With $|v_1|, |v_2| < \pi$, the great-circle arcs are less than half a great circle — and two distinct great circles from $p$ first reintersect at $-p$ (at angular distance $\pi$). So if the endpoints agree before $\pi$, the great circles agree, hence $v_1 = v_2$.

> [!note]- Hint 3
> At $|v| = \pi$: $\cos(\pi) = -1$ and $\sin(\pi) = 0$, so $\exp_p(v) = -p$ regardless of the direction $v/|v|$. So every $v$ on the boundary sphere $|v| = \pi$ is sent to $-p$.

---

# Solution

The exercise has three parts: **(a)** compute the explicit formula; **(b)** prove $\exp_p$ is a diffeomorphism on $\{|v| < \pi\}$ onto $S^n \setminus \{-p\}$; **(c)** observe the collapse on $\{|v| = \pi\}$.

**(a) Explicit formula.**

From the great-circle parametrisation:
$$\exp_p(v) = \gamma_v(1) = \cos(|v|)\, p + \sin(|v|)\, \frac{v}{|v|}, \qquad v \neq 0,$$
with $\exp_p(0) = p$ (taking the limit, $\cos(0) = 1$ and $\sin(0)/0 \cdot v$ makes sense as $v \to 0$ giving $p$).

> [!note]- Derivation
> The geodesic $\gamma_v$ with initial data $(p, v)$ is, by Step 2 of [[Ex - Great Circles are the Geodesics of the Sphere|the great-circle exercise]], $\gamma_v(t) = \cos(|v|t)p + \sin(|v|t) v/|v|$. Setting $t = 1$ gives the formula.

**(b) Diffeomorphism on the open ball of radius $\pi$ onto $S^n \setminus \{-p\}$.**

> [!note]- Derivation
> *Smoothness:* The formula $\exp_p(v) = \cos(|v|)p + \sin(|v|)v/|v|$ is smooth on $T_pS^n \setminus \{0\}$. Near $v = 0$, smoothness follows from the Taylor expansion $\sin(|v|)/|v| = 1 - |v|^2/6 + O(|v|^4)$, which is smooth in $v$ even at $0$. So $\exp_p$ is a smooth map $T_pS^n \to S^n$.
>
> *Image is contained in $S^n \setminus \{-p\}$ for $|v| < \pi$:* Compute $\langle \exp_p(v), p\rangle = \cos(|v|)|p|^2 + \sin(|v|)/|v| \cdot \langle v, p\rangle = \cos(|v|)$, using $|p| = 1$ and $v \perp p$ (since $v \in T_p S^n$). So $\langle \exp_p(v), p\rangle = \cos(|v|) > -1$ for $|v| < \pi$, which means $\exp_p(v) \neq -p$.
>
> *Surjective onto $S^n \setminus \{-p\}$:* Let $q \in S^n \setminus \{-p\}$. We construct $v$ with $\exp_p(v) = q$. Define $\theta := \arccos(\langle q, p\rangle) \in [0, \pi)$ — the angular distance from $p$ to $q$ (well-defined and strictly less than $\pi$ since $q \neq -p$). If $\theta = 0$ then $q = p = \exp_p(0)$, done. If $\theta > 0$, define $\hat v := (q - \langle q, p\rangle p)/|q - \langle q, p\rangle p|$ — the unit vector in $T_p S^n$ pointing toward $q$. Set $v := \theta \hat v$. Then $\exp_p(v) = \cos\theta\cdot p + \sin\theta \cdot \hat v = \cos\theta\cdot p + \sin\theta \cdot (q - \cos\theta\cdot p)/\sin\theta = \cos\theta\cdot p + q - \cos\theta\cdot p = q$. ✓
>
> *Injective on $\{|v| < \pi\}$:* Suppose $\exp_p(v_1) = \exp_p(v_2) = q$. Then both $v_1$ and $v_2$ give geodesics from $p$ to $q$ of length $|v_1|$ and $|v_2|$ respectively. By the geodesic-distance computation above, $|v_i| = \arccos(\langle q, p\rangle) = \theta$ for both — so $|v_1| = |v_2| = \theta$. And both $v_i/|v_i|$ point in the direction $(q - \cos\theta p)/\sin\theta$ (the unique unit tangent vector pointing toward $q$ — note $\sin\theta \neq 0$ since $\theta \neq 0, \pi$). So $v_1/|v_1| = v_2/|v_2|$, and with $|v_1| = |v_2| = \theta$, $v_1 = v_2$.
>
> *Smooth inverse:* The inverse map $\exp_p^{-1} : S^n \setminus \{-p\} \to \{|v| < \pi\}$ sends $q \mapsto \theta \cdot (q - \cos\theta p)/\sin\theta$, where $\theta = \arccos(\langle q, p\rangle)$. This is smooth on $S^n \setminus \{-p\}$ (since $\arccos$ is smooth on $(-1, 1)$ and the formula is smooth in $q$).

**(c) Collapse on the boundary sphere $\{|v| = \pi\}$.**

> [!note]- Derivation
> At $|v| = \pi$: $\cos\pi = -1$ and $\sin\pi = 0$. So $\exp_p(v) = -p + 0\cdot v/|v| = -p$ for *every* $v$ with $|v| = \pi$. So $\exp_p$ sends the entire sphere $\{|v| = \pi\}$ to the single point $-p$ — a massive collapse, with the entire $(n-1)$-sphere of unit-radius directions in $T_p S^n$ being identified.
>
> This is the conjugate-point phenomenon: $-p$ is conjugate to $p$ along every geodesic through $p$, with multiplicity $n - 1$ — there is an $(n-1)$-dimensional space of Jacobi fields along each great circle that vanish at both $p$ and $-p$, see [[Ex - Conjugate Points on the Round Sphere are Antipodal]]. Equivalently, $d(\exp_p)_v$ has rank $1$ (one-dimensional image, the radial direction) at $|v| = \pi$, and the kernel is the $(n-1)$-dimensional tangent space to the sphere $\{|v| = \pi\}$ at $v$.

> [!note]- Complete formal solution
> **(a)** For $v \in T_p S^n$ with $v \neq 0$,
> $$\exp_p(v) = \cos(|v|)p + \sin(|v|)\frac{v}{|v|},$$
> and $\exp_p(0) = p$. This formula is smooth on $T_pS^n$ (smoothly extending across $v = 0$ using $\sin(|v|)/|v| \to 1$).
>
> **(b)** $\exp_p$ restricted to the open ball $\{|v| < \pi\} \subseteq T_pS^n$ is a diffeomorphism onto $S^n \setminus \{-p\}$.
>
> *Smoothness:* immediate from the formula.
>
> *Image $\subseteq S^n \setminus \{-p\}$:* $\langle \exp_p(v), p\rangle = \cos(|v|) > -1$ for $|v| < \pi$, so $\exp_p(v) \neq -p$.
>
> *Surjective:* given $q \in S^n \setminus \{-p\}$, set $\theta := \arccos\langle q, p\rangle \in [0, \pi)$; if $\theta = 0$, $q = p = \exp_p(0)$; else, set $v := \theta \cdot (q - \cos\theta\cdot p)/\sin\theta$, verify $\exp_p(v) = q$.
>
> *Injective on $\{|v| < \pi\}$:* if $\exp_p(v_1) = \exp_p(v_2)$, then $|v_i| = \theta$ for both (length of the unique minimising geodesic to a non-antipodal point), and $v_i/|v_i|$ both point in the unique direction toward $q$ from $p$.
>
> *Smooth inverse:* $\exp_p^{-1}(q) = \theta(q - \cos\theta p)/\sin\theta$ for $\theta = \arccos\langle q, p\rangle$, smooth on $S^n \setminus \{-p\}$.
>
> **(c)** For every $v$ with $|v| = \pi$, $\exp_p(v) = \cos\pi\cdot p + \sin\pi \cdot v/|v| = -p$. So $\exp_p$ collapses the entire sphere $\{|v| = \pi\}$ to the single antipodal point $-p$. $\qquad\blacksquare$

---

# Key Takeaways

**The exponential map's failure to be a global diffeomorphism is detected by *conjugate points*.** On $S^n$, the antipodal point $-p$ is conjugate to $p$ along *every* great circle through $p$, with multiplicity $n - 1$ — the entire transverse direction at $-p$ is killed by the differential of $\exp_p$. This is the cleanest example of the [[Thm - Jacobi Equation and Conjugate Points|Jacobi-equation/conjugate-point dictionary]]: the failure of $d(\exp_p)$ to be invertible at $v$ with $|v| = \pi$ is exactly the existence of nonzero Jacobi fields along $\gamma_v$ vanishing at both $0$ and $1$. **The pattern:** on a compact positively-curved manifold, $\exp_p$ is a local diffeomorphism up to the first conjugate distance and fails globally beyond it.

**The injectivity radius equals the first conjugate distance for the round sphere.** The injectivity radius at $p \in S^n$ is the largest $r$ such that $\exp_p|_{B(0, r)}$ is injective — which is $\pi$ on the unit sphere. This equals the first conjugate distance (also $\pi$), so the entire injectivity-radius theory and the conjugate-point theory coincide on the sphere. In general manifolds the injectivity radius can be *smaller* than the first conjugate distance — the additional obstruction is the existence of multiple minimising geodesics (cut points) that aren't necessarily conjugate. The sphere is the simplest case where they agree.

**Computing the exponential map explicitly is the cleanest way to understand the geometry of a homogeneous space.** Whenever a manifold has enough symmetry (homogeneous, symmetric space), the geodesics are explicit (one-parameter subgroups, orbits of one-parameter isometry groups), so $\exp_p$ has an explicit formula. The technique transfers: on hyperbolic space $\mathbb{H}^n$, $\exp_p$ is the analogous formula with hyperbolic trigonometric functions ($\cosh, \sinh$ instead of $\cos, \sin$), and is a *global* diffeomorphism $T_p \mathbb{H}^n \to \mathbb{H}^n$ (no conjugate points anywhere). On a Lie group with bi-invariant metric, the Riemannian exponential is the Lie-group exponential, and the conjugate-point structure is determined by the Lie algebra eigenvalues. Each case is a direct computation — the difficulty is in setting up the geodesics, after which the exponential map is a one-line evaluation.
