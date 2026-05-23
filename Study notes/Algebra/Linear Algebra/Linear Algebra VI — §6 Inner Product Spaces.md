---
type: topic
subject: linear-algebra
chapter: "6"
title: "Linear Algebra VI — Inner Product Spaces"
tags: [algebra, linear-algebra]
---

# Notation Registry

The standing convention of this chapter is that $\mathbf{F}$ denotes either the real field $\mathbb{R}$ or the complex field $\mathbb{C}$. Every vector space is over $\mathbf{F}$, and every inner product is the one inherited from $\mathbf{F}$. Linearity conventions differ between communities and the choice matters as soon as $\mathbf{F} = \mathbb{C}$:

> [!warning] Convention: linearity in the first slot
> We follow Axler (LADR): the inner product $\langle\cdot,\cdot\rangle$ is **linear in the first slot** and conjugate-linear in the second. So $\langle \lambda u, v\rangle = \lambda \langle u, v\rangle$ but $\langle u, \lambda v\rangle = \bar\lambda \langle u, v\rangle$. Most pure-mathematics textbooks (Roman, Conway, Rudin) use this convention. Physicists and many quantum-mechanics texts use the opposite — linear in the **second** slot, conjugate-linear in the first — because of Dirac bra-ket notation $\langle\phi|\hat O|\psi\rangle$. Converting between conventions is mechanical: swap the slots of every inner product, and the chapter goes through verbatim with conjugates flipped.

- $V, W$ — inner product spaces over $\mathbf{F}$ (always finite-dimensional in this chapter unless stated)
- $\langle u, v\rangle$ — inner product of vectors $u, v \in V$
- $\|v\| = \sqrt{\langle v, v\rangle}$ — the **norm** of $v$ induced by the inner product
- $\bar\lambda$ — complex conjugate of $\lambda \in \mathbf{F}$; equals $\lambda$ when $\mathbf{F} = \mathbb{R}$
- $u \perp v$ — $u$ is **orthogonal** to $v$, that is $\langle u, v\rangle = 0$
- $e_1, \dots, e_n$ — typically an **orthonormal basis**: $\langle e_j, e_k\rangle = \delta_{jk}$
- $\delta_{jk}$ — Kronecker delta, equal to $1$ if $j = k$ and $0$ otherwise
- $U^\perp$ — the **orthogonal complement** $\{v \in V : \langle u, v\rangle = 0 \text{ for every } u \in U\}$
- $P_U$ — the **orthogonal projection** of $V$ onto a finite-dimensional subspace $U \subseteq V$
- $T^\dagger$ — the **pseudoinverse** of a linear map $T \in \mathcal{L}(V, W)$
- $\mathcal{L}(V, W)$ — linear maps $V \to W$; $V' = \mathcal{L}(V, \mathbf{F})$ is the dual space
- $\mathcal{P}_m(\mathbf{F})$ — polynomials of degree at most $m$ with coefficients in $\mathbf{F}$
- $\mathbf{F}^n$ with the **Euclidean inner product** $\langle (w_1, \dots, w_n), (z_1, \dots, z_n)\rangle = w_1 \bar z_1 + \cdots + w_n \bar z_n$
- $C[a, b]$ with the inner product $\langle f, g\rangle = \int_a^b f\bar g$ — the prototypical infinite-dimensional inner product space

---

# Motivation

Here is the entire topic in one sentence: an inner product is the structure that turns a bare vector space into a space with geometry. A vector space alone supports addition and scalar multiplication — the linear structure — but says nothing about length, angle, or perpendicularity. Adding a single bilinear (or sesquilinear) form $\langle\cdot,\cdot\rangle$ recovers all three at once. The norm $\|v\| = \sqrt{\langle v, v\rangle}$ is length; the distance $d(u, v) = \|u - v\|$ is distance; the formula $\cos\theta = \langle u, v\rangle / (\|u\|\,\|v\|)$ is angle; and orthogonality $\langle u, v\rangle = 0$ is perpendicularity. Even more, the inner product produces an identification $V \cong V'$ (the **Riesz representation theorem**), turning every linear functional into "take the inner product with some vector". The inner product is the price of admission to geometry inside a vector space.

The unifying frame of the chapter is **orthogonal projection as the bridge between minimization and orthogonality**. A typical problem in applied mathematics, and the problem this chapter exists to solve, is: given a subspace $U \subseteq V$ and a point $v \in V$, find the closest point in $U$ to $v$. The answer is the orthogonal projection $P_U v$, and the reason it works is a single picture: the closest point in $U$ to $v$ is the foot of the perpendicular from $v$ to $U$. The minimization problem and the orthogonality condition are the same problem viewed from two angles. This single identification unifies Gram-Schmidt (orthogonalizing a basis), Fourier expansion (writing a function as a sum of $\sin nx$, $\cos nx$), least squares (best-fitting a line to noisy data), and best polynomial approximation (replacing $\sin x$ by a degree-$5$ polynomial). Every one of these is "project onto a subspace".

There is one structural backbone for the chapter, the chain of equivalences that makes orthonormal bases the right thing to compute with:

$$
\text{inner product on } V \;\Longrightarrow\; \text{Gram-Schmidt} \;\Longrightarrow\; \text{orthonormal basis} \;\Longrightarrow\; V = U \oplus U^\perp \;\Longrightarrow\; P_U \text{ exists} \;\Longrightarrow\; \text{minimization solved.}
$$

Read left to right, the chapter is a single argument: an inner product lets you orthonormalize, an orthonormal basis decomposes the space into a subspace and its complement, this decomposition is the orthogonal projection, and the orthogonal projection solves every minimization problem. Read right to left, every applied-mathematics question about "closest point" is secretly a question about orthogonality.

A reader is assumed to have refreshed the notion of a [[Def - Vector Space|vector space]], a [[Def - Basis|basis]], a [[Def - Subspace|subspace]], a [[Def - Linear Map|linear map]], the dual space and dual basis (from [[Linear Algebra IV — §3E–F Products, Quotients, Duality]]), and the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] (rank-nullity). Familiarity with the complex conjugate $\bar\lambda$ and the modulus $|\lambda| = \sqrt{\lambda \bar\lambda}$ for $\lambda \in \mathbb{C}$ is essential — sesquilinearity is the one technical wrinkle separating real inner products from complex ones.

---

# Concept Map

## §6A Inner Products and Norms

