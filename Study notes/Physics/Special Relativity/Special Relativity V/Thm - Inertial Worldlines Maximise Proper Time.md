---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Proper Time"
  - "Def - Worldline of a Particle"
  - "Thm - The Reversed Triangle Inequality"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X \cdot X > 0$ and the [[Def - Proper Time|proper time]] along a worldline is $\tau = \int\sqrt{ds^2} = \int\sqrt{dt^2 - d\mathbf{x}^2}$. Events are $A, B$ with $B$ in the future light cone of $A$. A worldline joining them is $\mathcal{L}$; the straight (inertial) one is $\mathcal{L}_0$. In an inertial frame adapted to $\mathcal{L}_0$ (its four-velocity along the time axis), a competing worldline is written $\mathbf{x} = (X(t), Y(t), Z(t))$, dots denoting $d/dt$. Full registry on [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

---

# Statement

> **Theorem (inertial worldlines maximise proper time).** Let $A$ and $B$ be two events of Minkowski space with $B$ inside the future light cone of $A$ (so they can be joined by a timelike worldline). Among all timelike [[Def - Worldline of a Particle|worldlines]] from $A$ to $B$, the straight (inertial) worldline $\mathcal{L}_0$ has the **greatest** [[Def - Proper Time|proper time]]:
> $$\tau[\mathcal{L}] \;\le\; \tau[\mathcal{L}_0] \qquad\text{for every timelike worldline } \mathcal{L} \text{ from } A \text{ to } B,$$
> with equality if and only if $\mathcal{L} = \mathcal{L}_0$. Equivalently, in any inertial frame in which $A$ and $B$ are separated by $(\Delta t, \mathbf{0})$, every worldline satisfies $\tau[\mathcal{L}] \le \Delta t$, the proper time of the inertial worldline. The straight timelike line is a **timelike geodesic** — a curve of extremal (here maximal) metric length.

> **Corollary (twin paradox).** Of two twins who part at $A$ and reunite at $B$, the one who moves inertially (straight worldline) ages the most; any twin who accelerates (bent worldline) returns younger.

The conclusion is the exact opposite of the Euclidean fact that a straight line is the *shortest* path between two points — see Why Is It True.

---

# Motivation

The [[Def - Proper Time|proper time]] between two events depends on the worldline joining them, not just on the endpoints. That raises an immediate question with a definite answer: *which* worldline accumulates the most proper time? The question matters because proper time is the time a clock actually reads, so this is the question "which traveller ages the most between two meetings?" — and the answer is the foundation of both the resolution of the twin paradox and the variational principle of relativistic mechanics.

The result is the relativistic counterpart of the most familiar fact in Euclidean geometry — that a straight line is the shortest path between two points — but with a startling sign reversal: in spacetime the straight worldline is the *longest* in proper time, not the shortest. A clock that wanders through space, accelerating away and back, banks *less* time than one that sits still. This is not a paradox to be explained away; it is a direct consequence of the minus signs in the metric, and once it is internalised the twin paradox stops being puzzling — the travelling twin ages less simply because their worldline is "shorter" in the proper-time sense.

The theorem is also the special-relativistic seed of the **geodesic principle** that governs motion under gravity. A free particle is observed to follow the straight worldline; this theorem says the straight worldline is the one that extremises proper time, $\delta\int d\tau = 0$. Promoting "extremise proper time" to a *law of motion* — true even when the metric is curved — is exactly how general relativity describes free fall: a freely-falling particle follows the timelike geodesic, the curve of extremal proper time in the curved metric. So the content of this theorem, "inertial worldlines extremise proper time", is the flat-space prototype of "free-fall worldlines are geodesics".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "two timelike-separated events and a family of timelike worldlines joining them". The point of input broadening is to recognise the situations that secretly present this.

The first disguised source is **"two observers part and later reunite"**. Any scenario with two travellers who separate at one event and meet again at another — twins, a muon and the lab, two clocks on different flights — is exactly this setup, with the worldlines being the travellers' histories. The bridge is that an observer *is* a timelike worldline ([[Def - Worldline of a Particle]]), so "two observers meeting twice" is "two timelike worldlines with common endpoints". *Example problem:* decide which of two twins is younger at reunion ([[Ex - The twin paradox]]) — the inertial one is older.

The second disguised source is **"a sum of future-timelike four-vectors with fixed total"**. Whenever a bent worldline is approximated by straight timelike segments $U_1, U_2, \dots$ with fixed vector sum $U_1 + \cdots + U_n = \overrightarrow{AB}$, the question "is the bent path shorter?" is the question whether $\|U_1\| + \cdots + \|U_n\| \le \|U_1 + \cdots + U_n\|$ — which is the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]]. The bridge is that proper time of a straight segment is its Minkowski norm. *Example problem:* show a two-leg journey out-and-back has less proper time than staying put — directly the reversed triangle inequality applied to $U + V$ versus $U + V$.

