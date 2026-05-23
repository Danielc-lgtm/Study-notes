---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Topological Manifold"
  - "Def - Homeomorphism"
  - "Def - Continuous Map"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $M$ is a topological $n$-manifold (see [[Def - Topological Manifold]]), so $n \geq 0$ is fixed. A chart on $M$ is a pair $(U, \varphi)$ with $U \subseteq M$ open and $\varphi : U \to \widehat{U}$ a [[Def - Homeomorphism|homeomorphism]] onto an open subset $\widehat{U} = \varphi(U) \subseteq \mathbb{R}^n$. We write $x^i$ (with superscripts, following the [[Differential Geometry I — Smooth Manifolds and Atlases|chapter's convention]]) for the component functions of $\varphi$: $\varphi(p) = (x^1(p), \dots, x^n(p))$. An atlas is a collection $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$ of charts whose domains cover $M$. For the full registry, see [[Differential Geometry I — Smooth Manifolds and Atlases]].

This is a compound page: it defines two interlocking notions — **coordinate chart** and **atlas** — because they are introduced together and neither is fully usable without the other.

---

# Axiom Motivation

A topological manifold $M$ is defined by the existence of local homeomorphisms to $\mathbb{R}^n$ near every point. The next step is to give those local homeomorphisms a name, organize them into a structure, and use them as a tool for doing calculus. The pair $(U, \varphi)$ of a chart is the basic unit of this tool — it converts an opaque patch $U$ of the manifold into a concrete open subset of $\mathbb{R}^n$, where every computation of multivariable calculus is available. The atlas is the global organization: a family of charts whose domains cover $M$, so that every point lies in at least one chart.

Consider the alternatives. We could specify a single global homeomorphism $\varphi : M \to \widehat{M} \subseteq \mathbb{R}^n$ — but only the simplest manifolds (Euclidean spaces and their open subsets, graphs of functions) admit such a global chart. Already $S^1$ does not: a global chart would be a homeomorphism between the compact circle and an open subset of $\mathbb{R}$, which is impossible because the open subset is non-compact. So for most manifolds the local data of charts is essential, and the global manifold emerges only by gluing.

Consider the requirements on a single chart. *Open domain* $U \subseteq M$: open, because we want a "neighbourhood" — the chart should describe an entire region around each of its points, not just a single point. *Homeomorphism* $\varphi$: bijective continuous with continuous inverse, because we want to transport everything (continuity, convergence, open sets) freely between $U$ and $\widehat{U}$, and only a homeomorphism preserves these topological invariants in both directions. *Open image* $\widehat{U} \subseteq \mathbb{R}^n$: open, so that calculus in $\widehat{U}$ has wiggle room around every point — the standard calculus of $\mathbb{R}^n$ is set up on open subsets. Each of these requirements would be too weak if dropped: a non-open domain would not give a *neighbourhood*; a non-homeomorphism would not preserve the local topology; a non-open image would not support calculus.

Why call the components of $\varphi$ "coordinates"? Because they assign to each point $p \in U$ an $n$-tuple of real numbers $(x^1(p), \dots, x^n(p))$, just as Cartesian coordinates assign real-number tuples to points of the plane. The whole geometric content of a chart is that it makes the abstract point $p \in M$ accessible by *numbers*, and once numbers are available we can differentiate, integrate, and graph. The local coordinates engrave a "grid" on $U$, namely the preimages of the coordinate lines in $\mathbb{R}^n$.

Now to the atlas. A single chart almost never suffices (for the reasons above), so we collect charts: $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$, with $\bigcup_\alpha U_\alpha = M$. The covering condition is essential — every point must lie in some chart's domain — because we want chart-based methods to apply *everywhere* on $M$. The index set $I$ may be infinite, and is often required to be uncountable in the *maximal* atlas formulation of smooth structure (see [[Def - Smooth Atlas and Smooth Structure]]); a manifold may be covered by countably many charts (by second countability), but the maximal atlas — which includes every smoothly compatible chart — is enormous.

What is *not* required of an atlas at this level? Two things:

- The chart domains $U_\alpha$ need not be disjoint, and in fact they almost always overlap. The overlaps are where the work is done: in §1.2 we will demand that on overlaps the *transition function* $\varphi_\beta \circ \varphi_\alpha^{-1}$ be smooth, and this is what promotes a bare atlas (here) to a smooth atlas. At this level of definition, no smoothness is required.

- The charts need not be of the same "size" or "shape" — different charts can map onto open subsets of $\mathbb{R}^n$ of arbitrarily different shapes, and they need not be open balls or cubes. This flexibility is essential because for many spaces (especially quotient spaces), the most natural charts have irregular images.

The atlas concept is the universal one for "structure described by local data", and recurs in countless variations: complex manifolds (charts to $\mathbb{C}^n$), $C^k$-manifolds (transitions $C^k$), real-analytic manifolds (transitions real-analytic), Riemannian manifolds (charts plus a metric tensor at each point), spin manifolds (charts plus a spin structure), and so on. The pattern is to layer extra data onto the chart definition while keeping the same atlas structure underneath.

---

# The Definition

Let $M$ be a topological $n$-manifold.

**Coordinate chart.** A **coordinate chart** (or simply **chart**) on $M$ is a pair $(U, \varphi)$ consisting of:
- An **open subset** $U \subseteq M$, called the **coordinate domain** or **coordinate neighbourhood** of each of its points;
- A **homeomorphism** $\varphi : U \to \widehat{U}$, where $\widehat{U} = \varphi(U) \subseteq \mathbb{R}^n$ is an open subset of $\mathbb{R}^n$.

The map $\varphi$ is called the **coordinate map**. The component functions of $\varphi$, namely $x^i : U \to \mathbb{R}$ defined by $\varphi(p) = (x^1(p), \dots, x^n(p))$ — equivalently $x^i = \pi^i \circ \varphi$ where $\pi^i : \mathbb{R}^n \to \mathbb{R}$ is the $i$-th coordinate projection — are the **local coordinates** on $U$. We sometimes write the chart as $(U, x^1, \dots, x^n)$ or $(U, x^i)$ when we wish to emphasize the coordinate functions.

A chart $(U, \varphi)$ is said to be **centered at $p \in U$** if $\varphi(p) = 0$. From any chart $(U, \varphi)$ containing $p$ one obtains a chart centered at $p$ by replacing $\varphi$ with $\varphi - \varphi(p)$.

A chart is called a **coordinate ball** if $\widehat{U}$ is an open ball in $\mathbb{R}^n$, a **coordinate cube** if $\widehat{U}$ is an open cube. By Lee Lemma 1.10, every topological manifold has a countable basis of precompact coordinate balls.

**Atlas.** An **atlas** for $M$ is a collection $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$ of charts on $M$ whose domains cover $M$:
$$\bigcup_{\alpha \in I} U_\alpha = M.$$
The index set $I$ may be infinite; when $M$ is compact, $I$ may be taken finite; for general topological manifolds, $I$ may be taken countable (by second countability).

An atlas is just a covering family of charts; no compatibility between charts is required at this level. Compatibility is introduced in [[Def - Smooth Atlas and Smooth Structure]].

---

# Categorical / Structural Definition

A chart $(U, \varphi)$ on $M$ is, equivalently, an open immersion $\varphi : U \hookrightarrow \mathbb{R}^n$ in the category $\mathbf{Top}$ — that is, a homeomorphism onto an open subset of $\mathbb{R}^n$. From the point of view of sheaf theory, a chart is a *local trivialization* of $M$ — a piece of data identifying an open subset of $M$ with an open subset of the model $\mathbb{R}^n$, so that the structure sheaf of $M$ (in this case, the sheaf of continuous real-valued functions) restricts to the structure sheaf of the model. An atlas is then a *trivializing cover*: a family of local trivializations whose domains cover $M$.

This structural framing makes it clear how charts and atlases generalize:

- For a **smooth manifold**, replace "homeomorphism" with "diffeomorphism onto the open subset of $\mathbb{R}^n$" (in a sense made precise once a smooth structure is in place), and the structure sheaf is the sheaf of smooth functions.
- For a **complex manifold**, replace the model $\mathbb{R}^n$ with $\mathbb{C}^n$, and the structure sheaf is the sheaf of holomorphic functions.
- For a **vector bundle** of rank $k$ over $M$, replace the model with $U \times \mathbb{R}^k$ (or $U \times \mathbb{C}^k$), and the local trivialization is a fibre-preserving homeomorphism.
- For a **principal $G$-bundle**, replace the model with $U \times G$ for a Lie group $G$.

In all cases the categorical pattern is: a space is locally modelled on a chosen model, the local trivializations form an atlas, and the global structure is the (equivalence class of) atlases. This is the same pattern as scheme theory in algebraic geometry, $\infty$-topos theory in higher category theory, and physical model-building in mathematical physics.

---

# Relate to Other Fields / Compression

**True name:** A chart is "a local labelling of points of $M$ by real $n$-tuples, in a way that respects the topology." Whenever you want to do a calculation on $M$, you choose a chart, transport the calculation to $\widehat{U} \subseteq \mathbb{R}^n$, perform it using ordinary multivariable calculus, and transport the answer back. The whole subject of differential geometry can be read as "what kind of mathematical operations are independent of this choice of chart". An atlas is the global structure that makes "do everything in a chart, but the chart varies with the point" sensible.

In **classical mechanics**, a chart on the configuration space $Q$ of a system is a choice of *generalized coordinates*: angles for a pendulum, Cartesian coordinates for a free particle, Euler angles for a rigid body. The Lagrangian or Hamiltonian formalism is set up in generalized coordinates, but the equations of motion must be independent of the coordinate choice; the consistency requirement is exactly that the formalism transform correctly under chart transitions. The very concept of "phase space" $T^*Q$ as a manifold with canonical coordinates $(q, p)$ is a chart-based picture.

In **general relativity**, charts on spacetime are *coordinate systems*: $(t, x, y, z)$ in inertial frames, Schwarzschild coordinates $(t, r, \theta, \varphi)$ outside a black hole, comoving coordinates in cosmology, retarded null coordinates near a black-hole horizon. The Einstein equations are tensorial, hence chart-invariant; the same equation $R_{\mu\nu} - \tfrac{1}{2} g_{\mu\nu} R = 8 \pi T_{\mu\nu}$ takes different *expressions* in different charts but represents the same physical content. Choosing a chart is choosing a perspective; the geometry is in the chart-invariant content.

In **cartography**, every world map is, literally, a chart on $S^2$: a homeomorphism from an open subset of the sphere (whatever portion of the Earth the map covers) to an open subset of $\mathbb{R}^2$. Mercator, equirectangular, Lambert, polar stereographic — these are different charts, and the transitions between them are the transformations a navigator computes when switching reference maps. Stereographic projection in particular is the same map used in Lee Problem 1-7 to give $S^n$ its standard smooth structure. The reason every flat map distorts is that $S^2$ is not globally homeomorphic to any open subset of $\mathbb{R}^2$ — a single global chart does not exist.

---

# Examples / Corollaries

**Is an instance: $(\mathbb{R}^n, \mathrm{id})$.** The single chart consisting of all of $\mathbb{R}^n$ with the identity map is a chart, and the singleton $\{(\mathbb{R}^n, \mathrm{id})\}$ is an atlas. This is the **standard atlas** on $\mathbb{R}^n$, and the chart is a **global chart**. Open subsets of $\mathbb{R}^n$ admit similar global charts (their inclusion into $\mathbb{R}^n$).

**Is an instance: stereographic charts on $S^n$.** Let $N = (0, \dots, 0, 1)$ and $S = (0, \dots, 0, -1)$ be the north and south poles of $S^n \subseteq \mathbb{R}^{n+1}$. The stereographic projections
$$\sigma : S^n \setminus \{N\} \to \mathbb{R}^n, \quad \sigma(x) = \left(\frac{x^1}{1 - x^{n+1}}, \dots, \frac{x^n}{1 - x^{n+1}}\right),$$
$$\widetilde{\sigma} : S^n \setminus \{S\} \to \mathbb{R}^n, \quad \widetilde{\sigma}(x) = \left(\frac{x^1}{1 + x^{n+1}}, \dots, \frac{x^n}{1 + x^{n+1}}\right),$$
are homeomorphisms onto $\mathbb{R}^n$, so the pair $\{(S^n \setminus \{N\}, \sigma), (S^n \setminus \{S\}, \widetilde{\sigma})\}$ is a two-chart atlas on $S^n$. See [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]].

**Is an instance: graph coordinates on $S^n$.** For $i = 1, \dots, n+1$, let $U_i^\pm = \{x \in S^n : \pm x^i > 0\}$, and define $\varphi_i^\pm : U_i^\pm \to \mathbb{B}^n$ by $\varphi_i^\pm(x^1, \dots, x^{n+1}) = (x^1, \dots, \widehat{x^i}, \dots, x^{n+1})$ — drop the $i$-th coordinate. Each $\varphi_i^\pm$ is a homeomorphism onto the open unit ball $\mathbb{B}^n \subseteq \mathbb{R}^n$. The $2(n+1)$ charts cover $S^n$, so they form an atlas. This is Lee's Example 1.4. See [[Ex - Compatibility of Two Atlases on the Sphere]].

**Is an instance: affine charts on $\mathbb{RP}^n$.** For $i = 1, \dots, n+1$, let $U_i = \{[x^1 : \dots : x^{n+1}] : x^i \neq 0\}$ and
$$\varphi_i([x^1 : \dots : x^{n+1}]) = \left(\frac{x^1}{x^i}, \dots, \frac{\widehat{x^i}}{x^i}, \dots, \frac{x^{n+1}}{x^i}\right) \in \mathbb{R}^n.$$
Each $\varphi_i$ is a homeomorphism onto $\mathbb{R}^n$ (well-defined because the ratios are scale-invariant). The $n+1$ charts cover $\mathbb{RP}^n$. See [[Ex - Real Projective Space is a Smooth Manifold]].

**Is NOT an instance: the polar map $(r, \theta) \mapsto (r \cos\theta, r \sin\theta)$ on all of $\mathbb{R}^2$.** This *map* is smooth, but it is not a coordinate chart: it is not a homeomorphism onto its image. The preimage of any point $(x, y) = (r \cos\theta, r\sin\theta)$ with $r > 0$ includes both $(r, \theta)$ and $(r, \theta + 2\pi)$, so the map is not injective. To get a chart one must restrict to a subset on which the map *is* a homeomorphism: e.g., $r > 0, -\pi < \theta < \pi$, with image $\mathbb{R}^2 \setminus \{x \leq 0, y = 0\}$ — but this excludes the negative $x$-axis. To cover all of $\mathbb{R}^2 \setminus \{0\}$ with polar coordinates requires two charts (using complementary angular intervals), giving a polar atlas on the punctured plane.

**Is NOT an instance: a "chart" with non-open image.** The map $\varphi : (-1, 1) \to [0, 1)$, $\varphi(x) = |x|$, is continuous and surjective but not injective; even restricted to $(0, 1)$ where it is a homeomorphism onto $(0, 1)$, the issue is that $\varphi : (0, 1) \to (0, 1)$ would be a valid chart, but $\varphi : (-1, 1) \to [0, 1)$ is not, because the image $[0, 1)$ is not open in $\mathbb{R}$.

**Corollary (every topological manifold admits an atlas).** This is part of the definition of topological manifold: every point has a chart, and the union of any such collection of charts that covers $M$ is an atlas. By second countability, a countable atlas can always be extracted.

**Corollary (every chart has many sub-charts).** Given a chart $(U, \varphi)$ and any open $V \subseteq U$, the restriction $(V, \varphi|_V)$ is again a chart, with image $\varphi(V) \subseteq \widehat{U}$, automatically open. So every chart can be shrunk; this is the source of the flexibility behind the smooth manifold chart lemma (Lee 1.35).

**Calibration check.** Compute the chart-image $\sigma(S^1 \setminus \{N\})$ for stereographic projection from the north pole $N = (0, 1)$ of $S^1$: it should be all of $\mathbb{R}$ (verify: as $x$ approaches $N$, the projection goes to $\pm \infty$). Construct an atlas on the cylinder $S^1 \times \mathbb{R}$ with two charts. Verify that the open disk $\mathbb{B}^2 \subseteq \mathbb{R}^2$ admits an atlas with a single chart (the identity).

---

# Unlocked by This

> [!tip] Transition Function and Smooth Compatibility *(from this chapter, §1.2)*
> Once charts and atlases are in hand, the next step is to demand the charts cohere on overlaps — that is, that the [[Def - Transition Function|transition function]] $\varphi_\beta \circ \varphi_\alpha^{-1}$ between two charts be smooth. This promotes a topological atlas to a [[Def - Smooth Atlas and Smooth Structure|smooth atlas]], and is the gateway to calculus on manifolds.

> [!tip] Local Coordinate Expressions for Smooth Maps *(from [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]])*
> A function $f : M \to \mathbb{R}^k$ is *smooth* if its **coordinate representation** $\widehat{f} = f \circ \varphi^{-1} : \widehat{U} \to \mathbb{R}^k$ is smooth in the ordinary sense for some chart (equivalently, every chart) around each point. Charts are the bridge between the abstract notion of smoothness on $M$ and the concrete machinery of multivariable calculus.

> [!tip] Coordinate Vector Fields and Coordinate Frames *(from [[Differential Geometry III — Tangent Vectors and the Differential|DG III]])*
> Each chart $(U, \varphi)$ with local coordinates $x^1, \dots, x^n$ produces $n$ coordinate vector fields $\partial/\partial x^1, \dots, \partial/\partial x^n$ on $U$, which form a basis of every tangent space $T_pM$ at points $p \in U$. These are the coordinate-derivative operators of calculus, and they are the bridge from the abstract tangent space to concrete computations.
