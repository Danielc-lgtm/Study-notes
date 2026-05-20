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

Show that $f(z) = \bar z$ (complex conjugation) is real-differentiable everywhere on $\mathbb{C}$ but complex-differentiable *nowhere*.

Provide two proofs:

(a) Via the Cauchy–Riemann equations.

(b) Directly from the limit definition, by exhibiting two sequences $z_n \to w$ along which the difference quotient $(f(z_n) - f(w))/(z_n - w)$ has different limits.

**Recall:**

A function $f = u + iv : U \to \mathbb{C}$ is complex differentiable at $w$ iff $u, v$ are real differentiable at $w$ AND the [[Thm - Cauchy–Riemann Equations|Cauchy–Riemann equations]] $u_x = v_y, u_y = -v_x$ hold. The map $z = x + iy \mapsto \bar z = x - iy$ is the reflection across the real axis.

---

# Convergent Strategy

**Problem class:** Demonstrating *failure* of complex differentiability for a specific function.

**Assumption pattern:** Explicit formula in terms of $\bar z$ — a red flag that CR will fail.

**Theorem routing:** Either compute partials and verify CR fails (cleanest), or test the limit definition along two specific directions.

**Key decision point:** Recognizing that the appearance of $\bar z$ in the formula is *the* signal — a holomorphic function never depends on $\bar z$. The Wirtinger derivative $\partial \bar z/\partial \bar z = 1 \neq 0$ encapsulates this.

---

# Legal Operations Used

1. **Compute real and imaginary parts.** For $\bar z = x - iy$: $u = x, v = -y$.
2. **Check CR equations.** $u_x = 1, v_y = -1$ — they violate $u_x = v_y$.
3. **Test the limit along two directions.** Real axis ($z = w + h, h \in \mathbb{R}$) and imaginary axis ($z = w + ih$). Different limits prove no complex derivative exists.

---

# Hints

> [!note]- Hint 1
> Write $z = x + iy$, so $\bar z = x - iy$. Read off $u(x, y) = x, v(x, y) = -y$. Compute the partials and check CR.

> [!note]- Hint 2
> For the direct limit: take $z = w + h$ for real $h$, compute $(\bar z - \bar w)/(z - w) = \bar h/h = 1$ (real). Then take $z = w + ih$, compute $(\overline{ih})/(ih) = -ih/(ih) = -1$.

---

# Solution

**(a) Via CR.**

$f(z) = \bar z = x - iy$, so $u(x, y) = x$ and $v(x, y) = -y$. Compute:

> [!note]- Partials
> $u_x = 1, \quad u_y = 0, \quad v_x = 0, \quad v_y = -1$.

CR test: $u_x = 1$ but $v_y = -1$, so $u_x \neq v_y$. The CR equations *fail at every point*. By [[Thm - Cauchy–Riemann Equations]], $f$ is complex differentiable at no point. ✓

Note: $u, v$ are *real* differentiable (they are linear functions), so the failure is purely the CR condition — real differentiability does not upgrade to complex.

**(b) Direct limit calculation.**

Take any $w \in \mathbb{C}$. We compute $(\bar z - \bar w)/(z - w)$ along two paths to $w$.

> [!note]- Along the real axis
> Set $z = w + h$ with $h \in \mathbb{R}, h \to 0$. Then $\bar z = \bar w + h$ (since $\bar h = h$ for real $h$). So
> $$\frac{\bar z - \bar w}{z - w} = \frac{h}{h} = 1.$$

> [!note]- Along the imaginary axis
> Set $z = w + ih$ with $h \in \mathbb{R}, h \to 0$. Then $\bar z = \bar w + \overline{ih} = \bar w - ih$. So
> $$\frac{\bar z - \bar w}{z - w} = \frac{-ih}{ih} = -1.$$

The two limits differ ($1 \neq -1$). Since the limit must exist independently of direction for complex differentiability, $f'(w)$ does not exist. This holds at every $w \in \mathbb{C}$, so $f$ is complex differentiable nowhere. ✓

> [!note]- Complete formal solution
> **(a)** $\bar z = x - iy$, so $u = x, v = -y$. Partials: $u_x = 1, u_y = 0, v_x = 0, v_y = -1$. The CR equation $u_x = v_y$ becomes $1 = -1$, false. So CR fails everywhere; by [[Thm - Cauchy–Riemann Equations]], $f$ is complex differentiable nowhere.
>
> **(b)** Fix $w \in \mathbb{C}$. For $z = w + h$ real, $(\bar z - \bar w)/(z - w) = h/h = 1$. For $z = w + ih$ ($h$ real), $(\bar z - \bar w)/(z - w) = -ih/(ih) = -1$. The limit as $z \to w$ does not exist (two values along two directions). Hence $f'(w)$ does not exist for any $w$. $\blacksquare$

---

# Key Takeaways

**The presence of $\bar z$ is the signature of non-holomorphicity.**

A function with $\bar z$ appearing in its formula will, in general, fail to be holomorphic. The Wirtinger derivative formalism makes this precise: $\partial f/\partial \bar z = 0$ is *equivalent* to CR. The intuition is geometric: complex differentiability is $\mathbb{C}$-linearity of the differential, but conjugation is $\mathbb{C}$-*antilinear* (it commutes with $\bar i = -i$, not $i$). When you see $\bar z$, expect CR failure; when the formula is purely in $z$, expect holomorphicity.

**Direction-dependence of the difference quotient is the operational meaning of CR failure.**

The two-direction test — real axis vs. imaginary axis — is the cleanest way to *show* a function is not complex differentiable. The general pattern: if the limit along two specific directions differs, the limit fails to exist, and complex differentiability is ruled out. This converts an abstract limit-non-existence into a concrete computation.

**Real differentiability does not imply complex differentiability.**

$\bar z$ is a perfectly nice $C^\infty$ function of $(x, y)$ — it's even linear. But the *complex* structure is the extra rigidity: the differential must commute with multiplication by $i$, which the real-linear map $(x, y) \mapsto (x, -y)$ does *not* do. This is the conceptual lesson: holomorphicity is a much stronger condition than real differentiability, and it is the "$\mathbb{C}$-linearity of the differential" that distinguishes them.
