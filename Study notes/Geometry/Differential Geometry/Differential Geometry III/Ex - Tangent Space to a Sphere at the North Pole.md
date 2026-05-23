---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - The Tangent Space"
  - "Def - Coordinate Tangent Vectors"
  - "Def - The Tangent Space to a Submanifold"
  - "Def - Velocity of a Curve"
tags: [geometry, differential-geometry]
---

# Problem Statement

Consider the 2-sphere $S^{2} = \{(x, y, z) \in \mathbb{R}^{3} : x^{2} + y^{2} + z^{2} = 1\}$ as a smooth 2-manifold via the **stereographic projection** chart from the south pole, $\varphi_{N} : S^{2} \setminus \{S\} \to \mathbb{R}^{2}$, where $S = (0, 0, -1)$ and
$$\varphi_{N}(x, y, z) = \left(\frac{x}{1 + z},\; \frac{y}{1 + z}\right),$$
with inverse
$$\varphi_{N}^{-1}(u, v) = \left(\frac{2u}{1 + u^{2} + v^{2}},\; \frac{2v}{1 + u^{2} + v^{2}},\; \frac{1 - u^{2} - v^{2}}{1 + u^{2} + v^{2}}\right).$$

Let $N = (0, 0, 1)$ be the north pole.

(a) Compute the coordinate basis $\{\partial/\partial u|_{N}, \partial/\partial v|_{N}\}$ of $T_{N}S^{2}$.

(b) Identify the corresponding vectors in the ambient $\mathbb{R}^{3}$ — that is, compute their images under the differential of the inclusion $\iota : S^{2} \hookrightarrow \mathbb{R}^{3}$.

(c) Verify that these are tangent vectors to the embedded sphere in the sense of [[Def - The Tangent Space to a Submanifold]] — i.e., they are velocities of curves lying on $S^{2}$, and they lie in the plane $\{w \in \mathbb{R}^{3} : w_{3} = 0\}$ (the tangent plane to $S^{2}$ at $N$).

**Recall:**

