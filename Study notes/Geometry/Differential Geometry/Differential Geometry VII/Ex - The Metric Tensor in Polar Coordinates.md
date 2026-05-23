---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Pullback of a Covariant Tensor Field"
  - "Def - Tensor Field on a Manifold"
  - "Thm - Pullback Commutes with Tensor Product"
  - "Thm - Transformation Rule for Tensor Components"
tags: [geometry, differential-geometry, metric, polar-coordinates]
---

# Problem Statement

Consider $\mathbb{R}^2$ with the Euclidean metric

$$g = dx \otimes dx + dy \otimes dy,$$

a smooth, symmetric, positive-definite $(0, 2)$-tensor field. The polar-coordinate parametrization is the smooth map

$$F : \{(r, \theta) : r > 0,\ \theta \in \mathbb{R}\} \to \mathbb{R}^2 \setminus \{0\}, \quad F(r, \theta) = (r\cos\theta, r\sin\theta).$$

**(a)** Compute $F^*g$, the pullback of the Euclidean metric to polar coordinates.

**(b)** Verify the answer: $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$.

**(c)** Read off the components $g_{ij}$ in the polar chart and verify the transformation rule for tensor components against the Cartesian components $g_{ij} = \delta_{ij}$.

**Recall:**

A [[Def - Riemannian Metric|Riemannian metric]] is a smooth, symmetric, positive-definite covariant 2-tensor field; the Euclidean metric on $\mathbb{R}^2$ in Cartesian coordinates has components $g_{ij} = \delta_{ij}$ (the Kronecker delta).

The [[Def - Pullback of a Covariant Tensor Field|pullback]] of a covariant tensor field by a smooth map $F$ is computed by substituting the coordinate functions of $F$ and expanding via the chain rule. The naturality identities are $F^*(A \otimes B) = F^*A \otimes F^*B$ and $F^*(fA) = (f \circ F)\, F^*A$.

The [[Thm - Transformation Rule for Tensor Components|transformation rule]] for a $(0, 2)$-tensor under change of coordinates is

$$\tilde g_{ij} = \frac{\partial x^a}{\partial \tilde x^i}\, \frac{\partial x^b}{\partial \tilde x^j}\, g_{ab}.$$

For a $(0, 2)$-tensor, *two* old-from-new Jacobian factors appear, one per lower index.

---

# Convergent Strategy

**Problem class.** This is the canonical worked example of pullback of a metric tensor, demonstrating how the components of a *single* geometric object (the Euclidean metric) change between coordinate systems via the transformation rule. The pullback formula and the transformation rule give the same answer, providing a useful cross-check.

**Assumption pattern.** Two hypotheses: the Euclidean metric on $\mathbb{R}^2$ is the constant $(0, 2)$-tensor field with components $g_{ij} = \delta_{ij}$ in Cartesian coordinates; the polar-coordinate map $F$ has explicit coordinate functions $F^1 = r\cos\theta, F^2 = r\sin\theta$. From these, the chain rule gives the partial derivatives and the pullback follows.

**Theorem routing.** Apply [[Thm - Pullback Commutes with Tensor Product|naturality of pullback]]: $F^*g = F^*(dx) \otimes F^*(dx) + F^*(dy) \otimes F^*(dy)$. Each $F^*(dy^i)$ is the differential of the corresponding coordinate function: $F^*(dx) = d(r\cos\theta) = \cos\theta\, dr - r\sin\theta\, d\theta$, $F^*(dy) = d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$. Substituting and expanding the tensor products gives $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$ after cancellation.

**Key decision point.** The non-obvious step is to *expect cancellation* of the cross-terms $dr \otimes d\theta$ and $d\theta \otimes dr$. The cross-terms from $F^*(dx) \otimes F^*(dx)$ have coefficient $-r\sin\theta\cos\theta$, and the cross-terms from $F^*(dy) \otimes F^*(dy)$ have coefficient $+r\sin\theta\cos\theta$ — they cancel exactly, leaving only the diagonal terms. This is the geometric fact that polar coordinates are *orthogonal*: $\partial_r$ and $\partial_\theta$ are perpendicular in the Euclidean metric, so $g(\partial_r, \partial_\theta) = 0$ and the metric is diagonal.

