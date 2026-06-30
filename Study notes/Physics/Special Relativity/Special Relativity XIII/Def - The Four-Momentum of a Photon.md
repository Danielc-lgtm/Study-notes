---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Photons and Null Geodesics"
  - "Def - Classification of Four-Vectors"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \operatorname{diag}(+1,-1,-1,-1)$, so a null vector has $X\cdot X = 0$. A photon travels on a [[Def - Photons and Null Geodesics|null worldline]] at speed $c$ in every frame. Its four-momentum is $P$ with components $P^\mu = (E,\mathbf{p})$ relative to an [[Def - Observer and Local Rest Space|observer]] of four-velocity $U_0$; $\mathbf{n}$ is the photon's unit propagation direction in that observer's [[Def - Observer and Local Rest Space|local rest space]]. The angular frequency is $\omega$, the wave vector $\mathbf{k}$ (with $|\mathbf{k}| = \omega$ for light), the wave four-vector $K^\mu = (\omega, \mathbf{k}) = \omega(1,\mathbf{n})$, and $\hbar$ the reduced Planck constant ($h = 2\pi\hbar$). Full registry on [[Special Relativity XIII — Energy and Momentum]].

> [!warning] Convention
> In Gourgoulhon (mostly-plus) the photon four-momentum vector is $\vec p = (E/c)(\vec u_0 + \vec n)$ with $\vec p\cdot\vec p = 0$ and $E = \|\vec P\|_g\,c$. Translating to our mostly-minus signature and $c = 1$: $P = E(U_0 + \mathbf{n})$, $P\cdot P = 0$, and $E = |\mathbf{p}|$. The null condition $P\cdot P = 0$ is the same in both signatures (zero is signature-blind), but the *sign of the spatial-norm term* differs, so transcribe component expressions carefully.

---

# Axiom Motivation

The four-momentum of a massive particle was built as $P = mU$, the rest mass times the [[Def - Four-Velocity and Four-Acceleration|four-velocity]]. For a photon this construction collapses at every step, and the repair is the content of this page. A photon has *no rest mass*, $m = 0$, so $mU$ would be the zero vector — useless. Worse, a photon has *no four-velocity at all*: it travels on a null worldline along which [[Def - Proper Time|proper time]] does not advance ($ds^2 = 0$), so the proper-time derivative $dX/d\tau$ that defines the four-velocity is undefined ($d\tau = 0$, division by zero). The entire proper-time machinery that produced $U$ and then $P$ is inapplicable to light. Yet a photon manifestly carries energy and momentum — it pushes solar sails, it recoils atoms, it scatters electrons — so it must have *something* playing the role of four-momentum.

The way out is to ask which features of the four-momentum survive the limit $m\to 0$, and build the photon's four-momentum from those. The four-velocity does *not* survive (it requires a rest frame, which a photon lacks). But the *four-momentum itself* does survive: a massive particle has $P\cdot P = m^2 > 0$ (timelike), and as $m\to 0$ the four-momentum approaches the light cone, $P\cdot P \to 0$ (null), while remaining a perfectly good nonzero future-directed four-vector. So the photon's four-momentum is defined to be a **null** future-directed four-vector, $P\cdot P = 0$ — the $m\to 0$ boundary of the mass-shell hyperboloid. This is the single design decision: *keep the four-momentum, drop the four-velocity, and put the four-momentum on the light cone.*

