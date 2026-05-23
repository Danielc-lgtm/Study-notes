---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Tensor Field on a Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Pullback of a Covector Field"
tags: [geometry, differential-geometry, pullback]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds. $dF_p : T_pM \to T_{F(p)}N$ is the [[Def - The Differential of a Smooth Map|differential]] of $F$ at $p$. $A$ is a covariant $k$-tensor field on $N$, with pullback $F^*A$ a covariant $k$-tensor field on $M$. In coordinates: if $A$ has components $A_{i_1\cdots i_k}(y)$ in a chart $(y^j)$ on $N$, then $F^*A$ has the components determined by the chain rule applied to the coordinate functions $y^j = F^j(x)$ of $F$ in a chart $(x^a)$ on $M$. Einstein summation is in force. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

The motivation is to **transport a tensor field defined on $N$ back to a tensor field on $M$, given a smooth map $F : M \to N$**. The classical motivation is the change-of-variables formula in integration: if $\omega$ is a volume form on $N$ and we want to compute $\int_N \omega$ via a coordinate chart $F : U \subset \mathbb{R}^n \to N$, we need to express $\omega$ in coordinates on $\mathbb{R}^n$ — i.e., we need to *pull $\omega$ back* through $F$. The change-of-variables formula then says $\int_U F^*\omega = \int_N \omega$ (when $F$ is an oriented [[Def - Diffeomorphism|diffeomorphism]] onto $N$), and the Jacobian of $F$ appears automatically in the components of $F^*\omega$ — there is no need to multiply by a separate Jacobian factor.

The construction for covariant tensors is forced by what one wants pullback to do. A covariant $k$-tensor $\alpha$ at a point $q \in N$ is a multilinear functional on $T_qN^k$. To define $(F^*\alpha)_p$ at a point $p \in M$, we need a multilinear functional on $T_pM^k$. The natural thing to do is **use the differential $dF_p : T_pM \to T_{F(p)}N$ to push the vectors of $T_pM$ forward to $T_{F(p)}N$, then evaluate $\alpha$ at the image**. So

$$(F^*A)_p(v_1, \dots, v_k) := A_{F(p)}(dF_p(v_1), \dots, dF_p(v_k))$$

is the unique definition consistent with the slogan "pullback by $F$ = precomposition with $dF$".

This definition works for any smooth $F$, regardless of whether $dF_p$ is injective or surjective. The pullback exists and is a tensor field on *all* of $M$, including points where $F$ is not a local diffeomorphism. In particular, even if $F$ has critical points or degenerate behaviour, $F^*A$ is well-defined: the differential always exists, and the formula always makes sense.

**The asymmetry: covariant tensors pull back, contravariant tensors push forward.** A vector field $X$ on $N$ — a contravariant tensor field — does *not* have a canonical pullback to $M$. The reason is structural: to define a vector at $p \in M$ from a vector field on $N$, we would need to "pull a vector at $F(p)$ back to $p$", but $dF_p$ goes the wrong way (it pushes vectors of $T_pM$ forward to $T_{F(p)}N$, not the reverse). The reverse map $dF_p^{-1}$ exists only when $dF_p$ is invertible, i.e., when $F$ is a *local diffeomorphism*. So contravariant tensors pull back only when $F$ is a (local) diffeomorphism, while covariant tensors pull back universally.

This asymmetry is *the* fundamental reason for separating covariant and contravariant tensors. They behave differently under maps; the variance label is a functorial label, not a typographical convention. Lee uses the slogan "covariant tensors are *natural*, contravariant tensors are *constrained*" — meaning that covariant tensor fields have a clean and unrestricted pullback functor, while contravariant tensor fields only have a partial one.

One could ask what to do with **mixed tensors** under a smooth $F$ that is not a diffeomorphism. The answer is: nothing — mixed tensor fields have no canonical pullback (nor pushforward) under a generic smooth map. Only the purely covariant part can be pulled back. This is one reason differential geometry on manifolds emphasizes covariant tensor fields and differential forms: they are the universally well-behaved species. When $F$ is a diffeomorphism, all variances can be transported (covariant by pullback, contravariant by pushforward via $F^{-1}$, mixed by combining the two), and the categorical setup becomes symmetric.

The recipe in coordinates is the **substitution-and-expansion** algorithm. Given $A = A_{i_1\cdots i_k}(y)\, dy^{i_1}\otimes\cdots\otimes dy^{i_k}$ on $N$ and $F$ with coordinate functions $y^i = F^i(x)$, the pullback is

