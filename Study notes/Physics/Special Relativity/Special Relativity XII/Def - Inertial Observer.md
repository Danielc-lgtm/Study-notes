---
type: definition
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus metric $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a future-timelike four-velocity is normalised to $U \cdot U = 1$. An [[Def - Observer and Local Rest Space|observer]] $\mathcal{O}$ is a future-timelike unit worldline $\mathscr{L}$ parametrised by its proper time $\tau$ (sometimes written $t$), carrying an orthonormal [[Def - Local Frame and Four-Rotation|local frame]] $(e_0, e_1, e_2, e_3)$ with $e_0 = U$ the four-velocity. The four-acceleration is $a = \mathrm{d}U/\mathrm{d}\tau$ and the four-rotation $\omega$ is the spatial part of the frame's evolution, both orthogonal to $U$; see [[Def - Local Frame and Four-Rotation]]. Gourgoulhon writes the four-velocity $\vec{u}$ and works in the opposite signature. Full registry on [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

---

# Axiom Motivation

By this point in the series an observer is a thoroughly general object: a future-timelike unit worldline carrying an orthonormal frame, free to accelerate and free to let its frame rotate as it goes. This generality was deliberate — it is the level at which the equivalence principle later attaches gravity — but it is more than the historical theory of special relativity needed. Special relativity was built entirely on the *simplest* observers, the ones Newton would have recognised as "unaccelerated", and the desideratum here is to single those out as a distinguished subclass and to say precisely what distinguishes them. We want a definition that captures the intuition "this observer feels no force and is not spinning", excludes the accelerated and the rotating observers, and from which the classical conveniences — straight worldline, global coordinates, a single consistent "now" across all of space — follow as theorems.

The cleanest specification is in terms of the carried frame. An observer's local frame evolves along the worldline according to the general law $\mathrm{d}e_\alpha/\mathrm{d}\tau = (a\cdot e_\alpha)U - (U\cdot e_\alpha)a + \omega \times_U e_\alpha$, which decomposes the rate of change of each frame vector into a four-acceleration part and a four-rotation part. The simplest possible observer is the one whose frame *does not change at all*: $\mathrm{d}e_\alpha/\mathrm{d}\tau = 0$ for every $\alpha$. This is the design decision, and everything else is its unpacking. A constant frame means the observer carries the same four vectors at every event of its worldline — the same time direction, the same three spatial axes — which is exactly the geometric content of "not accelerating and not rotating". Reading off the evolution law, a constant frame is equivalent to the vanishing of both pieces: $a = 0$ and $\omega = 0$.

Now stress each condition in turn, because the definition has two independent axioms and dropping either gives a genuinely different object. Suppose we keep $a = 0$ but drop $\omega = 0$. Then the four-velocity $e_0 = U$ is constant, so the worldline is straight — the observer moves uniformly in a straight line — but the spatial triad $(e_1, e_2, e_3)$ is free to precess about the direction of motion. This is a perfectly good observer, unaccelerated yet *spinning*; its worldline is straight but it is *not* what we want to call inertial, because a gyroscope it carries would precess for no dynamical reason. Concretely, take $U$ constant and let the spatial frame rotate at constant angular velocity in proper time; then $a = \mathrm{d}U/\mathrm{d}\tau = 0$ but $\omega \neq 0$. This is exactly the counterexample that forbids the seductive shortcut "straight worldline, therefore inertial" — straightness controls only the four-acceleration, and Gourgoulhon flags precisely this as Remark 8.1. So the condition $\omega = 0$ is doing real work: without it the class would include spinning frames.

Suppose instead we keep $\omega = 0$ but drop $a = 0$. Then the frame does not spin, but the four-velocity changes — the observer accelerates, its worldline curves, and a carried accelerometer reads nonzero. This is a uniformly-or-non-uniformly accelerated observer (the Rindler observer of a later chapter is the prototype), and dropping $a=0$ admits all of them. The condition $a = 0$ is therefore the one that captures "feels no force": it is the relativistic statement that the observer is in free fall, or in the absence of gravity, simply at rest or in uniform motion. What goes wrong if we *strengthen* the definition — say, by demanding more than $a = \omega = 0$? There is nothing left to demand: a frame with vanishing acceleration and vanishing rotation is already constant, and a constant frame is the most rigid an observer can be. The two conditions together are exactly necessary and sufficient for the frame to be constant, so the definition is tight — neither axiom is redundant, and no third axiom is available.

One could ask why we phrase the definition through the frame at all, rather than simply as "straight worldline". The answer is the asymmetry just exposed: the worldline sees only the four-velocity $e_0$, so "straight worldline" is equivalent to "$a = 0$" alone and is blind to the spinning of the spatial frame. The frame-based definition is the one that captures the full physical notion of an inertial observer — unaccelerated *and* non-rotating — and it is the one from which the globality of the rest space (the property that really distinguishes inertial observers among all observers) will follow.

