---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Perfect Fluid"
  - "Thm - Energy-Momentum Conservation"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ (restored where the structure is clearer) and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The fluid is a [[Def - Perfect Fluid|perfect fluid]] with energy–momentum tensor $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$, four-velocity $u$ ($u\cdot u = 1$), proper energy density $\rho$, and pressure $p$. The four-acceleration of the fluid is $a^\mu = u^\nu\nabla_\nu u^\mu$ (see [[Def - Four-Velocity and Four-Acceleration]]). An external four-force density $f^\mu$ may act, decomposed relative to an inertial observer $\mathcal{O}$ of four-velocity $u_0$ into a power density and a force density. Relative to $\mathcal{O}$, the fluid three-velocity is $\mathbf{V}$ (so $u = \Gamma(u_0 + \mathbf{V})$ with $\Gamma = u\cdot u_0$), the energy density is $E = \Gamma^2(\rho+p) - p$, and $\nabla_\perp$ is the spatial gradient in $\mathcal{O}$'s rest space. The orthogonal projector onto $\mathcal{O}$'s rest space is $\perp^\mu{}_\nu = \delta^\mu_\nu - u_0^\mu u_{0\nu}$ (see [[Def - Observer and Local Rest Space]]). Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

---

# Statement

> **Relativistic Euler equation (four-dimensional form).** For a [[Def - Perfect Fluid|perfect fluid]] subject to an external four-force density $f^\mu$, the conservation law $\nabla_\mu T^{\mu\nu} = f^\nu$ projected orthogonal to the four-velocity gives
> $$(\rho + p)\,a^\mu \;=\; -\,\perp^{\mu\nu}_{(u)}\nabla_\nu p \;+\; \perp^{\mu\nu}_{(u)} f_\nu, \qquad \perp^{\mu\nu}_{(u)} = \eta^{\mu\nu} - u^\mu u^\nu,$$
> where $a^\mu = u^\nu\nabla_\nu u^\mu$ is the fluid four-acceleration. Equivalently, written out,
> $$(\rho+p)\,a^\mu = -\nabla^\mu p - (u^\nu\nabla_\nu p)\,u^\mu + f^\mu - (f\cdot u)\,u^\mu.$$

> **Relativistic Euler equation (3+1 form, relative to an inertial observer $\mathcal{O}$).** In terms of the fluid three-velocity $\mathbf{V}$, the energy density $E$, and the pressure $p$ measured by $\mathcal{O}$ (with $c$ restored),
> $$\frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V}\cdot\nabla)\mathbf{V} \;=\; -\frac{c^2}{E+p}\left[\nabla_\perp p + \frac{1}{c^2}\left(\frac{\partial p}{\partial t} + P_{\mathrm{ext}}\right)\mathbf{V}\right] + \frac{c^2}{E+p}\,\mathbf{F}_{\mathrm{ext}}.$$
> In the nonrelativistic limit ($\Gamma \to 1$, $\mathbf{V}/c \to 0$, $p/c^2 \ll \rho_{\mathrm m}$, $\varepsilon_{\mathrm{int}}/c^2 \ll \rho_{\mathrm m}$, so $E + p \to \rho_{\mathrm m}c^2$) this reduces to the **classical Euler equation**
> $$\frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\frac{1}{\rho_{\mathrm m}}\nabla p + \frac{1}{\rho_{\mathrm m}}\mathbf{F}_{\mathrm{ext}}.$$

The four-dimensional form is also called the **four-dimensional Euler equation**; it is "$\mathbf{a} = \mathbf{F}/m$" for a fluid element, with the effective inertia the proper enthalpy density $\rho + p$.

---

# Motivation

Newton's second law for a fluid is the Euler equation: the acceleration of a fluid element equals the force per unit mass, the force being supplied by the pressure gradient. Relativistic hydrodynamics needs the analogue, and the question this theorem answers is exactly which equation plays that role when the flow is fast or the matter hot, and what the inertia of a fluid element becomes.

