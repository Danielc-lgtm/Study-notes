---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Riemannian Manifold"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Problem Statement

The **upper half-plane** is the open subset
$$
\mathbb{H}^2 \;=\; \{(x, y) \in \mathbb{R}^2 \;:\; y > 0\}
$$
of $\mathbb{R}^2$. Equip it with the tensor field
$$
g_{\mathbb{H}} \;=\; \frac{dx^2 + dy^2}{y^2}.
$$

(a) Verify that $g_{\mathbb{H}}$ is a Riemannian metric on $\mathbb{H}^2$ — that is, smooth, symmetric, and positive-definite.

(b) Compute the length of the vertical segment $\gamma(t) = (x_0, t)$ for $t \in [a, b]$ with $0 < a < b$.

(c) Show that $g_{\mathbb{H}}$ is *not* equal to the Euclidean metric on $\mathbb{H}^2$ — these are two genuinely different Riemannian metrics on the same smooth manifold.

The hyperbolic plane $(\mathbb{H}^2, g_{\mathbb{H}})$ is one of the three classical model geometries (Euclidean, spherical, hyperbolic), with constant negative Gaussian curvature $-1$.

**Recall:**

![[Def - Riemannian Metric#The Definition]]

A smooth tensor field is positive-definite at a point if its matrix in any basis has all positive eigenvalues (equivalently, all principal minors positive).

The Euclidean metric on $\mathbb{R}^2$ in Cartesian coordinates is $\bar g = dx^2 + dy^2$, the constant tensor field with $\bar g_{ij} = \delta_{ij}$.

---

# Convergent Strategy

**Problem class.** This is a *verify a candidate metric and compute lengths* problem. The [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Problem-Solving Strategy|problem-solving strategy]] is mechanical for the verification part (check smoothness, symmetry, positive-definiteness of $g_{ij}$), and direct for the length computation (apply the formula $L_g(\gamma) = \int |\dot\gamma|_g\, dt$ with the given $g$).

**Assumption pattern.** The setup: an explicit formula $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$ — a *conformal rescaling* of the Euclidean metric by the positive smooth function $1/y^2$ on $\mathbb{H}^2$ (where $y > 0$). Conformal rescalings of a Riemannian metric by a positive function are again Riemannian metrics, so the verification is automatic once you notice the conformal structure. The conformal factor $1/y^2$ blows up as $y \to 0$ (the boundary of $\mathbb{H}^2$), reflecting the unbounded hyperbolic distance from any interior point to the boundary.

**Theorem routing.** For (a): the metric components are $g_{ij} = (1/y^2)\delta_{ij}$ in $(x, y)$ coordinates. Smoothness: $1/y^2$ is smooth on $\mathbb{H}^2$ since $y > 0$. Symmetry: $\delta_{ij}$ is symmetric, scalar multiples are too. Positive-definiteness: $1/y^2 > 0$ and $\delta_{ij}$ is positive-definite, so the scalar multiple is positive-definite. For (b): the vertical segment $\gamma(t) = (x_0, t)$ has $\dot\gamma = (0, 1)$ and $|\dot\gamma|_g^2 = g_{ij}\dot\gamma^i\dot\gamma^j = (1/t^2) \cdot 1 = 1/t^2$, so $|\dot\gamma|_g = 1/t$. The length is $\int_a^b 1/t\, dt = \log(b/a)$. For (c): the Euclidean metric has $\bar g_{ij} = \delta_{ij}$ uniformly, while $g_{\mathbb{H}}_{ij}(x, y) = (1/y^2)\delta_{ij}$ depends on $y$ — these are not equal pointwise.

**Key decision point.** The non-obvious part is *recognising that the hyperbolic length grows logarithmically as $a \to 0$*. The vertical segment from $(x_0, 1)$ to $(x_0, \varepsilon)$ has hyperbolic length $\log(1/\varepsilon) = -\log\varepsilon \to \infty$ as $\varepsilon \to 0$. So the "Euclidean boundary" $y = 0$ is at *infinite* hyperbolic distance — it is not part of $\mathbb{H}^2$ and is unreachable by curves of finite hyperbolic length. This is the geometric content of "hyperbolic space has constant negative curvature": [[Def - Geodesic|geodesics]] diverge from each other faster than in Euclidean space, and the boundary recedes to infinity.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Legal Operations|the topic page's Legal Operations]]:

5. **Verify positive-definiteness or non-degeneracy in coordinates** (operation 5). The matrix of $g_{\mathbb{H}}$ in $(x, y)$ coordinates is $(1/y^2)\delta_{ij}$ — a positive scalar times the identity matrix, hence positive-definite for all $y > 0$.

2. **Compute $g$ in coordinates by substitution** (operation 2) — implicit. The conformal rescaling $g_{\mathbb{H}} = (1/y^2)\bar g$ is a direct expression in terms of a known metric.

(Also: the length computation is a direct application of the [[Def - Length of a Curve and Riemannian Distance|length formula]].)

---

# Hints

> [!note]- Hint 1
> Write the metric components: $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$ means $g_{11} = 1/y^2 = g_{22}$, $g_{12} = g_{21} = 0$. So the metric matrix is $(1/y^2) \cdot I$, a positive scalar times the identity. This is a **conformally Euclidean** metric.

> [!note]- Hint 2
> For positive-definiteness, the matrix $(1/y^2)\delta_{ij}$ is positive-definite at every point $(x, y) \in \mathbb{H}^2$ because $1/y^2 > 0$ (since $y > 0$) and $\delta_{ij}$ is the identity matrix.

> [!note]- Hint 3
> For the length of the vertical segment $\gamma(t) = (x_0, t)$, $t \in [a, b]$: $\dot\gamma = (0, 1)$, so $|\dot\gamma|^2_{g_{\mathbb{H}}} = g_{ij}(\gamma(t))\dot\gamma^i\dot\gamma^j = (1/t^2)(0^2 + 1^2) = 1/t^2$. Hence $|\dot\gamma|_{g_{\mathbb{H}}} = 1/t$, and $L = \int_a^b (1/t)\, dt = \log(b/a)$.

---

# Solution

The proof breaks into three parts matching the parts of the problem. Part (a) verifies the metric properties using the conformal-rescaling structure. Part (b) computes the length of a vertical segment to illustrate the metric's structure. Part (c) shows $g_{\mathbb{H}} \neq \bar g$ by direct comparison. The decisive insight is that $g_{\mathbb{H}}$ is the Euclidean metric *rescaled* by the position-dependent factor $1/y^2$ — a conformal rescaling — and that this rescaling makes distances "longer" near the boundary $y = 0$ and "shorter" near $y = \infty$.

**Part (a): $g_{\mathbb{H}}$ is a Riemannian metric on $\mathbb{H}^2$.**

> [!note]- Derivation
> In Cartesian coordinates $(x, y)$ on $\mathbb{H}^2 \subseteq \mathbb{R}^2$, the tensor field $g_{\mathbb{H}}$ has components
> $$
> g_{\mathbb{H}, ij}(x, y) = \frac{1}{y^2} \delta_{ij} = \begin{pmatrix} 1/y^2 & 0 \\ 0 & 1/y^2 \end{pmatrix}.
> $$
>
> **Smoothness.** The function $1/y^2$ is smooth on the open set $\mathbb{H}^2 = \{y > 0\}$ (it is the composition of the smooth function $y \mapsto y^2$ and the smooth function $z \mapsto 1/z$ on $z > 0$). The components $g_{\mathbb{H}, ij}$ are scalar multiples of constants by a smooth function, hence smooth.
>
> **Symmetry.** The matrix $(1/y^2)\delta_{ij}$ is symmetric ($\delta_{ij} = \delta_{ji}$, and scalar multiplication preserves symmetry).
>
> **Positive-definiteness.** At every $(x, y) \in \mathbb{H}^2$, the factor $1/y^2 > 0$ (since $y > 0$). For any nonzero $v = (v^1, v^2) \in T_{(x,y)}\mathbb{H}^2$,
> $$
> g_{\mathbb{H}}(v, v) = \frac{1}{y^2}\bigl((v^1)^2 + (v^2)^2\bigr) > 0,
> $$
> since the Euclidean norm-squared of a nonzero vector is strictly positive and $1/y^2$ is strictly positive.
>
> Hence $g_{\mathbb{H}}$ is smooth, symmetric, positive-definite — a Riemannian metric on $\mathbb{H}^2$.

**Part (b): Length of the vertical segment.**

For $\gamma(t) = (x_0, t)$, $t \in [a, b]$ with $0 < a < b$:
$$
L_{g_{\mathbb{H}}}(\gamma) = \log\frac{b}{a}.
$$

> [!note]- Derivation
> The velocity of $\gamma$ is $\dot\gamma(t) = (0, 1) \in T_{(x_0, t)}\mathbb{H}^2$. Compute the $g_{\mathbb{H}}$-norm:
> $$
> |\dot\gamma(t)|_{g_{\mathbb{H}}}^2 = g_{\mathbb{H},ij}(\gamma(t))\, \dot\gamma^i\, \dot\gamma^j = \frac{1}{t^2}(0^2 + 1^2) = \frac{1}{t^2}.
> $$
> So $|\dot\gamma(t)|_{g_{\mathbb{H}}} = 1/t$.
>
> The length is then
> $$
> L_{g_{\mathbb{H}}}(\gamma) = \int_a^b |\dot\gamma(t)|_{g_{\mathbb{H}}}\, dt = \int_a^b \frac{1}{t}\, dt = \log b - \log a = \log\frac{b}{a}.
> $$

**Part (c): $g_{\mathbb{H}} \neq \bar g$.**

The two metrics have different component matrices at any point with $y \neq 1$.

> [!note]- Derivation
> The Euclidean metric on $\mathbb{H}^2$ in Cartesian coordinates is $\bar g = dx^2 + dy^2$, with components $\bar g_{ij} = \delta_{ij}$ at every point. The hyperbolic metric is $g_{\mathbb{H}} = (1/y^2)(dx^2 + dy^2)$, with components $g_{\mathbb{H}, ij}(x, y) = (1/y^2)\delta_{ij}$.
>
> At the point $(0, 2) \in \mathbb{H}^2$: $\bar g_{11}(0, 2) = 1$, while $g_{\mathbb{H}, 11}(0, 2) = 1/4 \neq 1$. So the two metrics disagree at this point, hence as global tensor fields they are different.
>
> Concretely, the Euclidean length of the vertical segment from $(0, 1)$ to $(0, 2)$ is $1$ (the Euclidean distance), but the hyperbolic length of the same segment is $\log 2 \approx 0.693 \neq 1$. Different lengths confirm different metrics.

> [!note]- Complete formal solution
> Let $\mathbb{H}^2 = \{(x, y) \in \mathbb{R}^2 : y > 0\}$ with $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$.
>
> **Part (a):** In Cartesian coordinates, $g_{\mathbb{H},ij}(x, y) = (1/y^2)\delta_{ij}$. Smoothness: $1/y^2$ is smooth on $\mathbb{H}^2$ since $y > 0$. Symmetry: matrix is diagonal hence symmetric. Positive-definiteness: at any $(x, y) \in \mathbb{H}^2$, for nonzero $v$, $g_{\mathbb{H}}(v, v) = (1/y^2)|v|^2_{\bar g} > 0$. Hence $g_{\mathbb{H}}$ is a Riemannian metric on $\mathbb{H}^2$.
>
> **Part (b):** The vertical segment $\gamma(t) = (x_0, t)$, $t \in [a, b]$, has velocity $\dot\gamma = (0, 1)$, hence $|\dot\gamma|^2_{g_{\mathbb{H}}} = (1/t^2)(0^2 + 1^2) = 1/t^2$, so $|\dot\gamma|_{g_{\mathbb{H}}} = 1/t$.
> $$
> L_{g_{\mathbb{H}}}(\gamma) = \int_a^b \frac{1}{t}\, dt = \log\frac{b}{a}.
> $$
>
> **Part (c):** At $(0, 2)$, $\bar g_{11} = 1$ but $g_{\mathbb{H}, 11} = 1/4$. So the metrics differ pointwise, hence differ as global tensor fields. The hyperbolic length of the vertical segment from $(0, 1)$ to $(0, 2)$ is $\log 2$, but the Euclidean length is $1$ — different values confirm different metrics. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to identify $\mathbb{H}^2$ with the Euclidean plane $\{y > 0\}$ by saying "it's a subset of $\mathbb{R}^2$, so it inherits the Euclidean metric". This is true — $\mathbb{H}^2$ does inherit the Euclidean metric as the *induced metric* from its embedding — but the *hyperbolic* metric $g_{\mathbb{H}}$ is a *different* metric, not induced from the embedding. They are both legitimate Riemannian metrics on the same smooth manifold $\mathbb{H}^2$, but they are not equal, and they give different geometries (Euclidean flat vs. hyperbolic constantly negatively curved). The choice of metric is not forced by the smooth structure.

---

# Key Takeaways

**Conformal rescalings of a Riemannian metric are Riemannian metrics.** A common construction: take a Riemannian metric $g$ and multiply it by a smooth positive function $e^{2\sigma(x)}$ to obtain a new metric $\tilde g = e^{2\sigma} g$. The new metric is still smooth, symmetric, and positive-definite (positive scalar times positive-definite is positive-definite), so it is a Riemannian metric. Two metrics related this way are **conformally equivalent**, and they preserve angles (the angle between two tangent vectors at a point depends only on the conformal class of the metric) but not lengths. The hyperbolic metric $g_{\mathbb{H}} = (1/y^2)\bar g$ is the conformal rescaling of the Euclidean metric by the factor $1/y^2$ on $\mathbb{H}^2$. Many of the most important Riemannian metrics in mathematics — the Fubini–Study metric on $\mathbb{CP}^n$, the hyperbolic metric on $\mathbb{H}^n$, the round metric on $S^n$ as a conformal rescaling of stereographic Euclidean — are obtained by conformal rescaling, and recognising the pattern is the reusable insight.

**The same smooth manifold can carry many genuinely different Riemannian metrics.** The open subset $\mathbb{H}^2 \subseteq \mathbb{R}^2$ is a single smooth manifold, but it admits at least two distinct Riemannian metrics — the induced Euclidean metric and the hyperbolic metric. These give different geometries (flat vs. constantly negatively curved), different distance functions, different [[Def - Geodesic|geodesics]], different volumes, different [[Def - Isometry|isometry]] [[Def - Group|groups]]. The geometric content of "$(M, g)$" depends on *both* the manifold and the metric, and changing the metric changes everything geometric while leaving the smooth structure intact. The reusable lesson: never assume "the geometry" of a smooth manifold without specifying a metric. The smooth manifold is a chassis; the metric is the engine.

**Hyperbolic distance blows up logarithmically near the boundary.** The boundary $y = 0$ of $\mathbb{H}^2$ — a *Euclidean* boundary in the embedding into $\mathbb{R}^2$ — is at *infinite* hyperbolic distance from any interior point. Specifically, the hyperbolic length of the vertical segment from $(x_0, 1)$ to $(x_0, \varepsilon)$ is $\log(1/\varepsilon)$, which goes to $\infty$ as $\varepsilon \to 0$. So the boundary is unreachable in the hyperbolic metric, and $(\mathbb{H}^2, g_{\mathbb{H}})$ is a *complete* Riemannian manifold despite having a Euclidean boundary — completeness depends on the metric, not on the embedding. The reusable lesson: completeness of a Riemannian manifold is determined by the metric, and a manifold can be "topologically incomplete" (have a Euclidean boundary) while being "geometrically complete" (no Cauchy sequence diverges from interior to boundary in finite hyperbolic distance). This is the conceptual content of the **Hopf–Rinow theorem** applied to $\mathbb{H}^2$.

**Cross-link to companion exercises:** [[Ex - The Round Metric on the Sphere via Restriction]] gives the round metric on $S^2$ — the positive-curvature constant-curvature companion. Together, hyperbolic plane and round sphere are the two non-trivial constant-curvature model geometries; the flat plane $(\mathbb{R}^2, \bar g)$ is the third. The classical Killing–Hopf theorem classifies simply connected constant-curvature Riemannian manifolds into exactly these three families (up to scale): Euclidean, spherical, hyperbolic.
