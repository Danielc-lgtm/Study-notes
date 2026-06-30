---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Lagrangian for a Particle in a Vector Field"
  - "Def - The Legendre Transform"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, timelike $\eta_{\mu\nu}\dot x^\mu\dot x^\nu > 0$ (Gourgoulhon: mostly-plus, opposite sign; his free constraint $p\cdot p = -m^2c^2$ is our $+m^2c^2$, his Dirac value $-\tfrac12 mc^2$ our $+\tfrac{m}{2}c^2$). A particle has worldline $x^\mu(\lambda)$, parameter-velocity $\dot x^\mu$, four-velocity $U$, charge $q$, potential one-form $A_\mu$. The generalized four-momentum is $p_\mu = \partial L/\partial\dot x^\mu$ (see [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]). The Hamiltonian is $H(x^\mu, p_\mu)$, phase space $\mathsf{P}$, Poisson bracket $\{f, g\}$. For systems of particles, $a, b$ index the particles, $\lambda_a$ their separate parameters, $m_a, q_a$ their masses and coupling constants. Full registry on [[Special Relativity XV — The Principle of Least Action]].

---

# Statement

> **Theorem (Hamiltonian formulation of the relativistic particle).** Let a relativistic particle have a reparametrisation-invariant Lagrangian $L(x^\mu, \dot x^\mu)$, homogeneous of degree one in $\dot x^\mu$. Then:
> 1. **(Vanishing canonical Hamiltonian.)** The naive Legendre transform vanishes identically: $H_{\text{naive}} := p_\mu\dot x^\mu - L = 0$, by Euler's identity $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$.
> 2. **(Non-invertible Legendre map.)** The map $\dot x^\mu \mapsto p_\mu = \partial L/\partial\dot x^\mu$ is not invertible: the Hessian $\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu$ annihilates $\dot x^\mu$. Consequently the momenta obey a **primary constraint** — for a free particle $\eta^{\mu\nu}p_\mu p_\nu = m^2c^2$, for a charged particle $\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu) = m^2c^2$.
> 3. **(Dirac's resolution.)** The Hamiltonian $H = \tfrac{1}{2m}\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu)$, proportional to the constraint, generates the correct dynamics: the canonical equations $\dot x^\mu = \partial H/\partial p_\mu$, $\dot p_\mu = -\partial H/\partial x^\mu$ reproduce the Lorentz-force equation of motion and fix the parameter to be the proper time, $\lambda = \tau$.

> **Corollary (energy Hamiltonian).** Parametrising instead by an inertial observer's time, the (now non-degenerate) Lagrangian $L = -m\sqrt{1 - \mathbf{v}^2}$ has the ordinary Legendre transform $H = \mathbf{p}\cdot\mathbf{v} - L = \sqrt{\mathbf{p}^2 + m^2}$, the energy of the particle as a function of its three-momentum $\mathbf{p} = m\gamma\mathbf{v}$.

---

# Motivation

The Hamiltonian formulation of any classical theory is worth having because it is the gateway to canonical quantisation, to the Poisson-bracket algebra of observables, and to the powerful machinery of canonical transformations. For the relativistic particle, constructing it is not the routine exercise it is in non-relativistic mechanics: the naive recipe produces a Hamiltonian that is identically zero, and one must understand *why* before one can repair it.

The "why" is the most instructive part, and it is the reason this theorem deserves a page of its own rather than a line in the definition. The vanishing of the canonical Hamiltonian is not an accident or an error; it is the signature of a **reparametrisation-invariant theory** — a theory with no absolute time. In such a theory, "evolution in the parameter $\lambda$" is not a physical process but a gauge transformation (a relabelling of points on the worldline), and the generator of a gauge transformation, the Hamiltonian, *must* vanish on the physical phase space. The same phenomenon recurs, far more consequentially, in general relativity, whose Hamiltonian is a sum of constraints because the theory is invariant under arbitrary changes of spacetime coordinates, and in string theory, where the worldsheet is reparametrisation-invariant. The relativistic particle is the simplest theory exhibiting this structure, and grasping it here — that the vanishing Hamiltonian and the primary constraint are two faces of the worldline's reparametrisation gauge symmetry — is grasping the first conceptual step of canonical quantum gravity.

The theorem also closes the loop on the formalism. Having a Hamiltonian, even a constrained one, lets the relativistic particle be embedded in the [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|symplectic geometry]] the reader already knows: phase space is a cotangent bundle, the dynamics is a Hamiltonian flow, observables form a Poisson algebra. Dirac's resolution — take the Hamiltonian proportional to the constraint — is the prototype of constrained Hamiltonian dynamics, and the energy Hamiltonian $H = \sqrt{\mathbf{p}^2 + m^2}$ is the object that, made into an operator, gives the relativistic wave equations. The theorem is the bridge from the variational picture of the chapter to the canonical picture of quantum mechanics.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever one has a reparametrisation-invariant Lagrangian, and recognising that condition is the first input-broadening move.

