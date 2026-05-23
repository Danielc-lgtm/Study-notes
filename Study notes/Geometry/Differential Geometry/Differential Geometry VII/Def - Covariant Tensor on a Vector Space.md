---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Multilinear Form"
  - "Def - Bilinear Form"
  - "Def - Tensor Product of Vector Spaces"
  - "Def - Dual Space"
  - "Def - Dual Basis"
tags: [geometry, differential-geometry, multilinear-algebra]
---

# Notation

$V$ is a finite-dimensional real vector space of dimension $n$. $V^*$ is its [[Def - Dual Space|dual space]], the space of linear functionals $V \to \mathbb{R}$. $(E_i)_{i=1}^n$ is a basis of $V$; $(\varepsilon^j)_{j=1}^n$ is the [[Def - Dual Basis|dual basis]] of $V^*$, characterized by $\varepsilon^j(E_i) = \delta^j_i$. The space of covariant $k$-tensors on $V$ is denoted $T^k(V^*)$, following Lee. Einstein summation is in force: a repeated upper-and-lower index pair is summed. The full notation registry sits on [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

The object we want to axiomatize is **a function that eats $k$ vectors and produces a number, linearly in each input separately**. The motivating examples are the inner product $\langle v, w \rangle$ on a real vector space (a function of two vectors, linear in each), the determinant $\det(v_1, \dots, v_n)$ of $n$ vectors in $\mathbb{R}^n$ (a function of $n$ vectors, linear in each), and the evaluation $\omega(v)$ of a linear functional on a vector (a function of one vector, linear in it). All three share the feature that each input slot is linear when the others are held fixed, and the output is a number. The covariant-$k$-tensor axioms write this down and nothing more, so that any theorem about covariant $k$-tensors applies to all three at once.

The single axiom is **multilinearity** — linearity in each input separately. The reason to demand this exact axiom and not a stronger one is best seen by contrast. The strictly stronger axiom is *joint* linearity in $V \times \cdots \times V$ — treating the $k$-tuple as a vector in $V \oplus \cdots \oplus V$ — but joint linearity forces $\alpha(\lambda v, \dots, \lambda v) = \lambda \alpha(v, \dots, v)$, whereas multilinearity forces $\alpha(\lambda v, \dots, \lambda v) = \lambda^k \alpha(v, \dots, v)$. The $\lambda^k$ scaling is what makes covariant tensors describe *polynomial* quantities of degree $k$ (the inner product gives $\|v\|^2$ when both arguments are $v$, the determinant gives $\det V$ when the columns are the columns of a matrix $V$). Joint linearity would force degree 1 behaviour, and we would lose the central examples. Multilinearity is the unique axiom that keeps the degree-$k$ polynomial character.

One could ask whether to *strengthen* multilinearity by demanding symmetry $\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = \alpha(v_1, \dots, v_k)$ for every permutation $\sigma$. This gives the subclass of [[Def - Symmetric Tensor Field|symmetric tensors]] $\Sigma^k(V^*)$. The reason not to bake symmetry into the covariant-tensor definition is the same as for [[Def - Bilinear Form|bilinear forms]]: it would exclude examples we genuinely want — the determinant is alternating, not symmetric, and pairings like $u^\top M v$ for non-symmetric $M$ are bilinear but not symmetric. Similarly, demanding alternation $\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\operatorname{sgn}\sigma)\,\alpha(v_1,\dots,v_k)$ would give the [[Def - Alternating Multilinear Form|alternating multilinear forms]] $\Lambda^k(V^*)$, also a useful subclass. Symmetric and alternating tensors are extra structure imposed on top of multilinearity; multilinearity itself is the *bare* notion from which both branch.

One could also ask whether to weaken the axiom by allowing the values to live in a vector space $U$ rather than $\mathbb{R}$. This gives **multilinear maps** $V^k \to U$, a strictly more general notion. The reason for fixing the codomain at $\mathbb{R}$ is that the universal property of the tensor product $V^{\otimes k}$ already converts general multilinear maps into linear maps on $V^{\otimes k}$, so the $U$-valued case reduces to the scalar-valued case after one application of the universal property. The scalar-valued case is the "primary" definition, and a covariant $k$-tensor *is* a scalar-valued multilinear map by definition.

The choice of using $k$ copies of *the same* space $V$ (rather than $k$ different spaces $V_1, \dots, V_k$) is what makes the tensor a "tensor on $V$". The more general notion of a multilinear map $V_1 \times \cdots \times V_k \to \mathbb{R}$ — an element of $V_1^* \otimes \cdots \otimes V_k^*$ — is sometimes useful (in the universal property of the tensor product), but the standard usage in differential geometry takes a single space $V = T_pM$ and builds all tensors from it. When you later see a contravariant tensor, it lives in $V \otimes \cdots \otimes V$; when you see a mixed tensor, in a tensor product of copies of $V$ and copies of $V^*$. The single-space convention is what makes the type $(k, \ell)$ a well-defined invariant.

