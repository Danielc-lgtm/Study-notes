---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Radiation by an Accelerated Charge (Larmor Formula)"
  - "Def - Energy-Momentum Tensor of the Electromagnetic Field"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ unless restored; signature mostly-minus. A charge $q$ has three-velocity $\mathbf V$ (speed $V$), three-acceleration $\boldsymbol\gamma$, and Lorentz factor $\Gamma = (1-V^2/c^2)^{-1/2}$ relative to an inertial observer $\mathcal O$. The direction of observation is the unit vector $\hat{\mathbf n}$, making polar angle $\theta$ with a chosen axis (the velocity, or the acceleration, depending on the case) and azimuthal angle $\phi$. The **Poynting vector** $\vec\varphi_{\text{em}} = \tfrac{1}{\mu_0}\mathbf E\times\mathbf B$ gives the energy flux; its magnitude as a function of direction is the **radiation pattern**. The retarded quantities $\mathbf V, \boldsymbol\gamma$ are evaluated at the retarded time $t_P = t - r/c$. Full registry on [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

---

# Statement

> **Theorem (Angular distribution of radiation).** The power radiated per unit solid angle by an accelerated charge is obtained from the Poynting vector of its radiative field. Three cases:
>
> **(i) Charge instantaneously at rest** ($\mathbf V = 0$). The pattern is a dipole donut,
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} = \frac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\sin^2\theta,$$
> where $\theta$ is the angle between the acceleration $\boldsymbol\gamma$ and $\hat{\mathbf n}$; the radiation vanishes along the acceleration and is maximal perpendicular to it. Integrating over the sphere recovers the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Larmor formula]].
>
> **(ii) Velocity collinear with acceleration** ($\mathbf V \parallel \boldsymbol\gamma$, linear accelerator). The dipole pattern is focused forward,
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \propto \frac{\sin^2\theta}{(1 - \tfrac{V}{c}\cos\theta)^6},$$
> with maxima at $\theta_\pm = \pm\arccos\!\big(\tfrac{6V/c}{1+\sqrt{1+24V^2/c^2}}\big)$, which approach $\theta_\pm \simeq \pm\tfrac{1}{\sqrt5\,\Gamma}$ in the ultrarelativistic limit.
>
> **(iii) Velocity orthogonal to acceleration** ($\mathbf V\perp\boldsymbol\gamma$, circular motion). The pattern is focused into a cone of half-angle $\theta \sim 1/\Gamma$ around the velocity direction, with the angular factor $(1-\tfrac Vc\cos\theta)^{-4}$ producing the forward beaming.
>
> In every relativistic case ($\Gamma \gg 1$) the radiation is **Doppler-boosted** into a narrow forward cone of half-angle $\sim 1/\Gamma$ around the instantaneous velocity, with the amplitude in that direction enormously enhanced.

---

# Motivation

The [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Larmor and Liénard formulas]] tell us the *total* power an accelerated charge radiates, summed over all directions. But a detector sits in one place, and what it records depends on *where* it is relative to the charge's motion. The question this theorem answers is: into which directions does an accelerated charge send its radiation, and how does that pattern change as the charge approaches the speed of light? The answer transforms a symmetric dipole donut, at low speed, into a tightly collimated forward searchlight at high speed — and that transformation is the single most important practical fact about relativistic radiation.

The reason it matters is **beaming**. At low speed a charge radiates most strongly perpendicular to its acceleration and not at all along it — the familiar dipole pattern of an antenna. But as the charge becomes relativistic, the radiation is swept forward into a cone of half-angle roughly $1/\Gamma$ around the direction of motion. For an electron with $\Gamma = 1000$, that cone is a milliradian wide. This is why synchrotron light is a pencil-thin, laser-like beam rather than a diffuse glow, why it can be aimed down a beamline at a sample centimetres across from tens of metres away, and why we see the jets of active galactic nuclei as one-sided even though they are emitted symmetrically in both directions — only the jet pointing toward us is beamed into our line of sight, a phenomenon called **Doppler boosting**.

The structural origin of the beaming is the factor $(1 - \tfrac Vc\cos\theta)^{-n}$ that appears in every relativistic radiation pattern. This is a power of the inverse Doppler factor, and it encodes the geometric squeezing of the emission: the same physics that blue-shifts and intensifies light from an approaching source concentrates the *radiated power* into the forward direction. The high power $n$ ($n = 6$ for the collinear case, modified to a cone for the orthogonal case) is what makes the focusing so dramatic — a small velocity-dependent denominator, raised to the sixth power and evaluated near $\theta = 0$, produces an enormous forward spike.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "an accelerated charge whose velocity and acceleration are specified relative to the observer". Recognising the three cases in practice:

