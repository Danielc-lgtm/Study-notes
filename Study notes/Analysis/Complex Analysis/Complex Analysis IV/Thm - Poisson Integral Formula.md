---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Harmonic Function"
  - "Def - Poisson Kernel"
  - "Thm - Mean Value Property of Harmonic Functions"
  - "Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)"
tags: [analysis, complex-analysis, pde]
---

# Notation

$\mathbb{D} = \{|z| < 1\}$, $P_r(\theta) = (1 - r^2)/(1 - 2r\cos\theta + r^2)$ is the Poisson kernel. $u_0 : S^1 \to \mathbb{R}$ is continuous boundary data. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Poisson Integral Formula).** Let $u_0 : S^1 \to \mathbb{R}$ be continuous, and define $u : \mathbb{D} \to \mathbb{R}$ by
> $$u(re^{i\theta}) := \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi)\, u_0(e^{i\phi})\,d\phi, \qquad 0 \leq r < 1,$$
> where $P_r(\psi) = (1 - r^2)/(1 - 2r\cos\psi + r^2)$ is the Poisson kernel. Then $u$ is harmonic on $\mathbb{D}$, extends continuously to $\overline{\mathbb{D}}$, and satisfies $u|_{S^1} = u_0$. Moreover, $u$ is the **unique** harmonic function on $\mathbb{D}$ with continuous extension to $\overline{\mathbb{D}}$ and prescribed boundary values $u_0$.

---

# Motivation

The Poisson integral formula solves the **Dirichlet problem on the unit disc**: given continuous boundary values $u_0 : S^1 \to \mathbb{R}$, find a harmonic function $u : \overline{\mathbb{D}} \to \mathbb{R}$ continuous up to the boundary with $u|_{S^1} = u_0$.

The mean value property tells us that *at the centre* $z = 0$, $u(0) = $ average of $u_0$. The Poisson integral generalizes this: $u(re^{i\theta}) = $ a *weighted* average of $u_0$, with weight $P_r(\theta - \phi)/(2\pi)$ at the boundary point $e^{i\phi}$.

This is one of the most useful results in classical analysis. It gives:
- *Existence* of harmonic extension of any continuous boundary data.
- *Uniqueness* (combined with the maximum principle).
- An explicit *integral representation* of harmonic functions on the disc.
- A reproducing kernel for the Hardy space $H^2(\mathbb{D})$.

Combined with conformal mapping (Riemann mapping theorem), the Poisson integral solves the Dirichlet problem on *any* simply connected domain.

---

# Sources and Targets

**Sources (Input Broadening)**

**Continuous boundary data $u_0 : S^1 \to \mathbb{R}$.** Standard hypothesis.

**$L^1$ boundary data.** More general: $u_0 \in L^1(S^1)$. The Poisson integral still defines a harmonic function on $\mathbb{D}$, but boundary values are recovered in a weaker (non-tangential, $L^1$) sense.

**Distribution boundary data.** Even more general: $u_0$ a distribution on $S^1$. The Poisson integral makes sense via the Fourier series interpretation, and gives a harmonic function with boundary values in the distributional sense.

**Targets (Output Amplification)**

Combine with **Riemann mapping.** Property $D$: $\phi : U \to \mathbb{D}$ a biholomorphism. Amplified result $E$: solve Dirichlet on $U$ by pulling back the Poisson integral on $\mathbb{D}$ via $\phi$. See [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].

Combine with **harmonic measure.** Property $D$: $z \in \mathbb{D}$. Amplified result $E$: $P_r(\theta - \phi)/(2\pi) d\phi$ is the harmonic measure at $z = re^{i\theta}$ — the probability distribution of the exit point of a Brownian motion starting from $z$.

Combine with **Hardy space reproducing kernel.** Property $D$: $H^2(\mathbb{D})$ Hilbert space of boundary $L^2$ functions extending to holomorphic. Amplified result $E$: the Poisson kernel is the reproducing kernel, $f(z) = \langle f, K_z\rangle$ for $K_z$ built from the Poisson kernel.

---

# Why Is It True

The proof has two parts: (1) the formula defines a harmonic function on $\mathbb{D}$; (2) it has the correct boundary values.

