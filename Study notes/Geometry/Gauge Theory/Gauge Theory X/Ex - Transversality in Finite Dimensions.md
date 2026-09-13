---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Regular Value and Transversality for Fredholm Maps"
  - "Thm - Regular Value and Transversality Theorems for Fredholm Maps"
  - "Def - Fredholm Map and Its Index"
tags: [geometry, gauge-theory]
---

# Problem Statement

This is a drill of the transversality definition in the setting where every space is finite-dimensional, so that a smooth map $F:X\to Y$ between manifolds is automatically Fredholm with $\operatorname{index}F=\dim X-\dim Y$, and the abstract preimage-dimension formula $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z$ can be checked against a picture one can draw.

Work through the following.

1. **(Parabola against horizontal lines.)** Parametrise the parabola by
$$F:\mathbb{R}\to\mathbb{R}^{2},\qquad F(x)=(x,x^{2}),$$
and for each real number $c$ let $Z_{c}:=\{(t,c):t\in\mathbb{R}\}=\mathbb{R}\times\{c\}$ be the horizontal line $y=c$, a one-dimensional embedded submanifold of $\mathbb{R}^{2}$. Decide, for every $c\in\mathbb{R}$, whether $F\pitchfork Z_{c}$. Wherever transversality holds, compute $\dim F^{-1}(Z_{c})$ both directly and from the formula $\operatorname{index}F+\dim Z_{c}$, and confirm they agree. Identify the single value of $c$ at which transversality fails and say geometrically what goes wrong.

2. **(A map to the plane against a coordinate line.)** For
$$F:\mathbb{R}^{3}\to\mathbb{R}^{2},\qquad F(x,y,z)=(x^{2}+y^{2},\,z),$$
and the line
$$Z:=\{(1,t):t\in\mathbb{R}\}=\{1\}\times\mathbb{R}\subset\mathbb{R}^{2}$$
(the vertical line $u=1$ in the target plane with coordinates $(u,v)$), decide whether $F\pitchfork Z$. If so, compute $\dim F^{-1}(Z)$ directly and from the formula $\operatorname{index}F+\dim Z$, and describe $F^{-1}(Z)$ as a familiar submanifold of $\mathbb{R}^{3}$.

**Recall:**

The objects in play are a smooth map $F$ between finite-dimensional manifolds, its differential $d_{x}F$, a regular value, transversality of a map to a submanifold, and the two preimage theorems.

