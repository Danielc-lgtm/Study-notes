---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Perfect Fluid"
  - "Thm - Energy-Momentum Conservation projected (Euler + energy equation)"
  - "Def - Baryon Four-Current and Its Conservation"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A **dust** (pressureless fluid) is the perfect fluid obtained by setting $p = 0$.

1. Write down the energy–momentum tensor of dust and verify it is the $p\to 0$ limit of the perfect-fluid tensor.
2. Impose conservation $\nabla_\mu T^{\mu\nu} = 0$ and show it splits into (i) a conservation law for the mass density and (ii) the equation of motion $a^\mu = 0$, i.e. dust free-falls along geodesics (straight worldlines in flat spacetime).
3. Interpret physically: why does pressureless matter move force-free, and why is $T^{\mu\nu} = \rho\,u^\mu u^\nu$ exactly the form for a swarm of non-interacting particles sharing one four-velocity?

**Recall:**

![[Def - Perfect Fluid#The Definition]]

For dust the proper energy density is $\rho = \rho_{\mathrm m}c^2$ with $\rho_{\mathrm m}$ the rest-mass density (with $c=1$, $\rho = \rho_{\mathrm m}$). The four-acceleration is $a^\mu = u^\nu\nabla_\nu u^\mu$ (see [[Def - Four-Velocity and Four-Acceleration]]); a worldline with $a^\mu = 0$ is a geodesic, a straight line in flat spacetime. Baryon (mass) conservation is $\nabla_\mu(\rho_{\mathrm m}u^\mu) = 0$ (see [[Def - Baryon Four-Current and Its Conservation]]).

---

# Convergent Strategy

**Problem class.** A *derive-an-equation-by-projection* problem in its simplest instance, referencing the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]]. The general method — project $\nabla_\mu T^{\mu\nu} = 0$ along and orthogonal to $u$ — applies, but with $p = 0$ the projections collapse to especially clean statements.

**Assumption pattern.** The single simplifying assumption is $p = 0$. This removes the pressure-gradient force entirely, so the orthogonal projection (which generically gives the Euler equation with a $-\nabla p$ force) becomes force-free, and the parallel projection (the energy equation) becomes pure mass conservation. The signpost is "pressureless" or "dust" or "cold collisionless matter".

**Theorem routing.** Apply [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)|the projection theorem]] with $p = 0$. The parallel projection gives $u^\mu\nabla_\mu\rho + \rho\nabla_\mu u^\mu = 0$, i.e. $\nabla_\mu(\rho u^\mu) = 0$, mass conservation. The orthogonal projection gives $\rho\,a^\mu = 0$, hence $a^\mu = 0$.

**Key decision point.** The one thing to notice is that with $p = 0$ the inertia $\rho + p$ becomes just $\rho$, and since $\rho > 0$ the equation $\rho\,a^\mu = 0$ forces $a^\mu = 0$ — there is no pressure gradient to provide a force, so the only consistent motion is force-free. The natural wrong move is to expect some residual force; there is none.

---

# Legal Operations Used

1. **Project the conservation law along the four-velocity** (operation 1 from the topic page): contracting $\nabla_\mu T^{\mu\nu} = 0$ with $u_\nu$ gives the energy equation, here pure mass conservation since $p = 0$.

2. **Project the conservation law orthogonal to the four-velocity** (operation 2): applying the orthogonal projector gives $\rho\,a^\mu = 0$, the force-free equation of motion.

3. **Use the unit-norm identity $u\cdot a = 0$** (operation 3): confirms the four equations of the orthogonal projection are the three rest-space components.

---

# Hints

> [!note]- Hint 1
> Set $p = 0$ in $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$. The metric term vanishes and you are left with $T^{\mu\nu} = \rho\,u^\mu u^\nu$.

> [!note]- Hint 2
> Take the divergence by the product rule: $\nabla_\mu(\rho u^\mu u^\nu) = \nabla_\mu(\rho u^\mu)u^\nu + \rho u^\mu\nabla_\mu u^\nu = \nabla_\mu(\rho u^\mu)u^\nu + \rho\,a^\nu$. The two terms are orthogonal (one along $u$, one across, since $u\cdot a = 0$), so each must vanish separately.

> [!note]- Hint 3
> The term along $u$ gives $\nabla_\mu(\rho u^\mu) = 0$ (mass conservation); the term across $u$ gives $\rho\,a^\nu = 0$, hence $a^\nu = 0$ since $\rho > 0$. Geodesic motion.

---

# Solution

The dust tensor is $T^{\mu\nu} = \rho\,u^\mu u^\nu$, and its conservation splits cleanly because the two terms in its divergence point in orthogonal directions: the part along $u$ is mass conservation, the part across $u$ is the force-free equation $a^\mu = 0$.

**Step 1: The dust tensor is the $p\to 0$ perfect fluid.**

> [!note]- Derivation
> The [[Def - Perfect Fluid|perfect-fluid tensor]] is $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$. Setting $p = 0$,
> $$T^{\mu\nu} = \rho\,u^\mu u^\nu.$$
> In the rest frame this is $\mathrm{diag}(\rho, 0, 0, 0)$ — pure energy density, zero stress, confirming pressurelessness. This is the energy–momentum tensor of a swarm of non-interacting particles all sharing the four-velocity $u$ at each event: summing the single-particle tensors $m_a c\int u_a\otimes u_a\,\delta\,d\tau$ and using the common four-velocity collapses the sum to $\rho_{\mathrm m}c^2\,u\otimes u$ with $\rho_{\mathrm m}$ the rest-mass density, i.e. $\rho\,u\otimes u$ with $\rho = \rho_{\mathrm m}c^2$.

