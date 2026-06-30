---
type: exercise-index
subject: special-relativity
section: "24.2"
tags: [physics, special-relativity]
---

## §24.2 The Relativistic Euler Equation and Sound — Exercises

The exercises of §24.2 drill the central technique of the chapter: extracting the dynamical equations of a perfect fluid by projecting the single conservation law $\nabla_\mu T^{\mu\nu} = 0$ along and orthogonal to the four-velocity. The pressureless limit (dust) shows the projection in its simplest form — mass conservation along the flow, force-free geodesic motion across it. Projecting onto the four-velocity gives the energy equation, which is secretly the first law of thermodynamics and, for a simple fluid, the conservation of entropy along the flow (adiabaticity). Projecting orthogonal to the four-velocity gives the relativistic Euler equation, "$\mathbf{a} = \mathbf{F}/(\rho+p)$" with the proper enthalpy density as inertia, reducing to classical Euler in the slow limit. Finally, linearising the coupled energy and Euler equations produces the wave equation for sound, with speed $c_s^2 = (\partial p/\partial\rho)_S$ — the adiabatic slope of the equation of state, evaluated here for radiation, stiff matter, and dust. The unifying observation: one conservation law, two projections, and the recurring discipline of using $u\cdot a = 0$ to discard terms.

- [[Ex - Dust as the pressureless limit of a perfect fluid]] (⭐) — set $p = 0$ to get $T^{\mu\nu} = \rho\,u^\mu u^\nu$, and show its conservation splits into mass conservation and force-free geodesic motion $a^\mu = 0$, so pressureless matter free-falls ([[Def - Perfect Fluid]], [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]], [[Def - Baryon Four-Current and Its Conservation]], [[Def - Four-Velocity and Four-Acceleration]]).

- [[Ex - Projecting the conservation law onto the four-velocity]] (⭐⭐) — contract $\nabla_\mu T^{\mu\nu} = 0$ with $u_\nu$ to derive the energy equation, interpret it via $\nabla_\mu u^\mu = \dot V/V$ as the first law $d(\rho V) = -p\,dV$, and reduce it (with baryon conservation) to entropy conservation $\nabla_u(s/n) = 0$ ([[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]], [[Def - Perfect Fluid]], [[Def - Baryon Four-Current and Its Conservation]], [[Def - Equation of State and Speed of Sound]]).

- [[Ex - The relativistic Euler equation from the orthogonal projection]] (⭐⭐) — apply the orthogonal projector to $\nabla_\mu T^{\mu\nu} = 0$ to obtain $(\rho+p)a^\mu = -\perp^{\mu\nu}\nabla_\nu p$, verify the time component is automatically satisfied, and take the nonrelativistic limit to recover classical Euler with inertia $\rho + p \to \rho_{\mathrm m}c^2$ ([[Thm - Relativistic Euler Equation]], [[Def - Perfect Fluid]], [[Def - Four-Velocity and Four-Acceleration]], [[Def - Observer and Local Rest Space]]).

- [[Ex - The speed of sound from linearised perturbations]] (⭐⭐) — linearise the energy and Euler equations about a homogeneous adiabatic perturbation to derive the wave equation $-c_s^{-2}\partial_t^2\delta\rho + \nabla^2\delta\rho = 0$, read off $c_s^2 = (\partial p/\partial\rho)_S$, and evaluate it for radiation ($1/\sqrt3$), the stiff fluid ($c$), and dust ($0$), with the causality bound ([[Def - Equation of State and Speed of Sound]], [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]], [[Thm - Relativistic Euler Equation]], [[Def - Perfect Fluid]]).
