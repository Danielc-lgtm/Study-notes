---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Tensor Field on a Manifold"
  - "Def - Symmetric and Alternating Bilinear Form"
tags: [geometry, differential-geometry, symmetric-tensors]
---

# Notation

$V$ is a finite-dimensional real vector space. $M$ is a smooth manifold. $S_k$ is the symmetric group on $k$ elements. $\Sigma^k(V^*) \subset T^k(V^*)$ is the subspace of symmetric covariant $k$-tensors on $V$; $\Sigma^k(T^*M)$ is the subbundle of $T^k T^*M$ whose fibre at $p$ is $\Sigma^k(T_p^*M)$. Sections of $\Sigma^k(T^*M)$ are *symmetric covariant $k$-tensor fields*. Components of a symmetric tensor are denoted $\alpha_{(i_1\cdots i_k)}$, where round brackets remind the reader that the indices are unordered. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

The motivating examples are the **inner product** (an $(0, 2)$-tensor field whose value $g(v, w)$ is independent of the order $v, w$), the **stress tensor** in continuum mechanics (a $(0, 2)$-tensor field whose symmetry $\sigma_{ij} = \sigma_{ji}$ encodes conservation of angular momentum), and the **second fundamental form** of an embedded submanifold (a $(0, 2)$-tensor field giving the extrinsic curvature, symmetric because the Hessian is symmetric). All three are tensor fields whose values depend symmetrically on their slots: permuting the inputs does not change the output. The symmetric-tensor-field axioms write down this property and nothing more.

The axiom is a single requirement: $\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = \alpha(v_1, \dots, v_k)$ for every permutation $\sigma \in S_k$. This is a strong condition — it cuts the $n^k$-dimensional space $T^k(V^*)$ down to a $\binom{n+k-1}{k}$-dimensional [[Def - Subspace|subspace]], since a symmetric tensor is determined by its values on *unordered* $k$-tuples of basis vectors, and the number of such unordered tuples is the multinomial coefficient counting multisets.

One could wonder whether the symmetry condition needs to be imposed on *every* permutation, or just on transpositions of adjacent slots. The answer: just transpositions suffice. Any permutation in $S_k$ is a product of transpositions, so if $\alpha$ is unchanged under every transposition then it is unchanged under every permutation. In practice the condition is checked by examining what happens when two specific arguments are swapped, and the rest follows by composition.

One could also ask why we treat symmetric tensors as a *subspace* of all covariant tensors, rather than as a separate algebraic object with its own multiplication. The conceptual reason is that the natural product of two symmetric tensors via the tensor product $\alpha \otimes \beta$ is *not* symmetric in general: it has the symmetric and antisymmetric parts mixed. To stay in $\Sigma^k(V^*)$, one needs the **symmetric product** $\alpha \beta := \mathrm{Sym}(\alpha \otimes \beta)$ — an explicit symmetrization. The reason symmetric tensors and alternating tensors get separate treatments is that they have *different products* (symmetric product vs. wedge product), and these products lead to different algebraic structures (the symmetric algebra $S^\bullet(V^*)$ vs. the exterior algebra $\Lambda^\bullet(V^*)$).

The separation of "symmetric tensor field" from "alternating tensor field" into two distinct definition pages — rather than collapsing them into one — is **deliberate**. Although the definitions are formally parallel (the only change is "symmetric under permutation" vs. "sign-flips under transposition"), the downstream curriculum splits along this line: symmetric tensors are the home of metrics, of quadratic functionals, of Riemannian geometry; alternating tensors are the home of forms, of integration, of de Rham cohomology. The two strands are studied in different chapters and with different tools, so they deserve separate definition pages despite the algebraic parallel.

The manifold-level definition simply requires that the symmetry hold *fibrewise*: a smooth covariant $k$-tensor field is symmetric if $A_p \in \Sigma^k(T_p^*M)$ for every $p$. Smoothness of $A$ is enough; the symmetry is automatic once the values are symmetric at each point. Equivalently, the components $A_{i_1\cdots i_k}(x)$ in any chart are symmetric in the indices: $A_{i_1\cdots i_k} = A_{i_{\sigma(1)}\cdots i_{\sigma(k)}}$ for all permutations $\sigma$.

---

# The Definition

A covariant $k$-tensor $\alpha$ on a finite-dimensional real vector space $V$ is **symmetric** if

$$\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = \alpha(v_1, \dots, v_k) \qquad \text{for every } \sigma \in S_k, \text{ for all } v_1, \dots, v_k \in V.$$

