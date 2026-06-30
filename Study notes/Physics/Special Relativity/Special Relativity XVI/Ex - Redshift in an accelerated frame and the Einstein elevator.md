---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Spectral Shift in an Accelerated Frame"
  - "Def - Rindler Coordinates and the Accelerated Frame"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Problem Statement

A uniformly accelerated observer $\mathcal{O}$ of proper acceleration $a$ sits at Rindler position $x = 0$. A comoving emitter $\mathcal{O}'$, fixed at Rindler position $x_{\mathrm{em}}$, sends a photon of energy $E_{\mathrm{em}}$ (measured by $\mathcal{O}'$) toward $\mathcal{O}$. Working with $c = 1$ except where restored:

1. By writing the photon's four-momentum and parallel-transporting it to the reception event, derive the received energy $E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$, and the redshift factor $z = 1/(1 + ax_{\mathrm{em}}) - 1$.
2. Show the result is independent of the emission time, and determine the sign of the shift: red from below ($x_{\mathrm{em}} < 0$), blue from above, with $z \to +\infty$ as $x_{\mathrm{em}} \to -a^{-1}$.
3. Reinterpret the entire calculation in **Einstein's elevator**: a light beam crosses an accelerating cabin from floor to ceiling. Show it is redshifted exactly as if it had climbed out of a uniform gravitational field, and identify the gravitational-redshift formula $z \simeq -gh/c^2$ (to first order, blueshift falling).
4. Show how $\mathcal{O}$ can measure their own proper acceleration $a$ from the redshift $z$ and the round-trip light time $2T$ alone, recovering $a = \mp\ln(1+z)/(cT)$.

**Recall:**

![[Thm - Spectral Shift in an Accelerated Frame#Statement]]

The energy an observer with four-velocity $W$ assigns a photon of four-momentum $P$ is $E = P\cdot W$ (mostly-minus). A photon emitted by an observer momentarily at rest in the inertial frame $\mathcal{O}_*$ has $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$, null since $(e_0^*\pm e_1^*)\cdot(e_0^*\pm e_1^*) = 0$. The receiver $\mathcal{O}$ has four-velocity $U(t) = \cosh(act)e_0^* + \sinh(act)e_1^*$ at proper time $t$ ([[Thm - Worldline of a Uniformly Accelerated Observer]]). The photon trajectory in [[Def - Rindler Coordinates and the Accelerated Frame|Rindler coordinates]] is $ct = \pm a^{-1}\ln[(1+ax)/(1+ax_{\mathrm{em}})]$. **Einstein's equivalence principle:** a uniformly accelerated frame is locally indistinguishable from a uniform gravitational field of strength $g = c^2 a$.

---

# Convergent Strategy

**Problem class.** A *relativistic-effect-in-the-accelerated-frame* problem, the third class in the [[Special Relativity XVI — Accelerated Observers#Problem-Solving Strategy|topic strategy]]: compute a redshift, and read its position-dependence through the equivalence principle. The decisive move is to transport the photon's four-momentum and compute $E = P\cdot U$ at emission and reception.

**Assumption pattern.** The emitter and receiver are *comoving* — at rest with respect to each other — so there is *no relative velocity* and the ordinary Doppler effect gives nothing. The shift comes entirely from the position-dependent clock rate, $\mathrm{d}\tau = (1+ax)\mathrm{d}t$. The signpost is "fixed in the accelerated frame": the emitter is a comoving observer, and the redshift is governed by the lapse factor $1 + ax_{\mathrm{em}}$.

**Theorem routing.** The route is: write $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$ (null, fixed in the inertial frame) $\Rightarrow$ find the reception time from the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler]] photon trajectory $\Rightarrow$ compute $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}}) = E_{\mathrm{em}}e^{\mp act_{\mathrm{rec}}} = E_{\mathrm{em}}(1+ax_{\mathrm{em}})$, the [[Thm - Spectral Shift in an Accelerated Frame|spectral-shift theorem]]. The equivalence principle then maps $ax_{\mathrm{em}} = gx_{\mathrm{em}}/c^2 = \Phi/c^2$ to the gravitational redshift.