The answer is delivered by a projection, and that is the conceptual heart of the result. The dynamics of any continuous medium is the single conservation law $\nabla_\mu T^{\mu\nu} = f^\nu$ ([[Thm - Energy-Momentum Conservation]]). This is a four-component equation, and a fluid dynamicist expects two things from it: an energy equation and an equation of motion. The four-velocity field gives spacetime, at each event, a preferred timelike direction; projecting the conservation law *along* that direction extracts the energy equation, and projecting *orthogonal* to it extracts the three components of the equation of motion. The relativistic Euler equation is the orthogonal projection. It is the precise statement of how the momentum of a perfect fluid evolves, and it is the equation that must reduce to classical Euler in the slow limit if relativity is to be consistent with everything we know about ordinary fluids.

The single most important feature of the result is what sits in front of the acceleration. Classically it is the mass density; here it is $\rho + p$, the proper enthalpy density. This is not a notational accident: pressure carries momentum flux, and accelerating a fluid element means pushing that flux around, so a fluid under pressure is harder to accelerate than its rest mass would suggest. The combination $\rho + p$ is the inertia of a relativistic fluid element, and the appearance of pressure there is the fluid-dynamical face of the inertia of energy. In the nonrelativistic limit the pressure becomes negligible against the rest-mass energy and $\rho + p$ collapses to the mass density, which is why the classical Euler equation never sees this effect.

The theorem also closes a logical loop with the energy equation. The four equations of the orthogonal projection look like four, but contracting the four-dimensional form with $u_\mu$ gives $0 = 0$ — the four-velocity component is automatically satisfied, because the right-hand side has been arranged (by subtracting the $u$-components) to be orthogonal to $u$. So the orthogonal projection genuinely yields three independent equations, the rest-space components, and the missing fourth equation is the energy equation obtained by the *parallel* projection. The two projections together exhaust the content of $\nabla_\mu T^{\mu\nu} = f^\nu$.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the medium is a perfect fluid and its energy–momentum is conserved (up to an external force)". The point of input broadening is to recognise the disguises that hypothesis wears.

