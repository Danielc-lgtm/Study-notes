---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Coordinate Chart and Atlas"
  - "Def - Topological Manifold"
  - "Def - Homeomorphism"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $M$ is a topological $n$-manifold and $(U, \varphi)$, $(V, \psi)$ are two [[Def - Coordinate Chart and Atlas|coordinate charts]] on $M$ with $U \cap V \neq \emptyset$. We write $\widehat{U} = \varphi(U) \subseteq \mathbb{R}^n$ and $\widehat{V} = \psi(V) \subseteq \mathbb{R}^n$. The full notation registry is on [[Differential Geometry I — Smooth Manifolds and Atlases]].

A function between open subsets of $\mathbb{R}^n$ is **smooth** ($C^\infty$) if each component function has continuous partial derivatives of all orders. It is a **diffeomorphism** if it is bijective, smooth, and has smooth inverse. These are the standard definitions from multivariable analysis; for the diffeomorphism criterion via the Jacobian, see [[Thm - The Inverse Function Theorem]].

---

# Axiom Motivation

We have charts $(U, \varphi)$ and $(V, \psi)$ on $M$, and we want to do calculus. In chart $(U, \varphi)$, a function $f : M \to \mathbb{R}$ is described by its coordinate representation $\widehat{f}_\varphi = f \circ \varphi^{-1} : \widehat{U} \to \mathbb{R}$, and we can differentiate $\widehat{f}_\varphi$ using ordinary multivariable calculus. In chart $(V, \psi)$, the same function is described by $\widehat{f}_\psi = f \circ \psi^{-1} : \widehat{V} \to \mathbb{R}$, and we can differentiate $\widehat{f}_\psi$. On the overlap $U \cap V$, both representations refer to the same function $f$, so they had better be related — and the relation is

$$\widehat{f}_\psi = f \circ \psi^{-1} = (f \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1}) = \widehat{f}_\varphi \circ (\varphi \circ \psi^{-1}).$$

The composition $\varphi \circ \psi^{-1}$ on the right is a map between open subsets of $\mathbb{R}^n$ — it converts $\psi$-coordinates back to $\varphi$-coordinates by going through $M$. This is the *transition function*. Its role is to translate the $\psi$-coordinate representation of any object on $M$ into the $\varphi$-coordinate representation, and vice versa.

The crucial observation: whether $\widehat{f}_\psi$ inherits the smoothness of $\widehat{f}_\varphi$ depends entirely on whether the transition function $\varphi \circ \psi^{-1}$ is itself smooth. If it is, then the chain rule guarantees that $\widehat{f}_\psi = \widehat{f}_\varphi \circ (\varphi \circ \psi^{-1})$ inherits the smoothness of $\widehat{f}_\varphi$; if it is not, then a $C^\infty$ function in one chart can fail to be $C^\infty$ in another. The function $f(x) = x$ on $\mathbb{R}$ is smooth in the standard chart $\varphi(x) = x$, but its representation in the chart $\psi(x) = x^{1/3}$ is $\widehat{f}_\psi(y) = y^3$, which is smooth — actually, this is fine. The relevant example (Lee Example 1.23) goes the other way: take $\psi(x) = x^3$ as the chart, so $\psi^{-1}(y) = y^{1/3}$; the transition $\varphi \circ \psi^{-1} = y^{1/3}$ is *not* smooth at the origin. A function smooth in the $\varphi$-chart (e.g., $f(x) = x$) has $\psi$-representation $\widehat{f}_\psi(y) = \psi^{-1}(y) = y^{1/3}$, which is *not* smooth. So the two charts disagree on which functions are smooth — and the disagreement is the failure of smoothness of the transition function.

The transition function is therefore the diagnostic for whether two charts can coexist in a "calculus-compatible" atlas. The definition collects this:

