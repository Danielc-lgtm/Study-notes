---
type: definition
subject: special-relativity
prereqs:
  - "Def - Nordström's Scalar Theory of Gravity"
  - "Def - The Energy-Momentum Tensor"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$. $G$ is Newton's constant; $\varepsilon_0$ the electric permittivity of vacuum; $\vec E$, $\vec B$ here denote the *gravitational* analogues of the electric and magnetic field vectors in the vector theory. $T^{\mu\nu}$ is the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]], $T = T^\mu{}_\mu$ its trace. $h_{\mu\nu}$ is a symmetric type-$(0,2)$ tensor field on Minkowski space — the gravitational tensor potential. $\Phi$ is the gravitational scalar potential of [[Def - Nordström's Scalar Theory of Gravity|Nordström's theory]]; $m$ the mass of a radiating particle, $\Gamma$ its Lorentz factor, $\vec V$ its velocity and $\vec\gamma_{\!a}$ its acceleration relative to an inertial observer. $g^\ast = \eta + h$ is the physical metric of the tensor theory. Full registry on [[Special Relativity XXV — Toward Relativistic Gravitation]].

> [!warning] Convention: gravitational "electromagnetism" signs
> The vector theory is obtained from Maxwell's theory by the substitution $\varepsilon_0 \leftrightarrow -1/(4\pi G)$, which makes like masses attract (where like charges repel). It is this *single sign change* that makes the field energy density negative; the rest of the formalism is electromagnetism transcribed. Signs are translated from Gourgoulhon's mostly-plus convention as elsewhere.

This is a compound page: it defines two distinct failed theories — the **vector theory** (spin-1) and the **tensor theory** (spin-2) — because they are the two remaining candidates after the scalar theory, presented together as the completion of the search for gravity-as-a-field-on-Minkowski-space, and the tensor case is what motivates leaving that framework for general relativity.

---

# Axiom Motivation

