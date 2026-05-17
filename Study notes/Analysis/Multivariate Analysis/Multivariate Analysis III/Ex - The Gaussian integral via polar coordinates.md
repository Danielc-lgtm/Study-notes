---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - The Change of Variables Formula"
  - "Thm - Fubini's Theorem"
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Evaluate the **Gaussian integral**
$$I = \int_{-\infty}^\infty e^{-x^2}\,dx.$$

The function $e^{-x^2}$ has no elementary antiderivative, so no one-variable method touches it. The trick is to compute $I^2$ as a double integral and change to polar coordinates.

**Recall:**

![[Thm - The Change of Variables Formula#Statement]]

[[Thm - The Change of Variables Formula|The change of variables formula]]: for a $C^1$ diffeomorphism $G : O \to \Omega$ and integrable $f$,
$$\int_\Omega f(y)\,dV(y) = \int_O f(G(x))\,|\det DG(x)|\,dV(x).$$
**Polar coordinates:** $G(r,\theta) = (r\cos\theta, r\sin\theta)$, with Jacobian matrix $DG = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}$ and Jacobian determinant $\det DG = r$. The map $G$ is a diffeomorphism from the *open* rectangle $(0,\infty)\times(0,2\pi)$ onto the plane minus a ray; it fails injectivity on the closed rectangle (the axis $r = 0$ collapses to the origin, the seam $\theta = 0 \equiv 2\pi$ is glued), but those failures occupy a [[Def - The Riemann Integral in Several Variables|nil set]] and do not affect the integral. [[Thm - Fubini's Theorem|Fubini's theorem]] reduces the double integral to iterated form.

---

# Convergent Strategy

**Problem class.** This is a *change-of-variables evaluation*: an integral made tractable by matching coordinates to a symmetry. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] prescribes choosing the coordinate system that respects the integrand's symmetry — here radial symmetry — so the integral collapses.

**Assumption pattern.** The integrand $e^{-x^2}$ is one-dimensional and elementary-antiderivative-free. The decisive move is to *raise the dimension*: $I^2 = \big(\int e^{-x^2}dx\big)\big(\int e^{-y^2}dy\big)$, and by Fubini this is the double integral $\int_{\mathbb{R}^2} e^{-x^2-y^2}\,dA$. The two-dimensional integrand $e^{-(x^2+y^2)}$ is *radially symmetric* — it depends only on $x^2 + y^2$ — which is exactly the cue for polar coordinates.

**Theorem routing.** Fubini turns $I^2$ into $\int_{\mathbb{R}^2} e^{-x^2-y^2}\,dA$. The change of variables formula with polar coordinates rewrites this as $\int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta$ — the Jacobian factor $r$ appears. The radial integral $\int_0^\infty e^{-r^2}r\,dr$ now *does* have an elementary antiderivative (substitute $s = r^2$), because the Jacobian supplied the missing factor $r$.

**Key decision point.** Two insights. First, *square the integral and go up a dimension* — the one-dimensional problem is unsolvable, the two-dimensional one is solvable, because two dimensions admits polar coordinates and one does not. Second, the Jacobian factor $r$ is not an annoyance but the *enabler*: $\int e^{-r^2}dr$ is still non-elementary, but $\int e^{-r^2}r\,dr$ is elementary, and the extra $r$ is precisely the polar Jacobian. The radial symmetry of $e^{-x^2-y^2}$ is what guarantees the $\theta$-integral is trivial.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce a multiple integral to iterated single integrals (Fubini).** $I^2$ is written as the double integral $\int_{\mathbb{R}^2}e^{-x^2-y^2}\,dA$ via the product-integrand form of Fubini.

2. **Change variables by a diffeomorphism, inserting the Jacobian.** Polar coordinates rewrite the double integral with the Jacobian factor $r$.

3. **Handle the non-injective boundary as a nil set.** Polar coordinates are a diffeomorphism only on the open rectangle; the omitted axis and seam have content zero.

4. **One-variable substitution.** The radial integral $\int_0^\infty e^{-r^2}r\,dr$ is evaluated by $s = r^2$.

---

# Hints

> [!note]- Hint 1
> You cannot integrate $e^{-x^2}$ in one variable. Instead of computing $I$, compute $I^2$. Write $I^2$ as a product of two one-variable integrals, one in $x$ and one in $y$, and combine them into a single double integral over the plane.

> [!note]- Hint 2
> $I^2 = \big(\int e^{-x^2}dx\big)\big(\int e^{-y^2}dy\big) = \int_{\mathbb{R}^2} e^{-x^2}e^{-y^2}\,dA = \int_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA$. The integrand depends only on $x^2 + y^2$ — it is radially symmetric. What coordinate system is built for radial symmetry?

