---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - The Regular Value Theorem"
  - "Def - Submanifold of Euclidean Space"
  - "Def - The Tangent Space to a Submanifold"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $S^{n-1} = \{x \in \mathbb{R}^n : |x|^2 = 1\}$ be the unit sphere.

1. Show that $S^{n-1}$ is a smooth $(n-1)$-dimensional submanifold of $\mathbb{R}^n$, by exhibiting it as a regular level set.
2. Determine the tangent space $T_p S^{n-1}$ at an arbitrary point $p \in S^{n-1}$, and the normal direction.
3. Explain why the level set $\{|x|^2 = 0\}$ is *not* a submanifold of dimension $n-1$ — what goes wrong, and where?

**Recall:**

The objects in play are the regular value, the regular value theorem, and the tangent space.

![[Thm - The Regular Value Theorem#Statement]]

By the [[Thm - The Regular Value Theorem|regular value theorem]], if $c$ is a regular value of $f \in C^k(U, \mathbb{R}^{n-d})$ — meaning $Df_p$ is surjective at every $p$ with $f(p) = c$ — then $f^{-1}(c)$ is a $d$-dimensional $C^k$ [[Def - Submanifold of Euclidean Space|submanifold]], with [[Def - The Tangent Space to a Submanifold|tangent space]] $T_p f^{-1}(c) = \ker Df_p$. For a *scalar* function $f : \mathbb{R}^n \to \mathbb{R}$, the derivative $Df_p$ is surjective onto $\mathbb{R}$ exactly when it is nonzero, i.e. when the gradient $\nabla f(p) \neq 0$. So a scalar level set is a hypersurface of dimension $n-1$ wherever the gradient does not vanish on it.

---

# Convergent Strategy

**Problem class.** This is a *manifold-structure* problem: present a set as a level set and certify it is a submanifold. The [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic strategy]] gives the route — write the set as $f^{-1}(c)$, check $c$ is a regular value by a pointwise rank computation, read off the dimension and tangent space.

**Assumption pattern.** The sphere is a scalar level set, $\{f = 1\}$ for $f(x) = |x|^2$. The defining function is a single quadratic, so the rank check reduces to "is the gradient nonzero?".

**Theorem routing.** Compute $\nabla f = 2x$; observe it is nonzero at every point of the sphere (since $x \neq 0$ there); conclude $1$ is a regular value; apply the [[Thm - The Regular Value Theorem|regular value theorem]] to get an $(n-1)$-dimensional submanifold with $T_p S^{n-1} = \ker Df_p$.

**Key decision point.** The instructive contrast is Part 3: the *same* function $f = |x|^2$ has $0$ as a *critical* value, because $\nabla f(0) = 0$ and the origin lies on $\{f = 0\}$. So whether a level set is a submanifold depends not on the function alone but on the *value* — and the regular value theorem is silent at critical values. Recognizing that the value, not just the function, must be checked is the point.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Check that a value is regular, then declare the level set a manifold.** Compute $\nabla f$, verify it is nonzero on the level set, conclude $1$ is a regular value and apply the regular value theorem.

2. **Compute a tangent space as a kernel.** The tangent space is $\ker Df_p$ — the directions in which $|x|^2$ does not change to first order.

3. **Diagnose a critical value where the theorem fails.** Identify where $\nabla f = 0$ and check whether that point lies on the level set in question.

---

# Hints

> [!note]- Hint 1
> Write the sphere as $\{f = 1\}$ for $f(x) = |x|^2 = x_1^2 + \dots + x_n^2$. Compute $\nabla f$.

> [!note]- Hint 2
> $\nabla f(x) = 2x$. On the sphere, $|x| = 1$, so $x \neq 0$, hence $\nabla f(x) = 2x \neq 0$ at every point of the sphere. What does the regular value theorem then conclude?

> [!note]- Hint 3
> The derivative is $Df_p(v) = \nabla f(p)\cdot v = 2\langle p, v\rangle$. The tangent space is $\ker Df_p = \{v : \langle p, v\rangle = 0\}$. Geometrically, which vectors are orthogonal to $p$?

> [!note]- Hint 4
> For Part 3: the value $0$ is different. The level set $\{|x|^2 = 0\}$ is just $\{0\}$, a single point. And $\nabla f(0) = 0$ — the origin, which lies on this level set, is a critical point. So $0$ is a critical value, and the regular value theorem does not apply.

---

# Solution

The sphere is the level set $\{|x|^2 = 1\}$, and its defining function has gradient $2x$, which is nonzero on the sphere. So $1$ is a regular value, the regular value theorem applies in one line, and the tangent space drops out as the hyperplane orthogonal to the radius.

**Step 1: The sphere is an $(n-1)$-dimensional submanifold.**

With $f(x) = |x|^2$, the value $1$ is a regular value of $f$, so $S^{n-1} = f^{-1}(1)$ is a smooth $(n-1)$-dimensional submanifold of $\mathbb{R}^n$.

> [!note]- Derivation
> Let $f : \mathbb{R}^n \to \mathbb{R}$, $f(x) = |x|^2 = x_1^2 + \dots + x_n^2$. This is a polynomial, hence $C^\infty$, and $S^{n-1} = \{x : f(x) = 1\} = f^{-1}(1)$.
>
> The gradient is $\nabla f(x) = (2x_1, \dots, 2x_n) = 2x$, so the derivative $Df_x : \mathbb{R}^n \to \mathbb{R}$ is $Df_x(v) = 2\langle x, v\rangle$. For a scalar-valued $f$, $Df_x$ is surjective onto $\mathbb{R}$ exactly when it is not the zero map, i.e. when $\nabla f(x) \neq 0$.
>
> At every point $x \in S^{n-1}$ we have $|x| = 1 \neq 0$, so $x \neq 0$, so $\nabla f(x) = 2x \neq 0$. Therefore $Df_x$ is surjective at *every* point of the level set $f^{-1}(1)$, which is the definition of $1$ being a **regular value** of $f$.
>
> By the [[Thm - The Regular Value Theorem|regular value theorem]], $f^{-1}(1) = S^{n-1}$ is a $C^\infty$ submanifold of $\mathbb{R}^n$ of dimension $n - (n - d)$ where the codomain has dimension $n - d = 1$, so $d = n - 1$. The sphere $S^{n-1}$ is an $(n-1)$-dimensional smooth submanifold.

**Step 2: The tangent space is the hyperplane orthogonal to $p$.**

At $p \in S^{n-1}$, the tangent space is $T_p S^{n-1} = \{v \in \mathbb{R}^n : \langle p, v\rangle = 0\} = p^\perp$, the hyperplane through the origin orthogonal to $p$; the normal direction is $p$ itself.

> [!note]- Derivation
> By the [[Thm - The Regular Value Theorem|regular value theorem]], the tangent space is the kernel of the derivative:
> $$T_p S^{n-1} = \ker Df_p = \{v \in \mathbb{R}^n : Df_p(v) = 0\} = \{v : 2\langle p, v\rangle = 0\} = \{v : \langle p, v\rangle = 0\}.$$
> This is the set of vectors orthogonal to $p$ — the hyperplane $p^\perp$ through the origin, of dimension $n - 1$, consistent with the manifold dimension.
>
> Geometrically this is exactly right: a vector is tangent to the sphere at $p$ precisely when it is perpendicular to the radius $p$. Intuitively, moving along the sphere keeps $|x|$ constant, so it does not change the distance to the origin to first order, so it has no radial component — it is orthogonal to $p$. The normal space $(T_p S^{n-1})^\perp$ is the line $\mathbb{R}p$ spanned by $p$, and the normal direction is the radius vector $p$ — also the gradient direction $\nabla f(p) = 2p$.

**Step 3: Why $\{|x|^2 = 0\}$ is not an $(n-1)$-submanifold.**

The level set $f^{-1}(0)$ is the single point $\{0\}$, and $0$ is a *critical* value of $f$: the gradient $\nabla f(0) = 0$ vanishes at the origin, which lies on this level set. The regular value theorem does not apply, and indeed a point is not an $(n-1)$-dimensional submanifold.

> [!note]- Derivation
> $f^{-1}(0) = \{x : |x|^2 = 0\} = \{0\}$, since $|x|^2 = 0$ forces $x = 0$. The regular value theorem requires $0$ to be a *regular* value — $\nabla f$ nonzero at every point of $f^{-1}(0)$. But the only point of $f^{-1}(0)$ is the origin, and $\nabla f(0) = 2\cdot 0 = 0$. The gradient *vanishes* at the unique point of the level set, so $0$ is a **critical value** and the [[Thm - The Regular Value Theorem|regular value theorem]] is silent.
>
> And the conclusion the theorem would have given is genuinely false: $\{0\}$ is a single point, which is a $0$-dimensional submanifold, *not* an $(n-1)$-dimensional one. The dimension formula "$d = n - 1$" derived for a regular value of a scalar function simply does not hold at the critical value $0$. This is the lesson: whether $f^{-1}(c)$ is an $(n-1)$-submanifold depends on the *value* $c$, not only on the function $f$ — the same $f = |x|^2$ gives a smooth sphere at $c = 1$ and a degenerate point at $c = 0$.
>
> (More dramatically, for $g(x,y) = x^2 - y^2$ the value $0$ is critical because $\nabla g(0,0) = 0$, and $g^{-1}(0)$ is two crossing lines — not a manifold at the crossing. The sphere's defining function is gentler: its only critical value is $0$, and the corresponding level set happens to be a single point rather than something self-crossing.)

> [!note]- Complete formal solution
> Let $f(x) = |x|^2$, $C^\infty$ on $\mathbb{R}^n$. Then $S^{n-1} = f^{-1}(1)$ and $\nabla f(x) = 2x$.
>
> *Part 1.* On $S^{n-1}$, $|x| = 1$ so $x \neq 0$, hence $\nabla f(x) = 2x \neq 0$; the scalar derivative $Df_x$ is therefore surjective at every point of $f^{-1}(1)$, so $1$ is a regular value. By the [[Thm - The Regular Value Theorem|regular value theorem]], $S^{n-1}$ is a $C^\infty$ submanifold of dimension $n - 1$.
>
> *Part 2.* $T_p S^{n-1} = \ker Df_p = \{v : 2\langle p,v\rangle = 0\} = p^\perp$, the hyperplane orthogonal to $p$; the normal direction is $p$.
>
> *Part 3.* $f^{-1}(0) = \{0\}$, and $\nabla f(0) = 0$, so $0$ is a critical value — the regular value theorem does not apply, and indeed $\{0\}$ is a $0$-dimensional, not $(n-1)$-dimensional, set. $\blacksquare$

---

# Key Takeaways

**Presenting a set as a regular level set is the standard, near-effortless way to prove it is a submanifold.** The entire argument for the sphere is: name the defining function $f = |x|^2$, compute its gradient $2x$, observe the gradient is nonzero on the level set, invoke the [[Thm - The Regular Value Theorem|regular value theorem]]. No charts are constructed, no parametrizations checked — a single gradient computation does everything, and it simultaneously delivers the dimension ($n$ minus the number of equations) and the tangent space (the kernel of the derivative). Whenever a set is presented by an equation, this is the first thing to try, and it almost always works.

**For a scalar function, "regular value" means "nonvanishing gradient on the level set" — surjectivity onto $\mathbb{R}$ is just nonzero-ness.** The abstract hypothesis of the regular value theorem is "$Df_p$ surjective", and for a map into $\mathbb{R}^{n-d}$ this is a rank condition on a matrix. But when the codomain is one-dimensional — a single equation — surjectivity onto $\mathbb{R}$ collapses to the derivative being nonzero, i.e. $\nabla f \neq 0$. So every level surface of a scalar function is automatically a smooth hypersurface *wherever its gradient does not vanish*. This is the most common case, and recognizing that "maximal rank" degenerates to "gradient nonzero" makes the check trivial.

**Whether a level set is a manifold depends on the value, not just the function — and the regular value theorem is silent at critical values.** The same function $f = |x|^2$ gives a smooth $(n-1)$-sphere at the value $1$ and a degenerate single point at the value $0$. The difference is entirely in the value: $1$ is regular, $0$ is critical because the gradient vanishes at the one point of $f^{-1}(0)$. The discipline, flagged on the topic page as an illegal-but-tempting move, is to never call a level set a submanifold without checking the *specific value*: locate the critical points of $f$ (where $\nabla f = 0$) and confirm none of them lie on the level set you care about. Where a critical point sits on the level set, expect — and find — a singular point: a pinch, a crossing, a degenerate point.

**The tangent space to a level set is the orthogonal complement of the gradient, and this geometry is universal.** For the sphere, $T_p S^{n-1} = p^\perp$ and the normal is the radius — but the underlying fact is general: for any regular level set $\{f = c\}$, the tangent space is $\ker Df_p$ and the normal direction is $\nabla f(p)$. The gradient always points perpendicular to the level set. This is the geometric content that makes the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]] work — the constraint gradients span the normal space — and it is worth carrying as a single picture: gradient ⟂ level set, tangent space = everything orthogonal to the gradient.
