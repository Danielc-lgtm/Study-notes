---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Morera's Theorem"
  - "Thm - Cauchy's Theorem for a Disc"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ open; $[a, b] \subseteq \mathbb{R}$; $\varphi : D \times [a, b] \to \mathbb{C}$ continuous, with $\varphi(\cdot, s) : D \to \mathbb{C}$ holomorphic for each $s \in [a, b]$. Define $g(z) := \int_a^b \varphi(z, s)\,ds$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

Many functions in complex analysis are defined by integrals depending on a complex parameter:
- $\Gamma(z) = \int_0^\infty t^{z - 1} e^{-t}\,dt$ for $\operatorname{Re} z > 0$;
- Fourier-type integrals $\int_{-\infty}^\infty e^{izt} f(t)\,dt$;
- Cauchy-type integrals $\int_\gamma g(w)/(w - z)\,dw$ for $z$ off the contour.

To use complex analysis on these, we need to know they are *holomorphic* in the parameter. This theorem provides the standard sufficient condition: if the integrand is continuous in $(z, s)$ and holomorphic in $z$ for each $s$, the integral is holomorphic in $z$.

The proof uses Morera's theorem and Fubini: swap integration over the triangle (in $z$) with integration over $[a, b]$ (in $s$), each interior triangle integral vanishes by Cauchy, so the outer integral vanishes, Morera concludes holomorphicity.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$\varphi$ continuous on $D \times [a, b]$, holomorphic in $z$ for each $s$".

The first disguised source is **a Cauchy-type integral** $g(z) = \int_\gamma f(w)/(w - z)^{n+1}\,dw$ for $z$ off the contour: $\varphi(z, s) = f(\gamma(s))\gamma'(s)/(\gamma(s) - z)^{n+1}$ is continuous in $(z, s)$ (denominator bounded below) and holomorphic in $z$ (no $\bar z$). So Cauchy-type integrals depend holomorphically on the parameter — the engine of CIF + higher-derivative CIF.

The second disguised source is **a power-series-defined integral**: $g(z) = \int_a^b e^{zs} f(s)\,ds$ (Laplace-type). $\varphi(z, s) = e^{zs} f(s)$ is continuous and holomorphic in $z$. So Laplace transforms are holomorphic in their parameter.

**Targets (Output Amplification)**

The conclusion is "$g$ is holomorphic on $D$".

Combine with **the derivative formula.** Property $D$: $\partial \varphi/\partial z$ continuous in $(z, s)$. The amplified result: $g'(z) = \int_a^b (\partial \varphi/\partial z)(z, s)\,ds$ — differentiation under the integral. This is the explicit derivative formula needed for many computations.

---

# Why Is It True

Show $g$ has vanishing triangle integrals. For any triangle $\Delta \subseteq D$:
$$\int_\Delta g(z)\,dz = \int_\Delta \int_a^b \varphi(z, s)\,ds\,dz = \int_a^b \int_\Delta \varphi(z, s)\,dz\,ds$$
by Fubini (legitimate since $\varphi$ is continuous on the compact $\Delta \times [a, b]$, hence bounded, hence absolutely integrable). For each fixed $s$, $\varphi(\cdot, s)$ is holomorphic on $D$, hence on a star-shaped region containing $\Delta$ (e.g., a small disc), so $\int_\Delta \varphi(z, s)\,dz = 0$ by Goursat. Therefore $\int_\Delta g(z)\,dz = 0$.

