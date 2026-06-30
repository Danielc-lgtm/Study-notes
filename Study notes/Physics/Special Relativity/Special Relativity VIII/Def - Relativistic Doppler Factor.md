---
type: definition
subject: special-relativity
prereqs:
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Velocity Relative to an Observer"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike four-velocity $u$ has $u \cdot u = +1$. Two observers $\mathcal{O}$ (the receiver) and $\mathcal{O}'$ (the emitter) have four-velocities $u, u'$; $\mathbf{V}$ is the velocity of the emitter $\mathcal{O}'$ relative to the receiver $\mathcal{O}$, a spacelike vector in the receiver's [[Def - Observer and Local Rest Space|local rest space]] $E_u$, with magnitude $V = \lVert \mathbf{V}\rVert_g$ and $\Gamma = (1 - V^2)^{-1/2} = u \cdot u'$ the [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] between them. The unit vector $\mathbf{n} \in E_u$ points **from the emitter toward the receiver** (the direction along which the receiver sees the light coming in, reversed — see the warning below). Frequencies are $f_{\mathrm{em}}$ (proper frequency of the source, measured in $\mathcal{O}'$'s frame) and $f_{\mathrm{rec}}$ (measured by $\mathcal{O}$). Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

> [!warning] Convention: the sign of $\mathbf{n}\cdot\mathbf{V}$ and Gourgoulhon's signature
> Two convention choices must be fixed together. **(i) Signature.** Gourgoulhon works in mostly-plus $\mathrm{diag}(-1,+1,+1,+1)$; here everything is mostly-minus, but the Doppler factor is a ratio of frequencies and so is signature-independent once $\mathbf{n}\cdot\mathbf{V}$ is read as an ordinary spatial dot product in the receiver's rest space. **(ii) Direction of $\mathbf{n}$.** We take $\mathbf{n}$ to point from emitter to receiver, so that an *approaching* source ($\mathbf{n}\cdot\mathbf{V} > 0$, the source velocity has a component toward the receiver) gives a *blueshift* $f_{\mathrm{rec}} > f_{\mathrm{em}}$. Some texts let $\mathbf{n}$ be the direction of light *propagation* (emitter to receiver, same as here) and others the direction *of observation* (receiver's line of sight toward the source, the negative of here); under that opposite choice the sign in $(1 - \mathbf{n}\cdot\mathbf{V})$ flips to $(1 + \mathbf{n}\cdot\mathbf{V})$. Always check, on a definitely-approaching source, that your formula gives a blueshift.

---

# Axiom Motivation

We want a single number that captures *everything* about how the motion of a light source changes the frequency a receiver measures. The acoustic Doppler effect — a passing siren dropping in pitch — already supplies a Newtonian template: the received frequency is the emitted frequency times a factor depending on the radial velocity. The question is what the *relativistic* factor must be, and why it cannot be the Newtonian one.

The first desideratum is that the factor must reduce to the Newtonian first-order shift $1 + \mathbf{n}\cdot\mathbf{V}$ when speeds are small, because at low velocity relativity must agree with everyday experience and with the well-tested acoustic analogy. So whatever we write must have $1 + \mathbf{n}\cdot\mathbf{V}$, or its reciprocal $1/(1 - \mathbf{n}\cdot\mathbf{V})$, as its leading behaviour. This already forces a *direction dependence*: the shift is largest for a source moving straight at the receiver and vanishes, to this order, for a source moving sideways.

The second desideratum is the one that has no Newtonian analogue and pins the factor uniquely: the *clock of the moving source runs slow*. The source emits one wave-crest per period of *its own* proper time; but the receiver measures intervals in *its* time, and the moving source's proper time is dilated by the [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] $\Gamma$ relative to the receiver. So even before any geometric direction effect, the source appears to tick — and therefore to emit crests — slower by a factor $\Gamma$. This is a genuinely relativistic, second-order ($V^2$) effect, and it is present for *any* direction of motion, including the transverse direction where the first-order effect vanishes entirely. The factor must therefore contain a $1/\Gamma$ that does not switch off when $\mathbf{n}\cdot\mathbf{V} = 0$.

Putting these together, the factor must be a product of a *classical direction part* and a *relativistic time-dilation part*:
$$\mathcal{D} = \underbrace{\frac{1}{1 - \mathbf{n}\cdot\mathbf{V}}}_{\text{classical, first order, directional}} \times \underbrace{\frac{1}{\Gamma}}_{\text{relativistic, second order, always present}}.$$
Why this particular combination and not, say, $1/\Gamma + 1/(1 - \mathbf{n}\cdot\mathbf{V})$ or some other assembly? Because the two effects act *multiplicatively on the period*: the geometric retardation stretches the *coordinate-time* interval between crest-arrivals by $1/(1 - \mathbf{n}\cdot\mathbf{V})$, and the time dilation converts the source's proper period into coordinate time by an independent factor $\Gamma$. Periods multiply, so frequencies (their reciprocals) multiply, giving the product above. The derivation in [[Thm - The Doppler Effect]] confirms this by computing the two crest-arrival events explicitly.