The first disguised source is **"the Lagrangian is homogeneous of degree one in the velocities."** Any Lagrangian built from $\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ and $A_\mu\dot x^\mu$ — the free particle, the minimally-coupled charge, the scalar and tensor couplings — is degree-one homogeneous, hence reparametrisation-invariant, hence subject to the vanishing-Hamiltonian and primary-constraint conclusions. The bridge is Euler's identity: degree-one homogeneity *is* $\dot x^\mu\partial L/\partial\dot x^\mu = L$. *Example problem:* show that the minimally-coupled charged particle has a vanishing canonical Hamiltonian and a primary constraint $(P - qA)\cdot(P - qA) = m^2$, and construct the Dirac Hamiltonian.

The second disguised source is **"the action has a local gauge symmetry."** More generally than reparametrisation, any local symmetry of the action — a transformation depending on an arbitrary function of the parameter — forces a degenerate Legendre transform and primary constraints, by the same mechanism. The bridge is that a gauge symmetry means the equations of motion do not determine all the velocities, so the fibre derivative cannot be invertible. *Example problem:* recognise that the einbein form of the free action, $S = \tfrac12\int(e^{-1}\eta\dot x\dot x - e m^2)d\lambda$, has a gauge symmetry mixing $e$ and the reparametrisation, and read off its constraint.

The third disguised source is **"the system has fewer physical degrees of freedom than configuration variables."** When the number of genuine degrees of freedom (here three) is less than the number of configuration coordinates (here four), the missing one signals a constraint and a degenerate Hamiltonian. The bridge is the counting argument: $n$ coordinates with $n - k$ physical degrees of freedom give $k$ primary constraints. *Example problem:* for the relativistic particle, identify the single missing degree of freedom with the parametrisation gauge and the single primary constraint with the mass shell.

**Targets (Output Amplification)**

The conclusion provides a Hamiltonian (constrained or energy) and the mass-shell constraint.

Combine the conclusion with **canonical quantisation**. Promoting the phase-space variables to operators with $[\hat x^\mu, \hat p_\nu] = i\hbar\delta^\mu_\nu$ and imposing the constraint as an operator condition on physical states, $(\hat P\cdot\hat P - m^2)|\psi\rangle = 0$, gives the **Klein–Gordon equation**. The further result is the relativistic wave equation, obtained by quantising the constraint rather than a Hamiltonian. The combination is the standard route from classical constrained dynamics to relativistic quantum mechanics, and it is why the constraint, not the (vanishing) Hamiltonian, is the object of interest. *Example:* the Klein–Gordon and Dirac equations.

Combine the conclusion with **the energy Hamiltonian and Hamilton's equations**. From $H = \sqrt{\mathbf{p}^2 + m^2}$, the equation $\mathbf{v} = \partial H/\partial\mathbf{p} = \mathbf{p}/\sqrt{\mathbf{p}^2 + m^2}$ recovers $\mathbf{p} = m\gamma\mathbf{v}$, and $\dot{\mathbf{p}} = -\partial H/\partial\mathbf{x} = 0$ for a free particle gives momentum conservation. The further result is the complete free-particle dynamics in the recognisable energy-momentum variables. The combination is useful because it connects the abstract constrained formalism to the familiar $E = \sqrt{\mathbf{p}^2 + m^2}$. *Example:* the relativistic dispersion relation as a Hamiltonian.

