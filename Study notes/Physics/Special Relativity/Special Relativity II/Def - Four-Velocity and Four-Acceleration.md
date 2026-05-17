---
type: definition
subject: special-relativity
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Vector"
  - "Def - The Lorentz Transformation"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$ (factors of $c$ restored where the contrast with the Newtonian limit is the point). A worldline is $X^\mu(\tau) = (t(\tau),\mathbf{x}(\tau))$, parametrised by [[Def - Proper Time|proper time]] $\tau$. The Minkowski metric is $\eta_{\mu\nu} = \operatorname{diag}(+1,-1,-1,-1)$ and the inner product is $A\cdot B = \eta_{\mu\nu}A^\mu B^\nu = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$. A particle's ordinary three-velocity in a frame is $\mathbf{u} = d\mathbf{x}/dt$, speed $u$, Lorentz factor $\gamma = (1-u^2)^{-1/2}$; its three-acceleration is $\mathbf{a} = d\mathbf{u}/dt$, and $\dot\gamma = d\gamma/dt$. A Lorentz transformation is $\Lambda^\mu{}_\nu$. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Axiom Motivation

In Newtonian mechanics, velocity is the rate of change of position, $\mathbf{u} = d\mathbf{x}/dt$, and it is the object every other dynamical quantity is built from. We want to carry this into special relativity, and the spacetime picture tells us what to aim for: a particle's history is a curve — a worldline — through Minkowski space, and the natural notion of "velocity" is the **tangent vector to that curve**. The desideratum is therefore a four-component object, the four-velocity, that points along the worldline and transforms as a [[Def - Four-Vector|four-vector]] — that is, as $U^\mu \to \Lambda^\mu{}_\nu U^\nu$ under a Lorentz transformation — so that any law written with it looks the same to every inertial observer.

The naive attempt is to differentiate the [[Def - Four-Vector|four-position]] with respect to coordinate time, $V^\mu = dX^\mu/dt$. This fails, and the reason is precise. The four-position $X^\mu$ is a four-vector, so under a boost $X^\mu \to \Lambda^\mu{}_\nu X^\nu$. But $t$ is the time *coordinate* of one frame, not an invariant — under the same boost $t$ itself changes. Dividing a four-vector by a frame-dependent number does not give a four-vector; $V^\mu = dX^\mu/dt$ transforms in a tangled, non-tensorial way, and a law built from it would not respect Postulate 1. Concretely, in the particle's own rest frame $V^0 = dt/dt = 1$, but a four-vector with time component $1$ in one frame does not have time component $1$ in another, so $V^\mu$ cannot be a four-vector.

The fix is forced and it is the whole reason [[Def - Proper Time|proper time]] was introduced. Proper time $\tau$ is a Lorentz *scalar* — the same number for every observer. Differentiating a four-vector with respect to a scalar yields a four-vector. So we *must* define the four-velocity as
$$U^\mu = \frac{dX^\mu}{d\tau},$$
and the difference from the naive $V^\mu$ is exactly one factor of $\gamma$, since $d\tau = dt/\gamma$. That single factor is what converts a non-tensor into a tensor. There is no freedom here: any other parameter would either fail to be invariant or fail to reduce to ordinary velocity at low speed.

This definition comes with a bonus that looks like a constraint and is in fact a gift. The four-velocity is **normalised**: $U\cdot U = c^2$ always, for every particle, regardless of its motion. The reason is that $U^\mu d\tau = dX^\mu$, so $U\cdot U\,d\tau^2 = dX\cdot dX = ds^2 = c^2 d\tau^2$. This resolves a puzzle: Newtonian velocity is three numbers, but a four-vector is four — where did the fourth degree of freedom come from? It did not. The normalisation $U\cdot U = c^2$ is one equation that ties the four components together, leaving exactly three free, as it must. The four-velocity is a *constrained* four-vector, confined to a hyperboloid in velocity space.

Acceleration is then immediate. The Newtonian acceleration is the second time-derivative of position; the relativistic four-acceleration must be the second *proper-time* derivative, $A^\mu = dU^\mu/d\tau$, for the same tensorial reason. And differentiating the constraint $U\cdot U = c^2$ — a constant — gives $2\,U\cdot A = 0$: the four-acceleration is automatically Minkowski-orthogonal to the four-velocity. This is not an extra assumption; it is what the normalisation forces, and it is the relativistic statement that a force cannot change a particle's rest mass, only redirect it in spacetime.

---

# The Definition

Let a particle move on a timelike worldline $X^\mu(\tau)$ through Minkowski space, parametrised by [[Def - Proper Time|proper time]] $\tau$. Work in an inertial frame in which the particle has three-velocity $\mathbf{u}$, speed $u$, and Lorentz factor $\gamma = (1-u^2/c^2)^{-1/2}$.

