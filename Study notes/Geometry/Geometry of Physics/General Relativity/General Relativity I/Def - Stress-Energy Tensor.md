---
type: definition
subject: general-relativity
prereqs:
  - "Def - Spacetime Manifold"
  - "Def - Four-Vector"
  - "Def - Tensor Field on a Manifold"
  - "Def - Minkowski Space and the Metric"
tags: [physics, general-relativity, matter, conservation-laws]
---

# Notation

Spacetime $(M, g)$ with signature $(+,-,-,-)$ and $c = 1$. The stress-energy tensor is denoted $T_{\mu\nu}$ (covariant components) or $T^{\mu\nu}$ (contravariant); indices are raised/lowered with $g$. We use $\rho$ for rest-frame energy density and $p$ for pressure (these are scalar fields). The four-velocity of a fluid element is $u^\mu$, normalised $g_{\mu\nu} u^\mu u^\nu = 1$ (timelike, unit). The electromagnetic field strength is $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Axiom Motivation

The desideratum is to identify the relativistic generalisation of Newton's mass density $\rho$ that serves as the source of the gravitational field. In Newtonian gravity, the source is the scalar mass density $\rho$, appearing on the right-hand side of Poisson's equation $\nabla^2 \phi = 4\pi G \rho$. In special relativity, the source must be a Lorentz-covariant object — but mass density is not a Lorentz scalar.

**Why is mass density not a scalar?** Consider a fluid at rest with rest-mass density $\rho_0$. In a frame moving with velocity $v$ relative to the fluid, two relativistic effects modify what is measured: (i) length contraction by $\gamma$ in the direction of motion, so the volume of a fluid element is contracted by $1/\gamma$, hence the density is increased by $\gamma$; (ii) the rest mass of each fluid particle is increased by $\gamma$ (since each particle is moving with the fluid relative to this frame). The combined effect gives moving density $\rho = \gamma^2 \rho_0$ — *two* factors of $\gamma$, not one. This means $\rho$ transforms as the $(0,0)$ component of a *rank-2 tensor*, not as a scalar.

**The right object: stress-energy tensor.** The minimal Lorentz-covariant object whose $(0,0)$ component is the energy density (so that it includes mass-energy via $E = mc^2$, rest-energy density $\rho c^2$ in conventional units) is a symmetric rank-2 tensor $T^{\mu\nu}$. Its components in an orthonormal frame have the physical interpretation:

- $T^{00}$ — **energy density** (mass-energy per unit volume).
- $T^{0i}$ — **energy flux** in the $i$-direction (equivalently, momentum density in the $i$-direction; the equality is a special-relativistic fact, $E = pc$ for light).
- $T^{ij}$ — the **stress tensor** of classical continuum mechanics: $T^{ii}$ (no sum) is the pressure or tension in direction $i$, $T^{ij}$ ($i \neq j$) is the shear stress.

The symmetry $T^{\mu\nu} = T^{\nu\mu}$ has two faces. The spatial part $T^{ij} = T^{ji}$ is the symmetry of the classical stress tensor (which follows from angular momentum conservation — antisymmetric stress would generate torques on infinitesimal volume elements). The mixed $T^{0i} = T^{i0}$ is the relativistic equality of energy flux and momentum density (energy carrying momentum is momentum, and conversely).

**Conservation: $\partial^\mu T_{\mu\nu} = 0$ (special relativity).** In special relativity, the local conservation of energy and momentum is expressed as four equations: $\nu = 0$ is energy conservation, $\partial_t T^{00} + \partial_i T^{0i} = 0$ (local rate of change of energy density equals negative divergence of energy flux); $\nu = i$ is momentum conservation, $\partial_t T^{0i} + \partial_j T^{ij} = 0$ (local rate of change of momentum density equals negative divergence of stress). These four equations are unified into the single tensor identity $\partial^\mu T_{\mu\nu} = 0$.

