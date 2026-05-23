---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Continuous Map"
  - "Def - Homeomorphism"
  - "Def - Path-Connected Space"
  - "Def - Connected Space"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$X, \tilde X$ are topological spaces, with $X$ connected and locally path-connected (and typically Hausdorff). $p : \tilde X \to X$ is the candidate covering map. For $x \in X$, the **fibre** is $p^{-1}(x) \subseteq \tilde X$. An open set $U \subseteq X$ is **evenly covered** by $p$ if $p^{-1}(U)$ is a disjoint union of open sets in $\tilde X$, each mapped homeomorphically to $U$ by $p$. The connected components of $p^{-1}(U)$ are called the **sheets** over $U$. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Axiom Motivation

We want to formalise the geometric picture: $\tilde X$ sits above $X$ in such a way that locally, $\tilde X$ looks like *several disjoint copies* of $X$ stacked on top of each other. Globally, the copies can twist and intermix (the helix above the circle, the orientable double cover of the Möbius strip), but locally near any point of $X$, the picture is trivial. So the definition must be local: at each point of the base, a neighbourhood lifts to a disjoint union of homeomorphic copies.

Why "homeomorphism" on each sheet and not just continuous bijection? Because we want both directions of the lift to be smooth (or continuous) — given a point in $U$, we want to choose a sheet and find the corresponding point in $\tilde X$ in a continuous way, and the inverse of $p$ restricted to a sheet must therefore be continuous. A continuous bijection in general is not a homeomorphism (the standard counterexample: $[0, 2\pi) \to S^1$ by $\theta \mapsto e^{i\theta}$), so we must demand the homeomorphism explicitly.

Why "disjoint" union? Because the local picture is supposed to be like stacked sheets — at each point of $U$, you should be able to tell unambiguously which sheet you are on. If the sheets glued together at any point in $p^{-1}(U)$, you would lose the ability to "lift" a path by following a specific sheet, and path lifting (the engine of the whole theory) would fail. Disjointness is what gives the fibre $p^{-1}(x)$ the structure of a *discrete* set: small neighbourhoods of distinct fibre points are disjoint.

What if we *dropped* the local-triviality condition and just demanded a surjective local homeomorphism? You get the broader class of **étale maps** in topology. Without local triviality, you can lose the ability to lift paths globally — locally you can pick a sheet, but globally the choices may not be coherent. For example, the open map $\mathbb{R} \sqcup \mathbb{R} \to \mathbb{R}$ that is identity on each copy is a local homeomorphism but not a covering map, since it is not surjective in the right sense — and worse, removing a point produces examples that are surjective local homeomorphisms but not coverings. Local triviality (= evenly covered neighbourhoods) is what makes the global theory clean.

What if we *strengthened* by demanding the same number of sheets globally? In the connected case, this is automatic: the function $x \mapsto |p^{-1}(x)|$ is locally constant (each evenly covered neighbourhood has the same fibre size everywhere) and hence constant on connected components of $X$. So local triviality plus connectedness of $X$ already gives a well-defined "sheet number," and we do not need to add it as an axiom.

What if we *strengthened* to demand $\tilde X$ connected? This is sometimes done — "connected covering space" — and most of the interesting theory does need it. But there are useful non-connected coverings (the trivial cover $X \sqcup X \to X$, the universal cover of a disconnected base) and the right convention is to put the connectedness on $\tilde X$ when it matters, leaving the bare definition free of it.

The base assumptions on $X$ (path-connected, locally path-connected, semi-locally simply connected) come in not at the definition of "covering" but at the *existence* of universal covers — see [[Def - Universal Cover]]. The bare notion of covering map needs only continuity and local triviality.

---

# The Definition

Let $X$ be a topological space. A continuous map $p : \tilde X \to X$ is a **covering map** (and $\tilde X$ is a **covering space** of $X$) if every point $x \in X$ has an open neighbourhood $U$ — called **evenly covered** by $p$ — such that
$$
p^{-1}(U) = \bigsqcup_{\alpha} \tilde U_\alpha
$$
is a *disjoint* union of open subsets $\tilde U_\alpha \subseteq \tilde X$, and for each $\alpha$, the restriction $p|_{\tilde U_\alpha} : \tilde U_\alpha \to U$ is a [[Def - Homeomorphism|homeomorphism]].

The set $p^{-1}(x) \subseteq \tilde X$ is called the **fibre** over $x$; it is a *discrete* subset of $\tilde X$. When $X$ is connected, $|p^{-1}(x)|$ is independent of $x$ and is called the **number of sheets** of the cover. A cover with $k$ sheets is **$k$-sheeted**. An **$\infty$-fold** cover has infinite fibres at every point.

In the smooth category, if $X$ and $\tilde X$ are [[Def - Smooth Manifold|smooth manifolds]] and $p$ is smooth (in addition to satisfying the topological covering condition), one says $p$ is a **smooth covering map**. In this case each restriction $p|_{\tilde U_\alpha}$ is a [[Def - Diffeomorphism|diffeomorphism]].

