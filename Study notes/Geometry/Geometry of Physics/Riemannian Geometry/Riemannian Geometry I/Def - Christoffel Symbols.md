---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$(M, g)$ — a Riemannian (or semi-Riemannian) manifold with metric components $g_{ij}$ in a chart and inverse $g^{ij}$. $(x^i)$ — local coordinates with coordinate frame $\partial_i = \partial/\partial x^i$. $\nabla$ — an affine connection on $TM$. The Einstein summation convention is in force throughout: a repeated upper-and-lower index is summed. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

The Christoffel symbols are the local-coordinate components of a connection on $TM$: they answer the question "what is $\nabla_{\partial_i}\partial_j$?" in terms of a basis. Since $\nabla_{\partial_i}\partial_j$ is a vector field, it can be expanded in the coordinate basis: $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$, and the $n^3$ coefficients $\Gamma^k_{ij}$ are exactly the Christoffel symbols. The whole content of the connection in the chart is in these $n^3$ functions: by the Leibniz rule and $C^\infty$-linearity, the action of $\nabla$ on any pair of vector fields is determined by its action on basis vector fields, so $(\nabla_X Y)^k = X^i \partial_i Y^k + \Gamma^k_{ij} X^i Y^j$ for any $X, Y$. The first term, $X(Y^k) = X^i \partial_i Y^k$, is the "naive" component derivative; the second is the **Christoffel correction** that converts the naive expression into a tensor.

The interesting feature — and the source of confusion for beginners — is that the Christoffel symbols **do not transform as a tensor**. They have three indices and look like $(1, 2)$-tensor components, but under a change of coordinates from $(x^i)$ to $(x'^a)$ they transform as
$$
\Gamma'{}^c_{ab} = \frac{\partial x'^c}{\partial x^k}\frac{\partial x^i}{\partial x'^a}\frac{\partial x^j}{\partial x'^b}\,\Gamma^k_{ij} + \frac{\partial x'^c}{\partial x^k}\,\frac{\partial^2 x^k}{\partial x'^a \partial x'^b}.
$$
The first term is the tensor part — the matrix-conjugation a $(1, 2)$-tensor would undergo. The second term is the **inhomogeneous correction**: a second-derivative piece that depends on the *curvature of the coordinate change*, not on $\Gamma$ at all. This inhomogeneous piece is what makes $\Gamma$ non-tensorial, and it is *precisely* what is needed for the *combination* $\nabla_X Y = (X^i \partial_i Y^k + \Gamma^k_{ij}X^i Y^j)\partial_k$ to transform as a vector: the inhomogeneous transformation of $\Gamma$ cancels the inhomogeneous transformation of $\partial_i Y^k$.

For a Riemannian (or semi-Riemannian) manifold with the Levi-Civita connection, the Christoffel symbols are determined explicitly by the metric:
$$
\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr).
$$
This **Christoffel formula** comes from solving the [[Thm - Koszul Formula|Koszul formula]] in the coordinate frame using $[\partial_i, \partial_j] = 0$. The two free indices $(i, j)$ are symmetric in this formula, reflecting the torsion-freeness of the Levi-Civita connection — for a general (non-Levi-Civita) connection on a Riemannian manifold, $\Gamma^k_{ij}$ need not be symmetric in $(i, j)$.

Why are there exactly $n^3$ Christoffel symbols? Because $\nabla_{\partial_i}\partial_j$ is a vector with $n$ components, for each of the $n \times n$ choices of $(i, j)$ — so $n^3$ components total. For the Levi-Civita connection the symmetry $\Gamma^k_{ij} = \Gamma^k_{ji}$ reduces this to $n^2(n+1)/2$ independent functions; for a connection with torsion there are no symmetry reductions.

**The Christoffel symbols vanish at a single point in normal coordinates.** Around any point $p$ of a Riemannian manifold one can choose **normal coordinates** (Riemann normal coordinates) in which $g_{ij}(p) = \delta_{ij}$ and $\partial_k g_{ij}(p) = 0$ — and consequently $\Gamma^k_{ij}(p) = 0$. This is the coordinate-system in which the metric looks "as Euclidean as possible at $p$" — first derivatives of $g$ vanish at $p$ but second derivatives generally do not, and those second derivatives are the **Riemann tensor at $p$**. Normal coordinates are the cleanest place to compute curvature.

