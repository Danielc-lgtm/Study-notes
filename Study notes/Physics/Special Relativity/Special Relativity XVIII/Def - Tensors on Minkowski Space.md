---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Four-Vector"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The vector space underlying [[Def - Minkowski Space and the Metric|Minkowski space]] is $E$ (four-dimensional, real); its **dual** $E^*$ is the space of linear forms $\omega : E \to \mathbb{R}$. A basis of $E$ is written $(e_\alpha)_{\alpha = 0,1,2,3}$, not necessarily orthonormal; its [[Def - Metric Duality and Index Manipulation|dual basis]] $(e^\alpha)$ of $E^*$ satisfies $\langle e^\alpha, e_\beta\rangle = \delta^\alpha{}_\beta$. Greek indices run $0$–$3$; the **Einstein summation convention** sums a repeated index appearing once up and once down. Vectors carry upper indices $X^\mu$; linear forms carry lower indices $\omega_\mu$; the action of a form on a vector is $\langle\omega, X\rangle = \omega_\mu X^\mu$. The metric components are $\eta_{\mu\nu} = g(e_\mu, e_\nu)$ in an orthonormal basis (more generally $g_{\alpha\beta}$), with inverse $\eta^{\mu\nu}$ ($\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu$). Full registry on [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

> [!warning] Convention: tensor type and signature
> We follow Gourgoulhon's **type $(k,\ell)$** convention: a type $(k,\ell)$ tensor eats $k$ **forms** and $\ell$ **vectors** — it is $k$ times contravariant and $\ell$ times covariant. (Some texts write $(p,q)$ for the same thing, others swap the slots; always check which factor counts up-indices.) Separately, Gourgoulhon's book uses the opposite metric signature $\mathrm{diag}(-1,+1,+1,+1)$; we translate to mostly-minus throughout. For a *vector* this flips the sign convention on lowering ($X_i = -X^i$ here), exactly as on [[Def - Metric Duality and Index Manipulation]] — but note that almost every *structural* tensor identity in this chapter depends only on $\det g < 0$, which holds in both signatures, so the formulas transcribe unchanged.

---

# Axiom Motivation

By the time relativity has built [[Def - Four-Vector|four-vectors]], linear forms, the [[Def - Minkowski Space and the Metric|metric]] $g$ (a symmetric bilinear form), the angular-momentum bilinear form (antisymmetric), the mixed product of an observer's local space (a trilinear form), the [[Def - The Levi-Civita Tensor|Levi-Civita]] four-linear form, and the [[Def - The Lorentz Group|Lorentz transformations]] (linear maps $E \to E$), it has accumulated a zoo of objects that *look* unrelated. The single observation that organises the whole zoo is this: every one of them is a **multilinear map** built from copies of $E$ and $E^*$ landing in $\mathbb{R}$. A four-vector is a linear map $E^* \to \mathbb{R}$; a form is a linear map $E \to \mathbb{R}$; the metric is a bilinear map $E \times E \to \mathbb{R}$; a Lorentz transformation, viewed correctly, is a bilinear map $E^* \times E \to \mathbb{R}$. The concept of **tensor** is the umbrella that contains them all, and the design decision is to define a tensor *by what it eats and the rule it obeys*, never by a list of components.

