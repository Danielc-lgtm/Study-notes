---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Relativistic Doppler Factor"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Thm - Time Dilation (General Observer)"
  - "Def - Photon Propagation Direction and Velocity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature, $u\cdot u = +1$. An emitter $\mathcal{O}'$ (four-velocity $u'$) sends light to a receiver $\mathcal{O}$ (four-velocity $u$); $\mathbf{V}$ is the velocity of the emitter relative to the receiver, in $E_u$, with magnitude $V$ and $\Gamma = (1 - V^2)^{-1/2} = u\cdot u'$ the [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] between them. The unit vector $\mathbf{n} \in E_u$ points from emitter to receiver (so $\mathbf{n}\cdot\mathbf{V} > 0$ for an approaching source — see the convention warning on [[Def - Relativistic Doppler Factor]]). Proper periods and frequencies: $\Delta t'_{\mathrm{em}}, f_{\mathrm{em}} = 1/\Delta t'_{\mathrm{em}}$ for the source; $\Delta t_{\mathrm{rec}}, f_{\mathrm{rec}} = 1/\Delta t_{\mathrm{rec}}$ for the receiver. We assume the receiver $\mathcal{O}$ is inertial (or the worldlines are close enough that curvature is negligible). Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

---

# Statement

> **The Doppler effect.** An observer $\mathcal{O}'$ emitting light at proper-frequency $f_{\mathrm{em}}$ is received by $\mathcal{O}$ at frequency
> $$f_{\mathrm{rec}} = \frac{f_{\mathrm{em}}}{\Gamma\,(1 - \mathbf{n}\cdot\mathbf{V})},$$
> where $\mathbf{V}$ is the source velocity relative to the receiver, $\mathbf{n}$ the unit vector from source to receiver, and $\Gamma = (1 - V^2)^{-1/2}$. Equivalently, the received and emitted periods satisfy $\Delta t_{\mathrm{rec}} = \Gamma(1 - \mathbf{n}\cdot\mathbf{V})\,\Delta t'_{\mathrm{em}}$.

> **Special cases.** For purely radial motion ($\mathbf{V} = V\mathbf{n}$, $V > 0$ for approach), $f_{\mathrm{rec}} = \sqrt{(1+V)/(1-V)}\,f_{\mathrm{em}}$. For purely transverse motion ($\mathbf{n}\cdot\mathbf{V} = 0$), $f_{\mathrm{rec}} = f_{\mathrm{em}}/\Gamma$, a pure redshift — the **transverse Doppler effect**. The non-relativistic limit is the first-order shift $f_{\mathrm{rec}} = (1 + \mathbf{n}\cdot\mathbf{V})f_{\mathrm{em}}$.

---

# Motivation

Everyone has heard the Doppler effect: a passing siren drops in pitch, an approaching train's whistle is sharp and a receding one flat. The question this theorem answers is what relativity changes about that familiar acoustic phenomenon when the waves are light rather than sound, and the answer contains one piece with no classical counterpart.

The classical Doppler effect is entirely geometric: as the source approaches, each successive wave-crest has a shorter distance to travel, so crests arrive more frequently and the pitch rises; as it recedes, the opposite. This gives a shift proportional to the *radial* velocity, vanishing when the source moves purely sideways — a transversely passing siren has, at the moment of closest approach, no shift at all. This first-order, direction-dependent piece survives into relativity essentially unchanged.

What relativity *adds* is the slowing of the moving source's clock. The source emits one wave-crest per tick of *its own* proper time, but the receiver counts crests in *its* time, and the moving source's clock is time-dilated by the [[Thm - Time Dilation (General Observer)|Lorentz factor]] $\Gamma$. So even setting aside the geometric crest-spacing effect, a moving source appears to emit crests more slowly by a factor $\Gamma$ — a redshift that is present for *any* direction of motion, including the transverse direction where the classical effect is exactly zero. This **transverse Doppler effect** is the purely relativistic content of the theorem: a source moving across your line of sight, with no radial velocity at all, is nonetheless redshifted, simply because its clock runs slow. It is a direct, laboratory-accessible manifestation of time dilation, and its measurement by Ives and Stilwell in 1938 was the first experimental confirmation of time dilation. The theorem matters because it packages the familiar classical shift and this new relativistic shift into a single factor, and isolating the $1/\Gamma$ is one of the cleanest tests of special relativity.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "an emitter and a receiver in relative motion, exchanging light". Its disguises:

The first disguised source is **"a spectral line from a moving astronomical object"**. A star, galaxy, or quasar emits at known rest-frame frequencies; its observed frequencies are Doppler-shifted, and inverting the shift gives its radial velocity. The bridge is that the emitting atom is the moving source. *Example problem:* measure the recession velocity of a galaxy from the redshift of its hydrogen lines (the basis of the velocity–distance relation).

The second disguised source is **"a photon's energy change between two observers"**. Because $E = \hbar\omega$, any problem about how a photon's *energy* transforms between frames is a Doppler problem in disguise. The bridge is that the [[Def - The Four-Momentum of a Photon|photon energy]] is $E = P\cdot u$, and the Doppler factor is the ratio of this projection onto the two observers. *Example problem:* the energy shift of a $\gamma$-ray between an emitting and absorbing nucleus in the Mössbauer effect (and its gravitational analogue, Pound–Rebka).

The third disguised source is **"a clock comparison via light signals"**. Whenever two observers compare their clocks by exchanging periodic signals, the rate at which one receives the other's ticks is the Doppler factor. The bridge is that a clock *is* a periodic emitter. *Example problem:* the radar/k-calculus derivation of time dilation, where the two-way signal exchange between observers encodes $\Gamma$ in the product of the approach and recession Doppler factors.

**Targets (Output Amplification)**

The conclusion is the frequency-shift factor $1/[\Gamma(1 - \mathbf{n}\cdot\mathbf{V})]$.

Combine the conclusion with **the transverse limit to isolate $\Gamma$**. Setting $\mathbf{n}\cdot\mathbf{V} = 0$ leaves the pure time-dilation factor $1/\Gamma$. The further result is a direct measurement of time dilation through a frequency shift, free of the (much larger) first-order effect. The combination is nonobvious because the first-order formula predicts *no* transverse shift, so any observed transverse shift is unambiguously relativistic; this is the logic of the Ives–Stilwell experiment.

Combine the conclusion with **the forward/backward product**. For radial motion, the product of the approach and recession factors is $\sqrt{(1+V)/(1-V)}\cdot\sqrt{(1-V)/(1+V)} = 1$, so the *product* of the two shifted frequencies equals $f_0^2$ independently of $V$. The further result is a velocity-independent test of relativity (the modern Reinhardt 2007 experiment, confirmed to $10^{-9}$). The combination is useful because the product is easier to measure precisely than either frequency, since it does not require knowing $V$ accurately.

