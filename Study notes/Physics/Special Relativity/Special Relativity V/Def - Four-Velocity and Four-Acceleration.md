---
type: definition
subject: special-relativity
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Vector"
  - "Def - Worldline of a Particle"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X \cdot X > 0$. A worldline is $\mathcal{L}$; its four-position is $X^\mu(\tau) = (t(\tau), \mathbf{x}(\tau))$, parametrised by [[Def - Proper Time|proper time]] $\tau$. In an inertial frame the particle has three-velocity $\mathbf{u} = d\mathbf{x}/dt$, speed $u = |\mathbf{u}|$, and Lorentz factor $\gamma = (1 - u^2)^{-1/2}$, with $dt/d\tau = \gamma$. The four-velocity is $U$, the four-acceleration $A$; their components are $U^\mu, A^\mu$. Greek indices run $0$–$3$, the metric raises and lowers them, $A_\mu = \eta_{\mu\nu}A^\nu$. This is a compound page: it defines two interlocking notions — the **four-velocity** and the **four-acceleration** — because they are introduced together (acceleration is the proper-time derivative of velocity) and neither is fully usable without the other. Full registry on [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

> [!warning] Convention
> Gourgoulhon defines a *dimensionless* four-velocity $\vec{u} = c^{-1}\,d\vec{x}/d\tau$ with $\vec{u}\cdot\vec{u} = -1$ in his mostly-plus signature, and a four-acceleration $\vec{a} = c^{-1}\,d\vec{u}/d\tau$ with $\vec{a}\cdot\vec{a} \ge 0$ (spacelike). Translating to our mostly-minus signature and natural units $c = 1$: the normalisation becomes $U \cdot U = +1$, the orthogonality $A \cdot U = 0$ is unchanged, and the four-acceleration is spacelike-or-zero, $A \cdot A \le 0$. With $c = 1$ our $U = dX/d\tau = \gamma(1, \mathbf{u})$ coincides with Gourgoulhon's dimensionless $\vec u$ and with Tong's $U = \gamma(c, \mathbf{u})$.

---

# Axiom Motivation

Newtonian mechanics is built by differentiating with respect to time: velocity is $d\mathbf{x}/dt$, acceleration $d^2\mathbf{x}/dt^2$, and the laws relate these three-vectors. The trouble in relativity is that the time coordinate $t$ is *frame-dependent* — it is one particular observer's clock, not a Lorentz scalar. If you differentiate the four-position $X^\mu$, which is a perfectly good [[Def - Four-Vector|four-vector]] (well, its displacement is), with respect to the non-scalar $t$, the result $dX^\mu/dt$ transforms in a tangled, non-tensorial way: under a boost both $X^\mu$ and $t$ change, and the quotient is not a four-vector. A law written with it would look different to every observer, violating the principle of relativity. So the naive "four-velocity" $dX^\mu/dt$ is the wrong object, and the whole of relativistic kinematics hinges on replacing it with the right one.

The fix is the one new ingredient of the previous page: differentiate with respect to **proper time** $\tau$ instead of coordinate time $t$. Proper time is a Lorentz scalar — every observer agrees on the reading of the clock carried along the worldline — so $dX^\mu/d\tau$ is a four-vector divided by a scalar, hence a genuine four-vector. This is the entire motivation: *to relativise a Newtonian rate of change, differentiate with respect to the invariant clock, not the observer's clock.* The four-velocity $U^\mu = dX^\mu/d\tau$ is what you get, and because $\tau$ is intrinsic to the worldline (not to any frame), $U$ is an **absolute** quantity, attached to the worldline itself and independent of any observer — a sharp contrast with the "ordinary velocity" $\mathbf{u}$, which only exists relative to a chosen observer (and is built in [[Special Relativity VII — Kinematics I, Motion Relative to an Observer|the kinematics chapter]]).

Why parametrise specifically by *proper* time and not by some other scalar — say, $\tau$ rescaled, or an affine parameter? Because proper time is the metric arc length, and arc-length parametrisation makes the tangent a **unit** vector. Concretely $U \cdot U = dX/d\tau \cdot dX/d\tau = ds^2/d\tau^2 = 1$, since $d\tau = \sqrt{ds^2}$. This normalisation is not a convention we impose but a consequence of choosing proper time, and it is enormously useful: it means the four-velocity carries only **three** independent components, not four (the fourth is fixed by $U \cdot U = 1$), which is exactly right — a particle's state of motion is three numbers. It also resolves a puzzle Tong highlights: the four-velocity is a four-component object, yet a velocity should be three numbers, and the constraint $U \cdot U = 1$ is precisely what removes the spurious fourth degree of freedom. One could instead use a dimensionful $dX/d\tau$ (Tong's $\gamma(c,\mathbf u)$, normalised to $c^2$) or Gourgoulhon's dimensionless version; all are the same object once $c = 1$, and we take the unit-norm form because the algebra is cleanest.

