---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Alternating Tensor and Lambda k V Dual"
  - "Def - Smooth Manifold"
  - "Def - The Tangent Space"
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Def - Tensor Field on a Manifold"
  - "Def - Alternating Tensor Field"
  - "Def - Vector Bundle"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold (Hausdorff, second-countable, with or without boundary). $T_pM$ is the tangent space at $p \in M$ and $T_p^*M = (T_pM)^*$ is the cotangent space. $\Lambda^k T_p^*M = \Lambda^k(T_pM)^*$ is the space of alternating $k$-tensors on $T_pM$ (see [[Def - Alternating Tensor and Lambda k V Dual]]). $\Lambda^k T^*M = \coprod_{p \in M} \Lambda^k T_p^*M$ is the bundle of alternating $k$-tensors over $M$; its smooth structure makes it a smooth vector bundle of rank $\binom{n}{k}$ over $M$. Smooth sections of this bundle are written $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$. In a chart $(U, (x^1, \dots, x^n))$, the coordinate basis vector fields are $\partial/\partial x^i$ and the coordinate $1$-forms are $dx^i$, dual in the sense $dx^i(\partial/\partial x^j) = \delta^i_j$. For an increasing multi-index $I = (i_1 < \cdots < i_k)$, $dx^I = dx^{i_1} \wedge \cdots \wedge dx^{i_k}$. The primed sum $\sum'_I$ is taken over increasing multi-indices only. The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Axiom Motivation

Two desiderata, jointly, force the definition.

First, we want **the manifold version of the alternating multilinear integrand built in MA IV.** On $\mathbb{R}^n$, a differential $k$-form is a smooth field of alternating $k$-linear maps on tangent vectors, written $\alpha = \sum'_I a_I(x)\,dx^I$, designed so that its integral over an oriented $k$-surface is independent of parametrization. We want to lift this to a manifold $M$, which only locally looks like $\mathbb{R}^n$, and which has *no canonical chart*. The obstacle is that a global definition must reduce, in any chart, to the MA IV definition, and the chart formulas must agree on overlaps. The patching is non-trivial: under a coordinate change with Jacobian $J^i_j = \partial \tilde x^i/\partial x^j$, a $1$-form $\omega = \omega_i\,dx^i$ becomes $\omega = \tilde\omega_j\,d\tilde x^j$ with $\tilde\omega_j = (J^{-1})^i_j \omega_i$ — covariant transformation. For higher-degree forms, the patching multiplies by the determinant of an appropriate submatrix of the Jacobian, and the wedge product is structured precisely so this works (the wedge of $k$ one-forms transforms by the $k \times k$ minor determinants).

Second, we want **smoothness in $p$.** A "form" that consisted of an alternating tensor at each point with no smoothness assumption would be a pointwise object with no calculus on it; we could not differentiate, integrate, or pull back. The smoothness assumption is the *minimum* needed to make the exterior derivative and pullback well-defined, and (since $d^2 = 0$ involves equality of mixed partials) it must in fact be $C^\infty$, not merely $C^1$ or $C^k$. So a differential $k$-form on $M$ is a smooth section of the alternating-tensor bundle.

The cleanest way to package the two desiderata is to introduce the **bundle of alternating $k$-tensors**: a smooth manifold $\Lambda^k T^*M$ whose fibre over $p \in M$ is $\Lambda^k T_p^*M$, equipped with a projection $\pi : \Lambda^k T^*M \to M$ that makes it a smooth vector bundle of rank $\binom{n}{k}$. A differential $k$-form is then a smooth section of this bundle — a smooth choice of $\omega_p \in \Lambda^k T_p^*M$ for each $p$. The bundle structure is inherited from that of the [[Def - Cotangent Space and Cotangent Bundle|cotangent bundle]] $T^*M$ via the functorial $\Lambda^k$ construction (which respects the local-trivialization structure of $T^*M$). On overlaps the transition functions of $\Lambda^k T^*M$ are determined by those of $T^*M$ via $\Lambda^k$ of the transition; smoothness is preserved.