**Step 2: Conservation splits into mass conservation and geodesic motion.**

> [!note]- Derivation
> Take the divergence and use the product rule:
> $$\nabla_\mu T^{\mu\nu} = \nabla_\mu(\rho u^\mu)\,u^\nu + \rho\,u^\mu\nabla_\mu u^\nu = \nabla_\mu(\rho u^\mu)\,u^\nu + \rho\,a^\nu = 0,$$
> with $a^\nu = u^\mu\nabla_\mu u^\nu$ the four-acceleration.
>
> *Parallel projection.* Contract with $u_\nu$. Since $u_\nu u^\nu = 1$ and $u_\nu a^\nu = 0$ (differentiating $u\cdot u = 1$ gives orthogonality of the four-acceleration, [[Def - Four-Velocity and Four-Acceleration]]),
> $$\nabla_\mu(\rho u^\mu) = 0,$$
> the conservation of mass (equivalently, the [[Def - Baryon Four-Current and Its Conservation|baryon/mass current]] $\rho_{\mathrm m}u^\mu$ is conserved).
>
> *Orthogonal projection.* Having shown the $u^\nu$ term vanishes via mass conservation, the remaining equation is $\rho\,a^\nu = 0$. Since $\rho > 0$,
> $$a^\nu = 0:$$
> the dust worldlines are geodesics — in flat spacetime, straight lines traversed at constant four-velocity. Dust free-falls.

> [!note]- Complete formal solution
> Dust is the perfect fluid with $p = 0$, so $T^{\mu\nu} = \rho\,u^\mu u^\nu$. Its divergence is $\nabla_\mu(\rho u^\mu)u^\nu + \rho\,a^\nu$ with $a^\nu = u^\mu\nabla_\mu u^\nu$. Contracting $\nabla_\mu T^{\mu\nu} = 0$ with $u_\nu$ and using $u\cdot u = 1$, $u\cdot a = 0$ gives $\nabla_\mu(\rho u^\mu) = 0$ (mass conservation); the residual equation is then $\rho\,a^\nu = 0$, and since $\rho > 0$, $a^\nu = 0$ (geodesic motion). Physically, with no pressure there is no force, so each fluid element moves inertially; the tensor $\rho\,u^\mu u^\nu$ is exactly that of non-interacting particles sharing one four-velocity, whose parallel worldlines exchange no momentum and hence support no pressure. $\blacksquare$

**Frame-invariance check.** In the rest frame, $T^{\mu\nu} = \mathrm{diag}(\rho,0,0,0)$ and $\nabla_\mu T^{\mu\nu} = 0$ reads $\partial_t\rho = 0$ (for static dust) and no spatial force — consistent with $a = 0$ and mass conservation. The split is the same in every frame because it is a tensor (projection) statement.

---

# Key Takeaways

**Pressurelessness is the absence of a force, hence geodesic motion.** The cleanest lesson of this exercise is that the pressure gradient is the *only* force a perfect fluid feels (in the absence of external forces), so when the pressure vanishes the fluid moves force-free — its worldlines are geodesics, straight lines in flat spacetime. This is why dust is the matter model for anything cold and collisionless: galaxies in cosmology, cold dark matter, a cloud of free-falling particles. The trigger to reach for dust is any phrase like "pressureless", "collisionless", "cold", or "non-interacting particles". The transferable diagnostic is that the inertia $\rho + p$ collapses to $\rho$, and since $\rho > 0$ the equation of motion $\rho\,a^\mu = 0$ leaves no room for acceleration. In general relativity this same fact becomes the statement that dust follows spacetime geodesics — the matter that defines free fall.

**The divergence of $\rho\,u\otimes u$ splits by orthogonality.** The structural move worth internalising is that $\nabla_\mu(\rho u^\mu u^\nu)$ has two pieces, one proportional to $u^\nu$ (along the flow) and one proportional to $a^\nu$ (across the flow, since $u\cdot a = 0$). Because these are orthogonal four-vectors, the single equation $\nabla_\mu T^{\mu\nu} = 0$ forces *each* to vanish independently — you get two equations for free. This is the simplest instance of the projection method that runs through the whole chapter: a conserved tensor built from $u$ decomposes its conservation law into a part along $u$ (energy/mass) and a part across $u$ (momentum). Recognising that $u\cdot a = 0$ is what makes the two pieces orthogonal is the key, and it recurs in every projection.

**The tensor $\rho\,u\otimes u$ is the fingerprint of shared four-velocity.** The reason dust has exactly this tensor — and the reason pressure is exactly what is missing — is kinetic. Pressure, microscopically, is the momentum carried across a surface by particles crossing it; if every particle shares the same four-velocity, the worldlines are parallel, nothing crosses between adjacent elements, and there is no pressure. Turning on a *spread* of velocities turns on pressure. So whenever you see $T^{\mu\nu} = \rho\,u^\mu u^\nu$ you should read "all the matter at this event moves together, with no velocity dispersion", and conversely a nonzero pressure signals an isotropic velocity spread. This kinetic picture is the bridge from the continuum tensor to the underlying particles, and it explains why dust is both the simplest fluid and the one with no sound ($c_s = 0$): with no pressure, there is nothing to carry a compression wave.
