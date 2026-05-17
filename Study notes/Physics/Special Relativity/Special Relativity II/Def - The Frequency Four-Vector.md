---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Vector"
  - "Def - Classification of Four-Vectors"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$. A spacetime point is $X^\mu = (t,\mathbf{x})$; the Minkowski metric is $\eta_{\mu\nu} = \operatorname{diag}(+1,-1,-1,-1)$ and the inner product $A\cdot B = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$. A wave has angular frequency $\omega$, wavelength $\lambda$, and travels in the unit spatial direction $\mathbf{n}$; its wavevector is $\mathbf{k} = (\omega/c)\,\mathbf{n}$ with $|\mathbf{k}| = 2\pi/\lambda$. An observer has [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu = \gamma(c,\mathbf{u})$. Planck's reduced constant is $\hbar$. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Axiom Motivation

A wave — a ripple on water, a sound wave, a light wave — is described by two pieces of data: how fast it oscillates, the angular frequency $\omega$, and which way it travels, a direction $\mathbf{n}$ (with the wavelength fixing the spatial period). The question that forces this definition is the usual one for the topic: **frequency and direction are frame-dependent — a moving observer sees a different colour and a different direction for the same light — so how should they be packaged so that the package transforms cleanly under a Lorentz transformation?**

The clue is in the structure of a plane wave itself. A monochromatic wave travelling in direction $\mathbf{n}$ has the form
$$\phi(t,\mathbf{x}) = \cos\!\big(\omega t - \mathbf{k}\cdot\mathbf{x}\big),\qquad \mathbf{k} = \tfrac{\omega}{c}\mathbf{n},$$
and the argument $\omega t - \mathbf{k}\cdot\mathbf{x}$ is the **phase**. Now think physically about what the phase *is*. Crests and troughs are physical events: a crest of a water wave passing a buoy is a fact every observer agrees happened. The phase counts crests; it is an integer-and-a-bit at each spacetime point, and that count cannot depend on who is looking. **The phase of a wave is a Lorentz scalar.** This is the lever.

Write the phase as a contraction. If we assemble the frequency and the wavevector into a four-component object $K^\mu = (\omega, \,c\,\mathbf{k}) = \omega(1,\mathbf{n})$, then the phase is exactly the Minkowski inner product $K\cdot X = \omega t - \mathbf{k}\cdot\mathbf{x}$ of this object with the four-position $X^\mu = (t,\mathbf{x})$. We now know two things: $X^\mu$ is a [[Def - Four-Vector|four-vector]], and the contraction $K\cdot X$ is a scalar. A four-component object whose contraction with every four-vector is a scalar is itself a four-vector — that is exactly what it means to transform correctly. So $K^\mu$ is forced to be a four-vector. We did not assume it; the invariance of the phase *proved* it.

Why this particular grouping and not a variant? Because it is the unique one making the phase a contraction. Group $\omega$ with $\mathbf{k}$ any other way and $K\cdot X$ is no longer the phase, so $K^\mu$ is no longer constrained to be a four-vector and the construction collapses. And the payoff justifies the definition: once $K^\mu$ is a four-vector, the Doppler effect (how $\omega$ changes between frames) and aberration (how $\mathbf{n}$ changes) are *both* just the transformation law $K^\mu\to\Lambda^\mu{}_\nu K^\nu$ — a single matrix multiplication replaces two separate derivations.

For light there is one more constraint. A light wave travels at speed $c$, so $|\mathbf{k}| = \omega/c$, which makes $K^\mu$ a **null** four-vector: $K\cdot K = \omega^2 - c^2|\mathbf{k}|^2 = 0$. This is the wave-side shadow of the fact that the [[Def - The Four-Momentum of a Photon|photon's four-momentum]] is null — and indeed, as quantum mechanics will tell us, $P^\mu = \hbar K^\mu$, so the frequency four-vector and the photon four-momentum are the same object up to the constant $\hbar$.

---

# The Definition

Consider a plane wave of angular frequency $\omega$ propagating through Minkowski space in the unit spatial direction $\mathbf{n}$, with phase velocity $v_p$ (so $v_p = c$ for light).

**Frequency four-vector.** The **frequency four-vector** (also called the **wave four-vector**) of the wave is
$$K^\mu \;=\; \Big(\frac{\omega}{c},\ \mathbf{k}\Big) \;=\; \frac{\omega}{c}\,(1,\ \tfrac{c}{v_p}\mathbf{n}),$$
where $\mathbf{k} = (\omega/v_p)\,\mathbf{n}$ is the ordinary wavevector. In natural units, for a wave of phase velocity $c$,
$$K^\mu \;=\; \omega\,(1,\ \mathbf{n}).$$
It is a [[Def - Four-Vector|four-vector]]: under a [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$, $K^\mu\to\Lambda^\mu{}_\nu K^\nu$. The wave itself is written covariantly as
$$\phi(X) \;=\; \cos\!\big(K\cdot X\big), \qquad K\cdot X = \omega t - \mathbf{k}\cdot\mathbf{x},$$
and the **phase $K\cdot X$ is a Lorentz scalar**.

**Null condition for light.** For a wave travelling at the speed of light, $|\mathbf{k}| = \omega/c$, so the frequency four-vector is [[Def - Classification of Four-Vectors|null]]:
$$K\cdot K \;=\; \frac{\omega^2}{c^2} - |\mathbf{k}|^2 \;=\; 0.$$

**Frequency measured by an observer.** An observer with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$ measures the wave to have angular frequency
$$\omega_{\text{obs}} \;=\; \frac{U\cdot K}{c} \qquad\big(\,=\;U\cdot K\ \text{in natural units}\,\big).$$
This is the invariant form of frequency: the right-hand side is a Lorentz scalar, so it may be evaluated in any convenient frame. In the observer's own rest frame $U^\mu = (c,\mathbf{0})$ and the formula returns $\omega_{\text{obs}} = \omega$, the frequency as measured in that frame; in any other frame it gives the Doppler-shifted value automatically.

**Link to the photon.** For light regarded as a stream of **photons**, quantum mechanics supplies $E = \hbar\omega$, and the [[Def - The Four-Momentum of a Photon|photon four-momentum]] is
$$P^\mu \;=\; \hbar\,K^\mu.$$

---

# Relate to Other Fields / Compression

The frequency four-vector is the relativistic completion of a structure already familiar from wave physics: the pair $(\omega, \mathbf{k})$ is the Fourier-conjugate of the pair $(t,\mathbf{x})$, and a plane wave $e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ is the basic Fourier mode. Relativity says these two pairs are not independent: $(t,\mathbf{x})$ assemble into the four-vector $X^\mu$, and $(\omega,\mathbf{k})$ must therefore assemble into the conjugate four-vector $K^\mu$, because their pairing — the phase — is an invariant. This is exactly the statement that in relativistic Fourier analysis one transforms over *spacetime* with the four-dimensional kernel $e^{-iK\cdot X}$, and the conjugate variable is the four-vector $K^\mu$.

Through $P^\mu = \hbar K^\mu$ the definition becomes the **de Broglie relation** in four-vector form: the time component $E = \hbar\omega$ is Planck's relation and the spatial part $\mathbf{p} = \hbar\mathbf{k}$ is de Broglie's. Because both sides are four-vectors the relation is automatically Lorentz-covariant — which is why it is most naturally stated *after* special relativity, and why it is the bridge from this classical-wave object to the quantum particle. The null condition $K\cdot K = 0$ becomes the photon's mass-shell condition $P\cdot P = 0$; for a massive quantum field the analogue is $K\cdot K = (m/\hbar)^2$, the **dispersion relation**, and the plane wave $e^{-iK\cdot X}$ with this dispersion is the elementary solution of the relativistic wave equations.

---

# Examples / Corollaries

**Is an instance — light from a star.** Light of frequency $\omega$ travelling in the $+x$ direction has $K^\mu = \omega(1,1,0,0)$, manifestly null: $K\cdot K = \omega^2 - \omega^2 = 0$. An observer at rest measures $U\cdot K = c\cdot\omega/c \cdot c$... in natural units $U^\mu = (1,\mathbf{0})$ gives $\omega_{\text{obs}} = U\cdot K = \omega$, as it must.

**Is an instance — the longitudinal Doppler effect.** For the same light $K^\mu = \omega(1,1,0,0)$, an observer moving toward the source with four-velocity $U^\mu = \gamma_u(1,-u,0,0)$ measures $\omega_{\text{obs}} = U\cdot K = \gamma_u\omega(1 + u)$. With $\gamma_u = (1-u^2)^{-1/2}$ this is $\omega\sqrt{(1+u)/(1-u)}$ — the wave is blueshifted. An observer receding sees the reciprocal, a redshift. See [[Ex - The relativistic Doppler effect]].

**Is an instance — the transverse Doppler effect.** An observer moving *perpendicular* to the light's direction, $U^\mu = \gamma_u(1,0,u,0)$, measures $\omega_{\text{obs}} = U\cdot K = \gamma_u\omega$ — a pure redshift by the factor $\gamma_u$, with no first-order term. This transverse shift is a direct measurement of time dilation and has no Newtonian (Galilean) analogue, where motion across the line of sight produces no frequency change at all.

**Is NOT an instance — a static field.** A constant, non-oscillating field has $\omega = 0$ and no propagation direction; there is no frequency four-vector. The construction needs an actual wave.

**Is NOT an instance — a wave at sub-light phase velocity treated as null.** A sound wave, or a light wave in a medium with $v_p < c$, has $|\mathbf{k}| = \omega/v_p > \omega/c$, so $K\cdot K = \omega^2/c^2 - |\mathbf{k}|^2 < 0$: its frequency four-vector is *spacelike*, not null. Only a wave whose phase velocity is exactly $c$ has a null $K^\mu$. The null condition is special to light in vacuum.

**Corollary — aberration is the spatial part of the transformation.** Writing out $K'^\mu = \Lambda^\mu{}_\nu K^\nu$, the spatial components show the propagation direction $\mathbf{n}$ rotating as one changes frame: a star directly overhead in one frame appears shifted toward the direction of motion in a boosted frame. Doppler shift (the change in $\omega = K^0$) and aberration (the change in $\mathbf{n}$) are the time and space parts of one four-vector transformation.

**Calibration check.** Verify that $K\cdot X = \omega t - \mathbf{k}\cdot\mathbf{x}$ is the phase; that $K\cdot K = 0$ for light but $< 0$ for a sub-light wave; that $\omega_{\text{obs}} = U\cdot K$ returns $\omega$ in the observer's rest frame; and that the transverse Doppler shift $\omega_{\text{obs}} = \gamma_u\omega$ is purely a time-dilation effect. If you can derive both the longitudinal blueshift and redshift from the one formula $\omega_{\text{obs}} = U\cdot K$ by changing the sign of $u$, you have understood the definition.

---

# Unlocked by This

> [!tip] The Photon Four-Momentum *(from this topic)*
> Multiplying the frequency four-vector by $\hbar$ gives the [[Def - The Four-Momentum of a Photon|photon's four-momentum]] $P^\mu = \hbar K^\mu$. The null condition $K\cdot K = 0$ becomes the photon mass-shell relation $P\cdot P = 0$, and the photon enters [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] through this identification.

> [!tip] Quantum Fields and Dispersion Relations *(from Quantum Field Theory)*
> The plane wave $e^{-iK\cdot X}$ is the elementary mode of every relativistic field; the condition $K\cdot K = m^2$ (in units $\hbar = 1$) is the **dispersion relation**, null for the photon and massive for matter fields. A quantum field is a superposition of these modes, and $K^\mu$ labels them.