$$F^*A = (A_{i_1\cdots i_k}\circ F)(x)\, dF^{i_1}\otimes\cdots\otimes dF^{i_k},$$

with $dF^i = (\partial F^i / \partial x^a)\, dx^a$ by the chain rule. Substituting and expanding, the components in the $(x^a)$ chart on $M$ pick up Jacobian factors $\partial F^i / \partial x^a$ for each covariant slot.

---

# The Definition

Let $F : M \to N$ be a smooth map of smooth manifolds, and let $A$ be a covariant $k$-tensor field on $N$. The **pullback** of $A$ by $F$ is the covariant $k$-tensor field $F^*A$ on $M$ defined pointwise by

$$(F^*A)_p(v_1, \dots, v_k) := A_{F(p)}(dF_p(v_1), \dots, dF_p(v_k))$$

for $p \in M$ and $v_1, \dots, v_k \in T_pM$.

For $k = 0$ (a smooth function $f$ on $N$), the formula reduces to $F^*f = f \circ F$. For $k = 1$ (a 1-form $\omega$ on $N$), it reduces to the [[Def - Pullback of a Covector Field|pullback of a covector field]] from [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

**Pullback exists and is smooth for any smooth $F$.** Even if $dF_p$ has nonzero kernel or fails to be surjective, the formula is well-defined: it only requires evaluating $A_{F(p)}$ on vectors that lie in the image of $dF_p$, which is a [[Def - Subspace|subspace]] of $T_{F(p)}N$. The smoothness of $F^*A$ as a section of $T^kT^*M$ is automatic because all the ingredients ($A$, $F$, $dF$) are smooth.

**Coordinate expression.** Let $(U, x^a)$ be a chart on $M$, $(V, y^i)$ a chart on $N$ with $F(U) \subseteq V$, and let $y^i = F^i(x)$ be the coordinate functions of $F$. If $A = A_{i_1\cdots i_k}(y)\, dy^{i_1}\otimes\cdots\otimes dy^{i_k}$, then

$$F^*A = (A_{i_1\cdots i_k}\circ F)(x)\, dF^{i_1}\otimes\cdots\otimes dF^{i_k}.$$

Expanding $dF^i = (\partial F^i / \partial x^a)\, dx^a$ via the chain rule and multiplying out gives

$$(F^*A)_{a_1\cdots a_k}(x) = (A_{i_1\cdots i_k}\circ F)(x)\, \frac{\partial F^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial F^{i_k}}{\partial x^{a_k}}.$$

The Jacobian factors are unavoidable; they encode the action of $dF_p$ in components.

**Naturality properties (proved in [[Thm - Pullback Commutes with Tensor Product]]).** For smooth maps $F : M \to N$ and $G : N \to P$, covariant tensor fields $A, B$ on $N$, and $f \in C^\infty(N)$:

1. **Linearity:** $F^*(aA + bB) = aF^*A + bF^*B$ for $a, b \in \mathbb{R}$.
2. **Tensor product:** $F^*(A \otimes B) = F^*A \otimes F^*B$.
3. **Function:** $F^*(fB) = (f \circ F)\, F^*B$, and $F^*f = f \circ F$ for $f$ viewed as a 0-tensor.
4. **Functoriality:** $(G \circ F)^* = F^* \circ G^*$.
5. **Identity:** $(\mathrm{id}_N)^*B = B$.

These together say that $F^*$ is a *contravariant functor* from "tensor fields on $N$" to "tensor fields on $M$", compatible with tensor product. Pullback is the most algebraically well-behaved operation on tensor fields.

---

# Categorical / Structural Definition

The pullback is the **dual of the pushforward** $dF$ extended functorially to multilinear constructions.

In categorical language: for any smooth map $F : M \to N$, the differential $dF : TM \to TN$ is a bundle map (over $F$) sending tangent vectors forward. Dualizing fibrewise gives the bundle map $dF^* : F^*T^*N \to T^*M$ on the pulled-back cotangent bundle, going *backwards* in the dual direction. Extending by tensor products gives the bundle map on tensor bundles $(dF^*)^{\otimes k} : F^*(T^kT^*N) \to T^kT^*M$. Composing with the canonical map of sections $\sigma_N \mapsto \sigma_N \circ F$ gives the pullback functor on sections:

$$F^* : \Gamma(T^kT^*N) \to \Gamma(T^kT^*M), \quad A \mapsto (dF^*)^{\otimes k} \circ (A \circ F).$$

The whole construction is functorial: it is a contravariant functor on the category of smooth manifolds, valued in the category of $C^\infty$-[[Def - Module|modules]].

The **universal property** of pullback: for any tensor field $B$ on $M$ and any "compatible" data, $F^*A$ is uniquely characterized by the requirement $F^*A(v_1, \dots, v_k) = A(dF v_1, \dots, dF v_k)$. This makes pullback the natural construction "make a tensor field on $M$ that agrees with $A$ when its inputs are differentials of $F$-pushed-forward vectors".

---

# Relate to Other Fields / Compression

Pullback of covariant tensor fields is the **manifold-level extension of pullback of covariant tensors at the linear-algebra level**. In [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]], a linear map $L : V \to W$ induces $L^* : T^k(W^*) \to T^k(V^*)$ on covariant tensors by precomposition. Here, $dF_p$ plays the role of $L$ at each point, and the manifold-level pullback is the smooth assembly of these point-level pullbacks.