Consider what would break if either factor were dropped. Drop the $1/\Gamma$ and you have the Newtonian formula, which predicts *no shift at all* for a transversely moving source — directly contradicted by the Ives–Stilwell experiment, which measures a redshift for atoms moving across the line of sight. Drop the classical $1/(1 - \mathbf{n}\cdot\mathbf{V})$ and you lose the ordinary blue/redshift of approaching and receding sources — the effect that lets astronomers measure radial velocities of stars and galaxies, and that dominates by an order of magnitude at any speed where the classical part is appreciable. Each factor is indispensable, and they occupy different orders in $V$: the classical part is the leading term, the relativistic part the leading *correction*. The whole content of the relativistic Doppler effect, beyond the acoustic one, is the surviving $1/\Gamma$.

---

# The Definition

The **relativistic Doppler factor** for light emitted by a source $\mathcal{O}'$ and received by an observer $\mathcal{O}$ is the ratio of received to emitted frequency,
$$
\boxed{\;\mathcal{D} \;:=\; \frac{f_{\mathrm{rec}}}{f_{\mathrm{em}}} \;=\; \frac{1}{\Gamma\,(1 - \mathbf{n}\cdot\mathbf{V})}\;}
\qquad\Big(\text{with } c:\;\; \mathcal{D} = \frac{1}{\Gamma\,(1 - \mathbf{n}\cdot\mathbf{V}/c)}\Big),
$$
where $\mathbf{V}$ is the velocity of the source relative to the receiver, $\mathbf{n}$ the unit vector from source to receiver, $\mathbf{n}\cdot\mathbf{V}$ the ordinary spatial dot product (the radial component of the source velocity), and $\Gamma = (1 - V^2)^{-1/2}$ the Lorentz factor between the two observers.

Equivalently, the factor is the ratio of emitted to received *period*, $\mathcal{D} = \Delta t_{\mathrm{em}}/\Delta t_{\mathrm{rec}}$, and because a photon's energy is proportional to its frequency ([[Def - The Four-Momentum of a Photon]]), it is also the ratio of received to emitted photon energy, $\mathcal{D} = E_{\mathrm{rec}}/E_{\mathrm{em}}$, and of received to emitted wave-number magnitude.

Two specialisations are worth recording:

**Radial (line-of-sight) motion.** If the source moves directly along the line connecting it to the receiver, $\mathbf{V} = V\mathbf{n}$ with $V > 0$ for approach, then $\mathbf{n}\cdot\mathbf{V} = V$ and the factor collapses to
$$
\mathcal{D}_{\mathrm{radial}} = \frac{1}{\Gamma(1 - V)} = \sqrt{\frac{1 + V}{1 - V}}\qquad(\text{approach}),
$$
using $\Gamma(1-V) = \sqrt{(1-V)/(1+V)}$. Receding motion ($V \to -V$) gives the reciprocal, a redshift.

**Transverse motion.** If the source moves perpendicular to the line of sight, $\mathbf{n}\cdot\mathbf{V} = 0$ and
$$
\mathcal{D}_{\mathrm{transverse}} = \frac{1}{\Gamma} < 1,
$$
a pure redshift with no classical analogue — the **transverse Doppler effect**, equal to the time dilation of the source clock.

---

# Categorical / Structural Definition

The Doppler factor is most cleanly understood as a *component of the action of the Lorentz group on the null tangent of a light ray*. A photon through an event has a future-directed null tangent $\ell$. Relative to an observer with four-velocity $u$, this tangent decomposes as $\ell = \omega\,(u + \mathbf{n})$, where $\omega > 0$ is the frequency the observer measures (up to the universal factor $\hbar$, the energy) and $\mathbf{n} \in E_u$ is the unit propagation direction the observer sees. The decomposition exhibits the two observer-dependent data carried by one ray: a positive scalar $\omega$ (frequency) and a point $\mathbf{n}$ of the observer's celestial sphere (direction).