Combine the conclusion with **the Poisson-bracket algebra**. The phase-space functions form a [[Def - Poisson Bracket|Poisson algebra]], and the constraint $C = P\cdot P - m^2$ generates the gauge transformations via $\{C, \cdot\}$; gauge-fixing (e.g. choosing $\lambda = \tau$) and passing to the Dirac bracket gives the reduced phase space of genuine degrees of freedom. The further result is the symplectic structure of the physical phase space, the arena for quantisation. The combination is nonobvious because it shows the constraint is not merely a relation among momenta but the *generator* of the theory's gauge symmetry. *Example:* the reduced phase space of the relativistic particle, six-dimensional (three positions, three momenta).

---

# Why Is It True

The whole theorem flows from one algebraic fact and its interpretation: **a Lagrangian homogeneous of degree one in the velocities has a Hessian that annihilates the velocity vector, and this single degeneracy simultaneously makes the canonical Hamiltonian vanish, makes the Legendre map non-invertible, and forces a primary constraint — all because the theory has a reparametrisation gauge symmetry that removes one degree of freedom.**

Start with Euler's identity. A function homogeneous of degree one satisfies $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$. Two consequences follow by differentiation and substitution. *Differentiating* the identity with respect to $\dot x^\nu$ gives $\partial L/\partial\dot x^\nu + \dot x^\mu\,\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu = \partial L/\partial\dot x^\nu$, hence $\dot x^\mu\,\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu = 0$: the Hessian has $\dot x^\mu$ in its kernel, so $\det(\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu) = 0$ and the Legendre map $\dot x \mapsto p = \partial L/\partial\dot x$ cannot be inverted. *Substituting* the identity into the naive Hamiltonian gives $H_{\text{naive}} = p_\mu\dot x^\mu - L = \dot x^\mu\,\partial L/\partial\dot x^\mu - L = L - L = 0$. The same identity is responsible for both failures.

Now interpret. The non-invertibility of $\dot x \mapsto p$ means the four momenta $p_\mu$ are not four independent functions of the four velocities $\dot x^\mu$ — there is a relation among them, the **primary constraint**, which for the free particle is computed directly: $p_\mu = m u_\mu$ with $u_\mu u^\mu = 1$ gives $\eta^{\mu\nu}p_\mu p_\nu = m^2$. The image of the Legendre map is not all of momentum space but the mass shell. And the vanishing of the canonical Hamiltonian means that $\lambda$-evolution is generated by *nothing* on the constraint surface — which is the correct statement, because $\lambda$ is an arbitrary parameter and shifting it is a gauge transformation, not a physical evolution. A reparametrisation-invariant theory *must* have a vanishing Hamiltonian, because a non-zero Hamiltonian would generate genuine evolution in an unphysical parameter.

Dirac's resolution is then natural. The physical content of the theory is "the worldline lies on the mass shell and is a geodesic," and the way to encode "stay on the mass shell" in Hamiltonian language is to take a Hamiltonian *proportional to the constraint*, $H = \tfrac{1}{2m}(P\cdot P - \text{const})$ or simply $\tfrac{1}{2m}P\cdot P$. Its numerical value on the motion is constant (it is $\tfrac{m}{2}$), so it carries no spurious evolution, but its *functional form* in $(x, p)$ is non-trivial, and Hamilton's equations $\dot x^\mu = \partial H/\partial p_\mu = \tfrac{1}{m}\eta^{\mu\nu}(p_\nu - qA_\nu)$ and $\dot p_\mu = -\partial H/\partial x^\mu$ reproduce, after a short calculation, the relativistic equation of motion *and* enforce $\lambda = \tau$. The mechanism is that the constraint generates the reparametrisation gauge orbit, and choosing the multiplier $\tfrac{1}{2m}$ corresponds to gauge-fixing $\lambda = \tau$.