**The Christoffel symbols are nonzero in non-Cartesian coordinates even on flat $\mathbb{R}^n$.** On Euclidean $\mathbb{R}^2$ in polar coordinates $(r, \theta)$, the metric is $g = dr^2 + r^2\,d\theta^2$ and the nonzero Christoffel symbols are $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$ ([[Ex - The Levi-Civita Connection of Polar Coordinates]]). The connection itself is flat — the curvature tensor is zero — but the Christoffel symbols are not zero because the coordinate frame $\partial_r, \partial_\theta$ is not orthonormal and rotates as you move. This is the canonical example showing $\Gamma$ is not a tensor: a tensor that is zero in one frame would be zero in all.

**In an orthonormal frame the "Christoffel symbols" go by another name.** When $(e_a)$ is an orthonormal frame (not a coordinate frame), the components $\omega^c_{ab}$ defined by $\nabla_{e_a}e_b = \omega^c_{ab}\,e_c$ are sometimes called Ricci rotation coefficients or, in physics, **spin connection coefficients**. They differ from the Christoffel symbols by both the change-of-frame transformation (encoded in $\Gamma' = g^{-1}\Gamma g + g^{-1}dg$, see [[Thm - Gauge Transformation Law for Connection 1-Forms]]) and by the failure of the orthonormal frame to commute ($[e_a, e_b] \neq 0$ in general, even for flat space in spherical coordinates). The collected data of $\omega^c_{ab}$ packages into the [[Def - Connection 1-Forms (Cartan)|connection 1-forms]] $\omega^a{}_b = \omega^a_{cb}\sigma^c$, which in the orthonormal-frame setting are *antisymmetric* in $a, b$ (when indices are lowered by the orthonormal metric) — this is the orthonormal-frame statement of metric-compatibility.

---

# The Definition

Let $(M, \nabla)$ be a smooth manifold with an affine connection $\nabla$ on $TM$, and let $(x^1, \ldots, x^n)$ be local coordinates on an open set $U \subseteq M$ with coordinate frame $\partial_i = \partial/\partial x^i$. The **Christoffel symbols** of $\nabla$ in the chart $(x^i)$ are the $n^3$ smooth functions $\Gamma^k_{ij} : U \to \mathbb{R}$ defined by
$$
\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\,\partial_k.
$$
For arbitrary smooth vector fields $X = X^i\partial_i$, $Y = Y^j\partial_j$ on $U$, the covariant derivative is
$$
(\nabla_X Y)^k = X^i\,\partial_i Y^k + \Gamma^k_{ij}\,X^i Y^j.
$$

When $(M, g)$ is Riemannian (or semi-Riemannian) and $\nabla$ is the **Levi-Civita connection**, the Christoffel symbols are given explicitly by the **Christoffel formula**
$$
\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr),
$$
and consequently they are symmetric in the lower indices: $\Gamma^k_{ij} = \Gamma^k_{ji}$.