The four-acceleration then has only one sensible definition: the proper-time derivative of the four-velocity, $A^\mu = dU^\mu/d\tau$. Two of its properties are forced, not chosen, and each is a constraint you get for free. First, $A$ is Minkowski-**orthogonal** to $U$: differentiating the identity $U \cdot U = 1$ gives $2\, A \cdot U = 0$. This is automatic and constrains the four-acceleration to the three-dimensional subspace orthogonal to the four-velocity — it has no component "along the direction of motion in spacetime", which is the relativistic statement that an ordinary force changes the *direction* of $U$ in spacetime without changing its (fixed) length. Second, $A$ is **spacelike or zero**: any nonzero vector orthogonal to a timelike vector is spacelike (a fact about the indefinite metric, proved below), so $A \cdot A \le 0$. The four-acceleration therefore lives *outside* the light cone, in contrast to the four-velocity which lives inside it. If one tried to define acceleration as $d^2\mathbf{x}/dt^2$ (the coordinate acceleration), one would get a frame-dependent three-vector with none of these clean invariant properties; the proper-time second derivative is the object that has them.

---

# The Definition

Let $\mathcal{L}$ be a [[Def - Worldline of a Particle|timelike worldline]] parametrised by its [[Def - Proper Time|proper time]] $\tau$, with four-position $X^\mu(\tau)$.

**Four-velocity.** The **four-velocity** of the particle is the proper-time derivative of its four-position,
$$
U^\mu \;:=\; \frac{dX^\mu}{d\tau}.
$$
In an inertial frame, using $dt/d\tau = \gamma$ and $\mathbf{u} = d\mathbf{x}/dt$,
$$
U^\mu \;=\; \frac{dt}{d\tau}\,(1, \mathbf{u}) \;=\; \gamma\,(1, \mathbf{u})
\qquad\Big(\text{with } c:\ U^\mu = \gamma\,(c, \mathbf{u})\Big).
$$
It is a **four-vector**: under a Lorentz transformation $\Lambda$ it transforms as $U^\mu \to \Lambda^\mu{}_\nu U^\nu$, precisely because $\tau$ is a Lorentz scalar. It is **future-directed**, **timelike**, and **unit-normalised**:
$$
\boxed{\,U \cdot U \;=\; \eta_{\mu\nu}U^\mu U^\nu \;=\; 1\,} \qquad (\text{with } c:\ U\cdot U = c^2).
$$
Equivalently, $U$ is *the unique future-directed unit timelike vector tangent to* $\mathcal{L}$ at each event. The set of all four-velocities is exactly the set $\mathcal{U}^+$ of future-directed unit timelike vectors.

**Four-acceleration.** The **four-acceleration** is the proper-time derivative of the four-velocity,
$$
A^\mu \;:=\; \frac{dU^\mu}{d\tau} \;=\; \frac{d^2 X^\mu}{d\tau^2}.
$$
It is a four-vector, and it satisfies two identities valid on every worldline:
$$
\boxed{\,A \cdot U \;=\; 0\,} \qquad\text{(orthogonal to the four-velocity)},
$$
$$
\boxed{\,A \cdot A \;\le\; 0\,} \qquad\text{($A$ is spacelike or zero), with equality iff } A = 0.
$$
The **proper acceleration** is the magnitude $a := \sqrt{-A \cdot A} = \|A\|$, the acceleration the particle feels in its own instantaneous rest frame (made precise for [[Special Relativity XVI — Accelerated Observers|accelerated observers]]). A worldline is straight (inertial) if and only if $A = 0$ identically.

In components, $A^0 = \gamma\,d\gamma/dt$ and $A^i = \gamma\,d(\gamma u^i)/dt$; for one-dimensional motion this reduces to $A^\mu = \gamma^4(u\,\dot u, \dot u, 0, 0)$ with $\dot u = du/dt$, whose norm is $-A\cdot A = \gamma^6\dot u^2$, so $a = \gamma^3|\dot u|$.

---

# Categorical / Structural Definition

The four-velocity is the **unit tangent field** of a timelike curve in the Lorentzian manifold $(\mathbb{M}, \eta)$, and the four-acceleration is the (flat) **covariant derivative of that field along the curve**. In the flat case the covariant derivative is just $d/d\tau$ on components; the structural content is that $A = \nabla_U U$, the rate of change of the unit tangent. This is the geometry that survives to the curved case: in $(M, g)$ the four-acceleration of a worldline is $A^\mu = \nabla_U U^\mu = \dfrac{dU^\mu}{d\tau} + \Gamma^\mu{}_{\nu\rho}U^\nu U^\rho$, and a **geodesic** is precisely a worldline with $A = 0$ — the curve that "transports its own tangent without turning". A free-falling particle has $A = 0$; what an accelerometer measures is $\|A\|$, which is why a freely-falling observer is weightless even in a gravitational field.

