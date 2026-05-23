---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Conjugate Point"
  - "Def - Jacobi Field"
  - "Ex - Jacobi Fields on a Sphere are Sinusoidal"
  - "Thm - Jacobi Equation and Conjugate Points"
tags: [geometry, riemannian-geometry, conjugate-points, sphere]
---

# Problem Statement

Let $(S^n, g)$ be the unit $n$-sphere with the round metric, $p \in S^n$, and $\gamma : \mathbb{R} \to S^n$ a unit-speed geodesic with $\gamma(0) = p$. Show that:

(a) The points conjugate to $p$ along $\gamma$ are exactly $\gamma(k\pi)$ for non-zero integers $k$. So the *first* conjugate point to $p$ is the antipode $-p = \gamma(\pi)$.

(b) The multiplicity of each conjugate point $\gamma(k\pi)$ along $\gamma$ is $n - 1$.

(c) Conclude that the exponential map $\exp_p : T_p S^n \to S^n$ fails to be a local diffeomorphism precisely on the spheres $\{|v| = k\pi : k \in \mathbb{Z}^+\}$ in $T_p S^n$, with corank $n - 1$ there.

**Recall:**

A point $\gamma(t_0)$ is [[Def - Conjugate Point|conjugate]] to $p = \gamma(0)$ along $\gamma$ if there exists a nonzero [[Def - Jacobi Field|Jacobi field]] $J$ along $\gamma$ with $J(0) = J(t_0) = 0$. The **multiplicity** is the dimension of the space of such Jacobi fields.

By [[Thm - Jacobi Equation and Conjugate Points|the Jacobi-equation/conjugate-point dictionary]], $\gamma(t_0)$ is conjugate to $p$ along $\gamma$ iff $d(\exp_p)_{t_0 v}$ is singular (where $v = \dot\gamma(0)$), with multiplicity equal to $\dim \ker d(\exp_p)_{t_0 v}$.

From [[Ex - Jacobi Fields on a Sphere are Sinusoidal]]: normal Jacobi fields along a unit-speed geodesic on $S^n$ are of the form $J(t) = (a\cos t + b\sin t)E(t)$ for parallel unit fields $E \perp T$.

---

# Convergent Strategy

**Problem class:** Determining the conjugate locus of a point on a specific manifold. This is in the "find conjugate points" class — usually approached by finding all Jacobi fields explicitly and identifying the zeros of those with $J(0) = 0$.

**Assumption pattern:** $S^n$ has constant sectional curvature $1$, and from [[Ex - Jacobi Fields on a Sphere are Sinusoidal|the sinusoidal exercise]] we have the explicit Jacobi-field formula. So the conjugate-point analysis reduces to: find the zeros of $\sin t$ for $t > 0$, which are $t = k\pi$ for $k \in \mathbb{Z}^+$.

**Theorem routing:** From the sinusoidal Jacobi field formula $J(t) = \sin(t)E(t)$ (with $E$ a parallel unit normal): zeros of $\sin t$ for $t > 0$ are at $t = \pi, 2\pi, 3\pi, \ldots$ For each such $t = k\pi$ and each parallel unit field $E$ in the $(n-1)$-dimensional space $T^\perp$, we get a vanishing Jacobi field. So the multiplicity is $n - 1$ at each.

**Key decision point:** Don't conflate the *first* conjugate point (the antipode at $\pi$) with the entire conjugate locus (the antipode together with the periodic returns $2\pi, 3\pi, \ldots$). The first conjugate distance is the most-used quantity (it bounds the injectivity radius and the Bonnet–Myers diameter), but the full periodic structure reveals why $\exp_p$ has multiple singular spheres rather than just one.

---

# Legal Operations Used

1. **Operation 8 from the topic page (solve the Jacobi equation along $\gamma$).** Use the explicit sinusoidal form from [[Ex - Jacobi Fields on a Sphere are Sinusoidal]].

2. **Operation from background (translation between Jacobi fields and exponential-map singularities).** Apply [[Thm - Jacobi Equation and Conjugate Points|the Jacobi-equation/conjugate-point dictionary]] to convert "vanishing Jacobi field" to "singular $d(\exp_p)$".

---

# Hints

> [!note]- Hint 1
> From [[Ex - Jacobi Fields on a Sphere are Sinusoidal]], the normal Jacobi field with $J(0) = 0$ and $J'(0) = E(0)$ (for parallel unit $E$) is $J(t) = \sin(t) E(t)$. For which $t > 0$ does $J(t) = 0$?

> [!note]- Hint 2
> Zeros of $\sin t$ for $t > 0$ are at $t = \pi, 2\pi, 3\pi, \ldots$ So conjugate points to $p$ along the great circle are at parameter values $k\pi$ for $k \in \mathbb{Z}^+$.

> [!note]- Hint 3
> At $t = k\pi$, the Jacobi field $\sin(t)E(t)$ vanishes for *every* choice of parallel unit field $E \perp T$ — and there is an $(n - 1)$-dimensional space of such directions. So the multiplicity of each conjugate point is $n - 1$.

