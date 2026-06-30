---
type: definition
subject: special-relativity
prereqs:
  - "Def - Velocity Relative to an Observer"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Local Frame and Four-Rotation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. The observer $\mathcal{O}$ has four-velocity $U_0$, proper time $t$, four-acceleration $A_0 = \mathrm{d}U_0/\mathrm{d}t$, and four-rotation $\boldsymbol\omega$; its [[Def - Observer and Local Rest Space|local rest space]] is $E_{U_0} = U_0^\perp$, with rest-space cross product $\times_{U_0}$. The particle $\mathcal{P}$ has four-velocity $U$, four-acceleration $A = \mathrm{d}U/\mathrm{d}\tau'$, position vector $\overrightarrow{OM} = x^i\,e_i$ in the rest space, and [[Def - Velocity Relative to an Observer|relative velocity]] $\mathbf V = \mathrm{d}\mathbf x/\mathrm{d}t$. The Lorentz factor is $\Gamma = U \cdot U_0$. To avoid collision between the Lorentz factor $\Gamma$ and Gourgoulhon's symbol $\vec\gamma$ for the relative acceleration, we write the relative acceleration in bold as $\boldsymbol{\gamma}$. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

---

# Axiom Motivation

Having defined the [[Def - Velocity Relative to an Observer|velocity]] of a particle relative to an observer as the rate of change of its rest-space position with respect to the observer's clock, the acceleration is the obvious next quantity: differentiate once more. The motivation is not in *what* to differentiate — that is forced, it is the velocity — but in appreciating a structural surprise that has no Newtonian counterpart, and in keeping this quantity rigorously distinct from its four-vector relative.

The surprise is this. In Newtonian physics, acceleration is *absolute* among inertial observers: a particle has one acceleration vector, and every inertial observer measures the same one, because they all share a universal time and differ only by a constant relative velocity, which drops out under two differentiations. Only velocity is relative; acceleration is not. The relativistic acceleration relative to an observer breaks this. Because it is the second derivative of position with respect to the *observer's* proper time, and because the relation between the observer's proper time and any other observer's involves the relative velocity (which is itself observer-dependent), the relative acceleration *does* depend on the observer, even among inertial ones. Two inertial observers in relative motion measure different relative accelerations for the same particle. This is not a defect of the definition; it is a true feature of relativistic kinematics, and the definition must be set up so that this observer-dependence is visible and not accidentally hidden.

The companion motivation is to keep the relative acceleration $\boldsymbol{\gamma}$ apart from the [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = \mathrm{d}U/\mathrm{d}\tau'$, which is a genuine four-vector and *is* observer-independent. The two are different objects, differentiated with respect to different times. The four-acceleration is differentiated with respect to the particle's own proper time and is a four-vector orthogonal to $U$; the relative acceleration is differentiated with respect to the observer's proper time and is a three-vector in the observer's rest space. They are related — the four-acceleration can be written in terms of the relative acceleration and velocity ([[Thm - Expression of the Four-Acceleration]]) — but they coincide only in the special case of momentary rest. The definition exists in part to mark this distinction sharply, because conflating them is the most common error in relativistic dynamics.

Why differentiate the rest-space velocity with respect to the observer's time, rather than building an acceleration some other way? Because we want the acceleration *this observer measures*: the rate at which the particle's velocity, as the observer clocks it, changes. This is the quantity that enters the observer's own Newtonian-looking equations of motion at low speed, and it is what an observer would compute from successive position measurements. For a non-inertial observer it must use the derivative-with-respect-to-the-observer (so the rotation of the observer's axes does not contaminate it), and consequently it inherits the centripetal and Coriolis terms familiar from rotating-frame mechanics: a particle moving in a straight line at constant speed will appear, to a rotating observer, to accelerate, exactly as in the Newtonian case.

What goes wrong with variants? If you differentiate with respect to the particle's proper time, you get (essentially) the four-acceleration, not the observer's measured acceleration. If you forget that the rest space rotates and use bare coordinate derivatives, a particle truly at rest relative to a rotating observer acquires a spurious acceleration. If you treat $\boldsymbol{\gamma}$ as observer-independent — importing the Newtonian intuition — you will get wrong answers whenever two inertial observers are compared. The definition is pinned by the demand that it be the second derivative of the rest-space position with respect to the observer's clock, computed in the observer's (possibly rotating) frame.

---

# The Definition

