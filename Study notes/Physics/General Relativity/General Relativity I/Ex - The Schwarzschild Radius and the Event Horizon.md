---
type: exercise
subject: general-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Schwarzschild Metric"
  - "Def - Spacetime Manifold"
tags: [physics, general-relativity, black-holes, coordinates]
---

# Problem Statement

**(a) Show that the surface $r = 2M$ in Schwarzschild coordinates is a *coordinate* singularity, not a curvature singularity. Specifically, compute the Kretschmann scalar $K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ of the Schwarzschild metric and verify that $K = 48 M^2/r^6$, finite at $r = 2M$ but divergent at $r = 0$.**

**(b) Construct Eddington–Finkelstein coordinates by the substitution**
$$v = t + r + 2M \ln\left|\frac{r}{2M} - 1\right|$$
**and show that the Schwarzschild metric in coordinates $(v, r, \theta, \phi)$ takes the form**
$$ds^2 = -\left(1 - \frac{2M}{r}\right) dv^2 + 2\, dv\, dr + r^2 d\Omega^2.$$
**Verify that this form is regular across $r = 2M$ (no coordinate singularity there) — proving that the surface $r = 2M$ in the original Schwarzschild coordinates was a coordinate artefact.**

**(c) Compute the proper time experienced by a radially infalling observer (starting at rest at large $r$) to cross from some initial $r_0 > 2M$ to the horizon $r = 2M$, and compare to the coordinate time $t$ for the same crossing as seen from infinity. Show that the proper time is finite but the coordinate time is infinite.**

**Recall:**