The first disguised source is **"the medium is isotropic in its rest frame and conduction-free"**. This is the physical, rather than tensorial, statement of the perfect-fluid condition (see [[Def - Perfect Fluid]]): a single pressure, no shear, no heat flux. Whenever a problem describes matter that, in its own rest frame, has one pressure pushing equally in all directions and no energy flowing relative to itself — an ideal gas, a photon gas, cold degenerate matter, cosmological matter — the perfect-fluid tensor applies and so does this theorem. The bridge is the reconstruction of $(\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ from rest-frame isotropy. *Example problem:* derive the equation of motion of the radiation fluid ($p = \rho/3$) in the early universe.

The second disguised source is **"the matter is the source of an Einstein-equation problem with a fluid"**. In general relativity, $\nabla_\mu T^{\mu\nu} = 0$ is not a postulate but an identity forced by the contracted Bianchi identity. So in any general-relativistic problem with a perfect-fluid source — a star, a cosmology — the conservation law holds automatically, and its orthogonal projection is the (curved-space) relativistic Euler equation. The bridge is $\nabla_\mu G^{\mu\nu} = 0 \Rightarrow \nabla_\mu T^{\mu\nu} = 0$. *Example problem:* obtain the Tolman–Oppenheimer–Volkoff equation of stellar hydrostatic equilibrium as the static, spherical specialisation.

The third disguised source is **"a dust cloud", i.e. pressureless matter**. Setting $p = 0$ is a special case of the perfect fluid, and the theorem then says $\rho\,a^\mu = 0$, i.e. $a^\mu = 0$: dust free-falls along geodesics. Whenever a problem treats matter as cold and collisionless — galaxies as point masses, cold dark matter — this is the relevant limit. The bridge is "$p = 0$ in the perfect-fluid tensor". *Example problem:* show that the worldlines of a pressureless cosmological fluid are geodesics; see [[Ex - Dust as the pressureless limit of a perfect fluid]].

**Targets (Output Amplification)**

The conclusion is the equation of motion $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu$.

Combine the conclusion with **the nonrelativistic expansion** $\Gamma \simeq 1$, $E + p \to \rho_{\mathrm m}c^2$. The further result is the classical Euler equation, and the combination is what assigns physical meaning to the relativistic inertia: the limit shows that $\rho + p$ is the relativistic promotion of the mass density. This is useful both as a consistency check and as the dictionary that names the relativistic quantities. *Example:* recover $\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\rho_{\mathrm m}^{-1}\nabla p$.

Combine the conclusion with **a static, spherically symmetric, gravitating configuration**. With gravity (a curved metric) and the requirement $\partial_t = 0$ and radial symmetry, the orthogonal projection of $\nabla_\mu T^{\mu\nu} = 0$ becomes the **Tolman–Oppenheimer–Volkoff equation** $dp/dr = -(\rho+p)(m+4\pi r^3 p)/[r(r-2m)]$. The combination is nonobvious because it fuses the fluid equation of motion with the Einstein equations, and it is the foundation of neutron-star structure. *Example:* the maximum-mass bound for neutron stars.

Combine the conclusion with **a linearised adiabatic perturbation about a homogeneous background**. Together with the energy equation, the linearised Euler equation gives a wave equation whose propagation speed is the speed of sound $c_s^2 = (\partial p/\partial\rho)_S$ (see [[Def - Equation of State and Speed of Sound]]). The combination is useful because it extracts the characteristic speed of the hydrodynamic system, controlling causality, hyperbolicity, and the existence of shocks. *Example:* show that the radiation fluid has $c_s = 1/\sqrt3$; see [[Ex - The speed of sound from linearised perturbations]].

---

# Why Is It True

The reason the theorem holds is that the conservation law $\nabla_\mu T^{\mu\nu} = 0$ has exactly four components, and the four-velocity field lets you sort them into "along the flow" (one component, energy) and "across the flow" (three components, momentum). The relativistic Euler equation is the across-the-flow part, and it must look like "$\mathbf{a} = \mathbf{F}/(\text{inertia})$" because that is what the spatial momentum balance of any mechanical system looks like.

**The mechanism in one sentence: feeding the perfect-fluid tensor into $\nabla_\mu T^{\mu\nu} = 0$ and projecting orthogonal to $u$ isolates the pressure gradient transverse to the flow as the only force on a fluid element, with the proper enthalpy density $\rho + p$ as the inertia.**

Take it slowly. Substitute $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ into the divergence and use the product rule:
$$\nabla_\mu T^{\mu\nu} = \nabla_\mu\big[(\rho+p)u^\mu\big]u^\nu + (\rho+p)u^\mu\nabla_\mu u^\nu - \nabla^\nu p.$$
The middle term is $(\rho+p)a^\nu$ — the inertia times the four-acceleration, already visible. The first term points along $u$ (it is a scalar times $u^\nu$), and the last term, the pressure gradient, has both a piece along $u$ and a piece across it. Now project orthogonal to $u$. The piece along $u$ in the first term is annihilated by the projector. The four-acceleration is *already* orthogonal to $u$ — because differentiating $u\cdot u = 1$ gives $u\cdot a = 0$ — so it survives the projection unchanged. The pressure gradient loses its $u$-component, leaving only its transverse part $-\perp^{\mu\nu}\nabla_\nu p$. What remains is exactly $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p$: the transverse pressure gradient accelerates the fluid element, with inertia $\rho+p$.

Why must the inertia be $\rho + p$ rather than $\rho$? Because the energy–momentum tensor's "flow of momentum" includes the pressure. The momentum density of the fluid relative to a moving observer is $(E+p)\mathbf{V}/c^2$, not $E\mathbf{V}/c^2$: the pressure adds to the momentum carried by the flow, because a moving pressurised fluid transports the work done by pressure. When you ask how hard it is to change that momentum — which is what an equation of motion measures — the pressure comes along, and the inertia is the enthalpy density $\rho + p$. This is the same physics as the inertia of energy in $E = mc^2$, now applied to the internal energy and pressure of a continuum, and it is invisible nonrelativistically only because $p$ is then utterly negligible against $\rho_{\mathrm m}c^2$.

Why is the transverse pressure gradient the only force (absent external forces)? Because a perfect fluid has, by definition, no shear and no conduction — the only stress is the isotropic pressure. An isotropic pressure pushes a fluid element only where the pressure is *unbalanced*, i.e. along its gradient, and only the component of that gradient transverse to the flow can change the *direction* of the four-velocity (the longitudinal component goes into the energy equation, changing the magnitude of the energy). So the spatial equation of motion sees exactly the transverse pressure gradient, which is the classical statement "fluid accelerates down the pressure gradient" lifted to four dimensions.

---

# What Makes This Hard

The conceptual hurdle is not the algebra but recognising that one tensor equation contains both the energy equation and the equation of motion, and that the projector is what separates them — most people expect to need two independent postulates and are surprised that momentum balance is just the orthogonal shadow of energy–momentum conservation. The non-obvious step is using $u\cdot a = 0$ (from differentiating the normalisation $u\cdot u = 1$) to see that the four-acceleration survives the orthogonal projection untouched while the longitudinal pieces are killed. The most common error is to forget the pressure in the inertia and write $\rho\,a^\mu$ or even $\rho_{\mathrm m}a^\mu$ instead of $(\rho+p)a^\mu$, importing the nonrelativistic mass density where the proper enthalpy density belongs.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Substitute the perfect-fluid tensor into $\nabla_\mu T^{\mu\nu} = f^\nu$, use the product rule to expose the four-acceleration term $(\rho+p)a^\nu$, then apply the orthogonal projector $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ (with respect to the *fluid* four-velocity). The identity $u\cdot a = 0$ makes the acceleration term invariant under the projection and kills the longitudinal scalar terms, leaving the transverse pressure gradient as the only force.

**Subgoal decomposition:**

1. **Expand the divergence of the perfect-fluid tensor.** Show $\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p$.
   - *Hint:* Apply the product rule to $(\rho+p)u^\mu u^\nu$ and use $u^\mu\nabla_\mu u^\nu = a^\nu$; the divergence of $-p\,\eta^{\mu\nu}$ is $-\nabla^\nu p$.
   - *Why needed:* It exposes the inertia-times-acceleration term and sorts the rest into longitudinal and transverse pieces.

2. **Record the unit-norm identity.** Show $u_\nu a^\nu = 0$.
   - *Hint:* Differentiate $u_\nu u^\nu = 1$ along $u$.
   - *Why needed:* It guarantees the acceleration term passes through the orthogonal projector unchanged.

3. **Apply the orthogonal projector.** Contract the expanded divergence with $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$.
   - *Hint:* The first term is a scalar times $u^\nu$, killed by the projector; $\perp^\mu{}_\nu a^\nu = a^\mu$ by step 2; the pressure gradient loses its $u$-component.
   - *Why needed:* It is the projection that isolates the rest-space (momentum) equation.

4. **Read off the four-dimensional Euler equation.** Conclude $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu$, equivalently $(\rho+p)a^\mu = -\nabla^\mu p - (u^\nu\nabla_\nu p)u^\mu + f^\mu - (f\cdot u)u^\mu$.
   - *Hint:* Write $\perp^{\mu\nu}\nabla_\nu p = \nabla^\mu p - u^\mu(u^\nu\nabla_\nu p)$.
   - *Why needed:* It is the statement of the theorem.

5. **(3+1 form and limit.)** Decompose relative to an inertial observer using $u = \Gamma(u_0 + \mathbf{V})$ and $E = \Gamma^2(\rho+p) - p$, then send $\Gamma \to 1$, $E + p \to \rho_{\mathrm m}c^2$.
   - *Hint:* The four-acceleration's spatial part is the material derivative $\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V}$ in the limit; the inertia $E + p$ becomes $\rho_{\mathrm m}c^2$.
   - *Why needed:* It identifies the relativistic equation with the classical Euler equation and names the inertia.

---

# Lemma Decomposition

> [!note]- Lemma 1: Divergence of the perfect-fluid tensor
> **Statement:** $\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]\,u^\nu + (\rho+p)\,a^\nu - \nabla^\nu p$, where $a^\nu = u^\mu\nabla_\mu u^\nu$.
>
> **Hint:** Product rule on $(\rho+p)u^\mu u^\nu$; the metric is covariantly constant so $\nabla_\mu(-p\,\eta^{\mu\nu}) = -\nabla^\nu p$.
>
> **Why needed:** It is the raw form of the conservation law for a perfect fluid, before projection, exposing the inertia-times-acceleration term.
>
> > [!note]- Full proof
> > Write $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$. Then
> > $$\nabla_\mu T^{\mu\nu} = \nabla_\mu\big[(\rho+p)u^\mu u^\nu\big] - \nabla_\mu(p\,\eta^{\mu\nu}).$$
> > For the first term, the product rule gives $\nabla_\mu[(\rho+p)u^\mu]\,u^\nu + (\rho+p)u^\mu\nabla_\mu u^\nu$, and $u^\mu\nabla_\mu u^\nu = a^\nu$ is the four-acceleration. For the second term, since the metric is covariantly constant, $\nabla_\mu(p\,\eta^{\mu\nu}) = \eta^{\mu\nu}\nabla_\mu p = \nabla^\nu p$. Combining,
> > $$\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]\,u^\nu + (\rho+p)\,a^\nu - \nabla^\nu p. \qquad \blacksquare$$

