---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Dual Space"
  - "Def - Dual Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are vector spaces over $\mathbb{F}$, and $T \in \mathcal{L}(V, W)$ is a linear map. The **dual map** of $T$ is the linear map $T' : W' \to V'$ defined by $T'(\varphi) = \varphi \circ T$ for $\varphi \in W'$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Convention.** Axler uses $T'$ for the dual map and reserves $T^*$ for the adjoint. Many books, especially in differential geometry, use $T^*$ for the dual.

---

# Axiom Motivation

The dual map exists because of one structural fact: *every linear map gives rise to a natural map on dual spaces, in the reverse direction*.

The desideratum is to make the assignment $V \mapsto V'$ functorial — to extend it to linear maps in a way consistent with composition. Given $T : V \to W$, we want an induced map between $V'$ and $W'$.

In which direction? The answer is *forced* by the definitions, and it is the reverse direction. Here is why. A functional $\varphi \in W'$ is a linear map $\varphi : W \to \mathbb{F}$. Composing with $T : V \to W$ gives the linear map $\varphi \circ T : V \to \mathbb{F}$, an element of $V'$. So $\varphi$ pulls back along $T$ to become a functional on $V$. This is the only natural way to associate something in $V'$ to something in $W'$ using $T$: we **pull back** a measurement on $W$ to a measurement on $V$ by feeding through $T$ first.

The reversal is the entire content of the dual map's definition. If we tried to push forward — to associate to $\varphi \in V'$ a functional in $W'$ — there is no canonical recipe: $\varphi$ is a function on $V$, $T$ is a map $V \to W$, and $T(v) \in W$ but $\varphi(v) \in \mathbb{F}$. You cannot get a function on $W$ out of these ingredients unless $T$ is invertible. The reverse direction is canonical; the forward direction is not.

The defining equation $T'(\varphi) := \varphi \circ T$ is also the only one consistent with the universal property of $\mathcal{L}(V, \mathbb{F}) = V'$: the functional $T'(\varphi)$ must be linear (composition of linear maps is linear, so $\varphi \circ T$ is linear), and it must be the unique linear map $V \to \mathbb{F}$ that "factors" $\varphi$ through $T$. So the definition is forced by both the categorical structure (the Hom-functor) and the direct manipulation of the symbols.

The contravariance property $(ST)' = T'S'$ — note the *reversal* of order — is the algebraic content of "this construction reverses arrows". The composition $ST$ takes $V$ first to $W$ via $T$, then to $X$ via $S$. The dual map $(ST)' : X' \to V'$ takes a functional on $X$ and pulls back to a functional on $V$, but the pullback should go in stages: pull back from $X'$ to $W'$ via $S$ (giving $S'$), and then from $W'$ to $V'$ via $T$ (giving $T'$). So $(ST)'$ is $T'$ then $S'$, applied in that order, which is the right-to-left composition $T' \circ S' = T'S'$. The reversal is forced by the structure.

The motivation for the matrix-level identity $(AB)^t = B^t A^t$ is the same: it is the matrix shadow of contravariance, $(ST)' = T'S'$, applied in dual bases. This single observation removes the mystery from one of the most-used identities in linear algebra.

---

# The Definition

Let $T \in \mathcal{L}(V, W)$. The **dual map** of $T$ is the map $T' : W' \to V'$ defined by
$$T'(\varphi) := \varphi \circ T \qquad \text{for } \varphi \in W'.$$
Equivalently, for each $v \in V$:
$$(T'(\varphi))(v) = \varphi(T(v)).$$

The map $T'$ is itself a **linear map** from $W'$ to $V'$. Linearity:
- $T'(\varphi + \psi) = (\varphi + \psi) \circ T = \varphi \circ T + \psi \circ T = T'(\varphi) + T'(\psi)$;
- $T'(\lambda \varphi) = (\lambda \varphi) \circ T = \lambda (\varphi \circ T) = \lambda T'(\varphi)$.

The dual operation has the following **algebraic properties**, for $S, T \in \mathcal{L}(V, W)$, $\lambda \in \mathbb{F}$, and $S' \in \mathcal{L}(W, X)$ (using $S'$ here as a generic linear map, *not* the dual of $S$ — we will rename it to avoid confusion):

> **Algebraic properties of the dual.** For $R, T \in \mathcal{L}(V, W)$, $\lambda \in \mathbb{F}$, and $S \in \mathcal{L}(W, X)$:
> - **Linearity in $T$:** $(R + T)' = R' + T'$ and $(\lambda T)' = \lambda T'$. So the map $T \mapsto T'$ is itself linear from $\mathcal{L}(V, W)$ to $\mathcal{L}(W', V')$.
> - **Contravariance:** $(ST)' = T'S'$. Note the order reversal: dualising a composition reverses the order.
> - **Identity:** $(\operatorname{id}_V)' = \operatorname{id}_{V'}$. The dual of the identity is the identity.

