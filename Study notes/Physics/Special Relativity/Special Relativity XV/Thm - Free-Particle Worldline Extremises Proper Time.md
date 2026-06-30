---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Inertial Worldlines Maximise Proper Time"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, timelike $\eta_{\mu\nu}\dot x^\mu\dot x^\nu > 0$ (Gourgoulhon: mostly-plus, opposite sign). A free particle of rest mass $m$ has worldline $x^\mu = x^\mu(\lambda)$, parameter-velocity $\dot x^\mu = dx^\mu/d\lambda$, four-velocity $U = dX/d\tau$ with $u_\mu = \eta_{\mu\nu}U^\nu$ and $U\cdot U = 1$ (with $c$: $c^2$), and four-acceleration $a^\mu = dU^\mu/d\tau$. The action is $S = \int L\,d\lambda$ with free Lagrangian $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ (see [[Def - Relativistic Action of a Free Particle]]). Full registry on [[Special Relativity XV — The Principle of Least Action]].

---

# Statement

> **Theorem (the free worldline is a timelike geodesic of maximal proper time).** Let $\mathcal{P}$ be a free particle of constant rest mass $m$, with action $S = -mc\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$. The principle of stationary action $\delta S = 0$ (over variations fixing the endpoints) is equivalent to the Euler–Lagrange equations, which reduce to
> $$\frac{du_\mu}{d\lambda} = 0 \qquad\Longleftrightarrow\qquad \frac{dU^\mu}{d\tau} = a^\mu = 0.$$
> The four-velocity is therefore constant: the worldline is a **straight line** of Minkowski spacetime, a **timelike geodesic**. Because the action equals $-mc^2$ times the [[Def - Proper Time|proper time]] and the constant is negative, the stationary worldline is the one of *maximal* proper time among all timelike worldlines joining the two events, in agreement with [[Thm - Inertial Worldlines Maximise Proper Time|Special Relativity V]].

> **Companion fact (degeneracy of the equations).** The four Euler–Lagrange equations are not independent: the homogeneity identity $\dot x^\mu\big[\partial L/\partial x^\mu - \tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu)\big] = 0$ holds identically, so only three of the four are independent. This reflects the three physical degrees of freedom of a particle together with the one-parameter freedom in choosing $\lambda$.

---

# Motivation

The free particle is where the variational machine is first turned on, and the theorem is the test of whether the [[Def - Relativistic Action of a Free Particle|free action]] was chosen correctly. We *want* the free worldline to come out straight — that is the content of relativistic inertia, established by other means in the kinematics chapters — and we want it to come out as a *maximum* of proper time, matching the geometric result of [[Thm - Inertial Worldlines Maximise Proper Time|Special Relativity V]]. The theorem confirms both, and in doing so validates the action principle as the correct foundation for relativistic dynamics.

The deeper point is that this is the simplest instance of the most important equation in gravitational physics. The same variation, performed for a *curved* metric $g_{\mu\nu}(x)$ instead of the flat $\eta_{\mu\nu}$, yields the geodesic equation $\ddot x^\mu + \Gamma^\mu_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0$ — the equation of motion of a freely-falling body in general relativity. Here, with the flat metric, the Christoffel symbols vanish and the geodesic equation collapses to "the four-velocity is constant," a straight line. So the theorem is not just a check on the formalism; it is the flat-spacetime seed of the principle that gravity bends worldlines by bending the metric. Understanding why $\delta S = 0$ gives a straight line here is understanding the template for why it gives orbits around a star there.

There is also a subtlety the theorem forces into the open: the role of the parameter $\lambda$. Because the action is reparametrisation-invariant, the four Euler–Lagrange equations cannot be independent — if they were, they would over-determine the three physical degrees of freedom. The redundancy is exactly the freedom to choose $\lambda$, and the theorem makes this concrete by exhibiting the identity that renders one equation a consequence of the other three. This is the first appearance of the gauge structure that dominates the [[Thm - Hamiltonian Formulation (Relativistic Particle)|Hamiltonian treatment]].

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the worldline makes the free action stationary." Recognising when this applies means recognising the free particle in disguise.

