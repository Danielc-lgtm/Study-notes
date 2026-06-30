---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Def - The Electromagnetic Field Tensor"
  - "Thm - Energy-Momentum Conservation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ unless $c$ is restored for recognisability, with mostly-minus signature $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$. $F$ is the [[Def - The Electromagnetic Field Tensor|electromagnetic field tensor]], an antisymmetric $(0,2)$-tensor with components $F_{\mu\nu}$; raised components $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta}$. Relative to an observer of four-velocity $U_0$, the electric and magnetic fields are $\mathbf{E} = F(\,\cdot\,, U_0)$ and $\mathbf{B}$, both spatial vectors in the rest space; $E = |\mathbf{E}|$, $B = |\mathbf{B}|$. The constant $\varepsilon_0$ is the vacuum permittivity, $\mu_0$ the permeability, with $\varepsilon_0\mu_0 c^2 = 1$. $J$ is the [[Def - The Electric Four-Current|electric four-current]]. The field invariants are $F_{\mu\nu}F^{\mu\nu} = 2(B^2 - E^2)$ (with $c=1$) and $({\star}F)_{\mu\nu}F^{\mu\nu} \propto \mathbf{E}\cdot\mathbf{B}$. Full registry on [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!warning] Convention
> Two conventions collide on this page. First, **signature**: Gourgoulhon uses mostly-plus, in which the trace term reads $-\tfrac14 F_{\mu\nu}F^{\mu\nu}\,g_{\alpha\beta}$ with his $g$; translating to mostly-minus flips the sign of $\eta^{\mu\nu}$ relative to his $g_{\alpha\beta}$, and the form below is the correct mostly-minus expression. Second, **units**: in SI the tensor carries a factor $\varepsilon_0$ (and a $\mu_0$ in the magnetic terms); in Heaviside–Lorentz / Gaussian units one sets $\varepsilon_0 = 1$ (or $4\pi$) and the famous compact form $T^{\mu\nu} = F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}$ results. Both are given; they differ only by the overall constant and the placement of $c$.

---

# Axiom Motivation

A region of pure electromagnetic field, with not a single charge inside it, can carry energy and momentum: sunlight warms your skin, a laser pushes a mirror, a radio wave makes an antenna current flow. So the field has an energy-momentum tensor of its own, and the problem is to find it. The naive hope — that we could just *postulate* "the field energy density is $\tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$" and assemble a tensor by hand — is fragile: it would not tell us the momentum density or the stress without separate guesses, and it would not guarantee the result transforms as a tensor. We want a principled construction, and the principle is **conservation**.

Here is the logic that forces the tensor. A system of charged particles in an electromagnetic field is *not* isolated: the field pushes on the charges, doing work and delivering momentum, so the particles' own energy-momentum tensor $T_{\text{mat}}$ has a nonzero divergence, $\vec\nabla\cdot T_{\text{mat}} = \mathcal F$, where $\mathcal F$ is the [[Thm - Energy-Momentum Conservation|four-force density]] the field exerts. By the Lorentz force law this density is $\mathcal F = F(\,\cdot\,, J)$, i.e. $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$. Now the *total* system — charges plus field — *is* isolated, because there is nothing outside it. So total energy-momentum must be conserved: there must exist a tensor $T_{\text{em}}$, attributable to the field, such that $\vec\nabla\cdot(T_{\text{mat}} + T_{\text{em}}) = 0$. This requires $\vec\nabla\cdot T_{\text{em}} = -\mathcal F = -F(\,\cdot\,, J)$. The construction is therefore: *find the symmetric tensor built from $F$ whose divergence equals minus the Lorentz four-force density.* There is essentially one answer, and that answer is the definition.

