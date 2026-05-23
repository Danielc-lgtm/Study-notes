---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Geodesic"
  - "Def - Length of a Curve and Riemannian Distance"
tags: [geometry, riemannian-geometry, variational-calculus]
---

# Notation

$(M, g)$ a Riemannian manifold; $\gamma : [a, b] \to M$ a piecewise smooth curve, with velocity $\dot\gamma(t) \in T_{\gamma(t)}M$. The Riemannian norm is $|\dot\gamma(t)| := \sqrt{g_{\gamma(t)}(\dot\gamma(t), \dot\gamma(t))}$. We use $T = \dot\gamma/|\dot\gamma|$ for the unit tangent when speaking of unit-speed reparametrisations. The full registry is at [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]]. **This is a compound page: it defines two interlocking functionals — length and energy — because they are introduced together, share the same critical points (geodesics), and play complementary roles in the variational theory.**

---

# Axiom Motivation

The motivating question is: **on a Riemannian manifold, what is the natural quantity to minimise to find [[Def - Geodesic|geodesics]], and what do we lose by choosing one over another?** The conventional answer in introductory expositions is "minimise the length," but this is technically incorrect in a subtle way that the energy functional fixes. Understanding *why* the energy is better — and what the length still does that the energy cannot — is the content of this definition.

**Length** $L(\gamma) = \int_a^b |\dot\gamma|\, dt$ is the natural geometric measurement: it counts the distance travelled along $\gamma$. It is **reparametrisation-invariant**: if $\tilde\gamma(s) = \gamma(\varphi(s))$ for any monotonic $\varphi$, then $L(\tilde\gamma) = L(\gamma)$. This is exactly what we want from a geometric quantity: the length of a path is a property of the *image* and not of any particular parametrisation.

Reparametrisation invariance is also what makes length *hard to vary*. The Euler–Lagrange equations associated to $L$ are degenerate: they say that the critical points are *unparametrised* geodesics, but they cannot pin down the parametrisation. The Hessian of $L$ at a critical point has a non-trivial kernel — the direction of reparametrisation — and any quadratic-form analysis (second variation, index form, conjugate points) is computed modulo this kernel. This is awkward at best and confusing at worst.

**Energy** $E(\gamma) = \tfrac12 \int_a^b g(\dot\gamma, \dot\gamma)\, dt = \tfrac12 \int_a^b |\dot\gamma|^2\, dt$ is the natural variational analogue of the kinetic energy of a particle traversing $\gamma$. The factor of $\tfrac12$ is conventional, matching the physics convention $T = \tfrac12 m v^2$ for kinetic energy of unit-mass particles. The energy is **not** reparametrisation-invariant — it depends on the speed at which the curve is traced, not just its image — but this is precisely what lets it pin down the parametrisation.

The Cauchy–Schwarz inequality
$$L(\gamma)^2 = \left(\int_a^b |\dot\gamma|\, dt\right)^2 \leq (b - a)\int_a^b |\dot\gamma|^2\, dt = 2(b - a)\, E(\gamma)$$
relates the two, with equality iff $|\dot\gamma|$ is constant — that is, iff $\gamma$ is parametrised at constant speed. So:

1. Among curves with fixed endpoints $(\gamma(a), \gamma(b))$ and fixed parameter interval $[a, b]$, minimising $E$ forces both $\gamma$ to minimise $L$ *and* to be constant-speed.
2. Among constant-speed curves with fixed endpoints, the two functionals have the same critical points (geodesics) and the same Hessians.
3. Critical points of $L$ alone (without the constant-speed constraint) are still geodesics, but only *up to reparametrisation* — the parametrisation is free.

So **the energy is the right functional for setting up the variational problem**: its critical points are *parametrised* geodesics, its Hessian is the index form $I$, and the variational analysis is non-degenerate. The length is the right functional for *interpreting* the result: it is what measures actual geometric distance.

