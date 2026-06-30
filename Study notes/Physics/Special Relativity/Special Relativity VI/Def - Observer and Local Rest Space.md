---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Einstein-Poincaré Simultaneity"
  - "Def - Worldline of a Particle"
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so timelike means $X\cdot X > 0$, spacelike $X\cdot X < 0$, null $X\cdot X = 0$. An **observer** $\mathcal{O}$ has a future-directed timelike unit worldline $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$) and reads [[Def - Proper Time|proper time]] $t$ on a carried clock. The **local rest space** at an event $A$ is written $E_{U_0}$ or $E_{U_0}(A)$ (as a vector subspace) and $\mathscr{E}_{U_0}(A)$ (as an affine hyperplane through $A$); the exact **simultaneity hypersurface** is $\Sigma_{U_0}(A)$. This is a compound page: it defines two interlocking notions — the **observer** and the **local rest space** — because the rest space is the observer's instantaneous notion of space and neither is usable without the other. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (mostly-plus, $\vec u\cdot\vec u = -1$) writes the rest space as $E_u(A) = u^\perp$ and notes its vectors are spacelike via $g(v,v) > 0$ in *his* convention. In our mostly-minus convention the orthogonal complement $U_0^\perp$ is unchanged (orthogonality is signature-free), but its vectors are spacelike in the sense $X\cdot X < 0$.

---

# Axiom Motivation

This page builds the two objects that turn a moving clock into an observer who can do physics: the **observer** itself, and the **space** that observer perceives at each instant. The starting point is already in hand from the previous page — [[Def - Einstein-Poincaré Simultaneity|simultaneity for 𝒪 is orthogonality to the four-velocity]] — and the question is what structure that simultaneity carves out.

First, what minimally *is* an observer? Up to now we have only had a worldline and a clock, enough to assign proper time along the worldline. To date and locate events off the worldline we need more, but the irreducible core is this: a future-directed timelike unit worldline (so that proper time and a four-velocity exist) together with the ability to make measurements. The four-velocity $U_0$ must be future-directed (an observer experiences time in one direction) and unit ($U_0\cdot U_0 = +1$, so that the parameter is proper time and the tangent is normalised). Why timelike and not null or spacelike? A null worldline has no proper time (no rest frame; it is a photon), and a spacelike worldline would describe faster-than-light motion with a frame-dependent time order — neither can carry a clock that ticks. So "future-directed timelike unit worldline" is forced by the demand that the observer have a well-defined proper time and a four-velocity. (Later this is enriched with a whole orthonormal frame; for now the worldline and clock suffice to define the rest space.)

Second, what is the observer's *space*? Intuitively it is the set of directions the observer regards as "purely spatial, no time component" — the directions in which simultaneous events lie. By the simultaneity criterion, $M$ is simultaneous with $A$ exactly when $U_0\cdot\overrightarrow{AM} = 0$, so the simultaneous *directions* are precisely the vectors orthogonal to $U_0$. This forces the definition: the local rest space is the orthogonal complement
$$
E_{U_0} \;=\; U_0^\perp \;=\; \{\,X : X\cdot U_0 = 0\,\}.
$$
Three features of this definition are not arbitrary but consequences of the metric, and each would fail for a different choice. Its **dimension is three**: because the metric is non-degenerate, the orthogonal complement of a one-dimensional subspace in four dimensions is three-dimensional — exactly the right number for "space". Were the metric degenerate (the Galilean case), the orthogonal complement could be larger, and "space" and "time" would not split cleanly. Its **vectors are all spacelike**: any nonzero vector orthogonal to a timelike vector is spacelike (a theorem about the indefinite metric, [[Def - Classification of Four-Vectors|classification of four-vectors]]), so the rest space contains no causal directions — you cannot travel within "an instant", as it must be. And it is an **affine hyperplane** when based at $A$: the events simultaneous with $A$ form $A + U_0^\perp$, a flat three-dimensional slice.

Why is the qualifier *local* essential, and not just cautious? Because the simultaneity criterion was derived under the assumption that $M$ is *near* the worldline (so the curvature of $\mathcal{L}_0$ between the radar events could be neglected). For an accelerated observer, the four-velocity rotates along the worldline, so the rest spaces at different proper times are tilted relative to each other and cannot be patched into one global slicing. Concretely, neighbouring rest spaces intersect at a finite distance $\|A_0\|^{-1}$ from the worldline, beyond which the construction folds over. Only for an [[Thm - Nonexistence of Absolute Time|inertial observer]] (zero four-acceleration) is the rest space global. So "local rest space" honestly records that the construction is exact only in a neighbourhood unless the observer is inertial — it is the affine tangent space, at $A$, to the true simultaneity hypersurface $\Sigma_{U_0}(A)$.