**Upgrade to GR: $\nabla^\mu T_{\mu\nu} = 0$.** In a curved spacetime, partial derivatives are replaced by covariant ones, and the conservation law becomes $\nabla^\mu T_{\mu\nu} = 0$. This is not an independent postulate — it follows from the Einstein field equations via the contracted Bianchi identity ([[Thm - Contracted Bianchi Implies Stress-Energy Conservation]]). The "conservation" is now local: the equation does not, in a generic curved spacetime, integrate to a global conservation law (energy is not conserved globally in the absence of a time-translation Killing vector). This is the cause of the **cosmological energy puzzle** — the apparent loss of energy as the universe expands and cosmic microwave background photons redshift is not a violation of GR, but the reflection that the FLRW spacetime lacks the time-translation symmetry that would give a globally conserved energy.

**Per-component motivation analysis:**

(a) *Why include $T^{00}$ (energy density)?* Without it there is no source of gravity (Poisson's equation requires a mass-energy density). This is the dominant source in non-relativistic regimes.

(b) *Why include $T^{ij}$ (pressure and stress)?* Pressure contributes to gravity in GR — a relativistic gas under high pressure gravitates more strongly than a low-pressure gas of the same energy density. In the perfect fluid form $T^{\mu\nu} = (\rho + p) u^\mu u^\nu - p g^{\mu\nu}$ (signature $+---$), the trace is $\rho - 3p$, and the gravitating combination in the Einstein equations is $\rho + 3p$ (Tolman–Oppenheimer–Volkoff equation for stellar equilibrium). For radiation ($p = \rho/3$, traceless), the gravitating effect is $2\rho$, twice the energy density alone.

(c) *Why include $T^{0i}$ (momentum density)?* Momentum density sources frame-dragging — a rotating mass distribution, with nonzero $T^{0i}$, generates the gravitomagnetic effects of Kerr-type spacetimes.

(d) *What if we drop the symmetry?* An antisymmetric part of $T^{\mu\nu}$ would represent angular momentum density (intrinsic spin). In standard GR this is set to zero (the **spin density** is not directly in the Einstein equations), but in **Einstein–Cartan theory** the antisymmetric part sources spacetime *torsion*. For ordinary matter (without intrinsic spin contributions), the symmetric stress-energy tensor suffices.

(e) *What if we drop conservation?* The Einstein equations would then be over-determined: $\nabla^\mu G_{\mu\nu} = 0$ identically (Bianchi), so $G_{\mu\nu} = 8\pi T_{\mu\nu}$ requires $\nabla^\mu T_{\mu\nu} = 0$. Without this, no consistent solutions exist. So the conservation of $T_{\mu\nu}$ is a structural necessity, not an extra postulate.

---

# The Definition

> **Definition (Stress-energy tensor).** The **stress-energy tensor** (also called the **energy-momentum tensor**) of a matter distribution or non-gravitational field on a spacetime $(M, g)$ is a symmetric $(0,2)$-tensor field $T_{\mu\nu}$ with the following physical interpretation in an orthonormal frame:
>
> - $T_{00}$: **energy density** (energy per unit volume, including rest-mass energy via $E = mc^2$);
> - $T_{0i} = T_{i0}$: **momentum density** in the $i$-direction (equivalently, energy flux);
> - $T_{ij}$: **spatial stress** — $T_{ii}$ (no sum) is the pressure (or tension if negative) in direction $i$, $T_{ij}$ ($i \neq j$) is the shear stress.
>
> The tensor is required to satisfy the **local conservation law** $\nabla^\mu T_{\mu\nu} = 0$.
>
> Defined variationally: for a matter action $S_\text{matter}[g, \psi]$ depending on the metric $g$ and matter fields $\psi$,
> $$T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta S_\text{matter}}{\delta g^{\mu\nu}}.$$
> This is the **Hilbert stress-energy tensor**, and it is automatically symmetric and (by [[Def - Diffeomorphism|diffeomorphism]] invariance of $S_\text{matter}$) conserved when matter equations of motion hold.

**Examples of standard matter content:**

**Dust** (pressureless matter, particles non-interacting except gravitationally):
$$T^{\mu\nu}_\text{dust} = \rho\, u^\mu u^\nu,$$
where $\rho$ is the rest-frame energy density and $u^\mu$ is the fluid four-velocity. In the rest frame ($u^\mu = (1, 0, 0, 0)$), the only nonzero component is $T^{00} = \rho$ — pure energy density, no pressure, no flux.

