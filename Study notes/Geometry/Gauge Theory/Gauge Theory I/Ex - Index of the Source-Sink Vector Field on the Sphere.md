---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Index of a Vector Field at a Zero"
  - "Thm - Poincare-Hopf Theorem"
tags: [geometry, gauge-theory, index, sphere]
---

# Problem Statement

Consider the unit sphere $S^2 \subset \mathbb{R}^3$ with spherical coordinates $(\theta, \phi)$ (colatitude and azimuth).

**(a)** Compute the [[Def - Index of a Vector Field at a Zero|index]] of the vector field $v = \partial/\partial\theta$ at each of its zeros, and verify that the total index equals $\chi(S^2) = 2$.

**(b)** Construct an explicit smooth vector field $w$ on $S^2$ with a *single* zero of index $+2$, located at the north pole. (Hint: use stereographic projection from the north pole.)

**Recall:**

![[Def - Index of a Vector Field at a Zero#The Definition]]

![[Thm - Poincare-Hopf Theorem#Statement]]

---

# Convergent Strategy

**Problem class:** This is a calibration exercise for the [[Def - Index of a Vector Field at a Zero|vector-field index]] in two dimensions, drilling the basic procedure: identify the zeros, choose a small circle around each, count the rotations of $v$ as you traverse the circle, sum the indices. Then verify the [[Thm - Poincare-Hopf Theorem|Poincaré-Hopf theorem]] against the known $\chi(S^2) = 2$. The exercise has two parts that illustrate complementary aspects: part (a) is a *standard* example with multiple zeros, summing to $2$; part (b) is an *extreme* example with a single highly degenerate zero of index $2$.

**Assumption pattern:** The vector field is given explicitly in coordinates. For part (a), the field $\partial/\partial\theta$ — pointing along lines of longitude — degenerates at the poles (where $\theta = 0$ or $\pi$) because the coordinates $(\theta, \phi)$ become singular. For part (b), we construct a field via stereographic projection: a uniform field on $\mathbb{R}^2$ pulls back to a sphere field that is well-behaved except at the projection point (the north pole), where the inverse projection map has a critical point. Both setups produce isolated zeros, hence Poincaré-Hopf applies.

**Theorem routing:** For each zero, compute the angular velocity of $v$ as you walk counterclockwise around a small circle in a local coordinate patch — this is the index. Sum and compare to $\chi(S^2)$. The route is direct: use the [[Def - Index of a Vector Field at a Zero|definition of index]] and the value $\chi(S^2) = 2$ (computable from $H^0(S^2) = H^2(S^2) = \mathbb{R}$, others zero, giving $\chi = 1 - 0 + 1 = 2$). No deep machinery is needed.

**Key decision point:** For part (a), the non-obvious step is to recognize that *both* poles are zeros of $\partial/\partial\theta$ and to determine the index *at each*. Naively the field "points away from the south pole and towards the north pole", suggesting a source and a sink — both of which have index $+1$. The total is then $+2$, matching $\chi(S^2)$. For part (b), the non-obvious step is the stereographic-projection construction and verification that the index at the north pole is $+2$ (a doubled angular winding from the squared denominator).

---

# Legal Operations Used

1. **Choose a local trivialization (chart) and compute in coordinates** (operation 1 of the topic page). For part (a), use spherical $(\theta, \phi)$ on each hemisphere; near each pole introduce *new* coordinates (e.g., $r = \theta$ or $r = \pi - \theta$, and $\phi$ unchanged) to deal with the coordinate singularity. For part (b), use the stereographic chart $(u, v) \in \mathbb{R}^2$ from the north pole.

7. **Compute the Kronecker index by going to a small circle and counting rotations** (operation 7). For each zero, surround it by a small circle and count how many times the field $v$ rotates as you walk once counterclockwise around. The answer is the index, by [[Def - Index of a Vector Field at a Zero|the definition]].

8. **Use trivialization-induced coordinates to make the computation concrete.** Choose coordinates adapted to the zero: at the north pole, use $r = \theta$, so the field $\partial/\partial\theta = \partial/\partial r$ points *radially outward* (a source). At the south pole, use $r = \pi - \theta$, so $\partial/\partial\theta = -\partial/\partial r$ points *radially inward* (a sink). Both are textbook examples of index $+1$.

---

# Hints

> [!note]- Hint 1
> The vector field $v = \partial/\partial\theta$ in spherical coordinates points along lines of longitude — south to north at the south pole, away from the south pole and toward the north pole. Where does this field vanish? At the poles, where the $(\theta, \phi)$ coordinates degenerate.

> [!note]- Hint 2
> Near a pole, set up *flat* coordinates: at the north pole, use $r = \theta$ (the angular distance from the pole) and $\phi$ (the azimuth, unchanged). In these coordinates the metric on the sphere becomes approximately $dr^2 + r^2d\phi^2$ — polar coordinates on a flat plane — so you can apply the planar index formula directly.

> [!note]- Hint 3
> In planar polar coordinates, the field $\partial/\partial r$ is a *source* — a radial outflow — with index $+1$. The field $-\partial/\partial r$ is a *sink* with index $+1$. Identify which is at which pole.

> [!note]- Hint 4 (for part b)
> Stereographic projection from the north pole sends a point $p \in S^2$ (other than $N$) to a point in the plane $\mathbb{R}^2$. The inverse projection $\pi^{-1} : \mathbb{R}^2 \to S^2 \setminus \{N\}$ has differential whose magnitude shrinks like $1/(1 + r^2)^2$ as $|r| \to \infty$, so a uniform field on $\mathbb{R}^2$ pulls back to a field on $S^2$ that vanishes only at $N$. Near $N$, use a chart inverse to the projection from the *south* pole; the field will look like $-z^2$ (in complex coordinates), with winding number $+2$.

---

# Solution

The proof breaks into two parts. Part (a) identifies the two zeros of $v = \partial/\partial\theta$, computes index $+1$ at each, and sums to $\chi(S^2) = 2$. Part (b) constructs the stereographic-projection field, identifies its single zero at the north pole, and computes the index there using complex coordinates to get $+2$. Both parts confirm Poincaré-Hopf.

## Part (a): The field $v = \partial/\partial\theta$

**Step 1: Identify the zeros of $v$.**

The vector field $v = \partial/\partial\theta$ vanishes where the coordinate vector $\partial/\partial\theta$ vanishes — which is *not* a property of the field per se, but of the *interpretation* of $\partial/\partial\theta$ as a tangent vector on $S^2$.

> [!note]- Derivation
> In spherical coordinates, the metric on $S^2$ is $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$. The coordinate vector $\partial/\partial\theta$ is a unit vector everywhere it is defined ($\theta \in (0, \pi)$, since the metric coefficient on $d\theta^2$ is $1$). But at $\theta = 0$ and $\theta = \pi$ (the poles), the coordinate system degenerates: $\phi$ is undefined, and the basis vectors $\partial/\partial\theta, \partial/\partial\phi$ are not well-defined.
>
> Extending the vector field smoothly to the poles requires us to compute the limit. At the north pole ($\theta = 0$), $\partial/\partial\theta$ in spherical coordinates corresponds to "moving along great circles emanating from the north pole" — for any direction of motion (any $\phi$), the velocity at the pole is in *that* direction. But these velocities all have unit magnitude and *different* directions for different $\phi$. So the field cannot be extended continuously to the pole as a non-zero vector; the only continuous extension is $v(N) = 0$.
>
> Same argument at the south pole: $v(S) = 0$.
>
> So $v = \partial/\partial\theta$ extends to a smooth vector field on $S^2$ that vanishes exactly at the two poles.

**Step 2: Index at the north pole.**

> [!note]- Derivation
> Near the north pole, introduce flat coordinates. Let $r = \theta$ (so $r \in [0, \delta)$ for small $\delta$) and keep $\phi$. The metric near $r = 0$ is approximately $ds^2 = dr^2 + r^2 d\phi^2$ (using $\sin\theta \approx \theta = r$). These are exactly polar coordinates on a flat plane near the origin, with the origin corresponding to the north pole.
>
> In these coordinates, $\partial/\partial\theta = \partial/\partial r$ — the *radially outward* unit vector. The field $\partial/\partial r$ on a flat plane has index $+1$ at the origin (source): as you walk counterclockwise around a small circle, $\partial/\partial r$ rotates from pointing right, to up, to left, to down, completing one full counterclockwise rotation.
>
> $$j_v(N) = +1.$$

**Step 3: Index at the south pole.**

> [!note]- Derivation
> Near the south pole, introduce flat coordinates differently. Let $r = \pi - \theta$ (so $r \in [0, \delta)$ for small $\delta$, with $r = 0$ corresponding to $\theta = \pi$, the south pole). Keep $\phi$. The metric near $r = 0$ is again $dr^2 + r^2d\phi^2$.
>
> In these coordinates, $\partial/\partial\theta = -\partial/\partial r$ — the *radially inward* vector. The field $-\partial/\partial r$ has index $+1$ at the origin (sink): as you walk counterclockwise, $-\partial/\partial r$ rotates from pointing left, to down, to right, to up, completing one full counterclockwise rotation.
>
> Note carefully: both source and sink have index $+1$, *not* opposite signs. The index counts *winding* of the field direction as you walk counterclockwise, and both source and sink wind once counterclockwise — they differ in the orientation of the *arrows* (outward vs inward), but the winding direction is the same.
>
> $$j_v(S) = +1.$$

**Step 4: Sum and compare to $\chi(S^2) = 2$.**

> [!note]- Derivation
> $$\sum_p j_v(p) = j_v(N) + j_v(S) = 1 + 1 = 2 = \chi(S^2). \checkmark$$
> Poincaré-Hopf is verified for $v = \partial/\partial\theta$ on $S^2$.

## Part (b): A vector field with a single zero of index $+2$

**Step 5: Stereographic projection setup.**

> [!note]- Derivation
> Let $\sigma : S^2 \setminus \{N\} \to \mathbb{R}^2$ be stereographic projection from the north pole $N$. Explicitly, for a point $p = (x, y, z) \in S^2$ with $z < 1$,
> $$\sigma(p) = \left(\frac{x}{1 - z}, \frac{y}{1 - z}\right).$$
> The inverse $\sigma^{-1} : \mathbb{R}^2 \to S^2 \setminus \{N\}$ is
> $$\sigma^{-1}(u, v) = \left(\frac{2u}{1 + u^2 + v^2}, \frac{2v}{1 + u^2 + v^2}, \frac{u^2 + v^2 - 1}{1 + u^2 + v^2}\right).$$
> Stereographic projection is a conformal map: it preserves angles but not distances.

**Step 6: Pull back a uniform field on $\mathbb{R}^2$.**

> [!note]- Derivation
> Take the uniform vector field $W = \partial/\partial u$ on $\mathbb{R}^2$ — every arrow points to the right with the same length. This field has no zeros on $\mathbb{R}^2$ (it is uniform).
>
> Pull $W$ back to $S^2 \setminus \{N\}$ via $\sigma^{-1}$: $w := (\sigma^{-1})_*W$. Concretely, at $\sigma^{-1}(u, v) \in S^2$, the vector $w$ is the pushforward of $\partial/\partial u$ at $(u, v)$.
>
> This vector $w$ is well-defined on $S^2 \setminus \{N\}$ (the chart) and is nowhere zero on $S^2 \setminus \{N\}$, since $W$ is nowhere zero on $\mathbb{R}^2$.

**Step 7: Extend across the north pole and identify the zero.**

> [!note]- Derivation
> As $(u, v) \to \infty$ in $\mathbb{R}^2$ (equivalently, as we approach $N$ on $S^2$), the magnitude of $w = (\sigma^{-1})_*W$ tends to *zero*. This is because $\sigma^{-1}$ is conformal but not isometric: it stretches distances near $\infty$ in $\mathbb{R}^2$ (where points are close to $N$ on $S^2$) by a factor depending on $1/(1 + u^2 + v^2)$. Pulling back a unit vector through such a stretching map shrinks the result.
>
> Concretely, the conformal factor is $\frac{2}{1 + u^2 + v^2}$, so $|w|_{S^2} = \frac{2}{1 + u^2 + v^2} \cdot |W|_{\mathbb{R}^2} = \frac{2}{1 + u^2 + v^2}$ on $S^2$. This tends to $0$ as $(u, v) \to \infty$, so $w$ extends continuously to $S^2$ with $w(N) = 0$.
>
> The only zero of $w$ on $S^2$ is the north pole.

**Step 8: Compute the index at the north pole.**

> [!note]- Derivation
> To compute the index at $N$, work in a chart *centred at $N$*. Use stereographic projection from the *south* pole: $\tilde\sigma : S^2 \setminus \{S\} \to \mathbb{R}^2$, which sends $N$ to the origin of $\mathbb{R}^2$. The composition $\tilde\sigma \circ \sigma^{-1} : \mathbb{R}^2 \setminus \{0\} \to \mathbb{R}^2 \setminus \{0\}$ is the **inversion** $(u, v) \mapsto (u, v)/(u^2 + v^2)$.
>
> Identifying $\mathbb{R}^2$ with $\mathbb{C}$ via $z = u + iv$, the inversion is $z \mapsto 1/\bar z$. (For our purposes only the *direction* matters, and $1/\bar z$ and $1/z$ have related arguments: $\arg(1/\bar z) = \arg z$.) Under the inversion, the field $W = \partial/\partial u = \partial/\partial z + \partial/\partial\bar z$ pulled back via $\tilde\sigma \circ \sigma^{-1}$ corresponds (up to conformal factor, which does not affect direction) to multiplication by $d(1/z)/dz = -1/z^2$. So in the $z$-coordinate near $N$, the field $w$ behaves like $-1/z^2 \cdot \partial/\partial z = -\bar z^2/|z|^4 \cdot \partial/\partial z$ in real terms — or more cleanly, after the change of coordinates from $\tilde z = 1/z$ (the south-pole stereographic coordinate near $N$), $w \sim -\tilde z^2$ pointing in the $\partial/\partial\tilde z$ direction.
>
> As $\tilde z = re^{i\alpha}$ traces a small circle around $N$ (varying $\alpha$ from $0$ to $2\pi$), the field $-\tilde z^2 = -r^2 e^{2i\alpha}$ traces a circle with angle $\pi + 2\alpha$ — winding **twice** counterclockwise as $\alpha$ goes from $0$ to $2\pi$. Hence the index is $+2$.
>
> $$j_w(N) = +2.$$

**Step 9: Verify Poincaré-Hopf.**

> [!note]- Derivation
> $$\sum_p j_w(p) = j_w(N) = +2 = \chi(S^2). \checkmark$$

> [!note]- Complete formal solution
> **Part (a).** The vector field $v = \partial/\partial\theta$ on $S^2$ extends smoothly with zeros at the two poles (by the limit argument in Step 1). Near the north pole, introduce flat coordinates $(r = \theta, \phi)$; the field becomes $\partial/\partial r$, the radial-outward field, with index $j_v(N) = +1$. Near the south pole, introduce flat coordinates $(r = \pi - \theta, \phi)$; the field becomes $-\partial/\partial r$, the radial-inward field, with index $j_v(S) = +1$. Total: $\sum j_v = 2 = \chi(S^2)$.
>
> **Part (b).** Let $\sigma : S^2 \setminus \{N\} \to \mathbb{R}^2$ be stereographic projection from $N$, with inverse $\sigma^{-1}(u, v) = \frac{1}{1 + u^2 + v^2}(2u, 2v, u^2 + v^2 - 1)$. Pull back the uniform field $W = \partial/\partial u$ on $\mathbb{R}^2$ via $\sigma^{-1}$ to get $w = (\sigma^{-1})_*W$ on $S^2 \setminus \{N\}$. The magnitude $|w|_{S^2} = 2/(1 + u^2 + v^2)$ tends to zero as $(u, v) \to \infty$ (i.e., near $N$), so $w$ extends to all of $S^2$ with $w(N) = 0$ — the only zero.
>
> To compute the index at $N$, use coordinates from the south-pole stereographic projection $\tilde z = 1/z$ near $N$. In the $\tilde z$-coordinate, the field $w$ is proportional to $-\tilde z^2 \partial/\partial\tilde z$ (computed by the chain rule on the inversion). The direction of $-\tilde z^2$ winds twice counterclockwise as $\tilde z$ traces a small circle once counterclockwise, hence $j_w(N) = +2$. Total: $\sum j_w = 2 = \chi(S^2)$. $\blacksquare$

> [!warning] Illegal but tempting: deriving the index from the local "behavior" rather than the rotation count
> It is tempting to call $\partial/\partial r$ "a source, hence index $+1$" and $-\partial/\partial r$ "a sink, hence index $-1$" by direct analogy with planar dynamics. But the index is the **rotation count of $v$**, not a qualitative descriptor of the dynamics. Both sources and sinks have index $+1$; what distinguishes them is the sign of $\det Dv_p$ (positive for sources/sinks, negative for saddles) but *not* the index. The error would compound: the sum $+1 + (-1) = 0$ would contradict $\chi(S^2) = 2$. Always do the direct rotation count.

---

# Key Takeaways

**The index of a vector field is a rotation count, not a qualitative descriptor of dynamics.**

The most common conceptual error is to confuse the *qualitative type* of a zero (source, sink, saddle, centre, dipole, etc.) with its *index*. Sources and sinks both have index $+1$; saddles have index $-1$; centres have index $+1$; dipoles (like the stereographic field's zero at $N$) have index $\pm 2$. The technique to *compute* the index — going to a small circle and counting how many times the field $v$ rotates as you walk counterclockwise — is the *only* technique that works uniformly. When a zero looks like a familiar planar type, you can read off the index from a table; when it looks like none of them, you must compute the rotation count directly. The lesson is to always think *winding*, never *dynamics*, when extracting the index.

**Stereographic projection is the universal tool for constructing fields with prescribed indices on $S^2$.**

Pulling back the field $z^k$ (complex coordinate) on $\mathbb{R}^2$ via inverse stereographic projection gives a field on $S^2$ with a single zero at the projection point of index *$+k$* (for $k > 0$) or $-|k|$ (for $k < 0$). This produces fields with any prescribed integer index. The pattern generalizes: to construct vector fields with prescribed zero structures on $S^n$ (or other manifolds), one can use compositions of projections, blow-ups, and explicit polynomial fields. The construction is the "engineering side" of vector-field theory, complementing the "obstructions side" (Poincaré-Hopf).

**Computational reliability comes from working in flat coordinates near each zero.**

The general formula for the index involves a Brouwer-degree computation in a small sphere around the zero — which is correct but unwieldy. The practical approach is to choose, near each zero, *flat* (or Euclidean) coordinates in which the field becomes a polynomial or simple expression in $(x, y)$ (in 2-d) or $(z, \bar z)$ (using complex coordinates). The index is then easy to read off: $z^k$ has index $k$; $\bar z^k$ has index $-k$; polynomial fields have index given by the lowest-order term's winding. Always invest the effort to set up the right local coordinates before computing.
