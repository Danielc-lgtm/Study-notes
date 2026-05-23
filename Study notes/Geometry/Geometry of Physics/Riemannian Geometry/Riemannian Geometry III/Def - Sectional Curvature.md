---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold with [[Def - Riemann Curvature Tensor|Riemann curvature tensor]] $R$. A **$2$-plane** in a tangent space $T_pM$ is a $2$-dimensional linear subspace $\sigma \subset T_pM$. We write $\sigma = \mathrm{span}(X, Y)$ when $X, Y$ are two linearly independent vectors spanning $\sigma$. The **Gram determinant** of $X, Y$ is

$$|X \wedge Y|^2 := |X|^2|Y|^2 - \langle X, Y\rangle^2,$$

the squared area of the parallelogram on $X, Y$ — strictly positive when $X, Y$ are linearly independent.

---

# Axiom Motivation

The full Riemann tensor $R^a_{\;bcd}$ has many components (in dimension $n$, the count is $\tfrac{1}{12}n^2(n^2 - 1)$ — twenty in dimension $4$). It is hard to wield, hard to compare across manifolds, and hard to recognise from intrinsic geometric quantities. What we want is a *scalar invariant* that summarises the most-useful curvature information in each direction. In dimension $2$, the answer is the **Gauss curvature** $K$, a single function on $M$. The question is: in higher dimension, how do we recover a Gauss-curvature-like scalar?

The natural answer comes from looking at $2$-dimensional totally geodesic surfaces. At a point $p$ and for a $2$-plane $\sigma \subset T_pM$, consider the surface formed by exponentiating all vectors in $\sigma$:

$$\Sigma_\sigma := \exp_p(\sigma \cap B_\epsilon(0)),$$

the image under the exponential map of a small ball in $\sigma$. This is a $2$-dimensional submanifold of $M$, geodesic at $p$ (its second fundamental form vanishes at $p$). It inherits a metric from $M$, so it has its own Gauss curvature at $p$. **Define $K(\sigma)$ to be the Gauss curvature of $\Sigma_\sigma$ at $p$.** This is a well-defined function on the Grassmannian of $2$-planes in $T_pM$.