Combine the conclusion with **relativistic beaming**. The same factor (raised to a power set by the spectral index) multiplies the observed *intensity*, not just the frequency, because both the photon energies and the photon arrival rate are Doppler-boosted. The further result is that an approaching relativistic source is dramatically brightened and a receding one dimmed — the reason one usually sees only the approaching jet of a double-jet source. The combination is useful for understanding the appearance of relativistic astrophysical sources, connecting to [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

---

# Why Is It True

The received period is the emitted period stretched by *two independent factors*, and the theorem is just their product.

**The one-line mechanism: the received period is the emitted period times (the time-dilation factor $\Gamma$, because the source's clock runs slow) times (the classical retardation factor $1 - \mathbf{n}\cdot\mathbf{V}$, because successive crests travel different distances).**

Trace two successive crests. The source emits crest $1$, then waits one proper period $\Delta t'_{\mathrm{em}}$ and emits crest $2$. First factor: that proper period, measured in the *receiver's* coordinate time, is dilated to $\Gamma\,\Delta t'_{\mathrm{em}}$ — the moving clock runs slow, so the coordinate-time gap between the two emissions is longer than the source's own period. This is the [[Thm - Time Dilation (General Observer)|time dilation]], and it is present regardless of direction.

Second factor: between the two emissions the source moves, so crest $2$ is emitted from a *different place* than crest $1$. If the source has moved toward the receiver (component $\mathbf{n}\cdot\mathbf{V} > 0$), crest $2$ has a *shorter* distance to travel and arrives sooner than it otherwise would, compressing the received interval; if the source moves away, crest $2$ is delayed. Quantitatively, in the coordinate time $\Gamma\Delta t'_{\mathrm{em}}$ between emissions the source advances a radial distance $\mathbf{n}\cdot\mathbf{V}\cdot\Gamma\Delta t'_{\mathrm{em}}$, which (light travelling at $1$) reduces the crest-$2$ travel time by that amount. So the received interval is the emission interval minus the saved travel time:
$$\Delta t_{\mathrm{rec}} = \Gamma\Delta t'_{\mathrm{em}} - \mathbf{n}\cdot\mathbf{V}\cdot\Gamma\Delta t'_{\mathrm{em}} = \Gamma(1 - \mathbf{n}\cdot\mathbf{V})\Delta t'_{\mathrm{em}}.$$
Frequencies are reciprocals of periods, giving $f_{\mathrm{rec}} = f_{\mathrm{em}}/[\Gamma(1 - \mathbf{n}\cdot\mathbf{V})]$.

Why is the transverse case a *redshift* and not no-shift? Because when $\mathbf{n}\cdot\mathbf{V} = 0$ the classical factor is $1$ but the time-dilation factor $\Gamma > 1$ remains, so the received period is *longer* than the emitted one — fewer crests per second, lower frequency, redshift. The classical intuition says "no radial velocity, no shift", and it is wrong precisely by the time dilation it ignores. The transverse Doppler effect is time dilation made audible (or visible): you are watching the source's clock tick slow, encoded as a reddening of its light.

---

# What Makes This Hard

The conceptual obstacle is the transverse case — the classical instinct that a sideways-moving source has no Doppler shift is so strong that the surviving $1/\Gamma$ feels like it must be an error; accepting it requires recognising that the source's *clock rate*, not just its position, enters the count. The non-obvious technical subtlety is the *definition of "transverse"*: the transverse Doppler shift depends on whether $\mathbf{n}\cdot\mathbf{V} = 0$ is imposed at the moment of *reception* (in the receiver's frame, giving pure $1/\Gamma$) or at the moment of *emission* (in which case there is also a first-order piece), and conflating the two is a classic source of error. The most common concrete mistake is a sign error in $\mathbf{n}\cdot\mathbf{V}$ — getting a redshift for an approaching source — which is why one should always check the formula against a definitely-approaching source.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Track two successive wave-crests. Compute the coordinate-time interval between their emissions (time dilation of the source clock). Compute the difference in their travel times to the receiver (the geometric retardation from the source's radial motion). The received interval is the emission interval plus the travel-time difference; invert for frequency.

**Subgoal decomposition:**

1. **Time-dilate the emission interval.** Show the coordinate-time gap between two emissions separated by proper period $\Delta t'_{\mathrm{em}}$ is $\Delta t_{\mathrm{em}} = \Gamma\Delta t'_{\mathrm{em}}$.
   - *Hint:* The source's proper time runs slow by $\Gamma$ relative to the receiver's coordinate time — direct [[Thm - Time Dilation (General Observer)|time dilation]].
   - *Why needed:* It is the always-present relativistic factor.

2. **Compute the travel-time difference.** Show the second crest's travel time is shorter by $\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$ than the first's.
   - *Hint:* Between emissions the source advances $\mathbf{V}\Delta t_{\mathrm{em}}$; the radial component $\mathbf{n}\cdot\mathbf{V}\Delta t_{\mathrm{em}}$ shortens the path, and light covers that at speed $1$.
   - *Why needed:* It is the classical directional factor.

3. **Assemble and invert.** Show $\Delta t_{\mathrm{rec}} = \Gamma(1 - \mathbf{n}\cdot\mathbf{V})\Delta t'_{\mathrm{em}}$ and take reciprocals.
   - *Hint:* Received interval = emission interval − saved travel time = $\Delta t_{\mathrm{em}}(1 - \mathbf{n}\cdot\mathbf{V})$.
   - *Why needed:* It gives the frequency formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: Time dilation of the emission interval
> **Statement:** Two crests emitted a proper period $\Delta t'_{\mathrm{em}}$ apart are separated, in the receiver's coordinate time, by $\Delta t_{\mathrm{em}} = \Gamma\Delta t'_{\mathrm{em}}$.
>
> **Hint:** Direct application of time dilation between source and receiver.
>
> **Why needed:** It is the relativistic factor present for all directions, including transverse.
>
> > [!note]- Full proof
> > The two emission events lie on the source's worldline, separated by the source's proper time $\Delta t'_{\mathrm{em}}$. The receiver $\mathcal{O}$ (inertial) assigns to this pair a coordinate-time interval; since the source moves at speed $V$ relative to $\mathcal{O}$, [[Thm - Time Dilation (General Observer)|time dilation]] gives $\Delta t_{\mathrm{em}} = \Gamma\,\Delta t'_{\mathrm{em}}$ with $\Gamma = (1 - V^2)^{-1/2}$. $\blacksquare$

> [!note]- Lemma 2: Retardation from radial motion
> **Statement:** The second crest's light-travel time to $\mathcal{O}$ is shorter than the first's by $\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$ (to first order in the small emission interval).
>
> **Hint:** The source moves between emissions; only the radial component changes the distance.
>
> **Why needed:** It is the classical directional factor.
>
> > [!note]- Full proof
> > Let $r_1, r_2$ be the distances (in $\mathcal{O}$'s rest space) from the two emission points to $\mathcal{O}$. Between emissions the source's displacement is $\mathbf{V}\Delta t_{\mathrm{em}}$, whose component along $\mathbf{n}$ (the source-to-receiver direction) is $\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$. To first order in the small interval, this reduces the distance: $r_2 - r_1 = -\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$. Light travels at speed $1$, so the travel times differ by $r_2 - r_1 = -\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$ (the second crest arrives earlier by $\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$ when the source approaches). $\blacksquare$

> [!note]- Lemma 3: The received interval
> **Statement:** $\Delta t_{\mathrm{rec}} = \Gamma(1 - \mathbf{n}\cdot\mathbf{V})\Delta t'_{\mathrm{em}}$, hence $f_{\mathrm{rec}} = f_{\mathrm{em}}/[\Gamma(1 - \mathbf{n}\cdot\mathbf{V})]$.
>
> **Hint:** Received interval = time between emissions + difference in arrival delays.
>
> **Why needed:** It is the conclusion.
>
> > [!note]- Full proof
> > The first crest is emitted at coordinate time $t_1^{\mathrm{em}}$ and received at $t_1^{\mathrm{rec}} = t_1^{\mathrm{em}} + r_1$; the second at $t_2^{\mathrm{em}} = t_1^{\mathrm{em}} + \Delta t_{\mathrm{em}}$ and received at $t_2^{\mathrm{rec}} = t_2^{\mathrm{em}} + r_2$. Hence
> > $$\Delta t_{\mathrm{rec}} = t_2^{\mathrm{rec}} - t_1^{\mathrm{rec}} = \Delta t_{\mathrm{em}} + (r_2 - r_1) = \Delta t_{\mathrm{em}}(1 - \mathbf{n}\cdot\mathbf{V}),$$
> > using Lemma 2. Substituting $\Delta t_{\mathrm{em}} = \Gamma\Delta t'_{\mathrm{em}}$ (Lemma 1) gives $\Delta t_{\mathrm{rec}} = \Gamma(1 - \mathbf{n}\cdot\mathbf{V})\Delta t'_{\mathrm{em}}$. Taking reciprocals of the periods, $f_{\mathrm{rec}} = f_{\mathrm{em}}/[\Gamma(1 - \mathbf{n}\cdot\mathbf{V})]$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 0 (well-posedness).* Assume the receiver $\mathcal{O}$ is inertial, so its worldline is a straight line and distances $r_1, r_2$ in its rest space are well-defined; if instead the worldlines are curved, assume the emission interval is small enough that the worldlines are locally straight (the formula holds in the limit of vanishing period).
>
> *Step 1 (emission interval, dilated).* Two successive crests are emitted a source-proper-period $\Delta t'_{\mathrm{em}}$ apart. By [[Thm - Time Dilation (General Observer)|time dilation]] (Lemma 1), the receiver assigns coordinate-time separation $\Delta t_{\mathrm{em}} = \Gamma\Delta t'_{\mathrm{em}}$.
>
> *Step 2 (retardation).* The source advances $\mathbf{V}\Delta t_{\mathrm{em}}$ between emissions; the radial component shortens the second crest's path by $\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$ (Lemma 2), so $r_2 - r_1 = -\mathbf{n}\cdot\mathbf{V}\,\Delta t_{\mathrm{em}}$.
>
> *Step 3 (received interval).* With $t_i^{\mathrm{rec}} = t_i^{\mathrm{em}} + r_i$ (light speed $1$),
> $$\Delta t_{\mathrm{rec}} = \Delta t_{\mathrm{em}} + (r_2 - r_1) = \Gamma\Delta t'_{\mathrm{em}}(1 - \mathbf{n}\cdot\mathbf{V}).$$
> Inverting, $f_{\mathrm{rec}} = f_{\mathrm{em}}/[\Gamma(1 - \mathbf{n}\cdot\mathbf{V})]$, the [[Def - Relativistic Doppler Factor|Doppler factor]] times $f_{\mathrm{em}}$.
>
> *Special cases.* Radial ($\mathbf{V} = V\mathbf{n}$): $\Gamma(1-V) = \sqrt{(1-V)/(1+V)}$, so $f_{\mathrm{rec}} = \sqrt{(1+V)/(1-V)}f_{\mathrm{em}}$. Transverse ($\mathbf{n}\cdot\mathbf{V} = 0$): $f_{\mathrm{rec}} = f_{\mathrm{em}}/\Gamma$. Low speed: $\Gamma \approx 1$, $f_{\mathrm{rec}} \approx (1 + \mathbf{n}\cdot\mathbf{V})f_{\mathrm{em}}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Astrophysics — redshift surveys and the velocity–distance relation.** The radial Doppler shift of galaxy spectra, plus the empirical proportionality of recession velocity to distance, is the observational foundation of the expanding universe. The application is nonobvious in that for nearby galaxies the cosmological redshift *reduces* to the kinematic Doppler shift of this theorem, while for distant ones it is a genuinely gravitational effect — a subtle distinction at the boundary of [[Special Relativity XXV — Toward Relativistic Gravitation]].

**Atomic physics — laser cooling and Doppler broadening.** The Doppler shift of an atom's absorption line as it moves toward or away from a laser is exploited to cool atomic gases (Doppler cooling) and limits spectroscopic resolution (Doppler broadening). The application is out-of-distribution because the *first-order* shift here is the workhorse, and the *transverse* (second-order) shift is a systematic to be removed in precision atomic clocks.

**Nuclear physics — the Mössbauer effect and gravitational redshift.** Recoil-free $\gamma$-ray emission (Mössbauer) gives such sharp lines that the tiny Doppler shift from a few mm/s of source motion is resolvable; the same technique measured the *gravitational* redshift in the Pound–Rebka experiment by detecting the frequency shift of $\gamma$-rays falling down a tower. The application is surprising because a kinematic Doppler shift is used as a ruler to measure a gravitational frequency shift, bridging this chapter to [[Special Relativity XXV — Toward Relativistic Gravitation]].

---

# Bridges

- **[[Def - Relativistic Doppler Factor]]** — this theorem *derives* the Doppler factor whose properties that definition page catalogues. The factor $1/[\Gamma(1-\mathbf{n}\cdot\mathbf{V})]$ is the content; the definition page records its radial/transverse limits, its multiplicativity, and its four-vector form $\mathcal{D} = (u'\cdot\ell)/(u\cdot\ell)$.

- **[[Thm - Time Dilation (General Observer)|Time dilation]]** — the transverse Doppler effect *is* time dilation, observed through light. The factor $\Gamma$ in the Doppler formula is exactly the time-dilation factor of the moving source's clock, and the transverse case ($\mathbf{n}\cdot\mathbf{V}=0$) strips away the classical effect to display time dilation directly as a frequency shift.

- **[[Thm - Aberration of Light]]** — Doppler and aberration are two halves of one map: the action of the boost on the photon's null tangent. The same change of observer that shifts the frequency (Doppler) also changes the arrival direction (aberration), and in an oblique geometry the two must be computed together, with $\mathbf{n}\cdot\mathbf{V}$ in the Doppler factor and the aberrated angle in the direction.

- **[[Def - The Four-Momentum of a Photon]]** — because $E = \hbar\omega$, the Doppler shift is the transformation law for a photon's energy, $E_{\mathrm{rec}} = \mathcal{D}E_{\mathrm{em}}$. This is the kinematic input to Compton scattering and inverse-Compton boosting, and it shows that the Doppler effect is the energy-momentum transformation of [[Special Relativity XIII — Energy and Momentum]] specialised to massless quanta.

---

# Unlocked by This

> [!tip] Relativistic Beaming and the One-Sided Jet *(from Astrophysics)*
> The Doppler factor, raised to a power set by the spectral index, multiplies the observed *intensity* of a relativistically moving source — not just its frequency — because both the photon energies and the photon arrival rate are boosted. An approaching jet is brightened by $\mathcal{D}^{3+\alpha}$ and a receding one dimmed by the reciprocal, which is why double-jet sources usually show only the approaching jet: the counter-jet is **Doppler-dimmed** below detection. This connects the kinematic Doppler effect to the observed morphology of active galactic nuclei, taken up with the radiation of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!tip] The Möbius Action on the Celestial Sphere *(from SL(2,C) and Spinors)*
> The Doppler shift and the [[Thm - Aberration of Light|aberration]] of the same ray are the two components of the action of a Lorentz transformation on a null direction; encoding the sky as the Riemann sphere $\mathbb{C}P^1$, this is a **Möbius transformation**, with the Doppler factor the conformal scaling that accompanies the fractional-linear map of the direction — the geometric content of the spinor map of [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].
