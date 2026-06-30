---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Rindler Coordinates and the Accelerated Frame"
  - "Thm - Clock Synchronization and Desynchronization in an Accelerated Frame"
  - "Thm - Worldline of a Uniformly Accelerated Observer"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike vector $X$ has $X\cdot X > 0$ and a photon four-momentum $P$ is null, $P\cdot P = 0$. $\mathcal{O}$ is the fiducial [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] of proper acceleration $a$ at Rindler position $x = 0$, four-velocity $U$, proper time $t$. The emitter $\mathcal{O}'$ is a comoving observer fixed at Rindler position $x_{\mathrm{em}}$, with four-velocity $U'$. The reference inertial observer $\mathcal{O}_*$ has frame $(e_0^*, e_1^*, e_2^*, e_3^*)$ and inertial coordinates $(ct_*, x_*, y_*, z_*)$. The energy an observer with four-velocity $W$ assigns to a photon of four-momentum $P$ is $E = P\cdot W$ (mostly-minus). $E_{\mathrm{em}}, f_{\mathrm{em}}, \lambda_{\mathrm{em}}$ are the emitted energy, frequency, wavelength; $E_{\mathrm{rec}}, f_{\mathrm{rec}}, \lambda_{\mathrm{rec}}$ the received; $z := \lambda_{\mathrm{rec}}/\lambda_{\mathrm{em}} - 1$ is the redshift factor. Full registry on [[Special Relativity XVI — Accelerated Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (§12.4.5) writes the photon energy as $E = -c\,\vec p\cdot\vec u$ in his mostly-plus signature; in our mostly-minus signature this becomes $E = P\cdot U$. The intermediate four-momentum $\vec p = (E_{\mathrm{em}}/c)(\vec e_0^* \pm \vec e_1^*)$ is null in both conventions ($(e_0^*\pm e_1^*)\cdot(e_0^*\pm e_1^*) = 1 - 1 = 0$). The final result $E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$ is signature-independent.

---

# Statement

> **Theorem (spectral shift in an accelerated frame).** Let $\mathcal{O}$ be a uniformly accelerated observer at Rindler position $x = 0$, and let a comoving emitter $\mathcal{O}'$ fixed at Rindler position $x_{\mathrm{em}}$ emit a photon of energy $E_{\mathrm{em}}$ (measured by $\mathcal{O}'$) toward $\mathcal{O}$. The energy received by $\mathcal{O}$ is independent of the emission time and equal to
> $$\boxed{\;E_{\mathrm{rec}} = E_{\mathrm{em}}\,(1 + a x_{\mathrm{em}})\;}$$
> The frequency, period, and wavelength transform by the same factor:
> $$f_{\mathrm{rec}} = f_{\mathrm{em}}(1 + ax_{\mathrm{em}}), \qquad T_{\mathrm{rec}} = \frac{T_{\mathrm{em}}}{1 + ax_{\mathrm{em}}}, \qquad \lambda_{\mathrm{rec}} = \frac{\lambda_{\mathrm{em}}}{1 + ax_{\mathrm{em}}},$$
> giving the redshift factor
> $$z = \frac{1}{1 + a x_{\mathrm{em}}} - 1.$$

> **Corollary (red below, blue above; the equivalence-principle reading).** Emission from "below" the receiver ($x_{\mathrm{em}} < 0$) is redshifted, $z > 0$, with $z \to +\infty$ as $x_{\mathrm{em}} \to -a^{-1}$ (the [[Def - Rindler Horizon|Rindler horizon]]); emission from "above" ($x_{\mathrm{em}} > 0$) is blueshifted, $z < 0$. To first order $z \simeq -ax_{\mathrm{em}}$, which read through the equivalence principle ($g = c^2 a$, $\Phi = gx$) is the **gravitational redshift** $z \simeq \Delta\Phi/c^2$: light climbing out of a potential well loses energy.

---

# Motivation

This theorem answers a question that sounds impossible at first: if two observers are *at rest with respect to each other*, how can the light one sends to the other be shifted in frequency? For inertial observers the answer is that it cannot — two mutually-at-rest inertial observers see each other's clocks and spectral lines unshifted. The accelerated frame breaks this, and the spectral shift is the most directly observable signature of that break.

The result is the operational counterpart of the [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|clock desynchronization]] theorem. There, two comoving clocks were found to tick at different rates, $\mathrm{d}t' = (1+ax_0)\mathrm{d}t$; here, that rate difference is read out *with light*. A photon is a clock — its period is the inverse of its frequency — so a photon emitted by the slow-ticking lower clock and received by the faster-ticking observer arrives with its period stretched, i.e. redshifted. The spectral shift is the desynchronization made visible: you do not need to physically transport clocks and compare them, you just exchange light.