**Transformation law.** Under a change of coordinates from $(x^i)$ to $(x'^a)$, the Christoffel symbols transform as
$$
\Gamma'{}^c_{ab} = \frac{\partial x'^c}{\partial x^k}\,\frac{\partial x^i}{\partial x'^a}\,\frac{\partial x^j}{\partial x'^b}\,\Gamma^k_{ij} + \frac{\partial x'^c}{\partial x^k}\,\frac{\partial^2 x^k}{\partial x'^a \partial x'^b}.
$$
The first term is the tensor part; the second is the inhomogeneous correction, which prevents $\Gamma$ from being a tensor.

---

# Relate to Other Fields / Compression

The compression: **the Christoffel symbols are the connection coefficients in a coordinate frame**, the coordinate-specific data needed to extend the partial-derivative operation into a chart-independent covariant derivative. Their non-tensoriality is the price of working with the coordinate frame; in a general frame they generalise to [[Def - Connection 1-Forms (Cartan)|connection 1-forms]] which have the same role and the same transformation behaviour.

In **physics**, the Christoffel symbols are the components of the **gravitational field** in general relativity. The geodesic equation $\ddot x^\lambda + \Gamma^\lambda_{\mu\nu}\dot x^\mu \dot x^\nu = 0$ is Newton's second law for a particle in a gravitational field, with $\Gamma^\lambda_{\mu\nu}$ playing the role of "gravitational force per unit velocity squared". The relation to the metric — $\Gamma^\lambda_{\mu\nu} = \tfrac{1}{2}g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu})$ — is how the **metric** (the gravitational potential) determines the **connection** (the gravitational force), in the same sense that the Newtonian gravitational potential $\Phi$ determines the Newtonian gravitational force $\mathbf{g} = -\nabla\Phi$.

**True name:** The "true name" of the Christoffel symbols is **the coordinate-frame components of the connection 1-form**. They are not three-indexed tensors — they are the entries $\omega^k{}_j(\partial_i) = \Gamma^k_{ij}$ of the connection 1-form matrix $\omega = (\omega^k{}_j)$ evaluated on coordinate vector fields. This perspective immediately explains the non-tensoriality (the connection 1-form is gauge-dependent), gives the right framework for working in non-coordinate frames (Cartan's structural equations), and clarifies the analogy to the gauge potential in physics (which is literally the connection 1-form in another setting). Once one thinks "$\Gamma^k_{ij}$ are components of a 1-form valued in $\mathrm{End}(TM)$", every property of the symbols becomes natural.

---

# Examples / Corollaries

**Example: flat $\mathbb{R}^n$ in Cartesian coordinates.** All $\Gamma^k_{ij} = 0$. The covariant derivative reduces to the partial derivative: $(\nabla_X Y)^k = X^i \partial_i Y^k$. The Levi-Civita connection of the Euclidean metric in Cartesian coordinates is the flat connection of vector calculus.

**Example: flat $\mathbb{R}^2$ in polar coordinates.** Metric $g = dr^2 + r^2\,d\theta^2$, so $g_{rr} = 1$, $g_{\theta\theta} = r^2$, $g_{r\theta} = 0$ and $g^{rr} = 1$, $g^{\theta\theta} = 1/r^2$. The Christoffel formula gives $\Gamma^r_{\theta\theta} = -\tfrac{1}{2}\partial_r g_{\theta\theta} = -\tfrac{1}{2}(2r) = -r$, $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \tfrac{1}{2}g^{\theta\theta}\partial_r g_{\theta\theta} = \tfrac{1}{2r^2}(2r) = 1/r$. All others vanish. The connection is flat (Riemann tensor zero), but the Christoffel symbols are nonzero — the canonical illustration that $\Gamma$ is not a tensor. See [[Ex - The Levi-Civita Connection of Polar Coordinates]].

**Example: the round 2-sphere.** Metric $g = d\theta^2 + \sin^2\theta\,d\varphi^2$. The Christoffel formula gives $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$, $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$, all others zero. The geodesic equation then reproduces the great-circle equations. See [[Ex - Christoffel Symbols of the Round Metric on the Sphere]].

**Example: the hyperbolic plane.** Upper half-plane metric $g = (dx^2 + dy^2)/y^2$. Christoffel symbols $\Gamma^x_{xy} = \Gamma^x_{yx} = -1/y$, $\Gamma^y_{xx} = 1/y$, $\Gamma^y_{yy} = -1/y$, all others zero. See [[Ex - Christoffel Symbols of the Hyperbolic Plane]].

**Non-example: $\Gamma^k_{ij} = 0$ for the Levi-Civita connection on a general curved manifold.** It is impossible to have all Christoffel symbols vanish in a coordinate chart unless the metric is flat (locally Euclidean). This is one direction of the **Riemann theorem**: a Riemannian metric is locally Euclidean if and only if the Riemann curvature tensor vanishes, and this is equivalent to the existence of coordinates in which $\Gamma^k_{ij} \equiv 0$.

**Non-example: $\Gamma^k_{ij}$ as a tensor.** The Christoffel symbols look like a $(1, 2)$-tensor by index structure, but they are not. Concretely on $\mathbb{R}^2$, all $\Gamma^k_{ij} = 0$ in Cartesian coordinates but $\Gamma^r_{\theta\theta} = -r$ in polar coordinates — a tensor that vanishes in one coordinate system would vanish in all. The transformation law has the inhomogeneous second-derivative term that prevents tensorial behaviour.

**Corollary (the symmetric and antisymmetric parts of $\Gamma$).** Decompose $\Gamma^k_{ij} = \Gamma^k_{(ij)} + \Gamma^k_{[ij]}$ into the symmetric and antisymmetric parts in the lower indices. The antisymmetric part $\Gamma^k_{[ij]} = \tfrac{1}{2}(\Gamma^k_{ij} - \Gamma^k_{ji})$ *is* a tensor — it equals $\tfrac{1}{2}T^k_{ij}$, half the [[Def - Torsion Tensor|torsion tensor]] components. So the non-tensoriality is concentrated in the symmetric part; the antisymmetric part of $\Gamma$ is tensorial because the inhomogeneous transformation term is symmetric in the lower indices (mixed second partial derivatives commute) and thus cancels on antisymmetrisation. This is the most efficient way to see that torsion is a tensor.

**Corollary (the Levi-Civita Christoffel formula from the Koszul formula).** Apply the [[Thm - Koszul Formula|Koszul formula]] with $X = \partial_i$, $Y = \partial_j$, $Z = \partial_l$ and use $[\partial_i, \partial_j] = 0$:
$$
2g(\nabla_{\partial_i}\partial_j, \partial_l) = \partial_i g(\partial_j, \partial_l) + \partial_j g(\partial_i, \partial_l) - \partial_l g(\partial_i, \partial_j) = \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}.
$$
Now $g(\nabla_{\partial_i}\partial_j, \partial_l) = g(\Gamma^k_{ij}\partial_k, \partial_l) = \Gamma^k_{ij} g_{kl}$, so $2\Gamma^k_{ij} g_{kl} = \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}$, and raising the index with $g^{kl}$ gives the Christoffel formula. This is a useful derivation to know: it shows the formula is forced by torsion-freeness ($\Gamma^k_{ij}$ symmetric in lower indices) and metric-compatibility.

