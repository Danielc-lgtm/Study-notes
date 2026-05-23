---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Mixed Tensor"
  - "Def - Tensor Field on a Manifold"
  - "Def - Dual Space"
tags: [geometry, differential-geometry, tensor-operations]
---

# Notation

$V$ is a finite-dimensional real vector space, $\dim V = n$. $M$ is a smooth manifold. $T^{(k,\ell)}(V)$ is the space of mixed $(k, \ell)$-tensors, $T^{(k,\ell)}M$ the corresponding bundle, $\mathcal{T}^{(k,\ell)}(M)$ the space of smooth $(k,\ell)$-tensor fields. The contraction collapsing the $i$-th upper index against the $j$-th lower index is denoted $C^i_j : T^{(k,\ell)} \to T^{(k-1, \ell-1)}$. In components, contraction sets one upper index equal to one lower index and sums (Einstein convention). Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

The motivation is to **reduce the rank of a tensor by exactly one upper and one lower slot, in a coordinate-invariant way**. The simplest example is the **trace** of a linear map $A : V \to V$: viewing $A$ as a $(1, 1)$-tensor with components $A^i_j$, the trace is $A^i_i = \sum_i A^i_i$. This is a single number — a $(0, 0)$-tensor — extracted from a $(1, 1)$-tensor by setting one upper index equal to one lower index and summing. The remarkable fact, which is what makes contraction useful, is that *the trace is independent of basis*: $\tilde A^i_i = A^i_i$ for any change of basis. The summation over a "repeated index" produces a basis-independent quantity precisely because one of the two indices transforms with the Jacobian and the other with the inverse Jacobian, and the two factors cancel.

The generalization to higher rank: given a $(k, \ell)$-tensor $T$ with $k, \ell \geq 1$, pick one upper slot (say the $i$-th) and one lower slot (say the $j$-th), and form the contraction by inserting the **trace pairing** $\mathrm{tr} : V \otimes V^* \to \mathbb{R}$, $v \otimes \omega \mapsto \omega(v)$ in those slots. The result has $k - 1$ upper indices and $\ell - 1$ lower indices, so it lives in $T^{(k-1, \ell-1)}$. In components, the recipe is just "match the chosen upper index to the chosen lower index and sum":

$$(C^i_j T)^{a_1\cdots \hat a_i \cdots a_k}_{b_1\cdots \hat b_j \cdots b_\ell} = T^{a_1\cdots a_{i-1}\, c\, a_{i+1}\cdots a_k}_{b_1\cdots b_{j-1}\, c\, b_{j+1}\cdots b_\ell}$$

(summed over the dummy index $c$, with hats indicating omission of the contracted slots).

Why does this define a *tensor*, rather than a basis-dependent quantity? The fundamental reason is the canonical isomorphism

$$\mathrm{tr} : V \otimes V^* \to \mathbb{R}, \quad v \otimes \omega \mapsto \omega(v),$$

which is well-defined and basis-independent. Contraction is just this trace pairing applied to the chosen upper-lower pair, with the remaining slots untouched. Since the trace pairing is coordinate-invariant, so is contraction.

The choice of *which* upper index to contract against *which* lower index matters: $C^1_1 T$ and $C^2_1 T$ are generally different tensors. Only the trace of a $(1, 1)$-tensor has no ambiguity (since there is only one slot of each kind). For higher-rank tensors, one must specify the pair of slots being contracted.

A natural question: can we contract a $(k, 0)$ or $(0, \ell)$ tensor against itself? Without extra structure, no — contraction requires one upper and one lower slot to pair. With a metric $g$, however, the metric *raises and lowers indices*, converting a $(0, \ell)$-tensor into a $(\ell, 0)$ via $T^{i_1\cdots i_\ell} = g^{i_1 a_1}\cdots g^{i_\ell a_\ell} T_{a_1\cdots a_\ell}$. After raising, contraction is possible. This is how the **scalar curvature** is obtained: contract the Ricci tensor (a $(0, 2)$-tensor) with the inverse metric to get a $(0, 0)$-tensor, $R = g^{ij}R_{ij}$.

One could ask whether contraction extends to other natural pairings: e.g., contracting an upper index against another upper index, or a lower against a lower. **Without a metric, no.** The only canonical pairing on $V \times V^*$ is the trace; there is no canonical pairing $V \times V \to \mathbb{R}$ or $V^* \times V^* \to \mathbb{R}$. With a metric, both become available: $g : V \times V \to \mathbb{R}$ and $g^{-1} : V^* \times V^* \to \mathbb{R}$. So the metric is what enables index gymnastics in general; without it, you are stuck with upper-against-lower contraction only.

