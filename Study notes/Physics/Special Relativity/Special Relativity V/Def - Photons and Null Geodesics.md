---
type: definition
subject: special-relativity
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - Worldline of a Particle"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a vector $X$ is **null** (lightlike) when $X \cdot X = 0$, timelike when $X \cdot X > 0$, spacelike when $X \cdot X < 0$. Points are events; an inertial frame gives coordinates $x^\mu = (t, x, y, z)$. A photon's worldline is a curve $\mathcal{L}$; its tangent (direction) vector is $V$. An event is $A$; its light cone is $\mathcal{I}(A)$, with future and past sheets $\mathcal{I}^+(A)$, $\mathcal{I}^-(A)$. An **affine parameter** along the null worldline is $\lambda$. Full registry on [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

> [!warning] Convention
> A null vector has the *same* defining condition $V \cdot V = 0$ in both signature conventions, since $0 = -0$; this is the one place where Gourgoulhon's mostly-plus and our mostly-minus agree without translation. The light-cone equation, however, flips sign: Gourgoulhon writes $-(x^0)^2 + (x^1)^2 + (x^2)^2 + (x^3)^2 = 0$, which for us is $(x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2 = 0$ — the same cone.

---

# Axiom Motivation

The previous pages built the kinematics of **massive** particles: their worldlines are timelike, they carry a [[Def - Proper Time|proper time]], and they have a [[Def - Four-Velocity and Four-Acceleration|four-velocity]]. But the particle whose behaviour forced relativity into existence — the photon — is exactly the one that breaks all of this machinery. A photon travels at the speed of light in every frame, so its worldline is *not* timelike; and "the speed of light" is the boundary case where the proper-time construction degenerates. This page is the repair: it defines the photon's history directly, as a curve, and identifies the structure that replaces proper time and four-velocity.

Start from what a photon's worldline must look like. On a spacetime diagram it travels at $45^\circ$ — at speed $1$ — so an infinitesimal step $d\vec{x}$ along it has $dt = |d\mathbf{x}|$, giving $ds^2 = dt^2 - d\mathbf{x}^2 = 0$. The tangent vector is therefore **null**: $V \cdot V = 0$. This is the defining geometric fact, and it is frame-independent because the [[Thm - Invariance of the Spacetime Interval|interval is invariant]] — a worldline that is null in one frame is null in all, which is the precise restatement of "light travels at $c$ for everybody". So a photon is represented by a *null* curve, just as a massive particle is represented by a *timelike* one. The qualifier "lightlike" for null vectors of the metric is justified exactly here: null directions are the directions light propagates, and one verifies in the [[Special Relativity XXII — Maxwell's Equations|theory of electromagnetism]] that the wave solutions of Maxwell's equations in vacuum do propagate along null directions of $\eta$.

But there is a sharper constraint: a free photon's worldline is not merely null, it is a **straight line**. Whereas massive particles follow a great variety of timelike curves (any curve with timelike tangents is allowed), a free photon in vacuum is compelled to follow a very specific kind of curve — a null *straight line*, called a **null geodesic**. This is a genuine extra postulate, the massless analogue of "free massive particles move in straight lines": a free photon moves uniformly in a fixed null direction. The distinction between a null *curve* and a null *geodesic* is real and worth making precise, because not every null curve is straight: one can write down null curves that bend (an example below), and these are *not* the histories of free photons.

Now the degeneration. Proper time is $\int\sqrt{ds^2}$, and along a null worldline $ds^2 = 0$ identically, so $\tau \equiv 0$: **proper time does not advance for a photon.** A clock carried by a photon would be frozen — no time elapses along a light ray. This is not a small technicality but a structural fact: the proper-time machinery, which made $dX/d\tau$ a four-vector, is simply unavailable, because dividing by $d\tau = 0$ is meaningless. Consequently a photon has **no four-velocity**: there is no unit tangent vector to normalise, because a null vector has *zero* norm, not unit norm — you cannot rescale a null vector to have $V \cdot V = 1$, since rescaling multiplies the norm by a positive factor and $0$ stays $0$. The four-velocity, defined as the unique unit timelike tangent, has no null counterpart.

