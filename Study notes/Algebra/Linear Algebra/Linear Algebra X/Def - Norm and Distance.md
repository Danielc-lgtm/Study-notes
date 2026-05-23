---
type: definition
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied, geometry]
---

# Notation

Throughout, $x, y, a, b$ are real $n$-vectors and $\alpha, \beta$ are real scalars. The inner product is $x^T y = \sum_i x_i y_i$. The Euclidean norm is $\|x\|$ (sometimes $\|x\|_2$ for clarity when other norms are in play). The all-ones vector is $\mathbf{1}$. The average of the entries of $x$ is $\operatorname{avg}(x) = \mathbf{1}^T x / n$.

This is a compound page: it defines four interlocking notions — the **Euclidean norm**, the **distance** between vectors, the **root-mean-square** value, and the **mean-square** value — because Boyd introduces them together and the formulas for one are obtained directly from the formulas for the others by simple algebraic manipulation.

---

# Axiom Motivation

What are we trying to capture with a norm? The desiderata are clear: we want a single non-negative number $\|x\|$ that measures the **magnitude** of the vector $x$, generalising the absolute value of a scalar to higher [[Def - Dimension|dimensions]]. The applied use cases — measuring the size of a residual, the distance between two data points, the energy of a signal — all want the same thing: a function $\|\cdot\| : \mathbb{R}^n \to \mathbb{R}_{\geq 0}$ that says "this vector is small / medium / large".

Four properties are non-negotiable. (i) **Non-negativity**: $\|x\| \geq 0$ always. (ii) **Definiteness**: $\|x\| = 0$ if and only if $x = 0$. The norm vanishes exactly at the zero vector — otherwise, $\|\cdot\|$ would conflate different vectors and lose its role as a magnitude. (iii) **Nonnegative homogeneity**: $\|\alpha x\| = |\alpha|\|x\|$ for any scalar $\alpha$. Scaling the vector by $\alpha$ should scale the magnitude by $|\alpha|$ — otherwise the norm would not respect the most basic vector-space operation. (iv) **Triangle inequality**: $\|x + y\| \leq \|x\| + \|y\|$. Going from the origin to $x + y$ is no longer than going to $x$ and then to $x + y$. This is what gives the resulting distance function the geometric structure of a metric.

These four properties define the *abstract* notion of a norm — any function satisfying them is "a norm" — but on $\mathbb{R}^n$ there is a Goldilocks choice: the **Euclidean norm** $\|x\| = \sqrt{x_1^2 + \cdots + x_n^2}$. Why this specific choice?

The Euclidean norm is the unique norm derived from an inner product: $\|x\| = \sqrt{x^T x}$. This is what makes it special among all norms: it interacts compatibly with angles, projections, orthogonality, and least-squares — all the geometric notions that fall out of the inner product. The other commonly-used norms — the $\ell^1$ norm $\|x\|_1 = \sum_i |x_i|$, the $\ell^\infty$ norm $\|x\|_\infty = \max_i |x_i|$ — are not inner-product norms and lack this rich geometric structure. They are useful for different purposes (sparsity for $\ell^1$, worst-case for $\ell^\infty$) but lose the angle/projection apparatus.

What if we weakened **definiteness** to allow $\|x\| = 0$ for some nonzero $x$? Then $\|\cdot\|$ is called a **seminorm**, and it identifies entire [[Def - Subspace|subspaces]] as "zero". Seminorms are useful (the seminorm $\|f\|_0 = |f(0)|$ on a function space, the seminorms in Sobolev spaces) but in $\mathbb{R}^n$ they are not what one means by "magnitude" — they only measure magnitude *modulo* some [[Def - Subspace|subspace]].

What if we **strengthened** by requiring $\|x + y\|^2 \leq \|x\|^2 + \|y\|^2$ unconditionally? This is the so-called "ultrametric" condition, and it forces every pair of vectors with disjoint support to behave as if orthogonal — too restrictive for the geometry of $\mathbb{R}^n$, where vectors at an acute angle have $\|x + y\|^2 > \|x\|^2 + \|y\|^2$.

The **distance** is the immediate corollary: $\operatorname{dist}(x, y) = \|x - y\|$. The four properties of the norm translate to the three properties of a *metric*: $\operatorname{dist}(x, y) \geq 0$ with equality iff $x = y$ (positivity), $\operatorname{dist}(x, y) = \operatorname{dist}(y, x)$ (symmetry), $\operatorname{dist}(x, z) \leq \operatorname{dist}(x, y) + \operatorname{dist}(y, z)$ (triangle inequality). The Euclidean distance is the standard notion of distance in $\mathbb{R}^2$ and $\mathbb{R}^3$, and it generalises verbatim to $\mathbb{R}^n$.

