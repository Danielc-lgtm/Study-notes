---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Vector"
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Four-vectors are $U, V$; the metric is $\eta = \mathrm{diag}(1,-1,-1,-1)$; the norm-squared is $U\cdot U = \eta_{\mu\nu}U^\mu U^\nu = (U^0)^2 - |\mathbf{U}|^2$. For a future-pointing timelike $U$ ($U\cdot U > 0$, $U^0 > 0$) the **Minkowski norm** is $\|U\| = \sqrt{U\cdot U} \ge 0$ — a genuine non-negative real number, since $U\cdot U > 0$. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Statement

> **The reversed (Minkowski) triangle inequality.** Let $U$ and $V$ be future-pointing timelike four-vectors. Then $U + V$ is again future-pointing timelike, and
> $$\boxed{\quad \sqrt{(U+V)\cdot(U+V)} \;\ge\; \sqrt{U\cdot U} \;+\; \sqrt{V\cdot V}\,, \quad}$$
> that is, $\|U + V\| \ge \|U\| + \|V\|$. Equality holds if and only if $U$ and $V$ are parallel (proportional).
>
> Compare the Euclidean triangle inequality $|\mathbf{u}+\mathbf{v}| \le |\mathbf{u}| + |\mathbf{v}|$: the inequality is **reversed**.

---

# Motivation

In Euclidean geometry the triangle inequality $|\mathbf{u}+\mathbf{v}| \le |\mathbf{u}|+|\mathbf{v}|$ says the straight path between two points is the *shortest*. It is the bedrock of "distance" — it is what makes the Euclidean norm a metric. The natural question, once [[Def - Minkowski Space and the Metric|Minkowski space]] is in hand, is whether the analogous statement holds for the Minkowski norm.

It does not — and the failure is not a defect but a discovery. For future-pointing timelike four-vectors the inequality holds with the sign *reversed*: $\|U+V\| \ge \|U\|+\|V\|$. The straight path is the *longest*, not the shortest.

To see why this matters, recall what the Minkowski norm of a timelike four-vector *means*. The pseudo-norm of a future-pointing timelike displacement is the [[Def - The Spacetime Interval|interval]] along it, which is the [[Def - Proper Time|proper time]] — the time a clock reads as it travels that displacement. Now interpret the theorem along worldlines. A clock going straight from event $A$ to event $C$ accumulates proper time $\|\overrightarrow{AC}\|$. A clock that detours through an intermediate event $B$ accumulates $\|\overrightarrow{AB}\| + \|\overrightarrow{BC}\|$. The theorem says the straight clock reads *more*:
$$\|\overrightarrow{AC}\| \ge \|\overrightarrow{AB}\| + \|\overrightarrow{BC}\|.$$
The inertial (straight, unaccelerated) worldline between two timelike-separated events has the **longest** proper time of any worldline joining them. Every detour — every bit of acceleration — *costs* proper time.

This is the geometric heart of the [[Ex - The twin paradox|twin paradox]]. The stay-at-home twin follows the straight worldline; the travelling twin follows a bent one. The theorem says straight is longest, so the stay-at-home twin ages more. The paradox's apparent symmetry is broken by exactly the asymmetry the theorem quantifies: one worldline is straight, the other bent, and bending costs time.

One should *expect* the reversal from the rotation analogy. The Euclidean triangle inequality is, at bottom, the Cauchy–Schwarz inequality $\mathbf{u}\cdot\mathbf{v} \le |\mathbf{u}||\mathbf{v}|$. Cauchy–Schwarz needs a *positive-definite* inner product. The Minkowski inner product is indefinite, so Cauchy–Schwarz fails — and on the timelike cone it fails in a definite direction, $U\cdot V \ge \|U\|\|V\|$ (the inequality flipped), which integrates up to the reversed triangle inequality. The reversal is the signature change of the metric, propagated to the level of inequalities.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$U$ and $V$ are future-pointing timelike four-vectors".

The first disguised source is **$U$ and $V$ are the four-velocities (times proper times) of physical observers**. Any massive observer has a future-pointing timelike four-velocity ([[Def - Classification of Four-Vectors]]); a worldline segment is its four-velocity scaled by the proper time elapsed, again future-pointing timelike. The bridge is that "physical observer" implies "timelike worldline". So whenever a problem features the worldlines of real observers or particles, the theorem's hypothesis is met. *Example problem:* compare the ageing of two twins ([[Ex - The twin paradox]]).

