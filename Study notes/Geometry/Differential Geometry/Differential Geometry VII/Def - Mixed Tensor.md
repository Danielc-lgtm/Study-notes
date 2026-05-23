---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Contravariant Tensor on a Vector Space"
  - "Def - Tensor Product of Vector Spaces"
  - "Def - Linear Map"
  - "Def - Dual Space"
tags: [geometry, differential-geometry, multilinear-algebra]
---

# Notation

$V$ is a finite-dimensional real vector space, $\dim V = n$, with dual $V^*$ and bases $(E_i), (\varepsilon^j)$. The space of mixed tensors of type $(k, \ell)$ on $V$ is denoted $T^{(k,\ell)}(V)$; equivalently $V^{\otimes k} \otimes (V^*)^{\otimes \ell}$. Components have $k$ upper indices (contravariant) and $\ell$ lower indices (covariant): $W^{i_1\cdots i_k}_{j_1\cdots j_\ell}$. Einstein summation is in force. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

**Standing convention — index order.** In $W^{i_1\cdots i_k}_{j_1\cdots j_\ell}$, upper indices come before lower indices, separated only by an offset. Lee's convention ($T^{(k,\ell)} = V^{\otimes k} \otimes (V^*)^{\otimes \ell}$, $k$ for contravariant first) is followed here; Frankel and many physics texts use $T^{k}_{\ell}$ with the *same* meaning, but some texts swap the roles of $k$ and $\ell$. We always have: **upper = contravariant, lower = covariant**, regardless of which comes first in the notation. The reader who encounters a foreign text should check the convention before interpreting indices.

> [!warning] Convention: $(k, \ell)$ vs $(\ell, k)$
> Lee's $T^{(k,\ell)}(V) = V^{\otimes k} \otimes (V^*)^{\otimes \ell}$ ("$k$ contravariant, $\ell$ covariant"). Some texts (including Lee's first edition) reverse this. **The reliable rule is to read the index positions, not the symbol $(k, \ell)$.** Upper indices = contravariant slots = pair with covectors. Lower indices = covariant slots = pair with vectors.

---

# Axiom Motivation

The thing being axiomatized is **a multilinear gadget that takes some vectors and some covectors as input and produces a number**. The motivating examples cover every kind of object we will encounter that is *not* purely covariant or purely contravariant.

The most basic example is a **linear map** $A : V \to V$. A linear map eats a vector and produces a vector; equivalently — using $W \cong T^1(W) \subset $ functionals on $W^*$ — it can be viewed as a function $W_A : V^* \times V \to \mathbb{R}$, $W_A(\omega, v) := \omega(Av)$. This $W_A$ is linear in $\omega$ (because $\omega$ enters linearly) and linear in $v$ (because $A$ is linear and $\omega$ is linear). So a linear map *is* a multilinear gadget with one covector slot and one vector slot — a mixed tensor of type $(1, 1)$. The Kronecker delta $\delta^i_j$, which has $W_{\mathrm{id}}(\omega, v) = \omega(v)$, is the identity-as-mixed-tensor; its components are $\delta^i_j = 1$ if $i = j$, else $0$, in *every* basis.

This observation is the secret reason mixed tensors matter. A purely covariant $k$-tensor is a "$k$-input gadget"; a purely contravariant $k$-tensor is a "$k$-output gadget"; but most objects in differential geometry have *both* inputs and outputs. A linear map takes vectors in and gives vectors out — its native type is $(1, 1)$. The Riemann curvature tensor takes three vectors in and gives one vector out — its native type is $(1, 3)$. The cofactor matrix in linear algebra, the structure constants of a Lie algebra ($c^k_{ij}$ with one upper and two lower indices), the metric connection's Christoffel symbols (one upper, two lower — though they are *not* tensors!) all naturally have mixed type. The mixed-tensor definition captures all of these in one framework.

The axiom is again multilinearity, now in slots of two different kinds. The contravariant slots accept covectors and produce values linearly in each covector; the covariant slots accept vectors and produce values linearly in each vector. The two kinds of slot must be tracked separately, because a contravariant slot transforms with the Jacobian under change of coordinates (i.e., behaves like a vector index) while a covariant slot transforms with the inverse Jacobian (covector-like). The structural reason — that a contravariant slot is "really" a vector, and a covariant slot is "really" a covector — is captured in the canonical isomorphism $T^{(k,\ell)}(V) \cong V^{\otimes k} \otimes (V^*)^{\otimes \ell}$ (in finite [[Def - Dimension|dimensions]]).