The **root-mean-square** value $\operatorname{rms}(x) = \|x\|/\sqrt n$ is a dimension-normalised version of the norm. The motivation is that $\|x\|$ scales with $\sqrt n$ for vectors with roughly-equal entries — for instance, $\|(\alpha, \alpha, \dots, \alpha)\| = |\alpha|\sqrt n$ — so as $n$ grows, $\|x\|$ inflates artificially. The RMS divides this out, giving a value that asymptotes to $|\alpha|$ regardless of $n$. This is exactly what you want when comparing vectors of different lengths or interpreting a norm as a "typical entry size".

---

# The Definition

**Euclidean norm.** For $x = (x_1, \dots, x_n) \in \mathbb{R}^n$, the **Euclidean norm** is
$$
\|x\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{x^T x}.
$$
When other norms are present, this is written $\|x\|_2$. In one dimension it reduces to the absolute value $|x|$.

**Euclidean distance.** For $a, b \in \mathbb{R}^n$, the **Euclidean distance** between $a$ and $b$ is
$$
\operatorname{dist}(a, b) = \|a - b\| = \sqrt{(a_1 - b_1)^2 + \cdots + (a_n - b_n)^2}.
$$
In one, two, and three [[Def - Dimension|dimensions]] this is the standard distance between the corresponding points.

**Mean-square value, root-mean-square value, RMS deviation.** For $x \in \mathbb{R}^n$:
$$
\operatorname{ms}(x) = \frac{\|x\|^2}{n} = \frac{x_1^2 + \cdots + x_n^2}{n}, \qquad \operatorname{rms}(x) = \sqrt{\operatorname{ms}(x)} = \frac{\|x\|}{\sqrt n}.
$$
For two vectors $x, y \in \mathbb{R}^n$, the **RMS deviation** is $\operatorname{rms}(x - y) = \|x - y\| / \sqrt n$.

**Properties of the norm.**
1. **Non-negative homogeneity:** $\|\alpha x\| = |\alpha|\|x\|$ for any scalar $\alpha$.
2. **Triangle inequality:** $\|x + y\| \leq \|x\| + \|y\|$.
3. **Non-negativity:** $\|x\| \geq 0$.
4. **Definiteness:** $\|x\| = 0 \iff x = 0$.

**Useful identities.** The norm of a sum: $\|x + y\|^2 = \|x\|^2 + 2 x^T y + \|y\|^2$. The norm of a stacked vector: $\|(a, b, c)\|^2 = \|a\|^2 + \|b\|^2 + \|c\|^2$. The **Chebyshev inequality**: if $k$ entries of $x$ have $|x_i| \geq a > 0$, then $k \leq \|x\|^2/a^2$.

---

# Relate to Other Fields / Compression

The Euclidean norm on $\mathbb{R}^n$ is the [[Def - Norm Induced by an Inner Product|norm induced by the standard inner product]]. The four norm properties listed above are the defining axioms of a *normed vector space*; any function on a vector space satisfying them is called a norm, and the pair $(V, \|\cdot\|)$ is a normed space. On $\mathbb{R}^n$, the Euclidean norm is the unique norm (up to scalar multiplication of the inner product) compatible with the geometry of *angles* — Cauchy–Schwarz, the angle definition, and the parallelogram law all require an inner product, and the Euclidean norm is the only one derived from one.

In functional analysis, the Euclidean norm is the special case $p = 2$ of the **$\ell^p$ norm** $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$ for $p \geq 1$. The cases $p = 1$ and $p = \infty$ are the other common ones; $p = 2$ is the only one whose unit ball is a perfect sphere, and the only one for which the parallelogram law holds. In probability, the RMS value of a random vector — the standard deviation of its norm — is the natural measure of spread, and the variance-decomposition $\operatorname{rms}(x)^2 = \operatorname{avg}(x)^2 + \operatorname{std}(x)^2$ is the deterministic analogue of $\mathbb{E}[X^2] = (\mathbb{E}[X])^2 + \operatorname{Var}(X)$.

**True name:** The Euclidean norm of $x$ is *the length of $x$ regarded as an arrow from the origin to the point $x$ in $\mathbb{R}^n$*. The Euclidean distance between $a$ and $b$ is *the length of the displacement from $a$ to $b$*. These are the same intuitions you have in two or three dimensions, transplanted verbatim to $n$ dimensions.

---

# Examples / Corollaries

**Is an instance — three-dimensional Euclidean distance.** For $a = (1, 2, 3)$ and $b = (4, 0, 3)$ in $\mathbb{R}^3$, $\operatorname{dist}(a, b) = \sqrt{9 + 4 + 0} = \sqrt{13} \approx 3.606$. This is the classical formula from analytic geometry, recovered as a special case of the general Euclidean distance.

**Is an instance — Boolean vector distance.** If $x, y \in \{0, 1\}^n$ are two Boolean vectors, then $\|x - y\|^2 =$ (number of indices where they differ), so $\|x - y\| = \sqrt{\operatorname{dist}_H(x, y)}$, where $\operatorname{dist}_H$ is the **Hamming distance**. The Euclidean distance between Boolean vectors is the square root of the count of disagreements.

