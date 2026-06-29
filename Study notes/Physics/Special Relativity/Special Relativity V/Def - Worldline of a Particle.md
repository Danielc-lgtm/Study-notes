---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Classification of Four-Vectors"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a vector $X$ is **timelike** when $X \cdot X > 0$, **spacelike** when $X \cdot X < 0$, and **null** when $X \cdot X = 0$. Points of Minkowski space $\mathbb{M}$ are **events**; in an inertial frame an event has coordinates $x^\mu = (t, x, y, z)$, $\mu = 0,1,2,3$, with $x^0 = t$. A curve is written $\mathcal{L}$, parametrised by a real parameter $\lambda$ through a map $\varphi : \lambda \mapsto A = \varphi(\lambda)$; its tangent vector is $V(\lambda) = dX/d\lambda$ with components $V^\mu = dx^\mu/d\lambda$. Spatial three-vectors are bold, $\mathbf{v}$. Full registry on [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

> [!warning] Convention
> Gourgoulhon, whose Chapter 2 this page follows, uses the opposite (**mostly-plus**) signature $\mathrm{diag}(-1,+1,+1,+1)$, in which a timelike vector has $g(v,v) < 0$ and a worldline tangent obeys $\vec{v} \cdot \vec{v} < 0$. We have flipped the overall sign of the metric, so for us the defining condition of a massive worldline is $V \cdot V > 0$, not $< 0$. Be careful when reading the source: every "timelike $\Leftrightarrow$ negative norm" there becomes "timelike $\Leftrightarrow$ positive norm" here.

---

# Axiom Motivation

Special relativity is a non-quantum theory, so a particle is idealised exactly as in classical mechanics: a point. The word *particle* covers both a genuine elementary particle and any physical system whose spatial extent is negligible at the scale of the phenomenon under study — a planet in its orbit, an atom in a beam, an astronaut in a spaceship. The question this page answers is: what mathematical object represents such a particle in the spacetime of [[Def - Minkowski Space and the Metric|Minkowski space]]?

The naive answer — "a point, moving in time" — secretly smuggles back the Newtonian splitting of spacetime into space and time. To say "the particle is at position $\mathbf{x}$ *at time* $t$" presupposes a meaning for "at a given instant", and that meaning is precisely the absolute simultaneity that relativity has destroyed (see [[Def - Inertial Frame and the Postulates of Special Relativity|the postulates]]). If we wish to keep the mixed space–time character of $\mathbb{M}$ and not pre-split it into a space part and a time part, we cannot describe the particle one instant at a time. We must describe it *all at once*, by its entire history. That history — the set of all events the particle ever occupies — is a one-dimensional curve in $\mathbb{M}$, and it is this curve, not any momentary point, that is the primary object. We call it the **worldline**.

So far this is just geometry; the physics enters in a single constraint on *which* curves are allowed. A massive particle cannot travel at or above the speed of light, which on a spacetime diagram means its worldline must everywhere be steeper than a light ray. The frame-independent way to say "steeper than light" is to demand that the tangent vector at every point be **timelike**: $V \cdot V > 0$. This is the bridge between the physics of "nothing outruns light" and the geometry of the curve. A curve all of whose tangents are timelike is exactly a curve that stays inside the [[Def - Photons and Null Geodesics|light cone]] of each of its points, and that is the precise geometric content of causality. The model is the displacement between two events: an infinitesimal step $d\vec{x}$ along the worldline is a future-directed timelike [[Def - Four-Vector|four-vector]].

Why insist that the tangent be timelike *everywhere*, rather than merely "on average"? Because the type of a vector — timelike, null, spacelike — is a pointwise, [[Thm - Invariance of the Spacetime Interval|Lorentz-invariant]] fact, and there is no consistent relativistic theory in which a worldline changes type partway along. A curve whose tangent were timelike on one stretch and spacelike on another would describe a particle that accelerates past the speed of light and back, and such a particle could be made, by a suitable choice of frame, to travel backward in time over the spacelike stretch — destroying causality. So the three kinds of worldline are mutually exclusive and exhaustive: always timelike (ordinary **massive** particles, this page), always null (photons and other massless particles, [[Def - Photons and Null Geodesics]]), or always spacelike (the hypothetical faster-than-light **tachyons**, which have no consistent dynamics and are excluded). If one weakened the requirement to "piecewise timelike or null", one would admit worldlines with null segments — but a null segment is a photon's history, not a massive particle's, and the proper-time machinery of the next pages breaks down on it.