**Part 1: Poisson integral is harmonic.** The Poisson kernel $P_r(\theta - \phi)$ is harmonic in $z = re^{i\theta}$ for each fixed $\phi$ (it is the real part of the holomorphic Möbius factor $(e^{i\phi} + z)/(e^{i\phi} - z)$). The integral of a harmonic function against $u_0$ is harmonic, provided we can interchange the integral and the Laplacian (which is fine for continuous $u_0$ and the smooth Poisson kernel).

**Part 2: Boundary values are $u_0$.** Need to show $u(re^{i\theta}) \to u_0(e^{i\theta})$ as $r \to 1^-$. This is the key technical step. Using the fact that $P_r$ is a *positive*, *normalized* kernel (integrating to $2\pi$) that *concentrates* at $\theta = 0$ as $r \to 1^-$, the convolution $P_r \star u_0$ converges to $u_0$ at every continuity point. (This is a standard "approximation to identity" argument.)

Together, these prove the Poisson integral solves the Dirichlet problem on $\mathbb{D}$.

**Uniqueness** follows from the maximum principle: any two harmonic extensions of $u_0$ have the same boundary values, so their difference is harmonic with zero boundary values, hence zero by max/min principle.

---

# What Makes This Hard

The non-obvious step is the **boundary-value-recovery argument**. The kernel $P_r$ has both positivity, normalization, and concentration as $r \to 1$, and these three properties combine to make $P_r \star u_0 \to u_0$. The concentration is the most subtle: $P_r(\theta)$ becomes very peaked at $\theta = 0$ as $r \to 1$, and most of the integral comes from boundary values very close to $\theta_0$ (the point where $z = re^{i\theta_0}$ is approaching the boundary). The uniform boundedness of $u_0$ on $S^1$ + continuity at $\theta_0$ gives the pointwise convergence.

A common mistake is to apply the formula carelessly to discontinuous $u_0$, expecting recovery of $u_0$ at jump discontinuities. The recovery is at *continuity points*; at jumps, the limit is the *average* of the left and right limits.

---

# Rederivation Scaffold

**High-level strategy:**
The Poisson integral is harmonic by the harmonicity of $P_r$ in $z$. Boundary values are recovered using the concentrating + positive + normalized properties of $P_r$ as $r \to 1$.

**Subgoal decomposition:**

1. **Harmonicity of Poisson kernel in $z$.** $P_r(\theta - \phi) = \operatorname{Re}\frac{e^{i\phi} + re^{i\theta}}{e^{i\phi} - re^{i\theta}}$, real part of a Möbius transformation of $z = re^{i\theta}$, hence harmonic.

2. **Define $u(z) := \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi) u_0(e^{i\phi})\,d\phi$ for $z = re^{i\theta}$.** Harmonic by interchange.

3. **Boundary value recovery.** $\lim_{r \to 1^-} u(re^{i\theta_0}) = u_0(e^{i\theta_0})$ at continuity points.

4. **Uniqueness.** Two harmonic extensions of the same boundary data agree, by max principle on their difference.

---

# Lemma Decomposition

> [!note]- Lemma 1: Poisson kernel is harmonic in $z$ for fixed $\phi$
> **Statement:** For each $\phi \in [0, 2\pi)$, the function $P_r(\theta - \phi)$ (in $z = re^{i\theta}$) is harmonic on $\mathbb{D}$.
>
> > [!note]- Full proof
> > Write $P_r(\theta - \phi) = \operatorname{Re}\frac{e^{i\phi} + re^{i\theta}}{e^{i\phi} - re^{i\theta}} = \operatorname{Re}\frac{e^{i\phi} + z}{e^{i\phi} - z}$ (where $z = re^{i\theta}$). The function $z \mapsto (e^{i\phi} + z)/(e^{i\phi} - z)$ is holomorphic on $\mathbb{D}$ (no pole at $|z| < 1$ since the pole is at $z = e^{i\phi}$ on the boundary). Its real part is harmonic.

