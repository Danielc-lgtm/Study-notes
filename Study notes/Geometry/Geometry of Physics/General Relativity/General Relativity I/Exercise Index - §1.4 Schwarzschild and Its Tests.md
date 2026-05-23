---
type: exercise-index
subject: general-relativity
section: "1.4"
tags: [physics, general-relativity, schwarzschild, black-holes, classical-tests]
---

## §1.4 Schwarzschild and Its Tests — Exercises

This section's exercises explore the Schwarzschild metric — the unique spherically symmetric vacuum solution of Einstein's equations — and its observational tests: light bending, perihelion precession, gravitational redshift, the event horizon, and the innermost stable circular orbit. The drills test the technique of computing curvature in an orthonormal frame (Cartan's structural equations), the distinction between coordinate and curvature singularities, the use of Killing-vector conserved quantities to reduce the geodesic equation to a one-dimensional integral, and the matching to Newtonian gravity in the weak-field limit. The convergent strategy for any Schwarzschild calculation is: (i) identify the symmetries (spherical, static); (ii) use Killing vectors to get conserved energy $E$ and angular momentum $L$; (iii) reduce to a radial effective potential equation; (iv) integrate.

- [[Ex - Computing the Ricci Tensor of the Schwarzschild Metric]] (⭐⭐⭐) — Use Cartan's structural equations to compute the connection 1-forms, curvature 2-forms, and Riemann tensor of the Schwarzschild metric in an orthonormal frame. Verify that the Ricci tensor vanishes ($R_{\mu\nu} = 0$), confirming the vacuum Einstein equations. ([[Def - The Schwarzschild Metric]], [[Def - The Einstein Field Equations]], [[Def - Riemannian Metric]])

- [[Ex - The Schwarzschild Radius and the Event Horizon]] (⭐⭐) — Show that $r = 2M$ in Schwarzschild is a coordinate singularity (Kretschmann scalar $K = 48 M^2/r^6$ is finite there), and $r = 0$ is a true curvature singularity ($K$ diverges). Construct Eddington-Finkelstein coordinates that extend the metric smoothly across the horizon. Show that a radially infalling observer reaches the horizon in finite proper time but infinite coordinate time. ([[Def - The Schwarzschild Metric]], [[Def - Spacetime Manifold]])

- [[Ex - Light Bending Around the Sun (Order of Magnitude)]] (⭐⭐) — Compute the deflection angle of a light ray grazing the Sun: $\Delta\phi = 4GM/(bc^2) \approx 1.75''$. Compare with the naive Newtonian particle prediction $2GM/(bc^2)$ — the factor of 2 enhancement comes from the spatial $g_{rr}$ component of the Schwarzschild metric. Confirmed by Eddington's 1919 eclipse expedition. ([[Def - The Schwarzschild Metric]])

Additional drills (web-search and beyond the topic page):

- *Perihelion precession of Mercury (the classical test).* Compute the timelike geodesic in Schwarzschild and find that orbits do not close: each orbit precesses by $\Delta\phi_\text{per} = 6\pi M/[a(1 - e^2)]$ per period, with $a$ the semi-major axis and $e$ the eccentricity. For Mercury ($a \approx 5.8 \times 10^7$ km, $e \approx 0.21$, $M_\odot \approx 1.5$ km), this gives $\approx 43''$/century — exactly the long-standing anomaly that Newtonian gravity could not explain (after accounting for perturbations from other planets). One of the strongest pieces of evidence for GR.

- *Gravitational redshift in Schwarzschild.* Show that a clock at radius $r$ in Schwarzschild measures proper time $d\tau = \sqrt{1 - 2M/r}\, dt$ relative to an asymptotic clock at infinity. A photon climbing from $r_e$ to infinity is redshifted by $\nu_\infty/\nu_e = \sqrt{1 - 2M/r_e}$. For the Pound-Rebka experiment ($h = 22.5$ m, $r_e \approx R_\oplus$), predict $\Delta\nu/\nu \approx 2.5 \times 10^{-15}$ — confirmed by Mössbauer spectroscopy.

- *Innermost stable circular orbit (ISCO).* Show that the effective potential for timelike circular orbits in Schwarzschild has its minimum at $r = 6M$ and an inflection at $r = 6M$ (one stable, one marginally stable). For $r < 6M$, no stable circular orbits exist. The **ISCO** at $r_\text{ISCO} = 6M$ is the inner edge of accretion disks around Schwarzschild black holes. The orbital binding energy at ISCO is $\sim 5.7\%$ of the rest energy — released as radiation during accretion, making accreting black holes the brightest sources in the universe.

- *Photon sphere at $r = 3M$.* Show that null [[Def - Geodesic|geodesics]] admit *circular* orbits only at $r = 3M$ — the **photon sphere**. These orbits are unstable: a slight perturbation either falls into the black hole or escapes. Light orbiting at $r = 3M$ around a Schwarzschild black hole forms the boundary of the "shadow" cast by the black hole — directly imaged by the **Event Horizon Telescope** in M87 (2019) and Sgr A* (2022).

- *Shapiro time delay.* Compute the additional time delay for a light signal passing close to a mass (compared to a straight-line trajectory in flat space): $\Delta t = (4GM/c^3)\ln(4 r_1 r_2/b^2)$ for impact parameter $b$ and distances $r_1, r_2$ to the source and receiver. Verified by radar signals to Mars and Venus reflecting off the spacecraft, with the delay $\sim 200$ microseconds for signals passing near the Sun. Now used in pulsar timing observations of binary systems.