These are the precise statements of "$T \mapsto T'$ is a contravariant functor on the category of vector spaces, valued in vector spaces and linear maps".

The proof of contravariance is a direct computation. For $\varphi \in X'$ and $v \in V$:
$$((ST)'(\varphi))(v) = \varphi(STv) = (\varphi \circ S)(Tv) = (S'(\varphi))(Tv) = (T'(S'(\varphi)))(v) = ((T' \circ S')(\varphi))(v).$$
So $(ST)'(\varphi) = (T' S')(\varphi)$ for every $\varphi$, hence $(ST)' = T'S'$.

---

# Categorical Definition

The dual map is the action of the **contravariant Hom-functor** $\operatorname{Hom}(-, \mathbb{F})$ on morphisms. To each linear map $T : V \to W$ this functor assigns the linear map $T' : W' \to V'$, $\varphi \mapsto \varphi \circ T$. The functor satisfies the axioms of a contravariant functor:
- preserves identities: $\operatorname{id}_V \mapsto \operatorname{id}_{V'}$;
- reverses composition: $S \circ T \mapsto T' \circ S'$ (i.e. arrows are reversed and composed in reverse).

A *contravariant functor* on the category of vector spaces is exactly a covariant functor on the *opposite category* (where arrows are reversed). So the dual is sometimes described as the "covariant functor $\operatorname{Vect}^{\operatorname{op}} \to \operatorname{Vect}$".

**Higher structure.** The double dual $V \mapsto V''$ is the composition of $\operatorname{Hom}(-, \mathbb{F})$ with itself, which is a *covariant* functor (two reversals cancel). The natural transformation $\Lambda : \operatorname{id} \Rightarrow (-)''$ given by $(\Lambda_V v)(\varphi) = \varphi(v)$ is *natural* in the categorical sense: for every $T : V \to W$, the diagram
$$\begin{array}{ccc} V & \xrightarrow{\;T\;} & W \\ {}_{\Lambda_V}\!\downarrow & & {}_{\Lambda_W}\!\downarrow \\ V'' & \xrightarrow{\;T''\;} & W'' \end{array}$$
commutes. This is the structural content of "$\Lambda$ does not depend on a choice", and it is the precise notion of *natural isomorphism*. See [[Ex - Double dual is naturally isomorphic to the original]].

---

# Relate to Other Fields / Compression

The dual map is the **pullback of measurements along $T$**: a measurement $\varphi$ on the target $W$ becomes a measurement $\varphi \circ T$ on the source $V$, obtained by first applying $T$. In integration theory this is the change-of-variables formula: if $T$ is a coordinate change, then $\varphi(Tv) = (T'\varphi)(v)$ is the integral of $\varphi$ after substitution. In dynamical systems, if $T$ is the flow of a system, then $T'$ is the *Koopman operator* — the natural action of the dynamics on the space of observables.

**True name:** the dual map is "pull back measurements along $T$". Operationally: to evaluate the pulled-back functional on a vector, first push the vector through $T$, then apply the original functional.

In differential geometry the dual map specialises to the *pullback of 1-forms*: if $f : M \to N$ is a smooth map of manifolds, then $f^* : T^*_{f(p)} N \to T^*_p M$ is the dual of the differential $df_p : T_p M \to T_{f(p)} N$, and pulls back covectors at $f(p)$ to covectors at $p$. This is the source of the entire calculus of pullbacks: 1-forms, $k$-forms, vector bundles. The contravariance — pullback reverses arrows — is identical to the linear-algebraic case.

The matrix-level shadow is the **transpose** (see [[Thm - Matrix of Dual Map is Transpose]]): the matrix of $T'$ in dual bases is the transpose of the matrix of $T$ in the original bases. This makes the identities $(AB)^t = B^t A^t$ and "row rank equals column rank" structural consequences of contravariance, not coincidental index manipulations.

---

# Examples / Corollaries

**Is an instance — dual of the identity.** Let $T = \operatorname{id}_V : V \to V$. Then for $\varphi \in V'$, $T'(\varphi) = \varphi \circ \operatorname{id}_V = \varphi$. So $T' = \operatorname{id}_{V'}$. The dual of the identity is the identity, confirming functoriality.

**Is an instance — dual of differentiation on polynomials.** Let $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$ be the differentiation map $D(p) = p'$. For $\varphi \in \mathcal{P}(\mathbb{R})'$ defined by $\varphi(p) = p(3)$ (evaluation at $3$), the dual map gives $D'(\varphi)(p) = \varphi(Dp) = (Dp)(3) = p'(3)$. So $D'(\varphi)$ is "evaluation of the derivative at $3$", a functional that takes a polynomial to the value of its derivative at $3$.

For another $\varphi(p) = \int_0^1 p(x)\, dx$, the dual map gives $D'(\varphi)(p) = \varphi(p') = \int_0^1 p'(x)\, dx = p(1) - p(0)$ by the fundamental theorem of calculus. So $D'$ converts integration into "boundary evaluation", a pleasant example of pullback turning a global operation (integration) into a local one (evaluation at endpoints).

