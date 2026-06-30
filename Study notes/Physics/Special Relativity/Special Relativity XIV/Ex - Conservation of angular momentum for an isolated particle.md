---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Angular Momentum"
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

An isolated particle of mass $m$ moves freely, so by the law of inertia its [[Def - Four-Momentum and Rest Mass|four-momentum]] $p = mU$ is constant. Working with $c = 1$:

1. Show by direct differentiation that the [[Def - Angular Momentum Four-Tensor|angular momentum]] $J_C = \overrightarrow{CM}^\flat\wedge p$ about a fixed event $C$ is constant along the worldline, identifying precisely which term vanishes for which reason.
2. A free particle has constant velocity $\mathbf{v}$ and passes through the point $\mathbf{r}_0$ at $t = 0$, so $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$. Compute the angular momentum vector $\vec\sigma_C = \overrightarrow{CM}\times\mathbf{p}$ about a fixed point $C$ (take $C$ at the spatial origin) and verify it is constant in time, even though $\mathbf{r}(t)$ is not.
3. Interpret the constancy geometrically: show that $\vec\sigma_C$ equals the momentum times the *perpendicular distance* (impact parameter) from $C$ to the line of motion, and explain why this is constant.
4. Now suppose a *central* four-force acts (always along $\overrightarrow{CM}$), so the particle is not free. Show that the angular momentum about $C$ is *still* conserved, and contrast the mechanism with part 1.

**Recall:**

![[Thm - Conservation of Angular Momentum#Statement]]

The four-velocity is $U = dM/d\tau$ (the proper-time derivative of the position), so $d\overrightarrow{CM}/d\tau = U$ for a *fixed* $C$. The exterior product of a vector with itself vanishes: $\vec a^\flat\wedge\vec a = 0$. The [[Def - Four-Torque|four-torque]] is $N_C = \overrightarrow{CM}^\flat\wedge f$.

---

# Convergent Strategy

**Problem class.** A *prove-a-conservation-law* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: a relativistic conservation law is "the right derivative is zero", found by differentiating the defining wedge.

**Assumption pattern.** The particle is isolated (part 1–3) or under a central force (part 4); the angular momentum is $\overrightarrow{CM}^\flat\wedge p$. The signpost is "free particle" or "central force": the first kills $dp/d\tau$, the second kills the moment $\overrightarrow{CM}^\flat\wedge f$. Both routes appear in [[Thm - Conservation of Angular Momentum|the theorem]].

**Theorem routing.** Part 1 differentiates and uses $p\parallel U$ and the law of inertia. Part 2–3 compute the explicit vector and interpret it. Part 4 uses the [[Def - Four-Torque|four-torque]] vanishing for a central force.

**Key decision point.** The crux of part 1 is that *two* terms appear in $dJ_C/d\tau$, and they vanish for *different* reasons: the $d\overrightarrow{CM}/d\tau\wedge p$ term vanishes because $U\parallel p$ (a relativistic identity, always true), while the $\overrightarrow{CM}\wedge dp/d\tau$ term vanishes by the law of inertia (only for a free particle). Conflating the two reasons is the classic error.

---

# Legal Operations Used

1. **Operation 7 from the topic page (compute a four-torque as $\overrightarrow{CM}^\flat\wedge f$).** Part 1 differentiates the angular momentum, and part 4 uses the four-torque vanishing for a central force.

2. **Operation 9 from the topic page (kill a term with parallelism/antisymmetry).** The $d\overrightarrow{CM}/d\tau\wedge p$ term vanishes because $U\parallel p$, and the central-force moment vanishes because $f\parallel\overrightarrow{CM}$.

---

# Hints

> [!note]- Hint 1
> Differentiate $J_C = \overrightarrow{CM}^\flat\wedge p$ by the Leibniz rule: $\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}$. Now evaluate each term: what is $d\overrightarrow{CM}/d\tau$? What is $dp/d\tau$ for a free particle?

> [!note]- Hint 2
> For the first term, $d\overrightarrow{CM}/d\tau = U$ (the four-velocity, since $C$ is fixed and $M$ moves), and $p = mU$, so the term is $U^\flat\wedge(mU) = m(U^\flat\wedge U) = 0$ — the wedge of a vector with itself.

> [!note]- Hint 3
> For part 2, with $C$ at the origin, $\overrightarrow{CM}$ has spatial part $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$, and $\mathbf{p} = E\mathbf{v}$ (constant). So $\vec\sigma_C = \mathbf{r}(t)\times\mathbf{p} = (\mathbf{r}_0 + \mathbf{v}t)\times E\mathbf{v} = \mathbf{r}_0\times E\mathbf{v} + t(\mathbf{v}\times E\mathbf{v})$. The second term vanishes because $\mathbf{v}\times\mathbf{v} = 0$.

> [!note]- Hint 4
> For part 4, a central force has $f\parallel\overrightarrow{CM}$, so the four-torque $N_C = \overrightarrow{CM}^\flat\wedge f = 0$ (wedge of parallel vectors). Hence $dJ_C/d\tau = N_C = 0$ — conserved. The mechanism differs from part 1: there $dp/d\tau = 0$ (no force at all); here $dp/d\tau\ne 0$ but its *moment* about $C$ is zero.

---

# Solution

The exercise proves the single-particle conservation law two ways and contrasts the free and central-force mechanisms. Part 1 differentiates abstractly; parts 2–3 verify and interpret geometrically; part 4 shows conservation survives a central force for a different reason.

**Step 1: Differentiation, term by term.**

> [!note]- Derivation
> By the Leibniz rule for the exterior product,
> $$\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}.$$
> **First term.** Since $C$ is fixed and $M = M(\tau)$ moves along the worldline, $\frac{d\overrightarrow{CM}}{d\tau} = \frac{dM}{d\tau} = U$, the [[Def - Four-Velocity and Four-Acceleration|four-velocity]]. And $p = mU$, parallel to $U$. So
> $$\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = U^\flat\wedge(mU) = m\,(U^\flat\wedge U) = 0,$$
> the exterior product of a vector with itself. This term vanishes for a *relativistic* reason — $p\parallel U$ — and it would vanish even if a force were present (as long as $p = mU$ holds, which it always does).
> **Second term.** The law of inertia for a free particle gives $\frac{dp}{d\tau} = 0$, so $\overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau} = 0$. This term vanishes because there is *no force*.
> Hence $\frac{dJ_C}{d\tau} = 0$: the angular momentum is constant along the worldline. The two terms vanish for two different reasons — $p\parallel U$ and $dp/d\tau = 0$ — and keeping them distinct is the point.

