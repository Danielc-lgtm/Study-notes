---
type: remark
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
  - "Thm - Borthwick-Judge-Perry Determinant Formula"
tags: [paper, brownian-loops, spectral-geometry, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 5.8"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a **geometrically finite hyperbolic surface of infinite area** (with at least one funnel end); critical exponent $\delta \in (0, 1)$, strictly less than $1$.
- $\Delta_X$ — the positive Laplace–Beltrami operator; the essential spectrum is $[1/4, \infty)$ continuous, but $0$ is *not* an $L^2$-eigenvalue (constants are not integrable on an infinite-area surface).
- $\det_0\Delta_X$ — the renormalised (0-)determinant of $\Delta_X$ (cusped/funnelled case; reduces to $\det_\zeta$ on a closed surface).
- $Z_X(s)$ — the Selberg zeta function; $Z_X(1) \ne 0$ in this regime.
- $\mu_X$ — the (ordinary, un-killed) Brownian loop measure on $X$.

> [!recall]- Critical exponent $\delta < 1$ (infinite-area case)
> **Formally:** $\delta = \delta(\Gamma) := \inf\{s > 0 : \sum_{h \in \Gamma} e^{-s\,d(z, hz)} < \infty\}$, independent of $z$; equivalent to the Hausdorff dimension of the limit set of $\Gamma$ on $\partial\mathbb H^2$. For a **geometrically finite** hyperbolic surface, $\delta = 1$ if and only if $\operatorname{Area}(X) < \infty$; equivalently $\delta < 1$ iff $X$ has at least one funnel end (a bell-mouthed infinite-area end).
> **In words:** a single number measuring how fast $\Gamma$'s orbit accumulates near the boundary — equivalently, by the prime geodesic theorem, how fast closed geodesics of length $\le R$ multiply as $R$ grows. Finite-area surfaces have the maximum rate $\delta = 1$; infinite-area ones proliferate strictly slower.
> **Concretely:** on a compact genus-$2$ surface, $\delta = 1$. On a "3-funnel sphere" (a sphere with three infinite-area trumpet-shaped ends), $\delta$ can be tuned continuously in $(0, 1)$ by adjusting funnel widths: thin funnels give small $\delta$, wide funnels approach $\delta = 1$. See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Selberg zeta $Z_X(s)$: $Z_X(1) \ne 0$ when $\delta < 1$
> **Formally:** $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$; the product converges absolutely for $\operatorname{Re} s > \delta$, and extends meromorphically to $\mathbb C$. On the boundary $\operatorname{Re}s = \delta$, $Z_X$ has zeros corresponding to Laplace eigenvalues $\lambda_j = s_j(1 - s_j)$ with $s_j \in (1/2, 1]$. When $\delta < 1$, the point $s = 1$ is *strictly inside* the convergence half-plane, and $Z_X(1) > 0$ is a finite positive number.
> **In words:** the Selberg product converges absolutely and non-trivially at $s = 1$ in the infinite-area regime, so $Z_X(1)$ is a definite positive real number, not zero.
> **Concretely:** a funnel sphere with $\delta = 1/2$ gives $Z_X(1)$ equal to some explicit positive number computable from the length spectrum; there is no zero at $s = 1$ to be divided out. See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Renormalised trace and 0-determinant (funnelled case)
> **Formally:** on a non-compact hyperbolic surface, $e^{-t\Delta_X}$ is not trace-class; Melrose's compactification $\bar X$ carries a boundary defining function $x$, and the **0-trace** is $^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) := \operatorname{FP}_{z=0}\int_X x^z p(t, z, z)\,d\!\operatorname{vol}_g$ (finite part at $z = 0$). Then $\det_0\Delta_X := e^{-(\zeta^0_X)'(0)}$ from the Mellin transform of the 0-trace.
> **In words:** the renormalised determinant, defined the same way on infinite-area as on cusped surfaces — a finite-part construction that subtracts off the divergence contributed by the infinite-volume ends before applying ordinary zeta-regularisation.
> **Concretely:** on a 3-funnel sphere, $\det_0\Delta_X$ is a finite positive number computable from the length spectrum. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

---

# Statement

