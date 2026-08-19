---
type: corollary
subject: probability-geometry
prereqs:
  - "Lemma - Selberg Zeta Criterion"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Def - The Loop-Length Integral"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 4.3"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a geometrically finite hyperbolic surface with critical exponent $\delta \in (0, 1]$.
- $\mathcal P_X$ — the primitive oriented closed geodesics of $X$, lengths $\ell_\gamma$.
- $C_X(\gamma^m)$ — the free homotopy class winding $m$ times around $\gamma$.
- $\kappa \in [-\frac14, \infty)$ — a real **killing rate**; the driving Bernstein function is $\phi(\lambda) = \lambda + \kappa$.
- $\mu^\kappa_X$ — the loop measure of Brownian motion on $X$ with constant killing rate $\kappa$ (equivalently, the loop measure of the Schrödinger operator $\Delta_{\mathbb H^2} + \kappa$).
- $s := \frac12 + \sqrt{\frac14 + \kappa}$ — the spectral parameter attached to $\kappa$; a real number in $[\frac12, \infty)$ when $\kappa \ge -\frac14$.
- $Z_X(s) = \prod_{\gamma}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ — the Selberg zeta function.

> [!recall]- Hyperbolic surface $X = \Gamma\backslash\mathbb H^2$
> **Formally:** $\mathbb H^2 = \{x + iy : y > 0\}$ with metric $ds^2 = (dx^2 + dy^2)/y^2$; $\Gamma \subset \mathrm{PSL}(2, \mathbb R)$ a discrete torsion-free subgroup; $X = \Gamma\backslash\mathbb H^2$ inherits the hyperbolic metric.
> **In words:** the upper half-plane with a curved ruler that shrinks near the real axis, quotiented by a discrete group of rigid motions to give a curved surface with a definite global shape (handles, cusps).
> **Concretely:** the Euclidean analogue is $T^2 = \mathbb R^2/\mathbb Z^2$; a hyperbolic genus-2 surface (two-holed pretzel) is $\Gamma\backslash\mathbb H^2$ for a 4-generator Fuchsian $\Gamma$. On a compact (cocompact $\Gamma$) surface, $\delta = 1$; on an infinite-area (funnelled) surface, $\delta < 1$. Full detail: [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].

> [!recall]- Brownian loop measure with killing $\mu^\kappa_X$
> **Formally:** for $\kappa \ge 0$, the killing-$\kappa$ Brownian loop measure on $X$ is $\mu^\kappa_X = \int_0^\infty \frac{dt}{t}\int_X \mathbb W^{t, \phi}_{z \to z, X}\,d\rho_X(z)$ with Bernstein function $\phi(\lambda) = \lambda + \kappa$; equivalently, its heat kernel is $p^\kappa_{\mathbb H^2}(t, z, w) = e^{-\kappa t}\,p_{\mathbb H^2}(t, z, w)$, weighting Brownian bridges by the survival factor $e^{-\kappa t}$. Extended to $\kappa \ge -\frac14$ (which reaches down to the spectral bottom of $\Delta_{\mathbb H^2}$) by analytic continuation of the resulting closed-form class mass.
> **In words:** the ordinary Brownian loop measure, tilted by an exponential decay in time $e^{-\kappa t}$: loops that take longer are penalised more. Corresponds to loops of the Schrödinger operator $\Delta_{\mathbb H^2} + \kappa$ (a constant potential). The special value $\kappa = 0$ gives the plain Brownian loop measure.
> **Concretely:** for $\kappa = 0$, no killing — this is the ordinary Brownian case; the summed non-trivial-class mass will turn out to diverge on any finite-area surface (where $\delta = 1$). For $\kappa > 0$, killing strictly compresses long loops; on a finite-area surface, $s(\kappa) > 1 = \delta$ and the summed mass becomes finite. Full detail: [[Def - Subordinate Brownian Loop Measure]] and [[Remark - The Range of the Killing Parameter]].

> [!recall]- Spectral parameter $s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$
> **Formally:** the map $\kappa \mapsto s$ solving $s(s - 1) = \kappa$ (with the branch $s \ge \frac12$) is $s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$; it is defined and real for $\kappa \ge -\frac14$, with $s(-\frac14) = \frac12$, $s(0) = 1$, and $s(\kappa) \to \infty$ as $\kappa \to \infty$.
> **In words:** the killing rate $\kappa$ and the zeta variable $s$ are two coordinates on the same parameter; the map $\kappa \mapsto s$ is the change of variables that turns the exponent $\sqrt{\frac14 + \kappa}$ appearing in the killed loop-length integral into the exponent $s - \frac12$ appearing in the log-expansion of $Z_X(s)$.
> **Concretely:** $\kappa = 0$: $s = 1$ (the natural home of the un-killed Brownian case; also the spectral bottom for finite-area hyperbolic surfaces). $\kappa = 2$: $s = \frac12 + \sqrt{9/4} = 2$. $\kappa = -\frac14$: $s = \frac12$ (the boundary; the spectral bottom of $\Delta_{\mathbb H^2}$ is $\frac14 = -\kappa$). The identity $s(s - 1) = \kappa$ (equivalently $\kappa = s^2 - s$) is worth memorising — it is exactly $\kappa_-(s)$ in [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]].

