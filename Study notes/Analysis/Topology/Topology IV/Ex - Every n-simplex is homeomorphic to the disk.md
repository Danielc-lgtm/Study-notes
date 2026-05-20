---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Convex Body"
  - "Thm - Compact Convex Body is Homeomorphic to a Disk"
  - "Def - Compact Space"
tags: [analysis, topology, convexity]
---

# Problem Statement

The **standard $n$-simplex** is
$$\Delta^n := \left\{(x_0, x_1, \dots, x_n) \in \mathbb{R}^{n+1} : x_i \geq 0, \, \sum_{i=0}^n x_i = 1\right\}.$$

Show that $\Delta^n$ is homeomorphic to the closed $n$-ball $D^n$.

**Recall:**

$\Delta^n$ sits in the affine hyperplane $\{\sum x_i = 1\} \subseteq \mathbb{R}^{n+1}$, which is an $n$-dimensional affine subspace. Within this hyperplane, $\Delta^n$ is a [[Def - Convex Body|convex body]]: closed (intersection of closed half-spaces and the hyperplane), convex (convex combinations preserve the constraints), and has nonempty interior (the centroid is interior).

[[Thm - Compact Convex Body is Homeomorphic to a Disk]] says: every compact convex body in $\mathbb{R}^n$ with nonempty interior is homeomorphic to $D^n$.

---

# Convergent Strategy

**Problem class:** Identify a specific compact convex set with the closed ball.

**Assumption pattern:** $\Delta^n$ is a compact convex body, but it sits inside the *hyperplane* $\{\sum x_i = 1\}$, not directly inside $\mathbb{R}^n$. The hyperplane is an affine subspace of dimension $n$, homeomorphic to $\mathbb{R}^n$.

**Theorem routing:** Identify the hyperplane $H := \{x \in \mathbb{R}^{n+1} : \sum x_i = 1\}$ with $\mathbb{R}^n$ via any affine isomorphism. Under this identification, $\Delta^n$ becomes a compact convex body in $\mathbb{R}^n$ with nonempty interior. Apply [[Thm - Compact Convex Body is Homeomorphic to a Disk]] to conclude $\Delta^n \cong D^n$.

**Key decision point:** The affine identification of $H \cong \mathbb{R}^n$. The simplest choice: project to the first $n$ coordinates, dropping $x_0$ (since $x_0 = 1 - \sum_{i=1}^n x_i$ is determined).

---

# Legal Operations Used

1. **Affine equivalence of $H$ with $\mathbb{R}^n$.** The hyperplane is an affine subspace, homeomorphic (in fact diffeomorphic) to $\mathbb{R}^n$ by any affine isomorphism.

2. **Apply the convex body theorem.** Once we identify $\Delta^n$ with a compact convex body in $\mathbb{R}^n$, the theorem gives the homeomorphism with $D^n$.

3. **Compactness.** $\Delta^n$ is compact as a closed bounded subset of $\mathbb{R}^{n+1}$ (each $x_i \in [0, 1]$).

---

# Hints

> [!note]- Hint 1
> $\Delta^n$ is a closed bounded subset of $\mathbb{R}^{n+1}$: each coordinate $x_i$ is in $[0, 1]$. So $\Delta^n \subseteq [0, 1]^{n+1}$, compact.

> [!note]- Hint 2
> $\Delta^n$ is convex: if $x, y \in \Delta^n$ and $t \in [0, 1]$, then $tx + (1-t)y$ has non-negative entries (convex combination of non-negative numbers is non-negative) and sums to $t \cdot 1 + (1-t) \cdot 1 = 1$. So $tx + (1-t)y \in \Delta^n$.

> [!note]- Hint 3
> Identify the hyperplane $H = \{\sum x_i = 1\}$ with $\mathbb{R}^n$ via the projection forgetting $x_0$: $(x_0, x_1, \dots, x_n) \mapsto (x_1, \dots, x_n)$. The inverse: $(x_1, \dots, x_n) \mapsto (1 - \sum_{i=1}^n x_i, x_1, \dots, x_n)$.

> [!note]- Hint 4
> Under this identification, $\Delta^n$ corresponds to $\{(x_1, \dots, x_n) \in \mathbb{R}^n : x_i \geq 0, \sum_{i=1}^n x_i \leq 1\}$. This is a compact convex body in $\mathbb{R}^n$ with nonempty interior (the open simplex $\{x_i > 0, \sum < 1\}$). Apply [[Thm - Compact Convex Body is Homeomorphic to a Disk]].

---

# Solution

**Step 1: Identify $\Delta^n$ with a subset of $\mathbb{R}^n$.**

> [!note]- Derivation
> The hyperplane $H := \{(x_0, \dots, x_n) \in \mathbb{R}^{n+1} : \sum x_i = 1\}$ is an $n$-dimensional affine subspace of $\mathbb{R}^{n+1}$.
>
> Define the affine isomorphism $\Phi : H \to \mathbb{R}^n$ by $\Phi(x_0, x_1, \dots, x_n) = (x_1, \dots, x_n)$ — projection onto the last $n$ coordinates. (Bijective because $x_0 = 1 - \sum_{i=1}^n x_i$ is determined by the others.)
>
> $\Phi$ is continuous (projection is continuous), $\Phi^{-1} : \mathbb{R}^n \to H$, $(x_1, \dots, x_n) \mapsto (1 - \sum_{i=1}^n x_i, x_1, \dots, x_n)$, is also continuous. So $\Phi$ is a homeomorphism.

