---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Musical Isomorphism (Flat and Sharp)"
  - "Def - Riemannian Metric"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Problem Statement

Consider $\mathbb{R}^2 \setminus \{0\}$ with the Euclidean metric in polar coordinates $(r, \theta)$:
$$
g \;=\; dr^2 + r^2\, d\theta^2.
$$

(a) Compute the matrix $g_{ij}$ of the metric and its inverse $g^{ij}$ in the polar coordinate basis $\{\partial_r, \partial_\theta\}$.

(b) For a smooth function $f(r, \theta) = r^2 \cos\theta$, compute the differential $df$ as a covector field and then compute the gradient $\mathrm{grad}_g f = (df)^\sharp$ as a vector field, by raising the index using $g^{ij}$.

(c) Verify that the result agrees with the result of computing the gradient in Cartesian coordinates $(x, y) = (r\cos\theta, r\sin\theta)$ and then converting back to polar.

**Recall:**

![[Def - Musical Isomorphism (Flat and Sharp)#The Definition]]

In coordinates, lowering: $X_i = g_{ij}X^j$. Raising: $\omega^i = g^{ij}\omega_j$. The gradient of $f$ in any coordinates is $\mathrm{grad}_g f = g^{ij}\, \partial_j f\, \partial_i$.

The polar-coordinate vector fields are $\partial_r = \cos\theta\, \partial_x + \sin\theta\, \partial_y$ and $\partial_\theta = -r\sin\theta\, \partial_x + r\cos\theta\, \partial_y$.

---

# Convergent Strategy

**Problem class.** This is a *raise and lower indices in non-Cartesian coordinates* problem — a routine but conceptually decisive computation. The [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Problem-Solving Strategy|problem-solving strategy]] identifies the route: when computing gradient/divergence/Laplacian on a non-Cartesian chart, the inverse metric $g^{ij}$ is essential and is what distinguishes the manifold-intrinsic gradient from the "vector of partial derivatives". The trap (illegal operation 3) is to write the gradient as $(\partial_r f, \partial_\theta f)$ and assume this is correct — it is not, except in Cartesian coordinates where $g^{ij} = \delta^{ij}$.

**Assumption pattern.** The setup is: the Euclidean metric expressed in polar coordinates is $g = dr^2 + r^2 d\theta^2$ — *not* the constant matrix $\delta_{ij}$. The $r^2$ factor on the $\theta$-component captures the fact that "angular distance" at radius $r$ scales with $r$ (an arc of angular width $d\theta$ at radius $r$ has Euclidean length $r\, d\theta$, hence "length-squared" $r^2\, d\theta^2$). This is the entire content of $g_{ij}$ in polar coordinates: the diagonal entries differ from $1$, and so does the inverse.

**Theorem routing.** Apply the formulas mechanically: the matrix $g_{ij} = \mathrm{diag}(1, r^2)$ has inverse $g^{ij} = \mathrm{diag}(1, 1/r^2)$. For $f(r, \theta) = r^2\cos\theta$, compute $df = \partial_r f\, dr + \partial_\theta f\, d\theta = 2r\cos\theta\, dr - r^2\sin\theta\, d\theta$. Raise: $(\mathrm{grad}\, f)^r = g^{rr}\, \partial_r f = 2r\cos\theta$ and $(\mathrm{grad}\, f)^\theta = g^{\theta\theta}\, \partial_\theta f = -(\sin\theta)/r$. So $\mathrm{grad}\, f = 2r\cos\theta\, \partial_r - (\sin\theta / r)\, \partial_\theta$. The path: parametrise the function, compute $df$, raise the index, read off the vector.

**Key decision point.** The non-obvious choice is *where* the $1/r^2$ factor goes. A common error is to write $\mathrm{grad}\, f = \partial_r f\, \partial_r + \partial_\theta f\, \partial_\theta$ — but this is wrong; the second term should be $(1/r^2)\partial_\theta f\, \partial_\theta$. The decision is to consciously apply $g^{ij}$ rather than the identity matrix. The verification in (c) (converting through Cartesian) is the safety check: if your polar gradient does not match the Cartesian one converted back, you have left out the inverse-metric factor.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Legal Operations|the topic page's Legal Operations]]:

4. **Use the musical isomorphism to convert between vectors and covectors** (operation 4). The sharp map $\sharp$ is applied to the covector $df$ to produce the vector field $\mathrm{grad}_g f$. The matrix of $\sharp$ in polar coordinates is the inverse metric $g^{ij}$.

2. **Compute $g$ in coordinates by substitution** (operation 2). The polar-coordinate expression $g = dr^2 + r^2 d\theta^2$ is computed by substituting $(x, y) = (r\cos\theta, r\sin\theta)$ into the Cartesian Euclidean metric $\bar g = dx^2 + dy^2$ and expanding.

5. **Verify positive-definiteness or non-degeneracy in coordinates** (operation 5). The metric matrix $\mathrm{diag}(1, r^2)$ has determinant $r^2 > 0$, confirming non-degeneracy and the existence of the inverse.

---

# Hints

> [!note]- Hint 1
> The matrix of $g$ in polar coordinates is read off from $g = g_{ij}\, du^i\, du^j$. With $u^1 = r$ and $u^2 = \theta$, $g = (1)dr^2 + (r^2)d\theta^2 + 0 \cdot dr\, d\theta$, so $g_{rr} = 1$, $g_{\theta\theta} = r^2$, $g_{r\theta} = 0$. The inverse matrix is the matrix-inverse of $\mathrm{diag}(1, r^2)$, which is $\mathrm{diag}(1, 1/r^2)$.

> [!note]- Hint 2
> The differential of $f$ is the covector field $df = \partial_r f\, dr + \partial_\theta f\, d\theta$. Compute the partial derivatives directly from $f = r^2\cos\theta$ and write down $df$.

> [!note]- Hint 3
> To raise the index of $df$, multiply by $g^{ij}$: $(\mathrm{grad}\, f)^r = g^{rr}\partial_r f + g^{r\theta}\partial_\theta f = 1 \cdot \partial_r f + 0 = \partial_r f$ and $(\mathrm{grad}\, f)^\theta = g^{\theta r}\partial_r f + g^{\theta\theta}\partial_\theta f = 0 + (1/r^2)\partial_\theta f$. The factor of $1/r^2$ on the $\theta$-component is the entire non-Cartesian content.

> [!note]- Hint 4 (for the verification in (c))
> In Cartesian coordinates, $f(r, \theta) = r^2\cos\theta = r^2 \cdot (x/r) = rx = \sqrt{x^2 + y^2}\cdot x$. Compute $\partial_x f$ and $\partial_y f$ directly (using quotient rule or implicit differentiation), then convert $\partial_x f\, \partial_x + \partial_y f\, \partial_y$ back to the polar basis $\{\partial_r, \partial_\theta\}$ using the transition rules.

---

# Solution

The proof breaks into three steps matching the parts of the problem. Step 1 computes the metric matrices. Step 2 computes the gradient in polar coordinates by raising indices. Step 3 verifies via Cartesian coordinates. The non-obvious move is in Step 2: the $1/r^2$ factor on the $\theta$-component is exactly the inverse-metric coefficient $g^{\theta\theta}$, and forgetting it is the canonical error.

**Step 1: Compute $g_{ij}$ and $g^{ij}$.**

In the polar coordinate basis $\{\partial_r, \partial_\theta\}$:
$$
g_{ij} = \begin{pmatrix} g_{rr} & g_{r\theta} \\ g_{\theta r} & g_{\theta\theta} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}, \qquad g^{ij} = \begin{pmatrix} 1 & 0 \\ 0 & 1/r^2 \end{pmatrix}.
$$

