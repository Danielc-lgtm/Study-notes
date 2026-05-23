---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Tangent Space"
  - "Def - Derivation at a Point"
  - "Def - Linear Map"
tags: [geometry, differential-geometry]
---

# Notation

$M$ and $N$ are [[Def - Smooth Manifold|smooth manifolds]], $F : M \to N$ is a [[Def - Smooth Map between Manifolds|smooth map]], and $p \in M$. The tangent spaces are $T_{p}M$ at $p \in M$ and $T_{F(p)}N$ at $F(p) \in N$, see [[Def - The Tangent Space]]. We use $v \in T_{p}M$ for a tangent vector at $p$ and $f \in C^{\infty}(N)$ for a smooth function on $N$. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

The motivation is to manufacture a linear map between tangent spaces from a smooth map between manifolds — the manifold analogue of the [[Def - The Total Derivative and Differentiability|total derivative]]. In multivariate analysis, a smooth map $\hat{F} : \mathbb{R}^{m} \to \mathbb{R}^{n}$ has a total derivative $D\hat{F}_{a} : \mathbb{R}^{m} \to \mathbb{R}^{n}$ at every $a$, which is the best linear approximation to $\hat{F}$ near $a$, represented by the Jacobian matrix. We want the same construction on manifolds, but without depending on a choice of chart.

Here is the situation. We have a smooth map $F : M \to N$ and a point $p \in M$. We want a linear map $dF_{p} : T_{p}M \to T_{F(p)}N$. A tangent vector $v \in T_{p}M$ is a derivation at $p$ — a linear map $v : C^{\infty}(M) \to \mathbb{R}$ satisfying the Leibniz rule. We need to define what $dF_{p}(v)$ is, i.e., specify a derivation at $F(p) \in N$ — a linear map $C^{\infty}(N) \to \mathbb{R}$ satisfying the Leibniz rule at $F(p)$.

The key insight is that there is a *natural* way to turn a function on $N$ into a function on $M$: precompose with $F$. If $f : N \to \mathbb{R}$ is smooth then $f \circ F : M \to \mathbb{R}$ is smooth. So we can ask the derivation $v$ at $p$ to act on $f \circ F$, getting a real number $v(f \circ F)$. Define
$$(dF_{p}(v))(f) = v(f \circ F).$$
This is the only natural construction available — it routes through the only operation that converts a function on $N$ into a function on $M$.

Let us verify that this construction does what we want. First, $dF_{p}(v)$ as a function of $f$ is **linear**: $(dF_{p}(v))(\alpha f + \beta g) = v((\alpha f + \beta g) \circ F) = v(\alpha\,(f \circ F) + \beta\,(g \circ F)) = \alpha\,v(f \circ F) + \beta\,v(g \circ F) = \alpha\,(dF_{p}(v))(f) + \beta\,(dF_{p}(v))(g)$. Second, it satisfies the **Leibniz rule at $F(p)$**: $(dF_{p}(v))(fg) = v((fg) \circ F) = v((f \circ F)(g \circ F)) = (f \circ F)(p) \cdot v(g \circ F) + (g \circ F)(p) \cdot v(f \circ F) = f(F(p)) \cdot (dF_{p}(v))(g) + g(F(p)) \cdot (dF_{p}(v))(f)$. Both checks are immediate from the corresponding properties of $v$ — no surprises.

Third, $dF_{p}$ as a function of $v$ is **linear**: $(dF_{p}(v_{1} + v_{2}))(f) = (v_{1} + v_{2})(f \circ F) = v_{1}(f \circ F) + v_{2}(f \circ F) = (dF_{p}(v_{1}))(f) + (dF_{p}(v_{2}))(f)$. Similarly for scalar multiplication. So $dF_{p} : T_{p}M \to T_{F(p)}N$ is a linear map between vector spaces, as desired.

