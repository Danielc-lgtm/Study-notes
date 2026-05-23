---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Riemannian Manifold"
  - "Def - Diffeomorphism"
  - "Def - Pullback of a Covariant Tensor Field"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

Let $(M, g)$ and $(N, h)$ be Riemannian manifolds (or, more generally, (semi-)Riemannian). A smooth map $F : M \to N$ is denoted $F : (M, g) \to (N, h)$ when one wants to track the metrics. We write $\mathrm{Isom}(M, g)$ for the group of isometries from $(M, g)$ to itself. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Axiom Motivation

The desideratum is to identify the *natural notion of equivalence* of Riemannian manifolds. Two manifolds are equivalent as smooth manifolds if there is a [[Def - Diffeomorphism|diffeomorphism]] between them; the question is what additional structure to require for them to be equivalent as Riemannian manifolds. The answer is: the diffeomorphism must *preserve the metric*. This is the definition of an isometry.

**Why a diffeomorphism?** Equivalence of Riemannian manifolds is symmetric, so the map and its inverse should both be well-behaved. A smooth bijection with smooth inverse — a diffeomorphism — is exactly the smoothness category's notion of isomorphism. Anything weaker (e.g., a [[Def - Homeomorphism|homeomorphism]], or a smooth bijection without smooth inverse) loses the smooth structure that the metric depends on.

**Why "$F^*h = g$"?** This is the precise way to say "the metric of $M$ equals the pulled-back metric from $N$". Pointwise, at each $p \in M$:
$$
g_p(v, w) = (F^*h)_p(v, w) = h_{F(p)}(dF_p v, dF_p w).
$$
Geometrically: the differential $dF_p : T_pM \to T_{F(p)}N$ is a *linear isometry* between the two inner-product spaces $(T_pM, g_p)$ and $(T_{F(p)}N, h_{F(p)})$. So $F$ takes the inner-product structure of $M$ exactly to the inner-product structure of $N$, at every point.

**Why is this the right equivalence relation?** Because every geometric quantity built from the Riemannian metric is preserved by [[Def - Isometry|isometries]]: lengths of curves (Exercise 13.24 of Lee — see [[Def - Length of a Curve and Riemannian Distance]]), distances ($d_h(F(p), F(q)) = d_g(p, q)$), angles, gradients, Christoffel symbols, curvature tensors, [[Def - Geodesic|geodesics]], the Laplace–Beltrami operator's spectrum. Anything that is a *function of $g$ alone* (no extra data) is preserved by [[Def - Isometry|isometries]]. So two Riemannian manifolds related by an isometry are indistinguishable by intrinsic geometric measurements — they are "the same" in every way that matters for Riemannian geometry.

**Why "local isometry"?** A local isometry is a smooth map $F : M \to N$ such that *every point* $p \in M$ has a neighborhood $U$ on which $F|_U$ is an isometry onto its image. Equivalently, $F$ is a local diffeomorphism with $F^*h = g$. Local isometries do not need to be globally bijective — they can have multiple sheets or self-overlap. This weaker notion is useful because many natural maps (covering maps, Riemannian submersions) are local but not global isometries.

**Per-axiom failure analysis:**

(a) *Drop "diffeomorphism", keep "$F^*h = g$".* You get **local isometries**, **Riemannian immersions** (when $F$ is an immersion satisfying the pullback condition), and **Riemannian embeddings**. These are useful weaker notions, and the diffeomorphism case is the strongest one.

(b) *Drop "$F^*h = g$", keep diffeomorphism.* You get a smooth diffeomorphism that does *not* preserve the metric. Such maps abound and are the [[Def - Diffeomorphism|diffeomorphisms]] of the underlying smooth manifold; they preserve everything *except* the geometry. The round sphere and the ellipsoid are diffeomorphic but not isometric, and the failure of [[Def - Diffeomorphism|diffeomorphisms]] to be isometries is what makes Riemannian geometry richer than smooth-manifold theory.

(c) *Weaken to a $C^0$ map preserving distance.* For a connected Riemannian manifold one can define a distance-preserving continuous map $F : (M, d_g) \to (N, d_h)$, where $d_g$, $d_h$ are the Riemannian distances. The **Myers–Steenrod theorem** says that a distance-preserving bijection between Riemannian manifolds is automatically a smooth isometry. So in the connected case the metric-space and smooth-manifold notions of isometry coincide — a remarkable rigidity result. (For disconnected manifolds, one has to be more careful.)

---

# The Definition