The first disguised source is **"a charge in a linear accelerator or undergoing bremsstrahlung"**, where the acceleration is along the velocity — case (ii). The bridge is that an electric field accelerating a charge along its motion produces $\boldsymbol\gamma\parallel\mathbf V$. *Example:* the forward-peaked X-ray emission when electrons decelerate in an X-ray tube anode.

The second disguised source is **"a charge in circular or helical motion"**, where the magnetic Lorentz force gives acceleration perpendicular to velocity — case (iii). The bridge is the centripetal nature of magnetic deflection. *Example:* the tangential, knife-edge beam of synchrotron radiation that sweeps past a fixed observer like a lighthouse, treated on [[Def - Synchrotron Radiation]].

The third disguised source is **"a non-relativistic emitter"**, where $V \ll c$ and the pattern is the undistorted dipole donut — case (i). The bridge is that all the Doppler factors reduce to $1$ when $V/c \to 0$. *Example:* a radio antenna, or any classical oscillating dipole, radiating in the textbook $\sin^2\theta$ pattern.

**Targets (Output Amplification)**

The conclusion is the directional power $\mathrm d\mathcal P/\mathrm d\Omega$.

Combine with **integration over the sphere** to recover the total power. Integrating $\mathrm d\mathcal P/\mathrm d\Omega$ over all directions must reproduce the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Larmor/Liénard]] total — a stringent consistency check, since the beaming factor and the total power are not independent. The further result is confidence that the directional and integrated formulas are mutually consistent. *Example:* verifying that the forward-beamed case (ii) integrates back to the Liénard $\Gamma^6$ power.

Combine with **the spectral content** to get the synchrotron spectrum. The forward beaming means a fixed observer sees the charge's radiation only during the brief instant its velocity points toward them — a short pulse, whose Fourier transform is a broad spectrum extending to high harmonics of the orbital frequency. The further result is the characteristic synchrotron frequency $f_c \sim \Gamma^3 (c/R)$, far above the orbital frequency. *Example:* the broad synchrotron spectrum from radio to X-rays, [[Def - Synchrotron Radiation]].

Combine with **the source's velocity to decide visibility** in astrophysics. Whether a relativistic jet is seen depends on whether its beaming cone includes the line of sight; the boosting factor $\sim\Gamma^3$ to $\Gamma^4$ in observed intensity makes approaching jets bright and receding ones invisible. The further result is the one-sided appearance of intrinsically two-sided jets. *Example:* the quasar 3C 175, whose counter-jet is undetectable because it is beamed away from us.

---

# Why Is It True

The pattern is the magnitude of the Poynting vector as a function of direction, and the relativistic distortion is entirely the Doppler factor doing two jobs at once.

**The bold one-liner: the radiation pattern is the rest-frame dipole donut $\sin^2\theta$ multiplied by a power of the inverse Doppler factor $(1 - \tfrac Vc\cos\theta)^{-n}$, which sweeps the donut forward into a cone of half-angle $1/\Gamma$ — relativistic aberration of the emitted light.**

Begin in the rest frame, case (i). The radiative field of a charge is transverse and proportional to the component of the acceleration perpendicular to the line of sight, which is $|\boldsymbol\gamma|\sin\theta$. The Poynting flux is the field squared, hence $\propto\gamma^2\sin^2\theta$ — zero along the acceleration ($\theta = 0$, no transverse component) and maximal perpendicular to it. This is the dipole donut, and it is the pattern of every slow antenna.