To find it, feed in what we know. The four-force density is $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$. Use the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$ to eliminate the current in favour of the field:
$$
\mathcal F_\alpha = \varepsilon_0\, F_{\alpha\mu}\nabla_\beta F^{\mu\beta}.
$$
This is a product of $F$ with a derivative of $F$, and the trick is to write it as a total divergence plus a leftover, then absorb the leftover using the *homogeneous* Maxwell equation $\mathrm dF = 0$. The homogeneous equation, written with the covariant derivative, is $\nabla_\beta F_{\mu\alpha} + \nabla_\mu F_{\alpha\beta} + \nabla_\alpha F_{\beta\mu} = 0$, the cyclic Bianchi-type identity, and contracting it against $F^{\mu\beta}$ yields the key identity $F^{\mu\beta}\nabla_\beta F_{\mu\alpha} = \tfrac14\nabla_\alpha(F_{\mu\nu}F^{\mu\nu})$. With this, the force density collapses to a single divergence,
$$
\mathcal F_\alpha = -\varepsilon_0\Big[\nabla_\beta\big(F_{\mu\alpha}F^{\mu\beta}\big) - \tfrac14\nabla_\alpha\big(F_{\mu\nu}F^{\mu\nu}\big)\Big] = -\nabla^\beta\Big[\varepsilon_0\big(F_{\mu\alpha}F^\mu{}_\beta - \tfrac14 g_{\alpha\beta}F_{\mu\nu}F^{\mu\nu}\big)\Big],
$$
and the bracketed object — manifestly a symmetric tensor built from $F$ — is exactly the energy-momentum tensor we sought, with $\mathcal F_\alpha = -\nabla^\beta T^{\text{em}}_{\alpha\beta}$.

Now examine the structure that fell out, because every term earns its place. The first term $F_{\mu\alpha}F^\mu{}_\beta$ is a symmetric product of two field tensors — it must be symmetric for $T$ to be a valid energy-momentum tensor, and it is, by the antisymmetry of $F$ ($F_{\mu\alpha}F^\mu{}_\beta = F_{\mu\beta}F^\mu{}_\alpha$ after relabelling). The second term, the trace piece $-\tfrac14 g_{\alpha\beta}F_{\mu\nu}F^{\mu\nu}$, is forced by the calculation, not added by hand: without it the divergence would not reproduce the Lorentz force, because the leftover from the homogeneous equation has to be cancelled. What would go wrong if we dropped it? The tensor would have the wrong divergence, energy-momentum would *not* be conserved, and the field could not consistently exchange energy with charges. The coefficient $\tfrac14$ is similarly fixed — it is the unique value that makes the cancellation exact.

The trace piece has a second virtue worth seeing in advance: it makes $T_{\text{em}}$ **traceless**. Taking the trace, $T^\mu{}_\mu = \varepsilon_0(F_{\mu\alpha}F^{\mu\alpha} - \tfrac14\cdot 4\cdot F_{\mu\nu}F^{\mu\nu}) = \varepsilon_0(F_{\mu\nu}F^{\mu\nu} - F_{\mu\nu}F^{\mu\nu}) = 0$, where the factor of $4$ comes from $g^{\alpha\beta}g_{\alpha\beta} = 4$ in four dimensions. The coefficient $\tfrac14$ is precisely $1/(\text{spacetime dimension})$ — it is the value that makes the trace vanish, and the vanishing trace is the deep statement that the electromagnetic field is *conformally invariant* and the photon is *massless*. So the same number, $\tfrac14$, is fixed independently by conservation and by tracelessness, and the two facts agree: this is the signature of a correct construction.

---

# The Definition