A subtler design question is why the energy uses *the square* of velocity. The natural alternatives — $|\dot\gamma|$ (which gives length), $|\dot\gamma|^4$, $|\dot\gamma|^p$ for $p > 1$ — all have the same critical points up to reparametrisation, but only $p = 2$ has the Cauchy–Schwarz relation that ties speed-constancy to length-minimisation. The $p = 2$ choice is also forced by physics: the kinetic energy of a moving particle is quadratic in velocity, and the Euler–Lagrange equations of $\int (T - V)\, dt$ produce Newton's equations, with the kinetic energy appearing exactly as $T = \tfrac12 g_{ij}\dot q^i \dot q^j$. So the variational formulation of mechanics *forces* $p = 2$.

The relaxation worth flagging is the choice of *parametrisation interval*. We have written $[a, b]$ for the parameter range, and the energy depends on $b - a$ (rescaling by $t \mapsto ct$ changes $E$ by a factor of $1/c$). For variational arguments where we want a single functional independent of the parametrisation interval, we conventionally fix $[a, b] = [0, 1]$. The length is unaffected by this choice.

A final design point: **piecewise smooth** is the right regularity class. We allow $\gamma$ to have corners (jumps in $\dot\gamma$) because variations of smooth curves naturally produce piecewise smooth curves (a "broken Jacobi field" picks up a delta-function contribution at the break point), and the index-theorem analysis requires the broken class to extract the correct multiplicities. Smooth-only curves form a smaller class on which the same variational analysis works, but the broken class is the natural setting.

---

# The Definition

For a piecewise smooth curve $\gamma : [a, b] \to M$ on a Riemannian manifold $(M, g)$:

The **length functional** is
$$L(\gamma) := \int_a^b \sqrt{g_{\gamma(t)}(\dot\gamma(t), \dot\gamma(t))}\, dt = \int_a^b |\dot\gamma(t)|\, dt.$$
It is **reparametrisation-invariant**: $L(\gamma \circ \varphi) = L(\gamma)$ for any orientation-preserving piecewise-smooth $\varphi : [a', b'] \to [a, b]$.

The **energy functional** is
$$E(\gamma) := \frac{1}{2}\int_a^b g_{\gamma(t)}(\dot\gamma(t), \dot\gamma(t))\, dt = \frac{1}{2}\int_a^b |\dot\gamma(t)|^2\, dt.$$
It is **not** reparametrisation-invariant: $E$ depends on the speed at which $\gamma$ traces its image.

**Cauchy–Schwarz inequality:**
$$L(\gamma)^2 \leq 2(b - a)\, E(\gamma),$$
with equality if and only if $|\dot\gamma(t)|$ is constant (i.e., $\gamma$ is parametrised at constant speed).

**Critical points (geodesics).** A curve $\gamma$ with fixed endpoints is a critical point of $E$ (with respect to fixed-endpoint variations) if and only if $\gamma$ is a [[Def - Geodesic|geodesic]] satisfying $\nabla_{\dot\gamma}\dot\gamma = 0$. The same is true for $L$ if we restrict to constant-speed parametrisations; without this restriction, critical points of $L$ are unparametrised geodesics.

---

# Relate to Other Fields / Compression

**True name:** **the action functionals whose Euler–Lagrange equations are the geodesic equation**. Length is the geometric one (the "physical" measurement); energy is the variational one (the well-posed minimisation problem). The two are linked by Cauchy–Schwarz, and in practice the energy is the one used for setting up variational arguments while the length is used for interpreting answers.

**The energy is the action for the free particle.** In classical mechanics, the kinetic energy of a particle of unit mass moving along $\gamma$ is $T(t) = \tfrac12 |\dot\gamma(t)|^2$, and the action is $S = \int T\, dt = E(\gamma)$. Hamilton's principle says: free-particle trajectories minimise (or extremise) the action. So the geodesic equation, derived as the Euler–Lagrange equation of $E$, is *exactly* Newton's equation for the free particle on $(M, g)$. With a potential $V$, the Lagrangian becomes $L = T - V$ and the trajectories satisfy a modified equation — but Jacobi's principle then re-parametrises these into geodesics of a different metric. See [[Thm - Hamilton's Principle Gives the Geodesic Equation]] and the Jacobi-principle exercise.

