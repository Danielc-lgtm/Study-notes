---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Impossibility of Global Clock Synchronization on a Rotating Disk"
  - "Def - Uniformly Rotating Observer"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A corotating observer $\mathcal{O}'$ at radius $r$ on a disk of angular velocity $\omega$ emits, at event $A$, a prograde signal $\mathscr{S}_+$ (with the rotation) and a retrograde signal $\mathscr{S}_-$ (against it); they return to $\mathcal{O}'$ at events $B_+$ and $B_-$, with $\mathcal{O}'$-proper times $t'_+$ and $t'_-$. Each travels the same closed path $\mathscr{C}$ in $\mathcal{O}$'s reference space. The common signal speed relative to corotating observers is $v$ (equal to $c$ for light); $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$, $\Gamma_{(0)}$ its value at the emitter; $\vec{\mathcal{A}}$ the area vector of the enclosed surface; $A = \|\vec{\mathcal{A}}\|$. The inertial angular velocities of the two signals are $\Omega_+ > 0$, $\Omega_- < 0$. Full registry on [[Special Relativity XVII — Rotating Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 13) uses $\mathrm{diag}(-1,+1,+1,+1)$. The Sagnac delay $\Delta t'$ is a positive scalar (the prograde signal always arrives later), independent of signature; the velocity-composition law and the circulation integral are carried over unchanged.

---

# Statement

> **The Sagnac effect.** A [[Def - Uniformly Rotating Observer|corotating observer]] $\mathcal{O}'$ emits at one event two signals travelling the same closed path $\mathscr{C}$ in opposite senses — prograde $\mathscr{S}_+$ (with the rotation) and retrograde $\mathscr{S}_-$ — with the *same* speed $v$ relative to corotating observers. After one circuit they return to $\mathcal{O}'$ at different proper times, separated by the **Sagnac delay**
> $$\Delta t' := t'_+ - t'_- = \frac{2}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\,\vec V\cdot d\vec\ell \;=\; 2\,\Delta t'_{\text{desync}} \;>\; 0,$$
> twice the [[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk|clock-desynchronization gap]], always positive (the prograde signal arrives later). For a circular path of radius $r$,
> $$\Delta t' = \frac{4\pi\Gamma\, r^2\omega}{c^2};$$
> for small velocities ($r\omega\ll c$),
> $$\Delta t' \simeq \frac{4}{c^2}\,\vec\omega\cdot\vec{\mathcal{A}} = \frac{4\omega A}{c^2}.$$
> The delay is **independent of the signal speed $v$** — identical for light, electrons, neutrons, or atoms — because the $c^2$ originates in the Minkowski metric, not in the propagation speed. The *proper travel times* of the two signals are equal, $T_+ = T_-$; only the arrival times dated by the emitter differ.

---

# Motivation

Send a pulse of light clockwise around a closed loop on a spinning platform, and another counter-clockwise, both starting from the same point at the same instant. In a non-rotating frame they would return together — same path length, same speed, same travel time. On a rotating platform they do *not* return together: the one going with the rotation arrives later than the one going against it, by a definite, measurable interval. This is the Sagnac effect, discovered by Georges Sagnac in 1913, and it is the most consequential single fact about rotating frames — the working principle of every ring-laser and fibre-optic gyroscope guiding aircraft, ships, and missiles today.

The effect is striking for what it does *not* depend on. It does not depend on the nature of the signal: light, electrons, neutrons, whole atoms all show the same delay (given the same path and the same speed relative to the disk). It does not depend on the speed of the signal: a slow signal and a fast signal traversing the same loop suffer the same Sagnac delay. And — the deepest point — the $c^2$ that appears in the formula is *not* the speed of the signal; it is the conversion factor between time and space in the Minkowski metric. The Sagnac delay is a statement about the geometry of spacetime as seen by a rotating observer, not about how anything propagates.

The cleanest way to understand it is that the Sagnac delay is exactly *twice the clock-desynchronization gap* of the previous theorem. Synchronizing clocks around the loop fails to close by $\Delta t'_{\text{desync}}$; a prograde signal picks up this gap with one sign and a retrograde signal with the opposite sign, so their arrival times differ by $2\Delta t'_{\text{desync}}$. The impossibility of global synchronization and the Sagnac effect are the same fact, the former phrased as a clock offset and the latter as an arrival-time difference. This is why the Sagnac delay is also $\propto\omega A/c^2$: it is the same circulation of the rotating congruence's velocity around the loop.

A subtle and important counterpoint: the *proper travel times* of the two signals — how long each takes by its own reckoning along the path — are *equal*. It is only the *arrival times as dated by the emitting observer* that differ, because the emitter's notion of simultaneity is the one that fails to close around the loop. The asymmetry is not in the journeys but in the bookkeeping of when they end.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever two signals are sent in opposite senses around a closed loop on a rotating system — and that hypothesis appears in many guises.

The first disguised source is **"a light beam split and recombined on a rotating table"**. The optical Sagnac interferometer splits a beam, sends the halves around a loop in opposite senses, and recombines them; the phase shift of the resulting fringes is $2\pi f$ times the Sagnac delay. The bridge is that the two beams are prograde and retrograde signals with $v = c$. *Example problem:* compute the fringe shift in Sagnac's original $0.0866\,\text{m}^2$ interferometer rotating at $2$ Hz.

The second disguised source is **"counter-propagating modes in a ring-laser cavity"**. A ring laser supports clockwise and counter-clockwise lasing modes; rotation makes their resonant frequencies differ, and the beat frequency measures $\omega$. The bridge is that the two cavity modes are the prograde and retrograde signals, and the Sagnac delay becomes a frequency split. *Example problem:* find the beat frequency of a square ring-laser gyroscope of side $L$ rotating at $\omega$.

The third disguised source is **"matter waves in an atom or neutron interferometer"**. Splitting a coherent matter wave and sending the parts around a loop in opposite senses produces a Sagnac phase, used as an ultra-sensitive rotation sensor. The bridge is that the matter wave is a signal with $v$ the particle speed (or phase velocity), and the speed-independence of the delay means the same $\propto\omega A$ formula applies. *Example problem:* compute the rotation sensitivity of a cold-atom Sagnac interferometer ([[Thm - Sagnac Delay and the Optical Sagnac Interferometer]]).

**Targets (Output Amplification)**

The conclusion is $\Delta t' = 2\Delta t'_{\text{desync}} = 4\omega A/c^2$ (small velocity).

Combine the conclusion with **the wave frequency** $f$. Multiplying by $2\pi f$ converts the delay to an interferometer phase shift $\Delta\phi = 2\pi f\,\Delta t' = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}}$. The combination is the bridge from the kinematic delay to the observable fringe pattern, and it is nonobvious that the phase depends on the *frequency*, not the wavelength and phase velocity separately — a distinction that matters for matter waves. *Example:* the Sagnac interferometer.

Combine the conclusion with **the number of loops $N$**. Winding the path $N$ times (a fibre coil) multiplies the enclosed area, hence the delay and phase, by $N$. The combination yields the design principle of the fibre-optic gyroscope: sensitivity is bought by adding fibre length. It is nonobvious only in that the enhancement is exactly linear in the number of turns. *Example:* a fibre-optic gyrometer with a several-kilometre coil.

Combine the conclusion with **the Earth's rotation $\omega_\oplus$**. The platform need not rotate relative to the lab; the Earth's own rotation suffices, given a large enough enclosed area. The combination is the basis of the Michelson–Gale–Pearson measurement and of ring-laser arrays that monitor the Earth's rotation rate. It is nonobvious that a table-fixed interferometer detects rotation at all, until one realizes the lab itself corotates with the Earth. *Example:* the $613\times339$ m Michelson–Gale interferometer.

---

# Why Is It True

The honest one-line reason is the link to synchronization: **the Sagnac delay is twice the amount by which clocks fail to synchronize around the loop.**

Here is the mechanism in full. Imagine trying to assign a consistent time to every point of the loop, synchronizing neighbour to neighbour. By the previous theorem this fails: going once around, your time disagrees with itself by $\Delta t'_{\text{desync}}$. Now consider the two signals. A prograde signal, travelling with the rotation, effectively "chases" the synchronization gap and arrives at the emitter at a time shifted by $+\Delta t'_{\text{desync}}$ relative to the would-be consistent time; a retrograde signal, travelling against the rotation, arrives shifted by $-\Delta t'_{\text{desync}}$. The difference of their arrival times is the sum of the magnitudes, $2\Delta t'_{\text{desync}}$. The two signals are a physical probe of the synchronization gap, and because they sample it with opposite signs, they double it.

A complementary picture, in the inertial frame, makes the asymmetry concrete. In the inertial frame both signals travel at the same speed (or the same speed relative to the disk, composed with the rim motion), but the *target* — the emitter — is moving. The prograde signal must chase the emitter, which has moved forward along the circle by the time the signal comes around, so it travels a slightly longer path and takes longer. The retrograde signal meets the emitter coming the other way, so it travels a slightly shorter path and arrives sooner. The path-length difference is $2\times$ (rim speed) $\times$ (travel time) $\sim 2r\omega\times(2\pi r/c)$, which works out to the Sagnac delay $4\pi r^2\omega/c^2$. The prograde signal is delayed because it chases a receding target; the retrograde signal is advanced because it meets an approaching one.

Two features deserve emphasis. First, the delay is **independent of the signal speed**: in the synchronization picture the gap $\Delta t'_{\text{desync}}$ is a property of the rotating frame's geometry, not of the signals, so any signal samples the same gap. The $c^2$ in $4\omega A/c^2$ is the metric factor in $\Delta t'_{\text{desync}}$, never a propagation speed — which is why one must *not* replace it by the particle's phase velocity for matter waves. Second, the **proper travel times are equal**, $T_+ = T_-$: each signal, by its own reckoning along the path, takes the same time, because the path and the speed relative to the disk are the same in both senses. The asymmetry lives entirely in the emitter's dating of the *arrival*, which is exactly where the non-closing simultaneity does its work.

---

# What Makes This Hard

The conceptual trap is thinking the Sagnac delay is about light, or about propagation speed — it is neither; it is the doubled synchronization gap, and the $c^2$ is metric, not kinematic, so the delay is the same for any signal at any speed. A second trap is expecting the two signals' *travel* times to differ; they do not (the proper travel times are equal), and the difference is purely in the emitter's dating of arrival. The non-obvious step in the clean derivation is recognizing that the prograde and retrograde signals sample the desynchronization gap with opposite signs, so that the arrival-time difference is $2\Delta t'_{\text{desync}}$ rather than $\Delta t'_{\text{desync}}$. The most common error is to attribute the effect to a difference in path length or speed in the rotating frame, missing that in the rotating frame both signals see the same path and speed and the effect is entirely in the (non-closing) simultaneity.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Two routes. (A) Synchronization route: each signal's return time, by the clock-transport formula of the previous section, equals the proper travel time (equal for both) plus $\pm\Delta t'_{\text{desync}}$; differencing gives $\Delta t' = 2\Delta t'_{\text{desync}}$. (B) Direct route (circular path): write the two signal worldlines as helices with inertial angular velocities $\Omega_\pm$, solve $\Omega_\pm t_{B_\pm} = \omega t_{B_\pm} \pm 2\pi$ for the return times, convert to $\mathcal{O}'$-proper time via $\Delta t' = \Gamma^{-1}(t_{B_+} - t_{B_-})$, and supply $\Omega_\pm$ from the relativistic velocity-composition law with the common signal speed $v$.

**Subgoal decomposition:**

1. **Equate the proper travel times.** Show $T_+ = T_-$ for the two signals (same path, same speed relative to corotating observers).
   - *Hint:* The proper travel time integrates $\Gamma\sqrt{1 - (r^2\omega^2/c^2)\sin^2\theta}\,d\ell/v$, which is independent of the sense of traversal.
   - *Why needed:* It isolates the entire effect into the arrival-time dating.

2. **Relate each return time to the synchronization gap.** Show $t'_\pm = T_\pm \pm \Delta t'_{\text{desync}}$ (with the desynchronization carried with opposite signs for the two senses).
   - *Hint:* The arrival event's date in the emitter's frame is the proper travel time plus the central-time gap accumulated around the loop, which is $\pm\Delta t'_{\text{desync}}$.
   - *Why needed:* It produces the delay as $\Delta t' = 2\Delta t'_{\text{desync}}$.

3. **Evaluate the circulation for a circular path.** Show $\Delta t' = 4\pi\Gamma r^2\omega/c^2$ at constant radius and $\frac{4}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$ for small velocities.
   - *Hint:* Double the constant-radius desynchronization $\pm 2\pi\Gamma r^2\omega/c^2$; for small velocities double the Stokes form $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$.
   - *Why needed:* It gives the explicit closed-form delay.

4. **(Direct check) Recover $\Delta t'$ from velocity composition.** Write $\Omega_\pm$ via $r\Omega_+ = (v + r\omega)/(1 + r\omega v/c^2)$, solve for $t_{B_\pm}$, and confirm the same $\Delta t'$.
   - *Hint:* $t_{B_+} = 2\pi/(\Omega_+ - \omega)$, $t_{B_-} = 2\pi/(\omega - \Omega_-)$; use $1 - r^2\omega^2/c^2 = \Gamma^{-2}$ and $v_+ = v_-$.
   - *Why needed:* It verifies the result independently and exhibits the speed-independence.

---

# Lemma Decomposition

> [!note]- Lemma 1: The proper travel times are equal
> **Statement:** The proper times $T_+$ and $T_-$ elapsed along the two signals between emission and return satisfy $T_+ = T_-$.
>
> **Hint:** Both signals traverse the same path $\mathscr{C}$ at the same speed $v$ relative to corotating observers; the proper-travel-time integral does not depend on the sense of traversal.
>
> **Why needed:** It shows the Sagnac delay is *not* a difference in travel time, but lies entirely in the arrival dating.
>
> > [!note]- Full proof
> > The proper time elapsed for a signal of speed $v$ relative to corotating observers, traversing the path, is $T_\pm = \frac{1}{v}\oint_{\mathscr{C}}\Gamma\sqrt{1 - (r^2\omega^2/c^2)\sin^2\theta}\,d\ell$, where $\theta$ is the angle between the path element and the rotation velocity. Since the integrand depends only on the geometry of $\mathscr{C}$ and the constant speed $v$ — not on the direction of travel — the integral is the same for both senses. Hence $T_+ = T_-$. (If $v\to c$, both vanish, as for light.) $\blacksquare$

> [!note]- Lemma 2: Each return time carries the desynchronization gap with opposite sign
> **Statement:** $t'_\pm = T_\pm \pm \Delta t'_{\text{desync}}$, so $\Delta t' = t'_+ - t'_- = 2\Delta t'_{\text{desync}}$.
>
> **Hint:** The total elapsed time measured by the central inertial observer between emission and return is the proper travel time (Lorentz-dilated) plus the synchronization gap accumulated around the loop, which is $+\Delta t'_{\text{desync}}$ for prograde and $-\Delta t'_{\text{desync}}$ for retrograde.
>
> **Why needed:** It is the heart of the theorem — the delay is twice the synchronization gap.
>
> > [!note]- Full proof
> > Following an observer who carries the signal once around the loop, the elapsed time measured by the central inertial observer is $dt = \Gamma\,dt'_{\text{signal}} + dt_{\text{sync}}$, where the first term is the dilated proper travel time and $dt_{\text{sync}} = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ is the synchronization increment (from the previous theorem). Integrating around the loop and converting to the emitter's proper time, the return time is $t'_\pm = T_\pm + \frac{1}{\Gamma_{(0)}}\oint_{\mathscr{C}}\frac{\Gamma^2\vec V\cdot d\vec\ell^\pm}{c^2}$, where $d\vec\ell^\pm$ is oriented in the sense of the signal. Since $d\vec\ell^- = -d\vec\ell^+$, the synchronization terms are $\pm\Delta t'_{\text{desync}}$, and with $T_+ = T_-$ (Lemma 1), $\Delta t' = t'_+ - t'_- = 2\Delta t'_{\text{desync}}$. $\blacksquare$

> [!note]- Lemma 3: The circular-path and small-velocity forms
> **Statement:** For a circular path, $\Delta t' = 4\pi\Gamma r^2\omega/c^2$; for small velocities, $\Delta t' \simeq \frac{4}{c^2}\vec\omega\cdot\vec{\mathcal{A}} = 4\omega A/c^2$.
>
> **Hint:** Double the corresponding desynchronization formulas from the previous theorem.
>
> **Why needed:** It gives the explicit closed-form delay used by experimenters.
>
> > [!note]- Full proof
> > By Lemma 2, $\Delta t' = 2\Delta t'_{\text{desync}}$. At constant radius, $\Delta t'_{\text{desync}} = 2\pi\Gamma r^2\omega/c^2$, so $\Delta t' = 4\pi\Gamma r^2\omega/c^2$. For small velocities, $\Delta t'_{\text{desync}} \simeq \frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$, so $\Delta t' \simeq \frac{4}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$. For a circle the enclosed area vector has magnitude $A = \pi r^2$ and is along $\vec\omega$, so $\vec\omega\cdot\vec{\mathcal{A}} = \omega\pi r^2$ and $\Delta t' = 4\omega\pi r^2/c^2$, consistent with the circular form at $\Gamma\to 1$. $\blacksquare$

> [!note]- Lemma 4: Independent derivation via velocity composition (circular path)
> **Statement:** Writing the signal worldlines as helices with inertial angular velocities $\Omega_\pm$ and using the [[Thm - Relativistic Velocity Addition|velocity-composition law]] $r\Omega_+ = (v + r\omega)/(1 + r\omega v/c^2)$ recovers $\Delta t' = 4\pi\Gamma r^2\omega/c^2$.
>
> **Hint:** The signal returns to $\mathcal{O}'$ when it has gained (prograde) or lost (retrograde) one full turn on the emitter: $\Omega_\pm t_{B_\pm} = \omega t_{B_\pm} \pm 2\pi$.
>
> **Why needed:** It verifies the result without invoking the synchronization gap and shows the speed-independence directly.
>
> > [!note]- Full proof
> > The prograde signal's worldline is $x_*(t) = r\cos\Omega_+ t$, $y_*(t) = r\sin\Omega_+ t$, $\Omega_+ > 0$; it meets the emitter (at angular position $\omega t$) when $\Omega_+ t_{B_+} = \omega t_{B_+} + 2\pi$, giving $t_{B_+} = 2\pi/(\Omega_+ - \omega)$. Similarly $t_{B_-} = 2\pi/(\omega - \Omega_-)$ with $\Omega_- < 0$. The emitter's proper-time delay is $\Delta t' = \Gamma^{-1}(t_{B_+} - t_{B_-}) = \frac{2\pi}{\Gamma}\big(\frac{1}{\Omega_+ - \omega} + \frac{1}{\Omega_- - \omega}\big)$. The velocity-composition law gives $r\Omega_+ = (v + r\omega)/(1 + r\omega v/c^2)$, hence $\Omega_+ - \omega = \Gamma^{-2}(1 + r\omega v/c^2)^{-1}v/r$, and similarly for $\Omega_- - \omega$ with $v\to -v$. Substituting and using $v_+ = v_- = v$, the $1/v$ terms cancel and $\Delta t' = 2\pi\Gamma r(2r\omega/c^2) = 4\pi\Gamma r^2\omega/c^2$. The signal speed $v$ has dropped out entirely. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 0 — equal proper travel times.* By Lemma 1, both signals, traversing the same closed path $\mathscr{C}$ at the same speed $v$ relative to corotating observers, have equal proper travel times $T_+ = T_-$. The Sagnac delay is therefore not a travel-time difference but lies in the arrival dating.
>
> *Delay as twice the synchronization gap.* By Lemma 2, the return time of each signal, as dated by the emitting observer $\mathcal{O}'$, is the proper travel time plus the synchronization gap accumulated around the loop, carried with opposite signs for the two senses: $t'_\pm = T_\pm \pm \Delta t'_{\text{desync}}$. Hence
> $$\Delta t' = t'_+ - t'_- = 2\Delta t'_{\text{desync}} = \frac{2}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell,$$
> which is positive (the prograde signal arrives later).
>
> *Explicit forms.* By Lemma 3, for a circular path $\Delta t' = 4\pi\Gamma r^2\omega/c^2$, and for small velocities $\Delta t' \simeq \frac{4}{c^2}\vec\omega\cdot\vec{\mathcal{A}} = 4\omega A/c^2$.
>
> *Independent verification.* By Lemma 4, writing the signal worldlines as helices and applying the relativistic velocity-composition law recovers $\Delta t' = 4\pi\Gamma r^2\omega/c^2$ without reference to the synchronization gap, and exhibits explicitly that the signal speed $v$ cancels, so the delay is independent of $v$.
>
> *Independence of signal speed and metric origin of $c^2$.* Since the delay equals $2\Delta t'_{\text{desync}}$, a property of the rotating frame's geometry, it is the same for any signal; the $c^2$ in $4\omega A/c^2$ comes from the Minkowski metric (via $\Delta t'_{\text{desync}}$), not from the propagation speed. In the Newtonian limit $c\to\infty$, $\Delta t'\to 0$: there is no Sagnac effect in Newtonian physics. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Ring-laser detection of Earth's rotation and geophysics.** Large ring-laser gyroscopes (such as the Wettzell "G" ring) measure the Earth's rotation rate $\omega_\oplus$ via the Sagnac frequency split with such precision that they detect length-of-day variations, polar motion, and even seismic rotational ground motion. The application is out-of-distribution because a special-relativistic rotating-frame effect becomes a tool of geodesy and seismology.

**Cold-atom interferometers and tests of the equivalence principle.** Atom-interferometric Sagnac sensors, exploiting the $\sim 10^8$ matter-wave enhancement, are among the most sensitive rotation sensors ever built and are used in precision tests of fundamental physics, including searches for violations of Lorentz invariance and the equivalence principle. The application is nonobvious because the same effect that runs a navigation gyroscope becomes a probe of foundational symmetries.

**The Sagnac effect and the one-way speed of light.** The Sagnac effect is sometimes invoked in discussions of whether the one-way speed of light is conventional: the round-trip is unambiguous, but the rotating-frame asymmetry probes the synchronization, which is convention-dependent. Analyzing the Sagnac delay in this light clarifies which features of the speed of light are physical and which are conventions of simultaneity. The application is surprising because a practical gyroscope effect bears on a deep foundational question.

---

# Bridges

- **[[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]]** — the Sagnac delay is exactly twice the desynchronization gap: $\Delta t' = 2\Delta t'_{\text{desync}}$. This is the single most important link in the chapter. The impossibility of synchronizing clocks around the loop, expressed as a clock offset, becomes the Sagnac effect when expressed as an arrival-time difference of counter-propagating signals — the same circulation $\oint\Gamma^2\vec V\cdot d\vec\ell$ in both, with the factor of two arising because the two signals sample the gap with opposite signs.

- **[[Thm - Relativistic Velocity Addition]]** — the direct (helix) derivation of the Sagnac delay routes through the relativistic composition of the signal speed $v$ with the rim speed $r\omega$ to get the inertial angular velocities $\Omega_\pm$. The remarkable cancellation of $v$ from the final answer — the speed-independence of the Sagnac effect — emerges from the structure of the composition law, and is the cleanest demonstration that the effect is metric, not kinematic.

- **The Aharonov–Bohm effect (quantum mechanics)** — the Sagnac phase is a line integral of a "potential" around a loop equal to a flux of a "field" ($2\vec\omega$) through the enclosed area, observable only through interference, with no local effect along the path. This is structurally identical to the Aharonov–Bohm phase, with the four-rotation playing the role of the magnetic field. The Sagnac effect is the rotational/gravomagnetic Aharonov–Bohm effect, and the matter-wave Sagnac phase makes the analogy literal: both are geometric phases.

- **Kelvin's circulation theorem (fluid dynamics)** — the Sagnac delay, being twice the circulation of $\Gamma^2\vec V$, is the rotating-observer analogue of Kelvin's relation between circulation and enclosed vorticity flux. The four-rotation $\vec\omega$ is the vorticity, the disk is a rigid-rotation flow, and the Sagnac delay measures the enclosed vorticity — which is why it is $\propto\omega A$.

---

# Unlocked by This

> [!tip] Inertial Navigation Systems *(from Aerospace Engineering)*
> The Sagnac effect is the operating principle of the **ring-laser gyroscope** and the **fibre-optic gyroscope**, which together form the rotation-sensing core of every modern **inertial navigation system** — in aircraft, ships, submarines, missiles, and spacecraft. Because they have no moving parts, they never wear out or drift mechanically, and combined with accelerometers they allow a vehicle to track its position by dead reckoning with no external reference. The abstract loop integral $\oint\Gamma^2\vec V\cdot d\vec\ell$ of this chapter is, in this guise, a multi-billion-dollar industry and the reason an airliner can navigate across an ocean with no GPS.

> [!tip] Matter-Wave Gyrometry and the Foundations of Quantum Mechanics *(from Atom Interferometry)*
> The matter-wave Sagnac effect, with its $\sim\Gamma_p mc^2/hf \sim 10^8$ enhancement over the optical effect, makes **atom and neutron interferometers** the most sensitive rotation sensors ever built, and a testing ground for the interplay of quantum mechanics, special relativity, and gravity. That the *same* geometric phase governs light and matter — but with the matter phase enormously larger — is itself a deep statement about the universality of the rotating-frame geometry, and matter-wave Sagnac experiments probe whether quantum particles respond to rotation exactly as relativity predicts.
