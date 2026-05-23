---
type: definition
subject: general-relativity
prereqs:
  - "Def - Einstein Tensor"
  - "Def - Stress-Energy Tensor"
  - "Def - Spacetime Manifold"
  - "Def - The Metric Tensor as Gravitational Potential"
tags: [physics, general-relativity, field-equations]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$, geometrised units $c = G = 1$ (so the equations read $G_{\mu\nu} = 8\pi T_{\mu\nu}$; to restore units, the right-hand side becomes $8\pi G T_{\mu\nu}/c^4$). The **Einstein tensor** is $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ (see [[Def - Einstein Tensor]]). The **stress-energy tensor** $T_{\mu\nu}$ is the source of the gravitational field (see [[Def - Stress-Energy Tensor]]). Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Axiom Motivation

The desideratum is to write down the equation that relates the geometry of spacetime to its matter content — the relativistic generalisation of Poisson's equation $\nabla^2 \phi = 4\pi G \rho$. Five structural requirements determine the form of the field equations.

**Requirement 1: Covariance under coordinate change.** Physical laws should be expressible in a form that does not single out any particular coordinate system (general covariance, **diffeomorphism invariance**). This forces the field equation to be a tensor equation — both sides must be tensors of the same rank.

**Requirement 2: Match the source.** The relativistic mass-energy density is the $(0,0)$ component of the symmetric stress-energy tensor $T_{\mu\nu}$ — a $(0,2)$-tensor with 10 independent components. So the LHS must be a symmetric $(0,2)$-tensor built from the metric.

**Requirement 3: Built from $g$ and its derivatives up to second order.** Higher-derivative theories generically introduce ghost modes and non-renormalisability (Ostrogradsky), and the Newtonian limit (Poisson, second-order in $\phi$) should be recovered.

**Requirement 4: Local energy-momentum conservation.** Matter satisfies $\nabla^\mu T_{\mu\nu} = 0$ in any reasonable theory. The LHS must therefore be divergence-free: $\nabla^\mu (\text{LHS}_{\mu\nu}) = 0$ identically.

**Requirement 5: Newtonian limit.** In the slow-motion weak-field limit, the equations must reduce to Poisson's equation $\nabla^2 \phi = 4\pi G \rho$ with the correct numerical coefficient.

The first four requirements, by **Lovelock's theorem**, force the LHS to be of the form $\alpha G_{\mu\nu} + \beta g_{\mu\nu}$ — the **Einstein tensor** plus a possible cosmological constant. The fifth requirement (Newtonian limit, see [[Thm - Newtonian Limit of Einstein's Equations]]) fixes $\alpha = 1$ when the RHS is $8\pi G T_{\mu\nu}$. The cosmological term $\beta g_{\mu\nu} = -\Lambda g_{\mu\nu}$ is left as a free parameter — observationally small but nonzero (dark energy).

**Why not just $R_{\mu\nu} = 8\pi T_{\mu\nu}$?** This was Einstein's first guess (October 1915), and it fails requirement 4: the Ricci tensor is *not* divergence-free in general; only the Einstein tensor is. The correction was Einstein's November 1915 breakthrough.

**Why is the coupling constant $8\pi G$?** This is fixed by the Newtonian limit. Computing the linearised Einstein equations around Minkowski with weak source and slow motion, the $(0,0)$ component reduces to $\nabla^2 h_{00} = -16\pi G \rho$ (in suitable gauge). With the identification $h_{00} = -2\phi$ (from the equivalence principle and the geodesic equation), this becomes $\nabla^2 (-2\phi) = -16\pi G \rho$, i.e., $\nabla^2 \phi = 4\pi G \rho$ — Newton's Poisson equation. The factor of $8\pi$ in the field equation gives the factor of $4\pi$ in Poisson's equation, which is the correct factor for Newtonian gravity in 3D.

**The equations as a coupled system.** The Einstein equations are *ten* coupled nonlinear second-order PDEs for the ten components of $g_{\mu\nu}$. But:

