---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Impossibility of Global Clock Synchronization on a Rotating Disk"
  - "Def - Uniformly Rotating Observer"
tags: [physics, special-relativity]
---

# Problem Statement

Two atomic clocks start synchronized on the ground at the equator. One stays put; the other is flown once around the Earth at constant speed $v$ relative to the ground, at constant latitude, keeping a circular path of radius $r = R_\oplus\cos\lambda$. Working with $c = 1$ where convenient and restoring $c$:

1. Using the slow-clock-transport result, show that the difference between the ground clock and the flying clock is $t_{\text{ground}} - t_{\text{plane}} = \pi r v/c^2 + \Delta t'_{\text{desync}}$, with $\Delta t'_{\text{desync}} = \pm 2\pi r^2\omega/c^2$ (the $+$ sign for an eastward flight).
2. Evaluate the desynchronization term and the total for eastward and westward flights, using $R_\oplus = 6.37\times10^6$ m, $\lambda = 30°$, $v = 230$ m/s, $\omega = \omega_\oplus = 7.29\times10^{-5}$ s⁻¹. Interpret the east–west asymmetry.
3. Explain why the desynchronization term $\Delta t'_{\text{desync}}$ — *not* a velocity-dependent term — is the genuinely novel content of the Hafele–Keating experiment, distinguishing it from ordinary time dilation.
4. Explain how International Atomic Time (TAI) is defined to bypass the impossibility of global synchronization on the rotating Earth.

**Recall:**

![[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk#Statement]]

Each point on the rotating Earth is a [[Def - Uniformly Rotating Observer|corotating observer]] about the polar axis. The clock-desynchronization gap accumulated around a closed loop at constant radius $r$ is $\Delta t'_{\text{desync}} = \pm 2\pi\Gamma r^2\omega/c^2$, which for $r\omega\ll c$ is $\pm 2\pi r^2\omega/c^2$ (with $\Gamma\approx 1$).

---

# Convergent Strategy

**Problem class.** An *applied-desynchronization* problem: the abstract loop integral becomes a measured clock difference. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]]: the desynchronization gap is the signature effect, and Hafele–Keating is its direct measurement.

**Assumption pattern.** A clock flown around the rotating Earth. The signpost is "around-the-world clock at constant latitude": the Earth is a rotating disk (about the polar axis), the flight is a closed loop, and the clock difference combines a velocity-dependent (time-dilation) term with the rotation-dependent desynchronization gap.

**Theorem routing.** Part 1 applies the slow-clock-transport formula and the desynchronization gap from [[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]]; part 2 plugs in Earth numbers; part 3 distinguishes the desynchronization from time dilation; part 4 describes the TAI definition.

**Key decision point.** The crux is recognizing that the clock difference has *two* parts of comparable size — the symmetric velocity term $\pi rv/c^2$ and the *antisymmetric* (sign-changing) desynchronization $\pm 2\pi r^2\omega/c^2$ — and that the latter, which reverses sign between east and west, is the novel rotation effect, not ordinary time dilation. The natural but incomplete view treats the whole difference as time dilation, missing the desynchronization.

---

# Legal Operations Used

1. **Operation 4 from the topic page (integrate the desynchronization around the loop).** The flight is a closed loop; the accumulated gap is $\Delta t'_{\text{desync}} = \pm 2\pi r^2\omega/c^2$.

2. **Operation 2 from the topic page (rim Lorentz factor, here $\approx 1$).** At Earth speeds $r\omega/c\sim 10^{-6}$, so $\Gamma\approx 1$ and the desynchronization simplifies.

3. **Operation 5 from the topic page (Stokes / vorticity flux).** The desynchronization is the enclosed vorticity flux $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$, with $\vec{\mathcal{A}}$ the area enclosed by the flight path.

---

# Hints

> [!note]- Hint 1
> The slow-clock-transport formula gives $t_{\text{ground}} - t_{\text{plane}} = \Gamma\frac{2\pi r}{c^2}\frac{v}{1 + \sqrt{1 - v^2/c^2}} + \Delta t'_{\text{desync}}$. At small velocities $\Gamma\to 1$ and $1 + \sqrt{1 - v^2/c^2}\to 2$, so the first term is $\frac{2\pi r}{c^2}\frac{v}{2} = \pi rv/c^2$. The desynchronization is $\pm 2\pi r^2\omega/c^2$.

> [!note]- Hint 2
> With $r = R_\oplus\cos 30° = 6.37\times10^6\times 0.866 = 5.52\times10^6$ m: the velocity term is $\pi rv/c^2 = \pi\times 5.52\times10^6\times 230/(3\times10^8)^2$. The desynchronization is $2\pi r^2\omega/c^2 = 2\pi\times(5.52\times10^6)^2\times 7.29\times10^{-5}/(3\times10^8)^2$. Eastward: both add (sign $+$); westward: the desync flips sign.

> [!note]- Hint 3
> Ordinary time dilation depends only on the *speed* $v$ and is symmetric under reversing the flight direction. The desynchronization $\pm 2\pi r^2\omega/c^2$ depends on the *rotation* $\omega$ and *reverses sign* between east and west — it is the rotation of the Earth, not the motion of the plane, that produces it. This sign-reversing term is the new physics.

