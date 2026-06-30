---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Relativistic Euler Equation"
  - "Def - Perfect Fluid"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Problem Statement

Starting from $\nabla_\mu T^{\mu\nu} = 0$ for a perfect fluid:

1. Apply the orthogonal projector $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ to derive the four-dimensional Euler equation $(\rho+p)a^\mu = -(\eta^{\mu\nu} - u^\mu u^\nu)\nabla_\nu p$.
2. Verify that contracting the four-dimensional Euler equation with $u_\mu$ gives $0 = 0$, confirming that the four equations are genuinely the three rest-space components.
3. Show that in the nonrelativistic limit the spatial part becomes the classical Euler equation $\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\rho_{\mathrm m}^{-1}\nabla p$, and identify the relativistic inertia.

**Recall:**

![[Thm - Relativistic Euler Equation#Statement]]

The four-acceleration is $a^\mu = u^\nu\nabla_\nu u^\mu$, orthogonal to $u$ ($u\cdot a = 0$, from differentiating $u\cdot u = 1$); see [[Def - Four-Velocity and Four-Acceleration]]. The orthogonal projector onto the rest space of $u$ is $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$, satisfying $\perp^\mu{}_\nu u^\nu = 0$ (see [[Def - Observer and Local Rest Space]]). The inertia is the proper enthalpy density $\rho + p$ (see [[Def - Perfect Fluid]]).

---

# Convergent Strategy

**Problem class.** A *derive-an-equation-by-projection* problem, extracting the momentum (vector) equation. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], the orthogonal projection of the conservation law gives the equation of motion.

**Assumption pattern.** The perfect-fluid tensor and the unit-norm identity $u\cdot a = 0$ are the ingredients. The signpost for the *orthogonal* projection is that you want the equation of motion (how the velocity changes) rather than the energy balance; the projector $\delta - u\otimes u$ discards the time direction and keeps the rest space.

**Theorem routing.** This is the orthogonal projection of [[Thm - Relativistic Euler Equation|the Euler theorem]]. Apply $\perp^\mu{}_\nu$ to the expanded divergence; the longitudinal term is killed, the acceleration term survives by $u\cdot a = 0$, the pressure gradient is projected to its transverse part.

**Key decision point.** The consistency check (part 2) is the conceptual heart: the four-dimensional Euler equation is manifestly four equations, but contracting with $u_\mu$ gives $0 = 0$ because the right-hand side was projected orthogonal to $u$ and the left-hand side $(\rho+p)a^\mu$ is already orthogonal. So the four equations encode only three independent statements — the rest-space momentum balance. The natural confusion is to think the time component carries extra information; it carries none, and the energy equation (the parallel projection) is the genuinely separate fourth equation.

---

# Legal Operations Used

1. **Project the conservation law orthogonal to the four-velocity** (operation 2 from the topic page): applying $\perp^\mu{}_\nu$ extracts the rest-space equation of motion.

2. **Use the unit-norm identity $u\cdot a = 0$** (operation 3): ensures the acceleration term passes through the projector unchanged and that the time component is trivially satisfied.

3. **Take the nonrelativistic limit** (operation 4): sends the inertia $\rho + p \to \rho_{\mathrm m}c^2$ and recovers classical Euler.

---

# Hints

> [!note]- Hint 1
> Use $\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p = 0$. Apply $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$. The first term has a factor $u^\nu$, killed by $\perp^\mu{}_\nu u^\nu = 0$.

> [!note]- Hint 2
> $\perp^\mu{}_\nu a^\nu = a^\mu - u^\mu(u_\nu a^\nu) = a^\mu$ since $u\cdot a = 0$. And $\perp^\mu{}_\nu\nabla^\nu p = \nabla^\mu p - u^\mu(u^\nu\nabla_\nu p)$. Assemble.

> [!note]- Hint 3
> For part 2, contract $(\rho+p)a^\mu = -\nabla^\mu p - (u^\nu\nabla_\nu p)u^\mu$ with $u_\mu$: left side $(\rho+p)(u\cdot a) = 0$; right side $-(u^\mu\nabla_\mu p) + (u^\nu\nabla_\nu p)(u\cdot u) = -(u\cdot\nabla p) + (u\cdot\nabla p) = 0$. Both sides zero.

> [!note]- Hint 4
> For part 3, the spatial part of $a^\mu$ in the nonrelativistic limit is the material derivative $\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V}$; the inertia $\rho + p \to \rho_{\mathrm m}c^2$, so $(\rho+p)a^i = -\nabla^i p$ becomes $\rho_{\mathrm m}(\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V}) = -\nabla p$.

