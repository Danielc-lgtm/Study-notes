---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus signature** $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike vector has positive norm-squared and the fluid four-velocity is normalised to $u\cdot u = +1$. The symbol $\rho$ denotes the **proper energy density** (energy per unit volume in the rest frame, including rest-mass energy), *not* the rest-mass density; $p$ is the pressure. The energy–momentum tensor is $T^{\mu\nu}$ (see [[Def - The Energy-Momentum Tensor]]); the four-velocity field is $u$, with four-acceleration $a^\mu = u^\nu\nabla_\nu u^\mu$ (see [[Def - Four-Velocity and Four-Acceleration]]). A general observer has four-velocity $u_0$, and the orthogonal projector onto that observer's rest space is $\perp^\mu{}_\nu = \delta^\mu_\nu - u_0^\mu u_{0\nu}$ (see [[Def - Observer and Local Rest Space]]). Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

> [!warning] Convention
> Gourgoulhon's *Special Relativity in General Frames* uses the **mostly-plus** signature, where the four-velocity satisfies $u\cdot u = -1$ and the perfect-fluid tensor reads $T = (\varepsilon + p)\,\underline{u}\otimes\underline{u} + p\,g$ with $\varepsilon$ the proper energy density. We use **mostly-minus**: flipping the overall sign of every metric contraction turns this into $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$, with $\rho = \varepsilon$. Both forms describe the same physics; only the signs of metric contractions differ.

---

# Axiom Motivation

We want a mathematical object that captures the simplest non-trivial continuous matter: a fluid with no internal friction and no heat conduction. The data such an object must carry are, at minimum, a velocity field — at each event, the mean four-velocity $u$ of the matter passing through — and the local energy content. The question is what tensor encodes "energy content" in a way compatible with relativity, and the answer is forced by what a comoving observer should measure.

Begin from the [[Def - The Energy-Momentum Tensor|energy–momentum tensor]] $T^{\mu\nu}$, whose general meaning is fixed: contracted twice with an observer's four-velocity it gives the energy density that observer measures, contracted once it gives momentum density, and its purely spatial part is the stress (the flux of momentum across surfaces). The defining desideratum of a *perfect* fluid is a statement about that stress: **in the rest frame of any fluid element, the stress is isotropic**. There is a single number, the pressure $p$, and the force per unit area across any surface element is $p$ times the unit normal, in every direction equally. No direction is special; there is no shear stress (which would be a velocity-gradient effect, viscosity) and no off-diagonal momentum flux. This is the precise content of "no viscosity, no anisotropy", and it is the one physical input.

