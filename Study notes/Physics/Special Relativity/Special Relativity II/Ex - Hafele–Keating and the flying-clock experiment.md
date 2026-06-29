---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Time Dilation"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Problem Statement

In 1971 Hafele and Keating flew four caesium atomic clocks on commercial airliners around the world and compared them, on return, with identical clocks left at the United States Naval Observatory. The clocks disagreed by of order $10^{-7}\ \text{s}$. This exercise estimates the **special-relativistic** part of that effect and explains why the full experiment also requires a **general-relativistic** part. Restore $c$ throughout.

1. Treating a flown clock as moving at constant ground speed $v$ for a total flight time $T$ (as measured on the ground), show that the special-relativistic time *lost* by the flown clock relative to the ground clock is, for $v \ll c$,
$$\Delta\tau_{\text{SR}} \approx -\tfrac{1}{2}\frac{v^2}{c^2}\,T.$$
Derive this by expanding the time-dilation factor to leading order in $v/c$.
2. Put in numbers: a jet at $v \approx 250\ \text{m/s}$ flying for $T \approx 48\ \text{hours}$. Compute $\Delta\tau_{\text{SR}}$ and confirm it is of order $10^{-7}\ \text{s}$ (tens to hundreds of nanoseconds).
3. Explain why the flown clock runs **slow** by this special-relativistic effect, but the *gravitational* effect of general relativity makes a clock at altitude run **fast** (a clock higher in a gravitational potential ticks faster). State that the two effects are comparable in magnitude for airliner altitudes and partly cancel, and that this is why the bare special-relativistic estimate does not match the raw data.
4. Explain the eastward/westward asymmetry: because the ground itself moves (Earth's rotation), the relevant speed in the time-dilation formula is the clock's speed in a *non-rotating* (Earth-centred inertial) frame, so an eastward-flying clock (with the rotation) and a westward-flying clock (against it) lose different amounts.

**Recall:**

![[Thm - Time Dilation#Statement]]

The **proper time** ([[Def - Proper Time]]) accumulated by a clock along its worldline is the time it actually reads; for a clock moving at speed $v$ for ground-frame duration $T$, the proper time is $T/\gamma$. The relevant inertial frame for time dilation is one that does *not* rotate — an Earth-centred frame in which the planet's surface is itself moving eastward at the equatorial rotation speed.

---

# Convergent Strategy

**Problem class.** A *compute-an-effect plus reconcile-two-contributions* problem, applying time dilation quantitatively to a real experiment and confronting the general-relativistic correction. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] of identifying proper times and checking consistency carries over, with the twist that two physical effects superpose.

**Assumption pattern.** The key approximation is $v \ll c$, which licenses the leading-order expansion $\gamma \approx 1 + \tfrac12 v^2/c^2$. The "lost time" is the difference between the ground clock's elapsed time $T$ and the flown clock's proper time $T/\gamma$. The eastward/westward asymmetry flags that the *inertial* frame is non-rotating, so ground speed must be measured against it.

**Theorem routing.** Part 1 applies [[Thm - Time Dilation]] and expands. Part 2 substitutes numbers. Part 3 contrasts the kinematic (special-relativistic) slowing with the gravitational (general-relativistic) speeding, noting comparable magnitudes. Part 4 corrects the velocity to the Earth-centred inertial frame.

**Key decision point.** The crux of part 1 is recognising that the *difference* between the two clocks, not the dilation factor itself, is the observable, and that for $v \ll c$ it is second order in $v/c$ — tiny, but measurable with atomic clocks. The crux of parts 3–4 is that the experiment is *not* a clean special-relativity test: a gravitational effect of the same order is superposed, and the inertial frame is the non-rotating one, so the naive "flown clock moves, ground clock rests" picture must be refined.

---

# Legal Operations Used

1. **Use time dilation: a moving clock runs slow by $\gamma$** (operation 3 from the topic page). The flown clock is the moving clock; its proper time is $T/\gamma$, and the lost time is $T - T/\gamma$.

2. **Work in the rest frame, then boost out** (operation 2). The clean inertial frame here is the Earth-centred non-rotating frame; both the flown and ground clocks move in it (part 4), and their proper times are computed relative to it.

3. **Compute an invariant in the most convenient frame** (operation 8). The accumulated proper time is the invariant arc length of each clock's worldline; comparing the two flown-versus-ground proper times is the observable.

---

# Hints

> [!note]- Hint 1
> The flown clock's proper time is $T/\gamma$; the ground clock reads $T$ (to leading order, ignoring its own motion for now). The difference is $T/\gamma - T = T(1/\gamma - 1)$. Expand $1/\gamma = \sqrt{1 - v^2/c^2} \approx 1 - \tfrac12 v^2/c^2$ for $v \ll c$. The leading term is $-\tfrac12 (v^2/c^2) T$ — negative, so the flown clock loses time.

> [!note]- Hint 2
> $v^2/c^2 = (250/3\times10^8)^2 \approx 7\times10^{-13}$. With $T = 48\ \text{h} = 1.7\times10^5\ \text{s}$, $\Delta\tau_{\text{SR}} \approx -\tfrac12 \times 7\times10^{-13} \times 1.7\times10^5 \approx -6\times10^{-8}\ \text{s}$ — about $-60\ \text{ns}$, of order $10^{-7}\ \text{s}$.

> [!note]- Hint 3
> Special relativity: motion slows a clock ($-\tfrac12 v^2/c^2\,T$). General relativity: being higher in a gravitational potential $\Phi$ *speeds* a clock by $+\,\Phi/c^2$ per unit time, i.e. $+\,gh/c^2 \cdot T$ for altitude $h$. At airliner altitude these are comparable (both $\sim 10^{-7}\ \text{s}$ over the flight), and they have *opposite* sign, so they partly cancel — the net is a delicate difference, which is why a bare SR estimate misses the data.

> [!note]- Hint 4
> The time-dilation formula needs the speed in an *inertial* (non-rotating) frame. The ground is not inertial — it rotates eastward. So a clock flying *eastward* moves faster in the inertial frame (its speed adds to the rotation) and loses *more* time; a clock flying *westward* moves slower (subtracts) and may even lose less than the ground clock. This is the eastward/westward asymmetry Hafele and Keating observed.

---

# Solution

The special-relativistic slowing of a flown clock is of order $100$ nanoseconds — small but well within atomic-clock precision. The full experiment superposes a comparable, opposite-signed gravitational effect, and the eastward/westward asymmetry comes from measuring speeds in the non-rotating frame.

**Step 1: The special-relativistic time loss.**

> [!note]- Derivation
> A clock moving at speed $v$ for ground-frame time $T$ accumulates proper time $\tau_{\text{flown}} = T/\gamma$ ([[Thm - Time Dilation]]), while the ground clock (momentarily idealised as at rest in the inertial frame) reads $\tau_{\text{ground}} = T$. The difference is
> $$\Delta\tau_{\text{SR}} = \tau_{\text{flown}} - \tau_{\text{ground}} = \frac{T}{\gamma} - T = T\left(\frac{1}{\gamma} - 1\right).$$
> For $v \ll c$, expand $1/\gamma = \sqrt{1 - v^2/c^2} = 1 - \tfrac12\frac{v^2}{c^2} - \tfrac18\frac{v^4}{c^4} - \cdots$. To leading order,
> $$\Delta\tau_{\text{SR}} \approx T\left(-\tfrac12\frac{v^2}{c^2}\right) = -\frac{1}{2}\frac{v^2}{c^2}\,T.$$
> The sign is negative: the flown clock **loses** time relative to the ground — it ticks slow, as a moving clock must. The effect is *second* order in $v/c$, which is why everyday speeds make it minuscule and why atomic clocks (stable to $\sim 10^{-13}$) are needed to see it.

**Step 2: The numbers.**

> [!note]- Derivation
> Take $v \approx 250\ \text{m/s}$ (a typical jet ground speed) and $T \approx 48\ \text{hours} = 1.7\times10^5\ \text{s}$. Then
> $$\frac{v^2}{c^2} = \left(\frac{250}{3\times10^8}\right)^2 \approx 6.9\times10^{-13},$$
> $$\Delta\tau_{\text{SR}} \approx -\tfrac12 \times 6.9\times10^{-13} \times 1.7\times10^5\ \text{s} \approx -5.9\times10^{-8}\ \text{s} \approx -60\ \text{ns}.$$
> This is of order $10^{-7}\ \text{s}$, matching the scale of the measured discrepancy. (The actual Hafele–Keating numbers, with realistic variable speeds and both flight directions, gave kinematic losses of order tens to a couple hundred nanoseconds depending on direction.)

**Step 3: The opposing gravitational effect.**

> [!note]- Derivation
> Special relativity says *motion* slows a clock: $\Delta\tau_{\text{SR}} = -\tfrac12(v^2/c^2)T < 0$. General relativity adds a second, independent effect: a clock higher in a gravitational potential ticks *faster*. Quantitatively, a clock at altitude $h$ above the ground gains, relative to the ground clock,
> $$\Delta\tau_{\text{GR}} \approx +\frac{gh}{c^2}\,T > 0,$$
> where $g$ is the gravitational acceleration ($\Phi = gh$ the potential difference). For an airliner at $h \approx 10\ \text{km}$ over $T \approx 1.7\times10^5\ \text{s}$, $\Delta\tau_{\text{GR}} \approx (9.8 \times 10^4 / 9\times10^{16}) \times 1.7\times10^5 \approx +1.8\times10^{-7}\ \text{s}$ — comparable in magnitude to the special-relativistic loss and of **opposite sign**. The two effects partly cancel: the net time difference is a delicate balance, $\Delta\tau = \Delta\tau_{\text{SR}} + \Delta\tau_{\text{GR}}$, with the gravitational term typically winning at airliner altitude (so a flown clock can end up *ahead*). This is precisely why a bare special-relativistic estimate does not match the raw data — the experiment tests the *sum* of the two relativistic effects, and Hafele and Keating's agreement with the combined prediction confirmed *both* special and general relativity at once.

**Step 4: The eastward/westward asymmetry.**

> [!note]- Derivation
> The time-dilation formula requires the clock's speed in an *inertial* frame, and the ground is **not** inertial — it rotates eastward at the equatorial speed $v_\oplus \approx 460\ \text{m/s}$. The clean inertial frame is the Earth-centred *non-rotating* frame, in which even the ground clock moves (eastward, at $v_\oplus$). A clock flying eastward at ground speed $v_{\text{air}}$ has inertial speed $v_\oplus + v_{\text{air}}$, while one flying westward has $v_\oplus - v_{\text{air}}$. Since $\Delta\tau_{\text{SR}} \propto -v^2$, the eastward clock (larger inertial speed) loses *more* kinematic time than the ground clock, and the westward clock (smaller inertial speed) loses *less* — indeed a westward clock can run *faster* than the ground clock kinematically. This direction dependence, superposed on the (direction-independent) gravitational gain, produces the observed asymmetry: the eastward and westward round-the-world flights returned with *different* clock offsets, both matching the combined relativistic prediction. The lesson is that "the ground clock is at rest" is false in the inertial frame, and getting the velocities right requires accounting for Earth's rotation.

> [!note]- Complete formal solution
> A flown clock at speed $v$ for ground time $T$ reads proper time $T/\gamma$, so its loss relative to a ground clock is $\Delta\tau_{\text{SR}} = T(1/\gamma - 1) \approx -\tfrac12(v^2/c^2)T$ to leading order in $v/c$. For $v = 250\ \text{m/s}$, $T = 48\ \text{h}$: $\Delta\tau_{\text{SR}} \approx -60\ \text{ns}$, of order $10^{-7}\ \text{s}$. General relativity adds a gravitational gain $\Delta\tau_{\text{GR}} \approx +gh\,T/c^2 \approx +180\ \text{ns}$ at $h \approx 10\ \text{km}$ — comparable and opposite — so the net is a partial cancellation and the bare SR estimate misses the raw data; the experiment tests the sum. Because the inertial frame is the non-rotating Earth-centred one, in which the ground itself moves east at $\sim 460\ \text{m/s}$, an eastward clock (inertial speed $v_\oplus + v_{\text{air}}$) loses more kinematic time than a westward one ($v_\oplus - v_{\text{air}}$), giving the observed eastward/westward asymmetry. $\blacksquare$

---

# Key Takeaways

**Observable time differences are second order in $v/c$, which is why atomic clocks are the right instrument.** The lost time $\Delta\tau_{\text{SR}} = -\tfrac12(v^2/c^2)T$ scales as the *square* of the small parameter $v/c$, so at aircraft speeds ($v/c \sim 10^{-6}$) it is suppressed by $\sim 10^{-12}$ relative to the elapsed time — utterly invisible to ordinary clocks, but a comfortable signal for caesium standards stable to $10^{-13}$. The general moral for relativistic estimates: the leading correction to a duration or length is usually $O(v^2/c^2)$, and recognising this tells you both how small the effect is and how precise an instrument you need to see it. The expansion $1/\gamma \approx 1 - \tfrac12 v^2/c^2$ is the workhorse for every low-speed relativistic estimate — kinetic energy $\tfrac12 mv^2$ as the first correction to $mc^2$, the transverse Doppler shift, the GPS clock rate — and being fluent with it converts "compute the relativistic effect" into a one-line Taylor expansion.

**Real relativistic experiments superpose special and general relativity, and the cleanest "SR demonstration" is rarely clean.** Hafele–Keating is presented as a time-dilation test, but the honest accounting shows a gravitational effect of *comparable magnitude and opposite sign* riding along, so the measured offset is a near-cancellation that tests the *sum* of both theories. This is the rule, not the exception: the Global Positioning System, gravitational redshift measurements, and precision clock comparisons all see kinematic and gravitational time dilation together, and disentangling them requires modelling both. The transferable diagnostic: whenever a clock's environment involves both motion *and* a change of gravitational potential (altitude, proximity to a mass), compute *both* $-\tfrac12 v^2/c^2$ and $+\Phi/c^2$ per unit time and add them — never report the kinematic piece alone as "the relativistic effect". That the two have opposite signs (motion slows, height speeds) is the single fact that explains why naive estimates of such experiments come out wrong.

**The inertial frame is non-rotating, and "the ground is at rest" is a trap.** The eastward/westward asymmetry is the experiment's sharpest lesson: time dilation must be computed with velocities measured in a genuine inertial frame, and the rotating Earth's surface is not one. In the Earth-centred non-rotating frame the ground clock is itself moving eastward at $\sim 460\ \text{m/s}$, so a flown clock's relevant speed is its inertial speed (rotation $\pm$ airspeed), not its airspeed, and the sign of $v^2$ then makes eastward and westward flights lose different amounts. The broader principle is that relativistic formulas are stated for inertial frames, and applying them in a rotating or accelerating frame without first transforming to an inertial one is a classic error; when a problem involves a spinning planet, an orbiting satellite, or any rotating apparatus, locate the non-rotating inertial frame first and measure all velocities against it. This is the same care that the [[Ex - The twin paradox|twin paradox]] demands (only one twin is inertial) and that makes the GPS correction — which must combine orbital-speed slowing and gravitational-altitude speeding in the Earth-centred inertial frame — come out right.
