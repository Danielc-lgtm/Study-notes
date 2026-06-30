---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Perfect Fluid"
  - "Thm - Energy-Momentum Conservation"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Baryon Four-Current and Its Conservation"
  - "Def - Equation of State and Speed of Sound"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, $u\cdot u = 1$. The fluid is a [[Def - Perfect Fluid|perfect fluid]] $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$, four-acceleration $a^\mu = u^\nu\nabla_\nu u^\mu$ (see [[Def - Four-Velocity and Four-Acceleration]]). The proper entropy density is $s$, the proper baryon density $n$, the entropy per baryon $S = s/n$, the temperature $T$ (do not confuse the scalar temperature $T$ with the tensor $T^{\mu\nu}$ — context disambiguates), and chemical potentials $\mu_a$; thermodynamics as on [[Def - Equation of State and Speed of Sound]]. An external four-force density $f^\mu$ may act. Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

---

# Statement

> **Projection of energy–momentum conservation for a perfect fluid.** Let a [[Def - Perfect Fluid|perfect fluid]] obey $\nabla_\mu T^{\mu\nu} = f^\nu$. Then this single four-vector law splits into two complementary pieces.
>
> **(Energy equation — projection along $u$.)** Contracting with $u_\nu$,
> $$u^\mu\nabla_\mu\rho + (\rho+p)\,\nabla_\mu u^\mu \;=\; -\,f\cdot u.$$
> For an isolated ($f = 0$) **simple fluid**, this is equivalent, via the thermodynamic relations and baryon conservation $\nabla_\mu(nu^\mu) = 0$, to the conservation of entropy, $\nabla_\mu(s u^\mu) = 0$, and hence to
> $$\nabla_u\!\left(\frac{s}{n}\right) = 0,$$
> the constancy of the entropy per baryon along each fluid line: the flow is **adiabatic**.
>
> **(Euler equation — projection orthogonal to $u$.)** Applying the projector $\perp^{\mu\nu} = \eta^{\mu\nu} - u^\mu u^\nu$,
> $$(\rho+p)\,a^\mu \;=\; -\,\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu,$$
> the four-dimensional [[Thm - Relativistic Euler Equation|relativistic Euler equation]].

The two projections together are equivalent to the full conservation law $\nabla_\mu T^{\mu\nu} = f^\nu$.

---

# Motivation

A fluid dynamicist confronting the relativistic conservation law $\nabla_\mu T^{\mu\nu} = 0$ wants two things from it: an *energy equation*, telling how the energy density evolves, and an *equation of motion*, telling how the velocity field evolves. Nonrelativistically these are separate statements — the energy equation and the Euler equation — and one might expect to need two separate postulates. This theorem says they are not separate: they are the two complementary projections of the *single* conservation law, and projecting along versus across the flow is exactly what separates energy balance from momentum balance.

The reason a four-velocity field makes this split possible is that it equips spacetime, at each event, with a preferred timelike direction. Any four-vector equation can be decomposed into its component along that direction (one scalar equation) and its components orthogonal to it (three equations). For the conservation law, the along-$u$ component is the rate of change of energy — the energy equation — and the orthogonal components are the rate of change of momentum — the Euler equation. This theorem is the statement that the decomposition works cleanly and that the two pieces have exactly the expected fluid-dynamical meanings.