After the scalar theory of [[Def - Nordström's Scalar Theory of Gravity|Nordström]] fails observationally, the natural question is whether a more complicated field does better. A relativistic field is classified by the [[Def - The Lorentz Group|Lorentz]] representation it carries — its spin — and the next two options are spin-1 (a vector field, like the electromagnetic potential) and spin-2 (a symmetric rank-2 tensor field). The motivation for each is an analogy, and the lesson of the chapter is that each analogy *fails in a specific, diagnostic way* that reveals gravity's true nature.

The vector theory is motivated by the spectacular success of electromagnetism, the prototype relativistic vector theory ([[Special Relativity XXI — The Electromagnetic Field|XXI]], [[Special Relativity XXII — Maxwell's Equations|XXII]]). Gravity, like electromagnetism, is long-range and falls off as $1/r^2$, so why not give it a vector potential $A^\mu$, a field tensor, and Maxwell-like equations? There is exactly one structural difference to accommodate: two identical charges *repel*, but two identical masses *attract*. In the electromagnetic action this attraction-versus-repulsion is encoded in the sign of the coupling constant, so to flip repulsion to attraction one performs the substitution $\varepsilon_0 \leftrightarrow -1/(4\pi G)$. The motivation is that this single change should convert the most successful field theory known into a theory of gravity. The axiom under test is therefore: *gravity is a vector field differing from electromagnetism only by the sign that makes like sources attract.* What breaks it is that the sign change is not cosmetic — it flips the sign of the field's energy.

The tensor theory is motivated by a deeper structural observation about what gravity couples to. The source of gravity is mass-energy, and mass-energy is not a scalar (which killed naive energy-as-source) and not a vector (a current), but a **rank-2 symmetric tensor**, the energy-momentum tensor $T^{\mu\nu}$. A field that couples naturally to a rank-2 tensor source must itself be a rank-2 tensor, contracted with the source: $\mathscr{L}_{\mathrm{inter}} = \tfrac{1}{2c}h_{\mu\nu}T^{\mu\nu}$. So the motivation is a matching of ranks: tensor source demands tensor field. The free field is then the unique consistent kinetic term for a massless symmetric tensor, the **Fierz-Pauli** Lagrangian (a massless spin-2 field). The axiom under test is: *gravity is a symmetric rank-2 tensor field $h_{\mu\nu}$ coupled to the energy-momentum tensor.* What breaks the lowest-order version is that the matter does not feel the field back; what fixes it turns the theory into general relativity.

It is worth being precise about *why* each spin fails, because the pattern is the content. A spin-0 field couples only to the scalar trace $T$, so it misses the bending of light (traceless radiation) — too little coupling. A spin-1 field couples to a vector current, and the antisymmetry that makes the electromagnetic field tensor produces, after the attractive sign flip, a Hamiltonian unbounded below — negative energy. A spin-2 field couples to the full tensor $T^{\mu\nu}$, which is the *right* coupling, but a *linear* spin-2 theory has a hidden gauge symmetry forcing $\partial_\mu T^{\mu\nu} = 0$ as an identity, which means the field exerts no net force on its sources — until one adds the nonlinear self-coupling that makes the field gravitate too, at which point the theory is general relativity. The three spins fail at three different points on the spectrum from "couples too weakly" to "couples correctly but only nonlinearly", and the survivor is spin-2 made nonlinear.

If one weakened the vector theory's defining sign — kept $+\varepsilon_0$, i.e. repulsion — one would have electromagnetism, with positive energy but the wrong force law (like masses would repel). There is no middle ground: the sign that gives attraction gives negative energy. If one truncated the tensor theory at linear order, one would have a consistent but empty theory (matter unmoved); the nonlinear completion is forced by demanding that the field's own energy gravitate. Each failure is rigid.

---

# The Definition

## The vector theory of gravity

The **vector theory** describes gravity by a four-vector potential on Minkowski spacetime, with dynamics obtained from electromagnetism ([[Special Relativity XXII — Maxwell's Equations|Maxwell's equations]]) by the substitution
$$
\varepsilon_0 \;\longleftrightarrow\; -\frac{1}{4\pi G},
$$
which flips the force between like sources from repulsive to attractive. The first component of the resulting field equation reduces to Poisson's equation $\Delta\Phi = 4\pi G\rho$ for a slowly-varying field. The theory's **field energy density**, obtained from the electromagnetic energy density by the same substitution, is
$$
\rho_{\mathrm{grav}} = -\frac{1}{8\pi G}\big(\vec E\cdot\vec E + c^2\,\vec B\cdot\vec B\big) \;<\; 0,
$$
where $\vec E$ and $\vec B$ are the gravitational "electric" and "magnetic" field vectors. **The energy density is negative**, which is the fatal defect. Equivalently, for a mass $m$ oscillating along an axis with acceleration $\vec\gamma_{\!a}$ collinear with its velocity $\vec V$ relative to an inertial observer $\mathcal{O}$, the radiated energy-flux vector ("gravitational Poynting vector") is
$$
\vec\varphi = -\frac{G m^2\,\Gamma^2\sin^2\theta}{4\pi c^3 r^2\big(1 - \tfrac{V}{c}\cos\theta\big)^6}\;\vec n,
$$
with $\vec n$ the unit vector from the particle's retarded position to the observation point. Because $\vec\varphi$ is *anti*parallel to $\vec n$, energy flows *toward* the particle: the system gains energy during oscillation, an instability. **The vector theory is not viable even theoretically.**

## The tensor theory of gravity

The **tensor theory** describes gravity by a symmetric type-$(0,2)$ tensor field $h_{\mu\nu}$ on Minkowski spacetime, coupled to matter through the interaction Lagrangian
$$
\mathscr{L}_{\mathrm{inter}} = \frac{1}{2c}\,h_{\mu\nu}\,T^{\mu\nu},
$$
where $T^{\mu\nu}$ is the total energy-momentum tensor of matter and non-gravitational fields (this implements the principle of universal coupling). The free-field Lagrangian $\mathscr{L}_{\mathrm{field}}$ is the **Fierz-Pauli** Lagrangian of a massless spin-2 field. The lowest-order theory is inconsistent as a theory of gravity: the matter energy-momentum tensor obeys $\vec\nabla\cdot T = 0$ by itself, so the density of gravitational four-force vanishes and **matter does not feel gravity**. To make matter respond, terms of order higher than $\mathscr{L}_{\mathrm{inter}}$ must be added to $\mathscr{L}_{\mathrm{field}}$ — the field must couple to its own energy-momentum. The resulting theory is **equivalent to general relativity**: the background Minkowski metric $\eta$ loses any physical meaning, and the physical metric is
$$
g^\ast = \eta + h.
$$
It is then simpler to work in the framework of general relativity directly than as a tensor field theory on a background.

---

# Categorical / Structural Definition

The two theories occupy fixed slots in the **spin classification** of relativistic fields. A massless field of spin $s$ on Minkowski space is an irreducible representation of the Poincaré group ([[Special Relativity XII — Inertial Observers and the Poincaré Group|XII]]) labelled by helicity $\pm s$; the candidate gravity theories are spin-0 (scalar, [[Def - Nordström's Scalar Theory of Gravity|Nordström]]), spin-1 (vector, this page), spin-2 (tensor, this page). The structural principle is **rank-matching of source and field**: a field couples to a current of the same tensor rank, so a scalar couples to a scalar (the trace $T$), a vector to a vector (a current $J^\mu$), and a symmetric tensor to a symmetric tensor (the stress tensor $T^{\mu\nu}$). Since the true source of gravity is the rank-2 symmetric energy-momentum tensor, only the spin-2 field has the right rank to couple to all of it — which is the structural reason gravity is spin-2.

The deeper structural fact distinguishing spin-1 from spin-2 is the sign of the energy carried by the field, which is fixed by the representation. For a spin-1 field the kinetic term has the form $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$, whose energy is positive *only* with the electromagnetic sign of the coupling (like charges repel); the attractive sign needed for gravity flips it negative. For a spin-2 field the kinetic term (Fierz-Pauli) has positive energy with the attractive sign — which is the structural statement that *attractive* long-range forces must be mediated by *even*-spin fields (spin-0 or spin-2), while *odd*-spin fields (spin-1) mediate forces that repel between like sources. This even/odd-spin attraction/repulsion rule is a general theorem of field theory, and it is the abstract reason the vector theory cannot describe an attractive gravity with positive energy.

---

# Relate to Other Fields / Compression

The vector theory is **gravitomagnetism** done wrong: the correct weak-field limit of general relativity *does* contain a "gravitomagnetic" sector formally resembling magnetism (frame-dragging, the Lense-Thirring effect), but it sits inside the spin-2 tensor theory, not a stand-alone spin-1 theory. The lesson is that the electromagnetic *analogy* survives in general relativity as a sub-structure of the tensor field, while the electromagnetic *template* — gravity as a primary vector field — does not.

**True name:** the vector theory's true name is *"the proof that gravity is not spin-1"*, and the tensor theory's is *"general relativity, linearised, on a background you are meant to forget"*. The vector theory exists only to be rejected, and its rejection (negative energy) is the cleanest argument that the mediator of gravity has even spin. The tensor theory is genuinely general relativity in a particular gauge and coordinate system — the weak-field expansion $g = \eta + h$ — and its only defect is conceptual: it pretends the flat background $\eta$ is physical when it is not.

The tensor theory is the natural home of **gravitational waves**. The Fierz-Pauli equation is a wave equation for $h_{\mu\nu}$, and its solutions — transverse, traceless, two-polarisation ripples propagating at $c$ — are exactly the gravitational waves detected by LIGO, computed in the linearised ($g = \eta + h$) approximation. So although the tensor theory fails as a *complete* theory, its linear part is quantitatively correct and is the framework in which gravitational radiation is actually calculated. This is the precise sense in which "general relativity in the weak field is special relativity plus a tensor field".

---

# Examples / Corollaries

**Is an instance (of failure) — the radiating oscillator in the vector theory.** A mass oscillating along a line radiates, by analogy with an oscillating charge. Computing its gravitational Poynting vector with the substitution $\varepsilon_0 \to -1/(4\pi G)$ gives $\vec\varphi \propto -\vec n$, pointing *toward* the mass. Energy flows inward; the oscillation is amplified; the theory is unstable. This is the concrete manifestation of the negative field energy.

**Is an instance — gravitational waves from the linearised tensor theory.** Solving the Fierz-Pauli equation for a time-varying mass distribution yields outgoing transverse-traceless waves, the quadrupole radiation of general relativity. A binary star system loses energy to these waves at the rate given by the quadrupole formula, matching the observed orbital decay of the Hulse-Taylor pulsar. The linear tensor theory gets this right because it *is* linearised general relativity.

**Is NOT an instance — a self-consistent linear tensor theory.** One might hope the linear theory $\mathscr{L}_{\mathrm{field}}^{\mathrm{Fierz-Pauli}} + \tfrac{1}{2c}h_{\mu\nu}T^{\mu\nu}$ is a complete theory of gravity. It is not: the field equations force $\partial_\mu T^{\mu\nu} = 0$ as a consistency condition, which says the matter moves as if *no* gravity acted on it. The field is sourced by matter but exerts no back-reaction — a half-theory. The only repair (adding the field's own stress to the source, order by order) sums to general relativity.

**Is NOT an instance — the vector theory with the electromagnetic sign.** Keeping $+\varepsilon_0$ (no sign flip) gives a theory with positive energy and stable radiation — but it is just electromagnetism relabelled, and it makes like masses *repel*. It is a perfectly good theory of a repulsive long-range vector force; it is not gravity. There is no choice of sign that is simultaneously attractive and positive-energy for a vector field.

**Corollary — even spin for attraction, odd spin for repulsion.** Collecting the two failures with Nordström's: scalar (spin-0, even) gives attraction; vector (spin-1, odd) gives repulsion between like sources when energy is positive; tensor (spin-2, even) gives attraction with positive energy. The pattern — even-spin mediators produce attraction between like charges, odd-spin produce repulsion — is the calibration that explains why both viable gravity candidates (Nordström's spin-0 and Einstein's spin-2) are even-spin, and why electromagnetism (spin-1) repels like charges.

**Calibration check.** The reader should be able to verify: (i) that the substitution $\varepsilon_0 \to -1/(4\pi G)$ flips the sign of the electromagnetic energy density to give $\rho_{\mathrm{grav}} < 0$; (ii) that the interaction $\tfrac{1}{2c}h_{\mu\nu}T^{\mu\nu}$ couples the tensor field to the *full* stress tensor, not just its trace (contrast Nordström); and (iii) that the linear tensor theory's consistency condition $\partial_\mu T^{\mu\nu} = 0$ is exactly the statement that matter ignores the field.

---

# Unlocked by This

> [!tip] Gravitational Waves and Their Detection *(from General Relativity and Astrophysics)*
> The Fierz-Pauli (linearised tensor) theory is the exact framework in which **gravitational waves** are computed: transverse-traceless ripples of $h_{\mu\nu}$ propagating at $c$ with two polarisations, sourced by the time-varying mass quadrupole. The waves detected by LIGO and Virgo from merging black holes and neutron stars are solutions of precisely this equation in the $g = \eta + h$ approximation. The spin-2 nature of the field is directly observable: gravitational waves have helicity $\pm 2$, manifest as the cross and plus polarisation patterns. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] General Relativity as the Nonlinear Completion of Spin-2 *(from General Relativity)*
> The most profound thing this page unlocks is that **general relativity is forced**: starting from a massless spin-2 field on flat space and demanding only self-consistency (the field must couple to its own energy-momentum), the infinite series of self-coupling corrections sums uniquely to the Einstein-Hilbert action. This is the Deser argument, and it shows general relativity is not an arbitrary geometric postulate but the *unique* consistent theory of an interacting massless spin-2 field. The flat background $\eta$ disappears into the physical metric $g^\ast = \eta + h$, and one has arrived at [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]] without ever invoking geometry — geometry emerges as the only way to make spin-2 consistent.