> [!note]- Derivation
> The metric $g = dr^2 + r^2 d\theta^2$ has component form $g = g_{ij}\, du^i\, du^j$ with $u^1 = r$, $u^2 = \theta$. Matching coefficients: $g_{rr} = 1$, $g_{\theta\theta} = r^2$, $g_{r\theta} = g_{\theta r} = 0$. So $g_{ij} = \mathrm{diag}(1, r^2)$.
>
> The inverse matrix of $\mathrm{diag}(1, r^2)$ is $\mathrm{diag}(1, 1/r^2)$, so $g^{ij} = \mathrm{diag}(1, 1/r^2)$. (Check: $g^{ij}g_{jk} = \mathrm{diag}(1 \cdot 1, (1/r^2) \cdot r^2) = \mathrm{diag}(1, 1) = \delta^i_k$.)

**Step 2: Compute the differential $df$ and then the gradient.**

For $f(r, \theta) = r^2\cos\theta$:
$$
df = 2r\cos\theta\, dr - r^2\sin\theta\, d\theta,
$$
and raising the index gives
$$
\operatorname{grad}_g f=2r\cos\theta\,\partial_r-\sin\theta\,\partial_\theta.
$$

> [!note]- Derivation
> **Differential.** $\partial_r f = \partial_r(r^2\cos\theta) = 2r\cos\theta$, and $\partial_\theta f = \partial_\theta(r^2\cos\theta) = -r^2\sin\theta$. So
> $$
> df = \partial_r f\, dr + \partial_\theta f\, d\theta = 2r\cos\theta\, dr - r^2\sin\theta\, d\theta.
> $$
>
> **Gradient by raising index.** Since $(df)^i=g^{ij}\partial_jf$ and $(g^{ij})=\operatorname{diag}(1,r^{-2})$,
> $$(df)^r=2r\cos\theta,\qquad (df)^\theta=\frac1{r^2}(-r^2\sin\theta)=-\sin\theta.$$
> Therefore
> $$\operatorname{grad}_g f=(df)^\sharp=2r\cos\theta\,\partial_r-\sin\theta\,\partial_\theta.$$

