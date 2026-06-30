---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
tags: [physics, special-relativity]
---

# Problem Statement

Parametrise a free particle's worldline by the proper time $t$ of an inertial observer $\mathcal{O}$, so that $\dot x^0 = c$ and $\dot x^i = V^i$, the components of the particle's velocity $\mathbf{V}$ relative to $\mathcal{O}$. Work with $c = 1$ where convenient.

1. Show that the free Lagrangian $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ becomes $L = -mc^2\sqrt{1 - \mathbf{V}^2/c^2} = -mc^2/\gamma$.
2. Compute the conjugate three-momentum $\mathbf{p} = \partial L/\partial\mathbf{V}$ and show it equals the relativistic momentum $m\gamma\mathbf{V}$.
3. Show the Euler–Lagrange equations give $d(m\gamma\mathbf{V})/dt = 0$, i.e. **relativistic Newton's second law** with zero force, and that for a particle in a potential $-V(\mathbf{x})$ added to $L$ they give $d\mathbf{p}/dt = -\nabla V$.
4. Expand $L$ for small $\mathbf{V}$ and recover the Newtonian Lagrangian $\tfrac12 m\mathbf{V}^2$ (up to the constant $-mc^2$). Comment on why the rest-energy constant does not affect the dynamics but does matter for the action's value.

**Recall:**

