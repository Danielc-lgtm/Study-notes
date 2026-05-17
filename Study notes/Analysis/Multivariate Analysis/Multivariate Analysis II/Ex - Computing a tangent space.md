---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - The Tangent Space to a Submanifold"
  - "Def - Submanifold of Euclidean Space"
  - "Thm - The Regular Value Theorem"
  - "Thm - The Chain Rule"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider the surface $M \subseteq \mathbb{R}^3$ given as the level set
$$M = \{(x,y,z) \in \mathbb{R}^3 : x^2 + y^2 - z = 0\},$$
the paraboloid $z = x^2 + y^2$. Fix the point $p = (1, 1, 2) \in M$.

1. Confirm $M$ is a smooth $2$-dimensional submanifold and compute the tangent space $T_p M$ as the **kernel of the derivative** of the implicit defining function.
2. Compute $T_p M$ again as the **image of the derivative** of a parametrization.
3. Compute $T_p M$ a third time from the **graphical** description $z = g(x,y)$.
4. Verify that all three computations give the same $2$-dimensional subspace, and write down the tangent plane $p + T_p M$ and a normal vector.

**Recall:**

The objects in play are the three representations of a submanifold and the matching tangent-space formulas.

![[Def - The Tangent Space to a Submanifold#The Definition]]

By [[Def - The Tangent Space to a Submanifold|the definition of the tangent space]], $T_p M$ is the set of velocities $\gamma'(0)$ of $C^1$ curves in $M$ through $p$; it is a $d$-dimensional linear subspace. It has two computational descriptions. **Implicit:** if $M = \{f = c\}$ near $p$ with $Df_p$ of maximal rank, then $T_p M = \ker Df_p$. **Parametric:** if $M = G(V)$ near $p$ with $G$ a maximal-rank parametrization and $G(y_0) = p$, then $T_p M = \operatorname{im} DG_{y_0}$. The graphical description is the special case of the parametric one with $G(x,y) = (x, y, g(x,y))$. By the [[Thm - The Regular Value Theorem|regular value theorem]], all these agree and equal the curve-defined tangent space.

---

# Convergent Strategy

**Problem class.** This is a *tangent-space computation* exercise, and it is calibrated to drill the *equivalence* of the three representations: the same subspace must come out three ways.

**Assumption pattern.** The surface is presented implicitly, $\{f = 0\}$ with $f = x^2 + y^2 - z$, but is *also* a graph ($z = x^2 + y^2$), hence trivially parametrizable. So all three descriptions are immediately available, and the exercise is to run all three and confirm agreement.

**Theorem routing.** Implicit route: $T_p M = \ker Df_p$, the kernel of the gradient. Parametric route: $T_p M = \operatorname{im}DG_p$, the column space of the parametrization's Jacobian. Graphical route: the tangent space is the graph of the linear map $Dg(1,1)$. The [[Thm - The Regular Value Theorem|regular value theorem]] guarantees these coincide.

**Key decision point.** There is no single hard step; the point is *procedural fluency*. Each representation hands you a *different formula* — a kernel, an image, a graph-of-derivative — and the skill is knowing which formula matches which description and executing each correctly. The verification that they agree is the calibration check that you have done each correctly.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Compute a tangent space as a kernel.** From the implicit description $M = \{f = 0\}$, $T_p M = \ker Df_p$.

2. **Compute a tangent space as an image.** From a parametrization $G$, $T_p M = \operatorname{im}DG$.

3. **Check that a value is regular.** Confirm $\nabla f \neq 0$ on $M$ so the regular value theorem applies.

4. **Differentiate to linearize a graph.** The tangent space to a graph is the graph of the derivative of the defining function.

---

# Hints

> [!note]- Hint 1
> Implicit route: $f(x,y,z) = x^2 + y^2 - z$, so $\nabla f = (2x, 2y, -1)$. At $p = (1,1,2)$, $\nabla f(p) = (2,2,-1)$ — nonzero, so $0$ is a regular value and $M$ is a smooth surface. $T_p M = \ker Df_p = \{(u,v,w) : 2u + 2v - w = 0\}$.

> [!note]- Hint 2
> Parametric route: parametrize $M$ by $G(s,t) = (s, t, s^2 + t^2)$, with $G(1,1) = p$. Compute $DG = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 2s & 2t\end{pmatrix}$, evaluate at $(1,1)$, and take the span of its columns.

> [!note]- Hint 3
> Graphical route: $z = g(x,y) = x^2 + y^2$. The tangent space to a graph is $\{(u, v, Dg(p)\cdot(u,v))\}$ where $Dg = (2x, 2y)$. At $(1,1)$, $Dg = (2,2)$, so $T_p M = \{(u, v, 2u + 2v)\}$.

> [!note]- Hint 4
> All three should give $\{(u,v,w) : w = 2u + 2v\}$. The kernel description $2u + 2v - w = 0$ is the same equation. The image description: columns $(1,0,2)$ and $(0,1,2)$ span exactly this plane. The normal is $\nabla f(p) = (2,2,-1)$.

---

# Solution

The paraboloid is presented implicitly, but it is also a graph, so all three descriptions of a submanifold are available at once. Each yields the tangent space by its own formula — a kernel, an image, a graph-of-derivative — and the three answers must, and do, coincide.

**Step 1: The implicit route — $T_p M = \ker Df_p$.**

With $f(x,y,z) = x^2 + y^2 - z$, the value $0$ is regular ($\nabla f(p) = (2,2,-1) \neq 0$), so $M$ is a smooth $2$-dimensional submanifold, and
$$T_p M = \ker Df_p = \{(u,v,w) \in \mathbb{R}^3 : 2u + 2v - w = 0\}.$$

> [!note]- Derivation
> Write $f(x,y,z) = x^2 + y^2 - z$, a $C^\infty$ function with $M = f^{-1}(0)$. The gradient is $\nabla f(x,y,z) = (2x, 2y, -1)$, and at every point of $M$ the third component is $-1 \neq 0$, so $\nabla f$ never vanishes on $M$ — the value $0$ is a regular value. By the [[Thm - The Regular Value Theorem|regular value theorem]], $M$ is a $2$-dimensional ($3 - 1$) $C^\infty$ submanifold.
>
> The derivative at $p = (1,1,2)$ is $Df_p(u,v,w) = \nabla f(p)\cdot(u,v,w) = 2u + 2v - w$, since $\nabla f(1,1,2) = (2,2,-1)$. The [[Def - The Tangent Space to a Submanifold|tangent space]] is the kernel:
> $$T_p M = \ker Df_p = \{(u,v,w) : 2u + 2v - w = 0\}.$$
> This is a plane through the origin in $\mathbb{R}^3$, of dimension $2$.

**Step 2: The parametric route — $T_p M = \operatorname{im}DG$.**

Parametrizing $M$ by $G(s,t) = (s, t, s^2 + t^2)$, the tangent space at $p = G(1,1)$ is the span of the columns of $DG(1,1)$:
$$T_p M = \operatorname{span}\{(1, 0, 2),\ (0, 1, 2)\}.$$

> [!note]- Derivation
> The map $G(s,t) = (s, t, s^2 + t^2)$ is a $C^\infty$ parametrization of $M$ (every point of the paraboloid is $G$ of its first two coordinates), with $G(1,1) = (1,1,2) = p$. Its Jacobian is
> $$DG(s,t) = \begin{pmatrix} \partial_s G_1 & \partial_t G_1 \\ \partial_s G_2 & \partial_t G_2 \\ \partial_s G_3 & \partial_t G_3\end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 2s & 2t\end{pmatrix}, \qquad DG(1,1) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 2 & 2\end{pmatrix}.$$
> This has rank $2$ (the top $2\times 2$ block is the identity), so $G$ is an immersion and $M$ is a $2$-dimensional submanifold. By the parametric formula for the [[Def - The Tangent Space to a Submanifold|tangent space]],
> $$T_p M = \operatorname{im}DG(1,1) = \{DG(1,1)\cdot(a,b) : (a,b) \in \mathbb{R}^2\} = \operatorname{span}\{(1,0,2),\ (0,1,2)\},$$
> the span of the two columns.

**Step 3: The graphical route — the tangent space is the graph of $Dg$.**

Writing $M$ as the graph $z = g(x,y) = x^2 + y^2$, the tangent space is the graph of the linear map $Dg(1,1)$:
$$T_p M = \{(u, v, 2u + 2v) : (u,v) \in \mathbb{R}^2\}.$$

> [!note]- Derivation
> The paraboloid is the graph of $g(x,y) = x^2 + y^2$. The tangent space to a graph at a point is the graph of the *derivative* of the defining function — the linearization. Here $Dg(x,y) = (2x, 2y)$, so $Dg(1,1) = (2,2)$, and
> $$T_p M = \{(u, v,\ Dg(1,1)\cdot(u,v)) : (u,v) \in \mathbb{R}^2\} = \{(u, v,\ 2u + 2v)\}.$$
> Intuitively: near $p$, $M$ is the graph $z = g(x,y)$, and its best linear approximation is the graph of the affine function $g(p) + Dg(p)\cdot((x,y)-(1,1))$; the tangent space (the linear part, based at the origin) is the graph of the *linear* map $Dg(p)$.

**Step 4: The three answers agree; the tangent plane and normal.**

All three computations describe the same plane $\{(u,v,w) : w = 2u + 2v\}$. The tangent plane is $p + T_p M = \{(x,y,z) : z - 2 = 2(x-1) + 2(y-1)\}$, i.e. $z = 2x + 2y - 2$, and a normal vector is $(2,2,-1)$.

> [!note]- Derivation
> *Agreement.* The implicit route gave $\{(u,v,w) : 2u + 2v - w = 0\}$, i.e. $w = 2u + 2v$. The graphical route gave $\{(u,v,2u+2v)\}$ — the same set. The parametric route gave $\operatorname{span}\{(1,0,2),(0,1,2)\}$; a general element is $a(1,0,2) + b(0,1,2) = (a, b, 2a+2b)$, which is exactly $\{(u,v,2u+2v)\}$ with $u = a, v = b$. So all three descriptions yield the identical $2$-dimensional subspace
> $$T_p M = \{(u,v,w) : w = 2u + 2v\}.$$
> This agreement is guaranteed in advance by the [[Thm - The Regular Value Theorem|regular value theorem]] and the equivalence of the [[Def - Submanifold of Euclidean Space|submanifold representations]]; computing all three is a calibration check that each was done correctly.
>
> *Tangent plane.* The tangent plane is the *affine* subspace through $p$ parallel to $T_p M$:
> $$p + T_p M = \{(1,1,2) + (u,v,2u+2v)\} = \{(x,y,z) : (z - 2) = 2(x - 1) + 2(y - 1)\},$$
> which simplifies to $z = 2x + 2y - 2$.
>
> *Normal vector.* The normal space is $(T_p M)^\perp$. From the implicit route the tangent space is the kernel of the gradient, so the normal direction is the gradient itself: $\nabla f(p) = (2, 2, -1)$. Check: $(2,2,-1)\cdot(1,0,2) = 2 - 2 = 0$ and $(2,2,-1)\cdot(0,1,2) = 2 - 2 = 0$, so $(2,2,-1)$ is orthogonal to both spanning vectors of $T_p M$, confirming it is normal.

> [!note]- Complete formal solution
> $M = \{f = 0\}$, $f(x,y,z) = x^2+y^2-z$.
>
> *Implicit.* $\nabla f = (2x,2y,-1)$, never zero on $M$, so $0$ is regular and $M$ is a $C^\infty$ $2$-submanifold. $T_p M = \ker Df_p = \{(u,v,w) : 2u+2v-w = 0\}$.
>
> *Parametric.* $G(s,t) = (s,t,s^2+t^2)$, $G(1,1) = p$, $DG(1,1) = \begin{pmatrix}1&0\\0&1\\2&2\end{pmatrix}$, rank $2$. $T_p M = \operatorname{im}DG(1,1) = \operatorname{span}\{(1,0,2),(0,1,2)\}$.
>
> *Graphical.* $z = g(x,y) = x^2+y^2$, $Dg(1,1) = (2,2)$. $T_p M = \{(u,v,2u+2v)\}$.
>
> *Agreement.* All three equal $\{(u,v,w) : w = 2u+2v\}$. Tangent plane $z = 2x+2y-2$; normal $\nabla f(p) = (2,2,-1)$. $\blacksquare$

---

# Key Takeaways

**Each representation of a submanifold hands you the tangent space by its own formula — kernel, image, or graph-of-derivative — and you must match the formula to the representation.** An implicit description $\{f = c\}$ gives $T_p M = \ker Df_p$: the tangent space is what the linearized constraint *kills*. A parametric description $G(V)$ gives $T_p M = \operatorname{im}DG$: the tangent space is what the linearized parametrization *reaches*. A graphical description $z = g(x)$ gives the tangent space as the *graph of $Dg$*: the linearization of the function. These are three genuinely different computations — solving a homogeneous equation, taking a column span, graphing a derivative — and fluency means executing whichever the problem hands you without confusion. The kernel route is usually fastest when the set is a level set; the image route when it is parametrized.

**Kernel and image are dual descriptions of the same subspace, and computing both is a built-in correctness check.** The tangent space is *one* subspace; that it can be obtained as the kernel of one derivative ($Df$) and the image of another ($DG$) reflects the duality between *constraints* (equations cutting the space down) and *parametrizations* (coordinates building it up). When a submanifold is available in more than one representation, computing the tangent space by each route and verifying they agree is the cheapest possible sanity check — a disagreement pinpoints an arithmetic slip immediately. The [[Thm - The Regular Value Theorem|regular value theorem]] and the equivalence of submanifold descriptions *guarantee* agreement in advance, so any mismatch is purely an error.

**The tangent space to a graph is the graph of the derivative — the cleanest case, and the one to picture.** When $M$ is the graph $z = g(x)$, the tangent space at $(p, g(p))$ is precisely the graph of the linear map $Dg(p)$. This is the most concrete tangent-space picture there is: the surface is a graph, its tangent space is the graph of the linearization, and the tangent *plane* is the graph of the first-order Taylor approximation $g(p) + Dg(p)(x - p)$. Since the [[Thm - The Implicit Function Theorem|implicit function theorem]] guarantees *every* submanifold is locally a graph, this picture is universally available — and it is the right mental image to carry for "tangent space".

**The normal direction is the gradient of the implicit defining function, orthogonal to every tangent vector.** Once $M = \{f = c\}$, the normal space at $p$ is spanned by $\nabla f(p)$, because the tangent space is $\ker Df_p$ and the gradient is orthogonal to its own kernel. Here $\nabla f(p) = (2,2,-1)$ is normal to the paraboloid at $p$, and one verifies it by checking orthogonality against the tangent spanning vectors. This is the same fact that drives the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]]: the constraint gradient is normal to the constraint surface. The trigger "I need a normal vector to a level set" should immediately summon "take the gradient of the defining function".
