---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis, signal-processing]
---

# Notation

$f : [0, \infty) \to \mathbb{R}$ (or $\mathbb{C}$) is a function defined on the non-negative reals; $s \in \mathbb{C}$ is the complex transform variable. The Laplace transform is $F(s) = \mathcal{L}\{f\}(s)$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

The Laplace transform converts functions of time $t \in [0, \infty)$ into functions of a complex frequency $s \in \mathbb{C}$. Its motivation has three threads:

**Engineering motivation: solving linear ODEs with initial conditions.** A differential equation like $f''(t) + 3f'(t) + 2f(t) = 0$ with $f(0) = a, f'(0) = b$ is hard to attack directly but trivial after Laplace transform: it becomes the algebraic equation $(s^2 + 3s + 2)F(s) =$ (terms involving initial conditions), which solves for $F(s)$, and then $f(t)$ is recovered by inverse transform. The Laplace transform converts calculus on $[0, \infty)$ to algebra on $\mathbb{C}$.

**Function-theoretic motivation: meromorphic extension and pole structure.** The integral $F(s) = \int_0^\infty f(t) e^{-st}\,dt$ converges absolutely in a half-plane $\{\operatorname{Re} s > c\}$ for some real $c$ (the "abscissa of convergence"), and gives a holomorphic function there. Typically, $F$ extends meromorphically to a larger region, with the poles encoding the *modes* of $f$ (e.g., $f(t) = e^{-t}$ has Laplace transform $1/(s + 1)$, with a pole at $s = -1$, encoding the exponential decay rate).

**Probabilistic motivation: $F(s)$ as expectation of $e^{-sT}$ for $T$ a random time.** The Laplace transform $F(s) = \mathbb{E}[e^{-sT}]$ where $T$ has density $f$ is the **moment generating function** in disguise, evaluated at $-s$. Many probability calculations reduce to Laplace transforms.

