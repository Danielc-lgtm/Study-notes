---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

A photon of angular frequency $\omega$ strikes an electron of rest mass $m_e$ that is initially **at rest**. The photon scatters off at an angle $\theta$ to its original direction, with a new frequency $\omega'$; the electron recoils. This is **Compton scattering**, $\gamma + e^- \to \gamma + e^-$.

Show that the scattered photon's frequency satisfies
$$\frac{1}{\omega'} - \frac{1}{\omega} \;=\; \frac{\hbar}{m_e c^2}\,(1 - \cos\theta),$$
equivalently $\hbar\,\omega\omega'(1-\cos\theta) = m_ec^2(\omega - \omega')$, and hence that the scattered photon is always *redshifted*, $\omega' \le \omega$.

**Recall:**

![[Def - The Four-Momentum of a Photon#The Definition]]

![[Thm - Conservation of Four-Momentum#Statement]]

A photon of frequency $\omega$ travelling in unit direction $\mathbf{e}$ has four-momentum $P_\gamma^\mu = \dfrac{\hbar\omega}{c}(1,\mathbf{e})$, which is null: $P_\gamma\cdot P_\gamma = 0$. An electron of rest mass $m_e$ has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P_e^\mu$ with $P_e\cdot P_e = m_e^2c^2$.

---

# Convergent Strategy

**Problem class.** This is a *collision-kinematics* problem with an unwanted final-state particle: we are asked about the photon's frequency, not the recoil electron's motion.

**Assumption pattern.** Four bodies appear — incoming photon, incoming (rest) electron, outgoing photon, outgoing electron — but the recoil electron's four-momentum $P_e'$ is a nuisance: it does not appear in the answer. The pattern "a final-state particle you do not care about" triggers the elimination-by-squaring technique.

**Theorem routing.** [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]] gives $P_\gamma + P_e = P_\gamma' + P_e'$. Isolate the unwanted $P_e'$ on one side: $P_e' = P_\gamma + P_e - P_\gamma'$. Square both sides; the left becomes the known invariant $m_e^2c^2$, and the right is a sum of inner products, two of which vanish because the photons are null ($P_\gamma\cdot P_\gamma = P_\gamma'\cdot P_\gamma' = 0$).

**Key decision point.** The decisive move is *rearrange to isolate $P_e'$, then square*. Squaring converts the unwanted electron four-momentum into the scalar $m_e^2c^2$, removing it from the problem entirely, while the photons' nullity kills two more terms. The recoil electron's speed and direction never need to be found.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — $P_\gamma + P_e = P_\gamma' + P_e'$.
2. **Square a four-momentum to extract an invariant mass** — squaring the isolated $P_e'$ gives $m_e^2c^2$.
3. **Go to the rest frame of a chosen particle** — the electron's initial rest frame, where $P_e = (m_ec,\mathbf{0})$.
4. **Use the photon's null four-momentum** — $P_\gamma\cdot P_\gamma = P_\gamma'\cdot P_\gamma' = 0$ removes two terms.

---

# Hints

> [!note]- Hint 1
> You are asked about the photon frequencies, not the recoil electron. The recoil electron's four-momentum $P_e'$ is a quantity you want to *eliminate*. How do you remove an unwanted four-momentum from a conservation equation?

> [!note]- Hint 2
> Conservation of four-momentum: $P_\gamma + P_e = P_\gamma' + P_e'$. Rearrange so $P_e'$ is alone: $P_e' = P_\gamma + P_e - P_\gamma'$. Now square both sides — take the Minkowski inner product of each side with itself.

> [!note]- Hint 3
> The left side becomes $P_e'\cdot P_e' = m_e^2c^2$, a known number. On the right, expand $(P_\gamma + P_e - P_\gamma')^2$. Two terms vanish: $P_\gamma\cdot P_\gamma = 0$ and $P_\gamma'\cdot P_\gamma' = 0$, because photons are null.

> [!note]- Hint 4
> Work in the electron's initial rest frame, $P_e = (m_ec,\mathbf{0})$. Then $P_e\cdot P_\gamma = m_e\hbar\omega$, $P_e\cdot P_\gamma' = m_e\hbar\omega'$, and $P_\gamma\cdot P_\gamma' = (\hbar^2\omega\omega'/c^2)(1-\cos\theta)$ where $\theta$ is the angle between the two photon directions.

---

# Solution

The recoil electron is a nuisance variable; the technique is to isolate its four-momentum and square it away. Squaring turns $P_e'$ into the known invariant $m_e^2c^2$, and the photons' nullity kills two further terms, leaving a one-line relation between the frequencies.

**Step 1: Conservation of four-momentum, with the electron isolated.**

$P_e' = P_\gamma + P_e - P_\gamma'$.

> [!note]- Derivation
> Label the four bodies: incoming photon $P_\gamma$, incoming electron $P_e$, outgoing photon $P_\gamma'$, outgoing (recoil) electron $P_e'$. With no external forces, [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] reads
> $$P_\gamma + P_e = P_\gamma' + P_e'.$$
> The answer involves only the photon frequencies; the recoil electron $P_e'$ is to be eliminated. Move everything except $P_e'$ to the other side:
> $$P_e' = P_\gamma + P_e - P_\gamma'.$$
> This isolates the unwanted four-momentum, ready to be squared away.

**Step 2: Square both sides.**

$m_e^2c^2 = P_e'\cdot P_e' = (P_\gamma + P_e - P_\gamma')^2$, and after using the photons' nullity this becomes $m_e^2c^2 = m_e^2c^2 + 2P_e\cdot P_\gamma - 2P_e\cdot P_\gamma' - 2P_\gamma\cdot P_\gamma'$.

> [!note]- Derivation
> Take the Minkowski inner product of each side of $P_e' = P_\gamma + P_e - P_\gamma'$ with itself.
>
> Left side: by the [[Def - Four-Momentum and Rest Mass|mass-shell relation]], $P_e'\cdot P_e' = m_e^2c^2$ — the recoil electron is on its mass shell, whatever its speed and direction. This is the whole point: squaring has replaced the unknown four-vector by the *known number* $m_e^2c^2$.
>
> Right side: expand the square of the three-term sum,
> $$(P_\gamma + P_e - P_\gamma')^2 = P_\gamma\cdot P_\gamma + P_e\cdot P_e + P_\gamma'\cdot P_\gamma' + 2P_\gamma\cdot P_e - 2P_\gamma\cdot P_\gamma' - 2P_e\cdot P_\gamma'.$$
> Now use the mass shells:
> - $P_\gamma\cdot P_\gamma = 0$ — the incoming photon is [[Def - The Four-Momentum of a Photon|null]];
> - $P_\gamma'\cdot P_\gamma' = 0$ — the outgoing photon is null;
> - $P_e\cdot P_e = m_e^2c^2$ — the incoming electron is on its mass shell.
>
> Two of the six terms vanish. So
> $$m_e^2c^2 = m_e^2c^2 + 2P_e\cdot P_\gamma - 2P_e\cdot P_\gamma' - 2P_\gamma\cdot P_\gamma'.$$
> The $m_e^2c^2$ cancels from both sides, leaving the clean relation
> $$P_e\cdot P_\gamma - P_e\cdot P_\gamma' = P_\gamma\cdot P_\gamma'.$$

**Step 3: Evaluate the inner products in the electron's rest frame.**

In the frame where the electron is initially at rest, the relation becomes $m_e\hbar(\omega - \omega') = \dfrac{\hbar^2\omega\omega'}{c^2}(1-\cos\theta)$.

> [!note]- Derivation
> Each surviving inner product is a Lorentz scalar, so evaluate them in whatever frame is easiest — the electron's initial **rest frame**, where $P_e = (m_ec,\mathbf{0})$. The photon four-momenta there are
> $$P_\gamma = \frac{\hbar\omega}{c}(1,\mathbf{e}), \qquad P_\gamma' = \frac{\hbar\omega'}{c}(1,\mathbf{e}'),$$
> with $\mathbf{e},\mathbf{e}'$ unit vectors and $\mathbf{e}\cdot\mathbf{e}' = \cos\theta$, $\theta$ the scattering angle.
>
> $$P_e\cdot P_\gamma = (m_ec)\Big(\frac{\hbar\omega}{c}\Big) - \mathbf{0}\cdot(\cdots) = m_e\hbar\omega,$$
> $$P_e\cdot P_\gamma' = (m_ec)\Big(\frac{\hbar\omega'}{c}\Big) = m_e\hbar\omega',$$
> $$P_\gamma\cdot P_\gamma' = \frac{\hbar\omega}{c}\cdot\frac{\hbar\omega'}{c}\big(1\cdot 1 - \mathbf{e}\cdot\mathbf{e}'\big) = \frac{\hbar^2\omega\omega'}{c^2}(1 - \cos\theta).$$
> Substituting into $P_e\cdot P_\gamma - P_e\cdot P_\gamma' = P_\gamma\cdot P_\gamma'$:
> $$m_e\hbar\omega - m_e\hbar\omega' = \frac{\hbar^2\omega\omega'}{c^2}(1-\cos\theta),$$
> that is,
> $$m_ec^2(\omega - \omega') = \hbar\,\omega\omega'\,(1-\cos\theta).$$

**Step 4: Rearrange into the Compton formula.**

Dividing by $\hbar\omega\omega'$ gives $\dfrac{1}{\omega'} - \dfrac{1}{\omega} = \dfrac{\hbar}{m_ec^2}(1-\cos\theta) \ge 0$, so $\omega' \le \omega$.

> [!note]- Derivation
> Divide both sides of $m_ec^2(\omega-\omega') = \hbar\omega\omega'(1-\cos\theta)$ by $m_ec^2\,\omega\omega'$:
> $$\frac{\omega - \omega'}{\omega\omega'} = \frac{\hbar}{m_ec^2}(1-\cos\theta) \;\Longrightarrow\; \frac{1}{\omega'} - \frac{1}{\omega} = \frac{\hbar}{m_ec^2}(1-\cos\theta).$$
> In terms of wavelength, $\omega = 2\pi c/\lambda$, this is the familiar Compton form
> $$\lambda' - \lambda = \frac{2\pi\hbar}{m_ec}(1-\cos\theta) = \frac{h}{m_ec}(1-\cos\theta),$$
> with $h/m_ec$ the **Compton wavelength** of the electron.
>
> Since $1 - \cos\theta \ge 0$ for every scattering angle (with equality only at $\theta = 0$, forward scattering — no collision), the right side is non-negative. Hence $1/\omega' \ge 1/\omega$, i.e. $\omega' \le \omega$: **the scattered photon always has lower frequency (longer wavelength) than the incident one** — it is redshifted. Physically, the photon hands some of its energy to the recoiling electron, and a less energetic photon is a lower-frequency one. The shift is largest for back-scattering, $\theta = \pi$, where $1-\cos\theta = 2$.

> [!note]- Complete formal solution
> Conservation of four-momentum: $P_\gamma + P_e = P_\gamma' + P_e'$. Isolate the recoil electron, $P_e' = P_\gamma + P_e - P_\gamma'$, and square:
> $$m_e^2c^2 = P_e'\cdot P_e' = (P_\gamma + P_e - P_\gamma')^2 = \underbrace{P_\gamma^2}_{0} + \underbrace{P_e^2}_{m_e^2c^2} + \underbrace{P_\gamma'^2}_{0} + 2P_\gamma\cdot P_e - 2P_\gamma\cdot P_\gamma' - 2P_e\cdot P_\gamma',$$
> using $P_\gamma^2 = P_\gamma'^2 = 0$ (photons null) and $P_e^2 = m_e^2c^2$. Cancelling $m_e^2c^2$:
> $$P_e\cdot P_\gamma - P_e\cdot P_\gamma' = P_\gamma\cdot P_\gamma'.$$
> In the electron's initial rest frame, $P_e = (m_ec,\mathbf{0})$, $P_\gamma = (\hbar\omega/c)(1,\mathbf{e})$, $P_\gamma' = (\hbar\omega'/c)(1,\mathbf{e}')$, $\mathbf{e}\cdot\mathbf{e}'=\cos\theta$:
> $$m_e\hbar\omega - m_e\hbar\omega' = \frac{\hbar^2\omega\omega'}{c^2}(1-\cos\theta).$$
> Dividing by $\hbar\omega\omega'$:
> $$\frac{1}{\omega'} - \frac{1}{\omega} = \frac{\hbar}{m_ec^2}(1-\cos\theta) \ge 0,$$
> so $\omega'\le\omega$: the scattered photon is redshifted. $\blacksquare$

---

# Key Takeaways

**Isolate the particle you do not care about, then square it away.** Compton scattering has four participants, but the answer mentions only two — the photon's incoming and outgoing frequencies. The recoil electron is dead weight. The universal technique for shedding such dead weight is to rearrange the conservation equation so the unwanted four-momentum stands alone, then take the Minkowski square: $P_e'\cdot P_e'$ collapses to the *known number* $m_e^2c^2$, and the unwanted particle's velocity and direction never enter. This is the single most important manoeuvre in relativistic collision physics, and it works because conservation of four-momentum is a *vector* equation that one is free to square. The trigger is precise: whenever a final-state particle appears in the conservation law but not in the question, isolate and square.

**A photon's nullity, $P_\gamma\cdot P_\gamma = 0$, is a gift — it deletes terms.** When the expression $(P_\gamma + P_e - P_\gamma')^2$ is expanded, two of its six terms vanish outright because each photon's self-inner-product is zero. A massless particle is, computationally, the friendliest object in a collision problem: every time its four-momentum is squared, the term disappears. This is why photon problems — Compton scattering, pair production, the Doppler effect — are often *shorter* than all-massive-particle problems despite seeming more exotic. Whenever a photon's four-momentum gets squared, write $0$ immediately.

**The Compton shift is the experiment that proved light is made of particles.** The derivation treats the photon as a particle with a definite four-momentum $P_\gamma^\mu = (\hbar\omega/c)(1,\mathbf{e})$ and applies conservation of four-momentum exactly as for two billiard balls. A pure wave theory of light predicts *no* frequency shift on scattering — a wave driving an electron re-radiates at the same frequency. The observed shift $\lambda' - \lambda = (h/m_ec)(1-\cos\theta)$, matching this calculation, was Compton's 1923 demonstration that light carries momentum in discrete quanta. The broader lesson for the topic: a photon, though massless and lacking a rest frame, participates in conservation of four-momentum on exactly the same footing as massive matter — and treating it so yields quantitative, experimentally confirmed predictions. The Compton wavelength $h/m_ec$ that sets the scale is itself a bridge: it is the length at which quantum and relativistic effects for the electron become comparable, and it reappears throughout quantum field theory.
