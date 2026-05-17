---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Inverse Function Theorem"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider the polar-coordinate map
$$F : (0, \infty) \times \mathbb{R} \to \mathbb{R}^2, \qquad F(r, \theta) = (r\cos\theta,\ r\sin\theta).$$

1. Compute the Jacobian matrix $JF(r,\theta)$ and its determinant. Conclude that $F$ is a local $C^\infty$-diffeomorphism near every point of its domain.
2. Show that $F$ is nevertheless **not** globally injective, and identify exactly the obstruction.
3. Exhibit a maximal open set on which $F$ *is* a global diffeomorphism, and name the additional hypothesis that makes the local conclusion global there.

**Recall:**

The objects in play are the Jacobian matrix, the inverse function theorem, and the distinction between local and global invertibility.

![[Thm - The Inverse Function Theorem#Statement]]

By the [[Thm - The Inverse Function Theorem|inverse function theorem]], a $C^k$ map $F$ between equal-dimensional Euclidean spaces with invertible derivative at a point $p_0$ is a $C^k$-diffeomorphism from some neighbourhood of $p_0$ onto an open set. The derivative $DF$ is represented by the Jacobian matrix $JF$, and it is invertible exactly when $\det JF \neq 0$. The conclusion is *local*: invertibility of $DF$ at every point gives only that $F$ is a *local* diffeomorphism everywhere, not a global one. A global conclusion requires a separate hypothesis — for instance restricting to a region on which $F$ is checked to be injective directly.

---

# Convergent Strategy

**Problem class.** This is a *local-invertibility* problem, and crucially it is also a problem about the *local/global gap* — the [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic strategy]] flags this as the recurring trap: invertible derivative everywhere does *not* yield a globally invertible map.

**Assumption pattern.** The map $F$ is the change to polar coordinates, smooth on its domain. Its Jacobian determinant is a single clean expression in $r$ alone, nonvanishing on the whole domain $r > 0$.

**Theorem routing.** Part 1 is a one-line application of the [[Thm - The Inverse Function Theorem|inverse function theorem]]: compute $\det JF$, observe it is nonzero, conclude local diffeomorphism. Part 2 requires *no theorem* — it is the observation that $F$ is $2\pi$-periodic in $\theta$, an explicit non-injectivity. Part 3 restricts the domain to a single period of $\theta$ and verifies global injectivity there directly.

**Key decision point.** The non-obvious content is recognizing that Parts 1 and 2 are not in conflict. The inverse function theorem's conclusion is *local* — it never promised global injectivity — so a map can be a local diffeomorphism at every point and still fail to be globally injective. The discipline is to state the local conclusion precisely and then investigate global behaviour as a *separate question*, which here is resolved by the periodicity.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Check a Jacobian determinant to claim local invertibility.** Compute $\det JF = r$; it is nonzero on the domain, so the inverse function theorem applies at every point.

2. **Resist promoting a local inverse to a global one.** Recognize that the inverse function theorem yields only a local statement, and investigate global injectivity separately.

3. **Restrict the domain and verify global injectivity by hand.** On a single period of $\theta$, check directly that $F$ is one-to-one, supplying the extra hypothesis that globalizes the conclusion.

---

# Hints

> [!note]- Hint 1
> Differentiate each component. $\partial_r(r\cos\theta) = \cos\theta$, $\partial_\theta(r\cos\theta) = -r\sin\theta$, and similarly for the second component. Assemble the $2\times 2$ matrix and take its determinant — it factors very cleanly.

> [!note]- Hint 2
> $\det JF = r(\cos^2\theta + \sin^2\theta) = r$, which is $> 0$ everywhere on $(0,\infty)\times\mathbb{R}$. So $DF$ is invertible at every point, and the inverse function theorem gives a local diffeomorphism near each point.

> [!note]- Hint 3
> Is $F$ injective? Compare $F(r,\theta)$ and $F(r, \theta + 2\pi)$. Cosine and sine are $2\pi$-periodic — so $F$ takes the same value at infinitely many points. The map wraps the strip around the punctured plane infinitely many times.

> [!note]- Hint 4
> Restrict $\theta$ to an open interval of length $2\pi$, say $(-\pi, \pi)$. On $(0,\infty)\times(-\pi,\pi)$ the pair $(r,\theta)$ is recovered uniquely from $(x,y) = F(r,\theta)$: $r = \sqrt{x^2+y^2}$ and $\theta$ is the unique angle in $(-\pi,\pi)$. So $F$ is a global diffeomorphism there — onto the plane minus the non-positive $x$-axis.

---

# Solution

The polar map has a nonvanishing Jacobian determinant everywhere on its domain, so the inverse function theorem makes it a local diffeomorphism at every point. But it is $2\pi$-periodic in the angle, so it is emphatically *not* globally injective — and this is the canonical illustration that the inverse function theorem's conclusion is irreducibly local.

**Step 1: The Jacobian and local invertibility.**

The Jacobian matrix is $JF(r,\theta) = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix}$, with $\det JF = r > 0$. By the inverse function theorem, $F$ is a local $C^\infty$-diffeomorphism near every point of its domain.

