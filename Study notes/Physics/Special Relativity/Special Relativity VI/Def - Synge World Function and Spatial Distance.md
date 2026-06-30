---
type: definition
subject: special-relativity
prereqs:
  - "Def - Einstein-Poincaré Simultaneity"
  - "Def - Observer and Local Rest Space"
  - "Thm - Euclidean Character of the Local Rest Space"
  - "Def - The Null Cone and the Time Arrow"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a spacelike vector has $X\cdot X < 0$ and its spatial length is $\|X\| = \sqrt{-X\cdot X}$. An observer $\mathcal{O}$ on worldline $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ reads [[Def - Proper Time|proper time]] $t$; $A$ is a worldline event of proper time $t$, $B$ a nearby event, and the radar photon is emitted at $A_1$ (proper time $t_1 < t$) and received at $A_2$ (proper time $t_2 > t$). The **world function** is $\Omega(A,B) = \tfrac12\,\overrightarrow{AB}\cdot\overrightarrow{AB}$ (Synge's $\Omega$; distinct from the four-rotation $\underline\Omega$). Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (mostly-plus) writes the spatial length as $\|\overrightarrow{AB}\|_g = \sqrt{\overrightarrow{AB}\cdot\overrightarrow{AB}}$, valid because his spacelike vectors have $\overrightarrow{AB}\cdot\overrightarrow{AB} > 0$. In our mostly-minus convention spacelike vectors have $\overrightarrow{AB}\cdot\overrightarrow{AB} < 0$, so $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}}$. The final Synge formula $\|\overrightarrow{AB}\| = c\sqrt{(t-t_1)(t_2-t)}$ is numerically identical in both conventions; only the intermediate scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB}$ flips sign.

---

# Axiom Motivation

Having pinned down *when* events are simultaneous, the observer now wants to know *how far apart* spatial things are. The naive answer is "lay down a ruler", but relativity makes rulers problematic — a ruler is an extended rigid body, and we will see there is no satisfactory notion of rigidity. The deeper point, which this page makes precise, is that an observer does not *need* a ruler: distance can be measured with nothing but a clock and the ability to bounce light. Time is the primary measurable; length is derived from it. This inversion of the usual hierarchy is the conceptual heart of the page, and it is exactly how the metre is defined today (as a fixed fraction of a light-second).

The construction is the same radar experiment that defined simultaneity, but now we keep a different piece of its output. Bounce a photon off the distant event $B$: emitted at proper time $t_1$, received at $t_2$, with the midpoint event $A$ (proper time $t = \tfrac12(t_1+t_2)$) simultaneous with $B$. The simultaneity construction extracted $U_0\cdot\overrightarrow{AB}$ (and set it to zero). But the *same* linear system also delivers the scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB}$, and that is precisely the squared spatial length, because $B$ lies in $\mathcal{O}$'s [[Def - Observer and Local Rest Space|rest space]] (it is simultaneous with $A$), where the [[Thm - Euclidean Character of the Local Rest Space|metric is Euclidean]]. So distance falls out of the radar data for free.

What form must the answer take? Dimensional and symmetry considerations almost fix it. The distance can depend only on the two one-way times $t - t_1$ (outbound) and $t_2 - t$ (inbound), it must vanish when $B$ is on the worldline (both times zero), and it must be symmetric under swapping emission and reception. The combination that does all this and has the dimensions of length (with $c$) is the geometric mean,
$$
\|\overrightarrow{AB}\| \;=\; c\sqrt{(t-t_1)(t_2-t)}.
$$
For a target the observer regards as *simultaneous* (so $t = \tfrac12(t_1+t_2)$, whence $t - t_1 = t_2 - t = \tfrac12(t_2-t_1)$), this collapses to the familiar half-round-trip rule $\|\overrightarrow{AB}\| = \tfrac12 c(t_2 - t_1)$ — distance equals half the round-trip time times $c$, the everyday radar formula. The general geometric-mean form is what is needed when $A$ is *not* the simultaneous midpoint.

Why introduce the world function $\Omega(A,B) = \tfrac12\overrightarrow{AB}\cdot\overrightarrow{AB}$ as well? Because the radar construction naturally produces the scalar square, and packaging "half the squared interval between two events" as a scalar field $\Omega$ on pairs of events is the object that *generalises* cleanly to curved spacetime, where there is no global notion of "the displacement vector $\overrightarrow{AB}$". In flat spacetime $\Omega$ is just $\tfrac12\overrightarrow{AB}\cdot\overrightarrow{AB}$; in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]] it becomes Synge's two-point world function, defined as half the squared geodesic distance, and it is the master tool for expanding any bitensor near coincidence. Introducing it here, where it is elementary, prepares that generalisation.

