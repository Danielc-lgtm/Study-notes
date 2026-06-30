---
type: definition
subject: special-relativity
prereqs:
  - "Thm - The Poincaré Group as a Lie Group"
  - "Def - The Poincaré Group"
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Lie Algebra of the Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$, so timelike means positive norm. The generators of the [[Def - The Poincaré Group|Poincaré]] Lie algebra are promoted to Hermitian operators on a Hilbert space: $P^\mu = (H, \boldsymbol{P})$ is the **four-momentum** (energy–momentum) operator, the generator of translations, and $J^{\mu\nu} = -J^{\nu\mu}$ is the **angular-momentum** tensor (the generator of Lorentz transformations), see [[Def - Angular Momentum Four-Tensor]]. Indices are raised and lowered with $\eta$. The totally antisymmetric Levi-Civita symbol is $\varepsilon^{\mu\nu\rho\sigma}$ with $\varepsilon^{0123} = +1$ (so $\varepsilon_{0123} = -1$ in this signature). The Pauli–Lubanski four-vector is $W^\mu$. The two Casimir labels are the rest mass $m \ge 0$ and the spin $s \in \{0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \ldots\}$. Full registry on [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

> [!warning] Convention
> The relation $W^2 = -m^2 s(s+1)$ is quoted here in the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$ used throughout this series. In the mostly-plus signature $\mathrm{diag}(-1,+1,+1,+1)$ common in the quantum-field-theory literature (and in Wigner's and Weinberg's conventions), the same physical statement reads $W^2 = +m^2 s(s+1)$ with $W^\mu W_\mu$ and $P^\mu P_\mu$ both carrying the opposite overall sign; the spin $s$ and mass $m$ are of course convention-independent. We keep mostly-minus, in which a massive particle's momentum $P$ is timelike with $P^2 = m^2 > 0$ and its Pauli–Lubanski vector $W$ is spacelike with $W^2 = -m^2 s(s+1) < 0$.

---

# Axiom Motivation

The Poincaré group is the symmetry group of every relativistic theory, and a quantum theory realises it as a unitary action on a Hilbert space of states. The decisive question — the one that turns this group from geometry into the foundation of particle physics — is: *how can the Poincaré group act on a Hilbert space irreducibly?* An irreducible action is one that does not split the Hilbert space into smaller invariant pieces; it is the indecomposable atom of relativistic quantum kinematics. The desideratum of this page is to find the *labels* that distinguish one irreducible action from another — the quantum numbers that say "this kind of particle, not that one" — in a way that is intrinsic to the group, independent of any choice of basis or frame.

The tool for labelling irreducible representations is the **Casimir operator**: an operator built from the generators that commutes with *every* generator of the group. By Schur's lemma, on an irreducible representation any operator commuting with the whole group action must be a scalar multiple of the identity — so each Casimir takes a single number as its value on each irreducible representation, and that number is a label. The motivating analogy is angular momentum: for the rotation group $\mathrm{SU}(2)$ there is one Casimir, $J^2 = J_x^2 + J_y^2 + J_z^2$, and its eigenvalue $j(j+1)$ labels the irreducible representations by spin $j$. The Poincaré group is larger and non-compact, and the question is how many Casimirs it has and what they label.

Why must one of them be $P^2 = P_\mu P^\mu$? The four-momentum operators $P^\mu$ generate translations and commute among themselves, $[P^\mu, P^\nu] = 0$, so any function of them is translation-invariant. The combination that is also *Lorentz*-invariant is the scalar $P^2 = P_\mu P^\mu$, contracted with the metric — it transforms as a Lorentz scalar because it is built by contracting the four-vector $P^\mu$ with itself. So $P^2$ commutes with translations (trivially) and with Lorentz transformations (being a scalar), hence with the whole group: it is a Casimir. Its value is the squared rest mass, $P^2 = m^2$, because on a one-particle state the four-momentum is the physical energy–momentum and $P\cdot P = E^2 - |\boldsymbol{P}|^2 = m^2$ is the relativistic mass-shell relation. This first Casimir labels representations by **mass**.

Why is mass not enough, and what is the second Casimir? Mass alone does not distinguish a spin-0 particle from a spin-1 particle of the same mass — both have $P^2 = m^2$ — so there must be a second label, the spin, and a second Casimir to carry it. The naive guess, "use the angular-momentum tensor $J^{\mu\nu}$", fails: the obvious scalar $J_{\mu\nu}J^{\mu\nu}$ is *not* a Casimir, because $J^{\mu\nu}$ does not commute with the translations $P^\rho$ — angular momentum is not translation-invariant (it depends on the choice of origin). The repair is the central construction of the page: combine $J^{\mu\nu}$ with $P^\sigma$ into a new four-vector that *is* translation-covariant, the **Pauli–Lubanski** vector
$$
W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma.
$$
Contracting the angular momentum against the momentum via the Levi-Civita symbol projects out exactly the *intrinsic* (spin) part of the angular momentum, discarding the origin-dependent orbital part. The miracle that makes this work is the identity $W \cdot P = 0$: the Pauli–Lubanski vector is always orthogonal to the momentum, by the antisymmetry of $\varepsilon$ against the symmetric pair $P_\mu P_\sigma$. This orthogonality is what guarantees $W^\mu$ measures only the spin: in the rest frame of a massive particle, where $P = (m, \mathbf{0})$, the constraint $W\cdot P = 0$ forces $W^0 = 0$, leaving $W^i = m J^i$, exactly $m$ times the spin three-vector. Then $W^2 = W_\mu W^\mu = -m^2(J^1{}^2 + J^2{}^2 + J^3{}^2) = -m^2\, s(s+1)$, with $s(s+1)$ the eigenvalue of the rest-frame $\mathrm{SU}(2)$ Casimir. This second Casimir labels representations by **spin**.

Why exactly two Casimirs, and not more or fewer? The rank of the Poincaré algebra and a counting of its invariant polynomials show there are precisely two independent Casimirs (for the connected group), $P^2$ and $W^2$. Two labels, $(m, s)$, completely specify an irreducible representation (together with discrete sign choices — the sign of energy, and for massless particles the sign of helicity). This is the precise sense in which mass and spin are not contingent attributes but the *complete intrinsic data* of an elementary particle: they are the two Casimir eigenvalues, the two numbers that name the irreducible representation. The whole apparatus — Casimirs, Pauli–Lubanski vector, the orthogonality $W\cdot P = 0$ — exists to extract those two numbers from the group in a frame-independent way.

---

# The Definition

The **Casimir invariants** of the Poincaré group are the two independent operators, built from the four-momentum $P^\mu$ and the angular-momentum tensor $J^{\mu\nu}$, that commute with every generator of the [[Def - The Poincaré Group|Poincaré]] Lie algebra:
$$
C_1 = P^2 = P_\mu P^\mu, \qquad C_2 = W^2 = W_\mu W^\mu,
$$
where the **Pauli–Lubanski four-vector** is
$$
W^\mu = -\tfrac{1}{2}\,\varepsilon^{\mu\nu\rho\sigma}\,J_{\nu\rho}\,P_\sigma.
$$
The Pauli–Lubanski vector satisfies the identities
$$
W \cdot P = W^\mu P_\mu = 0, \qquad [W^\mu, P^\nu] = 0, \qquad [J^{\mu\nu}, W^\rho] = i\big(\eta^{\nu\rho}W^\mu - \eta^{\mu\rho}W^\nu\big),
$$
the first expressing orthogonality to the momentum, the second translation-invariance, and the third that $W^\mu$ transforms as a Lorentz four-vector; together they make $W^2$ a Lorentz scalar commuting with all generators, hence Casimir.

On an irreducible unitary representation, by Schur's lemma, each Casimir is a scalar:
$$
C_1 = m^2 \quad(\text{the squared rest mass}), \qquad C_2 = -m^2\,s(s+1) \quad(\text{for } m > 0,\ \text{spin } s).
$$
The irreducible unitary representations of the (restricted) Poincaré group with non-negative energy are classified by the pair $(m, s)$ together with the choice of **little group**, the stabiliser of a standard momentum:

- **Massive, $m > 0$:** standard momentum $P = (m, \mathbf{0})$; little group $\mathrm{SO}(3)$ (rotations of the rest frame); representations labelled by spin $s \in \{0, \tfrac{1}{2}, 1, \ldots\}$, each of dimension $2s + 1$ (the polarisation states $s_z = -s, \ldots, +s$). Here $W^2 = -m^2 s(s+1)$.

- **Massless, $m = 0$:** standard momentum $P = (E, 0, 0, E)$; little group $\mathrm{ISO}(2)$ (the Euclidean group of the plane); $P^2 = 0$ and $W^2 = 0$ force $W^\mu = h\,P^\mu$ for a scalar **helicity** $h$; finite-dimensionality of the physical representation forces $h$ discrete, $h = \pm s$, giving exactly two states (e.g. the photon $h = \pm 1$, the graviton $h = \pm 2$).

The definition that organises all of relativistic quantum theory is: **an elementary particle is an irreducible unitary representation of the Poincaré group**, labelled by its two Casimir eigenvalues, mass $m$ and spin $s$.

---

# Relate to Other Fields / Compression

The Casimir story is the direct generalisation of the **angular-momentum Casimir** of ordinary quantum mechanics. For the rotation group $\mathrm{SU}(2)$ there is one Casimir $\boldsymbol{J}^2$ with eigenvalue $j(j+1)$, labelling representations by spin $j$ and dimension $2j+1$; the Poincaré spin Casimir $W^2 = -m^2 s(s+1)$ is exactly this, with $\boldsymbol{J}^2$ evaluated in the rest frame and scaled by $-m^2$, which is why a massive spin-$s$ particle has the same $2s+1$ states as a spin-$s$ angular-momentum multiplet — its little group *is* the rotation group of its rest frame.

**True name:** the Casimirs are *the complete frame-independent label of an irreducible Poincaré representation — the two numbers $(m, s)$ that say which particle*. Operationally, to identify a relativistic field or particle you compute $P^2$ (read off the mass) and $W^2$ (read off the spin), and the pair determines the representation up to discrete choices. This is more useful than any component-wise description because it is manifestly Lorentz- and translation-invariant: two observers in any relative motion, with any choice of origin, assign the *same* $(m, s)$, which is precisely what it means for these to be intrinsic properties of the particle rather than artifacts of a frame.

The deepest compression is the identification, due to Wigner, of "particle" with "irreducible unitary representation". A particle is not a localised lump; it is an indecomposable way the symmetries of spacetime act on a quantum state space. This dissolves several puzzles at once: it explains why every electron has identical mass and spin (they are all the same representation, not distinct objects that happen to match), why spin comes in the values $0, \tfrac{1}{2}, 1, \ldots$ (these are the allowed Casimir labels of the rest-frame $\mathrm{SU}(2)$), and why massless particles have only two polarisations regardless of spin (their little group is $\mathrm{ISO}(2)$, not $\mathrm{SO}(3)$). The free-field wave equations of quantum field theory — Klein–Gordon, Dirac, Maxwell, Proca — are nothing but the conditions that project the reducible space of fields onto a single irreducible $(m, s)$.

---

# Examples / Corollaries

**Is an instance — the scalar $(m, 0)$.** A spin-0 massive particle (the Higgs boson, a pion) has $P^2 = m^2$ and $W^\mu = 0$ (the spin three-vector vanishes), so $W^2 = 0 = -m^2\cdot 0\cdot 1$. Its representation is one-dimensional under the little group $\mathrm{SO}(3)$ — a single state, no polarisation. The field realising it obeys the Klein–Gordon equation $(\Box + m^2)\phi = 0$, which is precisely the operator statement $P^2 = m^2$ on a scalar field.

**Is an instance — the Dirac particle $(m, \tfrac{1}{2})$.** A spin-$\tfrac12$ massive particle (the electron) has $P^2 = m^2$ and $W^2 = -m^2\cdot\tfrac{1}{2}\cdot\tfrac{3}{2} = -\tfrac{3}{4}m^2$. Its little group $\mathrm{SO}(3)$ representation is two-dimensional, $2s+1 = 2$: spin up and spin down. The Dirac equation $(i\gamma^\mu\partial_\mu - m)\psi = 0$ is the first-order projector selecting this $(m, \tfrac{1}{2})$ from the reducible four-component field.

**Is an instance — the photon $(0, 1)$.** A massless spin-1 particle has $P^2 = 0$ and $W^2 = 0$, with $W^\mu = h P^\mu$ and helicity $h = \pm 1$. Crucially it has only *two* states, not three, because its little group is $\mathrm{ISO}(2)$ and the third would-be polarisation is removed (it is pure gauge). The source-free Maxwell equations realise this $(0,1)$ representation. This is the calibration example for the massive-versus-massless distinction: a *massive* spin-1 boson (the $W$ or $Z$, a Proca field $(m,1)$) has three polarisations, because *its* little group is $\mathrm{SO}(3)$.

**Is NOT an instance (excluded from physics) — a tachyonic representation.** A spacelike momentum, $P^2 = m^2 < 0$, gives a representation whose little group is $\mathrm{SO}(2,1)$ and which has no Lorentz-invariant notion of positive energy; such **tachyonic** representations are mathematically valid irreducibles of the Poincaré group but are excluded from physics because they would permit superluminal signalling and have no stable vacuum. The Casimir machinery describes them; physics discards them. This non-example marks the boundary between the representation theory and its physical sector.

**Is NOT an instance (excluded from physics) — a continuous-spin representation.** For a *massless* momentum, the non-compact little group $\mathrm{ISO}(2)$ also has infinite-dimensional representations in which its two "translation" generators act non-trivially, parametrised by a continuous real number (the "continuous spin" or "infinite spin"). These are genuine irreducibles with $P^2 = 0$, $W^2 = -\Xi^2 < 0$ for a continuous $\Xi$, but they describe a particle with infinitely many polarisations and are excluded from standard physics (no local field realises them with finitely many degrees of freedom). Demanding finite-dimensionality of the little-group representation is exactly what collapses the massless label to a single discrete helicity.

**Corollary — $W \cdot P = 0$ always.** From the antisymmetry of $\varepsilon^{\mu\nu\rho\sigma}$, $W^\mu P_\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu = 0$ because $P_\sigma P_\mu$ is symmetric in $(\sigma, \mu)$ while $\varepsilon$ is antisymmetric. Hence $W$ is spacelike for timelike $P$ (massive) and null-and-parallel for null $P$ (massless).

**Corollary — the number of polarisations.** A massive spin-$s$ particle has $2s+1$ states (the dimension of the spin-$s$ representation of $\mathrm{SO}(3)$); a massless particle of any spin $s \ge \tfrac12$ has exactly $2$ states (helicities $\pm s$). This single corollary explains the polarisation counts of all the fundamental fields.

**Calibration check.** If you have understood the definition you should be able to (i) compute $W^2$ for a spin-$s$ massive particle and get $-m^2 s(s+1)$; (ii) explain why $W^\mu$ rather than $J_{\mu\nu}J^{\mu\nu}$ is the spin Casimir, citing that $J^{\mu\nu}$ does not commute with $P^\rho$; and (iii) state why the photon has two polarisations while a massive vector boson has three, citing the little groups $\mathrm{ISO}(2)$ versus $\mathrm{SO}(3)$.

---

# Unlocked by This

> [!tip] An Elementary Particle Is a Representation of the Poincaré Group *(from QFT)*
> This is the conceptual summit of the special-relativity series, and the single most consequential idea this page seeds, so it is worth stating at length. Eugene Wigner proved in 1939 that the irreducible unitary representations of the Poincaré group are classified by the two Casimir eigenvalues — mass $m$ and spin $s$ — together with the choice of **little group**, the subgroup of Lorentz transformations fixing a standard momentum. The classification is exhaustive and constructive: every irreducible unitary representation with non-negative energy is *induced* from a finite-dimensional representation of the little group, by a procedure (the **Mackey machine** / method of induced representations) that builds the action on all momenta from the action on one. For a massive particle the little group is $\mathrm{SO}(3)$, the rotations of the rest frame, whose irreducible representations are the spin-$s$ multiplets of dimension $2s+1$; this is *why* a spin-$s$ particle has $2s+1$ polarisation states, and the formula $W^2 = -m^2 s(s+1)$ is the Poincaré-covariant statement of the rest-frame angular-momentum Casimir. For a massless particle the momentum is null, the little group is the non-compact $\mathrm{ISO}(2)$ — the Euclidean group of the plane, with one rotation and two "translations" — and demanding that the two non-compact generators act trivially (else a continuous, infinitely-degenerate spin) collapses the label to a single discrete **helicity** $\pm s$; this is *why* the photon ($s=1$) has only two polarisations $h = \pm 1$ rather than three, and the graviton ($s=2$) has $h = \pm 2$.
>
> The definition Wigner extracted is the one modern physics actually uses, and it should be stated without hedging: **an elementary particle is an irreducible unitary representation of the Poincaré group.** A "particle" is not a little ball with attributes; it is an indecomposable way the symmetries of spacetime can act on a quantum state space. Mass and spin are then not properties a particle *has* — they are the two labels that *name* the representation, the two Casimir eigenvalues, as intrinsic to the particle as the dimension is to a vector space. This reframes the entire ontology of quantum field theory. Every electron in the universe has identical mass and spin not because they are distinct objects that happen to coincide, but because they are literally the same representation $(m_e, \tfrac{1}{2})$ of the one spacetime symmetry group. When a field theorist writes down a free field they are realising a specific irreducible: the Klein–Gordon field is $(m, 0)$, the Dirac field $(m, \tfrac{1}{2})$, the Maxwell field $(0, 1)$, the Proca field $(m, 1)$, the linearised graviton $(0, 2)$. The free-field wave equations — Klein–Gordon, Dirac, Maxwell, Proca, Rarita–Schwinger — are nothing but the projection conditions that pick out a single irreducible $(m, s)$ from the reducible space of all fields, and the spin Casimir is what fixes the polarisation count that gauge invariance and the equivalence principle otherwise impose by hand.
>
> The classification also draws the boundary of the physically possible. The same machinery produces representations that physics must *exclude*: the **tachyonic** representations (spacelike $P$, $P^2 < 0$) with no Lorentz-invariant positive energy, and the **continuous-spin** representations (massless, with the $\mathrm{ISO}(2)$ translations acting non-trivially) with infinitely many polarisations. Seeing precisely *why* these are thrown out — they violate stability, locality, or finite degree-of-freedom counting — is seeing what makes a sensible particle, and it is the Casimir data that lets one state the exclusion sharply. Finally, the **Coleman–Mandula theorem** later shows that the largest symmetry group a non-trivial interacting relativistic theory can have is the Poincaré group times an internal symmetry group — the spacetime and internal symmetries cannot mix non-trivially — and the *only* loophole, discovered by relaxing the theorem's assumption to graded Lie algebras, is supersymmetry, whose **super-Poincaré** algebra extends the Poincaré algebra by fermionic generators $Q$ satisfying $\{Q, \bar{Q}\} \sim P$. Its irreducible representations, the supermultiplets, bundle particles of different spin (and equal mass) into a single representation, so that the Casimir structure is enlarged and a boson and a fermion become two states of *one* super-particle. All of this — the field equations, the polarisation counts, the exclusion of tachyons and continuous spin, the Coleman–Mandula boundary, and the supersymmetric loophole — is downstream of the two Casimirs defined on this page. The Poincaré group, studied as pure geometry in this chapter, turns out to *be* the classification of matter.

> [!tip] Spin and the Pauli–Lubanski Vector in Classical Mechanics *(from §14)*
> The Pauli–Lubanski construction has a classical counterpart: the [[Def - Spin Four-Vector|spin four-vector]] $S^\mu$ of a relativistic particle is, up to the factor $m$, the classical Pauli–Lubanski vector, satisfying the same orthogonality $S \cdot U = 0$ to the four-velocity. The classical spin precesses by the BMT equation in an electromagnetic field, and its magnitude $S \cdot S = -s^2$ (a constant of motion) is the classical shadow of the spin Casimir $W^2 = -m^2 s(s+1)$. See [[Def - Angular Momentum Four-Tensor]] and the spin four-vector.

> [!tip] The Mass as a Central Charge in the Galilean Limit *(from Non-Relativistic QM)*
> In the non-relativistic $c \to \infty$ contraction, the Poincaré group becomes the Galilean group, and the mass — a Casimir $P^2 = m^2$ here — migrates to become the *central charge* of the centrally-extended (Bargmann) Galilean algebra, $[K_i, P_j] = i m \delta_{ij}$. This is why non-relativistic wavefunctions of different mass cannot be superposed (Bargmann's superselection rule) while relativistic ones can: the mass is structurally different in the two theories, a Casimir relativistically and a central charge non-relativistically. Tracking this migration is one of the most illuminating windows on how relativistic and classical kinematics relate.
