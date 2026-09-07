---
type: definition
subject: special-relativity
prereqs:
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Four-Force"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, timelike $\eta_{\mu\nu}\dot x^\mu\dot x^\nu > 0$ (Gourgoulhon: mostly-plus, opposite sign). A particle $\mathcal{P}$ of rest mass $m$ and **charge** $q$ moves on a worldline $x^\mu(\lambda)$ with parameter-velocity $\dot x^\mu$, four-velocity $U$ ($u_\mu = \eta_{\mu\nu}U^\nu$, $U\cdot U = 1$), and four-acceleration $a^\mu = dU^\mu/d\tau$. The external field is given by a **potential one-form** $A$ with components $A_\mu(x)$ in the basis dual to $(e_\mu)$, so $A_\mu = \langle A, e_\mu\rangle$. The associated **field-strength two-form** has components $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ (see [[Def - The Electromagnetic Field Tensor]]). The action is $S = \int L\,d\lambda$. With $c$ restored the charge enters as $q/c$. Full registry on [[Special Relativity XV — The Principle of Least Action]].

---

# Axiom Motivation

We have the [[Def - Relativistic Action of a Free Particle|free action]] $-mc\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$; the goal is to *add an interaction* so that the particle responds to an external field, while preserving the two structural features that made the free action well-posed: it must be a Lorentz scalar (so all observers compute the same action), and it must be reparametrisation-invariant (so the action depends only on the worldline). The question is: what is the simplest interaction term meeting both demands?

The field must be encoded in some geometric object on spacetime. The simplest non-trivial choice, after a scalar, is a **one-form** $A$ — a field of linear forms $A_\mu(x)$. To build a scalar from $A$ and the worldline, contract $A$ with the only worldline-vector available, the tangent $\dot x^\mu$: the quantity $A_\mu(x)\dot x^\mu$ is a scalar (one index up, one down, summed). And it is *reparametrisation-invariant when integrated*: under $\lambda \to \tilde\lambda$, $\dot x^\mu = (d\tilde\lambda/d\lambda)\,\tilde x'^\mu$, so $A_\mu\dot x^\mu\,d\lambda = A_\mu\,dx^\mu$ depends only on the curve, exactly like the proper-time integrand. Indeed $A_\mu\dot x^\mu$ is homogeneous of degree *one* in $\dot x^\mu$, matching the free Lagrangian's homogeneity. So the simplest admissible interaction Lagrangian is
$$L_{\text{int}} = q\,A_\mu(x)\dot x^\mu,$$
with a coupling constant $q$ (the **charge**) measuring how strongly the particle feels the field. The action is then $S = -m\int d\tau + q\int A_\mu\,dx^\mu$, the free part plus the line integral of the potential along the worldline.

Why *this* and not a nearby variant? Consider the alternatives. *A term quadratic in $\dot x^\mu$*, say $A_{\mu\nu}\dot x^\mu\dot x^\nu$, would be homogeneous of degree two, breaking reparametrisation invariance — it would change the action's value under a reparametrisation, so "the action of a worldline in this field" would be ill-defined. (A degree-two term *can* be admitted by dividing by the free radicand, $h_{\mu\nu}\dot x^\mu\dot x^\nu/\sqrt{\eta\dot x\dot x}$, which restores degree one; this is the *tensor*-field coupling, a genuinely different and more complicated interaction used in attempts at flat-space gravity.) *A term with $A$ contracted against itself*, $A_\mu A^\mu$, would not involve the worldline-velocity at all and would describe a position-dependent potential energy, not a velocity-coupled force; it is the *scalar*-field coupling $\Phi(x)\sqrt{\eta\dot x\dot x}$ in disguise, again a different interaction. The linear-in-velocity, one-form coupling $qA_\mu\dot x^\mu$ is the unique simplest term that is both Lorentz-scalar and degree-one homogeneous, and it is the one that produces a *velocity-dependent* force — which, as we will see, is exactly the magnetic-type force of electromagnetism.