Why is this the *right* definition? Several converging reasons. (a) When $M$ and $N$ are open subsets of Euclidean spaces, $dF_{p}$ coincides with the total derivative $DF_{p}$ (after identifying tangent spaces with $\mathbb{R}^{n}$), so the manifold definition specializes correctly. (b) The chain rule $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ falls out immediately from the associativity of composition, since $(f \circ (G \circ F)) = ((f \circ G) \circ F)$. (c) The differential of the identity is the identity: $(d(\mathrm{id})_{p}(v))(f) = v(f \circ \mathrm{id}) = v(f)$, so $d(\mathrm{id})_{p} = \mathrm{id}_{T_{p}M}$. (d) For a diffeomorphism, $dF_{p}$ is an isomorphism with inverse $d(F^{-1})_{F(p)}$. Each of these properties — specialization, chain rule, identity, invertibility — is *forced* by the precomposition definition. No other natural construction has all four.

Why not define $dF_{p}$ via the curve picture instead, by $dF_{p}([\gamma]) = [F \circ \gamma]$? This works (and is equivalent by [[Thm - Equivalence of Tangent Vector Definitions]]), and is geometrically more intuitive. But it requires proving that the pushforward of curves respects the equivalence relation $\sim$ before the linear-map structure becomes visible. The derivation definition gives linearity and the chain rule for free.

Why not define $dF_{p}$ via the chart-tuple picture, as the Jacobian matrix? This is the working physicist's definition, but it requires proving chart-independence — that the Jacobian transforms correctly under change of chart by the multivariate chain rule. The abstract derivation definition makes coordinate-independence manifest: there are no coordinates in the definition.

A reader who has never seen the differential could invent it by the following route. Recognize that a smooth map $F : M \to N$ should induce a linear map between tangent spaces. Notice that the only natural operation converting $C^{\infty}(N) \to C^{\infty}(M)$ is precomposition with $F$. Define the differential by passing precomposition through the derivation. Verify that linearity, the chain rule, and Leibniz come for free. The crucial moment is recognizing precomposition as the natural construction — and "natural" here is in the precise categorical sense: precomposition is the dual map $F^{*}$ in the contravariant function-space functor, and the differential is its transpose in the tangent functor.

---

# The Definition

Let $F : M \to N$ be a smooth map between smooth manifolds and let $p \in M$. The **differential** of $F$ at $p$ is the linear map
$$dF_{p} : T_{p}M \to T_{F(p)}N$$
defined by
$$(dF_{p}(v))(f) = v(f \circ F)$$
for $v \in T_{p}M$ and $f \in C^{\infty}(N)$.

**Equivalent definitions (via the [[Thm - Equivalence of Tangent Vector Definitions|equivalence theorem]]):**

- **Curve picture:** $dF_{p}([\gamma]) = [F \circ \gamma]$.
- **Coordinate picture:** if $(U, \varphi)$ and $(V, \psi)$ are charts around $p$ and $F(p)$ with coordinates $x^{i}$ and $y^{j}$, and $\hat{F} = \psi \circ F \circ \varphi^{-1}$ is the coordinate representative, then
$$dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right) \;=\; \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)) \, \left.\frac{\partial}{\partial y^{j}}\right|_{F(p)}.$$
The matrix of $dF_{p}$ in coordinate bases is the **Jacobian matrix** of $\hat{F}$ at $\varphi(p)$.

**Properties (proved in [[Thm - Chain Rule for the Differential]] and the exercises):**

1. $dF_{p}$ is linear.
2. **Chain rule:** $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$.
3. **Identity:** $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$.
4. If $F$ is a [[Def - Diffeomorphism|diffeomorphism]], then $dF_{p}$ is a linear isomorphism with $(dF_{p})^{-1} = d(F^{-1})_{F(p)}$.

The **global differential** $dF : TM \to TN$ is the map whose restriction to each tangent space $T_{p}M$ is $dF_{p}$; it is smooth, see [[Thm - The Tangent Bundle is a Smooth Manifold]].

The differential is also called the **pushforward** (because it pushes tangent vectors from the domain to the codomain), the **tangent map**, or the **derivative** of $F$ at $p$. Common alternative notations: $F_{*p}$, $TF$, $T_{p}F$, $DF(p)$. We standardize on $dF_{p}$.

