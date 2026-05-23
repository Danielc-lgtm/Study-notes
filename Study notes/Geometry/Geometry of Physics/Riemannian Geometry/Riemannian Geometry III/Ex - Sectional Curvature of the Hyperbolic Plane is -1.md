---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Sectional Curvature"
  - "Def - The Hyperbolic Space H^n"
  - "Def - Constant Sectional Curvature"
tags: [geometry, riemannian-geometry, hyperbolic-geometry]
---

# Problem Statement

Let $H^2$ denote the upper half-plane $\{(x, y) \in \mathbb{R}^2 : y > 0\}$ equipped with the **Poincaré metric**
$$g = \frac{dx^2 + dy^2}{y^2}.$$
Show that $H^2$ has constant Gauss curvature $K \equiv -1$. (Equivalently, in arbitrary dimension, the hyperbolic $n$-space $H^n$ with the analogous upper-half-space metric has constant sectional curvature $-1$.)

**Recall:**

The [[Def - Sectional Curvature|Gauss curvature]] of a $2$-dimensional Riemannian manifold is the unique sectional curvature (only one $2$-plane at each point), and it can be computed from Cartan's structural equations in an orthonormal coframe via the formula $d\omega^1_{\;2} = K\,\sigma^1 \wedge \sigma^2$ where $\sigma^1, \sigma^2$ is the dual coframe and $\omega^1_{\;2}$ is the unique skew-symmetric connection 1-form.

The metric $g = (dx^2 + dy^2)/y^2$ on the upper half-plane is **conformally flat** (a positive function times the Euclidean metric), with conformal factor $1/y^2$.

---

# Convergent Strategy

**Problem class:** Sectional curvature computation on a specific Riemannian manifold via Cartan's structural equations. The conformal-flatness of the Poincaré metric makes this approach particularly clean: pick an orthonormal coframe scaled appropriately by $1/y$, solve the first structural equation for the connection 1-form, take exterior derivative, read off $K$.

**Assumption pattern:** The Poincaré metric is **conformally flat** ($g = \rho^2(\text{Euclidean})$ with $\rho = 1/y$), so the orthonormal coframe is just the rescaled coordinate coframe: $\sigma^1 = dx/y$, $\sigma^2 = dy/y$. Conformal flatness is the assumption that makes Cartan's method completely mechanical here.

**Theorem routing:** Cartan's structural equations in the orthonormal coframe: (a) First structural equation $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$, combined with skew-symmetry $\omega_{ab} = -\omega_{ba}$, uniquely determines the connection 1-form $\omega^1_{\;2}$. (b) Compute $d\omega^1_{\;2}$ and use the dimension-$2$ identity $d\omega^1_{\;2} = K\sigma^1 \wedge \sigma^2$ to read off $K$.

**Key decision point:** The choice of orthonormal coframe. For a conformally-flat metric $g = \rho^2 \bar g$ on $\mathbb{R}^2$, the orthonormal coframe is $\sigma^a = \rho\, d\bar x^a$ for $\bar x^a$ Euclidean coordinates. The non-obvious move is recognising that $d\sigma^1 = d(dx/y) = -dy \wedge dx/y^2 = (dx \wedge dy)/y^2$ requires using the chain rule on $1/y$, and that the connection 1-form $\omega^1_{\;2}$ comes out proportional to $dx/y$ — a quantity homogeneous of degree $-1$ in $y$.

---

# Legal Operations Used

