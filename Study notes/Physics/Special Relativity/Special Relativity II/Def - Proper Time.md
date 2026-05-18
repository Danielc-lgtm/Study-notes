---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spacetime Interval"
  - "Thm - Invariance of the Spacetime Interval"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We work in natural units with $c = 1$, so time and space are measured in the same unit; factors of $c$ are restored at the end by dimensional analysis if needed. A spacetime point is $X^\mu = (t,\mathbf{x})$, with $\mathbf{x}$ the spatial part. The Minkowski metric is $\eta_{\mu\nu} = \operatorname{diag}(+1,-1,-1,-1)$, and the [[Def - The Spacetime Interval|interval]] between infinitesimally separated events is $ds^2 = dt^2 - d\mathbf{x}^2$. A particle's ordinary velocity in a given inertial frame is $\mathbf{u} = d\mathbf{x}/dt$, its speed $u = |\mathbf{u}|$, and its Lorentz factor $\gamma = (1-u^2)^{-1/2}$. Proper time is denoted $\tau$ (some texts write $s$). The full symbol registry is on the parent page [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Axiom Motivation

We want to describe the motion of a particle, and the very first thing we did in pre-relativistic mechanics was to parametrise its trajectory by time: $\mathbf{x}(t)$, with velocity $d\mathbf{x}/dt$. In special relativity this innocent choice is poisoned at the root. There is no longer a single time $t$; each inertial observer carries their own time coordinate, and these coordinates disagree. Worse, $t$ is not a Lorentz invariant — under a boost it mixes with the spatial coordinates. Any quantity built by differentiating with respect to $t$ inherits this frame-dependence and transforms in a tangled way. So the question that forces the definition is: **is there a parameter along a particle's worldline that every observer agrees on?**

There is, and finding it is an exercise in asking what we already know to be invariant. The one quantity all inertial observers compute identically is the [[Def - The Spacetime Interval|spacetime interval]] — this is the content of [[Thm - Invariance of the Spacetime Interval|its invariance theorem]]. So whatever invariant parameter we want must be built from the interval. Now consider the simplest possible particle: one sitting still at the spatial origin of some frame $S'$. Between two ticks of its own clock, separated by coordinate time $\Delta t'$, it does not move, $\Delta\mathbf{x}' = 0$, so the interval between those two events is $\Delta s^2 = \Delta t'^2$. The interval *equals the time the particle's own clock reads*. That is the clue. We define the invariant parameter — call it **proper time** $\tau$ — so that along any worldline it agrees with the interval: $d\tau^2 = ds^2$. Because $ds^2$ is invariant, $\tau$ is invariant; because $\tau$ reduces to ordinary clock time when the particle is at rest, it deserves to be called a *time*.

Why this specific definition and not a nearby variant? Suppose we tried to keep coordinate time after all, or to use some other parameter. We would lose exactly the property that makes $\tau$ useful: differentiating the four-position $X^\mu$ with respect to $\tau$ gives a [[Def - Four-Velocity and Four-Acceleration|four-velocity]] that is a genuine four-vector, because $X^\mu$ is a four-vector and $\tau$ is a scalar, and a four-vector divided by a scalar is a four-vector. Differentiating instead with respect to $t$ would divide a four-vector by a frame-dependent number and produce a non-tensorial mess. So $\tau$ is forced on us as the unique invariant worldline parameter, and the entire machinery of relativistic dynamics — four-velocity, four-momentum, four-force — rests on this one choice.

There is also a sharp restriction built in. The definition $d\tau^2 = ds^2$ only makes sense, with $\tau$ real, when $ds^2 > 0$ — when the worldline is **timelike**, when successive events on it are separated by more time than space. This is automatic for any particle slower than light. But for a particle moving *at* the speed of light — a photon — the interval along its worldline is zero, $ds^2 = 0$, and proper time does not advance at all. There is no rest frame for such a particle and no clock that could measure its $\tau$. Proper time is therefore defined only for timelike worldlines, and the photon's exclusion is not an oversight but a genuine feature of the geometry — it is why massless particles need the separate treatment of [[Def - The Four-Momentum of a Photon|their four-momentum]].

---

# The Definition

Let a particle move on a **timelike worldline** through Minkowski space — a curve along which every infinitesimal displacement satisfies $ds^2 = dt^2 - d\mathbf{x}^2 > 0$ in every inertial frame. Pick an inertial frame with coordinates $(t,\mathbf{x})$, and let the worldline be $\mathbf{x}(t)$.

**Proper time.** The **proper time** elapsed along the worldline between two events $P_0$ and $P$ on it is the integral of the [[Def - The Spacetime Interval|interval]] along the curve,
$$\tau(P) \;=\; \int_{P_0}^{P} \sqrt{dt^2 - d\mathbf{x}^2}\;=\;\int_{P_0}^{P}\sqrt{1 - \Big(\tfrac{d\mathbf{x}}{dt}\Big)^2}\;\,dt\;=\;\int_{t_0}^{t}\frac{dt'}{\gamma\big(u(t')\big)},$$
where $u = |d\mathbf{x}/dt|$ is the instantaneous speed and $\gamma(u) = (1-u^2)^{-1/2}$. Restoring $c$, the infinitesimal form is
$$d\tau = \frac{ds}{c} = \sqrt{dt^2 - \frac{d\mathbf{x}^2}{c^2}} = dt\sqrt{1 - \frac{u^2}{c^2}} = \frac{dt}{\gamma}.$$

