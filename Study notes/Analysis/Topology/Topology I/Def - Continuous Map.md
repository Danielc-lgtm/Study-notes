---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Notation

Throughout, $(X, \tau_X)$ and $(Y, \tau_Y)$ are topological spaces. We write $f : X \to Y$ for a function between the underlying sets, and $f^{-1}(B) = \{x \in X : f(x) \in B\}$ for the preimage of $B \subseteq Y$. The phrase "$f$ is continuous" always implicitly refers to a topology on the source and on the target — the same function can be continuous with respect to one pair of topologies and discontinuous with respect to another. A **map** in topology means a *continuous* function; the word carries this default meaning throughout the subject. For the full registry of symbols see [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

The whole motivation for inventing topological spaces was to support a notion of continuity that does not depend on having a metric. So now we must write down the topological definition of continuity. The starting point is the $\varepsilon$–$\delta$ definition on metric spaces and the bridge theorem [[Thm - Continuity via Open Sets (Metric Spaces)|continuity via open sets]]: in a metric space, $f$ is continuous if and only if $f^{-1}(U)$ is open for every open $U$. This formulation has no reference to balls or distances — only to the open-set collections on both sides. So it transfers verbatim to the abstract setting: declare $f : X \to Y$ continuous when $f^{-1}(U) \in \tau_X$ for every $U \in \tau_Y$.

The question is whether this *is* the right definition — whether other formulations should be considered and rejected. The candidates are:

(a) **Preimage-of-open is open.** $f^{-1}(U)$ open whenever $U$ open. This is the definition we will adopt.

(b) **Image-of-open is open.** $f(U)$ open whenever $U$ open. This is the definition of an **open map**, and it is a *different* notion — there exist continuous maps that are not open, and open maps that are not continuous.

(c) **Image-of-closed is closed.** Analogous: this is the definition of a **closed map**.

(d) **Preimage-of-closed is closed.** $f^{-1}(F)$ closed whenever $F$ closed. This is *equivalent* to (a) by complementation: $f^{-1}(Y \setminus B) = X \setminus f^{-1}(B)$, so preimage commutes with complement, and preimage of open is open if and only if preimage of closed is closed.

So the substantive choice is between *preimage* and *image*, and between *open* and *closed*. Preimage and image are not symmetric: preimage commutes with arbitrary intersections and unions, while image commutes only with unions (in general, $f(A \cap B) \subseteq f(A) \cap f(B)$ but not the reverse). This asymmetry is the technical reason preimage-of-open is the right definition: it is the operation that preserves the topology axioms, namely arbitrary unions and finite intersections. If we used image instead, we would need a definition that respects the axiom "arbitrary unions are open", which images do — but we would also need "finite intersections", which images do not respect. So preimage wins on structural grounds.

Concretely, the $\varepsilon$–$\delta$ definition translates to preimage-of-open, not image-of-open, because the *target* side gives the $\varepsilon$ (the open neighbourhood of $f(x)$) and the *source* side gives the $\delta$ (the open neighbourhood of $x$). The $\delta$-ball lies in the preimage of the $\varepsilon$-ball; one starts with an open set on the target and pulls back to find an open set on the source. Image-of-open would correspond to "starting with $\delta$ first" — a backwards direction that does not match the natural quantifier order.

To see that image-of-open and preimage-of-open are *really* different, consider $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$. The preimage of any open set is open (since $f$ is continuous), but the image $f((-1, 1)) = [0, 1)$ is not open. So this $f$ is continuous but not open. Conversely, the projection $\pi : \mathbb{R}^2 \to \mathbb{R}$, $\pi(x, y) = x$, is both continuous and open (the image of an open box is an open interval). But consider a map that *is* open but not continuous: take $X = \mathbb{R}$ with the discrete topology and $Y = \mathbb{R}$ with the standard topology, and let $f$ be the identity. Then every set on $X$ is open, so $f(U) \subseteq Y$ is... well, in this example every $U \subseteq \mathbb{R}$ on the source side is open, but its image $\pi U) = U$ is open in $Y$ only when $U$ was open in the standard sense. So that doesn't quite give an example; let me try again. Take $f : \mathbb{R}_\text{indiscrete} \to \mathbb{R}_\text{standard}$ (discrete on the source, standard on the target). Wait, this is backwards. The cleanest example: let $f : \mathbb{R} \to \mathbb{R}$ send $x$ to its fractional part for $x \in [0, 1)$ and to a fixed irrational outside $[0, 1)$; one can engineer such a function to be open (the image of intervals is open) but discontinuous. In general, *open* and *continuous* are independent properties; continuous functions need not be open and open functions need not be continuous. The two notions are dual but neither implies the other.