The kernel $e^{-st}$ is chosen because:
- It is the *unique* function that converts differentiation in $t$ to multiplication in $s$: $\mathcal{L}\{f'\}(s) = s F(s) - f(0)$. The factor $e^{-st}$ is needed because $d/dt[e^{-st}] = -s e^{-st}$, so integration by parts produces a clean $s F(s)$.
- It decays rapidly for $\operatorname{Re} s > 0$, large $t$, making the integral converge even for $f$ growing like $e^{at}$.
- It is the analog of $e^{-i\omega t}$ in the Fourier transform (with $s = i\omega$), so Laplace generalizes Fourier.

What would break with a different kernel? Using $e^{-st^2}$ would give the Weierstrass-style transform, useful but with different algebraic properties. Using $1/(s + t)$ would give the Stieltjes transform. Each transform is engineered for a specific purpose; $e^{-st}$ is the one that diagonalizes the differentiation operator $d/dt$.

---

# The Definition

For $f : [0, \infty) \to \mathbb{C}$ (or $\mathbb{R}$) suitably integrable, the **Laplace transform** is
$$F(s) = \mathcal{L}\{f\}(s) := \int_0^\infty f(t) e^{-st}\,dt$$
for $s \in \mathbb{C}$ such that the integral converges absolutely.

**Domain of convergence.** If $|f(t)| \leq M e^{ct}$ for some $M, c$ (exponential growth bound), then the integral converges absolutely for $\operatorname{Re} s > c$, defining a holomorphic $F$ on the half-plane $\{\operatorname{Re} s > c\}$. The infimum of such $c$ is the **abscissa of convergence**.

**Analytic continuation.** $F$ typically extends meromorphically (or even holomorphically) to a larger region of $\mathbb{C}$, with isolated poles where the "modes" of $f$ live.

**Bromwich inverse formula.** If $f$ has Laplace transform $F$, then for $t > 0$,
$$f(t) = \frac{1}{2\pi i}\int_{c - i\infty}^{c + i\infty} F(s) e^{st}\,ds,$$
where the integral is along a vertical line $\operatorname{Re} s = c$ with $c$ greater than the abscissa of convergence. In practice, this is evaluated by *closing the contour* — to the left for $t > 0$ — and applying the residue theorem to sum residues of $F(s) e^{st}$ at all poles in the closed contour.

---

# Relate to Other Fields / Compression

The Laplace transform is the analog of the **Fourier transform** $\hat f(\omega) = \int_{-\infty}^\infty f(t) e^{-i\omega t}\,dt$, but for functions on $[0, \infty)$ instead of $\mathbb{R}$. The Fourier transform integrates against $e^{-i\omega t}$ (purely imaginary exponent); the Laplace transform against $e^{-st}$ (general complex exponent). Substituting $s = i\omega$ in the Laplace transform recovers (a piece of) the Fourier transform.

In **algebraic structure**, the Laplace transform is a ring homomorphism (well, an algebra homomorphism over $\mathbb{C}$) from the convolution algebra on $[0, \infty)$ to the pointwise multiplication algebra of holomorphic functions: $\mathcal{L}\{f \star g\} = \mathcal{L}\{f\}\cdot\mathcal{L}\{g\}$. Convolution is hard; pointwise multiplication is trivial. The transform "diagonalizes" convolution.

In **control theory**, the Laplace transform of a system's **impulse response** is the **transfer function**. The stability of the system is read off the pole locations of the transfer function: left half-plane ($\operatorname{Re} s < 0$) = stable, right half-plane = unstable.

In **probability**, the Laplace transform $\hat\mu(s) = \int_0^\infty e^{-st}\,d\mu(t)$ for a positive measure $\mu$ is the **moment generating function** (for negative $s$), or more generally the *Laplace–Stieltjes transform*. It uniquely determines the measure: two distinct measures have distinct Laplace transforms.

In **partial differential equations**, the Laplace transform is the workhorse for solving initial-boundary value problems on the half-line. Applied to time, it converts the PDE in $(t, x)$ into an ODE in $x$ (at each $s$), solvable by standard methods, then invert.

---

# Examples / Corollaries

**Is an instance — $f(t) = 1$.** $F(s) = \int_0^\infty e^{-st}\,dt = 1/s$ for $\operatorname{Re} s > 0$. Pole at $s = 0$.

**Is an instance — $f(t) = e^{at}$.** $F(s) = \int_0^\infty e^{(a - s)t}\,dt = 1/(s - a)$ for $\operatorname{Re} s > \operatorname{Re} a$. Pole at $s = a$.

**Is an instance — $f(t) = t^n$ for $n \geq 0$ integer.** $F(s) = n!/s^{n+1}$ for $\operatorname{Re} s > 0$. Pole of order $n + 1$ at $s = 0$.

**Is an instance — $f(t) = \sin(\omega t)$.** $F(s) = \omega/(s^2 + \omega^2)$ for $\operatorname{Re} s > 0$. Poles at $s = \pm i\omega$ (simple).

**Is an instance — $f(t) = \cos(\omega t)$.** $F(s) = s/(s^2 + \omega^2)$ for $\operatorname{Re} s > 0$. Poles at $s = \pm i\omega$.

**Operational rules (key for problem-solving).**
- Linearity: $\mathcal{L}\{af + bg\} = aF + bG$.
- Derivative: $\mathcal{L}\{f'\}(s) = sF(s) - f(0)$.
- Higher derivative: $\mathcal{L}\{f^{(n)}\}(s) = s^n F(s) - s^{n-1}f(0) - \ldots - f^{(n-1)}(0)$.
- Shift: $\mathcal{L}\{f(t - t_0) H(t - t_0)\}(s) = e^{-st_0}F(s)$ (where $H$ is the Heaviside step).
- Exponential modulation: $\mathcal{L}\{e^{at}f(t)\}(s) = F(s - a)$.
- Scaling: $\mathcal{L}\{f(\lambda t)\}(s) = (1/\lambda)F(s/\lambda)$.
- Convolution: $\mathcal{L}\{f \star g\}(s) = F(s)G(s)$, where $(f \star g)(t) = \int_0^t f(t - \tau)g(\tau)\,d\tau$.

**Calibration check — solving $f'' + f = 0, f(0) = 0, f'(0) = 1$ via Laplace.** Apply $\mathcal{L}$: $s^2 F(s) - s\cdot 0 - 1 + F(s) = 0$, so $F(s) = 1/(s^2 + 1)$. Inverting: $f(t) = \sin t$.

---

# Unlocked by This

> [!tip] Transfer Functions and Stability *(from Signal Processing)*
> The Laplace transform of an impulse response is the [[Def - Transfer Function and Stability|transfer function]]. Pole geometry classifies system stability.

> [!tip] Inverse Laplace via Residues *(from §3.4 and CA IV applications)*
> The Bromwich integral is evaluable by closing the contour and applying [[Thm - Residue Theorem|residues]] — see [[Ex - Inverse Laplace via residues]].

> [!tip] Mellin and Mellin–Barnes Transforms *(from Number Theory)*
> The Mellin transform $M\{f\}(s) = \int_0^\infty f(t) t^{s-1}\,dt$ is a variant of the Laplace transform with a power-law kernel. It is the foundation of analytic number theory and zeta-function theory.

> [!tip] Generating Functions *(from Combinatorics)*
> The discrete analog of the Laplace transform is the **Z-transform** $X(z) = \sum_{n=0}^\infty x_n z^{-n}$, and the generating function $\sum x_n z^n$. Both are Laurent-series-like objects whose pole structure encodes the asymptotic behaviour of the sequence.