This raises two questions a good definition must answer. First, what *direction* does $P$ point? It must be tangent to the photon's null worldline (a four-momentum is always tangent to the worldline, future-directed). Relative to an observer $U_0$, the photon moves at speed $c$ in some spatial direction $\mathbf{n}$, and the future-directed null vector along that direction is $U_0 + \mathbf{n}$ (one checks $(U_0+\mathbf{n})\cdot(U_0+\mathbf{n}) = 1 - 1 = 0$, null, using $U_0\cdot U_0 = 1$, $\mathbf{n}\cdot\mathbf{n} = -1$, $U_0\cdot\mathbf{n} = 0$). So $P$ is proportional to $U_0 + \mathbf{n}$. Second, what *magnitude* does $P$ have? Here the construction from a four-velocity gave the scale (it was $m$); for the photon that source is gone. The null condition fixes the *direction* of $P$ but leaves its overall scale free — a photon can be arbitrarily energetic or arbitrarily soft. The magnitude is therefore *not* determined by relativity at all; it is supplied externally by **quantum mechanics**, through the Planck–Einstein relation $E = \hbar\omega$. This is why the photon four-momentum sits at the boundary between classical relativity (which fixes its null direction) and quantum theory (which fixes its scale).

The proportionality constant is read off by matching to the general observer-decomposition. For any particle, the four-momentum relative to an observer decomposes as $P = E\,U_0 + \mathbf{p}$ with $E$ the energy and $\mathbf{p}$ the spatial momentum orthogonal to $U_0$. For the photon $P = \alpha(U_0 + \mathbf{n})$, comparison gives $\alpha = E$ (the coefficient of $U_0$) and spatial momentum $\mathbf{p} = E\,\mathbf{n}$, so $|\mathbf{p}| = E$. The null condition is then exactly the massless mass-shell: $P\cdot P = E^2 - |\mathbf{p}|^2 = E^2 - E^2 = 0$, consistent. Thus a photon has $E = |\mathbf{p}|$ — energy equals momentum magnitude — which is the $m = 0$ case of $E^2 = \mathbf{p}^2 + m^2$.

What *must not* be done is to assign a photon a four-velocity or a rest frame "by continuity". There is no frame in which a photon is at rest: in every inertial frame it moves at $c$ (this is the constancy of light, now seen as the statement that the photon is massless). One can always find an observer for whom a given photon's frequency is arbitrarily small or large — but never zero — so the frequency, and hence the energy, is frame-dependent, while the *null character* $P\cdot P = 0$ is absolute. The intrinsic, frame-independent content of a photon is its null four-momentum direction; its energy is a property of the photon-plus-observer.

---

# The Definition

A **photon** (or any massless particle) is a particle travelling on a future-directed [[Def - Photons and Null Geodesics|null geodesic]] at speed $c$ in every inertial frame, with zero rest mass. Its dynamics is carried by a **four-momentum** $P$ that is a future-directed **null** four-vector:
$$
P\cdot P \;=\; 0
\qquad\Longleftrightarrow\qquad
E \;=\; |\mathbf{p}|
\qquad\big(\text{with } c:\ E = |\mathbf{p}|\,c\big),
$$
the $m = 0$ case of the mass-shell relation $E^2 = \mathbf{p}^2 + m^2$. Relative to an [[Def - Observer and Local Rest Space|observer]] of four-velocity $U_0$, with the photon propagating in the unit spatial direction $\mathbf{n}$ of the observer's [[Def - Observer and Local Rest Space|local rest space]] ($\mathbf{n}\cdot U_0 = 0$, $\mathbf{n}\cdot\mathbf{n} = -1$), the four-momentum is
$$
P \;=\; E\,(U_0 + \mathbf{n}),
\qquad\text{equivalently}\qquad
P^\mu = (E,\ E\,\mathbf{n}) = (E,\ \mathbf{p}),\ \ \mathbf{p} = E\,\mathbf{n}.
$$

The **magnitude** of the four-momentum — the photon's energy relative to the observer — is supplied by quantum mechanics through the **Planck–Einstein relation**
$$
E \;=\; \hbar\omega \;=\; \frac{2\pi\hbar c}{\lambda},
$$
where $\omega$ is the angular frequency and $\lambda = 2\pi c/\omega$ the wavelength measured by the observer. Combining, the four-momentum is $\hbar$ times the **wave four-vector** $K^\mu = \omega(1,\mathbf{n})$:
$$
P^\mu \;=\; \hbar\,K^\mu,
\qquad
\mathbf{p} = \hbar\mathbf{k},\ \ |\mathbf{k}| = \omega,\ \ \mathbf{p} = \frac{2\pi\hbar}{\lambda}\,\mathbf{n}.
$$
The energy, momentum, frequency, and wavelength are all **relative to the observer**; the intrinsic, frame-independent datum of the photon is the null direction of $P$.

