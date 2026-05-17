---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Method of Lagrange Multipliers"
  - "Thm - First-Order Optimality Condition"
  - "Def - Directional Derivative and the Gradient"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider the function $f(x,y) = 4y - 3x$ and the compact set
$$K = \{(x,y) \in [-1,1]^2 : F(x,y) = 0\}, \qquad F(x,y) = y^3 - x^2.$$
Find the global maximum and the global minimum of $f$ on $K$.

**Recall:**

The objects in play are the constraint set, the method of Lagrange multipliers, and the notion of a non-regular constraint point.

![[Thm - The Method of Lagrange Multipliers#Statement]]

By the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]], at a local extremum of $f$ restricted to the constraint set $\{F = 0\}$, the gradients $\nabla f$ and $\nabla F$ are linearly dependent. At a **regular** point — one where $\nabla F \neq 0$ — this means $\nabla f = \lambda\nabla F$ for some multiplier $\lambda$. At a **non-regular** point — where $\nabla F = 0$ — the method gives no information about $f$, and such points must be checked by hand. The constraint curve here is contained in a *closed square*, so its boundary points (where the curve meets $\partial[-1,1]^2$) must also be examined separately. Since $K$ is compact and $f$ continuous, the Weierstrass theorem guarantees the global extrema exist and lie among these finitely many candidates.

---

# Convergent Strategy

