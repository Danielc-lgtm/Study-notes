---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Velocity Relative to an Observer"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a four-velocity is a future timelike unit vector ($U \cdot U = 1$) and the [[Def - Velocity Relative to an Observer|relative velocity]] $V$ is spacelike ($V \cdot V < 0$). The observer $\mathcal{O}$ has four-velocity $U_0$; the particle $\mathcal{P}$ has four-velocity $U = \Gamma(U_0 + V)$ with $V \cdot U_0 = 0$ and [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] $\Gamma = U \cdot U_0$. The speed is $|\mathbf V| = \|V\|_g = \sqrt{-V\cdot V}$, the Euclidean norm of $V$ in the rest space. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

---

# Statement

> **Theorem (maximum relative velocity).** Let $\mathcal{O}$ be an observer with four-velocity $U_0$ and $\mathcal{P}$ a massive particle with four-velocity $U$, whose worldline crosses that of $\mathcal{O}$ or for which $\mathcal{O}$ is inertial. Then the speed of $\mathcal{P}$ relative to $\mathcal{O}$ is strictly less than the speed of light:
> $$\|\mathbf V\|_g \;<\; c\qquad(\text{with }c=1:\ |\mathbf V| < 1).$$
> The constant $c$ is a strict upper bound for the relative velocity of any massive particle measured locally by any observer, and for inertial observers the bound extends to distant measurements. Equality $|\mathbf V| = c$ is approached only in the limit of a null (photonic) worldline.

A hypothetical particle on a *spacelike* worldline (a **tachyon**) would have $\|\mathbf V\|_g > c$ relative to any ordinary timelike observer; the speed of light is then the *minimum* speed of a tachyon, not a ceiling. The theorem is the kinematic statement that timelike worldlines stay below $c$ and null worldlines sit exactly at $c$.

---

# Motivation

In [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction|Special Relativity II]] the impossibility of reaching the speed of light appeared as a feature of the velocity-addition law: combining two sub-light speeds always gives a sub-light speed, with $c$ a fixed point and an unreachable ceiling. That is a true statement, but it is a statement about *composing* velocities, and it leaves open whether some other process — a sufficiently long acceleration, a clever frame — might break the barrier. This theorem settles the matter at the root. It is not about composition; it is about a single particle and a single observer, and it says that the very structure of a four-velocity — its being a *unit timelike* vector — forbids a relative speed of $c$ or more.

The role of the theorem is to make the speed limit a property of geometry rather than of dynamics. It costs no infinite energy argument, no relativistic-mass increase, no force law — it is purely kinematic, a consequence of the unit-norm constraint $U \cdot U = 1$ in an indefinite metric. The reader should expect such a result the moment they see that the four-velocity must be timelike: a timelike vector, by definition, has its time component dominating its space components, and the relative speed is the ratio of the space part to the time part, which is therefore bounded by one.

The deeper significance is that the bound is *exactly* the boundary between timelike and null. A massive particle has a timelike worldline, so $|\mathbf V| < c$ strictly; a photon has a null worldline, so $|\mathbf V| = c$ exactly; a tachyon would have a spacelike worldline, so $|\mathbf V| > c$. The three classes of [[Def - Classification of Four-Vectors|causal classification]] map precisely onto the three velocity regimes, and the speed of light is the dividing line. This is why the speed limit is unbreakable by any massive particle: to reach $c$ it would have to become null, i.e. massless, and a massive particle cannot.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{P}$ is a massive particle, i.e. its four-velocity is a future timelike unit vector". The point is to recognise this configuration in disguise.

The first disguised source is **"a particle has nonzero rest mass"**. Any massive particle — electron, proton, spaceship, planet — has a timelike worldline parametrised by proper time, hence a unit four-velocity, hence a relative speed below $c$. The bridge is that "rest mass nonzero" is equivalent to "worldline timelike, four-velocity exists and is unit". *Example problem:* show no rocket, however powerful, can carry a crew to $c$ — its worldline is timelike at every instant, so its speed relative to any observer stays below $c$.

The second disguised source is **"a four-velocity is given with $u^0 < \infty$"**. Whenever the four-velocity components are finite in some frame, the speed is $|\mathbf V| = \sqrt{\sum (u^i)^2}/u^0 < 1$, because the unit-norm constraint makes the numerator strictly less than the denominator. The bridge is the constraint $(u^0)^2 - \sum (u^i)^2 = 1$, forcing $\sum (u^i)^2 = (u^0)^2 - 1 < (u^0)^2$. *Example problem:* given $u^\alpha$, confirm the speed is below $c$ directly from the components.

