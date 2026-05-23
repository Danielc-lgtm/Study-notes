---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Embedded Submanifold"
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Pullback of a Covariant Tensor Field"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

Let $(M, g)$ be a Riemannian manifold and let $\iota : S \hookrightarrow M$ be an immersed or embedded submanifold. The **induced metric** on $S$ is denoted $\iota^* g$ (the pullback of $g$ along $\iota$), or sometimes just $g|_S$ or $\bar g$ when context is clear. For a more general smooth immersion $F : N \to M$ rather than an inclusion, the same construction gives the **pullback metric** $F^*g$ on $N$. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Axiom Motivation

The desideratum is to make submanifolds of a Riemannian manifold into Riemannian manifolds themselves, in a canonical way. The whole apparatus of Riemannian geometry — length of curves, distance, angles, gradients — should be available not just on $M$ but on every submanifold $S \subseteq M$ as well. The natural way to do this is to *restrict* the inner product structure of $M$ to the tangent spaces of $S$.

The picture is concrete: a tangent vector to $S$ at $p$ is also a tangent vector to $M$ at $p$, via the inclusion $\iota_*: T_pS \hookrightarrow T_pM$. The Riemannian metric $g$ on $M$ gives an inner product on $T_pM$; restricting this inner product to the [[Def - Subspace|subspace]] $T_pS \subseteq T_pM$ gives an inner product on $T_pS$. Doing this at every point of $S$ produces the induced inner product structure — the induced metric on $S$.

The single thing to check is that this restriction is again *positive-definite* — that is, that the restriction of a positive-definite inner product to a [[Def - Subspace|subspace]] is positive-definite. This is automatic from linear algebra: $g_p(v, v) > 0$ for every nonzero $v \in T_pM$ in particular implies $g_p(v, v) > 0$ for every nonzero $v \in T_pS \subseteq T_pM$. So the induced metric is automatically a Riemannian metric.

The same construction does *not* always work for pseudo-Riemannian metrics: the restriction of a non-degenerate indefinite form to a subspace can be degenerate. For instance, the Minkowski metric $\eta$ on $\mathbb{R}^4$ is non-degenerate, but its restriction to a null hyperplane (a hyperplane tangent to the light cone) is degenerate. So the analogous induced-metric construction for semi-Riemannian manifolds requires an additional condition: the metric restricted to the submanifold must remain non-degenerate. This is the source of the **non-degeneracy condition** in semi-Riemannian submanifold theory. In the Riemannian case it is free.

A second check: the construction must give a *smooth* tensor field on $S$, not just a pointwise inner product. This is the [[Def - Pullback of a Covariant Tensor Field|smoothness of pullback]] of covariant tensor fields: if $g$ is a smooth $(0, 2)$-tensor field on $M$ and $\iota : S \hookrightarrow M$ is smooth, then $\iota^* g$ is a smooth $(0, 2)$-tensor field on $S$. This is the general fact about pullbacks of covariant tensors, applied here.

A third subtlety: the metric on the *immersed* submanifold $S$ is well-defined only because the immersion $\iota_*$ is injective at each point — different tangent vectors to $S$ go to different tangent vectors of $M$, so restricting an inner product on $T_pM$ to $T_pS$ makes sense. For a *non-injective* map $F : N \to M$, the pullback $F^*g$ is still a covariant tensor field, but it might be degenerate (positive semi-definite rather than positive-definite) at points where $dF$ has nontrivial kernel. The induced metric on a submanifold avoids this by using only immersions, where $dF$ is injective everywhere.

Finally: the choice to use the pullback rather than some other construction is forced by the requirement of naturality. If $\phi : T \to S$ is a smooth map between submanifolds of $M$, then the inclusions compose: $\iota_T = \iota_S \circ \phi$, and pullbacks are functorial: $\iota_T^* g = \phi^* \iota_S^* g$. So the induced metric on $T$ obtained via $S$ is the same as the induced metric obtained directly from $M$ — a coherence statement that any other construction would have to verify but that pullbacks satisfy automatically.

---

# The Definition

> **Definition (Induced Metric).** Let $(M, g)$ be a Riemannian manifold, and let $\iota : S \hookrightarrow M$ be an immersed or embedded submanifold. The **induced metric** on $S$ is the [[Def - Pullback of a Covariant Tensor Field|pullback]] $\iota^* g$ — the $(0, 2)$-tensor field on $S$ defined by
> $$
> (\iota^* g)_p(v, w) \;=\; g_{\iota(p)}\bigl(\iota_*v,\ \iota_*w\bigr) \qquad \text{for } v, w \in T_pS.
> $$

