---
type: exercise
subject: riemannian-geometry
difficulty: "⭐"
prereqs:
  - "Def - Christoffel Symbols"
  - "Def - Levi-Civita Connection"
  - "Def - Curvature 2-Forms (Cartan)"
tags: [geometry, riemannian-geometry, connections]
---

# Problem Statement

Compute the Christoffel symbols of the Euclidean metric $g = dr^2 + r^2\,d\theta^2$ on $\mathbb{R}^2 \setminus \{0\}$ in polar coordinates. Verify the connection is *flat* by computing the curvature 2-forms in the coordinate frame (the Christoffel-based curvature formula) and showing they vanish. Contrast with the trivial connection $\nabla \equiv 0$ in Cartesian coordinates.

**Recall:**

The Christoffel formula for the Levi-Civita connection of a Riemannian metric $g$ in local coordinates is

![[Def - Christoffel Symbols#The Definition]]

The Riemann curvature tensor components in a coordinate frame are
$$
R^l{}_{ijk} = \partial_i \Gamma^l_{jk} - \partial_j \Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}.
$$
A connection is **flat** if the Riemann tensor vanishes identically.

The Euclidean plane $\mathbb{R}^2$ has the flat metric in Cartesian coordinates $g = dx^2 + dy^2$, with all Christoffel symbols zero. In polar coordinates $(r, \theta)$ where $x = r\cos\theta, y = r\sin\theta$, the same metric becomes $g = dr^2 + r^2\,d\theta^2$.

---

# Convergent Strategy

**Problem class:** A *transformation* exercise: the same Riemannian connection — the flat connection on $\mathbb{R}^2$ — is being described in two coordinate systems, and the Christoffel symbols differ because they are not tensorial. The point is to verify that the connection is flat (curvature zero) regardless of the coordinates, even though the Christoffel symbols are nonzero in polar.

**Assumption pattern:** A diagonal metric $g = dr^2 + r^2 d\theta^2$ is given, with only $g_{\theta\theta} = r^2$ having a nontrivial derivative ($\partial_r g_{\theta\theta} = 2r$). This is the simplest possible non-flat coordinate frame on the flat plane — and is the canonical illustration of "$\Gamma$ is not a tensor".

**Theorem routing:** Apply the [[Def - Christoffel Symbols|Christoffel formula]] to get the few nonzero $\Gamma^k_{ij}$. Then compute the [[Def - Curvature 2-Forms (Cartan)|Riemann tensor components]] from the coordinate formula and verify they vanish, confirming the connection is flat. The cancellation between $\partial\Gamma$ terms and $\Gamma\Gamma$ terms is the explicit demonstration of "zero in the abstract sense, despite nonzero coordinate components".

**Key decision point:** The non-obvious move is recognising that the cancellation in $R^l{}_{ijk}$ is *exact*, not approximate. The formula $\partial_i\Gamma^l_{jk} - \partial_j\Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}$ has four terms, two with $\partial$ and two with $\Gamma\Gamma$, and they cancel in pairs after using the specific values of $\Gamma$. This is the algebraic confirmation that the connection is "really" flat — the polar Christoffels are gauge artefacts, not curvature.

---

# Legal Operations Used

1. **Operation 1 from the topic page (Compute Christoffel symbols from the metric).** Apply the Christoffel formula to the polar metric. Few terms are nonzero.

2. **Operation 7 from the topic page (Change frame and transform the connection via the gauge law).** The polar Christoffels in the coordinate frame and the Cartesian Christoffels (all zero) in the Cartesian frame are related by the change-of-frame matrix (the Jacobian of the coordinate change). The gauge-transformation law $\Gamma' = g^{-1}\Gamma g + g^{-1}dg$ accounts for the difference.

---

# Hints

> [!note]- Hint 1
> The metric is $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = 0$. The inverse is $g^{rr} = 1, g^{\theta\theta} = 1/r^2$.

> [!note]- Hint 2
> The only nonzero metric derivative is $\partial_r g_{\theta\theta} = 2r$. By the Christoffel formula, the nonzero entries are $\Gamma^r_{\theta\theta} = -r$ (from $-\tfrac{1}{2}\partial_r g_{\theta\theta}$) and $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$ (from $\tfrac{1}{2}g^{\theta\theta}\partial_r g_{\theta\theta}$).

> [!note]- Hint 3
> To verify flatness, compute $R^l{}_{ijk}$ in coordinates. The only potentially nonzero component is $R^r{}_{\theta r\theta}$ (or $R^\theta{}_{r r\theta}$, related by symmetry). The four terms must cancel.

---

# Solution

