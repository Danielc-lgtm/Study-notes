---
type: definition
subject: special-relativity
prereqs:
  - "Def - Thomas Rotation"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Fermi-Walker Derivative"
  - "Def - Spin Four-Vector"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\mathcal{O}$ is an accelerated observer of worldline $\mathcal{L}$, proper time $t$, four-velocity $U$, four-acceleration $A\neq 0$ and *vanishing* [[Def - Local Frame and Four-Rotation|four-rotation]] $\vec\omega = 0$; its local frame is $(e_\alpha(t))$. $\mathcal{O}_*$ is the reference inertial observer of frame $(e_\alpha^*)$ and proper time $t_*$; $\Gamma$ is the Lorentz factor of $\mathcal{O}$ relative to $\mathcal{O}_*$, and $\mathbf{V}$, $\boldsymbol\gamma$ (bold) are $\mathcal{O}$'s three-velocity and three-acceleration relative to $\mathcal{O}_*$. $S$ is the [[Def - Spin Four-Vector|spin four-vector]] and $\mathbf{s}$ its spatial part. The cross product within the inertial rest space is $\times_{e_0^*}$, abbreviated $\times$. Full registry on [[Special Relativity XVI — Accelerated Observers]].

> [!warning] Convention: Gourgoulhon's $\vec\gamma$ versus the Lorentz factor
> Gourgoulhon writes $\vec\gamma$ for the *relative three-acceleration* of $\mathcal{O}$ as seen by $\mathcal{O}_*$ (an unfortunate clash with the usual symbol for the Lorentz factor), and $\Gamma$ for the Lorentz factor. To avoid confusion this page writes the relative three-acceleration as $\boldsymbol\gamma$ or, in the standard atomic-physics form, $\mathbf{a}$, and reserves $\Gamma$ (or $\gamma$) for the Lorentz factor. Watch this when transcribing.

---

# Axiom Motivation

We want to name and quantify a phenomenon that, on its face, should not exist: the spatial frame of a *non-rotating* observer rotates. Pinning down precisely what is rotating relative to what is the entire content of the motivation.

Start from the apparent paradox. An accelerated observer can carry a frame that is non-rotating by every operational test available to them: they hold three mutually perpendicular gyroscopes, and the frame's axes stay locked to the gyroscopes' axes. Mathematically, this is the condition that the [[Def - Local Frame and Four-Rotation|four-rotation]] $\vec\omega$ vanishes — the frame is [[Def - Fermi-Walker Derivative|Fermi–Walker transported]], dragged along the worldline with no twist relative to the worldline itself. Such an observer feels no Coriolis force, no centrifugal force; their local physics is that of a non-rotating frame. And yet, if the observer's worldline is curved and their acceleration is not parallel to their velocity, an inertial observer watching from outside sees the observer's spatial axes *steadily rotate*. Something must give: either "non-rotating" is ill-defined, or "rotation" means two different things.

It is the latter, and seeing why motivates the definition. There are two distinct standards against which rotation can be measured. The first is *intrinsic*: the frame is compared to itself along the worldline, via Fermi–Walker transport, and "non-rotating" means $\vec\omega = 0$. The second is *extrinsic*: the frame's axes are compared to the fixed axes of the inertial observer (ultimately, to the distant stars). For an observer on a *geodesic* (inertial), these two standards agree — a Fermi–Walker-transported frame keeps fixed directions relative to the stars. But for an accelerated observer on a curved worldline they cannot both hold, and the mismatch is a real, measurable rotation. The phenomenon we want to define is exactly this mismatch: the rotation of the intrinsically-non-rotating frame relative to the inertial frame.

Why does the mismatch arise, and why only when $\mathbf{a}\not\parallel\mathbf{V}$? The mechanism lives in the Lorentz group. At each instant the observer is related to the inertial observer by a boost $S$ (the boost carrying $\mathcal{O}_*$'s four-velocity to $\mathcal{O}$'s). An instant $dt$ later the observer's velocity has changed, and the new boost differs from the old by an infinitesimal boost $\Lambda$ of velocity $\mathbf{W} = c^2\,dt\,\mathbf{a}$ in the direction of the acceleration. The composition of two boosts in different directions is *not* a boost: by the [[Def - Thomas Rotation|polar decomposition]] it is a boost times a residual spatial rotation, the **Thomas rotation**. So the frame, as represented in the inertial observer's rest space, picks up an infinitesimal Thomas rotation at every step, and these accumulate into a steady precession. When $\mathbf{a}\parallel\mathbf{V}$ the two boosts are collinear, their composition *is* a boost, the Thomas rotation vanishes, and there is no precession — which is exactly why the uniformly accelerated observer of §16.2 (whose acceleration is always along the velocity) shows no Thomas precession. The phenomenon requires non-collinear acceleration and velocity, and the definition must say so.

