---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Map"
  - "Def - Basis"
  - "Def - Matrix of a Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$, with basis $(e_1, \dots, e_n)$ where $n = \dim V$. A bilinear form on $V$ is a function $\beta : V \times V \to \mathbb{F}$. The matrix of $\beta$ in the basis $(e_1, \dots, e_n)$ is the $n \times n$ matrix with entries $A_{ij} = \beta(e_i, e_j)$, denoted $\mathcal{M}(\beta, (e_1, \dots, e_n))$. The space of all bilinear forms on $V$ is denoted $V^{(2)}$. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] for the full notation registry.

---

# Axiom Motivation

The thing we want to axiomatize is **a numerical pairing of two vectors that is linear in each input separately**. The motivating examples are easy to enumerate: the inner product $\langle u, v\rangle$ on a real or complex space pairs two vectors to give a scalar; matrix multiplication $u^t M v$ pairs two column vectors via a fixed matrix $M$; the evaluation pairing $\varphi(v)$ between a linear functional and a vector; the integral pairing $\int_0^1 p(x) q(x)\, dx$ on polynomials; the determinant of two columns $\det(u\ v)$ for $u, v \in \mathbb{F}^2$. All of these share two structural features. First, each takes two vector inputs and produces one scalar output. Second, each is linear *separately* in each input — fixing one and varying the other gives a linear functional. The bilinear-form axioms write down this much and nothing more, so that any theorem proved from them speaks about all five examples (and the many others) simultaneously.

Linearity in each slot is the only axiom, but it deserves a careful unpacking, because **bilinearity is not the same as linearity in the joint input**. A linear functional on the Cartesian product $V \times V$ would be a map $\Phi : V \times V \to \mathbb{F}$ with $\Phi(a_1 (u_1, w_1) + a_2 (u_2, w_2)) = a_1 \Phi(u_1, w_1) + a_2 \Phi(u_2, w_2)$ — that is, a linear functional on the $2n$-dimensional space $V \oplus V$. A bilinear form, in contrast, asks for the *much stronger* condition that scaling $u$ alone scales the output, scaling $w$ alone scales the output, adding to $u$ adds to the output, and so on, with the two slots independent. The crucial consequence is $\beta(au, w) = a\beta(u, w) = \beta(u, aw)$, so scaling *both* slots by $a$ scales the output by $a^2$ — not $a$, as joint linearity would demand. This $a^2$ behaviour is what makes bilinear forms produce *quadratic* objects (norms, energies, areas) rather than linear ones. If we had instead asked for joint linearity in $V \times V$, we would have a linear functional on $V \oplus V$, the diagonal restriction $v \mapsto \Phi(v, v)$ would be linear in $v$, and we could not capture the inner product $\langle v, v\rangle = \|v\|^2$, which is fundamentally quadratic.

We could ask whether to strengthen the definition by demanding $\beta(u, w) = \beta(w, u)$ (symmetry). That gives the strict subclass of [[Def - Symmetric and Alternating Bilinear Form|symmetric bilinear forms]] of §9A. The reason not to bake symmetry into the bilinear-form definition is that it would exclude examples we genuinely want — the integral $\int p q'$ on a polynomial space is bilinear but not symmetric, the bilinear forms arising as $u^t M v$ for non-symmetric $M$ would all be excluded, and the symmetric/alternating decomposition $V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}}$ that organises the theory would lose its left-hand side. Symmetry is a useful *extra* condition; the general bilinear-form definition is the natural starting point.

The choice of using two copies of *the same* space $V$ (rather than two different spaces $V$ and $W$) reflects what we want to study: forms that pair a vector with itself or with another vector of the same kind. A pairing between *different* vector spaces — for instance the evaluation $\varphi(v)$ between a linear functional $\varphi \in V'$ and a vector $v \in V$ — also fits the bilinear-paradigm, and is called a **bilinear functional** on $V' \times V$. In §9D the tensor product is constructed using exactly such bilinear functionals on dual product spaces $V' \times W'$. So the "two copies of $V$" version is the special case relevant when we want a single bilinear quantity (like an inner product, energy, or quadratic form) attached to a single space.

