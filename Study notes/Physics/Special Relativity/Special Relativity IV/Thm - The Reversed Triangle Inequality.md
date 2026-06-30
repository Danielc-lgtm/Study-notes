---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Invariance of the Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. The metric is $\eta = \mathrm{diag}(1,-1,-1,-1)$ and $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu = X^0Y^0 - \mathbf{X}\cdot\mathbf{Y}$, where $\mathbf{X}$ is the spatial part of $X$. A four-vector $X$ is **timelike** if $X\cdot X > 0$, **future-pointing** if in addition $X^0 > 0$ (see [[Def - Classification of Four-Vectors]]). For a timelike $X$ the **Minkowski norm** is $\|X\| = \sqrt{X\cdot X} \ge 0$. The spatial Euclidean norm is written $|\mathbf{X}|$. Full registry on [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group]].

---

# Statement

> **Reversed triangle inequality (timelike vectors).** Let $U$ and $V$ be future-pointing timelike four-vectors. Then $U + V$ is again future-pointing timelike, and
> $$\|U + V\| \;\ge\; \|U\| + \|V\|,$$
> where $\|X\| = \sqrt{X\cdot X}$ is the Minkowski norm. Equality holds if and only if $U$ and $V$ are parallel ($U = \lambda V$ for some $\lambda > 0$).

> **Corollary (longest-worldline / wrong-way triangle).** Among all timelike worldlines joining two timelike-separated events, the straight (inertial, unaccelerated) one has the *greatest* [[Def - Proper Time|proper time]]; every bent worldline accumulates strictly less. The triangle inequality of Euclidean geometry is reversed: in Minkowski space the straight path is the longest, not the shortest.

---

# Motivation

In Euclidean geometry the triangle inequality $|\mathbf{a} + \mathbf{b}| \le |\mathbf{a}| + |\mathbf{b}|$ is the statement that a straight line is the shortest path: a detour is always longer. It is so basic that one expects some version of it to hold in any geometry. The motivation for this theorem is to discover what the triangle inequality becomes when the Euclidean metric is replaced by the indefinite [[Def - Minkowski Space and the Metric|Minkowski metric]] — and the answer is a genuine surprise: the inequality *reverses*. In Minkowski space, for timelike vectors, the sum is *longer* than the sum of the parts, and the straight worldline is the *longest*, not the shortest.

This is not a curiosity. It is the geometric heart of the twin paradox and the seed of the geodesic principle of general relativity. The travelling twin, whose worldline is bent at the turnaround, ages *less* than the stay-at-home twin, whose worldline is straight — and the precise reason is that a bent timelike worldline has less Minkowski length (less proper time) than the straight one between the same two events. The theorem makes "the straight worldline is the longest" a rigorous inequality, and it explains the twin paradox without any appeal to who feels acceleration: the asymmetry is geometric, written into the metric.

One should *expect* the reversal once one takes the indefiniteness of $\eta$ seriously. The ordinary triangle inequality rests on the Cauchy–Schwarz inequality $|\mathbf{a}\cdot\mathbf{b}| \le |\mathbf{a}||\mathbf{b}|$, which holds because the Euclidean form is positive definite. For the Minkowski inner product of two future-pointing timelike vectors the analogue is *reversed* — $U\cdot V \ge \|U\|\|V\|$, a "wrong-way Cauchy–Schwarz" — because the geometry of the forward light cone makes the time components dominate. Feeding the reversed Cauchy–Schwarz through the same algebra that produces the ordinary triangle inequality produces the reversed triangle inequality. The whole phenomenon traces to one sign in the metric.

The restriction to *future-pointing timelike* vectors is essential and worth flagging. For spacelike vectors, or for timelike vectors pointing into opposite light cones, neither inequality holds in a clean form — the reversal is special to vectors that both lie in the (convex) forward cone. Convexity of the forward cone is exactly the ingredient that makes "$U + V$ is timelike" and the inequality work, and it is why the theorem is about worldlines (which are forward-timelike) and not about arbitrary separations.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$U$ and $V$ are future-pointing timelike four-vectors". The disguises:

The first disguised source is **"$U$ and $V$ are the displacement four-vectors of two inertial worldline segments"**. Any unaccelerated segment of a massive particle's history is a future-pointing timelike vector (it moves slower than light, forward in time). So whenever a worldline is broken into straight pieces — most importantly the two legs of the twin's journey — each piece is an admissible $U$ or $V$, and the theorem compares the bent path to the straight one. The bridge is that a timelike worldline segment *is* a future-pointing timelike vector. *Example problem:* the two legs of the travelling twin, $U = (T, vT, 0, 0)$ and $V = (T, -vT, 0, 0)$, with $U + V = (2T, 0, 0, 0)$ the stay-at-home twin's displacement.

The second disguised source is **"$U$ and $V$ are four-velocities or four-momenta"**. A [[Def - Four-Velocity and Four-Acceleration|four-velocity]] has $V\cdot V = 1 > 0$ and $V^0 = \gamma > 0$, so it is future-pointing timelike; a massive particle's [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mV$ likewise. The theorem then applies to *sums* of four-momenta. The bridge is the normalisation $V\cdot V = 1$ (or $P\cdot P = m^2 > 0$). *Example problem:* the total four-momentum of several massive particles is future-pointing timelike, so the system's invariant mass $M = \|P_{\text{total}}\|$ satisfies $M \ge \sum_i m_i$ — a bound on the rest energy of a composite, with equality only if all particles are mutually at rest.

The third disguised source is **"a chain of timelike steps along any worldline"**. An arbitrary timelike worldline is a limit of polygonal worldlines made of many small future-pointing timelike steps $dX$. Applying the inequality to each pair and inducting shows the polygon's total Minkowski length is at most that of the straight chord. The bridge is that the integral $\int \|dX\| = \int\sqrt{ds^2}$ is the proper time, and the inequality bounds it. *Example problem:* prove that *any* accelerated worldline between two events has proper time strictly less than the inertial one ([[Ex - The reversed triangle inequality and the longest worldline]]).

**Targets (Output Amplification)**

The conclusion is "$\|U + V\| \ge \|U\| + \|V\|$".

Combine the conclusion with **iteration over many segments**. Applying the inequality repeatedly to a polygonal worldline gives that the straight chord is longer than any inscribed timelike polygon, and passing to the continuum limit gives that the inertial worldline maximises proper time among *all* timelike worldlines between two events. The further result is the **clock postulate / longest-worldline principle**. The combination is useful because it upgrades a two-vector statement to a statement about arbitrary curves. *Example:* the resolution of the twin paradox without acceleration bookkeeping.

Combine the conclusion with **the equality condition**. Equality holds *only* for parallel $U, V$ — that is, only when the worldline does not actually bend. The further result is that *any* genuine acceleration (any change of direction in spacetime) costs proper time strictly: the inequality is strict for a real detour. The combination is nonobvious because it turns "the straight path is longest" into "every detour is strictly shorter, with the deficit measuring the bending". *Example:* the missing proper time of the travelling twin is strictly positive and increases with the turnaround speed.

Combine the conclusion with **the invariant-mass interpretation**. Reading $U, V$ as four-momenta, $\|U + V\| \ge \|U\| + \|V\|$ becomes $M_{\text{system}} \ge m_1 + m_2$: the invariant mass of a system of particles is at least the sum of their rest masses, the excess being the kinetic and binding energy in the centre-of-momentum frame. The combination is useful because it converts a geometric inequality into a thermodynamic-flavoured bound on composite masses. *Example:* the threshold energy for an endothermic reaction or for pair production is set by this inequality.

---

# Why Is It True

The reversal is the shadow of one sign in the metric, and the cleanest way to see it is to compute in the rest frame of one of the vectors.

**The mechanism in one line: the forward light cone is convex and "time dominates", so adding two forward-timelike vectors makes the time parts reinforce while the space parts can only partially cancel — and since norm is built as time-squared *minus* space-squared, more reinforced time and less net space both push the norm up.**

