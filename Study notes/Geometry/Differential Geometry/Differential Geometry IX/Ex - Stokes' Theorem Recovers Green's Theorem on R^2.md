---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Green's Theorem"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, differential-geometry, stokes, greens-theorem]
---

# Problem Statement

Let $D \subseteq \mathbb{R}^2$ be a compact 2-manifold with smooth boundary $\partial D$ (carrying the induced orientation), and let $\omega = P\,dx + Q\,dy$ be a smooth 1-form on a neighborhood of $D$. Using [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem on manifolds]], show that
$$\oint_{\partial D}P\,dx + Q\,dy = \int_D\Big(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\Big)dx\wedge dy.$$
Verify that this is exactly the statement of [[Thm - Green's Theorem|Green's theorem]] in classical vector-calculus notation, and that the induced orientation on $\partial D$ matches the standard "counterclockwise" convention.

**Recall:**

![[Thm - Stokes' Theorem on Manifolds#Statement]]

Green's theorem: for a planar region $D$ with smooth boundary $\partial D$ oriented counterclockwise, and a 1-form $P\,dx + Q\,dy$ smooth on $D$:

![[Thm - Green's Theorem]]

The induced orientation on $\partial D \subseteq D$ is the one in which the outward-normal-to-boundary $N$ and a positive tangent vector $T$ satisfy: $(N, T)$ is positively oriented in $D$ — which on a planar region with the standard $dx\wedge dy$ orientation corresponds to $T$ pointing counterclockwise.

---

# Convergent Strategy

**Problem class:** Specialization of Stokes's theorem on a manifold to a specific dimensionality / setting. The general theorem $\int_M d\omega = \int_{\partial M}\omega$ becomes a familiar classical identity once the [[Def - Dimension|dimensions]] are fixed.

**Assumption pattern:** $D$ is a compact 2-manifold with boundary in $\mathbb{R}^2$, $\omega$ a 1-form. We have $n = 2$, $\omega$ is a $(n-1) = 1$-form, the boundary $\partial D$ is a 1-manifold (a curve), and the manifold-with-boundary structure is provided by the planar embedding. All hypotheses of Stokes are met.

**Theorem routing:** [[Thm - Stokes' Theorem on Manifolds]] directly: $\int_D d\omega = \int_{\partial D}\omega$. The only computational task is to expand $d\omega$ in coordinates and recognize the result as the integrand of Green's theorem.

**Key decision point:** The only choice is whether to compute $d\omega$ directly in coordinates (giving $(\partial_x Q - \partial_y P)\,dx\wedge dy$) or to invoke some more general framework. The direct coordinate computation is the right choice: it makes the identification with Green's theorem immediate and transparent.

---

# Legal Operations Used

1. **Operation 2 (use Stokes to swap interior for boundary)** from the [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem#Legal Operations|topic page]]. Directly applied with $n = 2$ and $\omega$ a 1-form. The interior integral $\int_D d\omega$ is computed via Stokes by recognizing it as the boundary integral $\int_{\partial D}\omega$.

2. **Operation 10 (read the boundary orientation off "outward-first")** from the topic page. Used to verify that the induced orientation on $\partial D$ matches the counterclockwise convention in $\mathbb{R}^2$.

---

# Hints

> [!note]- Hint 1
> Compute $d(P\,dx + Q\,dy)$ explicitly using the rules $d(P\,dx) = dP\wedge dx + P\,d(dx) = dP\wedge dx$ (since $d(dx) = 0$). Then $dP = (\partial_x P)\,dx + (\partial_y P)\,dy$.

> [!note]- Hint 2
> After computing $d\omega$, you should get $d\omega = (\partial_x Q - \partial_y P)\,dx\wedge dy$. Then apply Stokes directly: $\int_D d\omega = \int_{\partial D}\omega$.

> [!note]- Hint 3
> To match the induced orientation with "counterclockwise", think about the unit disc $D = \{x^2 + y^2 \leq 1\}$. The outward normal at a boundary point $(x, y) \in \partial D$ is $(x, y)$ itself. The boundary tangent $T$ must then satisfy "$N$ first, $T$ second is positive in $\mathbb{R}^2$", and with the standard $dx\wedge dy$ orientation, this forces $T$ to be the counterclockwise direction.

---

# Solution

The proof is two short computations followed by an orientation check. **Step 1** computes $d\omega$ in coordinates. **Step 2** applies Stokes's theorem on manifolds. **Step 3** verifies the boundary-orientation identification with the standard "counterclockwise" convention.

**Step 1: Compute $d\omega$ in coordinates.**

Apply the exterior derivative to $\omega = P\,dx + Q\,dy$:
$$d\omega = d(P\,dx) + d(Q\,dy) = dP\wedge dx + dQ\wedge dy,$$
using $d(P\,dx) = dP\wedge dx + P\,d(dx)$ and $d(dx) = 0$ (the differential of a coordinate function is closed).

> [!note]- Derivation
> The exterior derivative is a derivation: $d(P\alpha) = dP\wedge\alpha + P\,d\alpha$ for any function $P$ and form $\alpha$. Apply to $P\,dx$: $d(P\,dx) = dP\wedge dx + P\,d(dx) = dP\wedge dx$. Similarly $d(Q\,dy) = dQ\wedge dy$. Hence $d\omega = dP\wedge dx + dQ\wedge dy$.

Now expand $dP = \partial_xP\,dx + \partial_yP\,dy$ and $dQ = \partial_xQ\,dx + \partial_yQ\,dy$:
$$d\omega = (\partial_xP\,dx + \partial_yP\,dy)\wedge dx + (\partial_xQ\,dx + \partial_yQ\,dy)\wedge dy.$$
Wedging:
- $\partial_xP\,dx\wedge dx = 0$ (repeated factor).
- $\partial_yP\,dy\wedge dx = -\partial_yP\,dx\wedge dy$.
- $\partial_xQ\,dx\wedge dy = \partial_xQ\,dx\wedge dy$.
- $\partial_yQ\,dy\wedge dy = 0$ (repeated factor).

So
$$d\omega = (\partial_xQ - \partial_yP)\,dx\wedge dy.$$

> [!note]- Derivation
> The wedge product is antisymmetric in the order of differentials: $dy\wedge dx = -dx\wedge dy$ and $dx\wedge dx = 0 = dy\wedge dy$. Applying these to each of the four terms and collecting yields the displayed result. This is the *standard* expression for $d$ of a 1-form on $\mathbb{R}^2$, and it matches the curl-like quantity appearing in Green's theorem.

**Step 2: Apply Stokes's theorem.**

By [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem on manifolds]] applied to the oriented 2-manifold-with-boundary $D \subseteq \mathbb{R}^2$ (with $D$ carrying the standard $dx\wedge dy$ orientation and $\partial D$ the induced orientation) and the smooth $(n-1) = 1$-form $\omega$,
$$\int_D d\omega = \int_{\partial D}\omega.$$
Substituting $d\omega = (\partial_xQ - \partial_yP)\,dx\wedge dy$:
$$\int_D(\partial_xQ - \partial_yP)\,dx\wedge dy = \int_{\partial D}(P\,dx + Q\,dy).$$

> [!note]- Derivation
> This is a direct invocation of the manifold-version of Stokes's theorem. The hypotheses are met: $D$ is a compact oriented 2-manifold with boundary (the boundary is a smooth 1-manifold by assumption), $\omega$ is a smooth 1-form on a neighborhood of $D$ — in particular it is compactly supported on $D$. The conclusion is the displayed identity.

**Step 3: Verify the boundary-orientation matches "counterclockwise".**

Consider the unit disc $D = \{(x, y) : x^2 + y^2 \leq 1\}$ for concreteness. At a boundary point $(x_0, y_0) \in \partial D$, the outward normal is $N = (x_0, y_0)$ (the radial direction). A positively-oriented basis $T$ of $T_{(x_0, y_0)}\partial D$ (a 1-dimensional space) must satisfy $(N, T)$ positive in $T_{(x_0, y_0)}D$ — that is, $\det[N\ |\ T] > 0$ with the standard $dx\wedge dy$ orientation.

The unit tangent to the boundary at $(x_0, y_0)$ has two choices: $T_+ = (-y_0, x_0)$ (counterclockwise) and $T_- = (y_0, -x_0)$ (clockwise). Compute:
$$\det[N\ |\ T_+] = \det\begin{pmatrix}x_0 & -y_0 \\ y_0 & x_0\end{pmatrix} = x_0^2 + y_0^2 = 1 > 0,$$
$$\det[N\ |\ T_-] = \det\begin{pmatrix}x_0 & y_0 \\ y_0 & -x_0\end{pmatrix} = -x_0^2 - y_0^2 = -1 < 0.$$
So $T_+$ is the positively-oriented tangent, and the induced orientation on $\partial D$ is the counterclockwise direction — matching the standard convention of Green's theorem.

> [!note]- Derivation
> For a general planar region $D$ with smooth boundary, the same argument applies at each boundary point: the outward normal $N$ and a tangent $T$ to $\partial D$ form a positive basis of $T_pD$ exactly when $T$ points counterclockwise around the boundary. This is the *defining content* of the induced orientation: counterclockwise traversal of the boundary is "outward-first" in the planar case.

**Identification with Green's theorem.** Substituting the standard notation $\int_{\partial D}P\,dx + Q\,dy$ for the line integral and $\iint_D(\partial_xQ - \partial_yP)\,dA$ for the area integral, with $dA = dx\wedge dy$, we recover exactly Green's theorem:
$$\boxed{\oint_{\partial D}(P\,dx + Q\,dy) = \iint_D\Big(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\Big)\,dA.}$$

> [!note]- Complete formal solution
> Let $D \subseteq \mathbb{R}^2$ be a compact 2-manifold with smooth boundary $\partial D$, with $D$ carrying the standard orientation of $\mathbb{R}^2$ and $\partial D$ the induced orientation. Let $\omega = P\,dx + Q\,dy$ be a smooth 1-form on a neighborhood of $D$.
>
> Compute the exterior derivative:
> $$d\omega = d(P\,dx) + d(Q\,dy) = dP\wedge dx + dQ\wedge dy.$$
> Expanding $dP = \partial_xP\,dx + \partial_yP\,dy$ and similarly for $dQ$:
> $$d\omega = \partial_yP\,dy\wedge dx + \partial_xQ\,dx\wedge dy = (\partial_xQ - \partial_yP)\,dx\wedge dy.$$
>
> By [[Thm - Stokes' Theorem on Manifolds]] with $M = D$ (so $n = 2$) and the 1-form $\omega$,
> $$\int_D d\omega = \int_{\partial D}\omega.$$
> Substituting,
> $$\int_D(\partial_xQ - \partial_yP)\,dx\wedge dy = \int_{\partial D}(P\,dx + Q\,dy).$$
>
> The induced orientation on $\partial D$ is "outward-normal first": at $(x_0, y_0) \in \partial D$ with outward normal $N$, the tangent $T$ with $\det[N\ |\ T] > 0$ is the positively-oriented one — and this is the counterclockwise direction for any planar region.
>
> Hence the identity is Green's theorem with the standard counterclockwise convention on $\partial D$. $\blacksquare$

**Sanity-check via independent route.** Apply both sides to a simple test case: $D$ the unit disc and $\omega = -y\,dx + x\,dy$ (so $P = -y, Q = x$). Then $d\omega = (1 - (-1))\,dx\wedge dy = 2\,dx\wedge dy$, and $\int_D d\omega = 2\cdot\pi = 2\pi$. The line integral: parametrize $\partial D$ by $(x, y) = (\cos\theta, \sin\theta)$ counterclockwise, $dx = -\sin\theta\,d\theta$, $dy = \cos\theta\,d\theta$, so $\omega = -\sin\theta\cdot(-\sin\theta\,d\theta) + \cos\theta\cdot\cos\theta\,d\theta = (\sin^2\theta + \cos^2\theta)\,d\theta = d\theta$. The line integral is $\int_0^{2\pi}d\theta = 2\pi$. Both sides equal $2\pi$, confirming Green's theorem.

---

# Key Takeaways

**The classical theorems of vector calculus are special cases of Stokes's theorem on manifolds, distinguished only by the dimension and degree.** Green's theorem is $n = 2$, $\omega$ a 1-form. The divergence theorem is $n = 3$, $\omega$ a 2-form. Kelvin–Stokes is $n = 2$ (a surface in $\mathbb{R}^3$), $\omega$ a 1-form. The Fundamental Theorem of Calculus is $n = 1$, $\omega$ a 0-form (a function). All four are *the same identity* $\int_M d\omega = \int_{\partial M}\omega$, written in different [[Def - Dimension|dimensions]]. Once you have Stokes on manifolds, you have all four classical theorems for free — and you have the same theorem on manifolds without an embedding into $\mathbb{R}^N$, which is the point of the differential-geometric formulation. The trigger for using Stokes is *recognition that the integrand is a derivative of a simpler thing*, and the action is to convert one of the two integrals into the other.

**The induced orientation matches "counterclockwise" in the planar case by the outward-first convention.** This is the convention buried inside the standard statement of Green's theorem — most textbooks state it with "counterclockwise" and never explain that this is the same as the manifold-theoretic "induced orientation". The derivation is one explicit determinant computation: outward normal $N = (x, y)$, counterclockwise tangent $T = (-y, x)$, $\det[N\ |\ T] = 1 > 0$. This is the universal pattern: the induced orientation on a boundary is the "outward-first" one, which in any planar region is "counterclockwise" and in any 3D solid is "outward through each boundary face". Memorize this once and never re-derive.

**Stokes is the bridge between *closed* and *exact* forms in cohomology, even before invoking cohomology explicitly.** In the case of Green's theorem on a *non-simply-connected* region (e.g., an annulus), the same Stokes computation reveals that *closed* 1-forms ($d\omega = 0$, i.e. $\partial_xQ = \partial_yP$) need not be *exact* ($\omega = df$). The integral $\int_{\partial D}\omega$ over a non-trivial cycle can be nonzero even when $d\omega = 0$ — the obstruction is captured by [[Def - de Rham Cohomology|de Rham cohomology]] (computed in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|the next topic]]). The angular form on $\mathbb{R}^2\setminus\{0\}$, $\omega = (-y\,dx + x\,dy)/(x^2 + y^2)$, is the standard example: $d\omega = 0$ everywhere, but $\int_{\partial D}\omega = 2\pi$ for $D$ a disc containing the origin. Stokes does not fail here — it correctly diagnoses the absence of a global primitive.

**Companion exercise.** [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]] in [[Differential Geometry VIII — Differential Forms]] is the deeper version of this, computing $H^1_{dR}$ of the punctured plane via the angular form. [[Ex - The de Rham Cohomology of S^1 is R]] in this topic does the same on the circle. Together, these exercises drill the relationship between Stokes, closedness, and cohomology — which is the conceptual centerpiece of the topic.
