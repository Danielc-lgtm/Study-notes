---
type: exercise
subject: riemannian-geometry
difficulty: "⭐"
prereqs:
  - "Def - First Fundamental Form"
  - "Def - Second Fundamental Form"
  - "Def - Gauss Curvature and Mean Curvature"
tags: [geometry, riemannian-geometry, surfaces, curvature, sphere]
---

# Problem Statement

Show that the sphere of radius $a > 0$ in $\mathbb{R}^3$, with the round metric (the induced metric from the standard Euclidean inclusion $S^2_a \subset \mathbb{R}^3$), has constant Gauss curvature $K = 1/a^2$ everywhere.

Use spherical coordinates: parametrise $S^2_a$ (excluding the poles, which require a separate chart) as
$$
\mathbf{x}(\theta, \varphi) = (a\sin\theta\cos\varphi, a\sin\theta\sin\varphi, a\cos\theta),
$$
with $\theta \in (0, \pi)$ (colatitude) and $\varphi \in [0, 2\pi)$ (longitude).

**Recall:**

A regular surface $M \subset \mathbb{R}^3$ has a [[Def - First Fundamental Form|first fundamental form]] $\mathrm{I}$, the induced Riemannian metric on $M$, with components $g_{\alpha\beta} = \langle\mathbf{x}_\alpha, \mathbf{x}_\beta\rangle$ in coordinates.

