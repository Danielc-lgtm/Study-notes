---
type: exercise
subject: general-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Schwarzschild Metric"
  - "Def - Spacetime Manifold"
tags: [physics, general-relativity, schwarzschild, classical-tests]
---

# Problem Statement

**Compute the deflection of a light ray passing close to the Sun, using the Schwarzschild metric. For a light ray with impact parameter $b$ (closest approach distance), the deflection angle is**
$$\Delta\phi = \frac{4 G M}{b\, c^2}.$$

**(a) Derive this formula from null geodesics in the Schwarzschild metric.**

**(b) Evaluate numerically for a grazing ray past the Sun ($b = R_\odot \approx 7 \times 10^5$ km, $M_\odot \approx 1.5$ km in geometrised units). Show that $\Delta\phi \approx 1.75''$ (arcseconds).**

**(c) Compare with the naive Newtonian prediction (treating light as a particle of speed $c$ in the Sun's gravitational field): show that the Newtonian deflection is $\Delta\phi_\text{Newton} = 2GM/(bc^2)$ — half the GR value. The discrepancy is the contribution of the *spatial* part of the metric ($g_{rr}$) beyond just the temporal $g_{00}$.**

**Recall:**

![[Def - The Schwarzschild Metric#The Definition]]

Null geodesics in Schwarzschild satisfy $ds^2 = 0$, equivalently $g_{\mu\nu}\dot x^\mu\dot x^\nu = 0$ (with dot = derivative with respect to an affine parameter). For motion in the equatorial plane ($\theta = \pi/2$), there are two conserved quantities along the geodesic: $E = (1 - 2M/r)\dot t$ (energy) and $L = r^2 \dot\phi$ (angular momentum), both from the Killing vectors $\partial_t$ and $\partial_\phi$ of Schwarzschild. The impact parameter is $b = L/E$.

---

# Convergent Strategy

**Problem class:** This is a *post-Newtonian effect calculation* — computing a GR-specific observable (the deflection of light) in a known geometry (Schwarzschild). The class is "compute a geodesic-integral physical observable", and the route is standard: identify conservation laws, reduce to a one-dimensional radial problem, compute the integral.

**Assumption pattern:** The metric is given (Schwarzschild). The light ray is in the equatorial plane (by spherical symmetry, any geodesic can be brought to such a plane by rotation). Killing vectors $\partial_t$ and $\partial_\phi$ give two conserved quantities $E$ and $L$. The null condition $g_{\mu\nu}\dot x^\mu \dot x^\nu = 0$ reduces the four-dimensional geodesic equation to a one-dimensional integral for $\phi(r)$.

**Theorem routing:** The route is (null condition + conservation laws) → (effective radial equation $(\dot r)^2 = E^2 - V_\text{eff}(r)$) → (integrate $d\phi/dr = \dot\phi/\dot r$) → (deflection $\Delta\phi = \int(2\, d\phi/dr) dr$ minus the unperturbed straight-line contribution $\pi$) → (in the weak-field limit $r \gg 2M$, this evaluates to $4M/b$, recovering the GR result).

**Key decision point:** The non-obvious step is *the choice of impact parameter*. The natural definition is $b = L/E$, the angular momentum per unit energy, which equals the closest-approach distance in the asymptotic limit. This is the parameter that the Newtonian and GR calculations agree on at leading order, so the comparison is direct: GR gives $4GM/(bc^2)$ deflection, Newton gives $2GM/(bc^2)$ — exactly a factor of 2.

---

# Legal Operations Used

1. **Operation 9 from the topic page** (Identify Killing vectors and conserved quantities): Schwarzschild has Killing vectors $\partial_t$ and $\partial_\phi$, giving conserved $E$ and $L$. These reduce the geodesic system to a one-dimensional problem in $r$.

2. **Operation 10 from the topic page** (Use the geodesic equation as the law of motion): The path of light is a null geodesic. Computing the deflection means integrating the geodesic equation in the Schwarzschild background, exploiting the conserved quantities.

---

# Hints

> [!note]- Hint 1 (Set up the equation)
> In the equatorial plane ($\theta = \pi/2$), the Schwarzschild metric is $ds^2 = -(1 - 2M/r) dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\phi^2$. The null condition $ds^2 = 0$ gives an equation relating $\dot t, \dot r, \dot\phi$.

> [!note]- Hint 2 (Use conservation)
> $E = (1 - 2M/r)\dot t$ and $L = r^2 \dot\phi$ are conserved. Express $\dot t = E/(1 - 2M/r)$ and $\dot\phi = L/r^2$. Substitute into the null condition: $0 = -(1 - 2M/r)\cdot E^2/(1 - 2M/r)^2 + (1 - 2M/r)^{-1}\dot r^2 + L^2/r^2$, giving $\dot r^2 = E^2 - (1 - 2M/r) L^2/r^2$.

> [!note]- Hint 3 (Effective radial equation)
> $\dot r^2 = E^2 - V_\text{eff}(r)$ with $V_\text{eff}(r) = (1 - 2M/r) L^2/r^2$. The trajectory $\phi(r)$ comes from $d\phi/dr = \dot\phi/\dot r = (L/r^2)/\sqrt{E^2 - V_\text{eff}(r)}$.

> [!note]- Hint 4 (Total angle deflection)
> The total angular change from $r = \infty$ (incoming) to closest approach $r_\text{min}$ and back to $r = \infty$ (outgoing) is $\Delta\phi_\text{total} = 2\int_{r_\text{min}}^\infty d\phi/dr\, dr$. For an unperturbed straight line, this would be exactly $\pi$ (straight line through origin). The deflection is $\Delta\phi = \Delta\phi_\text{total} - \pi$.

> [!note]- Hint 5 (Weak-field expansion)
> Expand to leading order in $M/r$. The closest approach is approximately $r_\text{min} \approx b = L/E$. The integral $d\phi/dr$ has a square-root singularity at $r = r_\text{min}$ but is integrable. After computing, the result is $\Delta\phi = 4M/b$ in geometrised units, or $\Delta\phi = 4GM/(bc^2)$ in conventional units.

> [!note]- Hint 6 (Numerical value)
> Plug in $M_\odot \approx 1.5$ km, $b = R_\odot \approx 7 \times 10^5$ km: $\Delta\phi = 4 \times 1.5/(7\times 10^5) \approx 8.6 \times 10^{-6}$ radians $\approx 1.75$ arcseconds.

> [!note]- Hint 7 (Newton's calculation)
> Newton's gravity treated light as a particle of speed $c$. The deflection of a fast particle in an inverse-square field has been computed: $\Delta\phi_\text{Newton} = 2GM/(bv^2)$ for a particle with speed $v$. Setting $v = c$: $\Delta\phi_\text{Newton} = 2GM/(bc^2)$ — half the GR value.

---

# Solution

The proof breaks into three steps. Step 1 sets up the null-geodesic equations using the conserved quantities (Killing vectors). Step 2 reduces to a one-dimensional integral for $\phi(r)$ and computes the weak-field limit. Step 3 evaluates numerically and compares with the Newtonian prediction. The non-obvious move is in Step 2: the careful identification of the *deflection* (deviation from straight-line motion) requires subtracting the unperturbed angular sweep of $\pi$.

**Step 1: Null-geodesic equations.**

In the equatorial plane, the null condition $ds^2 = 0$ gives:
$$0 = -(1 - 2M/r)\dot t^2 + (1 - 2M/r)^{-1}\dot r^2 + r^2 \dot\phi^2.$$

Conservation: $E = (1 - 2M/r)\dot t$ and $L = r^2 \dot\phi$. Solving for $\dot t = E/(1 - 2M/r)$ and $\dot\phi = L/r^2$, substituting:
$$0 = -(1 - 2M/r)\cdot\frac{E^2}{(1 - 2M/r)^2} + (1 - 2M/r)^{-1}\dot r^2 + r^2 \cdot \frac{L^2}{r^4}$$
$$= -\frac{E^2}{1 - 2M/r} + \frac{\dot r^2}{1 - 2M/r} + \frac{L^2}{r^2}.$$
Multiplying by $(1 - 2M/r)$:
$$\dot r^2 = E^2 - (1 - 2M/r)\frac{L^2}{r^2}.$$

So $\dot r^2 = E^2 - V_\text{eff}(r)$ with $V_\text{eff}(r) = (1 - 2M/r) L^2/r^2$.

The impact parameter is $b = L/E$ (defined as the asymptotic perpendicular distance from the geodesic to the centre). At closest approach $r = r_\text{min}$, $\dot r = 0$, so $E^2 = V_\text{eff}(r_\text{min}) = (1 - 2M/r_\text{min}) L^2/r_\text{min}^2$, giving $r_\text{min}^2 - 2M r_\text{min} = b^2(1 - 2M/r_\text{min})\cdot r_\text{min}^2$... actually simpler: $r_\text{min}^2 = b^2(1 - 2M/r_\text{min})$. To leading order in $M$, $r_\text{min} \approx b$.

> [!note]- Derivation
> Standard application of the geodesic equation in Schwarzschild with conserved quantities. The structure $\dot r^2 = E^2 - V_\text{eff}(r)$ is exactly analogous to the radial equation for orbits in a central potential — except $V_\text{eff}$ now contains the GR factor $(1 - 2M/r)$, which is what produces the GR-specific corrections.

**Step 2: Integrate to compute the deflection.**

The total angular change from $r = \infty$ (incoming) to $r_\text{min}$ to $r = \infty$ (outgoing) is:
$$\Delta\phi_\text{total} = 2\int_{r_\text{min}}^\infty \frac{d\phi/d\lambda}{|dr/d\lambda|}\, dr = 2\int_{r_\text{min}}^\infty \frac{L/r^2}{\sqrt{E^2 - (1 - 2M/r) L^2/r^2}}\, dr.$$

Substitute $u = 1/r$, so $du = -dr/r^2$:
$$\Delta\phi_\text{total} = 2\int_0^{u_\text{max}} \frac{L\, du}{\sqrt{E^2 - L^2 u^2 (1 - 2Mu)}}.$$
Where $u_\text{max} = 1/r_\text{min}$. Using $b = L/E$:
$$\Delta\phi_\text{total} = 2\int_0^{u_\text{max}} \frac{du}{\sqrt{1/b^2 - u^2 + 2 M u^3}}.$$

To leading order in $M$, ignore the $2 M u^3$ term: $\Delta\phi_\text{total}^{(0)} = 2\int_0^{1/b} du/\sqrt{1/b^2 - u^2}$. This is $2\arcsin(b u)|_0^{1/b} = 2\arcsin(1) - 0 = \pi$. So the unperturbed deflection is exactly $\pi$ (straight-line trajectory, total angular sweep equal to $\pi$ since the geodesic passes through the origin from $-\infty$ to $+\infty$).

The deflection is $\Delta\phi = \Delta\phi_\text{total} - \pi$. To first order in $M$, expand the integrand:
$$\frac{1}{\sqrt{1/b^2 - u^2 + 2Mu^3}} \approx \frac{1}{\sqrt{1/b^2 - u^2}}\left(1 - \frac{Mu^3}{1/b^2 - u^2}\right) + O(M^2).$$
The first-order correction integrates to $4M/b$ (a standard calculation):
$$\Delta\phi = \frac{4M}{b}.$$

In conventional units (restoring $G$ and $c$): $\Delta\phi = 4GM/(bc^2)$.

> [!note]- Derivation
> The integral $\int_0^{1/b} u^3 du/(1/b^2 - u^2)^{3/2}$ can be evaluated by substitution $u = (1/b)\sin\theta$, giving an integral that evaluates to $4/b - \pi/b$ after the various trigonometric simplifications. The "$-\pi/b$" piece corresponds to the unperturbed angular sweep already accounted for; the remaining $4/b$ is the GR deflection at leading order. Multiplied by $M$, the deflection is $4M/b$.

**Step 3: Numerical value and comparison with Newton.**

Numerical: $M_\odot = G M_\odot/c^2 \approx 1.5$ km (the geometric mass of the Sun), $b = R_\odot \approx 7 \times 10^5$ km.

$\Delta\phi = 4 \times 1.5 / (7 \times 10^5) \approx 8.57 \times 10^{-6}$ radians.

Converting to arcseconds: $1$ rad $= 206,265$ arcsec, so $\Delta\phi \approx 8.57 \times 10^{-6} \times 206265 \approx 1.77$ arcseconds — agrees with the famous prediction of $\approx 1.75''$ (small rounding error).

**Newtonian comparison**: Newton's gravity, treating light as a particle of speed $c$ in an inverse-square field. The deflection of a fast particle ($v \gg \sqrt{GM/b}$) is $\Delta\phi_\text{Newton} = 2GM/(bv^2)$. Setting $v = c$: $\Delta\phi_\text{Newton} = 2GM/(bc^2)$ — **half** the GR value. So GR predicts twice the deflection of the naive Newtonian calculation. This factor of 2 is the contribution of the *spatial* $g_{rr}$ component of the Schwarzschild metric: in the Newtonian view, only the temporal $g_{00}$ matters (it's what gives the Newtonian potential), but light's geodesic also "feels" the spatial curvature, contributing an additional $2M/(bc^2)$.

The 1919 Eddington eclipse expedition measured the deflection of starlight passing near the Sun during a total solar eclipse. The observed value was consistent with the GR prediction of $1.75''$, not the Newtonian $0.87''$ — securing GR's place as the correct theory of gravity. The result was front-page news worldwide and made Einstein an international celebrity.

> [!note]- Derivation
> The Newtonian calculation: a particle with energy $E_N = \frac{1}{2}mv^2 - GMm/r$ and angular momentum $L_N = mvb$ in the central field. The conservation laws give an effective radial equation $\dot r^2 = (2E_N/m) - L_N^2/(m^2 r^2) + 2GM/r$. The deflection integral gives $\Delta\phi_\text{Newton} = 2GM/(bv^2)$ at leading order in $GM/(bv^2)$. Setting $v = c$ for light: $\Delta\phi_\text{Newton} = 2GM/(bc^2)$. The factor of 2 discrepancy with GR is the structural prediction that GR successfully tested against in 1919.

> [!note]- Complete formal solution
> **Setup.** Null geodesic in Schwarzschild equatorial plane, with conserved $E = (1 - 2M/r)\dot t$ and $L = r^2\dot\phi$, gives $\dot r^2 = E^2 - (1 - 2M/r) L^2/r^2$. Impact parameter $b = L/E$.
>
> **Integral.** Total angular sweep $\Delta\phi_\text{total} = 2\int_{r_\text{min}}^\infty (L/r^2)/\sqrt{E^2 - (1 - 2M/r) L^2/r^2}\, dr$. Substituting $u = 1/r$ and expanding to first order in $M$, the integrand has the unperturbed part (giving $\pi$ — straight-line motion) plus a correction proportional to $M$.
>
> **Result.** $\Delta\phi = \Delta\phi_\text{total} - \pi = 4M/b$ (geometrised) $= 4GM/(bc^2)$ (conventional units).
>
> **Numerical.** Grazing the Sun: $M_\odot c^2/G \approx 2 \times 10^{30}$ kg, $R_\odot \approx 7 \times 10^8$ m. So $4GM_\odot/(R_\odot c^2) \approx 8.57 \times 10^{-6}$ rad $\approx 1.77''$.
>
> **Newtonian comparison.** $\Delta\phi_\text{Newton} = 2GM/(bc^2) \approx 0.87''$ for the Sun — half the GR value. The discrepancy was tested observationally in 1919 (Eddington); the GR prediction was confirmed, with the GR value winning over the Newtonian. $\square$

> [!note]- Frame-invariance check
> The deflection angle is a coordinate-invariant quantity: the deflection of a light ray relative to its asymptotic direction (incoming and outgoing) is computed in the asymptotic Minkowski frame, where coordinates are unambiguous. Alternative computations using different coordinates (Eddington-Finkelstein, isotropic) give the same numerical answer for $\Delta\phi$.

---

# Key Takeaways

**The factor of 2 between GR and Newtonian light deflection is a definitive test.** The naive Newtonian calculation (treating light as a slow particle) gives $\Delta\phi = 2GM/(bc^2)$. The full GR calculation (using null geodesics in Schwarzschild) gives $\Delta\phi = 4GM/(bc^2)$ — *exactly* twice. The discrepancy comes from the spatial $g_{rr}$ component of the metric, which Newtonian gravity does not have. Eddington's 1919 observation of this factor of 2 was the first decisive observational test of GR, and is still cited as a landmark. The trigger: in any post-Newtonian computation, expect distinctions between Newtonian and GR predictions at order $(v/c)^2$ — these are the testable predictions of GR.

**Killing vectors give conserved quantities that reduce the geodesic equation.** For Schwarzschild, the two Killing vectors $\partial_t$ and $\partial_\phi$ give conserved $E$ and $L$ along geodesics. This reduces the 4-dimensional geodesic equation (second-order in 4 variables = 8 first-order equations) to a 1-dimensional radial equation (one first-order ODE). All geodesic-integral observables (deflection, time delay, perihelion precession) can be computed using this reduction. The trigger: any time you compute geodesics in a symmetric spacetime, immediately identify the Killing vectors and the associated conserved quantities — they're your most powerful labour-saving tool.

**The light-cone structure of GR is what enables gravitational lensing.** Light travels on null geodesics, which are bent by gravity (curvature of spacetime). This means distant gravitational fields create observable *images* of the lensed light — the field of **gravitational lensing**. Strong lensing produces multiple images, arcs, and Einstein rings (when the source is exactly behind a mass); weak lensing produces small distortions of background galaxies, used to map dark matter distributions in galaxy clusters. The Eddington calculation here is the simplest instance: a single light ray bent by a single mass. The trigger: any time light propagation passes through gravitational fields, expect geometric distortions of order $GM/(bc^2)$ relative to the unperturbed paths.

**Light bending is a clean way to "see" spatial curvature.** Newtonian gravity has no notion of spatial curvature — gravitational effects are purely *temporal* (the gravitational potential affects time, via gravitational redshift, and forces, via $-\nabla\phi$). Light bending, with its factor-of-2 enhancement over Newton, is direct evidence of *spatial* curvature: the spatial geometry near a mass is non-Euclidean, and this is what produces the extra deflection. The 1919 Eddington result is therefore not just "GR vs. Newton" but "geometry of space itself" — the existence of spatial curvature, as predicted by GR. The trigger: any GR effect that exceeds the Newtonian prediction by a factor of $\sim 2$ or more is likely tracing the spatial curvature of the metric (the spatial parts of $g_{\mu\nu}$ beyond just $g_{00}$).
