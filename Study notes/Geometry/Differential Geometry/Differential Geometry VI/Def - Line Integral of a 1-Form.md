---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covector Field and Differential 1-Form"
  - "Def - Pullback of a Covector Field"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Tangent Space"
tags: [geometry, differential-geometry, line-integral, 1-form]
---

# Notation

$M$ is a smooth manifold, $\omega \in \Omega^1(M)$ is a smooth 1-form on $M$. The integration curve is a piecewise smooth map $\gamma : [a, b] \to M$, with velocity $\gamma'(t) \in T_{\gamma(t)}M$ the tangent vector to the curve at parameter $t$. The line integral is denoted $\int_\gamma \omega$, with value in $\mathbb{R}$. For a closed curve (loop), $\gamma(a) = \gamma(b)$. For a piecewise smooth path that is the concatenation $\gamma = \gamma_1 + \gamma_2$ of two paths, $\int_{\gamma_1 + \gamma_2} \omega = \int_{\gamma_1} \omega + \int_{\gamma_2} \omega$.

---

# Axiom Motivation

The line integral of a 1-form is the manifold-native version of the classical line integral $\int_\gamma \mathbf{F} \cdot d\mathbf{r}$ from vector calculus. The motivation is to define an integral of a "field" along a "path" in a way that (a) makes intrinsic sense on a manifold (no metric, no coordinates), (b) generalizes the classical case correctly on Euclidean space, and (c) enjoys all the natural invariances and combinatorial properties one expects of an integral.

The classical formulation has two parts: a force field $\mathbf{F}$ on Euclidean space and a curve $\gamma$. The work integral is $\int_\gamma \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\gamma(t)) \cdot \gamma'(t) \, dt$, where $\mathbf{F}(\gamma(t)) \cdot \gamma'(t)$ is a scalar (the dot product of two vectors). On a manifold without a metric, the dot product is unavailable — but the *pairing of a covector with a tangent vector* is, and it is exactly the right replacement.