A beautiful sanity check, which also illuminates *why* the formula is a geometric mean, is the Euclidean analogy. In the Euclidean plane the **power of a point** $A$ with respect to a circle $\mathcal C$ of centre $B$ and radius $R$ is $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$ along any line through $A$ meeting $\mathcal C$ at $A_1, A_2$, and it equals $\|\overrightarrow{AB}\|^2 - R^2$. Synge's formula is the *Minkowskian* power of a point with the radius set to zero — because in spacetime the "circle" is the light cone, whose radius (measured by the metric) is zero, since $B$ is null-separated from both photon events $A_1, A_2$. The factorised geometric-mean structure is exactly the factorisation $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$ of the power of a point.

---

# The Definition

Let $\mathcal{O}$ be an observer on $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$, and let $B$ be an event near $\mathcal{L}_0$ with spacelike displacement $\overrightarrow{AB}$ from a worldline event $A$ of [[Def - Proper Time|proper time]] $t$. A photon emitted from $\mathcal{L}_0$ at proper time $t_1$ reflects at $B$ and returns at proper time $t_2$.

**Synge's spatial-distance formula.** The spatial length of $\overrightarrow{AB}$, measured with the metric, is
$$
\boxed{\,\|\overrightarrow{AB}\| \;=\; c\,\sqrt{(t - t_1)(t_2 - t)}\,},
$$
expressing distance purely in terms of the proper-time readings $t, t_1, t_2$. When $A$ and $B$ are **simultaneous** for $\mathcal{O}$ (so $t = \tfrac12(t_1+t_2)$ and $t - t_1 = t_2 - t = \tfrac12(t_2-t_1)$), it reduces to the half-round-trip rule
$$
\|\overrightarrow{AB}\| \;=\; \tfrac12\,c\,(t_2 - t_1).
$$

**World function.** The **world function** of two events $A, B$ in flat spacetime is half their squared interval,
$$
\Omega(A, B) \;:=\; \tfrac12\,\overrightarrow{AB}\cdot\overrightarrow{AB},
$$
so $\overrightarrow{AB}\cdot\overrightarrow{AB} = 2\Omega$. The radar construction yields $\overrightarrow{AB}\cdot\overrightarrow{AB} = -c^2(t-t_1)(t_2-t)$ in mostly-minus signature, whence $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}}$ gives Synge's formula. (In curved spacetime $\Omega$ is defined as half the squared geodesic distance between $A$ and $B$ — Synge's two-point world function.)

> [!note]- Derivation from the radar scalar square
> From the [[Def - Einstein-Poincaré Simultaneity|radar construction]], the two null conditions on the photon legs give (in mostly-minus signature, with $U_0\cdot U_0 = +1$)
> $$c^2(t-t_1)^2 + 2c(t-t_1)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0,$$
> $$c^2(t-t_2)^2 + 2c(t-t_2)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0.$$
> Solving the linear system for the two unknowns $U_0\cdot\overrightarrow{AB}$ and $\overrightarrow{AB}\cdot\overrightarrow{AB}$: subtracting gave $U_0\cdot\overrightarrow{AB} = -c[t - \tfrac12(t_1+t_2)]$. Substituting back into the first equation,
> $$\overrightarrow{AB}\cdot\overrightarrow{AB} = -c^2(t-t_1)^2 - 2c(t-t_1)\,U_0\cdot\overrightarrow{AB} = -c^2(t-t_1)^2 + 2c^2(t-t_1)\big[t - \tfrac12(t_1+t_2)\big].$$
> Factor out $c^2(t-t_1)$: the bracket is $-(t-t_1) + (2t - t_1 - t_2) = t - t_2$, so
> $$\overrightarrow{AB}\cdot\overrightarrow{AB} = c^2(t-t_1)(t-t_2) = -c^2(t-t_1)(t_2-t).$$
> This is negative (since $t_1 < t < t_2$), confirming $\overrightarrow{AB}$ is spacelike. The spatial length is $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}} = c\sqrt{(t-t_1)(t_2-t)}$. $\blacksquare$

---

# Relate to Other Fields / Compression

