---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Maxwell Equations"
  - "Def - Gauge Choice and the Lorenz Gauge"
  - "Def - The Four-Potential"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The field is the $2$-form $F$, the [[Def - The Four-Potential|four-potential]] the $1$-form $A$, the [[Def - The Electric Four-Current|four-current]] $J$. The **d'Alembertian** is $\Box := \nabla_\mu\nabla^\mu$; in inertial coordinates with $c = 1$ and signature $(+{-}{-}{-})$, $\Box = \partial_t^2 - \partial_x^2 - \partial_y^2 - \partial_z^2$. A null wave-vector $k$ satisfies $k\cdot k = 0$. Relative to an observer, $\mathbf E$ and $\mathbf B$ are the electric and magnetic fields, with $\hat{\mathbf n}$ the propagation direction. The Lorenz gauge is $\nabla\cdot A = 0$. Full registry on [[Special Relativity XXII — Maxwell's Equations]].

---

# Statement

> **Theorem (electromagnetic waves).** In a region free of charge and current ($J = 0$), the electromagnetic field obeys the **wave equation**
> $$\Box F = 0.$$
> Its solutions propagate at the speed $c$ that appears in the d'Alembertian. The general **plane-wave** solution depending on a single null direction is
> $$F(ct, x, y, z) = F_1(x - ct) + F_2(x + ct),$$
> where $F_1$ and $F_2$ are $2$-form fields constant on the null planes $x \mp ct = \text{const}$; $F_1$ propagates at $c$ in the $+x$ direction, $F_2$ in the $-x$ direction.

> **Properties of a single plane wave.** A single plane wave (say $F = F_1(x - ct)$) is **null** and **transverse**: its two invariants vanish,
> $$F_{\mu\nu}F^{\mu\nu} = 0, \qquad {\star}F_{\mu\nu}F^{\mu\nu} = 0,$$
> and relative to any observer the fields satisfy
> $$|\mathbf E| = c|\mathbf B|, \qquad \mathbf E\perp\mathbf B, \qquad \mathbf E\perp\hat{\mathbf n}, \qquad \mathbf B\perp\hat{\mathbf n},$$
> with $\mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ a right-handed orthogonal triad.

> **With a source.** In the presence of a current, the field obeys the inhomogeneous wave equation $\Box F = -\mu_0\,dJ^\sharp$ (the exterior derivative of the current as source), gauge-independently; in Lorenz gauge the potential obeys $\Box A = \mu_0 J$.

---

# Motivation

This theorem is the birth of light as a physical phenomenon within electromagnetism. Maxwell's equations were written to describe electric and magnetic fields produced by charges and currents; this theorem shows they also predict something no one put in by hand — fields that propagate through empty space, with no charges anywhere, at a definite speed $c$. Maxwell himself made the calculation in the 1860s, found that the predicted speed matched the measured speed of light, and drew the conclusion that *light is an electromagnetic wave*. It is one of the great unifications in physics: optics, which had been a separate science, became a chapter of electromagnetism.

The structural reason waves appear is the displacement current. The pre-Maxwell Ampère law $\nabla\times\mathbf B = \mu_0\mathbf J$ has no wave solutions in vacuum; it is Maxwell's added term $\tfrac{1}{c^2}\partial_t\mathbf E$ that lets a changing electric field source a magnetic field, which by Faraday's law sources an electric field, which sources a magnetic field — a self-sustaining ripple that propagates. In the covariant formulation this is automatic: combining $dF = 0$ and $d{\star}F = 0$ in vacuum forces $\Box F = 0$, and the speed $c$ is the one already sitting in the d'Alembertian. The wave is not added to electromagnetism; it is contained in it.

The properties of the wave — null, transverse, $|\mathbf E| = c|\mathbf B|$ — are exactly the experimental facts of light: it has no longitudinal component, its electric and magnetic fields are perpendicular and in phase, and it travels at $c$. That these follow from the abstract statement $\Box F = 0$ with $dF = 0$ is the theorem's payoff: the geometry of the field $2$-form encodes the polarisation structure of light. The two independent plane-wave polarisations are the two helicity states of the photon, the organising fact of quantum optics and of the photon's role in the Standard Model.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the field satisfies the source-free Maxwell equations in a region".