The first disguised source is **"the particle is isolated / no forces act."** A free particle is one subject to no interaction, and any problem describing an isolated particle, a particle far from all fields, or a particle between collisions is a free-particle problem to which the theorem applies. The bridge is that "no force" means the Lagrangian is the pure free Lagrangian, with no interaction term. *Example problem:* a cosmic-ray proton coasting through empty space between scattering events follows a straight worldline, derivable as the stationary point of $-mc^2\int d\tau$.

The second disguised source is **"the metric is flat and the parameter is affine."** The straight-line conclusion is the flat-metric specialisation of the geodesic equation; conversely, any setting where one has a constant metric and seeks the extremal-length curve is governed by this theorem. The bridge is that the free action is the length functional of $\eta$. *Example problem:* the shortest-proper-time-deficit path in a [[Def - Minkowski Space and the Metric|Minkowski]] diagram, or the straight-worldline limit used to calibrate the curved-spacetime geodesic equation at a point where $\Gamma = 0$.

The third disguised source is **"a conserved four-velocity is wanted."** Whenever a problem requires $U$ to be constant — to define an inertial frame, to set up a boost, to integrate a worldline — the underlying justification is this theorem: free motion has $dU/d\tau = 0$. The bridge is that constancy of $U$ is the *content* of the geodesic equation in flat space. *Example problem:* establishing that an inertial observer's four-velocity is the same at every event of their worldline, the premise of the global rest space in [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

**Targets (Output Amplification)**

The conclusion is "the worldline is straight, $dU^\mu/d\tau = 0$."

Combine the conclusion with **the conservation of four-momentum**. Since $P = mU$ and $U$ is constant, $P$ is constant: the geodesic conclusion immediately gives four-momentum conservation for a free particle. The further result is that energy and three-momentum, relative to any inertial observer, are conserved — the dynamical content of [[Thm - Conservation of Four-Momentum|Special Relativity XIII]] for an isolated particle. The combination is useful because it derives a conservation law from an equation of motion in one step. *Example:* a free particle's energy is the same at every point of its trajectory.

Combine the conclusion with **the reversed triangle inequality**. The straight worldline being the stationary point, together with [[Thm - The Reversed Triangle Inequality|the reversed triangle inequality]], upgrades "stationary" to "maximal": among all timelike worldlines between two events, the straight one has the greatest proper time, strictly greater than any bent one. The further result is the resolution of the [[Special Relativity V — Worldlines, Proper Time and Four-Velocity|twin paradox]] — the inertial twin ages most. The combination is nonobvious because variational stationarity alone does not tell you whether you have a maximum or a minimum; the indefinite signature, encoded in the reversed inequality, is what makes it a maximum. *Example:* the travelling twin returns younger.

Combine the conclusion with **the curved-metric generalisation**. Replacing $\eta$ by $g_{\mu\nu}(x)$ in the variation, the same calculation yields $\ddot x^\mu + \Gamma^\mu_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0$ rather than $\ddot x^\mu = 0$. The further result is the **geodesic equation of general relativity**, the equation of motion of a freely-falling body. The combination is the single most important application: free relativistic motion and gravitational free fall are the same variational problem with different metrics. *Example:* planetary orbits as timelike geodesics of the Schwarzschild metric.

---

# Why Is It True

The mechanism is purely that the free Lagrangian depends on position only through the metric, and the metric is constant: **with no $x$-dependence in $L$, the Euler–Lagrange equation says the canonical momentum is conserved, and the canonical momentum is the four-velocity — so the four-velocity is constant, which means the worldline is straight.**

Unpack the two halves. The Lagrangian $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ contains the *constant* matrix $\eta_{\mu\nu}$ and no explicit dependence on the coordinates $x^\mu$. Therefore $\partial L/\partial x^\mu = 0$, and the Euler–Lagrange equation $\partial L/\partial x^\mu = \tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu)$ degenerates to $\tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$: the generalized momentum $\partial L/\partial\dot x^\mu$ is conserved. This is the same logic as a cyclic coordinate in ordinary mechanics — absence from the Lagrangian means the conjugate momentum is constant — except that here *all four* coordinates are absent.

