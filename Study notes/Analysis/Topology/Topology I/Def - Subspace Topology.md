---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Basis and Subbasis for a Topology"
tags: [analysis, topology]
---

# Notation

$(X, \tau_X)$ is a topological space and $Y \subseteq X$ a subset. The **subspace topology** on $Y$ is denoted $\tau_Y$. The inclusion map is written $\iota : Y \hookrightarrow X$ — $\iota(y) = y$ as a function, but its source and target carry different topologies. Restriction of a function $f : Z \to X$ with image in $Y$ is written $f|^Y : Z \to Y$ (the corestriction). For $A \subseteq Y \subseteq X$, closures and interiors in different ambient spaces are distinguished by superscript: $\overline{A}^Y$ versus $\overline{A}^X$. The full notation registry sits on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

We have a topological space $X$ and we want to give a topology to a subset $Y \subseteq X$. There is essentially only one sensible answer, and the question is *what considerations force it*. Two universal requirements both lead to the same formula.

The first requirement is *continuity of the inclusion*. The inclusion $\iota : Y \to X$ should be continuous — moving a point in $Y$ slightly should move it slightly in $X$, which is what "inclusion" should mean topologically. Continuity of $\iota$ says: for every open $U \subseteq X$, the preimage $\iota^{-1}(U) = U \cap Y$ must be open in $Y$. So *at the very least* the topology on $Y$ must contain all sets of the form $U \cap Y$ for $U$ open in $X$. This forces a *lower bound* on what the open sets of $Y$ are.

The second requirement is *coherence with maps into $Y$*. A function $f : Z \to Y$ should be continuous if and only if the composition $\iota \circ f : Z \to X$ — which is the same function, viewed as taking values in the ambient space — is continuous. This is the natural compatibility: a function "into $Y$" should be continuous exactly when it is continuous "into $X$ landing in $Y$". For this to work, we cannot have *too many* open sets in $Y$ — extra open sets would make $\iota \circ f$ continuous (preimages of opens in $X$ are preimages of opens in $Y$ that come from $X$) without making $f$ continuous (extra open sets in $Y$ have preimages that need not be open in $Z$). So this requirement places an *upper bound* on the open sets of $Y$.

The two requirements meet at a single point: the topology on $Y$ must consist of *exactly* the sets $U \cap Y$ for $U$ open in $X$, no fewer and no more. The fewer bound comes from continuity of $\iota$; the more bound comes from the universal property of maps into $Y$. The formula

$$\tau_Y = \{U \cap Y : U \in \tau_X\}$$

is the unique topology satisfying both. This double universal-property characterization is itself the most important fact about the subspace topology: it tells you when you have it (whenever the formula holds) and what it does (the inclusion is continuous and corestriction is continuous-preserving).

One might ask why we do not just take the metric (if any) and use the same metric on $Y$. For metric spaces, this gives the same answer: the subspace topology coincides with the metric topology induced by restriction of the distance function. So there is nothing to choose between them. But for general topological spaces there is no metric to restrict, and the open-set formula is the only mechanism available. The metric case is a special case of the universal definition.

The closed-set version is then forced too: $C \subseteq Y$ is closed in $Y$ if and only if $C = F \cap Y$ for some closed $F \subseteq X$. The proof is mechanical: $C$ is closed in $Y$ iff $Y \setminus C$ is open in $Y$ iff $Y \setminus C = U \cap Y$ for some $U$ open in $X$, iff $C = (X \setminus U) \cap Y$ for $X \setminus U$ closed in $X$. So closeds-in-$Y$ are traces of closeds-in-$X$, just as opens-in-$Y$ are traces of opens-in-$X$.

---

# The Definition

Let $(X, \tau_X)$ be a topological space and $Y \subseteq X$ a subset. The **subspace topology** (or **relative topology** or **induced topology**) on $Y$ is the collection
$$\tau_Y = \{U \cap Y : U \in \tau_X\}.$$
Equipped with this topology, $Y$ is called a **subspace** of $X$. A subset $V \subseteq Y$ is **open in $Y$** if and only if $V = U \cap Y$ for some open $U$ in $X$; correspondingly, $C \subseteq Y$ is **closed in $Y$** if and only if $C = F \cap Y$ for some closed $F$ in $X$.