---

# Solution

The orthogonal projection of the conservation law isolates the transverse pressure gradient as the only force on a fluid element, with the proper enthalpy density $\rho + p$ as the inertia; contracting with $u$ confirms only three of the four components are independent, and the slow limit recovers classical Euler.

**Step 1: The four-dimensional Euler equation.**

> [!note]- Derivation
> Expand the divergence:
> $$\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]\,u^\nu + (\rho+p)a^\nu - \nabla^\nu p = 0.$$
> Apply $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ (recall $\perp^\mu{}_\nu u^\nu = u^\mu - u^\mu(u\cdot u) = 0$ since $u\cdot u = 1$):
> - First term: $\perp^\mu{}_\nu\,\nabla_\alpha[(\rho+p)u^\alpha]\,u^\nu = \nabla_\alpha[(\rho+p)u^\alpha]\,\perp^\mu{}_\nu u^\nu = 0$.
> - Acceleration term: $\perp^\mu{}_\nu(\rho+p)a^\nu = (\rho+p)(a^\mu - u^\mu(u_\nu a^\nu)) = (\rho+p)a^\mu$, using $u\cdot a = 0$.
> - Pressure term: $-\perp^\mu{}_\nu\nabla^\nu p = -(\nabla^\mu p - u^\mu(u^\nu\nabla_\nu p))$.
>
> Assembling,
> $$(\rho+p)a^\mu = -\nabla^\mu p - (u^\nu\nabla_\nu p)u^\mu = -(\eta^{\mu\nu} - u^\mu u^\nu)\nabla_\nu p = -\perp^{\mu\nu}\nabla_\nu p,$$
> the four-dimensional [[Thm - Relativistic Euler Equation|Euler equation]].

**Step 2: Only three independent components.**

> [!note]- Derivation
> Contract the four-dimensional Euler equation with $u_\mu$:
> $$(\rho+p)\,u_\mu a^\mu = -u_\mu\nabla^\mu p - (u^\nu\nabla_\nu p)(u_\mu u^\mu).$$
> Left side: $u_\mu a^\mu = 0$ ([[Def - Four-Velocity and Four-Acceleration|four-acceleration orthogonal to four-velocity]]), so it is zero. Right side: $-u^\mu\nabla_\mu p - (u^\nu\nabla_\nu p)(1) = -(u\cdot\nabla p) + (u\cdot\nabla p) = 0$. Hence $0 = 0$ identically. The $\nu = $ (time) component carries no information; the four-dimensional Euler equation is genuinely the *three* rest-space components of momentum balance. (The fourth equation — the energy equation — comes from the *parallel* projection, see [[Ex - Projecting the conservation law onto the four-velocity]].)

**Step 3: The nonrelativistic limit.**

> [!note]- Derivation
> Relative to an inertial observer, the spatial part of the four-acceleration in the limit $\Gamma \to 1$, $\mathbf{V}/c \to 0$ is the material derivative
> $$a^i \to \frac{\partial V^i}{\partial t} + V^j\frac{\partial V^i}{\partial x^j}.$$
> The inertia is $\rho + p \to \rho_{\mathrm m}c^2$ (since $p/c^2 \ll \rho_{\mathrm m}$ and $\varepsilon_{\mathrm{int}}/c^2 \ll \rho_{\mathrm m}$, so $\rho = \rho_{\mathrm m}c^2 + \varepsilon_{\mathrm{int}} \to \rho_{\mathrm m}c^2$). The spatial Euler equation $(\rho+p)a^i = -\nabla^i p$ (the transverse part of $\nabla p$ becomes the spatial gradient since $u^\mu\nabla_\mu p \to 0$ at leading order) becomes
> $$\rho_{\mathrm m}c^2\Big(\frac{\partial V^i}{\partial t} + V^j\frac{\partial V^i}{\partial x^j}\Big) = -\nabla^i p \quad\Longrightarrow\quad \frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\frac{1}{\rho_{\mathrm m}}\nabla p,$$
> restoring $c$. This is the **classical Euler equation**, with the rest-mass density as inertia.

