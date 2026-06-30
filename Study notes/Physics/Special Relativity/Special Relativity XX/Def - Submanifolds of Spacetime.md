---
type: definition
subject: special-relativity
prereqs:
  - "Def - Spacetime Orientation"
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. Spacetime is $\mathscr{E}$, with underlying vector space $E$ of displacements. A coordinate system is $(x^\alpha)$, $\alpha = 0,1,2,3$, with coordinate basis $(\vec{e}_\alpha)$. For a submanifold $\mathscr{V}$ of dimension $p$, an **adapted coordinate system** is one in which the $4-p$ constant coordinates carry **upper-case Latin** indices $A, B \in \{0,\dots,3-p\}$ and the $p$ varying ("internal") coordinates carry **lower-case Latin** indices $a, b \in \{4-p,\dots,3\}$. A **$p$-form** is a totally antisymmetric type-$(0,p)$ tensor (see [[Def - Alternate Forms and the Exterior Product]]). Full registry on [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]].

This is a compound page: it defines three interlocking notions — a **submanifold** of $\mathscr{E}$, a **submanifold with boundary**, and the **orientation** of a submanifold (with the induced orientation on a boundary) — because integration over a region requires all three at once, and none is usable alone.

---

# Axiom Motivation

We have learned to integrate over four-dimensional regions of spacetime. But the integrals physics needs most often are over regions of *lower* dimension: the total charge "now" is an integral over a three-dimensional slice of space; the flux through a wall is an integral over a two-dimensional surface; the proper time along a history is an integral over a one-dimensional curve. So we need a precise notion of "a $p$-dimensional region sitting inside four-dimensional spacetime", and that is what a submanifold is.

What should the definition capture? The model examples are a worldline (a curve, $p=1$), a sphere at an instant (a surface, $p=2$), and "all of space at a fixed time" (a hypersurface, $p=3$). The common feature of all three is that, locally, they are *level sets* of coordinates: a worldline is "fix $x^0, x^1, x^2$, let $x^3$ run"; a constant-time slice is "fix $x^0 = t$, let $x^1, x^2, x^3$ run". This suggests the definition: a submanifold of dimension $p$ is a region that, near each of its points, is cut out by $4-p$ equations $x^A = \mathrm{const}$ in some adapted coordinate system. The number $4-p$ of equations is the codimension, and the coordinates that are *not* fixed are the internal coordinates that parametrise the submanifold. This is the right level of generality: it allows arbitrary curvilinear adapted coordinates (so a sphere, naturally cut out by $r = R$ in spherical coordinates, qualifies just as a coordinate plane does), and it is local (a submanifold may need several adapted charts to cover it).

Why "in *some* adapted coordinate system" rather than a fixed one? Because the same submanifold is cut out by different equations in different coordinates, and the definition must not privilege one. The sphere $r = R$ in spherical coordinates is some curved surface in Cartesian coordinates; both descriptions are legitimate, and the change-of-coordinates condition (16.12 of the source) — that the new constant coordinates must remain constant on $\mathscr{V}$ — is exactly the compatibility that lets you pass between adapted charts.

Now, the bare definition by equalities cannot describe a region *with an edge*. A disk has a boundary circle; a closed ball has a boundary sphere; the cut-off slab "$t = 0$, $r \le R$" has a boundary "$t=0$, $r=R$". None of these is a submanifold in the equalities-only sense, because near a boundary point the region is only "half" of a coordinate neighbourhood. The fix is to add one *inequality*: a submanifold with boundary is cut out by the $4-p$ equalities together with $x^{4-p}\le K$ for a constant $K$. The boundary $\partial\mathscr{V}$, where $x^{4-p} = K$, is then itself a submanifold (in the equalities-only sense) of dimension $p-1$ — the edge has one fewer dimension, as it must. This is the minimal addition that lets the theory handle the compact regions Stokes' theorem is about; allowing $p=4$ in the with-boundary definition recovers the four-dimensional domains of the previous section, now equipped with a three-dimensional boundary.

Finally, orientation. To integrate over a submanifold you must choose a consistent sense of "positive" — the analogue of choosing $\mathrm{d}x\,\mathrm{d}y$ rather than $\mathrm{d}y\,\mathrm{d}x$. For the whole of spacetime this was done by choosing the 4-form $\epsilon$; for a $p$-submanifold it is done by choosing a nowhere-vanishing *$p$-form* $\rho$, which declares a $p$-tuple of tangent vectors right-handed when $\rho$ is positive on it. The reason an orientation must be a *nowhere-vanishing* form is that it must never be ambiguous: a form that vanished somewhere would fail to distinguish right- from left-handed at that point, tearing the consistent sense. Not every submanifold admits such a form (the Möbius strip does not — it is non-orientable), but every simply connected one does. The payoff of orientation is the *induced orientation on a boundary*, which is what makes Stokes' theorem hold with a definite sign: given an orientation $\rho$ on $\mathscr{V}$ and the outward-pointing coordinate vector $\vec{e}_{4-p}$ at the boundary, the $(p-1)$-form $\rho(\vec{e}_{4-p},\,\cdot\,)$ orients $\partial\mathscr{V}$. The choice "outward-normal-first" is not arbitrary: it is exactly the convention under which the fundamental theorem of calculus reads $f(B) - f(A)$ with the correct signs, and any other choice flips the sign of every Stokes computation.

