---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Norm and Distance"
tags: [algebra, linear-algebra, applied, geometry]
---

# Notation

Throughout, $a, b$ are nonzero $n$-vectors in $\mathbb R^n$. The Euclidean norm is $\|x\| = \sqrt{x^T x}$. The angle is written $\angle(a, b)$ and lies in $[0, \pi]$ when expressed in radians, or in $[0^\circ, 180^\circ]$ when in degrees. The default unit is radians.

---

# Axiom Motivation

The desideratum is to generalise the school-geometry notion of "the angle between two arrows" to $\mathbb R^n$ for arbitrary $n$. In two dimensions, two unit vectors $u, v$ satisfy $u^T v = \cos\theta$, where $\theta$ is the angle between them. This is the **law of cosines** specialised to unit-vector edges, and it can be verified by direct computation: if $u = (\cos\alpha, \sin\alpha)$ and $v = (\cos\beta, \sin\beta)$, then $u^T v = \cos\alpha\cos\beta + \sin\alpha\sin\beta = \cos(\alpha - \beta) = \cos\theta$.

The proposed generalisation to $\mathbb R^n$ is to *define* the angle by $\cos\theta = a^T b/(\|a\|\|b\|)$, taking $\theta = \arccos$ of that. This is well-posed exactly because of the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]], which guarantees that $|a^T b|/(\|a\|\|b\|) \leq 1$, so the arccos argument lies in $[-1, 1]$ and the angle in $[0, \pi]$ is unambiguous. Without Cauchy–Schwarz, the definition would not make sense — the arccos would attempt to take an out-of-range argument and fail.

The first desideratum any sensible "angle in $n$ dimensions" must satisfy is that it **reduces to the school-geometry angle in $n = 2$ and $n = 3$**. The formula above does, as the computation in two dimensions just above shows; the three-dimensional case is identical, since the angle between two vectors in $\mathbb R^3$ depends only on their two-dimensional projection onto the plane they span. So the proposed definition extends the familiar geometric angle, and any extension that does this and is "natural" must agree with it on the cases we already understand.

The second desideratum is **symmetry and scale-invariance**: the angle between $a$ and $b$ should equal the angle between $b$ and $a$, and the angle should not depend on the magnitudes of $a$ and $b$, only their directions. The formula $\arccos(a^T b/(\|a\|\|b\|))$ is manifestly symmetric, and scaling $a \to \alpha a$ (with $\alpha > 0$) gives $\arccos(\alpha a^T b/(\alpha\|a\|\|b\|)) = \arccos(a^T b/(\|a\|\|b\|))$ — the same angle. Scaling by a negative scalar flips the direction and changes the angle to its supplement, exactly as in school geometry.

The third desideratum is that the angle should make special configurations algebraically clean. We want orthogonality ($\theta = \pi/2$) to be characterised by $a^T b = 0$, alignment ($\theta = 0$) to be characterised by $a, b$ being positive scalar multiples, and anti-alignment ($\theta = \pi$) by negative scalar multiples. The formula achieves all three: $\cos(\pi/2) = 0$ corresponds to $a^T b = 0$; $\cos(0) = 1$ corresponds to $a^T b = \|a\|\|b\|$, the Cauchy–Schwarz equality case (positive multiples); $\cos(\pi) = -1$ corresponds to $a^T b = -\|a\|\|b\|$ (negative multiples).

What would go wrong with nearby variants? **Suppose we omitted the normalisation by $\|a\|\|b\|$ and used $a^T b$ alone as the "angle metric".** Then the result depends on the magnitudes of $a, b$, and two vectors that are parallel can have arbitrarily different "angles" depending on length. The normalisation strips this dependence. **Suppose we tried to define the angle as the arccos of something other than $a^T b / (\|a\|\|b\|)$ — say, $\arccos(a^T b/(\|a\|^p \|b\|^p))$ for $p \neq 1$.** Then unless $p = 1$, the formula either over- or under-corrects for magnitude, and the resulting "angle" no longer reduces to the school-geometry angle in low dimensions. The exponent $p = 1$ is forced.

**Why arccos rather than arcsin or arctan?** The natural quantity here is the cosine: $\cos\theta = (\text{inner product})/(\text{product of norms})$. The cosine is monotonic on $[0, \pi]$ — strictly decreasing from $1$ to $-1$ — so $\arccos$ is a well-defined inverse on this range. The sine, in contrast, is not monotonic on $[0, \pi]$, so $\arcsin(a^T b/(\|a\|\|b\|))$ would have an ambiguity (which the arccos resolves by ranging over the full $[0, \pi]$).

