---
type: exercise-index
subject: linear-algebra
section: "X.1"
tags: [algebra, linear-algebra, applied]
---

## §X.1 Vectors and Linear Functions — Exercises

The exercises of §X.1 drill the core distinction between linear and affine functions in applied modelling: when does a real-world dependence pass through the origin (linear), and when does it have an offset (affine)? The exercises also rehearse the basic moves of recognising an inner product, identifying a regression model's linear part and offset, and applying the homogenisation trick to absorb an offset into an augmented input. The targets are: (a) classify whether a given function is linear, affine, or neither; (b) extract the inner-product representation of a linear function or the matrix-plus-offset representation of an affine function; (c) recognise the practical importance of the constant-feature trick for applied modelling.

- [[Ex - Regression model as an affine function]] (⭐) — verify directly that the regression formula $\hat y(x) = x^T \beta + v$ is affine but not linear when $v \neq 0$, and apply the homogenisation trick to express it as a single inner product ([[Def - Affine and Linear Functions on Rn]])
- [[Ex - Triangle inequality for the Euclidean norm]] (⭐) — prove the triangle inequality by squaring norms and applying Cauchy–Schwarz to the cross term, and identify the equality case as alignment ([[Def - Norm and Distance]], [[Thm - Cauchy-Schwarz and the Angle in Rn]])
- **(Boyd Ex 2.1)** Determine whether the following functions $\mathbb R^n \to \mathbb R$ are linear, and if so give their inner-product representations: (a) the spread $f(x) = \max_k x_k - \min_k x_k$; (b) the difference $f(x) = x_n - x_1$; (c) the median of $x$ (with $n$ odd); (d) the average of odd-indexed entries minus the average of even-indexed entries. The exercise teaches recognition of linear functions in concrete formulas. (⭐, [[Def - Affine and Linear Functions on Rn]])
- **(Boyd Ex 2.2)** Processor power and temperature: from measurement data on the temperature rise of a three-processor system under different power loads, derive the affine function $T = a^T P + b$ relating power to temperature, using the affine-representation extraction $a_i = T(e_i) - T(0)$, $b = T(0)$. (⭐, [[Def - Affine and Linear Functions on Rn]], [[Def - Taylor Approximation (Boyd)]])
- **(Boyd Ex 2.9)** Compute the Taylor approximation of $f(x_1, x_2) = x_1 x_2$ at the expansion point $z = (1, 1)$, and evaluate the approximation error at $x = (1.05, 0.95)$ and $x = (0.85, 1.25)$. Compare to the exact value. (⭐, [[Def - Taylor Approximation (Boyd)]])
