---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Kelvin-Stokes Theorem"
  - "Def - The Exterior Derivative"
  - "Def - Pullback of a Differential Form"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

1. Compute the circulation $\oint_\gamma F\cdot T\,ds$ of the vector field $F(x,y,z) = (-y,\ x,\ z)$ around the unit circle $\gamma(t) = (\cos t,\ \sin t,\ 0)$ in the $xy$-plane, by replacing it with the flux of $\operatorname{curl} F$ through the flat disk the circle bounds.
2. Let $\gamma$ be the boundary of the triangle with vertices $(1,0,0)$, $(0,1,0)$, $(0,0,1)$, traversed counterclockwise as seen from the positive octant, and let $F(x,y,z) = (z,\ x,\ y)$. Compute $\oint_\gamma F\cdot T\,ds$ using Kelvin-Stokes, spanning $\gamma$ with the flat triangular surface.
3. For the field $F$ of part 1, recompute the circulation around the unit circle by spanning it instead with the upper unit hemisphere, and confirm the answer is unchanged — illustrating surface-independence of the flux of a curl.

**Recall:**

![[Thm - The Kelvin-Stokes Theorem#Statement]]

[[Thm - The Kelvin-Stokes Theorem|The Kelvin-Stokes theorem]]: for a compact oriented surface $M \subseteq \mathbb{R}^3$ with boundary $\partial M$ and a $C^1$ vector field $F$,
$$\iint_M(\operatorname{curl} F)\cdot N\;dS = \oint_{\partial M} F\cdot T\;ds.$$
The **curl** is $\operatorname{curl} F = (\partial_y F_3 - \partial_z F_2,\ \partial_z F_1 - \partial_x F_3,\ \partial_x F_2 - \partial_y F_1)$. The spanning surface $M$ is *not fixed by the problem* — any surface with boundary $\gamma$ gives the same flux.

---

# Convergent Strategy

**Problem class.** A *circulation computation* problem: evaluate a line integral around a closed space curve by trading it, via Kelvin-Stokes, for a flux of the curl. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy records the trigger — *complicated boundary curve, simple curl $\Rightarrow$ integrate the curl over a spanning surface*.

**Assumption pattern.** Each problem gives a closed space curve and a field. The recognizable feature: the direct line integral is a sum over arcs or has an awkward integrand, but the *curl* of the field is simple (often constant), and the curve obviously bounds a flat surface.

**Theorem routing.** Compute $\operatorname{curl} F$ — three partials. Choose a surface $M$ with $\partial M = \gamma$ (a flat disk, a flat triangle — the simplest available). Integrate $(\operatorname{curl} F)\cdot N$ over $M$. Part 3 replaces the flat disk by a hemisphere to verify surface-independence.

**Key decision point.** The crux is *choosing the spanning surface*. Kelvin-Stokes does not hand you a surface — it lets you pick *any* surface bounded by $\gamma$, and they all give the same flux. The skilled move is to span the curve with the flattest, simplest surface available (a planar disk, a planar polygon), because then the normal $N$ is constant and the flux integral is trivial. Part 3 confirms this freedom by getting the same answer from a curved hemisphere.

---

# Legal Operations Used

1. **Apply the general Stokes theorem (here the Kelvin-Stokes theorem)** — converting each circulation to a flux of the curl.
2. **Compute $d$ of a form / a curl** — computing $\operatorname{curl} F$ from the field.
3. **Choose the easier side of Stokes** — and, specifically, choose the easiest *spanning surface*, exploiting surface-independence.
4. **Pull a form back along a parametrization** — part 3, integrating the curl $2$-form over the hemisphere.

---

# Hints

> [!note]- Hint 1
> For part 1, compute $\operatorname{curl} F$ for $F = (-y, x, z)$ — it is a constant vector. The unit circle in the $xy$-plane bounds the flat unit disk; its normal $N$ (for the counterclockwise orientation) is constant. The flux is then $(\operatorname{curl} F\cdot N)$ times the disk's area.

> [!note]- Hint 2
> For part 2, compute $\operatorname{curl} F$ for $F = (z, x, y)$ — again constant. Span the triangle with its flat interior; the normal to the plane $x+y+z=1$ is the constant unit vector $(1,1,1)/\sqrt3$. The flux is $(\operatorname{curl} F\cdot N)$ times the triangle's area.

> [!note]- Hint 3
> For part 2, the triangle with vertices $(1,0,0), (0,1,0), (0,0,1)$ lies in the plane $x+y+z=1$. Its area: it is an equilateral triangle with side length $\sqrt2$, so area $= \tfrac{\sqrt3}{4}(\sqrt2)^2 = \tfrac{\sqrt3}{2}$.

> [!note]- Hint 4
> For part 3, the curl from part 1 is the constant vector $(0,0,2)$. Integrating its flux through the hemisphere: $(\operatorname{curl} F)\cdot N$ is not constant on the hemisphere, but the flux of a *constant* vector through any surface with a given boundary equals its flux through any other — because the constant field is a curl and surface-independence applies. Alternatively, integrate directly.

---

# Solution

Each circulation is replaced by the flux of $\operatorname{curl} F$ through a spanning surface. The curls here are constant vectors, so the flux is just (curl $\cdot$ normal) times area — provided the surface is flat.

**Step 1: circulation of $F = (-y, x, z)$ around the unit circle.**

$$\oint_\gamma F\cdot T\,ds = \iint_{\text{disk}}(\operatorname{curl} F)\cdot N\,dS = 2\cdot\operatorname{area}(\text{disk}) = 2\pi.$$

> [!note]- Derivation
> Compute the curl of $F = (-y, x, z)$:
> $$\operatorname{curl} F = (\partial_y F_3 - \partial_z F_2,\ \partial_z F_1 - \partial_x F_3,\ \partial_x F_2 - \partial_y F_1) = (0 - 0,\ 0 - 0,\ 1 - (-1)) = (0, 0, 2).$$
> The curl is the constant vector $(0, 0, 2)$.
>
> The unit circle $\gamma$ lies in the $xy$-plane; it bounds the flat unit disk $D = \{x^2+y^2 \le 1,\ z = 0\}$. With $\gamma$ traversed counterclockwise (as seen from above), the induced orientation gives $D$ the upward normal $N = (0, 0, 1)$.
>
> By Kelvin-Stokes,
> $$\oint_\gamma F\cdot T\,ds = \iint_D(\operatorname{curl} F)\cdot N\,dS = \iint_D (0,0,2)\cdot(0,0,1)\,dS = \iint_D 2\,dS = 2\cdot\operatorname{area}(D) = 2\pi.$$
> The circulation is $2\pi$. (The direct line integral confirms: $F\cdot T$ along $\gamma(t) = (\cos t, \sin t, 0)$ is $(-\sin t, \cos t, 0)\cdot(-\sin t, \cos t, 0) = \sin^2 t + \cos^2 t = 1$, so $\oint = \int_0^{2\pi} 1\,dt = 2\pi$. Kelvin-Stokes gives the same with less work.)

**Step 2: circulation of $F = (z, x, y)$ around the triangle.**

$$\oint_\gamma F\cdot T\,ds = \iint_{\text{triangle}}(\operatorname{curl} F)\cdot N\,dS = \sqrt3\cdot\frac{\sqrt3}{2} = \frac{3}{2}.$$

> [!note]- Derivation
> Compute the curl of $F = (z, x, y)$:
> $$\operatorname{curl} F = (\partial_y F_3 - \partial_z F_2,\ \partial_z F_1 - \partial_x F_3,\ \partial_x F_2 - \partial_y F_1) = (1 - 0,\ 1 - 0,\ 1 - 0) = (1, 1, 1).$$
> The curl is the constant vector $(1, 1, 1)$.
>
> The triangle with vertices $(1,0,0), (0,1,0), (0,0,1)$ lies in the plane $x + y + z = 1$. Span $\gamma$ with the flat triangular region $M$ in that plane. The upward-pointing unit normal to the plane (consistent with the counterclockwise orientation seen from the positive octant) is
> $$N = \frac{(1, 1, 1)}{\sqrt3}.$$
> Then $(\operatorname{curl} F)\cdot N = (1,1,1)\cdot(1,1,1)/\sqrt3 = 3/\sqrt3 = \sqrt3$, a constant.
>
> The area of the triangle: its three edges connect points at mutual distance $\sqrt2$ (e.g. $|(1,0,0)-(0,1,0)| = \sqrt2$), so it is equilateral with side $\sqrt2$, and an equilateral triangle of side $s$ has area $\tfrac{\sqrt3}{4}s^2 = \tfrac{\sqrt3}{4}\cdot 2 = \tfrac{\sqrt3}{2}$.
>
> By Kelvin-Stokes,
> $$\oint_\gamma F\cdot T\,ds = \iint_M(\operatorname{curl} F)\cdot N\,dS = \sqrt3\cdot\operatorname{area}(M) = \sqrt3\cdot\frac{\sqrt3}{2} = \frac{3}{2}.$$

**Step 3: surface-independence — span the unit circle with a hemisphere.**

$$\iint_{\text{hemisphere}}(\operatorname{curl} F)\cdot N\,dS = 2\pi = \oint_\gamma F\cdot T\,ds.$$

> [!note]- Derivation
> The field is again $F = (-y, x, z)$ with constant curl $\operatorname{curl} F = (0, 0, 2)$. Now span the unit circle $\gamma$ with the upper unit hemisphere $H = \{x^2+y^2+z^2 = 1,\ z \ge 0\}$, oriented with the outward normal, whose boundary is the same circle $\gamma$ with the same induced orientation.
>
> The flux of the constant vector $C = (0,0,2)$ through $H$ is $\iint_H C\cdot N\,dS$. There are two clean ways to see it equals $2\pi$.
>
> *By surface-independence.* Both the flat disk $D$ and the hemisphere $H$ have the same boundary $\gamma$ with the same orientation. Since $\operatorname{curl} F$ is a curl, the Kelvin-Stokes theorem gives $\iint_H(\operatorname{curl} F)\cdot N\,dS = \oint_\gamma F\cdot T\,ds = \iint_D(\operatorname{curl} F)\cdot N\,dS$. The flux of the curl through $H$ *must* equal the flux through $D$ — both equal the circulation. So the answer is $2\pi$, with no further computation.
>
> *By direct flux of a constant field.* The flux of a constant vector $C$ through any surface depends only on the surface's boundary, because $C\cdot N$ integrated over a surface equals $C\cdot(\text{vector area})$, and the vector area $\iint_M N\,dS$ depends only on $\partial M$. Concretely, the difference of fluxes through $H$ and $D$ is the flux through the *closed* surface $H \cup (-D)$ (hemisphere capped by the disk), which by the divergence theorem is $\int\operatorname{div} C\,dV = 0$ since $\operatorname{div}(0,0,2) = 0$. Hence flux through $H$ = flux through $D$ = $2\pi$.
>
> Either way, $\iint_H(\operatorname{curl} F)\cdot N\,dS = 2\pi$, identical to Step 1. The flux of the curl is independent of which surface spans the circle.

> [!note]- Complete formal solution
> **Part 1.** $\operatorname{curl}(-y,x,z) = (0,0,2)$. The unit circle bounds the flat disk $D$ with upward normal $N = (0,0,1)$. By Kelvin-Stokes, $\oint_\gamma F\cdot T\,ds = \iint_D(0,0,2)\cdot(0,0,1)\,dS = 2\operatorname{area}(D) = 2\pi$.
>
> **Part 2.** $\operatorname{curl}(z,x,y) = (1,1,1)$. The triangle lies in $x+y+z=1$ with unit normal $N = (1,1,1)/\sqrt3$; $(\operatorname{curl} F)\cdot N = \sqrt3$. The triangle is equilateral of side $\sqrt2$, area $\sqrt3/2$. By Kelvin-Stokes, $\oint_\gamma F\cdot T\,ds = \sqrt3\cdot\sqrt3/2 = 3/2$.
>
> **Part 3.** The hemisphere $H$ and the disk $D$ share the boundary $\gamma$; by Kelvin-Stokes both fluxes of $\operatorname{curl} F$ equal $\oint_\gamma F\cdot T\,ds = 2\pi$. Equivalently, $H \cup(-D)$ is closed and $\operatorname{div}\operatorname{curl} F = 0$, so the fluxes agree. $\blacksquare$

---

# Key Takeaways

**You choose the spanning surface — pick the flattest one, and the flux integral becomes trivial.** Kelvin-Stokes converts a circulation around a closed curve into the flux of the curl through a surface, and the decisive freedom is that the surface is *not* dictated by the problem: any surface with the given boundary works, and they all give the same answer. The skilled move is to span the curve with the simplest available surface — a planar disk, a planar polygon — because on a flat surface the unit normal $N$ is *constant*, and if (as is common) the curl is also constant, the flux integral collapses to (curl $\cdot$ normal) $\times$ area, a single multiplication. A circulation that would be a tedious sum of arc integrals becomes a one-line computation. The trigger to internalize: *given a circulation around a closed space curve, do not parametrize the curve — compute the curl, span the curve with the flattest surface you can, and dot.*

**Surface-independence of the flux of a curl is the structural reason the choice is free, and it is $d^2 = 0$ in disguise.** Part 3 is the verification that the hemisphere and the flat disk give identical fluxes — and this is not a numerical coincidence but a theorem. The flux of $\operatorname{curl} F$ through a surface depends only on the surface's boundary, because if two surfaces share a boundary, their union (with one reversed) is a *closed* surface, and the flux of a curl through a closed surface is zero — either because a closed surface has no boundary loop for Kelvin-Stokes, or because $\operatorname{div}\operatorname{curl} F = 0$ feeds the divergence theorem. This is the integral shadow of $d\circ d = 0$: the curl $2$-form $d\varphi_F$ is *exact*, and the integral of an exact form over a cycle depends only on the cycle's homology class. The practical consequence reaches beyond this exercise — whenever you integrate a curl (or any exact form) over a surface, you may deform the surface freely as long as the boundary is fixed, and you should deform it to wherever the computation is easiest.

**A constant curl signals that the answer is purely geometric — flux equals a dot product times an area.** In both parts 1 and 2 the curl came out as a *constant* vector, and whenever that happens the entire flux computation reduces to geometry: $\iint_M(\operatorname{curl} F)\cdot N\,dS$, with $\operatorname{curl} F$ constant, is $(\operatorname{curl} F)\cdot\iint_M N\,dS = (\operatorname{curl} F)\cdot(\text{vector area of }M)$, and the vector area depends only on the boundary curve. So a constant curl means: the circulation equals the constant curl vector dotted with the vector area enclosed by the curve. This is why fields like $(-y, x, z)$ — rigid-rotation-type fields — have circulations that are simply "twice the enclosed area" or similar: their curl is constant, and the circulation reads off the geometry of the loop directly. Recognizing a constant (or simple) curl early tells you the problem has collapsed to computing an area or a vector area, with no integration of the field itself required.