> [!note]- Lemma 2: The four-acceleration is orthogonal to the four-velocity
> **Statement:** $u_\nu a^\nu = 0$, where $a^\nu = u^\mu\nabla_\mu u^\nu$.
>
> **Hint:** Differentiate the normalisation $u_\nu u^\nu = 1$ along the flow.
>
> **Why needed:** It ensures the acceleration term survives the orthogonal projection unchanged, and is the single identity that makes the projection clean.
>
> > [!note]- Full proof
> > The four-velocity is a unit vector, $u_\nu u^\nu = 1$ (a constant). Differentiate along the flow with $u^\mu\nabla_\mu$:
> > $$0 = u^\mu\nabla_\mu(u_\nu u^\nu) = 2\,u_\nu\,u^\mu\nabla_\mu u^\nu = 2\,u_\nu a^\nu,$$
> > using metric compatibility to move $\nabla$ past the index lowering. Hence $u_\nu a^\nu = 0$: the four-acceleration is orthogonal to the four-velocity (in particular it is spacelike). $\blacksquare$

> [!note]- Lemma 3: The orthogonal projection isolates the transverse pressure gradient
> **Statement:** Applying $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ to $\nabla_\alpha T^{\alpha\nu} = f^\nu$ gives $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu$.
>
> **Hint:** The longitudinal term $\nabla_\alpha[(\rho+p)u^\alpha]u^\nu$ is killed by the projector; the acceleration term is unchanged by Lemma 2; the pressure gradient loses its $u$-component.
>
> **Why needed:** This is the projection step that produces the equation of motion; it is the whole content of the theorem.
>
> > [!note]- Full proof
> > Start from Lemma 1 with the external force: $\nabla_\alpha[(\rho+p)u^\alpha]u^\nu + (\rho+p)a^\nu - \nabla^\nu p = f^\nu$. Contract with the projector $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$, which satisfies $\perp^\mu{}_\nu u^\nu = u^\mu - u^\mu(u\cdot u) = 0$ since $u\cdot u = 1$.
> >
> > The first term: $\perp^\mu{}_\nu\,\nabla_\alpha[(\rho+p)u^\alpha]u^\nu = \nabla_\alpha[(\rho+p)u^\alpha]\,\perp^\mu{}_\nu u^\nu = 0$.
> >
> > The acceleration term: $\perp^\mu{}_\nu (\rho+p)a^\nu = (\rho+p)(a^\mu - u^\mu(u_\nu a^\nu)) = (\rho+p)a^\mu$, using $u_\nu a^\nu = 0$ from Lemma 2.
> >
> > The pressure term: $\perp^\mu{}_\nu(-\nabla^\nu p) = -(\nabla^\mu p - u^\mu u_\nu\nabla^\nu p) = -\perp^{\mu\nu}\nabla_\nu p$.
> >
> > The force term: $\perp^\mu{}_\nu f^\nu = \perp^{\mu\nu}f_\nu$. Assembling,
> > $$(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu,$$
> > which written out is $(\rho+p)a^\mu = -\nabla^\mu p - (u^\nu\nabla_\nu p)u^\mu + f^\mu - (f\cdot u)u^\mu$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the setup.** The fluid is a [[Def - Perfect Fluid|perfect fluid]], $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ with $u\cdot u = 1$, and its energy–momentum is conserved up to an external four-force density, $\nabla_\mu T^{\mu\nu} = f^\nu$ (see [[Thm - Energy-Momentum Conservation]]). We project orthogonal to the four-velocity.
>
> **Four-dimensional form.** By Lemma 1,
> $$\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]\,u^\nu + (\rho+p)a^\nu - \nabla^\nu p = f^\nu,$$
> with $a^\nu = u^\mu\nabla_\mu u^\nu$. Apply the orthogonal projector $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$. By Lemma 3 — using $\perp^\mu{}_\nu u^\nu = 0$ and the orthogonality $u_\nu a^\nu = 0$ of Lemma 2 — the longitudinal term drops, the acceleration term is preserved, and the pressure gradient is projected, giving
> $$\boxed{(\rho+p)\,a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu = -\nabla^\mu p - (u^\nu\nabla_\nu p)u^\mu + f^\mu - (f\cdot u)u^\mu.}$$
> This is the four-dimensional Euler equation. (Consistency check: contracting with $u_\mu$ gives $(\rho+p)(u\cdot a) = -(u\cdot\nabla p) + (u\cdot\nabla p) + (f\cdot u) - (f\cdot u) = 0$, and $u\cdot a = 0$, so $0 = 0$ — the four equations are genuinely the three rest-space components.)
>
> **3+1 form relative to an inertial observer $\mathcal{O}$.** Decompose with $u = \Gamma(u_0 + \mathbf{V})$, $\Gamma = u\cdot u_0$, and write the fluid energy density measured by $\mathcal{O}$ as $E = \Gamma^2(\rho+p) - p$ and its momentum density as $\boldsymbol\varpi = (E+p)\mathbf{V}/c^2$. The orthogonal projection of $\nabla_\mu T^{\mu\nu} = f^\nu$ onto $\mathcal{O}$'s rest space is the momentum-conservation statement $\partial_t\boldsymbol\varpi + \nabla\cdot S = \mathbf{F}_{\mathrm{ext}}$, where $S = p(\mathbb{1} + \cdots) + (E+p)\mathbf{V}\otimes\mathbf{V}/c^2$ is the stress relative to $\mathcal{O}$. Substituting and using the energy equation $\partial_t E + \nabla\cdot[(E+p)\mathbf{V}] = P_{\mathrm{ext}}$ (the parallel projection) to eliminate $\partial_t E$, and expanding with $\mathcal{O}$ inertial (so $\nabla u_0 = 0$, $\nabla\eta = 0$), one obtains
> $$\frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\frac{c^2}{E+p}\left[\nabla_\perp p + \frac{1}{c^2}\Big(\frac{\partial p}{\partial t} + P_{\mathrm{ext}}\Big)\mathbf{V}\right] + \frac{c^2}{E+p}\mathbf{F}_{\mathrm{ext}}.$$
> The $\nu = 0$ component is identically zero (since $V^0 = 0$, $F^0_{\mathrm{ext}} = 0$), consistent with the four-dimensional check.
>
> **Nonrelativistic limit.** Impose $\Gamma \to 1$, $\mathbf{V}/c \to 0$, and (from $E = \Gamma^2(\rho+p) - p$ with $\rho = \rho_{\mathrm m}c^2 + \varepsilon_{\mathrm{int}}$) the conditions $p/c^2 \ll \rho_{\mathrm m}$, $\varepsilon_{\mathrm{int}}/c^2 \ll \rho_{\mathrm m}$, so that $E + p \simeq \rho_{\mathrm m}c^2$ and $c^2/(E+p) \simeq 1/\rho_{\mathrm m}$. The bracketed correction terms $\propto 1/c^2$ vanish, and
> $$\frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\frac{1}{\rho_{\mathrm m}}\nabla p + \frac{1}{\rho_{\mathrm m}}\mathbf{F}_{\mathrm{ext}},$$
> the classical Euler equation. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Stellar structure and the TOV equation (general relativity).** The relativistic Euler equation, projected for a static spherically symmetric gravitating fluid, becomes the Tolman–Oppenheimer–Volkoff equation $dp/dr = -(\rho+p)(m+4\pi r^3 p)/[r(r-2m)]$, the master equation of neutron-star structure. The appearance is nonobvious because the flat-space momentum balance must be married to the Einstein equations, and both the inertia factor $\rho + p$ and a pressure-gravitates term $4\pi r^3 p$ emerge. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

