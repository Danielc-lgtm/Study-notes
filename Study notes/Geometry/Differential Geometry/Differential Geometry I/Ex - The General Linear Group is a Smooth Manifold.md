---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Thm - Open Subset of a Smooth Manifold"
  - "Def - Coordinate Chart and Atlas"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that the general linear group
$$\mathrm{GL}(n, \mathbb{R}) = \{A \in M(n \times n, \mathbb{R}) : \det A \neq 0\}$$
is a smooth manifold of dimension $n^2$, and identify its smooth structure.

**Recall:**

The space $M(n \times n, \mathbb{R})$ of all $n \times n$ real matrices is a real vector space of dimension $n^2$. Choosing the standard basis $\{E_{ij} : 1 \leq i, j \leq n\}$ (with $E_{ij}$ having $1$ in the $(i,j)$ position and $0$ elsewhere) gives an isomorphism $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$. The determinant $\det : M(n \times n, \mathbb{R}) \to \mathbb{R}$ is a polynomial function in the matrix entries, hence continuous.

The open submanifold theorem:

![[Thm - Open Subset of a Smooth Manifold#Statement]]

---

# Convergent Strategy

**Problem class:** Identifying a smooth manifold structure via the open-submanifold theorem — type 4 of the problem-solving routine in [[Differential Geometry I — Smooth Manifolds and Atlases#Problem-Solving Strategy]]. The space is presented as an open subset of a known smooth manifold (here, the vector space $M(n \times n, \mathbb{R})$).

**Assumption pattern:** $\mathrm{GL}(n, \mathbb{R})$ is defined by a *strict inequality* involving a continuous function (the determinant). Strict inequalities cut out *open* subsets. Once we recognize this, the open-submanifold theorem applies immediately and there is no further verification required — the smooth structure is automatic and inherited from the ambient $\mathbb{R}^{n^2}$.

**Theorem routing:** The route is: $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$ as a smooth $n^2$-manifold (since it is a finite-dimensional vector space with the standard smooth structure); $\det$ is a continuous (polynomial) function on $M(n \times n, \mathbb{R})$; $\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ is the preimage of an open set, hence open; by [[Thm - Open Subset of a Smooth Manifold]], $\mathrm{GL}(n, \mathbb{R})$ inherits a smooth manifold structure of dimension $n^2$.

**Key decision point:** Recognizing that the *strict* inequality $\det A \neq 0$ defines an open set — *not* an equality (which would give a closed submanifold of lower dimension). The closely related groups $\mathrm{SL}(n, \mathbb{R}) = \{A : \det A = 1\}$ (special linear group) and $\mathrm{O}(n) = \{A : A^T A = I\}$ (orthogonal group) are *not* open subsets — they are closed submanifolds of lower dimension, and require the more sophisticated regular value theorem of [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]] to handle.

---

# Legal Operations Used

1. **Operation 4 from the topic page (pass to an open subset).** $\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ is the preimage of an open set under a continuous function, hence open in $M(n \times n, \mathbb{R})$. By [[Thm - Open Subset of a Smooth Manifold]], $\mathrm{GL}(n, \mathbb{R})$ inherits a smooth $n^2$-manifold structure.

2. **Operation 8 from the topic page (verify Hausdorff and second countability by inheritance).** Both are inherited from $\mathbb{R}^{n^2}$ as a subspace.

---

# Hints

> [!note]- Hint 1
> Identify $M(n \times n, \mathbb{R})$ with $\mathbb{R}^{n^2}$ via the standard basis. Each matrix entry $a_{ij}$ becomes a coordinate of $\mathbb{R}^{n^2}$.

> [!note]- Hint 2
> The determinant $\det : M(n \times n, \mathbb{R}) \to \mathbb{R}$ is a polynomial in the $n^2$ matrix entries — explicitly, the Leibniz expansion $\det A = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_i a_{i, \sigma(i)}$ is a homogeneous polynomial of degree $n$. Polynomials are continuous.

> [!note]- Hint 3
> $\mathbb{R} \setminus \{0\}$ is open in $\mathbb{R}$. The preimage of an open set under a continuous function is open.

---

# Solution

The solution is one step: invoke the [[Thm - Open Subset of a Smooth Manifold]] after verifying that $\mathrm{GL}(n, \mathbb{R})$ is open in $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$.

**Step 1: $\mathrm{GL}(n, \mathbb{R})$ is an open subset of $\mathbb{R}^{n^2}$.**

Identify $M(n \times n, \mathbb{R})$ with $\mathbb{R}^{n^2}$ via the standard basis. The determinant function $\det : \mathbb{R}^{n^2} \to \mathbb{R}$ is a polynomial in the $n^2$ matrix entries, hence continuous. The set $\mathbb{R} \setminus \{0\}$ is open in $\mathbb{R}$. Therefore $\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ is open in $\mathbb{R}^{n^2}$.

> [!note]- Derivation
> *$\det$ is a polynomial.* By the Leibniz formula, $\det A = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) a_{1, \sigma(1)} a_{2, \sigma(2)} \cdots a_{n, \sigma(n)}$, a sum of products of matrix entries — a polynomial in the $n^2$ variables $\{a_{ij}\}$. Polynomial functions on $\mathbb{R}^{n^2}$ are smooth (in particular continuous).
>
> *Preimage of an open set under a continuous function is open.* This is a basic property of continuous maps in topology.
>
> *Conclusion.* $\mathrm{GL}(n, \mathbb{R})$ is open in $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$.

**Step 2: $\mathrm{GL}(n, \mathbb{R})$ inherits a smooth $n^2$-manifold structure from $\mathbb{R}^{n^2}$.**

By [[Thm - Open Subset of a Smooth Manifold]] applied to $M = \mathbb{R}^{n^2}$ and $U = \mathrm{GL}(n, \mathbb{R})$, $\mathrm{GL}(n, \mathbb{R})$ is a smooth manifold of dimension $n^2$ — the dimension of the ambient space $\mathbb{R}^{n^2}$.

> [!note]- Derivation
> *Single-chart atlas.* The most economical smooth atlas on $\mathrm{GL}(n, \mathbb{R})$ is the single chart $(\mathrm{GL}(n, \mathbb{R}), \mathrm{id})$, where the identity map is to be understood as the restriction of the identity on $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$ to the open subset $\mathrm{GL}(n, \mathbb{R})$. The image is $\mathrm{GL}(n, \mathbb{R})$ itself, an open subset of $\mathbb{R}^{n^2}$. So a single chart suffices to cover $\mathrm{GL}(n, \mathbb{R})$, and that single chart has image an open subset of $\mathbb{R}^{n^2}$.
>
> *Maximal smooth atlas.* The smooth structure on $\mathrm{GL}(n, \mathbb{R})$ inherited from $\mathbb{R}^{n^2}$ contains every chart smoothly compatible with the standard structure on $\mathbb{R}^{n^2}$, in particular every diffeomorphism of an open subset of $\mathrm{GL}(n, \mathbb{R})$ with an open subset of $\mathbb{R}^{n^2}$.

> [!note]- Complete formal solution
> **Claim.** $\mathrm{GL}(n, \mathbb{R})$ is a smooth manifold of dimension $n^2$.
>
> *Proof.* Identify the space of $n \times n$ real matrices $M(n \times n, \mathbb{R})$ with $\mathbb{R}^{n^2}$ via the standard basis. With this identification, $\mathbb{R}^{n^2}$ has the standard smooth $n^2$-manifold structure.
>
> The determinant $\det : \mathbb{R}^{n^2} \to \mathbb{R}$ is given by the Leibniz formula
> $$\det A = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{i=1}^n a_{i, \sigma(i)},$$
> a polynomial of degree $n$ in the $n^2$ matrix entries. Polynomials are smooth, in particular continuous.
>
> The set $\mathbb{R} \setminus \{0\}$ is open in $\mathbb{R}$. By continuity of $\det$, the preimage
> $$\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\}) = \{A \in M(n \times n, \mathbb{R}) : \det A \neq 0\}$$
> is open in $M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$.
>
> By [[Thm - Open Subset of a Smooth Manifold]], $\mathrm{GL}(n, \mathbb{R})$ is a smooth manifold of dimension $n^2$, with smooth structure inherited from $\mathbb{R}^{n^2}$. A single global chart (the inclusion $\mathrm{GL}(n, \mathbb{R}) \hookrightarrow M(n \times n, \mathbb{R}) \cong \mathbb{R}^{n^2}$ given by restricting the standard coordinates) is enough. $\blacksquare$