---

# The Definition

For two nonzero vectors $a, b \in \mathbb R^n$, the **angle** between $a$ and $b$ is
$$
\angle(a, b) = \arccos\!\left(\frac{a^T b}{\|a\| \|b\|}\right) \in [0, \pi].
$$
The arccos is well-defined because by the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]], $|a^T b| \leq \|a\|\|b\|$. The angle is sometimes expressed in degrees (with $\angle = 180^\circ$ corresponding to $\pi$ radians).

**Classification of angles.** For nonzero $a, b$:
- $\angle(a, b) = 0$ if and only if $a, b$ are **aligned** (each is a positive scalar multiple of the other): $b = \alpha a$ with $\alpha > 0$. This corresponds to $a^T b = \|a\|\|b\|$.
- $\angle(a, b) = \pi$ if and only if $a, b$ are **anti-aligned**: $b = \alpha a$ with $\alpha < 0$. This corresponds to $a^T b = -\|a\|\|b\|$.
- $\angle(a, b) = \pi/2$ if and only if $a, b$ are **orthogonal**, written $a \perp b$: this corresponds to $a^T b = 0$. By convention the zero vector is orthogonal to every vector.
- $\angle(a, b) < \pi/2$ if and only if $a^T b > 0$, called the **acute** case.
- $\angle(a, b) > \pi/2$ if and only if $a^T b < 0$, called the **obtuse** case.

**Properties.**
1. **Symmetry:** $\angle(a, b) = \angle(b, a)$.
2. **Positive-scaling invariance:** $\angle(\alpha a, \beta b) = \angle(a, b)$ for any scalars $\alpha, \beta > 0$.
3. **Sign-flip:** $\angle(-a, b) = \pi - \angle(a, b)$.
4. **Range:** $0 \leq \angle(a, b) \leq \pi$, with the extremes attained exactly in the aligned and anti-aligned cases.

**Norm-of-sum via angle.** $\|a + b\|^2 = \|a\|^2 + 2 \|a\|\|b\| \cos\angle(a, b) + \|b\|^2$. The Pythagorean theorem is the orthogonal case $\angle = \pi/2$.

---

# Relate to Other Fields / Compression

The angle between vectors in $\mathbb R^n$ is the standard angle from Euclidean geometry, extended to arbitrary dimensions using the inner product. The same construction works in any [[Def - Inner Product Space|inner product space]] over the reals, including infinite-dimensional Hilbert spaces of functions — there, the angle between two functions is $\arccos(\langle f, g\rangle/(\|f\|\|g\|))$, and orthogonality is the abstract notion that drives Fourier analysis.

In statistics and machine learning, the **cosine similarity** $a^T b/(\|a\|\|b\|) = \cos\angle(a, b)$ is the standard measure of similarity between high-dimensional vectors (word embeddings, document term-frequency vectors, user-preference vectors). The angle is preferred to the raw inner product because it strips out magnitude — two documents about the same topic but of different lengths should have similar cosine similarity, regardless of length. The same notion in slightly different language is the **Pearson correlation coefficient**, which is the cosine of the angle between the *de-meaned* versions of two vectors (see [[Def - Standard Deviation and Correlation Coefficient]]).

On the sphere, the angle between two unit vectors *is* the geodesic distance between them — the great-circle distance. This is the origin of the **spherical distance**: for two points $a, b$ on a sphere of radius $R$, the distance along the sphere is $R \angle(a, b)$. The formula is exact and not approximate, and it generalises to spheres in arbitrary dimensions.

**True name:** The angle between two vectors is *the cosine-similarity, with arccos applied* — equivalently, *the great-circle distance between the unit vectors $a/\|a\|, b/\|b\|$ on the unit sphere $S^{n-1}$*.

---

# Examples / Corollaries

**Is an instance — angle in two dimensions.** For $a = (1, 0)$ and $b = (1, 1)$, $a^T b = 1$, $\|a\| = 1$, $\|b\| = \sqrt 2$, so $\angle(a, b) = \arccos(1/\sqrt 2) = \pi/4 = 45^\circ$. This matches the school-geometry picture: $b$ is at $45^\circ$ above the positive $x$-axis.

**Is an instance — orthogonal coordinate axes.** The standard unit vectors $e_i, e_j$ in $\mathbb R^n$ have inner product $e_i^T e_j = \delta_{ij}$ (Kronecker delta), so $\angle(e_i, e_j) = \pi/2$ for $i \neq j$ and $\angle(e_i, e_i) = 0$. The coordinate axes are mutually orthogonal.