Since $\iota_*$ is injective at each $p$ (immersion), the right-hand side is a positive-definite inner product on $T_pS$, so $\iota^* g$ is itself a Riemannian metric on $S$. The submanifold $S$, equipped with $\iota^* g$, is a **Riemannian submanifold** of $M$.

More generally, for any smooth immersion $F : N \to M$ (not necessarily an inclusion), the same formula defines the **pullback metric** $F^* g$ on $N$, which is a Riemannian metric on $N$. The submanifold case is the special case where $F$ is the inclusion of $S$ as a subset of $M$.

**Computation in coordinates.** Suppose $S$ is parametrised locally by $X : U \subseteq \mathbb{R}^k \to M$, with $U$ open and $X$ a smooth immersion (an *immersed parametrisation*). Writing the parametrisation in ambient coordinates $X(u^1, \ldots, u^k) = (X^1(u), \ldots, X^n(u))$ in a chart of $M$, the induced metric has matrix
$$
(X^* g)_{\alpha\beta}(u) \;=\; g_{ij}(X(u))\, \frac{\partial X^i}{\partial u^\alpha} \frac{\partial X^j}{\partial u^\beta} \qquad (\alpha, \beta = 1, \ldots, k).
$$
In particular, when $M = \mathbb{R}^n$ with the Euclidean metric ($g_{ij} = \delta_{ij}$), this simplifies to
$$
(X^* \bar g)_{\alpha\beta}(u) \;=\; \sum_{i=1}^n \frac{\partial X^i}{\partial u^\alpha} \frac{\partial X^i}{\partial u^\beta} \;=\; \bigl\langle \partial_\alpha X,\ \partial_\beta X\bigr\rangle_{\bar g},
$$
the **first fundamental form** of classical differential geometry of curves and surfaces.

---

# Relate to Other Fields / Compression

This is the modern abstraction of the classical "first fundamental form" of a parametrised surface in $\mathbb{R}^3$. Given a parametrised surface $X : U \subseteq \mathbb{R}^2 \to \mathbb{R}^3$, the classical first fundamental form is the matrix
$$
\begin{pmatrix} E & F \\ F & G \end{pmatrix} \;=\; \begin{pmatrix} \langle X_u, X_u \rangle & \langle X_u, X_v \rangle \\ \langle X_v, X_u \rangle & \langle X_v, X_v \rangle \end{pmatrix},
$$
recording arc length, area, and angle on the surface in terms of the ambient Euclidean inner product. This is exactly the induced metric in the special case where the ambient manifold is $\mathbb{R}^3$ with the Euclidean metric and the submanifold is a parametrised surface. The induced-metric construction generalises this from surfaces in $\mathbb{R}^3$ to arbitrary submanifolds in arbitrary Riemannian manifolds.

The connection to [[Multivariate Analysis II — Inverse and Implicit Function Theorems|the regular value theorem]]: most submanifolds in practice arise as preimages $f^{-1}(c)$ of regular values of smooth functions, and the induced metric on such a preimage is computed from the parametric form. The classical "level set is a submanifold" theorem combined with the induced metric construction is how spheres, hyperboloids, tori, and most concrete Riemannian manifolds are built.

**True name:** The induced metric is *the restriction of the ambient inner product to tangent subspaces of the submanifold*. The pullback formula $\iota^* g$ is the formal mechanism; the picture is "stop at the submanifold and use the ambient inner product on whatever vectors are along".

---

# Examples / Corollaries

**Is an instance — the round metric on $S^n$.** The induced metric from the inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$, with $\mathbb{R}^{n+1}$ carrying the Euclidean metric, is the round metric $\mathring g$. In stereographic or spherical-coordinate parametrisations it has the standard forms; see [[Ex - The Round Metric on the Sphere via Restriction]].

**Is an instance — the cylinder metric.** The cylinder $\{(x, y, z) : x^2 + y^2 = 1\}$ in $\mathbb{R}^3$, with the induced Euclidean metric, has metric $d\theta^2 + dz^2$ in coordinates $(\theta, z)$ — the *flat* metric, locally isometric to $\mathbb{R}^2$. The cylinder is curved as an embedding (it is not a plane), but its intrinsic geometry is flat — this is the classical distinction between intrinsic and extrinsic curvature.

