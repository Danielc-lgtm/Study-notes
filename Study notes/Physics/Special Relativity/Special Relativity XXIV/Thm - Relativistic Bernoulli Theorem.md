---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Vorticity 2-Form"
  - "Def - Perfect Fluid"
  - "Def - Equation of State and Speed of Sound"
  - "Thm - Noether Theorem (Relativistic Particle)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ (restored where clearer) and use the mostly-minus signature, $u\cdot u = 1$. The fluid is a simple perfect fluid with four-velocity $u$, enthalpy per baryon $h = (\rho+p)/n$, and entropy per baryon $S = s/n$ (see [[Def - Equation of State and Speed of Sound]]). The fluid momentum one-form is $\pi = h\,u$ and the vorticity two-form is $\Omega = d\pi$, obeying the canonical equation $\Omega(u,\cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]). An inertial observer $\mathcal{O}$ has four-velocity $u_0$, with associated coordinates $(t, x^1, x^2, x^3)$; $\Gamma = u\cdot u_0$ is the fluid Lorentz factor relative to $\mathcal{O}$, and $\mathbf{V}$ the fluid three-velocity. The specific internal enthalpy is $H = (\varepsilon_{\mathrm{int}} + p)/(\rho_{\mathrm m})$ (enthalpy per unit mass, internal part). Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

---

# Statement

> **Relativistic Bernoulli's theorem.** Consider a simple perfect fluid in a flow that is **stationary** with respect to an inertial observer $\mathcal{O}$ of four-velocity $u_0$ (all fluid quantities measured by $\mathcal{O}$ are independent of $\mathcal{O}$'s proper time $t$). Then the scalar $\langle\pi, u_0\rangle$ is constant along each fluid line:
> $$\nabla_u\langle\pi, u_0\rangle = 0, \qquad \langle\pi, u_0\rangle = h\,(u\cdot u_0) = h\,\Gamma.$$
> The conserved scalar is the enthalpy per baryon times the fluid Lorentz factor relative to $\mathcal{O}$.

> **General form (Noether).** The result is a special case: for *any* vector field $G$ generating a symmetry of the flow, the scalar $\langle\pi, G\rangle$ is conserved along each fluid line,
> $$\nabla_u\langle\pi, G\rangle = 0.$$
> Bernoulli is the case $G = u_0$ (time translation); axisymmetry ($G$ a rotation generator) gives a conserved angular momentum per baryon.

In the nonrelativistic limit ($\Gamma \simeq 1 + \tfrac12 V^2$, $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$) the conserved scalar reduces to the **classical Bernoulli constant**: $H + \tfrac12 V^2$ (specific enthalpy plus kinetic energy per unit mass) is constant along each streamline.

---

# Motivation

Bernoulli's theorem is the most-used conservation law in classical fluid dynamics: in a steady flow, the sum of enthalpy and kinetic energy per unit mass is constant along each streamline, so where a fluid speeds up its pressure drops. It is the principle behind lift on a wing, flow through a nozzle, and the Venturi effect. The question this theorem answers is what becomes of it in relativity, and the answer is both cleaner and more general than the classical statement.

The classical proof is a slightly awkward manipulation of the steady Euler equation along a streamline. The relativistic proof is almost trivial *given the right object* — and that object is the fluid momentum one-form $\pi = hu$ and the canonical equation $\Omega(u,\cdot) = T\,dS$ of [[Def - Vorticity 2-Form]]. Bernoulli is just this equation contracted with the symmetry direction. The conserved scalar $\langle\pi, u_0\rangle$ is the projection of the fluid's momentum-per-baryon onto the observer's time direction — physically, the energy per baryon — and stationarity is exactly what makes it constant along the flow.

The deeper content is that Bernoulli is a *Noether theorem* for the fluid. A symmetry of the flow produces a conserved quantity along the fluid lines, exactly as a symmetry of a particle's worldline produces a conserved component of its four-momentum. Here the fluid momentum one-form $\pi = hu$ plays the role that the four-momentum $mcu$ plays for a particle, and $\langle\pi, G\rangle$ is the conserved Noether charge for the symmetry $G$. Stationarity (invariance under time translation, $G = u_0$) gives Bernoulli; axisymmetry (invariance under rotation) gives conservation of angular momentum per baryon along the flow. This is the unifying frame: Bernoulli is not a special trick of fluid mechanics but the fluid instance of the universal symmetry–conservation correspondence, with $\pi$ as the momentum and the fluid lines as the trajectories.