---

# Legal Operations Used

From [[Differential Geometry VII — Tensors and Tensor Fields#Legal Operations|the topic page's Legal Operations]]:

1. **Pull back covariant tensor fields** (operation 5). The whole exercise computes $F^*g$.

2. **Take the tensor product of two tensor fields** (operation 1). The metric is a sum of two tensor products $dx \otimes dx + dy \otimes dy$, and pullback commutes with tensor product.

3. **Change coordinates using the transformation rule** (operation 4). Part (c) verifies the transformation rule for $(0, 2)$-tensor components directly.

4. **Compute components in a chart** (operation 3). The final answer reads off the matrix $g_{ij}$ in the polar chart: $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = g_{\theta r} = 0$.

---

# Hints

> [!note]- Hint 1
> Decompose the metric using naturality: $F^*g = F^*(dx) \otimes F^*(dx) + F^*(dy) \otimes F^*(dy)$. Then compute each $F^*(dy^i)$ as the differential of the corresponding coordinate function of $F$.

> [!note]- Hint 2
> Compute $F^*(dx) = d(r\cos\theta) = \cos\theta\, dr - r\sin\theta\, d\theta$ and $F^*(dy) = d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$ using the product/chain rule.

> [!note]- Hint 3
> When you expand $F^*(dx) \otimes F^*(dx)$ and $F^*(dy) \otimes F^*(dy)$, the cross-terms in $dr \otimes d\theta + d\theta \otimes dr$ from the two tensor products have *opposite signs* and cancel. The result is the clean diagonal form $dr \otimes dr + r^2\, d\theta \otimes d\theta$.

---

# Solution

The proof breaks into three steps mirroring the problem. Step 1 computes the pullbacks of the basis 1-forms. Step 2 substitutes and expands, with the key cancellation of cross-terms. Step 3 reads off the components and cross-checks against the transformation rule.

**Step 1: Compute $F^*(dx)$ and $F^*(dy)$.**

By the naturality of pullback for 1-forms, $F^*(dx) = d(x \circ F) = d(r\cos\theta) = \cos\theta\, dr - r\sin\theta\, d\theta$ and $F^*(dy) = d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$.

> [!note]- Derivation
> $F : (r, \theta) \mapsto (r\cos\theta, r\sin\theta)$, so $x \circ F = r\cos\theta$ and $y \circ F = r\sin\theta$. The pullback of $dx$ is the differential of $x \circ F$:
> $$F^*(dx) = d(r\cos\theta) = \frac{\partial}{\partial r}(r\cos\theta)\, dr + \frac{\partial}{\partial\theta}(r\cos\theta)\, d\theta = \cos\theta\, dr - r\sin\theta\, d\theta.$$
> Similarly,
> $$F^*(dy) = d(r\sin\theta) = \frac{\partial}{\partial r}(r\sin\theta)\, dr + \frac{\partial}{\partial\theta}(r\sin\theta)\, d\theta = \sin\theta\, dr + r\cos\theta\, d\theta.$$

**Step 2: Substitute and expand the tensor product.**

Substituting into $F^*g = F^*(dx) \otimes F^*(dx) + F^*(dy) \otimes F^*(dy)$ and expanding, the cross-terms cancel and the result is $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$.

> [!note]- Derivation
> By the naturality of pullback,
> $$F^*g = F^*(dx \otimes dx + dy \otimes dy) = F^*(dx) \otimes F^*(dx) + F^*(dy) \otimes F^*(dy).$$
>
> Compute the first term:
> $$F^*(dx) \otimes F^*(dx) = (\cos\theta\, dr - r\sin\theta\, d\theta) \otimes (\cos\theta\, dr - r\sin\theta\, d\theta).$$
> Expanding by bilinearity:
> $$= \cos^2\theta\, dr \otimes dr - r\sin\theta\cos\theta\, dr \otimes d\theta - r\sin\theta\cos\theta\, d\theta \otimes dr + r^2\sin^2\theta\, d\theta \otimes d\theta.$$
>
> Compute the second term:
> $$F^*(dy) \otimes F^*(dy) = (\sin\theta\, dr + r\cos\theta\, d\theta) \otimes (\sin\theta\, dr + r\cos\theta\, d\theta).$$
> Expanding:
> $$= \sin^2\theta\, dr \otimes dr + r\sin\theta\cos\theta\, dr \otimes d\theta + r\sin\theta\cos\theta\, d\theta \otimes dr + r^2\cos^2\theta\, d\theta \otimes d\theta.$$
>
> Add the two terms. The $dr \otimes dr$ coefficients are $\cos^2\theta + \sin^2\theta = 1$. The $d\theta \otimes d\theta$ coefficients are $r^2\sin^2\theta + r^2\cos^2\theta = r^2$. The cross-terms $dr \otimes d\theta$ and $d\theta \otimes dr$ have coefficients $-r\sin\theta\cos\theta + r\sin\theta\cos\theta = 0$ — they *cancel*. So
> $$F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta.$$

**Step 3: Read off components and verify via transformation rule.**

The components of $F^*g$ in the polar chart are $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = g_{\theta r} = 0$. This agrees with the transformation rule applied to the Cartesian metric.

> [!note]- Derivation
> *Reading off components.* From $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$, the matrix of components in the basis $(dr, d\theta)$ is
> $$(g_{ij}) = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}.$$
> So $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = g_{\theta r} = 0$ — the metric is diagonal in polar coordinates, with the non-trivial scaling $r^2$ on $d\theta \otimes d\theta$.
>
> *Verification via the transformation rule.* The Cartesian components are $g_{ab} = \delta_{ab}$. The transformation rule says
> $$g_{ij}^{\text{polar}} = \frac{\partial x^a}{\partial \tilde x^i}\, \frac{\partial x^b}{\partial \tilde x^j}\, g_{ab}^{\text{Cart}} = \frac{\partial x^a}{\partial \tilde x^i}\, \frac{\partial x^a}{\partial \tilde x^j}$$
> (sum on $a$, since $g_{ab} = \delta_{ab}$ collapses $b$ to $a$).
>
> Compute each component:
> - $g_{rr} = (\partial x/\partial r)^2 + (\partial y/\partial r)^2 = \cos^2\theta + \sin^2\theta = 1$. ✓
> - $g_{\theta\theta} = (\partial x/\partial\theta)^2 + (\partial y/\partial\theta)^2 = (-r\sin\theta)^2 + (r\cos\theta)^2 = r^2\sin^2\theta + r^2\cos^2\theta = r^2$. ✓
> - $g_{r\theta} = (\partial x/\partial r)(\partial x/\partial\theta) + (\partial y/\partial r)(\partial y/\partial\theta) = \cos\theta \cdot (-r\sin\theta) + \sin\theta \cdot r\cos\theta = 0$. ✓
>
> So the transformation rule and the pullback computation agree — both give $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$.

> [!note]- Complete formal solution
> *Setup:* $g = dx \otimes dx + dy \otimes dy$ on $\mathbb{R}^2$; $F(r, \theta) = (r\cos\theta, r\sin\theta)$.
>
> *Step 1.* $F^*(dx) = d(r\cos\theta) = \cos\theta\, dr - r\sin\theta\, d\theta$ and $F^*(dy) = d(r\sin\theta) = \sin\theta\, dr + r\cos\theta\, d\theta$.
>
> *Step 2.* By naturality of pullback,
> $$F^*g = F^*(dx) \otimes F^*(dx) + F^*(dy) \otimes F^*(dy).$$
> Expanding the two tensor products and adding:
> - $dr \otimes dr$ coefficient: $\cos^2\theta + \sin^2\theta = 1$.
> - $d\theta \otimes d\theta$ coefficient: $r^2(\sin^2\theta + \cos^2\theta) = r^2$.
> - Cross-term coefficients: $\pm r\sin\theta\cos\theta$, summing to $0$.
>
> So $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$.
>
> *Step 3.* Components in polar chart: $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = 0$. Cross-check via transformation rule using the Cartesian components $\delta_{ab}$ matches. $\blacksquare$

> [!warning] Illegal but tempting: "the metric is always $\delta_{ij}$"
> A common error is to think that since the metric in Cartesian coordinates has components $\delta_{ij}$, the metric must have $\delta_{ij}$ components in every coordinate system. This is **wrong**. The metric is a *tensor field*; its components depend on the basis used. The Euclidean metric — as a geometric object — is the same in polar and Cartesian coordinates (it gives the same lengths and angles), but its components transform under the change of basis. In polar coordinates, the components are $(1, r^2, 0)$, not $(1, 1, 0)$. The $r^2$ factor on $g_{\theta\theta}$ is what makes the polar arc-length element $ds^2 = dr^2 + r^2 d\theta^2$ correct: it accounts for the fact that the angular distance corresponding to $d\theta$ is $r \cdot d\theta$, not $d\theta$ itself.

---

# Key Takeaways

**The line element $ds^2 = dr^2 + r^2 d\theta^2$ comes from the metric tensor.** Everyone has seen the polar-coordinate arc-length formula $ds^2 = dr^2 + r^2 d\theta^2$, but few realize it is *just* the components of the metric tensor read off from the symmetric tensor product $g = dr \otimes dr + r^2\, d\theta \otimes d\theta$. The $r^2$ on $d\theta^2$ is not an ad hoc correction; it is the component $g_{\theta\theta}$ of the Euclidean metric in the polar chart. The same logic applies to spherical, cylindrical, and any other coordinate system: the line element is the metric's symmetric form in the chosen coordinates.

**Polar coordinates are orthogonal — cross-terms cancel.** The vanishing of the cross-term $g_{r\theta} = 0$ is the algebraic expression of the geometric fact that $\partial_r$ and $\partial_\theta$ are perpendicular. The cancellation of $\pm r\sin\theta\cos\theta$ in the expansion is exactly this: the contributions from $F^*(dx)\otimes F^*(dx)$ and $F^*(dy) \otimes F^*(dy)$ have opposite signs in the cross-terms, and they cancel because the columns of the Jacobian matrix of $F$ are orthogonal. In any orthogonal coordinate system, the metric is diagonal and the cross-terms vanish. This is the "orthogonal" in "orthogonal coordinates".

**Pullback and transformation rule give the same answer.** This exercise demonstrates the equivalence of the two perspectives on coordinate change: pullback by the chart-transition map (the manifold-level operation) and the classical transformation rule for components (the index-gymnastics operation). They give identical results because they are the same operation expressed in different language. When computing tensors in non-Cartesian coordinates, you can choose whichever perspective is more convenient — but the answers must agree.

**The pattern generalizes to any coordinate system.** The polar-coordinate metric is the simplest non-trivial example, but the same recipe applies to spherical coordinates on $\mathbb{R}^3$ (yielding $g = dr^2 + r^2 d\theta^2 + r^2\sin^2\theta\, d\phi^2$), to coordinates on the sphere $S^2$ via stereographic projection, to coordinates on the hyperbolic plane, and to *every* curvilinear coordinate system one encounters in physics or geometry. The recipe — pull back the ambient metric using the coordinate map and expand — is universal. Once mastered, computing the metric in any chart becomes a routine substitute-and-expand exercise rather than a special case.
