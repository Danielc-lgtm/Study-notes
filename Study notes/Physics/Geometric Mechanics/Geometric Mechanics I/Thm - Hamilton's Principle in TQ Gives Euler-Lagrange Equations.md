---
type: theorem
subject: geometric-mechanics
prereqs:
  - "Def - The Lagrangian Function"
  - "Def - The Tangent Bundle"
tags: [physics, geometric-mechanics, lagrangian-mechanics, calculus-of-variations]
---

# Notation

$Q$ is a smooth manifold of dimension $n$ (configuration space). $L : TQ \to \mathbb{R}$ is a smooth Lagrangian (or $L : TQ \times \mathbb{R} \to \mathbb{R}$ for time-dependent). $\gamma : [a, b] \to Q$ is a smooth curve in $Q$; its lift to $TQ$ is $(\gamma(t), \dot\gamma(t))$. The action is $S[\gamma] := \int_a^b L(\gamma, \dot\gamma, t)\, dt$. A **variation** of $\gamma$ is a smooth family $\gamma_s$ of curves with $\gamma_0 = \gamma$ and the **variation field** $\delta\gamma := \partial\gamma_s/\partial s|_{s=0}$; the variation is **fixed-endpoint** if $\gamma_s(a) = \gamma(a)$ and $\gamma_s(b) = \gamma(b)$ for all $s$, equivalently $\delta\gamma(a) = \delta\gamma(b) = 0$.

---

# Statement

