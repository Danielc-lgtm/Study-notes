---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Def - Brouwer Degree of a Map"
tags: [geometry, topology, index]
---

# Notation

Let $M$ be an oriented smooth $n$-manifold, $v\in\mathfrak X(M)$, and let $p$ be an isolated zero of $v$.

# The Definition

> [!definition] Local index
> Choose an oriented chart $x:U\to\mathbb R^n$ with $x(p)=0$ and a closed ball $\overline B_\varepsilon\subset x(U)$ containing no other zero. Write the coordinate components of $v$ as $V:x(U)\to\mathbb R^n$. The **index** of $v$ at $p$ is
> $$
> \operatorname{ind}_p(v)=\deg\!\left(
> S_\varepsilon^{n-1}\longrightarrow S^{n-1},
> \quad y\longmapsto\frac{V(y)}{\lVert V(y)\rVert}
> \right).
> $$

The definition is independent of the oriented chart and sufficiently small ball. Indeed, changing oriented coordinates changes the normalized map on domain and target by maps of equal local orientation sign, so the two degree factors cancel. Shrinking the ball gives a homotopic normalized map through an annulus on which $v$ never vanishes.

For an unoriented manifold, use a local orientation consistently on both the domain sphere and fibre coordinates; reversing it reverses both and leaves the integer unchanged.

# Operational Characterizations

On an oriented surface, the index is the winding number of the vector direction along a small positively oriented circle. If the zero is nondegenerate, so $D V(0)$ is invertible, homotopy to the linearization gives
$$
\operatorname{ind}_p(v)=\operatorname{sgn}\det D V(0).
$$
The homotopy is valid on a sufficiently small sphere because
$V(y)=D V(0)y+o(\lVert y\rVert)$ and the invertible linear term has a positive lower bound there.

# Examples / Corollaries

In $\mathbb R^2$, a source $(x,y)$ and a sink $(-x,-y)$ have index $+1$, while the saddle $(x,-y)$ has index $-1$. The field corresponding to $z\mapsto z^m$ has index $m$, showing that degenerate zeros can have arbitrary integer index.

# Unlocked by This

Local index is stable under perturbations supported away from the boundary of the isolating ball. Its global sum on a closed surface is computed by [[Thm - Poincare-Hopf Theorem]].