The energy Hamiltonian is the down-to-earth alternative: break the covariance by choosing $\lambda = t$, an inertial time. Then the Lagrangian $-m\sqrt{1 - \mathbf{v}^2}$ is a function of $\mathbf{v}$ that is *not* homogeneous of degree one (it is $-m$ at $\mathbf{v} = 0$, not zero), so its Hessian in $\mathbf{v}$ is non-degenerate, the Legendre map $\mathbf{v} \mapsto \mathbf{p} = m\gamma\mathbf{v}$ is invertible, and the ordinary recipe gives $H = \mathbf{p}\cdot\mathbf{v} - L = m\gamma = \sqrt{\mathbf{p}^2 + m^2}$. The degeneracy was a consequence of insisting on a covariant parameter; fixing a time removes it, at the cost of singling out a frame and obscuring Lorentz covariance.

---

# What Makes This Hard

The technical content is short, but it is counterintuitive in a way that trips up nearly everyone the first time. The shock is that the Hamiltonian vanishes — a result that looks like a contradiction (no Hamiltonian, no dynamics?) until one recognises it as the fingerprint of reparametrisation invariance, after which it becomes a feature. The non-obvious step is Dirac's: realising that one should take a Hamiltonian *proportional to the constraint* whose numerical value is an irrelevant constant but whose functional form drives the dynamics. The most common error is to conclude from $H \equiv 0$ that the formalism has failed, rather than that the parameter $\lambda$ is gauge and the genuine dynamics lives on the constraint surface; the second most common is to forget that the *kinetic* momentum, not the canonical momentum, satisfies the mass shell for a charged particle.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Everything follows from Euler's homogeneity identity. Use it directly to show $H_{\text{naive}} = 0$; differentiate it to show the Hessian is singular and hence the Legendre map non-invertible; compute the constraint explicitly from $P = mU$; then verify Dirac's constraint-Hamiltonian reproduces the dynamics.

**Subgoal decomposition:**

1. **Show $H_{\text{naive}} = 0$.** From $\dot x^\mu\partial L/\partial\dot x^\mu = L$, conclude $p_\mu\dot x^\mu - L = 0$.
   - *Hint:* The naive Hamiltonian is literally the left minus the right side of Euler's identity.
   - *Why needed:* It establishes that the covariant Legendre transform carries no dynamics.

2. **Show the Legendre map is non-invertible.** Differentiate Euler's identity with respect to $\dot x^\nu$ to get $\dot x^\mu\,\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu = 0$.
   - *Hint:* The Hessian annihilates $\dot x^\mu$, so its determinant is zero.
   - *Why needed:* Non-invertibility means the momenta are constrained, not free.

3. **Compute the primary constraint.** From $p_\mu = m u_\mu$ (free) and $u_\mu u^\mu = 1$, get $\eta^{\mu\nu}p_\mu p_\nu = m^2$; for the charged case, $p_\mu = m u_\mu + qA_\mu$ gives $(p - qA)\cdot(p - qA) = m^2$.
   - *Hint:* Square the four-momentum and use the four-velocity normalisation.
   - *Why needed:* The constraint is the explicit relation that the non-invertibility predicted.

4. **Verify Dirac's Hamiltonian.** Take $H = \tfrac{1}{2m}\eta^{\mu\nu}(p_\mu - qA_\mu)(p_\nu - qA_\nu)$ and check that $\dot x^\mu = \partial H/\partial p_\mu$, $\dot p_\mu = -\partial H/\partial x^\mu$ give the Lorentz-force equation and $\lambda = \tau$.
   - *Hint:* $\partial H/\partial p_\mu = \tfrac1m(p^\mu - qA^\mu) = U^\mu$ fixes $\lambda = \tau$; differentiate again for the force.
   - *Why needed:* It confirms the constraint-Hamiltonian recipe reproduces the known dynamics.

