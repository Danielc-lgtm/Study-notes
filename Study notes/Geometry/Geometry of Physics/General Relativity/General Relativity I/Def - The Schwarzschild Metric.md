---
type: definition
subject: general-relativity
prereqs:
  - "Def - The Einstein Field Equations"
  - "Def - Spacetime Manifold"
  - "Def - Lorentzian Manifold"
tags: [physics, general-relativity, black-holes, exact-solutions]
---

# Notation

Spacetime $(M, g)$ with signature $(+,-,-,-)$, geometrised units $c = G = 1$. The Schwarzschild metric uses coordinates $(t, r, \theta, \phi)$: $t$ is the time of an asymptotic observer at rest at infinity, $r$ is the **areal radius** (sphere $r = a$ has area $4\pi a^2$, *not* radial distance from the centre), $\theta, \phi$ are standard spherical angles. The standard round 2-sphere metric is $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2$. $M$ denotes the **mass parameter** (in geometrised units, the literal mass of the central body; in $G$-units, $M$ has dimensions of mass and corresponds to length $GM/c^2$). The **Schwarzschild radius** is $r_s = 2M$ (or $r_s = 2GM/c^2$ in conventional units). Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Axiom Motivation

The desideratum is to identify the gravitational field outside an isolated, non-rotating, spherically symmetric mass — the simplest non-trivial source. This is the analogue of computing the Coulomb potential outside a static spherically symmetric charge distribution in electromagnetism: by symmetry, the answer depends on only one variable (the radial distance), and the field equations reduce to ODEs. In Newtonian gravity, the answer is $\phi = -GM/r$ (the inverse-square field of a point mass); in GR, the answer is the **Schwarzschild metric**.

**What symmetries do we impose?**

(i) **Spherical symmetry**: the metric is invariant under the $SO(3)$ action of spatial rotations. This means we can choose coordinates in which the angular dependence is exactly that of the round 2-sphere: $g_{\theta\theta} = -r^2$, $g_{\phi\phi} = -r^2 \sin^2\theta$, $g_{\theta\phi} = 0$ — i.e., the metric on the angular variables is $-r^2 d\Omega^2$ for some "radial coordinate" $r$ (which we can choose to be the areal radius).

(ii) **Stationarity** (time-translation invariance): the metric components are independent of the time coordinate $t$. The asymptotically flat case adds *staticness*: the metric is invariant under the time-reversal $t \to -t$ as well, which forces the off-diagonal $g_{tr}$ to vanish.

(iii) **Asymptotic flatness**: the metric approaches the Minkowski metric at $r \to \infty$. This ensures the mass parameter $M$ has a unique meaning as the total mass measured by an observer at infinity (the ADM mass).

(iv) **Vacuum**: $T_{\mu\nu} = 0$, equivalently $R_{\mu\nu} = 0$. This means we are computing the gravitational field outside the source, in the empty region.

The most general ansatz consistent with (i)-(iii) is
$$ds^2 = e^{2\Phi(r)}\, dt^2 - e^{2\Lambda(r)}\, dr^2 - r^2\, d\Omega^2,$$
with two unknown functions $\Phi(r)$ and $\Lambda(r)$ of the radial coordinate alone. Substituting into the vacuum Einstein equations $R_{\mu\nu} = 0$ gives a system of ODEs (computed in [[Thm - Schwarzschild Solution]]) with the unique solution
$$e^{2\Phi(r)} = e^{-2\Lambda(r)} = 1 - \frac{2M}{r},$$
where $M$ is an integration constant. Identifying $M$ with the Newtonian mass via the weak-field limit (so that the [[Def - Geodesic|geodesic]] equation in the Newtonian limit gives $\ddot x^\alpha = -\partial^\alpha \phi$ with $\phi = -M/r$) fixes the interpretation.

**Why is the areal radius $r$ the right choice?** In a spherically symmetric metric, we have freedom in how we label the radial coordinate. We could use the *proper radial distance* from some reference point; or we could use a coordinate adapted to the angular metric. The choice $r =$ "areal radius", defined by the area of the sphere of constant $r$ being $4\pi r^2$, is the simplest and the one that appears in the Schwarzschild solution. Note: $r$ is *not* the proper radial distance — that is $\int (1 - 2M/r)^{-1/2}\, dr$, which is larger than $r$ for the Schwarzschild metric. The naming "radial coordinate" is conventional but slightly misleading.

