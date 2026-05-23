---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Smooth Vector Field"
  - "Thm - Lie Bracket Properties"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $X, Y \in \mathfrak{X}(\mathbb{R}^3)$ be the smooth vector fields

$$X = x \frac{\partial}{\partial x} + \frac{\partial}{\partial y} + x(y + 1)\frac{\partial}{\partial z}, \qquad Y = \frac{\partial}{\partial x} + y \frac{\partial}{\partial z}.$$

Compute the Lie bracket $[X, Y]$ using the coordinate formula

$$[X, Y]^k = X^i \frac{\partial Y^k}{\partial x^i} - Y^i \frac{\partial X^k}{\partial x^i}.$$

Verify the result by checking that $[\partial/\partial x, \partial/\partial y] = 0$ for the coordinate vector fields (the bracket of coordinate vector fields vanishes).

**Recall:**

The Lie bracket of two smooth vector fields is defined by $[X, Y]f = X(Yf) - Y(Xf)$ on smooth functions, and has the coordinate formula above. The bracket is $\mathbb{R}$-bilinear, antisymmetric, satisfies the Jacobi identity, and satisfies the function product rule $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$.

![[Def - The Lie Bracket of Vector Fields#The Definition]]

The bracket of two coordinate vector fields is zero: $[\partial/\partial x^i, \partial/\partial x^j] = 0$ in any smooth chart — see [[Ex - The Coordinate Vector Fields Commute]].

---

# Convergent Strategy

**Problem class:** Direct application of the coordinate formula for the Lie bracket — a basic computational drill testing comfort with the standard formula. The class is "compute an explicit bracket"; the routine is mechanical once one identifies the components $X^i, Y^j$ in the standard basis.

**Assumption pattern:** Two vector fields are given in explicit coordinate form in $\mathbb{R}^3$ (a chart in which the coordinate vector fields are the standard $\partial/\partial x, \partial/\partial y, \partial/\partial z$). The components $X^1 = x, X^2 = 1, X^3 = x(y+1)$ and $Y^1 = 1, Y^2 = 0, Y^3 = y$ are smooth functions on $\mathbb{R}^3$. The smoothness allows us to apply the coordinate formula directly without worrying about regularity.

**Theorem routing:** The coordinate formula is part (e) of [[Thm - Lie Bracket Properties]]. The verification check uses part (e) again applied to coordinate vector fields (where all components are constants, so all partial derivatives vanish).

**Key decision point:** The only non-obvious choice is whether to compute the bracket using the coordinate formula or via the derivation definition $[X, Y]f = X(Yf) - Y(Xf)$. The coordinate formula is far more efficient here because it bypasses the second-order calculation; the derivation definition is the right choice when components are not given explicitly. Recognize the explicit coordinate form as the trigger for the coordinate formula.

---

# Legal Operations Used

1. **Operation 5 from the topic page (compute a Lie bracket coordinatewise).** Apply $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ component by component, with $X^i, Y^k$ smooth functions of the coordinates. The pattern is direct substitution; the only care needed is in identifying components against the standard basis.

2. **Operation 11 from the topic page ($\mathfrak{X}(M)$ as a $C^\infty(M)$-[[Def - Module|module]]).** Recognize that $X = x \partial_x + 1 \cdot \partial_y + x(y+1) \partial_z$ is a $C^\infty(M)$-linear combination of coordinate vector fields. This is the input format for the coordinate formula.

---

# Hints

> [!note]- Hint 1
> Read off the components: $X^1, X^2, X^3$ are the coefficients of $\partial_x, \partial_y, \partial_z$ in $X$, and similarly $Y^1, Y^2, Y^3$ for $Y$. Now apply $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ for each $k = 1, 2, 3$.

> [!note]- Hint 2
> For $k = 1$: $[X, Y]^1 = X^i \partial_i Y^1 - Y^i \partial_i X^1 = (x)(0) + (1)(0) + (x(y+1))(0) - (1)(1) - (0)(0) - (y)(0)$. Most of the terms vanish because most of the components are constants (so their partial derivatives are zero).

> [!note]- Hint 3
> For the verification: in any chart, the coordinate vector field $\partial/\partial x^i$ has constant components in the basis $(\partial_1, \partial_2, \dots, \partial_n)$ — namely $(0, \dots, 1, \dots, 0)$ with the $1$ in the $i$-th slot. So in the coordinate formula, all the partial derivatives of these components are zero, and the bracket vanishes.

---

# Solution

The proof breaks into two computations. Step 1 computes the three components $[X, Y]^k$ for $k = 1, 2, 3$ using the coordinate formula and the explicit forms of $X, Y$. Step 2 verifies the formula by applying it to two coordinate vector fields and obtaining zero. The non-obvious move is recognizing that most terms in the formula vanish because most components are constants.

**Step 1: Compute $[X, Y]$ component by component.**

We have $X^1 = x, X^2 = 1, X^3 = x(y+1)$ and $Y^1 = 1, Y^2 = 0, Y^3 = y$. The coordinate formula gives:

$$[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k = X^1 \partial_x Y^k + X^2 \partial_y Y^k + X^3 \partial_z Y^k - Y^1 \partial_x X^k - Y^2 \partial_y X^k - Y^3 \partial_z X^k.$$

For $k = 1$: $Y^1 = 1$ (constant), so $\partial_i Y^1 = 0$; the first three terms vanish. $X^1 = x$ has $\partial_x X^1 = 1$ and other partials zero; the last three terms give $-Y^1 \cdot 1 = -1$. So $[X, Y]^1 = -1$, but let's recompute: $-Y^1 \partial_x X^1 - Y^2 \partial_y X^1 - Y^3 \partial_z X^1 = -(1)(1) - (0)(0) - (y)(0) = -1$. So $[X, Y]^1 = 0 - (-1)$? Wait — re-read the formula: $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$. For $k = 1$: first term is $X^i \partial_i Y^1 = 0$ (since $Y^1 = 1$). Second term is $Y^i \partial_i X^1 = Y^1 \partial_x X^1 + Y^2 \partial_y X^1 + Y^3 \partial_z X^1 = (1)(1) + 0 + 0 = 1$. So $[X, Y]^1 = 0 - 1 = -1$.

Hmm, let me recompute using Lee's published Example 8.27, where the answer should be $-\partial/\partial x + (\text{something}) \partial/\partial z$. Let me re-read Lee's calculation carefully — actually Lee's result is $[X, Y] = -\partial/\partial x - y \partial/\partial z$. Let me recompute with this in mind.

> [!note]- Derivation (Step 1)
> $X^1 = x, X^2 = 1, X^3 = x(y+1)$; $Y^1 = 1, Y^2 = 0, Y^3 = y$.
>
> **Component $k = 1$:**
> - $X^i \partial_i Y^1 = X^1 \partial_x Y^1 + X^2 \partial_y Y^1 + X^3 \partial_z Y^1 = x \cdot 0 + 1 \cdot 0 + x(y+1) \cdot 0 = 0$ (since $Y^1 = 1$ is constant).
> - $Y^i \partial_i X^1 = Y^1 \partial_x X^1 + Y^2 \partial_y X^1 + Y^3 \partial_z X^1 = 1 \cdot 1 + 0 \cdot 0 + y \cdot 0 = 1$ (since $\partial_x x = 1$ and other partials vanish).
> - $[X, Y]^1 = 0 - 1 = -1$.
>
> **Component $k = 2$:**
> - $X^i \partial_i Y^2 = 0$ (since $Y^2 = 0$).
> - $Y^i \partial_i X^2 = Y^1 \partial_x X^2 + Y^2 \partial_y X^2 + Y^3 \partial_z X^2 = 1 \cdot 0 + 0 + y \cdot 0 = 0$ (since $X^2 = 1$ is constant).
> - $[X, Y]^2 = 0 - 0 = 0$.
>
> **Component $k = 3$:**
> - $X^i \partial_i Y^3 = X^1 \partial_x Y^3 + X^2 \partial_y Y^3 + X^3 \partial_z Y^3 = x \cdot 0 + 1 \cdot 1 + x(y+1) \cdot 0 = 1$ (since $Y^3 = y$, so $\partial_y Y^3 = 1$).
> - $Y^i \partial_i X^3 = Y^1 \partial_x X^3 + Y^2 \partial_y X^3 + Y^3 \partial_z X^3 = 1 \cdot (y+1) + 0 + y \cdot 0 = y + 1$.
> - $[X, Y]^3 = 1 - (y+1) = -y$.
>
> **Putting it together:**
> $$[X, Y] = -\frac{\partial}{\partial x} + 0 \cdot \frac{\partial}{\partial y} - y \frac{\partial}{\partial z} = -\frac{\partial}{\partial x} - y \frac{\partial}{\partial z}.$$

**Step 2: Verify the formula gives zero on coordinate vector fields.**

Take $X = \partial/\partial x^i$ and $Y = \partial/\partial x^j$ for any pair $i, j$. The components are $X^k = \delta^k_i$ and $Y^k = \delta^k_j$ — constants. So in the coordinate formula, every partial derivative $\partial_l X^k = 0$ and $\partial_l Y^k = 0$, and $[X, Y]^k = 0 - 0 = 0$.

> [!note]- Derivation (Step 2)
> $X = \partial/\partial x^i$ has components $X^k = \delta^k_i$ — equal to $1$ if $k = i$ and $0$ otherwise — all *constants*. Similarly $Y = \partial/\partial x^j$ has components $Y^k = \delta^k_j$ — constants. So $\partial_l X^k = 0$ and $\partial_l Y^k = 0$ for every $l$.
>
> The coordinate formula gives $[X, Y]^k = X^l \partial_l Y^k - Y^l \partial_l X^k = X^l \cdot 0 - Y^l \cdot 0 = 0$ for every $k$.
>
> So $[\partial/\partial x^i, \partial/\partial x^j] = 0$, in agreement with the chapter's general fact.

> [!note]- Complete formal solution
> The components of $X$ are $X^1 = x, X^2 = 1, X^3 = x(y+1)$; the components of $Y$ are $Y^1 = 1, Y^2 = 0, Y^3 = y$.
>
> By the coordinate formula $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$:
>
> **$k = 1$:** $Y^1 = 1$ is constant, so $X^i \partial_i Y^1 = 0$. $\partial_x X^1 = 1$ and other partials vanish, so $Y^i \partial_i X^1 = Y^1 \cdot 1 = 1$. Hence $[X, Y]^1 = -1$.
>
> **$k = 2$:** $Y^2 = 0$ everywhere, so $X^i \partial_i Y^2 = 0$. $X^2 = 1$ is constant, so $Y^i \partial_i X^2 = 0$. Hence $[X, Y]^2 = 0$.
>
> **$k = 3$:** $Y^3 = y$, with $\partial_y Y^3 = 1$ and others zero, so $X^i \partial_i Y^3 = X^2 \cdot 1 = 1$. $X^3 = x(y+1)$, with $\partial_x X^3 = y+1$, $\partial_y X^3 = x$, $\partial_z X^3 = 0$, so $Y^i \partial_i X^3 = Y^1(y+1) + Y^2 \cdot x + Y^3 \cdot 0 = (y+1) + 0 + 0 = y + 1$. Hence $[X, Y]^3 = 1 - (y+1) = -y$.
>
> Therefore:
> $$[X, Y] = -\frac{\partial}{\partial x} - y \frac{\partial}{\partial z}.$$
>
> *Verification on coordinate vector fields.* If $X = \partial/\partial x^i$ and $Y = \partial/\partial x^j$, all components are Kronecker deltas — constants — so all partial derivatives vanish, and the coordinate formula gives $[X, Y]^k = 0$ identically. Hence $[\partial/\partial x^i, \partial/\partial x^j] = 0$, consistent with the general fact.

---

# Key Takeaways

**The coordinate formula is a mechanical bracket calculator.** The formula $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ is the workhorse for every explicit bracket calculation. When you see vector fields presented as $X = X^i \partial_i$ and $Y = Y^j \partial_j$ with smooth components, just apply the formula component by component. The trigger condition is "I can read off the components of both fields in the same coordinate basis"; the action is "compute three derivatives and subtract". This is the first thing to try whenever a bracket appears with explicit data.

**Most terms in a bracket calculation vanish for trivial reasons.** Out of the $3 \times (3 + 3) = 18$ partial-derivative terms in the calculation above (six for each $k$), most are zero because most components are constants or independent of most variables. The strategy is to scan first for components that are constant (their partials vanish) or depend on only one variable (only one partial is nonzero), and rule out those terms by inspection. This makes the bracket calculation much faster than the naive expansion.

**Coordinate vector fields commute trivially.** $[\partial/\partial x^i, \partial/\partial x^j] = 0$ in any chart, because their components in the basis $(\partial_1, \dots, \partial_n)$ are Kronecker deltas — constants — and the coordinate formula reduces to $0$. This is the analytical content of equality of mixed partial derivatives, which is itself a consequence of the smoothness assumption. So *every* coordinate frame is a "commuting frame" (Lee Theorem 9.46), and the converse — every commuting frame is locally a coordinate frame — is the multi-field Straightening Theorem. The triviality of the coordinate-frame bracket is therefore not just trivia: it is the calibration point against which more interesting non-zero brackets are measured.

**Bracket components depend on the chart, but the bracket as a vector field does not.** The components $[X, Y]^k$ are chart-dependent, just like $X^i$ and $Y^j$ are. But the bracket $[X, Y]$ as an *intrinsic* vector field on the manifold is chart-independent. The reason is that the bracket is defined by an intrinsic derivation-commutator construction; the coordinate formula is one chart-representation, and a different chart would give the same intrinsic bracket via the components in that chart. The coordinate formula is "the bracket in coordinates", not "a chart-dependent bracket".
