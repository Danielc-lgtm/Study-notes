---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - Motion of a Charge in a Uniform Field"
  - "Def - The Lorentz Four-Force"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

A particle of charge $q$, rest mass $m$, and momentum $P = \Gamma_0 m V_0$ moves in a uniform magnetic field $\mathbf{B} = B\,e_3$ (no electric field), with initial velocity at pitch angle $\theta$ to $\mathbf{B}$.

1. From the equation of motion, derive the **cyclotron frequency** $\omega_B = qB/m$ governing the circular part of the motion, and show the speed (hence $\Gamma_0$) is constant.
2. Derive the **Larmor radius** $R = \Gamma_0 V_0\sin\theta/\omega_B = P\sin\theta/(qB)$, and use it to express the particle's momentum in terms of a measured radius: $P_\perp = qBR$.
3. Show that the *orbital* angular frequency, in coordinate time, is the **gyration frequency** $\omega = \omega_B/\Gamma_0$, *not* $\omega_B$ — the cyclotron frequency itself is the proper-time rate.
4. A proton ($q = e$, $m = 1.67\times10^{-27}\,$kg) and an electron move in a $1\,$T field. Compute $\omega_B$ for each; explain why a cyclotron with a fixed accelerating frequency works for protons (at modest energy) but not for electrons.

**Recall:**

![[Thm - Motion of a Charge in a Uniform Field#Statement]]

The equation of motion is the [[Def - The Lorentz Four-Force|Lorentz four-force]] law $m\,dU^\mu/d\tau = qF^\mu{}_\nu U^\nu$. The [[Def - Four-Momentum and Rest Mass|momentum]] is $P = \Gamma_0 m V_0$ with $\Gamma_0 = (1-V_0^2/c^2)^{-1/2}$. The magnetic field does no work, so $\Gamma_0$ is constant.

---

# Convergent Strategy

**Problem class.** A *trajectory-and-frequency* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.3]]: solve the circular motion in a magnetic field and extract the frequency, radius, and momentum relation. The routine is to decouple the equation of motion and read off the gyration parameters.

**Assumption pattern.** A pure magnetic field, so the motion is bounded and the speed is constant (the magnetic field does no work). The assumption "no electric field" is what makes $\Gamma_0$ constant and the frequency well-defined; the pitch angle $\theta$ is what splits the velocity into a transverse (circular) part and a longitudinal (drift along $\mathbf{B}$) part. The signpost is the constancy of the speed, which is the magnetic-field-does-no-work fact in action.

**Theorem routing.** Parts 1–3 route through the circular part of the [[Thm - Motion of a Charge in a Uniform Field|equation of motion]], yielding $\omega_B = qB/m$, $R = P\sin\theta/(qB)$, and the coordinate-time frequency $\omega = \omega_B/\Gamma_0$. Part 4 is numerical, applying the formula and the resonance discussion.

