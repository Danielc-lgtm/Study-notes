---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - Pullback of a Differential Form"
  - "Def - Orientation and the Integral of a Form"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $M$ be the piece of the graph $z = x^2 - y^2$ lying over the unit square $0 \le x \le 1$, $0 \le y \le 1$, parametrized by $\varphi(x, y) = (x,\ y,\ x^2 - y^2)$ and oriented by the upward normal.

1. Integrate the $2$-form $\omega = z\,dx\wedge dy$ over $M$ by pulling $\omega$ back along $\varphi$ to the unit square and evaluating the resulting ordinary double integral.
2. Integrate the $2$-form $\eta = x\,dy\wedge dz$ over the same surface $M$.
3. Reparametrize $M$ by $\psi(u, v) = (v,\ u,\ v^2 - u^2)$ — the same surface with the roles of the parameters swapped — and recompute $\int_M\omega$. Show the answer changes sign, and explain which orientation $\psi$ induces.

**Recall:**

![[Def - Orientation and the Integral of a Form#The Definition]]

To integrate a $2$-form over a parametrized surface: pull the form back along the chart $\varphi$ and integrate over the flat parameter domain, $\int_M\omega = \int_O\varphi^*\omega$, *provided $\varphi$ is orientation-preserving*. The integral is signed — reversing the parametrization's orientation negates it.

![[Def - Pullback of a Differential Form#The Definition]]

The [[Def - Pullback of a Differential Form|pullback]] replaces each $dx_j$ by $dF_j = \sum_\ell(\partial F_j/\partial y_\ell)\,dy_\ell$ and substitutes $F$ into coefficients; wedges are expanded by the [[Def - The Wedge Product|anticommutativity rule]].

---

# Convergent Strategy

**Problem class.** A *direct integration* problem: compute $\int_M\omega$ for an explicit form over an explicit parametrized surface. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy records that every integral over a curved object is reduced to a flat domain by pulling the form back along the chart — that is the only move here.

**Assumption pattern.** The surface is presented as a graph, the cleanest possible parametrization: the parameter domain is literally the unit square, and the chart $\varphi(x,y) = (x, y, f(x,y))$ has the first two components equal to the parameters. The form is a basic $2$-form with a polynomial coefficient.

**Theorem routing.** Pull $\omega$ back: $\varphi^*(z\,dx\wedge dy)$ replaces $z$ by $x^2 - y^2$ and $dx\wedge dy$ by $(\varphi^*dx)\wedge(\varphi^*dy)$. Because $\varphi_1 = x$ and $\varphi_2 = y$, the pullbacks $\varphi^*dx = dx$ and $\varphi^*dy = dy$ are trivial, so $\varphi^*\omega = (x^2-y^2)\,dx\wedge dy$ and the integral is an ordinary double integral. Part 2 is the same recipe but $\eta$ involves $dz$, so $\varphi^*dz$ must be computed and is nontrivial. Part 3 swaps parameters; the transition map has negative Jacobian, flipping the orientation.

**Key decision point.** The subtle point is orientation. Pulling back and integrating gives a *signed* number; whether that number is $\int_M\omega$ or $-\int_M\omega$ depends on whether the chart is orientation-preserving. Part 3 makes this concrete — the swap $\psi(u,v) = (v,u,\ldots)$ has $\det D(\varphi^{-1}\circ\psi) = -1$, so $\psi$ reverses orientation and its integral is the negative.

---

# Legal Operations Used

1. **Pull a form back along a parametrization to reduce an integral to a flat domain** — the core move in all three parts.
2. **Use the determinant identity for wedges** — implicitly, in expanding $(\varphi^*dx)\wedge(\varphi^*dz)$ for part 2.
3. **Choose / track the orientation** — part 3, where the sign of the answer is governed by the orientation the chart induces.

---

# Hints

> [!note]- Hint 1
> For part 1, the graph parametrization $\varphi(x,y) = (x, y, x^2-y^2)$ has first component $x$ and second component $y$, so $\varphi^*dx$ and $\varphi^*dy$ are as simple as possible. What are they? Then $\varphi^*\omega$ is just $(z\circ\varphi)\,dx\wedge dy$.

> [!note]- Hint 2
> For part 2, $\eta = x\,dy\wedge dz$ involves $dz$, and $\varphi_3 = x^2 - y^2$ is not a coordinate. Compute $\varphi^*dz = d(x^2-y^2) = 2x\,dx - 2y\,dy$. Then expand $(\varphi^*dy)\wedge(\varphi^*dz)$ and keep only the $dx\wedge dy$ term — the rest vanishes on a $2$-dimensional domain.

> [!note]- Hint 3
> For part 3, write the transition map $F = \varphi^{-1}\circ\psi$ explicitly: $\psi(u,v) = (v, u, \ldots)$ and $\varphi^{-1}(x,y,z) = (x,y)$, so $F(u,v) = (v, u)$. What is $\det DF$? An orientation-preserving chart has positive Jacobian relative to $\varphi$.

> [!note]- Hint 4
> In part 3 you can either recompute the pullback through $\psi$ directly (you will get $\psi^*\omega = (v^2-u^2)\,du\wedge dv$, integrated over the square) or use the change-of-variables identity $\int_O\psi^*\omega = \int_O(\det DF)\,\varphi^*\omega$. Either way the answer is the negative of part 1.

---

# Solution

Every integral over the surface is a pullback to the unit square followed by an ordinary double integral. The graph parametrization makes the pullbacks of $dx$ and $dy$ trivial; only $dz$ requires work.

**Step 1: $\int_M\omega$ for $\omega = z\,dx\wedge dy$.**

$$\int_M z\,dx\wedge dy = \int_0^1\!\!\int_0^1 (x^2 - y^2)\,dx\,dy = 0.$$

> [!note]- Derivation
> The chart is $\varphi(x,y) = (x, y, x^2-y^2)$, with components $\varphi_1 = x$, $\varphi_2 = y$, $\varphi_3 = x^2-y^2$. Pull back:
> $$\varphi^*dx = d\varphi_1 = dx, \qquad \varphi^*dy = d\varphi_2 = dy,$$
> trivially, because the first two components *are* the parameters. The coefficient $z$ pulls back to $z\circ\varphi = \varphi_3 = x^2 - y^2$. Hence
> $$\varphi^*\omega = (x^2 - y^2)\,(\varphi^*dx)\wedge(\varphi^*dy) = (x^2 - y^2)\,dx\wedge dy.$$
> The integral over $M$ is, by definition, the integral of $\varphi^*\omega$ over the parameter domain (the unit square), with $dx\wedge dy$ read as the positive area element:
> $$\int_M\omega = \int_0^1\!\!\int_0^1(x^2 - y^2)\,dx\,dy.$$
> Compute: $\int_0^1 x^2\,dx = \tfrac13$ and $\int_0^1 y^2\,dy = \tfrac13$, so the double integral is $\int_0^1\tfrac13\,dy - \int_0^1 y^2\,dy = \tfrac13 - \tfrac13 = 0$. By the symmetry $x \leftrightarrow y$ of the square against the antisymmetry of $x^2 - y^2$, the integral is zero.

**Step 2: $\int_M\eta$ for $\eta = x\,dy\wedge dz$.**

$$\int_M x\,dy\wedge dz = \int_0^1\!\!\int_0^1 (-2x^2)\,dx\,dy = -\frac{2}{3}.$$

> [!note]- Derivation
> Now the form involves $dz$, and $\varphi^*dz = d\varphi_3 = d(x^2-y^2) = 2x\,dx - 2y\,dy$ is nontrivial. The coefficient $x$ pulls back to $x$ (since $\varphi_1 = x$). So
> $$\varphi^*\eta = x\,(\varphi^*dy)\wedge(\varphi^*dz) = x\,\big[\,dy\wedge(2x\,dx - 2y\,dy)\,\big].$$
> Expand the wedge, tracking the reorder sign: $dy\wedge(2x\,dx) = 2x\,(dy\wedge dx) = -2x\,(dx\wedge dy)$, and $dy\wedge(2y\,dy) = 0$ (repeated factor). Hence
> $$\varphi^*\eta = x\cdot(-2x)\,dx\wedge dy = -2x^2\,dx\wedge dy.$$
> Integrating over the unit square with $dx\wedge dy$ the positive area element,
> $$\int_M\eta = \int_0^1\!\!\int_0^1(-2x^2)\,dx\,dy = -2\cdot\tfrac13 = -\tfrac23.$$
> The sign is genuine — it comes from the reordering $dy\wedge dx = -dx\wedge dy$. The lesson: when the form involves a non-coordinate differential, the pullback produces reorder signs that must be tracked, and they determine the sign of the flux.

**Step 3: reparametrize by $\psi(u,v) = (v, u, v^2-u^2)$ and recompute.**

$$\psi^*\omega = -\,(v^2-u^2)\,du\wedge dv = -\,F^*(\varphi^*\omega), \qquad \text{since } \det DF = -1.$$

The chart $\psi$ induces the *opposite* orientation; integrating with it computes $-\int_M\omega$.

> [!note]- Derivation
> The transition map is $F = \varphi^{-1}\circ\psi$. Since $\varphi^{-1}(x,y,z) = (x,y)$ and $\psi(u,v) = (v, u, v^2-u^2)$, we get $F(u,v) = (v, u)$. Its Jacobian matrix has rows $(0, 1)$ and $(1, 0)$, so $\det DF = -1 < 0$. Therefore $\psi$ is **orientation-reversing** relative to $\varphi$: it parametrizes $M$ with the *downward* normal, the opposite orientation.
>
> Pull $\omega = z\,dx\wedge dy$ back through $\psi$ directly. The components are $\psi_1 = v$, $\psi_2 = u$, $\psi_3 = v^2-u^2$. So $\psi^*dx = dv$, $\psi^*dy = du$, and the coefficient $z$ pulls back to $\psi_3 = v^2-u^2$. Hence
> $$\psi^*\omega = (v^2-u^2)\,(dv)\wedge(du) = (v^2-u^2)\,dv\wedge du = -(v^2-u^2)\,du\wedge dv.$$
> The reorder $dv\wedge du = -du\wedge dv$ produces the crucial minus sign. Integrating over the unit square in $(u,v)$, with $du\wedge dv$ the positive area element:
> $$\int_O\psi^*\omega = \int_0^1\!\!\int_0^1 -(v^2-u^2)\,du\,dv = -\Big(\int_0^1 v^2\,dv - \tfrac13\Big) = -(\tfrac13 - \tfrac13) = 0.$$
> Here the answer is again $0$ — but only because the integrand of part 1 was itself antisymmetric and integrated to zero. The *signed* relationship is the point: $\int_O\psi^*\omega = -\int_O\varphi^*\omega$ as forms, because $\psi^*\omega = (\det DF)\,F^*(\varphi^*\omega)$ with $\det DF = -1$. Had the part-1 integrand been a nonzero number $I$, part 3 would give $-I$. The orientation $\psi$ induces is the reverse of $\varphi$'s; integrating with it computes $-\int_M\omega$, not $\int_M\omega$.
>
> *The takeaway is structural, not numerical:* swapping two parameters has negative Jacobian, hence reverses orientation, hence negates the integral of every $2$-form. The vanishing in this particular example masks the sign flip; choose a form whose part-1 integral is nonzero (say $\omega' = (z+1)\,dx\wedge dy$, with $\int_M\omega' = 1$) and part 3 returns $-1$.

> [!note]- Complete formal solution
> **Part 1.** $\varphi(x,y) = (x,y,x^2-y^2)$, so $\varphi^*\omega = \varphi^*(z\,dx\wedge dy) = (x^2-y^2)\,dx\wedge dy$. Thus $\int_M\omega = \int_0^1\!\!\int_0^1(x^2-y^2)\,dx\,dy = \tfrac13 - \tfrac13 = 0$.
>
> **Part 2.** $\varphi^*dz = 2x\,dx - 2y\,dy$, so $\varphi^*\eta = x\,dy\wedge(2x\,dx-2y\,dy) = -2x^2\,dx\wedge dy$. Thus $\int_M\eta = \int_0^1\!\!\int_0^1(-2x^2)\,dx\,dy = -\tfrac23$.
>
> **Part 3.** The transition map $F = \varphi^{-1}\circ\psi$ is $F(u,v) = (v,u)$ with $\det DF = -1$, so $\psi$ reverses orientation. Directly, $\psi^*\omega = (v^2-u^2)\,dv\wedge du = -(v^2-u^2)\,du\wedge dv$, and $\int_O\psi^*\omega = -(\tfrac13-\tfrac13) = 0$. In general $\int_O\psi^*\omega = -\int_O\varphi^*\omega$; the common value $0$ here is an accident of this antisymmetric integrand. $\blacksquare$

---

# Key Takeaways

**A graph parametrization is the easiest possible chart, because two of the three pullbacks are trivial.** When a surface is presented as a graph $z = f(x,y)$, the chart $\varphi(x,y) = (x, y, f(x,y))$ has its first two components equal to the parameters, so $\varphi^*dx = dx$ and $\varphi^*dy = dy$ cost nothing — the only nontrivial pullback is $\varphi^*dz = df = f_x\,dx + f_y\,dy$. This is why, given a choice of how to parametrize a surface, a graph chart should always be preferred: it concentrates all the work into the single differential $dz$. The same principle scales: an $(n-1)$-surface in $\mathbb{R}^n$ presented as a graph $x_n = u(x')$ has all the pullback work concentrated in $\varphi^*dx_n = du$, which is exactly the structure exploited in the direct proof of the [[Thm - The Divergence Theorem|divergence theorem]].

**The integral of a form is signed, and the sign is the orientation — never report a magnitude without checking it.** Part 3 is the warning made concrete: the *same surface*, integrated against the *same form*, gives $+I$ or $-I$ depending on the parametrization, because swapping two parameters has negative Jacobian and reverses the induced orientation. A reparametrization with $\det DF > 0$ leaves the integral unchanged; one with $\det DF < 0$ negates it. The reliable discipline before reporting $\int_M\omega$: identify which orientation the surface carries (often "upward normal" or "outward normal"), check that the chart used is orientation-preserving for that choice (compute the Jacobian sign), and only then trust the sign of the answer. A correct magnitude with a wrong sign is a wrong flux — and in physics a wrong sign is the difference between charge flowing in and charge flowing out.

**When a basic $2$-form involves a non-coordinate differential, the reorder signs are where errors hide.** Part 1 was sign-free because $dx$ and $dy$ pulled back to themselves; part 2 was not, because $\varphi^*dz = 2x\,dx - 2y\,dy$ wedged against $dy$ produced $dy\wedge dx$, which must be reordered to $-dx\wedge dy$. Every flux integral of a form containing $dz$ (or any differential of a non-parameter coordinate) generates such reorderings, and the single most common computational error in the subject is dropping one of these signs. The discipline: after pulling back and before integrating, reduce every basic $2$-form to the *positive* increasing-index form $dx\wedge dy$ (or $du\wedge dv$), attaching the reorder sign, and only then read off the integrand. This is the same sign discipline as in [[Ex - Computing wedge products and exterior derivatives]], now carrying real consequences for the value of a flux.
