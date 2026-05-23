---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Coordinate Chart and Atlas"
  - "Def - The Tangent Space"
  - "Def - Derivation at a Point"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold and $p \in M$. A chart at $p$ is $(U, \varphi)$ with $\varphi : U \to \hat{U} \subseteq \mathbb{R}^{n}$ a diffeomorphism onto an open subset, see [[Def - Coordinate Chart and Atlas]]. The component functions of $\varphi$ are $x^{1}, \dots, x^{n}$ — smooth real-valued functions on $U$. For a smooth function $f \in C^{\infty}(U)$, its **coordinate representative** is $\hat{f} = f \circ \varphi^{-1} : \hat{U} \to \mathbb{R}$. We write $\partial f/\partial x^{i}|_{q}$ in $\mathbb{R}^{n}$ for the standard $i$-th partial derivative of a Euclidean function at a point. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

We want, in any chart $(U, \varphi)$ around $p$, a *natural basis* for $T_{p}M$ — a basis built from the chart, against which any tangent vector can be expanded with explicit components. Geometrically, the basis should be the "tangent vectors along the coordinate axes" — the $n$ directions one travels by moving in only the $i$-th coordinate while holding the others fixed.

In $\mathbb{R}^{n}$, the natural basis at every point is $\partial/\partial x^{i}|_{a}$, the partial-differentiation operators. These are derivations at $a$ — they are linear in $f$ and satisfy the product rule. They form a basis for $T_{a}\mathbb{R}^{n}$ because every derivation is determined by its values on the coordinate functions $x^{i}$ (which yield the components $v^{i}$) and the operators $\partial/\partial x^{i}|_{a}$ are independent (apply them to $x^{j}$ and get $\delta^{j}_{i}$).

The question is: on an abstract manifold, what plays the role of $\partial/\partial x^{i}|_{p}$? The answer is forced by the chart. Given $(U, \varphi)$, we can transport partial-differentiation from $\mathbb{R}^{n}$ to $U$ via $\varphi$. Specifically, define
$$\left.\frac{\partial}{\partial x^{i}}\right|_{p} (f) \;=\; \left.\frac{\partial \hat{f}}{\partial x^{i}}\right|_{\varphi(p)} \;=\; \frac{\partial (f \circ \varphi^{-1})}{\partial x^{i}}(\varphi(p)).$$
This is the recipe: "differentiate $f$'s coordinate representative in the $i$-th Euclidean direction at $\varphi(p)$, and call the result the action of $\partial/\partial x^{i}|_{p}$ on $f$".

This recipe defines a derivation at $p$ because (a) the coordinate-representation operator $f \mapsto \hat{f}$ is linear and [[Def - Ring|ring]]-homomorphic (it intertwines pointwise multiplication: $\widehat{fg} = \hat{f}\hat{g}$, since $(fg) \circ \varphi^{-1} = (f \circ \varphi^{-1})(g \circ \varphi^{-1})$), and (b) the standard partial derivative $\partial/\partial x^{i}|_{\varphi(p)}$ on $\mathbb{R}^{n}$ is a derivation at $\varphi(p)$. The composition of "take coordinate representative" with "differentiate in the $i$-th direction" is therefore a derivation at $p$.

Why is this *the* right definition? Because it makes the chart $\varphi$ into a "tangent-space isomorphism" $d\varphi_{p} : T_{p}U \to T_{\varphi(p)}\hat{U} \cong T_{\varphi(p)}\mathbb{R}^{n} \cong \mathbb{R}^{n}$, with $\partial/\partial x^{i}|_{p}$ mapping to the standard basis vector $\partial/\partial x^{i}|_{\varphi(p)}$ of $\mathbb{R}^{n}$. The coordinate tangent vectors are *defined* to make $\varphi$ tangent-linear in the canonical sense.

The basis property — that $\partial/\partial x^{1}|_{p}, \dots, \partial/\partial x^{n}|_{p}$ span $T_{p}M$ — follows from [[Thm - Dimension of the Tangent Space]] via the chart isomorphism. The vectors are linearly independent (apply them to the coordinate functions $x^{j}$ and get the identity matrix), and there are $n$ of them, matching the [[Def - Dimension|dimension]] of $T_{p}M$. So they are a basis.

The component formula $v = v^{i}\,\partial/\partial x^{i}|_{p}$ has the slick characterization $v^{i} = v(x^{i})$: the $i$-th component of $v$ is what $v$ does to the $i$-th coordinate function. *Proof:* $v(x^{j}) = v^{i}\,(\partial/\partial x^{i}|_{p})(x^{j}) = v^{i}\,\delta^{j}_{i} = v^{j}$. The components are an instance of the "feed coordinate functions to the linear operator" pattern.

