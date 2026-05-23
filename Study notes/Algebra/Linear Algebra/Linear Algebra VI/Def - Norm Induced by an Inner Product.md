---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$. The inner product $\langle\cdot,\cdot\rangle$ takes values in $\mathbf{F}$ but $\langle v, v\rangle$ is always real and non-negative (a consequence of the inner-product axioms). The norm is denoted $\|v\|$. See [[Linear Algebra VI — §6 Inner Product Spaces]] for the full notation registry.

---

# Axiom Motivation

We have an inner product, which assigns to every pair $(u, v)$ a scalar $\langle u, v\rangle$. We want to extract from it a notion of **length** or **magnitude** of a single vector, generalising $|x|$ on $\mathbb{R}$ and $|z|$ on $\mathbb{C}$ to any inner product space. The most natural candidate is "compute the inner product of $v$ with itself, take the square root". This works because the inner product axioms guarantee $\langle v, v\rangle \geq 0$, so the square root is well-defined.

The question is whether this candidate is a "norm" in the abstract sense — a function $V \to [0, \infty)$ that captures the operational features of length. A general norm on a vector space is required to satisfy four properties: non-negativity, definiteness (zero only at zero), absolute homogeneity ($\|\lambda v\| = |\lambda|\,\|v\|$), and the triangle inequality ($\|u + v\| \leq \|u\| + \|v\|$). We need to check that $\sqrt{\langle v, v\rangle}$ satisfies all four. Non-negativity is immediate from positivity. Definiteness is immediate from the definiteness axiom of the inner product. Absolute homogeneity is a calculation: $\|\lambda v\|^2 = \langle \lambda v, \lambda v\rangle = \lambda \bar\lambda \langle v, v\rangle = |\lambda|^2 \|v\|^2$, so $\|\lambda v\| = |\lambda|\,\|v\|$. The triangle inequality is the non-trivial one and is proved as a consequence of the [[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz inequality]] — see [[Thm - Triangle Inequality]].

The deeper question — why this particular norm, and not any other — has a beautiful answer. The norm $\|v\| = \sqrt{\langle v, v\rangle}$ is special among all norms: it is the **unique** norm satisfying the [[Thm - Parallelogram Law|parallelogram law]] $\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2)$. Equivalently, a norm comes from an inner product if and only if it satisfies the parallelogram law (a theorem of Jordan and von Neumann from 1935). The $\ell^p$ norms on $\mathbb{R}^n$, for $p \neq 2$, do not satisfy the parallelogram law and hence are not induced by any inner product. This is the *characterising* property of inner-product norms, and it is what makes the $p = 2$ case so geometrically rich.

There is one further motivation that should be made explicit. The norm gives more than length: it gives a **metric** $d(u, v) = \|u - v\|$ that turns $V$ into a metric space, with all the convergence and continuity infrastructure that comes with it. This metric is what lets us speak of "the closest point in a [[Def - Subspace|subspace]]", which is the engine of the entire later chapter. So the norm is the gateway from algebra (the inner product as a bilinear form) to topology and analysis (the metric and its limits).

---

# The Definition

Let $(V, \langle\cdot,\cdot\rangle)$ be an inner product space over $\mathbf{F}$. The **norm** of $v \in V$ is the non-negative real number

$$
\|v\| = \sqrt{\langle v, v\rangle}.
$$

The norm is well-defined because $\langle v, v\rangle$ is a non-negative real (by positivity and conjugate symmetry).

The norm satisfies:

1. **Non-negativity.** $\|v\| \geq 0$ for every $v \in V$.
2. **Definiteness.** $\|v\| = 0$ if and only if $v = 0$.
3. **Absolute homogeneity.** $\|\lambda v\| = |\lambda|\,\|v\|$ for every $\lambda \in \mathbf{F}$, $v \in V$.
4. **Triangle inequality.** $\|u + v\| \leq \|u\| + \|v\|$ for every $u, v \in V$ (see [[Thm - Triangle Inequality]]).

It also satisfies the **parallelogram law** $\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2)$ (see [[Thm - Parallelogram Law]]), which characterises norms coming from an inner product.

The function $d : V \times V \to [0, \infty)$ defined by $d(u, v) = \|u - v\|$ is a **metric** on $V$, making $(V, d)$ a metric space.

---

# Relate to Other Fields / Compression

The inner-product norm $\|v\| = \sqrt{\langle v, v\rangle}$ is the **$\ell^2$ norm** when $V = \mathbf{F}^n$ with the Euclidean inner product, $\|x\|_2 = \sqrt{\sum |x_k|^2}$. On the same space one can put other norms — $\ell^1$ ($\|x\|_1 = \sum |x_k|$), $\ell^\infty$ ($\|x\|_\infty = \max |x_k|$), or more generally $\ell^p$ for $p \in [1, \infty]$ — and these turn $\mathbb{R}^n$ into a different Banach space for each $p$. Only $p = 2$ comes from an inner product; the rest do not satisfy the parallelogram law and so are *strictly more general* than the inner-product-norm case. This is the precise sense in which inner product spaces are special among normed spaces: they carry not just length but the entire geometry of right angles, projections, and orthogonal decompositions.

On the function-space side, the **$L^2$ norm** $\|f\|_2 = \sqrt{\int |f|^2}$ comes from the inner product $\langle f, g\rangle = \int f\bar g$. The $L^p$ norms for $p \neq 2$ do not, which is why $L^2$ is the only $L^p$ space that is a Hilbert space, and why Fourier analysis fits naturally in $L^2$ but is awkward in $L^p$ for $p \neq 2$.