---

# The Definition

**Submanifold.** A part $\mathscr{V}$ of spacetime $\mathscr{E}$ is a **submanifold of dimension $p \in \{1,2,3\}$** if, in the neighbourhood of each of its points, there is a coordinate system $(x^\alpha)$ in which $\mathscr{V}$ is defined by the $4-p$ equations
$$
\mathscr{V}: \quad x^A = \mathrm{const}, \qquad A \in \{0,\dots,3-p\}.
$$
Such coordinates are **adapted to $\mathscr{V}$**. The three cases are:
- $p = 1$: $\mathscr{V}$ is a **curve** (e.g. a worldline); $x^0, x^1, x^2$ are constant and $x^3$ parametrises $\mathscr{V}$.
- $p = 2$: $\mathscr{V}$ is a **surface**; $x^0, x^1$ are constant and $(x^2, x^3)$ label its points.
- $p = 3$: $\mathscr{V}$ is a **hypersurface**; $x^0$ is constant and $(x^1, x^2, x^3)$ are internal coordinates.

In adapted coordinates, the last $p$ coordinate basis vectors $(\vec{e}_a)_{4-p\le a\le 3}$ are tangent to $\mathscr{V}$, and the first $4-p$ linear forms $(\mathrm{d}x^A)$ of the dual basis vanish on tangent vectors. A change of coordinates $(x^\alpha)\mapsto(x'^\alpha)$ keeps the new coordinates adapted iff
$$
\left.\frac{\partial x'^A}{\partial x^a}\right|_{\mathscr{V}} = 0, \qquad 0\le A\le 3-p,\quad 4-p\le a\le 3.
$$

**Submanifold with boundary.** A **submanifold with boundary** $\mathscr{V}$ of dimension $p$ is defined by adding to the equalities one inequality on the first internal coordinate:
$$
\mathscr{V}: \quad x^A = \mathrm{const}\ (A\in\{0,\dots,3-p\}) \quad\text{and}\quad x^{4-p}\le K,
$$
for a constant $K\in\mathbb{R}$. The value $p = 4$ is allowed (then the condition is $x^0\le K$), recovering the four-dimensional domains of the previous section. The **boundary** $\partial\mathscr{V}$ is the part where $x^{4-p} = K$; it is a submanifold (without boundary) of dimension $p-1$, defined by
$$
\partial\mathscr{V}: \quad x^A = \mathrm{const}, \qquad A \in \{0,\dots,4-p\},
$$
and on it the coordinate basis vector $\vec{e}_{4-p}$ is directed towards the exterior of $\mathscr{V}$.

**Orientation.** An **orientation** of a submanifold $\mathscr{V}$ of dimension $p$ is a differential $p$-form $\rho$ on $\mathscr{V}$ that vanishes for no $p$-tuple of linearly independent tangent vectors. $\mathscr{V}$ is **orientable** if such a $\rho$ exists, and $(\mathscr{V},\rho)$ is then an **oriented submanifold**. A $p$-tuple $(\vec{v}_1,\dots,\vec{v}_p)$ of tangent vectors is **right-handed** if $\rho(\vec{v}_1,\dots,\vec{v}_p) > 0$ and **left-handed** if $\rho(\vec{v}_1,\dots,\vec{v}_p) < 0$; adapted coordinates are **right-handed with respect to $\mathscr{V}$** when $(\vec{e}_a)$ is right-handed.

**Induced orientation.** If $\mathscr{V}$ (with boundary) carries the orientation $\rho$, the boundary $\partial\mathscr{V}$ inherits the **induced orientation** defined at each of its points by the $(p-1)$-form
$$
\rho_{\partial\mathscr{V}}(\vec{v}_1,\dots,\vec{v}_{p-1}) \;:=\; \rho(\vec{e}_{4-p}, \vec{v}_1,\dots,\vec{v}_{p-1}),
$$
where $\vec{e}_{4-p}$ is the outward-pointing coordinate vector. This is the **outward-normal-first** convention.

---

# Relate to Other Fields / Compression

This is the elementary, embedded-in-flat-space version of the general notion of a **smooth submanifold with boundary** treated in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]]. The general theory defines a submanifold as the image of an embedding or, equivalently (by the constant-rank theorem), as a level set of a submersion; the "adapted coordinates" of the present definition are exactly the flat-chart coordinates the constant-rank theorem provides, in which the embedding becomes the inclusion of a coordinate plane. The orientation by a nowhere-vanishing top-form is the standard definition, and the outward-normal-first induced orientation on the boundary is the [[Def - Spacetime Orientation|orientation]] convention that makes [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] sign-correct.