The payoff justifies the choice retroactively, and this is the most convincing motivation. Vary the action and the equation of motion is $mc^2 a_\mu = qF_{\mu\nu}U^\nu$, where $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is automatically antisymmetric. An antisymmetric $F$ guarantees the force is a *pure* four-force, $\langle f, U\rangle = qF_{\mu\nu}U^\mu U^\nu = 0$ (contraction of antisymmetric $F$ with symmetric $UU$ vanishes), which is exactly the condition that the rest mass stay constant — no four-force coupling to a massive particle may change its rest mass, and the one-form coupling delivers precisely this. Had we chosen a coupling whose force was not orthogonal to $U$, the rest mass would not be conserved and the particle would not remain the particle it was. The structure of the interaction is dictated by the requirement that it be a consistent force on a massive particle, and the one-form coupling is the unique simplest solution.

Finally, the choice is forced by a deeper principle visible only in hindsight: **gauge invariance**. The action $q\int A_\mu dx^\mu$ changes, under $A \mapsto A + d\chi$, by $q\int d\chi = q[\chi]_{A_1}^{A_2}$, a pure endpoint term that does not affect the equations of motion. So the physics depends on $A$ only through the gauge-invariant combination $F = dA$, and the potential $A$ is determined only up to a gradient. This redundancy is not a defect; it is the seed of the entire gauge principle, and it is automatic for the one-form coupling because $\int A_\mu dx^\mu$ is the integral of a one-form, the natural gauge-covariant object.

---

# The Definition

A particle $\mathcal{P}$ of rest mass $m$ and charge $q$ is said to be coupled to a **vector field** (or to undergo a **vectorial interaction**) with potential one-form $A$ if its dynamics follows from the principle of stationary action with Lagrangian
$$\boxed{\,L(x^\mu, \dot x^\mu) \;=\; -mc\,\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu} \;+\; \frac{q}{c}\,A_\mu(x)\,\dot x^\mu\,}$$
(with $c = 1$: $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu} + q A_\mu\dot x^\mu$), equivalently the action
$$S \;=\; -mc^2\!\int d\tau \;+\; q\!\int A_\mu\,dx^\mu \qquad(c=1:\ S = -m\!\int d\tau + q\!\int A_\mu\,dx^\mu).$$
This is the **minimal-coupling** prescription. The Lagrangian is a Lorentz scalar and is homogeneous of degree one in $\dot x^\mu$ (both terms are), so the action is reparametrisation-invariant.

The Euler–Lagrange equations of this Lagrangian are, using $\partial L/\partial\dot x^\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$ and $\partial L/\partial x^\mu = \tfrac{q}{c}(\partial_\mu A_\nu)\dot x^\nu$, equivalent (after dividing by the free radicand and parametrising by proper time) to the **Lorentz four-force law**
$$mc^2\,a_\mu \;=\; q\,F_{\mu\nu}\,U^\nu, \qquad F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu,$$
or in coordinate-free form $f = q\,F(\cdot, U)$, where $F$ is the antisymmetric **field-strength two-form** (see [[Def - The Electromagnetic Field Tensor]]). The force is a **pure four-force**: $\langle f, U\rangle = qF_{\mu\nu}U^\mu U^\nu = 0$ by the antisymmetry of $F$, so the rest mass $m$ is conserved along the worldline. When the field is electromagnetic, $q$ is the **electric charge** and this is the Lorentz force on a charged particle.

The **generalized four-momentum** (see [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]) is $p_\mu = \partial L/\partial\dot x^\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$, so the canonical momentum $P = mcU + \tfrac{q}{c}A$ differs from the kinetic momentum $mcU$ by $\tfrac{q}{c}A$; the kinetic momentum obeys the mass-shell relation $(P - \tfrac{q}{c}A)\cdot(P - \tfrac{q}{c}A) = m^2c^2$.

---