One could ask whether mixed tensors really need to be different from covariant ones. The argument *against* the distinction is that, given a basis, we can identify $V \cong V^*$ via $E_i \leftrightarrow \varepsilon^i$, converting a mixed tensor into a purely covariant one. The argument *for* the distinction is that this identification depends on the choice of basis — it is **not coordinate-invariant**, and it does *not* survive change of basis. A linear map $A$ has components $A^i_j$ that transform as $\tilde A^i_j = \frac{\partial \tilde x^i}{\partial x^a}\frac{\partial x^b}{\partial \tilde x^j} A^a_b$ — one Jacobian factor up, one inverse-Jacobian factor down. A purely covariant 2-tensor (like the metric) has components $g_{ij}$ that transform with *two* inverse-Jacobian factors. The transformations are genuinely different, and only a structure (a metric, in the manifold setting) lets you raise or lower indices.

The decision to keep $(k, \ell)$ as separate type indices — and to refuse to identify them — is **load-bearing for the entire chapter**. Every diagnostic ("is this object well-defined as a tensor of type $(k, \ell)$?") depends on tracking the variances correctly, and the transformation rule [[Thm - Transformation Rule for Tensor Components]] is the gauge of legality.

---

# The Definition

A **mixed tensor of type $(k, \ell)$** on a finite-dimensional real vector space $V$ is a multilinear function

$$W : \underbrace{V^* \times \cdots \times V^*}_{k \text{ slots}} \times \underbrace{V \times \cdots \times V}_{\ell \text{ slots}} \to \mathbb{R},$$

linear in each slot when the others are held fixed. The first $k$ slots accept covectors and are the **contravariant** slots; the last $\ell$ slots accept vectors and are the **covariant** slots.

The space of mixed tensors of type $(k, \ell)$ on $V$ is denoted

$$T^{(k,\ell)}(V) := V^{\otimes k} \otimes (V^*)^{\otimes \ell}.$$

In finite dimensions, this is canonically isomorphic to the space of multilinear functions above, with the elementary tensor

$$v_1 \otimes \cdots \otimes v_k \otimes \omega^1 \otimes \cdots \otimes \omega^\ell$$

corresponding to the multilinear functional $(\eta^1, \dots, \eta^k, u_1, \dots, u_\ell) \mapsto \eta^1(v_1)\cdots\eta^k(v_k)\omega^1(u_1)\cdots\omega^\ell(u_\ell)$.

**Special cases:**
- $T^{(0,0)}(V) = \mathbb{R}$.
- $T^{(1,0)}(V) = V$ (contravariant 1-tensors are vectors).
- $T^{(0,1)}(V) = V^*$ (covariant 1-tensors are covectors).
- $T^{(k,0)}(V) = T^k(V)$ (purely [[Def - Contravariant Tensor on a Vector Space|contravariant]] $k$-tensors).
- $T^{(0,\ell)}(V) = T^\ell(V^*)$ (purely [[Def - Covariant Tensor on a Vector Space|covariant]] $\ell$-tensors).
- $T^{(1,1)}(V) \cong \mathcal{L}(V, V)$, the space of [[Def - Linear Map|linear maps]] $V \to V$, via the identification $A \leftrightarrow W_A(\omega, v) := \omega(Av)$.

**Components.** Given a basis $(E_i)$ of $V$ and dual basis $(\varepsilon^j)$ of $V^*$, the components of $W \in T^{(k,\ell)}(V)$ are

$$W^{i_1\cdots i_k}_{j_1\cdots j_\ell} := W(\varepsilon^{i_1}, \dots, \varepsilon^{i_k}, E_{j_1}, \dots, E_{j_\ell}).$$

These are $n^{k+\ell}$ real numbers, the *full data* of $W$ in the chosen basis. The expansion in the basis-induced basis of $T^{(k,\ell)}(V)$ is

$$W = W^{i_1\cdots i_k}_{j_1\cdots j_\ell}\, E_{i_1}\otimes\cdots\otimes E_{i_k}\otimes \varepsilon^{j_1}\otimes\cdots\otimes\varepsilon^{j_\ell}.$$

**Dimension.** $\dim T^{(k,\ell)}(V) = n^{k+\ell}$.

---

# Categorical / Structural Definition

The categorical content is the combined universal property of $V^{\otimes k} \otimes (V^*)^{\otimes \ell}$. By the [[Thm - Universal Property of the Tensor Product|universal property]] applied $k + \ell$ times, multilinear maps $V^* \times \cdots \times V^* \times V \times \cdots \times V \to \mathbb{R}$ (a covector slot or a vector slot per factor) correspond to linear maps out of $V^{\otimes k} \otimes (V^*)^{\otimes \ell}$. The space $T^{(k,\ell)}(V)$ is the representing object for this multilinear functor.