> [!recall]- Killed loop-length integral $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$
> **Formally:** for $\phi(\lambda) = \lambda + \kappa$ with weighted potential measure $V_\phi(ds) = e^{-\kappa s}\,ds/s$, the loop-length integral is $I_\kappa(L) := \int_0^\infty \frac{e^{-s/4} e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,e^{-\kappa s}\,ds/s = \int_0^\infty \frac{e^{-(1/4 + \kappa)s} e^{-L^2/(4s)}}{2\sqrt\pi\,s^{3/2}}\,ds$. Applying the Gaussian-type identity $\int_0^\infty s^{-3/2} e^{-as - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ with $a = \frac14 + \kappa$, $b = L^2/4$ (so $2\sqrt{ab} = L\sqrt{\frac14 + \kappa}$, $\sqrt{\pi/b} = 2\sqrt\pi/L$) gives the closed form $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$.
> **In words:** the process-integral for killed Brownian motion has a one-line closed form: the exponential decay rate is $\sqrt{\frac14 + \kappa}$, and the $1/L$ prefactor comes from the geometric-integral normalisation. All the killing dependence is packed into that square-root exponent.
> **Concretely:** at $\kappa = 0$, $I_0(L) = e^{-L/2}/L$ (the pure Brownian case). At $L = 1$, $\kappa = 0$: $I_0(1) = e^{-1/2} \approx 0.607$. At $L = 1$, $\kappa = 2$: $I_2(1) = e^{-\sqrt{9/4}} = e^{-3/2} \approx 0.223$ — stronger killing crushes the integral. Full detail: [[Def - The Loop-Length Integral]] and [[Ex - The Subordinate Form of Brownian Motion with Killing]].

> [!recall]- Selberg zeta $Z_X(s)$ and critical exponent $\delta$
> **Formally:** $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ for $\operatorname{Re} s > \delta$; log-expansion $-\log Z_X(s) = \sum_\gamma\sum_{m \ge 1}\frac{1}{m}\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$. $\delta$ is the exponent of convergence of the Poincaré series $\sum_{h \in \Gamma} e^{-s\,d(z, hz)}$; $\delta = 1$ for finite-area surfaces, $\delta < 1$ for infinite-area ones.
> **In words:** a product of one factor per closed geodesic and per non-negative integer $k$; a generating function for the length spectrum, analogous to how the Riemann zeta $\prod_p(1 - p^{-s})^{-1}$ is a generating function for the primes. $\delta$ measures how fast closed geodesics multiply — the sum in the log-expansion converges only when $s$ beats $\delta$.
> **Concretely:** for a compact (cocompact-$\Gamma$) surface, $\delta = 1$ and $Z_X(1)$ is a limit at the *boundary* of convergence — divergent $-\log Z_X(1) = +\infty$. For a funnelled infinite-area surface with $\delta = 1/2$, $Z_X(1)$ is a finite positive number, and $-\log Z_X(1)$ is finite. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

---

# Statement

> **Corollary (Selberg zeta identity; Belyaev–Huseynli 4.3).** Let $X = \Gamma\backslash\mathbb H^2$ be a geometrically finite hyperbolic surface with critical exponent $\delta$. For each real $\kappa \ge -\frac14$ such that $s(\kappa) := \frac12 + \sqrt{\frac14 + \kappa} > \delta$,
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^{\infty}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; -\log Z_X\!\Big(\frac12 + \sqrt{\frac14 + \kappa}\Big).$$
> In particular, at $\kappa = 0$ (plain Brownian, $s = 1$), the total Brownian loop mass equals $-\log Z_X(1)$, which is finite iff $\delta < 1$ (infinite area) and divergent when $\delta = 1$ (finite area).

---

# In One Line

The summed mass, over every non-trivial non-peripheral homotopy class, of the killing-$\kappa$ Brownian loop measure *is* a specific value of the Selberg zeta function — the paper's bridge from a random-loop sum to a classical spectral object. Immediate from the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]] with constant $C = 1$, once one verifies that the killed class-mass has the canonical shape.

---

# Why It's True

**Mechanism (one sentence).** *The killed loop-length integral $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$ has exactly the algebraic form the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]] asks for, with $C = 1$ and $s = \frac12 + \sqrt{\frac14 + \kappa}$; feed it into the criterion, and the total mass drops out as $-\log Z_X(s)$.*