The key subtlety, captured in Lee's Exercise 3.17 and recurring everywhere in differential geometry, is that **$\partial/\partial x^{i}|_{p}$ depends on the entire chart $(x^{1}, \dots, x^{n})$, not just on the single coordinate function $x^{i}$**. Changing one coordinate function in a chart can change the basis vector $\partial/\partial x^{i}|_{p}$ associated with another. The reason is that $\partial/\partial x^{i}$ means "differentiate in the $x^{i}$ direction *while holding the other coordinates fixed*" — and what counts as "fixed" depends on which the other coordinates are.

A reader could invent this definition by the following route. Want a basis for $T_{p}M$. Use the chart $\varphi$ to push the canonical basis $\partial/\partial x^{i}|_{\varphi(p)}$ from $\mathbb{R}^{n}$ back to $M$. Verify the result is a derivation. Verify they are linearly independent (by pairing with coordinate functions). Verify they span. The whole construction is the chart's gift to the tangent space.

---

# The Definition

Let $(U, \varphi)$ be a smooth chart on $M$ at $p$, with coordinate functions $x^{1}, \dots, x^{n} : U \to \mathbb{R}$ (so $\varphi(q) = (x^{1}(q), \dots, x^{n}(q))$ for $q \in U$). For each $i \in \{1, \dots, n\}$, the **$i$-th coordinate tangent vector at $p$ associated with the chart $(U, \varphi)$** is the [[Def - Derivation at a Point|derivation]] $\partial/\partial x^{i}|_{p} \in T_{p}M$ defined by
$$\left.\frac{\partial}{\partial x^{i}}\right|_{p} (f) \;=\; \frac{\partial (f \circ \varphi^{-1})}{\partial x^{i}}\bigg|_{\varphi(p)}$$
for $f \in C^{\infty}(U)$ (extended by locality to $f \in C^{\infty}(M)$, see [[Def - Derivation at a Point]]). Equivalently, writing $\hat{f} = f \circ \varphi^{-1}$ for the coordinate representative:
$$\left.\frac{\partial}{\partial x^{i}}\right|_{p} (f) \;=\; \frac{\partial \hat{f}}{\partial x^{i}}(\varphi(p)).$$

**Basis property.** The $n$ coordinate tangent vectors $\partial/\partial x^{1}|_{p}, \dots, \partial/\partial x^{n}|_{p}$ form a basis of $T_{p}M$. Any tangent vector $v \in T_{p}M$ has a unique expansion
$$v \;=\; v^{i}\,\left.\frac{\partial}{\partial x^{i}}\right|_{p}$$
(Einstein summation), where the **components** of $v$ relative to the chart are
$$v^{i} \;=\; v(x^{i}).$$

**Change of chart.** If $(U, \varphi)$ and $(V, \tilde\varphi)$ are two charts at $p$ with coordinates $x^{i}$ and $\tilde x^{j}$, the bases are related by
$$\left.\frac{\partial}{\partial x^{i}}\right|_{p} \;=\; \frac{\partial \tilde x^{j}}{\partial x^{i}}(\varphi(p))\,\left.\frac{\partial}{\partial \tilde x^{j}}\right|_{p},$$
where $\partial \tilde x^{j}/\partial x^{i}$ is the standard Jacobian of the transition map $\tilde\varphi \circ \varphi^{-1}$. The components transform contragrediently:
$$\tilde v^{j} \;=\; \frac{\partial \tilde x^{j}}{\partial x^{i}}(\varphi(p))\,v^{i}.$$
This is the "transformation law for the components of a contravariant vector" of classical tensor calculus.

---

# Relate to Other Fields / Compression

In **multivariate analysis**, the operators $\partial/\partial x^{i}|_{a}$ on $\mathbb{R}^{n}$ are simply the standard partial-differentiation operators. The manifold definition transports this directly: $\partial/\partial x^{i}|_{p}$ on $M$ is the chart-image of $\partial/\partial x^{i}|_{\varphi(p)}$ on $\mathbb{R}^{n}$. So the manifold coordinate basis is just the Euclidean coordinate basis viewed through the chart.

