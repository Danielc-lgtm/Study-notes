---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Homotopy Equivalence and Contractible Space"
  - "Def - Homotopy"
tags: [analysis, topology, homotopy, contractibility]
---

# Problem Statement

Show that $\mathbb{R}^n$ is contractible: there is a continuous homotopy from the identity map $1_{\mathbb{R}^n}$ to the constant map $c_0$ sending everything to $0$.

Equivalently, show that $\mathbb{R}^n$ is homotopy equivalent to a point.

**Recall:**

$\mathbb{R}^n$ is [[Def - Homotopy Equivalence and Contractible Space|contractible]] if it is homotopy equivalent to a one-point space; equivalently, the identity $1_{\mathbb{R}^n}$ is [[Def - Homotopy|homotopic]] to a constant map. A homotopy is a continuous map $F : \mathbb{R}^n \times I \to \mathbb{R}^n$ with $F(x, 0) =$ identity and $F(x, 1) =$ constant.

---

# Convergent Strategy

**Problem class:** Exhibit a contraction homotopy on Euclidean space.

**Assumption pattern:** $\mathbb{R}^n$ is convex — the line segment from $x$ to $0$ lies entirely in $\mathbb{R}^n$. This is exactly the property we need.

**Theorem routing:** Construct the explicit linear-interpolation homotopy $F(x, t) = (1-t)x$. Verify continuity, the endpoint values, and the codomain.

**Key decision point:** The "scale by $1-t$" homotopy. At $t = 0$, no scaling; at $t = 1$, scale by $0$. The homotopy linearly interpolates between the identity and the constant map.

---

# Legal Operations Used

1. **Construct a homotopy by linear interpolation in a convex space.** When the target is convex (or star-shaped), straight-line homotopies $F(x, t) = (1-t) f_0(x) + t f_1(x)$ are continuous and valid.

2. **Verify endpoint conditions.** $F(x, 0) = f_0(x)$ and $F(x, 1) = f_1(x)$ as required.

---

# Hints

> [!note]- Hint 1
> The contracting homotopy "shrinks" the space toward the origin. The simplest such map: $F(x, t) = (1-t)x$. At $t = 0$, $F = 1_{\mathbb{R}^n}$; at $t = 1$, $F = c_0$.

> [!note]- Hint 2
> Continuity is just the continuity of scalar multiplication: $(x, t) \mapsto (1-t)x$ is continuous because both factors are continuous.

> [!note]- Hint 3
> The same trick works for any convex (or star-shaped) subset of $\mathbb{R}^n$ — contract to any "star center" linearly.

---

# Solution

The proof breaks into four short steps that exhibit a contraction homotopy on $\mathbb{R}^n$ via linear interpolation. Step 1 defines $F(x,t) = (1-t)x$; Step 2 checks continuity (polynomial in the coordinates); Step 3 verifies $F(\cdot, 0) = 1_{\mathbb{R}^n}$ and $F(\cdot, 1) = c_0$; Step 4 concludes contractibility. The non-obvious move is that there is no non-obvious move — convexity does all the work, because the straight-line segment from $x$ to $0$ stays inside $\mathbb{R}^n$, and the same recipe generalises to any star-shaped subset.

**Step 1: Define the contraction homotopy.**

Let $F : \mathbb{R}^n \times I \to \mathbb{R}^n$ be $F(x, t) = (1 - t) x$.

**Step 2: Verify continuity.**

> [!note]- Derivation
> $F$ is a polynomial in $(x_1, \dots, x_n, t)$: each component is $(1 - t)x_i$. Continuous because scalar multiplication and subtraction are continuous, and product of continuous functions is continuous. So $F : \mathbb{R}^n \times I \to \mathbb{R}^n$ is continuous.

**Step 3: Verify endpoint conditions.**

> [!note]- Derivation
> At $t = 0$: $F(x, 0) = (1 - 0)x = x$. So $F(\cdot, 0) = 1_{\mathbb{R}^n}$.
>
> At $t = 1$: $F(x, 1) = (1 - 1)x = 0$. So $F(\cdot, 1) = c_0$, the constant map at $0$.

**Step 4: Conclude $\mathbb{R}^n$ is contractible.**

$F$ is a homotopy from $1_{\mathbb{R}^n}$ to $c_0$. By the characterization of contractibility ([[Def - Homotopy Equivalence and Contractible Space]]), $\mathbb{R}^n$ is contractible.

> [!note]- Complete formal solution
> Define $F : \mathbb{R}^n \times I \to \mathbb{R}^n$ by $F(x, t) := (1 - t) x$. Continuous (polynomial in coordinates). $F(x, 0) = x = 1_{\mathbb{R}^n}(x)$; $F(x, 1) = 0 = c_0(x)$. Hence $1_{\mathbb{R}^n} \simeq c_0$, so $\mathbb{R}^n$ is contractible. $\blacksquare$

---

# Key Takeaways

**Linear interpolation is the default contraction in convex spaces.** Any convex subset of $\mathbb{R}^n$ (or any topological vector space) is contractible via the straight-line homotopy from $1$ to a constant map at any chosen point. The trigger-reaction pattern: "convex set + want to show contractible $\Rightarrow$ scale toward a fixed point". This is the simplest and most reliable form of homotopy construction.

**Star-shaped sets generalize the recipe.** A set $X \subseteq \mathbb{R}^n$ is **star-shaped** with respect to $x_0$ if for every $x \in X$, the segment $\overline{x_0 x}$ lies in $X$. Star-shaped sets are contractible: the homotopy $F(x, t) = (1-t)x + tx_0$ stays in $X$ by the star-shape assumption, and contracts $X$ to $\{x_0\}$. Convex sets are special star-shaped sets (star-shaped with respect to every point). So convexity is the strongest version of this principle.

**Topology vs. dimension.** $\mathbb{R}^n$ is contractible — homotopy equivalent to a point — for every $n \geq 0$. But $\mathbb{R}^n$ is *not homeomorphic* to a point for $n \geq 1$. The lesson: homotopy equivalence is much coarser than homeomorphism. The whole "shape" of $\mathbb{R}^n$ (size, dimension, density) is collapsed to nothing by homotopy equivalence.

**Punctured Euclidean space is NOT contractible.** $\mathbb{R}^n \setminus \{0\}$ for $n \geq 1$ is *not* contractible: it deformation retracts to $S^{n-1}$, which has nontrivial homotopy and homology (e.g., $\pi_{n-1}(S^{n-1}) = \mathbb{Z}$). The straight-line homotopy fails: linear interpolation toward $0$ would pass *through* the deleted point. So contractibility is a delicate property — small punctures destroy it. See [[Ex - Sphere is a deformation retract of punctured Euclidean space]].