The third disguised source is **"two timelike worldlines are compared"**. The relative speed of any two massive particles or observers is below $c$, by the theorem applied to either as observer of the other. The bridge is that both four-velocities are timelike unit vectors, and the relative velocity is the rest-space part of one decomposed against the other. *Example problem:* two beams of particles cross at a small angle; the relative speed of one beam's particles in the other beam's rest frame is below $c$, even though the lab-frame closing speed of the two beams can approach (but not exceed) $2c$.

**Targets (Output Amplification)**

The conclusion is "$|\mathbf V| < c$ for massive particles".

Combine the conclusion with **the relative velocity of light, $|\mathbf V| = c$**. The strict inequality for timelike worldlines and the equality for null worldlines together say the speed of light is the exact supremum of attainable massive speeds, approached but not reached as $\Gamma \to \infty$. The further result is that the photon is the limiting case of a massive particle as its rest mass tends to zero at fixed energy — the massless limit. The combination is useful because it places massive and massless particles on a single velocity scale with $c$ as the boundary, foundational for [[Def - The Four-Momentum of a Photon|massless four-momentum]].

Combine the conclusion with **the causal structure of [[Def - Classification of Four-Vectors|spacetime]]**. Since every massive particle moves below $c$ and every signal at or below $c$, the bound implies that causal influence cannot outrun light, so the [[Def - Causality and the Light Cone|light cone]] bounds the region a particle can reach. The further result is that the time-ordering of timelike-separated events is frame-independent (no observer sees an effect precede its cause), the foundation of relativistic causality. The combination is nonobvious because a statement about *speeds* becomes a statement about the *order of events*.

Combine the conclusion with **rapidity**. Writing $|\mathbf V| = \tanh\varphi$, the bound $|\mathbf V| < 1$ becomes $\varphi < \infty$: the rapidity is finite but unbounded, ranging over all of $\mathbb{R}$ while the speed is confined to $(-1,1)$. The further result is that rapidity, not velocity, is the natural additive coordinate — collinear boosts add rapidities — and the speed limit is "rapidity infinity", an asymptote never reached. The combination explains why [[Def - Rapidity|rapidity]] is the better variable and why no finite chain of boosts reaches $c$.

---

# Why Is It True

The theorem is the geometric statement that a unit timelike vector cannot lean too far into the spacelike directions, and the reason is the minus sign in the metric.

Start from the unit-norm constraint in the observer's frame: $(u^0)^2 - \sum_i (u^i)^2 = 1$. The time component squared *exceeds* the sum of the spatial components squared, by exactly one. The relative speed is the ratio of the spatial magnitude to the time component, $|\mathbf V| = \sqrt{\sum (u^i)^2}/u^0$, and since the numerator-squared is $(u^0)^2 - 1 < (u^0)^2$, the ratio is strictly less than one. **The speed is bounded because the time component of a unit timelike vector always dominates its spatial part — the metric's minus sign forces $u^0$ to be the largest component.** That is the whole mechanism: the indefinite norm being $+1$ means the timelike part wins, and "the timelike part wins" is exactly "the speed is below $c$".

The cleanest invariant form uses the decomposition $U = \Gamma(U_0 + V)$. Impose $U \cdot U = 1$:
$$
1 = \Gamma^2(U_0 + V)\cdot(U_0 + V) = \Gamma^2\big(\underbrace{U_0 \cdot U_0}_{+1} + 2\underbrace{V \cdot U_0}_{0} + \underbrace{V \cdot V}_{-|\mathbf V|^2}\big) = \Gamma^2(1 - |\mathbf V|^2).
$$
For this to have a real, positive $\Gamma$, the factor $1 - |\mathbf V|^2$ must be positive, so $|\mathbf V| < 1$. The bound is the requirement that the Lorentz factor be real: if the speed reached $c$, the factor $1 - |\mathbf V|^2$ would vanish and $\Gamma$ would diverge; beyond $c$ it would go imaginary, signalling that no timelike four-velocity exists. The speed limit is the reality condition on $\Gamma$.

