---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Relativistic Action of a Free Particle"
  - "Thm - Free-Particle Worldline Extremises Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A free particle of rest mass $m$ has action $S = -mc\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$, with $\lambda$ an arbitrary parameter along its worldline and $\dot x^\mu = dx^\mu/d\lambda$. Work with $c = 1$ and the mostly-minus metric $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. Carry out the variation $\delta S = 0$ with the endpoints held fixed, and obtain the Euler–Lagrange equations explicitly.
2. Show that they reduce to $du_\mu/d\lambda = 0$, where $u_\mu = \eta_{\mu\nu}U^\nu$ and $U^\mu = \dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$ is the unit four-velocity, and conclude that the worldline is a straight line.
3. Verify that the four Euler–Lagrange equations are **not independent**: show $\dot x^\mu[\text{EL}]_\mu \equiv 0$. Explain physically why one equation is redundant.
4. Repeat the variation for a general (possibly position-dependent) metric $g_{\mu\nu}(x)$ and show the result is the geodesic equation $\ddot x^\mu + \Gamma^\mu_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0$, identifying the Christoffel symbols. (This is the bridge to general relativity.)

**Recall:**

![[Def - Relativistic Action of a Free Particle#The Definition]]

The four-velocity $U = dX/d\tau$ is the unit-normalised tangent to the worldline, $\eta_{\mu\nu}U^\mu U^\nu = 1$ (with $c$: $= c^2$); see [[Def - Four-Velocity and Four-Acceleration]]. A worldline whose four-velocity is constant is a straight line of Minkowski spacetime, a **timelike geodesic** ([[Thm - Free-Particle Worldline Extremises Proper Time]]). The crucial discipline is to keep $\lambda$ arbitrary throughout the variation and impose the normalisation $U\cdot U = 1$ only afterwards.

---

# Convergent Strategy

**Problem class.** A *derive-an-equation-of-motion-from-an-action* problem, the foundational instance of the [[Special Relativity XV — The Principle of Least Action#Problem-Solving Strategy|topic strategy]]: vary the action, extract the Euler–Lagrange equations, simplify to a recognisable dynamical law. Here the law is the geodesic equation.

**Assumption pattern.** The Lagrangian is the free one, $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$, built from the square root of the Minkowski norm of the parameter-velocity. Its two relevant features are that it has *no explicit position dependence* (the metric is constant) and that it is *homogeneous of degree one* in $\dot x^\mu$. The first makes the Euler–Lagrange equation collapse to conservation of the generalized momentum; the second makes the four equations dependent.

**Theorem routing.** Variation gives the [[Def - Relativistic Action of a Free Particle|Euler–Lagrange equations]]; the absence of position dependence (via [[Thm - Free-Particle Worldline Extremises Proper Time]]) reduces them to $du_\mu/d\lambda = 0$; the homogeneity (Euler's identity) gives the redundancy $\dot x^\mu[\text{EL}]_\mu = 0$; and repeating the variation with $g_{\mu\nu}(x)$ instead of $\eta_{\mu\nu}$ produces the Christoffel terms, the route to the general-relativistic geodesic equation.

**Key decision point.** The non-obvious discipline is to keep $\lambda$ arbitrary and *not* impose $U\cdot U = 1$ before varying. Imposing it first collapses the free Lagrangian to the constant $-m$, whose Euler–Lagrange equations are the empty $0 = 0$; the normalisation must emerge as a consequence of the equations, not be fed in. The second subtlety is recognising the ratio $\dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$ as the unit four-velocity, which is what makes the messy derivative of the square root collapse into the clean statement $du_\mu/d\lambda = 0$.

---

# Legal Operations Used

1. **Vary the action and read off the Euler–Lagrange equations** (operation 1 from the topic page). The first variation with fixed endpoints, after integration by parts, gives $\partial L/\partial x^\mu - \tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$.

2. **Use Euler's homogeneity identity** (operation 2). The degree-one homogeneity of $L$ gives $\dot x^\mu\partial L/\partial\dot x^\mu = L$, from which the redundancy of the four equations follows by differentiation.

3. **Choose the parameter last, and impose $U\cdot U = 1$ a posteriori** (operation 7). Keep $\lambda$ arbitrary while varying; fix $\lambda = \tau$ and the normalisation only after the equations are written.

4. **Compute the generalized four-momentum** (operation 5). The quantity $\partial L/\partial\dot x^\mu = m u_\mu$ is the four-momentum, whose conservation is the equation of motion.

---

# Hints

> [!note]- Hint 1
> Write the Lagrangian as $L = -m\sqrt{w}$ with $w := \eta_{\mu\nu}\dot x^\mu\dot x^\nu$. The variation has a $\partial L/\partial x^\mu$ term and a $\partial L/\partial\dot x^\mu$ term; the first vanishes because $L$ has no explicit $x^\mu$ (the metric is constant). Focus on computing $\partial L/\partial\dot x^\mu$.

> [!note]- Hint 2
> $\partial L/\partial\dot x^\mu = -m\,\eta_{\mu\nu}\dot x^\nu/\sqrt{w}$. Recognise $\dot x^\nu/\sqrt{w} = U^\nu$, the unit four-velocity (it has Minkowski norm $w/w = 1$). So $\partial L/\partial\dot x^\mu = m u_\mu$, and the Euler–Lagrange equation is $d(m u_\mu)/d\lambda = 0$.

> [!note]- Hint 3
> For the redundancy: Euler's identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$, differentiated with respect to $\lambda$, gives $\dot x^\mu[\text{EL}]_\mu = 0$ after subtracting the chain-rule expression for $dL/d\lambda$. Physically, the redundancy is the freedom to reparametrise the worldline: the equations fix the *worldline*, not the *parametrisation*, so one combination of them must be automatically satisfied.

> [!note]- Hint 4
> For the curved metric: now $L = -m\sqrt{g_{\mu\nu}(x)\dot x^\mu\dot x^\nu}$ *does* depend on $x^\mu$ through $g_{\mu\nu}(x)$, so $\partial L/\partial x^\mu = -m\,(\partial_\mu g_{\nu\rho})\dot x^\nu\dot x^\rho/(2\sqrt{w})$ no longer vanishes. Carry through the Euler–Lagrange equation, parametrise by proper time at the end ($w = 1$), and collect the $\partial g$ terms into the symmetric combination $\Gamma^\mu_{\;\nu\rho} = \tfrac12 g^{\mu\sigma}(\partial_\nu g_{\sigma\rho} + \partial_\rho g_{\sigma\nu} - \partial_\sigma g_{\nu\rho})$.

---

# Solution

The proof breaks into four steps. Step 1 varies the action and finds the Euler–Lagrange equations vanish in their $x$-derivative because the flat metric is constant. Step 2 computes the momentum, recognises the four-velocity, and concludes $du_\mu/d\lambda = 0$, a straight line. Step 3 exhibits the redundancy via Euler's identity. Step 4 redoes the calculation for a curved metric, where the surviving $\partial g$ terms assemble into the Christoffel symbols and the geodesic equation. The non-obvious move throughout is keeping $\lambda$ arbitrary and recognising the unit four-velocity inside the derivative of the square root.

**Step 1: The variation gives $\tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$ for the flat metric.**

> [!note]- Derivation
> With $L = -m\sqrt{w}$, $w = \eta_{\mu\nu}\dot x^\mu\dot x^\nu$, the first variation of $S = \int L\,d\lambda$ under $x^\mu \mapsto x^\mu + \delta x^\mu$ (with $\delta x^\mu = 0$ at the endpoints) is, after integrating the $\delta\dot x^\mu$ term by parts,
> $$\delta S = \int_{\lambda_1}^{\lambda_2}\Big[\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big]\delta x^\mu\,d\lambda.$$
> Demanding $\delta S = 0$ for all $\delta x^\mu$ gives the Euler–Lagrange equations $\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu} = 0$. Now $L$ depends on position only through $\eta_{\mu\nu}$, which in inertial coordinates is the *constant* matrix $\mathrm{diag}(+1,-1,-1,-1)$; hence $\partial L/\partial x^\mu = 0$, and the equation reduces to
> $$\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu} = 0.$$

**Step 2: The momentum is $m u_\mu$, so $du_\mu/d\lambda = 0$ and the worldline is straight.**

> [!note]- Derivation
> Differentiate $L = -m\sqrt{w}$:
> $$\frac{\partial L}{\partial\dot x^\mu} = -m\cdot\frac{1}{2\sqrt{w}}\cdot\frac{\partial w}{\partial\dot x^\mu} = -m\cdot\frac{1}{2\sqrt{w}}\cdot 2\eta_{\mu\nu}\dot x^\nu = -m\,\frac{\eta_{\mu\nu}\dot x^\nu}{\sqrt{w}}.$$
> Define $U^\mu := \dot x^\mu/\sqrt{w}$. Then $\eta_{\mu\nu}U^\mu U^\nu = (\eta_{\mu\nu}\dot x^\mu\dot x^\nu)/w = w/w = 1$, so $U^\mu$ is the unit-normalised [[Def - Four-Velocity and Four-Acceleration|four-velocity]], independent of the parametrisation. Hence $\partial L/\partial\dot x^\mu = -m\,\eta_{\mu\nu}U^\nu = m\,u_\mu$ (writing $u_\mu := \eta_{\mu\nu}U^\nu$, the covariant component; the overall sign is absorbed into the definition, and one checks $u_0 = U^0 > 0$ for a future-pointing worldline, giving positive energy $p_0 = mu_0$). The Euler–Lagrange equation from Step 1 is then
> $$\frac{d}{d\lambda}(m\,u_\mu) = 0 \quad\Longrightarrow\quad \frac{du_\mu}{d\lambda} = 0,$$
> since $m$ is constant. Raising the index with the constant $\eta^{\mu\nu}$ gives $dU^\mu/d\lambda = 0$: the four-velocity is constant, so integrating, $x^\mu(\lambda) = x^\mu_0 + U^\mu\sigma(\lambda)$ for a scalar function $\sigma$ — a straight line of Minkowski spacetime, a timelike geodesic. Imposing $\lambda = \tau$ now (legitimately, after the equations) gives $a^\mu = dU^\mu/d\tau = 0$, zero four-acceleration.

**Step 3: The four equations are dependent; one is the reparametrisation redundancy.**

> [!note]- Derivation
> Euler's identity for the degree-one homogeneous $L$ reads $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$. Differentiate with respect to $\lambda$:
> $$\frac{dL}{d\lambda} = \ddot x^\mu\frac{\partial L}{\partial\dot x^\mu} + \dot x^\mu\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}.$$
> Independently, the chain rule gives $\frac{dL}{d\lambda} = \frac{\partial L}{\partial x^\mu}\dot x^\mu + \frac{\partial L}{\partial\dot x^\mu}\ddot x^\mu$. Subtracting, the $\ddot x^\mu\,\partial L/\partial\dot x^\mu$ terms cancel and
> $$0 = \frac{\partial L}{\partial x^\mu}\dot x^\mu - \dot x^\mu\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu} = \dot x^\mu\Big[\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big] = \dot x^\mu[\text{EL}]_\mu.$$
> So the contraction of the four Euler–Lagrange expressions with $\dot x^\mu$ vanishes identically: they are linearly dependent, and only three are independent. *Physically*, a particle has three degrees of freedom, but the worldline is described by four functions $x^\mu(\lambda)$; the extra function is the arbitrary choice of parameter $\lambda$. The equations of motion fix the worldline as a geometric curve but cannot fix its parametrisation, so one combination of them — the one along $\dot x^\mu$, the direction of "moving the parameter" — must be automatically satisfied. This is the reparametrisation gauge symmetry, the same redundancy that makes the canonical Hamiltonian vanish ([[Thm - Hamiltonian Formulation (Relativistic Particle)]]).

**Step 4: For a curved metric, the geodesic equation with Christoffel symbols.**

> [!note]- Derivation
> Now take $L = -m\sqrt{w}$ with $w = g_{\mu\nu}(x)\dot x^\mu\dot x^\nu$ for a position-dependent metric. The position-derivative no longer vanishes:
> $$\frac{\partial L}{\partial x^\mu} = -m\,\frac{(\partial_\mu g_{\nu\rho})\dot x^\nu\dot x^\rho}{2\sqrt{w}}.$$
> The velocity-derivative is $\partial L/\partial\dot x^\mu = -m\,g_{\mu\nu}\dot x^\nu/\sqrt{w}$. The Euler–Lagrange equation $\partial L/\partial x^\mu = \tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu)$ becomes, after dividing by $-m$ and parametrising by proper time so $\sqrt{w} = 1$ (constant),
> $$\frac{(\partial_\mu g_{\nu\rho})\dot x^\nu\dot x^\rho}{2} = \frac{d}{d\tau}\big(g_{\mu\nu}\dot x^\nu\big) = (\partial_\rho g_{\mu\nu})\dot x^\rho\dot x^\nu + g_{\mu\nu}\ddot x^\nu.$$
> Rearranging, $g_{\mu\nu}\ddot x^\nu + \big[(\partial_\rho g_{\mu\nu}) - \tfrac12(\partial_\mu g_{\nu\rho})\big]\dot x^\nu\dot x^\rho = 0$. Symmetrising the bracket in $\nu\rho$ (since it multiplies the symmetric $\dot x^\nu\dot x^\rho$) gives $\tfrac12(\partial_\rho g_{\mu\nu} + \partial_\nu g_{\mu\rho} - \partial_\mu g_{\nu\rho})$. Contracting with the inverse metric $g^{\sigma\mu}$,
> $$\ddot x^\sigma + \Gamma^\sigma_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0, \qquad \Gamma^\sigma_{\;\nu\rho} = \tfrac12 g^{\sigma\mu}\big(\partial_\nu g_{\mu\rho} + \partial_\rho g_{\mu\nu} - \partial_\mu g_{\nu\rho}\big).$$
> This is the **geodesic equation** of general relativity, with the **Christoffel symbols** $\Gamma$ built from first derivatives of the metric. For the flat metric, $\partial g = 0$, so $\Gamma = 0$ and the equation collapses to $\ddot x^\sigma = 0$, the straight line of Step 2. The Christoffel terms are precisely the contribution that the position-dependence of the metric — i.e. gravity — adds to free motion.

