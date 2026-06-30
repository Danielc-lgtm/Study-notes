---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Four-Potential"
  - "Def - Gauge Choice and the Lorenz Gauge"
  - "Thm - Maxwell Equations"
tags: [physics, special-relativity]
---

# Problem Statement

Recover the Coulomb field of a static point charge by solving Maxwell's equation for the potential.

1. For a static charge distribution at rest in an observer's frame, the four-current is $J^\mu = (\rho, \mathbf 0)$ and time-independent. Show that the potential can be taken as $A^\mu = (V, \mathbf 0)$ with $\boldsymbol{\mathcal A} = 0$, in Lorenz gauge, and that the wave equation $\Box A = \mu_0 J$ reduces to **Poisson's equation** $\nabla^2 V = -\rho/\varepsilon_0$.
2. Solve Poisson's equation for a point charge $\rho = q\,\delta^{(3)}(\mathbf x)$ to obtain the Coulomb potential $V = \frac{q}{4\pi\varepsilon_0 r}$.
3. Compute the field $\mathbf E = -\nabla V$ and recover Coulomb's law $\mathbf E = \frac{q}{4\pi\varepsilon_0 r^2}\hat{\mathbf r}$, with $\mathbf B = 0$.
4. Verify the result against Gauss's law $\oint\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$ on a sphere centred at the charge.

**Recall:**

![[Def - The Four-Potential#The Definition]]

In [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] is $\Box A^\nu = \mu_0 J^\nu$, with $\Box = \partial_t^2 - \nabla^2$ (inertial coordinates, $c = 1$). For a static configuration $\partial_t = 0$, so $\Box \to -\nabla^2$. Relative to the observer, $A = V\underline{U_0} + \boldsymbol{\mathcal A}$, $\mathbf E = -\nabla V - \partial_t\boldsymbol{\mathcal A}$, $\mathbf B = \nabla\times\boldsymbol{\mathcal A}$.

---

# Convergent Strategy

**Problem class.** A *solve-Maxwell-for-a-given-source* problem in its simplest static instance, the third target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: given the current, find the potential and hence the field. The routine is to choose the gauge, reduce to a solvable equation, solve, and differentiate.

**Assumption pattern.** The given is a static charge at rest, $J^\mu = (\rho, \mathbf 0)$ time-independent. The signpost is "static" — no time dependence and no current, so the magnetic potential vanishes and the d'Alembertian reduces to the Laplacian. What this unlocks is that the four-component wave equation collapses to a single scalar Poisson equation for $V$.

**Theorem routing.** The route is: $J^\mu = (\rho, \mathbf 0)$, static $\to$ Lorenz gauge with $A = (V, \mathbf 0) \to \Box A = \mu_0 J$ becomes $-\nabla^2 V = \mu_0\rho = \rho/\varepsilon_0$ (Poisson); solve for a point charge $\to V = \frac{q}{4\pi\varepsilon_0 r}$; differentiate ([[Def - The Four-Potential]]: $\mathbf E = -\nabla V$) $\to$ Coulomb's law; verify against [[Thm - Electric Charge Conservation and the Gauss Theorem|Gauss's law]].

**Key decision point.** The crux is recognising that in the static case the relativistic wave equation degenerates to the non-relativistic Poisson equation — the time-derivative term in $\Box$ vanishes, and electromagnetism reduces to electrostatics. The decision is to exploit the static symmetry fully: no current means no vector potential, no time dependence means no displacement current, and the whole covariant apparatus collapses to a single elliptic equation.

---

# Legal Operations Used

1. **Operation 4 from the topic page (choose the Lorenz gauge).** Part 1 works in Lorenz gauge, where $\Box A = \mu_0 J$ holds; for the static field this reduces to Poisson's equation.

2. **Operation 5 from the topic page (solve the wave equation with the Green function).** Part 2 solves Poisson's equation, the static limit of the wave equation, whose Green function is the Coulomb $1/r$.

3. **Operation 1 from the topic page (write the field as $F = dA$).** Part 3 differentiates the potential, $\mathbf E = -\nabla V$, to get the field.

---

# Hints

> [!note]- Hint 1
> For a static charge at rest with no current, take $\boldsymbol{\mathcal A} = 0$ and $V$ time-independent. Then $\nabla\cdot A = \partial_t V = 0$ (Lorenz gauge satisfied automatically). The $\nu = 0$ component of $\Box A^\nu = \mu_0 J^\nu$ is $\Box V = \mu_0\rho$; with $\partial_t = 0$, $\Box = -\nabla^2$, so $-\nabla^2 V = \mu_0\rho = \rho/\varepsilon_0$.