---

# Lemma Decomposition

> [!note]- Lemma 1: The canonical Hamiltonian vanishes
> **Statement:** For a Lagrangian homogeneous of degree one in $\dot x^\mu$, $H_{\text{naive}} = p_\mu\dot x^\mu - L = 0$.
>
> **Hint:** Apply Euler's identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ directly.
>
> **Why needed:** It is conclusion (1) and the first sign of the degeneracy.
>
> > [!note]- Full proof
> > By definition $p_\mu = \partial L/\partial\dot x^\mu$, so $p_\mu\dot x^\mu = \dot x^\mu\,\partial L/\partial\dot x^\mu$. Euler's theorem on homogeneous functions, applied to $L$ homogeneous of degree one in $\dot x^\mu$, gives $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$. Hence $H_{\text{naive}} = p_\mu\dot x^\mu - L = L - L = 0$. $\blacksquare$

> [!note]- Lemma 2: The Legendre map is non-invertible
> **Statement:** The Hessian $W_{\mu\nu} := \partial^2 L/\partial\dot x^\mu\partial\dot x^\nu$ satisfies $\dot x^\mu W_{\mu\nu} = 0$, so $\det W = 0$ and $\dot x^\mu \mapsto p_\mu$ cannot be inverted.
>
> **Hint:** Differentiate Euler's identity with respect to $\dot x^\nu$.
>
> **Why needed:** Non-invertibility is conclusion (2) and forces the primary constraint.
>
> > [!note]- Full proof
> > Differentiate $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$ with respect to $\dot x^\nu$:
> > $$\frac{\partial L}{\partial\dot x^\nu} + \dot x^\mu\frac{\partial^2 L}{\partial\dot x^\mu\partial\dot x^\nu} = \frac{\partial L}{\partial\dot x^\nu}.$$
> > Cancelling $\partial L/\partial\dot x^\nu$ from both sides leaves $\dot x^\mu W_{\mu\nu} = 0$, where $W_{\mu\nu} = \partial^2 L/\partial\dot x^\mu\partial\dot x^\nu$. Thus the nonzero vector $\dot x^\mu$ lies in the kernel of $W$, so $W$ is singular, $\det W = 0$. Since $\partial p_\mu/\partial\dot x^\nu = W_{\mu\nu}$, the map $\dot x \mapsto p$ has singular Jacobian and is not (locally) invertible. $\blacksquare$

