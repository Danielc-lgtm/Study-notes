---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Integral of a Compactly Supported Form on a Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Thm - Change of Variables for Integration on Manifolds"
tags: [geometry, differential-geometry, integration, sphere, parametrization]
---

# Problem Statement

Let $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$ be the standard area 2-form on $\mathbb{R}^3$ restricted to the unit sphere $S^2 \subseteq \mathbb{R}^3$, where $S^2$ carries the standard outward-normal orientation.

Using the spherical-coordinate parametrization $F : (0, \pi) \times (0, 2\pi) \to S^2$ defined by $F(\varphi, \theta) = (\sin\varphi\cos\theta, \sin\varphi\sin\theta, \cos\varphi)$:

(a) Verify that $F$ restricts to an orientation-preserving [[Def - Diffeomorphism|diffeomorphism]] onto its image (which is $S^2$ minus a measure-zero set).

(b) Compute the pullback $F^*\omega$.

(c) Compute $\int_{S^2}\omega$ using [[Thm - Change of Variables for Integration on Manifolds#Statement|the integration-over-parametrizations formula]].

**Recall:**

A smooth manifold integral is defined chart-by-chart with the change-of-variables formula:

![[Thm - Change of Variables for Integration on Manifolds#Statement]]

The pullback of forms by a smooth map $F : N \to M$ satisfies $F^*(\alpha\wedge\beta) = F^*\alpha\wedge F^*\beta$ and $F^*(df) = d(f\circ F)$.

The standard orientation of $S^n \subseteq \mathbb{R}^{n+1}$ is the one determined by the outward-normal-first convention, as established in [[Ex - The Sphere is Orientable but the Möbius Strip is Not]].

---

# Convergent Strategy

**Problem class:** Direct integration of a top-form on a manifold via parametrization — the most basic kind of problem in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|the topic]]. It routes through the integration-over-parametrizations formula to convert a manifold integral into an ordinary multivariable Riemann integral.

**Assumption pattern:** The sphere has an explicit global-up-to-measure-zero parametrization (spherical coordinates), and the 2-form $\omega$ is given explicitly on the ambient $\mathbb{R}^3$. This is the cleanest setup possible — no partitions of unity needed, just one parametrization. The orientation question reduces to checking the sign of the Jacobian of an explicit map.

**Theorem routing:** [[Thm - Change of Variables for Integration on Manifolds]] part (c) — the integration-over-parametrizations formula — converts the manifold integral $\int_{S^2}\omega$ into the Riemann integral $\int_D F^*\omega$, where $D = (0, \pi)\times(0, 2\pi)$ is the parameter domain. The pullback computation $F^*\omega = \sin\varphi\,d\varphi\wedge d\theta$ then makes the Riemann integral elementary.

**Key decision point:** The choice of spherical coordinates rather than another parametrization (e.g., stereographic projection) is the natural one because the form $\omega$ pulls back to something especially clean — $\sin\varphi\,d\varphi\wedge d\theta$. Stereographic projection would also work but would give a more complicated integrand involving $(1+|x|^2)^{-2}$ factors; the time spent on the pullback computation is the deciding factor.

---

# Legal Operations Used

1. **Operation 1 (pull back to a chart and integrate)** from the [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem#Legal Operations|topic page]]. This is the textbook application: an explicit parametrization $F : D \to S^2$ converts the manifold integral into a Riemann integral $\int_D F^*\omega$.

2. **Operation 8 (verify orientation-preservation via the sign of $\det DF$)** from the topic page. In part (a) we compute the Jacobian of an associated 3D map (the radial extension of $F$) to confirm orientation-preservation.

3. **Operation 4 (use the Riemannian volume formula)** [implicit]. The form $\omega$ restricted to $S^2$ is the Riemannian area form $\omega_g$ for the round metric — the pullback $F^*\omega = \sin\varphi\,d\varphi\wedge d\theta$ is the same as $\sqrt{\det g}\,d\varphi\wedge d\theta$ with $g_{\varphi\varphi} = 1, g_{\theta\theta} = \sin^2\varphi$. The integral over $S^2$ is therefore the surface area.

---

# Hints

> [!note]- Hint 1
> Compute $F^*(dx), F^*(dy), F^*(dz)$ first, using $F^*(dx^i) = d(x^i\circ F)$. Then wedge them in the combinations appearing in $\omega$.

> [!note]- Hint 2
> The orientation of $F$ is checked via Lemma 15.27 of Lee (or by direct calculation): consider the radial extension $\widetilde F(\rho, \varphi, \theta) = (\rho\sin\varphi\cos\theta, \rho\sin\varphi\sin\theta, \rho\cos\varphi)$ on $(0, \infty)\times(0,\pi)\times(0, 2\pi)$. Compute $\det D\widetilde F = \rho^2\sin\varphi > 0$. The restriction to $\rho = 1$ is $F$, and orientation is preserved.

> [!note]- Hint 3
> When computing $F^*\omega$, lots of terms will appear with $d\varphi\wedge d\varphi = 0$ or $d\theta\wedge d\theta = 0$. Be systematic: for each term in $\omega$, expand $F^*(dx)\wedge F^*(dy)$ etc., and collect.

> [!note]- Hint 4
> The final answer is $\int_{S^2}\omega = 4\pi$, which is the surface area of $S^2$. The integral $\int_0^\pi\int_0^{2\pi}\sin\varphi\,d\theta\,d\varphi$ is a routine multivariable integral.

---

# Solution

The proof breaks into three steps. **Step 1** verifies orientation-preservation by computing the radial-extension Jacobian. **Step 2** computes the pullback $F^*\omega$, the bulk of the algebra. **Step 3** performs the elementary Riemann integral to get $4\pi$.

**Step 1: Verify orientation-preservation.**

We verify that $F : D \to S^2$ (where $D = (0, \pi)\times(0, 2\pi)$) is orientation-preserving by appealing to the radial extension. Define $\widetilde F : (0, \infty)\times D \to \mathbb{R}^3\setminus\{0\}$ by
$$\widetilde F(\rho, \varphi, \theta) = (\rho\sin\varphi\cos\theta, \rho\sin\varphi\sin\theta, \rho\cos\varphi).$$
This is a [[Def - Diffeomorphism|diffeomorphism]] onto its image (the punctured 3-space minus the half-plane $\{y = 0, x \geq 0\}$).

> [!note]- Derivation
> Compute the Jacobian matrix:
> $$D\widetilde F = \begin{pmatrix}\sin\varphi\cos\theta & \rho\cos\varphi\cos\theta & -\rho\sin\varphi\sin\theta \\ \sin\varphi\sin\theta & \rho\cos\varphi\sin\theta & \rho\sin\varphi\cos\theta \\ \cos\varphi & -\rho\sin\varphi & 0\end{pmatrix}.$$
> Expanding along the third row:
> $$\det D\widetilde F = \cos\varphi\big(\rho^2\cos\varphi\cos^2\theta\sin\varphi + \rho^2\cos\varphi\sin^2\theta\sin\varphi\big) + \rho\sin\varphi\big(\rho\sin^2\varphi\cos^2\theta + \rho\sin^2\varphi\sin^2\theta\big),$$
> $$= \rho^2\sin\varphi\cos^2\varphi + \rho^2\sin^3\varphi = \rho^2\sin\varphi(\cos^2\varphi + \sin^2\varphi) = \rho^2\sin\varphi.$$
> For $\rho > 0$ and $\varphi \in (0, \pi)$ (so $\sin\varphi > 0$), $\det D\widetilde F > 0$. So $\widetilde F$ is orientation-preserving.
>
> By Lee's Lemma 15.27, the restriction of an orientation-preserving radial extension to $\rho = 1$ gives an orientation-preserving parametrization of the sphere with the outward-normal orientation. Hence $F$ is orientation-preserving.

**Step 2: Compute the pullback $F^*\omega$.**

We pull back $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$. First compute the pullbacks of $dx, dy, dz$:
$$F^*(dx) = d(\sin\varphi\cos\theta) = \cos\varphi\cos\theta\,d\varphi - \sin\varphi\sin\theta\,d\theta,$$
$$F^*(dy) = d(\sin\varphi\sin\theta) = \cos\varphi\sin\theta\,d\varphi + \sin\varphi\cos\theta\,d\theta,$$
$$F^*(dz) = d(\cos\varphi) = -\sin\varphi\,d\varphi.$$

Then compute the pullbacks of the three wedge-products:
$$F^*(dy\wedge dz) = F^*(dy)\wedge F^*(dz) = (\cos\varphi\sin\theta\,d\varphi + \sin\varphi\cos\theta\,d\theta)\wedge(-\sin\varphi\,d\varphi)$$
$$= -\sin\varphi(\sin\varphi\cos\theta\,d\theta\wedge d\varphi) = \sin^2\varphi\cos\theta\,d\varphi\wedge d\theta.$$

$$F^*(dz\wedge dx) = F^*(dz)\wedge F^*(dx) = (-\sin\varphi\,d\varphi)\wedge(\cos\varphi\cos\theta\,d\varphi - \sin\varphi\sin\theta\,d\theta)$$
$$= -\sin\varphi\cdot(-\sin\varphi\sin\theta)\,d\varphi\wedge d\theta = \sin^2\varphi\sin\theta\,d\varphi\wedge d\theta.$$

$$F^*(dx\wedge dy) = F^*(dx)\wedge F^*(dy) = (\cos\varphi\cos\theta\,d\varphi - \sin\varphi\sin\theta\,d\theta)\wedge(\cos\varphi\sin\theta\,d\varphi + \sin\varphi\cos\theta\,d\theta)$$
$$= \cos\varphi\cos\theta\cdot\sin\varphi\cos\theta\,d\varphi\wedge d\theta - \sin\varphi\sin\theta\cdot\cos\varphi\sin\theta\,d\theta\wedge d\varphi$$
$$= \sin\varphi\cos\varphi\cos^2\theta\,d\varphi\wedge d\theta + \sin\varphi\cos\varphi\sin^2\theta\,d\varphi\wedge d\theta$$
$$= \sin\varphi\cos\varphi\,d\varphi\wedge d\theta.$$

> [!note]- Derivation
> Each pullback is computed by writing $F^*$ as a linear combination of $d\varphi$ and $d\theta$, then wedging. Terms with repeated $d\varphi$ or $d\theta$ vanish. The standard $d\theta\wedge d\varphi = -d\varphi\wedge d\theta$ convention is used.

Now assemble:
$$F^*\omega = (F^*x)F^*(dy\wedge dz) + (F^*y)F^*(dz\wedge dx) + (F^*z)F^*(dx\wedge dy)$$
$$= \sin\varphi\cos\theta\cdot\sin^2\varphi\cos\theta + \sin\varphi\sin\theta\cdot\sin^2\varphi\sin\theta + \cos\varphi\cdot\sin\varphi\cos\varphi\quad(\text{coefficient of }d\varphi\wedge d\theta)$$
$$= \sin^3\varphi\cos^2\theta + \sin^3\varphi\sin^2\theta + \sin\varphi\cos^2\varphi$$
$$= \sin^3\varphi + \sin\varphi\cos^2\varphi = \sin\varphi(\sin^2\varphi + \cos^2\varphi) = \sin\varphi.$$

Therefore,
$$F^*\omega = \sin\varphi\,d\varphi\wedge d\theta.$$

> [!note]- Derivation
> Adding the three terms:
> - $x$ contribution: $\sin\varphi\cos\theta\cdot\sin^2\varphi\cos\theta = \sin^3\varphi\cos^2\theta$.
> - $y$ contribution: $\sin\varphi\sin\theta\cdot\sin^2\varphi\sin\theta = \sin^3\varphi\sin^2\theta$.
> - $z$ contribution: $\cos\varphi\cdot\sin\varphi\cos\varphi = \sin\varphi\cos^2\varphi$.
> Sum: $\sin^3\varphi(\cos^2\theta + \sin^2\theta) + \sin\varphi\cos^2\varphi = \sin^3\varphi + \sin\varphi\cos^2\varphi = \sin\varphi$.

**Step 3: Compute the integral.**

By [[Thm - Change of Variables for Integration on Manifolds#Statement|the integration-over-parametrizations formula]], since $F : D \to S^2 \setminus (\text{measure-zero set})$ is an orientation-preserving diffeomorphism onto an open dense subset of measure-zero complement,
$$\int_{S^2}\omega = \int_D F^*\omega = \int_0^{2\pi}\int_0^\pi\sin\varphi\,d\varphi\,d\theta.$$

> [!note]- Derivation
> Compute the iterated integral:
> $$\int_0^\pi\sin\varphi\,d\varphi = [-\cos\varphi]_0^\pi = -(-1) - (-1) = 2.$$
> $$\int_0^{2\pi}\int_0^\pi\sin\varphi\,d\varphi\,d\theta = \int_0^{2\pi}2\,d\theta = 4\pi.$$
>
> The image of $F$ is $S^2$ minus the half-meridian $\{(x, y, z) \in S^2 : y = 0, x \geq 0\}$, which is a 1-dimensional set (a curve) and has measure zero on $S^2$. So the parametrization-integral formula applies.

Hence $\int_{S^2}\omega = 4\pi$, which is the surface area of the unit 2-sphere.

> [!note]- Complete formal solution
> **Setup.** $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$, $F(\varphi, \theta) = (\sin\varphi\cos\theta, \sin\varphi\sin\theta, \cos\varphi)$ on $D = (0, \pi)\times(0, 2\pi)$.
>
> **Orientation-preservation.** The radial extension $\widetilde F(\rho, \varphi, \theta) = \rho\cdot F(\varphi, \theta)$ has Jacobian $\det D\widetilde F = \rho^2\sin\varphi > 0$ on $(0, \infty)\times D$, so $\widetilde F$ is orientation-preserving. By Lee's Lemma 15.27, $F$ — the restriction to $\rho = 1$ — is also orientation-preserving onto $S^2$ with the standard outward-normal orientation.
>
> **Pullback.** $F^*(dx) = \cos\varphi\cos\theta\,d\varphi - \sin\varphi\sin\theta\,d\theta$, $F^*(dy) = \cos\varphi\sin\theta\,d\varphi + \sin\varphi\cos\theta\,d\theta$, $F^*(dz) = -\sin\varphi\,d\varphi$. Wedge:
> $$F^*(dy\wedge dz) = \sin^2\varphi\cos\theta\,d\varphi\wedge d\theta, \quad F^*(dz\wedge dx) = \sin^2\varphi\sin\theta\,d\varphi\wedge d\theta, \quad F^*(dx\wedge dy) = \sin\varphi\cos\varphi\,d\varphi\wedge d\theta.$$
> Combining:
> $$F^*\omega = (\sin^3\varphi\cos^2\theta + \sin^3\varphi\sin^2\theta + \sin\varphi\cos^2\varphi)\,d\varphi\wedge d\theta = \sin\varphi\,d\varphi\wedge d\theta.$$
>
> **Integration.** By the parametrization formula,
> $$\int_{S^2}\omega = \int_D F^*\omega = \int_0^{2\pi}\int_0^\pi\sin\varphi\,d\varphi\,d\theta = \int_0^{2\pi}2\,d\theta = 4\pi.$$
> $\blacksquare$

**Sanity-check via independent route.** The form $\omega$ restricted to $S^2$ is the area form for the standard round metric (Lee's Example 15.22; this can also be seen directly: $\omega = \iota_\nu(dx\wedge dy\wedge dz)$ for $\nu = x\partial_x + y\partial_y + z\partial_z$ the position vector, which equals the Riemannian volume form for the round metric induced from $\mathbb{R}^3$). So $\int_{S^2}\omega = \mathrm{Area}(S^2) = 4\pi$, consistent with the classical surface-area formula for the unit sphere.

---

# Key Takeaways

**The integration-over-parametrizations formula is the practical face of the chart-by-chart definition.** Whenever you have a manifold and an explicit smooth parametrization $F : D \to M$ that is orientation-preserving onto an open dense subset, the integral on $M$ is just the multivariable Riemann integral of the pullback on $D$. This converts what looks like a "manifold integral" into something computable in elementary calculus. The trigger for this technique is *the existence of an explicit parametrization*, and the action is to pull back the integrand and evaluate. The Möbius strip, projective spaces, and other complex manifolds may not admit a single global parametrization; for those, one uses a partition of unity or breaks the manifold into pieces with measure-zero overlap.

**Spherical coordinates make the area form clean: $F^*\omega = \sin\varphi\,d\varphi\wedge d\theta$.** This is one of the most-used pullback identities in differential geometry. It says the area element on the sphere in spherical coordinates is $\sin\varphi\,d\varphi\,d\theta$ — the factor $\sin\varphi$ comes from the geometry (latitudes shrink to points at the poles) and is the same as $\sqrt{\det g_{ij}}$ for the round metric in these coordinates ($g_{\varphi\varphi} = 1, g_{\theta\theta} = \sin^2\varphi, g_{\varphi\theta} = 0$). The takeaway: whenever you see "area on a surface in spherical coordinates", $\sin\varphi$ should be automatic.

**Lee's Lemma 15.27 trick: orientation-checking via radial extension.** Verifying that a parametrization of an embedded hypersurface is orientation-preserving can be tedious if done by computing the Jacobian on the hypersurface directly. A clean trick: extend radially (or by any transverse vector field) to a parametrization of an open neighborhood of the hypersurface in the ambient manifold, and check that the extended Jacobian is positive. This reduces the question to an ordinary 3D (or $(n+1)$-D) determinant computation. The technique applies whenever the hypersurface has a clean transverse parametrization extension — which is the case for any embedded hypersurface in Euclidean space.

**Companion exercises.** This is the "compute an integral over a sphere" warm-up; [[Ex - Volume of the n-Sphere via the Volume Form]] generalizes to $S^n$ and the $n$-dimensional volume; [[Ex - Stokes' Theorem Recovers Green's Theorem on R^2]] shows the planar analog with Stokes (rather than direct parametrization) as the route. Together, these three exercises drill the core computational techniques of manifold integration.
