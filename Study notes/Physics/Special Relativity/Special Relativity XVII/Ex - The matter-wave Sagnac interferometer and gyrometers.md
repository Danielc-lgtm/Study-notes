---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Sagnac Delay and the Optical Sagnac Interferometer"
  - "Thm - The Sagnac Effect"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$ where convenient, restoring $c$ in final answers:

1. From the Sagnac delay $\Delta t' = 4\omega A/c^2$, derive the optical interferometer phase shift $\Delta\phi = (8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$, and evaluate it for Sagnac's 1913 experiment ($\lambda = 436$ nm, $\omega/2\pi = 2$ Hz, $A = 0.0866\,\text{m}^2$).
2. Derive the matter-wave phase shift $\Delta\phi = 4\Gamma_p(m/\hbar)\vec\omega\cdot\vec{\mathcal{A}}$ from the de Broglie frequency, and compute the ratio $\Delta\phi_{\text{mat}}/\Delta\phi_{\text{opt}}$ for a proton and visible light.
3. Explain why the aether theory predicts the *same* optical Sagnac effect as relativity but *no* matter-wave effect, so that the matter-wave Sagnac effect confirms relativity over the aether.
4. Explain the operating principle of (a) the fibre-optic gyrometer and (b) the ring-laser gyrometer, and why they have displaced mechanical gyroscopes in inertial navigation.

**Recall:**

![[Thm - Sagnac Delay and the Optical Sagnac Interferometer#Statement]]

The [[Thm - The Sagnac Effect|Sagnac delay]] is $\Delta t' = 4\omega A/c^2$ for a circular loop of enclosed area $A$, independent of the signal speed. The phase of a wave of frequency $f$ accumulated over a time $t$ is $2\pi f t$; the Planck–Einstein relation gives a particle's de Broglie frequency as $f = E/h$ with $E = \Gamma_p mc^2$ its relativistic energy.

---

# Convergent Strategy

**Problem class.** A *convert-delay-to-observable-and-interpret* problem capping §17.3. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]]: multiply the delay by the wave's angular frequency to get the phase; for matter waves use the de Broglie frequency.

**Assumption pattern.** A wave (light or matter) split and recombined around a rotating loop. The signpost is "interference fringes from counter-propagating waves on a rotating platform": the fringe shift is $2\pi f$ times the Sagnac delay, and the matter-wave frequency (the de Broglie frequency) is enormous, giving a huge enhancement.

**Theorem routing.** Part 1 multiplies the delay by $2\pi f = 2\pi c/\lambda$ ([[Thm - Sagnac Delay and the Optical Sagnac Interferometer]]); part 2 substitutes $f = \Gamma_p mc^2/h$; part 3 contrasts the aether and relativistic predictions; part 4 applies the formula to gyrometer designs.

**Key decision point.** The crux in part 2 is using the *radiation frequency* $f = \Gamma_p mc^2/h$, keeping the metric $c^2$ in the delay — *not* replacing the metric $c^2$ by the particle's phase velocity. The natural but wrong move is to write the formula "in terms of wave speed and wavelength" and substitute the matter-wave phase velocity, corrupting the metric $c^2$. The non-obvious recognition is that the speed-independence of the delay forces this discipline.

---

# Legal Operations Used

1. **Operation 9 from the topic page (Planck–Einstein relation for matter waves).** The matter-wave frequency is the de Broglie frequency $f = \Gamma_p mc^2/h$, giving the enhanced phase.

2. **Operation 8 from the topic page (equal signal speeds, metric origin of $c^2$).** The speed-independence of the delay means the $c^2$ is metric; for matter waves it must not be replaced by the phase velocity.

3. **Operation 5 from the topic page (the area-proportional form).** Both phases are $\propto\vec\omega\cdot\vec{\mathcal{A}}$, the enclosed vorticity flux; winding $N$ loops multiplies the area.

---

# Hints

