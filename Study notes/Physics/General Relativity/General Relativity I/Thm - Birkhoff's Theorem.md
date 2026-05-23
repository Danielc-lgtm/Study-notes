---
type: theorem
subject: general-relativity
prereqs:
  - "Def - The Einstein Field Equations"
  - "Def - The Schwarzschild Metric"
  - "Def - Spacetime Manifold"
tags: [physics, general-relativity, exact-solutions, black-holes]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$, geometrised units. Spherical coordinates $(t, r, \theta, \phi)$ with $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2$. The most general spherically symmetric metric ansatz is $ds^2 = -e^{2\nu(t, r)}\, dt^2 + e^{2\lambda(t, r)}\, dr^2 + r^2 d\Omega^2$ (the angular part is fixed by spherical symmetry, and we have used coordinate freedom to set $g_{tr} = 0$). Full registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Statement

> **Theorem (Birkhoff, 1923).** Any spherically symmetric vacuum solution of the Einstein field equations is necessarily static and is locally isometric to the Schwarzschild metric. Explicitly: if $(M, g)$ is a Lorentzian 4-manifold with metric admitting an isometric $SO(3)$ action whose orbits are spacelike 2-spheres, and if $R_{\mu\nu} = 0$ (vacuum), then there exist coordinates $(t, r, \theta, \phi)$ in a neighbourhood of any point such that
> $$ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2\, d\Omega^2,$$
> with $M$ an integration constant (the mass parameter).
>
> *Corollary 1.* Spherical gravitational collapse — even of a star that is dynamically pulsating, contracting, or expanding spherically — produces no exterior gravitational radiation. The exterior metric is *always* Schwarzschild, depending only on the total mass.
>
> *Corollary 2.* Inside a spherically symmetric matter distribution surrounding a vacuum region (a spherical shell, for example), the metric of the vacuum region is *flat Minkowski space*. This is the GR generalisation of Newton's shell theorem.
>
> *Corollary 3.* In Einstein–Maxwell theory (electromagnetism coupled to gravity), the analogous statement is **Birkhoff–Hoffmann**: the unique spherically symmetric solution with electromagnetic field is the Reissner–Nordström metric.

---

# Motivation

Birkhoff's theorem is the GR generalisation and *sharpening* of Newton's shell theorem. In Newtonian gravity, the gravitational field outside a spherically symmetric mass distribution equals that of a point mass with all the matter concentrated at the centre — and inside a spherical shell, the field vanishes. These are remarkable simplifications that make the Newtonian theory tractable: the entire complicated detail of a spherical body's interior structure is irrelevant to the exterior field, only its total mass matters.

Birkhoff's theorem extends this to GR with an additional, deeper statement: not only is the *exterior* field uniquely determined (by $M$), but the exterior metric is necessarily **static**, even if the source is dynamically changing in time (as long as the change preserves spherical symmetry). A spherically pulsating star produces no time-varying exterior field — therefore no gravitational radiation. This is a strong constraint: it rules out **monopole gravitational radiation** entirely. Gravitational waves require at least **quadrupole** asymmetry — radial pulsations are not enough.

The physical content of Birkhoff's theorem is therefore that gravity, like the Coulomb field outside a spherically symmetric charge distribution, has no spherically symmetric radiative modes. The lowest multipole that can radiate gravity is the quadrupole ($\ell = 2$), corresponding to the famous result that **gravitational wave luminosity** $\dot E \sim G/c^5 \cdot \dddot Q^2$ — the third time derivative of the mass quadrupole moment, vanishing for spherical symmetry.

In black hole physics, Birkhoff's theorem implies that the spherical collapse of a star produces a Schwarzschild black hole — exact, static, depending only on the total mass. The collapse process itself emits no gravitational radiation (no observer outside sees gravitational waves from a perfectly spherical collapse). Asymmetries in the collapse produce gravitational waves; the spherical part is invisible to gravitational wave detectors.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source B₁: Vacuum Einstein equations applied to a spherically symmetric ansatz.* Whenever the field equations are restricted by spherical symmetry (e.g., in a static or stationary scenario), Birkhoff's theorem applies — the solution is necessarily Schwarzschild (or its generalisation). *Example problem*: in cosmology, a spherically symmetric perturbation around a homogeneous background reduces to studying the dynamics of the metric in a Birkhoff-type ansatz; the result that the exterior metric depends only on the enclosed mass is what justifies "Newtonian intuition" for cosmological perturbations on small scales.