**Why does the solution have only one parameter?** This is **Birkhoff's theorem** in action: the unique spherically symmetric vacuum solution is parametrised by one number (the mass $M$). Even if the spherically symmetric source is dynamically pulsating (a radially oscillating star), the *exterior* metric is still the same static Schwarzschild metric — no monopole gravitational radiation is emitted. The mass $M$ is the only "hair" the Schwarzschild solution has.

**What happens at $r = 2M$?** The metric components blow up: $g_{tt} = 0$ and $g_{rr} = \infty$. Two possibilities: this is either a *coordinate singularity* (the geometry is regular but the chosen coordinates are bad) or a *curvature singularity* (the geometry is genuinely singular). Computing curvature scalars — e.g., the Kretschmann scalar $K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma} = 48 M^2/r^6$ — shows that $K$ is finite at $r = 2M$ but diverges at $r = 0$. So $r = 2M$ is a coordinate singularity (the **event horizon** of a black hole), and $r = 0$ is a genuine curvature singularity (where the geometry breaks down).

**Per-property motivation:**

(a) *If we drop spherical symmetry*: the metric has more components and the field equations don't reduce to ODEs in one variable. Examples: **Kerr metric** (axial symmetry, two parameters $M$ and angular momentum $J$); general stationary vacuum solutions can have many parameters.

(b) *If we drop staticness*: with only stationarity, off-diagonal $g_{ti}$ components appear (frame dragging) — the Kerr metric is stationary but not static.

(c) *If we drop asymptotic flatness*: the integration constants take different physical meanings. **Schwarzschild-de Sitter** ($\Lambda > 0$): $g = (1 - 2M/r - \Lambda r^2/3) dt^2 - (\ldots)^{-1} dr^2 - r^2 d\Omega^2$. Asymptotically de Sitter rather than Minkowski.

(d) *If we drop vacuum*: with a matter source, the interior of a star has a different (TOV) metric; Schwarzschild is the **exterior** solution.

---

# The Definition

> **Definition (Schwarzschild metric).** The **Schwarzschild metric** is the spherically symmetric, static, asymptotically flat vacuum solution of the Einstein field equations. In **Schwarzschild coordinates** $(t, r, \theta, \phi)$ (with $r > 2M$ in the exterior region):
> $$ds^2 = \left(1 - \frac{2M}{r}\right) dt^2 - \left(1 - \frac{2M}{r}\right)^{-1} dr^2 - r^2\, d\theta^2 - r^2 \sin^2\theta\, d\phi^2.$$
>
> Here:
> - $M$ is the **mass parameter** (in geometrised units; in conventional units, the gravitational mass of the source in units of $GM/c^2$).
> - $r_s = 2M$ is the **Schwarzschild radius** (the radius of the **event horizon** for a black hole, or the gravitational length scale for any source of mass $M$).
> - The coordinates are valid in the exterior region $r > 2M$; the interior region $0 < r < 2M$ has the same form but with the meaning of $t$ and $r$ swapped (the coordinate $r$ becomes timelike, $t$ becomes spacelike).
>
> The metric is the unique solution of the vacuum Einstein equations $R_{\mu\nu} = 0$ subject to spherical symmetry, staticness, and asymptotic flatness; this is **Birkhoff's theorem** (see [[Thm - Birkhoff's Theorem]]).

**Alternative coordinate systems:**

**Isotropic coordinates** $(\bar t, \bar r, \theta, \phi)$:
$$ds^2 = \left(\frac{1 - M/(2\bar r)}{1 + M/(2\bar r)}\right)^2 d\bar t^2 - \left(1 + \frac{M}{2\bar r}\right)^4 (d\bar r^2 + \bar r^2 d\Omega^2),$$
where $r = \bar r(1 + M/(2\bar r))^2$. Useful because the spatial part is conformally flat.