What goes wrong with image-of-open-is-open as a definition? Consider $f(x) = c$ constant on a discrete source. Every set on the source is open. The image of any open nonempty set is $\{c\}$, which is *not* open in (say) $\mathbb{R}$ with the standard topology. So a constant map fails to be "open" in the image sense, yet it is intuitively the *most* continuous map possible (everything maps to a single point — no movement at all). This single example shows image-of-open is not a sensible definition of continuity. The preimage formulation handles constants gracefully: $f^{-1}(U) = X$ if $c \in U$, $\emptyset$ otherwise, both of which are always open.

A second sanity check: continuity should be compositional. If $f : X \to Y$ and $g : Y \to Z$ are continuous, $g \circ f$ should be continuous. The preimage formulation makes this immediate: $(g \circ f)^{-1}(U) = f^{-1}(g^{-1}(U))$. If $U$ is open in $Z$, then $g^{-1}(U)$ is open in $Y$ (by continuity of $g$), so $f^{-1}(g^{-1}(U))$ is open in $X$ (by continuity of $f$). The image formulation would require $g(f(U))$ to be open whenever $U$ is open, which is the composition of "open" maps — and so it would only give a "compositional" continuity for open maps. This loses the metric-space continuity we started with. The preimage formulation extends $\varepsilon$–$\delta$ continuity; the image formulation does not.

A third reason: continuity should be a *local* notion. The map $f$ is continuous at $x$ if it sends nearby points to nearby points — a property of $f$ near $x$. The preimage formulation encodes this: $f^{-1}(V)$ is a neighbourhood of $x$ for every neighbourhood $V$ of $f(x)$, which is the local version of "preimage of open is open". The image formulation has no comparable local version — "$f$ at $x$ is open" would mean what?

Finally, the closed-set version $f^{-1}(F)$ closed whenever $F$ closed is *equivalent* to the open-set version by complementation. This is useful in practice: sometimes it is easier to verify continuity by checking closed sets (for instance when the closed sets are zero sets of equations). We will record this equivalence as an immediate corollary.

So the right definition is preimage-of-open-is-open, which (i) extends $\varepsilon$–$\delta$ continuity from metric spaces, (ii) makes composition automatic, (iii) makes constants trivially continuous, (iv) admits a local-at-a-point reformulation, (v) is equivalent to preimage-of-closed-is-closed, and (vi) is *not* the same as image-of-open-is-open (which gives a different and complementary notion called "open map").

---

# The Definition

Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be topological spaces and $f : X \to Y$ a function.

**Global continuity.** $f$ is **continuous** if
$$f^{-1}(U) \in \tau_X \quad \text{for every } U \in \tau_Y.$$
Equivalently (by complementation),
$$f^{-1}(F) \text{ is closed in } X \quad \text{for every closed } F \subseteq Y.$$

**Continuity at a point.** $f$ is **continuous at** $x \in X$ if for every open $U \subseteq Y$ with $f(x) \in U$, there exists an open $V \subseteq X$ with $x \in V$ and $f(V) \subseteq U$. Equivalently, $f^{-1}(U)$ is a neighbourhood of $x$ for every neighbourhood $U$ of $f(x)$.

**Equivalence of point-wise and global.** $f$ is continuous if and only if $f$ is continuous at every $x \in X$.

**Closed-set formulation.** $f$ is continuous if and only if $f^{-1}(F)$ is closed in $X$ for every closed $F \subseteq Y$, since $f^{-1}(Y \setminus B) = X \setminus f^{-1}(B)$.

**Closure formulation.** $f$ is continuous if and only if $f(\overline{A}) \subseteq \overline{f(A)}$ for every $A \subseteq X$. (One direction: $f^{-1}(\overline{f(A)})$ is closed and contains $A$, hence contains $\overline{A}$; so $f(\overline{A}) \subseteq \overline{f(A)}$. The other direction uses preimage of a closed set.)

