---
type: definition
subject: special-relativity
prereqs:
  - "Def - Local Frame and Four-Rotation"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$. An observer $\mathcal{O}$ has worldline $\mathcal{L}_0$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$), four-acceleration $A_0 = dU_0/d\tau$, [[Def - Proper Time|proper time]] $\tau$, and spatial rotation rate $\vec\omega\in U_0^\perp$. $V = V(\tau)$ is a vector field along $\mathcal{L}_0$; $dV/d\tau$ is the **absolute derivative**; $D_{\mathcal{O}}V$ the **derivative with respect to $\mathcal{O}$**; $D^{\mathrm{FW}}_{U_0}V$ the **Fermi–Walker derivative**. $\Pi(X) = X - (X\cdot U_0)U_0$ is the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] onto the rest space. This is a compound page: it defines three interlocking derivatives — the **absolute derivative**, the **derivative with respect to the observer**, and the **Fermi–Walker derivative** — because they differ only by which part of the frame's motion is subtracted, and none is fully understood without the others. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (mostly-plus, $\vec u\cdot\vec u = -1$) writes $D^{\mathrm{FW}}_u\vec v = d\vec v/dt - c(\vec a\cdot\vec v)\vec u + c(\vec u\cdot\vec v)\vec a$. Translating to our mostly-minus convention (where the Fermi–Walker tensor's two terms swap sign, as on [[Def - Local Frame and Four-Rotation]]), $D^{\mathrm{FW}}_{U_0}V = dV/d\tau - c[(U_0\cdot V)A_0 - (A_0\cdot V)U_0]$. The defining property $D^{\mathrm{FW}}_{U_0}U_0 = 0$ and the projection identity $D^{\mathrm{FW}}_{U_0}V = \Pi(dV/d\tau)$ on the rest space hold in both conventions.

---

# Axiom Motivation

The four-rotation showed that an observer's frame, carried along the worldline, undergoes two distinct motions: an unavoidable tilt of the time axis forced by the four-acceleration, and a genuine spatial rotation $\vec\omega$ of the three spatial axes. This page builds the *derivatives* that measure rates of change relative to these motions — and, crucially, the one derivative that strips out the spatial rotation to define "non-rotating transport". The payoff is the law a gyroscope obeys, the relativistic notion of carrying a direction along a worldline without spinning it.

Start with the naive derivative. A vector field $V(\tau)$ along the worldline has an ordinary proper-time derivative $dV/d\tau$, the **absolute derivative**. It is the honest rate of change of $V$ in spacetime, but it has a defect that makes it the *wrong* notion of "how $V$ changes for the observer": it does not preserve the rest space. If $V$ is purely spatial for $\mathcal{O}$ (lies in $U_0^\perp$), its absolute derivative generally acquires a time component, because $U_0\cdot(dV/d\tau) = \tfrac{d}{d\tau}(U_0\cdot V) - A_0\cdot V = -A_0\cdot V$, which is nonzero whenever $V$ has a component along the four-acceleration. So a gyroscope's spin vector, spatial for the observer, would seem to "tilt out of space" under the absolute derivative — a spurious effect, an artifact of the time axis moving, not of anything physically rotating the spin.

The fix has two stages, corresponding to the two motions of the frame. First, subtract the part of $dV/d\tau$ that comes from the observer's *frame* changing rather than $V$'s components changing. A vector field is "fixed with respect to $\mathcal{O}$" when its components in the frame are constant, $V = V^\alpha e_\alpha$ with $V^\alpha$ constant; the **derivative with respect to the observer** $D_{\mathcal{O}}V := (dV^\alpha/d\tau)e_\alpha$ measures only the change in components, ignoring the frame's motion entirely. By construction $D_{\mathcal{O}}V = 0$ iff $V$ is fixed with respect to $\mathcal{O}$, and — the key virtue — $D_{\mathcal{O}}$ *preserves the rest space*: if $V\in U_0^\perp$ then $D_{\mathcal{O}}V\in U_0^\perp$, because the spatial components $V^i$ stay spatial. This is the right notion of "rate of change as the observer sees it".

