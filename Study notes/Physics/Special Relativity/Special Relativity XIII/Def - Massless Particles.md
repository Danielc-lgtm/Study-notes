---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \operatorname{diag}(+1,-1,-1,-1)$, so $X\cdot X > 0$ timelike, $X\cdot X = 0$ null, $X\cdot X < 0$ spacelike. A particle has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E,\mathbf{p})$ and rest mass $m = \sqrt{P\cdot P}$. The speed relative to a frame is $u = |\mathbf{p}|/E$ (so that $\mathbf{p} = E\mathbf{u}$ for the velocity $\mathbf{u}$). Full registry on [[Special Relativity XIII — Energy and Momentum]].

---

# Axiom Motivation

The four-momentum was built from the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] as $P = mU$, a construction valid only for *massive* particles — those with a rest frame and a proper time. This page asks the complementary question: what *is* a massless particle, intrinsically, and why is "$m = 0$" the right characterisation? The answer reorganises the whole classification of particles around the sign of $P\cdot P$.

The naive definition, "a particle with $m = 0$", is correct but unilluminating, because for a massless particle the construction $P = mU$ that *defines* $m$ has broken down — there is no four-velocity $U$, so "$m = 0$" cannot be read literally as "the coefficient of $U$ is zero". The operational definition must come from the four-momentum directly. For a massive particle $P\cdot P = m^2 > 0$ (timelike); the natural boundary, the case $m\to 0$, is $P\cdot P = 0$ (null). So a massless particle is *defined* by its four-momentum being null: $P\cdot P = 0$, the $m\to 0$ limit of the mass-shell hyperboloid, which is the light cone itself. This is the design decision — characterise particles by the sign of $P\cdot P$, with massless meaning null.

This definition makes the speed limit a theorem about masslessness. A massless particle has $P\cdot P = E^2 - |\mathbf{p}|^2 = 0$, so $E = |\mathbf{p}|$, and its speed is $u = |\mathbf{p}|/E = 1 = c$. *Every* massless particle travels at exactly the speed limit, in every frame — and conversely a particle at the speed limit must be massless (a massive particle has $E > |\mathbf{p}|$, hence $u < 1$). This recasts the postulate "the speed of light is the same in every frame" as the deeper statement "there is a universal speed limit $c$, and any massless particle travels at it". The photon is singled out among physical phenomena not because light is special but because the photon happens to be massless; gravitons, equally massless, travel at the same speed.

The classification by the sign of $P\cdot P$ also exposes what is *forbidden*. A four-momentum with $P\cdot P > 0$ (timelike) is a massive particle, $u < c$; with $P\cdot P = 0$ (null) a massless particle, $u = c$; with $P\cdot P < 0$ (spacelike) it would describe a particle of imaginary rest mass, $m^2 < 0$, travelling *faster* than light — a **tachyon**. Tachyons are excluded, and seeing why is part of understanding masslessness as a boundary. A tachyon would have $u > c$, and a superluminal signal in one frame is a backward-in-time signal in another (the time-ordering of spacelike-separated events is frame-dependent), so tachyons would permit signalling into the past and the attendant causal paradoxes. The null cone $P\cdot P = 0$ is the boundary between the allowed timelike region (massive, causal) and the forbidden spacelike region (tachyonic, acausal); massless particles live exactly on it.

One subtlety the definition must handle: a massless particle has no rest frame, so quantities like proper time and four-velocity are undefined for it, and one cannot "boost to its rest frame" to read off its mass. The mass is instead defined directly as $m = \sqrt{P\cdot P} = 0$, the null condition, and all the kinematics is rephrased in terms of the four-momentum (which the particle has) rather than the four-velocity (which it lacks). This is why the [[Def - The Four-Momentum of a Photon|photon four-momentum]] is the fundamental object for light, and why its magnitude must be supplied externally by quantum mechanics: the relativistic machinery fixes only the null *direction*, never the scale.

---

# The Definition

