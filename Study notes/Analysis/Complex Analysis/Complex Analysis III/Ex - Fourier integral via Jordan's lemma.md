---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Jordan's Lemma"
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis]
---

# Problem Statement

Evaluate
$$\int_{-\infty}^\infty \frac{\cos x}{1 + x^2}\,dx$$
by considering $e^{iz}/(1 + z^2)$ on an upper semicircular contour and applying [[Thm - Jordan's Lemma|Jordan's lemma]].

**Recall:**

![[Thm - Jordan's Lemma#Notation]]

Jordan's lemma: if $f$ is holomorphic on $\{|z| > R_0\}$ in the upper half-plane with $|f(z)| \to 0$ uniformly as $|z| \to \infty$, then $\int_{C_R} f(z) e^{i\alpha z}\,dz \to 0$ for any $\alpha > 0$, where $C_R$ is the upper semicircle.

---

# Convergent Strategy

**Problem class:** Real Fourier-transform-like integral, evaluable by residues with Jordan's lemma controlling the side integral. The integrand $\cos x/(1 + x^2)$ is the real part of $e^{ix}/(1 + x^2)$, and the rational factor decays only like $1/x^2$ on the contour — without the exponential, Jordan's would not be needed, but with the oscillatory factor, the integral converges by oscillatory cancellation, and Jordan kills the semicircle.

**Assumption pattern:** $\cos x = \operatorname{Re}(e^{ix})$, so the integral is the real part of $\int e^{ix}/(1 + x^2)\,dx$. The complex extension $e^{iz}/(1 + z^2)$ has $|e^{iz}| = e^{-\operatorname{Im} z} \leq 1$ on the upper half-plane (with equality on the real axis), and decays exponentially as we move up.

**Theorem routing:** Compute $\int_{-\infty}^\infty e^{ix}/(1 + x^2)\,dx$ by contour integration (Jordan + residue theorem); take real part.

**Key decision point:** Close in the *upper* half-plane (where $e^{iz}$ decays for $\alpha = 1 > 0$). The upper-half-plane pole is at $z = i$.

---

# Legal Operations Used

1. **Recognize $\cos x = \operatorname{Re}(e^{ix})$**, so $\int \cos x/(1+x^2)\,dx = \operatorname{Re}\int e^{ix}/(1+x^2)\,dx$.
2. **Extend $e^{ix}/(1+x^2)$ to $e^{iz}/(1 + z^2)$** on $\mathbb{C}$.
3. **Close with the upper semicircle**, valid because $|e^{iz}|$ decays in the upper half-plane.
4. **Apply Jordan's lemma** to show the semicircle integral vanishes.
5. **Apply the residue theorem** to the closed contour.
6. **Take real part** of the result.

---

# Hints

> [!note]- Hint 1
> Consider $f(z) = e^{iz}/(1 + z^2)$. On the upper semicircle, $|e^{iz}| = e^{-\operatorname{Im} z}$ which is at most $1$ on the real axis and decays as we move into the upper half-plane.

> [!note]- Hint 2
> Compute $\operatorname{Res}_i (e^{iz}/(1 + z^2))$: this is $e^{i \cdot i}/(2i) = e^{-1}/(2i)$.

> [!note]- Hint 3
> By the residue theorem and Jordan's lemma, $\int_{-\infty}^\infty e^{ix}/(1 + x^2)\,dx = 2\pi i \cdot e^{-1}/(2i) = \pi/e$.

> [!note]- Hint 4
> Take real part: $\int_{-\infty}^\infty \cos x/(1 + x^2)\,dx = \operatorname{Re}(\pi/e) = \pi/e$.

---

# Solution

**Step 1: Setup — extend to the complex plane**

Recognize $\cos x = \operatorname{Re}(e^{ix})$, so
$$\int_{-\infty}^\infty \frac{\cos x}{1 + x^2}\,dx = \operatorname{Re}\int_{-\infty}^\infty \frac{e^{ix}}{1 + x^2}\,dx.$$

Consider $f(z) = e^{iz}/(1 + z^2)$ on $\mathbb{C}$, with poles at $z = \pm i$.

**Step 2: Close with the upper semicircle and apply the residue theorem**

> [!note]- Derivation
> Let $\Gamma_R = [-R, R] \cup C_R$ where $C_R = \{|z| = R, \operatorname{Im} z \geq 0\}$, oriented counterclockwise. For $R > 1$, $\Gamma_R$ encloses only the pole $z = i$.
>
> By the residue theorem:
> $$\oint_{\Gamma_R} \frac{e^{iz}}{1 + z^2}\,dz = 2\pi i \cdot \operatorname{Res}_i\frac{e^{iz}}{1 + z^2}.$$
>
> Compute the residue (simple pole at $i$): $\operatorname{Res}_i(e^{iz}/(1 + z^2)) = e^{i \cdot i}/(\,(1 + z^2)'|_{z = i}\,) = e^{-1}/(2i)$.
>
> So $\oint_{\Gamma_R} f\,dz = 2\pi i \cdot e^{-1}/(2i) = \pi/e$.

**Step 3: Apply Jordan's lemma to the semicircle**

> [!note]- Derivation
> On the upper semicircle, $|f(z)| = |e^{iz}|/|1 + z^2| \leq e^{-\operatorname{Im} z}/|R^2 - 1|$, so as $|z| \to \infty$ in the upper half-plane, $|f(z)| \to 0$ uniformly (in fact $|f| \to 0$ faster than $1/|z|$).
>
> By [[Thm - Jordan's Lemma|Jordan's lemma]] with $\alpha = 1$: $\int_{C_R} e^{iz}/(1 + z^2)\,dz \to 0$ as $R \to \infty$.

**Step 4: Take the limit**

> [!note]- Derivation
> Decompose: $\oint_{\Gamma_R} = \int_{-R}^R + \int_{C_R}$. As $R \to \infty$, the semicircle integral vanishes by Jordan, leaving
> $$\int_{-\infty}^\infty \frac{e^{ix}}{1 + x^2}\,dx = \pi/e.$$
>
> Take real part: $\int_{-\infty}^\infty \cos x/(1 + x^2)\,dx = \operatorname{Re}(\pi/e) = \pi/e$.
>
> (And $\int_{-\infty}^\infty \sin x/(1 + x^2)\,dx = \operatorname{Im}(\pi/e) = 0$, which is obvious by oddness.)

> [!note]- Complete formal solution
> Consider $f(z) = e^{iz}/(1 + z^2)$ on $\mathbb{C}$, with simple poles at $z = \pm i$.
>
> Close the real-axis contour with the upper semicircle $C_R$ to form $\Gamma_R$. For $R > 1$, the contour encloses only $z = i$. The residue is:
> $$\operatorname{Res}_i\frac{e^{iz}}{1 + z^2} = \frac{e^{i \cdot i}}{(1 + z^2)'|_i} = \frac{e^{-1}}{2i}.$$
>
> By the residue theorem:
> $$\oint_{\Gamma_R}\frac{e^{iz}}{1 + z^2}\,dz = 2\pi i \cdot \frac{e^{-1}}{2i} = \frac{\pi}{e}.$$
>
> On the upper semicircle, $f$ has $|f(z)| = e^{-\operatorname{Im} z}/|1 + z^2|$, and the prefactor $1/|1 + z^2| \leq 1/(R^2 - 1) \to 0$ uniformly. By [[Thm - Jordan's Lemma|Jordan's lemma]] with $\alpha = 1$, $\int_{C_R} f\,dz \to 0$ as $R \to \infty$.
>
> Hence
> $$\int_{-\infty}^\infty\frac{e^{ix}}{1 + x^2}\,dx = \pi/e,$$
> and taking real parts:
> $$\int_{-\infty}^\infty\frac{\cos x}{1 + x^2}\,dx = \pi/e. \quad\blacksquare$$

---

# Key Takeaways

**Trigger-reaction pattern — "Fourier-transform-like real integral" → "extend with $e^{i\alpha z}$, close in upper half-plane (for $\alpha > 0$), apply Jordan".** The standard recipe for $\int f(x) \cos(\alpha x)\,dx$ or $\int f(x)\sin(\alpha x)\,dx$ with $f$ rational. The $e^{i\alpha z}$ provides exponential decay in the upper half-plane (for $\alpha > 0$), making Jordan's lemma applicable and killing the semicircle's contribution.

**Always check the sign of $\alpha$ to choose the half-plane.** For $\alpha > 0$, close in the upper half-plane (where $|e^{i\alpha z}|$ decays). For $\alpha < 0$, close in the lower half-plane. Closing in the wrong half-plane gives $|e^{i\alpha z}|$ blowing up, and Jordan's lemma fails.

**The exponential factor is what makes Jordan applicable.** A bare $\int 1/(1 + x^2)\,dx$ doesn't need Jordan — the ML estimate already kills the semicircle. But $\int x/(1 + x^2)\cdot e^{i\alpha x}\,dx$ would have $|x/(1+x^2)| = O(1/R)$ on the semicircle, and bare ML gives $\pi R \cdot O(1/R) = O(1)$, not vanishing. Jordan provides the *additional decay* from $e^{i\alpha z}$ that closes the gap.

**Take real and imaginary parts at the end, not at the start.** It's much easier to do the contour integral for $e^{i\alpha z}$ (which is meromorphic) than for $\cos(\alpha z)$ or $\sin(\alpha z)$ (which would have to be expanded as $e^{i\alpha z} + e^{-i\alpha z}$ etc.). The strategy: extend to the complex exponential, integrate, then extract real/imaginary parts.

**Result interpretation.** $\pi/e$ is approximately $1.156$ — a positive value, consistent with the integrand $\cos x/(1+x^2)$ being positive on $|x| < \pi/2$ (where $\cos x > 0$) and decaying as $|x|$ grows. The exponential decay $e^{-1}$ comes from the *pole height* — the upper-half-plane pole at $z = i$ contributes $e^{-1}$ from the $e^{iz}$ factor.