> [!note]- Hint 2
> Poisson's equation $\nabla^2 V = -\rho/\varepsilon_0$ for a point source $\rho = q\delta^{(3)}(\mathbf x)$ has the Green-function solution $V = \frac{q}{4\pi\varepsilon_0}\frac{1}{r}$, where $\frac{1}{r}$ is the fundamental solution of the Laplacian, $\nabla^2\frac{1}{r} = -4\pi\delta^{(3)}(\mathbf x)$.

> [!note]- Hint 3
> $\mathbf E = -\nabla V = -\nabla(\frac{q}{4\pi\varepsilon_0 r}) = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf r}}{r^2}$, using $\nabla(1/r) = -\hat{\mathbf r}/r^2$. Since $\boldsymbol{\mathcal A} = 0$, $\mathbf B = \nabla\times\boldsymbol{\mathcal A} = 0$.

> [!note]- Hint 4
> Integrate $\mathbf E$ over a sphere of radius $R$ centred at the charge: $\oint\mathbf E\cdot d\mathbf S = \frac{q}{4\pi\varepsilon_0 R^2}\cdot 4\pi R^2 = \frac{q}{\varepsilon_0}$, matching Gauss's law with enclosed charge $Q = q$.

---

# Solution

The Coulomb field is the static limit of the wave equation. Step 1 reduces $\Box A = \mu_0 J$ to Poisson's equation; Step 2 solves it for a point charge; Step 3 differentiates to Coulomb's law; Step 4 checks against Gauss. The non-obvious point is in Step 1: the relativistic wave equation degenerates to non-relativistic electrostatics when nothing moves.

**Step 1: The static wave equation is Poisson's equation.**

> [!note]- Derivation
> For a static charge at rest, the four-current is $J^\mu = (\rho, \mathbf 0)$ with $\rho$ time-independent. Take the [[Def - The Four-Potential|potential]] $A^\mu = (V, \mathbf 0)$ — no magnetic potential, since there is no current. The [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] $\nabla\cdot A = \partial_t V = 0$ is satisfied automatically because $V$ is static. The $\nu = 0$ component of $\Box A^\nu = \mu_0 J^\nu$ is
> $$\Box V = \mu_0\rho.$$
> With $\partial_t = 0$ (static), the d'Alembertian $\Box = \partial_t^2 - \nabla^2$ reduces to $-\nabla^2$, so
> $$-\nabla^2 V = \mu_0\rho = \frac{\rho}{\varepsilon_0}, \qquad\text{i.e.}\qquad \nabla^2 V = -\frac{\rho}{\varepsilon_0}.$$
> This is **Poisson's equation** of electrostatics. The relativistic wave equation has degenerated to the non-relativistic elliptic equation because nothing depends on time — the displacement current and radiation are absent, and electromagnetism reduces to electrostatics. The spatial components $\Box A^i = \mu_0 J^i = 0$ are solved by $\boldsymbol{\mathcal A} = 0$.

**Step 2: The Coulomb potential solves Poisson's equation.**

> [!note]- Derivation
> For a point charge at the origin, $\rho = q\,\delta^{(3)}(\mathbf x)$, Poisson's equation is $\nabla^2 V = -\frac{q}{\varepsilon_0}\delta^{(3)}(\mathbf x)$. The fundamental solution of the Laplacian satisfies $\nabla^2\frac{1}{r} = -4\pi\,\delta^{(3)}(\mathbf x)$ (the $1/r$ is the Green function of $-\nabla^2$). Therefore
> $$V = \frac{q}{4\pi\varepsilon_0}\,\frac{1}{r},$$
> the **Coulomb potential**. Check: $\nabla^2 V = \frac{q}{4\pi\varepsilon_0}\nabla^2\frac{1}{r} = \frac{q}{4\pi\varepsilon_0}(-4\pi\delta^{(3)}) = -\frac{q}{\varepsilon_0}\delta^{(3)} = -\frac{\rho}{\varepsilon_0}$. ✓

**Step 3: Differentiating gives Coulomb's law.**

> [!note]- Derivation
> The electric field is $\mathbf E = -\nabla V$ (the static case of $\mathbf E = -\nabla V - \partial_t\boldsymbol{\mathcal A}$, with $\boldsymbol{\mathcal A} = 0$):
> $$\mathbf E = -\nabla\!\left(\frac{q}{4\pi\varepsilon_0 r}\right) = -\frac{q}{4\pi\varepsilon_0}\nabla\frac{1}{r} = -\frac{q}{4\pi\varepsilon_0}\left(-\frac{\hat{\mathbf r}}{r^2}\right) = \frac{q}{4\pi\varepsilon_0}\,\frac{\hat{\mathbf r}}{r^2},$$
> using $\nabla(1/r) = -\hat{\mathbf r}/r^2$. This is **Coulomb's law**: the field points radially outward (for $q > 0$) and falls off as $1/r^2$. The magnetic field is $\mathbf B = \nabla\times\boldsymbol{\mathcal A} = 0$ — a static charge produces no magnetic field in its rest frame, exactly as the field of an inertially-moving charge reduces to (a boosted) Coulomb field in [[Thm - The Liénard-Wiechert Potential]].