From the [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|MA IV]] viewpoint, pullback restricted to alternating tensor fields is the [[Def - Pullback of a Differential Form|pullback of differential forms]]. The chain rule $d(F^*\omega) = F^*(d\omega)$ — that pullback commutes with the exterior derivative — is one of the two facts that make Stokes's theorem on manifolds work (the other being the additivity of integration over compatible orientations).

From the physics side, pullback is **the operation by which physical fields transform under a change of coordinate chart**. If the metric tensor on a manifold is $g_{ij}$ in one chart and $\tilde g_{ab}$ in another, with the chart transition being the smooth map $F$, then $\tilde g = F^*g$. The transformation rule for tensor components in [[Thm - Transformation Rule for Tensor Components]] is precisely the pullback formula spelled out in coordinates.

**True name:** $F^*A$ is **the tensor field on $M$ whose value at $p$ is $A_{F(p)}$ precomposed with $dF_p$ in each slot**. Operationally: substitute coordinates and expand.

---

# Examples / Corollaries

**Is an instance: pullback of a smooth function.** $F^*f = f \circ F$. The most basic case, recovering function composition.

**Is an instance: pullback of a 1-form.** $F^*\omega = (\omega_i \circ F)\, dF^i = (\omega_i \circ F)(\partial F^i / \partial x^a)\, dx^a$. See [[Def - Pullback of a Covector Field]].

**Is an instance: the metric in polar coordinates.** $F(r, \theta) = (r\cos\theta, r\sin\theta)$ maps polar to Cartesian; $g = dx \otimes dx + dy \otimes dy$ is the Euclidean metric. Then $F^*g = dr \otimes dr + r^2\, d\theta \otimes d\theta$ — the polar form of the Euclidean metric. See [[Ex - The Metric Tensor in Polar Coordinates]].

**Is an instance: pullback of a volume form by a diffeomorphism.** For $F : \mathbb{R}^n \to \mathbb{R}^n$ a diffeomorphism and $\mathrm{vol} = dx^1 \wedge \cdots \wedge dx^n$, the pullback is $F^*\mathrm{vol} = \det(DF)\, dx^1 \wedge \cdots \wedge dx^n$. The Jacobian determinant of $F$ is built into the pullback formula automatically — this is the change-of-variables theorem in disguise.

**Is an instance: pullback by a constant map.** If $F : M \to N$ is the constant map $p \mapsto q_0$, then $dF_p = 0$ for all $p$. Hence $(F^*A)_p(v_1, \dots, v_k) = A_{q_0}(0, \dots, 0) = 0$. So the pullback of any covariant tensor field of positive rank by a constant map is zero. (Pullback of a *function*, however, is $F^*f = f \circ F = f(q_0) \cdot 1$ — the constant function on $M$.)

**Is NOT an instance: pullback of a vector field by a non-diffeomorphism.** A vector field $X$ on $N$ is contravariant, not covariant. There is no general pullback operation on vector fields unless $F$ is a diffeomorphism. So $F^*X$ is undefined for a generic smooth $F : M \to N$.

**Is NOT an instance: "pullback" along a path.** A curve $\gamma : [a, b] \to M$ does not pull back a vector field on $M$ to a vector field on $[a, b]$ — instead, one *restricts* the vector field along the curve, which is a different operation. The covariant tensor fields on $M$ *do* pull back along $\gamma$, giving covariant tensor fields on the interval.

