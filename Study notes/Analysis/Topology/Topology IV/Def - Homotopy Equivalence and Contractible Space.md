---
type: definition
subject: topology
prereqs:
  - "Def - Homotopy"
  - "Def - Continuous Map"
tags: [analysis, topology, homotopy]
---

# Notation

$X, Y$ are topological spaces, $f : X \to Y$ a continuous map. The homotopy relation $\simeq$ is on the topic page. $1_X$ is the identity map $X \to X$. $c_{y_0}$ is the constant map $X \to Y$, $x \mapsto y_0$. A "homotopy equivalence" relates *spaces*, written $X \simeq Y$ (caution: Bredon uses $\simeq$ for both homotopy of maps and homotopy equivalence of spaces; context disambiguates). The full registry is on the topic page.

---

# Axiom Motivation

We have defined homotopy of maps: two maps are equivalent if one can be continuously deformed into the other. The natural next question is: when should we declare two *spaces* equivalent? The naive answer is "when they are homeomorphic". But homeomorphism is much too fine for the purposes of algebraic topology — every nontrivial invariant we want to compute (fundamental group, homology, homotopy groups) is invariant under a coarser equivalence. We need a notion of "same shape" that aggregates homeomorphic spaces but allows additional flexibility: $\mathbb{R}^n$ should have the same shape as a point, since it can be continuously squished onto a point; an annulus should have the same shape as a circle.

The right definition follows the isomorphism pattern from category theory: in any category, two objects are isomorphic if there exist arrows $f : X \to Y$ and $g : Y \to X$ whose compositions are the identities. *In the homotopy category*, "identity" is replaced by "homotopic to the identity". So $f, g$ are **homotopy inverses** if $g \circ f \simeq 1_X$ and $f \circ g \simeq 1_Y$. The maps need not be true inverses — they only need to be inverses up to homotopy. The pair $(f, g)$ certifies that $X$ and $Y$ have the same homotopy type.

A space that is homotopy equivalent to a point is **contractible**. The condition unpacks to: there is a homotopy $H : X \times I \to X$ from $1_X$ to a constant map $c_{x_0}$, called a **contraction**. The space can be continuously collapsed onto a single point. The prototype is $\mathbb{R}^n$, contracted to $0$ by $H(x, t) = (1-t)x$. More generally, any **star-shaped** set with respect to a point $x_0$ — meaning the line segment $\overline{x_0 x}$ lies in the set for every $x$ — is contractible by the same linear-interpolation homotopy.

Why is "homotopy equivalent to a point" a good notion of "trivial topology"? Because the contraction provides a way to push every map $X \to Y$ or $Y \to X$ to a constant, so all homotopy invariants vanish (or become trivial). In particular, $\pi_n(X) = 0$ for all $n$ when $X$ is contractible. The space is invisible to any homotopy-theoretic eye.

The relation between contractibility and the existence of a homotopy $1_X \simeq c_{x_0}$ is captured by Proposition 14.5: $X$ is contractible iff $1_X$ is null-homotopic. The proof unfolds the definition: if $i : \{x_0\} \hookrightarrow X$ and $r : X \to \{x_0\}$ form a homotopy equivalence, then $i \circ r \simeq 1_X$, and $i \circ r = c_{x_0}$, the constant map. Conversely, if $1_X \simeq c_{x_0}$, the pair $(c_{x_0}, i)$ gives the homotopy equivalence.

A subtle but crucial point: homotopy equivalence is much coarser than homeomorphism. The disk $D^n$ is contractible (hence homotopy equivalent to a point) but is not homeomorphic to a point — it has dimension $n$, while a point has dimension $0$. The Möbius strip is homotopy equivalent to a circle (deformation retracts onto its central circle) but is not homeomorphic to one. Every contractible space looks like a point *to homotopy theory*, no matter how complicated it is geometrically.

---

# The Definition

**Homotopy equivalence.** A continuous map $f : X \to Y$ is a **homotopy equivalence** if there exists a continuous map $g : Y \to X$ (a **homotopy inverse**) with
$$g \circ f \simeq 1_X \quad \text{and} \quad f \circ g \simeq 1_Y.$$

**Homotopy equivalent spaces.** Two spaces $X, Y$ are **homotopy equivalent** (have the same **homotopy type**), written $X \simeq Y$, if there exists a homotopy equivalence between them.

**Contractible space.** A space $X$ is **contractible** if it is homotopy equivalent to a one-point space. Equivalently, the identity $1_X : X \to X$ is homotopic to a constant map $c_{x_0}$ for some $x_0 \in X$. The homotopy realizing $1_X \simeq c_{x_0}$ is a **contraction** of $X$ onto $x_0$.

**Null-homotopic map.** A map $f : X \to Y$ is **null-homotopic** if it is homotopic to a constant map. Equivalently, $f$ factors up to homotopy through a point.

---