The subspace topology is characterized by the following universal property: it is the *unique* topology on $Y$ such that, for every topological space $Z$ and function $f : Z \to Y$,
$$f \text{ is continuous} \iff \iota \circ f : Z \to X \text{ is continuous},$$
where $\iota : Y \to X$ is the inclusion. Equivalently — and this is the form Bredon uses — it is the **coarsest** (smallest) topology on $Y$ making the inclusion $\iota$ continuous.

If $X$ is a metric space with metric $d$, the restriction $d|_{Y \times Y}$ is a metric on $Y$, and the topology it induces on $Y$ coincides with the subspace topology.

**Bases for the subspace topology.** If $\mathcal{B}$ is a basis for $\tau_X$, then $\{B \cap Y : B \in \mathcal{B}\}$ is a basis for $\tau_Y$. The subspace topology inherits a basis from any basis of the ambient topology.

**Transitivity.** If $Z \subseteq Y \subseteq X$, the subspace topology on $Z$ as a subset of $Y$ equals the subspace topology on $Z$ as a subset of $X$. Subspaces of subspaces are subspaces.

---

# Categorical Definition

In the category $\mathbf{Top}$ of topological spaces and continuous maps, the subspace topology realises the **subobject** $Y \hookrightarrow X$ in the sense of universal property — it is the unique topology that makes the inclusion $\iota : Y \to X$ a categorical *monomorphism* with the corresponding factorisation property.

The vocabulary needed is mild. A *category* $\mathcal{C}$ consists of objects, arrows between objects, an associative composition, and identity arrows. A *universal property* characterises an object by stating that arrows into or out of it correspond, naturally, to a simpler kind of data. An *equalizer* of two parallel arrows $f, g : A \rightrightarrows B$ is the universal object $E$ equipped with an arrow $e : E \to A$ such that $f \circ e = g \circ e$ and every other arrow $e' : E' \to A$ equalising $f$ and $g$ factors uniquely through $e$. A *pullback* is the analogous construction for a corner $A \to C \leftarrow B$.

With this vocabulary, the subspace topology is the **initial topology** induced by the single inclusion $\iota : Y \to X$. The initial topology on a set $Y$ induced by a family $\{f_\alpha : Y \to X_\alpha\}$ of functions to topological spaces is the *coarsest* topology making every $f_\alpha$ continuous; for the single map $\iota$ with target $(X, \tau_X)$, this gives precisely $\tau_Y = \{U \cap Y : U \in \tau_X\}$. Equivalently, the inclusion $\iota$ is the **equalizer** of the two maps $\chi_Y, 1 : X \rightrightarrows \{0, 1\}_{\text{Sierp}}$ to the Sierpiński space (with $\chi_Y$ the characteristic function of $Y$ and $1$ the constant map), and also the **pullback** of the inclusion $\{*\} \hookrightarrow \{0, 1\}_{\text{Sierp}}$ along $\chi_Y$ — each formulation expresses the same universal property in a different categorical idiom.

The two characterising properties stated above (continuity of $\iota$ as a lower bound, universal coherence with maps into $Y$ as an upper bound) are exactly the **universal property of the subobject**: any continuous map $f : Z \to X$ that factors set-theoretically through $Y$ does so *uniquely* through a continuous map $\tilde f : Z \to Y$. The subspace topology is whatever makes this lift continuous, and the formula $U \cap Y$ is the smallest topology that makes it so.

This is the same universal-property machinery that, with the family of all projections $\pi_\alpha : \prod X_\alpha \to X_\alpha$, gives the [[Def - Product Topology|product topology]]; and the dual machinery — *final* topology, coarsest making maps *out of* a space continuous — gives the quotient topology. The subspace, product, and quotient topologies are three instances of the same construction: take an existing space (or family) and produce the *unique* topology on a new set that makes a given map (or family of maps) continuous in the appropriate direction. The forgetful functor $U : \mathbf{Top} \to \mathbf{Set}$ has a left adjoint (discrete topology) and a right adjoint (indiscrete topology), and the subspace and quotient constructions sit inside this adjoint scaffolding.

