---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Map"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $\mathbb{F}$. A **linear functional** on $V$ is a linear map $\varphi : V \to \mathbb{F}$ — that is, a linear map with codomain the field of scalars, viewed as a one-dimensional vector space over itself. The set of all such linear maps is the **dual space**, denoted $V' = \mathcal{L}(V, \mathbb{F})$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Convention.** Axler uses $V'$ for the dual space and reserves $V^*$ for the adjoint (introduced in [[Linear Algebra VII — §7 Operators on Inner Product Spaces|Chapter 7]]). Many authors, particularly in differential geometry and functional analysis, write $V^*$ for the dual instead. The mathematics is the same.

---

# Axiom Motivation

The dual space exists because *linear measurements* on a vector space deserve their own home. Asking "what is the natural class of measurements on $V$?" is a question whose answer is forced by linearity.

A measurement assigns a number to each vector. We want the measurement to be *linear*: $\varphi(v + w) = \varphi(v) + \varphi(w)$ and $\varphi(\lambda v) = \lambda \varphi(v)$. The first condition is additivity (the measurement of a sum is the sum of the measurements); the second is homogeneity (scaling the vector scales the measurement). Together they say the measurement is a linear map $V \to \mathbb{F}$. Linear measurements are the natural class because: (a) they are the simplest possible class of measurements after the constants; (b) they respect the structure that *makes* $V$ a vector space; and (c) they are the building blocks for every other linear-algebraic operation — coordinate functionals, integrals against test functions, inner products, traces — all are linear functionals at heart.

What is forced by the desideratum "the dual is a vector space"? Once we have linear functionals, we need to add and scale them. The natural definition is **pointwise**: $(\varphi + \psi)(v) := \varphi(v) + \psi(v)$ and $(\lambda \varphi)(v) := \lambda \varphi(v)$. Pointwise operations are forced by linearity: if we want $\varphi + \psi$ to remain a linear functional with linear addition, we are restricted to the pointwise definition (any other rule fails additivity or homogeneity for $\varphi + \psi$).

What is forced by "the dual has the same dimension as $V$, in finite [[Def - Dimension|dimensions]]"? This is not forced by the definition — it is a *theorem* (see [[Thm - Dimension of Dual Space]]). It is a remarkable consequence of the linear-map dimension formula $\dim \mathcal{L}(V, W) = (\dim V)(\dim W)$ combined with $\dim \mathbb{F} = 1$. The intuition: each functional is determined by what it does on a basis $v_1, \dots, v_n$, and that data is $n$ scalars $\varphi(v_k)$, so $V'$ has $n$ free parameters and dimension $n$.

What if we weakened "linear" to just "additive"? Over $\mathbb{R}$ or $\mathbb{C}$, additive measurements that are also continuous turn out to coincide with linear ones — that is the content of the continuity assumption. But additive measurements that are *not* continuous can be wild (require axiom of choice to even construct). Over $\mathbb{Q}$ or rough fields, additivity is strictly weaker. The linearity hypothesis is the right strength: strong enough to enforce structure, weak enough to include all the useful examples.

What if we strengthened to "continuous"? In finite [[Def - Dimension|dimensions]] every linear map is automatically continuous, so the strengthening is vacuous. In infinite dimensions it is non-vacuous and important: the "topological dual" $V'$ consisting of *continuous* linear functionals is generally a proper [[Def - Subspace|subspace]] of the algebraic dual, and the entire theory of Banach and Hilbert spaces rests on the distinction. For this topic — finite-dimensional linear algebra — continuity is automatic.

The deeper motivation, beyond the definitional one, is that $V'$ is the source of *coordinates*: once you choose a basis $v_1, \dots, v_n$ of $V$, the dual basis $\varphi_1, \dots, \varphi_n$ has $\varphi_j(v_k) = \delta_{jk}$, and $\varphi_j(v)$ extracts the $j$-th coordinate of $v$. So the dual space is a coordinate-free formalisation of the idea of coordinates. Without naming the dual, we cannot speak of "coordinates" without first committing to a basis; with the dual, coordinates become a *space* — the dual space — and bases of $V$ are dual to bases of $V'$.