The reduction to the classical statement is the dictionary that names the conserved scalar. Expanding $h\Gamma$ for slow motion, $\Gamma \simeq 1 + \tfrac12 V^2$ and $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$, the conserved $h\Gamma$ becomes (up to the rest-energy constant $m_{\mathrm b}c^2$) the classical Bernoulli constant $H + \tfrac12 V^2$. The relativistic $h\Gamma$ is the parent; the classical "enthalpy plus kinetic energy" is its slow-motion pronunciation.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a stationary flow of a simple perfect fluid". The disguises:

The first disguised source is **"a steady-state astrophysical flow"**. Accretion onto a compact object, a stellar wind, or a jet in steady state are all stationary flows in the rest frame of the central object, so Bernoulli applies and the scalar $h\Gamma$ is conserved along each streamline. The bridge is that "steady state in some frame" is "stationary with respect to that inertial observer". *Example problem:* relate the terminal Lorentz factor of a relativistic jet to the enthalpy at its base.

The second disguised source is **"any continuous symmetry of the flow"**, not only stationarity. Axisymmetric flows (rotating stars, accretion disks), helically symmetric flows, and others each furnish a symmetry generator $G$ and hence a conserved $\langle\pi, G\rangle$. The bridge is the Noether form $\nabla_u\langle\pi, G\rangle = 0$. *Example problem:* find the conserved angular momentum per baryon in an axisymmetric accretion flow.

The third disguised source is **"a flow with a Killing vector"**. In the general-relativistic generalisation, a spacetime symmetry is a Killing vector $\xi$, and if the flow respects it then $\langle\pi, \xi\rangle$ is conserved along the fluid lines. The bridge is that a Killing vector is a symmetry generator. *Example problem:* conserved energy per baryon of fluid orbiting a stationary black hole (using the timelike Killing vector).

**Targets (Output Amplification)**

The conclusion is "$\langle\pi, u_0\rangle = h\Gamma$ is constant along each fluid line".

Combine the conclusion with **the equation of state**. Since $h = (\rho+p)/n$ is fixed by the thermodynamics, conservation of $h\Gamma$ relates the Lorentz factor $\Gamma$ (the speed) directly to the local thermodynamic state along a streamline. The further result is the pressure–velocity relationship: where the flow accelerates ($\Gamma$ rises), the enthalpy $h$ must fall, so the pressure drops. The combination is useful because it converts a kinematic statement into a thermodynamic prediction. *Example:* the Venturi/nozzle relation, faster flow $\Rightarrow$ lower pressure.

Combine the conclusion with **the nonrelativistic limit**. Expanding $h\Gamma$ gives the classical constant $H + \tfrac12 V^2$. The combination is what names the conserved scalar as "energy per unit mass" and connects to the entire body of classical Bernoulli applications. *Example:* lift on an aerofoil, drainage from a tank (Torricelli).

Combine the conclusion with **irrotationality**. For an irrotational *and* stationary flow, the canonical equation forces $\langle\pi, u_0\rangle$ to be not merely constant along each line but *uniform across all fluid lines* (see [[Ex - Irrotational flow and the velocity potential]]). The combination is nonobvious because Bernoulli alone gives a constant per streamline that may differ between streamlines, while irrotationality upgrades it to a single global constant. *Example:* potential flow past a body, where one Bernoulli constant governs the whole field.

---

# Why Is It True

The reason is that $\langle\pi, u_0\rangle$ is the Noether charge of the time-translation symmetry, and a Noether charge is conserved along the flow precisely because the symmetry says "nothing depends on $t$".

**The mechanism in one sentence: contracting the canonical equation $\Omega(u,\cdot) = T\,dS$ with the symmetry generator $u_0$ turns the left side into the derivative-along-the-flow of $\langle\pi, u_0\rangle$ (by stationarity) and the right side into the derivative-along-the-flow of the entropy per baryon (which vanishes), leaving $\langle\pi, u_0\rangle$ constant.**

Take it in steps. The vorticity two-form is $\Omega = d\pi$, so $\Omega(\cdot, u_0)$, written in the coordinates of $\mathcal{O}$ where $u_0 = (1,0,0,0)$, has components $[\Omega(\cdot, u_0)]_\alpha = \partial_\alpha(\pi_\mu u_0^\mu) - \partial_0\pi_\alpha$. Stationarity means every $\pi_\alpha$ is independent of $t = x^0$, so the second term $\partial_0\pi_\alpha$ vanishes, leaving $\Omega(\cdot, u_0) = \nabla\langle\pi, u_0\rangle = d\langle\pi, u_0\rangle$ — the vorticity, fed the stationary direction, is the gradient of the conserved scalar. Now feed in the four-velocity: $\Omega(u, u_0) = \nabla_u\langle\pi, u_0\rangle$. But the canonical equation says $\Omega(u, \cdot) = T\,dS$, so $\Omega(u, u_0) = T\langle dS, u_0\rangle = T\nabla_{u_0}S$. And stationarity again kills this: $\nabla_{u_0}S = (1/c)\partial_t S = 0$ because $S$ does not depend on $t$. Therefore $\nabla_u\langle\pi, u_0\rangle = 0$.

