---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Geodesic"
  - "Thm - Existence and Uniqueness of Geodesics"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, geodesics, hyperbolic-geometry]
---

# Problem Statement

Let $\mathbb{H}^2 := \{(x, y) \in \mathbb{R}^2 : y > 0\}$ be the upper half-plane equipped with the Poincaré metric
$$g = \frac{dx^2 + dy^2}{y^2}.$$
Show that the [[Def - Geodesic|geodesics]] of $(\mathbb{H}^2, g)$ are exactly the **vertical lines** $\{x = x_0\}$ and the **semicircles** $\{(x, y) : (x - c)^2 + y^2 = r^2, y > 0\}$ whose centres lie on the $x$-axis.

**Recall:**

A [[Def - Geodesic|geodesic]] satisfies $\nabla_{\dot\gamma}\dot\gamma = 0$, equivalently $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$ in coordinates, with Christoffel symbols
$$\Gamma^k_{ij} = \tfrac12 g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}).$$

By [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness]], a geodesic is determined by its initial position and velocity.

---

# Convergent Strategy

**Problem class:** Identification of geodesics on a specific Riemannian manifold (the hyperbolic plane). As in [[Ex - Great Circles are the Geodesics of the Sphere]], the approach is one of three: direct ODE integration, symmetry/uniqueness, or projection. The hyperbolic plane has fewer "intrinsic" symmetries available as visible reflections than the sphere does, so we use a combined approach: compute Christoffel symbols, use the *isometry [[Def - Group|group]]* (Möbius transformations) to reduce to a single case, and integrate the ODE in that case.

**Assumption pattern:** The Poincaré metric is *conformally flat* — it equals $1/y^2$ times the Euclidean metric. Conformal flatness simplifies the Christoffel-symbol computation. The metric is also invariant under horizontal translations $(x, y) \mapsto (x + a, y)$, dilations $(x, y) \mapsto (\lambda x, \lambda y)$, and (less obviously) inversions. The isometry group is $\mathrm{PSL}(2, \mathbb{R})$ acting by Möbius transformations, transitively on $\mathbb{H}^2$.

**Theorem routing:** Two approaches combined. **First**, compute $\Gamma^k_{ij}$ for the Poincaré metric. **Second**, observe that vertical lines satisfy the geodesic equation directly. **Third**, use the isometry group: any semicircle is the image of a vertical line under some Möbius transformation, so semicircles are also geodesics. **Fourth**, use uniqueness: every initial-data pair $(p, v)$ determines a unique geodesic, and the family of vertical-line-or-semicircle parametrisations covers all initial data.

**Key decision point:** The decision is whether to integrate the geodesic ODE directly (laborious) or to use the conformal-flatness to extract conservation laws. The cleanest method uses *Killing vector fields* (horizontal translation and a less obvious second symmetry coming from $\mathrm{PSL}(2, \mathbb{R})$) — but for a first analysis the direct computation suffices and reveals the conserved quantity along the way.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the geodesic equation in coordinates).** We compute Christoffel symbols of the Poincaré metric and write down the geodesic equations in $(x, y)$ coordinates.

2. **Operation 2 from the topic page (use a Killing vector field).** Horizontal translation gives a Killing field $\partial_x$, producing the conserved quantity $g(\dot\gamma, \partial_x) = \dot x / y^2$. This conservation law is one of two needed to integrate the ODE; energy conservation $|\dot\gamma|^2 = 1$ is the other.

3. **Operation 3 from the topic page (exploit uniqueness to identify a geodesic).** For *vertical* geodesics we can use uniqueness directly: a reflection $x \mapsto -x$ around $x_0 = 0$ is an isometry fixing the initial data $(0, y_0; 0, \dot y_0)$, so the geodesic must lie on the fixed-point set $\{x = 0\}$.

---

# Hints

> [!note]- Hint 1
> Compute the Christoffel symbols of $g = (dx^2 + dy^2)/y^2$. The conformal-flatness simplifies the computation — there are only three non-zero $\Gamma^k_{ij}$ (after symmetry $\Gamma^k_{ij} = \Gamma^k_{ji}$).

> [!note]- Hint 2
> Vertical lines $x = x_0$ are geodesics: try $\gamma(t) = (x_0, e^t)$ or more generally $\gamma(t) = (x_0, y(t))$ for some function $y$.

> [!note]- Hint 3
> The metric is translation-invariant in $x$, so $\partial_x$ is a Killing vector field, and $g(\dot\gamma, \partial_x) = \dot x / y^2$ is conserved along every geodesic. Combined with $|\dot\gamma|^2 = (\dot x^2 + \dot y^2)/y^2 = \mathrm{const}$ (constant speed), this gives two conservation laws.

