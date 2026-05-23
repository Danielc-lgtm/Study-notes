---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Dual Space"
  - "Def - Dual Basis"
  - "Def - Tensor Product of Vector Spaces"
tags: [geometry, differential-geometry, multilinear-algebra]
---

# Notation

$V$ is a finite-dimensional real vector space of dimension $n$, with [[Def - Dual Space|dual]] $V^*$. $(E_i)$ is a basis of $V$ with [[Def - Dual Basis|dual basis]] $(\varepsilon^j)$ of $V^*$, $\varepsilon^j(E_i) = \delta^j_i$. The space of contravariant $k$-tensors on $V$ is denoted $T^k(V)$, paralleling the covariant notation $T^k(V^*)$ from [[Def - Covariant Tensor on a Vector Space]]. Components of a contravariant tensor sit with **upper indices**: $T^{i_1\cdots i_k}$. Einstein summation is in force. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

The motivation is the **dual** of the covariant case. There, we wanted a multilinear gadget eating vectors; here, we want a multilinear gadget eating *covectors* — linear functionals on $V$. The reason we need it: many objects in differential geometry (the inverse metric $g^{ij}$, a multi-vector $v_1 \wedge v_2$, the contravariant components of the Riemann curvature) are naturally functionals of covectors rather than of vectors. We need a name for this kind of object and a notation that keeps it distinct from the covariant case.

