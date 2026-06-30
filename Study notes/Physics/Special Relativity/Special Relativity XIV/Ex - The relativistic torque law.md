---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Four-Torque"
  - "Thm - Evolution of the Angular Momentum Vector"
  - "Def - Four-Force"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Def - Four-Torque|four-torque]] $N_C = \overrightarrow{CM}^\flat\wedge f$ drives the angular momentum of a particle. Working with $c = 1$:

1. Derive the four-torque from the definition: differentiate $J_C = \overrightarrow{CM}^\flat\wedge p$ along the worldline and show $N_C = dJ_C/d\tau = \overrightarrow{CM}^\flat\wedge f$, where $f = dp/d\tau$ is the [[Def - Four-Force|four-force]], explaining why the term involving $d\overrightarrow{CM}/d\tau$ vanishes.
2. Specialise to an inertial observer measuring the angular momentum vector $\vec\sigma_C$ about a fixed point $C$, and show the [[Thm - Evolution of the Angular Momentum Vector|evolution law]] reduces to the Newtonian torque law $\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F}$.
3. A charged particle moves in a uniform magnetic field $\mathbf{B} = B\hat{\mathbf z}$, with Lorentz force $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$. Compute the rate of change of its angular momentum about a point $C$ on the axis of its circular orbit, and interpret the result.
4. Show that for a central force ($\mathbf{F}\parallel\overrightarrow{CM}$) the angular momentum about $C$ is conserved, recovering the first integral of the relativistic central-force problem.

**Recall:**

![[Def - Four-Torque#The Definition]]

For a particle, $d\overrightarrow{CM}/d\tau = U$ (the four-velocity), and $p = mU$, so $d\overrightarrow{CM}/d\tau\wedge p = U^\flat\wedge mU = 0$. The angular momentum vector is $\vec\sigma_C = \overrightarrow{CM}\times\mathbf{p}$. The [[Thm - Evolution of the Angular Momentum Vector|evolution law]] for an inertial observer and fixed point is $d\vec\sigma_C/dt = \overrightarrow{CM}\times\mathbf{F}$.

---

# Convergent Strategy

**Problem class.** A *derive-and-apply-an-evolution-law* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: the evolution of angular momentum is the moment of the four-force, reducing to the laboratory torque law for an inertial observer.

**Assumption pattern.** A particle under a four-force; the angular momentum is $\overrightarrow{CM}^\flat\wedge p$. The signpost is "rate of change of angular momentum": this is the [[Def - Four-Torque|four-torque]], operation 7, computed by differentiating the defining wedge.

**Theorem routing.** Part 1 differentiates to get $N_C$. Part 2 specialises via the [[Thm - Evolution of the Angular Momentum Vector|evolution theorem]]. Part 3 applies to the Lorentz force. Part 4 uses centrality to get conservation.

**Key decision point.** The crux is recognising that $dJ/d\tau$ has two terms and only the moment-of-force term survives — the $d\overrightarrow{CM}/d\tau\wedge p$ term vanishes by $p\parallel U$. The same structure makes central forces conserve angular momentum (zero moment).

---

# Legal Operations Used

1. **Operation 7 from the topic page (compute a four-torque as $\overrightarrow{CM}^\flat\wedge f$).** The entire exercise is the derivation and application of the four-torque.

2. **Operation 9 from the topic page (kill a term with parallelism).** The $d\overrightarrow{CM}/d\tau\wedge p$ term and the central-force moment both vanish by parallelism.

---

# Hints

> [!note]- Hint 1
> Leibniz: $\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}$. The first term has $\frac{d\overrightarrow{CM}}{d\tau} = U$ and $p = mU$, so it is $U^\flat\wedge mU = 0$. The second is $\overrightarrow{CM}^\flat\wedge f$.

> [!note]- Hint 2
> For an inertial observer and fixed point, the [[Thm - Evolution of the Angular Momentum Vector|general evolution law]] drops the four-acceleration and frame-rotation terms, leaving $\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F}$ — the magnetic (space-space) part of the four-torque.