The payoff is that "spatial for $\mathcal{O}$" is now a precise, computable subspace, and the entire apparatus of measurement — projection, distance, frames — is built on it. The observer's perceived space is the negative-definite orthogonal complement of their own four-velocity, and everything else in the chapter is what you can do once you have it.

---

# The Definition

**Observer.** An **observer** $\mathcal{O}$ is a future-directed timelike unit worldline $\mathcal{L}_0$ — equivalently, a [[Def - Worldline of a Particle|worldline]] whose [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ satisfies $U_0\cdot U_0 = +1$ and is future-directed — together with an ideal clock measuring [[Def - Proper Time|proper time]] $t$ along $\mathcal{L}_0$ (and, from §6.2 onward, a carried orthonormal [[Def - Local Frame and Four-Rotation|local frame]]).

**Local rest space (vector form).** The **local rest space** of $\mathcal{O}$ at an event $A\in\mathcal{L}_0$ is the orthogonal complement of the four-velocity in the space of displacements:
$$
\boxed{\,E_{U_0}(A) \;=\; U_0(A)^\perp \;=\; \{\,X \in E : X\cdot U_0(A) = 0\,\}\,}.
$$
It is a **three-dimensional vector subspace**, and **all its nonzero vectors are spacelike** ($X\cdot X < 0$). Together with the line $\mathrm{Span}(U_0)$ it spans the whole displacement space:
$$
E \;=\; E_{U_0}(A) \;\overset{\perp}{\oplus}\; \mathrm{Span}\big(U_0(A)\big).
$$

**Local rest space (affine form).** The **affine local rest space** $\mathscr{E}_{U_0}(A)$ is the hyperplane through $A$ directed by $E_{U_0}(A)$:
$$
\mathscr{E}_{U_0}(A) \;=\; \{\,M : U_0(A)\cdot\overrightarrow{AM} = 0\,\}.
$$
By the [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré criterion]], $\mathscr{E}_{U_0}(A)$ is the set of events simultaneous with $A$ for $\mathcal{O}$ — to first order in the displacement from $\mathcal{L}_0$. It is the affine tangent space at $A$ to the exact **simultaneity hypersurface** $\Sigma_{U_0}(A)$, and the two coincide globally precisely when the observer is **inertial** (four-acceleration $A_0 = 0$) — see [[Thm - Nonexistence of Absolute Time]] and the locality discussion below. The dependence on proper time may be written $E_{U_0}(t)$, $\mathscr{E}_{U_0}(t)$.

---

# Categorical / Structural Definition

Structurally, the assignment $A \mapsto E_{U_0}(A)$ is a **distribution** along the worldline — a smoothly varying choice of three-dimensional subspace of the displacement space at each event — namely the kernel of the one-form $\underline{U_0} = g(U_0, \cdot)$ obtained by lowering the four-velocity. The rest space is $\ker\underline{U_0}$, and the projector onto it is built from $\underline{U_0}$. This is the flat-spacetime, single-worldline case of the general construction in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]]: a timelike unit vector field $U_0$ on (a region of) spacetime defines at each point the orthogonal three-plane $\ker\underline{U_0}$, and the question of whether these planes fit together into a foliation by hypersurfaces — whether the distribution is *integrable* — is governed by the Frobenius theorem. The distribution is integrable (so the local rest spaces patch into global simultaneity surfaces) exactly when $\underline{U_0}\wedge d\underline{U_0} = 0$, which for a single observer's congruence reduces to the vanishing of the four-rotation. This is the geometric content of "local": a non-integrable orthogonal distribution has no global slicing, and a rotating observer's rest spaces famously fail to integrate — the Sagnac/Ehrenfest phenomenon.

The pair (worldline, four-velocity) with its orthogonal complement is also the local model of a **point in the velocity space** of relativity: the future-directed unit timelike vectors form one sheet of a hyperboloid (a model of hyperbolic three-space), and $U_0$ is a point on it whose tangent space at that point is canonically the rest space $U_0^\perp$. The Lorentz group acts on this hyperboloid by isometries, moving one observer's $U_0$ to another's and carrying rest space to rest space.

---

# Relate to Other Fields / Compression

The local rest space is the relativistic version of the **instantaneous rest frame** of Newtonian mechanics, made coordinate-free: instead of "the frame momentarily co-moving with the particle", it is the metric orthogonal complement of the four-velocity, an intrinsic subspace of spacetime. In the $3+1$ formulation of general relativity it becomes the **spatial slice** seen by a family of observers, and the projector onto it is the central tool of that formalism. In gauge-theoretic language, choosing $U_0$ at each event and projecting onto $U_0^\perp$ is a **reduction** of the tangent-space structure group from the Lorentz group to the rotation group $SO(3)$ that fixes $U_0$ — the same reduction that, in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]], underlies the split of spacetime tensors into "energy density, momentum density, stress" as measured by a chosen observer.

