---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
tags: [analysis, topology, quotient]
---

# Notation

$X, Y, Z$ are topological spaces. $f : X \to Y$ is a surjection. $\sim$ is an equivalence relation on $X$, $X/{\sim}$ is the set of equivalence classes, $[x]$ is the class of $x$, and $\pi : X \to X/{\sim}$ is the canonical projection $x \mapsto [x]$. If $A \subseteq X$, then $X/A$ denotes the quotient by the relation whose nontrivial class is $A$ (everything in $A$ becomes one point, every point outside $A$ stays itself). The full registry is on [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Baire]].

---

# Axiom Motivation

We want a clean way to *paste* a topological space onto itself — to glue the two ends of a strip into a cylinder, to identify antipodes on a sphere, to fold the boundary of a disk to a point. The set-level operation is unambiguous: form the set of equivalence classes $X/{\sim}$. The question is which topology to put on it, and the answer is forced by a single requirement: the canonical projection $\pi : X \to X/{\sim}$ must be continuous, and we should not impose more openness than this forces.

Why "no more openness than forced"? Because the entire purpose of the quotient is to *forget* distinctions — to declare $a$ and $b$ the same point. Adding open sets would let the quotient detect distinctions $X$ itself does not, and one can readily check that any extra open set in the target pulls back to a non-saturated open set in $X$ — a set not closed under $\sim$ — which has no honest meaning at the level of equivalence classes. So we take the *largest* topology on $X/{\sim}$ making $\pi$ continuous. Concretely: $V \subseteq X/{\sim}$ is declared open iff $\pi^{-1}(V) \subseteq X$ is open. This is the **quotient topology**.

The choice is universal: any *finer* topology breaks continuity of $\pi$; any *coarser* one wastes information. The same definition applies to an arbitrary surjection $f : X \to Y$, not only to projections from equivalence relations — declare $V \subseteq Y$ open iff $f^{-1}(V) \subseteq X$ is open. A surjection equipped with this topology on its target is an **identification map**. The two viewpoints are essentially equivalent: every quotient by an equivalence relation is an identification map, and every identification map is a quotient by the relation $x \sim x' \iff f(x) = f(x')$.

If we *weaken* the definition — say, ask only that $\pi$ be continuous and accept some smaller topology — we lose the universal property: a function on the quotient that "ought to" be continuous (because its pullback to $X$ is) might fail to be. If we *strengthen* it — ask that $\pi$ also be open or closed — we exclude most natural examples; the projection $\mathbb{R} \to \mathbb{R}/\mathbb{Q}$ is not open. So "finest topology making $\pi$ continuous" is the unique sweet spot.

---

# The Definition

**Quotient topology.** Let $X$ be a topological space, $Y$ a set, $f : X \to Y$ a surjection. The **quotient topology** on $Y$ induced by $f$ is
$$\tau_f = \{V \subseteq Y : f^{-1}(V) \text{ is open in } X\}.$$
This is the largest (finest) topology on $Y$ making $f$ continuous.

**Identification map.** A surjection $f : X \to Y$ is an **identification map** (or **quotient map**) if $Y$ carries the quotient topology induced by $f$. Equivalently: $V \subseteq Y$ is open if and only if $f^{-1}(V)$ is open.

**Quotient space.** Given an equivalence relation $\sim$ on $X$, the **quotient space** $X/{\sim}$ is the set of equivalence classes equipped with the quotient topology induced by the canonical projection $\pi : X \to X/{\sim}$, $x \mapsto [x]$.

**Collapsing a subspace.** For $A \subseteq X$, $X/A$ denotes the quotient by the equivalence relation whose classes are $A$ and the singletons $\{x\}$ for $x \notin A$. Geometrically: $A$ is crushed to a single point.

---

# Relate to Other Fields / Compression

The quotient topology is the **coequalizer** in the category of topological spaces: it is the universal target for a map out of $X$ that identifies the equivalence classes. Dual to it is the **subspace topology**, which is the universal source mapping into $X$ (an equalizer). The pair (subspace, quotient) is the topological mirror of (subset, quotient set) in plain set theory, with the universal property selecting the canonical topology in each case. In algebraic terms, the projection $\pi$ is an epimorphism, and the quotient topology is the colimit of the diagram defining $\sim$.

