---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Harmonic Function"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis, pde]
---

# Notation

$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ is the open unit disc, $S^1 = \partial\mathbb{D} = \{|z| = 1\}$ is the unit circle. We parametrize $S^1$ by $e^{i\phi}$ for $\phi \in [0, 2\pi)$ and points in $\mathbb{D}$ by $re^{i\theta}$ with $0 \leq r < 1$. The Poisson kernel is $P_r(\theta)$, sometimes written $P(r, \theta)$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

We want to solve the **Dirichlet problem on the unit disc**: given continuous boundary data $u_0 : S^1 \to \mathbb{R}$, find a harmonic function $u : \overline{\mathbb{D}} \to \mathbb{R}$ with $u|_{S^1} = u_0$.

We know harmonic functions exist (any holomorphic function's real part is harmonic), and we know the maximum principle forces uniqueness: two harmonic extensions of the same boundary data must agree (their difference is harmonic with zero boundary values, hence zero by maximum/minimum principle). What we need is *existence*: given $u_0$, construct $u$.

The natural guess: $u$ should be a *weighted average* of the boundary values. The weight at each boundary point $e^{i\phi}$ should depend on how "close" the interior point $z = re^{i\theta}$ is to $e^{i\phi}$ — closer means more weight. The mean value property says that *at the centre* $z = 0$, the weight is uniform: $u(0) = (1/(2\pi))\int u_0(e^{i\phi})\,d\phi$. For non-central $z$, the weight should be biased toward boundary points near $z$.

The Poisson kernel $P_r(\theta - \phi)$ is the unique such weight that makes the formula work:
$$u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi) u_0(e^{i\phi})\,d\phi$$
defines a harmonic function with continuous boundary values $u_0$.

What does $P_r(\theta)$ look like? Three properties forced on it:
1. Positivity: weights should be non-negative.
2. Normalization: integral over the circle = $2\pi$ (so the result has the right "average" character).
3. Concentration: as $r \to 1^-$, the weight $P_r(\theta - \phi)$ should concentrate at $\phi = \theta$ (the boundary point closest to $z = re^{i\theta}$), so the integral converges to $u_0(e^{i\theta})$ — recovering the boundary value.

The Poisson kernel is the unique positive function satisfying (a) the mean value property (integral = $2\pi$, recovery of central value when $r = 0$), (b) the concentration property as $r \to 1$, and (c) harmonicity in $z$ for fixed $\phi$. Computing: the harmonic function $h_w(z) = \operatorname{Re}((w + z)/(w - z))$ for $|w| = 1$ has the right boundary behaviour, and setting $w = e^{i\phi}, z = re^{i\theta}$ extracts $P_r(\theta - \phi)$.

What would break with a different kernel? Without the harmonicity property, the integral wouldn't give a harmonic function. Without concentration, the integral wouldn't recover the boundary values. Without normalization, the formula would be off by a factor. The Poisson kernel is forced by these three constraints.

---

# The Definition

Let $0 \leq r < 1$ and $\theta \in \mathbb{R}$.

The **Poisson kernel** for the unit disc is
$$P_r(\theta) = \frac{1 - r^2}{1 - 2r\cos\theta + r^2}.$$

**Equivalent formulations.**

1. **Real part of a Möbius factor.** $P_r(\theta) = \operatorname{Re}\left(\frac{1 + re^{i\theta}}{1 - re^{i\theta}}\right) = \operatorname{Re}\left(\frac{e^{i\theta} + r e^{i\cdot 0}}{e^{i\theta} - r e^{i\cdot 0}}\cdot\frac{e^{-i\theta/2}}{e^{-i\theta/2}}\right)$ (and similar manipulations).

2. **Fourier series.** $P_r(\theta) = \sum_{n=-\infty}^\infty r^{|n|} e^{in\theta} = 1 + 2\sum_{n=1}^\infty r^n \cos(n\theta)$.

3. **In terms of complex variables.** For $z = re^{i\theta}, w = e^{i\phi}$ (with $|z| < 1, |w| = 1$):
$$P_r(\theta - \phi) = \operatorname{Re}\frac{w + z}{w - z} = \frac{|w|^2 - |z|^2}{|w - z|^2} = \frac{1 - r^2}{|e^{i\phi} - re^{i\theta}|^2}.$$
(The last expression uses $|w - z|^2 = (w - z)\overline{(w - z)} = |w|^2 - w\bar z - z\bar w + |z|^2 = 1 - 2r\cos(\theta - \phi) + r^2$.)

**Properties.**
- **Positive:** $P_r(\theta) \geq 0$ (and $> 0$ except at degenerate cases). Numerator $1 - r^2 > 0$ for $r < 1$; denominator $1 - 2r\cos\theta + r^2 = (1 - r)^2 + 2r(1 - \cos\theta) \geq (1 - r)^2 > 0$.
- **Normalized:** $\int_0^{2\pi} P_r(\theta)\,d\theta = 2\pi$.
- **Symmetric:** $P_r(-\theta) = P_r(\theta)$.
- **Concentrates at $\theta = 0$ as $r \to 1^-$:** $P_r(0) = (1 + r)/(1 - r) \to \infty$, and the mass concentrates on a shrinking neighborhood of $\theta = 0$.
- **Harmonic in $z = re^{i\theta}$ for fixed $\phi$:** $\Delta_z P_r(\theta - \phi) = 0$.

---

# Relate to Other Fields / Compression