> [!note]- Complete formal solution
> Apply $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ to the expanded divergence $\nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p = 0$. The longitudinal term dies ($\perp u = 0$), the acceleration survives ($\perp a = a$ by $u\cdot a = 0$), the pressure projects to its transverse part, giving $(\rho+p)a^\mu = -\nabla^\mu p - (u^\nu\nabla_\nu p)u^\mu$. Contracting with $u_\mu$ gives $0 = 0$ (left side $\propto u\cdot a = 0$; right side cancels), so only three components are independent — the rest-space momentum balance. In the limit $\Gamma \to 1$, $\rho + p \to \rho_{\mathrm m}c^2$, the spatial part becomes $\partial_t\mathbf{V} + (\mathbf{V}\cdot\nabla)\mathbf{V} = -\rho_{\mathrm m}^{-1}\nabla p$, the classical Euler equation, with the relativistic inertia $\rho + p$ revealed as the promotion of the rest-mass density. $\blacksquare$

---

# Key Takeaways

**The orthogonal projection isolates the transverse pressure gradient as the only force.** The structural lesson is that projecting $\nabla_\mu T^{\mu\nu} = 0$ orthogonal to $u$ produces exactly "$(\text{inertia})\times(\text{acceleration}) = (\text{transverse pressure force})$", which is Newton's second law for a fluid element. The projector does three jobs at once: it kills the longitudinal term (a multiple of $u^\nu$), it leaves the four-acceleration untouched (because $u\cdot a = 0$), and it strips the pressure gradient of its time component, leaving only the part that can change the *direction* of the flow. The transferable diagnostic is that for a perfect fluid the pressure gradient is the only internal force, and only its transverse part appears in the equation of motion — the longitudinal part goes into the energy equation instead. This clean separation is the payoff of the projection method and recurs whenever a conserved tensor is split by a preferred four-velocity.

**Four components, three equations: the time component is automatically satisfied.** The check that contracting with $u_\mu$ gives $0 = 0$ is more than a formality — it is the statement that the relativistic Euler equation, though written as four equations, contains only three independent ones, the rest-space momentum balance. The reason is built into the construction: the right-hand side was projected orthogonal to $u$, and the left-hand side $(\rho+p)a^\mu$ is automatically orthogonal to $u$, so both sides have zero $u$-component identically. The lesson to carry forward is that whenever you write a manifestly covariant equation of motion of the form "(inertia)$\times a^\mu$ = (orthogonal force)", the time component is free, and the genuinely independent fourth equation must be sought elsewhere — here, in the energy equation from the parallel projection. This is the relativistic analogue of the fact that the constraint $u\cdot u = 1$ removes one degree of freedom from the four-velocity.

**The inertia is $\rho + p$, and the slow limit proves it.** The nonrelativistic limit is not a mere consistency check; it is the procedure that *names* the relativistic inertia. The relativistic equation has $\rho + p$ in front of the acceleration; only by sending $\Gamma \to 1$ and watching $\rho + p \to \rho_{\mathrm m}c^2$ does one see that this combination is the relativistic promotion of the rest-mass density. The physical content — that pressure contributes to inertia — is invisible classically because $p$ is negligible against $\rho_{\mathrm m}c^2$, and it is the genuinely new relativistic effect that the limit erases. The trigger for vigilance: any time a relativistic fluid equation has a coefficient in front of the acceleration, check whether it is the enthalpy density $\rho + p$ rather than the mass density, because the difference is the inertia of pressure, the fluid face of $E = mc^2$.
