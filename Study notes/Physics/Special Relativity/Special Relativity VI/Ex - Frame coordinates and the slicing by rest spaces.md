---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Local Frame and Four-Rotation"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Nonexistence of Absolute Time"
tags: [physics, special-relativity]
---

# Problem Statement

An observer $\mathcal{O}$ carries a [[Def - Local Frame and Four-Rotation|local frame]] $(e_\alpha)$ along its worldline $\mathcal{L}_0$, defining coordinates $(t, x^i)$ for nearby events by $\overrightarrow{O(t)M} = x^i e_i(t)$, where $O(t)$ is the worldline event at [[Def - Proper Time|proper time]] $t$ and $\mathscr{E}_{U_0}(t)$ is the [[Def - Observer and Local Rest Space|local rest space]] there. Work with $c = 1$.

1. Show that the level sets $\{t = \mathrm{const}\}$ of the time coordinate are exactly the local rest spaces $\mathscr{E}_{U_0}(t)$, and that the spatial coordinate of $M$ is its position in the orthonormal triad.
2. For an observer with constant proper [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A_0$ (magnitude $a = \|A_0\|$, four-rotation $\vec\omega = 0$), show that the neighbouring rest spaces $\mathscr{E}_{U_0}(t)$ and $\mathscr{E}_{U_0}(t + dt)$ are **not parallel** but tilt relative to each other.
3. Show that the two neighbouring rest spaces **intersect** in a plane $\Pi$ at proper distance $a^{-1}$ from the worldline, and conclude that the coordinates $(t, x^i)$ are single-valued only for $r \ll a^{-1}$.
4. Evaluate the locality radius $a^{-1} = c^2/g$ for a human-scale acceleration $g = 10\ \mathrm{m\,s^{-2}}$, restoring $c$.

**Recall:**

![[Def - Local Frame and Four-Rotation#The Definition]]

A vector orthogonal to the worldline lies in the [[Def - Observer and Local Rest Space|local rest space]]; for an accelerated observer the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ rotates as $dU_0/d\tau = A_0$, so the rest spaces at different proper times are tilted ([[Thm - Nonexistence of Absolute Time|different four-velocities give different rest spaces]]). The proper acceleration magnitude is $a = \|A_0\| = \sqrt{-A_0\cdot A_0}$.

---

# Convergent Strategy

**Problem class.** A *build-coordinates-and-find-their-domain* problem: the observer's frame furnishes coordinates, and the task is to identify the constant-time surfaces and the limit of validity. The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] connects the slicing by rest spaces to the locality of the frame.

**Assumption pattern.** The frame's defining equation $\overrightarrow{O(t)M} = x^i e_i(t)$ and the rotation of $U_0$ under acceleration are the inputs. The key fact is that for an accelerated observer the rest spaces tilt (because $U_0$ rotates), so neighbouring slices intersect at a finite distance. The signpost is "accelerated observer's frame coordinates" — always local, with radius $a^{-1}$.

**Theorem routing.** Part 1 is definitional: $t$ labels the slice, $x^i$ the position within it. Part 2 uses $dU_0/d\tau = A_0\neq 0$ to show the normals $U_0(t)$ and $U_0(t+dt)$ differ, so the orthogonal hyperplanes tilt. Part 3 finds the intersection by setting the two slice equations equal, giving distance $a^{-1}$. Part 4 restores $c$.

**Key decision point.** The crux is that the *tilt* of the rest spaces is forced by the rotation of $U_0$, and the rate of tilt is the acceleration $a$, so the slices converge at distance $1/a$. The non-obvious point is that this is *not* a coordinate artifact removable by a better chart — it is the genuine geometric fact that an accelerated observer's simultaneity surfaces cross, the flat-space seed of horizons and tidal limits.

---

# Legal Operations Used

1. **Read the four-acceleration off the frame evolution** (operation 9 from the topic page). The rotation $dU_0/d\tau = A_0$ drives the tilting of the rest spaces.

2. **Translate simultaneity into orthogonality** (operation 2 from the topic page). Each rest space is the hyperplane orthogonal to $U_0(t)$; tilting normals give tilting (intersecting) hyperplanes.

3. **Compute a spatial distance** (operation 4 from the topic page). The intersection distance $a^{-1}$ is a proper length in the rest space.

---

# Hints

> [!note]- Hint 1
> By construction, $M$ with coordinate $t$ lies in $\mathscr{E}_{U_0}(t)$ (the slice through $O(t)$ orthogonal to $U_0(t)$). So $\{t = \mathrm{const}\}$ *is* a rest space. The $x^i$ are the components of $\overrightarrow{O(t)M}$ in the orthonormal triad $(e_i)$.

> [!note]- Hint 2
> The rest space $\mathscr{E}_{U_0}(t)$ has normal $U_0(t)$; the next one has normal $U_0(t+dt) = U_0(t) + A_0\,dt$ (since $dU_0/d\tau = A_0$). Since $A_0\neq 0$, the normals differ, so the hyperplanes are not parallel — they tilt by an angle of order $a\,dt$.

> [!note]- Hint 3
> Put the worldline event $O(t)$ at the origin, $U_0 = (1,0,0,0)$, $A_0 = a\,e_1$ (so $a = \|A_0\|$). The slice $\mathscr{E}_{U_0}(t)$ is $\{x^0 = 0\}$. The next slice $\mathscr{E}_{U_0}(t+dt)$ passes through $O(t+dt) = O(t) + dt\,U_0$ with normal $U_0 + a\,dt\,e_1$. Its equation is $(U_0 + a\,dt\,e_1)\cdot\overrightarrow{O(t+dt)M} = 0$. Expand to first order in $dt$; the intersection with $\{x^0 = 0\}$ is at $x^1 = -1/a$.

> [!note]- Hint 4
> Restore $c$: $a$ has dimensions of inverse length (in geometric units), and the proper acceleration in ordinary units is $g = c^2 a$, so $a^{-1} = c^2/g$. Plug $g = 10\ \mathrm{m\,s^{-2}}$, $c = 3\times10^8\ \mathrm{m\,s^{-1}}$.

---

# Solution

The computation localises the observer's coordinates. Step 1 identifies the constant-time slices as rest spaces. Step 2 shows the slices tilt because $U_0$ rotates under acceleration. Step 3 finds where neighbouring slices cross — at distance $1/a$ — bounding the coordinate domain. Step 4 puts in numbers: the radius is astronomically large for everyday accelerations.

**Step 1: Constant-time slices are the rest spaces.**

> [!note]- Derivation
> By the [[Def - Local Frame and Four-Rotation|definition]] of the observer coordinates, an event $M$ with time coordinate $t$ is the one lying in the local rest space $\mathscr{E}_{U_0}(t)$ — the hyperplane through the worldline event $O(t)$ orthogonal to $U_0(t)$ — and its spatial coordinates are the components $x^i$ of $\overrightarrow{O(t)M} = x^i e_i(t)$ in the orthonormal spatial triad. Hence
> $$\{t = \mathrm{const}\} = \mathscr{E}_{U_0}(t) = O(t) + U_0(t)^\perp,$$
> the local rest space, and $(x^1, x^2, x^3)$ is the Euclidean position of $M$ within it. The slicing of (a neighbourhood of) spacetime by the rest spaces *is* the time coordinate of the observer's frame.

**Step 2: For an accelerated observer the slices tilt.**

> [!note]- Derivation
> The rest space $\mathscr{E}_{U_0}(t)$ has unit normal $U_0(t)$. The neighbouring rest space at proper time $t + dt$ has normal
> $$U_0(t + dt) = U_0(t) + \frac{dU_0}{d\tau}\,dt = U_0(t) + A_0\,dt,$$
> using $dU_0/d\tau = A_0$ ([[Def - Four-Velocity and Four-Acceleration|four-acceleration]]). Since $A_0\neq 0$ (accelerated observer), the two normals $U_0(t)$ and $U_0(t) + A_0\,dt$ are **not parallel** — they differ by the spacelike vector $A_0\,dt$. Therefore the hyperplanes orthogonal to them are **not parallel** either: they tilt relative to one another by an angle of order $\|A_0\|\,dt = a\,dt$. (For an inertial observer, $A_0 = 0$, the normals are all equal, the rest spaces are parallel, and the slicing is global — consistent with [[Thm - Nonexistence of Absolute Time|inertial observers having global simultaneity]].)

**Step 3: Neighbouring slices intersect at distance $a^{-1}$.**

> [!note]- Derivation
> Adopt the instantaneous rest frame at $O(t)$: put $O(t)$ at the origin, $U_0(t) = (1, 0, 0, 0)$, and $A_0 = a\,e_1 = (0, a, 0, 0)$ (the acceleration is spacelike, in the rest space, of magnitude $a$). The slice $\mathscr{E}_{U_0}(t)$ is
> $$\{M : U_0\cdot\overrightarrow{OM} = 0\} = \{x^0 = 0\}.$$
> The next slice passes through $O(t + dt) = dt\,U_0 = (dt, 0, 0, 0)$ with normal $U_0 + a\,dt\,e_1 = (1, a\,dt, 0, 0)$, so its equation is
> $$(1, a\,dt, 0, 0)\cdot\overrightarrow{O(t+dt)M} = 0 \;\Longrightarrow\; (x^0 - dt) - a\,dt\,x^1 = 0$$
> (using $\overrightarrow{O(t+dt)M} = (x^0 - dt, x^1, x^2, x^3)$ and the metric sign on the spatial term, $-(-a\,dt)x^1$... let us be explicit: with $\eta = \mathrm{diag}(+,-,-,-)$, $(1, a\,dt, 0,0)\cdot(x^0 - dt, x^1, x^2, x^3) = (x^0 - dt) - a\,dt\,x^1$). Setting this to zero: $x^0 = dt(1 + a x^1)$. The **intersection** of the two slices is where both $x^0 = 0$ and $x^0 = dt(1 + a x^1)$ hold:
> $$0 = dt(1 + a x^1) \;\Longrightarrow\; 1 + a x^1 = 0 \;\Longrightarrow\; x^1 = -\frac{1}{a}.$$
> So the two neighbouring rest spaces meet in the plane $\Pi = \{x^0 = 0,\ x^1 = -1/a\}$, at proper distance $|x^1| = 1/a = a^{-1}$ from the worldline (on the side *opposite* the acceleration). Beyond this distance the slicing folds over: an event near $\Pi$ lies in *both* $\mathscr{E}_{U_0}(t)$ and $\mathscr{E}_{U_0}(t+dt)$, so it would receive two different time coordinates. Hence the frame coordinates $(t, x^i)$ are single-valued and well-behaved only within the **locality radius**
> $$r \ll a^{-1} = \|A_0\|^{-1}.$$

**Step 4: The locality radius for everyday acceleration.**

> [!note]- Derivation
> Restore $c$. In geometric units $a$ is an inverse length; the proper acceleration in ordinary units is $g = c^2 a$, so the locality radius is
> $$a^{-1} = \frac{c^2}{g}.$$
> For a human-scale acceleration $g = 10\ \mathrm{m\,s^{-2}}$ (about Earth gravity) and $c = 3\times10^8\ \mathrm{m\,s^{-1}}$,
> $$a^{-1} = \frac{(3\times10^8)^2}{10} = \frac{9\times10^{16}}{10} = 9\times10^{15}\ \mathrm{m} \approx 1\ \text{light-year}.$$
> So the local frame of an observer accelerating at Earth gravity is trustworthy out to about **one light-year** — the locality restriction is essentially never a practical constraint in a laboratory, but it is conceptually decisive: it is the flat-spacetime ancestor of the statement that a freely-falling frame in general relativity is only *locally* inertial, valid out to the tidal radius set by curvature.

> [!note]- Complete formal solution
> The observer coordinates assign $M$ the time $t$ of the rest space $\mathscr{E}_{U_0}(t)\ni M$ and the spatial position $x^i$ in the triad, so $\{t = \mathrm{const}\} = \mathscr{E}_{U_0}(t) = O(t) + U_0(t)^\perp$. For an accelerated observer the normal rotates, $U_0(t+dt) = U_0(t) + A_0\,dt$ with $A_0\neq 0$, so neighbouring rest spaces tilt by $\sim a\,dt$. In the instantaneous rest frame ($U_0 = (1,0,0,0)$, $A_0 = a\,e_1$), the slice $\{x^0 = 0\}$ and the next slice $x^0 = dt(1 + ax^1)$ intersect at $x^1 = -1/a$, so the coordinates are single-valued only for $r \ll a^{-1} = \|A_0\|^{-1}$. Restoring $c$, $a^{-1} = c^2/g$, which for $g = 10\ \mathrm{m\,s^{-2}}$ is $\approx 9\times10^{15}\ \mathrm{m}\approx 1$ light-year. $\blacksquare$

---

# Key Takeaways

**An accelerated observer's frame is local because their simultaneity surfaces tilt and cross — at distance $1/a$.** The word "local" in "local rest space" and "local frame" is not caution but a hard geometric limit: because the four-velocity rotates under acceleration ($dU_0/d\tau = A_0$), the orthogonal rest spaces at successive instants are not parallel, and neighbouring ones intersect at proper distance $a^{-1} = \|A_0\|^{-1}$ on the side away from the acceleration. Past that distance the slicing folds over and a single event gets two time-coordinates, so the frame is multivalued. The transferable insight: whenever you build coordinates from an accelerated observer's instantaneous rest spaces (Rindler coordinates, Fermi normal coordinates), they have a finite domain of validity set by the inverse acceleration, and the boundary is where the rest spaces cross. For the Rindler congruence this boundary *is* the horizon (the apex of the wedge), so the locality radius and the Rindler horizon are the same phenomenon.

**The tilt rate of the simultaneity surfaces is the acceleration — this is the flat-space seed of horizons and tidal limits.** The rate at which an accelerated observer's rest spaces tilt is exactly the proper acceleration $a$, so the convergence distance is $1/a$. This single fact connects three things: the Rindler horizon (where the rest spaces all cross, at the wedge apex), the desynchronisation of accelerated clocks (the front and back of an accelerating rocket age at different rates), and — through the equivalence principle — the tidal radius of a freely-falling frame in general relativity. The diagnostic to carry forward: an accelerated frame's coordinates are good to distance $\sim c^2/g$, and the obstruction to extending them is always the crossing of simultaneity surfaces, which physically manifests as a horizon or a clock desynchronisation. The bigger the acceleration, the smaller the trustworthy region — a near-light-speed accelerator's frame is local on a tiny scale, while Earth-gravity's frame is local on a light-year scale.

**The locality radius $c^2/g$ is astronomically large for everyday accelerations — the restriction is conceptual, not practical.** Plugging Earth gravity $g = 10\ \mathrm{m\,s^{-2}}$ into $a^{-1} = c^2/g$ gives about one light-year, so a laboratory accelerating at $1g$ has a perfectly good local frame out to interstellar distances. This is why Newtonian and special-relativistic laboratory physics never trips over the locality limit. But the restriction matters enormously in principle: it is the exact flat-spacetime precursor of the general-relativistic fact that a freely-falling frame is only *locally* inertial, and the size of the good region is set there by the spacetime curvature (the tidal radius) rather than by the acceleration. The reusable principle: the validity domain of a local frame is governed by whatever makes the rest spaces fail to be parallel — acceleration in flat spacetime ($r \ll c^2/g$), curvature in curved spacetime ($r \ll$ tidal radius $\sim |R|^{-1/2}$) — and recognising the parallel between the two is the cleanest way to understand why "local inertial frame" is the foundational object of general relativity.