The tachyon perspective sharpens the intuition. The three causal classes are exactly the three velocity regimes: timelike ($V\cdot V < 0$ for the *relative velocity*, which corresponds to a timelike *worldline* and gives $|\mathbf V| < 1$), null ($|\mathbf V| = 1$, the photon), spacelike worldline ($|\mathbf V| > 1$, the tachyon). The speed of light is not a wall the particle pushes against; it is the geometric seam between the kinds of worldline a particle can have, and a massive particle is sewn into the timelike side. To cross to $c$ it would have to change the causal class of its worldline from timelike to null — to become massless — which it cannot do.

---

# What Makes This Hard

The computation is a single line — impose $U \cdot U = 1$ on $U = \Gamma(U_0 + V)$ and read off $1 - |\mathbf V|^2 > 0$ — so the difficulty is not algebraic. It is in seeing that the bound is *kinematic*, not dynamical: students reflexively explain the speed limit by the infinite energy needed to reach $c$, but the theorem needs no energy, no force, no mass increase — only the unit-norm constraint. The non-obvious step is recognising that "the four-velocity is a *unit* *timelike* vector" already contains the entire speed limit. The common error is to conflate this with the velocity-addition argument (about composing speeds) or with the relativistic-mass argument (about dynamics), missing that the cleanest statement is purely geometric.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Substitute the orthogonal decomposition $U = \Gamma(U_0 + V)$ into the unit-norm constraint $U \cdot U = 1$, use $V \cdot U_0 = 0$ and $V \cdot V = -|\mathbf V|^2$, and conclude that $\Gamma^2(1 - |\mathbf V|^2) = 1$ forces $|\mathbf V| < 1$ for $\Gamma$ to be real and finite.

**Subgoal decomposition:**

1. **Expand the norm of the decomposed four-velocity.** Show $U \cdot U = \Gamma^2(1 - |\mathbf V|^2)$.
   - *Hint:* $(U_0 + V)\cdot(U_0 + V) = U_0\cdot U_0 + 2V\cdot U_0 + V\cdot V$; use $U_0\cdot U_0 = 1$, $V\cdot U_0 = 0$, $V\cdot V = -|\mathbf V|^2$.
   - *Why needed:* It reduces the unit-norm constraint to a relation between $\Gamma$ and the speed.

2. **Impose unit norm.** Set $U \cdot U = 1$ to get $\Gamma^2(1 - |\mathbf V|^2) = 1$.
   - *Hint:* The four-velocity is a unit vector by definition.
   - *Why needed:* It is the master relation from which both $\Gamma = (1-|\mathbf V|^2)^{-1/2}$ and the bound follow.

3. **Read off the bound from reality of $\Gamma$.** Conclude $1 - |\mathbf V|^2 > 0$, i.e. $|\mathbf V| < 1$.
   - *Hint:* $\Gamma^2 = 1/(1 - |\mathbf V|^2)$ must be positive and finite; $|\mathbf V| = 1$ makes it diverge, $|\mathbf V| > 1$ makes $\Gamma^2 < 0$.
   - *Why needed:* It is the statement of the theorem; the photon ($|\mathbf V| = 1$) is the boundary, the tachyon ($|\mathbf V| > 1$) the forbidden region.

---

# Lemma Decomposition

> [!note]- Lemma 1: The norm of the decomposed four-velocity is $\Gamma^2(1 - |\mathbf V|^2)$
> **Statement:** For $U = \Gamma(U_0 + V)$ with $U_0 \cdot U_0 = 1$, $V \cdot U_0 = 0$, and $V$ spacelike with $|\mathbf V|^2 = -V\cdot V$, one has $U \cdot U = \Gamma^2(1 - |\mathbf V|^2)$.
>
> **Hint:** Expand the bilinear form and drop the cross term using orthogonality.
>
> **Why needed:** It is the algebraic core; everything else is reading off consequences.
>
> > [!note]- Full proof
> > By bilinearity, $U \cdot U = \Gamma^2 (U_0 + V)\cdot(U_0 + V) = \Gamma^2\big(U_0\cdot U_0 + 2\,V\cdot U_0 + V\cdot V\big)$. Now $U_0 \cdot U_0 = 1$ (observer four-velocity is unit), $V \cdot U_0 = 0$ (the relative velocity lies in the rest space, orthogonal to $U_0$), and $V \cdot V = -|\mathbf V|^2$ ($V$ is spacelike, and the speed is its Euclidean rest-space norm). Substituting, $U \cdot U = \Gamma^2(1 + 0 - |\mathbf V|^2) = \Gamma^2(1 - |\mathbf V|^2)$. $\blacksquare$

