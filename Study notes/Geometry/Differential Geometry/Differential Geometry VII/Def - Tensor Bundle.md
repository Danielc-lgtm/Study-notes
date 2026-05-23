---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Mixed Tensor"
  - "Def - The Tangent Bundle"
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, bundles]
---

# Notation

$M$ is a smooth $n$-manifold (Hausdorff, second countable). $T_pM, T_p^*M$ are the tangent and cotangent spaces at $p$. For fixed nonnegative integers $k, \ell$, the **tensor bundle of type $(k, \ell)$** is $T^{(k,\ell)}M$, with total space the disjoint union $\bigsqcup_{p \in M} T^{(k,\ell)}(T_pM)$. The fibre over $p$ is the algebraic mixed-tensor space $T^{(k,\ell)}(T_pM) = (T_pM)^{\otimes k} \otimes (T_p^*M)^{\otimes \ell}$ — see [[Def - Mixed Tensor]]. The bundle projection is $\pi : T^{(k,\ell)}M \to M$. The full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

What we want is a **smooth manifold whose points are tensors at points of $M$**. The motivation is the same as for the [[Def - The Tangent Bundle|tangent bundle]] and [[Def - Cotangent Space and Cotangent Bundle|cotangent bundle]]: a tensor field is a smooth assignment of a tensor to each point, and "smooth" requires the codomain to be a smooth manifold. The tensor bundle is the smooth manifold that makes "smooth tensor field" make sense.

The construction proceeds by **fibrewise multilinear algebra plus a vector-bundle structure**. The fibrewise data is automatic: at each $p$, the algebra of [[Def - Mixed Tensor|mixed tensors]] $T^{(k,\ell)}(T_pM)$ is a well-defined vector space of [[Def - Dimension|dimension]] $n^{k+\ell}$. The work is in giving the disjoint union of these fibres a smooth structure compatible with the projection $\pi : T^{(k,\ell)}M \to M$. The recipe is:

1. **Local trivializations.** In a chart $(U, \varphi = (x^1, \dots, x^n))$ on $M$, the coordinate vector fields $(\partial_1, \dots, \partial_n)$ trivialize $TM|_U$ as $U \times \mathbb{R}^n$, and the coordinate covector fields $(dx^1, \dots, dx^n)$ trivialize $T^*M|_U$. Tensoring these together gives a local frame $\{\partial_{i_1}\otimes\cdots\otimes \partial_{i_k}\otimes dx^{j_1}\otimes\cdots\otimes dx^{j_\ell}\}$ for $T^{(k,\ell)}M|_U$, which trivializes the tensor bundle on $U$ as $U \times \mathbb{R}^{n^{k+\ell}}$.

2. **Transition functions.** On an overlap $U \cap U'$ between charts $(x^i)$ and $(\tilde x^i)$, the tensor-bundle frame changes by the [[Thm - Transformation Rule for Tensor Components|transformation rule]]: a Jacobian factor per upper index, an inverse-Jacobian factor per lower index. These are smooth functions of position, so the transition functions of $T^{(k,\ell)}M$ are smooth, and the bundle inherits a smooth vector-bundle structure.

3. **Manifold structure on the total space.** The total space $T^{(k,\ell)}M$ inherits a smooth manifold structure of dimension $n + n^{k+\ell}$ from the local trivializations: a point $(p, W) \in T^{(k,\ell)}M$ over $p \in U$ has coordinates $(x^1(p), \dots, x^n(p), W^{i_1\cdots i_k}_{j_1\cdots j_\ell})$, with the components $W^{\cdots}_{\cdots}$ taken in the coordinate frame.

The reason this is essentially **forced** and not a free choice is the [[Thm - Vector Bundle Construction Lemma|vector bundle construction lemma]]: given fibres $T^{(k,\ell)}(T_pM)$ varying with $p$ and transition functions that are smooth on overlaps, the lemma produces a unique smooth vector bundle structure (up to isomorphism) on the disjoint union. So the only thing to verify is that the transformation rule for tensor components is smooth — and it is, since it consists of products and reciprocals of partial derivatives of the (smooth) coordinate-change maps.

One could ask whether to define the tensor bundle as an *abstract* construction first, then identify it with the disjoint union of fibres. The standard route — and the one followed here and in Lee — does it the other way: start from the disjoint union, give it a smooth structure via local trivializations. The abstract approach exists (via the [[Thm - Universal Property of the Tensor Product|universal property]] of tensor products applied to bundles), but the concrete-disjoint-union approach is the one used in practice because local computations are immediate.

The relationship to existing bundles is:
- $T^{(0,0)}M = M \times \mathbb{R}$ (the trivial line bundle, sections = smooth functions).
- $T^{(1,0)}M = TM$ ([[Def - The Tangent Bundle|tangent bundle]]).
- $T^{(0,1)}M = T^*M$ ([[Def - Cotangent Space and Cotangent Bundle|cotangent bundle]]).

So the tensor bundles include $TM$ and $T^*M$ as special cases. The general tensor bundle is built from these two using tensor product operations on vector bundles, which can be defined fibrewise just as on vector spaces.

