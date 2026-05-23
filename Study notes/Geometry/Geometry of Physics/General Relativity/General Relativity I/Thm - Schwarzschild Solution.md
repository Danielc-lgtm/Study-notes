---
type: theorem
subject: general-relativity
prereqs:
  - "Def - The Schwarzschild Metric"
  - "Def - The Einstein Field Equations"
  - "Thm - Birkhoff's Theorem"
tags: [physics, general-relativity, exact-solutions, black-holes, flagship]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$, geometrised units $c = G = 1$. Spherical coordinates $(t, r, \theta, \phi)$ with $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2$. Spherically symmetric *static* ansatz: $ds^2 = -e^{2\Phi(r)} dt^2 + e^{2\Lambda(r)} dr^2 + r^2 d\Omega^2$, with $\Phi(r)$ and $\Lambda(r)$ two unknown functions to be determined. Full registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Statement

> **Theorem (Schwarzschild, 1916).** The unique spherically symmetric, static, asymptotically flat vacuum solution of the Einstein field equations $R_{\mu\nu} = 0$ in four spacetime [[Def - Dimension|dimensions]] is the **Schwarzschild metric**:
> $$ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2\, d\theta^2 + r^2 \sin^2\theta\, d\phi^2,$$
> where $M$ is an integration constant (the **mass parameter**, equal to the gravitational mass of the source in geometrised units; in conventional units, $M$ has dimensions of mass and the appearance is $g_{tt} = -(1 - 2GM/(rc^2))$). The metric is valid in the exterior region $r > 2M$; the surface $r = 2M$ is the **Schwarzschild radius** (a coordinate singularity, not a curvature singularity), and $r = 0$ is a genuine curvature singularity inside.
>
> The identification of $M$ with the gravitational mass is fixed by the weak-field limit: $g_{tt} \to -(1 + 2\phi)$ with $\phi = -M/r$, matching the Newtonian potential of a point mass $M$.
>
> *Corollary (with Birkhoff's theorem)*. The Schwarzschild metric is also the unique spherically symmetric vacuum solution, *without* assuming staticness: spherical symmetry plus vacuum forces staticness automatically.

---

# Motivation

The Schwarzschild solution is the first and most fundamental exact solution of the Einstein field equations. It describes the gravitational field outside an isolated, non-rotating, spherically symmetric mass — the geometry around the Sun, around the Earth (to leading order), around a non-rotating neutron star, and around a non-rotating black hole. Karl Schwarzschild found it in late 1915 (published 1916), while serving in the German army on the Eastern Front during WWI, less than two months after Einstein published the field equations. Schwarzschild died of a disease contracted at the front a few months later; his solution lived on.

The importance of the Schwarzschild solution is fourfold:

(i) **It is the GR replacement for Newton's $\phi = -GM/r$**. In the weak-field, slow-motion limit, [[Def - Geodesic|geodesics]] in the Schwarzschild geometry reduce to Newtonian orbits in the inverse-square gravity of a point mass. So the Schwarzschild metric *is* what Newton's potential becomes when you take general relativity seriously.

(ii) **It is the testing ground of GR**. The three "classical tests" of GR — perihelion precession of Mercury, light bending by the Sun, gravitational redshift — are all calculations of geodesics in the Schwarzschild metric outside the Sun. All three give predictions that disagree with Newtonian gravity by definite, computable amounts, and all three have been verified observationally.

(iii) **It is the simplest black hole**. The Schwarzschild metric has an event horizon at $r = 2M$ and a curvature singularity at $r = 0$, providing the simplest model of a black hole. Most of the conceptual understanding of black holes — event horizons, the Penrose diagram, time-dilation near the horizon, the inevitability of singularities — is developed first in the Schwarzschild context.

(iv) **It is the unique solution under the natural symmetries**. By **Birkhoff's theorem**, *any* spherically symmetric vacuum spacetime is the Schwarzschild metric — without assuming staticness! This makes Schwarzschild a structural feature of GR with spherical symmetry, not just one possible solution among many.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source B₁: Vacuum Einstein equations with maximal symmetry.* When one is solving the field equations with high symmetry (spherical, axial, etc.), the system reduces from PDEs to ODEs, allowing explicit integration. Schwarzschild is the spherical-symmetry case. *Example problem*: derive the gravitational field outside any spherically symmetric source — by Birkhoff, it is necessarily Schwarzschild.

*Source B₂: Black hole final-state result.* By the **no-hair theorem**, the most general stationary vacuum black hole is **Kerr** (mass and angular momentum). Schwarzschild is the $J = 0$ limit. So Schwarzschild is the late-time attractor of any non-rotating gravitational collapse. *Bridge argument*: spherical collapse → spherical exterior (Birkhoff) → Schwarzschild; the *final* state of any collapse to a non-rotating black hole is Schwarzschild. *Example problem*: an asymmetric collapse to a non-rotating black hole settles down to Schwarzschild + small ringdown modes that decay.

*Source B₃: Static spherically symmetric body.* In any practical astrophysical scenario with a roughly spherical, slowly-rotating body — the Sun, Earth, neutron stars — the exterior gravity is well-approximated by Schwarzschild, with corrections from rotation (Kerr) and asymmetry (multipole expansion). *Bridge argument*: at leading order, the body is spherical, and the exterior is Schwarzschild; higher-order asymmetries give corrections (frame dragging $\propto J/r^2$, quadrupole moment $\propto Q_2/r^3$, etc.). *Example problem*: the orbit of Mercury in the gravitational field of the Sun is, to excellent approximation, a geodesic in the Schwarzschild metric of the Sun's mass — yielding the 43"/century perihelion precession.

**Targets (Output Amplification).**

*Target T₁: Perihelion precession.* Computing timelike geodesics in the Schwarzschild metric and identifying their non-closed nature gives the **precession of perihelion**: each orbit advances by an angle $\Delta\phi = 6\pi M/[a(1 - e^2)]$ per period, where $a$ is the semi-major axis and $e$ the eccentricity. For Mercury ($a \approx 5.8 \times 10^7$ km, $e \approx 0.21$, $M = M_\odot \approx 1.5$ km), this gives $\approx 43''$/century — the long-standing anomaly resolved by GR.

*Target T₂: Light bending around the Sun.* Null geodesics passing near a mass $M$ at impact parameter $b$ are deflected by an angle $\Delta\phi = 4M/b$. For a grazing ray ($b = R_\odot$) past the Sun, $\Delta\phi \approx 1.75''$ — confirmed by Eddington's 1919 eclipse expedition. Newton's prediction (treating light as a slow particle with $v = c$) is half this value. The factor of 2 is the contribution of the spatial $g_{rr}$ component.

*Target T₃: Gravitational redshift.* A clock at radius $r$ in the Schwarzschild geometry runs at rate $d\tau = \sqrt{1 - 2M/r}\, dt$ compared to an asymptotic clock at infinity. A photon emitted at $r_e$ with frequency $\nu_e$ is observed at $r_o$ with frequency $\nu_o = \nu_e \sqrt{(1 - 2M/r_e)/(1 - 2M/r_o)}$. The **Pound–Rebka experiment** (1959) measured this redshift over a 22.5 m tower.

*Target T₄: Innermost stable circular orbit (ISCO).* The effective radial potential for timelike circular orbits in Schwarzschild has its minimum at $r = 6M$ — below this, no stable circular orbits exist. This is the inner edge of accretion disks around Schwarzschild black holes; matter spirals in from $r_\text{ISCO} = 6M$ to the horizon at $r_s = 2M$.

---

# Why Is It True

**The mechanism in one sentence: the spherically symmetric static vacuum metric has *two* unknown functions $\Phi(r)$ and $\Lambda(r)$ (functions of one variable $r$), and the *two* independent equations $R_{tt} = 0$ and $R_{rr} = 0$ from the vacuum Einstein equations integrate to the single-parameter Schwarzschild family.**

Concretely: the ansatz $ds^2 = -e^{2\Phi(r)} dt^2 + e^{2\Lambda(r)} dr^2 + r^2 d\Omega^2$ has two functions of $r$. The vacuum equations $R_{\mu\nu} = 0$ have multiple components, but most are automatically equivalent (by symmetry or by the Bianchi identity, which reduces 10 equations to 6 independent ones, and 6 to fewer under spherical symmetry). In fact, for the spherical-static ansatz, the field equations reduce to two ODEs:

- $G_{tt} = 0$: $\frac{d}{dr}\left[r(1 - e^{-2\Lambda})\right] = 0$.
- $G_{rr} = 0$: $r e^{-2\Lambda}(2\Phi' + 1/r) = 1$ (where $' = d/dr$).
- $G_{\theta\theta} = 0$: a consequence of the others by Bianchi (so no new information).

The first equation integrates immediately: $r(1 - e^{-2\Lambda}) = 2M$ for some integration constant $M$. Hence
$$e^{-2\Lambda} = 1 - \frac{2M}{r}.$$
Substituting into the second equation:
$$\left(1 - \frac{2M}{r}\right)\left(2\Phi' + \frac{1}{r}\right) = \frac{1}{r},$$
giving $2\Phi' = \frac{1}{r}\left[\frac{1}{1 - 2M/r} - 1\right] = \frac{2M/r^2}{1 - 2M/r}$. Integrating:
$$\Phi(r) = \frac{1}{2}\ln(1 - 2M/r) + \text{const}.$$
The constant is absorbed by rescaling $t$, so $\Phi(r) = \frac{1}{2}\ln(1 - 2M/r)$, hence $e^{2\Phi} = 1 - 2M/r$.

So $g_{tt} = -(1 - 2M/r)$ and $g_{rr} = (1 - 2M/r)^{-1}$ — the Schwarzschild metric.

**Why is this so clean?** Two reasons. First, spherical symmetry reduces the metric to two free functions of one variable, making it tractable. Second, the vacuum equations have just enough structure to fix these two functions uniquely (up to one integration constant, $M$) — neither over-determining nor under-determining the system. This is a generic feature of vacuum solutions with high symmetry: the system simplifies to an integrable ODE.

**The identification of $M$ with mass.** The integration constant $M$ that emerges from the ODE has no intrinsic meaning at this stage — it is just a number labelling the solution. Its physical interpretation as the gravitational mass comes from the Newtonian limit: $g_{tt} \approx -(1 - 2M/r) \approx -(1 + 2\phi)$ identifies $\phi = -M/r$ as the Newtonian gravitational potential of a point mass $M$. Equivalently, using the **ADM mass** definition at spatial infinity (a surface integral of the metric and its derivatives), one verifies that the asymptotic mass of the Schwarzschild spacetime equals $M$.

---

# What Makes This Hard

The technical difficulty is the computation of the Ricci tensor for the static spherical ansatz — algebraically straightforward but tedious. Using the orthonormal coframe (Cartan's structural equations) makes it cleaner: compute the connection 1-forms from $de^a + \omega^a{}_b \wedge e^b = 0$, then curvature 2-forms from $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$, then $R^a{}_{bcd}$ from the components of $\Omega^a{}_b$.

A common error is to assume staticness from the start without invoking Birkhoff — this is legitimate but conceals the deeper fact that staticness is *forced* by vacuum plus spherical symmetry (Birkhoff's theorem). Another common error is to forget that the coordinate $r$ is the *areal* radius (defined by the sphere $r$ having area $4\pi r^2$), not the proper radial distance. Using $r$ as proper distance gives a different parameterisation of the same geometry (the "isotropic coordinates") but the explicit form looks different.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Take the spherically symmetric static ansatz with two free radial functions. Compute the Einstein tensor components $G_{\mu\nu}$. Set them to zero and solve the resulting ODEs. The two independent equations give one equation for $\Lambda(r)$ (integrating immediately) and one for $\Phi(r)$ (integrating after substituting $\Lambda$). The result has one integration constant, identified with mass by the Newtonian limit.

**Subgoal decomposition:**

1. **Compute Einstein tensor components** for the static spherical ansatz.
   - *Hint:* Use Cartan's structural equations with the orthonormal coframe $\theta^0 = e^\Phi dt$, $\theta^1 = e^\Lambda dr$, $\theta^2 = r d\theta$, $\theta^3 = r\sin\theta d\phi$.
   - *Why needed:* Computes the LHS of the field equations.

2. **Solve $G_{tt} = 0$ for $\Lambda(r)$:** integrates to $e^{-2\Lambda} = 1 - 2M/r$ for an integration constant $M$.
   - *Hint:* $G_{tt}$ involves only $\Lambda$ and its derivative; the equation is first-order.
   - *Why needed:* Half of the Schwarzschild metric.

3. **Solve $G_{rr} = 0$ for $\Phi(r)$:** with $\Lambda$ known, integrates to $e^{2\Phi} = 1 - 2M/r$.
   - *Hint:* Substituting $\Lambda$ from Step 2 simplifies the equation; the second integration constant is absorbed by rescaling $t$.
   - *Why needed:* The other half.

4. **Verify $G_{\theta\theta} = 0$** holds automatically (consequence of Bianchi).
   - *Hint:* Direct computation, or invoke Bianchi identity.
   - *Why needed:* Confirms consistency.

5. **Identify $M$ as mass via Newtonian limit:** in the weak-field limit, $g_{tt} \to -(1 - 2M/r) \approx -(1 + 2\phi)$ with $\phi = -M/r$ — identifying $M$ as the gravitational mass of the central body.

---

# Lemma Decomposition

> [!note]- Lemma 1: Einstein tensor for spherical static ansatz
> **Statement:** For the metric $ds^2 = -e^{2\Phi(r)} dt^2 + e^{2\Lambda(r)} dr^2 + r^2 d\Omega^2$ with $\Phi, \Lambda$ functions of $r$ alone, the non-trivial Einstein-tensor components in the orthonormal frame are:
> $$G_{tt} = \frac{1}{r^2}\left[1 - \frac{d}{dr}(r e^{-2\Lambda})\right], \quad G_{rr} = \frac{1}{r^2}\left[2r e^{-2\Lambda} \Phi' + e^{-2\Lambda} - 1\right],$$
> with $G_{\theta\theta} = G_{\phi\phi}/\sin^2\theta$ a consequence of these via Bianchi.
>
> **Hint:** Use Cartan's structural equations: orthonormal coframe $\theta^0 = e^\Phi dt, \theta^1 = e^\Lambda dr, \theta^2 = r d\theta, \theta^3 = r\sin\theta d\phi$; solve $d\theta^a + \omega^a{}_b\wedge \theta^b = 0$ for the connection 1-forms (six unknowns, six equations); compute curvature 2-forms $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c\wedge\omega^c{}_b$; read off Riemann components and contract.
>
> **Why needed:** Provides the field equations as ODEs.
>
> > [!note]- Full proof
> > The connection 1-forms turn out to be $\omega^0{}_1 = \Phi' e^{\Phi - \Lambda} dt$, $\omega^2{}_1 = -e^{-\Lambda} d\theta$, $\omega^3{}_1 = -\sin\theta e^{-\Lambda} d\phi$, $\omega^3{}_2 = -\cos\theta d\phi$ (others zero by isotropy). The curvature 2-forms then give Riemann components like $R^{01}{}_{01} = -e^{-2\Lambda}[\Phi'' + (\Phi')^2 - \Phi'\Lambda']$, $R^{02}{}_{02} = -e^{-2\Lambda}\Phi'/r$, $R^{12}{}_{12} = -e^{-2\Lambda}\Lambda'/r$, $R^{23}{}_{23} = (1 - e^{-2\Lambda})/r^2$. Contracting and gathering gives the stated Einstein tensor components. Standard computation, in any GR text (e.g., Wald §6.1, Carroll §5.2). The detailed derivation is in [[Ex - Computing the Ricci Tensor of the Schwarzschild Metric]].

> [!note]- Lemma 2: First ODE — solving for $\Lambda(r)$
> **Statement:** $G_{tt} = 0$ implies $r(1 - e^{-2\Lambda}) = 2M$ for an integration constant $M$, i.e., $e^{-2\Lambda} = 1 - 2M/r$.
>
> **Hint:** $G_{tt} = (1/r^2)[1 - (d/dr)(re^{-2\Lambda})] = 0$ gives $(d/dr)(re^{-2\Lambda}) = 1$, integrating to $re^{-2\Lambda} = r + \text{const}$.
>
> **Why needed:** Provides $\Lambda(r)$ and hence $g_{rr}$.
>
> > [!note]- Full proof
> > From Lemma 1: $G_{tt} = (1/r^2)[1 - (d/dr)(r e^{-2\Lambda})] = 0$. So $(d/dr)(r e^{-2\Lambda}) = 1$, integrating to $r e^{-2\Lambda} = r - 2M$ for an integration constant $-2M$ (writing it as $-2M$ for later convenience). Hence $e^{-2\Lambda} = 1 - 2M/r$, equivalently $e^{2\Lambda} = (1 - 2M/r)^{-1}$.

> [!note]- Lemma 3: Second ODE — solving for $\Phi(r)$
> **Statement:** $G_{rr} = 0$, with $\Lambda$ from Lemma 2, implies $\Phi(r) = -\Lambda(r) +$ const, i.e., $e^{2\Phi} = 1 - 2M/r$ after absorbing the constant by rescaling $t$.
>
> **Hint:** Combine $G_{rr} = 0$ with the result of Lemma 2; the equation simplifies to $\Phi' + \Lambda' = 0$, integrating immediately.
>
> **Why needed:** Provides $\Phi(r)$ and hence $g_{tt}$.
>
> > [!note]- Full proof
> > From Lemma 1: $G_{rr} = (1/r^2)[2r e^{-2\Lambda}\Phi' + e^{-2\Lambda} - 1] = 0$. Using $e^{-2\Lambda} = 1 - 2M/r$: $G_{rr} = (1/r^2)[2r(1 - 2M/r)\Phi' + (1 - 2M/r) - 1] = (1/r^2)[2r(1 - 2M/r)\Phi' - 2M/r] = 0$. So $2r(1 - 2M/r)\Phi' = 2M/r$, hence $\Phi' = M/(r^2(1 - 2M/r))$. Integrating: $\Phi = -\frac{1}{2}\ln|1 - 2M/r| +$ const, after which choosing the constant by demanding $\Phi(r) \to 0$ as $r \to \infty$ (asymptotic flatness with standard time normalisation), $\Phi(r) = \frac{1}{2}\ln(1 - 2M/r)$, hence $e^{2\Phi} = 1 - 2M/r$ for $r > 2M$. Note that the sign of the constant is fixed by demanding $g_{tt} \to -1$ as $r \to \infty$, the asymptotic Minkowski form.

> [!note]- Lemma 4: Consistency check via $G_{\theta\theta} = 0$
> **Statement:** With $\Lambda, \Phi$ as above, $G_{\theta\theta} = 0$ automatically.
>
> **Hint:** Either compute directly (tedious) or invoke the contracted Bianchi identity: $\nabla^\mu G_{\mu\nu} = 0$, combined with $G_{tt} = G_{rr} = 0$, forces $G_{\theta\theta} = 0$.
>
> **Why needed:** Confirms the solution is consistent — no further constraints.
>
> > [!note]- Full proof
> > By the contracted Bianchi identity, $\nabla^\mu G_{\mu\nu} = 0$ identically. In the spherical static case, the four-divergence equations reduce to a single non-trivial equation relating $G_{tt}, G_{rr}, G_{\theta\theta}$. Setting $G_{tt} = G_{rr} = 0$ forces $G_{\theta\theta} = 0$ (one cannot have only some Einstein-tensor components vanish in a configuration with too much symmetry). Direct computation also confirms.

> [!note]- Lemma 5: Identification of $M$ as mass
> **Statement:** In the weak-field limit $r \gg M$, the Schwarzschild metric reduces to $g_{tt} \approx -(1 + 2\phi)$ with $\phi = -M/r$ — the Newtonian potential of a point mass $M$.
>
> **Hint:** Expand $g_{tt} = -(1 - 2M/r)$ around $M/r = 0$: $g_{tt} = -1 + 2M/r$. Compare with the weak-field form $g_{tt} = -(1 + 2\phi)$ to identify $\phi = -M/r$.
>
> **Why needed:** Gives the physical interpretation of the integration constant.
>
> > [!note]- Full proof
> > In the weak-field, slow-motion limit of GR, the geodesic equation reduces to $\ddot x^\alpha \approx -\partial^\alpha \phi$ with $g_{tt} = -(1 + 2\phi)$ (see [[Thm - Newtonian Limit of Einstein's Equations]]). Comparing with the Schwarzschild $g_{tt} = -(1 - 2M/r)$: $-(1 + 2\phi) = -(1 - 2M/r)$ gives $\phi = -M/r$, the Newtonian potential of a point mass $M$ at the origin. So $M$ is identified as the gravitational mass of the source.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0** (setup): Assume the spacetime is spherically symmetric, static, and asymptotically flat. Adopt coordinates $(t, r, \theta, \phi)$ with $r$ the areal radius, so the metric takes the ansatz
> $$ds^2 = -e^{2\Phi(r)} dt^2 + e^{2\Lambda(r)} dr^2 + r^2 d\Omega^2,$$
> with $\Phi, \Lambda$ functions of $r$ alone.
>
> **Step 1** (Einstein tensor): By Lemma 1, the non-trivial Einstein-tensor components are
> $$G_{tt} = \frac{1}{r^2}\left[1 - \frac{d}{dr}(r e^{-2\Lambda})\right], \quad G_{rr} = \frac{1}{r^2}\left[2r e^{-2\Lambda}\Phi' + e^{-2\Lambda} - 1\right].$$
>
> **Step 2** (solve for $\Lambda$): By Lemma 2, $G_{tt} = 0 \Rightarrow e^{-2\Lambda} = 1 - 2M/r$ for an integration constant $M$.
>
> **Step 3** (solve for $\Phi$): By Lemma 3, with $\Lambda$ from Step 2, $G_{rr} = 0 \Rightarrow e^{2\Phi} = 1 - 2M/r$ (after absorbing additive constant by $t$-rescaling).
>
> **Step 4** (consistency check): By Lemma 4, the remaining Einstein-tensor components $G_{\theta\theta}, G_{\phi\phi}$ vanish automatically (consequence of Bianchi).
>
> **Step 5** (Newtonian-limit identification): By Lemma 5, $M$ is identified with the gravitational mass of the source via the weak-field reduction $g_{tt} \to -(1 + 2\phi)$ with $\phi = -M/r$.
>
> **Conclusion**: The metric is
> $$ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2 d\Omega^2,$$
> the Schwarzschild metric, with $M$ the mass parameter. By Birkhoff's theorem (see [[Thm - Birkhoff's Theorem]]), the assumption of staticness is automatic from vacuum + spherical symmetry, so this is *the* unique spherically symmetric vacuum solution. $\square$

---

# Cross-Field Exercise Suggestions

**Application 1: Reissner–Nordström (charged) extension.** Repeat the derivation with the addition of an electromagnetic source: the ansatz includes a spherical electric field $E = Q/r^2$, the Einstein equations couple to Maxwell, and the joint solution is $g_{tt} = -(1 - 2M/r + Q^2/r^2)$, $g_{rr} = -(g_{tt})^{-1}$. The metric has two horizons (at $r_\pm = M \pm \sqrt{M^2 - Q^2}$) when $|Q| < M$, a naked singularity for $|Q| > M$.

**Application 2: Higher-dimensional Schwarzschild (Tangherlini, 1963).** Repeat in $D$ spacetime dimensions: the spherical ansatz has $(D-2)$-sphere angular part with metric $d\Omega^2_{D-2}$, and the vacuum equations give $g_{tt} = -(1 - r_s^{D-3}/r^{D-3})$, $g_{rr} = -(g_{tt})^{-1}$ where $r_s$ is the higher-dimensional Schwarzschild radius. The mass appears as $r_s^{D-3} \propto GM$.

**Application 3: Schwarzschild–de Sitter.** Repeat with cosmological constant $\Lambda > 0$: $g_{tt} = -(1 - 2M/r - \Lambda r^2/3)$, $g_{rr} = -(g_{tt})^{-1}$. Has two horizons: an inner black-hole horizon and an outer cosmological horizon. The two coincide at the **Nariai limit** $\Lambda M^2 = 1/9$.

**Application 4: Interior Schwarzschild — TOV equation.** Inside a spherically symmetric star with perfect-fluid matter, the field equations reduce to the **Tolman–Oppenheimer–Volkoff (TOV) equation** for the pressure $p(r)$ as a function of the energy density $\rho(r)$:
$$\frac{dp}{dr} = -\frac{(\rho + p)(M(r) + 4\pi r^3 p)}{r^2(1 - 2M(r)/r)},$$
where $M(r) = \int_0^r 4\pi r'^2 \rho(r')\, dr'$ is the mass enclosed within radius $r$. This is the relativistic equation of stellar structure, replacing Newton's $dp/dr = -\rho M(r)/r^2$.

---

# Bridges

- **[[Thm - Birkhoff's Theorem]]** — Birkhoff shows that the assumption of staticness in the Schwarzschild derivation is redundant: spherical symmetry plus vacuum *forces* staticness. So the unique spherical vacuum solution is Schwarzschild, period — not "Schwarzschild among many static spherical solutions". The proof of Birkhoff requires the time-dependent spherical ansatz; the simpler Schwarzschild derivation uses the static one directly, but Birkhoff confirms that no time-dependent solutions exist.

- **[[Def - The Schwarzschild Metric]]** — The theorem here derives the metric; the definition file describes its properties, coordinate systems, and physical interpretation. The two together give a complete picture of the Schwarzschild geometry.

- **[[Thm - Newtonian Limit of Einstein's Equations]]** — The identification of $M$ as the gravitational mass uses the Newtonian limit. In the weak-field, slow-motion regime, the Schwarzschild geodesic equation reduces to Newton's $\ddot x^\alpha = -\partial^\alpha \phi$ with $\phi = -M/r$, identifying $M$ as the Newtonian gravitating mass. This is the bridge between the GR exact solution and the Newtonian gravitational potential.

- **Kerr metric and the no-hair theorem** — The Schwarzschild solution is the $J = 0$ limit of the Kerr metric (rotating black hole). The **no-hair theorem** (Israel, Carter, Robinson, Hawking 1967–72) asserts: the unique stationary asymptotically flat vacuum black hole is Kerr; spherical (non-rotating) limit gives Schwarzschild. So Schwarzschild is the "simplest" black hole, characterised entirely by its mass.

- **AdS Schwarzschild** — In anti-de Sitter spacetime (negative $\Lambda$), the analogous spherical static vacuum solution is **Schwarzschild-AdS**: $g_{tt} = -(1 - 2M/r + r^2/L^2)$ where $L$ is the AdS radius. Used as the gravity dual of finite-temperature CFT states in **AdS/CFT correspondence**, with the black hole temperature corresponding to the CFT temperature.

---

# Unlocked by This

> [!tip] Classical Tests of GR *(from Observational GR)*
> The Schwarzschild solution is the testing ground for GR around the Sun. Computing geodesics in the Schwarzschild metric outside the Sun gives quantitative predictions for: **perihelion precession of Mercury** ($43''$/century), **light bending** by the Sun ($1.75''$ for grazing rays, twice the Newtonian-particle value), **gravitational redshift** (Pound–Rebka 1959). The agreement between these predictions and observation is one of the strongest pieces of evidence for GR.

> [!tip] Schwarzschild Black Holes and Event Horizons *(from Black Hole Physics)*
> The Schwarzschild radius $r_s = 2M$ defines the **event horizon** of a Schwarzschild black hole: a one-way membrane through which causal signals can enter but not exit. Inside, the singularity at $r = 0$ is unavoidable for all infalling worldlines. This is the simplest model of a black hole, and the structure (horizon, singularity, Penrose diagram) is the template for understanding all more general black-hole solutions.

> [!tip] Maximal Extension and Kruskal Coordinates *(from Mathematical GR)*
> The Schwarzschild metric in standard coordinates is only valid for $r > 2M$ (exterior region). The maximal analytic extension uses **Kruskal–Szekeres coordinates**, revealing the full structure: two asymptotically flat exterior regions (our universe and a parallel universe) connected by an **Einstein-Rosen bridge** (a wormhole), plus black-hole and white-hole interior regions. The Penrose diagram of the maximal extension is the iconic "hourglass" structure of black-hole geometry.

> [!tip] Hawking Radiation and Black Hole Thermodynamics *(from Quantum Gravity)*
> Quantum field theory in the Schwarzschild background predicts that the black hole emits thermal radiation at the **Hawking temperature** $T_H = \hbar/(8\pi M)$. The black hole has entropy $S_\text{BH} = A/(4 G\hbar) = 4\pi M^2/(G\hbar)$, formally identical to thermodynamic entropy. The discovery (Hawking 1974) suggests a deep connection between gravity, quantum mechanics, and thermodynamics — and is one of the central clues to quantum gravity.

> [!tip] Innermost Stable Circular Orbit and Accretion Disks *(from Astrophysics)*
> Circular orbits in Schwarzschild are stable only for $r > 6M$; below this, no stable circular orbits exist, and matter inevitably spirals into the black hole. The **ISCO** at $r_\text{ISCO} = 6M$ defines the inner edge of accretion disks around Schwarzschild black holes, where matter loses about 5.7% of its rest mass-energy as radiation before plunging in. This efficiency is what makes accreting black holes the brightest sources in the universe — far more efficient than nuclear fusion (0.7%) at converting mass to energy.

> [!tip] Schwarzschild ISCO and Photon Sphere as Astrophysical Targets *(from Black Hole Imaging)*
> The photon sphere of Schwarzschild ($r = 3M$, where light orbits in unstable circular orbits) is the boundary between captured and escaped light, defining the "shadow" cast by a black hole. The Event Horizon Telescope (2019, 2022) imaged the shadows of the supermassive black holes in M87 and Sgr A*, directly testing the Schwarzschild/Kerr geometry at the boundary of the photon sphere.
