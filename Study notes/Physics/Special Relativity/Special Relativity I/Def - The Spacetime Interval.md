---
type: definition
subject: special-relativity
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Two events have coordinates $(t_1, x_1, y_1, z_1)$ and $(t_2, x_2, y_2, z_2)$ in an inertial frame; their separation is $\Delta t = t_2 - t_1$, $\Delta x = x_2 - x_1$, and so on. The interval is written $\Delta s^2$ — a single symbol, *not* the square of a real number $\Delta s$, because the quantity can be negative. The infinitesimal version is the line element $ds^2$. The full registry is on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

The [[Def - The Lorentz Transformation|Lorentz transformation]] has just told us something disorienting: the time $\Delta t$ between two events and the distance $\Delta x$ between them are both frame-dependent. Two observers will not agree on how much time elapsed, nor on how far apart things were. In Newtonian physics each of these was an absolute, observer-independent fact; now both are gone. The natural question — and the one that organises the entire geometry of spacetime — is: **is anything left? Is there a quantity built from $\Delta t$ and $\Delta x$ that all observers agree on?**

There is, and one can almost guess it from the rotation analogy. In Euclidean geometry, a rotation changes the coordinates $\Delta x$ and $\Delta y$ of the separation between two points, but the *distance* $\Delta x^2 + \Delta y^2$ is left invariant — that is the defining property of a rotation. The Lorentz transformation is, structurally, a rotation between space and time, so we should look for a similar quadratic combination of $\Delta t$ and $\Delta x$ that the boost leaves alone. The desideratum is sharp: a quadratic form $a\,\Delta t^2 + b\,\Delta t\,\Delta x + c\,\Delta x^2$ whose value is unchanged when $\Delta t, \Delta x$ are run through the boost.

Imposing invariance ([[Thm - Invariance of the Spacetime Interval]]) pins it down: the combination must be $\Delta t^2 - \Delta x^2$, up to an overall scale. The crucial feature is the **minus sign**. In Euclidean geometry the two coordinates entered with the same sign, $+x^2 + y^2$, and rotations preserved that. Here time and space enter with *opposite* signs, $+\Delta t^2 - \Delta x^2$, and the boost preserves this indefinite combination. The minus sign is not a blemish; it is the entire difference between Minkowski geometry and Euclidean geometry, and it is forced — a $+\Delta x^2$ would not be boost-invariant.

Why define the interval as this specific combination and not, say, $\Delta t^2 + \Delta x^2$ or $|\Delta t| + |\Delta x|$? Because only $\Delta t^2 - \Delta x^2$ is invariant, and invariance is the whole point — we are hunting for the thing observers agree on. The cost of the minus sign is that the interval is **not positive definite**: it can be positive, negative, or zero, and two distinct events can have zero interval. This forces the strange convention of writing $\Delta s^2$ as an indivisible symbol rather than the square of anything real. But that cost buys the [[Def - Classification of Four-Vectors|causal classification]] of spacetime — timelike, spacelike, null — which is the deepest structure in the subject, so it is a bargain.

---

# The Definition

Let two events have separation $(\Delta t, \Delta x, \Delta y, \Delta z)$ in an inertial frame. The **spacetime interval** between them is
$$
\boxed{\quad \Delta s^2 \;=\; \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2 \quad}
$$
(with $c$ restored: $\Delta s^2 = c^2\,\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$). The symbol $\Delta s^2$ is a single quantity, which may be positive, negative, or zero; it is not in general the square of a real number.

The **classification of the separation** is by the sign of $\Delta s^2$:

- $\Delta s^2 > 0$ — the events are **timelike separated**. They are "closer in space than in time": a particle travelling slower than light can be present at both.
- $\Delta s^2 < 0$ — the events are **spacelike separated**. They are "closer in time than in space": no signal at or below the speed of light connects them.
- $\Delta s^2 = 0$ — the events are **null** or **lightlike separated**. They lie on a common light ray; a light signal connects them.

The **infinitesimal interval**, or **line element**, between two infinitesimally close events is
$$ds^2 = dt^2 - dx^2 - dy^2 - dz^2.$$
The interval has the same value in every inertial frame ([[Thm - Invariance of the Spacetime Interval]]); this invariance is its reason for existing.

---

# Categorical / Structural Definition

