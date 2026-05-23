---
type: exercise-index
subject: geometric-mechanics
section: "1.4"
tags: [physics, geometric-mechanics, variational-principles, lagrangian-mechanics]
---

## §1.4 Variational Principles in Mechanics — Exercises

The exercises in this section drill **the two-sided correspondence between variational principles on $TQ$ (Lagrangian) and Hamiltonian flows on $T^*Q$ (Hamiltonian)**, mediated by the Legendre transform. The unifying theme is **the equivalence of three formulations** — Euler–Lagrange equations $\frac{d}{dt}\frac{\partial L}{\partial \dot q} = \frac{\partial L}{\partial q}$ on $TQ$, Hamilton's canonical equations $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$ on $T^*Q$, and Jacobi's geodesic principle $\delta\int \sqrt{2(E - V) g_{ij}\dot q^i \dot q^j}\, dt = 0$ on $TQ$ in the conformally modified metric. Each formulation has different strengths: Lagrangian for symmetry analysis and Noether, Hamiltonian for phase-space geometry and conservation, Jacobi for reducing to a purely geometric statement when energy is conserved.

- [[Ex - Geodesic Flow on a Riemannian Manifold is Hamiltonian]] (⭐⭐) — derive the cotangent-bundle Hamiltonian $H(q, p) = \frac{1}{2}g^{ij}(q) p_i p_j$ from $L = \frac{1}{2}g_{ij}\dot q^i \dot q^j$ via Legendre transform; verify Hamilton's equations recover the geodesic equation $\ddot q^k + \Gamma^k_{ij}\dot q^i \dot q^j = 0$; explicitly identify the Hamiltonian flow on $T^*M$ as a lift of the geodesic spray on $TM$ ([[Def - Hamiltonian Function]], [[Def - The Legendre Transform]], [[Thm - Equivalence of Lagrangian and Hamiltonian Formalisms]]).

- [[Ex - Jacobi's Principle for a Particle in a Central Potential]] (⭐⭐⭐) — apply Jacobi's principle of "least action" to a particle with $L = \frac{1}{2}m|\dot{\vec r}|^2 - V(r)$; show trajectories at fixed energy $E$ are geodesics in the conformally modified metric $g^J_{ij} = 2(E - V)\delta_{ij}$; recover Kepler's elliptical orbits as geodesics in the Jacobi metric for $V = -k/r$; bridge to general relativity (where the Schwarzschild geodesics play the analogous role) ([[Def - The Lagrangian Function]], [[Thm - Hamilton's Principle in TQ Gives Euler-Lagrange Equations]]).

- [[Ex - The Lagrange Submanifold of a Magnetic Field]] (⭐⭐⭐) — for a charged particle in an electromagnetic field, the "minimal coupling" $L = \frac{1}{2}m|\dot{\vec r}|^2 - eV + (e/c)\vec A\cdot\dot{\vec r}$ produces the modified canonical momentum $\vec p = m\vec v + (e/c)\vec A$; the graph of $\vec p$ as a function of $(\vec r, \vec v)$ is a Lagrangian submanifold of $T^*Q \oplus T^*Q$; this is the variational origin of the gauge-covariant momentum operator $-i\hbar\nabla - (e/c)\vec A$ in quantum mechanics ([[Def - Lagrangian Submanifold]], [[Def - The Lagrangian Function]], [[Def - The Legendre Transform]]).