> [!note]- Hint 3
> Switch to polar coordinates $x = r\cos\theta$, $y = r\sin\theta$. The Jacobian determinant is $r$, so $dA = r\,dr\,d\theta$, and $x^2 + y^2 = r^2$. The integral becomes $\int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta$.

> [!note]- Hint 4
> The radial integral $\int_0^\infty e^{-r^2}r\,dr$ — note the factor $r$ from the Jacobian — is now elementary: substitute $s = r^2$, so $r\,dr = \tfrac12\,ds$. Then take the square root at the end.

---

# Solution

One dimension cannot integrate $e^{-x^2}$; two dimensions can, because the plane admits polar coordinates and the radial symmetry of $e^{-x^2-y^2}$ makes the angular integral trivial — while the polar Jacobian supplies exactly the factor $r$ that makes the radial integral elementary.

**Step 1: Square the integral into a double integral.**

$I^2 = \displaystyle\int_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA$.

> [!note]- Derivation
> The integral $I = \int_{-\infty}^\infty e^{-x^2}\,dx$ is a finite positive number (the integrand is positive and decays faster than any power, so the improper integral converges). Its square is a product of two copies, which we may write with different dummy variables:
> $$I^2 = \left(\int_{-\infty}^\infty e^{-x^2}\,dx\right)\left(\int_{-\infty}^\infty e^{-y^2}\,dy\right).$$
> The integrand of the prospective double integral is a *product* $e^{-x^2}\cdot e^{-y^2}$, and $e^{-x^2-y^2}$ is absolutely integrable on $\mathbb{R}^2$ (it is positive and decays exponentially). By the product-integrand form of [[Thm - Fubini's Theorem|Fubini's theorem]] — for an absolutely integrable product $u(x)v(y)$, the double integral equals the product of the one-dimensional integrals — 
> $$I^2 = \int_{\mathbb{R}^2} e^{-x^2}\,e^{-y^2}\,dA = \int_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA.$$
> The crucial gain: the two-dimensional integrand $e^{-(x^2+y^2)}$ depends on $(x,y)$ only through $x^2 + y^2$ — it is **radially symmetric**.

**Step 2: Change to polar coordinates.**

$I^2 = \displaystyle\int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta$.