**Cosmological perturbation theory (cosmology).** Linearising the relativistic Euler equation for the cosmic fluid about a homogeneous expanding background gives the equation governing the growth of density perturbations — the seeds of galaxies. The application is out-of-distribution because the "force" is gravitational and the background is time-dependent, yet the projection structure is identical, and the sound speed $c_s$ sets the Jeans length below which pressure resists collapse.

**Relativistic shock tubes (computational physics).** Casting the conservation law in flux-conservative form exposes a hyperbolic system whose characteristic speeds are built from $c_s$; the relativistic Euler equation then admits discontinuous shock solutions satisfying Rankine–Hugoniot jump conditions. The application is surprising because a smooth differential equation generates discontinuities, and it is the basis of every numerical simulation of relativistic jets and accretion flows.

---

# Bridges

- **[[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]** — the relativistic Euler equation is the *orthogonal* half of the projection of $\nabla_\mu T^{\mu\nu} = f^\nu$; the *parallel* half is the energy equation. The two are complementary projections of one conservation law: contracting with $u_\nu$ gives the scalar energy equation, projecting with $\delta - u\otimes u$ gives this vector equation of motion. Together they exhaust the four components of the conservation law.

- **The classical Euler equation** — the nonrelativistic shadow of this theorem, obtained by sending the inertia $\rho + p$ to the mass density $\rho_{\mathrm m}c^2$. The relativistic equation is primary; the classical one is its slow-motion pronunciation. The construction is explicit in the proof: the four-acceleration becomes the material derivative $\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V}$, and the transverse pressure gradient becomes $-\rho_{\mathrm m}^{-1}\nabla p$.

