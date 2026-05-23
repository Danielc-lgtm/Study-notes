---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Induced Metric on a Submanifold"
  - "Def - Embedded Submanifold"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Problem Statement

Consider the unit sphere $S^2 \subseteq \mathbb{R}^3$, parametrised in spherical coordinates by
$$
X(\theta, \varphi) \;=\; (\sin\theta \cos\varphi,\ \sin\theta \sin\varphi,\ \cos\theta), \qquad \theta \in (0, \pi),\ \varphi \in (0, 2\pi).
$$
Compute the induced metric on $S^2$ from the standard Euclidean metric $\bar g = dx^2 + dy^2 + dz^2$ on $\mathbb{R}^3$, and verify it equals the round metric
$$
g = d\theta^2 + \sin^2\theta\, d\varphi^2.
$$

**Recall:**

For a parametrised submanifold $S \subseteq M$ with parametrisation $X : U \subseteq \mathbb{R}^k \to M$ and ambient metric $g_M$ on $M$, the [[Def - Induced Metric on a Submanifold|induced metric]] on $S$ in the parametrisation coordinates has components
$$
(X^* g_M)_{ij}(u) \;=\; g_M\bigl(\partial_i X,\ \partial_j X\bigr)
$$
where $\partial_i X = \partial X / \partial u^i$ is the $i$th coordinate tangent vector. When $M = \mathbb{R}^N$ with the Euclidean metric, this reduces to the Euclidean dot product $\langle \partial_i X, \partial_j X \rangle$.