**Calibration check.** If you can perform the following four computations, you have understood Christoffel symbols. (i) Compute $\Gamma^k_{ij}$ for the Euclidean metric on $\mathbb{R}^2$ in polar coordinates (answer: $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = 1/r$, all others zero). (ii) Verify that the symmetric part of the transformation law is the inhomogeneous piece, so the antisymmetric part transforms as a tensor. (iii) Compute the Christoffel symbols of the round 2-sphere from the Christoffel formula and verify the geodesic equation $\ddot\theta - \sin\theta\cos\theta\,\dot\varphi^2 = 0$, $\ddot\varphi + 2\cot\theta\,\dot\theta\dot\varphi = 0$ is satisfied by great circles. (iv) Show that on a Lie group with bi-invariant metric, the Christoffel symbols in a left-invariant frame are $\Gamma^c_{ab} = \tfrac{1}{2}f^c{}_{ab}$ where $f^c{}_{ab}$ are the structure constants of the Lie algebra.

---

# Unlocked by This

> [!tip] The Geodesic Equation in Coordinates *(from Riemannian Geometry)*
> Once the Christoffel symbols are computed, the geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ becomes the explicit system
> $$
> \ddot\gamma^k + \Gamma^k_{ij}(\gamma(t))\,\dot\gamma^i\,\dot\gamma^j = 0.
> $$
> This is a system of $n$ second-order ODEs in the $n$ coordinate functions $\gamma^k(t)$, with initial data $\gamma(0)$ and $\dot\gamma(0)$. For symmetric backgrounds (spheres, hyperbolic spaces, FRW cosmology, Schwarzschild) the system often reduces to first-order via conserved quantities (Killing fields, energy, angular momentum). For the **Schwarzschild geometry** of [[General Relativity I — Einstein's Equations and Schwarzschild|GR I]], the geodesic equation in Schwarzschild coordinates gives the perihelion precession of Mercury, the gravitational deflection of light, and the orbital structure of test particles around a non-rotating black hole.

> [!tip] The Riemann Curvature Tensor in Coordinates *(from Riemannian Geometry)*
> The components of the Riemann curvature tensor in a coordinate frame are
> $$
> R^l{}_{ijk} = \partial_i\Gamma^l_{jk} - \partial_j\Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik},
> $$
> a polynomial in the first derivatives of the Christoffel symbols and quadratic in the symbols themselves. This is the coordinate-component formula one sees in every general relativity textbook. The formula is tedious to apply directly; for any nontrivial metric, [[Thm - Cartan's Second Structural Equation|Cartan's second structural equation]] in an orthonormal frame is dramatically faster.