The deepest reason the theorem matters is the bridge it builds to gravity. Einstein's equivalence principle says a uniformly accelerated frame is locally indistinguishable from a uniform gravitational field. This theorem, read through that principle, *is* the gravitational redshift — the prediction that light climbing out of a gravitational potential is shifted toward the red, measured by Pound and Rebka in $1959$. And it carries a structural consequence that special relativity cannot absorb: if clocks at different gravitational potentials genuinely run at different rates, no single flat metric can describe spacetime globally, and the metric must become position-dependent. The accelerated-frame redshift is, historically and logically, the first crack in special relativity that forces general relativity.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a photon is exchanged between two comoving observers in the accelerated frame, with the emitter at known Rindler position $x_{\mathrm{em}}$". The point of input broadening is to recognise the disguises.

The first disguised source is **"light is exchanged between two clocks at different altitudes in a uniform gravitational field"**. By the equivalence principle a static observer at altitude $x_0$ in a uniform field $g = c^2 a$ is a comoving accelerated observer, and the light exchanged between two such observers is governed by this theorem with $ax_{\mathrm{em}} = gx_{\mathrm{em}}/c^2 = \Phi/c^2$. The bridge is the identification of the Rindler potential with the gravitational potential. So any problem about the frequency shift of light rising or falling in a (locally uniform) gravitational field routes through this theorem. *Example problem:* a photon falls a height $h$ in gravity $g$; find its fractional blueshift (answer $gh/c^2$, the [[Ex - Redshift in an accelerated frame and the Einstein elevator|Pound–Rebka]] result).

The second disguised source is **"a photon's four-momentum is parallel-transported along a null geodesic and its energy compared at two events"**. The energy any observer assigns a photon is $E = P\cdot W$ for that observer's four-velocity $W$; if $P$ is the same (parallel-transported) four-vector at emission and reception, the energy ratio is determined entirely by the two four-velocities. The bridge is that in flat spacetime a free photon's four-momentum is constant in the inertial frame, so the shift comes only from the receiver's changing four-velocity. So any redshift computation reduces to "dot the conserved $P$ with the receiver's $U$". *Example problem:* compute the Doppler shift between two inertial observers as the same dot-product calculation.

The third disguised source is **"two events on the worldlines of two comoving observers are connected by a light ray, and their proper-time rates are known"**. Because frequency is inverse period and period is a proper-time interval, the frequency ratio is the inverse of the proper-time ratio between successive wavecrests. The bridge is the desynchronization relation $\mathrm{d}t' = (1+ax_0)\mathrm{d}t$: the ratio of clock rates *is* the spectral shift. So any problem that has already computed the comoving clock rates gives the redshift for free. *Example problem:* having found $\mathrm{d}t' = (1+ax_{\mathrm{em}})\mathrm{d}t$, read off $z = 1/(1+ax_{\mathrm{em}}) - 1$ with no further photon calculation.

**Targets (Output Amplification)**

The conclusion is $E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$, equivalently $z = 1/(1+ax_{\mathrm{em}}) - 1$.

Combine the conclusion with **a measurement of the round-trip light time**. If $\mathcal{O}$ also measures the round-trip time $2T$ of a photon between $x = 0$ and $x_{\mathrm{em}}$, then combining with the rigid-ruler relation $\ell_0 = a^{-1}|e^{\pm acT} - 1|$ eliminates $x_{\mathrm{em}}$ and yields the proper acceleration purely from $\mathcal{O}$'s own measurements: $a = \mp\ln(1+z)/(cT)$. The further result is that the proper acceleration is *measurable* by an observer who only watches redshifts and light-travel-times — they need no external reference. The combination is nonobvious because $a$ is a property of the worldline's curvature, yet it is extracted from spectroscopy and timing alone.

Combine the conclusion with **the limit $x_{\mathrm{em}} \to -a^{-1}$**. As the emitter approaches the horizon, $1 + ax_{\mathrm{em}} \to 0$ and $z \to +\infty$: the received light is shifted infinitely far to the red, its energy going to zero. The further result is the *infinite redshift surface* — the hallmark of a horizon, and the flat-spacetime template for the infinite redshift at a black-hole event horizon. The combination is useful because it shows a horizon is not a place where light is blocked but a place where light arrives infinitely reddened.