- $\varphi \circ \psi^{-1}$ has domain $\psi(U \cap V)$ (the image of the overlap in the $\psi$-chart) and codomain $\varphi(U \cap V)$ (the image of the overlap in the $\varphi$-chart). Both are open subsets of $\mathbb{R}^n$ (since $\varphi$ and $\psi$ are [[Def - Homeomorphism|homeomorphisms]]).
- $\varphi \circ \psi^{-1}$ is automatically a *homeomorphism* — composition of [[Def - Homeomorphism|homeomorphisms]]. This much is free.
- $\varphi \circ \psi^{-1}$ is *smooth* if both it and its inverse $\psi \circ \varphi^{-1}$ are smooth in the ordinary calculus sense — equivalently, $\varphi \circ \psi^{-1}$ is a [[Def - Diffeomorphism|diffeomorphism]] between open subsets of $\mathbb{R}^n$.

The first two are part of the definition; the third — smoothness — is the *smooth compatibility* condition that promotes a bare atlas to a smooth atlas (see [[Def - Smooth Atlas and Smooth Structure]]).

The transition function is also (literally, by its definition) the *change-of-coordinates map*: if $p \in U \cap V$ has $\varphi$-coordinates $(x^1, \dots, x^n)$ and $\psi$-coordinates $(y^1, \dots, y^n)$, then $y^j = (\psi \circ \varphi^{-1})^j(x^1, \dots, x^n)$. The transition tells you how the $\psi$-coordinates depend on the $\varphi$-coordinates and vice versa. Many computations in differential geometry are computations of transition functions: between rectangular and polar coordinates, between local frames on a vector bundle, between Cartesian and spherical coordinates on $S^2$.

One subtle point: why do we require *both* $\varphi \circ \psi^{-1}$ *and* its inverse $\psi \circ \varphi^{-1}$ to be smooth, rather than just one? Because either one alone is *not* enough: a smooth function may fail to have a smooth inverse, even when the inverse exists as a homeomorphism. The standard example is again Lee 1.23: $\psi(x) = x^3$ from $\mathbb{R}$ to $\mathbb{R}$ is smooth, but its inverse $\psi^{-1}(y) = y^{1/3}$ is not smooth at $0$. If we required only the forward smoothness, a chart $(U, \varphi)$ and a chart $(U, \varphi^3)$ (componentwise cubing) would be "smoothly compatible" in only one direction, and the smooth-structure equivalence relation would break. Demanding the transition be a *diffeomorphism* makes the relation symmetric and is the right strength.

---

# The Definition

Let $M$ be a topological $n$-manifold, and let $(U, \varphi)$ and $(V, \psi)$ be [[Def - Coordinate Chart and Atlas|coordinate charts]] on $M$ with $U \cap V \neq \emptyset$.

**Transition function.** The **transition function** (or **transition map** or **change-of-coordinates map**) from $\varphi$ to $\psi$ is the map

$$\psi \circ \varphi^{-1} : \varphi(U \cap V) \to \psi(U \cap V),$$

a function between open subsets of $\mathbb{R}^n$. It is automatically a [[Def - Homeomorphism|homeomorphism]] (composition of homeomorphisms restricted to open subsets).

**Smooth compatibility.** Two charts $(U, \varphi)$ and $(V, \psi)$ are **smoothly compatible** (or **$C^\infty$-compatible**) if either:
- $U \cap V = \emptyset$ (trivial overlap; compatibility holds vacuously), or
- The transition function $\psi \circ \varphi^{-1}$ is a **diffeomorphism** — smooth with smooth inverse — between the open subsets $\varphi(U \cap V)$ and $\psi(U \cap V)$ of $\mathbb{R}^n$.

In Lee's Proposition 1.17 and its proof, smoothness of one direction is shown to imply smoothness of the inverse (because the inverse of $\psi \circ \varphi^{-1}$ is $\varphi \circ \psi^{-1}$, which is the same kind of expression with the roles of $\varphi$ and $\psi$ swapped); hence to verify smooth compatibility it suffices to check smoothness in one direction. *Practical test*: by Corollary C.36 of Lee, if $\psi \circ \varphi^{-1}$ is smooth and injective with nonsingular Jacobian at every point, then it is a diffeomorphism — so one can often verify smoothness by computing the Jacobian.