**Key decision point.** The crux is recognising that two mutually-at-rest observers can disagree on frequency *without any Doppler effect*, because their clocks run at position-dependent rates. The trap is to look for a relative velocity to plug into the Doppler formula; there is none. The shift is the ratio of lapse functions at emitter and receiver, $1 + ax_{\mathrm{em}}$, which is the same factor as the clock desynchronization — the redshift is the desynchronization read out with light.

---

# Legal Operations Used

1. **Transport a photon's four-momentum and read energy as $E = P\cdot U$** (operation 6 from the topic page). Compute $P = E_{\mathrm{em}}(e_0^*\pm e_1^*)$ once at emission, parallel-transport it (it is constant in the inertial frame), and dot with the receiver's four-velocity at reception; the ratio is the spectral shift.

2. **Choose the tangent inertial observer and compute there** (operation 2 from the topic page). Working in $\mathcal{O}_*$'s inertial frame, with emission taken at $t = 0$ by stationarity, makes $P$ a fixed null vector and the photon trajectory a straight $45^\circ$ line.

3. **Take the low-velocity / small-distance limit to recover Newtonian gravity** (operation 9 from the topic page). Expanding $z = 1/(1+ax_{\mathrm{em}}) - 1 \approx -ax_{\mathrm{em}}$ and writing $\Phi = c^2 ax_{\mathrm{em}}$ recovers the gravitational redshift $z\approx -\Phi/c^2$.

---

# Hints

> [!note]- Hint 1
> The emitter and receiver are at rest with respect to each other, so there is no relative velocity and *no ordinary Doppler shift*. Do not look for a velocity. Instead, write the photon four-momentum $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$ (it is null and constant in the inertial frame) and compute the energy the receiver assigns, $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}})$.

> [!note]- Hint 2
> Find $t_{\mathrm{rec}}$ from the photon trajectory: in Rindler coordinates $ct = \pm a^{-1}\ln[(1+ax)/(1+ax_{\mathrm{em}})]$, set $x = 0$ to get $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1+ax_{\mathrm{em}})$. Then $E_{\mathrm{rec}} = E_{\mathrm{em}}(e_0^*\pm e_1^*)\cdot[\cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*] = E_{\mathrm{em}}(\cosh \mp \sinh) = E_{\mathrm{em}}e^{\mp act_{\mathrm{rec}}}$.

> [!note]- Hint 3
> Substitute $\mp act_{\mathrm{rec}} = \ln(1+ax_{\mathrm{em}})$ so $e^{\mp act_{\mathrm{rec}}} = 1 + ax_{\mathrm{em}}$, giving $E_{\mathrm{rec}} = E_{\mathrm{em}}(1+ax_{\mathrm{em}})$. The reception time has dropped out — the result is independent of *when* the photon was emitted, reflecting the stationarity of $\mathcal{O}$.

> [!note]- Hint 4
> For the elevator: a light beam from floor ($x_{\mathrm{em}} = -h$, below) to ceiling ($x = 0$) has $z = 1/(1 - ah) - 1 \approx ah$ for small $ah$ — a redshift. With $g = c^2 a$ and the floor a height $h$ below, $z\approx gh/c^2$. By the equivalence principle this is *identical* to the gravitational redshift of light climbing height $h$ in gravity $g$. (Light *falling* floor-to-ceiling in an upward-accelerating elevator... be careful: the floor accelerates up toward the light, blueshifting it; match signs to the gravitational case where falling light is blueshifted.)

---

# Solution

The redshift is the ratio of clock rates at the two ends, read out with a photon. Step 1 does the four-momentum computation and gets $E_{\mathrm{rec}} = E_{\mathrm{em}}(1+ax_{\mathrm{em}})$. Step 2 notes the time-independence and the sign. Step 3 reinterprets it in Einstein's elevator and extracts the gravitational redshift. Step 4 turns it into a measurement of $a$. The non-obvious move, in Step 1, is that there is *no Doppler effect* — the comoving observers have zero relative velocity — and the shift is purely the lapse-ratio.

**Step 1: The received energy is $E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$.**

