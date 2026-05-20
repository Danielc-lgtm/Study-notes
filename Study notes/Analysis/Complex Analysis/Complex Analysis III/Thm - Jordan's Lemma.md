---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$f$ is a function holomorphic on $\{|z| > R_0\}$, $C_R$ denotes the upper semicircle $\{|z| = R, \operatorname{Im} z \geq 0\}$ (oriented counterclockwise), and $\alpha > 0$ is a real number. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Statement

> **Theorem (Jordan's Lemma).** Let $\alpha > 0$, and let $f$ be holomorphic on $\{|z| > R_0\}$ with $M_R := \sup_{|z|=R,\,\operatorname{Im} z \geq 0}|f(z)| \to 0$ as $R \to \infty$. Let $C_R$ denote the upper semicircle $\{|z| = R, \operatorname{Im} z \geq 0\}$. Then
> $$\int_{C_R} f(z)\, e^{i\alpha z}\, dz \to 0 \qquad \text{as } R \to \infty.$$
> Quantitatively, $\left|\int_{C_R} f(z) e^{i\alpha z}\,dz\right| \leq \pi M_R/\alpha$.

---

# Motivation

The semicircle technique for rational integrals (close real-axis integral with a large upper semicircle) requires the integrand to decay sufficiently at infinity. For purely rational integrands $P/Q$, this means $\deg Q \geq \deg P + 2$, so that $|P/Q| = O(1/|z|^2)$ on the semicircle and the ML estimate forces the semicircle integral to vanish.

But what about integrals like $\int_{-\infty}^\infty (\cos x)/(1 + x^2)\,dx$? Here we want to integrate $e^{ix}/(1 + z^2)$ (and take real parts), but $|e^{ix}| = 1$ on the real axis, so $|e^{iz}/(1 + z^2)| = 1/(1 + R^2)$ on the semicircle, giving the ML bound $\pi R/(1 + R^2) \to 0$ — this happens to work for this specific example. But more generally, integrals like $\int x \sin(\alpha x)/(1 + x^2)\,dx$ have $|f(z)| = O(1/R)$ on the semicircle, and the bare ML estimate gives $\pi R \cdot O(1/R) = O(1)$, which does not vanish.

The reason these integrals *do* still vanish on the semicircle is the **exponential decay of $e^{i\alpha z}$ in the upper half-plane**. For $z = Re^{i\theta}$ in the upper half-plane, $|e^{i\alpha z}| = e^{-\alpha R \sin\theta}$, and on the bulk of the semicircle (away from $\theta = 0, \pi$), $\sin\theta$ is bounded below, so the exponential is much smaller than $1$. Jordan's lemma quantifies this: even with the weakest possible decay $|f(z)| = o(1)$ as $|z| \to \infty$, the integral $\int_{C_R} f(z) e^{i\alpha z}\,dz \to 0$.

This unlocks the entire class of *Fourier-transform-like* integrals: $\int f(x) e^{i\alpha x}\,dx$ for $\alpha > 0$, where $f$ is a rational function with only enough decay to be integrable. The technique handles all such integrals by closure in the upper half-plane.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ holomorphic in $\{|z| > R_0\}$, $|zf(z)|$ bounded (or $\to 0$) on the upper semicircle, $\alpha > 0$".

**$f$ rational with $\deg Q \geq \deg P + 1$.** Property $B$: rational, mild decay. Bridge: enough decay to make Jordan's lemma apply (and not enough for the bare ML technique). Triggers Fourier-transform-like integrals.

**$f(z) e^{i\alpha z}$ with $\alpha > 0$.** Property $B$: the exponential factor has the form needed. Bridge: directly applicable. The condition $\alpha > 0$ is essential — for $\alpha < 0$ the exponential grows on the upper half-plane and Jordan fails (use lower semicircle instead).

**$\cos(\alpha x), \sin(\alpha x)$ integrands.** Property $B$: take real or imaginary part of $e^{i\alpha x}$. Bridge: write integrand as a sum of $e^{i\alpha x}$ terms; apply Jordan to each.

**Targets (Output Amplification)**

The conclusion is $\int_{C_R} f(z) e^{i\alpha z}\,dz \to 0$ as $R \to \infty$.

Combine with the **residue theorem applied to $f(z) e^{i\alpha z}$ on the closed contour.** Amplified result: $\int_{-\infty}^\infty f(x) e^{i\alpha x}\,dx = 2\pi i \sum_{\operatorname{Im} w > 0} \operatorname{Res}_w[f(z) e^{i\alpha z}]$.

Combine with **taking real/imaginary parts.** $\int f(x)\cos(\alpha x)\,dx = \operatorname{Re}[2\pi i\sum\operatorname{Res}]$, similarly for $\sin$.

---

# Why Is It True

The key estimate is the *exponential decay of $e^{i\alpha z}$ in the upper half-plane*. For $z = Re^{i\theta}$ in the upper half-plane ($0 \leq \theta \leq \pi$), $\operatorname{Im} z = R\sin\theta \geq 0$, and $|e^{i\alpha z}| = e^{-\alpha R\sin\theta}$.

The cleverness is using **Jordan's inequality** $\sin\theta \geq 2\theta/\pi$ for $\theta \in [0, \pi/2]$ — a sharp bound saying $\sin\theta$ is at least the chord from $(0, 0)$ to $(\pi/2, 1)$. So $|e^{i\alpha z}| \leq e^{-2\alpha R\theta/\pi}$ for $\theta \in [0, \pi/2]$, by symmetry $|e^{i\alpha z}| \leq e^{-2\alpha R(\pi - \theta)/\pi}$ for $\theta \in [\pi/2, \pi]$.

The integral splits into two halves:
$$\int_{C_R} f(z) e^{i\alpha z}\,dz = \int_0^\pi f(Re^{i\theta}) e^{i\alpha Re^{i\theta}}\,iRe^{i\theta}\,d\theta.$$
Bound the absolute value using $|f(z)| \leq C/R$ (the hypothesis $|zf(z)| \to 0$, or bounded):
$$\left|\int\right| \leq \int_0^\pi C\cdot e^{-\alpha R\sin\theta}\,d\theta \leq 2 \int_0^{\pi/2} C\cdot e^{-2\alpha R\theta/\pi}\,d\theta = 2C \cdot \frac{\pi}{2\alpha R}(1 - e^{-\alpha R}) \to 0.$$
The factor $1/(\alpha R)$ kills the integral as $R \to \infty$, even though the bare ML would not work.

The conceptual point: the exponential $e^{i\alpha z}$ provides *enough* decay on the bulk of the upper semicircle (away from the endpoints $\theta = 0, \pi$ where $\sin\theta = 0$) to compensate for the only mild decay of $f$. Jordan's inequality is the explicit lower bound on $\sin\theta$ that makes this quantitative.

---

# What Makes This Hard

The non-obvious step is **Jordan's inequality $\sin\theta \geq 2\theta/\pi$ on $[0, \pi/2]$**, which converts the integral $\int_0^{\pi/2} e^{-\alpha R \sin\theta}\,d\theta$ into the elementary $\int_0^{\pi/2} e^{-2\alpha R\theta/\pi}\,d\theta = (\pi/(2\alpha R))(1 - e^{-\alpha R})$. Without this inequality, the $\sin\theta$ in the exponent makes the integral hard to bound directly. A common mistake is to apply Jordan's lemma in the lower half-plane for $\alpha > 0$ — but $e^{i\alpha z}$ *grows* in the lower half-plane (since $\operatorname{Im} z < 0$ gives $|e^{i\alpha z}| = e^{-\alpha\operatorname{Im} z} > 1$), so Jordan fails there. Similarly for $\alpha < 0$, one must use the lower semicircle.

---

# Rederivation Scaffold

**High-level strategy:**
On the upper semicircle $z = Re^{i\theta}$, $|e^{i\alpha z}| = e^{-\alpha R\sin\theta}$. Use Jordan's inequality $\sin\theta \geq 2\theta/\pi$ on $[0, \pi/2]$ to bound the integral. The $1/R$ factor from $|f(z)| \leq C/R$ combined with the $\pi/(2\alpha R)$ from the Jordan estimate gives a $1/R^2$-type decay, beating the $\pi R$ length factor.

**Subgoal decomposition:**

1. **Compute $|e^{i\alpha z}|$ on the upper semicircle.** For $z = Re^{i\theta}$ with $\theta \in [0, \pi]$, $|e^{i\alpha z}| = e^{-\alpha R\sin\theta}$.

2. **Apply Jordan's inequality.** $\sin\theta \geq 2\theta/\pi$ for $\theta \in [0, \pi/2]$, so $e^{-\alpha R\sin\theta} \leq e^{-2\alpha R\theta/\pi}$. By symmetry, similar bound on $[\pi/2, \pi]$.

3. **Bound the integral.**
$$\left|\int_{C_R} f e^{i\alpha z}\,dz\right| \leq \int_0^\pi |f(Re^{i\theta})| \cdot e^{-\alpha R\sin\theta} \cdot R\,d\theta \leq R \cdot \max|f| \cdot 2\int_0^{\pi/2} e^{-2\alpha R\theta/\pi}\,d\theta.$$

4. **Evaluate the elementary integral.** $\int_0^{\pi/2} e^{-2\alpha R\theta/\pi}\,d\theta = (\pi/(2\alpha R))(1 - e^{-\alpha R})$. So the bound is $\leq R \cdot \max|f| \cdot 2\cdot \pi/(2\alpha R) = \max|f| \cdot \pi/\alpha$.

5. **Use $\max|f| \to 0$.** The hypothesis $|zf(z)| \to 0$ (or just $|f(z)| \to 0$ uniformly on the semicircle) makes $\max|f| \to 0$, so the bound $\to 0$ as $R \to \infty$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Jordan's inequality
> **Statement:** For $\theta \in [0, \pi/2]$, $\sin\theta \geq 2\theta/\pi$.
>
> **Hint:** The function $\sin\theta/\theta$ is decreasing on $(0, \pi/2]$, with $\sin\theta/\theta = 1$ at $\theta = 0^+$ and $\sin(\pi/2)/(\pi/2) = 2/\pi$. So $\sin\theta/\theta \geq 2/\pi$ on $[0, \pi/2]$, equivalent to $\sin\theta \geq 2\theta/\pi$.
>
> > [!note]- Full proof
> > Define $g(\theta) = \sin\theta - 2\theta/\pi$ on $[0, \pi/2]$. Then $g(0) = 0, g(\pi/2) = 1 - 1 = 0$. We have $g'(\theta) = \cos\theta - 2/\pi$. The equation $\cos\theta = 2/\pi$ has a single root in $(0, \pi/2)$, say $\theta_0 = \arccos(2/\pi)$. So $g'$ is positive on $[0, \theta_0)$ and negative on $(\theta_0, \pi/2]$. Hence $g$ is increasing then decreasing, starting and ending at $0$. The minimum on $[0, \pi/2]$ is at the endpoints, both equal to $0$. So $g(\theta) \geq 0$, i.e., $\sin\theta \geq 2\theta/\pi$, on $[0, \pi/2]$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\alpha > 0$ and $f$ holomorphic on $\{|z| > R_0\}$ with $|f(z)| \to 0$ uniformly as $|z| \to \infty$ in the upper half-plane (the standard form of the hypothesis; "$|z f(z)|$ bounded" is the slightly weaker form, leading to a similar conclusion via the same argument).
>
> For $z = Re^{i\theta}$ on the upper semicircle $C_R$ (where $\theta \in [0, \pi]$):
> $$|e^{i\alpha z}| = |e^{i\alpha R(\cos\theta + i\sin\theta)}| = |e^{i\alpha R\cos\theta} e^{-\alpha R\sin\theta}| = e^{-\alpha R\sin\theta}.$$
>
> So
> $$\left|\int_{C_R} f(z) e^{i\alpha z}\,dz\right| \leq \int_0^\pi |f(Re^{i\theta})| \cdot e^{-\alpha R\sin\theta} \cdot R\,d\theta \leq M_R \cdot R \cdot \int_0^\pi e^{-\alpha R\sin\theta}\,d\theta,$$
> where $M_R := \sup_{|z|=R, \operatorname{Im} z \geq 0}|f(z)| \to 0$ as $R \to \infty$.
>
> **Bound the elementary integral.** By symmetry of $\sin$ about $\theta = \pi/2$, $\int_0^\pi e^{-\alpha R\sin\theta}\,d\theta = 2\int_0^{\pi/2} e^{-\alpha R\sin\theta}\,d\theta$. By Lemma 1, $\sin\theta \geq 2\theta/\pi$ on $[0, \pi/2]$, so
> $$\int_0^{\pi/2} e^{-\alpha R\sin\theta}\,d\theta \leq \int_0^{\pi/2} e^{-2\alpha R\theta/\pi}\,d\theta = \frac{\pi}{2\alpha R}\left(1 - e^{-\alpha R}\right) \leq \frac{\pi}{2\alpha R}.$$
> So $\int_0^\pi e^{-\alpha R\sin\theta}\,d\theta \leq \pi/(\alpha R)$.
>
> **Combine.** $\left|\int_{C_R} f(z) e^{i\alpha z}\,dz\right| \leq M_R \cdot R \cdot \pi/(\alpha R) = M_R \cdot \pi/\alpha \to 0$ as $R \to \infty$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The classic — $\int_{-\infty}^\infty (\cos x)/(1 + x^2)\,dx = \pi/e$.** Apply Jordan to $f(z) = 1/(1 + z^2)$, $\alpha = 1$. Pole at $i$, residue of $e^{iz}/(1 + z^2)$ at $i$ is $e^{i \cdot i}/(2i) = e^{-1}/(2i)$. Integral of $e^{ix}/(1+x^2)$ is $2\pi i \cdot e^{-1}/(2i) = \pi/e$. Take real part to get $\pi/e$ for $\cos x/(1+x^2)$.

**$\int_{-\infty}^\infty x\sin(\alpha x)/(x^2 + 1)\,dx$ for $\alpha > 0$.** Apply Jordan to $f(z) = z/(z^2 + 1)$, $\alpha$ as given. Pole at $z = i$, residue of $z e^{i\alpha z}/(z^2 + 1)$ at $i$ is $i e^{-\alpha}/(2i) = e^{-\alpha}/2$. Integral of $z e^{i\alpha z}/(z^2 + 1)$ is $2\pi i \cdot e^{-\alpha}/2 = \pi i e^{-\alpha}$. Take imaginary part to get $\pi e^{-\alpha}$.

**Inverse Fourier transform of a Lorentzian.** The Fourier transform of $\hat f(\omega) = 1/(\omega^2 + a^2)$ is $f(t) = (1/(2a))e^{-a|t|}$, evaluable via Jordan's lemma applied to the upper or lower half-plane depending on the sign of $t$. This is the classical "Lorentzian goes to exponential" Fourier transform pair.

---

# Bridges

- **[[Thm - Residue Theorem]]** — the engine combined with Jordan to evaluate Fourier-like integrals.

- **[[Thm - Real Rational Integrals via Residues]]** — Jordan extends this technique to oscillatory integrals where the bare ML estimate fails.

- **[[Thm - Trigonometric Integrals via Residues]]** — a different contour (unit circle) for periodic integrands.

---

# Unlocked by This

> [!tip] Fourier Transforms via Residues *(from Applied Analysis)*
> Every Fourier transform of a rational function can be evaluated by Jordan's lemma plus residues. This handles probability distributions (Lorentzian → exponential), signal processing (filter responses), and quantum mechanics (free propagators).

> [!tip] Inverse Laplace and Bromwich *(from Signal Processing)*
> The Bromwich integral for inverse Laplace transforms is a Jordan-like closure problem in the complex $s$-plane. The same exponential-decay argument applies.
