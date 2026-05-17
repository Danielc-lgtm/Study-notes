---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Implicit Function Theorem"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - The Chain Rule"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider the system of two equations in the four unknowns $(u, v, x, y)$:
$$F(u,v,x,y) = \begin{pmatrix} x(u^2 + v^2) \\ xu + yv\end{pmatrix} = \begin{pmatrix} 4 \\ 2\end{pmatrix}.$$

1. Verify that $(u_0, v_0, x_0, y_0) = (2, 0, 1, 1)$ is a solution.
2. Show that near this point the system defines $u$ and $v$ as smooth functions of $(x, y)$: there exist $C^\infty$ functions $u = u(x,y)$, $v = v(x,y)$ on a neighbourhood of $(1,1)$ with $u(1,1) = 2$, $v(1,1) = 0$, satisfying the system.
3. Compute the partial derivatives $\partial u/\partial x$, $\partial u/\partial y$, $\partial v/\partial x$, $\partial v/\partial y$ at the point $(x,y) = (1,1)$.

**Recall:**

The objects in play are the partial Jacobian, the implicit function theorem, and the derivative formula for the implicit solution.

![[Thm - The Implicit Function Theorem#Statement]]

By the [[Thm - The Implicit Function Theorem|implicit function theorem]], if $F(x_0, y_0) = c$ and the partial Jacobian $D_y F$ in the *dependent* variables is invertible at the base point, then near $(x_0, y_0)$ the equation $F = c$ is equivalent to $y = g(x)$ for a unique $C^k$ map $g$, with derivative $Dg = -(D_y F)^{-1}D_x F$. Here the dependent variables are $(u,v)$ and the free variables are $(x,y)$; the partial Jacobian to check is $D_{(u,v)}F$, a $2\times 2$ matrix. The derivative formula is obtained by differentiating the defining identity $F(\text{dependent}(x,y),\ x,y) = c$ with the [[Thm - The Chain Rule|chain rule]].

---

# Convergent Strategy

**Problem class.** This is a *local-solvability* problem: show a system can be solved for some variables in terms of the others, then compute the derivative of the implicit solution. The [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic strategy]] gives the fixed recipe: identify a base solution, choose the variable split, check the partial Jacobian, then differentiate the identity.

**Assumption pattern.** Four unknowns, two equations — so two variables can be solved for in terms of the other two. The problem *tells you* the split: solve for $(u,v)$ in terms of $(x,y)$. The base point is provided.

**Theorem routing.** Verify the base point satisfies the system. Form the partial Jacobian $D_{(u,v)}F$, evaluate at the base point, check it is invertible (nonzero determinant). The [[Thm - The Implicit Function Theorem|implicit function theorem]] then yields the smooth functions $u(x,y), v(x,y)$. For the derivatives, apply the formula $Dg = -(D_{(u,v)}F)^{-1}D_{(x,y)}F$.

**Key decision point.** The non-obvious part is purely computational discipline: assemble the *full* $2\times 4$ Jacobian, then *correctly partition* it into the $2\times 2$ dependent block $D_{(u,v)}F$ and the $2\times 2$ free block $D_{(x,y)}F$. The derivative of the implicit solution is the matrix product $-(D_{(u,v)}F)^{-1}D_{(x,y)}F$, and getting the blocks and the order right is the whole computation.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Split the variables and check a partial Jacobian to solve an equation.** Designate $(u,v)$ as dependent, $(x,y)$ as free; form $D_{(u,v)}F$ and check invertibility at the base point.

2. **Differentiate the defining identity to compute the derivative of an implicit function.** Apply the chain rule to $F(u(x,y), v(x,y), x, y) = c$ and solve the resulting linear system for the partials.

---

# Hints

> [!note]- Hint 1
> Check the base point: $F(2,0,1,1) = (1\cdot(4+0),\ 1\cdot 2 + 1\cdot 0) = (4, 2)$. Good. Now to solve for $(u,v)$, the relevant block is $D_{(u,v)}F$ — differentiate $F$ with respect to $u$ and $v$ only.

> [!note]- Hint 2
> $D_{(u,v)}F = \begin{pmatrix} \partial_u F_1 & \partial_v F_1 \\ \partial_u F_2 & \partial_v F_2\end{pmatrix} = \begin{pmatrix} 2xu & 2xv \\ x & y\end{pmatrix}$. Evaluate at $(2,0,1,1)$ and compute the determinant. If it is nonzero, the implicit function theorem applies.

> [!note]- Hint 3
> At $(2,0,1,1)$: $D_{(u,v)}F = \begin{pmatrix} 4 & 0 \\ 1 & 1\end{pmatrix}$, determinant $4 \neq 0$ — invertible. So $u, v$ are smooth functions of $(x,y)$ near $(1,1)$.

> [!note]- Hint 4
> The derivative formula is $Dg = -(D_{(u,v)}F)^{-1}D_{(x,y)}F$ where $g = (u,v)$. Compute $D_{(x,y)}F = \begin{pmatrix}\partial_x F_1 & \partial_y F_1 \\ \partial_x F_2 & \partial_y F_2\end{pmatrix} = \begin{pmatrix} u^2+v^2 & 0 \\ u & v\end{pmatrix}$, evaluate at the base point, invert the $2\times 2$ block, and multiply.

---

# Solution

Four unknowns and two equations leave two degrees of freedom, and the implicit function theorem says we can solve for *two* of the variables in terms of the other two — provided the partial Jacobian in the chosen dependent variables is invertible. Here the dependent block has determinant $4 \neq 0$, so $(u,v)$ are smooth functions of $(x,y)$, and the chain rule delivers their derivatives.

**Step 1: The base point is a solution.**

$F(2,0,1,1) = (4, 2)$, so $(2,0,1,1)$ satisfies the system.

> [!note]- Derivation
> Substitute $u = 2, v = 0, x = 1, y = 1$:
> $$F_1 = x(u^2 + v^2) = 1\cdot(2^2 + 0^2) = 4, \qquad F_2 = xu + yv = 1\cdot 2 + 1\cdot 0 = 2.$$
> So $F(2,0,1,1) = (4,2)$, the required value. The base point lies on the solution set.

**Step 2: $(u,v)$ are smooth functions of $(x,y)$.**

The partial Jacobian $D_{(u,v)}F(2,0,1,1) = \begin{pmatrix} 4 & 0 \\ 1 & 1\end{pmatrix}$ has determinant $4 \neq 0$, so by the implicit function theorem there are $C^\infty$ functions $u(x,y), v(x,y)$ near $(1,1)$ with $u(1,1) = 2$, $v(1,1) = 0$ solving the system.

> [!note]- Derivation
> The full Jacobian of $F$, with $F_1 = x(u^2+v^2)$ and $F_2 = xu + yv$, in the order $(u, v, x, y)$:
> $$JF = \begin{pmatrix} \partial_u F_1 & \partial_v F_1 & \partial_x F_1 & \partial_y F_1 \\ \partial_u F_2 & \partial_v F_2 & \partial_x F_2 & \partial_y F_2\end{pmatrix} = \begin{pmatrix} 2xu & 2xv & u^2+v^2 & 0 \\ x & y & u & v\end{pmatrix}.$$
> The *dependent* block — derivatives in $(u,v)$ — is the first two columns:
> $$D_{(u,v)}F = \begin{pmatrix} 2xu & 2xv \\ x & y\end{pmatrix}, \qquad D_{(u,v)}F(2,0,1,1) = \begin{pmatrix} 4 & 0 \\ 1 & 1\end{pmatrix}.$$
> Its determinant is $4\cdot 1 - 0\cdot 1 = 4 \neq 0$, so $D_{(u,v)}F$ is invertible at the base point. The map $F$ is $C^\infty$ (polynomial in its arguments). By the [[Thm - The Implicit Function Theorem|implicit function theorem]], with dependent variables $(u,v)$ and free variables $(x,y)$, there is a neighbourhood of $(1,1)$ and unique $C^\infty$ functions $u(x,y), v(x,y)$ with $u(1,1) = 2$, $v(1,1) = 0$ such that $F(u(x,y), v(x,y), x, y) = (4,2)$ identically.

**Step 3: The derivatives of the implicit solution at $(1,1)$.**

Writing $g = (u,v)$, the derivative is $Dg = -(D_{(u,v)}F)^{-1}D_{(x,y)}F$, which at $(1,1)$ evaluates to
$$Dg(1,1) = \begin{pmatrix} \partial u/\partial x & \partial u/\partial y \\ \partial v/\partial x & \partial v/\partial y\end{pmatrix} = \begin{pmatrix} -1 & 0 \\ -2 & -1\end{pmatrix}.$$
That is, $\partial u/\partial x = -1$, $\partial u/\partial y = 0$, $\partial v/\partial x = -2$, $\partial v/\partial y = -1$ at $(1,1)$.

> [!note]- Derivation
> Differentiate the identity $F(u(x,y), v(x,y), x, y) = (4,2)$ with the [[Thm - The Chain Rule|chain rule]]. Splitting the Jacobian into the dependent block $D_{(u,v)}F$ and the free block $D_{(x,y)}F$:
> $$0 = D_{(u,v)}F\cdot Dg + D_{(x,y)}F, \qquad\text{hence}\qquad Dg = -\big(D_{(u,v)}F\big)^{-1}D_{(x,y)}F.$$
> The *free* block — derivatives in $(x,y)$ — is the last two columns of $JF$:
> $$D_{(x,y)}F = \begin{pmatrix} u^2+v^2 & 0 \\ u & v\end{pmatrix}, \qquad D_{(x,y)}F(2,0,1,1) = \begin{pmatrix} 4 & 0 \\ 2 & 0\end{pmatrix}.$$
> Invert the dependent block. For $\begin{pmatrix} 4 & 0 \\ 1 & 1\end{pmatrix}$, the inverse is $\dfrac{1}{4}\begin{pmatrix} 1 & 0 \\ -1 & 4\end{pmatrix}$ (use $\begin{pmatrix} a&b\\c&d\end{pmatrix}^{-1} = \tfrac{1}{ad-bc}\begin{pmatrix} d&-b\\-c&a\end{pmatrix}$ with $ad-bc = 4$).
>
> Now multiply:
> $$Dg(1,1) = -\,\frac{1}{4}\begin{pmatrix} 1 & 0 \\ -1 & 4\end{pmatrix}\begin{pmatrix} 4 & 0 \\ 2 & 0\end{pmatrix} = -\,\frac{1}{4}\begin{pmatrix} 1\cdot 4 + 0\cdot 2 & 0 \\ -1\cdot 4 + 4\cdot 2 & 0\end{pmatrix} = -\,\frac{1}{4}\begin{pmatrix} 4 & 0 \\ 4 & 0\end{pmatrix} = \begin{pmatrix} -1 & 0 \\ -1 & 0\end{pmatrix}.$$
> Reading off the entries: $\partial u/\partial x = -1$, $\partial u/\partial y = 0$, $\partial v/\partial x = -1$, $\partial v/\partial y = 0$ at $(x,y) = (1,1)$.
>
> *(Consistency check by direct differentiation.* Differentiate $xu + yv = 2$ in $x$: $u + x u_x + y v_x = 0$, so at the base point $2 + u_x + v_x = 0$. With $u_x = -1$, $v_x = -1$: $2 - 1 - 1 = 0$. ✓ Differentiate $x(u^2+v^2) = 4$ in $x$: $(u^2+v^2) + x(2u\,u_x + 2v\,v_x) = 0$, at the base point $4 + (4u_x + 0) = 0$, so $u_x = -1$. ✓)*

> [!note]- Complete formal solution
> *Base point.* $F(2,0,1,1) = (1\cdot 4,\ 2) = (4,2)$. ✓
>
> *Solvability.* $JF = \begin{pmatrix} 2xu & 2xv & u^2+v^2 & 0 \\ x & y & u & v\end{pmatrix}$. The dependent block $D_{(u,v)}F = \begin{pmatrix} 2xu & 2xv \\ x & y\end{pmatrix}$ at $(2,0,1,1)$ equals $\begin{pmatrix} 4 & 0 \\ 1 & 1\end{pmatrix}$, $\det = 4 \neq 0$. By the [[Thm - The Implicit Function Theorem|implicit function theorem]] ($F$ is $C^\infty$), $u, v$ are $C^\infty$ functions of $(x,y)$ near $(1,1)$ with $u(1,1) = 2$, $v(1,1) = 0$.
>
> *Derivatives.* $Dg = -(D_{(u,v)}F)^{-1}D_{(x,y)}F$. At the base point $D_{(x,y)}F = \begin{pmatrix} 4 & 0 \\ 2 & 0\end{pmatrix}$ and $(D_{(u,v)}F)^{-1} = \tfrac14\begin{pmatrix} 1 & 0 \\ -1 & 4\end{pmatrix}$, so
> $$Dg(1,1) = -\tfrac14\begin{pmatrix} 1 & 0 \\ -1 & 4\end{pmatrix}\begin{pmatrix} 4 & 0 \\ 2 & 0\end{pmatrix} = \begin{pmatrix} -1 & 0 \\ -1 & 0\end{pmatrix}.$$
> Thus $u_x = -1, u_y = 0, v_x = -1, v_y = 0$ at $(1,1)$. $\blacksquare$

---

# Key Takeaways

**Solving a system for some variables is a fixed four-step recipe: base point, variable split, partial Jacobian, derivative formula.** Every local-solvability problem follows this exact path. First, find a known solution — the theorem is local and needs an anchor. Second, decide which variables are *dependent* (to be solved for) and which are *free*; the count must match the number of equations. Third, form the partial Jacobian in the dependent variables only and check it is invertible at the base point — this single determinant is the entire hypothesis. Fourth, if you need rates of change, apply $Dg = -(D_{\text{dep}}F)^{-1}D_{\text{free}}F$. The recipe never requires solving the system explicitly, which is the whole point: the functions $u(x,y), v(x,y)$ here have no elementary closed form, yet their existence, smoothness, and derivatives are all pinned down.

**The choice of which variables to solve for is the solver's, and it is governed by which block of the Jacobian is invertible.** The full Jacobian here is $2\times 4$; partitioning it into a $2\times 2$ dependent block and a $2\times 2$ free block is a *choice*, and the theorem succeeds for any choice whose dependent block is invertible. Had the $(u,v)$-block been singular, one would try the $(u,x)$-block, the $(x,y)$-block, and so on — the system is solvable for *some* pair of variables exactly when the full Jacobian has maximal rank $2$. The discipline is: never conclude "the system cannot be solved" from one bad split; check whether *another* split has an invertible block. This is the same principle that, in the scalar case, lets a level set with nonvanishing gradient always be solved for *some* coordinate.

**The derivative formula is just the chain rule on the defining identity, and it should be re-derived, not memorized.** The implicit functions satisfy $F(\text{dep}(x), x) = c$ *identically*, and differentiating an identity is always legal. The chain rule gives $D_{\text{dep}}F\cdot Dg + D_{\text{free}}F = 0$, a *linear* equation for the unknown matrix $Dg$, solved by inverting the dependent block. Re-deriving it this way — rather than recalling the formula $-(D_{\text{dep}}F)^{-1}D_{\text{free}}F$ — makes the structure transparent and is far less error-prone, especially for keeping the blocks and the multiplication order straight. The same move computes tangent spaces, comparative statics, and sensitivities throughout the subject: whenever a quantity is defined implicitly, differentiate its defining identity.

**Verify the answer by differentiating the original equations directly.** The block-matrix computation is mechanical and easy to slip on — a transposed block, a sign, an inverted-matrix entry. An independent check is cheap and decisive: differentiate each scalar equation of the system directly with respect to one free variable, substitute the base-point values and the computed partials, and confirm the equation holds. Here, differentiating $xu + yv = 2$ and $x(u^2+v^2) = 4$ in $x$ and substituting $u_x = v_x = -1$ both check out. This habit — compute by the formula, verify by direct differentiation — catches the great majority of arithmetic errors in implicit-differentiation problems.
