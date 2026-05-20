---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Properties of the Complex Exponential"
  - "Def - Complex Exponential and Trigonometric Functions"
tags: [analysis, complex-analysis]
---

# Problem Statement

Using **Euler's formula** $e^{i\theta} = \cos\theta + i\sin\theta$ and the **addition formula** $e^{i(\theta + \phi)} = e^{i\theta} e^{i\phi}$, derive the classical trigonometric addition formulas:

$$\cos(\theta + \phi) = \cos\theta \cos\phi - \sin\theta \sin\phi,$$
$$\sin(\theta + \phi) = \sin\theta \cos\phi + \cos\theta \sin\phi.$$

Then deduce the double-angle formulas:

$$\cos(2\theta) = \cos^2\theta - \sin^2\theta, \qquad \sin(2\theta) = 2\sin\theta\cos\theta.$$

**Recall:**

Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$ for $\theta \in \mathbb{R}$, from the power series $\exp(i\theta) = \sum (i\theta)^n/n!$ by separating real and imaginary parts. The [[Thm - Properties of the Complex Exponential|addition formula]] $\exp(z + w) = \exp(z)\exp(w)$ holds for all $z, w \in \mathbb{C}$.

---

# Convergent Strategy

**Problem class:** Algebraic identity from a known functional equation.

**Assumption pattern:** Two real numbers $\theta, \phi$; use the complex identity $e^{i(\theta + \phi)} = e^{i\theta} e^{i\phi}$ and separate real and imaginary parts.

**Theorem routing:** Apply Euler to both sides, expand the product, equate real and imaginary parts.

**Key decision point:** Recognizing that *both sides* of the identity, viewed in Cartesian $a + ib$ form, must have equal real parts and equal imaginary parts — this gives *two* identities from *one* complex identity.

---

# Legal Operations Used

1. **Apply Euler's formula** to convert $e^{i\theta}, e^{i\phi}, e^{i(\theta + \phi)}$ into $\cos/\sin$ form.
2. **Expand the product** $(\cos\theta + i\sin\theta)(\cos\phi + i\sin\phi)$ using distributivity.
3. **Equate real and imaginary parts** on both sides.

---

# Hints

> [!note]- Hint 1
> Write $e^{i(\theta + \phi)}$ in two ways: by Euler directly ($\cos(\theta + \phi) + i\sin(\theta + \phi)$), and by the addition formula then Euler ($e^{i\theta}e^{i\phi} = (\cos\theta + i\sin\theta)(\cos\phi + i\sin\phi)$). Equate.

> [!note]- Hint 2
> For double-angle, set $\theta = \phi$ in the result.

---

# Solution

**Step 1: Apply Euler to both sides.**

By Euler, $e^{i(\theta + \phi)} = \cos(\theta + \phi) + i\sin(\theta + \phi)$.

By the addition formula and Euler,
$$e^{i(\theta + \phi)} = e^{i\theta} e^{i\phi} = (\cos\theta + i\sin\theta)(\cos\phi + i\sin\phi).$$

**Step 2: Expand the product.**

$$(\cos\theta + i\sin\theta)(\cos\phi + i\sin\phi) = \cos\theta\cos\phi + i\cos\theta\sin\phi + i\sin\theta\cos\phi + i^2 \sin\theta\sin\phi$$
$$= (\cos\theta\cos\phi - \sin\theta\sin\phi) + i(\sin\theta\cos\phi + \cos\theta\sin\phi).$$

**Step 3: Equate.**

Both expressions for $e^{i(\theta + \phi)}$ must be equal as complex numbers. Equating real parts:
$$\cos(\theta + \phi) = \cos\theta\cos\phi - \sin\theta\sin\phi. \quad\checkmark$$
Equating imaginary parts:
$$\sin(\theta + \phi) = \sin\theta\cos\phi + \cos\theta\sin\phi. \quad\checkmark$$

**Step 4: Double-angle formulas.**

Set $\phi = \theta$ in the addition formulas:
$$\cos(2\theta) = \cos\theta\cos\theta - \sin\theta\sin\theta = \cos^2\theta - \sin^2\theta. \quad\checkmark$$
$$\sin(2\theta) = \sin\theta\cos\theta + \cos\theta\sin\theta = 2\sin\theta\cos\theta. \quad\checkmark$$

> [!note]- Complete formal solution
> By Euler's formula applied to $\theta + \phi$ on one hand, and to $\theta, \phi$ separately with the addition formula on the other:
> $$\cos(\theta + \phi) + i\sin(\theta + \phi) = e^{i(\theta + \phi)} = e^{i\theta}e^{i\phi} = (\cos\theta + i\sin\theta)(\cos\phi + i\sin\phi)$$
> $$= (\cos\theta\cos\phi - \sin\theta\sin\phi) + i(\sin\theta\cos\phi + \cos\theta\sin\phi).$$
> Equating real and imaginary parts yields the addition formulas. Setting $\phi = \theta$ yields the double-angle formulas. $\blacksquare$

---

# Key Takeaways

**One complex identity = two real identities.**

The structural lesson: a single identity in $\mathbb{C}$, equating two complex numbers, packs *two* real identities — one for real parts, one for imaginary parts. This is the universal complex-to-real conversion: any complex-analytic identity that involves Euler's formula will simultaneously deliver a $\cos$-identity and a $\sin$-identity. This is the main reason complex analysis is useful for trigonometric identities — what would be two separate proofs becomes one.

**The addition formula $e^{i(\theta+\phi)} = e^{i\theta}e^{i\phi}$ is the universal trig identity.**

Almost every trigonometric identity ultimately reduces to this single one. Multiple-angle formulas come from $e^{in\theta} = (e^{i\theta})^n$ and the binomial theorem (this is the **de Moivre identity** $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$). Sum-to-product formulas come from $e^{i\theta} + e^{i\phi} = e^{i(\theta + \phi)/2}(e^{i(\theta - \phi)/2} + e^{-i(\theta - \phi)/2}) = 2e^{i(\theta + \phi)/2}\cos((\theta - \phi)/2)$. The exponential is the *generating function* of all trigonometric identities.

**The complex perspective trivializes a class of computations.**

Identities that take pages of trigonometric manipulation often become two-line proofs in the complex setting. The mental discipline: when you see a real trigonometric problem, ask "can I lift this to the exponential?" If yes, the algebra usually simplifies dramatically. This is one of the operational triumphs of complex analysis applied to "elementary" problems.