A **massless particle** is a particle whose [[Def - Four-Momentum and Rest Mass|four-momentum]] is a future-directed **null** four-vector:
$$
m = 0 \;\Longleftrightarrow\; P\cdot P = 0 \;\Longleftrightarrow\; E = |\mathbf{p}|
\qquad\big(\text{with } c:\ E = |\mathbf{p}|\,c\big).
$$
Equivalently, it is the $m\to 0$ boundary of the mass-shell hyperboloid $P\cdot P = m^2$ (the light cone). A massless particle travels at the universal speed limit $c$ in every inertial frame,
$$
u = \frac{|\mathbf{p}|}{E} = 1 = c,
$$
and possesses no rest frame, no proper time, and no four-velocity; its dynamics is carried entirely by the four-momentum (see [[Def - The Four-Momentum of a Photon]]). The known massless particles are the **photon** (quantum of the electromagnetic field) and the **graviton** (quantum of the gravitational field).

The mass-shell sign **classifies all particles** by the [[Def - Classification of Four-Vectors|character of the four-momentum]]:
$$
P\cdot P > 0 \ (\text{timelike}):\ \text{massive},\ u < c;
\qquad
P\cdot P = 0 \ (\text{null}):\ \text{massless},\ u = c;
\qquad
P\cdot P < 0 \ (\text{spacelike}):\ \text{tachyon},\ u > c.
$$
**Tachyons** ($m^2 < 0$, imaginary rest mass) are excluded from the physical spectrum: they would travel faster than light, and a superluminal signal in one frame is a backward-in-time signal in another, violating causality. In quantum field theory a field with $m^2 < 0$ does not produce superluminal particles but signals an **instability of the vacuum**.

---

# Categorical / Structural Definition

Structurally, the three classes of particle are the three orbit-types of the Lorentz group acting on the space of four-momenta, distinguished by the value of the first Poincaré Casimir $P\cdot P$. The timelike orbits ($P\cdot P = m^2 > 0$, future sheet) are the massive particles; the null orbit ($P\cdot P = 0$, future cone minus apex) is the massless particles; the spacelike orbits ($P\cdot P < 0$) are the tachyons. The Lorentz group acts transitively within each orbit — any two four-momenta of the same mass are related by a boost — but cannot move between orbits, which is the geometric statement that mass is a Lorentz invariant.

The boundary status of the null orbit has the sharp Wigner-classification consequence already noted for the photon: the **little group** (stabiliser of a standard momentum) jumps from $SO(3)$ on the massive orbits to $ISO(2)$ on the null orbit. The representation theory is therefore *discontinuous* at $m = 0$: a massive spin-$s$ particle has $2s+1$ states (a full spin multiplet), while a massless particle has at most two **helicity** states (for the photon, the two circular polarisations), because the non-compact translations in $ISO(2)$ must act trivially in a finite-dimensional unitary representation. This is why "the $m\to 0$ limit of a massive vector particle" is subtle: the third polarisation does not simply disappear, it decouples, and the careful treatment of this limit is a recurring theme in gauge theory.

---

# Relate to Other Fields / Compression

In **electromagnetism** the masslessness of the photon is the particle-physics statement of two classical facts: light travels at $c$ in vacuum (the null condition $\omega = |\mathbf{k}|$), and the electromagnetic field has only two propagating polarisations (transverse waves, no longitudinal mode). The masslessness is *protected* by gauge symmetry, which forbids a photon mass term.

In **quantum field theory** "massless" means the field has no mass term $m^2\phi^2$ in its Lagrangian, so its quanta have $P\cdot P = 0$ and propagate at $c$. The tachyonic case $m^2 < 0$ is not a faster-than-light particle but a sign that the field is sitting at a *maximum* of its potential — the vacuum is unstable, and the field rolls down to a true minimum, the mechanism behind spontaneous symmetry breaking and the Higgs field.

**True name:** the operational characterisation of a massless particle, distinct from "rest mass zero", is **a particle whose four-momentum is null**, $P\cdot P = 0$, equivalently **a particle that travels at the speed limit $c$ in every frame**. This is what you use: in kinematics, the null self-square makes the particle's four-momentum vanish on squaring (the easiest particle to eliminate); in classification, $u = c$ identifies masslessness without any reference to a rest mass.