> **Definition (Isometry of [[Def - Riemannian Manifold|Riemannian Manifolds]]).** Let $(M, g)$ and $(N, h)$ be Riemannian manifolds. A **(Riemannian) isometry** $F : (M, g) \to (N, h)$ is a [[Def - Diffeomorphism|diffeomorphism]] $F : M \to N$ such that $F^*h = g$, that is,
> $$
> h_{F(p)}\bigl(dF_p v,\ dF_p w\bigr) \;=\; g_p(v, w) \qquad \text{for every } p \in M,\ v, w \in T_pM.
> $$
> The two Riemannian manifolds $(M, g)$ and $(N, h)$ are **isometric** if such an isometry exists.

The isometries of $(M, g)$ to itself form a [[Def - Group|group]] $\mathrm{Isom}(M, g) \leq \mathrm{Diff}(M)$ under composition, called the **isometry [[Def - Group|group]]** of $(M, g)$.

**Definition (Local Isometry).** A smooth map $F : M \to N$ is a **local isometry** if every $p \in M$ has an open neighborhood $U$ such that $F|_U : U \to F(U)$ is a (Riemannian) isometry; equivalently, $F$ is a local diffeomorphism satisfying $F^*h = g$.

**Definition (Locally Isometric).** Two Riemannian manifolds $(M, g)$ and $(N, h)$ are **locally isometric** if every point of $M$ has a neighborhood isometric to an open subset of $N$, *and* vice versa. (Both directions are needed for symmetry.)

**Definition (Flat [[Def - Riemannian Manifold|Riemannian Manifold]]).** A Riemannian manifold $(M, g)$ is **flat** if it is locally isometric to Euclidean space $(\mathbb{R}^n, \bar g)$. Equivalently, every point has a neighborhood in which $g$ takes the constant Euclidean coordinate expression $\delta_{ij}\, dx^i \otimes dx^j$.

---

# Categorical / Structural Definition

The isometries form the **morphisms in the category of Riemannian manifolds** $\mathbf{Riem}$, when we take morphisms to be metric-preserving maps. The objects of $\mathbf{Riem}$ are Riemannian manifolds $(M, g)$, and the morphisms $(M, g) \to (N, h)$ are smooth maps $F$ satisfying $F^*h = g$ — that is, Riemannian immersions when $F$ is an immersion. Restricting morphisms to diffeomorphisms gives the category $\mathbf{Riem}_{\cong}$ in which morphisms are isometries; isomorphism in this category is precisely Riemannian isometric equivalence.

The isometry group $\mathrm{Isom}(M, g)$ is the automorphism group of the object $(M, g)$ in the category $\mathbf{Riem}_{\cong}$. By a theorem of **Myers and Steenrod**, $\mathrm{Isom}(M, g)$ is always a (finite-dimensional) [[Def - Lie Group|Lie group]] — a very nontrivial fact, because a priori the isometry group is defined only as a group of diffeomorphisms (an infinite-dimensional group), and the metric-preserving condition is what cuts it down to a finite-dimensional Lie [[Def - Subgroup|subgroup]]. The Lie algebra of $\mathrm{Isom}(M, g)$ is the space of **Killing vector fields** — vector fields whose flow consists of isometries — which is itself a Lie algebra of finite [[Def - Dimension|dimension]] at most $n(n+1)/2$ (attained for Euclidean space, spheres, and hyperbolic space).

Structurally, an isometry is *the diffeomorphism category's notion of "structure-preserving map" lifted to Riemannian manifolds*: it preserves the smooth structure (it is a diffeomorphism) *and* the metric structure (the pullback condition).

---

# Relate to Other Fields / Compression

This is the smooth-manifold version of "linear isometry" from linear algebra. In a single inner-product space $(V, \langle\cdot,\cdot\rangle)$, a [[Def - Linear Map|linear map]] $L : V \to V$ is an isometry iff $\langle Lv, Lw\rangle = \langle v, w\rangle$ for all $v, w$ — equivalently, the matrix of $L$ in an orthonormal basis is orthogonal. The Riemannian isometry generalises this from a single inner-product space to a smooth family: at every $p$, the differential $dF_p$ is a linear isometry $(T_pM, g_p) \to (T_{F(p)}N, h_{F(p)})$.