So the natural definition: replace $\mathbf{F} \cdot d\mathbf{r}$ by $\omega(\gamma'(t))$, where $\omega$ is a 1-form (the cotangent-bundle generalization of $\mathbf{F}$). This pairing produces a smooth real-valued function of $t$, and we integrate it over $[a, b]$ by ordinary Riemann (or Lebesgue) integration:
$$\int_\gamma \omega := \int_a^b \omega_{\gamma(t)}(\gamma'(t)) \, dt.$$

The integrand is the pointwise pairing of a covector (at the point $\gamma(t) \in M$) with a tangent vector (at the same point $\gamma(t)$), so it lives in $\mathbb{R}$, and as $t$ varies it gives a smooth function $[a, b] \to \mathbb{R}$ (smooth because $\omega$ is smooth in $p$, $\gamma$ is smooth in $t$, and $\gamma'(t)$ depends smoothly on $t$).

This definition has three essential properties.

**Invariance under reparameterization.** If $\sigma : [c, d] \to [a, b]$ is an orientation-preserving diffeomorphism and $\tilde\gamma = \gamma \circ \sigma$, then $\int_{\tilde\gamma} \omega = \int_\gamma \omega$. This follows from the change-of-variables formula and the chain rule: $\tilde\gamma'(s) = \sigma'(s) \gamma'(\sigma(s))$, so $\omega(\tilde\gamma'(s)) = \sigma'(s) \omega(\gamma'(\sigma(s)))$, and substituting in the integral gives the same result. *Orientation-reversing reparameterization reverses the sign:* $\int_{-\gamma} \omega = -\int_\gamma \omega$.

**Additivity over concatenated paths.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$ (with the endpoint of $\gamma_1$ being the start of $\gamma_2$), then $\int_\gamma \omega = \int_{\gamma_1} \omega + \int_{\gamma_2} \omega$. This is the additivity of the Riemann integral over $[a, c] \cup [c, b] = [a, b]$.

**Naturality under smooth maps.** For $F : M \to N$ smooth and $\omega \in \Omega^1(N)$, $\int_{F \circ \gamma} \omega = \int_\gamma F^*\omega$. This is the change-of-variables formula for differential forms, and it follows from the pullback definition: $(F^*\omega)_{\gamma(t)}(\gamma'(t)) = \omega_{F(\gamma(t))}(dF(\gamma'(t))) = \omega_{(F\circ\gamma)(t)}((F\circ\gamma)'(t))$, so the integrands match.

These three properties characterize the line integral up to a choice of orientation. Together with the **fundamental theorem for exact forms** — $\int_\gamma df = f(\gamma(b)) - f(\gamma(a))$ for any smooth function $f$ — they make the line integral a powerful and computationally flexible tool.

What is forced by demanding $\gamma$ be **piecewise smooth** rather than just continuous? The integrand $\omega(\gamma'(t))$ requires the velocity $\gamma'(t)$ to exist, which requires $\gamma$ to be differentiable. For continuous-but-non-differentiable curves, the integral as defined here does not exist (though variational integrals over $C^0$ paths can be defined using Sobolev-space techniques). Piecewise smoothness is the practical compromise: allowing corners (concatenation of smooth pieces) is needed in many examples (polygonal paths, etc.), and the integral on each piece is well-defined.

What is forced by demanding $\omega$ be **smooth**? Smoothness of $\omega$ ensures the integrand $\omega(\gamma'(t))$ is smooth in $t$ (as a composition of smooth functions), so Riemann integrability is automatic. Continuous-form line integrals can be defined too — the integrand only needs to be integrable.

What is forced by demanding the integrand be the **pointwise pairing**? Linearity of the pairing in both $\omega$ and $\gamma'$ is what makes the line integral $\mathbb{R}$-bilinear in $\omega$ and additive in the curve. Pointwise (not nonlocal) pairing is forced by the structural requirement that the integral should respect coordinate splittings: $\int_\gamma (\omega_i \, dx^i)$ should be $\sum_i \int_\gamma \omega_i \, dx^i$, which it is precisely because the integrand is pointwise.

What if we **strengthened** by demanding $\omega$ be exact, $\omega = df$? Then the line integral has a particularly clean form: $\int_\gamma df = f(\gamma(b)) - f(\gamma(a))$, depending only on endpoints. This is the manifold-native version of the fundamental theorem of calculus, and 1-forms with this property — endpoints-only-dependent integrals — are exactly the exact 1-forms (modulo cohomology).

What if we **weakened** to non-smooth $\gamma$? Then the velocity might not exist pointwise, and the integral as defined fails. Generalizations using $L^p$-spaces and Sobolev-class curves exist but are part of geometric measure theory, not basic differential forms.

---

# The Definition

Let $M$ be a smooth manifold and $\omega \in \Omega^1(M)$ a smooth 1-form. Let $\gamma : [a, b] \to M$ be a piecewise smooth curve.

The **line integral** of $\omega$ along $\gamma$ is
$$\int_\gamma \omega := \int_a^b \omega_{\gamma(t)}\bigl( \gamma'(t) \bigr) \, dt,$$
where $\gamma'(t) \in T_{\gamma(t)}M$ is the velocity of $\gamma$ at parameter $t$, and the integrand $\omega_{\gamma(t)}(\gamma'(t))$ is the pointwise pairing of the covector $\omega_{\gamma(t)}$ with the tangent vector $\gamma'(t)$, producing a piecewise smooth real-valued function of $t$. The right-hand side is the ordinary Riemann integral of this function over $[a, b]$.

Equivalently, $\int_\gamma \omega = \int_{[a,b]} \gamma^*\omega$, where $\gamma^*\omega \in \Omega^1([a, b])$ is the pullback of $\omega$ along $\gamma$ — a 1-form on $[a, b]$, of the form $f(t) dt$ where $f(t) = \omega_{\gamma(t)}(\gamma'(t))$ — and the integral on the right is the ordinary integral $\int_a^b f(t) \, dt$.

**Coordinate expression.** If $\gamma$ lies in a chart $(U, x^i)$ with $\gamma(t) = (x^1(t), \dots, x^n(t))$ and $\omega = \omega_i \, dx^i$ on $U$, then
$$\int_\gamma \omega = \int_a^b \omega_i(\gamma(t)) \cdot \frac{dx^i}{dt}(t) \, dt = \int_a^b \omega_i(\gamma(t)) \cdot \dot{\gamma}^i(t) \, dt.$$
For piecewise smooth $\gamma$, split $[a, b]$ at the corners and sum.

**Key properties.**

- **Reparameterization invariance:** if $\sigma : [c, d] \to [a, b]$ is an orientation-preserving diffeomorphism and $\tilde\gamma = \gamma \circ \sigma$, then $\int_{\tilde\gamma} \omega = \int_\gamma \omega$. Orientation-reversing $\sigma$ gives a sign change. See [[Ex - Line Integral is Independent of Parameterization]].
- **Additivity over concatenation:** $\int_{\gamma_1 + \gamma_2} \omega = \int_{\gamma_1} \omega + \int_{\gamma_2} \omega$ for the concatenation $\gamma_1 + \gamma_2$.
- **Linearity in $\omega$:** $\int_\gamma (c_1 \omega_1 + c_2 \omega_2) = c_1 \int_\gamma \omega_1 + c_2 \int_\gamma \omega_2$.
- **Fundamental theorem for exact forms:** for $\omega = df$ with $f \in C^\infty(M)$, $\int_\gamma df = f(\gamma(b)) - f(\gamma(a))$.
- **Naturality:** for smooth $F : M \to N$, $\int_{F \circ \gamma} \omega = \int_\gamma F^*\omega$.

A 1-form $\omega$ is **conservative** if $\int_\gamma \omega$ depends only on the endpoints $\gamma(a), \gamma(b)$, not on the path. **Exact forms are conservative** (fundamental theorem). The converse is also true: a conservative 1-form on a connected manifold is exact. So "conservative" and "exact" coincide.

---

# Relate to Other Fields / Compression

The line integral is **the natural integral of a 1-form along a $1$-dimensional submanifold** — generalizing to higher-degree forms and higher-dimensional submanifolds via $\int_S \omega^{(k)}$ for $\omega^{(k)} \in \Omega^k$ and $S$ a $k$-dimensional submanifold. The full machinery is developed in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]] and culminates in **Stokes's theorem** $\int_S d\omega = \int_{\partial S} \omega$ — the line integral of a 1-form $\omega$ around the boundary of a 2-dimensional surface $S$ equals the surface integral of $d\omega$ over $S$.

The line integral is also the **manifold version of the work integral** in physics: for a force 1-form $\omega = F_i \, dx^i$ representing the work done per unit displacement, $\int_\gamma \omega$ is the total work done along the path $\gamma$. When $\omega$ is exact, $\omega = -dU$ for a potential energy $U$, and the work is path-independent: $\int_\gamma \omega = U(\gamma(a)) - U(\gamma(b))$. This is the precise statement of conservation of energy in the conservative-force case.

**True name:** the true name of the line integral $\int_\gamma \omega$ is "**the pullback $\gamma^*\omega$ of $\omega$ to $[a, b]$, integrated**". The operational consequence: every line integral is computed by pulling back to $[a, b]$, where it becomes an ordinary Riemann integral. The intrinsic content (independence of parameterization, additivity, naturality) is automatic from the pullback formalism.

A useful slogan: **the line integral $\int_\gamma \omega$ is the manifold's way of pairing a 1-form with a path, and pullback to $[a, b]$ is the universal computational tool**. In particular, every line-integral computation reduces to an integral on the interval — there is no "intrinsic" computation that doesn't go through this reduction.

In **classical mechanics**, line integrals of 1-forms appear everywhere: the action integral $S[\gamma] = \int_\gamma L \, dt$ is a line integral of the Lagrangian 1-form; the work-energy theorem expresses the kinetic energy change as $\int_\gamma F \, dx$ where $F$ is the force 1-form; phase-space trajectories integrate the canonical 1-form $p_i \, dq^i$ to give the action.

In **complex analysis**, contour integrals $\oint_\gamma f(z) dz$ are line integrals of the complex-valued 1-form $f(z) dz$ along a contour in $\mathbb{C}$. Cauchy's integral theorem ($\oint_\gamma f dz = 0$ for $f$ holomorphic, $\gamma$ a contractible loop) is the complex-analytic version of "exact forms have vanishing loop integrals", and the residue theorem (which relates contour integrals to residues at singularities) is the differential-form precursor to de Rham cohomology with singularities.

---

# Examples / Corollaries

**Is an instance — $\int_\gamma df$ for $f \in C^\infty(M)$.** By the fundamental theorem, $\int_\gamma df = f(\gamma(b)) - f(\gamma(a))$. Path-independence is exact.

**Is an instance — work integral on $\mathbb{R}^n$.** For $\omega = F_i \, dx^i$ (a force 1-form) and $\gamma(t)$ a smooth path, $\int_\gamma \omega = \int_a^b F_i(\gamma(t)) \dot\gamma^i(t) dt$, the classical work integral $\int \mathbf{F} \cdot d\mathbf{r}$.

**Is an instance — winding number.** The form $\omega = (x dy - y dx)/(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$ has $\int_\gamma \omega = 2\pi \cdot n(\gamma, 0)$, where $n(\gamma, 0)$ is the winding number of $\gamma$ around the origin. The integer-valued winding number is a topological invariant, and $\omega$ "measures" it.

**Is an instance — straight-line integral.** For $M = \mathbb{R}^2$, $\omega = x \, dy$, and $\gamma(t) = (t, t)$ for $t \in [0, 1]$: $\dot\gamma = (1, 1)$, so $\omega(\dot\gamma) = x \cdot 1 = t$ at parameter $t$, and $\int_\gamma x \, dy = \int_0^1 t \, dt = 1/2$.

**Is an instance — line integral around a closed loop.** For $M = \mathbb{R}^2$, $\omega = -y \, dx + x \, dy$, and $\gamma(t) = (\cos t, \sin t)$, $t \in [0, 2\pi]$ (the unit circle): $\dot\gamma = (-\sin t, \cos t)$, $\omega(\dot\gamma) = -\sin t \cdot (-\sin t) + \cos t \cdot \cos t = 1$, so $\int_\gamma \omega = 2\pi$. Note $\omega = d(\text{angle})$ on a simply connected region, but not globally.

**Is NOT depending on parameterization — reparameterizing a path.** Re-parameterize $\gamma(t) = t$ on $[0, 1]$ to $\tilde\gamma(s) = s^2$ on $[0, 1]$ (covering the same set). For $\omega = dx$: $\int_\gamma dx = \int_0^1 1 \, dt = 1$ and $\int_{\tilde\gamma} dx = \int_0^1 (\partial \tilde\gamma/\partial s) ds = \int_0^1 2s \, ds = 1$. Same answer.

**Is NOT vanishing on closed loops — closed but not exact 1-form.** For $\omega = (x dy - y dx)/(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$ and $\gamma$ the unit circle, $\int_\gamma \omega = 2\pi \neq 0$. Yet $d\omega = 0$. So closed-not-exact 1-forms have nonzero loop integrals, contradicting the naive "closed implies path-independent" intuition.

**Corollary — conservative forms are exact (on connected manifolds).** If $\int_\gamma \omega$ depends only on endpoints for every $\gamma$, define $f(p) := \int_{\gamma_0}^{\gamma_p} \omega$ for any path from a basepoint $p_0$ to $p$. The path-independence makes $f$ well-defined, and $df = \omega$ — see [[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact]].

**Corollary — naturality with pullback.** For smooth $F : M \to N$ and $\omega \in \Omega^1(N)$, $\int_{F\circ\gamma} \omega = \int_\gamma F^*\omega$. This is the change-of-variables formula for 1-forms.

**Corollary — closed loops and exactness.** $\omega$ is exact $\iff$ $\int_\gamma \omega = 0$ for every closed (loop) $\gamma$. The "only if" follows from the fundamental theorem; the "if" follows from constructing the potential function $f$ as above.

**Corollary — Stokes for closed paths.** When $\gamma = \partial S$ for a smooth surface $S \subseteq M$ and $\omega \in \Omega^1(M)$, Stokes's theorem gives $\int_{\partial S} \omega = \int_S d\omega$. So closed-loop integrals of closed 1-forms ($d\omega = 0$) vanish, *unless the loop is not the boundary of a surface* — which is a topological condition on $M$.

**Calibration check.** Compute $\int_\gamma dx + dy$ along the line segment from $(0, 0)$ to $(1, 1)$ in $\mathbb{R}^2$ and confirm the answer is $2$. Verify reparameterization invariance by computing the same integral with the parameterization $\gamma(t) = (t^2, t^2)$. Verify the fundamental theorem $\int_\gamma df = f(\gamma(b)) - f(\gamma(a))$ for $f(x, y) = xy$ and a specific path.

---

# Unlocked by This

> [!tip] Stokes's Theorem on Manifolds *(from Differential Geometry IX)*
> The line integral generalizes to integration of $k$-forms over $k$-dimensional oriented submanifolds, and **Stokes's theorem** $\int_S d\omega = \int_{\partial S} \omega$ ties integration of a $(k+1)$-form on $S$ to integration of the $k$-form on its boundary. For $k = 1$, this is the classical Stokes (curl theorem); for $k = 2$, the divergence theorem; for $k = n - 1$ on a closed manifold, it gives $\int_M d\omega = 0$. The theorem packages many classical integral identities of vector calculus into one differential-form statement.

> [!tip] Path Integral and Action Functional *(from Geometric Mechanics)*
> The **action functional** $S[\gamma] = \int_\gamma L \, dt$ on a space of paths $\gamma : [a, b] \to Q$ is a line integral of the Lagrangian 1-form. Variational calculus on path space, leading to the Euler–Lagrange equations and Hamilton's principle, lives natively as a calculus of line integrals. The whole apparatus of classical field theory and quantum mechanics is built on this foundation.

> [!tip] Holonomy of a Connection *(from Riemannian Geometry / Gauge Theory)*
> Given a connection $\nabla$ on a vector bundle and a loop $\gamma$ in $M$, **parallel transport** around $\gamma$ gives a linear map of the fibre $E_{\gamma(0)} \to E_{\gamma(0)}$ — the **holonomy** of $\nabla$ around $\gamma$. For a flat connection ($\nabla^2 = 0$), the holonomy depends only on the homotopy class of $\gamma$, and the holonomy group is a representation of $\pi_1(M)$. The relation to line integrals: a $U(1)$-connection on a line bundle is locally a 1-form $A$, and the holonomy around a loop is $\exp(i \int_\gamma A)$ — the "phase" of the wavefunction. This is the bridge to the Aharonov–Bohm effect and gauge theory.

> [!tip] Currents and Geometric Measure Theory *(from Analysis)*
> Allowing the curve $\gamma$ to be a more general "rectifiable" object (a current) and $\omega$ to have distributional coefficients gives **currents**, the integral-theoretic generalization of $k$-dimensional submanifolds with multiplicity. Geometric measure theory is the calculus of currents, with applications to soap-film problems, the Plateau problem, and regularity theory for minimal surfaces.
