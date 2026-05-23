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

Compute the Christoffel symbols of the Levi-Civita connection of the round metric
$$
g = d\theta^2 + \sin^2\theta\,d\varphi^2
$$
on $S^2$ in spherical coordinates $(\theta, \varphi)$ with $\theta \in (0, \pi)$ and $\varphi \in (0, 2\pi)$. Verify that the great-circle equation $\theta = \pi/2$ (the equator) and $\varphi(t) = \omega t$ (constant angular velocity) is a geodesic by checking it satisfies the geodesic equation $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$.

**Recall:**

The Christoffel formula for the Levi-Civita connection of a Riemannian metric $g$ in local coordinates is

![[Def - Christoffel Symbols#The Definition]]

The geodesic equation in coordinates is $\ddot\gamma^k + \Gamma^k_{ij}\,\dot\gamma^i\,\dot\gamma^j = 0$, the second-order ODE characterising curves whose velocity is parallel-transported along themselves: $\nabla_{\dot\gamma}\dot\gamma = 0$.

The round metric on $S^2$ in spherical coordinates is $g = d\theta^2 + \sin^2\theta\,d\varphi^2$, with components $g_{\theta\theta} = 1, g_{\varphi\varphi} = \sin^2\theta, g_{\theta\varphi} = 0$.

---

# Convergent Strategy

**Problem class:** This is a direct application of the [[Def - Christoffel Symbols|Christoffel formula]] to a concrete diagonal metric — the routine "compute the Levi-Civita connection from given metric components". The metric is diagonal in spherical coordinates, which substantially simplifies the computation. The subsequent verification of the geodesic equation is a routine substitution.

**Assumption pattern:** A specific 2-dimensional Riemannian manifold with metric given explicitly in coordinates is provided. The diagonal structure $g_{\theta\varphi} = 0$ means many terms in the Christoffel formula will vanish; the only non-constant component is $g_{\varphi\varphi} = \sin^2\theta$, so the only nontrivial derivatives are $\partial_\theta g_{\varphi\varphi} = 2\sin\theta\cos\theta$.

**Theorem routing:** Apply the [[Def - Christoffel Symbols|Christoffel formula]] $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ — derived from the [[Thm - Koszul Formula|Koszul formula]] specialised to coordinate frames — using the inverse metric $g^{\theta\theta} = 1, g^{\varphi\varphi} = 1/\sin^2\theta, g^{\theta\varphi} = 0$. Compute the few nonzero entries, then substitute into the geodesic equation.

**Key decision point:** The non-obvious move is *which* of the $n^3 = 8$ Christoffel symbols are zero. The strategy is to organise the calculation by upper index: for $\Gamma^\theta_{ij}$ we only need the $\theta$ row of $g^{kl}$ (so $g^{\theta\theta} = 1$); for $\Gamma^\varphi_{ij}$ we only need the $\varphi$ row ($g^{\varphi\varphi} = 1/\sin^2\theta$). Then iterate over $(i, j)$ and use the diagonal structure of $g$ to eliminate most terms.

---

# Legal Operations Used

1. **Operation 1 from the topic page (Compute Christoffel symbols from the metric).** Apply the Christoffel formula directly. The diagonal structure of $g$ kills most terms; the only nonzero derivative is $\partial_\theta(\sin^2\theta) = 2\sin\theta\cos\theta$, and it contributes only to terms with both $i = \varphi$ and $j = \varphi$ (or permutations involving these).

---

# Hints

> [!note]- Hint 1
> The metric is diagonal: $g_{\theta\theta} = 1, g_{\varphi\varphi} = \sin^2\theta$, others zero. The inverse is also diagonal: $g^{\theta\theta} = 1, g^{\varphi\varphi} = 1/\sin^2\theta$.

> [!note]- Hint 2
> The only metric component with a nonzero derivative is $g_{\varphi\varphi}$, and its only nonzero derivative is $\partial_\theta g_{\varphi\varphi} = 2\sin\theta\cos\theta$. All others vanish.

> [!note]- Hint 3
> For $\Gamma^\theta_{ij}$: only the $g^{\theta\theta} = 1$ component contributes, so $\Gamma^\theta_{ij} = \tfrac{1}{2}(\partial_i g_{j\theta} + \partial_j g_{i\theta} - \partial_\theta g_{ij})$. The only nonzero case is when $i = j = \varphi$, giving $\Gamma^\theta_{\varphi\varphi} = -\tfrac{1}{2}\partial_\theta g_{\varphi\varphi} = -\sin\theta\cos\theta$.

> [!note]- Hint 4
> For $\Gamma^\varphi_{ij}$: only $g^{\varphi\varphi} = 1/\sin^2\theta$ contributes. The nonzero cases are $(i, j) = (\theta, \varphi)$ and $(\varphi, \theta)$, giving $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$.

---

# Solution

**Plan paragraph.** The solution has three steps. Step 1 computes the inverse metric components, mechanically. Step 2 applies the Christoffel formula systematically, organising by upper index and using the diagonal structure of $g$ to eliminate vanishing terms. Step 3 substitutes the equatorial great circle into the geodesic equation and verifies it is satisfied. The key economy comes from recognising in Step 1 that only $g_{\varphi\varphi}$ has nontrivial derivatives, so the bulk of the Christoffel-formula terms vanish.

**Step 1: Compute the inverse metric.**

The metric components are $g_{\theta\theta} = 1, g_{\varphi\varphi} = \sin^2\theta, g_{\theta\varphi} = 0$. The inverse is computed by inverting the diagonal matrix: $g^{\theta\theta} = 1, g^{\varphi\varphi} = 1/\sin^2\theta, g^{\theta\varphi} = 0$.

> [!note]- Derivation
> The metric in matrix form is $\begin{pmatrix} 1 & 0 \\ 0 & \sin^2\theta \end{pmatrix}$, which has determinant $\sin^2\theta$. The inverse is $\begin{pmatrix} 1 & 0 \\ 0 & 1/\sin^2\theta \end{pmatrix}$, with components $g^{\theta\theta} = 1, g^{\varphi\varphi} = 1/\sin^2\theta, g^{\theta\varphi} = 0$.

**Step 2: Apply the Christoffel formula.**

The Christoffel formula is $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$.

For $\Gamma^\theta_{ij}$, only $g^{\theta\theta} = 1$ contributes (since $g^{\theta\varphi} = 0$):
$$
\Gamma^\theta_{ij} = \tfrac{1}{2}(\partial_i g_{j\theta} + \partial_j g_{i\theta} - \partial_\theta g_{ij}).
$$
Since $g_{j\theta}$ is nonzero only when $j = \theta$ (and then $g_{\theta\theta} = 1$, constant), the first two terms vanish unless... actually $g_{j\theta} = \delta_{j\theta}$ which is constant, so $\partial_i g_{j\theta} = 0$ identically. The first two terms vanish. So $\Gamma^\theta_{ij} = -\tfrac{1}{2}\partial_\theta g_{ij}$, nonzero only for $(i, j) = (\varphi, \varphi)$:
$$
\Gamma^\theta_{\varphi\varphi} = -\tfrac{1}{2}\partial_\theta(\sin^2\theta) = -\sin\theta\cos\theta.
$$

For $\Gamma^\varphi_{ij}$, only $g^{\varphi\varphi} = 1/\sin^2\theta$ contributes:
$$
\Gamma^\varphi_{ij} = \tfrac{1}{2\sin^2\theta}(\partial_i g_{j\varphi} + \partial_j g_{i\varphi} - \partial_\varphi g_{ij}).
$$
$\partial_\varphi g_{ij} = 0$ (the metric is independent of $\varphi$). $g_{j\varphi}$ is nonzero only when $j = \varphi$, giving $g_{\varphi\varphi} = \sin^2\theta$, with derivative $\partial_\theta(\sin^2\theta) = 2\sin\theta\cos\theta$ (and $\partial_\varphi = 0$). So $\partial_i g_{j\varphi}$ is nonzero only when $j = \varphi$ and $i = \theta$, giving $\partial_\theta g_{\varphi\varphi} = 2\sin\theta\cos\theta$. Similarly $\partial_j g_{i\varphi}$ is nonzero only when $i = \varphi$ and $j = \theta$.

Combining: $\Gamma^\varphi_{\theta\varphi} = \tfrac{1}{2\sin^2\theta}(0 + 2\sin\theta\cos\theta - 0) = \cos\theta/\sin\theta = \cot\theta$. By symmetry $\Gamma^\varphi_{\varphi\theta} = \cot\theta$. All other $\Gamma^\varphi_{ij}$ vanish.

> [!note]- Derivation
> Organise by upper index. For $\Gamma^\theta_{ij}$: $g^{\theta\theta} = 1$, $g^{\theta\varphi} = 0$, so $\Gamma^\theta_{ij} = \tfrac{1}{2}g^{\theta\theta}(\partial_i g_{j\theta} + \partial_j g_{i\theta} - \partial_\theta g_{ij}) = \tfrac{1}{2}(\partial_i g_{j\theta} + \partial_j g_{i\theta} - \partial_\theta g_{ij})$. Since $g_{j\theta} = \delta^j_\theta \cdot 1$ is a constant (either $0$ or $1$ depending on $j$), $\partial_i g_{j\theta} = 0$. So $\Gamma^\theta_{ij} = -\tfrac{1}{2}\partial_\theta g_{ij}$. The only $g_{ij}$ with nontrivial $\theta$-derivative is $g_{\varphi\varphi} = \sin^2\theta$, giving $\Gamma^\theta_{\varphi\varphi} = -\tfrac{1}{2}(2\sin\theta\cos\theta) = -\sin\theta\cos\theta$.
>
> For $\Gamma^\varphi_{ij}$: $g^{\varphi\varphi} = 1/\sin^2\theta$. $\Gamma^\varphi_{ij} = \tfrac{1}{2}\cdot\tfrac{1}{\sin^2\theta}(\partial_i g_{j\varphi} + \partial_j g_{i\varphi} - \partial_\varphi g_{ij})$. $\partial_\varphi$ of anything vanishes (the metric is $\varphi$-independent). For the first two: $g_{j\varphi} = \delta^j_\varphi \cdot \sin^2\theta$, so $\partial_i g_{j\varphi} = \delta^j_\varphi \cdot \delta^i_\theta \cdot 2\sin\theta\cos\theta = \delta^j_\varphi \cdot \delta^i_\theta \cdot 2\sin\theta\cos\theta$. Symmetrically for $\partial_j g_{i\varphi}$. Combining: $\Gamma^\varphi_{ij}$ is nonzero only when $\{i, j\}$ contains both $\theta$ and $\varphi$, giving $\Gamma^\varphi_{\theta\varphi} = \tfrac{1}{2\sin^2\theta}\cdot 2\sin\theta\cos\theta = \cot\theta$ and $\Gamma^\varphi_{\varphi\theta} = \cot\theta$ by symmetry.

**Summary of nonzero Christoffel symbols:**
$$
\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta, \qquad \Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta.
$$
All other Christoffel symbols are zero.

**Step 3: Verify the equator is a geodesic.**

Take $\gamma(t) = (\theta(t), \varphi(t)) = (\pi/2, \omega t)$. Then $\dot\gamma = (0, \omega), \ddot\gamma = (0, 0)$. The geodesic equation $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$ becomes:
- $k = \theta$: $0 + \Gamma^\theta_{\varphi\varphi}(\pi/2)\cdot\omega^2 = 0 + (-\sin(\pi/2)\cos(\pi/2))\omega^2 = 0 \cdot \omega^2 = 0$. ✓
- $k = \varphi$: $0 + 2\Gamma^\varphi_{\theta\varphi}(\pi/2)\cdot 0 \cdot \omega = 0$. ✓

Both components vanish, so the equator at constant angular velocity is indeed a geodesic.

> [!note]- Derivation
> Plug $\gamma(t) = (\pi/2, \omega t)$ into the geodesic equation. The $\theta$-component: $\ddot\theta + \Gamma^\theta_{ij}\dot\gamma^i\dot\gamma^j = 0 + \Gamma^\theta_{\varphi\varphi}\cdot \dot\varphi^2 = -\sin\theta\cos\theta \cdot \omega^2$. At $\theta = \pi/2$, $\cos(\pi/2) = 0$, so this vanishes. The $\varphi$-component: $\ddot\varphi + 2\Gamma^\varphi_{\theta\varphi}\dot\theta\dot\varphi = 0 + 2\cot\theta \cdot 0 \cdot \omega = 0$. Both equations satisfied — the equator at constant angular speed is a geodesic. (The factor of 2 in the $\varphi$-component comes from $\Gamma^\varphi_{\theta\varphi}\dot\theta\dot\varphi + \Gamma^\varphi_{\varphi\theta}\dot\varphi\dot\theta = 2\Gamma^\varphi_{\theta\varphi}\dot\theta\dot\varphi$ by symmetry.)

> [!note]- Complete formal solution
> **Christoffel symbols of the round metric on $S^2$.**
>
> Given $g = d\theta^2 + \sin^2\theta\,d\varphi^2$, compute the inverse: $g^{\theta\theta} = 1, g^{\varphi\varphi} = 1/\sin^2\theta, g^{\theta\varphi} = 0$.
>
> Apply the Christoffel formula $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. The diagonal structure of $g$ means only the $k = l$ contributions matter; the only nonzero derivative is $\partial_\theta(\sin^2\theta) = 2\sin\theta\cos\theta$.
>
> Direct computation:
> $$
> \Gamma^\theta_{\varphi\varphi} = -\tfrac{1}{2}\partial_\theta(\sin^2\theta) = -\sin\theta\cos\theta,
> $$
> $$
> \Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \tfrac{1}{2\sin^2\theta}\partial_\theta(\sin^2\theta) = \cot\theta.
> $$
> All other Christoffel symbols vanish.
>
> **Geodesic equation for the equator.** For $\gamma(t) = (\pi/2, \omega t)$: $\dot\theta = 0, \dot\varphi = \omega, \ddot\theta = \ddot\varphi = 0$. Plugging into $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$:
>
> $\theta$-component: $0 + \Gamma^\theta_{\varphi\varphi}\dot\varphi^2 = -\sin(\pi/2)\cos(\pi/2)\cdot\omega^2 = 0$ (since $\cos(\pi/2) = 0$). ✓
>
> $\varphi$-component: $0 + 2\Gamma^\varphi_{\theta\varphi}\dot\theta\dot\varphi = 2\cot(\pi/2)\cdot 0\cdot\omega = 0$. ✓
>
> Both vanish; the equator with constant angular velocity is a geodesic. $\blacksquare$

---

# Key Takeaways

**Diagonal-metric computation is mostly bookkeeping.** When the metric is diagonal — $g_{ij} = 0$ for $i \neq j$ — most of the Christoffel symbols are forced to be zero by index-matching, and the computation collapses to a few nonzero terms involving only the diagonal entries and their derivatives. The right organisational principle is "go through the upper index $k$ one at a time, restrict to the diagonal of $g^{kl}$, and identify which terms of the symmetrised partial-derivative expression are nonzero". This pattern recurs for every diagonal metric: warped products, FRW cosmology, Schwarzschild, conformally flat metrics. Once one internalises the bookkeeping, computing the Christoffel symbols of a diagonal metric is a 5-minute exercise.

**Equatorial great circles are geodesics by symmetry — and the calculation confirms it.** On any rotationally symmetric metric (which the round sphere is, in spherical coordinates), the equatorial circle should be a geodesic because of the symmetry: there is no preferred "north" or "south" direction at the equator, so the geodesic with initial velocity along $\partial_\varphi$ stays at the equator forever. The Christoffel-symbol calculation confirms this: the term $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ vanishes at the equator because $\cos(\pi/2) = 0$. This "vanishing of a Christoffel symbol at a symmetric configuration" is the geometric content of "Killing field along the geodesic" — there is a $\partial_\varphi$ Killing field, and its conserved quantity $g(\dot\gamma, \partial_\varphi) = \sin^2\theta\,\dot\varphi$ is constant along any geodesic (here equal to $\omega$ on the equator).

**The Christoffel symbols are not tensors — this calculation is intrinsic only after taking the geodesic equation.** The Christoffel symbols $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta, \Gamma^\varphi_{\theta\varphi} = \cot\theta$ are specific to spherical coordinates. In a different coordinate system (e.g., stereographic from the north pole), they would have entirely different values. What is *intrinsic* — coordinate-independent — is the *connection* $\nabla$ they represent and the geodesic structure that follows. The verification "the equator is a geodesic" is intrinsic, but the form of the verification (which Christoffel symbols are nonzero, where the cancellation happens) depends on the coordinates. The reusable insight: when comparing computations across coordinate systems, focus on intrinsic outcomes (geodesics, curvature scalars, holonomy), not on the Christoffel-symbol values themselves.

**The same computation generalises to any rotationally symmetric metric.** For a general warped-product metric of the form $g = dr^2 + f(r)^2\,d\Omega^2$ on $\mathbb{R}^+ \times S^{n-1}$ (where $d\Omega^2$ is the round metric on $S^{n-1}$), the Christoffel symbols mixing $r$ and the sphere directions are $\Gamma^r_{\text{sphere}} = -f f'$ and $\Gamma^{\text{sphere}}_{r,\text{sphere}} = f'/f$. The same pattern: only the warping function $f$ and its derivative appear. Concrete special cases: $f(r) = r$ gives flat $\mathbb{R}^n$ in polar coordinates; $f(r) = \sin r$ gives the round $S^n$; $f(r) = \sinh r$ gives hyperbolic $\mathbb{H}^n$. Each follows the same recipe and gives the same structure of Christoffel symbols. This is one of the most reusable patterns in Riemannian geometry — see also [[Ex - Christoffel Symbols of the Hyperbolic Plane]] for the hyperbolic case in different coordinates.