> [!note]- Hint 1
> The phase shift is $\Delta\phi = 2\pi f\,\Delta t'$ with $\Delta t' = 4\omega A/c^2$ and $f = c/\lambda$ for light. So $\Delta\phi = 2\pi(c/\lambda)(4\omega A/c^2) = 8\pi\omega A/(c\lambda)$. For Sagnac's numbers, $\omega = 2\pi\cdot 2 = 4\pi$ rad/s, $A = 0.0866$ m², $\lambda = 436$ nm, $c = 3\times10^8$ m/s.

> [!note]- Hint 2
> For matter waves, replace $f = c/\lambda$ by the de Broglie frequency $f = E/h = \Gamma_p mc^2/h$. Then $\Delta\phi = 2\pi(\Gamma_p mc^2/h)(4\omega A/c^2) = 8\pi\Gamma_p m\omega A/h = 4\Gamma_p(m/\hbar)\omega A$ (using $\hbar = h/2\pi$). The metric $c^2$ from the delay cancels the $c^2$ in $E$, leaving no $c$ — and no phase velocity.

> [!note]- Hint 3
> The aether theory says light moves at $c$ relative to the aether (not the emitter), which for the *optical* Sagnac effect gives the same $r\Omega_\pm = c$ result and hence the same delay. But for *massive* particles, the aether theory predicts the particle speed adds Galileanly to the rim speed, with no relativistic correction — and the resulting delay vanishes (no Sagnac effect for matter in the aether picture). Relativity predicts the same $\propto\omega A$ effect for matter as for light.

> [!note]- Hint 4
> (a) A fibre-optic gyrometer winds the light path $N$ times through a fibre coil, multiplying the enclosed area (hence the phase) by $N$. (b) A ring-laser gyrometer uses an annular laser cavity where rotation splits the resonant frequencies of the clockwise and counter-clockwise modes; the beat frequency measures $\omega$. Both have no moving parts.

---

# Solution

The route has four steps. Step 1 gives the optical phase and Sagnac's tiny $0.21$ rad. Step 2 gives the matter-wave phase, enhanced by $\sim 10^8$. Step 3 contrasts aether and relativity, showing matter waves discriminate. Step 4 describes the two gyrometer types. The non-obvious move is the disciplined use of the radiation frequency in Step 2, keeping the metric $c^2$ intact.

**Step 1: The optical phase is $\Delta\phi = 8\pi\omega A/(c\lambda)$; Sagnac measured $\approx 0.21$ rad.**

> [!note]- Derivation
> A wave of frequency $f$ returning with a time difference $\Delta t'$ between its two halves has a phase difference $\Delta\phi = 2\pi f\,\Delta t'$. With the [[Thm - The Sagnac Effect|Sagnac delay]] $\Delta t' = 4\omega A/c^2$ and $f = c/\lambda$ for light,
> $$\Delta\phi = 2\pi\frac{c}{\lambda}\cdot\frac{4\omega A}{c^2} = \frac{8\pi\omega A}{c\lambda} = \frac{8\pi}{c\lambda}\vec\omega\cdot\vec{\mathcal{A}}.$$
> For Sagnac's 1913 experiment, $\omega = 2\pi\times 2\,\text{Hz} = 4\pi\,\text{rad/s}$, $A = 0.0866\,\text{m}^2$, $\lambda = 436\,\text{nm} = 4.36\times10^{-7}\,\text{m}$, $c = 3.00\times10^8\,\text{m/s}$:
> $$\Delta\phi = \frac{8\pi\times 4\pi\times 0.0866}{3.00\times10^8\times 4.36\times10^{-7}} \approx \frac{8.6}{131} \approx 0.21\,\text{rad}.$$
> This tiny but measurable fringe shift is what Sagnac observed, with about 4% accuracy.

**Step 2: The matter-wave phase is $\Delta\phi = 4\Gamma_p(m/\hbar)\omega A$, enhanced by $\sim 10^8$.**

