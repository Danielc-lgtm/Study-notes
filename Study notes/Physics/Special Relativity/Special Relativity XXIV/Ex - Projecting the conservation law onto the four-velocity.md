---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Energy-Momentum Conservation projected (Euler + energy equation)"
  - "Def - Perfect Fluid"
  - "Def - Baryon Four-Current and Its Conservation"
  - "Def - Equation of State and Speed of Sound"
tags: [physics, special-relativity]
---

# Problem Statement

Let a perfect fluid obey $\nabla_\mu T^{\mu\nu} = 0$ (isolated).

1. Contract the conservation law with $u_\nu$ and derive the **energy equation** $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$.
2. Using the identity $\nabla_\mu u^\mu = \frac{1}{V}\frac{dV}{d\tau}$ for a comoving volume $V$, show that the energy equation is the **first law of thermodynamics** $\frac{d(\rho V)}{d\tau} = -p\frac{dV}{d\tau}$ for an adiabatic process.
3. For a simple fluid, substitute the thermodynamic relations and baryon conservation $\nabla_\mu(nu^\mu) = 0$ to show the energy equation is equivalent to entropy conservation $\nabla_\mu(s u^\mu) = 0$, hence $\nabla_u(s/n) = 0$: the flow is adiabatic.

**Recall:**

![[Thm - Energy-Momentum Conservation projected (Euler + energy equation)#Statement]]

The proper energy density is $\rho$, pressure $p$, proper baryon density $n$, proper entropy density $s$, entropy per baryon $S = s/n$, temperature $T$, chemical potential per baryon $\mu$. The first law is $d\rho = T\,ds + \mu\,dn$ and the Euler relation $\rho + p = Ts + \mu n$ (see [[Def - Equation of State and Speed of Sound]]). Baryon conservation is $\nabla_\mu(nu^\mu) = 0$ (see [[Def - Baryon Four-Current and Its Conservation]]). The four-acceleration $a^\mu = u^\nu\nabla_\nu u^\mu$ is orthogonal to $u$.

---

# Convergent Strategy

**Problem class.** A *derive-an-equation-by-projection* problem, with a thermodynamic payoff. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], the parallel projection of the conservation law extracts the energy equation, and the thermodynamic relations convert it to entropy conservation.

**Assumption pattern.** Three ingredients are present: the perfect-fluid form of $T^{\mu\nu}$, the unit-norm identity $u\cdot a = 0$, and (for part 3) the thermodynamic relations plus baryon conservation. The signpost for the parallel projection is that you want the *energy* (a scalar), not the momentum (a vector); contracting with $u_\nu$ extracts the scalar.

**Theorem routing.** Part 1 is the parallel projection of [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)|the projection theorem]]. Part 2 routes through the volume-expansion identity $\nabla_\mu u^\mu = \dot V/V$ from [[Def - Baryon Four-Current and Its Conservation]]. Part 3 routes the energy equation through the first law $d\rho = T\,ds + \mu\,dn$ and the Euler relation $\rho + p = Ts + \mu n$, then uses $\nabla_\mu(nu^\mu) = 0$ to cancel the chemical-potential term.

**Key decision point.** The crux of part 3 is recognising that the chemical-potential term cancels by *baryon conservation*, leaving only $T\nabla_\mu(su^\mu) = 0$. Without invoking baryon conservation, the entropy result is invisible — the energy equation looks like a statement about energy, and only the combination with $\nabla_\mu(nu^\mu) = 0$ reveals it as a statement about entropy.

---

# Legal Operations Used

1. **Project the conservation law along the four-velocity** (operation 1 from the topic page): contracting with $u_\nu$ extracts the scalar energy equation.

2. **Use the unit-norm identity $u\cdot a = 0$** (operation 3): kills the four-acceleration term in the parallel projection.

3. **Compute thermodynamic derivatives from the equation of state** (operation 10): the first law $d\rho = T\,ds + \mu\,dn$ converts the energy density's evolution into entropy and number evolution.

4. **Invoke baryon-number conservation** (operation 6): $\nabla_\mu(nu^\mu) = 0$ cancels the chemical-potential term, leaving entropy conservation.