Now compute the momentum. Differentiating the square root, $\partial L/\partial\dot x^\mu = -mc\,\eta_{\mu\nu}\dot x^\nu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$. The combination $\dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$ is precisely the unit-normalised [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$ (the parameter-velocity divided by its own Minkowski norm gives a vector of unit norm, independent of $\lambda$). So $\partial L/\partial\dot x^\mu = mc\,u_\mu$, and its conservation reads $du_\mu/d\lambda = 0$. Raising the index with the constant inverse metric, $dU^\mu/d\lambda = 0$, and since $U$ is constant the worldline integrates to a straight line $x^\mu(\lambda) = x^\mu_0 + U^\mu\,(\text{affine function of }\lambda)$.

The *maximum* (rather than minimum) character is a separate fact, and it comes from the indefinite signature. In a positive-definite metric the second variation of the length is positive and a geodesic is a local minimum of length. In the Lorentzian metric the spatial directions enter the proper time with a minus sign — wandering off in space *subtracts* from $\int d\tau$ — so any deviation from the straight worldline *decreases* the proper time, making the straight worldline a maximum. This is the content of [[Thm - The Reversed Triangle Inequality|the reversed triangle inequality]], and it is why "least action" coexists with "maximal proper time": the sign $-mc^2$ converts the maximum of $\int d\tau$ into the minimum of $S$.

Finally, the degeneracy. One of the four Euler–Lagrange equations is redundant because the action is reparametrisation-invariant: shifting $\lambda$ along the worldline is not a physical change, so the equations cannot determine the four functions $x^\mu(\lambda)$ uniquely — they fix the *worldline* but leave the parametrisation free. The identity $\dot x^\mu[\text{EL}]_\mu = 0$, a direct consequence of Euler's homogeneity identity, is the algebraic expression of this redundancy: contracting the four equations with $\dot x^\mu$ gives zero automatically, so they are linearly dependent.

---

# What Makes This Hard

The computation is short, and the conceptual hazards are two. First, the temptation to parametrise by proper time *before* varying: setting $\lambda = \tau$ collapses $L$ to the constant $-mc^2$ and the Euler–Lagrange equations to the vacuous $0 = 0$, losing all dynamics — the parameter must stay arbitrary until after the variation, and $U\cdot U = c^2$ imposed only afterwards. Second, the surprise that the stationary worldline is a *maximum* of proper time rather than a minimum; most people carry the Euclidean intuition that geodesics are shortest, and the sign flip from the indefinite metric — wandering in space decreases proper time — is the non-obvious point. The common error is to conclude from $\delta S = 0$ alone that one has a minimum of proper time, when in fact the indefinite signature makes it a maximum.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The free Lagrangian has no explicit $x$-dependence, so the Euler–Lagrange equation immediately gives conservation of the generalized momentum; compute that momentum and recognise it as the four-velocity, concluding $dU/d\lambda = 0$.

**Subgoal decomposition:**

1. **Note $\partial L/\partial x^\mu = 0$.** Observe that $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ contains only the constant metric and no explicit coordinates.
   - *Hint:* The metric $\eta_{\mu\nu}$ is constant; the coordinates $x^\mu$ appear nowhere.
   - *Why needed:* It makes the Euler–Lagrange equation reduce to conservation of the canonical momentum.

2. **Compute the generalized momentum.** Show $\partial L/\partial\dot x^\mu = mc\,u_\mu$.
   - *Hint:* Differentiate the square root; the ratio $\dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$ is the unit four-velocity $U^\mu$.
   - *Why needed:* It identifies the conserved quantity as the four-velocity.

3. **Conclude $du_\mu/d\lambda = 0$.** From steps 1–2, the Euler–Lagrange equation $\tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$ gives $d(mc\,u_\mu)/d\lambda = 0$, hence $dU^\mu/d\lambda = 0$.
   - *Hint:* Constant $m$; raise the index with the constant inverse metric.
   - *Why needed:* Constant four-velocity is a straight worldline — the conclusion.

4. **(Optional) Identify the maximum and the degeneracy.** Argue via [[Thm - The Reversed Triangle Inequality|the reversed triangle inequality]] that the straight worldline maximises proper time, and verify $\dot x^\mu[\text{EL}]_\mu \equiv 0$ from Euler's identity.
   - *Hint:* The indefinite signature makes spatial wandering decrease $\int d\tau$; contract the EL equations with $\dot x^\mu$.
   - *Why needed:* It pins down maximum-versus-minimum and exhibits the reparametrisation redundancy.

---

# Lemma Decomposition

> [!note]- Lemma 1: The free Lagrangian has no explicit coordinate dependence
> **Statement:** $\partial L/\partial x^\mu = 0$ for $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$.
>
> **Hint:** The metric is a constant matrix; the coordinates do not appear in $L$.
>
> **Why needed:** It reduces the Euler–Lagrange equation to the conservation of the generalized momentum, the heart of the proof.
>
> > [!note]- Full proof
> > $L$ depends on the position $x^\mu$ only through the metric components $\eta_{\mu\nu}$. In an inertial coordinate system these are the *constant* numbers $\mathrm{diag}(+1,-1,-1,-1)$, with no dependence on $x^\mu$. Hence $\partial L/\partial x^\mu = 0$. (In a non-inertial coordinate system the metric components would depend on position, and this lemma would fail — that is exactly the curved-space generalisation that produces the Christoffel terms.) $\blacksquare$

> [!note]- Lemma 2: The generalized momentum is $mc\,u_\mu$
> **Statement:** $\dfrac{\partial L}{\partial\dot x^\mu} = mc\,u_\mu$, where $u_\mu = \eta_{\mu\nu}U^\nu$ and $U^\mu = \dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$ is the unit-normalised four-velocity.
>
> **Hint:** Differentiate the square root and recognise the unit four-velocity.
>
> **Why needed:** It names the conserved quantity; combined with Lemma 1 it gives $d u_\mu/d\lambda = 0$.
>
> > [!note]- Full proof
> > Write $w := \eta_{\rho\sigma}\dot x^\rho\dot x^\sigma$, so $L = -mc\,w^{1/2}$. Then
> > $$\frac{\partial L}{\partial\dot x^\mu} = -mc\cdot\frac{1}{2}w^{-1/2}\cdot\frac{\partial w}{\partial\dot x^\mu} = -mc\cdot\frac{1}{2\sqrt{w}}\cdot 2\eta_{\mu\nu}\dot x^\nu = -mc\,\frac{\eta_{\mu\nu}\dot x^\nu}{\sqrt{w}}.$$
> > The minus sign is an artefact of having written the covariant component; define $U^\mu := \dot x^\mu/\sqrt{w}$, which satisfies $\eta_{\mu\nu}U^\mu U^\nu = w/w = 1$, the unit four-velocity (with $c$: normalise to $c^2$). Then $\partial L/\partial\dot x^\mu = mc\,\eta_{\mu\nu}U^\nu = mc\,u_\mu$, the covariant four-momentum component. (The apparent sign is absorbed into the definition of $u_\mu$; in mostly-minus, $u_\mu = \eta_{\mu\nu}U^\nu$ has $u_0 = U^0 > 0$ for a future-pointing worldline, consistent with positive energy. The cross-check $p_\mu = mc\,u_\mu$ matches [[Def - Four-Momentum and Rest Mass]].) $\blacksquare$

> [!note]- Lemma 3: The homogeneity identity makes the equations dependent
> **Statement:** $\dot x^\mu\Big[\dfrac{\partial L}{\partial x^\mu} - \dfrac{d}{d\lambda}\dfrac{\partial L}{\partial\dot x^\mu}\Big] = 0$ identically, so only three of the four Euler–Lagrange equations are independent.
>
> **Hint:** Use Euler's identity $\dot x^\mu\partial L/\partial\dot x^\mu = L$ and differentiate it.
>
> **Why needed:** It accounts for the reparametrisation freedom and the three physical degrees of freedom.
>
> > [!note]- Full proof
> > Euler's identity for the homogeneous-degree-one $L$ reads $\dot x^\mu\,\partial L/\partial\dot x^\mu = L$. Differentiate with respect to $\lambda$:
> > $$\frac{dL}{d\lambda} = \frac{d}{d\lambda}\Big(\dot x^\mu\frac{\partial L}{\partial\dot x^\mu}\Big) = \ddot x^\mu\frac{\partial L}{\partial\dot x^\mu} + \dot x^\mu\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}.$$
> > Also, by the chain rule, $\frac{dL}{d\lambda} = \frac{\partial L}{\partial x^\mu}\dot x^\mu + \frac{\partial L}{\partial\dot x^\mu}\ddot x^\mu$. Subtracting the two expressions for $dL/d\lambda$, the $\ddot x^\mu\,\partial L/\partial\dot x^\mu$ terms cancel, leaving
> > $$0 = \frac{\partial L}{\partial x^\mu}\dot x^\mu - \dot x^\mu\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu} = \dot x^\mu\Big[\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big].$$
> > Thus the contraction of the four Euler–Lagrange expressions with $\dot x^\mu$ vanishes identically: they are linearly dependent, and only three are independent. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** The action $S = -mc\int_{\lambda_1}^{\lambda_2}\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ is well-defined on timelike worldlines, where the radicand is positive, and is reparametrisation-invariant (the integrand is homogeneous of degree one in $\dot x^\mu$). We vary with the parameter $\lambda$ held arbitrary throughout and impose $U\cdot U = c^2$ only at the end.
>
> **Step 1.** The first variation, with $\delta x^\mu$ vanishing at $\lambda_1, \lambda_2$, gives the Euler–Lagrange equations
> $$\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu} = 0.$$
>
> **Step 2.** By Lemma 1, $\partial L/\partial x^\mu = 0$ (the metric is constant, the coordinates absent). The equation reduces to $\dfrac{d}{d\lambda}\dfrac{\partial L}{\partial\dot x^\mu} = 0$.
>
> **Step 3.** By Lemma 2, $\partial L/\partial\dot x^\mu = mc\,u_\mu$ with $u_\mu = \eta_{\mu\nu}U^\nu$ and $U^\mu = \dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$. Hence
> $$\frac{d}{d\lambda}(mc\,u_\mu) = 0 \quad\Longrightarrow\quad \frac{du_\mu}{d\lambda} = 0.$$
> Raising the index with the constant inverse metric $\eta^{\mu\nu}$ gives $dU^\mu/d\lambda = 0$: the four-velocity is constant.
>
> **Step 4.** A constant four-velocity integrates to $x^\mu(\lambda) = x^\mu_0 + U^\mu\,\sigma(\lambda)$ for some scalar function $\sigma$, a straight line of Minkowski spacetime — a timelike geodesic. Choosing the proper time $\lambda = \tau$ (legitimate now that the equations are derived) gives $\dot x^\mu = U^\mu$ and $a^\mu = dU^\mu/d\tau = 0$.
>
> **Step 5 — maximum, not minimum.** Among timelike worldlines from $A_1$ to $A_2$, the straight one has the greatest proper time: by [[Thm - The Reversed Triangle Inequality|the reversed triangle inequality]], any bent worldline (a concatenation of timelike segments) has strictly smaller total proper time. Since $S = -mc^2\int d\tau$ with the constant negative, the maximum of $\int d\tau$ is the minimum of $S$, so the stationary worldline is a minimum of the action and a maximum of proper time, consistent with [[Thm - Inertial Worldlines Maximise Proper Time]].
>
> **Step 6 — degeneracy.** By Lemma 3, $\dot x^\mu[\text{EL}]_\mu \equiv 0$, so the four Euler–Lagrange equations are dependent and only three are independent — the three physical degrees of freedom, the fourth equation being the reparametrisation redundancy. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Geodesics of a Riemannian manifold by the same variation.** The identical first-variation calculation, applied to the length functional $\int\sqrt{g_{ij}\dot x^i\dot x^j}\,d\lambda$ of a positive-definite metric, yields the Riemannian geodesic equation; the only changes are the metric's positive-definiteness (making geodesics *shortest*) and its position-dependence (producing Christoffel symbols). The flat free worldline is the constant-metric, indefinite-signature instance. The application is illuminating because it shows the relativistic free particle and the geodesics of [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] are one calculation; see [[Ex - Deriving the geodesic equation from the variational principle]].

