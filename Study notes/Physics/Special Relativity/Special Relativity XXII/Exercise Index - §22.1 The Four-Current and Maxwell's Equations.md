---
type: exercise-index
subject: special-relativity
section: "22.1"
tags: [physics, special-relativity]
---

## §22.1 The Four-Current and Maxwell's Equations — Exercises

The exercises of §22.1 drill the source of the electromagnetic field and the two covariant Maxwell equations. The unifying skill is *translation*: moving between the four-dimensional form ($J = \rho_0 U$; $dF = 0$ and $d{\star}F = \mu_0{\star}J$) and the three-dimensional form (charge density, current density; Gauss, Ampère, Faraday, no-monopole) by projecting onto an observer. Two structural lessons recur — that the homogeneous equations are free once $F = dA$ (via $d^2 = 0$), and that charge conservation $\nabla\cdot J = 0$ is forced by the same nilpotence rather than postulated. The displacement current, far from being an afterthought, is revealed as the time-component partner of the spatial current inside the single four-current $J^\mu = (\rho, \mathbf J)$.

- [[Ex - The homogeneous Maxwell equations from dF equals zero]] (⭐⭐) — unpack $dF = 0$ into the Bianchi identity and project onto an observer to recover $\nabla\cdot\mathbf B = 0$ (all-spatial indices) and Faraday's law $\nabla\times\mathbf E = -\partial_t\mathbf B$ (one temporal index), then show both are automatic when $F = dA$ via $d^2 = 0$ ([[Thm - Maxwell Equations]], [[Def - The Electromagnetic Field Tensor]], [[Special Relativity XIX/Def - The Exterior Derivative|Def - The Exterior Derivative]], [[Thm - Properties of the Exterior Derivative]], [[Def - The Four-Potential]]).

- [[Ex - Charge conservation from the nilpotence of d]] (⭐⭐) — apply $d$ to the inhomogeneous equation and use $d^2 = 0$ to derive $d{\star}J = 0$, give the index version via the symmetry/antisymmetry clash $\nabla_\nu\nabla_\mu F^{\mu\nu} = 0$, project to the continuity equation, and integrate over a spacetime tube with Stokes to prove the total charge is conserved in time and invariant across observers ([[Thm - Electric Charge Conservation and the Gauss Theorem]], [[Thm - Maxwell Equations]], [[Def - The Electric Four-Current]], [[Thm - Stokes Theorem on Spacetime]], [[Thm - Properties of the Exterior Derivative]]).

- [[Ex - The four-current of a continuous medium]] (⭐⭐) — from $J = \rho_0 U$ derive the observer's charge density $\rho = \gamma\rho_0$ (enhanced by length-contraction of the rest-frame volume) and current density $\mathbf J = \rho\mathbf v$, interpret $\nabla\cdot J = 0$ as conservation of each element's proper charge, and draw the structural analogy with the dust four-momentum $P = mU$ ([[Def - The Electric Four-Current]], [[Def - Four-Momentum and Rest Mass]]).

- [[Ex - Maxwell's equations in three-dimensional form]] (⭐⭐⭐) — project both covariant equations onto an observer to recover all four three-dimensional Maxwell equations, identify the displacement current as the $\mu = 0$ (time-derivative) part of the divergence $\nabla_\mu F^{\mu i}$, and show that dropping it makes Ampère's law inconsistent with charge conservation, so the covariant form forces the correction ([[Thm - Maxwell Equations]], [[Def - The Electromagnetic Field Tensor]], [[Def - The Electric Four-Current]], [[Thm - Electric Charge Conservation and the Gauss Theorem]]).