- The contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ gives four *automatic* identities, reducing the count of independent equations to six.
- Diffeomorphism invariance (general covariance) allows four-parameter coordinate redefinitions, removing four degrees of freedom from the metric.
- Net result: **two propagating degrees of freedom** — the two polarisations of gravitational waves, exactly as expected for a massless spin-2 field.

**Nonlinearity.** Unlike Maxwell's equations (linear in $A_\mu$) or the wave equation, the Einstein equations are *nonlinear* in the metric. The nonlinearity has a clean physical interpretation: gravity gravitates — gravitational energy (encoded in $G_{\mu\nu}$ via the metric) sources further gravitational field. This is essential for the consistency of the theory but makes exact solutions rare. Most realistic problems require either approximation methods (post-Newtonian expansion, weak-field perturbation theory) or numerical simulation.

**Per-requirement failure analysis:**

(a) *Without covariance*: a non-covariant equation singles out a preferred frame, contradicting the spirit of relativity. (Pre-relativity theories that posit a preferred frame, like the ether, fall in this category.)

(b) *Without matching source rank*: scalar gravity (with source $T = T^\mu{}_\mu$, the trace of the stress-energy) gives the wrong light-bending prediction (half the observed value) — falsified by Eddington 1919. Vector gravity (rank-1 source) gives wrong signs for static field (gravitational *repulsion* between two static masses) — clearly wrong.

(c) *Without second-order restriction*: $f(R)$ gravity ($R$ replaced by a general function in the action) has higher-derivative equations that are equivalent to GR plus a scalar field (with potential determined by $f$). Such theories are viable but introduce new physics (an extra scalar degree of freedom). Pure higher-derivative theories (with $R^2, R_{\mu\nu}R^{\mu\nu}$, etc., in the action) generically have ghost modes (Ostrogradsky's theorem).

(d) *Without divergence-freeness*: the Einstein equations would be inconsistent with energy-momentum conservation, as discussed in [[Def - Einstein Tensor]]. This is Einstein's October 1915 mistake.

(e) *Without correct Newtonian limit*: would fail observational tests of gravity in the weak-field, slow-motion regime (planetary orbits, falling apples).

---

# The Definition

> **Definition (Einstein field equations).** The **Einstein field equations** of general relativity are the coupled tensor equations
> $$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = 8\pi G\, T_{\mu\nu}$$
> (in geometrised units, $G = c = 1$, simply $G_{\mu\nu} = 8\pi T_{\mu\nu}$), where $G_{\mu\nu}$ is the [[Def - Einstein Tensor|Einstein tensor]] of the metric $g$ and $T_{\mu\nu}$ is the [[Def - Stress-Energy Tensor|stress-energy tensor]] of the matter and non-gravitational fields.
>
> **Including a cosmological constant** $\Lambda$:
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}.$$
>
> **In trace-reversed form** (equivalent, using $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ and taking the trace to eliminate $R$):
> $$R_{\mu\nu} = 8\pi G\left(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T\right),$$
> where $T = T^\mu{}_\mu = g^{\mu\nu} T_{\mu\nu}$.
>
> **Vacuum field equations** ($T_{\mu\nu} = 0$):
> $$R_{\mu\nu} = 0.$$
> The full Riemann tensor $R^\rho{}_{\sigma\mu\nu}$ need not vanish in vacuum (it has 20 independent components in 4D, of which the 10 Ricci components vanish in vacuum, leaving 10 components encoded in the **Weyl tensor** — the conformally invariant part of curvature).

The system is ten coupled second-order quasi-linear PDEs for $g_{\mu\nu}$, with the Bianchi identity providing four automatic constraints and diffeomorphism gauge invariance providing four removable gauge degrees of freedom, leaving two physical (gravitational wave) polarisations.

**Decomposed forms:**