---

# The Definition

A **linear functional** on $V$ is a linear map $\varphi : V \to \mathbb{F}$ — equivalently, an element of $\mathcal{L}(V, \mathbb{F})$ viewing $\mathbb{F}$ as a one-dimensional vector space over itself.

The **dual space** of $V$ is
$$V' := \mathcal{L}(V, \mathbb{F}),$$
the vector space of all linear functionals on $V$. Operations are pointwise:
$$(\varphi + \psi)(v) := \varphi(v) + \psi(v), \qquad (\lambda \varphi)(v) := \lambda \varphi(v).$$
The zero functional, sending every $v$ to $0 \in \mathbb{F}$, is the additive identity. The additive inverse of $\varphi$ is $-\varphi$, defined by $(-\varphi)(v) = -\varphi(v)$.

When $V$ is finite-dimensional, $V'$ is also finite-dimensional with $\dim V' = \dim V$ ([[Thm - Dimension of Dual Space]]); a particular basis is the **dual basis** of any chosen basis of $V$ ([[Def - Dual Basis]]).

---

# Categorical Definition

The dual space is a contravariant functor. Restating that statement precisely:

**Functoriality.** The assignment $V \mapsto V'$ is part of a functor on the category of vector spaces. To each linear map $T : V \to W$ corresponds a **dual map** $T' : W' \to V'$ defined by $T'(\varphi) = \varphi \circ T$ (see [[Def - Dual Map]]). The dual map reverses the direction of $T$, and satisfies:
- $(\operatorname{id}_V)' = \operatorname{id}_{V'}$ (the dual of the identity is the identity);
- $(ST)' = T' S'$ for $T : V \to W$, $S : W \to X$ (the dual of a composition is the *reversed* composition of the duals).

This second property is *contravariance*: arrows are reversed by the functor.

**Categorical definition.** The dual space $V'$ is the *contravariant Hom-functor* $\operatorname{Hom}(-, \mathbb{F})$ evaluated at $V$:
$$V' = \operatorname{Hom}_{\mathbb{F}}(V, \mathbb{F}),$$
where $\operatorname{Hom}_{\mathbb{F}}(V, W)$ denotes the space of linear maps $V \to W$. As a functor, $\operatorname{Hom}(-, \mathbb{F})$ takes objects (vector spaces) to objects (their duals) and arrows (linear maps) to arrows in the *opposite* direction (dual maps). It is contravariant in its first argument, which is why the direction reverses.

Two consequences of this categorical view are worth internalising. First, *all properties of the dual operation are functorial properties* — they follow from the contravariant-functor structure alone. The fact that $V \mapsto V'$ preserves dimension in finite dimensions is one example; the identities $(AB)^t = B^t A^t$ at the matrix level are another. Second, *the dual is universal among "spaces of measurements"* in the sense that every linear functional factors through $V'$ trivially. There is no smaller space that captures all linear measurements on $V$.