**Perfect fluid** (isotropic pressure, no shear or heat conduction):
$$T^{\mu\nu}_\text{PF} = (\rho + p)\, u^\mu u^\nu - p\, g^{\mu\nu}$$
(in signature $+---$). The rest-frame components are $T^{00} = \rho$, $T^{ii} = p$ — energy density and isotropic pressure. The relation $p = p(\rho)$ (equation of state) characterises the type of fluid: dust ($p = 0$), radiation ($p = \rho/3$), stiff fluid ($p = \rho$), cosmological constant ($p = -\rho$).

**Electromagnetic field:**
$$T^{\mu\nu}_\text{EM} = \frac{1}{4\pi}\left[F^{\mu\rho} F^\nu{}_\rho - \frac{1}{4} g^{\mu\nu} F^{\rho\sigma} F_{\rho\sigma}\right].$$
Symmetric, **traceless** (since $T^\mu{}_\mu = 0$ — a feature of conformal invariance of the EM action in 4D), and conserved whenever Maxwell's equations $\nabla_\mu F^{\mu\nu} = 0$ hold. The energy density is $T^{00} = (1/8\pi)(E^2 + B^2)$, the Poynting vector $T^{0i} = (1/4\pi)(\vec E \times \vec B)^i$.

**Massive scalar field (Klein–Gordon):**
$$T^{\mu\nu}_\phi = \partial^\mu \phi \partial^\nu \phi - g^{\mu\nu}\left[\frac{1}{2} \partial^\rho \phi \partial_\rho \phi - \frac{1}{2} m^2 \phi^2\right].$$
Conserved when the Klein–Gordon equation $(\Box + m^2)\phi = 0$ holds.

---

# Categorical / Structural Definition

The stress-energy tensor is the **Noether current** associated with **spacetime translation symmetry**. In flat spacetime, the matter action is invariant under translations $x^\mu \to x^\mu + a^\mu$, and Noether's theorem produces four conserved currents — the four components of $T^{\mu\nu}$ (one for each translation direction). The conservation $\partial^\mu T_{\mu\nu} = 0$ is the Noether identity for translation symmetry.

In curved spacetime, the spacetime translation symmetry is replaced by **diffeomorphism invariance** of the matter action. The Hilbert definition $T_{\mu\nu} = -(2/\sqrt{-g}) \delta S_\text{matter}/\delta g^{\mu\nu}$ produces, via diffeomorphism invariance of the matter action, the conservation law $\nabla^\mu T_{\mu\nu} = 0$ automatically (this is the **diffeomorphism Ward identity**, the generalisation of the Noether identity).

The stress-energy tensor is, structurally, a section of the bundle $S^2 T^*M$ (symmetric $(0,2)$-tensors). It transforms covariantly under coordinate changes (its components transform with two factors of the inverse Jacobian).

---

# Relate to Other Fields / Compression

**True name:** The stress-energy tensor is *the local distribution of energy, momentum, and stress in a relativistic continuous medium*. Its four-velocity $u^\mu$ identifies the local rest frame; in that frame, its components are the classical energy density, momentum density (zero for a fluid at rest), and stress tensor. In a moving frame, it transforms covariantly, mixing all components.

The stress-energy tensor unifies classical continuum mechanics with special relativity. Classical continuum mechanics has separate notions of mass density $\rho_\text{cl}$, momentum density $\rho \vec v$, energy density $\frac{1}{2} \rho v^2 + \rho U$ (kinetic plus internal), and stress tensor $\sigma_{ij}$; these are connected by classical conservation laws (continuity, Euler equation, energy equation). In relativity, all of these are unified into the single object $T^{\mu\nu}$, with the conservation laws unified into $\partial^\mu T_{\mu\nu} = 0$.

