---
type: corollary
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Prime Geodesic Theorem"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
  - "Ex - The Four Bernstein Functions of the Paper"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 4.7"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a geometrically finite hyperbolic surface with critical exponent $\delta \in (0, 1]$.
- $\mathcal P_X$ — the set of primitive oriented closed geodesics of $X$; lengths $\ell_\gamma$; $\ell_{\mathrm{sys}} := \min_\gamma \ell_\gamma$ the **systole** (length of the shortest closed geodesic).
- $C_X(\gamma^m)$ — the free homotopy class winding $m$ times around $\gamma$; $L := m\ell_\gamma$.
- $\phi : (0,\infty) \to (0,\infty)$ — a Bernstein function; the paper works with four concrete cases (Brownian $\phi = \lambda$; killed $\phi = \lambda + \kappa$; $\alpha$-stable $\phi = \lambda^{\alpha/2}$; shifted stable $\phi = (\lambda + \kappa)^{\alpha/2}$).
- $\mu^\phi_X$ — the $\phi$-subordinate loop measure on $X$.
- $s(\phi) \in \mathbb R$ — the **spectral parameter** attached to $\phi$: $s = 1$ for Brownian and $\alpha$-stable; $s = \frac12 + \sqrt{\tfrac14 + \kappa}$ for killed and shifted stable.
- $C(\phi) > 0$ — the multiplicative constant in the canonical class-mass shape: $C = 1$ for Brownian and killed; $C = \alpha/2$ for $\alpha$-stable and shifted stable.
- $N_X(R) := \#\{\gamma \in \mathcal P_X : \ell_\gamma \le R\}$ — the primitive geodesic counting function.

> [!recall]- Hyperbolic surface $X = \Gamma\backslash\mathbb H^2$
> **Formally:** $\mathbb H^2 = \{x + iy : y > 0\}$ with metric $ds^2 = (dx^2 + dy^2)/y^2$; $\Gamma$ a discrete torsion-free subgroup of $\mathrm{PSL}(2, \mathbb R)$; $X = \Gamma\backslash\mathbb H^2$ the quotient hyperbolic surface. Geometrically finite: a technical bound on complexity that includes both compact surfaces and infinite-area surfaces with a finite number of geometric ends.
> **In words:** upper half-plane with curved ruler, quotiented by a discrete symmetry group; the result is a curved surface with a nontrivial global shape.
> **Concretely:** the flat torus $T^2 = \mathbb R^2/\mathbb Z^2$ is the Euclidean model; hyperbolic examples include compact genus-$g$ surfaces ($g \ge 2$; finite area, $\delta = 1$) and funnel surfaces (infinite area, $\delta < 1$). Full detail: [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].

> [!recall]- Critical exponent $\delta$ (the proliferation rate)
> **Formally:** $\delta := \inf\{s > 0 : \sum_{h \in \Gamma} e^{-s\,d(z, hz)} < \infty\}$, independent of $z \in \mathbb H^2$. Equivalent descriptions: the Hausdorff dimension of the limit set of $\Gamma$ on $\partial\mathbb H^2$; the topological entropy of the geodesic flow. $\delta = 1$ for finite-area surfaces; $\delta < 1$ for infinite-area geometrically finite ones.
> **In words:** a single number measuring how fast the orbit $\Gamma z$ accumulates near the ideal boundary — equivalently, by the prime geodesic theorem below, how fast closed geodesics of length $\le R$ multiply as $R$ grows.
> **Concretely:** for a compact genus-2 surface, $\delta = 1$; for a "3-funnel sphere" (a sphere with three infinite-area trumpets), $\delta$ can be tuned continuously in $(0, 1)$ by adjusting the funnel widths; a very thin funnel gives $\delta$ close to $0$, wide funnels give $\delta$ close to $1$. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Prime geodesic theorem: $N_X(R) \sim e^{\delta R}/(\delta R)$
> **Formally:** as $R \to \infty$, $N_X(R) := \#\{\gamma \in \mathcal P_X : \ell_\gamma \le R\}$ satisfies $N_X(R) \sim \frac{e^{\delta R}}{\delta R}$; i.e. $\lim_{R \to \infty} N_X(R) \cdot \frac{\delta R}{e^{\delta R}} = 1$.
> **In words:** the count of primitive closed geodesics of length $\le R$ grows exponentially at exact rate $\delta$, with a $1/R$ correction that exactly mirrors the $1/\log x$ correction in the prime number theorem $\pi(x) \sim x/\log x = e^{\log x}/\log x$. Length plays the role of "log of a prime" and $\delta$ sets the exponential rate.
> **Concretely:** on a finite-area surface ($\delta = 1$): $N_X(10) \approx e^{10}/10 \approx 2200$ geodesics of length up to $10$; $N_X(20) \approx e^{20}/20 \approx 2.4 \times 10^7$. On an infinite-area surface with $\delta = 1/2$: $N_X(10) \approx 2e^5/10 \approx 30$. The exponential rate makes the geodesics multiply overwhelmingly fast; the sum $\sum_\gamma e^{-s\ell_\gamma}$ then converges iff $s$ beats $\delta$. Full detail: [[Thm - Prime Geodesic Theorem]].