A subtler point: the *double dual* $V'' = (V')'$ is the result of applying the contravariant functor twice, which gives a *covariant* functor (two reversals cancel). There is a natural transformation $\Lambda : \operatorname{id} \to (-)''$ given by $(\Lambda_V v)(\varphi) = \varphi(v)$, the *evaluation map*. In finite dimensions $\Lambda_V$ is an isomorphism for every $V$, and this isomorphism is *natural* — it does not depend on any choice of basis. This is the cleanest example of a natural transformation in linear algebra, and it is the gateway to category theory. See [[Ex - Double dual is naturally isomorphic to the original]].

---

# Relate to Other Fields / Compression

The dual space is a special case of the **Hom functor**. In any category, $\operatorname{Hom}(-, Y)$ is a contravariant functor for any fixed object $Y$; the dual is $Y = \mathbb{F}$. In differential geometry the cotangent space is $\operatorname{Hom}(T_p M, \mathbb{R})$, the dual of the tangent space. In group theory the dual group of a [[Def - Abelian Group|abelian group]] $G$ is $\operatorname{Hom}(G, \mathbb{C}^\times)$, the characters. In representation theory the dual of a representation is $\operatorname{Hom}(V, \mathbb{F})$ with the contravariant action.

**True name:** the dual is the *space of linear measurements* on $V$. Operationally: $V'$ is what you get when you ask "what linear functions $V \to \mathbb{F}$ exist?" and notice the answer is itself a vector space.

A useful slogan: *bases of $V$ correspond to bases of $V'$, dually*. Once a basis $v_1, \dots, v_n$ of $V$ is chosen, the dual basis $\varphi_1, \dots, \varphi_n$ of $V'$ is determined; and conversely a basis of $V'$ determines a basis of $V$ via the [[Ex - Double dual is naturally isomorphic to the original|double-dual identification]]. The dual space is "the space whose basis is the dual of yours".

---

# Examples / Corollaries

**Is an instance — coordinate functionals on $\mathbb{F}^n$.** Fix $(c_1, \dots, c_n) \in \mathbb{F}^n$. The map $\varphi(x_1, \dots, x_n) = c_1 x_1 + \cdots + c_n x_n$ is a linear functional on $\mathbb{F}^n$. As $(c_1, \dots, c_n)$ ranges over $\mathbb{F}^n$, we get *every* linear functional on $\mathbb{F}^n$ (by the formula $\varphi(x) = \sum_k \varphi(e_k) x_k$). So $(\mathbb{F}^n)' \cong \mathbb{F}^n$ via $(c_1, \dots, c_n) \leftrightarrow \sum_k c_k \varphi_k^{\text{std}}$ where $\varphi_k^{\text{std}}$ is the $k$-th coordinate projection. This is the prototypical example.

**Is an instance — integration on polynomials.** $\varphi(p) = \int_0^1 p(x)\, dx$ defines a linear functional $\varphi : \mathcal{P}(\mathbb{R}) \to \mathbb{R}$. Linearity is the linearity of integration: $\int(p + q) = \int p + \int q$ and $\int(\lambda p) = \lambda \int p$. So integration over a fixed interval is a linear functional, as is integration against any fixed weight $w(x)$: $\varphi(p) = \int_0^1 p(x) w(x)\, dx$.

**Is an instance — evaluation at a point.** For each $a \in \mathbb{F}$, the map $\operatorname{ev}_a : \mathcal{P}(\mathbb{F}) \to \mathbb{F}$, $\operatorname{ev}_a(p) = p(a)$ is a linear functional. Linearity: $(p + q)(a) = p(a) + q(a)$ and $(\lambda p)(a) = \lambda p(a)$. Evaluation at different points gives different functionals — distinct points give linearly independent functionals — so the polynomial-evaluation functionals provide infinite-dimensional families.

**Is an instance — the trace.** For $V = \mathcal{L}(\mathbb{F}^n)$ (the space of operators on $\mathbb{F}^n$, dimension $n^2$), the trace $\operatorname{tr} : V \to \mathbb{F}$, $\operatorname{tr}(A) = \sum_k A_{kk}$, is a linear functional. Linearity is immediate. The trace is a particularly important functional because it is also basis-independent — see [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces|Chapter 8]].

**Is NOT an instance — squaring on $\mathbb{R}^n$.** The map $\varphi(x) = \|x\|^2 = x_1^2 + \cdots + x_n^2$ is *not* a linear functional. It is additive only in the special case of orthogonal vectors, and it fails homogeneity: $\varphi(\lambda x) = \lambda^2 \varphi(x)$, not $\lambda \varphi(x)$. It is a *quadratic* functional, not a linear one. To pull functions like this into a linear-algebraic framework, one uses bilinear forms ([[Linear Algebra IX — §9 Multilinear Algebra and Determinants|Chapter 9]]).

**Is NOT an instance — the constant function $1$.** The map $\varphi : V \to \mathbb{F}$, $\varphi(v) = 1$ for all $v$, is not linear: $\varphi(0) = 1 \neq 0$, but linearity forces $\varphi(0) = 0$. The only constant linear functional is the zero functional.