**Connection to harmonic-map theory.** A harmonic map between Riemannian manifolds is a critical point of the energy $E(\varphi) = \tfrac12 \int |d\varphi|^2\, \mathrm{vol}_g$ — the higher-dimensional analogue of the curve energy. Harmonic maps generalise geodesics: a harmonic map from $(\mathbb{R}, dt^2)$ to $(M, g)$ is exactly a geodesic. The variational theory of geodesics is the warm-up for the variational theory of harmonic maps, minimal surfaces, and gauge connections.

---

# Examples / Corollaries

**Is an instance: a straight line in $\mathbb{R}^n$.** With $\gamma(t) = tv$ for $t \in [0, 1]$ and $v \in \mathbb{R}^n$: $L(\gamma) = |v|$ and $E(\gamma) = \tfrac12 |v|^2$. The Cauchy–Schwarz inequality becomes $|v|^2 \leq 2 \cdot 1 \cdot \tfrac12 |v|^2 = |v|^2$, equality — consistent with the curve being constant-speed.

**Is an instance: a great circle arc on $S^2$ of angular length $\theta$.** Parametrise at unit speed: $L = \theta$, $E = \theta^2/2$, $b - a = \theta$. Cauchy–Schwarz: $\theta^2 = 2 \theta \cdot \theta^2/2 = \theta^3$ — wait, that's not equality. Reparametrise: with $b - a = \theta$, $L = \theta$ and $2(b-a) E = 2\theta \cdot \theta^2/2 = \theta^3$. We need $L^2 \leq 2(b-a) E$, i.e. $\theta^2 \leq \theta^3$. This holds iff $\theta \geq 1$. The inequality goes the other way for $\theta < 1$? — no, recheck: actually, parametrising $\gamma : [0, b-a] \to S^2$ at unit speed, $L = b - a$ and $E = (b-a)/2$, so $L^2 = (b-a)^2$ and $2(b-a)E = (b-a)^2$ — equality holds. The earlier mistake conflated angular length and parameter range. The point: equality in Cauchy–Schwarz is constant speed, and the great circle parametrised at unit speed satisfies this trivially.

**Is an instance: a non-constant-speed parametrisation.** Take the equator of $S^2$ parametrised as $\gamma(t) = (\cos(t^2), \sin(t^2), 0)$ for $t \in [0, \sqrt{2\pi}]$. The length is $\int_0^{\sqrt{2\pi}} 2t\, dt = 2\pi$. The energy is $\tfrac12 \int_0^{\sqrt{2\pi}} (2t)^2 dt = 2 \int_0^{\sqrt{2\pi}} t^2 dt = \frac{2}{3}(2\pi)^{3/2}$. Cauchy–Schwarz: $L^2 = 4\pi^2$ and $2(b-a)E = 2\sqrt{2\pi} \cdot \frac{2}{3}(2\pi)^{3/2} = \frac{4}{3} \cdot 2\pi \cdot 2\pi = \frac{16\pi^2}{3} > 4\pi^2$. So the inequality is strict — consistent with $\gamma$ not being constant-speed (and indeed the speed is $|\dot\gamma| = 2t$).

**Is an instance: a constant curve.** $\gamma(t) \equiv p$ has $\dot\gamma = 0$, so $L(\gamma) = 0$ and $E(\gamma) = 0$. Cauchy–Schwarz: $0 \leq 0$, equality. The constant curve is the trivial geodesic, with zero velocity.

