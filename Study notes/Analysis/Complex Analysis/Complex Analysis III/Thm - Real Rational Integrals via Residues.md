---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis]
---

# Notation

$P, Q$ are polynomials in $z$, $R = P/Q$ is a rational function. The degree of $Q$ minus the degree of $P$ is the "decay rate" at infinity. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Statement

> **Theorem (Real Rational Integrals via Residues).** Let $R(x) = P(x)/Q(x)$ be a rational function with $P, Q$ polynomials such that $\deg Q \geq \deg P + 2$ and $Q$ has no real zeros. Then
> $$\int_{-\infty}^\infty R(x)\,dx = 2\pi i \sum_{w:\,\operatorname{Im} w > 0}\operatorname{Res}_w R,$$
> the sum being over all poles of $R$ in the open upper half-plane.

---

# Motivation

A classical question: how to evaluate $\int_{-\infty}^\infty P(x)/Q(x)\,dx$ when $P/Q$ is a rational function? Direct real-variable methods (partial fractions, trigonometric substitutions) work but are often tedious for polynomial degrees $\geq 3$. The residue theorem provides a slick alternative: extend the real-axis integral to a complex contour, apply residue calculus, and read off the answer.

The key idea: the integral $\int_{-\infty}^\infty R(x)\,dx$ along the real axis is one part of the closed contour $\Gamma_R$ consisting of the segment $[-R, R]$ together with the upper semicircle $C_R = \{|z| = R, \operatorname{Im} z \geq 0\}$. The closed contour encloses the upper-half-plane poles of $R$, and by the residue theorem $\oint_{\Gamma_R} R(z)\,dz = 2\pi i \sum_{\operatorname{Im} w > 0}\operatorname{Res}_w R$. Sending $R \to \infty$, the semicircle's contribution vanishes (provided $R$ decays fast enough at infinity), leaving $\int_{-\infty}^\infty R(x)\,dx = 2\pi i \sum_{\operatorname{Im} w > 0}\operatorname{Res}_w R$.

