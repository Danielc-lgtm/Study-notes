---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature, so a four-velocity is a future-directed timelike unit vector, $U \cdot U = 1$, with positive time component $u^0 > 0$ in any frame whose time axis is future-directed. The observer $\mathcal{O}$ has four-velocity $U_0$ and proper time $\tau$; the particle $\mathcal{P}$ has four-velocity $U$ and proper time $\tau'$. The [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] of $\mathcal{P}$ relative to $\mathcal{O}$ is $\Gamma = U \cdot U_0$, defined by $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$. In the observer's frame $(e_\alpha)$ with $e_0 = U_0$, the particle's four-velocity has components $u^\alpha = (u^0, u^1, u^2, u^3)$. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

---

# Statement

> **Theorem (time dilation, general observer).** Let $\mathcal{O}$ be an observer with four-velocity $U_0$ and let $\mathcal{P}$ be a particle with four-velocity $U$, whose worldline crosses that of $\mathcal{O}$ or for which $\mathcal{O}$ is inertial. Then the Lorentz factor satisfies
> $$\Gamma = U \cdot U_0 \;\geq\; 1,$$
> with equality if and only if $U = U_0$. Equivalently, in terms of proper-time increments,
> $$\mathrm{d}\tau \;\geq\; \mathrm{d}\tau',$$
> so the proper time $\mathcal{O}$ ascribes to a segment of $\mathcal{P}$'s worldline is at least the proper time $\mathcal{P}$ records on its own clock: a moving clock runs slow.

The inequality $U \cdot U_0 \geq 1$ for two future-directed timelike unit vectors is the **reversed Cauchy–Schwarz inequality** of Minkowski geometry; the equality case $U = U_0$ is the statement that the only way a particle's clock keeps pace with the observer's is for it to be at rest relative to the observer.

---

# Motivation

Time dilation was discovered in [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction|Special Relativity II]] by comparing two inertial frames with a [[Def - The Lorentz Transformation|Lorentz boost]]: a clock at rest in one frame ticks at intervals $T'$, and the other frame measures longer intervals $T = \gamma T'$. That treatment has a built-in limitation — it compares *coordinate* times in two *global* inertial frames, and it tacitly assumes the two events being timed lie on the moving clock's own worldline. This theorem removes both limitations. The events can lie anywhere; the observer can be accelerated; and the comparison is between the observer's proper time and the particle's proper time, made meaningful by the [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré simultaneity]] of the previous chapter rather than by a global coordinate frame.

The role of the theorem is to certify that the Lorentz factor, now defined as a scalar product $\Gamma = U \cdot U_0$, really deserves its name: it is always at least one, so the proper time the observer measures always exceeds the particle's own, never the reverse. Without this, "$\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$" would be just a definition with no physical bite; the inequality $\Gamma \geq 1$ is what makes it *time dilation* — a definite, signed effect. It is the general-observer foundation on which the muon experiments, the relativistic energy $E = \Gamma m$, and the twin paradox all rest.

The deeper significance is that the proof is purely geometric and reveals time dilation as an inequality about the indefinite metric. There is no boost, no coordinate transformation, no train: just the fact that a future timelike unit vector, decomposed against another, has a time component at least one. This is the reversed Cauchy–Schwarz inequality, the Minkowski cousin of the Euclidean $|x \cdot y| \leq \|x\|\|y\|$, with the inequality *reversed* by the signature — and it is the same fact that, integrated along worldlines, gives the [[Thm - Inertial Worldlines Maximise Proper Time|reversed triangle inequality]] and the twin paradox.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\Gamma$ is the Lorentz factor of a particle relative to an observer, with crossing worldlines or an inertial observer". The point is to recognise the many ways this configuration appears.

The first disguised source is **"two timelike worldlines pass through (or near) a common event"**. Any two massive particles, observers, clocks, or rockets whose paths meet supply two four-velocities and hence a Lorentz factor $\Gamma = U \cdot U_0$ to which the theorem applies. The bridge is that "meeting worldlines" is exactly the condition $\overrightarrow{OM} = 0$ under which $\Gamma = U \cdot U_0$ holds without correction terms. *Example problem:* two spaceships pass each other; show each pilot measures the other's clock to run slow, by the same factor.

