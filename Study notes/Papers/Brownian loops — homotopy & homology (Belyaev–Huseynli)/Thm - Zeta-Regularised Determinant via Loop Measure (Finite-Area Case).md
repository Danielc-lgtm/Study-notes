---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Borthwick–Judge–Perry Determinant Formula"
  - "Thm - Selberg Zeta Identity (Killing Case)"
  - "Def - Renormalised Integral and the 0-Trace"
tags: [paper, spectral-geometry, determinants, renormalisation]
---

# Notation

- $X$ — a geometrically finite hyperbolic surface of **finite area**, with $n_C$ cusps and Euler characteristic $\chi=\chi(X)$
- $M$, $F$, $D_X(s)$, $C_X$ — the constants and correction of [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]]
- $\kappa\geq0$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so $s(s-1)=\kappa$ and $\Delta_X-s(1-s)=\Delta_X+\kappa$
- $\det_0$ — the [[Def - Renormalised Integral and the 0-Trace|renormalised determinant]]
- $Z_X$, $Z'_X(1)$ — the Selberg zeta function and its derivative at $s=1$

---

# Type card

> [!abstract] Type card — Theorem 5.7 (determinant via loop measure, finite-area case)
> **Given.** A geometrically finite hyperbolic surface $X$ of finite area with $n_C$ cusps and Euler characteristic $\chi$; the constants $M$, $F$ and the function $D_X(s)$ of [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]]; and $\kappa\geq0$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so that $s(s-1)=\kappa$ and $\Delta_X-s(1-s)=\Delta_X+\kappa$.
>
> **Produces.** An identity expressing $-\log\det_0(\Delta_X+\kappa)$ through the total killing loop mass plus explicit topological terms; and, in the $\kappa\to0^+$ limit after dividing out the simple zero, the closed form $\log\det_0\Delta_X=\log C_X+\log Z'_X(1)$.
>
> **Lets you.** Run the entire §5 programme when the Laplacian has continuous spectrum and the heat semigroup is not trace class — so that a cusped surface, which by [[Thm - Finiteness of the Total Mass|Corollary 4.7]] has divergent Brownian total mass, still yields a well-defined determinant and hence a normalisable measure in §6.

---

# Statement

> **Theorem 5.7 (zeta-regularised determinant via Brownian loop measure, finite-area case).** Let $X$ be a geometrically finite hyperbolic surface of finite area, with $n_C$ cusps and Euler characteristic $\chi=\chi(X)$, and let $M$, $F$, $D_X(s)$ be as in Theorem 5.5. For $\kappa\geq0$, write $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so that $s(s-1)=\kappa$ and $\Delta_X-s(1-s)=\Delta_X+\kappa$. Then
> $$-\log\det{}_0(\Delta_X+\kappa) = F\kappa - M + \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) - D_X(s).\tag{67}$$
> Since $0$ lies in the spectrum of $\Delta_X$, the determinant of $\Delta_X$ itself is recovered by dividing out the simple zero,
> $$\det{}_0\Delta_X := \lim_{s\to1}\frac{\det_0\big(\Delta_X-s(1-s)\big)}{s(s-1)}.$$
> As $\kappa\to0^+$ this gives
> $$\log\det{}_0\Delta_X = M + D_X(1) + \log Z'_X(1) = \log C_X + \log Z'_X(1),\tag{68}$$
> where $D_X(1)=-\chi\log(2\pi)-n_C\log\big(\sqrt{2\pi}\big)$ and $C_X$ is as in Theorem 5.5.

---

# Why it is true

A substitution and a limit, and both have already been set up.

**The substitution.** [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]], taken in logarithmic form (65), says
$$-\log\det{}_0\big(\Delta_X-s(1-s)\big) = -Fs(1-s)-M-\log Z_X(s)-D_X(s),$$
in which the only non-elementary term is $-\log Z_X(s)$. And [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] says exactly what that term is: the total mass of the killing loop measure. Substituting, and using $s(1-s)=-\kappa$, gives (67). **Everything that is not the loop mass in (67) is a function of $\kappa$, $\chi$ and $n_C$ alone.**

**The limit.** This is the same mechanism as in [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]], and recognising it as the same mechanism is the efficient way to read §5. Since $\mathrm{Area}(X)<\infty$, $\lambda_0=0$ is in the spectrum, so $Z_X$ has a **simple zero at $s=1$**:
$$Z_X(s)=Z'_X(1)(s-1)+O\big((s-1)^2\big)\quad\Longrightarrow\quad -\log Z_X(s) = -\log Z'_X(1)-\log(s-1)+O(s-1).$$
So the total mass diverges as $\kappa\to0^+$, and it diverges by exactly $-\log(s-1)$. Meanwhile, dividing by $s(s-1)$ to form $\det_0\Delta_X$ subtracts $\log(s(s-1))$ from the log-determinant, and $s(s-1)=\kappa$ with $s-1\sim\kappa$ as $\kappa\to0^+$. **The two logarithms cancel.** With $F\kappa\to0$ and $D_X(s)\to D_X(1)$, what survives is (68).