The first disguised source is **"a region is far from all charges"**. The radiation zone of an antenna, the space between a source and a detector, the interstellar medium — all are effectively charge-free, so the field there obeys $\Box F = 0$ and is a superposition of waves. The bridge is that $J = 0$ locally suffices, even if charges exist elsewhere. The nonobviousness is that the *same* field that is sourced near the charges propagates as a free wave far away. *Example problem:* show that the field radiated by an antenna, measured far away, is a transverse wave.

The second disguised source is **"the field is given in Lorenz gauge with a known source"**. If $\nabla\cdot A = 0$, then $\Box A = \mu_0 J$ directly; in vacuum this is $\Box A = 0$, and the field $F = dA$ inherits $\Box F = 0$ because $\Box$ commutes with $d$. The bridge is the [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] reduction. *Example problem:* solve for the field of an oscillating current by solving the wave equation for $A$ and differentiating.

The third disguised source is **"the field is built as a null, transverse $2$-form"**. Any $F = k\wedge a$ with $k$ null, $a$ orthogonal to $k$, and dependence only on $k\cdot x$ automatically satisfies $\Box F = 0$ and $dF = 0$ — it is a wave by construction. The bridge is that the wedge structure plus null dependence forces both Maxwell equations. *Example problem:* verify that a circularly polarised field, written as a complex null bivector, solves vacuum Maxwell.

**Targets (Output Amplification)**

The conclusion is "$\Box F = 0$, with plane-wave solutions $F_1(x - ct) + F_2(x + ct)$".

Combine the conclusion with **the two invariants**. A single plane wave has $F_{\mu\nu}F^{\mu\nu} = 0$ and ${\star}F_{\mu\nu}F^{\mu\nu} = 0$, so it is a **null field**. The further result is that the wave cannot be transformed to a frame where it is purely electric or purely magnetic (unlike a Coulomb field) — it looks like a wave to every observer, only Doppler-shifted. The combination is nonobvious because the vanishing of both invariants is a strong, frame-independent constraint that classifies the field. *Example:* show that no boost turns a light wave into a static field.

Combine the conclusion with **the energy flux through a sphere**. The wave carries an energy flux (Poynting vector) $\mathbf S = \varepsilon_0 c^2\mathbf E\times\mathbf B$; integrating over a large sphere gives the radiated power. The further result, when the wave is the radiative tail of an accelerating charge, is the Larmor formula. The combination is the bridge from wave structure to energy transport. *Example:* compute the power radiated by an antenna from its far-field wave.

Combine the conclusion with **superposition and Fourier analysis**. Because $\Box$ is linear, any superposition of plane waves of different frequencies and directions solves $\Box F = 0$; conversely any vacuum field is such a superposition. The further result is the full apparatus of wave optics — interference, diffraction, wave packets. The combination is the foundation of classical optics. *Example:* construct a localised pulse as a Fourier superposition of plane waves.

---

# Why Is It True

The bolded mechanism: **the two Maxwell equations, applied in vacuum, say that $F$ is both closed ($dF = 0$) and co-closed ($d{\star}F = 0$); a form that is both is harmonic, and the Laplacian on Minkowski space is the wave operator, so $\Box F = 0$.** The wave equation is the statement that the field is a harmonic $2$-form, and harmonicity in Lorentzian signature is propagation at $c$.

Take it through the potential first, which is most transparent. In Lorenz gauge the inhomogeneous Maxwell equation is $\Box A = \mu_0 J$; in vacuum, $\Box A = 0$. The field is $F = dA$, and the d'Alembertian commutes with the exterior derivative (in inertial coordinates, both are built from partial derivatives that commute), so $\Box F = \Box(dA) = d(\Box A) = d(0) = 0$. The field satisfies the wave equation because the potential does, and the potential does because Maxwell reduces to a wave equation in Lorenz gauge. The speed is the speed in the d'Alembertian, the same $c$ in $\Box = \tfrac{1}{c^2}\partial_t^2 - \nabla^2$.