- **[[Def - Inner Product Space]]**
	- An **inner product** on a vector space $V$ over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ is a function $\langle\cdot,\cdot\rangle : V \times V \to \mathbf{F}$ that is positive ($\langle v, v\rangle \geq 0$ with equality iff $v = 0$), linear in the first slot, and conjugate-symmetric ($\langle u, v\rangle = \overline{\langle v, u\rangle}$). An **inner product space** is the pair $(V, \langle\cdot,\cdot\rangle)$. Canonical examples are $\mathbf{F}^n$ with the Euclidean inner product $\langle w, z\rangle = \sum w_i \bar z_i$, and $C[a, b]$ with $\langle f, g\rangle = \int_a^b f \bar g$; both are the prototypes of finite- and infinite-dimensional cases respectively. The positivity axiom is what makes $\langle v, v\rangle$ a *square length*; conjugate-symmetry is what forces $\langle v, v\rangle$ to be real in the first place.

- **[[Def - Norm Induced by an Inner Product]]**
	- The **norm** of $v \in V$ is $\|v\| = \sqrt{\langle v, v\rangle}$, well-defined because $\langle v, v\rangle \geq 0$. It satisfies $\|v\| = 0 \iff v = 0$, the homogeneity $\|\lambda v\| = |\lambda|\,\|v\|$, and the triangle inequality $\|u + v\| \leq \|u\| + \|v\|$. Conversely, a norm satisfies the [[Thm - Parallelogram Law|parallelogram law]] if and only if it comes from an inner product (via the [[Ex - Inner product determined by norm via the polarization identity|polarization identity]]); not every norm has this property — the $\ell^1$ and $\ell^\infty$ norms on $\mathbb{R}^n$ do not. The distance $d(u, v) = \|u - v\|$ then turns $V$ into a metric space.

- **[[Def - Orthogonal and Orthonormal Vectors]]**
	- Two vectors $u, v$ are **orthogonal**, written $u \perp v$, if $\langle u, v\rangle = 0$. A list $e_1, \dots, e_m$ is **orthonormal** if each vector has norm $1$ and any two distinct vectors are orthogonal — equivalently $\langle e_j, e_k\rangle = \delta_{jk}$. The orthogonality relation generalises perpendicularity from Euclidean geometry: in $\mathbb{R}^2$ with the dot product, $u \perp v$ exactly when the lines through the origin in directions $u$ and $v$ meet at a right angle. The zero vector is orthogonal to everything, and it is the only vector orthogonal to itself.

- **[[Thm - Pythagorean Theorem]]**
	- If $u \perp v$ in an inner product space, then $\|u + v\|^2 = \|u\|^2 + \|v\|^2$. The proof is one line: expand $\|u + v\|^2 = \langle u + v, u + v\rangle = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2$, and the two middle terms vanish by orthogonality. This is the *abstract* form of Pythagoras — the classical statement about right triangles in $\mathbb{R}^2$ is recovered when $V = \mathbb{R}^2$ — and it underlies every later result, because "compute a squared norm and discard cross-terms by orthogonality" is the engine of orthonormal-basis computations.

- **[[Thm - Cauchy-Schwarz Inequality]]**
	- For all $u, v \in V$, $|\langle u, v\rangle| \leq \|u\|\,\|v\|$, with equality iff one vector is a scalar multiple of the other. This is the single most-used inequality in inner product spaces. It says the angle formula $\cos\theta = \langle u, v\rangle / (\|u\|\,\|v\|)$ has $|\cos\theta| \leq 1$, making the *definition* of angle in $\mathbb{R}^n$ for $n \geq 4$ consistent. The cleanest proof is the **discriminant proof**: $\|u - t v\|^2$ is a non-negative real quadratic in $t \in \mathbb{R}$, so its discriminant is $\leq 0$ — that discriminant condition is exactly Cauchy-Schwarz.

- **[[Thm - Triangle Inequality]]**
	- For all $u, v \in V$, $\|u + v\| \leq \|u\| + \|v\|$. This is the geometric statement that the side of a triangle is shorter than the sum of the other two sides, and it follows from Cauchy-Schwarz in two lines: $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2 \leq \|u\|^2 + 2|\langle u, v\rangle| + \|v\|^2 \leq (\|u\| + \|v\|)^2$. Equality holds when one vector is a non-negative real multiple of the other. The reverse triangle inequality $|\|u\| - \|v\|| \leq \|u - v\|$ follows by applying the forward direction to $u$ and $u - v$.

- **[[Thm - Parallelogram Law]]**
	- For all $u, v \in V$, $\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2)$. The geometric content is that in any parallelogram, the sum of the squared diagonals equals the sum of the squared sides — Euclidean geometry done in any inner product space. Algebraically it is the identity that *characterises* inner-product norms among all norms: a norm comes from an inner product if and only if it satisfies this law (Jordan-von Neumann, 1935). The polarization identity recovers $\langle u, v\rangle$ from the norm alone.

- **[[Ex - Cauchy-Schwarz attained iff one vector is a scalar multiple of the other]]** (⭐⭐)
	- Show that $|\langle u, v\rangle| = \|u\|\,\|v\|$ if and only if one of $u, v$ is a scalar multiple of the other, with the scalar non-negative-real in the corresponding triangle-inequality case.

- **[[Ex - Inner product determined by norm via the polarization identity]]** (⭐⭐)
	- Prove the **polarization identity**: in a real inner product space $\langle u, v\rangle = \tfrac{1}{4}(\|u + v\|^2 - \|u - v\|^2)$; in a complex inner product space, the analogous identity uses four norms with $u + i^k v$ for $k = 0, 1, 2, 3$.

> [!tip] Unlocked: Indefinite [[Def - Bilinear Form|Bilinear Form]] *(from Special Relativity / Differential Geometry)*
> An inner product is a **positive-definite** symmetric (or Hermitian) bilinear form. Dropping positive-definiteness gives an **indefinite bilinear form**, the structure on [[Def - Minkowski Space and the Metric|Minkowski space]] $\mathbb{R}^4$ with $\langle x, y\rangle = -x^0 y^0 + x^1 y^1 + x^2 y^2 + x^3 y^3$. Almost every formal manipulation in this chapter goes through — the Cauchy-Schwarz inequality flips direction for timelike vectors, the Pythagorean theorem becomes the law of intervals — but the geometry changes radically: vectors can be "perpendicular to themselves" (lightlike), and the signature $(+, -, -, -)$ versus $(-, +, +, +)$ becomes a genuine physical choice.