---

# Relate to Other Fields / Compression

The subspace topology is the **pullback** construction in $\mathbf{Top}$ along an injection, and the same construction in different categories gives different inheritance laws. In the category of measurable spaces, a subset inherits a $\sigma$-algebra by intersection — the **trace $\sigma$-algebra** — by exactly the same formula: measurable in $Y$ iff trace of measurable in $X$. In smooth manifolds, the subspace topology is the *starting* topology on a submanifold, with the smooth structure pulled back from the ambient manifold's charts (see [[Def - Submanifold of Euclidean Space]]).

In the category of metric spaces, the subspace topology agrees with the topology induced by the restricted metric — the two structures (topology and metric) are pulled back in compatible ways. This is a special feature of metric spaces, and one reason the metric formalism is so robust: every natural categorical operation preserves the metric-to-topology correspondence.

A cautionary parallel: in **group theory**, a subset $H \subseteq G$ inherits the binary operation of $G$ trivially, but only forms a subgroup if it is closed under the operation and contains inverses — there is a *condition* on the subset, not just a construction. In topology, by contrast, every subset is automatically a subspace: there is no condition to check. This is why "subspace" is a much more permissive notion than "subgroup" — and why subspaces of "nice" topological spaces can have completely different qualitative behaviour (e.g. $\mathbb{Q} \subseteq \mathbb{R}$ inherits a topology in which it is neither compact, nor locally compact, nor connected, nor complete in the inherited metric).

---

# Examples / Corollaries

**Is an instance — $[0, 1)$ as a subspace of $\mathbb{R}$.** The half-open interval $[0, 1)$ with the subspace topology from standard $\mathbb{R}$ has $[0, 1/2)$ as an open set: $[0, 1/2) = (-1, 1/2) \cap [0, 1)$, and $(-1, 1/2)$ is open in $\mathbb{R}$. So $[0, 1/2)$ is open in $[0, 1)$ but **not** open in $\mathbb{R}$ — the point $0$ lacks two-sided room in the ambient space. This is the prototypical example of a set that is open in the subspace but not in the whole.

**Is an instance — the rationals as a subspace of $\mathbb{R}$.** $\mathbb{Q} \subseteq \mathbb{R}$ with the subspace topology has as its open sets all $U \cap \mathbb{Q}$ for $U \subseteq \mathbb{R}$ open. The set $\{q \in \mathbb{Q} : q^2 < 2\}$ is open *and* closed in $\mathbb{Q}$: it equals $(-\sqrt{2}, \sqrt{2}) \cap \mathbb{Q}$ (open) and equals $[-\sqrt{2}, \sqrt{2}] \cap \mathbb{Q}$ (closed), because $\pm\sqrt{2} \notin \mathbb{Q}$ so the open and closed intervals agree on $\mathbb{Q}$. So $\mathbb{Q}$ is **totally disconnected** — every connected component is a single point — even though it sits inside the connected $\mathbb{R}$. The subspace topology can completely transform the qualitative behaviour.

**Is an instance — the sphere as a subspace of $\mathbb{R}^3$.** The 2-sphere $S^2 = \{x \in \mathbb{R}^3 : |x| = 1\}$ inherits a topology from $\mathbb{R}^3$. The open sets of $S^2$ are intersections of open subsets of $\mathbb{R}^3$ with $S^2$. The subspace topology is what makes $S^2$ a topological manifold; one then equips it with the smooth structure to do geometry. The local-homeomorphism property of a sphere — every point has a neighbourhood in $S^2$ homeomorphic to an open disc in $\mathbb{R}^2$ — is a property of the subspace topology, before any smooth structure is introduced.