**Cocycle properties.** For three charts $(U_i, \varphi_i)$ ($i = 1, 2, 3$) with pairwise overlaps, the transition functions $\varphi_{ji} = \varphi_j \circ \varphi_i^{-1}$ satisfy:
- $\varphi_{ii} = \mathrm{id}$ on $\varphi_i(U_i)$;
- $\varphi_{ij} = \varphi_{ji}^{-1}$;
- $\varphi_{ki} = \varphi_{kj} \circ \varphi_{ji}$ on the triple overlap.
This is the **cocycle condition** for transition functions, and it is the structural data that defines fibre bundles and sheaves over $M$. (Cascini Remark 1.9.)

---

# Categorical / Structural Definition

A transition function is a *morphism in the local model* — a morphism between open subsets of $\mathbb{R}^n$ — that records the chart change. From the categorical point of view, an atlas on $M$ produces a *covering sieve* in the étale topology of $\mathbb{R}^n$: the charts $(U_\alpha, \varphi_\alpha)$ give morphisms $\widehat{U_\alpha} \to M$ (via $\varphi_\alpha^{-1}$, treating $M$ as the target), and the transition functions $\varphi_\beta \circ \varphi_\alpha^{-1}$ are the *coherence data* — they say how the two morphisms $\widehat{U_\alpha} \to M$ and $\widehat{U_\beta} \to M$ relate on the overlap.

Equivalently: a topological manifold *is* a topological space together with a maximal atlas of charts to $\mathbb{R}^n$, and the transition functions are the structural data of this atlas. The category $\mathbf{TopMan}$ of topological manifolds is then a subcategory of the category of *spaces locally modelled on open subsets of $\mathbb{R}^n$*, where the local model class is open inclusions and the compatibility is "homeomorphism". A smooth manifold sharpens this to: local model class = open subsets of $\mathbb{R}^n$, compatibility = diffeomorphism; the transition functions then take values in the *diffeomorphism pseudogroup* of $\mathbb{R}^n$.

This is the prototype of a **geometric structure** in the sense of Klein and Cartan: a manifold is given by a model, a *pseudogroup* of local automorphisms of the model, and an atlas of charts whose transition functions take values in the pseudogroup. The smooth structure on a manifold corresponds to the pseudogroup of local [[Def - Diffeomorphism|diffeomorphisms]] of $\mathbb{R}^n$; replacing this with the pseudogroup of local [[Def - Isometry|isometries]] of Euclidean space gives a Euclidean structure; with conformal local automorphisms, a conformal structure; with local affine maps, an affine structure; with local [[Def - Symplectomorphism (Canonical Transformation)|symplectomorphisms]], a symplectic structure (see [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]]).

---

# Relate to Other Fields / Compression

**True name:** A transition function is "the formula for translating between two coordinate systems on the same patch of manifold." It is the change-of-variables formula of multivariable calculus, made into a structural object.

In **physics**, transition functions are everywhere: from rectangular to polar/cylindrical/spherical coordinates in mechanics, from one observer's coordinates to another in special and general relativity (the Lorentz transformations, the diffeomorphism gauge of GR), from one local trivialization of a fibre bundle to another (the *gauge transformations* of Yang–Mills theory). The cocycle condition $\varphi_{ki} = \varphi_{kj} \circ \varphi_{ji}$ is the consistency requirement that makes "patching together local descriptions" globally well-defined — physically, that no observer's frame is privileged.

In **algebraic geometry**, transition functions become the *transition data* of a scheme: an affine scheme $\mathrm{Spec}\, A$ is the local model, and a general scheme is built by gluing affine schemes along transition isomorphisms. The cocycle condition is again the consistency requirement for the gluing.

In **complex geometry**, transition functions to $\mathbb{C}^n$ are required to be holomorphic — the model and the pseudogroup change, the structural picture is identical. The Riemann sphere $\mathbb{CP}^1 = S^2$ has two charts with transition function $w = 1/z$, which is holomorphic on $\mathbb{C} \setminus \{0\}$; this is the prototype complex manifold.

In **Riemannian geometry**, the transition functions of an isometric atlas — charts in which the metric is the standard Euclidean metric — are Euclidean isometries. The pseudogroup is reduced from "diffeomorphisms" to "isometries", and the resulting structure ("flat Riemannian manifold") is much more rigid.