> [!tip] Unlocked: Hilbert Space *(from Functional Analysis)*
> A **Hilbert space** is an infinite-dimensional inner product space that is **complete** in the induced metric — every Cauchy sequence converges. Lebesgue $L^2(X, \mu)$ is the canonical example. Almost the entire chapter generalizes verbatim with one caveat: in infinite [[Def - Dimension|dimensions]] one must add completeness assumptions, since orthogonal-complement decompositions $V = U \oplus U^\perp$ require $U$ to be a *closed* subspace. Bessel's inequality, the Riesz representation theorem, and the orthogonal-projection-as-minimizer theorem all extend; Gram-Schmidt extends to give countable orthonormal sequences. Modern quantum mechanics, signal processing, and PDE analysis all live in Hilbert spaces.

> [!note] Exercise Index — §6A
> [[Exercise Index - §6A Inner Products and Norms]]

## §6B Orthonormal Bases

- **[[Def - Orthonormal Basis]]**
	- An **orthonormal basis** of a finite-dimensional inner product space $V$ is a basis whose vectors form an orthonormal list — pairwise orthogonal and each of norm $1$. The standard basis $e_1, \dots, e_n$ of $\mathbf{F}^n$ with the Euclidean inner product is orthonormal; the basis $\{\cos kx, \sin kx\}$ of trigonometric polynomials is orthonormal in $L^2[-\pi, \pi]$ with appropriate normalisation. The defining feature is that the matrix of the inner product in this basis is the identity, $\langle e_j, e_k\rangle = \delta_{jk}$, which makes every inner-product computation maximally clean.

- **[[Ex - Orthonormal lists are linearly independent]]** (⭐)
	- Prove that every orthonormal list is linearly independent. The proof is the one-line application of orthonormality: if $\sum a_k e_k = 0$, take the inner product with $e_j$.

- **[[Thm - Gram-Schmidt Procedure]]**
	- Given a linearly independent list $v_1, \dots, v_m$ in an inner product space, **Gram-Schmidt** constructs an orthonormal list $e_1, \dots, e_m$ with the same span, and indeed with $\operatorname{span}(v_1, \dots, v_k) = \operatorname{span}(e_1, \dots, e_k)$ for each $k$. The construction is inductive: at step $k$, subtract from $v_k$ its orthogonal projection onto $\operatorname{span}(e_1, \dots, e_{k-1})$ and normalise. The corollaries are immediate and powerful: every finite-dimensional inner product space has an orthonormal basis, and every orthonormal list extends to one. The procedure also gives the **QR factorization** $A = QR$ of a matrix with linearly independent columns.

- **[[Thm - Riesz Representation Theorem (Finite-Dimensional)]]**
	- For a finite-dimensional inner product space $V$ and a linear functional $\varphi \in V'$, there exists a **unique** $v \in V$ such that $\varphi(u) = \langle u, v\rangle$ for every $u \in V$. The map $v \mapsto \langle\cdot, v\rangle$ is the **canonical isomorphism** $V \cong V'$ that an inner product provides. The construction is mechanical: with an orthonormal basis, $v = \sum_k \overline{\varphi(e_k)}\, e_k$. The result *fails* in infinite [[Def - Dimension|dimensions]] without completeness — see the warning callout below — and its extension to Hilbert spaces is the cornerstone of functional analysis.

- **[[Ex - Best polynomial approximation to sine]]** (⭐⭐)
	- Find the polynomial $p \in \mathcal{P}_5(\mathbb{R})$ minimising $\int_{-\pi}^\pi (\sin x - p(x))^2 \, dx$. The route is to Gram-Schmidt the basis $1, x, x^2, \dots, x^5$ with the $L^2[-\pi, \pi]$ inner product, then project $\sin x$ onto $\operatorname{span}(1, x, \dots, x^5)$.

- **[[Ex - Legendre polynomials from Gram-Schmidt]]** (⭐⭐)
	- Apply Gram-Schmidt to $1, x, x^2, \dots$ in $C[-1, 1]$ with inner product $\langle f, g\rangle = \int_{-1}^1 fg$, and verify the result is (proportional to) the **Legendre polynomials** $P_n(x)$.

> [!tip] Unlocked: Fourier Series *(from Analysis)*
> A **Fourier series** expands a periodic function $f \in L^2[-\pi, \pi]$ as $f(x) = \sum_{n \in \mathbb{Z}} c_n e^{inx}$ with $c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f(x) e^{-inx}\, dx$. The exponentials $\{e^{inx}/\sqrt{2\pi}\}$ form a (countable) orthonormal basis of $L^2[-\pi, \pi]$, and the formula for $c_n$ is exactly "$c_n = \langle f, e_n\rangle$" — the same expansion-coefficient formula as for finite-dim orthonormal bases. **Bessel's inequality** $\sum |c_n|^2 \leq \|f\|^2$ and its strengthening to **Parseval's identity** $\sum |c_n|^2 = \|f\|^2$ are the infinite-dimensional Pythagorean theorem. Modern signal processing, harmonic analysis, and PDE theory are built on this identification.

> [!tip] Unlocked: Orthogonal Polynomials *(from Special Functions)*
> Applying Gram-Schmidt to $1, x, x^2, \dots$ on an interval $[a, b]$ with weight function $w(x) > 0$, using the inner product $\langle f, g\rangle = \int_a^b f(x)g(x) w(x)\,dx$, produces a sequence of **orthogonal polynomials**. Different weights give different classical families: weight $1$ on $[-1, 1]$ gives **Legendre polynomials** (geometry of the sphere, quadrature); weight $e^{-x^2}$ on $\mathbb{R}$ gives **Hermite polynomials** (quantum harmonic oscillator); weight $e^{-x}$ on $[0, \infty)$ gives **Laguerre polynomials** (hydrogen atom radial wavefunctions); weight $(1 - x^2)^{-1/2}$ on $[-1, 1]$ gives **Chebyshev polynomials** (numerical analysis, polynomial approximation). They are all the same object — Gram-Schmidt applied to a different inner product.

> [!note] Exercise Index — §6B
> [[Exercise Index - §6B Orthonormal Bases]]

## §6C Orthogonal Complements and Minimization

- **[[Def - Orthogonal Complement]]**
	- The **orthogonal complement** of a subset $U \subseteq V$ is $U^\perp = \{v \in V : \langle u, v\rangle = 0 \text{ for every } u \in U\}$. It is always a subspace of $V$, even when $U$ is not. Two key examples: $\{0\}^\perp = V$, and $V^\perp = \{0\}$. The orthogonal complement is the geometric realisation of "everything perpendicular to $U$"; in $\mathbb{R}^3$ the orthogonal complement of a line through the origin is the plane through the origin perpendicular to it.

