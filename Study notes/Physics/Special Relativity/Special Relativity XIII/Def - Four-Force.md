---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \operatorname{diag}(+1,-1,-1,-1)$, so a timelike vector has $X\cdot X > 0$. A particle of rest mass $m$ has [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$ (normalised $U\cdot U = 1$), [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A^\mu = dU^\mu/d\tau$ (with $A\cdot U = 0$), and [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = mU^\mu = (E,\mathbf{p})$, parametrised by [[Def - Proper Time|proper time]] $\tau$. The four-force is $F^\mu$; the ordinary three-force in a frame is $\mathbf{f} = d\mathbf{p}/dt$, related to coordinate time $t$ by $dt/d\tau = \gamma$. Full registry on [[Special Relativity XIII — Energy and Momentum]].

> [!warning] Convention
> Gourgoulhon writes the four-force as the linear form $\boldsymbol{f} = d\boldsymbol{p}/d\tau$ and finds $\langle\boldsymbol{f}, \vec u\rangle = -c\,dm/d\tau$ in mostly-plus signature; the *pure* (Minkowski) force satisfies $\langle\boldsymbol{f},\vec u\rangle = 0$. Translating to our mostly-minus signature and $c = 1$: $F = dP/d\tau$ (a vector), the orthogonality identity becomes $F\cdot U = dm/d\tau$, and a pure four-force satisfies $F\cdot U = 0$ and so preserves the rest mass. The form $f = mc^2\vec a + c(dm/d\tau)\vec u$ becomes $F = mA + (dm/d\tau)U$.

---

# Axiom Motivation

Conservation of four-momentum says that an *isolated* particle has constant four-momentum, $dP/d\tau = 0$ — its worldline is straight, its mass and velocity constant (the law of inertia). The question this page answers is what happens when the particle is *not* isolated: when something pushes on it. In Newtonian mechanics the answer is Newton's second law, $\mathbf{f} = d\mathbf{p}/dt$, the force equals the rate of change of momentum. We want the relativistic counterpart, and the design problem is exactly the one that governed the four-velocity: the law must be a *tensor equation*, the same in every inertial frame, which means it must relate genuine four-vectors.

The Newtonian law $\mathbf{f} = d\mathbf{p}/dt$ fails this test on two counts. Its left side is a three-vector, its right side is differentiated with respect to the frame-dependent coordinate time $t$, and neither is a four-vector. So the relativistic law cannot simply be this with bold letters. The fix is dictated by what worked before: differentiate the [[Def - Four-Momentum and Rest Mass|four-momentum]] (a four-vector) with respect to **proper time** (a scalar). The result $dP/d\tau$ is a four-vector divided by a scalar, hence a four-vector, and *defining* the four-force to be this quantity, $F^\mu := dP^\mu/d\tau$, guarantees that the equation of motion $F^\mu = dP^\mu/d\tau$ is a tensor equation. This is the entire content of the definition: it is the unique covariant object that reduces to "rate of change of momentum" and is built to transform correctly.

There is an important honesty here, easy to miss: the equation $F^\mu = dP^\mu/d\tau$ is *empty of physics on its own*. It does not say what causes the force or how large it is; it merely names the proper-time derivative of the four-momentum "the four-force". Physical content enters only when the *form* of $F$ is supplied by a specific interaction — for the electromagnetic case, $F^\mu = q\,F^\mu{}_\nu U^\nu$ (the Lorentz force), and that specification, not $F = dP/d\tau$, is the physical postulate. The definition is a covariant container; the interactions fill it.

Now examine the structure of $F$ by expanding $P = mU$:
$$
F = \frac{dP}{d\tau} = \frac{d(mU)}{d\tau} = m\frac{dU}{d\tau} + \frac{dm}{d\tau}U = mA + \frac{dm}{d\tau}U.
$$
Two pieces appear, and the second is the genuinely relativistic novelty. The first piece $mA$ is "mass times four-acceleration", the direct analogue of Newton's $m\mathbf{a}$, and it changes the *direction* of $U$ in spacetime (turning the worldline). The second piece $\tfrac{dm}{d\tau}U$ has *no Newtonian counterpart*: it accounts for the possibility that the rest mass itself changes — that the particle gains or loses internal energy (an atom de-exciting, a composite body heating up). In Newtonian mechanics mass is sacrosanct; relativistically, because mass is a form of energy ($E = mc^2$), a force can change it, and the four-force has a component along $U$ that does exactly this.

Contracting $F$ with the four-velocity reveals which component carries the mass change. Differentiating the normalisation $U\cdot U = 1$ gives $A\cdot U = 0$, so the $mA$ piece is orthogonal to $U$ and drops out; the contraction is
$$
F\cdot U = \Big(mA + \frac{dm}{d\tau}U\Big)\cdot U = m\,(A\cdot U) + \frac{dm}{d\tau}(U\cdot U) = \frac{dm}{d\tau}.
$$
So the projection of the four-force *onto* the four-velocity is precisely the rate of change of the rest mass. This is the key structural fact, and it motivates the most useful sub-definition: a **pure** (or **Minkowski**) four-force is one orthogonal to the four-velocity, $F\cdot U = 0$. By the identity just derived, a pure force has $dm/d\tau = 0$ — *it preserves the rest mass*. This is exactly the class of forces that keep a particle's identity intact (an electron stays an electron), and it is no accident that the one fundamental relativistic force, the electromagnetic Lorentz force, is pure: the antisymmetry of the field tensor makes $F\cdot U = q\,F_{\mu\nu}U^\mu U^\nu = 0$ automatically, because a symmetric quantity (the contraction $U^\mu U^\nu$) summed against an antisymmetric one ($F_{\mu\nu}$) vanishes.

Why insist on the orthogonality constraint as the *definition* of "pure" rather than just noting it? Because it is the relativistic statement that the four-force, like the four-acceleration, has only **three** independent components, not four. The four-velocity already has its length fixed ($U\cdot U = 1$), so a force that changes only the *direction* of $U$ (not its mass-content) is confined to the three-dimensional subspace orthogonal to $U$. The constraint $F\cdot U = 0$ is what enforces "this force does not create or destroy rest energy", and it is what makes the relativistic Newton's second law for an ordinary force a statement about three numbers, matching the three components of the everyday force vector.

---

# The Definition

Let $\mathcal{P}$ be a particle of rest mass $m$ with [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu$, parametrised by [[Def - Proper Time|proper time]] $\tau$. The **four-force** acting on $\mathcal{P}$ is the proper-time derivative of its four-momentum,
$$
F^\mu \;:=\; \frac{dP^\mu}{d\tau}.
$$
It vanishes identically if and only if $\mathcal{P}$ is isolated (constant four-momentum). Writing $P = mU$ gives the decomposition
$$
F \;=\; m\,A + \frac{dm}{d\tau}\,U,
\qquad A^\mu = \frac{dU^\mu}{d\tau}\ \text{the four-acceleration},
$$
and contracting with the four-velocity (using $A\cdot U = 0$, $U\cdot U = 1$) gives the **mass-evolution identity**
$$
F\cdot U \;=\; \frac{dm}{d\tau}.
$$

A **pure four-force** (or **Minkowski force**) is a four-force orthogonal to the four-velocity,
$$
F\cdot U \;=\; 0,
$$
equivalently one that **preserves the rest mass**, $dm/d\tau = 0$; for a pure force $F = mA$, mass times four-acceleration. The dimension of a four-force is that of an ordinary force (mass $\times$ length $/$ time$^2$); the unit is the newton. The relation $F^\mu = dP^\mu/d\tau$ is a definition, not a physical law; physical content is supplied only by specifying the form of $F$ for a given interaction — the canonical example being the electromagnetic **Lorentz four-force**
$$
F^\mu \;=\; q\,F^\mu{}_\nu\,U^\nu,
$$
with $q$ the charge and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ the antisymmetric field-strength tensor; antisymmetry guarantees $F\cdot U = 0$, so the Lorentz force is pure and conserves the rest mass.

---

# Categorical / Structural Definition

Structurally the four-force is a **covector field along the worldline** valued in the cotangent space of Minkowski space at each event — or, with the metric used to raise the index, a tangent vector $F^\mu$ — and the equation of motion $F = dP/d\tau$ is the statement that the four-momentum is *not parallel-transported* along the worldline, $F$ being the obstruction. In flat spacetime parallel transport is trivial (constant components), so $F = dP/d\tau$; in the curved spacetime of general relativity the ordinary derivative is replaced by the covariant derivative $\nabla_U P$, and a geodesic (free fall) is the curved-space analogue of a force-free worldline, $\nabla_U P = 0$.

The orthogonality constraint $F\cdot U = 0$ for a pure force has a clean structural reading: the four-momentum of a mass-preserving particle is confined to the **mass shell** $P\cdot P = m^2$ (a fixed hyperboloid), and any four-force tangent to that hyperboloid — that is, orthogonal to $P$, hence to $U$ — moves the four-momentum *along* the shell without changing $m$. A force with a component off the shell (along $U$, i.e. along $P$) changes the radius $m$ of the shell, which is the mass-changing case $dm/d\tau = F\cdot U \ne 0$. Thus "pure force" $=$ "tangent to the mass shell", and the constraint $F\cdot U = 0$ is the tangency condition.

---

# Relate to Other Fields / Compression

In **Newtonian mechanics** the four-force is the unification of two separate things: the ordinary three-force $\mathbf{f} = d\mathbf{p}/dt$ (the spatial part of $F$, up to a factor of $\gamma$) and the *power* $dE/dt = \mathbf{f}\cdot\mathbf{u}$ (the time part), which Newton treated independently. The relativistic equation of motion $F = dP/d\tau$ contains Newton's second law and the work–energy theorem as its space and time components (see [[Thm - Relativistic Newton's Second Law]]).

In **general relativity** the four-force is what remains of the equation of motion after gravity is removed from the right side. Free fall is *not* a four-force in GR; it is the absence of one — a freely-falling particle has $\nabla_U U = 0$ (a geodesic), and gravity is encoded in the connection, not in a force. A genuine four-force (electromagnetic, say) then deflects the particle *off* its geodesic, $\nabla_U P = F$. This is the precise sense in which "gravity is not a force" in general relativity.

**True name:** the operational characterisation of a *pure* four-force, distinct from "orthogonal to the four-velocity", is **a force that preserves the rest mass**, $dm/d\tau = 0$. This is what the orthogonality buys you in practice: when a problem involves a force that keeps the particle's identity (any electromagnetic force on a fixed charge), you may treat $m$ as constant, so $E = \gamma m$ tracks the speed and the spatial equation $d\mathbf{p}/dt = \mathbf{f}$ is enough to solve the motion.

---

# Examples / Corollaries

**Is an instance — the Lorentz force on a charge.** A charge $q$ in an electromagnetic field experiences $F^\mu = q\,F^\mu{}_\nu U^\nu$, whose spatial part for an inertial observer is $\mathbf{f} = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$ and whose time part is the rate of working $q\,\mathbf{E}\cdot\mathbf{u}$. The antisymmetry $F_{\mu\nu} = -F_{\nu\mu}$ gives $F\cdot U = q F_{\mu\nu}U^\mu U^\nu = 0$ (a symmetric product against an antisymmetric tensor), so the force is **pure** and the electron's rest mass is preserved as it is accelerated.

**Is an instance — a mass-changing force on a composite particle.** A rocket emitting exhaust, or an atom emitting a photon, has $dm/d\tau \ne 0$: the rest mass of the remaining system decreases. The four-force then has a nonzero component $\tfrac{dm}{d\tau}U$ along the four-velocity, $F\cdot U = dm/d\tau < 0$. This is *not* a pure force; the internal energy of the system is changing.

**Is NOT an instance — a "force" with a frame-dependent expression.** The Newtonian $\mathbf{f} = m\,d^2\mathbf{x}/dt^2$ is not a four-force: it is a three-vector, differentiated with respect to the frame-dependent coordinate time, with no clean transformation law. Equating it to $dP/d\tau$ would mix a non-tensor with a tensor and produce a law that holds in one frame and fails in another. The four-force must be $dP/d\tau$, with the ordinary force recovered as the (boosted) spatial part.

**Is NOT an instance — gravity, in general relativity.** In GR the "gravitational force" is not a four-force at all. A freely-falling particle has $\nabla_U P = 0$ — it is on a geodesic, force-free — and what looks like a gravitational force is an artefact of using a non-inertial coordinate frame. A real four-force is something that pushes a particle *off* its geodesic. (In the flat-spacetime approximation of Newtonian gravity one may model it as a four-force, but the equivalence principle shows this is not fundamental.)

**Corollary — a pure force preserves the mass shell.** If $F\cdot U = 0$ then $dm/d\tau = 0$, so $P\cdot P = m^2$ stays constant along the worldline: the four-momentum slides along a fixed mass-shell hyperboloid. This is why an electron in any electromagnetic field remains an electron with the same rest mass, however violently it is accelerated.

**Corollary — the power is the work component.** Projecting $F = dP/d\tau$ onto an inertial observer, the time component gives $dE/d\tau =$ (time part of $F$), which converts via $d/d\tau = \gamma\,d/dt$ to $dE/dt = \mathbf{f}\cdot\mathbf{u}$ for a pure force — the rate of working equals the power delivered, the relativistic work–energy theorem ([[Thm - Relativistic Newton's Second Law]]).

**Calibration check.** If you have understood the definition you should be able to: (1) derive the mass-evolution identity $F\cdot U = dm/d\tau$ from $F = dP/d\tau$ and the normalisation $U\cdot U = 1$; (2) explain why the electromagnetic Lorentz force preserves rest mass, in one line — its $F\cdot U = qF_{\mu\nu}U^\mu U^\nu$ vanishes by antisymmetry; (3) state what physical content the equation $F^\mu = dP^\mu/d\tau$ carries on its own — none, until the form of $F$ is specified by an interaction.

---

# Unlocked by This

> [!tip] The Relativistic Equation of Motion *(from §13.3)*
> Projecting $F^\mu = dP^\mu/d\tau$ onto an inertial observer gives Newton's second law in covariant form: the spatial part is $d\mathbf{p}/dt = \mathbf{f}$ with $\mathbf{p} = \gamma m\mathbf{u}$, the time part the work–energy theorem $dE/dt = \mathbf{f}\cdot\mathbf{u}$. The acceleration is *not* parallel to the force. See [[Thm - Relativistic Newton's Second Law]].

> [!tip] The Lorentz Four-Force and Accelerators *(from Electromagnetism)*
> The one fundamental pure four-force, $F^\mu = q\,F^\mu{}_\nu U^\nu$, drives every particle accelerator: a uniform electric field gives the hyperbolic worldline of a linear accelerator (worked out in [[Special Relativity XXI — The Electromagnetic Field|Special Relativity XXI]]), a uniform magnetic field the circular motion of a cyclotron at frequency $\omega = qB/\gamma m$. The full theory of the electromagnetic field and its force is [[Special Relativity XXI — The Electromagnetic Field|Special Relativity XXI]].

> [!tip] The Free Particle from an Action Principle *(from Analytical Mechanics)*
> Setting $F = 0$ recovers $dP^\mu/d\tau = 0$, the Euler–Lagrange equation of the action $S = -m\int d\tau$. Adding a vector-potential coupling $q\int A_\mu\,dX^\mu$ produces the Lorentz four-force as the resulting equation of motion, so the electromagnetic force itself descends from an action principle — the route into the Lagrangian formulation of [[Special Relativity XV — The Principle of Least Action|Special Relativity XV]].