**Key decision point.** The crucial distinction is between the cyclotron frequency $\omega_B = qB/m$ (constant, the *proper-time* rate of the four-velocity's rotation) and the orbital frequency $\omega = \omega_B/\Gamma_0$ (the *coordinate-time* rate, velocity-dependent). The temptation is to use $\omega_B$ as the frequency at which the particle visibly circles; the resolution, which underlies the whole resonance discussion, is that the coordinate-time frequency is slowed by $\Gamma_0$.

---

# Legal Operations Used

1. **Operation 6 (write the equation of motion and decouple it)** from the topic page: separate the circular (magnetic) part. This is parts 1–3.

2. **Operation 7 (use that the magnetic field does no work)** from the topic page: conclude the speed and $\Gamma_0$ are constant. This is part 1.

3. **Operation 8 (extract the cyclotron frequency and Larmor radius)** from the topic page: this exercise *is* operation 8 in detail.

---

# Hints

> [!note]- Hint 1
> The transverse equations of motion are $\dot u^1 = \omega_B u^2$, $\dot u^2 = -\omega_B u^1$ with $\omega_B = qB/m$. Combine into $w = u^1 + iu^2$, $\dot w = -i\omega_B w$, so $w$ rotates at $\omega_B$ in proper time. Since $|w|$ is constant, the transverse speed is constant.

> [!note]- Hint 2
> The transverse velocity has magnitude $V_\perp = V_0\sin\theta$; in coordinate time it circles at angular frequency $\omega = \omega_B/\Gamma_0$, so the radius is $R = V_\perp/\omega = \Gamma_0 V_0\sin\theta/\omega_B$. Writing $P = \Gamma_0 m V_0$, this is $R = P\sin\theta/(qB)$, i.e. $P_\perp = qBR$.

> [!note]- Hint 3
> The cyclotron frequency $\omega_B = qB/m$ is the rate of rotation in *proper* time $\tau$. The relation between proper and coordinate time is $dt = \Gamma_0\,d\tau$ (constant since $\Gamma_0$ is constant), so the rotation rate in coordinate time is $\omega = \omega_B/\Gamma_0$.

> [!note]- Hint 4
> $\omega_B = qB/m$: for the proton, $\omega_B = (1.6\times10^{-19})(1)/(1.67\times10^{-27}) \approx 9.6\times10^7\,$rad/s; for the electron, $\approx 1.76\times10^{11}\,$rad/s. The electron goes relativistic at low energy ($\Gamma_0\gg1$ quickly), so its orbital frequency $\omega_B/\Gamma_0$ drifts away from any fixed accelerating frequency; the heavier proton stays near $\Gamma_0\approx1$ longer.

---

# Solution

The plan: decouple the magnetic motion to get the cyclotron frequency and constant speed (Step 1), find the Larmor radius and momentum relation (Step 2), distinguish the proper-time and coordinate-time frequencies (Step 3), and apply numerically with the resonance discussion (Step 4). The pivotal subtlety is the $\Gamma_0$ between $\omega_B$ and the orbital frequency.

**Step 1: The cyclotron frequency and constant speed.**

> [!note]- Derivation
> For $\mathbf{B} = B\,e_3$, $\mathbf{E} = 0$, the [[Thm - Motion of a Charge in a Uniform Field|equation of motion]] in the transverse plane is
> $$\dot u^1 = \omega_B u^2, \qquad \dot u^2 = -\omega_B u^1, \qquad \omega_B = \frac{qB}{m}.$$
> Combine into the complex variable $w = u^1 + iu^2$: $\dot w = \dot u^1 + i\dot u^2 = \omega_B u^2 - i\omega_B u^1 = -i\omega_B w$, so $w(\tau) = w(0)e^{-i\omega_B\tau}$. The transverse four-velocity rotates at the **cyclotron frequency** $\omega_B = qB/m$ in proper time. Since $|w|^2 = (u^1)^2 + (u^2)^2$ is constant, and the longitudinal $u^3$ is also constant (the $e_3$ equation is $\dot u^3 = 0$), the whole speed is constant: the magnetic field does no work, so $\Gamma_0$ (and the energy) is fixed. The trajectory is a helix — circular motion in the transverse plane, uniform drift along $\mathbf{B}$.

**Step 2: The Larmor radius and momentum.**

> [!note]- Derivation
> The transverse velocity has magnitude $V_\perp = V_0\sin\theta$ (the component of $V_0$ perpendicular to $\mathbf{B}$). In coordinate time the particle circles at the orbital frequency $\omega = \omega_B/\Gamma_0$ (Step 3), so the radius is
> $$R = \frac{V_\perp}{\omega} = \frac{V_0\sin\theta}{\omega_B/\Gamma_0} = \frac{\Gamma_0 V_0\sin\theta}{\omega_B}.$$
> Substituting $\omega_B = qB/m$ and $P = \Gamma_0 m V_0$ (the momentum magnitude):
> $$R = \frac{\Gamma_0 V_0\sin\theta\cdot m}{qB} = \frac{P\sin\theta}{qB}, \qquad\text{i.e.}\qquad P_\perp = P\sin\theta = qBR.$$
> This is the **Larmor radius** formula, and run backwards it is the basis of magnetic spectrometry: a particle's transverse momentum is $qBR$, so *measuring the radius of its track in a known field gives its momentum*. Every particle detector uses this.

**Step 3: Orbital frequency versus cyclotron frequency.**

> [!note]- Derivation
> The cyclotron frequency $\omega_B = qB/m$ governs the rotation in *proper* time $\tau$, as the solution $w\propto e^{-i\omega_B\tau}$ shows. But an experimenter watches the particle in *coordinate* time $t$. Since the speed is constant, $\Gamma_0$ is constant, and proper and coordinate time are related by $dt = \Gamma_0\,d\tau$. Therefore the rotation rate in coordinate time — the **gyration (synchrotron) frequency** — is
> $$\omega = \frac{\omega_B}{\Gamma_0} = \frac{qB}{\Gamma_0 m}.$$
> The orbital frequency is *slowed* by the relativistic factor $\Gamma_0$: a faster particle circles more slowly (in coordinate time) than $\omega_B$ would suggest, because its effective inertia $\Gamma_0 m$ is larger. At non-relativistic speeds $\Gamma_0\approx1$ and $\omega\approx\omega_B$; at high energy the two diverge.

**Step 4: Numerical values and the resonance condition.**

> [!note]- Derivation
> $\omega_B = qB/m$ in a $1\,$T field:
> $$\omega_B^{\text{proton}} = \frac{(1.60\times10^{-19})(1)}{1.67\times10^{-27}} \approx 9.6\times10^7\,\text{rad/s}, \qquad \omega_B^{\text{electron}} = \frac{(1.60\times10^{-19})(1)}{9.11\times10^{-31}} \approx 1.76\times10^{11}\,\text{rad/s}.$$
> A cyclotron accelerates by an oscillating electric field tuned to the orbital frequency. But the *orbital* frequency is $\omega = \omega_B/\Gamma_0$, which drifts as the particle speeds up. **Electrons** reach $\Gamma_0\gg1$ at very low kinetic energy (their rest energy is only $0.51\,$MeV, so even a few MeV makes them relativistic), so their orbital frequency falls rapidly away from any fixed accelerating frequency — a fixed-frequency cyclotron cannot keep them in resonance, and electrons are accelerated electrostatically or in linacs instead. **Protons** (rest energy $938\,$MeV) stay near $\Gamma_0\approx1$ up to $\sim20\,$MeV, so a fixed-frequency cyclotron keeps them roughly in resonance over that range — which is exactly the energy ceiling of a simple proton cyclotron. Beyond it one ramps the frequency (synchrocyclotron) or the field (synchrotron).

> [!note]- Complete formal solution
> The transverse equation of motion $\dot u^1 = \omega_B u^2$, $\dot u^2 = -\omega_B u^1$ gives $w = u^1+iu^2 \propto e^{-i\omega_B\tau}$ with $\omega_B = qB/m$; constant $|w|$ means constant speed (the magnetic field does no work, $\Gamma_0$ fixed). The radius is $R = V_\perp/\omega = \Gamma_0 V_0\sin\theta/\omega_B = P\sin\theta/(qB)$, so $P_\perp = qBR$. The orbital frequency in coordinate time is $\omega = \omega_B/\Gamma_0$ (since $dt = \Gamma_0 d\tau$), not $\omega_B$. Numerically $\omega_B^{\text{proton}}\approx9.6\times10^7$, $\omega_B^{\text{electron}}\approx1.76\times10^{11}\,$rad/s in $1\,$T; a fixed-frequency cyclotron keeps protons in resonance up to $\sim20\,$MeV but fails for electrons, which go relativistic at low energy and detune $\omega = \omega_B/\Gamma_0$. $\blacksquare$

---

# Key Takeaways

**Track radius measures momentum: $P_\perp = qBR$.** The Larmor-radius formula, run backwards, is the single most-used measurement in experimental particle physics: a charged particle's transverse momentum is $qBR$, so the curvature of its track in a known magnetic field directly gives its momentum. Every magnetic spectrometer, every bubble chamber, every modern tracking detector exploits this. The relativistic content is that the relevant momentum is the *relativistic* $P = \Gamma_0 m V_0$, not the Newtonian $mV_0$, so the formula holds unchanged into the ultrarelativistic regime where $P\approx\mathfrak{E}/c$. The trigger "curved track in a magnetic field" reacts to "$P_\perp = qBR$", and the reusable diagnostic is that the radius scales linearly with momentum at *fixed* field — which is also why higher-momentum particles in a detector are harder to distinguish from straight tracks.

**The cyclotron frequency is constant but the orbital frequency is not.** The subtle and consequential distinction is between $\omega_B = qB/m$ — the proper-time rotation rate, depending only on the field and the charge-to-mass ratio, hence *constant* — and the orbital frequency $\omega = \omega_B/\Gamma_0$ — the coordinate-time rate an observer sees, *slowed* by the relativistic factor. The reason a faster particle circles more slowly is its larger effective inertia $\Gamma_0 m$. This $\Gamma_0$ is not a technicality: it is the entire reason simple cyclotrons fail at high energy. Whenever a frequency in a magnetic field is in play, the question to ask is "proper time or coordinate time?" — the cyclotron frequency is the former, the observable orbital frequency the latter.

**Resonance detuning drives accelerator design.** The fact that the orbital frequency drifts as $\omega_B/\Gamma_0$ is what forced the evolution of accelerators beyond the simple cyclotron. Because electrons go relativistic at $\sim$MeV energies (rest energy only $0.51\,$MeV), their orbital frequency falls quickly and a fixed-frequency cyclotron cannot accelerate them — they are handled electrostatically or in linacs. Protons (rest energy $938\,$MeV) stay near $\Gamma_0\approx1$ up to $\sim20\,$MeV, the ceiling of a simple proton cyclotron. To go higher, one either ramps the accelerating frequency to track $\omega_B/\Gamma_0$ (the synchrocyclotron) or holds the particle on a fixed radius by ramping the field (the synchrotron, [[Ex - Synchrotron field ramp and the LHC magnets|next exercise]]). The reusable lesson is that a single relativistic correction — the $\Gamma_0$ in the orbital frequency — dictates the architecture of every high-energy circular machine.