Combine the first-order form $z \simeq -ax_{\mathrm{em}}$ with **the equivalence principle**. Writing $ax_{\mathrm{em}} = \Phi/c^2$ converts the kinematic redshift into the gravitational redshift $z \simeq \Delta\Phi/c^2$. The further result, combined with the demand that the redshift be a real, frame-independent physical effect, is the *incompatibility of the gravitational redshift with a flat metric* — the argument that forces spacetime curvature. The combination is the conceptual payoff of the chapter: a spectral-shift formula becomes the first evidence for general relativity.

---

# Why Is It True

The deep reason is that **a photon carries its own clock — its period — and that clock is compared against the receiver's clock, which runs at a different rate than the emitter's because the two sit at different distances from the common centre $A$.**

Start from the cleanest possible accounting. A photon of frequency $f_{\mathrm{em}}$ is a train of wavecrests separated by one period $T_{\mathrm{em}} = 1/f_{\mathrm{em}}$ of the emitter's proper time. Two successive crests are emitted at two events on $\mathcal{O}'$'s worldline, separated by $\mathrm{d}t' = T_{\mathrm{em}}$. Because $\mathcal{O}$ is *stationary* (all events on its worldline are equivalent), the photon's flight takes the same coordinate-time interval $\mathrm{d}t$ for each crest, so the two crests arrive at $\mathcal{O}$ separated by the *same* coordinate interval $\mathrm{d}t$ that separated their emissions. The crucial point is the conversion to proper time at each end: at the emitter $\mathrm{d}t' = (1 + ax_{\mathrm{em}})\mathrm{d}t$, while at the receiver $x = 0$ so $\mathrm{d}t_{\mathrm{rec}} = (1 + a\cdot 0)\mathrm{d}t = \mathrm{d}t$. The received period is therefore $T_{\mathrm{rec}} = \mathrm{d}t = \mathrm{d}t'/(1 + ax_{\mathrm{em}}) = T_{\mathrm{em}}/(1 + ax_{\mathrm{em}})$, and the frequency ratio inverts: $f_{\mathrm{rec}} = f_{\mathrm{em}}(1 + ax_{\mathrm{em}})$.

**The one-line mechanism: the photon's two wavecrests are separated by a fixed coordinate-time interval (because the observer is stationary), but the emitter and receiver convert that coordinate interval to proper time with different lapse factors $1 + ax$ — and the ratio of those lapses is the entire spectral shift.** This is why the redshift is the same number as the clock desynchronization: both are the ratio of lapse functions $(1 + ax_{\mathrm{em}})/(1 + a\cdot 0) = 1 + ax_{\mathrm{em}}$.

There is a complementary energy-based way to see it that makes no reference to crests. The photon's four-momentum $P$ is a fixed null four-vector in the inertial frame (a free photon does not change its momentum). The emitter measures $E_{\mathrm{em}} = P\cdot U'$, the receiver $E_{\mathrm{rec}} = P\cdot U$, with $U', U$ the two four-velocities. Since $\mathcal{O}$ and $\mathcal{O}'$ are stationary, one may compute both dot products at the symmetric instant where their frames align with $\mathcal{O}_*$; the receiver's four-velocity has "rotated" (boosted) relative to the emitter's by exactly the amount the worldline geometry dictates between the two positions, and that boost is what multiplies the energy by $1 + ax_{\mathrm{em}}$. The two derivations — crest-counting and energy dot-product — are the same fact seen as time and as energy, related by $E = hf$.

Why "red below, blue above"? An emitter below the receiver ($x_{\mathrm{em}} < 0$) is nearer the centre $A$, hence on a more sharply curved hyperbola, hence its clock ticks *slower* ($1 + ax_{\mathrm{em}} < 1$); its slow ticks make a low-frequency, redshifted signal. Light "climbs up" out of the strongly-accelerated region and loses frequency, exactly as light climbing out of a gravitational well loses energy.

---

# What Makes This Hard