What breaks if we drop smoothness in $p$? The exterior derivative becomes undefined (we cannot differentiate the coefficient functions $\omega_I$ in any chart). The Lie derivative becomes undefined (the flow's effect on $\omega$ requires differentiability in $t$, which propagates to differentiability in $p$). The Stokes theorem becomes undefined (the integral $\int_M d\omega$ requires $d\omega$ to exist). The whole downstream theory rests on smoothness.

What breaks if we drop alternation — work with general covariant tensor fields? Then change-of-variables under coordinate change would multiply by the full Jacobian, not the determinant, and the integration theory would not be invariant. We *can* integrate general $n$-tensor fields by introducing a density — a non-alternating object that transforms by $|\det J|$ — but the resulting theory is what physicists call "integration of scalar fields against a volume measure" and is fundamentally different from "integration of forms over oriented submanifolds". Forms and densities are two different things; both have their uses, but for the de Rham theory and Stokes' theorem we want forms.

Why insist on the bundle formulation? Couldn't we just say "a differential $k$-form is a chart-by-chart assignment of alternating tensors satisfying the right transition rules"? Yes, and that is what the bundle formulation encodes — the bundle of alternating tensors is precisely the geometric object whose sections are exactly such chart-by-chart assignments. The bundle viewpoint is preferred because it makes the smooth structure visible: $\Lambda^k T^*M$ is itself a smooth $2n$-manifold (well, $n + \binom{n}{k}$-dimensional), and "smooth section of a vector bundle" is a standard concept. The chart-by-chart viewpoint hides the bundle structure but is equivalent.

---

# The Definition

**The bundle.** Let $M$ be a smooth $n$-manifold. The **bundle of alternating $k$-tensors on $M$** is
$$\Lambda^k T^*M = \coprod_{p \in M} \Lambda^k T_p^*M,$$
with projection $\pi : \Lambda^k T^*M \to M$ sending $\Lambda^k T_p^*M$ to $\{p\}$. Standard methods (Lee Exercise 14.14) show that $\Lambda^k T^*M$ is a smooth vector bundle of rank $\binom{n}{k}$ over $M$, with local trivializations inherited from those of the cotangent bundle: in a chart $(U, x^i)$, $\Lambda^k T^*M\big|_U$ is trivialized by the basis $\{dx^I : I \text{ increasing of length } k\}$.

**The forms.** A **differential $k$-form** (or simply a $k$-**form**) on $M$ is a smooth section of $\Lambda^k T^*M$. Explicitly, a smooth map $\omega : M \to \Lambda^k T^*M$ with $\pi \circ \omega = \operatorname{id}_M$, so that $\omega_p \in \Lambda^k T_p^*M$ for every $p$, and the assignment $p \mapsto \omega_p$ is smooth.

The set of smooth $k$-forms on $M$ is denoted
$$\Omega^k(M) = \Gamma(\Lambda^k T^*M).$$
By convention $\Omega^0(M) = C^\infty(M)$ (a $0$-form is a smooth function), and $\Omega^1(M)$ is the space of smooth covector fields ([[Def - Covector Field and Differential 1-Form]]). For $k > n$, $\Omega^k(M) = \{0\}$ (the fibres are zero by the dimension theorem).

**Coordinate expression.** In any smooth chart $(U, x^1, \dots, x^n)$, a $k$-form $\omega$ on $U$ has the unique expansion
$$\omega = \sum'_I \omega_I\,dx^I = \sum_{i_1 < \cdots < i_k} \omega_{i_1 \cdots i_k}(x)\,dx^{i_1} \wedge \cdots \wedge dx^{i_k},$$
with smooth coefficient functions $\omega_I : U \to \mathbb{R}$ defined by
$$\omega_I = \omega\!\left(\frac{\partial}{\partial x^{i_1}}, \dots, \frac{\partial}{\partial x^{i_k}}\right).$$
The form $\omega$ is smooth at $p \in U$ if and only if every $\omega_I$ is smooth at $p$ (which suffices because the $dx^I$ form a smooth local frame for $\Lambda^k T^*M$ on $U$).

**Action on vector fields.** A smooth $k$-form $\omega$ defines, by $\omega(X_1, \dots, X_k)(p) = \omega_p(X_{1,p}, \dots, X_{k,p})$, a $C^\infty(M)$-multilinear, alternating map $\mathfrak{X}(M)^k \to C^\infty(M)$, where $\mathfrak{X}(M)$ is the space of [[Def - Vector Field on a Manifold|smooth vector fields]] on $M$. Conversely, the **tensor characterization lemma** says that every $C^\infty(M)$-multilinear alternating map $\mathfrak{X}(M)^k \to C^\infty(M)$ arises this way — there is a bijection between differential $k$-forms and such maps. This is what allows definitions like "$\omega(X, Y) := X g - Y f$" to actually produce a $1$-form when $f, g$ are smooth functions.

**Vector-space structure and module structure.** $\Omega^k(M)$ is an $\mathbb{R}$-vector space (pointwise addition and scalar multiplication of forms). It is also a module over the ring $C^\infty(M)$: if $f \in C^\infty(M)$ and $\omega \in \Omega^k(M)$, then $(f\omega)_p = f(p)\,\omega_p$ is a smooth $k$-form, and $\Omega^k(M)$ is closed under these operations.

**Graded algebra structure.** Defining $\Omega^\bullet(M) = \bigoplus_{k=0}^n \Omega^k(M)$ and the wedge product pointwise (see [[Def - The Wedge Product on a Manifold]]), $\Omega^\bullet(M)$ becomes an associative graded-anticommutative algebra over $C^\infty(M)$.

---

# Categorical Definition

The differential $k$-forms on $M$ are the smooth sections of the bundle $\Lambda^k T^*M$, which is the $k$-th exterior power of the cotangent bundle. Functorially, the assignment $M \mapsto \Omega^k(M)$ is a **contravariant functor** from the category of smooth manifolds and smooth maps to the category of $\mathbb{R}$-vector spaces (and even to graded-commutative algebras when $k$ runs over all degrees and the wedge product is included). A smooth map $F : M \to N$ induces the **pullback** $F^* : \Omega^k(N) \to \Omega^k(M)$ in the *reverse* direction; contravariance is encoded in $(F \circ G)^* = G^* \circ F^*$. See [[Def - Pullback of a Differential Form on a Manifold]].

Contravariance is forced by the structure of forms: a form at $F(p) \in N$ eats tangent vectors at $F(p)$; tangent vectors at $p \in M$ are sent forward by $dF_p$; so a form on $N$ becomes a form on $M$ by *pulling back* — moving the form against the direction of the map, while tangent vectors move with the map. This is the structural advantage of forms over vector fields: pullback exists for every smooth $F$ (no diffeomorphism required), because we only ever need to push tangent vectors forward (which $dF_p$ does universally), not pull them back.

The functor $\Omega^k(\cdot)$ is moreover compatible with the wedge product (making $\Omega^\bullet(\cdot)$ a functor into DGAs once the exterior derivative is added) and with the exterior derivative (in the sense $F^*d = dF^*$, [[Thm - Pullback Commutes with d for Forms on Manifolds]]). These compatibilities are encoded as **naturality** in category theory: the differential $d$ is a natural transformation $\Omega^k \to \Omega^{k+1}$ between functors.

---

# Relate to Other Fields / Compression

**Bridge to MA IV.** A differential $k$-form on a manifold is, in any chart $(U, x^i)$ with $U$ open in $M$ and $x : U \to V \subseteq \mathbb{R}^n$ a diffeomorphism, identified by the pullback $(x^{-1})^*\omega$ with a [[Def - Differential Form|differential k-form on V]] in the MA IV sense. The whole MA IV machinery — wedge product, exterior derivative, pullback, Stokes' theorem on contractible domains — applies to the local representative, and the chart-overlap consistency is what makes the construction globally well-defined. **A differential $k$-form on $M$ is the manifold generalization of $\mathbb{R}^n$ differential forms, patched chart-by-chart**, with the wedge-as-determinant identity ensuring overlap consistency. The local theory is MA IV; the manifold theory is the global packaging.

**Bridge to tensor fields (DG VII).** A differential $k$-form is exactly an [[Def - Alternating Tensor Field|alternating covariant k-tensor field]], i.e., a section of the alternating subbundle $\Lambda^k T^*M \subset T^k T^*M$ of the bundle of covariant $k$-tensors. Every algebraic operation on tensor fields (pullback, contraction, symmetrization, alternation) restricts to forms. The new operation that *only* exists for forms is the exterior derivative; there is no analogous chart-independent first-order operator on general tensor fields without choosing a connection. This is the structural reason differential forms are a richer subject than tensor fields generally.

**Bridge to LA IX multilinear algebra.** Pointwise, $\Lambda^k T_p^*M$ is the alternating-tensor space of [[Def - Alternating Multilinear Form|LA IX]]; every algebraic property — dimension count, elementary basis, wedge product — propagates pointwise to the manifold setting. The smooth-section construction is what packages the pointwise multilinear algebra into a global geometric object.

**True name:** A differential $k$-form on $M$ is "the kind of object whose integral over an oriented $k$-submanifold is well-defined and coordinate-free". The pointwise alternating-tensor structure is the algebraic encoding of "behaves correctly under reorientation and reparametrization."

A trigger-reaction pattern: **see "compute an integral on a submanifold of dimension $k$" → think "the integrand should be a differential $k$-form"**. This pattern is what motivates the entire theory: the kind of object whose integral over an oriented $k$-surface is coordinate-free is, uniquely, a differential $k$-form.

**Bridge to bundles (DG VI).** $\Omega^1(M) = \Gamma(T^*M)$ is the space of [[Def - Covector Field and Differential 1-Form|smooth covector fields]] from DG VI. For higher $k$, the bundle $\Lambda^k T^*M$ is built from $T^*M$ by the functorial construction $E \mapsto \Lambda^k E$ on vector bundles — a special case of associated-bundle constructions. The general theory of [[Def - Vector Bundle|vector bundles]] applies: transition functions of $\Lambda^k T^*M$ are obtained from those of $T^*M$ by applying $\Lambda^k$, and local frames of $T^*M$ give local frames of $\Lambda^k T^*M$ by wedging.

---

# Examples / Corollaries

**Is an instance — a function as a $0$-form.** A smooth function $f \in C^\infty(M)$ is a $0$-form, so $\Omega^0(M) = C^\infty(M)$. The exterior derivative of $f$ is the $1$-form $df$, characterized by $df(X) = X(f)$ for every vector field $X$; in coordinates $df = \sum_i (\partial f/\partial x^i)\,dx^i$.

**Is an instance — coordinate $1$-forms $dx^i$.** In a chart $(U, x^i)$, each coordinate function $x^i$ is smooth, so $dx^i$ is a smooth $1$-form on $U$. The family $\{dx^i\}$ is a basis of $T_p^*M$ at each $p \in U$, dual to $\{\partial/\partial x^i\}$. These local $1$-forms are the building blocks for all higher-degree forms via the wedge.

**Is an instance — the angular form on the punctured plane.** On $M = \mathbb{R}^2 \setminus \{0\}$, the $1$-form $\omega = \frac{-y\,dx + x\,dy}{x^2 + y^2}$ is smooth (the denominator never vanishes). It is closed ($d\omega = 0$) but not exact (no global function $\theta$ exists with $d\theta = \omega$, even though *locally* $\omega = d\theta$ where $\theta$ is the angle coordinate). It is the prototypical representative of a nonzero de Rham cohomology class. See [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]].

