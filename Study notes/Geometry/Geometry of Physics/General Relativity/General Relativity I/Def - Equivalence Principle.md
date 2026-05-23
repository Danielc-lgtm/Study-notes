---
type: definition
subject: general-relativity
prereqs:
  - "Def - Spacetime Manifold"
  - "Def - Lorentzian Manifold"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
tags: [physics, general-relativity, foundations]
---

# Notation

A spacetime $(M, g)$ with signature $(+,-,-,-)$. A **free-falling** observer is one acted on by no non-gravitational forces (gravity is not a force in GR, so this is a precise condition). A **locally inertial frame** at an event $p \in M$ is a coordinate system in which $g_{\mu\nu}(p) = \eta_{\mu\nu}$ and $\partial_\rho g_{\mu\nu}(p) = 0$ — Minkowski metric at $p$ with all first derivatives vanishing. Such coordinates always exist (Riemann normal coordinates). The "size" of a local region in which special relativity holds approximately is controlled by the Riemann curvature: the region must be small enough that tidal effects $\sim R_{\mu\nu\rho\sigma} x^\mu x^\rho$ are negligible. Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

This is a compound page: it states three interlocking forms of the equivalence principle — the **weak equivalence principle**, the **Einstein equivalence principle**, and the **strong equivalence principle** — because they form a hierarchy of increasingly strong physical claims that together motivate the geometric framework of GR.

---

# Axiom Motivation

The desideratum is to extract, from the experimental fact "all bodies fall with the same gravitational acceleration", the theoretical principle that *forces* the replacement of Newtonian gravity by a geometric theory. The principle is the equivalence principle, and its content is that gravity is *locally indistinguishable* from acceleration — which forces gravity to be the curvature of spacetime, not a force on top of a flat background.

**The empirical fact.** Galileo observed (perhaps apocryphally from the Tower of Pisa, but certainly via inclined-plane experiments) that bodies of different masses fall with the same acceleration in a gravitational field. Newton's theory accommodates this: the gravitational force on a body of mass $m$ is $F_g = m_g g$, with $m_g$ the *gravitational* mass, and Newton's second law gives the acceleration as $a = F_g/m_i = (m_g/m_i) g$, with $m_i$ the *inertial* mass. The observation $a = g$ for every body says $m_g = m_i$ for every body — gravitational and inertial mass are equal. In Newton, this is a *coincidence*: nothing in the theory requires it.

**Einstein's reading.** This is not a coincidence; it is a hint. If $m_g = m_i$ for every body, then in a freely-falling frame all gravitational accelerations cancel: an observer in a falling lift, with the lift accelerating downward at $g$ relative to the ground, sees objects floating around them, oblivious to gravity. Conversely, an observer in a uniformly accelerating spaceship far from any mass would see falling objects (relative to themselves) with the same universal acceleration — feel an apparent "gravitational" pull. The two situations — uniform gravity and uniform acceleration — are *locally indistinguishable* by any experiment. There is no operational way to tell whether you are at rest in a gravitational field or accelerating in flat space.

**The forced conclusion.** Gravity must be of a kind that can be made to vanish locally by choosing a freely-falling frame. The only way this can happen is if gravity is *not a force* at all but a feature of the geometry of spacetime: the freely-falling frame is the inertial frame, and the geometry has the property that nearby freely-falling frames disagree (because spacetime is curved). This is the entire content of "gravity is the curvature of spacetime" — gravity is what you cannot remove by a change of coordinates globally, but you *can* remove locally at any one event.

**The three hierarchical forms.**

The **weak equivalence principle (WEP)** is the original Galilean statement, sharpened: the trajectory of a freely-falling test body (small enough not to disturb the gravitational field) depends only on its initial position and velocity, not on its mass, charge, internal composition, or any other property. This is what experiments measure: Eötvös (1908) compared the falling rates of different materials, modern lunar laser ranging, the MICROSCOPE satellite — all confirm the WEP to one part in $10^{15}$.

The **Einstein equivalence principle (EEP)** strengthens this to: locally, in a freely-falling frame, the laws of *all of non-gravitational physics* are exactly those of special relativity. So not just gravitational falling but the structure of Maxwell's equations, atomic spectra, particle interactions — all are special-relativistic in any freely-falling frame. This is what forces the spacetime to be a Lorentzian manifold (so that each tangent space is Minkowski) and the law of motion to be the geodesic equation (so that the freely-falling worldlines are geodesics, the straight lines of the geometry).

