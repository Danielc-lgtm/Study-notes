---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Curvature is the Infinitesimal Holonomy"
  - "Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation"
  - "Def - Path-Ordered Exponential"
  - "Def - Holonomy Group of a Connection"
  - "Thm - Stokes' Theorem on Manifolds"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work in the trivial principal bundle $P = U \times G$ over an open set $U \subseteq \mathbb{R}^2$ containing the origin, with $G \subseteq GL(n; \mathbb{K})$ a matrix group, $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$. Let $X, Y \in \mathfrak{g} \subseteq \mathfrak{gl}(n; \mathbb{K})$ be **fixed constant matrices** (elements of the Lie algebra, so $\exp(tX), \exp(tY) \in G$), and consider the local connection $1$-form
$$A = x\,X\,dy + y\,Y\,dx \in \Omega^1(U; \mathfrak{g}),$$
that is, in the standard coordinates $(x^1, x^2) = (x, y)$ its coefficient matrices are $A_x = yY$ (the coefficient of $dx$) and $A_y = xX$ (the coefficient of $dy$). Note that $A$ **vanishes at the origin**: $A_x(0,0) = 0$ and $A_y(0,0) = 0$.

For $L > 0$ let $c_L$ be the boundary of the square
$$S = S_L = [0, L] \times [0, L] \subseteq \mathbb{R}^2,$$
traversed once counterclockwise starting and ending at the corner $b_0 = (0,0)$: bottom edge $(0,0) \to (L,0)$, right edge $(L,0) \to (L,L)$, top edge $(L,L) \to (0,L)$, left edge $(0,L) \to (0,0)$. Orient $S$ by $dx \wedge dy$, so that $\partial S = c_L$ with the induced (counterclockwise) orientation.

**The task.** Compute the holonomy $\operatorname{hol}(c_L) \in G$ of the connection along $c_L$ by expanding the path-ordered exponential (the Dyson series) to second order by hand, and verify the general small-loop formula
$$\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3) \qquad (L \searrow 0), \qquad F = dA + A \wedge A,$$
computing the exact coefficients of the expansion. In particular, determine at which order in $L$ the non-abelian commutator $[Y, X]$ first appears, and reconcile this with the shape of the curvature $F$.

**Recall:**

The objects in play are the local curvature $2$-form $F = dA + A \wedge A$, the holonomy of a loop as the path-ordered exponential of the local connection form, the second-order Dyson expansion, and Stokes' theorem for turning a line integral over $c_L$ into a surface integral over $S_L$.