Take it slowly. By Lorentz invariance ([[Thm - Invariance of the Spacetime Interval]]) we may evaluate everything in the rest frame of $U$, where $U = (\|U\|, 0, 0, 0)$ — all its length is in the time component. In that frame $V = (V^0, \mathbf{V})$ with $V^0 > 0$ and $\|V\|^2 = (V^0)^2 - |\mathbf{V}|^2 > 0$, so $V^0 > |\mathbf{V}| \ge 0$: a future-timelike vector has its time component bigger than its space component. Now
$$
U \cdot V = \|U\|\,V^0 > \|U\|\,|\mathbf{V}| \ge 0,
$$
and in particular $U\cdot V > 0$. Compare with the Euclidean Cauchy–Schwarz that would bound $U\cdot V$ from *above*: here, because of the minus sign in the metric, $U\cdot V = \|U\|V^0 \ge \|U\|\sqrt{(V^0)^2 - |\mathbf{V}|^2} = \|U\|\|V\|$ — the inequality runs the *other way*, $U\cdot V \ge \|U\|\|V\|$. This is the reversed Cauchy–Schwarz, and it is the whole engine.

With the reversed Cauchy–Schwarz in hand, expand the norm of the sum:
$$
\|U+V\|^2 = (U+V)\cdot(U+V) = U\cdot U + 2\,U\cdot V + V\cdot V = \|U\|^2 + 2\,U\cdot V + \|V\|^2 \ge \|U\|^2 + 2\|U\|\|V\| + \|V\|^2 = (\|U\| + \|V\|)^2.
$$
Taking square roots (both sides non-negative) gives $\|U+V\| \ge \|U\| + \|V\|$. The single step where this differs from the Euclidean derivation is the direction of the Cauchy–Schwarz inequality: in Euclidean space $2\mathbf{a}\cdot\mathbf{b} \le 2|\mathbf{a}||\mathbf{b}|$ makes $|\mathbf{a}+\mathbf{b}|^2 \le (|\mathbf{a}|+|\mathbf{b}|)^2$; here $2U\cdot V \ge 2\|U\|\|V\|$ makes $\|U+V\|^2 \ge (\|U\|+\|V\|)^2$. One sign flip in the metric flips one inequality, and the triangle inequality reverses.

Geometrically: the forward light cone is a convex cone, so $U + V$ stays inside it (future-timelike), and inside the forward cone the Minkowski norm behaves "concavely" — the straight diagonal of the parallelogram is longer than the two sides, the exact opposite of the Euclidean parallelogram where the diagonal is shorter than the sum of the sides. The proper-time clock runs *fastest* along the vector that is "most purely timelike", i.e. straight up the cone; any tilt into space (any spatial velocity) subtracts from the norm because space enters with a minus sign.

---

# What Makes This Hard

The proof is short, but two steps trip people up. The first is the direction of the Cauchy–Schwarz inequality: Euclidean instinct says $U\cdot V \le \|U\|\|V\|$, and the entire theorem hinges on recognising that for forward-timelike vectors it is *reversed*, $U\cdot V \ge \|U\|\|V\|$ — getting this backwards "proves" the ordinary (false) triangle inequality. The second is the temptation to take square roots of $\|U+V\|^2 \ge (\|U\|+\|V\|)^2$ without first checking both sides are non-negative and that $U+V$ is genuinely timelike (so $\|U+V\|$ is real); the convexity of the forward cone, which guarantees $U+V$ is future-timelike, is the step that is easy to skip but logically required.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Establish the reversed Cauchy–Schwarz $U\cdot V \ge \|U\|\|V\|$ for future-timelike $U, V$ by evaluating in the rest frame of $U$ (Lorentz invariance lets you). Then expand $\|U+V\|^2 = \|U\|^2 + 2U\cdot V + \|V\|^2$ and bound the middle term below, completing the square. Check $U+V$ is future-timelike so the square root is legitimate.

**Subgoal decomposition:**

1. **Show $U + V$ is future-pointing timelike.** Use the convexity of the forward light cone.
   - *Hint:* In the rest frame of $U$, write $V = (V^0, \mathbf{V})$ with $V^0 > |\mathbf{V}|$; then $(U+V)^0 = \|U\| + V^0 > 0$ and $(U+V)\cdot(U+V) > 0$ follows from the reversed Cauchy–Schwarz.
   - *Why needed:* It guarantees $\|U+V\|$ is real, so the final square root makes sense.