- **[[Def - Vorticity 2-Form]]** — the same equation of motion, recast in the exterior derivative as the canonical equation $\Omega(u,\cdot) = T\,dS$. Where this theorem uses the covariant derivative and projectors, the canonical form uses only $d$, and it is from the canonical form that Bernoulli, irrotational flow, and Kelvin's theorem descend. The two are equivalent statements of the perfect-fluid dynamics; the form-version is cleaner for conservation laws, the projection-version for the explicit equation of motion.

- **[[Def - Equation of State and Speed of Sound]]** — linearising this equation together with the energy equation produces a wave equation whose speed is the sound speed $c_s^2 = (\partial p/\partial\rho)_S$. The inertia $\rho + p$ that appears here also appears in the denominator of the sound-speed analysis, tying the equation of motion to the characteristic speed of the system.

---

# Unlocked by This

> [!tip] Hydrostatic Equilibrium and the TOV Equation *(from General Relativity)*
> The static specialisation of the relativistic Euler equation, with gravity, is the **Tolman–Oppenheimer–Volkoff equation** of stellar structure. It determines the mass–radius relation of compact stars and the maximum neutron-star mass; the inertia $\rho + p$ of this theorem becomes, with gravity, the statement that pressure gravitates. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] The Jeans Instability and Structure Formation *(from Cosmology)*
> Linearising the relativistic Euler equation in an expanding universe gives the equation for density-perturbation growth. Below the **Jeans length** (set by the sound speed $c_s$) pressure stabilises a region; above it, gravity wins and the perturbation collapses. This is the mechanism by which the smooth early universe grew the **galaxies and clusters** we see, and the sound speed of this chapter is precisely what sets the scale.
