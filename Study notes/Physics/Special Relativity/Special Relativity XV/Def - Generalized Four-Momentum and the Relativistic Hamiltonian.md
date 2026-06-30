---
type: definition
subject: special-relativity
prereqs:
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Lagrangian for a Particle in a Vector Field"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Legendre Transform"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, timelike $\eta_{\mu\nu}\dot x^\mu\dot x^\nu > 0$ (Gourgoulhon: mostly-plus, opposite sign throughout, with $P\cdot P = -m^2c^2$ where we have $+m^2c^2$). A particle has worldline $x^\mu(\lambda)$, parameter-velocity $\dot x^\mu$, four-velocity $U$ ($u_\mu = \eta_{\mu\nu}U^\nu$, $U\cdot U = 1$). The Lagrangian is $L(x^\mu, \dot x^\mu)$ and the action $S = \int L\,d\lambda$. For a charged particle, $q$ is the charge and $A_\mu$ the potential one-form (see [[Def - Lagrangian for a Particle in a Vector Field]]). Relative to an inertial observer we use the three-velocity $\mathbf{v}$, three-momentum $\mathbf{p}$, $\gamma = (1-\mathbf{v}^2)^{-1/2}$, scalar potential $\phi = A_0$, and vector potential $\mathbf{A}$. The Hamiltonian is $H$ and phase space $\mathsf{P}$. This is a **compound page**: it defines two interlocking notions — the generalized four-momentum and the relativistic Hamiltonian — because the second is the Legendre transform of the Lagrangian with respect to the first, and neither is fully usable without the other. Full registry on [[Special Relativity XV — The Principle of Least Action]].

---

# Axiom Motivation

Analytical mechanics has two pillars beyond the Lagrangian: the **conjugate momentum** $p = \partial L/\partial\dot q$, which is the conserved quantity of a cyclic coordinate and the variable that pairs with position in phase space, and the **Hamiltonian** $H = p\dot q - L$, the Legendre transform that re-expresses the dynamics on phase space and serves as the launching point for quantisation. The goal here is to construct both for a relativistic particle. The construction of the momentum is straightforward; the construction of the Hamiltonian runs into a characteristic relativistic obstruction that is itself instructive.

The generalized four-momentum is defined exactly as in non-relativistic mechanics: $p_\mu = \partial L/\partial\dot x^\mu$, the derivative of the Lagrangian with respect to the parameter-velocity. The motivation for *this* definition rather than some other is that it is the object Noether's theorem produces: the conserved charge of a symmetry is $p_\mu G^\mu$, and the conserved charge of a translation (a cyclic coordinate) is $p_\mu$ itself — so $p_\mu = \partial L/\partial\dot x^\mu$ is forced to be *the* momentum if conservation laws are to come out right. A subtlety peculiar to the relativistic case must be checked: because $\lambda$ is an arbitrary parameter, one might worry that $p_\mu$ depends on the choice of $\lambda$. It does not, and the reason is the degree-one homogeneity of $L$: the derivative $\partial L/\partial\dot x^\mu$ of a degree-one homogeneous function is degree *zero* homogeneous, hence invariant under rescaling $\dot x^\mu \mapsto \mu\dot x^\mu$, hence independent of the parametrisation. So the generalized four-momentum is a genuine geometric object along the worldline, a linear form, not an artefact of the parameter.

The Hamiltonian is where relativity bites. The naive definition $H = p_\mu\dot x^\mu - L$, copied from non-relativistic mechanics, *fails twice*, and both failures trace to the same source — the homogeneity of $L$. First, by Euler's identity $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$, the naive Hamiltonian is $H = \dot x^\mu\,\partial L/\partial\dot x^\mu - L = L - L = 0$ identically: a Hamiltonian that vanishes carries no dynamics. Second, the Legendre transform requires inverting the relation $p_\mu = \partial L/\partial\dot x^\mu$ to solve for $\dot x^\mu$ in terms of $p_\mu$, and this inversion is impossible because the Jacobian $\partial p_\mu/\partial\dot x^\nu = \partial^2 L/\partial\dot x^\mu\partial\dot x^\nu$ has $\dot x^\mu$ in its kernel (differentiate Euler's identity), so the map $\dot x \mapsto p$ is not invertible. Both failures say the same thing: the four functions $x^\mu(\lambda)$ carry only three physical degrees of freedom (the fourth being the parametrisation freedom), so the four momenta cannot be independent — they obey a **primary constraint**.