**Plan paragraph.** The solution has three steps. Step 1 computes the Christoffel symbols of the polar Euclidean metric (a 5-minute calculation). Step 2 plugs them into the Riemann tensor coordinate formula and verifies the four-term sum cancels to zero. Step 3 explains the connection to the Cartesian description via the gauge-transformation law: the polar Christoffels are the "$g^{-1}dg$" piece of changing frame from Cartesian to polar.

**Step 1: Christoffel symbols.**

From $g = dr^2 + r^2\,d\theta^2$: $g_{rr} = 1, g_{\theta\theta} = r^2$, $g_{r\theta} = 0$; inverse $g^{rr} = 1, g^{\theta\theta} = 1/r^2$. The only nontrivial derivative is $\partial_r g_{\theta\theta} = 2r$.

Apply the Christoffel formula:
- $\Gamma^r_{\theta\theta} = \tfrac{1}{2}g^{rr}(\partial_\theta g_{\theta r} + \partial_\theta g_{\theta r} - \partial_r g_{\theta\theta}) = \tfrac{1}{2}(0 + 0 - 2r) = -r$.
- $\Gamma^\theta_{r\theta} = \tfrac{1}{2}g^{\theta\theta}(\partial_r g_{\theta\theta} + \partial_\theta g_{r\theta} - \partial_\theta g_{r\theta}) = \tfrac{1}{2}(1/r^2)(2r) = 1/r$.
- $\Gamma^\theta_{\theta r} = \Gamma^\theta_{r\theta} = 1/r$ by symmetry.
- All others vanish.

> [!note]- Derivation
> Methodically apply $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. The inverse metric is diagonal, so only $l = k$ contributes. For $k = r$: $\Gamma^r_{ij} = \tfrac{1}{2}(\partial_i g_{jr} + \partial_j g_{ir} - \partial_r g_{ij})$. $g_{jr} = \delta_{jr}$ is constant, so the first two terms vanish; the third is nonzero only for $(i, j) = (\theta, \theta)$, giving $\Gamma^r_{\theta\theta} = -\tfrac{1}{2}\cdot 2r = -r$. For $k = \theta$: $\Gamma^\theta_{ij} = \tfrac{1}{2r^2}(\partial_i g_{j\theta} + \partial_j g_{i\theta} - \partial_\theta g_{ij})$. $\partial_\theta g_{ij} = 0$ (metric independent of $\theta$). $g_{j\theta} = r^2 \delta_{j\theta}$, $\partial_r g_{j\theta} = 2r\delta_{j\theta}$, $\partial_\theta g_{j\theta} = 0$. So $\partial_i g_{j\theta}$ is nonzero only when $i = r$ and $j = \theta$. Hence $\Gamma^\theta_{r\theta} = \tfrac{1}{2r^2}\cdot 2r = 1/r$, and by symmetry $\Gamma^\theta_{\theta r} = 1/r$.

**Summary:**
$$
\Gamma^r_{\theta\theta} = -r, \qquad \Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \tfrac{1}{r}, \qquad \text{all others} = 0.
$$

**Step 2: Verify the Riemann tensor vanishes.**

The only potentially nonzero component, by symmetry of the polar Christoffels, is $R^r{}_{\theta r\theta}$ (and its symmetries). Apply the coordinate formula:
$$
R^r{}_{\theta r\theta} = \partial_r \Gamma^r_{\theta\theta} - \partial_\theta \Gamma^r_{r\theta} + \Gamma^r_{rm}\Gamma^m_{\theta\theta} - \Gamma^r_{\theta m}\Gamma^m_{r\theta}.
$$

Term-by-term:
- $\partial_r \Gamma^r_{\theta\theta} = \partial_r(-r) = -1$.
- $\partial_\theta \Gamma^r_{r\theta} = \partial_\theta(0) = 0$.
- $\Gamma^r_{rm}\Gamma^m_{\theta\theta}$ summed over $m$: $\Gamma^r_{rr}\Gamma^r_{\theta\theta} + \Gamma^r_{r\theta}\Gamma^\theta_{\theta\theta} = 0\cdot(-r) + 0\cdot 0 = 0$.
- $\Gamma^r_{\theta m}\Gamma^m_{r\theta}$ summed over $m$: $\Gamma^r_{\theta r}\Gamma^r_{r\theta} + \Gamma^r_{\theta\theta}\Gamma^\theta_{r\theta} = 0\cdot 0 + (-r)\cdot(1/r) = -1$.

Sum: $R^r{}_{\theta r\theta} = -1 - 0 + 0 - (-1) = -1 + 1 = 0$. ✓

The cancellation between the $\partial$-term ($-1$) and the $\Gamma\Gamma$-term ($-1$ with the minus sign in front making it $+1$) is exact. The connection is flat.