But $D_{\mathcal{O}}$ subtracts *both* motions of the frame — the acceleration tilt *and* the spatial rotation. For a gyroscope we want to subtract only the unavoidable tilt and *keep* the rotation visible, because the whole point of a gyroscope is to detect rotation. So we want an intermediate derivative that strips the four-acceleration tilt but not the spatial rotation: the **Fermi–Walker derivative**
$$
D^{\mathrm{FW}}_{U_0}V := \frac{dV}{d\tau} - \Omega_{\mathrm{FW}}(V) = \frac{dV}{d\tau} - c\big[(U_0\cdot V)A_0 - (A_0\cdot V)U_0\big],
$$
obtained by subtracting only the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|Fermi–Walker part]] of the four-rotation. This is the derivative with respect to a *non-rotating* observer (one with $\vec\omega = 0$ sharing the worldline), and the three derivatives are related by
$$
D_{\mathcal{O}}V = D^{\mathrm{FW}}_{U_0}V - \vec\omega\times_{U_0}V :
$$
the observer derivative is the Fermi–Walker derivative minus the spatial rotation. A vector is **Fermi–Walker transported** when $D^{\mathrm{FW}}_{U_0}V = 0$ — this is the relativistic notion of non-rotating transport, the law a torque-free gyroscope obeys.

Why is the Fermi–Walker derivative the *right* notion of non-rotating, and not just $dV/d\tau$ or $D_{\mathcal{O}}$? Three properties single it out, each a desideratum. It must **preserve the four-velocity**: $D^{\mathrm{FW}}_{U_0}U_0 = 0$, so that the observer's own time direction is "non-rotatingly transported" into itself (a gyroscope's frame must keep $U_0$ as its time axis). It must **preserve the rest space**: spatial vectors stay spatial under it, unlike the absolute derivative. And on the rest space it must reduce to the cleanest possible operation — and indeed $D^{\mathrm{FW}}_{U_0}V = \Pi(dV/d\tau)$, the orthogonal projection of the absolute derivative onto the rest space, the minimal correction that keeps $V$ spatial. The first property fails for $dV/d\tau$ (which gives $A_0\neq 0$); the rotation-detection fails for $D_{\mathcal{O}}$ (which subtracts $\vec\omega$ too). Only the Fermi–Walker derivative subtracts exactly the unavoidable tilt and nothing more, which is why it, and not the others, is the relativistic generalisation of "parallel transport that doesn't rotate".

A subtlety worth flagging: the Fermi–Walker derivative depends *only on the worldline*, not on any spinning frame — there are infinitely many observers sharing one worldline, differing by their $\vec\omega$, and they all have the *same* Fermi–Walker derivative. It is the canonical, frame-independent "non-rotating" derivative attached to a worldline, which is exactly why it defines the standard of non-rotation against which the spatial rotation $\vec\omega$ of any particular observer is measured.

---

# The Definition

Let $V = V(\tau)$ be a vector field along the worldline $\mathcal{L}_0$ of an observer $\mathcal{O}$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$, four-acceleration $A_0$, and spatial rotation rate $\vec\omega$.

**Absolute derivative.** The **absolute derivative** of $V$ along $\mathcal{L}_0$ is the ordinary proper-time derivative $dV/d\tau$. With $V = V^\alpha e_\alpha$ in a [[Def - Local Frame and Four-Rotation|local frame]], $\dfrac{dV}{d\tau} = \dfrac{dV^\alpha}{d\tau}e_\alpha + V^\alpha\dfrac{de_\alpha}{d\tau}$.