Why does the scalar come out as $h\Gamma$? Because $\langle\pi, u_0\rangle = h\langle u, u_0\rangle = h(u\cdot u_0) = h\Gamma$ by the definitions of the momentum one-form and the Lorentz factor. Physically, $\langle\pi, u_0\rangle$ is the time-component of the momentum-per-baryon in $\mathcal{O}$'s frame — the energy per baryon — and it is conserved for the same reason a particle's energy is conserved in a time-independent situation.

The Noether generalisation is immediate: replace $u_0$ by any symmetry generator $G$. If the flow is invariant under $G$, then the same two cancellations (the $\partial_G\pi$ term and the $\nabla_G S$ term both vanish by the symmetry) give $\nabla_u\langle\pi, G\rangle = 0$. This is exactly the structure of Noether's theorem for a relativistic particle (see [[Thm - Noether Theorem (Relativistic Particle)]]), with the fluid momentum one-form $\pi = hu$ in the role of the particle's four-momentum $mcu$ and the fluid lines in the role of the particle worldline.

---

# What Makes This Hard

The conceptual leap is recognising Bernoulli as a Noether theorem rather than an algebraic accident of the steady Euler equation — once $\pi = hu$ is seen as the fluid's momentum, the conservation of $\langle\pi, u_0\rangle$ in a time-independent situation is as natural as energy conservation for a particle. The non-obvious technical step is that stationarity is used *twice*: once to drop $\partial_0\pi_\alpha$ (making $\Omega(\cdot, u_0)$ a pure gradient), and once to drop $\nabla_{u_0}S$ (killing the thermodynamic source). The most common error is to forget that the conserved scalar is $h\Gamma$ with the *enthalpy* $h$, not $\Gamma$ alone or $u\cdot u_0$ alone — the enthalpy weighting from $\pi = hu$ is essential and is what reduces to "enthalpy plus kinetic energy" classically.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Contract the canonical equation $\Omega(u,\cdot) = T\,dS$ with the symmetry direction $u_0$. Use stationarity to turn $\Omega(\cdot, u_0)$ into the gradient of $\langle\pi, u_0\rangle$ and to kill $\nabla_{u_0}S$. What remains is $\nabla_u\langle\pi, u_0\rangle = 0$. Identify the conserved scalar as $h\Gamma$ and expand for the nonrelativistic limit.

**Subgoal decomposition:**

1. **Compute $\Omega(\cdot, u_0)$ in $\mathcal{O}$'s coordinates.** Show $[\Omega(\cdot, u_0)]_\alpha = \partial_\alpha\langle\pi, u_0\rangle - \partial_0\pi_\alpha$.
   - *Hint:* $\Omega = d\pi$, so $\Omega_{\alpha\beta} = \partial_\alpha\pi_\beta - \partial_\beta\pi_\alpha$; contract with $u_0^\beta = \delta^\beta_0$.
   - *Why needed:* Exposes where stationarity enters.

2. **Apply stationarity to drop $\partial_0\pi_\alpha$.** Conclude $\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle$.
   - *Hint:* Stationary means $\partial_t\pi_\alpha = 0$.
   - *Why needed:* Makes the contracted vorticity a pure gradient.

3. **Feed in $u$ and use the canonical equation.** Get $\nabla_u\langle\pi, u_0\rangle = \Omega(u, u_0) = T\nabla_{u_0}S$.
   - *Hint:* $\Omega(u,\cdot) = T\,dS$, then contract with $u_0$.
   - *Why needed:* Connects the conserved scalar to the thermodynamic source.

4. **Kill the source by stationarity.** $\nabla_{u_0}S = (1/c)\partial_t S = 0$, so $\nabla_u\langle\pi, u_0\rangle = 0$.
   - *Hint:* $S$ independent of $t$.
   - *Why needed:* Completes the conservation.

5. **Identify and reduce.** $\langle\pi, u_0\rangle = h\Gamma$; expand $h\Gamma \simeq m_{\mathrm b}c^2(1 + (H + \tfrac12 V^2)/c^2)$ for the classical constant.
   - *Hint:* $\Gamma \simeq 1 + \tfrac12 V^2$, $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$.
   - *Why needed:* Names the conserved scalar and recovers classical Bernoulli.