The algebra is short; the place people stumble is keeping straight *which* observer's proper time and *which* four-velocity enter at each end, and not double-counting. The non-obvious step is recognising that the photon's coordinate flight-time is the *same* for two successive crests — this uses the stationarity of the observer ($\dot a = 0$) and is what makes the result independent of emission time. The most common error is to apply a naive special-relativistic Doppler formula with some "relative velocity" between the emitter and receiver: but they have *zero* relative velocity (they are comoving), so the ordinary Doppler effect gives no shift, and one must instead use the lapse-ratio. A second common error is a sign slip that swaps red and blue; the safe check is that the emitter *nearer the horizon* (more negative $x_{\mathrm{em}}$) is always redshifted.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the photon's four-momentum as a fixed null vector in the inertial frame, find the reception event from the Rindler photon-trajectory equation, and compute the received energy as $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}})$; the reception time drops out, leaving $E_{\mathrm{rec}} = E_{\mathrm{em}}(1+ax_{\mathrm{em}})$.

**Subgoal decomposition:**

1. **Write the photon four-momentum.** A photon emitted by $\mathcal{O}'$ (at rest in the instantaneous inertial frame at emission) with energy $E_{\mathrm{em}}$ has $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$, the $+$ sign for emission from below ($x_{\mathrm{em}} \le 0$, rightward propagation).
   - *Hint:* A photon four-momentum is $E$ times (unit time + unit propagation direction); it is null since $(e_0^*\pm e_1^*)\cdot(e_0^*\pm e_1^*) = 0$.
   - *Why needed:* $P$ is the conserved quantity transported to the reception event.

2. **Find the reception time.** The photon trajectory in Rindler coordinates is $ct = \pm a^{-1}\ln[(1+ax)/(1+ax_{\mathrm{em}})]$; at the receiver $x = 0$ this gives $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1+ax_{\mathrm{em}})$.
   - *Hint:* Set $b = x_{\mathrm{em}}$ and $x = 0$ in the Rindler photon-trajectory equation.
   - *Why needed:* It supplies $t_{\mathrm{rec}}$, needed for the receiver's four-velocity.

3. **Compute the received energy.** With $U(t_{\mathrm{rec}}) = \cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*$, form $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}}) = E_{\mathrm{em}}[\cosh(act_{\mathrm{rec}}) \mp \sinh(act_{\mathrm{rec}})] = E_{\mathrm{em}}e^{\mp act_{\mathrm{rec}}}$.
   - *Hint:* $(e_0^*\pm e_1^*)\cdot(\cosh\,e_0^* + \sinh\,e_1^*) = \cosh \mp \sinh = e^{\mp(\cdot)}$ in mostly-minus.
   - *Why needed:* It expresses $E_{\mathrm{rec}}$ in terms of $t_{\mathrm{rec}}$.

4. **Eliminate the reception time.** Substitute $act_{\mathrm{rec}} = \mp\ln(1+ax_{\mathrm{em}})$ so that $e^{\mp act_{\mathrm{rec}}} = 1 + ax_{\mathrm{em}}$, giving $E_{\mathrm{rec}} = E_{\mathrm{em}}(1+ax_{\mathrm{em}})$.
   - *Hint:* $e^{\mp act_{\mathrm{rec}}} = e^{\ln(1+ax_{\mathrm{em}})} = 1 + ax_{\mathrm{em}}$.
   - *Why needed:* It is the final, time-independent result; frequency, period, wavelength, and $z$ follow.

---

# Lemma Decomposition

> [!note]- Lemma 1: The photon four-momentum is $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$
> **Statement:** A photon emitted by the comoving observer $\mathcal{O}'$ at $x_{\mathrm{em}}$ with energy $E_{\mathrm{em}}$ has four-momentum $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$, with $+$ for $x_{\mathrm{em}} \le 0$ and $-$ for $x_{\mathrm{em}} \ge 0$.
>
> **Hint:** At emission $\mathcal{O}'$ is at rest in the instantaneous inertial frame $\mathcal{O}_*$ (chosen tangent at $t=0$), so $U'(0) = e_0^*$; the photon energy is $E_{\mathrm{em}} = P\cdot U'(0)$.
>
> **Why needed:** It is the conserved null four-vector that is transported to the reception event.
>
> > [!note]- Full proof
> > By the stationarity of $\mathcal{O}$ and $\mathcal{O}'$, take the emission to occur at $t = 0$, where the comoving emitter's four-velocity is $U'(0) = \cosh(0)e_0^* + \sinh(0)e_1^* = e_0^*$ (from [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame|Lemma 3]], $U' = \cosh(act)e_0^* + \sinh(act)e_1^*$, evaluated at $t=0$). A photon four-momentum is null and future-directed; propagating in the plane $\Pi$ it has the form $P = E_{\mathrm{em}}(e_0^* + \sigma e_1^*)$ with $\sigma = \pm 1$ the propagation direction. Indeed $P\cdot P = E_{\mathrm{em}}^2(1 - \sigma^2) = 0$, and $E_{\mathrm{em}} = P\cdot U'(0) = E_{\mathrm{em}}(e_0^* + \sigma e_1^*)\cdot e_0^* = E_{\mathrm{em}}$, consistent. For the photon to travel from the emitter (at $x_{\mathrm{em}}$) toward the receiver (at $x = 0$): if $x_{\mathrm{em}} \le 0$ the photon must move in the $+x_*$ direction, so $\sigma = +1$; if $x_{\mathrm{em}} \ge 0$ it moves in $-x_*$, so $\sigma = -1$. Hence $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$. $\blacksquare$