One technical demand remains: smoothness. We require the worldline to be **piecewise twice continuously differentiable** ($C^2$ on each piece of a finite subdivision). Twice, because we shall want not only a velocity (one derivative) but an acceleration (two derivatives); piecewise, because a real particle can change its acceleration abruptly — a rocket can fire its engine, reversing thrust at an instant — and we do not want to outlaw that. The corners where the acceleration jumps are isolated; between them the curve is honestly $C^2$.

---

# The Definition

A **worldline** of a massive particle is a piecewise twice continuously differentiable curve $\mathcal{L}$ of Minkowski space $(\mathbb{M}, \eta)$ such that every vector tangent to $\mathcal{L}$ is **timelike** (future-directed):
$$
V \cdot V \;=\; \eta_{\mu\nu} V^\mu V^\nu \;>\; 0 \qquad \text{at every point of } \mathcal{L}.
$$
Concretely, a **parametrisation** of $\mathcal{L}$ is an injective map
$$
\varphi : \mathbb{R} \supseteq I \longrightarrow \mathbb{M}, \qquad \lambda \longmapsto A = \varphi(\lambda),
$$
that is $C^2$ on each interval of a finite subdivision of its domain and whose image is $\mathcal{L} = \varphi(I)$. The associated **field of tangent vectors** is
$$
V(\lambda) \;=\; \frac{d\vec{x}}{d\lambda} \;=\; \frac{dx^\mu}{d\lambda}\, e_\mu,
$$
where $d\vec{x}$ is the infinitesimal displacement from $\varphi(\lambda)$ to $\varphi(\lambda + d\lambda)$ and $(e_\mu)$ is the coordinate basis of an inertial frame. The defining timelike condition is $V(\lambda) \cdot V(\lambda) > 0$ for all $\lambda$.

A given worldline admits **infinitely many parametrisations**: if $\varphi$ is one and $f : \mathbb{R} \to \mathbb{R}$ is any $C^2$ bijection, then $\tilde{\varphi} = \varphi \circ f$ is another, with tangent field rescaled by $df/d\lambda$. A bare parametrisation is therefore a purely mathematical choice carrying no physics. The next page singles out a canonical, physics-bearing parameter — the [[Def - Proper Time|proper time]] $\tau$, the elapsed time read by a clock carried along $\mathcal{L}$ — which is intrinsic to the worldline and independent of any parametrisation.

A **massless particle** (a photon) is *not* a worldline in this sense: its tangent is null, $V \cdot V = 0$, not timelike. Its history is a [[Def - Photons and Null Geodesics|null geodesic]], treated separately.

---

# Categorical / Structural Definition

A worldline is, structurally, a **timelike immersed curve** in the pseudo-Riemannian manifold $(\mathbb{M}, \eta)$ — the flat, constant-metric special case. An immersed curve is the image of a map $\varphi : I \to \mathbb{M}$ whose derivative never vanishes (so it has a well-defined tangent line at each point); "timelike" restricts the tangent line to lie inside the light cone. The set of parametrisations of a fixed worldline is a torsor under the group of $C^2$ orientation-preserving reparametrisations of the interval, $\mathrm{Diff}^2_+(I)$: any two parametrisations differ by composition with such a diffeomorphism, and no parametrisation is canonical until extra structure (the metric, giving arc length) is used to break the symmetry.