> [!note]- Complete formal solution
> Vary $S = -m\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ with fixed endpoints to get the Euler–Lagrange equations $\partial L/\partial x^\mu - \tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$. Since $\eta_{\mu\nu}$ is constant, $\partial L/\partial x^\mu = 0$, leaving $\tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$. Computing $\partial L/\partial\dot x^\mu = m u_\mu$ with $u_\mu = \eta_{\mu\nu}\dot x^\nu/\sqrt{\eta\dot x\dot x}$ the unit four-velocity, this reads $du_\mu/d\lambda = 0$, so $U$ is constant and the worldline is straight (a timelike geodesic); imposing $\lambda = \tau$ gives $a^\mu = 0$. The four equations are dependent: differentiating Euler's identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ and subtracting the chain-rule expression for $dL/d\lambda$ yields $\dot x^\mu[\text{EL}]_\mu \equiv 0$, the reparametrisation redundancy (three physical degrees of freedom, four coordinate functions). For a curved metric $g_{\mu\nu}(x)$, the position-derivative $\partial L/\partial x^\mu = -m(\partial_\mu g_{\nu\rho})\dot x^\nu\dot x^\rho/(2\sqrt{w})$ no longer vanishes; carrying through the Euler–Lagrange equation, parametrising by proper time, symmetrising, and contracting with $g^{\sigma\mu}$ gives $\ddot x^\sigma + \Gamma^\sigma_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0$ with $\Gamma^\sigma_{\;\nu\rho} = \tfrac12 g^{\sigma\mu}(\partial_\nu g_{\mu\rho} + \partial_\rho g_{\mu\nu} - \partial_\mu g_{\nu\rho})$ — the geodesic equation, reducing to $\ddot x^\sigma = 0$ when $\partial g = 0$. $\blacksquare$