1. **Operation 3 from the topic page (Cartan's structural equations in an orthonormal coframe).** The whole calculation is an application of this operation. For dimension $2$, the equation $\Omega^1_{\;2} = d\omega^1_{\;2}$ reduces to a single 1-form differentiation.

2. **Operation 4 from the topic page (descend from $R$ to $K$).** In dimension $2$, $K$ is the unique sectional curvature, and $K = R^1_{\;212}$ in an orthonormal frame.

---

# Hints

> [!note]- Hint 1
> Set up an orthonormal coframe for the conformally-flat metric $g = (dx^2 + dy^2)/y^2$. The natural choice is $\sigma^1 = dx/y$, $\sigma^2 = dy/y$ (so that $\sigma^1 \otimes \sigma^1 + \sigma^2 \otimes \sigma^2 = g$).

> [!note]- Hint 2
> The connection 1-form $\omega^1_{\;2}$ is uniquely determined by the first Cartan structural equation $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$ together with the skew-symmetry $\omega_{ab} = -\omega_{ba}$, hence $\omega^1_{\;1} = \omega^2_{\;2} = 0$ and $\omega^2_{\;1} = -\omega^1_{\;2}$. So the only unknown is $\omega^1_{\;2}$. Compute $d\sigma^1$ and $d\sigma^2$; write $\omega^1_{\;2} = a\sigma^1 + b\sigma^2$ for unknowns $a, b$; solve.

> [!note]- Hint 3
> $d\sigma^1 = d(dx/y) = -y^{-2}dy \wedge dx = -(\sigma^2/y) \wedge (y\sigma^1) = -\sigma^2 \wedge \sigma^1 = \sigma^1 \wedge \sigma^2$... wait let me redo this. $d\sigma^1 = d(y^{-1}dx) = -y^{-2}dy\wedge dx = y^{-2}dx\wedge dy = (dx/y) \wedge (dy/y) = \sigma^1\wedge\sigma^2$.
> Similarly $d\sigma^2 = d(y^{-1}dy) = -y^{-2}dy\wedge dy = 0$.

> [!note]- Hint 4
> First structural equation: $d\sigma^1 = -\omega^1_{\;2}\wedge\sigma^2$. We have $d\sigma^1 = \sigma^1\wedge\sigma^2$ and we want $-\omega^1_{\;2}\wedge\sigma^2 = \sigma^1\wedge\sigma^2$, so $\omega^1_{\;2} = -\sigma^1 = -dx/y$.
> Check with the second equation: $d\sigma^2 = -\omega^2_{\;1}\wedge\sigma^1 = \omega^1_{\;2}\wedge\sigma^1 = (-\sigma^1)\wedge\sigma^1 = 0$. ✓

> [!note]- Hint 5
> Compute the curvature 2-form: $\Omega^1_{\;2} = d\omega^1_{\;2} + \omega^1_{\;c}\wedge\omega^c_{\;2} = d(-dx/y) + 0$ (the wedge term vanishes since there is only one independent $\omega$). $d(-dx/y) = -d(dx/y) = -\sigma^1\wedge\sigma^2$ (using Hint 3). So $\Omega^1_{\;2} = -\sigma^1\wedge\sigma^2$, giving $K = R^1_{\;212} = -1$.

---

# Solution

The calculation has three steps. **Step 1** sets up the orthonormal coframe and computes its differentials. **Step 2** solves the first structural equation to find the unique connection 1-form $\omega^1_{\;2}$. **Step 3** computes the curvature 2-form $\Omega^1_{\;2} = d\omega^1_{\;2}$ and reads off $K = -1$.

**Step 1: Orthonormal coframe and its differentials.**

> [!note]- Derivation
> The Poincaré metric $g = (dx^2 + dy^2)/y^2$ is conformally flat with conformal factor $1/y$. An orthonormal coframe is
> $$\sigma^1 = \frac{dx}{y}, \qquad \sigma^2 = \frac{dy}{y}.$$
> Check: $\sigma^1 \otimes \sigma^1 + \sigma^2 \otimes \sigma^2 = (dx \otimes dx + dy \otimes dy)/y^2 = g$. ✓
>
> Compute differentials. $d\sigma^1 = d(y^{-1}dx) = -y^{-2}dy \wedge dx + y^{-1}d(dx) = y^{-2}dx\wedge dy + 0 = (dx/y)\wedge(dy/y) = \sigma^1 \wedge \sigma^2$. Similarly $d\sigma^2 = d(y^{-1}dy) = -y^{-2}dy\wedge dy = 0$. So
> $$d\sigma^1 = \sigma^1 \wedge \sigma^2, \qquad d\sigma^2 = 0.$$

**Step 2: Solve the first structural equation for $\omega^1_{\;2}$.**

> [!note]- Derivation
> In dimension $2$ with an orthonormal coframe, the connection 1-form matrix $\omega^a_{\;b}$ is skew: $\omega^1_{\;1} = \omega^2_{\;2} = 0$ and $\omega^2_{\;1} = -\omega^1_{\;2}$. So the only unknown is $\omega^1_{\;2}$.
>
> First structural equation $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$:
> - For $a = 1$: $d\sigma^1 + \omega^1_{\;2}\wedge\sigma^2 = 0$, i.e., $\sigma^1\wedge\sigma^2 = -\omega^1_{\;2}\wedge\sigma^2$.
> - For $a = 2$: $d\sigma^2 + \omega^2_{\;1}\wedge\sigma^1 = 0$, i.e., $0 = -\omega^1_{\;2}(-\wedge\sigma^1)$, so $\omega^1_{\;2}\wedge\sigma^1 = 0$.
>
> From the second equation, $\omega^1_{\;2}$ must be a multiple of $\sigma^1$: $\omega^1_{\;2} = -f(x, y)\sigma^1$ for some function $f$. Substitute into the first equation: $-f\sigma^1\wedge\sigma^2 = -\sigma^1\wedge\sigma^2$, so $f = 1$. Therefore
> $$\omega^1_{\;2} = -\sigma^1 = -\frac{dx}{y}.$$

**Step 3: Compute the curvature 2-form and read off $K = -1$.**

> [!note]- Derivation
> Cartan's second structural equation: $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$. In dimension $2$, the wedge sum is empty (only one independent $\omega$): $\omega^1_{\;c}\wedge\omega^c_{\;2} = \omega^1_{\;1}\wedge\omega^1_{\;2} + \omega^1_{\;2}\wedge\omega^2_{\;2} = 0 + 0 = 0$. So $\Omega^1_{\;2} = d\omega^1_{\;2}$.
>
> Compute: $d\omega^1_{\;2} = d(-dx/y) = -d(dx/y) = -\sigma^1\wedge\sigma^2$ (from Step 1).
>
> Now $\Omega^1_{\;2} = \tfrac{1}{2}R^1_{\;2cd}\sigma^c\wedge\sigma^d = R^1_{\;212}\sigma^1\wedge\sigma^2$ (using antisymmetry in $(c, d)$). Comparing: $R^1_{\;212} = -1$.
>
> In dimension $2$, the unique sectional curvature is $K = R^1_{\;212}$ (in an orthonormal frame): $K \equiv -1$. ∎

> [!note]- Complete formal solution
> Set $\sigma^1 = dx/y$, $\sigma^2 = dy/y$ — orthonormal coframe for $g = (dx^2 + dy^2)/y^2$. Compute $d\sigma^1 = \sigma^1\wedge\sigma^2$ and $d\sigma^2 = 0$. The unique skew connection 1-form solving $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$ is $\omega^1_{\;2} = -dx/y$. The curvature 2-form is $\Omega^1_{\;2} = d\omega^1_{\;2} = -\sigma^1\wedge\sigma^2$, giving $K = R^1_{\;212} = -1$.

> [!warning] Sanity check via independent route
> The hyperbolic plane is also realised as the unit disc $\{|z| < 1\}$ with Poincaré metric $g = 4|dz|^2/(1 - |z|^2)^2$. Same Cartan calculation, with $\sigma^1 = 2dx/(1-r^2)$, $\sigma^2 = 2dy/(1-r^2)$ ($r^2 = x^2 + y^2$), gives the same answer $K = -1$. The two models are isometric, so they *must* give the same curvature; the calculation confirms this without invoking the isometry explicitly.

---

# Key Takeaways

**Cartan's structural equations are the dominant route for sectional curvature in low dimension.** In dimension $2$, the entire curvature is captured by a single skew-symmetric connection 1-form $\omega^1_{\;2}$, and the Gauss curvature is read off $d\omega^1_{\;2} = K\sigma^1\wedge\sigma^2$. This route is much faster than computing the $6$ Christoffel symbols of a $2$-D metric and then the $4$ components of the Riemann tensor — the structural-equations approach packages the same information into one 1-form. Recognise the trigger: any $2$-D Riemannian manifold with a conformally-flat metric or a metric of the form $g = du^2 + G(u, v)^2 dv^2$ is ideal for Cartan's method (see Frankel §9.5c for the general $G$ formula $K = -G_{uu}/G$).

**Conformal flatness simplifies the orthonormal-frame setup.** A metric $g = \rho^2 \bar g$ with $\bar g$ flat has the rescaled coordinate coframe $\sigma^a = \rho\, d\bar x^a$ as an orthonormal coframe. The first structural equation then involves only $d\rho$, and the answer $\omega = -d\log\rho \wedge (\text{something})$ comes out clean. The Poincaré metric is the conformally-flat example par excellence; the same machine handles the round sphere via stereographic projection (which is a conformal map), the upper-half-space hyperbolic spaces in arbitrary dimension, and the Riemannian metrics on Riemann surfaces.

**Negative curvature is geodesic divergence; positive curvature is geodesic convergence.** Once you have $K = -1$ on $H^2$, the [[Thm - Cartan-Hadamard Theorem|Cartan–Hadamard theorem]] applies: $H^2$ is diffeomorphic to $\mathbb{R}^2$ via the exponential map, no conjugate points, geodesics diverge exponentially. This is exactly the "two geodesics from the same point are linked by exponentially-growing distance" property of hyperbolic geometry. The calculation $K = -1$ is the *quantitative* foundation of all these qualitative theorems.

**Comparison: this same Cartan-method calculation gives $K = +1$ on $S^2$ in the spherical-coordinate parametrisation** — see [[Ex - Computing the Riemann Tensor of S^2 from Cartan's Equations]] for that exercise. The two calculations are exactly parallel in structure but differ in sign at every step, reflecting the opposite-curvature geometries.