What is that constraint? For a free particle, $P = mU$ with $U\cdot U = 1$, so $P\cdot P = m^2$ (Gourgoulhon's $-m^2c^2$ in mostly-plus): the momenta lie on the **mass shell**, a three-dimensional surface in the four-dimensional momentum space. For a charged particle the kinetic momentum $P - qA$ lies on the mass shell, $(P - qA)\cdot(P - qA) = m^2$. The constraint *is* the relation the four momenta satisfy, and it is the geometric fact behind both failures of the naive Hamiltonian.

The resolution, due to Dirac, is to take a Hamiltonian *proportional to the constraint*. The function $H = \tfrac{1}{2m}\eta^{\mu\nu}(p_\mu - qA_\mu)(p_\nu - qA_\nu)$ is constant on the physical motion (its value is $\tfrac{1}{2m}\cdot m^2 = \tfrac{m}{2}$, or $-\tfrac12 mc^2$ in Gourgoulhon's signature) but its *functional dependence* on $(x^\mu, p_\mu)$ is non-trivial, and Hamilton's equations $\dot x^\mu = \partial H/\partial p_\mu$, $\dot p_\mu = -\partial H/\partial x^\mu$ correctly reproduce the equations of motion and additionally fix $\lambda = \tau$. The motivation for "proportional to the constraint" is that the constraint generates the gauge symmetry (reparametrisation), and a Hamiltonian that is a multiple of the constraint generates the same motion up to that gauge freedom — exactly what a reparametrisation-invariant theory requires.

There is a more elementary route, which sacrifices manifest covariance but produces the physically familiar Hamiltonian. Parametrise by an inertial observer's time, $\lambda = t$; then the free Lagrangian $L = -m\sqrt{1 - \mathbf{v}^2}$ is *not* homogeneous of degree one in the three-velocity $\mathbf{v}$ (it is a non-trivial function of $\mathbf{v}$), so its Legendre transform is non-degenerate and the naive recipe works: $\mathbf{p} = \partial L/\partial\mathbf{v} = m\gamma\mathbf{v}$, and $H = \mathbf{p}\cdot\mathbf{v} - L = m\gamma = \sqrt{\mathbf{p}^2 + m^2}$. This is the energy-momentum relation, read as the Hamiltonian — the energy expressed as a function of the three-momentum. The lesson is that the degeneracy is an artefact of insisting on a covariant parametrisation; choosing a time breaks the covariance and restores an ordinary Hamiltonian, at the cost of singling out a frame.

---

# The Definition

**The generalized four-momentum.** For a particle with Lagrangian $L(x^\mu, \dot x^\mu)$, the **generalized four-momentum** (or **canonical four-momentum**) is the field of linear forms $P$ along the worldline with components
$$\boxed{\,p_\mu \;:=\; \frac{\partial L}{\partial\dot x^\mu}\,}$$
in the basis dual to $(e_\mu)$. Because $L$ is homogeneous of degree one in $\dot x^\mu$, the components $p_\mu$ are homogeneous of degree zero, hence **independent of the parametrisation** $\lambda$. Explicitly:
- **Free particle:** $p_\mu = mc\,u_\mu$, i.e. $P = mcU$ (with $c=1$: $P = mU$), the [[Def - Four-Momentum and Rest Mass|four-momentum]] of the preceding chapter, satisfying the **primary constraint** $P\cdot P = m^2c^2$ (Gourgoulhon's $-m^2c^2$).
- **Particle in a vector field:** $p_\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$, i.e. $P = mcU + \tfrac{q}{c}A$; the **kinetic** momentum $P - \tfrac{q}{c}A = mcU$ satisfies $(P - \tfrac{q}{c}A)\cdot(P - \tfrac{q}{c}A) = m^2c^2$.

**The relativistic Hamiltonian.** The naive Legendre transform $H = p_\mu\dot x^\mu - L$ **vanishes identically** (Euler's identity) and the Legendre map is **non-invertible** (the Hessian of $L$ annihilates $\dot x^\mu$); see [[Thm - Hamiltonian Formulation (Relativistic Particle)]]. Two well-posed Hamiltonians replace it:

1. **The Dirac (constraint) Hamiltonian**, manifestly covariant, proportional to the mass-shell constraint:
$$\boxed{\,H(x^\mu, p_\mu) \;=\; \frac{1}{2m}\,\eta^{\mu\nu}\Big[p_\mu - \tfrac{q}{c}A_\mu\Big]\Big[p_\nu - \tfrac{q}{c}A_\nu\Big]\,}$$
(free particle: $q = 0$). Its numerical value on the motion is the constant $\tfrac{m}{2}c^2$ (Gourgoulhon's $-\tfrac12 mc^2$), but its functional form drives the canonical equations $\dot x^\mu = \partial H/\partial p_\mu$, $\dot p_\mu = -\partial H/\partial x^\mu$, which reproduce the Lorentz-force motion and select $\lambda = \tau$.

2. **The energy Hamiltonian**, non-covariant, obtained by parametrising with an inertial observer's time and Legendre-transforming in the three-velocity:
$$\boxed{\,H(\mathbf{x}, \mathbf{p}) \;=\; \sqrt{\mathbf{p}^2c^2 + m^2c^4}\,}\qquad(c=1:\ H = \sqrt{\mathbf{p}^2 + m^2}),$$
with charge: $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} + q\phi$ (with $c=1$). This $H$ is the energy of the particle, expressed as a function of the three-momentum $\mathbf{p} = m\gamma\mathbf{v}$; it is the time component of the four-momentum, $H = p^0 = E$.

The two Hamiltonians describe the same physics; the Dirac form keeps Lorentz covariance manifest and treats the constraint honestly, while the energy form is the recognisable $E(\mathbf{p})$ at the cost of singling out a frame.

---

# Categorical / Structural Definition

The generalized four-momentum is the **fibre derivative** of the Lagrangian, the canonical map from velocity space to momentum space underlying the [[Def - The Legendre Transform|Legendre transform]] of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|geometric mechanics]]. In coordinate-free terms, the Lagrangian is a function $L : TM \to \mathbb{R}$ on the tangent bundle (velocity space), and its fibre derivative $\mathbb{F}L : TM \to T^*M$ sends a velocity to the covector $p_\mu = \partial L/\partial\dot x^\mu$ — a momentum living in the cotangent space (phase space). The relativistic novelty is that this map is **not a local diffeomorphism**: its image is not all of $T^*M$ but the **mass-shell constraint surface** $\{P\cdot P = m^2\}$, a codimension-one submanifold. A Lagrangian whose fibre derivative is non-invertible in this way is called **degenerate** or **singular**, and the systematic theory of such Lagrangians — the Dirac–Bergmann constraint analysis — is the structural setting for the relativistic particle.

The Hamiltonian, in this picture, is a function on the cotangent bundle $T^*M$ (phase space, a [[Def - Symplectic Manifold|symplectic manifold]] carrying $\omega = dp_\mu\wedge dx^\mu$); its Hamiltonian vector field $X_H$, defined by $\iota_{X_H}\omega = dH$, generates the dynamics. For a regular Lagrangian, $H = p_\mu\dot x^\mu - L$ via the invertible fibre derivative, and the Lagrangian and Hamiltonian flows agree ([[Thm - Equivalence of Lagrangian and Hamiltonian Formalisms]]). For the degenerate relativistic Lagrangian this fails, and the Hamiltonian must be supplied differently (Dirac's constraint Hamiltonian, or the non-covariant energy). The relativistic particle is thus the canonical example distinguishing regular from degenerate Lagrangian systems.

---

# Relate to Other Fields / Compression

The generalized four-momentum is the relativistic instance of the **conjugate momentum** $p = \partial L/\partial\dot q$ of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian mechanics]], unified across the four spacetime directions and carrying a single subtlety: its time component is (minus, in some conventions) the energy. The relativistic Hamiltonian $H = \sqrt{\mathbf{p}^2 + m^2}$ is the **energy-momentum dispersion relation** read as a function on phase space, and its non-relativistic limit $\sqrt{\mathbf{p}^2 + m^2} \approx m + \mathbf{p}^2/(2m)$ recovers the Newtonian kinetic-energy Hamiltonian $\mathbf{p}^2/(2m)$ (plus the rest energy $m$).

**True name:** the generalized four-momentum is *"the thing you contract against displacements,"* a linear form, not a vector — and the relativistic Hamiltonian is *"the energy as a function of momentum,"* $E = \sqrt{\mathbf{p}^2 + m^2}$, with the covariant Dirac form being *"the mass-shell constraint used as a Hamiltonian."* The operational content of the momentum is that it is simultaneously the Noether charge (contracted with a generator), the Legendre variable (paired with velocity), and the quantisation target ($p_\mu \to i\hbar\partial_\mu$); the operational content of the Hamiltonian is that it is the generator of time-evolution and the operator whose eigenvalues are energies.

The degeneracy of the relativistic Lagrangian is the same phenomenon as the **constraints of gauge theory**: a reparametrisation-invariant or gauge-invariant Lagrangian always has a degenerate fibre derivative and a vanishing canonical Hamiltonian, because the gauge freedom means not all "velocities" correspond to physical motion. The relativistic particle is the simplest gauge system (its gauge symmetry is worldline reparametrisation), and its treatment is the template for the constrained Hamiltonian dynamics of electromagnetism, general relativity, and string theory.

---

# Examples / Corollaries

**Is an instance — the energy and three-momentum relative to an observer.** Decomposing the free four-momentum $P = mU$ relative to an inertial observer, the time component is the energy $p^0 = E = m\gamma$ and the spatial components are the three-momentum $\mathbf{p} = m\gamma\mathbf{v}$. The Hamiltonian $H = \sqrt{\mathbf{p}^2 + m^2} = m\gamma = E$ is exactly this energy, confirming that the relativistic Hamiltonian is the energy of the particle. The mass-shell constraint $P\cdot P = m^2$ reads $E^2 - \mathbf{p}^2 = m^2$, the famous $E^2 = \mathbf{p}^2c^2 + m^2c^4$.

**Is an instance — the Dirac Hamiltonian's constant value.** Evaluating the free Dirac Hamiltonian $H = \tfrac{1}{2m}\eta^{\mu\nu}p_\mu p_\nu$ on the physical motion, where $P\cdot P = m^2$, gives $H = \tfrac{1}{2m}\cdot m^2 = \tfrac{m}{2}$ — a constant. This constancy is consistent with the Hamiltonian being conserved (no explicit time-dependence), but it is the *functional form* $\tfrac{1}{2m}\eta^{\mu\nu}p_\mu p_\nu$, not the number $\tfrac{m}{2}$, that generates the equations of motion via Hamilton's equations.

**Is NOT an instance — the naive Legendre transform.** The quantity $H_{\text{naive}} = p_\mu\dot x^\mu - L$ is *not* a usable Hamiltonian: for the covariant relativistic Lagrangian it equals zero identically, by Euler's homogeneity identity. Attempting to use it produces no dynamics. This is the degeneracy that the Dirac or energy Hamiltonian circumvents; the naive recipe works only for non-degenerate (non-reparametrisation-invariant) Lagrangians.

**Is NOT an instance — the kinetic momentum as the canonical momentum (charged case).** For a charged particle, $mcU$ is the kinetic momentum, not the generalized momentum $P = mcU + \tfrac{q}{c}A$. The canonical momentum is the conserved Noether charge and the phase-space variable; the kinetic momentum is what satisfies the mass shell. Conflating them gives the wrong constraint ($P\cdot P = m^2$ instead of $(P - \tfrac{q}{c}A)\cdot(P - \tfrac{q}{c}A) = m^2$) and the wrong Hamiltonian.

**Corollary — minimal substitution.** The charged-particle constraint $(P - \tfrac{q}{c}A)\cdot(P - \tfrac{q}{c}A) = m^2c^2$ is obtained from the free constraint $P\cdot P = m^2c^2$ by the substitution $P \mapsto P - \tfrac{q}{c}A$. This **minimal substitution** $p_\mu \to p_\mu - \tfrac{q}{c}A_\mu$, applied to the free Hamiltonian, generates the entire electromagnetic coupling — in classical mechanics here, and (promoting to operators) in the Klein–Gordon and Dirac equations.

**Calibration check.** Verify that (i) $p_\mu = \partial L/\partial\dot x^\mu$ is independent of the parametrisation, by checking it is homogeneous of degree zero in $\dot x^\mu$; (ii) the free energy Hamiltonian $H = \sqrt{\mathbf{p}^2 + m^2}$ reproduces $\mathbf{p} = m\gamma\mathbf{v}$ via $\mathbf{v} = \partial H/\partial\mathbf{p}$, and $H = E = m\gamma$; (iii) the naive Hamiltonian $p_\mu\dot x^\mu - L$ vanishes for the free Lagrangian, using $\dot x^\mu\partial L/\partial\dot x^\mu = L$.

---

# Unlocked by This

> [!tip] The Klein–Gordon and Dirac Equations *(from Quantum Field Theory)*
> Promoting the generalized four-momentum to the operator $p_\mu \to i\hbar\,\partial_\mu$ and imposing the mass-shell constraint $\eta^{\mu\nu}p_\mu p_\nu = m^2c^2$ as an operator equation on a wavefunction gives the **Klein–Gordon equation** $(\hbar^2\Box + m^2c^2)\psi = 0$. Taking the "square root" of the energy Hamiltonian $H = \sqrt{\mathbf{p}^2c^2 + m^2c^4}$ — to obtain a first-order equation with a Hamiltonian linear in $\mathbf{p}$ — forces the introduction of the gamma matrices and yields the **Dirac equation**, whose solutions carry spin one-half. The minimal substitution $p_\mu \to p_\mu - \tfrac{q}{c}A_\mu$ couples both to electromagnetism. The classical four-momentum of this page is precisely the object that gets quantised.

> [!tip] Constrained Hamiltonian Systems and the Dirac Bracket *(from Gauge Theory)*
> The primary constraint $P\cdot P - m^2 = 0$ and the vanishing canonical Hamiltonian are the defining data of a **constrained Hamiltonian system** in the **Dirac–Bergmann** formalism. The constraint is **first-class** (its Poisson bracket with itself vanishes), which signals a gauge symmetry — here worldline reparametrisation. The systematic treatment introduces the **Dirac bracket** to handle constraints, gauge-fixing conditions to eliminate the redundancy, and culminates in the **BRST** quantisation used for gauge theories and gravity. The relativistic particle is the simplest worked example, and understanding its constraint is the entry point to the canonical quantisation of any gauge theory.

> [!tip] The Hamilton–Jacobi Equation and Geometric Optics *(from Classical Mechanics)*
> Writing $p_\mu = \partial_\mu \mathcal{S}$ for an action function $\mathcal{S}(x)$ and substituting into the mass-shell constraint gives the relativistic **Hamilton–Jacobi equation** $\eta^{\mu\nu}\partial_\mu\mathcal{S}\,\partial_\nu\mathcal{S} = m^2c^2$, whose characteristics are the particle worldlines. In the $m \to 0$ (or short-wavelength) limit this becomes the **eikonal equation** of geometric optics, and the bridge between the Hamilton–Jacobi action and the quantum phase is the WKB approximation. The generalized four-momentum as a gradient of the action is the classical limit of the quantum momentum operator acting on $e^{i\mathcal{S}/\hbar}$.
