---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Ehrenfest Paradox"
  - "Def - Uniformly Rotating Observer"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Problem Statement

Start from the Minkowski line element in inertial cylindrical coordinates $(t, r_*, \varphi_*, z_*)$ and pass to the corotating coordinates $(t, r, \varphi, z)$ defined by $\varphi_* = \varphi + \omega t$ (and $r_* = r$, $z_* = z$). Working with $c = 1$ where convenient:

1. Write the Minkowski line element $ds^2$ in inertial cylindrical coordinates, then substitute to obtain $ds^2$ in the corotating coordinates.
2. Identify the proper time of a corotating observer (at fixed $r, \varphi, z$) and recover the time-dilation relation $d\tau = \Gamma^{-1}dt$.
3. Read off the **spatial metric** measured by corotating observers — the proper-distance element $d\ell'^2$ — by the standard projection (the spatial metric of a stationary spacetime is $\gamma_{ij} = -g_{ij} + g_{0i}g_{0j}/g_{00}$). Show that the tangential element is $\Gamma\,r\,d\varphi$ and the radial element is $dr$.
4. Integrate to recover the Ehrenfest results: circumference $L' = \Gamma\,2\pi R$, radius $R' = R$, and the non-Euclidean ratio $L'/R' > 2\pi$.

**Recall:**

The Minkowski line element ([[Def - Minkowski Space and the Metric|Minkowski metric]]) in inertial cylindrical coordinates is $ds^2 = c^2 dt^2 - dr_*^2 - r_*^2\,d\varphi_*^2 - dz_*^2$ (mostly-minus, $c=1$: $ds^2 = dt^2 - dr_*^2 - r_*^2 d\varphi_*^2 - dz_*^2$). A [[Def - Uniformly Rotating Observer|corotating observer]] sits at fixed $(r,\varphi,z)$ in the rotating coordinates, rotating at $\varphi_* = \varphi + \omega t$ in the inertial frame; its Lorentz factor is $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$.

![[Def - The Ehrenfest Paradox#The Definition]]

---

# Convergent Strategy

**Problem class.** A *compute-the-induced-geometry* problem: transform the metric to the rotating frame and extract the spatial geometry. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]] for the Ehrenfest paradox is to measure lengths with corotating rulers, accounting for contraction tangentially but not radially.

**Assumption pattern.** A coordinate transformation $\varphi_* = \varphi + \omega t$ to the rotating frame. The signpost is "rotating coordinates": substituting into the flat metric produces cross terms $g_{t\varphi}$ that encode the rotation, and the spatial metric extracted from them is non-Euclidean.

**Theorem routing.** Part 1 substitutes the coordinate transformation into the flat metric; part 2 sets $dr = d\varphi = dz = 0$ to get the proper time, recovering $\Gamma$ from [[Def - Uniformly Rotating Observer]]; part 3 applies the spatial-metric projection of a stationary metric; part 4 integrates to recover the Ehrenfest circumference and radius from [[Def - The Ehrenfest Paradox]].

**Key decision point.** The crux is that the spatial metric is *not* simply the $g_{ij}$ block of the rotating metric, but the projected $\gamma_{ij} = -g_{ij} + g_{0i}g_{0j}/g_{00}$, which accounts for the corotating observer's simultaneity (orthogonal to its worldline). The naive reading of $g_{ij}$ would miss the $\Gamma$ enhancement of the circumference; the projection is what produces it. The non-obvious move is using the stationary-spacetime spatial-metric formula rather than the bare spatial block.

---

# Legal Operations Used

1. **Operation 6 from the topic page (measure lengths with corotating rulers).** The spatial metric $\gamma_{ij}$ gives the proper-distance element, contracted tangentially ($\Gamma r\,d\varphi$) but not radially ($dr$).

2. **Operation 2 from the topic page (the rim Lorentz factor).** $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ emerges from $g_{00}$ in the rotating coordinates and sets the circumference enhancement.

3. **Operation 3 from the topic page (Einstein–Poincaré simultaneity).** The spatial-metric projection encodes the corotating observer's simultaneity (orthogonality to the worldline), which is why $\gamma_{ij}\ne -g_{ij}$.