---

# Categorical / Structural Definition

The differential is the **morphism map** of the tangent-space functor $T : \mathrm{Diff}_{*} \to \mathrm{Vec}_{\mathbb{R}}$. We unpack what this means.

We have already seen (in [[Def - The Tangent Space]]) that $T_{p}M$ is the object map of a covariant functor from pointed smooth manifolds to real vector spaces. The differential $dF_{p}$ is the corresponding morphism map: given a morphism in $\mathrm{Diff}_{*}$ — a pointed smooth map $F : (M, p) \to (N, F(p))$ — the functor produces a morphism in $\mathrm{Vec}_{\mathbb{R}}$, the linear map $dF_{p} : T_{p}M \to T_{F(p)}N$.

The two functor axioms — preservation of identities and composition — are exactly the chain rule and identity properties:
- $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$ (identities go to identities);
- $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ (composition is preserved).

Together they say: **the assignment $F \mapsto dF_{p}$ is functorial in $F$**.

The proof of the chain rule from the precomposition definition is, as observed in the Axiom Motivation, a one-line consequence of the associativity of composition. The proof of the identity property is also one line. So the precomposition definition was *chosen* to make functoriality immediate.

The categorical viewpoint also lets us speak cleanly about the **global differential** as a functor in its own right. The assignment $M \mapsto TM$, $F \mapsto dF$ is a covariant functor $T : \mathrm{Diff} \to \mathrm{Diff}$ from smooth manifolds to smooth manifolds. This functor extends the tangent-space construction: it forgets the marked point but remembers the bundle structure. Higher iterates $T \circ T$ yield jet bundles, the natural setting for higher-order calculus.

**Why care?** Three reasons.

First, the functor viewpoint guarantees that the differential is *natural*: any construction defined purely in terms of $T_{p}M$ and $dF_{p}$ — vector fields, flows, the Lie bracket, the differential of a 1-form — is automatically coordinate-independent. Coordinate-independence is the technical heart of differential geometry, and naturality is its categorical packaging.

Second, the functor viewpoint exposes the relationship between $dF_{p}$ and other "linearization at a point" functors: the cotangent functor $T^{*}$ (contravariant — covectors pull back), the Kähler differentials in algebraic geometry, the Lie algebra functor on Lie groups, the Zariski tangent space functor. All these are different incarnations of the same idea, and the same categorical apparatus governs them.

Third, the functor viewpoint makes the proof of the chain rule trivial. The category-theoretic statement "$T$ is a functor" packages the chain rule, the identity rule, and the coordinate-independence into a single line. This is one of the cleanest illustrations of category theory's organizing power.

---

# Relate to Other Fields / Compression

In **multivariate analysis**, the differential $dF_{p}$ between tangent spaces of manifolds is *literally* the [[Def - The Total Derivative and Differentiability|total derivative]] computed in any chart and verified to be coordinate-independent. Concretely, if $M$ and $N$ are open subsets of Euclidean spaces, $T_{p}M = \mathbb{R}^{m}$ and $T_{F(p)}N = \mathbb{R}^{n}$ canonically, and $dF_{p}$ becomes the total derivative $DF_{p}$ from [[Def - The Total Derivative and Differentiability]]. The Jacobian matrix from [[Def - Partial Derivatives and the Jacobian Matrix]] is precisely the matrix of $dF_{p}$ in coordinate bases. The manifold construction is the chart-independent packaging of multivariate calculus.

**True name:** The differential $dF_{p}$ is "the Jacobian of $F$ at $p$, made coordinate-independent". Every computation of $dF_{p}$ either is done in coordinates (where the answer is a Jacobian matrix) or uses the curve recipe $dF_{p}(v) = (F \circ \gamma)'(0)$ (which is a one-variable derivative). The abstract derivation definition is what makes the result chart-invariant, but it is not what you compute with.

