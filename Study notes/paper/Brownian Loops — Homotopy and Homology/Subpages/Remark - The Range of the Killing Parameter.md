---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Hyperbolic Plane"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
tags: [paper, brownian-loops, hyperbolic-geometry, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 3.7"
---

# Notation

- $\kappa \in \mathbb{R}$ — the *killing parameter*, or (equivalently) the shift of the Laplacian $\Delta_{\mathbb{H}^2}$: the paper considers the family of operators $\Delta_{\mathbb{H}^2} + \kappa$ for varying $\kappa$.
- $\phi(\lambda) = \lambda + \kappa$ — a Bernstein function only when $\kappa \ge 0$; for $\kappa < 0$ it is not Bernstein (the "killing" is negative).
- $L = m\ell_\gamma$ — total translation length for a class $C_X(\gamma^m)$; $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$ the closed-form loop-length integral of §3.1.2.
- $\mathfrak{s}$ — the **spectral parameter**, related to $\kappa$ by the paper's identity $\kappa = \mathfrak{s}(\mathfrak{s} - 1)$; solving for $\mathfrak{s}$ with the positive-square-root branch gives $\mathfrak{s} = \frac12 + \sqrt{\frac14 + \kappa}$.
- $\Delta_{\mathbb{H}^2}$ — the positive Laplace–Beltrami operator on $\mathbb{H}^2$; its $L^2$-spectrum is $[1/4, \infty)$ (continuous), with spectral bottom $\lambda_0 = 1/4$.

> [!recall]- $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$ on $\mathbb{H}^2$
> **Formally:** the spectrum of the (positive) Laplace–Beltrami operator $\Delta_{\mathbb{H}^2}$ on $L^2(\mathbb{H}^2, \rho_{\mathbb{H}^2})$ is $\sigma(\Delta_{\mathbb{H}^2}) = [1/4, \infty)$, continuous, with no eigenvalues. The bottom is $\lambda_0 = 1/4 = (1/2)^2$, achieved as a generalised eigenvalue (spherical function).
> **In words:** $\Delta_{\mathbb{H}^2}$ has no $L^2$-eigenfunctions; instead it has a *continuous* spectrum starting at $1/4$. The number $1/4$ is a geometric invariant of the hyperbolic plane — it comes from the exponential volume growth of hyperbolic balls, which makes the return probability density of Brownian motion at time $t$ decay like $e^{-\lambda_0 t} = e^{-t/4}$ at long times.
> **Concretely:** compute the heat kernel at coincident points: $p_{\mathbb{H}^2}(t, z, z) = (4\pi)^{-3/2}e^{-t/4}\int_0^\infty u e^{-u^2/(4t)}/\sinh(u/2)\,du$ (with $u$ the distance variable); the factor $e^{-t/4}$ is exactly the spectral-bottom contribution, and $1/4$ is not an eigenvalue but the infimum of the continuous spectrum. On a compact hyperbolic surface $X = \Gamma\backslash\mathbb{H}^2$ the spectrum is discrete but the spectral gap can be smaller than $1/4$; on general geometrically finite $X$ (with cusps or funnels), $1/4$ often remains the essential spectral bottom.

> [!recall]- $\phi(\lambda) = \lambda + \kappa$ as a Bernstein function iff $\kappa \ge 0$
> **Formally:** a Bernstein function must be non-negative and non-decreasing on $(0,\infty)$ with $\phi(0^+) \ge 0$. The map $\phi(\lambda) = \lambda + \kappa$ satisfies $\phi(0^+) = \kappa$; this is non-negative iff $\kappa \ge 0$. So $\phi(\lambda) = \lambda + \kappa$ is Bernstein exactly for $\kappa \ge 0$; for negative $\kappa$ the "process" is not a genuine subordinated probability semigroup (it would need "negative killing", i.e. mass creation).
> **In words:** genuine killing removes mass at a fixed rate — Bernstein-valid. "Negative killing" would inject mass — not a probability process. But the closed-form loop-length integral $I_\kappa(L)$ derived from $\phi = \lambda + \kappa$ makes sense *analytically* for any $\kappa$ that keeps the exponent $\sqrt{1/4 + \kappa}$ real, i.e. for $\kappa \ge -1/4$.
> **Concretely:** for $\kappa = 0$, $\phi = \lambda$ is the identity Bernstein function (no subordination); for $\kappa = 1$, $\phi = \lambda + 1$ is Bernstein (killing at rate $1$); for $\kappa = -1/8$, $\phi = \lambda - 1/8$ is *not* Bernstein, but the integral $I_{-1/8}(L) = e^{-L\sqrt{1/8}}/L$ still makes sense and can be analysed as a formal object.

---

# Statement

> **Remark (the range $\kappa \ge -\frac14$; Belyaev–Huseynli 3.7).** For $\kappa \in [-\frac14, 0)$, the map $\phi(\lambda) = \lambda + \kappa$ is *not* a Bernstein function (it takes the negative value $\kappa$ at $\lambda = 0$), so the strict framework of §2 does not apply. Nevertheless, the closed-form loop-length integral $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$ and the induced class-mass formula
> $$\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{e^{(\frac12 - \sqrt{1/4+\kappa})L}}{e^L - 1}, \qquad L = m\ell_\gamma,$$
> continue to make sense analytically for all $\kappa \ge -\frac14$. Introducing the **spectral parameter** $\mathfrak{s}$ by $\mathfrak{s} = \frac12 + \sqrt{\frac14 + \kappa}$ (equivalently, $\kappa = \mathfrak{s}(\mathfrak{s} - 1)$), the condition $\kappa \ge -\frac14$ is exactly what keeps $\mathfrak{s}$ real, with the boundary case $\kappa = -1/4$ giving $\mathfrak{s} = 1/2$ — precisely the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$. ⚠️ *(Notation collision, flagged.)* The paper writes this spectral parameter as $s$, colliding with the subordination variable $s$; here it is renamed $\mathfrak{s}$ throughout. The dictionary $\kappa = \mathfrak{s}(\mathfrak{s} - 1)$ is the bridge to the Selberg zeta variable in §4.

---

# In One Line

Even though $\phi = \lambda + \kappa$ is Bernstein only for $\kappa \ge 0$, the class-mass formula is analytic in $\kappa$ throughout $[-\frac14, \infty)$; the extension to $\kappa \in [-\frac14, 0)$ is meaningful, and the endpoint $\kappa = -1/4$ corresponds to the bottom of the $\mathbb{H}^2$-spectrum via the change of variable $\kappa = \mathfrak{s}(\mathfrak{s} - 1)$.

---

# Unpacking

**Where the condition $\kappa \ge -\frac14$ comes from.** The class-mass depends on $\kappa$ through the factor $e^{-L\sqrt{1/4 + \kappa}}$: the exponent is real (and the mass is a real positive number) iff $1/4 + \kappa \ge 0$, i.e. $\kappa \ge -1/4$. For $\kappa < -1/4$, $\sqrt{1/4 + \kappa}$ becomes imaginary and the exponential oscillates instead of decaying; the "class mass" ceases to be a positive number and the physical interpretation breaks down.

**Why $-1/4$ is not arbitrary — it is the bottom of the $\mathbb{H}^2$-spectrum.** Setting $\mathfrak{s}(\mathfrak{s} - 1) = \kappa$ (a quadratic in $\mathfrak{s}$) gives $\mathfrak{s} = \frac12 \pm \sqrt{\frac14 + \kappa}$; keeping the branch with $\mathfrak{s} \ge \frac12$ (the "principal series bound") gives the paper's $\mathfrak{s} = \frac12 + \sqrt{\frac14 + \kappa}$. The map $\kappa\mapsto\mathfrak{s}$ is an increasing bijection from $[-\frac14, \infty)$ onto $[\frac12, \infty)$. The lower endpoint $\kappa = -\frac14$ corresponds to $\mathfrak{s} = \frac12$, which is precisely the *bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$*: eigenfunctions of $\Delta_{\mathbb{H}^2}$ (in the generalised, spherical-function sense) with eigenvalue $\mathfrak{s}(1 - \mathfrak{s})$ exist iff $\mathfrak{s}\in [\frac12, 1]$; at the boundary $\mathfrak{s} = \frac12$, the eigenvalue is $\frac14$, which is the spectral bottom.

**The physical interpretation.** In the language of the QM digression (§3.2), $\Delta_{\mathbb{H}^2} + \kappa$ is the Schrödinger operator with constant potential $\kappa$; requiring $\Delta_{\mathbb{H}^2} + \kappa \ge 0$ (a valid Euclidean-time Hamiltonian) is exactly the condition that $\kappa$ is at least the negative of the spectral bottom of $\Delta_{\mathbb{H}^2}$, i.e. $\kappa \ge -\frac14$. Below this threshold the semigroup $e^{-t(\Delta_{\mathbb{H}^2} + \kappa)}$ grows exponentially at large $t$ (because $e^{-t\kappa}\cdot e^{-t\lambda_0}$ diverges if $|\kappa| > \lambda_0 = 1/4$), and the loop measure ceases to have finite mass on any class.

**The bridge to the Selberg zeta.** In [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4]] the total mass of the killed loop measure is expressed as $\log$ of a **Selberg zeta function** evaluated at a spectral parameter $\mathfrak{s}$: $|\mu^\kappa_X| = \log Z_X(\mathfrak{s})$ (up to renormalisation). The identification $\kappa = \mathfrak{s}(\mathfrak{s} - 1)$ is exactly the substitution needed to align the paper's killing parameter with the Selberg zeta's spectral variable. The condition $\kappa \ge -1/4$ then translates to $\mathfrak{s} \ge 1/2$, which is the classical "critical line" (or half-plane) for Selberg-type zetas — the natural domain of convergence.

**Notation warning.** The paper uses $s$ for the spectral parameter and, separately, $s$ for the subordination variable in the definition of $V_\phi$ and $I_\phi$. These are distinct: one lies in $[\frac12, \infty)$ and parametrises the eigenvalue-vs-killing dictionary; the other lies in $(0, \infty)$ and is the internal clock of the subordinator. To keep the notes unambiguous, these notes rename the spectral parameter as $\mathfrak{s}$ (fraktur $s$) and reserve $s$ for the subordination variable. ⚠️ *(Notation collision flagged.)*

---

# Where the paper uses this

Justifies the closed-form class-mass formula of [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] (case §3.1.2) beyond the strict Bernstein range $\kappa \ge 0$; extends the injectivity argument of [[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]] to the full range $\kappa \ge -1/4$, and hence the metric-rigidity result [[Cor - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]]. The dictionary $\kappa = \mathfrak{s}(\mathfrak{s} - 1)$ is the primary link to the Selberg zeta of [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4]] and the determinant identity of [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]]. Read in context: [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]].