**True name:** a submanifold is "locally a coordinate slice", and its boundary orientation is "outward-normal-first". The operational content is that to integrate over $\mathscr{V}$ you find adapted coordinates making it a coordinate box, and to apply Stokes' theorem you orient $\partial\mathscr{V}$ so that prepending the outward vector to a positively-oriented boundary frame gives a positively-oriented frame of $\mathscr{V}$. Carrying these two recipes is what lets every integral and every boundary term in the chapter be computed without sign errors.

---

# Examples / Corollaries

**Is an instance — a sphere at an instant.** In inertial spherical coordinates $(t,r,\theta,\varphi)$, the conditions $t = 0$ and $r = R$ define a sphere $\mathscr{S}$ of radius $R$: a submanifold of dimension $p = 2$, with constant coordinates $(x^A) = (t, r)$ and internal coordinates $(x^a) = (\theta, \varphi)$. This is the prototypical surface; its area element is computed in [[Def - Volume, Area, Length Elements and Flux Integrals]].

**Is an instance — a constant-time hyperplane.** The single condition $t = 0$ in inertial coordinates defines a hyperplane (a hypersurface, $p = 3$): the rest space of the inertial observer who carries the coordinates, with internal coordinates $(r, \theta, \varphi)$ or $(x, y, z)$. This is the "space at an instant" over which total charge and energy are integrated.

**Is an instance — a submanifold with boundary.** The conditions $t = 0$ and $r \le R$ define a ball in the hyperplane $t = 0$: a submanifold with boundary of dimension $p = 3$. Its boundary, where $r = R$, obeys $t = 0$ and $r = R$ — the sphere of radius $R$, a submanifold of dimension $2$. The radial coordinate vector $\vec{e}_r$ points outward across the boundary sphere, as the definition requires.

**Is an instance — a null hypersurface.** In null coordinates $(u,v,\theta,\varphi)$ the condition $u = 0$ defines a hypersurface that is the future light cone of the origin event. It is a perfectly good submanifold of dimension $p = 3$, but its normal is *null* — a feature that breaks the unit-normal apparatus of [[Def - Volume, Area, Length Elements and Flux Integrals]] and requires a separate treatment.

**Is NOT an instance — a disk via the equalities-only definition.** A two-dimensional disk (a filled circle) is *not* a submanifold under the equalities-only definition, because near a point of its bounding circle the disk occupies only "half" a coordinate neighbourhood — there is no coordinate system making it a full coordinate plane there. The disk is a submanifold *with boundary*, cut out by an equality and the inequality $\rho\le R$; the bounding circle is its boundary. This is exactly the gap the with-boundary definition fills.

**Is NOT an instance — the Möbius strip (non-orientable).** A Möbius strip is a two-dimensional submanifold but admits no nowhere-vanishing 2-form: any attempt to choose a consistent right-handed sense fails after one trip around the strip, where the sense reverses. It is therefore *not orientable*, and integration of a 2-form over it (and hence Stokes' theorem) is not defined. Orientability is a genuine restriction, not automatic.

**Calibration check.** If you have understood these definitions you should be able to: (i) write the adapted coordinates and the constant/internal index sets for the worldline of an observer at rest (a curve $p=1$ in inertial coordinates); (ii) state the dimension of the boundary of a four-dimensional region and describe its defining equation; and (iii) explain why orienting a boundary "outward-normal-first" rather than "inward-normal-first" flips the sign of every Stokes integral, by tracing the sign of $\rho(\vec{e}_{4-p},\,\cdot\,)$.

---

# Unlocked by This

> [!tip] Cauchy Surfaces and the Initial-Value Formulation *(from General Relativity and PDE Theory)*
> A spacelike hypersurface — "all of space at one instant", with a timelike unit normal — is the relativistic notion of a moment of time, and the data a field carries on it constitute the **initial data** for the field's evolution. A spacelike hypersurface on which *every* inextendible causal curve registers exactly once is a **Cauchy surface**: specifying the field and its normal derivative there determines the field everywhere in the spacetime it controls. This is the geometric setting of the entire initial-value problem of relativistic physics, and in general relativity the **ADM formulation** recasts Einstein's equations as the evolution of the geometry of a Cauchy surface from one slice to the next — the submanifolds-with-boundary of this page are exactly the slices and the spacetime slabs between them.

> [!tip] Manifolds with Corners and the Cobordism Relation *(from Differential Topology)*
> Allowing a region to have not just a smooth boundary but **corners** — places where two boundary faces meet, locally modelled on a quadrant — extends Stokes' theorem to the regions one actually integrates over (a spacetime slab capped by two slices and a tube at infinity is such a corner-region). At a deeper level, the relation "$\mathscr{V}$ has boundary $\partial\mathscr{V}$" organises manifolds into the **cobordism** relation: two closed $(p-1)$-manifolds are cobordant if together they bound a $p$-manifold. Cobordism is the equivalence relation underlying a large part of differential topology, and Stokes' theorem is the reason it interacts so cleanly with integration — the integral of a closed form is a cobordism invariant.