**Is an instance — the volume form on an oriented Riemannian manifold.** On an oriented Riemannian $n$-manifold $(M, g)$, the Riemannian **volume form** is the unique top-degree form $\operatorname{vol}_g \in \Omega^n(M)$ that on an oriented orthonormal frame $\{e_i\}$ gives $\operatorname{vol}_g(e_1, \dots, e_n) = 1$. In coordinates $\operatorname{vol}_g = \sqrt{\det g_{ij}}\,dx^1 \wedge \cdots \wedge dx^n$. It is the integrand of "volume of a region" in Riemannian geometry. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]] and [[Def - Riemannian Volume Form]].

**Is NOT an instance — a vector field.** A vector field on $M$ is a section of $TM$, not of $\Lambda^k T^*M$. Vector fields and $1$-forms are *dual* but not the same: $X \in \mathfrak{X}(M)$ acts on functions ($X : C^\infty(M) \to C^\infty(M)$), while $\omega \in \Omega^1(M)$ acts on vector fields ($\omega : \mathfrak{X}(M) \to C^\infty(M)$). The musical isomorphism $\flat : TM \to T^*M$ from a Riemannian metric identifies them, but the identification is metric-dependent. In particular, vector fields cannot be pulled back along smooth maps (only along diffeomorphisms via pushforward of vectors and then inverse), while forms can.

