---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Elastic Collisions and the Compton Effect"
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Problem Statement

A photon of energy $E_1$ (wavelength $\lambda$) scatters off an electron of mass $m_e$ initially at rest, emerging at angle $\theta$ with energy $E_1'$ (wavelength $\lambda'$): $\gamma + e^- \to \gamma + e^-$.

1. Using conservation of four-momentum, derive the Compton wavelength shift $\lambda' - \lambda = \dfrac{h}{m_e c}(1 - \cos\theta)$.
2. Show the photon always loses energy ($E_1' \le E_1$), with the shift vanishing forward ($\theta = 0$) and maximal backward ($\theta = \pi$).
3. Compute the maximum energy transferred to the electron (the "Compton edge") for an incident photon of energy $E_1$.
4. Evaluate the maximum wavelength shift numerically and explain why the Compton effect is negligible for visible light but dominant for gamma rays.

Work with $c = 1$ in the derivation; restore $c$ in the final formulas.

**Recall:**

![[Thm - Elastic Collisions and the Compton Effect#Statement]]

The [[Def - The Four-Momentum of a Photon|photon four-momentum]] is null, $P_\gamma\cdot P_\gamma = 0$, with $E = hc/\lambda$ and, relative to an observer, $P_\gamma = E(U_0 + \mathbf{n})$. The electron four-momentum satisfies $P_e\cdot P_e = m_e^2$. Conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) gives $P_\gamma + P_e = P_\gamma' + P_e'$.

---

# Convergent Strategy

**Problem class.** The flagship *collision with an unwanted particle* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|invariant-mass-technique]] type: the recoil electron is uninteresting, so isolate its four-momentum and square to eliminate it.

**Assumption pattern.** A photon (null four-momentum), an electron at rest (four-momentum $(m_e, \mathbf{0})$), an elastic process (masses preserved). The signpost is "what is the energy/wavelength of the *scattered photon*?" — the recoil electron is the unwanted particle.

**Theorem routing.** The whole derivation is conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) plus the recoil-electron mass-shell, executed as [[Thm - Elastic Collisions and the Compton Effect]] Lemma 3: rearrange to $P_e' = P_\gamma + P_e - P_\gamma'$, square to $m_e^2$, use the null photon self-squares and the rest-frame electron contractions.

**Key decision point.** The crux is isolating the *recoil electron* (the unwanted particle), not the scattered photon. Squaring then trades the recoil electron for the known $m_e^2$, and the null photon self-squares ($P_\gamma\cdot P_\gamma = 0$) make the rest collapse. Isolating the photon instead would leave a harder equation.

---

# Legal Operations Used

1. **Write down the total four-momentum and set it equal before and after** (operation 1 from the topic page). Conservation reads $P_\gamma + P_e = P_\gamma' + P_e'$.

2. **Square a four-momentum to extract an invariant mass** (operation 2). Isolating the recoil electron and squaring converts its four-momentum to the known $m_e^2$, eliminating it.

3. **Go to the rest frame of a chosen massive particle** (operation 4). The electron is initially at rest, $P_e = (m_e, \mathbf{0})$, which simplifies the contractions $P_\gamma\cdot P_e = m_e E_1$.

---

# Hints

> [!note]- Hint 1
> The recoil electron is the unwanted particle. Rearrange conservation to isolate it: $P_e' = P_\gamma + P_e - P_\gamma'$. Take the Minkowski square of both sides; the left side is $P_e'\cdot P_e' = m_e^2$.

> [!note]- Hint 2
> Expand the right side. Use $P_\gamma\cdot P_\gamma = 0$ and $P_\gamma'\cdot P_\gamma' = 0$ (null photons), $P_e\cdot P_e = m_e^2$. The cross terms with the rest-frame electron are $P_\gamma\cdot P_e = m_e E_1$ and $P_\gamma'\cdot P_e = m_e E_1'$.

