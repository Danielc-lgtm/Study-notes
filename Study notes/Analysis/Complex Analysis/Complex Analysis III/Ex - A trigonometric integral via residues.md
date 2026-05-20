---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Trigonometric Integrals via Residues"
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis]
---

# Problem Statement

Evaluate
$$\int_0^{2\pi}\frac{d\theta}{5 + 4\cos\theta}.$$

**Recall:**

![[Thm - Trigonometric Integrals via Residues#The Definition]]

Substitution $z = e^{i\theta}$, $d\theta = dz/(iz)$, $\cos\theta = (z + 1/z)/2$.

---

# Convergent Strategy

**Problem class:** Trigonometric integral over a full period, evaluable by the unit-circle substitution.

**Assumption pattern:** $1/(5 + 4\cos\theta)$ is rational in $\cos\theta$, no real-$\theta$ zeros of denominator (since $5 + 4\cos\theta \geq 5 - 4 = 1 > 0$ for all $\theta$). So the integrand is smooth and bounded.

**Theorem routing:** Substitute $z = e^{i\theta}$, transform to a unit-circle contour integral, apply the residue theorem.

**Key decision point:** After substitution, the denominator factors; identify which roots are inside the unit circle.

---

# Legal Operations Used

1. **Substitute $z = e^{i\theta}$**, converting the integral to a contour integral on $|z| = 1$.
2. **Compute $\cos\theta = (z + 1/z)/2$, $d\theta = dz/(iz)$.**
3. **Simplify the integrand** and clear denominators.
4. **Factor the resulting polynomial** to identify roots.
5. **Determine which roots are inside $|z| = 1$.**
6. **Compute residues** and apply the residue theorem.

---

# Hints

> [!note]- Hint 1
> Substitute $\cos\theta = (z + 1/z)/2$, so $5 + 4\cos\theta = 5 + 2(z + 1/z) = (2z^2 + 5z + 2)/z$.

> [!note]- Hint 2
> The integrand becomes $\frac{1}{(2z^2 + 5z + 2)/z}\cdot\frac{dz}{iz} = \frac{dz}{i(2z^2 + 5z + 2)}$.

> [!note]- Hint 3
> Factor $2z^2 + 5z + 2 = (2z + 1)(z + 2)$. Roots at $z = -1/2$ (inside) and $z = -2$ (outside).

> [!note]- Hint 4
> Residue at $z = -1/2$: $\operatorname{Res}_{-1/2}\,1/(i(2z+1)(z+2)) = 1/(i \cdot 2 \cdot 3/2) = 1/(3i)$.

> [!note]- Hint 5
> Multiply by $2\pi i$: integral $= 2\pi i \cdot 1/(3i) = 2\pi/3$.

---

# Solution

The proof breaks into four steps. Step 1 substitutes $z = e^{i\theta}$ to convert the real trigonometric integral into a contour integral on the unit circle; Step 2 factors the resulting quadratic denominator $(2z+1)(z+2)$ and identifies $z = -1/2$ as the only pole inside; Step 3 computes the simple-pole residue; Step 4 applies the residue theorem to read off $2\pi/3$. The non-obvious move is in Step 1 — recognizing that $\cos\theta = (z + 1/z)/2$ produces a polynomial denominator only after multiplying through by $z$, which is also exactly what $d\theta = dz/(iz)$ supplies.

**Step 1: Substitute $z = e^{i\theta}$**

With $\cos\theta = (z + 1/z)/2$ and $d\theta = dz/(iz)$:
$$5 + 4\cos\theta = 5 + 4\cdot\frac{z + 1/z}{2} = 5 + 2z + \frac{2}{z} = \frac{2z^2 + 5z + 2}{z}.$$

So
$$\int_0^{2\pi}\frac{d\theta}{5 + 4\cos\theta} = \oint_{|z|=1}\frac{z}{2z^2 + 5z + 2}\cdot\frac{dz}{iz} = \oint_{|z|=1}\frac{dz}{i(2z^2 + 5z + 2)}.$$

**Step 2: Factor and identify poles inside the unit disc**

> [!note]- Derivation
> Factor: $2z^2 + 5z + 2 = (2z + 1)(z + 2)$. Roots: $z = -1/2$ and $z = -2$.
>
> $|{-1/2}| = 1/2 < 1$: inside the unit disc.
> $|{-2}| = 2 > 1$: outside.
>
> So only $z = -1/2$ contributes.

**Step 3: Compute the residue at $z = -1/2$**

> [!note]- Derivation
> The function is $1/(i(2z + 1)(z + 2))$. It has a simple pole at $z = -1/2$ (since $(2z + 1)$ has a simple zero there). By the quotient formula:
> $$\operatorname{Res}_{-1/2}\frac{1}{i(2z + 1)(z + 2)} = \frac{1}{i \cdot 2 \cdot (z + 2)}\bigg|_{z = -1/2} = \frac{1}{i \cdot 2 \cdot (3/2)} = \frac{1}{3i}.$$
> (The factor $2$ comes from $d(2z + 1)/dz = 2$.)

**Step 4: Apply the residue theorem**

> [!note]- Derivation
> By the residue theorem on the unit circle:
> $$\oint_{|z|=1}\frac{dz}{i(2z^2 + 5z + 2)} = 2\pi i \cdot \frac{1}{3i} = \frac{2\pi}{3}.$$

> [!note]- Complete formal solution
> Substitute $z = e^{i\theta}$, $d\theta = dz/(iz)$, $\cos\theta = (z + 1/z)/2$:
> $$\int_0^{2\pi}\frac{d\theta}{5 + 4\cos\theta} = \oint_{|z|=1}\frac{dz}{i(2z^2 + 5z + 2)} = \oint_{|z|=1}\frac{dz}{i(2z + 1)(z + 2)}.$$
>
> The integrand has poles at $z = -1/2$ (inside the unit disc) and $z = -2$ (outside). By the residue theorem:
> $$\oint = 2\pi i \cdot \operatorname{Res}_{-1/2}\frac{1}{i(2z + 1)(z + 2)} = 2\pi i \cdot \frac{1}{i \cdot 2 \cdot 3/2} = 2\pi i \cdot \frac{1}{3i} = \frac{2\pi}{3}.$$
> $\blacksquare$
>
> **General formula:** For $a > |b| > 0$, $\int_0^{2\pi} d\theta/(a + b\cos\theta) = 2\pi/\sqrt{a^2 - b^2}$. With $a = 5, b = 4$: $\sqrt{25 - 16} = 3$, giving $2\pi/3$. ✓

---

# Key Takeaways

**Trigger-reaction pattern — trigonometric integral over a full period → unit-circle substitution.** The substitution $z = e^{i\theta}$ is the standard move for $\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta$. The integrand becomes rational in $z$, the contour is the unit circle, and the residue theorem applies cleanly.

**Always identify which roots are inside the unit disc.** After substitution, the denominator is a polynomial in $z$; its roots are the poles of the integrand. By the residue theorem, only poles *inside* $|z| = 1$ contribute. For rational $R(\cos\theta, \sin\theta)$ with $a + b\cos\theta$ in the denominator, the roots are typically $-a/b \pm \sqrt{(a/b)^2 - 1}$, and one is inside, one outside (when $a > |b|$).

**The general formula $\int d\theta/(a + b\cos\theta) = 2\pi/\sqrt{a^2 - b^2}$ is worth memorizing.** It comes up frequently — in probability (the integral of a circular distribution), in electromagnetism (line charge in a half-plane), in fluid dynamics (flow circulation). The derivation is exactly the calculation above with general $a, b$.

**Substitution + residue is mechanical; the art is in handling more exotic integrals.** For $\int_0^{2\pi} \cos(n\theta) d\theta/(a + b\cos\theta)$, the substitution gives $\cos(n\theta) = (z^n + z^{-n})/2$, and the integrand has a more complex pole structure (including a pole of order $n$ at $z = 0$ from the $z^{-n}$ term). The technique extends, but requires care.
