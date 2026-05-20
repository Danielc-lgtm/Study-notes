---
type: exercise-index
subject: multivariate-analysis
section: "1.3"
tags: [analysis, multivariate-analysis]
---

## §1.3 Higher Derivatives and Taylor's Theorem — Exercises

The exercises of §1.3 drill higher derivatives, Schwarz's theorem, and Taylor expansion. Schwarz's theorem (equality of mixed partials) requires $C^2$; without it, the classical $xy(x^2-y^2)/(x^2+y^2)$ has unequal mixed partials at the origin. Taylor expansion via known one-variable series circumvents direct partial-derivative computation. And the analyticity ladder $C^0 \supsetneq C^1 \supsetneq C^2 \supsetneq \cdots \supsetneq C^\infty \supsetneq \text{analytic}$ has strict gaps, witnessed by flat functions like $e^{-1/t}$.

- [[Ex - A function with unequal mixed partials]] (⭐⭐) — exhibit the classical function $xy(x^2-y^2)/(x^2+y^2)$ whose mixed second partials at the origin both exist but disagree ($+1$ and $-1$), computed by iterated difference-quotient limits, and trace the disagreement to the failure of the $C^2$ hypothesis — the second partials are degree-$0$ homogeneous, hence discontinuous at the origin, so Schwarz's theorem does not apply and is not contradicted ([[Def - Higher-Order Derivatives and Ck Maps]], [[Def - Partial Derivatives and the Jacobian Matrix]], [[Thm - Schwarz's Theorem on Mixed Partials]]).

- [[Ex - Second-order Taylor expansion of a function]] (⭐) — compute the second-order Taylor polynomial of $\sqrt{1+x-y^2}$ without differentiating, by substituting the polynomial argument into the one-variable binomial series and truncating at total degree two, then read off the gradient and Hessian by uniqueness of the Taylor polynomial — with care for the multi-index factorials, which make the $x^2$ coefficient $\tfrac12\partial_{xx}f$ but the $xy$ coefficient $\partial_{xy}f$ ([[Thm - Taylor's Theorem in Several Variables]], [[Def - Higher-Order Derivatives and Ck Maps]], [[Def - Directional Derivative and the Gradient]]).

- [[Ex - Real analyticity in several variables]] (⭐⭐⭐) — establish the rung above $C^\infty$: prove real-analyticity is strictly stronger than smoothness via the flat function $e^{-1/t}$ whose Taylor series converges to the wrong function, then derive and apply the factorial-rate derivative-bound criterion $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$, whose factorial is calibrated to cancel the $1/\alpha!$ in the Taylor coefficient and force the remainder to vanish geometrically ([[Thm - Taylor's Theorem in Several Variables]], [[Def - Higher-Order Derivatives and Ck Maps]]).