**True name:** the local rest space is *the orthogonal complement of the four-velocity*, $U_0^\perp$ — and operationally, *the directions in which simultaneous events lie*. The first form is what you compute with (it is $\ker\underline{U_0}$, and $\Pi$ projects onto it); the second is what it means physically (the observer's instantaneous space).

---

# Examples / Corollaries

**Is an instance — the rest space of an inertial observer.** For an observer at rest in an inertial frame, $U_0 = (1, 0, 0, 0)$ (the time axis), and $U_0^\perp = \{(0, x^1, x^2, x^3)\}$ is the purely spatial hyperplane — the usual "space at a fixed time". Here the rest space is *global*: the same construction at every proper time gives the parallel hyperplanes $t = \mathrm{const}$, which foliate all of spacetime.

**Is an instance — the tilted rest space of a boosted observer.** For an observer moving at velocity $v$ along $x$, $U_0 = \gamma(1, v, 0, 0)$, and $U_0^\perp$ is spanned by $(v, 1, 0, 0)$ together with the transverse $e_2, e_3$. The first generator is tilted toward the light cone by the same rapidity as the worldline — this tilt is the relativity of simultaneity drawn on a spacetime diagram.

**Is NOT an instance — the worldline tangent itself.** The four-velocity $U_0$ is *not* in the rest space: $U_0\cdot U_0 = +1 \ne 0$, so $U_0\notin U_0^\perp$. The rest space contains no timelike direction at all; it is purely spatial. This is the calibration that the rest space is the *orthogonal complement*, not the whole space.

**Is NOT an instance — a null hyperplane.** The hyperplane orthogonal to a *null* vector $N$ (with $N\cdot N = 0$) is degenerate: it *contains* $N$ (since $N\cdot N = 0$), and the metric restricted to it is degenerate, not Euclidean. This is why the rest-space construction needs a *timelike* four-velocity: only then is the orthogonal complement spacelike and Euclidean. A photon has no rest space.

**Corollary — the rest space is three-dimensional and spacelike.** Because $\eta$ is non-degenerate and $U_0$ is timelike, $\dim U_0^\perp = 4 - 1 = 3$, and every nonzero $X\in U_0^\perp$ has $X\cdot X < 0$ (orthogonal to timelike $\Rightarrow$ spacelike). Thus $(E_{U_0}, -g)$ is a candidate Euclidean three-space — confirmed in [[Thm - Euclidean Character of the Local Rest Space]].

**Calibration check.** You should be able to: (1) write down $U_0^\perp$ explicitly for $U_0 = \gamma(1, \mathbf{v})$ and check its three basis vectors are spacelike and orthogonal to $U_0$; (2) explain why a null or spacelike worldline cannot be an observer's worldline (no proper time / no ticking clock); and (3) say in one sentence why the rest space is "local" for an accelerated observer (the four-velocity rotates, so neighbouring rest spaces tilt and fail to patch globally).

---

# Unlocked by This

> [!tip] The Orthogonal Projector and the Euclidean Rest Space *(from §6.1)*
> With the rest space defined as $U_0^\perp$, the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] $\Pi(X) = X - (X\cdot U_0)U_0$ resolves every vector into a spatial part (in $U_0^\perp$) and a time part (along $U_0$), and the [[Thm - Euclidean Character of the Local Rest Space|Euclidean character]] makes $U_0^\perp$ an ordinary three-dimensional Euclidean space under the spatial metric $h = -g|_{U_0^\perp}$.

> [!tip] Relative Velocity and the Kinematics of Particles *(from Kinematics)*
> The velocity of a particle *relative to* $\mathcal{O}$ is built by decomposing the particle's four-velocity $U$ as $U = \gamma(U_0 + V)$ with $V\in U_0^\perp$ the relative velocity — projecting onto the rest space is exactly how an observer extracts an ordinary three-velocity from a four-velocity in [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

> [!tip] The Local Frame and Observer Coordinates *(from §6.2)*
> Equipping the rest space with an orthonormal triad $e_1, e_2, e_3$ promotes it from an abstract subspace to a coordinate grid: the [[Def - Local Frame and Four-Rotation|local frame]] $(e_\alpha)$ with $e_0 = U_0$ furnishes coordinates $(t, x^i)$ for nearby events and a fixed Euclidean reference space, completing the definition of an observer who can both date and locate.

> [!tip] Inertial Observers and Global Simultaneity *(from the Poincaré group)*
> An observer whose rest spaces patch into a *global* foliation — whose simultaneity is observer-wide rather than merely local — is exactly an **inertial observer**, characterised by zero four-acceleration; this globality is the geometric content of [[Special Relativity XII — Inertial Observers and the Poincaré Group]] and the reason inertial frames carry a single time coordinate.