The **energy-momentum tensor of the electromagnetic field** is the symmetric, traceless $(0,2)$-tensor
$$
T^{\text{em}}_{\alpha\beta} \;=\; \varepsilon_0\left( F_{\mu\alpha}\,F^\mu{}_\beta \;-\; \tfrac14\, \eta_{\alpha\beta}\, F_{\mu\nu}F^{\mu\nu}\right),
$$
equivalently, with indices raised,
$$
T_{\text{em}}^{\mu\nu} \;=\; \varepsilon_0\left( F^{\mu\alpha}\,F^\nu{}_\alpha \;-\; \tfrac14\,\eta^{\mu\nu}\, F_{\alpha\beta}F^{\alpha\beta}\right).
$$
In **Heaviside–Lorentz units** ($\varepsilon_0 = 1$) this is the compact form quoted in field theory,
$$
T_{\text{em}}^{\mu\nu} = F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\,\eta^{\mu\nu}F^2, \qquad F^2 := F_{\alpha\beta}F^{\alpha\beta}.
$$
It satisfies, by construction, $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -\mathcal F_\alpha = -F_{\alpha\mu}J^\mu$, so that the total energy-momentum of field plus charges is conserved:
$$
\vec\nabla\cdot\big(T_{\text{em}} + T_{\text{mat}}\big) = 0.
$$
It is **symmetric** ($T^{\text{em}}_{\alpha\beta} = T^{\text{em}}_{\beta\alpha}$) and **traceless** ($\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = 0$).

**Quantities relative to an observer.** For an observer of four-velocity $U_0$ measuring electric field $\mathbf E$ and magnetic field $\mathbf B$:

- **Energy density:** $\displaystyle \rho_{\text{em}} = T_{\text{em}}(U_0, U_0) = \frac{\varepsilon_0}{2}\left(\mathbf{E}\cdot\mathbf{E} + c^2\,\mathbf{B}\cdot\mathbf{B}\right)$, the familiar $\tfrac12(\varepsilon_0 E^2 + B^2/\mu_0)$ with $c$ restored.

- **Energy-flux density (Poynting vector):** $\displaystyle \vec\varphi_{\text{em}} = \frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}$, the rate at which field energy crosses a surface per unit area.

- **Momentum density:** $\displaystyle \vec\varpi_{\text{em}} = \varepsilon_0\,\mathbf{E}\times\mathbf{B} = \frac{1}{c^2}\vec\varphi_{\text{em}}$, consistent with the general identity $\varphi = c^2\varpi$.

- **Stress (Maxwell stress tensor):** $\displaystyle S^{\text{em}}_{ij} = \varepsilon_0\left[\tfrac12\big(\mathbf{E}\cdot\mathbf{E} + c^2\mathbf{B}\cdot\mathbf{B}\big)\delta_{ij} - E_iE_j - c^2 B_iB_j\right]$, the force per unit area transmitted across a surface, i.e. $\mathbf{S}_{\text{em}} = \rho_{\text{em}}(\eta + U_0^\flat\otimes U_0^\flat) - \varepsilon_0(\mathbf E\otimes\mathbf E + c^2\mathbf B\otimes\mathbf B)$.

For the **radiative field** of an accelerated charge, for which the field invariant $F_{\mu\nu}F^{\mu\nu}$ vanishes (the radiation field is null), the trace term drops and the tensor reduces to $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\text{rad}})_{\mu\alpha}(F_{\text{rad}})^\mu{}_\beta$, which is used to compute radiated power on [[Thm - Radiation by an Accelerated Charge (Larmor Formula)]].

---

# Categorical / Structural Definition

The electromagnetic energy-momentum tensor is the canonical example of the *Hilbert (metric) energy-momentum tensor* obtained by varying the field action with respect to the metric. The Maxwell action is $S_{\text{em}} = -\tfrac{1}{4\mu_0}\int F_{\mu\nu}F^{\mu\nu}\sqrt{-g}\,\mathrm d^4x$, and
$$
T^{\text{em}}_{\mu\nu} = \frac{-2}{\sqrt{-g}}\frac{\delta S_{\text{em}}}{\delta g^{\mu\nu}}
$$
returns exactly the tensor above. This derivation makes three of its properties automatic and structural rather than computational. *Symmetry* is automatic because $g^{\mu\nu}$ is symmetric, so its variational partner is too. *Tracelessness* is the statement that the action is invariant under conformal rescalings $g_{\mu\nu}\mapsto\Omega^2 g_{\mu\nu}$ of the metric — Maxwell theory in four dimensions has no length scale, the photon is massless, and Noether's theorem for conformal symmetry gives $T^\mu{}_\mu = 0$. *Conservation* is Noether's theorem for diffeomorphism (in flat space, translation) invariance. The same variational definition is what makes $T_{\text{em}}$ the correct source term in the Einstein equation: the electromagnetic field gravitates through precisely the object you get by asking how its action responds to a change of geometry. This places the present construction — divergence equals minus the Lorentz force — and the variational construction on the same footing: they agree because both are extracting the conserved current of spacetime symmetry from the field.

