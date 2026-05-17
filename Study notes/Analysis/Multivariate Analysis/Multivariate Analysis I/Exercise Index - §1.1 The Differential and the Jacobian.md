---
type: exercise-index
subject: multivariate-analysis
section: "1.1"
tags: [analysis, multivariate-analysis]
---

## §1.1 The Differential and the Jacobian — Exercises

- [[Ex - A function differentiable but not continuously differentiable]] — separate the upper gap of the regularity ladder: build a function (the two-variable promotion of $x^2\sin(1/x)$) that is differentiable everywhere but whose partial derivative is discontinuous, so the converse of "continuous partials imply differentiability" fails; differentiability at the origin is checked directly from the $o(|h|)$ definition while the partial is shown to oscillate without limit ([[Def - The Total Derivative and Differentiability]], [[Def - Partial Derivatives and the Jacobian Matrix]], [[Thm - Continuous Partials Imply Differentiability]], [[Thm - Differentiability Implies Continuity]]).

- [[Ex - Partial derivatives exist without differentiability]] — separate the lower gap of the regularity ladder: show $xy/\sqrt{x^2+y^2}$ has both partials at the origin and is continuous there yet is not differentiable, by computing the directional derivative in a general direction and exhibiting its non-linearity in the direction — the obstruction that survives when the discontinuity obstruction is unavailable ([[Def - The Total Derivative and Differentiability]], [[Def - Partial Derivatives and the Jacobian Matrix]], [[Def - Directional Derivative and the Gradient]], [[Thm - Differentiability Implies Continuity]]).

- [[Ex - The Jacobian of polar coordinates]] — compute the Jacobian matrix of the polar-coordinate map $(r,\theta)\mapsto(r\cos\theta, r\sin\theta)$ and its determinant $r$, certifying differentiability through continuity of the partials, and interpret the determinant as the local area-scaling factor that becomes the weight $r\,dr\,d\theta$ in the change-of-variables formula ([[Def - Partial Derivatives and the Jacobian Matrix]], [[Def - The Total Derivative and Differentiability]], [[Thm - Continuous Partials Imply Differentiability]]).
