---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Cauchy–Riemann Equations"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Problem Statement

Verify directly, by computing real and imaginary parts and checking the Cauchy–Riemann equations, that the following functions are holomorphic on $\mathbb{C}$:

(a) $f(z) = z^2$.

(b) $f(z) = e^z$.

In each case, also compute the complex derivative $f'(z)$ from the CR formula $f'(z) = u_x + iv_x$ and verify it agrees with the expected value.

**Recall:**

A function $f = u + iv : U \to \mathbb{C}$ on an open $U \subseteq \mathbb{C}$ is complex differentiable at $w = c + id$ iff $u, v$ are real differentiable at $(c, d)$ and the [[Thm - Cauchy–Riemann Equations|Cauchy–Riemann equations]] $u_x = v_y, u_y = -v_x$ hold at $(c, d)$. When they hold, $f'(w) = u_x(c, d) + iv_x(c, d)$.

The [[Def - Complex Exponential and Trigonometric Functions|complex exponential]] is $e^z = \exp(z) = \sum_{n=0}^\infty z^n/n!$; on the real and imaginary axes, $e^{x + iy} = e^x(\cos y + i \sin y)$ (Euler's formula).

---

# Convergent Strategy

**Problem class:** Direct verification of complex differentiability by checking CR.

**Assumption pattern:** Explicit functions of $z = x + iy$ with computable real and imaginary parts.

**Theorem routing:** Compute $u(x, y), v(x, y)$; compute all four partials; check CR.

**Key decision point:** Setting up the real-imaginary decomposition cleanly. For $z^2$: $(x + iy)^2 = x^2 - y^2 + 2ixy$. For $e^z$: Euler's formula gives $e^x \cos y + i e^x \sin y$.

---

# Legal Operations Used

1. **Compute real and imaginary parts** of $f = u + iv$ using algebraic expansion.
2. **Compute partial derivatives** $u_x, u_y, v_x, v_y$.
3. **Verify CR equations** $u_x = v_y$ and $u_y = -v_x$.
4. **Extract $f'$ from the CR formula** $f'(z) = u_x + iv_x$.

---

# Hints

> [!note]- Hint 1
> Write $z = x + iy$ and compute $f(z)$ as $u(x, y) + iv(x, y)$ explicitly. For $z^2$, expand the binomial.

> [!note]- Hint 2
> For $e^z$, use Euler's formula: $e^{x + iy} = e^x(\cos y + i \sin y)$. So $u = e^x \cos y$ and $v = e^x \sin y$.

---

# Solution

**(a) $f(z) = z^2$.**

Write $z = x + iy$ with $x, y \in \mathbb{R}$. Then $f(z) = (x + iy)^2 = x^2 - y^2 + 2ixy$. So
$$u(x, y) = x^2 - y^2, \qquad v(x, y) = 2xy.$$

> [!note]- Computing partials
> $u_x = 2x, \quad u_y = -2y, \quad v_x = 2y, \quad v_y = 2x$.
>
> CR check: $u_x = 2x = v_y$. ✓ And $u_y = -2y = -v_x$. ✓

The CR equations hold everywhere; $u, v$ are $C^\infty$ (polynomials), so real differentiable. Hence $f$ is holomorphic on $\mathbb{C}$.

Derivative: $f'(z) = u_x + iv_x = 2x + i(2y) = 2(x + iy) = 2z$. ✓ Matches the expected $f'(z) = 2z$.

**(b) $f(z) = e^z$.**

By Euler's formula, $e^{x + iy} = e^x(\cos y + i\sin y)$. So
$$u(x, y) = e^x \cos y, \qquad v(x, y) = e^x \sin y.$$

> [!note]- Computing partials
> $u_x = e^x \cos y, \quad u_y = -e^x \sin y, \quad v_x = e^x \sin y, \quad v_y = e^x \cos y$.
>
> CR check: $u_x = e^x \cos y = v_y$. ✓ And $u_y = -e^x \sin y = -v_x$. ✓

Both $u, v$ are $C^\infty$ (products of $e^x$ with $\cos y$ or $\sin y$), so real differentiable. Hence $f$ is holomorphic on $\mathbb{C}$ (entire).

Derivative: $f'(z) = u_x + iv_x = e^x\cos y + ie^x \sin y = e^x(\cos y + i\sin y) = e^z$. ✓ Matches the expected $f'(z) = e^z$.

> [!note]- Complete formal solution
> **Part (a).** $f(z) = z^2$ has $u(x, y) = x^2 - y^2, v(x, y) = 2xy$. Partials: $u_x = 2x = v_y$, $u_y = -2y = -v_x$. CR holds; $u, v \in C^\infty(\mathbb{R}^2)$, so real differentiable. By [[Thm - Cauchy–Riemann Equations]], $f$ is holomorphic on $\mathbb{C}$ with $f'(z) = u_x + iv_x = 2x + 2iy = 2z$. $\blacksquare$
>
> **Part (b).** $f(z) = e^z$ has $u = e^x\cos y, v = e^x\sin y$. Partials: $u_x = e^x\cos y = v_y$, $u_y = -e^x\sin y = -v_x$. CR holds; $u, v \in C^\infty$, so real differentiable. By [[Thm - Cauchy–Riemann Equations]], $f$ is holomorphic on $\mathbb{C}$ (entire) with $f'(z) = u_x + iv_x = e^x\cos y + ie^x\sin y = e^x(\cos y + i\sin y) = e^z$. $\blacksquare$

---

# Key Takeaways

**The mechanical pattern for CR verification.**

The procedure is always the same: (1) write $f(z) = f(x + iy) = u(x, y) + iv(x, y)$ explicitly; (2) compute the four partials $u_x, u_y, v_x, v_y$; (3) check $u_x = v_y$ and $u_y = -v_x$. The hard part is step 1 — getting the real and imaginary parts right. For powers of $z$, expand via the binomial theorem. For $e^z$, use Euler's formula. For composite expressions like $\sin z$ or $\cos z$, use the exponential definitions.

**The CR formula is the natural derivative shortcut.**

Once CR is verified, the formula $f'(z) = u_x + iv_x$ provides the complex derivative *for free* from the real partials. This is often the quickest way to compute $f'(z)$ for explicit functions — faster than direct application of differentiation rules in the complex variable. The example $(z^2)' = 2z$ and $(e^z)' = e^z$ both fall out of the CR computation as bonuses.

**Holomorphicity = $\bar z$-free in formulas.**

A function given by a formula in $z$ alone (no $\bar z$ appearing) is automatically holomorphic — by composition of holomorphic functions. So $z^2, e^z, \sin z, z^3 + 5z + 7$, etc., are immediately known to be entire without computing CR. The CR verification confirms this. The Wirtinger criterion $\partial f/\partial \bar z = 0$ formalizes this observation.