> **Theorem (Hamilton's principle / Euler–Lagrange equations).** Let $Q$ be a smooth manifold, $L : TQ \times \mathbb{R} \to \mathbb{R}$ a smooth Lagrangian, and $\gamma : [a, b] \to Q$ a smooth curve. The following are equivalent:
>
> 1. $\gamma$ is a **stationary point** of the action $S[\gamma] = \int_a^b L(\gamma(t), \dot\gamma(t), t)\, dt$ among all smooth variations $\gamma_s$ with fixed endpoints, i.e., $\frac{d}{ds}\big|_{s=0} S[\gamma_s] = 0$ for every such variation.
>
> 2. $\gamma$ satisfies the **Euler–Lagrange equations** in every chart $(U, q^i)$ on $Q$:
>
> $$\frac{\partial L}{\partial q^i}\big(\gamma(t), \dot\gamma(t), t\big) - \frac{d}{dt}\frac{\partial L}{\partial \dot q^i}\big(\gamma(t), \dot\gamma(t), t\big) = 0, \quad i = 1, \dots, n.$$
>
> The equations are coordinate-invariant: they hold in one chart iff they hold in every chart. For a regular Lagrangian, the EL equations form a second-order ODE on $Q$ that locally has a unique solution for given initial position and velocity.

---

# Motivation

Hamilton's principle of stationary action is one of the **deepest unifying principles in physics**. It says that the actual trajectory of a physical system is a stationary point of an integral — the action — rather than the solution of a differential equation directly. This shift in perspective from "solve the equation" to "extremize the functional" has profound consequences.

First, it makes physics **coordinate-free**. The action $S[\gamma] = \int L\,dt$ is a number associated to a curve $\gamma$; the variational principle "stationary point" makes sense regardless of any coordinates. The Euler–Lagrange equations that result are automatically tensorial — they transform correctly under any coordinate change. This is in contrast to writing Newton's law $m\ddot q = -\nabla V$, which requires Cartesian coordinates and obscure connection terms in any other system.

Second, the variational principle **generalizes beautifully**. From classical mechanics it extends to:
- **Classical field theory**: $S = \int \mathcal{L}\,d^4x$ for a Lagrangian density $\mathcal{L}$. Euler–Lagrange becomes a PDE.
- **Electromagnetism**: $\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$ gives Maxwell's equations.
- **General relativity**: the Einstein–Hilbert action $S = \int R\sqrt{-g}\,d^4x$ gives Einstein's field equations.
- **Quantum mechanics**: Feynman's path integral $\int e^{iS/\hbar}\mathcal{D}[\gamma]$ sums over all paths weighted by $e^{iS/\hbar}$, with the classical limit picking out the stationary trajectories.
- **Optics**: Fermat's principle (light minimizes optical path length).

Third, the variational principle **encodes symmetries cleanly via Noether's theorem**. A continuous symmetry of the Lagrangian produces a conserved current, with no extra work. Spatial translations $\to$ momentum; rotations $\to$ angular momentum; time-translation $\to$ energy.

The theorem itself is a calculation in the calculus of variations: derive the Euler–Lagrange equations from the variational condition by integration by parts. The technical work is in handling the variation $\delta\dot\gamma = d(\delta\gamma)/dt$ (the variation of the velocity is the time derivative of the variation of the position) and discarding boundary terms.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is "you have a Lagrangian on $TQ$ and want to find the trajectory". Several setups produce Lagrangians naturally.

**Source: a mechanical system with kinetic + potential energy.** $L = T - V$ where $T = \tfrac{1}{2}g_{ij}(q)\dot q^i\dot q^j$ and $V = V(q, t)$. Hamilton's principle gives Newton's equations $m\ddot q = -\nabla V$ (in suitable coordinates) plus the geodesic terms when $g$ is non-Euclidean. *Example use:* the pendulum, double pendulum, particle in a central force, motion on a sphere.

**Source: a constrained system.** If a mechanical system is constrained to a submanifold $S \subset \mathbb{R}^N$, restrict $L = \tfrac{1}{2}m|\dot q|^2 - V$ to $TS$ and apply Hamilton's principle on $S$. The constraint forces are automatically incorporated — no Lagrange multipliers needed. *Example use:* the rigid pendulum (constrained to $S^1$), the spherical pendulum (constrained to $S^2$), a particle on a torus.

**Source: a relativistic free particle.** $L = -mc^2\sqrt{1 - |\dot q|^2/c^2}$, with the action being proportional to proper time. Stationary action gives geodesic motion in Minkowski space — straight-line trajectories at constant velocity. *Example use:* relativistic kinematics.

**Source: a Riemannian geodesic.** $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ alone (no potential). Hamilton's principle gives the geodesic equations $\ddot q^k + \Gamma^k_{ij}\dot q^i\dot q^j = 0$. *Example use:* geodesics on a sphere, on a surface in $\mathbb{R}^3$, on a general Riemannian manifold (see [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]]).

**Source: a field theory.** $L \to \mathcal{L}(\phi, \partial_\mu\phi)$ on infinite-dimensional field-configuration space. Stationary action gives the field equations as PDEs. *Example use:* Maxwell's equations from $\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$; the Klein–Gordon equation from $\mathcal{L} = \tfrac{1}{2}\partial_\mu\phi\,\partial^\mu\phi - \tfrac{1}{2}m^2\phi^2$.

**Targets (Output Amplification).**

The conclusion "Euler–Lagrange equations hold" combined with other facts gives many consequences.

**Target + Noether's theorem = conserved quantities.** A continuous symmetry of the Lagrangian (i.e., a 1-parameter family of transformations under which $L$ is invariant) produces a conserved quantity along EL trajectories. *Combination use:* derive momentum, angular momentum, and energy conservation from translational, rotational, and time-translational symmetries.

**Target + Legendre transform = Hamilton's equations.** For a regular Lagrangian, the EL equations on $TQ$ Legendre-transform to Hamilton's equations on $T^*Q$, giving the symplectic formulation. *Combination use:* convert any Lagrangian problem to a Hamiltonian one, and vice versa.

**Target + numerical integration = trajectory simulation.** The EL equations are a system of second-order ODEs that can be solved numerically. Variational integrators (which discretize the variational principle directly) preserve symmetries and conservation laws better than naive ODE integrators. *Combination use:* compute trajectories of solar-system bodies, of constrained mechanical systems, of robotic manipulators.

**Target + path integrals = quantum dynamics.** In Feynman's path-integral formulation, the quantum amplitude is a sum over paths weighted by $e^{iS/\hbar}$. The classical EL trajectory is the stationary-phase point in the limit $\hbar \to 0$. *Combination use:* WKB approximation, instantons, semiclassical analysis of quantum systems.

---

# Why Is It True

**The mechanism in one sentence:** *the variation of the action separates into a "boundary term" (which vanishes by the fixed-endpoint condition) and a "bulk term" whose vanishing for all variations forces the Euler–Lagrange equations pointwise, by the fundamental lemma of the calculus of variations.*

Here is the calculation. Take a variation $\gamma_s$ of $\gamma$ with $\gamma_0 = \gamma$ and variation field $\delta\gamma$. The variation of the velocity is $\delta\dot\gamma = (\partial^2\gamma_s/\partial s\partial t)|_{s=0} = (d/dt)\delta\gamma$ — the time derivative of the position variation.

The variation of the action is:
$$\frac{d}{ds}\bigg|_{s=0} S[\gamma_s] = \int_a^b \frac{d}{ds}\bigg|_{s=0} L(\gamma_s(t), \dot\gamma_s(t), t)\, dt = \int_a^b \left(\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial \dot q^i}\delta\dot q^i\right) dt,$$