**Is NOT an instance — a symmetric $2$-tensor field.** The Riemannian metric $g_p : T_pM \times T_pM \to \mathbb{R}$ is a smooth symmetric $(0, 2)$-tensor field, not an alternating one. It is *not* a $2$-form. The wedge of two $1$-forms gives a $2$-form, but the symmetric product of two $1$-forms gives a symmetric tensor, not a form.

**Is NOT an instance — a $k$-form with $k > \dim M$.** $\Omega^k(M) = \{0\}$ for $k > n = \dim M$, since $\Lambda^k T_p^*M = \{0\}$ pointwise. This makes the de Rham complex $\Omega^0(M) \to \Omega^1(M) \to \cdots \to \Omega^n(M)$ finite, ending at degree $n$.

**Corollary — local representation always exists.** Every $k$-form $\omega$ on $M$ admits, in every chart $(U, x^i)$, a unique expansion $\omega|_U = \sum'_I \omega_I\,dx^I$ with smooth $\omega_I$. Smoothness of $\omega$ is equivalent to smoothness of every $\omega_I$ in every chart. This local representation is what every computation reduces to.

**Corollary — vector-space dimension at a point.** $\dim_{\mathbb{R}} \Lambda^k T_p^*M = \binom{n}{k}$, with maximum at $k = \lfloor n/2 \rfloor$ and the palindrome $\binom{n}{k} = \binom{n}{n-k}$. Total dimension $\sum_k \binom{n}{k} = 2^n$. On $\mathbb{R}^3$ the dimensions are $1, 3, 3, 1$ — the source of the dimension-three coincidence that lets $1$-forms and $2$-forms both be disguised as vector fields.