- **[[Thm - Orthogonal Decomposition]]**
	- For a finite-dimensional subspace $U$ of an inner product space $V$, $V = U \oplus U^\perp$ — every $v \in V$ has a unique decomposition $v = u + w$ with $u \in U$ and $w \in U^\perp$. Consequently $\dim U^\perp = \dim V - \dim U$ and $(U^\perp)^\perp = U$. This is the structural backbone of the chapter: an orthonormal basis of $U$ extends to one of $V$ by adjoining an orthonormal basis of $U^\perp$, and the unique decomposition is what makes orthogonal projection well-defined. In infinite dimensions the decomposition needs $U$ to be a *closed* subspace.

- **[[Def - Orthogonal Projection]]**
	- For a finite-dimensional subspace $U \subseteq V$, the **orthogonal projection** $P_U : V \to V$ sends $v$ to the unique $u \in U$ in the decomposition $v = u + w$ with $u \in U, w \in U^\perp$. It is a linear operator satisfying three defining properties: idempotency ($P_U^2 = P_U$), self-adjointness ($\langle P_U v, w\rangle = \langle v, P_U w\rangle$), and $\operatorname{range}(P_U) = U$. With any orthonormal basis $e_1, \dots, e_m$ of $U$, the formula $P_U v = \sum_k \langle v, e_k\rangle e_k$ makes the projection explicit. *True name:* an orthogonal projection is the idempotent self-adjoint operator with range $U$.

- **[[Thm - Best Approximation by Orthogonal Projection]]**
	- For a finite-dimensional subspace $U \subseteq V$ and any $v \in V$, the projection $P_U v$ is the **unique closest point in $U$ to $v$**: $\|v - P_U v\| \leq \|v - u\|$ for every $u \in U$, with equality iff $u = P_U v$. The proof is the Pythagorean theorem applied to $v - u = (v - P_U v) + (P_U v - u)$, with the first summand in $U^\perp$ and the second in $U$. This is the theorem that unifies least squares, Fourier expansion, and best polynomial approximation: each is "project a target onto a subspace".

- **[[Ex - Distance to a subspace via orthogonal projection]]** (⭐⭐)
	- Compute the distance from a vector in $\mathbb{R}^4$ to a $2$-dimensional subspace, by Gram-Schmidting a basis of the subspace and projecting.

- **[[Def - Pseudoinverse]]**
	- For $T \in \mathcal{L}(V, W)$ between finite-dimensional inner product spaces, the **[[Def - Pseudoinverse|pseudoinverse]]** (or Moore-Penrose inverse) $T^\dagger \in \mathcal{L}(W, V)$ is defined by $T^\dagger w = (T|_{(\ker T)^\perp})^{-1} P_{\operatorname{range} T} w$. It collapses to $T^{-1}$ when $T$ is invertible. Its geometric meaning: $T^\dagger w$ is the smallest-norm vector $v$ minimising $\|Tv - w\|$ — the **least-squares solution of minimum norm**. Two cornerstone identities: $T T^\dagger = P_{\operatorname{range} T}$ and $T^\dagger T = P_{(\ker T)^\perp}$.

- **[[Ex - Cauchy-Schwarz attained iff one vector is a scalar multiple of the other]]** (⭐⭐) — *appears in §6A; deepens the geometry of equality cases used in projection.*

> [!tip] Unlocked: Hilbert Projection Theorem *(from Functional Analysis)*
> The finite-dimensional best-approximation theorem extends to any closed convex subset $C$ of a Hilbert space $H$: there is a unique closest point $P_C v$ in $C$ to any $v \in H$. When $C$ is a closed subspace, $P_C$ is linear and gives the **Hilbert projection theorem**, the engine behind every duality argument in functional analysis. The **Riesz representation theorem for Hilbert spaces** $H^* \cong H$ also follows directly: every continuous linear functional on $H$ is $\langle\cdot, v\rangle$ for some unique $v$.

> [!tip] Unlocked: Least Squares *(from Linear Algebra XI)*
> The **least-squares problem** $\min_x \|Ax - b\|$ for $A \in \mathbb{R}^{m \times n}$ is solved by $x = A^\dagger b$, the [[Def - Pseudoinverse|pseudoinverse]] applied to $b$. When $A$ has linearly independent columns, the formula simplifies to $x = (A^T A)^{-1} A^T b$ (the **normal equations**), and geometrically $Ax$ is the orthogonal projection of $b$ onto the column space of $A$. See [[Linear Algebra XI — Applied II — Least Squares]] for the data-fitting, classification, and regularization applications.

> [!note] Exercise Index — §6C
> [[Exercise Index - §6C Orthogonal Complements and Projections]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

Five recurring goals exhaust nearly every exercise in inner product spaces. The first is **identifying the closest point in a subspace to a given vector** — the orthogonal-projection problem in all its guises. This is the applied-mathematics target: least squares, best polynomial approximation, Fourier truncation, denoising, and signal compression are all variants of it. The second is **proving an inequality between $\langle\cdot,\cdot\rangle$ and $\|\cdot\|$** — Cauchy-Schwarz, the triangle inequality, Bessel's inequality, the AM-QM inequality. These usually reduce to an explicit non-negative expansion of $\|\sum a_k v_k\|^2$ and discarding non-negative terms. The third is **finding or characterising an orthonormal basis** — orthogonalizing a given basis via Gram-Schmidt, computing expansion coefficients $\langle v, e_k\rangle$, or constructing a basis that diagonalises an operator (the spectral theorem in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]). The fourth is **identifying a linear functional with a vector** — Riesz representation. The fifth is **decomposing $V$ as $U \oplus U^\perp$** and using the decomposition to convert geometric statements about subspaces into algebraic statements about vectors. These five targets — closest point, inequality, orthonormal basis, Riesz representative, complement decomposition — recur because the chapter is built from one structural idea (orthogonality) and these are its five faces.

**Sources — what assumptions do we usually leverage?**

The most common is **an explicit basis of a subspace, or of $V$**, ideally one already orthonormal — the moment you have an orthonormal basis, every inner-product computation becomes a finite sum $\langle v, w\rangle = \sum v_i \overline{w_i}$, expansion coefficients are $\langle v, e_k\rangle$, and projections are sums of these. A non-orthonormal basis is converted to an orthonormal one by [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] at the cost of one orthogonalization step per basis vector. The second is **a linearity hypothesis combined with the inner product** — many proofs proceed by expanding $\|v - tw\|^2$ as a quadratic in $t$, then exploiting that a real-valued quadratic that is everywhere non-negative has non-positive discriminant; this is the engine of Cauchy-Schwarz. The third is **a minimization problem in disguise** — a target like "find the polynomial $p$ minimising $\int (f - p)^2$" routes immediately to orthogonal projection. The fourth is **a linear functional in sight** — any time a problem says "a linear functional $\varphi$ on $V$ satisfies ...", Riesz turns $\varphi$ into "take the inner product with $v$" for some specific $v$, and the problem becomes about $v$. The fifth is **a self-adjoint or idempotent operator**: idempotent self-adjoint $\Rightarrow$ orthogonal projection, and self-adjoint operators are diagonalised by orthonormal bases in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]. The routes between these are: explicit basis + minimization $\to$ Gram-Schmidt + projection; linear functional + finite dimension $\to$ Riesz; sesquilinear estimate + quadratic-in-$t$ trick $\to$ Cauchy-Schwarz; orthogonal decomposition + Pythagoras $\to$ best approximation.

