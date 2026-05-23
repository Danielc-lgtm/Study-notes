---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Vector Bundle"
tags: [geometry, algebraic-topology, fibre-bundles]
---

# Notation

$E$, $B$ are topological spaces, $\pi : E \to B$ is a continuous (surjective) map. $F = \pi^{-1}(b_0)$ is the **fibre** over a point $b_0 \in B$. $W$ is an arbitrary "test" space. A **homotopy** is a map $H : W \times [0, 1] \to B$; a **lift** of $H$ through $\pi$ is a map $\tilde H : W \times [0, 1] \to E$ with $\pi \circ \tilde H = H$. The notation $F \hookrightarrow E \xrightarrow{\pi} B$ denotes a fibration with fibre $F$, total space $E$, base $B$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The motivating question is: *what is the right generalisation of "covering space" that supports a homotopy long exact sequence?* Covering spaces have discrete fibres and a strict path-lifting property — every path in the base lifts uniquely to a path in the total space, given a starting point. This gives the [[Algebraic Topology II — Fundamental Group and Covering Spaces|Galois correspondence]] between subgroups of $\pi_1(B)$ and connected covers, and it produces the short exact sequence $1 \to \pi_1(\tilde X) \to \pi_1(X) \to G \to 1$ for a regular cover.

We want a generalisation that allows the fibre $F$ to be non-discrete — a vector space, a Lie group, a manifold — while still supporting path lifting up to homotopy. The basic example to keep in mind is the **vector bundle**: $\pi : E \to B$ is locally a product $U \times \mathbb{R}^n \to U$, and the fibre $\mathbb{R}^n$ is a vector space, not a discrete set. Locally a bundle looks like a product, but globally it can twist (as the Möbius band twists $\mathbb{R}$ over $S^1$). The right axiom for "supports a homotopy long exact sequence" turns out to be the **homotopy lifting property** (HLP) — a homotopy lifting condition that is *generic*, not specific to the fibre type.

The homotopy lifting property says: given a homotopy $H : W \times [0, 1] \to B$ of the base, and a lift $\tilde h : W \to E$ of $h = H(\cdot, 0)$, we can extend $\tilde h$ to a lift $\tilde H : W \times [0, 1] \to E$ of the whole homotopy. Pictorially:

$$
\begin{array}{ccc}
W & \xrightarrow{\tilde h} & E \\
\downarrow i_0 & & \downarrow \pi \\
W \times [0, 1] & \xrightarrow{H} & B
\end{array}
$$

The HLP requires the existence of the diagonal arrow $\tilde H : W \times [0, 1] \to E$. This is a single axiom that subsumes path lifting for covering spaces (set $W = \mathrm{pt}$), and it is exactly enough to manufacture the boundary map $\partial : \pi_k(B) \to \pi_{k-1}(F)$ in the long exact sequence.

Why is this the right axiom? Consider the construction of $\partial$. Given a class in $\pi_k(B)$, represented by $f : S^k \to B$, we can think of $f$ as a homotopy: $S^k = I^k / \partial I^k$, and the inclusion $I^{k-1} \times \{0\} \hookrightarrow I^k$ gives a "starting position" for the homotopy. The HLP says we can lift this homotopy to $E$, starting from a lift of the constant map (the basepoint of $E$). The endpoint of the lifted homotopy is a map $I^{k-1} \to E$ whose boundary lies in the fibre $F = \pi^{-1}(b_0)$ — giving an element of $\pi_{k-1}(F)$. The construction works *because* of HLP, and the well-definedness modulo homotopy uses HLP again at the level of homotopies of homotopies.

If we required only path lifting (homotopy lifting for $W = \mathrm{pt}$), we would not get the boundary map for higher $k$; the construction needs the full homotopy lifting for $W = I^{k-1}$. So the HLP at the level of arbitrary $W$ — or at least for all CW complexes $W$ — is the natural axiom. Hurewicz fibrations are defined by the HLP for *all* spaces $W$; the slightly weaker notion of **Serre fibration** requires HLP only for $W$ a CW complex (or just for $W = D^n$ a disc), and it suffices for most computations. The distinction matters only for technical reasons; in this chapter we use **fibration** to mean either, and all our examples (smooth bundles, principal bundles, vector bundles, the Hopf fibration) satisfy both.