![[Def - Fredholm Map and Its Index#The Definition]]

Between finite-dimensional manifolds every smooth map is a [[Def - Fredholm Map and Its Index|Fredholm map]]: the differential $d_{x}F:T_{x}X\to T_{F(x)}Y$ is a linear map between finite-dimensional spaces, so its kernel and cokernel are automatically finite-dimensional and its range is closed. The index is the elementary linear-algebra quantity
$$\operatorname{index}d_{x}F=\dim\ker d_{x}F-\dim\operatorname{coker}d_{x}F=\dim X-\dim Y,$$
independent of $x$, by the rank–nullity theorem ($\dim\ker d_{x}F=\dim X-\operatorname{rank}d_{x}F$ and $\dim\operatorname{coker}d_{x}F=\dim Y-\operatorname{rank}d_{x}F$, whose difference is $\dim X-\dim Y$).

![[Def - Regular Value and Transversality for Fredholm Maps#The Definition]]

A point $y\in Y$ is a [[Def - Regular Value and Transversality for Fredholm Maps|regular value]] of $F$ if $d_{x}F$ is surjective for every $x\in F^{-1}(y)$ (vacuously if $F^{-1}(y)=\varnothing$). More generally, for an embedded submanifold $Z\subset Y$, the map $F$ is **transverse** to $Z$, written $F\pitchfork Z$, if
$$\operatorname{Im}d_{x}F+T_{z}Z=T_{z}Y\qquad\text{for every }z\in Z\text{ and every }x\in F^{-1}(z).$$
Taking $Z=\{y\}$ a single point (so $T_{z}Z=\{0\}$) recovers the condition that $y$ is a regular value.

![[Thm - Regular Value and Transversality Theorems for Fredholm Maps#Statement]]

The two preimage theorems we verify against are: **(i)** if $y$ is a regular value of $F$ then $F^{-1}(y)$ is a smooth embedded submanifold of $X$ with $\dim F^{-1}(y)=\operatorname{index}F$ and $T_{x}F^{-1}(y)=\ker d_{x}F$; and **(ii)** if $Z\subset Y$ is a finite-dimensional embedded submanifold and $F\pitchfork Z$, then $F^{-1}(Z)$ is a smooth embedded submanifold of $X$ with
$$\dim F^{-1}(Z)=\operatorname{index}F+\dim Z .$$
(Both are proved in full on [[Thm - Regular Value and Transversality Theorems for Fredholm Maps]].)

---

# Convergent Strategy

**Problem class.** This is a *decide-transversality-and-count-dimensions* drill: given an explicit smooth map and an explicit submanifold of its target, one must check the algebraic condition $\operatorname{Im}d_{x}F+T_{z}Z=T_{z}Y$ at each intersection point and then read the dimension of the preimage from the index formula. It is the finite-dimensional shadow of every genericity argument in gauge theory, where the same condition — differential-image plus submanifold-tangent fills the target — is what makes a moduli space smooth of the expected dimension.

**Assumption pattern.** In finite dimensions the transversality condition simplifies decisively: since $T_{z}Y$ is finite-dimensional, "$\operatorname{Im}d_{x}F+T_{z}Z=T_{z}Y$" is a rank condition one checks by comparing dimensions of concrete subspaces. When $Z$ is a hypersurface (codimension $1$), transversality reduces to "$\operatorname{Im}d_{x}F\not\subset T_{z}Z$", that is, the image of the differential is not entirely tangent to $Z$. When $F$ has more source dimensions than the codimension of $Z$, surjectivity of $d_{x}F$ already forces transversality regardless of $Z$; this is the situation in part 2.

**Theorem routing.** The route is uniform. First locate the intersection locus $F^{-1}(Z)$ by solving $F(x)\in Z$. At each such point compute the two subspaces $\operatorname{Im}d_{x}F$ and $T_{z}Z$ of $T_{z}Y$ and test whether they span. If they span at every point of $F^{-1}(Z)$, then $F\pitchfork Z$ and part (ii) of [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the transversality theorem]] gives $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z$ with $\operatorname{index}F=\dim X-\dim Y$. Finally cross-check this dimension against a direct description of $F^{-1}(Z)$.

**Key decision point.** The only subtlety is that transversality is a condition *at the intersection points only*: where $F^{-1}(Z)$ is empty the condition holds vacuously (part 1, $c<0$), and the index formula returns a submanifold of the predicted dimension which happens to be the empty set. The genuine decision is to test the spanning condition point by point on $F^{-1}(Z)$ and to recognise that failure at even one point (part 1, $c=0$, where the parabola is tangent to the line) destroys transversality and voids the dimension formula there — even though the preimage $F^{-1}(Z_{0})=\{0\}$ still happens to be a manifold, it is not the *transversal* intersection the theorem describes.

---

# Legal Operations Used

The following operations are drawn from the Legal Operations of the topic page [[Gauge Theory X — Fredholm Maps, Transversality, and Degree]]; until that page fixes their numbering they are named descriptively here.

1. **Compute the index of a finite-dimensional map as a dimension difference.** For $F:X\to Y$ between finite-dimensional manifolds, $\operatorname{index}F=\dim X-\dim Y$ with no analysis required.

2. **Locate the intersection locus by solving the incidence equations.** Determine $F^{-1}(Z)$ explicitly as the set of $x$ with $F(x)\in Z$.

3. **Test transversality as a spanning condition on two concrete subspaces.** At each $z\in Z$ with $x\in F^{-1}(z)$, decide whether $\operatorname{Im}d_{x}F+T_{z}Z$ exhausts $T_{z}Y$.

4. **Reduce hypersurface transversality to non-tangency.** For $Z$ of codimension $1$, transversality at $z$ is exactly "$\operatorname{Im}d_{x}F\not\subset T_{z}Z$".

5. **Apply the preimage-dimension formula.** Once $F\pitchfork Z$, invoke part (ii) of [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the transversality theorem]] for $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z$.

6. **Cross-check by a direct parametrisation of the preimage.** Confirm the computed dimension by exhibiting $F^{-1}(Z)$ as an explicit familiar submanifold.

---

# Hints

> [!note]- Hint 1
> Transversality is only tested *at points where $F$ actually hits $Z$*. So the first move in every part is to solve $F(x)\in Z$ and find the intersection locus. Where that locus is empty, transversality holds automatically.

> [!note]- Hint 2
> At an intersection point $z=F(x)$, you need two subspaces of $T_{z}Y=\mathbb{R}^{2}$: the image $\operatorname{Im}d_{x}F$ of the differential, and the tangent line $T_{z}Z$ to the submanifold. Transversality means these two together span $\mathbb{R}^{2}$. For a curve parametrised by $F$, $\operatorname{Im}d_{x}F$ is the span of the velocity vector $F'(x)$; for a line $Z$, $T_{z}Z$ is the line's own direction.

> [!note]- Hint 3
> Part 1: $F'(x)=(1,2x)$ and $Z_{c}$ has direction $(1,0)$. When do $(1,2x)$ and $(1,0)$ span $\mathbb{R}^{2}$? Only when $2x\ne 0$. Now which intersection points $x$ (solving $x^{2}=c$) have $x\ne 0$? Part 2: compute the $2\times 3$ Jacobian of $F$ and ask when it has rank $2$; at points with $x^{2}+y^{2}=1$ the point $(x,y)$ is never the origin, which is decisive.

> [!note]- Hint 4
> Part 1: for $c>0$ the two roots $x=\pm\sqrt c$ are nonzero, so transverse; for $c=0$ the single root $x=0$ gives $F'(0)=(1,0)$ parallel to the line, so *not* transverse (the parabola is tangent to $y=0$ at the origin); for $c<0$ no intersection, vacuously transverse. Index $F=1-2=-1$, so the formula gives $\dim F^{-1}(Z_{c})=-1+1=0$, matching the finite point set. Part 2: $d_{(x,y,z)}F$ is surjective wherever $(x,y)\ne(0,0)$, which holds on all of $F^{-1}(Z)$, so $F\pitchfork Z$; index $F=3-2=1$, and $\dim F^{-1}(Z)=1+1=2$ — the cylinder $x^{2}+y^{2}=1$.

---

# Solution

Both parts follow one recipe: solve for the intersection locus, compute at each intersection point the differential-image and the submanifold-tangent as concrete subspaces of the target, decide whether they span, and — where they do — read the preimage dimension from $\operatorname{index}F+\dim Z$ and confirm it against a direct description. The only conceptual care needed is that transversality is tested only at intersection points, so an empty intersection is vacuously transverse and a single point of tangency suffices to break transversality.

**Step 1: Part 1 — the index and the intersection locus.**

$F:\mathbb{R}\to\mathbb{R}^{2}$ has index $\operatorname{index}F=1-2=-1$, and $F^{-1}(Z_{c})=\{x:x^{2}=c\}$.

> [!note]- Derivation
> Since $F:\mathbb{R}\to\mathbb{R}^{2}$ is a smooth map between finite-dimensional manifolds, it is a [[Def - Fredholm Map and Its Index|Fredholm map]] with
> $$\operatorname{index}F=\dim\mathbb{R}-\dim\mathbb{R}^{2}=1-2=-1 \qquad \text{(index of a finite-dimensional map).}$$
> An intersection point is an $x\in\mathbb{R}$ with $F(x)=(x,x^{2})\in Z_{c}=\mathbb{R}\times\{c\}$; the first coordinate $x$ is unconstrained, and the second coordinate must equal $c$, so
> $$F^{-1}(Z_{c})=\{x\in\mathbb{R}:x^{2}=c\} \qquad \text{(the second coordinate of } F(x) \text{ is } x^{2}, \text{ set equal to } c\text{).}$$
> Thus $F^{-1}(Z_{c})$ has two points $\{\pm\sqrt c\}$ if $c>0$, one point $\{0\}$ if $c=0$, and is empty if $c<0$.

**Step 2: Part 1 — the transversality test at each intersection point.**

At $x$ with $F(x)\in Z_{c}$ we have $\operatorname{Im}d_{x}F=\operatorname{span}\{(1,2x)\}$ and $T_{z}Z_{c}=\operatorname{span}\{(1,0)\}$; these span $\mathbb{R}^{2}$ if and only if $x\ne 0$.

> [!note]- Derivation
> The differential of $F(x)=(x,x^{2})$ is $d_{x}F=(1,2x)^{\mathsf T}$, so
> $$\operatorname{Im}d_{x}F=\operatorname{span}\{(1,2x)\}\subset\mathbb{R}^{2} \qquad \text{(the image of a map from a line is the span of its velocity).}$$
> The line $Z_{c}=\mathbb{R}\times\{c\}$ has constant tangent direction $(1,0)$, so $T_{z}Z_{c}=\operatorname{span}\{(1,0)\}$ at every $z\in Z_{c}$. The transversality condition at $z=F(x)$ is $\operatorname{Im}d_{x}F+T_{z}Z_{c}=\mathbb{R}^{2}$, i.e. the two vectors $(1,2x)$ and $(1,0)$ are linearly independent. Their determinant is
> $$\det\begin{pmatrix}1&2x\\ 1&0\end{pmatrix}=1\cdot 0-2x\cdot 1=-2x \qquad \text{(expand the } 2\times2 \text{ determinant),}$$
> which is nonzero if and only if $x\ne 0$. (This is operation 4: $Z_{c}$ is a hypersurface, and transversality is non-tangency of the parabola's velocity to the line.)
>
> Now read off each case.
> - **$c>0$:** the intersection points $x=\pm\sqrt c$ are both nonzero, so the spanning condition holds at every point of $F^{-1}(Z_{c})$; hence $F\pitchfork Z_{c}$.
> - **$c=0$:** the only intersection point is $x=0$, where $(1,0)$ and $(1,0)$ coincide and fail to span; hence $F\not\pitchfork Z_{0}$. Geometrically, at the origin the parabola is *tangent* to the line $y=0$: its velocity $(1,0)$ points along the line.
> - **$c<0$:** $F^{-1}(Z_{c})=\varnothing$, so the transversality condition is vacuously satisfied; hence $F\pitchfork Z_{c}$.

**Step 3: Part 1 — the dimension formula against the direct count.**

Wherever $F\pitchfork Z_{c}$ (that is, $c\ne 0$), the formula gives $\dim F^{-1}(Z_{c})=\operatorname{index}F+\dim Z_{c}=-1+1=0$, matching the direct count.

> [!note]- Derivation
> For $c\ne 0$ we have $F\pitchfork Z_{c}$ (Step 2), so part (ii) of [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the transversality theorem]] applies. With $\operatorname{index}F=-1$ (Step 1) and $\dim Z_{c}=1$,
> $$\dim F^{-1}(Z_{c})=\operatorname{index}F+\dim Z_{c}=-1+1=0 \qquad \text{(preimage-dimension formula).}$$
> A zero-dimensional embedded submanifold is a discrete set of points. This matches Step 1 directly: for $c>0$, $F^{-1}(Z_{c})=\{\pm\sqrt c\}$ is two points ($0$-dimensional), and for $c<0$, $F^{-1}(Z_{c})=\varnothing$ (the empty manifold, of every dimension, in particular the predicted $0$). At $c=0$ the theorem does not apply because transversality fails; the preimage $\{0\}$ happens to be a manifold, but it is not the transversal intersection the formula describes, and indeed the parabola crosses the line tangentially there rather than cleanly.

**Step 4: Part 2 — the index, the intersection locus, and the transversality test.**

$F:\mathbb{R}^{3}\to\mathbb{R}^{2}$ has index $\operatorname{index}F=3-2=1$; the intersection locus is $F^{-1}(Z)=\{x^{2}+y^{2}=1\}$; and $d_{(x,y,z)}F$ is surjective at every point of it, so $F\pitchfork Z$.

> [!note]- Derivation
> The map $F(x,y,z)=(x^{2}+y^{2},z)$ between finite-dimensional manifolds is Fredholm with
> $$\operatorname{index}F=\dim\mathbb{R}^{3}-\dim\mathbb{R}^{2}=3-2=1 \qquad \text{(index of a finite-dimensional map).}$$
> An intersection point is $(x,y,z)$ with $F(x,y,z)=(x^{2}+y^{2},z)\in Z=\{1\}\times\mathbb{R}$; the first coordinate must be $1$ and the second (namely $z$) is unconstrained, so
> $$F^{-1}(Z)=\{(x,y,z):x^{2}+y^{2}=1\} \qquad \text{(set the first coordinate } x^{2}+y^{2}=1\text{).}$$
> The differential is the $2\times 3$ Jacobian
> $$d_{(x,y,z)}F=\begin{pmatrix}2x&2y&0\\ 0&0&1\end{pmatrix},$$
> whose rows are $(2x,2y,0)$ and $(0,0,1)$. These are linearly independent — hence $d_{(x,y,z)}F$ is surjective onto $\mathbb{R}^{2}$ — precisely when $(2x,2y)\ne(0,0)$, i.e. $(x,y)\ne(0,0)$. On the intersection locus $x^{2}+y^{2}=1$, we always have $(x,y)\ne(0,0)$, so $d_{(x,y,z)}F$ is surjective at every point of $F^{-1}(Z)$. Surjectivity of the differential gives $\operatorname{Im}d_{(x,y,z)}F=T_{z}\mathbb{R}^{2}$ already, so a fortiori $\operatorname{Im}d_{(x,y,z)}F+T_{z}Z=T_{z}\mathbb{R}^{2}$; hence $F\pitchfork Z$.

**Step 5: Part 2 — the dimension formula against the direct description.**

The formula gives $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z=1+1=2$, and indeed $F^{-1}(Z)$ is the cylinder $x^{2}+y^{2}=1$ in $\mathbb{R}^{3}$, a surface.

> [!note]- Derivation
> Since $F\pitchfork Z$ (Step 4) and $\dim Z=1$, part (ii) of [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the transversality theorem]] gives
> $$\dim F^{-1}(Z)=\operatorname{index}F+\dim Z=1+1=2 \qquad \text{(preimage-dimension formula).}$$
> Directly, $F^{-1}(Z)=\{(x,y,z):x^{2}+y^{2}=1\}$ is the circular cylinder of radius $1$ about the $z$-axis, parametrised by $(\theta,z)\mapsto(\cos\theta,\sin\theta,z)$; it is diffeomorphic to $S^{1}\times\mathbb{R}$, a $2$-dimensional embedded submanifold. Its dimension is $2$, matching the formula.

> [!note]- Complete formal solution
> **Part 1.** $F(x)=(x,x^{2})$ is Fredholm of index $1-2=-1$. Intersections with $Z_{c}=\mathbb{R}\times\{c\}$ solve $x^{2}=c$. At an intersection, $\operatorname{Im}d_{x}F=\operatorname{span}\{(1,2x)\}$ and $T Z_{c}=\operatorname{span}\{(1,0)\}$; they span $\mathbb{R}^{2}$ iff $\det\!\big(\begin{smallmatrix}1&2x\\1&0\end{smallmatrix}\big)=-2x\ne 0$, i.e. $x\ne 0$. Hence: for $c>0$ the roots $\pm\sqrt c$ are nonzero and $F\pitchfork Z_{c}$; for $c<0$ the intersection is empty and $F\pitchfork Z_{c}$ vacuously; for $c=0$ the only root $x=0$ gives tangency and $F\not\pitchfork Z_{0}$. Where transverse, $\dim F^{-1}(Z_{c})=\operatorname{index}F+\dim Z_{c}=-1+1=0$, agreeing with the count ($\{\pm\sqrt c\}$ two points for $c>0$; $\varnothing$ for $c<0$).
>
> **Part 2.** $F(x,y,z)=(x^{2}+y^{2},z)$ is Fredholm of index $3-2=1$. Intersections with $Z=\{1\}\times\mathbb{R}$ solve $x^{2}+y^{2}=1$. The Jacobian $\big(\begin{smallmatrix}2x&2y&0\\0&0&1\end{smallmatrix}\big)$ has rank $2$ whenever $(x,y)\ne(0,0)$, which holds throughout $x^{2}+y^{2}=1$; so $d F$ is surjective there and $F\pitchfork Z$. Thus $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z=1+1=2$, and $F^{-1}(Z)=\{x^{2}+y^{2}=1\}\cong S^{1}\times\mathbb{R}$ is the cylinder, a surface. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to declare a map "transverse to $Z$" the moment one exhibits *some* point where $\operatorname{Im}d_{x}F+T_{z}Z=T_{z}Y$, or to test the spanning condition at a point not in $Z$. Both are wrong. Transversality is a *universally quantified* condition over *all* intersection points $x\in F^{-1}(Z)$: in part 1 with $c>0$ one must check both roots $\pm\sqrt c$, not one; and at $c=0$ the single point $x=0$ fails, which by itself makes $F\not\pitchfork Z_{0}$. Conversely, testing the determinant $-2x$ at some $x$ with $x^{2}\ne c$ is meaningless, because such an $x$ is not an intersection point and imposes no condition. The safe procedure is to first pin down $F^{-1}(Z)$ exactly, then test the spanning condition at each of its points.

---

# Key Takeaways

**Transversality is a spanning condition tested only at intersection points, and an empty intersection is always transverse.** This is the reusable principle that governs every application of the concept, from these plane pictures to the smoothness of gauge-theoretic moduli spaces. The condition $\operatorname{Im}d_{x}F+T_{z}Z=T_{z}Y$ is required at every $x\in F^{-1}(Z)$ and at no other point; consequently, where $F$ misses $Z$ entirely, transversality holds vacuously and the preimage theorem returns the empty manifold of the predicted dimension. The transferable diagnostic is procedural: never test transversality before you have solved the incidence equations $F(x)\in Z$, and once you have, quantify over *all* solutions. In part 1 this is the difference between the clean two-point crossing at $c>0$ and the tangential failure at $c=0$; the entire content of "transversality" is that the crossing is clean at every contact.

**In finite dimensions the index is a dimension count and transversality is a rank condition, which is exactly why the abstract formula $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z$ is checkable by hand.** The trigger for the finite-dimensional shortcut is simply that source and target are ordinary manifolds: then $\operatorname{index}F=\dim X-\dim Y$ with no analysis, and the spanning condition becomes a statement about the rank of a Jacobian matrix. When $Z$ has codimension $1$ (a hypersurface, as both $Z_{c}$ and $Z$ here are), transversality collapses to "the image of $d_{x}F$ is not contained in $T_{z}Z$", a single non-vanishing determinant or a single rank-$2$ Jacobian. Note also the useful special case visible in part 2: if $d_{x}F$ is already *surjective* at the intersection points, then $F$ is transverse to *every* submanifold through those points, because a subspace summed with the whole target is the whole target. Recognising surjectivity of the differential as automatic transversality saves the explicit subspace computation whenever the map has enough source dimensions.

**The preimage-dimension formula is the finite-dimensional prototype of the moduli-space dimension count, and reading it correctly trains the reflex that governs the infinite-dimensional theory.** In part 2 the negative-to-positive shift is instructive: a map of index $-1$ (part 1) transverse to a line yields a $0$-dimensional intersection, whereas a map of index $+1$ (part 2) transverse to a line yields a $2$-dimensional cylinder — the same $+\dim Z$ correction added to opposite indices. In gauge theory the map is a section of an infinite-dimensional bundle, $Z$ is the zero section, and $\operatorname{index}F$ is the Fredholm index of a linearised elliptic operator; the formula $\dim(\text{moduli space})=\operatorname{index}+\dim Z$ is literally this one, with the finite-dimensional index replaced by the elliptic index computed in the companion exercise [[Ex - Semilinear Elliptic Maps are Fredholm]]. Drilling the finite-dimensional version until the count is automatic is what makes the expected-dimension formula for a moduli space read as an accounting identity rather than a mystery; the genericity that secures transversality in that setting is supplied by the Sard–Smale theorem and the parametric transversality package of [[Ex - Parametric Transversality for a Family of Elliptic Equations]].
