---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Uniformly Rotating Observer"
  - "Thm - 4-Acceleration and 4-Rotation of the Corotating Observer"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Lorentz Factor and Relative Velocity"
tags: [physics, special-relativity]
---

# Problem Statement

A disk rotates at constant angular velocity $\omega$ about its axis; the central observer $\mathcal{O}$ is inertial, and an inertial observer $\mathcal{O}_*$ shares its worldline carrying the non-rotating frame $(e^*_\alpha)$. A corotating observer $\mathcal{O}'$ sits at fixed radius $r$ and azimuth $\varphi$ on the disk. Working with $c = 1$ where convenient and restoring $c$ in the final answers:

1. Write the inertial-coordinate worldline of $\mathcal{O}'$ and compute its velocity $\vec V$ relative to $\mathcal{O}_*$. Show $\|\vec V\| = r\omega$ and deduce the bound $r < c/\omega$.
2. Compute the four-velocity $U'$ of $\mathcal{O}'$ in terms of $U$ (the central four-velocity) and $\vec V$, and find its Lorentz factor $\Gamma$.
3. Compute the four-acceleration $\vec a'$ of $\mathcal{O}'$. Show it is centripetal (radially inward) with magnitude $\Gamma^2 r\omega^2$ (in $c=1$ units), exceeding the Newtonian $r\omega^2$ by $\Gamma^2$.
4. Verify that $\vec a'$ is orthogonal to $U'$, as every four-acceleration must be.

**Recall:**

![[Def - Uniformly Rotating Observer#The Definition]]

The four-velocity is the unit-norm tangent to the worldline parametrized by proper time; the [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] is its proper-time derivative, $\vec a = dU/d\tau$, always orthogonal to $U$. The [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] of an observer moving at speed $\|\vec V\|$ relative to another is $\Gamma = (1 - \|\vec V\|^2/c^2)^{-1/2}$, and the four-velocities are related by the boost $U' = \Gamma(U + c^{-1}\vec V)$ with $\vec V$ in the rest space of $U$.

---

# Convergent Strategy

**Problem class.** A *compute-the-kinematic-invariants* problem, the basic exercise type of §17.1. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]] says: write the helical worldline, compute $\Gamma$ first, and read off the velocity, acceleration, and proper-time rate as multiples of powers of $\Gamma$.

**Assumption pattern.** A point fixed on a rigidly rotating disk, specified by its radius $r$ and the disk's angular velocity $\omega$. The signpost is "fixed at radius $r$ on a rotating disk" — this is the definition of a corotating observer, whose inertial worldline is immediately a circular helix. Everything follows by differentiation.

**Theorem routing.** Part 1 differentiates the helix to get $\vec V$; part 2 applies the boost relation $U' = \Gamma(U + c^{-1}\vec V)$ from [[Def - Lorentz Factor and Relative Velocity]]; part 3 differentiates $U'$ with respect to proper time, using $dt = \Gamma\,d\tau$, to get $\vec a'$, matching [[Thm - 4-Acceleration and 4-Rotation of the Corotating Observer]]; part 4 checks $U'\cdot\vec a' = 0$.

**Key decision point.** The crux is keeping straight the two time variables: the central proper time $t$ (equal to inertial time) and the corotating proper time $\tau$, related by $dt = \Gamma\,d\tau$. The four-acceleration is the derivative with respect to $\tau$, and the temptation is to compute the coordinate acceleration $d^2\vec x_*/dt^2 = r\omega^2$ and stop — missing the two factors of $\Gamma$ that convert it to the proper four-acceleration. The non-obvious move is recognizing that *each* proper-time derivative brings a factor $dt/d\tau = \Gamma$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the corotating worldline as a helix).** The worldline $x_*(t) = r\cos(\omega t + \varphi)$, $y_*(t) = r\sin(\omega t + \varphi)$ is the starting object; differentiating it once gives $\vec V$, twice gives the acceleration.

2. **Operation 2 from the topic page (compute the rim Lorentz factor first).** $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ is computed from $\|\vec V\| = r\omega$ and used as the currency for the four-velocity and four-acceleration.