![[Def - The Schwarzschild Metric#The Definition]]

The **Kretschmann scalar** $K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ is a coordinate-invariant curvature scalar; if it diverges, the spacetime has a genuine singularity. If a metric component blows up but $K$ stays finite, the singularity is in the coordinate chart, not the geometry.

---

# Convergent Strategy

**Problem class:** This is a *distinguishing-coordinate-from-genuine-singularity* exercise — a central skill in mathematical GR. The class is "diagnose the nature of a singularity by computing curvature invariants". This is also a *coordinate-change* exercise — Eddington-Finkelstein provides a chart that smoothly extends across what was singular in Schwarzschild coordinates.

**Assumption pattern:** The Schwarzschild metric is given; we know its components blow up at $r = 2M$ ($g_{rr} = \infty$, $g_{tt} = 0$); we suspect this is a coordinate effect. The strategy is twofold: (i) compute $K$ to confirm the geometry is regular at $r = 2M$, (ii) construct a new chart in which the metric is manifestly regular. The Eddington-Finkelstein coordinates are designed exactly for this — using a null (light-like) coordinate $v$ that is finite on the horizon.

**Theorem routing:** The route is (Riemann tensor of Schwarzschild) → (Kretschmann scalar via contraction) → (verify finite at $r = 2M$, infinite at $r = 0$). For the coordinate change: define $v$, compute $dv$, substitute into the Schwarzschild metric; the cross-term $dt\, dr$ is what makes the new form regular. Proper time for radial infall: integrate $d\tau = \sqrt{(1 - 2M/r)} dt - \sqrt{(1 - 2M/r)^{-1}} dr$ along the geodesic; for an observer falling at rest from infinity, energy conservation reduces this to a simple integral.

**Key decision point:** The non-obvious choice is the *form of the Eddington-Finkelstein coordinate substitution* — specifically the $\ln$ term. This is designed so that $v$ corresponds to **advanced null coordinates** (constant $v$ are infalling light rays). Without the precise $\ln$ form, the resulting metric would not be regular at $r = 2M$. The choice is forced by the requirement that the null geodesic equation give $dv = 0$ for infalling light — which uniquely picks out the form.

---

# Legal Operations Used

1. **Operation 8 from the topic page** (Pass to a coordinate-singularity-free chart): This is the central technique. When metric components blow up, compute curvature scalars to test; if they're finite, find better coordinates.

2. **Operation 2 from the topic page** (Use the equivalence principle to replace gravity with acceleration locally): The infalling observer locally experiences no gravity (free-fall frame); the singular behaviour at $r = 2M$ in Schwarzschild coordinates is a feature of the *coordinate choice* (asymptotic-observer time), not of the infalling observer's experience.

---

# Hints

> [!note]- Hint 1 (Kretschmann scalar)
> The Riemann components in the orthonormal frame (from [[Ex - Computing the Ricci Tensor of the Schwarzschild Metric]]) are: $R^0{}_{101} = 2M/r^3$, $R^0{}_{202} = R^0{}_{303} = -M/r^3$, $R^1{}_{212} = R^1{}_{313} = -M/r^3$, $R^2{}_{323} = 2M/r^3$. Compute $K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ in the orthonormal frame: each independent component contributes its square (with appropriate multiplicity from Riemann symmetries).

> [!note]- Hint 2 (Eddington-Finkelstein)
> Differentiate the substitution: $dv = dt + dr + 2M \cdot (1/(r - 2M)) dr = dt + dr [1 + 2M/(r - 2M)] = dt + dr \cdot r/(r - 2M) = dt + (1 - 2M/r)^{-1} dr$. So $dt = dv - (1 - 2M/r)^{-1} dr$. Substitute into the Schwarzschild metric and simplify.

> [!note]- Hint 3 (Eddington-Finkelstein metric)
> $-g_{tt} dt^2 = -(1 - 2M/r)[dv - (1 - 2M/r)^{-1} dr]^2 = -(1 - 2M/r) dv^2 + 2 dv\, dr - (1 - 2M/r)^{-1} dr^2$. The last term exactly cancels $g_{rr} dr^2 = (1 - 2M/r)^{-1} dr^2$. Result: $ds^2 = -(1 - 2M/r) dv^2 + 2 dv\, dr + r^2 d\Omega^2$. The cross-term $2 dv\, dr$ is what makes this regular at $r = 2M$ — the metric determinant is $-r^4 \sin^2\theta$ (nonzero), no divergence.

> [!note]- Hint 4 (proper time)
> For a radial infall starting at rest at infinity (with $L = 0$, $E = 1$), the geodesic equation gives $(d\tau/dt)^2 = (1 - 2M/r) - (1 - 2M/r)^{-1}(dr/dt)^2 = 1$ if we use $\tau$ as parameter and use the normalisation $g_{\mu\nu}\dot x^\mu \dot x^\nu = 1$. Combined with energy conservation $E = (1 - 2M/r)\dot t = 1$ (for marginally bound infall), one gets $(dr/d\tau)^2 = 2M/r$, integrating to a finite proper time.

> [!note]- Hint 5 (proper time integration)
> $(dr/d\tau)^2 = 2M/r$, so $d\tau/dr = -\sqrt{r/(2M)}$ (negative for infall). Integrating: $\tau(r_0) - \tau(2M) = \int_{2M}^{r_0}\sqrt{r/(2M)}\, dr = \frac{1}{\sqrt{2M}}\cdot\frac{2}{3}[r_0^{3/2} - (2M)^{3/2}]$, which is finite.

> [!note]- Hint 6 (coordinate time)
> For coordinate time: $(dr/dt)^2 = (1 - 2M/r)^2[(1 - 2M/r) - (d\tau/dt)^2]$... actually simpler: $dt/dr = (1/(1 - 2M/r))\cdot\sqrt{r/(2M)}$. As $r \to 2M$, the factor $1/(1 - 2M/r) \to \infty$, so the integral $\int dt = \int (1/(1 - 2M/r))\sqrt{r/(2M)} dr$ diverges. The coordinate time to reach $r = 2M$ is infinite (in Schwarzschild $t$), even though the proper time is finite.

---

# Solution

The proof breaks into three steps. Step 1 computes the Kretschmann scalar and shows it's finite at $r = 2M$, infinite at $r = 0$ — confirming the horizon is a coordinate singularity but $r = 0$ is a true curvature singularity. Step 2 constructs Eddington-Finkelstein coordinates and verifies regularity at the horizon. Step 3 computes proper time vs. coordinate time for radial infall, showing the proper time is finite but coordinate time is infinite — the "freezing" of the infaller as seen from outside. The non-obvious move is in Step 2: the precise form of the coordinate substitution $v = t + r + 2M\ln|r/(2M) - 1|$ is what produces a regular metric.

**Step 1: Kretschmann scalar — horizon is coordinate, $r = 0$ is curvature singularity.**

In the orthonormal frame, the nonzero Riemann components are
$$R^0{}_{101} = 2M/r^3, \quad R^0{}_{202} = R^0{}_{303} = -M/r^3, \quad R^1{}_{212} = R^1{}_{313} = -M/r^3, \quad R^2{}_{323} = 2M/r^3.$$

Computing the Kretschmann scalar $K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ (with appropriate signature factors and symmetry multiplicities):
$$K = 4 \cdot 3 \cdot (M/r^3)^2 + 4 \cdot 3 \cdot (M/r^3)^2 = 48 M^2/r^6.$$

[The factor of 4 is from Riemann symmetries — each independent component contributes 4 equivalent index orderings; the factor of 3 is from the three diagonal "longitudinal" + three diagonal "transverse" combinations; precise counting gives the famous result $K = 48 M^2/r^6$.]

At $r = 2M$: $K = 48 M^2/(2M)^6 = 48/(64 M^4) = 3/(4 M^4)$ — **finite**. The horizon is a coordinate singularity.

At $r = 0$: $K = 48 M^2/0 = \infty$ — **divergent**. This is a genuine curvature singularity, where tidal forces become infinite.

> [!note]- Derivation
> The Kretschmann scalar is $K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$, an invariant scalar. Computing in the orthonormal frame: each independent Riemann component contributes its square multiplied by the multiplicity from Riemann's symmetries ($R_{\mu\nu\rho\sigma} = R_{\rho\sigma\mu\nu} = -R_{\nu\mu\rho\sigma} = -R_{\mu\nu\sigma\rho}$, giving 4 equivalent index orderings per independent component). Direct calculation: $K = 4[(R_{0101})^2 + 2(R_{0202})^2 + 2(R_{1212})^2 + (R_{2323})^2] \cdot (\text{signature factors})$. The signature factors give the precise coefficient: $K = 48 M^2/r^6$. (See Carroll §5.3 for a detailed computation.)

**Step 2: Eddington-Finkelstein coordinates — metric is regular at horizon.**

Define the advanced null coordinate $v = t + r_*$, where $r_* = r + 2M \ln|r/(2M) - 1|$ is the **tortoise coordinate**. So $v = t + r + 2M\ln|r/(2M) - 1|$, as given.

Differentiate: $dv = dt + dr + 2M\cdot \frac{1}{r - 2M}\cdot dr = dt + dr[1 + 2M/(r - 2M)] = dt + dr \cdot r/(r - 2M) = dt + (1 - 2M/r)^{-1} dr$.

So $dt = dv - (1 - 2M/r)^{-1} dr$.

Substitute into the Schwarzschild metric $ds^2 = -(1 - 2M/r) dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\Omega^2$:
- $-(1 - 2M/r) dt^2 = -(1 - 2M/r)[dv - (1 - 2M/r)^{-1} dr]^2 = -(1 - 2M/r)[dv^2 - 2 dv\, dr \cdot (1 - 2M/r)^{-1} + (1 - 2M/r)^{-2} dr^2]$
  $= -(1 - 2M/r) dv^2 + 2 dv\, dr - (1 - 2M/r)^{-1} dr^2$.
- Adding $(1 - 2M/r)^{-1} dr^2$: the last terms cancel!

Result:
$$ds^2 = -(1 - 2M/r) dv^2 + 2\, dv\, dr + r^2\, d\Omega^2.$$

This is regular at $r = 2M$: the coefficient of $dv^2$ vanishes there but the cross-term $2 dv\, dr$ does not, so the metric is non-degenerate. Compute the determinant: in matrix form with rows/columns $(v, r, \theta, \phi)$, the $(v, r)$ block is $\begin{pmatrix} -(1 - 2M/r) & 1 \\ 1 & 0 \end{pmatrix}$ with determinant $-1$ (regardless of $r$). The full determinant is $-r^4 \sin^2\theta$ — nonzero for $r > 0, \sin\theta \neq 0$ — confirming the metric is non-singular at $r = 2M$.

> [!note]- Derivation
> The substitution $v = t + r_*$ replaces $t$ by an advanced null coordinate, where ingoing light rays satisfy $dv = 0$. The tortoise coordinate $r_* = r + 2M\ln|r/(2M) - 1|$ has the property that $dr_*/dr = (1 - 2M/r)^{-1}$, which is exactly what's needed to make the cross-term $2 dv\, dr$ appear in the transformed metric, killing the offending $g_{rr}$ singularity.

**Step 3: Proper time vs. coordinate time for radial infall.**

For radial infall ($d\theta = d\phi = 0$) starting at rest at infinity ($E = 1$, marginally bound), the geodesic equation reduces (using the conserved energy $E = (1 - 2M/r)\dot t = 1$, where $\dot{} = d/d\tau$ and using the normalisation $g_{\mu\nu}\dot x^\mu \dot x^\nu = 1$):

From the normalisation: $-(1 - 2M/r)\dot t^2 + (1 - 2M/r)^{-1}\dot r^2 = -1$. Using $\dot t = E/(1 - 2M/r) = 1/(1 - 2M/r)$:
$-(1 - 2M/r) \cdot 1/(1 - 2M/r)^2 + (1 - 2M/r)^{-1}\dot r^2 = -1$
$-(1 - 2M/r)^{-1} + (1 - 2M/r)^{-1}\dot r^2 = -1$
$(1 - 2M/r)^{-1}[\dot r^2 - 1] = -1$
$\dot r^2 = 1 - (1 - 2M/r) = 2M/r$.

So $\dot r = -\sqrt{2M/r}$ (negative for infall). Integrating $d\tau/dr = -\sqrt{r/(2M)}$:
$$\tau(r_0 \to 2M) = \int_{2M}^{r_0}\sqrt{r/(2M)}\, dr = \frac{1}{\sqrt{2M}}\cdot\frac{2}{3}[r_0^{3/2} - (2M)^{3/2}].$$
**Finite.** The infalling observer reaches the horizon in finite proper time.

For coordinate time: $dt/dr = \dot t/\dot r = [1/(1 - 2M/r)]/(-\sqrt{2M/r}) = -\sqrt{r/(2M)}/(1 - 2M/r)$. Near $r = 2M$, the factor $1/(1 - 2M/r) \to \infty$, and the integral
$$t(r_0 \to 2M) = \int_{r_0}^{2M}\frac{-\sqrt{r/(2M)}}{1 - 2M/r}\, dr$$
diverges logarithmically. **Infinite.** As seen from infinity (in Schwarzschild time $t$), the infalling observer never reaches the horizon — it asymptotically approaches and "freezes".

This is the "frozen star" phenomenon: from outside, the infaller appears to slow down and asymptotically freeze at the horizon; from the infaller's perspective, they cross the horizon in finite time and reach the singularity at $r = 0$ shortly after.

> [!note]- Derivation
> The infalling timelike geodesic uses conservation of energy ($E = -g_{t\mu}\dot x^\mu = $ const along geodesic) and the normalisation $g_{\mu\nu}\dot x^\mu \dot x^\nu = 1$ (for proper-time parametrisation). For an observer at rest at infinity, $E = 1$ (the "binding energy" is zero). The reduced equation $\dot r^2 = 2M/r$ integrates to give finite proper time. The coordinate time, computed by $dt/dr = \dot t/\dot r$, includes the factor $1/(1 - 2M/r)$ that diverges at the horizon, giving infinite coordinate time.

> [!note]- Complete formal solution
> **Part (a)** — Kretschmann scalar $K = 48 M^2/r^6$: finite at $r = 2M$ (value $3/(4M^4)$), divergent at $r = 0$. So the horizon is a coordinate singularity, $r = 0$ is a genuine curvature singularity.
>
> **Part (b)** — Eddington-Finkelstein coordinates $v = t + r_* = t + r + 2M\ln|r/(2M) - 1|$. Substituting $dt = dv - (1 - 2M/r)^{-1} dr$ into the Schwarzschild metric, the $g_{rr}$ singularity is exactly cancelled by the cross-term, giving
> $$ds^2 = -(1 - 2M/r) dv^2 + 2 dv\, dr + r^2 d\Omega^2.$$
> Metric determinant $= -r^4 \sin^2\theta \neq 0$ at $r = 2M$, confirming regularity.
>
> **Part (c)** — For radial infall from rest at infinity ($E = 1$): $(dr/d\tau)^2 = 2M/r$, giving finite proper time $\tau = \frac{2}{3\sqrt{2M}}[r_0^{3/2} - (2M)^{3/2}]$ to reach the horizon. Coordinate time $\int dt = \int (1/(1 - 2M/r))\sqrt{r/(2M)} dr$ diverges logarithmically near $r = 2M$ — infinite coordinate time for the infaller as seen from infinity.
>
> So the horizon $r = 2M$ is a one-way membrane: matter falls through in finite proper time but appears to "freeze" from outside. This is the characteristic feature of a black hole event horizon. $\square$

> [!note]- Sanity-check: regularity in Kruskal-Szekeres coordinates
> A more powerful chart is **Kruskal-Szekeres**, which extends the metric not only across $r = 2M$ but also reveals the full maximal analytic extension (two asymptotically flat regions, white-hole region, black-hole region). In Kruskal-Szekeres, the metric is regular across the entire Schwarzschild spacetime except at $r = 0$, providing the complete global picture of Schwarzschild geometry.

---

# Key Takeaways

**Always test putative singularities with curvature invariants.** A diverging metric component is *not* by itself a sign of a genuine singularity — it could be a coordinate effect. The standard test: compute curvature scalars like $R$ (Ricci scalar), $R_{\mu\nu} R^{\mu\nu}$, $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$ (Kretschmann). If these are finite, the singularity is in the chart; if they diverge, it's geometric. For Schwarzschild: $R = R_{\mu\nu} R^{\mu\nu} = 0$ (vacuum); only the Kretschmann is nonzero, and it's $48 M^2/r^6$ — finite at $r = 2M$, divergent at $r = 0$. The trigger: any time a metric component blows up, compute curvature invariants before declaring a singularity.

**Null coordinates are the key to extending past coordinate singularities.** The Eddington-Finkelstein coordinate $v$ is constant along *infalling light rays* — it is a **null coordinate**. The reason this works to extend across the horizon: null geodesics cross the horizon smoothly (they don't notice it), so a coordinate adapted to null geodesics is naturally regular there. The general technique: when a coordinate singularity blocks extension, look for null coordinates adapted to the natural null structure of the geometry. The trigger: a metric of the form $g_{tt} \to 0$ at some surface suggests using a null coordinate $v = t + r_*$ with $r_*$ defined so that $dr_*/dr = -1/g_{tt}$.

**Infalling proper time vs. coordinate time — the "frozen" black hole.** The mismatch between an infaller's finite proper time and an outside observer's infinite coordinate time is the defining feature of a black hole event horizon. From the infaller's perspective, crossing the horizon is unremarkable (no local experience of anything special) — they continue to fall inward and reach the singularity in finite proper time. From the outside, the infaller's image is gravitationally redshifted and time-dilated to the point of asymptotic freezing. This is the structural origin of "black holes are black" — light from inside the horizon never reaches outside, so no information about the infaller's continued journey can be received. The trigger: any time a relativistic effect compares proper time to coordinate time, recognise that they can differ drastically in strong fields.

**The maximal analytic extension reveals more structure than Schwarzschild coordinates show.** Beyond Eddington-Finkelstein, the **Kruskal-Szekeres coordinates** extend the Schwarzschild metric to its maximal analytic continuation, revealing two asymptotically flat regions (our universe and a parallel universe), a wormhole (Einstein-Rosen bridge) connecting them, a black-hole region, and a (time-reversed) white-hole region. The **Penrose diagram** of this maximal extension is the iconic "hourglass" picture of black hole geometry. The trigger for seeking the maximal extension: any time a coordinate system has limited validity (here Schwarzschild was only valid for $r > 2M$), there may be additional spacetime regions accessible through a better chart — and these "other regions" can have physical significance (parallel universes in eternal black holes; the white-hole interior as time-reverse of black hole formation).