where I've used the chain rule, with $\delta q^i := (\delta\gamma)^i$ and $\delta\dot q^i = (d/dt)\delta q^i$.

**Integrate the second term by parts**:
$$\int_a^b \frac{\partial L}{\partial \dot q^i}\frac{d\delta q^i}{dt}\, dt = \left[\frac{\partial L}{\partial \dot q^i}\delta q^i\right]_a^b - \int_a^b \frac{d}{dt}\frac{\partial L}{\partial \dot q^i}\delta q^i \, dt.$$

The boundary term vanishes because $\delta q^i(a) = \delta q^i(b) = 0$ (fixed endpoints). So:

$$\frac{d}{ds}\bigg|_{s=0} S[\gamma_s] = \int_a^b \left(\frac{\partial L}{\partial q^i} - \frac{d}{dt}\frac{\partial L}{\partial \dot q^i}\right)\delta q^i\, dt.$$

This vanishes for **every** smooth variation $\delta q^i$ vanishing at the endpoints. By the **fundamental lemma of the calculus of variations** (a continuous function $f(t)$ with $\int_a^b f(t)\phi(t)dt = 0$ for every smooth $\phi$ vanishing at $a, b$ must be identically zero), the integrand must vanish:

$$\frac{\partial L}{\partial q^i} - \frac{d}{dt}\frac{\partial L}{\partial \dot q^i} = 0, \quad i = 1, \dots, n.$$

These are the **Euler–Lagrange equations**.

**Why the boundary term vanishes:** because we impose the *fixed-endpoint* condition on variations. This is essential — without it, the EL equations would carry boundary terms, and the principle would be different (it would be a "free-endpoint" variational principle with associated **natural boundary conditions** at the endpoints).

