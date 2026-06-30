---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
  - "Def - Classification of Four-Vectors"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \operatorname{diag}(+1,-1,-1,-1)$, so a timelike vector has $X\cdot X > 0$. A massive particle has a [[Def - Worldline of a Particle|timelike worldline]] parametrised by [[Def - Proper Time|proper time]] $\tau$, with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu = dX^\mu/d\tau = \gamma(1,\mathbf{u})$ normalised to $U\cdot U = 1$, where $\mathbf{u} = d\mathbf{x}/dt$ is the three-velocity in a frame, $u = |\mathbf{u}|$, and $\gamma = (1-u^2)^{-1/2}$. The rest mass is $m$, the four-momentum $P$ with components $P^\mu = (E,\mathbf{p})$; $E$ is the energy and $\mathbf{p}$ the relativistic three-momentum relative to the frame. This is a compound page: it defines two interlocking notions — the **four-momentum** and the **rest mass** — because the rest mass is the constant of proportionality between the four-momentum and the four-velocity, and neither is fully usable without the other. Full registry on [[Special Relativity XIII — Energy and Momentum]].

> [!warning] Convention
> Gourgoulhon treats the four-momentum as a *linear form* $\boldsymbol{p}$ and defines the mass through $\vec p\cdot\vec p = -m^2c^2$ in his mostly-plus signature (timelike means $\vec p\cdot\vec p \le 0$), with $\boldsymbol p = mc\,\underline{u}$. Translating to our mostly-minus signature and $c=1$: the four-momentum is the *vector* $P = mU$, and the mass condition becomes $P\cdot P = +m^2$ (timelike, positive). We treat $P$ as a vector throughout — the standard physics convention and Tong's $P = (E/c, \mathbf{p})$ — the metric duality between vector and form being immaterial once a metric is fixed.

---

# Axiom Motivation

The previous chapter built the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$ as the proper-time derivative of the four-position, a genuine four-vector encoding a particle's state of motion. But the four-velocity alone cannot be the carrier of dynamics, and seeing why is the whole motivation. The four-velocity is *normalised*: $U\cdot U = 1$ always, for every particle, regardless of its mass. A speck of dust and a planet moving side by side have *identical* four-velocities. So the four-velocity knows the direction of motion in spacetime but nothing about the particle's inertia — its resistance to being pushed, the thing that is conserved when particles collide. Dynamics needs a four-vector that distinguishes the dust from the planet.

The fix is to weight the four-velocity by the one number that measures inertia and is intrinsic to the particle: its **mass**. We want a quantity $m$ that is a property of the particle alone — the same to every observer, attached to the worldline, not to any frame — exactly as the four-velocity is. The natural such number is the mass measured in the particle's own rest frame, the **rest mass**, and because the rest frame is intrinsic to the particle this is automatically a Lorentz scalar. Multiplying the four-velocity by it gives $P := mU$, the **four-momentum**, a four-vector because $U$ is a four-vector and $m$ is a scalar. The dust now has small $P$ and the planet large $P$, and the difference is exactly the inertia that was missing.

Why *this* construction and not some nearby variant — why not $P = m^2 U$, or $P = m\,U/|U|$, or the four-velocity with a different power of $\gamma$? Three desiderata pin it down. First, $P$ must be *additive and conserved*: the total four-momentum of a system is to be the sum of the parts', and that sum is to be conserved in interactions (this is the content of the next chapter, but it is the design goal). Additivity demands that $P$ scale linearly with the amount of stuff, which forbids $m^2$. Second, $P$ must reduce to the Newtonian momentum $m\mathbf{u}$ in the low-speed limit, so that the new theory contains the old; expanding $P = mU = m\gamma(1,\mathbf{u})$ gives spatial part $m\gamma\mathbf{u} \to m\mathbf{u}$ as $u\to 0$, which is correct. Third, the *time component* must turn out to be the energy — and this is the deep test. Expanding the time component $P^0 = m\gamma = m + \tfrac12 mu^2 + \cdots$ produces, after the constant $m$, exactly the Newtonian kinetic energy $\tfrac12 mu^2$. A four-vector whose spatial part is the momentum and whose time part is the energy is precisely what is needed for "conservation of $P$" to encompass both conservation of momentum and conservation of energy. The construction $P = mU$ is the *unique* one meeting all three demands.

