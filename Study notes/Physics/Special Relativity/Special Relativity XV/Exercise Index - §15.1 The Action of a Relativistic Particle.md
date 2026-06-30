---
type: exercise-index
subject: special-relativity
section: "15.1"
tags: [physics, special-relativity]
---

## §15.1 The Action of a Relativistic Particle — Exercises

The exercises of §15.1 drill the variational principle for a relativistic particle: writing the free action $S = -m\int d\tau$, varying it to obtain the geodesic equation, and adding interactions. The first exercise is the foundational variation — extract the Euler–Lagrange equations, recognise the unit four-velocity inside the derivative of the square root, conclude the worldline is straight, and (for a curved metric) read off the geodesic equation of general relativity. The second works in the inertial-observer parametrisation, where the Lagrangian $-mc^2\sqrt{1 - \mathbf{v}^2}$ becomes a function of the three-velocity alone, giving relativistic Newton's second law and the non-relativistic limit. The third is the minimal-coupling derivation of the Lorentz force, where the field strength $F = dA$ appears automatically as the antisymmetrisation of $\partial A$ and gauge invariance falls out of the line integral of a one-form. The unifying lesson: the action contains the dynamics, and every equation of motion in the chapter is obtained by varying it, with the parameter kept arbitrary until after the variation.

- [[Ex - Deriving the geodesic equation from the variational principle]] (⭐⭐) — vary $S = -m\int\sqrt{\eta\dot x\dot x}\,d\lambda$, use the absence of explicit position dependence to reduce the Euler–Lagrange equations to $du_\mu/d\lambda = 0$ (a straight worldline), exhibit the reparametrisation redundancy $\dot x^\mu[\text{EL}]_\mu \equiv 0$, and generalise to a curved metric to obtain the geodesic equation with Christoffel symbols ([[Def - Relativistic Action of a Free Particle]], [[Thm - Free-Particle Worldline Extremises Proper Time]], [[Def - Four-Velocity and Four-Acceleration]]).

- [[Ex - The relativistic Lagrangian relative to an inertial observer]] (⭐⭐) — reduce the free Lagrangian to $-mc^2\sqrt{1 - \mathbf{V}^2/c^2}$ in an inertial observer's time, compute the conjugate momentum $m\gamma\mathbf{V}$, derive relativistic Newton's second law $d\mathbf{p}/dt = -\nabla V$, and recover the Newtonian kinetic energy in the low-speed limit, noting why fixing an external time is legitimate while fixing proper time is not ([[Def - Relativistic Action of a Free Particle]], [[Def - Four-Momentum and Rest Mass]], [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]).

- [[Ex - The Lorentz force from minimal coupling]] (⭐⭐⭐) — vary the minimal-coupling Lagrangian $-m\sqrt{\eta\dot x\dot x} + qA_\mu\dot x^\mu$, watch the field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ emerge as the antisymmetrisation of $\partial A$, prove the force is pure ($qF_{\mu\nu}U^\mu U^\nu = 0$, so rest mass is conserved), establish gauge invariance under $A \mapsto A + d\chi$, and recover $d\mathbf{p}/dt = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$ ([[Def - Lagrangian for a Particle in a Vector Field]], [[Def - The Electromagnetic Field Tensor]], [[Def - Four-Force]], [[Def - Four-Velocity and Four-Acceleration]]).