In differential geometry, the quotient $G/H$ of a Lie group by a closed subgroup carries simultaneously a quotient topology *and* a smooth manifold structure — both inherited from $G$ by the same universal-property mechanism.

---

# Examples and Corollaries

**Is an instance — the circle as quotient.** Take $X = [0, 1]$ with the relation $0 \sim 1$. The quotient $[0, 1]/(0 \sim 1)$ is homeomorphic to $S^1$. Proof: the map $t \mapsto e^{2\pi i t}$ is continuous and constant on the equivalence class, hence descends; it is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism by [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]].

**Is an instance — $X/A$ collapsing a closed subspace.** $D^n / S^{n-1} \cong S^n$ collapses the boundary of the disk to a point. This is [[Thm - The Sphere as Quotient of the Disk]] and is the prototype "build a higher sphere from a lower disk".

**Is NOT an instance of a Hausdorff space — $\mathbb{R}/\mathbb{Q}$.** The equivalence $x \sim y \iff x - y \in \mathbb{Q}$ has uncountably many classes but every nonempty open set in the quotient pulls back to a $\mathbb{Q}$-saturated open in $\mathbb{R}$, which is all of $\mathbb{R}$. So the only opens in the quotient are $\emptyset$ and the whole space — the indiscrete topology. See [[Ex - A quotient with trivial topology]]. A reminder that quotients can be wildly non-Hausdorff even when $X$ is excellent.

**Corollary — a quotient of a compact space is compact.** $\pi$ is continuous and surjective, so $X/{\sim} = \pi(X)$ is the continuous image of a compact space, hence compact by [[Thm - Continuous Image of a Compact Space]].

**Corollary — a quotient of a connected space is connected.** Same reasoning with the continuous image of a connected space.

**Corollary — the projection is rarely open.** In $\mathbb{R} \to \mathbb{R}/\mathbb{Z}$, the open set $(-0.1, 0.1)$ in $\mathbb{R}$ projects to an open in $S^1$ (a neighborhood of $0$). But the open $(0.1, 0.3)$ projects to a set whose preimage is $\bigcup_n (n + 0.1, n + 0.3)$, also open — so this particular projection *is* open. In general, $\pi$ is open iff every open set is "saturated up" to an open set, which is a strong restriction.

**Calibration check.** Verify $[0, 1]/\{0, 1\}$ is $S^1$ (collapse two endpoints to one point), check that $S^2 / \{\pm x\} = \mathbb{R}P^2$ is Hausdorff (using Proposition 13.8: $X$ regular and $A$ closed gives $X/A$ Hausdorff), and verify that $\mathbb{R}^2 / \mathbb{Z}^2$ (treating $\mathbb{Z}^2$ as the equivalence relation $(x,y) \sim (u,w) \iff x - u, y - w \in \mathbb{Z}$) is the torus $S^1 \times S^1$. If all three check out via the universal property plus compact-to-Hausdorff upgrade, the definition is understood.

---

# Unlocked by This

> [!tip] CW Complex *(from Algebraic Topology)*
> A **CW complex** is built by inductively attaching $n$-cells (copies of $D^n$) to a lower-dimensional skeleton via maps $S^{n-1} \to X^{(n-1)}$ on the boundary. Each attachment is the [[Def - Adjunction Space|adjunction space]] $X^{(n-1)} \cup_{\partial} D^n$, which is itself a quotient. Every reasonable space in algebraic topology — spheres, projective spaces, Grassmannians, mapping cylinders, classifying spaces — is built this way.

> [!tip] Coequalizer *(from Category Theory)*
> In any category with a notion of "quotient", the **coequalizer** of two parallel arrows $f, g : A \to B$ is the universal object equipped with a map $B \to C$ such that $C \circ f = C \circ g$. The quotient topology realizes this in $\mathbf{Top}$: $X/{\sim}$ is the coequalizer of the two projections $R \rightrightarrows X$ where $R \subseteq X \times X$ is the relation. This unifies group quotients, ring quotients, and topological quotients under one categorical name.
