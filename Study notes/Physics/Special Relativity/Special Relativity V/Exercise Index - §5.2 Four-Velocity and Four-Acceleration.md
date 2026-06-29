---
type: exercise-index
subject: special-relativity
section: "5.2"
tags: [physics, special-relativity]
---

## §5.2 Four-Velocity and Four-Acceleration — Exercises

The exercises of §5.2 drill the kinematic four-vectors built by differentiating the four-position with respect to proper time: the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U = dX/d\tau$ (unit-normalised, $U \cdot U = 1$) and four-acceleration $A = dU/d\tau$ (orthogonal to $U$, spacelike), and the boundary case of the [[Def - Photons and Null Geodesics|photon]], for which this machinery degenerates. The foundational exercise establishes the three free identities ($U \cdot U = 1$, $A \cdot U = 0$, $A \cdot A \le 0$) that every later dynamical calculation rests on; the velocity-addition exercise shows the four-velocity's payoff — that the nonlinear composition of velocities, and aberration, reduce to a single Lorentz transformation $U' = \Lambda U$, because four-velocities transform rather than add; and the photon exercise traces exactly how and why the four-velocity fails for massless particles and what null four-momentum replaces it. The unifying thread: parametrise by proper time and the kinematic objects become genuine four-vectors, with the photon as the degenerate limit where the unit-tangent construction has no analogue.

- [[Ex - Four-velocity has unit norm and four-acceleration is orthogonal to it]] (⭐) — verify $U \cdot U = 1$ in a general frame and in the rest frame, differentiate it to get $A \cdot U = 0$, prove any vector orthogonal to a timelike vector is spacelike (so $A \cdot A \le 0$), and check all three on hyperbolic motion ([[Def - Four-Velocity and Four-Acceleration]], [[Def - Proper Time]], [[Def - Classification of Four-Vectors]]).

- [[Ex - Velocity addition and aberration from the four-velocity]] (⭐⭐) — boost the four-velocity $U' = \Lambda U$ and take ratios of components to recover the relativistic velocity-addition law and the aberration formula $\tan\alpha' = u\sin\alpha/[\gamma_v(u\cos\alpha - v)]$, and explain why four-velocities compose by the Lorentz group rather than by vector addition ([[Def - Four-Velocity and Four-Acceleration]], [[Thm - Relativistic Velocity Addition]], [[Def - The Lorentz Transformation]], [[Def - Rapidity]]).

- [[Ex - Why a photon has no four-velocity but a null four-momentum]] (⭐⭐) — show the proper time vanishes along a null worldline so the four-velocity is undefined, prove no unit null vector exists, exhibit the surviving null four-momentum $P \cdot P = 0$ with its affine parameter, and distinguish a null curve (the bending helix) from a null geodesic (a free photon) ([[Def - Photons and Null Geodesics]], [[Def - Four-Velocity and Four-Acceleration]], [[Def - Proper Time]], [[Def - Classification of Four-Vectors]]).
