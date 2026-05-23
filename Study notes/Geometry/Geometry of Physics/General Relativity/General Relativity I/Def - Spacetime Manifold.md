---
type: definition
subject: general-relativity
prereqs:
  - "Def - Lorentzian Manifold"
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Causal Classification of Tangent Vectors"
  - "Def - Smooth Manifold"
tags: [physics, general-relativity, lorentzian-geometry]
---

# Notation

A standing convention: throughout this topic, **signature is $(+,-,-,-)$ and units are geometrised ($c = G = 1$)**. The spacetime metric is denoted $g$, with components $g_{\mu\nu}$ in a coordinate chart, $\mu, \nu \in \{0, 1, 2, 3\}$. Greek indices range over $0, 1, 2, 3$ (spacetime); Latin indices $i, j, k$ over $1, 2, 3$ (spatial). The metric determinant $g = \det(g_{\mu\nu})$ is negative in Lorentzian signature; $\sqrt{-g}\, d^4x$ is the natural volume element. Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!warning] Convention: signature
> Frankel and these notes use $(+,-,-,-)$ ("mostly minus"). Wald, MTW, Carroll, and most contemporary GR textbooks use $(-,+,+,+)$ ("mostly plus"). Under signature flip, timelike means $g(v,v) < 0$ rather than $g(v,v) > 0$, and the sign of the Ricci tensor flips. Always check the convention of a source before importing formulas.

---

# Axiom Motivation

The desideratum is to set up the *geometric stage* on which general relativity will be performed. We need an arena in which: (i) the special-relativistic experience of every freely-falling observer is recovered locally, (ii) gravity can be encoded as a global geometric feature (curvature) rather than a force, (iii) the worldlines of massive particles, light rays, and observers can be described as curves, and (iv) the Einstein field equations make sense as PDEs for the geometric structure. The minimal mathematical object meeting all four is a *Lorentzian manifold*.

The dimension is four because special relativity has four-dimensional Minkowski space as its arena (one time, three spatial directions), and GR must reduce to SR locally. Higher-dimensional spacetimes (5D, 10D, 11D) appear in **Kaluza–Klein theory**, **string theory**, and **brane-world cosmologies**, but the observed physical world has four large dimensions, and the standard GR setup is four-dimensional.

**Why a manifold?** Because we want a geometric object where coordinates are local labels with no intrinsic significance — the same physics described in many coordinate systems, with smooth transitions between them. The diffeomorphism invariance that powers all of GR (the principle of general covariance) is exactly the freedom to use any smooth chart, which is the defining feature of a manifold. We want **smooth** charts because the Christoffel symbols (derivatives of the metric) and the Riemann tensor (second derivatives) must make sense; $C^\infty$ is the generous default, though existence theorems for the Einstein equations are usually proved with weaker regularity (Sobolev classes).

**Why connected?** A disconnected spacetime would have causally separate components — different "universes" — that cannot influence each other and have no operational interaction. Connectedness is the assumption that we are studying *one* universe. Mathematically it is a normalisation; the field equations could be solved component-by-component anyway.

**Why Hausdorff and second countable?** These are the standard topological regularity conditions on a [[Def - Smooth Manifold|smooth manifold]] that ensure partitions of unity exist, which in turn ensure that local objects (frame fields, connections, integrals) can be patched together globally. Without Hausdorff, distinct points cannot always be separated by disjoint neighbourhoods, allowing pathologies like the "line with two origins" — a manifold-like space where two points have identical neighbourhoods. Without second countable, partitions of unity may fail to exist, blocking the construction of global Riemannian metrics by averaging.

**Why Lorentzian signature?** Because the local model is Minkowski space, which has signature $(+,-,-,-)$ — one positive (time) direction, three negative (spatial) directions. The signature is what produces the **light cone** at every event, separating timelike from spacelike from null directions, and giving rise to all of causal structure. A Riemannian (positive-definite) metric on a 4-manifold would be perfectly mathematically consistent but would have no notion of time, no light cone, no causal structure — it would not be a spacetime. The fact that only certain 4-manifolds admit a Lorentzian metric — a topological obstruction — is a deep result (see [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]]); for example, $S^4$ does not admit one.