> [!note]- Hint 3
> For the magnetic field, the orbit is a circle in the plane perpendicular to $\mathbf{B}$. Take $C$ at the centre of the circle, so $\overrightarrow{CM}$ is the radius vector $\mathbf{r}$ (in the plane) and $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ points radially (centripetal). Compute $\overrightarrow{CM}\times\mathbf{F} = \mathbf{r}\times(q\mathbf{v}\times\mathbf{B})$.

> [!note]- Hint 4
> A central force has $\mathbf{F}\parallel\overrightarrow{CM}$, so $\overrightarrow{CM}\times\mathbf{F} = 0$, hence $\frac{d\vec\sigma_C}{dt} = 0$ — conserved. The angular momentum about the centre is a constant of motion.

---

# Solution

The exercise derives the four-torque and specialises it to the laboratory torque law, then applies it to a magnetic field and a central force. Part 1 differentiates; part 2 recovers Newton; part 3 computes the magnetic-field case; part 4 gets the central-force first integral.

**Step 1: Deriving the four-torque.**

> [!note]- Derivation
> By the Leibniz rule for the exterior product,
> $$\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}.$$
> For the first term, $\frac{d\overrightarrow{CM}}{d\tau} = U$ (the four-velocity, since $C$ is fixed), and $p = mU$, so $\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = U^\flat\wedge(mU) = m(U^\flat\wedge U) = 0$ — the wedge of a vector with itself. For the second term, $\frac{dp}{d\tau} = f$, the [[Def - Four-Force|four-force]]. Hence
> $$N_C = \frac{dJ_C}{d\tau} = \overrightarrow{CM}^\flat\wedge f,$$
> the relativistic **moment of the four-force**. The whole change in angular momentum is the moment of the force; the particle's motion relative to $C$ contributes nothing, because the four-velocity is parallel to the four-momentum.

**Step 2: The Newtonian torque law.**

> [!note]- Derivation
> For an inertial observer ($\vec a_0 = 0$, $\vec\omega = 0$, $D^{\mathrm{FW}}_{u_0} = d/dt$) measuring the angular momentum vector about a point $C$ fixed in the observer's reference space ($\vec V_C = 0$), the [[Thm - Evolution of the Angular Momentum Vector|general evolution law]] loses all its correction terms, leaving the magnetic (space-space) part of the four-torque:
> $$\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F},$$
> where $\mathbf{F}$ is the spatial force. This is *exactly* the Newtonian torque law $\frac{d\mathbf{L}}{dt} = \boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$. The relativistic theory recovers the laboratory torque law verbatim for an inertial observer and a fixed reference point — the elaborate four-torque machinery has the right classical limit.

**Step 3: Charged particle in a magnetic field.**

> [!note]- Derivation
> A charge $q$ in a uniform field $\mathbf{B} = B\hat{\mathbf z}$ moves in a circle in the $xy$-plane (the magnetic force does no work, so the speed and $\gamma$ are constant; the orbit is circular). Take $C$ at the centre of the circle, in the orbital plane, so $\overrightarrow{CM} = \mathbf{r}$ is the radius vector (in the plane) and the Lorentz force is $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, pointing radially inward (centripetal). The torque is
> $$\frac{d\vec\sigma_C}{dt} = \mathbf{r}\times\mathbf{F} = \mathbf{r}\times(q\mathbf{v}\times\mathbf{B}).$$
> Since $\mathbf{F}$ is radial ($\parallel\mathbf{r}$ or $\parallel -\mathbf{r}$), the cross product $\mathbf{r}\times\mathbf{F} = 0$: the magnetic force is central about the orbit centre, so it exerts *no torque* about $C$, and the angular momentum about the centre is conserved. (The orbital angular momentum $\vec\sigma_C = \mathbf{r}\times\mathbf{p} = \gamma m r v\,\hat{\mathbf z}$ is constant — the particle circulates at fixed radius and speed.) This is why a charged particle in a uniform magnetic field has a conserved orbital angular momentum about the orbit centre: the centripetal magnetic force has zero moment there.

**Step 4: Central-force conservation.**

