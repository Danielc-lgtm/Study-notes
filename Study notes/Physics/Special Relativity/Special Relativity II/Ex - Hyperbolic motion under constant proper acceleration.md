---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
  - "Def - Rapidity"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

A particle moves along the $x$-axis of an inertial frame $S$, undergoing **constant proper acceleration** $\kappa$ — meaning that the magnitude of its acceleration, as measured in the inertial frame momentarily comoving with the particle, is the constant $\kappa$. The particle is at rest at the origin at $t = \tau = 0$.

**(a)** Show that the four-velocity, as a function of proper time $\tau$, is
$$U^\mu(\tau) = \big(c\cosh(\kappa\tau/c),\ c\sinh(\kappa\tau/c),\ 0,\ 0\big),$$
and verify it satisfies the normalisation $U\cdot U = c^2$ and that the four-acceleration has constant Minkowski length $A\cdot A = -\kappa^2$.

**(b)** Integrate to find the worldline $\big(ct(\tau),\,x(\tau)\big)$, and show it is a hyperbola in the $(x,ct)$ plane.

**(c)** Find the ordinary speed $u$ and ordinary position $x$ as functions of the inertial coordinate time $t$, and show that $u\to c$ as $t\to\infty$ but $u < c$ always.

**(d)** A traveller accelerates at $\kappa = g$ (Earth gravity) for $10$ years of *proper* time. Roughly how much coordinate time elapses in $S$? (Numerically: $g\approx 1.03$ light-year/year².)

**Recall:**

