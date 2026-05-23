---
type: exercise-index
subject: general-relativity
section: "1.1"
tags: [physics, general-relativity, equivalence-principle]
---

## §1.1 Equivalence Principle and the Metric — Exercises

This section's exercises explore the foundational structure of GR: spacetime as a Lorentzian manifold, the equivalence principle as the demotion of gravity to geometry, and the role of the metric tensor as the gravitational potential. The drills test recognition of when the equivalence principle applies (any locally inertial frame), the identification of the Newtonian potential with the $g_{00}$ component of the metric, and the systematic reduction of GR to Newton in the weak-field slow-motion limit. The convergent strategy is to use the weak-field expansion $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$, identify $h_{00} = 2\phi$ (with $\phi$ the Newtonian potential), and verify that all Newtonian formulas emerge as leading-order limits.

- [[Ex - Newtonian Limit Recovers Poisson Equation]] (⭐⭐) — Linearise the Einstein equations around Minkowski; show that the $(0, 0)$ component reduces to Poisson's $\nabla^2 \phi = 4\pi G\rho$ in the weak-field slow-motion limit, confirming the coupling constant $8\pi G$ of GR is fixed by the Newtonian limit. ([[Def - The Einstein Field Equations]], [[Def - The Metric Tensor as Gravitational Potential]], [[Thm - Newtonian Limit of Einstein's Equations]])

- [[Ex - The Schwarzschild Radius and the Event Horizon]] (⭐⭐) — Compute the Kretschmann scalar $K = 48 M^2/r^6$ of Schwarzschild and verify $r = 2M$ is a coordinate singularity (regular geometry), $r = 0$ is a curvature singularity (divergent geometry). Construct Eddington-Finkelstein coordinates to extend across the horizon. ([[Def - The Schwarzschild Metric]], [[Def - Spacetime Manifold]])

- [[Ex - Light Bending Around the Sun (Order of Magnitude)]] (⭐⭐) — Compute the deflection of a light ray grazing the Sun in Schwarzschild geometry: $\Delta\phi = 4GM/(bc^2) \approx 1.75''$. Compare with the naive Newtonian particle deflection $2GM/(bc^2)$ — the factor of 2 discrepancy was confirmed by Eddington's 1919 eclipse expedition. ([[Def - The Schwarzschild Metric]])

Additional drills (web-search and beyond the topic page):

- *Pound-Rebka gravitational redshift.* Compute the predicted gravitational redshift of a $\gamma$-ray climbing a tower of height $h$ on Earth: $\Delta\nu/\nu = gh/c^2$. For the Pound-Rebka experiment ($h = 22.5$ m), the predicted redshift is $\sim 2.5 \times 10^{-15}$ — measurable with Mössbauer spectroscopy.

- *Why does GPS need GR?* GPS satellites orbit at $\sim 20,000$ km altitude. Compute the gravitational time dilation between the satellite and the ground, plus the special-relativistic time dilation from orbital motion ($v \sim 4$ km/s). Show that the net effect is $\sim 38$ microseconds per day — without GR correction, GPS positions would drift by $\sim 10$ km per day.

- *Tidal forces in free-fall frame.* In a freely-falling frame of finite size $\ell$ near Earth, compute the relative acceleration of two test bodies separated by $\ell$. Show that the tidal acceleration is $\sim (GM/r^3)\ell$, vanishing only in the limit $\ell \to 0$ — the equivalence principle is *local*, with the Riemann tensor encoding the obstruction to making it global.
