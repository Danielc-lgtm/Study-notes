---
type: definition
subject: topology
prereqs:
  - "Def - Continuous Map"
  - "Def - Product Topology"
tags: [analysis, topology, homotopy]
---

# Notation

$X, Y$ are topological spaces, $f, g : X \to Y$ continuous maps. $I = [0, 1]$ with its standard topology. A homotopy is a continuous map $F : X \times I \to Y$, with $X \times I$ carrying the product topology. We write $f_t(x) := F(x, t)$ for the $t$-slice. Homotopy is denoted $f \simeq g$; relative homotopy fixing $A \subseteq X$ is $f \simeq g$ **rel** $A$. The set of homotopy classes of maps $X \to Y$ is $[X, Y]$. Concatenation is $F * G$, inversion is $F^{-1}$. The full registry is on the topic page.

---

# Axiom Motivation

Geometric topology starts with the realization that two maps $f, g : X \to Y$ that *look* the same — that can be continuously deformed into one another — should be treated as equivalent for most topological purposes. Counting holes, classifying loops, detecting linking — none of these distinguish between maps that differ by a continuous wiggle. The right equivalence relation is **homotopy**: $f$ and $g$ are equivalent if there is a continuous one-parameter family of maps interpolating between them, parametrized by $t \in I$. The slices $f_0 = f$ and $f_1 = g$ are the endpoints; the intermediate slices $f_t$ are the deformation in progress.

Why parametrize by $[0, 1]$ specifically? Because we need a connected, ordered domain to give meaning to "start", "end", and "in-between", and $[0, 1]$ is the canonical such object — connected, compact, with two distinguished endpoints. Any homeomorphic interval works, but $I$ is the standard choice.

Why insist on *joint* continuity in $(x, t)$ rather than just separate continuity in each variable? Because separate continuity is far too weak: we need the map $F$ to be continuous as a function on $X \times I$, not just continuous in $x$ for each $t$ and in $t$ for each $x$. The product topology is the right notion: a basis of open sets is $U \times V$ for $U$ open in $X$, $V$ open in $I$. Joint continuity says the family deforms uniformly — small changes in $x$ and $t$ both give small changes in $f_t(x)$.

What about *relative* homotopies fixing a subset $A$? When studying maps that send a basepoint $x_0$ to $y_0$ (or that fix more general subspaces), one wants the homotopy to preserve this. A homotopy rel $A$ is one with $F(a, t) = F(a, 0)$ for all $a \in A$ and $t \in I$ — the values on $A$ are constant throughout the deformation. This is essential for the fundamental group, where loops at $x_0$ must remain loops at $x_0$ throughout the homotopy.

The strength of "is there a homotopy" as an equivalence relation: it is *coarser* than equality of maps but still records meaningful topological information. The "shape" of $X$ (counted by fundamental groups, homology, K-theory) is exactly what survives under homotopy. Anything finer is lost; anything coarser would identify too much.

---

# The Definition

**Homotopy.** Let $X, Y$ be topological spaces and $f_0, f_1 : X \to Y$ continuous maps. A **homotopy** from $f_0$ to $f_1$ is a continuous map
$$F : X \times I \to Y$$
such that $F(x, 0) = f_0(x)$ and $F(x, 1) = f_1(x)$ for all $x \in X$. The maps $f_0, f_1$ are then **homotopic**, written $f_0 \simeq f_1$. We denote the $t$-slice by $f_t(x) = F(x, t)$.

**Relative homotopy.** Let $A \subseteq X$. A homotopy $F : X \times I \to Y$ is a **homotopy rel $A$** if $F(a, t) = F(a, 0)$ for every $a \in A$ and every $t \in I$. We write $f_0 \simeq f_1$ rel $A$.

**Homotopy classes.** The relation $f \simeq g$ is an equivalence relation on $C(X, Y)$, the set of continuous maps $X \to Y$. The set of equivalence classes is denoted $[X, Y]$ — the **homotopy classes** of maps $X \to Y$.

**Concatenation.** Given homotopies $F : X \times I \to Y$ and $G : X \times I \to Y$ with $F(x, 1) = G(x, 0)$, the **concatenation** is
$$(F * G)(x, t) = \begin{cases} F(x, 2t) & 0 \leq t \leq 1/2 \\ G(x, 2t - 1) & 1/2 \leq t \leq 1 \end{cases}$$
which runs $F$ at double speed on $[0, 1/2]$ then $G$ at double speed on $[1/2, 1]$. The pasting lemma guarantees joint continuity.

**Inverse.** The **inverse** of $F$ is $F^{-1}(x, t) := F(x, 1 - t)$, running the homotopy in reverse.

**Constant homotopy.** A homotopy $F$ is **constant** (or **trivial**) if $F(x, t) = F(x, 0)$ for all $t$ — the map $f_0$ deformed by no deformation.

---

# Relate to Other Fields / Compression

