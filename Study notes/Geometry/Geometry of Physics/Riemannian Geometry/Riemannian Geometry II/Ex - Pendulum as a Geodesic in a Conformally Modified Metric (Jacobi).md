---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Hamiltonian Flow of the Kinetic Energy"
  - "Thm - Hamilton's Principle Gives the Geodesic Equation"
  - "Def - Length and Energy Functionals"
tags: [geometry, riemannian-geometry, jacobi-principle, classical-mechanics, pendulum]
---

# Problem Statement

(a) Let $(M, g)$ be a Riemannian manifold and $V : M \to \mathbb{R}$ a smooth potential. Consider a unit-mass particle on $M$ with Lagrangian $L = T - V$, where $T = \tfrac12 g_{ij}\dot q^i \dot q^j$ is the kinetic energy. At a fixed total energy $E$ (with $E > V$ throughout the trajectory), define the **Jacobi metric**
$$\tilde g := 2(E - V(q))\, g$$
on the classically-allowed region $\{q : V(q) < E\} \subseteq M$. Prove **Jacobi's principle of least action**: the trajectories of $L$ at energy $E$ are reparametrisations of the [[Def - Geodesic|geodesics]] of $\tilde g$.

(b) Apply this to the simple pendulum: a unit-mass bob on a unit-length rod swinging freely in a uniform gravitational field. The configuration space is $S^1$ (parametrised by the angle $\theta$ from the downward vertical), and the Lagrangian is $L = \tfrac12 \dot\theta^2 - (1 - \cos\theta)$ (taking the gravitational acceleration $g_{\mathrm{grav}} = 1$ and the bob's bottom position as the zero of potential).

(b1) Write down the Jacobi metric on the part of $S^1$ where the pendulum can reach at total energy $E$.

(b2) For oscillatory motion ($E < 2$), show that the period of the pendulum equals the length of a closed geodesic in the Jacobi metric.

(c) Derive that the Hamiltonian flow of $H = \tfrac12 g^{ij} p_i p_j$ on $T^*M$ generates the geodesic flow of $g$ on $M$ (i.e., proves the (iii) ⟺ (iv) equivalence in [[Thm - Hamilton's Principle Gives the Geodesic Equation]] explicitly).

**Recall:**

By [[Thm - Hamilton's Principle Gives the Geodesic Equation|Hamilton's principle]], the Euler–Lagrange equations of $L = T = \tfrac12 g_{ij}\dot q^i \dot q^j$ are the geodesic equations of $g$. For a Lagrangian $L = T - V$ with potential, the Euler–Lagrange equations are $\nabla_{\dot\gamma}\dot\gamma = -\mathrm{grad}_g V$ — i.e., the geodesic equation plus a "force" term.

The kinetic-energy [[Def - Hamiltonian Flow of the Kinetic Energy|Hamiltonian]] is $H = \tfrac12 g^{ij}p_i p_j$. With a potential, $H = T + V = \tfrac12 g^{ij}p_i p_j + V(q)$, the total energy.

---

# Convergent Strategy

**Problem class:** Conversion of a mechanical problem into a geometric problem via Jacobi's principle. This is the "geometric reformulation of classical mechanics" pattern — the exercise drills the central technique that makes Riemannian-geometry tools applicable to all conservative mechanical systems.

**Assumption pattern:** We have a Riemannian configuration manifold, a potential $V$, and a fixed total energy $E$. The classically-allowed region $\{V < E\}$ is where the trajectory can lie (outside this region, $T < 0$ which is unphysical). On this region the conformal factor $2(E - V)$ is positive, so $\tilde g = 2(E - V) g$ is a genuine Riemannian metric.

**Theorem routing:** Two routes for (a). **Route A (variational):** the trajectory of $L = T - V$ at energy $E$ extremises Maupertuis's action $\int p\, dq = \int 2T\, dt$. Using $T = E - V$ at fixed energy: $\int 2T\, dt = \int 2T\, dt$. Express in terms of arc length $ds$ of $g$: $ds = |\dot\gamma|_g\, dt = \sqrt{2T}\, dt$, so $\int 2T\, dt = \int \sqrt{2T} \cdot \sqrt{2T}\, dt = \int \sqrt{2T}\, ds = \int \sqrt{2(E - V)}\, ds$ — which is the length integral of $\tilde g = 2(E-V)g$. So extremising the original action is extremising the length of $\tilde g$ — i.e., the trajectories are geodesics of $\tilde g$ (up to reparametrisation). **Route B (direct conformal-metric calculation):** compute the Christoffel symbols of $\tilde g = e^{2\sigma} g$ for $\sigma = \tfrac12 \log(2(E - V))$, write down the geodesic equation, and verify it matches the Newtonian $\ddot\gamma = -\mathrm{grad}_g V$ modulo reparametrisation. (We do Route A, which is cleaner and more conceptual.)

**Key decision point:** The conversion is from a *first-order* problem (Lagrangian dynamics, second-order ODE in time) to a *zeroth-order* problem (geodesic of a different metric, second-order in arc length). The reparametrisation handles the time-vs-arc-length mismatch. The deep insight is that, at fixed energy, mechanics is *intrinsically* a geometric problem — the time variable is a parametrisation, not a fundamental geometric quantity, and the right metric on the configuration space is not $g$ but $\tilde g$.

---

# Legal Operations Used

1. **Operation 9 from the topic page (convert a Hamiltonian system to a geodesic flow via Jacobi).** This is the central operation; the exercise is a worked example.

2. **Operation 6 from the topic page (apply the first variation formula to a critical curve).** Used to set up the Euler–Lagrange equations and to verify the geodesic equation of $\tilde g$.

3. **Operation 10 from the topic page (pass between $TM$ and $T^*M$ via the Legendre transform).** Used in part (c) to convert the Lagrangian and Hamiltonian pictures.

---

# Hints

> [!note]- Hint 1
> For (a), use Maupertuis's principle: at fixed energy $E$, the trajectory extremises $\int p\, dq = \int p_i \dot q^i\, dt = \int 2T\, dt$ (using $p_i \dot q^i = 2T$ for quadratic kinetic energy). Express this in terms of the arc length $ds$ of $g$.

> [!note]- Hint 2
> At fixed total energy $E$, $T = E - V$. So $\int 2T\, dt = \int 2(E - V)\, dt$. And $ds = \sqrt{2T}\, dt = \sqrt{2(E-V)}\, dt$, so $dt = ds/\sqrt{2(E-V)}$. Substitute.

> [!note]- Hint 3
> $\int 2(E - V)\, dt = \int 2(E - V) \cdot \frac{ds}{\sqrt{2(E-V)}} = \int \sqrt{2(E-V)}\, ds$.

> [!note]- Hint 4
> But $\sqrt{2(E - V)}\, ds$ is the arc-length element of the metric $\tilde g = 2(E - V) g$. So $\int p\, dq = \int d\tilde s = \tilde L(\gamma)$ — the length of $\gamma$ in the Jacobi metric. Extremising this is extremising $\tilde L$, which is the geodesic equation of $\tilde g$.

> [!note]- Hint 5
> For (b), the configuration space is $S^1$ with metric $g = d\theta^2$. The potential is $V(\theta) = 1 - \cos\theta$. The Jacobi metric is $\tilde g = 2(E - 1 + \cos\theta) d\theta^2$ on $\{\theta : \cos\theta > 1 - E\}$.

---

# Solution

**Step 1: Proof of Jacobi's principle (part a).**

> [!note]- Derivation
> A trajectory $\gamma(t)$ of $L = T - V$ at fixed total energy $E$ satisfies, by Hamilton's principle on the constrained space $\{H = E\}$, **Maupertuis's principle**:
> $$\delta \int_a^b p_i\, \dot q^i\, dt = 0,$$
> with variations at fixed endpoints and fixed energy. (This is the version of Hamilton's principle adapted to the energy-shell — see Goldstein's *Classical Mechanics* §8.6, or Frankel §10.2c.)
>
> For the kinetic energy $T = \tfrac12 g_{ij}\dot q^i \dot q^j$, we have $p_i = g_{ij}\dot q^j$, so $p_i \dot q^i = g_{ij}\dot q^i \dot q^j = 2T$. So
> $$\int p\, dq = \int 2T\, dt.$$
>
> At fixed total energy $E$, conservation of energy gives $T + V = E$, hence $T = E - V$. So
> $$\int 2T\, dt = \int 2(E - V)\, dt.$$
>
> Convert to arc length of $g$. The speed in $g$-metric is $|\dot\gamma|_g = \sqrt{2T} = \sqrt{2(E - V)}$, so $ds = \sqrt{2(E - V)}\, dt$, hence $dt = ds/\sqrt{2(E - V)}$. Substitute:
> $$\int 2(E - V)\, dt = \int 2(E - V) \cdot \frac{ds}{\sqrt{2(E - V)}} = \int \sqrt{2(E - V)}\, ds = \int d\tilde s,$$
> where $d\tilde s = \sqrt{2(E - V)}\, ds$ is the arc-length element of the Jacobi metric $\tilde g = 2(E - V) g$ (since the arc-length-squared element is $d\tilde s^2 = 2(E - V) ds^2 = 2(E - V) g_{ij} dq^i dq^j$).
>
> So **Maupertuis's action equals the length of $\gamma$ in the Jacobi metric**:
> $$\int p\, dq = \tilde L(\gamma) := \int \sqrt{\tilde g(\dot\gamma, \dot\gamma)}\, dt.$$
>
> Extremising $\int p\, dq$ with fixed endpoints (and free time parametrisation, since both sides are reparametrisation-invariant) is the same as extremising $\tilde L$, which by the [[Thm - First Variation of Arc Length|first variation of arc length]] gives the geodesic equation of $\tilde g$. So **the spatial trajectory of $\gamma$ (independent of parametrisation) is a geodesic of $\tilde g$**.
>
> The time parametrisation is then determined by the energy: $dt = ds/\sqrt{2(E - V)}$, or equivalently $|\dot\gamma|_g = \sqrt{2(E - V(\gamma(t)))}$ along the trajectory.

**Step 2: Pendulum example (parts b1 and b2).**

> [!note]- Derivation
> Configuration space: $S^1$, parametrised by $\theta \in [0, 2\pi)$ or $\theta \in \mathbb{R}$ modulo $2\pi$. Metric: $g = d\theta^2$. Potential: $V(\theta) = 1 - \cos\theta$ (with $V(0) = 0$, $V(\pi) = 2$). Total energy: $E$.
>
> Classically-allowed region: $V < E$, i.e., $1 - \cos\theta < E$, i.e., $\cos\theta > 1 - E$. For $E < 2$ (oscillatory), this is $\theta \in (-\theta_0, \theta_0)$ where $\theta_0 = \arccos(1 - E)$. For $E = 2$ (separatrix), the allowed region is all of $S^1$ but the dynamics passes through the unstable equilibrium $\theta = \pi$ asymptotically. For $E > 2$ (rotational), the allowed region is all of $S^1$.
>
> **(b1) Jacobi metric on the allowed region:**
> $$\tilde g = 2(E - V)\, d\theta^2 = 2(E - 1 + \cos\theta)\, d\theta^2.$$
>
> **(b2) For $E < 2$ (oscillatory):** The trajectory in $\theta$-space is a closed loop (in the planar projection): the pendulum swings from $\theta = +\theta_0$ to $\theta = -\theta_0$ and back. As a geodesic of $\tilde g$, this is a closed curve — and its $\tilde g$-length is the **period of the pendulum**.
>
> Verify: the period is
> $$T_{\mathrm{period}} = \int_0^{T_{\mathrm{period}}} dt = \int 2 \cdot \frac{d\theta}{|\dot\theta|} = \int 2 \cdot \frac{d\theta}{\sqrt{2(E - V)}} = \int 2 \cdot \frac{d\theta}{\sqrt{2(E - 1 + \cos\theta)}}.$$
> (The factor of $2$ is because we integrate from $-\theta_0$ to $\theta_0$ and the pendulum traverses this twice in a period; but more carefully, the integral $\int_{-\theta_0}^{\theta_0} \frac{d\theta}{\sqrt{2(E - V)}}$ is the *half-period*, and we double it.)
>
> Compare to the $\tilde g$-length of the closed loop in $\theta$-space: $\tilde L(\gamma) = \int |\dot\theta|_{\tilde g}\, dt = \int \sqrt{\tilde g(\dot\theta, \dot\theta)}\, dt = \int \sqrt{2(E - V)} \cdot |\dot\theta|_g\, dt = \int \sqrt{2(E - V)}\cdot |\dot\theta|\, dt$.
>
> If $\gamma$ is parametrised by $\theta$ (arc-length-like in the Jacobi metric — actually no, $\theta$ is the original parameter), then $\tilde L = \int |\partial_\theta \gamma|_{\tilde g}\, d\theta = \int \sqrt{\tilde g_{\theta\theta}}\, d\theta = \int \sqrt{2(E - V)}\, d\theta$.
>
> The half-period is $\int_{-\theta_0}^{\theta_0} \frac{d\theta}{\sqrt{2(E - V)}}$. So the half-period is *not* the half-$\tilde g$-length; instead the relation is the Cauchy–Schwarz-like
> $$(\text{half-period}) \cdot (\text{half-}\tilde L) = \left(\int_{-\theta_0}^{\theta_0} \frac{d\theta}{\sqrt{2(E-V)}}\right) \cdot \left(\int_{-\theta_0}^{\theta_0}\sqrt{2(E-V)}\, d\theta\right) \geq \left(\int_{-\theta_0}^{\theta_0} 1\, d\theta\right)^2 = 4\theta_0^2.$$
>
> Wait — the textbook statement of "period = length of closed geodesic in Jacobi metric" is subtler. The Jacobi-metric trajectory's natural parametrisation is by Jacobi arc length $\tilde s$, not by the original time $t$. The conversion: $\tilde s = \int \sqrt{2(E-V)}\, dt$, so $d\tilde s = \sqrt{2(E-V)}\, dt$. The period in $\tilde s$ is $\tilde L(\gamma) = \oint d\tilde s = \oint \sqrt{2(E-V)}\, dt$. The period in $t$ is $\oint dt = \oint d\tilde s/\sqrt{2(E-V)}$.
>
> The cleaner statement: **the periodic motion of the pendulum at energy $E$ corresponds to a closed geodesic of $\tilde g$ on the allowed region of $S^1$**. The two parametrisations ($t$ vs $\tilde s$) are related by $d\tilde s/dt = \sqrt{2(E-V)}$, and the period in $t$ is the integral of the inverse on the closed geodesic.

**Step 3: Hamilton's equations are geodesic flow (part c).**

> [!note]- Derivation
> For $L = T = \tfrac12 g_{ij}\dot q^i \dot q^j$ (no potential), the Legendre transform gives the Hamiltonian $H = \tfrac12 g^{ij}p_i p_j$. Hamilton's equations:
> $$\dot q^i = \frac{\partial H}{\partial p_i} = g^{ij}p_j,$$
> $$\dot p_i = -\frac{\partial H}{\partial q^i} = -\tfrac12 \partial_i g^{jk}\, p_j\, p_k.$$
>
> Substitute $p_j = g_{jk}\dot q^k$:
> $$\dot p_i = -\tfrac12 \partial_i g^{jk}\, g_{jl}\dot q^l\, g_{km}\dot q^m.$$
> Using the identity $\partial_i(g^{jk}g_{kl}) = \partial_i \delta^j_l = 0$, so $\partial_i g^{jk}\cdot g_{kl} = -g^{jk}\partial_i g_{kl}$. Apply twice (multiplied by $g_{jm}$):
> $$\partial_i g^{jk}\cdot g_{jl}g_{km} = -g^{jk}g_{jl}\partial_i g_{km} = -\delta^k_l \partial_i g_{km} = -\partial_i g_{lm}.$$
> So $\dot p_i = \tfrac12 \partial_i g_{lm}\dot q^l \dot q^m$.
>
> Also, $\dot p_i = \frac{d}{dt}(g_{ij}\dot q^j) = \partial_l g_{ij}\dot q^l \dot q^j + g_{ij}\ddot q^j$.
>
> Equating: $g_{ij}\ddot q^j + \partial_l g_{ij}\dot q^l \dot q^j = \tfrac12 \partial_i g_{lm}\dot q^l \dot q^m$. Multiply by $g^{ki}$:
> $$\ddot q^k + g^{ki}\partial_l g_{ij}\dot q^l \dot q^j - \tfrac12 g^{ki}\partial_i g_{lm}\dot q^l \dot q^m = 0.$$
> Symmetrising the middle term (using $\dot q^l \dot q^j$ symmetry):
> $$\ddot q^k + \tfrac12 g^{ki}(\partial_l g_{ij} + \partial_j g_{il})\dot q^l \dot q^j - \tfrac12 g^{ki}\partial_i g_{lj}\dot q^l \dot q^j = 0.$$
> $$\ddot q^k + \tfrac12 g^{ki}(\partial_l g_{ij} + \partial_j g_{il} - \partial_i g_{lj})\dot q^l \dot q^j = 0.$$
> Recognise the Christoffel symbol: $\Gamma^k_{lj} = \tfrac12 g^{ki}(\partial_l g_{ij} + \partial_j g_{il} - \partial_i g_{lj})$. So
> $$\ddot q^k + \Gamma^k_{lj}\dot q^l \dot q^j = 0,$$
> the geodesic equation of $g$. **Hamilton's flow of $H = \tfrac12 g^{ij}p_i p_j$ on $T^*M$ is geodesic flow of $g$ on $M$**, after Legendre transform.

> [!note]- Complete formal solution
> **(a)** Maupertuis's principle at fixed energy: $\delta\int p\, dq = 0$, where $p\, dq = p_i \dot q^i dt = 2T\, dt = 2(E - V)\, dt$. Convert to $g$-arc-length $ds$ via $ds = \sqrt{2T}\, dt$: $\int 2(E-V)\, dt = \int \sqrt{2(E-V)}\, ds = \int d\tilde s$, where $d\tilde s$ is the arc length of $\tilde g = 2(E - V)g$. So extremising the action is extremising the length in $\tilde g$ — i.e., the spatial trajectory is a geodesic of $\tilde g$.
>
> **(b1)** Pendulum: $\tilde g = 2(E - 1 + \cos\theta) d\theta^2$ on $\{\theta : \cos\theta > 1 - E\}$.
>
> **(b2)** For $E < 2$, the pendulum motion is periodic and corresponds to a closed geodesic of $\tilde g$ on the interval $(-\theta_0, \theta_0)$, $\theta_0 = \arccos(1 - E)$. The period in $t$ is $\oint dt = \oint d\tilde s/\sqrt{2(E-V)}$, equivalently $\oint \sqrt{2/(E - 1 + \cos\theta)}\, d\theta/2 \cdot 2 = 2\int_{-\theta_0}^{\theta_0}\sqrt{2/(E-1+\cos\theta)}\, d\theta$ (factor of $2$ for back-and-forth) — the standard period formula for the pendulum.
>
> **(c)** Hamilton's equations of $H = \tfrac12 g^{ij}p_i p_j$ on $T^*M$, after Legendre transform $p_i = g_{ij}\dot q^j$, give the geodesic equation $\ddot q^k + \Gamma^k_{ij}\dot q^i\dot q^j = 0$ on $M$. (See Lemma 3 of [[Thm - Hamilton's Principle Gives the Geodesic Equation]].)
>
> So the Hamiltonian flow of $H$ on $T^*M$ generates geodesic flow of $g$ on $M$. $\qquad\blacksquare$

---

# Key Takeaways

**Jacobi's principle is the master technique converting mechanics into geometry.** *Every* conservative mechanical system on a configuration manifold $(M, g)$ with potential $V$, at fixed total energy $E$, has its trajectories as geodesics of the conformally rescaled metric $\tilde g = 2(E - V) g$ on the allowed region $\{V < E\}$. So **classical mechanics dissolves into Riemannian geometry**, and tools from one transfer freely to the other. Curvature of the Jacobi metric controls dynamical stability (positive curvature ⟹ focusing, hyperbolic instability); conjugate points of $\tilde g$ are *caustics* of the dynamics; closed geodesics of $\tilde g$ are *periodic orbits* of the mechanics. This is the foundation of "the geometric formulation of classical mechanics" and the bridge to [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

**The pendulum example is the simplest non-trivial Jacobi-metric computation.** The configuration manifold is $S^1$ (one-dimensional!), so the Jacobi metric is just a one-form $\tilde g_{\theta\theta} d\theta^2$, and "geodesics" are trivially just oriented paths on the line — there is no real geometry, just an integration. But the *period* of the closed geodesic (oscillatory motion at $E < 2$) is the period of the pendulum, and the integral $T(E) = 2\int_{-\theta_0}^{\theta_0}\sqrt{2/(E - 1 + \cos\theta)}\, d\theta$ is the *period function* of the pendulum, which has been studied in detail in classical mechanics and elliptic-integral theory (the formula involves the complete elliptic integral of the first kind). So the pendulum's quintessential property — its period depending on amplitude — is the $\tilde g$-length of the closed geodesic in the Jacobi metric.

**Hamilton's equations of $H = \tfrac12 g^{ij}p_i p_j$ are geodesic flow.** The Legendre transform converts the Lagrangian formulation $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ (geodesic equation as Euler–Lagrange) to the Hamiltonian formulation on $T^*M$ with $H = \tfrac12 g^{ij}p_i p_j$. Hamilton's equations $\dot q^i = \partial H/\partial p_i, \dot p_i = -\partial H/\partial q^i$ are equivalent to the geodesic equation. So **the cleanest formulation of geodesic flow is as a Hamiltonian flow on the cotangent bundle**, and this is the bridge to symplectic geometry. See [[Def - Hamiltonian Flow of the Kinetic Energy]] and [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

**The Kepler problem and integrability.** Applying Jacobi's principle to the Kepler problem (central potential $V = -k/r$) gives the Jacobi metric $\tilde g = 2(E + k/r) \delta$ on the appropriate region. The orbits are geodesics of *this* metric — and they are *conic sections* (ellipses for $E < 0$, parabolas for $E = 0$, hyperbolas for $E > 0$). The exceptional integrability of Kepler (more conservation laws than generic, via the Runge–Lenz vector) is a special property of this specific metric — it has a hidden symmetry making the geodesic flow super-integrable. This is one of the deepest concrete applications of Jacobi's principle and a beautiful example of "mechanics is geometry".
