---
type: definition
subject: special-relativity
prereqs:
  - "Def - Inertial Observer"
  - "Def - Observer and Local Rest Space"
  - "Thm - Globality of the Local Rest Space for Inertial Observers"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\mathcal{O}$ is an [[Def - Inertial Observer|inertial observer]] of worldline $\mathscr{L}$, four-velocity $U$, rest space $\mathscr{E}_u(t)$ and frame $(e_0 = U, e_1, e_2, e_3)$; $t$ is its proper time. A second observer $\mathcal{O}'$ is *fixed with respect to* $\mathcal{O}$ when its spatial coordinates $(x^1, x^2, x^3)$ in $\mathcal{O}$'s inertial frame are constant. Its worldline is $\mathscr{L}'$. Full registry on [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

---

# Axiom Motivation

A single inertial observer carries one clock and measures along one worldline. But physics is done with *frames* — extended grids of rulers and synchronised clocks filling a region of space — and the question this definition answers is: can one inertial observer's frame be populated by a whole family of inertial observers, one at each spatial point, all agreeing on time? The desideratum is a coherent rigid lattice of inertial observers that *is* a global inertial reference frame, the relativistic version of Newton's rigid coordinate grid.

The natural construction is to take observers "fixed with respect to" the original one — observers whose spatial coordinates in $\mathcal{O}$'s frame never change, sitting at fixed lattice points $(x^1, x^2, x^3)$. The motivating worry is whether such an observer is itself inertial, and whether their clocks can be made to agree. Both turn out favourably, and seeing *why* is the content. An observer fixed in $\mathcal{O}$'s inertial frame has, by the globality of $\mathcal{O}$'s rest space, a worldline that is a straight line *parallel* to $\mathscr{L}$ — because its position is $\overrightarrow{O(0)O'(t)} = ct\,U + x^i e_i$ with constant $x^i$ and constant $e_i$, so as $t$ runs the worldline traces $ct\,U$ plus a fixed offset, a line parallel to $\mathcal{O}$'s. A line parallel to an inertial worldline has the same constant four-velocity $U$, hence the same vanishing four-acceleration; equipping it with the same constant spatial frame $(e_i)$ makes its four-rotation vanish too. So a fixed observer is automatically inertial, with four-velocity equal to $\mathcal{O}$'s.

This is the crucial input, and it depends on $\mathcal{O}$ being inertial in the first place. Were $\mathcal{O}$ accelerated, an observer "fixed" at a constant spatial coordinate would *not* have a parallel straight worldline — it would share $\mathcal{O}$'s acceleration, its rest spaces would tilt and intersect, and the rigid grid would tear (this is the Bell-spaceship and Rindler-rigidity story of a later chapter). The rigidity is clean precisely because the parallelism of inertial rest spaces ([[Thm - Globality of the Local Rest Space for Inertial Observers]]) guarantees the lattice points keep constant separations measured in the common rest space. The four-velocity being shared means the whole lattice moves as one rigid body with no internal stresses — the relativistic notion of *Born rigidity* in its simplest, unaccelerated case.

The remaining freedom is the *synchronisation* of the clocks. Each fixed observer has its own proper time, and a priori the zero of each clock is arbitrary. But since all the worldlines are parallel with the same $U$, the proper times coincide up to a constant offset; choosing the *same origin* for every clock makes them all read the same value on each common rest-space slice $\mathscr{E}_u(t)$. The array is then **synchronised**: the ideal clocks carried by every observer indicate the same value simultaneously (in the shared Einstein–Poincaré sense, which for an inertial frame is unambiguous and global). This synchronisation is possible *only* because the rest spaces are global and non-intersecting; it is exactly the operation that fails for accelerated or rotating arrays, where global synchronisation is obstructed (the rotating-disk desynchronisation of a later chapter).

---

# The Definition

