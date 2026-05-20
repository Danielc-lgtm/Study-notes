---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Laplace Transform"
  - "Def - Removable Singularity, Pole, Essential Singularity"
tags: [analysis, complex-analysis, signal-processing]
---

# Notation

$h(t) : [0, \infty) \to \mathbb{R}$ is the **impulse response** of a linear time-invariant (LTI) system. $H(s) : \mathbb{C} \to \mathbb{C}$ is the **transfer function**, $H(s) = \mathcal{L}\{h\}(s)$. Poles of $H$ are points $s_k \in \mathbb{C}$ where $H$ blows up. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

A **linear time-invariant (LTI) system** is one whose response to inputs is linear (scaling and adding inputs scales and adds outputs) and time-invariant (shifting an input in time shifts the output by the same amount). Examples: a passive RLC circuit, a damped harmonic oscillator, a Bessel filter, a low-pass audio filter. These are ubiquitous in engineering.

The system is fully characterized by its **impulse response** $h(t)$: the output when the input is a Dirac delta $\delta(t)$. For an arbitrary input $x(t)$, the output is $y(t) = (h \star x)(t) = \int_0^t h(t - \tau) x(\tau)\,d\tau$ — convolution with $h$.

Convolution in time corresponds to multiplication in the Laplace transform domain: $Y(s) = H(s) X(s)$ where $H = \mathcal{L}\{h\}$, $X = \mathcal{L}\{x\}$, $Y = \mathcal{L}\{y\}$. The transfer function $H(s)$ encodes all the system's behaviour, *as a function of the complex frequency $s$*.

Why is this representation useful? Because $H(s)$ is a *meromorphic* function on $\mathbb{C}$, with isolated poles, and the geometry of those poles classifies the system's behaviour:

**Stability.** The system is stable (bounded inputs give bounded outputs) iff $h(t) \to 0$ as $t \to \infty$. For an LTI system whose transfer function has finitely many poles, this is equivalent to: all poles $s_k$ satisfy $\operatorname{Re} s_k < 0$ (left half-plane). The reason: each pole $s_k$ contributes a mode $e^{s_k t}$ to the impulse response (by the inverse Laplace formula and the residue theorem), which decays iff $\operatorname{Re} s_k < 0$.

**Marginal stability.** Poles on the imaginary axis ($\operatorname{Re} s = 0$) give modes $e^{i\omega t}$ — pure oscillation, neither growing nor decaying. The system response stays bounded but doesn't return to zero.

**Instability.** Any pole in the right half-plane gives a growing mode $e^{s_k t}$ with $\operatorname{Re} s_k > 0$, hence unbounded response.

This is the *true name* of stability in linear systems: **all poles in the left half-plane**. It is a finite-dimensional, easy-to-check condition that classifies the qualitative behaviour of a system in one geometric statement.

The complex analysis underlying this: the inverse Laplace transform formula $h(t) = (1/(2\pi i))\int_{c - i\infty}^{c + i\infty}H(s) e^{st}\,ds$, evaluable by residue theorem (close the contour to the left for $t > 0$), gives $h(t) = \sum_k \operatorname{Res}_{s_k}[H(s) e^{s_k t}]$. Each pole contributes a term involving $e^{s_k t}$, and the sign of $\operatorname{Re} s_k$ determines decay or growth.

---

# The Definition

For a linear time-invariant (LTI) system with impulse response $h : [0, \infty) \to \mathbb{R}$ (or $\mathbb{C}$):

**Transfer function.** $H(s) := \mathcal{L}\{h\}(s) = \int_0^\infty h(t) e^{-st}\,dt$, holomorphic on a half-plane $\{\operatorname{Re} s > c\}$, often extending meromorphically to a larger region.

**Stability classification.**
- The system is **stable** (or BIBO-stable, "bounded input, bounded output") if all poles of $H$ lie in the open left half-plane $\{\operatorname{Re} s < 0\}$.
- The system is **marginally stable** if all poles have $\operatorname{Re} s \leq 0$ and poles with $\operatorname{Re} s = 0$ are simple (higher-order poles on the imaginary axis give polynomial growth, not just oscillation, and are usually classified as unstable).
- The system is **unstable** if any pole has $\operatorname{Re} s > 0$ (or any pole on the imaginary axis is of order $\geq 2$).