The second disguised source is **"a particle's four-velocity is given in some inertial frame"**. The time component $u^0$ of any future timelike unit vector, in any frame, is the Lorentz factor relative to the observer at rest in that frame — and the unit-norm constraint forces $u^0 \geq 1$. The bridge is $\Gamma = U \cdot U_0 = u^0$ in the observer's frame. The nonobviousness is that you need no second worldline drawn explicitly: the frame itself *is* an inertial observer. *Example problem:* given $u^\alpha = (\Gamma, \Gamma\mathbf V)$, read off that the lab measures the particle's clock dilated by $u^0$.

The third disguised source is **"a decay, a period, or any internal clock process is specified in a particle's rest frame"**. A decay time, an oscillation period, the swing of a pendulum — any process with a definite duration in the particle's own frame is a proper-time interval $\mathrm{d}\tau'$, and the observer measures $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$. The bridge is that "any periodic or finite-duration physical process is a clock", so the theorem governs its observed rate. *Example problem:* a muon's proper lifetime is $\tau_0$; the terrestrial observer measures a lifetime $\Gamma\tau_0$, which is why muons reach the ground ([[Ex - The cosmic-ray muon reaches the ground]]).

**Targets (Output Amplification)**

The conclusion is "$\Gamma \geq 1$, i.e. $\mathrm{d}\tau \geq \mathrm{d}\tau'$".

Combine the conclusion with **a finite worldline integrated**. Integrating $\mathrm{d}\tau \geq \mathrm{d}\tau'$ along a particle's worldline between two events shared with the observer gives the integrated time dilation, and comparing a straight observer worldline with a bent particle worldline between the same endpoints gives the [[Thm - Inertial Worldlines Maximise Proper Time|reversed triangle inequality]]. The further result is the twin paradox: the straight (inertial) worldline accumulates the most proper time. The combination is useful because it lifts an infinitesimal inequality to a statement about total ageing along worldlines.

Combine the conclusion with **a rest mass $m$**. Multiplying the Lorentz factor by $m$ gives the relativistic energy $E = \Gamma m$, and $\Gamma \geq 1$ becomes $E \geq m$: the energy of a particle is at least its rest energy, with the excess $E - m = (\Gamma - 1)m$ the kinetic energy. The further result is that rest energy is a floor on total energy, the foundation of [[Def - Four-Momentum and Rest Mass|relativistic energy–momentum]]. The combination is nonobvious because a kinematic inequality ($\Gamma \geq 1$) becomes a dynamical one (energy bounded below by rest energy).

Combine the conclusion with **the symmetry $\Gamma = U \cdot U_0 = U_0 \cdot U$**. Since the scalar product is symmetric, *each* of two observers measures the *other's* clock to run slow, by the same factor. The further result is that time dilation is reciprocal and therefore *not* a contradiction: the apparent paradox ("how can each see the other slow?") dissolves because the two are comparing different pairs of events. The combination is the resolution of the most common confusion about time dilation, and it follows from nothing but the symmetry of the inner product.

---

# Why Is It True

The theorem is the reversed Cauchy–Schwarz inequality, and the reason it holds is the same reason its Euclidean cousin holds, read through the sign flip of the metric.

In Euclidean space, two *unit* vectors satisfy $x \cdot y = \cos\theta \leq 1$, with equality when they are equal — the dot product of unit vectors is bounded *above* by one, because $\cos$ is bounded above by one, and the bound is saturated when the angle vanishes. The "angle" measures how far apart the directions are, and the dot product shrinks as they separate.

In Minkowski space the same picture holds with one decisive change: the unit timelike vectors live on a *hyperboloid*, not a sphere, and the "angle" between them is the **rapidity** $\varphi$, a hyperbolic angle. The scalar product of two future timelike unit vectors is $U \cdot U_0 = \cosh\varphi$, and $\cosh$ is bounded *below* by one, with equality when $\varphi = 0$. So the dot product is bounded below, not above — it *grows* as the vectors separate (as the relative speed increases), starting from one when they coincide. That is the entire content of the theorem: **time dilation is the statement that $\cosh \geq 1$, exactly as the Euclidean angle inequality is the statement that $\cos \leq 1$ — the same fact with the hyperbola's unbounded growth replacing the circle's bounded oscillation.**

There is an even more elementary way to see it, the one the formal proof uses. In the observer's own frame, $\Gamma = U \cdot U_0$ is just the time component $u^0$ of the particle's four-velocity. The unit-norm constraint $U \cdot U = (u^0)^2 - \sum_i (u^i)^2 = 1$ rearranges to $u^0 = \sqrt{1 + \sum_i (u^i)^2}$, and the right-hand side is manifestly at least one, equal to one only when all the spatial components vanish — that is, when the particle is at rest in the observer's frame, $U = U_0$. The time component of a unit timelike vector cannot be less than one, because it has to "pay" for the spacelike components under the constraint that the *difference* of squares is one. The spacelike part borrows from the timelike part, forcing $u^0$ up. Time dilation is this borrowing made quantitative.