**Map.** Throughout topology, the word **map** means *continuous function*. Unless explicitly stated, every function between topological spaces in the topology course is assumed continuous.

---

# Categorical Definition

A continuous map is precisely a **morphism in the category $\mathbf{Top}$**. The vocabulary: a *category* $\mathcal{C}$ consists of objects, arrows (or *morphisms*) between objects, an associative composition law for arrows, and an identity arrow on each object acting as a unit for composition. The category $\mathbf{Top}$ takes [[Def - Topological Space|topological spaces]] as objects and continuous maps as arrows; composition is ordinary function composition, identity arrows are identity functions, and the laws hold because (i) the composite of two continuous functions is continuous (as verified above) and (ii) the identity function is continuous in any topology.

The categorical viewpoint refines the structural meaning of "continuity preserves the open-set structure". From the [[Def - Topological Space#Categorical Definition|frame perspective]], a topological space is the data of a frame $\tau$ (the lattice of open sets) attached to a set $X$. A continuous map $f : X \to Y$ is then equivalent to a **frame homomorphism** going *backwards*, $f^{-1} : \tau_Y \to \tau_X$: the preimage operation sends open sets of $Y$ to open sets of $X$, preserves arbitrary unions ($f^{-1}(\bigcup U_\alpha) = \bigcup f^{-1}(U_\alpha)$), preserves finite intersections ($f^{-1}(U \cap V) = f^{-1}(U) \cap f^{-1}(V)$), preserves the top element ($f^{-1}(Y) = X$), and preserves the bottom element ($f^{-1}(\emptyset) = \emptyset$). These four conditions are exactly the data of a frame homomorphism, and they are exactly the content of "continuous = preimage of open is open". The contravariance — frame homomorphism goes the opposite way to the continuous map — is the same phenomenon as ring homomorphisms going the opposite way to morphisms of affine schemes: spaces and their "rings of opens" sit on opposite sides of an adjunction.

This is what makes the asymmetric preimage formulation (chosen over image-of-open) *categorically* natural: preimage is the functor that turns the geometric direction $X \to Y$ into the algebraic direction $\tau_Y \to \tau_X$. The image operation has no such functorial behaviour — it does not respect arbitrary intersections — and that is why "image of open is open" defines the genuinely different notion of an [[Def - Topological Space|open map]] rather than a morphism in $\mathbf{Top}$. The category $\mathbf{Top}$ has all the standard universal constructions: products (the [[Def - Product Topology|product topology]]), coproducts (disjoint unions), equalizers (subspaces), and coequalizers (quotient spaces), each characterised by the universal property that continuous maps factor through them in the expected way.

---

# Relate to Other Fields / Compression

A continuous map is the **morphism** in the **category of topological spaces** $\mathsf{Top}$. The objects are topological spaces; the morphisms are continuous maps. Composition is composition of functions (well-defined because composition of continuous functions is continuous); identities are identity maps (continuous because $\text{id}^{-1}(U) = U$). The categorical perspective compresses the entire theory: any construction in topology (subspace, product, quotient, sum, function space) is characterized by a *universal property* in $\mathsf{Top}$.

In **functional analysis**, the analogue is the **bounded linear map** between Banach spaces — a linear map $T : V \to W$ with $\lVert Tv \rVert \leq M \lVert v \rVert$ for some constant $M$. For linear maps, boundedness is equivalent to continuity (one direction is immediate; the other uses linearity to translate continuity at $0$ to continuity everywhere). This is the trigger pattern *"prove continuity → prove boundedness"* for linear maps: a single estimate establishes continuity, no $\varepsilon$–$\delta$ needed.

In **algebraic topology**, a **homotopy** is a continuous map $H : X \times [0, 1] \to Y$ deforming one map into another. The notion of homotopy is built on the notion of continuity: every step of the deformation is continuous, and the deformation itself is continuous. The fundamental group, homology, and cohomology are all *invariants* of the homotopy class of a continuous map.

In **algebraic geometry**, the analogue of continuous map is a **morphism of schemes** — a continuous map of underlying topological spaces (in the Zariski topology) together with a compatible morphism of sheaves of rings. The condition is the same shape: preimage of open is open, plus algebraic data. The unified frame "continuity = preimage-of-open-is-open" extends from analysis to algebraic geometry without modification.

In **measure theory**, the analogue is a **measurable map** — $f : (X, \mathcal{A}) \to (Y, \mathcal{B})$ between measurable spaces such that $f^{-1}(B) \in \mathcal{A}$ for every $B \in \mathcal{B}$. The structural definition is identical to continuity, only with σ-algebras in place of topologies. A continuous map between topological spaces is automatically Borel-measurable — preimage-of-open is open, hence Borel.

---

# Examples / Corollaries

**Is an instance — the identity map $\text{id}_X : X \to X$.** $\text{id}_X^{-1}(U) = U$, which is open whenever $U$ is open. So the identity is continuous (in any topology).

**Is an instance — a constant map.** Take $f : X \to Y$ with $f(x) = c$ for all $x$. Then $f^{-1}(U) = X$ if $c \in U$, and $f^{-1}(U) = \emptyset$ otherwise. Both $X$ and $\emptyset$ are open. So constant maps are continuous, regardless of the topologies involved.

**Is an instance — the composition of two continuous maps.** If $f : X \to Y$ and $g : Y \to Z$ are continuous, then $(g \circ f)^{-1}(U) = f^{-1}(g^{-1}(U))$. If $U$ is open in $Z$, $g^{-1}(U)$ is open in $Y$ (by continuity of $g$), and $f^{-1}(g^{-1}(U))$ is open in $X$ (by continuity of $f$). So $g \circ f$ is continuous.

**Is an instance — $f : \mathbb{R} \to \mathbb{R}, f(x) = x^2$.** The preimage of an open interval $(a, b)$ is computable directly: if $a \geq 0$ and $b > 0$, then $f^{-1}((a, b)) = (-\sqrt{b}, -\sqrt{a}) \cup (\sqrt{a}, \sqrt{b})$ (or just the right-hand union if $a < 0$), which is open. If $a < 0$, $f^{-1}((a, b)) = (-\sqrt{b}, \sqrt{b})$, also open. So $f$ is continuous. Note that $f$ is *not* an open map: $f((-1, 1)) = [0, 1)$, not open. This illustrates that continuous and open are independent properties.

**Is an instance — every function from a discrete topological space.** If $X$ has the discrete topology, then every subset of $X$ is open. So $f^{-1}(U) \subseteq X$ is *automatically* open, regardless of what $U$ is or whether $f$ has any structure. Therefore *every* function out of a discrete space is continuous. This is the most permissive source topology.

**Is an instance — every function into an indiscrete space.** If $Y$ has the indiscrete topology $\{\emptyset, Y\}$, then $f^{-1}(\emptyset) = \emptyset$ and $f^{-1}(Y) = X$, both open. So *every* function into an indiscrete space is continuous. This is the most permissive target topology.

**Is NOT an instance — the identity from the standard topology to the discrete topology on $\mathbb{R}$.** The map $\text{id} : \mathbb{R}_\text{std} \to \mathbb{R}_\text{discrete}$. The set $\{0\}$ is open in $\mathbb{R}_\text{discrete}$. Its preimage is $\{0\}$, which is *not* open in $\mathbb{R}_\text{std}$. So this map is not continuous, even though it is the identity function. This shows that continuity depends genuinely on the topologies, not just on the function.

**Is NOT an instance — the floor function $\lfloor \cdot \rfloor : \mathbb{R} \to \mathbb{R}$ (both with the standard topology).** Take $U = (-0.5, 0.5)$, which is open. The preimage $\lfloor \cdot \rfloor^{-1}(U) = \{x : \lfloor x \rfloor = 0\} = [0, 1)$, which is *not* open (the point $0$ is in the set but every ball about $0$ contains negative numbers, which map to $\lfloor \cdot \rfloor = -1 \notin U$). So the floor function is not continuous. It is, however, continuous *at* every non-integer point — the discontinuity is concentrated on the integers.

**Open ≠ Continuous — the squaring map again.** $f(x) = x^2$ is continuous but not open: $f((-1, 1)) = [0, 1)$ is not open. Conversely, the projection $\pi : \mathbb{R}^2 \to \mathbb{R}, \pi(x, y) = x$ is *both* continuous and open: it is continuous because $\pi^{-1}((a, b)) = (a, b) \times \mathbb{R}$, an open strip; and it is open because the image of an open box $(a, b) \times (c, d)$ is the open interval $(a, b)$, and arbitrary unions of open boxes (which form a basis) map to arbitrary unions of open intervals. Open and continuous are independent, and a map can be neither, one, or both.

**Corollary — continuity is preserved by composition.** Composition of continuous maps is continuous; the identity is continuous. So topological spaces and continuous maps form a category.

**Corollary — continuity is preserved by restriction.** If $f : X \to Y$ is continuous and $A \subseteq X$ has the subspace topology, then $f|_A : A \to Y$ is continuous (preimage of open in $Y$ under the restriction is open in $A$, because it is the intersection of $A$ with the preimage in $X$).

**Corollary — continuity is preserved by corestriction to a subspace containing the image.** If $f : X \to Y$ is continuous and $f(X) \subseteq Z \subseteq Y$, then the map $\tilde f : X \to Z$ (same values, smaller codomain) is continuous when $Z$ has the subspace topology. This is the universal property of the subspace topology.

**Corollary — preimage commutes with intersection and complement.** $f^{-1}(A \cap B) = f^{-1}(A) \cap f^{-1}(B)$, $f^{-1}(Y \setminus A) = X \setminus f^{-1}(A)$, $f^{-1}(\bigcup_\alpha A_\alpha) = \bigcup_\alpha f^{-1}(A_\alpha)$. This is what makes the preimage formulation of continuity respect the topology axioms; image does not have these properties.

**Calibration check.** Verify that the absolute value function $|\cdot| : \mathbb{R} \to \mathbb{R}$ is continuous by computing the preimage of $(a, b)$ for various ranges of $a, b$. Verify that addition $+ : \mathbb{R}^2 \to \mathbb{R}, (x, y) \mapsto x + y$ is continuous by computing $+^{-1}((a, b)) = \{(x, y) : a < x + y < b\}$, which is the strip between two parallel lines, hence open. Verify that the floor function $\lfloor \cdot \rfloor : \mathbb{R} \to \mathbb{R}$ is discontinuous at $0$ but continuous at $0.5$. If you can also explain why the image-of-open-is-open formulation would make constant maps non-continuous, you have understood every clause.

---

# Unlocked by This

> [!tip] **Homeomorphism** *(from this topic)*
> A continuous bijection with continuous inverse — the "isomorphism" in $\mathsf{Top}$. Two spaces are homeomorphic if they cannot be distinguished by any topological property. See [[Def - Homeomorphism]].

> [!tip] **Continuity via Bases** *(from this topic)*
> $f$ is continuous if and only if $f^{-1}(B)$ is open for every $B$ in some basis (or subbasis) of $Y$. See [[Def - Basis and Subbasis for a Topology]]. This is the standard practical tool for verifying continuity — one rarely checks every open set; one checks a generating family.

> [!tip] **Universal Properties of Subspace, Product, Quotient** *(from this topic)*
> The subspace, product, and quotient topologies are each characterized by a universal property phrased in terms of continuous maps: a continuous map into a subspace $Y \subseteq X$ is a continuous map into $X$ that lands in $Y$; a continuous map into a product $\prod Y_\alpha$ is a continuous map into each factor; a continuous map out of a quotient $X/{\sim}$ is a continuous map out of $X$ that is constant on equivalence classes.

> [!tip] **Pasting Lemma** *(from this topic)*
> Continuous functions defined on closed (or open) pieces of a finite cover can be pasted together if they agree on overlaps, and the result is continuous on the union.

> [!tip] **Bounded Linear Maps** *(from Functional Analysis)*
> A linear map $T : V \to W$ between Banach spaces is continuous if and only if it is **bounded**: $\lVert Tv \rVert \leq M \lVert v \rVert$ for some $M$. Continuity of linear maps reduces to a single norm estimate, by linearity.

> [!tip] **Holomorphic / Smooth Maps** *(from Complex / Differential Geometry)*
> Holomorphic maps between complex manifolds, and smooth maps between smooth manifolds, are continuous as a special case. The topological notion of continuity is what makes the analytic and differentiable notions well-defined on charts.

> [!tip] **Measurable Maps** *(from Measure Theory)*
> A continuous map between topological spaces is **Borel-measurable**: $f^{-1}(\text{Borel}) \subseteq \text{Borel}$. The structural definition of measurable map ($f^{-1}(\mathcal{B}_Y) \subseteq \mathcal{A}_X$) is identical in shape to continuity, with σ-algebras in place of topologies.