What does this axiom exclude? A map $\pi : E \to B$ failing the HLP can have very different fibre types over different points: e.g., $\pi : \mathbb{R}^2 \to \mathbb{R}$ defined by $(x, y) \mapsto x$ has fibres all $\mathbb{R}$, this is a fibration. But the map $\pi : \mathbb{R}^2 \to \mathbb{R}$ defined by $(x, y) \mapsto xy$ has fibres $\mathbb{R}$ for $y =$ constant nonzero, but over $\{0\}$ the fibre is the union of axes — different topological type. This is *not* a fibration. The HLP is the technical condition that forces fibres to be homotopy-equivalent (as a consequence) and lets the long exact sequence work.

---

# The Definition

A continuous map $\pi : E \to B$ is a **Hurewicz fibration** if it has the **homotopy lifting property** with respect to every space $W$:

> Given any space $W$, any continuous map $\tilde h : W \to E$, and any continuous homotopy $H : W \times [0, 1] \to B$ with $H(\cdot, 0) = \pi \circ \tilde h$, there exists a continuous lift $\tilde H : W \times [0, 1] \to E$ with $\tilde H(\cdot, 0) = \tilde h$ and $\pi \circ \tilde H = H$.

If $B$ is path-connected, the **fibre** $F = \pi^{-1}(b_0)$ is well-defined up to homotopy equivalence (independent of $b_0$).

A map $\pi : E \to B$ is a **Serre fibration** if the HLP holds with respect to every CW complex $W$ (equivalently, every $W = D^n$ a disc). Every Hurewicz fibration is a Serre fibration; the converse fails in general but rarely matters in practice.

Standard notation: $F \hookrightarrow E \xrightarrow{\pi} B$ for a fibration with fibre $F$, total space $E$, base $B$.

**Examples of fibrations:**

- **Every fibre bundle** $\pi : E \to B$ (in particular every smooth principal or vector bundle) is a Hurewicz fibration. The HLP follows from local triviality and partitions of unity.
- **The trivial fibration** $\pi : B \times F \to B$, projection.
- **The path-loop fibration** $\Omega X \hookrightarrow PX \to X$, where $PX$ is the path space (paths starting at the basepoint) and $\Omega X$ is the loop space; $\pi$ is "evaluate at the endpoint".
- **Covering spaces** (special case where $F$ is discrete).

---

# Categorical / Structural Definition

In the **model category** language of homotopy theory, fibrations are one of three classes of distinguished morphisms (fibrations, cofibrations, weak equivalences) satisfying lifting axioms. The Hurewicz HLP is exactly the **right lifting property** of $\pi : E \to B$ against the inclusion $i_0 : W \hookrightarrow W \times [0, 1]$ for every space $W$:

$$
\begin{array}{ccc}
W & \to & E \\
\downarrow i_0 & \nearrow & \downarrow \pi \\
W \times [0, 1] & \to & B
\end{array}
$$

In the Quillen model structure on topological spaces, this characterises Hurewicz fibrations. Serre fibrations are characterised by the right lifting property against $i_0 : D^n \hookrightarrow D^n \times [0, 1]$ for every $n$.

The categorical content is that fibrations and cofibrations are *duals*: a fibration is "surjective on homotopy fibres" in a strong sense, and a cofibration is "injective on homotopy cofibres". The classes are interchanged by the duality $X \leftrightarrow \mathrm{Map}(X, ?)$, which sends spaces to function spaces.

A more refined notion is the **homotopy fibre** of an arbitrary map $f : X \to Y$: it is the pullback in homotopy of $X \to Y \leftarrow \mathrm{pt}$, computed as $X \times_Y PY$ where $PY$ is the path space. Every map has a homotopy fibre, and the long exact sequence of a fibration generalises to the **Puppe sequence** for arbitrary maps, with the homotopy fibre replacing the strict fibre.

