---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Tensor Bundle"
  - "Def - Mixed Tensor"
  - "Def - Section of a Vector Bundle"
  - "Def - Smooth Manifold"
  - "Def - Vector Field on a Manifold"
  - "Def - Covector Field and Differential 1-Form"
tags: [geometry, differential-geometry, tensor-fields]
---

# Notation

$M$ is a smooth $n$-manifold; $T^{(k,\ell)}M$ is the [[Def - Tensor Bundle|tensor bundle]] of type $(k, \ell)$. The space of smooth $(k, \ell)$-tensor fields is $\mathcal{T}^{(k,\ell)}(M) = \Gamma(T^{(k,\ell)}M)$. Lee uses $\mathcal{T}^k(M) = \Gamma(T^kT^*M)$ for purely covariant $k$-tensor fields. Vector fields are $\mathfrak{X}(M) = \Gamma(TM) = \mathcal{T}^{(1,0)}(M)$; covector fields / 1-forms are $\Omega^1(M) = \Gamma(T^*M) = \mathcal{T}^{(0,1)}(M)$. In a chart $(x^i)$, a $(k, \ell)$-tensor field has component functions $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}(x) \in C^\infty(U)$. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

What we want is **a tensor at every point of $M$, varying smoothly with the point**. The fibrewise data is already provided by [[Def - Mixed Tensor]]: at each $p$, the space $T^{(k,\ell)}(T_pM)$ is a finite-dimensional vector space. The non-trivial step is "varying smoothly", and there are several ways to make it precise — each capturing the same notion but emphasizing a different perspective. Understanding the equivalence between them is the central technical content of this definition.

**The first perspective: a smooth section of the tensor bundle.** This is the cleanest definition: a $(k, \ell)$-tensor field is a smooth section $A : M \to T^{(k,\ell)}M$, where $T^{(k,\ell)}M$ is the smooth vector bundle whose fibre at $p$ is $T^{(k,\ell)}(T_pM)$. Smoothness is smoothness of the map $A$ between manifolds. This perspective is most useful for proving things by appeal to the general theory of vector bundles (existence via partitions of unity, transversality results, characteristic classes).

**The second perspective: smooth component functions in every chart.** A rough section $A : M \to T^{(k,\ell)}M$ (one that need not be smooth) is smooth if and only if, in every smooth chart $(x^i)$, the $n^{k+\ell}$ component functions $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}(x) = A(dx^{i_1}, \dots, dx^{i_k}, \partial_{j_1}, \dots, \partial_{j_\ell})$ are smooth functions of position. This perspective is most useful for *computations*: when handed an explicit formula, you check smoothness of the components.

**The third perspective: a $C^\infty(M)$-multilinear map.** A smooth covariant $k$-tensor field $A$ induces a map $\mathfrak{X}(M) \times \cdots \times \mathfrak{X}(M) \to C^\infty(M)$ by $A(X_1, \dots, X_k)(p) = A_p(X_1|_p, \dots, X_k|_p)$, and this map is $C^\infty(M)$-multilinear: $A(\dots, fX_i, \dots) = f\, A(\dots, X_i, \dots)$ for $f \in C^\infty(M)$. The remarkable fact is that the converse holds: every $C^\infty(M)$-multilinear map $\mathfrak{X}(M)^k \to C^\infty(M)$ comes from a unique smooth covariant $k$-tensor field. This is the [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions|tensor characterization lemma]], the operational heart of the chapter.

The three perspectives are equivalent: the smoothness of the section, the smoothness of the components in charts, and the $C^\infty(M)$-multilinearity each detect the same class of objects. The first perspective is the **definition**, the second is the **chart-level diagnostic**, and the third is the **algebraic-operational diagnostic**.

Why is the algebraic characterization (perspective 3) so important? Because it is what distinguishes **tensorial** from **non-tensorial** operations. The Lie bracket $[X, Y]$, the covariant derivative $\nabla_X Y$ in the $X$ slot, and the exterior derivative $d\omega$ are all *not* $C^\infty(M)$-multilinear — they have differential terms that pick up $df$ when functions are pulled out of slots. The metric $g(X, Y)$, the curvature $R(X, Y, Z, \cdot)$, and the contraction $g^{ij}T_{ij}$ are $C^\infty(M)$-multilinear. The diagnostic is what tells you, at a glance, whether your object lives at a point or secretly involves derivatives across points.

One could ask whether we need all three perspectives — wouldn't just one suffice? In practice, all three are needed. The bundle-section perspective is what makes existence theorems (every manifold has a Riemannian metric) come from partition-of-unity arguments. The component perspective is what physicists use exclusively, with everything ultimately reduced to functions on chart domains. The $C^\infty(M)$-multilinear perspective is what makes proofs of tensorial identities clean ("the curvature tensor is $C^\infty(M)$-multilinear because the Christoffel symbols cancel — let me check the $X$ slot…"). Mastery of the topic means fluently moving between the three.