![[Def - Four-Velocity and Four-Acceleration#The Definition]]

The [[Def - Rapidity|rapidity]] $\phi$ associated with speed $u$ is defined by $u = c\tanh\phi$, so that $\gamma = \cosh\phi$ and $\gamma u/c = \sinh\phi$. A purely temporal/longitudinal four-vector $(c\cosh\phi, c\sinh\phi)$ has Minkowski square $c^2(\cosh^2\phi - \sinh^2\phi) = c^2$.

---

# Convergent Strategy

**Problem class.** This is a *worldline-construction* problem: integrate the relativistic equation of motion (here, the definition of four-acceleration) to recover the trajectory.

**Assumption pattern.** "Constant proper acceleration $\kappa$" is the constraint. It does *not* mean $d\mathbf{u}/dt$ is constant in $S$ — that would let $u$ exceed $c$. It means the invariant $A\cdot A = -\kappa^2$ is constant. The four-acceleration is constrained both by this and by the free orthogonality relation $A\cdot U = 0$.

**Theorem routing.** Part (a) routes through the two constraints $A\cdot U = 0$ and $A\cdot A = -\kappa^2$, together with $U\cdot U = c^2$, all from [[Def - Four-Velocity and Four-Acceleration|the definition of four-velocity and four-acceleration]]. These are most cleanly solved by parametrising the longitudinal four-velocity by [[Def - Rapidity|rapidity]]: $U^\mu = c(\cosh\phi,\sinh\phi)$ automatically satisfies $U\cdot U = c^2$, and the equations of motion become a trivial ODE for $\phi(\tau)$.

**Key decision point.** The decisive insight is the **rapidity substitution**. Writing $U^\mu = c(\cosh\phi(\tau),\sinh\phi(\tau),0,0)$ builds the normalisation in for free, just as writing a planar unit vector as $(\cos\theta,\sin\theta)$ builds in $|\mathbf{v}|=1$. The constant-proper-acceleration condition then says $\phi$ advances at a constant rate in proper time — rapidity is the relativistic analogue of velocity, and constant proper acceleration means *rapidity grows linearly with proper time*.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Differentiate with respect to proper time** — $A^\mu = dU^\mu/d\tau$, and the worldline is recovered by integrating $U^\mu = dX^\mu/d\tau$ in $\tau$.
2. **Use the normalisation and orthogonality $U\cdot U = c^2$, $A\cdot U = 0$** — these constrain the four-acceleration; the rapidity parametrisation makes them automatic.
3. **Use a Lorentz invariant** — "constant proper acceleration" is the statement that the invariant $A\cdot A$ is constant.

---

# Hints

> [!note]- Hint 1
> "Constant proper acceleration" does not mean $d u/dt = \text{const}$. It means the *invariant* $A\cdot A = -\kappa^2$ is constant. Write down what $A\cdot A$ and $A\cdot U$ are, and remember $U\cdot U = c^2$.

> [!note]- Hint 2
> For motion along the $x$-axis, the four-velocity has only a time and an $x$ component, tied by $U\cdot U = c^2$. Parametrise it as $U^\mu = c(\cosh\phi,\sinh\phi,0,0)$ — this satisfies the normalisation identically for any function $\phi(\tau)$. The unknown is now the single function $\phi(\tau)$.

> [!note]- Hint 3
> Compute $A^\mu = dU^\mu/d\tau = c\,\dot\phi\,(\sinh\phi,\cosh\phi,0,0)$. Then $A\cdot A = -c^2\dot\phi^2$. Setting this equal to $-\kappa^2$ gives $\dot\phi = \kappa/c$ — rapidity grows linearly in proper time.

> [!note]- Hint 4
> With $\phi = \kappa\tau/c$, integrate $U^\mu = dX^\mu/d\tau$ to get $ct(\tau)$ and $x(\tau)$. Hyperbolic identities then give $x^2 - (ct)^2 = (c^2/\kappa)^2$. For (c), use $u = dx/dt = (dx/d\tau)/(dt/d\tau)$.

---

# Solution

The trick is the rapidity parametrisation: writing the longitudinal four-velocity as $c(\cosh\phi,\sinh\phi)$ builds in $U\cdot U = c^2$ automatically, and constant proper acceleration becomes the statement that rapidity grows linearly in proper time, $\phi = \kappa\tau/c$. Everything else is hyperbolic-function bookkeeping.

**Step 1: The four-velocity (part a).**

Parametrising by rapidity and imposing constant proper acceleration gives $\phi(\tau) = \kappa\tau/c$, hence $U^\mu = c(\cosh(\kappa\tau/c),\sinh(\kappa\tau/c),0,0)$.

> [!note]- Derivation
> For motion confined to the $x$-axis the four-velocity is $U^\mu = (U^0,U^1,0,0)$, subject to $U\cdot U = (U^0)^2 - (U^1)^2 = c^2$. This is the equation of a hyperbola in $(U^1,U^0)$-space, so its general solution is the **rapidity parametrisation**
> $$U^\mu = c\big(\cosh\phi(\tau),\,\sinh\phi(\tau),\,0,\,0\big),$$
> for some function $\phi(\tau)$, since $c^2(\cosh^2\phi-\sinh^2\phi) = c^2$ identically. This is the exact analogue of writing a Euclidean unit vector as $(\cos\theta,\sin\theta)$ — the constraint is absorbed into the parametrisation. The four-acceleration is
> $$A^\mu = \frac{dU^\mu}{d\tau} = c\,\dot\phi\,\big(\sinh\phi,\,\cosh\phi,\,0,\,0\big).$$
> Check the orthogonality: $A\cdot U = c^2\dot\phi(\sinh\phi\cosh\phi - \cosh\phi\sinh\phi) = 0$ — automatic, as [[Def - Four-Velocity and Four-Acceleration|the definition]] guarantees. Now its Minkowski square:
> $$A\cdot A = c^2\dot\phi^2(\sinh^2\phi - \cosh^2\phi) = -c^2\dot\phi^2.$$
> "Constant proper acceleration $\kappa$" means $A\cdot A = -\kappa^2$, so $c^2\dot\phi^2 = \kappa^2$, giving $\dot\phi = \kappa/c$ (taking the particle to be speeding up). Integrating with $\phi(0)=0$ (the particle starts at rest, $U^1(0)=0$):
> $$\phi(\tau) = \frac{\kappa\tau}{c}, \qquad U^\mu(\tau) = c\Big(\cosh\frac{\kappa\tau}{c},\ \sinh\frac{\kappa\tau}{c},\ 0,\ 0\Big).$$
> The normalisation $U\cdot U = c^2$ holds by construction, and $A\cdot A = -\kappa^2$ by the choice of $\dot\phi$. **Rapidity grows linearly with proper time** — this is the cleanest possible statement of constant proper acceleration.

**Step 2: The worldline (part b).**

Integrating $dX^\mu/d\tau = U^\mu$ gives $ct(\tau) = (c^2/\kappa)\sinh(\kappa\tau/c)$ and $x(\tau) = (c^2/\kappa)\cosh(\kappa\tau/c)$, a hyperbola $x^2 - (ct)^2 = (c^2/\kappa)^2$.

> [!note]- Derivation
> By [[Def - Four-Velocity and Four-Acceleration|definition]] $U^\mu = dX^\mu/d\tau$, so integrate each component in proper time:
> $$\frac{d(ct)}{d\tau} = U^0 = c\cosh\frac{\kappa\tau}{c} \;\Longrightarrow\; ct(\tau) = \frac{c^2}{\kappa}\sinh\frac{\kappa\tau}{c} + C_0,$$
> $$\frac{dx}{d\tau} = U^1 = c\sinh\frac{\kappa\tau}{c} \;\Longrightarrow\; x(\tau) = \frac{c^2}{\kappa}\cosh\frac{\kappa\tau}{c} + C_1.$$
> The particle is at the origin at $\tau = 0$ in time but — choose the integration constant for $x$ so that the algebra is clean — set $t(0)=0$, so $C_0 = 0$, and let $x(0) = c^2/\kappa$ (i.e. $C_1 = 0$). Then
> $$ct(\tau) = \frac{c^2}{\kappa}\sinh\frac{\kappa\tau}{c},\qquad x(\tau) = \frac{c^2}{\kappa}\cosh\frac{\kappa\tau}{c}.$$
> Using $\cosh^2 - \sinh^2 = 1$,
> $$x^2 - (ct)^2 = \Big(\frac{c^2}{\kappa}\Big)^2\big(\cosh^2 - \sinh^2\big) = \Big(\frac{c^2}{\kappa}\Big)^2.$$
> The worldline is a **hyperbola** in the $(x,ct)$ plane — hence the name *hyperbolic motion* — with asymptotes the null lines $x = \pm ct$. The particle starts at $x = c^2/\kappa$ at rest and curves up toward the asymptote $x = ct$ without ever reaching it.

**Step 3: Speed and position in coordinate time (part c).**

In terms of $S$-coordinate time, $u(t) = \dfrac{\kappa t}{\sqrt{1 + \kappa^2t^2/c^2}}$ and $x(t) = \dfrac{c^2}{\kappa}\Big(\sqrt{1 + \kappa^2t^2/c^2} - 1\Big)$ (with the origin reset so $x(0)=0$); $u\to c$ as $t\to\infty$, but $u < c$ for all finite $t$.

> [!note]- Derivation
> The ordinary speed is $u = dx/dt = (dx/d\tau)/(dt/d\tau) = U^1/U^0$:
> $$u = c\,\frac{\sinh(\kappa\tau/c)}{\cosh(\kappa\tau/c)} = c\tanh\frac{\kappa\tau}{c}.$$
> So the rapidity $\phi = \kappa\tau/c$ is exactly the [[Def - Rapidity|rapidity]] of the velocity, $u = c\tanh\phi$ — confirming the parametrisation's name. To express $u$ in terms of $t$, invert $ct = (c^2/\kappa)\sinh(\kappa\tau/c)$: this gives $\sinh(\kappa\tau/c) = \kappa t/c$, hence $\cosh(\kappa\tau/c) = \sqrt{1 + \kappa^2t^2/c^2}$, so
> $$u(t) = c\,\frac{\sinh}{\cosh} = c\cdot\frac{\kappa t/c}{\sqrt{1+\kappa^2t^2/c^2}} = \frac{\kappa t}{\sqrt{1 + \kappa^2 t^2/c^2}}.$$
> As $t\to\infty$, the denominator $\sim\kappa t/c$, so $u\to c$ — the particle approaches the speed of light. But for any finite $t$, $\sqrt{1+\kappa^2t^2/c^2} > \kappa t/c$, so $u < c$ strictly. Constant proper acceleration forever still never breaks the speed limit; this is exactly the protection the diverging structure provides, and it is why the naive "constant $du/dt$" reading would be wrong.
>
> For the position, from $x(\tau) = (c^2/\kappa)\cosh(\kappa\tau/c) = (c^2/\kappa)\sqrt{1+\kappa^2t^2/c^2}$, and resetting the origin so $x(0)=0$:
> $$x(t) = \frac{c^2}{\kappa}\Big(\sqrt{1 + \frac{\kappa^2t^2}{c^2}} - 1\Big).$$
> For small $t$ this expands as $x\approx\tfrac12\kappa t^2$ — Newtonian uniform acceleration, as it must. For large $t$, $x\approx ct$ — motion at essentially light speed.

**Step 4: The traveller's clock (part d).**

> [!note]- Derivation
> The relation between proper time and coordinate time is $ct = (c^2/\kappa)\sinh(\kappa\tau/c)$, i.e.
> $$t = \frac{c}{\kappa}\sinh\frac{\kappa\tau}{c}.$$
> With $\kappa = g \approx 1.03$ ly/yr² and $c = 1$ ly/yr, the combination $g/c \approx 1.03\,\text{yr}^{-1}\approx 1\,\text{yr}^{-1}$, so $\kappa\tau/c \approx \tau$ measured in years. For $\tau = 10$ years,
> $$t = \frac{c}{\kappa}\sinh\frac{\kappa\tau}{c} \approx (1\,\text{yr})\cdot\sinh(10) \approx \frac{1}{2}e^{10}\;\text{yr} \approx \frac{1}{2}(22026)\;\text{yr} \approx 1.1\times10^4\;\text{yr}.$$
> Ten years of proper acceleration at Earth gravity carries the traveller roughly **eleven thousand years** into the future of frame $S$. The growth is *exponential* in proper time, because $\sinh$ is. A crewed rocket able to sustain $1g$ could, in a human lifetime of proper time, cross the observable universe — the limitation is energy and engineering, not relativity.

> [!note]- Complete formal solution
> Confining motion to the $x$-axis, write the four-velocity in rapidity form $U^\mu = c(\cosh\phi,\sinh\phi,0,0)$, which satisfies $U\cdot U = c^2$ identically. Then $A^\mu = c\dot\phi(\sinh\phi,\cosh\phi,0,0)$, giving $A\cdot U = 0$ and $A\cdot A = -c^2\dot\phi^2$. Constant proper acceleration $A\cdot A = -\kappa^2$ forces $\dot\phi = \kappa/c$, so with $\phi(0)=0$,
> $$\phi(\tau) = \kappa\tau/c, \qquad U^\mu = c(\cosh(\kappa\tau/c),\sinh(\kappa\tau/c),0,0).$$
> Integrating $dX^\mu/d\tau = U^\mu$ with suitable constants,
> $$ct(\tau) = \frac{c^2}{\kappa}\sinh\frac{\kappa\tau}{c}, \qquad x(\tau) = \frac{c^2}{\kappa}\cosh\frac{\kappa\tau}{c}, \qquad x^2 - (ct)^2 = (c^2/\kappa)^2,$$
> a hyperbola. Eliminating $\tau$: $u(t) = U^1/U^0 = c\tanh(\kappa\tau/c) = \kappa t/\sqrt{1+\kappa^2t^2/c^2}\to c$ as $t\to\infty$ with $u<c$ always, and $x(t) = (c^2/\kappa)(\sqrt{1+\kappa^2t^2/c^2}-1)$. Finally, $t = (c/\kappa)\sinh(\kappa\tau/c)$; for $\kappa=g$, $\tau=10$ yr gives $t\approx\tfrac12 e^{10}\approx 1.1\times10^4$ yr. $\blacksquare$

---

# Key Takeaways

**Rapidity is the relativistic analogue of velocity, and constant proper acceleration means rapidity grows linearly in proper time.** The whole problem turns on one substitution: parametrise the longitudinal four-velocity as $c(\cosh\phi,\sinh\phi)$. This builds the normalisation $U\cdot U = c^2$ in for free — exactly as $(\cos\theta,\sin\theta)$ builds in $|\mathbf{v}|=1$ — and converts a constrained problem into an unconstrained ODE for the single function $\phi(\tau)$. Constant proper acceleration then reads $\dot\phi = \kappa/c$, the cleanest possible statement: rapidity is what advances uniformly. This is why rapidity, not velocity, is the "right" relativistic velocity variable — velocities compose by the awkward addition formula, but rapidities simply *add*, and a constant push produces a constant *rapidity* rate. Whenever a problem involves sustained one-dimensional acceleration or composing many boosts, switch to rapidity and the hyperbolic functions do the bookkeeping.

**Constant proper acceleration forever still never reaches $c$ — the geometry is hyperbolic, not parabolic.** The naive "constant acceleration" picture from Newtonian physics is $x = \tfrac12 a t^2$, a parabola, with $u = at$ growing without bound. Relativistically, constant *proper* acceleration produces a *hyperbola* $x^2-(ct)^2 = \text{const}$, with $u = c\tanh(\kappa\tau/c)$ asymptoting to but never reaching $c$. The hyperbola's null asymptotes $x=\pm ct$ are the speed limit made geometric. The lesson is to be ruthless about what "constant acceleration" means: the frame-independent statement is that the invariant $A\cdot A = -\kappa^2$ is constant — the acceleration felt by the traveller — not that $d\mathbf{u}/dt$ is constant in some external frame, which is frame-dependent and would falsely permit superluminal speeds. Always anchor "constant" to a Lorentz invariant.

**Exponential growth in proper time is the engine of long-range space travel and of the Rindler horizon.** Because $t = (c/\kappa)\sinh(\kappa\tau/c)$, coordinate time runs *exponentially* fast in the traveller's proper time. Ten proper years at $1g$ buys eleven thousand coordinate years — a quantitative, dramatic form of the twin paradox. The same hyperbolic worldline has another striking feature: it has a null asymptote $x = ct$, and signals from beyond that line can never catch the eternally accelerating traveller. That asymptote is the **Rindler horizon**, a causal horizon created purely by acceleration, and it is the simplest model of a black-hole event horizon — the Unruh effect, Hawking radiation's flat-space cousin, lives on exactly this worldline. A single clean kinematics calculation thus reaches from interstellar travel to the thermodynamics of horizons.