---

# Legal Operations

These are the moves nearly every problem in inner product spaces routes through. A reader with no background should be able to scan this list when stuck and try each operation.

**Legal operations:**

1. **Expand $\|\alpha u + \beta v\|^2$ using sesquilinearity.** From the definition, $\|\alpha u + \beta v\|^2 = \langle \alpha u + \beta v, \alpha u + \beta v\rangle = |\alpha|^2 \|u\|^2 + \alpha\bar\beta\langle u, v\rangle + \bar\alpha\beta\langle v, u\rangle + |\beta|^2 \|v\|^2$. Almost every inequality proof, from Cauchy-Schwarz to the triangle inequality to the parallelogram law, starts by writing such an expansion and exploiting some non-negativity. *Trigger:* an inequality involving $\|\cdot\|$ and $\langle\cdot,\cdot\rangle$. *Pattern:* "expand both sides as polynomials in the scalars, use $\langle v, v\rangle \geq 0$, simplify".

2. **Orthogonalize via Gram-Schmidt.** Given any linearly independent list $v_1, \dots, v_m$, [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] produces an orthonormal list with the same span. This is the workhorse for converting any explicit basis into one that "behaves like the standard basis": expansion coefficients become inner products, the matrix of the inner product is the identity, and orthogonal projections are sums. *Trigger:* a problem that gives you a basis and asks for any inner-product computation. *Pattern:* "orthogonalize first, then compute".

3. **Project orthogonally to find the closest point.** To find the closest point in a finite-dimensional subspace $U$ to $v \in V$, compute $P_U v$. With an orthonormal basis $e_1, \dots, e_m$ of $U$, $P_U v = \sum_k \langle v, e_k\rangle e_k$. The distance is then $\|v - P_U v\| = \|v\| \cdot \sqrt{1 - \sum_k |\langle v, e_k\rangle / \|v\||^2}$ (or by directly subtracting). *Trigger:* the words "best approximation", "closest", "minimize $\|v - u\|$". *Pattern:* "build an orthonormal basis of the subspace by Gram-Schmidt, sum the projection coefficients, the residual is in $U^\perp$".

4. **Use Pythagoras to break a norm into orthogonal pieces.** Whenever $v = u + w$ with $u \perp w$, $\|v\|^2 = \|u\|^2 + \|w\|^2$. The most common deployment is when $u = P_U v$ and $w = v - P_U v$, giving $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2$. This is the abstract reason "orthogonality controls norms": orthogonal summands cannot interfere. *Trigger:* you have a decomposition with orthogonal summands. *Pattern:* "compute the squared norm of each piece, add".

5. **Apply Cauchy-Schwarz to bound a single inner product.** Whenever you need to bound $|\langle u, v\rangle|$, the immediate move is $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. This converts a bilinear quantity into a product of norms, which often are easier to bound separately. *Trigger:* a $\langle u, v\rangle$ appearing in an inequality. *Pattern:* "Cauchy-Schwarz, then bound $\|u\|$ and $\|v\|$ individually".

6. **Take the inner product with a basis vector to extract a coefficient.** If $e_1, \dots, e_n$ is an orthonormal basis and $v = \sum_k a_k e_k$, then $\langle v, e_j\rangle = a_j$. This is the orthonormal version of "read off the $j$-th coordinate" and is the basis of every expansion-coefficient computation, including Fourier coefficients. *Trigger:* you have a vector you want to expand or a sum you want to identify term-by-term. *Pattern:* "take $\langle\cdot, e_j\rangle$ of both sides".

7. **Convert a linear functional to a vector via Riesz.** Whenever a problem mentions a linear functional $\varphi$ on a finite-dimensional inner product space, [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz]] gives a unique $v$ with $\varphi(u) = \langle u, v\rangle$. This converts statements about $\varphi$ into statements about $v$. *Trigger:* "a linear functional on $V$ satisfies ...". *Pattern:* "write $\varphi(\cdot) = \langle\cdot, v\rangle$, work with $v$".

8. **Use the orthogonal decomposition $V = U \oplus U^\perp$.** When the subspace $U$ is in play, write $v = u + w$ with $u = P_U v \in U$ and $w \in U^\perp$. This breaks every problem about $V$ into a problem about $U$ and a problem about $U^\perp$, which often are independently easier. *Trigger:* a subspace $U \subseteq V$ is in sight and you want to use the geometry. *Pattern:* "decompose, deal with the two summands separately, recombine".

9. **Recognise idempotent + self-adjoint = orthogonal projection.** An operator $P \in \mathcal{L}(V)$ is an orthogonal projection onto its range if and only if $P^2 = P$ and $\langle Pu, v\rangle = \langle u, Pv\rangle$ for all $u, v$. This is the "categorical" characterisation that converts a computation about a specific projection into a structural fact about the operator class. *Trigger:* an operator $P$ satisfying $P^2 = P$ appears. *Pattern:* "check self-adjointness; if it holds, $P = P_{\operatorname{range} P}$".

10. **Use the polarization identity to recover $\langle\cdot,\cdot\rangle$ from $\|\cdot\|$.** Over $\mathbb{R}$: $\langle u, v\rangle = \tfrac{1}{4}(\|u+v\|^2 - \|u-v\|^2)$. Over $\mathbb{C}$, replace by the four-term version. This is how norm-level information feeds back into inner-product computations, and it is what makes the parallelogram law a *characterisation* of inner-product norms. *Trigger:* you have control of the norm but want to access the inner product. *Pattern:* "expand both norms, half the cross terms cancel, what survives is $\langle u, v\rangle$".

**Illegal but tempting operations:**

