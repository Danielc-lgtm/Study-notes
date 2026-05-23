---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Quotient Topology and Identification Map"
  - "Def - Product Topology"
  - "Thm - Universal Property of the Quotient"
  - "Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism"
tags: [analysis, topology, quotient, torus]
---

# Problem Statement

The $2$-torus $T^2$ has four standard definitions:

1. $T_1 := \mathbb{R}^2 / \mathbb{Z}^2$, the quotient of the plane by the equivalence relation $(x, y) \sim (x', y')$ iff $x - x', y - y' \in \mathbb{Z}$.
2. $T_2 := [0, 1]^2 / {\sim}$, the unit square with the equivalence relation identifying opposite edges: $(0, y) \sim (1, y)$ and $(x, 0) \sim (x, 1)$.
3. $T_3 := S^1 \times S^1$, the product of two circles.
4. $T_4 :=$ the "anchor ring" — the surface of revolution obtained by rotating a circle around a coplanar axis disjoint from it, sitting in $\mathbb{R}^3$.

Show that $T_1 \cong T_2 \cong T_3 \cong T_4$ as topological spaces.

**Recall:**

A [[Def - Quotient Topology and Identification Map|quotient topology]] is the finest topology on a quotient space making the projection continuous. A continuous bijection from a compact space to a Hausdorff space is automatically a [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|homeomorphism]]. The [[Thm - Universal Property of the Quotient|universal property]] says: a function out of a quotient is continuous iff its precomposition with the projection is continuous.

---

# Convergent Strategy

**Problem class:** Identification of multiple definitions of a quotient space.

**Assumption pattern:** Each definition is a quotient or product construction. The compact-Hausdorff upgrade is available because each constructed space is compact (continuous image of a compact source) and the targets are Hausdorff.

**Theorem routing:** [[Thm - Universal Property of the Quotient]] to construct continuous maps between the quotients; [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]] to upgrade to homeomorphism.

**Key decision point:** Choose the right pair-by-pair homeomorphisms. The cleanest chain is $T_1 \to T_2 \to T_3 \to T_4$, with each step a continuous bijection between compact and Hausdorff. Alternatively, $T_3$ can be taken as the "central" hub and each other shown to be homeomorphic to it directly.

---

# Legal Operations Used

1. **Construct a continuous map factoring through a quotient.** Given a continuous map respecting the equivalence relation, descend via the universal property.

2. **Compact-Hausdorff upgrade.** Continuous bijection from compact to Hausdorff is a homeomorphism.

3. **Build a quotient by an equivalence relation.** Define explicit equivalence; verify the resulting topology via universal property.

---

# Hints

> [!note]- Hint 1
> The strategy is "construct + descend + upgrade". For each pair, construct an explicit continuous map between the source and target that respects the equivalence; show it descends to a continuous map on the quotient; check bijectivity; upgrade compact-Hausdorff.

> [!note]- Hint 2
> For $T_1 \to T_3$: the map $(x, y) \mapsto (e^{2\pi i x}, e^{2\pi i y})$ from $\mathbb{R}^2$ to $S^1 \times S^1$ is continuous and respects the equivalence $\mathbb{Z}^2$. Descends to $T_1 \to T_3$.

> [!note]- Hint 3
> For $T_2 \to T_3$: similar. Restrict the same map to $[0, 1]^2$. The endpoints get sent to the same place: $e^{2\pi i \cdot 0} = e^{2\pi i \cdot 1} = 1$.

> [!note]- Hint 4
> For $T_3 \to T_4$: the anchor ring is parametrized by two angles. Use $(\theta, \phi) \mapsto ((R + r\cos \phi)\cos \theta, (R + r\cos \phi)\sin \theta, r \sin \phi)$ for radii $R > r > 0$. This is a continuous map from $S^1 \times S^1$ to $\mathbb{R}^3$, with image the anchor ring; injective and continuous, compact-Hausdorff upgrade.