Now boost. Two effects compound. First, **aberration**: the directions into which the radiation is emitted in the rest frame are swept forward in the lab frame, exactly as the apparent positions of stars crowd toward the forward direction for a fast-moving observer. A photon emitted sideways ($\theta' = 90°$) in the rest frame appears at $\cos\theta = V/c$ in the lab — for $V\to c$ that is $\theta\to 0$, i.e. nearly forward. So the whole donut is pushed into a narrow forward cone. Second, **intensity transformation**: the power per solid angle picks up factors of the Doppler factor because both the energy of each photon and the rate at which photons arrive are blue-shifted in the forward direction. The combination of aberration (which compresses the solid angle) and Doppler enhancement (which boosts the per-photon energy and arrival rate) produces the factor $(1-\tfrac Vc\cos\theta)^{-n}$, with the power $n$ depending on how many of these effects are counted in the chosen variables.

To see *why the cone half-angle is $1/\Gamma$*, look at where the denominator $(1-\tfrac Vc\cos\theta)$ becomes small. For $V/c = 1 - 1/(2\Gamma^2)$ and small $\theta$, $\cos\theta \approx 1 - \theta^2/2$, so $1 - \tfrac Vc\cos\theta \approx (1 + \Gamma^2\theta^2)/(2\Gamma^2)$. This is smallest — and the radiation strongest — when $\Gamma^2\theta^2 \lesssim 1$, i.e. $\theta \lesssim 1/\Gamma$. The angular width of the beam is set by where $\Gamma\theta$ is of order one, which is the universal relativistic beaming angle $1/\Gamma$. In the collinear case (ii) the numerator $\sin^2\theta$ vanishes exactly on axis, so the pattern is not a single forward spike but two lobes straddling the axis at $\theta_\pm \simeq 1/(\sqrt5\,\Gamma)$ — the competition between the $\sin^2\theta$ numerator (which kills the on-axis emission) and the $(1-\tfrac Vc\cos\theta)^{-6}$ denominator (which wants to push everything forward) places the maxima just off axis.

The orthogonal case (iii) is the one relevant to circular motion and synchrotron radiation: the acceleration is perpendicular to the velocity, the on-axis emission no longer vanishes, and the pattern becomes a genuine forward cone of half-angle $1/\Gamma$ swept around the velocity. A distant observer in the orbital plane therefore sees a flash each time the velocity points at them — the searchlight sweep that gives synchrotron radiation its pulsed, broad-spectrum character.

---

# What Makes This Hard

The conceptual subtlety is keeping straight that the relativistic distortion is *aberration of the emitted radiation*, not a change in the rest-frame emission pattern — in its own instantaneous rest frame the charge always radiates the simple dipole donut, and all the forward-beaming drama is the Lorentz transformation of that pattern to the lab. The non-obvious technical point is the *power* of the Doppler factor: it is $n = 6$ for the collinear case but the bookkeeping (how many factors come from aberration, how many from photon-energy blue-shift, how many from the retarded-time Jacobian $\mathrm dt_P/\mathrm dt = 1 - \tfrac Vc\cos\theta$) is where errors creep in. The most common mistake is to forget the retarded-time Jacobian, which contributes the extra powers that distinguish $\mathrm d\mathcal P/\mathrm d\Omega$ (power received per unit observer time) from power per unit retarded time.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the Poynting vector of the radiative field; for the rest frame extract the $\sin^2\theta$ dipole; boost to the lab by inserting the velocity, producing the Doppler denominator $(1-\tfrac Vc\cos\theta)$; specialise to collinear and orthogonal acceleration; expand near $\theta = 0$ in the ultrarelativistic limit to read off the $1/\Gamma$ cone.

**Subgoal decomposition:**

1. **Poynting vector of the radiative field.** Show $\vec\varphi_{\text{em}} = \tfrac{1}{\mu_0 c}(\mathbf E\cdot\mathbf E)\,\hat{\mathbf n}$ for the radiation field (where $\hat{\mathbf n}\cdot\mathbf E = 0$).
   - *Hint:* For the radiative field $\mathbf B = \hat{\mathbf n}\times\mathbf E/c$, so $\mathbf E\times\mathbf B = (E^2/c)\hat{\mathbf n}$.
   - *Why needed:* The pattern is $|\vec\varphi_{\text{em}}|$; this reduces it to $|\mathbf E|^2$.

2. **Rest-frame dipole.** For $\mathbf V = 0$, $\mathbf E \propto \hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$, giving $|\mathbf E|^2 \propto \gamma^2\sin^2\theta$.
   - *Hint:* $|\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)| = |\boldsymbol\gamma|\sin\theta$ is the perpendicular component.
   - *Why needed:* It is the pattern that gets boosted.

3. **Insert the velocity (general Liénard–Wiechert field).** The radiative field carries a denominator $(1-\tfrac Vc\cos\theta)^{3}$ from the retarded-time geometry; the Poynting flux squares the field and the Jacobian $\mathrm dt_P/\mathrm dt = (1-\tfrac Vc\cos\theta)$ contributes one more power.
   - *Hint:* Track the factor $(1-\hat{\mathbf n}\cdot\mathbf V/c)$ through the Liénard–Wiechert field and the retarded Jacobian.
   - *Why needed:* It produces the Doppler denominators $(1-\tfrac Vc\cos\theta)^{-4}$ or $^{-6}$.