> [!note]- Derivation
> For a de Broglie wave the relevant frequency is the Planck–Einstein frequency $f = E/h$, with $E = \Gamma_p mc^2$ the particle's relativistic energy relative to the corotating mirror. Substituting into $\Delta\phi = 2\pi f\,\Delta t'$:
> $$\Delta\phi = 2\pi\frac{\Gamma_p mc^2}{h}\cdot\frac{4\omega A}{c^2} = \frac{8\pi\Gamma_p m\omega A}{h} = 4\Gamma_p\frac{m}{\hbar}\vec\omega\cdot\vec{\mathcal{A}},$$
> using $\hbar = h/2\pi$. The metric $c^2$ from the delay has cancelled the $c^2$ in $E = \Gamma_p mc^2$, leaving a result with *no* $c$ — confirming one must use the *frequency*, not the phase velocity (a careless substitution of the phase velocity for the metric $c$ would corrupt this). The ratio to the optical phase, for the same $\omega$ and $A$, is
> $$\frac{\Delta\phi_{\text{mat}}}{\Delta\phi_{\text{opt}}} = \frac{\Gamma_p mc^2/h}{c/\lambda} = \frac{\Gamma_p mc^2}{hf} = \frac{\Gamma_p mc^2}{hc/\lambda}.$$
> For a proton ($mc^2\approx 0.94\,\text{GeV}$), $\Gamma_p\approx 1$, and visible light ($hf\approx 2\,\text{eV}$):
> $$\frac{\Delta\phi_{\text{mat}}}{\Delta\phi_{\text{opt}}} \approx \frac{0.94\times10^9}{2} \approx 4\times10^8.$$
> The matter-wave phase is some $10^8$ times larger, making matter-wave interferometers vastly more sensitive rotation sensors.

**Step 3: Matter waves discriminate relativity from the aether.**

> [!note]- Derivation
> The aether theory predicts that light moves at speed $c$ relative to the *aether*, not the emitter. For the optical Sagnac effect this gives the same inertial signal speed ($r\Omega_\pm = c$) as relativity, and hence the *same* delay $4\omega A/c^2$ — the optical Sagnac effect was in fact predicted within the aether theory (Lodge, 1893) and cannot distinguish the two frameworks. But for *massive* particles the aether theory predicts Galilean velocity addition: the particle speed adds to the rim speed with no relativistic correction, $v_\pm = c_{\text{part}}\mp r\omega$ relative to the aether, and substituting into the (nonrelativistic-limit) delay formula gives $\Delta t' = 0$ — *no* Sagnac effect for matter. Relativity, by contrast, predicts the same $\propto\omega A$ delay for matter as for light, because the delay is metric (independent of signal speed). Therefore the observed matter-wave Sagnac effect — first seen by Zimmerman and Mercereau in 1965 with superconducting electrons, and since with neutrons and atoms — is a confirmation of relativity that the aether theory cannot reproduce. (As Prunier noted in 1935, this is precisely why the matter-wave Sagnac effect is decisive where the optical one is not.)

**Step 4: Fibre-optic and ring-laser gyrometers.**

