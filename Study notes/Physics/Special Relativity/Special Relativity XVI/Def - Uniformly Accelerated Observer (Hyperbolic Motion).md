---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so timelike vectors have positive square. An **observer** is a future-directed timelike unit worldline $\mathcal{L}_0$ carrying an orthonormal frame; $U$ is its [[Def - Four-Velocity and Four-Acceleration|four-velocity]] ($U\cdot U = 1$) and $A = dU/dt$ its four-acceleration ($A\cdot U = 0$), with $t$ the [[Def - Proper Time|proper time]]. The four-acceleration is spacelike, so its norm is $\|A\| = \sqrt{-A\cdot A}$. The **four-rotation** $\vec\omega$ (equivalently the rotation part of the antisymmetric tensor $\Omega$) measures how the carried spatial frame turns relative to a non-rotating one ([[Def - Local Frame and Four-Rotation]]). Full registry on [[Special Relativity XVI — Accelerated Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 12) uses mostly-plus, with $\vec u\cdot\vec u = -1$ and a spacelike four-acceleration of *positive* square $\vec a\cdot\vec a = a^2$. Translating to mostly-minus flips the overall sign: $U\cdot U = +1$ and $A\cdot A = -a^2$, so the *norm* $\|A\| = \sqrt{-A\cdot A} = a$ is identical in both conventions. Only the squared scalar products carry the sign; the proper acceleration $a$ does not.

---

# Axiom Motivation

We want to capture the simplest possible non-inertial observer — the one closest to inertial while still genuinely accelerating. An inertial observer has zero four-acceleration; the natural next case is one whose four-acceleration is, in some sense, "constant". The whole subtlety of the definition is in pinning down *which* sense, because the obvious one is wrong.

The naive desideratum is to mimic Newton: a uniformly accelerated body should have $A = \mathrm{const}$, a fixed four-acceleration vector, just as a uniformly accelerated Newtonian particle has $\mathbf{a} = \mathrm{const}$. This fails, and the failure is instructive. The four-acceleration is not free; it is rigidly constrained by $A\cdot U = 0$, because differentiating $U\cdot U = 1$ gives $2A\cdot U = 0$. The four-velocity $U$ of an accelerating observer is *not* constant — that is the whole point of accelerating — so it rotates in spacetime, and a four-acceleration that stayed fixed could not remain orthogonal to a rotating $U$. Push this through: if $A = \mathrm{const}$, then integrating $dU/dt = A$ gives $U(t) = tA + U_0$, and demanding $U\cdot U = 1$ for all $t$ forces $t^2(A\cdot A) + 2t(U_0\cdot A) + U_0\cdot U_0 = 1$ identically in $t$, which requires $A\cdot A = 0$ and $U_0\cdot A = 0$. A four-acceleration orthogonal to a timelike vector is spacelike, and a spacelike vector with $A\cdot A = 0$ is zero. So $A = \mathrm{const}$ forces $A = 0$: the observer is inertial after all. The "obvious" definition collapses to the trivial case, and this is why it must be rejected.

The repair is to fix the *norm* rather than the vector: demand $\|A\| = a = \mathrm{const}$, and let the four-acceleration vector turn freely so as to stay orthogonal to the turning four-velocity. The norm $a$ is the magnitude of the acceleration the observer actually *feels* — the reading of an accelerometer they carry — and it is a scalar, invariant under Lorentz transformations, so "constant $\|A\|$" is a frame-independent statement. This is the correct generalisation of Newtonian uniform acceleration: not a constant vector, but a constant felt magnitude.

Two further conditions complete the definition, and each excludes a genuinely different observer. First, the worldline must lie in a **timelike plane** $\Pi$. Drop this, and one admits worldlines that wander in three spatial dimensions while keeping $\|A\| = a$ — for instance helical motion, which has constant proper acceleration but is not the clean back-and-forth hyperbolic motion we want; the plane condition is what makes the worldline a hyperbola rather than a more complicated curve of constant first curvature. Second, the **four-rotation must vanish**, $\vec\omega = 0$. Drop this, and the observer's spatial frame spins as it is carried along — the observer is rotating as well as accelerating, the subject of [[Special Relativity XVII — Rotating Observers|Chapter XVII]], not this one. Setting $\vec\omega = 0$ isolates *pure* acceleration: the frame is dragged along the worldline with no twist, Fermi–Walker transported. With these three conditions — constant proper acceleration, planar worldline, vanishing four-rotation — the observer is determined up to a choice of $a$ and an initial inertial frame, and the worldline is forced to be a hyperbola.

One can test the definition against the role it plays downstream. The whole point of a uniformly accelerated observer is that they are *stationary* in a precise sense: nothing about their local physics changes with proper time, because all events on their worldline are equivalent (a translation along the hyperbola is a Lorentz boost, a symmetry). This stationarity requires both that the felt acceleration not change ($\|A\| = \mathrm{const}$) and that the frame not rotate ($\vec\omega = 0$); a constant *vector* $A$ would single out a preferred direction in spacetime and break the equivalence of the worldline's events. So the definition is exactly what is needed for the observer to be the relativistic analogue of "sitting still in a uniform gravitational field" — a configuration in which, by the equivalence principle, the physics is genuinely time-independent.

---

# The Definition

A **uniformly accelerated observer** — equivalently an observer in **hyperbolic motion**, or a **Rindler observer** — is an [[Def - Observer and Local Rest Space|observer]] $\mathcal{O}$, of worldline $\mathcal{L}_0$, four-velocity $U$, four-acceleration $A$ and proper time $t$, satisfying three conditions:

1. **Planar worldline.** $\mathcal{L}_0$ lies in a timelike plane $\Pi$ of spacetime; equivalently $U(t)\in\Pi$ and $A(t)\in\Pi$ for all $t$.

2. **Constant proper acceleration.** The *norm* of the four-acceleration is constant along $\mathcal{L}_0$:
$$
a := \|A\| = \sqrt{-A\cdot A} = \mathrm{const}.
$$
The scalar $a$ is the **proper acceleration**; with $c$ restored it has dimensions of inverse length, $[a] = \mathrm{m}^{-1}$, and $g := c^2 a$ is the corresponding ordinary acceleration in $\mathrm{m\,s^{-2}}$.

3. **Vanishing four-rotation.** The [[Def - Local Frame and Four-Rotation|four-rotation]] of the carried frame is identically zero, $\vec\omega = 0$ — the frame is non-rotating (Fermi–Walker transported).

The condition is on the *norm* $a$, not on the four-acceleration *vector* $A$: imposing $A = \mathrm{const}$ together with $A\cdot U = 0$ and $U\cdot U = 1$ forces $A = 0$, an inertial observer. The vector $A$ continuously reorients so as to remain orthogonal to the changing four-velocity, while its length stays fixed.

An observer satisfying only conditions 2 and 3 (constant $\|A\|$, $\vec\omega = 0$) but with a worldline not confined to a plane is called a **stationary observer**; the uniformly accelerated observer is the planar special case, and an inertial observer ($a = 0$) is the degenerate case of both.

---

# Relate to Other Fields / Compression

The cleanest reframing is differential-geometric. A timelike worldline carries, by the Serret–Frenet construction ([[Def - Curvature and Torsions of a Worldline]]), a *first curvature* equal to the norm of the four-acceleration. So "uniformly accelerated" is exactly "constant first curvature", and the planar condition is "vanishing torsions". In Euclidean geometry the plane curve of constant curvature is the circle; in Lorentzian geometry the timelike plane curve of constant curvature is the equilateral hyperbola. The hyperbolic motion of relativity is the precise Minkowski analogue of uniform circular motion, with the proper acceleration $a$ playing the role of the curvature $\kappa = 1/r$ and $a^{-1}$ the radius of the osculating hyperbola.

**True name:** a uniformly accelerated observer is *a timelike worldline of constant curvature $a$, traversed at unit speed, with its frame Fermi–Walker transported*. The operational content is that the proper acceleration is the felt acceleration — what an accelerometer reads — and is constant, while the velocity, the coordinate acceleration, and the direction of $A$ all change. When a problem says "constant acceleration", read it as "constant felt magnitude", never "constant vector".

The concrete physical realisation is a charged particle in a uniform electrostatic field, treated in detail in [[Special Relativity XXI — The Electromagnetic Field|Chapter XXI]]: the Lorentz four-force $qF\cdot U$ produces a four-acceleration of constant norm $a = |q|E/(mc^2)$, so the particle's worldline is a hyperbola. This is the special-relativistic version of the parabolic trajectory of a charge in a capacitor, straightened into a hyperbola by the requirement that the speed never exceed $c$.

---

# Examples / Corollaries

**Is an instance — a charge in a uniform electric field.** A particle of charge $q$ and mass $m$ in a uniform electric field $\mathbf{E}$ experiences a four-acceleration of constant norm $a = |q|E/(mc^2)$, with the worldline confined to the plane spanned by the time direction and $\mathbf{E}$, and no rotation. It is the prototypical uniformly accelerated observer.

**Is an instance — the late-time limit of any bounded constant-thrust rocket.** A rocket that fires its engine to maintain a constant felt acceleration (a constant accelerometer reading) is uniformly accelerated for as long as the burn lasts, regardless of how its coordinate acceleration decays in the launch frame.

**Is NOT an instance — an observer with constant four-acceleration vector.** An observer for whom $A$ is a fixed vector (not merely fixed norm) cannot exist non-trivially: the orthogonality $A\cdot U = 0$ and normalisation $U\cdot U = 1$ force such an observer to be inertial, $A = 0$. The "constant vector" reading of uniform acceleration has no non-trivial solutions.

**Is NOT an instance — a helical worldline of constant proper acceleration.** A particle in a uniform magnetic field moves on a helix with constant $\|A\|$ (the centripetal four-acceleration has fixed norm) and $\vec\omega = 0$, so it is a *stationary* observer, but its worldline is not confined to a timelike plane — it is not uniformly accelerated in the sense of this page, and its worldline is not a hyperbola. This shows the planar condition is doing real work.

**Is NOT an instance — a rotating accelerated observer.** An observer on a circular orbit who keeps their spatial frame pointing radially "outward" has $\vec\omega\neq 0$: the frame rotates once per orbit. Even with constant $\|A\|$ and a planar (circular) orbit, the nonzero four-rotation excludes them from this definition and places them in [[Special Relativity XVII — Rotating Observers|Chapter XVII]]. (Curiously, this *same* orbiting observer's gyroscope undergoes Thomas precession — but that is a rotation relative to the *inertial* frame, not the intrinsic $\vec\omega$.)

**Corollary — the proper acceleration is observer-independent.** Because $a = \sqrt{-A\cdot A}$ is the norm of a four-vector, it is a Lorentz scalar: every inertial observer assigns the *same* value $a$ to the proper acceleration, even though they each measure a different *coordinate* acceleration. This is the precise sense in which "constant acceleration" is a meaningful, frame-free statement.

**Calibration check.** If the definition is understood, the reader should be able to: (i) explain in one line why $A = \mathrm{const}$ forces $A = 0$ (orthogonality to a turning $U$); (ii) compute the proper acceleration of an electron in a $1\,\mathrm{V/m}$ field and find the corresponding $a^{-1}$ in metres (it is enormous); and (iii) decide, for a given worldline, whether it is uniformly accelerated, merely stationary, or rotating, by checking the three conditions in turn.

---

# Unlocked by This

> [!tip] The Rindler Wedge and Its Coordinates *(from §16.2)*
> The set of all uniformly accelerated observers with their worldlines parallel in a given plane fills out a wedge-shaped region of Minkowski space — the **Rindler wedge** $x_* > |ct_*|$ — and their worldlines provide a natural coordinate grid on it, the [[Def - Rindler Coordinates and the Accelerated Frame|Rindler coordinates]]. The wedge is exactly the region causally accessible to the family of accelerated observers, bounded by the [[Def - Rindler Horizon|Rindler horizon]].

> [!tip] The Unruh Temperature *(from quantum field theory in curved spacetime)*
> The single scalar $a$ defined here sets the temperature of the **Unruh effect**: a uniformly accelerated detector immersed in the Minkowski vacuum registers a thermal bath at temperature $T = \hbar a/(2\pi c k_B)$. The proper acceleration is thus not merely a kinematic label but a thermodynamic one, and the same formula with the surface gravity in place of $a$ gives the **Hawking temperature** of a black hole. That a purely kinematic quantity — the felt acceleration of an observer in flat spacetime — should fix a temperature is among the deepest hints that gravity, thermodynamics, and quantum theory are intertwined.