The axiom — *smoothness* — is so weak it barely deserves the name. The substantive content is in the equivalence of the three perspectives, which is a *theorem*, not an axiom: the tensor characterization lemma.

---

# The Definition

Let $M$ be a smooth manifold and $k, \ell$ non-negative integers. A **$(k, \ell)$-tensor field** on $M$ is a smooth section of the [[Def - Tensor Bundle|tensor bundle]] $T^{(k,\ell)}M$:

$$A : M \to T^{(k,\ell)}M \quad \text{with} \quad \pi \circ A = \mathrm{id}_M,$$

where $\pi : T^{(k,\ell)}M \to M$ is the bundle projection. So for each $p \in M$, $A_p := A(p) \in T^{(k,\ell)}(T_pM)$, and the assignment $p \mapsto A_p$ is smooth in the sense that $A$ is a smooth map between manifolds.

The space of all smooth $(k, \ell)$-tensor fields on $M$ is denoted

$$\mathcal{T}^{(k,\ell)}(M) := \Gamma(T^{(k,\ell)}M).$$

**Equivalent characterizations** (proved in [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions]]): the following are equivalent for a rough section $A : M \to T^{(k,\ell)}M$:

1. $A$ is smooth.
2. In every smooth chart $(U, (x^i))$ on $M$, the component functions $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}(x) := A(dx^{i_1}, \dots, dx^{i_k}, \partial_{j_1}, \dots, \partial_{j_\ell})$ are smooth on $U$.
3. Each point of $M$ is contained in some chart in which the component functions are smooth.
4. For smooth vector fields $X_1, \dots, X_\ell$ and smooth 1-forms $\omega^1, \dots, \omega^k$ on $M$, the function $A(\omega^1, \dots, \omega^k, X_1, \dots, X_\ell) : M \to \mathbb{R}$ defined pointwise is smooth, and the resulting map $\Omega^1(M)^k \times \mathfrak{X}(M)^\ell \to C^\infty(M)$ is $C^\infty(M)$-multilinear.

**Local coordinate expression.** In a chart $(U, x^i)$, every smooth $(k, \ell)$-tensor field on $U$ can be written uniquely as

$$A = A^{i_1\cdots i_k}_{j_1\cdots j_\ell}(x)\, \partial_{i_1}\otimes\cdots\otimes\partial_{i_k}\otimes dx^{j_1}\otimes\cdots\otimes dx^{j_\ell},$$

with the $n^{k+\ell}$ component functions $A^{i_1\cdots i_k}_{j_1\cdots j_\ell} \in C^\infty(U)$.

**Special cases:**
- $\mathcal{T}^{(0,0)}(M) = C^\infty(M)$ (smooth functions).
- $\mathcal{T}^{(1,0)}(M) = \mathfrak{X}(M)$ ([[Def - Vector Field on a Manifold|vector fields]]).
- $\mathcal{T}^{(0,1)}(M) = \Omega^1(M)$ ([[Def - Covector Field and Differential 1-Form|covector fields / 1-forms]]).
- $\mathcal{T}^{(0,k)}(M) = \mathcal{T}^k(M)$ in Lee's notation — covariant $k$-tensor fields, the most common case in elementary differential geometry.

**Module structure.** The space $\mathcal{T}^{(k,\ell)}(M)$ is a module over the [[Def - The Smooth Functions Ring|ring]] $C^\infty(M)$ via pointwise scalar multiplication: $(fA)_p = f(p) A_p$. This module structure is what makes the $C^\infty(M)$-multilinear characterization (item 4) sensible.

**Operations.** The pointwise operations on each fibre extend to operations on tensor fields:
- **Sum:** $(A + B)_p = A_p + B_p$ — well-defined when $A, B$ have the same type.
- **Tensor product:** $(A \otimes B)_p = A_p \otimes B_p$ — type adds: $(k_1, \ell_1) + (k_2, \ell_2) = (k_1 + k_2, \ell_1 + \ell_2)$.
- **$C^\infty(M)$-scalar multiplication:** $(fA)_p = f(p) A_p$.
- **Contraction:** $C^i_j A$ — see [[Def - Contraction of a Tensor]].
- **Pullback (covariant only):** $F^*A$ for $F : M \to N$ smooth — see [[Def - Pullback of a Covariant Tensor Field]].

All operations preserve smoothness: a smooth tensor field operated on by a smooth operation yields a smooth tensor field.

---