A covering map is automatically:
- a [[Def - Continuous Map|continuous]] surjection (provided $X$ is connected and $\tilde X$ is non-empty);
- an open map (each $\tilde U_\alpha$ is open, and $p$ maps it homeomorphically onto an open $U$);
- a [[Def - Continuous Map|local homeomorphism]] (each point of $\tilde X$ has a neighbourhood mapped homeomorphically by $p$).

---

# Categorical / Structural Definition

A covering map $p : \tilde X \to X$ is a **fibre bundle with discrete fibre** — equivalently, a [[Def - Continuous Map|continuous]] map whose homotopy fibres are discrete spaces. In the category of fibre bundles, coverings are the case where the structure group is discrete (no continuous gauge freedom) and the fibre is a discrete set, so the bundle is locally trivial in the strongest possible sense.

In the language of sheaves, a covering map corresponds to a **locally constant sheaf** on $X$: the sheaf whose stalk at $x$ is the fibre $p^{-1}(x)$, with the local triviality saying the sheaf is locally constant. This is the bridge to the **étale fundamental group** in algebraic geometry: replacing topological covers by étale morphisms gives the algebraic analogue, with locally constant sheaves becoming "locally constant in the étale topology."

In the category $\mathbf{Top}_{/X}$ of topological spaces over $X$ (with morphisms being maps respecting projection to $X$), coverings form a full subcategory **closed under**: fibre products (the fibre product of two covers is a cover), disjoint unions, and quotients by free actions of finite groups. This is what makes the category of covers tractable, and is what supports the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]] with the subgroup lattice of $\pi_1$.

---

# Relate to Other Fields / Compression

A covering map is a **fibre bundle with discrete fibre**. Once you know fibre bundles, covering maps are the simplest case: the fibre is a discrete set (no continuous structure), so the structure group is the symmetric group of the fibre (or a subgroup thereof). The bundle classification of covers is by subgroups of $\pi_1$ of the base — see [[Thm - Galois Correspondence for Covering Spaces]] and [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]].

A covering map is also the **topological analogue of a Galois extension of fields**. In Galois theory, finite separable extensions of $K$ correspond to subgroups of $\mathrm{Gal}(\bar K / K)$; in covering-space theory, connected covers correspond to subgroups of $\pi_1$. The analogy is precise: Grothendieck's étale fundamental group makes it a literal statement of equivalence of categories.

**True name:** a covering map is a *local trivialisation in the strongest sense* — locally, $\tilde X \to X$ is a product $U \times F \to U$ with $F$ discrete. Globally, the discrete structure of the fibre forces the cover to be classified entirely by the **monodromy** action of $\pi_1(X)$ on a single fibre. So the true name of a covering map is: a *fibre bundle with discrete fibre*, classified up to isomorphism by an action of $\pi_1$ on the fibre.

---

# Examples / Corollaries

**Is an instance: $p : \mathbb{R} \to S^1$, $t \mapsto e^{2\pi i t}$.** The exponential map covers the circle infinitely. For any $z \in S^1$ with $z = e^{2\pi i \theta_0}$, the open arc $U = \{e^{2\pi i \theta} : |\theta - \theta_0| < \tfrac14\}$ is evenly covered by the disjoint union $\bigsqcup_{n \in \mathbb{Z}} (\theta_0 - \tfrac14 + n, \theta_0 + \tfrac14 + n)$ — infinitely many intervals, each mapped homeomorphically to $U$ by $p$. This is the **universal cover** of $S^1$; the deck group is $\mathbb{Z}$ acting by integer translations.

**Is an instance: $p : S^n \to \mathbb{RP}^n$ by antipodal quotient.** The map identifying antipodal points $x \sim -x$ gives a 2-sheeted cover. Each point $\mathbb{RP}^n$ has a small enough neighbourhood whose preimage is two disjoint open hemispheres, each homeomorphic to the neighbourhood. For $n \geq 2$, this is the **universal cover** of $\mathbb{RP}^n$ (since $S^n$ is simply connected for $n \geq 2$), and the deck group is $\mathbb{Z}/2$ acting antipodally.

**Is an instance: $p : \mathbb{R}^n \to T^n$ by $(\theta_1, \dots, \theta_n) \mapsto (e^{2\pi i \theta_1}, \dots, e^{2\pi i \theta_n})$.** The $n$-fold product of the $S^1$ cover gives the universal cover of the $n$-torus. The fibre is $\mathbb{Z}^n$; deck group is $\mathbb{Z}^n$ acting by integer translations.

**Is an instance: $p : S^1 \to S^1$, $z \mapsto z^n$ (for $n \geq 1$).** Each point of the base $S^1$ has $n$ preimages, distributed at angles differing by $2\pi/n$. This is the $n$-sheeted cover of the circle; it corresponds to the subgroup $n\mathbb{Z} \leq \mathbb{Z} = \pi_1(S^1)$. Note it is *not* the universal cover — the universal cover of $S^1$ is $\mathbb{R}$.