> [!note]- Lemma 2: Reality of the Lorentz factor bounds the speed
> **Statement:** If $\Gamma^2(1 - |\mathbf V|^2) = 1$ with $\Gamma$ real and finite, then $|\mathbf V| < 1$.
>
> **Hint:** Solve for $\Gamma^2$ and demand it be positive and finite.
>
> **Why needed:** It converts the master relation into the strict bound, and identifies $|\mathbf V| = 1$ as the (excluded) photonic boundary.
>
> > [!note]- Full proof
> > From $\Gamma^2(1 - |\mathbf V|^2) = 1$ we get $\Gamma^2 = (1 - |\mathbf V|^2)^{-1}$. For a massive particle $\Gamma = U \cdot U_0$ is a finite real number (the four-velocity exists and is a unit timelike vector), so $\Gamma^2$ is a positive finite real, forcing $1 - |\mathbf V|^2 > 0$, i.e. $|\mathbf V| < 1$. If $|\mathbf V| = 1$ the denominator vanishes and $\Gamma^2$ diverges — the four-velocity ceases to exist, which is exactly the photonic (null) case where the tangent cannot be normalised. If $|\mathbf V| > 1$ then $1 - |\mathbf V|^2 < 0$ and $\Gamma^2 < 0$, impossible for a real $\Gamma$ — the spacelike (tachyonic) case, with no timelike four-velocity. $\blacksquare$

> [!note]- Lemma 3: The bound is the boundary between causal classes
> **Statement:** The relative speed satisfies $|\mathbf V| < 1$, $= 1$, or $> 1$ according as the particle's worldline is timelike, null, or spacelike.
>
> **Hint:** Relate the sign of $\Gamma^2(1 - |\mathbf V|^2)$ to the sign of the worldline tangent's norm.
>
> **Why needed:** It interprets the bound geometrically and locates the photon and tachyon, showing $c$ is the seam between worldline types.
>
> > [!note]- Full proof
> > A worldline tangent $T$ proportional to $U_0 + V$ (with $V$ the relative velocity) has norm proportional to $1 - |\mathbf V|^2$. A timelike worldline has $T \cdot T > 0$, hence $1 - |\mathbf V|^2 > 0$ and $|\mathbf V| < 1$ (massive particle). A null worldline has $T \cdot T = 0$, hence $|\mathbf V| = 1$ (photon). A spacelike worldline has $T \cdot T < 0$, hence $|\mathbf V| > 1$ (tachyon). Thus the speed of light is precisely the value separating the three [[Def - Classification of Four-Vectors|causal classes]] of worldline, with massive particles strictly inside the timelike regime. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{P}$ be a massive particle with future timelike unit four-velocity $U$, and let $\mathcal{O}$ be an observer with four-velocity $U_0$, with crossing worldlines or $\mathcal{O}$ inertial, so the decomposition $U = \Gamma(U_0 + V)$ holds with $V \cdot U_0 = 0$ and $V$ spacelike.
>
> By Lemma 1,
> $$U \cdot U = \Gamma^2(1 - |\mathbf V|^2),$$
> where $|\mathbf V|^2 = -V \cdot V$ is the squared speed.
>
> Since $U$ is a unit vector, $U \cdot U = 1$, giving the master relation
> $$\Gamma^2(1 - |\mathbf V|^2) = 1.$$
>
> By Lemma 2, the Lorentz factor $\Gamma = U \cdot U_0$ is a finite real number for a massive particle, so $\Gamma^2 = (1 - |\mathbf V|^2)^{-1}$ is a positive finite real, which forces
> $$1 - |\mathbf V|^2 > 0,\qquad\text{i.e.}\qquad |\mathbf V| < 1 = c.$$
>
> The speed of any massive particle relative to any observer (locally, or globally if the observer is inertial) is therefore strictly below the speed of light. By Lemma 3, the value $|\mathbf V| = c$ is attained only by a null worldline (a photon, whose tangent cannot be normalised, so $\Gamma$ diverges), and $|\mathbf V| > c$ only by a spacelike worldline (a tachyon, for which $\Gamma^2 < 0$ and no timelike four-velocity exists). Hence $c$ is a strict upper bound for massive relative velocities and the exact boundary between the causal classes. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Accelerator physics — the unreachable ceiling at the LHC.** Protons in the LHC reach $\Gamma \approx 7000$, corresponding to $|\mathbf V| = \sqrt{1 - \Gamma^{-2}} \approx 1 - 10^{-8}$: within ten parts per billion of $c$, yet provably below it for any finite energy. Computing how close to $c$ a given Lorentz factor brings a particle — and confirming the gap never closes — is the bound made numerical. The application shows the speed limit is approached asymptotically, never breached, as the energy (hence $\Gamma$) grows without bound.