**Is an instance — surfaces of revolution.** For a curve $(a(t), b(t))$ in the half-plane $\{r > 0\}$, the surface of revolution $X(t, \theta) = (a(t)\cos\theta, a(t)\sin\theta, b(t))$ has induced metric $(a'(t)^2 + b'(t)^2) dt^2 + a(t)^2 d\theta^2$. If the curve is unit-speed ($a'^2 + b'^2 = 1$), this simplifies to $dt^2 + a(t)^2 d\theta^2$. The sphere ($a = \sin t$, $b = -\cos t$), the cylinder ($a = 1$, $b = t$), and the catenoid ($a = \cosh t$, $b = t$ — modulo arc-length reparametrisation) all fall under this pattern.

**Is an instance — graphs as submanifolds.** For an open $U \subseteq \mathbb{R}^n$ and a smooth $f : U \to \mathbb{R}$, the graph $\{(x, f(x)) : x \in U\} \subseteq \mathbb{R}^{n+1}$ is an embedded submanifold parametrised by $X(x) = (x, f(x))$. The induced metric is $\sum (dx^i)^2 + df^2 = (\delta_{ij} + \partial_i f \partial_j f)\, dx^i dx^j$.

**Is NOT an instance — a curve of velocity zero.** If $\gamma : I \to M$ is a smooth map with $\gamma'(t_0) = 0$ at some $t_0$, then $\gamma$ is not an immersion at $t_0$. The "pullback metric" $\gamma^* g$ has the value $(\gamma^* g)_{t_0}(\partial_t, \partial_t) = g_{\gamma(t_0)}(0, 0) = 0$, so it is degenerate. This is *not* an induced metric in our sense, because the map is not an immersion.

**Is NOT an instance — restriction without pullback.** The set-theoretic restriction "use $g_p$ on $T_pS$ for $p \in S$" looks like the induced metric and *is* the same thing — but to make it a coherent tensor field on $S$ rather than a pointwise restriction, one needs the smoothness coming from the pullback construction. The naive set-theoretic picture is right but does not establish smoothness; the pullback formalism does.

**Corollary — restriction of induced metric is induced metric.** If $T \subseteq S \subseteq M$ is a chain of submanifolds, then the induced metric on $T$ as a submanifold of $M$ equals the induced metric on $T$ as a submanifold of $(S, \iota^* g)$. This is the functoriality of pullback.

**Corollary — induced metric is a Riemannian metric.** The pullback $\iota^* g$ of a Riemannian metric along an immersion is again a Riemannian metric (smooth, symmetric, positive-definite). The positive-definiteness uses the injectivity of $\iota_*$ and the positive-definiteness of $g$.

**Calibration check.** First, compute the induced metric on the unit circle $S^1 \subseteq \mathbb{R}^2$ in the parametrisation $X(\theta) = (\cos\theta, \sin\theta)$. Expected: $g = d\theta^2$, the standard arc-length parametrisation. Second, compute the induced metric on the helix $X(t) = (\cos t, \sin t, t)$ in $\mathbb{R}^3$. Expected: $g = 2\, dt^2$, since $|\dot X|^2 = \sin^2 t + \cos^2 t + 1 = 2$. Third, verify that the induced metric is *not* changed by reparametrising the submanifold: a different parametrisation of the same $S$ gives the same metric (in the sense that the two coordinate expressions are related by the Jacobian of the parametrisation change).

---

# Unlocked by This

> [!tip] Concrete Riemannian Manifolds *(from Riemannian Geometry)*
> Every concrete Riemannian manifold one ever computes with is constructed via the induced metric: the sphere, the torus, the hyperboloid, surfaces of revolution, the matrix Lie groups as submanifolds of $\mathbb{R}^{n^2}$. The induced-metric construction is the workhorse of Riemannian geometry, and learning to compute pullbacks fluently is the practical skill of the chapter.

> [!tip] The Nash Embedding Theorem *(from Riemannian Geometry)*
> A deep result of John Nash asserts that *every* Riemannian manifold can be isometrically embedded in some Euclidean space $\mathbb{R}^N$ (with $N$ sufficiently large). So the induced-metric construction is in principle universal: every Riemannian manifold is, up to isometry, a submanifold of some $\mathbb{R}^N$. The catch is that $N$ can be very large compared to $n$, and the embedding is highly non-canonical, so for theoretical purposes one usually prefers the abstract definition.

> [!tip] Submanifold Geometry and the Second Fundamental Form *(from Riemannian Geometry)*
> The induced metric is the **first fundamental form**; the **second fundamental form** records how $S$ is curved within $M$ — the normal component of $\nabla_X Y$ for $X, Y$ tangent to $S$. Together they govern submanifold geometry: the Gauss equation relates the intrinsic curvature of $S$, the curvature of $M$, and the second fundamental form; the Codazzi equation governs how the second fundamental form propagates. This is the content of submanifold theory in Riemannian geometry.