**Step 2: Explicit computation.**

> [!note]- Derivation
> Place $C$ at the spatial origin. The particle's position has spatial part $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$, and its spatial momentum is $\mathbf{p} = E\mathbf{v}$ with $E = \gamma m$ constant (free particle). The angular momentum vector is
> $$\vec\sigma_C = \mathbf{r}(t)\times\mathbf{p} = (\mathbf{r}_0 + \mathbf{v}t)\times E\mathbf{v} = E\,(\mathbf{r}_0\times\mathbf{v}) + Et\,(\mathbf{v}\times\mathbf{v}).$$
> The second term vanishes because $\mathbf{v}\times\mathbf{v} = 0$. So
> $$\vec\sigma_C = E\,(\mathbf{r}_0\times\mathbf{v}) = \mathbf{r}_0\times\mathbf{p},$$
> independent of $t$ — constant, even though $\mathbf{r}(t)$ grows without bound. The time-dependence of the position is exactly along $\mathbf{v}$, which is parallel to $\mathbf{p}$, so it contributes nothing to the cross product. This is the explicit shadow of the term that vanished in Step 1.

**Step 3: Geometric interpretation.**

> [!note]- Derivation
> The magnitude of the angular momentum is $\|\vec\sigma_C\| = \|\mathbf{r}_0\times\mathbf{p}\| = \|\mathbf{p}\|\cdot d_\perp$, where $d_\perp = \|\mathbf{r}_0\|\sin\theta$ is the perpendicular distance from $C$ to the *line* of motion (the impact parameter), with $\theta$ the angle between $\mathbf{r}_0$ and $\mathbf{v}$. Since the particle moves along a fixed straight line and $C$ is fixed, the perpendicular distance from $C$ to that line is a constant of the geometry — it does not change as the particle slides along the line. And $\|\mathbf{p}\|$ is constant (free particle). So $\|\vec\sigma_C\| = \|\mathbf{p}\|\,d_\perp$ is manifestly constant. This is the geometric content of the conservation law: **a constant momentum along a fixed line has a constant moment about any point**, because both the momentum and the perpendicular lever arm are fixed. The direction of $\vec\sigma_C$ is also fixed (perpendicular to the plane containing $C$ and the line), so the full vector is conserved.

**Step 4: Conservation under a central force.**

