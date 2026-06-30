---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Equation of State and Speed of Sound"
  - "Thm - Energy-Momentum Conservation projected (Euler + energy equation)"
  - "Thm - Relativistic Euler Equation"
  - "Def - Perfect Fluid"
tags: [physics, special-relativity]
---

# Problem Statement

Consider an isolated homogeneous perfect fluid at rest (energy density $\rho$, pressure $p$ constant), and perturb it adiabatically: $\rho\to\rho+\delta\rho$, $\mathbf{V} = 0\to\delta\mathbf{V}$, with $\delta S = 0$.

1. Linearise the energy equation and the relativistic Euler equation about the static background to obtain the coupled system $\partial_t\delta\rho + (\rho+p)\nabla\cdot\delta\mathbf{V} = 0$ and $(\rho+p)\partial_t\delta\mathbf{V} = -\nabla\delta p$.
2. Using $\delta p = (\partial p/\partial\rho)_S\,\delta\rho$, eliminate $\delta\mathbf{V}$ to derive the wave equation $-c_s^{-2}\partial_t^2\delta\rho + \nabla^2\delta\rho = 0$ and read off $c_s^2 = (\partial p/\partial\rho)_S$.
3. Evaluate the sound speed for (a) a photon gas, $p = \rho/3$; (b) the stiff fluid $p = \rho$; (c) pressureless dust, $p = 0$. Comment on causality.

**Recall:**

The speed of sound is $c_s^2 = (\partial p/\partial\rho)_S$, the adiabatic slope of the [[Def - Equation of State and Speed of Sound|equation of state]]. The energy equation is $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$ and the relativistic Euler equation $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p$ (see [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]] and [[Thm - Relativistic Euler Equation]]). Causality requires $c_s \le c = 1$.

---

# Convergent Strategy

**Problem class.** A *linear-stability / wave-propagation* problem: perturb a background, linearise, and find the dispersion relation. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], extracting a characteristic speed requires *both* projections of the conservation law — the energy equation and the Euler equation together build the wave operator.

**Assumption pattern.** Three ingredients: a homogeneous static background (so background gradients vanish), an adiabatic perturbation (so $\delta S = 0$ and $\delta p = (\partial p/\partial\rho)_S\delta\rho$), and the [[Def - Equation of State and Speed of Sound|equation of state]] (to relate $\delta p$ to $\delta\rho$). The signpost "speed of sound" means: linearise, get a wave equation, read off the speed.

**Theorem routing.** Part 1 linearises the energy equation (from [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]) and the [[Thm - Relativistic Euler Equation|Euler equation]] about $\mathbf{V} = 0$. Part 2 uses the adiabatic equation of state $\delta p = c_s^2\delta\rho$ and combines $\partial_t$ of the energy equation with $\nabla\cdot$ of the Euler equation. Part 3 substitutes specific equations of state.