Also $g$ is continuous on $D$ (since $\varphi$ is uniformly continuous on compacts of $D \times [a, b]$). By [[Thm - Morera's Theorem]], $g$ is holomorphic on $D$.

For the derivative formula: $g'(z) = \int_a^b (\partial \varphi/\partial z)(z, s)\,ds$ follows from differentiating the equation $g(z) = \int \varphi\,ds$ via Fubini + standard difference-quotient bounds (uniform on compact subsets). Cambridge IB notes this is on an example sheet.

---

# What Makes This Hard

The non-obvious technical step is *Fubini's theorem* to swap the orders of integration — over the triangle and over $[a, b]$. The justification uses continuity of $\varphi$ on the compact $\Delta \times [a, b]$, which gives uniform continuity, in turn giving the swap. The proof is otherwise mechanical.

---

# Rederivation Scaffold

**High-level strategy:**
For any triangle in $D$, swap $\int_\Delta \int_a^b = \int_a^b \int_\Delta$ via Fubini. The inner $\int_\Delta$ vanishes by Cauchy on each $\varphi(\cdot, s)$. So all triangle integrals of $g$ vanish; by Morera, $g$ holomorphic.

**Subgoal decomposition:**

1. **$g$ is continuous on $D$.** Uniform continuity of $\varphi$ on compacts.

2. **Triangle integral of $g$ vanishes.** Fubini + Cauchy on $\varphi(\cdot, s)$.

3. **Morera concludes $g$ holomorphic.**

---

# Lemma Decomposition

> [!note]- Lemma 1: Fubini-style swap for continuous integrands
> **Statement:** Let $\phi : [a, b] \times [c, d] \to \mathbb{C}$ be continuous. Then $\int_a^b \int_c^d \phi(t, s)\,ds\,dt = \int_c^d \int_a^b \phi(t, s)\,dt\,ds$.
>
> > [!note]- Full proof
> > Cambridge Lemma 2.5.5: by uniform continuity of $\phi$ on the compact $[a, b] \times [c, d]$, $\phi$ is a uniform limit of step functions; for step functions the identity is direct; pass to the uniform limit. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We show $g$ is continuous and has vanishing triangle integrals, then apply Morera.
>
> **Continuity.** $\varphi$ continuous on $D \times [a, b]$, hence on any compact $K \times [a, b]$ with $K \subseteq D$ compact, hence uniformly continuous. For $z, z_0 \in K$: $|g(z) - g(z_0)| \leq \int_a^b |\varphi(z, s) - \varphi(z_0, s)|\,ds \leq (b - a) \cdot \sup_s |\varphi(z, s) - \varphi(z_0, s)| \to 0$ as $z \to z_0$ (by uniform continuity).
>
> **Triangle integrals.** Fix a triangle $\Delta \subseteq D$. By Lemma 1 (Fubini for continuous integrands on compact sets; for the triangle parametrized as a piecewise $C^1$ curve, the same swap applies):
> $$\int_\Delta g(z)\,dz = \int_\Delta \int_a^b \varphi(z, s)\,ds\,dz = \int_a^b \int_\Delta \varphi(z, s)\,dz\,ds.$$
> For each $s \in [a, b]$, $\varphi(\cdot, s)$ is holomorphic on $D$, hence on a star-shaped neighbourhood of $\Delta$ (e.g., a disc containing $\Delta$). By [[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat]], $\int_\Delta \varphi(z, s)\,dz = 0$. So $\int_\Delta g(z)\,dz = 0$.
>
> By [[Thm - Morera's Theorem]], $g$ is holomorphic on $D$. $\blacksquare$
>
> **Derivative formula.** With more work (uniform-in-$s$ control of the difference quotient $(\varphi(z + h, s) - \varphi(z, s))/h$), $g'(z) = \int_a^b (\partial \varphi/\partial z)(z, s)\,ds$.

---

# Cross-Field Exercise Suggestions

**Higher-derivative CIF revisited.** $f^{(n)}(w) = (n!/2\pi i)\oint f(z)/(z - w)^{n+1}\,dz$ — this is "$f^{(n)}$ is a holomorphic-parameter integral", with $\varphi(w, z) = f(z)/(z - w)^{n+1}$. The theorem confirms $w \mapsto $ integral is holomorphic in $w$.

**The Gamma function is holomorphic.** $\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\,dt$ is holomorphic for $\operatorname{Re}(z) > 0$. The integrand $t^{z-1}e^{-t} = e^{(z-1)\log t - t}$ is holomorphic in $z$, continuous in $(z, t)$ on $\{\operatorname{Re} z > 0\} \times (0, \infty)$. The integral converges absolutely and uniformly on compacts of $\{\operatorname{Re} z > 0\}$. Modifying the theorem statement for improper integrals (need to verify uniform convergence at the endpoints) gives the holomorphy.

**Fourier-type integrals.** $\hat f(\xi) = \int e^{-i\xi x} f(x)\,dx$ — for $f$ with compact support, the integrand is holomorphic in $\xi$, hence $\hat f$ extends to an entire function on $\mathbb{C}$. This is the source of Paley–Wiener theorems characterizing compactly supported functions by the behaviour of their Fourier transforms in the complex plane.

---

# Bridges

- **[[Thm - Morera's Theorem]]** — the bridge from triangle vanishing to holomorphicity.

- **[[Thm - Goursat's Theorem (Cauchy for a Triangle)]]** — used inside the proof for $\varphi(\cdot, s)$.

- **[[Thm - Cauchy Integral Formula]]** — itself an instance: $f(w)$ depends holomorphically on $w$ via the Cauchy integral.

- **[[Ex - Continuity from Morera (specific instance)]]** — an exercise applying this idea.