The energy half carries a beautiful payload for a closed fluid. The bare energy equation $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$ looks like a statement about energy, but feeding in the thermodynamic relations and baryon-number conservation transforms it into the statement that *entropy is conserved along the flow*: $\nabla_u(s/n) = 0$. The flow is adiabatic — no heat diffuses between fluid elements — and this is not an extra assumption but a *consequence* of perfect-fluid dynamics. Physically it is the first law $d(\rho V) = -p\,dV$ for a comoving volume $V$, which for a reversible (no dissipation) perfect fluid means $dS = 0$. This adiabaticity is the input that later collapses the canonical equation $\Omega(u,\cdot) = T\,dS$ and is what makes [[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)|Kelvin's theorem]] work.

The Euler half is the relativistic equation of motion, "$\mathbf{a} = \mathbf{F}/(\rho+p)$", treated in full on its own page ([[Thm - Relativistic Euler Equation]]). The point of *this* page is the unifying observation that energy and momentum balance are one law seen two ways, and that the entropy conservation is hidden inside the energy projection.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a perfect fluid with conserved (up to force) energy–momentum". The disguises:

The first disguised source is **"a thermodynamically closed fluid in local equilibrium"**. Whenever the matter is in local thermodynamic equilibrium with a well-defined entropy and an [[Def - Equation of State and Speed of Sound|equation of state]], the thermodynamic relations $d\rho = T\,ds + \sum\mu_a\,dn_a$ hold, and the energy projection can be converted to entropy conservation. The bridge is the substitution of the first law into the energy equation. *Example problem:* show that an ideal-gas fluid flows adiabatically in the absence of dissipation.

The second disguised source is **"a fluid with conserved particle currents"**. Baryon-number conservation $\nabla_\mu(nu^\mu) = 0$ (see [[Def - Baryon Four-Current and Its Conservation]]) is exactly what is needed to convert "entropy density current conserved" into "entropy *per baryon* conserved along the flow". The bridge is dividing the two conserved currents. *Example problem:* show that a chemically frozen fluid (fixed particle-to-baryon ratios) is isentropic along its flow lines.

The third disguised source is **"a homogeneous cosmological fluid"**. In a homogeneous universe the fluid is at rest in comoving coordinates, the spatial gradients vanish, and $\nabla_\mu u^\mu = 3\dot a/a$ is the Hubble expansion. The energy projection becomes the cosmological continuity equation directly. The bridge is the identification of $\nabla_\mu u^\mu$ with the expansion rate. *Example problem:* derive $\dot\rho + 3(\dot a/a)(\rho+p) = 0$.

**Targets (Output Amplification)**

The conclusions are the energy equation and the Euler equation.

Combine the energy equation with **the identity $\nabla_\mu u^\mu = \dot V/V$** for a comoving volume. The further result is the first law $d(\rho V) = -p\,dV$: the energy of a comoving element changes only by the work done by pressure. The combination is useful because it makes the energy equation manifestly the first law of thermodynamics carried along the worldline. *Example:* interpret cosmological energy loss as $pdV$ work done by the expanding universe.

Combine the energy and Euler equations with **a linearised adiabatic perturbation**. Together they give the wave equation for sound, with speed $c_s^2 = (\partial p/\partial\rho)_S$ (see [[Def - Equation of State and Speed of Sound]]). The combination is nonobvious because it takes *both* projections — the energy equation supplies one half of the wave operator, the Euler equation the other. *Example:* derive the sound speed of a relativistic gas; see [[Ex - The speed of sound from linearised perturbations]].

Combine the Euler equation with **the enthalpy one-form $\pi = hu$**. Lowering, multiplying by $h = (\rho+p)/n$, and applying the exterior derivative recasts the Euler equation as the canonical equation $\Omega(u,\cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]). The combination is useful because the form-version generates the conservation laws (Bernoulli, Kelvin) that the projection-version does not make transparent. *Example:* derive Bernoulli's theorem.

---

# Why Is It True

The split works because a unit timelike four-velocity field is a complete tool for decomposing four-vectors: any four-vector $W^\mu$ is uniquely $W^\mu = (W\cdot u)u^\mu + \perp^{\mu\nu}W_\nu$, a piece along $u$ and a piece across it. Apply this to the four-vector $\nabla_\mu T^{\mu\nu} - f^\nu$, which is zero; both its along-$u$ and across-$u$ parts must separately vanish, giving the two equations.