The single axiom is again multilinearity, applied to covector arguments: $T(\omega^1, \dots, \omega^k)$ is linear in each $\omega^i$ when the others are held fixed. Everything in the [[Def - Covariant Tensor on a Vector Space#Axiom Motivation|axiom motivation for covariant tensors]] applies verbatim with "covector" in place of "vector". The novelty is the use of the **canonical double-dual identification** $V \cong V^{**}$, which holds for finite-dimensional spaces and lets us identify $V$ itself with the space of linear functionals on $V^*$: a vector $v \in V$ acts on a covector $\omega \in V^*$ by $v(\omega) := \omega(v)$.

This identification is the reason we can write the elementary contravariant tensors as $v_1 \otimes \cdots \otimes v_k$ with $v_i \in V$, rather than as functionals on $V^{*k}$ explicitly: under the double-dual identification, $v_1 \otimes \cdots \otimes v_k$ acts on $(\omega^1, \dots, \omega^k)$ by $\omega^1(v_1)\cdots\omega^k(v_k)$, the same combinatorial expression as in the covariant case but with the roles of vectors and covectors swapped.

The finite-dimensionality assumption is *load-bearing* here. In infinite [[Def - Dimension|dimensions]], the canonical injection $V \to V^{**}$ is not generally surjective: there are linear functionals on $V^*$ that do not come from vectors of $V$. The double-dual identification fails, and the "$V$ as functionals on $V^*$" definition produces a strictly larger space than $V \otimes \cdots \otimes V$. For differential geometry, where the tangent spaces are finite-dimensional, this complication does not arise — we always have $\dim V = \dim V^*$ and the identification is canonical. But the reader should remember: contravariant tensors are *bare* tensor-product elements $v_1 \otimes \cdots \otimes v_k$, and identifying them with functionals on $V^{*k}$ is a finite-dimensional convenience, not a definition.

One could ask why we treat covariant and contravariant tensors as different objects rather than identifying them via the double-dual. The structural reason is that, in differential geometry, the natural maps are *different*: a smooth map $F : M \to N$ induces $dF : T_pM \to T_{F(p)}N$ pushing tangent vectors *forward*, and a dual map $dF^*$ on covectors pulling them *backward*. As a result, covariant tensors **pull back** under $F$ (universally, no assumption on $F$), while contravariant tensors **push forward** (and only when $F$ is a [[Def - Diffeomorphism|diffeomorphism]] do they have a well-defined pullback). The covariant/contravariant distinction is the distinction between "pulls back" and "pushes forward", and it is genuine: identifying $V$ with $V^{**}$ algebraically does not bridge this functorial distinction. Keeping the variances separate is what makes index gymnastics work — and what makes the transformation rule [[Thm - Transformation Rule for Tensor Components|distinguish upper and lower indices]].

---

# The Definition

A **contravariant $k$-tensor** on a finite-dimensional real vector space $V$ is a function $T : V^* \times \cdots \times V^* \to \mathbb{R}$ ($k$ copies of $V^*$) that is **linear in each slot when the other slots are held fixed**. Explicitly, for $1 \leq i \leq k$, for all covectors $\omega^1, \dots, \omega^k, \tilde\omega^i \in V^*$ and scalars $a, a' \in \mathbb{R}$:

$$T(\omega^1, \dots, a\omega^i + a'\tilde\omega^i, \dots, \omega^k) = a\,T(\omega^1, \dots, \omega^i, \dots, \omega^k) + a'\,T(\omega^1, \dots, \tilde\omega^i, \dots, \omega^k).$$

The space of contravariant $k$-tensors on $V$ is denoted $T^k(V)$. It is a vector space under pointwise operations.

**Identification with the tensor product.** In finite dimensions, the canonical double-dual identification $V \cong V^{**}$ gives

$$T^k(V) \cong V \otimes V \otimes \cdots \otimes V \quad (k\text{ factors}),$$

with the elementary tensor $v_1 \otimes \cdots \otimes v_k$ corresponding to the multilinear functional $(\omega^1, \dots, \omega^k) \mapsto \omega^1(v_1)\cdots\omega^k(v_k)$.

By convention, $T^0(V) = \mathbb{R}$ and $T^1(V) = V$ (every contravariant 1-tensor is a vector).

**Components.** Given a basis $(E_i)$ with dual basis $(\varepsilon^j)$, the **components** of $T$ in this basis are

$$T^{i_1\cdots i_k} := T(\varepsilon^{i_1}, \dots, \varepsilon^{i_k}), \qquad 1 \leq i_1, \dots, i_k \leq n,$$

with **upper indices** to mark contravariance. The expansion in the basis-induced basis of $T^k(V)$ is

$$T = T^{i_1\cdots i_k}\, E_{i_1} \otimes \cdots \otimes E_{i_k},$$

with the basis $\{E_{i_1}\otimes\cdots\otimes E_{i_k}\}$ of $T^k(V)$ consisting of $n^k$ elementary tensor products of basis vectors.

**Dimension.** $\dim T^k(V) = n^k$.

---

# Categorical / Structural Definition

The categorical content parallels [[Def - Covariant Tensor on a Vector Space#Categorical / Structural Definition|the covariant case]] with $V$ and $V^*$ swapped. The universal property of the tensor product gives natural [[Def - Isomorphism|isomorphisms]]

$$T^k(V) \cong (V^*)^{\otimes k\,*} \cong V^{\otimes k} \quad \text{(finite-dimensional)},$$

where the second isomorphism uses $V^{**} \cong V$.

**Functoriality.** A linear map $L : V \to W$ induces — *covariantly* in $L$ — a map $L_* : T^k(V) \to T^k(W)$ by $(L_*T)(\omega^1, \dots, \omega^k) := T(L^*\omega^1, \dots, L^*\omega^k)$, where $L^* : W^* \to V^*$ is the dual map. On elementary tensors, $L_*(v_1 \otimes \cdots \otimes v_k) = Lv_1 \otimes \cdots \otimes Lv_k$. This is the algebraic shadow of the *pushforward* of contravariant tensor fields, which exists in the manifold setting only when $F$ is a diffeomorphism.

The contrast with the covariant case is exact: covariant tensors are *contravariant* functors (linear maps go backwards), contravariant tensors are *covariant* functors (linear maps go forwards). The standard tensor-analysis terminology is the *opposite* of the category-theoretic terminology, which is the deepest source of confusion in tensor analysis.

---

# Relate to Other Fields / Compression

A contravariant $k$-tensor is to a covariant $k$-tensor what $V$ is to $V^*$: the **dual** notion. Where a covariant tensor eats vectors and produces scalars, a contravariant tensor eats covectors and produces scalars. The two are interconvertible whenever $V$ has an inner product (a [[Def - Riemannian Metric|metric]], in the manifold setting): the inner product gives an isomorphism $V \cong V^*$, called the **musical isomorphism** in differential geometry, and this can be used to "raise" or "lower" indices, converting between covariant and contravariant tensor types.

From the LA IX viewpoint, contravariant $k$-tensors on $V$ are exactly elements of $V^{\otimes k}$, the [[Def - Tensor Product of Vector Spaces|tensor product]] of $k$ copies of $V$. The space $V^{\otimes k}$ was constructed in LA IX as an abstract universal recipient of multilinear maps, and the contravariant-$k$-tensor language is the *application* of that construction to $V$ itself.

**True name:** A contravariant $k$-tensor on $V$ is **an element of $V^{\otimes k}$**, equivalently **a multilinear functional on $V^{*k}$**. In finite dimensions the two are canonically the same. Operationally: contravariant tensors carry upper indices, pair with covectors, push forward under linear maps.

---

# Examples / Corollaries

**Is an instance: a vector $v \in V$ is a contravariant 1-tensor.** Acts on a covector $\omega$ by $v(\omega) = \omega(v)$, linearly. Conversely, every contravariant 1-tensor on $V$ is a vector (in finite dimensions via the double-dual identification). So $T^1(V) = V$.

**Is an instance: the inverse of a metric, $g^{ij}$.** On an inner-product space, the inner product $\langle \cdot, \cdot \rangle$ has matrix $(g_{ij})$ in a basis — a covariant 2-tensor. Its inverse matrix $(g^{ij}) = (g_{ij})^{-1}$ defines a contravariant 2-tensor $G^{-1}(\omega, \eta) = g^{ij}\omega_i\eta_j$ — the "raising indices" operation in tensor analysis applied to the metric itself. The inverse metric is *the* prototypical contravariant 2-tensor on a Riemannian manifold.

**Is an instance: the elementary tensor $E_i \otimes E_j$.** Defined by $(E_i \otimes E_j)(\omega, \eta) = \omega_i \eta_j$. This is a contravariant 2-tensor, and the $n^2$ such tensors form a basis of $T^2(V)$. As in the covariant case, $E_i \otimes E_j \neq E_j \otimes E_i$ in general — the tensor product is not commutative.

**Is an instance: a multivector $v_1 \wedge v_2 \wedge \cdots \wedge v_k$.** The alternating contravariant $k$-tensor $\frac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma)\, v_{\sigma(1)} \otimes \cdots \otimes v_{\sigma(k)}$. Multivectors are the contravariant analogue of $k$-forms, and they appear in Plücker coordinates of Grassmannians, the geometric algebra of Clifford, and the theory of distributions on a manifold.

**Is NOT an instance: a quadratic function of a covector $T(\omega) = \omega(v)^2$ for fixed $v$.** This is *not* linear in $\omega$: $T(2\omega) = 4\omega(v)^2 = 4T(\omega)$, not $2T(\omega)$. So it fails to be a contravariant 1-tensor.

**Is NOT an instance: a contravariant tensor cannot be pulled back along a non-diffeomorphism.** This is a *type* statement: $T$ being contravariant means $T$ pushes forward but does not pull back in general. The non-example is exhibited by trying: if $F : \mathbb{R} \to \mathbb{R}^2$, $t \mapsto (t, 0)$, then a contravariant 1-tensor (= vector field) on $\mathbb{R}^2$ has no canonical pullback to $\mathbb{R}$, since $dF$ has full rank but a vector field on $\mathbb{R}^2$ might point in a direction not in the image of $dF$.

**Corollary (dimension).** $\dim T^k(V) = n^k = \dim T^k(V^*)$, but the two spaces are *not* canonically isomorphic; they only become so once a basis (or, in the manifold setting, a metric) is chosen.

**Corollary (the canonical pairing $T^k(V) \otimes T^k(V^*) \to \mathbb{R}$).** Given a contravariant $T$ and a covariant $\alpha$ of the same rank, there is a canonical bilinear pairing $\langle T, \alpha \rangle = T^{i_1\cdots i_k}\alpha_{i_1\cdots i_k}$ (full contraction). For $k=1$ this is the evaluation $\alpha(v)$; for $k = 2$ with $T = v\otimes w$ and $\alpha = \varphi\otimes\psi$, it is $\varphi(v)\psi(w)$. This pairing is the algebraic root of every "contract a tensor against a tensor" operation in the chapter.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that for any vector $v$, the contravariant tensor $v \otimes v$ has components $v^i v^j$; (ii) verify that on $V = \mathbb{R}^2$ with $v = E_1 + E_2$ and $w = E_1 - E_2$, the contravariant 2-tensor $v \otimes w$ has matrix $\begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$ in the standard basis (a rank-1 matrix, since $v \otimes w$ is an elementary tensor); (iii) verify the canonical pairing identity $\langle v \otimes w, \varphi \otimes \psi \rangle = \varphi(v) \psi(w)$ from the definitions.

---

# Unlocked by This

> [!tip] Contravariant Tensor Field on a Manifold *(from [[Differential Geometry VII — Tensors and Tensor Fields]])*
> A smoothly varying assignment of a contravariant $k$-tensor to each tangent space. Vector fields are the case $k = 1$. Higher-rank contravariant tensor fields appear as the inverse metric (a $(2,0)$-tensor field), bivector fields (used in Poisson geometry), and the contravariant version of the curvature tensor.

> [!tip] Multivector Field and the Schouten Bracket *(from Poisson Geometry)*
> A **multivector field** is an alternating contravariant tensor field. The space of multivector fields carries the **Schouten–Nijenhuis bracket**, an extension of the Lie bracket from vector fields to multivectors. A **Poisson bivector** $\pi \in T^{(2,0)}(M)$ with $[\pi, \pi]_{\text{Schouten}} = 0$ defines a Poisson manifold, the geometric structure underlying Hamiltonian mechanics in the absence of a symplectic form.

> [!tip] Tensor Density and the Volume Element *(from Riemannian Geometry / GR)*
> A contravariant tensor of weight 1 — a tensor times a power of $\det g$ — transforms with an extra Jacobian factor under change of coordinates. The natural volume element on a Riemannian manifold $\sqrt{|\det g|}\, dx^1\cdots dx^n$ is a tensor density of this form, and densities are what is integrated against tensor fields when no canonical volume form exists.