*Source B₂: Time-evolving spherically symmetric matter (gravitational collapse).* For a star or matter distribution that is spherically symmetric and evolving in time — collapsing, oscillating, or expanding — Birkhoff's theorem says the *exterior* metric is static Schwarzschild, regardless of the time-dependence of the source. *Bridge argument*: the field equations in vacuum force staticity (the time-dependence drops out); since the exterior is vacuum, the exterior metric is necessarily static. *Example problem*: an unstable spherical star undergoing collapse to a black hole — even with complex internal dynamics, the asymptotic external observer sees only static Schwarzschild gravity, characterised solely by the total mass $M$.

*Source B₃: Spherical electromagnetic source coupled to gravity (Reissner–Nordström).* For a spherically symmetric electromagnetic field plus gravity, the unique solution is Reissner–Nordström (a generalisation of Schwarzschild including the charge). *Bridge argument*: the addition of EM stress-energy changes the field equations but the symmetry argument still forces a unique static solution. *Example problem*: an oscillating spherical charge distribution produces no time-varying exterior metric or EM field — only static Reissner–Nordström outside.

**Targets (Output Amplification).**

*Target T₁: No monopole gravitational radiation.* Birkhoff's theorem combined with spherical-symmetry-preserving dynamics implies that gravitational waves cannot have $\ell = 0$ (monopole) multipole structure. The lowest radiating multipole is $\ell = 2$ (quadrupole). *Useful application*: the **gravitational wave luminosity formula** $\dot E_\text{GW} = (1/5) \langle \dddot Q_{\mu\nu} \dddot Q^{\mu\nu}\rangle$ (Einstein's quadrupole formula) involves only the quadrupole moment, with spherical sources radiating nothing. This is why **LIGO** detects binary mergers (highly non-spherical sources) but not radial oscillations of stars.

*Target T₂: Spherical interior vacuum is Minkowski.* By Birkhoff's theorem applied to a vacuum region inside a spherical shell, the vacuum is Minkowski (the mass parameter $M$ must vanish in the inner solution; otherwise the metric would be singular at $r = 0$). *Useful application*: inside a spherical shell of matter, there is no gravity — the shell exerts no net force on contents (the GR generalisation of Newton's shell theorem). This is what justifies treating the inside of a spherical mass distribution as flat in many approximations.

*Target T₃: Asymptotic Schwarzschild form of any spherical compact object.* Far from any spherically symmetric system (after waiting long enough for transients to decay), the exterior metric is Schwarzschild with $M$ being the total ADM mass. *Useful application*: gravitational mass at infinity is well-defined for any compact spherical source, and the Schwarzschild radius $r_s = 2M$ provides a characteristic length scale (the horizon scale, if $M$ is large enough to be a black hole).

---

# Why Is It True

**The mechanism in one sentence: spherical symmetry restricts the metric to depend only on $t$ and $r$, and the vacuum field equations then force the $t$-dependence to drop out — leaving a one-parameter family of static metrics, the Schwarzschild family.**

To unpack: the most general spherically symmetric metric in coordinates $(t, r, \theta, \phi)$ is, after coordinate adaptation,
$$ds^2 = -e^{2\nu(t, r)}\, dt^2 + e^{2\lambda(t, r)}\, dr^2 + r^2\, d\Omega^2,$$
with $r$ chosen as the areal radius and $g_{tr} = 0$ achieved by coordinate choice (the angular part is fixed by spherical symmetry up to the freedom in $r$). The functions $\nu(t, r)$ and $\lambda(t, r)$ are two free functions to be determined.

The vacuum Einstein equations $R_{\mu\nu} = 0$ give four equations. The off-diagonal $R_{tr}$ equation gives
$$\partial_t \lambda = 0,$$
so $\lambda = \lambda(r)$ — depends only on $r$. The $R_{tt}$ and $R_{rr}$ equations, combined, then give
$$\partial_r(\nu + \lambda) = 0,$$
so $\nu(t, r) = -\lambda(r) + f(t)$ for some function $f(t)$ of $t$ alone. The function $f(t)$ can be absorbed by a redefinition of the time coordinate $\tilde t = \int e^{f(t)/2}\, dt$, after which $\nu = \nu(r) = -\lambda(r)$. So both metric functions depend only on $r$ — the metric is **static**.