---

# Hints

> [!note]- Hint 1
> Substitute $\varphi_* = \varphi + \omega t$, so $d\varphi_* = d\varphi + \omega\,dt$, into $ds^2 = dt^2 - dr_*^2 - r_*^2 d\varphi_*^2 - dz_*^2$ (with $r_* = r$, $z_* = z$). Expand $r^2(d\varphi + \omega dt)^2 = r^2 d\varphi^2 + 2r^2\omega\,d\varphi\,dt + r^2\omega^2 dt^2$.

> [!note]- Hint 2
> A corotating observer has $dr = d\varphi = dz = 0$, so $ds^2 = (1 - r^2\omega^2/c^2)\,dt^2 = \Gamma^{-2}dt^2$. The proper time is $d\tau = \sqrt{ds^2} = \Gamma^{-1}dt$ — corotating clocks run slow by $\Gamma$.

> [!note]- Hint 3
> The rotating metric has $g_{00} = 1 - r^2\omega^2/c^2 = \Gamma^{-2}$, $g_{0\varphi} = -r^2\omega$ (the cross term), $g_{rr} = -1$, $g_{\varphi\varphi} = -r^2$, $g_{zz} = -1$. The spatial metric is $\gamma_{ij} = -g_{ij} + g_{0i}g_{0j}/g_{00}$. The $\varphi\varphi$ component gets the $g_{0\varphi}^2/g_{00}$ correction; the $rr$ and $zz$ do not (no cross terms).

> [!note]- Hint 4
> The $\varphi\varphi$ spatial metric component is $\gamma_{\varphi\varphi} = r^2 + (r^2\omega)^2/\Gamma^{-2} = r^2/(1 - r^2\omega^2/c^2) = \Gamma^2 r^2$, so the tangential element is $\sqrt{\gamma_{\varphi\varphi}}\,d\varphi = \Gamma r\,d\varphi$. The radial element is $\sqrt{\gamma_{rr}}\,dr = dr$. Integrate around the rim and along the radius.

---

# Solution

The route has four steps. Step 1 substitutes $\varphi_* = \varphi + \omega t$ into the flat metric, producing cross terms. Step 2 reads the corotating proper time as $\Gamma^{-1}dt$. Step 3 projects out the spatial metric, finding $\gamma_{\varphi\varphi} = \Gamma^2 r^2$ (tangentially enhanced) and $\gamma_{rr} = 1$ (radially unchanged). Step 4 integrates to recover $L' = \Gamma\,2\pi R$, $R' = R$. The non-obvious move is the spatial-metric projection in Step 3, which accounts for the corotating simultaneity.

**Step 1: The rotating-frame line element.**

> [!note]- Derivation
> The Minkowski line element in inertial cylindrical coordinates is
> $$ds^2 = dt^2 - dr_*^2 - r_*^2\,d\varphi_*^2 - dz_*^2.$$
> Substitute $\varphi_* = \varphi + \omega t$ (so $d\varphi_* = d\varphi + \omega\,dt$), $r_* = r$, $z_* = z$:
> $$ds^2 = dt^2 - dr^2 - r^2(d\varphi + \omega\,dt)^2 - dz^2.$$
> Expanding $r^2(d\varphi + \omega dt)^2 = r^2 d\varphi^2 + 2r^2\omega\,d\varphi\,dt + r^2\omega^2\,dt^2$,
> $$\boxed{ds^2 = \left(1 - \frac{r^2\omega^2}{c^2}\right)dt^2 - 2r^2\omega\,d\varphi\,dt - dr^2 - r^2\,d\varphi^2 - dz^2}$$
> (restoring $c$ in the $dt^2$ coefficient). The metric components are $g_{00} = 1 - r^2\omega^2/c^2 = \Gamma^{-2}$, $g_{0\varphi} = g_{\varphi 0} = -r^2\omega$, $g_{rr} = -1$, $g_{\varphi\varphi} = -r^2$, $g_{zz} = -1$. The cross term $g_{0\varphi} = -r^2\omega$ is the signature of rotation — it is what prevents a global time and produces the Sagnac effect.

**Step 2: Corotating proper time and time dilation.**

