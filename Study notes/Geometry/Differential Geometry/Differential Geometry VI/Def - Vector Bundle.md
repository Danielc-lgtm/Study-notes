---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Diffeomorphism"
  - "Def - Vector Space"
  - "Def - Linear Map"
tags: [geometry, differential-geometry, bundles]
---

# Notation

$M$ is a smooth manifold of dimension $n$, possibly with boundary, with smooth structure as in [[Def - Smooth Manifold]]. The candidate bundle is denoted $\pi : E \to M$, with $E$ called the **total space**, $M$ the **base manifold**, and $\pi$ the **projection**. The pre-image $E_p := \pi^{-1}(p) \subseteq E$ is the **fibre** over $p$ — a vector space of dimension $k$, the **rank** of the bundle. The full registry of bundle notation is on [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

The standing convention: "vector bundle" without further qualification means a *smooth real* vector bundle of finite rank $k$. Complex vector bundles replace $\mathbb{R}^k$ with $\mathbb{C}^k$ and $\mathrm{GL}(k, \mathbb{R})$ with $\mathrm{GL}(k, \mathbb{C})$; the structural theory is parallel and is deferred. "Topological" or "continuous" vector bundles drop the smoothness requirement on charts and trivializations and live in a separate (mostly larger) world; the smooth and topological theories coincide on smooth manifolds whenever the bundle is paracompact-friendly, but the conventions of this topic are smooth throughout.

---

# Axiom Motivation

The vector bundle is what you build when you want to **vary a vector space smoothly with a point on a manifold**. The motivating examples are intrinsic to manifold theory: at each point $p$ of a smooth manifold $M$, the tangent space $T_pM$ is a real vector space of [[Def - Dimension|dimension]] $n = \dim M$, but the various $T_pM$ for different $p$ are different vector spaces, and a tangent vector at $p$ cannot be compared with or added to a tangent vector at $q$. Yet we want to talk about "the tangent bundle", a single geometric object that knows about all the tangent spaces simultaneously, and on which we can define smoothness of vector fields. The vector bundle is the data structure that answers this need; the definition we give is the minimal one that supports this.

Begin with the desiderata. We want a single space $E$ whose points are pairs $(p, v)$ with $v \in V_p$ for some vector space $V_p$ depending on $p$; the points $(p, v_1)$ and $(p, v_2)$ should be addable (because the $v$'s live in the same vector space) but $(p, v)$ and $(q, w)$ for $p \neq q$ should not be addable (because they live in different vector spaces). We need a projection $\pi : E \to M$ recording $\pi(p, v) = p$, so that the fibre $\pi^{-1}(p)$ is exactly $V_p$. And we need to say what "smoothly varying" means, so that smooth sections — smooth choices of $v \in V_p$ for each $p$ — are well-defined.

The decisive idea is to demand **local triviality**: locally on $M$, the bundle should look like a product. Specifically, $M$ should have an open cover $\{U_\alpha\}$ such that on each $U_\alpha$ there exists a diffeomorphism $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ commuting with the projection (so the fibre over $p \in U_\alpha$ goes to $\{p\} \times \mathbb{R}^k$) and linear on each fibre (so the vector-space structure on $V_p$ is the one $\Phi_\alpha$ pulls back from $\{p\} \times \mathbb{R}^k$). This single condition does three jobs at once. It supplies smooth coordinates on $E$ (the manifold structure on $E$ is forced by the diffeomorphism); it supplies the vector-space structure on each $V_p$ (which is the one inherited from $\mathbb{R}^k$ via $\Phi_\alpha$, well-defined because the transitions are linear); and it supplies the meaning of "smooth section" (a section is smooth at $p$ if and only if its expression in any local trivialization is smooth).

Why **local** triviality rather than global triviality? Because global triviality is too strong. The Möbius bundle over $S^1$, the tangent bundle of $S^2$, the canonical line bundle on $\mathbb{CP}^n$ — all these are genuine vector bundles, all the natural examples — fail to be globally trivial. If we demanded $E = M \times \mathbb{R}^k$ globally, we would exclude precisely the bundles that motivate the theory. Local triviality is the strongest condition that admits the interesting examples and that suffices to define smoothness.

What is forced by demanding the trivializations be **linear on fibres**? Without this, the vector-space structure on the fibre would not be well-defined — two different trivializations might disagree about which $v$'s sum to give which third $v$. The linearity condition is exactly what makes the transition $\Phi_\alpha \circ \Phi_\beta^{-1}$ on a fibre land in $\mathrm{GL}(k, \mathbb{R})$, so the vector-space structure is independent of trivialization. Drop linearity and you get a **fibre bundle** with fibre $\mathbb{R}^k$ but no linear structure — a genuinely different (and more general) object, important in its own right but not a *vector* bundle.

What is forced by demanding the trivializations be **[[Def - Diffeomorphism|diffeomorphisms]]** rather than just bijections? Without this, the total space $E$ would inherit no smooth structure from the trivializations, and "smooth section" would be undefined. The diffeomorphism condition is the technical content of "smoothly varying": it says the local picture of the bundle is a smooth product, and the smooth structure on $E$ is forced uniquely by this requirement. Drop the diffeomorphism condition (or weaken it to [[Def - Homeomorphism|homeomorphism]]) and you get a **topological vector bundle**, where sections can be continuous but not differentiated.

What if we **strengthened** the definition by demanding global triviality? Then we would have only product bundles $M \times \mathbb{R}^k$, and the entire theory would collapse — there would be nothing to say about tangent bundles of curved manifolds beyond ordinary multivariable calculus. The Möbius bundle, $TS^2$, $TS^3 = S^3 \times \mathbb{R}^3$ being trivial while $TS^2$ is not — these phenomena would all vanish, and with them the geometric content of vector-bundle theory. So global triviality is too strong precisely because it excludes the interesting examples.

What if we **weakened** by allowing the fibre dimension to vary with $p$? Then we would have a *family of vector spaces over $M$* but no bundle in the strict sense — the local triviality with a fixed $\mathbb{R}^k$ would fail at points where the dimension jumps. Such families do arise (the bundle of differentials of a map of nonconstant rank, for instance) and have their own theory, but they are not vector bundles in our sense. The constant-rank condition is what makes local triviality possible and what gives the theory its uniform structure.

In summary, the four ingredients — total space $E$, projection $\pi : E \to M$, fibrewise vector-space structure, and local triviality — are each forced by one feature of "smoothly varying family of vector spaces over $M$". Total space and projection make $E$ a single geometric object indexed by $M$; the vector-space structure on fibres makes it a *vector* family; local triviality makes the family smoothly varying with a fixed-dimensional model fibre $\mathbb{R}^k$. Drop any one and you lose exactly that feature.

---

# The Definition

Let $M$ be a smooth manifold (possibly with boundary). A **smooth real vector bundle of rank $k$ over $M$** is the data of:

1. A smooth manifold $E$ (with or without boundary) called the **total space**.
2. A smooth surjection $\pi : E \to M$ called the **projection**.
3. For each $p \in M$, a real vector space structure on the fibre $E_p := \pi^{-1}(p)$ of dimension $k$.

This data is required to satisfy the **local triviality condition**: for every $p \in M$ there exist an open neighbourhood $U \subseteq M$ of $p$ and a diffeomorphism $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$ such that:

- (compatibility with projection) $\pi_1 \circ \Phi = \pi$, where $\pi_1 : U \times \mathbb{R}^k \to U$ is projection on the first factor;
- (linearity on fibres) for every $q \in U$, the restriction $\Phi|_{E_q} : E_q \to \{q\} \times \mathbb{R}^k$ is a linear isomorphism of vector spaces (where $\{q\} \times \mathbb{R}^k$ carries the obvious linear structure).

Such a $\Phi$ is called a **smooth local trivialization** of $E$ over $U$; see [[Def - Local Trivialization]]. The bundle is **trivial** if a global trivialization $E \to M \times \mathbb{R}^k$ exists. A **(smooth) section** of $E$ is a smooth map $\sigma : M \to E$ with $\pi \circ \sigma = \mathrm{id}_M$; see [[Def - Section of a Vector Bundle]]. The space of smooth global sections is denoted $\Gamma(E)$ and is a module over $C^\infty(M)$.

When the rank is $k = 1$ the bundle is called a **line bundle**. The standing examples to remember are the trivial bundle $M \times \mathbb{R}^k$, the tangent bundle $TM$ (rank $n = \dim M$, see [[Def - The Tangent Bundle]]), the cotangent bundle $T^*M$ (also rank $n$, see [[Def - Cotangent Space and Cotangent Bundle]]), and the Möbius bundle over $S^1$ (rank $1$, nontrivial).

---

# Categorical Definition

Vector bundles over $M$ form a category, and the categorical perspective sharpens both the definition and the consequences.

**The category $\mathbf{Vect}_M$.** Fix a smooth manifold $M$. The objects of the category $\mathbf{Vect}_M$ of smooth vector bundles over $M$ are smooth vector bundles $\pi : E \to M$, of any finite rank. A morphism from $\pi : E \to M$ to $\pi' : E' \to M$ is a smooth map $F : E \to E'$ that **covers the identity on $M$** — meaning $\pi' \circ F = \pi$, so that $F$ sends the fibre $E_p$ to the fibre $E'_p$ — and whose restriction to each fibre $F|_{E_p} : E_p \to E'_p$ is a linear map of vector spaces. These are the [[Def - Bundle Homomorphism|bundle homomorphisms over the base]]. Composition is ordinary composition of smooth maps, and the identity morphism on $E$ is the identity map. [[Def - Isomorphism|Isomorphisms]] in this category are bijective bundle [[Def - Homomorphism|homomorphisms]] over $M$ whose inverse is also a bundle homomorphism; one calls $E$ and $E'$ **isomorphic over $M$** in that case.

This category has rich structure. It has direct sums (Whitney sums $E \oplus E'$, the fibrewise direct sum), tensor products $E \otimes E'$ (fibrewise tensor product, see [[Def - Tensor Product of Vector Spaces]]), duals $E^*$ (fibrewise dual, see [[Def - Dual Space]]), and exterior powers $\Lambda^k E$. The trivial bundle $M \times \mathbb{R}$ acts as the identity for the tensor product, and $M \times \mathbb{R}^0 = M$ is the zero object. There is a "rank" functor $\mathbf{Vect}_M \to \mathbb{Z}_{\geq 0}$, sending a bundle to its rank, and this is additive on direct sums and multiplicative on tensor products. Up to isomorphism, $\mathbf{Vect}_M$ on a one-point manifold is the category of finite-dimensional real vector spaces.

**Vector bundle as a functor.** The construction $p \mapsto E_p$ can itself be viewed functorially. Consider the *fundamental groupoid* of $M$ (or simply the topological space $M$ thought of as a discrete category with smoothness): the bundle is a smoothly varying assignment of vector spaces, and a more sophisticated way to phrase it is that a vector bundle is a *locally trivial sheaf of free $C^\infty$-[[Def - Module|modules]] of constant rank*, or equivalently a *finitely generated projective module over $C^\infty(M)$* (Serre–Swan). The functoriality is that morphisms $f : M \to N$ induce **pullback functors** $f^* : \mathbf{Vect}_N \to \mathbf{Vect}_M$ — given a bundle $E \to N$, the pullback $f^*E := \{(p, v) \in M \times E : f(p) = \pi(v)\}$ is a smooth vector bundle over $M$ of the same rank, with fibre $(f^*E)_p = E_{f(p)}$.

**Cocycle description.** Yet another categorical perspective: a vector bundle is a *cocycle* in the Čech sense. Given an open cover $\{U_\alpha\}$, a rank-$k$ vector bundle is the same data as a Čech $1$-cocycle in the sheaf of smooth $\mathrm{GL}(k, \mathbb{R})$-valued functions on $M$ — that is, a collection of smooth maps $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$ satisfying the cocycle condition $\tau_{\alpha\gamma} = \tau_{\alpha\beta} \tau_{\beta\gamma}$, modulo coboundaries (refinements of the cover and choices of trivialization). This is the formal home of the [[Thm - Vector Bundle Construction Lemma|vector-bundle construction lemma]]: it says that the data of a bundle *is* the data of a cocycle.

The categorical view explains many properties at once. The contravariance of pullback is the categorical contravariance of $\mathrm{Hom}(-, V)$; the existence of direct sums and tensor products is inherited from the corresponding constructions on vector spaces, applied fibrewise; the equivalence with projective modules (Serre–Swan) is the bridge from differential geometry to commutative algebra. And the structure-[[Def - Group|group]] perspective — that vector bundles are bundles with structure group $\mathrm{GL}(k, \mathbb{R})$ — opens the door to principal bundles, associated bundles, and gauge theory, where one replaces $\mathrm{GL}(k, \mathbb{R})$ by an arbitrary Lie group.

---

# Relate to Other Fields / Compression

A vector bundle is a **vector-space-valued sheaf on $M$ that is locally free of constant rank**. The sheaf-theoretic phrasing is exact: the assignment $U \mapsto \Gamma(E|_U)$, sending an open set to the sections of $E$ over it, is a sheaf of $C^\infty(M)$-modules, and the local-triviality condition is the statement that this sheaf is locally isomorphic to the sheaf $U \mapsto C^\infty(U)^k$. Differential geometry on manifolds is sheaf theory specialized to the locally-free-of-constant-rank case.

A vector bundle is also a **principal $\mathrm{GL}(k, \mathbb{R})$-bundle with an associated $\mathbb{R}^k$**: the principal bundle records the structure-group data (the choices of basis for each fibre, up to $\mathrm{GL}(k, \mathbb{R})$-action) and the associated bundle reconstructs $E$ via the standard action. The principal-bundle viewpoint is the right setting for connections and curvature; the vector-bundle viewpoint is more economical for sections and pointwise computations.

**True name:** the true name of a vector bundle is "**a smoothly parametrized family of vector spaces, all of the same dimension, with smooth gluing across charts**". The technical apparatus — total space, projection, local trivializations — is the bookkeeping needed to make "smoothly parametrized family" precise. When you encounter a vector bundle in the wild, the operational thing to ask is: "what is the fibre $E_p$, and how does it twist as $p$ moves?" The first question is multilinear algebra at a point; the second is the transition function cocycle.

A useful slogan: **smooth fields on a manifold are sections of a vector bundle, and the bundle is determined by the field's transformation rule**. A vector field is a section of $TM$; a 1-form is a section of $T^*M$; a $(p, q)$-tensor field is a section of the bundle $T^{p,q}M$ of $(p, q)$-tensors; an $\mathrm{SO}(3)$-spinor field is a section of an associated bundle of the spin frame bundle. Every "field" in physics corresponds to a bundle, and the choice of bundle is forced by how the field's components must transform under a change of frame.

---

# Examples / Corollaries

**Is an instance — the product (trivial) bundle.** For any smooth manifold $M$ and any $k$, the projection $\pi : M \times \mathbb{R}^k \to M$ onto the first factor, with the obvious vector-space structure on each fibre $\{p\} \times \mathbb{R}^k$, is a smooth rank-$k$ vector bundle, with the identity map as a global trivialization. Every smooth vector bundle is *locally* of this form, but in general not globally.

**Is an instance — the tangent bundle $TM$.** For a smooth $n$-manifold $M$, the tangent bundle $TM = \bigsqcup_p T_pM$ with its natural projection and the smooth structure constructed in [[Def - The Tangent Bundle]] is a smooth rank-$n$ vector bundle. The local trivializations come from coordinate charts $(U, \varphi)$: the map $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^n$ sending $v^i \partial/\partial x^i|_p$ to $(p, v^1, \dots, v^n)$ is a smooth local trivialization. The transition functions between two such charts are the Jacobians of the coordinate transition maps.

**Is an instance — the cotangent bundle $T^*M$.** Dually, $T^*M = \bigsqcup_p T_p^*M$ is a smooth rank-$n$ vector bundle with transition functions equal to the *inverse transposes* of the Jacobians of coordinate transitions on $M$ (see [[Def - Cotangent Space and Cotangent Bundle]]). The dual coframe $(dx^1, \dots, dx^n)$ in a coordinate chart provides a local frame, paralleling the coordinate frame $(\partial/\partial x^i)$ of $TM$.

**Is an instance — the Möbius bundle.** Define $E = \mathbb{R}^2 / \sim$ where $(x, y) \sim (x + n, (-1)^n y)$ for $n \in \mathbb{Z}$, with projection $\pi : E \to S^1 = \mathbb{R}/\mathbb{Z}$ inherited from projection on the first coordinate. The fibres are copies of $\mathbb{R}$, and on small open arcs in $S^1$ the bundle is trivial; but globally $E$ is **not** isomorphic to $S^1 \times \mathbb{R}$. The Möbius bundle is the simplest nontrivial real vector bundle; its non-triviality is detected by the fact that $E$ is non-orientable as a manifold while $S^1 \times \mathbb{R}$ is orientable. See [[Ex - The Möbius Bundle is Nontrivial]].

**Is an instance — the tautological line bundle on $\mathbb{RP}^n$.** Recall $\mathbb{RP}^n$ is the set of lines through the origin in $\mathbb{R}^{n+1}$. The **tautological line bundle** $\gamma_n$ has total space $\{(\ell, v) \in \mathbb{RP}^n \times \mathbb{R}^{n+1} : v \in \ell\}$, with projection $(\ell, v) \mapsto \ell$. The fibre over $\ell$ is the line $\ell$ itself, a copy of $\mathbb{R}$. The tautological bundle is nontrivial; for $n = 1$ it is the Möbius bundle.

**Is an instance — the trivial bundle $TS^1$ is trivial.** Despite the tangent bundle being nontrivial for most spheres, $TS^1$ is trivial: the nonvanishing vector field $\partial/\partial\theta$ (the angular velocity field) is a global frame, so $TS^1 \cong S^1 \times \mathbb{R}$. This is a low-dimensional accident; for $n \neq 1, 3, 7$, $TS^n$ is nontrivial (hairy ball theorem and its higher-dimensional generalizations).

**Is NOT an instance — a "family of vector spaces" without local triviality.** Take $M = \mathbb{R}$ and define $E = \{(x, v) : v \in \mathbb{R}^{n(x)}\}$ where $n(x) = 1$ for $x \leq 0$ and $n(x) = 2$ for $x > 0$. This is a family of vector spaces parametrized by $\mathbb{R}$, but the fibre dimension jumps at $x = 0$, so no local trivialization with a fixed model fibre exists near $x = 0$. This is not a vector bundle — it is a *family*, but the constant-rank condition is exactly what disqualifies it.

**Is NOT an instance — the "[[Def - Fibration|fibration]]" $S^3 \to S^2$ (Hopf).** The Hopf fibration $\pi : S^3 \to S^2$ has fibres diffeomorphic to $S^1$ — not to a vector space. It is a fibre bundle with fibre $S^1$, indeed a principal $U(1)$-bundle, but not a vector bundle. Vector bundles are a special case of fibre bundles, namely those with fibre a vector space and linear transition functions.

**Corollary — sections of a vector bundle always exist.** For any smooth vector bundle $E \to M$, the **zero section** $\sigma_0(p) = 0_p \in E_p$ is a smooth global section. So $\Gamma(E)$ is never empty, and in fact it is always at least a one-dimensional vector space over $\mathbb{R}$ (containing the zero section and its scalar multiples — wait, scalar multiples of zero are all zero, so just the zero section). The interesting question is whether *nonvanishing* sections exist; that question is bundle-specific and topologically rich.

**Corollary — the rank determines local but not global structure.** Two rank-$k$ vector bundles over $M$ are locally isomorphic (both are locally $U \times \mathbb{R}^k$), but they need not be globally isomorphic — the isomorphism class is determined by the cocycle of transition functions modulo refinements, and there can be multiple inequivalent cocycles. The number of isomorphism classes of rank-$k$ vector bundles over $M$ is an invariant of $M$.

**Calibration check.** Verify that the projection $\pi_1 : M \times \mathbb{R}^k \to M$ with the obvious fibre structure satisfies all axioms. Convince yourself that the linearity-on-fibres condition for $\Phi$ is needed to make the vector-space structure independent of trivialization, by writing down what happens if you allow a nonlinear $\Phi$ on the fibres. Verify, on the Möbius bundle, that two trivializations exist on overlapping arcs and that their transition function on the overlap is the map $\pm 1 \in \mathrm{GL}(1, \mathbb{R})$.

---

# Unlocked by This

> [!tip] Principal Bundle *(from Gauge Theory / Fibre Bundles)*
> Stripping a vector bundle of its fibre and keeping only the structure group $\mathrm{GL}(k, \mathbb{R})$ acting on itself by left multiplication gives a **principal $\mathrm{GL}(k, \mathbb{R})$-bundle** over $M$. The vector bundle can be recovered as the *associated bundle* $E = P \times_{\mathrm{GL}(k, \mathbb{R})} \mathbb{R}^k$, where the equivalence relation is $(p \cdot g, v) \sim (p, g \cdot v)$. Principal bundles for compact Lie groups — $\mathrm{U}(1)$ for electromagnetism, $\mathrm{SU}(2)$ for the weak force, $\mathrm{SU}(3)$ for the strong force — are the geometric setting of gauge theory, and Yang–Mills theory is the variational calculus of connections on such bundles.

> [!tip] Connection and Curvature *(from Riemannian Geometry and Gauge Theory)*
> Sections of $E$ can be added pointwise but not naturally differentiated — comparing $\sigma(p)$ with $\sigma(q)$ requires a way to transport between fibres. A **connection** $\nabla$ on $E$ is a choice of such transport; in formula, it is an $\mathbb{R}$-bilinear map $\nabla : \mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E)$ satisfying $\nabla_{fX} \sigma = f \nabla_X \sigma$ (tensoriality in $X$) and $\nabla_X (f\sigma) = (Xf)\sigma + f \nabla_X \sigma$ (the Leibniz rule). The **curvature** of $\nabla$ is the 2-form-valued endomorphism $F = \nabla \circ \nabla$, and it measures the failure of parallel transport to be path-independent. On the tangent bundle of a Riemannian manifold, the unique torsion-free metric-compatible connection is the **Levi-Civita connection**, and its curvature is the Riemann curvature tensor — the central object of Riemannian geometry.

> [!tip] Characteristic Classes *(from Algebraic Topology)*
> The obstructions to triviality of a vector bundle — to finding a global trivialization $E \cong M \times \mathbb{R}^k$ — assemble into **characteristic classes**, cohomology classes of $M$ functorially attached to the bundle. The Stiefel–Whitney classes $w_i(E) \in H^i(M; \mathbb{Z}/2)$ live in $\mathbb{Z}/2$-cohomology and detect orientability ($w_1 = 0 \iff$ orientable) and the existence of spin structures ($w_2 = 0$ unlocks spinor fields). The Chern classes $c_i(E) \in H^{2i}(M; \mathbb{Z})$ are the integer-valued analogues for complex bundles; for the canonical line bundle on $\mathbb{CP}^n$, $c_1$ generates $H^2(\mathbb{CP}^n; \mathbb{Z})$. The Euler class $e(E) \in H^n(M; \mathbb{Z})$ for an oriented rank-$n$ bundle counts zeros of a generic section, and for the tangent bundle of an oriented closed manifold $\int_M e(TM) = \chi(M)$ — the Euler characteristic. Characteristic classes are the bridge between bundle theory and algebraic topology, and they are what makes the question "is this bundle trivial?" admit topological answers.

> [!tip] Hamiltonian Mechanics *(from Symplectic Geometry)*
> When the base manifold is interpreted as configuration space $Q$ of a mechanical system, the cotangent bundle $T^*Q$ becomes the **phase space**, with canonical symplectic structure $\omega = dp_i \wedge dq^i$. The position-momentum picture of Hamiltonian mechanics — with Hamilton's equations $\dot q^i = \partial H / \partial p_i$, $\dot p_i = -\partial H / \partial q^i$, conservation laws from Noether's theorem, Liouville's theorem on phase-space volume — all live natively on the cotangent bundle. Symplectic geometry is the geometry of $(T^*Q, \omega)$ and its generalizations, and it is the framework in which classical mechanics is coordinate-free.