> [!note]- Hint 3
> The two-photon cross term is $P_\gamma\cdot P_\gamma' = E_1 E_1'(1 - \cos\theta)$, with $\theta$ the angle between the incident and scattered photon directions. Substitute, cancel $m_e^2$, and you get $m_e E_1 - m_e E_1' = E_1 E_1'(1-\cos\theta)$.

> [!note]- Hint 4
> Divide by $m_e E_1 E_1'$ to get $\tfrac{1}{E_1'} - \tfrac{1}{E_1} = \tfrac{1}{m_e}(1-\cos\theta)$. Then $E = hc/\lambda$ gives $1/E = \lambda/hc$, so $\lambda' - \lambda = \tfrac{h}{m_ec}(1-\cos\theta)$. The maximum energy transfer is at $\theta = \pi$.

---

# Solution

Compton scattering is solved by the invariant-mass technique: isolate the unwanted recoil electron, square its four-momentum to $m_e^2$, and the null photon self-squares collapse the rest. Part 1 is this three-line derivation; Part 2 reads off the energy-loss monotonicity from $1-\cos\theta \ge 0$; Part 3 evaluates the maximum transfer at $\theta = \pi$; Part 4 compares the wavelength scale to visible and gamma-ray light.

**Step 1: The Compton wavelength shift.**