> [!note]- Derivation
> By stationarity, take emission at $t = 0$, where the comoving emitter is momentarily at rest in $\mathcal{O}_*$, so its four-velocity is $e_0^*$. The photon four-momentum is the null, future-directed vector $P = E_{\mathrm{em}}(e_0^* + \sigma e_1^*)$, $\sigma = \pm 1$ the propagation direction; indeed $P\cdot P = E_{\mathrm{em}}^2(1 - \sigma^2) = 0$ and $E_{\mathrm{em}} = P\cdot e_0^* = E_{\mathrm{em}}$ checks. For a photon travelling from $x_{\mathrm{em}} < 0$ toward $x = 0$, $\sigma = +1$ (rightward); from $x_{\mathrm{em}} > 0$, $\sigma = -1$. Being a free photon, $P$ is constant in the inertial frame, so the same $P$ is used at reception. The receiver's four-velocity at proper time $t_{\mathrm{rec}}$ is $U(t_{\mathrm{rec}}) = \cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*$, and the received energy is
> $$E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}}) = E_{\mathrm{em}}(e_0^* + \sigma e_1^*)\cdot[\cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*] = E_{\mathrm{em}}[\cosh(act_{\mathrm{rec}}) - \sigma\sinh(act_{\mathrm{rec}})],$$
> using $e_0^*\cdot e_0^* = 1$, $e_1^*\cdot e_1^* = -1$. With $\sigma = \pm 1$ this is $E_{\mathrm{em}}e^{\mp act_{\mathrm{rec}}}$.
>
> The reception time comes from the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler photon trajectory]] $ct = \sigma a^{-1}\ln[(1+ax)/(1+ax_{\mathrm{em}})]$ at $x = 0$: $ct_{\mathrm{rec}} = -\sigma a^{-1}\ln(1+ax_{\mathrm{em}})$, so $-\sigma act_{\mathrm{rec}} = \ln(1+ax_{\mathrm{em}})$ and $e^{-\sigma act_{\mathrm{rec}}} = 1 + ax_{\mathrm{em}}$. Therefore
> $$E_{\mathrm{rec}} = E_{\mathrm{em}}\,e^{-\sigma act_{\mathrm{rec}}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}}).$$
> By $E = hf$, the frequency obeys $f_{\mathrm{rec}} = f_{\mathrm{em}}(1+ax_{\mathrm{em}})$, the wavelength $\lambda_{\mathrm{rec}} = \lambda_{\mathrm{em}}/(1+ax_{\mathrm{em}})$, and the redshift factor is $z = \lambda_{\mathrm{rec}}/\lambda_{\mathrm{em}} - 1 = 1/(1+ax_{\mathrm{em}}) - 1$.

**Step 2: The result is independent of emission time; red below, blue above, infinite redshift at the horizon.**

> [!note]- Derivation
> $E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$ depends only on the emitter's position $x_{\mathrm{em}}$, *not* on the reception time $t_{\mathrm{rec}}$ — the time dropped out when the trajectory equation was substituted. This is required by the stationarity of $\mathcal{O}$: nothing about $\mathcal{O}$'s local physics changes with proper time, so a photon emitted later arrives equally shifted.
>
> Signs: for $x_{\mathrm{em}} < 0$ (emitter *below* the receiver, nearer the horizon), $1 + ax_{\mathrm{em}} < 1$, so $E_{\mathrm{rec}} < E_{\mathrm{em}}$ and $z > 0$ — a **redshift**. As $x_{\mathrm{em}}\to -a^{-1}$ (the emitter approaches the [[Def - Rindler Horizon|Rindler horizon]]), $1 + ax_{\mathrm{em}}\to 0$ and $z\to +\infty$: light from the horizon arrives infinitely reddened, with zero energy. For $x_{\mathrm{em}} > 0$ (emitter *above*), $1 + ax_{\mathrm{em}} > 1$, $z < 0$ — a **blueshift**. The pattern "red from below, blue from above" is the hallmark of climbing out of (or falling into) a potential.

**Step 3: Einstein's elevator — the redshift is the gravitational redshift, $z \simeq -gh/c^2$.**