**Corollary — every linear functional on $\mathbb{F}^n$ has matrix a row vector.** If $\varphi : \mathbb{F}^n \to \mathbb{F}$ is linear, the matrix of $\varphi$ with respect to the standard basis of $\mathbb{F}^n$ and the basis $\{1\}$ of $\mathbb{F}$ is a $1 \times n$ matrix: $\mathcal{M}(\varphi) = (c_1, \dots, c_n)$ where $c_k = \varphi(e_k)$. Linear functionals on $\mathbb{F}^n$ "are" row vectors.

**Corollary — kernel of a non-zero functional is a hyperplane.** For non-zero $\varphi \in V'$, the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] gives $\dim V = \dim \operatorname{null} \varphi + \dim \operatorname{range} \varphi$. Since $\varphi \neq 0$, $\operatorname{range} \varphi$ is a non-zero [[Def - Subspace|subspace]] of $\mathbb{F}$, so $\dim \operatorname{range} \varphi = 1$ and $\dim \operatorname{null} \varphi = \dim V - 1$. The null space is a **hyperplane** — a subspace of codimension $1$. Every hyperplane is the null space of some non-zero functional, and the functional is determined up to scalar.

**Calibration check.** Verify that integration $p \mapsto \int_0^1 p$ is linear on $\mathcal{P}(\mathbb{R})$. Verify that the constant function $\varphi(v) = 1$ fails linearity. Confirm that for $\mathbb{F}^n$, every linear functional has the form $\varphi(x_1, \dots, x_n) = c_1 x_1 + \cdots + c_n x_n$ for unique $(c_1, \dots, c_n) \in \mathbb{F}^n$.

---

# Unlocked by This

> [!tip] Dual Basis *(from this topic)*
> Once you have the dual space, the next question is "what is the dual basis of a given basis of $V$?" — see [[Def - Dual Basis]]. The dual basis lets you extract coordinates, and is the structural tool for the matrix-of-the-dual-map computation.

> [!tip] Dual Map *(from this topic)*
> Every linear map $T : V \to W$ has a [[Def - Dual Map|dual map]] $T' : W' \to V'$, defined by $T'(\varphi) = \varphi \circ T$. The dual map reverses arrows and is the matrix-level origin of the transpose.

> [!tip] Riesz Representation Theorem *(from Linear Algebra VI)*
> When $V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]], every linear functional has the form $\varphi(v) = \langle v, w \rangle$ for a unique $w \in V$. The map $w \mapsto \langle \cdot, w \rangle$ is a conjugate-linear isomorphism $V \cong V'$ that requires *the inner product* (a choice) rather than a basis. See [[Thm - Riesz Representation Theorem (Finite-Dimensional)]] in [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]].

> [!tip] Cotangent Space *(from Differential Geometry)*
> At each point $p$ of a smooth manifold $M$, the **cotangent space** $T_p^* M = (T_p M)'$ is the dual of the tangent space. Differential 1-forms are smooth assignments of covectors, and the cotangent bundle is the geometric vehicle for the calculus on manifolds. The exterior derivative $df$ of a function is a 1-form, and Stokes' theorem in its modern form is a statement about integration of differential forms — all of which live in tensor products of cotangent spaces.

> [!tip] Distributions *(from PDE Analysis)*
> The **distributions** $\mathcal{D}'(\Omega)$ on an open set $\Omega \subseteq \mathbb{R}^n$ are the continuous linear functionals on the space of test functions $C_c^\infty(\Omega)$ — that is, the dual of an infinite-dimensional function space. The Dirac delta $\delta_a(\varphi) = \varphi(a)$ is a distribution but not a function. Distributions generalise the notion of function in a way that lets differentiation be defined on objects that are not differentiable in the classical sense, and they are the foundation of modern PDE theory. The **Hahn-Banach theorem** of functional analysis is the substantive content that makes the dual of an infinite-dimensional Banach space large enough to be useful — in finite dimensions this is automatic.
