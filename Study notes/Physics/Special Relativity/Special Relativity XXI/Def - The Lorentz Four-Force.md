---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Electromagnetic Field Tensor"
  - "Def - Four-Force"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

SI units, $c$ kept explicit. Signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, timelike $X\cdot X > 0$. A particle $\mathcal{P}$ has charge $q$, rest mass $m$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ ($U\cdot U = 1$) and [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$, parametrised by [[Def - Proper Time|proper time]] $\tau$. The [[Def - The Electromagnetic Field Tensor|electromagnetic field tensor]] is the antisymmetric 2-form $F$, with $F^\mu{}_\nu = \eta^{\mu\alpha}F_{\alpha\nu}$. To avoid a clash of symbols, the Lorentz **four-force** is written $f$ (lowercase), reserving $F$ for the field tensor. An inertial observer $\mathcal{O}$ has four-velocity $U_0$, rest space $\mathcal{E}_{U_0}$; relative to $\mathcal{O}$ the particle has velocity $\mathbf{V}$ (with $\mathbf{V}\cdot U_0 = 0$), Lorentz factor $\Gamma = U\cdot U_0$, electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$. The spatial cross product in the rest space $\mathcal{E}_{U_0}$ is $\times_{U_0}$, defined through the Levi-Civita tensor restricted to that space. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

---

# Axiom Motivation

The equation of motion of a charged particle needs a four-force, and the [[Def - Four-Force|four-force]] of a general interaction is just $f = dP/d\tau$, an empty bookkeeping statement until the *form* of $f$ is supplied for the interaction at hand. For electromagnetism the form is dictated by two requirements, and the Lorentz four-force is what they produce.

The first requirement is **linearity in the four-velocity**, already argued on the [[Def - The Electromagnetic Field Tensor|field-tensor page]]: the force must depend on a direction intrinsic to the particle, the only such direction is the four-velocity $U$, and the simplest dependence is linear. Linearity in $U$ means the force is a linear map applied to $U$, and a linear map from vectors to one-forms is a bilinear form $F$ — so $f_\alpha = qF_{\alpha\beta}U^\beta$, with the proportionality constant absorbing the particle's **charge** $q$. The motivation for *this* definition, rather than a nearby variant, is that any nonlinear dependence on $U$ would either spoil the superposition of fields (the field from two sources is the sum of the individual fields, which forces linearity in $F$, and consistency forces linearity in $U$ too) or introduce a second particle-specific constant beyond the charge, of which there is no experimental sign.

The second requirement is that the force be a **pure four-force**, $f\cdot U = 0$. This is the demand that the electromagnetic interaction *conserve the rest mass* of the particle — that it accelerate the particle and bend its worldline without converting it into a different particle or heating its internal structure. Recall the mass-evolution identity from the [[Def - Four-Force|four-force page]]: $f\cdot U = dm/d\tau$, so $f\cdot U = 0$ is exactly $dm/d\tau = 0$. Imposing this on $f = qF(\cdot,U)$ forces $F$ to be antisymmetric (a bilinear form vanishing on the diagonal), and antisymmetry then *guarantees* $f\cdot U = 0$ for free — the purity is built into the structure. Drop the purity axiom and the field could have a symmetric part, exerting a force component along $U$ that would steadily change the rest energy; that is the description of a different physics (a scalar Yukawa-type coupling), not of electromagnetism.

What is gained by writing the force this way rather than as the textbook $\mathbf{f} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$? Manifest Lorentz covariance. The textbook form is the projection of $f$ onto one observer's rest space; it is correct but frame-bound, and it hides the fact that the electric and magnetic contributions are two faces of one tensor. The covariant form $f = qF(\cdot,U)$ holds in every frame, makes the rest-mass conservation a one-line consequence of antisymmetry, and exhibits the velocity-dependence (the $\mathbf{V}\times\mathbf{B}$ piece) as nothing more than the contraction of the space-space block of $F$ with the spatial part of $U$. The motivation, in one sentence, is to write the Lorentz force so that its frame-independence and its rest-mass-conservation are visible rather than accidental.

---

# The Definition

Let $\mathcal{P}$ be a particle of charge $q$ and [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ in an [[Def - The Electromagnetic Field Tensor|electromagnetic field]] $F$. The **Lorentz four-force** on $\mathcal{P}$ is
$$
f \;=\; q\,F(\,\cdot\,,U), \qquad f_\alpha \;=\; q\,F_{\alpha\beta}\,U^\beta, \qquad f^\mu \;=\; q\,F^\mu{}_\nu\,U^\nu.
$$
It is a **pure four-force**: $f\cdot U = 0$, hence it conserves the rest mass ($dm/d\tau = 0$). The relativistic equation of motion of the charged particle is
$$
\frac{dP^\mu}{d\tau} \;=\; q\,F^\mu{}_\nu\,U^\nu, \qquad\text{equivalently}\qquad m\,\frac{dU^\mu}{d\tau} \;=\; q\,F^\mu{}_\nu\,U^\nu,
$$
the second form using $P = mU$ and the constancy of $m$.

**Relative to an inertial observer $\mathcal{O}$.** Decompose $F$ into the electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ relative to $\mathcal{O}$, and the particle's four-velocity as $U = \Gamma(U_0 + \mathbf{V})$ with $\Gamma = U\cdot U_0$ the Lorentz factor and $\mathbf{V}$ the velocity in the rest space. The four-force splits into a temporal and a spatial part:
$$
\frac{d\mathfrak{E}}{dt} \;=\; q\,\mathbf{E}\cdot\mathbf{V}, \qquad\qquad \boldsymbol{\mathfrak{F}} \;=\; q\big(\mathbf{E} + \mathbf{V}\times_{U_0}\mathbf{B}\big),
$$
where $\mathfrak{E} = \Gamma m c^2$ is the particle's energy measured by $\mathcal{O}$, $t$ is $\mathcal{O}$'s proper time, and $\boldsymbol{\mathfrak{F}} = d\mathbf{p}/dt$ is the spatial **Lorentz force** (rate of change of relative three-momentum $\mathbf{p} = \Gamma m\mathbf{V}$). The temporal equation says the **magnetic field does no work**: only the electric field changes the particle's energy, and at the rate $q\,\mathbf{E}\cdot\mathbf{V}$. The spatial equation is the elementary Lorentz-force law, recovered as a frame-dependent projection of the covariant statement.

---

# Categorical / Structural Definition

The Lorentz four-force is the value of the bundle morphism $U \mapsto qF(\cdot,U)$, a fibrewise linear map $T\mathbb{M}\to T^*\mathbb{M}$ scaled by the charge. Raising an index, $f^\mu = qF^\mu{}_\nu U^\nu$ exhibits $qF^\mu{}_\nu$ as a (pointwise) element of the Lorentz Lie algebra $\mathfrak{so}(1,3)$ acting on the four-velocity: the electromagnetic field generates, at each instant, an *infinitesimal Lorentz transformation* of the particle's four-velocity. This is the structural reason the equation of motion $dU/d\tau = (q/m)F(\cdot,U)$ in a uniform field integrates to $U(\tau) = \exp\!\big((q/m)\tau\,\check F\big)U(0)$ with $\check F = F^\mu{}_\nu$ the field viewed as a Lie-algebra element — a one-parameter subgroup of $SO(1,3)$ acting on $U$. The electric part of $\check F$ is a boost generator, the magnetic part a rotation generator; hence pure-electric fields produce hyperbolic (boost) motion and pure-magnetic fields produce circular (rotation) motion, the two cases of [[Thm - Motion of a Charge in a Uniform Field]].

---

# Relate to Other Fields / Compression

In the **Lagrangian formulation** the Lorentz force is not postulated but derived: the action of a charged particle is $S = -mc\!\int d\tau + q\!\int A_\mu\,dx^\mu$, where $A$ is the [[Def - The Four-Potential|four-potential]] one-form, and varying it gives the Euler–Lagrange equation $m\,dU_\mu/d\tau = q(\partial_\mu A_\nu - \partial_\nu A_\mu)U^\nu = qF_{\mu\nu}U^\nu$, exactly the Lorentz four-force with $F = dA$. The vault's [[Def - Lagrangian for a Particle in a Vector Field|Lagrangian for a particle in a vector field]] (SR XV) sets this up; the Lorentz force is the canonical example of a force derived from a velocity-coupling $q\langle A,U\rangle$.

**True name:** the operationally useful form is *charge times field-matrix times four-velocity*, $f^\mu = qF^\mu{}_\nu U^\nu$ — a matrix–vector product. When you need the equation of motion, write $m\dot U^\mu = qF^\mu{}_\nu U^\nu$ and read $F^\mu{}_\nu$ off the field's blocks; when you need the elementary three-force, project onto the observer and get $q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$. The single most reusable consequence is *the magnetic field never changes a particle's energy* — power is $q\mathbf{E}\cdot\mathbf{V}$, with no $\mathbf{B}$ — which is the engine of every accelerator argument and is why cyclotrons accelerate only through the electric gaps, never in the magnetic dees.

This is the relativistic completion of the **Newtonian Lorentz force** $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$: the spatial part of $f$ reduces to it in the non-relativistic limit (where $\Gamma\to1$, $\mathbf{p}\to m\mathbf{v}$), while the temporal part $q\mathbf{E}\cdot\mathbf{V}$ is the work-energy theorem made into the fourth component of a four-vector equation. The four-force unifies "force changes momentum" and "power changes energy" into the single statement $dP/d\tau = qF(\cdot,U)$.

---

# Examples / Corollaries

**Is an instance — a charge in a pure electric field.** With $\mathbf{B}=0$, $\boldsymbol{\mathfrak{F}} = q\mathbf{E}$ and $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$: the particle accelerates along $\mathbf{E}$ and gains energy. Starting from rest in a uniform $\mathbf{E}$, the motion is hyperbolic (uniformly accelerated), with proper acceleration $a = qE/(mc^2)\cdot c^2 = qE/m$ in the rest frame.

**Is an instance — a charge in a pure magnetic field.** With $\mathbf{E}=0$, $\boldsymbol{\mathfrak{F}} = q\mathbf{V}\times\mathbf{B}$ and $d\mathfrak{E}/dt = 0$: the speed (and energy, and $\Gamma$) is constant, and the force is centripetal, producing circular or helical motion at the cyclotron frequency $\omega_B = qB/m$. The magnetic field bends the trajectory but does no work — see [[Thm - Motion of a Charge in a Uniform Field]].

**Is NOT an instance — a force along the four-velocity.** A four-force $f\propto U$ (for instance a hypothetical drag $f = -kU$) is *not* a Lorentz force: it has $f\cdot U = -kU\cdot U = -k\ne0$, so it changes the rest mass. No antisymmetric $F$ can produce such a force; the Lorentz force is always perpendicular to $U$.

**Is NOT an instance — the gravitational "force" in general relativity.** Gravity is not a four-force at all in general relativity; a freely-falling particle has $dU/d\tau$ equal to the *covariant* derivative being zero (a geodesic), not a Lorentz-type force term. The Lorentz force is a genuine non-gravitational interaction, deflecting worldlines away from geodesics.

**Corollary — rest mass is conserved.** Contracting the equation of motion with $U_\mu$: $U_\mu\,dP^\mu/d\tau = qF_{\mu\nu}U^\mu U^\nu = 0$ by antisymmetry, and the left side is $\tfrac12\,d(P\cdot U)/d\tau\cdot$-type bookkeeping giving $m\,dm/d\tau\cdot c^2 = 0$ (more directly, $\tfrac{d}{d\tau}(P\cdot P) = 2P\cdot f = 2mU\cdot f = 0$). So $m$ is constant: a charged particle in any electromagnetic field keeps its rest mass.

**Corollary — the work-energy theorem.** The temporal component, $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$, integrated over a path, gives the kinetic energy gained as $q\!\int\mathbf{E}\cdot d\mathbf{x}$ — for a uniform field along the displacement, $\Delta\mathfrak{E}_{\mathrm{kin}} = qE\,z = q\Delta V$ (with $\Delta V$ the potential difference), the basic relation behind a linear accelerator.

**Calibration check.** You have understood the definition if you can (i) show $f\cdot U = 0$ from antisymmetry alone, in one line; (ii) project $f = qF(\cdot,U)$ onto an inertial observer and recover both $\boldsymbol{\mathfrak{F}} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ and $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$; (iii) explain why a magnetic field cannot change a charged particle's energy, by reading the temporal component.

---

# Unlocked by This

> [!tip] The Equation of Motion and Accelerator Physics *(from §21.3)*
> The covariant equation $m\dot U^\mu = qF^\mu{}_\nu U^\nu$ is integrated for uniform fields in [[Thm - Motion of a Charge in a Uniform Field]], yielding the cyclotron orbit, hyperbolic motion, and the crossed-field trochoid; the fact that only $\mathbf{E}$ does work ($d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$) is the design principle of every particle accelerator.

> [!tip] The BMT Equation and Spin Precession *(from §14.3 and Accelerator Physics)*
> A particle with spin in an electromagnetic field obeys the **Bargmann–Michel–Telegdi equation**, the spin analogue of the Lorentz four-force: the spin four-vector $S$ precesses according to $dS^\mu/d\tau = \frac{gq}{2m}\big(F^\mu{}_\nu S^\nu + \ldots\big)$, with the anomalous magnetic moment governing the difference between spin and momentum precession rates. This is the basis of muon $g-2$ measurements; see [[Def - Spin Four-Vector]].

> [!tip] Maxwell's Equations from the Action *(from Electromagnetism)*
> The same coupling $q\langle A,U\rangle$ that produces the Lorentz force, when promoted to a field action $-\frac{1}{4\mu_0}\!\int F_{\mu\nu}F^{\mu\nu}\,d^4x + \int A_\mu J^\mu\,d^4x$, yields **Maxwell's equations** $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ on varying $A$; the Lorentz force and the field equations come from one action principle. See [[Special Relativity XXII — Maxwell's Equations]].
