---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Caratheodory's Principle (Inaccessibility)"
  - "Def - Adiabatic Process and Adiabatic Distribution"
  - "Thm - Caratheodory's Theorem on the Second Law"
  - "Thm - Chow's Connectivity Theorem (Statement)"
  - "Def - Closed and Exact Forms"
tags: [physics, thermodynamics, differential-geometry, contact-geometry]
---

# Problem Statement

Take the 1-form on $\mathbb{R}^3$ (with coordinates $(x, y, z)$):

$$\theta = y\, dx - x\, dy + dz.$$

This is Frankel's example (and the standard *contact* 1-form on $\mathbb{R}^3$). Treat it as a hypothetical "heat 1-form" $\delta Q$ for a fictitious thermodynamic system with 3-dimensional state space.

1. Compute $d\theta$ and the Frobenius obstruction $\theta \wedge d\theta$. Verify $\theta \wedge d\theta \neq 0$ at every point.
2. Conclude that $\theta$ does **not** admit any local integrating factor — there is no smooth function $S$ and nonzero $\lambda$ with $\theta = \lambda\, dS$ locally.
3. Verify directly via Chow's theorem (in concrete form) that every point of $\mathbb{R}^3$ is reachable from the origin by a sequence of piecewise smooth paths tangent to $\ker \theta$. Construct, in particular, a horizontal path from $(0, 0, 0)$ to $(0, 0, \epsilon)$ for arbitrary small $\epsilon > 0$ — a displacement in the "vertical" direction $\partial_z$, which is not in $\ker \theta$ at the origin.
4. Conclude that a "thermodynamic system" with this $\delta Q$ would violate Caratheodory's principle (every nearby state is adiabatically accessible) and admit no entropy function.

**Recall:**

[[Def - Caratheodory's Principle (Inaccessibility)|Caratheodory's principle]]: in every neighbourhood of every equilibrium state, there exist states not adiabatically accessible from the original.

[[Thm - Caratheodory's Theorem on the Second Law|Caratheodory's theorem]]: Caratheodory's principle for a smooth nowhere-vanishing 1-form $\theta$ implies $\theta \wedge d\theta = 0$ globally.

The [[Thm - Chow's Connectivity Theorem (Statement)|contrapositive of Chow's theorem]]: if a smooth codimension-one distribution $\ker \theta$ is non-involutive at $x_0$ (equivalently $\theta \wedge d\theta \neq 0$ at $x_0$), then there is an open neighbourhood of $x_0$ in which every point is reachable from $x_0$ by a piecewise smooth $\theta$-horizontal path.

A 1-form $\theta$ admits an integrating factor $\lambda$ on an open $V$ iff $\theta \wedge d\theta = 0$ on $V$ — see [[Thm - Existence of Integrating Factor for an Inaccessible Pfaffian]].

---

# Convergent Strategy

**Problem class:** This is a counterexample-construction problem demonstrating that Caratheodory's theorem is *not vacuous* — there exist nowhere-vanishing 1-forms on 3-manifolds for which the Frobenius obstruction $\theta \wedge d\theta$ is nonzero everywhere, and for these no entropy exists. The recurring pattern is: (i) write down a candidate 1-form; (ii) compute $\theta \wedge d\theta$ and check whether it vanishes; (iii) if it does not vanish, verify horizontal connectivity directly to confirm the contrapositive of Chow.

**Assumption pattern:** Frankel's 1-form $\theta = y\, dx - x\, dy + dz$ is chosen because it is the simplest non-trivial example: written with three linear functions of the coordinates so the computation of $d\theta$ is elementary, but with a "rotational" structure ($y\, dx - x\, dy$) that produces a non-zero $d\theta$ in the $dx \wedge dy$ direction. The form is nowhere zero (the $dz$ component is always 1). It is in fact the standard *contact form* on $\mathbb{R}^3$ in cylindrical-style coordinates, and the underlying distribution is the **standard contact structure** of differential geometry.

**Theorem routing:** Direct algebraic computation of $\theta \wedge d\theta$ shows it is nonzero everywhere. By the [[Thm - Existence of Integrating Factor for an Inaccessible Pfaffian|integrating-factor theorem]] (the equivalence chain), no integrating factor exists locally. By the contrapositive of [[Thm - Chow's Connectivity Theorem (Statement)|Chow's theorem]], horizontal connectivity holds locally — confirmed by explicit construction of horizontal paths between non-adjacent points. By [[Def - Caratheodory's Principle (Inaccessibility)|Caratheodory's principle]], adiabatic accessibility everywhere means the principle is violated.