The physical reading, due ultimately to Tong's slogan, is that *time itself runs slow in a moving frame*. A clock is any periodic process, and an elementary particle — structureless, with no internal machinery — runs slow just as a mechanical clock does, because it is not the machinery that slows but the proper time that elapses. The geometry is indifferent to what kind of clock it is; it only knows the worldline's length, and a worldline that moves through space banks less proper time than one that sits still, by exactly the factor $\cosh\varphi = \Gamma$.

---

# What Makes This Hard

The algebra is trivial — $u^0 = \sqrt{1 + \sum (u^i)^2} \geq 1$ is a one-line manipulation of the unit-norm constraint — so the difficulty is entirely conceptual, and it lies in two places. First, believing that the effect is reciprocal without being contradictory: each observer measures the other's clock to run slow, and the resolution (they compare different pairs of events) is where most people stumble, mistaking the symmetry of $\Gamma$ for a paradox. Second, identifying *which* proper time is the dilated one: $\mathrm{d}\tau$ (the observer's) is the *larger*, $\mathrm{d}\tau'$ (the particle's, the one on the moving clock) is the *smaller*, and getting the inequality backwards — concluding the moving clock runs fast — is the classic error, usually from confusing which frame holds the clock present at both events.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Work in the observer's own frame, where the Lorentz factor is the time component of the particle's four-velocity, and read the bound straight off the unit-norm constraint. The whole proof is the observation that the time component of a future timelike unit vector is $\sqrt{1 + (\text{spatial part})^2} \geq 1$.

**Subgoal decomposition:**

1. **Reduce the Lorentz factor to a time component.** Show that in the frame with $e_0 = U_0$, $\Gamma = U \cdot U_0 = u^0$.
   - *Hint:* $U_0 = e_0$ has components $(1,0,0,0)$; the scalar product $U \cdot U_0 = \eta_{\mu\nu}u^\mu \delta^\nu_0 = u^0$.
   - *Why needed:* It turns the abstract scalar product into a single component, on which the unit-norm constraint acts directly.

2. **Apply the unit-norm constraint.** From $U \cdot U = 1$, solve for $u^0$.
   - *Hint:* $U \cdot U = (u^0)^2 - \sum_i (u^i)^2 = 1$, and $u^0 > 0$ (future-directed), so $u^0 = \sqrt{1 + \sum_i (u^i)^2}$.
   - *Why needed:* It exhibits $u^0$ as a square root of one plus a sum of squares, manifestly $\geq 1$.

3. **Read off the bound and equality case.** Conclude $\Gamma = u^0 \geq 1$, with equality iff all $u^i = 0$, i.e. $U = U_0$.
   - *Hint:* $\sqrt{1 + s} = 1 \iff s = 0$.
   - *Why needed:* It is the statement of the theorem, including the equality condition.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Lorentz factor is the time component in the observer's frame
> **Statement:** In an orthonormal frame $(e_\alpha)$ with $e_0 = U_0$, the Lorentz factor of $\mathcal{P}$ relative to $\mathcal{O}$ is $\Gamma = U \cdot U_0 = u^0$, the time component of the particle's four-velocity.
>
> **Hint:** Write $U_0 = e_0$ in components and contract with $U$ using $\eta = \mathrm{diag}(1,-1,-1,-1)$.
>
> **Why needed:** It converts the scalar-product definition of $\Gamma$ into a single component, the object the unit-norm constraint controls.
>
> > [!note]- Full proof
> > In the observer's frame $U_0 = e_0$ has components $\delta^\alpha_0 = (1,0,0,0)$. The Minkowski scalar product is $U \cdot U_0 = \eta_{\mu\nu}u^\mu (U_0)^\nu = \eta_{\mu 0}u^\mu = \eta_{00}u^0 = u^0$, since $\eta_{00} = 1$ and $\eta_{i0} = 0$. Hence $\Gamma = U \cdot U_0 = u^0$. $\blacksquare$