The second disguised source is **$U$ and $V$ are future-pointing timelike four-momenta**. A massive particle's [[Def - Four-Momentum and Rest Mass|four-momentum]] is future-pointing timelike, $P\cdot P = m^2 > 0$. The bridge is the classification of four-momenta. The theorem then bounds the invariant mass of a composite: $\|P_1 + P_2\| \ge \|P_1\| + \|P_2\|$ says the invariant mass of two particles is at least the sum of their rest masses, with equality iff they are at relative rest. *Example problem:* [[Ex - The invariant mass of a system of particles]].

The third disguised source is **a sum of many timelike four-vectors — a piecewise worldline**. The two-vector inequality iterates: a worldline broken into many timelike segments has total proper time at most that of the straight segment spanning the same endpoints. The bridge is induction on the number of segments. *Example problem:* a clock taken on any closed-then-returning journey reads less than an inertial clock — the continuum twin paradox.

**Targets (Output Amplification)**

The conclusion is "$\|U+V\| \ge \|U\| + \|V\|$, with $U+V$ future-pointing timelike".

Combine the conclusion with **the proper-time interpretation of $\|\cdot\|$**. Since $\|U\|$ is the proper time along the timelike vector $U$, the inequality becomes "straight worldline maximises proper time". The further result is a *variational principle*: among all timelike worldlines between two events, the inertial one is the unique maximiser of proper time. This is the special-relativistic prototype of the geodesic principle of general relativity — freely-falling worldlines extremise proper time.

Combine the conclusion with **the limit of null worldlines**. As a worldline's segments approach the light cone, each $\|U\|$ tends to $0$, so the *total* proper time of a near-light detour tends to $0$. The further result is that there is no positive lower bound on proper time between two timelike-separated events — a clock can be made to read arbitrarily little by travelling near $c$ — and the infimum, $0$, is approached but never attained (a null worldline is not a clock). The combination explains the asymmetry of the twin paradox at its extreme.

Combine the conclusion with **iteration to a smooth curve**. Iterating gives, in the continuum limit, $\tau[\gamma] = \int\sqrt{ds^2} \le \|\overrightarrow{AC}\|$ for any timelike curve $\gamma$ from $A$ to $C$. The further result is the full statement that proper time is a *concave* functional maximised by the straight line — the foundation of the relativistic action principle for a free particle, whose Lagrangian is $-m\int d\tau$.

---

# Why Is It True

The cleanest intuition is to compare with Euclidean geometry term by term and watch the one sign flip.

In a Euclidean plane, the triangle inequality $|\mathbf{u}+\mathbf{v}| \le |\mathbf{u}|+|\mathbf{v}|$ holds because, when you square it, the cross term obeys Cauchy–Schwarz: $\mathbf{u}\cdot\mathbf{v} \le |\mathbf{u}||\mathbf{v}|$. The cross term is *bounded above* by the product of the norms, and that bound is exactly what makes $|\mathbf{u}+\mathbf{v}|^2 = |\mathbf{u}|^2 + 2\mathbf{u}\cdot\mathbf{v} + |\mathbf{v}|^2$ no bigger than $(|\mathbf{u}|+|\mathbf{v}|)^2$.

In Minkowski geometry, restrict to future-pointing timelike $U, V$. The key fact — the reversed Cauchy–Schwarz — is that now the cross term is *bounded below*: $U\cdot V \ge \|U\|\|V\| \ge 0$. Two future-pointing timelike vectors have a *positive*, large inner product. Why? Boost to the frame where $U$ is purely temporal, $U = (\|U\|,0,0,0)$. Then $V = (V^0,\mathbf{V})$ with $V^0 > |\mathbf{V}|$ (timelike, future-pointing), and $U\cdot V = \|U\|V^0$. Meanwhile $\|V\| = \sqrt{(V^0)^2-|\mathbf{V}|^2} \le V^0$. So $U\cdot V = \|U\|V^0 \ge \|U\|\|V\|$. The inner product *exceeds* the product of norms — the opposite of Cauchy–Schwarz — because the indefinite metric makes the temporal contribution $V^0$ dominate.