**Key decision point:** The non-obvious choice is the *explicit construction* of horizontal paths in Step 3. The path from $(0,0,0)$ to $(0,0,\epsilon)$ must move in $\ker \theta$ at every instant (where $\theta(\dot\gamma) = 0$), yet net-displace in the $\partial_z$ direction (transverse to $\ker \theta$ at the origin, where $\theta = dz$). The trick is to traverse a small closed loop in the $(x, y)$-plane: as you go around the loop, $\theta(\dot\gamma) = 0$ if you compensate the $y\,dx - x\,dy$ contribution with a small $z$-displacement, and the net $z$-displacement around the loop is the *area* enclosed in the $(x,y)$-plane. This is the commutator-flow construction made fully explicit.

---

# Legal Operations Used

1. **Operation 2 from the topic page (compute the Frobenius obstruction).** Compute $d\theta$ in coordinates, wedge with $\theta$, simplify, observe non-vanishing.

2. **Operation 9 from the topic page (use Chow's theorem to convert non-involutivity into horizontal connectivity).** Once non-involutivity is established, explicitly construct horizontal paths reaching arbitrary nearby points — verifying directly that Caratheodory's principle would fail.

3. **Operation 8 from the topic page (test exactness).** Verify $\theta$ is not closed by computing $d\theta \neq 0$, and not exact (a fortiori). Verify that no integrating factor exists by the equivalence to $\theta \wedge d\theta = 0$.

---

# Hints

> [!note]- Hint 1
> Compute $d\theta$ component by component: $d(y\, dx) = dy \wedge dx = -dx \wedge dy$, $d(-x\, dy) = -dx \wedge dy$, $d(dz) = 0$. Sum: $d\theta = -2\, dx \wedge dy$.

> [!note]- Hint 2
> Compute $\theta \wedge d\theta = (y\, dx - x\, dy + dz) \wedge (-2\, dx \wedge dy)$. The terms $y\, dx \wedge dx \wedge dy = 0$ and $-x\, dy \wedge dx \wedge dy = 0$ (repeated $dx, dy$). The only surviving term is $dz \wedge (-2\, dx \wedge dy) = -2\, dz \wedge dx \wedge dy = -2\, dx \wedge dy \wedge dz$.

> [!note]- Hint 3
> For the horizontal path: take a small circle of radius $r$ in the $(x, y)$-plane, parametrised as $(x(t), y(t)) = (r \cos t, r \sin t)$ for $t \in [0, 2\pi]$. To make the path horizontal ($\theta(\dot\gamma) = 0$), choose $z(t)$ so that $y\dot x - x\dot y + \dot z = 0$. Compute $y\dot x - x\dot y = (r \sin t)(-r \sin t) - (r \cos t)(r \cos t) = -r^2$. So $\dot z = r^2$, and $z(t) = r^2 t$. After going all the way around ($t = 0 \to 2\pi$), $z(2\pi) - z(0) = 2\pi r^2$ — the *area enclosed in the $(x,y)$-plane*.

> [!note]- Hint 4
> So a small loop in the $(x, y)$-plane produces a net vertical displacement $2\pi r^2$ — and by choosing $r$ small (so the loop is small), the displacement can be any positive value, including $\epsilon$. To reach $(0, 0, \epsilon)$ from $(0, 0, 0)$, traverse a circle of radius $r = \sqrt{\epsilon/(2\pi)}$. The construction is *exactly* the commutator-flow displacement in disguise.

---

# Solution

The proof breaks into four steps. Step 1 computes the Frobenius obstruction by direct algebra. Step 2 concludes via the integrating-factor theorem that no entropy exists. Step 3 constructs an explicit horizontal path producing vertical displacement, demonstrating horizontal connectivity. Step 4 wraps up by interpreting the result as a violation of Caratheodory's principle. The non-obvious move is in Step 3, where the horizontal path is a small circle in the $(x,y)$-plane lifted into a helix in $\mathbb{R}^3$, with the lift chosen so that $\theta(\dot\gamma) = 0$ — and the net $z$-displacement equals $2\pi$ times the enclosed area.

**Step 1: $\theta \wedge d\theta = -2\, dx \wedge dy \wedge dz \neq 0$ everywhere on $\mathbb{R}^3$.**

> [!note]- Derivation
> Compute $d\theta$ by applying $d$ to each term of $\theta = y\, dx - x\, dy + dz$:
> $$d(y\, dx) = dy \wedge dx + y\, d(dx) = dy \wedge dx = -dx \wedge dy.$$
> $$d(-x\, dy) = -dx \wedge dy + (-x)\, d(dy) = -dx \wedge dy.$$
> $$d(dz) = 0.$$
> Sum:
> $$d\theta = -dx \wedge dy - dx \wedge dy = -2\, dx \wedge dy.$$
>
> Now $\theta \wedge d\theta = (y\, dx - x\, dy + dz) \wedge (-2\, dx \wedge dy)$:
> $$= -2 y\, dx \wedge dx \wedge dy + 2x\, dy \wedge dx \wedge dy - 2\, dz \wedge dx \wedge dy.$$
> The first two terms vanish (repeated $dx \wedge dx$ and $dy \wedge dy$ inside the triple wedge). The third is
> $$-2\, dz \wedge dx \wedge dy = -2\, dx \wedge dy \wedge dz \neq 0$$
> (after cyclic reordering). So $\theta \wedge d\theta = -2\, dx \wedge dy \wedge dz$, a nowhere-zero 3-form on $\mathbb{R}^3$.

**Step 2: $\theta$ admits no local integrating factor.**

> [!note]- Derivation
> By [[Thm - Existence of Integrating Factor for an Inaccessible Pfaffian|the integrating-factor theorem]], $\theta = \lambda\, dS$ locally iff $\theta \wedge d\theta = 0$ identically. Here $\theta \wedge d\theta = -2\, dx \wedge dy \wedge dz \neq 0$ everywhere, so there is *no* open set on which $\theta = \lambda\, dS$ for any smooth nonzero $\lambda$ and smooth $S$.
>
> Equivalently, the distribution $\ker \theta$ is non-involutive at every point: there is no foliation of $\mathbb{R}^3$ by surfaces tangent to $\ker \theta$, so no "adiabatic surfaces" exist, so no entropy function $S$ has level sets matching the horizontal directions.

**Step 3: Explicit construction of a horizontal path from $(0,0,0)$ to $(0,0,\epsilon)$.**

> [!note]- Derivation
> Consider the curve parametrised by $t \in [0, 2\pi]$:
> $$\gamma(t) = (r \cos t, r \sin t, z(t))$$
> for some $r > 0$ (to be chosen) and $z(t)$ to be determined.
>
> Compute the tangent vector $\dot\gamma(t) = (-r \sin t, r \cos t, \dot z(t))$.
>
> Evaluate $\theta(\dot\gamma)$:
> $$\theta(\dot\gamma) = y \dot x - x \dot y + \dot z = (r \sin t)(-r \sin t) - (r \cos t)(r \cos t) + \dot z = -r^2 \sin^2 t - r^2 \cos^2 t + \dot z = -r^2 + \dot z.$$
> For $\gamma$ to be horizontal ($\theta(\dot\gamma) = 0$), we need $\dot z = r^2$, hence $z(t) = r^2 t + z(0) = r^2 t$ (taking $z(0) = 0$).
>
> So the horizontal path from $(0, 0, 0)$ is
> $$\gamma(t) = (r \cos t, r \sin t, r^2 t), \quad t \in [0, 2\pi].$$
> But wait: at $t = 0$, $\gamma(0) = (r, 0, 0)$, not $(0, 0, 0)$. So we need to also include a horizontal path from the origin to $(r, 0, 0)$ — but this is easy: along the $x$-axis with $y = 0, z = 0$, $\theta = -x\, dy + dz$, and the tangent $\dot x \partial_x$ gives $\theta(\dot\gamma) = 0$ trivially (since $\dot y = 0$ and $\dot z = 0$). So a straight-line motion along $x$ from $(0,0,0)$ to $(r, 0, 0)$ is horizontal.
>
> Concatenate: (i) move from $(0,0,0)$ to $(r, 0, 0)$ along the $x$-axis; (ii) traverse the helix $\gamma(t) = (r \cos t, r \sin t, r^2 t)$ for $t \in [0, 2\pi]$, ending at $(r, 0, 2\pi r^2)$; (iii) move from $(r, 0, 2\pi r^2)$ to $(0, 0, 2\pi r^2)$ along the $x$-axis (with $y = 0$, $z$ fixed at $2\pi r^2$; check $\theta(\dot\gamma) = 0$ since $\dot y = \dot z = 0$).
>
> Net displacement: $(0, 0, 2\pi r^2)$. Choosing $r = \sqrt{\epsilon/(2\pi)}$ gives net displacement $(0, 0, \epsilon)$. So the origin and $(0, 0, \epsilon)$ are connected by a piecewise smooth horizontal path for any $\epsilon > 0$.

**Step 4: Violation of Caratheodory's principle.**

> [!note]- Derivation
> The point $(0, 0, \epsilon)$ is arbitrarily close to the origin (for small $\epsilon$), and by Step 3 it is reachable from the origin by a horizontal path. The same construction with negative $r$ (running the loop the other way) gives net displacement $(0, 0, -\epsilon)$ — so the origin can reach states "below" itself as well. By varying the loop's centre and shape, *every* nearby point in $\mathbb{R}^3$ is horizontally reachable.
>
> If this were a thermodynamic system with $\delta Q = \theta$, then *every* nearby state would be adiabatically accessible from the origin — there would be no inaccessible states in any neighbourhood. This *violates* [[Def - Caratheodory's Principle (Inaccessibility)|Caratheodory's principle]], hence the system would violate the second law of thermodynamics. Equivalently, no global entropy function $S$ could exist for this $\delta Q$, because adiabatic accessibility being transitive across all of $\mathbb{R}^3$ would force $S$ to be constant — but then $\delta Q = T\, dS$ would force $\delta Q = 0$, contradicting $\delta Q \neq 0$.
>
> This is the concrete content of the Caratheodory–Frobenius theorem in negative form: a real physical system, governed by the second law, cannot have $\delta Q = y\, dx - x\, dy + dz$ as its heat 1-form. The geometry of $\delta Q$ in nature is integrable; the geometry of Frankel's contact form is not.

> [!note]- Complete formal solution
> *Step 1:* $\theta = y\, dx - x\, dy + dz$ on $\mathbb{R}^3$. Compute $d\theta = dy \wedge dx - dx \wedge dy = -2\, dx \wedge dy$. Then
> $$\theta \wedge d\theta = (y\, dx - x\, dy + dz) \wedge (-2\, dx \wedge dy) = -2\, dz \wedge dx \wedge dy = -2\, dx \wedge dy \wedge dz \neq 0.$$
>
> *Step 2:* By [[Thm - Existence of Integrating Factor for an Inaccessible Pfaffian|the integrating-factor theorem]], the non-vanishing $\theta \wedge d\theta$ means $\theta$ admits no local integrating factor — no $(\lambda, S)$ with $\theta = \lambda\, dS$ on any open set.
>
> *Step 3:* Construct explicit horizontal path from $(0,0,0)$ to $(0, 0, \epsilon)$:
> 1. Straight-line in $\partial_x$ from $(0,0,0)$ to $(r, 0, 0)$ — horizontal since $\theta(\dot x \partial_x) = y \cdot \dot x = 0$ at $y = 0$.
> 2. Helix $\gamma(t) = (r \cos t, r \sin t, r^2 t)$ for $t \in [0, 2\pi]$: $\theta(\dot \gamma) = -r^2 + r^2 = 0$ by construction. Endpoint: $(r, 0, 2\pi r^2)$.
> 3. Straight-line in $-\partial_x$ from $(r, 0, 2\pi r^2)$ to $(0, 0, 2\pi r^2)$ — horizontal as in step 1.
> Net displacement: $(0, 0, 2\pi r^2)$. Choose $r = \sqrt{\epsilon/(2\pi)}$ to achieve $(0, 0, \epsilon)$.
>
> *Step 4:* Every nearby point of the origin is horizontally accessible. Caratheodory's principle would assert otherwise. Hence this $\theta$ cannot be a physical heat 1-form: no integrating factor, no entropy, second-law violation.

> [!warning] Illegal but tempting alternative: claiming the helix is "not a real path"
> One might object that the helix is a closed curve in $(x, y)$ projected back to the same starting position, hence not a "real" thermodynamic process. This objection misses the point: the *path in $\mathbb{R}^3$* is not closed — it ends at $(r, 0, 2\pi r^2)$, displaced in $z$ from $(r, 0, 0)$. The projection to $(x, y)$ happens to be closed, but the lift to $\mathbb{R}^3$ is not, because the constraint $\theta(\dot\gamma) = 0$ forces a vertical drift proportional to the projected area swept out. This drift is exactly the **holonomy** of the connection associated to $\theta$, and it is the geometric mechanism behind the Aharonov-Bohm effect, the Berry phase, and other physical instances of non-integrability.

---

# Key Takeaways

**The Frobenius obstruction $\theta \wedge d\theta$ is the algebraic test for integrability.** Whenever you face a 1-form on a manifold of dimension $\geq 3$ and want to know if it admits an integrating factor, compute $\theta \wedge d\theta$. If it vanishes identically, an integrating factor exists locally; if it is nonzero anywhere, no local integrating factor exists at that point. The computation is mechanical: $d\theta$ from the coefficients of $\theta$, then wedge with $\theta$. For 2-dimensional manifolds the obstruction is automatically zero (it is a 3-form on a 2-manifold); for $\geq 3$ dimensions it is a genuine constraint. This is the trigger-reaction pattern: "want to know if $\theta$ admits an integrating factor → compute $\theta \wedge d\theta$".

**Horizontal connectivity in the absence of integrability is via "commutator-flow" loops.** The mechanism by which horizontal paths can drift transversely to the distribution is the commutator-flow: composing flows of two non-commuting horizontal vector fields in a closed loop produces displacement in the bracket direction. In Frankel's example, the bracket of $\partial_x + y \partial_z$ and $\partial_y - x \partial_z$ (two vector fields in $\ker \theta$ near the origin) is computed via the formula and gives $-2 \partial_z$ — transverse to $\ker \theta|_0 = \mathrm{span}(\partial_x, \partial_y)$. The explicit helix in Step 3 *realises* this commutator flow concretely: the small circle in $(x, y)$ is the flow loop, and the $z$-drift is the bracket displacement. This is the geometric heart of why Caratheodory's theorem works in the contrapositive direction.

**The standard contact form $\theta = y\, dx - x\, dy + dz$ is the "anti-Caratheodory" example.** It is the simplest 3-dimensional 1-form for which integrability *maximally* fails: its non-integrability is uniform (the obstruction is nonzero everywhere) and gives full horizontal connectivity. This is the prototypical **contact structure** of contact geometry, and the Heisenberg-group structure it carries is foundational to sub-Riemannian geometry. Recognising this form as the standard counterexample helps when encountering similar 1-forms in other contexts: any 1-form with the algebraic structure "rotational pair plus extra coordinate" is likely non-integrable, and the integrability check $\theta \wedge d\theta$ tells you for sure.

**The physical conclusion: real thermodynamic systems have integrable $\delta Q$, by physical fiat.** Frankel's example is a *mathematical* 1-form, not a physical heat form. The fact that integrability fails for it is not a flaw in nature but a constraint on what physical heat forms can look like: the second law (Caratheodory's principle) requires integrability, and this restricts the algebraic form of $\delta Q$ to a special subset of all possible 1-forms. The existence of entropy is, geometrically, the assertion that $\delta Q$ lies in this special integrable subset. Frankel's counterexample shows that *most* 1-forms are not in the subset — the second law is a substantive constraint, not a tautology. This sharpens the meaning of "second law of thermodynamics": it is the assertion that nature selects integrable 1-forms for the heat exchange of real systems.

**Companion exercises:** [[Ex - The Heat 1-Form for an Ideal Gas]] computes a physical $\delta Q$ and shows it *does* admit an integrating factor — the converse of the present exercise's counterexample. Together they illustrate the two sides of Caratheodory's theorem: real systems satisfy it (entropy exists), and artificial systems can violate it (entropy does not exist). The exercise `Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form` in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]] does the same computation in the differential-geometric setting without thermodynamic interpretation.