> [!warning] 1. Treating $\langle\cdot,\cdot\rangle$ as bilinear over $\mathbb{C}$
> Over the complex field, the inner product is **sesquilinear**, not bilinear. The slot conjugation is real: $\langle u, \lambda v\rangle = \bar\lambda \langle u, v\rangle$, not $\lambda \langle u, v\rangle$. A computation that treats both slots as linear silently makes $\langle iv, v\rangle = i\|v\|^2$ instead of the correct $-i\|v\|^2$, producing wrong answers and (worse) inner products that fail to be conjugate-symmetric. The repair condition: if the underlying field is $\mathbb{R}$, bilinearity is correct; over $\mathbb{C}$, always track conjugates. Concrete counterexample: in $\mathbb{C}$ with $\langle z, w\rangle = z\bar w$, $\langle 1, i\rangle = -i \neq i\langle 1, 1\rangle$.

> [!warning] 2. Assuming $V = U \oplus U^\perp$ in infinite dimensions without closedness
> In a finite-dimensional inner product space, every subspace $U$ satisfies $V = U \oplus U^\perp$. In a Hilbert space, the decomposition holds for **closed** [[Def - Subspace|subspaces]] only. Concrete counterexample: let $V = C[-1, 1]$ with $\langle f, g\rangle = \int fg$, and $U = \{f \in C[-1, 1] : f(0) = 0\}$. Then $U^\perp = \{0\}$ (any continuous $g$ orthogonal to every $f$ vanishing at $0$ must itself vanish on a dense set, hence everywhere), but $U \neq V$ (the constant function $1$ is not in $U$). The repair condition: $U$ must be a closed subspace. In finite dimensions every subspace is closed, so the issue does not arise — but the moment infinite dimensions enter, closedness is the missing hypothesis.

> [!warning] 3. Forming an orthogonal projection onto a non-finite-dimensional non-closed subspace
> The construction $P_U v =$ "the unique $u \in U$ with $v - u \in U^\perp$" requires the orthogonal decomposition $V = U \oplus U^\perp$, which in turn requires $U$ to be finite-dimensional (or closed in a Hilbert space). For a dense but non-closed subspace, the "projection" need not exist or need not be continuous. The repair condition: project onto the *closure* $\overline{U}$ instead.

> [!warning] 4. Concluding $P^2 = P$ alone makes $P$ an orthogonal projection
> Idempotency $P^2 = P$ only forces $P$ to be a (general, possibly oblique) projection — its range and kernel are complementary [[Def - Subspace|subspaces]], but they need not be **orthogonal**. The standard counterexample in $\mathbb{R}^2$: $P(x, y) = (x + y, 0)$ projects onto the $x$-axis along the line $y = -x$, but the $x$-axis and $y = -x$ are *not* perpendicular. The repair condition is to require both idempotency **and** self-adjointness ($\langle Pu, v\rangle = \langle u, Pv\rangle$); together these force the kernel to be the orthogonal complement of the range.

> [!warning] 5. Letting Cauchy-Schwarz be an inequality between sums rather than between norms
> A common mis-application is "(by Cauchy-Schwarz) $\sum a_k b_k \leq (\sum a_k)(\sum b_k)$", which is **false**. The correct inequality is $|\sum a_k b_k| \leq (\sum a_k^2)^{1/2} (\sum b_k^2)^{1/2}$ — the square root of *squared* sums, not the sums themselves. The repair condition: always have square roots of sums of squares on the right-hand side; otherwise you have written down a trivially false statement.

---

# Problem-Solving Strategy

The problems in inner product spaces split into five problem classes, and recognising which class you are in dictates the route to the answer.

If the problem **asks for the closest point in a subspace, or a "best approximation", or a "minimum of $\|v - u\|$ over $u \in U$"**, you are in a [[Thm - Best Approximation by Orthogonal Projection|best-approximation]] problem and the answer is $P_U v$. The route is mechanical: build an orthonormal basis $e_1, \dots, e_m$ of $U$ (by [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] if needed), and the projection is $P_U v = \sum_k \langle v, e_k\rangle e_k$. The minimum distance is $\|v - P_U v\|$, which by Pythagoras equals $\sqrt{\|v\|^2 - \|P_U v\|^2}$. This is by far the most common problem class because every applied-mathematics minimization in a vector space — least squares, polynomial approximation, signal compression — reduces to it. The non-obvious step is recognising the disguise: a question asking "what polynomial of degree $\leq 5$ best approximates $\sin x$" is asking for $P_U v$ where $U = \mathcal{P}_5$ and $v = \sin x$, but the words "projection" never appear.

If the problem **asks for an inequality between an inner product and norms**, you are most likely in a Cauchy-Schwarz application. The first move is to identify the two vectors $u, v$ and write down the Cauchy-Schwarz inequality $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. Often the problem is hidden — a sum $\sum a_k b_k$ is the inner product of $(a_1, \dots, a_n)$ and $(b_1, \dots, b_n)$; an integral $\int fg$ is the inner product in $C[a, b]$. If the inequality is not directly Cauchy-Schwarz, try the second move: expand $\|u - tv\|^2$ as a quadratic in $t$, observe that it is $\geq 0$, and exploit the discriminant. If the inequality still resists, try the third move: expand the parallelogram law or the polarization identity. The chain of triggers is: $\langle u, v\rangle$ appears in an inequality $\to$ Cauchy-Schwarz; the inequality involves $\|u + v\|, \|u - v\|, \|u\|, \|v\|$ $\to$ parallelogram law; the inequality is a refinement of triangle inequality $\to$ expand $\|u + v\|^2$ via sesquilinearity.

If the problem **asks you to construct an orthonormal basis or expand a vector in one**, you are in a Gram-Schmidt problem. The route is mechanical: take the given basis, apply Gram-Schmidt step by step, normalise each result. Once an orthonormal basis is in hand, every other question about expansion coefficients, projection coefficients, or Fourier coefficients reduces to computing $\langle v, e_k\rangle$ for various $v$. The non-obvious choice is in the inner product: a polynomial-approximation problem on $[-1, 1]$ uses $\langle f, g\rangle = \int_{-1}^1 fg$, but on $[-\pi, \pi]$ for Fourier work uses $\langle f, g\rangle = \int_{-\pi}^\pi fg$; the weight $w(x)$ in $\int fg\, w$ controls which classical orthogonal polynomials you produce.

If the problem **mentions a linear functional on a finite-dimensional inner product space**, you are in a Riesz representation problem. The route: by [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz]], $\varphi(u) = \langle u, v\rangle$ for a unique $v \in V$, which can be computed by $v = \sum_k \overline{\varphi(e_k)}\, e_k$ in any orthonormal basis. Every assertion about $\varphi$ now becomes an assertion about $v$. The non-obvious recognition: any time a problem mentions "the integral $\int_a^b f(x) g(x)\, dx$" as a function of $f$ for fixed $g$, that *is* a linear functional, and Riesz tells you what $g$ has to be.