---

# Examples / Corollaries

**Is an instance — the photon.** The photon has $P\cdot P = 0$, $E = |\mathbf{p}|$, travels at $c$, and has two helicity states (left- and right-circular polarisation). Its energy is supplied by $E = \hbar\omega$. See [[Def - The Four-Momentum of a Photon]].

**Is an instance — the graviton.** The (hypothetical, never individually detected) quantum of the gravitational field is massless, travels at $c$, and has two helicity states (the two polarisations of a gravitational wave, observed in 2015). Its masslessness is why gravitational waves travel at the speed of light.

**Is NOT an instance — the neutrino.** Long thought massless, neutrinos are now known to have small but nonzero rest mass (the differences between the three neutrino masses are $0.01$–$0.1$ eV, and the sum is below $\sim 0.3$ eV). They travel at *just below* $c$, with $P\cdot P = m_\nu^2 > 0$ (timelike), so they are massive particles — the discovery of neutrino oscillations established this.

**Is NOT an instance — a tachyon.** A particle with $P\cdot P < 0$ (imaginary rest mass, $u > c$) is excluded; no such particle has ever been observed, and its existence would permit backward-in-time signalling. In field theory $m^2 < 0$ signals a vacuum instability rather than a superluminal particle.

**Corollary — the speed limit is exactly $c$ for massless particles.** From $E = |\mathbf{p}|$, the speed $u = |\mathbf{p}|/E = 1 = c$, in every frame. A massless particle cannot be slowed below $c$ or sped above it; it is locked to the speed limit, which is why "the speed of light is invariant" is really "the photon is massless and so travels at the universal $c$".

**Corollary — no rest frame.** A massless particle's four-momentum $(E, \mathbf{p})$ with $E = |\mathbf{p}| > 0$ cannot be boosted to $(E', \mathbf{0})$, because that would require $E' = |\mathbf{0}| = 0$, i.e. the particle to vanish. There is no frame in which a photon is at rest; one can only redshift it towards (never to) zero energy.

**Calibration check.** If you have understood the definition you should be able to: (1) show that $P\cdot P = 0$ forces $u = c$ and conversely; (2) explain, in terms of the sign of $P\cdot P$, why massive, massless, and tachyonic particles are the three cases and which is forbidden; (3) state in one sentence why a massless particle has no rest frame — its energy in any frame is $|\mathbf{p}| > 0$, and a rest frame would require energy zero.

---

# Unlocked by This

> [!tip] Photon Kinematics in Conservation Laws *(from §13.2)*
> Because a massless particle has $P\cdot P = 0$, its four-momentum vanishes when an expression containing it is squared — making the photon the easiest particle to eliminate in [[Thm - Conservation of Four-Momentum|conservation]] calculations. This is the engine of [[Thm - Elastic Collisions and the Compton Effect|Compton scattering]], pair production, and the [[Ex - The relativistic rocket|photon rocket]].

> [!tip] Gauge Symmetry Protects Masslessness *(from Quantum Field Theory)*
> The photon's masslessness is enforced by **gauge symmetry**: the redundancy $A^\mu\to A^\mu + \partial^\mu\lambda$ in the four-potential forbids a mass term $m^2 A_\mu A^\mu$, locking $P\cdot P = 0$. The same mechanism, for non-abelian gauge groups, gives the massless gluons of the strong force; the W and Z bosons acquire mass only because the **Higgs mechanism** spontaneously breaks the symmetry — the tachyonic ($m^2 < 0$) Higgs field rolling to its true vacuum.

> [!tip] The Little Group and Helicity *(from Representation Theory)*
> The discontinuity of the **little group** at $m = 0$ — from $SO(3)$ (massive, full spin multiplet) to $ISO(2)$ (massless, two helicities) — is why a massless spin-1 particle has two polarisations, not three. This is the representation-theoretic content of masslessness in the Wigner classification, developed in [[Special Relativity XII — Inertial Observers and the Poincaré Group|Special Relativity XII]].