> **Remark (the infinite-area determinant case; Belyaev–Huseynli Remark 5.8).** When $\operatorname{Area}(X) = \infty$ (so the critical exponent $\delta < 1$), the paper's setup simplifies in two independent ways:
> - **The total Brownian loop mass is already finite** (§4 / [[Thm - Finiteness of the Total Loop Mass|Corollary 4.7]]): the Selberg-zeta sum $-\log Z_X(1)$ converges, so no renormalisation is required.
> - **$0$ is not an $L^2$-eigenvalue** of $\Delta_X$ (constants are not integrable on an infinite-area surface), so $Z_X(1) \ne 0$ and no zero must be divided out.
>
> Consequently the [[Thm - Borthwick-Judge-Perry Determinant Formula|Borthwick–Judge–Perry determinant formula]] evaluates directly at $s = 1$ without a limit, giving $\det_0\Delta_X = C_X\,Z_X(1)$ (with $C_X$ the same explicit universal constant as in the finite-area case), and the paper's loop-measure identity holds without derivative or $\log\kappa$ cancellation: $-\log\det_0\Delta_X = -\log C_X + \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\mu_X(C_X(\gamma^m))$. Lemonde–Wang [LW26] treat this case.

---

# In One Line

On an infinite-area hyperbolic surface everything is cleaner: the total loop mass is finite without killing, the Selberg zeta does not vanish at $s = 1$, and the loop-mass determinant identity holds directly at $s = 1$ — no $\kappa \to 0$ limit, no simple-zero division.

---

# Unpacking

**Why the total loop mass is already finite.** The finiteness threshold of [[Thm - Finiteness of the Total Loop Mass|Corollary 4.7]] is $s > \delta$: for plain Brownian ($\kappa = 0$, $s = 1$), the total mass is finite iff $1 > \delta$, i.e. iff $\delta < 1$, i.e. iff $X$ has infinite area. So the pathology that motivated §5 — the divergent total mass on a finite-area surface — simply does not occur in the infinite-area regime, and no killing / no renormalisation of the total is needed.

**Why $Z_X(1) \ne 0$.** On a finite-area surface, $\lambda_0 = 0$ is a genuine $L^2$-eigenvalue (constants are integrable because $\operatorname{Area}(X) < \infty$), which forces a zero of $Z_X$ at $s = 1$ (Remark 5.6, [[Remark - Why the Selberg Zeta Derivative Appears in Finite Area]]). On an infinite-area surface, $\int_X 1\,d\!\operatorname{vol} = \infty$, so constants are not in $L^2(X)$; hence $0$ is not an $L^2$-eigenvalue of $\Delta_X$, and there is no zero at $s = 1$ to cancel. The Selberg zeta at $s = 1$ is a finite positive number, and the [[Thm - Borthwick-Judge-Perry Determinant Formula|Borthwick–Judge–Perry formula]] evaluates directly there without any $\log\kappa$ dance.

**The identity, unpacked.** Substituting the [[Thm - Selberg Zeta Identity for the Total Loop Mass|Selberg zeta identity]] at $s = 1$ (which reads $-\log Z_X(1) = \sum_{\gamma,m}\mu_X(C_X(\gamma^m))$ in the infinite-area regime, since $s = 1 > \delta$) into the Borthwick–Judge–Perry formula $\det_0\Delta_X = C_X\,Z_X(1)$ gives $\log\det_0\Delta_X = \log C_X + \log Z_X(1) = \log C_X - \sum_{\gamma,m}\mu_X(C_X(\gamma^m))$, i.e. $-\log\det_0\Delta_X + \log C_X = \sum_{\gamma,m}\mu_X(C_X(\gamma^m))$ — the renormalised determinant is the total Brownian loop mass, up to the explicit constant $C_X = e^M(2\pi)^{-\chi}(\sqrt 2\,\pi)^{-n_C}$ (with no $Z_X'(1)$ derivative and no $\kappa \to 0$ limit). Lemonde–Wang cover the details in a companion work [LW26].

**Where this fits.** The paper's §5 is centrally about the finite-area case, where the total loop mass diverges and must be renormalised to $\det_0\Delta_X$ (giving [[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]]). The remark is a footnote that the infinite-area case is handled without any renormalisation apparatus — which is why the theorem is stated for the finite-area setting only. In [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6]] the finiteness of the total mass (in either regime) is what allows the loop measure to be normalised to a probability measure on homotopy classes.

---

# Where the paper uses this

Named as Remark 5.8 at the end of [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.2]], immediately before the section closes with a pointer to [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6]]. It clarifies the scope of [[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]] and the redundancy of the renormalisation apparatus in the infinite-area regime.