In group theory and physics, the isometry group of a (semi-)Riemannian manifold gives the *symmetry group* of the geometry. For $(\mathbb{R}^n, \bar g)$ it is the Euclidean group $E(n) = O(n) \ltimes \mathbb{R}^n$. For $(\mathbb{R}^4, \eta)$ Minkowski space, it is the Poincaré group, with the Lorentz subgroup $O(1, 3) = \mathrm{Isom}(\mathbb{R}^4, \eta)_{0}$ being the part fixing the origin. For the round sphere $(S^n, \mathring g)$ it is $O(n+1)$. For the hyperbolic plane $(\mathbb{H}^2, g_{\mathbb{H}})$ it is $\mathrm{PSL}(2, \mathbb{R})$. The isometry group encodes the geometry's symmetries.

**True name:** An isometry is *a smooth diffeomorphism whose differential is a linear isometry of inner-product spaces at every point*. The pullback condition $F^*h = g$ is the formal mechanism; the picture is "every tangent space gets sent isometrically to its image's tangent space".

---

# Examples / Corollaries

**Is an instance — translations of Euclidean space.** For any $a \in \mathbb{R}^n$, the translation $T_a : \mathbb{R}^n \to \mathbb{R}^n$, $T_a(x) = x + a$, is an isometry of $(\mathbb{R}^n, \bar g)$. Its differential is the identity, which preserves the Euclidean inner product. Together with the orthogonal transformations $O(n)$ (linear isometries), translations generate the full Euclidean group $E(n) = O(n) \ltimes \mathbb{R}^n = \mathrm{Isom}(\mathbb{R}^n, \bar g)$.

**Is an instance — rotations of the sphere.** Any element of $O(n+1) \subseteq GL(n+1, \mathbb{R})$ preserves the Euclidean inner product on $\mathbb{R}^{n+1}$, hence preserves the inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$ and the induced round metric on $S^n$. So $O(n+1)$ acts by isometries on $(S^n, \mathring g)$, and in fact $\mathrm{Isom}(S^n, \mathring g) = O(n+1)$ — every isometry of the round sphere is realised this way.

**Is an instance — Möbius transformations of the hyperbolic plane.** The orientation-preserving isometries of the upper half-plane $(\mathbb{H}^2, g_{\mathbb{H}})$ are the Möbius transformations $z \mapsto (az + b)/(cz + d)$ with $a, b, c, d \in \mathbb{R}$ and $ad - bc = 1$. This is the group $\mathrm{PSL}(2, \mathbb{R})$. Each such transformation preserves the upper half-plane and the metric $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$.

**Is an instance — left translations of a Lie group with a left-invariant metric.** If $G$ is a [[Def - Lie Group|Lie group]] equipped with a left-invariant Riemannian metric (constructed by translating any inner product on $\mathfrak{g} = T_e G$), then left translations $L_h : G \to G$, $L_h(g) = hg$, are isometries by construction. So $G$ acts on itself by isometries via left translation, embedding $G$ into $\mathrm{Isom}(G, g)$.

**Is NOT an instance — the differential of a generic diffeomorphism.** The diffeomorphism $\varphi : \mathbb{R}^n \to \mathbb{R}^n$, $\varphi(x) = 2x$ (scaling by 2) is a smooth diffeomorphism but *not* an isometry of $(\mathbb{R}^n, \bar g)$: $\varphi^* \bar g = 4\bar g \neq \bar g$. It is a **conformal** diffeomorphism (multiplies the metric by a constant) but not an isometry.

**Is NOT an instance — diffeomorphic but non-isometric manifolds.** The round sphere $(S^2, \mathring g)$ and the ellipsoid $\{(x/a)^2 + (y/b)^2 + (z/c)^2 = 1\}$ in $\mathbb{R}^3$ (with $a, b, c$ not all equal) are diffeomorphic as smooth manifolds but *not* isometric. The first has constant curvature, the second has varying curvature; an isometry would have to preserve curvature pointwise, which is impossible.

**Is NOT an instance — Minkowski space and Euclidean space.** $(\mathbb{R}^4, \eta)$ and $(\mathbb{R}^4, \bar g)$ are diffeomorphic (both have $\mathbb{R}^4$ as the smooth structure) but *not* isometric (the metrics have different signatures, $(1, 3)$ vs $(4, 0)$). Even in the broader semi-Riemannian sense, no map can be an isometry between manifolds of different signature.

**Corollary — isometries preserve distance.** If $F : (M, g) \to (N, h)$ is a Riemannian isometry between connected manifolds, then $d_h(F(p), F(q)) = d_g(p, q)$ for all $p, q \in M$. This justifies the name "isometry" — the metric (in the metric-space sense, [[Def - Length of a Curve and Riemannian Distance|Riemannian distance]]) is preserved.