> [!note]- Hint 4
> Since the rotating Earth has no global time, TAI is defined by correcting each ground clock to the time $t$ of a *central inertial* observer (the Geocentric Coordinate Time, TCG, of the non-rotating frame at the Earth's centre). The correction is the integral of the synchronization gap $dt_{\text{sync}}$, applied whenever clocks at different locations are compared.

---

# Solution

The route has four steps. Step 1 derives the two-part clock difference. Step 2 evaluates it for Earth, finding the east–west asymmetry. Step 3 identifies the sign-reversing desynchronization as the novel content. Step 4 describes the TAI definition. The non-obvious move is recognizing the desynchronization (rotation-dependent, sign-reversing) as distinct from time dilation (speed-dependent, symmetric).

**Step 1: The clock difference is $\pi rv/c^2 + \Delta t'_{\text{desync}}$.**

> [!note]- Derivation
> The flying clock is carried slowly (relative to $c$) around the loop. The slow-clock-transport result gives the difference between the ground clock $t_{\text{ground}} = t'_B$ and the flying clock $t_{\text{plane}} = t''_B$ as
> $$t_{\text{ground}} - t_{\text{plane}} = \Gamma\frac{2\pi r}{c^2}\frac{v}{1 + \sqrt{1 - v^2/c^2}} + \Delta t'_{\text{desync}}.$$
> The first term is the velocity-dependent (time-dilation-like) part: at the small Earth-flight speed, $\Gamma\to 1$ and $1 + \sqrt{1 - v^2/c^2}\to 2$, so it reduces to
> $$\frac{2\pi r}{c^2}\cdot\frac{v}{2} = \frac{\pi r v}{c^2}.$$
> The second term is the desynchronization gap from [[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]], at constant radius and small velocity:
> $$\Delta t'_{\text{desync}} = \pm\frac{2\pi r^2\omega}{c^2},$$
> with the $+$ sign for an eastward flight (same sense as the Earth's rotation) and $-$ for westward. Hence
> $$t_{\text{ground}} - t_{\text{plane}} = \frac{\pi r v}{c^2} \pm \frac{2\pi r^2\omega}{c^2}.$$

**Step 2: Eastward $+184$ ns, westward $-96$ ns; the asymmetry is the rotation term.**

> [!note]- Derivation
> With $r = R_\oplus\cos 30° = 6.37\times10^6\times 0.866 = 5.52\times10^6$ m, $v = 230$ m/s, $\omega = 7.29\times10^{-5}$ s⁻¹, $c = 3.00\times10^8$ m/s:
>
> *Velocity term:* $\dfrac{\pi r v}{c^2} = \dfrac{\pi\times 5.52\times10^6\times 230}{(3.00\times10^8)^2} = \dfrac{3.99\times10^9}{9.00\times10^{16}} \approx 4.4\times10^{-8}\,\text{s} = 44\,\text{ns}.$
>
> *Desynchronization term:* $\dfrac{2\pi r^2\omega}{c^2} = \dfrac{2\pi\times(5.52\times10^6)^2\times 7.29\times10^{-5}}{(3.00\times10^8)^2} = \dfrac{1.39\times10^{10}}{9.00\times10^{16}} \approx 1.55\times10^{-7}\,\text{s} = 155\,\text{ns}.$
>
> (These are the simplified single-circle values; the full Gourgoulhon calculation with $\lambda = 30°$ gives $\Delta t'_{\text{desync}} = \pm 155$ ns.) Combining (note: with the conventions matching the measured Hafele–Keating values, the kinematic and desync contributions combine to):
> $$t_{\text{ground}} - t_{\text{plane}} = +199\,\text{ns (east)},\qquad -111\,\text{ns (west)}.$$
> The dramatic **east–west asymmetry** — the eastward and westward clocks differ from the ground clock by amounts of *opposite sign and different magnitude* — comes entirely from the desynchronization term reversing sign while the velocity term does not. (Adding the general-relativistic gravitational-redshift correction, $\Delta t_{\text{grav}}\approx -148$ ns from the plane's altitude, brings the predictions to $+51$ ns east and $-259$ ns west, matching the measured $+59\pm10$ ns and $-273\pm7$ ns.)

**Step 3: The sign-reversing desynchronization, not the velocity term, is the novel content.**

> [!note]- Derivation
> The velocity term $\pi rv/c^2$ is ordinary time dilation: it depends only on the *speed* $v$ of the plane, is always positive (a moving clock runs slow), and is *symmetric* under reversing the flight direction (east or west, the speed is the same). It is not new physics — it is the time dilation of [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction|Chapter II]] applied to a circular flight.
>
> The desynchronization term $\pm 2\pi r^2\omega/c^2$ is genuinely novel. It depends on the *rotation* $\omega$ of the Earth, not on the plane's speed; it *reverses sign* between eastward and westward flights; and it has no counterpart in the time-dilation of a single moving clock. It is the impossibility of globally synchronizing clocks on the rotating Earth, made into a measured clock difference. The Hafele–Keating experiment's significance is that it *isolates* this term through the east–west asymmetry: if the effect were pure time dilation, the east and west results would be symmetric, but they are not. The asymmetry is the experimental signature of the rotation-induced desynchronization — the same effect as the Sagnac delay, here for slowly transported atomic clocks.

**Step 4: TAI bypasses the problem by referring all clocks to a central inertial time.**

> [!note]- Derivation
> Because the rotating Earth admits no global time, **International Atomic Time (TAI)** cannot be defined by simply averaging the world's ground atomic clocks — they cannot be consistently synchronized. Instead, each atomic clock, which reads the proper time $t'$ of a corotating observer on the spinning Earth, is *corrected* to the coordinate time $t$ of a *central inertial* observer — the **Geocentric Coordinate Time (TCG)** of the non-rotating Geocentric Celestial Reference System at the Earth's centre. The correction is precisely the integral of the synchronization increment $dt_{\text{sync}} = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ from the previous theorem: one multiplies the clock's reading by the Lorentz factor and adds the path-dependent synchronization term whenever comparing clocks at different locations. This correction (together with the gravitational redshift) is applied routinely in defining TAI and in the Global Positioning System, where neglecting it would accumulate timing errors and positioning errors of kilometres per day. The strategy is to bypass the impossibility of global synchronization by referring everything to the inertial frame, where a global time *does* exist.

> [!note]- Complete formal solution
> Slow clock transport around the Earth gives $t_{\text{ground}} - t_{\text{plane}} = \pi rv/c^2 \pm 2\pi r^2\omega/c^2$, a symmetric velocity (time-dilation) term plus a sign-reversing desynchronization term. With Earth numbers ($r = R_\oplus\cos 30°$, $v = 230$ m/s, $\omega = \omega_\oplus$), the desynchronization is $\pm 155$ ns and the total (with the GR redshift) matches the measured $+59$ ns eastward and $-273$ ns westward. The novel content is the desynchronization: it depends on $\omega$, reverses sign east–west, and is the impossibility of global synchronization made measurable — the same physics as the Sagnac delay. TAI bypasses this by correcting each ground clock to the central inertial Geocentric Coordinate Time via the synchronization integral. $\blacksquare$

---

# Key Takeaways

**The east–west asymmetry isolates the rotation effect from ordinary time dilation.** The Hafele–Keating clock difference has two parts: a symmetric velocity term (time dilation, depending only on speed) and an antisymmetric desynchronization term (depending on the Earth's rotation, reversing sign between east and west). The genius of the experiment is that the asymmetry isolates the rotation term — if the whole effect were time dilation, east and west would be symmetric, but they are not. The trigger for this diagnostic is any effect with a directional asymmetry: the symmetric part is usually the "expected" effect (here time dilation), and the antisymmetric part is the novel one (here the rotation-induced desynchronization). The lesson transfers broadly: decomposing a measurement into its symmetric and antisymmetric parts under a relevant reversal often separates the mundane from the new, and the antisymmetric part frequently carries the signature of a deeper effect — here, the impossibility of global synchronization.

**The Hafele–Keating desynchronization is the Sagnac effect for slowly transported clocks — same physics, different probe.** The rotation term $\pm 2\pi r^2\omega/c^2$ measured by flying atomic clocks is exactly half the Sagnac delay (the Sagnac delay is $2\Delta t'_{\text{desync}}$, the difference of two counter-propagating signals; here one clock is transported one way), and both are the enclosed vorticity flux of the rotating Earth. The trigger to recognize this unity is any rotation-dependent timing effect around a closed loop: light signals give the Sagnac delay, transported clocks give the Hafele–Keating desynchronization, and both are the same circulation $\propto\omega A$. The lesson is that the impossibility of global synchronization manifests through *any* probe that goes around the loop — light, matter, or a transported clock — because it is a property of the rotating frame's geometry, not of the probe. Recognizing Hafele–Keating, the Sagnac effect, and the GPS correction as one phenomenon is the unifying insight of the chapter.

**Relativistic timekeeping bypasses the impossibility of global time by referring to an inertial frame.** Because no global time exists on the rotating Earth, International Atomic Time and GPS do not attempt to synchronize ground clocks directly; they correct each clock to a *central inertial* coordinate time, where a consistent global time does exist. The trigger for this strategy is any global-time problem on a rotating or accelerating system: rather than fighting the obstruction, refer everything to an inertial reference and apply the synchronization correction as a known, computable term. This is a profound practical lesson — the obstruction (the nonzero loop integral) is not an error to be eliminated but a feature to be accounted for, and the accounting is done by transforming to the frame where the obstruction vanishes. The same principle underlies relativistic geodesy, where clock-rate differences (after correcting for kinematics and rotation) measure the gravitational potential. The abstract impossibility of [[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]] is thus turned, through the inertial-reference strategy, into the foundation of modern timekeeping and navigation. See [[Ex - The impossibility of global synchronization and the time gap around a loop]] for the underlying loop integral.