**Problem class.** This is a *constrained optimization over a compact set*. As the [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic's problem-solving strategy]] records, the candidate list for such a problem has three parts that must *all* be assembled: the Lagrange-multiplier solutions, the points where the constraint curve meets the boundary of the box, and the non-regular points of the constraint set.

**Assumption pattern.** The constraint $F(x,y) = y^3 - x^2 = 0$ is a *cusped curve* — it has a singular point. The constraint gradient $\nabla F = (-2x, 3y^2)$ vanishes exactly at the origin, so $(0,0)$ is a non-regular point, and this is the feature the problem is built around. The objective $f = 4y - 3x$ is linear, so $\nabla f = (-3, 4)$ is constant and nonzero everywhere.

**Theorem routing.** On the regular part of the curve, [[Thm - The Method of Lagrange Multipliers|Lagrange's theorem]] gives $\nabla f = \lambda\nabla F$, i.e. $(-3, 4) = \lambda(-2x, 3y^2)$, a system to solve together with $F = 0$. The boundary points are found by intersecting the curve with $\partial[-1,1]^2$. The non-regular point $(0,0)$ is examined directly.

**Key decision point.** The non-obvious move — and the entire point of the exercise — is realizing that the Lagrange equations do *not* see the origin. Because $\nabla F(0,0) = 0$, there is no $\lambda$ with $\nabla f(0,0) = \lambda\nabla F(0,0)$ (the right side is $0$, the left side is $(-3,4) \neq 0$). The origin is invisible to the method, yet it is a genuine candidate and, as it turns out, the global minimum. Forgetting it gives the wrong answer.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Set up the Lagrange equations on a constraint set.** Solve $\nabla f = \lambda\nabla F$ together with $F = 0$ for the regular extrema.

2. **Check the non-regular points of the constraint set by hand.** Identify where $\nabla F = 0$ — here the origin — and evaluate $f$ there directly, since Lagrange's theorem cannot see it.

3. **Examine the boundary of the search region.** The constraint curve sits in a closed box; its intersection with the box boundary supplies further candidates.

4. **Compare $f$ over the finite candidate list.** Compactness guarantees the global extrema are among the assembled candidates; evaluate $f$ on each and read off the largest and smallest.

---

# Hints

> [!note]- Hint 1
> The candidate list has three parts. First, the regular Lagrange candidates: solve $\nabla f = \lambda\nabla F$ with $F = 0$. Second, the boundary candidates: where does the curve $y^3 = x^2$ meet the edges of $[-1,1]^2$? Third — easy to forget — the non-regular points: where is $\nabla F = 0$?

> [!note]- Hint 2
> The Lagrange system is $(-3, 4) = \lambda(-2x, 3y^2)$. From the first component $\lambda = 3/(2x)$ (so $x \neq 0$); from the second $\lambda = 4/(3y^2)$ (so $y \neq 0$). Equate them, then use $y^3 = x^2$ to finish.

> [!note]- Hint 3
> Equating the two expressions for $\lambda$ gives $3\cdot 3y^2 = 4\cdot 2x$, i.e. $x = \tfrac{9}{8}y^2$. Combined with $x^2 = y^3$: substitute to get $\tfrac{81}{64}y^4 = y^3$, so $y^3(\tfrac{81}{64}y - 1) = 0$. Since $y \neq 0$, $y = 64/81$.

> [!note]- Hint 4
> The boundary of $[-1,1]^2$ meets $y^3 = x^2$ where $x = \pm 1, y = 1$ (since $y^3 = 1$): the points $(1,1)$ and $(-1,1)$. The non-regular point is the origin, where $\nabla F = (-2x, 3y^2) = 0$. Evaluate $f = 4y - 3x$ at the Lagrange point, at $(1,1)$, at $(-1,1)$, and at $(0,0)$, then compare.

---

# Solution

The constraint curve $y^3 = x^2$ is a cusped curve, and the search for extrema of the linear function $f = 4y - 3x$ on the compact piece $K$ has three sources of candidates: the regular interior of the curve (Lagrange), the two points where the curve hits the box boundary, and — crucially — the cusp at the origin, which the Lagrange method cannot detect.

**Step 1: The regular Lagrange candidate.**

On the part of the curve where $\nabla F \neq 0$, the Lagrange equations $\nabla f = \lambda\nabla F$ together with $F = 0$ have a single solution: the point $\left(\tfrac{8^3}{9^3}, \tfrac{8^2}{9^2}\right) = \left(\tfrac{512}{729}, \tfrac{64}{81}\right)$.

> [!note]- Derivation
> The gradients are $\nabla f = (-3, 4)$ and $\nabla F = (-2x, 3y^2)$. The Lagrange condition $\nabla f = \lambda\nabla F$ is the pair
> $$-3 = -2\lambda x, \qquad 4 = 3\lambda y^2.$$
> The first forces $x \neq 0$ and $\lambda = \tfrac{3}{2x}$; the second forces $y \neq 0$ and $\lambda = \tfrac{4}{3y^2}$. Equating:
> $$\frac{3}{2x} = \frac{4}{3y^2} \quad\Longrightarrow\quad 9y^2 = 8x \quad\Longrightarrow\quad x = \tfrac{9}{8}y^2.$$
> Now impose the constraint $F = 0$, i.e. $x^2 = y^3$:
> $$\Big(\tfrac{9}{8}y^2\Big)^2 = y^3 \quad\Longrightarrow\quad \tfrac{81}{64}y^4 = y^3 \quad\Longrightarrow\quad y^3\Big(\tfrac{81}{64}y - 1\Big) = 0.$$
> Since $y \neq 0$, we get $y = \tfrac{64}{81}$, and then $x = \tfrac{9}{8}y^2 = \tfrac{9}{8}\cdot\tfrac{64^2}{81^2} = \tfrac{512}{729}$. So the unique regular Lagrange candidate is $\left(\tfrac{512}{729}, \tfrac{64}{81}\right)$, and there
> $$f = 4\cdot\tfrac{64}{81} - 3\cdot\tfrac{512}{729} = \tfrac{256}{81} - \tfrac{1536}{729} = \tfrac{2304}{729} - \tfrac{1536}{729} = \tfrac{768}{729} \approx 1.053.$$

**Step 2: The boundary candidates.**

The constraint curve $y^3 = x^2$ meets the boundary of the box $[-1,1]^2$ at $(1,1)$ and $(-1,1)$, with $f(1,1) = 1$ and $f(-1,1) = 7$.

> [!note]- Derivation
> A point of $K$ on the boundary $\partial[-1,1]^2$ has $|x| = 1$ or $|y| = 1$. On the curve $y^3 = x^2 \geq 0$, so $y \geq 0$, and $y \leq 1$ forces $y^3 = x^2 \leq 1$. If $|x| = 1$ then $y^3 = 1$, so $y = 1$: the points $(1,1)$ and $(-1,1)$, both in the box. If $|y| = 1$ then $y = 1$ (since $y \geq 0$) and $x^2 = 1$ — the same two points. So the boundary contributes exactly $(1,1)$ and $(-1,1)$:
> $$f(1,1) = 4 - 3 = 1, \qquad f(-1,1) = 4 + 3 = 7.$$

**Step 3: The non-regular point — the cusp at the origin.**

The constraint gradient $\nabla F = (-2x, 3y^2)$ vanishes only at $(0,0)$, which lies on $K$. This point is *invisible to the Lagrange equations* and must be added by hand: $f(0,0) = 0$.

> [!note]- Derivation
> $\nabla F(x,y) = (-2x, 3y^2) = (0,0)$ iff $x = 0$ and $y = 0$, and $(0,0)$ satisfies $F = 0$, so it lies in $K$. At this point the Lagrange condition $\nabla f = \lambda\nabla F$ would read $(-3, 4) = \lambda(0,0) = (0,0)$, which has *no* solution $\lambda$ — the origin is a non-regular constraint point and the [[Thm - The Method of Lagrange Multipliers|method]] simply does not constrain $f$ there. (In the general form of Lagrange's theorem this is the case $\lambda_0 = 0$.) Nonetheless the origin is a genuine point of the compact set $K$ and therefore a candidate for a global extremum. Directly: $f(0,0) = 4\cdot 0 - 3\cdot 0 = 0$.

**Step 4: Compare the candidate list.**

The complete candidate list is $\left(\tfrac{512}{729}, \tfrac{64}{81}\right)$, $(1,1)$, $(-1,1)$, $(0,0)$, with $f$-values $\tfrac{768}{729} \approx 1.053$, $1$, $7$, $0$. Hence the global maximum of $f$ on $K$ is $\mathbf{7}$, attained at $(-1,1)$, and the global minimum is $\mathbf{0}$, attained at the cusp $(0,0)$.

> [!note]- Derivation
> Since $K$ is closed and bounded — a closed subset of the compact square — it is compact, and $f$ is continuous, so by the Weierstrass theorem $f$ attains a global maximum and a global minimum on $K$. Every global extremum is in particular a local extremum of $f|_K$; by the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]] a local extremum is either a regular point satisfying the Lagrange equations, a boundary point of the search region, or a non-regular constraint point. Steps 1–3 produced the complete list of all three kinds:
> $$f\Big(\tfrac{512}{729},\tfrac{64}{81}\Big) \approx 1.053, \quad f(1,1) = 1, \quad f(-1,1) = 7, \quad f(0,0) = 0.$$
> The largest value is $7$ at $(-1,1)$; the smallest is $0$ at $(0,0)$. $\blacksquare$

> [!note]- Complete formal solution
> $K = \{y^3 = x^2\} \cap [-1,1]^2$ is compact and $f(x,y) = 4y - 3x$ is continuous, so global extrema exist (Weierstrass). Candidates come in three kinds.
>
> *Regular Lagrange candidates.* $\nabla f = (-3,4)$, $\nabla F = (-2x, 3y^2)$. Solving $\nabla f = \lambda\nabla F$ with $F = 0$: $\lambda = 3/(2x) = 4/(3y^2)$ gives $x = \tfrac98 y^2$, and $x^2 = y^3$ then gives $y = \tfrac{64}{81}$, $x = \tfrac{512}{729}$. There $f = \tfrac{768}{729} \approx 1.053$.
>
> *Boundary candidates.* The curve meets $\partial[-1,1]^2$ at $(1,1)$ and $(-1,1)$; $f(1,1) = 1$, $f(-1,1) = 7$.
>
> *Non-regular candidate.* $\nabla F = 0$ only at $(0,0) \in K$; Lagrange's clean form fails there, so check directly: $f(0,0) = 0$.
>
> Comparing $\{1.053, 1, 7, 0\}$: the global maximum is $7$ at $(-1,1)$, the global minimum is $0$ at the cusp $(0,0)$. $\blacksquare$

---

# Key Takeaways

**A constrained optimization over a compact set is solved by assembling a finite candidate list of three kinds, and the list must be complete.** Compactness, via Weierstrass, guarantees the global extrema *exist* and therefore *are* among the candidates — but only if the candidate list is genuinely exhaustive. The three sources are: the regular Lagrange solutions, the boundary points where the constraint set meets the edge of the search region, and the non-regular points of the constraint set. The strategy is valid precisely because these three exhaust the possibilities of [[Thm - The Method of Lagrange Multipliers|Lagrange's theorem]], and it *fails* the moment one of the three is forgotten. The discipline is to write down all three categories explicitly before computing anything.

**Lagrange multipliers fail silently at non-regular constraint points, and the failure mode is geometric.** The Lagrange equations $\nabla f = \lambda\nabla F$ presuppose $\nabla F \neq 0$ — they can only express "$\nabla f$ parallel to $\nabla F$" when $\nabla F$ is a genuine direction. At the cusp $(0,0)$ of $y^3 = x^2$ the constraint gradient *vanishes*, the curve has no well-defined tangent line, and "$\nabla f$ normal to the constraint" is meaningless. The method does not warn you; it simply produces no equation for that point, and an unwary solver finds the maximum and never notices the minimum sitting at the cusp. The trigger to watch for is any constraint defined by a function whose gradient can vanish — polynomials with cusps, corners, or self-intersections — and the permanent rule is: locate the zeros of $\nabla F$ on the constraint set and add them to the candidate list by hand. This exercise is calibrated so that the global *minimum* lives exactly at the invisible point.

**The objective being linear makes the geometry vivid: extrema occur where a level line is tangent to the curve, or at a corner.** With $f = 4y - 3x$ the level sets are parallel straight lines, and maximising $f$ over $K$ means pushing the line $4y - 3x = c$ as far as possible while still touching $K$. On the smooth part of the curve the extreme line is *tangent* — that tangency is exactly the Lagrange condition $\nabla f \parallel \nabla F$. But the extreme contact can also happen at a *corner* of $K$ (a box-boundary point) or at the *cusp*, where there is no tangent line to be parallel to and the line simply touches the singular point. This picture — extremum = tangency, or extremum = corner contact — is the geometric content of constrained optimization and the reason the candidate list has the shape it does.

**When the constraint set sits inside a bounded region, the region's boundary is a third constraint surface.** Here $K$ is the intersection of a curve with a closed square, and the square's edges contribute candidates of their own — the points $(1,1)$ and $(-1,1)$, one of which is the global maximum. A search over a curve-inside-a-box is really a search over a one-dimensional set with endpoints, and endpoints of a one-dimensional search are exactly where the curve exits the box. Whenever a problem confines the constraint set to a bounded region, treat the region's boundary as an additional place where extrema can hide, on the same footing as the Lagrange points and the non-regular points.
