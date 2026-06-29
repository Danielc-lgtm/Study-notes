---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Proper Time"
  - "Thm - Inertial Worldlines Maximise Proper Time"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Problem Statement

In 1971 Hafele and Keating flew four caesium atomic clocks around the world on commercial jets — once eastward, once westward — and compared them on return with reference clocks that had stayed on the ground. This is the twin paradox made into a laboratory experiment. Working with $c$ restored:

1. Explain why *both* the flying clocks and the ground clock follow non-trivial worldlines (helices, not a straight line), so the comparison is genuinely "which worldline carries more proper time", and why the **direction** of flight matters.
2. Identify the two competing relativistic effects: the **special-relativistic** (kinematic, velocity) effect and the **general-relativistic** (gravitational redshift, altitude) effect. State the sign of each and why they are comparable in magnitude here.
3. Quote and interpret the measured results: eastward $T' = T - 59 \pm 10\ \mathrm{ns}$ and westward $T' = T + 273 \pm 7\ \mathrm{ns}$, against the special-relativity-plus-general-relativity predictions $-40 \pm 23\ \mathrm{ns}$ and $+275 \pm 21\ \mathrm{ns}$. What does the experiment confirm?
4. State briefly how the 1975 **Alley experiment** sharpened this, with its clean separation $T' = T - 5.7\,(\mathrm{SR}) + 52.8\,(\mathrm{GR}) = T + 47.1\ \mathrm{ns}$.

**Recall:**

