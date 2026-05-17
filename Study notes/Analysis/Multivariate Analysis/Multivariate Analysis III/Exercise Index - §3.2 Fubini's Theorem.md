---
type: exercise-index
subject: multivariate-analysis
section: "3.2"
tags: [analysis, multivariate-analysis]
---

## §3.2 Fubini's Theorem — Exercises

- [[Ex - An iterated integral over a non-rectangular region]] — evaluate $\iint_T xy\,dA$ over a triangle by describing the region as "between two graphs", reading its edges $y = 0$ and $y = x$ off as the inner limits, and reducing to nested one-variable integrals; cross-checked by the other order ([[Thm - Fubini's Theorem]], [[Def - The Riemann Integral in Several Variables]], [[Def - Jordan Measure]]).

- [[Ex - Reversing the order of integration]] — evaluate $\int_0^1\int_x^1 e^{y^2}\,dy\,dx$, impossible in the given order because $e^{y^2}$ has no elementary antiderivative, by re-describing the triangular region $\{0\leq x\leq y\leq 1\}$ from the other axis so the obstructing factor becomes constant during the inner integration ([[Thm - Fubini's Theorem]], [[Def - The Riemann Integral in Several Variables]], [[Def - Jordan Measure]]).

- [[Ex - A parameter integral by differentiation under the integral sign]] — evaluate the Frullani integral $\int_0^\infty\frac{e^{-ax}-e^{-bx}}{x}\,dx = \ln(b/a)$ by treating it as a function of the parameter $b$, differentiating to cancel the obstructing $1/x$, verifying exponential domination on the unbounded domain, and solving the resulting differential equation $F'(b) = 1/b$ with the boundary value $F(a) = 0$ ([[Thm - Differentiation Under the Integral Sign]], [[Thm - Fubini's Theorem]], [[Def - The Riemann Integral in Several Variables]]).
