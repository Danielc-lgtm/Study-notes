---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Topological Manifold"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Transition Function"
  - "Def - Smooth Atlas and Smooth Structure"
tags: [geometry, differential-geometry]
---

# Notation

A smooth manifold is a pair $(M, \mathcal{A})$ — a topological space $M$ together with a smooth structure $\mathcal{A}$. We write $\dim M = n$ for the dimension, and abbreviate $(M, \mathcal{A})$ to "$M$" once the smooth structure is fixed. Charts of the maximal atlas are **smooth charts**; coordinate maps are **smooth coordinate maps**; their component functions $x^1, \dots, x^n$ are **smooth local coordinates**. The standing convention is that $M$ is Hausdorff, second-countable, and finite-dimensional (see [[Def - Topological Manifold]]); "manifold" without qualification means "smooth manifold without boundary". For the full registry see [[Differential Geometry I — Smooth Manifolds and Atlases]].

---

# Axiom Motivation

The whole apparatus of [[Def - Topological Manifold|topological manifolds]], [[Def - Coordinate Chart and Atlas|charts and atlases]], [[Def - Transition Function|transition functions]], and [[Def - Smooth Atlas and Smooth Structure|smooth atlases and smooth structures]] has been built to make a single definition possible — "a space on which calculus is well-defined." That definition is here, and the structural motivation has already been laid out in the prior pages: the data needed is a topological manifold and a smooth structure. The remaining motivation is to explain *why* this is the right total package, and what alternative packagings exist.

Why a topological manifold *plus* a smooth structure, rather than some more compressed datum? Because the topological structure and the smooth structure are *independent*: a topological manifold may admit no smooth structure (Kervaire's 10-manifold), or it may admit multiple non-equivalent smooth structures (exotic $\mathbb{R}^4$'s, exotic spheres). The two pieces of data — "what space" (topological) and "what calculus" (smooth) — are genuinely distinct, and the definition reflects this by listing both.

Why insist on the maximal-atlas form of the smooth structure? Because we want to talk about *the* smooth charts of $M$ unambiguously. If "smooth structure" meant "equivalence class of smooth atlases", we would have to specify which representative atlas we use whenever we want to talk about smooth charts. The maximal-atlas form sidesteps this: a chart is smooth iff it is in the maximal atlas, full stop. [[Thm - Smooth Structure from Maximal Atlas]] guarantees the maximal atlas is uniquely determined by any representative atlas, so the choice of representative does not matter for any subsequent definition.

Why $C^\infty$ rather than $C^k$ for finite $k$, or real-analytic? The choice of $C^\infty$ is a convention with three motivations:

- It is the *limit* of all $C^k$: a $C^\infty$ atlas is a $C^k$ atlas for every finite $k$, so $C^\infty$ structure is the *intersection* of all $C^k$ structures, in a structural sense. Any theorem that requires "enough differentiability" can be proved in the $C^\infty$ category and is then automatically true in any sufficiently differentiable category.

- It is *more flexible than analytic*. A real-analytic ($C^\omega$) manifold has rigid transition functions (an analytic function determined by its values on any open set), and this rigidity is too restrictive for many constructions — in particular, partitions of unity cannot be analytic (compactly supported analytic functions are zero). A *smooth* (but not analytic) bump function is the foundational tool of [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]], and without it, basically nothing in modern differential geometry works.

- It is *coarse enough to permit many constructions*. The category of smooth manifolds has products, partitions of unity, embedding theorems (Whitney), Sard's theorem, transversality. The smaller categories (real-analytic, $C^k$) lose at least one of these properties.

