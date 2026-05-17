---
type: exercise-index
subject: multivariate-analysis
section: "3.3"
tags: [analysis, multivariate-analysis]
---

## §3.3 The Change of Variables Formula — Exercises

- [[Ex - The Gaussian integral via polar coordinates]] — evaluate $\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt\pi$ by squaring it into a double integral, recognizing the radial symmetry of $e^{-x^2-y^2}$, switching to polar coordinates so the Jacobian factor $r$ makes the radial integral elementary, and handling the non-injective polar seam as a nil set ([[Thm - The Change of Variables Formula]], [[Thm - Fubini's Theorem]], [[Def - The Riemann Integral in Several Variables]]).

- [[Ex - The volume of the n-dimensional ball]] — derive $V_n = \pi^{n/2}/\Gamma(n/2+1)$ for the unit ball by two routes: a Fubini slicing recursion using linear scaling of cross-sections, and a closed-form route equating two evaluations of the Gaussian integral $\int_{\mathbb{R}^n}e^{-|x|^2}$ — one by Fubini, one by the radial change of variables exposing $V_n$ as a coefficient ([[Thm - The Change of Variables Formula]], [[Thm - Fubini's Theorem]], [[Ex - The Gaussian integral via polar coordinates]], [[Def - The Riemann Integral in Several Variables]]).

- [[Ex - A nonlinear change of variables]] — evaluate $\iint_P(x+y)^2\,dA$ over a parallelogram by the substitution $u = x+y$, $v = x-y$ chosen so the region's edges become coordinate lines and $P$ becomes a rectangle, inverting the map to obtain the diffeomorphism, computing the Jacobian factor $\tfrac12$, and finishing with Fubini ([[Thm - The Change of Variables Formula]], [[Thm - Fubini's Theorem]], [[Def - The Riemann Integral in Several Variables]]).