Now reconstruct the tensor from this requirement. In the local rest frame the four-velocity is $u = (1,0,0,0)$. A comoving observer must measure energy density $\rho$, so $T^{00} = \rho$. The momentum density must vanish (the fluid is at rest, nothing is flowing), so $T^{0i} = 0$. The stress must be isotropic, $T^{ij} = p\,\delta^{ij}$. Assembling these in the rest frame, $T^{\mu\nu} = \mathrm{diag}(\rho, p, p, p)$ in the mostly-minus convention. The task is to write this as a frame-independent tensor expression built from the only available ingredients — the four-velocity $u$ and the metric $\eta$. The combination $u^\mu u^\nu$ is, in the rest frame, $\mathrm{diag}(1,0,0,0)$, and $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$. A short calculation shows
$$\rho\,u^\mu u^\nu \;-\; p\,(\eta^{\mu\nu} - u^\mu u^\nu) \;=\; (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$$
reproduces $\mathrm{diag}(\rho,p,p,p)$ in the rest frame, and being a tensor equation it then holds in every frame. So the form is not an ansatz to be guessed but the unique tensor that is built from $u$ and $\eta$, gives energy density $\rho$ and isotropic pressure $p$ to a comoving observer, and is symmetric. The term $-p(\eta^{\mu\nu} - u^\mu u^\nu)$ is exactly $p$ times the orthogonal projector onto the rest space (with a sign), which is the geometric way of saying "isotropic pressure in the rest space".

It is worth stressing each ingredient by asking what its absence would cost. If the **isotropy** were dropped — if the rest-frame stress were a general symmetric $3\times3$ matrix $\sigma_{ij}$ rather than $p\,\delta_{ij}$ — the off-diagonal and anisotropic parts would be shear stresses, and the fluid would be viscous; the tensor would acquire terms built from the velocity gradient $\nabla_\mu u_\nu$, and the clean form would be lost. The perfect fluid is precisely the case where these are absent. If the **vanishing momentum density in the rest frame** were dropped — if $T^{0i} \ne 0$ comoving — there would be a heat flux: energy flowing relative to the matter, which is conduction; this too adds a term, $q^\mu u^\nu + u^\mu q^\nu$ with $q$ the heat-flux vector orthogonal to $u$. Perfect means no conduction. If the **four-velocity were not a unit timelike field** — if $u\cdot u \ne 1$ — then $\rho = T(u,u)$ would not be the rest-frame energy density and the whole interpretation would collapse; the normalisation $u\cdot u = 1$ is what makes $u$ a genuine four-velocity and $\rho$ a genuine energy density. The single design decision is: of all symmetric tensors, take the one with isotropic rest-frame stress and no rest-frame energy flux, and it is forced to be $(\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$.

One can also motivate the definition from the dust limit, which shows the form is correct at least when $p = 0$. A cloud of non-interacting particles all sharing the same four-velocity $u$ at each event has energy–momentum tensor $T^{\mu\nu} = \rho_{\mathrm m}u^\mu u^\nu$ (mass density times $u\otimes u$), as one computes directly from the particle energy–momentum tensor by collapsing all four-velocities to the common $u$. This is the perfect-fluid form with $p = 0$, and pressure is exactly what is missing: pressure, in kinetic theory, is the momentum transferred between adjacent fluid elements by particles crossing between them, and if all particles share one four-velocity their worldlines are parallel and no crossing occurs. Turning on a velocity *spread* among the constituents turns on pressure, and the perfect-fluid tensor is the result when that spread is isotropic in the rest frame.

---

# The Definition

A **perfect fluid** is a continuous medium whose energy–momentum tensor takes the form
$$T^{\mu\nu} \;=\; (\rho + p)\,u^\mu u^\nu \;-\; p\,\eta^{\mu\nu},$$
where
- $u$ is the **fluid four-velocity**, a future-directed timelike unit vector field, $u_\mu u^\mu = 1$;
- $\rho$ is the **proper energy density**, a scalar field, equal to the energy density measured by a comoving observer: $\rho = T_{\mu\nu}u^\mu u^\nu$;
- $p$ is the **pressure**, a scalar field, the (isotropic) stress measured by a comoving observer.

Equivalently, in terms of the orthogonal projector $\perp^{\mu\nu} = \eta^{\mu\nu} - u^\mu u^\nu$ onto the local rest space (with $\perp^{\mu\nu}$ here having signature so that it is the *spatial* metric), the tensor is
$$T^{\mu\nu} = \rho\,u^\mu u^\nu - p\,\perp^{\mu\nu},$$
which displays it as "energy density along the time direction, isotropic pressure across the rest space". The field lines of $u$ are the **fluid lines** — the worldlines of fluid particles — and they form a congruence: through each event passes exactly one fluid line.

The defining physical characterisation is the **isotropy of the rest-frame stress**: in the local rest frame, where $u = (1,0,0,0)$, the components are
$$T^{\mu\nu}_{\text{rest}} = \begin{pmatrix} \rho & 0 & 0 & 0 \\ 0 & p & 0 & 0 \\ 0 & 0 & p & 0 \\ 0 & 0 & 0 & p \end{pmatrix},$$
so the stress tensor is $S_{ij} = p\,\delta_{ij}$, isotropic, with no shear and no heat flux. A medium with these properties (no viscosity, no conduction, isotropic pressure) is a perfect fluid; any anisotropy or energy flux in the rest frame takes it outside the class.

The system is closed by an **equation of state** relating $\rho$ and $p$ (see [[Def - Equation of State and Speed of Sound]]) and a velocity field; the dynamics is the conservation law $\nabla_\mu T^{\mu\nu} = 0$ (see [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]).

---

# Categorical / Structural Definition

Structurally, the perfect fluid is the **isotropic, conduction-free reduction of a general energy–momentum tensor**, and it is illuminating to see it as one term in a hierarchy of fluid models obtained by adding dissipative terms. Decompose any symmetric tensor $T^{\mu\nu}$ relative to a chosen unit timelike field $u$ into its irreducible pieces under the rotation group of the rest space:
$$T^{\mu\nu} = \rho\,u^\mu u^\nu + (q^\mu u^\nu + u^\mu q^\nu) - (p + \Pi)\perp^{\mu\nu} + \pi^{\mu\nu},$$
where $\rho = T_{\mu\nu}u^\mu u^\nu$ is the energy density, $q^\mu$ is the heat-flux vector (orthogonal to $u$), $p$ is the isotropic pressure, $\Pi$ is the bulk-viscous pressure, and $\pi^{\mu\nu}$ is the symmetric trace-free shear-stress tensor (orthogonal to $u$). This is the most general form, and each fluid model is a constraint on it. The **perfect fluid** is the maximally symmetric reduction: set $q^\mu = 0$ (no conduction), $\Pi = 0$ and $\pi^{\mu\nu} = 0$ (no viscosity), leaving $T^{\mu\nu} = \rho\,u^\mu u^\nu - p\,\perp^{\mu\nu}$. Turning $\pi^{\mu\nu}$ and $\Pi$ back on (proportional to the velocity gradient $\nabla_\mu u_\nu$) gives a **Navier–Stokes / Eckart viscous fluid**; turning $q^\mu$ on gives a **conducting fluid**. The perfect fluid is thus the "free" object of the category of relativistic fluids, the one with the full rotational symmetry of the rest space and no first-derivative (gradient) corrections.

A second structural reading is by symmetry. The perfect-fluid tensor is the unique (up to the two scalars $\rho$ and $p$) symmetric tensor built from $u$ and $\eta$ that is **invariant under the little group of $u$** — the $SO(3)$ of spatial rotations fixing the four-velocity. Any tensor invariant under that $SO(3)$ must be a linear combination of the two available invariant tensors, $u^\mu u^\nu$ and $\perp^{\mu\nu}$, and that combination is exactly the perfect-fluid form. So "perfect fluid" is the same as "energy–momentum tensor with full rotational isotropy about the flow", which is why it is the matter content assumed in the most symmetric spacetimes: a homogeneous isotropic cosmology *must* have a perfect-fluid source, because any other tensor would single out a spatial direction and break isotropy.

---

# Relate to Other Fields / Compression

The perfect fluid is the relativistic completion of the object that, in nonrelativistic fluid dynamics, is split between the **mass density** $\rho_{\mathrm m}$ and the **pressure** $p$ appearing in the Euler equation. In the slow-motion limit the energy density $\rho$ reduces to $\rho_{\mathrm m}c^2$ plus internal energy, and the tensor's conservation reproduces the continuity and Euler equations. The genuinely relativistic feature, invisible classically, is that the *inertia* of a fluid element is the proper enthalpy density $\rho + p$, not the mass density — pressure contributes to inertia, the fluid analogue of $E = mc^2$.

In **general relativity**, the perfect-fluid tensor is the standard matter source: it is the right-hand side $T_{\mu\nu}$ of the Einstein equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$ for stars, for cosmological matter, and for any situation where the matter is well-described as isotropic in its rest frame. The Friedmann–Lemaître cosmology assumes a perfect fluid because homogeneity and isotropy demand it.

In **thermodynamics**, the two scalars $\rho$ and $p$ are not independent of the microphysics: they are linked by an equation of state, and the combination $\rho + p = Ts + \sum_a\mu_a n_a$ is the proper enthalpy density, which is why $\rho + p$ rather than $\rho$ governs the inertia and the speed of sound.

**True name:** the operational characterisation of a perfect fluid is *"the rest-frame stress is isotropic: a single pressure, no shear, no heat flux"*. This is more useful than the tensor formula for recognising perfect fluids and for knowing what is being assumed: whenever you can argue that in the local rest frame there is one pressure pushing equally in all directions and no energy flowing relative to the matter, the perfect-fluid tensor applies, and the formula $(\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ follows. Conversely, any anisotropy of stress or any rest-frame heat flow takes you outside the class and adds dissipative terms.

---

# Examples / Corollaries

**Is an instance — dust (pressureless fluid).** Setting $p = 0$ gives $T^{\mu\nu} = \rho\,u^\mu u^\nu$, the energy–momentum tensor of **dust**: a cloud of non-interacting particles sharing a common four-velocity. This is the perfect fluid in its simplest form, and it models cold, collisionless matter — galaxies treated as point masses in cosmology, or cold dark matter. Its conservation $\nabla_\mu T^{\mu\nu} = 0$ splits into mass conservation and force-free geodesic motion; see [[Ex - Dust as the pressureless limit of a perfect fluid]].

**Is an instance — a photon gas (radiation fluid).** Electromagnetic radiation in thermal equilibrium is a perfect fluid with the equation of state $p = \rho/3$ (the trace of the [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|electromagnetic energy–momentum tensor]] vanishes, forcing $\rho = 3p$). This is the matter content of the radiation-dominated early universe, and its speed of sound is $c_s = 1/\sqrt3$. The energy density and pressure are isotropic in the rest frame of the radiation (the frame in which the radiation has no net momentum), so the perfect-fluid form applies even though the constituents move at the speed of light.

**Is an instance — a polytrope.** Cold dense matter (a white dwarf or neutron-star interior) is a barotropic perfect fluid with $p = \kappa\,n^\gamma$ for an adiabatic index $\gamma$ (for example $\gamma = 5/3$ for a non-relativistic degenerate electron gas, $\gamma = 4/3$ for an ultra-relativistic one). The energy density is $\rho = m_{\mathrm b}n + \kappa n^\gamma/(\gamma-1)$. This is the equation of state used in stellar-structure calculations.

**Is NOT an instance — a viscous fluid.** A real fluid with viscosity has shear stresses in its rest frame, $T^{ij} = p\,\delta^{ij} - \eta_{\text{visc}}(\partial_i V_j + \partial_j V_i - \tfrac23\delta_{ij}\nabla\cdot\mathbf{V}) - \cdots$, where the velocity-gradient terms are anisotropic. This breaks the isotropy that defines a perfect fluid; the tensor acquires terms built from $\nabla_\mu u_\nu$, and the medium is a viscous (Navier–Stokes or Israel–Stewart) fluid, not a perfect one. Honey, air with internal friction, and the quark–gluon plasma at finite viscosity are not perfect fluids, though the plasma is famously *close* to perfect.

**Is NOT an instance — a free electromagnetic field in general.** A single plane electromagnetic wave has an energy–momentum tensor that is highly anisotropic: all the momentum flows in the propagation direction, and the stress is not isotropic in any frame. Its tensor is $T^{\mu\nu} \propto k^\mu k^\nu$ with $k$ null, which is *not* of perfect-fluid form (there is no rest frame, and the stress is a pure pressure along one direction). Only an isotropic *gas* of radiation, averaged over directions, becomes a perfect fluid.

**Corollary — the trace fixes the equation-of-state combination.** Taking the trace, $T^\mu{}_\mu = \eta_{\mu\nu}T^{\mu\nu} = (\rho+p)(u\cdot u) - p\,\eta_{\mu\nu}\eta^{\mu\nu} = (\rho+p) - 4p = \rho - 3p$. So a *traceless* perfect fluid is exactly one with $p = \rho/3$ — radiation. This is the quickest way to see that a photon gas must have $p = \rho/3$: the electromagnetic tensor is traceless.

**Corollary — the energy density is recovered by double contraction.** Contracting twice with the four-velocity, $T_{\mu\nu}u^\mu u^\nu = (\rho+p)(u\cdot u)^2 - p(u\cdot u) = (\rho+p) - p = \rho$, confirming that $\rho$ is the energy density a comoving observer measures. Contracting once and projecting, $\perp_{\mu\alpha}T^{\alpha}{}_\nu u^\nu = 0$, confirms there is no rest-frame momentum density.

**Calibration check.** If you have understood the definition you should be able to: (i) write out $T^{\mu\nu}$ in the rest frame and confirm it is $\mathrm{diag}(\rho,p,p,p)$; (ii) compute the trace $T^\mu{}_\mu = \rho - 3p$ and deduce that radiation has $p = \rho/3$; (iii) explain why setting $p = 0$ gives dust and why dust has parallel, non-interacting fluid lines.

---

# Unlocked by This

> [!tip] The Relativistic Euler Equation *(from §24.2)*
> With the perfect-fluid tensor in hand, the entire dynamics is the conservation law $\nabla_\mu T^{\mu\nu} = 0$. Projecting it orthogonal to the four-velocity gives the [[Thm - Relativistic Euler Equation|relativistic Euler equation]], "$\mathbf{a} = \mathbf{F}/(\rho+p)$" with the proper enthalpy density as inertia; projecting along the four-velocity gives the energy equation and, for a closed fluid, the conservation of entropy along the flow.

> [!tip] The Tolman–Oppenheimer–Volkoff Equation and Stellar Structure *(from General Relativity)*
> Placed in a static, spherically symmetric general-relativistic spacetime, the perfect fluid obeys the **Tolman–Oppenheimer–Volkoff equation** of hydrostatic equilibrium, $dp/dr = -(\rho+p)(m+4\pi r^3 p)/[r(r-2m)]$. Closed with an equation of state, it determines the mass–radius relation of **white dwarfs** and **neutron stars** and the maximum mass beyond which no equilibrium exists and the star collapses to a black hole. The inertia-from-enthalpy fact of this page becomes, in the gravitating case, the fact that pressure itself gravitates — the $(\rho + p)$ and the $4\pi r^3 p$ in the numerator.

> [!tip] The Friedmann Cosmology *(from Cosmology)*
> A homogeneous, isotropic universe is forced to have a perfect-fluid source, because isotropy forbids any preferred spatial direction and hence any shear or heat flux. Feeding $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ (with the metric curved to the Friedmann–Lemaître–Robertson–Walker form) into the **Einstein equations** gives the **Friedmann equations** for the scale factor $a(t)$, and the conservation law gives $\dot\rho + 3(\dot a/a)(\rho+p) = 0$. With $p = w\rho$ this fixes how each component dilutes: matter as $a^{-3}$, radiation as $a^{-4}$, dark energy as a constant.
