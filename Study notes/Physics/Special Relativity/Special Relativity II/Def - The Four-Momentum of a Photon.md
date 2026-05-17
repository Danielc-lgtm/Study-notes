---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Frequency Four-Vector"
  - "Def - Classification of Four-Vectors"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$, with $c$ restored where useful. The Minkowski metric is $\eta_{\mu\nu} = \operatorname{diag}(+1,-1,-1,-1)$, inner product $A\cdot B = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$. A photon has energy $E$, three-momentum $\mathbf{p}$, angular frequency $\omega$, and travels in unit direction $\mathbf{n}$. Its [[Def - The Frequency Four-Vector|frequency four-vector]] is $K^\mu = \omega(1,\mathbf{n})$; $\hbar$ is the reduced Planck constant. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Axiom Motivation

Everything in [[Def - Four-Momentum and Rest Mass|four-momentum]] and [[Def - Four-Velocity and Four-Acceleration|four-velocity]] was built on [[Def - Proper Time|proper time]] — the four-velocity is $dX^\mu/d\tau$, the four-momentum is $mU^\mu$. For a photon this machinery seizes up completely. A photon travels at the speed of light in every frame, so its worldline is **null**: along it the [[Def - The Spacetime Interval|interval]] vanishes, $ds^2 = 0$, and proper time does not advance. There is no clock that ticks for a photon, no rest frame to boost to, no four-velocity $dX^\mu/d\tau$ (it is the indeterminate $0/0$), and no rest mass to measure in a rest frame that does not exist. The definition $P^\mu = mU^\mu$ is the meaningless product $0\cdot\infty$.

So the question is forced: **a photon plainly carries energy and momentum — it pushes on a solar sail, it recoils an atom — so it must have a four-momentum; but how is that four-momentum defined, if not as mass times four-velocity?**

The answer is to find what *survives* the degeneration. The four-velocity does not survive; proper time does not survive; but the **four-momentum**, as an object, can be kept if we define it directly rather than as $mU^\mu$. What must it look like? Two requirements pin it down.

First, the *direction* in spacetime. For a massive particle the four-momentum points along the worldline (it is $m$ times the tangent four-velocity). The photon's worldline is null, so its four-momentum must be a **null four-vector**: $P\cdot P = 0$. This is consistent with [[Thm - Mass-Energy Equivalence|the energy–momentum relation]] $E^2 = \mathbf{p}^2c^2 + m^2c^4$ — set $m = 0$ and it reads $E = |\mathbf{p}|c$, which is exactly $P\cdot P = E^2/c^2 - \mathbf{p}^2 = 0$. The photon is the limiting case of a massive particle as $m\to 0$: timelike four-momentum ($P\cdot P > 0$) becomes null ($P\cdot P = 0$). So the photon's four-momentum is null, and we may write $P^\mu = (E/c)(1,\mathbf{n})$ with $\mathbf{n}$ a unit vector — the direction of travel.

Second, the *magnitude*. The null condition fixes the four-momentum's *direction* in spacetime but not its length — a null vector can be scaled freely and stay null. For a massive particle the magnitude came from the rest mass via $P\cdot P = m^2c^2$; the photon has no rest mass, so that route is closed. The magnitude must come from somewhere else, and the "somewhere else" is **quantum mechanics**. A photon is the quantum of a light wave of angular frequency $\omega$, and the Planck relation $E = \hbar\omega$ supplies its energy. So the photon's four-momentum is $E/c$ times the null direction $(1,\mathbf{n})$, with $E = \hbar\omega$.

