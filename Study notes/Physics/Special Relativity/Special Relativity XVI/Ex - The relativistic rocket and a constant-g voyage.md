---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Worldline of a Uniformly Accelerated Observer"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Def - Rindler Horizon"
tags: [physics, special-relativity]
---

# Problem Statement

A rocket undergoes constant proper acceleration $g = 9.8\,\mathrm{m\,s^{-2}}$ (so the crew feel Earth-normal gravity), starting from rest. Working with $c$ restored:

1. Find the inertial-frame (Earth) time $t_*$, the distance $x_*$ travelled, and the onboard proper (crew) time $\tau$, each as a function of the others, for a voyage under constant $g$.
2. Show that for a long voyage the crew time grows only *logarithmically* with the distance, so that one can cross the galaxy ($\sim 30{,}000$ light-years) in a few decades of crew time while tens of thousands of years pass on Earth. Give the crew time to reach the galactic centre.
3. Consider a "there-and-back" or "accelerate-then-decelerate" trip: a rocket accelerates at $g$ for the first half and decelerates at $g$ for the second, to a destination a distance $D$ away. Find the total crew time and Earth time, and the relation to the [[Def - Rindler Horizon|Rindler horizon]] (why the rocket "never feels it has gone far").
4. Derive the **relativistic rocket equation** $\Delta v = c\tanh(g\tau_{\mathrm{burn}}/c)$ for the velocity gained in proper burn time $\tau_{\mathrm{burn}}$, and the mass ratio $M_i/M_f = \exp(\Delta\varphi\,c/v_{\mathrm{ex}})$ from four-momentum conservation, with $v_{\mathrm{ex}}$ the exhaust speed and $\Delta\varphi$ the rapidity gained.

**Recall:**

A rocket maintaining constant accelerometer reading $g$ is a [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] with proper acceleration $a = g/c^2$ (an inverse length).

![[Thm - Worldline of a Uniformly Accelerated Observer#Statement]]

The key results from the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]], with $c$ restored and $a = g/c^2$: velocity $u = gt_*/\sqrt{1 + (gt_*/c)^2}$; position $x_* = (c^2/g)[\sqrt{1 + (gt_*/c)^2} - 1]$; proper time $\tau = (c/g)\sinh^{-1}(gt_*/c)$; rapidity $\varphi = g\tau/c$. The Rindler horizon sits a distance $a^{-1} = c^2/g$ behind the rocket.

---

# Convergent Strategy

**Problem class.** A *compute-a-trajectory* problem extended into a *relativistic-effect* computation: take the hyperbolic worldline and extract the physically meaningful times and distances for a realistic voyage, then apply momentum conservation to the propulsion. The decisive move is to use the proper-time formula $\tau = (c/g)\sinh^{-1}(gt_*/c)$ and read off its logarithmic late-time behaviour.

**Assumption pattern.** Constant proper acceleration $g$, hence hyperbolic motion, hence $\tau = (c/g)\sinh^{-1}(gt_*/c)$ and $x_* = (c^2/g)[\cosh(g\tau/c) - 1]$. The signpost for part 2 is "long voyage": $g\tau/c \gg 1$ makes $\cosh$ and $\sinh$ exponential, so distance grows *exponentially* in crew time, equivalently crew time grows logarithmically in distance.

**Theorem routing.** Parts 1–3 route through the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]]: express everything in terms of the rapidity $\varphi = g\tau/c$, which is additive and makes the accelerate-then-decelerate trip a matter of adding and subtracting rapidities. Part 4 routes through four-momentum conservation: the rocket equation is the relativistic analogue of Tsiolkovsky's, with rapidity replacing velocity, derived by demanding conservation of the total (rocket + exhaust) four-momentum.

**Key decision point.** The crux of parts 2–3 is recognising that the *distance* the crew thinks they have travelled is bounded in a way the Earth distance is not — the perceived distance to the horizon is only $c^2/g\approx 1$ light-year. The accelerate-decelerate trip's subtlety is the turnaround: the rapidity must be built up to a maximum and then brought back to zero, and the symmetric split (half accelerating, half decelerating) is what minimises crew time for a rest-to-rest trip. Using rapidity additivity rather than velocity addition is what keeps the bookkeeping clean.

---

# Legal Operations Used

1. **Integrate constant proper acceleration into a hyperbola** (operation 1 from the topic page). All of the times and distances come from the hyperbolic worldline, with $a = g/c^2$ and the proper time $\tau = (c/g)\sinh^{-1}(gt_*/c)$.