The remaining equation (any of $R_{\theta\theta}$, $R_{\phi\phi}$, or the others) gives an ODE for $\lambda(r)$:
$$\frac{d}{dr}(r e^{-2\lambda}) = 1, \quad \text{i.e.,} \quad e^{-2\lambda} = 1 - \frac{2M}{r},$$
where $M$ is an integration constant. Hence $\nu = -\lambda$ gives $e^{2\nu} = 1 - 2M/r$, and the metric is Schwarzschild.

**The key insight: time-dependence is killed by the vacuum equations.** The two vacuum equations $R_{tr} = 0$ (giving $\partial_t\lambda = 0$) and $R_{tt}$ + $R_{rr}$ combination (giving $\partial_t \nu = 0$ after time redefinition) force *both* metric functions to be time-independent — even though the most general spherical ansatz allows time-dependence. The vacuum equations, applied to spherical symmetry, are restrictive enough to enforce staticness automatically. This is the entire content of Birkhoff's theorem.

The reason for this "extra" enforcement of staticness is, deeper, the absence of spherical-symmetric vacuum modes that can propagate: a vacuum Schwarzschild-like spacetime has no monopole radiative degree of freedom (gravitational waves must be quadrupolar, $\ell \geq 2$), so the only spherical vacuum solutions are static ones parametrised by $M$.

---

# What Makes This Hard

The technical difficulty is the computation of the Ricci tensor for the time-dependent spherical ansatz, requiring all four diagonal and the $tr$ component. The off-diagonal $R_{tr} = 0$ equation is the key — it is what kills the time-dependence of $\lambda$. A common error is to start with the *static* ansatz from the beginning (assuming staticness rather than deriving it), which collapses Birkhoff's theorem to "spherically symmetric static vacuum implies Schwarzschild" — true but missing the deeper statement that staticness is *forced*, not assumed. The full theorem (Birkhoff) is the time-dependent statement, and that requires actually computing the Ricci tensor with time-dependent metric functions.

Another subtle point: the theorem is *local* — it asserts local isometry to Schwarzschild in any neighbourhood. Globally, identifications of the maximal extension give other spacetimes (e.g., Schwarzschild with the spatial slice replaced by $S^1 \times S^2$ instead of $\mathbb{R} \times S^2$ — a topologically distinct spacetime with the same local metric). The theorem says nothing about global topology.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Write the most general spherically symmetric metric with two functions $\nu(t, r)$ and $\lambda(t, r)$. Compute the Ricci tensor components. Use the vanishing of $R_{\mu\nu}$ to derive (i) $\partial_t \lambda = 0$, (ii) $\partial_r(\nu + \lambda) = 0$, then re-coordinate $t$ to absorb the residual time-dependence. The remaining ODE in $r$ has a one-parameter family of solutions — the Schwarzschild family.

**Subgoal decomposition:**

1. **General spherical ansatz:** Argue that the most general spherical metric (after coordinate adaptation) is $ds^2 = -e^{2\nu(t, r)} dt^2 + e^{2\lambda(t, r)} dr^2 + r^2 d\Omega^2$.
   - *Hint:* Spherical symmetry fixes the angular part to $r^2 d\Omega^2$ (with $r$ the areal radius); coordinate freedom in $t \to t + f(r)$ kills $g_{tr}$; the remaining metric has two free functions of $(t, r)$.
   - *Why needed:* Sets up the problem.

2. **Compute Ricci tensor components** for the ansatz. Specifically, identify $R_{tr}$, $R_{tt}$, $R_{rr}$, $R_{\theta\theta} = R_{\phi\phi}/\sin^2\theta$.
   - *Hint:* Use Cartan structural equations or direct computation; this is mechanical but lengthy.
   - *Why needed:* Provides the field equations for the ansatz.

3. **Off-diagonal equation $R_{tr} = 0$ implies $\partial_t \lambda = 0$.**
   - *Hint:* $R_{tr} = -\frac{2}{r}\partial_t\lambda$ in this ansatz (computation).
   - *Why needed:* Kills time-dependence of $\lambda$.