A famous theorem of Whitney (1936) asserts that every $C^1$ manifold admits a unique compatible $C^\infty$ structure, and similarly for any $C^k$ with $k \geq 1$. So in dimensions where smooth structures exist at all (which is "most" dimensions; Kervaire's pathology is the exception), the $C^k$ and $C^\infty$ categories give the *same* manifolds up to diffeomorphism. This means choosing $C^\infty$ as the standard category loses no real generality, gains all the analytical advantages, and has the structural cleanness of being the limit of all finite-$k$ categories.

What about *exotic* smooth structures? A topological manifold may admit multiple non-diffeomorphic smooth structures. The 7-sphere $S^7$ has 28 distinct smooth structures (Milnor 1956; the topological/smooth diffeomorphism classification of $S^n$ is a major theorem); $\mathbb{R}^4$ admits uncountably many smooth structures (Donaldson, Freedman 1980s). These are deep phenomena and far beyond the scope of this chapter, but they show that the smooth structure is *not* a derived notion — it carries genuine content beyond the topology.

The categorical viewpoint sums it up: a smooth manifold is the prototype of *a space modelled locally on $\mathbb{R}^n$ in the differentiable category*. Replacing the model and the category produces the entire zoo of geometric structures.

---

# The Definition

A **smooth manifold of dimension $n$** is a pair $(M, \mathcal{A})$ where:

1. $M$ is a [[Def - Topological Manifold|topological manifold]] of dimension $n$ — that is, a Hausdorff, second-countable topological space such that every point has an open neighbourhood homeomorphic to an open subset of $\mathbb{R}^n$;

2. $\mathcal{A}$ is a [[Def - Smooth Atlas and Smooth Structure|smooth structure]] on $M$ — equivalently, a maximal smooth atlas, or an equivalence class of compatible smooth atlases.

When the smooth structure is understood, we write "$M$ is a smooth manifold" and call $\mathcal{A}$ the smooth structure of $M$. A chart of $\mathcal{A}$ is a **smooth chart** of $M$. The component functions of a smooth coordinate map are **smooth local coordinates** on the chart domain.

**Notational convention.** Following Lee, the term **manifold** without qualification will mean *smooth manifold without boundary* throughout this chapter and the rest of differential geometry. When boundary is allowed, we say [[Def - Smooth Manifold with Boundary|smooth manifold with boundary]]. When the topological-only structure is meant, we say *topological manifold*. When the smoothness class is something other than $C^\infty$, we say *$C^k$-manifold*, *real-analytic manifold*, *complex manifold* as appropriate.

**Equivalent specification.** By [[Thm - Smooth Structure from Maximal Atlas]] (Lee Proposition 1.17), a smooth structure on $M$ is determined by *any* smooth atlas on $M$. So in practice, to specify a smooth manifold, one specifies a topological manifold $M$ together with any smooth atlas $\mathcal{A}_0$, with the understanding that the smooth structure is the maximal atlas $\overline{\mathcal{A}_0}$ uniquely determined by $\mathcal{A}_0$.

---

# Categorical Definition

The category $\mathbf{Man}^\infty$ of smooth manifolds has:
- **Objects:** smooth manifolds $(M, \mathcal{A})$, varying in dimension;
- **Morphisms:** smooth maps $f : M \to N$ — continuous maps whose representation $\psi \circ f \circ \varphi^{-1}$ in any pair of smooth charts is a smooth function between open subsets of Euclidean spaces (see [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]]).

This is the central category of differential geometry. Compare:

- **$\mathbf{TopMan}$**: the category of topological manifolds, with continuous maps as morphisms. The forgetful functor $\mathbf{Man}^\infty \to \mathbf{TopMan}$ is *faithful* (a smooth map is determined by its continuous-function content) but not *full* (continuous maps need not be smooth) and not *essentially surjective* (some topological manifolds admit no smooth structure).

- **$\mathbf{Man}^{C^k}$**: $C^k$-manifolds for $k \geq 1$. The Whitney embedding theorem says every $C^k$-manifold admits a *unique compatible* $C^\infty$ structure, so the functor $\mathbf{Man}^\infty \to \mathbf{Man}^{C^k}$ that forgets the higher derivatives is essentially surjective on the connected components admitting smooth structures, and a categorical equivalence after passing to the appropriate quotient.

- **$\mathbf{Man}^{C^\omega}$**: real-analytic manifolds. Strictly more rigid than $\mathbf{Man}^\infty$; the forgetful functor is essentially neither full nor surjective (smooth manifolds may not admit any compatible real-analytic structure, and real-analytic maps are a strict subclass of smooth maps).

- **$\mathbf{ComplexMan}$**: complex manifolds. The forgetful functor "complex manifold → smooth manifold (of dimension $2n$ when complex dimension is $n$)" is faithful, not full, and not essentially surjective (most smooth even-dimensional manifolds have no compatible complex structure; existence is a delicate topological question).

The structural insight: $\mathbf{Man}^\infty$ sits at the "Goldilocks" point of geometric structures — strict enough to support calculus, flexible enough to support partitions of unity and gluing, well-behaved enough that finite-category theorems hold. The full chain
$$\mathbf{ComplexMan} \hookrightarrow \mathbf{Man}^{C^\omega} \hookrightarrow \mathbf{Man}^\infty \hookrightarrow \mathbf{Man}^{C^k} \hookrightarrow \mathbf{TopMan}$$
arranges the categories by rigidity; $\mathbf{Man}^\infty$ is the standard working category of differential geometry.