> [!note]- Lemma 2: The reception time is $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1 + ax_{\mathrm{em}})$
> **Statement:** A photon emitted at $(t, x) = (0, x_{\mathrm{em}})$ reaches $\mathcal{O}$ (at $x = 0$) at proper time $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1 + ax_{\mathrm{em}})$, sign $\mp = -\mathrm{sgn}(x_{\mathrm{em}})$.
>
> **Hint:** Null geodesics in the inertial plane are $ct_* = \pm(x_* - b)$; transforming to Rindler coordinates gives $ct = \pm a^{-1}\ln[(1+ax)/(1+ab)]$.
>
> **Why needed:** It supplies the reception event at which the receiver's four-velocity is evaluated.
>
> > [!note]- Full proof
> > A photon worldline in the inertial plane $\Pi$ is a straight $45^\circ$ line $ct_* = \sigma(x_* - b)$ ($\sigma = \pm 1$), where $b$ is its $x_*$-intercept at $t_* = 0$; for emission from $x_{\mathrm{em}}$ at $t = 0$, $b = x_{\mathrm{em}}$. Substituting the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler transformation]] $ct_* = (x+a^{-1})\sinh(act)$, $x_* = (x+a^{-1})\cosh(act) - a^{-1}$:
> > $$(x + a^{-1})\sinh(act) = \sigma\big[(x+a^{-1})\cosh(act) - a^{-1} - b\big].$$
> > Using $\cosh u = \tfrac12(e^u + e^{-u})$, $\sinh u = \tfrac12(e^u - e^{-u})$ and solving for $act$ gives
> > $$ct = \sigma\,a^{-1}\ln\!\left(\frac{1 + ax}{1 + ab}\right).$$
> > At the receiver $x = 0$ with $b = x_{\mathrm{em}}$: $ct_{\mathrm{rec}} = \sigma a^{-1}\ln[1/(1+ax_{\mathrm{em}})] = -\sigma a^{-1}\ln(1 + ax_{\mathrm{em}})$. With $\sigma = +1$ for $x_{\mathrm{em}} \le 0$ and $\sigma = -1$ for $x_{\mathrm{em}} \ge 0$, this is $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1+ax_{\mathrm{em}})$ with $\mp = -\mathrm{sgn}(x_{\mathrm{em}})$. $\blacksquare$