> [!note]- Derivation
> Polar coordinates are the map $G(r,\theta) = (r\cos\theta, r\sin\theta)$. Its Jacobian matrix and determinant are
> $$DG(r,\theta) = \begin{pmatrix}\cos\theta & -r\sin\theta\\[2pt] \sin\theta & r\cos\theta\end{pmatrix}, \qquad \det DG = r\cos^2\theta + r\sin^2\theta = r,$$
> so $|\det DG| = r$ for $r > 0$. The map $G$ is a $C^1$ diffeomorphism from the *open* rectangle $(0,\infty)\times(0,2\pi)$ onto $\mathbb{R}^2$ minus the non-negative $x$-axis. It is *not* a diffeomorphism on the closed rectangle: every point of the axis $r = 0$ maps to the origin, and $\theta = 0$ and $\theta = 2\pi$ give the same ray. But the excluded set — the origin and the positive $x$-axis — has content zero in $\mathbb{R}^2$ (a point and a ray are nil), and removing a nil set from the domain of integration does not change an integral. So the [[Thm - The Change of Variables Formula|change of variables formula]] applies on the open rectangle:
> $$I^2 = \int_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA = \int_{(0,\infty)\times(0,2\pi)} e^{-r^2}\,\underbrace{r}_{|\det DG|}\,dr\,d\theta,$$
> using $x^2 + y^2 = r^2$. By [[Thm - Fubini's Theorem|Fubini]], the double integral over the rectangle is the iterated integral
> $$I^2 = \int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta.$$

**Step 3: Evaluate the radial and angular integrals.**

$\displaystyle\int_0^\infty e^{-r^2}r\,dr = \tfrac12$, and $\displaystyle\int_0^{2\pi}d\theta = 2\pi$, so $I^2 = \pi$.

> [!note]- Derivation
> The radial integral now has the factor $r$ — supplied by the Jacobian — that makes it elementary. Substitute $s = r^2$, so $ds = 2r\,dr$, i.e. $r\,dr = \tfrac12\,ds$; as $r : 0 \to \infty$, $s : 0 \to \infty$:
> $$\int_0^\infty e^{-r^2}\,r\,dr = \int_0^\infty e^{-s}\,\tfrac12\,ds = \tfrac12\big[-e^{-s}\big]_0^\infty = \tfrac12(0 - (-1)) = \tfrac12.$$
> The integrand $e^{-r^2}r$ is independent of $\theta$, so the iterated integral separates:
> $$I^2 = \int_0^{2\pi}\left(\int_0^\infty e^{-r^2}r\,dr\right)d\theta = \int_0^{2\pi}\tfrac12\,d\theta = \tfrac12\cdot 2\pi = \pi.$$

**Step 4: Take the square root.**

$I = \sqrt{\pi}$.

> [!note]- Derivation
> $I = \int_{-\infty}^\infty e^{-x^2}\,dx$ is positive (the integrand is everywhere positive), and $I^2 = \pi$, so
> $$I = \int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}. \qquad \blacksquare$$
> As a corollary, the $n$-dimensional Gaussian integral factors: $\int_{\mathbb{R}^n} e^{-|x|^2}\,dV = \big(\int_{\mathbb{R}} e^{-x^2}dx\big)^n = \pi^{n/2}$.

> [!note]- Complete formal solution
> Let $I = \int_{-\infty}^\infty e^{-x^2}\,dx$, a finite positive number. Since $e^{-x^2-y^2}$ is absolutely integrable on $\mathbb{R}^2$, the product form of [[Thm - Fubini's Theorem|Fubini's theorem]] gives
> $$I^2 = \left(\int_{\mathbb{R}} e^{-x^2}dx\right)\left(\int_{\mathbb{R}} e^{-y^2}dy\right) = \int_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA.$$
> Polar coordinates $G(r,\theta) = (r\cos\theta, r\sin\theta)$ form a $C^1$ diffeomorphism of the open rectangle $(0,\infty)\times(0,2\pi)$ onto $\mathbb{R}^2$ minus a nil set, with $|\det DG| = r$. By the [[Thm - The Change of Variables Formula|change of variables formula]] and Fubini,
> $$I^2 = \int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta = 2\pi\int_0^\infty e^{-r^2}r\,dr = 2\pi\cdot\tfrac12 = \pi,$$
> the radial integral evaluated by $s = r^2$. Since $I > 0$, $I = \sqrt{\pi}$. $\blacksquare$

---

# Key Takeaways

**To compute an integral one dimension cannot handle, square it and go up a dimension.** The Gaussian integral $\int e^{-x^2}dx$ is unsolvable in one variable precisely because the line has no rotational symmetry to exploit. Squaring produces $\int_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA$, and the *plane* does have rotational symmetry, which polar coordinates capture. This dimension-raising trick is specific but recurring: whenever a one-variable integral resists, ask whether its square (or higher power) is a multidimensional integral with a symmetry the original lacked. The general principle is that *symmetry is a function of the ambient space* — the integrand $e^{-x^2}$ is "secretly radial" but only reveals it once embedded in $\mathbb{R}^2$.

**Match the coordinate system to the symmetry of the integrand — radial integrand, polar (or spherical) coordinates.** The trigger is an integrand depending on $(x,y)$ only through $x^2 + y^2$, or on $x \in \mathbb{R}^n$ only through $|x|$: such radial integrands become functions of $r$ alone in polar/spherical coordinates, and the angular integral collapses to the (constant) surface area. The change of variables formula is the tool that respects the symmetry, and the rule of thumb is: identify what the integrand and the domain are symmetric under, then choose coordinates adapted to that symmetry group. Radial symmetry calls for polar/spherical; translational symmetry calls for shifts; a linear deformation calls for a matrix substitution.

**The Jacobian factor is the enabler, not the obstacle — here it is exactly the missing $r$.** It is tempting to view the Jacobian $r$ as extra baggage the change of variables imposes. The opposite is true: $\int e^{-r^2}dr$ is still non-elementary, but $\int e^{-r^2}\,r\,dr$ *is* elementary, and the factor $r$ that makes the difference is precisely the polar Jacobian. The change of variables to polar coordinates did not merely simplify the integrand from $e^{-x^2-y^2}$ to $e^{-r^2}$; it also handed over the factor $r$ that the substitution $s = r^2$ needs. Watching for this — the Jacobian supplying exactly the factor a subsequent substitution requires — is a recurring pattern; it is the same phenomenon, in the $r$-direction, that makes spherical coordinates produce the $\rho^{n-1}$ that integrates the volume of a ball.

**A coordinate map that fails injectivity on a thin set is still legal — argue the failure away as nil.** Polar coordinates are not a diffeomorphism on the closed parameter rectangle: the axis $r = 0$ collapses and the seam $\theta = 0 \equiv 2\pi$ is glued. The [[Thm - The Change of Variables Formula|change of variables formula]] requires a genuine diffeomorphism, so one cannot apply it on the closed rectangle. The repair, which must be *stated* and not assumed, is that $G$ *is* a diffeomorphism on the open rectangle, and the omitted boundary — a point and a ray — has content zero, so removing it changes no integral. This same caveat attaches to spherical coordinates and every standard coordinate system; the discipline is to name the open region where the map is a true diffeomorphism and to note that what was excluded is nil.