**Derivative with respect to the observer.** The **derivative of $V$ with respect to $\mathcal{O}$** is
$$
\boxed{\,D_{\mathcal{O}}V := \frac{dV^\alpha}{d\tau}\,e_\alpha\,},
$$
the part of the change due only to the variation of $V$'s components in $\mathcal{O}$'s frame. It satisfies $D_{\mathcal{O}}V = 0 \Leftrightarrow V$ is fixed with respect to $\mathcal{O}$; $D_{\mathcal{O}}e_\alpha = 0$; $D_{\mathcal{O}}U_0 = 0$; and it **preserves the rest space**: $V\in E_{U_0}\Rightarrow D_{\mathcal{O}}V\in E_{U_0}$. In terms of the absolute derivative,
$$
D_{\mathcal{O}}V = \frac{dV}{d\tau} - c\big[(U_0\cdot V)A_0 - (A_0\cdot V)U_0\big] - \vec\omega\times_{U_0}V.
$$

**Fermi–Walker derivative.** The **Fermi–Walker derivative** of $V$ along $\mathcal{L}_0$ is the absolute derivative with the four-acceleration (Fermi–Walker) part of the four-rotation subtracted:
$$
\boxed{\,D^{\mathrm{FW}}_{U_0}V := \frac{dV}{d\tau} - c\big[(U_0\cdot V)A_0 - (A_0\cdot V)U_0\big]\,}.
$$
It depends only on the worldline (not on $\vec\omega$), and is related to the observer derivative by
$$
D_{\mathcal{O}}V = D^{\mathrm{FW}}_{U_0}V - \vec\omega\times_{U_0}V.
$$
$V$ is **Fermi–Walker transported** along $\mathcal{L}_0$ if $D^{\mathrm{FW}}_{U_0}V = 0$ — the relativistic notion of **non-rotating transport**. The Fermi–Walker derivative satisfies:
$$
D^{\mathrm{FW}}_{U_0}U_0 = 0, \qquad V\in E_{U_0}\Rightarrow D^{\mathrm{FW}}_{U_0}V\in E_{U_0}, \qquad V\in E_{U_0}\Rightarrow D^{\mathrm{FW}}_{U_0}V = \Pi\!\left(\frac{dV}{d\tau}\right),
$$
where $\Pi$ is the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]]. For an **inertial** observer ($A_0 = 0$) the Fermi–Walker derivative equals the absolute derivative, $D^{\mathrm{FW}}_{U_0}V = dV/d\tau$.

> [!note]- Derivation of the key properties
> **$D^{\mathrm{FW}}_{U_0}U_0 = 0$:** with $V = U_0$, use $U_0\cdot U_0 = +1$, $A_0\cdot U_0 = 0$, $dU_0/d\tau = cA_0$:
> $$D^{\mathrm{FW}}_{U_0}U_0 = cA_0 - c[(+1)A_0 - 0\cdot U_0] = cA_0 - cA_0 = 0.$$
> **Projection identity on the rest space:** let $V\in E_{U_0}$, so $U_0\cdot V = 0$. Then
> $$D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} - c[0\cdot A_0 - (A_0\cdot V)U_0] = \frac{dV}{d\tau} + c(A_0\cdot V)U_0.$$
> Now differentiate the constant $U_0\cdot V = 0$: $A_0\cdot V + U_0\cdot\dfrac{dV}{d\tau} = 0$ (since $dU_0/d\tau = A_0$ with $c=1$), so $c(A_0\cdot V) = -U_0\cdot\dfrac{dV}{d\tau}$ (with $c$: $cA_0\cdot V = -U_0\cdot dV/d\tau$). Hence
> $$D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} - \Big(U_0\cdot\frac{dV}{d\tau}\Big)U_0 = \Pi\!\left(\frac{dV}{d\tau}\right),$$
> the orthogonal projection of the absolute derivative onto the rest space. This both shows $D^{\mathrm{FW}}_{U_0}V\in E_{U_0}$ and identifies the Fermi–Walker derivative with the projected absolute derivative. $\blacksquare$

---

# Categorical / Structural Definition