This frame-independence is the entire point, and it is worth being precise about why the component-first definition is the wrong one. An older tradition (Gourgoulhon's Remark 14.2) defines a tensor as "an array of numbers $T^{\alpha_1\dots\alpha_k}{}_{\beta_1\dots\beta_\ell}$ that transforms in a particular way under a change of basis." This is operationally fine but conceptually backwards: it makes the *components* primary and the object secondary, so that one is forever checking whether a given array "is a tensor" by verifying a transformation law. The multilinear-map definition inverts this. The tensor *is* the map; its components in a basis are merely its values on the basis vectors and dual-basis forms, and the transformation law is then a *theorem* (a consequence of how bases change), not a definition. This is the same move that made [[Def - Four-Vector|four-vectors]] geometric objects rather than tuples, and the same move that, in [[Def - The Total Derivative and Differentiability|multivariate analysis]], makes the derivative a linear map rather than a Jacobian matrix.

Why insist on *multi*linearity rather than some weaker condition? Linearity in each slot separately is exactly the condition that makes the object compatible with the linear structure of spacetime — it is what guarantees that the tensor commutes with taking linear combinations of vectors, hence that its action is determined by its action on a basis (finitely many numbers), hence that it has well-defined components at all. Drop linearity in even one slot and the "tensor" would no longer be reconstructible from finite data, and the transformation law under $\Lambda$ would collapse. Multilinearity is the minimal hypothesis under which "a map of several vector and form arguments" becomes a finite-dimensional, basis-expandable object.

The slot structure — $k$ form-slots and $\ell$ vector-slots — is forced by the requirement that the **metric** be available to convert one into the other. Because $g$ is non-degenerate, [[Def - Metric Duality and Index Manipulation|metric duality]] identifies $E$ with $E^*$, so a form-slot and a vector-slot are interconvertible by raising or lowering an index. This is why one does not, in relativity, fuss over the *individual* numbers $k$ and $\ell$ so much as their sum: the **valence** (or order, or rank) $k + \ell$ is the robust invariant, because raising and lowering shuffle indices between up and down without changing the total count. A tensor "of valence $2$" can present as $T^{\mu\nu}$, $T^\mu{}_\nu$, or $T_{\mu\nu}$, and these are the same abstract object viewed through three index placements. The definition must therefore be flexible enough to allow any distribution of the $k + \ell$ slots, which is exactly what the type-$(k,\ell)$ family provides.

One small but load-bearing convention closes the construction: $E$ itself is recovered as type $(1,0)$. A vector $\vec v$ acts on a form by $\vec v(\omega) := \langle\omega, \vec v\rangle$, which is linear in $\omega$, so $\vec v$ is a tensor of type $(1,0)$ — a linear map $E^* \to \mathbb{R}$. This uses the canonical identification $E^{**} \cong E$ (every vector is a linear form on $E^*$), and it is the reason the contravariant index of a vector sits upstairs. Likewise an endomorphism $L : E \to E$ becomes a type $(1,1)$ tensor via $L(\omega, \vec v) := \langle\omega, L(\vec v)\rangle$. With these identifications the tensor framework swallows vectors, forms, bilinear forms, and linear maps as special cases, and there is exactly one kind of object to reason about.

---

# The Definition

For $(k,\ell) \in \mathbb{N}^2$ with $(k,\ell) \neq (0,0)$, a **tensor of type $(k,\ell)$** on $E$ is a map
$$
T : \underbrace{E^* \times \cdots \times E^*}_{k\text{ times}} \times \underbrace{E \times \cdots \times E}_{\ell\text{ times}} \longrightarrow \mathbb{R},
\qquad
(\omega_1, \dots, \omega_k, \vec v_1, \dots, \vec v_\ell) \longmapsto T(\omega_1, \dots, \omega_k, \vec v_1, \dots, \vec v_\ell),
$$
that is **linear with respect to each of its arguments** (multilinear). The integer $k + \ell$ is the **valence**, **order**, or **rank** of $T$; one says $T$ is $k$ times contravariant and $\ell$ times covariant. The set of all type-$(k,\ell)$ tensors is a real vector space $\mathscr{T}_{(k,\ell)}(E)$ of dimension $4^{k+\ell}$. By convention $\mathscr{T}_{(0,0)}(E) := \mathbb{R}$.

Through canonical identifications, the framework absorbs familiar objects:
$$
\mathscr{T}_{(1,0)}(E) = E, \qquad \mathscr{T}_{(0,1)}(E) = E^*, \qquad \mathscr{T}_{(1,1)}(E) = \mathscr{L}(E),
$$
where $\mathscr{L}(E)$ is the space of endomorphisms (linear maps $E \to E$): a vector $\vec v$ is the tensor $\omega \mapsto \langle\omega, \vec v\rangle$, and an endomorphism $L$ is the tensor $(\omega, \vec v) \mapsto \langle\omega, L(\vec v)\rangle$. In particular the metric $g$ is type $(0,2)$, the Levi-Civita tensor is type $(0,4)$, a [[Def - The Lorentz Group|Lorentz transformation]] is type $(1,1)$, and the angular-momentum bilinear form is type $(0,2)$.

**Components.** Given a basis $(e_\alpha)$ of $E$ and its [[Def - Metric Duality and Index Manipulation|dual basis]] $(e^\alpha)$, the **components** of $T$ are the $4^{k+\ell}$ real numbers
$$
T^{\alpha_1\dots\alpha_k}{}_{\beta_1\dots\beta_\ell} \;=\; T\big(e^{\alpha_1}, \dots, e^{\alpha_k}, e_{\beta_1}, \dots, e_{\beta_\ell}\big),
$$
and $T$ is reconstructed from them by the expansion
$$
T \;=\; T^{\alpha_1\dots\alpha_k}{}_{\beta_1\dots\beta_\ell}\; e_{\alpha_1} \otimes \cdots \otimes e_{\alpha_k} \otimes e^{\beta_1} \otimes \cdots \otimes e^{\beta_\ell},
$$
where $\otimes$ is the [[Def - Tensor Operations|tensor product]]. Its action on arguments is read off the components by
$$
T(\omega_1, \dots, \omega_k, \vec v_1, \dots, \vec v_\ell) \;=\; T^{\alpha_1\dots\alpha_k}{}_{\beta_1\dots\beta_\ell}\,(\omega_1)_{\alpha_1}\cdots(\omega_k)_{\alpha_k}\, v_1^{\beta_1}\cdots v_\ell^{\beta_\ell}.
$$

**Change of basis.** If $(e'_\alpha)$ is a second basis with change-of-basis matrix $P$ defined by $e'_\alpha = P^\beta{}_\alpha\, e_\beta$ (so the dual bases satisfy $e'^\alpha = (P^{-1})^\alpha{}_\beta\, e^\beta$), the components transform by one factor of $P^{-1}$ per upper index and one factor of $P$ per lower index:
$$
T'^{\alpha_1\dots\alpha_k}{}_{\beta_1\dots\beta_\ell} \;=\; (P^{-1})^{\alpha_1}{}_{\mu_1}\cdots(P^{-1})^{\alpha_k}{}_{\mu_k}\; P^{\nu_1}{}_{\beta_1}\cdots P^{\nu_\ell}{}_{\beta_\ell}\; T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_\ell}.
$$
For two inertial frames the change-of-basis matrix is $P = \Lambda^{-1}$ where $\Lambda$ is the restricted [[Def - The Lorentz Group|Lorentz transformation]] relating them. Special cases: a vector transforms by $v'^\alpha = (P^{-1})^\alpha{}_\beta v^\beta$, a form by $\omega'_\alpha = P^\beta{}_\alpha \omega_\beta$, a bilinear form by the matrix law $T' = {}^{t}P\, T\, P$, and an endomorphism by $T' = P^{-1} T P$.

---

# Categorical / Structural Definition

The space $\mathscr{T}_{(k,\ell)}(E)$ is, canonically, an iterated [[Def - Tensor Product of Vector Spaces|tensor product]]:
$$
\mathscr{T}_{(k,\ell)}(E) \;\cong\; \underbrace{E \otimes \cdots \otimes E}_{k} \otimes \underbrace{E^* \otimes \cdots \otimes E^*}_{\ell}.
$$
This is the precise content of the expansion above: the elementary tensors $e_{\alpha_1}\otimes\cdots\otimes e^{\beta_\ell}$ form a basis, and a general tensor is a linear combination of them with the components as coefficients. The identification rests on the [[Thm - Universal Property of the Tensor Product|universal property of the tensor product]]: multilinear maps out of $E^* \times \cdots \times E$ are in natural bijection with linear maps out of $E^{**}\otimes\cdots\otimes E^* \cong E\otimes\cdots\otimes E^*$, so "multilinear map" and "element of the tensor-product space" are two descriptions of the same object. A tensor is therefore both a multilinear form (its operational face) and a vector in a tensor-product space (its algebraic face), and the two faces are interchanged by this universal property.

The transformation law has a clean representation-theoretic reading. The [[Def - The Lorentz Group|Lorentz group]] acts on $E$ by its defining representation and on $E^*$ by the dual (contragredient) representation; $\mathscr{T}_{(k,\ell)}(E)$ then carries the tensor-product representation, $k$ copies of the defining and $\ell$ of the dual. The component transformation rule — one $P^{-1}$ per up-index, one $P$ per down-index — is exactly the statement that the components are the coordinates of a vector in this tensor-product representation. Because the metric supplies an invariant non-degenerate bilinear form, the defining and dual representations are *equivalent* (this is [[Def - Metric Duality and Index Manipulation|metric duality]]), which is the structural reason indices can be raised and lowered without leaving the isomorphism class of the tensor: $T^{\mu\nu}$, $T^\mu{}_\nu$, $T_{\mu\nu}$ all represent the same orbit.

The functor $E \mapsto \mathscr{T}_{(k,\ell)}(E)$ is covariant in the contravariant slots and contravariant in the covariant slots; a [[Def - The Lorentz Group|Lorentz transformation]] $\Lambda \in \mathscr{L}(E)$ pushes a type-$(k,\ell)$ tensor forward by acting with $\Lambda$ on each $E$-factor and $(\Lambda^{-1})^{t}$ on each $E^*$-factor, which is precisely the transformation law.

---

# Relate to Other Fields / Compression

A tensor on Minkowski space is the special case, with $E$ a *fixed* four-dimensional space and the [[Def - The Lorentz Group|Lorentz group]] the structure group, of a **tensor field on a manifold**. On a [[Def - Riemannian Manifold|(pseudo-)Riemannian manifold]] one has at each point a tangent space $T_pM$ and its dual $T_p^*M$, and a tensor field assigns to each point a tensor of type $(k,\ell)$ on $T_pM$, varying smoothly; the change-of-basis law becomes the change-of-coordinates (Jacobian) law, and the constant matrix $P = \Lambda^{-1}$ is replaced by the position-dependent Jacobian $\partial x'^\alpha/\partial x^\beta$. Special relativity is the flat, constant-metric corner of that theory, where every tangent space is the same $E$ and the only changes of basis are global linear maps.

The component bookkeeping — upper indices contravariant, lower indices covariant, summation only over an up–down pair — is the **abstract-index calculus** of Penrose, and it is the computational engine of general relativity, gauge theory, and continuum mechanics. The stress tensor of elasticity, the moment-of-inertia tensor of rigid-body dynamics, and the conductivity tensor of a crystal are all type-$(0,2)$ or type-$(1,1)$ tensors in exactly this sense — multilinear maps whose components rotate correctly under a change of orthonormal frame.

**True name:** a tensor is *a multilinear gadget identified with its components in any one basis, the components in every other basis being fixed by the up-$P^{-1}$/down-$P$ rule*. The operational reflex it installs: to decide whether a candidate array "is a tensor," do not check a transformation law by hand — instead exhibit it as a multilinear map (it eats so many forms and so many vectors and returns a number), and the transformation law follows for free. Conversely, an equation is **Lorentz covariant** — true in every frame — exactly when it equates tensors of the same type with all free indices matching and every summed index appearing once up, once down.

---

# Examples / Corollaries

**Is an instance — the metric.** $g$ is a type $(0,2)$ tensor, $g(\vec u, \vec v) = g_{\alpha\beta}u^\alpha v^\beta$, with components $g_{\alpha\beta} = g(e_\alpha, e_\beta)$ — in an orthonormal basis these are $\eta_{\alpha\beta} = \mathrm{diag}(1,-1,-1,-1)$. It is symmetric: $g_{\alpha\beta} = g_{\beta\alpha}$.

**Is an instance — the inverse metric.** The numbers $g^{\alpha\beta}$ (inverse matrix of $g_{\alpha\beta}$) are the components of a type $(2,0)$ tensor $g^{-1} = g^{\alpha\beta}\, e_\alpha\otimes e_\beta$; it is the tensor that *raises* indices, just as $g$ *lowers* them.

**Is an instance — a Lorentz transformation.** $\Lambda$ is a type $(1,1)$ tensor with components $\Lambda^\mu{}_\nu$; viewed as an endomorphism it sends $\vec v \mapsto \Lambda(\vec v)$ with $(\Lambda \vec v)^\mu = \Lambda^\mu{}_\nu v^\nu$. The single contraction of its one upper with its one lower index is its **trace**, $\Lambda^\mu{}_\mu$.

**Is NOT an instance — the coordinate tuple of a single event.** The four numbers $x^\mu = (t,x,y,z)$ of one event do *not* form the components of a tensor, because under a [[Def - The Poincaré Group|Poincaré]] change of origin they shift inhomogeneously, $x^\mu \mapsto \Lambda^\mu{}_\nu x^\nu + a^\mu$, which is not the homogeneous tensor law. A *difference* of two such tuples, $\Delta x^\mu$, is a genuine type-$(1,0)$ tensor (a [[Def - Four-Vector|four-vector]]).

**Is NOT an instance — an array with a "bad" index.** Writing $T^{\mu\mu}$ (a repeated *upper* index) is not a contraction and does not denote a tensor component; a legal contraction pairs one upper with one lower index, $T^\mu{}_\mu$. Tong's slogan: an expression like $X^\mu X^\mu$ is "illegal" in relativity, because it is not Lorentz invariant — the invariant is $X^\mu X_\mu = \eta_{\mu\nu}X^\mu X^\nu$.

**Corollary — components are basis values.** For a vector, $v^\alpha = \langle e^\alpha, \vec v\rangle$; for a form, $\omega_\alpha = \langle\omega, e_\alpha\rangle$. These recover the ordinary notion of "components in a basis," now seen as the tensor evaluated on dual-basis forms / basis vectors.

**Corollary — the action collapses to a contraction.** $\langle\omega, \vec v\rangle = \omega_\alpha v^\alpha$: the pairing of a form with a vector is the contraction of their components, one index up, one down. This is the prototype of every tensor contraction.

**Calibration check.** If you have understood the definition you can: (i) explain why a four-vector is a type $(1,0)$ tensor and write down the form it represents on $E^*$; (ii) given $g_{\alpha\beta}u^\alpha v^\beta$, identify the type and valence of $g$ and state how its components change under $P = \Lambda^{-1}$; (iii) say why $x^\mu$ is not a tensor but $\Delta x^\mu$ is.

---

# Unlocked by This

> [!tip] Operations on Tensors — Product, Contraction, Duality *(from §18.1)*
> With tensors defined as multilinear maps, the three operations that generate all of tensor algebra — the [[Def - Tensor Operations|tensor product]] $\otimes$ (build higher-valence tensors), **contraction** (sum an upper against a lower index, lowering valence by two), and [[Def - Metric Duality and Index Manipulation|metric duality]] (raise and lower with $g$) — turn $\bigoplus_{k,\ell}\mathscr{T}_{(k,\ell)}(E)$ into a single closed algebra. Every relativistic computation is a sequence of these three moves.

> [!tip] Alternate Forms and the Exterior Algebra *(from §18.2)*
> The fully antisymmetric type-$(0,p)$ tensors are the [[Def - Alternate Forms and the Exterior Product|p-forms]], the subspace on which the [[Def - The Hodge Star|exterior calculus]] lives. They are the tensors that integrate over $p$-dimensional surfaces and the ones from which the electromagnetic field is built.

> [!tip] The Energy-Momentum Tensor and the Stress of Fields *(from QFT and General Relativity)*
> The most physically central tensor of relativity is the symmetric type-$(2,0)$ **energy-momentum tensor** $T^{\mu\nu}$, whose components package energy density, momentum density, and stress, and which is the source term of the Einstein field equations. Its conservation law $\partial_\mu T^{\mu\nu} = 0$ is a tensor equation, hence holds in every frame; see [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!tip] Tensor Fields, the Covariant Derivative, and Curvature *(from General Relativity)*
> Letting the tensor vary from event to event gives a **tensor field**, and differentiating it requires the [[Def - The Covariant Derivative|covariant derivative]] $\nabla$ (since the naive partial derivative of components is not itself a tensor in curvilinear coordinates). The failure of second covariant derivatives to commute is the **Riemann curvature tensor** — the type-$(1,3)$ tensor that measures gravitation. Special relativity is where this machinery is assembled on flat spacetime, with curvature zero; see [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]].