3. **Operation 7 from the topic page (relativistic chain rule between $t$ and $\tau$).** Converting the inertial-time derivative to the proper-time derivative via $dt = \Gamma\,d\tau$ supplies the factors of $\Gamma$ in the four-acceleration.

---

# Hints

> [!note]- Hint 1
> A point fixed at $(r,\varphi)$ in the rotating frame, viewed from the inertial frame, goes in a circle of radius $r$ at angular velocity $\omega$: its worldline is the helix $x_*(t) = r\cos(\omega t + \varphi)$, $y_*(t) = r\sin(\omega t + \varphi)$, $z_* = 0$. Differentiate with respect to inertial time $t$ to get the three-velocity.

> [!note]- Hint 2
> The three-velocity has magnitude $r\omega$ (the rim speed), so the Lorentz factor is $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. The requirement that the worldline be timelike, $r\omega < c$, forces $r < c/\omega$. The four-velocity is the boosted central four-velocity, $U' = \Gamma(U + c^{-1}\vec V)$.

> [!note]- Hint 3
> The four-acceleration is $\vec a' = dU'/d\tau$, *not* $dU'/dt$. Use $dt = \Gamma\,d\tau$ so that $d/d\tau = \Gamma\,d/dt$. Only the azimuthal direction $\vec n$ depends on $t$ (through the rotation); $\Gamma$, $r$, $\omega$ are constant. Each derivative brings a $\Gamma$, so the result carries $\Gamma^2$.