**Eddington–Finkelstein coordinates** (advanced) $(v, r, \theta, \phi)$ with $v = t + r + 2M \ln|r/(2M) - 1|$:
$$ds^2 = \left(1 - \frac{2M}{r}\right) dv^2 - 2\, dv\, dr - r^2\, d\Omega^2.$$
This chart extends smoothly across the horizon $r = 2M$, revealing it as a coordinate singularity of the Schwarzschild chart, not a curvature singularity.

**Kruskal–Szekeres coordinates** $(U, V, \theta, \phi)$: the maximal analytic extension, revealing the full structure of the Schwarzschild geometry with two asymptotically-flat exterior regions ("our" region and a parallel universe) connected by an Einstein–Rosen bridge (wormhole), plus the black-hole and white-hole interior regions.

**Tortoise coordinate** $r_* = r + 2M \ln|r/(2M) - 1|$: maps the exterior region $r > 2M$ to $r_* \in (-\infty, \infty)$, with $r_* \to -\infty$ as $r \to 2M$. Useful for analysing wave propagation in the Schwarzschild geometry.

---

# Categorical / Structural Definition

The Schwarzschild metric is, structurally, the unique element of two intersecting structures:

(i) The space of spherically symmetric, static, asymptotically flat metrics on $\mathbb{R} \times \mathbb{R}^3 \setminus \{0\}$.

(ii) The space of solutions of the vacuum Einstein equations $R_{\mu\nu} = 0$.

The intersection has one parameter (the mass $M$), giving the one-parameter Schwarzschild family. By **Birkhoff's theorem**, the assumption of staticness is redundant: spherical symmetry plus vacuum forces staticness automatically. So the moduli space of spherically symmetric vacuum spacetimes is one-dimensional, parametrised by $M$.

In the **black hole no-hair theorem** framework, the Schwarzschild solution is the $J = 0$, $Q = 0$ case of the more general Kerr–Newman family parametrised by mass $M$, angular momentum $J$, and electric charge $Q$. The full family is the moduli space of stationary asymptotically flat black hole vacuum solutions to Einstein-Maxwell theory.

---

# Relate to Other Fields / Compression

**True name:** The Schwarzschild metric is *the GR replacement for the Newtonian potential $\phi = -GM/r$ of a point mass*. Both describe the gravitational field outside a non-rotating spherical mass; the Newtonian formula is the weak-field, slow-motion limit of the Schwarzschild metric (with $g_{tt} \approx 1 + 2\phi = 1 - 2M/r$). The Schwarzschild geometry is what Newton's potential becomes when you take seriously the spacetime structure of gravity.

The connection to **Newtonian gravity** is operational: in the limit $r \gg 2M$, Schwarzschild geodesics reduce to Newtonian orbits, with the leading corrections being the post-Newtonian effects (perihelion precession, light bending, time delay) that are the **classical tests of GR**. The factor of 2 in the light-bending prediction over the naive Newtonian-particle answer is precisely the contribution of the *spatial* part of the metric, $g_{rr} = -(1 - 2M/r)^{-1}$, beyond just the temporal $g_{tt}$.

In **black hole physics**, the Schwarzschild metric is the prototype: it has all the essential features (event horizon, singularity, Hawking radiation, no-hair) of more general black holes (Kerr, Reissner–Nordström) while being the simplest to compute with. The structure $r = 2M$ (event horizon) and $r = 0$ (singularity) is the template for understanding more general black-hole solutions.

In **cosmology**, the Schwarzschild metric describes the gravity of any spherical mass within a roughly flat asymptotic region — the geometry around the Sun in our solar system, around individual stars in a galaxy, around the central supermassive black hole of a galaxy. The corrections from the surrounding (cosmological) geometry are negligible at solar-system scales.

---

# Examples / Corollaries

**Is an instance — the gravity outside the Sun.** The Sun has mass $M_\odot \approx 2 \times 10^{30}$ kg, corresponding to $GM_\odot/c^2 \approx 1.5$ km. So the Schwarzschild radius of the Sun is $\sim 3$ km, while its actual physical radius is $\sim 700,000$ km — well outside the horizon. The Schwarzschild metric describes the gravity in the entire exterior region, where all classical tests of GR (light bending, perihelion precession of Mercury, Shapiro time delay) are performed.