In quantum field theory, the stress-energy tensor is the operator that generates spacetime translations, and its vacuum expectation value $\langle 0 | T_{\mu\nu} | 0 \rangle$ is the **vacuum energy density** — formally infinite in a cutoff-free theory, and the source of the **cosmological constant problem**. Anomalies in the conservation $\nabla^\mu T_{\mu\nu}$ at the quantum level (the **trace anomaly** for a conformally invariant theory) signal subtle quantum effects in curved spacetime.

---

# Examples / Corollaries

**Is an instance — dust (cosmological dust, "matter").** A pressureless fluid of non-interacting particles. $T^{\mu\nu} = \rho u^\mu u^\nu$. Cosmological matter (galaxies on large scales, cold dark matter) is well-modelled as dust.

**Is an instance — radiation.** A gas of photons or ultra-relativistic particles. Perfect fluid with $p = \rho/3$ (the famous relation, valid for any traceless symmetric stress-energy tensor in 4D). $T^{\mu\nu} = (4/3) \rho u^\mu u^\nu - (1/3) \rho g^{\mu\nu}$. The cosmic microwave background and the early radiation-dominated era of the universe are described by this.

**Is an instance — cosmological constant / dark energy.** Perfect fluid with $p = -\rho$, giving $T^{\mu\nu} = -\rho g^{\mu\nu}$. This is the stress-energy of a constant vacuum energy density $\rho_\Lambda$, equivalent to including a $\Lambda g_{\mu\nu}$ term in the Einstein equations. The constant-equation-of-state $w = p/\rho = -1$ is the **dark energy** equation of state, observed to within a few percent.

**Is an instance — perfect fluid star.** Inside a static spherically symmetric star, $T^{\mu\nu}$ is a perfect fluid with $\rho(r)$ and $p(r)$ functions of radius. The Einstein equations reduce to the **Tolman–Oppenheimer–Volkoff (TOV) equation** for $p(r)$, which is the relativistic equation of stellar structure.

**Is NOT an instance — a non-symmetric tensor.** The stress-energy tensor must be symmetric. Theories with intrinsic spin (Dirac fermions in Einstein–Cartan theory) can have an antisymmetric **spin tensor**, but it is a separate object from the symmetric stress-energy tensor.

**Is NOT an instance — gravitational energy.** The gravitational field has no well-defined local stress-energy tensor in GR (this is the deep statement of the equivalence principle: gravity can be locally transformed away, so any local "gravitational energy" can be made to vanish in the freely-falling frame). For asymptotically flat spacetimes there is a total **ADM mass** as a surface integral at infinity, but no local density. Various **pseudo-tensors** (Landau–Lifshitz, Møller, etc.) are coordinate-dependent attempts to define one; none is fully satisfactory. This is why gravity does *not* appear on the right-hand side of the Einstein equations as a self-source — the LHS contains gravity, and the RHS contains only non-gravitational matter.

**Corollary — Lorentz transformation of $T^{\mu\nu}$.** In an orthonormal frame with metric $\eta_{\mu\nu}$, under a Lorentz boost the stress-energy tensor transforms by $T'^{\mu\nu} = \Lambda^\mu{}_\rho \Lambda^\nu{}_\sigma T^{\rho\sigma}$. A purely-pressure-tensor in one frame becomes a momentum-flux tensor in another (a moving "pressure" carries energy flow).

**Corollary — energy conditions.** Physical reasonableness of matter is encoded in **energy conditions** on $T_{\mu\nu}$ — the **weak energy condition** $T_{\mu\nu} t^\mu t^\nu \geq 0$ for every future-directed timelike $t^\mu$ (energy density non-negative in every frame), the **dominant energy condition** ($-T^\mu{}_\nu t^\nu$ is causal and future-directed for every future-directed timelike $t$), etc. Standard matter satisfies these; some quantum effects (Casimir effect, Hawking radiation) can violate the weak energy condition locally.

**Corollary — trace.** The trace $T = T^\mu{}_\mu = g^{\mu\nu} T_{\mu\nu}$ is a Lorentz scalar. For a perfect fluid, $T = \rho - 3p$. For a traceless stress-energy (radiation, EM field), $T = 0$. The sign and magnitude of $T$ enter via the trace-reversed Einstein equations $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$.