> [!note]- Hint 4
> Use the two conservation laws to derive the trajectory in the $(x, y)$-plane. Eliminating $t$: the trajectory satisfies a relation between $x$ and $y$. Solve to show it's a vertical line ($\dot x = 0$ case) or a semicircle ($\dot x \neq 0$ case).

---

# Solution

The proof has three steps. **Step 1** computes the Christoffel symbols. **Step 2** verifies vertical lines are geodesics directly. **Step 3** uses conservation laws to derive the general case: non-vertical geodesics are semicircles centred on the $x$-axis.

**Step 1: Christoffel symbols of the Poincaré metric.**

> [!note]- Derivation
> With $g_{ij} = y^{-2}\delta_{ij}$ and $g^{ij} = y^2 \delta^{ij}$, compute:
> - $\partial_x g_{ij} = 0$ for all $i, j$ (metric is $x$-independent).
> - $\partial_y g_{xx} = \partial_y g_{yy} = -2 y^{-3}$, and $\partial_y g_{xy} = 0$.
>
> Apply $\Gamma^k_{ij} = \tfrac12 g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$:
> - $\Gamma^x_{xx} = \tfrac12 g^{xx}(2\partial_x g_{xx} - \partial_x g_{xx}) = 0$.
> - $\Gamma^x_{xy} = \tfrac12 g^{xx}(\partial_x g_{yx} + \partial_y g_{xx} - \partial_x g_{xy}) = \tfrac12 \cdot y^2 \cdot (0 + (-2y^{-3}) - 0) = -1/y$.
> - $\Gamma^x_{yy} = \tfrac12 g^{xx}(2\partial_y g_{yx} - \partial_x g_{yy}) = 0$.
> - $\Gamma^y_{xx} = \tfrac12 g^{yy}(2\partial_x g_{xy} - \partial_y g_{xx}) = \tfrac12 \cdot y^2 \cdot (0 - (-2y^{-3})) = 1/y$.
> - $\Gamma^y_{xy} = \tfrac12 g^{yy}(\partial_x g_{yy} + \partial_y g_{xy} - \partial_y g_{xy}) = 0$.
> - $\Gamma^y_{yy} = \tfrac12 g^{yy}(2\partial_y g_{yy} - \partial_y g_{yy}) = \tfrac12 \cdot y^2 \cdot (-2y^{-3}) = -1/y$.
>
> So the nonzero Christoffel symbols are
> $$\Gamma^x_{xy} = \Gamma^x_{yx} = -1/y, \qquad \Gamma^y_{xx} = 1/y, \qquad \Gamma^y_{yy} = -1/y.$$
>
> The geodesic equations are
> $$\ddot x + 2 \Gamma^x_{xy}\dot x \dot y = \ddot x - \frac{2 \dot x \dot y}{y} = 0,$$
> $$\ddot y + \Gamma^y_{xx}\dot x^2 + \Gamma^y_{yy}\dot y^2 = \ddot y + \frac{\dot x^2 - \dot y^2}{y} = 0.$$

**Step 2: vertical lines are geodesics.**

> [!note]- Derivation
> Try $\gamma(t) = (x_0, y(t))$ with $\dot x = 0$. The first equation gives $\ddot x = 0$ ✓. The second equation becomes $\ddot y - \dot y^2/y = 0$, i.e., $\ddot y = \dot y^2/y$.
>
> Solve: let $u = \dot y$. Then $\dot u = \ddot y = u^2/y$, so $\frac{du}{u^2} = \frac{dy}{y \cdot u} \cdot u = \frac{dy}{y}$. So $-1/u = -1/u(0) - \ln(y/y_0) \cdot$ wait, let me redo this. We have $\ddot y / \dot y^2 = 1/y$. Integrating: $\frac{d}{dt}(-1/\dot y) = \dot y/y$, so... another approach: try $\gamma(t) = (x_0, y_0 e^{\dot y_0 t / y_0})$ — so $y(t) = y_0 e^{at}$ with $a = \dot y_0/y_0$. Then $\dot y = a y$, $\ddot y = a^2 y$, and $\dot y^2/y = a^2 y$. ✓ The geodesic equation is satisfied.
>
> So vertical lines, parametrised as $\gamma(t) = (x_0, y_0 e^{at})$ for constants $x_0, y_0 > 0, a \in \mathbb{R}$, are geodesics. Constant speed: $|\dot\gamma|^2 = \dot y^2/y^2 = a^2$ — constant, consistent with the geodesic property of constant speed.