The **strong equivalence principle (SEP)** further requires this for *gravitational physics itself*: the gravitational dynamics in a freely-falling frame are also special-relativistic, with gravitational self-energy contributing to inertial mass with the same proportionality as other forms of energy. This is the most restrictive form and is what GR exactly satisfies. Some alternative theories (e.g., **scalar-tensor theories** like Brans–Dicke) satisfy EEP but violate SEP, distinguishing themselves observationally via **lunar laser ranging** tests of the Earth–Moon falling rate toward the Sun (the **Nordtvedt effect** — predicted in SEP-violating theories, not observed at the $\sim 10^{-13}$ level).

**Per-form failure analysis:**

(a) *If WEP fails*: different materials fall at different rates in gravity. This would distinguish a gravitational field from acceleration immediately (the falling lift would not be a "free-fall frame" for all bodies). Galileo's observation rules this out at the macroscopic level; precision tests rule it out for all known matter to extraordinary accuracy. Any theory predicting WEP violation must explain why the violation is so small.

(b) *If EEP fails*: even with WEP holding (mechanical free fall is universal), non-gravitational physics might differ in different freely-falling frames. For instance, atomic spectra might depend on position in a gravitational field (other than the gravitational redshift, which is a kinematic effect). Such violations would constitute "fifth forces" or position-dependent coupling constants — actively searched for and not detected.

(c) *If SEP fails (Nordtvedt effect)*: the Earth, with a small fraction of its mass in gravitational binding energy, would fall toward the Sun at a slightly different rate than the Moon, which has even smaller gravitational binding energy. This would produce a tiny perturbation of the lunar orbit — not observed, ruling out SEP violations at the $\sim 10^{-13}$ level (one of the strongest constraints on alternative gravity theories).

**Sources and targets of the principle.** The principle's *source* is a strong empirical fact (universal free fall). Its *target* is a structural constraint on any acceptable theory of gravity: the theory must be one in which the geodesics of spacetime are universal (independent of composition), the laws of physics are locally special-relativistic, and (in the strong form) gravity itself couples in a universal way. This single principle, properly elaborated, *implies* that spacetime is a Lorentzian manifold with the geodesic equation as the law of motion — the geometric framework of GR.

---

# The Definition

> **Definition (Equivalence principle, three forms).**
>
> **Weak equivalence principle (WEP):** The trajectory of a freely-falling test body in a gravitational field depends only on its initial position and velocity, not on its mass, composition, internal structure, or charge. Equivalently: gravitational mass equals inertial mass for all bodies, $m_g = m_i$.
>
> **Einstein equivalence principle (EEP):** WEP plus *local Lorentz invariance* (the outcome of any non-gravitational experiment is independent of the velocity of the freely-falling reference frame) plus *local position invariance* (the outcome of any non-gravitational experiment is independent of where and when in spacetime it is performed). Equivalently: locally, in a freely-falling frame, the laws of non-gravitational physics are exactly those of special relativity.
>
> **Strong equivalence principle (SEP):** EEP holds for *all* of physics, including gravitational physics — in particular, the outcome of any *local* experiment, including local gravitational experiments, depends only on the freely-falling frame and is identical to its special-relativistic counterpart. Equivalently: gravity universally couples to itself with the same proportionality with which it couples to non-gravitational energy.

The mathematical content of the EEP is the statement: at every event $p \in M$, there exist coordinates in which $g_{\mu\nu}(p) = \eta_{\mu\nu}$ and $\partial_\rho g_{\mu\nu}(p) = 0$ — **Riemann normal coordinates**. In these coordinates, the Christoffel symbols vanish at $p$, the geodesic equation reduces to $\ddot x^\mu = 0$ (free particles move in straight lines), and the law of motion is exactly that of special relativity *at $p$*. The first non-vanishing correction is at second order, encoded in the Riemann tensor:
$$g_{\mu\nu}(x) = \eta_{\mu\nu} - \frac{1}{3} R_{\mu\rho\nu\sigma}(p)\, x^\rho x^\sigma + O(x^3).$$
The Riemann tensor cannot be made to vanish at $p$ by any choice of coordinates — it is the genuine, invariant measure of the gravitational field strength (the **tidal field**), and it is what cannot be "transformed away" by an equivalence-principle argument.

The mathematical content of the SEP is that the *only* way matter and gravity can couple in a manner consistent with the principle is via the **minimal coupling prescription**: replace the Minkowski metric $\eta_{\mu\nu}$ in any matter Lagrangian by the spacetime metric $g_{\mu\nu}$, and replace partial derivatives $\partial_\mu$ by covariant derivatives $\nabla_\mu$. Any additional couplings (e.g., a direct coupling of matter to the Riemann tensor) would violate the SEP at some level.

---

# Relate to Other Fields / Compression