> [!note]- Hint 4
> By [[Thm - Jacobi Equation and Conjugate Points|the Jacobi-equation/conjugate-point dictionary]], $d(\exp_p)_{t_0 v}$ is singular at $t_0 v$ iff $\gamma_v(t_0)$ is conjugate to $p$. The kernel of $d(\exp_p)_{t_0 v}$ corresponds to the space of $w$ with $J_w(t_0) = 0$, which (by the sinusoidal formula) is the entire $T^\perp$ — i.e., the kernel is $(n-1)$-dimensional, corank $n-1$.

---

# Solution

**(a) Conjugate points along $\gamma$ are at $t = k\pi$ for $k \in \mathbb{Z} \setminus \{0\}$.**

> [!note]- Derivation
> By [[Ex - Jacobi Fields on a Sphere are Sinusoidal|the sinusoidal exercise]], the Jacobi field with $J(0) = 0$ and $J'(0) = E(0)$ (for parallel unit $E \perp T$) is $J(t) = \sin(t) E(t)$.
>
> $J(t_0) = 0$ iff $\sin(t_0) E(t_0) = 0$. Since $E(t_0) \neq 0$ ($E$ is a unit field, parallel-transported), this requires $\sin t_0 = 0$, i.e., $t_0 = k\pi$ for $k \in \mathbb{Z}$. Excluding $t_0 = 0$ (which gives the trivial conjugate-to-itself case), the conjugate parameter values are $t_0 = k\pi$ for $k \in \mathbb{Z}^+$ (and by reversing the geodesic also $k \in \mathbb{Z}^-$).
>
> The corresponding conjugate points are $\gamma(k\pi) \in S^n$. On the unit sphere parametrised by the great circle starting at $p$ in direction $v = \dot\gamma(0)$: $\gamma(t) = \cos(t)p + \sin(t)v$ (using the great-circle formula from [[Ex - Great Circles are the Geodesics of the Sphere]] with $|v| = 1$). At $t = \pi$: $\gamma(\pi) = -p + 0 = -p$, the antipode. At $t = 2\pi$: $\gamma(2\pi) = p$ (back to start). At $t = k\pi$: $\gamma(k\pi) = (-1)^k p$, alternating between $-p$ and $p$.
>
> So the conjugate locus to $p$ along $\gamma$ consists of the antipode $-p$ and the original point $p$ — periodic returns.

**(b) Multiplicity $n - 1$ at each conjugate point.**