Now change observer from $\mathcal{O}$ (four-velocity $u$) to $\mathcal{O}'$ (four-velocity $u'$). The *same* null tangent $\ell$ decomposes in $\mathcal{O}'$'s frame as $\ell = \omega'(u' + \mathbf{n}')$. The Doppler factor is exactly the ratio of the two frequency components,
$$
\mathcal{D} = \frac{\omega'}{\omega} = \frac{u' \cdot \ell}{u \cdot \ell},
$$
since $u \cdot \ell = \omega(u\cdot u) = \omega$ (using $u\cdot u = 1$, $u\cdot\mathbf{n} = 0$) and likewise $u'\cdot\ell = \omega'$. Written this way the factor is manifestly a *scalar*, a ratio of two invariant scalar products of the fixed null vector $\ell$ with the two four-velocities — which is why it is a clean geometric object and not merely an algebraic combination. The companion datum, the change $\mathbf{n} \mapsto \mathbf{n}'$, is the [[Thm - Aberration of Light|aberration]]; frequency-shift and aberration are the two halves of one map, the action of the boost relating $u$ and $u'$ on the ray. This is the structural fact that [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]] turns into the Möbius action on the celestial sphere.

---

# Relate to Other Fields / Compression

The Doppler factor is the relativistic deformation of the acoustic Doppler factor, with one structural addition. In acoustics the medium (air) provides a preferred rest frame, so the source-Doppler and observer-Doppler shifts are *different* functions of velocity, and the factor depends on the velocities of source and observer *separately* relative to the medium. In relativity there is no medium and no preferred frame, so the factor can depend only on the *relative* velocity of source and receiver — and the symmetry of the situation forces in the time-dilation factor $\Gamma$ that acoustics lacks. The classical part $1/(1 - \mathbf{n}\cdot\mathbf{V})$ is the acoustic factor in the limit where the wave speed is $c$; the $1/\Gamma$ is the purely relativistic addition.

In quantum-mechanical language the factor is the ratio of photon energies, $\mathcal{D} = E_{\mathrm{rec}}/E_{\mathrm{em}}$, because $E = \hbar\omega$. This is why the Doppler effect is equivalently a statement about the [[Def - The Four-Momentum of a Photon|photon four-momentum]]: the photon's energy is $E = P \cdot u$, the projection of its four-momentum on the observer's four-velocity, and the Doppler factor is the ratio of this projection onto the two observers. The Mössbauer effect and gravitational redshift experiments (Pound–Rebka) measure exactly this energy ratio for $\gamma$-ray photons.

