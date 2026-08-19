---
type: theorem
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [paper, brownian-loops, spectral-geometry, zeta-functions, external-input]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 5.5"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a **geometrically finite** hyperbolic surface (not necessarily compact), with $n_C$ cusps (points where the surface "ends" as a shrinking puncture-neighbourhood).
- $\chi = \chi(X) = 2 - 2g - n_C - n_F \in \mathbb Z$ — the Euler characteristic; for a finite-area surface without funnels this is $2 - 2g - n_C$.
- $\Delta_X$ — the positive Laplace–Beltrami operator (spectrum in $[0, \infty)$, continuous part $[1/4, \infty)$ one band per cusp when $n_C \ge 1$).
- $s \in \mathbb C$ — a spectral parameter; the shifted operator $\Delta_X - s(1-s)$ is central because $s(1-s)$ parametrises the "spectral variable" whose critical line $\operatorname{Re} s = 1/2$ meets the essential spectrum $[1/4, \infty)$.
- $Z_X(s) = \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ — the Selberg zeta function.
- ${\det}_0(\Delta_X - s(1-s))$ — the **renormalised (0-)determinant** of the shifted Laplacian; the cusped-surface substitute for $\det_\zeta$, defined via the renormalised (0-)trace.
- $G(s)$ — the **Barnes $G$-function**, the entire function satisfying $G(s+1) = \Gamma(s) G(s)$ with $G(1) = 1$ (the "double gamma"; the log-derivative of $G$ is a natural regulariser of $\sum \log\Gamma$).
- $\Gamma(s)$ — the classical Gamma function.
- $\zeta_R(s)$ — the Riemann zeta function; $\zeta_R'(-1) \approx -0.165$ is a specific numerical constant appearing in universal spectral formulas.
- The explicit constants: $M := \chi\left(\frac12\log 2\pi - 2\zeta_R'(-1) + \frac14\right)$, $F := -\chi$, $G_\infty(s) := (2\pi)^{-s}\,\Gamma(s)\,G(s)^2$, $C_X := e^M (2\pi)^{-\chi} (\sqrt 2\,\pi)^{-n_C}$.

> [!recall]- Zeta-regularised determinant of the Laplacian
> **Formally:** for a closed surface with Laplace eigenvalues $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots\to\infty$, the spectral zeta function is $\zeta_X(s):=\sum_{j\ge1}\lambda_j^{-s}$; it continues meromorphically to $\mathbb C$ and is regular at $s=0$, and $\log\det_\zeta\Delta_X:=-\zeta_X'(0)$.
> **In words:** the finite, canonical stand-in for the divergent product $\prod_{j\ge1}\lambda_j$ of Laplace eigenvalues. Formally $\sum\log\lambda_j = -\zeta_X'(0)$, and $\zeta_X'(0)$ is defined by analytic continuation.
> **Concretely:** three eigenvalues $\lambda = 1, 2, 3$ give $\zeta(s) = 1 + 2^{-s} + 3^{-s}$, $-\zeta'(0) = \log 6 = \log(1\cdot 2\cdot 3)$, the ordinary product. On the flat torus $T^2 = \mathbb R^2/(2\pi\mathbb Z)^2$, $\det_\zeta\Delta$ is a finite Jacobi-theta-product number. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Renormalised trace and 0-determinant (cusped case)
> **Formally:** on a finite-area but non-compact hyperbolic surface with cusps, Melrose's compactification $\bar X$ adds a boundary at infinity with a smooth boundary defining function $x : \bar X \to [0, \infty)$ ($x = 0$ exactly on the boundary). The **renormalised integral** $^{0}\!\!\int_X f := \operatorname{FP}_{z=0}\int_X x^z f\,d\!\operatorname{vol}_g$ takes the divergent $\int_X f$, multiplies the integrand by $x^z$ to make it convergent for $\operatorname{Re}z > 0$, analytically continues in $z$, and takes the **finite part** (constant term in the Laurent expansion) at $z = 0$. The **0-trace** is $^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) := \,^{0}\!\!\int_X p(t, z, z)\,d\!\operatorname{vol}_g$; then $\zeta^0_X(s) := \Gamma(s)^{-1}\int_0^\infty t^{s-1}(^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) - P)\,dt$ (with $P$ the projection onto the finite-dimensional $L^2$-null-space), and ${\det}_0\Delta_X := e^{-(\zeta^0_X)'(0)}$. On a closed surface, $x \equiv 1$ and the whole construction reduces to $\det_\zeta\Delta_X$.
> **In words:** on a cusped surface, the ordinary heat trace $\int_X p(t, z, z)\,d\!\operatorname{vol}$ diverges because the cusps contribute infinite volume of "flat" regions where $p(t, z, z) \sim 1/(4\pi t)$ but $\operatorname{vol}(\text{cusp}) = \infty$. The renormalisation multiplies the integrand by $x^z$, where $x$ is a coordinate that vanishes at the cusp — this makes the integral converge for large $z$, and analytic continuation to $z = 0$ picks out the "regular part" (throwing away the cusp singularity). What remains is finite spectral content that goes into the ordinary zeta-regularisation recipe.
> **Concretely:** on the modular surface $\mathrm{PSL}(2, \mathbb Z)\backslash\mathbb H^2$ (one cusp), the naive heat trace at time $t$ is $+\infty$; the 0-trace equals a finite $t$-dependent number. On a closed sphere (no cusps), $x \equiv 1$ and the entire construction reduces to $\det_\zeta$. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Selberg zeta $Z_X(s)$ (finite-area case)
> **Formally:** $Z_X(s) := \prod_{\gamma\in\mathcal P_X}\prod_{k\ge0}(1 - e^{-(s+k)\ell_\gamma})$ for $\operatorname{Re}s > 1$ (the critical exponent $\delta = 1$ on a finite-area surface); continues meromorphically to $\mathbb C$. Trivial and non-trivial zeros correspond to Laplace eigenvalues (finite-area case): each $\lambda_j = s_j(1 - s_j) < 1/4$ gives a zero of $Z_X$ at $s = s_j$; $\lambda_0 = 0$ forces a **simple zero at $s = 1$**.
> **In words:** a "prime-power" product over closed geodesics analogous to $\prod_p (1 - p^{-s})^{-1}$; its zeros encode the discrete Laplace spectrum. On a finite-area surface, $0$ is a Laplace eigenvalue, so $s = 1$ is a simple zero of $Z_X$.
> **Concretely:** for a compact hyperbolic surface, $Z_X(s)$ vanishes at $s = 1$; near it, $Z_X(s) = Z_X'(1)(s-1) + O((s-1)^2)$. See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Barnes $G$-function
> **Formally:** the **Barnes $G$-function** is the entire meromorphic function $G : \mathbb C \to \mathbb C$ characterised uniquely (up to a normalising constant) by the functional equation $G(z + 1) = \Gamma(z)\,G(z)$, the initial condition $G(1) = 1$, and convexity: $\log G(x + 1)$ is convex for $x > 0$. Explicit product: $G(1 + z) = (2\pi)^{z/2}\exp\!\left(-\frac{z + z^2(1 + \gamma_{\mathrm{EM}})}{2}\right)\prod_{k=1}^\infty\left(1 + z/k\right)^k \exp\!\left(-z + z^2/(2k)\right)$.
> **In words:** the "double Gamma" — a natural regularisation of the divergent product $\prod_{k=1}^\infty \Gamma(k) = \prod\prod j$, in the same way $\Gamma(z)$ regularises $(z-1)!$. It arises whenever you need to make sense of sums or products of $\log\Gamma$-values (e.g. one-loop determinants that involve a doubly-indexed product of eigenvalues, as in Selberg-zeta determinant formulas for cusped surfaces).
> **Concretely:** $G(2) = 1$, $G(3) = 1$, $G(4) = 2$, $G(5) = 12$; in general $G(n+2) = \prod_{k=1}^n k! = 1! \cdot 2! \cdots n!$ (the "superfactorial"). Its role in spectral geometry is essentially bookkeeping: the Selberg-zeta determinant formula for cusped surfaces contains a factor $G_\infty(s) = (2\pi)^{-s}\Gamma(s)G(s)^2$, whose logarithm is the natural regulariser of the sum over the continuous cusp spectrum.