This places the worldline in the same frame as a curve in Riemannian geometry, with one decisive difference. In a [[Def - Riemannian Metric|Riemannian]] manifold every immersed curve has a well-defined, always-positive arc length, and the arc-length parametrisation is the canonical one. Here the metric is indefinite, so arc length is real and positive only for *timelike* curves, where it is the [[Def - Proper Time|proper time]]; the canonical parameter exists for exactly the curves this definition admits. The generalisation to curved spacetime is immediate and is the entire kinematic substrate of general relativity: a worldline there is a timelike curve in a Lorentzian manifold $(M, g)$, the metric $\eta$ replaced by a position-dependent $g_{\mu\nu}(x)$, and the freely-falling worldlines become the timelike **geodesics** of $g$.

---

# Relate to Other Fields / Compression

A worldline is the relativistic replacement for the pair "trajectory $\mathbf{x}(t)$ + clock $t$" of Newtonian mechanics, fused into a single geometric object. In the Newtonian picture the trajectory lives in space $\mathbb{R}^3$ and time is an external, universal parameter ticking alongside it; the splitting is absolute. Relativity forbids the splitting — there is no universal $t$ — and the repair is to graph the trajectory *against* time inside one four-dimensional space, producing a curve. The "trajectory in space at successive times" becomes "a curve in spacetime", and the absolute external clock is replaced by the metric arc length along the curve.

**True name:** a worldline is *a timelike curve in Minkowski space, considered up to reparametrisation, with the metric arc length $\tau$ as its intrinsic clock.* What makes it operational is the last clause: you stop thinking of the particle as a point that moves and start thinking of it as a fixed one-dimensional locus in $\mathbb{M}$, on which the metric installs a god-given ruler (proper time). Every kinematic quantity — [[Def - Four-Velocity and Four-Acceleration|four-velocity, four-acceleration]] — is then a derivative with respect to that ruler, and is automatically a genuine four-vector because the ruler is frame-independent.

In differential geometry this is the statement that a worldline is an integral curve of a future-timelike vector field, and the proper-time parametrisation is its arc-length (affine) parametrisation. In the calculus of variations it is a competitor in the variational problem "extremise $\int d\tau$", whose extremals are the inertial worldlines ([[Thm - Inertial Worldlines Maximise Proper Time]]). In dynamical-systems language a parametrised worldline is a solution curve of the equation of motion $dU/d\tau = A$, with $A$ the four-acceleration supplied by the forces.

---

# Examples / Corollaries

**Is an instance — an inertial particle.** A free particle moving at constant velocity $\mathbf{v}$ (with $|\mathbf{v}| < 1$) has the straight worldline $x^\mu(\lambda) = x_0^\mu + \lambda\, U^\mu$ with $U^\mu = \gamma(1, \mathbf{v})$ and $\gamma = (1 - \mathbf{v}^2)^{-1/2}$. Its tangent is the constant vector $U$, with $U \cdot U = \gamma^2(1 - \mathbf{v}^2) = 1 > 0$, timelike everywhere. This is the simplest worldline — a straight line — and it is the relativistic statement of Newton's first law.

**Is an instance — an accelerated particle (hyperbolic motion).** A particle undergoing constant proper acceleration $a$ along $x$ traces an arc of a hyperbola, $t(\lambda) = a^{-1}\sinh(a\lambda)$, $x(\lambda) = a^{-1}\cosh(a\lambda)$ (with $\lambda = \tau$ the proper time). Its tangent $V = (\cosh a\tau, \sinh a\tau, 0, 0)$ has $V \cdot V = \cosh^2 - \sinh^2 = 1 > 0$, timelike everywhere, so this is a legitimate worldline despite the unbounded coordinate velocity approaching $1$. Such worldlines appear throughout the [[Ex - The twin paradox|twin paradox]] and in [[Special Relativity XVI — Accelerated Observers|accelerated-observer]] problems.

**Is NOT an instance — a light ray.** The straight line $x^\mu(\lambda) = \lambda(1, 1, 0, 0)$ has tangent $(1,1,0,0)$ with norm $1 - 1 = 0$: null, not timelike. This is a photon's history, a [[Def - Photons and Null Geodesics|null geodesic]], excluded from the definition. The proper time along it vanishes — a clock carried by a photon would be frozen — which is exactly why photons need separate treatment.