The motivation for caring is physical and historical. A particle with spin carried on a curved worldline — an electron in an atom, a polarised beam in a storage ring, a gyroscope in orbit — has its spin Fermi–Walker transported (in the absence of torque), hence intrinsically non-rotating, hence subject to Thomas precession relative to the laboratory. For the electron in an atom this precession is the missing ingredient in the spin–orbit coupling: without it the predicted fine-structure splitting of spectral lines is too large by a factor of two, and Thomas's 1926 calculation of exactly this precession supplied the famous "Thomas half" that fixed the discrepancy. The definition exists to make the precession precise so that this and the analogous effects (the BMT equation, geodetic precession in general relativity) can be computed.

---

# The Definition

Let $\mathcal{O}$ be an accelerated [[Def - Observer and Local Rest Space|observer]] of worldline $\mathcal{L}$, four-velocity $U$, four-acceleration $A\neq 0$ and vanishing [[Def - Local Frame and Four-Rotation|four-rotation]] ($\vec\omega = 0$), carrying the local frame $(e_\alpha(t))$. Let $\mathcal{O}_*$ be an inertial observer, $S$ the unique Lorentz boost carrying $\mathcal{O}_*$'s four-velocity to $\mathcal{O}$'s at proper time $t$, and define the triad
$$
\boldsymbol\varepsilon_i(t_*) := S^{-1}(e_i(t)), \qquad i = 1,2,3,
$$
which lies in $\mathcal{O}_*$'s rest space $E_{e_0^*}$ and "represents" $\mathcal{O}$'s spatial frame as seen by $\mathcal{O}_*$. **Thomas precession** is the rotation of this triad $(\boldsymbol\varepsilon_i)$ relative to $\mathcal{O}_*$ as $\mathcal{O}$ moves along its worldline. Although the local frame $(e_\alpha)$ is non-rotating in the intrinsic (Fermi–Walker) sense, the representative triad $(\boldsymbol\varepsilon_i)$ obeys the rotation law
$$
\frac{d\boldsymbol\varepsilon_i}{dt_*} = \vec\omega_T \times_{e_0^*}\boldsymbol\varepsilon_i,
$$
where the **Thomas precession (angular-velocity) vector** $\vec\omega_T\in E_{e_0^*}$ is
$$
\boxed{\;\vec\omega_T = \frac{\Gamma^2}{c^2(\Gamma + 1)}\,\boldsymbol\gamma\times_{e_0^*}\mathbf{V} = \frac{\Gamma - 1}{V^2}\,\boldsymbol\gamma\times_{e_0^*}\mathbf{V}\;}
$$
with $\boldsymbol\gamma$ and $\mathbf{V}$ the three-acceleration and three-velocity of $\mathcal{O}$ relative to $\mathcal{O}_*$. (The two expressions are equal via the identity $\Gamma^2/(1+\Gamma) = (\Gamma-1)c^2/V^2$.) The precession plane is $\Pi_R = \mathrm{Span}(\mathbf{V}, \boldsymbol\gamma)$, and $\vec\omega_T$ is its (oriented) normal. In the low-velocity limit $|\mathbf{V}|\ll c$,
$$
\vec\omega_T \simeq \frac{1}{2c^2}\,\boldsymbol\gamma\times_{e_0^*}\mathbf{V}.
$$

In the standard atomic-physics notation, writing $\mathbf{a} := \boldsymbol\gamma$ for the three-acceleration and $\mathbf{v} := \mathbf{V}$ for the three-velocity (and noting $\boldsymbol\gamma\times\mathbf{V} = -\mathbf{V}\times\boldsymbol\gamma$), the precession rate is
$$
\boldsymbol\Omega_T = \frac{\gamma^2}{\gamma + 1}\,\frac{\mathbf{a}\times\mathbf{v}}{c^2}\ \xrightarrow{\ v\ll c\ }\ \frac{1}{2c^2}\,\mathbf{a}\times\mathbf{v}.
$$