In **probability**, the Poisson kernel $P_r(\theta - \phi)/(2\pi)$ is the **density of the harmonic measure** at the boundary point $e^{i\phi}$ as seen from the interior point $re^{i\theta}$. Equivalently, it is the density of the exit distribution of a Brownian motion started at $re^{i\theta}$ from the disc. Higher density at $e^{i\phi}$ means a Brownian motion starting from $re^{i\theta}$ is more likely to exit near $e^{i\phi}$.

In **harmonic analysis**, the Poisson kernel is the convolution kernel that converts boundary functions to harmonic extensions. It is the analog (for the disc and Laplace's equation) of the heat kernel (for the half-plane and the heat equation): both are positive, normalized, concentrating kernels solving the respective PDE.

In **electromagnetism**, the Poisson kernel gives the steady-state potential inside a charged conducting cylinder: given a boundary potential $u_0(\phi)$, the potential at interior point $re^{i\theta}$ is $\int P_r(\theta - \phi)u_0(\phi)\,d\phi/(2\pi)$. This is one of the original physical motivations for the kernel.

In **operator theory**, the Poisson kernel implements the **harmonic extension operator** $E : C(S^1) \to H(\mathbb{D})$ (where $H$ denotes harmonic). Its $L^2$ version is the orthogonal projection onto the subspace of harmonic functions, and the kernel is the reproducing kernel of the Hardy space $H^2(\mathbb{D})$.

---

# Examples / Corollaries

**$P_0(\theta) = 1$.** At $r = 0$ (centre of disc), the kernel is constant $1$. So $u(0) = (1/(2\pi))\int u_0(e^{i\phi})\,d\phi$ — the mean value property. The Poisson kernel reduces to the uniform measure at the centre.

**$P_r(\theta)$ peaks at $\theta = 0$.** For fixed $r$, $P_r$ is maximized at $\theta = 0$ (closest boundary point to the interior point at angle $\theta_0 = 0$), with value $P_r(0) = (1 + r)/(1 - r)$. This grows without bound as $r \to 1$.

**$P_r(\theta) \to 0$ for $\theta \neq 0$ as $r \to 1$.** For fixed $\theta \neq 0$, the denominator stays bounded away from zero, and the numerator $1 - r^2 \to 0$, so $P_r(\theta) \to 0$. Combined with concentration at $\theta = 0$: $P_r$ converges (weakly) to $2\pi\delta_0$ as $r \to 1$.

**Fourier series interpretation.** $P_r(\theta) = \sum_{n\in\mathbb{Z}}r^{|n|}e^{in\theta}$, so the Poisson integral of a Fourier series $u_0(e^{i\phi}) = \sum_n a_n e^{in\phi}$ is $u(re^{i\theta}) = \sum_n a_n r^{|n|} e^{in\theta}$. The "Poisson extension" sends $a_n e^{in\phi}$ to $r^{|n|}a_n e^{in\theta} = a_n z^n$ for $n \geq 0$ and $a_n \bar z^{-n}$ for $n < 0$. Holomorphic and anti-holomorphic parts.

**Boundary values $u_0 =$ Heaviside (step).** $u_0(e^{i\phi}) = 1$ for $\phi \in (0, \pi)$, $0$ otherwise. The Poisson integral gives a harmonic function $u$ inside the disc with these boundary values. The result is $u(re^{i\theta}) = \arg(\text{something})/\pi$ — a function involving the argument, related to the Cayley transform.

**Sanity check — at $r = 0$, $u(0) =$ average of $u_0$.** $u(0\cdot e^{i\theta}) = (1/(2\pi))\int u_0(e^{i\phi}) P_0(\theta - \phi)\,d\phi = (1/(2\pi))\int u_0(e^{i\phi})\,d\phi$ — the mean of $u_0$, as expected.

**Sanity check — concentration as $r \to 1$.** For $u_0$ continuous, $\lim_{r \to 1^-} u(re^{i\theta}) = u_0(e^{i\theta})$ pointwise. This is the recovery of boundary values from the harmonic extension.

**Calibration check.** Verify that $P_0(\theta) = 1$ identically, so the Poisson formula at the centre reduces to the mean value property — the Poisson kernel is the deformation of the uniform measure that biases toward boundary points near the interior evaluation point. Verify $\int_0^{2\pi} P_r(\theta)\,d\theta = 2\pi$ (normalisation), which is what makes the Poisson integral a weighted *average*. And verify that as $r \to 1^-$, $P_r$ concentrates as a Dirac delta at $\theta = 0$ — $P_r(0) \to \infty$ while $P_r(\theta) \to 0$ for $\theta \neq 0$ — so the Poisson integral *recovers* boundary values in the limit.

---

# Unlocked by This

> [!tip] Poisson Integral Formula *(from §3.6+)*
> The [[Thm - Poisson Integral Formula|Poisson integral formula]] uses this kernel to solve the Dirichlet problem on the disc.

> [!tip] Harmonic Measure *(from Probability/Potential Theory)*
> The Poisson kernel is the density of the harmonic measure, a measure-theoretic interpretation linking complex analysis to probability and potential theory.

> [!tip] Reproducing Kernels in Hardy Spaces *(from Functional Analysis)*
> The Poisson kernel is the reproducing kernel for the Hardy space $H^2(\mathbb{D})$ of holomorphic $L^2$ functions on the disc, a foundational object in operator theory and signal processing.

> [!tip] Boundary Value Problems on Other Domains *(from Applied Math)*
> Combined with conformal mapping (Riemann mapping or explicit maps), the Poisson kernel solves boundary value problems on *any* simply connected domain — see [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].