**Is an instance — the gravity around a non-rotating black hole.** A black hole of mass $M$ with no rotation has Schwarzschild geometry. The event horizon is at $r = 2M$; outside, the geometry is exactly Schwarzschild. Inside (in the maximal extension), there is a singularity at $r = 0$ that all infalling worldlines eventually reach.

**Is an instance — the exterior of a star (or planet).** By Birkhoff's theorem, *any* spherically symmetric mass distribution has Schwarzschild geometry in its exterior region — the Earth, the Moon, a neutron star, a typical galaxy (to leading order, neglecting its non-spherical structure). The mass $M$ is the total mass within the radius of the body.

**Is NOT a solution if rotating.** A rotating spherical body has the **Kerr metric** in its exterior, not Schwarzschild — adding the angular-momentum parameter $J$. Schwarzschild is the $J = 0$ limit of Kerr.

**Is NOT a solution if charged.** A charged spherical body has the **Reissner–Nordström metric**: $g_{tt} = (1 - 2M/r + Q^2/r^2)$, with $Q$ the charge. Schwarzschild is the $Q = 0$ limit.

**Is NOT a solution if surrounded by matter.** If there is matter exterior to the source (a cosmological background, an accretion disk), the exterior metric is modified. Schwarzschild assumes pure vacuum in the exterior.

**Corollary — coordinate singularity at $r = 2M$.** The metric components $g_{tt}$ and $g_{rr}$ blow up, but the spacetime is regular: curvature scalars are finite, and Eddington–Finkelstein coordinates extend the metric smoothly across.

**Corollary — curvature singularity at $r = 0$.** The Kretschmann scalar $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma} = 48 M^2/r^6$ diverges as $r \to 0$ — a genuine curvature singularity, not a coordinate artefact.

**Corollary — proper distance vs. coordinate $r$.** The proper radial distance between two spheres of areal radii $r_1$ and $r_2$ (with $r_1 < r_2 <$ outside horizon) is $\int_{r_1}^{r_2} (1 - 2M/r)^{-1/2}\, dr$, which is *greater* than $r_2 - r_1$ (the spatial geometry is "stretched" radially compared to Euclidean). This is the GR analogue of Newton's negative gravitational potential.

**Corollary — time dilation in Schwarzschild.** A static observer at radius $r$ measures proper time $d\tau = \sqrt{1 - 2M/r}\, dt$, where $dt$ is the asymptotic time coordinate. So a clock at smaller $r$ runs slower than one at larger $r$ — **gravitational time dilation**. The effect diverges as $r \to 2M$: a clock at the horizon would appear (to an outside observer) to be infinitely time-dilated.

**Corollary — innermost stable circular orbit (ISCO).** The effective potential for timelike circular orbits in Schwarzschild has a minimum at $r = 6M$ and an inflection at $r = 6M$. Below this, no stable circular orbits exist; matter inevitably spirals into the black hole. The ISCO at $r_\text{ISCO} = 6M$ is the inner edge of accretion disks around Schwarzschild black holes.

**Corollary — light sphere (photon sphere).** Circular orbits of light exist at $r = 3M$ — the **photon sphere**. Light orbiting at this radius is unstable to perturbations.

**Calibration check.** (i) Verify by direct computation that the Schwarzschild metric satisfies $R_{\mu\nu} = 0$ (this is [[Ex - Computing the Ricci Tensor of the Schwarzschild Metric]]). (ii) Compute $g_{tt}$ at the surface of the Sun ($r = R_\odot \approx 7 \times 10^5$ km, $M_\odot \approx 1.5$ km): $g_{tt} = 1 - 2M_\odot/R_\odot \approx 1 - 4 \times 10^{-6}$ — a tiny deviation from $1$, consistent with the weak gravity of the Sun. (iii) Compute the Kretschmann scalar $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ for the Schwarzschild metric and verify it equals $48 M^2/r^6$, finite everywhere except $r = 0$.

---

# Unlocked by This