Equivalently, the [[Def - Covariant Tensor on a Vector Space|components]] $\alpha_{i_1\cdots i_k}$ in any basis satisfy $\alpha_{i_1\cdots i_k} = \alpha_{i_{\sigma(1)}\cdots i_{\sigma(k)}}$ for every $\sigma$.

The set of symmetric covariant $k$-tensors on $V$ is denoted $\Sigma^k(V^*) \subset T^k(V^*)$; it is a vector subspace.

**Symmetric tensor field on a manifold.** Let $M$ be a smooth manifold. A **symmetric covariant $k$-tensor field** on $M$ is a smooth covariant $k$-tensor field $A : M \to T^kT^*M$ such that $A_p \in \Sigma^k(T_p^*M)$ for every $p$.

Equivalent characterizations:
1. $A$ is symmetric at every point.
2. The component functions $A_{i_1\cdots i_k}$ in every chart are smooth and symmetric in the indices.
3. The $C^\infty(M)$-multilinear map $\mathfrak{X}(M)^k \to C^\infty(M)$ induced by $A$ is symmetric: $A(X_{\sigma(1)}, \dots, X_{\sigma(k)}) = A(X_1, \dots, X_k)$ for every $\sigma \in S_k$ and every $X_1, \dots, X_k \in \mathfrak{X}(M)$.

The space of smooth symmetric covariant $k$-tensor fields on $M$ is the space of smooth sections of $\Sigma^k(T^*M)$, denoted $\Sigma^k(M)$.

**[[Def - Dimension|Dimension]] of the fibre.** With $n = \dim V$,

$$\dim \Sigma^k(V^*) = \binom{n + k - 1}{k} = \frac{(n + k - 1)!}{k!\,(n-1)!}.$$

For $k = 2$: $\dim \Sigma^2(V^*) = \binom{n+1}{2} = n(n+1)/2$, the dimension of the space of symmetric matrices. For $k = 3, n = 3$: $\binom{5}{3} = 10$. For $k = n$ (top covariant degree): $\binom{2n-1}{n}$, generally much smaller than $n^k$.

**The symmetric product.** For $\alpha \in \Sigma^k(V^*)$ and $\beta \in \Sigma^\ell(V^*)$, their **symmetric product** is

$$\alpha\beta := \mathrm{Sym}(\alpha \otimes \beta) \in \Sigma^{k+\ell}(V^*),$$

where $\mathrm{Sym}$ is the [[Thm - Symmetrization and Alternation Projectors|symmetrization projector]]. The symmetric product is commutative ($\alpha\beta = \beta\alpha$) and associative, making $\Sigma^\bullet(V^*) = \bigoplus_k \Sigma^k(V^*)$ a commutative graded algebra — the **symmetric algebra** $S^\bullet(V^*)$. For two covectors $\alpha, \beta \in V^* = \Sigma^1(V^*)$, the symmetric product is $\alpha\beta = \frac{1}{2}(\alpha \otimes \beta + \beta \otimes \alpha)$.

---

# Categorical / Structural Definition

The space of symmetric tensors is the **invariants** of $T^k(V^*)$ under the natural action of the symmetric group $S_k$:

$$\Sigma^k(V^*) = T^k(V^*)^{S_k} = \{\alpha \in T^k(V^*) : \sigma \cdot \alpha = \alpha \ \forall \sigma \in S_k\},$$

where $S_k$ acts on covariant tensors by $(\sigma \cdot \alpha)(v_1, \dots, v_k) := \alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)})$.

Equivalently, $\Sigma^k(V^*)$ is the image of the symmetrization projector $\mathrm{Sym} : T^k(V^*) \to T^k(V^*)$, $\mathrm{Sym} = \frac{1}{k!}\sum_{\sigma \in S_k} \sigma$. The image of $\mathrm{Sym}$ and the $S_k$-invariants are the same subspace: this is a standard result in the representation theory of finite [[Def - Group|groups]] (averaging over the group action lands in the invariants and fixes them).

The **symmetric algebra** $S^\bullet(V^*) = \bigoplus_k \Sigma^k(V^*)$ has a universal property: it is the free commutative graded algebra generated by $V^*$, with the universal property that for any commutative graded algebra $A^\bullet$, a linear map $V^* \to A^1$ extends uniquely to a graded algebra homomorphism $S^\bullet(V^*) \to A^\bullet$. This is the symmetric-algebra analogue of the [[Thm - Universal Property of the Tensor Product|tensor algebra's universal property]], and it makes $S^\bullet(V^*)$ the home of polynomial functions on $V$.

---

# Relate to Other Fields / Compression

Symmetric covariant 2-tensors are exactly the [[Def - Symmetric and Alternating Bilinear Form|symmetric bilinear forms]] of [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]] §9A. Their study includes [[Def - Quadratic Form|quadratic forms]] (via $q_\alpha(v) = \alpha(v, v)$), [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]], diagonalization, and the signature classification. The transition from "symmetric bilinear form on $V$" to "symmetric $(0,2)$-tensor field on $M$" is the transition from a single vector space to a smoothly varying family — and the resulting object is the **metric tensor**, the foundation of Riemannian and pseudo-Riemannian geometry.