The single normalisation $U\cdot U = 1$ now hands over the deepest property of the four-momentum for free. Squaring $P = mU$ gives

$$P\cdot P = m^2\,(U\cdot U) = m^2.$$

This is the **mass-shell relation**, and it is the reason the rest mass is so well-named: it is the Minkowski *length* of the four-momentum, an invariant. The mass is not a separate input riding alongside $P$; it is recoverable from $P$ itself by taking the Minkowski norm. This is what makes mass frame-independent (a length is basis-independent) and, crucially, what makes mass *non-additive* — the length of a sum of four-vectors is not the sum of their lengths, a fact with enormous physical consequences (binding energy, the mass of a system of photons, the impossibility of certain reactions). Had one instead defined "mass" as $\gamma m$ (the old "relativistic mass"), it would have been frame-dependent and would have carried no information beyond the energy; the rest mass, the length of $P$, is the right invariant.

One should also see what would break with the naive alternative $P = m\,dX/dt$ (differentiating with respect to coordinate time). Coordinate time $t$ is a frame-dependent number, so $dX/dt$ is not a four-vector and $m\,dX/dt$ has no clean transformation law; its "mass-shell" would be frame-dependent, and a conservation law written with it would hold in one frame and fail in another. The factor of $\gamma = dt/d\tau$ that distinguishes $U = dX/d\tau$ from the naive $dX/dt$ is precisely what makes the four-momentum a genuine four-vector — and it is also exactly the factor that, applied to the spatial part, turns the Newtonian $m\mathbf{u}$ into the relativistic $\gamma m\mathbf{u}$ that diverges as $u\to c$ and thereby enforces the speed limit.

---

# The Definition

Let $\mathcal{P}$ be a particle of rest mass $m > 0$ travelling on a [[Def - Worldline of a Particle|timelike worldline]] with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$.

**Four-momentum.** The **four-momentum** of $\mathcal{P}$ is the four-vector
$$
P^\mu \;:=\; m\,U^\mu.
$$
In an inertial frame, using $U^\mu = \gamma(1,\mathbf{u})$,
$$
P^\mu \;=\; \big(\,\gamma m,\; \gamma m\,\mathbf{u}\,\big) \;=:\; (E, \mathbf{p}),
$$
so the time component is the **energy** $E = \gamma m$ and the spatial part is the **relativistic three-momentum** $\mathbf{p} = \gamma m\,\mathbf{u}$ (with $c$ restored: $P^\mu = (\gamma mc, \gamma m\mathbf{u})$, energy $E = \gamma mc^2$).

**Rest mass.** The **rest mass** (or **invariant mass**, or simply **mass**) $m$ is the Lorentz-invariant length of the four-momentum, defined equivalently by the **mass-shell relation**
$$
P\cdot P \;=\; m^2
\qquad\big(\text{with } c:\ P\cdot P = m^2c^2\big),
$$
which expands to the **energy–momentum relation** (the **dispersion relation**)
$$
E^2 \;=\; \mathbf{p}^2 + m^2
\qquad\big(\text{with } c:\ E^2 = \mathbf{p}^2c^2 + m^2c^4\big).
$$
For a *massive* particle $P$ is **timelike** and future-directed, $P\cdot P = m^2 > 0$; the locus of allowed four-momenta is one sheet of the hyperboloid $P\cdot P = m^2$, called the **mass shell**. Equivalently the four-momentum and four-velocity are collinear, $P = mU$, with $m = +\sqrt{P\cdot P}$.

The four-momentum and rest mass are **absolute** quantities — they depend only on the particle, not on any observer, on the same footing as the four-velocity. The energy $E$ and the three-momentum $\mathbf{p}$, by contrast, are *relative* to a chosen frame or [[Def - Observer and Local Rest Space|observer]] (see [[Thm - Energy and Momentum Relative to an Observer]]): they are the components of $P$ in that observer's frame.