---

# Relate to Other Fields / Compression

**True name:** a fibration is **a map whose lifts behave like the projection of a product bundle, up to homotopy**. The homotopy lifting property is the precise statement of "behaves like a projection" — paths and higher homotopies in the base can be lifted to the total space, with the lifts depending continuously on the starting position.

In **differential geometry**, every smooth [[Def - Vector Bundle|vector bundle]] and every smooth [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet|principal bundle]] is a fibration in the topological sense. The smooth structure gives more: connections, curvature, characteristic classes. But the *topological* notion of fibration captures the bare minimum needed for homotopy-theoretic computation.

In **homological algebra**, fibrations are the analogues of **surjective maps of chain complexes**. The long exact sequence of a fibration is the analogue of the long exact sequence in homology associated to a short exact sequence of chain complexes; both come from the same source — a "boundary map" between consecutive levels.

In **algebraic geometry**, the analogue is the **flat morphism** of schemes, and the analogue of the long exact sequence is the **Leray spectral sequence** for the higher direct images $R^q f_*$ of a sheaf along the fibration $f$. The strict Hurewicz HLP becomes flat descent.

In **physics**, fibrations are the geometric setting of **gauge theory**: the principal bundle is the fibration of frames, the connection is a horizontal distribution in the total space, the gauge group acts on the fibres. The Hopf bundle's HLP is what allows path-dependent phases (holonomies) to be computed by lifting paths from the base $S^2$ to the total space $S^3$.

---

# Examples / Corollaries

**Example: the Hopf fibration.** $S^1 \hookrightarrow S^3 \xrightarrow{\eta} S^2$ is a smooth principal $U(1)$-bundle, hence a Hurewicz fibration. See [[Def - The Hopf Map]] for details.

**Example: principal $G$-bundles.** Any smooth principal $G$-bundle $G \hookrightarrow P \xrightarrow{\pi} M$ is a fibration; the HLP follows from the local triviality $\pi^{-1}(U) \cong U \times G$ and partition-of-unity arguments. The fibre is $G$ itself.

**Example: vector bundles.** A rank-$n$ real or complex vector bundle $\mathbb{R}^n \hookrightarrow E \to B$ (resp. $\mathbb{C}^n$) is a Hurewicz fibration. Note: the fibre $\mathbb{R}^n$ is contractible, so the long exact sequence collapses: $\pi_k(E) \cong \pi_k(B)$ for all $k$. Vector bundles have the same homotopy as their bases.

**Example: $SU(n - 1) \hookrightarrow SU(n) \to S^{2n-1}$.** The unitary group $SU(n)$ acts transitively on the unit sphere $S^{2n-1} \subset \mathbb{C}^n$ (any unit vector can be sent to any other by a unitary), and the stabiliser of a basepoint is $SU(n-1)$. So $SU(n) \to S^{2n-1}$ is the quotient by $SU(n-1)$, exhibiting $SU(n)$ as the total space of a principal $SU(n-1)$-bundle over $S^{2n-1}$. The long exact sequence gives a recursive computation of $\pi_k(SU(n))$ in terms of $\pi_k$ of spheres.

**Example: path-loop fibration.** For a pointed space $(X, x_0)$, let $PX = \{\gamma : [0, 1] \to X : \gamma(0) = x_0\}$ be the **path space** (paths starting at $x_0$), and $\Omega X = \{\gamma : [0, 1] \to X : \gamma(0) = \gamma(1) = x_0\}$ the **loop space**. The evaluation map $\pi : PX \to X$ defined by $\pi(\gamma) = \gamma(1)$ is a Hurewicz fibration with fibre $\Omega X$. So we have

$$\Omega X \hookrightarrow PX \xrightarrow{\mathrm{ev}_1} X.$$

The path space $PX$ is contractible (paths can be shrunk to the constant path by reparametrisation), so the long exact sequence gives $\pi_k(X) \cong \pi_{k-1}(\Omega X)$ for all $k \geq 1$. This is the **loop-space adjunction**, and iterating gives $\pi_k(X) = \pi_0(\Omega^k X)$.