> [!note]- Derivation
> Einstein's elevator is a cabin accelerating "upward" (in the $+e_1^*$ direction) at proper acceleration $a$, with no windows — by the **equivalence principle**, its occupants cannot tell whether they are accelerating in deep space or standing still in a uniform gravitational field of strength $g = c^2 a$ pointing "down" ($-e_1^*$).
>
> A light beam is emitted at the floor and received at the ceiling, a height $h$ above. In Rindler coordinates the ceiling is the receiver at $x = 0$ and the floor is the emitter at $x_{\mathrm{em}} = -h$ (below). By Steps 1–2, $z = 1/(1 - ah) - 1 \approx ah$ for $ah\ll 1$ — a **redshift** of the light reaching the ceiling. The accelerating-frame explanation: during the photon's flight, the ceiling accelerates *away* from the oncoming light (it speeds up while the photon is in transit), so the light arrives with reduced frequency.
>
> Now read it through the equivalence principle. In the equivalent gravitational field, the floor is at *lower* potential $\Phi_{\mathrm{floor}} = -gh$ (taking the ceiling as $\Phi = 0$). Light *climbing* from floor to ceiling — out of the potential well — loses energy and is redshifted by
> $$z \simeq \frac{\Phi_{\mathrm{ceiling}} - \Phi_{\mathrm{floor}}}{c^2} = \frac{gh}{c^2},$$
> writing $\Phi = c^2 ax$ so $ah = \Phi_{\mathrm{difference}}/c^2$. This is the **gravitational redshift**: light climbing height $h$ in gravity $g$ is redshifted by $gh/c^2$ (and light *falling* is blueshifted by the same). The accelerated-frame calculation and the gravitational one give *identical* answers — that identity is the equivalence principle, and it is the content of the [[Special Relativity XVI — Accelerated Observers#Insights|"position-dependence is the fingerprint of gravity"]] insight: each factor $1 + ax$ is $1 + \Phi/c^2$.

**Step 4: $\mathcal{O}$ measures $a$ from $z$ and the round-trip light time, $a = \mp\ln(1+z)/(cT)$.**

> [!note]- Derivation
> The redshift gives $\mathcal{O}$ the quantity $ax_{\mathrm{em}}$: from $z = 1/(1+ax_{\mathrm{em}}) - 1$, $1 + ax_{\mathrm{em}} = 1/(1+z)$, so $ax_{\mathrm{em}} = 1/(1+z) - 1 = -z/(1+z)$. But $\mathcal{O}$ does not yet know $a$ and $x_{\mathrm{em}}$ separately. To separate them, $\mathcal{O}$ also measures the round-trip light time $2T$ of a photon bounced between $x = 0$ and $x_{\mathrm{em}}$. The rigid-ruler result gives the rest length in terms of $T$: $\ell_0 = |x_{\mathrm{em}}| = a^{-1}|e^{\pm acT} - 1|$, i.e. $1 + ax_{\mathrm{em}} = e^{\pm acT}$ (the round-trip relation, sign $\pm = \mathrm{sgn}(x_{\mathrm{em}})$). Comparing with $1 + ax_{\mathrm{em}} = 1/(1+z)$:
> $$e^{\pm acT} = \frac{1}{1+z} \quad\Longrightarrow\quad \pm acT = -\ln(1+z) \quad\Longrightarrow\quad a = \mp\frac{\ln(1+z)}{cT}.$$
> So $\mathcal{O}$ determines their *own* proper acceleration purely from a redshift measurement and a light-travel-time measurement — both performed locally, with no external reference. This shows the four-acceleration norm is a *measurable* quantity, as claimed in the chapter: an observer can read off how hard they are being pushed by watching the colour and timing of light from a fixed companion.

> [!note]- Complete formal solution
> A comoving emitter at Rindler $x_{\mathrm{em}}$ sends a photon of energy $E_{\mathrm{em}}$ toward $\mathcal{O}$ at $x = 0$. There is no relative velocity, so no Doppler shift; the photon four-momentum $P = E_{\mathrm{em}}(e_0^*\pm e_1^*)$ is null and constant in the inertial frame. The reception time, from the Rindler trajectory $ct = \pm a^{-1}\ln[(1+ax)/(1+ax_{\mathrm{em}})]$ at $x=0$, is $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1+ax_{\mathrm{em}})$. Then $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}}) = E_{\mathrm{em}}(\cosh \mp \sinh)(act_{\mathrm{rec}}) = E_{\mathrm{em}}e^{\mp act_{\mathrm{rec}}} = E_{\mathrm{em}}(1+ax_{\mathrm{em}})$, independent of emission time; so $z = 1/(1+ax_{\mathrm{em}}) - 1$, redshift for $x_{\mathrm{em}}<0$ ($z\to\infty$ at the horizon), blueshift for $x_{\mathrm{em}}>0$. In Einstein's elevator, light from the floor ($x_{\mathrm{em}}=-h$) to the ceiling has $z\approx ah = gh/c^2$, identical to the gravitational redshift of light climbing height $h$ in gravity $g = c^2 a$ — the equivalence principle. Finally, combining $1+ax_{\mathrm{em}} = 1/(1+z)$ with the round-trip relation $1+ax_{\mathrm{em}} = e^{\pm acT}$ gives $a = \mp\ln(1+z)/(cT)$: $\mathcal{O}$ measures its own proper acceleration from redshift and light-time alone. $\blacksquare$