> [!note]- Derivation
> Now let a central four-force act, $f\parallel\overrightarrow{CM}$ at every instant (the force always points toward or away from $C$). The particle is *not* free — $\frac{dp}{d\tau} = f\ne 0$ — so the Step 1 argument's second term does *not* vanish by the law of inertia. Instead, compute the [[Def - Four-Torque|four-torque]]:
> $$N_C = \frac{dJ_C}{d\tau} = \overrightarrow{CM}^\flat\wedge f.$$
> (The first term $\frac{d\overrightarrow{CM}}{d\tau}\wedge p = U^\flat\wedge p = 0$ still vanishes, by $p\parallel U$ — this part is unchanged.) Since $f$ is central, $f\parallel\overrightarrow{CM}$, so the wedge of parallel vectors vanishes:
> $$N_C = \overrightarrow{CM}^\flat\wedge f = 0\qquad(f\parallel\overrightarrow{CM}).$$
> Hence $\frac{dJ_C}{d\tau} = 0$: the angular momentum about $C$ is conserved, even though the particle accelerates. The *mechanism* is different from part 1: there, conservation followed from the absence of any force ($dp/d\tau = 0$); here, the force is present but has zero *moment* about $C$ (the force and the lever arm are parallel). This is the relativistic version of "central forces conserve angular momentum", and it is the first integral of the relativistic Kepler problem. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** $\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}$. First term $= U^\flat\wedge mU = 0$ ($p\parallel U$); second term $= 0$ (law of inertia). Hence $J_C$ constant.
>
> **Part 2.** With $C$ at the origin, $\vec\sigma_C = (\mathbf{r}_0 + \mathbf{v}t)\times E\mathbf{v} = E(\mathbf{r}_0\times\mathbf{v}) = \mathbf{r}_0\times\mathbf{p}$, constant (the $t$-term vanishes by $\mathbf{v}\times\mathbf{v} = 0$).
>
> **Part 3.** $\|\vec\sigma_C\| = \|\mathbf{p}\|\,d_\perp$ with $d_\perp$ the impact parameter; both factors are constant (fixed line, free particle), so $\vec\sigma_C$ is constant — a constant momentum along a fixed line has a constant moment.
>
> **Part 4.** For a central force $f\parallel\overrightarrow{CM}$, the four-torque $N_C = \overrightarrow{CM}^\flat\wedge f = 0$, so $dJ_C/d\tau = 0$ — conserved. Mechanism: zero moment of the force, not absence of force. $\blacksquare$

---

# Key Takeaways

**Two terms, two reasons — never collapse them.** The single most important discipline in this proof is recognising that $dJ_C/d\tau$ has two terms that vanish for *different* reasons. The term $\frac{d\overrightarrow{CM}}{d\tau}\wedge p$ vanishes because the four-velocity is parallel to the four-momentum, $p = mU$ — a relativistic identity that holds *always*, force or no force. The term $\overrightarrow{CM}\wedge\frac{dp}{d\tau}$ vanishes only when there is no force (law of inertia) or when the force is central (zero moment). Collapsing both into "$dp/d\tau = 0$" hides the structure and misses that conservation can hold for a *non-free* particle under a central force. The trigger to keep them separate: whenever you differentiate a product (or wedge) of a position and a momentum, the position-derivative term and the momentum-derivative term have independent fates, and you must check each.

**Conservation is geometry: constant momentum along a fixed line has constant moment.** The geometric picture from part 3 is the most transferable intuition. The angular momentum is momentum times perpendicular distance to the line of motion; for a free particle both are constant (the line is fixed, the momentum is free), so the angular momentum is constant *despite* the position growing without bound. The position's growth is entirely along the line of motion, parallel to the momentum, and parallel displacements contribute nothing to a cross product. This is why a free particle, sliding off to infinity, keeps a fixed angular momentum about any point: only the perpendicular lever arm matters, and it does not change. The diagnostic — "only the perpendicular component of the displacement contributes to the moment" — is the reusable lesson, and it explains at a glance why free particles conserve angular momentum and why central forces (parallel to the displacement) exert no torque.

**Central forces conserve angular momentum by zero moment, not zero force.** Part 4 isolates a distinct and reusable mechanism: a force can be present yet conserve angular momentum, provided it is central (parallel to the displacement from the reference point), because then its *moment* $\overrightarrow{CM}^\flat\wedge f$ vanishes. This is the relativistic foundation of the Kepler problem's first integral and of every central-force orbit. The trigger to recognise: whenever a force always points toward or away from a fixed centre, the angular momentum about that centre is conserved, the orbit lies in a plane, and the problem reduces to a one-dimensional radial equation. The contrast with the free-particle case — zero force versus zero moment — sharpens the understanding that what conservation of angular momentum really requires is not the absence of force but the absence of *torque*, and torque is the moment of the force, which a central force lacks.