**The brachistochrone and Fermat's principle as variational worldlines.** Fermat's principle — light takes the path of stationary optical length $\int n\,ds$ — is the same kind of variational statement, with the "metric" being the refractive index times the Euclidean line element. Solving it reproduces Snell's law and the bending of light in a medium. The application is out-of-distribution because it is geometric optics rather than mechanics, yet the Euler–Lagrange structure is identical, and the null-geodesic limit of the relativistic action connects the two.

**Orbits in the Schwarzschild metric.** Replacing $\eta$ by the Schwarzschild metric and varying gives the timelike geodesics that are planetary orbits; the conserved energy and angular momentum come from the metric's time-translation and rotation symmetries via Noether's theorem (Killing vectors). The application is the direct gravitational descendant of this theorem: free fall is free relativistic motion in a curved metric; see [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Thm - Inertial Worldlines Maximise Proper Time|Inertial worldlines maximise proper time]]** — that theorem (proved in [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]] by the reversed triangle inequality, a *global* comparison of worldlines) and this one (a *local* variational stationarity) are two derivations of the same fact: the straight timelike worldline extremises proper time. The variational version here additionally produces the *equation* $dU/d\tau = 0$ and generalises to curved metrics; the global version certifies that the extremum is a maximum. Together they give the complete characterisation of free worldlines.