2. **Switch to rapidity to make boosts additive** (operation 6 from the topic page). The accelerate-then-decelerate trip is handled by adding rapidities: build up $\varphi$, then subtract it back to zero. The rocket equation $\Delta v = c\tanh(g\tau_{\mathrm{burn}}/c)$ is rapidity addition in disguise.

3. **Take the low-velocity / small-distance limit to recover Newtonian results** (operation 9 from the topic page). For $g\tau/c\ll 1$ the formulas reduce to $x_* \approx \tfrac12 g\tau^2$ and $\tau\approx t_*$ — the Newtonian voyage — confirming the relativistic formulas in the appropriate limit.

---

# Hints

> [!note]- Hint 1
> Everything follows from $x_* = (c^2/g)[\cosh(g\tau/c) - 1]$ and $ct_* = (c^2/g)\sinh(g\tau/c)$, which are the hyperbolic worldline parametrised by *crew* proper time $\tau$ (set $a = g/c^2$ and $a\tau \to g\tau/c$). Invert as needed: $g\tau/c = \cosh^{-1}(1 + gx_*/c^2)$, or for the distance in terms of crew time, $x_* = (c^2/g)[\cosh(g\tau/c) - 1]$.

> [!note]- Hint 2
> For $g\tau/c \gg 1$, $\cosh(g\tau/c)\approx \tfrac12 e^{g\tau/c}$, so $x_* \approx (c^2/2g)e^{g\tau/c}$. Inverting, $\tau \approx (c/g)\ln(2gx_*/c^2)$ — logarithmic in distance. Plug in $x_* = 30{,}000$ light-years $= 30{,}000\,c\cdot\mathrm{yr}$ and $g = 9.8\,\mathrm{m\,s^{-2}}$. Useful number: $c/g \approx 0.97\,\mathrm{yr} \approx 1\,\mathrm{yr}$, and $g/c \approx 1.03\,\mathrm{yr^{-1}}$, so $g\cdot\mathrm{yr}/c \approx 1$.

> [!note]- Hint 3
> For the accelerate-decelerate trip to a destination $D$ away (rest to rest), by symmetry each half covers $D/2$. The crew time for each half is $\tau_{1/2} = (c/g)\cosh^{-1}(1 + gD/(2c^2))$, total $\tau = 2\tau_{1/2}$. The "perceived distance" / horizon connection: at any instant the rocket's Rindler horizon is only $c^2/g \approx 1$ light-year behind, and the distance the crew *reckons* (by their own rest-frame measurement) saturates — Tong's "doesn't think he's got far".

> [!note]- Hint 4
> The rocket equation: in proper burn time $\tau_{\mathrm{burn}}$ at constant proper acceleration $g$, the rapidity gained is $\Delta\varphi = g\tau_{\mathrm{burn}}/c$, so the velocity is $\Delta v = c\tanh(\Delta\varphi) = c\tanh(g\tau_{\mathrm{burn}}/c)$. For the mass ratio, conserve four-momentum: each bit of exhaust ejected at speed $v_{\mathrm{ex}}$ (rapidity $\varphi_{\mathrm{ex}} = \tanh^{-1}(v_{\mathrm{ex}}/c)$) changes the rocket's rapidity by $\mathrm{d}\varphi = -(v_{\mathrm{ex}}/c)\,\mathrm{d}M/M$. Integrate.

---

# Solution

The voyage is the hyperbolic worldline read for human purposes. Step 1 collects the time-and-distance formulas in crew-time form. Step 2 extracts the logarithmic growth that makes interstellar travel feasible for the crew (if not for those left behind). Step 3 handles the realistic rest-to-rest trip via rapidity addition and ties it to the horizon. Step 4 derives the propulsion law. The non-obvious content is the exponential/logarithmic late-time behaviour (Step 2) and the rapidity-additivity that organises the turnaround and the rocket equation (Steps 3–4).

**Step 1: $x_* = (c^2/g)[\cosh(g\tau/c) - 1]$, $ct_* = (c^2/g)\sinh(g\tau/c)$, $u = c\tanh(g\tau/c)$.**

