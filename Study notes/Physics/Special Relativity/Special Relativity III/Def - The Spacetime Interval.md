---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Two events $P, Q$ have coordinates $p^\mu, q^\mu = (t,x,y,z)$ in an inertial frame, $\mu = 0,1,2,3$, with $x^0 = t$. Their **separation** is the displacement four-vector $\overrightarrow{PQ}$ with components $\Delta x^\mu = q^\mu - p^\mu = (\Delta t, \Delta x, \Delta y, \Delta z)$. The **Minkowski metric** is $\eta = \mathrm{diag}(1,-1,-1,-1)$. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

> [!warning] Convention: signature
> We use **"mostly minus"**, $\eta = \mathrm{diag}(1,-1,-1,-1)$, so $\Delta s^2 = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ and a **timelike** separation has $\Delta s^2 > 0$. Tong uses this convention; Gourgoulhon uses the opposite sign, $\Delta s^2 = -\Delta t^2 + \Delta x^2 + \cdots$, with timelike $\Delta s^2 < 0$. Flip the overall sign to translate.

---

# Axiom Motivation

The earlier chapters dismantled the Newtonian absolutes: the elapsed time $\Delta t$ between two events and the spatial distance between them are now frame-dependent, different for different observers. Tong frames the question that the interval answers — "we have seen that time is relative, length is relative, simultaneity is relative; is nothing sacred? The answer is yes: there is one measurement all observers agree on." The interval is the construction of that one measurement.

What should it be? We want a quantity built from the separation $(\Delta t, \Delta x, \Delta y, \Delta z)$ that every inertial observer assigns the same value. The Euclidean guess, $\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$, fails: a boost changes it. The right combination is forced by the one physical input, the constancy of light. A light ray has $\Delta x = \Delta t$ in any frame (it moves at $c = 1$), so $\Delta t^2 - \Delta x^2 = 0$ in every frame; any invariant we build must vanish on light rays in all frames. The quadratic form whose zero set is the light cone $\Delta t = \pm|\Delta\mathbf{x}|$ is $\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$, up to an overall scale, and the relativity principle fixes the scale to $1$. The result is the **interval**, the scalar square of the separation under the [[Def - Minkowski Space and the Metric|Minkowski metric]].

The decisive design feature is the sign pattern: time enters with the opposite sign to space. This is not a cosmetic choice — it is what makes the interval invariant rather than the Euclidean distance, and it is what gives the interval its strangest property, that it is *not positive definite*. A genuine distance vanishes only between coincident points; the interval can vanish between *distinct* events (those on a common light ray) and can be negative (spacelike separation). One must resist the urge to "fix" this by taking absolute values or squaring differently: the indefiniteness is the physical content, the thing that encodes causal structure, and a positive-definite replacement would describe four-dimensional Euclidean space, where nothing relativistic happens.

Why a *quadratic* combination rather than, say, a linear one? Because a linear combination $a\Delta t + b\cdot\Delta\mathbf{x}$ is invariant only if it is trivial, whereas a quadratic form has a rich isometry group — the Lorentz group — under which it is preserved while its individual terms are scrambled. The interval is to the Lorentz group what the squared distance is to the rotation group: the quadratic invariant that *defines* the group as its symmetries. This is why the interval, not any of its pieces, is the foundation of the geometric viewpoint.

---

# The Definition

Let $P$ and $Q$ be two events with separation $(\Delta t, \Delta x, \Delta y, \Delta z)$ in an inertial frame. The **spacetime interval** between them is the scalar square of their separation four-vector under the [[Def - Minkowski Space and the Metric|Minkowski metric]]:
$$
\Delta s^2 \;:=\; g(\overrightarrow{PQ}, \overrightarrow{PQ}) \;=\; \eta_{\mu\nu}\,\Delta x^\mu \Delta x^\nu \;=\; \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2.
$$
With $c$ restored, $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$. The notation $\Delta s^2$ is a single symbol; despite the square it can be negative.

For two infinitesimally close events the interval is the **line element**
$$
ds^2 = dt^2 - dx^2 - dy^2 - dz^2 = \eta_{\mu\nu}\,dx^\mu dx^\nu,
$$
the form in which the metric is written in differential geometry.

The interval classifies the separation:
- **timelike** if $\Delta s^2 > 0$: $P$ and $Q$ are closer in space than in time, can be joined by a sub-light worldline, lie within each other's light cones;
- **spacelike** if $\Delta s^2 < 0$: closer in time than in space, no signal can join them, lie outside each other's light cones (and $\sqrt{\Delta s^2}$ is imaginary, though $\Delta s^2$ itself is a perfectly good real number);
- **null** (lightlike) if $\Delta s^2 = 0$ with $P \neq Q$: joined by a light ray.

