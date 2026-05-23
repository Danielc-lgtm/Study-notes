---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Smooth Map between Manifolds"
  - "Def - Linear Map"
  - "Def - Diffeomorphism"
tags: [geometry, differential-geometry, bundles]
---

# Notation

$\pi : E \to M$ and $\pi' : E' \to M'$ are smooth vector bundles. A bundle homomorphism is a smooth map $F : E \to E'$ covering a smooth map $f : M \to M'$. When $M = M'$ and $f = \mathrm{id}_M$, $F$ is a **bundle homomorphism over $M$**. The induced map on sections is denoted by the same symbol $F : \Gamma(E) \to \Gamma(E')$ when this causes no confusion.

---

# Axiom Motivation

A bundle homomorphism is the right notion of "map between vector bundles": a smooth map of total spaces that respects both the bundle structure (fibres go to fibres) and the linear structure (the restriction to each fibre is linear). The two conditions are forced by the requirement that the morphism be useful — that pulling structures along the morphism produce sensible objects.

The covering condition $\pi' \circ F = f \circ \pi$ says: $F$ takes the fibre $E_p$ over $p$ into the fibre $E'_{f(p)}$ over $f(p)$. Without this, $F$ would shuffle fibres in an unrestricted way, and the bundle structure would not transfer through $F$ — sections of $E$ would not map to sections of $E'$, and the categorical structure of $\mathbf{Vect}$ would collapse. The covering condition is the structural minimum for $F$ to be a morphism in any reasonable category of bundles.

The fibrewise-linearity condition says: $F|_{E_p} : E_p \to E'_{f(p)}$ is a linear map between vector spaces. Without this, the vector-space structure on fibres would not be preserved by $F$ — addition of vectors in $E_p$ would not commute with $F$. Linearity on fibres is the bundle counterpart of "$F$ respects the algebraic structure of the underlying object" in any category whose morphisms preserve algebraic structure.

What is forced by demanding $F$ is **smooth** as a map of manifolds, not just continuous? Smoothness of $F$ propagates: smooth sections of $E$ map to smooth sections of $E'$ via $\sigma \mapsto F \circ \sigma \circ f^{-1}$ (when $f$ is invertible — see below for the general case). Without smoothness, the bundle morphism would be only continuous-bundle theory.

What is forced by allowing $F$ to **cover any smooth map $f$**, rather than only the identity or only diffeomorphisms? Allowing general $f$ makes bundle homomorphisms reflect the natural maps that arise in geometry. The most important example is the **differential of a smooth map**: if $\phi : M \to N$ is smooth, then $d\phi : TM \to TN$ is a bundle homomorphism covering $\phi$. If we restricted to identity-covering maps, we would exclude $d\phi$ from the category and lose the basic functorial example.

What is forced by demanding the *restriction to each fibre* is linear, rather than $F$ as a map of total spaces being linear? Total-space linearity doesn't make sense — the total space $E$ is a manifold, not a vector space — so the only "linear" condition that has content is the fibrewise one. This is the same situation as in the definition of a vector bundle: the linear structure is fibrewise, not total-space.

What if we **strengthened** to demand the linear maps on fibres are isomorphisms? Then $F$ would be a **bundle isomorphism** (when also a diffeomorphism with inverse a bundle homomorphism). Such $F$ form a subclass of bundle homomorphisms — the invertible ones — and are exactly the isomorphisms in the category of bundles. Demanding fibrewise isomorphism in the definition of a bundle homomorphism would exclude noninjective and nonsurjective examples, including the zero map and the projection onto a subbundle.

What if we **weakened** to drop the covering condition? Then $F$ would be an arbitrary smooth map $E \to E'$, with no requirement to fibre-preserve. This includes far more maps than is useful — for instance, every diffeomorphism of $E$ to itself (regardless of how it permutes fibres) would qualify. Restricting to fibre-preserving maps is what makes the morphisms reflect the bundle structure.

What if we **weakened** to drop the linearity-on-fibres condition? Then $F$ would be a fibre-preserving smooth map between total spaces, without linear structure preserved. These are **fibre-bundle morphisms**, useful for general fibre bundles where the fibre is just a manifold (no vector-space structure). For vector bundles, dropping linearity loses the algebra: $F$ would not send sums of sections to sums, and the algebraic structure on $\Gamma(E)$ would not transfer.

---

# The Definition

Let $\pi : E \to M$ and $\pi' : E' \to M'$ be smooth vector bundles. A **(smooth) bundle homomorphism** from $E$ to $E'$ is a smooth map $F : E \to E'$ together with a smooth map $f : M \to M'$ such that:

1. **Covering:** the diagram commutes,
$$\pi' \circ F = f \circ \pi.$$
   Equivalently, $F$ maps the fibre $E_p$ over $p \in M$ into the fibre $E'_{f(p)}$ over $f(p) \in M'$. The map $f$ is called the **base map** that $F$ **covers**.

2. **Fibrewise linearity:** for every $p \in M$, the restriction
$$F|_{E_p} : E_p \to E'_{f(p)}$$
   is a linear map of vector spaces.

The base map $f$ is uniquely determined by $F$ (when $F$ is nonzero on all fibres), since $f(p) = \pi'(F(v))$ for any $v \in E_p$.

A **bundle homomorphism over $M$** is the special case $M = M'$ and $f = \mathrm{id}_M$: a smooth map $F : E \to E'$ with $\pi' \circ F = \pi$, linear on each fibre $E_p \to E'_p$. Bundle homomorphisms over $M$ are the morphisms of the category $\mathbf{Vect}_M$ of vector bundles over $M$.

A **bundle isomorphism** is a bundle homomorphism that is a diffeomorphism of total spaces whose inverse is also a bundle homomorphism. Equivalently (by a standard result), it is a bijective smooth bundle homomorphism whose restrictions to fibres are all linear isomorphisms.

**Induced map on sections.** A bundle homomorphism $F : E \to E'$ over $M$ induces a $C^\infty(M)$-module homomorphism $\Gamma(E) \to \Gamma(E')$, written by the same symbol $F$, defined by
$$F(\sigma)(p) := F(\sigma(p)) \in E'_p.$$
A standard result (the **bundle homomorphism characterization lemma**) says: a map $\Gamma(E) \to \Gamma(E')$ that is $C^\infty(M)$-linear and sends smooth sections to smooth sections arises from a unique bundle homomorphism over $M$. This is a *tensoriality criterion*: bundle homomorphisms are exactly the $C^\infty(M)$-linear maps on sections.

---

# Relate to Other Fields / Compression

A bundle homomorphism is the **vector-bundle morphism**: it is exactly the type of map that gives the category $\mathbf{Vect}_M$ (or its variant $\mathbf{Vect}$ with varying base) its structure. The two conditions — covering, fibrewise-linear — together say that $F$ is a "$\mathbb{R}^k$-linear morphism varying smoothly with $p$".

A bundle homomorphism is the **bundle analogue of a linear map** between vector spaces. Just as linear maps $V \to W$ are the morphisms of the category of vector spaces, bundle homomorphisms $E \to E'$ are the morphisms in the bundle category. The matrix-of-a-linear-map representation in linear algebra has a bundle counterpart: in chosen local frames for $E$ and $E'$, a bundle homomorphism is represented by a smooth matrix-valued function on the overlap of trivializing opens.

The **bundle homomorphism characterization lemma** (linear over $C^\infty(M)$ ⟺ comes from a bundle homomorphism) is the structural keystone: it says the algebra of sections detects the geometry of bundles. The categorical content: the functor $\Gamma : \mathbf{Vect}_M \to \mathbf{Mod}_{C^\infty(M)}$ (sending a bundle to its module of sections) is fully faithful — bundle homomorphisms are exactly the $C^\infty(M)$-module homomorphisms between section spaces.

**True name:** the true name of a bundle homomorphism is "**a smoothly varying linear map between fibres**". The covering map records "which fibre to which fibre"; the fibrewise-linearity records "as a linear map". When you write a bundle homomorphism in local frames, the data is a smooth matrix-valued function, and that is exactly what the categorical content says.

A useful slogan: **bundle homomorphisms are $C^\infty(M)$-linear; differential operators (like the exterior derivative or the Lie derivative) are not**. The Lie derivative $\mathcal{L}_X$ acts on vector fields but is not a bundle homomorphism, because $\mathcal{L}_X(fY) = (Xf)Y + f \mathcal{L}_X Y \neq f \mathcal{L}_X Y$ in general — the Leibniz rule violates $C^\infty(M)$-linearity. This is the **tensoriality criterion**: the operations that are pointwise are bundle homomorphisms; the operations that differentiate are not.

---

# Examples / Corollaries

**Is an instance — the differential $dF : TM \to TN$.** For a smooth map $F : M \to N$, the differential $dF$ (see [[Def - The Differential of a Smooth Map]]) is a smooth bundle homomorphism covering $F$. Fibrewise, $dF_p : T_pM \to T_{F(p)}N$ is a linear map. This is the prototypical example and is the reason "differential" is functorial.

**Is an instance — scalar multiplication by a smooth function.** Given $f \in C^\infty(M)$ and a vector bundle $E$, the map $F : E \to E$, $F(v) = f(\pi(v)) v$, is a smooth bundle homomorphism over $M$. Fibrewise, it acts on $E_p$ as multiplication by the scalar $f(p) \in \mathbb{R}$. The corresponding map on sections is $\sigma \mapsto f \sigma$.

**Is an instance — the zero bundle homomorphism.** The map $F : E \to E'$, $F(v) = 0_{f(\pi(v))}$ (the zero vector in $E'_{f(p)}$), is a bundle homomorphism for any base map $f$. Fibrewise it is the zero linear map.

