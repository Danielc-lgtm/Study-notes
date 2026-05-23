---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Involutive Distribution"
  - "Thm - Frobenius Theorem in Forms Language"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry, frobenius, contact]
---

# Problem Statement

On $\mathbb{R}^3$ with coordinates $(x, y, z)$, consider the **standard contact form**

$$\alpha = dz - y\,dx,$$

and let $D = \ker \alpha$ be the rank-$2$ distribution it defines.

**(a)** Find an explicit local frame $\{X_1, X_2\}$ for $D$.

**(b)** Show that $D$ is *not* involutive at any point of $\mathbb{R}^3$ — equivalently, by [[Thm - Frobenius Theorem in Forms Language]], compute $\alpha \wedge d\alpha$ and observe it is nowhere zero.

**(c)** Conclude that $D$ has no integral surface passing through any point.

**(d)** Give the geometric picture: as you move in the $x$-direction, the plane $D_{(x, y, z)}$ twists in a helical pattern.

**Recall:**

![[Def - Involutive Distribution#The Definition]]

![[Thm - Frobenius Theorem in Forms Language#Statement]]

For a codimension-$1$ distribution $D = \ker \omega$ defined by a single $1$-form $\omega$ on $\mathbb{R}^3$: $D$ is involutive $\iff$ $\omega \wedge d\omega = 0$.

---

# Convergent Strategy

**Problem class:** Non-involutivity check for a codimension-$1$ distribution defined by a single $1$-form. Pattern: compute $\omega \wedge d\omega$ as a $3$-form, observe it is non-zero everywhere, conclude non-involutivity by the forms criterion.

**Assumption pattern:** The $1$-form $\alpha = dz - y\,dx$ is a specific algebraic expression in coordinates. The exterior derivative computation $d\alpha$ is direct ($d^2 = 0$ on coordinate functions, Leibniz on wedge products), and then $\alpha \wedge d\alpha$ is a wedge product of standard $1$-forms with explicit coefficients.

**Theorem routing:** [[Thm - Frobenius Theorem in Forms Language]] (criterion (e) for codimension-$1$): involutive $\iff$ $\omega \wedge d\omega = 0$. Compute and observe the answer is a non-zero $3$-form on $\mathbb{R}^3$. Cross-check via the vector-field criterion: find $X_1, X_2 \in \Gamma(D)$ with $[X_1, X_2] \notin D$.

**Key decision point:** The choice to use the forms criterion $\omega \wedge d\omega = 0$ (rather than the vector-field criterion $[X, Y] \in D$) is more efficient — a single algebraic identity to check. But computing the explicit non-vanishing bracket is also illuminating, showing geometrically *which* direction the bracket escapes into.

---

# Legal Operations Used

1. **Test involutivity by $1$-forms** (operation 5 from the topic page). For a codimension-$1$ distribution $D = \ker \alpha$, the criterion reduces to checking $\alpha \wedge d\alpha = 0$ — a single algebraic identity.

2. **Test involutivity by Lie brackets on a local frame** (operation 4 from the topic page). Find $X_1, X_2 \in \Gamma(D)$, compute $[X_1, X_2]$, check if it is in $D$.

3. **Apply $d^2 = 0$ to simplify computations** (implicit in standard form algebra). $d(dx) = d(dy) = d(dz) = 0$, so the exterior derivative reduces to products of partials.

---

# Hints

> [!note]- Hint 1
> To find a frame for $D = \ker \alpha$, find two linearly independent vector fields $X_1, X_2$ with $\alpha(X_i) = 0$. Try $X_1 = \partial_y$ (easy: $\alpha(\partial_y) = dz(\partial_y) - y\cdot dx(\partial_y) = 0 - 0 = 0$). For $X_2$, look for $\partial_x + ?\partial_z$ — the coefficient on $\partial_z$ is forced by $\alpha(X_2) = 0$.

> [!note]- Hint 2
> Compute $d\alpha$. Use $d(fg\,dx) = df \wedge g\,dx + f\,d(g\,dx)$ and the fact that $d(dx) = 0$.

> [!note]- Hint 3
> Compute $\alpha \wedge d\alpha$. The result is a $3$-form on $\mathbb{R}^3$, which has at most $\binom{3}{3} = 1$ independent basis element, $dx \wedge dy \wedge dz$. Identify the coefficient.

> [!note]- Hint 4
> Cross-check via Lie brackets: compute $[X_1, X_2]$ for $X_1 = \partial_y$, $X_2 = \partial_x + y\partial_z$.

> [!note]- Hint 5
> Geometric picture: at $(x, y, z)$, the plane $D_{(x,y,z)} = \ker \alpha = \{(a, b, c) : c = ya\}$ is spanned by $(0, 1, 0)$ and $(1, 0, y)$. The second vector — the $\partial_x$-direction adjusted by $y\partial_z$ — rotates as $y$ changes.

---

# Solution

The plan: (a) find a frame for $D$, (b) verify non-involutivity via the $\alpha \wedge d\alpha$ criterion *and* cross-check by computing $[X_1, X_2]$, (c) conclude no integral surface exists, (d) visualize.

**Part (a): Frame for $D = \ker \alpha$.**

> [!note]- Derivation
> A vector $V = a\partial_x + b\partial_y + c\partial_z \in T_{(x,y,z)}\mathbb{R}^3$ lies in $D_{(x,y,z)} = \ker \alpha$ iff
> $$\alpha(V) = dz(V) - y\cdot dx(V) = c - ya = 0 \quad \iff \quad c = ya.$$
>
> So $D_{(x,y,z)}$ is the $2$-plane $\{(a, b, ya) : a, b \in \mathbb{R}\}$, spanned by $(0, 1, 0)$ and $(1, 0, y)$.
>
> As vector fields:
> $$X_1 = \partial_y, \qquad X_2 = \partial_x + y\partial_z.$$
>
> Check: $\alpha(X_1) = dz(\partial_y) - y\cdot dx(\partial_y) = 0 - 0 = 0$. $\alpha(X_2) = dz(\partial_x + y\partial_z) - y\cdot dx(\partial_x + y\partial_z) = y - y \cdot 1 = 0$. Both are in $\ker \alpha$.
>
> Linear independence: at any point, the $\partial_y$ and $\partial_x + y\partial_z$ are independent (their first three components $(0, 1, 0)$ and $(1, 0, y)$ are linearly independent in $\mathbb{R}^3$, since the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \\ 0 & y \end{pmatrix}$ has rank $2$). So $\{X_1, X_2\}$ is a frame for $D$ on all of $\mathbb{R}^3$.

**Part (b): Non-involutivity via $\alpha \wedge d\alpha$.**

> [!note]- Derivation
> Compute $d\alpha$:
> $$d\alpha = d(dz - y\,dx) = d(dz) - d(y\,dx) = 0 - dy \wedge dx = -dy \wedge dx = dx \wedge dy.$$
> (Using $d(dz) = 0$, $d(y\,dx) = dy \wedge dx + y\,d(dx) = dy \wedge dx + 0$, and $-dy\wedge dx = dx \wedge dy$.)
>
> Compute $\alpha \wedge d\alpha$:
> $$\alpha \wedge d\alpha = (dz - y\,dx) \wedge dx \wedge dy.$$
> Distribute: $dz \wedge dx \wedge dy - y\,dx \wedge dx \wedge dy$. The second term has $dx \wedge dx = 0$, so it vanishes.
> $$\alpha \wedge d\alpha = dz \wedge dx \wedge dy = dx \wedge dy \wedge dz,$$
> using $dz \wedge dx \wedge dy = -dx \wedge dz \wedge dy = dx \wedge dy \wedge dz$.
>
> This is the standard volume form on $\mathbb{R}^3$, *nowhere zero*. So $\alpha \wedge d\alpha \neq 0$ everywhere.
>
> By the codimension-$1$ Frobenius criterion (Corollary to [[Thm - Frobenius Theorem in Forms Language]]), $D$ is *not* involutive at any point.

**Part (b) cross-check via Lie brackets.**

> [!note]- Derivation
> $$[X_1, X_2] = [\partial_y, \partial_x + y\partial_z] = [\partial_y, \partial_x] + [\partial_y, y\partial_z].$$
> $[\partial_y, \partial_x] = 0$ (coordinate vector fields commute). $[\partial_y, y\partial_z] = (\partial_y y)\partial_z + y[\partial_y, \partial_z] = 1\cdot\partial_z + 0 = \partial_z$.
>
> So $[X_1, X_2] = \partial_z$.
>
> Is $\partial_z \in D$? Check $\alpha(\partial_z) = dz(\partial_z) - y\,dx(\partial_z) = 1 - 0 = 1 \neq 0$. So $\partial_z \notin \ker\alpha = D$.
>
> Hence $[X_1, X_2] \notin D$, confirming non-involutivity. The escape direction is $\partial_z$ — the "vertical" direction perpendicular to the contact plane.

**Part (c): No integral surface.**

> [!note]- Derivation
> By [[Thm - The Frobenius Theorem]] (vector-field version) or [[Thm - Frobenius Theorem in Forms Language]] (forms version), a distribution admits integral submanifolds through every point iff it is involutive. Since $D$ is *not* involutive (parts (b)), $D$ has *no* integral $2$-surface passing through any point.
>
> Concretely: suppose $\Sigma$ were an integral surface through $(x_0, y_0, z_0)$. Then $T_p\Sigma = D_p$ for $p \in \Sigma$. In particular $X_1, X_2 \in \Gamma(D|_\Sigma)$ are tangent vector fields on $\Sigma$, and their bracket $[X_1, X_2]$ must be tangent to $\Sigma$ — i.e. in $D$. But we computed $[X_1, X_2] = \partial_z \notin D$. Contradiction. So no such $\Sigma$ exists.

**Part (d): Geometric picture — the helical twist.**

> [!note]- Derivation
> At $(x, y, z)$, the plane $D_{(x, y, z)}$ is spanned by:
> - $X_1|_{(x,y,z)} = (0, 1, 0)$ — always pointing in the $\partial_y$ direction.
> - $X_2|_{(x,y,z)} = (1, 0, y)$ — pointing in $\partial_x + y\partial_z$.
>
> So $D_{(x,y,z)}$ is the plane through $(x, y, z)$ containing the $\partial_y$ axis and the direction $(1, 0, y)$. As $y$ changes, the second spanning vector tilts: at $y = 0$ it is horizontal $(1, 0, 0)$; at $y = 1$ it is at slope $1$ in the $z$-direction $(1, 0, 1)$; at $y = -1$ it tilts the other way $(1, 0, -1)$.
>
> Moving along the $\partial_x$-direction at constant $y$, $z$: the plane rotates not at all (the plane equation depends only on $y$, not $x$). Moving along the $\partial_y$-direction at constant $x$, $z$: the plane rotates (the "$\partial_z$"-component coefficient $y$ changes linearly). This is the *helical screw twist*: the plane rotates around the $\partial_y$-axis as you translate in $y$.
>
> The picture: imagine standing at the origin, looking out the $\partial_x$-axis. The contact plane $D_0$ is the $xy$-plane (slope $y = 0$). Step in the $\partial_y$-direction; the plane tilts up by $1$ unit per unit of $y$. The plane "screws" around the $y$-axis as you translate. This screwing is the geometric content of non-involutivity — there is no surface that "absorbs" all these tilted planes consistently.

> [!note]- Complete formal solution
> **(a)** $\alpha(V) = c - ya = 0$ for $V = (a, b, c)$, so $D_{(x,y,z)} = \{(a, b, ya)\}$, spanned by $X_1 = \partial_y$ and $X_2 = \partial_x + y\partial_z$. Both have $\alpha(X_i) = 0$, and they are linearly independent at every point.
>
> **(b)** $d\alpha = -dy \wedge dx = dx \wedge dy$. Then $\alpha \wedge d\alpha = (dz - y\,dx)\wedge dx \wedge dy = dz \wedge dx \wedge dy - y\,dx\wedge dx\wedge dy = dx \wedge dy \wedge dz + 0 = dx \wedge dy \wedge dz$, the standard volume form — nowhere zero. By [[Thm - Frobenius Theorem in Forms Language]], $D$ is not involutive at any point.
>
> *Cross-check.* $[X_1, X_2] = [\partial_y, \partial_x + y\partial_z] = (\partial_y y)\partial_z = \partial_z$. $\alpha(\partial_z) = 1 \neq 0$, so $\partial_z \notin D$. Confirms $[X_1, X_2] \notin D$.
>
> **(c)** Suppose $\Sigma$ is an integral surface through some point. Then $X_1, X_2$ restrict to vector fields tangent to $\Sigma$, and their bracket $[X_1, X_2]$ must also be tangent. But $[X_1, X_2] = \partial_z \notin D$. Contradiction; no integral surface exists.
>
> **(d)** Geometrically, $D_{(x, y, z)}$ is the plane $z' - z = y(x' - x)$ in tangent space coordinates — the plane through $(x, y, z)$ containing $\partial_y$ and the tilted direction $(1, 0, y)$. As $y$ changes (motion in the $\partial_y$-direction), the tilt grows linearly in $y$, producing a helical screw rotation around the $y$-axis. The contact plane field twists everywhere, and this twist is the geometric obstruction to an integral surface. $\blacksquare$

> [!warning] Illegal but tempting alternative — looking for a "near-integral" surface
> It is tempting to think one can find an "approximate" integral surface — a $2$-manifold tangent to $D$ along most of its area, with small failures only "on a set of measure zero." This is *impossible*: non-involutivity means the obstruction is *uniform*, present at every point. The bracket $[X_1, X_2] = \partial_z$ is a non-zero smooth field, not an exceptional discontinuity. There is no $2$-manifold tangent to $D$ along any open set — even an arbitrarily small one. This is one of the sharpest manifestations of the local-to-global obstruction in distribution theory.

---

# Key Takeaways

**The single algebraic identity $\alpha \wedge d\alpha = 0$ characterizes involutivity of a codimension-$1$ distribution.** This is the most computationally efficient involutivity test in the entire theory: a single $3$-form (in dimension $3$) or $(n+1)$-form (in dimension $n$) computed and checked. For higher-codimension distributions, the analogue is $d\omega^i \wedge \omega^1 \wedge \cdots \wedge \omega^{n-k} = 0$ for each $i$. The trigger: whenever a distribution is defined by an annihilating $1$-form, *first* compute $\omega \wedge d\omega$ and check whether it vanishes. If it doesn't, you have non-involutivity certified in one step.

**The standard contact form $\alpha = dz - y\,dx$ is the prototype of a *maximally non-involutive* distribution.** Beyond just $\alpha \wedge d\alpha \neq 0$, the value $\alpha \wedge d\alpha = dx \wedge dy \wedge dz$ is the *standard volume form* — the strongest possible non-vanishing. This makes the standard contact form into a **contact form** in the strict sense: a $1$-form on a $(2n+1)$-manifold with $\alpha \wedge (d\alpha)^n$ nowhere zero. Contact geometry is the systematic study of such maximally non-integrable structures, and the standard form is the local model (by Darboux's theorem). The trigger to recognize the contact pattern: any time $\omega \wedge d\omega$ is *not just non-zero, but a volume form*, you have a contact structure, with all the rich geometry that entails.

**Non-involutivity manifests geometrically as a helical screw twist.** The picture in this exercise — the contact plane rotates around the $y$-axis as you translate in $y$, with no $2$-surface that "absorbs" all these tilted planes — is the universal geometric meaning of non-involutivity for codimension-$1$ distributions. Other examples: the rolling-ball constraint, the parallel-parking distribution, the skating constraint. Each has the same fundamental structure: a plane field that *twists*, with the twist quantified by $\omega \wedge d\omega$. The trigger to recognize: when constraints couple displacement in different directions in a path-dependent way (you can reach a configuration via a sequence of small allowed moves, but not directly), you are in a non-involutive setting.

**Non-involutivity in mechanics: nonholonomic constraints generate motion in "forbidden" directions through bracket maneuvers.** A skate on ice has the constraint $\omega = -\sin\phi\,dx + \cos\phi\,dy = 0$ (velocity along the blade), giving a rank-$2$ distribution on $(x, y, \phi)$-space. This distribution is non-involutive — $\omega \wedge d\omega \neq 0$ — and the bracket of two tangent vector fields generates a "rotational" displacement not in the distribution. This is why a skater can change orientation by an angled push, and why a car can parallel-park (small back-forth maneuvers generate sideways motion). The standard contact distribution is the geometric model for these constraints. *Companion exercise:* [[Ex - An Involutive Distribution from Three Vector Fields]] gives the contrast — a distribution whose involutivity test passes/fails depending on the specific brackets.