> [!note]- Lemma 3: The received energy is $E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$
> **Statement:** $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}}) = E_{\mathrm{em}}e^{\mp act_{\mathrm{rec}}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}})$.
>
> **Hint:** Dot the conserved $P$ with $U(t_{\mathrm{rec}}) = \cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*$, then substitute Lemma 2.
>
> **Why needed:** It is the theorem; the frequency and redshift formulas follow by $E = hf$ and $\lambda = c/f$.
>
> > [!note]- Full proof
> > The four-momentum $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$ (Lemma 1) is constant in the inertial frame (a free photon). The energy $\mathcal{O}$ assigns at reception is $E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}})$ with $\mathcal{O}$'s four-velocity $U(t_{\mathrm{rec}}) = \cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*$. In mostly-minus,
> > $$E_{\mathrm{rec}} = E_{\mathrm{em}}(e_0^* \pm e_1^*)\cdot[\cosh(act_{\mathrm{rec}})e_0^* + \sinh(act_{\mathrm{rec}})e_1^*] = E_{\mathrm{em}}[\cosh(act_{\mathrm{rec}}) \mp \sinh(act_{\mathrm{rec}})] = E_{\mathrm{em}}\,e^{\mp act_{\mathrm{rec}}},$$
> > using $e_0^*\cdot e_0^* = 1$, $e_1^*\cdot e_1^* = -1$, $e_0^*\cdot e_1^* = 0$, and $\cosh u \mp \sinh u = e^{\mp u}$. By Lemma 2, $\mp act_{\mathrm{rec}} = \ln(1 + ax_{\mathrm{em}})$, so $e^{\mp act_{\mathrm{rec}}} = 1 + ax_{\mathrm{em}}$ and
> > $$E_{\mathrm{rec}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}}). \qquad \blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Let the comoving emitter $\mathcal{O}'$ at Rindler position $x_{\mathrm{em}}$ emit a photon of energy $E_{\mathrm{em}}$ toward $\mathcal{O}$ (at $x = 0$). By stationarity, take emission at $t = 0$.
>
> By **Lemma 1**, the photon four-momentum is the null vector $P = E_{\mathrm{em}}(e_0^* \pm e_1^*)$, with $\pm = -\mathrm{sgn}(x_{\mathrm{em}})$ chosen so the photon travels toward the receiver; $P$ is constant in the inertial frame.
>
> By **Lemma 2**, the photon reaches $\mathcal{O}$ at proper time $ct_{\mathrm{rec}} = \mp a^{-1}\ln(1+ax_{\mathrm{em}})$, obtained from the Rindler photon-trajectory equation $ct = \pm a^{-1}\ln[(1+ax)/(1+ax_{\mathrm{em}})]$ at $x = 0$.
>
> By **Lemma 3**, the received energy is
> $$E_{\mathrm{rec}} = P\cdot U(t_{\mathrm{rec}}) = E_{\mathrm{em}}\,e^{\mp act_{\mathrm{rec}}} = E_{\mathrm{em}}(1 + ax_{\mathrm{em}}),$$
> independent of $t_{\mathrm{rec}}$ (consistent with stationarity). By the Planck–Einstein relation $E = hf$ the frequencies obey $f_{\mathrm{rec}} = f_{\mathrm{em}}(1 + ax_{\mathrm{em}})$, hence $T_{\mathrm{rec}} = T_{\mathrm{em}}/(1+ax_{\mathrm{em}})$ and (since $\lambda = cT$) $\lambda_{\mathrm{rec}} = \lambda_{\mathrm{em}}/(1+ax_{\mathrm{em}})$. The redshift factor is
> $$z = \frac{\lambda_{\mathrm{rec}}}{\lambda_{\mathrm{em}}} - 1 = \frac{1}{1 + ax_{\mathrm{em}}} - 1.$$
> For $x_{\mathrm{em}} < 0$ (emitter below): $z > 0$, redshift, $z\to+\infty$ as $x_{\mathrm{em}}\to -a^{-1}$. For $x_{\mathrm{em}} > 0$: $z < 0$, blueshift. To first order $z \simeq -ax_{\mathrm{em}}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Pound–Rebka experiment (experimental gravitation).** A $14.4\,\mathrm{keV}$ gamma-ray from $^{57}\mathrm{Fe}$ rises or falls a tower of height $h = 22.5\,\mathrm{m}$; the predicted fractional shift $gh/c^2 \approx 2.5\times 10^{-15}$ matches the theorem with $ax_{\mathrm{em}} = gh/c^2$. The application is the canonical first test of the equivalence principle, and it requires the Mössbauer effect to make the gamma-ray linewidth narrow enough to resolve the tiny shift. It is nonobvious because the same formula derived for a rocket in deep space predicts a laboratory result governed by Earth's gravity.

**Cosmological redshift and the expanding universe (cosmology).** Although the cosmological redshift is governed by the scale factor rather than a static potential, the structural idea — a photon's wavelength stretched by the ratio of "clock rates" at emission and reception — is the same, and the Rindler redshift is the simplest exactly-soluble model of a photon's frequency changing between two observers in relative geometric configuration. The application is surprising because the static accelerated frame and the dynamic expanding universe share the "ratio of lapses" mechanism.

**Gravitational redshift of starlight and white-dwarf spectra (astrophysics).** Light leaving the surface of a compact star climbs out of a deep gravitational potential and is redshifted by $z \simeq GM/(Rc^2)$; for the white dwarf Sirius B this was an early confirmation of general relativity. Modelling the near-surface region by a Rindler frame with $a = GM/R^2$ recovers the leading-order shift. The application battle-tests the source by mapping "Rindler position" to "radial coordinate" and "$a^{-1}$" to the near-surface scale height.