---

# The Definition

Let $V$ be a finite-dimensional real vector space and let $k, \ell \geq 1$. For $1 \leq i \leq k$ and $1 \leq j \leq \ell$, the **contraction** $C^i_j : T^{(k,\ell)}(V) \to T^{(k-1, \ell-1)}(V)$ is the linear map defined as follows.

On elementary tensors $v_1 \otimes \cdots \otimes v_k \otimes \omega^1 \otimes \cdots \otimes \omega^\ell$ in $T^{(k,\ell)}(V)$,

$$C^i_j(v_1 \otimes \cdots \otimes v_k \otimes \omega^1 \otimes \cdots \otimes \omega^\ell) := \omega^j(v_i)\, v_1 \otimes \cdots \otimes \hat v_i \otimes \cdots \otimes v_k \otimes \omega^1 \otimes \cdots \otimes \hat\omega^j \otimes \cdots \otimes \omega^\ell,$$

where the hats indicate omission of the contracted factors. The map extends to all of $T^{(k,\ell)}(V)$ by linearity, well-defined by the universal property of the tensor product.

**In components.** Given a basis $(E_a)$ of $V$ with dual basis $(\varepsilon^b)$, a $(k, \ell)$-tensor $T$ has components $T^{a_1\cdots a_k}_{b_1\cdots b_\ell}$. The contraction $C^i_j T$ has components

$$(C^i_j T)^{a_1\cdots a_{i-1}\, a_{i+1}\cdots a_k}_{b_1\cdots b_{j-1}\, b_{j+1}\cdots b_\ell} = T^{a_1\cdots a_{i-1}\, c\, a_{i+1}\cdots a_k}_{b_1\cdots b_{j-1}\, c\, b_{j+1}\cdots b_\ell},$$

with the Einstein summation over the dummy index $c$. The contracted positions disappear: the result has $k - 1$ upper indices and $\ell - 1$ lower indices.

**Contraction is coordinate-invariant.** Under a change of basis, the components transform by the tensor rule, and the Jacobian factors on the $c$-index (one upper, one lower) cancel. So $C^i_j T$ is a well-defined element of $T^{(k-1, \ell-1)}$, with components transforming by the appropriate tensor rule.

**Contraction of tensor fields.** For a smooth $(k, \ell)$-tensor field $A$ on $M$ with $k, \ell \geq 1$ and chosen indices $i, j$, the contraction $C^i_j A$ is the smooth $(k-1, \ell-1)$-tensor field defined fibrewise: $(C^i_j A)_p := C^i_j(A_p)$. Smoothness is automatic because contraction is a linear operation on each fibre, and linear fibre operations preserve smoothness of sections.

**Special cases:**
- $(1, 1) \to (0, 0)$: $C^1_1$ of a $(1, 1)$-tensor $A^i_j$ is the scalar $A^i_i$ — the **trace** of $A$. For an endomorphism $A : V \to V$, this recovers the standard matrix trace.
- $(1, 2) \to (0, 1)$: $C^1_1$ of a $(1, 2)$-tensor $T^a_{bc}$ is the 1-tensor $T^c_{cb}$ — contract the upper index against the first lower index.
- $(1, 3) \to (0, 2)$: contraction of the Riemann curvature $R^i_{jk\ell}$ on (say) the first upper and second lower indices gives the **Ricci tensor** $R_{j\ell} = R^i_{ji\ell}$, a $(0, 2)$-tensor.

**Iterated contractions and full contraction.** Repeated contractions reduce the type by $(1, 1)$ each time. The result of $\min(k, \ell)$ contractions is a tensor of type $(k - \min(k,\ell), \ell - \min(k,\ell))$, equal to $(\max(k - \ell, 0), \max(\ell - k, 0))$.

For a $(k, k)$-tensor, the full contraction $C^1_1 \circ C^2_2 \circ \cdots \circ C^k_k$ produces a scalar — the *full trace*, an invariant of the tensor.

---

# Categorical / Structural Definition