**Modal decomposition.** For a rational $H(s) = P(s)/Q(s)$ with $Q$ having simple roots $s_1, \ldots, s_n$ in the left half-plane and $\deg Q > \deg P$, the impulse response decomposes as
$$h(t) = \sum_{k=1}^n \operatorname{Res}_{s_k}[H(s) e^{st}] = \sum_{k=1}^n \frac{P(s_k)}{Q'(s_k)} e^{s_k t}.$$
The system response is a sum of modal exponentials $e^{s_k t}$.

---

# Relate to Other Fields / Compression

In **electrical engineering**, transfer functions describe the input-output relation of circuits, filters, and amplifiers. The poles of an RLC circuit's transfer function are at specific frequencies (determined by component values), and pole geometry determines whether the circuit is a stable amplifier, an oscillator, or an unstable runaway.

In **mechanical engineering**, the transfer function of a mass-spring-damper system $m\ddot x + c\dot x + kx = F(t)$ is $H(s) = 1/(ms^2 + cs + k)$. Poles at $s = (-c \pm \sqrt{c^2 - 4mk})/(2m)$. For positive $m, c, k$: real part is $-c/(2m) < 0$, so the system is always stable (poles in left half-plane). The oscillation frequency is $\operatorname{Im}(s) = \sqrt{4mk - c^2}/(2m)$.

In **control theory**, the **Nyquist criterion** uses the argument principle (applied to $1 + H(s)$) to determine closed-loop stability from the open-loop transfer function. The **root locus** is the geometry of how the poles move as a feedback gain varies, also analyzed using complex-analytic ideas.

In **quantum mechanics**, the Green's function $G(E) = 1/(E - H)$ of a quantum system is a holomorphic-in-$E$ resolvent, with poles at the eigenvalues. The pole positions are the energy spectrum.

In **economics** (time-series analysis), the AR(p) and ARMA(p, q) models have transfer functions $1/(1 - \phi_1 z - \phi_2 z^2 - \ldots - \phi_p z^p)$ in the Z-transform domain. Stationarity requires all poles outside the unit disc.

---

# Examples / Corollaries

**Is an instance — first-order system $\dot y + a y = x$.** Transfer function $H(s) = 1/(s + a)$, pole at $s = -a$. Stable iff $a > 0$.

**Is an instance — damped harmonic oscillator $\ddot y + 2\zeta\omega_0 \dot y + \omega_0^2 y = x$.** Transfer function $H(s) = 1/(s^2 + 2\zeta\omega_0 s + \omega_0^2)$. Poles at $s = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$. 
- $\zeta > 1$ (overdamped): two real poles in left half-plane. Stable.
- $\zeta = 1$ (critically damped): double pole at $-\omega_0$. Stable.
- $0 < \zeta < 1$ (underdamped): complex conjugate poles at $-\zeta\omega_0 \pm i\omega_0\sqrt{1 - \zeta^2}$ in left half-plane. Stable, with oscillation.
- $\zeta = 0$ (undamped): poles at $\pm i\omega_0$ on imaginary axis. Marginally stable (pure oscillation).
- $\zeta < 0$: poles in right half-plane. Unstable.

**Is an instance — integrator $\dot y = x$.** Transfer function $H(s) = 1/s$, pole at $s = 0$ on imaginary axis. Marginally stable (integrates inputs; bounded input gives bounded output asymptotically, but doesn't decay).

**Is an instance — pure delay $y(t) = x(t - T)$.** Transfer function $H(s) = e^{-sT}$. Entire function (no poles), so trivially stable. But not rational.

**Calibration check — bandpass filter.** A $2$nd-order bandpass filter with centre frequency $\omega_0 = 100$ rad/s and quality factor $Q = 10$ has poles at $s = -\omega_0/(2Q) \pm i\omega_0\sqrt{1 - 1/(4Q^2)}$. Substituting: $-100/(20) \pm i 100\sqrt{1 - 1/400} = -5 \pm i \cdot 99.94 \ldots$. Both poles in the left half-plane (real part $-5 < 0$), so stable. The imaginary part is approximately $\omega_0$, confirming the bandpass at $\sim$100 rad/s. See [[Ex - Bandpass filter design via pole placement]].

---

# Unlocked by This

> [!tip] Inverse Laplace and Residues *(from §3.4 and Applications)*
> The time-domain response is recovered by [[Ex - Inverse Laplace via residues|inverse Laplace transform via residues]].

> [!tip] Stability Analysis *(from Applications)*
> [[Ex - Transfer function stability analysis]] applies the pole-location dictionary to classify systems.

> [!tip] Filter Design *(from Applications)*
> [[Ex - Bandpass filter design via pole placement]] designs a 2nd-order filter by placing poles in the left half-plane at desired frequencies.

> [!tip] Nyquist Stability Criterion *(from Control Theory)*
> The **Nyquist criterion** uses the argument principle ($\oint H'/H$) on a Nyquist contour to count right-half-plane poles of $1 + L(s)H(s)$ for feedback systems. It is the workhorse of frequency-domain control design.
