---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Relativistic Bernoulli Theorem"
  - "Def - Vorticity 2-Form"
  - "Def - Equation of State and Speed of Sound"
tags: [physics, special-relativity]
---

# Problem Statement

1. For a simple perfect fluid in a flow stationary with respect to an inertial observer $\mathcal{O}$ (four-velocity $u_0$), use the canonical equation $\Omega(u,\cdot) = T\,dS$ to prove that $\langle\pi, u_0\rangle = h\Gamma$ is constant along each fluid line.
2. Take the nonrelativistic limit and recover the classical Bernoulli constant $H + \tfrac12 V^2$ (specific enthalpy plus kinetic energy per unit mass).
3. Apply the result to steady flow through a converging nozzle: relate the change in flow speed to the change in enthalpy, and explain why the fluid accelerates where the enthalpy (and pressure) drops.

**Recall:**

![[Thm - Relativistic Bernoulli Theorem#Statement]]

The fluid momentum one-form is $\pi = h\,u$ with $h = (\rho+p)/n$ the enthalpy per baryon; the vorticity two-form is $\Omega = d\pi$, obeying the canonical equation $\Omega(u,\cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]). The fluid Lorentz factor relative to $\mathcal{O}$ is $\Gamma = u\cdot u_0$. The specific internal enthalpy is $H = (\varepsilon_{\mathrm{int}} + p)/\rho_{\mathrm m}$ (see [[Def - Equation of State and Speed of Sound]]).

---

# Convergent Strategy

**Problem class.** An *exploit-a-symmetry* problem: a stationary flow has a time-translation symmetry, which by the Noether structure produces a conserved scalar along the flow. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], the canonical equation $\Omega(u,\cdot) = T\,dS$ is the tool, and Bernoulli is it contracted with the symmetry direction.

**Assumption pattern.** The key assumption is *stationarity* — fluid quantities measured by $\mathcal{O}$ are independent of $\mathcal{O}$'s time. This is used twice: to make $\Omega(\cdot, u_0)$ a pure gradient, and to kill the entropy source $\nabla_{u_0}S$. The signpost is "steady flow" or "stationary".