> [!note]- Derivation
> $R^l{}_{ijk} = \partial_i\Gamma^l_{jk} - \partial_j\Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}$.
>
> With $(l, i, j, k) = (r, \theta, r, \theta)$ — i.e., $R^r{}_{\theta r\theta}$, no wait. Let me re-index: the convention is $R^l{}_{ijk}$ where the lower indices are antisymmetric in $(j, k)$ (or in $(i, j)$ depending on convention). Frankel uses $R^i{}_{jkl}$ with the second-pair antisymmetry. Let's compute $R^r{}_{\theta r\theta}$ (which means: $\nabla_{\partial_r}\nabla_{\partial_\theta}\partial_\theta - \nabla_{\partial_\theta}\nabla_{\partial_r}\partial_\theta$, in components $R^r{}_{\theta r\theta}\partial_r$). Using the explicit formula with $(i, j) = (r, \theta)$ as the antisymmetric pair and lower index $k = \theta$:
> $R^r{}_{\theta r\theta} = \partial_r\Gamma^r_{\theta\theta} - \partial_\theta\Gamma^r_{r\theta} + \Gamma^r_{rm}\Gamma^m_{\theta\theta} - \Gamma^r_{\theta m}\Gamma^m_{r\theta}$.
>
> $\partial_r\Gamma^r_{\theta\theta} = \partial_r(-r) = -1$.
> $\partial_\theta\Gamma^r_{r\theta} = 0$ since $\Gamma^r_{r\theta} = 0$.
> $\Gamma^r_{rm}\Gamma^m_{\theta\theta}$: $\Gamma^r_{rr} = 0, \Gamma^r_{r\theta} = 0$, so this entire term is zero.
> $\Gamma^r_{\theta m}\Gamma^m_{r\theta}$: $\Gamma^r_{\theta r} = 0, \Gamma^r_{\theta\theta} = -r$; $\Gamma^r_{r\theta} = 0, \Gamma^\theta_{r\theta} = 1/r$. So $\Gamma^r_{\theta r}\Gamma^r_{r\theta} = 0$ and $\Gamma^r_{\theta\theta}\Gamma^\theta_{r\theta} = (-r)(1/r) = -1$. Sum: $-1$.
> Total: $-1 - 0 + 0 - (-1) = 0$. ✓
>
> Similarly all other components of $R$ vanish (by the various symmetries of the Riemann tensor and the structure of the polar Christoffels). The connection is flat.

**Step 3: The gauge transformation viewpoint.**

In Cartesian coordinates $(x, y)$, the same Euclidean metric is $g = dx^2 + dy^2$ with all Christoffel symbols zero — the connection is trivially flat. The polar Christoffels $\Gamma^r_{\theta\theta} = -r, \Gamma^\theta_{r\theta} = 1/r$ are entirely the **$g^{-1}dg$ correction** of the [[Thm - Gauge Transformation Law for Connection 1-Forms|gauge-transformation law]] $\Gamma' = g^{-1}\Gamma g + g^{-1}dg$ for the change of frame $g$ from Cartesian to polar (where $\Gamma = 0$ in the Cartesian frame).

The change-of-frame matrix from Cartesian basis $(\partial_x, \partial_y)$ to polar basis $(\partial_r, \partial_\theta)$ is the inverse Jacobian: $\partial_r = \cos\theta\partial_x + \sin\theta\partial_y$, $\partial_\theta = -r\sin\theta\partial_x + r\cos\theta\partial_y$, so the change-of-frame matrix is $g = \begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix}$ (in components $g^a{}_i$ with $a \in \{x, y\}$ and $i \in \{r, \theta\}$). Computing $g^{-1}dg$ gives precisely the polar Christoffel symbols organised as connection 1-forms. The cancellation in $R^l{}_{ijk}$ above is then the algebraic confirmation that "$g^{-1}dg$ has zero curvature" — which is automatic since the gauge-equivalent flat connection (Cartesian) has zero curvature.

> [!note]- Derivation
> Detailed calculation: the change-of-frame matrix is $P = \begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix}$, with inverse $P^{-1} = \begin{pmatrix}\cos\theta & \sin\theta \\ -\sin\theta/r & \cos\theta/r\end{pmatrix}$. Differentiating, $dP = \begin{pmatrix}-\sin\theta\,d\theta & -\sin\theta\,dr - r\cos\theta\,d\theta \\ \cos\theta\,d\theta & \cos\theta\,dr - r\sin\theta\,d\theta\end{pmatrix}$. Computing $P^{-1}dP$ is a matrix product yielding the polar connection 1-forms; verification that this matches the Christoffel-based values is left as a check.