The desideratum is then: express $K(\sigma)$ in terms of $R$ and the metric. The relevant computation (Gauss's equation for the totally geodesic $\Sigma_\sigma$) gives

$$K(\sigma) = \frac{\langle R(X, Y)Y, X\rangle}{|X \wedge Y|^2}$$

for any basis $X, Y$ of $\sigma$. The denominator $|X \wedge Y|^2$ is precisely what's needed to make the expression basis-independent: under a basis change $(X, Y) \mapsto (X', Y') = (X, Y)M$ with $\det M = \lambda$, both the numerator and denominator transform by $\lambda^2$.

Why the specific combination $\langle R(X, Y)Y, X\rangle$? Of the algebraically independent combinations $\langle R(X, Y)Z, W\rangle$ with $X, Y, Z, W$ drawn from $\{X, Y\}$, this one uses the **antisymmetries** of $R$ optimally: $\langle R(X, Y)Y, X\rangle$ is the only nonzero "diagonal" of $R$ in the basis $\{X, Y\}$, after applying the symmetries to identify $R(Y, X)X, Y\rangle = \langle R(X, Y)Y, X\rangle$ and noting that combinations like $\langle R(X, X)Y, Y\rangle$ vanish.

What would happen if we dropped the area normalisation? The numerator $\langle R(X, Y)Y, X\rangle$ alone is a sextic in $(X, Y)$ — scaling $X \mapsto 2X$ multiplies it by $4$. So we would have a function on tangent *vectors*, not on tangent *planes*. The whole point of sectional curvature is to be a function on the Grassmannian, since the $2$-plane is what's geometrically intrinsic, not the choice of basis.

---

# The Definition

> **Definition (Sectional curvature).** Let $(M, g)$ be a Riemannian manifold and $\sigma \subset T_pM$ a $2$-plane. The **sectional curvature** of $\sigma$ is
>
> $$K(\sigma) := \frac{\langle R(X, Y)Y, X\rangle}{|X|^2|Y|^2 - \langle X, Y\rangle^2}$$
>
> for any basis $\{X, Y\}$ of $\sigma$. By the symmetries of $R$, the value is independent of the choice of basis. When $\{X, Y\}$ is orthonormal, the denominator is $1$ and $K(X, Y) = \langle R(X, Y)Y, X\rangle$.

**Geometric characterisation.** $K(\sigma)$ equals the **Gauss curvature** at $p$ of the totally geodesic $2$-dimensional surface $\Sigma_\sigma = \exp_p(\sigma \cap B_\epsilon)$. This is the operational definition: $K(\sigma) > 0$ means geodesics spreading from $p$ into $\sigma$ converge back (like longitudes on a sphere); $K(\sigma) < 0$ means they diverge (like geodesics on the hyperbolic plane).

---

# Relate to Other Fields / Compression

In **surface theory**, sectional curvature is the Gauss curvature: there is only one $2$-plane at each point, and $K(\sigma) = K_{\mathrm{Gauss}}$.

In **physics**, sectional curvature is the **tidal curvature** in the plane $\sigma$: if $T$ and $J$ are tangent and normal to a worldline with $\sigma = \mathrm{span}(T, J)$, then $K(T, J) = -\langle R(J, T)T, J\rangle / |J|^2$ (up to sign convention) controls the relative acceleration of nearby worldlines via the geodesic deviation equation. Positive sectional curvature is "tidally focusing"; negative sectional curvature is "tidally defocusing."

In **comparison geometry**, sectional curvature is the curvature invariant that controls comparison theorems for triangles (Toponogov), Jacobi fields (Rauch), and the global topology (Synge, Cartan–Hadamard). Most "curvature bounds" in Riemannian geometry are sectional-curvature bounds.

**True name:** *Sectional curvature $K(\sigma)$ is the Gauss curvature at $p$ of the $2$-surface spanned by all geodesics emanating from $p$ tangent to $\sigma$.* If you want to know what positive sectional curvature *means*, you look at this surface and apply your intuition for $2$-dimensional surfaces in $\mathbb{R}^3$ — convex like a sphere, saddle-shaped like a pseudosphere, or flat like a plane.

---

# Examples / Corollaries

**Example 1 (constant sectional curvature).** A manifold has constant sectional curvature $K_0$ exactly when $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$. The three model spaces of constant sectional curvature are the round $n$-sphere ($K_0 = 1$), Euclidean $n$-space ($K_0 = 0$), and hyperbolic $n$-space ($K_0 = -1$). Rescaling the metric by a factor $\lambda > 0$ rescales sectional curvature by $\lambda^{-2}$, so $S^n$ of radius $r$ has $K = 1/r^2$.

**Example 2 (Fubini–Study metric on $\mathbb{CP}^n$).** Complex projective space with the Fubini–Study metric has sectional curvature satisfying $1/4 \le K(\sigma) \le 1$. The maximum $K = 1$ is achieved on complex lines (planes invariant under the complex structure $J$); the minimum $K = 1/4$ is achieved on totally real planes ($J\sigma \perp \sigma$). This pinching is exactly the boundary value in Berger's classical sphere theorem.

**Example 3 (product manifold).** On $M_1 \times M_2$ with the product metric, sectional curvature of a $2$-plane spanned by $X = X_1 \oplus 0$ and $Y = 0 \oplus Y_2$ (one vector from each factor) is **zero**: $R(X, Y) = 0$ because $R$ is block-diagonal. So $S^2 \times S^2$ has $K = 1$ on planes tangent to either $S^2$ factor and $K = 0$ on mixed planes — its sectional curvature is *not* constant, but is nonnegative.

**Non-example (flat torus).** $T^n = \mathbb{R}^n/\mathbb{Z}^n$ with the flat metric has $K \equiv 0$, the constant-curvature-$0$ case. It is locally indistinguishable from $\mathbb{R}^n$ (universal cover is $\mathbb{R}^n$ with the flat metric) but globally is a compact, multiply-connected manifold. Constant curvature does not determine the global topology — that requires simple connectedness.

**Non-example (a "sectional curvature" that's not).** The naive expression $\langle R(X, Y)Z, W\rangle$ without setting $Z = Y$ and $W = X$ is **not** a scalar invariant of the $2$-plane $\sigma = \mathrm{span}(X, Y)$ — it depends on $Z, W$ separately. The specific combination $\langle R(X, Y)Y, X\rangle$ is the unique one (up to scale) that descends to a function on $2$-planes.

**Calibration check.** If you have understood the definition correctly you should be able to: (a) verify $K(\sigma) = \langle R(X, Y)Y, X\rangle$ for an orthonormal basis $\{X, Y\}$; (b) show that under a basis change $\{X, Y\} \mapsto \{X', Y'\}$ with the same span, the ratio in the definition is unchanged; (c) read off from $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$ that this manifold has constant sectional curvature $K_0$.

---

# Unlocked by This

> [!tip] Comparison Theorems *(from Riemannian Geometry III)*
> Almost every global curvature-topology theorem is phrased as a sectional-curvature bound: **Cartan–Hadamard** ($K \le 0$), **Synge** ($K > 0$ with extra hypotheses), **Bonnet–Myers** (a slight weakening via Ricci), **the sphere theorem** ($1/4 < K \le 1$). The cleanness of these hypotheses reflects that sectional curvature is the right invariant for comparison-geometry questions.

> [!tip] Sphere Theorem *(from Comparison Geometry)*
> A simply-connected, complete Riemannian manifold with $1/4 < K \le 1$ is homeomorphic to $S^n$ (Berger–Klingenberg, $1960$s) and in fact *diffeomorphic* to $S^n$ (**Brendle–Schoen**, $2009$, via Ricci flow). The constant $1/4$ is sharp: $\mathbb{CP}^n$ saturates it and is not homeomorphic to a sphere.

> [!tip] Curvature Operator Positivity *(from Geometric Analysis)*
> A condition stronger than positive sectional curvature is **positive curvature operator**, $\mathcal{R} > 0$ on $\Lambda^2 T_pM$. This stronger condition implies positive sectional curvature but is not equivalent in dimension $\ge 4$. Hamilton's Ricci-flow analysis on manifolds with positive curvature operator is the starting point of the modern sphere-theorem programme.