**Step 3: Verify via Cartesian coordinates.**

In Cartesian coordinates $(x, y) = (r\cos\theta, r\sin\theta)$, $f = r^2\cos\theta = r \cdot (r\cos\theta) = r \cdot x$. Since $r = \sqrt{x^2 + y^2}$, $f(x, y) = x\sqrt{x^2 + y^2}$. The Cartesian gradient is $\mathrm{grad}\, f = \partial_x f\, \partial_x + \partial_y f\, \partial_y$ (since $g^{ij} = \delta^{ij}$ in Cartesian coordinates).

> [!note]- Derivation
> Compute the Cartesian partial derivatives:
> $$
> \partial_x f = \partial_x(x\sqrt{x^2 + y^2}) = \sqrt{x^2 + y^2} + x \cdot \frac{x}{\sqrt{x^2 + y^2}} = \sqrt{x^2 + y^2} + \frac{x^2}{\sqrt{x^2 + y^2}} = \frac{2x^2 + y^2}{\sqrt{x^2 + y^2}}.
> $$
> $$
> \partial_y f = \partial_y(x\sqrt{x^2 + y^2}) = x \cdot \frac{y}{\sqrt{x^2 + y^2}} = \frac{xy}{\sqrt{x^2 + y^2}}.
> $$
>
> In polar coordinates $x = r\cos\theta$, $y = r\sin\theta$, $\sqrt{x^2+y^2} = r$:
> $$
> \partial_x f = \frac{2r^2\cos^2\theta + r^2\sin^2\theta}{r} = r(2\cos^2\theta + \sin^2\theta) = r(\cos^2\theta + 1) = r + r\cos^2\theta.
> $$
>
> Similarly $\partial_y f = \frac{r\cos\theta \cdot r\sin\theta}{r} = r\sin\theta\cos\theta$.
>
> Now convert $\partial_x$ and $\partial_y$ to the polar basis. The chain rule gives:
> $$
> \partial_x = \cos\theta\, \partial_r - \frac{\sin\theta}{r}\, \partial_\theta, \qquad \partial_y = \sin\theta\, \partial_r + \frac{\cos\theta}{r}\, \partial_\theta.
> $$
> (Verify: $\partial_x r = \partial_x \sqrt{x^2+y^2} = x/r = \cos\theta$; $\partial_x \theta = \partial_x \arctan(y/x) = -y/r^2 = -\sin\theta/r$; etc.)
>
> So
> $$
> \mathrm{grad}\, f = \partial_x f\, \partial_x + \partial_y f\, \partial_y = r(\cos^2\theta + 1)\bigl(\cos\theta\, \partial_r - \tfrac{\sin\theta}{r}\partial_\theta\bigr) + r\sin\theta\cos\theta\bigl(\sin\theta\, \partial_r + \tfrac{\cos\theta}{r}\partial_\theta\bigr).
> $$
>
> The $\partial_r$ coefficient: $r(\cos^2\theta + 1)\cos\theta + r\sin^2\theta\cos\theta = r\cos\theta(\cos^2\theta + 1 + \sin^2\theta) = r\cos\theta \cdot 2 = 2r\cos\theta$. ✓
>
> The $\partial_\theta$ coefficient: $-r(\cos^2\theta + 1)\sin\theta / r + r\sin\theta\cos\theta \cdot \cos\theta / r = -(\cos^2\theta + 1)\sin\theta + \sin\theta\cos^2\theta = \sin\theta(-\cos^2\theta - 1 + \cos^2\theta) = -\sin\theta$. ✓
>
> Both agree with the direct polar computation in Step 2.