---

# Categorical / Structural Definition

The four-momentum is best understood structurally as a point on a *coadjoint orbit* of the Poincaré group, but the elementary structural statement suffices here: the rest mass is the value of the **first Casimir invariant** of the Poincaré group on the particle's state. A Casimir invariant of a Lie group is a function on the representation space that commutes with the entire group action — it is constant on each irreducible representation and so labels the representation. For the Poincaré group (boosts, rotations, and spacetime translations together) the first Casimir is $P_\mu P^\mu$, and its value is $m^2$. This is the precise sense in which "mass is frame-independent": frame changes are elements of the Lorentz subgroup, the Casimir commutes with them, so $m^2$ is unchanged.

This places the four-momentum in a uniform hierarchy with the other conserved quantities of relativistic mechanics, each the conserved current of a symmetry of Minkowski space under **Noether's theorem**. Spacetime *translation* invariance gives the conserved four-momentum $P^\mu$ (the subject of this chapter); Lorentz *rotation/boost* invariance gives the conserved angular-momentum tensor $J^{\mu\nu}$ (the next chapter). The four-momentum is the Noether charge of translations, and its conservation in an isolated system is the statement that the laws are the same at every point of spacetime. In the Wigner classification an elementary particle simply *is* an irreducible unitary representation of the Poincaré group, labelled by exactly two Casimirs — this mass $m^2 = P_\mu P^\mu$, and a spin built from the Pauli–Lubanski vector — which is the group-theoretic reason a particle carries those and only those two intrinsic labels.

---

# Relate to Other Fields / Compression

In **Newtonian mechanics** the four-momentum is the unification of two separate objects: the momentum $\mathbf{p}$ and the energy $E$, which Newton kept apart with independent conservation laws, become the space and time parts of one four-vector. The non-relativistic limit recovers both — the spatial part $\gamma m\mathbf{u} \to m\mathbf{u}$ is the Newtonian momentum, and the time part $\gamma m \to m + \tfrac12 mu^2$ is the rest energy plus the Newtonian kinetic energy.

In **quantum mechanics** the four-momentum becomes the operator $P_\mu \to i\hbar\partial_\mu$, the covariant packaging of $E \to i\hbar\partial_t$ and $\mathbf{p}\to -i\hbar\nabla$; fed into the mass-shell $P\cdot P = m^2$ it produces the Klein–Gordon wave equation. The de Broglie relation $P^\mu = \hbar K^\mu$ identifies the four-momentum with the wave four-vector of the associated matter wave.

**True name:** the operational characterisation of the rest mass, distinct from "the mass in the rest frame", is **the Minkowski length of the four-momentum**, $m = \sqrt{P\cdot P}$. This is what you actually compute with: it is frame-independent, it is recovered from $P$ by squaring, and it makes immediately visible that mass is *not* additive (the length of a sum is not the sum of lengths). Whenever you need the mass of a particle or a system, the move is not to find a rest frame but to square the four-momentum.

---

# Examples / Corollaries

**Is an instance — an electron in flight.** An electron ($m_e = 511$ keV with $c=1$) moving at $\gamma = 2$ has four-momentum $P = (2 m_e, \sqrt{3}\,m_e\,\hat{\mathbf{u}})$, since $\mathbf{p} = \gamma m_e\mathbf{u}$ with $\gamma u = \sqrt{\gamma^2-1} = \sqrt{3}$. Its energy is $E = 2m_e = 1.022$ MeV, its momentum magnitude $|\mathbf{p}| = \sqrt{3}\,m_e$, and indeed $E^2 - \mathbf{p}^2 = 4m_e^2 - 3m_e^2 = m_e^2$, the mass-shell.

**Is an instance — a particle at rest.** A particle at rest has $\mathbf{u} = 0$, $\gamma = 1$, so $P = (m, \mathbf{0})$: all of its four-momentum is energy, $E = m$ (that is, $E = mc^2$), and it carries no three-momentum. The four-momentum points purely in the time direction, and $P\cdot P = m^2$ trivially. This is the apex of the mass-shell hyperboloid.