# Relate to Other Fields / Compression

This is the relativistic, geometric form of the **minimal-coupling** rule familiar from non-relativistic mechanics, where a charged particle in a magnetic field has Lagrangian $L = \tfrac12 m\dot{\mathbf{x}}^2 + q\mathbf{A}\cdot\dot{\mathbf{x}} - q\phi$. The relativistic version unifies the scalar potential $\phi$ and vector potential $\mathbf{A}$ into the single one-form $A_\mu = (\phi, -\mathbf{A})$ (mostly-minus) and replaces the kinetic term by the proper-time term; the interaction $qA_\mu\dot x^\mu = q(\phi\,dt - \mathbf{A}\cdot d\mathbf{x})/d\lambda \cdot d\lambda$ is the covariant packaging of $-q\phi\,dt + q\mathbf{A}\cdot d\mathbf{x}$.

The construction is literally the same as the **coupling of a particle to a connection** in [[Gauge Theory — Series Map|gauge theory]]. The potential one-form $A$ *is* the connection one-form of the electromagnetic $U(1)$ bundle; the line integral $q\int A_\mu dx^\mu$ is the *holonomy* (the integrated connection along the path), which determines the phase a charged quantum particle accumulates; and the gauge transformation $A \mapsto A + d\chi$ is a change of bundle trivialisation. Minimal coupling is the statement that the charge's phase is parallel-transported by the connection $A$, and the classical Lorentz force is the shadow of that parallel transport.

**True name:** the vector-field action is *"free action plus the holonomy of the potential."* The operational content is that you couple a charge to a field by *adding the line integral of the connection one-form along the worldline*, weighted by the charge — and everything follows: the Lorentz force (by variation), the gauge invariance (because $\int d\chi$ is a boundary term), and the canonical momentum $mcU + \tfrac{q}{c}A$ (by differentiation). To reconstruct the interaction, remember "add $q\int A$."

---

# Examples / Corollaries

**Is an instance — a charge in a uniform magnetic field.** Take $A_\mu$ such that $F_{\mu\nu}$ has only the $F_{12} = -B$ component (a uniform field $\mathbf{B} = B\hat{\mathbf{z}}$). The Lorentz force $mc^2 a_\mu = qF_{\mu\nu}U^\nu$ gives circular motion in the $xy$-plane at the cyclotron frequency $\omega = qB/(m\gamma)$ — the helical worldline of a charged particle in a magnetic field. This is the prototypical vectorial interaction and the basis of cyclotrons and synchrotrons.

**Is an instance — a charge in a static electric field.** Take $A_0 = \phi(x)$ time-independent, $\mathbf{A} = 0$, so $F_{0i} = -\partial_i\phi = E_i$. The Lorentz force gives $mc^2 a_i = qE_i$, the relativistic generalisation of $\mathbf{F} = q\mathbf{E}$, with the relativistic correction that the *rest* mass times *four*-acceleration appears, not the Newtonian $m\ddot{\mathbf{x}}$. Because $A_0$ is time-independent, the energy $p_0$ is conserved (a Noether charge of time-translation).

**Is NOT an instance — a scalar coupling $-q\Phi\sqrt{\eta\dot x\dot x}$.** The Lagrangian $L = -[mc + \tfrac{q}{c}\Phi(x)]\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ couples the particle to a *scalar* field $\Phi$, not a vector field. Its force, $f = -q\Phi\,a - q\,\nabla\Phi\circ\perp_U$, involves the four-acceleration and the projector onto the rest space — a fundamentally different structure from the velocity-linear Lorentz force, and not derivable from a one-form. The scalar coupling effectively makes the mass position-dependent ($m \to m + \tfrac{q}{c}\Phi$); it is *not* the electromagnetic interaction.