> [!note]- Complete formal solution
> **Part (a).** From $g = dr^2 + r^2 d\theta^2$:
> $$
> g_{ij} = \mathrm{diag}(1, r^2), \qquad g^{ij} = \mathrm{diag}(1, 1/r^2).
> $$
>
> **Part (b).** For $f = r^2\cos\theta$:
> $$
> df = 2r\cos\theta\, dr - r^2\sin\theta\, d\theta.
> $$
> The gradient is $\mathrm{grad}\, f = (df)^\sharp = g^{ij}\partial_j f\, \partial_i$:
> $$
> (\mathrm{grad}\, f)^r = g^{rr}\partial_r f = 1 \cdot 2r\cos\theta = 2r\cos\theta,
> $$
> $$
> (\mathrm{grad}\, f)^\theta = g^{\theta\theta}\partial_\theta f = \frac{1}{r^2}(-r^2\sin\theta) = -\sin\theta.
> $$
> So
> $$
> \mathrm{grad}\, f = 2r\cos\theta\, \partial_r - \sin\theta\, \partial_\theta.
> $$
>
> **Part (c).** In Cartesian coordinates, $f(x, y) = x\sqrt{x^2 + y^2}$, with partial derivatives
> $$
> \partial_x f = \frac{2x^2 + y^2}{\sqrt{x^2+y^2}}, \qquad \partial_y f = \frac{xy}{\sqrt{x^2+y^2}}.
> $$
> The Cartesian gradient $\partial_x f\, \partial_x + \partial_y f\, \partial_y$, converted to the polar basis using $\partial_x = \cos\theta\, \partial_r - (\sin\theta/r)\partial_\theta$ and $\partial_y = \sin\theta\, \partial_r + (\cos\theta/r)\partial_\theta$, gives:
> - $\partial_r$ coefficient: $\partial_x f\, \cos\theta + \partial_y f\, \sin\theta = r(\cos^2\theta + 1)\cos\theta + r\sin\theta\cos\theta\sin\theta = 2r\cos\theta$. ✓
> - $\partial_\theta$ coefficient: $-\partial_x f\, \sin\theta/r + \partial_y f\, \cos\theta/r = -\sin\theta$. ✓
>
> Both methods give the same gradient. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might write the gradient as $\partial_r f\, \partial_r + \partial_\theta f\, \partial_\theta = 2r\cos\theta\, \partial_r - r^2\sin\theta\, \partial_\theta$ — forgetting the factor of $g^{\theta\theta} = 1/r^2$ in the $\partial_\theta$ component. This wrong answer would give a $\theta$-component proportional to $r^2$, not constant in $r$ as the correct answer is. The error comes from treating the coordinate basis $\{\partial_r, \partial_\theta\}$ as if it were *orthonormal*, which it is not in polar coordinates: $|\partial_\theta|_g = r$, not $1$. The orthonormal frame is $\{\partial_r, (1/r)\partial_\theta\}$. To avoid the error: always insert $g^{ij}$ explicitly when computing gradient in non-Cartesian coordinates.