Let $\mathcal{O}$ be an [[Def - Inertial Observer|inertial observer]] with worldline $\mathscr{L}$, constant four-velocity $U$, rest space $\mathscr{E}_u(t)$, and constant frame $(e_0 = U, e_1, e_2, e_3)$. An observer $\mathcal{O}'$ is **fixed with respect to** $\mathcal{O}$ if its spatial coordinates $(x^1, x^2, x^3)$ in $\mathcal{O}$'s inertial frame are constant in time. Then:

1. The worldline $\mathscr{L}'$ of $\mathcal{O}'$ is a straight line of Minkowski spacetime **parallel** to $\mathscr{L}$, with
$$
\overrightarrow{O(0)\,O'(t)} = ct\,U + x^i e_i \qquad (x^i \text{ constant}).
$$
2. $\mathcal{O}'$ has the same four-velocity $U$ as $\mathcal{O}$, hence (equipped with the same constant spatial frame $(e_i)$) is itself an inertial observer, with rest spaces coinciding with those of $\mathcal{O}$: $\mathscr{E}_{u'}(t) = \mathscr{E}_u(t)$.
3. The proper time of $\mathcal{O}'$ coincides with that of $\mathcal{O}$ up to a constant; choosing the same origin for all proper times makes the clocks **synchronised** — every observer's clock reads the same value on each common rest-space slice.

A **rigid array of inertial observers** is any family of observers, each fixed with respect to a given inertial observer $\mathcal{O}$ (equivalently, all sharing the common four-velocity $U$ and constant frame), with proper times sharing a common origin so that the carried clocks are synchronised. Such an array fills out a region of spacetime with a lattice of parallel inertial worldlines whose mutual spatial separations, measured in the common rest space, are constant in time. The array realises a **global inertial reference frame**: the inertial coordinate system $(ct, x^1, x^2, x^3)$ assigns to each event the reading of the array's clocks and the lattice position of the observer present there. The coordinates $(x^i)$ are called the **inertial coordinates** (or Minkowskian, or Galilean coordinates) of the frame.

---

# Relate to Other Fields / Compression

A rigid array of inertial observers is the relativistic version of the **rigid coordinate grid** of Newtonian mechanics — a lattice of clocks and rulers, all at rest with respect to one another, all keeping the same time. The difference from the Newtonian grid is that "the same time" is now Einstein–Poincaré simultaneity, which is frame-dependent: a *different* inertial array, in relative motion, slices spacetime into a different family of synchronous surfaces, and the two arrays disagree about simultaneity even though each is internally consistent.

**True name:** a rigid array of inertial observers is *a congruence of parallel inertial worldlines with synchronised clocks* — equivalently, the integral curves of a single constant four-velocity field, time-sliced by their common rest spaces. The "congruence of parallel worldlines" form is the operational one: it tells you the array is rigid (parallel lines keep constant separation), inertial (each line is straight with the shared $U$), and globally synchronisable (the common rest spaces never intersect), all at once.

The compression worth recording is that the rigid array is the *simplest* solution of the **Born rigidity** condition — the relativistic criterion for a body whose parts maintain constant mutual distances in their instantaneous rest spaces. For an unaccelerated body the Born condition is satisfied by exactly the parallel-inertial-worldline congruences described here. The general (accelerated) Born-rigid motions are far more constrained — the Herglotz–Noether theorem shows the rigid motions of relativity form only a finite-parameter family, in stark contrast to the infinite-dimensional rigid motions of Newtonian mechanics — and the inertial rigid array is the trivial, stress-free representative.

---

# Examples / Corollaries

**Is an instance — the standard inertial frame.** Take $\mathcal{O}$ at rest at the spatial origin with $U = (1, \mathbf{0})$, and populate every lattice point $(x^1, x^2, x^3) \in \mathbb{R}^3$ with an observer at rest there. All worldlines are vertical (parallel to the time axis), all clocks tick coordinate time, and synchronising them at $t = 0$ makes the whole grid read the same time on every horizontal slice $t = \mathrm{const}$. This is the canonical global inertial frame.