**Is NOT an instance — a tachyon worldline.** The line $x^\mu(\lambda) = \lambda(1, 2, 0, 0)$ has tangent norm $1 - 4 = -3 < 0$: spacelike, a faster-than-light trajectory. No massive particle follows it; admitting it would let a suitable observer see the particle travel backward in time. Spacelike worldlines are excluded.

**Is NOT an instance — a type-changing curve.** A curve whose tangent is timelike on $\lambda < 0$ and spacelike on $\lambda > 0$ is not a worldline of any single particle; the type must be constant along the whole curve. This is not a smoothness failure but a physical one: there is no relativistic process that accelerates a massive particle through the speed of light.

**Corollary — a null tangent does not require a straight line.** A *null geodesic* is straight, but a general *null curve* need not be: the helix $x^0(\lambda) = r\lambda$, $x^1(\lambda) = r\cos\lambda$, $x^2(\lambda) = r\sin\lambda$, $x^3(\lambda) = 0$ has tangent $(r, -r\sin\lambda, r\cos\lambda, 0)$ with norm $r^2 - r^2\sin^2\lambda - r^2\cos^2\lambda = 0$, null at every point, yet the curve is not a straight line. (It is, however, not the history of a free photon, which must be straight.) The analogous timelike statement — that a worldline can curve while staying timelike — is what makes acceleration possible.

**Calibration check.** You have understood the definition if you can: (i) given a parametrised curve $x^\mu(\lambda)$, compute the tangent $V^\mu = dx^\mu/d\lambda$ and classify the curve by the sign of $V \cdot V$; (ii) explain why $x^\mu(\lambda) = \lambda(1, 1, 0, 0)$ is excluded while $x^\mu(\lambda) = \lambda(2, 1, 0, 0)$ is admitted; and (iii) state why the worldline, not the instantaneous position, is the primary object — because "the position now" presupposes a frame-dependent notion of simultaneity.

---

# Unlocked by This

> [!tip] Proper Time as Metric Arc Length *(from this chapter)*
> A worldline is a curve, and the [[Def - Minkowski Space and the Metric|metric]] measures the "length" of a curve. For a timelike worldline that length is the **proper time** ([[Def - Proper Time]]) — the time a clock actually accumulates as it travels along $\mathcal{L}$. This is the single most important construction unlocked here, and it is the seed of the geodesic principle of gravitation.

> [!tip] Four-Velocity and Four-Acceleration *(from this chapter)*
> Once the proper time gives the worldline an intrinsic clock, differentiating the four-position with respect to it produces the **four-velocity** $U = dX/d\tau$ and, again, the **four-acceleration** $A = dU/d\tau$ ([[Def - Four-Velocity and Four-Acceleration]]) — both genuine four-vectors, because $\tau$ is a Lorentz scalar.

> [!tip] The Geodesic and the Curved-Spacetime Worldline *(from General Relativity)*
> The worldline survives the passage to gravitation essentially unchanged: in a curved spacetime $(M, g)$ a massive particle still follows a timelike curve, and a *freely-falling* one follows a timelike **geodesic** — the curve that extremises proper time, $\delta\int d\tau = 0$. The flat-space straight worldline of an inertial particle ([[Thm - Inertial Worldlines Maximise Proper Time]]) is the $g = \eta$ special case. What changes is only that "straightest possible" must be defined intrinsically, through the **connection** built from $g_{\mu\nu}(x)$, giving the **geodesic equation** $\dfrac{dU^\mu}{d\tau} + \Gamma^\mu{}_{\nu\rho}U^\nu U^\rho = 0$; in flat space the Christoffel symbols $\Gamma$ vanish and this collapses to $dU^\mu/d\tau = 0$. The entire kinematic apparatus of this chapter — worldline, proper time, four-velocity, four-acceleration — transfers verbatim to general relativity, which is why setting it up frame-independently here is the right preparation for gravity.