**Is an instance — Boyd's three-dimensional example.** For $a = (1, 2, -1)$ and $b = (2, 0, -3)$ in $\mathbb R^3$, $a^T b = 2 + 0 + 3 = 5$, $\|a\| = \sqrt 6$, $\|b\| = \sqrt{13}$. So $\cos\angle(a, b) = 5/\sqrt{78} \approx 0.566$ and $\angle(a, b) \approx 0.969$ radians or $55.5^\circ$.

**Is an instance — spherical distance between cities.** For two points on Earth at latitudes/longitudes $(\theta_1, \lambda_1)$ and $(\theta_2, \lambda_2)$, the surface distance is $R \angle(a, b)$ where $a, b$ are the corresponding $3$-vectors on the sphere of radius $R$. This is the formula commercial airlines use for great-circle distances.

**Is NOT an instance — undefined angle for the zero vector.** The angle $\angle(0, b)$ is not defined (the formula divides by $\|0\| = 0$). By convention, the zero vector is *orthogonal to every vector*, but this is the conventional extension, not the definition; the angle itself is undefined.

**Is NOT an instance — angle in non-Euclidean metrics.** The construction relies on the *Euclidean* inner product. For other norms (the $\ell^1$ norm, the $\ell^\infty$ norm), there is no corresponding "angle" because the norm does not come from an inner product. This is the fundamental reason the Euclidean norm is special: it admits geometry.

**Corollary — Pythagorean theorem for orthogonal vectors.** If $a \perp b$, then $\angle(a, b) = \pi/2$, $\cos\angle = 0$, and the norm-of-sum formula gives $\|a + b\|^2 = \|a\|^2 + \|b\|^2$ — the Pythagorean theorem.

**Corollary — triangle inequality with equality.** The triangle inequality $\|a + b\| \leq \|a\| + \|b\|$ holds with equality if and only if $a$ and $b$ are *aligned*, $\angle(a, b) = 0$. The proof is direct from $\|a + b\|^2 = \|a\|^2 + 2\|a\|\|b\|\cos\angle + \|b\|^2$: equality in the triangle inequality is $\|a + b\|^2 = (\|a\| + \|b\|)^2$, which is $\cos\angle = 1$.

**Corollary — angles between non-negative vectors.** If all entries of $a$ and $b$ are non-negative, then $a^T b \geq 0$, so $\angle(a, b) \in [0, \pi/2]$ — the angle is always acute or right. This is geometrically obvious in $\mathbb R^2$: two arrows in the first quadrant cannot make an obtuse angle. Orthogonality requires the supports to be disjoint: $a^T b = 0$ iff $a_i b_i = 0$ for every $i$.

**Calibration check.** Verify that $\angle(e_1, e_2) = \pi/2$ in $\mathbb R^n$ for any $n$. Verify that $\angle((1, 1), (1, -1)) = \pi/2$, an example of orthogonal vectors that are not coordinate axes. Verify that for two unit vectors $u, v$ with $u^T v = -1$, we have $\angle(u, v) = \pi$ and $v = -u$ (the anti-aligned case).

---

# Unlocked by This

> [!tip] Orthogonal Projections and Least Squares *(from Linear Algebra VI)*
> The angle between a vector and a subspace generalises to **orthogonal projection**: given $v$ and a subspace $W$, the projection $P_W v$ is the unique vector in $W$ closest to $v$, and $v - P_W v$ is orthogonal to $W$. The projection minimises the distance, the angle between $v$ and $P_W v$ is the smallest possible angle between $v$ and any vector in $W$, and this is the geometric heart of least-squares regression.

> [!tip] Spherical Geometry and Hyperbolic Geometry *(from Differential Geometry)*
> The angle on a sphere is the geodesic distance for unit vectors; on a hyperbolic space, the analogous construction uses a Lorentzian inner product, and the geodesic distance becomes $\operatorname{arccosh}$ of an analogous expression. These three geometries — Euclidean, spherical, and hyperbolic — are the three constant-curvature model spaces of differential geometry.

> [!tip] Vector-Space Embeddings and Cosine Similarity in NLP *(from Machine Learning)*
> Word embeddings — high-dimensional vector representations of words — use cosine similarity (the cosine of the angle) to measure word similarity. The classical example is that the embedding of "king" minus "man" plus "woman" is approximately the embedding of "queen", with similarities measured by cosine. The angle-based geometry is what makes such analogies computationally tractable.