Equivalently, **proper time is the time read by an ideal clock carried along the worldline**, and the differential relation between proper time and the coordinate time of any inertial frame is
$$\frac{dt}{d\tau} = \gamma(u).$$

The freedom to choose the starting event $P_0$ is the freedom to shift $\tau$ by an additive constant; only proper-time *differences* are physical. Proper time is a **Lorentz invariant**: every inertial observer, integrating along the same worldline, obtains the same value, because the integrand $ds$ is invariant.

For a **spacelike** curve one can analogously define a *proper length* by inserting a minus sign under the square root, $d\ell = \sqrt{d\mathbf{x}^2 - dt^2}$; this is the length of an extended body measured in its own rest frame. For a **null** worldline the integrand vanishes identically and no proper-time parameter exists.

---

# Relate to Other Fields / Compression

Proper time is the Minkowski analogue of **arc length** in Riemannian geometry. In Euclidean space the arc length of a curve is $\int\sqrt{dx^2 + dy^2 + dz^2}$, and it is invariant under rotations because the integrand is a rotation-invariant quantity. Proper time is $\int\sqrt{dt^2 - d\mathbf{x}^2}$, and it is invariant under Lorentz transformations because the integrand is Lorentz-invariant. The single sign flip in the metric is the entire difference. This is more than an analogy: in [[Multivariate Analysis I — Differentiation in Several Variables|differential geometry]] one defines the length of a curve on any manifold as the integral of $\sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}$ against the metric tensor $g$, and proper time is exactly this construction with $g = \eta$, the flat Minkowski metric. When the metric becomes curved — in general relativity — proper time is still defined by the very same integral, now along worldlines in a curved spacetime, and the geodesics (extremal-proper-time curves) are the trajectories of free-falling particles.

The indefinite signature produces one inversion of intuition worth flagging. In Euclidean geometry the straight line is the *shortest* path between two points. In Minkowski geometry, the straight (constant-velocity) worldline between two timelike-separated events is the one of *longest* proper time — this is the content of the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]]. An accelerated traveller always ages *less* than an inertial one, and by accelerating hard enough the proper time can be made arbitrarily small. This is the twin paradox, and it is a theorem of Minkowski geometry, not a paradox at all.

---

# Examples / Corollaries

**Is an instance — uniform motion, the time-dilation formula.** A particle moving at constant speed $u$ for a coordinate-time interval $\Delta t$ experiences proper time $\Delta\tau = \Delta t/\gamma = \Delta t\sqrt{1-u^2}$. Since $\gamma \geq 1$, the moving clock advances *less* than the coordinate clock: this is time dilation, and it is the simplest instance of the definition. In the particle's own rest frame $u = 0$, $\gamma = 1$, and $\tau$ coincides with coordinate time, as it must.

**Is an instance — the accelerated twin.** Take a worldline that leaves a point, accelerates out and back, and returns. The proper time elapsed is $\tau = \int dt/\gamma(t)$, with $\gamma > 1$ wherever the traveller moves, so $\tau < \Delta t$, the coordinate time measured by a twin who stayed put. The travelling twin returns younger. There is no contradiction with relativity's symmetry between observers because the worldlines are *not* symmetric — one is straight, the other bent — and proper time depends on the worldline, exactly as Euclidean arc length depends on the path. See [[Ex - Proper time along an accelerated worldline]].

**Is NOT an instance — a photon's worldline.** A photon travels at $u = c$, so along its worldline $d\mathbf{x}^2 = dt^2$ and $ds^2 = 0$ in every frame. The proper-time integral gives $\tau = 0$ identically: proper time does not advance, there is no clock that ticks for a photon, and the definition simply does not apply. This is why massless particles are handled through [[Def - The Four-Momentum of a Photon|their four-momentum]] rather than through proper time.

**Is NOT an instance — a spacelike curve.** A curve along which $d\mathbf{x}^2 > dt^2$ — for example the locus of "all of space at one instant" — is spacelike, the would-be integrand $\sqrt{dt^2-d\mathbf{x}^2}$ is imaginary, and proper *time* is undefined. The right invariant for such a curve is proper *length*, $\int\sqrt{d\mathbf{x}^2-dt^2}$, the analogue with the opposite sign.

**Corollary — proper time is reparametrisation-independent.** The integral $\int\sqrt{dt^2-d\mathbf{x}^2}$ depends only on the worldline as a geometric curve, not on how it is parametrised, since it can be written $\int\sqrt{\eta_{\mu\nu}\,\dot X^\mu\dot X^\nu}\,d\lambda$ for any parameter $\lambda$ and the $d\lambda$ cancels. This is what makes $\tau$ a *canonical* parameter: it is intrinsic to the worldline.