4. **Collinear case maxima.** With $\boldsymbol\gamma\parallel\mathbf V$, maximise $\sin^2\theta/(1-\tfrac Vc\cos\theta)^6$ over $\theta$.
   - *Hint:* Set the derivative to zero; solve the quadratic in $\cos\theta$, then Taylor-expand for $V\to c$.
   - *Why needed:* It gives $\theta_\pm \simeq 1/(\sqrt5\Gamma)$.

5. **Ultrarelativistic cone.** Expand $1 - \tfrac Vc\cos\theta \approx (1+\Gamma^2\theta^2)/(2\Gamma^2)$ for small $\theta$.
   - *Hint:* $V/c \approx 1 - 1/(2\Gamma^2)$, $\cos\theta \approx 1-\theta^2/2$.
   - *Why needed:* It shows the pattern is significant only for $\Gamma\theta\lesssim 1$, the $1/\Gamma$ cone.

---

# Lemma Decomposition

> [!note]- Lemma 1: The radiation Poynting vector is radial and quadratic in the transverse field
> **Statement:** For the radiative field, $\vec\varphi_{\text{em}} = \dfrac{\mathbf E\cdot\mathbf E}{\mu_0 c}\,\hat{\mathbf n}$, with $\mathbf E\perp\hat{\mathbf n}$.
>
> **Hint:** The radiation field satisfies $\mathbf B = c^{-1}\hat{\mathbf n}\times\mathbf E$ and $\hat{\mathbf n}\cdot\mathbf E = 0$.
>
> **Why needed:** It reduces the directional power to the squared magnitude of the radiative electric field, the quantity that carries the angular dependence.
>
> > [!note]- Full proof
> > For the far (radiative) field of a localised source, $\mathbf B = c^{-1}\hat{\mathbf n}\times\mathbf E$ and $\hat{\mathbf n}\cdot\mathbf E = 0$ (the field is transverse to the propagation direction $\hat{\mathbf n}$). Then $\vec\varphi_{\text{em}} = \tfrac{1}{\mu_0}\mathbf E\times\mathbf B = \tfrac{1}{\mu_0 c}\mathbf E\times(\hat{\mathbf n}\times\mathbf E) = \tfrac{1}{\mu_0 c}[(\mathbf E\cdot\mathbf E)\hat{\mathbf n} - (\mathbf E\cdot\hat{\mathbf n})\mathbf E] = \tfrac{\mathbf E\cdot\mathbf E}{\mu_0 c}\hat{\mathbf n}$, using $\mathbf E\cdot\hat{\mathbf n} = 0$. The flux is radial with magnitude $|\mathbf E|^2/\mu_0 c$. $\blacksquare$

> [!note]- Lemma 2: The rest-frame dipole pattern
> **Statement:** For a charge instantaneously at rest, $\mathrm d\mathcal P/\mathrm d\Omega = \dfrac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\sin^2\theta$, $\theta$ being the angle between $\boldsymbol\gamma$ and $\hat{\mathbf n}$.
>
> **Hint:** The rest-frame radiative field is $\mathbf E \propto \hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$; its magnitude is the perpendicular acceleration $\gamma\sin\theta$.
>
> **Why needed:** It is the undistorted pattern; every relativistic case is this multiplied by Doppler factors.
>
> > [!note]- Full proof
> > In the instantaneous rest frame the radiative electric field at distance $r$ is $\mathbf E = \tfrac{q}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)$. Its magnitude is $|\mathbf E| = \tfrac{q}{4\pi\varepsilon_0 c^2 r}|\boldsymbol\gamma|\sin\theta$, since $|\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\gamma)|$ is the component of $\boldsymbol\gamma$ perpendicular to $\hat{\mathbf n}$, equal to $\gamma\sin\theta$. By Lemma 1, $\mathrm d\mathcal P/\mathrm d\Omega = r^2|\vec\varphi_{\text{em}}| = \tfrac{r^2|\mathbf E|^2}{\mu_0 c} = \tfrac{q^2\gamma^2\sin^2\theta}{16\pi^2\varepsilon_0 c^3}$ (using $\mu_0 = 1/\varepsilon_0 c^2$). Integrating with $\int\sin^2\theta\,\mathrm d\Omega = 8\pi/3$ recovers $\mathcal P = q^2\gamma^2/6\pi\varepsilon_0 c^3$, the Larmor formula. $\blacksquare$