The third disguised source is **"an integral $\int\sqrt{1 - u^2}\,dt$ is to be bounded"**. Any quantity of the form "elapsed proper time of a moving clock" is this integral, and the theorem says it is maximised by $u = 0$ (staying at rest in the adapted frame). The bridge is the local time-dilation factor $d\tau = dt\sqrt{1 - u^2} \le dt$. *Example problem:* compute and bound the proper time of an [[Ex - Proper time along an accelerated worldline|accelerated worldline]], confirming it falls short of the inertial value.

**Targets (Output Amplification)**

The conclusion is "$\tau[\mathcal{L}] \le \tau[\mathcal{L}_0]$, with equality only for the straight line".

Combine the conclusion with **the variational principle $\delta\int d\tau = 0$**. Since the straight worldline is the maximiser, it is in particular a stationary point of the proper-time functional, so the inertial worldline extremises $\int d\tau$. The further result is the [[Special Relativity XV — The Principle of Least Action|action principle]] for the free relativistic particle, $S = -m\int d\tau$, whose Euler–Lagrange equations give $dU/d\tau = 0$. The combination is useful because it converts a geometric inequality into a dynamical law, and the law generalises to curved spacetime where the inequality (a global maximum) may fail but the stationarity (geodesic) survives.

Combine the conclusion with **the limit of bending the worldline toward null**. The proper time can be made *arbitrarily small* by routing the worldline ever closer to a light-ray zigzag (out at nearly $c$, back at nearly $c$), since null segments have zero proper time. The further result is that proper time between two fixed events ranges over the open interval $(0, \tau_0]$: the inertial value $\tau_0$ is the supremum and is attained, while $0$ is the infimum and is *not* attained. The combination is nonobvious because it says the maximiser is unique and attained while the minimiser does not exist — a one-sided extremum, a hallmark of the indefinite metric. *Example:* the [[Ex - A round trip to the galactic centre|galactic-centre traveller]] can compress decades of Earth-time into a few years of ship-time, with no positive lower bound on ship-time.

Combine the conclusion with **the invariance of proper time**. Because $\tau$ is [[Thm - Invariance of the Spacetime Interval|frame-independent]], the verdict "the inertial twin is older" holds in *every* frame — it is not an artefact of the lab frame. The further result is that the twin paradox has no frame-dependent escape: there is no frame in which the accelerated twin ages more. The combination is what defeats the naive "by symmetry each should see the other as younger" objection — the comparison is of two invariant numbers, $\tau[\mathcal{L}]$ and $\tau[\mathcal{L}_0]$, and invariants do not flip between frames.

---

# Why Is It True

The deep reason is the rotation analogy, run with the metric's minus signs in place — and the sign flip is the whole story.

**In Minkowski space, spatial motion subtracts from elapsed time, so the path that moves least in space banks the most time.** That single sentence is the mechanism. The infinitesimal proper time is $d\tau = \sqrt{dt^2 - d\mathbf{x}^2} = dt\sqrt{1 - u^2}$, and the spatial displacement enters with a *minus* sign. The more a worldline moves through space (the larger $u$), the smaller the square root, and the less proper time accumulates per unit of coordinate time. The inertial worldline between $A$ and $B$, in the frame where $A$ and $B$ are at the same place, does not move through space at all ($\mathbf{x}$ constant), so it suffers no reduction: it accumulates the full $\int dt$. Every other worldline must move through space to get from $A$ to $B$ and back to the same place (or detour), and every bit of spatial motion costs it proper time. So the straight worldline wins.