---

# Relate to Other Fields / Compression

This tensor unifies the three energy quantities of pre-relativistic electromagnetism — Poynting's energy density, Poynting's energy flux, and Maxwell's stress tensor — into a single object, exactly as the general [[Def - The Energy-Momentum Tensor|energy-momentum tensor]] unifies density, momentum, and stress for matter. Poynting's theorem $\partial_t u + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E$ and the Maxwell-stress momentum-balance law $\partial_t\mathbf g + \vec\nabla\cdot\overleftrightarrow{T} = -(\rho\mathbf E + \mathbf j\times\mathbf B)$ are precisely the time and space components of the single covariant law $\nabla_\mu T_{\text{em}}^{\mu\nu} = -F^{\nu}{}_\mu J^\mu$. What three nineteenth-century theorems said, one tensor equation now says.

**True name:** the electromagnetic energy-momentum tensor is *the unique symmetric traceless tensor quadratic in $F$ whose divergence is the negative Lorentz four-force density.* Both qualifiers are load-bearing: "quadratic in $F$" because energy is quadratic in field amplitude; "traceless" because the photon is massless; and "divergence = $-\mathcal F$" because that is the conservation requirement that fixes every coefficient. When you need to remember the tensor, do not memorise the matrix — remember that it is built to make field-plus-matter energy-momentum conserved, and reconstruct it from $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$ and the Maxwell equations.

The structure $F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F^2$ recurs verbatim in **Yang–Mills theory**: the energy-momentum tensor of a non-abelian gauge field is $T^{\mu\nu} = \mathrm{tr}(F^{\mu\alpha}F^\nu{}_\alpha) - \tfrac14\eta^{\mu\nu}\mathrm{tr}(F^2)$, the abelian formula with a colour trace inserted. The gluon field of quantum chromodynamics carries energy and momentum by exactly this expression, which is why most of the mass of the proton — the energy of confined gluon and quark fields — is, in the end, this tensor's $00$ component integrated over the proton.

---

# Examples / Corollaries

**Is an instance — a static Coulomb field.** Around a point charge at rest, $\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0 r^2)$ and $\mathbf B = 0$. The energy density is $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}E^2 = q^2/(32\pi^2\varepsilon_0 r^4)$, the Poynting vector vanishes (no energy flows in a static field), and the Maxwell stress is a tension along field lines and a pressure across them — the mechanism by which like charges "feel" their repulsion as a real stress in the field between them. Integrating $\rho_{\text{em}}$ over all space outside a radius $a$ gives the field energy $q^2/(8\pi\varepsilon_0 a)$, the electrostatic self-energy.

**Is an instance — a plane electromagnetic wave.** For a wave travelling in the $\hat{\mathbf n}$ direction, $\mathbf B = \hat{\mathbf n}\times\mathbf E/c$ and $E = cB$, so the magnetic and electric energy densities are equal and $\rho_{\text{em}} = \varepsilon_0 E^2$. The Poynting vector is $\vec\varphi_{\text{em}} = \varepsilon_0 c E^2\,\hat{\mathbf n} = \rho_{\text{em}}\,c\,\hat{\mathbf n}$: the energy flows at the speed of light in the propagation direction, as it must for radiation. The momentum density is $\rho_{\text{em}}/c$ along $\hat{\mathbf n}$ — so the wave carries momentum $E/c$ per unit energy, the radiation-pressure relation, and the field invariant $E^2 - c^2B^2 = 0$ confirms the wave is null.