If the problem **asks you to compute or analyse an orthogonal projection** without an obvious minimization framing, the route is to identify $U = \operatorname{range}(P)$ and check the projection-defining conditions: $P^2 = P$ and self-adjointness $\langle Pu, v\rangle = \langle u, Pv\rangle$. Once these are verified, $P = P_U$ and you may use $P_U v = \sum_k \langle v, e_k\rangle e_k$ for any orthonormal basis of $U$. Problems often disguise themselves: "show $T = P_{\operatorname{range} T}$ for some $T$" is a check of these two conditions in disguise.

The single unifying meta-question of this chapter is: **what is the closest thing in $U$ to $v$, and how does the answer change as $U$ changes?** Cauchy-Schwarz is the special case $U = \operatorname{span}(v)$ (the closest scalar multiple of $v$ to anything has the inequality as its statement). Gram-Schmidt is the iterative construction of "the closest vector in $\operatorname{span}(v_1, \dots, v_k)$ subtracted out at each step". Bessel's inequality says "the truncated expansion is the projection, so its norm is at most the full norm". Riesz says "every linear functional is, secretly, an inner-product-with-some-vector, and the vector lives in the closest one-dimensional subspace dual to $\ker\varphi$". Every named theorem in the chapter is a re-reading of "project onto a subspace".

---

# Most Reusable Properties

- **[[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz Inequality]]**: $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. This is the most-used single inequality in inner product spaces, and arguably in analysis. **Typical use:** any time you need to bound an inner product, an integral $\int fg$, a sum $\sum a_k b_k$, or a covariance — convert to a product of norms (or $L^2$-norms or standard deviations) and bound those separately. It also justifies the angle definition in $\mathbb{R}^n$ for $n \geq 4$, gives the proof of the triangle inequality, gives the correlation-coefficient bound $|\rho| \leq 1$ in statistics, and powers the proof of Bessel's inequality.

- **[[Thm - Gram-Schmidt Procedure|Gram-Schmidt Procedure]]**: turns a linearly independent list into an orthonormal one with the same partial spans. **Typical use:** whenever a problem hands you a basis that is not orthonormal and asks for any inner-product computation. After Gram-Schmidt, every inner-product computation becomes a finite sum with no cross-terms. It is also the proof of existence of orthonormal bases, the construction of classical orthogonal polynomials (Legendre, Hermite, Chebyshev, Laguerre — different inner products), and the algorithmic ingredient of the QR factorization.

- **[[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz Representation]]**: every linear functional on a finite-dimensional inner product space is "take the inner product with some vector". **Typical use:** whenever a problem mentions "the linear functional $\varphi$" or an expression of the form "the integral against $f$" — Riesz turns it into a concrete vector. It is the natural isomorphism $V \cong V'$ that the inner product provides, the proof technique behind the existence of adjoints, and the conceptual reason "linear functionals" and "vectors" become interchangeable once an inner product is fixed.

- **[[Thm - Best Approximation by Orthogonal Projection|Best Approximation]]**: $\|v - P_U v\| \leq \|v - u\|$ for all $u \in U$. **Typical use:** any minimization problem of the form "minimise $\|v - u\|$ over $u \in U$" — least squares, Fourier truncation, best polynomial approximation, denoising. It also gives the projection-as-closest-point characterisation that lets you *recognise* an orthogonal projection from the minimization property alone.

- **[[Thm - Orthogonal Decomposition|Orthogonal Decomposition]]**: $V = U \oplus U^\perp$ for any finite-dimensional subspace $U$. **Typical use:** every time you want to use the geometry of "the part in $U$" and "the part orthogonal to $U$" separately. It underlies the existence of orthogonal projections, the rank-nullity theorem in inner product form, the spectral theorem, and the QR factorization.

---

# Bridges

1. **Hilbert space — the infinite-dimensional generalization (Functional Analysis).** A Hilbert space is an inner product space that is **complete** in the induced metric. Lebesgue $L^2(X, \mu)$ is the canonical example: the space of equivalence classes of measurable functions with $\int |f|^2\, d\mu < \infty$, equipped with $\langle f, g\rangle = \int f \bar g\, d\mu$. Almost every theorem in this chapter generalises with one caveat: the orthogonal decomposition $V = U \oplus U^\perp$ holds for **closed** subspaces $U$, not arbitrary ones. With that caveat in place, Riesz representation extends (the **Riesz representation theorem for Hilbert spaces** $H^* \cong H$), Gram-Schmidt extends to countable orthonormal sequences, the best-approximation theorem extends to closed convex subsets (the **Hilbert projection theorem**), and Bessel's inequality + completeness gives convergence of orthonormal expansions in $L^2$. Modern quantum mechanics is a theory of vectors in Hilbert space — states are unit vectors, observables are self-adjoint operators, time evolution is unitary.

2. **Lebesgue $L^2$ — the prototypical Hilbert space (Analysis).** Take a measure space $(X, \mu)$ and form $L^2(X, \mu) = \{f : \int |f|^2\, d\mu < \infty\} / \sim$ where two functions are identified if they differ on a $\mu$-null set. With $\langle f, g\rangle = \int f \bar g\, d\mu$, $L^2$ is a Hilbert space. The orthonormal expansions of $L^2[-\pi, \pi]$ in $\{e^{inx}/\sqrt{2\pi}\}$ *are* Fourier series; the orthonormal expansions of $L^2(\mathbb{R}, e^{-x^2/2}\, dx)$ in Hermite polynomials are the spectral decomposition of the quantum harmonic oscillator. The bridge from this chapter is exact: finite-dimensional inner-product-space theorems become $L^2$ theorems by replacing finite sums with integrals and finite bases with orthonormal sequences.

3. **Fourier series — orthonormal-basis expansion in $L^2[-\pi, \pi]$ (Analysis).** A Fourier series $f(x) = \sum_n c_n e^{inx}$ with $c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f(x) e^{-inx}\, dx$ is exactly the orthonormal expansion of $f$ in the basis $\{e^{inx}/\sqrt{2\pi}\}_{n \in \mathbb{Z}}$ of $L^2[-\pi, \pi]$, and the formula for $c_n$ is "$c_n = \langle f, e_n\rangle$" applied to that basis. **Bessel's inequality** $\sum |c_n|^2 \leq \|f\|_2^2$ is the infinite-dimensional Pythagorean theorem in inequality form; **Parseval's identity** $\sum |c_n|^2 = \|f\|_2^2$ is its equality version (which holds because the trigonometric basis is *complete*). The truncated series $\sum_{|n| \leq N} c_n e^{inx}$ is the orthogonal projection of $f$ onto the $(2N+1)$-dimensional subspace of trigonometric polynomials of degree $\leq N$, and the **best-approximation theorem** says this truncation minimises $\int |f - P|^2$ over all such $P$.

