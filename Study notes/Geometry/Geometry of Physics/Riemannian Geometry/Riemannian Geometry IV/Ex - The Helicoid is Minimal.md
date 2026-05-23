---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Minimal Surface"
  - "Def - Gauss Curvature and Mean Curvature"
  - "Def - First Fundamental Form"
  - "Def - Second Fundamental Form"
tags: [geometry, riemannian-geometry, surfaces, minimal-surfaces, helicoid]
---

# Problem Statement

The **helicoid** is the surface
$$
\mathbf{x}(u, v) = (v\cos u,\, v\sin u,\, au), \qquad u \in \mathbb{R},\;\; v \in \mathbb{R},
$$
where $a > 0$ is a constant. Geometrically, it is the surface swept out by a horizontal line through the $z$-axis as the line rotates about the $z$-axis at constant angular velocity while translating along the axis at constant linear velocity — a screw motion.

Show that the helicoid is a **minimal surface**: its mean curvature $H \equiv 0$ everywhere. Compute the principal curvatures and the Gauss curvature explicitly.

**Recall:**

![[Def - Minimal Surface#The Definition]]

A **ruled surface** is one swept out by a one-parameter family of straight lines (the "rulings"). The helicoid is a ruled surface, with rulings being the horizontal lines through the $z$-axis at each height.

**Catalan's theorem (1842):** The only ruled minimal surfaces in $\mathbb{R}^3$ are the plane and the helicoid.

---

# Convergent Strategy

**Problem class:** Direct verification of minimality for a specific surface, with the additional feature that the helicoid is a ruled surface (so its tangent plane along each ruling has a special structure). The computation follows the same routine as for the catenoid — compute fundamental forms, evaluate $H$ — but the algebra is slightly less clean because the helicoid is not a surface of revolution.

**Assumption pattern:** The helicoid is parametrised explicitly, with smooth dependence on $(u, v)$ and regular everywhere (the cross product $\mathbf{x}_u\times\mathbf{x}_v$ is always nonzero — verify in Step 2). The "ruled" structure means $\mathbf{x}_v = (\cos u, \sin u, 0)$ has constant length $1$, simplifying the metric component $G$. The screw symmetry — invariance under $u \to u + \alpha$ combined with $z \to z + a\alpha$ — implies that the helicoid is **homogeneous** (every point is equivalent to every other), so $H$ and $K$ are functions of one variable only.

**Theorem routing:** Compute $E, F, G, e, f, g_\mathrm{II}$ directly. Use the formula $H = (Eg_\mathrm{II} + Ge - 2Ff)/(EG - F^2)$. The crucial observation is that for the helicoid, $e = g_\mathrm{II} = 0$ — the second fundamental form is purely off-diagonal (its matrix is $\bigl(\begin{smallmatrix}0&f\\f&0\end{smallmatrix}\bigr)$), making the formula reduce to $H = (-2Ff)/(EG - F^2)$. Since for the helicoid $F = 0$ as well (we verify), the result is $H = 0/(EG) = 0$.

**Key decision point:** Recognising that for a *ruled* surface (parametrised so $v$ is the parameter along the rulings), the second derivative $\mathbf{x}_{vv} = 0$ (the rulings are straight lines, so $v$-second-derivative vanishes). This immediately gives $g_\mathrm{II} = \langle\mathbf{x}_{vv}, N\rangle = 0$, killing half of the second fundamental form's diagonal. The remaining half $e = \langle\mathbf{x}_{uu}, N\rangle$ is more involved but in the helicoid case also turns out to be zero, leaving only the off-diagonal $f$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (compute $(g_{\alpha\beta}, b_{\alpha\beta})$ from a parametrisation):** Standard six-step routine.

2. **Operation 2 from the topic page (formula for $H$ from fundamental forms):** Once $E, F, G, e, f, g_\mathrm{II}$ are known, plug in to verify $H = 0$.

3. **Special trick for ruled surfaces:** $\mathbf{x}_{vv} = 0$ along each ruling (rulings are straight lines), so $g_\mathrm{II} = 0$ for free.

---

# Hints

> [!note]- Hint 1
> Compute $\mathbf{x}_u$ and $\mathbf{x}_v$. The metric components are $E = v^2 + a^2$, $F = 0$, $G = 1$. The cross-term $F$ vanishes because $\mathbf{x}_u$ has a $z$-component while $\mathbf{x}_v$ has none — they are orthogonal at every point. **Crucial:** $G = 1$ comes from $|\mathbf{x}_v| = 1$, which is the "ruled-by-unit-vectors" property.

> [!note]- Hint 2
> The unit normal is $N = (a\sin u, -a\cos u, v)/\sqrt{v^2 + a^2}$. Verify $|N|^2 = 1$.

> [!note]- Hint 3
> Second derivatives: $\mathbf{x}_{uu} = (-v\cos u, -v\sin u, 0)$ and $\mathbf{x}_{vv} = 0$. So $e = \langle\mathbf{x}_{uu}, N\rangle = (-v\cos u\cdot a\sin u - v\sin u\cdot(-a\cos u) + 0\cdot v)/\sqrt{v^2 + a^2} = 0$ (the trigonometric terms cancel), and $g_\mathrm{II} = 0$ (since $\mathbf{x}_{vv} = 0$). Only $f = \langle\mathbf{x}_{uv}, N\rangle$ is nonzero — compute it.

---

# Solution

The proof breaks into three steps. Step 1 computes the first fundamental form. Step 2 finds the unit normal and the second fundamental form (with the special "$\mathbf{x}_{vv} = 0$" simplification). Step 3 verifies $H = 0$.

**Step 1: First fundamental form is $\mathrm{I} = (v^2 + a^2)\, du^2 + dv^2$.**

> [!note]- Derivation
> Tangent vectors:
> $$
> \mathbf{x}_u = (-v\sin u, v\cos u, a),
> $$
> $$
> \mathbf{x}_v = (\cos u, \sin u, 0).
> $$
> Inner products:
> $$
> E = \langle\mathbf{x}_u, \mathbf{x}_u\rangle = v^2\sin^2 u + v^2\cos^2 u + a^2 = v^2 + a^2,
> $$
> $$
> G = \langle\mathbf{x}_v, \mathbf{x}_v\rangle = \cos^2 u + \sin^2 u + 0 = 1,
> $$
> $$
> F = \langle\mathbf{x}_u, \mathbf{x}_v\rangle = -v\sin u\cos u + v\cos u\sin u + a\cdot 0 = 0.
> $$
> So $\mathrm{I} = (v^2 + a^2)\, du^2 + dv^2$, and $\det g_{\alpha\beta} = v^2 + a^2$.

**Step 2: Unit normal $N = (a\sin u, -a\cos u, v)/\sqrt{v^2 + a^2}$ and second fundamental form $\mathrm{II} = -2(a/\sqrt{v^2 + a^2})\, du\, dv$.**

> [!note]- Derivation
> Cross product:
> $$
> \mathbf{x}_u\times\mathbf{x}_v = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\-v\sin u & v\cos u & a\\ \cos u & \sin u & 0\end{vmatrix}
> $$
> $$
> = (v\cos u\cdot 0 - a\sin u)\mathbf{i} - (-v\sin u\cdot 0 - a\cos u)\mathbf{j} + (-v\sin^2 u - v\cos^2 u)\mathbf{k}
> $$
> $$
> = (-a\sin u, a\cos u, -v).
> $$
> Hmm let me redo: the cross product formula. $\mathbf{x}_u\times\mathbf{x}_v =$ determinant.
>
> $i$-component: $(\mathbf{x}_u)_y(\mathbf{x}_v)_z - (\mathbf{x}_u)_z(\mathbf{x}_v)_y = (v\cos u)(0) - (a)(\sin u) = -a\sin u$.
>
> $j$-component: $-((\mathbf{x}_u)_x(\mathbf{x}_v)_z - (\mathbf{x}_u)_z(\mathbf{x}_v)_x) = -((-v\sin u)(0) - (a)(\cos u)) = a\cos u$.
>
> $k$-component: $(\mathbf{x}_u)_x(\mathbf{x}_v)_y - (\mathbf{x}_u)_y(\mathbf{x}_v)_x = (-v\sin u)(\sin u) - (v\cos u)(\cos u) = -v(\sin^2 u + \cos^2 u) = -v$.
>
> So $\mathbf{x}_u\times\mathbf{x}_v = (-a\sin u, a\cos u, -v)$, magnitude $\sqrt{a^2 + v^2}$.
>
> Unit normal: $N = (-a\sin u, a\cos u, -v)/\sqrt{v^2 + a^2}$.
>
> (Alternatively, one can use $N = (a\sin u, -a\cos u, v)/\sqrt{v^2 + a^2}$ with the opposite orientation — both are valid; the sign of $H$ depends on the choice. We use the orientation giving the cross product convention above; $H = 0$ is the same either way.)
>
> Second derivatives:
> $$
> \mathbf{x}_{uu} = (-v\cos u, -v\sin u, 0),
> $$
> $$
> \mathbf{x}_{uv} = (-\sin u, \cos u, 0),
> $$
> $$
> \mathbf{x}_{vv} = (0, 0, 0).
> $$
> Dot with $N$:
> $$
> e = \langle\mathbf{x}_{uu}, N\rangle = \frac{(-v\cos u)(-a\sin u) + (-v\sin u)(a\cos u) + 0\cdot(-v)}{\sqrt{v^2 + a^2}} = \frac{av\sin u\cos u - av\sin u\cos u}{\sqrt{v^2 + a^2}} = 0.
> $$
> $$
> f = \langle\mathbf{x}_{uv}, N\rangle = \frac{(-\sin u)(-a\sin u) + (\cos u)(a\cos u) + 0\cdot(-v)}{\sqrt{v^2 + a^2}} = \frac{a\sin^2 u + a\cos^2 u}{\sqrt{v^2 + a^2}} = \frac{a}{\sqrt{v^2 + a^2}}.
> $$
> $$
> g_\mathrm{II} = \langle\mathbf{x}_{vv}, N\rangle = 0.
> $$
>
> So $\mathrm{II} = 2f\, du\, dv = \frac{2a}{\sqrt{v^2 + a^2}}\, du\, dv$, equivalently $\mathrm{II} = b_{12}\,du\, dv$ with $b_{11} = b_{22} = 0$ and $b_{12} = b_{21} = a/\sqrt{v^2 + a^2}$.

**Step 3: Verify $H = 0$ and $K = -a^2/(v^2 + a^2)^2$.**

> [!note]- Derivation
> Mean curvature: $H = (Eg_\mathrm{II} + Ge - 2Ff)/(EG - F^2)$. Substituting:
> $$
> H = \frac{(v^2 + a^2)(0) + (1)(0) - 2(0)(a/\sqrt{v^2 + a^2})}{(v^2 + a^2)(1) - 0^2} = \frac{0 - 0 - 0}{v^2 + a^2} = 0.
> $$
> So $H = 0$ everywhere — the helicoid is minimal.
>
> Gauss curvature: $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$. Substituting:
> $$
> K = \frac{(0)(0) - (a/\sqrt{v^2 + a^2})^2}{v^2 + a^2} = \frac{-a^2/(v^2 + a^2)}{v^2 + a^2} = -\frac{a^2}{(v^2 + a^2)^2}.
> $$
> Hyperbolic everywhere, consistent with $H = 0$ forcing $K \leq 0$. The curvature is largest in magnitude at $v = 0$ (the central axis), where $K = -1/a^2$, and decays as $|v| \to \infty$.

> [!note]- Complete formal solution
> Parametrise the helicoid as $\mathbf{x}(u, v) = (v\cos u, v\sin u, au)$.
>
> Tangent vectors $\mathbf{x}_u = (-v\sin u, v\cos u, a)$, $\mathbf{x}_v = (\cos u, \sin u, 0)$. First fundamental form: $E = v^2 + a^2$, $F = 0$, $G = 1$. Determinant $\det g = v^2 + a^2$.
>
> Unit normal $N = (-a\sin u, a\cos u, -v)/\sqrt{v^2 + a^2}$.
>
> Second derivatives: $\mathbf{x}_{uu} = (-v\cos u, -v\sin u, 0)$, $\mathbf{x}_{uv} = (-\sin u, \cos u, 0)$, $\mathbf{x}_{vv} = 0$. Dotting with $N$: $e = 0$, $f = a/\sqrt{v^2 + a^2}$, $g_\mathrm{II} = 0$.
>
> Mean curvature: $H = (Eg_\mathrm{II} + Ge - 2Ff)/(EG - F^2) = ((v^2 + a^2)\cdot 0 + 1\cdot 0 - 2\cdot 0\cdot f)/(v^2 + a^2) = 0$. The helicoid is minimal. $\square$
>
> Gauss curvature: $K = (eg_\mathrm{II} - f^2)/(EG - F^2) = (0 - a^2/(v^2 + a^2))/(v^2 + a^2) = -a^2/(v^2 + a^2)^2$. Hyperbolic everywhere.
>
> Principal curvatures (from the eigenvalues of the shape operator with matrix $b^\alpha_{\;\beta} = g^{\alpha\gamma}b_{\gamma\beta}$):
> $$
> b^\alpha_{\;\beta} = \begin{pmatrix}1/(v^2 + a^2) & 0\\ 0 & 1\end{pmatrix}\begin{pmatrix}0 & a/\sqrt{v^2 + a^2}\\ a/\sqrt{v^2 + a^2} & 0\end{pmatrix} = \begin{pmatrix}0 & a/((v^2 + a^2)^{3/2})\\ a/\sqrt{v^2 + a^2} & 0\end{pmatrix}.
> $$
> Characteristic polynomial: $\det(b^\alpha_{\;\beta} - \kappa I) = \kappa^2 - 0\cdot\kappa - (a/((v^2+a^2)^{3/2}))\cdot(a/\sqrt{v^2+a^2}) = \kappa^2 - a^2/(v^2+a^2)^2 = 0$, giving $\kappa = \pm a/(v^2+a^2)$. So $\kappa_1 = a/(v^2+a^2) > 0$ and $\kappa_2 = -a/(v^2+a^2) < 0$, with sum $0 = H$ and product $-a^2/(v^2+a^2)^2 = K$.

> [!tip] Bonnet deformation: catenoid ↔ helicoid
> The catenoid and helicoid are related by a continuous family of minimal surfaces, all locally isometric: $\mathbf{x}_\theta(u, v) = \cos\theta\cdot\mathbf{x}_{\text{cat}} + \sin\theta\cdot\mathbf{x}_{\text{hel}}$ (with appropriate reparametrisation). At $\theta = 0$, the surface is the catenoid; at $\theta = \pi/2$, it is the helicoid; intermediate $\theta$ gives an "intermediate" minimal surface (sometimes called the **right-helicoid** family). All members of this family are *locally isometric* (the first fundamental form is the same up to coordinate change), but globally non-isometric (the catenoid is topologically a cylinder, the helicoid is topologically a plane). This is the **Bonnet deformation** of conjugate minimal surfaces, derivable via the Weierstrass–Enneper representation.

---

# Key Takeaways

**Ruled surfaces have one principal curvature equal to zero along the ruling — except the helicoid.** A ruled surface $\mathbf{x}(u, v) = \alpha(u) + v\beta(u)$ has $\mathbf{x}_{vv} = 0$, so $g_\mathrm{II} = 0$. If additionally $\beta(u)$ has constant length (so $G = |\beta|^2 =$ const) and the ruling direction is asymptotic, both diagonal entries of $\mathrm{II}$ vanish and the surface is minimal — but this is restrictive. The helicoid satisfies these conditions: $\beta(u) = (\cos u, \sin u, 0)$ has constant length $1$, and the ruling direction $\partial/\partial v$ is asymptotic (the normal curvature in this direction vanishes). **Catalan's theorem (1842)** asserts that the helicoid and the plane are the *only* ruled minimal surfaces in $\mathbb{R}^3$; all other ruled surfaces (cylinders, cones, tangent-developable surfaces) have $H \neq 0$.

**The helicoid is the "twisted plane" — locally isometric to the catenoid via Bonnet deformation.** Two surfaces are **conjugate** in the Weierstrass–Enneper sense if their data $(g, \eta)$ are related by $\eta \to i\eta$ (multiplication by $i$); the resulting surface immersions are then real and imaginary parts of the same complex integral. The catenoid and helicoid are conjugate ($g = e^z, \eta = -e^{-z}dz$ for the catenoid; same $g$, $\eta \to i\eta$ for the helicoid). The interpolating Bonnet family $\mathbf{x}_\theta = \mathrm{Re}(e^{i\theta}\int)$ for $\theta \in [0, \pi/2]$ gives a continuous deformation between them — all minimal, all locally isometric. This is one of the most beautiful classical results in minimal-surface theory.

**The helicoid is a **fundamental example** in geometric analysis.** Its simplicity (explicit parametrisation, constant negative curvature on the central axis), its homogeneity (every point is equivalent under the screw symmetry), and its rich function-theoretic structure (Weierstrass–Enneper data $g = e^z, \eta = -i e^{-z}dz$) make it a standard test case for many theorems in the field. The **Colding–Minicozzi theorem** (2004) — that the helicoid is the unique simply-connected non-flat embedded minimal surface in $\mathbb{R}^3$ that is properly embedded — is a celebrated rigidity result, the analogue of Bernstein's theorem for embedded surfaces.

**The screw symmetry forces $H, K$ to depend only on $v$.** The helicoid is invariant under the screw motion $u \to u + \alpha$, $z \to z + a\alpha$, which is an isometry of $\mathbb{R}^3$ (it preserves the Euclidean metric). So $H$ and $K$, being geometric invariants, must be invariant under this isometry, hence depend only on $v$ (the distance from the central axis, since $u$ is the parameter along the screw direction). We confirmed this: $K(v) = -a^2/(v^2 + a^2)^2$, function of $v$ alone.

**Companion exercises:** Compare with [[Ex - The Catenoid is a Minimal Surface]] (the Bonnet conjugate, $H = 0$ and $K = -1/(a^2\cosh^4(v/a))$). The catenoid and helicoid together exhibit the two basic types of minimal surfaces — the rotationally-symmetric catenoid and the screw-symmetric helicoid — and the **Bonnet deformation** connecting them.