> [!warning] Sanity-check: $\mathrm{GL}(n, \mathbb{R})$ is *not* connected
> Although $\mathrm{GL}(n, \mathbb{R})$ is a smooth $n^2$-manifold, it is *not connected*. It has two connected components:
> $$\mathrm{GL}^+(n, \mathbb{R}) = \{\det > 0\}, \quad \mathrm{GL}^-(n, \mathbb{R}) = \{\det < 0\}.$$
> Each component is itself open in $\mathbb{R}^{n^2}$ (the open submanifold theorem applies to each), and each is a smooth manifold of dimension $n^2$. The identity matrix $I$ is in $\mathrm{GL}^+$ (since $\det I = 1$); the matrix $\mathrm{diag}(-1, 1, \dots, 1)$ is in $\mathrm{GL}^-$ (det $= -1$). For complex matrices, $\mathrm{GL}(n, \mathbb{C}) = \{A \in M(n, \mathbb{C}) : \det A \neq 0\}$ is connected (the complex determinant takes values in $\mathbb{C} \setminus \{0\}$, which is connected).

---

# Key Takeaways

**The trigger pattern: "open subset of a smooth manifold" — instant smooth structure.** Whenever you encounter a space defined by a *strict* inequality involving continuous functions on a known smooth manifold — $\{f > 0\}$, $\{f \neq 0\}$, $\{f < c\}$, intersections of these — the open-submanifold theorem ([[Thm - Open Subset of a Smooth Manifold]]) immediately gives a smooth manifold of the same dimension as the ambient one. No further work is needed; the smooth structure is inherited. This is the cheapest construction in the chapter, and is the source of essentially all matrix Lie groups as smooth manifolds.