Let $\mathcal{O}$ be an observer with four-velocity $U_0$, proper time $t$, and local frame $(e_\alpha)$, and let $\mathcal{P}$ be a particle with rest-space position vector $\overrightarrow{OM} = x^i(t)\,e_i$ and [[Def - Velocity Relative to an Observer|relative velocity]] $\mathbf V$.

**The acceleration of the particle $\mathcal{P}$ relative to the observer $\mathcal{O}$** is the second derivative of $\mathcal{P}$'s rest-space position vector with respect to $\mathcal{O}$'s proper time, equivalently the first derivative of the relative velocity:
$$
\boxed{\;\boldsymbol{\gamma} := \frac{\mathrm{d}^2\mathbf x}{\mathrm{d}t^2} = \frac{\mathrm{d}\mathbf V}{\mathrm{d}t},\qquad \boldsymbol{\gamma}(t) := \frac{\mathrm{d}^2 x^i}{\mathrm{d}t^2}\,e_i(t)\;}
$$
a vector in the local rest space $E_{U_0}(t)$. The derivative is taken with respect to the observer — that is, in the observer's rotating-and-tilting frame — so that for a non-inertial observer the relation to the absolute second derivative of the position vector along the worldline carries inertial-force terms:
$$
\frac{\mathrm{d}^2\overrightarrow{OM}}{\mathrm{d}t^2} = \boldsymbol{\gamma} \;+\; \underbrace{\boldsymbol\omega\times_{U_0}\big(\boldsymbol\omega\times_{U_0}\overrightarrow{OM}\big)}_{\text{centripetal}} \;+\; \underbrace{2\,\boldsymbol\omega\times_{U_0}\mathbf V}_{\text{Coriolis}} \;+\;\frac{\mathrm{d}\boldsymbol\omega}{\mathrm{d}t}\times_{U_0}\overrightarrow{OM} \;+\;(\text{relativistic terms}).
$$
For an **inertial observer** ($A_0 = 0$, $\boldsymbol\omega = 0$) the centripetal, Coriolis, and frame-rotation terms vanish, and $\boldsymbol{\gamma}$ is simply the ordinary second derivative $\mathrm{d}^2\mathbf x/\mathrm{d}t^2$ of the position in the (now non-rotating) rest space.

The relative acceleration is a spatial vector: $\boldsymbol{\gamma} \cdot U_0 = 0$, and its components in the observer's frame are $\boldsymbol{\gamma}^\alpha = (0, \boldsymbol{\gamma}^1, \boldsymbol{\gamma}^2, \boldsymbol{\gamma}^3)$ with $\boldsymbol{\gamma}^i = \mathrm{d}^2 x^i/\mathrm{d}t^2$. Its relation to the particle's four-acceleration $A$ is the subject of [[Thm - Expression of the Four-Acceleration]]; the two coincide, $A = \boldsymbol{\gamma}$, exactly when $\mathcal{P}$ is momentarily at rest relative to $\mathcal{O}$ (so $\mathbf V = 0$, $\Gamma = 1$) and $\mathcal{O}$ is inertial.

---

# Relate to Other Fields / Compression

In rotating-frame classical mechanics, the centripetal and Coriolis terms in the relation between $\boldsymbol{\gamma}$ and the absolute second derivative are *identical in form* to the fictitious accelerations of a Newtonian rotating frame: $\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)$ and $2\boldsymbol\omega\times\mathbf v$. This is no coincidence — the observer's four-rotation $\boldsymbol\omega$ plays exactly the role of the angular velocity of a Newtonian rotating frame, and the rest-space cross product $\times_{U_0}$ is the ordinary cross product on the (Euclidean) rest space. The relativistic terms in the full formula are the corrections that survive at high speed; the Newtonian terms are recovered in the limit $|\mathbf V| \to 0$, $A_0 \cdot \overrightarrow{OM} \to 0$. Gourgoulhon's Remark 4.6 makes this split explicit: the first line of the general formula is "Newtonian", the second "relativistic".

In differential geometry, $\boldsymbol{\gamma}$ is the projection onto the rest space of the absolute (Fermi–Walker) second derivative of the position vector along the observer's worldline, with the connection terms of the moving frame producing the inertial-force corrections. This is the flat-spacetime, single-worldline instance of the general apparatus relating an ambient covariant derivative to its restriction to a curve.

**True name:** The relative acceleration is the second derivative of the particle's rest-space position with respect to the observer's clock, computed in the observer's frame — an *observer-dependent* three-vector, to be contrasted with the *observer-independent* four-acceleration. Operationally: for an inertial observer it is just $\mathrm{d}^2\mathbf x/\mathrm{d}t^2$; for a rotating one, add the centripetal and Coriolis terms.