**Key decision point.** The crux is that the perturbation must be *adiabatic*: sound is fast compared to heat diffusion, so the entropy per baryon is held fixed and the derivative is $(\partial p/\partial\rho)_S$, not $(\partial p/\partial\rho)_T$. Using the isothermal derivative gives the wrong speed (Newton's error). The second decision is to combine the two linearised equations correctly — take the time derivative of one and the divergence of the other so the $\delta\mathbf{V}$ terms match and cancel.

---

# Legal Operations Used

1. **Project the conservation law along and orthogonal to $u$** (operations 1 and 2 from the topic page): the energy equation and the Euler equation are the two linearised inputs, and *both* are needed to build the wave operator.

2. **Compute thermodynamic derivatives from the equation of state** (operation 10): $\delta p = (\partial p/\partial\rho)_S\delta\rho$ closes the system and defines $c_s$.

3. **Use the unit-norm identity** (operation 3): in the rest-frame linearisation, $u^\mu \simeq (1, \delta\mathbf{V})$ to first order keeps $u\cdot u = 1$.

---

# Hints

> [!note]- Hint 1
> About the static background $\mathbf{V} = 0$, the four-velocity is $u^\mu \simeq (1, \delta V^i)$ to first order. The energy equation $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$ linearises to $\partial_t\delta\rho + (\rho+p)\partial_i\delta V^i = 0$ (background $\rho$, $p$ constant). The Euler equation $(\rho+p)a^i = -\nabla^i p$ linearises to $(\rho+p)\partial_t\delta V^i = -\partial_i\delta p$ (since $a^i \simeq \partial_t\delta V^i$ about rest).

> [!note]- Hint 2
> Adiabatic: $\delta p = (\partial p/\partial\rho)_S\,\delta\rho =: c_s^2\,\delta\rho$. Substitute into the Euler equation: $(\rho+p)\partial_t\delta V^i = -c_s^2\partial_i\delta\rho$. Now take $\partial_t$ of the energy equation and $\partial_i$ of this; subtract to eliminate $\delta V$.

> [!note]- Hint 3
> $\partial_t^2\delta\rho = -(\rho+p)\partial_i\partial_t\delta V^i = -(\rho+p)\partial_i[-c_s^2\partial_i\delta\rho/(\rho+p)] = c_s^2\nabla^2\delta\rho$. So $\partial_t^2\delta\rho = c_s^2\nabla^2\delta\rho$, a wave equation with speed $c_s$.

> [!note]- Hint 4
> For the photon gas $p = \rho/3$: $c_s^2 = dp/d\rho = 1/3$, $c_s = 1/\sqrt3$. For $p = \rho$: $c_s = 1$. For dust $p = 0$: $c_s = 0$.

---

# Solution

Linearising the energy and Euler equations about a static homogeneous background and closing with the adiabatic equation of state produces a wave equation for the density perturbation, whose speed is the adiabatic slope $c_s^2 = (\partial p/\partial\rho)_S$.

**Step 1: The linearised system.**

> [!note]- Derivation
> Choose the rest frame of the background fluid, so $\mathbf{V} = 0$, $\rho$, $p$ constant in space and time. The perturbed four-velocity is $u^\mu \simeq (1, \delta V^i)$ (keeping $u\cdot u = 1$ to first order). Linearise the two projected equations:
>
> *Energy equation* $u^\mu\nabla_\mu\rho + (\rho+p)\nabla_\mu u^\mu = 0$. To first order, $u^\mu\nabla_\mu\rho \simeq \partial_t\delta\rho$ (background $\rho$ constant) and $\nabla_\mu u^\mu \simeq \partial_i\delta V^i$, so
> $$\partial_t\delta\rho + (\rho+p)\,\partial_i\delta V^i = 0. \tag{a}$$
>
> *Euler equation* $(\rho+p)a^i = -\partial^i p$. About rest, $a^i \simeq \partial_t\delta V^i$, so
> $$(\rho+p)\,\partial_t\delta V^i = -\partial_i\delta p. \tag{b}$$

**Step 2: The wave equation and the sound speed.**

> [!note]- Derivation
> The perturbation is adiabatic, $\delta S = 0$, so by the [[Def - Equation of State and Speed of Sound|equation of state]] $p = p(\rho, S)$,
> $$\delta p = \Big(\frac{\partial p}{\partial\rho}\Big)_S\,\delta\rho =: c_s^2\,\delta\rho.$$
> Substitute into (b): $(\rho+p)\partial_t\delta V^i = -c_s^2\partial_i\delta\rho$. Now take $\partial_t$ of (a) and use this:
> $$\partial_t^2\delta\rho = -(\rho+p)\,\partial_i(\partial_t\delta V^i) = -\partial_i\big[(\rho+p)\partial_t\delta V^i\big] = -\partial_i\big[-c_s^2\partial_i\delta\rho\big] = c_s^2\,\nabla^2\delta\rho.$$
> Hence
> $$-\frac{1}{c_s^2}\,\partial_t^2\delta\rho + \nabla^2\delta\rho = 0,$$
> a **wave equation** with propagation speed $c_s$. The density perturbation $\delta\rho$ (and, via $\delta p = c_s^2\delta\rho$, the pressure perturbation) propagates at the **speed of sound**
> $$\boxed{c_s = \sqrt{\Big(\frac{\partial p}{\partial\rho}\Big)_S}}\quad(c = 1).$$

**Step 3: Specific equations of state.**

> [!note]- Derivation
> (a) **Photon gas**, $p = \rho/3$ (linear): $c_s^2 = dp/d\rho = 1/3$, so $c_s = 1/\sqrt3 \approx 0.577\,c$. The sound speed of a relativistic radiation fluid; subluminal, as required.
>
> (b) **Stiff fluid**, $p = \rho$: $c_s^2 = dp/d\rho = 1$, so $c_s = c$. Sound travels at the speed of light. This is the limiting causal equation of state — the "hardest" matter compatible with $c_s \le c$.
>
> (c) **Dust**, $p = 0$: $c_s = 0$. Pressureless matter transmits no pressure waves; there is nothing to restore a compression, so no sound. (Cold dark matter is "pressureless" in exactly this sense, which is why it clusters on all scales — no Jeans cutoff.)
>
> *Causality.* The bound $c_s \le c$ is a constraint on the *slope* $(\partial p/\partial\rho)_S \le 1$: the pressure may not rise faster than the energy density. It is saturated only by $p = \rho$. An equation of state with $dp/d\rho > 1$ would transmit sound superluminally and is forbidden.

> [!note]- Complete formal solution
> In the background rest frame, linearise about $\mathbf{V} = 0$ with $u^\mu \simeq (1, \delta V^i)$. The energy equation gives $\partial_t\delta\rho + (\rho+p)\partial_i\delta V^i = 0$ and the Euler equation $(\rho+p)\partial_t\delta V^i = -\partial_i\delta p$. The adiabatic equation of state gives $\delta p = c_s^2\delta\rho$ with $c_s^2 = (\partial p/\partial\rho)_S$. Taking $\partial_t$ of the first and $\partial_i$ of the second and combining yields $\partial_t^2\delta\rho = c_s^2\nabla^2\delta\rho$, a wave equation with speed $c_s$. For $p = \rho/3$, $c_s = 1/\sqrt3$; for $p = \rho$, $c_s = c$; for $p = 0$, $c_s = 0$. Causality requires the slope $(\partial p/\partial\rho)_S \le 1$, saturated by $p = \rho$. $\blacksquare$

**Independent check via the equation-of-state slope.** The result $c_s^2 = dp/d\rho$ can be verified directly: a sound wave is a small adiabatic compression, and the restoring "stiffness" is precisely how much $p$ rises per unit rise in $\rho$ at fixed entropy. The wave equation merely confirms that this stiffness is the squared propagation speed, as in any elastic medium where $c^2 = (\text{stiffness})/(\text{inertia})$ — here both the numerator and the role of inertia are folded into the single derivative because $\rho$ is the energy density.

---

# Key Takeaways

**The sound speed is the adiabatic slope, not a ratio — and both projections are needed.** The defining lesson is that $c_s^2 = (\partial p/\partial\rho)_S$ is a *derivative* of the equation of state taken at fixed entropy per baryon, and that deriving it requires *both* the energy equation and the Euler equation. The energy equation supplies $\partial_t\delta\rho \sim \nabla\cdot\delta\mathbf{V}$ (how compression changes density) and the Euler equation supplies $\partial_t\delta\mathbf{V} \sim \nabla\delta p$ (how a pressure gradient drives flow); combining them — time derivative of one, divergence of the other — builds the second-order wave operator. The transferable diagnostic is that whenever you want a propagation speed in a continuum, you linearise the *coupled* continuity-and-momentum system, not either equation alone, because a wave is an exchange between the density and velocity fields. And the speed is always a stiffness (a derivative of the restoring force law), never a crude ratio like $\sqrt{p/\rho}$ — the two coincide only for a linear equation of state.

**Adiabatic, not isothermal: the fixed-$S$ subscript is physics, not pedantry.** A sound wave compresses the fluid faster than heat can diffuse, so each element compresses *adiabatically*, holding its entropy per baryon fixed. This is why the derivative is $(\partial p/\partial\rho)_S$ and not $(\partial p/\partial\rho)_T$. The distinction is historically famous: Newton computed the speed of sound in air with the isothermal derivative and got an answer 18% too low; Laplace corrected it by using the adiabatic derivative, which for an ideal gas is larger by $\sqrt\gamma$. The lesson to carry: when a process is fast compared to its relevant transport (heat conduction, here), use the adiabatic (constant-entropy) thermodynamic derivative, and always ask *which variable is held fixed*. The fixed-$S$ subscript encodes the physical fact that sound is a reversible, isentropic oscillation.

**Causality is a bound on the stiffness, and $p = \rho$ is the hardest matter.** The requirement $c_s \le c$ translates into $(\partial p/\partial\rho)_S \le 1$: the equation of state may not stiffen faster than $p = \rho$. This single inequality constrains the densest stable matter and is the central question in neutron-star physics — how close can $c_s$ come to $c$ at the highest densities? The trigger to recall this: whenever an equation of state is proposed, check its slope against unity; a slope exceeding one signals acausal, superluminal sound and is unphysical. The two extremes computed here bracket the possibilities — dust ($c_s = 0$, infinitely soft, no sound) and the stiff fluid ($c_s = c$, maximally hard) — and every real fluid lies between, with the radiation value $1/\sqrt3$ a useful relativistic benchmark. This bound is also why the conservation-law system is hyperbolic with subluminal characteristics, which is what makes the initial-value problem well-posed and admits shocks.