---

# Hints

> [!note]- Hint 1
> Use the expanded divergence $\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p$. Contract with $u_\nu$. The acceleration term dies ($u\cdot a = 0$), and the pressure-gradient pieces partially cancel.

> [!note]- Hint 2
> The energy equation $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$ is, along a fluid line (parametrised by proper time $\tau$, so $u^\mu\nabla_\mu = d/d\tau$), $\dot\rho + (\rho+p)\dot V/V = 0$. Multiply by $V$ and recognise $\dot\rho V + \rho\dot V = d(\rho V)/d\tau$.

> [!note]- Hint 3
> Substitute $\dot\rho = T\dot s + \mu\dot n$ (first law along the flow) and $\rho + p = Ts + \mu n$ (Euler relation). Collect the $T$ and $\mu$ terms: you get $T[\dot s + s\,\dot V/V] + \mu[\dot n + n\,\dot V/V] = 0$, i.e. $T\nabla_\mu(su^\mu) + \mu\nabla_\mu(nu^\mu) = 0$. Now use baryon conservation.

---

# Solution

The parallel projection of the conservation law is the energy equation, which is the first law of thermodynamics in disguise; feeding in the thermodynamic relations and baryon conservation reveals it as the conservation of entropy along the flow.

**Step 1: The energy equation.**

> [!note]- Derivation
> From the expanded divergence of the perfect-fluid tensor,
> $$\nabla_\mu T^{\mu\nu} = \nabla_\mu[(\rho+p)u^\mu]u^\nu + (\rho+p)a^\nu - \nabla^\nu p,$$
> contract with $u_\nu$. Since $u_\nu u^\nu = 1$, the first term gives $\nabla_\mu[(\rho+p)u^\mu] = u^\mu\nabla_\mu(\rho+p) + (\rho+p)\nabla_\mu u^\mu$. Since $u_\nu a^\nu = 0$ (the four-acceleration is orthogonal to the unit four-velocity), the second term vanishes. The third gives $-u^\mu\nabla_\mu p$. So
> $$u^\mu\nabla_\mu(\rho+p) + (\rho+p)\nabla_\mu u^\mu - u^\mu\nabla_\mu p = 0,$$
> and the $u^\mu\nabla_\mu p$ terms cancel, leaving
> $$u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0.$$

**Step 2: The energy equation is the first law $d(\rho V) = -p\,dV$.**

> [!note]- Derivation
> Along a fluid line, $u^\mu\nabla_\mu = d/d\tau$ (the proper-time derivative), and the volume-expansion identity (see [[Def - Baryon Four-Current and Its Conservation]]) gives $\nabla_\mu u^\mu = \dot V/V$. The energy equation becomes
> $$\dot\rho + (\rho+p)\frac{\dot V}{V} = 0.$$
> Multiply by $V$:
> $$\dot\rho V + \rho\dot V + p\dot V = 0 \implies \frac{d(\rho V)}{d\tau} = -p\frac{dV}{d\tau}.$$
> With $U = \rho V$ the energy of the comoving element, this is $dU = -p\,dV$ — the **first law of thermodynamics** for an adiabatic process (no heat input). The energy of a fluid element changes only by the work $-p\,dV$ done against its boundary.

**Step 3: Entropy conservation, hence adiabaticity.**

> [!note]- Derivation
> For a simple fluid $\rho = \rho(s, n)$, the first law gives $\dot\rho = T\dot s + \mu\dot n$ along the flow. Substitute into the energy equation $\dot\rho + (\rho+p)\dot V/V = 0$, and use the Euler relation $\rho + p = Ts + \mu n$:
> $$T\dot s + \mu\dot n + (Ts + \mu n)\frac{\dot V}{V} = 0.$$
> Group:
> $$T\Big[\dot s + s\frac{\dot V}{V}\Big] + \mu\Big[\dot n + n\frac{\dot V}{V}\Big] = 0,$$
> i.e. $T\,\nabla_\mu(su^\mu) + \mu\,\nabla_\mu(nu^\mu) = 0$ (each bracket is $\frac{1}{V}\frac{d(XV)}{d\tau} = \nabla_\mu(Xu^\mu)$). By [[Def - Baryon Four-Current and Its Conservation|baryon conservation]] $\nabla_\mu(nu^\mu) = 0$, the second term vanishes, leaving $T\nabla_\mu(su^\mu) = 0$, hence (since $T \ne 0$)
> $$\nabla_\mu(su^\mu) = 0.$$
> Finally, $\nabla_u(s/n) = \frac{1}{n}[\nabla_\mu(su^\mu) - (s/n)\nabla_\mu(nu^\mu)] = 0$: the entropy per baryon is constant along each fluid line. The flow is **adiabatic** — no heat diffuses between fluid elements.