---

# The Definition

Let $M$ be a smooth $n$-manifold and let $k, \ell$ be non-negative integers. The **tensor bundle of type $(k, \ell)$** over $M$, denoted $T^{(k,\ell)}M$, is the disjoint union

$$T^{(k,\ell)}M := \bigsqcup_{p \in M} T^{(k,\ell)}(T_pM),$$

equipped with the unique smooth vector bundle structure satisfying:

1. **Projection.** The natural projection $\pi : T^{(k,\ell)}M \to M$ sending $(p, W) \in \{p\} \times T^{(k,\ell)}(T_pM)$ to $p$ is smooth.

2. **Local trivializations.** For each smooth chart $(U, \varphi = (x^1, \dots, x^n))$ of $M$, the map

$$\Phi_U : \pi^{-1}(U) \to U \times \mathbb{R}^{n^{k+\ell}}, \quad (p, W) \mapsto (p, W^{i_1\cdots i_k}_{j_1\cdots j_\ell})$$

(where $W^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ are the components of $W$ in the coordinate frame at $p$) is a [[Def - Diffeomorphism|diffeomorphism]] that is fibrewise linear.

3. **Transition functions.** On an overlap of charts $(x^i)$ and $(\tilde x^i)$, the transition function $\Phi_{\tilde U} \circ \Phi_U^{-1} : (U \cap \tilde U) \times \mathbb{R}^{n^{k+\ell}} \to (U \cap \tilde U) \times \mathbb{R}^{n^{k+\ell}}$ acts on the fibre coordinates by

$$\tilde W^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}\frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\cdots\frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\, W^{a_1\cdots a_k}_{b_1\cdots b_\ell}.$$

The **rank** of the tensor bundle is $n^{k+\ell}$. Special cases:

| $(k, \ell)$ | Tensor bundle | Standard name |
|---|---|---|
| $(0, 0)$ | $M \times \mathbb{R}$ | Trivial line bundle |
| $(1, 0)$ | $TM$ | [[Def - The Tangent Bundle|Tangent bundle]] |
| $(0, 1)$ | $T^*M$ | [[Def - Cotangent Space and Cotangent Bundle|Cotangent bundle]] |
| $(k, 0)$ | $T^kTM$ | Contravariant $k$-tensor bundle |
| $(0, \ell)$ | $T^\ell T^*M$ | Covariant $\ell$-tensor bundle |
| $(1, 1)$ | $\mathrm{End}(TM)$ | Endomorphism bundle |
| $(0, 2)$ | $T^2 T^*M$ | Bilinear form bundle (home of metrics) |
| $(1, 3)$ | $T^{(1,3)}M$ | Home of the Riemann curvature |

**Tensor bundle as built from $TM$ and $T^*M$.** As vector bundles,

$$T^{(k,\ell)}M = \underbrace{TM \otimes \cdots \otimes TM}_{k} \otimes \underbrace{T^*M \otimes \cdots \otimes T^*M}_{\ell},$$

where $\otimes$ is the tensor product of vector bundles (defined fibrewise, with smooth transition functions given by tensor products of the transition functions of the factors).

---

# Categorical / Structural Definition

The tensor bundle is a **functor** $T^{(k,\ell)} : \mathbf{SmoothBundles}(M) \to \mathbf{SmoothBundles}(M)$ applied to $TM$ and $T^*M$. More precisely:

The tensor product of two vector bundles $E, F$ over $M$ is constructed by taking, at each point $p$, the algebraic tensor product $E_p \otimes F_p$ of the fibres, and equipping the disjoint union with the natural smooth structure inherited from the transition functions of $E$ and $F$. Dualization is similarly fibrewise.

The tensor bundle $T^{(k,\ell)}M$ is then *the* iterated tensor product

$$T^{(k,\ell)}M = TM^{\otimes k} \otimes (T^*M)^{\otimes \ell}.$$

Universal property: a smooth bundle map $E \to T^{(k,\ell)}M$ over $M$ is the same as a smooth, fibrewise-multilinear map from $k$ copies of $TM$ and $\ell$ copies of $T^*M$ into $E$ — i.e., the universal property of the algebraic tensor product, applied bundle-by-bundle.

---

# Relate to Other Fields / Compression

The tensor bundle is **the manifold-level lift of the multilinear algebra of $V$ from [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]]**. Every linear-algebraic construction on a vector space — tensor product, dualization, symmetrization, alternation — has a bundle-level version, obtained by applying the construction to each fibre $T_pM$ and patching smoothly. The patching is automatic when the construction is functorial in the input vector space, which all the standard ones are.

From the bundle theory side, $T^{(k,\ell)}M$ is one of the **associated bundles** to the frame bundle $\mathrm{Fr}(M)$ of $M$, with the structure group $GL(n, \mathbb{R})$ acting on the standard fibre $T^{(k,\ell)}(\mathbb{R}^n)$ by the natural tensor representation. The transformation rule for components is exactly the action of the change-of-frame element of $GL(n, \mathbb{R})$ on the fibre.

