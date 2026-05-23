---
type: exercise-index
subject: general-relativity
section: "1.3"
tags: [physics, general-relativity, variational-principle, action]
---

## §1.3 Hilbert's Variational Approach — Exercises

This section's exercises explore the variational formulation of general relativity: the Hilbert action $S = (1/16\pi G)\int R\sqrt{-g}\, d^4x + S_\text{matter}$ as the source of Einstein's equations via $\delta S = 0$, the variational definition of the stress-energy tensor $T_{\mu\nu} = -(2/\sqrt{-g})\delta S_\text{matter}/\delta g^{\mu\nu}$, and the systematic computation of $T_{\mu\nu}$ for various matter Lagrangians. The drills test the variational technique applied to different matter types (electromagnetic, scalar field), the verification of stress-energy conservation as a Noether identity for diffeomorphism invariance, and the structure of the variation $\delta(R\sqrt{-g})$ that produces the Einstein tensor. The convergent strategy is to identify which parts of the matter Lagrangian depend on the metric (typically $\sqrt{-g}$ and the inverse metric $g^{\mu\nu}$ appearing in kinetic terms), vary these, and assemble the resulting tensor; conservation is then automatic via the Noether identity.

- [[Ex - Stress-Energy Tensor of the Electromagnetic Field]] (⭐⭐) — Apply the variational definition to the Maxwell action $-(1/16\pi)\int F_{\mu\nu} F^{\mu\nu}\sqrt{-g}\, d^4x$; derive the stress-energy tensor $T_{\mu\nu}^\text{EM} = (1/4\pi)[F_{\mu\rho} F_\nu{}^\rho - \frac{1}{4} g_{\mu\nu} F^{\rho\sigma} F_{\rho\sigma}]$. Verify symmetry, tracelessness, and conservation. ([[Def - Hilbert Action]], [[Def - Stress-Energy Tensor]], [[Thm - Hilbert's Variational Principle Yields Einstein Equations]])

- [[Ex - Conservation of Energy-Momentum for the Klein-Gordon Field]] (⭐⭐) — Apply the variational definition to the scalar-field action $\int[\frac{1}{2} g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - V(\phi)]\sqrt{-g}\, d^4x$; derive the Klein-Gordon equation (from $\delta\phi$) and the stress-energy tensor (from $\delta g^{\mu\nu}$); verify that conservation $\nabla^\mu T_{\mu\nu}^\phi = (\Box\phi + V'(\phi))\partial_\nu\phi = 0$ when Klein-Gordon holds — a Noether identity for diffeomorphism invariance. ([[Def - Hilbert Action]], [[Def - Stress-Energy Tensor]])

- [[Ex - Newtonian Limit Recovers Poisson Equation]] (⭐⭐) — Linearise the Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ around Minkowski space and show that the $(0,0)$ component reduces to Poisson's $\nabla^2 \phi = 4\pi G\rho$ in the weak-field slow-motion limit. The coupling $8\pi G$ in the Einstein equations is fixed by this requirement of the correct Newtonian limit. ([[Def - The Einstein Field Equations]], [[Thm - Newtonian Limit of Einstein's Equations]])

Additional drills (web-search and beyond the topic page):

- *Hilbert action variation: explicit derivation of $\delta R$.* Show that under $g^{\mu\nu} \to g^{\mu\nu} + \delta g^{\mu\nu}$, the variation of the Ricci scalar is $\delta R = R_{\mu\nu}\delta g^{\mu\nu} + g^{\mu\nu}\delta R_{\mu\nu}$, with the second piece being a *total divergence* (Palatini identity). For compactly-supported variations, the boundary term vanishes, and the variation of the Hilbert action gives the Einstein tensor.

- *Gauss-Bonnet term is topological in 4D.* Show that the Gauss-Bonnet term $\mathcal{G} = R^2 - 4 R_{\mu\nu} R^{\mu\nu} + R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ contributes nothing to the field equations in 4D (it's a topological invariant, $\int \mathcal{G}\sqrt{-g}\, d^4x$ is the Euler characteristic up to a constant). In higher dimensions, $\mathcal{G}$ contributes non-trivially and gives **Lovelock gravity** — a natural extension of GR.

- *Brans-Dicke scalar-tensor gravity.* Vary the Brans-Dicke action $S = (1/16\pi)\int (\phi R - \omega \phi^{-1} \partial^\mu\phi\partial_\mu\phi)\sqrt{-g}\, d^4x + S_\text{matter}[g, \psi]$ with respect to $g^{\mu\nu}$ and the scalar $\phi$. Show that the field equations differ from Einstein's by additional terms involving the scalar field — a viable alternative to GR. Brans-Dicke is observationally constrained by solar-system tests (Cassini mission: $\omega > 40,000$), making it essentially indistinguishable from GR in current observations.

- *Gibbons-Hawking-York term and black hole entropy.* For Euclidean Schwarzschild (Wick-rotated time), evaluate the on-shell action $S_E = S_\text{Hilbert} + S_\text{GHY}$ at the black hole solution. Show that the result is $S_E = \beta M/2 = M^2/(2T_H)$ where $T_H = 1/(8\pi M)$ is the Hawking temperature. This is identified with the thermodynamic free energy, giving the **Bekenstein-Hawking entropy** $S_\text{BH} = A/(4G\hbar) = 4\pi M^2/(G\hbar)$ — area divided by 4 Planck areas. A remarkable result deriving black hole thermodynamics from the on-shell evaluation of the gravitational action.