**Four-velocity.** The **four-velocity** of the particle is the proper-time derivative of its four-position,
$$U^\mu \;=\; \frac{dX^\mu}{d\tau}.$$
Using $dt/d\tau = \gamma$ and the chain rule, its components in the chosen frame are
$$U^\mu \;=\; \frac{dt}{d\tau}\,\frac{dX^\mu}{dt} \;=\; \gamma\,(c,\ \mathbf{u}) \;=\; (\gamma c,\ \gamma\mathbf{u}).$$
Because $X^\mu$ is a [[Def - Four-Vector|four-vector]] and $\tau$ is a Lorentz scalar, $U^\mu$ is a four-vector: under a [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$, it transforms as $U^\mu \to \Lambda^\mu{}_\nu U^\nu$. It satisfies the **normalisation constraint**
$$U\cdot U \;=\; \eta_{\mu\nu}U^\mu U^\nu \;=\; \gamma^2(c^2 - u^2) \;=\; c^2,$$
a Lorentz-invariant identity holding for every particle. Hence the four-velocity is a future-pointing timelike four-vector of fixed Minkowski length, and carries only three independent components.

**Four-acceleration.** The **four-acceleration** is the proper-time derivative of the four-velocity,
$$A^\mu \;=\; \frac{dU^\mu}{d\tau} \;=\; \frac{d^2 X^\mu}{d\tau^2}.$$
It is a four-vector for the same reason. Its components, with $\mathbf{a} = d\mathbf{u}/dt$ the ordinary three-acceleration and $\dot\gamma = d\gamma/dt$, are
$$A^\mu \;=\; \gamma\,\frac{dU^\mu}{dt} \;=\; \gamma\big(\dot\gamma c,\ \dot\gamma\,\mathbf{u} + \gamma\,\mathbf{a}\big).$$
Differentiating the normalisation $U\cdot U = c^2$ with respect to $\tau$ gives the **orthogonality relation**
$$A\cdot U \;=\; \eta_{\mu\nu}A^\mu U^\nu \;=\; 0,$$
so the four-acceleration is always Minkowski-orthogonal to the four-velocity. In the **instantaneous rest frame** of the particle ($\mathbf{u}=0$, $\dot\gamma=0$) the four-acceleration reduces to $A^\mu = (0,\mathbf{a}_0)$, with $\mathbf{a}_0$ the ordinary acceleration measured in that frame; its Minkowski length is $A\cdot A = -|\mathbf{a}_0|^2$, a Lorentz invariant called the **proper acceleration**.

---

# Relate to Other Fields / Compression

The four-velocity is, in the language of [[Multivariate Analysis I — Differentiation in Several Variables|differential geometry]], the **unit tangent vector** to a curve, parametrised by arc length. On a Riemannian manifold one parametrises a curve by its arc length $s$ and the tangent $dx^\mu/ds$ is automatically a unit vector; here the manifold is Minkowski space, the "arc length" is proper time, and $U^\mu = dX^\mu/d\tau$ is automatically of fixed Minkowski norm $c^2$. The four-acceleration $dU^\mu/d\tau$ is then the rate of turning of this tangent vector — in the curved-spacetime version it becomes the *covariant* derivative of $U^\mu$ along the worldline, and a curve with zero four-acceleration is a geodesic.

The orthogonality $A\cdot U = 0$ is the same fact as the elementary observation that the velocity of a point moving on a sphere is tangent to the sphere, hence perpendicular to the radius. There, $\mathbf{x}\cdot\mathbf{x} = R^2$ constant gives $\mathbf{x}\cdot\dot{\mathbf{x}} = 0$. Here, $U\cdot U = c^2$ constant gives $U\cdot A = 0$. Any time a vector is constrained to have fixed length, its derivative is orthogonal to it; the four-velocity living on the hyperboloid $U\cdot U = c^2$ is the relativistic instance.

The transformation law $U^\mu\to\Lambda^\mu{}_\nu U^\nu$ is what makes [[Thm - Relativistic Velocity Addition|relativistic velocity addition]] trivial. Composing velocities is, in Newtonian physics, vector addition; relativistically it is *not*, and the reason is that velocities are encoded in four-velocities, and four-velocities are combined by applying a Lorentz transformation — composing two elements of the [[Group Theory I — §1.1–1.2|Lorentz group]] — not by adding. The clean statement is the invariant contraction $U\cdot U' = c^2\gamma_{\text{rel}}$, where $\gamma_{\text{rel}}$ is the Lorentz factor of the relative speed between two particles; computing this inner product in two different frames and equating reproduces the addition formula in one line.

---

# Examples / Corollaries

**Is an instance — a particle at rest.** A stationary particle has $\mathbf{u}=0$, $\gamma=1$, so $U^\mu = (c,0,0,0)$. The normalisation gives $U\cdot U = c^2$, the simplest check. This is the four-velocity in the particle's own rest frame, and it is the configuration to which one boosts in collision problems.

**Is an instance — recovering velocity addition.** Take a particle of four-velocity $U^\mu = \gamma_u(c,\mathbf{u})$ in frame $S$, and boost to a frame $S'$ moving at speed $v$ along the $x$-axis: $U'^\mu = \Lambda^\mu{}_\nu U^\nu$. Dividing the spatial components of $U'^\mu$ by its time component returns the particle's velocity in $S'$ — and the answer is exactly the [[Thm - Relativistic Velocity Addition|relativistic velocity addition]] formula, including the correct transverse components. The four-velocity does the bookkeeping automatically.

**Is an instance — constant proper acceleration.** A particle with $A\cdot A = -\kappa^2$ constant (constant proper acceleration $\kappa$) moves, in a fixed inertial frame, on the hyperbola $x^2 - (ct)^2 = (c^2/\kappa)^2$. Its four-velocity components are hyperbolic functions of proper time, $U^\mu = (c\cosh(\kappa\tau/c),\,c\sinh(\kappa\tau/c),0,0)$, which manifestly satisfy $U\cdot U = c^2$. See [[Ex - Hyperbolic motion under constant proper acceleration]].

**Is NOT an instance — the naive $dX^\mu/dt$.** The object $V^\mu = dX^\mu/dt = (c,\mathbf{u})$ is *not* a four-velocity: it has $V\cdot V = c^2 - u^2$, which is not invariant (it depends on the frame, since $u$ does), and it does not transform as a four-vector. It is the four-velocity missing its factor of $\gamma$. This is the standard mistake the proper-time construction exists to forbid.

**Is NOT an instance — a photon's "four-velocity".** A photon moves on a null worldline along which [[Def - Proper Time|proper time]] does not advance, so $dX^\mu/d\tau$ is the meaningless $0/0$. No matter how one normalises a four-vector tangent to a null worldline, its Minkowski length is $0$, not $c^2$. A photon simply has no four-velocity; it is described instead by its [[Def - The Four-Momentum of a Photon|null four-momentum]].

**Corollary — the orthogonality is a free equation.** Because $A\cdot U = 0$ always holds, the four-acceleration of a particle of given four-velocity is constrained to a three-dimensional subspace (the Minkowski-orthogonal complement of $U^\mu$). In the instantaneous rest frame this says $A^0 = 0$: there is no "time component" of acceleration in the rest frame, which is why $A^\mu = (0,\mathbf{a}_0)$ there.

**Calibration check.** Verify $U\cdot U = c^2$ directly from $U^\mu = \gamma(c,\mathbf{u})$; verify that $A\cdot U = 0$ follows from differentiating $U\cdot U = c^2$; and check that in the instantaneous rest frame $\dot\gamma = 0$, so the messy four-acceleration $\gamma(\dot\gamma c,\dot\gamma\mathbf{u}+\gamma\mathbf{a})$ collapses to $(0,\mathbf{a}_0)$. If you can also explain why $U^\mu$ has only three independent components despite having four entries, you have understood the definition.

---

# Unlocked by This

> [!tip] The Four-Momentum *(from this topic)*
> Multiplying the four-velocity by the invariant [[Def - Four-Momentum and Rest Mass|rest mass]] gives the **four-momentum** $P^\mu = mU^\mu$, the four-vector that is actually *conserved* in physical processes. The normalisation $U\cdot U = c^2$ becomes the mass-shell relation $P\cdot P = m^2c^2$.

> [!tip] The Four-Force and Newton's Second Law *(from this topic)*
> Setting the proper-time derivative of the four-momentum equal to a four-force gives the relativistic [[Thm - The Relativistic Equation of Motion|equation of motion]] $F^\mu = dP^\mu/d\tau$. The orthogonality $A\cdot U = 0$ becomes $F\cdot U = 0$, the statement that an ordinary force does not change the rest mass.

> [!tip] The Four-Velocity Field and the Energy–Momentum Tensor *(from Continuum Mechanics and General Relativity)*
> Promoting the four-velocity from a single particle to a **field** $U^\mu(x)$ defined throughout a region describes a continuous medium; the **energy–momentum tensor** of a perfect fluid, $T^{\mu\nu} = (\rho+p)U^\mu U^\nu + p\,\eta^{\mu\nu}$, is built from it.