> [!note]- Derivation
> A rocket with constant accelerometer reading $g$ has proper acceleration $a = g/c^2$ (the four-acceleration norm; recall $\|A\| = a$ is an inverse length and $g = c^2 a$ the ordinary acceleration). Substituting $a = g/c^2$ into the [[Thm - Worldline of a Uniformly Accelerated Observer|worldline theorem]]'s formulas, parametrised by crew proper time $\tau$ (which is the observer's $t$):
> $$ct_* = a^{-1}\sinh(ac\tau) = \frac{c^2}{g}\sinh\!\Big(\frac{g\tau}{c}\Big), \qquad x_* = a^{-1}[\cosh(ac\tau) - 1] = \frac{c^2}{g}\Big[\cosh\!\Big(\frac{g\tau}{c}\Big) - 1\Big],$$
> and the velocity relative to Earth is $u = c\tanh(g\tau/c)$, the rapidity $\varphi = g\tau/c$. Inverting the distance relation, $g\tau/c = \cosh^{-1}(1 + gx_*/c^2)$, and the Earth time $t_* = (c/g)\sinh(g\tau/c)$. For $g\tau/c \ll 1$ these reduce to the Newtonian $x_*\approx\tfrac12 g\tau^2$, $t_*\approx\tau$, $u\approx g\tau$ — the everyday voyage. The numbers that make the rest tractable: $c/g \approx 0.97$ years, so $g\cdot(\text{1 year})/c \approx 1.03 \approx 1$; that is, accelerating at $g$ for about a year of crew time brings the rapidity to $\approx 1$ and the speed to $\tanh(1)\approx 0.76\,c$.

**Step 2: Crew time is logarithmic in distance; the galactic centre is $\approx 19$ years of crew time, $\approx 30{,}000$ years of Earth time.**

> [!note]- Derivation
> For a long voyage, $g\tau/c \gg 1$, so $\cosh(g\tau/c)\approx\sinh(g\tau/c)\approx\tfrac12 e^{g\tau/c}$. Then
> $$x_* \approx \frac{c^2}{2g}\,e^{g\tau/c} \quad\Longrightarrow\quad \tau \approx \frac{c}{g}\ln\!\Big(\frac{2gx_*}{c^2}\Big).$$
> The distance grows *exponentially* in crew time, equivalently crew time grows only *logarithmically* in distance. Meanwhile the Earth time $t_* = (c/g)\sinh(g\tau/c) \approx x_*/c$ grows *linearly* — the rocket is moving at nearly $c$, so Earth-frame time is essentially the light-travel time.
>
> To the galactic centre, $x_* = 30{,}000$ light-years. With $c/g\approx 0.97\,\mathrm{yr}$ and $g/c\approx 1.03\,\mathrm{yr^{-1}}$,
> $$\tau \approx (0.97\,\mathrm{yr})\ln\!\big(2\times 1.03\,\mathrm{yr^{-1}}\times 30{,}000\,\mathrm{yr}\big) = (0.97\,\mathrm{yr})\ln(6.2\times 10^4) \approx (0.97)(11.0)\,\mathrm{yr} \approx 11\,\mathrm{yr}.$$
> A fuller computation using $\tau = (c/g)\cosh^{-1}(1 + gx_*/c^2)$ gives $\approx 10$–$11$ years one-way for continuous acceleration. The crew reaches the galactic centre in about a decade of their own time, while $\approx 30{,}000$ years pass on Earth — the most dramatic illustration of [[Ex - Hyperbolic motion under constant proper acceleration|time dilation]] under sustained acceleration. The asymmetry is the constant-$g$ twin paradox: the proper-time deficit of the bent hyperbolic worldline relative to Earth's straight one.

**Step 3: A rest-to-rest trip to distance $D$ takes crew time $\tau = (4c/g)\cosh^{-1}(1 + gD/(4c^2))$... by halves; the horizon bounds the perceived distance.**

> [!note]- Derivation
> For a rest-to-rest voyage of total distance $D$, accelerate at $g$ for the first half-distance $D/2$, then *decelerate* at $g$ for the second half — by symmetry the two halves take equal crew time. Each half is a hyperbolic segment covering distance $D/2$, so by Step 1 (inverted) each takes crew time
> $$\tau_{1/2} = \frac{c}{g}\cosh^{-1}\!\Big(1 + \frac{gD}{2c^2}\Big), \qquad \tau_{\mathrm{total}} = 2\tau_{1/2} = \frac{2c}{g}\cosh^{-1}\!\Big(1 + \frac{gD}{2c^2}\Big).$$
> (The four-leg there-and-back trip, accelerating and decelerating twice, is $4\tau_{1/2}$.) In rapidity terms: build the rapidity from $0$ up to $\varphi_{\max} = (g/c)\tau_{1/2}$ over the first half, then bring it back down to $0$ over the second — rapidities add and subtract linearly, which is why the symmetric split is natural.
>
> The horizon connection (Tong): at every instant of acceleration, the rocket's [[Def - Rindler Horizon|Rindler horizon]] sits only $c^2/g \approx 1$ light-year *behind* it. The distance the crew *reckons* to have travelled — measured in their instantaneous rest frame, $x' = x_*/\gamma$ — saturates at $x' \to c^2/g$ as $\tau\to\infty$ (length contraction shrinks the Earth-measured distance back down). So despite crossing the galaxy in Earth-frame terms, the crew "doesn't think they've gone far": their reckoned distance is bounded by the horizon scale. This is the perceived-distance signature of the horizon, the complement of [[Ex - The Rindler horizon and the light that never catches up|the light that never catches up]].