In sheaf-theoretic language, a smooth manifold is a *locally ringed space* $(M, C^\infty_M)$ such that $(M, C^\infty_M)$ is locally isomorphic, as a locally ringed space, to $(\widehat{U}, C^\infty_{\widehat{U}})$ for some open $\widehat{U} \subseteq \mathbb{R}^n$. The smooth structure is reconstructed from the structure sheaf $C^\infty_M$: a chart is the data of an open set $U$ and an isomorphism $(U, C^\infty_M|_U) \cong (\widehat{U}, C^\infty_{\widehat{U}})$. This is the *ringed-space* perspective, the gateway to scheme theory and sheaf cohomology in algebraic geometry.

---

# Relate to Other Fields / Compression

**True name:** A smooth manifold is "a topological manifold where you can take derivatives unambiguously." The technical definition (maximal smooth atlas) packages this content; the operational content is that smooth functions, smooth maps, tangent vectors, and all of calculus are well-defined on $M$ — and the chain rule guarantees that everything is independent of the choice of chart.

In **classical mechanics**, the *configuration space* of a mechanical system (the set of all positions) is a smooth manifold. For a pendulum: $S^1$. For a double pendulum: $T^2$. For a rigid body in $\mathbb{R}^3$: $\mathbb{R}^3 \times \mathrm{SO}(3)$. The Lagrangian formalism is set up on the tangent bundle $TM$; the Hamiltonian on $T^*M$ — both inherently manifold constructions.

In **general relativity**, *spacetime* is a smooth 4-manifold equipped with a Lorentzian metric. The smoothness of spacetime is a working assumption (not derived from any deeper principle) and is occasionally relaxed in low-regularity GR for matter sources with shocks. The smooth structure is what makes the Einstein equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$ a well-posed PDE system.

In **gauge theory** and the **Standard Model**, the fields are sections of vector bundles over a smooth manifold (spacetime), and the gauge transformations are smooth maps to a Lie group. The smooth manifold structure is the kinematic backdrop on which physics happens.

In **algebraic topology**, the smooth manifold is the simplest case of a *manifold-like space* on which one can study homology, cohomology, characteristic classes, and Morse theory. Many topological theorems (Lefschetz fixed-point theorem, Poincaré–Hopf, de Rham) are proved by exploiting the smooth structure even though the conclusions are topological.

In **mathematical physics and quantum field theory**, smooth manifolds are the substrate for *path integrals* (configuration spaces of fields), *gauge theories* (principal bundles over spacetime), *string theory* (worldsheet/world-volume manifolds), and *general relativity* (spacetime). Every formulation of quantum field theory beyond toy models assumes smooth manifold structure.

The unifying compression: a smooth manifold is the natural setting for any mathematical or physical theory in which *fields*, *derivatives*, and *local-to-global gluing* are involved.

---

# Examples / Corollaries

**Is an instance: $\mathbb{R}^n$ with the standard smooth structure.** Single chart $(\mathbb{R}^n, \mathrm{id})$ as the determining smooth atlas. Smooth functions on $\mathbb{R}^n$ in this structure are smooth in the ordinary multivariable-calculus sense.

**Is an instance: $S^n$ with the standard smooth structure.** The two-chart stereographic atlas (Lee Problem 1-7) or the $2(n+1)$-chart graph atlas (Lee Example 1.4) — they determine the same smooth structure ([[Ex - Compatibility of Two Atlases on the Sphere]]). The standard smooth structure on $S^n$.

**Is an instance: $\mathbb{RP}^n$ with the standard smooth structure.** The $(n+1)$-chart affine atlas (see [[Ex - Real Projective Space is a Smooth Manifold]]) determines a smooth structure on $\mathbb{RP}^n$.

**Is an instance: $\mathbb{CP}^n$ with its smooth structure.** Analogous to $\mathbb{RP}^n$ but with $(n+1)$ charts to $\mathbb{C}^n \cong \mathbb{R}^{2n}$; the transitions are holomorphic, in particular smooth. (Lee Problem 1-9.) This is the prototype complex manifold of complex dimension $n$ and real dimension $2n$.

**Is an instance: the $n$-torus $T^n = S^1 \times \cdots \times S^1$.** Product of $n$ copies of $S^1$, smooth by [[Thm - Product of Smooth Manifolds is a Smooth Manifold]]. Alternatively, the quotient $\mathbb{R}^n / \mathbb{Z}^n$ — the two constructions give the same smooth structure. See [[Ex - The Torus is a Smooth Manifold via Quotient]].

**Is an instance: $\mathrm{GL}(n, \mathbb{R})$.** As an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$ (defined by $\det \neq 0$), it inherits a smooth manifold structure of dimension $n^2$ by [[Thm - Open Subset of a Smooth Manifold]]. See [[Ex - The General Linear Group is a Smooth Manifold]].

