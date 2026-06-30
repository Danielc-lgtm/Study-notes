---
type: exercise-index
subject: special-relativity
section: "24.3"
tags: [physics, special-relativity]
---

## §24.3 Vorticity, Bernoulli and Kelvin's Theorem — Exercises

The exercises of §24.3 exploit the exterior-calculus reformulation of perfect-fluid dynamics — the canonical equation $\Omega(u,\cdot) = T\,dS$ for the vorticity two-form $\Omega = d\pi$ built from the fluid momentum one-form $\pi = hu$ — to derive the classical conservation laws of fluid mechanics in their relativistic form. Bernoulli's theorem emerges as a Noether statement: a stationary flow has a time-translation symmetry, and the conserved Noether charge $\langle\pi, u_0\rangle = h\Gamma$ (energy per baryon) is constant along each streamline, reducing to the classical "enthalpy plus kinetic energy" constant. Irrotational flow is the vanishing of the vorticity two-form, which by the Poincaré lemma gives a velocity potential — but, crucially, it is the enthalpy-weighted velocity $hu$, not $u$, that is the gradient $d\Psi$. Kelvin's circulation theorem is the conservation of the circulation $\oint\pi = \int\Omega$ under transport along the flow, proved by Stokes' theorem on the swept fluid tube and conditional on the flow being barotropic or isentropic — its baroclinic failure being the mechanism of vorticity generation. The recurring lesson: the metric-free exterior derivative makes closedness and exactness do the work, and the vorticity two-form is the structural twin of the electromagnetic field two-form.

- [[Ex - Bernoulli's theorem along a streamline]] (⭐⭐) — use the canonical equation in a stationary flow to prove $\nabla_u\langle\pi, u_0\rangle = 0$, identify the conserved scalar as $h\Gamma$ (energy per baryon), recover the classical Bernoulli constant $H + \tfrac12 V^2$, and apply it to nozzle flow and jet acceleration ([[Thm - Relativistic Bernoulli Theorem]], [[Def - Vorticity 2-Form]], [[Def - Equation of State and Speed of Sound]]).

- [[Ex - Irrotational flow and the velocity potential]] (⭐⭐) — show $\Omega = 0 \iff d\pi = 0$, hence (Poincaré) $hu = d\Psi$, emphasise that it is the enthalpy-weighted velocity that is exact (not $u$), and derive the potential equation $\square\Psi + \nabla\ln(n/h)\cdot\nabla\Psi = 0$, reducing to a wave equation for the stiff equation of state ([[Def - Vorticity 2-Form]], [[Special Relativity XIX/Def - The Exterior Derivative|Def - The Exterior Derivative]], [[Def - Baryon Four-Current and Its Conservation]], [[Def - Equation of State and Speed of Sound]]).

- [[Ex - Conservation of circulation by transport along fluid lines]] (⭐⭐⭐) — write circulation as the flux $\int_\mathcal{S}\Omega$, carry a loop along the flow and apply Stokes on the fluid tube with the canonical equation to prove $C(\mathcal{C}') = C(\mathcal{C}) - \int_\mathcal{T} T\nabla_{e_3}S$, conclude conservation for barotropic or isentropic flow, and connect the baroclinic failure to vorticity generation and Alfvén's frozen-in theorem ([[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)]], [[Def - Vorticity 2-Form]], [[Thm - Stokes Theorem on Spacetime]], [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]).