---

# Bridges

- **[[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame]]** — the spectral shift and the clock desynchronization are the same physics in two guises. The frequency ratio $f_{\mathrm{rec}}/f_{\mathrm{em}} = 1 + ax_{\mathrm{em}}$ is exactly the inverse of the proper-time ratio $\mathrm{d}t'/\mathrm{d}t = 1 + ax_{\mathrm{em}}$ for the comoving emitter, because a photon's period is a proper-time interval and frequency is its inverse. One theorem compares clocks by transporting them; the other compares them with light. The shared factor $1 + ax_{\mathrm{em}}$ — the ratio of the lapse function at emitter and receiver — is the single quantity governing both.

- **[[Def - The Four-Momentum of a Photon]]** — the whole calculation rests on the photon four-momentum being a fixed null vector $P$ in the inertial frame, with the energy any observer assigns given by $E = P\cdot U_{\mathrm{obs}}$. The redshift is then purely the change in this dot product as the receiver's four-velocity rotates relative to the emitter's. This is the operation "transport $P$, dot with $U$" that computes every Doppler and gravitational shift in relativity.

- **Gravitational redshift and the Schwarzschild metric** — read through the equivalence principle, $z \simeq -ax_{\mathrm{em}} = -\Phi/c^2$ is the leading term of the exact Schwarzschild gravitational redshift $1 + z = (1 - 2GM/rc^2)^{-1/2}$ for light climbing out of the field of a mass $M$. The Rindler factor $1 + ax$ is the flat-spacetime stand-in for the Schwarzschild lapse $\sqrt{1 - 2GM/rc^2}$, and the infinite redshift at $x_{\mathrm{em}} = -a^{-1}$ is the stand-in for the infinite redshift at the event horizon $r = 2GM/c^2$, developed in [[General Relativity I — Einstein's Equations and Schwarzschild]].

- **The incompatibility argument and spacetime curvature** — the deepest bridge is destructive: this theorem shows that two mutually-at-rest observers see each other's spectral lines shifted, which means their clocks run at different rates, which means *no single inertial frame* can cover the region. In flat spacetime the effect is an artifact of the chosen accelerated frame; but if a *real* gravitational field produces a *real* redshift (Pound–Rebka), then the metric $g_{\mu\nu}(x)$ must genuinely vary from place to place, and spacetime must be curved. The accelerated-frame redshift is the seed of [[Special Relativity XXV — Toward Relativistic Gravitation|the argument that forces general relativity]].

---

# Unlocked by This

> [!tip] The Gravitational Redshift and the Failure of Flat Spacetime *(from General Relativity)*
> Read through Einstein's **equivalence principle** — that physics in a uniformly accelerated frame is locally identical to physics in a uniform gravitational field — the first-order formula $z \simeq -ax_{\mathrm{em}}$ *is* the **gravitational redshift**: a photon falling a height $h$ in gravity $g$ is blueshifted by $gh/c^2$, and one climbing out is redshifted. This is the effect measured by **Pound and Rebka**. The decisive consequence is that the gravitational redshift is *incompatible with a flat Minkowski metric*: if clocks at different gravitational potentials genuinely tick at different rates — and the redshift says they do — then the metric $g_{\mu\nu}(x)$ must vary from place to place, no global inertial frame can exist, and spacetime must be curved. The accelerated-frame redshift is the first crack in special relativity that forces **general relativity**, taken up in [[Special Relativity XXV — Toward Relativistic Gravitation]] and [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] The Unruh Temperature and Horizon Thermodynamics *(from quantum field theory in curved spacetime)*
> The infinite redshift as $x_{\mathrm{em}} \to -a^{-1}$ — light from the [[Def - Rindler Horizon|Rindler horizon]] arrives with zero energy — is the classical skeleton of the **Unruh effect**. When a quantum field is described in the accelerated frame, the horizon's infinite redshift, together with the tracing-out of modes hidden behind it, turns the Minkowski vacuum into a thermal state at the **Unruh temperature** $T = \hbar a/(2\pi c k_B)$. The same infinite-redshift surface, promoted to a black-hole event horizon, makes the hole radiate at the **Hawking temperature**. The spectral shift of this page is the classical limit in which the horizon's role as an infinite-redshift surface first appears.
