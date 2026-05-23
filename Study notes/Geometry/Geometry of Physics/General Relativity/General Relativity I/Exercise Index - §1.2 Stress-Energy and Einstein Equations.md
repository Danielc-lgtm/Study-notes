---
type: exercise-index
subject: general-relativity
section: "1.2"
tags: [physics, general-relativity, stress-energy, conservation-laws]
---

## §1.2 Stress-Energy and Einstein Equations — Exercises

This section's exercises explore the construction and properties of the matter stress-energy tensor: the dust and perfect-fluid forms, the electromagnetic stress-energy, and the conservation $\nabla^\mu T_{\mu\nu} = 0$. The drills test recognition of the perfect-fluid pattern in various contexts (cosmology, stellar interiors, radiation), the projection technique for decomposing conservation laws into physical equations (continuity and Euler), and the variational definition of $T_{\mu\nu}$ from an action. The convergent strategy is to identify the local invariants of the matter (rest-frame energy density, pressure, four-velocity), write the stress-energy as a tensor combination, and verify conservation by computing $\nabla^\mu T_{\mu\nu}$ — which factors as (equation of motion) $\times$ (something) by Noether's second theorem.

- [[Ex - Stress-Energy Tensor of Dust]] (⭐) — Verify that $T^{\mu\nu} = \rho u^\mu u^\nu$ has the correct rest-frame components and that conservation $\nabla_\mu T^{\mu\nu} = 0$ unpacks (via projection along and orthogonal to $u^\mu$) into the continuity equation and the [[Def - Geodesic|geodesic]] equation. ([[Def - Stress-Energy Tensor]], [[Def - Four-Vector]], [[Def - Spacetime Manifold]])

- [[Ex - Stress-Energy Tensor of the Electromagnetic Field]] (⭐⭐) — Derive the Maxwell stress-energy tensor $T_{\mu\nu} = (1/4\pi)[F_{\mu\rho} F_\nu{}^\rho - \frac{1}{4} g_{\mu\nu} F^2]$ from the action $S = -(1/16\pi)\int F^2 \sqrt{-g}\, d^4 x$ via the variational formula. Verify symmetry, tracelessness ($T^\mu{}_\mu = 0$ — conformal invariance of 4D Maxwell), conservation, and the classical limit $T^{00} = (1/8\pi)(E^2 + B^2)$. ([[Def - Stress-Energy Tensor]], [[Def - Hilbert Action]])

- [[Ex - Conservation of Energy-Momentum for the Klein-Gordon Field]] (⭐⭐) — For a free massive scalar field with action $S_\phi = \int [\frac{1}{2} g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - \frac{1}{2} m^2\phi^2]\sqrt{-g}\, d^4x$, derive the Klein-Gordon equation $\Box\phi + m^2\phi = 0$ (by varying with respect to $\phi$), derive the stress-energy tensor $T_{\mu\nu}^\phi = \partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\mathcal{L}_\phi$ (by varying with respect to $g^{\mu\nu}$), and verify $\nabla^\mu T_{\mu\nu}^\phi = (\Box\phi + m^2\phi)\partial_\nu\phi = 0$ when Klein-Gordon holds. ([[Def - Stress-Energy Tensor]], [[Def - Hilbert Action]])

Additional drills (web-search and beyond the topic page):

- *Perfect fluid in FLRW cosmology.* Substitute the perfect-fluid stress-energy into the FLRW metric and derive the Friedmann equations $H^2 = (8\pi G/3)\rho - K/a^2$ and $\ddot a/a = -(4\pi G/3)(\rho + 3p)$. For different equations of state $w = p/\rho$ (matter $w=0$, radiation $w=1/3$, dark energy $w=-1$), determine the time-evolution of $\rho(a)$ and $a(t)$.

- *Tolman-Oppenheimer-Volkoff (TOV) equation.* For a static spherically symmetric perfect-fluid star, derive the TOV equation $dp/dr = -(\rho + p)(M(r) + 4\pi r^3 p)/[r^2(1 - 2M(r)/r)]$ — the relativistic equation of stellar structure. Compare with Newton's $dp/dr = -\rho M(r)/r^2$; the differences (the $\rho + p$ factor, the $4\pi r^3 p$ inside, the $1 - 2M/r$ outside) come from relativistic effects on pressure, energy density, and spatial curvature.

- *Energy conditions.* For a perfect fluid $T^{\mu\nu} = (\rho + p) u^\mu u^\nu - p g^{\mu\nu}$, formulate and check the **weak energy condition** ($T_{\mu\nu} t^\mu t^\nu \geq 0$ for timelike $t$), the **dominant energy condition** ($-T^\mu{}_\nu t^\nu$ is causal for timelike $t$), and the **strong energy condition** ($T_{\mu\nu} t^\mu t^\nu \geq \frac{1}{2} T t^\mu t_\mu$). Determine which equation-of-state ranges $w = p/\rho$ satisfy each. Show that dark energy ($w = -1$) violates the strong energy condition (gravity is repulsive at cosmological scales).