Now square the desired inequality. We want $\|U+V\|^2 \ge (\|U\|+\|V\|)^2$, i.e.
$$\|U\|^2 + 2\,U\cdot V + \|V\|^2 \ \ge\ \|U\|^2 + 2\|U\|\|V\| + \|V\|^2,$$
which reduces to exactly $U\cdot V \ge \|U\|\|V\|$ — the reversed Cauchy–Schwarz we just established. So the triangle inequality reverses *because* the Cauchy–Schwarz inequality reverses, and that reverses because the metric is indefinite and timelike vectors are dominated by their (large, positive) time components.

The proper-time reading makes the result physically unsurprising. Norm = elapsed clock time. A straight worldline "spends all its interval on time". A bent worldline spends part of its interval on spatial motion — and in Minkowski geometry, spatial motion *subtracts* from the interval (the minus signs). So a moving clock has less interval left over for time. Detour = motion = wasted interval = less proper time. The straight path, doing no spatial wandering, banks the maximum proper time.

---

# What Makes This Hard

The non-obvious step is the **reversed Cauchy–Schwarz** $U\cdot V \ge \|U\|\|V\|$ — it is the opposite of the Euclidean inequality, and the instinct to bound $U\cdot V$ *above* must be actively suppressed. The most common error is to import the ordinary triangle inequality unchanged, concluding the bent worldline is shorter and hence the *travelling* twin ages more — the exact reverse of the truth. A second pitfall is forgetting the future-pointing hypothesis: for two timelike vectors pointing into opposite halves of the cone, $U+V$ need not even be timelike, and the inequality has no content. The proof's one real idea is the frame choice — boost so $U$ is purely temporal — which makes the reversed Cauchy–Schwarz a one-line computation.

---

# Rederivation Scaffold

**High-level strategy:**
Square the inequality; it reduces to the reversed Cauchy–Schwarz $U\cdot V \ge \|U\|\|V\|$. Prove that by boosting to the frame where $U$ is purely temporal, where it becomes the elementary inequality $V^0 \ge \sqrt{(V^0)^2 - |\mathbf{V}|^2}$.

**Subgoal decomposition:**

1. **Show $U+V$ is future-pointing timelike.** So that $\|U+V\|$ is a real non-negative number and the inequality has meaning.
   - *Hint:* Boost so $U = (U^0,0,0,0)$; then $(U+V)\cdot(U+V) = (U^0+V^0)^2 - |\mathbf{V}|^2 > (V^0)^2 - |\mathbf{V}|^2 > 0$, and $U^0+V^0 > 0$.
   - *Why needed:* The inequality is between two non-negative reals only if $U+V$ is timelike.

2. **Reduce to reversed Cauchy–Schwarz.** Square both sides; cancel $\|U\|^2$ and $\|V\|^2$.
   - *Hint:* $\|U+V\|^2 = \|U\|^2 + 2U\cdot V + \|V\|^2$; the target $(\|U\|+\|V\|)^2$ differs only in the cross term.
   - *Why needed:* It isolates the single inequality that carries the whole theorem.

3. **Prove $U\cdot V \ge \|U\|\|V\|$.** In the frame where $U$ is purely temporal.
   - *Hint:* There $U\cdot V = U^0 V^0 = \|U\|V^0$, and $V^0 \ge \|V\|$ since $\|V\|^2 = (V^0)^2 - |\mathbf{V}|^2 \le (V^0)^2$.
   - *Why needed:* It is the reversed Cauchy–Schwarz, the crux.

4. **Equality case.** Trace when each step is tight.
   - *Hint:* $V^0 = \|V\|$ forces $\mathbf{V} = 0$, i.e. $V \parallel U$ in that frame, hence in all frames.
   - *Why needed:* Identifies that equality means no acceleration — the inertial worldline.

---

# Lemma Decomposition

