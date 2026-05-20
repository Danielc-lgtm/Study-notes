---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Transfer Function and Stability"
  - "Def - Laplace Transform"
  - "Thm - Computing Residues"
  - "Ex - Transfer function stability analysis"
tags: [analysis, complex-analysis, signal-processing]
---

# Problem Statement

Design a 2nd-order bandpass filter with centre frequency $\omega_0 = 100$ rad/s and quality factor $Q = 10$. Specifically:

(a) Determine the pole locations of the transfer function.

(b) Verify the system is stable (poles in left half-plane).

(c) Write down the transfer function $H(s)$.

(d) Compute the impulse response $h(t)$ via inverse Laplace.

(e) Interpret the design choice physically: how do the parameters $\omega_0$ and $Q$ control the filter's behaviour?

**Recall:**

![[Def - Transfer Function and Stability#The Definition]]

For a 2nd-order bandpass, the transfer function has the form $H(s) = (\omega_0/Q)s/(s^2 + (\omega_0/Q)s + \omega_0^2)$, with poles at $-\omega_0/(2Q) \pm i\omega_0\sqrt{1 - 1/(4Q^2)}$ (for $Q > 1/2$).

---

# Convergent Strategy

**Problem class:** Engineering design problem: given desired filter specifications, find the transfer function. Demonstrates the *inverse* direction of stability analysis — *placing* poles to achieve a desired response.

**Assumption pattern:** $\omega_0 = 100$ rad/s (centre frequency where the filter passes the signal); $Q = 10$ (quality factor, $Q = \omega_0/$bandwidth — higher $Q$ means narrower passband).

**Theorem routing:** The poles are at $-\omega_0/(2Q) \pm i\omega_0\sqrt{1 - 1/(4Q^2)}$ for the 2nd-order bandpass. With $Q = 10$: real part $= -100/20 = -5$, imaginary part $= 100\sqrt{1 - 1/400} = 100\sqrt{0.9975} \approx 99.875$.

**Key decision point:** The pole locations encode the filter's behaviour. Real part $-5$: damping (decay rate $5$ Hz, or time constant $1/5 = 0.2$ s). Imaginary part $\approx 100$: resonant frequency (close to $\omega_0$). Both negative real ⟹ stable.

---

# Legal Operations Used

1. **Compute pole locations** from the 2nd-order bandpass formula.
2. **Verify stability** by checking the real part is negative.
3. **Write the transfer function** in factored form: $H(s) = (\omega_0/Q)s/((s - s_+)(s - s_-))$ where $s_\pm$ are the poles.
4. **Compute the impulse response** via inverse Laplace and partial fractions.

---

# Hints

> [!note]- Hint 1
> 2nd-order bandpass: $H(s) = (\omega_0/Q)s/(s^2 + (\omega_0/Q)s + \omega_0^2)$. Poles satisfy $s^2 + (\omega_0/Q)s + \omega_0^2 = 0$.

> [!note]- Hint 2
> Quadratic formula: $s = -\omega_0/(2Q) \pm \sqrt{(\omega_0/(2Q))^2 - \omega_0^2} = -\omega_0/(2Q) \pm \omega_0\sqrt{1/(4Q^2) - 1}$.
>
> For $Q > 1/2$ (underdamped — usual case): the term under the square root is negative, giving complex conjugate poles $-\omega_0/(2Q) \pm i\omega_0\sqrt{1 - 1/(4Q^2)}$.

> [!note]- Hint 3
> With $\omega_0 = 100, Q = 10$: real part $-100/20 = -5$. Imaginary part $100\sqrt{1 - 1/400} = 100\sqrt{0.9975} \approx 99.875$.

> [!note]- Hint 4
> Both poles have real part $-5 < 0$. Stable.

---

# Solution

**(a) Pole locations**

> [!note]- Derivation
> The 2nd-order bandpass transfer function has the form
> $$H(s) = \frac{(\omega_0/Q) s}{s^2 + (\omega_0/Q) s + \omega_0^2}.$$
> Poles solve $s^2 + (\omega_0/Q) s + \omega_0^2 = 0$, i.e., $s = -\omega_0/(2Q) \pm \omega_0 \sqrt{1/(4Q^2) - 1}$.
>
> Substituting $\omega_0 = 100, Q = 10$:
> - Real part: $-\omega_0/(2Q) = -100/20 = -5$.
> - Discriminant: $1/(4Q^2) - 1 = 1/400 - 1 = -0.9975$.
> - Imaginary part: $\omega_0\sqrt{|\text{disc}|} = 100\sqrt{0.9975} \approx 99.875$.
>
> Poles: $s_\pm = -5 \pm i \cdot 99.875$ rad/s.

**(b) Stability**

> [!note]- Derivation
> Both poles have real part $-5 < 0$, so both are in the left half-plane. The system is **stable**.
>
> Specifically: the impulse response will decay like $e^{-5t}$ (time constant $\tau = 1/5 = 0.2$ s).

**(c) Transfer function**

> [!note]- Derivation
> $$H(s) = \frac{(\omega_0/Q) s}{s^2 + (\omega_0/Q)s + \omega_0^2} = \frac{10 s}{s^2 + 10 s + 10000}.$$
> Factored form: $H(s) = (10s)/((s + 5 - 99.875i)(s + 5 + 99.875i))$.

**(d) Impulse response**

> [!note]- Derivation
> $h(t) = \mathcal{L}^{-1}\{H(s)\}(t)$ for $t > 0$.
>
> Partial fractions or residue calculation: $h(t) = \sum_{\text{poles}}\operatorname{Res}[H(s) e^{st}]$.
>
> At $s = s_+ = -5 + 99.875i$: $\operatorname{Res}_{s_+}[H(s) e^{st}] = (10 s_+ e^{s_+ t})/(s_+ - s_-)$. With $s_+ - s_- = 2 \cdot 99.875 i = 199.75 i$:
> $$\operatorname{Res}_{s_+} = \frac{10 \cdot (-5 + 99.875i) e^{(-5 + 99.875i)t}}{199.75 i}.$$
>
> At $s = s_- = -5 - 99.875i$: analogous, with complex conjugate.
>
> Summing the two and simplifying: $h(t) = (10/\omega_d)e^{-5t}\left[\omega_d\cos(\omega_d t) - 5\sin(\omega_d t)\right]$ where $\omega_d = 99.875$.
>
> Equivalently: $h(t) = 10 e^{-5t}\left[\cos(\omega_d t) - (5/\omega_d)\sin(\omega_d t)\right] \approx 10 e^{-5t}\cos(99.875 t)$ for $t > 0$ (the correction from the $5/\omega_d \approx 0.05$ term is small for high-$Q$ filters).

**(e) Physical interpretation**

> [!note]- Derivation
> **$\omega_0 = 100$ rad/s** is the *centre frequency* — the frequency at which the filter has maximum gain. Equivalently, the imaginary part of the pole ($\approx 99.875$) is very close to $\omega_0$.
>
> **$Q = 10$** is the *quality factor*, equal to $\omega_0/\Delta\omega$ where $\Delta\omega$ is the bandwidth (the width of the passband). Higher $Q$:
> - Narrower passband (more selective).
> - Slower decay of impulse response (rings longer).
> - Pole locations closer to the imaginary axis (less damping).
>
> For $Q = 10$: bandwidth $\approx \omega_0/Q = 10$ rad/s, time constant $1/5 = 0.2$ s. So the filter rings at $\approx 100$ rad/s for about $5$ to $10$ cycles before damping out.
>
> **Trade-off**: higher $Q$ = better frequency selectivity but slower transient response. Typical audio filters have $Q \sim 1$; resonant systems (laser cavities, quartz crystals) have $Q \gg 10^6$.

> [!note]- Complete formal solution
> **Pole locations.** For a 2nd-order bandpass with $\omega_0, Q$: $s = -\omega_0/(2Q) \pm i\omega_0\sqrt{1 - 1/(4Q^2)}$. With $\omega_0 = 100, Q = 10$: $s = -5 \pm 99.875i$.
>
> **Stability.** Real part $-5 < 0$, both poles in left half-plane. Stable.
>
> **Transfer function.** $H(s) = 10s/(s^2 + 10s + 10000)$.
>
> **Impulse response.** $h(t) = 10 e^{-5t}\cos(99.875 t)$ for $t > 0$ (approximately; exact formula has a small correction).
>
> **Interpretation.** Filter rings at $\omega_0 = 100$ rad/s, with envelope decay $e^{-5t}$. Passband bandwidth $\Delta\omega \approx 10$ rad/s (centred at $\omega_0$). Q-factor $= 10$ means the filter passes a narrow band around $\omega_0$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "design a filter with specifications" → "place poles in $s$-plane".** Filter design is *inverse* analysis: given desired frequency response, determine the transfer function (equivalently, the pole/zero locations). The Q-factor and centre frequency directly determine pole placement: pole at $-\omega_0/(2Q) + i\omega_0\sqrt{1 - 1/(4Q^2)}$ (with conjugate).

**Pole-zero placement geometry.**
- **Poles** in left half-plane = stable. Closer to imaginary axis = higher Q, less damping.
- **Zeros** affect the passband shape (e.g., a zero at $s = 0$ for high-pass filters; zeros at $s = \pm i\omega_0$ for notch filters).
- **Distance from imaginary axis** $= $ damping rate (real part magnitude).
- **Distance from origin** $\approx \omega_0$ $= $ resonant frequency.

**Bode plot interpretation.** For a 2nd-order bandpass, the magnitude $|H(i\omega)|$:
- At $\omega = 0$: $|H| = 0$ (zero at origin).
- At $\omega = \omega_0$: $|H| = $ maximum $= 1$ (for the normalization above).
- At $\omega \to \infty$: $|H| \to 0$.
- Bandwidth $\Delta\omega = \omega_0/Q$.

**Higher-order filters.** $n$-pole filters (Butterworth, Chebyshev, Elliptic) place poles on specific curves in the $s$-plane:
- **Butterworth**: poles equally spaced on a circle, maximally flat passband.
- **Chebyshev**: poles on an ellipse, steeper roll-off but ripples in passband.
- **Elliptic**: optimal in transition bandwidth, but ripples in both bands.

All are constructed by *placing poles* (and zeros for Elliptic) to optimize a specific criterion.

**Quartz crystal oscillators.** Have $Q \sim 10^4$ to $10^6$, with poles extremely close to the imaginary axis. Used in clocks, radios, GPS systems. The high Q gives extremely stable frequency reference.

**Numerical filter design tools.** MATLAB's `butter`, `cheby1`, `cheby2`, `ellip` functions all implement pole-placement-based filter design. Python's `scipy.signal` package has equivalents. The theory is exactly the complex analysis of transfer-function poles.