2. **Prove the reversed Cauchy–Schwarz $U\cdot V \ge \|U\|\|V\|$.** Evaluate in the rest frame of $U$.
   - *Hint:* There $U\cdot V = \|U\|V^0$ and $\|V\| = \sqrt{(V^0)^2 - |\mathbf{V}|^2} \le V^0$, so $U\cdot V = \|U\|V^0 \ge \|U\|\|V\|$.
   - *Why needed:* It is the reversed engine that flips the triangle inequality.

3. **Complete the square.** Expand $\|U+V\|^2$ and use step 2.
   - *Hint:* $\|U+V\|^2 = \|U\|^2 + 2U\cdot V + \|V\|^2 \ge \|U\|^2 + 2\|U\|\|V\| + \|V\|^2 = (\|U\|+\|V\|)^2$.
   - *Why needed:* It is the algebra that turns the reversed Cauchy–Schwarz into the reversed triangle inequality.

4. **Identify the equality case.** Track when step 2 is an equality.
   - *Hint:* $V^0 = \|V\|$ forces $\mathbf{V} = 0$ in $U$'s rest frame, i.e. $V \parallel U$.
   - *Why needed:* It shows every genuine bend is a strict loss of proper time.

---

# Lemma Decomposition

> [!note]- Lemma 1: Reversed Cauchy–Schwarz for future-timelike vectors
> **Statement:** For future-pointing timelike $U, V$, one has $U\cdot V \ge \|U\|\,\|V\| > 0$, with equality iff $U \parallel V$.
>
> **Hint:** Evaluate in the rest frame of $U$, where $U = (\|U\|, \mathbf{0})$.
>
> **Why needed:** It is the reversed inequality that, fed through the completing-the-square algebra, produces the reversed triangle inequality; it is the single place the metric's minus sign acts.
>
> > [!note]- Full proof
> > By [[Thm - Invariance of the Spacetime Interval|Lorentz invariance]] the inner products $U\cdot V$, $\|U\|$, $\|V\|$ are unchanged by a boost, so evaluate in the rest frame of $U$, where $U = (\|U\|, 0, 0, 0)$. Write $V = (V^0, \mathbf{V})$. Since $V$ is future-timelike, $(V^0)^2 - |\mathbf{V}|^2 = \|V\|^2 > 0$ and $V^0 > 0$, hence $V^0 = \sqrt{\|V\|^2 + |\mathbf{V}|^2} \ge \|V\|$. Therefore
> > $$U\cdot V = \|U\|\,V^0 - \mathbf{0}\cdot\mathbf{V} = \|U\|\,V^0 \ge \|U\|\,\|V\| > 0.$$
> > Equality $V^0 = \|V\|$ forces $|\mathbf{V}| = 0$, i.e. $V$ is at rest in $U$'s frame, i.e. $V$ is parallel to $U$ (both purely timelike there). $\blacksquare$

> [!note]- Lemma 2: The sum of two future-timelike vectors is future-timelike
> **Statement:** If $U, V$ are future-pointing timelike then so is $U + V$.
>
> **Hint:** The time component is manifestly positive; for timelikeness expand $(U+V)\cdot(U+V)$ and use Lemma 1.
>
> **Why needed:** Without it, $\|U+V\| = \sqrt{(U+V)\cdot(U+V)}$ might be imaginary and the theorem's statement would be meaningless.
>
> > [!note]- Full proof
> > In the rest frame of $U$ (or any frame), $(U+V)^0 = U^0 + V^0 > 0$ since both summands have positive time component. For timelikeness,
> > $$(U+V)\cdot(U+V) = \|U\|^2 + 2\,U\cdot V + \|V\|^2 > 0,$$
> > because $\|U\|^2 > 0$, $\|V\|^2 > 0$, and $U\cdot V > 0$ by Lemma 1. So $U+V$ is timelike with positive time component, i.e. future-pointing timelike. (Geometrically: the forward light cone is convex, being $\{X : X^0 > |\mathbf{X}|\}$, a convex set, so it is closed under addition.) $\blacksquare$