Contrast the Euclidean situation, where the analogous "length" is $\int\sqrt{dt^2 + d\mathbf{x}^2}$ with a *plus* sign: there, motion *adds* to the length, so the path that moves least (the straight line) is the *shortest*. The relativistic minus sign flips "shortest" to "longest". This is the same flip that turns the circle-preserving rotations $\cos\theta, \sin\theta$ into the hyperbola-preserving boosts $\cosh\varphi, \sinh\varphi$, and that reverses the triangle inequality.

The triangle-inequality picture makes the discreteness of the argument visible. Approximate any bent worldline by a chain of straight timelike segments $U_1, U_2, \dots, U_n$, future-directed, with $U_1 + \cdots + U_n = \overrightarrow{AB}$ the straight displacement. The proper time of the bent path is the sum of the segment lengths $\sum\|U_i\|$, and the proper time of the straight path is $\|\overrightarrow{AB}\| = \|\sum U_i\|$. The [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] for future-timelike vectors says $\|\sum U_i\| \ge \sum\|U_i\|$ — the norm of the sum is at least the sum of the norms — which is precisely $\tau[\mathcal{L}_0] \ge \tau[\mathcal{L}]$. Each "kink" where the chain bends is a place where strict inequality bites; a straight chain (no kinks) is the only case of equality. So the theorem is the reversed triangle inequality, integrated.

One should also see *why bending must cost something*. At a kink, two future-timelike segments meet at an angle (a change of velocity, i.e. acceleration). The reversed triangle inequality is strict unless the two segments are parallel; a genuine change of direction in spacetime — which is what acceleration is — always strictly reduces the total length. So the proper-time deficit of a worldline is a direct measure of how much it accelerates: a straight (unaccelerated) worldline has zero deficit, and the more it bends, the larger the deficit.

---

# What Makes This Hard

The conceptual hurdle is believing the sign: every Euclidean instinct says "straight = shortest", and one must actively hold onto the fact that the indefinite metric reverses this to "straight = longest". The technical subtlety is that the inequality $\sqrt{1 - (\dot X^2 + \dot Y^2 + \dot Z^2)} \le 1$ used in the proof is pointwise and becomes equality only when all spatial velocities vanish, so one must argue that the *integrated* inequality is strict unless the worldline is straight in the adapted frame. The most common error is to misidentify which worldline is the geodesic, or to assert (falsely) that the geodesic *minimises* — null geodesics minimise (length zero), but timelike geodesics maximise.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Choose the inertial frame adapted to the straight worldline $\mathcal{L}_0$ — the frame in which $\mathcal{L}_0$ runs along the time axis, so $A$ and $B$ have spatial coordinates that agree. In this frame the straight worldline's proper time is just the coordinate-time difference $\Delta t$. Parametrise any competing worldline $\mathcal{L}$ by the coordinate time $t$ of this frame (legitimate because $\mathcal{L}$ is timelike, hence everywhere inside the light cone, so $t$ increases monotonically along it). Write its proper time as an integral and bound the integrand pointwise.

**Subgoal decomposition:**

1. **Set up the adapted frame and parametrise by $t$.** Choose the frame where $\mathcal{L}_0$ is the time axis; then $A = (t_A, \mathbf{x}_0)$, $B = (t_B, \mathbf{x}_0)$ for a common $\mathbf{x}_0$, and $\tau[\mathcal{L}_0] = t_B - t_A$. Parametrise $\mathcal{L}$ as $\mathbf{x} = (X(t), Y(t), Z(t))$.
   - *Hint:* A timelike worldline stays inside light cones, so $dt > 0$ along it and $t$ is a good parameter.
   - *Why needed:* It makes the straight worldline's proper time trivial and gives a common parameter for the comparison.

2. **Write the proper time of $\mathcal{L}$ as an integral over $t$.** Using $d\tau = \sqrt{dt^2 - d\mathbf{x}^2}$, factor out $dt$.
   - *Hint:* $d\tau = dt\sqrt{1 - (\dot X^2 + \dot Y^2 + \dot Z^2)}$.
   - *Why needed:* It exposes the integrand that must be bounded.

