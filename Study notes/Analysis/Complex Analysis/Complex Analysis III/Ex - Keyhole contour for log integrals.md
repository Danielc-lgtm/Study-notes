---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
  - "Def - Branch of the Logarithm"
  - "Thm - Existence of Log and Square Root on Simply Connected Domains"
tags: [analysis, complex-analysis]
---

# Problem Statement

(a) Show that
$$\int_0^\infty \frac{\log x}{1 + x^2}\,dx = 0$$
by symmetry, and verify by direct computation if you wish.

(b) Evaluate
$$\int_0^\infty \frac{dx}{1 + x^3}$$
using a *cube-root keyhole contour* — a sector of opening angle $2\pi/3$ in the complex plane.

**Recall:**

![[Def - Branch of the Logarithm#Notation]]

On a simply connected $U \subseteq \mathbb{C}^\times$, a branch of $\log z$ exists by [[Thm - Existence of Log and Square Root on Simply Connected Domains|the log existence theorem]], and $z^\alpha = e^{\alpha\log z}$ for any $\alpha \in \mathbb{C}$.

---

# Convergent Strategy

**Problem class:** Contour integration with branch cuts. The integrand has either a logarithm or a fractional power, which is multi-valued and requires a branch cut.

**Assumption pattern:** The integrand $\log x/(1 + x^2)$ involves $\log$, which has a branch cut. The integrand $1/(1 + x^3)$ involves $x^3$, which has cube roots distributed at angles $\pi/3, \pi, 5\pi/3$ — only one inside any $2\pi/3$ sector.

**Theorem routing:** (a) Substitute $x \to 1/x$ to show the integral equals its negative, so it is $0$. (b) Choose a sector contour exploiting the cube-root symmetry: $(1 + (xe^{2\pi i/3})^3) = (1 + x^3)$, so the integrand has the same form along the ray $\arg z = 2\pi/3$ as along the positive real axis. This makes the sector integral cancel cleanly to give the answer.

**Key decision point:** Choosing the contour shape. For (a), no contour needed — symmetry alone. For (b), the cube-root structure of $1 + x^3$ suggests a sector of angle $2\pi/3$.

---

# Legal Operations Used

For (a): **Substitute $x = 1/u$** to relate $\int_0^\infty f(x)\,dx$ to itself with reversed sign.

For (b):
1. **Choose a sector contour** $\Gamma_R$ consisting of: the positive real axis from $0$ to $R$, the arc $\{R e^{i\theta} : 0 \leq \theta \leq 2\pi/3\}$, and the ray back from $R e^{2\pi i/3}$ to $0$.
2. **Identify the pole inside** the sector: the cube roots of $-1$ are $e^{i\pi/3}, e^{i\pi}, e^{i 5\pi/3}$. Only $e^{i\pi/3}$ is inside the sector (between angle $0$ and $2\pi/3$).
3. **Compute the integral on each side of the sector contour.** On the ray $\arg z = 2\pi/3$ traversed back: $z = re^{2\pi i/3}$, so $z^3 = r^3 e^{2\pi i} = r^3$, hence $1 + z^3 = 1 + r^3$. The integrand is the same as on the real axis (up to the orientation factor $e^{2\pi i/3}$).
4. **Apply the residue theorem.**

---

# Hints

> [!note]- Hint for (a)
> Substitute $x = 1/u$, $dx = -du/u^2$. Then $\log x = -\log u$, and $1 + x^2 = 1 + 1/u^2 = (u^2 + 1)/u^2$. The integrand transforms: $\log x/(1+x^2)\cdot dx = -\log u \cdot u^2/(u^2 + 1)\cdot (-du/u^2) = \log u/(1+u^2)\cdot du$. With limits flipped (since $x = 0 \to u = \infty$ and vice versa), this gives the integral equals its negative, hence zero.

> [!note]- Hint for (b)
> Use the sector $\{re^{i\theta} : 0 \leq r \leq R, 0 \leq \theta \leq 2\pi/3\}$. The integral over the arc vanishes as $R \to \infty$. The integral over the ray $\arg z = 2\pi/3$ relates back to the real-axis integral by the cube-root symmetry of $1 + z^3$.

> [!note]- Hint for (b) — pole computation
> $1 + z^3 = 0 \implies z^3 = -1 \implies z = e^{i\pi(2k+1)/3}$ for $k = 0, 1, 2$. The cube roots of $-1$ are $e^{i\pi/3}, e^{i\pi}, e^{i5\pi/3}$. Only $e^{i\pi/3}$ is inside the sector (angle in $(0, 2\pi/3)$).

> [!note]- Hint for (b) — residue
> $\operatorname{Res}_{e^{i\pi/3}}\frac{1}{1 + z^3} = \frac{1}{3 z^2}\bigg|_{z = e^{i\pi/3}} = \frac{1}{3 e^{2\pi i/3}}$.

---

# Solution

**(a) $\int_0^\infty \log x/(1 + x^2)\,dx = 0$**

> [!note]- Derivation
> Substitute $x = 1/u$. Then $dx = -du/u^2$, $\log x = -\log u$, $1 + x^2 = (u^2 + 1)/u^2$. So
> $$\frac{\log x}{1 + x^2}\,dx = -\log u \cdot \frac{u^2}{u^2 + 1}\cdot\left(-\frac{du}{u^2}\right) = \frac{\log u}{u^2 + 1}\,du.$$
> Wait — that gives the same integrand, not its negative. Let me redo:
> $$\frac{\log x}{1 + x^2}\,dx = \frac{-\log u}{(u^2 + 1)/u^2}\cdot\left(-\frac{du}{u^2}\right) = \frac{-\log u \cdot u^2 \cdot -du}{u^2(u^2 + 1)} = \frac{\log u}{u^2 + 1}\,du.$$
> Hmm, still same sign. Let me check more carefully: $\log(1/u) = -\log u$, so we get a factor $-1$ from the logarithm. The $dx = -du/u^2$ gives another factor $-1$. The denominator: $1 + (1/u)^2 = 1 + 1/u^2 = (u^2 + 1)/u^2$, so dividing by this is multiplying by $u^2/(u^2 + 1)$. Combined: $(-\log u) \cdot u^2/(u^2 + 1) \cdot (-du/u^2) = \log u \cdot du/(u^2 + 1)$.
>
> But the limits flip: $x = 0 \to u = \infty$, $x = \infty \to u = 0$. So
> $$\int_0^\infty \frac{\log x}{1 + x^2}\,dx = \int_\infty^0 \frac{\log u}{1 + u^2}\,du = -\int_0^\infty \frac{\log u}{1 + u^2}\,du.$$
> The integral equals its negative, so it is $0$.

**(b) $\int_0^\infty dx/(1 + x^3) = 2\pi/(3\sqrt{3})$**

**Step 1: Set up the sector contour**

> [!note]- Derivation
> Consider $f(z) = 1/(1 + z^3)$ on $\mathbb{C}\setminus\{\text{cube roots of } -1\}$. The cube roots of $-1$ are $\omega_k = e^{i\pi(2k+1)/3}$ for $k = 0, 1, 2$: $\omega_0 = e^{i\pi/3}, \omega_1 = e^{i\pi} = -1, \omega_2 = e^{i5\pi/3} = e^{-i\pi/3}$.
>
> Choose the sector $\Gamma_R$ consisting of three pieces: (i) the positive real axis $[0, R]$, (ii) the arc $\gamma_R = \{Re^{i\theta} : 0 \leq \theta \leq 2\pi/3\}$, (iii) the ray $L_R$ from $Re^{2\pi i/3}$ back to $0$.
>
> Only $\omega_0 = e^{i\pi/3}$ lies in the sector (angle $\pi/3 \in (0, 2\pi/3)$).

**Step 2: Apply the residue theorem**

> [!note]- Derivation
> By the residue theorem (counterclockwise orientation of $\Gamma_R$):
> $$\oint_{\Gamma_R}\frac{dz}{1 + z^3} = 2\pi i\cdot\operatorname{Res}_{\omega_0}\frac{1}{1 + z^3}.$$
> Compute the residue: $\operatorname{Res}_{\omega_0}1/(1 + z^3) = 1/(3z^2)|_{z = \omega_0} = 1/(3 \omega_0^2) = 1/(3 e^{2\pi i/3})$.
>
> So $\oint_{\Gamma_R}\,dz/(1 + z^3) = 2\pi i/(3 e^{2\pi i/3})$.

**Step 3: Compute each piece of the boundary**

> [!note]- Derivation
> **Real axis piece:** $\int_0^R dx/(1 + x^3)$. As $R \to \infty$, this is the integral we want.
>
> **Arc piece:** On $|z| = R$, $|1 + z^3| \geq R^3 - 1$ for $R$ large, so $|1/(1 + z^3)| \leq 1/(R^3 - 1)$. The arc has length $(2\pi/3)R$. By ML: $|\int_{\gamma_R}| \leq (2\pi/3)R/(R^3 - 1) \to 0$.
>
> **Ray piece:** On the ray $z = r e^{2\pi i/3}$ for $r \in [0, R]$, traversed from $R e^{2\pi i/3}$ back to $0$. Then $z^3 = r^3 e^{2\pi i} = r^3$, so $1 + z^3 = 1 + r^3$. And $dz = e^{2\pi i/3}\,dr$. The integral is
> $$\int_R^0 \frac{e^{2\pi i/3}\,dr}{1 + r^3} = -e^{2\pi i/3}\int_0^R \frac{dr}{1 + r^3}.$$

**Step 4: Combine**

> [!note]- Derivation
> Summing the three pieces and letting $R \to \infty$:
> $$\int_0^\infty\frac{dx}{1+x^3} - e^{2\pi i/3}\int_0^\infty\frac{dr}{1 + r^3} = \frac{2\pi i}{3 e^{2\pi i/3}}.$$
> Factor: $(1 - e^{2\pi i/3})\int_0^\infty dx/(1 + x^3) = 2\pi i/(3 e^{2\pi i/3})$.
> $$\int_0^\infty \frac{dx}{1 + x^3} = \frac{2\pi i}{3 e^{2\pi i/3}(1 - e^{2\pi i/3})}.$$
> Simplify the denominator: $e^{2\pi i/3}(1 - e^{2\pi i/3}) = e^{2\pi i/3} - e^{4\pi i/3}$. Using $e^{2\pi i/3} = -1/2 + i\sqrt{3}/2$ and $e^{4\pi i/3} = -1/2 - i\sqrt{3}/2$, we get $e^{2\pi i/3} - e^{4\pi i/3} = i\sqrt{3}$.
>
> So $\int_0^\infty dx/(1 + x^3) = 2\pi i/(3 \cdot i\sqrt{3}) = 2\pi/(3\sqrt{3})$.

> [!note]- Complete formal solution (part b)
> Consider $f(z) = 1/(1 + z^3)$ on the sector $\{re^{i\theta} : r > 0, 0 \leq \theta \leq 2\pi/3\}$. The cube roots of $-1$ in this sector: only $z = e^{i\pi/3}$.
>
> Apply the residue theorem to the boundary $\Gamma_R$ of the sector of radius $R$:
> $$\oint_{\Gamma_R}\frac{dz}{1 + z^3} = 2\pi i \cdot \operatorname{Res}_{e^{i\pi/3}}\frac{1}{1+z^3} = \frac{2\pi i}{3 e^{2\pi i/3}}.$$
>
> The arc contribution vanishes as $R \to \infty$ by ML estimate.
>
> The ray contribution: on $z = re^{2\pi i/3}$ traversed inward, $z^3 = r^3$ (cube of a cube root of unity is $1$, so the angle is irrelevant), and the integral becomes $-e^{2\pi i/3}\int_0^\infty dr/(1 + r^3)$.
>
> Combining:
> $$(1 - e^{2\pi i/3})\int_0^\infty\frac{dx}{1 + x^3} = \frac{2\pi i}{3 e^{2\pi i/3}}.$$
> Multiplying out: $e^{2\pi i/3}(1 - e^{2\pi i/3}) = e^{2\pi i/3} - e^{4\pi i/3} = i\sqrt{3}$.
>
> $$\int_0^\infty \frac{dx}{1 + x^3} = \frac{2\pi i}{3 i\sqrt{3}} = \frac{2\pi}{3\sqrt{3}}. \quad\blacksquare$$

---

# Key Takeaways

**Trigger-reaction pattern — "integral of $1/(1 + x^n)$ on $[0, \infty)$" → "sector contour of angle $2\pi/n$".** The integrand $1/(1+x^n)$ has $n$-fold symmetry: $1 + (xe^{2\pi i/n})^n = 1 + x^n$. A sector of angle $2\pi/n$ exploits this, making the ray integral relate cleanly to the real-axis integral via a phase factor. This works for any $n \geq 2$.

**Trigger-reaction pattern — "$\int_0^\infty f(x) \log x\,dx$" → "substitute $x = 1/u$ and check symmetry"; if symmetric, the answer is $0$.** Many "$\log$-times-rational" integrals on the positive half-line vanish by this substitution. The key is that $\log(1/u) = -\log u$ provides the sign flip.

**Choice of contour reflects symmetry of the integrand.** For symmetric problems on $(-\infty, \infty)$, use a semicircle. For symmetric problems on $[0, \infty)$ with $n$-fold symmetry $f(\omega x) =$ phase $\cdot f(x)$, use a sector of angle $2\pi/n$. For problems with logarithmic singularities or branch cuts on the positive real axis, use a *keyhole contour* (full circle minus a small slit along the cut).

**The arc/ray contributions must vanish for the technique to work.** Always verify ML-type estimates on the arc, and identify the ray relationship to the real-axis integral via the symmetry of the integrand. Mistakes in the orientation or phase factor lead to wrong answers.

**General formula.** $\int_0^\infty dx/(1 + x^n) = (\pi/n)/\sin(\pi/n)$ for $n \geq 2$. Verify for $n = 2$: $\pi/2/\sin(\pi/2) = \pi/2 \cdot 1 = \pi/2$. ✓ Verify for $n = 3$: $\pi/3/\sin(\pi/3) = \pi/3/(\sqrt{3}/2) = 2\pi/(3\sqrt{3})$. ✓