The two identities have clean structural readings. $U \cdot U = 1$ says the four-velocity is a section of the **unit timelike hyperboloid bundle**: at each event, $U$ lives on the future sheet of $\{X : X \cdot X = 1\}$, a copy of three-dimensional hyperbolic space $\mathbb{H}^3$ on which the [[Def - The Lorentz Group|Lorentz group]] acts as the isometry group. (The [[Def - Rapidity|rapidity]] is the hyperbolic distance on this space.) The orthogonality $A \cdot U = 0$ says the four-acceleration is tangent to the hyperboloid at $U$ — the only way a unit vector can change is by sliding along the surface of unit vectors, never off it, which is the geometric reason an ordinary force cannot change a particle's rest mass.

---

# Relate to Other Fields / Compression

The four-velocity is the basic kinematic four-vector of relativistic mechanics, the object from which the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$, the [[Def - Four-Force|four-force]] $F = dP/d\tau$, and the relativistic equation of motion are all built. It is the relativistic completion of the Newtonian velocity, and the four-acceleration the completion of Newtonian acceleration, with the substitution $d/dt \to d/d\tau = \gamma^{-1}d/dt$ throughout.

**True name (four-velocity):** *the unique future-directed unit timelike vector tangent to the worldline* — equivalently $\gamma(1, \mathbf{u})$ in any frame. The operational payoff of "unit" is that $U \cdot U = 1$ is a free equation true for every particle; squaring or contracting four-velocities is the cleanest route to relative speeds (the relative Lorentz factor of two particles is $U \cdot U' = \gamma_{\mathrm{rel}}$) and to [[Thm - Relativistic Velocity Addition|velocity addition]], which becomes a single matrix multiplication $U' = \Lambda U$ rather than a nonlinear formula.

**True name (four-acceleration):** *the proper-time rate of change of the four-velocity, always orthogonal to it and always spacelike* — equivalently, what an accelerometer riding the worldline reads (its magnitude). The orthogonality $A \cdot U = 0$ is a free equation that constrains the four-acceleration to three dimensions and guarantees the rest mass is conserved under any force.

Across fields the same construction appears as the unit-speed parametrisation of a curve and its geodesic curvature: in Riemannian geometry the four-acceleration is the curvature vector of the curve, and its magnitude $\|A\|$ is the [[Def - Curvature and Torsions of a Worldline|curvature]] of the worldline (the first invariant of its Serret–Frenet apparatus). In dynamical systems a worldline is a solution of the second-order system $\ddot X = A(X, \dot X)$ on the unit-tangent bundle.

---

# Examples / Corollaries

**Is an instance — a particle at rest.** A particle at rest in a frame has $\mathbf{u} = 0$, $\gamma = 1$, and $U^\mu = (1, \mathbf{0})$, with $U \cdot U = 1$. This is the simplest four-velocity, and every other is a Lorentz boost of it: $\mathcal{U}^+$ is a single Lorentz orbit of $(1,\mathbf 0)$.

**Is an instance — a uniformly moving particle.** Moving at speed $u$ along $x$: $U^\mu = \gamma(1, u, 0, 0)$, $U \cdot U = \gamma^2(1 - u^2) = 1$. The four-acceleration vanishes, $A = 0$, since $U$ is constant — an inertial worldline.

**Is an instance — hyperbolic motion.** A particle with constant proper acceleration $a$ along $x$ has $U^\mu = (\cosh a\tau, \sinh a\tau, 0, 0)$ (a [[Def - Rapidity|rapidity]] $a\tau$ growing linearly with proper time), so $U \cdot U = \cosh^2 - \sinh^2 = 1$, and $A^\mu = dU/d\tau = a(\sinh a\tau, \cosh a\tau, 0, 0)$. Check: $A \cdot U = a(\sinh\cosh - \cosh\sinh) = 0$, and $A \cdot A = a^2(\sinh^2 - \cosh^2) = -a^2 < 0$, spacelike, with $\|A\| = a$ constant. This is the worldline of the [[Ex - The twin paradox|twin-paradox traveller]] on each arc.

**Is NOT an instance — the coordinate velocity $(1, \mathbf{u})$.** The three-velocity packaged as $(1, \mathbf{u})$ (without the $\gamma$) is *not* a four-velocity: it is not unit-normalised ($1 - u^2 = \gamma^{-2} \ne 1$) and, crucially, it does not transform as a four-vector under boosts. The factor $\gamma = dt/d\tau$ is exactly what is needed to make $\gamma(1, \mathbf{u})$ transform correctly, because it converts the coordinate-time derivative into a proper-time derivative.

**Is NOT an instance — a photon.** A photon has no four-velocity: along its null worldline $d\tau = 0$, so $dX/d\tau$ is undefined, and there is no unit null vector (a null vector has zero norm, not unit norm). The photon's kinematics is carried instead by its null [[Def - The Four-Momentum of a Photon|four-momentum]], not a four-velocity — see [[Def - Photons and Null Geodesics]].

**Is NOT an instance — a four-acceleration parallel to the four-velocity.** No worldline has $A \parallel U$ with $A \ne 0$: that would violate $A \cdot U = 0$ (a nonzero multiple of $U$ has $U\cdot U = 1 \ne 0$). The four-acceleration is necessarily transverse to the four-velocity; "speeding up in spacetime" is impossible because the four-velocity has fixed length.

**Corollary — the rest mass is conserved under an ordinary force.** Because $A \cdot U = 0$, the four-force $F = mA$ (for fixed $m$) satisfies $F \cdot U = 0$, which is exactly the statement $dm/d\tau = 0$ when worked through; a purely mechanical force changes a particle's energy and momentum but not its rest mass. (Forces that change rest mass, like radiative ones, have a component along $U$ and are not of the form $mA$.)

**Calibration check.** You have understood the definitions if you can: (i) write down $U^\mu$ for a particle of speed $u$ and verify $U \cdot U = 1$; (ii) prove $A \cdot U = 0$ in one line by differentiating $U \cdot U = 1$; and (iii) explain why a photon has no four-velocity but does have a four-momentum.

---

# Unlocked by This

> [!tip] Four-Momentum and $E = mc^2$ *(from Energy and Momentum)*
> Multiplying the four-velocity by the invariant [[Def - Four-Momentum and Rest Mass|rest mass]] $m$ gives the **four-momentum** $P^\mu = mU^\mu = (E, \mathbf{p})$ — the object that is actually conserved. Its time component is the energy $E = \gamma m$, whose low-speed expansion $E = m + \tfrac12 mu^2 + \cdots$ exhibits the rest energy $mc^2$; its norm is $P \cdot P = m^2 U \cdot U = m^2$, the mass-shell relation. The entire content of [[Special Relativity XIII — Energy and Momentum]] is built on the four-velocity defined here.

> [!tip] The Four-Force and the Relativistic Equation of Motion *(from Energy and Momentum)*
> Newton's second law, made Lorentz-covariant, is $F^\mu = dP^\mu/d\tau = mA^\mu$ for constant rest mass, with the **four-force** $F^\mu$ inheriting the orthogonality $F \cdot U = 0$ from the four-acceleration. The one physically important relativistic force, the Lorentz force, is $F^\mu = q\,F^\mu{}_\nu U^\nu$ with $F^\mu{}_\nu$ the [[Def - The Electromagnetic Field Tensor|field-strength tensor]] — and the four-velocity defined here is what it acts on.

> [!tip] Fermi–Walker Transport and the Curvature of a Worldline *(from Accelerated Observers)*
> The four-acceleration is the first invariant of the **Serret–Frenet apparatus** of the worldline: $\|A\|$ is its [[Def - Curvature and Torsions of a Worldline|curvature]], and the orthonormal tetrad built from $U$ and $A$ is carried along the worldline by **Fermi–Walker transport**, the relativistic notion of "non-rotating" that defines a gyroscope's axes for an accelerated observer. This is the bridge from a particle's kinematics to the frame an accelerated *observer* carries, developed in [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]] and [[Special Relativity XVI — Accelerated Observers]].

> [!tip] The Geodesic Four-Velocity in Curved Spacetime *(from General Relativity)*
> In a curved spacetime the four-velocity is still the unit tangent $U \cdot U = 1$ (now in the metric $g$), and the four-acceleration is the **covariant** derivative $A^\mu = \nabla_U U^\mu = dU^\mu/d\tau + \Gamma^\mu{}_{\nu\rho}U^\nu U^\rho$. A freely-falling particle has $A = 0$ — it follows a **geodesic** — so "free fall" is the curved-space version of "inertial motion", and the weightlessness of an astronaut is the statement $A = 0$. The four-acceleration is exactly what distinguishes a rocket (engine on, $A \ne 0$) from free fall ($A = 0$), and an accelerometer measures $\|A\|$ regardless of any gravitational field.