**The mechanism in one sentence: the along-$u$ projection of $\nabla_\mu T^{\mu\nu} = 0$ is the rate of change of energy in a comoving frame (the first law), and the across-$u$ projection is the rate of change of momentum (Newton's law), because projecting along versus across the flow is exactly the split between energy and momentum balance.**

For the energy half, contract the expanded divergence (Lemma 1 of [[Thm - Relativistic Euler Equation]]) with $u_\nu$. The acceleration term dies because $u\cdot a = 0$, and what remains is $u^\mu\nabla_\mu(\rho+p) + (\rho+p)\nabla_\mu u^\mu - u^\nu\nabla_\nu p = u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu$ (the $\nabla p$ pieces partially cancel). Now read this through the identity $\nabla_\mu u^\mu = \dot V/V$ for a comoving volume: it says $\dot\rho + (\rho+p)\dot V/V = 0$, i.e. $d(\rho V)/d\tau = -p\,\dot V$, which is $dU = -p\,dV$ — the first law of thermodynamics for an adiabatic (reversible) process. So the energy equation *is* the first law, and for a perfect (dissipationless) fluid the first law with no heat input is $T\,dS = 0$, i.e. entropy is conserved. To see the entropy explicitly, write $\rho$'s change using the first law $d\rho = T\,ds + \mu\,dn$ (simple fluid), and use baryon conservation $\nabla_\mu(nu^\mu) = 0$ to eliminate $dn$; the temperature factors out and what survives is $T\nabla_\mu(su^\mu) = 0$, hence $\nabla_\mu(su^\mu) = 0$. Dividing by the conserved $n$ gives $\nabla_u(s/n) = 0$.

For the momentum half, the across-$u$ projection isolates the transverse pressure gradient as the only force, with inertia $\rho + p$ — this is the content of [[Thm - Relativistic Euler Equation]], and the intuition is given there. The key point uniting the two halves is that the *same* law, $\nabla_\mu T^{\mu\nu} = 0$, supplies both: there is one conservation principle, and energy and momentum balance are its shadow along and across the flow.

---

# What Makes This Hard

The surprise that trips people is that *two* fluid equations come from *one* conservation law — most expect energy balance and momentum balance to be independent inputs, and the projection structure that unifies them is not obvious in advance. The non-obvious step in the energy half is recognising that the bare energy equation hides entropy conservation: it takes the substitution of the thermodynamic first law *and* baryon-number conservation to reveal $\nabla_u(s/n) = 0$, and forgetting either ingredient leaves the result invisible. The most common error is to mishandle the $\nabla p$ terms in the along-$u$ projection (the pressure gradient contributes to *both* projections, and its longitudinal part must be tracked carefully).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Expand $\nabla_\mu T^{\mu\nu}$ for the perfect fluid, then take the two projections. For the energy equation, contract with $u_\nu$ and use $u\cdot a = 0$. To extract entropy conservation, substitute the thermodynamic first law and baryon conservation, watching the temperature factor out. For the Euler equation, apply the orthogonal projector (full details on the [[Thm - Relativistic Euler Equation]] page).

**Subgoal decomposition:**

1. **Expand the divergence.** Show $\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p$.
   - *Hint:* Product rule; $u^\mu\nabla_\mu u^\nu = a^\nu$.
   - *Why needed:* Common starting point for both projections.

2. **Project along $u$.** Contract with $u_\nu$, use $u\cdot u = 1$ and $u\cdot a = 0$, to get $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = -f\cdot u$.
   - *Hint:* $u_\nu u^\nu = 1$ makes $\nabla_\mu[(\rho+p)u^\mu]$ survive; $u_\nu a^\nu = 0$ kills the acceleration; $u_\nu\nabla^\nu p$ from the pressure term combines with $\nabla_\mu(\rho+p)\cdot$ the $u$-derivative.
   - *Why needed:* The energy equation.

3. **Convert to entropy conservation (isolated simple fluid).** Substitute $d\rho = T\,ds + \mu\,dn$ and use $\nabla_\mu(nu^\mu) = 0$ to reduce the energy equation to $T\nabla_\mu(su^\mu) = 0$.
   - *Hint:* $u^\mu\nabla_\mu\rho = T u^\mu\nabla_\mu s + \mu u^\mu\nabla_\mu n$; rewrite using $\nabla_\mu(su^\mu) = u^\mu\nabla_\mu s + s\nabla_\mu u^\mu$ and the Euler relation $\rho + p = Ts + \mu n$.
   - *Why needed:* Reveals adiabaticity, $\nabla_u(s/n) = 0$.

4. **Project orthogonal to $u$.** Apply $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ to get $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu$.
   - *Hint:* See [[Thm - Relativistic Euler Equation]] Lemma 3.
   - *Why needed:* The Euler equation, the momentum half.

---

# Lemma Decomposition

> [!note]- Lemma 1: The energy projection
> **Statement:** Contracting $\nabla_\mu T^{\mu\nu} = f^\nu$ with $u_\nu$ gives $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = -f\cdot u$.
>
> **Hint:** Use $u\cdot u = 1$, $u\cdot a = 0$; combine the $u$-derivative of $(\rho+p)$ with the longitudinal pressure-gradient term.
>
> **Why needed:** It is the energy equation, the along-flow half of the split.
>
> > [!note]- Full proof
> > From the expanded divergence $\nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p = f^\nu$, contract with $u_\nu$. Since $u_\nu u^\nu = 1$, the first term gives $\nabla_\mu[(\rho+p)u^\mu] = u^\mu\nabla_\mu(\rho+p) + (\rho+p)\nabla_\mu u^\mu$. Since $u_\nu a^\nu = 0$ (the four-acceleration is orthogonal to $u$), the second term vanishes. The third gives $-u_\nu\nabla^\nu p = -u^\mu\nabla_\mu p$. Assembling,
> > $$u^\mu\nabla_\mu(\rho+p) + (\rho+p)\nabla_\mu u^\mu - u^\mu\nabla_\mu p = -f\cdot u,$$
> > and the $u^\mu\nabla_\mu p$ terms cancel ($u^\mu\nabla_\mu(\rho+p) - u^\mu\nabla_\mu p = u^\mu\nabla_\mu\rho$), leaving
> > $$u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = -f\cdot u. \qquad \blacksquare$$

> [!note]- Lemma 2: Energy equation is entropy conservation (isolated simple fluid)
> **Statement:** For $f = 0$ and a simple fluid, the energy equation is equivalent to $\nabla_\mu(su^\mu) = 0$, hence $\nabla_u(s/n) = 0$.
>
> **Hint:** Substitute the first law $u^\mu\nabla_\mu\rho = Tu^\mu\nabla_\mu s + \mu u^\mu\nabla_\mu n$ and the Euler relation $\rho + p = Ts + \mu n$; use $\nabla_\mu(nu^\mu) = 0$.
>
> **Why needed:** It is the payload of the energy projection — the flow is adiabatic.
>
> > [!note]- Full proof
> > For a simple fluid $\rho = \rho(s, n)$, the first law gives $u^\mu\nabla_\mu\rho = T\,u^\mu\nabla_\mu s + \mu\,u^\mu\nabla_\mu n$. The Euler relation gives $\rho + p = Ts + \mu n$. Substitute both into the energy equation $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$:
> > $$T u^\mu\nabla_\mu s + \mu u^\mu\nabla_\mu n + (Ts + \mu n)\nabla_\mu u^\mu = 0.$$
> > Group the $T$ and $\mu$ terms:
> > $$T\big[u^\mu\nabla_\mu s + s\nabla_\mu u^\mu\big] + \mu\big[u^\mu\nabla_\mu n + n\nabla_\mu u^\mu\big] = 0,$$
> > i.e. $T\,\nabla_\mu(su^\mu) + \mu\,\nabla_\mu(nu^\mu) = 0$. By baryon conservation $\nabla_\mu(nu^\mu) = 0$, the second term vanishes, leaving $T\,\nabla_\mu(su^\mu) = 0$, hence $\nabla_\mu(su^\mu) = 0$ (with $T \ne 0$). Finally
> > $$\nabla_u\!\Big(\frac{s}{n}\Big) = \frac{1}{n}\Big[\nabla_\mu(su^\mu) - \frac{s}{n}\nabla_\mu(nu^\mu)\Big] = 0,$$
> > using both conservation laws. $\blacksquare$

> [!note]- Lemma 3: The momentum projection
> **Statement:** Applying $\perp^\mu{}_\nu = \delta^\mu_\nu - u^\mu u_\nu$ to $\nabla_\alpha T^{\alpha\nu} = f^\nu$ gives $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu$.
>
> **Hint:** The longitudinal term is killed by the projector; $\perp a = a$ by $u\cdot a = 0$.
>
> **Why needed:** It is the Euler equation, the across-flow half; proved in full on [[Thm - Relativistic Euler Equation]].
>
> > [!note]- Full proof
> > This is Lemma 3 of [[Thm - Relativistic Euler Equation]]. Contracting the expanded divergence with $\perp^\mu{}_\nu$: the longitudinal term $\nabla_\alpha[(\rho+p)u^\alpha]u^\nu$ dies since $\perp^\mu{}_\nu u^\nu = 0$; the acceleration term gives $(\rho+p)a^\mu$ since $u\cdot a = 0$; the pressure term gives $-\perp^{\mu\nu}\nabla_\nu p$; the force gives $\perp^{\mu\nu}f_\nu$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — setup.** The fluid is a [[Def - Perfect Fluid|perfect fluid]] obeying $\nabla_\mu T^{\mu\nu} = f^\nu$. By Lemma 1 of [[Thm - Relativistic Euler Equation]], $\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p$.
>
> **Energy equation.** By Lemma 1 above, contracting with $u_\nu$ yields
> $$u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = -f\cdot u.$$
> For an isolated ($f=0$) simple fluid, Lemma 2 converts this — using the first law and baryon conservation $\nabla_\mu(nu^\mu) = 0$ — into $\nabla_\mu(su^\mu) = 0$ and hence $\nabla_u(s/n) = 0$: the entropy per baryon is constant along each fluid line, and the flow is adiabatic.
>
> **Euler equation.** By Lemma 3, projecting orthogonal to $u$ yields
> $$(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p + \perp^{\mu\nu}f_\nu,$$
> the four-dimensional relativistic Euler equation.
>
> **Completeness.** The two projections decompose the four-vector equation $\nabla_\mu T^{\mu\nu} - f^\nu = 0$ into its component along $u$ (one scalar, the energy equation) and its components orthogonal to $u$ (three, the Euler equation), and any four-vector that vanishes has both projections vanishing. Hence the two equations together are equivalent to the full conservation law. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Cosmological continuity (cosmology).** For a homogeneous fluid at rest in comoving coordinates, the energy projection becomes $\dot\rho + 3(\dot a/a)(\rho+p) = 0$, the equation governing how energy density evolves with the scale factor. The application is nonobvious because the "expansion" $\nabla_\mu u^\mu = 3\dot a/a$ is purely geometric, yet the equation is just the first law $d(\rho V) = -p\,dV$ for the expanding comoving volume.

**Entropy production and the arrow of time (statistical mechanics).** The perfect-fluid result $\nabla_\mu(su^\mu) = 0$ is the *reversible* limit; adding viscosity or conduction makes $\nabla_\mu(su^\mu) \ge 0$, the local second law. The application is illuminating because it shows the perfect fluid sits exactly at the boundary of reversibility, and the entropy-production rate measures the departure.

**Bjorken flow in heavy-ion collisions (nuclear physics).** The boost-invariant longitudinal expansion of the quark–gluon plasma created in a collision is governed by the energy projection with a specific expansion profile, giving $d\rho/d\tau = -(\rho+p)/\tau$. The application is out-of-distribution because the "fluid" is a transient fireball, yet the same projection structure applies and predicts the cooling rate.

---

# Bridges

- **[[Thm - Relativistic Euler Equation]]** — the orthogonal half of this theorem. The Euler equation is the momentum projection; this page additionally extracts the energy projection and its adiabaticity payload, showing that the two equations a fluid dynamicist needs are the two shadows of one conservation law.

- **[[Def - Baryon Four-Current and Its Conservation]]** — the partner conservation law. Baryon conservation $\nabla_\mu(nu^\mu) = 0$ is exactly what is needed to convert the energy projection's "entropy density conserved" into "entropy *per baryon* conserved along the flow", giving adiabaticity $\nabla_u(s/n) = 0$.

- **The first law of thermodynamics** — the energy equation, read through $\nabla_\mu u^\mu = \dot V/V$, is $d(\rho V) = -p\,dV$, the first law for an adiabatic process. The perfect fluid is thus thermodynamics in motion: each fluid element is a small thermodynamic system whose first law is enforced by the conservation of energy–momentum.

- **[[Def - Vorticity 2-Form]]** — the Euler equation recast in the exterior derivative. The adiabaticity $\nabla_u S = 0$ established here is what allows the canonical equation $\Omega(u,\cdot) = T\,dS$ to be simplified and is essential to Bernoulli's and Kelvin's theorems.

---

# Unlocked by This

> [!tip] The Cosmological Continuity Equation *(from Cosmology)*
> In a homogeneous expanding universe the energy projection becomes $\dot\rho + 3\frac{\dot a}{a}(\rho+p) = 0$. With an equation of state $p = w\rho$ this gives the scaling of each component: matter ($w=0$) as $a^{-3}$, radiation ($w=1/3$) as $a^{-4}$, a cosmological constant ($w=-1$) constant. This single equation is the thermodynamic backbone of the **hot Big Bang**, and it is nothing but the first law $d(\rho V) = -p\,dV$ for the expanding volume.

> [!tip] The Second Law and Dissipative Fluids *(from Non-equilibrium Thermodynamics)*
> The perfect-fluid result $\nabla_\mu(su^\mu) = 0$ is the reversible boundary. Real fluids have $\nabla_\mu(su^\mu) \ge 0$ — the **local second law** — with the entropy-production rate fixed by the viscous and conductive fluxes. This is the starting point of **relativistic dissipative hydrodynamics** (Eckart, Landau–Lifshitz, Israel–Stewart), where the challenge is to add dissipation without violating causality.