4. **Diagonal combination gives $\partial_r(\nu + \lambda) = 0$.**
   - *Hint:* Take a suitable combination of $R_{tt} = 0$ and $R_{rr} = 0$ (e.g., $e^{-2\nu} R_{tt} + e^{-2\lambda} R_{rr}$) to isolate the gradient of $\nu + \lambda$.
   - *Why needed:* Constrains $\nu(t, r)$ to be $\nu(t, r) = -\lambda(r) + f(t)$.

5. **Reparametrise $t$ to kill $f(t)$.** The substitution $\tilde t = \int e^{f(t)/2}\, dt$ makes $e^{2\nu} \to e^{-2\lambda(r)}$.
   - *Hint:* Just calculus — choose the new time coordinate so the metric coefficient is $-(1 - 2M/r)$.
   - *Why needed:* Cleans up the metric to standard Schwarzschild form.

6. **Solve the remaining ODE for $\lambda(r)$.** The remaining vacuum equation (any of $R_{\theta\theta} = 0$ or $R_{rr} = 0$) is $\frac{d}{dr}(r e^{-2\lambda}) = 1$, integrating to $e^{-2\lambda} = 1 - 2M/r$.
   - *Hint:* This is a first-order linear ODE.
   - *Why needed:* Gives the explicit Schwarzschild form.

7. **Identify $M$ as the mass parameter** via the Newtonian limit (or via the ADM mass at infinity).

---

# Lemma Decomposition

> [!note]- Lemma 1: General spherically symmetric metric ansatz
> **Statement:** The most general spherically symmetric Lorentzian metric in 4D, after coordinate adaptation, takes the form
> $$ds^2 = -e^{2\nu(t, r)} dt^2 + e^{2\lambda(t, r)} dr^2 + r^2 d\Omega^2.$$
>
> **Hint:** Spherical symmetry means there is an $SO(3)$ isometry group whose orbits are spacelike 2-spheres. Adapt coordinates so the angular part is the standard round 2-sphere $r^2 d\Omega^2$ with $r$ the areal radius. The remaining metric is on the $(t, r)$ plane with two free functions; the $g_{tr}$ component can be killed by a coordinate change $t \to t + f(r)$.
>
> **Why needed:** Sets up the problem with explicit metric components.
>
> > [!note]- Full proof
> > Standard manipulation. The $SO(3)$ orbits are 2-spheres, and the metric restricted to each orbit is a constant multiple of the standard round metric $r^2 d\Omega^2$; the constant defines the areal radius $r$. The orthogonal (Lorentzian) 2-plane has coordinates $(t, r)$, with the metric being a general Lorentzian 2-metric $g_{tt}(t, r) dt^2 + 2g_{tr} dt\, dr + g_{rr} dr^2$. By choosing coordinates so that $g_{tr} = 0$ (possible by a coordinate change in the $(t, r)$ plane), one gets the stated form, with $e^{2\nu}$ and $e^{2\lambda}$ positive (Lorentzian signature requires $g_{tt} < 0, g_{rr} > 0$).

> [!note]- Lemma 2: $R_{tr} = 0$ implies $\lambda = \lambda(r)$
> **Statement:** Computing the Ricci tensor of the ansatz, $R_{tr} = -(2/r) \partial_t \lambda$. Vanishing requires $\partial_t \lambda = 0$, so $\lambda$ depends only on $r$.
>
> **Hint:** Direct computation using Cartan's structural equations or Christoffel symbols. The cross-component $R_{tr}$ is the most rapidly vanishing component, and is exactly proportional to $\partial_t \lambda$.
>
> **Why needed:** First step of killing time-dependence.
>
> > [!note]- Full proof
> > Using the orthonormal coframe $\theta^0 = e^\nu dt$, $\theta^1 = e^\lambda dr$, $\theta^2 = r d\theta$, $\theta^3 = r\sin\theta d\phi$, compute the connection 1-forms via $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ and $\omega_{ab} = -\omega_{ba}$. The off-diagonal mixed-time-radial Ricci component comes from the curvature 2-form $\Omega^0{}_1 = d\omega^0{}_1 + \omega^0{}_c \wedge \omega^c{}_1$, contributing the term $-(2/r)\partial_t\lambda$. (Details in Frankel §11.5 or Wald §6.1.) Setting $R_{tr} = 0$ forces $\partial_t\lambda = 0$.

