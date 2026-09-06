---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Smooth Vector Field"
  - "Def - Flow of a Vector Field"
  - "Thm - Commuting Flows Theorem"
tags: [geometry, differential-geometry]
---

# Problem Statement

On $\mathbb{R}^2$, define the smooth vector fields

$$X = \frac{\partial}{\partial x}, \qquad Y = x \frac{\partial}{\partial y}.$$

(a) Compute $[X, Y]$ using the coordinate formula.

(b) Find the flows $\phi^X$ and $\phi^Y$ of $X$ and $Y$ explicitly.

(c) Verify that $\phi^X$ and $\phi^Y$ do not commute, i.e. find $s, t \in \mathbb{R}$ and $p \in \mathbb{R}^2$ with $\phi^X_s \phi^Y_t(p) \neq \phi^Y_t \phi^X_s(p)$.

(d) Confirm consistency with the [[Thm - Commuting Flows Theorem]].

**Recall:**

![[Def - The Lie Bracket of Vector Fields#The Definition]]

[[Thm - Commuting Flows Theorem]]: For smooth $X, Y \in \mathfrak{X}(M)$, the following are equivalent: (i) $[X, Y] = 0$; (ii) flows of $X, Y$ commute on overlapping domains.

The flow $\phi^X_t(p)$ is the integral curve of $X$ starting at $p$, evaluated at time $t$. The flow domain may be a strict subset of $\mathbb{R} \times M$.

---

# Convergent Strategy

**Problem class:** A computational exercise illustrating the [[Thm - Commuting Flows Theorem]]. The bracket is computed, the flows are computed, and the non-commutation is verified directly. The class is "calibration check for the commuting-flows-iff-bracket-vanishes equivalence".

**Assumption pattern:** Two vector fields are given in explicit coordinate form on $\mathbb{R}^2$ (so the standard chart, the coordinate vector fields are simply $\partial_x, \partial_y$). The ODEs for the integral curves are straightforward — $X = \partial_x$ has translational integral curves, $Y = x \partial_y$ has integral curves parametrised by $x$.

**Theorem routing:** [[Def - The Lie Bracket of Vector Fields|Lie bracket coordinate formula]] gives $[X, Y]$ in one line. Solving the integral-curve ODEs gives the flows. Composing the flows in both orders shows non-commutation. The [[Thm - Commuting Flows Theorem]] then closes the loop: bracket nonzero ⟹ flows do not commute.

**Key decision point:** The vector field $Y = x \partial_y$ has a position-dependent coefficient — the speed of vertical motion depends on the horizontal position. This dependence is what creates the non-commutation: flowing horizontally first changes $x$, which changes the speed of the subsequent vertical motion. The mental picture is "shear" — flowing along $Y$ shifts horizontal lines vertically by an amount that depends on $x$. The bracket measures the rate at which this shear is generated.

---

# Legal Operations Used

1. **Operation 5 from the topic page (compute a Lie bracket coordinatewise).** Apply the coordinate formula to $X = \partial_x$, $Y = x \partial_y$.

2. **Operation 1 from the topic page (reduce a global problem to a chart).** $\mathbb{R}^2$ is its own chart.

3. **Operation 2 from the topic page (invoke Picard–Lindelöf).** Solve the integral-curve ODEs $\dot\gamma^i = X^i(\gamma)$ and $\dot\gamma^i = Y^i(\gamma)$.

4. **Operation 8 from the topic page (use $[X, Y] = 0$ to commute flows; or its contrapositive).** Since the bracket is nonzero, the flows do not commute.

---

# Hints

> [!note]- Hint 1
> For (a): apply the coordinate formula $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ with $X^1 = 1, X^2 = 0$ and $Y^1 = 0, Y^2 = x$. Most terms vanish because $X^i$ are constants.

> [!note]- Hint 2
> For (b) flow of $X = \partial_x$: the ODE is $\dot x = 1, \dot y = 0$, so $\phi^X_s(x_0, y_0) = (x_0 + s, y_0)$ — horizontal translation. Flow of $Y = x \partial_y$: the ODE is $\dot x = 0, \dot y = x$, so $\phi^Y_t(x_0, y_0) = (x_0, y_0 + t x_0)$ — vertical shift by $t x_0$ (preserving $x$, shifting $y$ by $t$ times the *fixed* $x$-value).

> [!note]- Hint 3
> For (c): compute $\phi^X_s \phi^Y_t (x_0, y_0)$ and $\phi^Y_t \phi^X_s (x_0, y_0)$ separately. The first applies $\phi^Y_t$ to $(x_0, y_0)$ getting $(x_0, y_0 + tx_0)$, then applies $\phi^X_s$ getting $(x_0 + s, y_0 + tx_0)$. The second applies $\phi^X_s$ first to get $(x_0 + s, y_0)$, then $\phi^Y_t$ to get $(x_0 + s, y_0 + t(x_0 + s))$. The $y$-coordinates differ by $ts$.

---

# Solution

The proof has four steps corresponding to (a)–(d). Plan: compute the bracket (one line), find the flows (solve two ODEs), compute the composition in both orders (algebra), and check the difference equals the bracket times $s t$ to leading order (verifying the [[Thm - Commuting Flows Theorem|Commuting Flows Theorem]] geometrically).

**Step 1 (a): Compute $[X, Y]$.**

$X^1 = 1, X^2 = 0$ (constants); $Y^1 = 0, Y^2 = x$. Coordinate formula:
- $[X, Y]^1 = X^i \partial_i Y^1 - Y^i \partial_i X^1 = 0 - 0 = 0$ (both terms zero: $Y^1 = 0$ has zero derivative, $X^1 = 1$ has zero derivative).
- $[X, Y]^2 = X^i \partial_i Y^2 - Y^i \partial_i X^2 = (1) \partial_x x + 0 - 0 = 1$.

So $[X, Y] = \partial/\partial y \neq 0$ — the bracket is nonzero everywhere.

> [!note]- Derivation (Step 1)
> $X = \partial_x$ has components $X^1 = 1, X^2 = 0$ — both constants, so all partial derivatives of $X^k$ are zero.
>
> $Y = x \partial_y$ has components $Y^1 = 0$ (constant, partials zero) and $Y^2 = x$ (depends on $x$, $\partial_x Y^2 = 1$, $\partial_y Y^2 = 0$).
>
> Coordinate formula:
> - $[X, Y]^1 = X^i \partial_i Y^1 - Y^i \partial_i X^1$. $Y^1 = 0$ has zero partials, so $X^i \partial_i Y^1 = 0$. $X^1 = 1, X^2 = 0$ both constants, so $Y^i \partial_i X^1 = 0$. Hence $[X, Y]^1 = 0$.
> - $[X, Y]^2 = X^i \partial_i Y^2 - Y^i \partial_i X^2$. $Y^2 = x$, so $X^i \partial_i Y^2 = X^1 \cdot 1 + X^2 \cdot 0 = 1$. $X^2 = 0$ is constant, so $Y^i \partial_i X^2 = 0$. Hence $[X, Y]^2 = 1$.
>
> So $[X, Y] = 0 \cdot \partial_x + 1 \cdot \partial_y = \partial/\partial y$.

**Step 2 (b): Compute the flows.**

For $X = \partial_x$: $\dot x = 1, \dot y = 0$, so starting at $(x_0, y_0)$, the integral curve is $(x_0 + s, y_0)$. Hence $\phi^X_s(x, y) = (x + s, y)$.

For $Y = x \partial_y$: $\dot x = 0, \dot y = x$. Starting at $(x_0, y_0)$, $x(t) = x_0$ (constant) and $y(t) = y_0 + x_0 t$, so $\phi^Y_t(x, y) = (x, y + tx)$.

Both flows are global ($\mathcal{D} = \mathbb{R} \times \mathbb{R}^2$ for each), since the integral curves are defined for all $t$.

> [!note]- Derivation (Step 2)
> *Flow of $X = \partial_x$.* ODE: $\dot \gamma^1(t) = 1, \dot \gamma^2(t) = 0$ with $\gamma(0) = (x_0, y_0)$. Integrate: $\gamma^1(t) = x_0 + t, \gamma^2(t) = y_0$. So $\phi^X_t(x_0, y_0) = (x_0 + t, y_0)$ — translation in the $x$-direction by $t$. Defined for all $t$; global flow.
>
> *Flow of $Y = x \partial_y$.* ODE: $\dot \gamma^1(t) = 0, \dot \gamma^2(t) = \gamma^1(t)$ with $\gamma(0) = (x_0, y_0)$. From the first equation, $\gamma^1(t) = x_0$ (constant). Substituting into the second: $\dot \gamma^2 = x_0$, so $\gamma^2(t) = y_0 + t x_0$. Hence $\phi^Y_t(x_0, y_0) = (x_0, y_0 + t x_0)$ — vertical shift by $t x_0$, with the $x$-coordinate preserved. Defined for all $t$; global flow.

**Step 3 (c): Verify non-commutation.**

Compute $\phi^X_s \phi^Y_t(x_0, y_0)$ and $\phi^Y_t \phi^X_s(x_0, y_0)$:

- $\phi^Y_t(x_0, y_0) = (x_0, y_0 + t x_0)$. Then $\phi^X_s(x_0, y_0 + t x_0) = (x_0 + s, y_0 + t x_0)$.
- $\phi^X_s(x_0, y_0) = (x_0 + s, y_0)$. Then $\phi^Y_t(x_0 + s, y_0) = (x_0 + s, y_0 + t(x_0 + s)) = (x_0 + s, y_0 + t x_0 + ts)$.

Comparing $y$-coordinates: the first composition gives $y_0 + t x_0$, the second gives $y_0 + t x_0 + ts$. They differ by $ts$. So the flows do not commute (take any $s, t \neq 0$ and any starting point $(x_0, y_0)$).

> [!note]- Derivation (Step 3)
> Compute the two compositions starting from $(x_0, y_0)$:
>
> **Order 1: $\phi^X_s \circ \phi^Y_t$.** Apply $\phi^Y_t$ first: $(x_0, y_0) \mapsto (x_0, y_0 + t x_0)$. Then $\phi^X_s$: $(x_0, y_0 + t x_0) \mapsto (x_0 + s, y_0 + t x_0)$.
>
> **Order 2: $\phi^Y_t \circ \phi^X_s$.** Apply $\phi^X_s$ first: $(x_0, y_0) \mapsto (x_0 + s, y_0)$. Then $\phi^Y_t$: $(x_0 + s, y_0) \mapsto (x_0 + s, y_0 + t(x_0 + s)) = (x_0 + s, y_0 + t x_0 + ts)$.
>
> The two results agree in the $x$-coordinate but differ in the $y$-coordinate by $ts$:
> $$\phi^Y_t \phi^X_s(x_0, y_0) - \phi^X_s \phi^Y_t(x_0, y_0) = (0, ts).$$
>
> For any nonzero $s, t$ the flows do not commute.

**Step 4 (d): Consistency with the Commuting Flows Theorem.**

The [[Thm - Commuting Flows Theorem]] says flows commute iff bracket vanishes. We computed $[X, Y] = \partial_y \neq 0$ in Step 1, so the theorem predicts non-commutation. Step 3 verified this directly. To leading order in $(s, t)$, the discrepancy between the two compositions is $(0, ts) = ts \cdot \partial_y \big|_p = ts \cdot [X, Y]_p$ — the bracket times $st$. This is the geometric content: the bracket *measures* the discrepancy of the parallelogram closure.

> [!note]- Derivation (Step 4)
> From Step 3, $\phi^Y_t \phi^X_s(p) - \phi^X_s \phi^Y_t(p) = (0, ts) \in \mathbb{R}^2$.
>
> Interpret this in $T_p \mathbb{R}^2 \cong \mathbb{R}^2$: the vector $(0, ts) = ts \cdot (0, 1) = ts \cdot \partial_y|_p = ts \cdot [X, Y]_p$.
>
> In this affine example the coordinate difference between the two ordered compositions is exactly $st\,\partial_y$. In general, after choosing a chart and fixing an order convention, the difference has leading mixed term $st[X,Y]_p$ and remainder $O(|s|^2|t|+|s||t|^2)$. Thus bracket vanishing removes the mixed second-order term.

> [!note]- Complete formal solution
> **(a)** With $X = \partial_x$ ($X^1 = 1, X^2 = 0$) and $Y = x \partial_y$ ($Y^1 = 0, Y^2 = x$), the coordinate formula gives $[X, Y]^1 = 0 - 0 = 0$ and $[X, Y]^2 = X^1 \partial_x Y^2 + X^2 \partial_y Y^2 - 0 = 1 \cdot 1 + 0 = 1$. So $[X, Y] = \partial/\partial y \neq 0$.
>
> **(b)** $\phi^X_s(x, y) = (x + s, y)$ from $\dot x = 1, \dot y = 0$; $\phi^Y_t(x, y) = (x, y + tx)$ from $\dot x = 0, \dot y = x$. Both flows are global.
>
> **(c)** $\phi^X_s \phi^Y_t(x_0, y_0) = \phi^X_s(x_0, y_0 + tx_0) = (x_0 + s, y_0 + tx_0)$. $\phi^Y_t \phi^X_s(x_0, y_0) = \phi^Y_t(x_0 + s, y_0) = (x_0 + s, y_0 + t(x_0 + s))$. The two results differ by $(0, ts)$, so flows do not commute for any nonzero $s, t$.
>
> **(d)** The bracket $[X, Y] = \partial_y$ is nonzero; the [[Thm - Commuting Flows Theorem]] predicts non-commuting flows, confirmed by (c). The discrepancy $(0, ts) = ts \cdot \partial_y|_p = ts \cdot [X, Y]_p$ is the bracket times $st$ — the leading-order signature of the bracket on the flow parallelogram. $\qquad\blacksquare$

---

# Key Takeaways

**The bracket measures failure of flow parallelograms to close.** In a coordinate chart, reversing the order of the two short flows changes the endpoint by a mixed term $st[X,Y]_p$, up to the sign determined by which ordered difference is taken, plus $O(|s|^2|t|+|s||t|^2)$. Here the chosen difference is exactly $st\partial_y$, with all higher terms absent. The invariant formulation uses the four-flow commutator rather than subtracting points of a manifold.

**Position-dependent coefficients are the source of non-commutation.** $X = \partial_x$ has constant coefficients; $Y = x \partial_y$ has a position-dependent coefficient (the speed of $y$-motion depends on $x$). It is this position-dependence that creates the non-commutation: flowing along $X$ changes $x$, which then changes how $Y$ behaves on the next flow step. Two vector fields with constant coefficients on $\mathbb{R}^n$ always commute (their bracket is zero by the coordinate formula). So non-commutation requires that at least one vector field have non-constant coefficients in some direction. This is the geometric source of all the rich structure in non-trivial Lie algebras.

**The pair $(\partial_x, x \partial_y)$ is the "Heisenberg" archetype.** This exercise is essentially the Lie algebra of the **Heisenberg [[Def - Group|group]]**: the smallest non-abelian Lie group, whose Lie algebra has the bracket relation $[X, Y] = Z$ with $Z$ central. Adding a third vector field $Z = \partial_y$ and noting that $[X, Y] = Z$, $[X, Z] = 0$, $[Y, Z] = 0$ gives the Heisenberg algebra. The exponential map of this algebra is the multiplication law of the Heisenberg group, with non-trivial shear in one coordinate. The exercise is therefore a concrete window into Lie group geometry — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**The bracket pinpoints the *direction* of non-commutation, not just its existence.** $[X, Y] = \partial_y$ is in the $y$-direction, and the discrepancy of the flows is also in the $y$-direction (gap is $(0, ts)$). This is no coincidence: the bracket gives both the *direction* and the *coefficient* (the rate per unit area $st$) of the leading-order non-commutation. Two vector fields with $[X, Y]_p = c \partial_z|_p$ for some constant $c$ produce a parallelogram gap of $c st \partial_z|_p$ at $p$ — direction and magnitude both visible in the bracket.