---

# Key Takeaways

**The free worldline is a geodesic because the Lagrangian has no explicit position dependence.** The entire derivation hinges on the single observation that the flat metric is constant, so $\partial L/\partial x^\mu = 0$, which turns the Euler–Lagrange equation into the conservation of the generalized momentum $\partial L/\partial\dot x^\mu = m u_\mu$. This is the relativistic four-dimensional version of the elementary fact that a cyclic coordinate has a conserved conjugate momentum — except that *all four* coordinates are cyclic, so the *entire* four-momentum is conserved and the worldline is straight. The trigger to recognise: whenever a Lagrangian lacks explicit dependence on a coordinate, the conjugate momentum is conserved, and if it lacks dependence on *all* coordinates, the motion is "free" in the corresponding generalized sense. The same logic, applied to a curved metric where $\partial L/\partial x^\mu \neq 0$, produces exactly the Christoffel terms that bend the worldline — gravity is the failure of the metric to be constant.

**Keep the parameter arbitrary until after varying — the normalisation is an output, not an input.** The most common and most fatal error in this calculation is to impose $U\cdot U = 1$ (i.e. $\lambda = \tau$) before performing the variation. Doing so collapses the free Lagrangian to the constant $-m$, whose Euler–Lagrange equations are the vacuous $0 = 0$, and all dynamical content is lost. The reason is that the constraint $U\cdot U = 1$ restricts the allowed variations, and a constrained variation is not a free one; the constraint must emerge as a *consequence* of the equations of motion, imposed only afterwards. This discipline — vary first, constrain second — recurs throughout relativistic and gauge-theoretic variational problems, wherever the action is reparametrisation- or gauge-invariant. Whenever a problem offers a tempting constraint that would simplify the Lagrangian, ask whether imposing it would secretly fix a gauge before the variation is done; if so, resist.

**The redundancy of the four equations is the reparametrisation gauge symmetry, and it is the seed of constrained dynamics.** The identity $\dot x^\mu[\text{EL}]_\mu \equiv 0$ is not a curiosity but the first appearance of a structure that dominates relativistic field theory: a theory invariant under a local symmetry (here reparametrisation of the worldline) always has dependent equations of motion, a vanishing canonical Hamiltonian, and primary constraints, all expressing the same redundancy. The count is exact: four coordinate functions minus one gauge freedom equals three physical degrees of freedom. Recognising this pattern lets you anticipate, before any calculation, that the [[Thm - Hamiltonian Formulation (Relativistic Particle)|Hamiltonian formulation]] will be subtle (the naive Hamiltonian will vanish) and that the theory will have a constraint. The general-relativistic and string-theoretic generalisations of this exercise have the same structure with more gauge freedom, and the relativistic particle is the cleanest place to first see it. For the curved-metric companion calculation see [[Thm - Free-Particle Worldline Extremises Proper Time]], and for the Noether conservation laws that accompany the geodesic equation see [[Ex - Four-momentum conservation from translation invariance]].
