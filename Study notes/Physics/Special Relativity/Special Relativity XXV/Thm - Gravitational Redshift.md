---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$. $\Phi$ is the gravitational potential; $\vec g = -\gamma\,\vec e_x$ a uniform field of magnitude $\gamma > 0$ ($\gamma$ a field strength, *not* the Lorentz factor); $x_{\mathrm{em}}$ the altitude (abscissa) of the emitter $\mathcal{O}'$ in the frame of the receiver $\mathcal{O}$ at the origin. $\Delta t'$ is the proper period of the emitted periodic signal, $\Delta t$ that of the received signal. $\nu = 1/\Delta t$ is frequency; $\Delta\nu/\nu$ the fractional shift (redshift if negative). $\vec a = (\gamma/c^2)\vec e_x$ is the proper acceleration the equivalence principle assigns. For experiments: $g = 9.8\ \mathrm{m\,s^{-2}}$ surface gravity, $h$ a height difference, $M_\oplus$, $R_\oplus$ Earth's mass and radius. Full registry on [[Special Relativity XXV — Toward Relativistic Gravitation]].

---

# Statement

> **Gravitational redshift.** Let two observers $\mathcal{O}$ and $\mathcal{O}'$ be mutually at rest at altitudes $0$ and $x_{\mathrm{em}}$ in a uniform gravitational field $\vec g = -\gamma\vec e_x$. If $\mathcal{O}'$ emits a periodic signal of proper period $\Delta t'$, then $\mathcal{O}$ receives it with proper period
> $$\Delta t = \frac{\Delta t'}{1 + \gamma\,x_{\mathrm{em}}/c^2}.$$
> Equivalently, for a small height difference $h$ in a field of magnitude $g$, the fractional frequency shift of a signal travelling *upward* is
> $$\frac{\Delta\nu}{\nu} = -\frac{\Delta\Phi}{c^2} = -\frac{g\,h}{c^2} \;<\; 0 \quad(\text{a redshift}),$$
> where $\Delta\Phi = gh > 0$ is the gain in gravitational potential. A clock deeper in the potential runs slow relative to one higher up.

> **Corollary (general static field).** Between two static observers at potentials $\Phi_{\mathrm{em}}$ and $\Phi_{\mathrm{rec}}$, the received and emitted frequencies satisfy $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 - (\Phi_{\mathrm{rec}} - \Phi_{\mathrm{em}})/c^2$ to first order, which is the linearisation of the exact general-relativistic redshift $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = \sqrt{g_{00}(\mathrm{em})/g_{00}(\mathrm{rec})}$.

---

# Motivation

The equivalence principle is a statement about the *equivalence* of gravity and acceleration; on its own it is a principle, not a number. The gravitational redshift is its first quantitative, measurable consequence — the prediction that turns the principle into physics one can test on a laboratory tower. It answers a concrete question: if two clocks sit at different heights in a gravitational field, do they tick at the same rate? Newtonian physics says yes, trivially; the equivalence principle says no, and gives the exact discrepancy.

The result matters for three reasons. First, it is the cleanest experimental verification of the equivalence principle, confirmed from the Pound-Rebka tower experiment to the GPS constellation. Second, it is the lever in [[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity|Schild's argument]] that pries spacetime loose from flatness: a redshift in a static field is incompatible with a time-translation-invariant metric, so the existence of the redshift *forces* the metric to become position-dependent. Third, it is of genuine practical importance — satellite navigation simply does not work without correcting for it, the only everyday technology for which the relativistic character of gravity must be taken into account.

One should expect such an effect from the accelerated-frame picture. Put two observers in a rocket accelerating "upward", the lower one emitting light to the upper one. During the light's transit the upper observer accelerates away from the oncoming signal, so by the ordinary Doppler effect he receives a *lower* frequency — a redshift. This has nothing to do with gravity; it is pure special-relativistic kinematics in an accelerated frame. The equivalence principle then says the same must happen in a gravitational field, with the rocket's acceleration replaced by the local gravity. The motivation for the precise formula is just to do this Doppler bookkeeping carefully, which the accelerated-observer chapter has already done.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "two static observers at different potentials in a gravitational field". The disguises:

The first disguised source is **"a clock and a higher clock, anywhere in a static field"** — not necessarily uniform. For a general static potential $\Phi(\vec r)$ the formula generalises to $\Delta\nu/\nu = -\Delta\Phi/c^2$ with $\Delta\Phi$ the potential difference, so the theorem applies to any pair of fixed observers in any static field, including the Earth's $1/r$ field. The bridge is that the uniform-field result, integrated along the path, gives the potential-difference form. *Example problem:* find the rate difference between a clock on the ground and a clock on a mountain of height $h$ (use $\Delta\Phi = gh$).

The second disguised source is **"an accelerated observer emitting to another"** — pure special relativity, no gravity. By the equivalence principle the accelerated-frame spectral shift *is* the gravitational redshift, so any accelerated-emission problem is a redshift problem in disguise. The bridge is the equivalence principle itself. *Example problem:* compute the frequency shift between the nose and tail of a uniformly accelerating rocket, and recognise it as the redshift for an equivalent field.

The third disguised source is **"energy conservation for a photon climbing a potential"**. A photon of energy $E = h\nu$ has effective mass $E/c^2$ (by [[Thm - Mass-Energy Equivalence|mass-energy equivalence]]), so climbing a height $h$ it does work $(E/c^2)gh$ against gravity and loses energy, hence frequency. The bridge is that energy conservation forces $\Delta\nu/\nu = -gh/c^2$, recovering the redshift from thermodynamics alone (Einstein's original 1911 argument). *Example problem:* derive the redshift by demanding that a mass-to-photon-to-mass cycle conserves energy.

**Targets (Output Amplification)**

The conclusion is "$\Delta t = \Delta t'/(1+\gamma x_{\mathrm{em}}/c^2)$, a redshift upward".

Combine the conclusion with **a static field's time-translation symmetry**. This is Schild's argument: the redshift plus staticity contradicts the Minkowski metric. The further result is that the metric must be a position-dependent field — the founding step of general relativity ([[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity]]). The combination is the single most consequential use of the redshift, turning a measured shift into a structural revolution.

Combine the conclusion with **a strong field near a compact object**. For the Schwarzschild metric the exact redshift is $\nu_\infty/\nu_{\mathrm{em}} = \sqrt{1 - 2GM/(rc^2)}$, of which the weak-field formula is the linearisation. The further result is that as $r \to 2GM/c^2$ the redshift diverges — light from a black-hole horizon is infinitely redshifted, which is *why* black holes are black. The combination extrapolates the laboratory effect to its dramatic strong-field limit. *Example:* the redshift of light emitted just outside a Schwarzschild horizon.

Combine the conclusion with **a precise frequency standard and a known height**. Inverting the formula, a measured redshift between two atomic clocks *determines* their potential difference, hence their height difference, to centimetre precision. The further result is chronometric levelling — clocks as altimeters — now an operational tool in geodesy. The combination is useful because it runs the theorem backward: measure the shift, infer the field.

---

# Why Is It True

The cleanest derivation is the accelerated-frame Doppler argument, and it makes the result inevitable.

Replace the gravitational field by the equivalent acceleration: by the equivalence principle, two observers at rest in the uniform field $\vec g = -\gamma\vec e_x$ behave exactly like two observers in a rocket with proper acceleration $a = \gamma/c^2$, the lower one at $x = 0$ and the upper at $x = x_{\mathrm{em}}$. Now follow a light signal from the lower (emitter $\mathcal{O}'$, say — though here let the higher one receive) to the higher observer. The signal takes a time $\approx x_{\mathrm{em}}/c$ to climb. During that time the receiver, accelerating "upward" at $a$, picks up an extra velocity $\Delta v \approx a\,(x_{\mathrm{em}}/c) = a\,x_{\mathrm{em}}/c$ directed *away* from the oncoming light. By the ordinary first-order Doppler effect, a receiver moving away at $\Delta v$ sees the frequency reduced by a factor $(1 - \Delta v/c) = (1 - a\,x_{\mathrm{em}}/c^2) = (1 - \gamma x_{\mathrm{em}}/c^2)$. A signal climbing the potential is thus redshifted by exactly the factor the theorem states (to first order).

**The mechanism is one line: while the light climbs, the receiver accelerates away from it, so it arrives Doppler-redshifted — and by the equivalence principle that acceleration is gravity.** The redshift is not a property of light, or of clocks, in isolation; it is the Doppler shift of an accelerated receiver, reinterpreted by the equivalence principle as a gravitational effect. The factor $\gamma x_{\mathrm{em}}/c^2 = \Delta\Phi/c^2$ is the product (acceleration)$\times$(distance)/(speed)$^2$ = (velocity gained during transit)/(speed), which is just the Doppler parameter.

There is a second, independent way to see it that does not even mention acceleration: energy conservation. A photon of frequency $\nu$ carries energy $h\nu$, hence (by $E = mc^2$) effective gravitational mass $h\nu/c^2$. Climbing a height $h$ against gravity $g$, it must do work $(h\nu/c^2)gh$, and this energy can only come from the photon itself, so its energy drops by that amount: $h\,\Delta\nu = -(h\nu/c^2)gh$, giving $\Delta\nu/\nu = -gh/c^2$. That the two utterly different arguments — accelerated-frame Doppler and photon energy conservation — give the identical answer is a sign that the result is robust and forced, not an artifact of either picture.

The deeper meaning, which only emerges once one accepts the result, is that the redshift is really a statement about *clocks*, not light. The reason the received frequency is lower is that the emitting clock, deep in the potential, *runs slow*: it produces fewer crests per second of the receiver's time. Light merely carries the news of the clock rates between the two locations. This is why the redshift is the seed of the metric-as-field idea — it says proper time itself depends on position.

---

# What Makes This Hard

The conceptual difficulty is keeping straight *which way* is the redshift: a signal going *up* (out of the well) is redshifted, going *down* is blueshifted, and the sign of $x_{\mathrm{em}}$ in the formula must be tracked against the direction of travel. The common error is to confuse the gravitational redshift with the special-relativistic Doppler or transverse-Doppler shifts that may be present simultaneously (as in the GPS and Vessot-Levine analyses, where the kinematic time dilation and the gravitational redshift have *opposite* signs and must be carefully separated). The non-obvious physical point is that the effect is a statement about clock rates and proper time, not about photons losing energy "to gravity" as if gravity were a medium — the energy-conservation derivation is a heuristic, and the true content is that the metric measuring proper time depends on altitude.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the equivalence principle to convert the uniform field into a uniform acceleration $a = \gamma/c^2$, then either (a) quote the accelerated-observer period relation from [[Special Relativity XVI — Accelerated Observers|XVI]], or (b) do the first-order Doppler bookkeeping: the receiver gains velocity $a\,x_{\mathrm{em}}/c$ away from the signal during its transit, redshifting it by $(1 - a x_{\mathrm{em}}/c^2)$.

**Subgoal decomposition:**

1. **Convert field to acceleration.** By the equivalence principle, observers at rest in $\vec g = -\gamma\vec e_x$ are uniformly accelerated with $a = \gamma/c^2$.
   - *Hint:* The Newtonian-limit identification is field strength $=$ proper acceleration.
   - *Why needed:* It moves the problem into flat-spacetime accelerated-observer kinematics, which the reader already knows.

2. **Compute the transit-time velocity gain.** The light takes $\approx x_{\mathrm{em}}/c$ to climb; the receiver gains $\Delta v = a\,x_{\mathrm{em}}/c$.
   - *Hint:* $\Delta v = a\,\Delta t_{\mathrm{transit}}$ with $\Delta t_{\mathrm{transit}} = x_{\mathrm{em}}/c$.
   - *Why needed:* This velocity is the Doppler parameter.

3. **Apply the first-order Doppler shift.** A receiver moving away at $\Delta v$ sees frequency reduced by $(1 - \Delta v/c) = (1 - \gamma x_{\mathrm{em}}/c^2)$.
   - *Hint:* $\Delta\nu/\nu = -\Delta v/c$ for recession.
   - *Why needed:* It yields the period relation $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2)$ and the redshift $\Delta\nu/\nu = -\Delta\Phi/c^2$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Equivalence-principle conversion of field to acceleration
> **Statement:** Observers at rest in the uniform field $\vec g = -\gamma\vec e_x$ are physically equivalent to uniformly accelerated observers with proper acceleration $\vec a = (\gamma/c^2)\vec e_x$.
>
> **Hint:** The equivalence principle plus the Newtonian-limit identification of $|\vec g|$ with proper acceleration.
>
> **Why needed:** It transfers the problem to the accelerated-observer kinematics of [[Special Relativity XVI — Accelerated Observers|XVI]].
>
> > [!note]- Full proof
> > The equivalence principle states that an inertial observer at rest in a uniform gravitational field is, for all local physical measurements, equivalent to a uniformly accelerated observer in flat spacetime. Quantitatively, an observer held at rest in the field $\vec g = -\gamma\vec e_x$ must be supported by a force producing an upward proper acceleration that exactly opposes the field; in the Newtonian limit this proper acceleration has magnitude $\gamma$, so in geometric units $\vec a = (\gamma/c^2)\vec e_x$. (This is the same identification by which a person standing on Earth has proper acceleration $g = 9.8\ \mathrm{m\,s^{-2}}$ directed upward.) Thus the two observers $\mathcal{O}$, $\mathcal{O}'$ at altitudes $0$, $x_{\mathrm{em}}$ are uniformly accelerated observers with this $\vec a$. $\blacksquare$

> [!note]- Lemma 2: The accelerated-receiver Doppler shift
> **Statement:** When light climbs from $x = 0$ to $x = x_{\mathrm{em}}$ between two observers of common proper acceleration $a$, the receiver gains velocity $\Delta v = a\,x_{\mathrm{em}}/c$ away from the signal, so the received frequency is reduced by the factor $(1 - a x_{\mathrm{em}}/c^2)$.
>
> **Hint:** Transit time $x_{\mathrm{em}}/c$; velocity gain $a\times$ transit time; first-order Doppler $\Delta\nu/\nu = -\Delta v/c$.
>
> **Why needed:** It is the quantitative redshift, equivalent to the exact accelerated-frame period relation to first order.
>
> > [!note]- Full proof
> > The light signal travels the distance $x_{\mathrm{em}}$ from $\mathcal{O}'$ (here taken as the lower emitter) to $\mathcal{O}$ in coordinate time $\Delta t_{\mathrm{transit}} \approx x_{\mathrm{em}}/c$. During this interval the receiver, with proper acceleration $a$ directed along $+\vec e_x$ (away from the oncoming light if the light climbs), increases its velocity by $\Delta v = a\,\Delta t_{\mathrm{transit}} = a\,x_{\mathrm{em}}/c$, directed away from the source. By the first-order [[Special Relativity VIII — Kinematics II, Change of Observer|Doppler effect]] for a receiver receding at speed $\Delta v$, the observed frequency is reduced:
> > $$\frac{\nu_{\mathrm{rec}}}{\nu_{\mathrm{em}}} = 1 - \frac{\Delta v}{c} = 1 - \frac{a\,x_{\mathrm{em}}}{c^2} = 1 - \frac{\gamma x_{\mathrm{em}}}{c^2}.$$
> > Equivalently the periods satisfy $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2)$ (the exact accelerated-frame result, of which this is the first-order expansion), and with $\gamma x_{\mathrm{em}} = \Delta\Phi$ the fractional shift is $\Delta\nu/\nu = -\Delta\Phi/c^2$, a redshift for the upward-climbing signal. $\blacksquare$

> [!note]- Lemma 3: Energy-conservation cross-check
> **Statement:** Treating a photon as having gravitational mass $h\nu/c^2$, energy conservation as it climbs a height $h$ in field $g$ gives the same redshift $\Delta\nu/\nu = -gh/c^2$.
>
> **Hint:** Work done against gravity $= (h\nu/c^2)gh$ comes from the photon's energy $h\nu$.
>
> **Why needed:** An independent derivation confirming the result is forced, not an artifact of the accelerated-frame picture.
>
> > [!note]- Full proof
> > A photon of frequency $\nu$ has energy $E = h\nu$ and, by [[Thm - Mass-Energy Equivalence|mass-energy equivalence]], effective gravitational mass $m = E/c^2 = h\nu/c^2$. Climbing a height $h$ in a uniform field of magnitude $g$, it does work $W = mgh = (h\nu/c^2)gh$ against gravity. By energy conservation this work is paid for by a loss of the photon's own energy, $\Delta E = h\,\Delta\nu = -W$, so
> > $$h\,\Delta\nu = -\frac{h\nu}{c^2}gh \quad\Longrightarrow\quad \frac{\Delta\nu}{\nu} = -\frac{gh}{c^2} = -\frac{\Delta\Phi}{c^2}.$$
> > This matches Lemma 2 exactly. (This is the heuristic; the rigorous content is that proper time depends on altitude, but energy conservation gives the right number.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Two observers $\mathcal{O}$ and $\mathcal{O}'$ are mutually at rest at altitudes $0$ and $x_{\mathrm{em}}$ in a uniform gravitational field $\vec g = -\gamma\vec e_x$, $\gamma > 0$.
>
> **By Lemma 1**, the equivalence principle makes them uniformly accelerated observers with proper acceleration $\vec a = (\gamma/c^2)\vec e_x$.
>
> **By the accelerated-observer kinematics of [[Special Relativity XVI — Accelerated Observers|XVI]]** (Lemma 2), the proper period $\Delta t'$ of a signal emitted at the abscissa $x_{\mathrm{em}}$ and the proper period $\Delta t$ at which it is received at the origin are related by
> $$\Delta t = \frac{\Delta t'}{1 + \gamma x_{\mathrm{em}}/c^2}.$$
> Writing $\gamma x_{\mathrm{em}} = \Delta\Phi$ (the potential difference) and expanding for $\Delta\Phi/c^2 \ll 1$,
> $$\frac{\Delta\nu}{\nu} = \frac{\Delta t' - \Delta t}{\Delta t} \approx -\frac{\Delta\Phi}{c^2} = -\frac{gh}{c^2},$$
> a redshift for a signal travelling upward ($x_{\mathrm{em}} > 0$, $\Delta\Phi > 0$) and a blueshift downward.
>
> **By Lemma 3**, the same result follows from photon energy conservation, confirming it is independent of the derivation route.
>
> For a general static field with potential $\Phi(\vec r)$, integrating the infinitesimal relation along the path gives $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 - (\Phi_{\mathrm{rec}} - \Phi_{\mathrm{em}})/c^2$ to first order, the linearisation of the exact general-relativistic redshift $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = \sqrt{g_{00}(\mathrm{em})/g_{00}(\mathrm{rec})}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nuclear physics — the Mössbauer effect as the enabling technology.** The Pound-Rebka experiment needed a frequency standard sharp enough to resolve $\Delta\nu/\nu \sim 10^{-15}$ over $22\,\mathrm{m}$. The ${}^{57}\mathrm{Fe}$ gamma line ($14\,\mathrm{keV}$) is broadened by recoil and thermal Doppler — except when the emitting nucleus is locked in a crystal lattice, the **Mössbauer effect**, which makes the whole lattice recoil and gives a line sharp enough to measure the shift. The application links a relativity test to solid-state nuclear physics. See [[Thm - Mass-Energy Equivalence]].

**Aerospace engineering — the GPS clock correction.** GPS satellites orbit at $r_{\mathrm{sat}} = 2.65\times 10^4\,\mathrm{km}$. Their clocks run *fast* by gravitational redshift ($+5.3\times 10^{-10}$, being higher in the potential) and *slow* by kinematic time dilation ($-8.3\times 10^{-11}$, moving at $3.87\,\mathrm{km\,s^{-1}}$); the net is $+4.5\times 10^{-10}$, and if uncorrected the timing drifts $46\,\mu\mathrm{s}/\mathrm{day}$, giving a $14\,\mathrm{km}$ position error. The exercise is to compute both effects and their sum. This is the one everyday technology that fails without relativity.

**Astrophysics — the redshift of light from a white dwarf or neutron star.** A photon leaving the surface of a compact star climbs out of a deep potential well and is redshifted by $\Delta\nu/\nu = -GM/(Rc^2)$; for Sirius B this is measurable and confirms the mass-radius relation, and for a neutron star ($GM/Rc^2 \sim 0.2$) the full Schwarzschild formula is needed. The application uses the redshift as a probe of stellar structure. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity]]** — this redshift is the *premise* of the capstone theorem. The capstone takes the redshift in a static field and shows it is incompatible with the time-translation-invariant Minkowski metric, forcing the metric to become a position-dependent field. The redshift is the measurable fact; the capstone is the structural consequence. Without the redshift there is no argument that spacetime must curve.

- **[[Def - Uniformly Accelerated Observer (Hyperbolic Motion)]]** and **[[Def - Rindler Coordinates and the Accelerated Frame]]** — the redshift is computed entirely from the accelerated-observer kinematics of [[Special Relativity XVI — Accelerated Observers|XVI]]. The spectral shift between Rindler observers — a pure special-relativistic effect, no gravity — becomes the gravitational redshift by the equivalence principle. The accelerated frame is where the formula is derived; the gravitational field is where it is applied.

- **[[Thm - Mass-Energy Equivalence]]** — the energy-conservation derivation rests on the photon's gravitational mass $h\nu/c^2$, which is mass-energy equivalence applied to light. Einstein's original 1911 derivation of the redshift used exactly this, deriving a spacetime effect from the prohibition of a gravitational perpetual-motion machine.

- **The Schwarzschild redshift in general relativity** — the weak-field formula $\Delta\nu/\nu = -\Delta\Phi/c^2$ is the linearisation of the exact result $\nu_\infty/\nu_{\mathrm{em}} = \sqrt{1 - 2GM/(rc^2)}$ in the Schwarzschild metric of [[General Relativity I — Einstein's Equations and Schwarzschild]]. The general-relativistic redshift is the metric component $\sqrt{g_{00}}$ directly: proper time is $d\tau = \sqrt{g_{00}}\,dt$, so clocks at different $g_{00}$ tick at different rates, and the redshift *is* the ratio of $\sqrt{g_{00}}$ at the two locations. This is the precise sense in which the redshift measures the metric.

---

# Unlocked by This

> [!tip] Chronometric Levelling and Relativistic Geodesy *(from Metrology)*
> Inverting the redshift turns clocks into altimeters: since $\Delta\nu/\nu = -\Delta\Phi/c^2$, comparing the rates of two optical atomic clocks measures their gravitational potential difference, hence (in a known field) their height difference, to centimetre precision. This **chronometric levelling** is now an operational geodetic technique, and a global network of optical clocks defines a relativistic geoid. The redshift, once a delicate test of principle, has become a survey instrument.

> [!tip] The Schwarzschild Horizon and Infinite Redshift *(from General Relativity)*
> Extrapolated to a strong field, the redshift $\nu_\infty/\nu_{\mathrm{em}} = \sqrt{1 - 2GM/(rc^2)}$ diverges as the emitter approaches the **Schwarzschild radius** $r_s = 2GM/c^2$: light emitted at the horizon arrives infinitely redshifted, with zero frequency and zero energy. This is the precise statement that **a black hole is black** — no signal from the horizon can reach a distant observer at finite frequency. The flat-space redshift of this chapter is the gentle laboratory shadow of this dramatic horizon physics; see [[General Relativity I — Einstein's Equations and Schwarzschild]].