**Step 4: Verification by Gauss's law.**

> [!note]- Derivation
> Take a sphere $\mathcal S$ of radius $R$ centred at the charge. The flux of $\mathbf E$ through it:
> $$\oint_{\mathcal S}\mathbf E\cdot d\mathbf S = \frac{q}{4\pi\varepsilon_0 R^2}\oint_{\mathcal S}\hat{\mathbf r}\cdot d\mathbf S = \frac{q}{4\pi\varepsilon_0 R^2}\cdot(4\pi R^2) = \frac{q}{\varepsilon_0},$$
> since $\hat{\mathbf r}\cdot d\mathbf S = dS$ on the sphere (the field is radial) and the sphere's area is $4\pi R^2$. This matches [[Thm - Electric Charge Conservation and the Gauss Theorem|Gauss's law]] $\oint\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$ with enclosed charge $Q = q$, and the result is independent of $R$ (the $R^2$ in the field cancels the $R^2$ in the area) — the hallmark of an inverse-square field. ✓

> [!note]- Complete formal solution
> For a static point charge at rest, take $A^\mu = (V, \mathbf 0)$ in Lorenz gauge (satisfied automatically since $\partial_t V = 0$). The wave equation $\Box V = \mu_0\rho$ reduces, with $\partial_t = 0$, to Poisson's equation $\nabla^2 V = -\rho/\varepsilon_0$. For $\rho = q\delta^{(3)}(\mathbf x)$, the Green function of $-\nabla^2$ gives $V = \frac{q}{4\pi\varepsilon_0 r}$. Then $\mathbf E = -\nabla V = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf r}}{r^2}$ (Coulomb's law) and $\mathbf B = 0$. Gauss's law on a sphere of radius $R$ gives $\oint\mathbf E\cdot d\mathbf S = \frac{q}{4\pi\varepsilon_0 R^2}\cdot 4\pi R^2 = q/\varepsilon_0$, confirming the enclosed charge. $\blacksquare$

---

# Key Takeaways

**The static limit of the relativistic wave equation is the non-relativistic Poisson equation.** The unifying lesson is that electrostatics is the time-independent corner of electromagnetism: when the source is static, the d'Alembertian $\Box = \partial_t^2 - \nabla^2$ loses its time-derivative term and becomes $-\nabla^2$, so the covariant wave equation $\Box A = \mu_0 J$ collapses to Poisson's equation $\nabla^2 V = -\rho/\varepsilon_0$. The displacement current vanishes (nothing changes in time), the magnetic potential vanishes (no current), and the four-component relativistic problem reduces to a single elliptic scalar equation. The transferable principle: whenever a relativistic field problem has a static or stationary source, drop the time derivatives and the problem becomes its non-relativistic, elliptic counterpart — Poisson for electrostatics, Laplace in vacuum. This is why electrostatics looks non-relativistic even though it is a special case of a fully relativistic theory.

**The Coulomb field is the Green function of the Laplacian, and the inverse-square law is its signature.** The reusable fact is that the $1/r$ potential is the fundamental solution of $-\nabla^2$ in three dimensions ($\nabla^2(1/r) = -4\pi\delta^{(3)}$), so the field of any static charge distribution is built by convolving $\rho$ with $1/r$. The inverse-square falloff $\mathbf E \sim 1/r^2$ is not an independent empirical law but a geometric consequence: the flux through a sphere is field $\times$ area $\sim (1/r^2)\times r^2$, a constant independent of radius, which is exactly Gauss's law. The trigger to recognise this everywhere is "a static source in three dimensions"; the field is then the $1/r$-convolution, and its flux measures the enclosed charge. The same Green-function logic, with the *retarded* Green function of the d'Alembertian instead of the static $1/r$, gives the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert potential]] for moving charges — the Coulomb field is the static special case.

**Gauss's law provides an independent route that exploits symmetry, bypassing the differential equation entirely.** The verification in Step 4 illustrates a powerful alternative technique: for sufficiently symmetric charge distributions, Gauss's law $\oint\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$ determines the field directly, without solving Poisson's equation. For a spherically symmetric source, the field is radial and constant on spheres, so the flux is $E\cdot 4\pi r^2 = Q/\varepsilon_0$, giving $E = Q/(4\pi\varepsilon_0 r^2)$ in one line. The reusable diagnostic: when a problem has spherical, cylindrical, or planar symmetry, reach for the integral form (Gauss's law) rather than the differential form (Poisson), because the symmetry makes the flux integral trivial. This frame-invariant, symmetry-driven shortcut is the standard method for fields of symmetric distributions, and it provides the independent cross-check that confirms the differential-equation solution.