**Is an instance — RMS of a constant vector.** For $x = \alpha \mathbf{1}$ (every entry equal to $\alpha$), $\|x\| = |\alpha| \sqrt n$ and $\operatorname{rms}(x) = |\alpha|$. The RMS is independent of $n$, which is what justifies its use as a "typical entry" measure.

**Is NOT an instance — the function $f(x) = \max_i x_i$ as a "norm".** The maximum-entry function is not a norm because it fails non-negativity (it can be negative) and definiteness (e.g., $f(-1, -2, -3) = -1$ but $x \neq 0$). The corrected function $\|x\|_\infty = \max_i |x_i|$ *is* a norm — the $\ell^\infty$ norm — but it is different from the Euclidean norm and lacks the inner-product structure.

**Is NOT an instance — the function $\rho(x) = x_1^2 + \cdots + x_n^2$ (the squared norm) as a "norm".** The squared norm is not a norm: it fails non-negative homogeneity, $\rho(\alpha x) = \alpha^2 \rho(x) \neq |\alpha| \rho(x)$. It is a *seminorm-squared* and is useful as the *objective function* of least-squares problems, but not as a norm itself.

**Corollary — the parallelogram law.** For any $x, y \in \mathbb{R}^n$,
$$\|x + y\|^2 + \|x - y\|^2 = 2 \|x\|^2 + 2 \|y\|^2.$$
This identity characterises inner-product norms among all norms: a norm $\|\cdot\|$ comes from an inner product if and only if it satisfies the parallelogram law. So the parallelogram law is a litmus test for "Euclidean-style" geometry.

**Corollary — Pythagorean theorem.** If $x^T y = 0$ (i.e., $x$ and $y$ are orthogonal), then $\|x + y\|^2 = \|x\|^2 + \|y\|^2$. This is the special case of the norm-of-sum identity where the cross term $2 x^T y$ vanishes. It generalises to any orthogonal sum: for pairwise orthogonal $x_1, \dots, x_k$, $\|x_1 + \cdots + x_k\|^2 = \|x_1\|^2 + \cdots + \|x_k\|^2$.

**Corollary — Chebyshev concentration.** The Chebyshev inequality $k \leq \|x\|^2 / a^2$ implies that *no entry of $x$ can exceed $\|x\|$ in absolute value*: if any $|x_i| > \|x\|$, the inequality with $k = 1$ would say $1 \leq \|x\|^2 / |x_i|^2 < 1$, a contradiction. Equivalently, $\|x\|_\infty \leq \|x\|_2$.

**Calibration check.** Verify that $\|(3, 4)\| = 5$ (the canonical $3$-$4$-$5$ triangle). Verify that for $x = (1, -2, 3, 2)$, $\operatorname{avg}(x) = 1$, $\|x - \operatorname{avg}(x) \mathbf 1\|^2 = 0 + 9 + 4 + 1 = 14$, and $\operatorname{rms}(x - \operatorname{avg}(x)\mathbf 1) = \sqrt{14/4} = 1.871\ldots$ — the standard deviation of $x$. Verify that $\|(1, 1, 1, 1)\|/\sqrt 4 = 1 = \operatorname{rms}((1, 1, 1, 1))$, showing that the RMS of a constant vector is the constant.

---

# Unlocked by This

> [!tip] The Cauchy–Schwarz Inequality and Angles *(from this topic)*
> Once the Euclidean norm is in place, the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]] $|a^T b| \leq \|a\| \|b\|$ becomes the gateway to *angles between vectors*: $\angle(a, b) = \arccos(a^T b / (\|a\|\|b\|))$ is well-defined. See [[Def - Angle Between Vectors]].

> [!tip] Norm-Induced Topology and Banach Spaces *(from Functional Analysis)*
> The Euclidean norm on $\mathbb{R}^n$ generates a *topology* — the standard topology — in which a sequence $x^{(k)} \to x$ iff $\|x^{(k)} - x\| \to 0$. Every norm on $\mathbb{R}^n$ generates the same topology (a fact called "equivalence of norms in finite dimensions"), but in infinite-dimensional spaces (function spaces, sequence spaces), different norms generate different topologies — the gateway to Banach spaces and functional analysis.

> [!tip] $L^p$ Spaces and Lebesgue Integration *(from Measure Theory)*
> The discrete RMS value $\operatorname{rms}(x) = \sqrt{(1/n)\sum_i x_i^2}$ is the discrete analogue of $\|f\|_{L^2(\mu)} = \sqrt{\int f^2 \,d\mu}$ for a function $f$ on a probability space. The whole theory of $L^p$ spaces lifts the Euclidean-norm ideas to infinite-dimensional function spaces, with the integral playing the role of the sum.