3. **Bound the integrand pointwise.** The square root is $\le 1$, with equality iff $\dot X = \dot Y = \dot Z = 0$.
   - *Hint:* $\dot X^2 + \dot Y^2 + \dot Z^2 \ge 0$, so $1 - (\dots) \le 1$.
   - *Why needed:* It turns the integral inequality into the result.

4. **Integrate and identify the equality case.** $\tau[\mathcal{L}] = \int\sqrt{1 - |\dot{\mathbf{x}}|^2}\,dt \le \int dt = t_B - t_A = \tau[\mathcal{L}_0]$, with equality iff $\mathbf{x}$ is constant, i.e. $\mathcal{L} = \mathcal{L}_0$.
   - *Hint:* Equality in the integral forces equality in the integrand everywhere.
   - *Why needed:* It delivers both the inequality and the uniqueness of the maximiser.

---

# Lemma Decomposition

> [!note]- Lemma 1: A timelike worldline can be parametrised by the adapted coordinate time
> **Statement:** In an inertial frame adapted to $\mathcal{L}_0$, the coordinate time $t$ strictly increases along any timelike worldline $\mathcal{L}$ from $A$ to $B$, so $\mathbf{x} = \mathbf{x}(t)$ is a valid parametrisation with $|\dot{\mathbf{x}}| < 1$.
>
> **Hint:** A future-timelike tangent has positive time component and $|d\mathbf{x}/dt| < 1$.
>
> **Why needed:** It legitimises using $t$ as the common parameter and guarantees the integrand's square root is real.
>
> > [!note]- Full proof
> > A worldline is timelike, so its tangent $V = (dt/d\lambda)(1, d\mathbf{x}/dt)$ has $V \cdot V > 0$, i.e. $(dt/d\lambda)^2(1 - |d\mathbf{x}/dt|^2) > 0$, forcing $|d\mathbf{x}/dt| < 1$. Future-directedness gives $dt/d\lambda > 0$, so $t$ increases monotonically along $\mathcal{L}$ and may be used as a parameter; the bound $|\dot{\mathbf{x}}| < 1$ ensures $1 - |\dot{\mathbf{x}}|^2 > 0$, so $\sqrt{1 - |\dot{\mathbf{x}}|^2}$ is real and positive. $\blacksquare$

> [!note]- Lemma 2: The proper-time integrand is bounded by $1$
> **Statement:** Along $\mathcal{L}$, $d\tau = dt\sqrt{1 - |\dot{\mathbf{x}}|^2} \le dt$, with equality at a point iff $\dot{\mathbf{x}} = 0$ there.
>
> **Hint:** $|\dot{\mathbf{x}}|^2 \ge 0$, and $\sqrt{1 - s} \le 1$ for $s \ge 0$ with equality iff $s = 0$.
>
> **Why needed:** It is the pointwise inequality whose integral gives the theorem, and its equality condition pins down the maximiser.
>
> > [!note]- Full proof
> > From $d\tau^2 = dt^2 - |d\mathbf{x}|^2$, dividing by $dt^2$ (positive by Lemma 1) gives $(d\tau/dt)^2 = 1 - |\dot{\mathbf{x}}|^2$. Since $|\dot{\mathbf{x}}|^2 = \dot X^2 + \dot Y^2 + \dot Z^2 \ge 0$, we have $0 < 1 - |\dot{\mathbf{x}}|^2 \le 1$, hence $0 < d\tau/dt \le 1$, i.e. $d\tau \le dt$. Equality holds at a point exactly when $|\dot{\mathbf{x}}|^2 = 0$, i.e. all three spatial velocities vanish there. $\blacksquare$

