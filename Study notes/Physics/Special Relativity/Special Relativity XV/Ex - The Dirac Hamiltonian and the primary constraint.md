---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Hamiltonian Formulation (Relativistic Particle)"
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
  - "Def - Relativistic Action of a Free Particle"
  - "Def - The Legendre Transform"
tags: [physics, special-relativity]
---

# Problem Statement

Consider the manifestly covariant free Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ (with $c = 1$), parametrised by an arbitrary $\lambda$.

1. Show that the naive Hamiltonian $H = p_\mu\dot x^\mu - L$ vanishes identically, and explain why in terms of Euler's homogeneity identity.
2. Show that the Legendre map $\dot x^\mu \mapsto p_\mu = \partial L/\partial\dot x^\mu$ is **not invertible** by computing the Hessian $\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu$ and exhibiting $\dot x^\mu$ in its kernel. Derive the resulting **primary constraint** $\eta^{\mu\nu}p_\mu p_\nu = m^2$.
3. Following Dirac, adopt the constraint Hamiltonian $H = \tfrac{1}{2m}\eta^{\mu\nu}p_\mu p_\nu$ and show that Hamilton's equations $\dot x^\mu = \partial H/\partial p_\mu$, $\dot p_\mu = -\partial H/\partial x^\mu$ reproduce free motion and fix $\lambda = \tau$.
4. Explain conceptually why the canonical Hamiltonian vanishes — what is the gauge symmetry, and what does $H \equiv 0$ mean physically?

**Recall:**