---

# Solution

The proof breaks into three steps, each executing the "construct + descend + upgrade" recipe to identify a quotient with a product or embedded space. Step 1 builds $T_1 \cong T_3$ via $(x,y) \mapsto (e^{2\pi i x}, e^{2\pi i y})$, descending from $\mathbb{R}^2$ to $\mathbb{R}^2/\mathbb{Z}^2$ and upgrading to homeomorphism by the compact-to-Hausdorff theorem; Step 2 does $T_2 \cong T_3$ using the same exponential map restricted to $[0,1]^2$, which respects the edge identifications; Step 3 does $T_3 \cong T_4$ via the standard anchor-ring parametrization $\Theta(\theta, \phi) = ((R + r\cos\phi)\cos\theta, (R + r\cos\phi)\sin\theta, r\sin\phi)$. The non-obvious move is the universal compact-Hausdorff upgrade — it lets us avoid constructing inverse maps explicitly, since a continuous bijection from a compact space into a Hausdorff space is automatically a homeomorphism.

**Step 1: $T_1 \cong T_3$.**

Define $\Phi : \mathbb{R}^2 \to S^1 \times S^1$ by $\Phi(x, y) = (e^{2\pi i x}, e^{2\pi i y})$. Continuous (each component is the composition $\mathbb{R} \to \mathbb{C}$, $t \mapsto e^{2\pi i t}$). Respects $\mathbb{Z}^2$: $\Phi(x + m, y + n) = (e^{2\pi i (x + m)}, e^{2\pi i (y + n)}) = (e^{2\pi i x}, e^{2\pi i y}) = \Phi(x, y)$ for $m, n \in \mathbb{Z}$.

By [[Thm - Universal Property of the Quotient]], $\Phi$ descends to a continuous $\bar\Phi : T_1 = \mathbb{R}^2/\mathbb{Z}^2 \to S^1 \times S^1$. Bijective: $\bar\Phi([(x,y)]) = (e^{2\pi i x}, e^{2\pi i y})$, and two points map to the same image iff $x - x' \in \mathbb{Z}$ and $y - y' \in \mathbb{Z}$, iff they are in the same $\mathbb{Z}^2$-class. So $\bar\Phi$ is injective. Surjective: any $(z, w) \in S^1 \times S^1$ has $z = e^{2\pi i x}, w = e^{2\pi i y}$ for some $x, y \in [0, 1)$.

> [!note]- Derivation — compact-Hausdorff upgrade
> $T_1 = \mathbb{R}^2/\mathbb{Z}^2$ is compact: it equals the continuous image of $[0, 1]^2$ (compact) under the quotient projection. $S^1 \times S^1$ is Hausdorff (product of Hausdorff spaces). $\bar\Phi$ is a continuous bijection. By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\bar\Phi$ is a homeomorphism.

**Step 2: $T_2 \cong T_3$.**

Define $\Psi : [0, 1]^2 \to S^1 \times S^1$ by the same formula $\Psi(x, y) = (e^{2\pi i x}, e^{2\pi i y})$. Continuous. Respects the edge identifications: $\Psi(0, y) = (1, e^{2\pi i y}) = \Psi(1, y)$, and similarly $\Psi(x, 0) = \Psi(x, 1)$.

By the universal property, $\Psi$ descends to $\bar\Psi : T_2 \to S^1 \times S^1$. Bijective (the identifications make the map well-defined on the boundary; on the interior, distinct points have distinct images).

> [!note]- Derivation — compact-Hausdorff upgrade
> $T_2 = [0,1]^2/{\sim}$ is compact (continuous image of compact $[0, 1]^2$). $S^1 \times S^1$ is Hausdorff. Continuous bijection upgrade gives $\bar\Psi$ a homeomorphism.

**Step 3: $T_3 \cong T_4$.**

