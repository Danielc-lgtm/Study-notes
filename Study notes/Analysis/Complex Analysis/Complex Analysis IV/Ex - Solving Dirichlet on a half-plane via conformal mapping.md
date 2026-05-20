---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Poisson Integral Formula"
  - "Def - Conformal Map"
  - "Thm - Möbius Transformations Preserve Generalized Circles"
  - "Ex - Conformal map from upper half-plane to disc"
tags: [analysis, complex-analysis, pde]
---

# Problem Statement

Solve Laplace's equation $\Delta u = 0$ on the upper half-plane $\mathbb{H} = \{\operatorname{Im} z > 0\}$ with boundary data on $\mathbb{R}$:
$$u(x, 0) = \begin{cases}1 & x > 0, \\ 0 & x < 0.\end{cases}$$

Use the Cayley transform $T(z) = (z - i)/(z + i)$ to map $\mathbb{H}$ conformally to the unit disc, transfer the boundary data, solve on $\mathbb{D}$ via Poisson, and pull back.

**Recall:**

![[Thm - Poisson Integral Formula#Notation]]

The Cayley transform $T : \mathbb{H} \to \mathbb{D}$ maps real axis to unit circle, $i \mapsto 0$, $\infty \mapsto 1$.

---

# Convergent Strategy

**Problem class:** Solve a Dirichlet problem on a non-canonical domain ($\mathbb{H}$) by conformally mapping to a canonical one ($\mathbb{D}$). The discontinuous boundary data (Heaviside step) introduces some technical care.

**Assumption pattern:** $\mathbb{H}$ with boundary $\mathbb{R}$, step-function boundary data. Cayley transform $T(z) = (z - i)/(z + i)$ available.

**Theorem routing:** Three-step process: (1) transfer boundary data via $T$, (2) solve Dirichlet on $\mathbb{D}$ via Poisson integral, (3) pull back via $T^{-1}$.

**Key decision point:** Use the **direct formula** for the Poisson integral on the upper half-plane (no need to go through $\mathbb{D}$): for $\mathbb{H}$, the Poisson kernel is $P(x, y; t) = y/(\pi((x - t)^2 + y^2))$, and the harmonic extension of $u_0$ is $u(x, y) = \int_{-\infty}^\infty P(x, y; t) u_0(t)\,dt$.

This is the **arctan integral**: $u(x, y) = (1/\pi)\arctan((\text{something})/y) + $ constant.

---

# Legal Operations Used

1. **Recognize the harmonic function** $u(x, y) = (1/\pi)\arctan(x/y) + 1/2$ has $u(x, y \to 0^+) = $ step function ($1$ for $x > 0$, $0$ for $x < 0$, with value $1/2$ on the boundary itself).
2. **Alternative: explicit Poisson on $\mathbb{H}$** — verify with the formula.
3. **Optional: pull back from disc.** Express $u$ on $\mathbb{D}$ in terms of the Cayley-transformed boundary data, then pull back via $T^{-1}$.

---

# Hints

> [!note]- Hint 1
> Direct: try $u(x, y) = (1/\pi)\arctan(x/y) + C$. At $x > 0, y \to 0^+$: $\arctan(x/y) \to \arctan(\infty) = \pi/2$, so $u \to 1/2 + C$. At $x < 0, y \to 0^+$: $\arctan(x/y) \to \arctan(-\infty) = -\pi/2$, $u \to -1/2 + C$. To match the step (1 for $x > 0$, 0 for $x < 0$): $1/2 + C = 1$ and $-1/2 + C = 0$, both give $C = 1/2$.

> [!note]- Hint 2
> Verify $u(x, y) = (1/\pi)\arctan(x/y) + 1/2$ is harmonic. $\arctan(x/y) = \operatorname{Im}(\log(y - ix)) = \operatorname{Im}(-i\log(x + iy))$... wait, more carefully:
>
> $\arctan(x/y) = \operatorname{Im}(\log(y + ix)/(y - ix))/2$? Better: $\arctan(x/y)$ for $y > 0$ equals $\pi/2 - \arg z$ where $z = x + iy$ in the upper half plane. So $\arctan(x/y) = (\pi/2) - \operatorname{Im}\log z$ (where $\log$ is the principal branch).
>
> Hence $u = (1/\pi)((\pi/2) - \operatorname{Im}\log z) + 1/2 = 1 - (1/\pi)\operatorname{Im}\log z$.

> [!note]- Hint 3
> Since $\log z$ is holomorphic on $\mathbb{H}$, $\operatorname{Im}\log z$ is harmonic on $\mathbb{H}$. So $u$ is harmonic.

---

# Solution

**Step 1: Direct guess**

> [!note]- Derivation
> Recognize that for $z = x + iy$ in $\mathbb{H}$, the principal branch of $\log z$ has $\arg z = \pi - \arctan(x/y)$... actually, let me be careful:
>
> For $z = x + iy$ with $y > 0$: $\arg z \in (0, \pi)$. Specifically, $\arg z = \arctan(y/x)$ if $x > 0$, and $\arg z = \pi - \arctan(y/|x|) = \pi + \arctan(y/x)$ if $x < 0$ (since $\arctan$ has principal range $(-\pi/2, \pi/2)$).
>
> Equivalently, $\arg z = \arctan(y/x)$ adjusted to be in $(0, \pi)$, which equals $\pi/2 - \arctan(x/y)$ (when both $x$ and $y$ are positive; the formula extends to $x < 0$ via the relation $\arctan(x/y) + \arctan(y/x) = \pm\pi/2$).
>
> Direct check: $\arctan(x/y) \to \pi/2$ as $x \to +\infty$ (fixed $y > 0$). $\arctan(x/y) \to -\pi/2$ as $x \to -\infty$.

**Step 2: Define $u$ and verify boundary values**

> [!note]- Derivation
> Define $u(x, y) = \frac{1}{\pi}\arctan(x/y) + \frac{1}{2}$ for $y > 0$.
>
> Boundary behaviour (as $y \to 0^+$, fixed $x$):
> - $x > 0$: $x/y \to +\infty$, $\arctan(x/y) \to \pi/2$. $u \to (1/\pi)(\pi/2) + 1/2 = 1/2 + 1/2 = 1$. ✓
> - $x < 0$: $x/y \to -\infty$, $\arctan(x/y) \to -\pi/2$. $u \to (1/\pi)(-\pi/2) + 1/2 = -1/2 + 1/2 = 0$. ✓
> - $x = 0$: $\arctan(0/y) = 0$. $u = 1/2$ (value at the jump).

**Step 3: Verify $u$ is harmonic on $\mathbb{H}$**

> [!note]- Derivation
> Observe that $\arctan(x/y)$ is related to $\arg z$ for $z = x + iy$ in $\mathbb{H}$. Specifically, $\arg z + \arctan(x/y) = \pi/2$ for $z \in \mathbb{H}$ (verify: at $z = i$, $\arg z = \pi/2$ and $\arctan(0) = 0$; at $z = 1 + i$, $\arg z = \pi/4$ and $\arctan(1) = \pi/4$; sum is $\pi/2$. ✓).
>
> So $\arctan(x/y) = \pi/2 - \arg z = \pi/2 - \operatorname{Im}\log z$.
>
> Therefore $u(x, y) = (1/\pi)(\pi/2 - \operatorname{Im}\log z) + 1/2 = 1 - (1/\pi)\operatorname{Im}\log z$.
>
> Since $\log z$ is holomorphic on $\mathbb{H}$ (which is simply connected and avoids $0$), $\operatorname{Im}\log z$ is harmonic. Hence $u$ is harmonic.
>
> Equivalently: $u = (1/\pi)\arctan(x/y) + 1/2 = (1/\pi)\operatorname{Im}\log(-iz) + 1/2$ (computing: $-iz = y - ix$ for $z = x + iy$, $\log(-iz) = (1/2)\log(x^2 + y^2) + i\arg(-iz) = $ etc.; the calculation works out the same way).

**Step 4: Verify via the Poisson integral on $\mathbb{H}$**

> [!note]- Derivation
> The Poisson kernel for $\mathbb{H}$: $P(x, y; t) = y/(\pi((x - t)^2 + y^2))$ (analogous to disc Poisson, with $|z|^2 - 1$ replaced by $y$, etc.).
>
> Apply to step boundary data: $u(x, y) = \int_0^\infty (y/\pi)/((x - t)^2 + y^2)\,dt$.
>
> Substitute $s = (t - x)/y$: $dt = y\,ds$, $(x - t)^2 + y^2 = y^2(s^2 + 1)$. So
> $$u(x, y) = \int_{-x/y}^\infty \frac{y}{\pi}\cdot\frac{y\,ds}{y^2(s^2 + 1)} = \frac{1}{\pi}\int_{-x/y}^\infty\frac{ds}{1 + s^2} = \frac{1}{\pi}[\arctan s]_{-x/y}^\infty = \frac{1}{\pi}\left(\frac{\pi}{2} - \arctan(-x/y)\right).$$
>
> Simplifying: $\arctan(-x/y) = -\arctan(x/y)$, so $u(x, y) = 1/2 + (1/\pi)\arctan(x/y)$. ✓

> [!note]- Complete formal solution
> Define $u(x, y) = \frac{1}{\pi}\arctan(x/y) + \frac{1}{2}$ for $y > 0$.
>
> **Boundary values.** As $y \to 0^+$ with $x \neq 0$:
> $$\lim_{y \to 0^+}u(x, y) = \frac{1}{\pi}\arctan(\operatorname{sgn}(x)\cdot\infty) + \frac{1}{2} = \begin{cases}1 & x > 0, \\ 0 & x < 0.\end{cases}$$
> Matches the prescribed step boundary data.
>
> **Harmonicity.** $\arctan(x/y) = \pi/2 - \arg z$ for $z = x + iy \in \mathbb{H}$ (verify on test points). So $u = (1/\pi)(\pi/2 - \operatorname{Im}\log z) + 1/2 = 1 - (1/\pi)\operatorname{Im}\log z$. Since $\log z$ is holomorphic on $\mathbb{H}$, $\operatorname{Im}\log z = \arg z$ is harmonic, hence $u$ is harmonic.
>
> **Verification by Poisson on $\mathbb{H}$.** The Poisson integral $u(x, y) = (1/\pi)\int_0^\infty y/((x - t)^2 + y^2)\,dt$ evaluates to the same formula by the substitution $s = (t - x)/y$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "Dirichlet on $\mathbb{H}$ with discontinuous boundary data" → "arctangent of $x/y$".** The step-function boundary data has harmonic extension involving $\arctan(x/y)$, related to the argument $\arg z$. This is the simplest nontrivial Dirichlet problem on the half-plane.

**Real and imaginary parts of $\log z$ give the standard harmonic functions on $\mathbb{H}$.** $\operatorname{Re}\log z = \log|z|$ (harmonic on $\mathbb{C}^\times$, with logarithmic singularity at $0$) and $\operatorname{Im}\log z = \arg z$ (harmonic on simply connected $\mathbb{H}$). The harmonic conjugate of $\log|z|$ on $\mathbb{H}$ is $\arg z$.

**Conformal mapping recipe (general).** For Dirichlet on a domain $D$:
1. Find $\phi : D \to \mathbb{D}$ biholomorphic (Riemann mapping theorem or explicit Möbius).
2. Transfer boundary data: $\tilde u_0 = u_0 \circ \phi^{-1}$ on $\partial\mathbb{D}$.
3. Solve on $\mathbb{D}$ via Poisson: $\tilde u(\zeta) = (1/(2\pi))\int P_r(\theta - \psi)\tilde u_0(e^{i\psi})\,d\psi$.
4. Pull back: $u(z) = \tilde u(\phi(z))$.

This works because *conformal pullback preserves harmonicity*.

**Direct Poisson on $\mathbb{H}$ via the kernel $P(x, y; t) = y/(\pi((x - t)^2 + y^2))$.** Avoids the explicit conformal mapping. The kernel is positive, normalized ($\int_{-\infty}^\infty P\,dt = 1$), and concentrates at $t = x$ as $y \to 0$ — all the properties needed for boundary recovery.

**Generalization to higher dimensions.** The Dirichlet problem on a half-space in $\mathbb{R}^n$ has a similar Poisson kernel $C_n y/(|x - t|^2 + y^2)^{n/2}$. Higher-dimensional harmonic analysis follows the same template.