**Why coordinate-free:** the EL equations $\partial L/\partial q^i - (d/dt)(\partial L/\partial \dot q^i) = 0$ transform tensorially under coordinate changes on $Q$. The proof: the action $S$ is a *number*, invariant under coordinate changes; the variation is similarly coordinate-invariant; hence the EL equations, being the necessary conditions, are coordinate-invariant. (This is in contrast to Newton's law $m\ddot q = -\nabla V$, which in non-Euclidean coordinates picks up Christoffel-symbol terms that "should not be there".)

---

# What Makes This Hard

The proof itself is a straightforward calculus-of-variations argument, but several subtleties trip up beginners. (1) The variation of the velocity $\delta\dot\gamma = (d/dt)\delta\gamma$ is the **time derivative of the position variation** — not an independent variation. This is the most common source of confusion: students initially think $\delta q$ and $\delta\dot q$ can be varied independently. (2) The **fixed-endpoint condition** $\delta q(a) = \delta q(b) = 0$ is essential — without it, boundary terms remain and the equations are different. (3) The **fundamental lemma** requires the variation to range over a sufficiently rich class of functions (smooth, compactly supported in $(a, b)$) to conclude pointwise vanishing of the integrand. (4) The EL equations are **second-order ODEs** when $L$ is regular — the "$d/dt$" acting on $\partial L/\partial \dot q^i$ introduces $\ddot q$, giving a second-order system. (5) The coordinate-invariance of EL is non-obvious without the geometric setup — it requires that the action is coordinate-invariant and the variations are coordinate-invariant, which together force the EL conditions to be coordinate-invariant.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Compute the variation $\delta S[\gamma]$ by chain rule; integrate by parts to convert $\delta\dot q$ into $-(d/dt)\partial L/\partial \dot q^i$; discard the boundary term by fixed-endpoint; apply the fundamental lemma to conclude the integrand is zero, giving EL.

**Subgoal decomposition:**

1. **Express $\delta S$ via chain rule.** $\delta S = \int (\partial L/\partial q^i \delta q^i + \partial L/\partial \dot q^i \delta \dot q^i)dt$.
   - *Hint:* chain rule on $L(\gamma_s, \dot\gamma_s, t)$ differentiated at $s = 0$.
   - *Why needed:* first step in the variation calculation.

2. **Use $\delta\dot q = d(\delta q)/dt$.** Since $\dot\gamma_s = d\gamma_s/dt$, we have $\delta\dot\gamma = d(\delta\gamma)/dt$.
   - *Hint:* commutativity of $\partial/\partial s$ and $\partial/\partial t$ for smooth functions.
   - *Why needed:* sets up integration by parts.

3. **Integrate the second term by parts.** Convert $(\partial L/\partial \dot q^i)d(\delta q^i)/dt$ into $d[(\partial L/\partial \dot q^i)\delta q^i]/dt - (d/dt)(\partial L/\partial \dot q^i)\delta q^i$.
   - *Hint:* standard integration by parts in $t$.
   - *Why needed:* converts the velocity-variation term into a position-variation term plus a boundary term.

4. **Discard boundary term.** The fixed-endpoint condition $\delta q(a) = \delta q(b) = 0$ kills the boundary term $[(\partial L/\partial \dot q^i)\delta q^i]_a^b$.
   - *Hint:* fixed endpoints.
   - *Why needed:* removes the boundary contribution, leaving only the bulk integral.

5. **Apply the fundamental lemma of the calculus of variations.** $\int_a^b [\partial L/\partial q^i - (d/dt)\partial L/\partial \dot q^i]\delta q^i\, dt = 0$ for every fixed-endpoint variation $\delta q$ implies the bracket is zero pointwise.
   - *Hint:* fundamental lemma of CoV.
   - *Why needed:* concludes the Euler–Lagrange equations from the integral condition.

6. **Verify coordinate-invariance.** The action $S$ is intrinsic (coordinate-free); variations $\delta\gamma$ are intrinsic; hence EL is intrinsic, holds in every chart.
   - *Hint:* geometric reasoning.
   - *Why needed:* ensures EL is a genuine equation on $Q$, not a chart-dependent statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\delta\dot\gamma = d(\delta\gamma)/dt$
> **Statement:** For a smooth variation $\gamma_s$ of $\gamma$, the variation of the velocity equals the time derivative of the position variation: $\partial\dot\gamma_s/\partial s|_{s=0} = d(\partial\gamma_s/\partial s|_{s=0})/dt$.
>
> **Hint:** Commutativity of $\partial/\partial s$ and $\partial/\partial t$.
>
> **Why needed:** Sets up integration by parts.
>
> > [!note]- Full proof
> > $\dot\gamma_s(t) := \partial\gamma_s/\partial t$. So $\partial\dot\gamma_s/\partial s = \partial^2\gamma_s/\partial s\partial t$. By the equality of mixed partials (smoothness of $\gamma_s$ in both $s$ and $t$), $\partial^2\gamma_s/\partial s\partial t = \partial^2\gamma_s/\partial t\partial s = (d/dt)(\partial\gamma_s/\partial s)$. Evaluating at $s = 0$: $\delta\dot\gamma = (d/dt)\delta\gamma$.

> [!note]- Lemma 2: Fundamental lemma of the calculus of variations
> **Statement:** Let $f : [a, b] \to \mathbb{R}$ be a continuous function. If $\int_a^b f(t)\phi(t)\,dt = 0$ for every smooth $\phi$ with $\phi(a) = \phi(b) = 0$, then $f(t) = 0$ for all $t \in [a, b]$.
>
> **Hint:** If $f(t_0) \neq 0$ at some $t_0$, construct a bump function $\phi$ supported near $t_0$ with $\int f\phi > 0$ — contradiction.
>
> **Why needed:** Converts the integral condition $\int(\cdots)\delta q\,dt = 0$ for all variations to the pointwise condition.
>
> > [!note]- Full proof
> > Suppose $f(t_0) \neq 0$ for some $t_0 \in (a, b)$; without loss of generality $f(t_0) > 0$. By continuity, $f(t) > f(t_0)/2 > 0$ on a neighbourhood $(t_0 - \delta, t_0 + \delta) \subset (a, b)$. Take a smooth bump function $\phi$ supported in this neighbourhood, with $\phi \geq 0$ and $\phi(t_0) = 1$. Then $\int_a^b f\phi\,dt \geq (f(t_0)/2)\int_a^b \phi\,dt > 0$ — contradicting the assumption. So $f \equiv 0$ on $(a, b)$; by continuity, $f \equiv 0$ on $[a, b]$.

> [!note]- Lemma 3: Coordinate-invariance of EL
> **Statement:** The Euler–Lagrange equations are tensorial under smooth coordinate changes on $Q$: if they hold in one chart, they hold in every chart.
>
> **Hint:** The action $S$ is a coordinate-invariant integral; the variational condition is coordinate-invariant; hence the necessary conditions are coordinate-invariant.
>
> **Why needed:** Ensures EL is a genuine equation on $Q$, not a chart-dependent statement.
>
> > [!note]- Full proof
> > The action $S[\gamma] = \int L(\gamma, \dot\gamma, t)\,dt$ is intrinsic: $L$ is a function on $TQ$, $\gamma$ and $\dot\gamma$ are intrinsic. Under a smooth coordinate change $q \to \tilde q(q)$, the chain rule transforms $\dot q$ to $\dot{\tilde q} = (\partial \tilde q/\partial q)\dot q$, and $L$ transforms as a scalar (its value depends only on the geometric point in $TQ$, not the chart). The action $S$ is therefore the same number computed from either chart. Variations $\delta\gamma$ are intrinsic vector fields along $\gamma$; in coordinates, $\delta\tilde q^j = (\partial\tilde q^j/\partial q^i)\delta q^i$.
> >
> > The variational condition $(d/ds)|_{s=0}S[\gamma_s] = 0$ is intrinsic, hence the resulting Euler–Lagrange equations are intrinsic: they hold in any chart iff they hold in any other. A direct calculation verifies this: the EL equation $\partial L/\partial q^i - (d/dt)\partial L/\partial \dot q^i = 0$ in one chart implies the same equation in another chart, with appropriate index changes by the chain rule.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $Q$ be a smooth manifold, $L : TQ \times \mathbb{R} \to \mathbb{R}$ a smooth Lagrangian, and $\gamma : [a, b] \to Q$ a smooth curve.
>
> **Step 1 — Setup.** Take a smooth variation $\gamma_s : [a, b] \to Q$ with $\gamma_0 = \gamma$ and $\gamma_s(a) = \gamma(a)$, $\gamma_s(b) = \gamma(b)$ for all $s$ in a neighbourhood of $0$. Let $\delta\gamma := \partial\gamma_s/\partial s|_{s=0}$, a vector field along $\gamma$ with $\delta\gamma(a) = \delta\gamma(b) = 0$. Work in a chart $(U, q^i)$ on $Q$ covering $\gamma([a, b])$ (if necessary, decompose $[a, b]$ into subintervals each in one chart and handle them separately).
>
> **Step 2 — Chain rule on the action.** Compute the variation of the action:
> $$\frac{d}{ds}\bigg|_{s=0} S[\gamma_s] = \frac{d}{ds}\bigg|_{s=0} \int_a^b L(\gamma_s(t), \dot\gamma_s(t), t)\, dt.$$
> Exchanging differentiation under the integral (justified by smoothness):
> $$= \int_a^b \frac{d}{ds}\bigg|_{s=0} L(\gamma_s, \dot\gamma_s, t)\, dt = \int_a^b \left(\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial \dot q^i}\delta\dot q^i\right) dt,$$
> by the chain rule, with $\delta q^i = (\delta\gamma)^i$ and $\delta\dot q^i = (\delta\dot\gamma)^i$ in the chart coordinates.
>
> **Step 3 — Use $\delta\dot\gamma = d(\delta\gamma)/dt$.** By Lemma 1, $\delta\dot q^i = d(\delta q^i)/dt$. Substitute:
> $$\delta S = \int_a^b \left(\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial \dot q^i}\frac{d\delta q^i}{dt}\right) dt.$$
>
> **Step 4 — Integration by parts on the second term.** $\int_a^b (\partial L/\partial \dot q^i)(d\delta q^i/dt)dt = [(\partial L/\partial \dot q^i)\delta q^i]_a^b - \int_a^b (d/dt)(\partial L/\partial \dot q^i)\delta q^i\, dt$.
>
> The boundary term $[(\partial L/\partial \dot q^i)\delta q^i]_a^b$ vanishes because $\delta q^i(a) = \delta q^i(b) = 0$ (fixed-endpoint condition).
>
> So:
> $$\delta S = \int_a^b \left(\frac{\partial L}{\partial q^i} - \frac{d}{dt}\frac{\partial L}{\partial \dot q^i}\right)\delta q^i\, dt.$$
>
> **Step 5 — Apply fundamental lemma (Lemma 2).** $\gamma$ is a stationary point iff $\delta S = 0$ for *every* smooth fixed-endpoint variation $\delta q^i$. By the fundamental lemma (applied to each component $i$ separately, and noting that the variations $\delta q^i$ can be chosen as arbitrary smooth functions vanishing at $a$ and $b$):
> $$\frac{\partial L}{\partial q^i}\big(\gamma, \dot\gamma, t\big) - \frac{d}{dt}\frac{\partial L}{\partial \dot q^i}\big(\gamma, \dot\gamma, t\big) = 0, \quad i = 1, \dots, n,$$
> at every $t \in [a, b]$.
>
> Conversely, if the EL equations hold, then $\delta S = 0$ for every fixed-endpoint variation. So the two conditions are equivalent.
>
> **Step 6 — Coordinate invariance (Lemma 3).** The EL equations transform tensorially under coordinate changes on $Q$, so they hold in one chart iff they hold in every chart.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fermat's principle in optics.** Light traveling through a medium with refractive index $n(x)$ takes the path of stationary optical path length: the action is $S = \int n(x)\,ds$ where $ds$ is arc length. The Lagrangian (parameterizing by, say, $x^1$) is $L = n(x)\sqrt{1 + |\dot x^\perp|^2}$ where $\dot x^\perp$ is the velocity in the directions orthogonal to $x^1$. Hamilton's principle gives the **eikonal equation** governing light rays, which in homogeneous media reduces to straight-line propagation and in inhomogeneous media gives Snell's law and refraction.

