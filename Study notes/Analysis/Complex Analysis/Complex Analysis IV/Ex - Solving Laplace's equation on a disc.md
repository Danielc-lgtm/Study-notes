---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Harmonic Function"
  - "Thm - Poisson Integral Formula"
  - "Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)"
tags: [analysis, complex-analysis, pde]
---

# Problem Statement

Find the harmonic function $u : \overline{\mathbb{D}} \to \mathbb{R}$ on the closed unit disc satisfying the boundary condition $u(e^{i\theta}) = \cos(2\theta)$.

**Recall:**

![[Def - Harmonic Function#The Definition]]

A harmonic function $u$ on $\overline{\mathbb{D}}$ continuous with boundary values $u_0$ on $S^1$ is uniquely determined by $u_0$ ([[Thm - Maximum Principle for Harmonic Functions|max principle for uniqueness]]), and given by the Poisson integral formula
$$u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi) u_0(e^{i\phi})\,d\phi.$$

---

# Convergent Strategy

**Problem class:** Solve a Dirichlet problem on the unit disc with specific boundary data. Two strategies: (a) recognize the boundary data as the real part of a polynomial, get the answer directly; (b) compute the Poisson integral explicitly.

**Assumption pattern:** Boundary data $\cos(2\theta) = \operatorname{Re}(e^{2i\theta}) = \operatorname{Re}(z^2)|_{|z| = 1}$.

**Theorem routing:** $u_0 = \operatorname{Re}(z^2)|_{S^1}$. The harmonic extension is the real part of the corresponding holomorphic function on $\mathbb{D}$: $u(z) = \operatorname{Re}(z^2)$. This is the unique harmonic extension (by max principle uniqueness).

**Key decision point:** Recognize the boundary data as the real part of a holomorphic function. This avoids the explicit Poisson integral computation.

---

# Legal Operations Used

1. **Rewrite $\cos(2\theta)$ as $\operatorname{Re}(e^{2i\theta})$.**
2. **Identify $e^{2i\theta}$ as $z^2|_{|z| = 1}$**, where $z = e^{i\theta}$.
3. **Recognize $z \mapsto z^2$ as holomorphic on $\mathbb{D}$.**
4. **Take real part: $u(z) = \operatorname{Re}(z^2) = \operatorname{Re}((re^{i\theta})^2) = r^2\cos(2\theta)$.**
5. **Verify**: $u(re^{i\theta}) = r^2\cos(2\theta)$ is harmonic (real part of holomorphic), and on $|z| = 1$ ($r = 1$): $u(e^{i\theta}) = \cos(2\theta)$, matching the boundary data.

---

# Hints

> [!note]- Hint 1
> The boundary data $\cos(2\theta) = \operatorname{Re}(e^{2i\theta})$. On $|z| = 1$, $z = e^{i\theta}$, so $e^{2i\theta} = z^2$.

> [!note]- Hint 2
> $z^2$ is holomorphic on $\overline{\mathbb{D}}$. So $\operatorname{Re}(z^2)$ is harmonic on $\overline{\mathbb{D}}$ with boundary values $\operatorname{Re}(z^2)|_{|z| = 1} = \cos(2\theta)$.

> [!note]- Hint 3
> By max-principle uniqueness, $u(z) = \operatorname{Re}(z^2) = r^2\cos(2\theta)$ is the answer.

> [!note]- Hint 4 (alternative via Poisson)
> Compute $u(re^{i\theta}) = (1/(2\pi))\int_0^{2\pi}P_r(\theta - \phi)\cos(2\phi)\,d\phi$. Use the Fourier series of $P_r$: $P_r(\theta) = 1 + 2\sum_{n \geq 1}r^n\cos(n\theta)$. Orthogonality of cosines gives $u(re^{i\theta}) = r^2\cos(2\theta)$.

---

# Solution

**Step 1: Identify the boundary data as the real part of holomorphic**

> [!note]- Derivation
> $\cos(2\theta) = \operatorname{Re}(e^{2i\theta})$. On $S^1$ (where $z = e^{i\theta}$), this equals $\operatorname{Re}(z^2)$.
>
> The function $z \mapsto z^2$ is holomorphic on $\mathbb{D}$ (in fact on $\mathbb{C}$, an entire function), continuous on $\overline{\mathbb{D}}$.

**Step 2: Take the real part on the interior**

> [!note]- Derivation
> Define $u(z) = \operatorname{Re}(z^2)$. Then:
> - $u$ is harmonic on $\mathbb{D}$ (real part of a holomorphic function is harmonic).
> - On the boundary $|z| = 1$: $u(e^{i\theta}) = \operatorname{Re}(e^{2i\theta}) = \cos(2\theta) = u_0(e^{i\theta})$.
> - $u$ is continuous on $\overline{\mathbb{D}}$ (since $z \mapsto z^2$ is continuous).

**Step 3: Express in polar form**

> [!note]- Derivation
> Write $z = re^{i\theta}$, $z^2 = r^2 e^{2i\theta} = r^2(\cos(2\theta) + i\sin(2\theta))$. So $u(re^{i\theta}) = \operatorname{Re}(z^2) = r^2\cos(2\theta)$.

**Step 4: Uniqueness**

> [!note]- Derivation
> By the [[Thm - Maximum Principle for Harmonic Functions|maximum principle]], the Dirichlet problem has at most one solution. We've exhibited one ($u = \operatorname{Re}(z^2) = r^2\cos(2\theta)$), so it's the unique solution.

**Verification via Poisson**

> [!note]- Derivation (alternative)
> The Poisson integral formula gives the same answer. Using the Fourier series of $P_r$:
> $$P_r(\theta - \phi) = 1 + 2\sum_{n \geq 1}r^n\cos(n(\theta - \phi)).$$
> So
> $$u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi}\left(1 + 2\sum_n r^n\cos(n(\theta - \phi))\right)\cos(2\phi)\,d\phi.$$
> Using orthogonality of cosines: $(1/(2\pi))\int\cos(n(\theta - \phi))\cos(2\phi)\,d\phi = (\cos(n\theta)/2)\delta_{n, 2}$ (only $n = 2$ contributes).
>
> So $u(re^{i\theta}) = 2 \cdot r^2 \cdot \cos(2\theta)/2 = r^2\cos(2\theta)$. ✓