![[Def - Relativistic Action of a Free Particle#The Definition]]

Relative to an inertial observer $\mathcal{O}$, choosing the parameter $\lambda = t$ (the observer's time), the particle's velocity is $\mathbf{V} = (V^i)$ with $V^i = dx^i/dt$, and the Lorentz factor is $\gamma = (1 - \mathbf{V}^2/c^2)^{-1/2}$. The relativistic three-momentum is $\mathbf{p} = m\gamma\mathbf{V}$ and the energy is $E = m\gamma c^2$ ([[Def - Four-Momentum and Rest Mass]]). Unlike the manifestly covariant Lagrangian, this inertial-observer form is *not* homogeneous of degree one in $\mathbf{V}$, so it admits an ordinary, non-degenerate Legendre transform.

---

# Convergent Strategy

**Problem class.** A *derive-an-equation-of-motion* problem in the inertial-observer parametrisation, which trades manifest Lorentz covariance for the computational transparency of ordinary three-dimensional analytical mechanics (operation 8 of the [[Special Relativity XV — The Principle of Least Action#Legal Operations|topic]]).

**Assumption pattern.** The parameter is fixed to be an inertial observer's time $t$, so $\dot x^0 = c$ is constant and the dynamical variables are the three spatial velocities $V^i$. This breaks the covariance but makes the Lagrangian a function of $\mathbf{V}$ alone, $L = -mc^2/\gamma$, which is *not* degree-one homogeneous and so behaves like an ordinary Lagrangian.

**Theorem routing.** Substituting $\dot x^0 = c$, $\dot x^i = V^i$ into [[Def - Relativistic Action of a Free Particle|the free Lagrangian]] gives the $\sqrt{1 - \mathbf{V}^2}$ form; differentiating gives the [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian|conjugate momentum]] $m\gamma\mathbf{V}$; the Euler–Lagrange equations give relativistic Newton's second law; and the small-$\mathbf{V}$ expansion recovers the Newtonian limit.

**Key decision point.** The crux is recognising that fixing $\lambda = t$ is *legitimate here* — unlike imposing $\lambda = \tau$, which would be fatal. The difference: $\tau$ is the *particle's* proper time, intrinsic to the worldline, and imposing it constrains the variations; $t$ is an *external* observer's time, a perfectly good arbitrary parameter, and fixing it merely chooses a (non-covariant) gauge in which the Lagrangian becomes non-degenerate. This is why the inertial-observer Lagrangian admits an honest Legendre transform while the covariant one does not.

---

# Legal Operations Used

1. **Switch to the inertial-observer Lagrangian for explicit computation** (operation 8 from the topic page). With $\lambda = t$, the Lagrangian becomes $-mc^2\sqrt{1 - \mathbf{V}^2/c^2}$, a function of $\mathbf{V}$ alone, and ordinary three-dimensional mechanics applies.

2. **Vary the action and read off the Euler–Lagrange equations** (operation 1). The three-dimensional Euler–Lagrange equations $\tfrac{d}{dt}(\partial L/\partial V^i) - \partial L/\partial x^i = 0$ give the equation of motion.

3. **Compute the generalized momentum** (operation 5). Here $\mathbf{p} = \partial L/\partial\mathbf{V} = m\gamma\mathbf{V}$, the relativistic three-momentum.

---

# Hints

> [!note]- Hint 1
> Substitute $\dot x^0 = c$ and $\dot x^i = V^i$ into $\eta_{\mu\nu}\dot x^\mu\dot x^\nu = c^2 - \mathbf{V}^2$ (mostly-minus). The square root is then $\sqrt{c^2 - \mathbf{V}^2} = c\sqrt{1 - \mathbf{V}^2/c^2}$, so $L = -mc\cdot c\sqrt{1 - \mathbf{V}^2/c^2}$.

> [!note]- Hint 2
> Differentiate $L = -mc^2\sqrt{1 - \mathbf{V}^2/c^2}$ with respect to $V^i$. The chain rule gives $\partial L/\partial V^i = -mc^2\cdot\tfrac{-V^i/c^2}{\sqrt{1 - \mathbf{V}^2/c^2}} = m\gamma V^i$, so $\mathbf{p} = m\gamma\mathbf{V}$.

> [!note]- Hint 3
> For a free particle $L$ has no $\mathbf{x}$-dependence, so the Euler–Lagrange equation is $\tfrac{d}{dt}(\partial L/\partial V^i) = 0$, i.e. $d\mathbf{p}/dt = 0$. Adding a potential $-V(\mathbf{x})$ makes $\partial L/\partial x^i = -\partial V/\partial x^i$, giving $d\mathbf{p}/dt = -\nabla V$.

> [!note]- Hint 4
> Use $\sqrt{1 - \mathbf{V}^2/c^2} \approx 1 - \tfrac{\mathbf{V}^2}{2c^2}$ for small $\mathbf{V}$, so $L \approx -mc^2 + \tfrac12 m\mathbf{V}^2$. A constant added to a Lagrangian changes the action by a constant times the elapsed time, which has no effect on $\delta S$ (the endpoints are fixed), so it does not affect the equations of motion — but it does change the *numerical value* of the action, which matters in the path integral $e^{iS/\hbar}$.

---

# Solution

The solution is a straightforward substitution-and-differentiate calculation in four short steps. Step 1 substitutes the inertial parametrisation into the free Lagrangian. Step 2 differentiates to find the relativistic momentum. Step 3 reads off relativistic Newton's second law, with and without a potential. Step 4 takes the non-relativistic limit. The conceptual content is in the contrast with the covariant calculation: fixing an *external* time is legitimate and yields a non-degenerate Lagrangian, whereas fixing the *particle's* proper time would not.

**Step 1: $L = -mc^2\sqrt{1 - \mathbf{V}^2/c^2}$.**

> [!note]- Derivation
> With $\lambda = t$, the parameter-velocities are $\dot x^0 = dx^0/dt = c$ (since $x^0 = ct$) and $\dot x^i = dx^i/dt = V^i$. The Minkowski norm of the tangent is
> $$\eta_{\mu\nu}\dot x^\mu\dot x^\nu = (\dot x^0)^2 - (\dot x^i)^2 = c^2 - \mathbf{V}^2,$$
> using mostly-minus. Hence
> $$L = -mc\sqrt{c^2 - \mathbf{V}^2} = -mc^2\sqrt{1 - \frac{\mathbf{V}^2}{c^2}} = -\frac{mc^2}{\gamma},$$
> where $\gamma = (1 - \mathbf{V}^2/c^2)^{-1/2}$. This is the form quoted in introductory textbooks (Landau–Lifshitz, Feynman). Note it is *not* of the form (kinetic) $-$ (potential): the free relativistic Lagrangian is minus the rest energy divided by $\gamma$.

**Step 2: The conjugate momentum is $\mathbf{p} = m\gamma\mathbf{V}$.**

> [!note]- Derivation
> Differentiate $L = -mc^2(1 - \mathbf{V}^2/c^2)^{1/2}$ with respect to $V^i$:
> $$p_i = \frac{\partial L}{\partial V^i} = -mc^2\cdot\frac12(1 - \mathbf{V}^2/c^2)^{-1/2}\cdot\Big(-\frac{2V^i}{c^2}\Big) = \frac{mV^i}{\sqrt{1 - \mathbf{V}^2/c^2}} = m\gamma V^i.$$
> So $\mathbf{p} = m\gamma\mathbf{V}$, the relativistic three-momentum of [[Def - Four-Momentum and Rest Mass]] — the spatial part of the four-momentum $P = mU$, since $U^i = \gamma V^i$. The conjugate momentum of the inertial-observer Lagrangian *is* the physical relativistic momentum, with the Lorentz factor $\gamma$ multiplying the Newtonian $m\mathbf{V}$.

**Step 3: Relativistic Newton's second law.**

> [!note]- Derivation
> For a free particle, $L = -mc^2/\gamma$ has no explicit dependence on the position $\mathbf{x}$, so $\partial L/\partial x^i = 0$, and the Euler–Lagrange equations $\tfrac{d}{dt}(\partial L/\partial V^i) - \partial L/\partial x^i = 0$ reduce to
> $$\frac{d\mathbf{p}}{dt} = \frac{d}{dt}(m\gamma\mathbf{V}) = 0,$$
> conservation of relativistic three-momentum. Now add a potential interaction, $L = -mc^2/\gamma - V(\mathbf{x})$ (a scalar potential energy, appropriate for a static conservative force). Then $\partial L/\partial x^i = -\partial V/\partial x^i$, and the Euler–Lagrange equations give
> $$\frac{d\mathbf{p}}{dt} = -\nabla V,$$
> **relativistic Newton's second law**: the rate of change of the relativistic momentum $m\gamma\mathbf{V}$ equals the force $-\nabla V$. This is the three-dimensional form of $f = dP/d\tau$; the only difference from the Newtonian law is that $\mathbf{p} = m\gamma\mathbf{V}$ carries the factor $\gamma$, so as $|\mathbf{V}| \to c$ the momentum diverges and the particle resists further acceleration — no force can push it past $c$.

**Step 4: The non-relativistic limit.**

> [!note]- Derivation
> Expand $\sqrt{1 - \mathbf{V}^2/c^2}$ for $|\mathbf{V}| \ll c$:
> $$L = -mc^2\Big(1 - \frac{\mathbf{V}^2}{2c^2} - \frac{\mathbf{V}^4}{8c^4} - \cdots\Big) = -mc^2 + \frac12 m\mathbf{V}^2 + \frac{m\mathbf{V}^4}{8c^2} + \cdots.$$
> The leading non-constant term is the **Newtonian kinetic energy** $\tfrac12 m\mathbf{V}^2$, confirming that the relativistic Lagrangian reduces to the Newtonian one at low speeds. The constant $-mc^2$ is the rest energy; it adds $-mc^2(t_2 - t_1)$ to the action. Because the endpoints (and hence the elapsed time $t_2 - t_1$) are held fixed in the variation, this constant contributes nothing to $\delta S$ and so does not affect the equations of motion — Newtonian mechanics never noticed the rest energy. But the constant *does* change the numerical value of $S$, which matters in the path-integral weight $e^{iS/\hbar}$ and is the origin of the rest-energy phase $e^{-imc^2 t/\hbar}$ of a relativistic wavefunction. The next term $m\mathbf{V}^4/(8c^2)$ is the leading relativistic correction to the kinetic energy.

> [!note]- Complete formal solution
> With $\lambda = t$, $\dot x^0 = c$, $\dot x^i = V^i$, the norm $\eta_{\mu\nu}\dot x^\mu\dot x^\nu = c^2 - \mathbf{V}^2$, so $L = -mc\sqrt{c^2 - \mathbf{V}^2} = -mc^2\sqrt{1 - \mathbf{V}^2/c^2} = -mc^2/\gamma$. Differentiating, $\mathbf{p} = \partial L/\partial\mathbf{V} = m\gamma\mathbf{V}$, the relativistic three-momentum. For a free particle $\partial L/\partial\mathbf{x} = 0$, so the Euler–Lagrange equations give $d(m\gamma\mathbf{V})/dt = 0$; adding $-V(\mathbf{x})$ gives $d\mathbf{p}/dt = -\nabla V$, relativistic Newton's second law. Expanding for small $\mathbf{V}$, $L \approx -mc^2 + \tfrac12 m\mathbf{V}^2$, recovering the Newtonian kinetic energy; the constant $-mc^2$ drops out of $\delta S$ (fixed endpoints) so does not affect the dynamics, but contributes the rest-energy phase to the action's value. $\blacksquare$

---

# Key Takeaways

**Fixing an external observer's time is legitimate; fixing the particle's proper time is not.** This exercise and [[Ex - Deriving the geodesic equation from the variational principle|the geodesic derivation]] look superficially similar — both fix the parameter $\lambda$ — but the difference is decisive. Here $\lambda = t$ is an *inertial observer's* time, an external coordinate that is a perfectly valid arbitrary parameter; fixing it merely chooses a non-covariant description in which the Lagrangian $-mc^2/\gamma$ is a non-degenerate function of $\mathbf{V}$, so the ordinary machinery of Lagrangian and Hamiltonian mechanics applies. Imposing $\lambda = \tau$, the *particle's* proper time, would instead constrain the variations and collapse the Lagrangian to a constant. The diagnostic: a parameter intrinsic to the worldline (proper time) cannot be fixed before varying, but a parameter external to it (an observer's time) can. This is why the inertial-observer Lagrangian, alone among the parametrisations, admits an honest Legendre transform to $H = \sqrt{\mathbf{p}^2 + m^2}$.

**The relativistic momentum $m\gamma\mathbf{V}$ is the conjugate momentum, and its divergence at $c$ is the speed limit.** The conjugate momentum $\mathbf{p} = \partial L/\partial\mathbf{V} = m\gamma\mathbf{V}$ differs from the Newtonian $m\mathbf{V}$ only by the factor $\gamma$, but that factor is the whole of relativistic dynamics: as $|\mathbf{V}| \to c$, $\gamma \to \infty$, so a finite force (a finite $d\mathbf{p}/dt$) produces a vanishing acceleration $d\mathbf{V}/dt$, and the particle can be pushed arbitrarily close to $c$ but never reach it. The reusable principle is that relativistic Newton's second law is $d(m\gamma\mathbf{V})/dt = \mathbf{F}$, *not* $m\,d\mathbf{V}/dt = \mathbf{F}$; the mass that resists acceleration grows with speed. This is the dynamical face of the kinematic fact that $c$ is an unreachable ceiling, and it is why particle accelerators need ever more energy for ever smaller speed gains near $c$.

**A constant in the Lagrangian is invisible to the dynamics but visible to the action.** The rest-energy term $-mc^2$ in the expanded Lagrangian is a pure constant, and constants drop out of the Euler–Lagrange equations because $\delta S$ holds the endpoints (and hence the elapsed time) fixed — which is why Newtonian mechanics, working only with the dynamics, never needed the concept of rest energy. But the constant is *not* physically inert: it changes the numerical value of the action $S$, and the action's value is what appears in the quantum-mechanical phase $e^{iS/\hbar}$. The rest-energy contribution $-mc^2(t_2 - t_1)$ becomes the rapidly oscillating phase $e^{-imc^2 t/\hbar}$ of a relativistic wavefunction, the very factor one strips off to obtain the non-relativistic Schrödinger equation. The general lesson: total derivatives and constants in a Lagrangian are dynamically irrelevant but can carry physical meaning (boundary terms, anomalies, phases) once the theory is quantised. For the covariant treatment that keeps Lorentz invariance manifest, and the Legendre transform that turns this Lagrangian into $H = \sqrt{\mathbf{p}^2 + m^2}$, see [[Ex - Legendre transform to the relativistic Hamiltonian]].