![[Def - First Fundamental Form#The Definition]]

The [[Def - Second Fundamental Form|second fundamental form]] $\mathrm{II}$ is the symmetric bilinear form $\mathrm{II}(X, Y) = \langle\mathbf{x}_{\alpha\beta}, N\rangle\, du^\alpha du^\beta$, where $N$ is the unit normal to $M$.

The [[Def - Gauss Curvature and Mean Curvature|Gauss curvature]] is $K = \det b_{\alpha\beta}/\det g_{\alpha\beta} = (eg_\mathrm{II} - f^2)/(EG - F^2)$ in classical notation, where $(E, F, G) = (g_{11}, g_{12}, g_{22})$ and $(e, f, g_\mathrm{II}) = (b_{11}, b_{12}, b_{22})$.

---

# Convergent Strategy

**Problem class:** Direct computation of a curvature invariant on an explicit parametrised surface. This is the most basic type of surface-theory problem — given $\mathbf{x}(u, v)$, mechanically compute $E, F, G, e, f, g_\mathrm{II}$ via dot products of derivative vectors, then assemble $K$. Every such problem follows the same six-step routine.

**Assumption pattern:** The parametrisation $\mathbf{x}(\theta, \varphi)$ is given explicitly with smooth dependence on $(\theta, \varphi)$, and is regular (the cross product $\mathbf{x}_\theta\times\mathbf{x}_\varphi$ is nonzero) away from the poles. The spherical geometry has rotational symmetry around the $z$-axis, which we exploit by choosing the colatitude/longitude coordinates — the symmetry implies $F = 0$ and $g_{\alpha\beta}$ has the form $\mathrm{diag}(E, G)$.

**Theorem routing:** Direct computation via the determinant formula. Compute $\mathbf{x}_\theta, \mathbf{x}_\varphi, \mathbf{x}_{\theta\theta}, \mathbf{x}_{\theta\varphi}, \mathbf{x}_{\varphi\varphi}$ as vectors in $\mathbb{R}^3$; take dot products to get $E, F, G$; cross-product gives the unit normal $N = (\mathbf{x}_\theta\times\mathbf{x}_\varphi)/|\mathbf{x}_\theta\times\mathbf{x}_\varphi|$; dot products with $N$ give $e, f, g_\mathrm{II}$; the formula $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$ assembles the answer.

**Key decision point:** Choose the right coordinates. Spherical coordinates are ideal because the rotational symmetry forces $F = 0$ and the metric components depend only on $\theta$ (not on $\varphi$). In stereographic coordinates, the formula would also work but the algebra is uglier (the metric has a conformal factor $1/(1 + r^2/4a^2)^2$ or similar). Recognising that "rotational symmetry $\Rightarrow$ use polar-style coordinates" is the key insight that simplifies the problem.

---

# Legal Operations Used

1. **Operation 1 from the topic page (compute $(g_{\alpha\beta}, b_{\alpha\beta})$ from a parametrisation):** Compute $\mathbf{x}_\theta, \mathbf{x}_\varphi$ and dot products to get $E, F, G$; compute $\mathbf{x}_{\theta\theta}, \mathbf{x}_{\theta\varphi}, \mathbf{x}_{\varphi\varphi}$ and dot products with $N$ to get $e, f, g_\mathrm{II}$. This is the entire computational mechanic, applied directly.

2. **Operation 2 from the topic page (determinant ratio formula):** Once the fundamental forms' components are in hand, $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$ assembles the result mechanically.

---

# Hints

> [!note]- Hint 1
> Compute the tangent vectors $\mathbf{x}_\theta$ and $\mathbf{x}_\varphi$ first. Notice that the rotational symmetry implies $\langle\mathbf{x}_\theta, \mathbf{x}_\varphi\rangle = 0$ for spherical coordinates — so $F = 0$ and the metric is diagonal.

> [!note]- Hint 2
> The unit normal at $\mathbf{x}(\theta, \varphi) \in S^2_a$ is the outward radial direction: $N(\theta, \varphi) = \mathbf{x}(\theta, \varphi)/a$. So computing $N$ doesn't require the cross product — you can just normalise the position vector.

> [!note]- Hint 3
> For the second derivatives, you should find $\mathbf{x}_{\theta\theta} = -\mathbf{x}$, $\mathbf{x}_{\varphi\varphi} = -a\sin\theta(\sin\theta\cos\varphi, \sin\theta\sin\varphi, 0)$ (perpendicular to the $z$-axis), and $\mathbf{x}_{\theta\varphi}$ orthogonal to the radial direction (zero dot product with $N$).

---

# Solution

The proof breaks into three computational steps. Step 1 computes the first fundamental form via the inner products of tangent vectors. Step 2 computes the unit normal and the second fundamental form via dot products of second-derivative vectors with the normal. Step 3 assembles $K$ via the determinant-ratio formula.

**Step 1: Compute the first fundamental form $\mathrm{I} = a^2\, d\theta^2 + a^2\sin^2\theta\, d\varphi^2$.**

> [!note]- Derivation
> The tangent vectors are
> $$
> \mathbf{x}_\theta = (a\cos\theta\cos\varphi, a\cos\theta\sin\varphi, -a\sin\theta),
> $$
> $$
> \mathbf{x}_\varphi = (-a\sin\theta\sin\varphi, a\sin\theta\cos\varphi, 0).
> $$
> Compute the inner products:
> $$
> E = \langle\mathbf{x}_\theta, \mathbf{x}_\theta\rangle = a^2\cos^2\theta\cos^2\varphi + a^2\cos^2\theta\sin^2\varphi + a^2\sin^2\theta = a^2(\cos^2\theta + \sin^2\theta) = a^2,
> $$
> $$
> G = \langle\mathbf{x}_\varphi, \mathbf{x}_\varphi\rangle = a^2\sin^2\theta\sin^2\varphi + a^2\sin^2\theta\cos^2\varphi = a^2\sin^2\theta,
> $$
> $$
> F = \langle\mathbf{x}_\theta, \mathbf{x}_\varphi\rangle = -a^2\sin\theta\cos\theta\sin\varphi\cos\varphi + a^2\sin\theta\cos\theta\sin\varphi\cos\varphi = 0.
> $$
> Hence $\mathrm{I} = a^2 d\theta^2 + a^2\sin^2\theta\, d\varphi^2$, and $\det g_{\alpha\beta} = a^4\sin^2\theta$.

**Step 2: Compute the second fundamental form $\mathrm{II} = -a\, d\theta^2 - a\sin^2\theta\, d\varphi^2$.**

> [!note]- Derivation
> The unit normal (outward) at $\mathbf{x}(\theta, \varphi)$ is $N(\theta, \varphi) = \mathbf{x}(\theta, \varphi)/a = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ (because $|\mathbf{x}| = a$ on the sphere).
>
> Second derivatives:
> $$
> \mathbf{x}_{\theta\theta} = (-a\sin\theta\cos\varphi, -a\sin\theta\sin\varphi, -a\cos\theta) = -\mathbf{x},
> $$
> $$
> \mathbf{x}_{\varphi\varphi} = (-a\sin\theta\cos\varphi, -a\sin\theta\sin\varphi, 0),
> $$
> $$
> \mathbf{x}_{\theta\varphi} = (-a\cos\theta\sin\varphi, a\cos\theta\cos\varphi, 0).
> $$
> Dot with $N = \mathbf{x}/a$:
> $$
> e = \langle\mathbf{x}_{\theta\theta}, N\rangle = \langle -\mathbf{x}, \mathbf{x}/a\rangle = -|\mathbf{x}|^2/a = -a^2/a = -a.
> $$
> For $f = \langle\mathbf{x}_{\theta\varphi}, N\rangle$: $\mathbf{x}_{\theta\varphi} = a\cos\theta(-\sin\varphi, \cos\varphi, 0)$ has zero $z$-component, and $N = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ has nonzero $z$-component but vanishes against $\mathbf{x}_{\theta\varphi}$ in the $z$-direction; the $xy$-projection of $\mathbf{x}_{\theta\varphi}$ is $a\cos\theta(-\sin\varphi, \cos\varphi)$, perpendicular to the $xy$-projection of $N$ which is $\sin\theta(\cos\varphi, \sin\varphi)$. The inner product of two perpendicular vectors is $0$, so $f = 0$.
>
> Explicit check: $\langle\mathbf{x}_{\theta\varphi}, N\rangle = (-a\cos\theta\sin\varphi)(\sin\theta\cos\varphi) + (a\cos\theta\cos\varphi)(\sin\theta\sin\varphi) + 0 \cdot\cos\theta = -a\sin\theta\cos\theta\sin\varphi\cos\varphi + a\sin\theta\cos\theta\sin\varphi\cos\varphi = 0$.
>
> For $g_\mathrm{II} = \langle\mathbf{x}_{\varphi\varphi}, N\rangle$: $\mathbf{x}_{\varphi\varphi} = -a\sin\theta(\cos\varphi, \sin\varphi, 0)$. Dotting with $N$: $-a\sin\theta\cos\varphi\cdot\sin\theta\cos\varphi - a\sin\theta\sin\varphi\cdot\sin\theta\sin\varphi + 0\cdot\cos\theta = -a\sin^2\theta(\cos^2\varphi + \sin^2\varphi) = -a\sin^2\theta$.
>
> Hence $\mathrm{II} = -a\, d\theta^2 - a\sin^2\theta\, d\varphi^2$, and $\det b_{\alpha\beta} = a^2\sin^2\theta$.

**Step 3: Compute $K = 1/a^2$.**

> [!note]- Derivation
> $K = \det b_{\alpha\beta}/\det g_{\alpha\beta} = (a^2\sin^2\theta)/(a^4\sin^2\theta) = 1/a^2$.
>
> This is the Gauss curvature at every point of the sphere of radius $a$ — constant, positive, equal to $1/a^2$, independent of the specific point (a manifestation of the spherical symmetry).

> [!note]- Complete formal solution
> Parametrise $S^2_a$ in spherical coordinates by $\mathbf{x}(\theta, \varphi) = (a\sin\theta\cos\varphi, a\sin\theta\sin\varphi, a\cos\theta)$ with $\theta \in (0, \pi)$, $\varphi \in [0, 2\pi)$.
>
> The tangent vectors are $\mathbf{x}_\theta = (a\cos\theta\cos\varphi, a\cos\theta\sin\varphi, -a\sin\theta)$ and $\mathbf{x}_\varphi = (-a\sin\theta\sin\varphi, a\sin\theta\cos\varphi, 0)$. Direct computation of inner products gives $E = a^2$, $F = 0$, $G = a^2\sin^2\theta$, so $\det g_{\alpha\beta} = a^4\sin^2\theta$.
>
> The outward unit normal is $N(\theta, \varphi) = \mathbf{x}/a = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$.
>
> The second derivatives are $\mathbf{x}_{\theta\theta} = -\mathbf{x}$, $\mathbf{x}_{\theta\varphi} = (-a\cos\theta\sin\varphi, a\cos\theta\cos\varphi, 0)$, and $\mathbf{x}_{\varphi\varphi} = (-a\sin\theta\cos\varphi, -a\sin\theta\sin\varphi, 0)$.
>
> Dotting with $N$: $e = \langle\mathbf{x}_{\theta\theta}, N\rangle = \langle -\mathbf{x}, \mathbf{x}/a\rangle = -a$; $f = \langle\mathbf{x}_{\theta\varphi}, N\rangle = 0$ (direct computation of the dot product cancels); $g_\mathrm{II} = \langle\mathbf{x}_{\varphi\varphi}, N\rangle = -a\sin^2\theta$.
>
> Hence $\det b_{\alpha\beta} = eg_\mathrm{II} - f^2 = (-a)(-a\sin^2\theta) - 0 = a^2\sin^2\theta$.
>
> The Gauss curvature is $K = \det b_{\alpha\beta}/\det g_{\alpha\beta} = (a^2\sin^2\theta)/(a^4\sin^2\theta) = 1/a^2$, constant.
>
> Note: the principal curvatures are $\kappa_1 = e/E = -1/a$ and $\kappa_2 = g_\mathrm{II}/G = -a\sin^2\theta/(a^2\sin^2\theta) = -1/a$, both equal to $-1/a$ (Frankel's outward-normal convention gives negative values). The sphere is umbilic everywhere ($\kappa_1 = \kappa_2$), consistent with the spherical symmetry.

> [!tip] Sanity check via Theorema Egregium
> One can verify by computing $R_{1212}$ from the Christoffel symbols of $g_{\alpha\beta}$ alone, without reference to the embedding. The Christoffel symbols of $\mathrm{I} = a^2 d\theta^2 + a^2\sin^2\theta\, d\varphi^2$ are $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$ (others zero). Direct computation gives $R^\theta_{\;\varphi\theta\varphi} = \sin^2\theta$, hence $R_{\theta\varphi\theta\varphi} = g_{\theta\theta}R^\theta_{\;\varphi\theta\varphi} = a^2\sin^2\theta$. And $\det g = a^4\sin^2\theta$. So $K = R_{1212}/\det g = (a^2\sin^2\theta)/(a^4\sin^2\theta) = 1/a^2$, matching the extrinsic computation. This is Theorema Egregium in action.

---

# Key Takeaways

**The six-step computational mechanic.** The routine "first derivatives → first fundamental form, second derivatives + unit normal → second fundamental form, determinant ratio → Gauss curvature" is the universal pattern for direct computation of $K$ on parametrised surfaces. The mechanic uses only multivariable calculus and basic linear algebra; the algorithm is automatic, and a parametrisation always gives a well-defined Gauss curvature at regular points. This is the bread-and-butter calculation of classical surface theory, and one should be able to execute it cleanly on a new surface within minutes.

**Symmetry simplifies the computation dramatically.** Spherical coordinates exploit the rotational symmetry of $S^2_a$ around the $z$-axis: the coordinate vector $\mathbf{x}_\varphi$ is orthogonal to $\mathbf{x}_\theta$ everywhere (so $F = 0$), and the metric components depend only on $\theta$ (not $\varphi$). This makes the algebra tractable. For a surface without such symmetry (a generic ellipsoid, say), the off-diagonal term $F$ is nonzero and the formulas are much messier. The lesson: when a surface has a continuous symmetry, choose coordinates adapted to the symmetry, and the metric becomes diagonal or simpler.

**The unit normal on a sphere is the radial direction.** On the sphere of radius $a$, the outward unit normal at $p$ is just $p/a$ — the *position vector* normalised. This is a special feature of spheres centred at the origin: the position vector is automatically normal. Other surfaces require computing $\mathbf{x}_u\times\mathbf{x}_v$ and normalising; spheres avoid this. The corresponding formula for the shape operator simplifies: $S = -dN = -(\partial p/a)/\partial p\cdot dp = -\mathrm{Id}/a$, which immediately gives $\kappa_1 = \kappa_2 = -1/a$ (with the outward normal). Recognising "for a sphere, the normal is radial" is a useful shortcut, applicable also to balls and spherical caps.

**The constant Gauss curvature $K = 1/a^2$ is the calibration example of all of surface theory.** Every text uses this example to introduce $K$, and it is the simplest case where $K$ is positive (and so any positive-curvature behaviour can be compared to it). The sphere of radius $a$ has $K = 1/a^2$, $H = -2/a$ (Frankel; or $-1/a$ with the average convention), area $4\pi a^2$, Gauss–Bonnet integral $\int K\, dA = K\cdot\mathrm{Area} = (1/a^2)\cdot 4\pi a^2 = 4\pi = 2\pi\chi(S^2)$ — consistent. Internalising this single example gives the calibration for all of curvature theory.

**Companion exercises:** Compare with [[Ex - Gauss Curvature of the Pseudosphere is -1]] (constant negative curvature, the hyperbolic analogue) and [[Ex - The Catenoid is a Minimal Surface]] (minimal surface, $H = 0$ but $K = -1/(a^2\cosh^4)$ variable negative). Together these three exercises calibrate intuition for positive, negative-constant, and variable-negative Gauss curvature on simple surfaces.