**True name:** $\partial/\partial x^{i}|_{p}$ is "the velocity of the $i$-th coordinate curve at $p$". The $i$-th coordinate curve at $p$ is $\gamma_{i}(t) = \varphi^{-1}(\varphi(p) + t\,e_{i})$ — move in the $i$-th coordinate direction in the chart, transport back to $M$. Its velocity at $t = 0$ is $\partial/\partial x^{i}|_{p}$; see [[Ex - Tangent Vectors as Velocities of Coordinate Curves]]. This is the geometric picture: the coordinate basis vectors are the velocities of curves along the coordinate axes.

In **classical tensor calculus** (the language used by physicists from Einstein to the present), tangent vectors are defined as "tuples of numbers transforming by the Jacobian under change of coordinates". The components $v^{i}$ of $v$ in chart $(U, \varphi)$ are exactly the numbers, and the change-of-chart formula above is exactly the Jacobian rule. The modern manifold formulation justifies the classical tensor calculus by *defining* the abstract object (the tangent vector) and *deriving* the component transformation rule from the change-of-chart formula — rather than the other way around.

In **physics** the upper-index convention for components ($v^{i}$) versus the lower-index convention for coordinate basis vectors ($\partial/\partial x^{i}$, where the $i$ counts as "lower" because it is in the denominator) follows the **Einstein summation convention**: a repeated index, once up and once down, is summed. This convention is precisely set up to make the contraction $v^{i}\,\partial/\partial x^{i}|_{p}$ a coordinate-independent quantity — the tangent vector itself.

---

# Examples / Corollaries

**Coordinate basis on $\mathbb{R}^{n}$.** The chart on $\mathbb{R}^{n}$ is the identity map $\mathrm{id} : \mathbb{R}^{n} \to \mathbb{R}^{n}$, with coordinate functions $x^{i}$ the standard Euclidean coordinates. The coordinate tangent vectors $\partial/\partial x^{i}|_{a}$ are the standard partial-differentiation operators, $(\partial/\partial x^{i}|_{a})(f) = \partial f/\partial x^{i}(a)$. This is the prototype.

**Coordinate basis on $S^{2}$ in spherical coordinates.** With $\varphi(p) = (\theta, \phi)$ the spherical coordinates of $p \in S^{2}$ (with the poles excluded), the coordinate tangent vectors at $p$ are $\partial/\partial \theta|_{p}$ (the velocity vector along a meridian) and $\partial/\partial \phi|_{p}$ (the velocity vector along a parallel). At the equator with $\theta = \pi/2$, $\partial/\partial \phi$ points east and $\partial/\partial \theta$ points north — geometrically explicit.

**Change of chart between Cartesian and polar coordinates on $\mathbb{R}^{2} \setminus \{0\}$.** With Cartesian $(x, y)$ and polar $(r, \theta)$, the transition is $x = r\cos\theta$, $y = r\sin\theta$. At a point $p$ with polar coordinates $(r_{0}, \theta_{0})$:
$$\left.\frac{\partial}{\partial r}\right|_{p} = \cos\theta_{0}\,\left.\frac{\partial}{\partial x}\right|_{p} + \sin\theta_{0}\,\left.\frac{\partial}{\partial y}\right|_{p}, \quad \left.\frac{\partial}{\partial \theta}\right|_{p} = -r_{0}\sin\theta_{0}\,\left.\frac{\partial}{\partial x}\right|_{p} + r_{0}\cos\theta_{0}\,\left.\frac{\partial}{\partial y}\right|_{p}.$$
This is the Jacobian formula applied verbatim.

**Coordinate basis on $\mathrm{GL}(n, \mathbb{R})$ at $I$.** $\mathrm{GL}(n)$ is an open subset of the vector space $M_{n}(\mathbb{R})$, with the chart being the inclusion. The coordinate functions $X^{ij}$ are the matrix entries; the coordinate tangent vectors $\partial/\partial X^{ij}|_{I}$ are the directional derivatives along the elementary matrix $E_{ij}$ (with $1$ in position $(i,j)$ and zeros elsewhere). The basis $\{\partial/\partial X^{ij}|_{I} : 1 \leq i, j \leq n\}$ has $n^{2}$ elements, matching $\dim \mathrm{GL}(n) = n^{2}$.

**Is NOT a chart-independent statement: "the basis vector $\partial/\partial x^{1}|_{p}$".** The notation $\partial/\partial x^{1}|_{p}$ refers to *the entire chart*, not just the single coordinate function $x^{1}$. Lee's Exercise 3.17 makes this concrete: take coordinates $(x, y)$ on $\mathbb{R}^{2}$ and the new coordinates $(\tilde x, \tilde y) = (x, y + x^{3})$. The coordinate function $\tilde x$ equals $x$, but $\partial/\partial \tilde x|_{p}$ differs from $\partial/\partial x|_{p}$ at any point with $x \neq 0$: the first holds $\tilde y$ fixed (which constrains $y$ to vary), while the second holds $y$ fixed. The lesson is that *both coordinate functions of the chart* determine each basis vector.