Operationally this is **radar ranging**, the principle behind radar, sonar (with sound speed in place of $c$), lidar, and laser interferometric distance measurement: distance is half the signal round-trip time times the signal speed. The 1983 SI redefinition of the metre — the distance light travels in vacuum in $1/299\,792\,458$ of a second — *is* this formula elevated to a definition, making length officially a derived quantity and the speed of light an exact defined constant. The world function $\Omega$ is, in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]], Synge's two-point function, the basic ingredient of the covariant expansion of Green functions, the geodesic deviation, and the optical (Fermat) metric used to compute gravitational lensing.

**True name:** the spatial distance is *the geometric mean of the two one-way light times, times $c$* — $\|\overrightarrow{AB}\| = c\sqrt{(t-t_1)(t_2-t)}$ — equivalently *the square root of (minus) the world function's double*. The geometric-mean structure is the Minkowskian power of a point with zero radius; carrying that picture makes the formula impossible to misremember.

---

# Examples / Corollaries

**Is an instance — half the round-trip to a simultaneous target.** A radar operator pings a target simultaneous with the moment of detection: emission at $t_1$, reception at $t_2$, target dated to $t = \tfrac12(t_1+t_2)$. The distance is $\tfrac12 c(t_2 - t_1)$, the everyday formula. This is the special case $t - t_1 = t_2 - t$ of the general geometric mean.

**Is an instance — the metre as a light-time.** Defining $1\ \mathrm{m}$ as the distance light travels in $1/299\,792\,458\ \mathrm{s}$ is exactly Synge's formula with a fixed round-trip time; the SI metre is a chronometric quantity. This is the formula serving as a *definition* rather than a measurement.

**Is NOT an instance — a "distance" to a timelike-separated event.** If $B$ is *not* simultaneous with any chosen $A$ but timelike-separated from the worldline, $\overrightarrow{AB}$ is not spacelike and $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}}$ is imaginary — there is no spatial distance, because the events are not "at the same time" in any rest space. The formula presupposes $B$ in a rest space (spacelike separation); applied blindly it signals its own inapplicability via a negative radicand.

**Is NOT an instance — a ruler measurement assuming rigidity.** Measuring distance by laying down a rigid rod is *not* equivalent to Synge's chronometric distance unless the rod is Born-rigid, and we will see no extended rigid rod exists. The radar definition is primary precisely because it needs no rigid body. (See [[Def - Born Rigidity Criterion]].)

**Corollary — the power of a point with zero radius.** The Euclidean identity $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} + R^2$ becomes, in spacetime with $R = 0$ (because $\overrightarrow{BA_1}, \overrightarrow{BA_2}$ are null), $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$; writing $\overrightarrow{AA_1} = c(t_1 - t)U_0$, $\overrightarrow{AA_2} = c(t_2 - t)U_0$ and using $U_0\cdot U_0 = +1$ recovers $\|\overrightarrow{AB}\|^2 = c^2(t-t_1)(t_2-t)$. The geometric-mean structure *is* the factorised power of a point.

**Calibration check.** You should be able to: (1) recover $\|\overrightarrow{AB}\| = \tfrac12 c(t_2-t_1)$ as the simultaneous special case of the geometric-mean formula; (2) state why the radicand is positive exactly when $B$ is spacelike-separated, i.e. lies in a rest space; and (3) explain the power-of-a-point analogy, including why the "radius" is zero in the Minkowskian case.

---

# Unlocked by This

> [!tip] Born's Rigidity Criterion *(from §6.2)*
> Applying Synge's formula to a pair of neighbouring worldlines (the two ends of a ruler) and demanding the distance be constant gives **Born's rigidity criterion**: the ruler is rigid iff the photon round-trip time between its ends is constant, $\|\overrightarrow{AB}\| = \tfrac12 c(t_2 - t_1) = \mathrm{const}$ — a chronometric, ruler-free rigidity test. See [[Def - Born Rigidity Criterion]].

> [!tip] The Local Frame and Observer Coordinates *(from §6.2)*
> Synge's formula is the tool for verifying that a carried tetrad is orthonormal — orthogonality and unit-length of the spatial axes are checked by measuring distances chronometrically — and hence for setting up the observer's [[Def - Local Frame and Four-Rotation|local frame]] and spatial coordinates $(x^i)$.

> [!tip] Synge's World Function and the Optical Metric *(from General Relativity)*
> The world function $\Omega(A,B)$ generalises to half the squared geodesic distance in curved spacetime — **Synge's two-point function** — the master tool for covariant near-coincidence expansions, geodesic deviation, and the **optical (Fermat) metric** governing gravitational lensing in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]].