A test of having understood the axioms: can you invent the change-of-basis formula? Given a basis change $C$ (the matrix whose columns express the new basis vectors in the old basis), how does the matrix of a bilinear form transform? The answer is $A_{\text{new}} = C^t A_{\text{old}} C$, with the transpose appearing — *not* the inverse, as in the operator change-of-basis formula. The reason is that an operator transforms vectors covariantly $v_{\text{new}} = C^{-1} v_{\text{old}}$ (because $v$ in new coordinates is $v$ in old coordinates transformed back), and an operator acts on vectors, so it transforms as $A_{\text{new}} = C^{-1} A_{\text{old}} C$. A bilinear form, by contrast, takes two vectors as inputs, so its transformation involves $C$ applied to *each input*, giving $C^t A_{\text{old}} C$. The asymmetry between covariance and contravariance is what distinguishes "$T_{\mathrm{ij}}$ as the matrix of an operator" from "$T_{ij}$ as the matrix of a bilinear form", and it is the seed of the tensor-type-classification $(p, q)$ in differential geometry.

---

# The Definition

A **bilinear form** on a vector space $V$ over a field $\mathbb{F}$ is a function $\beta : V \times V \to \mathbb{F}$ that is **linear in each slot** when the other slot is held fixed. Explicitly, for all $u, u', w, w' \in V$ and $a, a' \in \mathbb{F}$:

1. **Linearity in the first slot.** $\beta(au + a'u', w) = a\beta(u, w) + a'\beta(u', w)$.
2. **Linearity in the second slot.** $\beta(u, aw + a'w') = a\beta(u, w) + a'\beta(u, w')$.

The set of bilinear forms on $V$, denoted $V^{(2)}$, is itself a vector space under pointwise addition and scalar multiplication.

**The matrix of a bilinear form.** Given a basis $(e_1, \dots, e_n)$ of $V$, the **matrix** $\mathcal{M}(\beta, (e_1, \dots, e_n))$ of $\beta$ in this basis is the $n \times n$ matrix with entries

$$A_{ij} = \beta(e_i, e_j).$$

By bilinearity, $\beta$ is determined by these values: if $u = \sum_i u_i e_i$ and $w = \sum_j w_j e_j$, then

$$\beta(u, w) = \sum_{i, j} u_i w_j \beta(e_i, e_j) = u^t A w,$$

where $u, w$ are written as column vectors of coefficients.

**Change of basis.** If $(f_1, \dots, f_n)$ is a second basis with $f_k = \sum_j C_{jk} e_j$, and if $A$ and $B$ are the matrices of $\beta$ in $(e_i)$ and $(f_i)$ respectively, then

$$B = C^t A C.$$

Note the transpose, not the inverse — this is the contrast with the operator change-of-basis formula $B = C^{-1} A C$.

---

# Categorical / Structural Definition

The categorical formulation makes the relationship between bilinear forms, the tensor product, and linear duality precise.

**A bilinear form on $V$ is a linear functional on $V \otimes V$.** Recall (from [[Def - Tensor Product of Vector Spaces]]) that the [[Thm - Universal Property of the Tensor Product|universal property]] of the tensor product asserts a bijective correspondence

$$\mathcal{B}(V, V; \mathbb{F}) \;\cong\; \mathcal{L}(V \otimes V, \mathbb{F}) = (V \otimes V)',$$

where the left side is bilinear maps $V \times V \to \mathbb{F}$ and the right side is linear functionals on $V \otimes V$. A bilinear form $\beta$ corresponds to the linear functional $\hat\beta$ with $\hat\beta(u \otimes w) = \beta(u, w)$. Hence $V^{(2)} = (V \otimes V)'$.

**A bilinear form on $V$ is a linear map $V \to V'$.** Equivalently (via "currying"), a bilinear $\beta : V \times V \to \mathbb{F}$ corresponds to a linear map $L_\beta : V \to V'$ by $L_\beta(u)(w) = \beta(u, w)$. The pair $(V, \beta)$ is **non-degenerate** when $L_\beta$ is an isomorphism, equivalently when the matrix $A$ is invertible. The two presentations — bilinear-form-as-functional-on-$V \otimes V$ and bilinear-form-as-linear-map-$V \to V'$ — are two different shadows of the same underlying object, related by the tensor-hom adjunction $\mathcal{B}(V, V; \mathbb{F}) \cong \mathcal{L}(V, V')$.