> [!note]- Lemma 3: $R_{tt} + e^{2(\lambda - \nu)} R_{rr} = 0$ implies $\partial_r(\nu + \lambda) = 0$
> **Statement:** A combination of the diagonal $tt$ and $rr$ Ricci components, set equal to zero, yields $\partial_r(\nu + \lambda) = 0$, hence $\nu(t, r) + \lambda(r) = f(t)$ for some function $f$ of $t$ alone.
>
> **Hint:** The diagonal Ricci components contain terms $\partial_r \nu, \partial_r \lambda$ explicitly. Take a linear combination to eliminate the curvature terms and isolate the gradient.
>
> **Why needed:** Constrains $\nu$ given $\lambda(r)$.
>
> > [!note]- Full proof
> > Direct computation. The components are $R_{tt} = e^{2\nu}[\partial_r^2\nu + (\partial_r\nu)^2 - \partial_r\nu \partial_r\lambda + (2/r)\partial_r\nu]$ and $R_{rr} = -[\partial_r^2\nu + (\partial_r\nu)^2 - \partial_r\nu \partial_r\lambda - (2/r)\partial_r\lambda]$. Setting $R_{tt} + e^{2(\lambda-\nu)} R_{rr} = 0$ (an algebraic combination), the second-derivative terms and the squared-first-derivative terms cancel, leaving $(2/r)(\partial_r\nu + \partial_r\lambda) = 0$, hence $\partial_r(\nu + \lambda) = 0$.

> [!note]- Lemma 4: Reparametrising $t$ to standardise the metric
> **Statement:** The residual function $f(t) = \nu(t, r) + \lambda(r)$ can be absorbed by a redefinition of the time coordinate $\tilde t = \int e^{f(t)/2}\, dt$, after which $\nu = -\lambda(r)$.
>
> **Hint:** Under $t \to \tilde t = \int e^{f/2} dt$, $d\tilde t = e^{f/2} dt$, so $-e^{2\nu} dt^2 = -e^{2\nu - f} d\tilde t^2 = -e^{-2\lambda} d\tilde t^2$.
>
> **Why needed:** Makes the metric coefficients depend only on $r$ — the final static form.
>
> > [!note]- Full proof
> > Direct calculation. After the substitution, $g_{\tilde t\tilde t} = -e^{2\nu(t, r)}\cdot (dt/d\tilde t)^2 = -e^{2\nu - f(t)} = -e^{-2\lambda(r)}$, depending only on $r$.

> [!note]- Lemma 5: Solving the ODE
> **Statement:** With $\nu = -\lambda(r)$, the remaining vacuum Einstein equation (e.g., $R_{\theta\theta} = 0$) reduces to $\frac{d}{dr}(r e^{-2\lambda}) = 1$, with the integral $e^{-2\lambda} = 1 - 2M/r$ for an integration constant $M$.
>
> **Hint:** Direct integration of a first-order linear ODE.
>
> **Why needed:** Final form of the Schwarzschild metric.
>
> > [!note]- Full proof
> > Compute $R_{\theta\theta}$ with $\nu = -\lambda(r)$: $R_{\theta\theta} = 1 - e^{-2\lambda}(1 - 2r\partial_r\lambda) = 1 - e^{-2\lambda} - r\partial_r(e^{-2\lambda})$. Setting this to zero: $r\partial_r(e^{-2\lambda}) + e^{-2\lambda} = 1$, i.e., $\frac{d}{dr}(r e^{-2\lambda}) = 1$. Integrating: $r e^{-2\lambda} = r - 2M$ for an integration constant $-2M$, hence $e^{-2\lambda} = 1 - 2M/r$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0** (setup): Assume $(M, g)$ is a Lorentzian 4-manifold with spherical symmetry — an isometric $SO(3)$ action whose orbits are spacelike 2-spheres. Adapt local coordinates so the orbits are coordinate spheres, $r$ is the areal radius, $g_{tr} = 0$, and the metric takes the form (Lemma 1):
> $$ds^2 = -e^{2\nu(t, r)} dt^2 + e^{2\lambda(t, r)} dr^2 + r^2 d\Omega^2.$$
>
> **Step 1** (off-diagonal equation): Compute $R_{tr}$. By Lemma 2, $R_{tr} = -(2/r)\partial_t\lambda$. The vacuum equation $R_{tr} = 0$ implies $\partial_t\lambda = 0$, so $\lambda = \lambda(r)$.
>
> **Step 2** (diagonal combination): By Lemma 3, the combination $R_{tt} + e^{2(\lambda - \nu)} R_{rr} = (2/r)\partial_r(\nu + \lambda)$. Vanishing gives $\partial_r(\nu + \lambda) = 0$, so $\nu(t, r) + \lambda(r) = f(t)$ for some $f$.
>
> **Step 3** (coordinate adaptation): By Lemma 4, redefine $t \to \tilde t = \int e^{f(t)/2}\, dt$ to absorb $f$. The metric becomes (renaming $\tilde t \to t$):
> $$ds^2 = -e^{-2\lambda(r)} dt^2 + e^{2\lambda(r)} dr^2 + r^2 d\Omega^2.$$
> This is now static.
>
> **Step 4** (radial ODE): By Lemma 5, the remaining equation $R_{\theta\theta} = 0$ becomes $\frac{d}{dr}(r e^{-2\lambda}) = 1$, integrating to
> $$e^{-2\lambda(r)} = 1 - \frac{2M}{r},$$
> for an integration constant $M$.
>
> **Step 5** (identification): The metric is
> $$ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2 d\Omega^2,$$
> the Schwarzschild metric. The constant $M$ is identified as the gravitational mass parameter via the asymptotic ($r \to \infty$) Newtonian limit (where $g_{tt} \approx -(1 + 2\phi)$ with $\phi = -M/r$ the Newtonian potential of a point mass $M$).
>
> The argument is *local*: it establishes local isometry to Schwarzschild in a neighbourhood of any point. Global topology may differ (e.g., quotient identifications giving different global spacetimes).
>
> $\square$