---

# The Definition

An **inertial observer** is an [[Def - Observer and Local Rest Space|observer]] $\mathcal{O}$ whose orthonormal local frame $(e_\alpha)$ is constant along its worldline:
$$
\frac{\mathrm{d}e_\alpha}{\mathrm{d}\tau} = 0, \qquad \alpha = 0, 1, 2, 3,
$$
where $\tau$ is the observer's proper time. Equivalently — by the frame-evolution law — an inertial observer is one whose four-acceleration and four-rotation both vanish along the entire worldline:
$$
\forall \tau, \qquad a(\tau) = 0 \quad\text{and}\quad \omega(\tau) = 0.
$$

Since $e_0 = U$ is the four-velocity, the condition $a = \mathrm{d}U/\mathrm{d}\tau = 0$ makes $U$ a single constant vector of the displacement space $E$, the same at every event of the worldline. Integrating $\mathrm{d}x^\alpha/\mathrm{d}\tau = U^\alpha$ (with $c$: $\mathrm{d}x^\alpha/\mathrm{d}t = c\,U^\alpha$) twice then gives the worldline as a straight line of Minkowski spacetime,
$$
x^\alpha(\tau) = U^\alpha\,\tau + x_0^\alpha
\qquad\left(\text{with } c:\quad x^\alpha(t) = c\,U^\alpha\,t + x_0^\alpha\right),
$$
parametrised affinely by proper time, with $(U^\alpha, x_0^\alpha)$ eight constants fixed by the initial four-velocity and initial event.

**The converse fails.** A straight worldline guarantees only $a = 0$; it does not guarantee $\omega = 0$. An observer with constant four-velocity but a precessing spatial triad has a straight worldline yet is not inertial. The inertial observers are a *proper* subclass of the unaccelerated observers.

The four-velocity of an inertial observer being a single constant vector is the property that makes its [[Def - Observer and Local Rest Space|local rest space]] global (see [[Thm - Globality of the Local Rest Space for Inertial Observers]]); the qualifier "local" may then be dropped, and one speaks simply of the **frame** and **rest space** of the inertial observer, and of the global **inertial coordinates** (also called Minkowskian or Galilean coordinates) it defines.

---

# Relate to Other Fields / Compression

The inertial observer is the flat-spacetime ancestor of the **freely-falling observer** of general relativity. There, the worldline of an observer in free fall is a *geodesic* — a curve of vanishing covariant acceleration $\nabla_U U = 0$ — and the condition $a = 0$ of this page is exactly the geodesic condition specialised to flat spacetime, where the covariant derivative reduces to the ordinary one. The condition $\omega = 0$ becomes Fermi–Walker transport with no spatial rotation, the curved-spacetime notion of "non-spinning frame". So an inertial observer is a freely-falling, non-rotating observer in the spacetime that happens to have no gravity.

**True name:** an inertial observer is *an observer whose four-velocity is constant and whose carried frame does not spin* — equivalently, the observer for whom a carried accelerometer reads exactly zero and a carried gyroscope does not precess. This operational form is what one actually checks: point an accelerometer (tests $a = 0$) and a gyroscope (tests $\omega = 0$), and the observer is inertial precisely when both read null. It is more useful than the geometric "constant frame" because it is what a physical apparatus measures, and it makes immediate why inertiality is a frame-independent, absolute property: acceleration and rotation are absolute, detectable without reference to any other observer, unlike velocity which is relative.

There is also a structural compression worth stating: the inertial observers are exactly the orbits of the *one-parameter subgroups of translations* of the Poincaré group. A constant four-velocity $U$ generates the translation $\tau \mapsto$ (translate by $\tau U$), and the worldline $x_0 + \tau U$ is the orbit of the starting event under this subgroup. In this sense the inertial worldlines are the integral curves of the constant vector fields on Minkowski space, i.e. the orbits of the translation subgroup of [[Def - The Poincaré Group|the Poincaré group]] — which is the precise link between the geometry of this page and the group theory of the chapter.

---

# Examples / Corollaries

**Is an instance — an observer at rest at the spatial origin of an inertial frame.** Take $U = (1, 0, 0, 0)$ (with $c$: $U = (1, \mathbf{0})$ so that $\mathrm{d}x^0/\mathrm{d}t = c$), constant, with the standard spatial axes $e_i$ also constant. Then $a = \mathrm{d}U/\mathrm{d}\tau = 0$ and $\omega = 0$: this is the canonical inertial observer, sitting still, ageing along the time axis. Its worldline is the straight line $x^\alpha(\tau) = (\tau, 0, 0, 0)$.