This categorical reading explains the change-of-basis formula. The map $L_\beta : V \to V'$ has matrix $A$ in the bases $(e_i)$ for $V$ and the dual basis $(e^i)$ for $V'$. Changing the basis of $V$ via $C$ induces a *dual* basis change of $V'$ via $(C^t)^{-1}$ (because the dual basis transforms contravariantly), and the matrix of $L_\beta$ in the new bases is $(C^t)^{-1} A C^{-1} \cdot C = C^t \cdot$... actually the cleanest way to see it: $L_\beta(C f_k) = \sum_i C_{ik} L_\beta(e_i)$, and reading off coordinates of $L_\beta(f_k)$ in the new dual basis introduces a factor of $C^t$.

---

# Relate to Other Fields / Compression

A bilinear form is **a quadratic-form-with-its-symmetric-bilinear-form-hidden**. Every bilinear form $\beta$ defines a quadratic form $q_\beta(v) = \beta(v, v)$, and conversely (in characteristic $\neq 2$) every quadratic form arises from a unique *symmetric* bilinear form. Bilinear forms thus carry the same data as quadratic forms when symmetric, plus extra antisymmetric content when not symmetric. The decomposition $\beta = \rho + \alpha$ into symmetric and alternating parts splits this content.

From the differential geometry side, a bilinear form on the tangent space at each point is a **type $(0, 2)$ tensor field** — covariant in two indices, contravariant in zero. The metric tensor $g_{ij}$ of a Riemannian manifold is exactly a smoothly varying family of symmetric bilinear forms, one on each tangent space. The whole machinery of tensor analysis is built on understanding bilinear and multilinear forms.

**True name:** A bilinear form is the universal pairing that is linear separately in each input — the "two-vector-in, one-scalar-out, linear-each-slot" gadget. Operationally, the test for bilinearity is "fix the second slot, the first slot is linear; fix the first slot, the second slot is linear."

---

# Examples / Corollaries

**Is an instance: the inner product on a real inner product space.** $\beta(u, v) = \langle u, v\rangle$ is bilinear because the inner product is linear in each variable (over $\mathbb{R}$); it is also symmetric and positive definite. This is the model example and the source of intuition for everything else. Its matrix in an orthonormal basis is the identity matrix.

**Is an instance: $\beta(u, v) = u^t M v$ for any fixed matrix $M$.** For $u, v \in \mathbb{F}^n$ and any $n \times n$ matrix $M$, the function $\beta_M(u, v) = u^t M v$ is bilinear. Its matrix in the standard basis is exactly $M$, since $\beta_M(e_i, e_j) = e_i^t M e_j = M_{ij}$. Every bilinear form on $\mathbb{F}^n$ arises this way for a unique $M$, giving the canonical identification $V^{(2)} \cong M_n(\mathbb{F})$ in coordinates.

**Is an instance: the evaluation pairing $V' \times V \to \mathbb{F}$, $(\varphi, v) \mapsto \varphi(v)$.** This is bilinear by definition of "linear functional". It is the most natural bilinear pairing in linear algebra: it does not require any extra structure (no inner product, no choice of basis) and is what defines the dual space. Strictly this is a bilinear *functional* on a product of two *different* spaces, but the same axioms apply.

**Is an instance: $\beta(p, q) = \int_0^1 p(x) q(x)\, dx$ on the polynomial space $\mathcal{P}_n(\mathbb{R})$.** This is bilinear because integration is linear, and it is symmetric and positive definite — an inner product. Its matrix in the basis $(1, x, x^2, \dots, x^n)$ is the **Hilbert matrix** $H_{ij} = 1/(i + j - 1)$, famously ill-conditioned.

**Is an instance: the non-symmetric form $\beta(p, q) = p(0) \cdot q'(1)$ on $\mathcal{P}_n(\mathbb{R})$.** This is bilinear (each slot is a linear operation on the polynomial), but it is *not* symmetric — $\beta(1, x) = 1 \cdot 1 = 1$ while $\beta(x, 1) = 0 \cdot 0 = 0$. It is one of LADR's example 9.8 type constructions and shows that bilinear forms need not look like inner products.

