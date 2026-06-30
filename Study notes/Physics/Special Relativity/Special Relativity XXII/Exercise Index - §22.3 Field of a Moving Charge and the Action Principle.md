---
type: exercise-index
subject: special-relativity
section: "22.3"
tags: [physics, special-relativity]
---

## §22.3 Field of a Moving Charge and the Action Principle — Exercises

The exercises of §22.3 drill the two capstone results of the chapter: the field of a single charge in arbitrary motion (Liénard–Wiechert), and the derivation of Maxwell's equations from a variational principle. The unifying skill in the Liénard–Wiechert exercises is *retardation* — the field at a point depends on the charge's state at the one retarded point where its worldline pierces the past light cone, localised by the Dirac-delta composition identity — and the resulting split into a Coulomb part ($1/r^2$, non-radiating) and a radiative part ($1/r$, carrying energy to infinity, nonzero only under acceleration). The action exercise closes the logical circle: the simplest Lorentz-scalar Lagrangian $-\tfrac14 F^2 + A\cdot J$ has Maxwell's inhomogeneous equation as its Euler–Lagrange equation, with $dF = 0$ automatic from $F = dA$, and the interaction term identical to the particle's minimal coupling — exhibiting electromagnetism as the abelian member of the family of gauge field theories.

- [[Ex - The Liénard-Wiechert potential from the retarded Green function]] (⭐⭐⭐) — substitute the point-charge current into the retarded-Green-function solution of $\Box A = \mu_0 J$, collapse the spacetime integral onto the worldline, show the timelike worldline pierces the past light cone at one retarded point with crossing rate $|g'(\tau_P)| = 2R$, and apply the Dirac-delta composition identity to obtain $A = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$ ([[Thm - The Liénard-Wiechert Potential]], [[Def - The Electric Four-Current]], [[Def - Gauge Choice and the Lorenz Gauge]]).

- [[Ex - The field of a uniformly moving charge]] (⭐⭐) — set the acceleration to zero in the Liénard–Wiechert field to get the purely Coulombic $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$, show it points at the charge's present (not retarded) position, derive the flattened field $\mathbf E \propto \frac{1 - v^2}{(1 - v^2\sin^2\theta)^{3/2}}$ (enhanced transverse, suppressed longitudinal), and recover the static Coulomb field in the rest frame ([[Thm - The Liénard-Wiechert Potential]], [[Def - The Electromagnetic Field Tensor]]).

- [[Ex - Maxwell's equations from the action]] (⭐⭐⭐) — argue that $-\tfrac14 F^2$ is the unique Lorentz-scalar quadratic first-order free term, derive the Euler–Lagrange field equation by varying and discarding the boundary term, compute $\frac{\partial\mathcal L}{\partial A_\beta} = J^\beta$ and $\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = F^{\beta\alpha}$ to assemble $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, and show $dF = 0$ is automatic while the interaction reduces to the minimal-coupling term $q\int A\cdot dX$ ([[Thm - Maxwell Equations from a Principle of Least Action]], [[Def - The Four-Potential]], [[Thm - Noether Theorem (Relativistic Particle)]], [[Thm - Maxwell Equations]]).

- [[Ex - Larmor radiated power from the radiative field]] (⭐⭐) — write the radiative field $\mathbf E_{\mathrm{rad}} \propto a/r$ of a slowly-moving charge, form the Poynting vector and show it falls off as $1/r^2$ (so the sphere flux is finite — radiation), find the $\sin^2\Theta$ dipole angular distribution (no emission along the acceleration), and integrate to the Larmor formula $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$ ([[Thm - The Liénard-Wiechert Potential]], [[Thm - Electromagnetic Waves]]).