> [!note]- Complete formal solution
> Recognize $\cos(2\theta) = \operatorname{Re}(e^{2i\theta}) = \operatorname{Re}(z^2)$ on $|z| = 1$.
>
> The function $u(z) := \operatorname{Re}(z^2) = r^2\cos(2\theta)$ (writing $z = re^{i\theta}$) is harmonic on $\overline{\mathbb{D}}$ (real part of a holomorphic function). On the boundary $|z| = 1$: $u(e^{i\theta}) = \cos(2\theta)$, matching the prescribed boundary data.
>
> By uniqueness of the Dirichlet problem ([[Thm - Maximum Principle for Harmonic Functions|maximum principle]]), $u(re^{i\theta}) = r^2\cos(2\theta)$ is the answer. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "boundary data $\cos(n\theta)$ or $\sin(n\theta)$ on $S^1$" → "harmonic extension $r^n\cos(n\theta)$ or $r^n\sin(n\theta)$".** The trigonometric boundary functions correspond to powers of $z$ (real or imaginary parts), and the harmonic extension is just multiplication by $r^n$. This is the "Fourier-series solution" of the Dirichlet problem.

**Boundary data as Fourier series.** Any continuous boundary data $u_0(e^{i\theta}) = \sum_n a_n\cos(n\theta) + b_n\sin(n\theta)$ has harmonic extension $u(re^{i\theta}) = \sum_n r^n(a_n\cos(n\theta) + b_n\sin(n\theta))$. The convergence is automatic by the Poisson kernel's structure. This is the "modes" of the Dirichlet problem.

**Recognize as real part of holomorphic when possible.** If you can express $u_0$ as $\operatorname{Re} f|_{S^1}$ for some explicit holomorphic $f$, then $u = \operatorname{Re} f$ is the answer immediately — no integral computation needed. Common cases: $u_0 = \cos(n\theta) = \operatorname{Re}(z^n)$, $u_0 = \log|z + 1|$ at the boundary, etc.

**The Poisson integral is the general tool, but specific cases often have closed-form answers.** For "nice" boundary data (polynomial in $\cos\theta, \sin\theta$, or piecewise smooth), the harmonic extension has a closed-form. For more general boundary data, the Poisson integral is the only systematic approach.

**Solving harder Dirichlet problems via conformal mapping.** For domains other than $\mathbb{D}$ (e.g., $\mathbb{H}$, polygons), use the [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping theorem]] to map conformally to $\mathbb{D}$, apply Poisson, pull back. See [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].