**Is NOT an instance — a tensor with a nonzero trace.** Any candidate "electromagnetic energy-momentum tensor" with $T^\mu{}_\mu \ne 0$ is wrong. The dust tensor $\varepsilon_0 U^\mu U^\nu$ has trace $\varepsilon_0 \ne 0$ and describes massive matter, not radiation; if you ever compute an electromagnetic $T$ and find a nonzero trace, you have made a sign error in the $\tfrac14$ term. Tracelessness is the calibration that the photon is massless.

**Corollary — radiation pressure.** A perfectly absorbing surface hit by a wave of energy density $\rho_{\text{em}}$ at normal incidence feels a pressure $P = \rho_{\text{em}}$ (the $\hat{\mathbf n}\hat{\mathbf n}$ component of the Maxwell stress for a null field), and a perfectly reflecting surface feels $2\rho_{\text{em}}$. This is the force that drives solar sails and that, summed over a star's interior, provides radiation pressure support against gravity.

**Corollary — the field invariant controls the structure.** When $F_{\mu\nu}F^{\mu\nu} > 0$ (magnetic-dominated, $B > E/c$) there is a frame where the field is purely magnetic; when $< 0$ (electric-dominated) a frame where it is purely electric; when $= 0$ (radiative/null) no such frame exists. The trace term of $T_{\text{em}}$ carries exactly this invariant, which is why the radiative tensor (null field, invariant zero) loses its trace term entirely. See [[Thm - The Electromagnetic Field Invariants]].

**Calibration check.** If you have understood the definition you should be able to: (i) verify that $T_{\text{em}}$ is traceless by contracting with $\eta^{\alpha\beta}$ and using $g^{\alpha\beta}g_{\alpha\beta} = 4$; (ii) compute $\rho_{\text{em}} = T_{\text{em}}(U_0,U_0)$ from the component definition and recover $\tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$, checking that the trace term contributes through $\eta_{\alpha\beta}U_0^\alpha U_0^\beta = 1$; and (iii) confirm that for a null (radiative) field the energy density equals the magnitude of the momentum density times $c$, the hallmark of something moving at the speed of light.

---

# Unlocked by This

> [!tip] Radiated Power and the Larmor Formula *(from Radiation Theory)*
> Contracting the radiative part of $T_{\text{em}}$ with the propagation direction and integrating over a sphere surrounding an accelerated charge gives the total radiated power — the **Larmor formula** and its relativistic generalisation, the **Liénard formula** — derived on [[Thm - Radiation by an Accelerated Charge (Larmor Formula)]]. The energy-momentum tensor is the bridge from "the field of a charge" to "the energy that charge loses": you compute $T_{\text{em}}$ from the radiative field and read off the flux.

> [!tip] Electromagnetic Mass and the Abraham–Lorentz Problem *(from Classical Electron Theory)*
> Integrating $T_{\text{em}}$ over the field of a moving charge assigns the field an energy and a momentum, and demanding these transform as a four-vector exposes the classical **"4/3 problem"**: the naive field momentum of a charged sphere is $\tfrac43$ of (energy)$/c^2$, a famous inconsistency resolved only by including the stresses (Poincaré stresses) that hold the charge together. This is the historical seed of the **Abraham–Lorentz radiation-reaction force** and the recognition that a point charge cannot be treated as purely electromagnetic.

> [!tip] The Source of Gravity for Light *(from General Relativity)*
> Because $T_{\text{em}}$ is the source term in the Einstein equation, **light gravitates**: a box of radiation has weight, two beams of light attract, and the energy density of the electromagnetic field curves spacetime. The traceless property has a striking consequence here — a universe filled with radiation has $T^\mu{}_\mu = 0$, which fixes the relation between its pressure and energy density to $p = \rho/3$, the equation of state of the radiation-dominated early universe. The bridge to the curved theory is **[[General Relativity I — Einstein's Equations and Schwarzschild]]**.
