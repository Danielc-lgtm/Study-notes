---
type: definition
subject: special-relativity
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Worldline of a Particle"
  - "Thm - Inertial Worldlines Maximise Proper Time"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike worldline has $\eta_{\mu\nu}\dot x^\mu\dot x^\nu > 0$ and proper time $d\tau = \sqrt{\eta_{\mu\nu}\,dx^\mu dx^\nu}$ (with $c$: $d\tau = c^{-1}\sqrt{\eta_{\mu\nu}\,dx^\mu dx^\nu}$). The source (Gourgoulhon) uses mostly-plus $\mathrm{diag}(-1,+1,+1,+1)$, where the same action reads $S = -mc\int\sqrt{-g_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda$ with timelike $\dot x\cdot\dot x < 0$. A particle $\mathcal{P}$ of rest mass $m$ has worldline $\mathcal{L}: x^\mu = x^\mu(\lambda)$, with $\lambda$ an arbitrary parameter increasing along $\mathcal{L}$, parameter-velocity $\dot x^\mu = dx^\mu/d\lambda$, and tangent vector $V = \dot x^\mu e_\mu$. The four-velocity is $U = dX/d\tau$, normalised to $U \cdot U = 1$ (with $c$: $U \cdot U = c^2$), with covariant components $u_\mu = \eta_{\mu\nu}U^\nu$. The action between events $A_1$ (parameter $\lambda_1$) and $A_2$ (parameter $\lambda_2$) is $S = \int_{\lambda_1}^{\lambda_2} L\,d\lambda$. Full registry on [[Special Relativity XV — The Principle of Least Action]].

> [!warning] Convention
> Gourgoulhon writes the free action as $S = -mc\int\sqrt{-g_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda = -mc^2\int d\tau$ in mostly-plus signature, where the minus under the root makes the radicand positive for a timelike worldline. In our mostly-minus signature the radicand $\eta_{\mu\nu}\dot x^\mu\dot x^\nu$ is *already* positive for a timelike worldline, so the minus disappears: $S = -mc\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda = -mc^2\int d\tau$. The overall sign $-mc^2$ in front is the *same* in both conventions and is physically meaningful (it makes maximal proper time a minimal action); only the sign inside the square root is signature-dependent.

---

# Axiom Motivation

The two preceding chapters established relativistic dynamics through equations of motion and conservation laws. The goal now is to find the *action* — the single functional whose stationary points are the physical worldlines — because a variational formulation is the gateway to Noether's theorem (symmetries become conservation laws) and to quantum mechanics (the action survives into the path integral). The question is: what number should a free particle make stationary?

The decisive clue is already in hand. We know from [[Thm - Inertial Worldlines Maximise Proper Time|Special Relativity V]] that the inertial worldline between two timelike-separated events is the one of *greatest* [[Def - Proper Time|proper time]] — it is a timelike geodesic, a curve of extremal Lorentzian length. So the free particle already extremises a natural geometric quantity, the proper time. The simplest hypothesis is that the action *is* proportional to proper time, $S = \alpha\int d\tau$, and the only work left is to fix the constant $\alpha$.

Two requirements pin down $\alpha$. First, the action must have the dimensions of an action — energy times time — and proper time already carries the dimension of time, so $\alpha$ must have the dimension of an energy. The only energy available from the single datum of a *free* particle is its rest energy $mc^2$, so $\alpha = \pm mc^2$ up to a dimensionless factor, and we take the simplest choice $|\alpha| = mc^2$. Second, the *sign* must be negative. The principle is conventionally stated as "least action," meaning the physical worldline minimises $S$; but the inertial worldline *maximises* proper time. To turn a maximum of $\int d\tau$ into a minimum of $S$, multiply by a negative number. Hence $\alpha = -mc^2$, and
$$S = -mc^2\int d\tau.$$
The negative sign is not a free convention — it is forced by the demand that "least action" be literally true, given that proper time is maximised. (One could equally adopt the convention "stationary action" and allow either sign; the standard choice $-mc^2$ makes the free-particle action a genuine minimum.)

Now consider what could go wrong if either requirement were relaxed. *If the constant were positive*, $\alpha = +mc^2$: the action would be *maximised* by the physical worldline, contradicting the name "least action" and, more importantly, disagreeing with the path-integral weight $e^{iS/\hbar}$ in which the classical worldline must be a stationary-phase point of the correct character; the sign also fixes the direction of the energy and the boundedness of the Hamiltonian below. *If the proportionality were to coordinate time rather than proper time*, $S = \alpha\int dt$: the action would not be a Lorentz scalar — different observers would assign different actions to the same worldline — and the variational principle would single out a preferred frame, violating the principle of relativity. Proper time is the unique reparametrisation-invariant, frame-independent measure of "length" along a timelike worldline, which is exactly why it must be the integrand.

There is a final, structural requirement that the proper-time form satisfies automatically and that any candidate action must obey: **reparametrisation invariance**. A worldline is a geometric object — a curve in spacetime — and the action must depend only on the curve, not on the arbitrary parameter $\lambda$ used to describe it. Writing $d\tau = \sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$, the action becomes $S = \int L\,d\lambda$ with $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$, and one checks that under a change of parameter $\lambda \to \tilde\lambda$ the Lagrangian rescales exactly so that $L\,d\lambda$ is invariant. This forces $L$ to be a **positive homogeneous function of degree one** in $\dot x^\mu$: $L(x, \mu\dot x) = \mu L(x, \dot x)$ for all $\mu > 0$. The square root is precisely such a function. Were $L$ *not* homogeneous of degree one — say the naive $\tfrac{1}{2}m\eta_{\mu\nu}\dot x^\mu\dot x^\nu$, homogeneous of degree two — the action would change value under reparametrisation, and "the value of $S$ on a worldline" would be ill-defined. Homogeneity of degree one is the algebraic price of having no absolute time to parametrise by, and it has far-reaching consequences (the vanishing of the canonical Hamiltonian, the existence of a primary constraint) explored in [[Thm - Hamiltonian Formulation (Relativistic Particle)]].

---

# The Definition

The **action of a free particle** of rest mass $m$ between two events $A_1, A_2$ of its [[Def - Worldline of a Particle|worldline]] $\mathcal{L}$ is
$$S \;=\; -mc^2\!\int_{A_1}^{A_2} d\tau \;=\; -mc^2\,(\tau_2 - \tau_1),$$
the elapsed [[Def - Proper Time|proper time]] multiplied by $-mc^2$. Parametrising $\mathcal{L}$ by an arbitrary parameter $\lambda$ and using $d\tau = c^{-1}\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ (mostly-minus; Gourgoulhon's $c^{-1}\sqrt{-g_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda$), the action takes the form $S = \int_{\lambda_1}^{\lambda_2} L\,d\lambda$ with **Lagrangian**
$$\boxed{\,L(x^\mu, \dot x^\mu) \;=\; -mc\,\sqrt{\eta_{\mu\nu}\,\dot x^\mu\dot x^\nu}\,}\qquad(c=1:\ L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}).$$
This $L$ is a **positive homogeneous function of degree one** in the parameter-velocities, $L(x, \mu\dot x) = \mu L(x, \dot x)$ for all $\mu > 0$, which makes the action **reparametrisation-invariant** (its value depends only on the worldline, not on $\lambda$). By Euler's theorem on homogeneous functions, this homogeneity is equivalent to the identity
$$\dot x^\mu\,\frac{\partial L}{\partial \dot x^\mu} \;=\; L.$$

Relative to an inertial observer $\mathcal{O}$, choosing the parameter $\lambda = t$ ($\mathcal{O}$'s proper time) and writing the particle's velocity relative to $\mathcal{O}$ as $\mathbf{v}$, the Lagrangian becomes the form found in introductory textbooks,
$$L \;=\; -mc^2\sqrt{1 - \frac{\mathbf{v}\cdot\mathbf{v}}{c^2}} \;=\; -\frac{mc^2}{\gamma},$$
where $\gamma = (1 - \mathbf{v}^2/c^2)^{-1/2}$. This is **not** of the form (kinetic energy) $-$ (potential energy); the relativistic free Lagrangian is the negative rest energy divided by the Lorentz factor, and its low-velocity expansion $L \approx -mc^2 + \tfrac{1}{2}m\mathbf{v}^2$ recovers the Newtonian kinetic energy $\tfrac{1}{2}m\mathbf{v}^2$ (the constant $-mc^2$ does not affect the equations of motion).

---

# Relate to Other Fields / Compression

This definition is the Lorentzian instance of a general construction in [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles|Riemannian geometry]]: the **length functional** of a metric, $\int\sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$, whose stationary curves are the geodesics. The free action is exactly this functional for the flat indefinite metric $\eta$, weighted by $-mc$. In the Riemannian (positive-definite) case the stationary curve is the *shortest* path; in the Lorentzian case, because the metric is indefinite, the timelike stationary curve is the *longest* in proper time — the sign flip that distinguishes [[Thm - Inertial Worldlines Maximise Proper Time|maximal-proper-time geodesics]] from minimal-length ones.

**True name:** the free action is *proper time, signed so that geodesics are maximal*. The operational content is not the formula $-mc^2\int d\tau$ but the statement "the free particle extremises its proper time, and the extremum is a maximum." This is what lets you predict the equation of motion (geodesic), the conservation laws (from the symmetries of proper time, which are the Poincaré symmetries of $\eta$), and the sign conventions of the whole formalism, all from one sentence. To reconstruct the action from scratch, remember the geometry and supply the dimensional constant $-mc^2$.

The reparametrisation invariance, encoded in the degree-one homogeneity, is the same structural feature that appears in the [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem|integration of one-forms]]: $\int A_\mu dx^\mu$ over a curve is reparametrisation-invariant for the same reason, because $A_\mu \dot x^\mu\,d\lambda = A_\mu\,dx^\mu$ depends only on the curve. A relativistic Lagrangian is, in this light, a one-form on the space of worldline-tangents, and the action is its integral along the worldline.

---

# Examples / Corollaries

**Is an instance — the inertial-observer form.** Taking $\lambda = t$ for an inertial observer reduces $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ to $L = -mc^2\sqrt{1 - \mathbf{v}^2/c^2}$, since $\dot x^0 = c$, $\dot x^i = v^i$, and $\eta_{\mu\nu}\dot x^\mu\dot x^\nu = c^2 - \mathbf{v}^2$. This is the standard textbook free Lagrangian; its parameter $t$ is constrained (it is a specific observer's time), so it is *not* homogeneous of degree one in the three-velocity, and unlike the manifestly covariant form it admits an ordinary, non-degenerate Legendre transform.

**Is an instance — the proper-time parametrisation, and why it is dangerous.** Choosing $\lambda = \tau$ from the start gives $\dot x^\mu = U^\mu$ with $\eta_{\mu\nu}U^\mu U^\nu = c^2$ a constant, so $L = -mc\sqrt{c^2} = -mc^2$ becomes a *constant*. Its Euler–Lagrange equations are the empty statement $0 = 0$. This is correct but useless: the parametrisation $\lambda = \tau$ may be imposed only *after* the equations of motion are derived, never before, because the constraint $U\cdot U = c^2$ restricts the variations (Gourgoulhon's Remark 11.3).

**Is NOT an instance — the degree-two Lagrangian $\tfrac{1}{2}m\eta_{\mu\nu}\dot x^\mu\dot x^\nu$.** The quantity $S' = \int\tfrac{1}{2}m\eta_{\mu\nu}\dot x^\mu\dot x^\nu\,d\lambda$ is *not* the free action, because it is homogeneous of degree *two* in $\dot x^\mu$, hence *not* reparametrisation-invariant: rescaling $\lambda$ changes its value. Its Euler–Lagrange equations do give straight worldlines (it is the "energy functional," and its critical points are affinely-parametrised geodesics), and it is often used as a computational convenience precisely because its Legendre transform is non-degenerate — but it is a *different functional* from the proper-time action, equal to it only when $\lambda$ is already an affine parameter. The distinction matters: $S'$ secretly fixes the parametrisation, while $S$ leaves it free.

**Is NOT an instance — a massless particle.** Setting $m = 0$ makes $S = 0$ identically, so the proper-time action says nothing about photons: a null worldline has $\int d\tau = 0$. A free [[Def - The Four-Momentum of a Photon|photon]] needs a different action (the degree-two einbein form $S = \int \tfrac{1}{2e}\eta_{\mu\nu}\dot x^\mu\dot x^\nu\,d\lambda$ with an auxiliary field $e$, which admits the $m \to 0$ limit), because the geometric notion "proper time along the worldline" degenerates to zero on the light cone. The proper-time action is intrinsically a *massive*-particle construction.

**Corollary — the generalized momentum is the four-momentum.** Differentiating, $\partial L/\partial\dot x^\mu = -mc\,\eta_{\mu\nu}\dot x^\nu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma} = mc\,u_\mu$, so the generalized four-momentum $p_\mu = \partial L/\partial\dot x^\mu = mc\,u_\mu$ equals the covariant components of $P = mcU$ — the [[Def - Four-Momentum and Rest Mass|four-momentum]] of the preceding chapter, with $P\cdot P = m^2c^2$. The variational formalism reproduces, rather than redefines, the four-momentum.

**Calibration check.** Verify that (i) $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ is homogeneous of degree one, $L(x, \mu\dot x) = \mu L(x,\dot x)$ for $\mu > 0$, and confirm the Euler identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ by direct differentiation; (ii) the low-velocity expansion of $-mc^2\sqrt{1-\mathbf{v}^2/c^2}$ is $-mc^2 + \tfrac12 m\mathbf{v}^2 + O(\mathbf{v}^4)$, recovering the Newtonian kinetic energy; (iii) imposing $\lambda = \tau$ before varying collapses $L$ to the constant $-mc^2$ and verify that this gives the empty equation $0 = 0$, so that the proper-time gauge must be fixed only after varying.

---

# Unlocked by This

> [!tip] The Geodesic Action of General Relativity *(from General Relativity)*
> Replacing the flat metric $\eta_{\mu\nu}$ by a curved metric $g_{\mu\nu}(x)$ gives the action $S = -mc\int\sqrt{g_{\mu\nu}(x)\,\dot x^\mu\dot x^\nu}\,d\lambda$ of a free particle in a gravitational field. Its Euler–Lagrange equations are the **geodesic equation** $\ddot x^\mu + \Gamma^\mu_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0$, with the Christoffel symbols arising from the position-dependence of $g_{\mu\nu}$. The flat free action is the $g = \eta$ special case, where $\Gamma = 0$ and the geodesics are straight. This is the precise sense in which "gravity is geometry": a freely-falling body extremises proper time in the curved metric, exactly as the free relativistic particle does in the flat one. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] The Path Integral and the Classical Limit *(from Quantum Mechanics)*
> In the path-integral formulation, the quantum amplitude to propagate from $A_1$ to $A_2$ is a sum over *all* worldlines weighted by $e^{iS/\hbar}$, with $S$ the action of this page. In the limit $\hbar \to 0$, the rapidly oscillating phase cancels except near worldlines where $S$ is stationary — and stationary $S$ is exactly the principle of least action. The classical free worldline is recovered as the stationary-phase point of the quantum sum, and the *sign* of $S = -mc^2\int d\tau$ is what makes the phase oscillate with the correct character. The action defined here is the object that survives into the quantum theory.

> [!tip] The Einbein and the Massless Limit *(from String Theory and Field Theory)*
> The square-root form of the free action is awkward to quantise and degenerates for $m = 0$. An equivalent action introduces an auxiliary worldline field $e(\lambda)$ — the **einbein** — as $S = \tfrac{1}{2}\int\big(e^{-1}\eta_{\mu\nu}\dot x^\mu\dot x^\nu - e\,m^2c^2\big)\,d\lambda$; integrating out $e$ recovers the proper-time action for $m \neq 0$, while the form remains well-defined at $m = 0$, describing massless particles. This einbein trick is the point-particle prototype of the **Polyakov action** of the relativistic string, where the einbein becomes a worldsheet metric. The reparametrisation invariance of the proper-time action becomes the worldsheet diffeomorphism invariance of string theory.