**Functoriality.** A linear map $L : V \to W$ induces actions on mixed tensors that go in *both* directions, depending on the slot. The contravariant slots push forward (with $L$), the covariant slots pull back (with $L^*$). In general, when $L$ is not invertible, this does not give a well-defined action on the whole mixed tensor — only the purely covariant part can be pulled back (so a $(0, \ell)$-tensor pulls back unconditionally), and only the purely contravariant part can be pushed forward (a $(k, 0)$-tensor pushes forward). For a genuine mixed tensor with $k, \ell \geq 1$, the action exists only when $L$ is an **isomorphism** (linear in the algebraic setting, [[Def - Diffeomorphism|diffeomorphism]] in the manifold setting).

This is precisely why pullback in [[Def - Pullback of a Covariant Tensor Field]] is restricted to covariant tensor fields, and why the more flexible notion of pulling back mixed tensor fields requires the map to be a diffeomorphism.

---

# Relate to Other Fields / Compression

A mixed tensor of type $(k, \ell)$ is a **multi-input, multi-output multilinear gadget** with $k$ "outputs" (the contravariant slots, since they pair with covectors which are the natural test functionals on $V$) and $\ell$ "inputs" (the covariant slots, vectors). Or equivalently: $\ell$ inputs and $k$ outputs. The matrix of a linear map $A : V \to V$ is a $(1, 1)$-tensor — one slot in, one slot out — exactly because $A$ has one input slot (a vector) and one output (a vector); the multilinear functional $W_A(\omega, v) = \omega(Av)$ packages "input $v$, output $Av$" as a single multilinear gadget.

From the LA IX viewpoint, a mixed tensor is an element of $V^{\otimes k} \otimes (V^*)^{\otimes \ell}$. The covariant and contravariant pieces multiply by [[Def - Tensor Product of Vector Spaces|tensor product]]; the entire space of mixed tensors of *all* types $\bigoplus_{k, \ell \geq 0} T^{(k,\ell)}(V)$ forms a graded algebra — the **mixed tensor algebra** of $V$. Restricting to the bigrading and the tensor product, we get a bigraded algebra where multiplication respects the bigrading: $T^{(k_1, \ell_1)} \otimes T^{(k_2, \ell_2)} \to T^{(k_1+k_2, \ell_1+\ell_2)}$.

**True name:** A $(k, \ell)$-tensor is **an element of $V^{\otimes k} \otimes (V^*)^{\otimes \ell}$**, equivalently a multilinear functional eating $k$ covectors and $\ell$ vectors. Operationally: $k$ upper indices, $\ell$ lower indices. A linear map is a $(1, 1)$-tensor; the metric is a $(0, 2)$-tensor; the Riemann curvature is a $(1, 3)$-tensor; the Riemann curvature with the index lowered is a $(0, 4)$-tensor.

---

# Examples / Corollaries

**Is an instance: a vector $v \in V$ is a $(1, 0)$-tensor.** Eats one covector $\omega$ and gives $\omega(v) \in \mathbb{R}$.

**Is an instance: a covector $\omega \in V^*$ is a $(0, 1)$-tensor.** Eats one vector $v$ and gives $\omega(v)$.

**Is an instance: a linear map $A : V \to V$ is a $(1, 1)$-tensor.** Via $W_A(\omega, v) = \omega(Av)$. In a basis $A(E_j) = A^i_j E_i$, and the components of $W_A$ are $W_A(\varepsilon^i, E_j) = \varepsilon^i(A E_j) = \varepsilon^i(A^k_j E_k) = A^k_j \delta^i_k = A^i_j$ — the *matrix entries of $A$*. So the matrix of a linear map *is* the component array of its associated $(1, 1)$-tensor.

**Is an instance: the identity map's tensor — the Kronecker delta $\delta^i_j$.** $W_{\mathrm{id}}(\omega, v) = \omega(v)$, with components $\delta^i_j = \varepsilon^i(E_j)$. The remarkable fact is that the components are **the same in every basis**, $\delta^i_j$. This is the only mixed tensor with that property: it is fixed under all changes of basis. See [[Ex - The Kronecker Delta as a Mixed Tensor]].

**Is an instance: a bilinear form $\beta(v, w)$ on $V$ is a $(0, 2)$-tensor.** Components $\beta_{ij}$. The metric is the prototypical example.

**Is an instance: the inverse metric $g^{ij}$ is a $(2, 0)$-tensor.** Components are the inverse matrix to the metric's; the inverse metric eats two covectors and is the bilinear form on $V^*$ that pairs covectors via the metric.

**Is an instance: the structure constants of a Lie algebra, $c^k_{ij}$.** With $[E_i, E_j] = c^k_{ij} E_k$ in a basis of the Lie algebra. These are a $(1, 2)$-tensor under change of basis of the Lie algebra; under change of *coordinate basis* on a manifold (when the Lie algebra is $\mathfrak{g}$ for a Lie [[Def - Group|group]] $G$), they remain $(1, 2)$-tensorial because the structure constants are intrinsic to $\mathfrak{g}$.