---

# Cross-Field Exercise Suggestions

**Application 1: Spherical gravitational collapse.** Consider a spherical star collapsing into a black hole. By Birkhoff's theorem, the exterior metric throughout the collapse is *exactly* the static Schwarzschild metric — no time-dependence in the exterior. So an observer outside the star sees the same gravity throughout the collapse, with only the location of the surface changing. No gravitational radiation is emitted by the spherical collapse — the first detectable gravitational radiation comes only from deviations from spherical symmetry.

**Application 2: Spherical EM field — Reissner–Nordström.** The Einstein–Maxwell equations with a spherically symmetric electromagnetic source yield the **Reissner–Nordström metric** $ds^2 = -(1 - 2M/r + Q^2/r^2) dt^2 + (\ldots)^{-1} dr^2 + r^2 d\Omega^2$ with $A = (Q/r) dt$. This is the EM-generalisation of Birkhoff (Birkhoff–Hoffmann): the unique spherical solution of Einstein–Maxwell vacuum (no other matter, but with EM field) is Reissner–Nordström, characterised by mass $M$ and charge $Q$.

**Application 3: Higher dimensions.** The higher-dimensional Schwarzschild solution (Tangherlini, 1963) in $D$ dimensions is $g_{tt} = -(1 - r_s^{D-3}/r^{D-3})$, $g_{rr} = -(g_{tt})^{-1}$, with $d\Omega^2_{D-2}$ the metric on the unit $(D-2)$-sphere. Birkhoff's theorem holds in higher dimensions: spherical symmetry in vacuum forces this solution.

**Application 4: Cosmological perturbations.** When studying small-scale density perturbations in cosmology, the spherical-perturbation regime is governed by Birkhoff-type reasoning: the exterior of a spherical overdensity behaves like Schwarzschild, with $M$ being the enclosed mass. This is the GR justification for treating small-scale clustering "Newtonianly" — the spherical exterior is just Schwarzschild around the enclosed mass.

---

# Bridges

- **[[Thm - Schwarzschild Solution]]** — Birkhoff's theorem is the *uniqueness* counterpart of Schwarzschild's derivation: Schwarzschild constructs the metric assuming staticness and spherical symmetry; Birkhoff shows that even without assuming staticness, the vacuum equations force it. So Birkhoff + Schwarzschild together give: spherically symmetric vacuum implies static, and static + spherically symmetric vacuum gives the Schwarzschild metric uniquely (up to the mass parameter).

- **Newton's shell theorem** — In Newtonian gravity, the field of a spherically symmetric mass distribution outside the source equals that of a point mass; inside a spherical shell, the field vanishes. Birkhoff's theorem is the GR generalisation, with an added bonus: not only is the field uniquely determined by the total mass, but the *spacetime metric* is exactly Schwarzschild (not just approximately), and the interior of a shell is genuinely flat Minkowski. The Newtonian theorem is a corollary of Birkhoff in the weak-field limit.