---

# Key Takeaways

**Comoving observers see a shift with no Doppler effect — the redshift is the ratio of clock rates.** The decisive conceptual takeaway is that two observers *at rest with respect to each other* can disagree on frequency, even though there is no relative velocity and hence no ordinary Doppler shift. The shift is purely the position-dependence of the clock rate, $\mathrm{d}\tau = (1+ax)\mathrm{d}t$: the emitter's clock ticks at a different rate than the receiver's, and the photon faithfully reports the ratio. The trigger to recognise this elsewhere: whenever light is exchanged between two points held at fixed positions in an accelerated (or gravitational) field, do *not* reach for the Doppler formula — compute the ratio of lapse factors $1 + ax$ at the two points. This is the same factor as the [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|clock desynchronization]], and the redshift is simply that desynchronization read out with light rather than by transporting clocks.

**Transport the four-momentum and dot with $U$ — this computes every shift in relativity.** The reusable computational technique is operation 6: the energy any observer assigns a photon is $E = P\cdot U_{\mathrm{obs}}$, and since a free photon's four-momentum is constant in the inertial frame, the entire shift comes from the change in the receiver's four-velocity between emission and reception. The trigger: any frequency-shift problem — Doppler, gravitational, cosmological — reduces to "write the null $P$, find the two four-velocities, take two dot products, divide". The hyperbolic-function bookkeeping ($\cosh \mp \sinh = e^{\mp(\cdot)}$) is what makes the accelerated-frame case collapse to the clean $1 + ax_{\mathrm{em}}$. This single method unifies the kinematic and gravitational shifts and removes the need to memorise separate formulas.

**The equivalence principle turns the calculation into gravity — position-dependence is the fingerprint of a potential.** The Einstein-elevator reinterpretation is the conceptual payoff: the *identical* calculation that gives the accelerated-frame redshift gives the gravitational redshift, because a uniformly accelerated frame *is* (locally) a uniform gravitational field. The trigger to deploy the equivalence principle as a shortcut: whenever a quantity in an accelerated frame carries the factor $1 + ax$, rewrite it as $1 + \Phi/c^2$ with $\Phi = gx$ the gravitational potential, and read the result as the corresponding gravitational statement — redshift $\Delta\Phi/c^2$, time dilation $1 + \Phi/c^2$. This is why the chapter is the launchpad for general relativity: the Pound–Rebka redshift, the GPS clock corrections, and the gravitational redshift of starlight are all this one formula, and its incompatibility with a flat metric is the [[Special Relativity XXV — Toward Relativistic Gravitation|argument that forces spacetime to curve]].

**The proper acceleration is measurable from redshift and light-time alone.** A quieter but important takeaway from Step 4 is that an observer can determine their own four-acceleration norm $a$ — a frame-independent physical quantity — purely from local optical measurements: the redshift $z$ of light from a fixed companion and the round-trip light time $2T$. The diagnostic this leaves: the four-acceleration is not an abstract bookkeeping device but an operationally accessible quantity, read off as $a = \mp\ln(1+z)/(cT)$. This complements the accelerometer (which measures $a$ directly) and shows the redundancy of relativistic measurements — colour, timing, and force all encode the same $a$. The same logic, applied near a black hole, lets a hovering observer measure the local "surface gravity" from the redshift of light from a companion and the light-travel-time between them.

This exercise applies the [[Thm - Spectral Shift in an Accelerated Frame|spectral-shift theorem]] and pairs with [[Ex - Clock desynchronization and Rindler rigidity]] (the clock-rate side of the same physics) and [[Ex - A free particle in the Rindler frame mimics uniform gravity]] (the equivalence principle for a falling particle).