**Why a time orientation?** The light cone at each event has two halves (the future cone and the past cone, in Minkowski space's terminology), but distinguishing future from past requires a *continuous* choice — a continuous future-pointing timelike vector field. This is the **time orientation**. Without it, one cannot globally distinguish forward time evolution from backward, and concepts like "before" and "after" become ambiguous. Most physical spacetimes are time-orientable (e.g., Schwarzschild, FLRW); some interesting ones (Gödel universe with closed timelike curves, certain pp-waves) are not. Standard GR assumes time-orientability as part of the definition of spacetime.

**What is excluded by each axiom failure?**

(a) *If we drop connectedness*: causally separate components — physically uninteresting, since by construction no signal connects them.

(b) *If we drop Hausdorff*: pathological "branched" spacetimes (e.g., where time can split into multiple futures), studied as toy examples of non-deterministic evolution but not standard.

(c) *If we drop second countable*: long lines, etc. — topologically pathological, blocks construction of partitions of unity.

(d) *If we drop Lorentzian signature*: no causal structure, no relativity. Riemannian 4-manifolds describe "Euclidean gravity" (a tool in **quantum gravity via the Euclidean path integral**, **gravitational instantons**), but not physical spacetimes.

(e) *If we drop time orientation*: causally consistent in some patches but no global "arrow of time"; **closed timelike curves** can exist, and one runs into the **grandfather paradox**.

**Forward reference (why is the structure exactly this?):** The full structural reason for these axioms emerges from the **initial-value formulation** of the Einstein equations. To have a well-posed Cauchy problem — given initial data on a 3D spatial slice, solve for the future evolution — one needs **global hyperbolicity**: the spacetime should be foliated by a one-parameter family of spacelike Cauchy surfaces. This is a *stronger* condition than time-orientability, and is usually added in mathematical GR; spacetimes that are not globally hyperbolic admit closed timelike curves or other causal pathologies.

---

# The Definition

> **Definition (Spacetime).** A **spacetime** is a quadruple $(M, g, \tau)$ consisting of:
>
> (i) a four-dimensional, connected, Hausdorff, second-countable smooth manifold $M$;
>
> (ii) a smooth Lorentzian metric $g$ on $M$ — a smooth section of $S^2 T^*M$ such that at each point $p \in M$, the bilinear form $g_p$ on $T_p M$ has signature $(+, -, -, -)$;
>
> (iii) a **time orientation** $\tau$: a smooth, globally-defined, future-pointing timelike vector field on $M$ (or equivalently, a continuous choice of the "future" half of the light cone at each event).
>
> Points of $M$ are called **events**. A smooth curve $\gamma : I \to M$ is **timelike** if $g(\dot\gamma, \dot\gamma) > 0$ everywhere; **null** if $g(\dot\gamma, \dot\gamma) = 0$ everywhere with $\dot\gamma \neq 0$; **spacelike** if $g(\dot\gamma, \dot\gamma) < 0$ everywhere; **causal** if it is timelike or null. The **worldline** of a particle is a future-directed causal curve.

The metric is sometimes written in **abstract index notation** as $g_{ab}$ (Penrose's convention), where indices are formal labels rather than coordinate components, to emphasise that the metric is a coordinate-independent object. In coordinate form, $g = g_{\mu\nu}(x)\, dx^\mu \otimes dx^\nu$, and the **line element** is $ds^2 = g_{\mu\nu}\, dx^\mu dx^\nu$.

Additional structures often assumed:

- **Time-orientable:** required as part of the definition (item iii). Non-time-orientable spacetimes exist but are not standard.
- **Globally hyperbolic:** there exists a smooth spacelike 3-surface $\Sigma \subseteq M$ that every inextendible causal curve crosses exactly once — a **Cauchy surface**. This is the strongest commonly-assumed causality condition, and ensures the Einstein equations have a well-posed initial-value problem on $\Sigma$.
- **Asymptotically flat:** $g$ approaches the Minkowski metric $\eta$ at spatial infinity, in a precise asymptotic sense. Used for isolated systems (stars, black holes) and for defining total mass via the ADM construction.

---

# Categorical / Structural Definition

In the language of [[Def - Riemannian Manifold|(semi-)Riemannian manifolds]], a spacetime is a four-dimensional, oriented, time-oriented [[Def - Lorentzian Manifold|Lorentzian manifold]]. From the structural side, it is the data of:

- A four-manifold $M$ — an object of the category of smooth manifolds with smooth maps as morphisms.
- A section of the bundle $S^2_- T^*M \to M$ of symmetric $(0,2)$-tensors with Lorentzian signature — the metric.
- A connected component of the bundle of non-spacelike vectors over $M$ — the time orientation.

The natural morphisms between spacetimes are **isometries** preserving the time orientation: smooth diffeomorphisms $f : M_1 \to M_2$ such that $f^* g_2 = g_1$ and $f_* \tau_1$ is future-directed in $M_2$. Two isometric spacetimes describe the same physics; the "general covariance principle" is the statement that physically meaningful quantities depend only on the isometry class.

The category of spacetimes is *not* well-behaved in obvious ways (no products, no colimits in general), but it admits enough structure to support most differential-geometric constructions: tensor bundles, connections, curvatures, integration, etc.

---

# Relate to Other Fields / Compression

A spacetime is the relativistic replacement for the Newtonian decomposition "space $\times$ time". In Newtonian mechanics, time is a separate scalar parameter, and space is a 3-dimensional Euclidean space $\mathbb{R}^3$; the product $\mathbb{R} \times \mathbb{R}^3$ is the arena. In special relativity, time and space are unified into Minkowski space $\mathbb{R}^{1,3}$ — see [[Def - Minkowski Space and the Metric]] — and the product structure is replaced by the indefinite metric. In general relativity, this unification is preserved but the metric becomes position-dependent; a spacetime is the local Minkowski structure assembled into a curved manifold.

**True name:** A spacetime is *the geometric object whose local model at every event is Minkowski space*. The equivalence principle is the assertion that physics in a small neighbourhood of an event is identical to physics in Minkowski space at the origin — and the spacetime is the global structure assembling these local Minkowski spaces. Operationally, "spacetime" is "Minkowski space, locally, with possibly nontrivial gluing".

The mathematical content (the Lorentzian manifold) is shared with [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]]; the physical content (the interpretation of events, worldlines, causality) is what distinguishes a spacetime from a generic Lorentzian manifold. The Einstein equations then constrain *which* Lorentzian manifolds qualify as physical spacetimes — namely those whose Einstein tensor is $8\pi$ times a physically reasonable stress-energy tensor.

---

# Examples / Corollaries

**Is an instance — Minkowski space.** The flat spacetime $(\mathbb{R}^4, \eta)$ with $\eta = \mathrm{diag}(1, -1, -1, -1)$, time orientation $\partial_t$. This is the spacetime of special relativity, the unique flat solution of the vacuum Einstein equations (up to identifications giving Minkowski quotients). It serves as the local model at every event of every spacetime.

**Is an instance — Schwarzschild spacetime.** The pair $(M, g)$ with $M = \mathbb{R} \times (2M, \infty) \times S^2$ (the exterior region $r > 2M$) and $g$ the Schwarzschild metric (see [[Def - The Schwarzschild Metric]]). Time orientation is given by $\partial_t$. This is the spacetime outside a non-rotating spherical mass. The maximal extension (Kruskal–Szekeres) includes the interior region $0 < r < 2M$ as well, and contains two asymptotically-flat exterior regions connected by a wormhole.

**Is an instance — Friedmann–Lemaître–Robertson–Walker (FLRW) cosmology.** With $M = I \times \Sigma$ for an interval $I \subseteq \mathbb{R}$ (cosmic time) and a 3-manifold $\Sigma$ of constant spatial curvature (sphere $S^3$, flat $\mathbb{R}^3$, or hyperbolic $\mathbb{H}^3$), and metric $ds^2 = dt^2 - a(t)^2 d\sigma^2$ where $a(t)$ is the scale factor and $d\sigma^2$ is the spatial metric on $\Sigma$. This is the standard cosmological model, describing a homogeneous and isotropic expanding universe.

**Is an instance — de Sitter spacetime.** $(\mathbb{R}^4, g)$ with constant positive curvature, the maximally symmetric vacuum solution of $R_{\mu\nu} = \Lambda g_{\mu\nu}$ for $\Lambda > 0$. Conformally, the entire de Sitter spacetime is a "ball" with future and past spacelike infinities. It serves as a model for the early universe (cosmic inflation) and for the late-time accelerated expansion driven by dark energy.

**Is NOT an instance — the 2-sphere $S^2$ with its round metric.** This is a Riemannian 2-manifold, not a spacetime: signature is $(+, +)$, not Lorentzian. It has no causal structure.

**Is NOT an instance — Euclidean $\mathbb{R}^4$ with the standard metric.** Signature $(+,+,+,+)$, not Lorentzian. Useful as a tool in **Euclidean quantum gravity** (Wick rotation), but not a physical spacetime.

**Is NOT an instance — the figure-eight space.** Not a manifold (not locally Euclidean at the crossing point). Spacetimes must be manifolds — every event has a neighbourhood diffeomorphic to $\mathbb{R}^4$.

**Is NOT an instance — a 4-dimensional manifold that admits no Lorentzian metric.** For example, $S^4$: there is a topological obstruction (the Euler characteristic must vanish for a closed manifold to admit a non-vanishing line field, equivalent to a Lorentzian metric). So $S^4$ has no spacetime structure — there is no Lorentzian metric on the 4-sphere.

**Corollary — At every event, the tangent space is Minkowski space.** $T_p M$ with the bilinear form $g_p$ is a four-dimensional real vector space with an indefinite inner product of signature $(+, -, -, -)$ — exactly Minkowski space. This is the formal content of the equivalence principle: the linear approximation to spacetime at any event *is* Minkowski space.

**Corollary — At every event, there exist locally inertial coordinates.** In a neighbourhood of any event $p$, one can choose coordinates (Riemann normal coordinates) in which $g_{\mu\nu}(p) = \eta_{\mu\nu}$ and $\partial_\rho g_{\mu\nu}(p) = 0$ — so all Christoffel symbols vanish at $p$. In these coordinates, the laws of physics at $p$ are exactly those of special relativity. (The second derivatives of $g$ cannot generically be made to vanish — they encode the Riemann curvature.)

**Corollary — Light cones partition tangent spaces.** At each event $p$, the tangent space $T_p M \setminus \{0\}$ partitions into: timelike vectors (open, two components — future and past), null vectors (the light cone, a hypersurface), spacelike vectors (open, one component for $n \geq 3$). The partition is invariant under Lorentz transformations of $T_p M$.

**Calibration check.** (i) Verify that the cylinder $S^1 \times \mathbb{R}^3$ with metric $d\phi^2 - dx^2 - dy^2 - dz^2$ is a spacetime, but is not simply connected — what timelike loops exist? (ii) Show that Minkowski space minus a point is still a spacetime (a manifold, Lorentzian, time-orientable), but is not globally hyperbolic. (iii) Compute the dimension of the space of spacetime metrics on a fixed 4-manifold $M$, modulo diffeomorphisms (the "moduli space"); this is infinite-dimensional.

---

# Unlocked by This

> [!tip] Global Causal Structure *(from Mathematical General Relativity)*
> Once the spacetime structure is fixed, the **causal future** $J^+(p) = \{q \in M : \exists$ future-directed causal curve from $p$ to $q\}$ and **chronological future** $I^+(p)$ (timelike curves only) are defined. The properties of these sets — closure, achronality, edge — and the analysis of **Cauchy surfaces**, **globally hyperbolic spacetimes**, and **conformal infinity** form the subject of **causal structure theory**. The **singularity theorems** of Hawking and Penrose, **cosmic censorship** conjectures, and the **positive mass theorem** all live at this level.

> [!tip] Initial-Value Formulation of GR *(from Numerical Relativity)*
> Specifying initial data on a Cauchy surface — a Riemannian metric $h_{\alpha\beta}$ on a 3-manifold $\Sigma$, plus its "time derivative" (the second fundamental form $b_{\alpha\beta}$) — and evolving via the Einstein equations gives the future development. The constraint equations on $\Sigma$ (Hamiltonian and momentum constraints, the $G_{0\mu}$ Einstein equations) restrict the initial data; the evolution equations propagate. This is the **ADM (Arnowitt-Deser-Misner) formulation** and the basis of **numerical relativity** — the computational simulation of black hole mergers, the source of recent gravitational wave detections.

> [!tip] Hawking–Penrose Singularity Theorems *(from Mathematical General Relativity)*
> Any spacetime satisfying reasonable conditions — energy conditions, generic condition on Riemann, plus either trapped surface or other geometric hypothesis — must contain incomplete causal geodesics: singularities are unavoidable. This says the Big Bang singularity in FLRW cosmology and the singularity at $r = 0$ inside a black hole are not artefacts of symmetry but structural features. The proofs use **focusing theorems** (Raychaudhuri's equation for null and timelike congruences) and the analysis of causal structure, applied to the spacetime manifold.

> [!tip] Cauchy Surfaces and Global Hyperbolicity *(from PDE Theory on Manifolds)*
> The well-posedness of the Einstein equations (and of hyperbolic PDEs on spacetimes in general) requires **global hyperbolicity**: existence of a Cauchy surface. Geroch (1970) showed that globally hyperbolic spacetimes are topologically products $\mathbb{R} \times \Sigma$, with $\Sigma$ a Cauchy surface. This connects spacetime topology to the PDE theory of evolution problems — only certain spacetime topologies admit well-posed initial-value problems for the field equations.
