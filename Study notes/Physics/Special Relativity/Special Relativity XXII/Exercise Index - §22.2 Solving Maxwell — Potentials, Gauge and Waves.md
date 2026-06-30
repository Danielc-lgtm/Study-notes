---
type: exercise-index
subject: special-relativity
section: "22.2"
tags: [physics, special-relativity]
---

## §22.2 Solving Maxwell — Potentials, Gauge and Waves — Exercises

The exercises of §22.2 drill the solution machinery of electromagnetism: introduce the four-potential $A$ (making $dF = 0$ automatic), fix the gauge to decouple the field equation, and solve the resulting wave equation. The unifying route is fixed and worth memorising — write $F = dA$, impose the Lorenz gauge $\nabla\cdot A = 0$, reduce $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ to the wave equation $\Box A = \mu_0 J$, and solve. The exercises span the three regimes: the source-free wave (a transverse, null plane wave), the gauge reduction itself (always attainable by solving a scalar wave equation for the gauge function), and the static limit (where the wave equation degenerates to Poisson's equation and recovers the Coulomb field). The recurring insight is that the potential is the lever and $F = dA$ its fulcrum: every solution method routes through stepping up to $A$ and back down to $F$.

- [[Ex - The plane electromagnetic wave]] (⭐⭐) — solve $\Box F = 0$ with a plane-wave ansatz, show $\Box A = 0$ forces a null wave-vector $k\cdot k = 0$ and Lorenz gauge forces transversality $k\cdot a = 0$, compute the field as the wedge $F = -(k\wedge a)\sin$ and show both invariants vanish (the wave is null), and decompose onto an observer to recover the right-handed triad $\mathbf E\perp\mathbf B\perp\hat{\mathbf n}$ with $|\mathbf E| = c|\mathbf B|$ ([[Thm - Electromagnetic Waves]], [[Def - The Four-Potential]], [[Thm - Maxwell Equations]], [[Def - Gauge Choice and the Lorenz Gauge]]).

- [[Ex - Reducing to the Lorenz gauge]] (⭐⭐) — show $\nabla\cdot A \to \nabla\cdot A + \Box\chi$ under $A \to A + d\chi$, so solving $\Box\chi = -\nabla\cdot A$ always attains the Lorenz gauge, insert $F = dA$ to reduce $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ to the decoupled wave equation $\Box A = \mu_0 J$, exhibit the residual freedom $\Box\chi = 0$, and explain why the Lorenz gauge is Lorentz-invariant (a scalar four-divergence) while the Coulomb gauge is not ([[Def - Gauge Choice and the Lorenz Gauge]], [[Def - The Four-Potential]], [[Thm - Maxwell Equations]]).

- [[Ex - The Coulomb field as a static potential]] (⭐⭐) — for a static charge reduce $\Box A = \mu_0 J$ to Poisson's equation $\nabla^2 V = -\rho/\varepsilon_0$, solve for a point charge to get the Coulomb potential $V = \frac{q}{4\pi\varepsilon_0 r}$, differentiate to recover Coulomb's law $\mathbf E = \frac{q}{4\pi\varepsilon_0 r^2}\hat{\mathbf r}$ with $\mathbf B = 0$, and verify against Gauss's law on a sphere ([[Def - The Four-Potential]], [[Def - Gauge Choice and the Lorenz Gauge]], [[Thm - Maxwell Equations]], [[Thm - Electric Charge Conservation and the Gauss Theorem]]).
