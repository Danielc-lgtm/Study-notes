---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Change of Variables Formula"
  - "Thm - Fubini's Theorem"
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $P$ be the parallelogram in the $(x,y)$-plane with vertices $(0,0)$, $(1,1)$, $(2,0)$, $(1,-1)$. Evaluate
$$\iint_P (x + y)^2 \, dA$$
by means of the change of variables
$$u = x + y, \qquad v = x - y.$$

(The substitution is *linear*, hence a clean diffeomorphism — the "nonlinear" of the title refers to changing variables by a non-identity map; the same technique handles genuinely nonlinear substitutions, and the takeaways treat that case.)

**Recall:**

![[Thm - The Change of Variables Formula#Statement]]

[[Thm - The Change of Variables Formula|The change of variables formula]]: for a $C^1$ diffeomorphism $G : O \to \Omega$ and integrable $f$, $\int_\Omega f(y)\,dV(y) = \int_O f(G(x))\,|\det DG(x)|\,dV(x)$. When the substitution is presented as new variables in terms of old, $u = u(x,y)$, $v = v(x,y)$ — call this map $T$ — the relevant Jacobian is that of the *inverse* map $G = T^{-1}$: one has $|\det DG| = 1/|\det DT|$, since $DG = (DT)^{-1}$. [[Thm - Fubini's Theorem|Fubini's theorem]] then evaluates the integral over the new region, which a well-chosen substitution makes a rectangle.

---

# Convergent Strategy

**Problem class.** This is a *change-of-variables evaluation* where the substitution is chosen to *straighten the domain*. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] notes that a linear deformation of the domain calls for a matrix substitution, chosen so the transformed region is Fubini-friendly.

**Assumption pattern.** The parallelogram $P$ has edges along the lines $x + y = \text{const}$ and $x - y = \text{const}$ — its sides are level sets of $u$ and $v$. The recognizable feature: the domain is awkward in $(x,y)$ but becomes a *rectangle* in coordinates $(u,v)$ adapted to its edges. The integrand $(x+y)^2 = u^2$ also simplifies.

**Theorem routing.** The map $T(x,y) = (x+y, x-y)$ sends $P$ to a rectangle $P^*$ in the $(u,v)$-plane. Its inverse $G(u,v) = (\tfrac{u+v}{2}, \tfrac{u-v}{2})$ is the diffeomorphism the change of variables formula needs, with Jacobian $|\det DG| = \tfrac12$. The integral becomes $\iint_{P^*} u^2\cdot\tfrac12\,du\,dv$, a rectangle integral that [[Thm - Fubini's Theorem|Fubini]] evaluates immediately.

**Key decision point.** Two points. First, the substitution is *chosen to straighten the region*: the parallelogram's edges are level sets of $u = x+y$ and $v = x-y$, so in $(u,v)$ those edges become coordinate lines and $P$ becomes a rectangle — that is why this particular substitution. Second, the Jacobian bookkeeping: the substitution is given as new-in-terms-of-old ($u,v$ as functions of $x,y$), but the change of variables formula wants the diffeomorphism $G$ mapping new coordinates to old, so one must either invert the map or use $|\det DG| = 1/|\det DT|$. Getting which determinant goes where is the standard pitfall.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Change variables by a diffeomorphism, inserting the Jacobian.** The substitution $G(u,v) = (\tfrac{u+v}{2}, \tfrac{u-v}{2})$ rewrites the integral with the Jacobian factor $\tfrac12$.

2. **Use a linear change of variables to compute volumes / transform regions.** The linear map straightens the parallelogram into a rectangle.

3. **Reduce a multiple integral to iterated single integrals (Fubini).** The rectangle integral $\iint_{P^*} u^2\cdot\tfrac12\,du\,dv$ is evaluated by iteration.

---

# Hints

> [!note]- Hint 1
> The parallelogram is awkward to integrate over in $(x,y)$. Look at its edges: each side lies on a line of the form $x + y = \text{const}$ or $x - y = \text{const}$. That is the cue for which new variables to use.

> [!note]- Hint 2
> With $u = x + y$ and $v = x - y$, find the ranges of $u$ and $v$ over the parallelogram by plugging in the four vertices. You should find $u$ and $v$ each range over an interval, so $P$ becomes a *rectangle* in $(u,v)$.

> [!note]- Hint 3
> The change of variables formula needs the map $G$ from $(u,v)$ to $(x,y)$. Invert the substitution: solve $u = x+y$, $v = x-y$ for $x$ and $y$. You get $x = \tfrac{u+v}{2}$, $y = \tfrac{u-v}{2}$. Compute the Jacobian matrix $DG$ and its determinant.

> [!note]- Hint 4
> The integrand $(x+y)^2$ is just $u^2$. With $|\det DG| = \tfrac12$, the integral becomes $\iint_{P^*} u^2\cdot\tfrac12\,du\,dv$ over the rectangle $P^*$. Integrate by Fubini.

---

# Solution

The parallelogram's edges are level sets of $x+y$ and $x-y$, so in coordinates $u = x+y$, $v = x-y$ the domain becomes a rectangle and the integrand becomes $u^2$. The change of variables formula supplies the Jacobian factor $\tfrac12$.

**Step 1: The substitution turns the parallelogram into a rectangle.**

In $(u,v)$-coordinates, $P$ becomes the rectangle $P^* = [0,2]\times[-2,2]$... let us determine it from the vertices.

> [!note]- Derivation
> The four vertices of $P$ are $(0,0), (1,1), (2,0), (1,-1)$. Apply $u = x+y$, $v = x-y$ to each:
> $$(0,0) \mapsto (u,v) = (0, 0), \quad (1,1) \mapsto (2, 0), \quad (2,0) \mapsto (2, 2), \quad (1,-1) \mapsto (0, 2).$$
> The images are $(0,0), (2,0), (2,2), (0,2)$ — the four corners of the rectangle
> $$P^* = \{(u,v) : 0 \leq u \leq 2,\ 0 \leq v \leq 2\}.$$
> The edges confirm the choice of substitution: the side of $P$ from $(0,0)$ to $(1,1)$ lies on the line $x - y = 0$, i.e. $v = 0$; the side from $(1,1)$ to $(2,0)$ lies on $x + y = 2$, i.e. $u = 2$; and so on. Each edge of the parallelogram is a level set of $u$ or of $v$, which is exactly why $P$ becomes a coordinate rectangle in $(u,v)$.

**Step 2: Invert the substitution and compute the Jacobian.**

$G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$, with $|\det DG| = \tfrac12$.

> [!note]- Derivation
> The [[Thm - The Change of Variables Formula|change of variables formula]] is stated for a diffeomorphism $G$ mapping the *new* coordinates to the *old*: $\int_\Omega f(y)\,dy = \int_O f(G(x))|\det DG(x)|\,dx$. Here the new coordinates are $(u,v)$ and the old are $(x,y)$, so we need $G : (u,v) \mapsto (x,y)$. Invert the linear system $u = x+y$, $v = x-y$: adding gives $u + v = 2x$, subtracting gives $u - v = 2y$, so
> $$G(u,v) = (x, y) = \left( \frac{u+v}{2},\ \frac{u-v}{2} \right).$$
> This $G$ is a linear bijection $\mathbb{R}^2 \to \mathbb{R}^2$, hence a $C^1$ diffeomorphism. Its Jacobian matrix is the constant matrix
> $$DG = \begin{pmatrix} \partial x/\partial u & \partial x/\partial v \\[2pt] \partial y/\partial u & \partial y/\partial v \end{pmatrix} = \begin{pmatrix} \tfrac12 & \tfrac12 \\[2pt] \tfrac12 & -\tfrac12 \end{pmatrix}, \qquad \det DG = \tfrac12\cdot(-\tfrac12) - \tfrac12\cdot\tfrac12 = -\tfrac12.$$
> So $|\det DG| = \tfrac12$. (Cross-check: the forward map $T(x,y) = (x+y, x-y)$ has $\det DT = \det\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix} = -2$, and indeed $|\det DG| = 1/|\det DT| = 1/2$, consistent with $DG = (DT)^{-1}$.)

**Step 3: Rewrite the integral and evaluate by Fubini.**

$\displaystyle\iint_P (x+y)^2\,dA = \iint_{P^*} u^2\cdot\tfrac12\,du\,dv = \tfrac{16}{3}$.

> [!note]- Derivation
> The integrand transforms simply: $(x+y)^2 = u^2$, since $u = x+y$. By the [[Thm - The Change of Variables Formula|change of variables formula]] with the diffeomorphism $G$ of Step 2,
> $$\iint_P (x+y)^2\,dA = \iint_{P^*} \underbrace{u^2}_{f\circ G}\cdot\underbrace{\tfrac12}_{|\det DG|}\,du\,dv.$$
> The new region $P^* = [0,2]\times[0,2]$ is a rectangle, so [[Thm - Fubini's Theorem|Fubini's theorem]] applies directly, and since the integrand $u^2$ does not depend on $v$ the iterated integral separates into a product:
> $$\iint_{P^*} \tfrac12\,u^2\,du\,dv = \tfrac12\left(\int_0^2 u^2\,du\right)\left(\int_0^2 dv\right).$$
> The two factors are $\int_0^2 u^2\,du = \big[\tfrac{u^3}{3}\big]_0^2 = \tfrac83$ and $\int_0^2 dv = 2$. Therefore
> $$\iint_P (x+y)^2\,dA = \tfrac12\cdot\tfrac83\cdot 2 = \frac{8}{3}. \qquad \blacksquare$$

> [!note]- Complete formal solution
> The parallelogram $P$ with vertices $(0,0),(1,1),(2,0),(1,-1)$ has edges on the lines $x\pm y = \text{const}$. Under $T(x,y) = (x+y, x-y)$ the vertices map to $(0,0),(2,0),(2,2),(0,2)$, so $P$ corresponds to the rectangle $P^* = [0,2]^2$ in $(u,v)$.
>
> The inverse $G(u,v) = (\tfrac{u+v}{2}, \tfrac{u-v}{2})$ is a $C^1$ diffeomorphism with constant Jacobian $DG = \tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $|\det DG| = \tfrac12$. Since $(x+y)^2 = u^2$, the [[Thm - The Change of Variables Formula|change of variables formula]] gives
> $$\iint_P (x+y)^2\,dA = \iint_{P^*} u^2\cdot\tfrac12\,du\,dv = \tfrac12\left(\int_0^2 u^2\,du\right)\left(\int_0^2 dv\right) = \tfrac12\cdot\tfrac83\cdot 2 = \frac{8}{3}. \qquad \blacksquare$$

---

# Key Takeaways

**Choose the substitution to straighten the domain — let the region's edges become coordinate lines.** The whole reason $u = x+y$, $v = x-y$ is the right substitution is that the parallelogram's four edges lie on lines $x+y = \text{const}$ and $x-y = \text{const}$ — they are level sets of $u$ and $v$. In $(u,v)$-coordinates those edges become $u = \text{const}$ and $v = \text{const}$, so the parallelogram becomes a rectangle, on which Fubini is trivial. The trigger is a domain whose boundary is built from level sets of some pair of functions: take those functions as the new coordinates. This generalizes far beyond linear substitutions — a region bounded by hyperbolas $xy = \text{const}$ and lines $y/x = \text{const}$ is straightened by $u = xy$, $v = y/x$; a region between parabolas is straightened by matching coordinates. The substitution is selected by the *geometry of the domain*, not by the integrand.

**The change of variables formula needs the diffeomorphism from new coordinates to old — invert, or use the reciprocal Jacobian.** A substitution is usually handed to you as new-in-terms-of-old, $u = u(x,y)$, $v = v(x,y)$ — call that map $T$. But the formula $\int_\Omega f\,dy = \int_O (f\circ G)|\det DG|\,dx$ is written for $G$ mapping the *new* variables to the *old*, i.e. $G = T^{-1}$. There are two correct ways to get the Jacobian factor: invert $T$ explicitly to get $G$ and compute $\det DG$, or compute $\det DT$ and use $|\det DG| = 1/|\det DT|$, valid because $DG = (DT)^{-1}$. The standard error is to use $|\det DT|$ where $|\det DG|$ is needed — here that would insert a factor $2$ instead of $\tfrac12$, off by a factor of $4$. The discipline: always be explicit about which map is the diffeomorphism whose Jacobian appears.

**For genuinely nonlinear substitutions the procedure is identical — only the Jacobian is no longer constant.** Here the substitution was linear, so $DG$ was a constant matrix and $|\det DG| = \tfrac12$ everywhere. For a nonlinear substitution — polar coordinates, $u = xy$/$v = y/x$, or any $C^1$ diffeomorphism — the steps are exactly the same: identify the region in new coordinates, write $G$ from new to old, compute the Jacobian determinant (now a *function* of the new variables), and apply the formula. The only differences are that $|\det DG(u,v)|$ stays inside the integral as a non-constant weight, and that one must check $G$ is a genuine diffeomorphism (injective, nonvanishing Jacobian) on the open region of integration, repairing any thin non-injective set as nil — as polar coordinates require in [[Ex - The Gaussian integral via polar coordinates]]. The linear case is the nonlinear procedure with the Jacobian frozen to a constant.