The corollary is a **direct specialisation** of the general lemma: no new machinery, just a shape-check. The reader should think of it as "apply the criterion." The interest lies in what the identity *means*: for $\kappa = 0$ (pure Brownian, $s = 1$), the total mass of all non-trivial-non-peripheral classes is the log of the Selberg zeta at the spectral-bottom point $s = 1$; this is exactly the point where finite-area surfaces cease to have a finite total mass (because $\delta = 1$ meets $s = 1$, the boundary of convergence of the double series), motivating the renormalisation §5 will perform.

---

# Proof

> [!note]- Gap-free proof of Corollary 4.3
> **Step 1 — write out the killed loop-length integral.** By [[Def - The Loop-Length Integral|Definition 3.6]] applied to $\phi(\lambda) = \lambda + \kappa$ (whose weighted potential measure is $V_\phi(ds) = e^{-\kappa s}\,ds/s$; see the Notation recall or [[Ex - The Subordinate Form of Brownian Motion with Killing]]), and using the Gaussian-type integral $\int_0^\infty s^{-3/2} e^{-as - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ with $a = \frac14 + \kappa$, $b = L^2/4$,
> $$I_\kappa(L) \;=\; \frac{e^{-L\sqrt{1/4 + \kappa}}}{L}.$$
>
> **Step 2 — assemble $\frac{L}{2\sinh(L/2)}\,I_\kappa(L)$ and identify the shape.** Substituting the closed form of $I_\kappa$,
> $$\frac{L}{2\sinh(L/2)}\,I_\kappa(L) \;=\; \frac{L}{2\sinh(L/2)}\cdot\frac{e^{-L\sqrt{1/4 + \kappa}}}{L} \;=\; \frac{e^{-L\sqrt{1/4 + \kappa}}}{2\sinh(L/2)}.$$
> Expand $2\sinh(L/2) = e^{L/2} - e^{-L/2}$ and factor $e^{L/2}$ out of the denominator:
> $$\frac{e^{-L\sqrt{1/4 + \kappa}}}{e^{L/2} - e^{-L/2}} \;=\; \frac{e^{-L\sqrt{1/4 + \kappa}}\cdot e^{-L/2}}{1 - e^{-L}} \;=\; \frac{e^{-L(\sqrt{1/4 + \kappa} + 1/2)}}{1 - e^{-L}}.$$
> Multiply numerator and denominator by $e^L$:
> $$\frac{L}{2\sinh(L/2)}\,I_\kappa(L) \;=\; \frac{e^{-L(\sqrt{1/4 + \kappa} + 1/2)}\cdot e^L}{(1 - e^{-L})\cdot e^L} \;=\; \frac{e^{L(1/2 - \sqrt{1/4 + \kappa})}}{e^L - 1}.$$
> Set $s := \frac12 + \sqrt{\frac14 + \kappa}$, so $1 - s = \frac12 - \sqrt{\frac14 + \kappa}$. Then
> $$\frac{L}{2\sinh(L/2)}\,I_\kappa(L) \;=\; \frac{e^{(1-s)L}}{e^L - 1} \;=\; 1 \cdot \frac{e^{(1-s)L}}{e^L - 1}.$$
> This matches the shape of the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion (Lemma 4.2)]] with $C = 1$ and this specific $s$.
>
> **Step 3 — apply the Selberg zeta criterion.** The hypothesis of Lemma 4.2 asks that $s > \delta$; the corollary's hypothesis says exactly this. Applying the lemma with $C = 1$,
> $$\sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^{\infty}\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; -1 \cdot \log Z_X(s) \;=\; -\log Z_X\!\Big(\frac12 + \sqrt{\frac14 + \kappa}\Big).$$
>
> **Step 4 — specialise to $\kappa = 0$ and read off the finiteness dichotomy.** At $\kappa = 0$, $s = \frac12 + \sqrt{1/4} = 1$. On a **finite-area** surface, $\delta = 1$: the hypothesis $s > \delta$ *fails* (equality, not strict), so the corollary does not apply directly — the sum is $\lim_{s \downarrow 1} -\log Z_X(s)$, which diverges to $+\infty$ (this is the classical fact that $Z_X(s) \to 0$ as $s \downarrow \delta$; see [[Thm - Finiteness of the Total Loop Mass|Corollary 4.7]] for the sharp statement). On an **infinite-area** surface, $\delta < 1$: the hypothesis holds strictly at $\kappa = 0$, and the total Brownian loop mass is the finite number $-\log Z_X(1)$. $\blacksquare$

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1.1]]. This identity is the paper's central bridge from probability to spectral geometry; it is the input to the physical re-reading of [[Remark - Bosonic Partition Function Interpretation|Remark 4.4]], and the finite-area divergence it exhibits at $\kappa = 0$ is the divergence that [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]] renormalises (the contractible class is the culprit, subtracted off to give a finite zeta-regularised determinant). Corollary 4.7 ([[Thm - Finiteness of the Total Loop Mass]]) gives the sharp finiteness criterion.
