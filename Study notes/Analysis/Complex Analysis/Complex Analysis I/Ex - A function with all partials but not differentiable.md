---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Cauchy–Riemann Equations"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Problem Statement

Construct a function $f : \mathbb{C} \to \mathbb{C}$ such that, at the origin $0 \in \mathbb{C}$:

(a) Both partial derivatives $u_x(0, 0), u_y(0, 0), v_x(0, 0), v_y(0, 0)$ exist.

(b) The Cauchy–Riemann equations $u_x = v_y, u_y = -v_x$ are satisfied at $(0, 0)$.

(c) But $f$ is *not* complex differentiable at $0$.

Conclude that "existence of partials + CR" is *strictly weaker* than complex differentiability — the missing ingredient is real differentiability of $u, v$.

**Suggestion.** Try
$$f(z) = \begin{cases} \dfrac{\bar z^2}{z} & z \neq 0 \\ 0 & z = 0\end{cases}$$
or equivalently $f(x + iy) = (x^3 - 3xy^2 + i(3x^2 y - y^3))/((x^2 + y^2)^{1/2})$ — alternatively, a function of the form $f(z) = \exp(-1/z^4)$ extended by $0$ at $0$.

**Recall:**

A function $f = u + iv$ is complex differentiable at $w$ iff $u, v$ are *real* differentiable at $w$ AND CR holds. *Real differentiability* of $u$ at $(c, d)$ means $u(x, y) - u(c, d) - u_x(c-c) - u_y(y - d) = o(\sqrt{(x-c)^2 + (y-d)^2})$. Existence of partials is *not* enough: a function can have both partials at a point without being real differentiable there.

---

# Convergent Strategy

**Problem class:** Constructing a counterexample showing CR-without-differentiability does not imply holomorphicity.

**Assumption pattern:** Find a function whose partials at $0$ exist by direct computation (the function is *separately* differentiable along axes) but whose full $\mathbb{R}^2 \to \mathbb{R}^2$ differential does not exist.

**Theorem routing:** Direct verification.

**Key decision point:** Choosing the function. Pathological homogeneous functions like $\bar z^2/z$ (where the modulus stays under control along axes but not generally) are the classical examples. The Cambridge notes recommend something like $f(z) = \exp(-1/z^4)$ extended by $0$, which has CR holding by computation at $0$ but is genuinely not differentiable there.

---

# Legal Operations Used

1. **Compute partials directly at the origin** by the definition $u_x(0,0) = \lim_{h \to 0}(u(h, 0) - u(0, 0))/h$, etc.
2. **Verify CR holds at the single point.**
3. **Test the complex limit along a non-axial direction** (e.g., $z = h(1 + i)$ for $h \to 0$) and show it differs from the value predicted by the CR formula.

---

# Hints

> [!note]- Hint 1
> Take $f(z) = \bar z^5/|z|^4$ for $z \neq 0$ and $f(0) = 0$. Verify each partial at the origin is $0$ (along each axis, $f$ vanishes faster than $|z|$). CR trivially holds. But along $z = t(1 + i)$, the limit $f(z)/z$ is nonzero.

> [!note]- Hint 2
> Alternative: $f(z) = (\bar z)^2/z$ for $z \neq 0$, $f(0) = 0$. Then $u(x, 0) = x$ and $u(0, y) = -y \cdot \text{something}$. Partials at $0$ work out; CR holds at $0$; but the limit along $z = h e^{i\theta}$ depends on $\theta$.

> [!note]- Hint 3
> The standard Cambridge example: $f(z) = \exp(-1/z^4)$ for $z \neq 0$, $f(0) = 0$. Along the real axis, $f(t) = e^{-1/t^4} \to 0$ extremely fast; all real-derivatives at $0$ are $0$. Similarly along the imaginary axis. So CR holds. But along $z = te^{i\pi/8}$, $z^4 = t^4 e^{i\pi/2} = it^4$, so $1/z^4 = -i/t^4$, and $f = \exp(i/t^4)$ — oscillates wildly, doesn't go to $0$. Failure of differentiability.

---

# Solution

We use the function suggested in the Cambridge IB notes:
$$f(z) = \begin{cases} \exp(-1/z^4) & z \neq 0 \\ 0 & z = 0\end{cases}.$$

**Step 1: Partials at the origin all exist and equal zero.**

> [!note]- Along the real axis
> For $z = h \in \mathbb{R}, h \neq 0$: $f(h) = \exp(-1/h^4)$. As $h \to 0$: $-1/h^4 \to -\infty$, so $f(h) \to 0$ — at rate faster than any polynomial. So $f(h)/h \to 0$, i.e., the directional derivative along $\mathbb{R}$ is $0$.

> [!note]- Along the imaginary axis
> For $z = ih, h \in \mathbb{R}, h \neq 0$: $z^4 = (ih)^4 = i^4 h^4 = h^4$, so $f(ih) = \exp(-1/h^4)$ — same as before. Again $\to 0$ super-polynomially. Directional derivative along $i\mathbb{R}$ is $0$.

