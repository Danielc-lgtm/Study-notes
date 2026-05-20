---
type: theorem
subject: topology
prereqs:
  - "Def - Quotient Topology and Identification Map"
  - "Thm - Universal Property of the Quotient"
  - "Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism"
tags: [analysis, topology, quotient, sphere]
---

# Notation

$D^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$ the closed unit $n$-disk; $S^n = \{x \in \mathbb{R}^{n+1} : \|x\| = 1\}$ the unit $n$-sphere; $S^{n-1} = \partial D^n$ the boundary of $D^n$. $D^n/S^{n-1}$ the quotient of $D^n$ collapsing the boundary to a point. The full registry is on the topic page.

---

# Motivation

This theorem is the workhorse identification in basic topology: it says that the $n$-sphere can be built from the $n$-disk by collapsing the boundary to a single point. Geometrically, you take the disk and pull all the boundary inwards to a single "north pole"; the resulting space is the sphere.

Why is this useful? Because it lets you build spheres iteratively from disks, which are easier to work with: $D^n$ is a convex body (and hence contractible), while $S^n$ is much more rigid (and not contractible). The decomposition $S^n = (D^n \setminus S^{n-1}) \cup \{*\}$ — an open $n$-disk plus one point — is the prototype CW decomposition: $S^n$ has cells of dimensions $0$ and $n$.

The result also generalizes the classical view of $S^n$ as a "compactified open disk": the open ball $\operatorname{int}(D^n)$, plus a point at infinity to close it up, gives $S^n$. The theorem makes this rigorous via the quotient construction.

---

# Statement

For each $n \geq 1$, the quotient space $D^n / S^{n-1}$ — the $n$-disk with its boundary $(n-1)$-sphere collapsed to a single point — is homeomorphic to the $n$-sphere $S^n$:
$$D^n / S^{n-1} \cong S^n.$$

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for the construction is: "we have $D^n$, a closed disk, and want to identify it with a sphere via a boundary-collapsing quotient". The technique generalizes to:

**Suspension of a sphere.** Property $B$: instead of $D^n$, take the cylinder $S^{n-1} \times I$ and collapse each end of the cylinder to a point. The bridge: $D^n \cong CS^{n-1}$ (the cone on $S^{n-1}$), and collapsing the cone point's boundary gives a sphere; iterating, $\Sigma S^{n-1} = S^n$. So suspension is iterated coning, and the sphere identification iterates: $S^{n+1} = \Sigma S^n$. *Example:* the suspension construction in homotopy theory.

**Join of spheres.** Property $B$: $S^n * S^m$, the join, is $S^{n+m+1}$. The proof factors through the same "collapse" pattern, with $D^{n+1} \times D^{m+1}$ as the input. The bridge: the join is a particular adjunction.

**Targets (Output Amplification)**

The conclusion $D^n / S^{n-1} \cong S^n$ amplifies in several directions.

Combine with **homotopy invariance.** Property $D$: $D^n$ is contractible. The amplified result $E$: $S^n = D^n / S^{n-1}$ has the same singular homology as the pair $(D^n, S^{n-1})$, which gives $H_n(S^n) = \mathbb{Z}$, the fundamental computation. This is the basis of the long exact sequence of a pair.

Combine with **cellular structure.** Property $D$: the quotient gives a CW structure on $S^n$ with one $0$-cell and one $n$-cell. The amplified result $E$: $S^n$ has a minimal CW structure, and its cellular chain complex is $\mathbb{Z} \to 0 \to \dots \to 0 \to \mathbb{Z}$, immediately giving its homology.

Combine with **the degree of a map.** Property $D$: a map $f : S^n \to S^n$ extends to $f : D^n \to D^n$ via the cone structure. The amplified result $E$: the degree of $f$ is computable from how it acts on the top-dimensional cell — a fundamental tool of degree theory.

---

# Why Is It True