> [!note]- Complete formal solution
> **Christoffel symbols.** Polar Christoffels of the Euclidean metric $g = dr^2 + r^2 d\theta^2$:
> $$
> \Gamma^r_{\theta\theta} = -r, \qquad \Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \tfrac{1}{r}, \qquad \text{all others} = 0.
> $$
> Computed from the Christoffel formula using only $\partial_r g_{\theta\theta} = 2r$ as the nontrivial metric derivative.
>
> **Flatness.** $R^r{}_{\theta r\theta} = \partial_r\Gamma^r_{\theta\theta} - \partial_\theta\Gamma^r_{r\theta} + \Gamma^r_{rm}\Gamma^m_{\theta\theta} - \Gamma^r_{\theta m}\Gamma^m_{r\theta} = -1 - 0 + 0 + 1 = 0$. All other components vanish by symmetries.
>
> **Gauge interpretation.** The polar Christoffels are the "$g^{-1}dg$" part of the gauge-transformation law from the trivially-flat Cartesian connection. The connection is intrinsically the flat connection; the polar coordinate representation is non-zero only because the polar coordinate frame is itself rotating with respect to parallel transport. $\blacksquare$

---

# Key Takeaways

**$\Gamma$ is not a tensor — and polar coordinates on flat $\mathbb{R}^2$ is the canonical demonstration.** A tensor that vanishes in one coordinate system vanishes in all coordinate systems. The Christoffel symbols of the Euclidean metric are all zero in Cartesian coordinates and equal to $-r$ and $1/r$ in polar coordinates — so $\Gamma$ cannot be a tensor. The "extra" terms $\Gamma^r_{\theta\theta} = -r$ and $\Gamma^\theta_{r\theta} = 1/r$ are not measuring any geometric property of the manifold; they are the "$g^{-1}dg$" correction needed to express the *intrinsically flat* connection in a *coordinate frame that itself rotates*. This is the most important conceptual lesson of the chapter on connections: the Christoffel symbols are gauge-dependent, and "flat" is a property of the connection (the curvature tensor), not of the Christoffel symbols.

**The cancellation in the Riemann tensor is the algebraic content of "the polar Christoffels are gauge artefacts".** When computing $R^r{}_{\theta r\theta}$, the two $\partial\Gamma$ terms and the two $\Gamma\Gamma$ terms cancel pairwise: $-1 + 1 = 0$. This is not accidental; it is the algebraic confirmation that the polar Christoffels are obtained from a *gauge transformation* of the trivial connection. The relation $\Omega' = g^{-1}\Omega g$ for the curvature, combined with $\Omega = 0$ in the Cartesian frame, forces $\Omega' = 0$ in the polar frame too — and this is exactly what the cancellation realises in components. The reusable insight: when the curvature is zero in one frame, it must be zero in every frame, and the Christoffel-formula computation provides a direct verification of this gauge invariance.

**The recipe for the polar / spherical / cylindrical Christoffels is universal.** The same computation works for any coordinate system that is "polar-like" — including spherical $(r, \theta, \varphi)$ on $\mathbb{R}^3$, cylindrical $(r, \varphi, z)$ on $\mathbb{R}^3$, hyperspherical on $\mathbb{R}^n$. The structure is: the radial direction is "trivially flat" (Christoffel of mixed radial-angular involves $\partial_r$ of the angular metric), and the angular directions inherit Christoffel symbols from the sphere geometry. For example, on $\mathbb{R}^3$ in spherical coordinates the Christoffel symbols include $\Gamma^r_{\theta\theta} = -r, \Gamma^r_{\varphi\varphi} = -r\sin^2\theta, \Gamma^\theta_{r\theta} = 1/r, \Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta, \Gamma^\varphi_{r\varphi} = 1/r, \Gamma^\varphi_{\theta\varphi} = \cot\theta$ — a direct generalisation of the polar case combined with the round-sphere case. Once the recipe is internalised, computing Christoffel symbols of polar-type coordinates is a 5-minute exercise.

**Cartesian coordinates and the geometric meaning of "trivial connection".** In Cartesian coordinates on $\mathbb{R}^n$, the Levi-Civita connection has all Christoffel symbols zero. The connection is the **flat connection**: $\nabla_X Y$ is the componentwise directional derivative $X^i\partial_i Y^j$, with no Christoffel correction. Parallel transport along any curve preserves all components — vectors are "moved without changing their components". This is the prototype of a flat connection, and the entire field of "computations using polar/spherical/cylindrical coordinates" is the application of the gauge-transformation law to express this trivial connection in non-trivial coordinate systems. The conceptual takeaway: every nontrivial-looking computation in non-Cartesian coordinates on $\mathbb{R}^n$ is a re-expression of the trivial Cartesian connection, and the answer is "intrinsically" the same.
