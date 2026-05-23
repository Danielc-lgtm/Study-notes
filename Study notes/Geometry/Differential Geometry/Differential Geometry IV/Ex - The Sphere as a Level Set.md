---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Embedded Submanifold"
  - "Def - Regular and Critical Points"
  - "Def - Tangent Space of a Submanifold"
  - "Thm - Regular Value Theorem on Manifolds"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that the unit $n$-sphere
$$S^n = \{x \in \mathbb{R}^{n+1} : |x|^2 = 1\}$$
is an embedded smooth submanifold of $\mathbb{R}^{n+1}$ of [[Def - Dimension|dimension]] $n$, by applying the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] to the function $f(x) = |x|^2$. Compute the tangent space $T_p S^n$ explicitly as a [[Def - Subspace|subspace]] of $T_p \mathbb{R}^{n+1} \cong \mathbb{R}^{n+1}$, and verify that it is the orthogonal complement of $p$.

**Recall:**

![[Thm - Regular Value Theorem on Manifolds#Statement]]

A point $p \in M$ is a [[Def - Regular and Critical Points|regular point]] of $\Phi : M \to N$ if $d\Phi_p$ is surjective; a value $c \in N$ is a regular value if every point of $\Phi^{-1}(c)$ is regular. By [[Thm - Regular Value Theorem on Manifolds]], a regular level set $\Phi^{-1}(c)$ is a properly embedded submanifold with $T_p \Phi^{-1}(c) = \ker d\Phi_p$.

---

# Convergent Strategy

**Problem class:** This is the simplest kind of regular value theorem application — verifying a candidate submanifold (the sphere) is indeed an embedded submanifold by showing it is a regular level set of an explicit smooth function. It belongs to the "submanifold from level set" class identified in the topic's [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds#Problem-Solving Strategy|problem-solving strategy]]. The route is: write down the defining function, compute the differential, check surjectivity at every point of the level set, conclude.

**Assumption pattern:** The level set $\{|x|^2 = 1\}$ is described by a single equation in $n + 1$ unknowns. The defining function $f(x) = |x|^2$ has codomain $\mathbb{R}$, so the surjectivity of $df_p$ at a point of the level set is just "$df_p \neq 0$", i.e., the gradient does not vanish on the sphere. This is the simplest scalar case of the regular value theorem.

**Theorem routing:** The route is single-step: $\{f = 1\}$ for $f(x) = |x|^2$, with $df_p \neq 0$ on the sphere (since $df_p(v) = 2 p \cdot v$, which is nonzero as long as $p \neq 0$ — and $p \neq 0$ on the sphere since $|p| = 1$). Hence by [[Thm - Regular Value Theorem on Manifolds]], $S^n$ is an embedded submanifold of codimension $1$ in $\mathbb{R}^{n+1}$, with tangent space $T_p S^n = \ker df_p = \{v : p \cdot v = 0\}$ — the orthogonal complement of $p$.

**Key decision point:** There is no "key decision point" — this is the canonical first example of the regular value theorem, and the only choice is to use $f(x) = |x|^2$ (rather than, say, $|x| - 1$, which is not differentiable at the origin but is at the sphere). The choice of $f$ matters: $|x|^2$ is smooth on all of $\mathbb{R}^{n+1}$, while $|x|$ is not smooth at the origin (the origin is not on the sphere, but having a smooth defining function on a neighbourhood is cleaner). The "smoothness needed only near the level set" subtlety is one to remember in harder problems.

---

# Legal Operations Used

1. **Operation 2 from the topic page (apply the regular value theorem):** the entire solution is a single application of this operation. Write the sphere as a level set of an explicit smooth function, check the differential is surjective everywhere on the level set, conclude submanifold structure and tangent space.

2. **Operation 1 (compute the differential in coordinates):** in computing $df_p$ for $f(x) = |x|^2 = \sum_i x_i^2$, the differential is $df_p = (2x_1, \dots, 2x_{n+1})\big|_p = 2 \langle p, \cdot \rangle$. This is the standard Jacobian computation for a scalar function on $\mathbb{R}^{n+1}$.

---

# Hints

> [!note]- Hint 1
> What smooth function $f : \mathbb{R}^{n+1} \to \mathbb{R}$ has the unit sphere as a level set? Pick the simplest one.

> [!note]- Hint 2
> Compute $df_p$ for your chosen $f$. Where does $df_p$ vanish?

> [!note]- Hint 3
> The set where $df_p$ vanishes is the critical set of $f$. Check whether any critical point lies on the sphere. If not, $1$ is a regular value, and the regular value theorem applies.

> [!note]- Hint 4
> For the tangent space, recall that the tangent space of a regular level set at $p$ is the kernel of $d\Phi_p$. For your $f$, what is $\ker df_p$ explicitly?

---

# Solution

The proof breaks into three short steps. Step 1 identifies the sphere as a level set of $f(x) = |x|^2$. Step 2 computes the differential and verifies it is nonzero on the level set. Step 3 applies the regular value theorem to conclude both the submanifold structure and the tangent space.

**Step 1: $S^n$ is the level set $\{f = 1\}$ for $f : \mathbb{R}^{n+1} \to \mathbb{R}$, $f(x) = |x|^2$.**

> [!note]- Derivation
> The function $f(x) = |x|^2 = x_1^2 + \dots + x_{n+1}^2$ is smooth on all of $\mathbb{R}^{n+1}$ (it is a polynomial). The unit sphere is by definition $\{x : |x|^2 = 1\}$, which is $f^{-1}(1)$. So the sphere is the level set of $f$ at the value $1$.

**Step 2: $df_p$ is nonzero at every point of $S^n$.**

> [!note]- Derivation
> The differential of $f(x) = \sum_i x_i^2$ at $p = (p_1, \dots, p_{n+1})$ is
> $$df_p(v) = \sum_i 2 p_i v_i = 2 \langle p, v \rangle,$$
> where $\langle \cdot, \cdot \rangle$ is the standard inner product on $\mathbb{R}^{n+1}$. In matrix form, the Jacobian is the row vector $Df(p) = (2p_1, \dots, 2p_{n+1}) = 2 p^T$.
>
> The differential $df_p$ vanishes iff $p = 0$ — that is, $f$'s unique critical point is the origin. Since the origin is *not* on the sphere ($|0|^2 = 0 \neq 1$), $df_p \neq 0$ at every point $p$ of the sphere. So every point of $S^n$ is a regular point of $f$, hence $1$ is a regular value of $f$.

**Step 3: Apply the regular value theorem.**

> [!note]- Derivation
> By [[Thm - Regular Value Theorem on Manifolds]] (with $M = \mathbb{R}^{n+1}$, $N = \mathbb{R}$, $\Phi = f$, $c = 1$), the level set $S^n = f^{-1}(1)$ is a properly embedded smooth submanifold of $\mathbb{R}^{n+1}$ of codimension $\dim N = 1$, hence of dimension $(n+1) - 1 = n$. The tangent space at any $p \in S^n$ is
> $$T_p S^n = \ker df_p = \{v \in \mathbb{R}^{n+1} : 2 \langle p, v \rangle = 0\} = \{v \in \mathbb{R}^{n+1} : \langle p, v \rangle = 0\}.$$
> This is the orthogonal complement of $p$ in $\mathbb{R}^{n+1}$ — an $n$-dimensional linear subspace.
>
> The sphere is also **properly** embedded because it is closed in $\mathbb{R}^{n+1}$ (continuous preimage of the closed singleton $\{1\}$) and is in fact compact (closed and bounded).

> [!note]- Complete formal solution
> Define $f : \mathbb{R}^{n+1} \to \mathbb{R}$ by $f(x) = |x|^2 = \sum_{i=1}^{n+1} x_i^2$. Then $f$ is smooth (polynomial), and $S^n = f^{-1}(1)$.
>
> The differential of $f$ at $p$ is $df_p(v) = 2 \langle p, v \rangle$, so $df_p$ vanishes iff $p = 0$. Since $0 \notin S^n$ (because $|0| = 0 \neq 1$), $df_p \neq 0$ at every $p \in S^n$, meaning every $p \in S^n$ is a regular point of $f$. So $1$ is a regular value of $f$.
>
> By [[Thm - Regular Value Theorem on Manifolds]], $S^n = f^{-1}(1)$ is a properly embedded smooth submanifold of $\mathbb{R}^{n+1}$ of codimension $\dim \mathbb{R} = 1$, hence of dimension $n$. The tangent space at $p \in S^n$ is
> $$T_p S^n = \ker df_p = \{v \in \mathbb{R}^{n+1} : \langle p, v \rangle = 0\} = p^\perp,$$
> the orthogonal complement of $p$ in $\mathbb{R}^{n+1}$. $\qquad\blacksquare$

---

# Key Takeaways

**The simplest level-set construction.** This exercise is the canonical first illustration of the regular value theorem. The pattern — write the candidate submanifold as a level set, compute the differential, check it is surjective at every preimage point, conclude — is the most-used routine in submanifold theory. Whenever you encounter a candidate submanifold defined by a single equation (a hypersurface), this is the technique. The variations come in choosing the defining function (sometimes there are multiple natural choices, like $|x|$ vs $|x|^2$, and the choice affects smoothness on the ambient space) and in handling multiple equations (where the differential is a Jacobian matrix and "surjective" means "rows linearly independent"). The basic strategy is unchanged across these variations.

**Tangent space as kernel — the most efficient computation.** The identification $T_p S^n = \ker df_p$ is the most computationally direct tangent-space characterisation, and this exercise illustrates it at its simplest: $df_p(v) = 2\langle p, v\rangle$, so $\ker df_p = p^\perp$. For more elaborate submanifolds (matrix [[Def - Group|groups]], intersections of hypersurfaces), the same approach works — the differential is a linear map between tangent spaces of the ambient and the codomain, and its kernel is the tangent space of the submanifold. This is the workhorse for tangent space computations in Lie theory: $T_I \mathrm{O}(n)$, $T_I \mathrm{SL}(n)$, etc., are all kernels of differentials of defining maps. The lesson: when a submanifold is described implicitly, use the kernel formula; when described parametrically, use the image formula; when the description is mixed, use whichever is easier.

**The orthogonal complement appears naturally.** The tangent space to the sphere at a point is the orthogonal complement of the position vector — a geometric fact familiar from vector calculus, here recovered from the abstract regular value theorem. This is one of the cleanest illustrations of the principle that **the geometry of the submanifold is encoded in the differential of the defining map**: $\nabla f$ at a point is normal to the level set there, so the level set's tangent space is the perpendicular space. For more general defining maps $\Phi : M \to N$ with $\dim N > 1$, the analogous statement is that the **rows of the Jacobian span the normal space**, and the level set's tangent space is the orthogonal complement of these rows. The single-row case is just the gradient.

**Cross-link to companion exercises.** This is the prototype; [[Ex - The Special Linear Group is a Submanifold of GL(n)|Ex - The Special Linear Group is a Submanifold of GL(n)]] and [[Ex - The Orthogonal Group as a Regular Level Set]] develop the matrix-group analogues, and [[Ex - The Hopf Map is a Submersion]] uses the same theorem in the opposite direction (proving a map is a submersion using the level-set structure).