---

# Examples / Corollaries

**Is an instance — uniform circular motion (inertial observer).** For $\mathcal{P}$ orbiting in the rest space, $x^1 = R\cos\Omega t$, $x^2 = R\sin\Omega t$, the relative acceleration is $\boldsymbol{\gamma} = -R\Omega^2\cos\Omega t\,e_1 - R\Omega^2\sin\Omega t\,e_2 = -\Omega^2\overrightarrow{OM}$, purely centripetal, pointing toward the centre with magnitude $R\Omega^2$. This is the ordinary centripetal acceleration, exactly as in Newtonian mechanics, because the observer is inertial.

**Is an instance — uniformly accelerated motion (inertial observer).** For collinear motion with constant proper acceleration $a$, the relative acceleration is $\boldsymbol{\gamma} = a/\Gamma^3$ along the direction of motion: it *decreases* as the speed grows, because the observer sees the particle's velocity asymptote toward $c$ and so its rate of change must fall. The four-acceleration norm stays constant at $a$; the relative acceleration does not.

**Is NOT an instance — the four-acceleration.** The four-acceleration $A = \mathrm{d}U/\mathrm{d}\tau'$ is not the relative acceleration: it is a four-vector (four components, orthogonal to $U$), differentiated with respect to the particle's proper time, and observer-independent, whereas $\boldsymbol{\gamma}$ is a rest-space three-vector differentiated with respect to the observer's time and observer-dependent. They agree only at momentary rest. Confusing them is the standard error of relativistic dynamics.

**Is NOT an instance — the bare coordinate acceleration in a rotating frame.** For a rotating observer, the second coordinate derivative $\mathrm{d}^2 x^i/\mathrm{d}t^2$ of a particle held fixed in the observer's rest space is nonzero (the coordinates change as the basis rotates), yet the particle's relative acceleration — and relative velocity — are zero, since it does not move relative to the observer. The relative acceleration uses the derivative with respect to the observer, which removes the basis rotation.

**Corollary — observer-dependence among inertial observers.** Two inertial observers in relative motion measure different relative accelerations for the same particle, because $\boldsymbol{\gamma}$ depends on the relative velocity (see [[Thm - Expression of the Four-Acceleration]]), which differs between them. This is the relativistic departure from the Newtonian absoluteness of acceleration, and the key thing to remember when comparing frames.

**Corollary — the relative acceleration lies in the rest space.** Since $\boldsymbol{\gamma}$ is the derivative of a vector field valued in the (varying) rest space, projected back to the rest space, it satisfies $\boldsymbol{\gamma} \cdot U_0 = 0$: it has no time component in the observer's frame. It is a genuine spatial acceleration, the kind that enters the observer's three-dimensional Newtonian-looking equations at low speed.

**Calibration check.** If you have understood the definition you should be able to: (i) compute $\boldsymbol{\gamma}$ for circular and for uniformly accelerated motion seen by an inertial observer, and confirm the circular case is purely centripetal; (ii) state the two ways $\boldsymbol{\gamma}$ differs from the four-acceleration $A$ (the time of differentiation, and observer-dependence) and the single condition under which they coincide; (iii) identify which term in the general formula a rotating observer needs so that a particle at rest relative to them has zero relative acceleration.

---

# Unlocked by This

> [!tip] The Relativistic Equation of Motion and Relativistic Mass *(from Relativistic Dynamics)*
> Newton's second law relativistically reads $\mathbf f = \mathrm{d}\mathbf p/\mathrm{d}t = \mathrm{d}(\Gamma m\mathbf V)/\mathrm{d}t$, and expanding the derivative shows the three-force and the relative acceleration $\boldsymbol{\gamma}$ are related by *direction-dependent* factors: $\Gamma m$ transverse to the velocity, $\Gamma^3 m$ along it. These are the **transverse and longitudinal relativistic masses**, the precise statement that "a relativistic particle is harder to accelerate along its motion than across it", developed in **Special Relativity XIII**.

> [!tip] Hyperbolic Motion and the Rindler Horizon *(from Accelerated Observers)*
> A particle whose four-acceleration has constant norm — constant proper acceleration — undergoes **hyperbolic motion**, with relative acceleration $\boldsymbol{\gamma} = a/\Gamma^3$ falling off as it nears the speed of light. Integrating gives the worldline $x^2 - t^2 = 1/a^2$ and the **Rindler horizon**, the surface that an eternally accelerating observer can never receive signals from beyond. This is the kinematic foundation of **Special Relativity XVI** and the Unruh effect.