From the algebra side, the symmetric algebra $S^\bullet(V^*) = \bigoplus_k \Sigma^k(V^*)$ is canonically isomorphic to the polynomial algebra $\mathbb{R}[V] = \mathbb{R}[x^1, \dots, x^n]$, with a symmetric $k$-tensor corresponding to a homogeneous polynomial of degree $k$ on $V$. The isomorphism sends $\varepsilon^{i_1}\varepsilon^{i_2}\cdots\varepsilon^{i_k} \in \Sigma^k(V^*)$ to the monomial $x^{i_1}x^{i_2}\cdots x^{i_k}$. So a symmetric covariant $k$-tensor is *literally* a polynomial of degree $k$ in the coordinates, viewed multilinearly.

**True name:** A symmetric covariant $k$-tensor on $V$ is **a homogeneous polynomial of degree $k$ on $V$**, viewed multilinearly (via polarization). The symmetric tensor field analogue on $M$ is a *fibrewise polynomial* — a smooth assignment of a homogeneous polynomial to each tangent space.

---

# Examples / Corollaries

**Is an instance: the Euclidean inner product on $\mathbb{R}^n$.** $g(v, w) = \sum_i v^i w^i$, components $g_{ij} = \delta_{ij}$ (symmetric). Promoted to a tensor field, this is the Euclidean metric on $\mathbb{R}^n$ as a manifold.

**Is an instance: any [[Def - Riemannian Metric|Riemannian metric]] $g$ on $M$.** A smooth, symmetric, positive-definite $(0,2)$-tensor field. The symmetry is *the* defining symmetry property of an inner product, transferred to each tangent space.

**Is an instance: the [[Def - Minkowski Space and the Metric|Minkowski metric]] $\eta$ on $\mathbb{R}^4$.** $\eta = \operatorname{diag}(-1, 1, 1, 1)$ in inertial coordinates. Symmetric in $(\mu, \nu)$. Positive-*indefinite* (signature $(-, +, +, +)$ or $(+, -, -, -)$), so it is a semi-Riemannian rather than Riemannian metric, but symmetric.

**Is an instance: the Cauchy stress tensor $\sigma_{ij}$ in continuum mechanics.** A symmetric $(0, 2)$-tensor field on a body manifold, with $\sigma_{ij} = \sigma_{ji}$ as a consequence of conservation of angular momentum (Cauchy's second law). See [[Ex - The Stress Tensor as a Symmetric 2-Tensor]].

**Is an instance: the second fundamental form of an embedded submanifold.** For an immersed submanifold $i : N \hookrightarrow M$ with normal bundle $\nu$, the second fundamental form $\mathrm{II}$ is a symmetric $(0, 2)$-tensor field on $N$ valued in $\nu$. Its symmetry is the symmetry of the Hessian of the embedding.

**Is an instance: the Ricci tensor $R_{ij}$.** On a Riemannian manifold, the contraction $R_{ij} = R^k_{kij}$ of the Riemann curvature is a symmetric $(0, 2)$-tensor field. (Symmetry is a nontrivial consequence of the Bianchi identities and is *not* immediate from the definition.)

**Is NOT an instance: a generic bilinear form $\beta(v, w) = v^\top M w$ with $M$ non-symmetric.** Take $M = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}$ on $\mathbb{R}^2$. Then $\beta(e_1, e_2) = 1$ but $\beta(e_2, e_1) = 0$, so $\beta$ is bilinear but *not* symmetric.

**Is NOT an instance: the wedge product $\omega \wedge \eta$ of two 1-forms.** This is an *alternating* 2-form: $(\omega \wedge \eta)(v, w) = -(\omega \wedge \eta)(w, v)$. So the wedge product is the *opposite* extreme — see [[Def - Alternating Tensor Field]].

**Corollary (dimension).** $\dim \Sigma^k(V^*) = \binom{n + k - 1}{k}$.