**True name:** $T^{(k,\ell)}M$ is **the smooth vector bundle whose fibre at each point is the algebraic mixed-tensor space**. Its sections are tensor fields. Its transition functions are the tensor-rule transformation laws.

---

# Examples / Corollaries

**Is an instance: $TM = T^{(1,0)}M$.** The tangent bundle. Fibres are $T_pM$. Sections are vector fields.

**Is an instance: $T^*M = T^{(0,1)}M$.** The cotangent bundle. Fibres are $T_p^*M$. Sections are 1-forms.

**Is an instance: $T^2T^*M = T^{(0,2)}M$.** Sections are covariant 2-tensor fields, including metrics, symplectic forms, the second fundamental form of an embedded submanifold, the energy-momentum tensor of physics.

**Is an instance: the trivial bundle $M \times \mathbb{R}$.** This is $T^{(0,0)}M$, and its sections are smooth functions $C^\infty(M)$.

**Is an instance: the endomorphism bundle $\mathrm{End}(TM) = T^{(1,1)}M$.** Sections are smoothly varying linear endomorphisms of $TM$. The identity endomorphism — a globally-defined section — corresponds to the Kronecker delta in components, $\delta^i_j$ in every chart.

**Is NOT an instance: the *frame bundle* $\mathrm{Fr}(M)$.** This is a principal $GL(n, \mathbb{R})$-bundle, not a vector bundle. Its fibres are not vector spaces but the set of ordered bases of the corresponding tangent space. The tensor bundles are *associated* to the frame bundle but are distinct objects.

**Is NOT an instance: the unit sphere bundle $UTM$ of a Riemannian manifold.** The fibres are unit tangent vectors, which form a $(n-1)$-sphere, not a vector space. So $UTM$ is a fibre bundle but not a vector bundle, and it is not a tensor bundle.

**Corollary (rank).** As a vector bundle, $\mathrm{rank}(T^{(k,\ell)}M) = n^{k+\ell}$, where $n = \dim M$. *Proof:* the fibre is $T^{(k,\ell)}(\mathbb{R}^n) \cong \mathbb{R}^{n^{k+\ell}}$.

**Corollary (smooth structure).** The total space $T^{(k,\ell)}M$ is a smooth manifold of dimension $n + n^{k+\ell}$. *Proof:* the local trivializations cover the total space, the transition functions between trivializations are smooth, and the result is a smooth manifold by the usual chart-gluing argument.

**Corollary (sections are tensor fields).** A smooth section of $T^{(k,\ell)}M$ is a smooth map $\sigma : M \to T^{(k,\ell)}M$ with $\pi \circ \sigma = \mathrm{id}_M$. Equivalently, a smooth assignment of a $(k,\ell)$-tensor at each point — see [[Def - Tensor Field on a Manifold]].

**Calibration check.** If you have understood the definition, you should be able to: (i) state the rank of $T^{(2,3)}M$ when $\dim M = 4$ — it is $4^5 = 1024$; (ii) verify that on $M = \mathbb{R}^n$ (a single chart globally), $T^{(k,\ell)}\mathbb{R}^n \cong \mathbb{R}^n \times \mathbb{R}^{n^{k+\ell}}$ is trivially globally trivial; (iii) explain why $TS^2$ is *not* globally trivial (the hairy ball theorem), and conclude that $T^{(1,0)}S^2 = TS^2$ has no global frame, while $T^{(0,0)}S^2 = S^2 \times \mathbb{R}$ trivially does.

---

# Unlocked by This

> [!tip] Tensor Field on a Manifold *(from [[Differential Geometry VII — Tensors and Tensor Fields]])*
> A smooth section of the tensor bundle. The Riemannian metric is a section of $T^2T^*M$, the curvature is a section of $T^{(1,3)}M$. See [[Def - Tensor Field on a Manifold]].

> [!tip] Associated Bundles and the Frame Bundle *(from Gauge Theory)*
> The tensor bundle $T^{(k,\ell)}M$ is associated to the principal $GL(n, \mathbb{R})$-frame bundle $\mathrm{Fr}(M)$ via the natural representation of $GL(n, \mathbb{R})$ on $T^{(k,\ell)}(\mathbb{R}^n)$. Reducing the structure group (to $O(n)$ via a metric, to $SO(n)$ via a metric and orientation, to $\mathrm{Spin}(n)$ via a spin structure) reduces the tensor bundles to bundles of the same type but with extra constraints — e.g., $O(n)$-reduction lets one consistently raise and lower indices. This is the abstract perspective on the index gymnastics of physics.

> [!tip] Spinor Bundle *(from Gauge Theory / GR with Spinors)*
> The **spinor bundle** is *not* a tensor bundle: it is the associated bundle to a $\mathrm{Spin}(n)$-principal bundle (a "spin structure") via a different representation than the tensor ones. Spinors are objects that transform under a *double cover* of the rotation group, and they do not fit into the tensor framework. They are the obstruction to "everything is a tensor" — and they explain why Dirac fermions in physics need extra geometric data beyond the metric.