Why does $\Box$ produce *propagation at $c$*, rather than some other behaviour? Because $\Box = \tfrac{1}{c^2}\partial_t^2 - \nabla^2$ factors, in one dimension, as $\tfrac{1}{c^2}(\partial_t - c\partial_x)(\partial_t + c\partial_x)$, and the operators $\partial_t \mp c\partial_x$ annihilate any function of $x \pm ct$. So the general solution is $f(x - ct) + g(x + ct)$: a profile moving rigidly to the right at speed $c$ plus one moving left at $c$. This is d'Alembert's solution, and it is why the wave moves at exactly the $c$ in the operator — the operator is *built* to annihilate functions of $x \mp ct$.

The properties of a single wave follow from $dF = 0$ plus the null dependence. Writing the wave as a function of the single null combination $\xi = x - ct$, the field is $F = F(\xi)$; the closedness $dF = 0$ forces the components to be arranged so that $F = k\wedge a$ with $k$ the null wave-vector ($k\cdot k = 0$) and $a$ the polarisation, transverse to $k$. The wedge structure $F = k\wedge a$ immediately gives ${\star}F\cdot F \propto \epsilon(k, a, k, a) = 0$ (an $\epsilon$ with two repeated arguments) — the second invariant vanishes. The first invariant $F_{\mu\nu}F^{\mu\nu} \propto (k\cdot k)(a\cdot a) - (k\cdot a)^2 = 0$ because $k\cdot k = 0$ and $k\cdot a = 0$. Both invariants vanish, so the field is null. Decomposing $F = k\wedge a$ relative to an observer, the transversality $k\cdot a = 0$ and nullity $k\cdot k = 0$ translate to $\mathbf E\perp\mathbf B\perp\hat{\mathbf n}$ and $|\mathbf E| = c|\mathbf B|$ — the polarisation structure of light, read off the geometry of the bivector.

---

# What Makes This Hard

The conceptual step people miss is that the wave equation does not need to be derived by laboriously taking the curl of Faraday and substituting Ampère (the standard three-dimensional route); it is immediate from $\Box F = 0$, which is just "$F$ is closed and co-closed in vacuum". The technical subtlety is the sign of $\Box$ in mostly-minus signature: $\Box = \partial_t^2 - \nabla^2$ here (some references, mostly-plus, write $\Box = -\partial_t^2 + \nabla^2$), and getting this sign wrong flips a wave equation into an elliptic equation with no propagating solutions. The most common error in the wave's properties is to forget that $|\mathbf E| = c|\mathbf B|$ (not $|\mathbf E| = |\mathbf B|$) when $c \ne 1$, and to mis-assign the handedness of the $(\mathbf E, \mathbf B, \hat{\mathbf n})$ triad.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Impose Lorenz gauge so $\Box A = \mu_0 J$; in vacuum $\Box A = 0$; since $\Box$ commutes with $d$, $\Box F = 0$. Factor $\Box$ to get d'Alembert's solution $F_1(x - ct) + F_2(x + ct)$. For a single wave, use $dF = 0$ and null dependence to write $F = k\wedge a$ with $k$ null and $a$ transverse, then read off the invariants and the $\mathbf E$, $\mathbf B$ structure.

**Subgoal decomposition:**

1. **Reduce to the wave equation.** From $dF = 0$ and $d{\star}F = 0$ (vacuum), or from $\Box A = 0$ in Lorenz gauge, obtain $\Box F = 0$.
   - *Hint:* $\Box$ commutes with $d$; $F = dA$ and $\Box A = 0$ give $\Box F = d(\Box A) = 0$.
   - *Why needed:* It is the central equation; everything follows from it.

2. **Solve by factoring.** Factor $\Box = \tfrac{1}{c^2}(\partial_t - c\partial_x)(\partial_t + c\partial_x)$ in the relevant direction.
   - *Hint:* $\partial_t \mp c\partial_x$ annihilates functions of $x \pm ct$; the general solution is $F_1(x - ct) + F_2(x + ct)$.
   - *Why needed:* It produces the plane-wave form and exhibits propagation at $c$.

3. **Identify the wedge structure of a single wave.** For $F = F(\xi)$, $\xi = x - ct$, use $dF = 0$ to write $F = k\wedge a$ with $k$ the null wave-vector and $a$ transverse.
   - *Hint:* Closedness constrains the components so that $F$ is the wedge of the propagation null vector with the polarisation.
   - *Why needed:* The wedge structure delivers the invariants and the transversality.

