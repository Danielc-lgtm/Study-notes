---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Volume, Area, Length Elements and Flux Integrals"
  - "Def - Integration of Forms and the Volume Element"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. Use inertial spherical coordinates $(t, r, \theta, \varphi)$, in which the line element is $\mathrm{d}s^2 = \mathrm{d}t^2 - \mathrm{d}r^2 - r^2\mathrm{d}\theta^2 - r^2\sin^2\theta\,\mathrm{d}\varphi^2$.

1. Compute the metric components $g_{\mu\nu}$ and $\sqrt{|g|}$.
2. **Length.** For the radial curve $\theta = \mathrm{const}$, $\varphi = \mathrm{const}$, $t = \mathrm{const}$ (a spacelike curve parametrised by $r$), find the length element $\mathrm{d}\ell$ and confirm $\mathrm{d}\ell = \mathrm{d}r$. Compute the length from $r=0$ to $r=R$.
3. **Area.** For the sphere $t = 0$, $r = R$ (a spacelike 2-surface), find the area element $\mathrm{d}S$ and confirm $\mathrm{d}S = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$. Compute the total area.
4. **Volume.** For the spatial ball $t = 0$, $r \le R$ (a hypersurface region), find the volume element $\mathrm{d}V$ and confirm $\mathrm{d}V = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$. Compute the total volume.

**Recall:**

The length, area, and volume elements are defined as follows.

