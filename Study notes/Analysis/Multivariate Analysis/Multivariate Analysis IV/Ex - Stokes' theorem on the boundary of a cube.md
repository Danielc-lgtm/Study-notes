---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Def - Pullback of a Differential Form"
  - "Def - Orientation and the Integral of a Form"
  - "Thm - The General Stokes Theorem"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $M = [0,1]^3$ be the solid unit cube in $\mathbb{R}^3$, oriented by the standard orientation $dx\wedge dy\wedge dz$, with boundary $\partial M$ the six faces, each carrying the outward-normal induced orientation. Let
$$\beta = x\,dy\wedge dz$$
be a $2$-form on $\mathbb{R}^3$.

1. Compute $d\beta$ and the volume integral $\int_M d\beta$ directly.
2. Compute the surface integral $\int_{\partial M}\beta$ directly, face by face — there are six faces; show that four of them contribute zero and identify the two that do not.
3. Verify that the two computations agree, confirming the general Stokes theorem $\int_M d\beta = \int_{\partial M}\beta$ in this concrete case, and explain why the four vanishing faces vanish.

**Recall:**

![[Thm - The General Stokes Theorem#Statement]]

[[Thm - The General Stokes Theorem|Stokes' theorem]]: for a compact oriented surface with boundary, $\int_M d\beta = \int_{\partial M}\beta$, where $\partial M$ carries the *induced* (outward-normal-first) orientation. The cube is a surface with corners; Stokes still applies.

![[Def - Orientation and the Integral of a Form#The Definition]]

To integrate a $2$-form over a face, parametrize the face and pull the form back; the [[Def - Orientation and the Integral of a Form|induced orientation]] fixes the sign. The outward normal of the face $\{x_i = 1\}$ points in $+e_i$, of $\{x_i = 0\}$ in $-e_i$.

---

# Convergent Strategy

**Problem class.** A *verification* problem: compute both sides of a Stokes identity independently and confirm they match. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy notes that the cube is the cleanest setting to see the proof mechanism of Stokes — interior cancellation, boundary survival — made fully explicit.

**Assumption pattern.** The domain is a cube — a surface with corners, not smooth, but Stokes still applies because a cube decomposes into (indeed *is*) a cornered piece. The form $\beta = x\,dy\wedge dz$ is a basic $2$-form, so its exterior derivative is a single term and its restriction to each face is easy.

**Theorem routing.** Part 1: $d\beta = dx\wedge dy\wedge dz$, so $\int_M d\beta$ is just the volume of the cube. Part 2: on each face, parametrize by the two free coordinates and pull $\beta$ back; a face where $dy\wedge dz$ pulls back to zero (because $y$ or $z$ is constant) contributes nothing, and the two $x = \text{const}$ faces are the only survivors. Part 3 matches the numbers.

**Key decision point.** The non-obvious part is the *orientation bookkeeping on the faces*. The two surviving faces are $\{x=1\}$ and $\{x=0\}$; the outward normal points $+e_x$ on the first and $-e_x$ on the second, so the two contributions have opposite sign — and the cube computation works precisely because $\beta$ depends on $x$, so the two faces do *not* cancel but combine into $\int_0^1 dx = 1$. Getting the induced-orientation signs right is the whole subtlety.

---

# Legal Operations Used

1. **Compute $d$ of a form** — part 1, computing $d\beta = dx\wedge dy\wedge dz$.
2. **Apply the general Stokes theorem** — the identity being verified; also the licence (operation 9, subdivide into cornered pieces) that lets Stokes apply to the non-smooth cube.
3. **Pull a form back along a parametrization** — part 2, pulling $\beta$ back onto each of the six faces.
4. **Track the induced orientation** — part 2, fixing the sign of each face's contribution by the outward-normal convention.

---

# Hints

> [!note]- Hint 1
> For part 1, $d\beta = d(x\,dy\wedge dz)$. The coefficient is $x$; differentiate it and wedge on the new differential, discarding repeated-index terms. Only one term survives. Then $\int_M d\beta$ is the integral of a constant over the cube.

> [!note]- Hint 2
> For part 2, the six faces are $\{x=0\}, \{x=1\}, \{y=0\}, \{y=1\}, \{z=0\}, \{z=1\}$. On a face where $y$ is constant, what is the pullback of $dy$? On a face where $z$ is constant, what is the pullback of $dz$? The form $\beta$ contains $dy\wedge dz$.

> [!note]- Hint 3
> On the faces $\{x=0\}$ and $\{x=1\}$, the coordinates $y, z$ are free, so $dy\wedge dz$ survives the pullback. The coefficient $x$ is constant on each: $0$ on one face, $1$ on the other. The outward normal is $+e_x$ on $\{x=1\}$ and $-e_x$ on $\{x=0\}$ — this fixes the orientation sign.

> [!note]- Hint 4
> The face $\{x=1\}$ contributes $+\int\int x\,dy\,dz = +1$ (with $x=1$); the face $\{x=0\}$ contributes $-\int\int x\,dy\,dz = 0$ (with $x=0$). The minus sign is from the inward-pointing... no — from the *outward* normal $-e_x$ on the $x=0$ face. Sum the six faces and compare with part 1.

---

# Solution

The exterior derivative $d\beta$ is the constant $3$-form $dx\wedge dy\wedge dz$, so the left side of Stokes is the cube's volume. On the right side, four of the six faces kill the form because $dy$ or $dz$ pulls back to zero there; the two $x = \text{const}$ faces survive, and because $\beta$'s coefficient $x$ differs on them, they combine rather than cancel.

**Step 1: $d\beta$ and $\int_M d\beta$.**

$$d\beta = dx\wedge dy\wedge dz, \qquad \int_M d\beta = \int_{[0,1]^3} 1\,dV = 1.$$

> [!note]- Derivation
> The form is $\beta = x\,dy\wedge dz$, coefficient $x$. Apply the exterior derivative: differentiate $x$ with respect to all three variables and wedge the new differential onto $dy\wedge dz$:
> $$d\beta = (\partial_x x)\,dx\wedge dy\wedge dz + (\partial_y x)\,dy\wedge dy\wedge dz + (\partial_z x)\,dz\wedge dy\wedge dz.$$
> Now $\partial_x x = 1$, $\partial_y x = 0$, $\partial_z x = 0$, and the second and third terms have repeated differentials anyway. So
> $$d\beta = dx\wedge dy\wedge dz.$$
> The left side of Stokes is the integral of this $3$-form over the cube. By the definition of the integral of a top-degree form, $\int_M(dx\wedge dy\wedge dz)$ is the ordinary integral of the coefficient $1$ over $[0,1]^3$:
> $$\int_M d\beta = \int_0^1\!\!\int_0^1\!\!\int_0^1 1\;dx\,dy\,dz = 1.$$
> (Indeed $d\beta$ is the volume form, so $\int_M d\beta$ is the volume of the cube, which is $1$.)

**Step 2: $\int_{\partial M}\beta$, face by face.**

Four faces ($y=0, y=1, z=0, z=1$) contribute $0$. The face $x=1$ contributes $+1$; the face $x=0$ contributes $0$. Total: $\int_{\partial M}\beta = 1$.

> [!note]- Derivation
> The boundary $\partial M$ is six unit squares. On each, parametrize by the two free coordinates, pull $\beta = x\,dy\wedge dz$ back, and attach the sign of the outward-normal induced orientation.
>
> *Faces $\{y = 0\}$ and $\{y = 1\}$.* Here $y$ is constant, so the pullback of $dy$ to the face is $d(\text{const}) = 0$. Since $\beta$ contains the factor $dy$, the pullback $\beta|_{\text{face}} = x\,(\,0\,)\wedge dz = 0$. Both faces contribute $0$.
>
> *Faces $\{z = 0\}$ and $\{z = 1\}$.* Here $z$ is constant, so the pullback of $dz$ is $0$. Since $\beta$ contains $dz$, $\beta|_{\text{face}} = x\,dy\wedge 0 = 0$. Both faces contribute $0$.
>
> *Face $\{x = 1\}$.* Here $x$ is constant ($= 1$), and the free coordinates are $y, z$, so $dy$ and $dz$ pull back to themselves and $dy\wedge dz$ survives. The outward normal points in $+e_x$, and the induced orientation of this face (outward normal first, then a positive frame of the face) makes $dy\wedge dz$ the *positive* area form. The coefficient $x = 1$. So
> $$\int_{\{x=1\}}\beta = +\int_0^1\!\!\int_0^1 1\;dy\,dz = +1.$$
>
> *Face $\{x = 0\}$.* Again $y, z$ free, $dy\wedge dz$ survives. But the outward normal points in $-e_x$, so the induced orientation makes $-dy\wedge dz$ the positive area form — the contribution carries a minus sign relative to the $dy\wedge dz$ reading. The coefficient $x = 0$. So
> $$\int_{\{x=0\}}\beta = -\int_0^1\!\!\int_0^1 0\;dy\,dz = 0.$$
> (The minus sign is genuine, but here it multiplies $0$.)
>
> Summing all six faces:
> $$\int_{\partial M}\beta = \underbrace{0 + 0 + 0 + 0}_{y,z\text{ faces}} + \underbrace{1}_{x=1} + \underbrace{0}_{x=0} = 1.$$

**Step 3: agreement, and why the four faces vanish.**

Both sides equal $1$: $\int_M d\beta = 1 = \int_{\partial M}\beta$. Stokes' theorem is confirmed.

> [!note]- Derivation
> Part 1 gave $\int_M d\beta = 1$; part 2 gave $\int_{\partial M}\beta = 1$. They agree — the general Stokes theorem $\int_M d\beta = \int_{\partial M}\beta$ holds for this $\beta$ on the cube.
>
> *Why the four faces vanish.* The form $\beta = x\,dy\wedge dz$ "wants" to be integrated over a surface whose tangent plane contains the $y$- and $z$-directions — a surface where $y$ and $z$ vary. On a face where $y$ is held constant ($\{y=0\}$ or $\{y=1\}$), the $1$-form $dy$ restricts to zero, because $dy$ measures change in $y$ and there is none along the face; the factor $dy$ inside $\beta$ then kills the whole pullback. Likewise on the $z$-constant faces. So $\beta$ "sees" only the two faces on which both $y$ and $z$ are free — the $x = \text{const}$ faces. This is the general principle: *a basic $2$-form $dx_i\wedge dx_j$ restricts to zero on any face where $x_i$ or $x_j$ is constant.*
>
> *Why the two surviving faces do not cancel.* The faces $\{x=0\}$ and $\{x=1\}$ carry *opposite* induced orientations (outward normals $-e_x$ and $+e_x$). If the coefficient of $\beta$ were independent of $x$ — say $\beta = 5\,dy\wedge dz$ — the two contributions would be $+5$ and $-5$ and would cancel, giving $\int_{\partial M}\beta = 0$, consistent with $d\beta = 0$ for an $x$-independent coefficient. The two faces fail to cancel here precisely because $\beta$'s coefficient $x$ takes *different values* on them ($1$ versus $0$), and that difference, $1 - 0 = 1$, is exactly $\int_0^1\partial_x x\,dx$ — the Fundamental Theorem of Calculus in the $x$-direction. This is the proof mechanism of Stokes laid bare: the boundary integral is the *net* of the two transverse faces, and that net is the integral of the derivative across the slab between them.

> [!note]- Complete formal solution
> **Left side.** $d\beta = d(x\,dy\wedge dz) = dx\wedge dy\wedge dz$, so $\int_M d\beta = \int_{[0,1]^3} 1\,dV = 1$.
>
> **Right side.** On $\{y=\text{const}\}$ and $\{z=\text{const}\}$, the pullback of $dy$ resp. $dz$ vanishes, so $\beta$ restricts to $0$ on those four faces. On $\{x=1\}$ (outward normal $+e_x$, induced orientation making $dy\wedge dz$ positive), $\int\beta = +\int_0^1\!\int_0^1 1\,dy\,dz = 1$. On $\{x=0\}$ (outward normal $-e_x$, induced orientation making $dy\wedge dz$ negative), $\int\beta = -\int_0^1\!\int_0^1 0\,dy\,dz = 0$. Sum: $\int_{\partial M}\beta = 1$.
>
> **Agreement.** $\int_M d\beta = 1 = \int_{\partial M}\beta$, verifying Stokes' theorem. $\blacksquare$

---

# Key Takeaways

**A basic $2$-form restricts to zero on any face where one of its differentials is held constant — this is how Stokes' boundary integral selects faces.** The form $\beta = x\,dy\wedge dz$ contributed nothing on four of the cube's six faces, and the reason was uniform: $dy$ restricts to zero on a $y$-constant face, $dz$ on a $z$-constant face, and either vanishing factor kills the whole pullback. This is a completely general and very useful shortcut for any boundary integral over a box-like region: before computing, look at each face, ask which coordinates are constant there, and discard every face on which the form has a differential of a constant coordinate. Typically only a few faces survive — for a basic $(n-1)$-form $dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$ on an $n$-cube, only the two faces $\{x_j = 0\}$ and $\{x_j = 1\}$ survive. This pre-selection turns a six-integral (or $2n$-integral) computation into a two-integral one.

**The induced orientation makes opposite faces carry opposite signs, and that sign difference is the Fundamental Theorem of Calculus.** The two surviving faces $\{x=0\}$ and $\{x=1\}$ had outward normals pointing in opposite directions, so their contributions entered the boundary integral with opposite signs. The boundary integral is therefore a *difference* — the value of the coefficient on the far face minus its value on the near face — and that difference is exactly $\int_0^1\partial_x(\text{coefficient})\,dx$. This is not a peculiarity of the cube; it is the engine of Stokes' theorem itself, visible without the partition-of-unity machinery. The practical consequence: if a form's coefficient is *independent* of the transverse coordinate, the two faces cancel and the boundary integral is zero — which is consistent, because then $d\beta = 0$ too. The lesson for verification problems: always attach the outward-normal sign to each surviving face; the cancellations and non-cancellations it produces are the whole content of the theorem.

**The cube is the worked model of Stokes' proof — interior structure cancels, boundary survives — and works despite the corners.** A solid cube is not a smooth surface; it has edges and vertices where the boundary is not differentiable. Yet Stokes' theorem applies, because the theorem holds for surfaces *with corners*, and a cube is the prototypical such surface. The verification here makes the proof mechanism concrete: the four tangential faces contribute nothing (the "interior cancels" half), the two transverse faces combine into the integral of the derivative (the "boundary survives" half). Whenever a region is a box, a polytope, or a piecewise-smooth domain, the same applies — subdivide if necessary into cornered pieces, apply Stokes to each, and the internal faces cancel because each is shared by two pieces with opposite induced orientation. The cube computation is the template for trusting Stokes on any non-smooth but piecewise-nice domain.
