---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lorentzian Manifold"
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Classification of Four-Vectors"
tags: [geometry, differential-geometry, lorentzian-geometry]
---

# Notation

Let $(M, g)$ be a Lorentzian manifold (signature $(1, n-1)$ in Lee's "mostly minus" convention; see [[Def - Lorentzian Manifold]]). For a tangent vector $v \in T_pM$ we use the term **norm-squared** for the quantity $g_p(v, v)$, even though it can be negative or zero — the term is conventional, not literal. We say $v$ is:
- **timelike** if $g_p(v, v) > 0$,
- **spacelike** if $g_p(v, v) < 0$ (or $v = 0$, depending on convention; the conventions disagree on the zero vector),
- **null** or **lightlike** if $g_p(v, v) = 0$ and $v \neq 0$.

(In the "mostly plus" convention, timelike means $g(v, v) < 0$ — the signs flip with the convention.) The collective term for non-spacelike vectors (timelike or null) is **causal**. The set of null vectors at $p$ forms the **light cone** at $p$, a quadric cone in $T_pM$. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

This is a compound page: it defines three interlocking notions — timelike, spacelike, null — because they are introduced together and exhaust the classification of nonzero tangent vectors on a Lorentzian manifold.

---

# Axiom Motivation

The desideratum is to install on every tangent space of a [[Def - Lorentzian Manifold|Lorentzian manifold]] the causal classification of [[Def - Classification of Four-Vectors|four-vectors]] that is the bedrock of special relativity: every nonzero vector falls into one of three classes — *timelike* (positive norm-squared), *spacelike* (negative norm-squared), or *null* (zero norm-squared but nonzero vector). This trichotomy is invariant under Lorentz transformations of the tangent space and encodes the local causal structure: timelike directions are "time-like" in the sense that worldlines along them are achievable by massive particles, spacelike directions are "space-like" in the sense that no signal can travel along them, and null directions are "light-like" in the sense that only light travels along them.

The classification is **forced** by the indefiniteness of the Lorentzian inner product. In a positive-definite (Riemannian) inner product, $g(v, v) > 0$ for every nonzero $v$ — only one sign is possible, and there is no classification. In an indefinite inner product, the sign of $g(v, v)$ depends on $v$, and the three cases (positive, negative, zero) are all genuinely populated by nonzero vectors. The classification is then *into the orbits of the Lorentz [[Def - Group|group]] $O(1, n-1)$ acting on $T_pM$*: the Lorentz [[Def - Group|group]] is the orthogonal group of the indefinite form, and its orbits on $T_pM \setminus \{0\}$ are exactly the timelike vectors (split into future-directed and past-directed in the time-oriented case), the spacelike vectors, and the null vectors (also split into future and past in the time-oriented case).

**Why is the trichotomy invariant under Lorentz transformations?** Because the sign of $g(v, v)$ is preserved by any isometry: if $L$ is a Lorentz transformation (an isometry of $T_pM$), then $g(Lv, Lv) = g(v, v)$, so the sign is the same. This is what makes the classification *intrinsic* to the geometry, not dependent on a choice of frame. Two observers in different inertial frames will agree on whether a given tangent vector is timelike, spacelike, or null, even though they will measure its components differently.

**Why is the boundary case (null) physically important?** The null vectors are the directions along which light propagates. The light cone at a point $p$ is the set of tangent vectors $v$ with $g_p(v, v) = 0$ — a hypersurface in $T_pM$ (a quadric cone). It separates the timelike directions (inside the cone, in two halves) from the spacelike directions (outside the cone). This geometric structure — light cone in every tangent space — is the local model for the global **causal structure** of spacetime: which events can causally influence which.

**Why are timelike vectors "physically realisable" but spacelike not?** A particle's worldline is a curve in $M$, and its velocity vector at each point lies in the tangent space. For a *massive* particle moving slower than light, the velocity is in the timelike interior of the light cone. For *light* (photons), the velocity is on the light cone (null). For a *spacelike* direction, there is no physical particle whose worldline points there — moving faster than light would be required, and that is excluded in relativity. So the timelike-null part of the tangent space is physically realisable, and the spacelike part is not (for worldlines; for instantaneous spatial vectors it is). This is what justifies the name "causal" for timelike-or-null.

**Why is the term "norm-squared" not a true norm?** Because for spacelike vectors $g(v, v) < 0$, so $\sqrt{g(v, v)}$ is imaginary, and for null vectors it is zero on a nonzero vector — both fail the axioms of a true norm. The term "Lorentzian norm-squared" or just "$g$-norm-squared" is conventional; one writes $|v|^2_g = g(v, v)$ with the understanding that this is not non-negative. For spacelike vectors one sometimes defines the "spacelike length" $\sqrt{-g(v, v)}$, which is real and non-negative for spacelike vectors.

**Per-axiom failure analysis (really per-case analysis):**

(a) *What if we drop the indefiniteness?* Then $g$ is positive-definite (Riemannian), and the only sign possible is positive (or zero for $v = 0$). No trichotomy. This is the *whole* difference between Riemannian and Lorentzian geometry, and the causal structure is the new feature.

(b) *What if we drop non-degeneracy?* Then there are vectors with $g(v, w) = 0$ for every $w$ — null vectors in a degenerate-form sense, but also "invisible" vectors. The classification becomes muddled, and the meaningful definition of light cone breaks down.

(c) *What if the signature is $(p, q)$ with $p, q \geq 2$?* The set $\{v : g(v, v) > 0\}$ is now a multi-dimensional cone, not a half-line of a single one-dimensional cone. The single "time direction" of a Lorentzian manifold has no analogue, and the causal structure is replaced by a higher-dimensional cone structure. Such manifolds (signature $(2, 2)$, $(3, 3)$, etc.) appear in twistor theory but do not have the simple causal structure of the Lorentzian case.

---

# The Definition

> **Definition (Causal classification).** Let $(M, g)$ be a Lorentzian manifold (signature $(1, n-1)$). A nonzero tangent vector $v \in T_pM \setminus \{0\}$ is:
>
> (i) **timelike** if $g_p(v, v) > 0$;
>
> (ii) **spacelike** if $g_p(v, v) < 0$;
>
> (iii) **null** (or **lightlike**) if $g_p(v, v) = 0$.
>
> The zero vector $v = 0$ is conventionally classified as spacelike (some authors), or as "trivially null" (others), or left unclassified. A nonzero vector that is either timelike or null is called **causal** — these are the directions along which physical signals can travel.

The set of null vectors at $p$ is called the **light cone** at $p$, denoted $C_p \subseteq T_pM$. It is a quadric hypersurface in $T_pM$ — the zero set of the quadratic form $v \mapsto g_p(v, v)$, which in pseudo-orthonormal coordinates is $(v^0)^2 - \sum_{i=1}^{n-1}(v^i)^2 = 0$. Removing the origin, $C_p \setminus \{0\}$ has two connected components — the **future light cone** and the **past light cone** — *if* the manifold is time-oriented (a global choice of future-pointing direction at every point). Without a time orientation, the two halves of the cone are not globally distinguishable, only locally at each point.

The set of timelike vectors at $p$ forms an open set with two connected components (inside the future light cone and inside the past light cone, when time-oriented). The set of spacelike vectors is connected (it is the complement of the closed solid light cone, which is connected since the light cone has codimension $1$ and removing it from $T_pM$ leaves a single connected piece when $n - 1 \geq 2$, or two pieces in 2-D).

A **causal curve** is a smooth (or piecewise smooth) curve $\gamma : I \to M$ such that $\dot\gamma(t)$ is causal (timelike or null) at every $t$. A **timelike curve** has $\dot\gamma$ timelike everywhere; a **null curve** has $\dot\gamma$ null everywhere.

---

# Relate to Other Fields / Compression

This is the manifold version of the [[Def - Classification of Four-Vectors|four-vector classification]] from [[Special Relativity I — Lorentz Transformations and Minkowski Space]]. In flat Minkowski space $(\mathbb{R}^4, \eta)$ the classification is global and frame-invariant by direct calculation; in a curved Lorentzian manifold the classification is pointwise — at each event the tangent space is a Minkowski-like vector space with its own light cone — but the same trichotomy holds. The global structure is more subtle: when the light cones at different points are "glued together" by the smooth structure of the metric, they produce a global causal structure on $M$, the central object of mathematical general relativity.

In physics, the classification is the geometric content of the speed of light limit. Massive particles (positive rest mass) have timelike worldlines; massless particles (light) have null worldlines; tachyons (which would have spacelike worldlines) are excluded as unphysical. So the causal classification corresponds directly to the particle taxonomy of relativistic physics: massive, massless, or unphysical.

**True name:** The causal classification is *the partition of nonzero tangent vectors into orbits of the Lorentz group $O(1, n-1)$ on $T_pM \setminus \{0\}$*. The three orbits are the timelike (split into future and past in the time-oriented case), the spacelike, and the null vectors. The classification by sign of $g(v, v)$ is the operational form; the orbit picture is the structural one.

---

# Examples / Corollaries

**Is an instance — vectors in Minkowski space.** In $(\mathbb{R}^4, \eta)$ with $\eta = \mathrm{diag}(1, -1, -1, -1)$:
- $v = (1, 0, 0, 0)$ has $\eta(v, v) = 1 > 0$ — timelike.
- $v = (0, 1, 0, 0)$ has $\eta(v, v) = -1 < 0$ — spacelike.
- $v = (1, 1, 0, 0)$ has $\eta(v, v) = 1 - 1 = 0$ — null. This is a vector along a light ray in the $tx$-plane.
- $v = (2, 1, 0, 0)$ has $\eta(v, v) = 4 - 1 = 3 > 0$ — timelike, but tilted.

**Is an instance — vectors at a point of Schwarzschild spacetime.** Far from the black hole ($r \gg 2GM$), the metric is approximately Minkowski and the classification is approximately the special-relativistic one. Near the event horizon ($r = 2GM$), the metric coefficient $(1 - 2GM/r)$ vanishes, and what is "timelike" coordinate-wise reverses — inside the horizon, the radial coordinate becomes timelike and time becomes spacelike. This is the geometric content of "you cannot escape from inside the horizon": every causal future-directed curve must have $r$ decreasing.

**Is an instance — null [[Def - Geodesic|geodesics]] as light rays.** A null geodesic is a curve $\gamma$ whose tangent $\dot\gamma$ is always null and parallel-transported. In Minkowski space these are straight lines with $\eta(\dot\gamma, \dot\gamma) = 0$ — light rays. In curved spacetime they are the worldlines of light propagating through the gravitational field; gravitational lensing is the deflection of null [[Def - Geodesic|geodesics]] by curvature.

**Is NOT an instance — the zero vector.** The zero vector $v = 0$ is conventionally excluded from the classification (or assigned to "spacelike" by some authors). It has $g(0, 0) = 0$ trivially but is not what one means by "null" — null means $g(v, v) = 0$ and $v \neq 0$.

**Is NOT an instance — a Riemannian "null vector".** In a Riemannian manifold (positive-definite metric), the equation $g(v, v) = 0$ forces $v = 0$. So Riemannian manifolds have no nontrivial null vectors. The whole classification is empty for them, which is another way of saying Riemannian geometry has no causal structure.

**Corollary — the trichotomy is invariant under [[Def - Isometry|isometries]].** If $F : (M, g) \to (N, h)$ is a Lorentzian isometry and $v \in T_pM$, then $h(dF_p v, dF_p v) = g(v, v)$, so $v$ and $dF_p v$ have the same sign of norm-squared, hence the same causal classification. Causal classification is preserved by [[Def - Isometry|isometries]].

**Corollary — the trichotomy is invariant under parallel transport.** The Levi-Civita connection of a Lorentzian metric is metric-compatible: parallel transport along a curve preserves $g$. So a tangent vector that is timelike (resp. spacelike, null) at one point remains so under parallel transport along any curve. In particular, a geodesic that is timelike at one point is timelike everywhere along its trajectory (since $\dot\gamma$ is parallel-transported along $\gamma$).

**Corollary — the reverse triangle inequality for timelike vectors.** For future-directed timelike vectors $u, v$ in Minkowski space (or in the tangent space of a Lorentzian manifold), $\sqrt{g(u + v, u + v)} \geq \sqrt{g(u, u)} + \sqrt{g(v, v)}$ — the triangle inequality reversed. See [[Thm - The Reversed Triangle Inequality]] in the SR notes. The geometric content: an "inertial worldline" (straight) between two timelike-separated events is the *longest* in proper time, not the shortest — the twin paradox.

**Calibration check.** First, classify the vectors $v_1 = (3, 1, 0, 0)$, $v_2 = (1, 1, 1, 0)$, $v_3 = (1, \sqrt{2}, 0, 0)$ in Minkowski $\mathbb{R}^4$ with $\eta = \mathrm{diag}(1, -1, -1, -1)$. Expected: $\eta(v_1, v_1) = 9 - 1 = 8 > 0$ timelike; $\eta(v_2, v_2) = 1 - 1 - 1 = -1 < 0$ spacelike; $\eta(v_3, v_3) = 1 - 2 = -1 < 0$ spacelike (note that $v_3$ is *not* null despite having component magnitude $1, \sqrt{2}$). Second, find all null vectors in 2-D Minkowski space $(\mathbb{R}^2, \eta = dt^2 - dx^2)$. Expected: $\eta(v, v) = (v^0)^2 - (v^1)^2 = 0$ iff $v^0 = \pm v^1$, i.e., $v = (\pm a, a)$ for $a \in \mathbb{R}$ — the light cone is two lines through the origin. Third, show that in a 2-D Lorentzian manifold the set of timelike vectors at a point is disconnected (two halves), but in [[Def - Dimension|dimension]] $\geq 3$ it is *not* obvious from this without time orientation. (In any [[Def - Dimension|dimension]], the timelike set has two connected components, but distinguishing "future" from "past" requires a continuous choice.)

---

# Unlocked by This

> [!tip] The Causal Structure of Spacetime *(from Mathematical General Relativity)*
> The pointwise classification at every tangent space, smoothed out across the manifold, gives the **global causal structure** of a Lorentzian manifold: the chronological and causal future/past of events ($I^+(p)$, $J^+(p)$), the achronal sets, the Cauchy surfaces. This is the geometric data on which the **singularity theorems** of Penrose and Hawking, the **positive energy theorem** of Schoen–Yau and Witten, and the entire **cosmic censorship** programme of Penrose are built. The classification of a single tangent vector grows into the global geometric structure of spacetime.

> [!tip] The Light Cone as Fundamental Structure *(from Conformal Geometry)*
> The light cone at each point is a more fundamental structure than the metric itself. Two Lorentzian metrics related by a *conformal* rescaling $g' = \Omega^2 g$ (with $\Omega > 0$ smooth) have the same light cones — null vectors of $g$ are null vectors of $g'$ — and the resulting **conformal structure** is exactly the data of the light cones. The Penrose conformal compactification, the singularity theorem proofs (which use only causal structure), and conformal techniques in gravitational scattering theory all live at this level. The metric retains information beyond conformal structure (the actual lengths of timelike intervals), but the causal/conformal structure already captures much.

> [!tip] The Energy Conditions of General Relativity *(from General Relativity)*
> The Einstein field equations relate $g_{\mu\nu}$ to the energy–momentum tensor $T_{\mu\nu}$. Physical reasonableness of matter is encoded in **energy conditions**: the **weak energy condition** $T_{\mu\nu}t^\mu t^\nu \geq 0$ for every timelike $t$ (energy density is non-negative in every frame); the **null energy condition** $T_{\mu\nu}k^\mu k^\nu \geq 0$ for every null $k$ (light propagating through matter is not focussed in pathological ways); the **strong** and **dominant** energy conditions. Each of these is a statement about $T_{\mu\nu}$ evaluated on causal vectors — the causal classification of tangent vectors is what gives the conditions meaning. The singularity theorems use null and strong energy conditions essentially.

> [!tip] Black Holes — Event Horizon as a Null Hypersurface *(from Black Hole Physics)*
> The **event horizon** of a black hole is a null hypersurface: a hypersurface whose tangent vectors include a null direction (the "generators" of the horizon are null geodesics). The geometry of null hypersurfaces — Raychaudhuri's equation for null congruences, area theorems, surface gravity — is a substantial chapter of mathematical general relativity, and the causal classification is what makes null hypersurfaces distinguished.