---

# Statement

> **Theorem (Borthwick–Judge–Perry determinant formula; Belyaev–Huseynli Theorem 5.5, external input).** Let $X = \Gamma\backslash\mathbb H^2$ be a geometrically finite hyperbolic surface with $n_C$ cusps and Euler characteristic $\chi = \chi(X)$. Then for $s \in \mathbb C$ (avoiding poles),
> $${\det}_0\!\big(\Delta_X - s(1-s)\big) \;=\; Z_X(s)\,e^{M + F\,s(1-s)}\,G_\infty(s)^\chi\,\Big(\sqrt 2 \big[2s\sqrt\pi\,(s - \frac12)\big]\,\Gamma(s - \frac12)\Big)^{-n_C},$$
> where $G_\infty(s) = (2\pi)^{-s}\,\Gamma(s)\,G(s)^2$ (with $G$ the Barnes $G$-function), $M = \chi\!\left(\frac12\log 2\pi - 2\zeta_R'(-1) + \frac14\right)$, and $F = -\chi$.
>
> **Consequence.** Evaluating at $s = 1$ (or taking the appropriate limit if $Z_X(1) = 0$), the renormalised determinant of $\Delta_X$ itself is $\det_0 \Delta_X = C_X\,Z_X'(1)$ (finite-area case; the simple zero of $Z_X$ at $s = 1$ is divided out to leave the derivative) or $\det_0\Delta_X = C_X\,Z_X(1)$ (infinite-area case), with the explicit constant $C_X = e^M (2\pi)^{-\chi} (\sqrt 2\,\pi)^{-n_C}$.

---

# In One Line

The renormalised determinant of the shifted Laplacian on a geometrically finite hyperbolic surface factors *explicitly* as (Selberg zeta) $\times$ (universal $s$-dependent gamma-and-Barnes-$G$ factors coming from the continuous cusp spectrum) $\times$ (topological constant). This is the cusped analogue of D'Hoker–Phong's $\det_\zeta\Delta = Z_X'(1)\,e^{(2g-2)(\cdots)}$ formula on a closed surface.

---

# Why It's True (intuition)

**Mechanism (one sentence).** *Both sides satisfy the same second-order differential equation in the spectral variable $s$ — namely $\big(\frac{1}{2s-1}\partial_s\big)^2 \log F(s) = -\,^{0}\!\operatorname{Tr}(R_X(s)^2)$, where $R_X(s) = (\Delta_X - s(1-s))^{-1}$ is the resolvent — so they agree up to an integration constant $e^{M + Fs(1-s)}$ that is pinned down by the small-$s$ asymptotics, and the explicit cusp factors come from the contribution of the continuous spectrum (parametrised by the Eisenstein series, whose scattering matrix contributes $\Gamma$ and $G$ pieces).*

**Where the pieces come from.**
- $Z_X(s)$: the **discrete-spectrum content**, encoded in the closed geodesics via the Selberg product. This is the piece that becomes the loop mass when combined with the Selberg zeta identity.
- $G_\infty(s)^\chi$: the **local geometric anomaly** — the term you get if the surface had no cusps and no discrete spectrum; the Euler characteristic $\chi$ appears because the anomaly is proportional to it (Gauss–Bonnet-type origin, cf. the $\chi/6$ constant in the small-time heat trace).
- The $\Gamma(s - 1/2)^{-n_C}$ factor: the **continuous cusp spectrum**, which produces one "band" per cusp; each band contributes a scattering-matrix factor that turns out to be a specific ratio of Gamma functions.
- $e^{M + Fs(1-s)}$: an **integration constant** of the resolvent-trace differential equation; the two parameters $M, F$ are fixed by the small-$s$ or large-$s$ asymptotic behaviour.

*This intuition is not a proof.* The full derivation is a resolvent-trace calculation combined with the Eisenstein series' scattering-matrix explicit formula.

---

# Proof

> [!cite]- External input — Borthwick–Judge–Perry determinant formula
> **Statement (typed):** as above.
> **Why it's true (intuition):** as above; the mechanism is integrating a resolvent-trace differential equation for $\log\det_0$ in the spectral parameter $s$, with the constants pinned by asymptotics and the explicit cusp factors coming from the scattering matrix of the Eisenstein series.
> **Source.** David Borthwick, Christopher Judge, and Peter A. Perry, *Selberg zeta functions and relative determinants for surfaces of infinite area*, Comment. Math. Helv. **80** (2005), 483–515 (Theorem 1.1 and its consequence at $s = 1$). See also Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces*, Progress in Mathematics **256**, Birkhäuser (2007), Ch. 10, for the geometrically finite finite-area case with cusps. **Take on faith** with the exact statement above; the proof lies well above the paper-notes floor and beyond what the Belyaev–Huseynli paper itself proves. The factor $Z_X$ is what becomes the loop mass on substitution of the [[Thm - Selberg Zeta Identity for the Total Loop Mass|Selberg zeta identity]].

---

# Where the paper uses this

The paper cites Borthwick–Judge–Perry as Theorem 5.5 in [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.2]] and combines it with the Selberg zeta identity ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]) to give [[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]]: the renormalised determinant $\det_0\Delta_X$ on a cusped finite-area surface expressed as a loop mass plus explicit cusp corrections, with the same $\log\kappa$/simple-zero cancellation as in the compact case ([[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]]).

---

# Verified against

Borthwick–Judge–Perry, *Selberg zeta functions and relative determinants for surfaces of infinite area* (Comment. Math. Helv. 2005) — original statement and proof. Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces* (Birkhäuser 2007), Ch. 10 — expository account with the cusp factors. Statement matches Belyaev–Huseynli §5.2 exactly.