# Relate to Other Fields / Compression

Homotopy equivalence is the isomorphism relation in the **homotopy category** $\mathbf{Ho}(\mathbf{Top})$ obtained by formally inverting homotopy equivalences (equivalently, by passing to homotopy classes of maps). Two spaces are isomorphic in $\mathbf{Ho}(\mathbf{Top})$ iff they are homotopy equivalent. This is the canonical home for algebraic topology: every homotopy invariant — fundamental group, homology, cohomology, K-theory — is a functor out of $\mathbf{Ho}(\mathbf{Top})$.

In abstract category theory, the analogous notion is **weak equivalence** in a model category. Quillen's axioms abstract the topological setting into a framework where "weak equivalence" plus "fibration" plus "cofibration" determine a well-behaved homotopy theory. The topological case is the prototype.

In algebraic terms, a chain complex is **chain-equivalent** to another if there are chain maps in both directions whose compositions are chain-homotopic to the identities. Two chain-equivalent complexes have the same homology.

---

# Examples and Corollaries

**Is an instance — $\mathbb{R}^n$ is contractible.** Take $H(x, t) = (1-t)x$. At $t = 0$, $H = 1_{\mathbb{R}^n}$; at $t = 1$, $H = c_0$. So $1_{\mathbb{R}^n} \simeq c_0$, and $\mathbb{R}^n$ is contractible. See [[Ex - Rn is contractible]]. The same argument works for any **star-shaped** set with respect to the origin.

**Is an instance — the Möbius strip and the circle.** The Möbius band deformation retracts to its central circle: $H(x, t) = (1 - t) \cdot x + t \cdot p(x)$ where $p$ projects to the central circle. So Möbius $\simeq S^1$. The inclusion of the central circle and the projection back to it are mutually homotopy inverse.

**Is an instance — the mapping cylinder.** For any $f : X \to Y$, the mapping cylinder $M_f$ is homotopy equivalent to $Y$ via the retraction $r : M_f \to Y$ and the inclusion $Y \hookrightarrow M_f$. See [[Thm - Mapping Cylinder is Deformation Retract of Target]].

**Is NOT an instance of homotopy equivalent — $S^n$ and a point.** The sphere $S^n$ for $n \geq 1$ is *not* contractible. Proof requires algebraic topology: $\pi_n(S^n) = \mathbb{Z}$, but $\pi_n(\text{point}) = 0$. This is the first nontriviality result of homotopy theory, and one of the hardest to prove from scratch. (For $n = 1$, $\pi_1(S^1) = \mathbb{Z}$ via the winding number argument.)

**Is NOT an instance — $\mathbb{R}^n$ and a point homeomorphically.** $\mathbb{R}^n$ is contractible but *not* homeomorphic to a point — it has uncountably many points. Homotopy equivalence is genuinely coarser than homeomorphism. The conflation is a common error.

**Corollary — homotopy equivalence is an equivalence relation.** Reflexive (identity is its own homotopy inverse), symmetric (the inverse pair flips), transitive (composing equivalences with their inverses, using composition-respects-homotopy).

**Corollary — contractible spaces are simply connected.** If $X$ is contractible, then $\pi_n(X) = 0$ for all $n \geq 0$. Every map from a sphere $S^n$ to $X$ extends to a map from $D^{n+1}$, using the contraction homotopy to "fill in" the disk. In particular, $\pi_1(X) = 0$, so $X$ is simply connected.

**Corollary — a retract of a contractible space is contractible.** If $X$ is contractible and $r : X \to A$ is a retraction (with $i : A \hookrightarrow X$ the inclusion), then $A$ is contractible. The contraction of $X$ restricts to a contraction of $A$ — see [[Ex - A retract of a contractible space is contractible]].

**Calibration check.** Verify: the annulus $\{(x, y) : 1 \leq x^2 + y^2 \leq 4\}$ is homotopy equivalent to $S^1$ (radial deformation retract); the Möbius strip is not homeomorphic to the cylinder $S^1 \times I$ even though both are homotopy equivalent to $S^1$ (they differ in orientability); the dunce cap is contractible despite being non-trivially built. If all three check out, you understand homotopy equivalence.

---

# Unlocked by This

> [!tip] Homotopy Category *(from Algebraic Topology)*
> The **homotopy category** $\mathbf{Ho}(\mathbf{Top})$ has topological spaces as objects and homotopy classes of maps as morphisms. Two spaces are isomorphic in this category iff they are homotopy equivalent. Every algebraic invariant of topology factors through this category.

> [!tip] Model Category *(from Abstract Homotopy Theory)*
> Quillen's **model category** axioms abstract the topological setting into a framework where homotopy equivalence ("weak equivalence") plus "fibration" and "cofibration" interact in well-defined ways. The category of topological spaces, the category of simplicial sets, and the category of chain complexes are all model categories with equivalent homotopy theories.