- *Trace-reversed* (eliminating $R$): $R_{\mu\nu} = 8\pi (T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$.
- *3+1 (ADM)*: split into **constraints** ($G_{0\mu} = 8\pi T_{0\mu}$, on each spatial slice) and **evolution equations** ($G_{\alpha\beta} = 8\pi T_{\alpha\beta}$, propagating forward in time).
- *Frame form*: in an orthonormal frame, $G(e_a, e_b) = 8\pi T(e_a, e_b)$, with $G(e_0, e_0) = K(e_1 \wedge e_2) + K(e_1 \wedge e_3) + K(e_2 \wedge e_3)$ — the sum of three spatial sectional curvatures, Wheeler's geometric form.

---

# Categorical / Structural Definition

The Einstein field equations are the **Euler–Lagrange equations** of the **Hilbert action** $S = \frac{1}{16\pi G}\int R\sqrt{-g}\, d^4x + S_\text{matter}$, varied with respect to the inverse metric $g^{\mu\nu}$. See [[Thm - Hilbert's Variational Principle Yields Einstein Equations]] for the derivation. In this variational picture:

- The gravitational degrees of freedom are the metric $g^{\mu\nu}$ — a section of the bundle of inverse Lorentzian metrics over $M$.
- The phase space (in the canonical formulation, on a spatial slice) is the cotangent bundle of the space of spatial metrics, with the second fundamental form $b_{\alpha\beta}$ as the conjugate momentum.
- The Einstein equations are Hamilton's equations for this system, with the Hamiltonian being a sum of constraints (the **Hamiltonian constraint** $G_{00}$ and the **momentum constraints** $G_{0i}$).
- The constraints generate the diffeomorphism gauge group, and the physical phase space is the cotangent bundle of the space of spatial metrics modulo spatial diffeomorphisms, restricted to the constraint surface.

This is the framework of **Hamiltonian general relativity** and the basis of **canonical quantum gravity** (the Wheeler–DeWitt equation).

In the **gauge theory** language: the metric is a section of a frame bundle, the Levi-Civita connection is a gauge field for the local Lorentz group $SO(1,3)$, the Riemann tensor is the curvature of this connection. The Einstein equations have the form "curvature equals source" — but it is a contracted, trace-modified curvature (the Einstein tensor) that appears, not the full Riemann/curvature 2-form. This is why GR is *first-order* in the Riemann curvature on the LHS but the matter coupling on the RHS is at the same order — gravity is *not* quite a standard Yang-Mills theory.

---

# Relate to Other Fields / Compression

**True name:** The Einstein field equations are *the statement "$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = 8\pi T_{\mu\nu}$" — the unique (up to cosmological constant) symmetric, divergence-free, second-order, generally covariant equation relating the geometry of spacetime to its matter content*. The form is structurally forced by these requirements (Lovelock's theorem), and the coupling constant is forced by the Newtonian limit. Everything in GR is the working-out of consequences of this equation.

The equations have a structural analogy to **Maxwell's equations** $\partial^\mu F_{\mu\nu} = 4\pi J_\nu$: in both cases, the LHS is a divergence-free combination of curvatures of the relevant gauge field (the Levi-Civita connection for gravity, the $U(1)$ connection $A_\mu$ for electromagnetism), and the RHS is the source (stress-energy for gravity, charge-current for EM). The conservation of the source ($\nabla^\mu T_{\mu\nu} = 0$ for gravity, $\partial^\nu J_\nu = 0$ for EM) is forced by the divergence-freeness of the LHS — a structural identity, not an additional postulate.

The difference is the nonlinearity: $F_{\mu\nu}$ is linear in $A_\mu$, but $G_{\mu\nu}$ is highly nonlinear in $g_{\mu\nu}$ (containing terms like $\Gamma\Gamma$ quadratic in connection coefficients, which are first derivatives of $g$, so $G$ contains products of first derivatives of $g$ as well as second derivatives). This nonlinearity is the deep reason GR is so much harder than EM.

---

# Examples / Corollaries

**Is an instance — Schwarzschild solution** ($T_{\mu\nu} = 0$, spherical symmetry, static, asymptotically flat). $R_{\mu\nu} = 0$ has the unique spherically symmetric static asymptotically flat solution $g = (1 - 2M/r) dt^2 - (1 - 2M/r)^{-1} dr^2 - r^2 d\Omega^2$. The exterior gravity of the Sun, planets, neutron stars, and non-rotating black holes. See [[Def - The Schwarzschild Metric]] and [[Thm - Schwarzschild Solution]].

**Is an instance — FLRW cosmology** (perfect fluid, homogeneous, isotropic). Metric $ds^2 = dt^2 - a(t)^2 d\sigma_K^2$ (with $d\sigma_K^2$ the metric on the spatial slice of constant curvature $K$). The Einstein equations reduce to the **Friedmann equation** $\left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3} \rho - \frac{K}{a^2}$ and the **acceleration equation** $\frac{\ddot a}{a} = -\frac{4\pi G}{3}(\rho + 3p)$. These govern the expansion history of the universe.

**Is an instance — Reissner–Nordström** (electromagnetic source, spherical, static). $T_{\mu\nu}$ is the electromagnetic stress-energy of a point charge; the Einstein equations couple to Maxwell, and the joint solution is $g = (1 - 2M/r + Q^2/r^2) dt^2 - (\ldots)^{-1} dr^2 - r^2 d\Omega^2$ with $A = (Q/r) dt$.

**Is an instance — gravitational waves in vacuum.** Linearising around Minkowski, $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$, the vacuum equations in the **transverse-traceless gauge** become $\Box h_{\mu\nu}^{TT} = 0$ — the wave equation for the metric perturbation. Solutions are propagating gravitational waves at the speed of light, with the two polarisations $h_+, h_\times$ detected by LIGO.

**Is NOT a solution — arbitrary metric with arbitrary $T_{\mu\nu}$.** The Einstein equations are *constraints*: not every metric satisfies them for some matter, and not every matter distribution is compatible with some metric. The relation between $G_{\mu\nu}$ (depending nonlinearly on $g$) and $T_{\mu\nu}$ (depending on the matter and the metric) is a coupled system, not a free choice on either side.

**Is NOT a special-relativistic equation.** Although special relativity is the local limit of GR, the Einstein equations are intrinsically nonlinear and global. The LHS contains curvature, vanishing in Minkowski space, so SR is the trivial vacuum solution $T_{\mu\nu} = 0$ and $g = \eta$. Any nontrivial matter source gives a nontrivial curvature, requiring GR.

**Corollary — vacuum has $R = 0$.** In vacuum, $G_{\mu\nu} = 0$, so the trace gives $g^{\mu\nu} G_{\mu\nu} = -R = 0$, hence $R = 0$. The vacuum equations reduce to $R_{\mu\nu} = 0$ (zero Ricci tensor), not the full $R^\rho{}_{\sigma\mu\nu} = 0$ (which would be flat spacetime, only the trivial vacuum).

**Corollary — gravitational radiation has trace-free stress.** In vacuum, $T = 0$, so propagating gravitational waves have no trace contribution — the polarisations are inherently transverse-traceless.

**Corollary — conservation is automatic.** Taking the covariant divergence of the field equations and using $\nabla^\mu G_{\mu\nu} = 0$ (Bianchi) gives $\nabla^\mu T_{\mu\nu} = 0$ — local conservation of energy-momentum is a *consequence* of the field equations, not an independent postulate. This is structurally beautiful and a key consistency check.

**Calibration check.** (i) Verify dimensional consistency: $[G_{\mu\nu}] = \text{length}^{-2}$ and $[T_{\mu\nu}] = \text{energy/volume} = \text{mass}\cdot c^2/\text{length}^3$, so the coupling $[8\pi G/c^4] = \text{length}/\text{mass} = $ length$^{-1}/$mass$\cdot$length$^{-1}$ giving consistent inverse-length-squared on both sides. (ii) Count degrees of freedom: 10 metric components $-$ 4 gauge $-$ 4 constraint $= 2$ physical, matching the two gravitational wave polarisations. (iii) Verify that the Einstein equations are consistent with vanishing $T_{\mu\nu}$ by the trivial solution $g = \eta$ (Minkowski).

---

# Unlocked by This

> [!tip] Gravitational Wave Detection and the Two Polarisations *(from Gravitational Wave Astronomy)*
> The vacuum Einstein equations admit propagating wave solutions with two physical polarisations $h_+, h_\times$ — the two transverse-traceless modes of the metric perturbation. These were predicted by Einstein in 1916, indirectly confirmed via the inspiral of the **Hulse–Taylor binary pulsar** (Nobel Prize 1993), and directly detected by **LIGO** in 2015 — gravitational waves from the merger of two black holes. The field of **gravitational wave astronomy** is now mature, with dozens of mergers detected and the LIGO/Virgo/KAGRA network expanding.

> [!tip] Numerical Relativity and Binary Mergers *(from Computational General Relativity)*
> Solving the full Einstein equations for binary black hole mergers — the source of LIGO's detections — requires numerical simulation. The breakthrough came with the **BSSN formulation** (Baumgarte–Shapiro–Shibata–Nakamura, late 1990s) and **moving puncture techniques** (2005), which finally allowed stable long-time evolution. Modern simulations match observed gravitational wave signals to remarkable precision, validating the full nonlinear Einstein equations in the strong-field regime.

> [!tip] The Cosmological Constant Problem *(from Quantum Gravity)*
> The cosmological constant $\Lambda$ in the Einstein equations is observationally $\sim 10^{-52}\,\mathrm{m}^{-2}$ — corresponding to a vacuum energy density $\sim 10^{-29}\,\mathrm{g/cm}^3$. Quantum field theory naively predicts $\sim 10^{120}$ times larger, the worst quantitative discrepancy in physics. Various proposed resolutions — anthropic selection from a string landscape, dynamical relaxation mechanisms, supersymmetric cancellations — remain unresolved.

> [!tip] No-Hair Theorem and Black Hole Uniqueness *(from Black Hole Physics)*
> Solutions of the Einstein equations describing stationary black holes are uniquely determined by three parameters: mass $M$, angular momentum $J$, and charge $Q$ — the **no-hair theorem** (Israel, Carter, Robinson, Hawking, in stages from 1967–1972). The most general such solution is **Kerr–Newman**. Any "hair" (additional fields like scalars, gauge fields) is forbidden by stability or constrained to vanish. This makes black holes the simplest objects in the universe: three numbers determine their entire structure.

> [!tip] AdS/CFT Correspondence *(from String Theory and Quantum Gravity)*
> Solutions of the Einstein equations with negative cosmological constant $\Lambda < 0$ are **anti-de Sitter** spacetimes. **Maldacena's conjecture** (1997) asserts that quantum gravity (with strings) on $\text{AdS}_{d+1}$ is dual to a conformal field theory on its $d$-dimensional conformal boundary — a precise realisation of the holographic principle. The duality has become a powerful tool for studying **strongly-coupled quantum field theories** (heavy-ion collisions, condensed matter at quantum critical points) by translating to weakly-coupled gravity calculations.

> [!tip] The Singularity Theorems *(from Mathematical General Relativity)*
> The Einstein equations, combined with **energy conditions** on $T_{\mu\nu}$ and global structure assumptions (trapped surface, achronal achronal surface), imply that the spacetime is geodesically incomplete — **Hawking–Penrose singularity theorems**. So Big Bang singularities in cosmology and black hole interior singularities are not artefacts of symmetry but generic features of solutions to the Einstein equations with physical matter. This is one of the deepest results of mathematical GR, and the source of the search for **quantum gravity** (which is expected to resolve the singularities).