> [!note]- Lemma 3: The primary constraint
> **Statement:** The momenta satisfy $\eta^{\mu\nu}p_\mu p_\nu = m^2c^2$ (free), or $\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu) = m^2c^2$ (charged).
>
> **Hint:** Use $P = mcU$ (or $P = mcU + \tfrac{q}{c}A$) and the four-velocity normalisation $U\cdot U = c^2$.
>
> **Why needed:** It is the explicit relation among momenta that the non-invertibility guarantees, and the object that gets quantised.
>
> > [!note]- Full proof
> > *Free particle:* $p_\mu = mc\,u_\mu$ (from [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]), so $\eta^{\mu\nu}p_\mu p_\nu = m^2c^2\,\eta^{\mu\nu}u_\mu u_\nu = m^2c^2\,(U\cdot U) = m^2c^2$, using $U\cdot U = c^2$ (with $c=1$: $= m^2$). *Charged particle:* $p_\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$, so $p_\mu - \tfrac{q}{c}A_\mu = mc\,u_\mu$, and the same computation gives $\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu) = m^2c^2$. (In Gourgoulhon's mostly-plus signature both right sides are $-m^2c^2$.) $\blacksquare$

> [!note]- Lemma 4: Dirac's Hamiltonian reproduces the dynamics
> **Statement:** For $H = \tfrac{1}{2m}\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu)$, Hamilton's equations give $\dot x^\mu = U^\mu$ (so $\lambda = \tau$) and $mc^2 a_\mu = qF_{\mu\nu}U^\nu$.
>
> **Hint:** Compute $\partial H/\partial p_\mu$ and $\partial H/\partial x^\mu$; the first identifies $\dot x^\mu$ with the kinetic momentum over $m$.
>
> **Why needed:** It shows the constraint-proportional Hamiltonian, despite its constant value, generates the correct equations of motion.
>
> > [!note]- Full proof
> > Write $\pi_\mu := p_\mu - \tfrac{q}{c}A_\mu$ for the kinetic momentum, so $H = \tfrac{1}{2m}\eta^{\mu\nu}\pi_\mu\pi_\nu$. The first canonical equation:
> > $$\dot x^\mu = \frac{\partial H}{\partial p_\mu} = \frac{1}{m}\eta^{\mu\nu}\pi_\nu = \frac{1}{m}\pi^\mu.$$
> > Since $\pi_\mu = mc\,u_\mu$ on the physical motion, $\dot x^\mu = c\,u^\mu = c\,U^\mu$; choosing units so this reads $\dot x^\mu = U^\mu$ identifies the parameter with proper time, $\lambda = \tau$. The second canonical equation, $\dot p_\mu = -\partial H/\partial x^\mu = -\tfrac{1}{m}\eta^{\nu\rho}\pi_\nu\,\partial_\mu(-\tfrac{q}{c}A_\rho) = \tfrac{q}{mc}\pi^\rho\,\partial_\mu A_\rho$, combined with $\dot p_\mu = m\,\dot u_\mu + \tfrac{q}{c}\dot A_\mu = m\,\dot u_\mu + \tfrac{q}{c}(\partial_\rho A_\mu)\dot x^\rho$, yields after rearrangement $mc^2 a_\mu = q(\partial_\mu A_\nu - \partial_\nu A_\mu)U^\nu = qF_{\mu\nu}U^\nu$, the Lorentz force. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — homogeneity.** The Lagrangian is homogeneous of degree one in $\dot x^\mu$, so Euler's identity $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$ holds, and $p_\mu := \partial L/\partial\dot x^\mu$ is defined.
>
> **Part 1 — vanishing canonical Hamiltonian.** By Lemma 1, $H_{\text{naive}} = p_\mu\dot x^\mu - L = \dot x^\mu\,\partial L/\partial\dot x^\mu - L = 0$.
>
> **Part 2 — non-invertibility and constraint.** By Lemma 2, differentiating Euler's identity gives $\dot x^\mu\,\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu = 0$, so the Hessian is singular and the Legendre map $\dot x \mapsto p$ is non-invertible. By Lemma 3, the momenta therefore satisfy the primary constraint $\eta^{\mu\nu}p_\mu p_\nu = m^2c^2$ (free) or $\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu) = m^2c^2$ (charged).
>
> **Part 3 — Dirac's resolution.** Take $H = \tfrac{1}{2m}\eta^{\mu\nu}(p_\mu - \tfrac{q}{c}A_\mu)(p_\nu - \tfrac{q}{c}A_\nu)$. By the constraint its value on the motion is $\tfrac{1}{2m}\cdot m^2c^2 = \tfrac{m}{2}c^2$, constant. By Lemma 4, Hamilton's equations $\dot x^\mu = \partial H/\partial p_\mu$, $\dot p_\mu = -\partial H/\partial x^\mu$ give $\dot x^\mu = U^\mu$ (fixing $\lambda = \tau$) and $mc^2 a_\mu = qF_{\mu\nu}U^\nu$, the Lorentz-force equation of motion. Setting $q = 0$ recovers the free particle, with $H = \tfrac{1}{2m}\eta^{\mu\nu}p_\mu p_\nu$ and straight-line motion.
>
> **Corollary — energy Hamiltonian.** Parametrise by $\lambda = t$, an inertial observer's time. The Lagrangian $L = -mc^2\sqrt{1 - \mathbf{v}^2/c^2}$ is a non-degenerate function of $\mathbf{v}$ (its Hessian in $\mathbf{v}$ is invertible), so $\mathbf{p} = \partial L/\partial\mathbf{v} = m\gamma\mathbf{v}$ is invertible for $\mathbf{v}$, and $H = \mathbf{p}\cdot\mathbf{v} - L = m\gamma c^2 = \sqrt{\mathbf{p}^2c^2 + m^2c^4}$. With a vector field, $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2c^2 + m^2c^4} + q\phi$ (charge $q$, scalar potential $\phi = A_0$). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Hamiltonian constraint of general relativity.** General relativity, being invariant under arbitrary spacetime coordinate changes, has a Hamiltonian that is a *sum of constraints* — the famous Hamiltonian and momentum constraints of the ADM formulation — and its total Hamiltonian vanishes on physical configurations, exactly as for the relativistic particle. The "problem of time" in quantum gravity (the Wheeler–DeWitt equation $\hat H|\Psi\rangle = 0$) is the field-theoretic version of $H \equiv 0$ here. The application is the deepest descendant of this theorem: diffeomorphism invariance forces a vanishing Hamiltonian, and the relativistic particle is the finite-dimensional model. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