**Example: covering spaces.** $\pi : \tilde X \to X$ a covering with fibre $F$ (a discrete set with the action of $\pi_1(X)$). Path lifting is the classical lifting property; the HLP follows from the local triviality $\pi^{-1}(U) = U \times F$. The long exact sequence collapses to short exact $1 \to \pi_1(\tilde X) \to \pi_1(X) \to F \to 1$ (with $\pi_k(\tilde X) = \pi_k(X)$ for $k \geq 2$, see [[Algebraic Topology II — Fundamental Group and Covering Spaces]]).

**Is NOT an instance: the projection $\pi : \mathbb{R}^2 \to \mathbb{R}$, $(x, y) \mapsto xy$.** The fibre over $0$ is the union of axes (not contractible), while the fibre over $1$ is the hyperbola $xy = 1$ (two components, each contractible). The fibres are not even homotopy-equivalent, so this cannot be a fibration. The HLP fails: there are homotopies in the base near $0$ that cannot be lifted.

**Is NOT an instance: a map that is surjective with non-empty fibres but lacks lifting.** For instance the doubling map $z \mapsto z^2$ on the unit disc $\{|z| \leq 1\} \to \{|z| \leq 1\}$ is surjective but not a fibration (fibres have one or two points depending on whether $z = 0$); the map fails HLP because lifts are not unique.

**Corollary: fibres of a fibration are homotopy-equivalent.** If $\pi : E \to B$ is a Hurewicz fibration with $B$ path-connected, then for any $b_0, b_1 \in B$, the fibres $\pi^{-1}(b_0)$ and $\pi^{-1}(b_1)$ are homotopy-equivalent. The equivalence is constructed by choosing a path from $b_0$ to $b_1$ and lifting it; the HLP gives a continuous family of homotopy equivalences parametrised by paths.

**Corollary: the long exact sequence of a fibration.** $F \hookrightarrow E \xrightarrow{\pi} B$ gives $\cdots \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \to \pi_{k-1}(F) \to \cdots$. See [[Thm - Long Exact Sequence of a Fibration]].

**Calibration check.** If you understand the definition you should be able to: (i) verify that a trivial bundle $B \times F \to B$ satisfies HLP directly; (ii) explain why a vector bundle has the same higher homotopy as its base; (iii) explain why the path-loop fibration produces the loop-space adjunction $\pi_k(X) = \pi_{k-1}(\Omega X)$.

---

# Unlocked by This

> [!tip] Serre Spectral Sequence *(from Homological Algebra)*
> The long exact sequence of a fibration is the bottom row of a much richer apparatus: the **Serre spectral sequence**, which relates $H_*(F)$, $H_*(B)$, and $H_*(E)$ via the $E^2$-page $E^2_{p, q} = H_p(B; H_q(F))$, converging to $H_{p+q}(E)$. The spectral sequence collapses for fibrations with simply connected base and constant local coefficients, giving the Künneth-type formula. It is the standard tool for computing homology of fibre bundles and is the engine behind many characteristic-class computations: $H^*(BU(n))$ is computed as the cohomology of the bar-construction $EU(n) \to BU(n)$ via Serre, yielding the polynomial ring $\mathbb{Z}[c_1, \ldots, c_n]$ of universal Chern classes.

> [!tip] Postnikov Towers *(from Homotopy Theory)*
> Every connected space $X$ has a **Postnikov tower**: a sequence of fibrations
> $$\cdots \to X[2] \to X[1] \to X[0] = \mathrm{pt}$$
> with $X[n]$ having homotopy concentrated in degrees $\leq n$ ($\pi_k(X[n]) = \pi_k(X)$ for $k \leq n$, zero otherwise), and the fibre $K(\pi_{n+1}, n+1)$ of $X[n+1] \to X[n]$ being an Eilenberg–MacLane space. The gluing data — the **$k$-invariants** — completely determine the homotopy type of $X$. Postnikov towers are the systematic way to build complicated spaces out of Eilenberg–MacLane pieces, layer by layer of homotopy.
