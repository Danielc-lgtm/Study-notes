---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Mean Value Property for Holomorphic Functions"
  - "Thm - Real and Imaginary Parts of a Holomorphic Function are Harmonic"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $u : \Omega \to \mathbb{R}$ be a *harmonic* function on an open $\Omega \subseteq \mathbb{R}^2 \cong \mathbb{C}$. Show that for any $a \in \Omega$ and $r > 0$ with $\overline{D(a, r)} \subseteq \Omega$:
$$u(a) = \frac{1}{2\pi}\int_0^{2\pi} u(a + re^{i\theta})\,d\theta.$$
That is, the value at the centre equals the average over any surrounding circle. This is **Gauss's mean value theorem** for harmonic functions.

**Recall:**

[[Thm - Mean Value Property for Holomorphic Functions]]: $f$ holomorphic on $D(a, R), r < R$: $f(a) = (1/2\pi)\int_0^{2\pi} f(a + re^{i\theta})\,d\theta$. [[Thm - Real and Imaginary Parts of a Holomorphic Function are Harmonic]]: $u, v$ real and imaginary parts of holomorphic $f$ are harmonic. Conversely, on a simply connected domain, harmonic functions have harmonic conjugates.

---

# Convergent Strategy

**Problem class:** Lift a result about holomorphic functions to harmonic functions.

**Assumption pattern:** A harmonic $u$ on a disc.

**Theorem routing:** Build a holomorphic $f = u + iv$ on the disc (harmonic conjugate exists on simply connected discs). Apply MVP to $f$. Take real parts.

**Key decision point:** On a small enough disc, harmonic conjugates exist. The result is *local*, so we work on a sub-disc.

---

# Legal Operations Used

1. **Construct harmonic conjugate** on a disc.
2. **Form holomorphic $f = u + iv$.**
3. **Apply [[Thm - Mean Value Property for Holomorphic Functions|MVP]]** to $f$.
4. **Take real parts** of the resulting identity.

---

# Hints

> [!note]- Hint 1
> On the open disc $\overline{D(a, r)}$ (slightly enlarged) — simply connected — every harmonic function has a harmonic conjugate. Build $v$ and form $f = u + iv$, holomorphic.

> [!note]- Hint 2
> MVP for $f$: $f(a) = (1/2\pi)\int_0^{2\pi} f(a + re^{i\theta})\,d\theta$. Take real parts (both sides).

---

# Solution

The proof breaks into three steps. Step 1 promotes the harmonic $u$ to a holomorphic $f = u + iv$ on a slightly larger disc using the existence of a harmonic conjugate on a simply connected domain; Step 2 invokes the mean value property for holomorphic functions, which gives a complex-valued identity at the centre $a$; Step 3 takes real parts to extract the harmonic statement. The non-obvious move is in Step 1 — recognizing that the harmonic mean value property is just MVP for $f$ in disguise, and that the harmonic conjugate is the bridge.

**Step 1: Harmonic conjugate.**

Since $\overline{D(a, r)} \subseteq \Omega$ and $\Omega$ open, there is a slightly larger disc $D(a, R)$ with $r < R$ and $D(a, R) \subseteq \Omega$. The disc $D(a, R)$ is simply connected, so the harmonic $u$ has a harmonic conjugate $v$ on $D(a, R)$: $v$ is harmonic, and $f := u + iv$ is holomorphic on $D(a, R)$.

> [!note]- Construction of $v$
> Define $v$ by integrating $dv = -u_y\,dx + u_x\,dy$ along paths from $a$. This 1-form is closed on $\Omega$ (since $u$ is harmonic, hence $-u_{yy} = u_{xx}$, the closedness condition). On the simply connected disc $D(a, R)$, the closed form is exact, so $v$ exists.

**Step 2: Apply MVP to $f$.**

By [[Thm - Mean Value Property for Holomorphic Functions]] applied to $f$ on $D(a, R)$ with $r < R$:
$$f(a) = \frac{1}{2\pi}\int_0^{2\pi} f(a + re^{i\theta})\,d\theta.$$

**Step 3: Take real parts.**

$\operatorname{Re} f = u$, so
$$u(a) = \operatorname{Re} f(a) = \operatorname{Re}\left(\frac{1}{2\pi}\int_0^{2\pi} f(a + re^{i\theta})\,d\theta\right) = \frac{1}{2\pi}\int_0^{2\pi} \operatorname{Re} f(a + re^{i\theta})\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} u(a + re^{i\theta})\,d\theta.$$
The interchange of $\operatorname{Re}$ and $\int$ is justified by linearity of $\operatorname{Re}$ (it commutes with integration of complex-valued functions). $\blacksquare$

> [!note]- Complete formal solution
> Build a harmonic conjugate $v$ on a disc $D(a, R) \supseteq \overline{D(a, r)}$, so $f = u + iv$ is holomorphic. MVP for $f$ gives $f(a) = (1/2\pi)\int f(a + re^{i\theta})\,d\theta$. Take real parts: $u(a) = (1/2\pi)\int u(a + re^{i\theta})\,d\theta$. $\blacksquare$

---

# Key Takeaways

**Harmonic functions inherit MVP from holomorphic.**

The mean value property of harmonic functions in 2D is a direct consequence of MVP for holomorphic functions. The bridge is the harmonic conjugate construction, which works on simply connected domains (in particular, on every disc).

For dimensions $\geq 3$, the same MVP holds for harmonic functions, but the proof is different (no complex structure). The general statement: a harmonic function on $\mathbb{R}^n$ satisfies $u(a) = (1/\text{vol}(\partial B))\int_{\partial B} u$ over any ball boundary $B$ centred at $a$. Plus a stronger "ball average" version.

**Reading the complex statement as two real statements.**

A single complex identity (MVP for $f$) packages two real identities (MVP for $u$, MVP for $v$). This is the universal "complex = $2 \times$ real" lifting: a complex-analytic identity is two real-analytic identities in disguise.

**Equivalence of mean value property and harmonicity.**

The converse to Gauss's theorem also holds: a continuous function on an open set satisfying the mean value property on every disc contained in the set is harmonic. So the *characterization* of harmonic functions can be either "$\Delta u = 0$" (differential) or "mean value property" (integral). These two characterizations are equivalent and both useful.