**True name:** the Doppler factor is *the ratio of the null tangent's projections onto the two observers' four-velocities*, $\mathcal{D} = (u'\cdot\ell)/(u\cdot\ell)$. This operational form is what to reach for in any four-vector calculation: it makes the factor manifestly invariant, it derives the radial and transverse special cases by inspection, and it generalises without change to curved spacetime, where $u, u', \ell$ are taken at the emission and reception events along the photon's actual (possibly bent) null geodesic.

---

# Examples / Corollaries

**Is an instance — the radial blueshift of an approaching star.** A star approaching at $V = 0.1$ along the line of sight has $\mathcal{D} = \sqrt{1.1/0.9} \approx 1.106$, so its spectral lines are shifted to the blue by about $10.6\%$ in frequency. Astronomers invert this to read off radial velocities; the linear approximation $\mathcal{D} \approx 1 + V$ suffices for stellar speeds.

**Is an instance — the transverse redshift in Ives–Stilwell.** Hydrogen atoms in a beam, observed at right angles to their motion, emit light redshifted by exactly $1/\Gamma$. At the beam speed $V \approx 4\times 10^{-3}$ used by Ives and Stilwell, $1/\Gamma \approx 1 - \tfrac12 V^2 \approx 1 - 8\times 10^{-6}$, a few parts in a million — small, but the *only* effect at this geometry, and its detection (via the averaging trick of [[Ex - The Ives-Stilwell experiment and transverse Doppler]]) was the first laboratory confirmation of time dilation.

**Is an instance — relativistic beaming of a jet.** The same factor (raised to a power that depends on the spectral shape) multiplies the *intensity* of a relativistically moving source, not just the frequency: an approaching jet with $\mathcal{D} \gg 1$ is beamed forward and appears far brighter than a receding one with $\mathcal{D} \ll 1$. This is why one usually sees only the approaching jet of a double-jet source — its counter-jet is Doppler-dimmed below detection.

**Is NOT an instance — the acoustic Doppler shift of a siren.** The factor for sound is *not* $1/[\Gamma(1 - \mathbf{n}\cdot\mathbf{V})]$: it contains no $\Gamma$ (there is no time dilation in Newtonian acoustics) and it depends on the velocities of source and observer *separately* relative to the air, not only on their relative velocity. A source and observer at rest relative to each other but both moving through the air register *no* shift acoustically and *no* shift relativistically — but a source and observer in relative transverse motion register *no* first-order acoustic shift yet a relativistic transverse redshift $1/\Gamma$. The presence of a medium is exactly what distinguishes the two.

**Is NOT an instance — a frequency change from gravity alone in flat spacetime.** In special relativity, with no gravity, a source and receiver at rest relative to one another ($\mathbf{V} = 0$, $\Gamma = 1$) register $\mathcal{D} = 1$, no shift, regardless of their separation. The gravitational redshift, by contrast, shifts the frequency between two *static* observers at different potentials with no relative velocity at all; it requires curved spacetime (see [[Special Relativity XXV — Toward Relativistic Gravitation]]) and is not an instance of the kinematic Doppler factor.

**Corollary — the factor is multiplicative under composition.** If $\mathcal{O}'$ recedes from $\mathcal{O}$ and $\mathcal{O}''$ recedes collinearly from $\mathcal{O}'$, the Doppler factor from $\mathcal{O}''$ to $\mathcal{O}$ is the *product* $\mathcal{D}(\mathcal{O}\leftarrow\mathcal{O}')\,\mathcal{D}(\mathcal{O}'\leftarrow\mathcal{O}'')$ — equivalently, in terms of rapidity $\varphi$ (with $V = \tanh\varphi$), the radial factor is $\mathcal{D} = e^{-\varphi}$ for recession, and rapidities add. This is the cleanest statement of relativistic Doppler: *the Doppler factor is the exponential of (minus) the rapidity*, so frequency shifts compose by multiplying, exactly as boosts compose by adding rapidities.

**Corollary — forward and backward radial factors multiply to one.** For motion at speed $V$ directly toward and directly away, $\mathcal{D}_{\mathrm{toward}}\cdot\mathcal{D}_{\mathrm{away}} = \sqrt{(1+V)/(1-V)}\cdot\sqrt{(1-V)/(1+V)} = 1$. This is the basis of the modern Ives–Stilwell test (Reinhardt 2007), which measures the *product* of the two shifted frequencies and checks it equals $f_0^2$, independently of $V$.

**Calibration check.** If you have understood the definition you should be able to: (i) check that the radial factor $1/[\Gamma(1-V)]$ equals $\sqrt{(1+V)/(1-V)}$ by writing $\Gamma = 1/\sqrt{1-V^2}$ and factoring $1 - V^2 = (1-V)(1+V)$; (ii) confirm that for transverse motion the factor is $1/\Gamma < 1$, a redshift, and explain in one sentence why it is a redshift and not a blueshift (the moving clock runs slow, so crests arrive less often); and (iii) verify that as $V \to 0$ the factor becomes $1 + \mathbf{n}\cdot\mathbf{V} + O(V^2)$, recovering the Newtonian first-order shift.

---

# Unlocked by This

> [!tip] The Photon Four-Momentum Transformation *(from Relativistic Dynamics)*
> Because a photon's energy is $E = \hbar\omega$ and its momentum magnitude is $p = \hbar\omega$ (with $c=1$), the Doppler factor is simultaneously the transformation law for a photon's **energy and momentum** under a change of observer: $E_{\mathrm{rec}} = \mathcal{D}\,E_{\mathrm{em}}$. This is the kinematic input to **Compton scattering**, the **inverse-Compton** boosting of photons by relativistic electrons, and the **relativistic beaming** of moving sources; the four-momentum version is developed in [[Special Relativity XIII — Energy and Momentum]].

> [!tip] The Möbius Action on the Celestial Sphere *(from SL(2,C) and Spinors)*
> The Doppler factor and the [[Thm - Aberration of Light|aberration]] of the same ray are the two components of the action of a Lorentz transformation on a null direction. Encoding the sky as the Riemann sphere $\mathbb{C}P^1$, this action is a **Möbius transformation**, and the Doppler factor is the modulus-type scaling that accompanies the fractional-linear map of the direction. This is the geometric content of the spinor map $SL(2,\mathbb{C}) \to SO^+(1,3)$ — see [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

> [!tip] Cosmological Redshift and the Expanding Universe *(from General Relativity and Cosmology)*
> In an expanding universe the wavelength of light is stretched by the **scale factor** between emission and reception, giving the cosmological redshift $1 + z = a(t_{\mathrm{rec}})/a(t_{\mathrm{em}})$. For nearby sources this reduces to the kinematic radial Doppler factor defined here (Hubble's law $V = H_0 d$), but for distant sources it is a genuinely gravitational effect of the time-dependent metric, not a velocity Doppler shift — the distinction between the two is one of the subtle conceptual points where the flat-spacetime factor of this page must be handled with care.