From the real-axis behaviour: $u(h, 0) + iv(h, 0) = e^{-1/h^4}$. Since $e^{-1/h^4}$ is *real* (for real $h$), we get $u(h, 0) = e^{-1/h^4}$ and $v(h, 0) = 0$. So $u_x(0, 0) = \lim_{h \to 0} e^{-1/h^4}/h = 0$, $v_x(0, 0) = 0$.

From the imaginary-axis behaviour: similarly $u(0, h) = e^{-1/h^4}, v(0, h) = 0$. So $u_y(0, 0) = 0, v_y(0, 0) = 0$.

**Step 2: CR holds at $0$.**

All four partials are $0$ at the origin, so $u_x(0,0) = v_y(0,0) = 0$ and $u_y(0,0) = -v_x(0,0) = 0$ trivially. ✓

**Step 3: $f$ is not complex differentiable at $0$.**

If $f$ were complex differentiable at $0$, the CR formula would give $f'(0) = u_x(0,0) + iv_x(0,0) = 0$. So the difference quotient $(f(z) - f(0))/(z - 0) = f(z)/z$ would have to tend to $0$ as $z \to 0$.

Test along the ray $z = t e^{i\pi/8}$ for $t > 0$ small. Then $z^4 = t^4 e^{i\pi/2} = i t^4$, so $1/z^4 = -i/t^4$ (modulus $1/t^4$, on the imaginary axis). Then
$$f(z) = \exp(-1/z^4) = \exp(i/t^4).$$
This has modulus $1$ for every $t > 0$. So $|f(z)/z| = 1/t \to \infty$ as $t \to 0^+$.

So $f(z)/z$ does *not* tend to $0$; the complex derivative at $0$ does not exist.

> [!note]- Complete formal solution
> Let $f(z) = e^{-1/z^4}$ for $z \neq 0$, $f(0) = 0$.
>
> **Partials at $0$.** Along $z = h$ real: $f(h) = e^{-1/h^4}$, real-valued. So $u(h, 0) = e^{-1/h^4}, v(h, 0) = 0$. Hence $u_x(0, 0) = \lim_{h \to 0} e^{-1/h^4}/h = 0$ (the exponential decays faster than $h^{-1}$ blows up) and $v_x(0, 0) = 0$. Similarly along $z = ih$: $z^4 = h^4$ (real), so $f(ih) = e^{-1/h^4}$ is real; $u(0, h) = e^{-1/h^4}, v(0, h) = 0$; hence $u_y(0, 0) = 0, v_y(0, 0) = 0$.
>
> **CR at $0$.** $u_x = 0 = v_y$ and $u_y = 0 = -v_x$. ✓
>
> **$f$ not differentiable at $0$.** Take $z_t = te^{i\pi/8}$ for $t > 0$. Then $z_t^4 = t^4 e^{i\pi/2} = it^4$. So $-1/z_t^4 = -1/(it^4) = i/t^4$ (purely imaginary). Hence $f(z_t) = e^{i/t^4}$, which has modulus $1$. The difference quotient is $f(z_t)/z_t = e^{i/t^4}/(te^{i\pi/8})$, with modulus $1/t \to \infty$ as $t \to 0^+$. So $f(z)/z$ has no limit as $z \to 0$, and $f'(0)$ does not exist. $\blacksquare$

---

# Key Takeaways

**Partial-derivative existence is much weaker than real differentiability.**

The classical pathology of multivariable calculus: a function can have all partial derivatives at a point yet not be real differentiable there. The standard example $f(x, y) = xy/(x^2 + y^2)$ at $(0,0)$ has both partials $0$ but no good linear approximation. The complex-analytic version is more striking: even with CR holding, complex differentiability fails. The lesson: the *correct* version of the CR theorem requires real differentiability of $u, v$, not just existence of partials. Stating CR with only "partials exist" is a *false theorem* — this exercise is the standard counterexample.

**Looman–Menchoff and the strengthened theorem.**

The Looman–Menchoff theorem is the deep result that *fills the gap*: if $f$ is continuous on $U$ and the CR equations hold at every point of $U$ (with partials existing pointwise), then $f$ is holomorphic on $U$. So "CR + partials existence" can fail at an *isolated* point (like our example at $0$), but if it holds on a whole open set with continuity, holomorphicity follows. This is a delicate regularity statement and is normally stated, not proved, in introductory complex analysis.

**The Wirtinger viewpoint clarifies what goes wrong.**

The Wirtinger derivative $\partial f/\partial \bar z = \tfrac12(\partial f/\partial x + i \partial f/\partial y)$ captures the "non-holomorphic part" of a function. For real-differentiable $f$, holomorphicity is equivalent to $\partial f/\partial \bar z = 0$. At isolated points where real differentiability fails, the Wirtinger derivative may not even be defined, and pathologies like this one arise. The cleanest framing of holomorphicity is via the Wirtinger criterion; the CR equations are its component form.