> [!note]- Lemma 3: Equality in the integral forces the straight worldline
> **Statement:** If $\int\sqrt{1 - |\dot{\mathbf{x}}|^2}\,dt = \int dt$ over $[t_A, t_B]$, then $\dot{\mathbf{x}} \equiv 0$, so $\mathbf{x}$ is constant and $\mathcal{L} = \mathcal{L}_0$.
>
> **Hint:** A continuous nonnegative integrand with the same integral as its upper bound must equal the bound everywhere.
>
> **Why needed:** It upgrades the inequality to a strict one for every non-inertial worldline, giving uniqueness of the maximiser.
>
> > [!note]- Full proof
> > Let $f(t) = 1 - \sqrt{1 - |\dot{\mathbf{x}}(t)|^2} \ge 0$, continuous and nonnegative by Lemma 2. The hypothesis says $\int_{t_A}^{t_B} f(t)\,dt = 0$. A continuous nonnegative function with zero integral vanishes identically, so $f \equiv 0$, i.e. $\sqrt{1 - |\dot{\mathbf{x}}|^2} = 1$ everywhere, forcing $|\dot{\mathbf{x}}| \equiv 0$. Then $\mathbf{x}(t)$ is constant, equal to the common spatial coordinate $\mathbf{x}_0$ of $A$ and $B$, so $\mathcal{L}$ is the straight time-axis worldline $\mathcal{L}_0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** Since $B$ lies inside the future light cone of $A$, the displacement $\overrightarrow{AB}$ is future timelike, and at least one timelike worldline joins $A$ to $B$ (the straight one). Choose an inertial frame adapted to the straight worldline $\mathcal{L}_0$: take its [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0 \propto \overrightarrow{AB}$ along the time axis. In this frame $A = (t_A, \mathbf{x}_0)$ and $B = (t_B, \mathbf{x}_0)$ share the spatial coordinate $\mathbf{x}_0$, with $t_B > t_A$, and the straight worldline has
> $$\tau[\mathcal{L}_0] = \int_{t_A}^{t_B}\sqrt{dt^2 - 0} = t_B - t_A.$$
>
> **Step 1 — parametrise the competitor by $t$.** Let $\mathcal{L}$ be any timelike worldline from $A$ to $B$. By Lemma 1, $t$ increases monotonically along $\mathcal{L}$, so $\mathcal{L}$ is the graph $\mathbf{x} = \mathbf{x}(t) = (X(t), Y(t), Z(t))$ for $t \in [t_A, t_B]$, with $\mathbf{x}(t_A) = \mathbf{x}(t_B) = \mathbf{x}_0$ and $|\dot{\mathbf{x}}| < 1$.
>
> **Step 2 — write its proper time.** By definition of [[Def - Proper Time|proper time]],
> $$\tau[\mathcal{L}] = \int_{\mathcal{L}}\sqrt{dt^2 - d\mathbf{x}^2} = \int_{t_A}^{t_B}\sqrt{1 - \big(\dot X^2 + \dot Y^2 + \dot Z^2\big)}\;\,dt.$$
>
> **Step 3 — bound pointwise.** By Lemma 2 the integrand satisfies $\sqrt{1 - |\dot{\mathbf{x}}|^2} \le 1$ at every $t$, so
> $$\tau[\mathcal{L}] = \int_{t_A}^{t_B}\sqrt{1 - |\dot{\mathbf{x}}|^2}\;dt \ \le\ \int_{t_A}^{t_B} dt = t_B - t_A = \tau[\mathcal{L}_0].$$
>
> **Step 4 — equality case.** By Lemma 3, equality $\tau[\mathcal{L}] = \tau[\mathcal{L}_0]$ forces $\dot{\mathbf{x}} \equiv 0$, hence $\mathbf{x} \equiv \mathbf{x}_0$ and $\mathcal{L} = \mathcal{L}_0$. Therefore the straight worldline strictly maximises the proper time among all timelike worldlines from $A$ to $B$.
>
> **Geodesic statement and corollary.** The straight timelike line is thus a curve of extremal (maximal) metric length — a **timelike geodesic** — and $\delta\int d\tau = 0$ at it. The twin-paradox corollary is immediate: the twin on $\mathcal{L}_0$ (inertial) reads $\tau[\mathcal{L}_0]$, every accelerating twin reads strictly less, so the inertial twin is older at reunion. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The brachistochrone's mirror image (calculus of variations).** The Euclidean variational problem "shortest path between two points" has the straight line as a minimiser; this theorem is its Lorentzian mirror, "longest proper time", with the straight worldline a maximiser. Setting up the Euler–Lagrange equation for $\int\sqrt{1 - |\dot{\mathbf{x}}|^2}\,dt$ and finding its (maximising) extremal is an instructive variational exercise that makes the sign reversal explicit; the application is nonobvious because variational problems are reflexively associated with minimisation.

**Invariant mass of a composite as a triangle inequality (particle physics).** The reversed triangle inequality behind this theorem also bounds the [[Def - Four-Momentum and Rest Mass|invariant mass]] of a system: $M = \|\sum P_i\| \ge \sum\|P_i\| = \sum m_i$, so a bound system's mass exceeds the sum of its parts' masses unless they are all comoving. This is the same inequality with four-momenta in place of worldline displacements; the application is out-of-distribution because "mass" does not look like "proper time" until both are seen as Minkowski norms.

**Geodesics on a Lorentzian surface (differential geometry).** On a curved Lorentzian manifold the analogous statement — that timelike geodesics locally maximise proper time — is a cornerstone of causality theory and the singularity theorems. Verifying it for a simple curved metric (for example a $2$-dimensional Robertson–Walker or Rindler patch) and watching the *global* maximum fail (conjugate points) while the *local* extremum survives is a clean bridge from this flat result to general relativity; the application is surprising because the flat global maximum is so robust.

---

# Bridges

- **[[Thm - The Reversed Triangle Inequality]]** — this theorem *is* the reversed triangle inequality, integrated along a worldline. For two future-timelike vectors $U, V$ the reversed inequality $\|U + V\| \ge \|U\| + \|V\|$ says the straight path (displacement $U + V$) beats the two-leg path (legs $U$, $V$) in proper time; a general bent worldline is the limit of many such legs, and the theorem follows by summing. The reversed inequality is the infinitesimal/discrete statement, this theorem the integrated/continuous one.

- **[[Def - Proper Time]]** — the theorem is a statement about the proper-time functional, and it is what makes proper time behave like a *time* rather than a *length*: the straightest clock ages the most, so "ageing" and "metric length of worldline" are the same thing, with the extremum a maximum because the metric is indefinite.

- **Euclidean geodesics minimise distance** — the exact analogue with the sign reversed: in a Riemannian manifold the straight line (geodesic) *minimises* arc length; in a Lorentzian manifold the straight timelike line (geodesic) *maximises* proper time. The proof structures are mirror images, differing only in whether the spatial term enters the line element with a plus or a minus.

- **[[Special Relativity XV — The Principle of Least Action]]** — promoting "the inertial worldline extremises $\int d\tau$" to a variational *principle* gives the action $S = -m\int d\tau$ of the free relativistic particle; the conjugate momentum is the [[Def - Four-Momentum and Rest Mass|four-momentum]], and the Euler–Lagrange equations are $dU/d\tau = 0$. The theorem provides the geometric content that the action principle then elevates to a law.

---

# Unlocked by This

> [!tip] The Geodesic Principle of General Relativity *(from General Relativity)*
> This theorem is the flat-space prototype of the **geodesic principle**: a freely-falling particle follows the timelike curve that extremises proper time. In a curved spacetime $(M, g)$ the proper-time functional is $\int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$, and its extremals are the **timelike geodesics**, obeying $\dfrac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu{}_{\nu\rho}\dfrac{dx^\nu}{d\tau}\dfrac{dx^\rho}{d\tau} = 0$ with the **Christoffel symbols** $\Gamma$ built from the metric. Free fall *is* geodesic motion, and the straight inertial worldline of this theorem is the $g = \eta$, $\Gamma = 0$ case. Crucially, in curved spacetime the *global* maximum can fail — beyond a conjugate point a geodesic no longer maximises — but the *local* extremum (stationarity) always survives, which is why the law of motion is "extremise", not "maximise". The resolution of the twin paradox in a gravitational field (e.g. a clock at altitude versus one on the ground) is computed by exactly this principle.

> [!tip] Time Travel to the Future, and its Limits *(from this chapter)*
> Because an accelerating traveller's worldline is shorter in proper time, a round trip can compress an arbitrary amount of coordinate time into a short ship-time — effectively **time travel to the future** ([[Ex - A round trip to the galactic centre]]). The traveller can reach the galactic centre, ageing only years while millennia pass on Earth, all while moving strictly slower than light. But the same Minkowski structure forbids time travel to the *past*: with all light cones parallel, no worldline can return to an event in its own past while staying timelike. Only in curved spacetime, where light cones tip over, can this prohibition be challenged.