The construction generalizes to **infinite-dimensional manifolds** modelled on Banach spaces, with the differential becoming a bounded linear operator between Banach spaces — the **Fréchet derivative** between tangent spaces. The whole apparatus survives in infinite dimensions provided one is careful with boundedness and continuity.

In **physics**, the differential is the *velocity push-forward*: if a particle in $M$ has worldline $\gamma$ with velocity $\gamma'(0) = v \in T_{p}M$, and $F : M \to N$ is a coordinate transformation or a physical map, then the velocity of the transformed worldline at the transformed point is $dF_{p}(v) = (F \circ \gamma)'(0) \in T_{F(p)}N$. The differential is the "Galilean transformation of velocity" in the geometric language. In special relativity, the differential of a Lorentz transformation $\Lambda : \mathbb{R}^{4} \to \mathbb{R}^{4}$ is $\Lambda$ itself (the differential of a linear map is the map), so four-velocities transform under $\Lambda$ exactly as the spacetime coordinates do — this is the operational content of [[Def - Four-Vector|four-vector]] transformation laws.

In **category theory**, the differential is the morphism map of the tangent functor $T_{p}$, which has many cousins: the cotangent functor (contravariant), the de Rham functor (taking smooth manifolds to graded algebras), the Hochschild homology functor (taking algebras to chain complexes). All are "linearization at a point" or "linearization globally" functors, and the differential is the simplest case.

---

# Examples / Corollaries

**The differential of a linear map between vector spaces is itself.** If $V, W$ are finite-dimensional vector spaces and $L : V \to W$ is linear (hence smooth), then for any $a \in V$, $dL_{a} : T_{a}V \to T_{La}W$ is — via the identifications $T_{a}V \cong V$ and $T_{La}W \cong W$ from [[Def - The Tangent Space]] — equal to $L$ itself. This generalizes the fact that the total derivative of a linear map is the map.

**The differential of a constant map is zero.** If $F : M \to N$ is constant, $F \equiv q$ for some $q \in N$, then for any $f \in C^{\infty}(N)$, $f \circ F$ is the constant function $f(q)$, so $v(f \circ F) = 0$ by the constants-are-annihilated property of derivations. Hence $dF_{p}(v) = 0$ for every $v$.

**The differential of the identity is the identity.** $d(\mathrm{id}_{M})_{p}(v))(f) = v(f \circ \mathrm{id}) = v(f)$, so $d(\mathrm{id}_{M})_{p}(v) = v$. This is the "identity goes to identity" axiom of functoriality.

**Computing $dF_{p}$ in coordinates.** Let $F : \mathbb{R}^{2} \to \mathbb{R}^{3}$ be $F(x, y) = (x^{2}, xy, e^{y})$. At $p = (1, 0)$:
$$dF_{p} = D F(1, 0) = \begin{pmatrix} 2x & 0 \\ y & x \\ 0 & e^{y} \end{pmatrix}\bigg|_{(1,0)} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ 0 & 1 \end{pmatrix}.$$
So $dF_{(1,0)}(\partial/\partial x|_{p}) = 2\,\partial/\partial u|_{F(p)}$ and $dF_{(1,0)}(\partial/\partial y|_{p}) = \partial/\partial v|_{F(p)} + \partial/\partial w|_{F(p)}$.

**Computing $dF_{p}$ via a curve.** Let $F : \mathrm{GL}(n, \mathbb{R}) \to \mathrm{GL}(n, \mathbb{R})$ be matrix inversion, $F(A) = A^{-1}$. To compute $dF_{I}(H)$ for $H \in M_{n}(\mathbb{R}) = T_{I}\mathrm{GL}(n)$, take the curve $\gamma(t) = I + tH$ (for $t$ small, this stays in $\mathrm{GL}(n)$). Then $\gamma'(0) = H$ and $(F \circ \gamma)(t) = (I + tH)^{-1} = I - tH + O(t^{2})$ as $t \to 0$, so $dF_{I}(H) = (F \circ \gamma)'(0) = -H$. This is much faster than expanding in coordinates.