> [!note]- Derivation
> A corotating observer is fixed in the rotating coordinates: $dr = d\varphi = dz = 0$. Along its worldline,
> $$ds^2 = g_{00}\,dt^2 = \left(1 - \frac{r^2\omega^2}{c^2}\right)dt^2 = \Gamma^{-2}\,dt^2.$$
> The proper time is
> $$d\tau = \sqrt{ds^2} = \Gamma^{-1}\,dt,$$
> so $\tau = t\sqrt{1 - r^2\omega^2/c^2}$. A corotating clock runs slow relative to the central clock by the rim Lorentz factor $\Gamma$ — ordinary time dilation, since the corotating observer moves at $r\omega$ relative to the inertial one. This recovers the result of [[Def - Uniformly Rotating Observer]].

**Step 3: The spatial metric — tangentially enhanced, radially unchanged.**

> [!note]- Derivation
> The proper distance measured by corotating observers between simultaneous events is governed by the spatial metric of the stationary metric,
> $$\gamma_{ij} = -g_{ij} + \frac{g_{0i}g_{0j}}{g_{00}},$$
> the projection orthogonal to the corotating worldline (this is exactly the Einstein–Poincaré simultaneity condition, [[Def - Einstein-Poincaré Simultaneity]], built into the metric). The components:
> - **Radial:** $g_{0r} = 0$, so $\gamma_{rr} = -g_{rr} = 1$. No correction — the radial direction is orthogonal to the motion.
> - **Vertical:** $g_{0z} = 0$, so $\gamma_{zz} = -g_{zz} = 1$. No correction.
> - **Tangential:** $g_{0\varphi} = -r^2\omega$, $g_{00} = \Gamma^{-2}$, so
> $$\gamma_{\varphi\varphi} = -g_{\varphi\varphi} + \frac{g_{0\varphi}^2}{g_{00}} = r^2 + \frac{(r^2\omega)^2}{\Gamma^{-2}} = r^2 + r^4\omega^2\Gamma^2 = r^2\Gamma^2\left(\Gamma^{-2} + r^2\omega^2\right) = r^2\Gamma^2,$$
> using $\Gamma^{-2} + r^2\omega^2/c^2 = 1$. So the proper spatial line element is
> $$d\ell'^2 = dr^2 + \Gamma^2 r^2\,d\varphi^2 + dz^2.$$
> The tangential proper-length element is $\sqrt{\gamma_{\varphi\varphi}}\,d\varphi = \Gamma r\,d\varphi$ — *enhanced* by $\Gamma$ — while the radial element is $dr$ — unchanged. This is the heart of the Ehrenfest result.

**Step 4: The Ehrenfest circumference and radius.**

> [!note]- Derivation
> Integrating the spatial line element:
> - **Circumference** (around the rim at fixed $r = R$, $z = 0$): $L' = \oint\Gamma R\,d\varphi = \Gamma R\int_0^{2\pi}d\varphi = \Gamma\,2\pi R$ (with $\Gamma$ constant at fixed $R$).
> - **Radius** (along fixed $\varphi$, from centre to rim): $R' = \int_0^R dr = R$.
> Hence
> $$\frac{L'}{R'} = \frac{\Gamma\,2\pi R}{R} = \Gamma\,2\pi > 2\pi,$$
> the **non-Euclidean** ratio of [[Def - The Ehrenfest Paradox]]. The corotating observers measure a circumference exceeding $2\pi$ times the radius — the disk's rest geometry is that of a surface of negative Gaussian curvature, even though the spacetime is flat. The spatial metric $d\ell'^2 = dr^2 + \Gamma^2 r^2 d\varphi^2$ makes this explicit and quantitative.