The compression: every "geometric structure" on a manifold is determined by reducing the structure group of the transition functions from "diffeomorphism" to some subclass (isometry, orientation-preserving, holomorphic, symplectic, contact, complex-analytic). The smooth structure of this chapter is the maximally flexible case.

---

# Examples / Corollaries

**Is an instance: the stereographic transition on $S^n$.** With $\sigma$ stereographic projection from the north pole and $\widetilde{\sigma}$ from the south pole (see [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]), the transition function on the overlap $S^n \setminus \{N, S\}$ is
$$\widetilde{\sigma} \circ \sigma^{-1} : \mathbb{R}^n \setminus \{0\} \to \mathbb{R}^n \setminus \{0\}, \quad u \mapsto \frac{u}{|u|^2}.$$
This is the *inversion in the unit sphere* of $\mathbb{R}^n$, and it is smooth on $\mathbb{R}^n \setminus \{0\}$ (each component is a rational function with nonvanishing denominator). Hence the two stereographic charts are smoothly compatible.

**Is an instance: the projective space transition.** With charts $\varphi_i$ on $\mathbb{RP}^n$ as in [[Ex - Real Projective Space is a Smooth Manifold]], the transition between $\varphi_i$ and $\varphi_j$ (say $i < j$) is
$$\varphi_j \circ \varphi_i^{-1}(u^1, \dots, u^n) = \left(\frac{u^1}{u^j}, \dots, \frac{u^{j-1}}{u^j}, \frac{1}{u^j}, \frac{u^{j+1}}{u^j}, \dots, \frac{u^{i-1}}{u^j}, \frac{u^{i+1}}{u^j}, \dots, \frac{u^n}{u^j}\right),$$
where the inserted "$1/u^j$" is in the $i$-th position (replacing the original $u^i$ that has been "promoted" to $1$ in the $\varphi_i^{-1}$ step). This is a rational function of $u$ with denominator $u^j$, which is nonzero on the overlap (the overlap is precisely the locus where both $x^i \neq 0$ and $x^j \neq 0$, equivalently $u^j \neq 0$ in $\varphi_i$-coordinates). Hence smooth.

**Is an instance: the Cartesian-to-polar transition on $\mathbb{R}^2 \setminus \{0\}$.** The polar chart $\psi(r, \theta) = (r \cos\theta, r\sin\theta)$ on the open set $\{r > 0, -\pi < \theta < \pi\}$ is a chart on $\mathbb{R}^2 \setminus \{x \leq 0, y = 0\}$. The transition with the standard Cartesian chart on the same domain is
$$\psi^{-1}(x, y) = \left(\sqrt{x^2 + y^2}, \arctan(y/x)\right) \text{ (with appropriate branch of } \arctan\text{)},$$
which is smooth on its open domain (the Jacobian is $1/r \neq 0$). Hence polar coordinates are smoothly compatible with Cartesian on the appropriate domain.

**Is NOT an instance of smooth compatibility: the standard chart and the cube-root chart on $\mathbb{R}$.** Let $\varphi(x) = x$ and $\psi(x) = x^{1/3}$ (the cube root, well-defined for negative inputs as well). Both are homeomorphisms of $\mathbb{R}$ to $\mathbb{R}$, hence charts. The transition is
$$\psi \circ \varphi^{-1}(x) = x^{1/3},$$
which is *not* smooth at the origin (its derivative $\tfrac{1}{3} x^{-2/3}$ blows up). Hence $\varphi$ and $\psi$ are *not* smoothly compatible — they define different smooth structures on $\mathbb{R}$ (Lee Example 1.23).

**Is NOT an instance: the standard chart and the $|x|$-chart on $\mathbb{R}$.** The map $\psi(x) = |x|$ is not even a homeomorphism (not injective), so it is not a chart, and the notion of "transition function" does not apply.