**Step 3: non-vertical geodesics are semicircles centred on the $x$-axis.**

> [!note]- Derivation
> Conservation laws.
>
> *Killing field $\partial_x$.* Since $g$ is $x$-independent, $\partial_x$ is a Killing field, and $C := g(\dot\gamma, \partial_x) = g_{xx}\dot x = \dot x/y^2$ is conserved.
>
> *Energy.* $E := |\dot\gamma|^2 = (\dot x^2 + \dot y^2)/y^2$ is conserved (geodesics have constant speed).
>
> For a non-vertical geodesic, $\dot x \neq 0$, so $C \neq 0$. We can derive the trajectory equation:
> $$\frac{dy}{dx} = \frac{\dot y}{\dot x}.$$
> From the two conservation laws:
> $$\dot x = C y^2, \qquad E y^2 = \dot x^2 + \dot y^2 \implies \dot y^2 = E y^2 - C^2 y^4.$$
> So
> $$\left(\frac{dy}{dx}\right)^2 = \frac{\dot y^2}{\dot x^2} = \frac{E y^2 - C^2 y^4}{C^2 y^4} = \frac{E - C^2 y^2}{C^2 y^2}.$$
> Let $r := \sqrt{E}/|C|$ (a constant). Then
> $$\left(\frac{dy}{dx}\right)^2 = \frac{r^2 - y^2}{y^2}, \qquad\text{i.e.,}\qquad \frac{dy}{y\sqrt{(r^2 - y^2)/y^2}} = \pm dx, \qquad \frac{y\, dy}{\sqrt{r^2 - y^2}} = \pm y \cdot dx.$$
>
> Hmm, let me redo this. From $(dy/dx)^2 \cdot y^2 = r^2 - y^2$, we get $y^2 (dy)^2 + y^2 (dx)^2 \cdot \text{adjustment}$... let me try again.
>
> From $(dy/dx)^2 = (r^2 - y^2)/y^2$:
> $$y \, dy = \pm \sqrt{r^2 - y^2}\, dx.$$
> Square and combine: $y^2\, dy^2 = (r^2 - y^2)\, dx^2$, i.e., $y^2(dy^2 + dx^2) = r^2\, dx^2$ (adding $y^2 dx^2$ to both sides). Hmm, this doesn't quite work either.
>
> Let me try the substitution $y = r \sin\theta$ directly. Then $dy = r\cos\theta\, d\theta$, and $\sqrt{r^2 - y^2} = r\cos\theta$. So
> $$\frac{r\sin\theta \cdot r\cos\theta\, d\theta}{r\cos\theta} = \pm dx, \qquad r\sin\theta\, d\theta = \pm dx, \qquad x - x_0 = \mp r\cos\theta.$$
> So $x - x_0 = \mp\sqrt{r^2 - y^2}$, i.e., $(x - x_0)^2 = r^2 - y^2$, i.e.,
> $$(x - x_0)^2 + y^2 = r^2.$$
>
> This is a circle of radius $r$ centred at $(x_0, 0)$ on the $x$-axis. Since $y > 0$, the geodesic is the upper semicircle.

**Step 4: uniqueness check.**

> [!note]- Derivation
> Every initial data $(p, v) \in T\mathbb{H}^2$ is realised by a vertical-line geodesic (if $v$ is vertical, i.e., $\dot x = 0$) or a semicircle geodesic (otherwise — choose the unique semicircle through $p$ tangent to $v$ at $p$).
>
> By [[Thm - Existence and Uniqueness of Geodesics|uniqueness]], these are *the* geodesics. So the geodesics of $\mathbb{H}^2$ are exactly the vertical lines and the upper semicircles centred on the $x$-axis.

