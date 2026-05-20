---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Cauchy Integral Formula"
tags: [analysis, complex-analysis]
---

# Problem Statement

Evaluate the contour integral
$$\int_{|z|=2} \frac{e^z}{z - 1}\,dz$$
where the circle $|z| = 2$ is traversed counterclockwise.

**Recall:**

[[Thm - Cauchy Integral Formula|CIF]]: for $f$ holomorphic on a disc $D(a, R)$ and $w \in D(a, \rho)$ with $\rho < R$:
$$f(w) = \frac{1}{2\pi i}\oint_{|z - a| = \rho}\frac{f(z)}{z - w}\,dz.$$

---

# Convergent Strategy

**Problem class:** Direct application of CIF — integrand has the form $f(z)/(z - w)$ with $f$ holomorphic and $w$ inside the contour.

**Assumption pattern:** Identify $f(z) = e^z$ (entire, hence holomorphic on the disc), $w = 1$ (inside $|z| < 2$).

**Theorem routing:** Apply CIF to obtain $f(w) = (1/2\pi i)\oint f(z)/(z - w)\,dz$, then multiply by $2\pi i$ to get the integral.

**Key decision point:** Recognizing the integrand's structure and identifying $f, w$.

---

# Legal Operations Used

1. **Identify the integrand as $f(z)/(z - w)$.** $f(z) = e^z, w = 1$.
2. **Check $f$ is holomorphic on a disc containing the contour.** $f = e^z$ is entire.
3. **Check $w$ is inside the contour.** $|1| = 1 < 2$. ✓
4. **Apply CIF.** $f(1) = (1/2\pi i)\oint e^z/(z - 1)\,dz$, so integral $= 2\pi i f(1) = 2\pi i e$.

---

# Hints

> [!note]- Hint 1
> The integrand has the form $f(z)/(z - w)$. What is $f$, and what is $w$? Is $w$ inside the circle $|z| = 2$?

> [!note]- Hint 2
> Apply CIF: $f(w) = (1/2\pi i) \oint f(z)/(z - w)\,dz$. So integral = $2\pi i \cdot f(w)$.

---

# Solution

The proof breaks into three short steps. Step 1 recognizes the integrand as the canonical CIF shape $f(z)/(z-w)$; Step 2 verifies that the hypotheses (holomorphy of $f$ on a disc containing the contour, $w$ inside the contour) are met; Step 3 reads off the value as $2\pi i \cdot f(w)$. The only non-obvious move is the pattern match — once $f$ and $w$ are named, the rest is mechanical.

**Step 1: Identify the CIF structure.**

The integrand $e^z/(z - 1) = f(z)/(z - w)$ with $f(z) = e^z$ and $w = 1$.

**Step 2: Verify hypotheses.**

$f(z) = e^z$ is entire, hence holomorphic on any disc containing the contour $|z| = 2$. The point $w = 1$ has $|w - 0| = 1 < 2$, so $w$ is inside the circle $|z| = 2$.

**Step 3: Apply CIF.**

By [[Thm - Cauchy Integral Formula|CIF]] applied to $f = e^z$ on the disc $D(0, R)$ (for any $R > 2$, so the disc contains the contour $|z| = 2$):
$$f(1) = \frac{1}{2\pi i}\oint_{|z|=2}\frac{e^z}{z - 1}\,dz.$$
So
$$\oint_{|z|=2}\frac{e^z}{z - 1}\,dz = 2\pi i \cdot f(1) = 2\pi i \cdot e^1 = 2\pi i e.$$

> [!note]- Complete formal solution
> Apply [[Thm - Cauchy Integral Formula]] with $f(z) = e^z$ (entire) and $w = 1$ (inside $|z| = 2$): $\oint_{|z|=2} e^z/(z - 1)\,dz = 2\pi i \cdot e^1 = 2\pi i e$. $\blacksquare$

---

# Key Takeaways

**Pattern recognition for CIF.**

An integrand of the form $f(z)/(z - w)$ — with a single simple pole at $w$ inside the contour, and $f$ holomorphic on a region containing both the pole and the contour — is the *canonical* setup for CIF. The integral evaluates to $2\pi i \cdot f(w)$. This pattern is universal: recognize it, identify $f$ and $w$, apply.

**Variations and extensions.**

- For higher-order poles $f(z)/(z - w)^{n+1}$: use the higher-derivative CIF $\oint f(z)/(z - w)^{n+1}\,dz = (2\pi i/n!) f^{(n)}(w)$.
- For multiple poles inside the contour: use the residue theorem ([[Complex Analysis III — Winding, Laurent, Residues|CA III]]).
- For a pole *outside* the contour: by Cauchy's theorem, the integral is $0$ (the integrand is holomorphic inside).

**The exponential is friendly.**

$f(z) = e^z$ is entire and gives nice values at integer-rational points: $f(0) = 1, f(1) = e, f(i\pi) = -1$, etc. Combined with CIF, integrals of $e^z$ over various circles give clean answers.