Visualize $D^n$ as a closed disk. The boundary $S^{n-1}$ is a sphere of one lower dimension sitting on the rim. As we pull the rim together to a single point, the disk warps into a sphere: imagine a flat disk in $\mathbb{R}^3$, then the rim contracting and lifting up to a single "north pole" while the interior of the disk swells outward and downward to become the rest of the sphere.

The construction in Bredon (Example 13.10) makes this precise via an explicit projection. Place a disk of radius 2 with center at height 1 on the vertical axis. This is the "lower $n$-hemisphere" of a vertical scaling. Project radially (towards the vertical axis) onto a sphere of radius 1 centered at the origin. The map is distance-decreasing in some sense, hence continuous, and sends the rim of the disk (boundary $S^{n-1}$) to the north pole.

The factored map $\bar k : D^n / S^{n-1} \to S^n$ is then:

- *Surjective:* the radial projection covers $S^n$ (every point of $S^n$ is hit by the disk).
- *Injective:* points in the interior of $D^n$ project to different points of $S^n$ (the radial projection is injective on the interior), and all boundary points project to the same point (the north pole) — but they are identified in the quotient, so $\bar k$ is injective on the quotient.

So $\bar k$ is a continuous bijection. The source $D^n / S^{n-1}$ is compact (continuous image of compact $D^n$), and the target $S^n$ is Hausdorff (subspace of $\mathbb{R}^{n+1}$). By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\bar k$ is a homeomorphism.

The reason to *expect* this result: every topological identification of "fold the boundary of a disk to a point" should give *something*, and that something should be a closed manifold of the same dimension. The simply-connected closed $n$-manifolds in dimension $n$ are very rigid; the most natural one is $S^n$. The theorem confirms that the natural construction does produce the natural manifold.

---

# What Makes This Hard