The interval is the **quadratic form associated to the Minkowski metric**. A symmetric bilinear form $\eta$ on a real vector space assigns to each vector $X$ a number $\eta(X,X)$, its quadratic form; here the vector space is the space of event-separations, $\eta$ is the [[Def - Minkowski Space and the Metric|Minkowski metric]] $\mathrm{diag}(1,-1,-1,-1)$, and
$$\Delta s^2 = \eta(\Delta X, \Delta X) = \Delta X^\mu\, \eta_{\mu\nu}\, \Delta X^\nu$$
for the separation four-vector $\Delta X$. From this viewpoint the interval is not a primitive object but the diagonal of the metric, and the metric is the primitive. The advantage of the bilinear-form perspective is that it makes the invariance of the interval an instance of the invariance of the metric: a [[Def - The Lorentz Group|Lorentz transformation]] is *defined* as a linear map preserving $\eta$, hence preserves $\eta(X,X)$ for every $X$, hence preserves the interval. §1.3 takes this structural view as primary.

---

# Relate to Other Fields / Compression

The interval is the Minkowski analogue of **Euclidean distance-squared**. In $\mathbb{R}^3$ the quantity $\Delta x^2 + \Delta y^2 + \Delta z^2$ is the squared distance, invariant under the rotation group $O(3)$, and it is positive definite — zero only when the two points coincide. The interval $\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ is its relativistic replacement, invariant under the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$, and it differs in exactly one respect: the signature. Euclidean distance has signature $(+,+,+)$; the interval has signature $(+,-,-,-)$. Every difference between the two geometries — null vectors, the light cone, the reversed triangle inequality — is downstream of that one sign.

In general relativity the line element $ds^2$ generalises to $ds^2 = g_{\mu\nu}(x)\,dx^\mu dx^\nu$ with a position-dependent metric $g_{\mu\nu}$, encoding gravity as curvature. The constant Minkowski $ds^2$ of special relativity is the flat, gravitation-free case — the local model that curved spacetime is built to look like at every point.

---

# Examples / Corollaries

**Is an instance — two ticks of a clock at rest.** A clock sitting still at $x = 0$ ticks at $t = 0$ and $t = T$. The separation is $\Delta t = T$, $\Delta x = 0$, so $\Delta s^2 = T^2 > 0$: the two ticks are **timelike separated**, as they must be — a clock (slower than light) is present at both. Here $\Delta s = T$ is the [[Def - Proper Time|proper time]] between the ticks.

**Is an instance — the two ends of a measuring rod, taken simultaneously.** A rod of length $L$ lies along the $x$-axis; consider its two ends at the same instant, $\Delta t = 0$, $\Delta x = L$. Then $\Delta s^2 = -L^2 < 0$: the two events are **spacelike separated**. No signal connects "the left end now" to "the right end now", which is exactly why simultaneity of these events is frame-dependent.

**Is an instance — emission and absorption of a photon.** A photon is emitted at one event and absorbed at another. Light travels at speed $1$, so $\Delta x = \Delta t$ and $\Delta s^2 = \Delta t^2 - \Delta x^2 = 0$: the events are **null separated**. This is the calibration check — any pair of events on a light ray has zero interval.

**Is NOT an instance of "zero distance implies same point".** Two *distinct* events on a light ray have $\Delta s^2 = 0$. In a Euclidean space, zero distance forces the points to coincide; in Minkowski space it does not. This is the most important way the interval differs from an ordinary distance, and it is a direct consequence of indefiniteness.

**Corollary — the interval refines "elapsed time" and "distance".** Newtonian physics had two separate invariants, $\Delta t$ and $\sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$. Relativity fuses them: neither is invariant alone, but the specific combination $\Delta t^2 - \Delta x^2 - \cdots$ is. The interval is what survives when time and distance individually do not.

**Corollary — the light cone is the locus $\Delta s^2 = 0$.** Fixing one event at the origin, the set of events with $\Delta s^2 = 0$ is the cone $t^2 = x^2 + y^2 + z^2$ — the [[Ex - Causal structure and the light cone|light cone]]. It separates the timelike interior (causally connectible) from the spacelike exterior (causally disconnected).

---

# Unlocked by This

> [!tip] Proper Time *(from Relativistic Kinematics)*
> For a timelike worldline, integrating $ds = \sqrt{ds^2}$ along the curve gives the **proper time** ([[Def - Proper Time]]) — the time elapsed on a clock carried along that worldline. The interval is the infinitesimal building block of proper time, just as the Euclidean line element is the building block of arc length.

> [!tip] The Metric Tensor of General Relativity *(from General Relativity)*
> Promoting the constant Minkowski line element $ds^2 = dt^2 - dx^2 - dy^2 - dz^2$ to a position-dependent form $ds^2 = g_{\mu\nu}(x)\,dx^\mu dx^\nu$ gives the **metric tensor** of general relativity; its variation encodes the gravitational field, and the geodesics of $g$ are the worldlines of freely-falling bodies.