**Is an instance — dual of a coordinate projection.** Let $\pi_1 : \mathbb{F}^n \to \mathbb{F}$, $\pi_1(x_1, \dots, x_n) = x_1$. The dual map $\pi_1' : \mathbb{F}' \to (\mathbb{F}^n)'$ takes a functional on $\mathbb{F}$ (which is just a scalar, since $\mathcal{L}(\mathbb{F}, \mathbb{F}) \cong \mathbb{F}$) to a functional on $\mathbb{F}^n$. If $\varphi_c : \mathbb{F} \to \mathbb{F}$ is multiplication by $c$, then $\pi_1'(\varphi_c)(x_1, \dots, x_n) = \varphi_c(\pi_1(x_1, \dots, x_n)) = c x_1$. So $\pi_1'$ embeds $\mathbb{F}'$ into $(\mathbb{F}^n)'$ as the first coordinate functional, scaled.

**Is NOT an instance — pushforward of measurements is not generally defined.** Given $\varphi \in V'$ and $T : V \to W$, there is no canonical functional on $W$ associated to $\varphi$ — there is no "$T_* \varphi$". The only natural map between $V'$ and $W'$ associated to $T$ is the *dual* $T'$, going from $W'$ to $V'$. When $T$ is invertible, one can define a pushforward as $\varphi \circ T^{-1}$, but this requires invertibility and is not canonical without it.

**Corollary — algebraic properties of the dual.** The identities $(R + T)' = R' + T'$, $(\lambda T)' = \lambda T'$, $(ST)' = T'S'$ exhibit the dual as a contravariant linear functor. The first two say $T \mapsto T'$ is itself linear; the third says it reverses composition.

**Corollary — dualising is an isomorphism $\mathcal{L}(V, W) \cong \mathcal{L}(W', V')$.** When $V$ and $W$ are finite-dimensional, the map $T \mapsto T'$ is a linear isomorphism between these two spaces. Both have dimension $\dim V \cdot \dim W$. (See Exercise 18 of LADR §3F.)

**Corollary — dualising preserves invertibility.** If $T : V \to W$ is invertible (necessarily $\dim V = \dim W$), then $T' : W' \to V'$ is also invertible, with $(T')^{-1} = (T^{-1})'$. Proof: $T T^{-1} = \operatorname{id}_W$ dualises to $(T^{-1})' T' = \operatorname{id}_{W'}$, and similarly $T^{-1} T = \operatorname{id}_V$ dualises to $T' (T^{-1})' = \operatorname{id}_{V'}$, exhibiting the inverse. The order reversal is exactly contravariance in action.

**Calibration check.** Verify that $T'$ is linear (from the definitions of $\varphi + \psi$ and $\lambda \varphi$). Confirm the contravariance identity $(ST)' = T'S'$ by direct substitution. Verify that for $T = 0$, the dual $T'$ is also $0$ — the zero map has zero as its dual.

---

# Unlocked by This

> [!tip] Matrix of Dual Map is Transpose *(from this topic)*
> In dual bases, the matrix of $T'$ is the transpose of the matrix of $T$ — see [[Thm - Matrix of Dual Map is Transpose]]. This is the structural origin of the identity $(AB)^t = B^t A^t$.

> [!tip] Null Space and Range of Dual Map *(from this topic)*
> $\operatorname{null} T' = (\operatorname{range} T)^0$ and $\operatorname{range} T' = (\operatorname{null} T)^0$ — see [[Thm - Null Space and Range of Dual Map]]. The four-faceted theorem ties the dual map to the [[Def - Annihilator (Dual Space)|annihilator]] construction.

> [!tip] Adjoint Operator *(from Linear Algebra VII)*
> In an inner product space, every linear map $T : V \to W$ has an **adjoint** $T^* : W \to V$ defined by $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$. The adjoint is *not* the same as the dual map: it goes between $W$ and $V$, not between $W'$ and $V'$. But they are *related*: under the Riesz representation isomorphism $W \cong W'$, the adjoint $T^*$ corresponds to the dual $T'$. This is the deep reason for the notational clash between $T^*$ and $T'$ in different traditions.

> [!tip] Pullback of Differential Forms *(from Differential Geometry)*
> For a smooth map $f : M \to N$ of manifolds, the **pullback** $f^* \omega$ of a differential 1-form $\omega$ on $N$ is the form on $M$ defined pointwise as the dual map of the differential $df$. Higher-rank forms pull back similarly via tensor powers of the dual map. The whole calculus of differential forms — Stokes' theorem, de Rham cohomology, integration on manifolds — uses the pullback construction, which is the dual map applied pointwise on cotangent spaces.