**Corollary — isometries preserve all metric-derived quantities.** Lengths of curves, angles between tangent vectors, gradients (for the metric-dual), Christoffel symbols (in corresponding coordinates), the Riemann curvature tensor, [[Def - Geodesic|geodesics]] (isometries send geodesics to geodesics — see [[Ex - Isometries Send Geodesics to Geodesics]]), and the Laplace–Beltrami spectrum are all preserved.

**Corollary — the isometry group is a finite-dimensional Lie group.** By the **Myers–Steenrod theorem**, for any Riemannian manifold $(M, g)$, the isometry group $\mathrm{Isom}(M, g)$ is a (finite-dimensional) Lie group of [[Def - Dimension|dimension]] at most $n(n+1)/2$. The maximum is attained by the constant-curvature simply-connected manifolds: Euclidean space $\mathbb{R}^n$ (dim $E(n) = n + n(n-1)/2 = n(n+1)/2$), the sphere $S^n$ (dim $O(n+1) = n(n+1)/2$), hyperbolic space $\mathbb{H}^n$.

**Calibration check.** First, verify that the rotation $R_\theta : \mathbb{R}^2 \to \mathbb{R}^2$, $R_\theta(x, y) = (x\cos\theta - y\sin\theta, x\sin\theta + y\cos\theta)$, is an isometry of $(\mathbb{R}^2, \bar g)$. Second, show that the map $F : (\mathbb{R}^2, \bar g) \to (\mathbb{R}^2, \bar g)$, $F(x, y) = (2x, y/2)$, is *not* an isometry, even though it has determinant $1$ — it scales the $x$-direction and shrinks the $y$-direction, distorting the inner product. Third, identify all isometries of the flat torus $T^n = \mathbb{R}^n / \mathbb{Z}^n$ that fix the origin. Expected: $O(n) \cap GL(n, \mathbb{Z})$, the orthogonal transformations preserving the integer lattice (a finite group: for $n = 2$ it has order 8, the dihedral group of order 8).

---

# Unlocked by This

> [!tip] Symmetric Spaces *(from Riemannian Geometry and Representation Theory)*
> A Riemannian manifold $(M, g)$ is **symmetric** if every point has a geodesic involution (an isometry that fixes the point and reverses every geodesic through it). Such manifolds are highly symmetric — examples include all simply-connected constant-curvature spaces, the Grassmannians, the spaces $G/K$ for Lie groups with $G$ semisimple and $K$ maximal compact. The classification of simply connected Riemannian symmetric spaces is **Cartan's theorem**, which identifies them with pairs $(\mathfrak{g}, \mathfrak{k})$ from Lie theory. This is one of the deepest connections between Riemannian geometry, Lie theory, and representation theory.

> [!tip] The Myers–Steenrod Theorem *(from Riemannian Geometry)*
> The **Myers–Steenrod theorem** asserts that the isometry group of a Riemannian manifold is automatically a finite-dimensional Lie group, with the maximum dimension $n(n+1)/2$ attained exactly for constant-curvature simply connected manifolds. This is a deep rigidity result: a priori the isometry group is an infinite-dimensional group of diffeomorphisms, and metric-preservation is what cuts it down to a finite-dimensional Lie group. The Lie algebra is the space of **Killing vector fields** — vector fields generating one-parameter families of isometries — and is closed under the Lie bracket.

> [!tip] Spectral Geometry and "Hearing the Shape of a Drum" *(from Spectral Geometry)*
> The **spectrum** of the Laplace–Beltrami operator $\Delta_g$ on a compact Riemannian manifold is invariant under isometries — two isometric manifolds have the same spectrum. The converse — does the spectrum determine the manifold up to isometry? — is the question of whether one can "hear the shape of a drum". The answer is no in general (Sunada's method constructs pairs of isospectral non-isometric manifolds), but yes in many special cases (e.g., dimension-$2$ surfaces of small enough genus). This is the founding question of spectral geometry, and it is fundamentally about which geometric quantities are isometry invariants.

> [!tip] Killing Vector Fields and Conserved Quantities *(from Geometric Mechanics)*
> A **Killing vector field** on $(M, g)$ is a vector field whose flow consists of isometries; equivalently, its Lie derivative annihilates $g$: $\mathcal{L}_X g = 0$. Killing fields generate one-parameter subgroups of $\mathrm{Isom}(M, g)$ and, by **Noether's theorem** applied to geodesic motion, each Killing field provides a conserved quantity along every geodesic: the inner product $g(X, \dot\gamma)$ is constant. In general relativity, time-translation Killing fields give conserved energy, rotation Killing fields give conserved angular momentum, etc. — this is the geometric origin of conservation laws in physics.
