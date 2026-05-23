---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Field"
tags: [algebra, linear-algebra]
---

# Notation

The underlying field is $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ throughout this chapter. We write $\bar\lambda$ for the complex conjugate of $\lambda \in \mathbf{F}$, with the convention that $\bar\lambda = \lambda$ when $\mathbf{F} = \mathbb{R}$. The inner product is denoted $\langle u, v\rangle$, and the induced norm is $\|v\| = \sqrt{\langle v, v\rangle}$. We refer to the parent page [[Linear Algebra VI — §6 Inner Product Spaces]] for the full notation registry.

> [!warning] Convention: linearity in the first slot
> We follow Axler (LADR), Roman, and most pure-mathematics sources in taking the inner product to be **linear in the first slot** and **conjugate-linear (antilinear) in the second**:
> $$\langle \lambda u, v\rangle = \lambda \langle u, v\rangle, \qquad \langle u, \lambda v\rangle = \bar\lambda\, \langle u, v\rangle.$$
> Physicists (and any text using Dirac bra-ket notation $\langle\phi|\hat O|\psi\rangle$) use the opposite convention — linear in the **second** slot, conjugate-linear in the first. To convert a result between conventions, swap the two slots of every inner product and conjugate as appropriate. The mathematical content is identical; only the symbols rearrange.

---

# Axiom Motivation

The thing we are trying to axiomatize is **a way to measure both magnitude and relative orientation of vectors**. Look at the prototypical setting: $\mathbb{R}^3$ with the dot product $x \cdot y = x_1 y_1 + x_2 y_2 + x_3 y_3$. The dot product packs a lot of geometry into one operation. The length of $x$ is $\sqrt{x \cdot x}$. The angle $\theta$ between $x$ and $y$ satisfies $x \cdot y = \|x\|\,\|y\| \cos\theta$. Two vectors are perpendicular precisely when $x \cdot y = 0$. The projection of $x$ onto the line through $y$ is $(x \cdot y / y \cdot y)\, y$. We want to extract from this concrete operation the minimal set of properties that produce all of this geometry — and we want the properties to make sense not just on $\mathbb{R}^n$ but on any vector space, real or complex, finite-dimensional or otherwise. The axioms of an inner product are the answer.

Start with the requirement that $\langle v, v\rangle$ should be a non-negative real number, so that "$\sqrt{\langle v, v\rangle}$" is well-defined as a length. This forces **positivity**: $\langle v, v\rangle \geq 0$ for all $v$. We also want the length to be zero only for the zero vector — anything else, and there would be a non-zero vector whose distance to the origin is zero, breaking metric intuition entirely. This forces **definiteness**: $\langle v, v\rangle = 0$ if and only if $v = 0$. If we dropped definiteness, the resulting structure (a "semi-inner-product" or "positive semi-definite form") would give a "norm" that is zero on a nontrivial [[Def - Subspace|subspace]] — and we lose the ability to distinguish points. Concrete counterexample: on $\mathbb{R}^2$, the form $(x, y) \mapsto x_1 y_1$ is positive but not definite, since $(0, 1)$ has "length" zero, and the corresponding "metric" cannot tell $(0, 1)$ from $(0, 0)$.