> [!tip] Black Holes and the Event Horizon *(from Black Hole Physics)*
> The surface $r = 2M$ in the Schwarzschild metric is the **event horizon** of a black hole: a one-way membrane through which causal signals can pass inward but not outward. Once a worldline crosses the horizon, it must reach the singularity at $r = 0$ in a finite proper time. This is the basis of **black hole physics**: the geometry inside, the **Penrose diagram**, the **Kruskal extension**, the **white hole** time-reverse, and the **wormhole** topology of the maximal extension.

> [!tip] Classical Tests of General Relativity *(from Observational General Relativity)*
> The Schwarzschild geometry around the Sun is the testing ground of GR. Three classical tests: (i) **perihelion precession of Mercury** ($43''$/century in excess of Newtonian, predicted exactly by Schwarzschild geodesics); (ii) **light bending** around the Sun ($1.75''$ for grazing rays, twice the naive Newtonian particle answer; confirmed by Eddington 1919); (iii) **gravitational redshift** of light climbing out of a gravitational well (Pound–Rebka 1959, confirming the $g_{tt}$ time-dilation prediction). Modern tests: **Shapiro time delay** (radar signals to Mars), **frame-dragging** (Gravity Probe B), **gravitational waves** (LIGO).

> [!tip] Kerr Black Hole *(from Rotating Black Holes)*
> Generalising Schwarzschild to include rotation gives the **Kerr metric**, parametrised by mass $M$ and angular momentum $J$. The Kerr geometry has an **ergosphere** (region where no observer can remain stationary), an **inner Cauchy horizon**, and a *ring* singularity (not point). By the **no-hair theorem**, Kerr–Newman is the most general stationary asymptotically flat black hole solution to Einstein–Maxwell theory. Real astrophysical black holes are believed to be near-extremal Kerr (rotating at significant fractions of the maximal $J = M^2$).

> [!tip] Hawking Radiation and Black Hole Thermodynamics *(from Quantum Gravity)*
> Quantum field theory in the Schwarzschild background predicts that the black hole emits thermal radiation at the **Hawking temperature** $T_H = \hbar/(8\pi M)$ — a remarkable quantum-gravitational result. The black hole has entropy $S_\text{BH} = A/(4 G\hbar) = 4\pi M^2/(G\hbar)$ — area divided by 4 Planck areas. These obey thermodynamic laws (first, second, third) formally identical to ordinary thermodynamics, suggesting a deep connection between gravity, quantum mechanics, and information.

> [!tip] Penrose Diagrams and Conformal Compactification *(from Mathematical General Relativity)*
> The maximal analytic extension of Schwarzschild via Kruskal–Szekeres coordinates can be conformally compactified into a **Penrose diagram** — a finite picture revealing the entire causal structure. Includes two asymptotically flat regions, an Einstein–Rosen bridge connecting them, future and past singularities, and various horizons. This is the working tool for analysing global causal structure of spacetimes.

> [!tip] Singularity Theorems and the Inevitability of Singularities *(from Mathematical General Relativity)*
> The Schwarzschild singularity at $r = 0$ is a genuine spacetime singularity. The **Penrose–Hawking singularity theorems** show that this is generic: under reasonable conditions (energy conditions, trapped surface, global hyperbolicity), every gravitational collapse must produce a singularity. So the singularity in Schwarzschild is not an artefact of symmetry but a structural prediction of GR for any sufficiently dense matter distribution.

> [!tip] Numerical Relativity and Binary Mergers *(from Computational General Relativity)*
> The merger of two black holes — observed by LIGO — produces a single Schwarzschild (or Kerr) black hole as the final state, after a complex transient phase requiring numerical simulation. The Schwarzschild geometry is the *attractor* of black hole physics: any gravitational collapse approaches a Schwarzschild (or Kerr–Newman) state at late times, due to the no-hair theorem.

> [!tip] Gravitational Lensing and the Black Hole Shadow *(from Observational Black Hole Physics)*
> Light passing close to a Schwarzschild black hole is bent by GR (the photon sphere at $r = 3M$ is the boundary between "captured" and "escaped" photons). The Event Horizon Telescope (2019) imaged the **shadow** of the supermassive black hole in M87 (and 2022 in Sgr A*), confirming the Schwarzschild/Kerr geometry around real astrophysical black holes via direct imaging.