**The mechanism in one line: the $\log$-divergence of the total loop mass as the killing rate goes to zero is exactly the simple zero of $Z_X$ at $s=1$ that the eigenvalue $\lambda_0=0$ creates, and dividing that zero out of the determinant cancels it.**

Note that the whole content is a cancellation of two divergences that have a *common origin*: both come from $\lambda_0=0$. That is why the renormalisation is forced rather than chosen — there is exactly one zero to divide out and exactly one divergence to cancel.

---

# Strategy

**Strategy.** Substitute the Corollary 4.3 identity $-\log Z_X(s)=\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ into the logarithm (65) of the Borthwick–Judge–Perry factorisation, using $s(1-s)=-\kappa$; then take the limit by expanding $Z_X(s)=Z'_X(1)(s-1)+O((s-1)^2)$ and observing that dividing by $s(s-1)=\kappa$ subtracts a $\log(s-1)$ that cancels the divergence, since $s-1\sim\kappa$.

> [!note]- Proof (skippable)
> Substituting $-\log Z_X(s)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ into (65) and using $s(1-s)=-\kappa$ gives
> $$-\log\det{}_0(\Delta_X+\kappa) = F\kappa - M + \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) - D_X(s),$$
> which is (67).
>
> For the limit: $\mathrm{Area}(X)<\infty$ forces a simple zero $Z_X(s)=Z'_X(1)(s-1)+O((s-1)^2)$, so
> $$-\log Z_X(s) = -\log Z'_X(1)-\log(s-1)+O(s-1).$$
> Dividing by $s(s-1)$ subtracts $\log\big(s(s-1)\big)$ from $\log\det_0(\Delta_X-s(1-s))$; since $s(s-1)=\kappa$ and $s-1\sim\kappa$ as $\kappa\to0^+$, the resulting $-\log(s-1)$ cancels the divergence in $-\log Z_X(s)$. Together with $F\kappa\to0$, $D_X(s)\to D_X(1)$, and $D_X(1)=\log C_X-M$, this yields (68). $\;\square$

---

# What this assumes, and where to climb

**Theorem 5.5** — [[Thm - Borthwick–Judge–Perry Determinant Formula]], quoted wholesale, together with its own dependence on the Barnes $G$-function and on the meromorphic continuation of $Z_X$.

**Corollary 4.3** — [[Thm - Selberg Zeta Identity (Killing Case)]], and through it the whole §3 apparatus. This is the paper's own contribution to the theorem; everything else is imported.

**The renormalised determinant** — [[Def - Renormalised Integral and the 0-Trace]], which is what $\det_0$ means, and [[Def - Eisenstein Series and the Continuous Spectrum]], which is why it is needed.

**Finite area, hence $\lambda_0=0$ in the spectrum, hence a simple zero of $Z_X$ at $s=1$.** This is a genuine hypothesis, not a convenience. In the infinite-area case $0$ is not an $L^2$ eigenvalue, $Z_X(1)\neq0$, there is no zero to divide out, and no limit to take. See Remark 5.8 below.

**$s>1$**, so that $\kappa\geq0$ and the corollary's convergence hypothesis $s>\delta=1$ holds. At $\kappa=0$ exactly, the total mass diverges — the limit is one-sided.

> [!note] Remark 5.8 — the infinite-area case
> When $\mathrm{Area}(X)=\infty$ one has $\delta<1$, so by [[Thm - Finiteness of the Total Mass|Corollary 4.7]] the total mass of subordinate Brownian loop measure is **already finite** and no renormalisation is required. The determinant identity then holds directly at $s=1$, because $0$ is not an $L^2$ eigenvalue and $Z_X(1)\neq0$. The corresponding expression for $-\log\det_0\Delta_X$ via the loop mass and the resonance divisor of $Z_X$ is Lemonde–Wang's, and is recoverable from Theorem 5.5. A Polyakov conformal anomaly formula for non-compact surfaces also exists in the literature.

---

# What consumes this

Nothing downstream in the paper; §6 runs on [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] directly rather than on any §5 result.

The theorem's role is to complete the coverage: together with [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] and Remark 5.8, every geometrically finite hyperbolic surface now has its determinant expressed through loop masses — closed, cusped-finite-area, and infinite-area.

---

# Reading it against the rest of the paper

The parallel with Theorem 5.1(ii) is exact and worth stating, because it makes §5 much shorter to hold in mind. **In both cases:** a killing rate $\kappa>0$ makes the total mass finite; an imported spectral result (Naud's formula there, Borthwick–Judge–Perry here) expresses the log-determinant in terms of quantities the paper controls; Corollary 4.3 substitutes the loop mass for $-\log Z_X(s)$; and the $\kappa\to0^+$ limit works because a $\log\kappa$ cancels against the simple zero of $Z_X$ at $s=1$ created by $\lambda_0=0$. The results even have the same shape: $\log\det=\text{(explicit constant)}+\log Z'_X(1)$, with the constant $\mathrm{Area}(X)E$ in the compact case and $\log C_X$ here.

What differs is only which spectral machinery is imported to get there, and that difference is forced by the spectrum: discrete and trace-class in one case, continuous and not in the other.