**Is NOT an instance — the kinetic momentum mistaken for the canonical momentum.** The quantity $mcU$ is the kinetic momentum, *not* the generalized (canonical) momentum $P = mcU + \tfrac{q}{c}A$. Writing the conserved Noether charge or the Hamiltonian variable as $mcU$ for a charged particle is an error: the conserved canonical momentum is $mcU + \tfrac{q}{c}A$, and it is this that gets promoted to $i\hbar\partial_\mu$ in quantisation. The two coincide only when $A = 0$ (free particle).

**Corollary — gauge invariance of the dynamics.** Under $A \mapsto A + d\chi$, the action changes by $q\int d\chi = q[\chi(A_2) - \chi(A_1)]$, an endpoint term independent of the path between $A_1$ and $A_2$. The Euler–Lagrange equations, which depend only on bulk variations with fixed endpoints, are therefore unchanged: the equation of motion depends on $A$ only through $F = dA$. The canonical momentum, however, *does* shift, $P \mapsto P + q\,d\chi$, which is why the canonical momentum is gauge-dependent while the kinetic momentum $mcU$ is gauge-invariant.

**Calibration check.** Verify that (i) $L_{\text{int}} = \tfrac{q}{c}A_\mu\dot x^\mu$ is homogeneous of degree one in $\dot x^\mu$, so the full Lagrangian remains reparametrisation-invariant; (ii) the force $qF_{\mu\nu}U^\nu$ is orthogonal to $U$, $qF_{\mu\nu}U^\mu U^\nu = 0$, by the antisymmetry of $F$, confirming the rest mass is conserved; (iii) under $A \mapsto A + d\chi$ the action changes only by a boundary term, so the equations of motion are gauge-invariant while the canonical momentum $P = mcU + \tfrac{q}{c}A$ is not.

---

# Unlocked by This

> [!tip] The Lorentz Force and the Field-Strength Tensor *(from Electromagnetism)*
> Varying this action *is* the derivation of the **Lorentz force** $f = qF(\cdot, U)$, and it shows that the electric and magnetic fields are not fundamental: what is fundamental is the potential one-form $A$, and the observable field is its exterior derivative $F = dA$, an antisymmetric tensor whose six components are the three of $\mathbf{E}$ and three of $\mathbf{B}$ relative to an observer. The exactness $F = dA$ forces the homogeneous Maxwell equations $dF = 0$ automatically (by $d^2 = 0$), before any field dynamics is specified. See [[Special Relativity XXI — The Electromagnetic Field]] and [[Special Relativity XXII — Maxwell's Equations]].

> [!tip] Gauge Invariance and the Aharonov–Bohm Effect *(from Quantum Mechanics and Gauge Theory)*
> The gauge invariance $A \mapsto A + d\chi$ of this action — the physics depending only on $F = dA$ — is the classical root of the **gauge principle**. Quantum-mechanically, the line integral $q\int A_\mu dx^\mu$ is the phase a charged particle accumulates, and although it is gauge-dependent, the phase *difference* around a closed loop, $q\oint A_\mu dx^\mu = q\int F$, is gauge-invariant and physically observable even where $F = 0$ along the path — the **Aharonov–Bohm effect**. The potential $A$ is the **electromagnetic connection** of [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]], and minimal coupling is parallel transport of the quantum phase.

> [!tip] Minimal Coupling in Quantum Field Theory *(from Quantum Field Theory)*
> The canonical momentum $P = mcU + \tfrac{q}{c}A$ produced here, promoted to an operator, gives the **minimal-coupling substitution** $p_\mu \to p_\mu - \tfrac{q}{c}A_\mu$ that couples *every* charged quantum field to electromagnetism: the Klein–Gordon and Dirac equations acquire their electromagnetic interaction by replacing the free four-momentum with the kinetic one $P - \tfrac{q}{c}A$. The mass-shell constraint $(P - \tfrac{q}{c}A)\cdot(P - \tfrac{q}{c}A) = m^2$ derived on this page becomes, under quantisation, the gauge-covariant wave equation. This single substitution is the origin of all electromagnetic interactions in the Standard Model.