**Corollary (basis).** For a basis $(E_i)$ of $V$ and dual basis $(\varepsilon^j)$, a basis of $\Sigma^k(V^*)$ is given by the symmetrizations $\mathrm{Sym}(\varepsilon^{i_1} \otimes \cdots \otimes \varepsilon^{i_k})$ indexed by *weakly increasing* index tuples $1 \leq i_1 \leq i_2 \leq \cdots \leq i_k \leq n$. The number of such tuples is the multiset coefficient $\binom{n+k-1}{k}$, agreeing with the dimension count.

**Corollary (decomposition for $k = 2$).** $T^2(V^*) = \Sigma^2(V^*) \oplus \Lambda^2(V^*)$, with the projections being $\mathrm{Sym}$ and $\mathrm{Alt}$. *Proof:* every $\beta \in T^2(V^*)$ decomposes uniquely as $\beta = \mathrm{Sym}(\beta) + \mathrm{Alt}(\beta)$, since $\mathrm{Sym}(\beta)(v, w) = \frac{1}{2}(\beta(v,w) + \beta(w,v))$ and $\mathrm{Alt}(\beta)(v, w) = \frac{1}{2}(\beta(v,w) - \beta(w,v))$ sum to $\beta(v, w)$.

**Corollary (no analogous decomposition for $k \geq 3$).** For $k \geq 3$, $T^k(V^*) \supsetneq \Sigma^k(V^*) \oplus \Lambda^k(V^*)$ — there are tensors that vanish under both $\mathrm{Sym}$ and $\mathrm{Alt}$. They live in the "mixed Young tableau" components, which are needed to span the full tensor space and have their own (non-trivial) representation-theoretic structure.

**Calibration check.** If you have understood the definition, you should be able to: (i) write down a basis of $\Sigma^2(\mathbb{R}^3{}^*)$ and verify it has 6 elements ($n(n+1)/2 = 6$ for $n = 3$); (ii) verify that the Riemannian metric in polar coordinates, $g = dr \otimes dr + r^2\, d\theta \otimes d\theta$, equals its symmetrization (the cross terms $dr \otimes d\theta + d\theta \otimes dr$ vanish, so $g$ is already symmetric); (iii) compute the symmetric product $dx\, dy = \frac{1}{2}(dx \otimes dy + dy \otimes dx)$ on $\mathbb{R}^2$ and verify it is symmetric.

---

# Unlocked by This

> [!tip] Riemannian Metric *(from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]])*
> A smooth, symmetric, **positive-definite** $(0,2)$-tensor field. Positive-definiteness — $g_p(v, v) > 0$ for $v \neq 0$ — is the extra condition that promotes a symmetric $(0,2)$-tensor field into a metric. Existence: partition-of-unity argument. The metric is *the* central object of Riemannian geometry: lengths, angles, volume, the musical isomorphism, the Levi-Civita connection, geodesics, curvature.

> [!tip] Semi-Riemannian / Lorentzian Manifold *(from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]])*
> Drop positive-definiteness, demand only nondegeneracy ($g_p(v, w) = 0$ for all $w$ implies $v = 0$). Then $g$ has a fixed signature at each point. Lorentzian signature $(-, +, +, +)$ (Lee) or $(+, -, -, -)$ (physics) is the case relevant to general relativity, and Minkowski space is its prototype. The *symmetric* part of the structure is the same as in the Riemannian case; what changes is the positivity condition.

> [!tip] Stress-Energy Tensor *(from General Relativity)*
> The **stress-energy tensor** $T_{\mu\nu}$ in general relativity is a symmetric $(0,2)$-tensor field, packaging energy density, momentum density, and stress into one tensorial object. Its symmetry encodes conservation of angular momentum and the absence of intrinsic-spin contributions in classical GR. Einstein's field equations equate $T_{\mu\nu}$ (symmetric) with the Einstein tensor $G_{\mu\nu}$ (also symmetric), and the matching of types is what makes GR a well-defined tensorial field theory.

> [!tip] The Polynomial Ring as a Symmetric Algebra *(from Commutative Algebra)*
> The symmetric algebra $S^\bullet(V^*) = \bigoplus_k \Sigma^k(V^*)$ is canonically isomorphic to the polynomial ring $\mathbb{R}[V] = \mathbb{R}[x^1, \dots, x^n]$. So a symmetric tensor of rank $k$ "is" a homogeneous polynomial of degree $k$ on $V$. The polarization identity inverts this: a homogeneous polynomial recovers its associated symmetric tensor by the formula $\alpha(v_1, \dots, v_k) = \frac{1}{k!}\sum_\sigma p(v_{\sigma(1)} + \cdots + v_{\sigma(k)}) \pm$ correction terms.