4. **Read off invariants and field structure.** Compute $F_{\mu\nu}F^{\mu\nu}$ and ${\star}F_{\mu\nu}F^{\mu\nu}$ from $F = k\wedge a$; decompose onto an observer.
   - *Hint:* $k\cdot k = 0$ and $k\cdot a = 0$ kill the first invariant; the $\epsilon$ with repeated $k, a$ kills the second; the wedge gives $\mathbf E\perp\mathbf B\perp\hat{\mathbf n}$, $|\mathbf E| = c|\mathbf B|$.
   - *Why needed:* It establishes that the wave is null and transverse — the properties of light.

---

# Lemma Decomposition

> [!note]- Lemma 1: Vacuum Maxwell forces the wave equation
> **Statement:** If $dF = 0$ and $d{\star}F = 0$, then $\Box F = 0$.
>
> **Hint:** Pass to the potential in Lorenz gauge, or use $\Box = -(d\delta + \delta d)$ on forms.
>
> **Why needed:** It is the reduction of the two first-order Maxwell equations to one second-order wave equation.
>
> > [!note]- Full proof
> > Route via the potential: since $dF = 0$, write $F = dA$; impose the [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] $\nabla\cdot A = 0$. The inhomogeneous Maxwell equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu = 0$ then reduces to $\Box A^\nu = 0$ (the term $\nabla^\nu(\nabla\cdot A)$ vanishes in Lorenz gauge). In inertial coordinates the d'Alembertian commutes with partial derivatives, so $\Box F_{\mu\nu} = \Box(\partial_\mu A_\nu - \partial_\nu A_\mu) = \partial_\mu(\Box A_\nu) - \partial_\nu(\Box A_\mu) = 0$. Hence $\Box F = 0$. (Gauge-independently: on forms, $\Box = -(d\delta + \delta d)$ where $\delta$ is the codifferential; $dF = 0$ kills $\delta d$'s... rather, $d{\star}F = 0$ means $\delta F = 0$, and $dF = 0$, so $\Box F = -(d\delta + \delta d)F = 0$.) $\blacksquare$

> [!note]- Lemma 2: d'Alembert's solution
> **Statement:** The general solution of $\Box \phi = 0$ depending on $(t, x)$ only is $\phi = f(x - ct) + g(x + ct)$.
>
> **Hint:** Factor the d'Alembertian.
>
> **Why needed:** It gives the plane-wave form and the propagation speed $c$.
>
> > [!note]- Full proof
> > In $(t, x)$, $\Box = \tfrac{1}{c^2}\partial_t^2 - \partial_x^2 = \tfrac{1}{c^2}(\partial_t - c\partial_x)(\partial_t + c\partial_x)$. Introduce null coordinates $\xi = x - ct$, $\eta = x + ct$; then $\partial_t = c(\partial_\eta - \partial_\xi)$, $\partial_x = \partial_\xi + \partial_\eta$, and $\Box = -4\partial_\xi\partial_\eta$ (up to the overall $c$ factor). The equation $\partial_\xi\partial_\eta\phi = 0$ integrates to $\phi = f(\xi) + g(\eta) = f(x - ct) + g(x + ct)$. The piece $f(x - ct)$ is constant on the planes $x - ct = \text{const}$, which move at $dx/dt = c$ in the $+x$ direction; $g(x + ct)$ moves at $c$ in the $-x$ direction. $\blacksquare$

> [!note]- Lemma 3: A single wave is null and transverse
> **Statement:** For $F = k\wedge a$ with $k\cdot k = 0$ and $k\cdot a = 0$, both invariants vanish: $F_{\mu\nu}F^{\mu\nu} = 0$ and ${\star}F_{\mu\nu}F^{\mu\nu} = 0$.
>
> **Hint:** Compute each invariant from the wedge $F_{\mu\nu} = k_\mu a_\nu - k_\nu a_\mu$.
>
> **Why needed:** It establishes the null character that distinguishes a wave from a Coulomb field.
>
> > [!note]- Full proof
> > With $F_{\mu\nu} = k_\mu a_\nu - k_\nu a_\mu$, $F_{\mu\nu}F^{\mu\nu} = (k_\mu a_\nu - k_\nu a_\mu)(k^\mu a^\nu - k^\nu a^\mu) = 2[(k\cdot k)(a\cdot a) - (k\cdot a)^2]$. Since $k\cdot k = 0$ and $k\cdot a = 0$, this is $0$. For the second invariant, ${\star}F_{\mu\nu}F^{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma}F^{\mu\nu}$; with $F = k\wedge a$ this is proportional to $\epsilon_{\mu\nu\rho\sigma}k^\mu a^\nu k^\rho a^\sigma$, which vanishes because $\epsilon$ is totally antisymmetric and the arguments $k$ and $a$ each appear twice. Hence ${\star}F_{\mu\nu}F^{\mu\nu} = 0$. Both invariants vanish: the field is null. (The transversality $k\cdot a = 0$ and nullity $k\cdot k = 0$ are forced by $dF = 0$ for a field depending only on $k\cdot x$; the closedness requires the polarisation to be orthogonal to the null propagation vector.) $\blacksquare$