> [!recall]- Canonical shape $\mu^\phi_X(C_X(\gamma^m)) = \frac{C}{m}\cdot\frac{e^{(1-s)L}}{e^L - 1}$
> **Formally:** for each of the paper's four Bernstein functions, the $\phi$-subordinate class-mass has the closed form $\mu^\phi_X(C_X(\gamma^m)) = \frac{C(\phi)}{m}\cdot\frac{e^{(1-s(\phi))L}}{e^L - 1}$ with $L = m\ell_\gamma$: $(C, s) = (1, 1)$ (Brownian), $(C, s) = (1, \frac12 + \sqrt{\tfrac14 + \kappa})$ (killed), $(C, s) = (\alpha/2, 1)$ ($\alpha$-stable), $(C, s) = (\alpha/2, \frac12 + \sqrt{\tfrac14 + \kappa})$ (shifted stable).
> **In words:** all four class-masses studied in §3.1 share the same algebraic silhouette — a $1/m$ from the winding, a $1/(e^L - 1)$ from the geometry, and an exponential decay $e^{(1-s)L}$ controlled by the process's spectral parameter $s$. Only the pair $(C, s)$ changes; the finiteness argument below only uses this shared shape.
> **Concretely:** Brownian, $L = 1$: $\mu(C) = 1/(e - 1) \approx 0.582$; the summed mass over all $\gamma$ and $m$ will be dominated (asymptotically in the geodesic length) by $\sum_\gamma e^{-\ell_\gamma}$. Full detail: [[Ex - The Four Bernstein Functions of the Paper]] and [[Thm - Mass of a Subordinate Brownian Loop Class]].

---

# Statement

> **Corollary (finiteness of the total loop mass; Belyaev–Huseynli 4.7).** Let $X = \Gamma\backslash\mathbb H^2$ be a geometrically finite hyperbolic surface with critical exponent $\delta$. For each of the paper's four Bernstein functions $\phi$, with spectral parameter $s(\phi) \in \mathbb R$ (namely $s = 1$ for Brownian and $\alpha$-stable; $s = \frac12 + \sqrt{\tfrac14 + \kappa}$ for killed and shifted stable, with $\kappa \ge -\tfrac14$): if
> $$s(\phi) \;>\; \delta,$$
> then the total mass over non-trivial non-peripheral homotopy classes is finite,
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^{\infty}\mu^\phi_X\big(C_X(\gamma^m)\big) \;<\; \infty.$$
> Moreover, the threshold is sharp: at $s(\phi) = \delta$ the sum diverges, and $Z_X(s) \to 0$ as $s \downarrow \delta$.

---

# In One Line

The total mass is finite exactly when the **loop-decay rate $s$** beats the **geodesic-proliferation rate $\delta$**. On a finite-area surface ($\delta = 1$), plain Brownian ($s = 1$) sits right at the threshold and diverges; a strictly positive killing rate $\kappa > 0$ is required to push $s > 1$ and get finiteness.

---

# Why It's True

**Mechanism (one sentence).** *Summing the canonical class-mass shape over the winding number $m$ reduces the total sum to $\sum_\gamma e^{-s\ell_\gamma}$; the prime geodesic theorem says the geodesic counting function grows like $e^{\delta R}/R$, so this sum behaves like $\int e^{-(s - \delta)R}/R\,dR$, convergent iff $s > \delta$.*