4. **[[Def - Minkowski Space and the Metric|Minkowski Space]] — an indefinite bilinear form (Special Relativity).** Minkowski space $\mathbb{R}^4$ with $\langle x, y\rangle = -x^0 y^0 + x^1 y^1 + x^2 y^2 + x^3 y^3$ is not an inner product space — the form is **indefinite**, not positive-definite, so the "norm-squared" can be negative (timelike vectors) or zero on nonzero vectors (lightlike vectors). The signature is the entire structural difference: many formal manipulations carry over, including the polarization identity and the **reverse triangle inequality** for timelike vectors (the twin paradox is a triangle-inequality statement in the indefinite metric, with the direction flipped). The signature $(-, +, +, +)$ used here is the "particle physics" convention; the $(+, -, -, -)$ convention is also common, and the two are interconverted by negating the metric. Special relativity is, in this language, "the geometry you get when you replace the inner product by an indefinite form of signature $(1, 3)$".

5. **Statistical correlation and covariance (Probability and Statistics).** The covariance $\operatorname{Cov}(X, Y) = E[(X - EX)(Y - EY)]$ is the inner product on the space of mean-zero finite-variance random variables (modulo equivalence by almost-everywhere equality). The variance $\operatorname{Var}(X) = \operatorname{Cov}(X, X) = \|X - EX\|^2$ is the squared norm. The **correlation coefficient** $\rho(X, Y) = \operatorname{Cov}(X, Y) / (\sigma_X \sigma_Y) = \cos\theta$ is the cosine of the angle between $X - EX$ and $Y - EY$ in this inner product space, and the fact $|\rho| \leq 1$ is **exactly** Cauchy-Schwarz. The orthogonal projection of $Y$ onto $\operatorname{span}(1, X)$ is the **best linear predictor** of $Y$ given $X$, which is the **linear regression** formula; least-squares regression is an inner-product-space minimization in disguise.

---

# Insights

**The unifying frame: an inner product gives a vector space three things at once — length, angle, and a canonical isomorphism with its dual.** It is tempting to think of an inner product as just "a way to compute dot products". The productive viewpoint is that it is the structure that lets a vector space carry geometry in the same way that a metric lets a set carry topology. The single bilinear (sesquilinear) form generates: (i) a **norm** $\|v\| = \sqrt{\langle v, v\rangle}$, hence a **metric** $d(u, v) = \|u - v\|$, hence a topology and notion of convergence; (ii) an **angle** $\theta = \arccos\bigl(\langle u, v\rangle / (\|u\|\,\|v\|)\bigr)$, hence orthogonality, projections, and right angles; and (iii) an **identification** $V \cong V'$ via Riesz, which makes linear functionals and vectors interchangeable. Each downstream theorem of the chapter is a consequence of one or more of these three. Whenever you study an inner product space, ask three questions: what does the norm say, what does the angle say, and what does the Riesz isomorphism say.

**The true name of an orthonormal basis: a basis in which the matrix of the inner product is the identity.** The textbook definition — "pairwise orthogonal and each of norm $1$" — is the right thing to check but the wrong thing to think. What an orthonormal basis is *for* is making computations clean. In an orthonormal basis $e_1, \dots, e_n$, the inner product $\langle v, w\rangle = \sum v_k \overline{w_k}$ is just the Euclidean dot product on coordinates; expansion coefficients are inner products $v = \sum \langle v, e_k\rangle e_k$; projection onto $U = \operatorname{span}(e_1, \dots, e_m)$ is $P_U v = \sum_{k \leq m} \langle v, e_k\rangle e_k$; and the Pythagorean theorem gives $\|v\|^2 = \sum |\langle v, e_k\rangle|^2$. Every computation in the chapter that is *cheap* is cheap because of orthonormality. When stuck, the first instinct should be "do I have an orthonormal basis here? If not, Gram-Schmidt one."

**Trigger-reaction patterns specific to this chapter.** *See a minimization problem in a vector space ("closest", "best fit", "smallest residual")* $\to$ reach for [[Thm - Best Approximation by Orthogonal Projection|orthogonal projection]]. *See a basis you want clean inner-product behaviour from* $\to$ [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] it. *See a linear functional on a finite-dimensional inner product space* $\to$ apply [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz]] to convert it into a vector. *See an inequality between an inner product and norms* $\to$ try [[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz]] first, then the parallelogram law, then expanding $\|u - tv\|^2$ as a quadratic in $t$. *See an idempotent operator* $\to$ check self-adjointness; if it holds, it is an [[Def - Orthogonal Projection|orthogonal projection]]. *See a sum $\sum a_k b_k$* $\to$ recognise it as the inner product of $(a_1, \dots, a_n)$ and $(b_1, \dots, b_n)$, opening the door to Cauchy-Schwarz.

**Inheritance: every property in this chapter is inherited from the field's order or absolute value.** Positivity of $\langle v, v\rangle$ comes from positivity in $\mathbb{R}$ (or $|z|^2 \geq 0$ in $\mathbb{C}$). The triangle inequality comes from the triangle inequality on $\mathbb{R}_{\geq 0}$. Conjugate-symmetry comes from the conjugation involution on $\mathbb{C}$. Whenever you wonder "where is this property *actually* coming from", the answer is "the underlying field". This is also why generalizing to a field without an absolute value (a finite field, say) breaks everything — there is no notion of "positive" for $\langle v, v\rangle$ to be, so an "inner product" over $\mathbb{F}_p$ has to be redefined from scratch (as a non-degenerate bilinear form, dropping positivity), and the geometric intuition fails.

**The categorical view of orthogonal projection.** An orthogonal projection $P_U$ is characterised by three properties: (i) idempotency $P_U^2 = P_U$ (it is a projection), (ii) self-adjointness $\langle P_U u, v\rangle = \langle u, P_U v\rangle$ (which forces $\ker P_U = (\operatorname{range} P_U)^\perp$), and (iii) $\operatorname{range}(P_U) = U$. The first two together encode "orthogonal projection onto *something*"; the third pins down *what*. This characterisation upgrades projections from "constructed objects" to "operators satisfying these three axioms", and matches the more general definition that surfaces in Hilbert space theory and von Neumann algebra theory. From this viewpoint, $P_U \mapsto U$ is a bijection between orthogonal projections in $\mathcal{L}(V)$ and (closed) subspaces of $V$, and the lattice of subspaces of $V$ is canonically the lattice of orthogonal projections — a fact that is the start of the geometry of operator algebras.