> [!note]- Lemma 3: Completing the square
> **Statement:** $\|U+V\|^2 \ge (\|U\| + \|V\|)^2$, hence $\|U+V\| \ge \|U\| + \|V\|$.
>
> **Hint:** Expand the left side and bound the cross term below using Lemma 1.
>
> **Why needed:** It is the final algebraic step; combined with Lemma 2 (which makes the square root real) it is the theorem.
>
> > [!note]- Full proof
> > By Lemma 2, $U+V$ is future-timelike, so $\|U+V\| = \sqrt{(U+V)\cdot(U+V)}$ is real and non-negative. Expand:
> > $$\|U+V\|^2 = (U+V)\cdot(U+V) = U\cdot U + 2\,U\cdot V + V\cdot V = \|U\|^2 + 2\,U\cdot V + \|V\|^2.$$
> > By Lemma 1, $U\cdot V \ge \|U\|\|V\|$, so
> > $$\|U+V\|^2 \ge \|U\|^2 + 2\|U\|\|V\| + \|V\|^2 = (\|U\| + \|V\|)^2.$$
> > Both $\|U+V\|$ and $\|U\|+\|V\|$ are non-negative, so taking square roots preserves the inequality: $\|U+V\| \ge \|U\| + \|V\|$. Equality holds iff Lemma 1 is an equality, i.e. iff $U \parallel V$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U, V$ be future-pointing timelike four-vectors.
>
> *Step 0 — well-posedness.* By Lemma 2, $U+V$ is future-pointing timelike, so $(U+V)\cdot(U+V) > 0$ and $\|U+V\| = \sqrt{(U+V)\cdot(U+V)}$ is a well-defined non-negative real number. Likewise $\|U\|, \|V\| > 0$.
>
> *Reversed Cauchy–Schwarz.* By Lemma 1, evaluating in the rest frame of $U$, we have $U\cdot V \ge \|U\|\,\|V\|$, with equality iff $U \parallel V$. The direction of this inequality is opposite to the Euclidean Cauchy–Schwarz, and it is the consequence of the indefinite signature: in $U$'s rest frame $U\cdot V = \|U\|V^0$ and $V^0 \ge \|V\|$ because a future-timelike vector's time component dominates its norm.
>
> *Completing the square.* By Lemma 3,
> $$\|U+V\|^2 = \|U\|^2 + 2\,U\cdot V + \|V\|^2 \ge \|U\|^2 + 2\|U\|\|V\| + \|V\|^2 = (\|U\| + \|V\|)^2,$$
> and taking non-negative square roots,
> $$\|U+V\| \ge \|U\| + \|V\|,$$
> with equality iff $U \parallel V$.
>
> *Corollary (longest worldline).* Apply the inequality to the two legs of a worldline broken at one point, then inductively to a worldline broken into $N$ future-timelike segments $U_1, \dots, U_N$: $\big\|\sum_k U_k\big\| \ge \sum_k \|U_k\|$. The left side is the Minkowski length of the straight chord $\sum_k U_k$ from the first event to the last; the right side is the total length of the polygonal (bent) worldline. Passing to the continuum, the inertial worldline's [[Def - Proper Time|proper time]] $\|\,\Delta X\,\|$ exceeds the proper time $\int\sqrt{ds^2}$ of any other timelike worldline between the same two events, strictly unless the worldline is straight. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Invariant mass of a composite system.** Read $U, V$ as the [[Def - Four-Momentum and Rest Mass|four-momenta]] of two massive particles. Then $\|U+V\| \ge \|U\| + \|V\|$ says the invariant mass $M = \|P_1 + P_2\|$ of the pair is at least $m_1 + m_2$, the excess being the kinetic energy available in the centre-of-momentum frame. This sets reaction thresholds: to create a particle of mass $M$ you need total invariant mass $\ge M$. The application is nonobvious because a statement about "the length of a sum of vectors" is secretly a statement about energy thresholds in particle physics.