**Is NOT an instance: the Christoffel symbols $\Gamma^k_{ij}$.** Despite having the index structure of a $(1, 2)$-tensor, the Christoffel symbols are *not* tensorial — their transformation rule has an extra term: $\tilde\Gamma^k_{ij} = \frac{\partial \tilde x^k}{\partial x^a}\frac{\partial x^b}{\partial \tilde x^i}\frac{\partial x^c}{\partial \tilde x^j} \Gamma^a_{bc} + \frac{\partial \tilde x^k}{\partial x^a}\frac{\partial^2 x^a}{\partial \tilde x^i \partial \tilde x^j}$. The second term is the **anomalous term** that disqualifies $\Gamma$ as a tensor: a true tensor's transformation has only one term, with no second derivatives. The Christoffel symbols define a *connection*, which is a more general notion than a tensor; the difference of two connections, however, *is* a tensor.

**Is NOT an instance: a bilinear functional $V \times V^* \to \mathbb{R}$ that takes the vector slot and the covector slot in a fixed order.** This is a $(1, 1)$-tensor *modulo ordering convention*. Lee writes the covector slot first, the vector slot second; physics papers often use the opposite. The two are isomorphic as vector spaces but careless ordering will reverse upper and lower indices in components, with disastrous consequences for any subsequent contraction.

**Corollary (dimension).** $\dim T^{(k,\ell)}(V) = n^{k + \ell}$.

**Corollary ($T^{(1,1)}(V) \cong \mathcal{L}(V, V)$).** The map $A \mapsto W_A$ is a vector-space isomorphism between linear self-maps of $V$ and $(1, 1)$-tensors on $V$. This identifies "matrices" with "$(1,1)$-tensors", and is the algebraic reason mixed-type tensors appear everywhere linear maps do.

**Calibration check.** If you have understood the definition, you should be able to: (i) write down the components of the projection $P : \mathbb{R}^2 \to \mathbb{R}^2$, $P(x, y) = (x, 0)$, as a $(1, 1)$-tensor and identify them with the matrix $\begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}$; (ii) verify that the Kronecker delta $\delta^i_j$ has the same components $\delta^i_j$ in every basis of $V$; (iii) explain why the trace $\mathrm{tr}(A) = A^i_i$ (summed) is a well-defined invariant of the $(1, 1)$-tensor (a contraction, by anticipation of [[Def - Contraction of a Tensor]]), independent of basis.

---

# Unlocked by This

> [!tip] Tensor Field of Mixed Type *(from [[Differential Geometry VII — Tensors and Tensor Fields]])*
> A smoothly varying assignment of a $(k, \ell)$-tensor to each tangent space. The framework includes vector fields ($(1,0)$), 1-forms ($(0,1)$), endomorphism fields ($(1,1)$), the metric ($(0,2)$), and the curvature tensor ($(1,3)$).

> [!tip] The Riemann Curvature Tensor *(from Riemannian Geometry)*
> The **Riemann curvature tensor** $R \in T^{(1,3)}(M)$, defined by $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]}Z$, is the central object of Riemannian geometry. Its three covariant slots eat vectors $X, Y, Z$ and its one contravariant slot returns a vector $R(X, Y)Z$. The mixed type is essential: the curvature is an operator-valued multilinear gadget, and the operator-output is exactly what the contravariant slot encodes. Lowering the contravariant index with the metric gives the symmetric $(0, 4)$-tensor $R_{abcd} = g_{ae}R^e_{bcd}$.

> [!tip] Index Gymnastics and the Musical Isomorphism *(from Riemannian Geometry)*
> On a manifold with metric $g$, the **musical isomorphism** $\flat : TM \to T^*M$ and its inverse $\sharp : T^*M \to TM$ let you convert covariant indices to contravariant and vice versa: $T^a{}_b \mapsto T_{ab} = g_{ac} T^c{}_b$ ("lowering an index"), $T^a{}_b \mapsto T^{ab} = T^a{}_c g^{cb}$ ("raising an index"). The whole physicist's index-shuffling repertoire is the application of $\flat$ and $\sharp$ to specific slots of a mixed tensor. Different positions of indices on the "same" tensor correspond to different mixed types — they encode the same geometric information, but with different functorial behaviour.

> [!tip] The Stress-Energy Tensor and Conservation Laws *(from General Relativity)*
> The **stress-energy tensor** $T^{\mu\nu}$ in GR is a contravariant $(2, 0)$-tensor (with two upper indices) or, equivalently, $T^\mu{}_\nu$ as $(1, 1)$ (with one each), or $T_{\mu\nu}$ as $(0, 2)$ — the three forms encode the same physics but in different functorial roles. Conservation $\nabla_\mu T^{\mu\nu} = 0$ is most naturally stated with the contravariant form, while Einstein's equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ matches both sides as $(0,2)$ symmetric tensors. The flexibility to move indices is what makes the metric and the tensor framework work together.
