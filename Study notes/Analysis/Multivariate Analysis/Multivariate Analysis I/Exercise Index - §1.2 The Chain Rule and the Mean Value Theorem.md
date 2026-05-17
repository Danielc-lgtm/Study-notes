---
type: exercise-index
subject: multivariate-analysis
section: "1.2"
tags: [analysis, multivariate-analysis]
---

## §1.2 The Chain Rule and the Mean Value Theorem — Exercises

- [[Ex - The chain rule through a coordinate change]] — express a function in polar coordinates by composing it with the polar map, and use the chain rule $J(g\circ\Phi) = Jg(\Phi)\cdot J\Phi$ to relate the polar partials to the Cartesian partials, then invert the polar Jacobian (legal since $\det J\Phi = r \neq 0$) to recover the Cartesian gradient from polar data ([[Thm - The Chain Rule]], [[Def - Partial Derivatives and the Jacobian Matrix]], [[Def - Directional Derivative and the Gradient]]).

- [[Ex - Bounding a map with the mean value inequality]] — show an explicit trigonometric map with a $\tfrac14$ prefactor is a contraction: bound the operator norm of its Jacobian by $\tfrac12$ through the dominating Hilbert–Schmidt norm, feed that uniform bound into the mean value inequality on the convex domain $\mathbb{R}^2$, and deduce uniqueness of fixed points and the Cauchy property of the iteration sequence ([[Thm - The Mean Value Inequality]], [[Def - The Total Derivative and Differentiability]], [[Def - Partial Derivatives and the Jacobian Matrix]], [[Thm - Continuous Partials Imply Differentiability]]).

- [[Ex - Differentiating a function constant along curves]] — prove that a differentiable function on the punctured plane is rotationally symmetric if and only if its gradient is everywhere radial, by differentiating the constancy relation along a circular curve with the chain rule (forward direction) and integrating a vanishing circular derivative back via the constancy corollary of the mean value inequality (converse direction) ([[Thm - The Chain Rule]], [[Thm - The Mean Value Inequality]], [[Def - Directional Derivative and the Gradient]]).