**Step 4: Rocket equation $\Delta v = c\tanh(g\tau_{\mathrm{burn}}/c)$; mass ratio $M_i/M_f = \exp(\Delta\varphi\,c/v_{\mathrm{ex}})$.**

> [!note]- Derivation
> *Velocity from burn time.* At constant proper acceleration $g$, the rapidity accumulates linearly: $\Delta\varphi = (g/c)\tau_{\mathrm{burn}}$ after proper burn time $\tau_{\mathrm{burn}}$. Since $v = c\tanh\varphi$, the velocity gained (starting from rest) is
> $$\Delta v = c\tanh\!\Big(\frac{g\tau_{\mathrm{burn}}}{c}\Big).$$
> This is the **relativistic rocket equation** for velocity: it is just rapidity additivity, and it shows $\Delta v < c$ always (you cannot exceed light speed however long you burn), with the Newtonian $\Delta v\approx g\tau_{\mathrm{burn}}$ for short burns.
>
> *Mass ratio from four-momentum conservation.* In the rocket's instantaneous rest frame, ejecting a mass $|\mathrm{d}M|$ of exhaust at speed $v_{\mathrm{ex}}$ (rearward) carries away momentum, and conservation of the total four-momentum gives the rocket a rapidity increment. In the instantaneous rest frame the exhaust has rapidity $\varphi_{\mathrm{ex}} = \tanh^{-1}(v_{\mathrm{ex}}/c)$; balancing momentum to first order in $\mathrm{d}M$,
> $$M\,\mathrm{d}\varphi = -v_{\mathrm{ex}}\,\frac{\mathrm{d}M}{c}\cdot\frac{c}{c}\quad\Rightarrow\quad \mathrm{d}\varphi = -\frac{v_{\mathrm{ex}}}{c}\frac{\mathrm{d}M}{M},$$
> where $\mathrm{d}M < 0$ (the rocket loses mass) and $\mathrm{d}\varphi > 0$. Integrating from initial mass $M_i$ (rapidity $0$) to final $M_f$ (rapidity $\Delta\varphi$):
> $$\Delta\varphi = \frac{v_{\mathrm{ex}}}{c}\ln\!\Big(\frac{M_i}{M_f}\Big) \quad\Longleftrightarrow\quad \frac{M_i}{M_f} = \exp\!\Big(\frac{c\,\Delta\varphi}{v_{\mathrm{ex}}}\Big) = \exp\!\Big(\frac{c}{v_{\mathrm{ex}}}\tanh^{-1}\frac{\Delta v}{c}\Big).$$
> This is the relativistic Tsiolkovsky equation: it is the Newtonian $M_i/M_f = \exp(\Delta v/v_{\mathrm{ex}})$ with the velocity $\Delta v$ replaced by the rapidity $c\,\Delta\varphi = c\tanh^{-1}(\Delta v/c)$. Because rapidity diverges as $\Delta v\to c$, the mass ratio required to approach light speed grows *exponentially without bound* — the fundamental obstacle to relativistic rocketry. For a photon rocket ($v_{\mathrm{ex}} = c$), $M_i/M_f = e^{\Delta\varphi}$, the most efficient possible.

> [!note]- Complete formal solution
> A rocket at constant proper acceleration $g$ has $a = g/c^2$ and, by the worldline theorem in crew-time form, $x_* = (c^2/g)[\cosh(g\tau/c) - 1]$, $ct_* = (c^2/g)\sinh(g\tau/c)$, $u = c\tanh(g\tau/c)$, rapidity $\varphi = g\tau/c$. For $g\tau/c\gg 1$, $x_*\approx (c^2/2g)e^{g\tau/c}$, so crew time $\tau\approx (c/g)\ln(2gx_*/c^2)$ is logarithmic in distance while Earth time $t_*\approx x_*/c$ is linear: to the galactic centre ($30{,}000$ ly), $\tau\approx 10$–$11$ years against $\approx 30{,}000$ Earth years. A rest-to-rest trip of distance $D$ (accelerate then decelerate, by halves) takes crew time $\tau = (2c/g)\cosh^{-1}(1 + gD/2c^2)$; the crew's reckoned distance saturates at the horizon scale $c^2/g\approx 1$ ly (Tong). The relativistic rocket equation is $\Delta v = c\tanh(g\tau_{\mathrm{burn}}/c)$ (rapidity additivity), and four-momentum conservation gives the mass ratio $M_i/M_f = \exp(c\,\Delta\varphi/v_{\mathrm{ex}}) = \exp[(c/v_{\mathrm{ex}})\tanh^{-1}(\Delta v/c)]$, diverging as $\Delta v\to c$. $\blacksquare$