**Is an instance — the identity on a bundle.** $\mathrm{id}_E : E \to E$ is a bundle homomorphism over $M$ with base map $\mathrm{id}_M$. Fibrewise it is the identity linear map.

**Is an instance — the dual map of a bundle homomorphism.** Given a bundle homomorphism $F : E \to E'$ over $M$, there is a dual bundle homomorphism $F^* : (E')^* \to E^*$ over $M$, defined fibrewise by $F^*_p = (F_p)^* : (E'_p)^* \to E_p^*$, the dual of $F_p$ in the sense of [[Def - Dual Map]]. The direction is reversed — this is the contravariance of duality.

**Is an instance — inclusion of a subbundle.** If $D \subseteq E$ is a [[Def - Subbundle|subbundle]], the inclusion $\iota : D \hookrightarrow E$ is a smooth bundle homomorphism over $M$, with each $\iota_p : D_p \to E_p$ the inclusion of a linear subspace.

**Is NOT a bundle homomorphism — the Lie derivative.** The Lie derivative $\mathcal{L}_X : \mathfrak{X}(M) \to \mathfrak{X}(M)$, $\mathcal{L}_X Y = [X, Y]$, is an $\mathbb{R}$-linear map on sections, but it is *not* $C^\infty(M)$-linear: $\mathcal{L}_X (fY) = (Xf) Y + f \mathcal{L}_X Y$, which is not $f \mathcal{L}_X Y$ unless $Xf = 0$ everywhere. By the bundle homomorphism characterization lemma, $\mathcal{L}_X$ does not come from a bundle homomorphism. It is a differential operator, not a tensor.

**Is NOT a bundle homomorphism — the exterior derivative.** The exterior derivative $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is $\mathbb{R}$-linear but not $C^\infty(M)$-linear: $d(f \omega) = df \wedge \omega + f \, d\omega$. The Leibniz rule shows $d$ involves differentiation, not pointwise linear algebra.

**Is NOT a bundle homomorphism — a smooth map of total spaces that doesn't cover any base map.** Define $F : T\mathbb{R}^2 \to T\mathbb{R}$, $F(x, y, v, w) = (x + y, v + w)$. This is a smooth map of manifolds, but $\pi'(F(x, y, v, w)) = x + y$, which depends on the second base coordinate $y$ even though the source point is $(x, y)$ — so $F$ does not have a well-defined "base map" of the form $f(x, y) = $ something. Actually, $f(x, y) = x + y$ *is* a well-defined base map here, and the projection condition is satisfied. So this *is* a bundle homomorphism after all. (Genuine non-examples of the covering condition are harder to construct because the projection condition is automatically forced once $F$ takes fibres to fibres.)

**Corollary — bundle homomorphisms over $M$ form a $C^\infty(M)$-module.** The set $\mathrm{Hom}_M(E, E')$ of bundle homomorphisms over $M$ is itself a $C^\infty(M)$-module under pointwise operations. Sum, scalar-function multiplication, and the zero homomorphism are all bundle homomorphisms.

**Corollary — composition of bundle homomorphisms is a bundle homomorphism.** Given $F : E \to E'$ covering $f : M \to M'$ and $F' : E' \to E''$ covering $f' : M' \to M''$, the composition $F' \circ F : E \to E''$ covers $f' \circ f : M \to M''$ and is fibrewise linear. So bundle homomorphisms form a category.

**Calibration check.** Verify that $dF : TM \to TN$ for a smooth $F : M \to N$ satisfies $\pi_N \circ dF = F \circ \pi_M$ (covering condition) and that each $dF_p$ is linear (fibrewise linearity). Verify the tensoriality criterion: scalar multiplication by $f \in C^\infty(M)$ is $C^\infty(M)$-linear on sections, while the Lie derivative is not. Convince yourself that bundle isomorphisms over $M$ are exactly the bijective fibrewise-isomorphism bundle homomorphisms.

---

# Unlocked by This

> [!tip] Pullback of a Bundle *(from Differential Geometry)*
> Given a bundle homomorphism $F : E \to E'$ covering $f : M \to M'$, the bundle $E$ is identified with the **pullback bundle** $f^*E'$ when $F$ is fibrewise an isomorphism — that is, $E$ is the bundle over $M$ whose fibre at $p$ is $E'_{f(p)}$. Pullback bundles are essential to gauge theory and to differential geometry of fibrations.

> [!tip] Connection-Preserving Bundle Map *(from Riemannian Geometry)*
> A bundle homomorphism $F : E \to E'$ between bundles equipped with connections $\nabla, \nabla'$ is **connection-preserving** if $F \circ \nabla = \nabla' \circ F$ at the level of sections. Such maps are the morphisms of the category of bundles-with-connection, and isometries of Riemannian manifolds (or, more generally, of frame bundles preserving the Levi-Civita connection) are the prototypical examples.

> [!tip] Sheaf of Homomorphisms *(from Algebraic Geometry)*
> The sheaf $\mathcal{Hom}(E, E')$ of local bundle homomorphisms is itself a sheaf of $C^\infty(M)$-modules, and its sections are exactly $\Gamma(\mathrm{Hom}(E, E'))$. As a sheaf, it satisfies an internal-hom adjunction: $\mathrm{Hom}(E_1 \otimes E_2, E') \cong \mathrm{Hom}(E_1, \mathrm{Hom}(E_2, E'))$. This is the categorical statement that bundles have a closed monoidal structure over their base, with $\otimes$ and $\mathcal{Hom}$ as the tensor and internal-hom functors.
