---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Joukowski Aerofoil Construction"
  - "Def - Conformal Map"
  - "Def - Complex Potential"
tags: [analysis, complex-analysis, fluid-dynamics]
---

# Problem Statement

(a) Show that the Joukowski transformation $J(z) = z + 1/z$ maps the unit circle $|z| = 1$ to the segment $[-2, 2]$ on the real axis (traversed twice).

(b) Show that for $r > 1$, the circle $|z| = r$ maps to an ellipse in the $w$-plane with semi-axes $r + 1/r$ (along $\operatorname{Re} w$) and $r - 1/r$ (along $\operatorname{Im} w$).

(c) Show that an off-centred circle $|z - z_0| = a$ with $z_0 = -\epsilon$ (small real, positive) and $a = 1 + \epsilon$ (so the circle passes through $z = 1$) maps under $J$ to an aerofoil-like curve in the $w$-plane, with a sharp cusp at $w = J(1) = 2$.

**Recall:**

![[Thm - Joukowski Aerofoil Construction#The Definition]]

$J(z) = z + 1/z$ is conformal except at $z = \pm 1$ (where $J' = 1 - 1/z^2 = 0$). The unit circle maps to the segment $[-2, 2]$.

---

# Convergent Strategy

**Problem class:** Verify the geometric action of the Joukowski transformation on three increasingly nontrivial curves. Each part builds intuition for the next: unit circle → segment, larger circle → ellipse, off-centred circle → aerofoil.

**Assumption pattern:** $J(z) = z + 1/z$, $z = re^{i\theta}$ for various $r$.

**Theorem routing:** Direct computation in polar coordinates, separating into real and imaginary parts.

**Key decision point:** Use the polar form $z = re^{i\theta}$ to compute $J(z) = re^{i\theta} + (1/r)e^{-i\theta} = (r + 1/r)\cos\theta + i(r - 1/r)\sin\theta$. Reading off real and imaginary parts gives the ellipse parametrization.

---

# Legal Operations Used

1. **Polar parametrization** $z = re^{i\theta}$, $1/z = (1/r)e^{-i\theta}$.
2. **Compute $J(z) = z + 1/z$ in real/imaginary parts**: $J(z) = (r + 1/r)\cos\theta + i(r - 1/r)\sin\theta$.
3. **For $r = 1$**: $J = 2\cos\theta + i\cdot 0 = 2\cos\theta$, real, in $[-2, 2]$.
4. **For $r > 1$**: ellipse equation $X/(r + 1/r))^2 + (Y/(r - 1/r))^2 = 1$.
5. **For off-centred circle**: parametrize $z = z_0 + ae^{i\theta}$, compute $J(z)$, observe cusp at $z = 1$.

---

# Hints

> [!note]- Hint 1
> Polar form: $z + 1/z = re^{i\theta} + r^{-1}e^{-i\theta} = (r + r^{-1})\cos\theta + i(r - r^{-1})\sin\theta$.

> [!note]- Hint 2
> For $r = 1$: $r + r^{-1} = 2$, $r - r^{-1} = 0$. So $J(e^{i\theta}) = 2\cos\theta \in [-2, 2]$.

> [!note]- Hint 3
> For $r > 1$: write $w = X + iY = (r + r^{-1})\cos\theta + i(r - r^{-1})\sin\theta$. Then $X/(r + r^{-1}) = \cos\theta$, $Y/(r - r^{-1}) = \sin\theta$. Squaring and adding: $X^2/(r + r^{-1})^2 + Y^2/(r - r^{-1})^2 = 1$, an ellipse.

> [!note]- Hint 4
> For the off-centred circle: $z = z_0 + ae^{i\theta}$, $J(z) = z_0 + ae^{i\theta} + 1/(z_0 + ae^{i\theta})$. Near $z = 1$ (corresponding to $z_0 + ae^{i\theta} = 1$, i.e., $\theta$ near $0$ for the specific values $z_0 = -\epsilon, a = 1 + \epsilon$), the second term $1/(z_0 + ae^{i\theta}) = 1/z$ has a "pinch" because $J'(1) = 0$.

---

# Solution

**(a) Unit circle to $[-2, 2]$**

> [!note]- Derivation
> On $|z| = 1$: $z = e^{i\theta}, 1/z = e^{-i\theta}$. So
> $$J(e^{i\theta}) = e^{i\theta} + e^{-i\theta} = 2\cos\theta.$$
> As $\theta$ varies over $[0, 2\pi)$, $2\cos\theta$ takes every value in $[-2, 2]$, traversing the segment *twice* (once for $\theta \in [0, \pi]$, decreasing from $2$ to $-2$; once for $\theta \in [\pi, 2\pi]$, increasing back).

**(b) Circle of radius $r > 1$ to ellipse**

> [!note]- Derivation
> On $|z| = r$: $z = re^{i\theta}, 1/z = (1/r)e^{-i\theta}$. So
> $$J(re^{i\theta}) = re^{i\theta} + \frac{1}{r}e^{-i\theta} = (r + 1/r)\cos\theta + i(r - 1/r)\sin\theta.$$
>
> Writing $w = X + iY$: $X = (r + 1/r)\cos\theta$, $Y = (r - 1/r)\sin\theta$.
>
> Setting $A = r + 1/r$ and $B = r - 1/r$ (note $A > B > 0$ for $r > 1$):
> $$\frac{X^2}{A^2} + \frac{Y^2}{B^2} = \cos^2\theta + \sin^2\theta = 1,$$
> the equation of an ellipse with semi-axes $A = r + 1/r$ along $X$-axis and $B = r - 1/r$ along $Y$-axis.

**(c) Off-centred circle to aerofoil**

> [!note]- Derivation
> Parametrize the off-centred circle: $z(\theta) = z_0 + ae^{i\theta}$ with $z_0 = -\epsilon, a = 1 + \epsilon$. Then
> $$J(z(\theta)) = z_0 + ae^{i\theta} + \frac{1}{z_0 + ae^{i\theta}}.$$
>
> At $\theta = 0$: $z(0) = z_0 + a = -\epsilon + 1 + \epsilon = 1$. So $J(z(0)) = 1 + 1/1 = 2$. This is the cusp point (trailing edge of the aerofoil).
>
> $J'(z) = 1 - 1/z^2$ vanishes at $z = \pm 1$. At $z = 1$ (where the circle passes), $J' = 0$, so the conformality fails. The image curve develops a *cusp* (zero-angle point) at $w = J(1) = 2$.
>
> Elsewhere on the circle, $J' \neq 0$, so the map is conformal, and the circle maps to a smooth curve. The resulting image is closed (since the circle is closed), with a single cusp at $w = 2$ and the rest of the curve smooth — the characteristic Joukowski aerofoil shape.
>
> The "thickness" and "camber" of the aerofoil depend on the position of $z_0$:
> - Real $z_0$ (real offset): symmetric aerofoil.
> - Imaginary $z_0$ (vertical offset): cambered (asymmetric) aerofoil with curvature.
> - Larger $|z_0|$: thicker aerofoil.

> [!note]- Complete formal solution
> **(a)** On $|z| = 1$: $z = e^{i\theta}$, $J(e^{i\theta}) = e^{i\theta} + e^{-i\theta} = 2\cos\theta$. As $\theta$ ranges $[0, 2\pi)$, this traces $[-2, 2]$ twice.
>
> **(b)** On $|z| = r > 1$: $z = re^{i\theta}$, $J(re^{i\theta}) = (r + 1/r)\cos\theta + i(r - 1/r)\sin\theta$. Setting $X = (r + 1/r)\cos\theta, Y = (r - 1/r)\sin\theta$, the curve is the ellipse $X^2/(r + 1/r)^2 + Y^2/(r - 1/r)^2 = 1$.
>
> **(c)** For an off-centred circle $|z - z_0| = a$ with $z_0$ near $0$ and $a$ such that the circle passes through $z = 1$ (e.g., $z_0 = -\epsilon, a = 1 + \epsilon$): the image $J(\text{circle})$ is a closed curve with a cusp at $w = J(1) = 2$ (because $J'(1) = 0$, the Joukowski critical point) and smooth elsewhere. The cusp is the trailing edge of the aerofoil. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "conformal mapping with critical points" → "cusps in the image".** When a conformal map has a critical point on the boundary of a domain (where $f' = 0$), the image of the boundary develops a cusp at the image of that critical point. Joukowski has critical points at $z = \pm 1$, and aerofoils are obtained by passing the boundary circle through one of these critical points.

**Conformal mapping pulls back flows.** Once we have the Joukowski biholomorphism (between cylinder-exterior and aerofoil-exterior), the *flow* around the cylinder pulls back to a flow around the aerofoil. The complex potential $w_z(z) = U(z + a^2/z)$ in the $z$-plane (cylinder flow) becomes $w_\zeta(\zeta) = w_z(J^{-1}(\zeta))$ in the $\zeta$-plane (aerofoil flow).

**The Kutta condition selects the physical flow.** Among the one-parameter family of flows around the aerofoil (parameterized by circulation), the Kutta condition picks the unique one with finite velocity at the cusp. This determines the lift via the Kutta–Joukowski theorem $L = \rho U \Gamma$.

**Generalizations.**
- **Kármán–Trefftz transformation**: $J_k(z) = k\cdot((z + 1)^k + (z - 1)^k)/((z + 1)^k - (z - 1)^k)$ generalizes Joukowski, producing aerofoils with non-zero trailing-edge angle (more realistic).
- **Schwarz–Christoffel transformation**: maps the upper half-plane to a polygon, used for more general aerofoil shapes — see [[Ex - Schwarz–Christoffel for a polygon]].

**Engineering significance.** The Joukowski construction was the *first analytical model of aerofoil flow*, demonstrating that lift comes from circulation. Before Joukowski, aerodynamic forces were poorly understood and the Wright Brothers had to rely on empirical data. The mathematical theory enabled rational aerofoil design.