---

# Categorical / Structural Definition

Structurally, the massless four-momentum lives on the *boundary* of the family of mass shells. The mass shells $\{P : P\cdot P = m^2,\ P^0 > 0\}$ for $m > 0$ are a one-parameter family of nested timelike hyperboloids inside the future light cone; their limit as $m\to 0^+$ is the future light cone itself, $\{P : P\cdot P = 0,\ P^0 > 0\}$, which is the massless mass shell. A photon four-momentum is a point on this cone (minus the apex).

In the Wigner classification this boundary status has a sharp group-theoretic counterpart. A massive particle's four-momentum can be boosted to its rest frame $(m,\mathbf{0})$, whose stabiliser in the Lorentz group (the **little group**) is the rotation group $SO(3)$, giving the $(2s+1)$-fold spin multiplet. A massless particle's four-momentum can never be brought to rest; the best one can do is a standard null momentum such as $E(1,0,0,1)$, whose little group is $ISO(2)$, the Euclidean group of the plane — and the topology of $ISO(2)$ forces the spin to collapse to a single **helicity** (the photon has just two states, left- and right-circular polarisation, rather than three). The discontinuity in the little group at $m = 0$ is the representation-theoretic shadow of the fact that the photon has no rest frame, and it is why a massless spin-1 particle has two polarisations, not three.

---

# Relate to Other Fields / Compression

In **classical electromagnetism** the photon four-momentum is the particle face of the plane electromagnetic wave: the wave four-vector $K^\mu = (\omega, \mathbf{k})$ that appears in the phase $e^{-iK\cdot X}$ of a light wave is, up to the factor $\hbar$, the photon's four-momentum. The null condition $K\cdot K = 0$ is the wave's dispersion relation $\omega = |\mathbf{k}|$ (light travels at $c$), and the relativistic Doppler effect and aberration are the transformation of $K^\mu$ between observers.

In **quantum mechanics** the relation $P = \hbar K$ is the photon's case of de Broglie's hypothesis $P^\mu = \hbar K^\mu$, which for massive particles relates momentum to the wavelength of the matter wave. The Planck–Einstein $E = \hbar\omega$ is the quantum of the relation; it is the equation that, applied to the photoelectric effect, won Einstein the Nobel Prize and established the corpuscular nature of light.

**True name:** the operational characterisation of a massless particle, distinct from "a particle of zero rest mass", is **a particle whose four-momentum is null**, $P\cdot P = 0$. This is what you compute with: in any conservation-of-four-momentum problem, the photon contributes a four-vector whose self-square *vanishes*, so squaring an expression containing it simply drops that term — making the photon, despite having no rest frame, the *easiest* particle to handle algebraically.

---

# Examples / Corollaries

**Is an instance — a visible-light photon.** A photon of wavelength $\lambda = 500$ nm has energy $E = 2\pi\hbar c/\lambda \approx 2.5$ eV and four-momentum $P = E(U_0 + \mathbf{n})$ relative to a laboratory observer, with $|\mathbf{p}| = E$. Its Minkowski square is $E^2 - E^2 = 0$: null, as required.

**Is an instance — the cosmic microwave background.** A CMB photon at the peak of the $2.725$ K blackbody has energy $E \approx 1.2\times10^{-3}$ eV and a null four-momentum; the smallness of $E$ relative to particle masses is exactly why such photons can only be made to pair-produce or photoproduce pions by colliding with ultra-relativistic particles (the inverse Compton effect and the GZK cutoff, [[Ex - Inverse Compton scattering and the GZK cutoff]]).