> [!note]- Complete formal solution
> Contracting $\nabla_\mu T^{\mu\nu} = 0$ with $u_\nu$, using $u\cdot u = 1$ and $u\cdot a = 0$, gives the energy equation $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$. Along a fluid line with $\nabla_\mu u^\mu = \dot V/V$, this is $\dot\rho + (\rho+p)\dot V/V = 0$, i.e. $d(\rho V)/d\tau = -p\,\dot V$, the first law $dU = -p\,dV$. For a simple fluid, substituting $\dot\rho = T\dot s + \mu\dot n$ and $\rho + p = Ts + \mu n$ yields $T\nabla_\mu(su^\mu) + \mu\nabla_\mu(nu^\mu) = 0$; baryon conservation $\nabla_\mu(nu^\mu) = 0$ kills the second term, so $\nabla_\mu(su^\mu) = 0$ and $\nabla_u(s/n) = 0$. The flow conserves entropy per baryon and is adiabatic. $\blacksquare$

---

# Key Takeaways

**The energy equation is the first law carried along the worldline.** The single most illuminating identification in this exercise is that the parallel projection of $\nabla_\mu T^{\mu\nu} = 0$ — which looks like an abstract tensor statement — is exactly the first law of thermodynamics $dU = -p\,dV$ for a comoving fluid element. The bridge is the identity $\nabla_\mu u^\mu = \dot V/V$: the four-divergence of the velocity *is* the fractional rate of expansion of a comoving volume. Once this is seen, the energy equation is no longer mysterious — it says a fluid element's energy changes only by pressure work, which is the first law with no heat input. The transferable lesson is that whenever you project a conserved energy–momentum tensor along the flow, you are reading off the local first law; the relativistic packaging hides a thermodynamic statement every fluid dynamicist knows. This is also why an equation of state is needed to close the system: the energy equation is thermodynamics, and thermodynamics needs the equation of state.

**Entropy conservation is hidden, and baryon conservation reveals it.** The deeper payoff — that the flow is adiabatic, $\nabla_u(s/n) = 0$ — is not visible in the bare energy equation. It emerges only when you substitute the thermodynamic relations *and* invoke baryon conservation, at which point the chemical-potential term cancels and pure entropy conservation survives. The diagnostic to carry forward is that two conserved currents sharing the same flow lines (here entropy $su^\mu$ and baryon number $nu^\mu$) give a conserved *ratio* (here $s/n$), and that ratio's constancy along the flow is what "adiabatic" means. Whenever you have a fluid with a conserved particle number and want to know whether it flows isentropically, this is the route: project for the energy equation, substitute thermodynamics, cancel against number conservation. The cancellation is not an accident — it is the statement that a reversible (perfect, dissipationless) fluid produces no entropy.

**Adiabaticity is the input that makes the conservation laws work.** The result $\nabla_u(s/n) = 0$ established here is not an end in itself; it is the hypothesis that later powers [[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)|Kelvin's circulation theorem]] and simplifies the canonical equation $\Omega(u,\cdot) = T\,dS$. When $S = s/n$ is constant on a loop, it stays constant on the whole tube swept by the flow (because it is conserved along each line), which is exactly the condition under which circulation is conserved. So this exercise supplies a load-bearing fact for the rest of the chapter. The trigger to recall it: any time a problem invokes "isentropic" or "adiabatic" flow, the justification is this projection — perfect-fluid dynamics *forces* adiabaticity, it need not be assumed separately.