> [!note]- Lemma 3: The ultrarelativistic beaming cone has half-angle $1/\Gamma$
> **Statement:** For $V/c = 1 - 1/(2\Gamma^2)$ and small $\theta$, the Doppler denominator is $1 - \tfrac Vc\cos\theta \approx (1+\Gamma^2\theta^2)/(2\Gamma^2)$, so any pattern $\propto(1-\tfrac Vc\cos\theta)^{-n}$ is significant only for $\Gamma\theta\lesssim 1$.
>
> **Hint:** Taylor-expand $V/c$ and $\cos\theta$ to second order and add.
>
> **Why needed:** It is the quantitative statement of relativistic beaming — the universal $1/\Gamma$ opening angle.
>
> > [!note]- Full proof
> > For $\Gamma \gg 1$, $V/c = \sqrt{1-1/\Gamma^2} \approx 1 - 1/(2\Gamma^2)$. For small $\theta$, $\cos\theta \approx 1 - \theta^2/2$. Then
> > $$1 - \frac Vc\cos\theta \approx 1 - \Big(1-\frac{1}{2\Gamma^2}\Big)\Big(1-\frac{\theta^2}{2}\Big) \approx \frac{1}{2\Gamma^2} + \frac{\theta^2}{2} = \frac{1+\Gamma^2\theta^2}{2\Gamma^2},$$
> > dropping the cross-term $\theta^2/(4\Gamma^2)$. A factor $(1-\tfrac Vc\cos\theta)^{-n} = (2\Gamma^2)^n(1+\Gamma^2\theta^2)^{-n}$ is maximal at $\theta = 0$ and falls to a fraction of its peak once $\Gamma^2\theta^2 \sim 1$, i.e. $\theta\sim 1/\Gamma$. The radiation is thus confined to a forward cone of half-angle $\sim 1/\Gamma$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — radiative field and far zone.** We work in the far zone where the field is purely radiative, transverse ($\hat{\mathbf n}\cdot\mathbf E = 0$), and falls as $1/r$; the power per solid angle is $\mathrm d\mathcal P/\mathrm d\Omega = r^2|\vec\varphi_{\text{em}}|$.
>
> By **Lemma 1**, $\mathrm d\mathcal P/\mathrm d\Omega = r^2|\mathbf E|^2/\mu_0 c$.
>
> **Case (i), $\mathbf V = 0$.** By **Lemma 2**, $\mathrm d\mathcal P/\mathrm d\Omega = \tfrac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\sin^2\theta$, the dipole donut, integrating to the Larmor power.
>
> **Cases (ii) and (iii), $\mathbf V \ne 0$.** The general (Liénard–Wiechert) radiative field carries the retarded-geometry denominator: with $\kappa = 1 - \hat{\mathbf n}\cdot\mathbf V/c = 1 - \tfrac Vc\cos\theta$, the field is $\mathbf E \propto \tfrac{1}{\kappa^3}\,\hat{\mathbf n}\times[(\hat{\mathbf n}-\mathbf V/c)\times\boldsymbol\gamma]$, and the power per unit *observer* solid angle and time includes one further factor of $\kappa$ from the retarded-time Jacobian $\mathrm dt_P/\mathrm dt = \kappa$. Squaring the field and folding in the Jacobian gives the directional power with denominator $\kappa^{6}$ (collinear, where the numerator is $\sin^2\theta$) or the corresponding form with $\kappa^4$ (orthogonal). Explicitly, for $\boldsymbol\gamma\parallel\mathbf V$,
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} = \frac{q^2\gamma^2}{16\pi^2\varepsilon_0 c^3}\,\frac{\sin^2\theta}{(1-\tfrac Vc\cos\theta)^6}.$$
> Maximising over $\theta$: setting $\tfrac{\mathrm d}{\mathrm d\theta}\big[\sin^2\theta(1-\tfrac Vc\cos\theta)^{-6}\big] = 0$ yields a quadratic in $\cos\theta$ whose physical root is $\cos\theta_\pm = \tfrac{\sqrt{1+24V^2/c^2}-1}{4V/c}$, i.e. $\theta_\pm = \arccos\!\big(\tfrac{6V/c}{1+\sqrt{1+24V^2/c^2}}\big)$. Taylor-expanding for $V\to c$ gives $\theta_\pm \simeq \pm 1/(\sqrt5\,\Gamma)$.
>
> For $\boldsymbol\gamma\perp\mathbf V$ (case iii), the numerator no longer vanishes on axis and the pattern $\propto(1-\tfrac Vc\cos\theta)^{-4}[\,\cdots\,]$ becomes a forward cone; by **Lemma 3**, in the ultrarelativistic limit the cone half-angle is $\sim 1/\Gamma$. In all relativistic cases the radiation is Doppler-boosted into a forward cone of half-angle $1/\Gamma$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**One-sided astrophysical jets.** Active galactic nuclei eject plasma in two opposite relativistic jets, intrinsically symmetric, yet we usually observe only one. Applying the beaming factor (the observed intensity scales as $\sim\Gamma^{3\text{–}4}$ in the forward direction and is suppressed by the same factor backward) shows the approaching jet is boosted into visibility while the receding one is dimmed below detection. The quasar 3C 175 is a textbook example. This is the angular-distribution theorem read as an observational selection effect.