**The relativistic string and the Polyakov action.** Replacing the worldline by a worldsheet, the Nambu–Goto action is the area (the two-dimensional analogue of proper-time length), reparametrisation-invariant in two parameters, with a vanishing Hamiltonian and the Virasoro constraints as its primary constraints. The einbein of the particle becomes the worldsheet metric of the Polyakov action. The application generalises the entire structure of this theorem from one to two worldsheet dimensions; the relativistic particle is "string theory in zero spatial dimensions."

**Geodesic flow as a Hamiltonian system.** On any (pseudo-)Riemannian manifold, the geodesic flow is the Hamiltonian flow of $H = \tfrac{1}{2}g^{\mu\nu}p_\mu p_\nu$ on the cotangent bundle — precisely the free Dirac Hamiltonian. The relativistic free particle is the geodesic flow of the flat metric, and the conserved quantities (energy, momentum) are the Poisson-commuting integrals of this flow. The application connects this theorem to the [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|symplectic]] theory of integrable systems; see [[Ex - Geodesic Flow on a Riemannian Manifold is Hamiltonian]].

---

# Bridges

- **[[Def - The Legendre Transform|The Legendre transform]]** — this theorem is a case study in the *failure* of the Legendre transform when the Lagrangian is degenerate. In [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|geometric mechanics]], the [[Thm - Equivalence of Lagrangian and Hamiltonian Formalisms|equivalence of the Lagrangian and Hamiltonian pictures]] requires the fibre derivative $\dot q \mapsto p$ to be a diffeomorphism, i.e. a non-degenerate Hessian. The relativistic free Lagrangian violates exactly this condition; its fibre derivative maps onto the mass-shell constraint surface rather than onto all of phase space. Dirac's constrained-Hamiltonian theory is the general machinery for degenerate Legendre transforms, and the relativistic particle is its simplest non-trivial instance — the canonical example separating regular from singular Lagrangian systems.

- **[[Def - Poisson Bracket|The Poisson bracket]] and symplectic phase space** — once a Hamiltonian (the Dirac or energy form) is in hand, the relativistic particle lives in the [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|symplectic]] world: phase space is the cotangent bundle $T^*M$ with $\omega = dp_\mu\wedge dx^\mu$, the observables form a Poisson algebra, and the dynamics is the Hamiltonian flow $\iota_{X_H}\omega = dH$. The primary constraint $P\cdot P - m^2$ is a *first-class* constraint: its Poisson bracket with itself vanishes, marking it as the generator of the reparametrisation gauge symmetry. The reduced (gauge-fixed) phase space, six-dimensional, carries the genuine degrees of freedom. This is the constrained-Hamiltonian instance of the general symplectic framework.