> [!note]- Lemma 1: A future-pointing timelike vector can be boosted to be purely temporal
> **Statement:** If $U$ is future-pointing timelike, there is an inertial frame in which $U = (\|U\|, 0, 0, 0)$.
>
> **Hint:** $U$ is, up to scale, a four-velocity; boost to its rest frame.
>
> **Why needed:** It is the frame choice that turns the reversed Cauchy–Schwarz into a one-line inequality.
>
> > [!note]- Full proof
> > Write $U = (U^0,\mathbf{U})$ with $U^0 > 0$ and $(U^0)^2 > |\mathbf{U}|^2$. The vector $\mathbf{U}/U^0$ has magnitude $< 1$, so it is a physical velocity; perform the [[Def - The Lorentz Transformation|Lorentz boost]] with that velocity (composed with a rotation aligning $\mathbf{U}$ with the $x$-axis). A boost takes a four-vector to the frame moving with the corresponding velocity, where its spatial part vanishes: $U \to (\tilde U^0, 0,0,0)$. The norm is invariant, $(\tilde U^0)^2 = U\cdot U = \|U\|^2$, and $\tilde U^0 > 0$ since the time-orientation of a timelike vector is boost-invariant ([[Def - Classification of Four-Vectors]]). Hence $U = (\|U\|,0,0,0)$ in this frame. $\blacksquare$

> [!note]- Lemma 2: Reversed Cauchy–Schwarz for future-pointing timelike vectors
> **Statement:** If $U, V$ are future-pointing timelike, then $U\cdot V \ge \|U\|\,\|V\| > 0$, with equality iff $U \parallel V$.
>
> **Hint:** Boost $U$ to be purely temporal (Lemma 1), then compare $V^0$ with $\|V\|$.
>
> **Why needed:** It is the single inequality the whole theorem reduces to.
>
> > [!note]- Full proof
> > By Lemma 1, work in the frame where $U = (\|U\|,0,0,0)$. Write $V = (V^0,\mathbf{V})$; since $V$ is future-pointing timelike, $V^0 > 0$ and $(V^0)^2 > |\mathbf{V}|^2$. Then
> > $$U\cdot V = U^0 V^0 - \mathbf{U}\cdot\mathbf{V} = \|U\|\,V^0 - 0 = \|U\|\,V^0.$$
> > Now $\|V\|^2 = (V^0)^2 - |\mathbf{V}|^2 \le (V^0)^2$, and since $V^0 > 0$ and $\|V\| \ge 0$, this gives $V^0 \ge \|V\|$. Hence
> > $$U\cdot V = \|U\|\,V^0 \ge \|U\|\,\|V\| > 0.$$
> > Equality $V^0 = \|V\|$ holds iff $|\mathbf{V}| = 0$, i.e. $V = (V^0,0,0,0)$ is parallel to $U$ in this frame; parallelism is frame-independent, so equality iff $U \parallel V$. $\blacksquare$

