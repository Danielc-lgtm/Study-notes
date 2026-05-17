---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - The Exterior Derivative"
  - "Def - Pullback of a Differential Form"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

1. Let $F : \mathbb{R}^2 \to \mathbb{R}^2$ be polar coordinates, $F(r, \theta) = (r\cos\theta,\ r\sin\theta)$. Compute the pullbacks $F^*dx$, $F^*dy$, and $F^*(dx\wedge dy)$, and confirm that the coefficient of $F^*(dx\wedge dy)$ is the Jacobian determinant $\det DF$.
2. Let $\varphi : \mathbb{R}^2 \to \mathbb{R}^3$ parametrize a piece of the unit sphere by $\varphi(u, v) = (\sin u\cos v,\ \sin u\sin v,\ \cos u)$. Pull back the $1$-form $\alpha = z\,dx$ from $\mathbb{R}^3$ to a $1$-form $\varphi^*\alpha$ on the $(u,v)$-plane.
3. With $F$ the polar map of part 1, take the $1$-form $\alpha = -y\,dx + x\,dy$ on $\mathbb{R}^2$. Compute $F^*\alpha$ and $F^*(d\alpha)$ separately, and verify the naturality identity $d(F^*\alpha) = F^*(d\alpha)$.

**Recall:**

![[Def - Pullback of a Differential Form#The Definition]]

The mechanics: the [[Def - Pullback of a Differential Form|pullback]] $F^*$ substitutes $F$ into coefficients and replaces each $dx_j$ by $dF_j = \sum_\ell(\partial F_j/\partial y_\ell)\,dy_\ell$, then expands wedges by the [[Def - The Wedge Product|wedge algebra]]. The two identities under test:

- **Jacobian on top degree:** $F^*(A\,dx_1\wedge\cdots\wedge dx_n) = A(F)\,(\det DF)\,dy_1\wedge\cdots\wedge dy_n$.
- **Naturality:** $d(F^*\alpha) = F^*(d\alpha)$, i.e. pullback commutes with the [[Def - The Exterior Derivative|exterior derivative]].

---

# Convergent Strategy

**Problem class.** A *computation-plus-verification* problem: execute the pullback recipe on explicit maps, then confirm two structural identities in concrete instances. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy notes that pulling a form back to a flat domain is the universal first move for any integral over a curved object, so the recipe must be fluent.

**Assumption pattern.** Each part gives an explicit smooth map and an explicit form. The recognizable structure: replace $dx_j$ by $dF_j$ — the differential of the $j$-th component — then do wedge algebra. Nothing else is involved.

**Theorem routing.** Part 1 routes through the recipe and the Jacobian identity. Part 2 routes through the recipe alone — the only subtlety is substituting $F$ into the coefficient *and* expanding $dx$ correctly. Part 3 routes through the naturality identity: compute the left side ($d$ after pullback) and the right side ($d$ before pullback) and match.

**Key decision point.** In part 3 the decision is which side of $d(F^*\alpha) = F^*(d\alpha)$ to trust as a check. The interesting observation is that the right side is *much* easier — $d\alpha$ for $\alpha = -y\,dx + x\,dy$ is the simple $2$-form $2\,dx\wedge dy$, whose pullback is just $2\det DF$ — whereas the left side requires pulling back $\alpha$ first and then differentiating a more complicated $1$-form. Naturality says you may always compute on the easy side; this exercise verifies that, and the takeaway is to exploit it.

---

# Legal Operations Used

1. **Pull a form back along a parametrization** — the core operation, applied in all three parts.
2. **Use the determinant identity for wedges** — part 1, where wedging the two row $1$-forms produces $\det DF$.
3. **Use $dF^* = F^*d$ as an algebraic shortcut** — part 3 verifies it, and the takeaway is to use it to compute on whichever side is simpler.

---

# Hints

> [!note]- Hint 1
> $F^*dx$ is the differential of the first component $F_1 = r\cos\theta$: compute $dF_1 = (\partial_r F_1)\,dr + (\partial_\theta F_1)\,d\theta$. Do the same for $F^*dy = dF_2$. Then $F^*(dx\wedge dy) = (F^*dx)\wedge(F^*dy)$ — expand the wedge.

> [!note]- Hint 2
> For $\varphi^*(z\,dx)$: the coefficient $z$ becomes $z\circ\varphi = \cos u$, and $dx$ becomes $d\varphi_1$ where $\varphi_1 = \sin u\cos v$. Compute $d\varphi_1 = (\partial_u\varphi_1)\,du + (\partial_v\varphi_1)\,dv$ and multiply by $\cos u$.

> [!note]- Hint 3
> First compute $d\alpha$ for $\alpha = -y\,dx + x\,dy$ on $\mathbb{R}^2$ — it is a clean $2$-form. Pulling that back is a one-liner using the Jacobian identity. Separately, pull $\alpha$ itself back to the $(r,\theta)$-plane, then apply $d$. The two results must agree.

> [!note]- Hint 4
> In part 3, after pulling $\alpha = -y\,dx + x\,dy$ back through the polar map, you should find $F^*\alpha = r^2\,d\theta$ (a remarkably clean $1$-form — it is the angular form in disguise). Then $d(F^*\alpha) = d(r^2\,d\theta) = 2r\,dr\wedge d\theta$. Compare with $F^*(d\alpha)$.

---

# Solution

The pullback recipe is uniform: substitute $F$ into coefficients, replace $dx_j$ with $dF_j$, expand wedges. The verifications in parts 1 and 3 confirm the two structural identities.

**Step 1: pull back $dx$, $dy$, $dx\wedge dy$ under the polar map.**

$$F^*dx = \cos\theta\,dr - r\sin\theta\,d\theta, \qquad F^*dy = \sin\theta\,dr + r\cos\theta\,d\theta,$$
$$F^*(dx\wedge dy) = r\,dr\wedge d\theta, \quad\text{and } r = \det DF.$$

> [!note]- Derivation
> The components are $F_1 = r\cos\theta$, $F_2 = r\sin\theta$. By the recipe, $F^*dx = dF_1$:
> $$F^*dx = \frac{\partial F_1}{\partial r}\,dr + \frac{\partial F_1}{\partial\theta}\,d\theta = \cos\theta\,dr - r\sin\theta\,d\theta.$$
> Similarly $F^*dy = dF_2 = \sin\theta\,dr + r\cos\theta\,d\theta$.
>
> Now $F^*(dx\wedge dy) = (F^*dx)\wedge(F^*dy)$, since pullback is an algebra homomorphism:
> $$(\cos\theta\,dr - r\sin\theta\,d\theta)\wedge(\sin\theta\,dr + r\cos\theta\,d\theta).$$
> Distribute into four terms. The $dr\wedge dr$ and $d\theta\wedge d\theta$ terms vanish. The surviving terms are $r\cos^2\theta\,dr\wedge d\theta$ and $-r\sin^2\theta\,d\theta\wedge dr = +r\sin^2\theta\,dr\wedge d\theta$. Summing:
> $$F^*(dx\wedge dy) = r(\cos^2\theta + \sin^2\theta)\,dr\wedge d\theta = r\,dr\wedge d\theta.$$
> The Jacobian matrix of $F$ has rows $(\cos\theta, -r\sin\theta)$ and $(\sin\theta, r\cos\theta)$, with determinant $\det DF = r\cos^2\theta + r\sin^2\theta = r$. The coefficient of $F^*(dx\wedge dy)$ is exactly this $\det DF$ — the top-degree Jacobian identity, confirmed. (This is also the familiar area element $dx\,dy = r\,dr\,d\theta$.)

**Step 2: pull back $z\,dx$ to the sphere parameter plane.**

$$\varphi^*(z\,dx) = \cos u\,(\cos u\cos v\,du - \sin u\sin v\,dv) = \cos^2 u\cos v\,du - \sin u\cos u\sin v\,dv.$$

> [!note]- Derivation
> The map has components $\varphi_1 = \sin u\cos v$, $\varphi_2 = \sin u\sin v$, $\varphi_3 = \cos u$. The form $\alpha = z\,dx$ has coefficient $z$ and differential $dx$.
>
> The coefficient pulls back to $z\circ\varphi = \varphi_3 = \cos u$. The differential pulls back to $\varphi^*dx = d\varphi_1$:
> $$d\varphi_1 = \frac{\partial\varphi_1}{\partial u}\,du + \frac{\partial\varphi_1}{\partial v}\,dv = \cos u\cos v\,du - \sin u\sin v\,dv.$$
> Therefore
> $$\varphi^*(z\,dx) = (\cos u)\,(\cos u\cos v\,du - \sin u\sin v\,dv) = \cos^2 u\cos v\,du - \sin u\cos u\sin v\,dv.$$
> Note the two ingredients did not interfere: the coefficient was simply composed with $\varphi$, and the differential was independently replaced by $d\varphi_1$. The product is the pulled-back $1$-form on the $(u,v)$-plane.

**Step 3: verify naturality $d(F^*\alpha) = F^*(d\alpha)$ for the polar map.**

For $\alpha = -y\,dx + x\,dy$: both $d(F^*\alpha)$ and $F^*(d\alpha)$ equal $2r\,dr\wedge d\theta$.

> [!note]- Derivation
> *Right side — pull back, after differentiating.* On $\mathbb{R}^2$, $d\alpha = d(-y\,dx + x\,dy)$. The coefficient of $dx$ is $-y$ with $\partial_y(-y) = -1$; the coefficient of $dy$ is $x$ with $\partial_x(x) = 1$. So $d\alpha = -1\,dy\wedge dx + 1\,dx\wedge dy = 2\,dx\wedge dy$. Pulling back this top-degree form, by Step 1,
> $$F^*(d\alpha) = F^*(2\,dx\wedge dy) = 2\,F^*(dx\wedge dy) = 2r\,dr\wedge d\theta.$$
>
> *Left side — differentiate, after pulling back.* First pull $\alpha$ back. The coefficients become $-y\circ F = -r\sin\theta$ and $x\circ F = r\cos\theta$; the differentials become $F^*dx$ and $F^*dy$ from Step 1. So
> $$F^*\alpha = (-r\sin\theta)(\cos\theta\,dr - r\sin\theta\,d\theta) + (r\cos\theta)(\sin\theta\,dr + r\cos\theta\,d\theta).$$
> Collect the $dr$ terms: $-r\sin\theta\cos\theta + r\cos\theta\sin\theta = 0$. Collect the $d\theta$ terms: $r^2\sin^2\theta + r^2\cos^2\theta = r^2$. Hence
> $$F^*\alpha = r^2\,d\theta.$$
> (This clean result is no accident: $\alpha = -y\,dx + x\,dy$ is $r^2\,d\theta$ in disguise — it is the angular form scaled, see [[Ex - A closed form that is not exact]].) Now differentiate:
> $$d(F^*\alpha) = d(r^2\,d\theta) = (2r\,dr)\wedge d\theta = 2r\,dr\wedge d\theta.$$
>
> *Comparison.* Both sides equal $2r\,dr\wedge d\theta$. The naturality identity $d(F^*\alpha) = F^*(d\alpha)$ holds, as it must — and the computation exhibits the practical point: the right side ($d$ first, then pull back a clean $2$-form) took two lines, while the left side ($pull back first, then differentiate$) took six. Naturality licenses always choosing the easier order.

> [!note]- Complete formal solution
> **Part 1.** $F_1 = r\cos\theta$, $F_2 = r\sin\theta$. $F^*dx = dF_1 = \cos\theta\,dr - r\sin\theta\,d\theta$; $F^*dy = dF_2 = \sin\theta\,dr + r\cos\theta\,d\theta$. Then $F^*(dx\wedge dy) = (F^*dx)\wedge(F^*dy) = r\,dr\wedge d\theta$, and $\det DF = r$, matching.
>
> **Part 2.** $\varphi_1 = \sin u\cos v$, $\varphi_3 = \cos u$. $\varphi^*(z\,dx) = (\cos u)\,d\varphi_1 = \cos u(\cos u\cos v\,du - \sin u\sin v\,dv) = \cos^2 u\cos v\,du - \sin u\cos u\sin v\,dv$.
>
> **Part 3.** $d\alpha = 2\,dx\wedge dy$, so $F^*(d\alpha) = 2r\,dr\wedge d\theta$. Separately $F^*\alpha = r^2\,d\theta$, so $d(F^*\alpha) = 2r\,dr\wedge d\theta$. The two agree: $d(F^*\alpha) = F^*(d\alpha)$. $\blacksquare$

---

# Key Takeaways

**The pullback recipe never changes: substitute into coefficients, replace each $dx_j$ by $dF_j$, expand the wedge.** Every pullback computation in the subject — reducing a surface integral to a flat domain, transporting a form across a coordinate change, proving Stokes' theorem — is this same three-step recipe, and the only thing that varies is the map. The two halves of the recipe do not interact: the coefficient is simply composed with $F$, and the differentials are independently replaced. The single most common error is to forget that $dx_j$ becomes the *whole differential* $dF_j = \sum_\ell(\partial F_j/\partial y_\ell)\,dy_\ell$ — a sum over *all* parameter variables — not just a relabelled symbol. Once the recipe is automatic, pulling a form back to a parameter domain is the reflexive first move whenever an integral over a parametrized object appears.

**Naturality, $d(F^*\alpha) = F^*(d\alpha)$, is a license to compute on the easy side.** Part 3 makes the practical content vivid: differentiating first and pulling back second took a quarter of the work of pulling back first and differentiating second, because $d\alpha$ happened to be a simple top-degree form. The identity guarantees the two orders give the same answer, so you are *free* to pick the cheaper one — and the cheaper one is usually "apply $d$ in whichever space the form is simplest, then pull back". This is not a minor convenience: the proof of the general Stokes theorem leans on exactly this commutation to push the computation into a model half-space, and the homotopy-invariance of de Rham cohomology is naturality applied to a homotopy. Whenever a problem involves both a pullback and an exterior derivative, the first question is "which order is less work" — and naturality says you may always ask it.

**A clean pullback is a signal that the form was secretly written in the wrong coordinates.** In part 3 the form $\alpha = -y\,dx + x\,dy$, which looks like a generic $1$-form in Cartesian coordinates, pulled back to the strikingly simple $r^2\,d\theta$ in polar coordinates. This is diagnostic: a form that simplifies dramatically under a change of variables was "really" a natural object in the new coordinates all along. Here $\alpha$ is, up to the factor $r^2$, the angular form $d\theta$ — the object that measures winding around the origin — and the polar map is exactly the coordinate system adapted to it. The general lesson for problem-solving: when a pullback collapses a messy form to a tiny one, you have found the form's natural home, and computations (line integrals, exactness checks, periods) should be done there. Recognizing the angular form behind $-y\,dx + x\,dy$ is the recognition that drives the entire closed-but-not-exact phenomenon of [[Ex - A closed form that is not exact]].
