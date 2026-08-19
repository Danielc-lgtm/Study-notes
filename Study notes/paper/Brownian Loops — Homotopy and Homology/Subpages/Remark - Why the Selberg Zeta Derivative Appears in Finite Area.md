---
type: remark
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Borthwick-Judge-Perry Determinant Formula"
tags: [paper, brownian-loops, spectral-geometry, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 5.6"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a geometrically finite hyperbolic surface; the case of interest here is **finite area**, i.e. $\operatorname{Area}(X) < \infty$.
- $\Delta_X$ — the positive Laplace–Beltrami operator; on a finite-area surface the constant functions are square-integrable (because $\int_X 1\,d\!\operatorname{vol} < \infty$), so **$\lambda_0 = 0$ is an $L^2$-eigenvalue** with the eigenspace spanned by constants.
- $Z_X(s)$ — the Selberg zeta function; simple zero at $s = 1$ on a finite-area surface.
- $\det_0\Delta_X$ — the renormalised (0-)determinant of $\Delta_X$ (cusped case; reduces to $\det_\zeta$ on a closed surface).
- $s = \frac12 + \sqrt{\frac14 + \kappa}$ — the spectral parameter tied to a killing rate $\kappa \ge 0$; $s = 1 \Leftrightarrow \kappa = 0$.

> [!recall]- Simple zero of $Z_X$ at $s = 1$ (finite-area case)
> **Formally:** on a finite-area hyperbolic surface, each Laplace eigenvalue $\lambda_j \in [0, 1/4)$ gives a zero of $Z_X(s)$ at $s_j = \frac12 + \sqrt{1/4 - \lambda_j} \in (1/2, 1]$, of multiplicity equal to the eigenvalue's multiplicity. Since $\lambda_0 = 0$ is an $L^2$-eigenvalue of multiplicity $1$ (the constants), $s = 1$ is a **simple zero** of $Z_X$: $Z_X(s) = Z_X'(1)(s - 1) + O((s - 1)^2)$ near $s = 1$, with $Z_X'(1) > 0$.
> **In words:** the Selberg zeta encodes the discrete Laplace spectrum through its zeros; a $\lambda = 0$ eigenvalue produces a zero at $s = 1$. So $Z_X(1) = 0$ exactly when the Laplacian has a zero eigenvalue, which is exactly when $X$ has finite area.
> **Concretely:** on a compact hyperbolic surface, $\lambda_0 = 0$ (constants integrable), so $Z_X(1) = 0$ and $-\log Z_X(s) \to +\infty$ as $s \to 1$ — this divergence is the classical fact that makes the total Brownian loop mass infinite on any finite-area surface. On an infinite-area surface with critical exponent $\delta < 1$, constants are *not* $L^2$-integrable, $0$ is not an $L^2$-eigenvalue, and $Z_X(1) \ne 0$ is a finite positive number. See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Renormalised trace and 0-determinant (cusped case)
> **Formally:** on a cusped finite-area surface, $e^{-t\Delta_X}$ is not trace-class; Melrose's compactification $\bar X$ carries a boundary defining function $x$, and the **0-trace** is $^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) := \operatorname{FP}_{z=0}\int_X x^z p(t, z, z)\,d\!\operatorname{vol}_g$ (finite part at $z = 0$). Then $\zeta^0_X(s) := \Gamma(s)^{-1}\int_0^\infty t^{s-1}(^{0}\!\operatorname{Tr}(e^{-t\Delta_X}) - P)\,dt$ (with $P$ the $L^2$-null-space projection), and $\det_0\Delta_X := e^{-(\zeta^0_X)'(0)}$.
> **In words:** the renormalised determinant on a cusped surface — the ordinary zeta-regularisation applied to a heat trace whose cusp divergence has been subtracted off. It reduces to $\det_\zeta\Delta_X$ on a closed surface.
> **Concretely:** the modular surface has one cusp and one $L^2$-eigenvalue at $0$; its 0-determinant is finite. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

---

# Statement