> [!note]- Complete formal solution
> Substituting $\varphi_* = \varphi + \omega t$ into the flat cylindrical metric gives $ds^2 = (1 - r^2\omega^2/c^2)dt^2 - 2r^2\omega\,d\varphi\,dt - dr^2 - r^2 d\varphi^2 - dz^2$, with $g_{00} = \Gamma^{-2}$, $g_{0\varphi} = -r^2\omega$. A corotating observer ($dr = d\varphi = dz = 0$) has $d\tau = \Gamma^{-1}dt$. The spatial metric $\gamma_{ij} = -g_{ij} + g_{0i}g_{0j}/g_{00}$ gives $\gamma_{rr} = 1$, $\gamma_{zz} = 1$, and $\gamma_{\varphi\varphi} = r^2 + r^4\omega^2\Gamma^2 = \Gamma^2 r^2$, so $d\ell'^2 = dr^2 + \Gamma^2 r^2 d\varphi^2 + dz^2$. The tangential element is $\Gamma r\,d\varphi$, the radial $dr$. Integrating, $L' = \Gamma\,2\pi R$ and $R' = R$, so $L'/R' = \Gamma\,2\pi > 2\pi$ — the non-Euclidean Ehrenfest geometry. $\blacksquare$

**Frame-invariance check.** The spatial metric $d\ell'^2 = dr^2 + \Gamma^2 r^2 d\varphi^2$ can be checked against the direct length-contraction argument: a tangential arc, viewed by the inertial observer, is contracted to $r\,d\varphi$ from its proper length $\Gamma r\,d\varphi$, consistent with the rim observer measuring the longer $\Gamma r\,d\varphi$; the radial direction, perpendicular to the motion, is uncontracted, so $\gamma_{rr} = 1$. Both routes agree.

---

# Key Takeaways

**The cross term $g_{0\varphi}$ in a rotating metric is the signature of rotation, and it is what makes the geometry non-trivial.** Transforming the flat metric to rotating coordinates produces an off-diagonal term $g_{0\varphi} = -r^2\omega$ mixing time and angle. This single term carries all the rotational physics: it prevents the existence of a global time (no choice of time coordinate removes it globally), it produces the Sagnac effect, and through the spatial-metric projection it enhances the tangential proper length. The trigger to watch for is any metric with $g_{0i}\ne 0$ — a *stationary but not static* metric: such metrics describe rotating or otherwise circulating frames, and the off-diagonal terms encode frame dragging, the impossibility of global synchronization, and a non-trivial spatial geometry. The same structure appears in the Kerr metric of a rotating black hole, where $g_{t\varphi}\ne 0$ is the gravomagnetic frame-dragging term — the curved-spacetime descendant of the rotating-disk cross term.

**The spatial metric is the *projected* metric, not the bare spatial block — and the projection encodes simultaneity.** The proper distances corotating observers measure are governed by $\gamma_{ij} = -g_{ij} + g_{0i}g_{0j}/g_{00}$, not by $-g_{ij}$ alone. The correction term comes from the corotating observer's simultaneity (its rest space is orthogonal to its worldline, not to the global time axis), and it is exactly what enhances the tangential length by $\Gamma$. The trigger is any proper-distance computation in a stationary metric with $g_{0i}\ne 0$: never read distances off the bare $g_{ij}$ block; always project. Forgetting the projection would give a Euclidean circumference $2\pi r$ instead of the correct $\Gamma\,2\pi r$, missing the entire Ehrenfest effect. This projection is the metric incarnation of the Einstein–Poincaré simultaneity convention, and getting it right is the difference between Euclidean and non-Euclidean disk geometry.

**A flat spacetime can have a curved spatial slice — the curvature lives in the choice of observer, not in the spacetime.** The spacetime here is exactly flat Minkowski space (zero Riemann tensor), yet the rest geometry of the corotating congruence is non-Euclidean ($L'/R' = \Gamma\,2\pi > 2\pi$), the geometry of a negatively curved surface. The resolution is that "the rest space of the rotating observers" is not a slice of the flat spacetime but the projected geometry of a congruence with vorticity, and that projected geometry can curve even when the ambient spacetime does not. The trigger to keep these distinct is the question "curvature of *what*?": the spacetime, or the spatial slice of a particular family of observers. This distinction is the conceptual seed of general relativity — it shows that non-Euclidean geometry can arise from acceleration/rotation in flat spacetime, which made it natural for Einstein to suppose that gravity (equivalent to acceleration) curves the *spacetime* itself. See [[Def - The Ehrenfest Paradox]] for the historical role of this observation.