> [!note]- Derivation
> For any central force ($\mathbf{F}\parallel\overrightarrow{CM}$ at every instant — the force always points toward or away from $C$), the torque vanishes:
> $$\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F} = 0\qquad(\mathbf{F}\parallel\overrightarrow{CM}),$$
> because the cross product of parallel vectors is zero. Hence the angular momentum about $C$ is conserved:
> $$\vec\sigma_C = \text{const}.$$
> This is the **first integral** of the relativistic central-force problem: the angular momentum about the centre is constant, so the motion lies in a plane (perpendicular to the constant $\vec\sigma_C$), and the orbit problem reduces to a one-dimensional radial equation — exactly as in the Newtonian Kepler problem, but with relativistic energy-momentum relations. The conserved angular momentum is what produces the (precessing) relativistic orbit. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** $\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge f$; first term $= U^\flat\wedge mU = 0$ ($p\parallel U$); so $N_C = \overrightarrow{CM}^\flat\wedge f$.
>
> **Part 2.** Inertial observer, fixed point: the evolution law reduces to $\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F}$, the Newtonian torque law.
>
> **Part 3.** For a charge in $\mathbf{B} = B\hat{\mathbf z}$ with $C$ at the orbit centre, $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ is radial, so $\mathbf{r}\times\mathbf{F} = 0$ — zero torque, conserved orbital angular momentum.
>
> **Part 4.** A central force has $\overrightarrow{CM}\times\mathbf{F} = 0$, so $\vec\sigma_C$ is conserved — the first integral of the relativistic central-force problem, confining the motion to a plane. $\blacksquare$

---

# Key Takeaways

**The four-torque is the moment of the force, and only the moment survives.** The single structural fact is that differentiating the angular momentum gives two terms, and only the moment of the four-force $\overrightarrow{CM}^\flat\wedge f$ survives — the other term, $d\overrightarrow{CM}/d\tau\wedge p$, vanishes because the four-velocity is parallel to the four-momentum. This is the relativistic upgrade of "the rate of change of angular momentum is the torque", $d\mathbf{L}/dt = \mathbf{r}\times\mathbf{F}$, and it reduces to exactly that for an inertial observer and a fixed point. The reusable insight is that the moment of the *force* (not the motion of the particle) drives the angular momentum, and the relativistic identity $p\parallel U$ is what guarantees this — a fact with no role in the Newtonian derivation but essential here. When you need the rate of change of angular momentum, compute the moment of the force and discard everything else.

**Central and centripetal forces exert no torque — zero moment, conserved angular momentum.** Parts 3 and 4 share a mechanism: a force pointing along the displacement from the reference point has zero moment there, so the angular momentum about that point is conserved. The magnetic force on a circular orbit is centripetal (radial about the centre), hence torque-free about the centre; a central force is radial by definition, hence torque-free about the centre. The transferable diagnostic is that whenever a force is parallel to the lever arm — radial, centripetal, central — it conserves angular momentum about the relevant point, the motion lies in a plane, and the problem gains a first integral. This is the foundation of every central-force orbit, from the relativistic Kepler problem to the cyclotron motion of a charge in a magnetic field, and recognising "this force is radial about that point" immediately gives you a conservation law.

**The relativistic torque law is the laboratory torque law plus frame corrections.** The recovery of $d\vec\sigma_C/dt = \mathbf{r}\times\mathbf{F}$ for an inertial observer is the crucial sanity check: relativity does not overturn the laboratory torque law but reproduces it, adding corrections (the $-E\vec a_0$ inertial-force term and the $\vec\omega\times\overrightarrow{OC}$ frame-rotation term) only when the observer accelerates or rotates. The reusable lesson is that the covariant evolution law contains the Newtonian one as its inertial, fixed-point limit, and the extra terms have clear physical origins — pseudo-forces from acceleration, Coriolis effects from rotation. When working in a rotating or accelerated frame, you must include these corrections; in an inertial lab with a fixed reference point, the bare torque law suffices. Knowing which corrections appear when, and that they vanish in the inertial case, lets you move confidently between the covariant and laboratory descriptions of angular-momentum evolution.