---

# Lemma Decomposition

> [!note]- Lemma 1: The contracted vorticity is a gradient in a stationary flow
> **Statement:** In a flow stationary with respect to $\mathcal{O}$ (coordinates with $u_0 = (1,0,0,0)$), $\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle$.
>
> **Hint:** Expand $\Omega = d\pi$ in components and contract with $u_0^\beta = \delta^\beta_0$; the $\partial_0$ term vanishes by stationarity.
>
> **Why needed:** It turns the left side of the canonical equation into the gradient of the candidate conserved scalar.
>
> > [!note]- Full proof
> > Since $\Omega = d\pi$, the components are $\Omega_{\alpha\beta} = \partial_\alpha\pi_\beta - \partial_\beta\pi_\alpha$. Contract with $u_0^\beta = \delta^\beta_0$:
> > $$[\Omega(\cdot, u_0)]_\alpha = \Omega_{\alpha\beta}u_0^\beta = \partial_\alpha(\pi_\beta u_0^\beta) - \pi_\beta\partial_\alpha u_0^\beta - \partial_0\pi_\alpha.$$
> > Since $u_0$ is a constant vector field (the four-velocity of an inertial observer), $\partial_\alpha u_0^\beta = 0$, so the middle term drops, giving $[\Omega(\cdot, u_0)]_\alpha = \partial_\alpha\langle\pi, u_0\rangle - \partial_0\pi_\alpha$. In a stationary flow all components $\pi_\alpha$ are independent of $t = x^0$, so $\partial_0\pi_\alpha = 0$, leaving
> > $$\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle. \qquad \blacksquare$$

> [!note]- Lemma 2: The thermodynamic source vanishes for a stationary flow
> **Statement:** In a stationary flow, $\langle dS, u_0\rangle = \nabla_{u_0}S = 0$.
>
> **Hint:** The entropy per baryon measured by $\mathcal{O}$ is independent of $\mathcal{O}$'s time.
>
> **Why needed:** It kills the right-hand side $T\langle dS, u_0\rangle$ of the contracted canonical equation.
>
> > [!note]- Full proof
> > $\langle dS, u_0\rangle = u_0^\mu\partial_\mu S = \partial_0 S = (1/c)\partial_t S$ in $\mathcal{O}$'s coordinates. Stationarity means every fluid quantity measured by $\mathcal{O}$, including the entropy per baryon $S$, is independent of $t$, so $\partial_t S = 0$ and $\nabla_{u_0}S = 0$. $\blacksquare$

> [!note]- Lemma 3: The conserved scalar is $h\Gamma$
> **Statement:** $\langle\pi, u_0\rangle = h\,(u\cdot u_0) = h\Gamma$.
>
> **Hint:** $\pi = hu$; $\Gamma = u\cdot u_0$.
>
> **Why needed:** It identifies the conserved quantity physically as the energy per baryon and connects to the classical Bernoulli constant.
>
> > [!note]- Full proof
> > By definition $\pi = hu$, so $\langle\pi, u_0\rangle = h\langle u, u_0\rangle = h(u\cdot u_0)$. The fluid Lorentz factor relative to $\mathcal{O}$ is $\Gamma = u\cdot u_0$ (in mostly-minus). Hence $\langle\pi, u_0\rangle = h\Gamma$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — setup.** The fluid is a simple perfect fluid obeying the canonical equation $\Omega(u,\cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]), with $\Omega = d\pi$, $\pi = hu$. The flow is stationary with respect to an inertial observer $\mathcal{O}$ of four-velocity $u_0$.
>
> By Lemma 1, stationarity gives $\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle$. Feed the four-velocity into the first slot: $\Omega(u, u_0) = \nabla_u\langle\pi, u_0\rangle$.
>
> By the canonical equation, $\Omega(u, u_0) = T\langle dS, u_0\rangle$. By Lemma 2, stationarity gives $\langle dS, u_0\rangle = 0$. Hence
> $$\nabla_u\langle\pi, u_0\rangle = 0,$$
> the scalar $\langle\pi, u_0\rangle$ is constant along each fluid line. By Lemma 3, this scalar is $\langle\pi, u_0\rangle = h\Gamma$.
>
> **General (Noether) form.** Replace $u_0$ by any symmetry generator $G$ of the flow. The same two steps — Lemma 1 with $G$ (the $\partial_G\pi$ term vanishes by the symmetry) and Lemma 2 with $G$ (the $\nabla_G S$ term vanishes by the symmetry) — give $\nabla_u\langle\pi, G\rangle = 0$.
>
> **Nonrelativistic limit.** Write $\Gamma \simeq 1 + \tfrac12 V^2$ and $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$ with $H$ the specific internal enthalpy. Then
> $$h\Gamma \simeq m_{\mathrm b}c^2\Big(1 + \frac{H}{c^2}\Big)\Big(1 + \frac{V^2}{2c^2}\Big) \simeq m_{\mathrm b}c^2 + m_{\mathrm b}\Big(H + \frac{V^2}{2}\Big),$$
> to leading order. The constant rest-energy term $m_{\mathrm b}c^2$ aside, conservation of $h\Gamma$ along the flow is conservation of $H + \tfrac12 V^2$ along each streamline — the classical Bernoulli theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Relativistic jet acceleration (astrophysics).** A steady relativistic jet conserves $h\Gamma$ along each streamline, so as the jet's enthalpy $h$ is converted to bulk kinetic energy, $\Gamma$ rises: the terminal Lorentz factor is set by the enthalpy at the jet base. The application is nonobvious because it predicts the jet speed from thermodynamics alone, and it explains why hotter or more magnetized launching regions produce faster jets.

