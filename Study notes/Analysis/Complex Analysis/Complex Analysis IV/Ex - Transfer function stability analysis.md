---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Transfer Function and Stability"
  - "Def - Laplace Transform"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis, signal-processing]
---

# Problem Statement

Consider the damped harmonic oscillator
$$\ddot y(t) + 2\zeta\omega_0\dot y(t) + \omega_0^2 y(t) = x(t),$$
where $\omega_0 > 0$ is the natural frequency and $\zeta \geq 0$ is the damping ratio. The transfer function is $H(s) = 1/(s^2 + 2\zeta\omega_0 s + \omega_0^2)$.

(a) Find the poles of $H(s)$ as a function of $\zeta$.

(b) Classify the system's stability for $\zeta > 1, \zeta = 1, 0 < \zeta < 1, \zeta = 0, \zeta < 0$.

(c) For $\zeta = 0.1, \omega_0 = 100$ rad/s, compute the impulse response and confirm stability.

**Recall:**

![[Def - Transfer Function and Stability#The Definition]]

Stability: all poles of $H$ in left half-plane $\{\operatorname{Re} s < 0\}$.

---

# Convergent Strategy

**Problem class:** Classify the stability of a 2nd-order linear system by pole location, as a parameter varies.

**Assumption pattern:** Quadratic denominator $s^2 + 2\zeta\omega_0 s + \omega_0^2$ — standard 2nd-order system form. Roots given by the quadratic formula.

**Theorem routing:** Apply the [[Def - Transfer Function and Stability|stability dictionary]]: pole location → stability classification.

**Key decision point:** Compute the roots of the denominator: $s = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$. Behaviour depends on sign of $\zeta^2 - 1$.

---

# Legal Operations Used

1. **Apply the quadratic formula** to find poles of $H$.
2. **Classify pole locations** by real part:
   - $\operatorname{Re} > 0$: unstable.
   - $\operatorname{Re} = 0$: marginally stable (if simple) or unstable (if higher-order).
   - $\operatorname{Re} < 0$: stable.
3. **Compute impulse response** via inverse Laplace.

---

# Hints

> [!note]- Hint 1
> Roots of $s^2 + 2\zeta\omega_0 s + \omega_0^2 = 0$: $s = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$.

> [!note]- Hint 2
> $\zeta > 1$: real distinct roots; $\zeta = 1$: real double root; $0 < \zeta < 1$: complex conjugate roots; $\zeta = 0$: purely imaginary; $\zeta < 0$: real part positive.

> [!note]- Hint 3
> Real part of the roots: $-\zeta\omega_0$ for $|\zeta| \leq 1$; $-\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$ for $|\zeta| > 1$. Stable iff this real part is negative.

---

# Solution

**(a) Poles of $H(s)$**

> [!note]- Derivation
> Denominator: $s^2 + 2\zeta\omega_0 s + \omega_0^2 = 0$.
>
> Quadratic formula: $s = -\zeta\omega_0 \pm \sqrt{\zeta^2\omega_0^2 - \omega_0^2} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$.
>
> Cases:
> - $\zeta > 1$ (overdamped): $\sqrt{\zeta^2 - 1}$ real, two real distinct roots $s_{\pm} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$.
> - $\zeta = 1$ (critically damped): double real root $s = -\omega_0$.
> - $0 < \zeta < 1$ (underdamped): complex conjugate pair $s_\pm = -\zeta\omega_0 \pm i\omega_0\sqrt{1 - \zeta^2}$.
> - $\zeta = 0$ (undamped): purely imaginary $s_\pm = \pm i\omega_0$.
> - $\zeta < 0$: real part positive in some way (depends on $|\zeta|$ vs $1$).

**(b) Stability classification**

> [!note]- Derivation
> Real part of the poles:
> - $\zeta > 1$ (overdamped): real parts are $-\zeta\omega_0 + \omega_0\sqrt{\zeta^2 - 1}$ and $-\zeta\omega_0 - \omega_0\sqrt{\zeta^2 - 1}$. For $\zeta > 1$: $\sqrt{\zeta^2 - 1} < \zeta$ (since $\zeta^2 - 1 < \zeta^2$), so $-\zeta\omega_0 + \omega_0\sqrt{\zeta^2 - 1} < 0$. Both roots in left half-plane. **Stable**.
> - $\zeta = 1$ (critically damped): double root at $-\omega_0 < 0$. Stable (left half-plane).
> - $0 < \zeta < 1$ (underdamped): real parts $-\zeta\omega_0 < 0$. **Stable** with oscillation at frequency $\omega_0\sqrt{1 - \zeta^2}$.
> - $\zeta = 0$ (undamped): poles at $\pm i\omega_0$, on imaginary axis. **Marginally stable** (pure oscillation, $\sin(\omega_0 t)$ response).
> - $\zeta < 0$: real parts positive (or complex with positive real part). **Unstable**.

**(c) Impulse response for $\zeta = 0.1, \omega_0 = 100$**

> [!note]- Derivation
> $\zeta = 0.1 < 1$, underdamped. Poles: $s_\pm = -0.1 \cdot 100 \pm i \cdot 100\sqrt{1 - 0.01} = -10 \pm i \cdot 100 \cdot 0.99499... \approx -10 \pm 99.5i$.
>
> Both poles in the left half-plane (real part $-10 < 0$). System is stable, with damped oscillation at frequency $\omega_d = \omega_0\sqrt{1 - \zeta^2} \approx 99.5$ rad/s, time-decay constant $1/(\zeta\omega_0) = 0.1$ s.
>
> Impulse response (inverse Laplace via residues): partial fractions or direct formula gives
> $$h(t) = \frac{1}{\omega_d}e^{-\zeta\omega_0 t}\sin(\omega_d t) = \frac{1}{99.5}e^{-10 t}\sin(99.5 t) \quad \text{for } t > 0.$$
> Verification: amplitude decays as $e^{-10t}$ (consistent with real part $-10$); frequency $99.5$ rad/s (consistent with imaginary part).

> [!note]- Complete formal solution
> Denominator roots: $s = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$.
>
> Real part of the roots:
> - $|\zeta| < 1$: real part $-\zeta\omega_0$ (negative iff $\zeta > 0$).
> - $\zeta > 1$: real parts $-\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$ (both negative iff $\zeta > 0$).
> - $\zeta < 0$: at least one root has real part $> 0$, hence unstable.
>
> Stability: $\zeta > 0$ gives stable; $\zeta = 0$ marginal; $\zeta < 0$ unstable. The boundary between stable and unstable is the imaginary axis ($\zeta = 0$), with $\zeta > 0$ corresponding to "energy dissipation" and $\zeta < 0$ to "energy injection".
>
> For $\zeta = 0.1, \omega_0 = 100$: poles at $-10 \pm 99.5i$, both in left half-plane. Stable underdamped oscillator with damped frequency $99.5$ rad/s and time decay $1/10 = 0.1$ s. Impulse response: $h(t) = (1/99.5) e^{-10t}\sin(99.5 t)$ for $t > 0$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "transfer function with quadratic denominator" → "compute roots via quadratic formula, classify by real part".** The standard analysis. The discriminant $\zeta^2 - 1$ classifies into overdamped/critical/underdamped, and the real part determines stability.

**The "Bode plot" geometry.** The pole locations in the complex $s$-plane visualize the system:
- Distance from origin: natural frequency $\omega_0$.
- Angle from real axis: $\cos^{-1}(\zeta)$ (real axis = critically damped, vertical = undamped).
- Negative real direction: damping rate $\zeta\omega_0$.
- Imaginary direction: oscillation frequency $\omega_0\sqrt{1 - \zeta^2}$ (for underdamped).

**Engineering interpretations.**
- **Mechanical oscillator** (mass-spring-damper): $m\ddot x + c\dot x + kx = F$. $\omega_0 = \sqrt{k/m}, \zeta = c/(2\sqrt{km})$. Damping ratio $\zeta$ characterizes the energy dissipation per cycle.
- **Electrical RLC circuit**: similar with capacitor, inductor, resistor.
- **Servo control**: closed-loop systems often have 2nd-order behaviour; $\zeta = 0.7$ is a common "fast but not too oscillatory" choice.

**The boundary case $\zeta = 0$ (undamped) is marginally stable.** Poles on imaginary axis give pure oscillation $\sin(\omega_0 t)$, neither growing nor decaying. In practice, real systems always have some damping, so marginal stability is the idealization, not the reality.

**Higher-order systems.** Same principles apply: factor the denominator (FTA gives $n$ roots), examine each root's real part, classify each mode. System is stable iff *all* poles in left half-plane.