**Einstein–Hilbert action and general relativity.** The action for general relativity is $S[g] = \int R\sqrt{-g}\,d^4x$, where $R$ is the Ricci scalar and $g$ the spacetime metric. The variational principle $\delta S = 0$ with respect to the metric $g_{\mu\nu}$ produces Einstein's field equations $R_{\mu\nu} - \tfrac{1}{2}Rg_{\mu\nu} = 0$ (vacuum). Adding matter via $S_{\text{matter}} = \int \mathcal{L}_{\text{matter}}\sqrt{-g}\,d^4x$ gives the full Einstein equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ with stress-energy on the right. The variational principle is the cleanest formulation of GR, manifestly diffeomorphism-invariant.

**Quantum mechanics: path integrals.** The propagator $\langle q_f|e^{-i\hat H T/\hbar}|q_i\rangle$ is the path integral $\int e^{iS[\gamma]/\hbar}\mathcal{D}[\gamma]$ over all paths from $q_i$ to $q_f$, weighted by the action. The classical limit $\hbar \to 0$ is dominated by the stationary-phase paths — exactly the Euler–Lagrange trajectories. The path integral is the natural quantization in the Lagrangian framework and is the standard tool in modern quantum field theory.

**Minimal surface problem.** The action for a surface $z = u(x, y)$ in $\mathbb{R}^3$ is $S = \int \sqrt{1 + |\nabla u|^2}\,dA$ — the surface area. The Euler–Lagrange equation gives the **minimal-surface equation** $\nabla \cdot (\nabla u/\sqrt{1+|\nabla u|^2}) = 0$, equivalent to mean-curvature zero. Solutions include the plane, the catenoid, the helicoid, and the Scherk surfaces. The variational formulation makes the geometry of these surfaces transparent.