**Flow near a black hole (general relativity).** With the timelike Killing vector $\xi$ of a stationary black-hole spacetime, the Noether form gives $\langle\pi, \xi\rangle$ conserved along the fluid lines — the relativistic Bernoulli constant for accretion. The application is out-of-distribution because the "symmetry" is a spacetime Killing vector rather than a flow stationarity, yet the structure is identical, and it governs the energetics of accretion onto compact objects.

**The de Laval nozzle and transonic flow (aerospace engineering).** Classical Bernoulli, with the area–velocity relation, explains why a converging–diverging nozzle accelerates a flow through the sound speed. The relativistic version applies to the launching of relativistic outflows. The application is surprising because the same conserved scalar controls both a jet engine and an astrophysical jet, the difference being only the magnitude of $\Gamma$.

---

# Bridges

- **[[Def - Vorticity 2-Form]]** — Bernoulli is the canonical equation $\Omega(u,\cdot) = T\,dS$ contracted with the time-translation symmetry $u_0$. The fluid momentum one-form $\pi = hu$ is the object whose contraction $\langle\pi, u_0\rangle$ is the conserved scalar; without the enthalpy weighting in $\pi$ the conserved quantity would not be the energy per baryon and would not reduce to the classical Bernoulli constant.

- **[[Thm - Noether Theorem (Relativistic Particle)]]** — Bernoulli is the fluid analogue of Noether's theorem for a particle. For a particle, a symmetry $G$ gives the conserved $\langle mcu, G\rangle$; for the fluid, the same symmetry gives $\langle\pi, G\rangle = \langle hu, G\rangle$ conserved along the fluid lines, with the momentum one-form $\pi = hu$ replacing the particle four-momentum $mcu$. The fluid lines are the analogue of the particle worldline.

- **The classical Bernoulli theorem** — the nonrelativistic shadow, $H + \tfrac12 V^2$ constant along streamlines. The relativistic $h\Gamma$ is the parent; expanding for slow motion recovers the classical constant, with the specific enthalpy $H$ coming from $h$ and the kinetic energy $\tfrac12 V^2$ from $\Gamma$. This is the dictionary that names the relativistic scalar as energy per unit mass.

- **[[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)]]** — the companion conservation law from the same canonical equation. Bernoulli is the conservation of a scalar along a fluid line (a symmetry statement); Kelvin is the conservation of a circulation around a loop (a flux statement). Both descend from $\Omega(u,\cdot) = T\,dS$, and both require the barotropic or isentropic condition for the cleanest form.

---

# Unlocked by This

> [!tip] Relativistic Jet and Wind Energetics *(from Astrophysics)*
> Bernoulli's conserved $h\Gamma$ governs the acceleration of **relativistic jets** and **stellar winds**: enthalpy at the source converts to bulk Lorentz factor downstream, so the terminal $\Gamma$ is fixed by the launching thermodynamics. This is a basic diagnostic for active galactic nuclei and gamma-ray-burst outflows, where observed Lorentz factors of hundreds are traced back to the enthalpy and magnetization at the central engine.

> [!tip] Conserved Energy of Accreting Matter *(from General Relativity)*
> In a stationary black-hole spacetime the Noether form gives a conserved energy per baryon $\langle\pi, \xi\rangle$ for fluid following the timelike **Killing vector** $\xi$. This is the relativistic Bernoulli constant of accretion, controlling how much gravitational energy is liberated as matter spirals in — the engine of quasar luminosity. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
