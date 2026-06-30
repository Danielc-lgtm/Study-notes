---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Inertial Observer"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Problem Statement

An [[Def - Inertial Observer|inertial observer]] is defined by the vanishing of its four-acceleration and four-rotation; in particular its four-velocity satisfies $\mathrm{d}U/\mathrm{d}\tau = 0$. Working with $c = 1$ in an inertial coordinate system with affine frame $(O; e_0, e_1, e_2, e_3)$:

1. Starting from $a = \mathrm{d}U/\mathrm{d}\tau = 0$, show that the four-velocity components $U^\alpha$ are constants.
2. Using $U^\alpha = \mathrm{d}x^\alpha/\mathrm{d}\tau$, integrate to obtain the worldline $x^\alpha(\tau)$, and identify the eight constants of integration.
3. Conclude that the worldline is a straight line of Minkowski spacetime, and state the form with $c$ restored.
4. Verify that the parameter $\tau$ is proper time, i.e. that the normalisation $U\cdot U = 1$ is consistent with the solution.

**Recall:**

![[Def - Inertial Observer#The Definition]]

The **four-velocity** $U = \mathrm{d}x/\mathrm{d}\tau$ is the derivative of the worldline with respect to [[Def - Proper Time|proper time]] $\tau$, a future-timelike unit vector $U\cdot U = 1$ (in mostly-minus, $c = 1$); see [[Def - Four-Velocity and Four-Acceleration]]. The **four-acceleration** is $a = \mathrm{d}U/\mathrm{d}\tau$. A [[Def - Worldline of a Particle|worldline]] is a timelike curve $\tau\mapsto x^\alpha(\tau)$ in spacetime. In an affine frame, an event $M$ has position $\overrightarrow{OM} = x^\alpha e_\alpha$.

---

# Convergent Strategy

**Problem class.** A *characterise-a-worldline* problem of the simplest kind: integrate a differential condition on the four-velocity to get the worldline. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for observer problems says to compute the four-acceleration first and, when it vanishes, integrate to the explicit worldline.

**Assumption pattern.** The single assumption is $\mathrm{d}U/\mathrm{d}\tau = 0$. This is an ordinary differential equation — the very simplest, a vanishing derivative — and its solution is a constant; integrating once more gives an affine (linear-in-$\tau$) function. The signpost is "vanishing four-acceleration", which always means "integrate twice".

**Theorem routing.** No theorem is needed beyond the definitions: $a = 0 \Rightarrow U = \text{const}$ (one integration), then $U = \mathrm{d}x/\mathrm{d}\tau \Rightarrow x^\alpha(\tau) = U^\alpha\tau + x_0^\alpha$ (second integration). The result is recognised as a straight line because $x^\alpha$ is an affine function of $\tau$. The normalisation $U\cdot U = 1$ is checked against the constant solution to confirm $\tau$ is proper time.

**Key decision point.** The only subtlety is appreciating what the result does *not* say: it gives only that the worldline is straight, equivalent to $a = 0$ alone, and is silent about the four-rotation $\omega$. A reader who concludes "therefore the observer is inertial" has overreached — straightness needs $\omega = 0$ added to be inertiality. This exercise establishes one of the two halves of the definition's geometric content.

---

# Legal Operations Used

1. **Integrate $\mathrm{d}U/\mathrm{d}\tau = 0$ to a straight worldline** (operation 2 from the topic page). The vanishing four-acceleration is integrated once to give a constant four-velocity and once more to give the affine worldline $x^\alpha = U^\alpha\tau + x_0^\alpha$.

2. **Test inertiality by the conditions $a = 0$ and $\omega = 0$** (operation 1 from the topic page). The exercise uses only the first condition, $a = 0$, and is careful to note that the second, $\omega = 0$, is *not* established by straightness — which is the point of the converse-fails remark.

---

# Hints

> [!note]- Hint 1
> "Four-acceleration is zero" means $\mathrm{d}U^\alpha/\mathrm{d}\tau = 0$ for each $\alpha$. What kind of function has zero derivative everywhere?

> [!note]- Hint 2
> Once $U^\alpha$ is a constant, recall that $U^\alpha = \mathrm{d}x^\alpha/\mathrm{d}\tau$. Integrate this once more: the integral of a constant is a linear function of $\tau$ plus a constant.

> [!note]- Hint 3
> The result $x^\alpha(\tau) = U^\alpha\tau + x_0^\alpha$ is the parametric equation of a straight line through the event $x_0$ in the direction $U$. The eight constants are the four $U^\alpha$ (initial four-velocity) and the four $x_0^\alpha$ (initial event).

---

# Solution

The proof is two integrations. Step 1 integrates the vanishing four-acceleration to a constant four-velocity; Step 2 integrates the four-velocity to the affine worldline and recognises it as a straight line; Step 3 confirms the parameter is proper time. The whole content is that a vanishing second derivative gives an affine function.

**Step 1: The four-velocity is constant.**

> [!note]- Derivation
> By [[Def - Inertial Observer|inertiality]], the four-acceleration vanishes:
> $$a^\alpha = \frac{\mathrm{d}U^\alpha}{\mathrm{d}\tau} = 0 \qquad \text{for all } \alpha = 0, 1, 2, 3.$$
> A function on an interval whose derivative is identically zero is constant. Hence each $U^\alpha$ is a constant, which we denote $U^\alpha = U_0^\alpha$:
> $$U^\alpha(\tau) = U_0^\alpha = \text{const}.$$
> Geometrically, the four-velocity is one fixed vector of the displacement space $E$, the same at every event of the worldline.

**Step 2: The worldline is a straight line.**

> [!note]- Derivation
> The four-velocity is the proper-time derivative of the position: $U^\alpha = \mathrm{d}x^\alpha/\mathrm{d}\tau$ (see [[Def - Four-Velocity and Four-Acceleration]]). With $U^\alpha = U_0^\alpha$ constant, this is
> $$\frac{\mathrm{d}x^\alpha}{\mathrm{d}\tau} = U_0^\alpha.$$
> Integrating in $\tau$,
> $$x^\alpha(\tau) = U_0^\alpha\,\tau + x_0^\alpha,$$
> where $x_0^\alpha$ are four constants of integration. Together with the four $U_0^\alpha$, these are the **eight constants** $(U_0^\alpha, x_0^\alpha)$, fixed by the initial four-velocity and the initial event $\overrightarrow{OM_0} = x_0^\alpha e_\alpha$.
>
> This is the parametric equation of a straight line of Minkowski spacetime: the locus $\{x_0 + \tau U_0 : \tau\in\mathbb{R}\}$ is the affine line through the event $x_0$ in the direction $U_0$. With $c$ restored — recalling $x^0 = ct$ and $U^\alpha = c^{-1}\mathrm{d}x^\alpha/\mathrm{d}t$ on the worldline parametrised by proper time — the worldline reads
> $$x^\alpha(\tau) = c\,U_0^\alpha\,\frac{\tau}{c} + x_0^\alpha = U_0^\alpha(c\tau) + x_0^\alpha,$$
> still an affine function, hence still a straight line. (Gourgoulhon's eq. 8.5 is $x^\alpha(t) = c\,u_0^\alpha\,t + x_0^\alpha$ with $t$ the proper time.)

**Step 3: The parameter is proper time.**

> [!note]- Derivation
> For $\tau$ to be proper time, the four-velocity must be unit, $U\cdot U = 1$ (mostly-minus, $c = 1$). Since $U_0^\alpha$ is constant, the constraint $\eta_{\alpha\beta}U_0^\alpha U_0^\beta = 1$ is a single algebraic condition on the constants, automatically preserved along the worldline (there is nothing to evolve). It reduces the eight constants to seven free parameters: three for the direction of $U_0$ on the unit hyperboloid (the velocity) and four for the initial event. Consistency holds: the constraint is compatible with $U_0$ constant, confirming that $\tau$ is indeed proper time and that equal increments $\Delta\tau$ correspond to equal displacements $U_0^\alpha\Delta\tau$ along the line. Thus an inertial clock ticks uniformly with respect to any inertial coordinate time, dilated only by the constant Lorentz factor $\gamma = U_0^0$.

> [!note]- Complete formal solution
> By [[Def - Inertial Observer|inertiality]] the four-acceleration vanishes, $\mathrm{d}U^\alpha/\mathrm{d}\tau = 0$, so each four-velocity component is constant, $U^\alpha = U_0^\alpha$. Since $U^\alpha = \mathrm{d}x^\alpha/\mathrm{d}\tau$, integrating gives the worldline
> $$x^\alpha(\tau) = U_0^\alpha\,\tau + x_0^\alpha,$$
> an affine function of $\tau$, i.e. the straight line through $x_0$ in the direction $U_0$, with eight integration constants $(U_0^\alpha, x_0^\alpha)$ — the initial four-velocity and initial event. With $c$ restored, $x^\alpha(\tau) = c\,U_0^\alpha\,t + x_0^\alpha$ (proper time $t$), still a straight line. The normalisation $\eta_{\alpha\beta}U_0^\alpha U_0^\beta = 1$ is a single constant constraint, consistent with $U_0$ constant, confirming $\tau$ is proper time. The result establishes that an inertial observer's worldline is straight — equivalently $a = 0$ — but says nothing about the four-rotation; straightness is necessary, not sufficient, for inertiality. $\blacksquare$

---

# Key Takeaways

**Vanishing four-acceleration means a straight worldline, by two integrations — the simplest computation in the chapter, but the foundation of everything.** The entire derivation is "zero second derivative gives an affine function", and the affine function $x^\alpha(\tau) = U_0^\alpha\tau + x_0^\alpha$ is the straight worldline. The trigger to recognise this pattern is the phrase "vanishing four-acceleration" or "free particle" or "no force": each is the condition $\mathrm{d}U/\mathrm{d}\tau = 0$, and each is integrated the same way. The eight constants — four velocity components, four position components — are the complete initial data of an inertial observer, exactly as a Newtonian free particle is specified by initial position and velocity. This is the relativistic statement of Newton's first law: in the absence of force, the worldline is straight in spacetime, which is uniform motion in space.

**The result is one half of inertiality, not the whole — straightness controls only $a$, never $\omega$.** The single most important thing this exercise teaches is restraint: having shown the worldline is straight, one must *not* conclude the observer is inertial. Straightness is equivalent to $a = 0$ alone; it is blind to the four-rotation $\omega$, which concerns whether the carried spatial frame precesses. An observer can have a perfectly straight worldline and still be non-inertial because its frame spins ([[Ex - A straight worldline need not be inertial]] constructs exactly this). The diagnostic to carry forward: whenever you have established "straight worldline", ask separately whether the frame rotates, and only when both $a = 0$ and $\omega = 0$ may you say "inertial". Gourgoulhon flags this precisely (his Remark 8.1: the converse of "inertial $\Rightarrow$ straight" is false).

**The constancy of the four-velocity is the lever that unlocks the rest of §12.1.** What this exercise really delivers is not the worldline formula but the fact behind it: $U$ is one fixed vector. Everything else special about an inertial observer flows from that single fact — the rest-space hyperplanes are parallel (same normal $U$), they never intersect, and the inertial coordinates are global ([[Thm - Globality of the Local Rest Space for Inertial Observers]]). Whenever a problem about an inertial observer stalls, the move is to return to "the four-velocity is constant" and ask what that constancy gives. Here it gives a straight line; in the globality theorem it gives a parallel foliation; in the rigid-array construction it gives parallel worldlines with synchronisable clocks. The constancy of $U$ is the seed from which the whole geometry of the inertial frame grows.
