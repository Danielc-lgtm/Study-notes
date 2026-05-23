---
type: definition
subject: general-relativity
prereqs:
  - "Def - Spacetime Manifold"
  - "Def - Lorentzian Manifold"
  - "Def - Riemannian Metric"
  - "Def - Minkowski Space and the Metric"
tags: [physics, general-relativity, lorentzian-geometry]
---

# Notation

Spacetime $(M, g)$ with signature $(+,-,-,-)$ and $c = G = 1$. In a coordinate chart $(x^0, x^1, x^2, x^3)$ with $x^0 = t$, the metric components are $g_{\mu\nu}(x)$, a symmetric matrix at each event. The full notation registry is on [[General Relativity I — Einstein's Equations and Schwarzschild]]. The "Newtonian potential" $\phi$ is the classical gravitational potential (so that the Newtonian gravitational acceleration is $-\nabla\phi$); we will see that in the weak-field limit, $g_{00} \approx -(1 - 2\phi)$ identifies $\phi$ with half the deviation of $g_{00}$ from $-1$.

---

# Axiom Motivation

The desideratum is to identify, in the apparatus of [[Def - Lorentzian Manifold|Lorentzian geometry]], the geometric object that plays the role Newton's scalar potential $\phi$ played in Newtonian gravity. Newton's gravity has one scalar field, $\phi(x)$, satisfying Poisson's equation $\nabla^2 \phi = 4\pi G \rho$; the gravitational force on a test body is $-\nabla\phi$. In Einstein's theory, we will see this is replaced by **ten** scalar functions — the ten independent components of the symmetric metric tensor $g_{\mu\nu}(x)$. Why ten potentials instead of one?

**The equivalence principle forces the answer.** Einstein's central insight is that a freely-falling observer feels no gravity — the laws of physics in their frame are exactly those of special relativity. This means that the "stage" of physics is no longer fixed Minkowski space but a *locally Minkowskian* manifold: at each event, in a freely-falling frame, the metric is approximately $\eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$. Globally, the metric is a smoothly varying object $g_{\mu\nu}(x)$ that reduces to $\eta$ at each point in adapted coordinates. The full geometric information is contained in $g_{\mu\nu}$ — the *deviations* of the metric from $\eta$ are what carry the gravitational field. Since $g_{\mu\nu}$ is symmetric in its two indices, it has $4 \times 5/2 = 10$ independent components, and these are the **ten metric potentials**.

**Why is $g_{00}$ the Newtonian potential?** This identification is forced by demanding that the relativistic theory reduce to Newton's in the appropriate limit. Consider a slowly-moving test body in a weak gravitational field: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$, and the body has velocity $v \ll c = 1$. The geodesic equation for the body is

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu{}_{\nu\rho} \frac{dx^\nu}{d\tau} \frac{dx^\rho}{d\tau} = 0.$$

At low velocity, the four-velocity components are $u^\mu \approx (1, \vec v)$, and the spatial geodesic equation becomes, to leading order, $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00}$. A direct computation gives $\Gamma^\alpha{}_{00} \approx \frac{1}{2} g^{\alpha\beta} (\partial_\beta g_{00} - \text{small terms})$ for a static metric, so $\ddot x^\alpha \approx -\frac{1}{2} \partial^\alpha g_{00}$. Comparing with Newton's $\ddot x^\alpha = -\partial^\alpha \phi$, we read off $g_{00} = -(1 - 2\phi) + O(\phi^2)$ (with $g_{00} \to -1$ at infinity where $\phi \to 0$). **So $g_{00}$ encodes the Newtonian potential, plus relativistic corrections.**

**What do the other nine components do?** The diagonal spatial components $g_{ii}$ describe the spatial geometry — in the weak-field limit they describe small spatial curvature, contributing for instance the factor-of-2 enhancement of light bending compared to a naive Newtonian estimate. The off-diagonal $g_{0i}$ describe **frame dragging** (also called gravitomagnetism): a rotating massive body (the Earth) drags spacetime around with it, slowly rotating the local inertial frame of a freely-falling observer — confirmed by the Gravity Probe B experiment (2011). The off-diagonal $g_{ij}$ describe shears and the polarisations of **gravitational waves** — the two transverse-traceless polarisations that travel at the speed of light, detected directly by LIGO in 2015. So:

- $g_{00}$: Newtonian potential (the dominant gravitational attraction).
- $g_{0i}$: frame-dragging / gravitomagnetic field (rotational effects).
- $g_{ij}$ diagonal: spatial curvature (corrections to spatial distances).
- $g_{ij}$ off-diagonal: gravitational wave polarisations.

None of the latter nine are visible in Newton's theory — Newton has only $g_{00}$. Their presence is what distinguishes GR from a relativistic upgrade of Newton, and what makes GR a richer theory.

**Why ten? Because gravity is a rank-2 symmetric tensor field, not a scalar.** This is a structural fact about how the field equations must be constructed. If gravity were governed by a scalar potential alone, the source would be a scalar (energy density $\rho$); but in special relativity, energy density is not a Lorentz invariant — it transforms as the $(0,0)$ component of the stress-energy tensor $T_{\mu\nu}$. So the source of gravity is a *symmetric rank-2 tensor*, $T_{\mu\nu}$, with ten independent components; and the gravitational field that responds to it must also be a symmetric rank-2 tensor. The metric $g_{\mu\nu}$ is exactly such a tensor — symmetric, ten components, transforming covariantly. **Scalar gravity would only couple to the trace of $T_{\mu\nu}$, missing momentum and pressure**; **vector gravity** (like Maxwell theory) would couple to a four-vector source, but the source $T_{\mu\nu}$ is rank-2, not rank-1.

**Per-component failure analysis (why all ten components matter):**

(a) *If we kept only $g_{00}$* (scalar gravity, like Nordström's theory): no light bending around the Sun (the prediction would be only the Newtonian half-value), no frame-dragging, no gravitational waves. Falsified.

(b) *If we kept only $g_{00}$ and $g_{ij}$ diagonal*: get the correct factor-of-2 light bending, but no frame-dragging and no gravitational waves. Misses the rotational and dynamical aspects.

(c) *If we required $g_{0i} = 0$ globally*: cannot describe rotating sources (no Kerr solution, no frame dragging), can only describe static or irrotational spacetimes.

(d) *If we required $g_{ij}$ diagonal globally*: cannot describe gravitational waves, anisotropic spatial geometries, or most realistic dynamical spacetimes.

The full tensor structure is needed for GR to capture all the relevant physics; reducing it amputates predictions.

---

# The Definition

> **Definition (Metric potentials).** In a spacetime $(M, g)$ in a coordinate chart $(x^\mu)$, the **metric potentials** are the ten independent components $g_{\mu\nu}(x)$ of the symmetric Lorentzian metric tensor. The **line element** is
> $$ds^2 = g_{\mu\nu}\, dx^\mu dx^\nu,$$
> and the metric potentials are the coefficients that appear in this expression. They are functions of the coordinates $x^\mu$, smooth where the chart is defined, and define a symmetric matrix $(g_{\mu\nu}(x))$ at each event of signature $(+,-,-,-)$ (with $g_{00} < 0$ in chart coordinates where $\partial_t$ is timelike).

The role of $g_{\mu\nu}$ as gravitational potential is operational: the Christoffel symbols (which generate the "gravitational force" on test bodies via the geodesic equation) are first derivatives of $g_{\mu\nu}$, exactly as the Newtonian force $-\nabla \phi$ is the first derivative of the Newtonian potential. The Riemann tensor (which encodes the tidal forces and is the genuine measure of gravitational field strength) is second derivatives of $g_{\mu\nu}$. So the entire gravitational field — including its dynamics under the Einstein equations — is captured by the metric.

In coordinate-independent form, $g$ is a symmetric $(0,2)$-tensor field on $M$: a smooth section of the bundle $S^2 T^*M$. Its components in a coordinate basis are the $g_{\mu\nu}$.

**Decomposition in the weak-field limit:** Around a flat background, we write
$$g_{\mu\nu}(x) = \eta_{\mu\nu} + h_{\mu\nu}(x), \quad |h_{\mu\nu}| \ll 1,$$
where $\eta = \mathrm{diag}(1,-1,-1,-1)$ is Minkowski and $h_{\mu\nu}$ is the metric perturbation. The components have direct physical interpretations:
- $h_{00} = -2\phi$ where $\phi$ is the Newtonian potential.
- $h_{0i} = A_i$ are the components of a **gravitomagnetic vector potential** (frame-dragging).
- $h_{ij}^{TT}$ (the transverse-traceless part) are the gravitational wave amplitudes.

---

# Relate to Other Fields / Compression

The metric potentials in GR are the analogue of the **vector potential $A_\mu$ of electromagnetism**, with two important differences. First, $A_\mu$ has four components and is a one-form (rank-1 tensor); $g_{\mu\nu}$ has ten components and is a symmetric two-form (rank-2 tensor). Second, $A_\mu$ has $U(1)$ gauge invariance $A_\mu \to A_\mu + \partial_\mu \chi$; $g_{\mu\nu}$ has diffeomorphism invariance $g_{\mu\nu} \to g_{\mu\nu} + \mathcal{L}_\xi g_{\mu\nu}$ where $\xi$ is a vector field generating the diffeomorphism. The gauge invariance reduces the physical degrees of freedom: $A_\mu$ has $4 - 2 = 2$ physical polarisations (transverse photons), and $g_{\mu\nu}$ has $10 - 4 - 4 = 2$ physical polarisations (the two transverse-traceless gravitational wave polarisations, $+$ and $\times$).

**True name:** The metric is *the geometric structure that simultaneously defines distances and times AND encodes the gravitational field*. There is no separation in GR between "the arena" (spacetime) and "the field" (gravity) — they are the same object, the metric $g_{\mu\nu}$. This is the deepest structural innovation of GR, and it is what makes the theory both elegant and difficult: the geometry is dynamical, with its own equations of motion, but it is also the background on which all other physics happens.

The connection to **classical field theory** is direct: the metric is a tensor field on spacetime, like the electromagnetic field $F_{\mu\nu}$ or the gauge fields of the Standard Model, and it satisfies Lagrangian field equations (the Einstein equations from the Hilbert action — see [[Thm - Hilbert's Variational Principle Yields Einstein Equations]]). The conceptual novelty is that this particular tensor field also defines the geometry of the arena in which it lives, leading to the self-coupled nonlinear structure of GR.

---

# Examples / Corollaries

**Is an instance — Minkowski metric in inertial coordinates.** $g_{\mu\nu} = \eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$, constant. No gravity (no curvature); the Christoffel symbols all vanish; geodesics are straight lines in coordinates. This is the flat limit, special relativity.

**Is an instance — Schwarzschild metric in Schwarzschild coordinates.** $g_{tt} = (1 - 2M/r)$, $g_{rr} = -(1 - 2M/r)^{-1}$, $g_{\theta\theta} = -r^2$, $g_{\phi\phi} = -r^2 \sin^2\theta$, all other components zero. The non-trivial $g_{tt}$ encodes the Newtonian potential $\phi = -M/r$ (since $g_{tt} \approx 1 + 2\phi$ in the weak-field limit), and the non-trivial $g_{rr}$ encodes the spatial curvature. No off-diagonal components, since the geometry is static and spherically symmetric.

**Is an instance — Kerr metric for a rotating black hole.** Has nonzero $g_{t\phi}$, the **frame-dragging** component: an observer at rest in the asymptotic frame, dropped near a rotating black hole, will be carried around in the direction of rotation. This off-diagonal term has no Newtonian analogue.

**Is an instance — gravitational wave in TT gauge.** $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}^{TT}$ where $h^{TT}_{ij}$ is the transverse-traceless part of the perturbation, traveling at $c = 1$. The two polarisations $h_+, h_\times$ are encoded in the off-diagonal spatial components.

**Is NOT a metric — a non-symmetric matrix.** A metric must be symmetric ($g_{\mu\nu} = g_{\nu\mu}$); an asymmetric tensor would not give a well-defined inner product. **Einstein–Cartan theory** considers a non-symmetric connection (with torsion), but the metric itself stays symmetric.

**Is NOT a (physical) metric — a tensor of wrong signature.** A positive-definite tensor of signature $(+,+,+,+)$ is a Riemannian metric, not a Lorentzian one — useful for Euclidean quantum gravity (Wick rotation) but not as a physical spacetime metric.

**Is NOT a metric — a degenerate tensor.** A metric must be non-degenerate ($\det g \neq 0$): the bilinear form must have no "null direction" annihilating everything. Degenerate metrics arise in some extended theories (Newton–Cartan gravity has a degenerate temporal metric and a degenerate spatial metric).

**Corollary — units of the metric.** With $g_{\mu\nu}$ dimensionless and $dx^\mu$ in length units, $ds^2$ has units of length-squared, which is appropriate. With the conversion $c = 1$, length and time are the same units; with $G = 1$, mass is also length units (the geometrised mass of the Sun is $\sim 1.5$ km).

**Corollary — number of independent components.** A symmetric $4 \times 4$ matrix has $4 + \binom{4}{2} = 4 + 6 = 10$ independent entries. Of these, $4$ can be set to specified values at any one point (the locally inertial frame, $g_{\mu\nu}(p) = \eta_{\mu\nu}$), so at the level of a single point $g_{\mu\nu}$ has $10 - 10 = 0$ invariants. The invariant content is in the *derivatives* — the curvature tensors.

**Corollary — Christoffel symbols from the metric.** The Levi-Civita connection has components
$$\Gamma^\rho{}_{\mu\nu} = \frac{1}{2} g^{\rho\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}).$$
The Christoffel symbols are *not* tensors (they transform inhomogeneously), but their derivatives combine into the Riemann tensor, which is a genuine tensor.

**Calibration check.** (i) For the Schwarzschild metric, compute $g_{tt}$ at the surface of the Sun ($r \approx 7 \times 10^5$ km, $M_\odot \approx 1.5$ km) and verify $|h_{00}| = 2M/r \sim 4 \times 10^{-6}$ — a very weak field. (ii) Show that $\det g_{\mu\nu}$ for the Schwarzschild metric is $-r^4 \sin^2\theta$, independent of $M$ — this is the volume element's coefficient. (iii) Verify that the Schwarzschild metric, to leading order in $M/r$, is $g \approx \eta + h$ with $h_{tt} = -2M/r$ (matching $\phi = -M/r$ as expected from $h_{tt} = -2\phi$).

---

# Unlocked by This

> [!tip] Frame Dragging and Gravity Probe B *(from Experimental General Relativity)*
> The $g_{0i}$ components of the metric — vanishing in spherically symmetric static spacetimes but nonzero around any rotating mass — encode **frame-dragging**: the inertial frames near a rotating body are slowly rotated relative to those at infinity. **Gravity Probe B** (launched 2004, results 2011) used a satellite with ultra-precise gyroscopes to measure the frame-dragging effect of the rotating Earth — confirmed at the predicted level of $\sim 37$ milliarcseconds per year. The effect scales with the **angular momentum** of the source, not just the mass, and is one of the cleanest tests of the off-diagonal metric components.

> [!tip] Gravitational Waves and LIGO *(from Observational General Relativity)*
> The transverse-traceless $h_{ij}^{TT}$ components of the metric perturbation propagate at the speed of light and carry energy away from accelerating mass distributions (non-spherical, dynamically changing sources). **LIGO** (2015) directly detected the gravitational waves from a binary black hole merger — a strain $h \sim 10^{-21}$ over its 4 km detector arms. Since then, dozens of detections (mergers of black holes and neutron stars) have opened the field of **gravitational wave astronomy**. The two polarisations $h_+$ and $h_\times$ are the two physical degrees of freedom of the metric after gauge-fixing — direct experimental evidence that gravity is described by a *rank-2 tensor* field, not a scalar or vector.

> [!tip] The Cosmological Metric and the Expansion of the Universe *(from Cosmology)*
> The Friedmann–Lemaître–Robertson–Walker metric $ds^2 = dt^2 - a(t)^2 d\sigma^2$ uses a single scale factor $a(t)$ to encode the entire expansion history of the universe. Cosmological observations (cosmic microwave background, large-scale structure, supernovae, baryon acoustic oscillations) determine $a(t)$ and hence the matter content of the universe via the Einstein equations. The **observable universe** has $a$ increasing with time; **dark energy** ($\Lambda$) accelerates this expansion; **inflation** (a very brief de Sitter phase early on) generated the initial conditions. The entire cosmological narrative is encoded in this single function of one variable, derived from the Einstein equations applied to the spatially homogeneous metric ansatz.

> [!tip] ADM Decomposition and Numerical Relativity *(from Computational General Relativity)*
> Splitting the metric into "spatial" and "temporal" parts via the **ADM decomposition** (Arnowitt–Deser–Misner) — with a lapse $N$, shift $N^i$, and spatial metric $h_{ij}$ on each constant-$t$ slice — recasts the Einstein equations as a Hamiltonian system. This is the formulation used in **numerical relativity**, the computational simulation of binary black hole mergers, gravitational wave templates, and other dynamical spacetimes. Until the early 2000s, numerical instabilities plagued these simulations; the **BSSN formulation** (Baumgarte–Shapiro and Shibata–Nakamura, late 1990s) — a reformulation of the evolution equations — finally allowed stable long-time evolution and the first successful binary black hole merger simulations (2005).