---

# Key Takeaways

**Sustained acceleration makes distance exponential in crew time — the galaxy is a decade away for the traveller, an age away for those left behind.** The headline result, that crew time grows only logarithmically with distance ($\tau\approx (c/g)\ln(2gx_*/c^2)$), is the single most striking consequence of hyperbolic motion, and it follows the instant you write $\cosh(g\tau/c)\approx\tfrac12 e^{g\tau/c}$ for a long voyage. The trigger to deploy it: any "how long does a constant-$g$ trip take" question — recognise that the Earth-frame time and the crew time diverge wildly because the rocket spends almost all the journey at nearly $c$. The reusable structure is that *constant proper acceleration means exponential-in-proper-time*: the Lorentz factor, the energy, the distance, and the redshift all grow like $e^{g\tau/c}$, the same exponential that appears in the Unruh temperature and in inflationary cosmology, where a constant "acceleration" (Hubble rate) drives exponential expansion.

**Rapidity additivity is the right bookkeeping for staged and reversed acceleration.** The accelerate-then-decelerate trip and the rocket equation both become simple once you work in rapidity: $\varphi = g\tau/c$ accumulates *linearly* in proper burn time, adds and subtracts across legs, and converts to velocity only at the end via $v = c\tanh\varphi$. The trigger: whenever a problem chains accelerations — a turnaround, a multi-stage burn, a there-and-back trip — switch to rapidity, do the arithmetic as ordinary addition and subtraction, and convert back. The velocity-addition formula and its nonlinearity are exactly what rapidity linearises, and the rocket equation $\Delta v = c\tanh(g\tau_{\mathrm{burn}}/c)$ *is* the statement "rapidity accumulates at rate $g/c$". This is the same principle that makes the relativistic Tsiolkovsky equation the Newtonian one with velocity replaced by rapidity.

**The mass ratio diverges as you approach light speed — this is the hard limit on rocketry.** The relativistic rocket equation $M_i/M_f = \exp[(c/v_{\mathrm{ex}})\tanh^{-1}(\Delta v/c)]$ shows that because rapidity $\tanh^{-1}(\Delta v/c)$ diverges as $\Delta v\to c$, the propellant mass required grows *exponentially without bound*. Even a perfectly efficient photon rocket ($v_{\mathrm{ex}} = c$) needs $M_i/M_f = e^{\varphi}$, which for $\varphi\sim 11$ (the galactic-centre rapidity at the moment of peak speed) is a mass ratio of $\sim 10^5$ — and that is one-way, ignoring deceleration. The diagnostic this leaves: in any relativistic propulsion estimate, the figure of merit is the *rapidity* to be gained, not the velocity, because the fuel cost is exponential in rapidity. The deeper lesson is that the Newtonian intuition "just keep burning" fails not because the engine weakens but because the geometry — the unboundedness of rapidity — makes the last increments of speed infinitely expensive.

**The perceived distance is bounded by the horizon, even as the Earth-frame distance is unbounded.** A subtle but important takeaway from Step 3 is that the crew, measuring distance in their own instantaneous rest frame, never reckons they have travelled more than about $c^2/g\approx 1$ light-year — the [[Def - Rindler Horizon|Rindler horizon]] scale — because length contraction shrinks the Earth-measured distance back down as their speed climbs. This is Tong's "despite all that effort, an accelerated observer doesn't think he's got very far", and it is the perceived-distance complement of the [[Ex - The Rindler horizon and the light that never catches up|light that never catches up]]: the horizon manifests both as a region the crew can never see *behind* and as a ceiling on the distance they reckon to have gone *ahead*. The reusable insight is that "distance travelled" is frame-dependent in accelerated motion, and the rest-frame-reckoned distance saturates at the horizon scale while the inertial-frame distance grows without bound — two correct answers measuring different things.

This exercise completes the §16.1 trio with [[Ex - Hyperbolic motion under constant proper acceleration]] (the underlying worldline) and [[Ex - The Rindler horizon and the light that never catches up]] (the horizon's other face).