**True name:** The equivalence principle is *the assertion that the worldlines of freely-falling test bodies form a universal congruence — the timelike geodesics of a Lorentzian metric — that depends only on the spacetime geometry and not on the body's composition*. This is its operational form: gravity is the geometry that all freely-falling bodies trace out, the same for everyone, and the metric is the encoding of this universal pattern.

The equivalence principle is, mathematically, the demand that the connection used in the law of motion be the **Levi-Civita connection** of the metric (the unique metric-compatible, torsion-free connection). If the connection were not Levi-Civita, different bodies could couple to different connections and fall differently. The principle is what selects the Levi-Civita connection from the larger set of possible affine connections.

In categorical terms, the equivalence principle is a **naturality condition**: physics in a freely-falling frame depends only on the geometry, not on the choice of frame, so the laws transform covariantly under change of frame. This is the foundation of **general covariance** — the freedom to use any coordinates — and is what gives the Einstein equations their diffeomorphism-invariant form.

In **gauge theory** terms, gravity (the spin connection) is a *gauge field* of the local Lorentz group, and the equivalence principle is the statement that this gauge symmetry is exact — every observer at every event has their own copy of the Lorentz group acting on their tangent space, and physics is invariant under independent choices at each event. The gauge field encoding the relative rotations of these local Lorentz frames is the Riemannian (Levi-Civita) connection.

---

# Examples / Corollaries

**Is an instance — Einstein's thought experiment of the falling lift.** An observer inside a closed lift in free fall (cable cut) feels no gravity: a ball released from their hand floats next to them, a beam of light travels in a straight line, all of physics looks like special relativity. From outside, the lift and its contents are all falling at $9.8\,\mathrm{m/s}^2$ (in Earth's field), but inside the relative motion is null. This is exactly the EEP: locally, in the freely-falling frame, gravity has been transformed away.

**Is an instance — astronauts in orbit feel weightless.** An astronaut on the International Space Station is in free fall around the Earth (orbit is free fall that keeps missing the ground). They feel no gravity, despite the Earth's gravitational field being almost as strong at orbit altitude as at the surface. The freely-falling frame of the ISS is locally a special-relativistic frame.

**Is an instance — bending of light.** Apply EEP to a freely-falling observer in a gravitational field. In their frame, light travels in straight lines (special relativity). From the ground-fixed frame, the freely-falling observer is accelerating downward, and so they see a horizontally-emitted light ray as appearing to fall along with them — i.e., light bends in a gravitational field. The quantitative prediction requires GR (the factor of 2 over the naive answer), but the qualitative prediction — light bends in gravity — follows directly from EEP.

**Is an instance — gravitational redshift.** Apply EEP to a photon climbing a tower. In the freely-falling frame around the photon's emission point, the photon has frequency $\nu_e$. In the ground-fixed frame, this photon climbs against gravity and (by energy conservation, $h\nu$ vs. $mgh$ effective mass) loses energy, hence frequency. The receiver at the top measures a lower frequency $\nu_r = \nu_e(1 + gh/c^2)$ — the gravitational redshift. Confirmed by Pound–Rebka (1959).

**Is NOT a consequence of EEP — gravitational self-energy.** The gravitational binding energy of a body contributes to its mass via $E = mc^2$. Whether this gravitational mass contributes to *gravitational coupling* with the same proportionality as other forms of energy is the content of SEP, not EEP. GR satisfies SEP; Brans–Dicke theory does not. The **Nordtvedt effect** is the experimental test.

**Is NOT a violation of EEP — different falling rates of charged particles.** A charged particle in a gravitational field radiates (Larmor radiation in the freely-falling frame, modified in the ground frame); this is sometimes claimed to "fall differently" than a neutral particle. In fact, the EEP is preserved — the charged particle's trajectory in the gravitational field follows the geodesic, but it also radiates electromagnetic energy that carries off momentum, modifying the trajectory at second order. The EEP applies to test bodies neglecting radiation reaction, exactly as Galileo's law neglects air resistance.

**Is NOT a violation of EEP — tidal forces.** In a freely-falling frame, gravity vanishes *to first order* but not to second order: nearby test bodies separated by distance $\ell$ experience a relative acceleration $\sim R_{\mu\nu\rho\sigma} u^\mu u^\rho \ell^\nu \ell^\sigma$, the tidal force, which is the genuine gravitational field strength. This does *not* violate the EEP: the EEP is a *local* statement (at a single event), and tidal forces are the manifestation that the locality has a finite extent — encoded in the Riemann tensor, which obstructs making first-order accelerations vanish over an extended region.