![[Thm - Hamiltonian Formulation (Relativistic Particle)#Statement]]

A Lagrangian homogeneous of degree one in $\dot x^\mu$ satisfies Euler's identity $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$ ([[Def - Relativistic Action of a Free Particle]]). The [[Def - The Legendre Transform|Legendre transform]] $H = p_\mu\dot x^\mu - L$ requires the map $\dot x \mapsto p$ to be invertible, i.e. a non-degenerate Hessian. The relativistic free Lagrangian violates this, and the resolution is Dirac's constraint Hamiltonian; see [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]].

---

# Convergent Strategy

**Problem class.** A *diagnose-a-degeneracy* problem: show that a reparametrisation-invariant Lagrangian has a vanishing canonical Hamiltonian and a primary constraint, then resolve the difficulty by Dirac's method. This is the subtle Hamiltonian case flagged in the [[Special Relativity XV — The Principle of Least Action#Problem-Solving Strategy|topic strategy]].

**Assumption pattern.** The Lagrangian is the manifestly covariant free one, *homogeneous of degree one* in $\dot x^\mu$. This single property — via Euler's identity — simultaneously causes the vanishing Hamiltonian, the non-invertible Legendre map, and the primary constraint. Recognising the homogeneity is the trigger that predicts all three pathologies.

**Theorem routing.** Euler's identity (from [[Def - Relativistic Action of a Free Particle|the free Lagrangian]]'s homogeneity) gives $H_{\text{naive}} = 0$ directly; differentiating it gives the singular Hessian, hence non-invertibility and the constraint $P\cdot P = m^2$; and [[Thm - Hamiltonian Formulation (Relativistic Particle)|Dirac's resolution]] supplies a working Hamiltonian proportional to the constraint, verified by Hamilton's equations.

**Key decision point.** The conceptual crux is interpreting $H \equiv 0$ not as a failure but as the signature of the reparametrisation gauge symmetry: in a theory with no absolute time, $\lambda$-evolution is gauge, so its generator (the Hamiltonian) must vanish. The technical crux is realising that Dirac's Hamiltonian, despite having the *constant value* $\tfrac{m}{2}$ on the motion, has a *non-trivial functional form* in $(x, p)$ that drives Hamilton's equations — the value and the functional dependence are different things.

---

# Legal Operations Used

1. **Perform the Legendre transform — carefully** (operation 6 from the topic page). Recognise that the naive transform fails for the degree-one homogeneous Lagrangian and switch to Dirac's constraint Hamiltonian.

2. **Use Euler's homogeneity identity** (operation 2). The identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ gives $H_{\text{naive}} = 0$, and its derivative gives the singular Hessian.

3. **Compute the generalized four-momentum** (operation 5). $p_\mu = m u_\mu$, satisfying the primary constraint $\eta^{\mu\nu}p_\mu p_\nu = m^2$.

4. **Choose the parameter last** (operation 7). The Dirac Hamiltonian's equations *select* $\lambda = \tau$ rather than requiring it as input.

---

# Hints

> [!note]- Hint 1
> $H_{\text{naive}} = p_\mu\dot x^\mu - L = \dot x^\mu\,\partial L/\partial\dot x^\mu - L$. By Euler's identity for the degree-one homogeneous $L$, $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$, so $H_{\text{naive}} = L - L = 0$.

> [!note]- Hint 2
> Compute $\partial L/\partial\dot x^\mu = -m\,\eta_{\mu\nu}\dot x^\nu/\sqrt{w}$ with $w = \eta_{\rho\sigma}\dot x^\rho\dot x^\sigma$. Differentiate again: $\partial^2 L/\partial\dot x^\mu\partial\dot x^\nu = -m[\eta_{\mu\nu}/\sqrt{w} - \eta_{\mu\rho}\dot x^\rho\eta_{\nu\sigma}\dot x^\sigma/w^{3/2}]$. Contract with $\dot x^\nu$ to verify it vanishes. The constraint: $p_\mu = m u_\mu$, so $\eta^{\mu\nu}p_\mu p_\nu = m^2 u_\mu u^\mu = m^2$.

> [!note]- Hint 3
> For $H = \tfrac{1}{2m}\eta^{\mu\nu}p_\mu p_\nu$: $\dot x^\mu = \partial H/\partial p_\mu = \tfrac{1}{m}\eta^{\mu\nu}p_\nu = \tfrac{1}{m}p^\mu = u^\mu = U^\mu$ (using $p^\mu = m u^\mu$), which identifies $\dot x^\mu$ with the unit four-velocity, fixing $\lambda = \tau$. And $\dot p_\mu = -\partial H/\partial x^\mu = 0$ (no $x$-dependence), so $p_\mu$ constant — free motion.

> [!note]- Hint 4
> The gauge symmetry is *reparametrisation* of the worldline: shifting $\lambda \to \lambda + \epsilon(\lambda)$ is not a physical change. The Hamiltonian generates $\lambda$-evolution; since $\lambda$-evolution is gauge (unphysical), its generator must vanish on the physical phase space. $H \equiv 0$ means "there is no absolute time, only the gauge parameter $\lambda$."

---

# Solution

The solution exhibits the three pathologies and then resolves them. Step 1 shows the naive Hamiltonian vanishes. Step 2 computes the Hessian, shows it is singular, and derives the primary constraint. Step 3 verifies Dirac's constraint Hamiltonian reproduces the dynamics. Step 4 interprets $H \equiv 0$ as the reparametrisation gauge symmetry. Throughout, the single source of every effect is the degree-one homogeneity of the Lagrangian.

**Step 1: The naive Hamiltonian vanishes.**

> [!note]- Derivation
> The generalized momentum is $p_\mu = \partial L/\partial\dot x^\mu$, so $p_\mu\dot x^\mu = \dot x^\mu\,\partial L/\partial\dot x^\mu$. The free Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ is homogeneous of degree one in $\dot x^\mu$: $L(\mu\dot x) = \mu L(\dot x)$ for $\mu > 0$. Euler's theorem on homogeneous functions then gives
> $$\dot x^\mu\frac{\partial L}{\partial\dot x^\mu} = L.$$
> Therefore the naive Hamiltonian
> $$H_{\text{naive}} = p_\mu\dot x^\mu - L = \dot x^\mu\frac{\partial L}{\partial\dot x^\mu} - L = L - L = 0$$
> vanishes identically — not on a particular solution, but as an algebraic identity for every worldline. A Hamiltonian that is zero everywhere generates no evolution; the naive recipe has failed.

**Step 2: The Legendre map is non-invertible; the primary constraint.**

> [!note]- Derivation
> Compute the momentum and the Hessian. With $w = \eta_{\rho\sigma}\dot x^\rho\dot x^\sigma$,
> $$p_\mu = \frac{\partial L}{\partial\dot x^\mu} = -m\,\frac{\eta_{\mu\nu}\dot x^\nu}{\sqrt{w}}, \qquad W_{\mu\nu} := \frac{\partial^2 L}{\partial\dot x^\mu\partial\dot x^\nu} = -m\Big[\frac{\eta_{\mu\nu}}{\sqrt{w}} - \frac{(\eta_{\mu\rho}\dot x^\rho)(\eta_{\nu\sigma}\dot x^\sigma)}{w^{3/2}}\Big].$$
> Contract the Hessian with $\dot x^\nu$:
> $$W_{\mu\nu}\dot x^\nu = -m\Big[\frac{\eta_{\mu\nu}\dot x^\nu}{\sqrt{w}} - \frac{(\eta_{\mu\rho}\dot x^\rho)(\eta_{\nu\sigma}\dot x^\sigma\dot x^\nu)}{w^{3/2}}\Big] = -m\Big[\frac{\eta_{\mu\nu}\dot x^\nu}{\sqrt{w}} - \frac{(\eta_{\mu\rho}\dot x^\rho)\,w}{w^{3/2}}\Big] = 0,$$
> using $\eta_{\nu\sigma}\dot x^\sigma\dot x^\nu = w$. So $\dot x^\mu$ lies in the kernel of $W$: the Hessian is singular, $\det W = 0$, and the Legendre map $\dot x \mapsto p$ (whose Jacobian is $W$) is **not invertible**. The four momenta therefore cannot be four independent functions of the four velocities — they satisfy a relation, the **primary constraint**. Compute it: $p_\mu = m u_\mu$ with $u_\mu = \eta_{\mu\nu}\dot x^\nu/\sqrt{w} = \eta_{\mu\nu}U^\nu$ and $U\cdot U = 1$, so
> $$\eta^{\mu\nu}p_\mu p_\nu = m^2\,\eta^{\mu\nu}u_\mu u_\nu = m^2\,(U\cdot U) = m^2.$$
> This is the **mass-shell constraint** $P\cdot P = m^2$: the momenta lie on a three-dimensional surface in four-dimensional momentum space, the geometric reason for the non-invertibility.

**Step 3: Dirac's Hamiltonian reproduces the dynamics.**

> [!note]- Derivation
> Following Dirac, take the Hamiltonian *proportional to the constraint*:
> $$H = \frac{1}{2m}\eta^{\mu\nu}p_\mu p_\nu = \frac{1}{2m}p_\mu p^\mu.$$
> On the physical motion its value is $\tfrac{1}{2m}m^2 = \tfrac{m}{2}$, a constant — but its *functional dependence* on $(x^\mu, p_\mu)$ is non-trivial, and that is what drives Hamilton's equations. The first canonical equation:
> $$\dot x^\mu = \frac{\partial H}{\partial p_\mu} = \frac{1}{m}\eta^{\mu\nu}p_\nu = \frac{1}{m}p^\mu.$$
> Since $p^\mu = m U^\mu$ on the physical motion, $\dot x^\mu = U^\mu$, the unit four-velocity. But $\dot x^\mu = dx^\mu/d\lambda$, and $dx^\mu/d\tau = U^\mu$ by definition, so $\dot x^\mu = U^\mu$ forces $d\lambda = d\tau$: the Dirac Hamiltonian *selects the proper time as parameter*, $\lambda = \tau$ — a gauge-fixing that the formalism performs automatically. The second canonical equation:
> $$\dot p_\mu = -\frac{\partial H}{\partial x^\mu} = 0,$$
> since $H = \tfrac{1}{2m}p_\mu p^\mu$ has no explicit $x$-dependence. So $p_\mu = \text{const}$, the four-momentum is conserved, and the worldline is straight (free motion). The constraint Hamiltonian, despite its constant value, generates exactly the free dynamics and fixes the parameter.

**Step 4: Why the canonical Hamiltonian vanishes.**

> [!note]- Derivation
> The vanishing of $H_{\text{naive}}$ is the fingerprint of a **gauge symmetry**: the reparametrisation invariance of the worldline. The action $S = -m\int\sqrt{\eta\dot x\dot x}\,d\lambda$ depends only on the worldline as a geometric curve, not on the parameter $\lambda$; shifting $\lambda \to \lambda + \epsilon(\lambda)$ (a relabelling of the points along the curve) is a symmetry that depends on an *arbitrary function* — the definition of a local gauge symmetry. The Hamiltonian is the generator of $\lambda$-evolution; but $\lambda$-evolution is precisely the gauge transformation, an *unphysical* relabelling, so its generator must vanish on the physical phase space. $H \equiv 0$ is the statement "there is no preferred time in this theory; the parameter $\lambda$ is pure gauge." The genuine, physical evolution is the relation among the three physical degrees of freedom, recovered by *gauge-fixing* — choosing a parameter, as the Dirac Hamiltonian does by selecting $\lambda = \tau$. This is not a pathology but a precise reflection of the absence of absolute time, and it is the finite-dimensional model of the vanishing Hamiltonian of general relativity (the Wheeler–DeWitt equation $\hat{H}|\Psi\rangle = 0$), where diffeomorphism invariance forces the same structure.

> [!note]- Complete formal solution
> *Vanishing Hamiltonian:* $H_{\text{naive}} = p_\mu\dot x^\mu - L = \dot x^\mu\partial L/\partial\dot x^\mu - L = L - L = 0$ by Euler's identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ (degree-one homogeneity). *Non-invertibility:* the Hessian $W_{\mu\nu} = -m[\eta_{\mu\nu}/\sqrt{w} - (\eta_{\mu\rho}\dot x^\rho)(\eta_{\nu\sigma}\dot x^\sigma)/w^{3/2}]$ satisfies $W_{\mu\nu}\dot x^\nu = 0$, so $\det W = 0$ and $\dot x \mapsto p$ is non-invertible; the momenta obey the primary constraint $\eta^{\mu\nu}p_\mu p_\nu = m^2 u_\mu u^\mu = m^2$. *Dirac's resolution:* with $H = \tfrac{1}{2m}p_\mu p^\mu$, Hamilton's equations give $\dot x^\mu = p^\mu/m = U^\mu$ (fixing $\lambda = \tau$) and $\dot p_\mu = 0$ (free motion); the value $H = m/2$ is constant but the functional form drives the dynamics. *Interpretation:* $H \equiv 0$ is the signature of the worldline reparametrisation gauge symmetry — $\lambda$-evolution is unphysical gauge, so its generator vanishes; physical evolution is recovered by gauge-fixing. $\blacksquare$

---

# Key Takeaways

**Degree-one homogeneity causes the vanishing Hamiltonian, the non-invertible Legendre map, and the constraint — three symptoms of one disease.** The entire structure of this exercise traces to the single fact that the covariant Lagrangian is homogeneous of degree one in $\dot x^\mu$. Euler's identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ gives the vanishing Hamiltonian directly; differentiating it gives the singular Hessian (hence the non-invertible Legendre map); and the non-invertibility forces a relation among the momenta (the mass-shell constraint). These are not three separate problems but one, viewed from three angles, and recognising the homogeneity lets you predict all of them before any calculation. The reusable diagnostic: whenever a Lagrangian is homogeneous of degree one in its velocities — the hallmark of a reparametrisation-invariant action — expect a vanishing canonical Hamiltonian and primary constraints, and plan to use Dirac's method or to break the covariance. This pattern recurs in every reparametrisation-invariant theory: the relativistic string, general relativity, and any geometric action built from an arc length or volume.

**The Dirac Hamiltonian has a constant value but a non-trivial functional form, and the distinction is everything.** Dirac's resolution looks paradoxical: the Hamiltonian $H = \tfrac{1}{2m}p_\mu p^\mu$ equals the constant $\tfrac{m}{2}$ on the physical motion, yet it generates non-trivial dynamics. The resolution is that Hamilton's equations involve the *partial derivatives* $\partial H/\partial p_\mu$ and $\partial H/\partial x^\mu$, which depend on the *functional form* of $H$ in the phase-space variables, not on its numerical value along a trajectory. A function can be constant on a particular surface (the mass shell) while having non-zero gradients off it, and it is those gradients that drive the flow. The reusable insight is to distinguish a Hamiltonian's value (often fixed by a constraint) from its functional dependence (which generates the equations of motion); in constrained systems these are routinely different, and conflating them is a common error. The same point underlies the Hamiltonian of general relativity, which vanishes on physical configurations but whose functional form generates the Einstein evolution.

**The vanishing Hamiltonian is the absence of absolute time, and gauge-fixing restores dynamics.** The deepest lesson is conceptual: $H \equiv 0$ is not a failure of the formalism but a precise statement that the theory has no preferred time — the parameter $\lambda$ is pure gauge, a relabelling of worldline points, and the generator of its evolution must therefore vanish. Physical evolution lives in the relations among the genuine degrees of freedom and is recovered by *gauge-fixing*: choosing a parameter (the Dirac Hamiltonian automatically selects $\lambda = \tau$). This is the simplest instance of the "problem of time" that dominates canonical quantum gravity, where general covariance forces a vanishing Hamiltonian and the Wheeler–DeWitt equation $\hat{H}|\Psi\rangle = 0$ replaces the time-dependent Schrödinger equation. Understanding why $H \equiv 0$ for the humble relativistic particle — and how gauge-fixing recovers ordinary dynamics — is the first and most transferable step toward understanding constrained quantisation and quantum gravity. For the non-covariant route that sidesteps the constraint by yielding $H = \sqrt{\mathbf{p}^2 + m^2}$ directly, see [[Ex - Legendre transform to the relativistic Hamiltonian]].