**Calibration check.** (i) Verify that for dust in the rest frame ($u^\mu = (1, 0, 0, 0)$), $T^{\mu\nu} = \rho u^\mu u^\nu$ gives $T^{00} = \rho$ and all other components zero. (ii) Compute $T^{00}$ for a perfect fluid in a boosted frame moving at velocity $v$; verify that it differs from the rest-frame value by relativistic factors of $\gamma$ and $p$. (iii) Verify that the trace of the electromagnetic stress-energy tensor in flat 4D space vanishes (this is the trace anomaly of the conformal symmetry of Maxwell's equations).

---

# Unlocked by This

> [!tip] Energy Conditions and Singularity Theorems *(from Mathematical General Relativity)*
> The **Hawking–Penrose singularity theorems** require an **energy condition** on $T_{\mu\nu}$: the **strong energy condition** $(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T) t^\mu t^\nu \geq 0$ (gravity is attractive), or the weaker **null energy condition** $T_{\mu\nu} k^\mu k^\nu \geq 0$ for null $k$. These conditions, combined with global hyperbolicity and the existence of a trapped surface, imply that the spacetime is geodesically incomplete — a singularity must form. So the qualitative properties of the matter — encoded in the energy conditions — determine the global structure of the spacetime, completely independent of the detailed dynamics.

> [!tip] ADM Mass and the Positive Energy Theorem *(from Mathematical General Relativity)*
> For asymptotically flat spacetimes, the **ADM mass** is a total energy defined as a surface integral over a 2-sphere at infinity, expressible in terms of the asymptotic behaviour of the spatial metric and second fundamental form. The **Schoen–Yau positive energy theorem** (1979) and Witten's spinor proof (1981) show that if the dominant energy condition holds, the ADM mass is non-negative, with equality only for Minkowski space. This is the relativistic generalisation of the classical "kinetic energy is non-negative".

> [!tip] Cosmological Energy and the FLRW Universe *(from Cosmology)*
> In the FLRW universe, the cosmological "fluid" is a perfect fluid with equation of state $p = w\rho$ for various components: matter ($w = 0$), radiation ($w = 1/3$), dark energy ($w = -1$). The conservation $\nabla_\mu T^{\mu\nu} = 0$ in the expanding spacetime gives $\dot\rho + 3H(\rho + p) = 0$ — a homogeneous fluid loses density as the universe expands, with the rate set by the equation of state. The cosmic microwave background photons redshift away energy ($\rho_\text{rad} \propto a^{-4}$ where $a$ is the scale factor), while matter density dilutes only by volume ($\rho_\text{matter} \propto a^{-3}$), and dark energy stays constant ($\rho_\Lambda =$ const).

> [!tip] Vacuum Energy and the Cosmological Constant Problem *(from Quantum Field Theory in Curved Spacetime)*
> Quantum field theory predicts that even in the vacuum, the fields have nonzero ground-state energy: $\langle 0 | T_{\mu\nu} | 0 \rangle = -\rho_\text{vac} g_{\mu\nu}$, with $\rho_\text{vac}$ formally divergent and naturally of order the cutoff scale (Planck scale, $\sim 10^{72}\,\mathrm{GeV}^4$). The observed cosmological constant corresponds to $\rho_\Lambda \sim 10^{-47}\,\mathrm{GeV}^4$ — a discrepancy of $\sim 120$ orders of magnitude, the **cosmological constant problem**, perhaps the worst quantitative disagreement in theoretical physics.

> [!tip] Holography and the Information Content of Spacetime *(from Quantum Gravity)*
> The **Bekenstein–Hawking entropy** of a black hole is $S_\text{BH} = A/4$ (in natural units) — area divided by four Planck areas. This implies that the **entropy density of a region** (and hence the amount of information that can be stored) is bounded not by volume but by surface area — the **holographic principle**. The matter and its stress-energy tensor "live on" a lower-dimensional boundary in some deep sense, made precise in the **AdS/CFT correspondence**: a strongly-coupled field theory in $d$ dimensions is equivalent to a gravity theory (with stress-energy tensor as a boundary operator) in $d+1$ dimensions.