![[Def - Induced Metric on a Submanifold#The Definition]]

---

# Convergent Strategy

**Problem class.** This is a *compute the induced metric on a parametrised submanifold* problem — the most common task in concrete Riemannian geometry. The [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Problem-Solving Strategy|problem-solving strategy]] of the topic page identifies the routine: given a parametrisation $X : U \to \mathbb{R}^N$ of a submanifold $S$, the induced metric has matrix components $(X^* \bar g)_{ij} = \langle \partial_i X, \partial_j X\rangle$, the Gram matrix of the coordinate tangent vectors in the ambient Euclidean inner product. Every textbook example (sphere, torus, surface of revolution, hyperbolic plane via the upper half-plane) is a direct application of this routine.

**Assumption pattern.** The hypothesis is "the sphere is the parametrised image of an explicit map $X : (0, \pi) \times (0, 2\pi) \to \mathbb{R}^3$, and $\mathbb{R}^3$ carries the Euclidean metric." The parametrisation is smooth and is an immersion on its domain (the differential has rank $2$ for $\theta \in (0, \pi)$). The Euclidean metric on $\mathbb{R}^3$ is the constant $\delta_{ij}$ in Cartesian coordinates. These are the two pieces of data the formula requires.

**Theorem routing.** Apply the [[Def - Induced Metric on a Submanifold|induced-metric formula]] mechanically: compute $\partial_\theta X$ and $\partial_\varphi X$ as vectors in $\mathbb{R}^3$, then compute their pairwise Euclidean inner products. The result is the matrix $g_{ij}$ of the round metric, by direct algebra. The path is: parametrisation $\to$ coordinate tangent vectors $\to$ Gram matrix $\to$ induced metric in coordinates.

**Key decision point.** The non-obvious choice is *which parametrisation* to use. The standard spherical-coordinate parametrisation $(\theta, \varphi)$ covers most of $S^2$ but excludes the poles ($\theta = 0, \pi$) and the date line ($\varphi = 0 = 2\pi$). For computing the induced metric formula in the interior, this is enough — and the resulting formula $d\theta^2 + \sin^2\theta\, d\varphi^2$ extends continuously to the excluded points (the coordinate singularity at the poles is a parametrisation artefact, not a metric singularity). One could alternatively use stereographic coordinates, which give a smooth global chart on $S^2 \setminus \{\text{pole}\}$ but a more complicated formula; the spherical-coordinate computation is the simplest, even though it requires recognising that the answer is globally defined despite the coordinate singularity.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Legal Operations|the topic page's Legal Operations]]:

1. **Pull back an ambient metric along an immersion** (operation 1). The sphere is presented as a parametrised submanifold of $\mathbb{R}^3$, and the induced metric is the pullback of the Euclidean metric along the parametrisation $X$. This is the entire structure of the problem.

2. **Compute $g$ in coordinates by substitution** (operation 2). The Gram-matrix computation $g_{ij} = \langle \partial_i X, \partial_j X \rangle$ is the substitution of the parametrisation into the ambient metric, expanded out to read off coefficients.

8. **Restrict a metric to a submanifold** (operation 8). The induced metric on $S^2$ is the restriction of the Euclidean structure to tangent vectors of $S^2$, with the parametrisation providing the explicit local coordinates.

---

# Hints

> [!note]- Hint 1
> Write $X(\theta, \varphi)$ as three Cartesian-coordinate functions $(X^1, X^2, X^3)$ and compute $\partial_\theta X = (\partial_\theta X^1, \partial_\theta X^2, \partial_\theta X^3)$ and $\partial_\varphi X$ similarly. These are the coordinate tangent vectors to $S^2$ at the point $X(\theta, \varphi)$.

> [!note]- Hint 2
> The induced metric matrix has components $g_{ij} = \langle \partial_i X, \partial_j X\rangle$ where the inner product is the Euclidean dot product in $\mathbb{R}^3$. Compute the three numbers $g_{\theta\theta}$, $g_{\theta\varphi} = g_{\varphi\theta}$, $g_{\varphi\varphi}$ and check that they give the expected $d\theta^2 + \sin^2\theta\, d\varphi^2$.

> [!note]- Hint 3
> Trigonometric identities are essential: $\cos^2 + \sin^2 = 1$. The off-diagonal term $g_{\theta\varphi}$ should be exactly zero, by computation of the dot product; the diagonal entries should be $1$ and $\sin^2\theta$. If a calculation gives something else, check signs.

---

# Solution

The proof breaks into three steps. Step 1 computes the coordinate tangent vectors $\partial_\theta X$ and $\partial_\varphi X$ as vectors in $\mathbb{R}^3$. Step 2 computes the Gram matrix entries using the Euclidean dot product. Step 3 identifies the result as $d\theta^2 + \sin^2\theta\, d\varphi^2$. The non-obvious move is in Step 2, where two trigonometric identities ($\cos^2 + \sin^2 = 1$ and the orthogonality of $\partial_\theta X$ and $\partial_\varphi X$) collapse the algebra to a clean answer.

**Step 1: Compute the coordinate tangent vectors $\partial_\theta X$ and $\partial_\varphi X$.**

In Cartesian coordinates $X = (X^1, X^2, X^3)$:
$$
\partial_\theta X = (\cos\theta\cos\varphi,\ \cos\theta\sin\varphi,\ -\sin\theta),
$$
$$
\partial_\varphi X = (-\sin\theta\sin\varphi,\ \sin\theta\cos\varphi,\ 0).
$$

> [!note]- Derivation
> Recall $X(\theta, \varphi) = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$.
>
> For $\partial_\theta X$:
> - $\partial_\theta X^1 = \partial_\theta(\sin\theta\cos\varphi) = \cos\theta\cos\varphi$,
> - $\partial_\theta X^2 = \partial_\theta(\sin\theta\sin\varphi) = \cos\theta\sin\varphi$,
> - $\partial_\theta X^3 = \partial_\theta(\cos\theta) = -\sin\theta$.
>
> So $\partial_\theta X = (\cos\theta\cos\varphi, \cos\theta\sin\varphi, -\sin\theta)$.
>
> For $\partial_\varphi X$:
> - $\partial_\varphi X^1 = \partial_\varphi(\sin\theta\cos\varphi) = -\sin\theta\sin\varphi$,
> - $\partial_\varphi X^2 = \partial_\varphi(\sin\theta\sin\varphi) = \sin\theta\cos\varphi$,
> - $\partial_\varphi X^3 = \partial_\varphi(\cos\theta) = 0$.
>
> So $\partial_\varphi X = (-\sin\theta\sin\varphi, \sin\theta\cos\varphi, 0)$.

**Step 2: Compute the Gram matrix entries using the Euclidean dot product.**

$$
g_{\theta\theta} = \langle \partial_\theta X, \partial_\theta X\rangle = 1,
$$
$$
g_{\theta\varphi} = g_{\varphi\theta} = \langle \partial_\theta X, \partial_\varphi X\rangle = 0,
$$
$$
g_{\varphi\varphi} = \langle \partial_\varphi X, \partial_\varphi X\rangle = \sin^2\theta.
$$

> [!note]- Derivation
> **$g_{\theta\theta}$:** $\langle \partial_\theta X, \partial_\theta X\rangle = (\cos\theta\cos\varphi)^2 + (\cos\theta\sin\varphi)^2 + (-\sin\theta)^2 = \cos^2\theta(\cos^2\varphi + \sin^2\varphi) + \sin^2\theta = \cos^2\theta + \sin^2\theta = 1$ (using $\cos^2 + \sin^2 = 1$).
>
> **$g_{\theta\varphi}$:** $\langle \partial_\theta X, \partial_\varphi X\rangle = (\cos\theta\cos\varphi)(-\sin\theta\sin\varphi) + (\cos\theta\sin\varphi)(\sin\theta\cos\varphi) + (-\sin\theta)(0) = -\sin\theta\cos\theta\sin\varphi\cos\varphi + \sin\theta\cos\theta\sin\varphi\cos\varphi = 0$. The two cross terms cancel exactly.
>
> **$g_{\varphi\varphi}$:** $\langle \partial_\varphi X, \partial_\varphi X\rangle = (-\sin\theta\sin\varphi)^2 + (\sin\theta\cos\varphi)^2 + 0^2 = \sin^2\theta(\sin^2\varphi + \cos^2\varphi) = \sin^2\theta$.

**Step 3: Identify the result as $g = d\theta^2 + \sin^2\theta\, d\varphi^2$.**

The induced metric has component matrix $\mathrm{diag}(1, \sin^2\theta)$, so
$$
g = g_{\theta\theta}\, d\theta^2 + 2 g_{\theta\varphi}\, d\theta\, d\varphi + g_{\varphi\varphi}\, d\varphi^2 = d\theta^2 + \sin^2\theta\, d\varphi^2.
$$

This is the **round metric** on $S^2$ in spherical-coordinate parametrisation.

> [!note]- Derivation
> The metric tensor in coordinates is $g = g_{ij}\, du^i \otimes du^j$ (symmetric, so the symmetric product is what matters). Substituting $u^1 = \theta$, $u^2 = \varphi$ and the computed components: $g = 1 \cdot d\theta \otimes d\theta + 0 \cdot d\theta\otimes d\varphi + 0 \cdot d\varphi\otimes d\theta + \sin^2\theta\, d\varphi \otimes d\varphi$. Using the symmetric-product convention $du^i du^j = \tfrac{1}{2}(du^i \otimes du^j + du^j \otimes du^i)$, this is $d\theta^2 + \sin^2\theta\, d\varphi^2$. Done.

> [!note]- Complete formal solution
> Let $S^2 \subseteq \mathbb{R}^3$ be the unit sphere, parametrised by
> $$
> X(\theta, \varphi) = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta), \qquad \theta \in (0, \pi),\ \varphi \in (0, 2\pi).
> $$
>
> The differentials of the components are
> $$
> \partial_\theta X = (\cos\theta\cos\varphi, \cos\theta\sin\varphi, -\sin\theta), \qquad \partial_\varphi X = (-\sin\theta\sin\varphi, \sin\theta\cos\varphi, 0).
> $$
>
> The induced metric is the pullback $X^* \bar g$ of the Euclidean metric, with components
> $$
> (X^* \bar g)_{ij} = \langle \partial_i X, \partial_j X\rangle_{\bar g}.
> $$
>
> Computing:
> $$
> g_{\theta\theta} = \cos^2\theta\cos^2\varphi + \cos^2\theta\sin^2\varphi + \sin^2\theta = \cos^2\theta + \sin^2\theta = 1,
> $$
> $$
> g_{\theta\varphi} = -\sin\theta\cos\theta\sin\varphi\cos\varphi + \sin\theta\cos\theta\sin\varphi\cos\varphi + 0 = 0,
> $$
> $$
> g_{\varphi\varphi} = \sin^2\theta\sin^2\varphi + \sin^2\theta\cos^2\varphi + 0 = \sin^2\theta.
> $$
>
> Hence the induced metric is $g = d\theta^2 + \sin^2\theta\, d\varphi^2$, the round metric on $S^2$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to "use that $S^2$ has constant curvature $1$" to write down the metric directly, but this assumes the answer (the round metric *is* the constant-curvature-$1$ metric — we need to verify this from the embedding). The right approach is to compute from the parametrisation; the curvature characterisation comes *after* one has the metric and can compute its curvature tensor.

