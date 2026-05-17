---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$, with $c$ restored where the Newtonian comparison matters. A particle has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E/c,\mathbf{p})$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu = \gamma(c,\mathbf{u})$, four-acceleration $A^\mu$, rest mass $m$, parametrised by [[Def - Proper Time|proper time]] $\tau$. The four-force is $F^\mu$; the ordinary three-force is $\mathbf{f}$. The Minkowski inner product is $A\cdot B = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Notation note

This page restates Newton's second law in Lorentz-covariant form. It has a `# Statement` section so it can be transcluded.

# Statement

> **The relativistic equation of motion.** The Lorentz-covariant form of Newton's second law for a particle of constant rest mass $m$ is
> $$F^\mu \;=\; \frac{dP^\mu}{d\tau} \;=\; m\,A^\mu,$$
> where $P^\mu$ is the [[Def - Four-Momentum and Rest Mass|four-momentum]], $A^\mu = dU^\mu/d\tau$ the [[Def - Four-Velocity and Four-Acceleration|four-acceleration]], $\tau$ the [[Def - Proper Time|proper time]], and $F^\mu$ a **four-force**. The four-force is constrained to be Minkowski-orthogonal to the four-velocity,
> $$F\cdot U \;=\; 0,$$
> which is precisely the condition that the force not change the particle's rest mass. In an inertial frame where the particle moves with velocity $\mathbf{u}$, speed $u$, Lorentz factor $\gamma$, the four-force has components
> $$F^\mu \;=\; \big(\gamma\,\mathbf{u}\cdot\mathbf{f}/c,\ \ \gamma\,\mathbf{f}\big),$$
> where $\mathbf{f} = d\mathbf{p}/dt$ is the ordinary three-force acting on the relativistic three-momentum. The spatial part of $F^\mu = dP^\mu/d\tau$ then reproduces $\mathbf{f} = d\mathbf{p}/dt$ and the time part reproduces the work–energy relation $dE/dt = \mathbf{u}\cdot\mathbf{f}$. When $F^\mu = 0$ the equation reduces to conservation of four-momentum, $dP^\mu/d\tau = 0$.

---

# Motivation

Newton's second law, $\mathbf{f} = d\mathbf{p}/dt = m\mathbf{a}$, is the centrepiece of pre-relativistic dynamics. It is built from three-vectors and from differentiation with respect to coordinate time $t$. By now we know exactly why that is unacceptable in relativity: $t$ is a frame-dependent coordinate, three-vectors are not the natural objects, and a law written this way will not look the same to every inertial observer. The question this theorem answers is the inevitable last step of the topic: **what is the Lorentz-covariant form of $\mathbf{f} = d\mathbf{p}/dt$?**