**True name:** an inner-product norm is the unique norm such that the parallelogram law holds. Equivalently, it is the norm satisfying $\|u + v\|^2 - \|u - v\|^2 = 4 \operatorname{Re}\langle u, v\rangle$ — the **polarization identity** that recovers the inner product from the norm. The two pieces of data (norm, inner product) are interconvertible whenever either is given.

---

# Examples / Corollaries

**Is an instance: Euclidean norm on $\mathbb{R}^n$.** From the dot product $\langle x, y\rangle = \sum x_k y_k$, the induced norm is $\|x\| = \sqrt{x_1^2 + \cdots + x_n^2}$ — the standard length.

**Is an instance: Euclidean norm on $\mathbb{C}^n$.** From $\langle w, z\rangle = \sum w_k \bar z_k$, the induced norm is $\|z\| = \sqrt{|z_1|^2 + \cdots + |z_n|^2}$ — the absolute values are essential, because $z_k^2$ would be complex.

**Is an instance: $L^2$ norm on $C[a, b]$.** From $\langle f, g\rangle = \int_a^b fg$, the induced norm is $\|f\|_2 = \sqrt{\int_a^b f(x)^2\, dx}$. This is the "energy" of $f$, in the engineering interpretation.

**Is an instance: standard deviation as a norm.** On mean-zero random variables, $\langle X, Y\rangle = E[XY] = \operatorname{Cov}(X, Y)$, and the induced norm is $\|X\| = \sqrt{E[X^2]} = \sigma_X$, the standard deviation. So **standard deviation is the inner-product norm on the space of mean-zero random variables.**

**Is NOT an instance: the $\ell^1$ norm $\|x\|_1 = \sum |x_k|$ on $\mathbb{R}^n$ (for $n \geq 2$).** Check the parallelogram law on $u = (1, 0)$, $v = (0, 1)$: $\|u + v\|_1^2 + \|u - v\|_1^2 = 4 + 4 = 8$, but $2(\|u\|_1^2 + \|v\|_1^2) = 2(1 + 1) = 4$. Since $8 \neq 4$, the $\ell^1$ norm does not come from an inner product. This non-example shows that "being a norm" is genuinely weaker than "being an inner-product norm".

**Is NOT an instance: the $\ell^\infty$ norm $\|x\|_\infty = \max_k |x_k|$ on $\mathbb{R}^n$ (for $n \geq 2$).** Same vectors $u, v$ above: $\|u + v\|_\infty^2 + \|u - v\|_\infty^2 = 1 + 1 = 2$, but $2(\|u\|_\infty^2 + \|v\|_\infty^2) = 2(1 + 1) = 4$. Parallelogram law fails — again $\ell^\infty$ is a Banach space but not a Hilbert space.

**Corollary (norm-squared identity).** $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$. This is the algebraic identity behind the proof of the triangle inequality and the Pythagorean theorem. Over $\mathbb{R}$, the real-part disappears and the identity becomes $\|u + v\|^2 = \|u\|^2 + 2\langle u, v\rangle + \|v\|^2$.

**Corollary (polarization identity).** Over $\mathbb{R}$, $\langle u, v\rangle = \tfrac{1}{4}(\|u + v\|^2 - \|u - v\|^2)$. Over $\mathbb{C}$, $\langle u, v\rangle = \tfrac{1}{4}(\|u + v\|^2 - \|u - v\|^2 + i\|u + iv\|^2 - i\|u - iv\|^2)$. The norm determines the inner product. See [[Ex - Inner product determined by norm via the polarization identity]].

**Calibration check.** Three things a reader should verify: (i) for $z = (1, i) \in \mathbb{C}^2$ with the Euclidean inner product, $\|z\| = \sqrt{2}$, not $0$ — the conjugates rescue the answer; (ii) the parallelogram law holds for any two vectors in $\mathbb{R}^2$ with the dot product, but fails for the $\ell^1$ norm on the same space; (iii) for $f(x) = \sin x$ on $[-\pi, \pi]$ with $\langle f, g\rangle = \int fg$, the norm is $\|f\| = \sqrt{\pi}$ — the integral $\int_{-\pi}^\pi \sin^2 x\, dx = \pi$.

---

# Unlocked by This

> [!tip] Banach Space *(from Functional Analysis)*
> A **Banach space** is a complete normed vector space — a vector space with a norm in which every Cauchy sequence converges. Every Hilbert space is a Banach space, but not vice versa: $L^p(X, \mu)$ for $p \neq 2$ is a Banach space that is not a Hilbert space. Many classical spaces of analysis ($L^p$, $C(K)$ for $K$ compact, $C^k(\overline\Omega)$, the Sobolev spaces $W^{k,p}$ for $p \neq 2$) are Banach but not Hilbert, and the lack of an inner product means they lack orthogonal decomposition, but they retain norms, distances, and continuity.

> [!tip] Metric Space and Topology *(from Topology and Analysis)*
> The distance $d(u, v) = \|u - v\|$ turns any inner product space into a **metric space**, and hence a **topological space** with a notion of open and closed sets, convergence, and continuity. This is the gateway from finite-dimensional linear algebra to analysis: limits, derivatives, and integrals of operator-valued or function-valued objects are defined using the norm-induced metric. A finite-dimensional inner product space is automatically complete (every Cauchy sequence converges), so the analytic complications start in infinite dimensions.