The proof is a **race** between two exponentials. The class-mass carries a factor $e^{-s\ell_\gamma}$ per (primitive) geodesic — an exponential *decay* at rate $s$. The number of geodesics of length $\le R$ grows like $e^{\delta R}$ — an exponential *proliferation* at rate $\delta$. Summing $e^{-s\ell_\gamma}$ over $\gamma$ is a race between these two rates; the sum converges iff the decay wins, i.e. iff $s > \delta$.

Two subtleties: **(i)** the $1/(e^L - 1)$ denominator of the class-mass does not change the asymptotics because it approaches $1$ up to a $(1 - e^{-\ell_{\mathrm{sys}}})^{-1}$ factor (loops are at least as long as the systole); **(ii)** the winding sum $\sum_{m \ge 1} e^{-sm\ell_\gamma}/m = -\log(1 - e^{-s\ell_\gamma})$ contributes only a lower-order correction to $e^{-s\ell_\gamma}$ (since $e^{-s\ell_\gamma} \to 0$ along the length spectrum), so summing over $m$ first collapses cleanly to a $\gamma$-sum of the same asymptotic order as $\sum_\gamma e^{-s\ell_\gamma}$.

The **sharpness** at $s = \delta$ is inherited from the sharpness of the Selberg product's convergence: $Z_X(s)$ has a simple zero at $s = \delta$ (equivalently the Poincaré series diverges at $s = \delta$), so $-\log Z_X(s) \to +\infty$ as $s \downarrow \delta$.

---

# Proof