By the [[Thm - Invariance of the Spacetime Interval|invariance theorem]], $\Delta s^2$ takes the same value in every inertial frame. By Gourgoulhon's Remark 1.6, $d(P,Q) = \sqrt{g(\overrightarrow{PQ},\overrightarrow{PQ})}$ is *not* a distance in the topologist's sense — it vanishes for distinct null-separated events and is imaginary for spacelike separation — which is why $\mathbb{M}$ is a pseudo-metric space, not a metric space.

---

# Relate to Other Fields / Compression

The interval is the **quadratic form of the Minkowski metric**, and the entire content of "the interval is invariant" is "the Lorentz group preserves this quadratic form" — exactly parallel to the Euclidean statement "the rotation group preserves $x^2 + y^2 + z^2$". In the language of bilinear forms, $\Delta s^2 = g(X,X)$ where $X = \overrightarrow{PQ}$, so the interval is the diagonal restriction of the [[Def - Minkowski Space and the Metric|metric]], and by polarisation the full bilinear form is recoverable from it: $g(X,Y) = \tfrac12[(X+Y)\cdot(X+Y) - X\cdot X - Y\cdot Y]$.

This is the analogue of squared Euclidean distance with the signature changed from $(n,0)$ to $(1,3)$: the same construction — a quadratic form on a vector space, invariant under the form's isometry group — with indefiniteness substituted for positive-definiteness. Everything strange about the interval (zero distance between distinct points, imaginary distances, reversed inequalities) is the price and the payoff of that one sign change.

**True name:** the interval is *the scalar square of the separation under $η$* — $\Delta s^2 = X\cdot X$ for $X = \overrightarrow{PQ}$. The operational content is that any invariant you want to build is, at bottom, a scalar product of four-vectors, computable in whichever frame is most convenient; the interval is the prototype, the case where the two four-vectors coincide.

---

# Examples / Corollaries

**Is an instance — the proper time of a clock.** Two ticks of a clock at rest happen at the same place, $\Delta\mathbf{x} = 0$, so $\Delta s^2 = \Delta t^2 > 0$ is timelike and $\sqrt{\Delta s^2} = \Delta t$ is the time the clock reads. The interval *is* the proper time for timelike separations: a frame-independent elapsed time, computed most easily in the rest frame where the spatial part vanishes.

**Is an instance — a light pulse.** A pulse emitted at $P = (0,0,0,0)$ and absorbed at $Q = (1,1,0,0)$ has $\Delta s^2 = 1 - 1 = 0$: null. The two events are distinct yet separated by zero interval — the signature of lightlike separation, impossible in a Euclidean space.

**Is NOT an instance — the Euclidean distance.** The quantity $\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$ is *not* the interval and is *not* invariant: a boost along $x$ sends $(\Delta t, \Delta x) \mapsto (\gamma(\Delta t - v\Delta x), \gamma(\Delta x - v\Delta t))$, and $\Delta t^2 + \Delta x^2$ changes, whereas $\Delta t^2 - \Delta x^2$ does not. The sign is the whole difference.

**Corollary — the interval can be zero for distinct events.** Any two events on a common light ray have $\Delta s^2 = 0$, so the interval fails the defining property of a metric ($d(P,Q) = 0 \Rightarrow P = Q$). This is the calibration check for understanding indefiniteness, and the reason $\mathbb{M}$ carries a *pseudo*-metric.

**Corollary — the sign is Lorentz invariant.** Since $\Delta s^2$ itself is invariant, so is its sign, and the sign is the [[Def - Classification of Four-Vectors|causal classification]]. All observers agree on whether two events are timelike, spacelike, or null separated, even though they disagree on $\Delta t$ and $|\Delta\mathbf{x}|$ separately.

**Calibration check.** If you have understood the definition you can: (i) compute the interval between $(0,0,0,0)$ and $(3,1,2,2)$ as $9 - 1 - 4 - 4 = 0$ and conclude they are null-separated; (ii) explain why $\Delta s^2 = 0$ does not force the events to coincide; (iii) state which frame makes the interval easiest to evaluate for a timelike separation (the rest frame, where $\Delta\mathbf{x} = 0$ and $\Delta s^2 = \Delta t^2$).

---

# Unlocked by This

> [!tip] Proper Time *(from Relativistic Kinematics)*
> The interval along a particle's worldline, integrated, gives the **proper time** — the time read by a clock carried along that worldline; see [[Def - Proper Time]] in [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]]. This is the parameter with respect to which four-velocity and four-acceleration are defined, and the invariance of the interval is exactly what makes proper time a genuine, observer-independent quantity.

> [!tip] The Line Element of General Relativity *(from General Relativity)*
> In a curved spacetime the constant line element $ds^2 = \eta_{\mu\nu}dx^\mu dx^\nu$ is replaced by $ds^2 = g_{\mu\nu}(x)\,dx^\mu dx^\nu$ with a position-dependent metric — the form in which the gravitational field is encoded. The interval of this page is the flat, special-relativistic case, and the geodesics that extremise it become, in the curved case, the worldlines of freely-falling bodies.