# Categorical / Structural Definition

A $(k,\ell)$-tensor field is **a $C^\infty(M)$-linear combination of basis tensor fields** in any chart. More structurally:

The space $\mathcal{T}^{(k,\ell)}(M)$ of smooth $(k, \ell)$-tensor fields is the iterated tensor product, **over the ring $C^\infty(M)$**, of the modules of vector fields and 1-forms:

$$\mathcal{T}^{(k,\ell)}(M) \cong \underbrace{\mathfrak{X}(M) \otimes_{C^\infty(M)} \cdots \otimes_{C^\infty(M)} \mathfrak{X}(M)}_{k \text{ factors}} \otimes_{C^\infty(M)} \underbrace{\Omega^1(M) \otimes_{C^\infty(M)} \cdots \otimes_{C^\infty(M)} \Omega^1(M)}_{\ell \text{ factors}}.$$

This is a precise statement of the tensor characterization lemma: tensor fields are tensor products of vector field and 1-form modules over the smooth-functions ring. The categorical content is that "tensor product over $C^\infty(M)$" is the right algebraic operation to use — *not* tensor product over $\mathbb{R}$ — and this is what gives the $C^\infty(M)$-multilinearity.

**Functoriality.** A smooth map $F : M \to N$ induces (i) pullback on covariant tensor fields, $F^* : \mathcal{T}^{(0,\ell)}(N) \to \mathcal{T}^{(0,\ell)}(M)$ — see [[Def - Pullback of a Covariant Tensor Field]]; (ii) pushforward on contravariant tensor fields *if* $F$ is a diffeomorphism; (iii) full pullback/pushforward on all tensor field types *if* $F$ is a diffeomorphism. The asymmetry is intrinsic: covariant tensors pull back universally, contravariant ones need invertibility of the map.

---

# Relate to Other Fields / Compression

A $(k, \ell)$-tensor field is **the manifold-level lift of a fibrewise mixed-tensor object**, with smoothness. Every concept from [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]] — [[Def - Tensor Product of Vector Spaces|tensor products]], [[Def - Bilinear Form|bilinear forms]], [[Def - Multilinear Form|multilinear forms]] — has a tensor-field version, obtained by applying the linear-algebraic construction to each tangent space and patching smoothly. The patching is automatic because the constructions are functorial in the input vector space.

From the bundle theory side, $\mathcal{T}^{(k,\ell)}(M)$ is the space of sections of an associated bundle: tensor fields are *associated-bundle-section-objects*, parallel to how spinor fields are spin-associated-bundle-sections. The framework generalizes to any representation of $GL(n, \mathbb{R})$ on a vector space, with the tensor case being the family of natural tensor representations.

**True name:** A tensor field is **a $C^\infty(M)$-multilinear gadget on $\mathfrak{X}(M)$ and $\Omega^1(M)$**. Operationally: it eats some vector fields and some 1-forms, returns a smooth function (or, more generally, a tensor field of lower rank), and respects the $C^\infty(M)$-module structure (no derivative terms appear when you pull functions out of slots).

---

# Examples / Corollaries

**Is an instance: any smooth function $f \in C^\infty(M)$ is a $(0, 0)$-tensor field.** The bundle $T^{(0,0)}M = M \times \mathbb{R}$ is trivial; sections are smooth functions.

**Is an instance: any [[Def - Vector Field on a Manifold|vector field]] $X \in \mathfrak{X}(M)$ is a $(1, 0)$-tensor field.** In coordinates, $X = X^i(x)\,\partial_i$, with $X^i \in C^\infty(U)$.

**Is an instance: any [[Def - Covector Field and Differential 1-Form|1-form]] $\omega$ is a $(0, 1)$-tensor field.** In coordinates, $\omega = \omega_j(x)\, dx^j$, with $\omega_j \in C^\infty(U)$.

**Is an instance: a Riemannian metric $g$ is a $(0, 2)$-tensor field.** In coordinates, $g = g_{ij}(x)\, dx^i \otimes dx^j$. It is the standard worked example: the Euclidean metric in polar coordinates has components $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = g_{\theta r} = 0$, smooth functions of $(r, \theta)$. See [[Ex - The Metric Tensor in Polar Coordinates]].

**Is an instance: the Kronecker delta as the identity-as-$(1,1)$-tensor field.** $\delta = \delta^i_j\, \partial_i \otimes dx^j$. The component "function" is constant: $\delta^i_j(x) = \delta^i_j$ for all $x$, in every chart. This is the global identity endomorphism of $TM$. See [[Ex - The Kronecker Delta as a Mixed Tensor]].