> [!note]- Lemma 2: The time component of a future timelike unit vector is at least one
> **Statement:** If $U$ is a future-directed timelike unit vector, $U \cdot U = 1$ and $u^0 > 0$, then $u^0 = \sqrt{1 + \sum_{i=1}^3 (u^i)^2} \geq 1$, with equality iff $u^1 = u^2 = u^3 = 0$.
>
> **Hint:** Expand the unit-norm constraint in components and solve for $u^0$, choosing the positive root.
>
> **Why needed:** It is the bound itself; combined with Lemma 1 it gives $\Gamma \geq 1$.
>
> > [!note]- Full proof
> > The unit-norm constraint reads $U \cdot U = \eta_{\mu\nu}u^\mu u^\nu = (u^0)^2 - (u^1)^2 - (u^2)^2 - (u^3)^2 = 1$, so $(u^0)^2 = 1 + \sum_{i=1}^3 (u^i)^2$. Since $U$ is future-directed, $u^0 > 0$, and taking the positive square root gives $u^0 = \sqrt{1 + \sum_i (u^i)^2}$. The radicand is $\geq 1$ with equality iff $\sum_i (u^i)^2 = 0$, i.e. iff each $u^i = 0$; then $U = u^0 e_0 = e_0 = U_0$. Hence $u^0 \geq 1$ with equality iff $U = U_0$. $\blacksquare$