A test of having understood the definition: can you invent the **components**? Given a basis $(E_i)$ and dual basis $(\varepsilon^j)$, multilinearity says $\alpha$ is determined by its values $\alpha_{i_1\cdots i_k} := \alpha(E_{i_1}, \dots, E_{i_k})$ on the $n^k$ tuples of basis vectors. The expansion $\alpha = \alpha_{i_1\cdots i_k}\, \varepsilon^{i_1}\otimes\cdots\otimes \varepsilon^{i_k}$ then expresses $\alpha$ as a linear combination of tensor products of dual basis elements, with the components $\alpha_{i_1\cdots i_k}$ as coefficients. The reason it works is multilinearity: every tensor is determined by its values on basis tuples, and the products $\varepsilon^{i_1}\otimes\cdots\otimes\varepsilon^{i_k}$ form a basis of $T^k(V^*)$ — they take the value $1$ at $(E_{i_1}, \dots, E_{i_k})$ and $0$ at every other tuple of basis vectors.

---

# The Definition

A **covariant $k$-tensor** on a finite-dimensional real vector space $V$ is a function $\alpha : V \times \cdots \times V \to \mathbb{R}$ ($k$ copies of $V$) that is **linear in each slot when the other slots are held fixed**. Explicitly, for $1 \leq i \leq k$, for all vectors $v_1, \dots, v_k, v'_i \in V$ and all scalars $a, a' \in \mathbb{R}$:

$$\alpha(v_1, \dots, av_i + a'v'_i, \dots, v_k) = a\,\alpha(v_1, \dots, v_i, \dots, v_k) + a'\,\alpha(v_1, \dots, v'_i, \dots, v_k).$$

The space of all covariant $k$-tensors on $V$ is denoted $T^k(V^*)$. It is itself a vector space under pointwise addition and scalar multiplication.

**The number $k$** is called the **rank** (or order) of the tensor. By convention, $T^0(V^*) = \mathbb{R}$ (real numbers are covariant 0-tensors). The case $k = 1$ recovers $T^1(V^*) = V^*$, linear functionals on $V$. The case $k = 2$ recovers [[Def - Bilinear Form|bilinear forms]] on $V$.

**Components.** Given a basis $(E_1, \dots, E_n)$ of $V$ with dual basis $(\varepsilon^1, \dots, \varepsilon^n)$ of $V^*$, the **components** of $\alpha$ in this basis are the $n^k$ real numbers

$$\alpha_{i_1\cdots i_k} := \alpha(E_{i_1}, \dots, E_{i_k}), \qquad 1 \leq i_1, \dots, i_k \leq n.$$

These components determine $\alpha$ uniquely: for any vectors $v_j = v_j^{i_j} E_{i_j}$,

$$\alpha(v_1, \dots, v_k) = \alpha_{i_1\cdots i_k}\, v_1^{i_1} \cdots v_k^{i_k}$$

(Einstein summation over each $i_j$). Equivalently, $\alpha$ has the expansion in the **basis-induced basis of $T^k(V^*)$**:

$$\alpha = \alpha_{i_1\cdots i_k}\, \varepsilon^{i_1} \otimes \cdots \otimes \varepsilon^{i_k},$$

where $\varepsilon^{i_1}\otimes\cdots\otimes\varepsilon^{i_k} \in T^k(V^*)$ is the covariant $k$-tensor sending $(v_1, \dots, v_k)$ to $\varepsilon^{i_1}(v_1)\cdots\varepsilon^{i_k}(v_k) = v_1^{i_1}\cdots v_k^{i_k}$.

**Identification with the tensor product.** Via the [[Thm - Universal Property of the Tensor Product|universal property]],

$$T^k(V^*) \cong V^* \otimes V^* \otimes \cdots \otimes V^* \quad (k\text{ factors}),$$

with the elementary tensor $\omega^1 \otimes \cdots \otimes \omega^k$ in $V^{*\otimes k}$ corresponding to the multilinear functional $(v_1, \dots, v_k) \mapsto \omega^1(v_1)\cdots\omega^k(v_k)$. This canonical identification is the bridge to all multilinear-algebra machinery from [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]].

**Dimension.** $\dim T^k(V^*) = n^k$, with basis $\{\varepsilon^{i_1}\otimes\cdots\otimes\varepsilon^{i_k} : 1 \leq i_1, \dots, i_k \leq n\}$ of $n^k$ elements.

---

# Categorical / Structural Definition

The categorical definition of a covariant $k$-tensor uses the [[Thm - Universal Property of the Tensor Product|universal property of the tensor product]].

