---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gravitational Redshift"
  - "Def - Time Dilation"
  - "Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity"
tags: [physics, special-relativity]
---

# Problem Statement

The Global Positioning System (GPS) is the one piece of everyday technology that does not work without relativity. A GPS receiver determines its position by measuring the arrival times of timing signals from at least four satellites and solving for $(t, x, y, z)$. Timing errors of $\sim 30\,\mathrm{ns}$ correspond to position errors of $\sim 10\,\mathrm{m}$ (the speed of light gap), so GPS satellite clocks must be synchronised with the ground-frame clocks to nanosecond precision over years of operation. This requires correcting for both special and general relativistic effects.

Take GPS satellites at orbital radius $r_{\mathrm{sat}} = 2.66\times 10^4\,\mathrm{km}$ (measured from Earth's centre), with orbital speed $v_{\mathrm{sat}} = 3.87\,\mathrm{km\,s^{-1}}$. Take Earth's radius $R_\oplus = 6.378\times 10^3\,\mathrm{km}$, mass $M_\oplus = 5.972\times 10^{24}\,\mathrm{kg}$, surface gravity $g = 9.81\,\mathrm{m\,s^{-2}}$, with $GM_\oplus = 3.986\times 10^{14}\,\mathrm{m^3\,s^{-2}}$.

1. *Kinematic time dilation.* Compute the fractional rate at which a satellite clock runs slow due to its orbital speed, $\Delta\nu/\nu = -v_{\mathrm{sat}}^2/(2c^2)$, and convert to seconds-per-day.

2. *Gravitational redshift.* The satellite is at a higher gravitational potential than the ground clock (less negative $\Phi$). Compute the fractional rate at which the satellite clock runs *fast* due to the redshift:
$$\frac{\Delta\nu}{\nu}\bigg|_{\mathrm{grav}} = +\frac{GM_\oplus}{c^2}\left(\frac{1}{R_\oplus} - \frac{1}{r_{\mathrm{sat}}}\right),$$
and convert to seconds-per-day.

3. *Net offset.* Combine: the *net* satellite clock rate is $\Delta\nu/\nu = +\Delta\nu_{\mathrm{grav}}/\nu - \Delta\nu_{\mathrm{kin}}/\nu$. Compute and compare with the standard quoted value of $+38.6\,\mu\mathrm{s/day}$.

4. *Frequency offset of the onboard clocks.* GPS satellites carry cesium and rubidium atomic clocks tuned on the ground to nominal frequency $10.23\,\mathrm{MHz}$. To make them tick at the ground-frame nominal rate when in orbit, they are *deliberately mis-tuned* on the ground by a fractional offset. Compute the offset $\Delta f / f$, and verify it matches the official GPS specification of $\Delta f/f = -4.46\times 10^{-10}$ (satellite clocks tuned to run slow on the ground, so they run on-spec in orbit).

5. *Cost of ignoring relativity.* If the corrections were not applied, the satellite clocks would drift by the rate computed in part 3. Compute the cumulative timing error after one day, and convert to a position error (via $\Delta x = c\,\Delta t$). Compare with GPS specifications of $\sim 10\,\mathrm{m}$ accuracy.

**Recall:**

![[Thm - Gravitational Redshift#Statement]]

A clock at height $h$ above the Earth's surface runs *fast* relative to a surface clock by $\Delta\nu/\nu_{\mathrm{grav}} = +gh/c^2$ for small $h$. For the larger height of a GPS orbit, use the full potential difference between the two altitudes, $\Delta\Phi = GM_\oplus(1/R_\oplus - 1/r_{\mathrm{sat}})$ (Earth's surface deeper in the potential).

A clock moving at speed $v$ relative to the ground runs *slow* by special-relativistic time dilation: $\Delta\nu/\nu_{\mathrm{kin}} = -v^2/(2c^2)$ to leading order in $v/c$.

Both effects are present for a GPS satellite — they have *opposite signs* and the gravitational effect wins by about $6\times$. This is the one everyday system where the relativistic correction is dominated by gravity, not by special-relativistic kinematics.

---

# Convergent Strategy

**Problem class.** A *numerical exercise in combined SR + GR clock corrections*, with the punchline that without both relativity corrections GPS would be useless within hours.

**Assumption pattern.** Two effects: (i) kinematic time dilation, slowing the satellite clock, computed from the orbital speed; (ii) gravitational redshift, speeding the satellite clock, computed from the potential difference. They have opposite signs and must be added carefully. Both are first-order in the relevant small parameters ($v^2/c^2$ and $\Phi/c^2$), so linear superposition applies.

**Theorem routing.** Part 1 uses the special-relativistic time-dilation formula at quadratic order in $v/c$. Part 2 uses the gravitational-redshift formula with $\Delta\Phi = GM_\oplus(1/R_\oplus - 1/r_{\mathrm{sat}})$. Part 3 combines them with the correct sign convention. Part 4 inverts the convention to specify how the clocks are mis-tuned. Part 5 propagates the error to position accuracy.

**Key decision point.** The crux is the sign convention: the gravitational effect makes the satellite clock fast (because the satellite is higher), the kinematic effect makes it slow (because the satellite moves). Net: satellite runs fast, and the on-board frequency must be reduced. Subtraction of the two with correct signs is the only nontrivial bookkeeping in the exercise; the rest is plugging in numbers.

---

# Legal Operations Used

1. **Derive the redshift from the accelerated-frame spectral shift** (operation 6 from the topic page): part 2 uses the gravitational-potential form of the redshift between satellite and ground.

2. **Take the Newtonian (weak, slow) limit** (operation 1 from the topic page): both effects are computed to leading order in $v^2/c^2$ and $\Phi/c^2$, valid for GPS parameters ($v/c \sim 10^{-5}$, $\Phi/c^2 \sim 10^{-9}$).

3. **Invoke the equivalence principle to swap a gravitational field for an accelerated frame** (operation 2 from the topic page): justifies the use of the redshift formula in the Earth's static field.

---

# Hints

> [!note]- Hint 1
> $v_{\mathrm{sat}} = 3.87\,\mathrm{km\,s^{-1}} = 3.87\times 10^3\,\mathrm{m\,s^{-1}}$, $c = 3\times 10^8\,\mathrm{m\,s^{-1}}$. So $v^2/(2c^2) = (3.87\times 10^3)^2/(2\times 9\times 10^{16}) \approx 1.50\times 10^7/(1.8\times 10^{17}) \approx 8.3\times 10^{-11}$. In seconds per day ($86400\,\mathrm{s}$): $\Delta t = 8.3\times 10^{-11}\times 86400 \approx 7.2\,\mu\mathrm{s}$. So the orbital motion slows the satellite clock by $\approx 7.2\,\mu\mathrm{s/day}$.

> [!note]- Hint 2
> $GM_\oplus = 3.986\times 10^{14}\,\mathrm{m^3\,s^{-2}}$. Potential difference: $\Delta\Phi/c^2 = (GM_\oplus/c^2)\,(1/R_\oplus - 1/r_{\mathrm{sat}}) = (3.986\times 10^{14}/(9\times 10^{16}))\,(1/(6.378\times 10^6) - 1/(2.66\times 10^7))$. Compute: $GM/c^2 \approx 4.43\times 10^{-3}\,\mathrm{m}$ (Earth's "gravitational radius"). Then $1/R_\oplus \approx 1.568\times 10^{-7}\,\mathrm{m}^{-1}$, $1/r_{\mathrm{sat}} \approx 3.759\times 10^{-8}\,\mathrm{m}^{-1}$, difference $\approx 1.192\times 10^{-7}\,\mathrm{m}^{-1}$. Product: $\Delta\Phi/c^2 \approx 4.43\times 10^{-3}\times 1.192\times 10^{-7} \approx 5.28\times 10^{-10}$. In sec/day: $5.28\times 10^{-10}\times 86400 \approx 45.6\,\mu\mathrm{s/day}$. Satellite clock runs fast by $\approx 45.6\,\mu\mathrm{s/day}$.

> [!note]- Hint 3
> Net: $+45.6 - 7.2 = +38.4\,\mu\mathrm{s/day}$. The satellite clock runs *fast* by about $38.4\,\mu\mathrm{s/day}$. Standard quoted: $38.6\,\mu\mathrm{s/day}$ (matches to rounding).

> [!note]- Hint 4
> To make the satellite clock tick at the ground-frame nominal $10.23\,\mathrm{MHz}$ when in orbit, the ground-tuned frequency must be reduced by the net fractional rate: $\Delta f/f = -(+5.28\times 10^{-10} - 8.3\times 10^{-11}) = -4.45\times 10^{-10}$. The factory specification is $\Delta f/f = -4.4647\times 10^{-10}$ (or equivalently $\Delta f = -4.567\times 10^{-3}\,\mathrm{Hz}$ at $10.23\,\mathrm{MHz}$). Match: yes, to the second decimal place.

> [!note]- Hint 5
> One day of uncorrected drift: $\Delta t \approx 38.6\,\mu\mathrm{s} = 3.86\times 10^{-5}\,\mathrm{s}$. Position error: $\Delta x = c\Delta t = 3\times 10^8 \times 3.86\times 10^{-5} = 1.158\times 10^4\,\mathrm{m} \approx 11.6\,\mathrm{km}$. After one day of uncorrected operation the position error is $\sim 10\,\mathrm{km}$, completely useless. Standard quote: $\sim 14\,\mathrm{km/day}$, in agreement with this within rounding (different sources use slightly different orbital parameters).

---

# Solution

This exercise is a computational closure on the chapter: it takes the abstract framework — kinematic time dilation, gravitational redshift, the equivalence principle — and uses it to compute the *one everyday technology* that fails without relativity. The numbers are striking: ignoring relativity means accumulating $\sim 12\,\mathrm{km/day}$ of position error, and the dominant correction is *gravitational*, not kinematic. GPS is gravitational physics applied at the centimetre scale.

**Step 1: Kinematic time dilation.**

> [!note]- Derivation
> A clock moving at speed $v$ in some inertial frame runs slow relative to the frame's clocks by the special-relativistic time-dilation factor $\Gamma = (1 - v^2/c^2)^{-1/2}$. For $v \ll c$, expand:
> $$\frac{1}{\Gamma} = \sqrt{1 - v^2/c^2} \approx 1 - \frac{v^2}{2c^2}.$$
> So $d\tau_{\mathrm{sat}}/dt_{\mathrm{ground}} = 1/\Gamma \approx 1 - v_{\mathrm{sat}}^2/(2c^2)$.
> In fractional frequency:
> $$\frac{\Delta\nu}{\nu}\bigg|_{\mathrm{kin}} = -\frac{v_{\mathrm{sat}}^2}{2c^2}.$$
> Plug in $v_{\mathrm{sat}} = 3.87\,\mathrm{km\,s^{-1}} = 3870\,\mathrm{m\,s^{-1}}$:
> $$\frac{v_{\mathrm{sat}}^2}{2c^2} = \frac{(3870)^2}{2\,(3\times 10^8)^2} = \frac{1.498\times 10^7}{1.8\times 10^{17}} = 8.32\times 10^{-11}.$$
> Over one day ($86400\,\mathrm{s}$):
> $$\Delta\tau_{\mathrm{kin}} = -8.32\times 10^{-11}\times 86400\,\mathrm{s} \approx -7.19\,\mu\mathrm{s/day}.$$
> The satellite clock runs *slow* by about $7.2\,\mu\mathrm{s/day}$ due to its orbital motion. This is a standard SR effect: a moving clock ticks slower as seen from a stationary frame.

**Step 2: Gravitational redshift.**

> [!note]- Derivation
> A clock at gravitational potential $\Phi_{\mathrm{sat}}$ (satellite) compared to one at potential $\Phi_{\mathrm{gnd}}$ (ground) runs *fast* by the fractional rate (linearised redshift):
> $$\frac{\Delta\nu}{\nu}\bigg|_{\mathrm{grav}} = +\frac{\Phi_{\mathrm{sat}} - \Phi_{\mathrm{gnd}}}{c^2}.$$
> For Earth's gravitational potential $\Phi(r) = -GM_\oplus/r$:
> $$\Phi_{\mathrm{sat}} - \Phi_{\mathrm{gnd}} = -GM_\oplus\left(\frac{1}{r_{\mathrm{sat}}} - \frac{1}{R_\oplus}\right) = GM_\oplus\left(\frac{1}{R_\oplus} - \frac{1}{r_{\mathrm{sat}}}\right) > 0.$$
> Plug in $GM_\oplus = 3.986\times 10^{14}\,\mathrm{m^3\,s^{-2}}$, $R_\oplus = 6.378\times 10^6\,\mathrm{m}$, $r_{\mathrm{sat}} = 2.66\times 10^7\,\mathrm{m}$:
> $$\frac{1}{R_\oplus} = 1.568\times 10^{-7}\,\mathrm{m}^{-1}, \quad \frac{1}{r_{\mathrm{sat}}} = 3.759\times 10^{-8}\,\mathrm{m}^{-1}, \quad \text{difference} = 1.192\times 10^{-7}\,\mathrm{m}^{-1}.$$
> $$\frac{\Delta\Phi}{c^2} = \frac{3.986\times 10^{14}\times 1.192\times 10^{-7}}{(3\times 10^8)^2} = \frac{4.751\times 10^{7}}{9\times 10^{16}} = 5.28\times 10^{-10}.$$
> Over one day:
> $$\Delta\tau_{\mathrm{grav}} = +5.28\times 10^{-10}\times 86400\,\mathrm{s} \approx +45.6\,\mu\mathrm{s/day}.$$
> The satellite clock runs *fast* by about $45.6\,\mu\mathrm{s/day}$ because it is higher in the Earth's potential.

**Step 3: Net offset.**

> [!note]- Derivation
> Total satellite clock rate compared to ground:
> $$\frac{\Delta\nu}{\nu}\bigg|_{\mathrm{net}} = +\frac{\Delta\Phi}{c^2} - \frac{v_{\mathrm{sat}}^2}{2c^2} = +5.28\times 10^{-10} - 8.32\times 10^{-11} = +4.45\times 10^{-10}.$$
> In sec/day:
> $$\Delta\tau_{\mathrm{net}} = +4.45\times 10^{-10}\times 86400\,\mathrm{s} \approx +38.4\,\mu\mathrm{s/day}.$$
> So *uncorrected, a GPS satellite clock would run fast by about $38\,\mu\mathrm{s/day}$ relative to a ground clock*. The standard GPS-system value (using slightly more precise orbital and Earth parameters) is $+38.6\,\mu\mathrm{s/day}$, in excellent agreement.
>
> *Sign and ratio.* The two effects work in opposite directions: the orbital motion slows the satellite clock (SR), the higher gravity speeds it up (GR). The gravitational effect dominates by a factor of about $5.5\times$ — so the satellite ends up running fast on net. This is the *only* commonly cited example in technology where the gravitational time effect dominates the kinematic one.

**Step 4: Frequency offset of the onboard clocks.**

> [!note]- Derivation
> To make the satellite clock tick at the ground-frame nominal $f_0 = 10.23\,\mathrm{MHz}$ when in orbit, it must be *deliberately mis-tuned* on the ground so that, after the $+4.45\times 10^{-10}$ orbital rate, it lands at $f_0$. The required ground frequency:
> $$f_{\mathrm{ground}} = f_0\cdot(1 - 4.45\times 10^{-10}) = 10.23\,\mathrm{MHz}\,(1 - 4.45\times 10^{-10}).$$
> Equivalently, the fractional offset is $\Delta f / f = -4.45\times 10^{-10}$, with $\Delta f = -10.23\times 10^6\times 4.45\times 10^{-10} = -4.55\times 10^{-3}\,\mathrm{Hz} \approx -4.55\,\mathrm{mHz}$.
>
> *Official specification.* The GPS Interface Specification (ICD-GPS-200) specifies the satellite onboard clock frequency offset as $\Delta f/f = -4.4647\times 10^{-10}$, equivalently $\Delta f = -4.567\times 10^{-3}\,\mathrm{Hz}$ at $10.23\,\mathrm{MHz}$. (The specification uses more precise values for $v_{\mathrm{sat}}$, $r_{\mathrm{sat}}$, and treats the orbit as elliptical rather than circular, but the leading number is the one this exercise reproduces.)
>
> Our $-4.45\times 10^{-10}$ matches to better than $0.4\%$. *The number that appears on the factory floor for a GPS satellite atomic clock is the one this exercise computes.*

**Step 5: Cost of ignoring relativity.**

> [!note]- Derivation
> Without the offset correction, the satellite clock drifts at $+38.4\,\mu\mathrm{s/day}$. Over $1\,\mathrm{day}$ of uncorrected operation:
> $$\Delta t = 38.4\,\mu\mathrm{s} = 3.84\times 10^{-5}\,\mathrm{s}.$$
> Position error via $\Delta x = c\Delta t$:
> $$\Delta x = (3\times 10^8\,\mathrm{m\,s^{-1}})\times(3.84\times 10^{-5}\,\mathrm{s}) = 1.152\times 10^4\,\mathrm{m} \approx 11.5\,\mathrm{km}.$$
> So after just one day of operation without relativity corrections, a GPS receiver would be off by $\sim 11\,\mathrm{km}$. The standard quoted value (e.g., Ashby 2003) is $\sim 14\,\mathrm{km/day}$, using slightly more precise system parameters.
>
> GPS specifications require $\sim 10\,\mathrm{m}$ accuracy. Without relativity, this would be exceeded within
> $$\Delta t_{\mathrm{threshold}} = \frac{10\,\mathrm{m}/(3\times 10^8\,\mathrm{m\,s^{-1}})}{4.45\times 10^{-10}} \approx \frac{3.3\times 10^{-8}}{4.45\times 10^{-10}} = 75\,\mathrm{s} \approx 1\,\mathrm{minute}.$$
> **A GPS receiver would be useless within one minute of activation if relativity were ignored.** This is why GPS is the standard example of "everyday relativity" — it is the one technology in which the corrections are not academic.
>
> *Other relativistic corrections in GPS.* Additional refinements include: the eccentricity of satellite orbits (causing periodic variations), the Sagnac effect (Earth's rotation affecting signal arrival times in the rotating ECEF frame), the gravitational frequency shift between satellites of differing altitudes due to orbital eccentricity, and higher-order $(v/c)^4$ corrections for the most precise applications. All are second-order to the leading effects computed above, but together they push GPS-style techniques (and the related VLBI, lunar laser ranging) toward $\mathrm{nm}$ and $\mathrm{ns}$ precision.

> [!note]- Complete formal solution
> (1) Kinematic time dilation: $\Delta\nu/\nu|_{\mathrm{kin}} = -v_{\mathrm{sat}}^2/(2c^2)$. With $v_{\mathrm{sat}} = 3.87\,\mathrm{km\,s^{-1}}$, $\Delta\nu/\nu = -8.32\times 10^{-11}$, equivalent to $-7.2\,\mu\mathrm{s/day}$ (satellite clock runs slow). (2) Gravitational redshift: $\Delta\nu/\nu|_{\mathrm{grav}} = +GM_\oplus(1/R_\oplus - 1/r_{\mathrm{sat}})/c^2$. With given parameters, $\Delta\nu/\nu = +5.28\times 10^{-10}$, equivalent to $+45.6\,\mu\mathrm{s/day}$ (satellite clock runs fast). (3) Net: $+4.45\times 10^{-10}$ ($\approx +38.4\,\mu\mathrm{s/day}$), matching standard quote $+38.6\,\mu\mathrm{s/day}$ to rounding. Gravitational effect dominates kinematic by $\sim 5.5\times$. (4) Onboard clock frequency offset: $\Delta f/f = -4.45\times 10^{-10}$, giving $\Delta f \approx -4.55\,\mathrm{mHz}$ at $10.23\,\mathrm{MHz}$; matches GPS specification $-4.4647\times 10^{-10}$ to $0.4\%$. (5) Uncorrected position error: $\Delta x = c\Delta t = 11.5\,\mathrm{km}/\mathrm{day}$ (vs $\sim 14\,\mathrm{km/day}$ standard). Required GPS accuracy of $\sim 10\,\mathrm{m}$ would be exceeded after $\sim 1\,\mathrm{minute}$. *GPS is the one everyday technology in which relativity is operationally indispensable, and the dominant correction is the gravitational redshift — special relativity's correction is six times smaller and has the opposite sign.* $\blacksquare$

---

# Key Takeaways

**GPS is the everyday technology in which gravity *dominates* the relativistic correction over kinematic time dilation, by a factor of $\sim 6$.** The most striking lesson of the exercise is the relative size of the two relativistic corrections: kinematic time dilation slows the satellite clock by $\sim 7\,\mu\mathrm{s/day}$, while the gravitational redshift speeds it up by $\sim 46\,\mu\mathrm{s/day}$. Most popular accounts emphasise special relativity as "the" surprising correction to clocks, but for GPS the gravitational correction is the dominant one, and is *opposite in sign*. This is geometrically the assertion that the satellite is higher in the Earth's gravitational potential well, so its clock runs faster, while its orbital motion makes it run slower — and the altitude effect wins. The reusable lesson, beyond the GPS specifics: for any clock-comparison problem involving altitude and motion, both effects must be tracked, and which one dominates depends on the specifics of the geometry — for a low-altitude fast-moving system, kinematics may win; for a high-altitude slow system, gravity does. The fact that GPS clocks are *deliberately mis-tuned by $-4.5\times 10^{-10}$ at the factory* to compensate for these effects is the smoking gun: relativity is built into the engineering specifications.

**Without relativity, GPS would accumulate $\sim 12\,\mathrm{km/day}$ of position error — and would fail its $10\,\mathrm{m}$ spec within one minute.** The numerical takeaway: a $4.5\times 10^{-10}$ clock rate error, integrated over a day, gives a $38\,\mu\mathrm{s}$ time error and an $11\,\mathrm{km}$ position error via the light-speed conversion. This is the single most often-cited operational consequence of general relativity, and it is the easiest one to verify: GPS *works*, to the $\sim 10\,\mathrm{m}$ accuracy it claims, only because both special and general relativistic corrections are applied. The propagation of error is also illuminating — a millisecond timing error becomes a $300\,\mathrm{km}$ position error, so the precision constraints on GPS clocks are extreme ($10\,\mathrm{m}$ accuracy demands $30\,\mathrm{ns}$ timing precision over years). Atomic clocks meet this; quartz oscillators do not. The reusable principle: any precision time-and-distance system must trace its error propagation through $\Delta x = c\Delta t$, and once this conversion factor is appreciated, the case for relativity in such systems becomes immediate — a difference of a part per billion in clock rate, accumulated over a day, is meters of position error, exactly the threshold of usability.

**The gravitational redshift is the same physics throughout — from Pound-Rebka in a $22\,\mathrm{m}$ tower to GPS at $20{,}000\,\mathrm{km}$ altitude.** The deep structural lesson is the *universality* of the gravitational time effect: the same formula $\Delta\nu/\nu = -\Delta\Phi/c^2$ that quantitatively explains Pound-Rebka (over $22\,\mathrm{m}$, $\Delta\nu/\nu \sim 10^{-15}$) also predicts GPS clock rates (over $20{,}000\,\mathrm{km}$, $\Delta\nu/\nu \sim 10^{-10}$) to part-per-thousand precision. From laboratory tower to satellite orbit, the equivalence principle and its redshift consequence apply uniformly, with only the value of $\Delta\Phi$ changing. This is the practical face of the universality the chapter has emphasised: gravity's coupling to *all* energy-momentum (via its trace, or via the metric in general relativity) means the redshift applies to *any* clock, of any composition, anywhere — atomic, mechanical, gamma-ray, GPS — with the same factor $-\Delta\Phi/c^2$. There is no clock anywhere on or above Earth's surface that is immune to gravitational time dilation, and modern atomic clocks ($10^{-17}$ precision) have made it possible to *measure* the redshift over a $30\,\mathrm{cm}$ height difference — chronometric levelling using clocks as relativistic altimeters. The reusable thread: the gravitational redshift is the single most pervasive prediction of general relativity in technology, and its universality is exactly what makes gravity geometrisable; every other interaction would require species-specific corrections.