**Step 2: Show $\Phi(\Delta^n)$ is a compact convex body in $\mathbb{R}^n$.**

> [!note]- Derivation
> $\Phi(\Delta^n) = \{(x_1, \dots, x_n) \in \mathbb{R}^n : x_i \geq 0 \text{ for } i = 1, \dots, n, \text{ and } 1 - \sum_{i=1}^n x_i \geq 0\}$.
>
> This is a closed subset of $\mathbb{R}^n$ (cut out by closed half-spaces $x_i \geq 0$ and $\sum x_i \leq 1$).
>
> Convex: convex combinations of points satisfying $x_i \geq 0$ and $\sum x_i \leq 1$ satisfy the same. Hence $\Phi(\Delta^n)$ is convex.
>
> Bounded: each $x_i \in [0, 1]$, so $\Phi(\Delta^n) \subseteq [0, 1]^n$. Hence compact (closed and bounded in $\mathbb{R}^n$).
>
> Nonempty interior: the point $(1/(n+1), \dots, 1/(n+1)) \in \Phi(\Delta^n)$ has each coordinate $1/(n+1) > 0$ and the sum is $n/(n+1) < 1$, so it lies in the open simplex $\{x_i > 0, \sum x_i < 1\}$. A small ball around this point stays in $\Phi(\Delta^n)$ (each coordinate stays positive and the sum stays below $1$, by continuity).

**Step 3: Apply the compact convex body theorem.**

> [!note]- Derivation
> $\Phi(\Delta^n)$ is a compact convex body in $\mathbb{R}^n$ with nonempty interior. By [[Thm - Compact Convex Body is Homeomorphic to a Disk]], $\Phi(\Delta^n) \cong D^n$.

**Step 4: Conclude $\Delta^n \cong D^n$.**

Combining: $\Delta^n \xrightarrow{\Phi} \Phi(\Delta^n) \cong D^n$. Both are homeomorphisms, so $\Delta^n \cong D^n$.

> [!note]- Complete formal solution
> Define $\Phi : \{(x_0, \dots, x_n) \in \mathbb{R}^{n+1} : \sum x_i = 1\} \to \mathbb{R}^n$ by $\Phi(x_0, \dots, x_n) = (x_1, \dots, x_n)$, a homeomorphism (affine isomorphism). Then $\Phi(\Delta^n) = \{(x_1, \dots, x_n) \in \mathbb{R}^n : x_i \geq 0, \sum x_i \leq 1\}$ is a compact convex body in $\mathbb{R}^n$ with nonempty interior. By [[Thm - Compact Convex Body is Homeomorphic to a Disk]], $\Phi(\Delta^n) \cong D^n$. Composing the two homeomorphisms: $\Delta^n \cong D^n$. $\blacksquare$

---

# Key Takeaways

**Affine vs. linear identification of hyperplanes.** A "$k$-dimensional convex body in an $n$-dimensional affine subspace of $\mathbb{R}^N$" is, intrinsically, a $k$-dimensional convex body in $\mathbb{R}^k$. The affine identification is just a change of coordinates. So the dimension that matters is the *intrinsic* dimension (the dimension of the affine span), not the ambient dimension. The $n$-simplex has intrinsic dimension $n$ even though it sits in $\mathbb{R}^{n+1}$.

**The convex body theorem is a powerful black box.** Once you've recognized a set as a compact convex body with nonempty interior in some $\mathbb{R}^n$, the theorem [[Thm - Compact Convex Body is Homeomorphic to a Disk]] immediately gives the disk identification. The trigger-reaction pattern: "see a compact convex full-dimensional set $\Rightarrow$ homeomorphic to $D^n$".

**Generalization: every convex polytope is a disk.** $\Delta^n$ is one example of a convex polytope. The same argument shows: every compact convex polytope (convex hull of finitely many points) of dimension $n$ is homeomorphic to $D^n$. This is the topological foundation of polytope theory and combinatorial topology.

**The boundary $\partial \Delta^n$ is a sphere.** As a corollary, the boundary of the $n$-simplex (the union of its $(n-1)$-dimensional faces) is homeomorphic to $S^{n-1}$. For $n = 2$: a triangle's boundary is a circle. For $n = 3$: a tetrahedron's boundary is a 2-sphere. This is the basis for simplicial approximation in algebraic topology — every continuous map from a triangle's boundary to $X$ is, up to homotopy, a map from a circle to $X$.

**The interior $\operatorname{int}(\Delta^n)$ is an open disk.** The interior of $\Delta^n$ (open simplex) is homeomorphic to $\operatorname{int}(D^n) = $ open ball, which is homeomorphic to $\mathbb{R}^n$. So $\operatorname{int}(\Delta^n) \cong \mathbb{R}^n$ — the open simplex is a "copy of $\mathbb{R}^n$" with a cellular boundary glued on. This decomposition is the cellular structure of the simplex.