Why **linearity in the first slot** — additivity $\langle u + v, w\rangle = \langle u, w\rangle + \langle v, w\rangle$ and homogeneity $\langle \lambda u, v\rangle = \lambda \langle u, v\rangle$? The motivation is the dot product: $(x + x') \cdot y = x \cdot y + x' \cdot y$ and $(\lambda x) \cdot y = \lambda (x \cdot y)$ are immediate from the formula $x \cdot y = \sum x_k y_k$, and they are what make the dot product *interact correctly* with the linear structure of the vector space. Drop linearity and you get a function that depends on $u$ in some non-linear way; the geometry of projections and orthogonality immediately breaks, because the projection formula $(\langle u, v\rangle / \|v\|^2)\, v$ depends on linearity of $\langle u, v\rangle$ in $u$ for "the projection of $u_1 + u_2$ is the sum of the projections" to hold. So if we ever want orthogonal projection to be a linear operator, linearity in one slot is forced.

Why **conjugate symmetry** $\langle u, v\rangle = \overline{\langle v, u\rangle}$ and not plain symmetry $\langle u, v\rangle = \langle v, u\rangle$? Over $\mathbb{R}$ they are the same condition. Over $\mathbb{C}$ they differ, and the choice of conjugate symmetry is forced by positivity. Here is the argument: if $\langle\cdot,\cdot\rangle$ were both linear in *both* slots and symmetric, then for any $v$ we would have $\langle iv, iv\rangle = i \cdot i \cdot \langle v, v\rangle = -\langle v, v\rangle$. So $\langle iv, iv\rangle = -\|v\|^2 \leq 0$. But then $\langle iv, iv\rangle$ is non-positive *and* by positivity non-negative, forcing $iv = 0$, hence $v = 0$. The only vector satisfying both is the zero vector — so plain symmetric bilinearity is incompatible with positivity over $\mathbb{C}$. The repair is to introduce conjugation in one slot: conjugate symmetry plus linearity-in-first-slot gives $\langle iv, iv\rangle = i \cdot \bar i \cdot \langle v, v\rangle = |i|^2 \|v\|^2 = \|v\|^2 \geq 0$, restoring positivity. The conjugate is the price the complex inner product pays for being compatible with the complex structure.

Conjugate symmetry has a second consequence: $\langle v, v\rangle = \overline{\langle v, v\rangle}$, so $\langle v, v\rangle$ is automatically **real**, and the positivity axiom is then a meaningful statement (otherwise "non-negative" would not make sense for a complex number). Conjugate-linearity in the second slot is then forced: $\langle u, \lambda v\rangle = \overline{\langle \lambda v, u\rangle} = \overline{\lambda \langle v, u\rangle} = \bar\lambda \overline{\langle v, u\rangle} = \bar\lambda \langle u, v\rangle$. So we get the "sesquilinear" (one-and-a-half-linear) structure for free from linearity-in-first-slot plus conjugate-symmetry.

The test of the axioms: could a reader who has never seen this definition invent it from the desiderata "magnitude, angle, perpendicularity, projection, applicable to real and complex spaces"? Positivity and definiteness give magnitude and the property "zero iff trivial". Linearity in the first slot gives compatibility with the linear structure (and hence the existence of linear projections). Conjugate symmetry rescues positivity over $\mathbb{C}$ and forces $\langle v, v\rangle \in \mathbb{R}$. There is no further axiom; these four (positivity, definiteness, linearity-in-first-slot, conjugate symmetry) are minimal and sufficient.

---

# The Definition

Let $V$ be a vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$. An **inner product** on $V$ is a function $\langle\cdot,\cdot\rangle : V \times V \to \mathbf{F}$ satisfying:

1. **Positivity.** $\langle v, v\rangle \geq 0$ for every $v \in V$, where the order on $\mathbf{F}$ is the order on $\mathbb{R}$ (and a complex number is "$\geq 0$" by definition meaning real and non-negative).
2. **Definiteness.** $\langle v, v\rangle = 0$ if and only if $v = 0$.
3. **Additivity in the first slot.** $\langle u + v, w\rangle = \langle u, w\rangle + \langle v, w\rangle$ for all $u, v, w \in V$.
4. **Homogeneity in the first slot.** $\langle \lambda u, v\rangle = \lambda \langle u, v\rangle$ for all $\lambda \in \mathbf{F}$, $u, v \in V$.
5. **Conjugate symmetry.** $\langle u, v\rangle = \overline{\langle v, u\rangle}$ for all $u, v \in V$.

An **inner product space** is a pair $(V, \langle\cdot,\cdot\rangle)$ consisting of a vector space together with an inner product on it. When the inner product is clear from context, we abuse language and call $V$ itself the inner product space.

Conjugate-linearity in the second slot — $\langle u, v + w\rangle = \langle u, v\rangle + \langle u, w\rangle$ and $\langle u, \lambda v\rangle = \bar\lambda \langle u, v\rangle$ — follows from axioms 3–5 and is therefore not listed separately.

---

# Categorical / Structural Definition

An inner product on $V$ over $\mathbb{R}$ is a **symmetric positive-definite bilinear form** — equivalently, an element of $\operatorname{Sym}^2 V^*$ that is positive-definite as a quadratic form. Over $\mathbb{C}$, it is a **conjugate-symmetric positive-definite sesquilinear form** — an element of $\overline{V}^* \otimes V^*$ that is conjugate-symmetric and positive-definite.

The categorical perspective: a **real inner product space** is a vector space $V$ together with a chosen isomorphism $V \cong V^*$ that is symmetric (its transpose equals itself) and positive (the resulting pairing $V \otimes V \to \mathbb{R}$ takes diagonal elements to non-negative reals). This is the Riesz isomorphism made the *defining datum* rather than a derived consequence: an inner product *is* a choice of identification of $V$ with its dual.

This perspective is what makes the theory transport: a Riemannian manifold has an inner product on each tangent space, smoothly varying — that is, a smooth choice of isomorphism $TM \cong T^*M$, which is exactly the **metric tensor**. A pseudo-Riemannian manifold (such as the spacetime of general relativity) has the same data but without positivity. The inner product axioms are picking out exactly the *positive-definite* case of the more general structure of "a non-degenerate symmetric or Hermitian bilinear form".

A **morphism** of inner product spaces — an **[[Def - Isometry|isometry]]** — is a linear map $T : V \to W$ preserving the inner product, $\langle Tu, Tv\rangle_W = \langle u, v\rangle_V$. [[Def - Isometry|Isometries]] are the natural notion of "equivalence of geometry" on vector spaces, and they form a [[Def - Group|group]] $O(V)$ (the orthogonal [[Def - Group|group]], when $V$ is real) or $U(V)$ (the unitary group, when $V$ is complex).

---

# Relate to Other Fields / Compression

An inner product space is the bare minimum structure on a vector space that lets you do **Euclidean geometry**. Drop positivity (keep symmetry and non-degeneracy) and you get **pseudo-inner-product spaces**, of which [[Def - Minkowski Space and the Metric|Minkowski space]] is the canonical physical example. Drop definiteness (keep positivity) and you get a **semi-inner-product space**, which appears in the construction of $L^p$ for $p = 2$ as a quotient by the null subspace. Add completeness in the induced metric and you get a **Hilbert space**, the central object of functional analysis. Generalise from a single bilinear form to a smooth field of forms on a manifold and you get a **Riemannian metric**.

The compression that makes an inner product compute geometry is that one bilinear form *simultaneously* encodes length (via $\langle v, v\rangle$), angle (via $\arccos(\langle u, v\rangle / (\|u\|\,\|v\|))$), orthogonality ($\langle u, v\rangle = 0$), and the canonical isomorphism $V \cong V^*$ (Riesz). A naive separate-axioms approach would require length, angle, perpendicularity, and duality as four independent structures; the inner product packs them into one.

**True name:** an inner product is the *positive-definite case* of a non-degenerate symmetric (or Hermitian) bilinear form. The chapter and the rest of finite-dimensional inner-product-space theory is "what extra you get when you assume the form is positive definite".

---

# Examples / Corollaries

**Is an instance: the Euclidean inner product on $\mathbf{F}^n$.** For $w = (w_1, \dots, w_n), z = (z_1, \dots, z_n) \in \mathbf{F}^n$, define $\langle w, z\rangle = w_1 \bar z_1 + \cdots + w_n \bar z_n$. Over $\mathbb{R}$ this is the familiar dot product $\sum w_k z_k$. All five axioms are immediate from the field axioms in $\mathbf{F}$. This is the inner product on $\mathbf{F}^n$ unless one is told otherwise.

**Is an instance: weighted inner product on $\mathbf{F}^n$.** Fix positive numbers $c_1, \dots, c_n > 0$ and define $\langle w, z\rangle = \sum_k c_k w_k \bar z_k$. Positivity holds because each $c_k > 0$, and the other axioms transfer from the Euclidean case. Changing the $c_k$'s rescales the geometry: the unit ball becomes an axis-aligned ellipsoid with semi-axes $1/\sqrt{c_k}$. This shows that the "shape of the unit ball" is not determined by the vector space alone — different inner products give genuinely different geometries on the same underlying vector space.

**Is an instance: $L^2$ inner product on continuous functions.** Let $V = C[a, b]$, the space of continuous real-valued functions on $[a, b]$. Define $\langle f, g\rangle = \int_a^b f(x) g(x)\, dx$. Positivity follows because $\int f^2 \geq 0$, and definiteness because a non-negative continuous function with integral zero is identically zero. Linearity and symmetry are immediate from the linearity of the integral. This is the prototype of infinite-dimensional inner product spaces; its completion is $L^2[a, b]$, a Hilbert space.

**Is an instance: an inner product on $\mathcal{P}(\mathbb{R})$ with point-and-derivative data.** On polynomials, $\langle p, q\rangle = p(0) q(0) + \int_{-1}^1 p'(x) q'(x)\, dx$ is an inner product (LADR example 6.3(d)). Positivity is clear; definiteness uses that if $\langle p, p\rangle = 0$ then $p(0) = 0$ and $p' = 0$, hence $p = 0$. This shows that inner products can incorporate *both* point evaluation and integral information; the freedom in choosing an inner product is much larger than the canonical examples suggest.

**Is an instance: covariance as an inner product on mean-zero random variables.** On the space of mean-zero random variables with finite variance, $\langle X, Y\rangle = E[XY] = \operatorname{Cov}(X, Y)$ is an inner product (after quotienting by random variables that are almost-surely zero, to enforce definiteness). The induced norm is the standard deviation, $\|X\| = \sigma_X$. The angle satisfies $\cos\theta = \operatorname{Cov}(X, Y)/(\sigma_X \sigma_Y) = \rho(X, Y)$, the correlation coefficient. The Cauchy-Schwarz inequality $|\operatorname{Cov}(X, Y)| \leq \sigma_X \sigma_Y$ is exactly $|\rho| \leq 1$.

**Is NOT an instance: $(x, y) \mapsto |x_1 y_1| + |x_2 y_2|$ on $\mathbb{R}^2$.** This function is positive and definite but fails linearity: $((-1)\cdot 1) y_1 = -y_1 \neq -|y_1| = |(-1)\cdot 1| \cdot |y_1|$ already shows the failure. The absolute values break the linear structure entirely. This non-example probes axiom (4): linearity must be honest, not "linearity in absolute value".

**Is NOT an instance: $(x, y) \mapsto x_1 y_1 + x_3 y_3$ on $\mathbb{R}^3$.** This is bilinear and symmetric but fails definiteness: $\langle (0, 1, 0), (0, 1, 0)\rangle = 0$ despite $(0, 1, 0) \neq 0$. The form is positive *semi-*definite, missing only definiteness. The geometry on $\mathbb{R}^3$ it gives is the geometry of $\mathbb{R}^3 / \operatorname{span}(e_2)$, which is well-defined on the quotient but not on $\mathbb{R}^3$ itself. Non-example probing axiom (2).

**Is NOT an instance: the Minkowski metric $\langle x, y\rangle = -x^0 y^0 + x^1 y^1 + x^2 y^2 + x^3 y^3$ on $\mathbb{R}^4$.** This is bilinear, symmetric, non-degenerate, but **indefinite**: a timelike vector $(1, 0, 0, 0)$ has $\langle v, v\rangle = -1 < 0$, and a lightlike vector $(1, 1, 0, 0)$ has $\langle v, v\rangle = 0$ despite being nonzero. So both positivity and definiteness fail. See [[Def - Minkowski Space and the Metric]]. This is the indefinite generalization that special relativity demands.

**Corollary (basic properties of $\langle\cdot,\cdot\rangle$).** From the axioms, for every $u, v, w \in V$ and $\lambda \in \mathbf{F}$:
- $\langle 0, v\rangle = \langle v, 0\rangle = 0$ (linearity).
- $\langle u, v + w\rangle = \langle u, v\rangle + \langle u, w\rangle$ (additivity in second slot, from additivity in first slot + conjugate symmetry).
- $\langle u, \lambda v\rangle = \bar\lambda \langle u, v\rangle$ (conjugate-linearity in second slot).
- $\langle v, v\rangle \in \mathbb{R}$ for every $v$ (conjugate symmetry forces $\langle v, v\rangle = \overline{\langle v, v\rangle}$).

**Calibration check.** Three verifications a reader should be able to perform after reading the definition: (i) verify that the Euclidean inner product on $\mathbb{C}^2$, $\langle (w_1, w_2), (z_1, z_2)\rangle = w_1 \bar z_1 + w_2 \bar z_2$, satisfies all five axioms (the conjugate is essential for positivity); (ii) compute $\langle (1, i), (1, i)\rangle$ and confirm it equals $2$, not $0$ (this checks understanding of the conjugate); (iii) check that the form $(x, y) \mapsto x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ violates positivity, and identify the offending vector.

---

# Unlocked by This

> [!tip] Hilbert Space *(from Functional Analysis)*
> A **Hilbert space** is an inner product space that is **complete** in the metric $d(u, v) = \|u - v\|$ — every Cauchy sequence converges. The canonical example is $L^2(X, \mu)$, the space of (equivalence classes of) measurable functions with $\int |f|^2\, d\mu < \infty$, equipped with $\langle f, g\rangle = \int f \bar g\, d\mu$. Hilbert spaces are the natural setting for: Fourier analysis (orthonormal expansions in $L^2$), quantum mechanics (states as unit vectors, observables as self-adjoint operators), partial differential equations (Sobolev spaces $H^s$), and statistical estimation (Hilbert space of random variables). Almost the entire content of this chapter — Cauchy-Schwarz, Gram-Schmidt, Riesz representation, orthogonal projection, best approximation — extends with one caveat: orthogonal-complement decompositions $V = U \oplus U^\perp$ require $U$ to be **closed** as a subspace.

> [!tip] Riemannian Metric *(from Differential Geometry)*
> A **Riemannian metric** on a smooth manifold $M$ is a smoothly-varying choice of inner product $g_p$ on each tangent space $T_p M$. The metric tensor $g$ is then a section of $\operatorname{Sym}^2 T^*M$ that is positive-definite at every point. The Riemannian metric controls geometry on $M$: lengths of curves are $\int_a^b \sqrt{g_{\gamma(t)}(\dot\gamma, \dot\gamma)}\, dt$, the gradient of a function is the metric dual of its differential, geodesics are paths of shortest length. Special relativity replaces the positive-definiteness with indefiniteness of signature $(1, 3)$ (giving Lorentzian / pseudo-Riemannian geometry), and general relativity makes the metric the dynamical field of physics.

> [!tip] $C^*$-algebra and Operator Algebras *(from Operator Theory)*
> The algebra $\mathcal{B}(H)$ of bounded operators on a Hilbert space $H$ has a canonical involution $T \mapsto T^*$ (the adjoint, defined via the inner product) and a norm $\|T\| = \sup_{\|v\| = 1} \|Tv\|$. These satisfy the **$C^*$-identity** $\|T^*T\| = \|T\|^2$, the defining axiom of an abstract $C^*$-algebra. The entire subject of operator algebras — including von Neumann algebras, quantum group symmetries, free probability — is the abstract theory of such structures, with the inner product on the underlying Hilbert space as its origin.