> [!note]- Complete formal solution
> **Claim.** The geodesics of $(\mathbb{H}^2, g)$ with $g = (dx^2 + dy^2)/y^2$ are exactly:
> - The vertical lines $\{x = x_0\}$, with parametrisations $\gamma(t) = (x_0, y_0 e^{at})$ for $a \in \mathbb{R}$;
> - The upper semicircles $\{(x, y) : (x - x_0)^2 + y^2 = r^2, y > 0\}$ centred on the $x$-axis at $(x_0, 0)$ with radius $r > 0$, with appropriate constant-speed parametrisations.
>
> *Proof.* The Christoffel symbols of $g$ are computed in Step 1: nonzero ones are $\Gamma^x_{xy} = \Gamma^x_{yx} = -1/y$, $\Gamma^y_{xx} = 1/y$, $\Gamma^y_{yy} = -1/y$.
>
> The geodesic equations are
> $$\ddot x - 2\dot x \dot y/y = 0, \qquad \ddot y + (\dot x^2 - \dot y^2)/y = 0.$$
>
> Vertical lines: with $\dot x = 0$, the first equation is satisfied, and the second becomes $\ddot y - \dot y^2/y = 0$, with general solution $y(t) = y_0 e^{at}$ for $a = \dot y_0/y_0$. So vertical lines parametrised exponentially in $y$ are geodesics.
>
> Non-vertical geodesics: use the conservation laws $C = \dot x/y^2$ (from Killing field $\partial_x$) and $E = (\dot x^2 + \dot y^2)/y^2$ (constant speed). Eliminate $t$: $(dy/dx)^2 = (E - C^2 y^2)/(C^2 y^2)$. Set $r := \sqrt E/|C|$; substitute $y = r\sin\theta$ to integrate. The trajectory satisfies $(x - x_0)^2 + y^2 = r^2$ — the upper semicircle of radius $r$ centred at $(x_0, 0)$ on the $x$-axis.
>
> By [[Thm - Existence and Uniqueness of Geodesics|uniqueness]], every initial data is realised by exactly one of these — vertical line or semicircle — so the geodesics are exactly the curves described. $\qquad\blacksquare$

---

# Key Takeaways

**Killing fields produce conservation laws that integrate the geodesic ODE.** The Poincaré metric is $x$-translation-invariant, so $\partial_x$ is a Killing field. By Noether's theorem (applied to the energy functional or directly via $X g(\dot\gamma, \partial_x) = g(\nabla_X \partial_x, \dot\gamma) + g(\partial_x, \nabla_X \dot\gamma)$ and the geodesic equation), $g(\dot\gamma, \partial_x) = \dot x/y^2$ is conserved. This conservation law, combined with energy conservation $|\dot\gamma|^2 = \mathrm{const}$, is enough to integrate the geodesic ODE in $\mathbb{H}^2$. **The general pattern: $n$ Killing fields plus the energy conservation give $n + 1$ conservation laws on a $2n$-dimensional cotangent bundle, and $n + 1$ first integrals on a $2n$-D system reduce to an $(n - 1)$-D problem.** For $n = 2$ (the hyperbolic plane), this leaves a $0$-dimensional problem — the trajectory is determined algebraically by the conservation laws, which is what we found.

**Conformal flatness of the metric makes the Christoffel computation efficient.** A metric of the form $g = \rho^2 \delta$ (conformally flat with conformal factor $\rho$) has Christoffel symbols expressible purely in terms of $\rho$ and its derivatives — no need for the full $g^{kl}(\partial g + \partial g - \partial g)$ formula. The Poincaré metric has $\rho = 1/y$, so derivatives of $\rho$ involve only $y$, and the Christoffels are $\Gamma \sim 1/y$ (up to signs). The same trick applies to all stereographic, conformal, and isothermal coordinate systems — when the metric is in this form, Christoffel computation is one step rather than the full formula.

**The isometry group $\mathrm{PSL}(2, \mathbb{R})$ acts by Möbius transformations.** The vertical-line geodesics and semicircle geodesics are not isolated cases — they are related by [[Def - Isometry|isometries]]. The map $(x, y) \mapsto (-1/(x + iy))$ (an inversion through a point on the $x$-axis, after some Möbius simplification) sends a vertical line to a semicircle. So the full isometry group acts on the set of geodesics, and identifying *one* geodesic type (vertical lines, the easy case) plus the isometry group action gives all geodesics. This is the cleanest way to handle hyperbolic geometry: identify the isometry group, find one geodesic, apply the group to get all of them. The same pattern works for the disk model and for higher-dimensional hyperbolic spaces $\mathbb{H}^n$.

**Geodesics of $\mathbb{H}^2$ have no conjugate points.** Sectional curvature of $\mathbb{H}^2$ is $-1$ everywhere, and by the [[Thm - Jacobi Equation and Conjugate Points|Jacobi-equation analysis]], non-positive curvature forbids conjugate points. So *every* geodesic of $\mathbb{H}^2$ is the unique length-minimising curve between any two of its points, and the exponential map $\exp_p : T_p \mathbb{H}^2 \to \mathbb{H}^2$ is a global [[Def - Diffeomorphism|diffeomorphism]] (Cartan–Hadamard, see [[Riemannian Geometry III — Riemann Curvature and Topology]]). This is the deep structural fact that makes hyperbolic space behave so cleanly.