**Is NOT an instance — a massive particle's four-momentum.** An electron's four-momentum has $P\cdot P = m_e^2 > 0$ (timelike), not null; it lies *inside* the future light cone, not on it. An electron has a rest frame in which $P = (m_e, \mathbf{0})$, whereas no boost brings a photon's four-momentum to the form $(E, \mathbf{0})$ — a photon at rest would have $E = 0$, i.e. no photon at all.

**Is NOT an instance — a spacelike four-vector.** A four-vector with $P\cdot P < 0$ is spacelike and would describe a tachyon; it is neither a massive particle (timelike) nor a photon (null). Photons sit exactly on the null cone separating the timelike (massive) and spacelike (forbidden) regions.

**Corollary — a photon's frequency is observer-dependent but never zero.** Since $E = \hbar\omega = P\cdot U_0$ depends on the observer's four-velocity, two observers measure different frequencies for the same photon (the Doppler effect). One can make $\omega$ arbitrarily small (observer chasing the photon) or arbitrarily large (observer approaching it), but never zero, because $P$ is a fixed nonzero null vector and $P\cdot U_0 > 0$ for any future-directed timelike $U_0$.

**Corollary — for a photon, energy and momentum magnitude coincide.** $E = |\mathbf{p}|$ exactly (with $c$: $E = |\mathbf{p}|c$), the $m=0$ limit of $E^2 = \mathbf{p}^2 + m^2$. This is what lets photon energies and momenta be used interchangeably in conservation calculations, and it is the radiation-pressure relation: a beam of energy $E$ carries momentum $E/c$.

**Calibration check.** If you have understood the definition you should be able to: (1) verify directly that $U_0 + \mathbf{n}$ is null, using the rest-space orthonormality $U_0\cdot U_0 = 1$, $\mathbf{n}\cdot\mathbf{n} = -1$, $U_0\cdot\mathbf{n} = 0$; (2) explain why a photon has no four-velocity but does have a four-momentum, in one sentence — proper time does not advance along a null worldline, so $dX/d\tau$ is undefined, but $P$ need not be built from $d/d\tau$; (3) state what supplies the *magnitude* of the photon four-momentum and why relativity alone cannot — quantum mechanics, via $E = \hbar\omega$, because the null condition fixes only the direction.

---

# Unlocked by This

> [!tip] The Relativistic Doppler Effect and Compton Scattering *(from §13.2)*
> Because the photon energy is $E = P\cdot U_0 = \hbar\,U_0\cdot K$, every question about the *colour* of light reduces to contracting the photon four-momentum with an observer's four-velocity or transforming it between frames: the relativistic **Doppler effect** is this for two observers, and the **Compton effect** ([[Thm - Elastic Collisions and the Compton Effect]]) is this for a photon scattering off an electron. The null self-square $P\cdot P = 0$ makes the photon drop out cleanly when conservation equations are squared.

> [!tip] Photons in Conservation Laws — Pair Production and the Photon Rocket *(from §13.2)*
> A photon enters [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] on equal footing with massive particles, which makes pair production ($\gamma\gamma\to e^+e^-$), the impossibility of single-photon decay ([[Ex - Whether a particle reaction is kinematically allowed]]), and the [[Ex - The relativistic rocket|photon rocket]] all computable. The key recurring fact is that the *null* self-square $P\cdot P = 0$ vanishes on squaring, so a photon's four-momentum is the easiest to eliminate.

> [!tip] Massless Fields and Gauge Symmetry *(from Quantum Field Theory)*
> The photon is the quantum of the electromagnetic field, a massless spin-1 (vector) field. Its masslessness is not accidental: it is *protected* by **gauge symmetry**, the redundancy $A^\mu \to A^\mu + \partial^\mu\lambda$ in the four-potential, which forbids a mass term $m^2 A_\mu A^\mu$ and forces $P\cdot P = 0$. The same logic, applied to non-abelian gauge groups, gives the gluons of the strong force; the W and Z bosons acquire mass only through the Higgs mechanism breaking the symmetry.