> [!note]- Gap-free proof of Corollary 4.7
> **Setup.** By the recall above, each class-mass has the shape $\mu^\phi_X(C_X(\gamma^m)) = \frac{C}{m}\cdot\frac{e^{(1-s)L}}{e^L - 1}$ with $L = m\ell_\gamma$, $C > 0$, and $s = s(\phi)$. Let $\ell_{\mathrm{sys}} := \min_\gamma \ell_\gamma$ be the systole. Because $X$ is geometrically finite, $\ell_{\mathrm{sys}} > 0$.
>
> **Step 1 — bound the winding sum.** For every $L \ge \ell_{\mathrm{sys}}$, $e^L - 1 = e^L(1 - e^{-L}) \ge e^L(1 - e^{-\ell_{\mathrm{sys}}})$; so
> $$\frac{e^{(1-s)L}}{e^L - 1} \;=\; \frac{e^{-sL}\cdot e^L}{e^L - 1} \;\le\; \frac{e^{-sL}}{1 - e^{-\ell_{\mathrm{sys}}}}.$$
> Sum over $m \ge 1$ (with $L = m\ell_\gamma$), using the elementary identity $\sum_{m \ge 1} x^m/m = -\log(1 - x)$ for $|x| < 1$ applied to $x = e^{-s\ell_\gamma} \in (0, 1)$:
> $$\sum_{m \ge 1}\mu^\phi_X\big(C_X(\gamma^m)\big) \;\le\; \frac{C}{1 - e^{-\ell_{\mathrm{sys}}}}\sum_{m \ge 1}\frac{e^{-sm\ell_\gamma}}{m} \;=\; -\frac{C}{1 - e^{-\ell_{\mathrm{sys}}}}\log\big(1 - e^{-s\ell_\gamma}\big).$$
> Using the elementary inequality $-\log(1 - x) \le x/(1 - x)$ for $x \in (0, 1)$, and $1 - e^{-s\ell_\gamma} \ge 1 - e^{-s\ell_{\mathrm{sys}}}$,
> $$\sum_{m \ge 1}\mu^\phi_X\big(C_X(\gamma^m)\big) \;\le\; \frac{C}{(1 - e^{-\ell_{\mathrm{sys}}})(1 - e^{-s\ell_{\mathrm{sys}}})}\cdot e^{-s\ell_\gamma} \;=:\; K \cdot e^{-s\ell_\gamma}$$
> for a finite constant $K > 0$ depending only on $\phi$ and the systole (not on $\gamma$).
>
> **Step 2 — reduce total mass to $\sum_\gamma e^{-s\ell_\gamma}$.** Summing Step 1 over $\gamma \in \mathcal P_X$,
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu^\phi_X\big(C_X(\gamma^m)\big) \;\le\; K\sum_{\gamma \in \mathcal P_X} e^{-s\ell_\gamma}.$$
> Conversely, keeping only $m = 1$ in the class-mass and dropping the $1/(e^L - 1)$ denominator gives $\mu^\phi_X(C_X(\gamma)) \ge C\,e^{-s\ell_\gamma}/(e^{\ell_\gamma})$ — a positive multiple of $e^{-(s+1)\ell_\gamma}$; so the total sum is at least $C\sum_\gamma e^{-(s+1)\ell_\gamma}$, which is of the same rate as $\sum_\gamma e^{-s\ell_\gamma}$ shifted by $1$. **The total mass is finite iff $\sum_{\gamma \in \mathcal P_X} e^{-s\ell_\gamma} < \infty$** — this reduction is the crux.
>
> **Step 3 — evaluate the geodesic sum via the counting function.** Write the sum as a Riemann–Stieltjes integral against $N_X$: since $N_X(R) = 0$ for $R < \ell_{\mathrm{sys}}$,
> $$\sum_{\ell_\gamma \le T} e^{-s\ell_\gamma} \;=\; \int_{[0, T]} e^{-sR}\,dN_X(R).$$
> Integration by parts (or an Abel summation): $\int e^{-sR}\,dN_X(R) = e^{-sT}N_X(T) + s\int_0^T e^{-sR}N_X(R)\,dR$ (the boundary term at $R = 0$ vanishes because $N_X(0^-) = 0$). Substituting the [[Thm - Prime Geodesic Theorem|prime geodesic theorem]] $N_X(R) \asymp e^{\delta R}/R$ (asymptotic equivalence, so bounded above and below by a constant multiple),
> $$e^{-sR}N_X(R) \;\asymp\; \frac{e^{-(s - \delta)R}}{R}, \qquad e^{-sR}\int_0^T N_X(R)\,dR \;\asymp\; \int_c^T \frac{e^{-(s - \delta)R}}{R}\,dR$$
> for large $R$ (and any convenient lower cutoff $c \ge \ell_{\mathrm{sys}}$).
>
> **Step 4 — convergence analysis.** The integral $\int_c^\infty e^{-(s - \delta)R}/R\,dR$ converges iff $s > \delta$ (for $s > \delta$, $e^{-(s - \delta)R}$ decays exponentially and dominates the $1/R$ singularity at infinity; for $s = \delta$, the integrand becomes $1/R$ and the integral diverges like $\log R$; for $s < \delta$, the integrand blows up). At $s > \delta$, additionally $e^{-sT}N_X(T) \sim e^{-(s - \delta)T}/(\delta T) \to 0$, so the boundary term at $T = \infty$ vanishes. Therefore
> $$\sum_{\gamma \in \mathcal P_X} e^{-s\ell_\gamma} \;<\; \infty \iff s > \delta.$$
> Combining with Step 2, the total mass is finite iff $s > \delta$. $\blacksquare$
>
> **Step 5 — sharpness at $s \downarrow \delta$.** For the killed case (where the Selberg zeta identity of [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] applies), the total mass equals $-\log Z_X(s)$. As $s \downarrow \delta$, the argument above shows the double series (log-expansion of $Z_X$) diverges to $+\infty$; by monotone convergence (all terms positive), $-\log Z_X(s) \uparrow +\infty$, hence $Z_X(s) \downarrow 0$. So the total mass blows up as $s$ approaches the critical exponent from above — the threshold is sharp.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.2]]. Sets up the **motivation for §5**: on a **finite-area** surface, $\delta = 1$; the plain Brownian case has $s = 1$ and sits exactly at the divergent threshold. Since the summand is finite for each class (Theorem 3.5), the divergence lives in the *contractible* class (which is dropped from this sum but contributes the divergent short-loop mass of §2). [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]] renormalises exactly this divergence, extracting the zeta-regularised determinant of the Laplacian. For infinite-area surfaces, or for any strictly positive killing rate on a finite-area surface, the corollary already gives finiteness with no renormalisation required.