> [!note]- Derivation
> Differentiating the two components $F_1 = r\cos\theta$, $F_2 = r\sin\theta$:
> $$JF(r,\theta) = \begin{pmatrix} \partial_r F_1 & \partial_\theta F_1 \\ \partial_r F_2 & \partial_\theta F_2\end{pmatrix} = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix}.$$
> The determinant is
> $$\det JF = (\cos\theta)(r\cos\theta) - (-r\sin\theta)(\sin\theta) = r\cos^2\theta + r\sin^2\theta = r.$$
> On the domain $(0,\infty)\times\mathbb{R}$ we have $r > 0$, so $\det JF \neq 0$ everywhere, meaning $DF(r,\theta)$ is an invertible linear map at every point. The components of $F$ are built from $\cos, \sin$, and multiplication, so $F$ is $C^\infty$. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], for every point $(r_0,\theta_0)$ there is an open neighbourhood on which $F$ restricts to a $C^\infty$-diffeomorphism onto an open subset of $\mathbb{R}^2$.

**Step 2: $F$ is not globally injective.**

For every $(r,\theta)$ and every integer $k$, $F(r, \theta + 2\pi k) = F(r,\theta)$. So $F$ takes each value infinitely often: it is not injective on its full domain.

> [!note]- Derivation
> Since $\cos$ and $\sin$ have period $2\pi$,
> $$F(r, \theta + 2\pi k) = \big(r\cos(\theta + 2\pi k),\ r\sin(\theta + 2\pi k)\big) = (r\cos\theta,\ r\sin\theta) = F(r,\theta)$$
> for every $k \in \mathbb{Z}$. The points $(r, \theta), (r, \theta\pm 2\pi), (r, \theta\pm 4\pi), \dots$ are *distinct* points of the domain $(0,\infty)\times\mathbb{R}$ with the *same* image. So $F$ is far from injective — geometrically, it wraps the infinite strip $(0,\infty)\times\mathbb{R}$ around the punctured plane $\mathbb{R}^2\setminus\{0\}$ infinitely many times, like an endless spiral ramp projecting onto a single annulus.
>
> This does **not** contradict Step 1. The [[Thm - The Inverse Function Theorem|inverse function theorem]] only ever asserts a *local* inverse — an inverse on *some* neighbourhood of each point — and a local inverse near $(r,\theta)$ is a completely different function from a local inverse near $(r, \theta + 2\pi)$, even though both points have the same image. Invertibility of $DF$ at every point is genuinely weaker than global injectivity of $F$; this map is the standard example showing the gap is real.

**Step 3: A maximal domain of global invertibility.**

Restricting the angle to an open interval of length $2\pi$, say $\theta \in (-\pi, \pi)$, makes $F$ a global $C^\infty$-diffeomorphism
$$F : (0,\infty)\times(-\pi,\pi) \xrightarrow{\ \sim\ } \mathbb{R}^2\setminus\{(x,0) : x \leq 0\}.$$

> [!note]- Derivation
> On the restricted domain $\Omega = (0,\infty)\times(-\pi,\pi)$ we verify *global* injectivity directly — this is the separate hypothesis the [[Thm - The Inverse Function Theorem|inverse function theorem]] cannot supply. Suppose $F(r_1,\theta_1) = F(r_2,\theta_2) = (x,y)$. Taking norms, $r_1 = \sqrt{x^2+y^2} = r_2$, since $r > 0$. Then $(\cos\theta_1,\sin\theta_1) = (\cos\theta_2,\sin\theta_2)$, and within a single period $(-\pi,\pi)$ the angle is uniquely determined by its cosine and sine, so $\theta_1 = \theta_2$. Hence $F$ is injective on $\Omega$.
>
> The image is $\mathbb{R}^2$ minus the non-positive $x$-axis: a point $(x,y) \neq (0,0)$ has a unique polar angle in $(-\pi,\pi)$ unless it lies on the negative $x$-axis (angle $\pm\pi$, excluded) or is the origin (excluded since $r > 0$). On this image, the inverse is the explicit smooth map $(x,y)\mapsto\big(\sqrt{x^2+y^2},\ \operatorname{atan2}(y,x)\big)$, where $\operatorname{atan2}$ is smooth off the non-positive $x$-axis. By Step 1 the local inverses are smooth, and a globally injective local diffeomorphism with open image is a global diffeomorphism. The interval $(-\pi,\pi)$ is *maximal* in length: any open $\theta$-interval longer than $2\pi$ contains two points differing by $2\pi$, on which $F$ agrees, destroying injectivity.