**Corollary (chain rule).** $(G \circ F)^*A = F^*(G^*A)$ for smooth $F : M \to N$, $G : N \to P$, $A$ a covariant tensor field on $P$. *Proof:* by the chain rule for differentials, $d(G \circ F)_p = dG_{F(p)} \circ dF_p$, so $(G \circ F)^*A_p(v_1, \dots, v_k) = A_{(G \circ F)(p)}(d(G \circ F)_p v_1, \dots) = A_{G(F(p))}(dG_{F(p)} dF_p v_1, \dots) = F^*(G^*A)_p(v_1, \dots, v_k)$.

**Corollary (functorial in $F$).** Pullback $F^*$ is a $\mathbb{R}$-linear map $\Gamma(T^kT^*N) \to \Gamma(T^kT^*M)$, and it respects the algebraic operations on covariant tensor fields.

**Corollary (pullback by an embedding restricts).** If $F : M \hookrightarrow N$ is an [[Def - Immersion, Submersion, and Embedding|embedding]] of $M$ as a submanifold of $N$, then $F^*A$ is the **restriction** of $A$ to $M$ in a natural sense — at each $p \in M$, $(F^*A)_p$ is the restriction of $A_p$ (viewed as a multilinear form on $T_pN$) to the subspace $T_pM \subseteq T_pN$.

**Corollary (the induced metric on a submanifold).** If $g$ is a Riemannian metric on $N$ and $F : M \hookrightarrow N$ is an embedding, then $F^*g$ is a Riemannian metric on $M$ — the **induced metric** (or "first fundamental form") on the submanifold. This is one of the most-used pullback applications in geometry: the metric on the sphere $S^2 \subset \mathbb{R}^3$ is the pullback of the Euclidean metric on $\mathbb{R}^3$ along the inclusion.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that $F^*(f \cdot \omega) = (f \circ F) \cdot F^*\omega$ for a function $f$ and 1-form $\omega$ on $N$; (ii) compute the pullback of $dx \otimes dy$ on $\mathbb{R}^2$ along $F(t) = (t, t^2)$ — answer: $1 \cdot 2t\, dt \otimes dt = 2t\, dt \otimes dt$; (iii) explain why pullback is functorial in $F$ ($\mathrm{id}^* = \mathrm{id}$ and $(G \circ F)^* = F^* \circ G^*$) and why functoriality is what makes pullback "natural" in the categorical sense.

---

# Unlocked by This

> [!tip] Pullback of Differential Forms *(from [[Differential Geometry VIII — Differential Forms]])*
> The restriction of $F^*$ to alternating $(0, k)$-tensor fields gives the pullback of differential forms. Crucially, $F^*$ commutes with the wedge product ($F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$) and with the exterior derivative ($F^*d = dF^*$). These two facts together make Stokes's theorem on manifolds work and underlie the entire theory of de Rham cohomology.

> [!tip] The Change-of-Variables Formula and Integration *(from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]])*
> The integral of an $n$-form over an oriented $n$-manifold is *defined* by pulling the form back to a chart in $\mathbb{R}^n$ and integrating in the Lebesgue sense. The Jacobian factor that would normally appear in the change-of-variables formula is absorbed into the components of $F^*\omega$, making the integration formula coordinate-free at the manifold level: $\int_M \omega = \sum_\alpha \int_{U_\alpha} (\varphi_\alpha)^*\omega \cdot \rho_\alpha$, with $\rho_\alpha$ a partition of unity and $\varphi_\alpha$ the charts.

> [!tip] Induced Metric and the First Fundamental Form *(from Riemannian Geometry)*
> An [[Def - Immersion, Submersion, and Embedding|embedded submanifold]] $M \hookrightarrow N$ of a Riemannian manifold inherits a Riemannian metric by pullback: $g_M := F^*g_N$. This is the **induced metric** or **first fundamental form**, and it is the basic construction for studying submanifolds — the round metric on $S^n \subset \mathbb{R}^{n+1}$, the Poincaré metric on the upper half-plane embedded in $\mathbb{R}^2$ with the right ambient form, the Fubini-Study metric on $\mathbb{CP}^n \subset $ something complex.

> [!tip] Coordinate Transformations as Pullbacks *(from Tensor Analysis)*
> When a tensor field is given by components in chart $\varphi : U \to \mathbb{R}^n$ and we want its components in a different chart $\psi : U \to \mathbb{R}^n$, the answer is the pullback of the tensor by the transition map $\psi \circ \varphi^{-1}$. The transformation rule [[Thm - Transformation Rule for Tensor Components]] is exactly the pullback formula in coordinates. So "transforming a tensor under change of coordinates" and "pulling back a tensor under a chart transition" are the same operation.