**Is an instance — an observer in uniform motion.** Take $U = \gamma(1, v, 0, 0)$ with $\gamma = (1-v^2)^{-1/2}$, constant, and a constant spatial triad obtained by boosting the standard axes. Again $a = 0$ and $\omega = 0$: a particle coasting at constant velocity is an inertial observer, and its worldline is the straight line $x^\alpha(\tau) = \gamma(\tau, v\tau, 0, 0) + x_0^\alpha$. Any two inertial observers of this kind are related by a [[Def - The Lorentz Transformation|Lorentz transformation]] (plus a shift of origin), which is the content of §12.2.

**Is NOT an instance — a uniformly accelerated observer.** Take the hyperbolic worldline $x^1 = \sqrt{a^{-2} + (x^0)^2}$ of an observer with constant proper acceleration. Its four-velocity is *not* constant — it rotates hyperbolically in the $(x^0, x^1)$-plane — so $a \neq 0$, and the observer is not inertial. Its worldline is a hyperbola, not a straight line, and (as a later chapter shows) its rest spaces intersect, producing a coordinate horizon. This is the prototypical non-inertial observer.

**Is NOT an instance — an unaccelerated but spinning observer.** Take $U = (1, 0, 0, 0)$ constant (so $a = 0$ and the worldline is the straight time axis), but let the spatial triad rotate, $e_1(\tau) = \cos(\Omega\tau)\,\hat{x} + \sin(\Omega\tau)\,\hat{y}$, $e_2(\tau) = -\sin(\Omega\tau)\,\hat{x} + \cos(\Omega\tau)\,\hat{y}$, $e_3 = \hat{z}$, precessing at rate $\Omega$ in proper time. Then $\mathrm{d}e_1/\mathrm{d}\tau \neq 0$, so the frame is not constant, $\omega \neq 0$, and the observer is *not* inertial — even though its worldline is a perfectly straight line. This is the decisive non-example: it shows that straightness of the worldline is strictly weaker than inertiality, and it is the explicit construction behind [[Ex - A straight worldline need not be inertial]].

**Corollary — the four-velocity is constant.** An immediate consequence of $a = 0$ is that $U(\tau)$ is one fixed vector of $E$, independent of $\tau$. This single fact is the workhorse of the chapter: from it follow the straightness of the worldline, the parallelism of the rest-space hyperplanes, and the globality of the inertial coordinates.

**Corollary — proper time is affine parameter along the worldline.** Because $U$ is constant and unit, the proper time $\tau$ is, up to scale, an affine parameter on the straight-line worldline: equal increments of $\tau$ correspond to equal coordinate displacements $U^\alpha\,\Delta\tau$. An inertial clock therefore ticks uniformly in any inertial coordinate time, dilated only by the constant factor $\gamma$.

**Calibration check.** If you have understood the definition you should be able to (i) write down the worldline of an inertial observer with given initial four-velocity $U$ and initial event $x_0$, namely $x^\alpha(\tau) = U^\alpha\tau + x_0^\alpha$; (ii) decide, given an observer with $a = 0$, whether it is inertial — and answer "not necessarily, only if also $\omega = 0$"; and (iii) explain why a carried accelerometer and a carried gyroscope together test inertiality, the accelerometer testing $a = 0$ and the gyroscope testing $\omega = 0$.

---

# Unlocked by This

> [!tip] Globality of the Rest Space *(from §12.1)*
> The constancy of the four-velocity, established here, is exactly what makes the inertial observer's [[Def - Observer and Local Rest Space|rest space]] global: the $U^\perp$ hyperplanes are all parallel, never intersect, and tile spacetime, so the observer's coordinates $(ct, x^i)$ extend over the whole of $\mathscr{E}$. See [[Thm - Globality of the Local Rest Space for Inertial Observers]].

> [!tip] The Rigid Array of Inertial Observers *(from §12.1)*
> Once one inertial observer is fixed, every observer at rest with respect to it is also inertial, with parallel worldline and synchronised clocks — a [[Def - Rigid Array of Inertial Observers|rigid array]] of inertial observers that fills out a global inertial frame.

> [!tip] Geodesics and the Equivalence Principle *(from General Relativity)*
> The condition $a = 0$ is the flat-spacetime form of the geodesic equation $\nabla_U U = 0$, and the inertial observer is the ancestor of the **freely-falling observer** of general relativity. The **equivalence principle** asserts that a freely-falling, non-rotating observer is *locally* inertial: along their geodesic worldline a carried accelerometer and gyroscope read zero, and the laws of physics reduce to those of special relativity. What this page establishes globally — straightness, constant frame — holds in a curved spacetime only along a single worldline, to first order; the failure to extend it globally is the gravitational field, and its irreducible part is the curvature. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