**Calibration check.** Verify that $dt/d\tau = \gamma$ follows directly from $d\tau = dt/\gamma$; that for $u\ll c$ one has $d\tau \approx dt(1 - u^2/2c^2)$, so the leading correction to clock time is second order in $u/c$; and that the total proper time along a worldline, $T = \int d\tau = \int dt/\gamma$, is always less than or equal to the coordinate time, with equality only for an inertial (constant-velocity) worldline. If you can also explain why a photon has $\tau = 0$ while a slow particle has $\tau\approx t$, you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] The Relativistic Action *(from Geometric Mechanics and Field Theory)*
> A free relativistic particle moves on the worldline that **extremises its proper time**: the action is $S = -mc^2\int d\tau$. This is the relativistic principle of least action; the Euler–Lagrange equations give a straight worldline, and the conjugate momentum is exactly the [[Def - Four-Momentum and Rest Mass|four-momentum]]. Because the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] makes the straight worldline a *maximum* of proper time, the principle is a maximum, not a minimum.

> [!tip] Geodesics in Curved Spacetime *(from General Relativity)*
> Proper time $\tau = \int\sqrt{g_{\mu\nu}dx^\mu dx^\nu}$ generalises verbatim to a **curved** metric $g_{\mu\nu}$. The worldlines of free-falling particles are the **timelike geodesics** — the curves of extremal proper time — and gravity is the statement that these geodesics are bent. Proper time is the functional whose extremals *are* the law of motion.

> [!tip] Proper Time as Arc Length and the Geodesic Equation *(from General Relativity and Geometric Mechanics)*
> Proper time is, structurally, the **arc length** of a worldline measured in the spacetime metric: $\tau = \int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$, exactly the differential-geometry formula for the length of a curve on a manifold, with the Minkowski metric $g = \eta$ in flat space and a curved $g_{\mu\nu}$ once gravity is switched on. The single sign flip in the metric's signature is the only thing distinguishing it from Riemannian arc length. Reading proper time as a length immediately suggests a **variational principle**: a free particle should move on the worldline that *extremises* this length, and writing the relativistic action as $S = -mc^2\int d\tau$ makes the conjugate momentum the [[Def - Four-Momentum and Rest Mass|four-momentum]] and the Euler–Lagrange equations the law of motion. In flat space extremising proper time gives a straight worldline; in a curved metric the same extremisation produces the **geodesic equation** $d^2x^\mu/d\tau^2 + \Gamma^\mu{}_{\nu\rho}\,(dx^\nu/d\tau)(dx^\rho/d\tau) = 0$, where the Christoffel symbols $\Gamma$ are built from derivatives of $g_{\mu\nu}$. The trajectory of a free-falling particle is therefore the curve of extremal proper time — gravity is encoded entirely in how the metric makes that extremal worldline bend. Because the indefinite signature makes the straight worldline a *maximum* of proper time (the reversed triangle inequality), the relativistic least-action principle is really a principle of maximal ageing.

> [!tip] Worldline Length, Extremal Ageing, and the Relativistic Action *(from General Relativity and Geometric Mechanics)*
> It is worth isolating, as one clean chain of ideas, what proper time *becomes* once the setting is allowed to be curved. Begin with the observation that $\tau = \int\sqrt{\eta_{\mu\nu}\,dx^\mu dx^\nu}$ is not a special-relativistic accident but an instance of the general **arc length** of a curve on a manifold: differential geometry assigns to any curve the integral $\int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$ of the metric tensor along it, and proper time is exactly this with $g = \eta$. Replace $\eta$ by a position-dependent metric $g_{\mu\nu}(x)$ — the move from special to general relativity — and the *same* formula, $\tau = \int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$, still defines the time elapsed on a clock carried along the worldline; nothing in the construction needed flatness. Now ask which worldline a free particle actually follows. The answer is the one that **extremises** this length, and the cleanest way to state it is through a variational principle: take the **relativistic action** $S = -mc^2\int d\tau$ and demand $\delta S = 0$. The Euler–Lagrange equations of this functional are the **geodesic equation** $d^2x^\mu/d\tau^2 + \Gamma^\mu{}_{\nu\rho}\,(dx^\nu/d\tau)(dx^\rho/d\tau) = 0$, with the Christoffel symbols $\Gamma$ assembled from first derivatives of $g_{\mu\nu}$; in flat space and Cartesian coordinates every $\Gamma$ vanishes and the law collapses to the straight worldline $d^2x^\mu/d\tau^2 = 0$ of this topic. The same variational principle hands you the [[Def - Four-Momentum and Rest Mass|four-momentum]] for free, as the momentum $\partial L/\partial\dot x^\mu$ conjugate to the four-position. The one feature inherited from the indefinite signature is that the extremum is a *maximum*: among timelike worldlines joining two events, the geodesic is the one of *greatest* proper time, so the relativistic principle of least action is in truth a principle of *maximal ageing* — a free particle is the one that ages as much as possible between two events.