**Is NOT a closed subspace in itself — $(0, 1)$ as a subspace of $\mathbb{R}$.** The open interval $(0, 1)$ inherits the subspace topology from $\mathbb{R}$. As a topological space in itself, it is homeomorphic to all of $\mathbb{R}$ (via $x \mapsto \tan(\pi(x - 1/2))$). So a property of $(0, 1)$ "as an ambient space" — like completeness in any inherited metric — is not a topological property and is *not* inherited from $\mathbb{R}$. Properties that *are* inherited: openness, closedness (of subsubsets), the subspace topology of further sub-subsets, and any property defined purely in terms of the open sets.

**Corollary — continuity of restrictions.** If $f : X \to W$ is continuous and $Y \subseteq X$, the restriction $f|_Y : Y \to W$ (where $Y$ carries the subspace topology) is continuous. *Proof:* $f|_Y = f \circ \iota$ where $\iota : Y \to X$ is continuous (by the universal property's lower bound) and $f$ is given continuous, so the composition is continuous. This is so silently used that it is rarely stated, but it is the foundation of every "consider the restriction of $f$ to..." argument in analysis.

**Corollary — corestriction to image.** If $f : Z \to X$ is continuous and $f(Z) \subseteq Y$, then $f$ factors through $Y$ as a continuous map $\tilde f : Z \to Y$. *Proof:* by the universal property of the subspace topology, $\tilde f$ is continuous iff $\iota \circ \tilde f = f$ is — and that is given. This is the "lift to a subspace" move and is one of the most-used legal operations in topology arguments.

**Corollary — closed-in-subspace formula.** A set $C \subseteq Y$ is closed in $Y$ if and only if $C = F \cap Y$ for some closed $F$ in $X$. Equivalently, $C$ is closed in $Y$ iff $C = \overline{C}^X \cap Y$ (every closed-in-subspace set is the trace of its own closure in $X$ — this is the content of [[Thm - Closure-in-Subspace Formula]]).

**Calibration check.** Compute the subspace topology of $\mathbb{Z} \subseteq \mathbb{R}$ — every singleton $\{n\} = (n - 1/2, n + 1/2) \cap \mathbb{Z}$ is open, so $\mathbb{Z}$ inherits the discrete topology. Verify that the subspace topology of any finite set in any Hausdorff space is discrete. Construct a basis for the subspace topology of $[0, 1] \subseteq \mathbb{R}$ — the half-open intervals $[0, b)$, $(a, b)$, $(a, 1]$ work. If you can also explain why a subset of a compact space need not be compact in the subspace topology but a *closed* subset always is, you have understood the difference between "inherited from $X$" and "true of $Y$ as its own space".

---

# Unlocked by This

> [!tip] Submanifolds of Euclidean Space *(from Differential Geometry)*
> A **submanifold** of $\mathbb{R}^n$ — see [[Def - Submanifold of Euclidean Space]] — is, before being any kind of smooth object, a topological subspace of $\mathbb{R}^n$. Every notion of "continuous function on the submanifold", "tangent vector at a point", "smooth chart" is defined relative to the subspace topology. The local triviality property (every point of the submanifold has a neighbourhood in the subspace topology homeomorphic to $\mathbb{R}^d$) is the topological substrate on which the smooth structure is erected.

> [!tip] Closed and Open Submanifolds *(from Differential Topology)*
> A submanifold is **closed** if it is a closed subspace of the ambient space — this is a topological condition. Closed submanifolds inherit completeness from the ambient (in any compatible metric), while open submanifolds need not. The closed-vs-open distinction at the subspace-topology level controls a long list of downstream geometric properties: completeness, boundedness, properness of maps, and the existence of compactly supported objects.

> [!tip] Initial and Final Topologies *(from General Topology)*
> The subspace topology is the prototype of the **initial topology** construction: given functions $f_\alpha : Y \to X_\alpha$, the coarsest topology on $Y$ making every $f_\alpha$ continuous. The dual construction — the coarsest topology on $X$ making functions *out of* $X$ continuous — is the **final topology**, which produces the [[Topology I — §1–3 Metric and Topological Spaces|quotient topology]]. The pair (initial, final) is the universal-property scaffolding underlying products, subspaces, quotients, sums, and the weak / weak-$*$ topologies of functional analysis.