**Is NOT an instance: the length functional has multiple critical points at a single image.** Any reparametrisation of a geodesic image is also a critical point of $L$ — this is the degeneracy that makes $L$ awkward for variational analysis. The energy, by contrast, has a unique critical-point parametrisation among reparametrisations of a fixed image: the constant-speed one.

**Corollary (equality in Cauchy–Schwarz ⟺ constant speed).** *Calibration check:* Cauchy–Schwarz applied to the functions $1$ and $|\dot\gamma|$ on $[a, b]$ gives equality iff one is a multiple of the other, i.e. iff $|\dot\gamma|$ is constant.

**Corollary (geodesics minimise energy ⟺ they minimise length and are constant-speed).** Suppose $\gamma$ minimises $E$ over piecewise-smooth curves with fixed endpoints. Then for any other such curve $\tilde\gamma$, $L(\tilde\gamma)^2 \leq 2(b-a) E(\tilde\gamma)$, so a minimiser of $E$ is also (essentially) a minimiser of $L^2$, hence of $L$. *Calibration check:* the converse direction (minimisers of $L$ that are constant-speed minimise $E$) follows by reparametrising at constant speed without changing the length.

**Corollary (energy is convex in the parametrisation).** Among reparametrisations of a fixed unparametrised curve, the constant-speed parametrisation minimises $E$. *Calibration check:* this is the equality condition of Cauchy–Schwarz applied with $L$ fixed.

**Corollary (Euler–Lagrange of energy is the geodesic equation).** In coordinates with Lagrangian $L(\gamma, \dot\gamma) = \tfrac12 g_{ij}\dot\gamma^i \dot\gamma^j$, the Euler–Lagrange equations $\frac{d}{dt}\frac{\partial L}{\partial \dot\gamma^k} = \frac{\partial L}{\partial \gamma^k}$ produce $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$. This is the content of [[Thm - Hamilton's Principle Gives the Geodesic Equation]].

**Calibration check.** If you can verify (a) that the Cauchy–Schwarz inequality $L^2 \leq 2(b-a)E$ becomes equality exactly at constant-speed curves, (b) that minimising $E$ among fixed-endpoint curves automatically produces a constant-speed geodesic that also minimises $L$, and (c) that the length is degenerate under reparametrisation while the energy is not — then you have understood the definition.

---

# Unlocked by This

> [!tip] The First and Second Variation Formulas *(from Riemannian Geometry)*
> The first variation of energy gives the geodesic equation as Euler–Lagrange equations: $\nabla_{\dot\gamma}\dot\gamma = 0$ ⟺ $\gamma$ is a critical point of $E$ with fixed endpoints. The second variation of energy gives the **index form** $I(V, W) = \int g(V', W') - g(R(V, T)T, W)$ on normal variations — the Hessian of the energy at a geodesic. See [[Thm - First Variation of Arc Length]] and [[Thm - Second Variation of Arc Length]].

> [!tip] Hamilton's Principle and Geodesics *(from Geometric Mechanics)*
> The energy functional is exactly the action of a free unit-mass particle. So the variational characterisation of geodesics — they minimise (or extremise) energy — is the Hamiltonian/Lagrangian formulation of classical mechanics, specialised to the case of no potential. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] and [[Thm - Hamilton's Principle Gives the Geodesic Equation]].

> [!tip] **Harmonic Maps** *(from Geometric Analysis)*
> The same idea — minimise the squared norm of the derivative — generalises to maps $\varphi : (N, h) \to (M, g)$ via the **harmonic-map energy** $E(\varphi) = \tfrac12 \int_N |d\varphi|^2\, \mathrm{vol}_h$. Critical points are **harmonic maps**, generalising both harmonic functions ($M = \mathbb{R}$) and geodesics ($N = \mathbb{R}$). The Eells–Sampson theorem, the existence theory for harmonic maps to non-positively curved targets, and applications to minimal surfaces, Teichmüller theory, and Margulis superrigidity all flow from this generalisation.