**Is an instance: the Grassmannian $G_k(V)$.** The space of $k$-dimensional subspaces of an $n$-dimensional vector space $V$, with the smooth structure constructed via the smooth manifold chart lemma (Lee 1.35). Dimension $k(n-k)$. See [[Ex - The Grassmannian is a Smooth Manifold]].

**Is an instance: the Möbius band (without boundary).** A non-orientable smooth 2-manifold, constructed as the quotient of $\mathbb{R} \times (-1, 1)$ by the action $(x, y) \sim (x+1, -y)$. The smooth structure is induced by the quotient; the resulting manifold is a non-trivial smooth structure on the topological cylinder. (The Möbius *band with boundary*, $\mathbb{R} \times [-1, 1] / \sim$, is a smooth manifold with boundary, see [[Def - Smooth Manifold with Boundary]].)

**Is an instance: $\mathbb{R}$ with the non-standard chart $\psi(x) = x^3$.** The atlas $\{(\mathbb{R}, \psi)\}$ defines a smooth structure on $\mathbb{R}$ *different from the standard one* — not equivalent, since the transition $y \mapsto y^{1/3}$ is not smooth at $0$. However, this smooth manifold is *diffeomorphic* to standard $\mathbb{R}$ via the smooth map $x \mapsto x^3$ from standard $\mathbb{R}$ to non-standard $\mathbb{R}$; in fact, by Lee Problem 1-6, there are uncountably many distinct smooth structures on any positive-dimensional topological manifold, all diffeomorphic to each other. The "moduli space of smooth structures up to diffeomorphism" is much smaller than the "set of smooth structures."

**Is an instance: the Heisenberg group $H_3$.** The 3-dimensional Lie group of upper-triangular $3 \times 3$ matrices with $1$'s on the diagonal — an open subset of an affine subspace of $M(3, \mathbb{R})$, hence smooth.

**Is NOT an instance: the line with two origins.** Locally Euclidean and second-countable but *not Hausdorff* (Lee Problem 1-1). Not a topological manifold, hence not a smooth manifold.

**Is NOT an instance: an uncountable disjoint union of $\mathbb{R}$'s.** Locally Euclidean and Hausdorff but not second-countable (Lee Problem 1-2). Not a topological manifold, hence not a smooth manifold.

**Is NOT an instance: the closed unit interval $[0, 1]$.** Locally Euclidean except at the endpoints, where the locally Euclidean condition fails (the only neighbourhoods of $0$ are of the form $[0, \varepsilon)$, not homeomorphic to open subsets of $\mathbb{R}$). It *is* a smooth manifold with boundary (see [[Def - Smooth Manifold with Boundary]]).

**Is NOT an instance: a generic algebraic variety with singularities.** The variety $\{xy = 0\} \subseteq \mathbb{R}^2$ — the union of the two axes — fails to be locally Euclidean at the origin (a neighbourhood of the origin contains arbitrarily small open subsets of the two axes, which has no homeomorphism to an open subset of $\mathbb{R}$, nor to an open subset of $\mathbb{R}^2$). It is a smooth manifold *away from* the origin, but not at the origin.

**Corollary (every open subset is a smooth manifold).** By [[Thm - Open Subset of a Smooth Manifold]], any open $U \subseteq M$ inherits a smooth $n$-manifold structure from $M$. This is used constantly: matrix Lie groups, the upper half-space, complements of closed sets.

**Corollary (every finite product is a smooth manifold).** By [[Thm - Product of Smooth Manifolds is a Smooth Manifold]], the finite product $M_1 \times \cdots \times M_k$ inherits a smooth structure of dimension $\sum n_i$.

**Corollary (every level set with regular value is a smooth manifold).** By the regular value theorem (preview of [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]), if $\Phi : U \to \mathbb{R}^k$ is smooth on $U \subseteq \mathbb{R}^n$ open and $c$ is a regular value, then $\Phi^{-1}(c)$ is a smooth $(n-k)$-manifold. This is the source of most concrete examples: $S^n = \{|x|^2 = 1\}$, $\mathrm{SL}(n) = \{\det A = 1\}$, $O(n) = \{A^T A = I\}$.

**Corollary (existence of a global single chart implies $\mathbb{R}^n$).** A smooth manifold $M$ of dimension $n$ admits a single global chart iff $M$ is diffeomorphic to an open subset of $\mathbb{R}^n$.