**Corollary — tensor-characterization for forms.** A $C^\infty(M)$-multilinear, alternating map $\mathfrak{X}(M)^k \to C^\infty(M)$ is equivalent to a smooth $k$-form on $M$. The proof reduces to showing that a $C^\infty(M)$-multilinear map is *pointwise* (i.e., $\omega(X_1, \dots, X_k)(p)$ depends only on $X_{i,p}$), which uses partitions of unity to localize.

**Calibration check.** Verify $\Omega^2(\mathbb{R}^2) = C^\infty(\mathbb{R}^2)\,dx \wedge dy$ has $1$ generator; verify $\Omega^1(M)$ on a $3$-manifold has $\binom{3}{1} = 3$ local coefficients per chart; check that on $S^1$ (a $1$-manifold), $\Omega^1(S^1)$ is one-dimensional as a $C^\infty(S^1)$-module; explain why $\Omega^4(S^3) = 0$. If you can also explain why a $2$-form on a $3$-manifold has the "same shape" (componentwise) as a vector field but transforms differently under coordinate change, you have understood the dimensional coincidence.

---

# Unlocked by This

> [!tip] The Exterior Derivative *(this chapter)*
> Once we have $\Omega^k(M)$, the [[Def - Exterior Derivative on a Manifold|exterior derivative]] $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is the canonical first-order operator: linear, satisfies graded Leibniz, squares to zero, extends the differential of functions. The whole de Rham theory follows.

> [!tip] Integration over Oriented Submanifolds *(from Differential Geometry IX)*
> A compactly supported $k$-form on an oriented $k$-manifold (or on an embedded oriented $k$-submanifold of a larger manifold) has a well-defined integral $\int_M \omega \in \mathbb{R}$, computed patch by patch via charts. The integral is independent of the choice of oriented charts, courtesy of the determinant-convention wedge identity. This is the start of [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> The complex $\Omega^0(M) \to \Omega^1(M) \to \cdots \to \Omega^n(M)$ with differential $d$ has cohomology $H^k_{dR}(M) = \ker d / \operatorname{im} d$ — the **de Rham cohomology** of $M$. By **de Rham's theorem** these are isomorphic to the singular cohomology groups of $M$ with real coefficients, making $H^k_{dR}(M)$ a topological invariant computable from calculus.

> [!tip] Symplectic and Contact Geometry *(from Geometric Mechanics)*
> A **symplectic manifold** is an even-dimensional manifold with a closed non-degenerate $2$-form. A **contact manifold** is an odd-dimensional one with a maximally non-integrable hyperplane field, encoded by a $1$-form $\alpha$ satisfying $\alpha \wedge (d\alpha)^n \neq 0$. Both structures are differential forms with prescribed algebraic and differential properties, and their study is geometric mechanics.

> [!tip] Maxwell's Equations on Spacetime *(from Electromagnetism)*
> The electromagnetic field strength is a $2$-form $F$ on $4$-dimensional spacetime. The homogeneous Maxwell equations are $dF = 0$ (Bianchi identity), and the inhomogeneous ones are $d\star F = J$ for the current $1$-form $J$ and Hodge dual $\star F \in \Omega^2(M)$. The whole structure of classical electromagnetism is the calculus of a single $2$-form on a Lorentzian $4$-manifold.