> [!note]- Complete formal solution
> $JF(r,\theta) = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}$, $\det JF = r$. On $(0,\infty)\times\mathbb{R}$, $r > 0$, so $DF$ is everywhere invertible and $F \in C^\infty$; by the [[Thm - The Inverse Function Theorem|inverse function theorem]] $F$ is a local $C^\infty$-diffeomorphism at every point.
>
> $F$ is not globally injective: $F(r,\theta+2\pi k) = F(r,\theta)$ for all $k \in \mathbb{Z}$, so each value is attained infinitely often. This does not contradict the local statement — the inverse function theorem asserts only local inverses.
>
> Restricted to $\Omega = (0,\infty)\times(-\pi,\pi)$, $F$ is injective: $F(r_1,\theta_1) = F(r_2,\theta_2)$ forces $r_1 = r_2$ (equal norms) and $\theta_1 = \theta_2$ (unique angle in one period). A globally injective local diffeomorphism with open image is a global diffeomorphism, so $F : \Omega \xrightarrow{\sim} \mathbb{R}^2\setminus\{(x,0):x\leq 0\}$. The length $2\pi$ is maximal. $\blacksquare$

---

# Key Takeaways

**The inverse function theorem is local, and a nonvanishing Jacobian everywhere does not buy global injectivity — the polar map is the canonical witness.** This is the single most important caveat of the theorem, flagged on the topic page as an illegal-but-tempting move. The Jacobian determinant of the polar map is $r$, nonzero throughout the domain, so $F$ is a local diffeomorphism *everywhere*; yet $F$ is $2\pi$-periodic and wraps its domain around the plane infinitely often. Local invertibility at every point is a statement about *infinitesimal* behaviour — the linearization is invertible — and infinitesimal data cannot see the global phenomenon of the domain wrapping back onto itself. Whenever you apply the inverse function theorem, state the conclusion as *local* and never silently upgrade it; if you need a global inverse, that is a separate theorem with a separate hypothesis.

**Globalizing requires a separate, nameable hypothesis — here, restricting to one period.** The local-to-global gap is closed not by the inverse function theorem but by extra information supplied by hand. The general options the topic records are properness, monotonicity, or positive-definiteness of the symmetric part of $DF$ on a convex domain; here the relevant device is *restricting the domain* so that the periodicity causing non-injectivity is broken. On $(0,\infty)\times(-\pi,\pi)$ — exactly one period of the angle — global injectivity is verified directly, by recovering $(r,\theta)$ uniquely from $(x,y)$. The lesson generalizes: when a local diffeomorphism fails to be global, look for the *symmetry* responsible (here, the $\mathbb{Z}$-action $\theta\mapsto\theta+2\pi$) and restrict to a *fundamental domain* of that symmetry.

**The Jacobian determinant of a coordinate change is the local volume-distortion factor, and its vanishing locus is exactly where the coordinates break down.** The determinant $\det JF = r$ is not merely a number to check against zero — it is the factor by which $F$ scales areas near $(r,\theta)$, and it is the very factor that appears in the change-of-variables formula $dx\,dy = r\,dr\,d\theta$. It vanishes precisely at $r = 0$, the origin, which is exactly the point where polar coordinates are singular (the angle is undefined there). Reading the Jacobian determinant tells you *both* where the inverse function theorem applies *and* where the coordinate system genuinely degenerates — these are the same locus, and this coincidence recurs for every coordinate system (spherical coordinates degenerate on the polar axis, where their Jacobian determinant vanishes).

**A globally injective local diffeomorphism is automatically a global diffeomorphism — injectivity is the only missing ingredient.** Once Step 1 establishes that $F$ is a local diffeomorphism at every point (open map, smooth local inverses) and Step 3 establishes global injectivity, no further work is needed: a bijective local diffeomorphism is a global one, because the global inverse agrees locally with the smooth local inverses, hence is itself smooth. This is the precise sense in which "local diffeomorphism + injective = global diffeomorphism", and it tells you exactly what to prove when you want a global statement — establish the local diffeomorphism property by the Jacobian, then establish injectivity by any means available, and the two combine for free.