**Calibration check.** Identify the dimension of the following smooth manifolds: $\mathbb{R}^n$ (answer: $n$), $S^n$ ($n$), $\mathbb{RP}^n$ ($n$), $\mathbb{CP}^n$ ($2n$), $T^n$ ($n$), $\mathrm{GL}(n, \mathbb{R})$ ($n^2$), $G_k(\mathbb{R}^n)$ ($k(n-k)$). Verify that the disjoint union $\mathbb{R} \sqcup \mathbb{R}^2$ is *not* a smooth manifold in the sense of this definition (it would have to have a fixed dimension; the dimensions differ). Verify that the smooth structure on $\mathbb{R}$ defined by the chart $\psi(x) = x^3$ is genuinely different from the standard one (the transition $x \mapsto x^{1/3}$ is not smooth at $0$) but is diffeomorphic to the standard structure via the map $x \mapsto x^3$.

---

# Unlocked by This

> [!tip] Smooth Maps and the Category of Smooth Manifolds *(from [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]])*
> Once smooth manifolds are defined, the natural morphisms between them are **smooth maps**: maps whose coordinate representations are smooth in the ordinary sense. The category $\mathbf{Man}^\infty$ is the central category of differential geometry. Diffeomorphisms — invertible smooth maps with smooth inverse — are the isomorphisms; the diffeomorphism class is the natural equivalence class of smooth manifolds.

> [!tip] Tangent Space and the Tangent Bundle *(from [[Differential Geometry III — Tangent Vectors and the Differential|DG III]])*
> At each point $p$ of a smooth manifold $M$, the **tangent space** $T_pM$ is a finite-dimensional vector space of the same dimension as $M$, encoding "directions of motion" at $p$. The disjoint union $TM = \bigsqcup_p T_pM$ assembles into a smooth manifold (the *tangent bundle*) of dimension $2 \dim M$. The smooth structure on $TM$ is built from the smooth structure on $M$.

> [!tip] Vector Fields, Differential Forms, and All of Calculus on Manifolds *(from [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]] onwards)*
> Vector fields ($X : M \to TM$), differential forms ($\omega \in \Omega^k(M)$), tensors, and all the calculus of multivariable analysis transfer to manifolds via the smooth structure. The exterior derivative, the Lie bracket, the wedge product, and integration of forms are all defined on smooth manifolds, and Stokes's theorem $\int_M d\omega = \int_{\partial M} \omega$ is the integration-by-parts formula on manifolds with boundary.

> [!tip] Riemannian Manifolds *(from Riemannian Geometry — [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|DG XII]])*
> Adding a smoothly-varying inner product on each tangent space — a **Riemannian metric** — to a smooth manifold gives a *Riemannian manifold* $(M, g)$. Length, angle, distance, geodesics, volume, and curvature are then defined. Every paracompact smooth manifold admits a Riemannian metric (by partition of unity).

> [!tip] Lie Groups *(from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]])*
> A **Lie group** is a smooth manifold equipped with smooth group operations (multiplication and inversion). The general linear group, the orthogonal group, the unitary group, the symplectic group are all Lie groups, and their representation theory is the algebraic backbone of physics. The whole rich theory of Lie groups depends on the underlying manifold being *smooth* (the multiplication map must be smooth, the exponential map must be smooth).

> [!tip] Complex Manifolds and Kähler Geometry *(from Complex Geometry)*
> Replacing $\mathbb{R}^n$ with $\mathbb{C}^n$ and "smooth" with "holomorphic" gives a **complex manifold**. Adding a compatible Riemannian metric satisfying a closedness condition gives a **Kähler manifold**, the framework of algebraic geometry, Hodge theory, and string theory.

> [!tip] Symplectic Manifolds *(from Symplectic Geometry)*
> A smooth manifold $M^{2n}$ equipped with a closed nondegenerate 2-form $\omega$ (a "symplectic form") is a **symplectic manifold**, the framework of Hamiltonian mechanics. The cotangent bundle $T^*M$ of any smooth manifold is naturally symplectic, providing the canonical phase space of classical mechanics.

> [!tip] Fibre Bundles and Gauge Theory *(from [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|DG VI]] and beyond)*
> A **fibre bundle** is a smooth manifold $E$ equipped with a smooth surjection $\pi : E \to M$ whose fibres are all diffeomorphic to a fixed model fibre $F$. **Vector bundles**, **principal $G$-bundles**, **frame bundles** are special cases. Gauge theories are the differential geometry of principal bundles, and the matter of Yang–Mills theory and the Standard Model.

> [!tip] General Relativity *(from Mathematical Physics)*
> **General relativity** is the differential geometry of a smooth 4-manifold equipped with a Lorentzian metric. The Einstein equations are PDEs for this metric, and singularity theorems (Hawking, Penrose) constrain the global geometry. Without the smooth-manifold framework, the language of GR cannot even be written down.