Homotopy is the **equivalence relation of the homotopy category** $\mathbf{Ho}(\mathbf{Top})$: the category obtained from $\mathbf{Top}$ by formally identifying homotopic maps. Most algebraic invariants of topology (fundamental group, homology, cohomology, K-theory) factor through this quotient — they are functors $\mathbf{Ho}(\mathbf{Top}) \to \mathbf{Grp}$ (or $\mathbf{Ab}$), so they cannot distinguish homotopic maps. Conversely, finding new homotopy invariants is the central programme of algebraic topology.

In differential topology, the smooth analogue is **smooth homotopy** (a $C^\infty$ map $F : X \times I \to Y$), and the Whitney approximation theorem says: every continuous homotopy can be approximated by a smooth one. So $[X, Y]_{C^\infty} = [X, Y]$ for smooth manifolds.

In algebra, homotopy of chain complexes is the analogous equivalence relation: two chain maps are chain-homotopic if they differ by a boundary in the mapping complex. This is the algebraic shadow of the topological notion and the foundation of derived categories.

---

# Examples and Corollaries

**Is an instance — straight-line homotopy in a convex space.** If $Y \subseteq \mathbb{R}^n$ is convex and $f, g : X \to Y$ are continuous, then $F(x, t) = (1-t)f(x) + tg(x)$ is a homotopy from $f$ to $g$. Continuity follows from continuity of $f, g$ and joint continuity of scalar multiplication and addition. *Any two maps into a convex set are homotopic.*

**Is an instance — the contraction of $\mathbb{R}^n$.** The identity $1_{\mathbb{R}^n}$ and the constant map $c_0$ are homotopic via $F(x, t) = (1-t)x$. This is [[Ex - Rn is contractible]].

**Is NOT an instance — distinct degrees on the circle.** The map $z \mapsto z$ on $S^1$ and the map $z \mapsto z^2$ are *not* homotopic, because they have different *winding numbers* (degrees) — $1$ and $2$. The space of maps $S^1 \to S^1$ is partitioned into homotopy classes indexed by $\mathbb{Z}$, with $[S^1, S^1] = \mathbb{Z}$. This is the source of $\pi_1(S^1) = \mathbb{Z}$.

**Corollary — composition respects homotopy.** If $f_0 \simeq f_1 : X \to Y$ via $F$, and $g_0 \simeq g_1 : Y \to Z$ via $G$, then $g_0 \circ f_0 \simeq g_1 \circ f_1$ via $(x, t) \mapsto G(F(x, t), t)$. This is what makes the homotopy category well-defined: composition of homotopy classes is well-defined.

**Corollary — homotopy is an equivalence relation.** Reflexivity (constant homotopy from $f$ to itself), symmetry (inversion $F^{-1}$), transitivity (concatenation $F * G$). Joint continuity at $t = 1/2$ in the concatenation uses the pasting lemma — both pieces agree at the boundary.

**Corollary — every map to a contractible space is null-homotopic.** If $Y$ is contractible (homotopy equivalent to a point), then every $f : X \to Y$ is homotopic to a constant. Compose $f$ with the contraction homotopy on $Y$.

**Calibration check.** Verify: any two maps from a connected space to a discrete space are homotopic iff they are equal (homotopies cannot jump discrete components). Verify: the loops $\gamma(t) = (\cos 2\pi t, \sin 2\pi t)$ and $\delta(t) = (\cos 4\pi t, \sin 4\pi t)$ on $S^1$ are not homotopic, but $\gamma$ and $\eta(t) = (\cos 2\pi(1-t), \sin 2\pi(1-t))$ (the same loop traversed backwards) are *also* not homotopic — they have degrees $1$ and $-1$.

---

# Unlocked by This

> [!tip] Fundamental Group *(from Algebraic Topology)*
> The **fundamental group** $\pi_1(X, x_0)$ is the set of homotopy classes (rel endpoints) of loops based at $x_0$, with the group operation given by concatenation. The reparametrization lemma (§14) makes the group axioms work up to homotopy. $\pi_1(S^1) = \mathbb{Z}$ captures winding number and underwrites the Fundamental Theorem of Algebra.

> [!tip] Homotopy Groups *(from Algebraic Topology)*
> Higher homotopy groups $\pi_n(X, x_0) = [(S^n, *), (X, x_0)]$ are sets (groups for $n \geq 1$, abelian for $n \geq 2$) of homotopy classes of based maps from spheres. Computing them is famously hard — $\pi_3(S^2) = \mathbb{Z}$ (the Hopf map) was unexpected at the time, and the stable homotopy groups of spheres are a current research frontier.

> [!tip] Chain Homotopy *(from Homological Algebra)*
> Two chain maps $f, g : C_\bullet \to D_\bullet$ are **chain-homotopic** if there is a degree-$+1$ map $h$ with $\partial h + h \partial = g - f$. Chain-homotopic maps induce the same map on homology — the algebraic counterpart of homotopic continuous maps inducing the same map on $\pi_n$.