> [!note]- Lemma 3: The sum of two future-pointing timelike vectors is future-pointing timelike
> **Statement:** If $U, V$ are future-pointing timelike, so is $U + V$.
>
> **Hint:** Use the frame of Lemma 1 and the reversed Cauchy–Schwarz.
>
> **Why needed:** It guarantees $\|U+V\| = \sqrt{(U+V)\cdot(U+V)}$ is a real non-negative number, so the inequality is between honest reals.
>
> > [!note]- Full proof
> > In the frame where $U = (\|U\|,0,0,0)$ and $V = (V^0,\mathbf{V})$ with $V^0 > |\mathbf{V}|$:
> > $$(U+V)\cdot(U+V) = (\|U\| + V^0)^2 - |\mathbf{V}|^2.$$
> > Since $\|U\| > 0$ and $V^0 > 0$, $(\|U\|+V^0)^2 > (V^0)^2 > |\mathbf{V}|^2$, so $(U+V)\cdot(U+V) > 0$ — timelike. The time component $\|U\| + V^0 > 0$ — future-pointing. (Equivalently, expand $(U+V)\cdot(U+V) = U\cdot U + 2U\cdot V + V\cdot V$; all three terms are positive, the middle by Lemma 2.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U, V$ be future-pointing timelike four-vectors, so $\|U\| = \sqrt{U\cdot U}$ and $\|V\| = \sqrt{V\cdot V}$ are positive reals.
>
> By Lemma 3, $U+V$ is future-pointing timelike, so $(U+V)\cdot(U+V) > 0$ and $\|U+V\| = \sqrt{(U+V)\cdot(U+V)}$ is a well-defined positive real. Both sides of the claimed inequality are therefore non-negative reals, and it suffices to prove the squared inequality.
>
> Expand, using bilinearity of the inner product:
> $$\|U+V\|^2 = (U+V)\cdot(U+V) = U\cdot U + 2\,U\cdot V + V\cdot V = \|U\|^2 + 2\,U\cdot V + \|V\|^2.$$
> The target $(\|U\|+\|V\|)^2 = \|U\|^2 + 2\|U\|\|V\| + \|V\|^2$. Subtracting, the inequality $\|U+V\|^2 \ge (\|U\|+\|V\|)^2$ is equivalent to
> $$U\cdot V \ \ge\ \|U\|\,\|V\|.$$
> This is exactly Lemma 2 (the reversed Cauchy–Schwarz). Hence $\|U+V\|^2 \ge (\|U\|+\|V\|)^2$, and taking the (non-negative) square root,
> $$\|U+V\| \ge \|U\| + \|V\|.$$
> **Equality.** Equality in the final inequality holds iff equality holds in Lemma 2, which by that lemma's proof occurs iff $U$ and $V$ are parallel. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The twin paradox as a triangle.** Model the travelling twin's journey as two timelike four-vectors $U$ (outbound leg) and $V$ (return leg), and the stay-at-home twin's worldline as the single timelike vector $U+V$ (their endpoints coincide). The theorem says $\|U+V\| \ge \|U\| + \|V\|$ — the stay-at-home twin's proper time exceeds the traveller's. The whole paradox is one application of the theorem; see [[Ex - The twin paradox]]. The application is nonobvious because the paradox is usually argued with time-dilation formulas, whereas it is a single geometric inequality.

**Invariant mass exceeds the sum of rest masses.** For two massive particles with four-momenta $P_1, P_2$ (future-pointing timelike), the total $P = P_1 + P_2$ has invariant mass $M = \|P\| \ge \|P_1\| + \|P_2\| = m_1 + m_2$. The system is heavier than its parts, the excess being kinetic energy of relative motion; equality holds iff the particles are mutually at rest. The application is out-of-distribution because "mass is not additive" sounds like a dynamical fact, yet it is the reversed triangle inequality; see [[Ex - The invariant mass of a system of particles]].

**The free-particle action.** The relativistic action of a free massive particle is $S = -m\int d\tau$, the proper time along its worldline (up to the constant $-m$). The theorem, iterated to the continuum, says proper time is *maximised* by the straight worldline, so the free particle's actual path *minimises* $S$ — Hamilton's principle. The application is surprising because it shows the reversed triangle inequality *is* the variational principle of relativistic mechanics.

---

# Bridges

- **The Euclidean triangle inequality** — the direct foil. $|\mathbf{u}+\mathbf{v}| \le |\mathbf{u}|+|\mathbf{v}|$ rests on Cauchy–Schwarz, which needs a positive-definite inner product; the Minkowski inner product is indefinite, Cauchy–Schwarz reverses on the timelike cone, and so does the triangle inequality.

- **[[Def - Classification of Four-Vectors]]** — the theorem lives entirely on the future-pointing timelike cone, and shows that cone is *convex* (closed under addition) — a fact the classification does not by itself give.

- **[[Thm - Invariance of the Spacetime Interval]]** — the norm $\|U\|$ is the interval, invariant; the theorem is a statement *about* that invariant, the way the Euclidean triangle inequality is a statement about Euclidean distance.

- **The geodesic principle of general relativity** — "straight worldline maximises proper time" generalises to "freely-falling worldlines extremise proper time among timelike curves", the relativistic replacement for Newton's first law.

---

# Unlocked by This

> [!tip] The Twin Paradox Resolved Geometrically *(from §1.3)*
> The theorem says the inertial worldline has the longest proper time, so the stay-at-home twin ages more — no time-dilation bookkeeping required ([[Ex - The twin paradox]]). The asymmetry is geometric: one worldline is straight, the other bent.

> [!tip] The Action Principle for a Relativistic Particle *(from Relativistic Dynamics and Field Theory)*
> Since proper time is maximised by the straight worldline, the free-particle **action** $S = -m\int d\tau$ is extremised by inertial motion. This is the relativistic Hamilton's principle, and the starting point for the Lagrangian formulation of relativistic mechanics and field theory.