> **Remark (why $Z_X'(1)$, not $Z_X(1)$, appears in the finite-area answer; Belyaev–Huseynli Remark 5.6).** The finite-area version of the determinant formula ([[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]]) reads $\log\det_0\Delta_X = \log C_X + \log Z_X'(1)$ — with the *derivative* $Z_X'(1)$ on the right, rather than $Z_X(1)$. This is not a normalisation choice: it is forced by the fact that on a finite-area hyperbolic surface $0 \in \operatorname{spec}\Delta_X$, so $Z_X$ has a simple zero at $s = 1$, and that zero must be **divided out** in the definition of $\det_0\Delta_X$ (otherwise the determinant would be zero). What survives, once the zero is removed, is $Z_X'(1)$.
>
> The parallel remark for the infinite-area case ([[Remark - The Infinite-Area Determinant Case|Remark 5.8]]) is that $\lambda_0 = 0$ is *not* an $L^2$-eigenvalue, $Z_X(1) \ne 0$, and no division/derivative is needed: the identity holds with $Z_X(1)$ itself.

---

# In One Line

The derivative $Z_X'(1)$ appears because the finite-area Laplacian has $\lambda_0 = 0$ as an eigenvalue, which forces $Z_X$ to vanish at $s = 1$; the determinant is defined by dividing that zero out, and the derivative is what is left.

---

# Unpacking

**The mechanism explicitly.** The [[Thm - Borthwick-Judge-Perry Determinant Formula|Borthwick–Judge–Perry formula]] gives $\det_0(\Delta_X - s(1-s)) = Z_X(s)\,\cdot(\text{analytic non-vanishing factors})$. In the finite-area case, both sides vanish at $s = 1$: the operator $\Delta_X - 0 = \Delta_X$ has $\lambda_0 = 0$ as an eigenvalue, so any honest "determinant" of $\Delta_X$ excluding the zero mode requires *first* dividing the shifted determinant by the offending zero. Concretely, the renormalised determinant of $\Delta_X$ itself is defined by
$$\det_0\Delta_X \;:=\; \lim_{s \to 1}\;\frac{\det_0(\Delta_X - s(1-s))}{s(s - 1)}.$$
The numerator has the simple zero $Z_X(s) \sim Z_X'(1)(s - 1)$; the denominator has $s(s-1) \sim s - 1$ near $s = 1$; so the ratio limits to $Z_X'(1)\cdot(\text{analytic factors at }s=1)/1 = Z_X'(1)\cdot C_X$. Both zeros cancel, and $Z_X'(1)$ is what emerges.

**Why divide by $s(s - 1)$?** The operator $\Delta_X - s(1-s)$ becomes $\Delta_X$ at $s = 1$; its zero eigenvalue is *unshifted* from the zero mode of $\Delta_X$ (i.e. $\lambda_0 - 1\cdot 0 = 0$). To define a "determinant with the zero mode removed" — the natural analogue of the closed-surface $\det_\zeta$ which also excludes $\lambda_0 = 0$ — you must formally divide the $\det_0(\Delta_X - s(1-s))$ by the offending eigenvalue $s(s - 1)$ (which is what shifts to $0$ at $s = 1$), producing the ratio above. The change of variable $s(s-1) = \kappa$ makes the same point on the killing side: at $\kappa = 0$, the killed determinant $\det_0(\Delta_X + \kappa)$ vanishes, and one must divide by $\kappa$ (equivalently by $s(s-1)$) to get a finite answer.

**Contrast with the closed case.** On a closed surface, the Theorem 5.1(ii) $\kappa\to 0$ limit ([[Thm - Determinant as Renormalised Loop Mass]]) shows the same mechanism at the level of the loop mass: the $\log\kappa$ in $-\log\det_\zeta\Delta = -\operatorname{Area}(X)E + \log\kappa - \log Z_X(s) + O(\kappa)$ is exactly there to cancel $-\log(s - 1) \approx -\log\kappa$ coming from the expansion $-\log Z_X(s) = -\log Z_X'(1) - \log(s - 1) + O(s - 1)$. The two logarithms cancel and $\log Z_X'(1)$ survives — the same "divide out the simple zero" mechanism as here, dressed differently.

**Contrast with the infinite-area case.** When $\operatorname{Area}(X) = \infty$, constants are not $L^2$-integrable, so $0$ is not an eigenvalue; $Z_X(1) \ne 0$ (and moreover, in this regime the total Brownian loop mass is already finite, no killing needed). No division, no derivative — the formula reads with $Z_X(1)$ directly. See [[Remark - The Infinite-Area Determinant Case|Remark 5.8]].

---

# Where the paper uses this

Named as Remark 5.6 in [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.2]], immediately preceding [[Thm - Determinant via Loop Measure, Finite-Area Case|Theorem 5.7]] whose $\kappa \to 0$ limit exhibits the mechanism explicitly.
