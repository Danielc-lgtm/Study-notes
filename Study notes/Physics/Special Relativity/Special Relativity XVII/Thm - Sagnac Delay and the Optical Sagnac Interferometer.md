---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - The Sagnac Effect"
  - "Def - Uniformly Rotating Observer"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A corotating semi-transparent mirror (identified with the corotating observer $\mathcal{O}'$) splits a monochromatic beam of frequency $f$, wavelength $\lambda = c/f$ for light, into prograde and retrograde halves that recombine after one circuit. The Sagnac delay is $\Delta t'$ (from [[Thm - The Sagnac Effect]]); the resulting phase shift is $\Delta\phi$. The enclosed area vector is $\vec{\mathcal{A}}$, magnitude $A$; the disk angular velocity is $\vec\omega$. For matter waves: $m$ is the particle rest mass, $\Gamma_p$ its Lorentz factor relative to $\mathcal{O}'$, $E = \Gamma_p mc^2$ its energy, $\hbar = h/2\pi$ the reduced Planck constant, $v$ the particle (phase) velocity. Full registry on [[Special Relativity XVII — Rotating Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 13) uses $\mathrm{diag}(-1,+1,+1,+1)$. The phase $\Delta\phi$ is a positive scalar; all formulas below are signature-independent.

---

# Statement

> **The optical Sagnac interferometer.** Splitting a monochromatic wave of frequency $f$ at a corotating mirror, sending the halves prograde and retrograde around a closed loop, and recombining them produces interference fringes shifted by the phase
> $$\Delta\phi = 2\pi f\,\Delta t' = \frac{8\pi f}{c^2}\,\vec\omega\cdot\vec{\mathcal{A}},$$
> where $\Delta t'$ is the [[Thm - The Sagnac Effect|Sagnac delay]]. For light in vacuum, $f = c/\lambda$, so
> $$\Delta\phi = \frac{8\pi}{c\lambda}\,\vec\omega\cdot\vec{\mathcal{A}}.$$
> The frequency $f$ is the same at recombination as at emission (the corotating observer is stationary), so the two beams differ only in phase.

> **The matter-wave interferometer.** For de Broglie waves of massive particles, the relevant frequency is the de Broglie frequency $f = E/h = \Gamma_p mc^2/h$, giving
> $$\Delta\phi = 4\Gamma_p\,\frac{m}{\hbar}\,\vec\omega\cdot\vec{\mathcal{A}}.$$
> The matter-wave phase exceeds the optical phase, for the same area and rotation, by the factor
> $$\frac{\Delta\phi_{\text{mat}}}{\Delta\phi_{\text{opt}}} = \Gamma_p\,\frac{mc^2}{hf} \sim 4\times 10^8$$
> for a proton with visible light, making matter-wave interferometers vastly more sensitive rotation sensors. The correct formula uses the *radiation frequency* $f$, not the phase velocity: replacing the metric $c^2$ by the particle phase velocity $v$ would be wrong.

---

# Motivation

The Sagnac delay $\Delta t' = 4\omega A/c^2$ is a time difference, but the way it is actually measured is as a *phase* difference between two recombined waves — a shift in the interference fringes that a detector can read with extraordinary sensitivity. This theorem converts the delay into the observable phase, and in doing so reveals two things: how a practical rotation sensor works, and a subtle point about which $c$ appears in the formula that distinguishes the relativistic origin of the effect from a naive propagation picture.

The optical case is direct. A monochromatic wave has phase $2\pi f t'$ at the corotating mirror; the prograde and retrograde halves return at times differing by $\Delta t'$, so their phases differ by $2\pi f\,\Delta t'$. Multiply out and the fringe shift is $\Delta\phi = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}}$, or in terms of wavelength $(8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$. Sagnac measured exactly this in 1913 with a tabletop interferometer; Michelson, Gale, and Pearson measured the phase due to the Earth's *own* rotation in 1925 with a kilometre-scale interferometer in Illinois. The sensitivity scales with the enclosed area, which is why one makes the interferometer large — or, in a fibre-optic gyroscope, winds the light path many times to multiply the area.

The matter-wave case is where the theorem becomes both subtle and powerful. A de Broglie wave also has a frequency — the Planck–Einstein frequency $f = E/h$, with $E = \Gamma_p mc^2$ the particle's energy — and the same phase argument gives $\Delta\phi = 2\pi f\,\Delta t'$. Because the particle's energy $mc^2$ is enormous compared to an optical photon's $hf$, the matter-wave phase is larger by a factor $\sim\Gamma_p mc^2/hf \sim 10^8$ for a proton with visible light. This is why atom and neutron interferometers are the most sensitive rotation sensors ever built. But the subtlety is sharp: the correct formula uses the *radiation frequency* $f$, and the $c^2$ in $4\omega A/c^2$ remains the metric factor — it must *not* be replaced by the particle's phase velocity. A naive reading that "the $c$ is the speed of the wave" would give the wrong matter-wave phase by a factor $(c/v)^2$. The Sagnac effect's independence of signal speed, established in the previous theorem, is exactly what this warning enforces: the delay is metric, the frequency is what converts it to phase.

This theorem is also the historical and conceptual capstone of the chapter, because the matter-wave Sagnac effect is the experiment that distinguishes relativity from the discredited aether theory. The aether theory, predicting the *optical* Sagnac effect correctly (Lodge, 1893), predicts *no* effect for massive particles; relativity predicts the same $\propto\omega A$ effect for matter as for light. The observed matter-wave Sagnac phase is therefore a confirmation of relativity that the aether cannot mimic.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever a wave is split, sent both ways around a rotating loop, and recombined.

The first disguised source is **"a fibre-optic gyroscope"**. Light from a laser is split, sent both ways through a long coil of optical fibre wound $N$ times, and recombined; the phase shift is $N$ times the single-loop value. The bridge is that the wound fibre multiplies the enclosed area by $N$. *Example problem:* find the rotation sensitivity of a fibre-optic gyroscope with a $1$ km coil of $20$ cm radius.

The second disguised source is **"a ring-laser gyroscope"**. An annular laser cavity supports counter-propagating modes whose resonant frequencies are split by the rotation; the beat frequency, proportional to $\omega$, is measured. The bridge is that the Sagnac phase per round trip becomes a frequency difference between the cavity modes. *Example problem:* relate the beat frequency of a ring laser to its enclosed area and the rotation rate.

The third disguised source is **"an atom or neutron interferometer"**. A coherent beam of atoms or neutrons is split and recombined around a loop; the Sagnac phase is read from the matter-wave fringes. The bridge is that the de Broglie wave has frequency $f = \Gamma_p mc^2/h$, giving the enhanced matter-wave phase. *Example problem:* compute the rotation sensitivity of a cold-cesium-atom Sagnac interferometer and compare to an optical one of the same area.

**Targets (Output Amplification)**

The conclusion is $\Delta\phi = 2\pi f\,\Delta t' = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}}$.

Combine the conclusion with **the number of fibre turns $N$**. The phase becomes $N$ times larger, $\Delta\phi = N(8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$, the design equation of the fibre-optic gyroscope. The combination shows how to engineer sensitivity, and it is nonobvious only in that the enhancement is exactly linear in turns with no diminishing returns until fibre attenuation matters. *Example:* a high-sensitivity navigation-grade fibre gyroscope.

Combine the conclusion with **the cavity resonance condition**. In a ring laser the Sagnac phase per round trip translates into a frequency split $\Delta\nu \propto \omega A/(\lambda L)$ between the counter-propagating modes ($L$ the perimeter), measured as a beat. The combination yields the ring-laser readout, and it is nonobvious that a phase shift becomes a frequency shift via the resonance condition. *Example:* the Wettzell "G" ring laser monitoring Earth's rotation.

Combine the conclusion with **the particle mass $m$**. For matter waves the phase is $4\Gamma_p(m/\hbar)\vec\omega\cdot\vec{\mathcal{A}}$, enormously larger than the optical phase. The combination explains the supremacy of atom interferometry for rotation sensing, and it is nonobvious that heavier or faster particles give larger phase (through $\Gamma_p m$), the opposite of the wavelength intuition. *Example:* precision tests of fundamental physics with atom-interferometric gyroscopes.

---

# Why Is It True

The phase shift is the delay times the angular frequency, and the only subtlety is *which* frequency.

The mechanism is elementary once the Sagnac delay is granted. A monochromatic wave at the corotating mirror oscillates as $\sin(2\pi f t')$. The prograde half returns at proper time $t'_+ = t' - t'_+(\text{travel})$ and the retrograde at $t'_-$, and because the corotating observer is *stationary* (its four-acceleration and four-rotation have constant norm, by [[Thm - 4-Acceleration and 4-Rotation of the Corotating Observer|the kinematics theorem]]), the returning waves have the *same* frequency $f$ as at emission — no Doppler reshift, because the geometry along the worldline is unchanging. The two returning waves are therefore $\sin(2\pi f(t' - t'_+))$ and $\sin(2\pi f(t' - t'_-))$, differing in phase by $\Delta\phi = 2\pi f(t'_+ - t'_-) = 2\pi f\,\Delta t'$. Substituting the Sagnac delay gives the result.

**The one-line mechanism:** *the fringe shift is the Sagnac delay measured in radians of the wave's own oscillation, $\Delta\phi = 2\pi f\,\Delta t'$ — frequency converts the metric time gap into observable phase.*

The subtle point is the identity of $f$, and it is here that the previous theorem's "independence of signal speed" does its decisive work. The Sagnac delay $\Delta t' = 4\omega A/c^2$ is a fixed geometric quantity, the same for any wave. To turn it into a phase one multiplies by the wave's angular frequency $2\pi f$. For light, $f = c/\lambda$, so $\Delta\phi = (8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$ — but the two $c$'s here have *different origins*: the $c^2$ in $\Delta t'$ is the metric, while the $c$ from $f = c/\lambda$ is the propagation speed of light specifically. For a matter wave the propagation (phase) velocity is $v\ne c$, but the frequency is still $f = E/h = \Gamma_p mc^2/h$, and the delay's $c^2$ stays metric. If one carelessly wrote the optical formula in terms of "wave speed and wavelength" and then substituted the matter-wave phase velocity for $c$, one would corrupt the metric $c^2$ and get the wrong answer by $(c/v)^2$. The clean statement, true for any wave, is $\Delta\phi = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}}$ with $f$ the radiation frequency and $c^2$ the metric — and the matter-wave enhancement $\Gamma_p mc^2/hf$ is simply the ratio of the de Broglie frequency to the optical frequency.

---

# What Makes This Hard

The non-obvious point is which frequency to use and which $c$ is metric. The Sagnac delay's $c^2$ is the spacetime metric factor and must never be replaced by the wave's phase velocity; the conversion factor from delay to phase is the radiation frequency $f$ (which for light is $c/\lambda$ but for matter is $\Gamma_p mc^2/h$, *not* $v/\lambda_{\text{dB}}$ in a way that touches the metric). The common error is to write $\Delta\phi$ "in terms of wavelength and wave speed" and then substitute the matter-wave phase velocity, corrupting the metric $c^2$ and getting the matter-wave phase wrong by $(c/v)^2$. A second subtlety is recognizing that the returning waves have the same frequency as at emission — which requires the corotating observer to be *stationary*, a fact that must be cited, not assumed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the wave phase at the corotating mirror as $2\pi f t'$. Argue that the returning prograde and retrograde waves keep the frequency $f$ (the corotating observer is stationary), so their phase difference is $2\pi f$ times the arrival-time difference $\Delta t'$. Substitute the Sagnac delay to get the optical phase. For matter waves, replace $f$ by the de Broglie frequency $\Gamma_p mc^2/h$ and simplify with $\hbar = h/2\pi$.

**Subgoal decomposition:**

1. **Establish frequency conservation.** Show the returning waves have the same frequency $f$ as at emission.
   - *Hint:* The corotating observer is stationary ($\|\vec a'\|$, $\|\vec\omega'\|$ constant), so successive wave nodes are related by a constant time translation — no reshift.
   - *Why needed:* It guarantees the recombining waves differ only in phase, not frequency.

2. **Convert the delay to a phase.** Show $\Delta\phi = 2\pi f\,\Delta t'$ and substitute $\Delta t' = (4/c^2)\vec\omega\cdot\vec{\mathcal{A}}$.
   - *Hint:* Phase difference $=$ angular frequency $\times$ time difference.
   - *Why needed:* It gives the optical phase $\Delta\phi = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}} = (8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$.

3. **Specialize to matter waves.** Replace $f$ by $\Gamma_p mc^2/h$.
   - *Hint:* Planck–Einstein $E = hf$ with $E = \Gamma_p mc^2$; use $\hbar = h/2\pi$.
   - *Why needed:* It gives $\Delta\phi = 4\Gamma_p(m/\hbar)\vec\omega\cdot\vec{\mathcal{A}}$ and the enhancement ratio $\Gamma_p mc^2/hf$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The returning waves keep their frequency
> **Statement:** The prograde and retrograde waves return to the corotating mirror with the same frequency $f$ they had at emission.
>
> **Hint:** The corotating observer is a stationary observer (constant $\|\vec a'\|$ and $\|\vec\omega'\|$ along its worldline), so the worldlines of successive wave nodes are related by a constant time translation.
>
> **Why needed:** Without frequency conservation, the recombining waves would differ in frequency, not merely phase, and the fringe analysis would fail.
>
> > [!note]- Full proof
> > By [[Thm - 4-Acceleration and 4-Rotation of the Corotating Observer|the kinematics theorem]], the corotating observer $\mathcal{O}'$ has four-acceleration and four-rotation of constant norm along its worldline, hence is a stationary observer. For such an observer, the geometry experienced is the same at every instant of proper time, so the worldlines of successive nodes of an emitted wave are deducible from one another by a constant proper-time translation. Therefore the period of the nodes at reception equals the period at emission, and the returning waves $\mathscr{S}_\pm$ have the same frequency $f$ as the emitted wave. $\blacksquare$

> [!note]- Lemma 2: The optical phase shift
> **Statement:** $\Delta\phi = 2\pi f\,\Delta t' = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}} = (8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$.
>
> **Hint:** Phase difference is angular frequency times arrival-time difference; substitute the Sagnac delay and $\lambda = c/f$.
>
> **Why needed:** It is the observable fringe shift for light.
>
> > [!note]- Full proof
> > Writing the field component as $E_\pm(t') = \sin(2\pi f(t' - t'_\pm))$ for the prograde/retrograde returning waves (same frequency by Lemma 1), the phase difference read at recombination is $\Delta\phi = 2\pi f(t'_+ - t'_-) = 2\pi f\,\Delta t'$. Substituting the [[Thm - The Sagnac Effect|Sagnac delay]] $\Delta t' = (4/c^2)\vec\omega\cdot\vec{\mathcal{A}}$ gives $\Delta\phi = (8\pi f/c^2)\vec\omega\cdot\vec{\mathcal{A}}$. For light $f = c/\lambda$, so $\Delta\phi = (8\pi/c\lambda)\vec\omega\cdot\vec{\mathcal{A}}$. $\blacksquare$

> [!note]- Lemma 3: The matter-wave phase shift and enhancement
> **Statement:** $\Delta\phi = 4\Gamma_p(m/\hbar)\vec\omega\cdot\vec{\mathcal{A}}$, with $\Delta\phi_{\text{mat}}/\Delta\phi_{\text{opt}} = \Gamma_p mc^2/hf \sim 4\times10^8$ for a proton and visible light.
>
> **Hint:** Replace the radiation frequency $f$ in $\Delta\phi = 2\pi f\,\Delta t'$ by the de Broglie frequency $E/h = \Gamma_p mc^2/h$; use $\hbar = h/2\pi$.
>
> **Why needed:** It gives the matter-wave phase and quantifies the sensitivity advantage.
>
> > [!note]- Full proof
> > For a de Broglie wave the frequency is $f = E/h$ (Planck–Einstein), with $E = \Gamma_p mc^2$ the particle energy relative to $\mathcal{O}'$. Substituting into $\Delta\phi = 2\pi f\,\Delta t' = 2\pi f\,(4/c^2)\vec\omega\cdot\vec{\mathcal{A}}$: $\Delta\phi = 2\pi\frac{\Gamma_p mc^2}{h}\frac{4}{c^2}\vec\omega\cdot\vec{\mathcal{A}} = \frac{8\pi\Gamma_p m}{h}\vec\omega\cdot\vec{\mathcal{A}} = 4\Gamma_p\frac{m}{\hbar}\vec\omega\cdot\vec{\mathcal{A}}$ (using $\hbar = h/2\pi$). The ratio to the optical phase (same area, same rotation) is $\Delta\phi_{\text{mat}}/\Delta\phi_{\text{opt}} = (\Gamma_p mc^2/h)/f = \Gamma_p mc^2/hf$; for a proton ($mc^2\sim 0.9$ GeV), $\Gamma_p\sim 1$, and visible light ($hf\sim 2$ eV), this is $\sim 4\times10^8$. The metric $c^2$ from $\Delta t'$ has cancelled against the $c^2$ in $E = \Gamma_p mc^2$, leaving a manifestly speed-independent result — confirming that one must use the frequency, not the phase velocity. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 0 — frequency conservation.* By Lemma 1, the corotating mirror $\mathcal{O}'$ is a stationary observer, so the prograde and retrograde waves return with the same frequency $f$ as at emission; the recombining waves differ only in phase.
>
> *Optical phase.* By Lemma 2, the phase difference at recombination is $\Delta\phi = 2\pi f(t'_+ - t'_-) = 2\pi f\,\Delta t'$. Substituting the [[Thm - The Sagnac Effect|Sagnac delay]] $\Delta t' = (4/c^2)\vec\omega\cdot\vec{\mathcal{A}}$,
> $$\Delta\phi = \frac{8\pi f}{c^2}\vec\omega\cdot\vec{\mathcal{A}} = \frac{8\pi}{c\lambda}\vec\omega\cdot\vec{\mathcal{A}}\qquad(\text{light},\ f = c/\lambda).$$
>
> *Matter-wave phase.* By Lemma 3, replacing $f$ by the de Broglie frequency $\Gamma_p mc^2/h$,
> $$\Delta\phi = 4\Gamma_p\frac{m}{\hbar}\vec\omega\cdot\vec{\mathcal{A}},$$
> with the matter-to-optical ratio $\Gamma_p mc^2/hf \sim 4\times10^8$ for a proton and visible light. The metric $c^2$ in the delay is never the propagation speed: for matter the correct formula keeps the radiation frequency $f$ and the metric $c^2$, and substituting the phase velocity for $c$ would err by $(c/v)^2$.
>
> *Historical confirmation.* Sagnac (1913) measured $\Delta\phi \simeq 0.21$ rad for $\lambda = 436$ nm, $\omega/2\pi = 2$ Hz, $A = 0.0866\,\text{m}^2$; Michelson, Gale, and Pearson (1925) measured the phase due to the Earth's rotation with a $613\times339\,\text{m}$ interferometer ($\Delta\phi\simeq 1.44$ rad). Both agree with the formula. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The aether test — why matter waves discriminate.** The aether theory predicts the optical Sagnac effect correctly (the beams move at $c$ relative to the aether) but predicts *no* effect for massive particles, whereas relativity predicts the same $\propto\omega A$ effect for matter. Working out both predictions and seeing where they diverge is a clean exercise in distinguishing relativity from its historical rival. The application is nonobvious because the optical effect alone cannot decide between the theories — only the matter-wave effect can.

**Ring-laser sensitivity and the standard quantum limit.** Pushing ring-laser and atom-interferometric gyroscopes to their fundamental sensitivity runs into quantum noise (shot noise, the standard quantum limit), and the analysis combines the Sagnac phase with quantum measurement theory. The application is out-of-distribution because a relativistic geometric effect meets quantum metrology at the precision frontier.

**Gravitational analogues — the gravomagnetic clock effect.** In general relativity, a rotating mass produces a gravomagnetic field that splits the orbital periods of co- and counter-rotating satellites — the gravomagnetic clock effect — structurally a gravitational Sagnac effect. Relating the flat-spacetime Sagnac formula to its curved-spacetime analogue is a bridge exercise toward general relativity. The application is surprising because the same area-times-rotation structure reappears for orbits around a spinning mass.

---

# Bridges

- **[[Thm - The Sagnac Effect]]** — this theorem is the observable face of the Sagnac delay: it multiplies the delay $\Delta t'$ by the wave's angular frequency $2\pi f$ to get the measured fringe shift. The delay carries the physics (the metric $c^2$, the speed-independence); the frequency is merely the conversion to phase. The two theorems together give the complete account: the delay is metric and universal, the phase is what an interferometer reads.

- **The Planck–Einstein and de Broglie relations (quantum mechanics)** — the matter-wave phase relies on assigning a frequency $f = E/h$ to a massive particle's wave, the Planck–Einstein relation, with $E = \Gamma_p mc^2$ the relativistic energy. The enormous matter-wave enhancement $\Gamma_p mc^2/hf$ is a direct consequence of the particle's rest energy dwarfing an optical photon's energy, and it is the quantum-relativistic input that makes atom interferometers supreme rotation sensors.

- **The Aharonov–Bohm effect (quantum mechanics)** — the matter-wave Sagnac phase $\Delta\phi = 4\Gamma_p(m/\hbar)\vec\omega\cdot\vec{\mathcal{A}}$ is a geometric phase of exactly the Aharonov–Bohm type: a $\frac{1}{\hbar}$ times a loop integral of a potential, equal to a flux of a field ($\propto\vec\omega$) through the enclosed area, observable only by interference. The four-rotation $\vec\omega$ is the analogue of the magnetic field and the metric coupling the analogue of the vector potential; the matter-wave Sagnac effect makes the rotational Aharonov–Bohm analogy literal and quantitative.

---

# Unlocked by This

> [!tip] The Gyrolaser and Inertial Navigation *(from Aerospace Engineering)*
> The optical Sagnac phase is the readout of the **ring-laser gyroscope** (gyrolaser) — a helium–neon laser in an annular cavity, where rotation splits the frequencies of the clockwise and counter-clockwise cavity modes and the beat measures $\omega$ — and the **fibre-optic gyroscope**, where the light traverses a coil wound $N$ times to multiply the area. Together they are the rotation-sensing heart of modern **inertial navigation systems**, with no moving parts and no mechanical drift. This theorem is the bridge from the geometric Sagnac delay to the engineered instrument that navigates aircraft and spacecraft.

> [!tip] Atom Interferometry and Precision Tests of Physics *(from Quantum Metrology)*
> The matter-wave enhancement factor $\Gamma_p mc^2/hf \sim 10^8$ makes **atom and neutron interferometers** the most sensitive rotation sensors ever constructed, and a platform for precision tests of general relativity, the equivalence principle, and Lorentz invariance. That the geometric Sagnac phase governs matter waves with this enormous enhancement — first observed by Zimmerman and Mercereau in 1965 with superconducting electrons, and since with neutrons, calcium, sodium, and cesium atoms — is both a triumph of relativity over the aether theory and the foundation of a precision-measurement industry.