![[Def - Coordinate Tangent Vectors#The Definition]]

For a submanifold $M \subseteq \mathbb{R}^{N}$ at $p$, the **tangent space** $T_{p}M \subseteq \mathbb{R}^{N}$ as a Euclidean [[Def - Subspace|subspace]] consists of velocity vectors $\gamma'(0)$ of curves $\gamma$ in $M$ with $\gamma(0) = p$; see [[Def - The Tangent Space to a Submanifold]].

The **stereographic projection from $S$** sends a point $(x, y, z) \neq S$ to the point of the equatorial plane $z = 0$ where the line from $S$ through $(x, y, z)$ crosses the plane.

---

# Convergent Strategy

**Problem class:** This is a *concrete tangent-space computation* — work out the basis of $T_{N}S^{2}$ in a specific chart and identify the result geometrically via the embedding into $\mathbb{R}^{3}$. The general routine is: identify the coordinates of $N$ in the chart; differentiate the chart inverse along each coordinate direction; the resulting velocity vector in $\mathbb{R}^{3}$ is the image of the corresponding coordinate basis vector under $d\iota$.

**Assumption pattern:** $S^{2}$ is presented as a regular level set of $f(x, y, z) = x^{2} + y^{2} + z^{2} - 1$ in $\mathbb{R}^{3}$, with smooth structure from the stereographic chart $\varphi_{N}$ at the south pole. The chart is centered such that the north pole has coordinates $(0, 0)$ — convenient for the computation. The chart's inverse $\varphi_{N}^{-1}$ is an explicit formula, allowing direct differentiation.

**Theorem routing:** From [[Ex - Tangent Vectors as Velocities of Coordinate Curves]], $\partial/\partial u|_{N}$ is the velocity of the coordinate curve $\gamma_{u}(t) = \varphi_{N}^{-1}(t, 0)$, and similarly for $\partial/\partial v|_{N}$. Differentiate each curve at $t = 0$ to get a velocity vector in $\mathbb{R}^{3}$. Verify the result lies in the tangent plane $\{w_{3} = 0\}$, which by [[Def - The Tangent Space to a Submanifold]] is exactly $\ker df_{N}$ where $f(x, y, z) = x^{2} + y^{2} + z^{2} - 1$ and $df_{N}(w) = 2 \cdot N \cdot w = 2 w_{3}$. So the tangent plane is $\{w : w_{3} = 0\}$.

**Key decision point:** The non-obvious step is choosing the chart $\varphi_{N}$ from the south pole — *not* from the north pole. This puts $N$ at the origin of the chart, where the inverse formula simplifies. The temptation is to use a chart from $N$ itself, but that excludes $N$ from the chart's domain. The choice to use the *opposite-pole* chart for computations at $N$ is the standard trick.

---

# Legal Operations Used

1. **Express the velocity of a coordinate curve in coordinates** (operations 1 and 9 from the topic page). By [[Ex - Tangent Vectors as Velocities of Coordinate Curves]], $\partial/\partial u|_{N}$ is the velocity at $t = 0$ of the curve $\gamma_{u}(t) = \varphi_{N}^{-1}(t, 0)$. Compute this velocity by differentiating each component of $\varphi_{N}^{-1}(t, 0)$ in $t$ at $t = 0$.

2. **Compute the differential via a curve** (operation 1). The inclusion $\iota : S^{2} \to \mathbb{R}^{3}$ has differential $d\iota_{N}(v) = (\iota \circ \gamma)'(0)$ where $\gamma$ is a curve realizing $v$. Since $\iota$ is the inclusion, $\iota \circ \gamma = \gamma$ as functions $J \to \mathbb{R}^{3}$, so $d\iota_{N}(v) = \gamma'(0) \in \mathbb{R}^{3}$ — the ambient velocity.

3. **Compute the tangent space to a level set as $\ker df_{p}$** (operation 6). For $S^{2} = \{f = 0\}$ with $f(x, y, z) = x^{2} + y^{2} + z^{2} - 1$, $df_{N}(w) = 2(x w_{1} + y w_{2} + z w_{3})|_{N} = 2 w_{3}$ at the north pole. The kernel is $\{w : w_{3} = 0\}$.

---

# Hints

> [!note]- Hint 1
> Find the coordinates of $N$ in the chart $\varphi_{N}$: $\varphi_{N}(N) = (0/(1+1), 0/(1+1)) = (0, 0)$. So $N$ has chart coordinates $(0, 0)$.

> [!note]- Hint 2
> By [[Ex - Tangent Vectors as Velocities of Coordinate Curves]], $\partial/\partial u|_{N}$ is the velocity of the coordinate curve $\gamma_{u}(t) = \varphi_{N}^{-1}(t, 0)$. Compute $\gamma_{u}(t) \in \mathbb{R}^{3}$ explicitly using the formula for $\varphi_{N}^{-1}$, then differentiate at $t = 0$.

> [!note]- Hint 3
> Similarly compute $\partial/\partial v|_{N}$ as the velocity of $\gamma_{v}(t) = \varphi_{N}^{-1}(0, t)$ at $t = 0$. Verify both velocity vectors lie in the plane $\{w : w_{3} = 0\}$ — the tangent plane to $S^{2}$ at $N$.

> [!note]- Hint 4
> For the inclusion's differential $d\iota_{N}$: since the inclusion is the identity in the ambient coordinates, $d\iota_{N}(v)$ is just $v$ viewed as an ambient $\mathbb{R}^{3}$ vector. So the velocities computed in Steps 2–3 *are* the embedded tangent vectors.

---

# Solution

Compute the chart-inverse along each coordinate direction, differentiate at $N$, and recognize the result as the standard basis of the equatorial plane in $\mathbb{R}^{3}$. The tangent plane at $N$ is the horizontal plane $\{w_{3} = 0\}$, and the coordinate basis maps to the two horizontal directions.

**Step 1: $\partial/\partial u|_{N}$ is the velocity at $t = 0$ of $\varphi_{N}^{-1}(t, 0)$ in $\mathbb{R}^{3}$.**

Compute $\varphi_{N}^{-1}(t, 0)$ and differentiate at $t = 0$.

> [!note]- Derivation
> Substituting $u = t, v = 0$ in the formula for $\varphi_{N}^{-1}$:
> $$\varphi_{N}^{-1}(t, 0) = \left(\frac{2t}{1 + t^{2}},\; 0,\; \frac{1 - t^{2}}{1 + t^{2}}\right).$$
> At $t = 0$ this is $(0, 0, 1) = N$, confirming the chart-coordinate identification.
>
> Differentiate each component in $t$:
> - First component: $(2t)/(1 + t^{2})$. Derivative: $(2(1 + t^{2}) - 2t \cdot 2t)/(1 + t^{2})^{2} = 2(1 - t^{2})/(1 + t^{2})^{2}$. At $t = 0$: $2$.
> - Second component: $0$. Derivative: $0$.
> - Third component: $(1 - t^{2})/(1 + t^{2})$. Derivative: $(-2t(1 + t^{2}) - (1 - t^{2}) \cdot 2t)/(1 + t^{2})^{2} = -4t/(1 + t^{2})^{2}$. At $t = 0$: $0$.
>
> So $\gamma_{u}'(0) = (2, 0, 0) \in \mathbb{R}^{3}$.

**Step 2: $\partial/\partial v|_{N}$ is the velocity at $t = 0$ of $\varphi_{N}^{-1}(0, t)$ in $\mathbb{R}^{3}$.**

Compute $\varphi_{N}^{-1}(0, t)$ and differentiate at $t = 0$.

> [!note]- Derivation
> Substituting $u = 0, v = t$:
> $$\varphi_{N}^{-1}(0, t) = \left(0,\; \frac{2t}{1 + t^{2}},\; \frac{1 - t^{2}}{1 + t^{2}}\right).$$
> Differentiate at $t = 0$: $(0, 2, 0) \in \mathbb{R}^{3}$. So $\gamma_{v}'(0) = (0, 2, 0)$.

**Step 3: Identify the embedded tangent vectors.**

The inclusion $\iota : S^{2} \hookrightarrow \mathbb{R}^{3}$ has $d\iota_{N}(v) = v$ as an ambient vector, since $\iota$ is the identity in coordinates.

> [!note]- Derivation
> By the curve formula for the differential (Corollary 3.25 of Lee), $d\iota_{N}(\partial/\partial u|_{N}) = (\iota \circ \gamma_{u})'(0)$. Since $\iota$ is the inclusion, $\iota \circ \gamma_{u} = \gamma_{u}$ as smooth curves $J \to \mathbb{R}^{3}$, so $d\iota_{N}(\partial/\partial u|_{N}) = \gamma_{u}'(0) = (2, 0, 0)$.
>
> Similarly $d\iota_{N}(\partial/\partial v|_{N}) = (0, 2, 0)$.
>
> So the embedded tangent vectors at $N$ corresponding to the coordinate basis are $(2, 0, 0)$ and $(0, 2, 0)$ — both lying in the equatorial plane $z = 0$ of $\mathbb{R}^{3}$.

**Step 4: Verify membership in the level-set tangent space.**

Compute $\ker df_{N}$ for $f(x, y, z) = x^{2} + y^{2} + z^{2} - 1$ and check the two vectors are in the kernel.

> [!note]- Derivation
> $df_{(x, y, z)}(w) = 2(xw_{1} + yw_{2} + zw_{3})$, so $df_{N}(w) = 2(0 \cdot w_{1} + 0 \cdot w_{2} + 1 \cdot w_{3}) = 2 w_{3}$. The kernel is $\{(w_{1}, w_{2}, w_{3}) : w_{3} = 0\}$ — the horizontal plane at $N$.
>
> The vectors $(2, 0, 0)$ and $(0, 2, 0)$ both have $w_{3} = 0$, so they lie in $\ker df_{N}$. They are linearly independent, hence span the 2-dimensional kernel. By [[Def - The Tangent Space to a Submanifold]], $T_{N}S^{2} = \ker df_{N}$, the horizontal plane at $N$, and the embedded coordinate basis spans this plane.

> [!note]- Complete formal solution
> The stereographic projection from the south pole takes $N = (0, 0, 1)$ to $\varphi_{N}(N) = (0, 0) \in \mathbb{R}^{2}$, so $N$ has chart coordinates $(0, 0)$.
>
> *Part (a) — Coordinate basis at $N$.* By [[Ex - Tangent Vectors as Velocities of Coordinate Curves]], $\partial/\partial u|_{N}$ is the velocity at $t = 0$ of $\gamma_{u}(t) = \varphi_{N}^{-1}(t, 0)$, and $\partial/\partial v|_{N}$ is the velocity at $t = 0$ of $\gamma_{v}(t) = \varphi_{N}^{-1}(0, t)$. These are formal tangent vectors in $T_{N}S^{2}$.
>
> *Part (b) — Embedded tangent vectors.* Compute the curves' Euclidean components:
> $$\gamma_{u}(t) = \left(\frac{2t}{1+t^{2}}, 0, \frac{1-t^{2}}{1+t^{2}}\right), \quad \gamma_{v}(t) = \left(0, \frac{2t}{1+t^{2}}, \frac{1-t^{2}}{1+t^{2}}\right).$$
> Differentiating at $t = 0$:
> $$\gamma_{u}'(0) = (2, 0, 0), \quad \gamma_{v}'(0) = (0, 2, 0).$$
> These are the images of the coordinate basis under the differential of the inclusion $\iota : S^{2} \hookrightarrow \mathbb{R}^{3}$.
>
> *Part (c) — Verification.* The defining function $f(x, y, z) = x^{2} + y^{2} + z^{2} - 1$ has $df_{N}(w) = 2w_{3}$, so $\ker df_{N} = \{(w_{1}, w_{2}, w_{3}) : w_{3} = 0\}$ — the horizontal plane. Both $(2, 0, 0)$ and $(0, 2, 0)$ lie in this plane, so they are in the tangent space to the embedded sphere $S^{2} \subseteq \mathbb{R}^{3}$ at $N$, with $T_{N}S^{2} = \{w : w_{3} = 0\}$. The embedded coordinate basis spans this 2-dimensional plane.
>
> Geometrically, the horizontal plane at $N$ is the natural tangent plane to the sphere there — it is what you would draw as the "tangent plane to a sphere at its top point". $\qquad\blacksquare$

---

# Key Takeaways

**Stereographic projection from the opposite pole is the canonical chart for computations at a pole.** This is a recurring trick in differential geometry: to compute at a point $p$, use a chart that has $p$ in its domain and ideally puts $p$ at the origin. For the sphere, stereographic projection from the antipodal point is the natural choice, because the antipodal point is missing from the domain — exactly what you need. The chart $\varphi_{N}$ projects from the south pole, putting $N$ at the chart origin, where the inverse $\varphi_{N}^{-1}$ simplifies to $(0, 0, 1)$ plus low-order corrections. The "use a chart that excludes the target point and places it at the chart origin" trick recurs throughout differential geometry — for projective space, Lie [[Def - Group|groups]], and more.

**The differential of an inclusion just reads off Euclidean velocity.** For a submanifold $M \subseteq \mathbb{R}^{N}$, the inclusion $\iota : M \to \mathbb{R}^{N}$ has differential $d\iota_{p}(v) = \gamma'(0) \in \mathbb{R}^{N}$ for any curve $\gamma$ on $M$ realizing $v$. So the embedded tangent vectors are *just* the Euclidean velocities of curves on $M$. This is the cleanest way to identify abstract tangent vectors with their concrete Euclidean realizations — and it is exactly the bridge between [[Def - The Tangent Space|abstract TₚM]] and [[Def - The Tangent Space to a Submanifold|embedded TₚM ⊂ ℝᴺ]]. Whenever you have a manifold sitting in Euclidean space, this is the route to make the abstract tangent space concrete.

**The tangent space to a level set is the kernel of the differential of the defining function.** For $M = \{f = c\}$ regular, $T_{p}M = \ker df_{p}$. This converts tangent-space computations on level sets into kernel computations on linear maps — usually the fastest route. For the sphere at $N$, $df_{N}(w) = 2w_{3}$, so $\ker df_{N} = \{w_{3} = 0\}$ in one line. This is the *level-set picture* of the tangent space, complementary to the *chart picture* (with the coordinate basis). The two pictures agree (by the equivalence theorem), and one chooses whichever is more convenient for the problem.