**Is NOT a tangent vector: an operator on $C^{\infty}(M)$ that is not the precomposed image of a derivation.** Suppose $L : C^{\infty}(N) \to \mathbb{R}$ is an operator at $F(p)$ that does *not* arise as $v(f \circ F)$ for any $v \in T_{p}M$. Then $L$ might be linear and Leibniz at $F(p)$ (hence a tangent vector at $F(p)$) without being in the image of $dF_{p}$. The image of $dF_{p}$ is exactly the *rank* of $dF_{p}$ — see [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

**Corollary — the kernel of $dF_{p}$ is the tangent space of the "infinitesimal level set".** Tangent vectors $v$ with $dF_{p}(v) = 0$ are those for which $v(f \circ F) = 0$ for every $f \in C^{\infty}(N)$. Geometrically, these are velocities of curves in $M$ that $F$ sends to constant curves at $F(p)$ to first order — the "infinitesimal preimage" $F^{-1}(F(p))$ at the tangent level. This is the source of the [[Def - Tangent Space of a Submanifold|tangent space of a submanifold defined by a regular value]].

**Corollary — diffeomorphisms have isomorphic differentials.** If $F : M \to N$ is a diffeomorphism, then $F \circ F^{-1} = \mathrm{id}_{N}$ and $F^{-1} \circ F = \mathrm{id}_{M}$. Differentiating with the chain rule, $dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$ and $d(F^{-1})_{F(p)} \circ dF_{p} = \mathrm{id}_{T_{p}M}$. So $dF_{p}$ is a vector-space isomorphism. In particular, $\dim T_{p}M = \dim T_{F(p)}N$, which gives the proof that diffeomorphic manifolds have the same dimension.

**Calibration check.** Verify that the differential of the squaring map $F : \mathbb{R} \to \mathbb{R}$, $F(x) = x^{2}$, at $x = 3$ is the linear map $h \mapsto 6h$, i.e., $dF_{3} = 6 \cdot \mathrm{id}_{T_{3}\mathbb{R}}$. Verify that the differential of complex squaring $z \mapsto z^{2}$ at $z = 1$ is the map $w \mapsto 2w$. Verify that the differential of the inverse map $A \mapsto A^{-1}$ on $\mathrm{GL}(n)$ at $I$ is $H \mapsto -H$. If you can also explain why the differential of a diffeomorphism is automatically an isomorphism, you have understood the role of functoriality in this definition.

---

# Unlocked by This

> [!tip] Chain Rule and Functoriality *(from Differential Geometry)*
> The chain rule $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ is the categorical statement that $T_{p}$ is a covariant functor from pointed smooth manifolds to vector spaces. See [[Thm - Chain Rule for the Differential]]. From this, the differential of a diffeomorphism is automatically an isomorphism, and many invariants of $F$ become invariants of $dF_{p}$.

> [!tip] Rank of a Smooth Map *(from Differential Geometry)*
> The **rank** of $F$ at $p$ is the rank of the linear map $dF_{p}$. The constant-rank maps fall into the classes of submersions ($dF_{p}$ surjective), immersions ($dF_{p}$ injective), and embeddings (injective immersions that are homeomorphisms onto their images). The rank theorem gives a local normal form. See [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

> [!tip] Pullback of a Covector *(from Differential Geometry)*
> The *dual* construction to the differential is the **pullback** of covectors: $F^{*}\omega_{p}(v) = \omega_{F(p)}(dF_{p}(v))$ for a covector $\omega \in T^{*}_{F(p)}N$. The pullback is contravariant in $F$ — pulling covectors backward, while the differential pushes vectors forward. The dichotomy "vectors push forward, covectors pull back" is one of the most useful slogans in differential geometry. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

> [!tip] The Jacobian Determinant and Volume *(from Multivariate Analysis)*
> When $\dim M = \dim N$, the differential $dF_{p}$ is a linear map between vector spaces of the same dimension, and its determinant (after picking bases) is the **Jacobian determinant**. The Jacobian determinant measures the local volume distortion of $F$ and underlies the change-of-variables formula for integration. See [[Def - Determinant]].