---

# Key Takeaways

**The Gram-matrix formula is the entire game for parametrised submanifolds.** Whenever a submanifold $S$ of $\mathbb{R}^N$ is given by an explicit parametrisation $X : U \subseteq \mathbb{R}^k \to \mathbb{R}^N$, the induced metric in those coordinates has matrix $g_{ij} = \langle \partial_i X, \partial_j X \rangle$ — the **Gram matrix** of the coordinate tangent vectors in the ambient Euclidean inner product. This single formula handles the round metric on $S^n$, the flat metric on a torus parametrised in $\mathbb{R}^4$, the metric of a surface of revolution, the metric of a graph $\{(x, f(x)) : x \in U\} \subseteq \mathbb{R}^{n+1}$, and the metric on any explicit submanifold of any ambient Euclidean space. The reusable lesson: when faced with "compute the metric on this surface", do not look for a clever trick — write down the parametrisation, compute the partial derivatives, dot them in pairs, write down the result. The answer falls out.

**Coordinate singularities are parametrisation artifacts, not metric singularities.** The spherical-coordinate parametrisation breaks down at the poles ($\theta = 0$, $\theta = \pi$) — at these points the formula $\partial_\varphi X = (-\sin\theta\sin\varphi, \sin\theta\cos\varphi, 0)$ becomes the zero vector, the parametrisation fails to be an immersion, and the metric matrix becomes singular ($\det g = \sin^2\theta \to 0$). But the round metric *itself* is smooth at the poles — this is a defect of the coordinate chart, not of the geometry. The same trick (a different chart, perhaps stereographic) covers the poles smoothly. The takeaway: when computing metrics in non-trivial coordinate charts, expect coordinate singularities and recognise them as artefacts — switch charts to verify the metric extends smoothly. This is the manifold's way of saying "no single coordinate chart covers the entire manifold without losing some smoothness".

**The induced metric is what makes "intrinsic geometry on submanifolds" rigorous.** The classical theory of "Gaussian curvature of surfaces" (Theorema Egregium and so on) lives in the language of induced metrics: the **first fundamental form** of a parametrised surface is exactly the induced metric, and the **second fundamental form** records how the surface curves within the ambient space. The Theorema Egregium says the *Gaussian curvature* — a quantity computed from the first fundamental form alone — is invariant under isometries: it is "intrinsic to the surface". This is the founding theorem of intrinsic differential geometry, and it relies on having a clean intrinsic notion (the induced metric). The reusable insight: any property of the induced metric is an **intrinsic property** of the submanifold, independent of how it sits in the ambient space. The same submanifold could be isometrically embedded in many ways into different ambient spaces; the *induced metric* and its consequences are the same.

**Cross-link to companion exercises:** See [[Ex - The Hyperbolic Plane as a Riemannian Manifold]] for another classical induced-metric calculation (the upper-half-plane model), and [[Ex - The Metric Tensor in Polar Coordinates]] for the Euclidean metric in non-Cartesian coordinates on $\mathbb{R}^2$.