> [!note]- Derivation
> At $t_0 = k\pi$, every Jacobi field of the form $J(t) = \sin(t) E(t)$ vanishes — for every parallel unit field $E \perp T$. The space of parallel unit-normal directions $E(0) \in T_p S^n$ orthogonal to $T(0) = v$ has dimension $n - 1$ (the orthogonal complement of a unit vector in an $n$-dimensional space). Each direction gives a 1-dimensional space of Jacobi fields vanishing at $t_0$ (the constant-multiple line).
>
> But wait — the space of Jacobi fields with $J(0) = 0$ has dimension $n$ (it is the space of valid $J'(0) \in T_p S^n$). Among these, the ones that *also* vanish at $t_0 = k\pi$ are exactly those with $J'(0) \perp T$ — i.e., the $(n - 1)$-dimensional subspace of $T^\perp$. So the multiplicity of the conjugate pair $(p, \gamma(k\pi))$ is $n - 1$.
>
> (The tangential Jacobi field $J(t) = t T(t)$ with $J(0) = 0, J'(0) = T(0)$ does not vanish for $t > 0$ — it grows linearly, the standard "reparametrisation" tangential Jacobi field. So only the *normal* Jacobi fields contribute to the multiplicity.)

**(c) $\exp_p$ singular spheres at $|v| = k\pi$, corank $n - 1$.**

> [!note]- Derivation
> By [[Thm - Jacobi Equation and Conjugate Points|the dictionary]], $d(\exp_p)_{tv}$ has kernel of dimension equal to the multiplicity of the conjugate pair $(p, \gamma_v(t))$. At $|v| = 1$ and $t = k\pi$, this is the multiplicity $n - 1$ from part (b). More generally, parametrising the tangent vector as $tv$ for unit $v$, the singular set of $d(\exp_p)$ in $T_p S^n$ is the union of spheres $\{|tv| = k\pi : k \in \mathbb{Z}^+\} = \{|w| = k\pi\}$ — the spheres of radius $k\pi$ in $T_p S^n$.
>
> $d(\exp_p)_w$ has rank $1$ at $w$ with $|w| = k\pi$: the radial direction survives (always — radial directions map to geodesic velocity by homogeneity), but the entire $(n-1)$-dimensional transverse direction is collapsed.
>
> So the first singular sphere (at $|w| = \pi$) is collapsed by $\exp_p$ to the antipode $-p$ — consistent with [[Ex - The Exponential Map on a Sphere is a Local Diffeomorphism]]. The second singular sphere (at $|w| = 2\pi$) is collapsed to $p$ itself. The third (at $|w| = 3\pi$) to $-p$, and so on.

> [!note]- Complete formal solution
> **(a)** From the sinusoidal Jacobi-field formula (Ex on Jacobi fields), the Jacobi field with $J(0) = 0, J'(0) = E$ (for parallel unit $E \perp T$) is $J(t) = \sin(t) E(t)$. This vanishes at $t = k\pi$ for $k \in \mathbb{Z}$, $k \neq 0$. So conjugate points to $p$ along $\gamma$ are at parameter $t = k\pi$ for $k \in \mathbb{Z} \setminus \{0\}$. The corresponding geometric points are $\gamma(\pi) = -p$ (antipode), $\gamma(2\pi) = p$, $\gamma(3\pi) = -p$, $\ldots$.
>
> **(b)** At each conjugate parameter $t_0 = k\pi$, the space of Jacobi fields with $J(0) = J(t_0) = 0$ is $\{J(t) = \sin(t) E(t) : E\text{ parallel unit normal field}\}$, of dimension $n - 1$ (one for each direction in $T^\perp$). So the multiplicity of the conjugate pair $(p, \gamma(k\pi))$ is $n - 1$.
>
> **(c)** By the [[Thm - Jacobi Equation and Conjugate Points|Jacobi-equation/conjugate-point dictionary]], $d(\exp_p)_w$ is singular at $w$ iff $|w|$ is a conjugate distance from $p$ — i.e., iff $|w| \in \{k\pi : k \in \mathbb{Z}^+\}$. The kernel of $d(\exp_p)_w$ at such a singular point is $(n-1)$-dimensional (the entire $T^\perp$ collapses), so the corank is $n - 1$ and the rank is $1$. $\qquad\blacksquare$

---

# Key Takeaways

**On constant-curvature spaces, conjugate points are completely classified by the sectional curvature.** The first conjugate distance is $\pi/\sqrt{K}$ for sectional curvature $K > 0$ (sphere of radius $1/\sqrt K$ has first conjugate distance $\pi/\sqrt K$, scaling appropriately); $\infty$ for $K \leq 0$. The multiplicity is $n - 1$ for constant positive curvature (every direction in $T^\perp$ supports a vanishing Jacobi field at the conjugate distance). This is the simplest possible conjugate-point structure: maximally degenerate, periodic, and globally determined by the curvature. **Comparison theorems** (Rauch, Bonnet–Myers) measure non-constant-curvature manifolds against this baseline.

**The high multiplicity of the antipodal conjugate point on $S^n$ is the geometric reason $\exp_p$ "collapses spheres".** Every great circle through $p$ passes through the antipode $-p$ at distance $\pi$, so the entire sphere of radius $\pi$ in $T_p S^n$ is sent to $-p$. The multiplicity $n - 1$ says that all $n - 1$ transverse directions to a great circle are simultaneously collapsed — explaining why the image of the radius-$\pi$ sphere is a single point rather than a lower-dimensional submanifold. In contrast, on a manifold with *generic* curvature, conjugate points along a typical geodesic would have multiplicity $1$ (single eigenvalue of $R(\cdot, T)T$ achieves the critical value), and the singular locus of $\exp_p$ would be a stratified set, not a clean sphere.

**The periodic-conjugate structure $k\pi$ reflects the global periodicity of geodesic flow on the sphere.** Each great circle on $S^n$ is a closed orbit of period $2\pi$, so the geodesic flow on the unit tangent bundle $S(TS^n)$ is *completely periodic* — every orbit returns. The conjugate-point analysis recovers this: not only does the antipode appear at $\pi$, but the original point reappears at $2\pi$, and the pattern repeats with period $2\pi$. This is a very special feature of the round sphere — generic positive-curvature manifolds do not have closed geodesic flow (the Riemannian metrics with this property are called **Zoll metrics**, and the round sphere is one of very few examples).

**Compare with hyperbolic space: no conjugate points anywhere.** On $\mathbb{H}^n$ with constant sectional curvature $-1$, the Jacobi equation along a unit-speed geodesic is $f'' - f = 0$ (sign flip from the sphere), with solutions $\sinh t, \cosh t$. The solution with $f(0) = 0, f'(0) = 1$ is $\sinh t$, which is *never zero for $t > 0$*. So $\mathbb{H}^n$ has no conjugate points anywhere — and consequently $\exp_p : T_p \mathbb{H}^n \to \mathbb{H}^n$ is a global diffeomorphism (Cartan–Hadamard, see [[Riemannian Geometry III — Riemann Curvature and Topology]]). The contrast — periodic conjugate locus on $S^n$ vs none on $\mathbb{H}^n$ — is the cleanest manifestation of the positive-vs-negative-curvature dichotomy.