Thomas precession occurs if and only if $\mathbf{a}$ and $\mathbf{V}$ are **not collinear** (so $\boldsymbol\gamma\times\mathbf{V}\neq 0$); for collinear acceleration and velocity — as for the uniformly accelerated observer of §16.2 — $\vec\omega_T = 0$ and there is no precession.

---

# Categorical / Structural Definition

Thomas precession is the **holonomy** of Fermi–Walker transport, measured against the inertial trivialisation. Carrying a spatial frame around a closed loop in velocity space (a closed orbit returns the four-velocity to its starting value) produces a net rotation — the integrated Thomas rotation — and this rotation depends only on the loop, not on how it is traversed in time. It is the special-relativistic instance of the general phenomenon that transporting a frame along a curved path in a curved space yields a rotation governed by the curvature enclosed.

The relevant "curved space" is **velocity space**, the hyperboloid $\{U : U\cdot U = 1, U^0 > 0\}$, which is a model of hyperbolic space $\mathbb{H}^3$ of constant negative curvature. The four-velocity of the accelerated observer traces a curve on this hyperboloid; Fermi–Walker transport of the spatial frame is parallel transport with respect to the hyperboloid's natural connection; and the Thomas rotation accumulated around a loop is the holonomy of that connection, equal to the (hyperbolic) area enclosed. For a circular orbit the enclosed solid angle on the velocity hyperboloid is exactly $2\pi(\Gamma - 1)$, which is the angular deficit per revolution — the same $(\Gamma-1)$ that appears in the orbiting-gyroscope formula. This is why Thomas precession is "geometric": it is a holonomy, a property of the path in velocity space, independent of the dynamical details.

The same structure recurs across physics. In general relativity, transporting a gyroscope around a massive body gives **geodetic precession**, the holonomy of the Levi-Civita connection. In quantum mechanics, transporting a state around a loop in parameter space gives the **Berry phase**, the holonomy of the Berry connection. Thomas precession is the flat-spacetime, classical-spin member of this family, with the velocity hyperboloid as the curved space and its curvature as the source.

---

# Relate to Other Fields / Compression

The cleanest reframing is that Thomas precession is the *time-derivative version* of the [[Def - Thomas Rotation|Thomas rotation]]. The Thomas rotation is the discrete rotation left over when two finite boosts are composed; Thomas precession is what you get by composing a continuous family of infinitesimal boosts along a worldline and reading off the rotation rate. The same gyrogroup structure that makes velocity addition non-commutative (Chapter IX) makes the spatial frame precess: the *gyration* of the gyrogroup is the Thomas rotation, and its differential is $\vec\omega_T$.

**True name:** Thomas precession is *the rate at which a Fermi–Walker-transported spatial frame rotates relative to the inertial frame*, equal to $\frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}/c^2$. The operational content is that a gyroscope carried on a curved, non-radial trajectory does not keep a fixed direction relative to the stars; it precesses, even though it is torque-free, purely from the kinematics of the changing boost.

The distinction this concept forces — between intrinsic non-rotation ($\vec\omega = 0$) and extrinsic non-rotation (fixed relative to the stars) — is the same distinction that, in general relativity, separates **frame-dragging** and **geodetic precession** from naive parallel transport, and that, in quantum mechanics, makes the **Berry phase** nonzero for a state transported around a loop. Thomas precession is the simplest, exactly-soluble member of this family: flat spacetime, classical spin, an explicit rate.

---

# Examples / Corollaries

**Is an instance — a gyroscope in circular orbit.** A free gyroscope carried on a circular orbit of radius $R$ and angular velocity $\Omega$ has centripetal acceleration $\mathbf{a} = -R\Omega^2\hat{\mathbf{r}}$ perpendicular to its velocity $\mathbf{v} = R\Omega\hat{\boldsymbol\theta}$, so $\mathbf{a}\not\parallel\mathbf{v}$ and Thomas precession occurs at $\vec\omega_T = -(\Gamma-1)\Omega\,\mathbf{e}_3$, opposite to the orbital sense; see [[Ex - Thomas precession of a gyroscope in circular orbit]].

