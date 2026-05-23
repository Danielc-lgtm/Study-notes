---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Christoffel Symbols"
  - "Def - Riemannian Metric"
  - "Def - Levi-Civita Connection"
tags: [geometry, riemannian-geometry, connections]
---

# Problem Statement

Compute the Christoffel symbols of the Levi-Civita connection of the **upper-half-plane hyperbolic metric**
$$
g = \frac{dx^2 + dy^2}{y^2}
$$
on the upper half-plane $\mathbb{H}^2 = \{(x, y) \in \mathbb{R}^2 : y > 0\}$. Verify that vertical lines $\gamma(t) = (x_0, e^t)$ and the semicircle $\gamma(t) = (R\tanh t, R\,\mathrm{sech}\,t)$ centred on the $x$-axis with radius $R$ are geodesics.

**Recall:**

The Christoffel formula for the Levi-Civita connection of a Riemannian metric $g$ in local coordinates is

![[Def - Christoffel Symbols#The Definition]]

The geodesic equation in coordinates is $\ddot\gamma^k + \Gamma^k_{ij}\,\dot\gamma^i\,\dot\gamma^j = 0$, the equation $\nabla_{\dot\gamma}\dot\gamma = 0$ written in components.

The upper-half-plane model $\mathbb{H}^2$ with metric $g = (dx^2 + dy^2)/y^2$ is one of the standard models of the hyperbolic plane. Its isometry group is the Möbius transformations $z \mapsto (az + b)/(cz + d)$ with $a, b, c, d \in \mathbb{R}$ and $ad - bc = 1$ (acting on $z = x + iy$), and its geodesics are vertical lines and semicircles centred on the $x$-axis.

---

# Convergent Strategy

**Problem class:** Direct application of the [[Def - Christoffel Symbols|Christoffel formula]] to a concrete conformally flat metric — the routine "compute the Levi-Civita connection from given metric components". The hyperbolic metric is *conformal* to the Euclidean one: $g = e^{2\rho}(dx^2 + dy^2)$ with $\rho = -\log y$. The conformal structure produces a specific pattern in the Christoffel symbols.

**Assumption pattern:** The metric is diagonal but *not* of the simple "diagonal metric" form of the round sphere — both $g_{xx}$ and $g_{yy}$ are nontrivial functions of $y$. The structural simplification: $g_{xx} = g_{yy} = 1/y^2$, so both have the same $y$-dependence, and $\partial_x g_{ij} = 0$ identically (the metric is independent of $x$, reflecting the translation Killing field $\partial_x$).

**Theorem routing:** Apply the [[Def - Christoffel Symbols|Christoffel formula]] $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ using the inverse metric $g^{xx} = g^{yy} = y^2$. Compute carefully, then substitute the proposed geodesics into the geodesic equation.

**Key decision point:** The non-obvious move is recognising that the symmetry $g_{xx} = g_{yy}$ produces a "conformal" pattern in the Christoffel symbols, with all six nonzero entries involving the same factor $1/y$ (or $-1/y$). The signs and which indices appear are determined by the symmetry, but care is needed not to forget the *symmetrisation* of the Christoffel formula in $(i, j)$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (Compute Christoffel symbols from the metric).** Apply the Christoffel formula. The conformal structure $g = e^{2\rho}\delta_{ij}$ with $\rho = -\log y$ means the only metric-derivative-with-respect-to-coordinate that is nonzero is the $y$-derivative of $1/y^2$, namely $-2/y^3$.

---

# Hints

> [!note]- Hint 1
> Write $g_{xx} = g_{yy} = 1/y^2$, $g_{xy} = 0$. The inverse is $g^{xx} = g^{yy} = y^2$.

> [!note]- Hint 2
> The metric is independent of $x$, so $\partial_x g_{ij} = 0$ for all $i, j$. The only nonzero derivative is $\partial_y g_{xx} = \partial_y g_{yy} = -2/y^3$.

> [!note]- Hint 3
> For each Christoffel symbol, only the $y$-derivative contributes. The pattern: $\Gamma^k_{ij}$ is nonzero only when an even number of the indices $(k, i, j)$ are $y$ (so the $y$-derivative of $1/y^2$ enters once, and the factor of $y^2$ from the inverse metric pulls out cleanly).

> [!note]- Hint 4
> The expected answer: $\Gamma^x_{xy} = \Gamma^x_{yx} = -1/y$, $\Gamma^y_{xx} = 1/y$, $\Gamma^y_{yy} = -1/y$, all others zero.

---

# Solution

**Plan paragraph.** The solution has three steps. Step 1 computes the inverse metric and identifies the nonzero metric derivatives. Step 2 applies the Christoffel formula systematically — the $x$-independence eliminates many terms, and the conformal structure produces a uniform pattern of $\pm 1/y$ values. Step 3 verifies the vertical line and the semicircle satisfy the geodesic equation.

**Step 1: Compute the inverse metric and derivatives.**

$g_{xx} = g_{yy} = 1/y^2$, $g_{xy} = 0$. Inverse: $g^{xx} = g^{yy} = y^2$, $g^{xy} = 0$. The only nonzero metric derivative: $\partial_y g_{xx} = \partial_y g_{yy} = -2/y^3$; $\partial_x g_{ij} = 0$ for all $i, j$.

> [!note]- Derivation
> Direct from $g_{ij} = y^{-2}\delta_{ij}$. The metric matrix is $y^{-2}I$, with inverse $y^2 I$. The $x$-derivative of any component vanishes; the $y$-derivative of $1/y^2$ is $-2/y^3$.

**Step 2: Apply the Christoffel formula.**

The formula is $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. The diagonal inverse metric means only $l = k$ contributes.

For $\Gamma^x_{ij}$ ($k = x$, so $l = x$):
$$
\Gamma^x_{ij} = \tfrac{y^2}{2}(\partial_i g_{jx} + \partial_j g_{ix} - \partial_x g_{ij}) = \tfrac{y^2}{2}(\partial_i g_{jx} + \partial_j g_{ix})
$$
(the last term vanishes since $\partial_x g_{ij} = 0$). $g_{jx} = \delta_{jx}/y^2$, with $\partial_y g_{xx} = -2/y^3$ and $\partial_x g_{xx} = 0$. So $\partial_i g_{jx}$ is nonzero only when $j = x$ and $i = y$. Thus:
- $(i, j) = (y, x)$: $\Gamma^x_{yx} = \tfrac{y^2}{2}\cdot(\partial_y g_{xx} + \partial_x g_{yx}) = \tfrac{y^2}{2}\cdot(-2/y^3 + 0) = -1/y$.
- $(i, j) = (x, y)$: by symmetry $\Gamma^x_{xy} = -1/y$.

All other $\Gamma^x_{ij}$ vanish.

For $\Gamma^y_{ij}$ ($k = y$, so $l = y$):
$$
\Gamma^y_{ij} = \tfrac{y^2}{2}(\partial_i g_{jy} + \partial_j g_{iy} - \partial_y g_{ij}).
$$
$g_{jy} = \delta_{jy}/y^2$. $\partial_i g_{jy}$ is nonzero only when $j = y$ and $i = y$. $\partial_y g_{ij}$ is nonzero when $(i, j) = (x, x)$ or $(y, y)$.
- $(i, j) = (x, x)$: $\Gamma^y_{xx} = \tfrac{y^2}{2}(0 + 0 - \partial_y g_{xx}) = \tfrac{y^2}{2}\cdot \tfrac{2}{y^3} = \tfrac{1}{y}$.
- $(i, j) = (y, y)$: $\Gamma^y_{yy} = \tfrac{y^2}{2}(\partial_y g_{yy} + \partial_y g_{yy} - \partial_y g_{yy}) = \tfrac{y^2}{2}\cdot \partial_y g_{yy} = \tfrac{y^2}{2}\cdot(-2/y^3) = -1/y$.
- $(i, j) = (x, y)$ or $(y, x)$: $\Gamma^y_{xy} = \Gamma^y_{yx} = \tfrac{y^2}{2}(\partial_x g_{yy} + \partial_y g_{xy} - \partial_y g_{xy}) = 0$.

> [!note]- Derivation
> Methodically work through each combination $(k, i, j) \in \{x, y\}^3$. The pattern: $\Gamma^k_{ij}$ is nonzero precisely when the index combination $(k, i, j)$ has either ($k = y$, $i = j = x$) — giving the third-term contribution $-\partial_y g_{xx}$, all positive after the metric factors; or one of the other patterns producing the $\pm 1/y$ values listed. The computation involves no algebra beyond substituting and tracking signs.

**Summary of nonzero Christoffel symbols:**
$$
\Gamma^x_{xy} = \Gamma^x_{yx} = -\tfrac{1}{y}, \qquad \Gamma^y_{xx} = \tfrac{1}{y}, \qquad \Gamma^y_{yy} = -\tfrac{1}{y}.
$$
All others vanish.

**Step 3a: Verify the vertical line $\gamma(t) = (x_0, e^t)$ is a geodesic.**

$\dot\gamma = (0, e^t)$, $\ddot\gamma = (0, e^t)$. Plug into the geodesic equation.
- $x$-component: $0 + 2\Gamma^x_{yx}\dot y \dot x + \Gamma^x_{yy}\dot y^2 + \cdots = 2(-1/y)\cdot e^t \cdot 0 + 0 = 0$. ✓
- $y$-component: $e^t + \Gamma^y_{yy}\dot y^2 + \Gamma^y_{xx}\dot x^2 = e^t + (-1/y)\cdot e^{2t} + (1/y)\cdot 0$.

At $\gamma(t)$, $y = e^t$, so $-(1/y)e^{2t} = -e^{2t}/e^t = -e^t$. So the $y$-component is $e^t - e^t = 0$. ✓

> [!note]- Derivation
> The curve $\gamma(t) = (x_0, e^t)$ has $\dot x = 0, \dot y = e^t, \ddot x = 0, \ddot y = e^t$. The geodesic equation in $y$: $\ddot y + \Gamma^y_{ij}\dot\gamma^i\dot\gamma^j = e^t + \Gamma^y_{yy}\dot y^2 + \Gamma^y_{xx}\dot x^2 = e^t + (-1/y)e^{2t} + 0$. At $y = e^t$: $-(1/e^t)e^{2t} = -e^t$. So $e^t - e^t = 0$. The $x$-equation is trivially zero. The vertical line at unit speed (in the hyperbolic metric) is parametrised by $y = e^t$ — at $y = e^t$ the hyperbolic speed is $|\dot\gamma|_g = |\dot y|/y = e^t/e^t = 1$.

**Step 3b: Verify the semicircle $\gamma(t) = (R\tanh t, R\,\mathrm{sech}\,t)$ is a geodesic.**

$\dot\gamma = (R\,\mathrm{sech}^2 t, -R\,\mathrm{sech}\,t\,\tanh t)$. $\ddot\gamma = (-2R\,\mathrm{sech}^2 t\,\tanh t, -R\,\mathrm{sech}\,t(1 - 2\tanh^2 t))$, using standard hyperbolic-function derivatives.

The geodesic equation $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$ at $y = R\,\mathrm{sech}\,t$.

- $x$-component: $\ddot x + 2\Gamma^x_{xy}\dot x\dot y = -2R\,\mathrm{sech}^2 t \tanh t + 2(-1/y)(R\,\mathrm{sech}^2 t)(-R\,\mathrm{sech}\,t\,\tanh t)$. The second term: $2(-1/(R\,\mathrm{sech}\,t))(R\,\mathrm{sech}^2 t)(-R\,\mathrm{sech}\,t\,\tanh t) = 2R\,\mathrm{sech}^2 t\,\tanh t$. Summing: $-2R\,\mathrm{sech}^2 t\tanh t + 2R\,\mathrm{sech}^2 t\,\tanh t = 0$. ✓

- $y$-component: $\ddot y + \Gamma^y_{xx}\dot x^2 + \Gamma^y_{yy}\dot y^2 = -R\,\mathrm{sech}\,t(1 - 2\tanh^2 t) + (1/y)R^2\,\mathrm{sech}^4 t + (-1/y)R^2\,\mathrm{sech}^2 t \tanh^2 t$. With $y = R\,\mathrm{sech}\,t$: $(1/y)R^2\,\mathrm{sech}^4 t = R\,\mathrm{sech}^3 t$ and $(1/y)R^2\,\mathrm{sech}^2 t \tanh^2 t = R\,\mathrm{sech}\,t \tanh^2 t$. So the $y$-equation is $-R\,\mathrm{sech}\,t(1 - 2\tanh^2 t) + R\,\mathrm{sech}^3 t - R\,\mathrm{sech}\,t\,\tanh^2 t$. Use $\mathrm{sech}^2 t = 1 - \tanh^2 t$: $R\,\mathrm{sech}^3 t = R\,\mathrm{sech}\,t(1 - \tanh^2 t)$. Combining: $-R\,\mathrm{sech}\,t(1 - 2\tanh^2 t) + R\,\mathrm{sech}\,t(1 - \tanh^2 t) - R\,\mathrm{sech}\,t\,\tanh^2 t = R\,\mathrm{sech}\,t[-(1 - 2\tanh^2 t) + (1 - \tanh^2 t) - \tanh^2 t] = R\,\mathrm{sech}\,t\cdot 0 = 0$. ✓

> [!note]- Derivation
> The semicircle parametrisation $\gamma(t) = (R\tanh t, R\,\mathrm{sech}\,t)$ satisfies $x^2 + y^2 = R^2\tanh^2 t + R^2\,\mathrm{sech}^2 t = R^2$, so it lies on the circle of radius $R$ centred at the origin (which intersects the upper half-plane in a semicircle from $(-R, 0)$ to $(R, 0)$). The parameter $t$ ranges over $\mathbb{R}$, with $\gamma(0) = (0, R)$ the topmost point and $\gamma(\pm\infty)$ approaching $(\pm R, 0)$. The computation above verifies both components of the geodesic equation. The unit-speed parameter is $t$ in the hyperbolic metric: $|\dot\gamma|^2_g = (\dot x^2 + \dot y^2)/y^2 = R^2(\mathrm{sech}^4 t + \mathrm{sech}^2 t \tanh^2 t)/(R^2\,\mathrm{sech}^2 t) = \mathrm{sech}^2 t + \tanh^2 t = 1$. So the parametrisation is by hyperbolic arc length.

> [!note]- Complete formal solution
> **Christoffel symbols.** The Levi-Civita Christoffel symbols of $g = (dx^2 + dy^2)/y^2$ on $\mathbb{H}^2$, computed from the formula $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ using $g^{xx} = g^{yy} = y^2$ and the only nonzero derivative $\partial_y g_{xx} = \partial_y g_{yy} = -2/y^3$:
> $$
> \Gamma^x_{xy} = \Gamma^x_{yx} = -\tfrac{1}{y}, \qquad \Gamma^y_{xx} = \tfrac{1}{y}, \qquad \Gamma^y_{yy} = -\tfrac{1}{y}.
> $$
> All other Christoffel symbols vanish.
>
> **Vertical line is a geodesic.** $\gamma(t) = (x_0, e^t)$ has $\dot x = 0, \dot y = e^t, \ddot y = e^t$. $y$-equation: $e^t + \Gamma^y_{yy}\dot y^2 = e^t - (1/e^t)(e^t)^2 = e^t - e^t = 0$. $x$-equation: trivially zero. Both vanish.
>
> **Semicircle is a geodesic.** $\gamma(t) = (R\tanh t, R\,\mathrm{sech}\,t)$. Direct substitution into both components of the geodesic equation gives zero, using $\mathrm{sech}^2 = 1 - \tanh^2$. (See Step 3b for the algebra.)
>
> Both families — vertical lines and semicircles centred on the $x$-axis — are geodesics. $\blacksquare$

---

# Key Takeaways

**Conformally flat metrics produce a uniform Christoffel pattern.** When $g = e^{2\rho}\delta_{ij}$ for a function $\rho$ (the metric is a conformal rescaling of the Euclidean metric), the Christoffel symbols have a uniform form: $\Gamma^k_{ij} = \delta^k_i\partial_j\rho + \delta^k_j\partial_i\rho - \delta_{ij}\delta^{kl}\partial_l\rho$. For the hyperbolic case $\rho = -\log y$, this gives the values $\pm 1/y$ computed above. The same formula applies to *all* conformally flat metrics — and many physically interesting metrics are conformally flat (e.g., 2-dimensional manifolds locally, the FRW spatial sections, conformal compactifications of spacetimes in general relativity). Recognising "this is a conformal rescaling" immediately gives the connection without re-doing the Christoffel formula from scratch.

**Geodesics on hyperbolic space are vertical lines and semicircles centred on $\partial\mathbb{H}^2$ — and this is a Möbius-invariant statement.** The geodesics computed here are the prototypes of hyperbolic geodesics, and they have a beautiful invariance property: the isometry group of $\mathbb{H}^2$ is the Möbius group $\mathrm{PSL}_2(\mathbb{R})$, which acts on the upper half-plane by $z \mapsto (az + b)/(cz + d)$. This group sends vertical lines and semicircles (centred on the $x$-axis) to other such curves — they are the "Möbius-invariant family" of curves. The fact that geodesics are this family is a deep statement: it says the connection-theoretic notion of geodesic (defined via $\nabla_{\dot\gamma}\dot\gamma = 0$) coincides with the symmetry-invariant notion of "lines" in hyperbolic geometry. The reusable lesson: in highly symmetric spaces, geodesics are often determined by symmetry alone, and the Christoffel computation is then a consistency check.

**The hyperbolic plane has constant negative Gaussian curvature $K = -1$.** Using Cartan's structural equations or the explicit computation, the curvature 2-form of $\mathbb{H}^2$ is $\Omega^1{}_2 = -\sigma^1 \wedge \sigma^2$ (with orthonormal coframe $\sigma^1 = dx/y, \sigma^2 = dy/y$), giving the Riemann tensor component $R^1{}_{212} = -1$ and Gaussian curvature $K = -1$. This is the canonical model of a space of constant negative curvature, and it is the prototype for the **Cartan-Hadamard theorem**: any complete simply-connected manifold of non-positive sectional curvature is diffeomorphic to $\mathbb{R}^n$ via the exponential map. $\mathbb{H}^n$ is the case of constant negative curvature, and the theorem is essentially the statement that the exponential map at any point is a global diffeomorphism.

**The recipe for any 2D metric in conformal form.** Take any 2D Riemannian metric, write it (locally) in **isothermal coordinates** as $g = e^{2\rho(x, y)}(dx^2 + dy^2)$, and the Christoffel symbols are immediately $\Gamma^k_{ij} = (\partial_i\rho)\delta^k_j + (\partial_j\rho)\delta^k_i - (\partial_k\rho)\delta_{ij}$. This works for *any* 2D metric (isothermal coordinates always exist locally on a 2-manifold, by the Korn-Lichtenstein theorem on the existence of conformal flat coordinates). The hyperbolic case $\rho = -\log y$ is one example; the round 2-sphere in stereographic coordinates is another ($\rho = -\log\bigl(\tfrac{1+x^2+y^2}{2}\bigr)$); the flat torus is yet another ($\rho = 0$, trivial). The recipe makes 2D Riemannian geometry feel uniformly computable.