The three derivatives are three **connections along the worldline** — covariant-derivative operators on the bundle of vectors over $\mathcal{L}_0$ — differing by their connection coefficients along the curve. The absolute derivative is the flat (trivial) connection $d/d\tau$. The Fermi–Walker derivative is the flat connection corrected by the Fermi–Walker generator: $D^{\mathrm{FW}}_{U_0} = d/d\tau - \Omega_{\mathrm{FW}}$, where $\Omega_{\mathrm{FW}}\in\mathfrak{so}(1,3)$ is the boost part of the four-rotation. The observer derivative further subtracts the rotation generator: $D_{\mathcal{O}} = d/d\tau - \Omega = D^{\mathrm{FW}}_{U_0} - \Omega_{\mathrm{rot}}$. In bundle language, Fermi–Walker transport is the parallel transport of the connection $d/d\tau - \Omega_{\mathrm{FW}}$; it is the *unique* metric connection along the worldline that transports $U_0$ into itself (i.e. has $U_0$ as a parallel section) while being torsion-free relative to the four-acceleration. The defining feature — $D^{\mathrm{FW}}_{U_0}U_0 = 0$ together with metric-compatibility — is exactly the condition that singles out Fermi–Walker transport among all transports along the curve.

In [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian-geometry]] terms, the absolute derivative is the flat-spacetime restriction of the covariant derivative $\nabla_{U_0}$ along the worldline, and Fermi–Walker transport is the standard modification of parallel transport that keeps a frame "as non-rotating as possible" along a non-geodesic curve. On a geodesic (inertial worldline, $A_0 = 0$) the Fermi–Walker correction vanishes and Fermi–Walker transport *is* parallel transport.

---

# Relate to Other Fields / Compression

The Fermi–Walker derivative is the relativistic law of the **gyroscope**: a torque-free spinning top carried along a worldline keeps its spin axis Fermi–Walker transported, and the residual rotation this predicts for an accelerated path is **Thomas precession**, the kinematic effect that supplies the famous factor of $\tfrac12$ in atomic spin–orbit coupling. In rotating-frame mechanics, the observer derivative's extra term $-\vec\omega\times_{U_0}V$ is precisely the **Coriolis-type** term: $\vec\omega$ is the angular velocity of the observer's frame, and the difference between the absolute and observer derivatives is the relativistic version of the classical relation $(d/dt)_{\text{inertial}} = (d/dt)_{\text{rotating}} + \boldsymbol\omega\times$. In [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]], Fermi–Walker transport along an observer's worldline is what defines the non-rotating local frame underlying Fermi normal coordinates and the operational meaning of "non-rotating" in the presence of gravity.

**True name:** the Fermi–Walker derivative is *the projected absolute derivative on the rest space, $\Pi(dV/d\tau)$, extended to all vectors so that $U_0$ is parallel* — operationally, *the rate of change a gyroscope measures*. The absolute, Fermi–Walker, and observer derivatives differ by which generators of the four-rotation are subtracted: none, the boost part, or all of it.

---

# Examples / Corollaries

**Is an instance — a Fermi–Walker-transported gyroscope on an accelerated worldline.** A spin vector $S\in U_0^\perp$ carried with $D^{\mathrm{FW}}_{U_0}S = 0$ stays in the rest space and represents a non-rotating gyroscope; on a curved (accelerated) worldline its components in a fixed lab frame nonetheless change, and integrating around a closed orbit gives the Thomas precession. This is the canonical use of the Fermi–Walker derivative.

**Is an instance — the absolute derivative for an inertial observer.** When $A_0 = 0$, all three derivatives' acceleration terms vanish: $D^{\mathrm{FW}}_{U_0}V = dV/d\tau$, and if also $\vec\omega = 0$ then $D_{\mathcal{O}}V = dV/d\tau$ as well. For an inertial, non-rotating observer the distinctions collapse — the simplest case.