---

# Key Takeaways

**The inverse metric $g^{ij}$ is exactly what distinguishes "gradient" from "partial derivatives".** In Cartesian coordinates on Euclidean space, the matrix of the metric is the identity, and the gradient of $f$ equals the vector of partial derivatives — this is what gets taught in elementary calculus, and it is correct there. In *any other* coordinate system or any other Riemannian manifold, the gradient is $g^{ij}\partial_j f\, \partial_i$, and the inverse metric factor $g^{ij}$ matters. The reusable lesson: whenever you write the gradient in non-Cartesian coordinates (polar, spherical, cylindrical, or on a curved manifold), consciously insert the inverse metric. The same applies to other vector-calculus operators: the **divergence** $\mathrm{div}\, X = (1/\sqrt{\det g})\partial_i(\sqrt{\det g}\, X^i)$ involves the metric determinant; the **Laplacian** $\Delta_g f = (1/\sqrt{\det g})\partial_i(\sqrt{\det g}\, g^{ij}\partial_j f)$ involves both the inverse metric and the determinant. Forgetting these factors is the canonical error in physics calculations on curved manifolds.

**Coordinate-basis vectors are not in general orthonormal.** A confusing aspect of differential geometry, especially when one comes from elementary linear algebra, is that the basis $\{\partial_1, \ldots, \partial_n\}$ of $T_pM$ in a coordinate chart is *not* orthonormal in general. In polar coordinates, $|\partial_r|_g = 1$ but $|\partial_\theta|_g = r$. The corresponding **orthonormal frame** is $\{\partial_r, (1/r)\partial_\theta\}$ — the "unit angular vector" requires a factor of $1/r$. When computing in physics (where the orthonormal-frame components are often the "physical" components), one must distinguish coordinate components from frame components. The reusable triplet to remember: **coordinate basis** is $\{\partial_i\}$, **orthonormal frame** is $\{e_i\}$ with $g(e_i, e_j) = \delta_{ij}$, and the conversion between them involves the metric matrix. The "components of a vector" depend on which basis you use.

**The Cartesian verification is a powerful sanity check.** Whenever you compute something in non-Cartesian coordinates and worry you may have made an index-raising error, convert to Cartesian (where the metric is trivial) and back. If the two computations agree, you almost certainly have the right answer. This is a manifestation of the general principle that *manifold-intrinsic quantities are chart-independent*: the gradient of $f$ is a vector field, the same vector field in every chart, even though its component formula changes. The Cartesian–polar verification is the most useful instance of this in two-dimensional problems.

**Cross-link to companion exercises:** This exercise is the index-gymnastics calibration for the chapter. The same technique generalises to spherical coordinates (where one computes the Laplace–Beltrami operator on $S^2$ and recovers the familiar angular Laplacian formula), to higher-rank tensors, and to general semi-Riemannian manifolds. See [[Def - Musical Isomorphism (Flat and Sharp)]] for the conceptual content, and [[Ex - The Round Metric on the Sphere via Restriction]] for a companion induced-metric computation that produces the metric matrix in spherical coordinates needed for further index gymnastics.