- **Quadrupole formula for gravitational waves** — Birkhoff's theorem implies no monopole gravitational radiation; the lowest radiating multipole is the quadrupole. Combined with the linearised theory, this gives **Einstein's quadrupole formula** $\dot E_\text{GW} = (G/5c^5)\langle \dddot{Q}_{\mu\nu}\dddot{Q}^{\mu\nu}\rangle$ for the gravitational wave luminosity, with $Q_{\mu\nu}$ the mass quadrupole moment of the source. The formula vanishes identically for any spherical source — direct verification of Birkhoff's no-radiation prediction.

- **No-hair theorems** — Birkhoff is the spherical case of a more general uniqueness theorem for black holes. The **no-hair theorem** (Israel–Carter–Robinson–Hawking, 1967–1972) asserts that the unique stationary axially symmetric vacuum black hole is **Kerr** (mass and angular momentum), and the unique stationary axially symmetric Einstein–Maxwell black hole is **Kerr–Newman** (mass, angular momentum, charge). Birkhoff is the spherical, vacuum case of this hierarchy: spherical symmetry forces vanishing angular momentum and gives Schwarzschild.

---

# Unlocked by This

> [!tip] No Monopole Gravitational Radiation *(from Gravitational Wave Theory)*
> Birkhoff's theorem implies that gravitational radiation has lowest multipole $\ell = 2$ (quadrupole) — there is no monopole ($\ell = 0$) or dipole ($\ell = 1$) gravitational radiation. The monopole vanishes by Birkhoff; the dipole vanishes by momentum conservation (the dipole is the position of the centre of mass, which moves uniformly in vacuum). This is the structural reason why **LIGO** sees gravitational waves only from highly asymmetric sources (binary inspirals, asymmetric supernovae) and not from radial pulsations.

> [!tip] Gravitational Collapse to a Black Hole *(from Black Hole Formation)*
> In Oppenheimer–Snyder (1939) spherical collapse, a uniform-density spherical dust ball collapses to a black hole. By Birkhoff's theorem, the exterior is always Schwarzschild, and the only thing that changes is the position of the matter surface. An external observer sees the surface asymptotically approach the Schwarzschild radius $r_s = 2M$ but never quite reach it (in Schwarzschild coordinates) — though crossing happens in finite proper time for the infalling matter. This is the simplest model of black hole formation, and its remarkably clean structure follows from Birkhoff's theorem.

> [!tip] Reissner–Nordström and Birkhoff–Hoffmann *(from Charged Black Holes)*
> The Einstein–Maxwell version of Birkhoff: any spherically symmetric solution of Einstein–Maxwell vacuum (no other matter, just EM field plus gravity) is necessarily static and equals **Reissner–Nordström** with mass $M$ and charge $Q$. The proof is analogous to Birkhoff for vacuum, with the additional Maxwell equations restricting the EM field. The resulting charged black hole has two horizons (outer and inner) when $|Q| < M$ and a *naked* singularity for $|Q| > M$ (excluded by the **cosmic censorship conjecture**).

> [!tip] Vaidya Metric — Beyond Birkhoff *(from Time-Dependent Spherical Solutions)*
> The **Vaidya metric** describes a spherically symmetric *radiating* spacetime — a spherical body emitting or absorbing null radiation (light). It is *not* vacuum (there is null matter throughout) and therefore Birkhoff's theorem does not apply directly. The Vaidya solution generalises Schwarzschild to time-dependent mass $M(v)$, where $v$ is an outgoing null coordinate. It is used to model **Hawking radiation** (a slowly-evaporating black hole) and accretion onto compact objects.

> [!tip] Lemaître–Tolman–Bondi Spacetimes *(from Cosmology and Spherical Inhomogeneity)*
> The **LTB metrics** describe spherically symmetric *dust* distributions (perfect fluid with $p = 0$) — generalisations of Schwarzschild and FLRW for arbitrary spherical inhomogeneity in a dust universe. Birkhoff's theorem applies to the *exterior vacuum* surrounding each spherical shell, but the LTB metric describes the matter-filled interior. Used to model spherical collapse, cosmological voids, and density perturbations in inhomogeneous cosmology.
