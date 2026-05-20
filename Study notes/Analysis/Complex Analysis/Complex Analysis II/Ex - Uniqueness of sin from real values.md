---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Identity Theorem (Uniqueness of Analytic Continuation)"
  - "Def - Complex Exponential and Trigonometric Functions"
tags: [analysis, complex-analysis]
---

# Problem Statement

Show that the complex sine $\sin z := (e^{iz} - e^{-iz})/(2i)$ is the *unique* entire function whose restriction to $\mathbb{R}$ equals the real $\sin x$.

More precisely: if $g : \mathbb{C} \to \mathbb{C}$ is entire and $g(x) = \sin x$ for every $x \in \mathbb{R}$, then $g(z) = \sin z$ for every $z \in \mathbb{C}$.

**Recall:**

[[Def - Complex Exponential and Trigonometric Functions|Complex sine]] $\sin z := (e^{iz} - e^{-iz})/(2i)$, entire (since $e^{\pm iz}$ are entire). On $\mathbb{R}$: $\sin x = (\cos x + i\sin x - \cos x + i\sin x)/(2i) = 2i\sin x/(2i) = \sin x$ (the real one), by Euler's formula.

[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]: two holomorphic functions on a connected domain agreeing on a set with an accumulation point are equal everywhere.

---

# Convergent Strategy

**Problem class:** Uniqueness of analytic continuation from real to complex.

**Assumption pattern:** Two entire functions agreeing on $\mathbb{R}$ — accumulating everywhere along $\mathbb{R}$ in $\mathbb{C}$.

**Theorem routing:** Set $h = g - \sin$, entire and identically zero on $\mathbb{R}$. Identity theorem: $h \equiv 0$ on $\mathbb{C}$.

**Key decision point:** Recognizing that $\mathbb{R}$ has accumulation points everywhere along it (any point of $\mathbb{R}$ is an accumulation of $\mathbb{R}$), so the identity theorem applies.

---

# Legal Operations Used

1. **Form the difference** $h = g - \sin$, entire (difference of entire).
2. **$h \equiv 0$ on $\mathbb{R}$** by hypothesis.
3. **Identify $\mathbb{R}$ as a set with accumulation points in $\mathbb{C}$.** Every point of $\mathbb{R}$ is an accumulation.
4. **Apply [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]** to conclude $h \equiv 0$, hence $g = \sin$.

---

# Hints

> [!note]- Hint 1
> Form $h(z) := g(z) - \sin z$. Show $h$ is entire and vanishes on $\mathbb{R}$.

> [!note]- Hint 2
> $\mathbb{R}$ has accumulation points everywhere along it (any $x \in \mathbb{R}$ is approached by other reals). Apply identity theorem.

---

# Solution

The proof is the canonical "difference of two candidates vanishes on a set with an accumulation point" pattern, in three steps. Step 1 builds the entire difference $h = g - \sin$ and verifies it vanishes on $\mathbb{R}$ via Euler's formula identifying complex and real sine on the real axis; Step 2 notes that every real point is an accumulation point of $\mathbb{R}$ in $\mathbb{C}$; Step 3 applies the identity theorem to conclude $h \equiv 0$. The non-obvious point is that the *complex* sine genuinely agrees with the real sine on $\mathbb{R}$ — without that, the identity theorem would be applied to a different agreement set.

**Step 1: Define $h$ and verify properties.**

Let $h(z) := g(z) - \sin z$. Both $g$ and $\sin$ are entire (by hypothesis and by definition), so $h$ is entire.

By hypothesis, $g(x) = \sin x$ for all $x \in \mathbb{R}$, and $\sin x$ here is the real $\sin x$. We need to confirm: the *complex* $\sin z$ evaluated at $z = x \in \mathbb{R}$ equals the real $\sin x$.

Compute: $\sin x = (e^{ix} - e^{-ix})/(2i) = (\cos x + i\sin x_{\text{real}} - \cos x + i\sin x_{\text{real}})/(2i) = 2i\sin x_{\text{real}}/(2i) = \sin x_{\text{real}}$. ✓ (Here $\sin x_{\text{real}}$ is the real sine; I write it explicitly to avoid confusion.)

So $h(x) = g(x) - \sin x = \sin x_{\text{real}} - \sin x_{\text{real}} = 0$ for all $x \in \mathbb{R}$.

**Step 2: $\mathbb{R}$ has accumulation points in $\mathbb{C}$.**

For any $x_0 \in \mathbb{R}$ and any $\varepsilon > 0$, the neighbourhood $D(x_0, \varepsilon) \subseteq \mathbb{C}$ contains $\{x_0 + t : 0 < |t| < \varepsilon\}$, infinitely many real points different from $x_0$. So $x_0$ is an accumulation point of $\mathbb{R}$ in $\mathbb{C}$.

**Step 3: Apply the identity theorem.**

$\mathbb{C}$ is connected. $h$ is entire (holomorphic on $\mathbb{C}$) and vanishes on $\mathbb{R}$, which has an accumulation point in $\mathbb{C}$ (any point of $\mathbb{R}$). By [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]], $h \equiv 0$ on $\mathbb{C}$.

So $g(z) = \sin z$ for all $z \in \mathbb{C}$. $\blacksquare$

> [!note]- Complete formal solution
> Let $h = g - \sin$ (both entire, so $h$ entire). $h(x) = 0$ for $x \in \mathbb{R}$ (since complex $\sin$ agrees with real $\sin$ on $\mathbb{R}$ by Euler's formula). $\mathbb{R}$ has accumulation points in $\mathbb{C}$ (any real point). By [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]] on the connected $\mathbb{C}$, $h \equiv 0$, so $g \equiv \sin$. $\blacksquare$

---

# Key Takeaways

**Analytic continuation from $\mathbb{R}$ to $\mathbb{C}$.**

This is the prototype: a holomorphic function on $\mathbb{C}$ that is determined by its values on $\mathbb{R}$. The same argument extends:
- $\cos z$ is the unique entire function extending real $\cos x$.
- $e^z$ extends $e^x$ uniquely.
- $\Gamma(z)$ extends the real $\Gamma(x)$ for $x > 0$ uniquely on a maximal domain.

The principle is so strong that one *defines* complex functions by their real restrictions plus "extend analytically", and the extension is automatic. This is the foundation of analytic number theory and special function theory.

**Functional identities extend from real to complex.**

Once we know complex $\sin$ is the unique extension of real $\sin$, identities like $\sin^2 z + \cos^2 z = 1$ extend from $\mathbb{R}$ (where they are standard) to $\mathbb{C}$ — by applying the identity theorem to both sides of the equation. Both sides are entire functions of $z$; they agree on $\mathbb{R}$; hence agree on $\mathbb{C}$.

The same argument lifts:
- All trigonometric identities;
- The exponential addition formula $e^{z + w} = e^z e^w$;
- Polynomial identities of any degree.

This conversion of "real identity" into "complex identity" via analytic continuation is one of the cleanest applications of complex methods.