**Theorem routing.** This is a direct application of [[Thm - Relativistic Bernoulli Theorem|Bernoulli's theorem]]: contract $\Omega(u,\cdot) = T\,dS$ with $u_0$, use stationarity, get $\nabla_u\langle\pi, u_0\rangle = 0$. The conserved scalar is $\langle\pi, u_0\rangle = h\Gamma$ by the definition of $\pi$.

**Key decision point.** The crux is recognising that $\langle\pi, u_0\rangle$ — the projection of the fluid momentum-per-baryon onto the observer's time direction — is the right conserved quantity, and that it equals $h\Gamma$ with the *enthalpy* weighting. The natural error is to expect $\Gamma$ (the Lorentz factor) alone to be conserved; it is the product $h\Gamma$, and the enthalpy factor is what makes it reduce to "enthalpy plus kinetic energy" classically.

---

# Legal Operations Used

1. **Exploit a symmetry via the Noether-type scalar** (operation 7 from the topic page): stationarity is the time-translation symmetry, and $\langle\pi, u_0\rangle$ is its conserved charge along the flow.

2. **Form the fluid momentum one-form and take its exterior derivative** (operation 5): the canonical equation $\Omega(u,\cdot) = T\,dS$ is the starting point.

3. **Take the nonrelativistic limit** (operation 4): expands $h\Gamma$ to the classical Bernoulli constant.

---

# Hints

> [!note]- Hint 1
> In $\mathcal{O}$'s coordinates, $u_0 = (1,0,0,0)$. Since $\Omega = d\pi$, the contraction $[\Omega(\cdot, u_0)]_\alpha = \partial_\alpha\langle\pi, u_0\rangle - \partial_0\pi_\alpha$. Stationarity kills $\partial_0\pi_\alpha$, so $\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle$.

> [!note]- Hint 2
> Feed in $u$: $\nabla_u\langle\pi, u_0\rangle = \Omega(u, u_0) = T\langle dS, u_0\rangle = T\nabla_{u_0}S$. Stationarity kills $\nabla_{u_0}S = (1/c)\partial_t S = 0$. Hence $\nabla_u\langle\pi, u_0\rangle = 0$.

> [!note]- Hint 3
> $\langle\pi, u_0\rangle = h(u\cdot u_0) = h\Gamma$. Expand $\Gamma \simeq 1 + \tfrac12 V^2$, $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$, so $h\Gamma \simeq m_{\mathrm b}c^2 + m_{\mathrm b}(H + \tfrac12 V^2)$. Dropping the constant rest energy, $H + \tfrac12 V^2$ is conserved.

> [!note]- Hint 4
> For the nozzle, conservation of $H + \tfrac12 V^2$ along a streamline means $H$ falls as $V$ rises. Since enthalpy and pressure rise together (for a normal fluid), the pressure drops where the flow speeds up — the Venturi effect.

---

# Solution

Bernoulli's theorem is the canonical equation contracted with the time-translation symmetry: stationarity makes the contracted vorticity a gradient and kills the entropy source, leaving the energy per baryon $h\Gamma$ constant along each streamline.

**Step 1: $h\Gamma$ is conserved along the flow.**

> [!note]- Derivation
> Work in $\mathcal{O}$'s coordinates, where $u_0 = (1,0,0,0)$. Since $\Omega = d\pi$, $\Omega_{\alpha\beta} = \partial_\alpha\pi_\beta - \partial_\beta\pi_\alpha$, and contracting with $u_0^\beta = \delta^\beta_0$,
> $$[\Omega(\cdot, u_0)]_\alpha = \partial_\alpha(\pi_\beta u_0^\beta) - \partial_0\pi_\alpha = \partial_\alpha\langle\pi, u_0\rangle - \partial_0\pi_\alpha.$$
> Stationarity means each $\pi_\alpha$ is independent of $t = x^0$, so $\partial_0\pi_\alpha = 0$ and $\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle$. Feed in the four-velocity:
> $$\nabla_u\langle\pi, u_0\rangle = \Omega(u, u_0).$$
> By the [[Def - Vorticity 2-Form|canonical equation]] $\Omega(u,\cdot) = T\,dS$, the right side is $T\langle dS, u_0\rangle = T\nabla_{u_0}S = T\cdot\frac{1}{c}\partial_t S = 0$ by stationarity. Hence
> $$\nabla_u\langle\pi, u_0\rangle = 0,$$
> and $\langle\pi, u_0\rangle = h(u\cdot u_0) = h\Gamma$ is constant along each fluid line.

**Step 2: The classical Bernoulli constant.**

> [!note]- Derivation
> Expand for slow motion: $\Gamma \simeq 1 + \tfrac12 V^2/c^2$ and $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$ with $H$ the specific internal enthalpy. Then
> $$h\Gamma \simeq m_{\mathrm b}c^2\Big(1 + \frac{H}{c^2}\Big)\Big(1 + \frac{V^2}{2c^2}\Big) \simeq m_{\mathrm b}c^2 + m_{\mathrm b}\Big(H + \frac{V^2}{2}\Big),$$
> to first order in $1/c^2$. The constant $m_{\mathrm b}c^2$ aside, conservation of $h\Gamma$ is conservation of
> $$H + \frac{V^2}{2} = \text{const along each streamline},$$
> the **classical Bernoulli theorem**: specific enthalpy plus kinetic energy per unit mass is constant along a streamline in steady flow.

**Step 3: Flow through a nozzle.**

> [!note]- Derivation
> Along a streamline through a steady converging nozzle, $H + \tfrac12 V^2$ is constant, so where the flow accelerates ($V$ increases) the specific enthalpy $H$ must decrease by $\Delta H = -\Delta(\tfrac12 V^2)$. For a normal fluid the enthalpy increases with pressure (at fixed entropy, $dH = dp/\rho_{\mathrm m} > 0$ for $dp > 0$), so a drop in enthalpy is a drop in pressure: the pressure is *lowest* where the flow is *fastest*. This is the **Venturi effect**, the principle behind the carburettor, the aerofoil (faster flow over the curved upper surface $\Rightarrow$ lower pressure $\Rightarrow$ lift), and the constriction flowmeter. In the relativistic version, the same conservation of $h\Gamma$ governs the acceleration of astrophysical jets: enthalpy at the base converts to bulk Lorentz factor downstream.

> [!note]- Complete formal solution
> In $\mathcal{O}$'s coordinates with $u_0 = (1,0,0,0)$, stationarity gives $\Omega(\cdot, u_0) = d\langle\pi, u_0\rangle$ (the $\partial_0\pi_\alpha$ term vanishes). Feeding in $u$ and using the canonical equation, $\nabla_u\langle\pi, u_0\rangle = \Omega(u, u_0) = T\nabla_{u_0}S = 0$ (again by stationarity). Hence $h\Gamma = \langle\pi, u_0\rangle$ is constant along each fluid line. Expanding $\Gamma \simeq 1 + \tfrac12 V^2$, $h \simeq m_{\mathrm b}c^2(1 + H/c^2)$ recovers $H + \tfrac12 V^2$ constant — classical Bernoulli. In a nozzle this means the pressure drops where the flow speeds up (Venturi), and relativistically it means jet enthalpy converts to bulk Lorentz factor. $\blacksquare$

---

# Key Takeaways

**Bernoulli is a Noether theorem: a symmetry gives a conserved scalar along the flow.** The deepest lesson is that Bernoulli's theorem is not a special algebraic trick but the fluid instance of the symmetry–conservation correspondence. Stationarity is invariance under time translation, and the conserved Noether charge is $\langle\pi, u_0\rangle$ — the time-component of the fluid momentum-per-baryon, i.e. the energy per baryon. The fluid momentum one-form $\pi = hu$ plays exactly the role of a particle's four-momentum $mcu$, and the fluid lines play the role of the particle worldline. The transferable insight is that *any* symmetry of the flow produces a conserved $\langle\pi, G\rangle$: axisymmetry gives conserved angular momentum per baryon, a Killing vector in curved spacetime gives a conserved energy. When you see a steady or symmetric flow, look for the conserved $\langle\pi, G\rangle$ — it is the relativistic Bernoulli constant for that symmetry.

**Stationarity is used twice, and the conserved scalar carries the enthalpy.** The technical heart is that stationarity enters the proof at two points: it makes the contracted vorticity $\Omega(\cdot, u_0)$ a pure gradient (killing $\partial_0\pi$), and it kills the thermodynamic source $\nabla_{u_0}S$. Both are needed; missing either breaks the conservation. And the conserved scalar is $h\Gamma$ with the *enthalpy per baryon* $h$, not the Lorentz factor alone — the enthalpy weighting from $\pi = hu$ is what makes the conserved quantity reduce to "specific enthalpy plus kinetic energy" rather than "kinetic energy" alone. The diagnostic to carry: the relativistic Bernoulli constant is energy per baryon, $h\Gamma$, and its enthalpy content is what distinguishes it from a bare kinematic factor. Forgetting the enthalpy gives the wrong classical limit.

**Faster flow means lower pressure, from jets to wings.** The physical payoff — conservation of $H + \tfrac12 V^2$ — says that where a steady flow speeds up, its enthalpy and pressure drop. This single statement explains lift on an aerofoil (faster flow over the top, lower pressure, net upward force), the Venturi constriction (flow accelerates and pressure falls in the throat), Torricelli's law for tank drainage, and, relativistically, the acceleration of jets (enthalpy converts to Lorentz factor). The trigger for applying Bernoulli is any steady flow where you want to relate speed and pressure at two points on a streamline: equate $H + \tfrac12 V^2$ at the two points. The relativistic and classical versions are the same statement at different speeds — the jet engine and the astrophysical jet obey one conservation law, distinguished only by the magnitude of $\Gamma$.