**Is an instance: the cross-product-like form $\alpha(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{R}^2$.** This is bilinear and *alternating* — $\alpha(v, v) = 0$ identically. Its matrix in the standard basis is $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which is antisymmetric. This is the prototypical alternating bilinear form, and on $\mathbb{R}^n$ for $n = 2$ it is essentially the determinant $\det(u\ v)$.

**Is NOT an instance: $f(u, v) = \|u\| + \|v\|$ on a real inner product space.** This fails linearity in each slot: $f(2u, v) = 2\|u\| + \|v\| \neq 2(\|u\| + \|v\|)$. The sum-of-norms is *not* bilinear; it is not even linear in either slot individually. It probes axiom 1 (and 2).

**Is NOT an instance: $g(u, v) = \langle u, v\rangle^2$ on a real inner product space.** This fails linearity in each slot: $g(au, v) = a^2 \langle u, v\rangle^2 \neq a g(u, v)$ (for $a \neq 0, 1$). Squaring an inner product is *quadratic* in each slot, not linear, so it is not a bilinear form. It probes axiom 1.

**Corollary (dimension of $V^{(2)}$).** The space of bilinear forms on an $n$-dimensional $V$ has dimension $n^2$. A bilinear form is determined by its matrix $(A_{ij})_{i, j=1}^n$, which has $n^2$ free entries. This is one of those facts so basic it is rarely stated explicitly, but it is the reason $V^{(2)} \cong M_n(\mathbb{F}) \cong \mathbb{F}^{n^2}$.

**Corollary (bilinear functions are "matrix sandwiches").** Every bilinear form on $\mathbb{F}^n$ has the form $\beta(u, v) = u^t M v$ for a unique matrix $M = \mathcal{M}(\beta, (e_1, \dots, e_n))$. So bilinear forms on $\mathbb{F}^n$ and $n \times n$ matrices are the same data — provided one fixes a basis.

**Calibration check.** If you have understood the definition, you should be able to verify: (i) the function $\beta(u, v) = u_1 v_1 - u_2 v_2$ on $\mathbb{R}^2$ is bilinear and symmetric but not positive definite (it is the Minkowski metric in two dimensions, signature $(1, 1)$); (ii) the function $\beta(u, v) = u^t v$ on $\mathbb{R}^n$ is bilinear with matrix $I$ in the standard basis; and (iii) the function $\beta(u, v) = \|u + v\|^2 - \|u - v\|^2$ on a real inner product space is bilinear, and (after computing) equals $4\langle u, v\rangle$ — the [[Ex - Inner product determined by norm via the polarization identity|polarisation identity]].

---

# Unlocked by This

> [!tip] Symmetric Bilinear Form *(LADR §9A)*
> A bilinear form that is also symmetric, $\beta(u, w) = \beta(w, u)$. See [[Def - Symmetric and Alternating Bilinear Form]]. Symmetric bilinear forms are diagonalisable and classified up to congruence by the signature in [[Thm - Sylvester's Law of Inertia|Sylvester's law]].

> [!tip] Quadratic Form *(LADR §9A)*
> The "diagonal" $q_\beta(v) := \beta(v, v)$ of a bilinear form. See [[Def - Quadratic Form]]. In characteristic $\neq 2$, every quadratic form arises from a unique symmetric bilinear form via polarisation.

> [!tip] Tensor of Type (0,2) *(from Differential Geometry)*
> A smoothly varying family of bilinear forms on the tangent spaces of a manifold. The Riemannian metric is the prototypical example. The "two covariant indices" $T_{ij}$ in physicists' tensor notation are exactly the two slots of a bilinear form.

> [!tip] Sesquilinear Form *(from Complex Inner Product Theory)*
> The complex generalisation: a function $\beta : V \times V \to \mathbb{C}$ that is conjugate-linear in the first slot and linear in the second (or vice versa, depending on convention). The Hermitian inner product is the prototype. Sesquilinear forms are not bilinear in the strict sense — but the theory is closely parallel, with Hermitian forms playing the role of symmetric bilinear forms.