> [!note]- Lemma 4: $\mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ form an orthogonal triad with $|\mathbf E| = c|\mathbf B|$
> **Statement:** Decomposing $F = k\wedge a$ relative to an observer gives $\mathbf E\perp\mathbf B$, both $\perp\hat{\mathbf n}$, with $|\mathbf E| = c|\mathbf B|$.
>
> **Hint:** Write $k = \omega(U_0/c + \hat{\mathbf n})$ and extract $\mathbf E$, $\mathbf B$ from $F = k\wedge a$.
>
> **Why needed:** It recovers the experimental polarisation structure of light.
>
> > [!note]- Full proof
> > Relative to an observer of four-velocity $U_0$, a null wave-vector decomposes as $k = \omega(U_0 + \hat{\mathbf n})$ with $\hat{\mathbf n}$ a unit spatial vector (the propagation direction) and $\omega$ the frequency. The polarisation $a$, transverse to $k$ and (after a residual gauge choice) to $U_0$, is a spatial vector $\mathbf a\perp\hat{\mathbf n}$. From $F = k\wedge a$, the electric field $\mathbf E = F(\cdot, U_0)$ is $\propto\omega\mathbf a$ (transverse), and the magnetic field $\mathbf B = {\star}F(\cdot, U_0)$ is $\propto\omega\,\hat{\mathbf n}\times\mathbf a$ (also transverse, and perpendicular to $\mathbf E$). The magnitudes satisfy $|\mathbf B| = |\hat{\mathbf n}\times\mathbf a|\cdot(\omega/c) = |\mathbf E|/c$ since $|\hat{\mathbf n}| = 1$ and $\hat{\mathbf n}\perp\mathbf a$. Thus $\mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ are mutually orthogonal with $|\mathbf E| = c|\mathbf B|$, and the orientation $\mathbf E\times\mathbf B\parallel\hat{\mathbf n}$ makes them right-handed (the Poynting vector points along propagation). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **The wave equation.** In a charge-free region, the source-free [[Thm - Maxwell Equations|Maxwell equations]] are $dF = 0$ and $d{\star}F = 0$. By Lemma 1, writing $F = dA$ and imposing the [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] gives $\Box A = 0$, and since $\Box$ commutes with $d$, $\Box F = 0$. (Independently of any source, the inhomogeneous equation gives $\Box A = \mu_0 J$ in Lorenz gauge, hence $\Box F = -\mu_0\,dJ^\sharp$ in general, gauge-independently.)
>
> **Plane-wave solution.** By Lemma 2, the general solution depending on $(t, x)$ is $F = F_1(x - ct) + F_2(x + ct)$, a superposition of fields rigidly translating at $c$ in the $\pm x$ directions on the null planes $x \mp ct = \text{const}$.
>
> **Null and transverse.** A single wave $F = F_1(x - ct)$ depends only on the null combination $\xi = x - ct$; closedness $dF = 0$ forces $F = k\wedge a$ with $k$ the null wave-vector ($k\cdot k = 0$) and $a$ transverse ($k\cdot a = 0$). By Lemma 3, both invariants $F_{\mu\nu}F^{\mu\nu}$ and ${\star}F_{\mu\nu}F^{\mu\nu}$ vanish — the field is null. By Lemma 4, decomposing onto any observer gives $\mathbf E\perp\mathbf B\perp\hat{\mathbf n}$, a right-handed triad, with $|\mathbf E| = c|\mathbf B|$. These are exactly the properties of a light wave. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Gravitational waves.** The linearised Einstein equations in harmonic gauge read $\Box\bar h_{\mu\nu} = -16\pi G\,T_{\mu\nu}$; in vacuum $\Box\bar h_{\mu\nu} = 0$, the same wave equation, with solutions propagating at $c$ and two transverse-traceless polarisations. Recognising gravitational radiation as the tensor analogue of the electromagnetic wave is nonobvious because gravity is usually thought of as static (Newtonian), yet its radiative sector is structurally identical to electromagnetism's.