**A covariant $k$-tensor on $V$ is a linear functional on $V^{\otimes k}$.** The universal property of the tensor product asserts a natural bijection

$$\{\text{multilinear maps } V^k \to \mathbb{R}\} \;\cong\; \mathcal{L}(V^{\otimes k}, \mathbb{R}) = (V^{\otimes k})^*,$$

sending a multilinear $\alpha$ to the unique linear $\hat\alpha : V^{\otimes k} \to \mathbb{R}$ with $\hat\alpha(v_1 \otimes \cdots \otimes v_k) = \alpha(v_1, \dots, v_k)$. So the space $T^k(V^*)$ of covariant $k$-tensors is canonically isomorphic to the dual of $V^{\otimes k}$, and in turn to $(V^*)^{\otimes k}$ in finite [[Def - Dimension|dimensions]] (using $(A \otimes B)^* \cong A^* \otimes B^*$ for finite-dimensional spaces). The three descriptions — multilinear functional, linear functional on $V^{\otimes k}$, element of $(V^*)^{\otimes k}$ — are the *same* object viewed three ways.

**Functoriality.** A linear map $L : V \to W$ induces, by precomposition, a *covariant* (in the sense of category theory) map $L^* : T^k(W^*) \to T^k(V^*)$ given by $(L^*\beta)(v_1, \dots, v_k) := \beta(Lv_1, \dots, Lv_k)$. (Note: the *category-theoretic* "covariance" of this map is the *opposite* of the geometric sense — it goes $W \to V$ when $L$ goes $V \to W$. The terminological clash is the reason the geometric word "covariant" is so often confusing.) This is the algebraic shadow of the pullback operation on covariant tensor fields.

---

# Relate to Other Fields / Compression

A covariant $k$-tensor is the natural multilinear generalization of a [[Def - Bilinear Form|bilinear form]]. The case $k = 1$ recovers the [[Def - Dual Space|dual space]] $V^*$; the case $k = 2$ recovers bilinear forms; for general $k$ it is the [[Def - Multilinear Form|multilinear form]] of [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]] read with a covariance-tracking convention. The renaming from "multilinear form" to "covariant tensor" reflects a deliberate emphasis: in the manifold context, covariant tensors will pair with vectors (which are contravariant), and the up-down distinction will become operationally important.

From the geometry side, a covariant $k$-tensor on $T_pM$ is the algebraic ingredient of a covariant $k$-tensor field on $M$ at the point $p$. The metric tensor is a covariant 2-tensor at each point; the symplectic form on a symplectic manifold is an alternating covariant 2-tensor at each point; the volume form on an oriented Riemannian manifold is an alternating covariant $n$-tensor at each point.

**True name:** A covariant $k$-tensor is **the universal recipient of $k$-tuples of vectors that linearizes each slot**. Operationally, the test is the multilinearity check: fix all-but-one slot, the remaining slot should be linear in its input.

---

# Examples / Corollaries

**Is an instance: a linear functional $\omega \in V^*$ is a covariant 1-tensor.** It eats one vector and produces a number, linearly. Conversely, every covariant 1-tensor is a linear functional. So $T^1(V^*) = V^*$.

**Is an instance: a [[Def - Bilinear Form|bilinear form]] $\beta : V \times V \to \mathbb{R}$ is a covariant 2-tensor.** Bilinearity is exactly multilinearity for $k = 2$. So $T^2(V^*)$ is the space of bilinear forms. The dot product, the Minkowski metric $\eta(v,w) = -v^0 w^0 + v^1 w^1 + v^2 w^2 + v^3 w^3$, and the form $\beta(v, w) = v^\top M w$ for any $n \times n$ matrix $M$ are all instances.

**Is an instance: the determinant $\det(v_1, \dots, v_n)$ on $\mathbb{R}^n$.** Viewed as a function of $n$ vectors (the columns of an $n \times n$ matrix), the determinant is multilinear, hence a covariant $n$-tensor on $\mathbb{R}^n$. It is moreover alternating. The fact that $T^n(\mathbb{R}^{n*}) \supseteq \Lambda^n(\mathbb{R}^{n*})$ has dimension at least 1, combined with $\dim \Lambda^n(\mathbb{R}^{n*}) = \binom{n}{n} = 1$, shows that *every* alternating covariant $n$-tensor on $\mathbb{R}^n$ is a scalar multiple of $\det$. This is the algebraic basis of the [[Def - Volume Form|volume form]] in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

**Is an instance: the elementary tensor $\varepsilon^i \otimes \varepsilon^j$ on $V$.** Defined by $(\varepsilon^i \otimes \varepsilon^j)(v, w) = v^i w^j$. This is a covariant 2-tensor, and the $n^2$ such tensors form a basis of $T^2(V^*)$. Note that $\varepsilon^i \otimes \varepsilon^j \neq \varepsilon^j \otimes \varepsilon^i$ in general (they take different values when $v \neq w$), so the tensor product on covectors is **not commutative**.