What replaces proper time as a parameter? Since arc length is identically zero, it cannot parametrise the curve; one needs a different distinguished parameter. The answer is an **affine parameter** $\lambda$: a parameter along the null geodesic in which the tangent $V = dX/d\lambda$ is *parallel-transported* (constant, in flat space), so that the worldline is "as straight as possible" and $dV/d\lambda = 0$. An affine parameter is determined up to an affine reparametrisation $\lambda \mapsto a\lambda + b$ (whence the name), and it is the right substitute: it exists for null geodesics exactly as proper time exists for timelike geodesics, and in the curved-spacetime generalisation it is what the geodesic equation is written in terms of. Physically, the natural affine parameter is supplied by the photon's [[Def - The Four-Momentum of a Photon|four-momentum]] $P^\mu = dX^\mu/d\lambda$, which is null ($P \cdot P = 0$) and is the object through which a photon enters every conservation law on the same footing as a massive particle.

---

# The Definition

In vacuum, a **massless particle** — and in particular a **photon** — is represented by a **straight line** $\mathcal{L}$ of Minkowski space $\mathbb{M}$ whose direction vector is a **null** vector of the metric:
$$
V \cdot V \;=\; \eta_{\mu\nu} V^\mu V^\nu \;=\; 0, \qquad V \ne 0.
$$
Such a line is called a **null geodesic** of spacetime. If the particle is a photon, $\mathcal{L}$ is also called a **light ray**.

Because $V \cdot V = 0$, the [[Def - The Spacetime Interval|interval]] along $\mathcal{L}$ vanishes, $ds^2 = 0$, so the [[Def - Proper Time|proper time]] is identically zero and **cannot parametrise** the worldline. The null geodesic is instead parametrised by an **affine parameter** $\lambda$, in which the tangent vector $V = dX/d\lambda$ is constant (parallel-transported):
$$
\frac{dV^\mu}{d\lambda} \;=\; 0,
$$
determined up to the affine freedom $\lambda \mapsto a\lambda + b$ ($a > 0$). The natural affine parameter is fixed by setting the tangent equal to the photon's null [[Def - The Four-Momentum of a Photon|four-momentum]], $P^\mu = dX^\mu/d\lambda$, with $P \cdot P = 0$. A massless particle has **no four-velocity** (there is no unit null vector) and **no rest mass** ($m = 0$).

A more general **null curve** is a curve of $\mathbb{M}$ all of whose tangent vectors are null, *without* requiring straightness. Every null geodesic is a null curve, but not conversely. A free photon follows a null *geodesic*; null curves that are not geodesics are not the histories of free photons.