**Is an instance: $p : \mathrm{SU}(2) \to \mathrm{SO}(3)$, the spin double cover.** $\mathrm{SU}(2) \cong S^3$ is simply connected, $\mathrm{SO}(3) \cong \mathbb{RP}^3$ has $\pi_1 = \mathbb{Z}/2$; the map is a 2-sheeted covering and a Lie-group homomorphism. See [[Ex - SU(2) is the Universal Cover of SO(3)]].

**Is an instance: the orientation cover of the Möbius strip.** The Möbius strip has a 2-sheeted cover by a cylinder $S^1 \times I$, with the cover identifying $(z, t)$ with $(-z, -t)$ — see [[Ex - The Orientable Double Cover of the Möbius Strip]] and [[Def - Orientable Double Cover]].

**Is NOT an instance: $p : (0, \infty) \to S^1$, $t \mapsto e^{2\pi i \log t}$.** This is a local homeomorphism, but it is *not* a covering map: although every point has preimages, the preimages near a fixed $z \in S^1$ accumulate at $0$, so no neighbourhood of $z$ is evenly covered (the preimage stretches off to $t \to 0^+$ without a clean disjoint-union structure).

**Is NOT an instance: $p : [0, 1] \to S^1$, $t \mapsto e^{2\pi i t}$.** This map is *almost* a covering — restricted to $(0, 1)$ it would be — but the endpoints $0$ and $1$ both map to the basepoint $1 \in S^1$, and any neighbourhood of $1$ has preimage that is *not* a disjoint union of homeomorphic copies. The compactness of $[0,1]$ ruins local triviality at the basepoint.

**Is NOT an instance: the projection $\mathbb{R}^2 \to \mathbb{R}$, $(x,y) \mapsto x$.** This is a fibre bundle with fibre $\mathbb{R}$, but $\mathbb{R}$ is *not discrete* — the fibre is connected, not a disjoint union of points. So this is a fibration but not a covering map.

**Is NOT an instance: the Hopf map $S^3 \to S^2$.** This is a fibre bundle with fibre $S^1$ — connected, not discrete — so it is not a covering. (It is a principal $\mathrm{U}(1)$-bundle, generalising the structure of a covering.) See [[Ex - The Hopf Map is a Submersion]] and [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]].

**Corollary (uniqueness of path lifts):** for a covering $p : \tilde X \to X$, any continuous path $\gamma : I \to X$ together with a chosen starting lift $\tilde x_0 \in p^{-1}(\gamma(0))$ has a unique lift $\tilde\gamma : I \to \tilde X$ with $\tilde\gamma(0) = \tilde x_0$ — see [[Thm - Path Lifting and Homotopy Lifting]].

**Corollary (fibre cardinality is locally constant):** for a covering $p : \tilde X \to X$, the function $x \mapsto |p^{-1}(x)|$ is locally constant — so constant on connected components of $X$. Proof: on each evenly covered $U$, $|p^{-1}(x)| = $ number of sheets above $U$, independent of $x \in U$.

**Corollary (covering of a covering):** if $p : \tilde X \to X$ and $q : \tilde{\tilde X} \to \tilde X$ are covering maps and $X$ is locally path-connected, then $p \circ q : \tilde{\tilde X} \to X$ is also a covering map. This makes "covering" closed under composition.

**Calibration check.** If you can (a) write down what "evenly covered" means, (b) give two different coverings of $S^1$ and identify their number of sheets, and (c) explain why the projection $\mathbb{R}^2 \to \mathbb{R}$ is not a covering even though it is a fibre bundle, you have understood the definition. Bonus: verify that the antipodal map makes $S^2 \to \mathbb{RP}^2$ a covering by explicitly describing an evenly covered neighbourhood.

---

# Unlocked by This

> [!tip] The Galois Correspondence for Covers *(in this topic)*
> Once you have coverings, every connected cover $\tilde X \to X$ corresponds to a subgroup $p_*\pi_1(\tilde X) \leq \pi_1(X)$, and this correspondence is a bijection — see [[Thm - Galois Correspondence for Covering Spaces]]. So the cardinality of the **set of connected covers** of $X$ equals the cardinality of the **set of subgroups** of $\pi_1(X)$, a purely algebraic count.

> [!tip] Fibre Bundles and Principal Bundles *(from Gauge Theory II)*
> A covering map is a fibre bundle with discrete fibre. The general theory of [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet|fibre bundles]] allows the fibre to be any topological space and the structure group to be any topological group acting on the fibre. Principal bundles ($G$-torsors) are the "fundamental" fibre bundles; vector bundles come from associated-bundle constructions. The whole machinery of [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|gauge theory]] generalises the covering-space picture.

> [!tip] The Étale Fundamental Group *(from Algebraic Geometry)*
> Grothendieck replaced topological covers with **étale morphisms** of schemes (algebraic-geometric analogues of "local isomorphisms") and recovered a fundamental group $\pi_1^{\mathrm{ét}}(X)$ classifying finite étale covers. For complex algebraic varieties $\pi_1^{\mathrm{ét}}$ is the profinite completion of the topological $\pi_1$; for $X = \mathrm{Spec}\,K$ it is the absolute Galois group of $K$. This was Grothendieck's bridge from topology to number theory.