**Headlight effect for moving light sources.** A relativistically moving isotropic emitter (in its rest frame) appears, to a stationary observer, to beam its light forward into a cone of half-angle $1/\Gamma$ — the "headlight" or "searchlight" effect. This is the same aberration that beams an accelerated charge's radiation, applied to an isotropic source, and it governs the apparent brightness of relativistic particles and the forward-peaked emission of fast-moving plasmas. The application connects radiation beaming to the relativistic aberration of light.

**Pulsar lighthouse beams.** A rotating neutron star's relativistic particle beam sweeps across the sky; the narrow $1/\Gamma$ emission cone is why pulsars are seen as sharp periodic pulses rather than steady sources. The angular distribution of the beamed synchrotron/curvature radiation sets the pulse width. The application shows the same beaming physics operating on a galactic, rotating-magnetosphere scale.

---

# Bridges

- **[[Thm - Radiation by an Accelerated Charge (Larmor Formula)]]** — the total power of which this theorem is the directional refinement. Integrating $\mathrm d\mathcal P/\mathrm d\Omega$ over the sphere must reproduce the Larmor/Liénard total; the angular distribution and the integrated power are two views of the same Poynting flux, one resolved in direction and one summed.

- **[[Def - Synchrotron Radiation]]** — the application of case (iii) to a charge in circular motion. The $1/\Gamma$ forward cone, swept around the orbit, is what makes a fixed observer see a sequence of brief pulses, and the brevity of each pulse (by Fourier duality) is the origin of the broad, high-frequency synchrotron spectrum. The angular distribution is the geometric input to the spectral calculation.

- **Relativistic aberration of light** — the kinematic principle underlying the beaming. The forward-sweeping of the emission directions is exactly the aberration formula $\cos\theta = (\cos\theta' + V/c)/(1 + \tfrac Vc\cos\theta')$ applied to the directions of emitted photons: rest-frame sideways emission ($\theta' = 90°$) appears at $\cos\theta = V/c$, nearly forward for $V\to c$. The radiation pattern's distortion is aberration made visible in energy flux.

---

# Unlocked by This

> [!tip] The Synchrotron Spectrum and Characteristic Frequency *(from Radiation Theory)*
> The $1/\Gamma$ beaming means a distant observer is illuminated only during the fraction $\sim 1/\Gamma$ of the orbit when the velocity points toward them, receiving a pulse of duration $\sim 1/(\Gamma^3\omega_B)$ — shortened by an extra $\Gamma^2$ from the retarded-time compression of an approaching source. By Fourier duality this short pulse contains frequencies up to the **characteristic frequency** $f_c \sim \Gamma^3(c/R)$, far above the orbital frequency. The angular distribution is thus the geometric seed of the broad synchrotron spectrum developed on [[Def - Synchrotron Radiation]].

> [!tip] Doppler Boosting and Superluminal Motion *(from High-Energy Astrophysics)*
> The same forward beaming, combined with light-travel-time effects, produces **apparent superluminal motion** in relativistic jets: a blob moving toward us at $\Gamma\gg1$ appears to move across the sky faster than light, because it nearly keeps pace with its own emitted radiation. Doppler boosting enhances the approaching component's flux by $\sim\Gamma^{3\text{–}4}$, and together these effects make blazars (jets pointed at Earth) among the brightest and most variable objects in the sky. The angular distribution of radiation is the foundation of relativistic-jet astrophysics.