**Is NOT an instance — the coordinate momentum $m\,dX/dt$.** The naive object $m\,dX/dt = m(1,\mathbf{u})$ (no factor of $\gamma$) is *not* a four-momentum: it is not built by differentiating with respect to the invariant proper time, so it is not a four-vector, its components do not transform by the Lorentz matrix, and its "norm" $m^2(1 - u^2) = m^2/\gamma^2$ is frame-dependent rather than the invariant $m^2$. The missing factor of $\gamma = dt/d\tau$ is exactly what would make it a genuine four-momentum.

**Is NOT an instance — a tachyonic "four-momentum".** A four-vector $P$ with $P\cdot P < 0$ (spacelike) would describe a particle of imaginary rest mass, $m^2 < 0$ — a **tachyon**, travelling faster than light. No physical particle has such a four-momentum; the mass-shell of real particles is the timelike sheet $P\cdot P = m^2 \ge 0$. Spacelike four-momenta are excluded not as a definition but because they would permit superluminal signalling (and, in field theory, signal a vacuum instability rather than a real particle).

**Corollary — energy and momentum diverge at the speed limit.** As $u\to c$, $\gamma\to\infty$, so both $E = \gamma m$ and $|\mathbf{p}| = \gamma m u$ diverge. No finite four-momentum reaches the light cone from the timelike side, which is the four-momentum statement of the speed limit: it would take infinite energy to accelerate a massive particle to $c$.

**Corollary — the energy–momentum relation from one squaring.** Evaluating $P\cdot P$ in components, $P\cdot P = E^2 - \mathbf{p}^2$; setting this equal to the invariant $m^2$ gives $E^2 = \mathbf{p}^2 + m^2$ immediately, the relation connecting energy and momentum that every dispersion-relation calculation uses.

**Calibration check.** If you have understood the definition you should be able to, without looking anything up: (1) write the four-momentum of a particle of mass $m$ moving at speed $u$ along the $x$-axis, and verify its Minkowski square is $m^2$ regardless of $u$; (2) show that the time component reduces to $m + \tfrac12 mu^2$ for small $u$ and identify each term; (3) explain in one sentence why a system of two photons can have nonzero mass even though each photon has $P\cdot P = 0$ — because the mass is the length of the *sum* of the four-momenta, and two null vectors in different directions sum to a timelike one.

---

# Unlocked by This

> [!tip] Conservation of Four-Momentum *(from §13.2)*
> With the four-momentum in hand, the master law of relativistic dynamics is that the total four-momentum of an isolated system is conserved, $\sum P_{\text{in}} = \sum P_{\text{out}}$ — a single four-vector equation containing conservation of energy and momentum at once. See [[Thm - Conservation of Four-Momentum]].

> [!tip] The Mass Shell and Quantum Fields *(from Quantum Field Theory)*
> The mass-shell relation $P\cdot P = m^2$, under the substitution $P_\mu \to i\hbar\partial_\mu$, becomes the **Klein–Gordon equation** $(\Box + m^2)\phi = 0$ — the field equation of a free spin-0 particle. The hyperboloid $P\cdot P = m^2$ is the "mass shell" on which the on-shell momenta of physical particles live; off-shell momenta appear in internal lines of Feynman diagrams. The whole apparatus of relativistic quantum field theory is built on this one geometric relation.

> [!tip] Casimir Invariants and the Wigner Classification *(from Representation Theory)*
> The rest mass $m^2 = P_\mu P^\mu$ is the **first Casimir invariant** of the Poincaré group, and a particle is an irreducible unitary representation labelled by exactly two Casimirs: this mass, and a spin built from the Pauli–Lubanski vector. The classification splits sharply at $m = 0$: massive particles have little group $SO(3)$ and a $(2s+1)$-fold spin multiplet, while massless particles have little group $ISO(2)$ and just two helicity states. This is the deep content of [[Special Relativity XII — Inertial Observers and the Poincaré Group|Special Relativity XII]].