The non-obvious step is *constructing* the explicit continuous bijection $D^n / S^{n-1} \to S^n$. The radial projection from a translated disk (Bredon's construction) requires some geometric setup that is not the first thing one would write down. A simpler but equivalent route is to use the cone structure: $D^n \cong CS^{n-1}$ identifies the disk with the cone on its boundary, and then $CS^{n-1}/S^{n-1}$ is the suspension construction, which equals $S^n$ as a routine consequence. The common error is to assert the homeomorphism without specifying the map — "the disk with boundary collapsed must be a sphere by intuition" is suggestive but not a proof.

---

# Rederivation Scaffold

**High-level strategy:**
Construct an explicit continuous map $D^n \to S^n$ sending all of $S^{n-1}$ to one point (the north pole), and bijective elsewhere. Descend to the quotient via the universal property. Upgrade via compact-Hausdorff.

**Subgoal decomposition:**

1. **Construct the radial projection.** Let $p : D^n \to S^n$ be the explicit projection from a translated disk to the sphere (Bredon's construction) or equivalently use the cone structure $D^n \cong CS^{n-1}$ and project $CS^{n-1} \to \Sigma S^{n-1} = S^n$.
   - *Hint:* The map sends $(x, t) \in CS^{n-1}$ (with $\|x\| = 1$, $t \in [0, 1]$, with $t = 1$ being the cone point) to $S^n$ via $(\sin(\pi t) \cdot x, \cos(\pi t))$.
   - *Why needed:* This is the descent target.

2. **Descend to the quotient.** Since $p$ is constant on $S^{n-1} = \partial D^n$ (sending it all to the north pole), it factors through the quotient $D^n/S^{n-1}$, giving a continuous map $\bar p : D^n/S^{n-1} \to S^n$ by [[Thm - Universal Property of the Quotient]].
   - *Hint:* The universal property requires checking $p$ is well-defined on equivalence classes.

3. **Show $\bar p$ is bijective.** Surjectivity: $p$ surjective. Injectivity: $p$ is injective on $D^n \setminus S^{n-1}$, and identifies all of $S^{n-1}$ to one point — but the quotient already identifies these.

4. **Upgrade to homeomorphism.** $D^n / S^{n-1}$ is compact (image of compact $D^n$); $S^n$ is Hausdorff. By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\bar p$ is a homeomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: The cone $CS^{n-1}$ is homeomorphic to $D^n$
> **Statement:** Let $CS^{n-1} = (S^{n-1} \times I) / (S^{n-1} \times \{1\})$ be the cone on the sphere. Then $CS^{n-1} \cong D^n$.
>
> **Hint:** The map $(x, t) \mapsto (1-t)x$ from $S^{n-1} \times I$ to $D^n$ collapses $S^{n-1} \times \{1\}$ to $0$ and is bijective elsewhere.
>
> **Why needed:** Connects the cone to the disk for the cone-version of the proof.
>
> > [!note]- Full proof
> > Define $f : S^{n-1} \times I \to D^n$ by $f(x, t) = (1-t)x$. This is continuous (multiplication is continuous), surjective (every point of $D^n$ is of the form $(1 - \|y\|/1)(y/\|y\|)$ for $y \neq 0$, with $0$ mapped to by $t = 1$), and identifies $S^{n-1} \times \{1\}$ to the single point $0 \in D^n$. By the universal property of the quotient, $f$ descends to a continuous bijection $CS^{n-1} \to D^n$. $CS^{n-1}$ is compact (image of compact $S^{n-1} \times I$); $D^n$ is Hausdorff. By compact-Hausdorff upgrade, the descended map is a homeomorphism.

> [!note]- Lemma 2: The suspension $\Sigma S^{n-1}$ is homeomorphic to $S^n$
> **Statement:** Let $\Sigma S^{n-1} = (S^{n-1} \times I) / \sim$ where $\sim$ collapses $S^{n-1} \times \{0\}$ to one point and $S^{n-1} \times \{1\}$ to another. Then $\Sigma S^{n-1} \cong S^n$.
>
> **Hint:** Construct the explicit map $(x, t) \mapsto (\sin(\pi t) x, \cos(\pi t)) \in S^n \subseteq \mathbb{R}^{n+1}$.
>
> **Why needed:** This is the "suspension equals next sphere" identification, equivalent to the disk-quotient theorem.
>
> > [!note]- Full proof
> > Define $g : S^{n-1} \times I \to S^n$ by $g(x, t) = (\sin(\pi t) x, \cos(\pi t))$, where $x \in S^{n-1} \subseteq \mathbb{R}^n$ and the result lies in $\mathbb{R}^{n+1}$. Check: $\|g(x, t)\|^2 = \sin^2(\pi t)\|x\|^2 + \cos^2(\pi t) = \sin^2(\pi t) + \cos^2(\pi t) = 1$, so $g$ maps into $S^n$. Continuous (composition of continuous functions). Surjective: every point of $S^n$ has the form $(y, z)$ with $\|y\|^2 + z^2 = 1$; set $z = \cos(\pi t)$ for $t \in [0, 1]$ (uniquely determined), then $y = \sin(\pi t) x$ for $x = y/\|y\| \in S^{n-1}$ (with conventions at the poles). Identifies $S^{n-1} \times \{0\}$ to the north pole $(0, \dots, 0, 1)$ and $S^{n-1} \times \{1\}$ to the south pole $(0, \dots, 0, -1)$. By universal property, descends to a continuous bijection $\Sigma S^{n-1} \to S^n$. By compact-Hausdorff upgrade, a homeomorphism.

> [!note]- Lemma 3: $D^n / S^{n-1} \cong CS^{n-1} / S^{n-1} = \Sigma S^{n-1} / \{N\}$
> **Statement:** Collapsing the boundary of the disk is the same as taking the suspension of the boundary and identifying one cone point.
>
> **Hint:** The cone $CS^{n-1}$ has $S^{n-1}$ as its base (the $t = 0$ end) and one cone point (the $t = 1$ end); the disk $D^n$ is the cone with $S^{n-1}$ as the boundary. Collapsing the boundary of the disk corresponds to collapsing the base of the cone.
>
> **Why needed:** Combines Lemmas 1 and 2 to get the main theorem.
>
> > [!note]- Full proof
> > By Lemma 1, $D^n \cong CS^{n-1}$ with the boundary $S^{n-1} \subseteq D^n$ corresponding to $S^{n-1} \times \{0\}$ in the cone. So $D^n / S^{n-1} \cong CS^{n-1} / (S^{n-1} \times \{0\})$. The right side, by definition, is the suspension $\Sigma S^{n-1}$ with one cone point already identified to a different point (the cone point $S^{n-1} \times \{1\}$), so it equals $\Sigma S^{n-1}$. By Lemma 2, $\Sigma S^{n-1} \cong S^n$.

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $D^n \cong CS^{n-1}$ via $(x, t) \mapsto (1-t)x$ — a homeomorphism. This carries the boundary $S^{n-1} \subseteq D^n$ to $S^{n-1} \times \{0\}$ in $CS^{n-1}$. So
> $$D^n / S^{n-1} \cong CS^{n-1} / (S^{n-1} \times \{0\}).$$
> The right side has the cone point $S^{n-1} \times \{1\}$ already identified (by the cone construction) and now also $S^{n-1} \times \{0\}$ identified to a single point: this is exactly the suspension $\Sigma S^{n-1}$ (which identifies both ends of $S^{n-1} \times I$). By Lemma 2, $\Sigma S^{n-1} \cong S^n$ via $(x, t) \mapsto (\sin(\pi t)x, \cos(\pi t))$.
>
> Composing: $D^n / S^{n-1} \cong S^n$. $\blacksquare$
>
> Alternative direct proof (Bredon's approach): place $D^n$ as the disk of radius 2 with center at height 1 on the vertical axis. Project radially toward the vertical axis onto the unit sphere $S^n$ centered at the origin. This is distance-decreasing on the disk, hence continuous. The boundary $S^{n-1}$ of the disk projects to the north pole (north pole = point closest to disk's center in the radial direction); interior points project to other points of $S^n$ injectively. The factored map $\bar k : D^n / S^{n-1} \to S^n$ is a continuous bijection, and is a homeomorphism by [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]].

---

# Cross-Field Exercise Suggestions

**One-point compactification of $\mathbb{R}^n$.** The one-point compactification of $\mathbb{R}^n$ (Euclidean space plus a point at infinity) is $S^n$. The proof is analogous to the disk-quotient: $\mathbb{R}^n$ embeds in $D^n$ as the interior, and the boundary is "infinity" — collapsing it gives $S^n$. This is the classical "stereographic projection compactification" argument.

**Smash product of spheres.** $S^m \wedge S^n = S^{m+n}$ (smash product of spheres is the next sphere). The proof writes both sides as quotients of cells via the disk-sphere identification.

**The Hopf fibration.** $S^3 / S^1 = S^2$ (mod out $S^3$ by the diagonal $S^1$ action). The proof uses the disk-quotient idea combined with the $S^1$ action on each fiber.

---

# Bridges

- **[[Thm - Universal Property of the Quotient]]** — the engine for descending the explicit map to the quotient.

- **[[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]** — the upgrade from continuous bijection to homeomorphism.

- **[[Def - Mapping Cylinder and Mapping Cone]]** — the cone construction $CS^{n-1}$ is the mapping cone of $1_{S^{n-1}}$, and the disk $D^n$ is the cone.

---

# Unlocked by This

> [!tip] CW Structure of Spheres *(from Algebraic Topology)*
> $S^n$ has a CW structure with one $0$-cell (the basepoint) and one $n$-cell (the open disk attached via $S^{n-1} \to *$). This is the minimal CW decomposition and immediately gives $H_n(S^n) = \mathbb{Z}, H_k(S^n) = 0$ for $0 < k < n$.

> [!tip] Suspension Functor *(from Stable Homotopy Theory)*
> The **suspension** $\Sigma X = (X \times I)/(X \times \{0\} \cup X \times \{1\})$ raises sphere dimension: $\Sigma S^n = S^{n+1}$. Iterating gives the Freudenthal suspension theorem: $\pi_k(X)$ stabilizes for $k$ small relative to $n$ when $X$ is $(n-1)$-connected.