**Is an instance — an electron in a hydrogen atom.** The orbiting electron is centripetally accelerated, $\mathbf{a}\perp\mathbf{v}$, so its spin precesses by Thomas precession; this is the kinematic correction that halves the naive spin–orbit coupling energy (the Thomas half); see [[Ex - The Thomas half and atomic fine structure]].

**Is NOT an instance — a uniformly accelerated observer.** The uniformly accelerated observer of §16.2 has acceleration always collinear with velocity ($\mathbf{a}\parallel\mathbf{v}$, both along $e_1$), so $\boldsymbol\gamma\times\mathbf{V} = 0$ and $\vec\omega_T = 0$: there is *no* Thomas precession, even though the observer is strongly accelerated. This shows that acceleration alone does not cause Thomas precession — the acceleration must turn the velocity.

**Is NOT an instance — an inertial observer.** An inertial observer ($\mathbf{a} = 0$) has $\vec\omega_T = 0$ trivially: a Fermi–Walker-transported frame on a geodesic keeps fixed directions relative to the stars. Thomas precession is strictly an accelerated-motion effect.

**Corollary — Thomas precession is a pure relativistic effect, of order $\Gamma - 1$.** Because $\vec\omega_T \propto \Gamma - 1$ (equivalently $\propto v^2/c^2$ at low speed), it vanishes in the Newtonian limit $c\to\infty$: there is no Thomas precession in non-relativistic mechanics. It is invisibly small for slow motion and dominant only at relativistic speeds — which is why it first surfaced in atomic spectra, where the electron's orbital speed is a few percent of $c$.

**Corollary — the precession is opposite to the sense of the velocity's turning.** The sign in $\vec\omega_T \propto \boldsymbol\gamma\times\mathbf{V}$ (acceleration cross velocity) means that for a velocity turning counterclockwise (centripetal acceleration pointing inward), the Thomas precession is *clockwise* — opposite to the orbital revolution. A gyroscope carried around a loop lags behind the orbital rotation by the Thomas angle.

**Calibration check.** If the definition is understood, the reader should be able to: (i) state in one sentence why a non-rotating frame ($\vec\omega = 0$) nonetheless precesses relative to the inertial frame (two standards of rotation; their mismatch is the accumulated Thomas rotation); (ii) explain why $\mathbf{a}\parallel\mathbf{v}$ gives no precession (collinear boosts compose to a boost); and (iii) write the low-velocity rate $\tfrac12\mathbf{a}\times\mathbf{v}/c^2$ and check it has the dimensions of an angular velocity.

---

# Unlocked by This

> [!tip] The BMT Equation *(from accelerator and particle physics)*
> Adding the dynamical torque exerted by an electromagnetic field on a particle's magnetic moment to the kinematic Thomas precession gives the **Bargmann–Michel–Telegdi (BMT) equation**, the covariant law for the precession of a spin in arbitrary $\mathbf{E}$ and $\mathbf{B}$ fields. The Thomas precession $\vec\omega_T$ is the field-free, purely kinematic piece; the full equation governs how a polarised beam's spin precesses in a storage ring, and the small excess of the spin precession over the orbital frequency is what the muon **anomalous magnetic moment** ($g-2$) experiments measure. The kinematic Thomas term must be subtracted to extract the genuine anomaly.

> [!tip] Geodetic Precession and Frame-Dragging *(from General Relativity)*
> In general relativity the same intrinsic-versus-extrinsic split appears, but now the curvature is that of spacetime itself rather than of velocity space. A gyroscope carried around a massive body precesses by the **geodetic effect** (from the curvature produced by the body's mass) and, if the body rotates, by **frame-dragging** (the Lense–Thirring effect). Both are holonomies of parallel transport, exactly as Thomas precession is the holonomy of Fermi–Walker transport in flat spacetime, and Gravity Probe B measured them by tracking gyroscopes in Earth orbit. Thomas precession is the flat-spacetime limit and the conceptual prerequisite: the special-relativistic part of a gyroscope's precession in orbit is precisely $\vec\omega_T$.
