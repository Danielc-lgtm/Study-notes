---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Harmonic Function"
tags: [analysis, complex-analysis, fluid-dynamics]
---

# Notation

$D \subseteq \mathbb{C}$ is a domain (open, path-connected). $z = x + iy \in D$ is a point in the flow domain. $w(z) = \phi(z) + i\psi(z)$ is the **complex potential**, with $\phi$ the **velocity potential** and $\psi$ the **stream function**, both real-valued. The fluid velocity field is $\vec v = (v_x, v_y) = (v_x(x, y), v_y(x, y))$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

Consider a 2D fluid flow that is:
1. **Incompressible**: $\nabla \cdot \vec v = \partial v_x/\partial x + \partial v_y/\partial y = 0$ (no sources/sinks; mass is conserved locally).
2. **Irrotational**: $\nabla \times \vec v = \partial v_y/\partial x - \partial v_x/\partial y = 0$ (no vorticity; the fluid doesn't spin locally).

These two conditions together force $\vec v$ to be the gradient of a scalar potential (irrotationality) *and* the curl of a vector potential (incompressibility). In 2D, these two requirements combine into a single complex-analytic structure: $\vec v$ derives from a **holomorphic** function on the flow domain.

Specifically: irrotationality means $\vec v = \nabla \phi$ for some scalar $\phi$ (the **velocity potential**). Incompressibility then gives $\Delta \phi = 0$, so $\phi$ is harmonic. On a simply connected $D$, $\phi$ has a harmonic conjugate $\psi$ (the **stream function**), and $w = \phi + i\psi$ is holomorphic. The complex velocity is $\bar v = v_x - iv_y$ (note the conjugate), and computation shows $\bar v = dw/dz = \phi_x + i\psi_x = \phi_x - i\phi_y = v_x - iv_y$. So the holomorphic function $w$ encodes the entire velocity field via differentiation.

Why "complex" and not just the gradient $\nabla\phi$? Because the complex structure $w = \phi + i\psi$ packages *both* the velocity potential and the stream function into one object, and the holomorphicity is the geometric content of incompressibility + irrotationality together. The stream function has an important physical meaning: level curves $\psi = $ const are *streamlines* — paths the fluid follows. So $w$ encodes both the dynamics ($\phi$, velocity) and the geometry ($\psi$, streamlines) in one holomorphic function.

This is one of the most productive ideas in applied mathematics: **2D incompressible irrotational flow is exactly holomorphic function theory**. Every theorem about holomorphic functions translates to a fact about fluid flow. Singularities of $w$ correspond to physical objects: simple pole = source/sink, logarithmic singularity = vortex, dipole = doublet. Conformal mapping pulls back flows: flow around an obstacle is computed by mapping the exterior of the obstacle to a simple domain.

What about non-incompressible or non-irrotational flows? They are not captured by a single holomorphic function. Compressible flow (high-Mach-number aerodynamics) is described by nonlinear PDEs. Viscous flow (Navier-Stokes) has $\nabla\times\vec v \neq 0$ in general. The complex potential framework is restricted to *inviscid, incompressible, irrotational* flows — the "ideal" idealization, which captures the leading-order behaviour in many physical regimes (low-speed aerodynamics, ocean surface waves, hydrodynamics).

---

# The Definition

Let $D \subseteq \mathbb{C}$ be a simply connected domain representing the flow region. A **complex potential** for a 2D incompressible irrotational flow on $D$ is a holomorphic function
$$w(z) = \phi(z) + i\psi(z), \quad z \in D,$$
where:
- $\phi : D \to \mathbb{R}$ is the **velocity potential**: $\nabla\phi = (v_x, v_y) = \vec v$, the fluid velocity field.
- $\psi : D \to \mathbb{R}$ is the **stream function**: the harmonic conjugate of $\phi$. Level curves $\psi = $ const are streamlines of the flow.

**Complex velocity.** The velocity is recovered from $w$ by
$$\bar v(z) := v_x(z) - iv_y(z) = \frac{dw}{dz}.$$
(Note the complex conjugate: it is $v_x - iv_y$, not $v_x + iv_y$, because of the way the gradient maps under the complex-to-real identification.)

**Boundary condition.** For flow past a solid obstacle $\partial D$, the boundary is a *streamline* — fluid cannot penetrate it. So $\psi = $ constant on $\partial D$ (typically $\psi = 0$).

**Singularities and their physical meaning.**
- **Simple pole** at $a$: $w(z) \sim c/(z - a)$ near $a$. Physically a *source* (if $c$ has the right sign) or *sink*. The "flux" out of a small loop around $a$ is $\operatorname{Re}\oint \bar v\,d\bar z \cdot $ (real factor) = $2\pi \operatorname{Im} c$ (mass flux).
- **Logarithmic singularity** at $a$: $w(z) \sim -i(\Gamma/(2\pi))\log(z - a)$. Physically a *vortex* with circulation $\Gamma = \oint \vec v\cdot d\vec\ell$. The stream function has a logarithmic singularity at the vortex centre; the velocity decays like $1/|z - a|$.
- **Higher-order pole** (dipole, multipole): doublet flows, used in modeling more complex flow geometries.

---

# Relate to Other Fields / Compression

In **electromagnetism**, the same complex-potential framework applies to 2D **electrostatic problems**. A 2D charge distribution gives an electric field $\vec E = \nabla\phi$ with $\phi$ harmonic in charge-free regions. The "complex potential" $\Phi = \phi + i\psi$ is holomorphic, with simple poles at point charges (logarithmic singularities in the corresponding scalar potential — wait, this needs care). The mathematical structure is identical to fluid flow.

In **steady-state heat conduction** in 2D, the temperature satisfies Laplace's equation (in the absence of sources), so it is harmonic. The same complex-potential framework applies: the temperature is the real part of a holomorphic function, and conformal mapping techniques solve heat conduction on complicated geometries.

In **magnetostatics**, the magnetic field of a 2D system can be derived from a complex potential. Currents are vortex singularities; lines of constant $\psi$ are field lines.

In **stokes flow** (very low Reynolds number, almost no inertia), the streamline function $\psi$ satisfies the **biharmonic equation** $\Delta^2 \psi = 0$, not Laplace. This is a higher-order PDE, and the complex-potential framework doesn't apply directly — though related complex techniques exist (e.g., the Muskhelishvili formulation).

---

# Examples / Corollaries

**Is an instance — uniform flow.** $w(z) = U z$ for real $U > 0$. Velocity $\bar v = U$, so $v_x = U, v_y = 0$ — uniform flow in the $x$-direction with speed $U$. Streamlines: $\psi = \operatorname{Im}(Uz) = Uy$, horizontal lines.

**Is an instance — point source at origin.** $w(z) = (m/(2\pi))\log z$ for $m > 0$. Velocity $\bar v = m/(2\pi z)$, magnitude $m/(2\pi|z|)$, direction outward from origin. Streamlines: $\psi = (m/(2\pi))\arg z = $ const → radial lines. The mass flux through any loop around the origin is $m$ (the source strength). Note: $\log z$ requires choosing a branch; on simply connected domains avoiding the origin, this is fine.

**Is an instance — point vortex at origin.** $w(z) = -i(\Gamma/(2\pi))\log z$. Velocity $\bar v = -i\Gamma/(2\pi z) = (-i\Gamma/(2\pi)) \cdot 1/z$. Magnitude $\Gamma/(2\pi|z|)$. Direction: rotating around the origin (the factor $-i$ rotates by $-\pi/2$). Streamlines: circles around the origin. Circulation: $\oint \vec v \cdot d\vec\ell = \Gamma$ (independent of loop choice, by the residue theorem).

**Is an instance — flow past a cylinder.** $w(z) = U(z + a^2/z)$ for a cylinder of radius $a$ in a uniform stream $U$ from $-\infty$. On $|z| = a$ (cylinder boundary): $z + a^2/z = z + a^2/\bar z \cdot |z|^2/|z|^2 = z + \bar z = 2\operatorname{Re}(z)$, so $\psi = \operatorname{Im}(w) = U \operatorname{Im}(z + a^2/z) = U(\operatorname{Im} z - a^2\operatorname{Im} z/|z|^2)$, which equals $0$ on $|z| = a$. So the cylinder boundary is the $\psi = 0$ streamline. See [[Ex - Flow past a cylinder via complex potential]] for the full analysis.

**Is an instance — flow with circulation past a cylinder.** $w(z) = U(z + a^2/z) - i(\Gamma/(2\pi))\log(z/a)$ adds a vortex at the centre to the cylinder flow, giving net circulation $\Gamma$. The boundary $|z| = a$ remains a streamline ($\log(z/a) = \log 1 + i\arg(z/a) = i\arg z$ on $|z| = a$, so adds $\Gamma\arg z/(2\pi)$ to $\psi$, which is constant on $|z| = a$ only as a multivalued function — proper treatment needs branch cuts). The lift (by Kutta–Joukowski) is $L = \rho U \Gamma$.

**Is NOT an instance — turbulent flow.** Turbulent flow has $\nabla \times \vec v \neq 0$ (vorticity is the defining feature), and is not captured by a single holomorphic potential.

**Is NOT an instance — compressible flow.** When the density varies, $\nabla \cdot \vec v \neq 0$, breaking the incompressibility assumption.

---

# Unlocked by This

> [!tip] Joukowski Aerofoil *(from §3.5+ Applications)*
> The [[Thm - Joukowski Aerofoil Construction|Joukowski transformation]] maps cylinder flow to flow past an aerofoil, with the Kutta condition selecting the circulation.

> [!tip] Conformal Maps for Flow Past Obstacles *(from Applications)*
> Conformal mapping pulls back complex potentials from a simple geometry (cylinder, half-plane) to complicated ones (aerofoils, polygons). The pullback is automatic because conformal maps preserve harmonicity.

> [!tip] Kutta–Joukowski Theorem *(from Aerodynamics)*
> The lift on an aerofoil in 2D incompressible flow is $L = \rho U \Gamma$, with $\Gamma$ the circulation. The proof uses the residue at infinity of the complex velocity.

> [!tip] Vortex Dynamics *(from Geophysics)*
> Multiple vortex configurations in 2D (point vortex systems, Kirchhoff's vortex laws) are governed by the dynamics of the complex potential. Used in geophysical fluid dynamics for modeling cyclones and ocean eddies.