The answer follows the recipe that has worked for every other quantity. We have already relativised position into [[Def - Four-Vector|four-position]], velocity into [[Def - Four-Velocity and Four-Acceleration|four-velocity]], and momentum into [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu$. To relativise the *law* $\mathbf{f} = d\mathbf{p}/dt$, replace the frame-dependent rate $d/dt$ by the invariant rate $d/d\tau$, and replace the three-force $\mathbf{f}$ by a four-vector $F^\mu$. The result, $F^\mu = dP^\mu/d\tau$, is a four-vector equation: both sides transform as four-vectors, so the law is the same in every inertial frame. That is the whole construction, and it is exactly parallel to the construction of the four-velocity.

But the construction also tells us something we did not ask for. The four-force is not an arbitrary four-vector. Because $P^\mu = mU^\mu$ with $m$ constant and $U\cdot U = c^2$, differentiating gives $F^\mu = mA^\mu$ and $F\cdot U = mA\cdot U = 0$ — the four-force is *forced* to be orthogonal to the four-velocity. Three of the four components of $F^\mu$ are independent; the fourth is determined. And this constraint has a physical meaning: $F\cdot U = 0$ is the statement that an ordinary force changes a particle's *energy and momentum* but not its *rest mass*. A push speeds a particle up, but it does not turn an electron into something heavier. This is why, in practice, this equation is less central than [[Thm - Conservation of Four-Momentum|conservation of four-momentum]]: most of the dramatic relativistic processes — decays, particle creation — *do* change rest masses, and they are not the action of a four-force on a single particle but the interaction of several. The relativistic equation of motion governs a particle pushed by a genuine force; the one force that survives into the relativistic regime intact is the electromagnetic force, and writing *that* in four-vector form is the equation's main application.

---

# Sources and Targets

**Sources (Input Broadening)**

The equation $F^\mu = dP^\mu/d\tau$ applies whenever a particle of definite rest mass is acted on by a force. The skill is recognising the disguised forms of "there is a four-force".

The first disguised source is **a charged particle in an electromagnetic field.** Property $B$: a particle of charge $q$ moving through electric and magnetic fields. The bridge: the electromagnetic force has a Lorentz-covariant form, $F^\mu = q\,F^\mu{}_\nu U^\nu$, with $F^\mu{}_\nu$ the field-strength tensor; this automatically satisfies $F\cdot U = 0$ because $F_{\mu\nu}$ is antisymmetric, so $F_{\mu\nu}U^\mu U^\nu = 0$. The non-obviousness: the messy three-vector Lorentz force $\mathbf{f} = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$ is the spatial part of a clean four-vector equation. *Example:* the motion of an electron in an accelerator or a magnetic trap.

The second disguised source is **the free-particle limit, $F^\mu = 0$.** Property $B$: a particle with no force acting. The bridge: $F^\mu = 0$ makes $dP^\mu/d\tau = 0$, so $P^\mu$ is constant — the particle moves on a straight worldline at constant four-velocity. The non-obviousness: [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] for a single free particle, and the law of inertia, are the $F^\mu = 0$ case of this equation. *Example:* any particle between interactions in a collision problem.

The third disguised source is **a variational principle with a known Lagrangian.** Property $B$: a relativistic system whose dynamics come from an action $S = \int L\,d\lambda$. The bridge: the Euler–Lagrange equations $\frac{d}{d\lambda}(\partial L/\partial\dot X^\mu) = \partial L/\partial X^\mu$ are, for the relativistic particle, exactly $dP_\mu/d\tau = F_\mu$, with $F_\mu$ the generalised force $\partial L/\partial X^\mu$. The non-obviousness: this equation of motion is the Euler–Lagrange equation of the proper-time action. *Example:* deriving the Lorentz force from the action of a charge coupled to the electromagnetic potential.

**Targets (Output Amplification)**

The conclusion is the four-vector law $F^\mu = dP^\mu/d\tau = mA^\mu$ with $F\cdot U = 0$.

Combine the conclusion with **the spatial projection in a chosen frame.** Property $D$: a frame in which the particle has velocity $\mathbf{u}$. The amplified result $E$: the spatial part of $F^\mu = dP^\mu/d\tau$ reads $\gamma\mathbf{f} = \gamma\,d\mathbf{p}/dt$, i.e. $\mathbf{f} = d\mathbf{p}/dt$ with $\mathbf{p} = \gamma m\mathbf{u}$ the relativistic momentum — Newton's law survives verbatim, provided "momentum" means the relativistic momentum.

Combine the conclusion with **the time projection.** Property $D$: the same frame. The amplified result $E$: the time component of $F^\mu = dP^\mu/d\tau$ is the work–energy relation $dE/dt = \mathbf{u}\cdot\mathbf{f}$ — the rate of change of total energy equals the rate of working of the force. The orthogonality $F\cdot U = 0$ is what guarantees the time and space components are consistent, encoding no independent information.

Combine the conclusion with **the constraint $F\cdot U = 0$ and constant rest mass.** Property $D$: the requirement that the rest mass not change. The amplified result $E$: $F\cdot U = 0$ is *equivalent* to $d(P\cdot P)/d\tau = 0$, i.e. $dm/d\tau = 0$. A four-force orthogonal to the four-velocity is precisely a force that accelerates a particle without altering what it is.

---

# Why Is It True

The equation should feel inevitable, because it is the only thing the construction principle of the whole topic could produce.

We have a recipe, used for every quantity so far: to relativise a Newtonian object, replace coordinate-time derivatives by proper-time derivatives, and replace three-vectors by four-vectors. Newton's second law is $\mathbf{f} = d\mathbf{p}/dt$. Apply the recipe: $\mathbf{p}$ becomes the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu$, $d/dt$ becomes $d/d\tau$, and $\mathbf{f}$ becomes a four-vector $F^\mu$. The result is $F^\mu = dP^\mu/d\tau$. There is no other candidate: any equation that is to (i) be a four-vector equation, hence frame-independent, and (ii) reduce to $\mathbf{f} = d\mathbf{p}/dt$ at low speed, must have this form. The right-hand side $dP^\mu/d\tau$ is a four-vector because $P^\mu$ is a four-vector and $\tau$ is a scalar; setting it equal to a four-vector $F^\mu$ produces a covariant law. This is the same logic that built the four-velocity, applied one level up.

Why must the four-force be orthogonal to the four-velocity? This is not an extra postulate but a consequence, and seeing it is the heart of the intuition. A particle of constant rest mass has $P\cdot P = m^2c^2$, a constant. Differentiate with respect to proper time:
$$\frac{d}{d\tau}(P\cdot P) = 2\,P\cdot\frac{dP}{d\tau} = 2\,P\cdot F = 2m\,U\cdot F.$$
The left side is the derivative of a constant, so it is zero, hence $U\cdot F = 0$. The four-force *cannot* have a component along the four-velocity, because such a component would change the four-momentum's Minkowski length, which is the rest mass. This is the same geometry as in [[Def - Four-Velocity and Four-Acceleration|four-acceleration]]: anything constrained to a surface of fixed length has its rate of change tangent to the surface, orthogonal to the radius. The four-force lives in the three-dimensional subspace orthogonal to $U^\mu$ — it can redirect and re-energise the particle but cannot alter what it is.

And why does the spatial part reproduce the familiar $\mathbf{f} = d\mathbf{p}/dt$? Because $d/d\tau = \gamma\,d/dt$, the spatial part of $F^\mu = dP^\mu/d\tau$ reads $F^{\text{spatial}} = \gamma\,d\mathbf{p}/dt$. If we *define* the three-force as $\mathbf{f} = d\mathbf{p}/dt$ — the rate of change of the relativistic momentum — then $F^{\text{spatial}} = \gamma\mathbf{f}$, and the law is just $\mathbf{f} = d\mathbf{p}/dt$ dressed with a factor of $\gamma$ that accounts for the proper-time-versus-coordinate-time conversion. Newton's law is not overthrown; it is recovered, with the single amendment that momentum means $\gamma m\mathbf{u}$. The time component, by the orthogonality constraint, then carries no new information — it is forced to be the work–energy relation $dE/dt = \mathbf{u}\cdot\mathbf{f}$, the statement that energy increases at the rate the force does work. One four-vector equation, three independent components, reproducing Newton's law and the work–energy theorem together.

---

# What Makes This Hard

The non-obvious step is recognising that the four-force is *not* a free four-vector: the constraint $F\cdot U = 0$ is forced by constancy of the rest mass, and it ties the time component to the spatial components, so a relativistic "force" has only three independent components, not four. The most common error is to relativise Newton's law as $\mathbf{f} = m\mathbf{a}$ with $\mathbf{a} = d\mathbf{u}/dt$ the ordinary acceleration — this is wrong because $m\mathbf{a}$ is not $d\mathbf{p}/dt$ once $\mathbf{p} = \gamma m\mathbf{u}$ (the $\gamma$ depends on $u$, so differentiating produces extra terms), and the force is generally not parallel to the acceleration. A second frequent slip is to differentiate with respect to coordinate time $t$ rather than proper time $\tau$, which destroys the four-vector character of the equation.

---

# Rederivation Scaffold

**High-level strategy:**
Relativise Newton's law by the standard recipe — proper-time derivative of the four-momentum equals a four-force. The orthogonality $F\cdot U = 0$ is forced by constancy of the rest mass; the spatial and time projections recover Newton's law and the work–energy relation.

**Subgoal decomposition:**

1. **Write the covariant law.** Replace $d/dt\to d/d\tau$ and $\mathbf{p}\to P^\mu$, $\mathbf{f}\to F^\mu$ in $\mathbf{f} = d\mathbf{p}/dt$, giving $F^\mu = dP^\mu/d\tau$.
   - *Hint:* The right side is a four-vector iff differentiation is with respect to the scalar $\tau$.
   - *Why needed:* This is the equation; the rest is verifying its structure.

2. **Derive the orthogonality constraint.** Differentiate $P\cdot P = m^2c^2$ with respect to $\tau$.
   - *Hint:* $d(P\cdot P)/d\tau = 2P\cdot(dP/d\tau) = 2P\cdot F$; the left side is zero for constant $m$.
   - *Why needed:* It shows $F\cdot U = 0$, and that the four-force has only three independent components.

3. **Project onto space.** Using $d/d\tau = \gamma\,d/dt$, write the spatial part of $F^\mu = dP^\mu/d\tau$.
   - *Hint:* $F^{\text{spatial}} = \gamma\,d\mathbf{p}/dt$; define $\mathbf{f} = d\mathbf{p}/dt$ so $F^{\text{spatial}} = \gamma\mathbf{f}$.
   - *Why needed:* It recovers Newton's law with relativistic momentum.

4. **Project onto time.** Write the time part, and identify it with the work–energy relation.
   - *Hint:* $F^0 = \gamma\,d(E/c)/d\tau\cdot\ldots$; the orthogonality $F\cdot U = 0$ forces $dE/dt = \mathbf{u}\cdot\mathbf{f}$.
   - *Why needed:* It shows the time component carries no independent content.

---

# Lemma Decomposition

> [!note]- Lemma 1: The four-force is orthogonal to the four-velocity
> **Statement:** For a particle of constant rest mass $m$, the four-force satisfies $F\cdot U = 0$.
>
> **Hint:** Differentiate the mass-shell relation $P\cdot P = m^2c^2$.
>
> **Why needed:** It shows the four-force is constrained — only three of its components are free — and that it cannot change the rest mass.
>
> > [!note]- Full proof
> > The [[Def - Four-Momentum and Rest Mass|four-momentum]] of a particle of rest mass $m$ obeys the mass-shell relation $P\cdot P = m^2c^2$. If $m$ is constant, the right side is constant in $\tau$, so
> > $$0 = \frac{d}{d\tau}(P\cdot P) = \frac{d}{d\tau}(\eta_{\mu\nu}P^\mu P^\nu) = 2\,\eta_{\mu\nu}P^\mu\frac{dP^\nu}{d\tau} = 2\,P\cdot\frac{dP}{d\tau} = 2\,P\cdot F.$$
> > Since $P^\mu = mU^\mu$, this is $2m\,U\cdot F = 0$, hence $U\cdot F = 0$ (for $m\neq 0$). The four-force is Minkowski-orthogonal to the four-velocity. Conversely, $F\cdot U = 0$ implies $d(P\cdot P)/d\tau = 0$, i.e. the rest mass is conserved: orthogonality of the four-force to the four-velocity is *equivalent* to constancy of the rest mass. $\square$

> [!note]- Lemma 2: The spatial projection recovers Newton's law
> **Statement:** In a frame where the particle has velocity $\mathbf{u}$, the spatial components of $F^\mu = dP^\mu/d\tau$ read $\gamma\mathbf{f} = \gamma\,d\mathbf{p}/dt$, equivalently $\mathbf{f} = d\mathbf{p}/dt$ with $\mathbf{p} = \gamma m\mathbf{u}$.
>
> **Hint:** Convert proper-time to coordinate-time derivatives with $d/d\tau = \gamma\,d/dt$.
>
> **Why needed:** It shows the covariant law reduces to the familiar Newtonian form, with relativistic momentum.
>
> > [!note]- Full proof
> > The spatial part of the four-momentum is $\mathbf{p} = \gamma m\mathbf{u}$, and the spatial part of $F^\mu$ is, by definition of the four-force components, $\gamma\mathbf{f}$ where $\mathbf{f}$ is the ordinary three-force. The spatial part of the equation $F^\mu = dP^\mu/d\tau$ is therefore
> > $$\gamma\mathbf{f} = \frac{d\mathbf{p}}{d\tau} = \frac{dt}{d\tau}\frac{d\mathbf{p}}{dt} = \gamma\,\frac{d\mathbf{p}}{dt},$$
> > using the [[Def - Proper Time|proper-time]] relation $dt/d\tau = \gamma$. Cancelling $\gamma$:
> > $$\mathbf{f} = \frac{d\mathbf{p}}{dt}, \qquad \mathbf{p} = \gamma m\mathbf{u}.$$
> > Newton's second law survives verbatim, provided "momentum" is the relativistic momentum $\gamma m\mathbf{u}$. Note that $\mathbf{f}\neq m\mathbf{a}$ in general: differentiating $\mathbf{p} = \gamma m\mathbf{u}$ gives $\mathbf{f} = \gamma m\mathbf{a} + (d\gamma/dt)m\mathbf{u}$, so the force has a component along $\mathbf{u}$ in addition to the $m\mathbf{a}$ term, and force and acceleration are not parallel unless $\mathbf{u}$ and $\mathbf{a}$ are. $\square$

> [!note]- Lemma 3: The time projection is the work–energy relation
> **Statement:** The time component of $F^\mu = dP^\mu/d\tau$ is equivalent to $dE/dt = \mathbf{u}\cdot\mathbf{f}$, and carries no information independent of the spatial part.
>
> **Hint:** Use the orthogonality $F\cdot U = 0$ from Lemma 1.
>
> **Why needed:** It shows the four-force has only three independent components and identifies the time component physically.
>
> > [!note]- Full proof
> > The time component of $F^\mu = dP^\mu/d\tau$ is $F^0 = dP^0/d\tau = \gamma\,dP^0/dt = \gamma\,d(E/c)/dt$. To identify $F^0$, use the orthogonality $F\cdot U = 0$ from Lemma 1. With $U^\mu = \gamma(c,\mathbf{u})$ and $F^\mu = (F^0,\gamma\mathbf{f})$,
> > $$0 = F\cdot U = F^0 U^0 - \boldsymbol{F}^{\text{sp}}\cdot\mathbf{U} = F^0\,\gamma c - (\gamma\mathbf{f})\cdot(\gamma\mathbf{u}) = \gamma\big(F^0 c - \gamma\,\mathbf{f}\cdot\mathbf{u}\big).$$
> > Hence $F^0 = \gamma\,(\mathbf{u}\cdot\mathbf{f})/c$. Equating to $F^0 = \gamma\,d(E/c)/dt$:
> > $$\gamma\frac{1}{c}\frac{dE}{dt} = \gamma\frac{\mathbf{u}\cdot\mathbf{f}}{c} \;\Longrightarrow\; \frac{dE}{dt} = \mathbf{u}\cdot\mathbf{f}.$$
> > The rate of change of total energy equals the rate at which the force does work — the work–energy theorem, unchanged from Newtonian mechanics with $E$ now the total relativistic energy. Because $F^0$ was *determined* by the orthogonality constraint from the spatial force, the time component contains no information beyond the spatial part: a relativistic force has three independent components. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **The covariant law.** To relativise Newton's law $\mathbf{f} = d\mathbf{p}/dt$ we apply the construction principle of the topic: replace the [[Def - Four-Momentum and Rest Mass|three-momentum]] by the four-momentum $P^\mu$, the frame-dependent rate $d/dt$ by the invariant rate $d/d\tau$, and the three-force by a four-vector $F^\mu$. This gives
> $$F^\mu = \frac{dP^\mu}{d\tau}.$$
> Since $P^\mu$ is a four-vector and $\tau$ a Lorentz scalar, $dP^\mu/d\tau$ is a four-vector, so the equation is Lorentz-covariant: it holds in every inertial frame if in one. For constant rest mass, $P^\mu = mU^\mu$ gives $F^\mu = m\,dU^\mu/d\tau = mA^\mu$.
>
> **The orthogonality constraint.** By **Lemma 1**, differentiating $P\cdot P = m^2c^2$ for constant $m$ yields $P\cdot F = 0$, i.e. $F\cdot U = 0$: the four-force is Minkowski-orthogonal to the four-velocity, equivalently the four-force conserves the rest mass. A four-force has only three independent components.
>
> **Spatial projection.** By **Lemma 2**, in a frame where the particle has velocity $\mathbf{u}$ and Lorentz factor $\gamma$, the spatial part of $F^\mu = dP^\mu/d\tau$, using $d/d\tau = \gamma\,d/dt$, reduces to
> $$\mathbf{f} = \frac{d\mathbf{p}}{dt}, \qquad \mathbf{p} = \gamma m\mathbf{u},$$
> Newton's second law with relativistic momentum.
>
> **Time projection.** By **Lemma 3**, the orthogonality $F\cdot U = 0$ forces the time component to be
> $$\frac{dE}{dt} = \mathbf{u}\cdot\mathbf{f},$$
> the work–energy relation, carrying no information independent of the spatial part.
>
> **Free-particle limit.** When $F^\mu = 0$, the equation reads $dP^\mu/d\tau = 0$: the four-momentum is constant, the particle moves inertially, and [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] for a single free particle is recovered. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Lorentz force in covariant form.** The one force that survives intact into the relativistic regime is the electromagnetic one. Writing $F^\mu = q\,F^\mu{}_\nu U^\nu$ with $F_{\mu\nu}$ the antisymmetric field-strength tensor, the orthogonality $F\cdot U = 0$ is *automatic* — $F_{\mu\nu}U^\mu U^\nu = 0$ by antisymmetry — so the electromagnetic force never changes a particle's rest mass. Verifying that the spatial part of $q\,F^\mu{}_\nu U^\nu$ is the familiar $q(\mathbf{E}+\mathbf{u}\times\mathbf{B})$ and the time part is the rate of working $q\mathbf{E}\cdot\mathbf{u}$ is the central application of this theorem, and it is the bridge to electromagnetism.

**Hyperbolic motion as constant four-force.** A particle under a constant proper acceleration has $A\cdot A = -\kappa^2$, so $F\cdot F = -m^2\kappa^2$ is constant — a "constant force" in the relativistic sense. Solving $F^\mu = mA^\mu$ with this constraint reproduces the hyperbolic worldline of [[Ex - Hyperbolic motion under constant proper acceleration]]. The application battle-tests the orthogonality constraint: the four-force, though constant in magnitude, must continuously rotate to stay orthogonal to the ever-changing four-velocity.

**The relativistic rocket.** A rocket expelling exhaust is a variable-rest-mass system, so the single-particle equation $F^\mu = dP^\mu/d\tau$ does not apply to the rocket alone — but applying $dP^\mu/d\tau$ to the *total* system (rocket plus exhaust), with $F^\mu = 0$, recovers [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] and integrates to the relativistic rocket equation. See [[Ex - The relativistic rocket]]. The application shows the boundary of the theorem: it governs a *fixed-mass* particle, and variable-mass problems must be handled through conservation of four-momentum for a closed system.

---

# Bridges

- **[[Thm - Conservation of Four-Momentum]]** — the $F^\mu = 0$ special case. When no four-force acts, $dP^\mu/d\tau = 0$ and the four-momentum is conserved; the multi-particle version is conservation of four-momentum.

- **[[Def - Four-Velocity and Four-Acceleration]]** — supplies $A^\mu = dU^\mu/d\tau$ and the orthogonality $A\cdot U = 0$, which becomes $F\cdot U = 0$.

- **[[Def - Four-Momentum and Rest Mass]]** — the four-momentum whose proper-time derivative is the four-force; the mass-shell relation $P\cdot P = m^2c^2$ is what the constraint $F\cdot U = 0$ preserves.

- **The Lorentz force and the field-strength tensor** *(Electromagnetism)* — the electromagnetic four-force $F^\mu = qF^\mu{}_\nu U^\nu$ is the prototype relativistic force; its antisymmetric structure guarantees $F\cdot U = 0$.

- **The Euler–Lagrange equations** *(Geometric Mechanics)* — for a relativistic particle the equation of motion is the Euler–Lagrange equation of the proper-time action $S = -mc^2\int d\tau$; the four-force is the generalised force $\partial L/\partial X^\mu$.

---

# Unlocked by This

> [!tip] Relativistic Electrodynamics *(from Electromagnetism)*
> Writing the equation of motion as $dP^\mu/d\tau = q\,F^\mu{}_\nu U^\nu$ unifies the electric and magnetic forces into a single tensor equation, and is the dynamical half of relativistic electrodynamics (Maxwell's equations being the other half).

> [!tip] Hamiltonian and Lagrangian Relativistic Mechanics *(from Geometric Mechanics)*
> The equation of motion follows from the relativistic action $S = -mc^2\int d\tau$. The conjugate momentum is the four-momentum, the mass-shell relation is a Hamiltonian constraint, and this is the gateway to the canonical formulation of relativistic dynamics and field theory.