> [!note]- Lemma 2: Approximation to the identity
> **Statement:** Let $u_0 : S^1 \to \mathbb{R}$ be continuous. Then $u(re^{i\theta}) = (P_r \star u_0)(\theta)/(2\pi) \to u_0(e^{i\theta})$ as $r \to 1^-$, uniformly in $\theta$.
>
> **Hint:** Use positivity, normalization, and concentration of $P_r$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $u_0 : S^1 \to \mathbb{R}$ be continuous, and define
> $$u(re^{i\theta}) := \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi) u_0(e^{i\phi})\,d\phi$$
> for $0 \leq r < 1$.
>
> **Step 1: $u$ is harmonic on $\mathbb{D}$.** By Lemma 1, $P_r(\theta - \phi)$ is harmonic in $z = re^{i\theta}$ for each fixed $\phi$. Differentiating under the integral (legal by dominated convergence and smoothness of $P_r$): $\Delta u = (1/(2\pi))\int_0^{2\pi}(\Delta_z P_r(\theta - \phi))u_0(e^{i\phi})\,d\phi = 0$.
>
> **Step 2: Boundary values.** By Lemma 2 (approximation to the identity), $u(re^{i\theta}) \to u_0(e^{i\theta})$ as $r \to 1^-$, uniformly in $\theta$. So $u$ extends continuously to $\overline{\mathbb{D}}$ with $u|_{S^1} = u_0$.
>
> **Step 3: Uniqueness.** Suppose $\tilde u$ is another harmonic function on $\mathbb{D}$, continuous on $\overline{\mathbb{D}}$ with $\tilde u|_{S^1} = u_0$. Then $v = u - \tilde u$ is harmonic on $\mathbb{D}$, continuous on $\overline{\mathbb{D}}$ with $v|_{S^1} = 0$. By the [[Thm - Maximum Principle for Harmonic Functions|maximum and minimum principles]] (and the fact that $v$ achieves max on the closed disc by compactness), $\max v = \max_{S^1} v = 0$ and $\min v = 0$, so $v \equiv 0$. Hence $u = \tilde u$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Specific Dirichlet problem.** Boundary data $u_0(e^{i\phi}) = \cos(2\phi)$. The Poisson integral gives $u(re^{i\theta}) = r^2\cos(2\theta)$. Check via the formula or recognize $u = \operatorname{Re}(z^2) = r^2\cos(2\theta)$. See [[Ex - Solving Laplace's equation on a disc]].

**Step boundary data.** $u_0(e^{i\phi}) = 1$ for $\phi \in (0, \pi)$, $0$ otherwise. The Poisson integral gives a harmonic function with a known closed form involving $\arctan$.

**Conformal pullback.** Dirichlet problem on the half-plane $\mathbb{H}$: map $\mathbb{H}$ to $\mathbb{D}$ via $z \mapsto (z - i)/(z + i)$, transfer boundary data, apply Poisson on $\mathbb{D}$, pull back. See [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].

**Harmonic measure interpretation.** The Poisson kernel $P_r(\theta - \phi)/(2\pi)$ is the density of the exit distribution of a Brownian motion starting at $re^{i\theta}$ from $\mathbb{D}$. The Poisson integral $u = $ expectation of $u_0$ at the exit point — a probabilistic representation of the Dirichlet problem.

---

# Bridges

- **[[Def - Poisson Kernel]]** — the kernel.

- **[[Def - Harmonic Function]]** — the object being constructed.

- **[[Thm - Mean Value Property of Harmonic Functions]]** — special case at the centre.

- **[[Thm - Maximum Principle for Harmonic Functions]]** — used for uniqueness.

- **[[Thm - Riemann Mapping Theorem (Statement)]]** — combined with Poisson to solve Dirichlet on any simply connected domain.

---

# Unlocked by This

> [!tip] Hardy Spaces *(from Functional Analysis)*
> The Poisson kernel is the reproducing kernel of the Hardy space $H^2(\mathbb{D})$.

> [!tip] Brownian Motion and Potential Theory *(from Probability)*
> The probabilistic representation $u(z) = \mathbb{E}_z[u_0(B_\tau)]$ connects harmonic functions to Brownian motion.

> [!tip] Plurisubharmonic Functions and Several Complex Variables *(from Several Complex Variables)*
> The Poisson kernel and its multidimensional analogs are foundational in pluripotential theory.