- **Systems of particles: the Tetrode–Fokker action and Wheeler–Feynman electrodynamics** — extending to $N$ particles requires $N$ separate time parameters $\lambda_a$, and the most general interacting action is the **Tetrode–Fokker** action
  $$S = -\sum_a m_a c\!\int\!\sqrt{\eta_{\mu\nu}\dot x_a^\mu\dot x_a^\nu}\,d\lambda_a + \sum_{a<b} q_a q_b\!\iint\! K(x_a, \dot x_a, x_b, \dot x_b)\,d\lambda_a\,d\lambda_b,$$
  the sum of free actions plus a double integral describing **action at a distance** with no intervening field. Choosing the kernel $K$ with a light-cone delta function $\delta\big(\eta_{\mu\nu}(x_a - x_b)^\mu(x_a - x_b)^\nu\big)$ makes the interaction propagate at the speed of light along both sheets of the null cone; the vectorial choice $K = \tfrac{1}{4\pi}\eta_{\mu\nu}\dot x_a^\mu\dot x_b^\nu\,\delta(\dots)$ gives **Wheeler–Feynman electrodynamics**, which (ignoring radiation reaction) is physically equivalent to Maxwell theory with the half-sum of retarded and advanced [[Special Relativity XXII — Maxwell's Equations|Liénard–Wiechert potentials]]. Because the double sum has $b \neq a$, there is no self-interaction and hence none of the self-energy divergences of field theory (Gourgoulhon's Remark 11.14); radiation reaction is recovered by including absorber charges at the periphery. The equations of motion are **integro-differential**, not a Cauchy problem, so uniqueness from initial data is lost — the price of dispensing with the field.

- **The no-interaction theorem** — at the Hamiltonian level a sharp obstruction appears. A *relativistic Hamiltonian theory* consists of a phase space with a Poisson bracket and an action of the [[Def - The Poincaré Group|Poincaré group]] by canonical transformations. The **no-interaction theorem** (Currie–Jordan–Sudarshan, 1963) proves that two conditions are incompatible unless the particles do not interact: (i) the Hamiltonian structure is Poincaré-invariant, and (ii) the particles' spacetime positions are the canonical coordinates. Interaction, relativity, and "position is canonical" cannot all hold at once. The resolution — the *a priori* Hamiltonian formalism of Droz-Vincent — abandons (ii), letting the canonical coordinates be abstract phase-space variables distinct from the literal positions. This theorem marks the boundary of the particle picture: relativistic interaction pushes one toward fields, which mediate the interaction locally and restore a well-posed initial-value problem.

---

# Unlocked by This

> [!tip] The Problem of Time in Quantum Gravity *(from General Relativity and Quantum Gravity)*
> The vanishing Hamiltonian $H \equiv 0$ of this reparametrisation-invariant theory is the finite-dimensional model of the central difficulty of canonical quantum gravity. General relativity, invariant under arbitrary spacetime diffeomorphisms, has a Hamiltonian that is a sum of constraints, and its quantum version is the **Wheeler–DeWitt equation** $\hat H|\Psi\rangle = 0$ — a "Schrödinger equation with no time on the right-hand side." The **problem of time** is how to recover dynamics and an arrow of time from a theory whose Hamiltonian vanishes. The relativistic particle exhibits the difficulty in miniature and resolves it: the genuine evolution is gauge-fixed (here $\lambda = \tau$), and the physical content lives on the constraint surface. Understanding why $H \equiv 0$ here is the first step toward understanding quantum gravity.

> [!tip] Worldline Quantum Field Theory *(from Quantum Field Theory)*
> Quantising the relativistic particle by the path integral over worldlines, $\int\mathcal{D}x\,e^{iS}$, with the action of this chapter, gives the **worldline formalism** for the propagator of a relativistic particle — Feynman's original "sum over paths" for a relativistic field. The mass-shell constraint becomes the propagator's pole at $p^2 = m^2$; the einbein integral produces the Schwinger proper-time representation $\int_0^\infty ds\,e^{-s(p^2 + m^2)}$. This worldline picture is an efficient alternative to Feynman diagrams for computing loop amplitudes, and it is the conceptual seed of string perturbation theory, where the worldline becomes a worldsheet. The constrained Hamiltonian structure derived here is what the quantisation must respect.