![[Thm - Curvature is the Infinitesimal Holonomy#Statement]]

The theorem above is exactly the general statement this exercise instantiates: for a matrix group $G \subseteq GL(n; \mathbb{K})$ and a small loop $c_L$ at $b_0$ of length $O(L)$ bounding a surface $S_L$ of area $O(L^2)$, the holonomy is $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$, with $F = dA + A \wedge A$ the local curvature. Our $A$ is a concrete case in which the whole expansion can be carried out by hand.

![[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation#Statement]]

Concretely, in a trivialisation the holonomy is the value at the endpoint of the solution of the parallel-transport equation $\dot v(\tau) = -A(\dot c_L(\tau))\, v(\tau)$, $v(0) = v_0$, so that $\operatorname{hol}(c_L) = \mathcal{P}\exp\!\big({-}\oint_{c_L} A\big)$, and by the theorem above this operator is given by the **Dyson series**
$$\mathcal{P}\exp\!\Big({-}\oint_{c_L} A\Big) = 1_n - \int_0^1 \! d\tau\, A(\dot c_L(\tau)) + \int_0^1 \! d\tau_2 \int_0^{\tau_2} \! d\tau_1\, A(\dot c_L(\tau_2))\, A(\dot c_L(\tau_1)) - \cdots,$$
where $A(\dot c_L(\tau)) = A_x(c_L(\tau))\,\dot x(\tau) + A_y(c_L(\tau))\,\dot y(\tau) \in \mathfrak{g}$ is the connection form contracted against the velocity, and the $j$-th term is the ordered integral $(-1)^j \int_{0 \le \tau_1 \le \cdots \le \tau_j \le 1} A(\dot c_L(\tau_j)) \cdots A(\dot c_L(\tau_1))$.

![[Thm - Stokes' Theorem on Manifolds#Statement]]

We use Stokes' theorem in the plane in the form $\oint_{\partial S} \eta = \int_S d\eta$ for a $1$-form $\eta$ on $S$; applied componentwise to the $\mathfrak{g}$-valued form $A$ it gives $\oint_{c_L} A = \int_{S_L} dA$.

Two standing facts about parallel transport are used and recalled at their point of use: holonomy is **invariant under orientation-preserving reparametrisation** and **multiplicative under concatenation of curves**, so that the transport along a concatenation is the composition (in reverse order) of the transports along the pieces — both proved on **[[Thm - Properties of Parallel Transport|Thm - Properties of Parallel Transport]]**.

---

# Convergent Strategy

**Problem class:** This is a *verify-an-asymptotic-formula-by-explicit-computation* problem: we are handed a specific connection and asked to reproduce, from the raw Dyson series, the leading behaviour that [[Thm - Curvature is the Infinitesimal Holonomy|the infinitesimal-holonomy theorem]] predicts in general, and to expose one feature the general statement leaves implicit — the order at which the non-commutative correction enters. The value of the exercise is that the general proof freezes the connection coefficients at the base point $b_0$ and estimates the rest; here $A(b_0) = 0$, so the frozen coefficients vanish and the "obvious" second-order term disappears, forcing us to see where the commutator actually lives.

**Assumption pattern:** The connection $A = xX\,dy + yY\,dx$ is engineered so that its restriction to each edge of the square is a *constant* matrix times the parameter differential. The recognisable trigger is that the coefficient $A_x = yY$ is annihilated on the two horizontal edges where either $y = 0$ or $\dot x = 0$ against a fixed $x$, and $A_y = xX$ is annihilated on the two vertical edges where either $x = 0$ or $\dot y = 0$. Whenever the pulled-back connection form $A(\dot c)$ is a *constant* element of $\mathfrak{g}$ along an edge, the path-ordered exponential over that edge is an ordinary matrix exponential, because a constant matrix commutes with itself and the ordering in the Dyson series becomes irrelevant.

**Theorem routing:** The route is: (1) compute $F = dA + A \wedge A$ by the [[Thm - Curvature is the Infinitesimal Holonomy|structure formula]] and integrate it over $S_L$ to fix the target $\int_{S_L} F$; (2) parametrise $c_L$ and evaluate $A(\dot c_L)$ on each edge, finding it vanishes on two edges and is a constant matrix on the other two; (3) read the first-order Dyson term as $-\oint_{c_L} A$ and turn it into $-\int_{S_L} dA$ by [[Thm - Stokes' Theorem on Manifolds|Stokes]]; (4) evaluate the second-order Dyson term directly from the piecewise-constant integrand and check it is $O(L^4)$; (5) assemble, and compare with $1_n - \int_{S_L} F$. As an independent check we also compute $\operatorname{hol}(c_L)$ exactly by the concatenation law of [[Thm - Properties of Parallel Transport|parallel transport]], obtaining a product of two matrix exponentials whose Taylor expansion reproduces the Dyson result term by term.

**Key decision point:** The single non-obvious move is to *not trust the general formula's bookkeeping blindly*. The general theorem writes the second-order antisymmetric term as $-\int_S [A_j(0), A_k(0)]\, dx^j \wedge dx^k$, which for our $A$ is identically zero because $A_j(0) = 0$. One might therefore expect the commutator $[Y, X]$ to be absent — but it is present in $F$, through the term $A \wedge A = xy[Y,X]\,dx \wedge dy$, and it contributes $\int_{S_L} A \wedge A = \tfrac{L^4}{4}[Y,X]$. The reconciliation is that this contribution is $O(L^4)$, hence beneath the $O(L^3)$ accuracy of the theorem: at the controlled order the holonomy sees only $\int_{S_L} dA$, and the commutator is genuinely a higher-order effect *for a connection that vanishes at the base point*. Recognising that "the curvature has an $A \wedge A$ piece" and "the holonomy expansion shows a commutator at order $L^2$" are not the same statement is the point of the drill.

---

# Legal Operations Used

This solution deploys the following operations from the [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections#Legal Operations|topic page's Legal Operations]]; where the topic page numbering is not yet fixed, each is named descriptively.

1. **Compute a local curvature from its connection form by the structure formula.** Apply $F = dA + A \wedge A$ to the given $A$, computing $dA$ as $(\partial_x A_y - \partial_y A_x)\,dx \wedge dy$ and $A \wedge A$ as $[A_x, A_y]\,dx \wedge dy$.

2. **Contract a connection form against a curve's velocity edge by edge.** Evaluate $A(\dot c_L(\tau)) = A_x\,\dot x + A_y\,\dot y$ along each straight edge of the square, using the vanishing of $A_x$ or $A_y$ on the edge to simplify.

3. **Collapse a path-ordered exponential to an ordinary exponential on an edge where the integrand is constant.** On an edge where $A(\dot c_L)$ is a constant matrix, the Dyson ordering is vacuous and $\mathcal{P}\exp$ over that edge equals $\exp$ of the ordinary integral.

4. **Convert a loop integral of a $1$-form into a surface integral of its differential (Stokes).** Rewrite the first-order Dyson term $-\oint_{c_L} A$ as $-\int_{S_L} dA$.

5. **Evaluate a nested (ordered) double integral of a piecewise-constant matrix function directly.** Split the second-order Dyson term across the regions where the integrand is constant and sum the contributions.

6. **Compose parallel transports along a concatenated curve in reverse order.** Multiply the four edge transports (identity on two edges) in the order dictated by the concatenation law to obtain the exact holonomy as a sanity check.

7. **Match a matrix asymptotic expansion order by order in the small parameter.** Compare the Dyson result, the exact product expansion, and $1_n - \int_{S_L} F$ coefficient by coefficient in powers of $L^2$.

---

# Hints

> [!note]- Hint 1
> First fix the target you are trying to hit. Compute the curvature $F = dA + A \wedge A$ for $A = xX\,dy + yY\,dx$. Remember that for a matrix-valued $1$-form $A = A_x\,dx + A_y\,dy$ one has $A \wedge A = A_x A_y\,dx \wedge dy + A_y A_x\,dy \wedge dx = [A_x, A_y]\,dx \wedge dy$ — the wedge of a $1$-form with itself does *not* vanish when the coefficients are matrices, because the coefficients multiply in a fixed order. Then integrate $F$ over the square $[0,L]^2$.

> [!note]- Hint 2
> Now look at the loop. On each of the four edges, at least one of $dx, dy$ vanishes and one of the coefficients $A_x = yY$, $A_y = xX$ is annihilated. Work out $A(\dot c_L)$ on each edge. You should find it is *zero* on the bottom and left edges, and a *constant* matrix on the right and top edges. A constant integrand kills the path-ordering: the transport over such an edge is a plain $\exp$.

> [!note]- Hint 3
> The first-order Dyson term is $-\oint_{c_L} A$. Either sum the four edge contributions directly, or use Stokes: $\oint_{c_L} A = \int_{S_L} dA = (X - Y)L^2$. This is the leading term. For the second-order term $\int_0^1 d\tau_2 \int_0^{\tau_2} d\tau_1\, A(\dot c_L(\tau_2))\,A(\dot c_L(\tau_1))$, use a parametrisation that traverses each edge in an equal quarter of $[0,1]$ so the integrand is piecewise constant, and integrate the nested integral region by region. Check whether this term is $O(L^2)$ or $O(L^4)$.

> [!note]- Hint 4
> The second-order term comes out $O(L^4)$, not $O(L^2)$ — because the integrand $A(\dot c_L)$ is itself $O(L^2)$ (it is a constant matrix like $LX$ times a velocity of size $O(L)$), so two factors give $O(L^4)$. Hence to order $O(L^3)$ the holonomy is $1_n - (X-Y)L^2 + O(L^3) = 1_n - \int_{S_L} dA + O(L^3)$. The commutator $[Y,X]$ hides in $\int_{S_L} A \wedge A = \tfrac{L^4}{4}[Y,X]$, which is $O(L^4)$ and so beneath the theorem's accuracy. For a clean cross-check, compute the holonomy exactly as the ordered product of the two non-trivial edge exponentials and Taylor-expand.

---

# Solution

The computation proceeds in five steps. We first pin down the target $\int_{S_L} F$ from the structure formula. We then observe that the pulled-back connection $A(\dot c_L)$ vanishes on two edges and is constant on the other two, which trivialises the path-ordering; the first-order Dyson term is then $-\int_{S_L} dA$ by Stokes, and the second-order term is an elementary integral of a piecewise-constant matrix function, which turns out to be $O(L^4)$. Assembling and comparing with $1_n - \int_{S_L} F$ verifies the formula and locates the commutator at order $L^4$. Throughout, $1_n$ denotes the identity matrix and all products are matrix products.

**Step 1: Compute the curvature and its flux $\int_{S_L} F$ — the target of the verification.**

With $A_x = yY$ and $A_y = xX$, the curvature is $F = (X - Y + xy[Y,X])\,dx \wedge dy$, and $\int_{S_L} F = (X - Y)L^2 + \tfrac{L^4}{4}[Y,X]$.

> [!note]- Derivation
> The local curvature is $F = dA + A \wedge A$ (the structure formula for a matrix group, in which the bracket term $\tfrac12[A \wedge A]$ equals $A \wedge A$; this is the convention recalled on [[Thm - Curvature is the Infinitesimal Holonomy|the infinitesimal-holonomy theorem]]).
>
> *The exterior derivative.* For a matrix-valued $1$-form $A = A_x\,dx + A_y\,dy$ with $A_x, A_y \in C^\infty(U; \mathfrak{g})$,
> $$dA = (\partial_x A_y - \partial_y A_x)\,dx \wedge dy \qquad \text{(exterior derivative of a $1$-form in two variables)}.$$
> Here $\partial_x A_y = \partial_x(xX) = X$ (since $X$ is constant) and $\partial_y A_x = \partial_y(yY) = Y$ (since $Y$ is constant), so
> $$dA = (X - Y)\,dx \wedge dy \qquad \text{(substituting } \partial_x A_y = X,\ \partial_y A_x = Y).$$
>
> *The quadratic term.* Expanding the wedge of the matrix-valued form with itself and keeping the matrix order,
> $$A \wedge A = A_x A_y\, dx \wedge dy + A_y A_x\, dy \wedge dx = (A_x A_y - A_y A_x)\, dx \wedge dy = [A_x, A_y]\, dx \wedge dy \qquad \text{(} dy \wedge dx = -\,dx \wedge dy \text{)}.$$
> With $A_x = yY$ and $A_y = xX$,
> $$[A_x, A_y] = [yY, xX] = xy\,[Y, X] \qquad \text{(bilinearity of the commutator; } x, y \text{ scalars)},$$
> so $A \wedge A = xy\,[Y, X]\,dx \wedge dy$.
>
> *The curvature.* Adding the two,
> $$F = dA + A \wedge A = \big(X - Y + xy\,[Y, X]\big)\,dx \wedge dy.$$
>
> *The flux.* Integrating over the square $S_L = [0,L]^2$ with the orientation $dx \wedge dy$,
> $$\int_{S_L} F = \int_0^L\!\!\int_0^L \big(X - Y + xy\,[Y,X]\big)\,dx\,dy = (X - Y)\,L^2 + [Y,X]\Big(\int_0^L x\,dx\Big)\Big(\int_0^L y\,dy\Big),$$
> where the constant matrices $X - Y$ and $[Y,X]$ come out of the integral (Fubini, applied to each matrix entry, all integrands continuous). Since $\int_0^L x\,dx = \int_0^L y\,dy = \tfrac{L^2}{2}$,
> $$\int_{S_L} F = (X - Y)\,L^2 + [Y,X]\,\frac{L^2}{2}\cdot\frac{L^2}{2} = (X - Y)\,L^2 + \frac{L^4}{4}\,[Y,X].$$
> The abelian part $(X-Y)L^2$ is $O(L^2)$; the commutator part $\tfrac{L^4}{4}[Y,X]$ is $O(L^4)$. Keep both — the second will be the crux of Step 5.

**Step 2: Evaluate $A(\dot c_L)$ on each edge; it vanishes on two edges and is constant on the other two.**

Contracting $A$ against the velocity of each straight edge gives $0$ on the bottom and left edges, the constant $LX$ (per unit velocity) on the right edge, and the constant $-LY$ on the top edge.

> [!note]- Derivation
> The contraction is $A(\dot c_L) = A_x(c_L)\,\dot x + A_y(c_L)\,\dot y = yY\,\dot x + xX\,\dot y$, evaluated along each edge. We record for each edge which of $dx, dy$ is zero and the value of the surviving term.
>
> - **Bottom edge** $(0,0) \to (L,0)$: here $y \equiv 0$ and $\dot y \equiv 0$. Then $yY\,\dot x = 0$ (because $y = 0$) and $xX\,\dot y = 0$ (because $\dot y = 0$). Hence $A(\dot c_L) \equiv 0$.
> - **Right edge** $(L,0) \to (L,L)$: here $x \equiv L$ and $\dot x \equiv 0$. Then $yY\,\dot x = 0$ (because $\dot x = 0$) and $xX\,\dot y = LX\,\dot y$. Hence $A(\dot c_L) = LX\,\dot y$, with $LX$ a *constant* matrix.
> - **Top edge** $(L,L) \to (0,L)$: here $y \equiv L$ and $\dot y \equiv 0$. Then $yY\,\dot x = LY\,\dot x$ and $xX\,\dot y = 0$ (because $\dot y = 0$). Hence $A(\dot c_L) = LY\,\dot x$; since $x$ decreases from $L$ to $0$, $\dot x < 0$, and $LY$ is a *constant* matrix.
> - **Left edge** $(0,L) \to (0,0)$: here $x \equiv 0$ and $\dot x \equiv 0$. Then $yY\,\dot x = 0$ (because $\dot x = 0$) and $xX\,\dot y = 0$ (because $x = 0$). Hence $A(\dot c_L) \equiv 0$.
>
> The two edges where $A$ vanishes are exactly the ones sitting on the coordinate axes through the base point $b_0 = (0,0)$, where the connection form is zero; this is the first sign that the base-point value $A(b_0) = 0$ will suppress the naive leading commutator. On the two non-trivial edges the integrand is a *constant* Lie-algebra element (times the scalar velocity), which is what makes the path-ordering collapse in the next steps.

**Step 3: The first-order Dyson term equals $-\int_{S_L} dA = -(X - Y)L^2$.**

The first-order term is $-\oint_{c_L} A$; summing the edges (or applying Stokes) gives $-(X - Y)L^2$.

> [!note]- Derivation
> The first-order term of the Dyson series (recalled from [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the path-ordered-exponential theorem]]) is
> $$T_1 := \int_0^1 A(\dot c_L(\tau))\,d\tau = \oint_{c_L} A,$$
> the ordinary line integral of the $\mathfrak{g}$-valued form $A$ around the loop (this identity is the definition of the integral of a form along a curve; it is parametrisation-independent). By Step 2 the bottom and left edges contribute $0$, so
> $$\oint_{c_L} A = \int_{\text{right}} A + \int_{\text{top}} A = \int_{y=0}^{y=L} LX\,dy + \int_{x=L}^{x=0} LY\,dx \qquad \text{(only the right and top edges survive, Step 2)}.$$
> The right-edge integral is $LX\!\int_0^L dy = L^2 X$; the top-edge integral is $LY\!\int_L^0 dx = LY\cdot(0 - L) = -L^2 Y$. Hence
> $$T_1 = \oint_{c_L} A = L^2 X - L^2 Y = (X - Y)\,L^2.$$
> As a consistency check on the orientation, [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — for a $1$-form $\eta$ on the oriented surface $S$ with induced boundary orientation, $\oint_{\partial S}\eta = \int_S d\eta$, applied to each matrix entry of $A$ — gives
> $$\oint_{c_L} A = \int_{S_L} dA = \int_{S_L}(X - Y)\,dx \wedge dy = (X - Y)\,L^2 \qquad \text{(} dA = (X-Y)\,dx \wedge dy \text{ from Step 1)},$$
> in agreement. The first-order contribution to the holonomy is therefore $-T_1 = -(X - Y)L^2$, and it is $O(L^2)$.

**Step 4: The second-order Dyson term is $O(L^4)$; compute it exactly.**

Parametrising each edge over an equal quarter of $[0,1]$, the second-order integrand is piecewise constant, and the ordered double integral evaluates to $L^4\big(\tfrac12 X^2 + \tfrac12 Y^2 - YX\big)$.

> [!note]- Derivation
> Choose the parametrisation $c_L : [0,1] \to \mathbb{R}^2$ that traverses the bottom, right, top, left edges over the intervals $[0,\tfrac14]$, $[\tfrac14,\tfrac12]$, $[\tfrac12,\tfrac34]$, $[\tfrac34,1]$ respectively, at constant speed on each. This is an orientation-preserving reparametrisation of the loop, and holonomy is invariant under such reparametrisation ([[Thm - Properties of Parallel Transport|Thm - Properties of Parallel Transport]]), so the answer does not depend on this choice; we make it only to render the integrand piecewise constant.
>
> On the right edge the coordinate $y$ runs from $0$ to $L$ over an interval of length $\tfrac14$, so $\dot y = L/(1/4) = 4L$, and by Step 2, $A(\dot c_L) = LX\,\dot y = 4L^2 X$ there. On the top edge the coordinate $x$ runs from $L$ to $0$ over an interval of length $\tfrac14$, so $\dot x = -L/(1/4) = -4L$, and $A(\dot c_L) = LY\,\dot x = -4L^2 Y$ there. Writing $g(\tau) := A(\dot c_L(\tau))$, we thus have the piecewise-constant function
> $$g(\tau) = \begin{cases} 0, & \tau \in [0, \tfrac14], \\ P := 4L^2 X, & \tau \in (\tfrac14, \tfrac12), \\ Q := -4L^2 Y, & \tau \in (\tfrac12, \tfrac34), \\ 0, & \tau \in (\tfrac34, 1]. \end{cases}$$
> (We verify the normalisation: $\int_{1/4}^{1/2} P\,d\tau = 4L^2 X\cdot\tfrac14 = L^2 X$ and $\int_{1/2}^{3/4} Q\,d\tau = -4L^2 Y\cdot\tfrac14 = -L^2 Y$, reproducing the edge integrals of Step 3.)
>
> The second-order term is the ordered integral
> $$T_2 := \int_0^1 d\tau_2 \int_0^{\tau_2} d\tau_1\, g(\tau_2)\,g(\tau_1) = \int_0^1 g(\tau_2)\,G(\tau_2)\,d\tau_2, \qquad G(\tau) := \int_0^\tau g(\tau_1)\,d\tau_1,$$
> where the inner integral is written as the antiderivative $G$. We evaluate $\int_0^1 g\,G$ over the four subintervals, using that $g \equiv 0$ on $[0,\tfrac14]$ and $(\tfrac34,1]$:
>
> - On $(\tfrac14, \tfrac12)$: $g(\tau_2) = P$ and $G(\tau_2) = \int_{1/4}^{\tau_2} P\,d\tau_1 = P\,(\tau_2 - \tfrac14)$ (since $g = 0$ before $\tfrac14$). Contribution:
> $$\int_{1/4}^{1/2} P\cdot P\,(\tau_2 - \tfrac14)\,d\tau_2 = P^2 \int_0^{1/4} u\,du = P^2\cdot\frac{(1/4)^2}{2} = \frac{P^2}{32} \qquad (u = \tau_2 - \tfrac14).$$
> - On $(\tfrac12, \tfrac34)$: $g(\tau_2) = Q$ and $G(\tau_2) = \int_{1/4}^{1/2} P\,d\tau_1 + \int_{1/2}^{\tau_2} Q\,d\tau_1 = \tfrac{P}{4} + Q\,(\tau_2 - \tfrac12)$. Contribution:
> $$\int_{1/2}^{3/4} Q\Big(\tfrac{P}{4} + Q\,(\tau_2 - \tfrac12)\Big)\,d\tau_2 = Q\,\tfrac{P}{4}\cdot\tfrac14 + Q^2\int_0^{1/4} u\,du = \frac{QP}{16} + \frac{Q^2}{32} \qquad (u = \tau_2 - \tfrac12).$$
>
> Summing the two contributions (the others vanish),
> $$T_2 = \frac{P^2}{32} + \frac{QP}{16} + \frac{Q^2}{32}.$$
> Substituting $P = 4L^2 X$ and $Q = -4L^2 Y$, so $P^2 = 16L^4 X^2$, $Q^2 = 16L^4 Y^2$, and $QP = (-4L^2 Y)(4L^2 X) = -16 L^4 YX$,
> $$T_2 = \frac{16 L^4 X^2}{32} + \frac{-16 L^4 YX}{16} + \frac{16 L^4 Y^2}{32} = L^4\Big(\tfrac12 X^2 - YX + \tfrac12 Y^2\Big).$$
> Every term carries the factor $L^4$: the second-order Dyson term is $O(L^4)$. The reason is structural — each factor $g$ is $O(L^2)$ (a constant matrix such as $4L^2 X$), so a product of two of them is $O(L^4)$; this is special to the present connection, whose vanishing at $b_0$ makes $A(\dot c_L)$ one order smaller than the generic $O(L)$.

**Step 5: Assemble the expansion and verify $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$; locate the commutator.**

Collecting the Dyson terms gives $\operatorname{hol}(c_L) = 1_n - (X-Y)L^2 + O(L^4)$, which matches $1_n - \int_{S_L} F$ to order $O(L^3)$; the commutator $[Y,X]$ enters $\int_{S_L} F$ only at order $L^4$, through the $A \wedge A$ term, hence lies beneath the theorem's accuracy.

> [!note]- Derivation
> By the Dyson series (recalled in the Problem Statement, and convergent by [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the path-ordered-exponential theorem]]),
> $$\operatorname{hol}(c_L) = 1_n - T_1 + T_2 - T_3 + \cdots,$$
> where $T_j$ is the $j$-th ordered integral. Since each factor $g = A(\dot c_L)$ is $O(L^2)$ and the ordered $j$-fold integral of an $O(L^2)$ function over the simplex $\{0 \le \tau_1 \le \cdots \le \tau_j \le 1\}$ of volume $1/j!$ is $O(L^{2j})$, we have $T_j = O(L^{2j})$; in particular $T_3 = O(L^6)$ and all higher terms are $O(L^6)$. Combining Steps 3 and 4,
> $$\operatorname{hol}(c_L) = 1_n - (X - Y)L^2 + L^4\Big(\tfrac12 X^2 + \tfrac12 Y^2 - YX\Big) + O(L^6).$$
> Truncating at the theorem's stated accuracy $O(L^3)$ (that is, discarding the $O(L^4)$ term),
> $$\operatorname{hol}(c_L) = 1_n - (X - Y)L^2 + O(L^3).$$
> On the other hand, from Step 1,
> $$1_n - \int_{S_L} F = 1_n - (X - Y)L^2 - \frac{L^4}{4}[Y,X],$$
> whose $O(L^2)$ part is also $1_n - (X-Y)L^2$. Therefore
> $$\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3),$$
> which is exactly the claim of [[Thm - Curvature is the Infinitesimal Holonomy|the infinitesimal-holonomy theorem]] for this loop.
>
> *Where the commutator lives.* The non-abelian correction $[Y,X]$ appears in the curvature through the quadratic piece $A \wedge A = xy[Y,X]\,dx\wedge dy$, and its flux is $\int_{S_L} A \wedge A = \tfrac{L^4}{4}[Y,X]$ (Step 1), which is $O(L^4)$. It is therefore invisible at the theorem's controlled order $O(L^3)$: to that order the holonomy equals $1_n - \int_{S_L} dA + O(L^3)$, the *abelian* answer, and the commutator is a genuinely higher-order effect. This is the manifestation, in a concrete example, of the fact that the general proof's leading antisymmetric term $-\int_S [A_j(0), A_k(0)]\,dx^j\wedge dx^k$ vanishes here because $A_j(0) = 0$: the connection sits at zero at the base point, so its self-commutator is pushed from the generic order $L^2$ down to $L^4$.

> [!note]- Complete formal solution
> **Claim.** For $A = xX\,dy + yY\,dx$ with $X, Y \in \mathfrak{g}$ constant and $c_L = \partial([0,L]^2)$ counterclockwise from the origin,
> $$\operatorname{hol}(c_L) = 1_n - (X-Y)L^2 + L^4\big(\tfrac12 X^2 + \tfrac12 Y^2 - YX\big) + O(L^6) = 1_n - \int_{S_L} F + O(L^3), \quad F = dA + A\wedge A.$$
>
> *Curvature.* With $A_x = yY$, $A_y = xX$: $dA = (\partial_x A_y - \partial_y A_x)\,dx\wedge dy = (X - Y)\,dx\wedge dy$, and $A\wedge A = [A_x, A_y]\,dx\wedge dy = xy[Y,X]\,dx\wedge dy$, so $F = (X - Y + xy[Y,X])\,dx\wedge dy$ and $\int_{S_L} F = (X-Y)L^2 + \tfrac{L^4}{4}[Y,X]$.
>
> *Holonomy by the Dyson series.* Along $c_L$, $A(\dot c_L) = yY\,\dot x + xX\,\dot y$ vanishes on the bottom edge ($y=0,\ \dot y=0$) and the left edge ($x=0,\ \dot x=0$), equals the constant $LX\,\dot y$ on the right edge ($x=L,\ \dot x = 0$), and equals the constant $LY\,\dot x$ on the top edge ($y=L,\ \dot y = 0$). The first-order term is $T_1 = \oint_{c_L} A = L^2 X - L^2 Y = (X-Y)L^2$ (equivalently $\int_{S_L} dA$ by Stokes). Parametrising each edge over an equal quarter of $[0,1]$ makes $g(\tau) := A(\dot c_L(\tau))$ piecewise constant with values $P = 4L^2 X$ on $(\tfrac14,\tfrac12)$, $Q = -4L^2 Y$ on $(\tfrac12,\tfrac34)$, and $0$ elsewhere; the second-order term is $T_2 = \tfrac{P^2}{32} + \tfrac{QP}{16} + \tfrac{Q^2}{32} = L^4(\tfrac12 X^2 - YX + \tfrac12 Y^2)$. Since each $g$ is $O(L^2)$, $T_j = O(L^{2j})$ and $T_3, T_4, \dots = O(L^6)$. Hence
> $$\operatorname{hol}(c_L) = 1_n - T_1 + T_2 + O(L^6) = 1_n - (X-Y)L^2 + L^4\big(\tfrac12 X^2 + \tfrac12 Y^2 - YX\big) + O(L^6).$$
>
> *Verification.* Discarding the $O(L^4)$ term, $\operatorname{hol}(c_L) = 1_n - (X-Y)L^2 + O(L^3)$; and $1_n - \int_{S_L} F = 1_n - (X-Y)L^2 - \tfrac{L^4}{4}[Y,X]$ has the same $O(L^2)$ part. Therefore $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$. The commutator $[Y,X]$ enters $\int_{S_L} F$ only at $O(L^4)$, via $\int_{S_L} A\wedge A = \tfrac{L^4}{4}[Y,X]$, and is thus beneath the theorem's $O(L^3)$ accuracy: the connection's vanishing at the base point suppresses the self-commutator from the generic order $L^2$ to order $L^4$. $\blacksquare$

> [!note]- Independent sanity check: the exact holonomy as a product of two exponentials
> Because $A(\dot c_L)$ is a *constant* matrix along each edge, the transport across each edge is an ordinary matrix exponential, and we can compute $\operatorname{hol}(c_L)$ exactly with no truncation. On an edge where $A(\dot c_L)$ is constant, the parallel-transport equation $\dot v = -A(\dot c_L)v$ has constant coefficient, so its transport is $\exp\!\big({-}\int_{\text{edge}} A\big)$ (this is the commuting case of the path-ordered exponential, [[Def - Path-Ordered Exponential|Def - Path-Ordered Exponential]]). By Step 2 and Step 3 the four edge transports are
> $$U_{\text{bottom}} = 1_n, \quad U_{\text{right}} = \exp(-L^2 X), \quad U_{\text{top}} = \exp\!\big({-}({-}L^2 Y)\big) = \exp(L^2 Y), \quad U_{\text{left}} = 1_n,$$
> using $\int_{\text{right}} A = L^2 X$ and $\int_{\text{top}} A = -L^2 Y$. By the concatenation law ([[Thm - Properties of Parallel Transport|Thm - Properties of Parallel Transport]]), the transport along the loop (bottom, then right, then top, then left) is the product in reverse order:
> $$\operatorname{hol}(c_L) = U_{\text{left}}\,U_{\text{top}}\,U_{\text{right}}\,U_{\text{bottom}} = \exp(L^2 Y)\,\exp(-L^2 X).$$
> Taylor-expanding with $a := L^2$,
> $$\exp(aY)\exp(-aX) = \big(1_n + aY + \tfrac{a^2}{2}Y^2 + \cdots\big)\big(1_n - aX + \tfrac{a^2}{2}X^2 - \cdots\big) = 1_n + a(Y - X) + a^2\big(\tfrac12 X^2 + \tfrac12 Y^2 - YX\big) + O(a^3),$$
> and with $a = L^2$ this is $1_n - (X-Y)L^2 + L^4(\tfrac12 X^2 + \tfrac12 Y^2 - YX) + O(L^6)$ — exactly the Dyson result of Step 5, term for term. This confirms both the first- and second-order coefficients. Notice also that the exact holonomy is *not* $\exp\!\big({-}\int_{S_L} F\big)$: their $L^4$ terms differ ($\tfrac12 X^2 + \tfrac12 Y^2 - YX$ versus $-\tfrac14[Y,X]$), as they must, since equality of holonomy with $\exp(-\int_S F)$ holds only in the abelian case ([[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral]]).

> [!warning] Illegal but tempting route: reading the commutator off $F$ as an $O(L^2)$ term
> It is tempting to argue: "$F$ has the piece $xy[Y,X]\,dx\wedge dy$, therefore the holonomy expansion $1_n - \int_{S_L} F$ shows the commutator $[Y,X]$ already at leading order." This is wrong on two counts. First, the flux of that piece is $\int_{S_L} xy[Y,X]\,dx\wedge dy = \tfrac{L^4}{4}[Y,X]$, which is $O(L^4)$, *not* $O(L^2)$, because the coefficient $xy$ vanishes to second order at the corner $b_0 = (0,0)$. Second, and more subtly, one might try to salvage the claim by invoking the general proof's antisymmetric term $-\int_{S}[A_j(0),A_k(0)]\,dx^j\wedge dx^k$; but here $A_j(0) = 0$, so this term is identically zero, and the commutator does *not* appear at order $L^2$. The extra condition under which the commutator *would* appear at order $L^2$ is $A(b_0) \ne 0$: if the connection had a non-zero constant part $A(b_0) = A_x(0)\,dx + A_y(0)\,dy$ with $[A_x(0), A_y(0)] \ne 0$, then $\int_S A\wedge A \approx [A_x(0),A_y(0)]\,L^2$ would contribute at order $L^2$. The present connection is engineered to sit at zero at the base point precisely so that this leading commutator is absent, which is why the drill exposes the order-counting so cleanly.

---

# Key Takeaways

**The holonomy of a small loop is, to second order, one minus the flux of the curvature through the loop — but the order at which each piece of the curvature contributes depends on how the connection behaves at the base point.** The general theorem $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$ packages two contributions: the abelian flux $\int_S dA$, which is always $O(L^2)$, and the non-abelian flux $\int_S A\wedge A = \int_S [A_x, A_y]\,dx\wedge dy$, whose order depends on the size of $A$ near $b_0$. When $A(b_0) \ne 0$, the integrand $[A_x, A_y]$ is $O(1)$ and the commutator contributes at $O(L^2)$, on the same footing as $dA$; when $A(b_0) = 0$, as here, the integrand is $O(L^2)$ pointwise and the commutator is pushed to $O(L^4)$, below the theorem's accuracy. The reusable principle: *reading a term off the curvature is not the same as knowing its order in the loop-size expansion* — one must integrate the actual coefficient over the actual loop, because the flux weights each region of the surface by how large the curvature is there. The trigger for this caution is any statement of the form "the curvature has such-and-such a term, so the holonomy shows it"; the correct move is to integrate and count powers of $L$.

**When a connection restricts to a constant Lie-algebra element on each leg of a loop, the path-ordering evaporates and the holonomy is an ordinary product of matrix exponentials.** The path-ordered exponential exists precisely because $A(\dot c(\tau_1))$ and $A(\dot c(\tau_2))$ generally fail to commute; but on a straight edge where $A(\dot c)$ is a *constant* matrix, that matrix commutes with itself and the ordered integral collapses to $\exp\!\big({-}\int_{\text{edge}} A\big)$. Recognising this turns an infinite Dyson series into a finite product — here $\exp(L^2 Y)\exp(-L^2 X)$, exact to all orders. The transferable diagnostic: on any piecewise-linear loop, check whether the pulled-back connection is constant on each segment; if so, compute the exact holonomy as a reverse-order product of segment exponentials and use it to check any perturbative expansion. This is the same mechanism that makes lattice gauge theory tractable — the link variables are exactly the edge exponentials of this kind — and it is why "compute the small-square holonomy" is the fundamental building block of the curvature-as-infinitesimal-holonomy picture.

**The residual non-commutativity of the two exponentials, not the curvature flux, controls the holonomy beyond leading order — and the two disagree already at the next order.** The exact answer $\exp(L^2 Y)\exp(-L^2 X)$ expands as $1_n - (X-Y)L^2 + L^4\big(\tfrac12(X-Y)^2 + \tfrac12[X,Y]\big) + O(L^6)$, where the algebraic identity $\tfrac12 X^2 + \tfrac12 Y^2 - YX = \tfrac12(X-Y)^2 + \tfrac12[X,Y]$ splits the $L^4$ coefficient into a "square of the first-order term" part $\tfrac12(X-Y)^2$ and a genuine commutator part $\tfrac12[X,Y]$. Neither matches the $-\tfrac14[Y,X]$ that $1_n - \int_{S_L} F$ would predict at $L^4$, which is the concrete reason the identity $\operatorname{hol} = \exp(-\int_S F)$ fails in the non-abelian case: only when $[X,Y] = 0$ (abelian structure group, or commuting $X, Y$) do the two exponentials merge into $\exp\!\big({-}(X-Y)L^2\big)$ and the holonomy become the exact exponential of minus the curvature flux, as on [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]]. The general lesson for spaced practice: the small-loop expansion is a Baker–Campbell–Hausdorff computation in disguise, and the commutator that BCH produces is exactly the field strength the holonomy "measures" — but only to leading order, and only with the correct order-counting. A natural companion drill is [[Ex - The Dyson Series for a Two-Level System|Ex - The Dyson Series for a Two-Level System]], where the same second-order Dyson term is computed for a time-dependent two-level Hamiltonian and shown to differ from $\tfrac12(\int A)^2$ exactly when the two matrix pieces fail to commute.