> [!note]- Derivation
> **(a) Fibre-optic gyrometer.** Light from a laser is split, sent both ways through a coil of optical fibre wound $N$ times (total length up to several kilometres), and recombined. Winding the path $N$ times multiplies the enclosed area, so the phase is $N$ times the single-loop value: $\Delta\phi = N(8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$. The long path makes small rotations measurable.
>
> **(b) Ring-laser gyrometer (gyrolaser).** An annular laser cavity (typically helium–neon) supports clockwise and counter-clockwise lasing modes. Rotation makes their effective path lengths, and hence their resonant frequencies, differ by an amount proportional to $\omega$; the beat between the two modes is measured directly as a frequency, $\Delta\nu\propto\omega A/(\lambda L)$ ($L$ the perimeter). This is a frequency readout rather than a fringe count, giving high precision.
>
> **Why they displaced mechanical gyroscopes.** Both have *no moving parts*: there is no spinning mass to wear out, no bearings to introduce friction, and no mechanical drift. They are light, compact, robust, and turn on instantly. Combined with accelerometers, they form the rotation-sensing core of inertial navigation systems in aircraft, ships, submarines, missiles, and spacecraft, allowing dead-reckoning navigation with no external reference. The optical gyrometers dominate the industrial market; matter-wave gyrometers, though far more sensitive, require accelerators (neutrons) or ultra-cold atoms and remain laboratory instruments.

> [!note]- Complete formal solution
> The optical phase is $\Delta\phi = 2\pi f\Delta t' = (8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$; Sagnac's numbers give $\approx 0.21$ rad. The matter-wave phase, using the de Broglie frequency $f = \Gamma_p mc^2/h$, is $\Delta\phi = 4\Gamma_p(m/\hbar)\vec\omega\cdot\vec{\mathcal{A}}$, larger by $\Gamma_p mc^2/hf\sim 4\times10^8$ for a proton and visible light (the metric $c^2$ cancels, so no phase velocity enters). The aether theory reproduces the optical effect (light at $c$ relative to aether) but predicts no matter-wave effect (Galilean addition gives zero), so the matter-wave Sagnac effect confirms relativity. Fibre-optic gyrometers wind $N$ loops to multiply the area; ring-laser gyrometers read the frequency split of counter-propagating cavity modes; both, lacking moving parts, have displaced mechanical gyroscopes in inertial navigation. $\blacksquare$

---

# Key Takeaways

**Use the radiation frequency, keep the metric $c^2$ — the speed-independence of the delay enforces this discipline.** Converting the Sagnac delay to a phase requires multiplying by the *radiation frequency* $f$ (which for light is $c/\lambda$ but for matter is the de Broglie frequency $\Gamma_p mc^2/h$), while the $c^2$ in the delay stays the *metric* factor and must never be replaced by the wave's phase velocity. The trigger is any matter-wave version of a relativistic formula derived for light: do not naively substitute the particle's speed for $c$, because the $c$'s have different origins (some metric, some propagation). Here the metric $c^2$ from the delay cancels the $c^2$ in the particle energy, leaving a result with no $c$ at all — and a careless substitution would corrupt this by $(c/v)^2$. The discipline is a direct consequence of the Sagnac effect's speed-independence: the delay is geometric, so the only place propagation enters is through the relation $f = c/\lambda$ for light specifically, which has no analogue for the metric $c^2$.

**Matter waves are $\sim 10^8$ times more sensitive because rest energy dwarfs photon energy — and this is what beats the aether.** The matter-wave Sagnac phase exceeds the optical phase by $\Gamma_p mc^2/hf$, the ratio of the particle's rest energy to an optical photon's energy, which is $\sim 10^8$ for a proton. The trigger to recognize this enhancement is any interferometric phase $\propto f$: replacing light by matter replaces the optical frequency by the enormous de Broglie frequency $mc^2/h$, gaining many orders of magnitude. This is why atom and neutron interferometers are the most sensitive rotation sensors ever built. It is also the decisive test of relativity over the aether: the aether theory reproduces the optical effect but predicts *zero* matter-wave effect, so the mere existence of a matter-wave Sagnac phase — let alone its $\propto\omega A$ form — falsifies the aether. The optical effect alone cannot decide between the theories; the matter-wave effect can, which is the deep reason the enhancement matters beyond mere sensitivity.

**A geometric loop integral becomes a navigation industry: no moving parts, no drift.** The abstract circulation $\oint\Gamma^2\vec V\cdot d\vec\ell$ of this chapter, made observable as an interferometer phase or a frequency split, is the operating principle of the fibre-optic and ring-laser gyrometers that navigate every modern aircraft and spacecraft. The trigger connecting theory to technology is the area-proportionality $\Delta\phi\propto\omega A$: to measure a small rotation, enlarge the enclosed area, whether by winding fibre $N$ times or building a large ring cavity. Because these devices sense rotation through a geometric phase rather than a spinning mass, they have no moving parts, never wear out, and do not drift mechanically — the qualities that made them displace the gimballed mechanical gyroscope. The lesson is that a relativistic effect of order $\omega A/c^2$, seemingly tiny, becomes a precision instrument once one understands that it is a geometric phase whose sensitivity is bought by area. See [[Ex - The Sagnac delay around a circular loop]] for the delay these instruments measure.