**Is NOT an instance: $\alpha(v, w) = \|v\| \cdot \|w\|$.** This is *not* a bilinear form, hence not a covariant 2-tensor: $\alpha(2v, w) = 2\|v\|\,\|w\| = 2\alpha(v,w)$ when both inputs are positively scaled, but $\alpha(-v, w) = \|v\|\,\|w\| = \alpha(v, w)$ rather than $-\alpha(v, w)$ as bilinearity would demand. The norm is not linear in its argument; it is *seminorm-linear*, which is a strictly weaker property.

**Is NOT an instance: $\alpha(v, w) = \langle v, w\rangle^2$.** This is *quadratic* in each slot, not linear: $\alpha(2v, w) = 4\langle v, w\rangle^2 = 4\alpha(v, w)$, not $2\alpha(v, w)$. So it fails multilinearity. Squaring an inner product produces a degree-4 polynomial, not a covariant 2-tensor.

**Corollary (dimension).** $\dim T^k(V^*) = n^k$, where $n = \dim V$. *Proof:* the basis $\{\varepsilon^{i_1}\otimes\cdots\otimes\varepsilon^{i_k}\}$ has $n^k$ elements; linear independence is a direct evaluation argument (evaluate a linear combination at $(E_{j_1}, \dots, E_{j_k})$ and read off coefficients).

**Corollary (components determine the tensor).** Two covariant $k$-tensors $\alpha, \alpha'$ on $V$ are equal if and only if they have the same components in some (equivalently every) basis. This is multilinearity: a tensor is determined by its values on basis tuples.

**Corollary (the tensor product is multilinear in its arguments).** The operation $(\omega^1, \dots, \omega^k) \mapsto \omega^1 \otimes \cdots \otimes \omega^k$, viewed as a function $V^* \times \cdots \times V^* \to T^k(V^*)$, is itself multilinear: $\omega^1 \otimes \cdots \otimes (a\omega^i + b\tilde\omega^i) \otimes \cdots \otimes \omega^k = a\,\omega^1\otimes\cdots\otimes\omega^k + b\,\omega^1\otimes\cdots\otimes\tilde\omega^i\otimes\cdots\otimes\omega^k$.

**Calibration check.** If you have understood the definition, you should be able to: (i) compute the components of the bilinear form $\beta(v, w) = v^\top M w$ on $\mathbb{R}^n$ in the standard basis and find they equal $M_{ij}$; (ii) verify that the elementary tensors $\varepsilon^i\otimes\varepsilon^j\otimes\varepsilon^k$ are linearly independent in $T^3(V^*)$ for $\dim V \geq 2$ (the $n^3$ values at $(E_a, E_b, E_c)$ form an $n^3 \times n^3$ permutation matrix); (iii) verify that on $V = \mathbb{R}^2$, the bilinear form $\alpha(v, w) = v^1 w^2 - v^2 w^1$ is alternating, hence the element of $\Lambda^2(V^*)$ that the determinant equals up to a sign.

---

# Unlocked by This

> [!tip] Covariant Tensor Field on a Manifold *(from [[Differential Geometry VII — Tensors and Tensor Fields]])*
> A smoothly varying assignment of a covariant $k$-tensor to each tangent space of a manifold. See [[Def - Tensor Field on a Manifold]]. The metric tensor, the Riemann curvature, the stress tensor are all instances. The whole machinery of tensor analysis on manifolds is this fibrewise construction patched together smoothly.

> [!tip] Riemannian Metric *(from Riemannian Geometry)*
> A **Riemannian metric** is a covariant 2-tensor field on $M$ that is symmetric and positive definite at every point. The fibre-level structure (symmetric, positive-definite bilinear form) is exactly the inner-product structure of [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]], applied tangent-space-by-tangent-space. The covariant-tensor language is what makes the metric a *coordinate-invariant* object.

> [!tip] Differential k-Form *(from [[Differential Geometry VIII — Differential Forms]])*
> An **alternating** covariant $k$-tensor field. Differential forms are the subset of covariant tensor fields with antisymmetric components, and they support extra operations — wedge product, exterior derivative, integration — that have no analogue for general covariant tensors.

> [!tip] Symplectic Form *(from Symplectic Geometry)*
> A **closed, nondegenerate** alternating covariant 2-tensor field $\omega$ on a $2n$-manifold. The fibre at each point is an alternating bilinear form, with the nondegeneracy condition that $\omega^n$ is a nonzero $2n$-form (volume). Symplectic forms are the geometric structure underlying Hamiltonian mechanics: position and momentum live in a symplectic phase space.