The trace pairing $\mathrm{tr} : V \otimes V^* \to \mathbb{R}$ — sending $v \otimes \omega$ to $\omega(v)$ — is **the unique linear map** (up to scalar) that is invariant under the diagonal $GL(V)$-action. *Proof sketch:* the only $GL(V)$-invariant element of $V^* \otimes V$ (the natural target's dual) is the identity endomorphism $\sum_i \varepsilon^i \otimes E_i$, and trace pairing is dual to it.

Contraction $C^i_j : T^{(k,\ell)} \to T^{(k-1, \ell-1)}$ is the application of the trace pairing to the chosen $i$-th $V$-factor and $j$-th $V^*$-factor of $V^{\otimes k} \otimes (V^*)^{\otimes \ell}$:

$$C^i_j = \mathrm{id}^{\otimes (i-1)} \otimes (\mathrm{tr} \cdot) \otimes \mathrm{id}^{\otimes (k - i)} \otimes \mathrm{id}^{\otimes (j-1)} \otimes \mathrm{id}^{\otimes (\ell - j)},$$

where the trace pairing is applied in the appropriate factor positions (matching the $i$-th $V$ slot with the $j$-th $V^*$ slot).

The categorical content: contraction is the *unit/counit* of the **adjunction** $\otimes V \dashv \otimes V^*$ in the category of finite-dimensional vector spaces. The unit is the dualization $\mathbb{R} \to V \otimes V^*$ (the identity-as-element-of-$V \otimes V^*$, $\sum_i E_i \otimes \varepsilon^i$), and the counit is the trace $V^* \otimes V \to \mathbb{R}$. Contraction $C^i_j$ is the application of the counit to the chosen pair of slots.

This functorial reading is what makes contraction natural under any morphism. In the manifold setting, the trace pairing of a vector field with a 1-form is a $C^\infty(M)$-bilinear pairing $\mathfrak{X}(M) \times \Omega^1(M) \to C^\infty(M)$ — i.e., the natural evaluation $(\omega, X) \mapsto \omega(X)$. Contraction of a tensor field is the application of this evaluation in selected slots.

---

# Relate to Other Fields / Compression

Contraction is the **trace operation** generalized to tensors of arbitrary type. The trace of a matrix, the divergence of a vector field (a contraction involving the covariant derivative), the Ricci tensor as a contraction of the Riemann curvature — all are instances of the same algebraic operation.

From the linear algebra side, contraction is the linear algebra fact that $V \otimes V^* \cong \mathcal{L}(V, V)$ comes with a canonical map to $\mathbb{R}$, the trace. The trace is defined coordinate-independently because of this canonical identification — see [[Def - Tensor Product of Vector Spaces|tensor products]] and the example $V^* \otimes V \cong \mathcal{L}(V, V)$.

From the physics side, contraction is **summing over a repeated up-down index pair** (Einstein summation). The notation $A^i_i$ is *defined* to mean the trace; the index conventions are designed so that contractions always make sense automatically.

**True name:** Contraction is **the trace pairing $V \otimes V^* \to \mathbb{R}$ applied to selected slots of a tensor**. Operationally: set one upper index equal to one lower index and sum.

---

# Examples / Corollaries

**Is an instance: the trace of a matrix.** For a $(1, 1)$-tensor $A^i_j$, the contraction $A^i_i$ is the matrix trace $\sum_i A^i_i$. Coordinate-invariant because $\tilde A^i_i = \frac{\partial \tilde x^i}{\partial x^a}\frac{\partial x^b}{\partial \tilde x^i} A^a_b = \delta^b_a A^a_b = A^a_a$.

**Is an instance: the Ricci tensor.** The Riemann curvature is a $(1, 3)$-tensor $R^i_{jk\ell}$. The Ricci tensor is the contraction on the first upper and second lower indices: $R_{j\ell} = R^i_{ji\ell}$, a $(0, 2)$-tensor. (Lee and most modern texts; some old conventions contract on different positions.)

**Is an instance: the scalar curvature.** Contract the Ricci tensor with the inverse metric: $R = g^{j\ell} R_{j\ell}$, a $(0, 0)$-tensor (a function). This is a *double* operation: index raising via the metric, then contraction.

**Is an instance: the divergence of a vector field.** For a vector field $X^i$ and a connection $\nabla$ on $M$, the covariant derivative $\nabla X$ is a $(1, 1)$-tensor field with components $(\nabla X)^i_j = \partial_j X^i + \Gamma^i_{jk}X^k$. Its trace $(\nabla X)^i_i$ is the divergence $\operatorname{div} X$, a function. So divergence is "covariant differentiate, then contract".

**Is an instance: the evaluation $\omega(X)$ of a 1-form on a vector field.** Treat $\omega \otimes X$ as a $(1, 1)$-tensor field; contract to get the scalar $\omega(X) = \omega_i X^i$. This shows that the natural evaluation pairing *is* a contraction.

**Is NOT an instance: "summing over indices in any order".** Without a metric, you cannot contract upper-against-upper or lower-against-lower. The "sum" $T^{ii}$ for a $(2, 0)$-tensor is *not* basis-independent: $\tilde T^{ii} = \frac{\partial \tilde x^i}{\partial x^a}\frac{\partial \tilde x^i}{\partial x^b} T^{ab}$, with *both* Jacobian factors going the same way — they do not cancel, and the "sum" is chart-dependent.

**Is NOT an instance: a "contraction" of a $(2, 1)$-tensor that doesn't specify which slot.** A $(2, 1)$-tensor $T^{ij}_k$ has *two* upper slots and *one* lower; contracting requires specifying which upper slot pairs with the lower. The two contractions $T^{ij}_i$ (contract first upper with lower) and $T^{ij}_j$ (contract second upper with lower) are *different* $(1, 0)$-tensors in general; only when $T$ is symmetric in its upper indices do they agree.

**Corollary (contraction is a linear map).** $C^i_j(aT + bS) = a\, C^i_j T + b\, C^i_j S$ for $a, b \in \mathbb{R}$ and $T, S \in T^{(k,\ell)}(V)$. This follows because contraction is a tensor-product operation applied to the trace pairing, and tensor products are bilinear.

**Corollary (contraction commutes with pullback for the trace).** For a smooth map $F : M \to N$ and a covariant tensor field $A$ on $N$, contraction and pullback do *not* in general commute (because contraction needs at least one contravariant slot, which only pullback of mixed tensors would have, and that requires $F$ [[Def - Diffeomorphism|diffeomorphism]]). But for the **full trace** (which produces a scalar), pullback gives $F^*(\mathrm{tr}\, A) = \mathrm{tr}(F^* A)$ when $F$ is a diffeomorphism.

**Corollary (multiplicativity of trace under tensor product).** $\mathrm{tr}(A \otimes B) = (\mathrm{tr}\, A)(\mathrm{tr}\, B)$ for $(1, 1)$-tensors $A, B$. *Proof:* in components, $(A \otimes B)^{ij}_{k\ell} = A^i_k B^j_\ell$, and contracting both pairs gives $A^i_i B^j_j$.

**Calibration check.** If you have understood the definition, you should be able to: (i) compute the trace of the projection $P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ on $\mathbb{R}^2$ — it is $P^i_i = 1$; (ii) verify that for the Kronecker delta $\delta$, the trace is $\delta^i_i = n$ in $n$ [[Def - Dimension|dimensions]]; (iii) explain why the "naive trace" $T^{ii}$ of a contravariant 2-tensor is *not* basis-independent, and identify the basis-independent quantity built from $T^{ij}$ alone — *there is none*, until you contract with a metric (or with a covariant 2-tensor), giving $g_{ij}T^{ij}$ which is invariant.

---

# Unlocked by This

> [!tip] The Ricci Tensor *(from Riemannian Geometry)*
> The **Ricci tensor** $R_{j\ell} = R^i_{ji\ell}$ is the contraction of the Riemann curvature on its first contravariant index. It is a symmetric $(0, 2)$-tensor field, and it plays the central role in Einstein's equations. The scalar curvature $R = g^{j\ell}R_{j\ell}$ is its further contraction with the inverse metric, a function on $M$ encoding average curvature.

> [!tip] The Divergence Theorem and Conservation Laws *(from Riemannian Geometry / GR)*
> The **divergence** $\operatorname{div} X = \nabla_i X^i$ of a vector field is the trace of its covariant derivative. On an oriented Riemannian manifold, the divergence theorem $\int_M (\operatorname{div} X)\, \mathrm{vol}_g = \int_{\partial M} g(X, n)\, \mathrm{vol}_{\partial M}$ generalizes the classical divergence theorem from $\mathbb{R}^n$. The conservation law $\nabla_\mu T^{\mu\nu} = 0$ for the stress-energy tensor in GR is a contraction-style identity, and the integrated version is the conservation of energy-momentum.

> [!tip] Trace as Coordinate-Invariant Scalar *(from Operator Theory / Linear Algebra)*
> The trace of a linear operator is coordinate-invariant precisely because it is a tensor contraction. The same principle generalizes: any invariant of a tensor under change of basis is built from contractions and other coordinate-invariant operations. In matrix theory, the "elementary symmetric functions of the eigenvalues" — trace, sum of principal minors, determinant — are all coordinate-invariant, and all are tensor invariants of the endomorphism $A$.