---

# Bridges

- **[[Thm - Equivalence of Lagrangian and Hamiltonian Formalisms]]**: this theorem is one half of the equivalence — EL equations on $TQ$. Hamilton's equations on $T^*Q$ are the other half, and the [[Def - The Legendre Transform|Legendre transform]] is the bridge. Together they say: the same dynamical content can be described variationally on $TQ$ or symplectically on $T^*Q$.

- **Noether's theorem (variational version)**: every continuous symmetry of the Lagrangian produces a conserved quantity along EL trajectories. The proof is a one-line application of the EL equations: if $L(\gamma_s, \dot\gamma_s, t) = L(\gamma, \dot\gamma, t)$ for a 1-parameter family $\gamma_s$, then differentiating in $s$ and using EL gives $(d/dt)(\xi^i \partial L/\partial \dot q^i) = 0$, where $\xi = \partial\gamma_s/\partial s|_{s=0}$ — the conserved quantity is $\xi^i \partial L/\partial \dot q^i$ (the "Noether charge"). The bridge to the Hamiltonian/symplectic version is via the moment map.

- **Calculus of variations**: this theorem is one instance of the **general Euler–Lagrange equations** in the calculus of variations. The same proof structure applies to higher-order Lagrangians, multi-variable Lagrangians (field theories), and constrained variational problems. The bridge: the Euler–Lagrange equations are the universal first-order necessary conditions for stationarity of an integral functional.