**Quantum field theory of the photon.** Quantising the free Maxwell field $\Box A = 0$ in Lorenz gauge gives the photon: the two transverse polarisations of the classical wave become the two helicity states of a massless spin-$1$ particle. Recognising the wave's polarisation structure as the photon's helicity is out-of-distribution because it bridges classical wave optics to particle physics; the masslessness is forced by gauge invariance.

**Acoustic and elastic waves.** The same d'Alembertian governs sound in a fluid ($\Box p = 0$ with $c$ the sound speed) and elastic waves in a solid, where the factoring into left- and right-movers and the transverse/longitudinal mode structure parallel the electromagnetic case. The application is surprising because the physics (pressure, displacement) is entirely different, yet the wave operator and its solution structure are identical — a universal feature of hyperbolic equations.

---

# Bridges

- **[[Thm - Maxwell Equations]]** — the wave equation $\Box F = 0$ is the vacuum combination of the two Maxwell equations: $dF = 0$ (closed) and $d{\star}F = 0$ (co-closed) together make $F$ harmonic, and the Lorentzian Laplacian is the wave operator. The displacement current in the inhomogeneous equation is exactly what makes $\Box F = 0$ have propagating rather than static solutions.

- **[[Def - Gauge Choice and the Lorenz Gauge]]** — the cleanest route to the wave equation is through the potential in Lorenz gauge, where $\Box A = \mu_0 J$ holds directly; the field inherits the wave equation because $\Box$ commutes with $d$. The Lorenz gauge is the gauge in which wave propagation is manifest, and the residual freedom $\Box\chi = 0$ is itself a wave equation for the gauge function.

- **[[Thm - The Liénard-Wiechert Potential]]** — the radiative part of the field of an accelerating charge is, far away, a plane wave: the $1/r$ radiative tail is a transverse, null field locally indistinguishable from a free wave. The Liénard–Wiechert field's far zone is where the source-free wave structure of this theorem applies, and the energy it carries is computed from the wave's Poynting flux.

- **Fourier analysis and wave optics** — because $\Box$ is linear, the plane waves $F = a\,e^{ik\cdot x}$ (with $k\cdot k = 0$) form a complete basis, and every vacuum field is a Fourier superposition of them. Interference, diffraction, and wave packets are all consequences of superposing solutions of $\Box F = 0$; the theorem is the foundation on which classical optics is built.

---

# Unlocked by This

> [!tip] Radiation and the Poynting Vector *(from Classical Electrodynamics)*
> The wave carries energy: the **Poynting vector** $\mathbf S = \varepsilon_0 c^2\mathbf E\times\mathbf B$ is the energy flux, and for a wave with $|\mathbf E| = c|\mathbf B|$ it points along $\hat{\mathbf n}$ with magnitude $\varepsilon_0 c E^2$. Integrating the Poynting flux of the radiative far field over a sphere gives the radiated power, the engine of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]] and the Larmor formula. The energy and momentum of the wave are packaged in the electromagnetic energy–momentum tensor $T^{\mu\nu}$.

> [!tip] The Photon and Quantum Optics *(from QFT)*
> Quantising $\Box A = 0$ promotes the two transverse polarisations of the classical wave to the two helicity states of the **photon**, a massless spin-$1$ particle. The masslessness is forced by the gauge invariance $A \to A + d\chi$, which removes the longitudinal and timelike polarisations; this is why the photon has only two states rather than three. The wave's frequency $\omega$ and wave-vector $\mathbf k$ become the photon's energy $\hbar\omega$ and momentum $\hbar\mathbf k$, the null condition $k\cdot k = 0$ becoming the masslessness $E = |\mathbf p|c$.