**Is an instance: any tensor product $X \otimes \omega$ of a vector field and a 1-form is a $(1, 1)$-tensor field.** In coordinates, $(X \otimes \omega)^i_j = X^i \omega_j$, smoothly varying.

**Is NOT an instance: the Lie bracket $[X, Y]$ viewed as a $(1, 2)$-operation.** It is a multilinear map $\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ in the $\mathbb{R}$-multilinear sense, but it is *not* $C^\infty(M)$-multilinear: $[fX, Y] = f[X, Y] - (Yf)X$. The Lie bracket is therefore *not* a tensor field; it is a *differential operation* on pairs of vector fields.

**Is NOT an instance: the partial derivative $\partial_i f$ viewed as a "$(0, 1)$-tensor".** It is *not* well-defined as a tensor field: in another chart, $\tilde\partial_i f = (\partial x^j / \partial \tilde x^i) \partial_j f$ — which *is* the transformation rule for a 1-form. So actually, $\partial_i f$ *is* the components of the 1-form $df$. The genuine non-tensor in this vein is $\partial_i \partial_j f$ — the second partial derivative, which has a Christoffel-symbol anomaly under change of coordinates and is *not* a $(0, 2)$-tensor field. The correct tensorial second-derivative is the Hessian via a connection, $\nabla\nabla f$, which is $(0, 2)$.

**Corollary (module dimension).** The module $\mathcal{T}^{(k,\ell)}(M)$ over $C^\infty(M)$ is locally free of rank $n^{k+\ell}$. *Proof:* in any chart, the basis tensor fields $\partial_{i_1}\otimes\cdots\otimes dx^{j_\ell}$ form a basis of the module restricted to the chart.

**Corollary (locality).** Tensor field operations are local: if $A = A'$ on an open set $U$, then any tensor field constructed from $A$ agrees with the one constructed from $A'$ on $U$. *Proof:* component functions are local, and tensor field operations are component-by-component.

**Corollary (smoothness preserved).** Sum, $C^\infty(M)$-scalar multiplication, tensor product, contraction, and pullback of smooth tensor fields are smooth.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that the Euclidean metric on $\mathbb{R}^2$ in polar coordinates has components $g_{rr} = 1, g_{\theta\theta} = r^2$ — smooth on the chart $\{r > 0\}$ but not extending to the origin (which is why polar coordinates have a coordinate singularity at $r = 0$); (ii) state the $C^\infty(M)$-multilinearity test for the metric $g$, and verify $g(fX, Y) = f g(X, Y)$; (iii) explain why a constant tensor field on $S^2$ — e.g., $\partial_\theta$ in spherical coordinates extended globally — is *not* well-defined, but a global metric tensor field on $S^2$ *is* well-defined (because the metric is a section of a different bundle whose transition functions cancel the chart-dependence of the components).

---

# Unlocked by This

> [!tip] Riemannian Metric *(from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]])*
> A smooth, symmetric, positive-definite $(0,2)$-tensor field $g$ on $M$. The fundamental object of Riemannian geometry. Existence: every smooth manifold admits a Riemannian metric, via partitions of unity. Once $g$ is fixed, $M$ inherits: lengths of curves, angles between vectors, volume forms, the musical isomorphism, the Levi-Civita connection, geodesics, and the curvature.

> [!tip] Stress-Energy Tensor *(from General Relativity)*
> The **stress-energy tensor** is a symmetric $(0,2)$-tensor field on the spacetime manifold encoding the matter content. Einstein's equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ equate the Einstein tensor (a curvature contraction) with the stress-energy tensor. Both sides are symmetric $(0,2)$-tensor fields, and they transform identically under change of coordinates — manifest tensoriality is what makes general covariance well-defined.

> [!tip] Differential Form *(from [[Differential Geometry VIII — Differential Forms]])*
> A differential $k$-form is an alternating $(0, k)$-tensor field. The forms support extra operations: wedge product, exterior derivative, pullback, integration. The exterior derivative $d$ is *not* $C^\infty(M)$-multilinear (it has a Leibniz rule with a derivative term), so $d$ is not a tensor operation — but $d\omega$ is a tensor field, the *output* of a non-tensorial operation applied to a tensor.

> [!tip] Curvature Tensor *(from Riemannian Geometry)*
> The **Riemann curvature tensor** $R \in \mathcal{T}^{(1,3)}(M)$ is the central tensor field of Riemannian geometry. Defined from a connection $\nabla$ by $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$, and proved $C^\infty(M)$-multilinear in all three slots — *despite* the appearance of the connection (which is not $C^\infty(M)$-linear in $X$) and the Lie bracket (which is not tensorial). The terms conspire to cancel, and the resulting object is a tensor field. This is the prototype of a "curvature is tensorial" argument.