Fix radii $R > r > 0$. Parametrize the anchor ring $T_4 \subseteq \mathbb{R}^3$ by
$$\Theta(\theta, \phi) = ((R + r\cos\phi)\cos\theta, (R + r\cos\phi)\sin\theta, r\sin\phi),$$
viewed as a map $S^1 \times S^1 \to \mathbb{R}^3$ (using $\theta, \phi \in \mathbb{R}/2\pi\mathbb{Z}$).

Continuous: each component is a product of cosines, sines, constants.

Injective: $\Theta(\theta_1, \phi_1) = \Theta(\theta_2, \phi_2)$ requires same $\theta$ (from the $(\cos\theta, \sin\theta)$ factor projected to the $xy$-direction) and same $\phi$ (from $z = r \sin\phi$ and the radial distance $\sqrt{x^2 + y^2} = R + r\cos\phi$). Care at $\phi = \pi$ (where $\sin\phi = 0$) — but $r\cos\phi = -r$ gives radial distance $R - r > 0$, so the point is on the inner circle. Bijection: image is exactly $T_4$.

> [!note]- Derivation — compact-Hausdorff upgrade
> $S^1 \times S^1$ is compact (product of compacts). $T_4 \subseteq \mathbb{R}^3$ is Hausdorff (subspace of Hausdorff). $\Theta$ is a continuous bijection onto $T_4$. By compact-to-Hausdorff upgrade, $\Theta$ is a homeomorphism.

> [!note]- Complete formal solution
> By Steps 1, 2, 3: $T_1 \cong T_3$, $T_2 \cong T_3$, $T_3 \cong T_4$. Composing: $T_1 \cong T_2 \cong T_3 \cong T_4$. $\blacksquare$
>
> Explicitly, the chain of homeomorphisms is:
> $$T_1 = \mathbb{R}^2/\mathbb{Z}^2 \xrightarrow{\bar\Phi} S^1 \times S^1 = T_3 \xrightarrow{\Theta} T_4,$$
> and $T_2 = [0, 1]^2/{\sim} \xrightarrow{\bar\Psi} T_3$. Composing $\bar\Psi^{-1}$ with $\bar\Phi$ gives $T_1 \cong T_2$.

---

# Key Takeaways

**The "construct + descend + upgrade" recipe.** This is the canonical proof structure for identifying a quotient with a known space. The pattern is: (1) write down a continuous map from the source $X$ (before quotienting) to the target $Y$; (2) check that the map respects the equivalence relation on $X$; (3) use [[Thm - Universal Property of the Quotient]] to descend to a continuous map $X/{\sim} \to Y$; (4) check bijectivity; (5) upgrade via [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]. This is the trigger-reaction pattern: "see a continuous bijection out of a compact quotient into a Hausdorff space $\Rightarrow$ it's a homeomorphism".

**Compactness comes from the source.** $T_1$ and $T_2$ are compact because they are continuous images of compact spaces ($[0, 1]^2$ or finite-area regions of $\mathbb{R}^2$). $T_3$ is compact as a product of compacts. $T_4$ is compact as a continuous image of $S^1 \times S^1$. So the compactness of all four pieces ultimately traces back to compactness of $[0, 1]$.

**Choice of map matters, but uniqueness up to homotopy doesn't.** The specific maps $\Phi, \Psi, \Theta$ are not unique — different parametrizations give different but equivalent homeomorphisms. What matters is that *some* such map exists. This is the structural content of "the torus is well-defined as a topological space": all four constructions give the same space up to homeomorphism, even if individual homeomorphisms differ.

**Higher-dimensional generalization.** The same proof works in higher dimensions: $T^n := \mathbb{R}^n/\mathbb{Z}^n \cong [0, 1]^n/{\sim} \cong (S^1)^n$. The fourth (embedded) form gets harder — there is no clean $\mathbb{R}^{n+1}$-embedded analogue of the anchor ring for $n \geq 3$ — but the first three are immediate.
