---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Field"
tags: [algebra, linear-algebra]
---

# Problem Statement

Show that $\omega = \dfrac{-1 + \sqrt{3} i}{2}$ is a cube root of $1$ — that is, $\omega^3 = 1$. Then find all three cube roots of $1$ in $\mathbb{C}$.

(LADR Exercise 1A.7.)

**Recall:**

$\mathbb{C}$ is the field of complex numbers with $i^2 = -1$ and the usual arithmetic. The cube roots of $1$ are the solutions of $z^3 = 1$ in $\mathbb{C}$.

---

# Convergent Strategy

**Problem class:** This is a **direct computation** problem in complex arithmetic. The pattern is to compute $\omega^3$ step by step using $i^2 = -1$ and verify the answer, then factor $z^3 - 1$ to enumerate all cube roots.

**Assumption pattern:** $\omega = (-1 + \sqrt{3} i)/2$ is given as a specific element of $\mathbb{C}$, and complex arithmetic is the only tool — we are not using any structural theorems, just the field axioms of $\mathbb{C}$ together with $i^2 = -1$.

**Theorem routing:** Factor $z^3 - 1 = (z - 1)(z^2 + z + 1)$. The roots of $z^2 + z + 1$ are $\omega = \frac{-1 + \sqrt{3} i}{2}$ and $\overline{\omega} = \frac{-1 - \sqrt{3} i}{2}$, so the three cube roots of $1$ are $1, \omega, \overline{\omega}$.

**Key decision point:** The slick computation is in polar form: $\omega = e^{2\pi i /3}$, so $\omega^3 = e^{2 \pi i} = 1$. But the exercise is in cartesian form so the computation is direct: compute $\omega^2$ first, then $\omega^3 = \omega \cdot \omega^2$.

---

# Legal Operations Used

1. **Direct algebraic computation in $\mathbb{C}$ using $i^2 = -1$** (closest topic-page operation: multiply by the conjugate / use the field axioms of $\mathbb{F}$, operation 8 in spirit). Applied here to compute $\omega^2$ and then $\omega \cdot \omega^2$, each step expanding products via distributivity and reducing $i^2 \to -1$.

2. **Factor a polynomial to extract roots.** The factorization $z^3 - 1 = (z - 1)(z^2 + z + 1)$ converts the cube-root problem into a linear factor (root $1$) and a quadratic. Solving the quadratic via the quadratic formula gives the two remaining roots. This factor-and-solve pattern recurs whenever roots of a polynomial are requested.

---

# Hints

> [!note]- Hint 1
> Compute $\omega^2$ first, then $\omega^3 = \omega \cdot \omega^2$. Use $i^2 = -1$ throughout.

> [!note]- Hint 2
> Polar form: $\omega = \cos(2\pi/3) + i \sin(2\pi/3) = e^{2\pi i/3}$.

---

# Solution

Plan: compute $\omega^2$ directly, then $\omega \cdot \omega^2$.

**Step 1: Compute $\omega^2$.**

> [!note]- Derivation
> $\omega = (-1 + \sqrt{3} i)/2$, so
> $$\omega^2 = \frac{(-1 + \sqrt{3} i)^2}{4} = \frac{1 - 2\sqrt{3} i + 3 i^2}{4} = \frac{1 - 2\sqrt{3} i - 3}{4} = \frac{-2 - 2\sqrt{3} i}{4} = \frac{-1 - \sqrt{3} i}{2}.$$

**Step 2: Compute $\omega^3 = \omega \cdot \omega^2$.**

> [!note]- Derivation
> $$\omega \cdot \omega^2 = \frac{(-1 + \sqrt{3} i)(-1 - \sqrt{3} i)}{4} = \frac{1 - (\sqrt{3} i)^2}{4} = \frac{1 - 3 i^2}{4} = \frac{1 + 3}{4} = 1.$$
> The cross terms cancel and the conjugate-difference trick produces the difference of squares.

**Step 3: List all cube roots of $1$.**

> [!note]- Derivation
> Factor $z^3 - 1 = (z - 1)(z^2 + z + 1)$. The quadratic $z^2 + z + 1$ has roots $z = \frac{-1 \pm \sqrt{-3}}{2} = \frac{-1 \pm \sqrt{3} i}{2}$. So the three cube roots of $1$ are
> $$1, \quad \omega = \frac{-1 + \sqrt{3} i}{2}, \quad \overline{\omega} = \frac{-1 - \sqrt{3} i}{2}.$$

> [!note]- Complete formal solution
> $\omega^2 = \frac{(-1 + \sqrt{3}i)^2}{4} = \frac{-2 - 2\sqrt{3}i}{4} = \frac{-1 - \sqrt{3}i}{2}$. Then $\omega^3 = \omega \cdot \omega^2 = \frac{(-1+\sqrt{3}i)(-1 - \sqrt{3}i)}{4} = \frac{1 + 3}{4} = 1$.
>
> The cube roots of $1$ are the roots of $z^3 - 1 = (z-1)(z^2 + z + 1)$, namely $1, \omega, \overline{\omega} = \omega^2$. $\blacksquare$

---

# Key Takeaways

**Roots of unity in $\mathbb{C}$ form a cyclic [[Def - Group|group]] under multiplication.** The three cube roots $1, \omega, \omega^2$ satisfy $\omega^3 = 1$ and form a [[Def - Group|group]] of order $3$ under multiplication. More generally, the $n$th roots of unity form a cyclic [[Def - Group|group]] of order $n$, isomorphic to $\mathbb{Z}/n\mathbb{Z}$. This is the foundational example in the study of cyclotomic fields and is one of the first appearances of group theory inside complex analysis.

**Polar form makes roots of unity transparent.** Writing $\omega = e^{2\pi i/3}$, $\omega^k = e^{2\pi i k/3}$, and the $n$th roots of unity are $\{e^{2 \pi i k/n} : k = 0, 1, \dots, n-1\}$. The cartesian form $\frac{-1 + \sqrt{3} i}{2}$ is unilluminating; the polar form $e^{2\pi i/3}$ exposes the geometric structure (equally spaced points on the unit circle). Switching between cartesian and polar form is one of the basic conversions in complex analysis, and recognizing when to use which is a transferable skill.

**Cyclotomic polynomials decompose $z^n - 1$.** The factorization $z^3 - 1 = (z - 1)(z^2 + z + 1)$ generalizes: $z^n - 1 = \prod_{d \mid n} \Phi_d(z)$ where $\Phi_d(z)$ is the $d$th cyclotomic polynomial, the minimal polynomial over $\mathbb{Q}$ of a primitive $d$th root of unity. The roots of $\Phi_d$ are exactly the primitive $d$th roots of unity. This bridges complex analysis (roots of unity) with number theory (cyclotomic fields) and is foundational to Galois theory.