> [!note]- Lemma 3: Reformulation as proper times
> **Statement:** $\Gamma \geq 1$ is equivalent to $\mathrm{d}\tau \geq \mathrm{d}\tau'$, the observer's proper-time increment being at least the particle's.
>
> **Hint:** Use the defining relation $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$ with $\mathrm{d}\tau' > 0$.
>
> **Why needed:** It expresses the bound in the physical language of clock readings, the form in which time dilation is stated and measured.
>
> > [!note]- Full proof
> > By definition of the [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]], $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$, with both proper-time increments positive (time advances along any future-directed worldline). Multiplying the inequality $\Gamma \geq 1$ by $\mathrm{d}\tau' > 0$ gives $\Gamma\,\mathrm{d}\tau' \geq \mathrm{d}\tau'$, i.e. $\mathrm{d}\tau \geq \mathrm{d}\tau'$. Equality holds iff $\Gamma = 1$, i.e. iff $U = U_0$ (the particle shares the observer's four-velocity). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Choose the observer's orthonormal frame $(e_\alpha)$ with $e_0 = U_0$ and the $e_i$ spanning the rest space, so $\eta_{\alpha\beta} = \mathrm{diag}(1,-1,-1,-1)$.
>
> By Lemma 1, the Lorentz factor is the time component of the particle's four-velocity in this frame:
> $$\Gamma = U \cdot U_0 = u^0.$$
>
> By Lemma 2, the unit-norm constraint $U \cdot U = 1$ together with the future-directed condition $u^0 > 0$ gives
> $$u^0 = \sqrt{1 + \sum_{i=1}^3 (u^i)^2} \;\geq\; 1,$$
> with equality if and only if all spatial components vanish, i.e. $U = U_0$. Hence
> $$\Gamma = u^0 \geq 1,\qquad \Gamma = 1 \iff U = U_0.$$
>
> By Lemma 3, this is equivalent, via $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$ with $\mathrm{d}\tau' > 0$, to
> $$\mathrm{d}\tau \geq \mathrm{d}\tau',$$
> the observer's proper-time increment being at least the particle's, with equality iff the particle is at rest relative to the observer. This is the statement of the theorem.
>
> (Coordinate-free restatement of the inequality: for two future-directed timelike unit vectors $U, U_0$, write $U = \Gamma(U_0 + V)$ with $V \cdot U_0 = 0$, $V$ spacelike. Then $U \cdot U = \Gamma^2(U_0 \cdot U_0 + 2 V\cdot U_0 + V \cdot V) = \Gamma^2(1 + V\cdot V) = \Gamma^2(1 - |\mathbf V|^2) = 1$, so $\Gamma = (1 - |\mathbf V|^2)^{-1/2} \geq 1$, with equality iff $|\mathbf V| = 0$, recovering the reversed Cauchy–Schwarz inequality $U \cdot U_0 = \Gamma \geq 1$.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Particle physics — decay lengths of beam particles.** An unstable particle of proper lifetime $\tau_0$ produced at Lorentz factor $\Gamma$ travels a mean distance $\Gamma V\tau_0$ before decaying, $\Gamma$ times the naive estimate. Computing the beamline length over which a given fraction of a pion or kaon beam survives is a direct application: the survival probability is $\exp(-L/\Gamma V\tau_0)$. The application is everyday in accelerator design and is the working form of $\mathrm{d}\tau = \Gamma\mathrm{d}\tau'$. See [[Ex - The cosmic-ray muon reaches the ground]].

**Astrophysics — the apparent lifetime of cosmic-ray nuclei.** Ultra-high-energy cosmic rays have enormous Lorentz factors ($\Gamma \sim 10^{11}$ for the highest), so even short-lived nuclear states survive intergalactic distances in the lab frame while decaying promptly in their own. Estimating the propagation distance of an unstable cosmic-ray species is the same calculation at extreme $\Gamma$, where the reversed Cauchy–Schwarz bound is saturated to one part in $10^{22}$.

**Atomic physics — the transverse Doppler effect as time dilation.** A moving atom's emission frequency is shifted partly by the ordinary Doppler effect and partly by time dilation; for motion transverse to the line of sight the *only* shift is the time-dilation factor $\Gamma$, so $\nu_{\mathrm{obs}} = \nu_0/\Gamma$. Measuring this transverse shift (the Ives–Stilwell experiment) is a direct test of $\mathrm{d}\tau = \Gamma\mathrm{d}\tau'$ using an atomic clock, connecting this theorem to the Doppler material of [[Special Relativity VIII — Kinematics II, Change of Observer]].

---

# Bridges

- **[[Thm - Time Dilation]]** — the Special Relativity II version, derived by a Lorentz boost between two inertial frames, $T = \gamma T'$. This theorem generalises it to an arbitrary (possibly accelerated) observer and recasts the factor as a scalar product $\Gamma = U \cdot U_0$; the boost-based result is the special case where both worldlines are inertial and the two events lie on the moving clock's worldline. The conceptual content — a moving clock runs slow — is identical; what changes is that no global frame is needed, only the two four-velocities and the local rest space.

- **[[Thm - Inertial Worldlines Maximise Proper Time]]** — the integrated form. Where this theorem gives the infinitesimal inequality $\mathrm{d}\tau \geq \mathrm{d}\tau'$, integrating it along worldlines between two shared events and comparing a straight observer path with a bent particle path yields the reversed triangle inequality: the inertial (straight) worldline has the *longest* proper time. The twin paradox is the integrated time dilation of this theorem, and the equality case $U = U_0$ here is the equality case (collinear segments) there.

- **Reversed Cauchy–Schwarz inequality** — the abstract statement. For two future-directed timelike unit vectors in a Lorentzian space, $U \cdot U_0 \geq 1$. This theorem is that inequality with a physical name; the Euclidean Cauchy–Schwarz $|x \cdot y| \leq \|x\|\|y\|$ becomes, for the indefinite metric restricted to the future timelike cone, the *reversed* bound, with $\cosh$ replacing $\cos$ and the lower bound replacing the upper. The same sign flip reverses the triangle inequality and produces the twin paradox.

- **[[Def - Four-Momentum and Rest Mass]]** — the dynamical amplification. Multiplying $\Gamma \geq 1$ by the rest mass $m$ gives $E = \Gamma m \geq m$: the relativistic energy is bounded below by the rest energy, and the excess is the kinetic energy. The kinematic floor on the Lorentz factor becomes the energetic floor of [[Special Relativity XIII — Energy and Momentum]].

---

# Unlocked by This

> [!tip] Relativistic Energy and the Rest-Energy Floor *(from Relativistic Dynamics)*
> Time dilation's inequality $\Gamma \geq 1$, multiplied by the rest mass, says the relativistic energy $E = \Gamma m$ is at least the rest energy $m$ (with $c$: $mc^2$), with the difference $(\Gamma - 1)m$ being the kinetic energy. This is the kinematic origin of **mass–energy equivalence**: a body at rest has energy $mc^2$, and to set it in motion costs the additional $(\Gamma - 1)mc^2$. The full development is **Special Relativity XIII**.

> [!tip] Gravitational Time Dilation and the Geodesic Principle *(from General Relativity)*
> Integrating $\mathrm{d}\tau \geq \mathrm{d}\tau'$ and promoting the flat metric to a curved $g_{\mu\nu}(x)$ gives **gravitational time dilation**: a clock deeper in a gravitational potential ticks slower, because the metric component converting coordinate time to proper time is smaller there. A freely-falling body follows the worldline of *longest* proper time — a **timelike geodesic** — the curved-spacetime version of the reversed triangle inequality. The Global Positioning System corrects for both the special-relativistic dilation of this theorem and the gravitational one of [[General Relativity I — Einstein's Equations and Schwarzschild]].