**Is an instance — a uniformly moving frame.** Boost the standard array by velocity $v$ along $x$: every observer now has $U = \gamma(1, v, 0, 0)$, the worldlines are parallel lines of slope $1/v$ in the $(t, x)$-diagram, and the common rest spaces are the tilted hyperplanes $t = vx + \mathrm{const}$. The array is rigid and synchronised in its own sense, though the original array disagrees with its simultaneity. This is a second global inertial frame, related to the first by a passive [[Def - The Poincaré Group|Poincaré transformation]].

**Is NOT an instance — a uniformly accelerated "rigid" array.** Take observers each undergoing constant proper acceleration, arranged to stay at fixed Rindler coordinate positions. Their worldlines are hyperbolae, not parallel straight lines; their rest spaces are *not* parallel and in fact all intersect at the Rindler horizon; and their clocks cannot be globally synchronised — clocks at different heights tick at different rates (the accelerated redshift). This is a Born-rigid array, but *not* an inertial one, and it exhibits precisely the pathologies (intersecting rest spaces, desynchronisation, horizon) that the inertial case avoids.

**Is NOT an instance — a rotating array.** A lattice corotating with a spinning disk has each observer on a helical worldline with nonzero four-acceleration (centripetal) and nonzero four-rotation; the clocks around the rim cannot be globally synchronised (the Sagnac desynchronisation), and the spatial geometry is non-Euclidean (the Ehrenfest paradox). Again Born-rigid in the rotating sense but not inertial.

**Corollary — mutual separations are constant.** For two members of the array at lattice points $x^i$ and $y^i$, the separation vector in the common rest space is $(y^i - x^i)e_i$, constant in $t$, with constant Euclidean length $\big[\sum_i(y^i - x^i)^2\big]^{1/2}$. The lattice is rigid: no member approaches or recedes from another.

**Corollary — the array defines a global inertial coordinate system.** Every event $M$ of spacetime is assigned the coordinates $(ct, x^i)$ where $t$ is the synchronised clock reading of the array on the rest space through $M$, and $(x^i)$ the lattice position of the worldline through $M$. This is a global affine chart, the inertial coordinate system, valid over all of $\mathscr{E}$ — which is possible exactly because the rest spaces are global ([[Thm - Globality of the Local Rest Space for Inertial Observers]]).

**Calibration check.** If you have understood the definition you should be able to (i) explain why an observer fixed in an inertial frame is automatically inertial, citing the parallelism of the worldlines and the shared four-velocity; (ii) explain why the clocks can be globally synchronised, citing the non-intersection of the common rest spaces; and (iii) name one feature (intersecting rest spaces, or clock desynchronisation, or a horizon) that an accelerated or rotating array has but an inertial array does not.

---

# Unlocked by This

> [!tip] The Global Inertial Frame and the Change of Frame *(from §12.2)*
> A rigid array of inertial observers *is* a global inertial reference frame, and two such frames in relative motion are related by a passive [[Def - The Poincaré Group|Poincaré transformation]] $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$ — the change of inertial coordinates that the Poincaré group governs.

> [!tip] Born Rigidity and the Herglotz–Noether Theorem *(from Accelerated and Rotating Observers)*
> The inertial rigid array is the simplest solution of the **Born rigidity** condition. The general accelerated rigid motions are tightly constrained: the **Herglotz–Noether theorem** shows that, unlike in Newtonian mechanics, a rigid body in special relativity has only a finite-parameter family of possible motions, which is why a relativistic rigid rod cannot be set spinning up arbitrarily and why the rotating disk (Ehrenfest paradox) is subtle. The intersecting rest spaces and clock desynchronisation absent here become central there.

> [!tip] Failure of Global Synchronisation in Curved Spacetime *(from General Relativity)*
> The global synchronisation of a rigid inertial array depends on the non-intersection of its rest spaces, which holds only in flat spacetime. In a general gravitational field one cannot in general build a global rigid array of freely-falling observers with synchronised clocks — tidal forces (geodesic deviation) make neighbouring freely-falling worldlines converge or diverge — and the obstruction is the spacetime curvature. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