This is exactly the [[Def - The Frequency Four-Vector|frequency four-vector]] $K^\mu = \omega(1,\mathbf{n})$ scaled by $\hbar/c$: the photon four-momentum is $P^\mu = \hbar K^\mu$ (with appropriate $c$'s). The classical wave four-vector and the quantum particle four-momentum are the same object up to the constant $\hbar$ — which is the relativistic form of de Broglie's hypothesis.

Why insist on the null condition rather than just declaring the photon some four-vector? Because the null condition is what makes the photon participate in [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] on the same footing as massive particles, and it is what kills terms when four-momenta are squared. The whole point of the definition is to let a photon into a collision calculation; the null condition $P\cdot P = 0$ is the price of admission and, simultaneously, the computational gift.

---

# The Definition

A **photon** is a massless particle: a quantum of light, with rest mass $m = 0$, travelling at the speed of light $c$ in every inertial frame, along a **null worldline**. Proper time does not advance along its worldline, so a photon has no [[Def - Four-Velocity and Four-Acceleration|four-velocity]] and no rest frame.

**Four-momentum of a photon.** A photon of energy $E$, travelling in the unit spatial direction $\mathbf{n}$, has **four-momentum**
$$P^\mu \;=\; \Big(\frac{E}{c},\ \mathbf{p}\Big), \qquad \mathbf{p} = \frac{E}{c}\,\mathbf{n},$$
that is, $P^\mu = \dfrac{E}{c}\,(1,\ \mathbf{n})$. It is a **null** (lightlike) four-vector:
$$P\cdot P \;=\; \eta_{\mu\nu}P^\mu P^\nu \;=\; \frac{E^2}{c^2} - \mathbf{p}^2 \;=\; 0,$$
equivalently the photon's energy–momentum relation is
$$E \;=\; |\mathbf{p}|\,c.$$
This is the $m = 0$ case of the [[Thm - Mass-Energy Equivalence|massive energy–momentum relation]] $E^2 = \mathbf{p}^2c^2 + m^2c^4$.

**Magnitude from quantum mechanics.** The null condition fixes the four-momentum's direction in spacetime but not its scale. The scale is supplied by the **Planck relation**: a photon associated with a light wave of angular frequency $\omega$ has energy
$$E \;=\; \hbar\,\omega, \qquad |\mathbf{p}| = \frac{\hbar\omega}{c}.$$
Hence the photon four-momentum is $\hbar$ times the [[Def - The Frequency Four-Vector|frequency four-vector]] $K^\mu = (\omega/c)(1,\mathbf{n})$:
$$P^\mu \;=\; \hbar\,K^\mu.$$
This is the relativistic form of the **de Broglie relation**.

**Behaviour under transformations.** Being a four-vector, $P^\mu \to \Lambda^\mu{}_\nu P^\nu$ under a [[Def - The Lorentz Transformation|Lorentz transformation]]. The photon enters [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] $\sum P_{\text{in}}^\mu = \sum P_{\text{out}}^\mu$ exactly as a massive particle does — the only difference being its null mass shell, $P\cdot P = 0$.

---

# Relate to Other Fields / Compression

The photon four-momentum is the **null** member of the family of four-momenta, sitting on the boundary between the timelike four-momenta of massive particles ($P\cdot P > 0$) and the spacelike four-momenta of hypothetical [[Def - Classification of Four-Vectors|tachyons]] ($P\cdot P < 0$). In the geometry of [[Def - Minkowski Space and the Metric|Minkowski space]], four-momenta of a fixed mass $m$ live on a hyperboloid $P\cdot P = m^2c^2$; as $m\to 0$ the hyperboloid degenerates onto the **light cone** $P\cdot P = 0$, and the photon four-momentum lies on that cone. The classification of particles by mass is the classification of which mass-shell surface their four-momentum inhabits, and the photon's is the cone itself.

Through $P^\mu = \hbar K^\mu$ the definition is the relativistic **de Broglie relation**. Its time component $E = \hbar\omega$ is Planck's quantum hypothesis; its spatial part $\mathbf{p} = \hbar\mathbf{k}$ is de Broglie's matter-wave relation. The whole relation is a four-vector equation, hence Lorentz-covariant — which is the structural reason it could be stated cleanly only after relativity, and why it unifies Planck's and de Broglie's separate insights. In quantum field theory the photon is the quantum of the electromagnetic field, and its null four-momentum reflects that the electromagnetic field is **massless**; the masslessness is, in turn, protected by gauge invariance. The statement "$P\cdot P = 0$ for a photon" is the kinematic shadow of "the photon is the massless gauge boson of electromagnetism".

---

# Examples / Corollaries

**Is an instance — a photon travelling along the $x$-axis.** A photon of energy $E$ moving in $+x$ has $P^\mu = (E/c)(1,1,0,0)$. Check: $P\cdot P = (E/c)^2 - (E/c)^2 = 0$, null. Its frequency is $\omega = E/\hbar$.

**Is an instance — the limit of a fast massive particle.** A particle of rest mass $m$ and energy $E\gg mc^2$ has $|\mathbf{p}|c = \sqrt{E^2 - m^2c^4}\approx E(1 - m^2c^4/2E^2)$, so $E\approx|\mathbf{p}|c$ and $P\cdot P = m^2c^2 \approx 0$: an ultra-relativistic massive particle is nearly a photon. The photon is the exact $m\to 0$ endpoint of this family.

**Is NOT an instance — a photon "four-velocity".** There is no four-velocity for a photon: $U^\mu = dX^\mu/d\tau$ is meaningless because [[Def - Proper Time|proper time]] is constant ($d\tau = 0$) along a null worldline. Any attempt to write $P^\mu = mU^\mu$ for a photon is the indeterminate $0\cdot\infty$. The photon four-momentum must be defined directly, as above.

**Is NOT an instance — a massive particle's four-momentum.** A massive particle has $P\cdot P = m^2c^2 > 0$, a *timelike* four-momentum, never null. The defining feature of the photon four-momentum is its nullity; a timelike four-momentum belongs to something with rest mass.

**Corollary — a photon cannot be brought to rest.** If a photon could be at rest in some frame it would have $\mathbf{p} = 0$, hence $E = |\mathbf{p}|c = 0$ — no photon at all. A photon has the same speed $c$ in every frame and no rest frame; "zero rest mass" is shorthand for "massless", since a genuinely massless particle can never be at rest.

**Corollary — the photon's energy is frame-dependent but its nullity is not.** Under a boost, $P^\mu\to\Lambda^\mu{}_\nu P^\nu$ changes the energy $E = cP^0$ (this is the Doppler effect) and the direction $\mathbf{n}$ (aberration), but $P\cdot P = 0$ is a Lorentz invariant — every observer agrees the photon is massless.

**Corollary — a single photon cannot decay or pair-produce in vacuum.** A lone photon has $P\cdot P = 0$; any system it could turn into would have to have the same total four-momentum, hence the same invariant mass zero — but two massive particles have positive invariant mass. So $\gamma\to e^+e^-$ is forbidden for a free photon. See [[Ex - Pair production and the photon-photon threshold]].

**Calibration check.** Verify $P\cdot P = 0$ from $P^\mu = (E/c)(1,\mathbf{n})$; verify that $E = \hbar\omega$ and $P^\mu = \hbar K^\mu$ are consistent with $K^\mu = (\omega/c)(1,\mathbf{n})$; check that setting $m=0$ in $E^2 = \mathbf{p}^2c^2 + m^2c^4$ gives $E = |\mathbf{p}|c$; and confirm that a photon has no rest frame because $\mathbf{p}=0$ would force $E=0$. If you can explain why the null condition fixes the photon four-momentum's direction but not its magnitude, and what supplies the magnitude, you have understood the definition.

---

# Unlocked by This

> [!tip] Pair Production, Compton Scattering, and the Doppler Effect *(from this topic)*
> Because the photon has a four-momentum, it enters [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] like any particle. [[Ex - Compton scattering|Compton scattering]], [[Ex - Pair production and the photon-photon threshold|pair production]], and the [[Ex - The relativistic Doppler effect|Doppler effect]] are all computed from $P_\gamma^\mu$ and its null condition.

> [!tip] The Massless Gauge Boson *(from Electromagnetism and Gauge Theory)*
> The photon is the quantum of the electromagnetic field, and its masslessness ($P\cdot P = 0$) is enforced by **gauge invariance**. In the Standard Model the other force carriers — the gluons (massless) and the $W,Z$ bosons (massive, mass from the Higgs mechanism) — are classified by exactly this distinction.

> [!tip] Photon Gases and Radiation Pressure *(from Statistical Mechanics and Cosmology)*
> A gas of photons — black-body radiation — has an [[Def - Four-Momentum and Rest Mass|energy–momentum]] content built from $P_\gamma^\mu$; its pressure is $p = \rho/3$, the equation of state of a relativistic gas, governing the early radiation-dominated universe.