- **[[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]]** — this theorem supplies the premise Noether's theorem needs: the worldline satisfies the Euler–Lagrange equations. The conservation laws that Noether extracts (four-momentum, angular momentum) are therefore statements *about geodesics*. In particular, $P = mU$ is constant precisely because $U$ is constant, which this theorem establishes; the two results are the equation of motion and its conserved quantities, the two halves of free-particle dynamics.

- **The geodesic equation of general relativity** — replacing the flat metric $\eta_{\mu\nu}$ by a position-dependent $g_{\mu\nu}(x)$ and repeating the variation gives $\ddot x^\mu + \Gamma^\mu_{\;\nu\rho}\dot x^\nu\dot x^\rho = 0$, with $\Gamma^\mu_{\;\nu\rho} = \tfrac12 g^{\mu\sigma}(\partial_\nu g_{\sigma\rho} + \partial_\rho g_{\sigma\nu} - \partial_\sigma g_{\nu\rho})$ arising from the $\partial_\mu g$ terms that were absent in the flat case (Lemma 1 fails for a curved metric). The flat free worldline is the $\Gamma = 0$ special case. This is the variational route to the equation of motion of a freely-falling body, and it makes "gravity is the curvature of the metric" a precise statement: the worldline bends because $g_{\mu\nu}$ varies. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Unlocked by This

> [!tip] Free Fall as Geodesic Motion *(from General Relativity)*
> The **equivalence principle** asserts that a freely-falling body feels no force, and this theorem makes that precise: in general relativity a freely-falling body follows a **timelike geodesic** of the spacetime metric $g_{\mu\nu}$, the curve that extremises proper time, obtained by exactly the variation performed here but with $\eta$ replaced by $g$. Gravity is not a force in the worldline's frame; it is the curvature of the metric, which makes the extremal-proper-time worldlines bend. The straight worldline of the free relativistic particle is the local, flat-spacetime model that every freely-falling worldline resembles in a small enough neighbourhood. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