**Strict inequality cuts out an open set; equality cuts out a closed lower-dimensional submanifold.** The transition from $\det A \neq 0$ (an *inequality*) to $\det A = 1$ (an *equality*) takes you from $\mathrm{GL}(n, \mathbb{R})$ (open, dimension $n^2$) to $\mathrm{SL}(n, \mathbb{R})$ (closed, dimension $n^2 - 1$). The smooth structure is no longer inherited from the open-submanifold theorem; instead, it requires the *regular value theorem* ([[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]). This is the fundamental distinction between *open* submanifolds (this exercise) and *closed embedded* submanifolds (developed in DG IV).

**Once $\mathrm{GL}(n, \mathbb{R})$ is a smooth manifold, the rest of matrix Lie theory follows.** The general linear group is the *prototype matrix Lie group*. From this exercise, the following all follow with minimal extra work:
- $\mathrm{GL}(n, \mathbb{C}) = \det^{-1}(\mathbb{C} \setminus \{0\}) \subseteq M(n, \mathbb{C}) \cong \mathbb{R}^{2n^2}$ is a smooth manifold of (real) dimension $2n^2$ — same argument with complex matrices.
- $\mathrm{GL}^+(n, \mathbb{R}) = \det^{-1}((0, \infty))$ is a smooth manifold of dimension $n^2$ — its identity component.
- The space of *upper-triangular invertible matrices* and the space of *invertible diagonal matrices* are smooth manifolds (open subsets of corresponding affine subspaces of $M(n, \mathbb{R})$).
The whole landscape of matrix Lie groups built from $\mathrm{GL}$ via further restrictions (equality constraints, leading to submanifolds via the regular value theorem) is in [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]].

**The dimension of $\mathrm{GL}(n, \mathbb{R})$ is $n^2$ — every entry is independent.** $n^2$ is the dimension of the *ambient* matrix space, and openness preserves it. This is the analytical intuition: at a generic invertible matrix $A$, you can perturb each of the $n^2$ entries independently and stay invertible (since the determinant is a nonzero polynomial, hence its zero set has codimension at least $1$). The full $n^2$-dimensional neighbourhood of $A$ in $\mathrm{GL}$ is genuine. Compare: $\mathrm{SL}(n) = \{A : \det A = 1\}$ has dimension $n^2 - 1$ (one constraint), $\mathrm{O}(n) = \{A : A^T A = I\}$ has dimension $\frac{n(n-1)}{2}$ (the constraint $A^T A = I$ gives $\frac{n(n+1)}{2}$ equations, so codimension is $\frac{n(n+1)}{2}$ when the constraints are independent).