**Causality and signalling — why faster-than-light implies time travel.** If a signal could exceed $c$, some inertial observer would see it travel backward in time, allowing a message to its own past and a causal paradox. The bound $|\mathbf V| < c$ for massive carriers, combined with the [[Def - Classification of Four-Vectors|causal classification]], is what forbids this; deriving the backward-signalling from an assumed superluminal speed battle-tests the bound against the deepest structural constraint of the theory. See [[Ex - Classifying worldlines and why tachyons would signal into the past]].

**Plasma and astrophysics — apparent superluminal motion.** Relativistic jets from active galactic nuclei can *appear* to move across the sky faster than light, because a blob moving toward us at $|\mathbf V| < c$ nearly catches its own emitted light. The *apparent* transverse speed can exceed $c$ while the *actual* speed stays below it — an illusion, not a violation. Reconciling the superluminal appearance with the bound is a classic exercise, isolating the difference between the genuine relative velocity (below $c$) and a projected, light-travel-time-distorted apparent velocity.

---

# Bridges

- **[[Thm - Relativistic Velocity Addition]]** — the composition view of the same ceiling. Where velocity addition shows that *combining* two sub-light speeds never reaches $c$ (with $c$ a fixed point of the composition law), this theorem shows that a *single* particle's relative speed is below $c$ for purely kinematic reasons. The two are consistent: composition cannot escape the timelike regime because it maps timelike four-velocities to timelike four-velocities. Rapidity unifies them — addition of rapidities is unbounded, but the corresponding speed asymptotes to $c$.

- **[[Def - Classification of Four-Vectors]]** — the geometric backbone. The three velocity regimes $|\mathbf V| < c$, $= c$, $> c$ are exactly the timelike, null, and spacelike worldline classes. This theorem is the velocity-space face of the causal trichotomy: a massive particle lives in the timelike class, so its speed is below $c$; the speed of light is the null seam; tachyons would inhabit the spacelike class. The invariance of the classification (the sign of a norm is Lorentz-invariant) is why every observer agrees the particle is sub-light.

- **[[Thm - Invariance of the Velocity of Light]]** — the boundary case. This theorem gives the strict bound for massive particles; the invariance-of-light theorem gives the equality for photons, $|\mathbf V| = c$ exactly, for every observer. Together they say the speed of light is simultaneously the unreachable ceiling for massive particles and the universal, observer-independent speed of light itself — the same number playing two roles, both forced by the geometry of timelike and null vectors.

- **[[Def - Rapidity]]** — the unbounded coordinate. The bound $|\mathbf V| < c$ corresponds, under $|\mathbf V| = \tanh\varphi$, to $\varphi \in \mathbb{R}$ finite but unbounded: rapidity has no ceiling, while velocity asymptotes to $c$. This is why rapidity is the natural parameter for boosts and why the speed limit is "rapidity infinity" — an asymptote, not a wall, reached only in the photonic limit.

---

# Unlocked by This

> [!tip] The Massless Limit and Photon Four-Momentum *(from Relativistic Dynamics)*
> The photon sits exactly at the boundary $|\mathbf V| = c$ that massive particles approach but never reach. Taking the rest mass to zero at fixed energy sends $\Gamma \to \infty$ and $|\mathbf V| \to c$, and the four-momentum $P = mU = \Gamma m(U_0 + V)$ tends to a finite null vector — the [[Def - The Four-Momentum of a Photon|photon four-momentum]]. The speed ceiling is thus the kinematic gateway from massive to massless particles, developed in **Special Relativity XIII**.

> [!tip] Relativistic Causality and the Light Cone *(from Causal Structure)*
> Because every massive particle and every signal travels at or below $c$, causal influence is confined to the future [[Def - Causality and the Light Cone|light cone]], and the time-ordering of causally connected (timelike-separated) events is the same for all observers. The bound is what guarantees that no observer sees an effect precede its cause — the consistency of relativistic causality — and it is why a faster-than-light particle would be a faster-than-light *signal*, hence a time machine.