> [!note]- Hint 4
> The acceleration points radially inward (toward the axis), along the corotating frame vector $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$. Its magnitude is $\Gamma^2 r\omega^2$. To check orthogonality to $U'$, note that $\vec a'$ is purely spatial in the corotating rest space (along $e'_2$), and $e'_2\cdot U' = 0$ by construction.

---

# Solution

The route has four steps. Step 1 writes the helix and differentiates it to get $\vec V = r\omega\,\vec n$ with $\|\vec V\| = r\omega$, forcing $r < c/\omega$. Step 2 boosts to get $U' = \Gamma(U + c^{-1}\vec V)$ with $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. Step 3 differentiates $U'$ with respect to *proper* time, the two factors of $\Gamma$ from $dt = \Gamma\,d\tau$ producing $\vec a' = (\Gamma^2/c^2)r\omega^2 e'_2$. Step 4 checks $U'\cdot\vec a' = 0$. The non-obvious move is the proper-time derivative in Step 3.

**Step 1: The velocity is $\vec V = r\omega\,\vec n$, with $\|\vec V\| = r\omega$, forcing $r < c/\omega$.**

> [!note]- Derivation
> The corotating observer at $(r,\varphi)$ traces, in inertial coordinates,
> $$x_*(t) = r\cos(\omega t + \varphi),\qquad y_*(t) = r\sin(\omega t + \varphi),\qquad z_*(t) = 0.$$
> Differentiating with respect to inertial time $t$ (which equals the central proper time),
> $$\frac{d\vec x_*}{dt} = r\omega\big(-\sin(\omega t + \varphi)\,e^*_1 + \cos(\omega t + \varphi)\,e^*_2\big) = r\omega\,\vec n,$$
> where $\vec n = -\sin\varphi\,e_1 + \cos\varphi\,e_2$ is the azimuthal unit vector (in the rotating frame, $\vec n$ is the tangential direction). Its magnitude is $\|\vec V\| = r\omega$ — the rim speed. The worldline is timelike only if $\|\vec V\| < c$, i.e.
> $$r\omega < c \quad\Longrightarrow\quad r < \frac{c}{\omega}.$$
> Beyond the light cylinder $r = c/\omega$ the worldline would be spacelike and admit no observer.

**Step 2: The four-velocity is $U' = \Gamma(U + c^{-1}\vec V)$, with $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$.**

> [!note]- Derivation
> The corotating observer moves at velocity $\vec V$ relative to the inertial observer $\mathcal{O}_*$ (whose four-velocity is $U$, the same as the central observer's). By the standard relation between four-velocities under a boost ([[Def - Lorentz Factor and Relative Velocity]]),
> $$U' = \Gamma\big(U + c^{-1}\vec V\big) = \Gamma\big(U + (r\omega/c)\vec n\big),$$
> where the Lorentz factor is determined by the relative speed $\|\vec V\| = r\omega$:
> $$\Gamma = \frac{1}{\sqrt{1 - \|\vec V\|^2/c^2}} = \frac{1}{\sqrt{1 - r^2\omega^2/c^2}}.$$
> One checks $U'\cdot U' = \Gamma^2(U\cdot U + 2c^{-1}U\cdot\vec V + c^{-2}\vec V\cdot\vec V) = \Gamma^2(1 + 0 - r^2\omega^2/c^2) = \Gamma^2\Gamma^{-2} = 1$ (mostly-minus, $U\cdot\vec V = 0$ since $\vec V$ is spacelike in $U$'s rest space, $\vec V\cdot\vec V = -r^2\omega^2$ in mostly-minus). So $U'$ is correctly unit timelike.

**Step 3: The four-acceleration is $\vec a' = (\Gamma^2/c^2)r\omega^2\,e'_2$, centripetal, of magnitude $\Gamma^2 r\omega^2$.**

> [!note]- Derivation
> The four-acceleration is the derivative of $U'$ with respect to the corotating observer's *proper time* $\tau$, related to inertial time by $dt = \Gamma\,d\tau$, so $d/d\tau = \Gamma\,d/dt$. With $\Gamma$, $r$, $\omega$ constant, only $\vec n$ varies with $t$:
> $$\vec a' = \frac{dU'}{d\tau} = \Gamma\frac{dU'}{dt} = \Gamma\cdot\Gamma\frac{r\omega}{c}\frac{d\vec n}{dt}.$$
> The azimuthal vector $\vec n = -\sin(\omega t + \varphi)\,e^*_1 + \cos(\omega t + \varphi)\,e^*_2$ rotates: $\dfrac{d\vec n}{dt} = -\omega\big(\cos(\omega t + \varphi)\,e^*_1 + \sin(\omega t + \varphi)\,e^*_2\big) = \omega\,e'_2$, where $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$ is the inward radial unit vector. Hence
> $$\vec a' = \Gamma^2\frac{r\omega}{c}\cdot\omega\,e'_2 = \frac{\Gamma^2 r\omega^2}{c}\,e'_2 \;\xrightarrow{\text{restore } c}\; \frac{\Gamma^2}{c^2}r\omega^2\,e'_2.$$
> The acceleration points inward (centripetal), with magnitude $\Gamma^2 r\omega^2$ in $c = 1$ units — the Newtonian centripetal acceleration $r\omega^2$ enhanced by $\Gamma^2$. This matches [[Thm - 4-Acceleration and 4-Rotation of the Corotating Observer]].

**Step 4: The four-acceleration is orthogonal to the four-velocity.**

> [!note]- Derivation
> The four-acceleration $\vec a' = (\Gamma^2/c^2)r\omega^2 e'_2$ lies along the spatial frame vector $e'_2$ of the corotating observer. By construction the spatial frame vectors of any observer are orthogonal to its four-velocity: $e'_2\cdot U' = 0$. Hence $\vec a'\cdot U' = 0$, as required of every four-acceleration (differentiate $U'\cdot U' = 1$ to get $2\,U'\cdot\vec a' = 0$). Explicitly, $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$ is a combination of spatial central-frame vectors, each orthogonal to $U$, and $e'_2\cdot U' = e'_2\cdot\Gamma(U + c^{-1}\vec V) = \Gamma c^{-1}(e'_2\cdot\vec V)$; since $e'_2$ (radial) is orthogonal to $\vec V$ (tangential), this vanishes.

> [!note]- Complete formal solution
> The corotating observer at $(r,\varphi)$ has inertial worldline $x_*(t) = r\cos(\omega t + \varphi)$, $y_*(t) = r\sin(\omega t + \varphi)$, $z_* = 0$, giving velocity $\vec V = r\omega\,\vec n$ ($\vec n$ the azimuthal unit vector) of magnitude $r\omega$, so timelikeness requires $r < c/\omega$. The four-velocity is $U' = \Gamma(U + c^{-1}\vec V)$ with $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$, verified unit by $U'\cdot U' = \Gamma^2(1 - r^2\omega^2/c^2) = 1$. The four-acceleration is $\vec a' = dU'/d\tau = \Gamma\,dU'/dt = \Gamma^2(r\omega/c)\,d\vec n/dt$; since $d\vec n/dt = \omega\,e'_2$ (inward radial), $\vec a' = (\Gamma^2/c^2)r\omega^2\,e'_2$, centripetal of magnitude $\Gamma^2 r\omega^2$. It is orthogonal to $U'$ because $e'_2\cdot U' = \Gamma c^{-1}(e'_2\cdot\vec V) = 0$ (radial $\perp$ tangential). $\blacksquare$

**Frame-invariance check.** The result $\vec a' = (\Gamma^2/c^2)r\omega^2 e'_2$ can be checked against the general formula relating three-acceleration and four-acceleration for circular (purely transverse) motion: the proper transverse acceleration is $\Gamma^2$ times the coordinate transverse acceleration, and the coordinate centripetal acceleration of the helix is $r\omega^2$, giving $\Gamma^2 r\omega^2$ — agreeing with the direct computation.

---

# Key Takeaways

**The helix is the master object: differentiate once for velocity, twice (in proper time) for acceleration.** Every kinematic quantity of a corotating observer is read off the helical worldline $x_*(t) = r\cos(\omega t + \varphi)$, $y_*(t) = r\sin(\omega t + \varphi)$. The first derivative with respect to inertial time gives the tangential velocity $r\omega\,\vec n$; the second, suitably converted to proper time, gives the inward four-acceleration. The trigger for this approach is any problem about a point fixed on a rotating body — turntables, flywheels, the rotating Earth, particles in storage rings. The transferable lesson is that "rigidly rotating at radius $r$" *is* "helical worldline", and helices are differentiated mechanically. Once you have the helix, no separate relativistic-kinematics bookkeeping is needed; the geometry does the work.

**Two factors of $\Gamma$ separate the four-acceleration from the Newtonian centripetal acceleration, and they come from the proper-time derivative.** The Newtonian centripetal acceleration of circular motion is $r\omega^2$; the relativistic four-acceleration is $\Gamma^2 r\omega^2$. The two extra factors of $\Gamma$ enter because the four-acceleration is differentiated with respect to the corotating observer's *proper time* $\tau$, not the inertial time $t$, and $dt = \Gamma\,d\tau$ means each derivative brings a factor $\Gamma$. The trigger to watch for is any "acceleration" of a relativistic object that is really a four-acceleration: always ask whether the derivative is with respect to proper time, and if so, insert the $\Gamma$ factors. This is the same mechanism that makes transverse force on a fast particle exceed the Newtonian expectation, and forgetting it is the single most common error in this exercise. For a rim approaching $c$, the enhancement diverges — it costs unboundedly much four-acceleration to keep a near-luminal point on its circular track.

**The light cylinder $r < c/\omega$ is a hard physical limit forced by timelikeness, not a coordinate artifact.** The requirement $\|\vec V\| = r\omega < c$ means a rigid disk cannot extend beyond radius $c/\omega$ at angular velocity $\omega$ — there is simply no observer there, because the would-be worldline is spacelike. This is not a removable feature of the coordinates; it is the statement that you cannot rigidly rotate an arbitrarily large disk at fixed $\omega$. The trigger is any rotating system specified by an angular velocity: immediately ask how large it can be before the rim reaches $c$. The same bound governs pulsar magnetospheres (field lines cannot corotate beyond the light cylinder) and is the flat-spacetime ancestor of the Kerr black hole's ergosphere. Recognizing the bound as a timelikeness constraint, rather than a quirk, is what lets you transfer it to those settings.