**Corollary — components from action on coordinate functions.** For any $v \in T_{p}M$ and any chart at $p$, $v(x^{i}) = v^{i}$. *Proof:* $v(x^{j}) = v^{i}\,(\partial/\partial x^{i}|_{p})(x^{j}) = v^{i}\,(\partial \hat{x^{j}}/\partial x^{i})(\varphi(p)) = v^{i}\,\delta^{j}_{i} = v^{j}$, since $\hat{x^{j}} = x^{j} \circ \varphi^{-1}$ is the $j$-th coordinate function on $\mathbb{R}^{n}$. So to extract the components of $v$ in a chart, feed $v$ the coordinate functions one at a time.

**Corollary — the components of $\partial/\partial x^{j}|_{p}$ are $\delta^{j}_{i}$.** By the previous corollary, the $i$-th component of $\partial/\partial x^{j}|_{p}$ in the chart $(x^{1}, \dots, x^{n})$ is $(\partial/\partial x^{j}|_{p})(x^{i}) = \delta^{i}_{j}$. So the coordinate basis is "the basis whose components are the standard basis vectors".

**Calibration check.** Verify that $\partial/\partial r|_{p}$ and $\partial/\partial \theta|_{p}$ at $p = (1, 0) \in \mathbb{R}^{2}$ in polar coordinates equal $\partial/\partial x|_{p}$ and $\partial/\partial y|_{p}$ respectively (the radial direction at $(1,0)$ is the $x$-direction; the angular direction at $(1,0)$ is the $y$-direction). Verify that if $v = 3\,\partial/\partial r|_{p} - \partial/\partial \theta|_{p}$ at $p = (2, \pi/2)$ in polar coordinates, then $v$ in Cartesian coordinates is $\partial/\partial y|_{p} + 2\,\partial/\partial x|_{p}$ (this is Lee's worked Example 3.16). If you can also explain why $\partial/\partial x^{i}|_{p}$ depends on the entire chart, not just the single coordinate function $x^{i}$, you have understood the geometric content.

---

# Unlocked by This

> [!tip] Differential in Coordinates *(from Differential Geometry)*
> The matrix of the differential $dF_{p}$ in coordinate bases is the Jacobian matrix of the coordinate representative $\hat{F}$, see [[Ex - Computing the Differential in Local Coordinates]]. The coordinate-basis pair-up is what reduces manifold calculus to the Euclidean calculus of partials.

> [!tip] Velocity of a Curve in Coordinates *(from Differential Geometry)*
> For a smooth curve $\gamma : J \to M$ whose coordinate representative is $\hat\gamma(t) = (\gamma^{1}(t), \dots, \gamma^{n}(t))$, the velocity in coordinates is $\gamma'(t_{0}) = (d\gamma^{i}/dt)(t_{0})\,\partial/\partial x^{i}|_{\gamma(t_{0})}$. See [[Def - Velocity of a Curve]].

> [!tip] Dual Basis on the Cotangent Space *(from Differential Geometry)*
> The **dual basis** to $\{\partial/\partial x^{i}|_{p}\}$ on $T^{*}_{p}M$ is $\{dx^{i}|_{p}\}$, where $dx^{i}|_{p}$ is the differential of the coordinate function $x^{i}$ viewed as a covector at $p$. The pairing is $dx^{j}|_{p}(\partial/\partial x^{i}|_{p}) = \delta^{j}_{i}$. See [[Def - Dual Basis]] for the linear-algebra prototype, and [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]] for the manifold cotangent bundle.

> [!tip] Christoffel Symbols *(from Riemannian Geometry)*
> In a chart, the **Christoffel symbols** $\Gamma^{k}_{ij}$ of the Levi-Civita connection are defined by $\nabla_{\partial/\partial x^{i}}\,\partial/\partial x^{j} = \Gamma^{k}_{ij}\,\partial/\partial x^{k}$ — they record how the coordinate basis vectors "fail to be parallel" with respect to the connection. The Christoffel symbols are not the components of a tensor; they transform inhomogeneously under change of chart. This is the calculational heart of Riemannian geometry, to be developed in **Riemannian Geometry**.