**Information geometry and the data-processing flavour.** In Minkowski-like indefinite geometries that appear in information theory (e.g. the light-cone structure of the space of probability distributions under certain divergences), reversed triangle inequalities control how "distinguishability" accumulates along a chain. The structural analogy is that an indefinite quadratic form reverses the usual subadditivity into superadditivity. The application is surprising because the same sign-flip mechanism that governs proper time governs accumulation of a quantity along a path in an unrelated field.

**Comparison geometry and the Lorentzian splitting theorem.** In Lorentzian geometry (the curved generalisation), the reversed triangle inequality becomes the statement that timelike geodesics *locally maximise* proper time, and global versions feed into singularity theorems and the Lorentzian splitting theorem of general relativity. The application is the deepest: the local inequality proved here is the linearised seed of the global causal-structure theorems that constrain the geometry of spacetime itself.

---

# Bridges

- **Euclidean triangle inequality** — this theorem is its exact mirror image. The Euclidean inequality $|\mathbf{a}+\mathbf{b}| \le |\mathbf{a}|+|\mathbf{b}|$ comes from $\mathbf{a}\cdot\mathbf{b} \le |\mathbf{a}||\mathbf{b}|$ (ordinary Cauchy–Schwarz); the Minkowski version reverses both the Cauchy–Schwarz and the triangle inequality, $U\cdot V \ge \|U\|\|V\|$ giving $\|U+V\| \ge \|U\|+\|V\|$. The single difference is the sign of the metric, and the parallelism of the two proofs (complete the square after Cauchy–Schwarz) makes the reversal transparent. In Euclidean space the diagonal of a parallelogram is shorter than the sum of the sides; in the forward cone of Minkowski space it is longer.

- **[[Thm - Invariance of the Spacetime Interval]]** — the proof uses interval invariance to pass to the rest frame of $U$, where the computation is trivial. This is the "evaluate the invariant in the convenient frame" move: the inequality is a statement about Lorentz-invariant quantities ($U\cdot V$, $\|U\|$, $\|V\|$), so proving it in one frame proves it in all. The reversed triangle inequality is a theorem *about* the geometry that the interval-invariance theorem establishes.

- **[[Def - Classification of Four-Vectors]]** — the theorem lives entirely in the future timelike cone, the set $\{X : X\cdot X > 0,\ X^0 > 0\}$, and its convexity (that the cone is closed under addition) is what makes $U+V$ admissible. The classification into timelike/spacelike/null is the prerequisite vocabulary; the theorem is a statement about the convex geometry of one of those three classes.

- **[[Def - Proper Time]]** and the geodesic principle — the corollary "straight worldlines are longest in proper time" is the special-relativistic statement that inertial motion *extremises* (maximises) proper time. In general relativity this becomes the geodesic principle: freely-falling worldlines are the timelike geodesics, the curves of locally maximal proper time. The reversed triangle inequality is the flat-spacetime seed of "free fall maximises ageing", and the twin paradox is its simplest instance.

---

# Unlocked by This

> [!tip] The Twin Paradox as Geometry *(from Relativistic Kinematics)*
> The corollary resolves the twin paradox with no appeal to acceleration bookkeeping: the stay-at-home twin's worldline is straight, the traveller's is bent, and by the reversed triangle inequality the straight one accumulates more [[Def - Proper Time|proper time]]. The traveller returns younger because a bent timelike worldline is *shorter* in proper time, full stop. The worked computation, including the simultaneity sweep at the turnaround, is [[Ex - The reversed triangle inequality and the longest worldline]] and is taken up again in [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

> [!tip] The Geodesic Principle and Lorentzian Comparison Geometry *(from General Relativity)*
> The local statement "inertial worldlines maximise proper time" generalises to curved spacetime as the **geodesic principle**: a freely-falling test body follows a timelike geodesic, a curve of locally extremal proper time. The reversed triangle inequality is the linearised, flat-spacetime version, and its global Lorentzian analogues (the timelike comparison theorems) are technical ingredients in the **singularity theorems** of Hawking and Penrose. The convexity of the light cone used in the proof is the local form of the causal-structure hypotheses those theorems require.
