---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Laplace Transform"
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis, signal-processing]
---

# Problem Statement

Compute the inverse Laplace transform of $F(s) = 1/(s^2 + 1)$ using the Bromwich inversion formula and residues. Confirm the answer is $f(t) = \sin(t)$ for $t > 0$.

**Recall:**

![[Def - Laplace Transform#The Definition]]

Bromwich inverse: $f(t) = (1/(2\pi i))\int_{c - i\infty}^{c + i\infty}F(s) e^{st}\,ds$, evaluable for $t > 0$ by closing the contour to the *left* and applying residues.

---

# Convergent Strategy

**Problem class:** Compute inverse Laplace transform by closing the Bromwich contour and applying residues. The pole structure of $F$ determines the modes of $f(t)$.

**Assumption pattern:** $F(s) = 1/(s^2 + 1) = 1/((s - i)(s + i))$ has simple poles at $s = \pm i$. The Bromwich integral closes to the left for $t > 0$, enclosing both poles.

**Theorem routing:** Apply the residue theorem: $f(t) = \sum_{\text{poles}}\operatorname{Res}_{s_k}(F(s) e^{st})$ for $t > 0$.

**Key decision point:** The pole at $s = i$ contributes $e^{it}/(2i)$, the pole at $s = -i$ contributes $e^{-it}/(-2i)$. Sum: $(e^{it} - e^{-it})/(2i) = \sin t$.

---

# Legal Operations Used

1. **Identify poles of $F(s) = 1/(s^2 + 1)$**: $s = \pm i$, both simple.
2. **Compute residues of $F(s) e^{st}$ at each pole**:
   - At $s = i$: $\operatorname{Res}_i F(s) e^{st} = e^{i t}/(s + i)|_{s = i} = e^{it}/(2i)$.
   - At $s = -i$: $\operatorname{Res}_{-i} F(s) e^{st} = e^{-it}/(s - i)|_{s = -i} = e^{-it}/(-2i)$.
3. **Apply residue theorem**: $f(t) = \sum \operatorname{Res} = e^{it}/(2i) - e^{-it}/(2i) = (e^{it} - e^{-it})/(2i) = \sin t$.
4. **Verify closure of contour vanishes**: $F(s) = O(1/|s|^2)$ at infinity, so the left semicircle's contribution vanishes by Jordan-like estimate.

---

# Hints

> [!note]- Hint 1
> Poles of $F(s) = 1/(s^2 + 1)$: $s = \pm i$.

> [!note]- Hint 2
> $\operatorname{Res}_i F(s) e^{st} = e^{i \cdot i t}/(2i) = e^{it}/(2i)$. Wait — more carefully, evaluating at $s = i$: $e^{st}|_{s = i} = e^{it}$. And $(s + i)|_{s = i} = 2i$. So residue is $e^{it}/(2i)$. ✓

> [!note]- Hint 3
> Sum: $e^{it}/(2i) + e^{-it}/(-2i) = (e^{it} - e^{-it})/(2i) = \sin t$.

---

# Solution

The proof breaks into four steps that execute the Bromwich-via-residues recipe. Step 1 identifies the simple poles of $F(s) = 1/(s^2+1)$ at $s = \pm i$; Step 2 computes the residues of $F(s) e^{st}$ at each pole using the quotient formula, yielding $e^{\pm it}/(\pm 2i)$; Step 3 verifies the left semicircle vanishes (the contour-closure step that licenses Bromwich); Step 4 applies the residue theorem and recognizes the sum as $\sin t$ via the Euler-identity decomposition $(e^{it} - e^{-it})/(2i)$. The non-obvious move is in Step 3 — closing the Bromwich contour to the *left* for $t > 0$ uses that $|e^{st}|$ decays exponentially when $\operatorname{Re} s \to -\infty$ and $t > 0$, which encodes causality.

**Step 1: Identify poles**

$F(s) = 1/(s^2 + 1) = 1/((s - i)(s + i))$. Simple poles at $s = i$ and $s = -i$.

**Step 2: Compute residues of $F(s) e^{st}$**

> [!note]- Derivation
> **At $s = i$** (simple pole, quotient form):
> $$\operatorname{Res}_i F(s) e^{st} = \frac{e^{st}}{(s^2 + 1)'\big|_{s = i}} = \frac{e^{it}}{2s\big|_{s = i}} = \frac{e^{it}}{2i}.$$
>
> **At $s = -i$:**
> $$\operatorname{Res}_{-i} F(s) e^{st} = \frac{e^{-it}}{2s\big|_{s = -i}} = \frac{e^{-it}}{-2i}.$$

**Step 3: Verify the left semicircle's contribution vanishes**

> [!note]- Derivation
> Choose the Bromwich contour: vertical line $\operatorname{Re} s = c$ for $c > 0$, closed by a large semicircle to the left. On this semicircle, $\operatorname{Re} s \to -\infty$, so $|e^{st}| = e^{(\operatorname{Re} s)t}$ decays exponentially for $t > 0$ (the key fact licensing closure to the left).
>
> $|F(s)| = 1/|s^2 + 1| \leq 1/(|s|^2 - 1) \to 0$ as $|s| \to \infty$. By an ML estimate (or Jordan-like argument), the integral over the semicircle tends to $0$ as the radius $\to \infty$.

**Step 4: Apply the residue theorem**

> [!note]- Derivation
> By the [[Thm - Residue Theorem|residue theorem]], for $t > 0$:
> $$f(t) = \frac{1}{2\pi i}\oint_{\Gamma}F(s) e^{st}\,ds = \sum_{\text{poles}}\operatorname{Res} = \frac{e^{it}}{2i} + \frac{e^{-it}}{-2i} = \frac{e^{it} - e^{-it}}{2i} = \sin t.$$
>
> So $\mathcal{L}^{-1}\{1/(s^2 + 1)\}(t) = \sin t$ for $t > 0$. ✓

> [!note]- Complete formal solution
> $F(s) = 1/(s^2 + 1)$ has simple poles at $s = \pm i$.
>
> By the Bromwich inversion formula and the residue theorem (with the contour closed to the left for $t > 0$, the left semicircle vanishing by ML):
> $$f(t) = \operatorname{Res}_{i}[F(s) e^{st}] + \operatorname{Res}_{-i}[F(s) e^{st}] = \frac{e^{it}}{2i} + \frac{e^{-it}}{-2i} = \frac{e^{it} - e^{-it}}{2i} = \sin t.$$
>
> Verification: $\mathcal{L}\{\sin t\}(s) = \int_0^\infty\sin t \cdot e^{-st}\,dt = 1/(s^2 + 1)$ (standard). ✓ $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "inverse Laplace via residues" → "close Bromwich to the left, sum residues".** For $F(s)$ rational with poles $s_k$, the inverse Laplace is $f(t) = \sum_k\operatorname{Res}_{s_k}[F(s)e^{st}]$. Each pole contributes a modal term $e^{s_k t}$ (or $te^{s_k t}$ for higher-order poles), weighted by the residue.

**The pole positions are the system's "frequencies".** $s = \pm i$ give the oscillation $\sin t$ (real-axis behaviour at imaginary frequency $\pm 1$). $s = -1$ would give decay $e^{-t}$. $s = -1 + 2i$ would give damped oscillation $e^{-t}(\cos 2t + i\sin 2t)$.

**For $t < 0$, close the contour to the right.** $|e^{st}|$ decays for $\operatorname{Re} s$ large positive (i.e., to the right) when $t < 0$. If $F$ has no poles in the right half-plane (typical for stable systems), the integral is zero, and $f(t) = 0$ for $t < 0$. This is the *causality* of the Laplace inverse.

**Higher-order poles give polynomial-times-exponential.** $F(s) = 1/(s + 1)^2$ has a double pole at $s = -1$. Residue formula: $\operatorname{Res}_{-1}(e^{st}/(s + 1)^2) = d/ds[e^{st}]|_{s = -1} = t e^{-t}$. So $\mathcal{L}^{-1}\{1/(s + 1)^2\} = t e^{-t}$.

**General formula for rational $F$.** For $F(s) = P(s)/Q(s)$ with $Q$ having simple zeros $s_k$ and $\deg Q > \deg P$:
$$f(t) = \sum_k \frac{P(s_k)}{Q'(s_k)}e^{s_k t}, \quad t > 0.$$
The "partial fraction decomposition" of $F$ gives the same answer.

**Applications.** Solving linear ODEs with initial conditions; analyzing transfer functions; computing the time-domain response of linear systems. See [[Ex - Transfer function stability analysis]] and [[Ex - Bandpass filter design via pole placement]].