![[Def - Volume, Area, Length Elements and Flux Integrals#The Definition]]

For a spacelike curve, $\mathrm{d}\ell = \|\mathrm{d}\vec{\ell}\|_g = \sqrt{|\mathrm{d}\vec{\ell}\cdot\mathrm{d}\vec{\ell}|}$. For a hypersurface with future unit normal $\vec{n}$, $\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$. For a spacelike 2-surface with orthonormal normal pair $(\vec{n}, \vec{s})$, $\mathrm{d}S = (n^0 s^1 - n^1 s^0)\sqrt{|g|}\,\mathrm{d}x^2\mathrm{d}x^3$.

---

# Convergent Strategy

**Problem class.** A *compute-an-integral-over-a-region* drill across all three lower dimensions, exercising the volume-form constructions of [[Def - Volume, Area, Length Elements and Flux Integrals]] on the most familiar metric.

**Assumption pattern.** A single coordinate system adapted to three nested submanifolds (radial curve, sphere, ball), and a metric whose determinant gives $\sqrt{|g|} = r^2\sin\theta$. The signpost is that each submanifold is a coordinate slice in spherical coordinates, so the appropriate $p$-form is read off directly.

**Theorem routing.** Each part applies the relevant formula from [[Def - Volume, Area, Length Elements and Flux Integrals]]: $\mathrm{d}\ell = \|\mathrm{d}\vec{\ell}\|_g$ for the curve, $\mathrm{d}S = (n^0s^1-n^1s^0)\sqrt{|g|}\,\mathrm{d}x^2\mathrm{d}x^3$ for the surface, $\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$ for the hypersurface. The normals are the normalised coordinate basis vectors.

**Key decision point.** The only subtlety is normalising the coordinate basis vectors to get the unit normals: $\vec{e}_r$ has $\vec{e}_r\cdot\vec{e}_r = -1$ already (unit), but $\vec{e}_\theta$ has $\vec{e}_\theta\cdot\vec{e}_\theta = -r^2$ (not unit). Since the area and volume formulas already include $\sqrt{|g|}$, the coordinate normals' time components $n^0 = 1$ suffice and the metric factor handles the rest — recognising this avoids double-counting normalisation factors.

---

# Legal Operations Used

1. **Operation 3 from the topic page (build the submanifold's volume form from its normals).** Each part constructs the appropriate $p$-form ($\mathrm{d}\ell$, $\mathrm{d}S$, $\mathrm{d}V$) for its submanifold.

2. **Operation 1 from the topic page (write the four-volume element as $\sqrt{|g|}\,\mathrm{d}^4x$).** The factor $\sqrt{|g|} = r^2\sin\theta$, computed once in part 1, feeds the area and volume elements.

---

# Hints

> [!note]- Hint 1
> The metric is diagonal: $g_{tt}=1$, $g_{rr}=-1$, $g_{\theta\theta}=-r^2$, $g_{\varphi\varphi}=-r^2\sin^2\theta$. The determinant is $g = 1\cdot(-1)\cdot(-r^2)\cdot(-r^2\sin^2\theta) = -r^4\sin^2\theta$, so $\sqrt{|g|} = r^2\sin\theta$.

> [!note]- Hint 2
> Along the radial curve only $r$ varies, so $\mathrm{d}\vec{\ell} = \mathrm{d}r\,\vec{e}_r$ and $\mathrm{d}\vec{\ell}\cdot\mathrm{d}\vec{\ell} = g_{rr}\,\mathrm{d}r^2 = -\mathrm{d}r^2$, giving $\mathrm{d}\ell = \sqrt{|-\mathrm{d}r^2|} = \mathrm{d}r$.

> [!note]- Hint 3
> For the sphere, the normal pair is $\vec{n} = \vec{e}_0 = (1,0,0,0)$ (timelike) and $\vec{s} = \vec{e}_r = (0,1,0,0)$ (spacelike unit, since $\vec{e}_r\cdot\vec{e}_r=-1$). Then $n^0 s^1 - n^1 s^0 = 1$, and $\mathrm{d}S = 1\cdot\sqrt{|g|}\,\mathrm{d}\theta\,\mathrm{d}\varphi = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$ at $r=R$.

> [!note]- Hint 4
> For the ball, the hypersurface is $t=0$ with normal $\vec{n}=\vec{e}_0$, $n^0=1$, so $\mathrm{d}V = \sqrt{|g|}\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$.

---

# Solution

Everything follows from one computation — $\sqrt{|g|} = r^2\sin\theta$ — and reading off the appropriate $p$-form for each submanifold. The plan: compute the metric determinant; then for the radial curve, sphere, and ball in turn, write the length, area, and volume element and integrate.

**Step 1: $\sqrt{|g|} = r^2\sin\theta$.**

> [!note]- Derivation
> The metric is diagonal with $g_{tt} = 1$, $g_{rr} = -1$, $g_{\theta\theta} = -r^2$, $g_{\varphi\varphi} = -r^2\sin^2\theta$. The determinant is the product of the diagonal entries:
> $$g = (1)(-1)(-r^2)(-r^2\sin^2\theta) = -r^4\sin^2\theta .$$
> Hence $\sqrt{|g|} = \sqrt{r^4\sin^2\theta} = r^2\sin\theta$ (taking $\sin\theta\ge 0$ on $[0,\pi]$ and $r\ge 0$). This single factor will supply the geometry for the area and volume elements.

**Step 2: Length element $\mathrm{d}\ell = \mathrm{d}r$; radial length $R$.**

> [!note]- Derivation
> Along the radial curve ($t,\theta,\varphi$ fixed), the displacement is $\mathrm{d}\vec{\ell} = \mathrm{d}r\,\vec{e}_r$, so
> $$\mathrm{d}\vec{\ell}\cdot\mathrm{d}\vec{\ell} = g_{rr}\,(\mathrm{d}r)^2 = -(\mathrm{d}r)^2 ,$$
> a negative number (the curve is spacelike). The length element is $\mathrm{d}\ell = \|\mathrm{d}\vec{\ell}\|_g = \sqrt{|{-}(\mathrm{d}r)^2|} = \mathrm{d}r$. Integrating from $r=0$ to $r=R$,
> $$\ell = \int_0^R\mathrm{d}r = R .$$
> The radial coordinate measures proper distance directly, as expected: $\vec{e}_r$ is already a unit vector.

**Step 3: Area element $\mathrm{d}S = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$; total area $4\pi R^2$.**

> [!note]- Derivation
> The sphere $t=0$, $r=R$ is a spacelike 2-surface. Its tangent directions are $\vec{e}_\theta, \vec{e}_\varphi$; the orthogonal complement $\Pi^\perp$ is spanned by the orthonormal pair $\vec{n} = \vec{e}_0 = (1,0,0,0)$ (timelike, $\vec{n}\cdot\vec{n}=+1$) and $\vec{s} = \vec{e}_r = (0,1,0,0)$ (spacelike unit, $\vec{s}\cdot\vec{s}=g_{rr}=-1$), with $\vec{n}\cdot\vec{s}=0$. Then $n^0 s^1 - n^1 s^0 = 1\cdot1 - 0\cdot0 = 1$, and with $\sqrt{|g|} = R^2\sin\theta$ at $r=R$,
> $$\mathrm{d}S = (n^0 s^1 - n^1 s^0)\sqrt{|g|}\,\mathrm{d}\theta\,\mathrm{d}\varphi = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi .$$
> Integrating,
> $$S = \int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi\,R^2 = 2\cdot2\pi\cdot R^2 = 4\pi R^2 ,$$
> the standard sphere area.

**Step 4: Volume element $\mathrm{d}V = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$; total volume $\frac{4}{3}\pi R^3$.**

> [!note]- Derivation
> The spatial ball $t=0$, $r\le R$ lies in the hypersurface $t=0$, whose future timelike unit normal is $\vec{n} = \vec{e}_0$, $n^0 = 1$. The volume element is
> $$\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi ,$$
> the standard spatial volume element. Integrating over the ball,
> $$V = \int_0^R r^2\,\mathrm{d}r\int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi = \frac{R^3}{3}\cdot2\cdot2\pi = \frac{4}{3}\pi R^3 .$$
> All three elementary geometric formulas — radial length $R$, sphere area $4\pi R^2$, ball volume $\frac{4}{3}\pi R^3$ — emerge from the single metric factor $\sqrt{|g|} = r^2\sin\theta$ and the appropriate $p$-form.

> [!note]- Complete formal solution
> The metric is $\mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$, so $g = -r^4\sin^2\theta$ and $\sqrt{|g|}=r^2\sin\theta$. *Length:* along the radial curve $\mathrm{d}\vec{\ell}=\mathrm{d}r\,\vec{e}_r$, $\mathrm{d}\vec{\ell}\cdot\mathrm{d}\vec{\ell}=-\mathrm{d}r^2$, $\mathrm{d}\ell=\mathrm{d}r$, $\ell=\int_0^R\mathrm{d}r=R$. *Area:* sphere $r=R$, normals $\vec{n}=\vec{e}_0$, $\vec{s}=\vec{e}_r$, $n^0s^1-n^1s^0=1$, $\mathrm{d}S=R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$, $S=4\pi R^2$. *Volume:* ball $r\le R$, $\vec{n}=\vec{e}_0$, $n^0=1$, $\mathrm{d}V=r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$, $V=\frac{4}{3}\pi R^3$. $\blacksquare$

---

# Key Takeaways

**One metric determinant gives every lower-dimensional measure.** The factor $\sqrt{|g|} = r^2\sin\theta$, computed once from the metric, supplies the area element ($R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$), the volume element ($r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$), and — through the line element — the length element ($\mathrm{d}r$). This is the practical payoff of the uniform "$\epsilon_{\mathscr{V}}$ from the normals" construction: you do not memorise three separate formulas for length, area, and volume in each coordinate system; you compute $\sqrt{|g|}$ once and read off the appropriate $p$-form. The trigger is any integral over a submanifold in a given coordinate system — start by computing the metric determinant. The same recipe works unchanged in cylindrical, oblate-spheroidal, or any curvilinear coordinates, and in curved spacetime where $\sqrt{|g|}$ encodes genuine geometry rather than just a coordinate choice.

**Watch which coordinate basis vectors are already unit and which are not.** In spherical coordinates $\vec{e}_r$ is a unit vector ($\vec{e}_r\cdot\vec{e}_r = -1$) but $\vec{e}_\theta$ and $\vec{e}_\varphi$ are not ($\vec{e}_\theta\cdot\vec{e}_\theta = -r^2$). The subtlety, and a common source of double-counting, is that the area and volume *formulas already contain* $\sqrt{|g|}$, which accounts for the non-unit tangent vectors, so you must *not* additionally rescale them — you only need the *normal* directions' components ($n^0$, $s^1$), which for the coordinate normals are simply $1$. Recognising that the $\sqrt{|g|}$ factor and the normal components play complementary, non-overlapping roles is what keeps the computation clean. The general lesson: when a formula bundles the metric factor, supply only the normalised normals and let $\sqrt{|g|}$ handle the tangential geometry.

**The radial coordinate measures proper distance, but the angular ones do not — this is the metric talking.** That $\mathrm{d}\ell = \mathrm{d}r$ along a radial line but the angular displacement $\mathrm{d}\theta$ corresponds to proper length $r\,\mathrm{d}\theta$ is the elementary face of a deep fact: coordinates are labels, and only the metric converts coordinate differences into physical lengths. The factor $r$ relating $\mathrm{d}\theta$ to arc length is exactly $\sqrt{|g_{\theta\theta}|}$, and the same structure — coordinate intervals weighted by metric components — governs every length, area, and volume in the chapter and in general relativity, where the weighting factors carry the gravitational field. Recognising "coordinate interval times $\sqrt{|g_{\text{that direction}}|}$ = proper length" is the portable insight, and it is why one must always pass through the metric rather than reading lengths off coordinates directly.