> [!note]- Derivation
> Conservation of four-momentum: $P_\gamma + P_e = P_\gamma' + P_e'$. Isolate the recoil electron (the particle whose details we do not want):
> $$P_e' = P_\gamma + P_e - P_\gamma'.$$
> Take the Minkowski square. The left side is the electron mass-shell, $P_e'\cdot P_e' = m_e^2$. The right side expands to
> $$m_e^2 = \underbrace{P_\gamma\cdot P_\gamma}_{0} + \underbrace{P_e\cdot P_e}_{m_e^2} + \underbrace{P_\gamma'\cdot P_\gamma'}_{0} + 2P_\gamma\cdot P_e - 2P_\gamma\cdot P_\gamma' - 2P_e\cdot P_\gamma',$$
> using that the photons are **null** ($P_\gamma\cdot P_\gamma = P_\gamma'\cdot P_\gamma' = 0$) and $P_e\cdot P_e = m_e^2$. With the electron initially at rest, $P_e = (m_e, \mathbf{0})$, so $P_\gamma\cdot P_e = m_e E_1$ and $P_\gamma'\cdot P_e = m_e E_1'$; the two-photon term is $P_\gamma\cdot P_\gamma' = E_1 E_1'(1-\cos\theta)$ (photons at angle $\theta$). Substituting:
> $$m_e^2 = m_e^2 + 2m_e E_1 - 2E_1 E_1'(1-\cos\theta) - 2m_e E_1'.$$
> Cancel $m_e^2$ and divide by $2$:
> $$m_e E_1 - m_e E_1' = E_1 E_1'(1-\cos\theta).$$
> Divide by $m_e E_1 E_1'$:
> $$\frac{1}{E_1'} - \frac{1}{E_1} = \frac{1}{m_e}(1-\cos\theta).$$
> Since $E = hc/\lambda$, $1/E = \lambda/(hc)$, so multiplying by $hc$:
> $$\boxed{\ \lambda' - \lambda = \frac{h}{m_e c}(1-\cos\theta)\ },$$
> the Compton wavelength shift, with $h/m_e c = 2.426\times10^{-12}$ m the electron Compton wavelength.

**Step 2: The photon always loses energy.**

> [!note]- Derivation
> From $\tfrac{1}{E_1'} - \tfrac{1}{E_1} = \tfrac{1}{m_e}(1-\cos\theta)$ and $1 - \cos\theta \ge 0$ for all $\theta$, we have $\tfrac{1}{E_1'} \ge \tfrac{1}{E_1}$, hence $E_1' \le E_1$: the scattered photon has *less* energy than the incident one (and correspondingly $\lambda' \ge \lambda$). Equality holds only when $\cos\theta = 1$, i.e. $\theta = 0$ — forward scattering is a "miss" with no energy transfer. The shift is maximal at $\theta = \pi$ (backward scattering, a head-on hit), where $1 - \cos\theta = 2$ and $\lambda' - \lambda = 2h/m_ec$. Physically the photon must give the electron recoil momentum, and to conserve energy it sacrifices some of its own — more for a harder (larger-angle) bounce.

**Step 3: The Compton edge.**

> [!note]- Derivation
> The energy transferred to the electron is $\Delta E = E_1 - E_1'$, maximal at $\theta = \pi$. From the energy form $\tfrac{1}{E_1'} = \tfrac{1}{E_1} + \tfrac{1-\cos\theta}{m_e}$, at $\theta = \pi$,
> $$\frac{1}{E_1'} = \frac{1}{E_1} + \frac{2}{m_e} = \frac{m_e + 2E_1}{m_e E_1} \;\Longrightarrow\; E_1' = \frac{m_e E_1}{m_e + 2E_1}.$$
> The maximum energy transfer (the **Compton edge**) is
> $$\Delta E_{\max} = E_1 - E_1' = E_1\Big(1 - \frac{m_e}{m_e + 2E_1}\Big) = \frac{2E_1^2}{m_e + 2E_1}.$$
> For $E_1 \ll m_e$ (low-energy photon) this is $\approx 2E_1^2/m_e$, small; for $E_1 \gg m_e$ (high-energy photon) it approaches $E_1 - m_e/2$, so nearly all the photon energy is transferred. The Compton edge appears as a sharp cutoff in the energy spectrum of recoil electrons in gamma-ray detectors.

**Step 4: The wavelength scale.**

> [!note]- Derivation
> The maximum wavelength shift is $2h/m_ec = 2\times 2.426\times10^{-12}\ \text{m} = 4.85\times10^{-12}$ m $= 4.85$ pm.
>
> - **Visible light:** $\lambda \approx 500$ nm $= 5\times10^{-7}$ m. The fractional shift is at most $(\lambda'-\lambda)/\lambda \approx 4.85\times10^{-12}/5\times10^{-7} \approx 10^{-5}$ — utterly negligible. Visible photons scatter off electrons without measurable colour change.
> - **Gamma rays:** $\lambda \sim 10^{-12}$ m (energy $\sim$ MeV). The shift $\sim 2.4$ pm is *comparable to the wavelength itself*, so the energy change is order-unity. The Compton effect dominates.
>
> The dividing scale is the electron Compton wavelength $h/m_ec$, equivalently the photon energy $m_ec^2 = 511$ keV: the effect is significant only for photons with $\lambda \lesssim h/m_ec$, i.e. $E_1 \gtrsim m_ec^2$ — X-rays and gamma rays. This is why Compton's original experiment used X-rays ($\lambda = 70.8$ pm from molybdenum $K_\alpha$), where the few-pm shift is measurable.

> [!note]- Complete formal solution
> Conservation $P_\gamma + P_e = P_\gamma' + P_e'$; isolate the recoil electron $P_e' = P_\gamma + P_e - P_\gamma'$ and square to $m_e^2$. Using $P_\gamma\cdot P_\gamma = P_\gamma'\cdot P_\gamma' = 0$, $P_e = (m_e,\mathbf{0})$ so $P_\gamma\cdot P_e = m_e E_1$, $P_\gamma'\cdot P_e = m_e E_1'$, and $P_\gamma\cdot P_\gamma' = E_1 E_1'(1-\cos\theta)$, one gets $m_e E_1 - m_e E_1' = E_1 E_1'(1-\cos\theta)$, hence $\tfrac{1}{E_1'}-\tfrac{1}{E_1} = \tfrac{1}{m_e}(1-\cos\theta)$ and $\lambda'-\lambda = \tfrac{h}{m_ec}(1-\cos\theta)$. Since $1-\cos\theta\ge0$, $E_1'\le E_1$ (photon always loses energy), maximal at $\theta=\pi$ where $E_1' = m_eE_1/(m_e+2E_1)$ and $\Delta E_{\max} = 2E_1^2/(m_e+2E_1)$ (the Compton edge). The maximum wavelength shift $2h/m_ec = 4.85$ pm is negligible against visible wavelengths ($\sim 10^{-5}$ fractional) but order-unity for gamma rays, so the effect matters only for $E_1 \gtrsim m_ec^2 = 511$ keV. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to isolate the *scattered photon* instead, $P_\gamma' = P_\gamma + P_e - P_e'$, and square. But $P_\gamma'\cdot P_\gamma' = 0$ (null) gives an equation still containing the unknown recoil electron $P_e'$ through the cross terms $P_e\cdot P_e'$ and $P_\gamma\cdot P_e'$ — the recoil electron is *not* eliminated, and you are left with its unknown energy and direction. The technique only works when you isolate and square the four-momentum you do *not* want (the recoil electron), so that *it* becomes the known $m_e^2$. Always square the unwanted particle.

---

# Key Takeaways

**Isolate and square the unwanted particle — the recoil electron, not the scattered photon.** The entire Compton derivation hinges on one decision: which four-momentum to isolate before squaring. The answer is always the particle you do *not* care about — here the recoil electron, whose energy and direction are not asked for. Isolating it ($P_e' = P_\gamma + P_e - P_\gamma'$) and squaring turns *it* into the known $m_e^2$, eliminating it from the problem; what remains is a scalar equation in the photon energies and the scattering angle. Isolating the scattered photon instead would leave the recoil electron in the equation, defeating the purpose. The reusable reflex, drilled by this exercise and by [[Ex - Two-body decay kinematics|two-body decay]] and [[Ex - Threshold energy for particle production|thresholds]]: identify the unwanted particle, isolate its four-momentum, square it to its mass-shell.

**Null photons make the algebra collapse — $P_\gamma\cdot P_\gamma = 0$ is what does the work.** The reason Compton scattering is a *clean* calculation, despite involving four particles, is that the photons contribute null four-momenta whose self-squares vanish on squaring. Of the six terms in the expanded square, two ($P_\gamma\cdot P_\gamma$ and $P_\gamma'\cdot P_\gamma'$) are zero outright, and the rest-frame electron makes two more ($P_\gamma\cdot P_e$, $P_\gamma'\cdot P_e$) trivially $m_e$ times an energy. The only nontrivial term is the two-photon cross product $P_\gamma\cdot P_\gamma' = E_1 E_1'(1-\cos\theta)$, which carries the angle dependence. The trigger: whenever a photon appears in a conservation equation, remember its null self-square, which is exactly what makes it the *easiest* participant to handle — a massless particle simplifies the algebra rather than complicating it.

**The electron Compton wavelength sets the scale — the effect matters only near $m_ec^2$.** The wavelength shift is of order $h/m_ec = 2.4$ pm, independent of the incident wavelength, so the *fractional* shift is significant only when $\lambda \lesssim h/m_ec$, i.e. when the photon energy approaches the electron rest energy $m_ec^2 = 511$ keV. This is why the Compton effect is invisible for visible light (fractional shift $\sim 10^{-5}$) but dominant for gamma rays (order-unity), and why Compton needed X-rays to see it. The reusable diagnostic: to judge whether a quantum/relativistic photon effect is observable, compare the relevant energy to the rest energy of the particle it interacts with — for electrons, $511$ keV. Below that scale the photon behaves classically; near and above it, its particle nature (the recoil, the energy transfer) takes over. This same scale, $m_ec^2$, sets the threshold for pair production and is the natural energy unit of QED.