This is the prototype of "evaluate a real integral by closing in the complex plane". Variants handle rational integrals on the half-line, integrals involving trigonometric or exponential factors (combined with Jordan's lemma), and more exotic contours (keyhole, rectangle, semi-circular). The technique reaches a vast class of integrals that resist real-variable methods.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$R = P/Q$ rational, $\deg Q \geq \deg P + 2$, $Q$ has no real zeros".

**$R$ rational with $\deg Q \geq \deg P + 2$.** The decay condition $\deg Q - \deg P \geq 2$ is what makes the semicircle contribution vanish: on $|z| = R$, $|R(z)| \leq C/R^{\deg Q - \deg P}$, and the ML estimate gives $|\int_{C_R} R(z)\,dz| \leq \pi R \cdot C/R^2 = C\pi/R \to 0$. For $\deg Q - \deg P = 1$, the semicircle doesn't vanish ($\pi R \cdot C/R = C\pi$ stays bounded), so the technique doesn't work directly.

**$Q$ has no real zeros.** This avoids singularities on the contour; if $Q$ has real zeros, the integral $\int_{-\infty}^\infty R\,dx$ may not converge (principal value might still exist, with a different technique).

**Variants.** With trigonometric or exponential factors: $f(x) e^{i\alpha x}$ — use Jordan's lemma for the semicircle. With logarithmic factors: use keyhole contour. With $\int_0^\infty$ — different contour entirely (sometimes use $f(x) \log x$ over the keyhole).

**Targets (Output Amplification)**

The output is a closed-form evaluation of $\int_{-\infty}^\infty R(x)\,dx$.

Combine with **Jordan's lemma for oscillatory integrals.** Property $D$: $R(x) e^{i\alpha x}$ with $\alpha > 0$. Amplified result $E$: $\int_{-\infty}^\infty R(x) e^{i\alpha x}\,dx = 2\pi i \sum_{\operatorname{Im} w > 0}\operatorname{Res}_w[R(z) e^{i\alpha z}]$ — Fourier-transform-like.

Combine with **taking real or imaginary parts.** Property $D$: $\cos(\alpha x) = \operatorname{Re} e^{i\alpha x}$, $\sin(\alpha x) = \operatorname{Im} e^{i\alpha x}$. Amplified result $E$: $\int R(x)\cos(\alpha x)\,dx = \operatorname{Re}[2\pi i\sum\operatorname{Res}]$, similarly for $\sin$.

Combine with **convergence of $\int_0^\infty$.** Property $D$: if $R$ is *even*, $\int_{-\infty}^\infty R = 2\int_0^\infty R$, halving the work. For odd $R$, $\int_{-\infty}^\infty R = 0$.

---

# Why Is It True

The picture: close the real-axis integral with a large semicircle. The closed contour encloses some poles (the upper-half-plane ones). The residue theorem evaluates the closed integral in terms of these residues. The real-axis piece is what we want; the semicircle piece is what we need to bound.

The semicircle bound is an *ML estimate* (length times max). On $|z| = R$ in the upper half-plane, $|R(z)| \leq C/R^{\deg Q - \deg P}$ for $R$ large (dominant terms of $P, Q$); length of semicircle is $\pi R$. So $|\int_{C_R} R\,dz| \leq \pi R \cdot C/R^{\deg Q - \deg P} = C\pi/R^{\deg Q - \deg P - 1}$. For this to vanish as $R \to \infty$, need $\deg Q - \deg P > 1$, i.e., $\deg Q \geq \deg P + 2$.

The choice of *upper* semicircle is somewhat arbitrary — we could choose the lower one, enclosing different poles. The residues sum to give the *same* answer (the integral is independent of contour choice). Conventionally upper is used; if $R$ has no upper-half-plane poles but does have lower-half-plane ones, use lower instead (with a sign flip for the orientation).

The condition "$Q$ has no real zeros" is what makes the contour avoid singularities on the real axis. If $Q$ has real zeros, the integral diverges (unless one takes principal value, requiring small semicircles indenting around the real-axis poles).

---

# What Makes This Hard

The non-obvious step is **choosing the right contour and verifying the side-integral vanishes**. The standard upper-semicircle works for rational integrals with sufficient decay, but variants (Jordan's lemma for oscillatory, keyhole for $\log$, rectangle for hyperbolic) require different choices. A common mistake is to apply the upper semicircle technique to $R(x) e^{i\alpha x}$ with $\alpha < 0$ (the exponential blows up on the upper semicircle) — should use lower semicircle. A second slip is to forget the decay condition $\deg Q \geq \deg P + 2$ and apply the technique to $\int 1/(1 + x)\,dx$, which actually diverges.

---

# Rederivation Scaffold

**High-level strategy:**
Extend $R(x)$ to $R(z)$ on $\mathbb{C}$. Close the real-axis contour with a large upper semicircle. Apply the residue theorem to the closed contour. Show the semicircle's contribution vanishes as the radius grows. The real-axis piece equals the residue sum.

**Subgoal decomposition:**

1. **Define the closed contour $\Gamma_R = [-R, R] \cup C_R$**, where $C_R$ is the upper semicircle $|z| = R, \operatorname{Im} z \geq 0$, oriented counterclockwise.

2. **Apply residue theorem to $\Gamma_R$.** For $R$ large enough to enclose all upper-half-plane poles, $\oint_{\Gamma_R} R(z)\,dz = 2\pi i \sum_{\operatorname{Im} w > 0}\operatorname{Res}_w R$.

3. **Show $\int_{C_R} R(z)\,dz \to 0$ as $R \to \infty$.**
   - *Hint:* ML estimate. $|R(z)| \leq C/R^{\deg Q - \deg P}$ on $|z| = R$ for $R$ large; length of $C_R$ is $\pi R$; product is $C\pi/R^{\deg Q - \deg P - 1} \to 0$ when $\deg Q - \deg P \geq 2$.

4. **Take the limit.** $\int_{-R}^R R(x)\,dx + \int_{C_R} R\,dz = 2\pi i \sum\operatorname{Res}$. As $R \to \infty$, semicircle vanishes, and $\int_{-R}^R R\,dx \to \int_{-\infty}^\infty R\,dx$. Conclusion: $\int_{-\infty}^\infty R(x)\,dx = 2\pi i \sum_{\operatorname{Im} w > 0}\operatorname{Res}_w R$.

---

# Lemma Decomposition

> [!note]- Lemma 1: ML estimate on the semicircle
> **Statement:** If $\deg Q \geq \deg P + 2$ and $|z| = R$, then $|R(z)| \leq C/R^{\deg Q - \deg P}$ for $R$ large, where $C$ is a constant depending on $P, Q$.
>
> > [!note]- Full proof
> > Write $P(z) = p_d z^d + (\text{lower})$ and $Q(z) = q_n z^n + (\text{lower})$ with $d = \deg P, n = \deg Q$. For $|z| = R$ large, $|P(z)| \leq 2|p_d| R^d$ and $|Q(z)| \geq |q_n| R^n/2$. So $|R(z)| = |P/Q| \leq 4|p_d|/|q_n| \cdot R^{d - n} = C/R^{n - d}$ with $C = 4|p_d|/|q_n|$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R(x) = P(x)/Q(x)$ with $\deg Q \geq \deg P + 2$ and $Q$ has no real zeros.
>
> Let $w_1, \ldots, w_m$ be the upper-half-plane zeros of $Q$ (and hence the upper-half-plane poles of $R$). Choose $\rho > 0$ large enough that all $w_i$ satisfy $|w_i| < \rho$.
>
> For $R > \rho$, consider the contour $\Gamma_R = [-R, R] \cup C_R$ traversed counterclockwise, where $C_R$ is the upper semicircle $|z| = R, \operatorname{Im} z \geq 0$. By the [[Thm - Residue Theorem|residue theorem]],
> $$\oint_{\Gamma_R} R(z)\,dz = 2\pi i \sum_{i=1}^m \operatorname{Res}_{w_i} R.$$
>
> **Semicircle bound.** By Lemma 1, $|R(z)| \leq C/R^{\deg Q - \deg P}$ on $|z| = R$ for $R$ large. By the ML estimate,
> $$\left|\int_{C_R} R(z)\,dz\right| \leq \pi R \cdot \frac{C}{R^{\deg Q - \deg P}} = \frac{C\pi}{R^{\deg Q - \deg P - 1}} \to 0 \quad \text{as } R \to \infty,$$
> since $\deg Q - \deg P - 1 \geq 1$.
>
> **Real-axis piece.** $\int_{-R}^R R(x)\,dx = \int_{[-R, R]} R(z)\,dz$ (real and complex integrals coincide on real segments).
>
> **Take the limit.** $\int_{-R}^R R(x)\,dx + \int_{C_R} R(z)\,dz = \oint_{\Gamma_R} R(z)\,dz = 2\pi i \sum_i \operatorname{Res}_{w_i} R$. As $R \to \infty$:
> $$\int_{-\infty}^\infty R(x)\,dx = 2\pi i \sum_{\operatorname{Im} w > 0} \operatorname{Res}_w R. \quad\blacksquare$$
>
> **Variant — use of lower semicircle.** Closing with the lower semicircle (clockwise orientation) gives $\int_{-\infty}^\infty R(x)\,dx = -2\pi i \sum_{\operatorname{Im} w < 0}\operatorname{Res}_w R$. Both formulas give the same answer because the *full* sum of residues (over all poles of $R$, plus the residue at $\infty$) is zero.

---

# Cross-Field Exercise Suggestions

**The classic — $\int dx/(1 + x^2) = \pi$.** Apply with $R(z) = 1/(1 + z^2)$, $\deg Q - \deg P = 2$, upper-half-plane pole at $z = i$ with residue $1/(2i)$. Result: $2\pi i \cdot 1/(2i) = \pi$.

**Generalizing — $\int dx/(1 + x^2)^n = ?$.** Higher-order pole at $z = i$, requires the derivative formula. For $n = 2$: pole of order 2 at $i$; $\operatorname{Res}_i 1/(z^2+1)^2 = -i/4$ (computed in [[Thm - Computing Residues#Cross-Field Exercise Suggestions|computing residues]]). Result: $2\pi i \cdot (-i/4) = \pi/2$.

**Integral with two parameters — $\int dx/((x^2 + a^2)(x^2 + b^2)) = \pi/(ab(a + b))$ for $a, b > 0$.** Simple poles at $\pm ai, \pm bi$; only $ai$ and $bi$ in upper half-plane; partial-fraction-decompose to compute residues, sum.

---

# Bridges

- **[[Thm - Residue Theorem]]** — the engine.

- **[[Thm - Computing Residues]]** — to actually compute the residues at upper-half-plane poles.

- **[[Thm - Jordan's Lemma]]** — extends the technique to oscillatory integrals where the rational decay is insufficient.

- **[[Thm - Trigonometric Integrals via Residues]]** — variant where the contour is the unit circle, not a real-axis-plus-semicircle.

---

# Unlocked by This

> [!tip] Inverse Laplace via Residues *(from Applications)*
> The Bromwich integral $f(t) = (2\pi i)^{-1}\int_{c - i\infty}^{c + i\infty} F(s) e^{st}\,ds$ is exactly an upper-half-plane closure problem (rotated 90°), and the same technique applies: close the contour to the left, apply residues.

> [!tip] Probability — Characteristic Functions *(from Probability Theory)*
> The Fourier-transform of a probability density (the *characteristic function*) often has a meromorphic structure, and inverting via residues gives the original density. Many classical distributions have density-characteristic-function pairs evaluable by this technique.