**Corollary (smoothness in any chart from one chart, given smooth compatibility).** Suppose $\mathcal{A}$ is a smooth atlas containing the chart $(V_0, \psi_0)$, and $f : M \to \mathbb{R}$ has smooth coordinate representation $f \circ \psi_0^{-1}$ on $\psi_0(V_0)$. Then for every chart $(V, \psi) \in \mathcal{A}$, the coordinate representation $f \circ \psi^{-1}$ is smooth on $\psi(V \cap V_0)$. *Proof:* $f \circ \psi^{-1} = (f \circ \psi_0^{-1}) \circ (\psi_0 \circ \psi^{-1})$, and both factors are smooth (the second by smooth compatibility). This shows smoothness in one chart of a smooth atlas propagates to all charts — the foundational consistency property of a smooth manifold.

**Corollary (transition function inherits orientation reversal).** If we declare a chart $(U, \varphi)$ to be *positively oriented* and we compose with a diffeomorphism $h : \widehat{U} \to \widehat{U}$, the resulting chart $(U, h \circ \varphi)$ is positively oriented iff $\det Dh > 0$ everywhere. The transition function between two positively-oriented charts of an oriented atlas has positive Jacobian determinant everywhere — this is the working definition of an oriented atlas, used in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

**Calibration check.** Compute the transition function between the two stereographic charts of $S^1$ and verify it is $u \mapsto 1/u$ on $\mathbb{R} \setminus \{0\}$. Verify the cocycle property $\varphi_{31} = \varphi_{32} \circ \varphi_{21}$ for three of the projective-space charts $\varphi_1, \varphi_2, \varphi_3$ on $\mathbb{RP}^2$ on the triple overlap. Verify that the Jacobian of the stereographic transition $u \mapsto u/|u|^2$ on $\mathbb{R}^n \setminus \{0\}$ is $-1/|u|^{2n}$ — in particular, the transition reverses orientation, so the natural orientation of $S^n$ requires picking up a sign in one of the stereographic charts.

---

# Unlocked by This

> [!tip] Smooth Atlas and Smooth Structure *(from this chapter, §1.2)*
> The smooth-compatibility relation is the equivalence relation on atlases that defines a [[Def - Smooth Atlas and Smooth Structure|smooth structure]]. The construction of a smooth manifold from a single smooth atlas — via the [[Thm - Smooth Structure from Maximal Atlas|maximal atlas theorem]] — is the practical content of the chapter.

> [!tip] Coordinate Representations and Smooth Maps *(from [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]])*
> Once smooth compatibility is in place, a function $f : M \to \mathbb{R}^k$ or a map $F : M \to N$ is smooth precisely when its coordinate representations are smooth in *every* chart. The transition functions guarantee that smoothness in one chart propagates to all charts.

> [!tip] Fibre Bundles and Cocycle Data *(from [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|DG VI]] and Gauge Theory)*
> The cocycle condition $\varphi_{ki} = \varphi_{kj} \circ \varphi_{ji}$ is the defining datum of a **fibre bundle**: given an open cover of $M$ and transition functions $\{g_{\alpha\beta}\}$ taking values in a structure group $G$ and satisfying the cocycle condition, one constructs the principal $G$-bundle by gluing local trivializations. **Gauge theory** is the differential geometry of principal bundles, with the transition functions as the *gauge group elements*.

> [!tip] Sheaves *(from Algebraic Geometry and Differential Geometry)*
> A **sheaf** on $M$ is an assignment of an abelian group (or ring, module, space) $\mathcal{F}(U)$ to each open $U \subseteq M$, with restriction maps $\mathcal{F}(U) \to \mathcal{F}(V)$ for $V \subseteq U$ satisfying gluing axioms. The transition functions of an atlas are the prototype of sheaf-theoretic data: they describe how local information on overlapping patches assembles into global information. The sheaf of smooth functions $C^\infty_M$ on a smooth manifold encodes its entire smooth structure.

> [!tip] Pseudogroups and Geometric Structures *(from Geometric Structures in the Sense of Klein)*
> A general geometric structure on $M$ is determined by a *pseudogroup* of local diffeomorphisms of the model space $\mathbb{R}^n$ (orientation-preserving, isometric, holomorphic, symplectic, contact, complex-analytic) into which all transition functions of the atlas are required to take values. This is the **Cartan/Klein program**: classify geometric structures by classifying pseudogroups, equivalently classifying $G$-structures on the frame bundle.