![[Def - Proper Time#The Definition]]

The [[Def - Proper Time|proper time]] along a worldline is its metric arc length, $\tau = \int\sqrt{ds^2} = \int dt/\gamma$; it depends on the worldline, not just the endpoints. That the *straightest* worldline carries the *most* proper time is [[Thm - Inertial Worldlines Maximise Proper Time|the geodesic principle]]. An atomic clock is an excellent approximation to an ideal clock, reading proper time independent of its acceleration up to $\sim 10^{23}\,\mathrm{m\,s^{-2}}$.

---

# Convergent Strategy

**Problem class.** An *experimental-verification* problem: turning the twin paradox into measurable numbers, with the complication that two effects (special- and general-relativistic) both contribute. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: compute the proper time of each worldline as $\int dt/\gamma$, but here the gravitational potential also enters, so the proper time picks up an altitude term from general relativity.

**Assumption pattern.** The decisive subtleties are: (i) the ground clock is *not* inertial — it co-rotates with the spinning Earth, so it too has a velocity (and hence a helical worldline), which is why flight *direction* matters (eastward adds to the Earth's rotation, westward subtracts); and (ii) the planes fly higher in Earth's gravitational potential, so the general-relativistic redshift speeds them up — an effect of comparable size to the kinematic slowing, which *must* be included.

**Theorem routing.** Part 1 routes through the observation that all clocks are on helical (rotating) worldlines, so the comparison is worldline-against-worldline. Part 2 splits the proper-time difference into a velocity piece (special relativity, $-\tfrac12 v^2/c^2$ in the metric) and a potential piece (general relativity, $+\Phi/c^2$). Part 3 reads off the data. Part 4 cites Alley's cleaner numbers.

**Key decision point.** The crux — and the reason this experiment is subtle — is that you cannot treat the ground clock as the "stay-at-home inertial twin". It is rotating with the Earth, so *both* twins move, and the eastward/westward asymmetry comes from adding versus subtracting the plane's velocity to the ground clock's rotational velocity. The second crux is that special relativity alone is *insufficient*: the gravitational (general-relativistic) effect is comparable and opposite in sign, so the honest comparison requires both.

---

# Legal Operations Used

1. **Compute proper time along each worldline** (proper-time operation). Each clock's elapsed time is $\int dt/\gamma$ along its helical worldline; the difference is what is measured.

2. **Classify and compare worldlines** (operation 9 from the topic page). All clocks follow timelike helices; the question is which helix carries more proper time, decided by speed (and, via general relativity, altitude).

3. **Separate invariant contributions** (operation related to invariants). The proper-time difference splits cleanly into a velocity (special-relativistic) term and a gravitational-potential (general-relativistic) term.

---

# Hints

> [!note]- Hint 1
> The ground clock is *not* at rest in an inertial frame — it rotates with the Earth at the local surface speed. So both the plane and the ground clock have velocities, and the relevant quantity is the *difference* in their speeds. Eastward flight adds the plane's speed to the Earth's rotation; westward subtracts it. This is why the two flights give different — even opposite-sign — results.

> [!note]- Hint 2
> Two effects: (SR) a faster clock runs slow, $d\tau \approx dt(1 - \tfrac12 v^2/c^2)$; (GR) a clock higher in the gravitational potential runs *fast*, $d\tau \approx dt(1 + \Phi/c^2)$ with $\Phi = gh > 0$ at altitude $h$. The plane is both faster (SR slows it) and higher (GR speeds it). At airliner altitude and speed the two effects are comparable in magnitude.

> [!note]- Hint 3
> Eastward: the plane's eastward speed adds to the Earth's rotation, so the SR slowing dominates and the clock loses time, $T' < T$ ($-59$ ns). Westward: the plane partly cancels the Earth's rotation, the SR effect is smaller, and the GR altitude gain wins, so the clock *gains* time, $T' > T$ ($+273$ ns). Both agree with the combined prediction within error bars.

> [!note]- Hint 4
> Alley used a dedicated aircraft flying a tight loop at low speed, making the SR and GR contributions cleanly separable: $-5.7$ ns from velocity, $+52.8$ ns from altitude, net $+47.1$ ns, confirmed to $1.5\%$.

---

# Solution

The Hafele–Keating experiment is the twin paradox dragged out of thought-experiment land and onto commercial airliners — and its lasting lesson is that proper time genuinely depends on the worldline, atomic clocks genuinely track it, and the effect is real to the nanosecond. The plan: Step 1 establishes that all clocks are on rotating worldlines; Step 2 separates the two relativistic effects; Step 3 reads the data; Step 4 cites the cleaner Alley follow-up.

**Step 1: Every clock is on a helical worldline, and direction matters.**

> [!note]- Derivation
> Naively one pictures the ground clock as the "stay-at-home inertial twin" and the planes as travellers. But the Earth *rotates*, so the ground clock co-rotates with it, tracing a **helix** in spacetime (circular motion at the local surface speed $v_\oplus = \Omega R\cos\lambda \approx 460\,\mathrm{m\,s^{-1}}\cos\lambda$ at latitude $\lambda$), not a straight line. The flying clocks also trace helices, at the planes' ground speeds. So the experiment compares the proper times of *three different helical worldlines* between the departure event $A$ and the return event $B$ — a genuine "which worldline carries more proper time" comparison, computed by integrating $\int dt/\gamma$ along each (Gourgoulhon does this with the full reconstructed trajectories).
>
> Because the ground clock is itself moving, the **direction of flight matters**. An *eastward* plane flies in the same sense as the Earth's rotation, so its total speed (in a non-rotating, Earth-centred inertial frame) is *larger* than the ground clock's — it moves faster, hence its clock is slowed more by the kinematic effect. A *westward* plane flies against the rotation, partly cancelling it, so its inertial-frame speed is *smaller* than the ground clock's — it moves *slower*, and its clock can run *faster* than the ground clock. This is why the two flights give opposite-sign results: the right reference is the non-rotating frame, in which neither clock is at rest.

**Step 2: The two competing effects, special- and general-relativistic.**

> [!note]- Derivation
> The proper time of a clock at speed $v$ and gravitational potential $\Phi = gh$ (height $h$ above the ground) is, to first order,
> $$d\tau \approx dt\Big(1 - \frac{v^2}{2c^2} + \frac{\Phi}{c^2}\Big),$$
> the first correction being **special-relativistic** (velocity time dilation, a *slowing*, sign $-$) and the second **general-relativistic** (gravitational redshift: clocks higher in the potential run *faster*, sign $+$). The plane is both *faster* than the ground clock (SR slows it relative to the ground) and *higher* (GR speeds it relative to the ground). The difference in elapsed times between a flying clock and the ground clock is
> $$T' - T \approx \int\Big[-\frac{v_{\text{plane}}^2 - v_{\text{ground}}^2}{2c^2} + \frac{g\,h}{c^2}\Big]dt,$$
> with the velocities in the non-rotating frame. The two terms are *comparable in magnitude* at airliner altitude ($\sim 10\,\mathrm{km}$) and speed ($\sim 250\,\mathrm{m\,s^{-1}}$): the gravitational redshift over $10\,\mathrm{km}$ and the velocity dilation at jet speeds both produce shifts of order tens to hundreds of nanoseconds over a round-the-world flight. **Special relativity alone is therefore insufficient** — the experiment tests the *sum* of the two effects, and the gravitational piece (strictly a general-relativistic effect, [[Special Relativity XXV — Toward Relativistic Gravitation|treated later]]) must be included to compare with data.

**Step 3: The measured results.**

> [!note]- Derivation
> The precise computation, using the reconstructed airplane trajectories (Gourgoulhon carries it out in the energy chapter), predicts, and the experiment measures:
> $$\textbf{Eastward:}\quad T' = T - 59 \pm 10\ \mathrm{ns}\quad(\text{prediction } -40 \pm 23\ \mathrm{ns}),$$
> $$\textbf{Westward:}\quad T' = T + 273 \pm 7\ \mathrm{ns}\quad(\text{prediction } +275 \pm 21\ \mathrm{ns}).$$
> *Eastward* ($T' < T$, the clock loses time): the plane's eastward speed *adds* to the Earth's rotation, so the kinematic (SR) slowing dominates the gravitational (GR) speeding, and the flying clock comes back *younger* — the classic twin-paradox outcome, the bent-and-fast worldline carrying less proper time.
>
> *Westward* ($T' > T$, the clock gains time): flying against the rotation *reduces* the plane's inertial-frame speed below the ground clock's, so the SR effect is small and the GR altitude gain *wins* — the flying clock comes back *older*. (The ground clock, rotating fastest eastward, is now the faster-moving one, so *it* is the more time-dilated.)
>
> Within the (sizeable) error bars, both measurements agree with the special-relativity-plus-general-relativity predictions. **The experiment confirms that the proper time elapsed between two events depends on the worldline joining them** — that Newton's absolute time is wrong and relativity's worldline-dependent time is right — and that atomic clocks track proper time to the nanosecond. It is the experimental demonstration that the twin paradox is a real, measurable effect, not a semantic puzzle.

**Step 4: The Alley experiment (1975).**

> [!note]- Derivation
> Carroll Alley sharpened the test in 1975 with a dedicated antisubmarine aircraft (a Lockheed P-3C Orion) flying a tight $15$-hour loop over Chesapeake Bay at low speed ($\sim 150\,\mathrm{m\,s^{-1}}$) and moderate altitude ($\sim 7.6$–$10.7\,\mathrm{km}$), against identical clocks in a trailer on the ground. The low speed and controlled trajectory made the two contributions cleanly separable:
> $$T' = T \underbrace{-\ 5.7\,\mathrm{ns}}_{\text{SR (velocity)}}\ \underbrace{+\ 52.8\,\mathrm{ns}}_{\text{GR (altitude)}} = T + 47.1\ \mathrm{ns},$$
> measured in agreement to a relative accuracy of $1.5\%$. Here the gravitational (GR) effect is about *ten times* the kinematic (SR) effect — the slow, high loop maximises the altitude term and minimises the velocity term — giving a net *gain* of $47$ ns. This confirms the twin paradox (the special-relativistic piece) to about $15\%$ accuracy in isolation, and the combined relativistic time-keeping to $1.5\%$. Together with Hafele–Keating, it establishes proper time as the physical time read by real clocks.

> [!note]- Complete formal solution
> The ground clock co-rotates with the Earth (helix at $\sim 460\,\mathrm{m\,s^{-1}}\cos\lambda$), so all clocks are on helical worldlines and the experiment compares their proper times $\int dt/\gamma$; flight direction matters because eastward adds to, and westward subtracts from, the Earth's rotation in the non-rotating frame. To first order $d\tau \approx dt(1 - v^2/2c^2 + \Phi/c^2)$: the velocity term (SR) slows the clock, the potential term (GR, $\Phi = gh$) speeds it, and at airliner altitude/speed the two are comparable, so both must be included. Measured: eastward $T' = T - 59 \pm 10$ ns (SR slowing dominates, clock younger), westward $T' = T + 273 \pm 7$ ns (GR altitude wins, clock older), agreeing with the SR+GR predictions $-40 \pm 23$ and $+275 \pm 21$ ns. The experiment confirms proper time depends on the worldline and atomic clocks track it. Alley (1975), a slow high loop, cleanly split $T' = T - 5.7\,(\mathrm{SR}) + 52.8\,(\mathrm{GR}) = T + 47.1$ ns to $1.5\%$. $\blacksquare$

> [!warning] Illegal but tempting: treating the ground clock as the inertial stay-at-home twin
> The instinct from the idealised [[Ex - The twin paradox|twin paradox]] is to call the ground clock "the inertial twin who ages more" and the planes "the travellers who age less". This fails here for two reasons. First, the ground clock is *not* inertial — it rotates with the Earth, so *both* clocks move, and the right reference is a non-rotating Earth-centred frame in which neither is at rest; this is exactly why the westward clock can come back *older* than the ground clock (it moves *slower* than the rotating ground). Second, the gravitational (GR) effect is comparable to and opposite from the kinematic (SR) effect, so even the sign of the result is not fixed by special relativity alone. The diagnostic: in any real twin-paradox experiment on a rotating, gravitating planet, you must (i) work in a non-rotating frame so the ground clock's own motion is accounted for, and (ii) include the gravitational redshift — the naive "stay-at-home is inertial, traveller ages less" picture is only the flat-space, single-turnaround idealisation.

---

# Key Takeaways

**The twin paradox is an experimental fact: proper time really depends on the worldline.** Hafele–Keating and Alley are not demonstrations of a thought experiment — they are measurements, to the nanosecond, confirming that two clocks reunited after travelling different worldlines read different elapsed times. This nails down the central claim of the chapter: [[Def - Proper Time|proper time]] is the metric arc length of a worldline, it is path-dependent, and atomic clocks track it. Newton's absolute time — one universal clock for all — is experimentally *false*. The reusable lesson is that the abstract geometric statement "$\tau = \int\sqrt{ds^2}$ depends on the curve" has a hard empirical consequence that has been checked and re-checked (GPS satellites correct for exactly these effects continuously, or they would accumulate kilometre-scale position errors per day). When you compute a proper-time difference, you are computing something nature has measured.

**Special relativity is not enough on a gravitating planet — the gravitational redshift is comparable.** A clean conceptual takeaway is that the "twin paradox" near Earth has *two* contributions of similar size and opposite sign: the kinematic (special-relativistic) slowing of a fast clock, and the gravitational (general-relativistic) speeding of a high clock. Get one without the other and you predict the wrong answer — even the wrong sign, as the eastward/westward asymmetry shows. The trigger to watch for: any precision-timing comparison involving altitude (aircraft, satellites, mountaintops) requires *both* the velocity term $-v^2/2c^2$ and the potential term $+\Phi/c^2$. This is the first place in the special-relativity curriculum where general relativity becomes unavoidable, and it previews [[Special Relativity XXV — Toward Relativistic Gravitation|the bridge to gravitation]]: the same metric arc-length integral, now in a position-dependent metric $g_{00}(x) = 1 + 2\Phi/c^2$, governs both effects at once.

**On a rotating planet, both twins move — choose a non-rotating frame.** The subtlety that makes Hafele–Keating richer than the idealised twin paradox is that the "stay-at-home" ground clock co-rotates with the Earth, so it is not inertial and not at rest in any natural frame. The correct bookkeeping uses a non-rotating, Earth-centred frame in which *neither* clock is at rest, and the proper-time difference depends on the *difference* of their speeds — which is why eastward (plane faster than ground) and westward (plane slower than ground) give opposite signs. The general diagnostic for any rotating-frame timing problem: do not privilege the "ground" as inertial; transform to a genuinely non-rotating frame, account for every clock's motion there, and only then compare proper times. This same care is what [[Special Relativity XVII — Rotating Observers|rotating-observer problems]] demand, and it is the practical face of the principle that proper time is computed along *each* worldline in a common inertial frame, never by declaring one observer privileged. See [[Ex - The ideal clock hypothesis and a circular-motion clock]] for why atomic clocks track proper time despite acceleration, and [[Ex - A round trip to the galactic centre]] for the same proper-time geometry at astronomical scale.