**Is NOT an instance — using the absolute derivative as the gyroscope law.** Setting $dV/d\tau = 0$ (absolute parallel transport) for a spin vector on an accelerated worldline is *wrong*: it does not preserve the rest space ($U_0\cdot V$ would change), so the "spin" tilts out of space, and it does not even keep $U_0$ as the time axis. The absolute derivative is not the non-rotating transport; the Fermi–Walker derivative is. This is the calibration that the four-acceleration correction is essential.

**Is NOT an instance — using the observer derivative to detect rotation.** A gyroscope obeying $D_{\mathcal{O}}S = 0$ would, by construction, be fixed in the observer's frame — including the frame's spin $\vec\omega$ — so it could never reveal that the frame rotates. The observer derivative subtracts $\vec\omega$ and is therefore blind to it; the Fermi–Walker derivative keeps $\vec\omega$ visible, which is why a gyroscope (governed by Fermi–Walker) detects the frame's rotation. This distinguishes the two corrected derivatives.

**Corollary — three derivatives, three subtractions.** $\dfrac{dV}{d\tau}$ subtracts nothing; $D^{\mathrm{FW}}_{U_0}V = \dfrac{dV}{d\tau} - \Omega_{\mathrm{FW}}(V)$ subtracts the four-acceleration tilt; $D_{\mathcal{O}}V = \dfrac{dV}{d\tau} - \Omega(V)$ subtracts the whole four-rotation. The Fermi–Walker derivative sits exactly in between, and $D_{\mathcal{O}} = D^{\mathrm{FW}}_{U_0} - \vec\omega\times_{U_0}$.

**Corollary — Fermi–Walker transport is metric.** Because $\Omega_{\mathrm{FW}}\in\mathfrak{so}(1,3)$ is antisymmetric, Fermi–Walker transport preserves inner products: $\tfrac{d}{d\tau}(V\cdot W) = D^{\mathrm{FW}}_{U_0}V\cdot W + V\cdot D^{\mathrm{FW}}_{U_0}W$, so two Fermi–Walker-transported vectors keep their lengths and angles. A transported gyroscope keeps its spin magnitude.

**Calibration check.** You should be able to: (1) verify $D^{\mathrm{FW}}_{U_0}U_0 = 0$ and $D^{\mathrm{FW}}_{U_0}V = \Pi(dV/d\tau)$ for $V\in U_0^\perp$; (2) explain why the absolute derivative is the *wrong* gyroscope law (it does not preserve the rest space); and (3) state the three-derivative relation $D_{\mathcal{O}} = D^{\mathrm{FW}}_{U_0} - \vec\omega\times_{U_0}$ and which motion each derivative subtracts.

---

# Unlocked by This

> [!tip] Thomas Precession *(from Accelerated Observers)*
> Integrating the Fermi–Walker transport law for a gyroscope around a circular orbit yields **Thomas precession** — the kinematic rotation of an accelerated, non-rotating spin relative to the lab frame — the source of the factor of $\tfrac12$ in atomic fine structure and the kinematic heart of the BMT equation, developed in [[Special Relativity XVI — Accelerated Observers]].

> [!tip] The Spin Four-Vector and the BMT Equation *(from Relativistic Spin Dynamics)*
> A particle's [[Def - Spin Four-Vector|spin four-vector]] $S$ (orthogonal to $U_0$) is Fermi–Walker transported in the absence of torque; adding the electromagnetic torque gives the **Bargmann–Michel–Telegdi equation** for spin precession in a field, the basis of $g{-}2$ measurements ([[Special Relativity XIV — Angular Momentum and Spin]]).

> [!tip] Fermi Normal Coordinates and Gyroscopes in Gravity *(from General Relativity)*
> In curved spacetime, Fermi–Walker transport along an observer's worldline defines the **non-rotating local frame** and Fermi normal coordinates; gyroscopes in orbit precess by the **geodetic** and **frame-dragging (Lense–Thirring)** effects, measured by Gravity Probe B, which are the curved-spacetime corrections to the flat Fermi–Walker law of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]].