**Light cone.** The set of all photon worldlines through a fixed event $A$ — every light ray passing through, emitted at, or received at $A$ — forms the **light cone** of $A$:
$$
\mathcal{I}(A) \;=\; \big\{\, M \in \mathbb{M} \ :\ \overrightarrow{AM} \cdot \overrightarrow{AM} = 0 \,\big\},
\qquad\text{i.e. } (x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2 = 0
$$
in inertial coordinates centred on $A$. It is a three-dimensional cone with apex $A$, with a **future sheet** $\mathcal{I}^+(A)$ (forward in time) and a **past sheet** $\mathcal{I}^-(A)$. The cone separates the events related to $A$ by a **timelike** vector (inside, causally connectible to $A$) from those related by a **spacelike** vector (outside, causally disconnected). The light cone depends only on the event $A$, not on any worldline through it, and the light cones of different events differ by a mere translation.

---

# Categorical / Structural Definition

A null geodesic is a **null geodesic of the Lorentzian manifold** $(\mathbb{M}, \eta)$ in the flat case: an affinely-parametrised curve $\lambda \mapsto X(\lambda)$ with null tangent satisfying the geodesic equation $\nabla_V V = 0$, which in flat inertial coordinates is $d^2 X^\mu/d\lambda^2 = 0$ — a straight line. The three classes of geodesic in a Lorentzian manifold are timelike, null, and spacelike, exactly mirroring the [[Def - Classification of Four-Vectors|classification of four-vectors]] by the sign of the tangent's norm; null geodesics are the borderline case, the worldlines of massless particles.

The structural reason a null geodesic carries an affine parameter but not an arc-length parameter is that the metric arc-length functional $\int\sqrt{|g(\dot X, \dot X)|}\,d\lambda$ is **degenerate** on null curves (its integrand vanishes), so it cannot single out a parameter; the geodesic *equation* $\nabla_V V = 0$, by contrast, is non-degenerate and determines the parameter up to affine freedom. This is why the variational characterisation of geodesics splits: timelike geodesics are critical points (in fact maxima, [[Thm - Inertial Worldlines Maximise Proper Time]]) of proper time, but null geodesics are not critical points of any length functional — they are characterised purely by the affine-geodesic equation, or equivalently as the curves of *minimal* (zero) metric length connecting their endpoints.

In the bundle picture the light cone at an event $A$ is the **null cone of the tangent space** $T_A\mathbb{M}$, the zero locus of the quadratic form $\eta$; the assignment $A \mapsto \mathcal{I}(A)$ is the *conformal structure* of spacetime. Indeed, null geodesics and the light-cone field depend on the metric only up to an overall positive rescaling $\eta \mapsto \Omega^2(x)\,\eta$ — they are **conformally invariant**, which is the deep reason massless particles see only the causal (conformal) structure of spacetime and not its full metric.

---

# Relate to Other Fields / Compression

The photon is the **degenerate ($m \to 0$) limit** of a massive particle, and the right way to think of it is as the boundary of the theory rather than an exception to it. A massive particle has timelike four-momentum $P \cdot P = m^2 > 0$; a (hypothetical) tachyon would have spacelike $P \cdot P < 0$; the photon sits exactly on the dividing null cone, $P \cdot P = 0$. Everything that needed the four-velocity is rephrased in terms of the four-momentum, which the photon has; the magnitude of that four-momentum, which the proper-time construction would have fixed for a massive particle, is instead supplied by quantum mechanics through $E = \hbar\omega$.

**True name:** a photon is *a null straight line carrying a null four-momentum*, parametrised by an affine parameter, with no proper time and no four-velocity. The operational reflex is: whenever a calculation contains a photon, its four-momentum squares to **zero**, $P_\gamma \cdot P_\gamma = 0$, which is an even more powerful simplifier than the massive mass-shell relation — the term simply drops out when you square.

In differential geometry null geodesics are the integral curves of the conformal (causal) structure; in optics they are the rays of geometric optics (the eikonal/Hamilton–Jacobi limit of wave propagation), which is the precise sense in which "light ray" is literal. In the conformal field theory and causal-set programmes, the light-cone field $A \mapsto \mathcal{I}(A)$ — not the metric — is taken as the primitive datum, and the metric is reconstructed from it up to a conformal factor. The light cone is also the carrier of **causality**: $A$ can influence $B$ only if $B$ lies on or inside $\mathcal{I}^+(A)$.

---

# Examples / Corollaries

**Is an instance — a light ray along $x$.** The line $x^\mu(\lambda) = (\lambda, \lambda, 0, 0)$ has tangent $V = (1,1,0,0)$ with $V \cdot V = 1 - 1 = 0$: null, and straight, so it is a null geodesic — a photon moving in the $+x$ direction at speed $1$. Its four-momentum is $P^\mu = E(1,1,0,0)$ for a photon of energy $E$, with $P \cdot P = 0$.

**Is an instance — the light cone of the origin.** The future light cone $\mathcal{I}^+(0)$ is the set $\{(t, \mathbf{x}) : t = |\mathbf{x}|,\ t > 0\}$, the union of all forward null rays from the origin. A flash of light emitted at the origin reaches exactly the events on $\mathcal{I}^+(0)$.

**Is NOT an instance — a timelike worldline.** A massive particle moving at speed $u < 1$ has tangent $(1, \mathbf{u})$ with norm $1 - u^2 > 0$: timelike, not null. It is *not* a null geodesic; it carries a proper time and a four-velocity, and travels strictly inside the light cone.

**Is NOT an instance — a bending null curve.** The helix $x^0(\lambda) = r\lambda$, $x^1(\lambda) = r\cos\lambda$, $x^2(\lambda) = r\sin\lambda$, $x^3(\lambda) = 0$ (with $r > 0$) has tangent $(r, -r\sin\lambda, r\cos\lambda, 0)$ and norm $r^2 - r^2\sin^2\lambda - r^2\cos^2\lambda = 0$: null at every point. So it is a null *curve* — but it is not a straight line, hence **not a null geodesic**, and it is not the history of a free photon. (It illustrates that "all tangents null" is weaker than "null geodesic".)

**Corollary — no clock keeps time along a light ray.** Since $ds^2 = 0$ along any null worldline, $\tau = \int\sqrt{ds^2} = 0$: a clock carried by a photon registers no elapsed time between any two events on its path. "From the photon's point of view" no time passes — though strictly there is no photon rest frame, so the phrase is heuristic.

**Corollary — light cones tile spacetime by translation.** Because the cone equation $\overrightarrow{AM} \cdot \overrightarrow{AM} = 0$ depends only on the *difference* $\overrightarrow{AM}$, the light cone of any event $B$ is the light cone of $A$ shifted by $\overrightarrow{AB}$. All light cones are parallel — a fact that, in [[Special Relativity I — Postulates and Lorentz Transformations|flat spacetime]], forbids closed timelike curves and hence time travel to the past; in curved spacetime the cones tilt from event to event, and the prohibition can fail.

**Calibration check.** You have understood the definition if you can: (i) verify that $(\lambda, \lambda, 0, 0)$ is a null geodesic but $(\lambda, 2\lambda, 0, 0)$ and $(\lambda, \tfrac12\lambda, 0, 0)$ are not (one spacelike, one timelike); (ii) explain why a photon has no proper time and no four-velocity but does have a null four-momentum; and (iii) write the light-cone equation of an event and state why all light cones are parallel translates.

---

# Unlocked by This

> [!tip] The Four-Momentum of a Photon *(from Energy and Momentum)*
> A photon has no four-velocity, but it carries a **null four-momentum** $P^\mu = (E, \mathbf{p})$ with $P \cdot P = 0$, equivalently $E = |\mathbf{p}|$ ([[Def - The Four-Momentum of a Photon]]). Quantum mechanics supplies its magnitude through $E = \hbar\omega$ and $P^\mu = \hbar K^\mu$, tying it to the wave's frequency four-vector. With this one object the photon enters [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] exactly as a massive particle does — the basis of Compton scattering, pair production, and the relativistic Doppler effect.

> [!tip] Causal Structure and the Light Cone *(from this chapter and Observers)*
> The light cone is the carrier of **causality**: event $A$ can influence event $B$ only if $B$ lies on or inside $\mathcal{I}^+(A)$, i.e. $\overrightarrow{AB}$ is future timelike or null. Because the cone is [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]], all observers agree on this causal relation, even though they disagree on the time-ordering of spacelike-separated events. This is the geometric origin of the prohibition on faster-than-light signalling.

> [!tip] Null Geodesics and the Conformal Structure of Spacetime *(from General Relativity)*
> In a curved spacetime light still follows **null geodesics** — now of the curved metric $g$ — and the light-cone field $A \mapsto \mathcal{I}(A)$ becomes the **conformal structure**, the metric up to a position-dependent positive factor $\Omega^2(x)$. Because null geodesics and light cones are conformally invariant, massless particles probe only this causal skeleton, not the full metric: gravitational lensing is the bending of null geodesics by curvature, black-hole horizons are surfaces where the future light cones tip inward, and the causal (Penrose) diagrams that classify spacetimes are drawn entirely from the light-cone field. The affine parameter introduced here is exactly the parameter in which the curved null-geodesic equation $\nabla_V V = 0$ is written.