**Corollary — the law of motion is the geodesic equation.** If freely-falling worldlines are universal (depend only on geometry), they are *the* preferred curves of the geometry — and the unique preferred curves of a Lorentzian manifold are the geodesics of the Levi-Civita connection. So EEP implies the geodesic hypothesis for free particles.

**Corollary — spacetime is Lorentzian.** If at every event there is a frame in which the laws of physics are those of special relativity (with Minkowski metric $\eta$), then the local model at every event is Minkowski space — which means the spacetime is a 4-dimensional Lorentzian manifold.

**Corollary — minimal coupling for matter.** The SEP, when applied to constructing matter Lagrangians on a curved spacetime, forces the "minimal coupling prescription": $\eta \to g$ and $\partial \to \nabla$. Non-minimal couplings (like a coupling of the matter to the Ricci scalar) violate SEP unless the coupling is gauge-equivalent to a redefinition of fields.

**Calibration check.** (i) Argue from the EEP why a vertical pencil dropped inside a freely-falling lift floats horizontally next to a coin also dropped inside, regardless of their masses. (ii) Estimate the size of a "local" region in which EEP-based reasoning is valid near the surface of the Earth, given that the tidal acceleration over a distance $\ell$ is $\sim (GM/r^3)\ell = (10^{-7}\, \mathrm{s}^{-2})\ell$; how small must $\ell$ be for the tidal acceleration to be below $10^{-12} g$? (iii) The Pound–Rebka experiment measured the redshift of a $\gamma$-ray over $h = 22.5\,\mathrm{m}$; predict $\Delta\nu/\nu = gh/c^2 \approx 2.5 \times 10^{-15}$ — the result confirmed at $\sim 1\%$.

---

# Unlocked by This

> [!tip] Geodesic Equation as the Law of Motion *(from General Relativity)*
> The EEP forces freely-falling worldlines to be the geodesics of the spacetime metric: $\ddot x^\mu + \Gamma^\mu{}_{\nu\rho} \dot x^\nu \dot x^\rho = 0$. Massive particles follow timelike geodesics (with $g(\dot x, \dot x) = 1$ for proper-time parametrisation); light follows null geodesics ($g(\dot x, \dot x) = 0$). This is the GR replacement for Newton's $\ddot x = -\nabla \phi$, and it is the operational content of "gravity is geometry".

> [!tip] Frame-Dragging and the Lense–Thirring Effect *(from Rotating Spacetimes)*
> A consequence of GR going beyond the strict EEP is **frame-dragging** by rotating bodies: a rotating mass (Earth, sun, black hole) drags inertial frames around with it. The Lense–Thirring effect predicts a precession of orbits or gyroscopes around a rotating body, beyond what would be expected from the body's mass alone. Gravity Probe B (2011) measured this precession around the rotating Earth at $37$ milliarcseconds per year, confirming GR's prediction.

> [!tip] Tests of EEP via Atom Interferometry *(from Precision Tests of Gravity)*
> Modern atom interferometers compare the gravitational acceleration of different atomic species ($^{85}$Rb vs. $^{87}$Rb, $^{40}$K vs. $^{87}$Rb, etc.) to constrain composition-dependent violations of the EEP. The MICROSCOPE satellite (2017) achieved a precision of $\sim 10^{-15}$ on the Eötvös parameter. Future space missions (STE-QUEST) aim for $10^{-17}$ — directly probing **fifth-force** scenarios and modified gravity theories at unprecedented precision.

> [!tip] Strong Equivalence Principle and the Nordtvedt Effect *(from Lunar Laser Ranging)*
> The SEP predicts that the Earth and Moon fall toward the Sun at *exactly* the same rate, despite their different gravitational self-energies. **Lunar laser ranging** measures the lunar orbit to millimeter precision and constrains any differential acceleration to $\sim 10^{-13}$, ruling out a wide class of SEP-violating alternative gravity theories (including most scalar-tensor extensions of Brans–Dicke type).

> [!tip] Equivalence Principle in Quantum Mechanics *(from Quantum Gravity)*
> The EEP applied to quantum mechanics has subtleties: a quantum particle in a gravitational field experiences gravity via the metric coupling in the Klein–Gordon or Dirac equation. The **COW experiment** (Colella–Overhauser–Werner, 1975) used neutron interferometry to detect a quantum phase shift induced by Earth's gravity — confirming that gravity couples to the *energy* (including kinetic) of the neutron, as the EEP requires. The full quantum equivalence principle (whether all matter has "equivalence-principle-respecting" couplings to gravity at the quantum level) is an active research area, motivated by potential **violations from Planck-scale physics** in string theory and quantum gravity.