- **Geodesic equation in Riemannian geometry**: for $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$, the EL equations are the geodesic equations $\ddot q^k + \Gamma^k_{ij}\dot q^i\dot q^j = 0$. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for the full development of geodesic flows as a variational problem.

---

# Unlocked by This

> [!tip] Noether's Theorem (Variational Version) *(from Classical Mechanics)*
> Every continuous symmetry of the Lagrangian produces a conserved current along EL trajectories. For a 1-parameter group of transformations $\gamma_s$ with $L(\gamma_s, \dot\gamma_s, t) = L(\gamma, \dot\gamma, t)$ (i.e., $L$ is invariant), the conserved quantity is the **Noether charge** $J := \xi^i (\partial L/\partial \dot q^i)$ where $\xi = (d\gamma_s/ds)|_{s=0}$. For Lagrangians invariant under translations, $J$ is the linear momentum; under rotations, the angular momentum; under time-translation (autonomous Lagrangian), the energy $E = \dot q^i \partial L/\partial \dot q^i - L$. Noether's theorem is the **deepest single result in classical mechanics**, providing a one-to-one correspondence between continuous symmetries and conservation laws.

> [!tip] Field Theory and the Euler–Lagrange PDE *(from Mathematical Physics)*
> The Euler–Lagrange formalism extends from finite-dimensional Lagrangians to **Lagrangian densities** $\mathcal{L}(\phi, \partial_\mu\phi)$ for field theory. The action is $S[\phi] = \int \mathcal{L}\,d^4x$, and the EL equations become PDEs:
> $$\frac{\partial \mathcal{L}}{\partial \phi} - \partial_\mu\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)} = 0.$$
> All classical field theories — electromagnetism, gauge theories (Yang–Mills, the Standard Model), general relativity, the Klein–Gordon and Dirac equations of relativistic quantum mechanics — are derived from this variational principle. The Lagrangian density is the fundamental object; the field equations are derived.

> [!tip] Path Integral Quantization *(from Quantum Field Theory)*
> Feynman's **path integral** formulation of quantum mechanics generalizes the variational principle: the quantum amplitude $\langle f|i\rangle$ is the integral $\int e^{iS[\gamma]/\hbar}\mathcal{D}[\gamma]$ over all paths from $i$ to $f$, weighted by the classical action. In the limit $\hbar \to 0$, the integral is dominated by the stationary-phase points — the classical EL trajectories. The path integral is the natural language for **quantum field theory**, gauge theory quantization, and Standard Model calculations. It preserves manifest Lorentz invariance (where canonical quantization breaks it) and provides the Feynman-rules generating functional that underlies all of perturbative QFT.
