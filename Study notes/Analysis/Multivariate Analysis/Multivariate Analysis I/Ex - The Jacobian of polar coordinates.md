---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - The Total Derivative and Differentiability"
  - "Thm - Continuous Partials Imply Differentiability"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $\Phi : (0,\infty) \times \mathbb{R} \to \mathbb{R}^2$ be the **polar-coordinate map**
$$\Phi(r, \theta) = (r\cos\theta,\; r\sin\theta).$$

1. Compute the Jacobian matrix $J\Phi(r,\theta)$ and confirm that $\Phi$ is differentiable everywhere on its domain.
2. Compute the **Jacobian determinant** $\det J\Phi(r,\theta)$.
3. Interpret the determinant geometrically: explain why it equals $r$, the local area-scaling factor of the change to polar coordinates.

**Recall:**

The objects in play are the Jacobian matrix and the criterion for differentiability.

![[Def - Partial Derivatives and the Jacobian Matrix#The Definition]]

For a map $\Phi : U \to \mathbb{R}^m$, the [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian matrix]] $J\Phi$ is the $m \times n$ array whose $(i,j)$ entry is $\partial \Phi_i/\partial x_j$ — row $i$ holds the partials of the $i$-th component, column $j$ holds the partial in the $j$-th variable. When $\Phi$ is differentiable, $J\Phi$ is the matrix of the total derivative $D\Phi$.

![[Thm - Continuous Partials Imply Differentiability#Statement]]

By [[Thm - Continuous Partials Imply Differentiability]], once the partials are computed and seen to be continuous, $\Phi$ is differentiable and $J\Phi$ genuinely is the matrix of $D\Phi$.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-derivative* problem — the most routine class in the topic, where the work is organisational. As the [[Multivariate Analysis I — Differentiation in Several Variables#Problem-Solving Strategy|topic page]] notes, for an explicitly given map the cheap and correct route is: differentiate each component with respect to each variable, observe the partials are continuous, and invoke [[Thm - Continuous Partials Imply Differentiability]].

**Assumption pattern.** $\Phi$ is given by an explicit formula built from $\cos$, $\sin$, and multiplication — all elementary, all smooth. The recognisable feature is "explicit elementary formula", which signals that differentiability is free and the only task is the bookkeeping of the Jacobian.

**Theorem routing.** Part 1: compute the four partials $\partial_r \Phi_i$, $\partial_\theta \Phi_i$ by Analysis I rules, arrange them as a $2\times 2$ matrix; continuity of the entries plus [[Thm - Continuous Partials Imply Differentiability]] gives differentiability. Part 2: compute the $2 \times 2$ determinant. Part 3: read $\det J\Phi$ as the factor by which $\Phi$ scales areas, since the determinant of a linear map is its volume-scaling factor and the derivative is the local linear approximation.

**Key decision point.** There is no genuine obstacle — this is a calibration exercise. The one point worth noticing is *why* the determinant deserves to be called an area-scaling factor: it is because $\Phi$ near a point is well-approximated by its derivative $D\Phi$, a linear map, and the determinant of a linear map is exactly its (signed) volume-scaling factor. The Jacobian determinant is the bridge from this topic to the change-of-variables formula for integrals.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Differentiate componentwise.** Treat the two components $\Phi_1 = r\cos\theta$ and $\Phi_2 = r\sin\theta$ separately; the rows of $J\Phi$ are their derivatives.

2. **Compute partials by Analysis I rules.** Differentiate each component with respect to $r$ (with $\theta$ frozen) and with respect to $\theta$ (with $r$ frozen).

3. **Verify differentiability via continuity of the partials.** The four partials are elementary continuous functions, so [[Thm - Continuous Partials Imply Differentiability]] makes $\Phi$ differentiable and certifies $J\Phi$ as the matrix of $D\Phi$.

---

# Hints

> [!note]- Hint 1
> $\Phi$ has two components. Differentiate each with respect to each of the two variables $r, \theta$. Remember: when differentiating in $r$, treat $\theta$ as a constant; when differentiating in $\theta$, treat $r$ as a constant. You will get four numbers — the four entries of a $2\times2$ matrix.

> [!note]- Hint 2
> The Jacobian is $J\Phi = \begin{pmatrix} \partial_r\Phi_1 & \partial_\theta\Phi_1 \\ \partial_r\Phi_2 & \partial_\theta\Phi_2 \end{pmatrix}$. The determinant of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is $ad - bc$. Use $\cos^2\theta + \sin^2\theta = 1$.

> [!note]- Hint 3
> For Part 3: the derivative $D\Phi$ is the *linear* map best approximating $\Phi$ near a point. The determinant of a linear map is the factor by which it scales areas (in $\mathbb{R}^2$) or volumes (in $\mathbb{R}^n$). So $|\det J\Phi|$ is how much $\Phi$ stretches a tiny patch of $(r,\theta)$-space into $(x,y)$-space. Why should that be $r$? Think of a thin polar rectangle $[r, r+dr]\times[\theta,\theta+d\theta]$ — what is its area in the plane?

---

# Solution

The polar-coordinate map is smooth, so its differentiability is free and the entire exercise is the computation of a $2\times2$ matrix and its determinant. The determinant comes out to $r$, and that single number is the seed of the change-of-variables formula: it is why the area element in polar coordinates is $r\,dr\,d\theta$, not $dr\,d\theta$.

**Step 1: The Jacobian is $J\Phi(r,\theta) = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}$, and $\Phi$ is differentiable everywhere.**

> [!note]- Derivation
> The components are $\Phi_1(r,\theta) = r\cos\theta$ and $\Phi_2(r,\theta) = r\sin\theta$. Differentiating each with respect to each variable, treating the other as constant:
> $$\partial_r \Phi_1 = \cos\theta, \qquad \partial_\theta \Phi_1 = -r\sin\theta,$$
> $$\partial_r \Phi_2 = \sin\theta, \qquad \partial_\theta \Phi_2 = r\cos\theta.$$
> Arranging these as the [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian matrix]] — row $i$ holding the partials of $\Phi_i$, column $1$ the $r$-partials, column $2$ the $\theta$-partials —
> $$J\Phi(r,\theta) = \begin{pmatrix} \partial_r\Phi_1 & \partial_\theta\Phi_1 \\[1mm] \partial_r\Phi_2 & \partial_\theta\Phi_2 \end{pmatrix} = \begin{pmatrix} \cos\theta & -r\sin\theta \\[1mm] \sin\theta & r\cos\theta \end{pmatrix}.$$
> Each of the four entries is an elementary function (a product of $r$ or a constant with $\cos\theta$ or $\sin\theta$), hence continuous on the whole domain $(0,\infty)\times\mathbb{R}$. By [[Thm - Continuous Partials Imply Differentiability]], $\Phi$ is differentiable everywhere on its domain, and $J\Phi$ is genuinely the matrix of the total derivative $D\Phi_{(r,\theta)}$.

**Step 2: The Jacobian determinant is $\det J\Phi(r,\theta) = r$.**

> [!note]- Derivation
> For a $2\times2$ matrix, $\det\begin{pmatrix} a & b \\ c & d\end{pmatrix} = ad - bc$. With $a = \cos\theta$, $b = -r\sin\theta$, $c = \sin\theta$, $d = r\cos\theta$,
> $$\det J\Phi(r,\theta) = (\cos\theta)(r\cos\theta) - (-r\sin\theta)(\sin\theta) = r\cos^2\theta + r\sin^2\theta = r(\cos^2\theta + \sin^2\theta) = r.$$
> So $\det J\Phi(r,\theta) = r$, which is strictly positive on the domain $(0,\infty)\times\mathbb{R}$.

**Step 3: Geometric interpretation — $r$ is the local area-scaling factor.**

> [!note]- Derivation
> Near a point $(r,\theta)$, the map $\Phi$ is approximated to first order by its derivative: $\Phi(r + dr,\, \theta + d\theta) \approx \Phi(r,\theta) + D\Phi_{(r,\theta)}(dr, d\theta)$. The derivative $D\Phi_{(r,\theta)}$ is a *linear* map, and a basic fact of linear algebra is that a linear map $\mathbb{R}^2 \to \mathbb{R}^2$ scales every area by the absolute value of its determinant. Therefore $\Phi$ scales the area of an infinitesimal patch by $|\det J\Phi(r,\theta)| = r$.
>
> Concretely: a small polar "rectangle" $[r, r+dr] \times [\theta, \theta + d\theta]$ in coordinate space has area $dr\,d\theta$. Its image in the plane is a thin curved sliver — an annular wedge — of radial extent $dr$ and arc-length extent $r\,d\theta$ (arc length is radius times angle). To first order this sliver is a rectangle of side lengths $dr$ and $r\,d\theta$, hence of area $r\,dr\,d\theta$. The ratio of image area to source area is $r$ — exactly the Jacobian determinant.
>
> This is the origin of the polar area element $dA = r\,dr\,d\theta$ and the seed of the [[Def - Partial Derivatives and the Jacobian Matrix|change-of-variables formula]]: integrating in polar coordinates requires the weight $r$ precisely because the map stretches area by the factor $r$. The Jacobian determinant being small ($r \to 0$, near the origin) reflects that the polar map crushes a whole circle's worth of $\theta$-values onto a single point — the coordinate change degenerates there, which is why the origin is excluded from the domain.

> [!note]- Complete formal solution
> **Claim.** $\Phi(r,\theta) = (r\cos\theta, r\sin\theta)$ is differentiable on $(0,\infty)\times\mathbb{R}$ with $J\Phi(r,\theta) = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}$ and $\det J\Phi(r,\theta) = r$.
>
> The partials are $\partial_r\Phi_1 = \cos\theta$, $\partial_\theta\Phi_1 = -r\sin\theta$, $\partial_r\Phi_2 = \sin\theta$, $\partial_\theta\Phi_2 = r\cos\theta$. These are continuous on the domain, so by [[Thm - Continuous Partials Imply Differentiability]] $\Phi$ is differentiable and $J\Phi$ is the matrix of $D\Phi$. The determinant is $\cos\theta\cdot r\cos\theta - (-r\sin\theta)\cdot\sin\theta = r(\cos^2\theta+\sin^2\theta) = r$. Since $D\Phi$ is the linear approximation of $\Phi$ and a linear map scales areas by $|\det|$, the map $\Phi$ scales infinitesimal areas by $r$ — equivalently the planar area element is $r\,dr\,d\theta$. $\blacksquare$

---

# Key Takeaways

**For an explicitly given smooth map, differentiability is free and the Jacobian is pure bookkeeping.** This is the routine case, and recognising it saves effort: when a map is written as an explicit formula in elementary functions, do not reach for the $o(|h|)$ definition. Compute the partials by the rules of Analysis I, note that they are continuous (a glance suffices for elementary expressions), and invoke [[Thm - Continuous Partials Imply Differentiability]] — differentiability is settled and the array of partials is certified as the matrix of the derivative. The genuine subtleties of the subject live entirely in *piecewise-defined* functions at their suspect points; an honest formula has none. The polar map is the prototype: four one-line partial derivatives and the work is done.

**The Jacobian determinant is the local volume-scaling factor, and that single fact bridges differentiation to integration.** The determinant $\det J\Phi$ is not an incidental number — it is the factor by which $\Phi$ stretches infinitesimal volumes, because $\Phi$ near a point *is* its derivative $D\Phi$ to first order, and the determinant of a linear map is by definition its volume-scaling factor. This is why the change-of-variables formula for integrals carries the weight $|\det J\Phi|$: substituting coordinates re-measures volume, and the Jacobian determinant is the conversion rate. The polar computation $\det J\Phi = r$ *is* the statement that the area element is $r\,dr\,d\theta$. Whenever a coordinate change appears in an integral, the Jacobian determinant is the thing to compute, and this exercise is the smallest instance of that universal pattern. The same determinant being positive everywhere here also previews the inverse function theorem: a non-vanishing Jacobian determinant is exactly the condition for the coordinate change to be locally invertible.

**A coordinate change degenerates exactly where its Jacobian determinant vanishes, and that is why domains are restricted.** The polar map has $\det J\Phi = r$, which vanishes as $r \to 0$. This is not a blemish — it is the map telling you the truth: at the origin, every value of $\theta$ produces the same point $(0,0)$, so a whole one-dimensional family of coordinate pairs collapses to a single point, and no coordinate change can be invertible there. The vanishing determinant is the analytic signature of this collapse. The lesson generalises: when you set up a coordinate system, the locus where the Jacobian determinant vanishes is where the system breaks down, and it must be excluded from the domain. Reading the determinant tells you not only the scaling factor but also where the construction is legitimate at all.
